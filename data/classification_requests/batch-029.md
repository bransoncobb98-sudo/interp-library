# Classification request: batch 29 of 53 (40 records, IC-1521 to IC-1560)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-029-reply.json`.

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

## IC-1521: Broken – A Collection in Memory of Matthew Shepard

- Title: Broken – A Collection in Memory of Matthew Shepard
- Author (byline): Leslea Newman, Rachel Hadas, Beatrix Gates and Patricia Spears Jones
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 780
- Already set (do not supply): none

### Source block (context only)

```text
Author: Leslea Newman
Book: October Mourning: A Song for Matthew Shepard
ISBN: 978-0763658076
Publisher: Candlewick
Date (Month/Year): Sept 2012
Poems:
• What You Can Do in Eighteen Hours
• Once Upon a Time
• Wounded
• Frat Boys
Author: Scott Gibson (Editor)
Book: Blood & Tears: Commemorative Poems for
Matthew Shepard
ISBN: 978-1891305153
Publisher: Painted Leaf Press
Date (Month/Year): June 1999
Poems:
• The Fence by Rachel Hadas
• Seeking Tenderness by Beatrix Gates
• My Matthew Shepard Poem by Patricia Spears
Jones
```

### Introduction (context only: never use it for content warnings)

```text
On October 6, 1998, Aaron McKinney and Russel Henderson savagely beat Matthew Shepard, lashed him to a fence, and left him to die for no reason other than his sexual preference. And the nation was shocked . . . But it was obviously an isolated incident, or so it was claimed.

Now more than 20 years later, our society has become jaded to violence and suffering. Another school shooting? More immigrants denied asylum? Another unarmed black, or Asian or homosexual murdered? Thoughts and prayers

(beat) and we move on.

But these are not isolated incidents . . . they happen because our society is . . . Broken – A Collection in Memory of Matthew Shepard by Leslea Newman, Rachel Hadas,
```

### Performance text (classify this)

```text
What You Can Do in 18 Hours by Leslea Newman (Pg 17) Write a term paper Cram for a final

Fly across the ocean Drive cross-country

Scale a mountain Run a marathon

See the moon disappear Watch the sun rise and set

Wait to be discovered lashed to a fence

Shivering under a blanket of stars Beatrix Gates and Patricia Spears Jones

The Fence by Rachel Hadas
(Pg 52) How does justice work?
Punishment? Revenge?
Is one life worth
more than another?
No one to see
whose tears washed two paths
clean on his bloody face,
who stood, wrists bound
(the ropes, a sheriff said,
almost too tight to cut),
tied to a fence under the autumn sky
as night turned into day.
No one nearby.
No one to say
whose enemy he was,
whose prey, and why.

Seeking Tenderness by Beatrix Gates

(Pg 35) [But] Stories walk backwards out of the split-rail lodgepole pine, the deer fence where you hung . . .

TRANSITION

And if we trace the story back . . . Aaron McKinney and Russell Henderson were products of the society that raised them. The boys who hung Matthew’s broken body (crucified not with nails but with rope) to a fence, were sentenced to life behind bars. And society brushed off its culpability, sighed and moved on . . .

(Pg 36) Someone said that Aaron, like a lot of people who

talk a lot,
had nothing to say, that his friends called him a shrimp,
just bullied him around,
“He wasn’t the mean guy,”
one said, “he was just Aaron, the little guy.”

Once Upon a Time by Leslea Newman (Pg 81) (in Aaron’s voice) “I don’t like gay people. As far as Matt is concerned, I don’t have any remorse”

Seeking Tenderness by Beatrix Gates

(Pg 37) (in the landlady’s voice)
“Russell’s about the most American
kid you can get. He’s a pizza-eating, beer-drinking,
fishing, hunting, work-on-your-car
type of kid – just regular,” his landlady said.

Wounded by Leslea Newman

(Pg 78) (In Russell’s voice) “You know, my mom was killed in Laramie. She was raped, and then the guy just left her on the side of the road.”

TRANSITION

Matthew was taken to Poudre Valley Hospital in Fort Collins, Colorado, where he died six days later. And that Saturday afternoon, a few blocks from his hospital bed, it was a celebration: The Colorado State University homecoming parade. Spirits were high and the floats were spectacular. Well, except for the Wizard of Oz float . . . Our society is broken.

The Frat Boys by Leslea Newman
(Pg 51) Hey, wouldn’t it be funny
Hey, wouldn’t it be hysterial
Hey, wouldn’t it be a riot

to make our scarecrow the scarecrow on our float the scarecrow on our homecoming float

look like a homo look like a queer look like a freakin’ fairy?

Hey, that would be funny
Hey, that would be hysterical
Hey, that would be a riot
Like that fag from Wyoming
that fag they tied to the fence
that fag they thought was a scarecrow

Seeking Tenderness by Beatrix Gates (Pg 39) The cyclist who found Matthew Shepard thought he was a scarecrow until he saw the human hair.

The Frat Boys by Leslea Newman
(Pg 51) Let’s write I LIKE BOYS on his shirt
Let’s write I’M GAY on his hat
Let’s write I LOVE DICK on his pants

Hey, that’s really funny Hey, that’s really hysterical Hey, that’s really a riot . . .

Hey, that’ll knock ‘em dead My Matthew Shepard Poem by Patricia Spears Jones

(Pg 65-66) What I know about America is that hatred crawls through the culture like the cracks in the San Andreas fault.

Edifices are built to withstand the inevitable
quakes, but the quakes grow stronger.
Whatever we dream -- harmony or a reasonable tolerance -
-- is destroyed in the wake

of men drinking and killing. Their blood lusted laughter howling through the night.

A Black man in Texas. A white man in Wyoming. A doctor at his window about to eat dinner with his family. A nurse on her way to work at a clinic.

The playing field is not level. In fact, there is no playing

field. There are men enraged by change. And women bitter

about it.
And people, say
gay, Black, Latino, Chinese, Japanese, Arab, or Jewish
to blame, always to blame.

The ugly men in their same wool suits and striped ties gibber political correctness, freedom, fairness every time they claim that these are acts of individuals, not of society.

*According to“The Crucifixion of Matthew Shepard” by Melanie Thernstrom, published in Vanity Fair, March 1999. “On Saturday afternoon, a few blocks from the hospital bed where Matthew’s parents were keeping vigil, a Colorado State University homecoming parade passed by. ON a Wizard of Oz float sponsored by the Pi Kappa Alpha fraternity and Alpha Chi Omega sorority, the scarecrow character had been defaced. Scrawled in black spray paint was I’M GAY, as well as anti-homosexual obscenities.”
```

---

## IC-1522: Buddy Wakefield Collection

- Title: Buddy Wakefield Collection
- Author (byline): Buddy Wakefield
- Work: Stunt Water
- Publisher: Write Bloody Publishing
- Publication date as stated: Oct 2015
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1427
- Already set (do not supply): none

### Source block (context only)

```text
Author: Buddy Wakefield
Book: Stunt Water
ISBN: 978-1938912603
Publisher: Write Bloody Publishing
Date (Month/Year): Oct 2015
```

### Introduction (context only: never use it for content warnings)

```text
In an interview in 2012, Buddy Wakefield explained his motivation for writing poetry: “[It’s] the reflection. The intention. The idea that someone who had a similar starting point will recognize my writing on the wall as their own, and they will trust it to walk from the bottom of the barrel out.”

See, Buddy Wakefield spent a lifetime of overcompensating for a lack of masculinity. He grew up queer in the south and experienced public shame first-hand. And still -- despite his fear of intimacy, he (like we all do) searched for that special someone, and he (like we all have) survived the devastation of a failed major relationship. Gay or straight we all seek connection, we all seek love.

Giant Saint Everything and Hurling Crowbirds at Mockingbars by Buddy Wakefield
```

### Performance text (classify this)

```text
Giant Saint Everything
There were days I wanted out.
But then You would go and do things
like dive into the Vancouver ocean,
big brilliant cliché poem that You are,
water rolling off Your back
as You swam toward a sunset
that hung like a sacred recipe painted
all the way around Your holy head.

And then there were the ways You caught me moving back into my cave where the wheels turn, same wheels that drove You off. I should have told You before talking in terms of Forever that any given day wears me out and works me sour, that there are nights when the sky is so clear I stand obnoxious underneath it begging for the stars to shoot at me just so I can feel at Home.

What’s left of You now is a shrine
built from the pieces I kept of Your presence,
Your incredible stretch of presence.
It sits in Our room like a sandpiper
cross-legged and crying,
remembering the night we met
and the day You left, and the Light
shifting in between.
By the side of it stands a picture of the poem where I

promised, “You will never have another lonely holiday.”

The words “I Promise” and “Forever”
begged me not to use them
but sometimes I don’t listen to God,
so You can imagine how much it hurt
to let Your last birthday pass
with no word. On August 3rd.
You weren’t the only one comin’ up lonesome.

Listen, if I had to make a list
of everything everywhere
- and I mean everything… everywhere -
the very last to-do on that infinite list of
every – single – thing – would be – to hurt You,
so I need You to know
that in an attempt to keep my promise
I did write a letter to You on Your birthday.

It was covered in stickers of flock-printed stars, choir claps, and a bonfire of buttercups stuck in the air, but when I finally drew enough courage to send You all the Love in the World my hand snapped off in the mailbox from clenching.

It was returned to me with a gospelstitch, a hope stamp and a note etched into the palm I had to pry open with the pressure of pitching doves reminding me we agreed to let each other go.

There is a point when tears don’t work
to wash things away anymore.
Grabbing for breath has now broken my fingers.
I miss You so much some days
that I beg for the airplane to crash
with just enough time in the freefall
for scribbling “I Love You” across my chest.
That way – when they find my burning breast plate –
they will tell You how the very last thing I did with my

life was call out Your name.

Arnold Remond Liesting (A.R.L)

I know You’re momma didn’t raise a sissy, so it’s best if I believe that You’ve bounced back and been born again, but, Baby,

in the bottom left corner of dreams
in the dark spot
where it gets windy and hollow
I can still see you flailing,
eating knuckle cake,
full torque and tender,
heart pounding from being pulled under,
feet bleeding from bracing for endings,
tongue dying to curse Forever
because promises murder us backwards
when people like me don’t keep them.

And sure, we all deserve absolution,
but especially You. You and Faith,
You’ve got the same hungerpunch, same song
still rising off the watertrain running through the laws
of a moon dead set on daylight
digging marbles from the trees
in a Love not scared to make no sense
and monkey enough to see
the same devastating reason for living this life:
My Giant
Saint
Everything

I promise You. Forever.

These words have buckled my lips
so far back to the beginning
that I am now allowed only Today,
So today, from my snap-chested heart spraying
fully flying
sending out the birds:
Today I stop believing in words.
Today all my visions reverted blurs
like the night We saw the Light
and I could not shut up

but I swear I was feelin’ silence.

HURLING CROWBIRDS AT MOCKINGBARS (HOPE IS NOT A COURSE OF ACTION)

If we were created in God’s image
then when God was a child
he smushed fire ants with his fingertips
and avoided tough questions.
There are ways around being the go-to person
even for ourselves
even when the answer is clear
like the holy water Gentiles drank
before they realized Forgiveness
is the release of all hope for a better past.

I thought those were chime shells in your pocket so I chucked a quarter at it hoping to hear some part of you respond on a high note. You acted like I was hurling crowbirds at mockingbars and abandoned me for not making sense. Evidently, I don’t experience things as rationally as you do.

For example, I know mercy when I have enough money to change the jukebox at a

gay bar
(somebody’s gotta change that).
You understand the power of God’s mercy
whenever someone shoves a stick of morphine
straight up into your heart.
It felt amazing
the days you were happy to see me

so I smashed a beehive against the ocean
to try and make our splash last longer.
Remember all the honey
had me lookin’ like a jellyfish ape
but you walked off the water in a porcupine of light
strands of gold
drizzling out to the tips of your wasps.
This is an apology letter to the both of us
for how long it took me to let things go.

It was not my intention to make such a
production of the emptiness between us
playing tuba on the tombstone of a soprano
to try and keep some dead singer’s perspective alive.
It’s just that I coulda swore you had sung me a love song

back there
and that you meant it
but I guess sometimes people just chew with their
mouth open

so I ate ear plugs alive with my throat hoping they’d get lodged deep enough inside the empty

spots
that I wouldn’t have to hear you leaving
so I wouldn’t have to listen to my heart keep saying
all my eggs were in a basket of red flags
all my eyes to a bucket of blindfolds
in the cupboard with the muzzles and the gauze
ya know I didn’t mean to speed so far out and off
trying to drive all your nickels to the well
when you were happy to let them wishes drop

but I still show up for gentleman practice
in the company of lead dancers
hoping their grace will get stuck in my shoes.
Is that a handsome shadow on my breath, sweet woman
or is it a cattle call
in a school of fish? Still dance with me
less like a waltz for panic
more for the way we’d hoped to swing
the night we took off everything
and we were swingin’ for the fences

don’t hold it against
my love
you know I wanna breath deeper than this
you know I didn’t mean to look so serious
didn’t mean to act like a filthy floor
didn’t mean to turn us both into a cutting board
but there were knives s-stuck
in the words where I came from
too much time in the back of my words.
I pulled knives from my back and my words.
I cut trombones from the moment you slipped away

and I know it left me lookin’ like a knife fight, lady yeah you know it left me feelin’ like a shotgun shell you know I know I mighta gone and lost my breath but I wanna show ya how I found my breath to death it was buried under all the wind instruments hidden in your castanets goddamn if ya ever wanna know how it felt when ya left yeah if you ever wanna come inside

just knock on the spot

where I finally pressed STOP

playing musical chairs with exit signs.

I’m gonna cause you a miracle when you see the way I kept God’s image alive.

Forgiveness is for anybody who needs a safe passage through my mind.

If I was really created in God’s image
then when God was a boy
he wanted to grow up to be a man
a good man
and when God was a man
a good man
He started telling the truth in order to get honest
responses.
He’d say,
“I know.
I really shoulda wore my cross
again
but I don’t wanna scare the gentiles off.”
```

---

## IC-1523: The Bully

- Title: The Bully
- Author (byline): Cheryl Costello-Forshey
- Work: Chicken Soup for the Teenage Soul IV
- Publisher: HCI Teens
- Publication date as stated: 2004
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1090
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cheryl Costello-Forshey
Book: Chicken Soup for the Teenage Soul IV
ISBN: 978-0757302336
Publisher: HCI Teens
Date (Month/Year): 2004
```

### Introduction (context only: never use it for content warnings)

```text
We have a bullying problem in America. -- at schools, work, government, police departments, everywhere. It’s a problem that becomes a little less obvious after middle and high school, true. But bullying never really goes away.

And what’s worse is that bullying today usually isn’t conducted in secret, but up front and in the open with a gaggle of spectator observing. Take President Trump for example. He has racked up dozens of controversial comments targeting Muslims, disabled people and especially women. He often employs crass language. Is this bullying? YES! But while President Trump’s remarks have shocked and offended millions, they have also attracted large numbers of supporters who find his bullying tactics refreshing.

Let’s face it people. Words matter. They matter in elementary school, they matter in high school and they matter in the adult world. And the longer we stand by and accept the behavior of bullies, the more damage will be done to our society.

Cheryl Costello-Forshey examines this issue in her poem, The Bully.
```

### Performance text (classify this)

```text
He rages from within, his eyes fixed in a stare, Anxious for a fight, with whom he doesn’t care. His heart is filled with anger, his fists clenched in a ball, Eager to ruin someone’s day, as they hurry down the hall. Who shall be his victim, there are many he can choose, The girl with braces on her teeth, the kid in school who’s

new. To him they’re all the same, how he longs to make them

cry, And as the anger builds within, his classmates scurry by. And then he sees around the corner, the shortest boy in

class, Should he be his victim, he wonders when he teased him

last.
He doesn’t quite recall, he really doesn’t care.
His choice is finally made, because the boy is there.
So he calls out nasty names, as the boy dares to hurry

by, A boy who’s done nothing wrong, just merely wondering

why. Why he’s being teased, why won’t anyone step in?

He’s terrified of fighting back; there’s no doubt he’d

never win.

And there stands in the doorway, a teacher in plain view, Who merely shakes his head, for what else can he do? He’s simply there to teach, the boys aren’t in his class, Teasing is a apart of life; it’s a phase he knows will pass. So the bully is the victor, his places has well been

earned, The lesson no one taught him, is one he’ll never learn To a teacher, he’s merely trouble, to the kids he’s to be

feared, To his alcoholic father, he’s a mistake and wasted years. He’s headed for a jail term; his life cannot be saved, His problems are his own; his path to crime is paved. So there he stands so angry, his back against the wall, Begging for attention, by making others small.

Standing on a corner, traffic whizzing by, He yells out to the world, angry clouds roll through the

sky.

His displeasure is apparent, his fists clenched so ever

tight Who shall be his victim, on this fast approaching night? There are many he can choose from; they all deserve his

rage, To him the world’s just an act, he longs for center stage. And then he spies that tired old man, with groceries in

his hand, At last he’s found his victim, he proceeds without a plan. He calls out angry threats, as the old man stumbles by, One who’s done nothing wrong, just merely wondering

why? Why he’s being cursed at, why won’t anyone step in, He’s terrified of fighting back; there’s no doubt he’d

never win.

And there stands in the doorway, a grocer in plain view, Who merely shakes his head, for what else can he do? The man is not his father; the boy is not his son, Words are nothing more than that, the boy’s just having

fun.

So the bully is the victor, his place has well been earned, The lesson no one taught him, is the one he’ll never learn. To the grocer he’s merely trouble, to the old man he’s to

be feared. To his alcoholic father, he’s a mistake and wasted years. He's headed for a jail term; his life cannot be saved, His problems are his own; his path to crime is paved. So there he stands so angry, his back against the wall, Begging for attention, by making others small. Drunk and with a shotgun gripped within his hand, Hidden in the shadows, by a station where he stands. He watches cars pull in and out, customers walking to

and fro, Staring past their faces, as they rush past him on the

go. Who shall be his victim, on that robbery barely planned, There are many he can choose from, their lives so close

at hand His heart beats out in anger; his brow is damp with

sweat, He has to win this game; the rules have long been set.

He sees her through the window, of her bright and shiny

car, The east perfect target, his plan will take him far. He hurries to the car door, he forces himself inside, The shotgun near her head, as she begs him for her life. But they are merely words; they do not faze his ears, Her life is unimportant; he mocks her many tears. And somewhere in the struggle, her screams pierce

throughout the air, She is just another victim, why, because she’s there.

And there stands in the doorway, a mechanic in plain

view, Watching as the man drives away, what else can he do? The girl is not his daughter; the boy is not his son, He could not risk his own life, to stop a stranger with a

gun. The papers showed his picture, his face glorified across

the screen. To the world he was a loser, to himself he’d found his|

dream.

For at last somebody noticed, the boy with all that rage, At last he found an audience, there from center stage. So the bully was the victor, his place had well been

earned, And the lesson no one taught him, someone else was

forced to learn. For somewhere in the world, the shortest boy in class, Stands there on the corner, watching everybody pass. His anger overflowing, poison in his heart, Getting even for his torment, seems the perfect place

to start. And elsewhere on the sidewalk, creeps a feeble man, For his own protection, a weapon in his hand. Watching every single person, who quickly passes by, His heart no longer frightened, he’s no longer asking

why. For inside he knows the answer, as does the smallest boy

in class, Words ignite an anger, whose meaning may not pass. But perhaps the biggest lesson, that stands out from

the rest, Has been forced upon a mother, who wonders what lies

next. As she stands there at the gravesite, where he only

daughter lay, Wondering about the horrible events, that led her to

that day. What caused a child so young, only sixteen years of age, To be filled with so much anger, to internalize such rage. That he would kill her daughter, so young and full of life, Didn’t anyone ever take the time, to teach him wrong

from right? To his father he was nothing; his life at home was fear, And from his drunken father, came a message very

clear. Words that wreaked their damage, that no one cared to

see, The day a good-for-nothing boy, became what they said

he’d be.
```

---

## IC-1524: Butcher (Poems from)

- Title: Butcher (Poems from)
- Author (byline): Natasha T. Miller
- Work: Butcher
- Publisher: Button Poetry
- Publication date as stated: Feb 2021
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1079
- Already set (do not supply): none

### Source block (context only)

```text
Author: Natasha T. Miller
Book: Butcher
ISBN: 978-1943735907
Publisher: Button Poetry
Date (Month/Year): Feb 2021
```

### Introduction (context only: never use it for content warnings)

```text
Poems from Butcher by Natasha T. Miller in tribute to the death of her brother.
```

### Performance text (classify this)

```text
The Playground is Empty (pg 34) When my city turned dark & into a playground full of ghosts, we stayed, climbed the polls, turned the lights back on ourselves, & made so much noise that the rest of the world had to come back to see what was happening.

Two days after my brother died, I peeled myself out of bed to go teach poems to tenth graders, & a week later a girl who had just lost her mother left a note on my desk that only read: “thank you, thank you.”

It was in that moment I understood,
success is not about money or a bottom line;
success is sometimes just the lifeline
between your journey and how your story
can inspire or save someone else.

Family Reunion (pg 8-9)
The day after the dead
dies it’s a family reunion
the day after the dead is buried
it’s a death

And you have to go to work tomorrow because
bereavement days last the same amount of time whether
you just buried your dog or
your only brother or
lost them both
and buried them right next to each other

And you have to iron your clothes now
when they can no longer see your wounds
they expect you to no longer look like s***
the obituary is already wrinkled
you start to feel like you should be
straightened out by now
It’s not like he just died yesterday
it’s not like people are still calling to see if you’re okay

You should be able to rest now
you’re not dreaming bout him anymore
because even the dead can feel when they’re old news
when their sons have stopped asking
when they’re coming back home
when the rest in peace shirts are too faded to remember
who you were remembering

Who were you remembering?

How long has it been since their profile became just another picture at the bottom of a police file since their dirty clothes at the bottom of your hamper stopped smelling like all the trouble you tried to pray them away from

How long has it been since your friends stopped
by the house with flowers for your mother
listened to you repeat the same stories
laughed and engaged as if it was the first time they’ve
heard that name in years
How long has it been?

How many days does it take for a death to stop feeling like a family reunion for you to feel alone

Like an only child like you’ve lost something you love and you can feel it now?

TRANSITION

Grief and an overwhelming sadness: These are undeniable emotions when faced with mortality. But Natasha T. Miller is dealing with more than just the loss of her brother. She continues to deal with the circumstances surrounding his death. See he didn’t die in an accident, or from some unresolved medical condition. He died because of the lifestyle he chose. His name was Marcus, but they say . . .

They Say (pg 47) They say you shouldn’t mourn the loss of a drug dealer. Say the drug dealers stood on the tracks their whole lives. Challenging the train. Knew that even if the weather delayed it death was still. Showing up at their front door. They say the drug dealer died so casually. Say what’s-his-name’s-child on Joy Road or Rosa Parks Blvd, was murdered in cold blood. On his front porch. They say his. Don’t say his name. Don’t care about the death of a dealer. They don’t give the drug dealer a backstory or a reason why. He’s just another one. They say his. Don’t say his name. Say his funeral is next week. Don’t talk about who he was. They say his casket was nice. Say his mother was nice. Was burying her only son and still. Had enough strength to stand outside the church and laugh. Don’t say his name. Treat it like a weight their fragile tongues are too weak to hold. Don’t wanna make the mistake of humanizing the drug dealer. Can’t let anyone know they gave a damn. They say his death. I say his death. I say his in every conversation since he left. It’s been 1,956 days since my brother was murdered. I haven’t said his name once. I say my brother in every conversation since his death. I say his death. I say his. I say his death. I say his. See I’m afraid the more times I say his name. The quicker I’ll empty myself of his memory. I’m scared of remembering what his name tastes like. Afraid it’ll fall like ashes in my mouth. Buried underneath my tongue. My lips into a headstone. That forces me to talk about him. To stop saying his. To say his name. To say Marcus. To say Marcus. To say my brother. His name was. Marcus.

Your Son’s Smile (pg 39) You tryna make me believe you some type of Jesus

Like you weren’t just another Black man With no father

Bad Habits An untimely death

And a sister that won’t forget about you

Your mama’s addiction Your father’s regret

You deserved this life as much as anyone else You didn’t start this war on drugs

You were a casualty in it.

I Learned of Grief Too Late (pg 55-56) Grief is more contagious than joy

It seems easier to hand our baggage
to people we love than move
through the world freely
It’s the reason I left my mother
at home to mourn the death of her only
son alone while I went on the road
to perform poems for strangers

Because hurt people hurt people is so damn cliché but true

So you blame anything on the dead

You become the excuse and the excused, The burning building and the fire, expecting to be rescued while left alone

Until you’re left alone and can no longer blame your behavior on your pain

Until you hear someone you love say they can’t forgive you and feel success and emptiness in the same body

Until you’re humbled until you realize that you’re not the only one

We are all hurting and as a result, all hurting each other.

Until you learn to be grieving and gracious

Until you learn that this s*** is never just about you.

To Existing Being Enough (pg 22) On days like today, you’re just existing, and that’s fine.

The ocean is not always a tsunami. The wind is not always a tornado.

You are no less powerful in all your stillness.
```

---

## IC-1525: The Butter Battle Book

- Title: The Butter Battle Book
- Author (byline): Theodore Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House, Inc.
- Publication date as stated: March 1984
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1440
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
The pettiness behind the conflict of the Cold War is Dr. Seuss's vehicle for conveying the astounding destructive potential behind a war where the enemies lose sight of their true goals and meaninglessly try to "out do" each other. The “war” ends up being fought for the wrong reasons and becomes something that we will forever regret. While the arms race between the United States and Russia no longer exists, The Butter Battle Book by Theodore Geisel (aka Dr. Seuss) still explores the important issue of escalating violence and the "an eye-for-an-eye" mentality that not only exists at an international level but also in the cities, schoolyards, and homes of some to this day. The Butter Battle Book by Theodore Geisel (aka Dr. Seuss)
```

### Performance text (classify this)

```text
On the last day of summer, ten hours before Fall… my grandfather took me out to the wall.

For a while he stood silent. Then finally he said, with a very sad shake of his very old head, “As you know, on this side of the Wall we are Yooks. On the far other side of this Wall live the Zooks.”

Then my grandfather said, “It’s high time that you knew of the terribly horrible thing that Zooks do. In every Zook house and in every Zook town every Zook eats his bread with the butter side down!”

“But we Yooks, as you know, when we breakfast or sup, spread our bread,” Grandpa said, “with the butter side up. That’s the right, honest way!” Grandpa gritted his teeth. “So you can’t trust a Zook who spreads bread underneath! Every Zook must be watched! He has kinks in his soul! That’s why, as a youth, I made watching my goal, watching Zooks for the Zook-Watching Border Patrol!

In those days, of course, the Wall wasn’t so high and I could look any Zook square in the eye.

If he dared to come close I could give him a twitch with my tough tufted prickely Snick-Berry Switch.

For a while that worked fine. All the Zooks stayed away and our country was safe. Then one terrible day a very rude Zook by the name of VanItch snuck up and slingshotted my Snick-Berry Switch!

With my broken- off switch, with my head hung in shame, to the Chief Yookeroo in great sorrow I came. But our leader just smiled. He said, “ You’re not to blame. And those Zooks will be sorry they started this game.

“We’ll dress you right up in a fancier suit! We’ll give you a fancier slingshot to shoot!” And he ordered the Boys in the Back Room to figger how to build me some sort of triple-sling jigger.

With my Triple-Sling Jigger I sure felt much bigger.

I marched to the Wall with great vim and great vigor, right up to VanItch with my hand on the trigger. “I’ll have no more nonsense,” I said with a frown, “from Zooks who eat bread with the butter side down!”

VanItch looked quite sickly. He ran off quite quickly.

I’m unhappy to say he came back the next day in a spiffy new suit with a big new machine, and he snarled as he said, looking frightfully mean, “You may fling those hard rocks with your Triple-Sling Jigger. But I, also, now have my hand on a trigger!

“My wonderful weapon, the Jigger-Rock Snatchem, will fling ‘em right back just as quick as we catch ‘em. We’ll have no more nonsense. We’ll take no more gupp from you Yooks who eat bread with the butter side up!”

“I have failed, sir,” I sobbed as I made my report to the Chief Yookeroo in the headquarters fort. He just laughed. “You’ve done nothing at all of the sort. Our slingshots have failed. That was old-fashioned stuff. Slingshots, dear boy, are not modern enough.

“All we need is some newfangled kind of gun. My Boys in the Back Room have already begun to think up a walloping whiz-zinger one! My Bright Boys are thinking. They’re on the right track. They’ll think one up quick and we’ll send you right back!”

They thought up a great one! They certainly did. They thought up a gun called the Kick-a-Doo Powder and ant’s eggs and bees’ legs and dried-fried clam chowder. And they carefully trained a real smart dog named Daniel to serve as our country’s first gun-toting spaniel.

Then Daniel, the Kick-a-Poo Spaniel, and I marched back toward the Wall with our heads held up gigh while everyone cheered and their cheers filled the sky; “Fight! Fight for the Butter Side Up! Do or die!”

Well . . .

We didn’t do. And we didn’t quite die. But we sure did get worsted, poor Daniel and I. VanItch was there too! And he said, the old pig, “The Boys as in my Back Room invented this rig called the Eight-Nozzled, Elephant-Toted Boom- Blitz. It shoots high-explosive sour cherry stone pits and will put your dumb Kick-a-Poo Kid on the fritz!” Poor Daniel and I were scared out of our witz!

Once more, by VanItch I was bested and beat. Once again I limped home from the Wall in defeat. I dragged and I sagged and my spirits were low, as low as I thought that they ever could go, when I heard a Boom-Bah! And a Diddle-dee-Dill! And our Butter-Up Band marched up over the Hill!

The Chief Yookeroo had sent them to meet me along with the Right-Side-Up Song Girls to greet me. They sang: “Oh, be faithful! Believe in thy butter!” And they lifted my spirits right out of the gutter!

“My boy”, smiled the Chief Yookeroo, “we’ve just voted and made you a general! You’ve been promoted. Your pretty new uniform’s ready. Get in it! The Big War is coming. You’re going to begin it! And what’s more, this time you are certain to win it.

“My Boys in the Back Room have finally found how. Just wait till you see what they’ve puttered up now! In their great new machine you’ll fly over that Wall and clobber those Butter-Down Zooks one and all!”

Those Boys in the Back Room sure knew how to putter! They made me a thing called the Utterly Sputter and I jumped aboard with my heart all aflutter and steered toward the land of the Upside-Down Butter.

This machine was so modern, so frightfully new, no one knew quite exactly just what it would do!

But it had several faucets that sprinkled Blue Goo which, somehow, would sprinkle the Zooks as I flew and gum up that upside-down butter they chew.

I was racing pell-mell when I heard a voice yell, “If you sprinkle us Zooks, you’ll get sprinkled as well!”

VanItch had a Sputter exactly like mine! And he yelled, “My Blue-Gooer is working just fine! And I’m here to say that if Yooks can goo Zooks, you’d better forget it. ‘Cause Zooks can goo Yooks!”

I flew right back home and, as you may have guessed, I was downright despondent, disturbed, and depressed. And I saw, just as soon as I stepped back on land, so were all of the girls of the Butter-Up Band.

The Chief Drum Majorette, Miz Yookie-Ann Sue, said, “That was a pretty sour flight that you flew. And the Chief Yookeroo has been looking for you!”

I raced to his office. The place was a sight. “Have no fears,” said the Chief. “Everything is all right. My Bright Back Room Boys have been brighter than bright. They’ve thought up a gadget that’s Newer than New. It is filled with mysterious Moo-Lacka-Moo and can blow all those Zooks clear to Sala-ma-goo. THEY’VE INVENTED THE BITSY BIG- BOY BOOMEROO!

“You just run to the wall like a nice little man. Drop this bomb on the Zooks just as fast as you can. I have ordered all Yooks to stay safe underground while the Bitsy Big-Boy Boomeroo is around.”

As I raced for that Wall, with the bomb in my hand, I noticed that every last Yook in our land was obeying our Chief Yookeroo’s grim command.

They were all bravely marching, with banners aflutter, down a hole! For their country! And Right-Side-Up Butter!

That’s when Grandfather found me! He grabbed me. He said, “You should be down that hole! And you’re up here instead! But perhaps this is all for the better, somehow. You will see me make history! RIGHT HERE! AND RIGHT NOW!

Grandpa leapt up that Wall with a lopulous leap and he clearedhis harse throat with a bopulous beep. He screamed, “Here’s the end of that terrible town full of Zooks who eat bread with the butter side down!”

And at the very instant we heard a klupp-klupp of feet on the Wall and old VanItch klupped up! The Boys in HIS Back Room had made him one too! In his fist was another Big- Boy Boomeroo! “I’ll blow you,” he yelled, “into pork and wee beans! I’ll butter-side-up you to small smithereens!”

“Grandpa!” I shouted. “Be careful! Oh, gee! Who’s going to drop it? Will you. . . Or will he . . . ?”

“Be patient,” said Grandpa. “We’ll see. We will see. . . “
```

---

## IC-1526: Cat’s in the Cradle and Love You Forever

- Title: Cat’s in the Cradle and Love You Forever
- Author (byline): Harry Chapin and Robert Munsch
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1292
- Already set (do not supply): none

### Source block (context only)

```text
Author: Harry Chapin
Book: Songs of the 1970s
ISBN: 978-1495000348
Publisher: Hal Leonard
Date (Month/Year): Feb 2015
Author: Robert Munsch
ISBN: 978-0920668375
Publisher: Firefly Books
Date (Month/Year): Sept 1995
```

### Introduction (context only: never use it for content warnings)

```text
For a couple of hundred years now, each generation of fathers has passed on less and less to their sons--not just less power, but less wisdom. And less love. Today, we’ve reached a point where many fathers are largely irrelevant in the lives of their children.

Harry Chapin's hit lyrical poem "Cat's in the Cradle" is about an overly-absent father. Time passes, with other responsibilities always taking precedence over his child, until suddenly the child is grown, minus the influence of his father. Ironically, Harry Chapin died in a car accident in 1981 and never got to see his own children grown up . . . making this poem somehow even sadder.

This compilation combines Cat’s in the Cradle by Harry Chapin and Love You Forever by Robert Munsch . . . to remind both parents and children that it’s never too late to love.

Cat’s in the Cradle by Harry Chapin
```

### Performance text (classify this)

```text
My child arrived just the other day
He came to the world in the usual way
But there were planes to catch and bills to pay
He learned to walk while I was away
And he was talkin' 'fore I knew it, and as he grew
He'd say "I'm gonna be like you dad
You know I'm gonna be like you"

And the cat's in the cradle and the silver spoon Little boy blue and the man on the moon When you comin' home dad? I don't know when, but we'll get together then son You know we'll have a good time then

My son turned ten just the other day He said, "Thanks for the ball, Dad, come on let's play Can you teach me to throw", I said "Not today I got a lot to do", he said, "That's ok" And he walked away but his smile never dimmed And said, "I'm gonna be like him, yeah You know I'm gonna be like him"

And the cat's in the cradle and the silver spoon Little boy blue and the man on the moon When you comin' home son? I don't know when, but we'll get together then son You know we'll have a good time then

Well, he came home from college just the other day So much like a man I just had to say "Son, I'm proud of you, can you sit for a while?" He shook his head and said with a smile "What I'd really like, Dad, is to borrow the car keys See you later, can I have them please?"

And the cat's in the cradle and the silver spoon Little boy blue and the man on the moon When you comin' home son? I don't know when, but we'll get together then son You know we'll have a good time then

I've long since retired, my son's moved away I called him up just the other day I said, "I'd like to see you if you don't mind" He said, "I'd love to, Dad, if I can find the time You see my new job's a hassle and kids have the flu But it's sure nice talking to you, Dad It's been sure nice talking to you"

And as I hung up the phone it occurred to me He'd grown up just like me My boy was just like me

And the cat's in the cradle and the silver spoon Little boy blue and the man on the moon When you comin' home son? I don't know when, but we'll get together then son You know we'll have a good time then

TRANSITION Love You Forever started as a song that Robert Munch made up to comfort himself while he and his wife grieved the stillborn death of two children. Every time he sang it to himself, he cried for the loss of those two children he would never hold . . . never see grow up. In this poem, we learn so much about the circle of life, about youth, about parenting and about our own responsibilities to our children and to our parents as they get older. Love You Forever by Robert Munsch

A mother held her new baby
and very slowly rocked him back and forth,
back and forth, back and forth.
And while she held him, she sang:

I'll love you forever,
I'll like you for always,
As long as I'm living
my baby you'll be.

The baby grew.
He grew and he grew and he grew.
He grew until he was two years old,
and he ran all around the house.

He pulled all the books off the shelves.
He pulled all the food out of the refrigerator
and he took his mother's watch and
flushed it down the toilet.
Sometimes his mother would say,
"This kid is driving me CRAZY!"

But at night time,
when that two-year-old was quiet,
she opened the door to his room,
crawled across the floor,
looked up over the side of his bed;
and if he was really asleep
she picked him up and rocked him back and forth,
back and forth, back and forth.
While she rocked him she sang:

I'll love you forever,
I'll like you for always,
As long as I'm living
my baby you'll be.

The little boy grew.
He grew and he grew and he grew.
He grew until he was nine years old.
And he never wanted to come in for dinner,
he never wanted to take a bath,
and when grandma visited he always said bad words.
Sometimes his mother wanted to sell him to the zoo!

But at night time,
when he was asleep,
the mother quietly opened the door to his room,
crawled across the floor
and looked up over the side of the bed.
If he was really asleep,
she picked up that nine-year-old boy
and rocked him back and forth,
back and forth, back and forth.
And while she rocked him she sang:

I'll love you forever,
I'll like you for always,
As long as I'm living
my baby you'll be.

The boy grew.
He grew and he grew and he grew.
He grew until he was a teenager.
He had strange friends
and he wore strange clothes
and he listened to strange music.
Sometimes the mother felt like she was in a zoo!

But at night time,
when that teenager was asleep,
the mother opened the door to his room,
crawled across the floor
and looked up over the side of the bed.
If he was really asleep she picked up that great big boy
and rocked him back and forth,
back and forth, back and forth.
While she rocked him she sang:
I'll love you forever,
I'll like you for always,
As long as I'm living
my baby you'll be.

That teenager grew.
He grew and he grew and he grew.
He grew until he was a grown-up man.
He left home and got a house across town.
But sometimes on dark nights
the mother got into her car and drove across town.
If all the lights in her son's house were out,
she opened his bedroom window,
crawled across the floor,
and looked up over the side of his bed.
If that great big man was really asleep
she picked him up and rocked him back and forth,
back and forth, back and forth.
And while she rocked him she sang:

I'll love you forever,
I'll like you for always,
As long as I'm living
my baby you'll be.

Well, that mother, she got older.
She got older and older and older.
One day she called up her son and said,
"You'd better come see me
because I'm very old and sick."
So her son came to see her.
When he came in the door she tried to sing the song.
She sang:

I'll love you forever, I'll like you for always...

But she couldn't finish
because she was too old and sick.
The son went to his mother.
He picked her up and rocked her back and forth,
back and forth, back and forth.
And he sang this song:
I'll love you forever,
I'll like you for always,
As long as I'm living
my Mommy you'll be.

When the son came home that night,
he stood for a long time at the top of the stairs.
Then he went into the room
where his very new baby daughter was sleeping.
He picked her up in his arms
and very slowly rocked her back and forth,
back and forth, back and forth.
And while he rocked her he sang:

I'll love you forever,
I'll like you for always,
As long as I'm living
my baby you'll be.
```

---

## IC-1527: Cautionary Tales for Children

- Title: Cautionary Tales for Children
- Author (byline): Hilaire Belloc
- Work: Not specified
- Publisher: Harcourt, Inc.
- Publication date as stated: Dec 2002
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 859
- Already set (do not supply): none

### Source block (context only)

```text
Author: Hilaire Belloc
ISBN: 978-0151007158
Publisher: Harcourt, Inc.
Date(Month/Year): Dec 2002
```

### Introduction (context only: never use it for content warnings)

```text
Children grow up hearing tales told to them by their parents and grandparents. Often these tales are designed to teach a lesson, caution against disobedience or sometime even terrorize the poor tots into good behavior. Collectively we call these stories Cautionary Tales.

Now I’m not talking about stories like Hansel and Gretel, who use their wits and resourcefulness to not only kill the wicked witch in the house of gingerbread, but also to find their way home and live happily ever after. . . . No, in Cautionary Tales, the children have bad habits, disobey their elders or otherwise make really bad decisions AND they meet a fate that often far exceeds the crime.

Today, you’ll hear about 4 lovely children: Henry King, Jim, Charles Augustus Fortescue, and Rebecca . . . All typical children who meet their unfortunate demise in Cautionary Tales for Children by Hilaire Belloc.
```

### Performance text (classify this)

```text
Meet Henry King who had the terrible habit of
gnawing on non-food items . .
The Chief Defect of Henry King
Was chewing little bits of String.
At last he swallowed some which tied
Itself in ugly Knots inside.
Physicians of the Utmost Fame
Were called at once; but when they came
They answered, as they took their Fees,
“There is no Cure for this Disease.
“Henry will very soon be dead.”
His Parents stood about his Bed
Lamenting his Untimely Death,
When Henry, with his Latest Breath,
Cried, “Oh, my Friends, be warned by me,
That Breakfast, Dinner, Lunch, and Tea
Are all the Human Frame requires...”
With that, the Wretched Child expires.
**************************************************
Next there was Jim who had a tendency to wander
away from his elders . . .
There was a Boy whose name was Jim;
His Friends were very good to him.
They gave him Tea, and Cakes, and Jam,
And slices of delicious Ham,
And Chocolate with pink inside
And little Tricycles to ride,
And read him Stories through and through,
And even took him to the Zoo--
But there it was the dreadful Fate
Befell him, which I now relate.
You know--or at least you ought to know,
For I have often told you so--
That Children never are allowed
To leave their Nurses in a Crowd;
Now this was Jim's especial Foible,
He ran away when he was able,
And on this inauspicious day
He slipped his hand and ran away!
He hadn't gone a yard when--Bang!
With open Jaws, a lion sprang,
And hungrily began to eat
The Boy: beginning at his feet.
Now, just imagine how it feels
When first your toes and then your heels,
And then by gradual degrees,
Your shins and ankles, calves and knees,
Are slowly eaten, bit by bit.
No wonder Jim detested it!
No wonder that he shouted “Hi!”
The Honest Keeper heard his cry,
Though very fat he almost ran
To help the little gentleman.
“Ponto!” he ordered as he came
(For Ponto was the Lion's name),
“Ponto!” he cried, with angry Frown,
“Let go, Sir! Down, Sir! Put it down!”
The Lion made a sudden stop,
He let the Dainty Morsel drop,
And slunk reluctant to his Cage,
Snarling with Disappointed Rage.
But when he bent him over Jim,
The Honest Keeper's Eyes were dim.
The Lion having reached his Head,
The Miserable Boy was dead!
When Nurse informed his Parents, they
Were more Concerned than I can say:--
His Mother, as She dried her eyes,
Said, “Well--it gives me no surprise,
He would not do as he was told!''
His Father, who was self-controlled,
Bade all the children round attend
To James's miserable end,
And always keep a-hold of Nurse
For fear of finding something worse.

**************************************************
But, contrary to popular belief, not all misbehaving
children are boys
. . . Meet Rebecca Who Slammed Doors For Fun And
Perished Miserably
A trick that everyone abhors
In little girls is slamming doors.
A wealthy banker's little daughter
Who lived in Palace Green, Bayswater
(By name Rebecca Offendort),
Was given to this furious sport.
She would deliberately go
And slam the door like billy-o!

To make her uncle Jacob start. She was not really bad at heart, But only rather rude and wild; She was an aggravating child... It happened that a marble bust Of Abraham was standing just Above the door this little lamb Had carefully prepared to slam, And down it came! It knocked her flat! It laid her out! She looked like that. Her funeral sermon (which was long And followed by a sacred song) Mentioned her virtues, it is true, But dwelt upon her vices too, And showed the deadful end of one Who goes and slams the door for fun. The children who were brought to hear The awful tale from far and near Were much impressed, and idly swore They never more would slam the door, -- As often they had done before.

************************************************** And occasionally you even find a well-behaved child. I’ll leave you on a less macabre note by introducing the benefits of good behavior through Charles Augustus Fortescue . . .

The nicest child I ever knew
Was Charles Augustus Fortescue.
He never lost his cap, or tore
His stockings or his pinafore:
In eating Bread he made no Crumbs,
He was extremely fond of sums,
To which, however, he preferred
The Parsing of a Latin Word--
He sought, when it was within his power,
For information twice an hour,
And as for finding Mutton-Fat
Unappetizing, far from that!
He often, at his Father's Board,
Would beg them, of his own accord,
To give him, if they did not mind,
The Greasiest Morsels they could find--
His Later Years did not belie
The Promise of his Infancy.
In Public Life he always tried
To take a judgment Broad and Wide;
In Private, none was more than he
Renowned for quiet courtesy.
He rose at once in his Career,
And long before his Fortieth Year
Had wedded Fifi, Only Child
Of Bunyan, First Lord Aberfylde.
He thus became immensely Rich,
And built the Splendid Mansion which
Is called The Cedars, Muswell Hill,
Where he resides in affluence still,
To show what everybody might
Become by SIMPLY DOING RIGHT.
```

---

## IC-1528: A Proposed Curriculum Change and First Period

- Title: A Proposed Curriculum Change and First Period
- Author (byline): Richard Howard and Kevin M. Derring
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1256
- Already set (do not supply): none

### Source block (context only)

```text
Author: Richard Howard
Book: The Best American Poetry 2012
ISBN: 978-1439181539
Publisher: Scribner
Date (Month/Year): September 2012
Author: Kevin M. Derrig
Book: The Spoken Word Revolution: Slam, Hip Hop &
the Poetry of a New Generation
ISBN: 978-1402202469
Publisher: Sourcebooks, Incorporated
Date (Month/Year): March 2005
```

### Introduction (context only: never use it for content warnings)

```text
As many teachers know, the national discussion on education is overcrowded with opinions on teacher training, salaries, tenure, and unions -- with occasional detours through iPads, textbooks, and national policy. In fact, it seems that we listen to every interested party except the one for whom education exists in the first place: students.

This compilation looks at education through the eyes of students. In the first poem “A Proposed Curriculum Change” by Richard Howard, a fifth grade class wishes to change their “one-sided” school curriculum and composes a letter to the “powers that be” with the help of their teacher.
```

### Performance text (classify this)

```text
Dear Mrs Masters,

It's happened again! and the whole Fifth-Grade Class is upset

(which is why we're writing again: you told us to tell you when "anything related to

school" upsets the class, so now we're telling). You see, just last week,

thanks to Mr Lee's connections (that's what he calls the friends

who do him favors), our Fifth-Grade Science Class, all twelve, until the Klein twins got mumps,

-together, of course-and had to stay home, so we invited

Mike Rahn and Clark Taft, the two smartest kids in the Fourth-Grade,

to come instead, since Mr Lee had specified there would be twelve students visiting

the Sandusky Labs for our winter-term science field trip, and

no one wants to sec two favors go to waste. Dinny-that's

Mr Lee: he asked us all to call him that,
and now he's the one teacher at school
we're on first-name, or
maybe nick-name terms

with ... whom. Anyway, Dinny has this friend Mr Morton

who works in the Labs (he told us right away, "Call me Mort, everyone does"-first names must be a sort of code for Scientists),

on the development of cancerous tumors that he trained

to grow in mice (induced was the word he used).
When he offered to show us how
his experiment
was coming along,

Lucy Wensley asked "Mr Mort" ifhe could tell one mouse

from the next: "Do you ever see something
individual about a mouse-
some particular
mouse you're working on?"

(Lucy sometimes brings her pet guinea-pig to school with her,

so of course she'd ask a thing like that.)
Her question really surprised Mort, but
maybe what he said
was a good answer;

after a moment he told this story: last week he had

to kill a mouse with a newborn litter, and to save her young, gave them to another mouse to bring them up with her own; and when

that experiment worked, he gave that foster-mother mouse

another litter of newborn young, to see
what she would do. At first all went well:
the new babies were
fat and already

growing fur, though still blind-and then one night she ate them all! ...

Not just Lucy but our whole Class, including the two Fourth-Graders, listened without saying anything.

Nobody moved. Mort

opened the lab door, saying "Boys and girls, please come with me"

and the spell was broken. But Mrs Masters,
no one has forgotten Mort's story.
Over and over
in Dinny's classes

we've learned this lesson: In the Animal World-and aren't we

animals too?-mothers and fathers go
after their young, all shapes and sizes,
pigs in model farms,
Komodo dragons,

and now even mice! Maybe our own parents will eat us

eventually-they may have eaten us
already, and the rest of our life
is just the process
of their digestion.

That's not our life, it's our education, but it seems so ...

one-sided! Maybe in Sixth-Grade, things will work
the other way around, so that sons
murder their fathers,
babies eat grownups,

and Snow White poisons her wicked step-mother. So far that's

the best reason to leave Fifth-Grade behind us. Still, we don't see why Science-at least Dinny Lee's version – has to be so ... so

animalistic. That may be how life is, but we'd like

to put in a word-two words-for Other Things we could learn at Park School, Duncan Chu says that the right phrase for what we mean is

human interest: what we want to study at Park School

is how people have managed to avoid behaving like animals, instead of becoming them.

Is Science only

a history of death? Maybe we'll find out in Sixth-Grade that

no Fate is worse than death after all,
and that life is going to be ours.
Dear Mrs Masters,
if these suggestions

make sense to you, please let us (and Dinny Lee) know about

what courses we'll be taking next year along
the lines we have designated here,
and the kind of books
we should be reading

over the summer. (signed) Respectfully, the Fifth-Grade Class:

Judy Abrams, Nancy Akcrs,Jean Sturges, David
Halperin,
David Stashower, Jane McCullough,
Arthur Englander,
Anne Wiebe, Lois

Hexter, Jeunessc Ames, David McConnehey, Duncan Chu

and today's guests, Mike Rahn & Clark Taft visiting from the Fourth-Grade Class

TRANSITION You see, a one-size fits all curriculum is counter-productive. With the variety of student backgrounds, cultures and abilities; teachers are placed in an untenable situation. Trying to adhere to the curriculum requirements prescribed by the system while engaging students in class sizes that are often too large for individualized instruction has left many teachers feeling unappreciated, burned-out, used-up and frustrated . . . Teachers who once were devoted to their students have become less and less tolerant, less caring, less nurturing and more and more frustrated. That’s the word that is heard most often from teachers . . . frustrated. And ultimately it is the student who bears the brunt of that frustration. Now, don’t get me wrong, there are still inspiring, devoted teachers out there; but the system has also created teachers like the one in First Period by Kevin M. Derring half way through first period dust accumulated on the sweaty palm of my

raised hand must be a centimeter thick by now as the chicken-legged teacher goes around the

room
defacing students’ homework from last night
with red pen graffiti
that focuses more on missed commas than the

content of the sentences he finally decides to acknowledge me “Mr. Derrig, why do I have a feeling that this is

another one of your dumb comments. You constantly waste my time. Why

don’t you just drop out or something?”

why don’t I just drop out why don’t I just drop out! and it was at that moment that all statistics

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
```

---

## IC-1529: The Chambers of a Gun if the Bullet Does Not Exist

- Title: The Chambers of a Gun if the Bullet Does Not Exist
- Author (byline): Zanne Langlois and Natasha Hooper
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1094
- Already set (do not supply): none

### Source block (context only)

```text
Author: Zanne Langlois
ISBN: On-line Transcript
https://mrsconnollysclass.com/wp-
content/uploads/2021/01/chambers-of-a-gun-zanne-
langlois.pdf
Publisher: Button Poetry
Date (Month/Year): 2015
Author: Natasha Hooper
Book: Fight Evil with Poetry, Volume 1, Pgs 103-104
ISBN: 978-0997129762
Publisher: Sideshow Media Group
Date (Month/Year): Oct 2018
```

### Introduction (context only: never use it for content warnings)

```text
Sometimes complex processes are easier to understand when you break them down into their component parts. Take America’s uncomfortable marriage to gun violence for example – Let’s look at the numbers for one day only. Just one day. As families and communities rang in the New Year in 2025, there were more than 200 shootings across the country -- a total of 78 people were killed and another 197 people were injured.*

The Chambers of a Gun by Zanne Langlois breaks gun violence down in another way -- address the political and public systems that fail to prevent these tragedies. Inaction in the face of tragedy. Thoughts and prayers but let’s stop there.
```

### Performance text (classify this)

```text
The Chambers of a Gun by Zanne Langlois
A gun has 26 working parts-
The length of the barrel, the speed of the bullet,
And caliber of the ammunition determines lethality.
There are 6 chambers in the cylinder.
When cocked, the hammer clicks, as it locks into place.
The trigger requires a precise amount of pressure to fire.

The target erupts, as the bullet forces entry, Opening a door that cannot be closed. An act that cannot be undone.

A school shooting has countless working parts. The lengths at which the shooter will go to force entry. The speed of the response and the caliber of the security

system
Determine its lethality.
The first shot triggers a lock-down.
The fire alarm sounds as chaos erupts
And classrooms become as deadly and inescapable
As gas chambers.
The shooter burns through clips of bullets,
Until police, moving with precision, secure the building.
Reopening closed doors, separating the student body
Into living and dead.

The Senate has 100 working parts. The size of the majority, the length of their terms, And the caliber of the lobbyists determine its productivity. The massacre of school children triggers debate in the

chamber.

But while the men and women are dead-locked,
Arguing endlessly behind closed doors,
Two pressure cookers erupt in Boston.
And new images of carnage force entry into our minds.
We barely notice when the Senate body rejects gun control.

The American electorate has 200 million working parts. The size of the tragedy, the length of the media coverage, And the caliber of the press photographers determines the

level of outrage.
Pressure builds and erupts in shocked headlines,
But the firing squad has no trigger to pull.
The shooter's last bullet forced entry to his skull,
Closing the door to why and leaving only what,
And how, and this is not a question we want to answer.
The four chambers of a human heart
Are each filled with separate desires.
For safety, for freedom, for power, for protection.
We are dead-locked. And minds that are closed cannot be

re-opened.

But a murdered child has no working parts. Its body does not function.

The size of the child at the time of its death determines The length of a coffin. A coffin is a chamber lined with silk and sorrow. When the lid clicks shut, it cannot be re-opened. When will this trigger more than tears? When will we feel the pressure of small hands Hammering on the locked doors or our hearts? As soon as our eyes are dry, we shut them again.

*Introduction statistic source https://www.everytown.org/press/2025-already-marked-by-tragedy-as-gun-violence-devastates-new-years-celebrations-advocates-urge-lawmakers-entering-legislative-sessions-to-pass-stronger-gun-safety-measures/ TRANSITION

But what if (pause as if seeing someone roll their eyes) I know, but “what if” will get us just as far as “thoughts and prayers” when it comes to gun violence. So, what if guns were symbols of peace rather than destruction? What if joy could replace death? And what if the bullet did not exist? Instead -- only hope, only joy, only triumph, only life. Natasha Hooper reimagines everyday gun use and the possibility of a better future in what she admits may only happen in an alternate universe. The Bullet Does Not Exist by Natasha Hooper

The Bullet Does Not Exist by Natasha Hooper In Jacksonville, Florida, a man parks his vehicle at a gas station. With all his angst resting quietly in his glove compartment, he makes his displeasure known next to a car full of black boy joy and turns jubilee into chaos. A teenager is no more by the end of the night while another Friday will be a commemoration in a year's time and we are all left wondering how the gun keeps ending up in the wrong hands.

There is an alternate universe in which the word "gun" is

welcomed
into every conversation.
Where a holster hangs from a hip as brilliantly as a star,
Waiting to be birthed into the next milky way.
Each gun is handled with a soft grip,
Like a withered petal seconds away from becoming dust.
'Whisper' is etched into the metal of every muzzle and

alas,
The bullet does not exist.
In this universe, we load our guns with bliss.
Pack happiness tightly into each magazine,
And pull the trigger as if it were a sunrise on a Sunday

morning. We say things like "Remember that shootout at the gas

station? How the gunman came prepared, Concealed his dreams in his car like some undiscovered

magic
at the base of an ocean.
Remember how we showed him our carefree
and he showed us his barrel?
Pointed it at all the young and black bodies, repeatedly

pulling the trigger And the only thing that came out was laughter?" Each shootout would indeed be a welcomed experience with no funerals to follow. A trip to the gun range would be therapy, a Berreta to

dispense our tears and a shotgun with only tissues in the barrel. Tamir would play cops and robbers without imagining

death,
Chyna would walk home with only a compliment on her
back,
Philando would drive away wiping the excess elation off
his shirt,
And all the church members of Charleston would have
just one more thing to sing about.
Yes, the bullet would not exist,
Which would mean that the gun could never
be in the hands of the wrong person.
An empty clip would be celebrated as a selfless act.
"Look at all the joy he gave away today, how he unified

our nation
with each shot, each invisible ray travelling faster
than the speed of sound
to transform any particular body into a better version of

itself."

There would be so much delight spilled onto the

concrete that we would lay down just to soak it up. Draw chalk outlines around our own bodies to save our

places. This alternate universe exists with no mention of the

term 'justifiable death', but rather 'inexplicably content'. This alternate universe exists with the universal

knowledge
that we will not die today from our guns.
That we will not die any day from our guns.
That our bullets will not even exist if they be

synonymous with death.
Only hope,
Only joy,
Only triumph,
Only life,
Only life,
This alternate universe is life-giving, with the safety off
and a fistful of smiles
Rifles poised at the ready with a clip full of possibilities,
Pointed at anyone ready and willing
To accept it.
```

---

## IC-1530: The Cherokee Lottery Collection

- Title: The Cherokee Lottery Collection
- Author (byline): William Jay Smith
- Work: The Cherokee Lottery
- Publisher: Curbstone Books
- Publication date as stated: May 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1105
- Already set (do not supply): none

### Source block (context only)

```text
All poems are from the following source:
Author: William Jay Smith
Book: The Cherokee Lottery
ISBN: 978-1880684665
Publisher: Curbstone Books
Date (Month/Year): May 2000
```

### Introduction (context only: never use it for content warnings)

```text
In 1828 gold was discovered on Cherokee land at Dahlonega in northern Georgia, where the Cherokees for centuries had hunted. Now they grew crops, and tended lush peach orchards and rich cattle farms. But still they did not own Dahlonega. In May 1830, at Present Andrew Jackson’s prodding, Congress passed the Removal Act, which set aside territory west of the Mississippi for the relocation of Indian tribes. The Indians had no choice. Eight years later, when all resistance had failed, the Cherokee joined other tribes in forced exile. Thousands died on what became known as the Trail of Tears. The devastation began with . . . The Cherokee Lottery by William Jay Smith.
```

### Performance text (classify this)

```text
The Cherokee Lottery

-- Georgia 1838and while the wheel creaked

When the Cherokees refused to leave, the state set up a lottery

to rid them of their land: a clumsy wooden wheel

sat poised above great black numbers painted on bright squares –

woodpecker red and watermelon green, wild azalea orange

and morningglory blue – to designate the farms

that now were up for grabs: and while the wheel creaked

slowly round, the Georgians danced and sang:

“All we want in this creation

Is a pretty little girl

And a big plantation

Way down yonder

In the Cherokee Nation!” and laughed until they cried.

General Winfield Scott,

blue-uniformed, bushy-browed, six-foot-three, arrived from Washington

and addressed the Cherokees: “May’s full moon

is already on the wane, and before another

passes, every Cherokee, man, woman, and child,

must move along to join their brothers in the West.”

And when his troops swept in

from every quarter, fixed bayonets flashing in the sun

to roust them from their tables and their beds,

the Cherokees, stripped of everything they owned,

at last lined up to go.

White-haired Going Snake

the eighty-year-old chief, on his pony led the way,

followed by young men on horseback. Then the women and children,

with rustling sound wind makes in tall dry grass,

came on, and no one spoke, no one cried: only the dogs

howled as if they along could voice the nation’s grief

while the procession slowly wound its way off through the tall pines

over the red clay.

At the moment they began to move,

a low rumble of distant thunder broke directly westward

and a dark spiral cloud rose above the horizon,

but the sun was unclouded, the thunder rolled away,

and no rain fell.

TRANSITION

15,000 Indian men, women and children were forced to march westward to what is now Oklahoma. Of these, an estimated 4,000 died on the brutal journey due to starvation, exhaustion, and exposure to the unforgiving elements. Smith both celebrates and mourns his own Choctaw heritage, and that of all Americans, in the haunting poem . . . The Pumpkin Field.

The Pumpkin Field

-- An Army Lieutenant observes the Cherokees he guards on their passage to the west, Arkansas 1838

What a grand lot they were,

the Cherokees I first saw in June, lined up in their Georgian camp

to greet the chief on their departure, elegant blankets hanging loose

about their shoulders, ramrod-straight, dark eyes darting from high-boned

copper faces under bright turbans and striped caps pulled down at an angle,

some in long robes, some in tunics, all with sashes or wondrous drapery,

they stood, framed by bearded oaks, Old Testament patriarchs

pausing on their way to the Promised Land.

Then in October, where I'd been sent ahead

to patrol their passage here in Arkansas, they came from a cold and threadbare wood,

thin pines bent and tipped with sleet, eyes glazed and blank,

half-naked, barefoot, bones poking through

their scarecrow shredded clothing, and stumbled through layers of mist

onto a scraggly open field where in wet and tangled grass

fat pumpkins lay in rows like painted severed heads.

Oblivious to all around them,

skeletal automatons, the Cherokees plunged ahead

until a farmer on the edge bade them halt

and, breaking off a pumpkin, invited them to take

whatever his poor field could offer.

Flies swarming to their target,

they darted up and down the rows, black hair flying,

long-nailed tentacles protruding, they ripped apart

the pumpkin flesh until their brown and vacant

faces merged with jagged pulp, seeds foaming from

their hungry mouths, and all I could see, as on some battlefield, was

everywhere a wasted mass of orange flesh.

A light rain then began to fall

as if the shredded pumpkin fiber drifted down around us:

I felt ill and sensed that cholera

had set in. The farmer guided me inside his cabin

and put me down in a dark corner where between the logs

I could empty my stomach.

All night long I lay there

while wind roared and rain beat down

and through it I could hear the sloshing of the weary feet,

the creak and rattle of ox-carts, the cursing of the drivers,

cracking their long whips to urge the oxen on, the whinnying of horses

as they struggled through the mud.

"What have we done to these people?"

I cried out ... And then a silence fell; across the dark I saw

row after row of pumpkins carved and slit, their crooked eyes

and pointed teeth all candle-lit within, not pumpkins but death's-heads they were

with features of the vacant hungry faces I had seen,

stretching to infinity and glowing in the dark-

and glowing still when I awoke-

as they do now, and as they always will.

TRANSITION

There were ten million Native Americans on this continent when the first non-Indians arrived. Over the next 300 years, 90% of the Native American population was wiped out by disease, famine, or warfare imported by the whites. By 1840 all the eastern tribes had been subdued, annihilated or forcibly removed to Indian Territory west of the Mississippi. This is the . . . . Song of the Dispossessed

Song of the Dispossessed

You came across the water,

like gods you walked ashore the fabric of our dreaming

was the clothing that you wore.

You came with ornament

far brighter than the sun; you brought the handsome horse,

the flashing blade, the gun.

You brought your holy book

that held a world entire, a life that never ended;

and water that was fire.

You said, “We’ll live as brothers,

as brothers we will die; we’ll share the forest carpet

and the blanket of the sky.”

But then when we came near you,

you said “Now move away; you come too close now, brother,

it’s dangerous to stay

so close to one another;

and you must understand that we know what is better –

we’ll send you to a land

far richer in the west

beyond the great brown river where grass is always green

and there you’ll live forever.”

And so you took our country,

you took our sacred ground, the birds and beasts we cherished,

the falling water’s sound, the stag that with his antlers

breaks the sun-flecked trail, the mockingbird, the turkey,

the heron and the quail.

You sent us to this desert,

this sand, these pitted stones, where wind rakes through the gully

and bares the bison’s bones,

where now above this barren earth

your great bald eagle screams, that robbed us of our country

and carried off our dreams.
```

---

## IC-1531: The City of Slaughter

- Title: The City of Slaughter
- Author (byline): Chaim Nahman Bialik
- Work: Selected Poems of C.N. Bialik
- Publisher: Penguin Group (USA)
- Publication date as stated: July 2003
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1382
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chaim Nahman Bailik
Book: Selected Poems of C.N. Bialik
ISBN: 978-1585673438
Publisher: Penguin Group (USA)
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
Chiam Nahman Bialik was sent by the Jewish Historical Commission to interview Jewish survivors of the Kishinev pogroms of 1903. His response was the epic poem, In the City of Slaughter, a powerful statement of anguish at the situation of the Jews. This poem not only describes the terror and devastation of the event but also castigates the victims for their passivity in face of the onslaught. Words are truly powerful . . . In the City of Slaughter by Chiam Nahman Bialik
```

### Performance text (classify this)

```text
Arise and go now to the city of slaughter;
Into its courtyard wind thy way;
There with thine own hand touch, and with the eyes of
thine head,
Behold on tree, on stone, on fence, on mural clay,
The spattered blood and dried brains of the dead.
Proceed thence to the ruins, the split walls reach,
Where wider grows the hollow, and greater grows the
breach;
Pass over the shattered hearth, attain the broken wall
Those burnt and barren brick, whose charred stones
reveal
The open mouths of such wounds, that no mending
Shall ever mend, nor healing ever heal.
There will thy feet in feathers sink, and stumble
On wreckage doubly wrecked, scroll heaped on
manuscript.
Fragments again fragmented
Pause not upon this havoc; go thy way…
Unto the attic mount, upon thy feet and hands;
Behold the shadow of death among the shadows stands.
Crushed in their shame, they saw it all;
They did not pluck their eyes out; they
Beat not their brains against the wall!
Perhaps, perhaps, each watcher bad it in his heart to
pray:
A miracle, O Lord, and spare my skin this day!
Come, now, and I will bring thee to their lairs
The privies, jakes and pigpens where the heirs
Of Hasmoneans lay, with trembling knees,
Concealed and cowering -the sons of the Maccabees!

The seed of saints, the scions of the lions!
Who, crammed by scores in all the sanctuaries of their
shame
So sanctified My name!
It was the flight of mice they fled,
The scurrying of roaches was their flight;
They died like dogs, and they were dead!
And on the next morn, after the terrible night
The son who was not murdered found
The spurned cadaver of his father on the ground.
Now wherefore dost thou weep, O son of Man?
Brief-weary and forespent, a dark Shekinah
Runs to each nook and cannot find its rest;
Wishes to weep, but weeping does not come;
Would roar; is dumb.
Its head beneath its wing, its wing outspread
Over the shadows of the martyr'd dead,
Its tears in dimness and in silence shed.
And thou, too, son of man, close now the gate behind
thee;
Be closed in darkness now, now thine that charnel space;
So tarrying there thou wilt be one with pain and anguish
And wilt fill up with sorrow thine heart for all its days.
Then on the day of thine own desolation
A refuge will it seem,
Lying in thee like a curse, a demon's ambush,
The haunting of an evil dream,
O, carrying it in thy heart, across the world's expanse
Thou wouldst proclaim it, speak it out,
But thy lips shall not find its utterance.
Beyond the suburbs go, and reach the burial ground.
Let no man see thy going; attain that place alone,
A place of sainted graves and martyr-stone.
Stand on the fresh-turned soil.
There in the dismal corner, there in the shadowy nook,
Multitudinous eyes will look
Upon thee from the sombre silence
The spirits of the martyrs are these souls,
Gathered together, at long last,
Beneath these rafters and in these ignoble holes.
The hatchet found them here, and hither do they come
To seal with a last look, as with their final breath,
The agony of their lives, the terror of their death.
Question the spider in his lair!
His eyes beheld these things; and with his web he can
A tale unfold horrific to the ear of man:
A tale of cloven belly, feather-filled;
Of nostrils nailed, of skull-bones bashed and spilled;
Of murdered men who from the beams were hung,
And of a babe beside its mother flung,
Its mother speared, the poor chick finding rest
Upon its mother's cold and milkless breast;
Of how a dagger halved an infant's word,
Its ma was heard, its mama never heard.
Then wilt thou bid thy spirit - Hold, enough!
Stifle the wrath that mounts within thy throat,
Bury these things accursed,
Within the depth of thy heart, before thy heart will
burst!
Then wilt thou leave that place, and go thy way
And lo-
The earth is as it was, the sun still shines:
It is a day like any other day.

Descend then, to the cellars of the town,
There where the virginal daughters of thy folk were
fouled,
Where seven heathen flung a woman down,
The daughter in the presence of her mother,
The mother in the presence of her daughter,
Before slaughter, during slaughter and after slaughter!
Note also, do not fail to note,
In that dark corner, and behind that cask
Crouched husbands, bridegrooms, brothers, peering
from the cracks,
Watching the sacred bodies struggling underneath
The bestial breath,
Stifled in filth, and swallowing their blood!
Such silence will take hold of thee, thy heart will fail
With pain and shame, yet I
Will let no tear fall from thine eye.
Though thou wilt long to bellow like the driven ox
That bellows, and before the Altar balks,
I will make hard thy heart, yea, I
Will not permit a sigh.

See, see, the slaughtered calves, so smitten and so laid;
Is there a price for their death? How shall that price be
paid?
Forgive, ye shamed of the earth, yours is a pauper-Lord!
Poor was He during your life, and poorer still of late.
When to my door you come to ask for your reward,
I'll open wide: See, I am fallen from My high estate.
I grieve for you, my children. My heart is sad for you.
Your dead were vainly dead; and neither I nor you
Know why you died or wherefore, for whom, nor by what
laws;
Your deaths are without reason; your lives are without
cause.
Turn, then, thy gaze from the dead, and I will lead
Thee from the graveyard to thy living brothers,
And thou wilt come, with those of thine own breed,
Into the synagogue, and on a day of fasting,
To hear the cry of their agony,
Their weeping everlasting.
Thy skin will grow cold, the hair on thy skin stand up,
And thou wilt be by fear and trembling tossed;
Thus groans a people which is lost.
Look in their hearts - behold a dreary waste,
Where even vengeance can revive no growth,
And yet upon their lips no mighty malediction
Rises, no blasphemous oath.
Speak to them, bid them rage!
Let them against me raise the outraged hand,
Let them demand!
Demand the retribution for the shamed
Of all the centuries and every age!
Let fists be flung like stone
Against the heavens and the heavenly Throne!
And thou, too, pity them not, nor touch their wound;
Within their cup no further measure pour.
Wherever thou wilt touch, a bruise is found,
Their flesh is wholly sore.
For since they have met pain with resignation
And have made peace with shame,
What shall avail thy consolation?
They are too wretched to evoke thy scorn.
They are too lost thy pity to evoke.

So let them go, then, men to sorrow born,
Mournful and slinking, crushed beneath their yoke.
So to their homes, and to their hearth depart
Rot in the bones, corruption in the heart.
And go upon the highway,
Thou shalt then meet these men destroyed by sorrow,
Sighing and groaning, at the doors of the wealthy
Proclaiming their sores, like so much peddler's wares,
The one his battered head, t'other limbs unhealthy,
One shows a wounded arm, and one a fracture bares.
And all have eyes that are the eyes of slaves,
Slaves flogged before their masters;
And each one begs, and each one craves:
Reward me, Master, for that my skull is broken.
Reward me for my father who was martyred!
And so their sympathy implore.
For you are now as you have been of yore
As you stretched your hand
So will you stretch it,
And as you have been wretched
So are you wretched!
What is thy business here, o son of man?
Rise, to the desert flee!
The cup of affliction thither bear with thee!
Take thou they soul, rend it in many a shred!
With impotent rage, thy heart deform!
Thy tear upon the barren boulders shed
And send they bitter cry into the storm.
```

---

## IC-1532: The Clichéd Meaning of Life

- Title: The Clichéd Meaning of Life
- Author (byline): Drew Tarvin
- Work: Not specified
- Publisher: Drew Tarvin.com
- Publication date as stated: Sept 21, 2017
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 764
- Already set (do not supply): none

### Source block (context only)

```text
Author: Drew Tarvin
ISBN: On-Line Transcript
https://drewtarvin.com/comedy/cliched-meaning-life/
Publisher: Drew Tarvin.com
Date (Month/Year): Sept 21, 2017
```

### Introduction (context only: never use it for content warnings)

```text
Drew Tarvin is an improviser, author, speaker, and corporate humorist hailing from the great state of Ohio. His first poetry show was in Pensacola, Florida, May 26, 2015. Up until that point, he had never tried any spoken word poetry; he was working mainly as a stand-up comedian in NYC. He quickly realized that the expectations of a spoken word crowd are quite different than that of improv or stand-up, because as he puts it, “spoken word audiences don’t care if you make them laugh, but they do want you to make them feel.”

The Clichéd Meaning of Life by Drew Tarvin
```

### Performance text (classify this)

```text
Have you ever seen a performance so inspirational, gone through a breakup so challenging, or had a milkshake that was so delicious . . . you started to contemplate the meaning of life? The essence of our existence? The significance of our sentience?

I don’t know; it’s something I’ve been thinking about a lot lately -- the meaning of life. But the more you read, the more confusing it all seems.

Maybe the meaning of life is money . . .

As they say money makes the world go ‘round . . .
Yet they also say the best things in life are free.
So do you live free or die hard?
Cuz to make ends meet
You have to start rollin’ in the dough.

But doe, a deer, a female deer . . .
Is nothing when the buck stops right here.
And I ain’t saying she’s a gold digger,
But mo money -- mo problems,
So you better check yourself before you wreck yourself,
Because money can’t buy happiness.

But don’t worry, be happy,
And live happily ever after
In a land far far away
Where there’s light at the end of the tunnel.
And to pass with flying colors,
Don’t color outside the lines
But think outside the box.

I don’t want to go off on a tangent
But things don’t add up
If it’s the thought that counts
And it’s better to give than to receive
Then sharing is caring.

But Jimmy crack corn and I don’t care,
Because crack is whack
And it’s hugs not drugs,
So put that in your pipe and smoke it.

But do you just say no
Or do you just do it?
If impossible is nothing,
Then a mission impossible
Ain’t nothing but a G thang, baby.
So Stop! Collaborate, and Listen.

Because maybe the meaning of life isn’t money; maybe the meaning of life is knowledge.

Because knowledge is power
And with great power comes great responsibility,
So don’t just drink responsibly,
but think responsibly,
Because I know what you did last summer.

And knowing is half the battle.
But is it a battle of the wits
Or a battle to the death?
Is the pen mightier than the sword,
Or is it a sword in the stone,
That can break my bones,
when words will never hurt me.

Because I’m rubber and you’re glue,
so whatever you say bounces off me and sticks to you
So speak now or forever hold your peace.
And don’t judge a book by its cover,
Because beauty is only skin deep.
And if looks can kill
And I wear my heart on my sleeve,
Then I’m armed and dangerous.

And home is where the heart is And there’s no place like home, Sweet home, Alabama.

But that’s just my state of mind In this state of denial Of the status quo.

I say carpe diem
If it’s quid pro quo
Get yourself tit for tat,
And break me off a piece of that.

So eat great, even late
Because if you’re hungry, why wait?
Except patience is a virtue,
So don’t stop believin’ but
Stop, in the name of love.

Because maybe the meaning of life isn’t money or knowledge; maybe the meaning of life is love.

What’s love got to do with it? (Got to do with it?) Well, love conquers all, And even if you’ve lost that lovin’ feeling, Know that it’s better to have loved and lost than to never have loved at all.

Because there are plenty of fish in the sea,
And when love is in the air
You’ll be walking on cloud nine.
But when it rains it pours,
And if you’re under the weather
And can’t see through the fog
We may not see eye-to-eye.

If love is blind
And hindsight is 20/20,
Then is love at first sight
Really meant to be?

Or not to be? That’s the question.
And if you’ve got questions, we’ve got answers,
If you can do it, we can help,
Because when you’re here, you’re family,
And family matters
As you step by step
Through the wonder years.

Because what goes up, must come down,
What goes around, comes around.
There’s nothing to fear but fear itself.
To live and learn
You have to crash and burn,
And the only failure is quitting.

So what are you waiting for?
To have the time of your life.
You have to find the time
To live a life worth living
So stop! Hammertime.

Maybe the meaning of life isn’t money, knowledge, or love. Maybe the meaning of life is to find meaning in life. Or maybe it’s milkshakes; I don’t know.
```

---

## IC-1533: Code Orange and The Good News

- Title: Code Orange and The Good News
- Author (byline): Matt Mason
- Work: Things We Don't Know We Don't Know
- Publisher: The Backwater Press
- Publication date as stated: March 2006
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 666
- Already set (do not supply): none

### Source block (context only)

```text
Author: Matt Mason
Book: Things We Don't Know We Don't Know
ISBN: 978-0976523185
Publisher: The Backwater Press
Date (Month/Year): March 2006
```

### Introduction (context only: never use it for content warnings)

```text
Secretary of Defense, Donald Rumsfeld once said . . . . "There are known knowns. These are things we know that we know. There are known unknowns. That is to say, there are things that we know we don't know. But there are also unknown unknowns. There are things we don't know we don't know."

How do you conduct your life in this time of terror when every day is Code Orange by Mat Mason
```

### Performance text (classify this)

```text
Code Orange It's not always

the little boy who cries

Wolf!

sometimes
the wolf
cries
wolf

and

points away.

Duct tape your doors shut, we're on Code Orange, Code Orange, people, blue skies

no matter, there's anthrax somewhere, somebody said something about smallpox

wherever, an unnamed man reportedly said something

big was coming down

eventually. A man said
people were going to die,
people are going to die,
Americans are going to die.

Officials are quoted as saying things,
officials are quoted as saying, Hurry, hurry, run,
seal yourself in a ziplock bag
in a lead-walled box
in a hole
in the earth
in prayer to our God,

and sources report
we aren't ready, we're not scared enough
and if we
don't get a little more hysterical,
then the terrorists will win

because sources suggest it could be any day, hour, minute, second,

duck! it could be any metropolis, city, small town, farmstead, or possibly even somewhere else; for God's sake, there are

experts

saying
we're not safe, we're not safe,
now do what we say
and nobody gets hurt.

There's fear
out past your walls, there's fear itself
blowing against the plastic sheeting and the bars of grey
tape,
there's so much
to fear, we must do more,
we have to fight them,
kill them, cripple them
for Jesus,

Amen!

It's not always

the little boy

who cries

Wolf! Sometimes the wolf

cries wolf.

And it's not always the wolf our little boys are sent out to kill.

TRANSITION So how DO you conduct your life in this time of terror? Who do you turn to for re-assurance? Who provides that peace for you? Perhaps, if you could find Jesus in everyday situations, and not get wrapped up in the seriousness of life, He could be the solace for you too. That’s The Good News by Matt Mason.

The Good News Jesus lent me ten bucks when I forgot my wallet at lunch. Sure, he could've ordered a chicken pesto sandwich and broke it into two full meals, but he's no show off. That's what I like about Jesus.

Jesus listens to cool music. If it weren't for Jesus, I never would have known about Tom Waits or Ani DiFranco, and I sure wouldn't own any Lyle Lovett.

But Jesus makes a kickass mix tape.

Jesus loves cows,
thinks my poems with cows in them are a hoot
and encourages me
to look at herds of white cows
in a green field
and imagine salvation
is underneath each windmill.

Jesus tells me Pat Robertson's right,
and so is Al Sharpton.
That they're both wrong, too,
but that's not the point.
His point's how God's sewn into every fabric.
Even yourself. Even Elvis.

Jesus saves and Jesus recycles.

Jesus eats fish for more
than Omega-3 fatty acids,
drinks red wine for more reasons
than his sacred heart.

Jesus doesn't dress like the Medieval paintings
with the gold hats and the Mr. T rosaries.
Sure, he can clean up nice,
but Jesus likes blue jeans.

Jesus pisses me off
with his honesty
sometimes.
But it's not like he's ever wrong.

Jesus makes a killer chianti,
but he refuses to turn water
into Diet Coke for me.
"What's the difference?" he asks.

Jesus acts real serious
when somebody rushes up to him hollering, "Jesus,
can you take me up to Heaven,
I will see you in the Kingdom, Jesus!"
Jesus says they should get their kumbayayas off
by putting on some overalls
and hammering in the morning.
May as well make Heaven bigger,
not just your egos.

Jesus digs the "How does Jesus eat M&M's" joke. He won't do it at a party, but he did do it once when just the two of us were watching cartoons.

Jesus wanted me to tell you he loves you. Jesus also wants you to stop doing that thing.

Jesus tells me I'm saved. Then he laughs real loud. Jesus makes me nervous when he does that.
```

---

## IC-1534: Collection from Chasing Utopia: A Hybrid

- Title: Collection from Chasing Utopia: A Hybrid
- Author (byline): Nikki Giovanni
- Work: Chasing Utopia: A Hybrid
- Publisher: William Morrow Paperbacks
- Publication date as stated: Sept 2016
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 936
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nikki Giovanni
Book: Chasing Utopia: A Hybrid
ISBN: 978-0062562883
Publisher: William Morrow Paperbacks
Date (Month/Year): Sept 2016
```

### Introduction (context only: never use it for content warnings)

```text
“Words are the lifeblood for writers.” Writers spend their days imagining just the right combination of words put together in such a way that a beautiful sentence or idea emerges. When this happens, what is written can actually take the reader beyond the page - creating images, pictures, colors, sounds, and smells that transport the reader to another world, a world beyond the everyday realities of life.

In this collection of poetry from Chasing Utopia by Nikki Giovanni, the joy of words is celebrated.
```

### Performance text (classify this)

```text
FOR HAKI MADHUBUTI (a prose poem)

Words are the lifeblood of writers. Though I must admit I don't know if we dream in words or if we word our dreams.

Words are like quilts. You have to put a bunch together to make something warm and comforting or patch together something that will prick and scratch the spirit. No matter how we weave this experience, we sculpt an idea and shape a phrase.

A phrase. Usually we find phrases to describe whatever it is. No word is sufficient to stand alone. Not even strong words like FREEDOM or soft words like LOVE. They all are better when added to . . . for example FOR ALL . . . or je t'aime. Love phrases work in all languages. The human experiment has turned on many important phrases WE THE PEOPLE, taxation without representation and even things like REMEMBER THE MAINE. There are other political phrases like LIBERTE, EGALITE, FRATERNITE. I especially like WE SHALL OVERCOME. There are personal phrases like Yes. Which may be the only one-word phrase we ever use. No requires a bit more. There are personal phrases such as You Look Beautiful and I am so proud of you but maybe that's a sentence not a phrase.

The human imagination is the engine that has carried us from caves in Europe, from the rain forests of South America, from the lush and mineral-rich lands of Africa, from the beautiful amber waves of North America, from the roaring seas and the frozen tundra, in fact, to wherever humans gather . . .

TRANSITION And one of the most beautiful uses of words is to create poetry . . . it is profoundly significant.

THE SIGNIFICANCE OF POETRY

Poetry is as necessary
To life
As salt is to stew
As garlic is to pasta
As perfume is to summer nights
As shaving lotion is to mornings
As your smile is to
My happiness
Poetry is as significant
To life
As yeast is to bread
As butter is to toast
As grapes are to wine
As sugar is to lemons
How else will we get Lemonade
Poetry is to me
Your voice
Your touch
Your laughter
That feeling at the end of day
That I am
Not alone

TRANSITION Lucille Clifton, an American poet from Buffalo, New York, explains . . . “The first poets didn’t come out of a classroom, that poetry began when somebody walked off of a savanna or out of a cave and looked up at the sky with wonder and said, “Ahhh.” That was the first poem. – Lucille Clifton I WISH I COULD LIVE (IN A BOOK)

(for Charles A. Smith, Jr.)

I wish I could live
In a book
All wrapped up
In my fairy Godmother's arms
Or sitting with my
Cave Mother baking dinosaur
Eggs
If I lived
In a book
I could fly With Ali Baba
And even though it's not right
To steal
The Forty Thieves are
Pretty cool
Maybe there would be
A book about me
One day
Just a little girl being brave
In a world where water
Is in short supply
But everybody
Has a gun
I don't think
That's a good idea
I'd rather be in
A book
Making biscuits
On the frontier

TRANSITION Poetry is described by Dennis Gabor as “plucking at the heartstrings, and making music with them.”

I WISH I COULD LIVE (IN MUSIC)

I wish I could live
In music
I'd be all
Kinds:
Opera arias
Folk telling news
Minuets
Hoedown dancing calling square dancers
Whoa!
Bring me some
Disco
Yeah I'd be a Spiritual
And then a wonderful
Foot-stomping
Gospel tune
Some blues-almost forgot
The Blues
And we need
Jazz
I need me "A-Tisket A-Tasket"
Some little yellow basket
But not a
White Horse
I'm never gonna ride
The White Horse
I want to be Little Richard
Even Donald Duck sang
Little Richard
I mean Quack Quack Quack
Won't You Come Along with Me?
Now I'm rappin' I'm telling the news
Napster freed me
And I can choose
To have it all
For free download
Yeah I want to live
In music
Teach
Learn
Rejoice
In music
In music I'm free
To be a better me
TRANSITION
Linda Besner writes . . . “Poetry is art made of words . . . I
would love it if all major cities had a poetry museum, where
you could go for a visit dressed up in your best all-black
clothes. The poems would be widely spaced on clean white
walls, big enough for four or five people at once to stand in
front of them and read.”

I WISH I COULD LIVE (IN A PAINTING)

There is something
About a railroad station
Not only the big pretty ones
Like in Cincinnati saying
"Gateway to the South"
or even Boston's Back Bay with
that heroic Tina Allen sculpture of A.
Philip Randolph
Union Station in DC ... union being
Not only North and South
But working men and women getting
A fair wage for giving
A hard day's work
And those greatest of Black Men . . .
the Pullman Porters . . .
Who set the style . . .
who took America from primitive to privilege
Giving service all through the night
Cooking the meals
Setting the tables
Washing . . .
pressing so others could look
Like gentlemen
Others sorted the mail
Which arrived
On time in the right city
No ZIP code needed thank you
These men could read
And no machine was invited
To that party
There is something about parallel
Lines moving up
And down over
Horizon and dreams never ever
Touching but rather on
A lonely journey with another
Lonely friend they don't talk
Though a song is sung
Parallel lines . . . not sea
Nor sky . . . hold the dreams
Of women
I wish I lived
In a painting
```

---

## IC-1535: A Collection of Childhood

- Title: A Collection of Childhood
- Author (byline): Not specified
- Work: Poetry U.S.A (edited by Paul Molloy)
- Publisher: Scholastic, Inc
- Publication date as stated: Jan 1968
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1134
- Already set (do not supply): none

### Source block (context only)

```text
All Poems found in
Book: Poetry U.S.A (edited by Paul Molloy)
ISBN: 978-0590355865
Publisher: Scholastic, Inc
Date (Month/Year): Jan 1968
```

### Introduction (context only: never use it for content warnings)

```text
Childhood was a time when the world felt endless, and every corner held a new adventure. You see, kids have a unique way of seeing the world -- like turning a stick into a horse or imagining bending trees as part of a game instead of signs of bad weather. Childhood is a precious chapter in life that shapes our sense of wonder, joy, and connection. It’s a time when the world feels full of possibilities, and every day is an adventure waiting to unfold. These early experiences shape how we see the world and who we become. And as we grow older, childhood memories remind us of the joy and wonder we once felt. My wish for all of us is that we can always hold on to that sense of magic. . .

A Collection of Childhood Memories with poems by Theodore Roethke, May Swenson, Robert Fitzgerald, Robert Frost and Galway Kinnell
```

### Performance text (classify this)

```text
Memories With Poems by Theodore Roethke, May Swenson, Robert Fitzgerald, Robert Frost and Galway Kinnell

My Papa’s Waltz by Theodore Roethke (Pg 18)
The whiskey on your breath
Could make a small boy dizzy;
But I hung on like death:
Such waltzing was not easy.

We romped until the pans
Slid from the kitchen shelf;
My mother’s countenance
Could not unfrown itself.

The hand that held my wrist
Was battered on one knuckle;
At every step you missed
My right ear scraped a buckle.

You beat time on my head
With a palm caked hard by dirt,
Then waltzed me off to bed
Still clinging to your shirt.

The Centaur by May Swenson (Pg 19-21)
The summer that I was ten–
Can it be there was only one
summer that I was ten? It must
have been a long one then–
each day I'd go out to choose
a fresh horse from my stable

which was a willow grove down by the old canal. I'd go on my two bare feet.

But when, with my brother's jack-knife, I had cut me a long limber horse with a good thick knob for a head,

and peeled him slick and clean except a few leaves for the tail, and cinched my brother's belt

around his head for a rein, I'd straddle and canter him fast up the grass bank to the path,

trot along in the lovely dust
that talcumed over his hoofs,
hiding my toes, and turning
his feet to swift half-moons.
The willow knob with the strap
jouncing between my thighs

was the pommel and yet the poll of my nickering pony's head. My head and my neck were mine,

yet they were shaped like a horse. My hair flopped to the side like the mane of a horse in the wind.

My forelock swung in my eyes, my neck arched and I snorted. I shied and skittered and reared,

stopped and raised my knees, pawed at the ground and quivered. My teeth bared as we wheeled

and swished through the dust again.
I was the horse and the rider,
and the leather I slapped to his rump
spanked my own behind.
Doubled, my two hoofs beat
a gallop along the bank,

the wind twanged in my mane, my mouth squared to the bit. And yet I sat on my steed

quiet, negligent riding, my toes standing the stirrups, my thighs hugging his ribs.

At a walk we drew up to the porch. I tethered him to a paling. Dismounting, I smoothed my skirt

and entered the dusky hall. My feet on the clean linoleum left ghostly toes in the hall.

Cobb Would Have Caught It by Robert Fitzgerald (Pg 37)

In sunburnt parks where Sundays lie, Or the wide wastes beyond the cities, Teams in grey deploy through sunlight.

Talk it up, boys, a little practice.

Coming in stubby and fast, the baseman Gathers a grounder in fat green grass, Picks it stinging and clipped as wit Into the leather: a swinging step Wings it deadeye down to first. Smack. Oh, attaboy, attaoldboy.

Catcher reverses his cap, pulls down Sweaty casque, and squats in the dust: Pitcher rubs new ball on his pants, Chewing, puts a jet behind him; Nods past batter, taking his time. Batter settles, tugs at his cap: A spinning ball: step and swing to it, Caught like a cheek before it ducks By shivery hickory: socko, baby: Cleats dig into dust. Outfielder, On his way, looking over shoulder, Makes it a triple. A long peg home.

Innings and afternoons. Fly lost in sunset. Throwing arm gone bad. There's your old ball game. Cool reek of the field. Reek of companions.

Birches by Robert Frost (Pg 92-93)
When I see birches bend to left and right
Across the lines of straighter darker trees,
I like to think some boy’s been swinging them.
But swinging doesn’t bend them down to stay
As ice-storms do. Often you must have seen them
Loaded with ice a sunny winter morning
After a rain. They click upon themselves
As the breeze rises, and turn many-colored
As the stir cracks and crazes their enamel.
Soon the sun’s warmth makes them shed crystal shells
Shattering and avalanching on the snow-crust—
Such heaps of broken glass to sweep away
You'd think the inner dome of heaven had fallen.
They are dragged to the withered bracken by the load,
And they seem not to break; though once they are bowed
So low for long, they never right themselves:
You may see their trunks arching in the woods
Years afterwards, trailing their leaves on the ground
Like girls on hands and knees that throw their hair
Before them over their heads to dry in the sun.
But I was going to say when Truth broke in
With all her matter-of-fact about the ice-storm
I should prefer to have some boy bend them
As he went out and in to fetch the cows—
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

So was I once myself a swinger of birches. And so I dream of going back to be.

First Song by Galway Kinnell (Pg 123)

Then it was dusk in Illinois, the small boy
After an afternoon of carting dung
Hung on the rail fence, a sapped thing
Weary to crying. Dark was growing tall
And he began to hear the pond frogs all
Calling on his ear with what seemed their joy.

Soon their sound was pleasant for the boy Listening in the smoky dusk and the nightfall Of Illinois, and from the fields two small Boys came bearing cornstalk violins And they rubbed the cornstalk bows with resins And the three sat there scraping of their joy.

It was now fine music the frogs and the boys
Did in the towering Illinois twilight make
And into dark in spite of a shoulder's ache
A boy's hunched body loved out of a stalk
The first song of his happiness, and the song woke
His heart to the darkness and into the sadness of joy.
```

---

## IC-1536: Collection on Cancer

- Title: Collection on Cancer
- Author (byline): Robert W. King, Mark Ritvo and Steve Kantor
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 780
- Already set (do not supply): none

### Source block (context only)

```text
Author: Max Ritvo
Book: Four Reincarnations: Poems (Pg 65)
ISBN: 978-1571314901
Publisher: Milkweed Editions
Date (Month/Year): October 4, 2016
NOTE: Also found on Poets.org (Approved NDSA
Author: Robert W. King
Book: Nimrod International Journal, Volume 58.2)
ASIN: B0011E9UQE
Publisher: University of Tulsa
Date (Month/Year): 2015
Author: Max Ritvo
ISBN: N/A
Publisher: Poets.org (Approved NSDA Website)
Weblink: https://poets.org/poem/cachexia
Author: Kevin Kantor
Book: Endowing Vegetables with too much
Meaning (Pg 10)
ISBN: 978-1512133417
Publisher: CreateSpace Independent Publishing Platform
Date (Month/Year): July 16, 2015
```

### Introduction (context only: never use it for content warnings)

```text
Cancer has traditionally been the diagnosis people fear most. But is dying from cancer so much worse than the alternatives? The advantage of death from cancer is that while it is possible to live with this disease for a long time, the dying process happens relatively fast, yet slow enough to give time for yourself and those around you to prepare for your death and say goodbye. This collection imagines cancer through various metaphors . . . but in the end, cancer takes on its own voiced persona and speaks to us directly. A Collection on Cancer by Robert W. King, Mark Ritvo and
```

### Performance text (classify this)

```text
Touching the Floor
I touch my palms to the floor
and granite rhinos surge up my arms
and lock in my shoulders.
Water flecks on my back
and my head is shaved
by bladed cream.

But then my time in my body is up
and it’s time for my mind:
It seeks wisdom
and the rhinos fall into a well,
their faces falling apart—

I want to know what their last words are but their lips are fading into the purple.

I put my hands into the ground again but rhinos come only for the body and never for the mind.

I used to want infinite time with my thoughts.
Now I’d prefer to give all my time
to a body that’s dying
from cancer.

website) at https://poets.org/poem/touching-floor Steve Kantor.

Embedding the Cancer Port It's called a port, a harbor, haven, home, a city on the coast of my chest opened for a passage into my heart—which we say is where emotions live—and it's embedded,

slipped into a shallow nest of flesh, a bump, a lump under the skin on the right so the narrow street can reach the marketplace of the aorta, receptive to any incoming ship, needle, boat, barge, unloading its spices, crates of dates, barrels of poisons, Etoposide phosphate, amethyst, amaranth, Cisplatin, amphorae of wine and olives.

I carry it secretly under my skin
because it is easier. I carry
everything under my skin, so lightly
I barely notice, watching from the ramparts

the dangerous rocky anchorage below
where goods and evils, bundled together
and tied, arrive, waiting to be unloaded
and poured out into a welcoming country.

Cachexia

(wasting of the body due to sever chronic illness)

Today I woke up in my body and wasn’t that body anymore.

It’s more like my dog—
for the most part obedient,
warming to me
when I slip it goldfish or toast,

but it sheds. Can’t get past a simple sit, stay, turn over. House-trained, but not entirely.

This doesn’t mean it’s time to say goodbye.

I’ve realized the estrangement is temporary, and for my own good:

My body’s work to break the world into bricks and sticks has turned inward.

As all the doors in the world grow heavy a big white bed is being put up in my heart.

A Letter from Cancer

Dear Lover,

These buzzing fluorescents have you looking a little

pale, Just a little washed out.

And all this antiseptic is far from complimenting that

perfume. This linoleum will make your most stylish pair of pumps

look cheap.

Sweetheart, you look tired. I'll never understand how it is that you don't see it.

How terribly beautiful you are. Look in the mirror.

I'm in all the dark spots. The hallowed slopes

In your eyes and beneath them Your color it's just so delicious.

Listen to the sound of my voice To these sweet nothings.

I will love your everything. Every multicolored malignancy.

Raw and heaving. Breathe with me, bleed out with me

We will waste away together. Hush now.

I will hold you through these tremors. It is just the way that we dance, baby.

Listen to the music This mutation is orchestral, this spreading so symphonic.

Split cells 2 by 2 by 4 Watch our love spread.

Lover, why do you want me dead? I will show you heaven, baby.

Give you the stars and the sun Those are sunspots on your lungs.

You can't just tie a ribbon around me, cough me up. Really now? Did you think i'd go that easy?

That I'd ever think to up and leave you. Rest darling, lay down.

You know how I love to lay rivers Through your shattered glass veins.

Your heart is just as big as they all said it was, But not as strong.

All of that veined pride as I'm pumping. I know that poker-face all too well.

You will love me. I gave you my sun. love me.

Deadly I'll make you an angel. Love me, I'll make you feel radiance.

You will meet me there. In 9 months or 6 months or 3.

They try to time-stamp our love, expiration date us But take your time. I'll wait for you.

Quite impatient as you wake on night With a stitch in your side or wasp in your brain.

And you will know, I've come back for you.

I will always come back for you, darling We will look so beautiful laid out with all the wilted lilies.

They will weep for everything that you were And for everything you will never be

Without me. Lover, it is my understanding that you want me dead.

Fine Die with me.
```

---

## IC-1537: A Collection on Suicide

- Title: A Collection on Suicide
- Author (byline): Patrick Roche and Jared Singer
- Work: Forgive Yourself These Tiny Acts of Self- Destruction
- Publisher: Button Poetry
- Publication date as stated: Dec 2019
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 953
- Already set (do not supply): none

### Source block (context only)

```text
Author: Philip Roche
ISBN: NSDA Approved Website
https://themighty.com/2019/06/slam-poetry-mental-
illness/
Publisher: The Mighty.com
Date (Month/Year): June 27, 2019
*NOTE: Lines from Every 40 Seconds are shown in
BLACK
Author: Jared Singer
Book: Forgive Yourself These Tiny Acts of Self-
Destruction
ISBN: 978-1943735617
Publisher: Button Poetry
Date (Month/Year): Dec 2019
*NOTE: Lines from I Have Never Been Suicidal are
shown in GREEN
*NOTE: Lines from A Letter to Sarah Contemplating
Super Powers are shown in ORANGE
```

### Introduction (context only: never use it for content warnings)

```text
Every 40 seconds . . . by the end of this presentation 10 people will have taken their lives.

A Collection on Suicide containing Every 40 Seconds by Patrick Roche, I Have Never Been Suicidal and A Letter to Sarah Contemplating Super Powers by Jared Singer
```

### Performance text (classify this)

```text
Contains the following color-coded, interspersed poems:

Every 40 Seconds by Patrick Roche

•

I Have Never Been Suicidal by Jared Singer

•

A Letter to Sarah . . . by Jared Singer

• NOTE: Each poem should have a different voice for the most impactful presentation

Every 40 seconds. This is not a list poem. This is a eulogy for those swallowed by their own minds. This is a call to arms, a call to speak. This is not family gatherings when I mention mental health and am told not to spoil the turkey, That it is uncouth, impolite, That it is better to stay silent. This is taking that silence and breaking it with my hands, with my teeth and tongue. This is people with mental illness banging our heads against the walls, not out of insanity but to try to make some noise, to be heard.

Too often we are ashamed, too often we are in the shadows. In 2014, the World Health Organization released a report stating that at least 800,000 people commit suicide every year. That averages to 1 person every 40 seconds.

I have never been suicidal, never wanted to kill myself

I have always believed that life is a gift. Sometimes it’s a gift you don’t want,

an itchy sweater you wish you could return. I have never wanted to kill myself,

but I have wanted to die Prayed for it.

Every 40 seconds.
Suicide is not always a banshee wailing against your
eardrums, it is a child playing hide-and-seek behind your
friends smile.
They will not wear it openly, they cannot hold it's hand
and introduce it to you, it is always invisible.
Suicide is a lonely ghost desperate to give itself
playmates.
If you’d only told us something was wrong
we could’ve held you
told you we loved you.
We could have helped.
[Suicide] is not a permanent solution to a temporary
problem, these are so rarely temporary problems.
It is aiming for a long nights sleep after years of
insomnia.
It is the seduction of safety and simplicity.
Sometimes it is careful planning;
Drafting the note . . . . Every 40 seconds.
If I could travel through time,
I would go back to the moment
before it was too late.
Right before the moment you wrote a suicide note
that started Dear Jared:

Inspecting your apartment for beams that can support
your weight.
Or it is a flip switch given the right trigger, or no
trigger at all.
It is painting a target on the highway divider.
It is imaging the phone call my mother will get in the
middle of a nap.
Sometimes it is sudden, it is not always arriving-
At the most convenient time but the clock keeps ticking.
Every 40 seconds.
I’d always thought that despair
would feel empty. That’s how it’s
always described. It isn’t --
it is full and terror-cold.
I am happier than I have ever been.
I still have a hard time believing in myself,
use the word broken too much.

I have never been suicidal, but now I love the living.
I stopped looking at life as good or bad, a series
of snapshots where each was either a reason
to live or a reason to die.
I have not always wanted to live. For a long time I
couldn’t even imagine what joy would feel like.
It’s a melody. It’s a tide. It is full and warm.
Every 40 seconds.
This is not a list poem.
This is the tea kettle rising to a soprano screech but you
keep ignoring it to watch TV,
It keeps whistling and crying but you keep ignoring it;
How much noise do I have to make?
When we tell you we are suicidal, it is a cry for help but
that's not a sign of weakness.
This is not a sign of weakness.
This is saying we're fighting and
and we've been fighting with every weapon
and fist we have.
We've crashed against the cliff side, broken and
splintered, but we're still fighting with whatever we can.
I'm using my voice, it's all I have left.
Every 40 seconds.
If I could regenerate any damage to my body,
I would double back flip belly flop
off the tallest building I could find.
I would make you watch.
Would not tell you it won’t kill me.
When my body hits the ground,
turns bone to dust,
when blood splatters across your face
there will be a moment
where your heart stops,
where the belly drops out of your everything.
I would calmly walk over to you and say
yeah, ever since you killed yourself
it’s been like that for all of us
All of the time.
Over the years, I've written different versions of my
suicide note.
On the nights I almost took my life, I always deleted or
threw away the note rather than sending it or leaving it
for someone, I assumed the words would just make them
uncomfortable.
I’m doing this now because I know you will be the one to
find me
because of all of my friends I think you’re the one
whose strong enough to take it.
What made you think I was strong enough to take this?
If I'm going to die, better to do it without all that fuss;
better to do it in silence.
Hundreds of thousands of people are dying in silence and
because of silence.
If you’d only told us something was wrong
we could’ve held you
told you we loved you.
We could have helped.
This is not a list poem, this is saying we can keep each
other breathing.
This is speaking louder than the stigma and hoping
someone will listen
```

---

## IC-1538: The Coming of Archy and Mehitabel and her Kittens

- Title: The Coming of Archy and Mehitabel and her Kittens
- Author (byline): Don Marquis
- Work: Archy and Mehitabel
- Publisher: Random House, Inc.
- Publication date as stated: Sept 1987
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1101
- Already set (do not supply): none

### Source block (context only)

```text
Author: Don Marquis
Book: Archy and Mehitabel
ISBN: 978-0385094788
Publisher: Random House, Inc.
Date(Month/Year): Sept 1987
```

### Introduction (context only: never use it for content warnings)

```text
In 1916, Marquis introduced a fictional cockroach named "Archy" into his daily newspaper column at the New York Tribune. Archy's best friend was an alley cat named "Mehitabel," and the two of them shared a series of day-to-day adventures that made satiric commentary on daily life in the city during the 1910's and 20's. The Coming of Archy and Mehitable and her Kittens by Don Marquis
```

### Performance text (classify this)

```text
We came into our room earlier than usual in the morning, and discovered a gigantic cockroach jumping about upon the keys. He did not see us, and we watched him. He would climb painfully upon the framework of the machine and cast himself with all his force upon a key, head downward, and his weight and the impact of the blow were just sufficient to operate the machine, one slow letter after another. He could not work the capital letters, and he had a great deal of difficulty operating the mechanism that shifts the paper so that a fresh line may be started. We never saw a cockroach work so hard or perspire so freely in all our lives. After about an hour of this frightfully difficult literary labor he fell to the floor exhausted. Congratulating ourselves that we had left a sheet of paper in the machine the night before so that all this work had not been in vain, we made an examination, and this is what we found

The Coming of Archy

expression is the need of my soul i was once avers libre bard but i died and my soul went into the body of a cockroach it has given me a new outlook upon life i see things from the under side now thank you for the apple peelings in the wastepaper basket but your paste is getting so stale i cant eat it there is a cat here called mehitabel i wish you would have removed she nearly ate me the other night why dont she catch rats that is what she is supposed to be for there is a rat here she should get without delay most of these rats here are just rats but this rat is like me he has a human soul in him he used to be a poet himself night after night i have written poetry for you on your typewriter and this big brute of a rat who used to be a poet comes out of his hole when it is done and reads it and sniffs at it he is jealous of my poetry he used to make fun of it when we were both human he was a punk poet himself and after he has read it he sneers and then he eats it i wish you would have mehitabel kill that rat or get a cat that is onto her job and i will write you a series of poems showing how things look to a cockroach that rats name is Freddy the next time freddy dies i hope he wont be a rat but something smaller i hope i will be a rat in the next transmigration and freddy a cockroach i will teach him to sneer at my poetry then archy TRANSITION Mehitabel has a weakness for bad-boy tomcats and pals around with other up-to-no-good street cats. Archy repeatedly tries to encourage Mehitabel to clean up her act and get a job as a nice house kitten where she can be taken care of. But Mehitabel is taking no advice from Archy . . . afterall, she’s her own woman, errr. Cat. . . . Mehitabel and her Kittens

Mehitabel and her Kittens

well boss
mehitabel the cat
has reappeared in her old haunts with a
flock of kittens
three of them this time
archy she said to me yesterday
the life of a female artist is continually hampered what
in hell have i done to deserve all these kittens
i look back on my life and it seems to me to be just one
damned kitten after another
i am a dancer archy and my only prayer is to be allowed
to give my best to my art
but just as i feel
that i am succeeding
in my life work
along comes another batch
of these damned kittens
it is not archy
that i am shy on mother love god knows i care for
the sweet little things
curse them
but am i never to be allowed to live my own life
i have purposely avoided matrimony in the interests
of the higher life
but i might just
as well have been a domestic slave for all the freedom
i have gained
i hope none of them
gets run over by
an automobile
my heart would bleed
if anything happened
to them and i found it out
but it isn t fair archy
it isn t fair
these damned tom cats have all the fun and freedom
if i was like some of these green eyed feline vamps i
know i would simply walk out on the bunch of them and
let them shift for themselves but i am not that kind
archy i am full of mother love my kindness has always
been my curse
a tender heart is the cross i bear self sacrifice always
and forever is my motto damn them
i will make a home
for the sweet innocent
little things .
unless of course providence
in his wisdom should remove them they are living
just now in an abandoned garbage can just behind
a made over stable in greenwich village and if it rained
into the can before i could
get back and rescue them
i am afraid the little
dears might drown
it makes me shudder just
to think of it
of course if i were a family cat they would probably
be drowned anyhow sometimes i think
the kinder thing would be
for me to carry the
sweet little things
over to the river
and drop them in myself
but a mother’s love archy
is so unreasonable
something always prevents me these terrible
conflicts are always
presenting themselves
to the artist
the eternal struggle
between art and life archy
is something fierce
yes something fierce
my what a dramatic
life i have lived
one moment up the next
moment down again
but always gay archy always gay and always the lady too
in spite of hell
well boss it will
be interesting to note
just how mehitabel
works out her present problem a dark mystery still
broods over the manner
in which the former
family of three kittens disappeared
one day she was talking to me of the kittens
and the next day when i asked her about them
she said innocently
what kittens
interrogation point
and that was all
i could ever get out
of her on the subject
we had a heavy rain
right after she spoke to me but probably that garbage
can leaks and so the kittens
have not yet
been drowned
archy
```

---

## IC-1539: Commercial Break and Midnight

- Title: Commercial Break and Midnight
- Author (byline): Tim Seibles
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1190
- Already set (do not supply): none

### Source block (context only)

```text
Author: Barbara Cameron
ASIN: B0076XDT08
Publisher: BSX Records
Date (Month/Year): Feb 2012
Author: Tim Seibles
Book: Hammerlock
ISBN: 978-1880834459
Publisher: Cleveland State U Poetry Center
Date (Month/Year): Jan 1999
Author: Tim Seibles
Book: Hammerlock
ISBN: 978-1880834459
Publisher: Cleveland State U Poetry Center
Date (Month/Year): Jan 1999
```

### Introduction (context only: never use it for content warnings)

```text
Do you remember the old Saturday morning cartoon? The Road Runner Show! The one where there was no dialogue and the only line ever uttered was “Meep-Meep!” And yet we were mesmerized by the entire premise of the cartoon. We knew Wile E Coyote would never catch and eat the Road Runner, but watching his wide variety of failures was something we eagerly awaited every weekend. Tim Seibles explores the inner thoughts of both the Road Runner and the Coyote in these poems: Commercial Break and Midnight.
```

### Performance text (classify this)

```text
(Singing) If you're on a highway and Road Runner goes beep beep. Just step aside or you might end up in a heap. Road Runner, Road Runner runs down the road all day. Even the coyote can't make him change his ways.

Road Runner, the coyote's after you. Road Runner, if he catches you you're through.

That coyote is really a crazy clown,
When will he learn that he never can mow him down?
Poor little Road Runner never bothers anyone,
Just runnin' down the road's his idea of having fun.

Lyrics and Music can be found at: https://www.youtube.com/watch?v=XuemcUasZ5E

Commercial Break: Road-Runner, Uneasy

If I didn't know better I'd say
the sun never moved ever,
that somebody just pasted it there
and said the hell with it,
but that's impossible.
After a while you have to give up
those conspiracy theories.
I get the big picture. I mean,
how big can the picture be?
I actually think it's kind of funny —
that damn coyote always scheming,
always licking his skinny chops
and me, pure speed, the object of all
his hunger, the everything he needs —
talk about impossible, talk about
the grass is always greener...
I am the other side of the fence.
You've got to wonder, at least a little,
if this could be a set-up:
with all the running I do —
the desert, the canyons, the hillsides, the desert —
all this open road has got to
lead somewhere else. I mean,
that's what freedom's all about, right?
Ending up where you want to be.
I used to think it was funny — Roadrunner
the coyote's after you Roadrunner...
Now I'm mainly tired. Not that
you'd ever know. I mean
I can still make the horizon
in two shakes of a snake's tongue,
but it never gets easier out here, alone
with Mr. Big Teeth and his ACME supplies:
leg muscle vitamins, tiger traps,
instant tornado seeds.
C'mon! I'm no tiger.
And who's making all this stuff?
I can't help being a little uneasy.
I do one of my tricks,
a rock-scorching, razor turn at 600 miles an hour,
and he falls off the cliff, the coyote —
he really falls: I see the small explosion,
his body slamming into dry dirt
so far down in the canyon
the river looks like a crayon doodle.
That has to hurt, right?
Five seconds later, he's just up the highway
hoisting a huge anvil
above a little, yellow dish of bird feed —
like I don't see what's goin' on. C'mon!
You know how sometimes, even though you're
very serious about the things you do,
it seems like, secretly, there's a
big joke being played,
and you're part of what
someone else is laughing at — only
you can't prove it, so you
keep sweating and believing in
your career, as if that
makes the difference, as if somehow
playing along isn't really
playing along as long as you're
not sure what sort of fool
you're being turned into, especially
if you're giving it one-hundred percent.
So, when I see dynamite
tucked under the ACME road-runner cupcakes,
as long as I don't wonder why my safety
isn't coming first in this situation,
as long as I don't think me
and the coyote are actually
working for the same people,
as long as I eat and
get away I'm not really stupid,
right? I'm just fast.

TRANSITION

Over the years, poor Wile E. Coyote suffered a lot of heartache and physical pain in his quest for sustenance. It almost seemed like he’d been cursed, and he was, in fact — by none other than animator Chuck Jones. Wile E. Coyote, genius. Who else would think of such elaborate schemes to get a meal? Does it matter that all of his schemes failed? It may have left him perpetually hungry, but it doesn’t change his status as one of the most creative and undaunted coyotes around. Midnight by Tim Seibles Midnight: The Coyote, Down in the Mouth

I used to sleep so well. My mother could carry me by the neck scruff without waking me up.

Even the dark tasted good with the quite noise of family around me,

and sunrise simply meant I could catch grasshoppers drunk on due.

Of course I didn’t know the roadrunner then and whatever I wanted seemed nearby and easy.

Now, I close my eyes and he’s there
in slow motion technicolor
all a-trot. His heart like a little tom-tom
loud enough to be visible in that bony chest.

Come morning, it will be the same, but hotter. A buzz of shins, the road sizzling like a fuse. Meep. . . . Meep . . .

I used to believe what I did mattered in
some spectacular way
As if a big audience sat somewhere
really watching
really wondering
how well I would do out here.

At first I thought it was only a matter of time.
I’d put on a bib,
pick up some silverware,
duck behind a cactus,
just to ham it up a little.

He was mine.

I figured a few near misses for suspense, then CHOMP – the good life, of course.

I’ve been after the roadrunner for so long, I can’t tell if it’s hunger, love, or just plain stupidity.

Maybe that’s what’s so goddamn funny.

My life whittled down to a
riot of while pursuits and slim chances
to grab something that
I don’t even understand.

I mean, if I had his speed,
I’d get the hell away from here.
I’d be so gone,
even color couldn’t catch me.
It’s crazy. . .

I’ve died lots of times. LOTS!
blown up,
bowled over by boulders,
run over by trucks.

Somedays when I’m a thousand feet below the ledge
and a thousand more from impact,
I stop and look up at that
pebble-headed feather duster
and touch my chin. . . .

Who keeps bringing me back?

How can I keep hitting the ground and
getting up with nothing but
another perfect scheme.
It’s got to end somewhere doesn’t it?

There’s got to be some way to . . . . I don’t even want to be a coyote anymore.

carnivirest sharpest toothiest.

It’s not me.

It’s like my appetite doesn’t belong in my belly. Like I’m hungry because someone else wants to eat.

Like I’m stuck in this story
no matter how bad I want to get out.
and me trying to get out of the story
IS the story.

Of course, I think my life means something and of course, it does.

Otherwise, I’d be running around all the time . . .
and there would be no . . .
it would seem like my life had been . . .
I mean, who hasn’t wondered, right?

But if this is not my life, then what am I doing and who should I ask?

Honestly,
if you can just stand still for a minute,
you start to see the whole show.
I mean, it’s all perspective.

If you can step out of the action long enough to catch your breath, you become your own audience.

And, of course, there you are,
a scrawny animal
starving in the middle of a desert
squeezing your knife and fork.
```

---

## IC-1540: A Coney Island of the Mind

- Title: A Coney Island of the Mind
- Author (byline): Lawrence Ferlinghetti
- Work: Not specified
- Publisher: New Directions Publishing
- Publication date as stated: Oct 1974
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 970
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lawrence Ferlinghetti
ISBN: 978-0811200417
Publisher: New Directions Publishing
Date(Month/Year): Oct 1974
```

### Introduction (context only: never use it for content warnings)

```text
By immersing ourselves in poetry we realize how the greatest poets not only change the way we see the world but also cause us to question our perception and interpretation of everyday reality. We realize that the greatest poetry "subverts the dominant paradigm," ultimately challenges the status quo of the world, and transforms it into something new and strange. Come with me to Lawrence Ferlinghetti’s Coney Island of the Mind in the decade after the end of World War II . . . the war to end all wars . . .
```

### Performance text (classify this)

```text
In Goya's greatest scenes we seem to see
the people of the world
exactly at the moment when
they first attained the title of
"suffering humanity"
They write upon the page
in a veritable rage
of adversity
Heaped up
groaning with babies and bayonets
under cement skies
in an abstract landscape of blasted trees
bent statues bats wings and beaks
slippery gibbets
cadavers and carnivorous cocks
and all the final hollering monsters
of the
"imagination of disaster"
they are so bloody real
it is as if they really still existed
And they do
Only the landscape is changed
They are still ranged along the roads
plagued by legionaries
false windmills and demented roosters
They are the same people
only further from home
on freeways fifty lanes wide
on a concrete continent
spaced with bland billboards
illustrating imbecile illusions of happiness
The scene shows fewer tumbrils
but more maimed citizens
in painted cars
and they have strange license plates
and engines
that devour America

Oh, Beautiful for spacious skies; for amber waves of grain . . . purple mountains . . . fruited plains; America the beautiful?

The poet's eye obscenely seeing
sees the surface of the round world
with its drunk rooftops
and wooden oiseaux on clotheslines
and its clay males and females
with hot legs and rosebud breasts
in rollaway beds
and its trees full of mysteries
and its Sunday parks and speechless statues
and its America
with its ghost towns and empty Ellis Islands
and its surrealist landscape of
mindless prairies
supermarket suburbs
steamheated cemeteries
cinerama holy days
and protesting cathedrals
a kissproof world of plastic toiletseats tampax and taxis
drugged store cowboys and Las Vegas virgins
disowned Indians and cinemad matrons
unroman senators and conscientious non-objectors
and all the other fatal shorn-up fragments
of the immigrant's dream come too true
and mislaid
among the sunbathers

America, America, God shed his grace on thee; and crowned they good with brotherhood. Brotherhood? What brotherhood?

In a surrealist year
of sandwichmen and sunbathers
dead sunflowers and live telephones
house-broken politicos with party whips
performed as usual
in the rings of their sawdust circuses
where tumblers and human cannonballs
filled the air like cries
when some cool clown
pressed an inedible mushroom button
and an inaudible Sunday bomb
fell down
catching the president at his prayers
on the 19th green

O it was a spring
of fur leaves and cobalt flowers
when the cadillacs fell thru the trees like rain
drowning the meadows with madness
while out of every imitation cloud
dropped myriad of wingless crowds
of nutless nagaski survivors
And lost teacups
full of our ashes
floated by

So pledge allegiance to America . . One nation under God; indivisible; with liberty and justice . . . but is it truly justice for all?

Sometime during eternity
some guys show up
and one of them
who shows up real late
is a kind of carpenter
from some square-type place
like Galilee
and he starts wailing
and claiming he is hip
to who made heaven
and earth
and that the cat
who really laid on us
is his Dad
And moreover
he adds
It's all writ down
on some scroll-type parchments
which some henchmen
leave lying around the Dead Sea somewheres
a long time ago
and which you won't even find
for a coupla thousand years or so
or at least for
nineteen hundred and fortyseven
of them
to be exact
and even then
nobody really believes them
or me
for that matter

You're hot they tell him And they cool him

They stretch him on the Tree to cool
And everybody after that
is always making models
of this Tree
with Him hung up
and always crooning His name
and calling Him to come down
and sit in
on their combo
as if he the king cat
who's got to blow
or they can't quite make it

Only he don't come down from His Tree

Him just hang there
on His Tree
looking real Petered out
and real cool
and also
according to a roundup
of late world news
from the usual unreliable sources
real dead

And yet why focus on foreign concepts such as liberty, beauty, justice, faith; when the average American’s world is only slightly larger than his/her own dinner plate, gas tank, city park . . so why worry? Americans of all people should have every opportunity to be happy!

In Golden Gate Park that day
a man and his wife were coming along
thru the enormous meadow
which was the meadow of the world
He was wearing green suspenders
and carrying an old beat-up flute
in one hand
while his wife had a bunch of grapes
which she kept handing out
individually
to various squirrels
as if each
were a little joke

And then the two of them come on
thru the enormous meadow
which was the meadow of the world
and then
at a very still spot where the trees dreamed
and seemed to have been waiting thru all time
for them
they sat down together on the grass
without looking at each other
and ate oranges
without looking at each other
and put the peels
in a basket which they seemed
to have brought for that purpose
without looking at each other

and then
he took his shirt and undershirt off
but kept his hat on
sideways
and without saying anything
fell asleep under it
And his wife just sat there looking
at the birds which flew about
calling to each other
in the silly air
as if they were questioning existence
or trying to recall something forgotten

But then finally
she too lay down flat
and just lay there looking up
at nothing
yet fingering the old flute
which nobody played
and finally looking over
at him
without any particular expression
except a certain awful look
of terrible depression
```

---

## IC-1541: Confronting American Apathy

- Title: Confronting American Apathy
- Author (byline): Ralph Black, Tony Hoagland and Raul Herrera
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1508
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ralph Black
Book: The Ecopoetry Anthology, Pgs 185-187
ISBN: 978-1595341464
Publisher: Trinity University Press
Date (Month/Year): Feb 2013
Author: Tony Hoagland
Book: What Narcissism Means to Me, Pgs 7-8
ISBN: 978-1555973865
Publisher: Graywolf Press
Date (Month/Year): Jan 2003
Author: Raul Herrera
Book: Get Lit Rising, Pgs 2-4
ISBN: 978-1582705774
Publisher: Simon Pulse/Beyond Words
Date (Month/Year): Oct 2016
```

### Introduction (context only: never use it for content warnings)

```text
Once upon a time in the United States of America, there lived a nation of citizens that showed tremendous interest in the state of their country’s well-being. With incredible zeal, these citizens worked tirelessly to correct any local, national or international issue that threatened them either as individuals or collectively, showing no fear and great resolve while addressing any elected or appointed public official that didn’t accurately represent their beliefs, ethics, morals and values. Once upon a time. . .

However, this state of involvement is no longer the norm for most U.S. citizens and hasn’t been for nearly 40 years. I ask you this: Are you happy with the direction our society is taking, or have you given up hope that any action you take will bring about change?

Confronting American Apathy through poetry: 21st Century Lecture by Ralph Black, America by Tony Hoagland and Earthquake by Raul Herrera
```

### Performance text (classify this)

```text
21st Century Lecture by Ralph Black (Pg 185-187)
Listen. You know what a torn shirt
the world's become. You know how thin
its fabric. You know what seams are,
and how your life, as though by accident,
settles in and trembles them apart.
And everyone knows you don't mean it.
So you say to yourself, don't be stupid.
You say, don't sham and swindle your way
through these stark desecrations,
don't stand around as your body's
warming waters rise, as they lift
and pool around the trunks
of three-hundred-year-old trees-

the ones that snatched away your breath

and all your words when you were a kid. Your tea is getting cold. The shirts you bought on a whim have to go back to the Singapore sweatshop. You're a smart enough guy, keening over the paper each morning, tuned in to just the right litany of fear – Baghdad, Darfur, the Bronx-the outstretched or instantly severed hand. You could turn the page from the steady unraveling of the planet's bright threads. But your throat rasps and freezes at the sight of the sea lion sow chewing the face off her newborn pup; at the Coho hatchlings spilling out of the hatchery flume, carrying their constellations of DNA up and against the river's age-old equations; at the polar bears starving at the edge of their ice. You know the word starving, you know the meaning of CO , you know

2 how apple seeds and smart bombs bloom, how simple it is to flay a range of hills, eviscerate a mountain with a spark. You know how the stones can keep you warm. You're not an idiot. You're not a fool. You won't let your heart-that tiny, glacial island-fracture and calve. You think your love for your children and your children's love for everything but homework and spinach should be plenty. The name of the wind is changing. The wind, which you know is your breath, and spills over flooded deltas, which churns through the gleaming thickets of oil refineries, fission factories, wind farms, water mills, think tanks, smelters, grinders, brothels, landfills, gun shops, billboards declaring the newest-brightest-best- You know how it fills you, how it lifts away from you the words you use to talk back to yourself late into the night. It's a very old wind, and you utter it over and over, a mantra, a koan, a playing out of words like an old uncle spiraling ten-pound test over his favorite run of rapids thirty miles up the East Fork of that river that spills now green and empty as an eye. You know all this. No one's telling you anything you haven't known for a hundred years. But your tongue says say it, just the same. Your mouth makes the shape of a call, a cry, an uneven song. You reach for a pen, tired as you are. You write it down, because stories and maps are the same. You think of the photograph you saw at the museum: a ten-year-old boy born blind who lost both his arms in his country's war.

He's at a desk, reading a book with his mouth.
He's leaning in and kissing the words,
in love with his own hunger.
He's doing with his whole body
everything he knows how to do.

TRANSITION

But what can I do, you ask . . . I can’t solve these problems. I’m just one person. OK – fine, let’s bring it down to an individual level. Let’s talk about consumerism: the obsession with acquisition that has become the organizing principle of American life. You are part of a culture in which the people will do most anything to acquire the means to consume — work slavish hours, maybe even two jobs, buy homes beyond their means and think nothing of running up credit card debt. We’ve reached a crisis point – a crisis of consumerism – What can you do? Choose wisely . . . choose to stop acquiring “things” . . . and according to Tony Hoagland . . . wake up.

America by Tony Hoagland (Pg 7-8)

Then one of the students with blue hair and a tongue

stud Says that America is for him a maximum-security prison

Whose walls are made of RadioShacks and Burger Kings,

and MTV episodes Where you can’t tell the show from the commercials,

And as I consider how to express how full of s*** I

think he is, He says that even when he’s driving to the mall in his

Isuzu

Trooper with a gang of his friends, letting rap music

pour over them Like a boiling Jacuzzi full of ballpeen hammers, even

then he feels

Buried alive, captured and suffocated in the folds Of the thick satin quilt of America

And I wonder if this is a legitimate category of pain, or whether he is just spin doctoring a better grade,

And then I remember that when I stabbed my father in

the dream last night, It was not blood but money That gushed out of him, bright green hundred-dollar

bills Spilling from his wounds, and—this is the weird part—, He gasped “Thank god—those Ben Franklins were Clogging up my heart—

And so I perish happily, Freed from that which kept me from my liberty”—

Which was when I knew it was a dream, since my dad Would never speak in rhymed couplets,

And I look at the student with his acne and cell phone

and phony ghetto clothes
And I think, “I am asleep in America too,
And I don’t know how to wake myself either,”
And I remember what Marx said near the end of his

life:

“I was listening to the cries of the past, When I should have been listening to the cries of the

future.”

But how could he have imagined 100 channels of 24-hour

cable Or what kind of nightmare it might be

When each day you watch rivers of bright merchandise

run past you And you are floating in your pleasure boat upon this

river Even while others are drowning underneath you And you see their faces twisting in the surface of the

waters

And yet it seems to be your own hand Which turns the volume higher?

Poems from What Narcissism Means to Me

TRANSITION

The final poem in this collection is Earthquake by Raul Herrera. In it he implores all individuals to use their voices to elicit change -- to speak out. The vibration of our collective voices will have as much power as the vibrations of an Earthquake by Raul Herrera

Earthquake by Raul Herrera (Pg 2-4) In 1906 an 8.2 sized earthquake ruptured the San

Andreas Fault, killing an estimated 3,000 people. If vibrations break boulders and devastate lives, Then our words can split open minds and alter the geo-

graphical shape of its content.
Because sound is vibration.
Our verbs are its earthquakes
And our hands are much like the Richter scale.
Charting the magnitude of our words.
So when you write,
Fight the urge to destroy your enemies.
Because and earthquake,
Named Gandhi
once told me,
Even revenge has aftershocks.
That even a whisper
Can cause a revolution.
In 2010 a 7.0-sizedearthquake takes the lives of 300,000

Haitians.
Do not underestimate
The Hercules behind your tongue.
Your voices are the reasons this planet’s axis is tilted.
But your silence is the reason this planet is dying.
So let’s cause a ruckus!
If Earthquakes can destroy lives,
Our voices can rebuild them.
In 2011 a 9.0-earthquake demolishes Fukushima, Japan.
“I have been to the mountaintop and I looked over and I’ve
seen the
Promised land.”
But the only thing in our way
Is a mute mountain.
So we
Crumble mountains.
We
Crack Rock
without needing a pipe.
Just give me a word.
One sentence can make the ground move like a Tsunami.
You can see their words cracking the concrete.
Cracking
Like the backs of the rebels from the past.
Cracking
Like the blast that killed 2Pac’s laugh.
Malcolm exited this world
believing that his earthquake would cause repercussions
“The future belongs to those who prepare for it today.”

So today I have a dream.
But my dream wasn’t heard
Today I have a dream
But my dream was deferred
Today I had a dream about a King but the king wasn’t
heard.
The legends are angry.
The world is violent
While we stay . . .

Why?
Newton’s 3rd law states,
“For every action there is an equal and opposite reaction.”
For example, if the action is
division
Then the opposite reaction would be
communication
Problems react to solutions.
Oppression reacts to revolution.
The death of Trayvon Martin reacts to Zimmerman’s

prosecution. Now this is law.

Voices react to vibrations,
Vibrations react to earthquakes.
So if sound is vibration
Our verbs are its earthquakes.
So let’s break the ground our fallen heroes are trapped

underneath.

Resurrect poets from graves.
REACT
Leaders from being slayed
REACT
Let’s speak with tremors trembling towers>
Talk like an earthquake.

Be like a rock, And watch this granite planet Shake
```

---

## IC-1542: Conversations about Home (at a deportation centre) and Rigged Game

- Title: Conversations about Home (at a deportation centre) and Rigged Game
- Author (byline): Warsan Shire and Dylan Garity
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1294
- Already set (do not supply): none

### Source block (context only)

```text
Author: Warsan Shire
Book: Teaching My Mother How to Give Birth
ISBN: 978-1905233298
Publisher: Flipped Eye Publishing Limited
Date (Month/Year): Dec 2011
Author: Dylan Garity
Book: Viral
ISBN: 978-0989641517
Publisher: Button Poetry
Date (Month/Year): Dec 2013
```

### Introduction (context only: never use it for content warnings)

```text
A new report from the Center for Immigration Studies has determined that as of October 2014, one out of every five U.S. residents doesn't speak English in their home. The new data shows that the number of people who speak a language other than English has reached an all-time high of 61.8 million with the largest increases from 2010 to 2013 being speakers of Spanish, Chinese, and Arabic.

Statistics are great, but the stories behind the statistics often get overlooked. Why are so many speakers of other languages coming to America? Perhaps we should take a moment to consider the homes from which they fled. Conversations about Home (at a deportation centre) by Warsan Shire.
```

### Performance text (classify this)

```text
Well, I think home spat me out, the blackouts and curfews like tongue against loose tooth. God, do you know how difficult it is, to talk about the day your own city dragged you by the hair, past the old prison, past the school gates, past the burning torsos erected on poles like flags? When I meet others like me I recognise the longing, the missing, the memory of ash on their faces. No one leaves home unless home is the mouth of a shark. I've been carrying the old anthem in my mouth for so long that there’s no space for another song, another tongue or another language. I know a shame that shrouds, totally engulfs. I tore up and ate my own passport in an airport hotel. I’m bloated with language I can't afford to forget.

*

They ask me how did you get here? Can’t you see it on my body? The Libyan desert red with immigrant bodies, the Gulf of Aden bloated, the city of Rome with no jacket. I hope the journey meant more than miles because all of my children are in the water. I thought the sea was safer than the land. I want to make love but my hair smells of war and running and running. I want to lay down, but these countries are like uncles who touch you when you're young and asleep. Look at all these borders, foaming at the mouth with bodies broken and desperate. I’m the colour of hot sun on my face, my mother’s remains were never buried. I spent days and nights in the stomach of the truck, I did not come out the same. Sometimes it feels like someone else is wearing my body.

*

I know a few things to be true. I do not know where I am going, where I have come from is disappearing, I am unwelcome and my beauty is not beauty here. My body is burning with the shame of not belonging, my body is longing. I am the sin of memory and the absence of memory. I watch the news and my mouth becomes a sink full of blood. The lines, the forms, the people at the desks, the calling cards, the immigration officer, the looks on the street, the cold settling deep into my bones, the English classes at night, the distance I am from home. But Alhamdulilah all of this is better than the scent of a woman completely on fire, or a truckload of men who look like my father, pulling out my teeth and nails, or fourteen men between my legs, or a gun, or a promise, or a lie, or his name, or his manhood in my mouth.

*

I hear them say, go home, I hear them say, f***** immigrants, f***** refugees. Are they really this arrogant? Do they not know that stability is like a lover with a sweet mouth upon your body one second and the next you are a tremor lying on the floor covered in rubble and old currency waiting for its return. All I can say is, I was once like you, the apathy, the pity, the ungrateful placement and now my home is the mouth of a shark, now my home is the barrel of a gun. I'll see you on the other side.

TRANSITION The lucky families who are not deported and are allowed to stay in America have the luxury of healthcare and education. Education . . . . but often only in English, not their native language. For example, In 2002, Massachusetts residents voted to replace transitional bilingual education with an English-only curriculum, which meant that English as a Second Language teachers are no longer allowed to help students with their native language in any way. Yet the students are still expected to perform at grade level by the end of the school year. Dylan Garity, whose sister is an ESL teacher concludes that "Even with the best resources available, it's impossible for these students to achieve those standards." – not only is it an affront to basic human rights . . . . It’s a Rigged Game by Dylan Garity

RIGGED GAME

Every day when I was five, my older sister would play teacher. Her students were me, my stuffed rabbit and an American girl doll, She’d line us up at the end of the bed and teach us whatever she’d learned in school that day.

Now, she teaches ESL at an elementary school in Boston and every week she tells me stories about her students. Ana does not know how to read in Spanish, much less English but she still wants to be a writer when she grows up. Juan chooses to stay inside and study at recess so that one day he’ll be able to teach his own brother.

These kids are good organs in a sick body.
In 2001, No Child Left Behind
gutted bilingual education.
Students who have been in the country for one year
are now expected to perform at grade level
on standardized English tests.
My sister is not allowed to instruct them in Spanish.
If the kids don’t jump high enough, the school loses
money
Improving a school by picking its pockets
is like tuning a guitar by ripping off the strings.

Learning to read in a new language before you can even read in your own is like learning to walk while a pit bull is chasing you. Like learning to sing with the conductor’s fist down your throat

This year, for my sister’s birthday,
I bought books for her students.
A poem on one page in Spanish, the next in English.
She is not allowed to help them read the first.
Their heritage is a banned book

Learning to read in a new language when you can’t even read in your own is like trying to heal a burn victim by drowning them. We are telling these children who have spent their whole lives in the deep end that they’ll learn how to swim if they just float out a little farther.

In the 1980s, American slaughterhouses
began building corrals in curves,
so no animals could see the blood at the end of the
track.
This is how we kept them moving forward.
In 2001, we began building the hallways of our schools in
curves.
This is how we keep them moving forward.

You never learn, you fail the test You never learn you fail the test You never learn, you drop out.

I know, I am lucky enough to be one of the winners of
this game
I was handed a head start
and a rulebook in my own tongue

but the winners of a rigged game should not get to write the rules.

On the television,
some senator preaches that throwing money
at an “urban school” is like feeding caviar to your dog.
They just won’t know how to appreciate it
After all, if these parents can’t take care
of their own children, why should we?

Well tell that to Ana
who has my sister translate newsletters aloud to her
father
because he, too, was never taught how to read

Tell that to Juan whose mother and baby sister are still in Guatemala whose father works three jobs

My sister tells me school is the most stable place in these kids’ lives. She has been a teacher since she was smaller than they are. but since when does being a teacher mean having to swear not to help?

Since when does being a teacher mean having your hands
tied
as the schoolhouse burns to the ground?
We are leading these children along a track built in
circles
as their lungs fill with smoke
telling them it is their fault
they can’t find a way out
```

---

## IC-1543: Crack Squirrels

- Title: Crack Squirrels
- Author (byline): Cristin O’Keefe Aptowicz
- Work: Everything is Everything
- Publisher: Write Bloody Publishing
- Publication date as stated: Jan 2010
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 564
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cristin O’Keefe Aptowicz
Book: Everything is Everything
ISBN: 978-0984251513
Publisher: Write Bloody Publishing
Date (Month/Year): Jan 2010
```

### Introduction (context only: never use it for content warnings)

```text
Crack Squirrels by Cristin O’Keefe Aptowicz appears in her 5th poetry collection entitled “Everything is Everything” and the title for her collection has a funny story to it that epitomizes the life philosophy of Ms Aptowicz. She was watching the first season of “Sesame Street” -- a much different show than the current incarnation (so much so that the DVD box carries a warning NOT to show it to young children), and she became fairly obsessed with its brazen weirdness.

One of the sketches is a Kermit the Frog “News Flash” where he is reporting on Jack Be Nimble’s attempt to jump over a candlestick. Well, in this version, Jack Be Nimble is this dazed hippie who doesn’t seem to understand the concept of “over.” He goes UNDER the candlestick. He goes AROUND the candlestick and all to the annoyance of Kermit the Frog.

The first time he makes the attempt, he yells a mantra of some sort to focus himself, “Everything is Everything!” and just starts running. Cristin adopted this manta and began intoning “Everything is Everything” whenever she attempted to do something new that she wasn’t sure she was going to do right. . . . From her book “Everything is Everything” I offer today, Crack Squirrels by Cristin O’Keefe Aptowic.z
```

### Performance text (classify this)

```text
In the mid-1980s, New York City had a serious problem and that problem was Crack Squirrels.

Crack Squirrels! the newspaper headlines read. Crack Squirrels! The local news anchors intoned. Crack Squirrels! Crack Squirrels!

In the mid-1980s, the Northern part of Central Park had become infested with Crack Squirrels. Wild-eyed, craven-mouthed, mad Crack Squirrels. Jonesing, addicted, twitching Crack Squirrels. Crack Squirrels who’d do anything for their next fix.

Crack Squirrels! How did this happen? The citizens of New York City asked after hearing of joggers being attacked, of bloody scratched up school children, shaky home video footage of the swarming Crack

Squirrels. Who got these squirrels so addicted to crack!?

In the mid-1980s, the crack epidemic hit New York City

hard. The newly minted-addicts took their rocks to Central Park to hit their high. When they were done, they left their

trash behind: crack vials, dosed aluminum foil, discarded pipes.

While scavenging for food, the jovial, fat and stupid

squirrels of Central Park – who had been, up to this point, straight-

edge vegans! – got curious and began sniffling the empty vials, licking the pipes and foil, and they liked it. They liked it a

lot. They liked it too much. They became Crack Squirrels.

Crack squirrels, the police officers said, are becoming a problem. The tourists don’t know any better. The

injuries are no joke. Squirrels can cause some serious damage,

especially Crack Squirrels.

We need to detox these squirrels! said the animal rights activists. We need to sedate squirrels and bring them to a crack-free environment!

No, what we need to do is kill these damn squirrels, said the republicans. The last things the taxpayers should be doing is paying for Crack Squirrels to go to rehab. What we need to do is poison them.

Poison them with what, crack? said the cynics.
Hey, what if a hawk ate a crack squirrel,
said the paranoid hippies. Would it become
a crack hawk? Because that would be a bad scene, man.

No, look, said the zoologists. Squirrels can’t survive on crack alone. These squirrels aren’t eating, they are barely drinking, they are spending their days attacking people for crack. These animals aren’t long for this world. What everyone should be focused on is how to get humans to stop taking crack, and once we’ve figured that out, the squirrel problem will take care of itself. Wait, wait, wait, what if a coyote eats a crack hawk, asked the stoner college kids, would it become a crack

coyote? Seriously, I’ve heard there are coyotes like in the ramble, and imagine if those coyotes become crack coyotes. I would carry like a whole bunch of crack on me at all

times, and if a crack coyote would come after me, I’d toss the

crack in one direction, and run in the others, and I’d be like, “Fooled your Crack Coyote!”And I’d be alive.

Nah man, said his stoner friend. I’d carry the carcass of a crack hawk with me everywhere, because I don’t think the crack coyote would even know what crack is, right? Think about it.

Yeah well, said the stoner college kid, Good luck trying to hunt and kill a crack hawk. Cause, if that’s your plan, man, if that’s your solution to this whole thing, That’s the dumbest plan I’ve ever heard. I’m serious. The dumbest.
```

---

## IC-1544: The Creation and Go Down Death (A Funeral Sermon)

- Title: The Creation and Go Down Death (A Funeral Sermon)
- Author (byline): James Weldon Johnson
- Work: God's Trombones
- Publisher: Penguin Books
- Publication date as stated: February 1990
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1068
- Already set (do not supply): none

### Source block (context only)

```text
BOTH POEMS ARE FROM
Author: James Weldon Johnson
Book: God's Trombones
ISBN: 978-0140184037
Publisher: Penguin Books
Date (Month/Year): February 1990
```

### Introduction (context only: never use it for content warnings)

```text
The poet and civil rights activist, James Weldon Johnson was influenced by his impressions of the rural South. His interest in the African-American folk tradition was ignited and resulted in a collection of “sermons” entitled God’s Trombones. It is said that Johnson considered the voice of the black preacher to be a musical instrument “not a piano . . . or trumpet but a trombone. From the printed page, peals the roar of the black preacher delivering a rousing sermon. The ability of Johnson to capture the sense of deliverance from the trials and tribulations of everyday life is indeed a talent. The Creation and Go Down Death (A Funeral Sermon) by James Weldon Johnson from the anthology God’s Trombones.
```

### Performance text (classify this)

```text
The Creation

And God stepped out on space, And he looked around and said: I'm lonely - I'll make me a world.

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

Go Down, Death (A Funeral Sermon)

Weep not, weep not,
She is not dead;
She's resting in the bosom of Jesus.
Heart-broken husband--weep no more;
Grief-stricken son--weep no more;
Left-lonesome daughter --weep no more;
She only just gone home.
Day before yesterday morning,
God was looking down from his great, high heaven,
Looking down on all his children,
And his eye fell of Sister Caroline,
Tossing on her bed of pain.
And God's big heart was touched with pity,
With the everlasting pity.

And God sat back on his throne,
And he commanded that tall, bright angel standing at his
right hand:
Call me Death!
And that tall, bright angel cried in a voice
That broke like a clap of thunder:
Call Death!--Call Death!
And the echo sounded down the streets of heaven
Till it reached away back to that shadowy place,
Where Death waits with his pale, white horses.
And Death heard the summons,
And he leaped on his fastest horse,
Pale as a sheet in the moonlight.
Up the golden street Death galloped,
And the hooves of his horses struck fire from the gold,
But they didn't make no sound.
Up Death rode to the Great White Throne,
And waited for God's command.
And God said: Go down, Death, go down,
Go down to Savannah, Georgia,
Down in Yamacraw,
And find Sister Caroline.
She's borne the burden and heat of the day,
She's labored long in my vineyard,
And she's tired--
She's weary--
Go down, Death, and bring her to me.
And Death didn't say a word,
But he loosed the reins on his pale, white horse,
And he clamped the spurs to his bloodless sides,
And out and down he rode,
Through heaven's pearly gates,
Past suns and moons and stars;
on Death rode,
Leaving the lightning's flash behind;
Straight down he came.
While we were watching round her bed,
She turned her eyes and looked away,
She saw what we couldn't see;
She saw Old Death. She saw Old Death
Coming like a falling star.
But Death didn't frighten Sister Caroline;
He looked to her like a welcome friend.
And she whispered to us: I'm going home,
And she smiled and closed her eyes.
And Death took her up like a baby,
And she lay in his icy arms,
But she didn't feel no chill.
And death began to ride again--
Up beyond the evening star,
Into the glittering light of glory,
On to the Great White Throne.
And there he laid Sister Caroline
On the loving breast of Jesus.
And Jesus took his own hand and wiped away her tears,
And he smoothed the furrows from her face,
And the angels sang a little song,
And Jesus rocked her in his arms,
And kept a-saying: Take your rest,
Take your rest.
Weep not--weep not,
She is not dead;
She's resting in the bosom of Jesus.
```

---

## IC-1545: The Crickets Have Arthritis

- Title: The Crickets Have Arthritis
- Author (byline): Shane Koyczan
- Work: Our Deathbeds Will Be Thirsty, Pgs 30-35
- Publisher: McKellar and Martin
- Publication date as stated: 2012
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1297
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shane Koyczan
Book: Our Deathbeds Will Be Thirsty, Pgs 30-35
ISBN: 978-0986576775
Publisher: McKellar and Martin
Date (Month/Year): 2012
```

### Introduction (context only: never use it for content warnings)

```text
* According to the American Childhood Cancer Organization, each year in the U.S. an estimated 15,800 children between the ages of birth and 19 years of age are diagnosed with cancer. Approximately one in 285 children will be diagnosed with cancer before their 20th birthday.

Unfortunately, for some children the battle with cancer doesn't end in the word "remission" or "cure," but in death. These brave little warriors have lost their battle with the cancer monster; and have traded their armor for angel wings.

The Crickets Have Arthritis by Shane Koyczan
```

### Performance text (classify this)

```text
(Pg 30-35) it doesn’t matter why I was there, where the air is sterile and the sheets sting. it doesn’t matter that I was hooked up to this thing that buzzed and beeped every time my heart leaped, like a man whose faith tells him: gods hands are big enough to catch an airplane

or a world,

doesn’t matter that I was curled up like a fist protesting death, or that every breath was either hard labor or hard time, or that I’m either always too hot or too cold it doesn’t matter because my hospital roommate wears star wars pajamas, and he’s nine years old His name is Louis and I don’t have to ask what he’s got, the bald head with the skin and bones frame speaks volumes. The Gameboy and feather pillow blooms like they’re trying to make him feel at home ‘cause he’s gonna be here a while

I manage a smile the first time I see him and it feels like the biggest lie I’ve ever told. so I hold my breath ‘cause I’m thinking any minute now he’s gonna call me on it I hold my breath ‘cause I’m scared of a fifty seven pound boy hooked to a machine, because he’s been watching me, and maybe I’ve got him pegged all wrong, like

maybe he’s bionic or something. so I look away.

like I just made eye contact with a gang member who’s got a rap sheet the length of a lecture on dumb mistakes politicians have made. I look away like he’s gonna give me my life back the minute I’ve got something to trade, I nearly pull out my pack and say

Cigarette?

but my fear subsides in the moment I realize Louis is all about show and tell. he’s got everything from a shot gun shell to a crow’s foot and he can put them all in context like: See, this is from a shooting range and see, this is from a weird girl I watch his hands curl around a cuff link and a tie tack and realize that every nick knack is a treasure and every treasure’s got a story and every time I think I can’t handle more he hits me with another story. says:

See, this is from my father. see, this is from my brother. see, this is from that weird girl. see this is from my mother. it took me two days to figure out that

that weird girl, is his sister.

took him about two hours today after she left for him to figure out he missed her.

they visit every day and stay well past visiting hours. because for them that term doesn’t apply. but when they do leave Louis and I are left alone and he says the worst part about being sick is you get all the free ice cream you ask for. and he says the worst part about that is realizing that there’s

nothing more they can do for you. he says:

Ice Cream can’t make everything ok.

and there’s no easy way of asking and I already know what he’s gonna say, but maybe he just needs to say it so I ask him any way. Are you scared? Louis doesn’t even lower his voice when he says

“Hell” yeah.

I listen to a nine year old boy say the word *Hell*, like he was a thirty year old man with a nose bleed being lowered into a shark tank, he’s got a right to it and if it takes this kid a curse word to help him get through it, I want to teach him to swear like the devil was sitting there taking notes with a pen and a pad but before I can forget that Louis is nine years old he says:

please don’t tell my dad.

he asks me if I believe in angels,

and before I realize I don’t have the heart to tell him, I tell him Not lately, and I just lay there waiting for him to hate me. but he doesn’t know how to, so he never does.

Louis loves like a man who lived in a time before God gave religion to men and left it to them to figure out what hate was.

He never greets me with silence. only smiles. and a patience I’ve never seen in someone who knows they’re dying. and I’m trying so hard not to remind him, I’ll be out of here in a couple of days, taking my life for granted. and he’ll still be planted in this bed like a flower that refuses to grow, I’ve been with him for five days and all I really know is Louis loves to pull feathers out of his pillow, and watch them float to the ground, almost as if he was the philosopher inside of the scientist ready to say that its gravity that’s been getting us down. but the truth is

there’s not enough miracles to go around kid,

and there’s too many people petitioning God for the winning lotto ticket. and for every answered prayer there’s a cricket with arthritis, and the only reason we can’t find answers is the search party didn’t invite us, and Louis right now the crickets have arthritis so there is no music. no symphony of nature swelling to crescendos, as if we bent halo’s into melodies that could keep rhythm with the way our hearts beat.

so we must meet silence with the same level of noise that the parents of dying nine year old boys make when they take liberties in talking with heaven. we must shout until we shatter in our own vibrations then let our lives

echo, and grow echo, and grow echo, and grow

Grow distant.

grow distant enough to know that as far as our efforts go we don’t always get a reply. but I swear to whatever God I can find in the time I have left I’m gonna remember you kid. gonna tell your story as often as every story you told me, and every time I tell it I’ll say see, there’s bravery in this world there’s 6.5 billion people curled up like fists protesting death, but every breath we take has to be given back, a nine year old boy taught me that.

so hold your breath. the same way you’d hold a pen when writing thank you letters on your skin to every tree that gave you that breath to hold.

then let it go. as if you understand something about getting old and having to give back

because what is your night worth without a story to tell, and why wield a word like worth if you’ve got nothing to sell. people drop pennies down a wishing well as if the cost of a desire is equal to that of a thought. but if you’ve got expectations expect others have bought your exact same dream for the price of the hard work, hang in, hold on mentality, like I accept any challenge so challenge me like

I’ve brought a knife to this gun fight, the other night I mugged a mountain so bring that . . . I’ve had practice.

Louis and I cracked this world wide open and found the prize inside because we never lied to ourselves, never told ourselves it would be easy or undemanding. so we sing in our own vibration and dare angels to eavesdrop and stop midflight to pluck feathers from their wings and write demands on God’s hands

I don’t often believe in angels, but on the day I left, Louis pulled a feather from his pillow and said this is for you,

I half expected him to say See, this is the first one I grew.
```

---

## IC-1546: The Crucifixion

- Title: The Crucifixion
- Author (byline): James Weldon Johnson
- Work: God’s Trombones
- Publisher: Rebound by Sagebrush
- Publication date as stated: Oct 1999
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 504
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Weldon Johnson
Book: God’s Trombones
ISBN: 978-0140184037
Publisher: Rebound by Sagebrush
Date(Month/Year): Oct 1999
```

### Introduction (context only: never use it for content warnings)

```text
According to the Gospels, Jesus had no particular quarrel with Rome and did not violate Roman law. And yet he was executed by a means exclusively reserved for those guilty of crimes against the empire. Crucifixion is a "cruel and unusual" punishment, calculated to derive the maximum amount of suffering. First a flogging and weakening by a loss of blood. Then outstretched arms fashioned by throngs or nails to a heavy wooden beam, which the victim carried across his neck and shoulders to the place of execution. The Crucifixion by James Weldon Johnson
```

### Performance text (classify this)

```text
Jesus, my gentle Jesus,
Walking in the dark of the Garden –
The Garden of Gethsemane,
Saying to the three disciples:
Sorrow is in my soul –
Even unto death;
Tarry ye here a little while,
And watch with me.

Jesus, my burdened Jesus,
Praying in the dark of the Garden –
The Garden of Gethsemane.
Saying: Father,
Oh, Father,
This bitter cup,
This bitter cup,
Let it pass from me.

Jesus, my sorrowing Jesus,
The sweat like drops of blood upon his brow,
Talking with his Father,
While the three disciples slept,
Saying: Father,
Oh, Father,
Not as I will,
Not as I will,
But let thy will be done.

Oh, look at black-hearted Judas –
Sneaking through the dark of the Garden –
Leading his crucifying mob.
Oh, God!
Strike him down!
Why don't you strike him down,
Before he plants his traitor's kiss
Upon my Jesus' cheek?

And they take my blameless Jesus,
And they drag him to the Governor,
To the mighty Roman Governor.
Great Pilate seated in his hall, –
Said: In this man I find no fault.
I find no fault in him.
And Pilate washed his hands.
But they cried out, saying:
Crucify him! –
Crucify him! –
Crucify him! –
His blood be on our heads.
And they beat my loving Jesus,
They spit on my precious Jesus;
They dressed him up in a purple robe,
They put a crown of thorns upon his head,
And they pressed it down –
Oh, they pressed it down –
And they mocked my sweet King Jesus.

Up Golgotha's rugged road
I see my Jesus go.
I see him sink beneath the load,
I see my drooping Jesus sink.
And then they laid hold on Simon,
Black Simon, yes, black Simon,
And Simon bore the cross.

On Calvary, on Calvary,
They crucified my Jesus.
They nailed him to the cruel tree,
And the hammer!
The hammer!
The hammer!

Rang through Jerusalem's streets.
The hammer!
The hammer!
The hammer!
Rang through Jerusalem's streets.

Jesus, my lamb-like Jesus,
Shivering as the nails go through his hands;
Jesus, my lamb-like Jesus,
Shivering as the nails go through his feet.
Jesus, my darling Jesus,
Groaning as the blood came spurting from his wound.
Oh, look how they done my Jesus.

Mary,
Weeping Mary,
Sees her poor little Jesus on the cross.
Mary,
Weeping Mary,
Sees her sweet, baby Jesus on the cruel cross,
Hanging between two thieves.

And Jesus, my lonesome Jesus,
Called out once more to his Father,
Saying:
My God,
My God,
Why hast thou forsaken me?
And he drooped his head and died.

And the veil of the temple was split in two, The midday sun refused to shine, The thunder rumbled and the lightning wrote And unknown language in the sky. What a day! Lord, what a day! When my blessed Jesus died.

Oh, I tremble, yes, I tremble,
It causes me to tremble, tremble,
When I think how Jesus died;
Died on the steeps of Calvary,
How Jesus died for sinners,
Sinners like you and me.
```

---

## IC-1547: A Day for Anne Frank

- Title: A Day for Anne Frank
- Author (byline): C.K. Williams
- Work: Collected Poems
- Publisher: Macmillan
- Publication date as stated: 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 728
- Already set (do not supply): none

### Source block (context only)

```text
Author: C.K. Williams
Book: Collected Poems
ISBN: 978-0374530990
Publisher: Macmillan
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
The number of children murdered during the Nazi genocide may never be known. Some estimates range as high as 1.5 million. Nazi persecution, arrests, and deportations were directed against all members of Jewish families without concern for age. Plucked from their homes and stripped of their childhoods, the children witnessed the murder of parents, siblings, and relatives. They faced starvation, illness and brutal labor, until they were consigned to the gas chambers. Anne Frank was a young girl who was caught up in the horror of the Holocaust and yet in her diary, she wrote the following words “"I simply can't build my hopes on a foundation of confusion, misery and death... I think... peace and tranquility will return again." The following poem by C.K. Williams imagines a scenario for the final days of the famous diarist whose life ended in at the concentration camp Bergen-Belsen. “A Day for Anne Frank” by C.K. Williams
```

### Performance text (classify this)

```text
God hates you!

-St. John Chrysostom
1.
I look onto an alley here
Where, though tough weed and flowers thrust up
through cracks and strain
Toward the dulled sunlight,
There is the usual filth spilling from cans,
The heavy soot shifting in the gutters
People come by mostly
to walk their dogs or to take the shortcut
between the roaring main streets,
Or just to walk
and stare up at the smoky windows,
But this morning when I looked out
Children were there running back and forth
Between the houses toward me.
They were playing with turtles --
Skimming them down the street
Like pennies or flat stones,
And bolting, shouting, after the broken corpses
One had a harmonica, and as he ran,
his cheeks bloating and collapsing like a heart,
I could hear its bleat, and then the girls’ screams
suspended behind them with their hair
And all of them: their hard, young breath,
their feet pounding wildly on the pavement to the
corner.

2.
I thought of you at that age,
Little Sister, I thought of you.
Thin as a door,
and of how your thighs would have swelled
and softened like cake,
Your breasts have bleached
and the new hair growing on you like song
would have stiffened and gone dark.
There was rain for a while, and then not.
Because no one came, I slept again,
and dreamed that you were here with me,
Snarled on me like wire,
Tangled so closely to me that we were vines
or underbrush together,
or hands clenched.

3.
They are cutting babies in half on bets.
The beautiful sergeant has enough money to drink
for a week.
The beautiful lieutenant can’t stop betting.
The little boy whimpers
he’ll be good.
The beautiful cook is gathering up meat
for the dogs.
The beautiful dogs
love it all.
Their flanks glisten.
They curl up in their warm kennels
and breathe.
They breathe.

4.
Little Sister,
you are a clot
in the snow,
blackened,
a chunk of phlegm
or puke
And there are men with faces
leaning over you with watercans

watering you!
in the snow, as though flowers would sprout
from your armpits
and genitals.

Little Sister, I am afraid of the flowers sprouting from you.

I am afraid of the silver petals
that crackle
of the stems darting
in the wind
of the roots.

5.
The twilight rots.
Over the greasy bridges and factories,
it dissolves
and the clouds swamp in its rose
to nothing.
I think sometimes the slag heaps by the river
should be bodies
and that the pods of moral terror
men make of their flesh should split
and foam their cold, sterile seeds into the tides
like snow
or ash.

6.
Stacks of hair were there
little mountains
the gestapo children must have played in
and made love in and loved
the way children love haystacks or mountains
Oh, God, the stink
of hair oil and dandruff

Their mothers must have thrown them into their tubs like puppies and sent them to bed

coming home so filthy stinking

of jew’s hair

of gold fillings, of eyelids.

7.
Under me on a roof
a sparrow little by little
is being blown away.
A cage of bone is left,
part of its wings,
a stain.

8. And in Germany the street car conductors go to work in their stiff hats, depositing workers and housewives where they belong, pulling the bell chains, moving drive levers forward or back. 9. I am saying goodbye to you before our death. Dear Father: I am saying goodbye to you before my death. We are so anxious to live, but all is lost -- we are not allowed! I am so afraid of this death, because little children are thrown into the graves alive. Goodbye forever.

I kiss you.

10.
Come with me, Anne,
Come,
It is awful not to be anywhere at all,
to have no one
like an old whore,
a general.

Come sit with me here, kiss me; my heart is too wounded with forgiveness.

There is an end now.
Stay.
Your foot hooked through mine
your hand against my hand
your hip touching me lightly.

it will end now it will not begin again.

Stay They will pass and not know us.

the cold brute earth is asleep.

there is no danger.

there is nothing,

Anne

there is nothing.
```

---

## IC-1548: Day Two

- Title: Day Two
- Author (byline): Kevin W. Burke
- Work: Wish You Were Here
- Publisher: Kevin W. Burke
- Publication date as stated: 2011
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 620
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kevin W. Burke
Book: Wish You Were Here
ISBN: N/A
Publisher: Kevin W. Burke
Date (Month/Year): 2011
NOTE: can be purchased on-line at
http://www.kevinwburkepoetry.com/store
NOTE: As of 1/26/2016 this book is out of stock on the
author's website and is unable to be located for purchase
at any other location. Use caution when performing in
tournaments where proof of publication (ie original
source) is required.
```

### Introduction (context only: never use it for content warnings)

```text
There is growing consensus among researchers and educators that the single most important factor in determining a student’s performance is the quality of his or her teacher. Yet, every school day, nearly a thousand teachers leave the field of teaching. One teacher voiced her reason for leaving after 16 years: “I can neither teach them properly nor fight for their education while trapped in silent submission.”

Submission to government imposed “teaching methods and evaluations” that have become more important than the people engaged in this most important endeavor - learning.

In Day Two by Kevin W. Burke, we hear the inner voice of a substitute teacher and what he or she WISHES to say to the students. But instead – where education is concerned - the “silent submission” epidemic continues and is actually passed along to the students themselves. Day Two by Kevin W. Burke
```

### Performance text (classify this)

```text
So, I come from a long line of
bartenders,
sweat-breakers,
broken backs from digging ditches,
and a few teachers.
Mom taught math,
Sis' teaches English,
and Dad
told us stories.

Now, all of this spins around in my mind and I see it spinning faster and faster in the reflection in the eyes of the student whose face is only inches from mine as he says, "What are you gonna do about it if I don't" all puffer fish, pointy chested as the rest of the high school class waits.

Waits
as I feel the ink
beneath my long sleeves,
buttons, and slacks
begin to burn.
Waits
as my first mosh-pit branded brain
begins to boil.
Waits as I keep back the gasoline bile
and get all choked up on
the hand-grenade pins and needles
that have been planted in my throat
and grown a drum set in my jawbone
I play
in time
with the swaying picket signs.

But today, today I muted it.

Honestly,
I'm proud of this kid.
I want to tell him this.
I want to tell him I'm glad.
that after thirteen years of learning,
the one thing he has not picked up on
is to blindly follow authority.

I want to tell him this.
I want to tell him I'm sorry.
I'm sorry you're stuck in a broken system
where men in designer suits
who have never seen a classroom
keep cutting art out of the heart of education
because you can't express yourself
properly or profitably enough
through a color by letters
number two pencil
piss poor pointillist painting
like A, B, C, or D all of the above
is being held above all else.
I wanna tell him all of this.
I wanna tell him I'm sorry,
but I say,

"Sit down.”

Sit down. Save your strength, kid.

Hold on to that crumpled paper, homemade bomb heart that keeps blasting shards of chicken scratch shrapnel through your blood stream. Hold on to this like sand bags for a real rainy day.

Trust me.
I know it hurts
It did and still does for me,
but there's a difference between
picking a fight and picking your fights.
Sit down.
This one's not worth it.
There are bigger fish to fry eyes with.
I'm temporary, kid..
I'm gone from your life
by the end of this period.
Then I'm off to who knows where
to substitute
all of their authority
and none of the mutual respect.

All of their authority
and none of the time.
All of their authority
and none of the real chances
to make you listen,
so listen now,
"Sit down."
A cop's not gonna be so polite, kid.
You'll get nothing less than a slap on the jaw
with a night stick.
"Sit down."
There's something to be said for political captives,
but there's not much valor in a detention slip.
"Sit down."
And stand up
for something worth it.
Stand up strong for something worth it.
But for now,
"Sit down."

I'm sorry.
I'm tired.
I spent all of yesterday
in a gang graffiti soaked, in-school suspension classroom
squared off with a seventh grade girl
with more balls than you’d know what to do with
and a blade in her backpack for the walk home.
"Sit down."
This tough guy act doesn’t scare me.
For Christsake you're wearing 3D glasses with the
lenses popped out.
How am I supposed to take you seriously right now?
But seriously,
you might not get it now
and you probably think
I'm just some power trippin’ jerk telling you what to do,
but really,
when I’m saying “"Sit down"
I'm praying you learn what it means to
stand up.
```

---

## IC-1549: Death of a Hired Man

- Title: Death of a Hired Man
- Author (byline): Robert Frost
- Work: Poems by Robert Frost
- Publisher: Signet Classics
- Publication date as stated: April 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1418
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Frost
Book: Poems by Robert Frost
ISBN: 978-0451527875
Publisher: Signet Classics
Date(Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
Consider the value and importance of human life. Does it matter if the person is old, or young? Does the manner in which they die alter the importance of their life? Unfortunately, if one is treated as essentially worthless for any length of time, one is likely to experience such feelings. People often descend on a spiral of 'Learned Helplessness', gradually becoming les and less able to approach the world or even themselves in a positive or even neutral manner. What, exactly, is the value of a life? You must answer that question for yourself, but first witness the turmoil surrounding the Death of a Hired Man by Robert Frost.
```

### Performance text (classify this)

```text
Mary sat musing on the lamp-flame at the table Waiting for Warren. When she heard his step, She ran on tip-toe down the darkened passage To meet him in the doorway with the news And put him on his guard. 'Silas is back.' She pushed him outward with her through the door And shut it after her. "Be kind," she said. She took the market things from Warren's arms And set them on the porch, then drew him down To sit beside her on the wooden steps.

'When was I ever anything but kind to him?
But I'll not have the fellow back,' he said.
'I told him so last haying, didn't I?
"If he left then," I said, "that ended it."
What good is he? Who else will harbor him
At his age for the little he can do?
What help he is there's no depending on.
Off he goes always when I need him most.
'He thinks he ought to earn a little pay,
Enough at least to buy tobacco with,
won't have to beg and be beholden."
"All right," I say "I can't afford to pay
Any fixed wages, though I wish I could."
"Someone else can."
"Then someone else will have to.
I shouldn't mind his bettering himself
If that was what it was. You can be certain,
When he begins like that, there's someone at him
Trying to coax him off with pocket-money, --
In haying time, when any help is scarce.
In winter he comes back to us. I'm done.'

'Shh I not so loud: he'll hear you,' Mary said.

'I want him to: he'll have to soon or late.'

'He's worn out. He's asleep beside the stove. When I came up from Rowe's I found him here, Huddled against the barn-door fast asleep, A miserable sight, and frightening, too- You needn't smile -- I didn't recognize him- I wasn't looking for him- and he's changed. Wait till you see.'

'Where did you say he'd been?

'He didn't say. I dragged him to the house, And gave him tea and tried to make him smoke. I tried to make him talk about his travels.

Nothing would do: he just kept nodding off.'

'What did he say? Did he say anything?'

'But little.'

'Anything? Mary, confess He said he'd come to ditch the meadow for me.'

'Warren!'

'But did he? I just want to know.'

'Of course he did. What would you have him say?
Surely you wouldn't grudge the poor old man
Some humble way to save his self-respect.
He added, if you really care to know,
He meant to dear the upper pasture, too.
That sounds like something you have heard before?
Warren, I wish you could have heard the way
He jumbled everything. I stopped to look
Two or three times -- he made me feel so queer--
To see if he was talking in his sleep.
He ran on Harold Wilson -- you remember -
The boy you had in haying four years since.
He's finished school, and teaching in his college.
Silas declares you'll have to get him back.
He says they two will make a team for work:
Between them they will lay this farm as smooth!
The way he mixed that in with other things.
He thinks young Wilson a likely lad, though daft
On education -- you know how they fought
All through July under the blazing sun,
Silas up on the cart to build the load,
Harold along beside to pitch it on.'

'Yes, I took care to keep well out of earshot.'

'Well, those days trouble Silas like a dream.
You wouldn't think they would. How some things linger!
Harold's young college boy's assurance piqued him.
After so many years he still keeps finding
Good arguments he sees he might have used.
I sympathize. I know just how it feels
To think of the right thing to say too late.
Harold's associated in his mind with Latin.
He asked me what I thought of Harold's saying
He studied Latin like the violin
Because he liked it -- that an argument!
He said he couldn't make the boy believe
He could find water with a hazel prong--
Which showed how much good school had ever done
him. He wanted to go over that. 'But most of all
He thinks if he could have another chance
To teach him how to build a load of hay --'

'I know, that's Silas' one accomplishment.
He bundles every forkful in its place,
And tags and numbers it for future reference,
So he can find and easily dislodge it
In the unloading. Silas does that well.
He takes it out in bunches like big birds' nests.
You never see him standing on the hay
He's trying to lift, straining to lift himself.'

'He thinks if he could teach him that, he'd be Some good perhaps to someone in the world. He hates to see a boy the fool of books. Poor Silas, so concerned for other folk, And nothing to look backward to with pride, And nothing to look forward to with hope, So now and never any different.'

Part of a moon was filling down the west,
Dragging the whole sky with it to the hills.
Its light poured softly in her lap. She saw
And spread her apron to it. She put out her hand
Among the harp-like morning-glory strings,
Taut with the dew from garden bed to eaves,
As if she played unheard the tenderness
That wrought on him beside her in the night.
'Warren,' she said, 'he has come home to die:
You needn't be afraid he'll leave you this time.'
'Home,' he mocked gently.
'Yes, what else but home?
It all depends on what you mean by home.
Of course he's nothing to us, any more
then was the hound that came a stranger to us
Out of the woods, worn out upon the trail.'

'Home is the place where, when you have to go there, They have to take you in.'

'I should have called it Something you somehow haven't to deserve.'

Warren leaned out and took a step or two,
Picked up a little stick, and brought it back
And broke it in his hand and tossed it by.
'Silas has better claim on' us, you think,
Than on his brother? Thirteen little miles
As the road winds would bring him to his door.
Silas has walked that far no doubt to-day.
Why didn't he go there? His brother's rich,
A somebody- director in the bank.'

'He never told us that.'

'We know it though.'

'I think his brother ought to help, of course. I'll see to that if there is need. He ought of right To take him in, and might be willing to-- He may be better than appearances. But have some pity on Silas. Do you think If he'd had any pride in claiming kin Or anything he looked for from his brother, He'd keep so still about him all this time?'

'I wonder what's between them.'

'I can tell you. Silas is what he is -- we wouldn't mind him-- But just the kind that kinsfolk can't abide. He never did a thing so very bad.

He don't know why he isn't quite as good As anyone. He won't be made ashamed To please his brother, worthless though he is.'

'I can't think Si ever hurt anyone.'

'No, but he hurt my heart the way he lay
And rolled his old head on that sharp-edged chair-back.
He wouldn't let me put him on the lounge.
You must go in and see what you can do.
I made the bed up for him there to-night.
You'll be surprised at him -- how much he's broken.
His working days are done; I'm sure of it.'

'I'd not be in a hurry to say that.'

'I haven't been. Go, look, see for yourself.
But, Warren, please remember how it is:
He' come to help you ditch the meadow.
He has a plan, You mustn't laugh at him.
He may not speak of it, and then he may.

I'll sit and see if that small sailing cloud Will hit or miss the moon.'

It hit the moon.

Then there were three there, making a dim row, The moon, the little silver cloud, and she. Warren returned-- too soon, it seemed to her, Slipped to her side, caught up her hand and waited.

'Warren?' she questioned.

'Dead,' was all he answered.
```

---

## IC-1550: A Definition and A Familiar Letter

- Title: A Definition and A Familiar Letter
- Author (byline): Peter Nicholson and Oliver Wendell Holmes
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1043
- Already set (do not supply): none

### Source block (context only)

```text
Author: Peter Nicholson
Book: A Dwelling Place
ISBN: 978-0908022120
Publisher: Wellington Lane Press
Date(Month/Year): 1997
Author: Oliver Wendell Holmes
Book: The Poetical Works of Oliver Wendell Holmes
ISBN: 978-1417919642
Publisher: Kessinger Publishing
Date(Month/Year): May 30, 2005
```

### Introduction (context only: never use it for content warnings)

```text
Art is meant to dig down into the soil and put forth the images through which people may see their own lives refracted, their own emotions portrayed, even ennobled and transformed. Poetry is art as reflected in “A Definition” by Peter Nicholson.
```

### Performance text (classify this)

```text
A Definition
It lives
When the gold myrtle-wreath
From an uncertain tomb
Is put on display under glass,
Is sex and death
In each of their various fashions,
Tastes of salt,
Smells of hot bitumen
Or a handful of crushed leaves.

It rids the boredom of known stuff
And gossip that doesn't amaze
In a shiver scalping our skin.
It can't be polite-
Mucus, scar tissue, fluids
Best not mentioned
Rush to its page
That we sometimes write,
Sometimes sleep with,
Sometimes kill with.
Our depression won't exhaust it.
Think of a cleaver stuck in your thigh,
Skin made mortal,
Or the crimp on the face
When we stand on the edge of large things-
A hard birth, the end of the affair,
That loved thing whose name makes us sweat.
It isn't money,
Though money might buy
Something of it
(Cézannes on the wall,
The rights to Fellini's next film).
It might come
Just as you've ironed the ninth shirt
And feel like throwing the kid
Who hasn't shut up for three hours
Out the window along with the bills
(But the child
Is made wholly of this thing-
It can shred as years intervene).
Then, for each expert
Who sets down its plan,
The real thing goes off at tangents.
It won't fit in troughs,
Glinting, flittering over books,
Breaking Olympic records.
Try to put a sack over it,
Hold it under water- just like Johnny,
It'll be back, grinning.
So, whatever you might think
About its demise, it will be around,
The warmth behind our monotony,
That passion in the slipstream,
For it lives and keeps on:
That's what poetry is.

TRANSITION More than a century and a half before Nicholson penned his Australian ode to poetry, another intellectual an ocean away in Britain set down his view of poetry in more light-hearted manner. A triple threat as doctor, speaker and author, Oliver Wendell Holmes was a leading citizen of 19th-century Boston whose command of the language has stood the test of time. A Familiar Letter by Oliver Wendell Holmes

A Familiar Letter

YES, write, if you want to, there's nothing like trying; Who knows what a treasure your casket may hold?

I'll show you that rhyming's as easy as lying, If you'll listen to me while the art I unfold.

Here's a book full of words; one can choose as he fancies, As a painter his tint, as a workman his tool; Just think! all the poems and plays and romances Were drawn out of this, like the fish from a pool!

You can wander at will through its syllabled mazes, And take all you want, not a copper they cost,-- What is there to hinder your picking out phrases For an epic as clever as "Paradise Lost"?

Don't mind if the index of sense is at zero, Use words that run smoothly, whatever they mean; Leander and Lilian and Lillibullero Are much the same thing in the rhyming machine.

There are words so delicious their sweetness will smother That boarding-school flavor of which we're afraid, There is "lush"is a good one, and "swirl" is another,-- Put both in one stanza, its fortune is made.

With musical murmurs and rhythmical closes
You can cheat us of smiles when you've nothing to tell
You hand us a nosegay of milliner's roses,
And we cry with delight, "Oh, how sweet they do smell!"

Perhaps you will answer all needful conditions
For winning the laurels to which you aspire,
By docking the tails of the two prepositions
I' the style o' the bards you so greatly admire.

As for subjects of verse, they are only too plenty
For ringing the changes on metrical chimes;
A maiden, a moonbeam, a lover of twenty
Have filled that great basket with bushels of rhymes.

Let me show you a picture--'t is far from irrelevant-- By a famous old hand in the arts of design; 'T is only a photographed sketch of an elephant,-- The name of the draughtsman was Rembrandt of Rhine.

How easy! no troublesome colors to lay on, It can't have fatigued him,-- no, not in the least,-- A dash here and there with a haphazard crayon, And there stands the wrinkled-skinned, baggy-limbed beast.

Just so with your verse,-- 't is as easy as sketching,-- You can reel off a song without knitting your brow, As lightly as Rembrandt a drawing or etching; It is nothing at all, if you only know how.

Well; imagine you've printed your volume of verses: Your forehead is wreathed with the garland of fame, Your poems the eloquent school-boy rehearses, Her album the school-girl presents for your name;

Each morning the post brings you autograph letters; You'll answer them promptly,-- an hour isn't much For the honor of sharing a page with your betters, With magistrates, members of Congress, and such.

Of course you're delighted to serve the committees That come with requests from the country all round, You would grace the occasion with poems and ditties When they've got a new schoolhouse, or poorhouse, or pound.

With a hymn for the saints and a song for the sinners, You go and are welcome wherever you please; You're a privileged guest at all manner of dinners, You've a seat on the platform among the grandees.

At length your mere presence becomes a sensation, Your cup of enjoyment is filled to its brim With the pleasure Horatian of digitmonstration, As the whisper runs round of "That's he!" or "That's him!"

But remember, O dealer in phrases sonorous,
So daintily chosen, so tunefully matched,
Though you soar with the wings of the cherubim o'er us,
The ovum was human from which you were hatched.

No will of your own with its puny compulsion
Can summon the spirit that quickens the lyre;
It comes, if at all, like the Sibyl's convulsion
And touches the brain with a finger of fire.

So perhaps, after all, it's as well to he quiet
If you've nothing you think is worth saying in prose,
As to furnish a meal of their cannibal diet
To the critics, by publishing, as you propose.

But it's all of no use, and I'm sorry I've written,-- I shall see your thin volume some day on my shelf; For the rhyming tarantula surely has bitten, And music must cure you, so pipe it yourself.
```

---

## IC-1551: Den of Lions (Stigmata)

- Title: Den of Lions (Stigmata)
- Author (byline): Terry Anderson
- Work: Not specified
- Publisher: Ballantine Books
- Publication date as stated: Jan 1995
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1049
- Already set (do not supply): none

### Source block (context only)

```text
Author: Terry Anderson
ISBN: 978-0345467928
Publisher: Ballantine Books
Date (Month/Year): Jan 1995
```

### Introduction (context only: never use it for content warnings)

```text
What is it like to exist for seven years in darkness and chains, not knowing from one day to the next how much longer you will be a prisoner? Or if you will be released from captivity the next day – or killed. Terry Anderson, chief Middle East correspondent for The Associate Press, was abducted in Beirut, Lebanon on March 16, 1985. Physically imprisoned, beaten, treated more as an object than as a human being, Anderson found out how the human spirit can reach beyond the bars of prison. These poems were written by Mr. Anderson during his captivity, set to memory and then recorded after his release in Den of Lions by Terry Anderson.
```

### Performance text (classify this)

```text
STIGMATA I

Seven years in chains
while love lies barren,
while children grow;
one lost, one not known,
and others left unseeded
now will never be.
Grim, terrible years
In subterranean cells,
a pawn of evil hypocrites;
passed from hand to hand
across the Muslim archipelago,
Taped and bagged like
some dead meat, despised,
inedible, but useful in trade.
Harsh and painful years
of darkness, damp and dirt,
humiliations heaped in myriads,
hatred and contempt received, returned.
Wasted, empty years? Not quite.
No years are empty in a life;
and wasted – that depends on
what is made of them, and after.

STIGMATA II

Pursuing idle pleasures,
abruptly snatched by wild
fantassins waving guns,
pushed and pulled down
from the sunny heights
into a darker world
where venomed voices
whisper menace and blows
erupt out of the night.
There’s no appeal;
the laws and judges
of this court are ruthless,
mercy’s alien and justice
twisted out of shape.
A man is just a thing
to be abused or not or
any whim or aim, or none.

STIGMATA III

Early endless weeks, chained, blindfolded. Each small movement brings a curse, a threat, a blow. Sometimes the vultures gather around to poke and prod with talon, stick, or gun, mutter maledictions and predict an early, painful end they don’t impress; no thief throws away his booty. More frightening are the vultures of the mind. Remorse, regret circle through the night alighting each in turn to tear a tasty morsel from the soul.

There’s much that vultures love -- noisome, rank, and nasty. Petty vices, packets full of lies, Soft overripe indulgences, and rankest, juiciest of all, Selfish pain inflicted on an open, trusting heart. The leavings of this carrion feast are meager, unimpressive: Some kindnesses, bits of charity, Aa few small acts of real love, and heaps of good intentions; all strung together by the only thing of value here -- a steel determination to survive.

STIGMATA IV

Prayers in the night hurled
fiercely at an absent God;
pleas, promises, bargains offered,
but no answers. Not until
each act in life’s examined
and acknowledged; remorse, regret
put in their proper places --
commendable but useless.
Then, after hours of cold
and bitter honesty, into
exhausted calm comes a presence,
softly, almost timorously,
of warmth and light and love.
It will not stay; recoils
from each new blast of anger;
flees absolutely from
hatred’s demon glare,
but leaves behind a longing,
comfort, and all anguish
smaller than before.
No flawed man, beset by passion
can hope to hold it long
Though some rare souls
bathe often in its glow.
For most, a light,
Infrequent touch, perhaps
just once a life,
must be enough.

STIGMATA VI

Isolation ends; other denizens
of this mad gulag bring relief
and aid in staving off
the savages without, within.
Self-flagellation can be purifying,
but carried on too long becomes
indulgence, a twisted kind of pride.
New minds bring fresh air;
new shoulders can be leaned on;
new regards provide a scale,
a balance that makes it easier
to maintain both faith and hope.
Personalities and politics
are different; five egos
in a room must clash and rub.
But differences are unimportant
next to shared laughter and shared pain.
Each takes from each;
each gives of what he has.

STIGMATA VI

Evil dealt with daily
becomes familiar, even ordinary.
At first just faceless and
malefic minions, guards
become distinct and separate.
Some are petty, mean, and vicious,
other ordinary, even sympathetic.
Communication can begin,
and some small understanding,
but soon runs into walls of
background, belief, and circumstance.
The logic is too different;
mental language untranslatable.
There’s no shared view of God or man.
Oppressor and oppressed,
Each sees the other
a victim bound and blind.

STIGMATA VII

A six-foot chain, a six-foot cell
allow t wo paces: step, step,
and turn; step, step, and turn.
When the body’s bound,
the mind leaps free to soar
and twist and turn back
on itself until its very freedom
becomes a kind of prison.
Each emotion’s felt in
fierce intensity, swelling,
fading only to return again
on a wild, unpiloted
roller coaster ride
that never ends, ignoring
pain, sickness, even death,
devouring all without a pause.
Time’s fragmented, each moment
endless, unconnected to
the swiftly passing years.

STIGMATA VIII

As in all prisons, information
is both punishment and weapon.
All news is censored; none allowed
at all for weeks, then glimpses
granted of family, friends’ concern.
Finally the game apparently
grows tiresome. Without a word,
a radio appears, magazines, even
television, and the world crashes in.
Not the one abandoned --
this is a frantic, changing place.
Wars, disasters, famines are
different, but the same.
What startles are the images
of empty-handed people defying tanks;
of nations by the score
reclaiming freedom; the abrupt
irrelevance of long-held enmities,
old alliances, and once-feared weapons;
of history resuming its
awkward, stumbling climb.

STIGMATA IX

Companions leave; new friends
arrive only to go home in turn,
Stirring hope, envy, and frustration.
Negotiations start, stumble,
stop, and start again
as each participant gropes a
and grasps for small advantages>
But slowly, it becomes apparent
that the roller coaster ride
has neared its end.
Soon it will be time to
leave this unamusemet park.
What of the man who will emerge,
pale, shocked by the images
cast from distorted mirrors?
Better, or worse?
Or like the world
that greets him,
unchanged in essence,
but shake into new relations
with himself, and others?

STIGMATA X

No man can ever start anew completely;
he's everything he's done
or said or failed to do.
Each bit is added on,
Altering the whole,
But covering, not replacing
what has gone before.
A piece of unfired clay,
he bears the marks
and scars of all his years.
Not just clay, though
sculptor, too;
he helps to mold himself:
Object, artist, audience.
Sometimes, though, larger hands --
destiny, fate, karma, God --
take firmly hold and,
wielding fierce events,
risk fracture to hack
and carve away some
awkward, ugly bits.
The final work cannot be seen
until it's fired, and all fires cold.

Paul knew: suffering and pain
are the truest ways,
the only ways for some of us,
to draw out that within
which answers to
the purpose of it all.
```

---

## IC-1552: The Digital Disconnect

- Title: The Digital Disconnect
- Author (byline): Marshall Davis Jones, Gary Turk, and Phil Kaye
- Work: Date & Time, Pg 13
- Publisher: Button Poetry
- Publication date as stated: Sept 2018
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 835
- Already set (do not supply): none

### Source block (context only)

```text
Poem: Touchscreen
Author: Marshall Davis Jones
ISBN: 978-1312089372
Publisher: Lulu.com
Date (Month/Year): April 2014
*****
Poem: Look Up
Author: Gary Turk
ISBN: On-Line Transcript of Spoken Word Short Film
Publisher: Mutimedia-English.com
Date (Month/Year): 2014
https://multimedia-english.com/videos/esl/look-up-gary-
turk-5492/
*****
Poem: Internet Speaks Back to the Author, 2018
Author: Phil Kaye
Book: Date & Time, Pg 13
ISBN: 978-1943735365
Publisher: Button Poetry
Date (Month/Year): Sept 2018
```

### Introduction (context only: never use it for content warnings)

```text
Today, we work remotely, attend school virtually, have our meals and groceries delivered with a click of an app button, and “Zoom” our family gatherings. Wow! January 1, 1983 was the official birthday of the internet and we have come SO far!

And yet, in the words of poet Tyler Knott Gregson: “Despite our hyper-connectedness, somewhere along the way we've lost our ability to speak with people, truly speak with them in person, with eyes finding eyes and ears ready to listen."

Today, mental health issues are on the rise; Tik Tok challenges can shut down entire school systems and an epidemic of loneliness is spreading across America. The time has come to question the negative impacts technology has had on our society.

This is the Digital Disconnect including Touchscreen by Marshall Davis Jones; Look Up by Gary Turk and The Internet Speaks back to the Author, 2018 by Phil Kaye
```

### Performance text (classify this)

```text
NOTE: Lines from poems are intertwined and designated by the following color-codes.

Touchscreen by Marshall Davis Jones

Look Up by Gary Turk

Internet Speaks back to the Author by Phil Kaye (Commercial voice) Introducing the new Apple iPerson complete with multi-touch and volume control Doesn't it feel good to touch?

My world has become so digital
I have forgotten what that feels like.
It used to be hard to connect when friends formed cliques,
Now it's even more difficult to connect
now that clicks form friends
But who am I to judge?

I have 422 friends, yet I am lonely.
I speak to all of them every day, yet none of them know
me.
The problem I have sits in the spaces between
Looking into their eyes, or at a name on a screen.

I face Facebook more than books face me I update my status - 420 spaces - to prove I’m still breathing.

Failure to do this daily
means my whole web wide world would forget that I exist.
But with 3,000 friends online,
and only five I can count in real life,
why wouldn't I spend more time in a world
where there are more people that 'like' me
Wouldn't you?

iPod iMac iPhone iChat I can do all of these things without making eye contact

I'm guilty of being part of this machine, This digital world, where we are heard but not seen. Where we type as we talk, and we read as we chat Where we spend hours together without making eye

contact

You would think these headphone jacks inject in the flesh the way we connect to disconnect

(Internet voice) tell me what you want
every door you enter
I will let you in
my friend Rihanna said that
you want to see her?
here she is
parts of herself
she never meant to show
but I got them for you

click - to proceed the checkout

All this technology we have, it's just an illusion Community, companionship, a sense of inclusion Yet when you step away from this device of delusion You awaken to see a world of confusion.

(Internet voice) is that too much?
are you upset with me?
here
a man belly flopping onto a lake
a goat climbing on people doing yoga
a baby crying hysterically & now laughing
a magician revealing his tricks

click - to x out where our hearts once were
We edit and exaggerate, crave adulation
We pretend not to notice the social isolation
We put our words into order and tint our lives a-glistening
We don't even know if anyone is listening

click - I've uploaded this hug I hope she gets it

(Internet voice) why are you sad?
here
the woman you kissed two nights ago
she was recently in Florida
it was colder than she expected
here, her mother
two Huskies
little brother’s graduation
view from the old apartment
best sushi she's ever had
her Bestie
it's okay
she shared it with me
so I could show you

click . . .

(Internet voice) a photo of your old best friend
who called you three days ago
don't call him now
let me show you him
you like it better that way
look how you two dressed up together

that Halloween
he doesn't want to do that anymore
except with me
I won't let him change I promise

click . . .

(Internet voice) don't leave you're safe here with me

click . . .

We're surrounded by children, who since they were born, Have watched us living like robots, who now think it's the

norm.
When I was a child, I'd never be home
Be out with my friends, on our bikes we'd roam
I'd wear holes on my trainers, and graze up my knees
We'd build our own clubhouse, high up in the trees

Now the park's so quiet, it gives me a chill See no children outside and the swings hanging still. There's no skipping, no hopscotch, no church and no

steeple We're a generation of idiots -- smart phones and dumb people.

(Internet voice) don't leave you're safe here with me

When my phone goes off, iTouch and iTouch and iTouch

Look up from your phone, shut down the display Take in your surroundings, make the most of today

When my phone goes off, iTouch and iTouch and iTouch

Look up from your phone, shut down those displays
We have a finite existence, a set number of days
Don't waste your life getting caught in the net,
When the end comes, nothing's worse than regret.

When my phone goes off, iTouch and iTouch and iTouch

Don't give into a life where you follow the hype
Give people your love, don't give them your 'like'
Disconnect from the need to be heard and defined
Go out into the world, leave distractions behind.

In a world where voices are only read
and laughter is never heard
I'm so desperate to feel . . . .
So when my phone goes off,
iTouch Look up from your phone and iTouch Shut down
that display and iTouch (Stop watching) because I hope the
screen can touch me back (Stop watching)
and maybe it will
When our technology is advanced enough . . .
to make us human again
```

---

## IC-1553: Dirty Dimes

- Title: Dirty Dimes
- Author (byline): Mike McGee
- Work: In Search of Midnight
- Publisher: Write Bloody Publishing
- Publication date as stated: June 2009
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 672
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mike McGee
Book: In Search of Midnight
ISBN: 978-0982148822
Publisher: Write Bloody Publishing
Date(Month/Year): June 2009
```

### Introduction (context only: never use it for content warnings)

```text
In an era when people routinely ask “What would Jesus do?” how many of us really practice what is preached? How many of us go the extra mile just because it's the right thing to do? If you really embrace the idea that we should treat others as we would like to be treated, test yourself the next time you're in the position to lend a hand. Will you be that person who is too busy, thinking the next person will take care of it? Let's take a minute to hold a mirror up to our behavior. The question is will you be happy with the reflection you see. It’s about our ability to connect with people we don’t know. To care about them and worry about them and imagine ourselves in their shoes. Dirty Dimes by Mike McGee
```

### Performance text (classify this)

```text
I’m wide awake as I stock the candy aisle in this late-
night drugstore
My bell rings and I head toward my cash register
Two women
Barely thirty
Looking for a cashier
Make eye contact with me and wait for my slow legs to
reach them
My eyes are drawn to their items
and then to the skin of the woman closest to me
She’s wearing a man’s dress shirt completely unbuttoned
And no bra
The skin I see is her stomach and her chest
I can see her entire right breast
So I look away
Somewhat ashamed
I am forced to look at her face
It is far too thin to be healthy
A bandanna squeezes her bald head tightly
She is pale and weak from chemical or disease
Her eyes bulge like those of surprise
Her sunken face looks like that of a former beauty
queen
She stares at the products as I ring them up
And I try not to stare at her small breasts every time
her shirt swings open
Her friend stands behind her
Clean and strong
Maybe she’s her lover
Maybe they’re related
None of the items I ring up will tell me who the friend is
They only say that the exposed woman is very ill
And bleeds from sores; wounds
She is afflicted with something
And none of these products have brand names
So she is poor
They are poor together
And about to give me their money
This woman must have cancer
I want to strike up a conversation
Something to get my mind away from this apparent
mortality
Maybe she has AIDS
Maybe she shared the wrong needle with the wrong
person
But every dying human looks like a junkie at some point
Her friend looks at her with worry
Cementing all my assumptions
She is her guardian
The one who will and is watching her die
The one who will pick out her cheap coffin
The only one willing to bury her
And there is so much love between these two
I can’t look at her breasts anymore
Because they’ll be underground next Christmas
And that makes me shiver like it was a new thing
I am taking up way too much of their precious time
So I speed up the process and bag their stuff as quickly
as possible
And I hit the total button:
Three dollars-and-sixty-seven cents in low grade medical
supplies
Maybe these items will help her live another day
I should just give them to her
But that would draw attention
And I would be another person
In their lives
Reminding a living person that they are dying
and that would not be fair
So the friend pulls out some money
The dead woman beats her to the counter
With a handful of dirty dimes
The kind collected in a cup on a street corner
Downtown dimes discarded by uptown business men
And women who aren’t dying this very minute
My pity turns to anger as she picks lint out of the
change on the counter
I am upset that this nice woman is so ill
but she’s cracking smiles at me
with big teeth through thin lips
She knows I know
Maybe she’s content
Why can’t I just let her be a stranger
I watch her count the dirty dimes off the counter
But I don’t count along with her
Because I want her to come up short
I take 36 dimes and try to assume some sort of apathy
But it never works
And they leave with smiles on their faces
That I couldn’t have possibly given them
and for the rest of the night I can’t focus on shit
I make sure every customer after them gets a dirty
dime in their change
And I try not cry for some reason
I just don’t get paid enough for that sort of thing
It is 3 AM
and I am tired of trying not to care about people who
don’t know me
```

---

## IC-1554: Diving into the Wreck

- Title: Diving into the Wreck
- Author (byline): Adrienne Rich
- Work: The Fact of a Doorframe, Pgs 101-103
- Publisher: W.W Norton and Company
- Publication date as stated: December 2002
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 461
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adrianne Rich
Book: The Fact of a Doorframe, Pgs 101-103
ISBN: 978-0393323955
Publisher: W.W Norton and Company
Date (Month/Year): December 2002
```

### Introduction (context only: never use it for content warnings)

```text
The word wreck is used to describe the tangible and intangible. While a boat can become “shipwrecked” a girl may also call herself an “emotional wreck.” This word can mean a mess or disaster: an unknown or ambiguity. A wreck, though never pleasant, changes those that experience it. One poetess dives into both the literal and the metaphorical wrecks of history and mythology in

“Diving into the Wreck” by Adrienne Rich
```

### Performance text (classify this)

```text
(Pgs 101-103) First having read the book of myths,
and loaded the camera,
and checked the edge of the knife-blade, I put on
the body-armor of black rubber
the absurd flippers
the grave and awkward mask.
I am having to do this
not like Cousteau with his
assiduous team
aboard the sun-flooded schooner
but here alone.

There is a ladder.
The ladder is always there
hanging innocently
close to the side of the schooner.
We know what it is for,
we who have used it.
Otherwise
it's a piece of maritime floss
some sundry equipment.
I go down.
Rung after rung and still
the oxygen immerses me
the blue light
the clear atoms
of our human air.
I go down.
My flippers cripple me,
I crawl like an insect down the ladder
and there is no one
to tell me when the ocean
will begin.

First the air is blue and then
it is bluer and then green and then
black I am blacking out and yet
my mask is powerful
it pumps my blood with power
the sea is another story
the sea is not a question of power
I have to learn alone
to turn my body without force
in the deep element.
And now: it is easy to forget
what I came for
among so many who have always
lived here
swaying their crenellated fans
between the reefs
and besides
you breathe differently down here.
I came to explore the wreck.
The words are purposes.
The words are maps.
I came to see the damage that was done
and the treasures that prevail.
I stroke the beam of my lamp
slowly along the flank
of something more permanent
than fish or weed
the thing I came for:
the wreck and not the story of the wreck
the thing itself and not the myth
the drowned face always staring
toward the sun
the evidence of damage
worn by salt and sway into this threadbare beauty
the ribs of the disaster curving their assertion
among the tentative haunters.

This is the place.

And I am here, the mermaid
whose dark hair streams black,
the merman in his armored body.
We circle silently
about the wreck
we dive into the hold.
I am she: I am he
whose drowned face sleeps with open eyes
whose breasts still bear the stress
whose silver, copper, vermeil cargo lies obscurely inside barrels
half-wedged and left to rot
we are the half-destroyed instruments
that once held to a course
the water-eaten log
the fouled compass.

We are, I am, you are
by cowardice or courage
the one who find our way
back to this scene
carrying a knife, a camera
a book of myths
in which
our names do not appear.
```

---

## IC-1555: The Echoes of Teachers

- Title: The Echoes of Teachers
- Author (byline): Kevin M Derrig and Taylor Mali
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 959
- Already set (do not supply): none

### Source block (context only)

```text
Author: Taylor Mali
Book: What Learning Leaves, 2nd Edition
ISBN: 978-1887012171
Publisher: Write Bloody Publishing
Date (Month/Year): March 2013
Author: Kevin M. Derrig
Book: The Spoken Word Revolution: Slam, Hip Hop &
the Poetry of a New Generation; Pgs 220-221
ISBN: 978-1402202469
Publisher: Sourcebooks, Incorporated
Date (Month/Year): March 2005
```

### Introduction (context only: never use it for content warnings)

```text
In Taylor Mali’s unapologetic declaration, “What Teachers Make,” teaching is not a fallback plan but a force -- measured not in salary, but in courage, curiosity, and lives changed.

However, Kevin M. Derrig’s “First Period” shifts the lens, exposing what happens when teachers forget their responsibility. When red ink wounds deeper than it corrects, and a raised hand becomes a breaking point.

Teachers hold the power to build or to bruise, to ignite possibility or silence it. What happens in the classroom can echo for a lifetime.

The Echoes of Teachers with poems by Kevin M Derrig and Taylor Mali
```

### Performance text (classify this)

```text
What Teachers Make, or, Objection overruled, or
If things don’t work out, you can always go to law school
by Taylor Mali
(Pgs 35-37) He says the problem with teachers is
What’s a kid going to learn
from someone who decided his best option in life
was to become a teacher?
He reminds the other dinner guests that it’s true
what they say about teachers:
Those who can, do; those who can’t, teach.

I decide to bite my tongue instead of his and resist the temptation to remind the dinner guests that it’s also true what they say about lawyers.

Because we’re eating, after all, and this is polite

conversation.

I mean, you’re a teacher, Taylor. Be honest. What do you make?

And I wish he hadn’t done that
(asked me to be honest)
because, you see, I have a policy
about honesty and a**‐kicking:
if you ask for it, then I have to let you have it.

You want to know what I make?

I make kids work harder than they ever thought they

could. I can make a C+ feel like a Congressional Medal of Honor and an A- feel like a slap in the face.

How dare you waste my time with anything less than your very best.

I make kids sit through 40 minutes of study hall
in absolute silence. No, you may not work in groups.
No, you may not ask a question.
Why won’t I let you go to the bathroom?
Because you’re bored, and you don’t really have to go to

the bathroom, do you?

I make parents tremble in fear when I call home: Hello, this is Mr. Mali. I hope I haven’t called at a bad

time, I just wanted to talk to you about something your son said

today.
To the biggest bully in the grade, he said,
“Leave the kid alone. I still cry sometimes, don’t you?
It’s no big deal.”
And that was noblest act of courage I have ever seen.

I make parents see their children for who they are and what they can be.

You want to know what I make?

I make kids wonder,
I make them question.
I make them criticize.
I make them apologize and mean it.
I make them write, write, write
and then I make them read.

I make them spell
definitely beautiful, definitely beautiful, definitely beautiful
over and over and over again until they will never misspell
either one of those words again.
I make them show all their work in math
and hide it on their final drafts in English.
I make them understand that if you’ve got this,
then you follow this,
and if someone ever tries to judge you
by what you make, you give them this!

Here, let me break it down for you, so you know what I

say is true: I make a god*** difference! What about you?

NOTE: Author grants use of his poetry for forensics competitions: “If you are looking for permission to perform one of my poems in forensic competition, consider it granted.” https://taylormali.com/contact/seeking-permission/

First Period by Kevin M Derrig

(Pg 220-221) half way through first period dust accumulated on the sweaty palm of my

raised hand must be a centimeter thick by now as the chicken-legged teacher goes around the

room
defacing students’ homework from last night
with red pen graffiti
that focuses more on missed commas than the

content of the sentences

he finally decides to acknowledge me “Mr. Derrig, why do I have a feeling that this is

another one of your dumb comments. You constantly waste my time. Why

don’t you just drop out or something?”

why don’t I just drop out why don’t I just drop out!

and it was at that moment that all statistics

began to make sense to me statistics of children whose mouths water more

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

just a little more help than others

I wanted to turn my shot-down hand into a fist I wanted to hit him ‘til he was incapable of

speaking anymore but I didn’t want to become another number in

overflowing manila folders of children arrested in school

and we wonder why a gun seems to fit perfectly

in the hands of this generation’s adolescents

ladies and gentlemen I’m writing this poem to highlight that which has

been stuck like gum
underneath wobbly desks
free from parental eyes
only to mess the hand of those who have to sit
there
I’m writing this poem to speak for all the rows of

children before me who remained voiceless in the cracks of school

and its sound proof textbooks I’m writing this poem for all the children who

have not yet been named the ones that will one day have to fill these rows

I’ve been struggling in only to enter classrooms where they’ll be shot

down for what they feel

ladies and gentlemen the future of America is being crushed between

the molars of power-hungry tyrants who think class rooms

are boot camps

and if we have any teachers in the audience I urge you to understand that the hand you grab

the chalk with
the hand you grab those red pens with
the voices you speak with
are oversized chisels
and you must proceed to teach with caution
for what you say and what you do is written in

stone and if you chisel too hard these minds can crack

“So what don’t you understand now, Mr. Derrig?”

I just wanted to know if I could go to the bathroom

(“First Period” as part of another collection) IL State Qualifier

(“First Period” as part of another collection) KS State Qualifier – (This collection)
```

---

## IC-1556: El Mozote

- Title: El Mozote
- Author (byline): Andrea Gibson
- Work: Pole Dancing to Gospel Hymns
- Publisher: Write Bloody Publishing
- Publication date as stated: June 2008
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 682
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andrea Gibson
Book: Pole Dancing to Gospel Hymns
ISBN: 978-0981521305
Publisher: Write Bloody Publishing
Date (Month/Year): June 2008
```

### Introduction (context only: never use it for content warnings)

```text
In December 1981 soldiers of the Salvadoran Army's select, American-trained Atlacatl Battalion entered the village of El Mozote, where they murdered hundreds of men, women, and children, often by decapitation. Although reports of the massacre -- and photographs of its victims -- appeared in the United States, the Reagan administration quickly dismissed them as propaganda. In the end, El Mozote was forgotten. The war in El Salvador continued, with American funding. This poem serves as a testament to the forgotten victims of a neglected theater of the cold war. El Mozote by Andrea Gibson.
```

### Performance text (classify this)

```text
El Salvador, 1981.
In the village of El Mozote
the twilight sun was falling slow
behind the mountain’s red earth.
December soil giving birth
to the stretching necks of noble pines, rising
falling shedding humble shadows upon the golden corn
fields below

but the day’s tender glow told nothing
of the dark fear of the people
hiding horrified in their homes.
And then the soldiers came.

The soldiers came in the name of cleansing,
cleansing their country free
of potential communist rebels.
Plan was, if they couldn’t catch the fish
then they were gonna drain the sea.
So they pounded on the village doors
with the butts of their M16s,
“Get out here now!”
‘til every person in the village was mouth-down in the
dirt.

And the soldiers shouted questions
while mothers trembled and the children cried
and the fathers begged for their lives,
begged for their families to live, “We are an innocent
people,
we have not taken sides, we have no answers to give.”

And they had no answers to give.
So when night dropped its ebony skirt
the people of El Mozote were still
mouth-down in the dirt.
And there had never been a night so long,
sleepess with terror, the darkness drew on and on
so when dawn finally sprinkled her first shards of light
the people of the village
having lived through the night
dared, for a moment, hope.
But no.
The slaughter began with the men.
Fathers, brothers, grandfathers, sons,
not one was left alive.
Beheaded with machetes, their crimson corpses
were stacked and stacked and stacked in piles,
while each mother clutched her child to her chest
praying, “Jesus save us, Jesus save us.”
They couldn’t imagine the terror coming next.

The children were hung from trees,
tossed in the air and caught
on the bloodied blades of bayonets.
The women were slaughtered with M16s,
as there ten-year-old daughters
writhed in heaving pain beneath the soldiers’ brutal sex,
Their screams futile as the soft seams of their flesh
tore and ripped to fit the gang-raping warheads
of a sin no god would ever forgive.

And there has never been a sound more terrible,
more impossibly unbearable
than the desperate shrill of the death
piercing hour after hour the miles of El Salvador’s hillls,
and still, beneath it all,
like breath rises from shattered chests
and wings rise from burning nests
beneath it all
one little girl sang.

Cristo me ama, bien lo se

(Jesus loves me, this I know)

Through the slaughter of their father
and the slaughter of her mother,
a day howling a horror like no other
she sang.

Su palabra me hace ver

(For the Bible tells me so) As soldier after soldier drilled her body with his phallic hate, she sang through rape after rape after brutal rape, as everything around her bled desperate with cries the little girl sang hymns to the sky.

Que los ninos son de aquel

(Little ones to Him belong) She sang ‘til they shot her in the chest, and still she sang like the blessed of the blessed.

She sang ‘til they shot her again and even then as she choked on her blood she sang.

Quien es nuestro amigo fiel

(They are weak but He is strong) She sang ‘til they slit her throat.

Yes, Jesus loves me

Yes, Jesus loves me

Yes, Jesus loves me

The Bible tells me so
And she was only one of over 900 innocent people
tortured and killed that day at the massacre at El
Mozote,
funded by the USA.
A crime covered up and denied by our government for
years
because killers were trained
in the School of the Americas, Ft. Benning, Georgia.

And now as the militia of the red, white, and blue treads the guilty waters of another bloody slaughter our nation’s government is still hiding still denying its people honest information. But we who walk among the land of the relatively free have an obligation to hunt down the truth, have an obligation to lift our voices against any more pain inflicted on anyone in our names.

Our resistance is the key. The caged bird sings. The caged bird would rather be free.
```

---

## IC-1557: Erika: Poems of the Holocaust

- Title: Erika: Poems of the Holocaust
- Author (byline): William Heyen
- Work: Not specified
- Publisher: Time Being Books
- Publication date as stated: June 1991
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1469
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Heyen
ISBN: 978-1877770210
Publisher: Time Being Books
Date (Month/Year): June 1991
```

### Introduction (context only: never use it for content warnings)

```text
It is the stories that bring history to life. The more we liste, the more understand. When we are able to personalize random facts and statistics, history becomes human, becomes real.

Martin Niemöller was a prominent Protestant pastor who emerged as an outspoken public foe of Adolf Hitler. He spent the last seven years of Nazi rule in concentration camps. He penned the following lines just after the Holocaust, and argued against apathy—and for the moral connectedness of all people.

“First they came for the Socialists, and I did not speak out— Because I was not a Socialist. Then they came for the Trade Unionists, and I did not speak out— Because I was not a Trade Unionist. Then they came for the Jews, and I did not speak out— Because I was not a Jew. Then they came for me—and there was no one left to speak for me.”
```

### Performance text (classify this)

```text
Stories (pg 5)

What if the world is filled with stories? --
we hear only a few, live fewer,
and most that we live or hear
solve nothing, lead nowhere . . . .

Riddle (pg 36-37)

From Belsen a crate of gold teeth,
from Dachau a mountain of shoes,
from Auschwitz a skin lampshade
Who killed the Jews?

Not I, cries the typist,
not I, cries the engineer,
not I, cries Adolf Eichmann,
Not I, cries Albert Speer.

David Nova swallowed gas,
Hyman Abrahms was beaten and starved.
Some men signed their papers,
and some stood guard,

and some herded them in,
And some dropped the pellets,
and some spread the ashes,
and some hosed the walls,
Some smelled the smoke,
some just heard the news.
Were they Germans? Were they Nazis?
Were they human? Who killed the Jews?

The stars will remember the gold,
the sun will remember the shoes,
the moon will remember the skin.
But who killed the Jews?

Three Relations (Sachsenhausen, 1944) (pg 22-23)

The small stone house stands by itself, thirty meters long, thirty meters wide, five meters high. Two small windows with heavy bars. A lawn in front, And a wooden shack, where people undress, to shower, they think. They walk into the stone house.

Concrete floor and no furniture.
Maybe two hundred nozzles stick out.
The two windows and door lined with rubber.
It’s a shower, all right, but gas comes out
and twists their bodies into awful shapes
Gas does not put them quietly to sleep.
Their flesh is torn with their own or others’ teeth.

Their bodies were bluish red.
We dragged them out of the gas house
by hair and ears and feet
and threw them on a flat wagon
Each wagon had room for seventy bodies.
We drove the load to the crematorium.
We stacked them at the entrance

Flesh does not burn like wood -- it takes a long time to burn humans.

Simple Truths (pg 107-110)

When a man has grown a body,
a body to carry with him
through nature for as long as he can,
when this body is taken from him
by other men and women who happen to be,
this time, in uniform,
Then it is clear he has experienced
an act of barbarism,

And when a man has a wife,
a wife to love for as long as he lives,
When this wife if marked with a yellow star
and driven into a chamber she will never leave alive,
then this is murder,
so much is clear.
and when a woman has hair,
when her hair is shorn and her scalp bleeds,
when a woman has children,
Children to love for as long as she lives,
when the children are taken from her,
When a man and his wife and their children
Are put to death in a chamber of gas,
or with pistols at close range, or are starved,
or beaten, or injected by the thousands,
Or ripped apart, by the thousands, by the millions,

it is clear that where we are
is Europe, in our century, during the years
from nineteen-hundred and thirty-five
to nineteen-hundred and forty-five
after the death of Jesus, who spoke of a different
order,
but whose father, who is our father,
If he is our father,
If we must speak of him as father,
Watched, and witnessed, and knew,

And when we remember,
When we touch the skin of our own bodies,
When we open our eyes into dream
or within the morning shine of sunlight
and remember what was taken
from these men, from these women,
from these children gassed and starved
and beaten and thrown against walls
and made to walk the valley
of knives and icepicks and otherwise
exterminated in ways appearing to us almost
beyond even the maniacal human imagination,
Then it is clear that this is the German Reich<
During approximately ten tears of our lord’s time,

and when we read a book of these things,
when we hear the names of the camps,
when we see the films of the bulldozed dead
or the film of one boy struck on the head
with a club in the hands
of a German doctor who will wait
some days for the boy’s skull to knit, and will enter
the time in his ledger, and then
take up the club to strike the boy again,
and wait some weeks for the boy’s skull to knit,
and enter the time in his ledger again<
and strike the boy again,
and so on, until the boy, who,
at the end of the film of his life
can hardly stagger forward toward the doctor,
does die, and the doctor
enters exactly the time of the boy’s death in his
ledger,

when we read these things or see them,
then it is clear to us that this
happened, and within the lord’s allowance, this
work of his minions, his poor
vicious dumb German victims twisted
into the swastika shapes of trees struck by lightning
on this his earth, if he is our father,
if we must speak of him in this way,
this presence above us, within us, this
mover, this first cause, this spirit, this
curse, this bloodstream and brain-current, this
unfathomable oceanic ignorance of ourselves, this is
automatic electric Aryan swerve, this

fortune that you and I were not the victims this luck that you and I were not the murderers, this sense that you and I are clean and understand, this stupidity that gives him breath, gives him life as we kill them all, as we killed them all.

TRANSITION

Although the Holocaust occurred more than 50 years ago, once again history seems to be repeating itself. The Syrian crisis finds millions of Syrian mothers and children attempting to flee their country due to violent civil war. Those who are not fortunate enough to get out of the country face air raids, bombings, constant terrorist attacks and are even at risk of losing their lives. The Jewish children of the Holocaust and the Syrian children of today face a world with too much apathy. First they came for the Muslims . . . . and I did not speak out . . . in fact I closed my door . . . because I was not a Muslim . . . After the Holocaust, the world said “Never Again” – Well, never is here and it’s happening again in Syria. Are you willing to be held accountable for our silence and inaction during the worst humanitarian crisis of our time?

The Children (pg 116 – 118)

I do not think we can save them.
I remember, within my dream, repeating
I do not think we can save them.
but our cars follow one another
over cobblestones. Our dim
Headlamps, yellow in fog, brush past,
at the center of a market square,
its cathedral’s great arched doors.
I know, now, this is a city
in Germany, two years
after the Crystal Night. I think ahead
to the hospital, the children.
I do not think we can save them.
Inside this dream,
in a crystal dashboard vase,
one long-stemmed rose unfolds
strata of soft red light.
Its petals fall, tears, small
flames. I cup my palm to hold them,
and my palm fills to its brim,
will overflow.
Is this the secret, then? . . .
Now I must spill the petal light, and drive.

We are here, in front of the hospital,
our engines murmuring. Inside,
I carry a child under each arm,
Down stairs, out to my car.
One’s right eyeball hangs on its cheek
on threads of nerve and tendon
but h e s till smiles, and I love him.
The other has lost her chin --
I can see straight down her throat
to where her heart beats
black-red, black-red.
I do not think we can save them.

I am the last driver in this procession.
Many children huddle in my car.
We have left the city. Our lights
tunnel the fog beneath arches of linden,
toward Bremerhaven, toward
the western shore..
I do not think we can save them.
This time, at the thoughts, lights
whirl in my mirror, intense
fear, and the screams of sirens.
I begin to cry, for myself, for the children.
A voice in my dream says
this was the midnight you were born. . .

Later, something brutal happened, of course, but as to this life I had to, I woke, and cannot, or will not, remember. But the children, of course, were murdered, their graves lost, their names lost, Even those two faces lost to me. Still, this morning, inside the engine of my body, for once, as I wept and breathed deep, relief, waves of relief, as though the dreamed rose would spill its petals forever.

I prayed thanks. For one night, at least,
I tried to save the children
to keep them safe in my own body,
and knew I would again. Amen.
```

---

## IC-1558: Establishing Perpetual Care at the Locust Grove Baptist Cemetery

- Title: Establishing Perpetual Care at the Locust Grove Baptist Cemetery
- Author (byline): Linda Hasselstrom
- Work: Land Circle
- Publisher: Fulcrum Publishing
- Publication date as stated: Nov 1991
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 882
- Already set (do not supply): none

### Source block (context only)

```text
Author: Linda Hasselstrom
Book: Land Circle
ISBN: 978-1555910822
Publisher: Fulcrum Publishing
Date(Month/Year): Nov 1991
```

### Introduction (context only: never use it for content warnings)

```text
Linda Hasselstrom, who runs a cattle ranch in western South Dakota and has deep ties to the land, speaks eloquently on environmental subjects. In this collection of poems and essays she pays tribute to the people of the Great Plains and their way of life, taking issue with those who regard the area as an arid expanse fit only for waste dumps and exploitation. Writing movingly about the death of her husband and her efforts to cope with grief, she extols the virtues of hard physical work and the satisfactions of being close to the land. Using vivid images of wildlife and landscapes, the author challenges animal rights activists, praises the cow, makes a strong case for sustainability in agriculture. Establishing Perpetual Care at the Locust Grove Baptist Cemetery by Linda Hasselstrom.
```

### Performance text (classify this)

```text
A knock at the front door echoes in the landlady’s empty hall tinkles past the crystal in the cabinet, drums across her kitchen floor to mine. She’s not home. Whoever it is will come to my door next. I stretch, drop the pen and fill the kettle. Light the stove with a wooden match.

A stooped man in a black suit
rounds the corner, dust rising
behind his cane with every step.
Ancient sweat stains streak
the band of his straw hat
like layers in old sandstone.
He shuts the gate behind him.
Thumps the door four times
with a rugged fist.
Straightens his shoulders.

I snap the bolt open, but stay behind the locked screen door. “Good afternoon,” I say.

He pinches his hat with two gnarled fingers, lifts, and says, “Good day, Ma'am. I'm Walter Mathis from up at Locust Grove.” He hangs the cane on one arm, mops his forehead with a red kerchief, tucks it in a shirt pocket. “Does Mrs. Notye Murray still live here?”

He’s afraid she’s dead.
“Yes,” I say. Adding the “Sir”
is automatic, involuntary, even.
“That’s her door you knocked on.”

“She's not home, then,” he says,
nodding. Just what he thought.
He squints, leaning toward the screen.
“You her granddaughter?”

“No sir, just a tenant—I rent this back apartment,” I say.

Because it’s cheap, I think; because
I’ve left my husband
and have no money and no credit.
“When she goes out in the afternoon,
she's always back by dark,” I say.
“Unless it’s her whist night. But that’s Thursday.”

He leans back on his heels,
rapping the cane against the concrete step.
Eyes the packing plant fence
like he's tempted to get the hammer
and a fistful of nails out of the tool box
I know is behind the pickup seat,
fix the blasted thing so it’ll stand up straight.
“Well,” he mutters. “Let me think.”
He yanks the hat brim down.

I unlock the screen door, step outside
to say, “She might be home earlier.
I’m not real sure where she was going
but if she went for poke salat
and lambs quarters,
she might be home pretty soon.”

“Cooks ‘em up with bacon, I bet,”
he says, grinning. “Bet you never had
vittles like that, beings you are a northern lady.”
He nods. Another thing he knew
without even thinking.
I nod right back at him. The cane
pounds once more on the step.
His mind’s made up. “Well.
I gotta be gettin back to Locust Grove
so you tell Notye—you tell Miz Murray for me.
We gotta get goin on this perpetual care
for the cemetery up there. Us old-timers,
we figure maybe the next generation
won't be as interested in the folks there.
But her and me, we got close folks—
she's got her ma and pa and husband up there
and all my folks are together in that one spot.”

I nod again. Now I remember who I am,
even if I don’t know where.
I can see the cemetery in my home town,
where once I could imagine
my husband’s tombstone with mine beside it,
infinitely announcing our devotion.

He shoves the hat to wipe
his forehead on his sleeve,
yanks the brim back down. Nods again.
“Well, I live right by the cemetery, don’t ya know.
Me an’ Howard Breedlove and Walt Kinsolving—
that's my son-in-law—we all got together
cause folks been wanting to give me money
so there'd be some kind of continual care.
And I figgered if I just took money
even if I put it in a bank,
pretty soon some bank examiners'd
want to know what I'm doin,
and pretty soon after that
the income tax people
would come a'sniffin around.

So we formed an association. I'm president.
Yep. Howard Breedlove's treasurer.
I come down here today to get papers
drawed up and signed. And I wanted to tell her
if she wants to send a check
to make it out right, to make it out to
The Locust Grove Baptist Cemetery Association.
I always mow the lawn, mowed it
seven times last year, charged forty dollars
an they paid me OK, but the year before
I mowed it ten times an there wasn't
enough money in the treasury to pay me
so I just give 'em the last one.
I lived there all my life and all my folks
are buried there. I usually got
some grandchildren to help me.
About your size."

Walter Mathis waves his cane,
redeems me as his grandchild.
I’m ready to follow him home
to Locus Grove, learn to cook
poke salat just the way he likes it.

“Here now, you tell Miz. Murray
I come by and to make the check out
Locust Grove Baptist Cemetery Association.”
He tips his hat again. “Good day to you, ma’am.”

The kettle’s boiling. While Walter’s 1953 Ford pickup
lumbers down the street, I pour my tea,
take the cup upstairs and lean to look
out the bedroom window, to watch
until Walter Mathis turns left
on the gravel road out of town,
headed back to Locust Grove.
I sip my tea and know it’s time
I headed home
where people recognize me,
where the cemetery dust
is folks I knew.
```

---

## IC-1559: Fierce Fairytales (Societal Impacts on Men)

- Title: Fierce Fairytales (Societal Impacts on Men)
- Author (byline): Nakita Gill
- Work: Fierce Fairytales
- Publisher: Hachette Books
- Publication date as stated: Sept 2018
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1354
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nakita Gill
Book: Fierce Fairytales
ISBN: 978-0316420747
Publisher: Hachette Books
Date (Month/Year): Sept 2018
```

### Introduction (context only: never use it for content warnings)

```text
Men in our society today are suffering, and the people in their immediate circles are in crisis because of it. Men can literally be self-destructing right before our eyes and we just ignore it. See, society hasn’t done a good job equipping men for the roles we expect them to step into. We expect good men, wise men, protectors; but we don’t equip them to be the men we want and need them to be. The bottom line is that hurt people hurt people . . . By the time most men figure out they are damaged, it’s usually too late.

Nakita Gill examines this societal travesty in her book of poems entitled: Fierce Fairytales
```

### Performance text (classify this)

```text
Man Up, Hercules (Pg 127-128)

When I was a child, my worst nightmare was to see my father cry.

It occurs to me now that the world around me doesn't want men to feel. It emphasizes stoicism till they bottle up their feelings.

And if ever one of them falters, 'man up' becomes the dark magic to charm them back into line. 'Man up' is that villain who shows up with lackeys 'grow a pair' and 'boys don't cry'.

We tell our sons stories about heroes like Hercules, but forget to mention how Hercules' rage caused him to murder his entire family.

And by telling them stories where anger becomes the only acceptable way they can express themselves, we are teaching them shouting, punching, yelling is all they can ever do to release themselves from hell.

And this is how cursed phrases like 'man up' contribute to the greatest killer of men under 45.

Repression leads to depression,
depression leads to trying to find ways to be alive
and after years of being told not to feel,
the only way to truly feel it all becomes suicide.

We have created nooses with words and watch passively as our sons tighten them around each other's necks.

So I will tell my son, I will say, Cry, let the dam burst, and let the rivers you are holding

back run free. It will release everything that hurts you and finally you will be able to breathe.

The definition of who you are as a man is too

powerful to be swayed by a phrase, it doesn't have to be proven through self-hate.

When they tell you to 'man up' look them in the eyes and just say, 'I will not, no.' Child's Play (Pg 25)

It always begins when we are children with imaginations so big we put whole universes to shame.

We tell each other stories layered with childlike epiphany and fiery self-belief

We squabble over who gets to play the princess or the hero prince.

None of us want to be
the dragon that is slayed
nor the ogre nor the witch.
Right there in our child's mind
we decide everyone can
only be very evil or very good.

We never stop to consider that all of us are capable of doing terrible things.

We have all taken turns being Red Riding Hood and we have all been the wolf

TRANSITION

But as is true for everyone, we grew up . . . our world changed and the fairy tales darkened

How a Hero Becomes a Villain (Pg 51-52)

Trauma when left untreated has the capacity to make a villain out of you.

No one understands how little boys
who save villages, who become war heroes,
who have fathers that just expect
them to be brave no matter the cost
become villains without even trying to.

How you weren't always an arrogant,
self-involved, obsessive bad guy, how that is
just the way you project yourself
to keep the vulnerable little boy hidden;
this is what is expected of you,
the strongest man in the whole village.

This is how a hero like Gaston becomes the devil in the story which could Have been about his only chance at finding love.

Take this as your reminder. Not all heroes wear capes. Some wear darkness, some wear wounds.

The Woods Reincarnated (Pg 13)

[And as time passed]

We traded the woods for high-rises,

the wolf became the boy next door,

soft brown eyes and close-lipped smiles

to hide the flash of fangs instead of teeth.

The huntsman became the 'nice' man

that happened to live down the street

whose laugh never quite reached his eyes,

and the beaten track gets hazy

between grandmother and beast.

When the forest paths become the backstreets of a city,

Where predators learn a sweeter language

Accented with false niceties.

Sometimes it’s the wolf that thrives.

[This is] What happens to the fairytale

when the woods have been replaced by cities;

and a concrete jungle that comes to life . . .

The Trolls (After Shane Koyczan) (Pg 105-108)

Banished beneath bridges,
there were once brewing beasts
we gave a different name.
We called them trolls before
but it appears their numbers
have doubled, have tripled
have quadrupled since.
So here it is,
an origin story about the monsters amongst us
with no princess or prince.
In desperation to save themselves
from the dreadful damp below bridges,
they began to prey on humanity.
But the more they tried to hurt us
the more we fought back
until one day we finally
managed to beat them back,
the stories became legend
and the legends became myths,
yet this is where the story really begins.

You see, the trolls were never dead.
They were simply asleep,
biding their time,
waiting for us to forget them,
to leave them as fairy stories.
When the first child turned on
his first computer, a tremor was felt.
And that was when they rose
from their man-made prison hell,
they wore new avatars
and had learned to embrace
their lack of empathy and morality,
instead of hearts they now devoured
hopes, dreams, and an entire human just being.

They seek out the depressed
and find the lonely,
they make targets out of children
and sow divisive seeds
amongst friends and families.
All through the words on a screen
they make weapons; sticks and stones,
shovels to bury dreams.

They break open souls,
eat whatever happiness is left inside
and cause death and suicides,
destroy families and cause loss
using just words,
lies twisted into more lies.

We cannot hide from them,
cannot beat them back,
we cannot turn them into stories again,
we must face simple facts:
they now live amongst us
their bridges are burned and gone.
They wear armor made of code.

We cannot protect our children
from these evil beings,
but we can teach them
how to protect themselves.

TRANSITION

Unfortunately, protecting himself was never something that the Hatter in Alice in Wonderland learned to do. And while children love his fantastical character and the randomness of his thoughts, his existence too has a dark side. How did society impact the Hatter? Did it truly make him ‘mad’? . . . hurt people hurt people.

The Hatter

To understand what they did to the Hatter, I must first tell

you about people who know how to play with your

brokenness like it is a fidget spinner without so much as

touching your skin-a form of abuse known as gaslighting.

You say it happened, they say it did not.

You say it had to, they say it cannot.

They pull at a thread of pain left by someone in your mind,

and sew an entire ghost out of you.

Build you a dark wonderland and ask you to call it home.

Tell you, 'Why can't you just be happy?' And you cannot

because happiness in this story is a queen you do not trust

being built from your own delusions.

When this happens, you are like the Hatter. Trapped here

in this fairytale world, half mad because someone you love

keeps lying to you.

Is this rain, dear? No it isn't, it's a raven.

Is this a door? No, it is a writing desk.

Is this my mind? No, it is now my rabbit hole, and I’m

going to make you fall so far down there is no way out.

This is why the raven becomes like a writing desk, nonsensi-

cal riddles and memories become valid, nothing makes

sense anymore anyway.

You start wondering if anything you ever thought happened

to you actually happened to you and this is their violence.

This is their abuse. It has left bruises and gashes along your

brain that no one else knows are there.

Doubting yourself is now a reflex. Trusting yourself is no

longer muscle memory but a long, strenuous process.

They called the Hatter
completely mad.
Because he is cursed
to both remember
and to forget.

They call me mad too
because my curse is to heal
through remembering
everything you tried
to make me forget.

********

'Man up'

'grow a pair'

'boys don't cry'

'Man up'

(Stand up straight and tall, square your shoulders and say with conviction)

'I will not, no.'
```

---

## IC-1560: Fight Evil with Poetry

- Title: Fight Evil with Poetry
- Author (byline): Not specified
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 956
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dick Westheimer
Web link: https://rattle.com/an-american-jew-fails-to-
make-sense-of-the-carnage-in-gaza-by-dick-westheimer/
Publisher: Rattle Magazine; Rattle's Poets Respond
Date (Month/Year): June 1, 2021
Author: Yoram Symons
Book: Fight Evil with Poetry, Pgs 99-101
ISBN: 978-0997129762
Publisher: Sideshow Media Group
Date (Month/Year): Oct 2018
```

### Introduction (context only: never use it for content warnings)

```text
The war in Gaza, particularly the loss of civilian lives, has led to a questioning of Israel's actions and a sense of disconnect for some Jews who initially supported Israel's response. Poet Dick Westheimer explains: “I am shocked by news from the Middle East -- from the evictions of Palestinians from Sheikh Jarrah to the raids on the al- Aqsa mosque to the Hamas rockets cascading indiscriminately on Israeli cities to the massive reprisals -- resulting in incalculable suffering -- launched against Gaza. Like many American Jews I am torn between my desire to see a secure Israeli/Jewish state and the horror of seeing my fellow Jews forsake fundamentally Jewish values.” -- Tikkun Olam (repairing the world), Tzedakah

(righteous giving) and Chesed (loving-kindness).

An American Jew Fails to Make Sense of the Carnage in Gaza by Dick Westheimer
```

### Performance text (classify this)

```text
An American Jew Fails to Make Sense of the Carnage in Gaza by Dick Westheimer Four-year-old Sarah of Gaza can’t feel her legs. Her brother can’t forget the roof falling. Their father, Zahir can’t find a way to help either of them and I can’t stop crying -- anymore than I can stop being a Jew, anymore than I can forget the hunger that claws at my gut on a fast

day, anymore than I can stop a building from collapsing

on a child in Gaza.

Out my window, I see a red-winged blackbird harrying a vulture who can’t stop being a vulture set upon by a

blackbird who can’t help being a blackbird harassing a vulture who can’t stop eying the mamma-bird’s

gape-mouthed nestlings.

I am neither vulture nor red-wing. Nor am I a Jew at least according to Genesis 1:26 which says on the sixth

day God created humans -- nothing about Palestinians and Jews and line 21 didn’t say on the fifth day God created blackbirds and buzzards -- just nonspecific winged things. Yet I see in the trees outside my window -- one Biblically unspecified species that can’t resist

tormenting another.

Making sense of the never-ending contest among
our tribes by counting dead Gazans and Israelis
is like trying to understand the Bible
by counting its words then dividing
by the pieces of shrapnel lodged in little Sarah’s spine
or the tally of rockets that rained on Israel last week
or the count of families fearing eviction from Sheikh Jarrah
or the sum of all Arabs driven from their homes
or Jews from theirs or the two fingers, blackened and

scarred, Sarah raises, smiling as she says to the reporter,

“I am strong.”

But here we are, smile and shrapnel, blackbird and buzzard, the fifth day and the sixth -- and then the seventh when

God said: you guys figure it out.

We didn’t.

Which is ironic because my tribe worked out a lot -- like “welcome the stranger” and “love thy neighbor” and don’t

covet or murder or lie about anyone. We did just fine except for the times it felt like every person in the world wanted to burn us or drive us away. Yet, as soon as we found refuge in a land already inhabited, built that place in our own image, we turned into

a covetous sort.

Tonight at Shabbat, my four-year-old grandson Jude,

dressed in lavender, twirls and tumbles about the room, sparks like stars in the

candlelight. I recall a video of Sarah from the day before the bombs fell. She shows off her pink Eid dress, her eyes smile deep

chocolate brown
like Jude’s. I turn away and dream of a future:
At a feast, I am arm-in-arm with Zahir
as our two dancers swirl in a blur of scarves,

purple and pink.

TRANSITION The Israel-Hamas war includes many if only’s: If only Hamas had not rampaged across Israel’s southern border to torture, murder and kidnap on Oct. 7, 2023; if only Hamas had not cynically placed their fighters, command centers and weaponry in crowded civilian centers; if only the leaders on both sides could agree on a ceasefire; if only Jewish people living abroad weren’t facing increasing levels of antisemitism as a direct result of decisions over which they have no control . . . I am a Jew by Yoram Symons

I Am A Jew By Yoram Symons I am a Jew

And, sometimes
I am afraid
to admit
that I'm a Jew

So, sometimes
I just sit
And admit
Nothing.

You can hide the Jew.

Jew isn't a skin colour.
What's your name?
Yoram I say
That's an interesting name. Where's it from?
It's Jewish
I wanna say
Ought to say
Should say
But don't say
So instead I say
It's from the Bible. Towards the back.
And then change the topic of conversation.

Because you can hide the Jew. Jew isn't a skin colour.

My fear is this.
I get up in public spaces
In front of all the anticipating faces
To reveal vulnerability and existentiality

But then from the back somewhere Someone suddenly screams:

F**** you Jew!

Why are you murdering Palestinian babies?

Look at you,

Standing up there on a stage

While you oppress an entire people,

Grind them under your colonial boot,

Murder their children,

Massacre their babies,

Demolish their homes and

Steal their land and

Systematically

Systematically

Systematically

Deny their existence as a people,

Deny their right to their own homeland,

Deny that they are even suffering at all,

And on top of it all

To cry to the world

That you are the victim.

F*** you Jew.

So what do I say? What should I say?

I ought to say:
F***the Government of Israel!
I recognize
Your dirty lies
Your apartheid
And your genocide

But by the time I get home
By the time I get home
And check my facebook feed
It begins:

How dare you?

Betray your own people!

Haven't we suffered enough?

All those generations

Died for you

And now you throw it in their faces

Coward

Traitor

Self-hating Jew-hater.

Don't you understand?

They want to kill us Murder us

Throw us into the sea

Smash us

Gas us

Make us bleed

Seventy years of Israel with a gun to our heads

And you want the holocaust

To happen to us

Again?

We are murdering human beings!

They are animals! We invaded their land

It's not theirs, it's ours! We are doing to them what was done to us

Shut up! Shut up!

There is NO comparison There IS SO a comparison

There is NO comparison!

SHUT UP! SHUT UP!

SHUT UP.

Shut up

Shut up
```
