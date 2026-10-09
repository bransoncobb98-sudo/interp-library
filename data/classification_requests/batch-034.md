# Classification request: batch 34 of 53 (40 records, IC-1721 to IC-1760)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-034-reply.json`.

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

## IC-1721: Tom Thomson in Purgatory

- Title: Tom Thomson in Purgatory
- Author (byline): Troy Jollimore
- Work: Not specified
- Publisher: Margie/IntuiT House
- Publication date as stated: Aug 2006
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 725
- Already set (do not supply): none

### Source block (context only)

```text
Author: Troy Jollimore
ISBN: 978-0971904057
Publisher: Margie/IntuiT House
Date (Month/Year): Aug 2006
```

### Introduction (context only: never use it for content warnings)

```text
Purgatory is believed by Roman Catholics, and very few other Christians, to be a location or state where the souls of most individuals go at the time of death. The purpose of purgatory is to cleanse the individual from the temporal consequences of her or his sins while on earth. Eventually, the person will be eligible to be transferred to Heaven . Tom Thomson has reached the end of his life . . he’s not a hero, he’s not famous – He is “everyman” and for this very reason we can identify with the inventory of his life.

He’s Tom Tomson in Purgatory by Troy Jollimore.
```

### Performance text (classify this)

```text
Sin Cleansing # 1: Tom Thomson in his office, Thursday afternoon

Fills out grant applications. Honestly. Although they asked him not to. That's, you know, against the rules. Is honesty, that is. And knows he therefore will not one red cent get from them this year. Nor desires he to. Rejection is his muse. He thrives on it! (Who else can say they thrive on anything?) These days, that is. (His father's phrase.) But he's more strong than they by far: For he can smile and hoist a planet onto shoulder, he can laugh at pain (and knows more pain than they) more pain, more love, more lust, more everything! He is made stronger what does not kill him. And what does kill him, make him stronger still.

Sin Cleansing # 2: Tom Thomson in His Library

Bookplates, he useth not. Nor needs he to.
Reason the First: all his books share his scent,
a musk of salt-sea air, pine redolent,
and hint of freshly doused campfire (suggest-
ing liberty to some, but to the rest
the reek of disappointment.) Crack the spine
and sniff: you'll know if from his cache it came.
Reason the Next: he has not loaned a book
to anyone for ten plus years. For no
one reads no more, and fewer people still
read what he reads, or feel the slightest pull
to transact business -- giftings, borrowings --
with this musty old man whose books all smell
of salt, of lonesome woods, of drenched dead flames.

Sin Cleansing # 3: Tom Thomson in Limbo

Each thing done is a thousand things not done:
to read Frost is to not-read Henry James
or Keats and/or Rimbaud or Heisenberg ...
(Calculus floors him. Physics spins his mind
beyond all equilibrium.) But worse,
to read anyone else's books is to
not-write his own. But why, when others' songs
fill all the airwaves full, should lack of song
on his own part make him feel shameful so?
If every ear already is stuffed dumb,
why want a voice? (He knows what she'd suggest:
pure egotism.) "In silence can man best
preserve his own integrity," fortune
from fortune cookie say. "And he say " ."

Sin Cleansing # 4: Tom Thomson in Stereo

The all-day all-night FM radio station
that broadcasts just south of his cerebellum
has switched formats. Now
it’s Greatest Misses From Your Teens and Twenties:
a looped guitar set on Repeat Repeat
overdub-echoed, greased with Frippertronics;
an anxious dream in which, again, again,
he do, he say, exactly the wrong thing,
or miss the meaningful, inviting glance,
or stand on shore as the last boat, last chance,
pass by his little island. Twist the knob,
the song remain the same. He needs anten-
nae longer than the ones he got to hear
the tune of glad heart that must somewhere play.

Sin Cleansing # 5: Tom Thomson in Transit

"That train's not run here for a thousand years." (He means a hundred, maybe?) "They still sell the tickets at the station, though, if any-one would like a useless souvenir ... "

And Tom is tempted: he do love useless things. Remind him, they, of someone he knows well. His wallet's stuffed with currency from all manner of countries not in business now;

his camera aches for discontinued film.
(Ditto his typewriter & its odd ribbon.)
And all his maps are maps of continents
that sank without a trace some time ago,

flora and fauna gone extinct, extinct as Tom himself feel he must surely go.

Sin Cleansing # 6: Tom Thomson in Doubt

Lay down them projects for the crackling stars.
The hourglass sifts itself. Stars sprawl and blaze
in every each direction, and their howl
torments him into sleep. There was a point
from which they all emerged, of infinite mass,
through which he right now passes possibly through,
knowing it not. But then, what does he know?
And what could tell he to another ear?
Ears tilt away from him now when he speaks,
and people form strange patterns, fields, as if
a magnet he, and iron filings they.
“Lay down,” he just repeats, “them projects.” He
gives often to himself advice, and trusts
himself, though less these days, to get it right.

Cleansing Complete: Tom Thomson in Flanders Fields

The poppies grow, between the crosses row
by regimented row, and as they bob
pathetic Tom bobs too (I mean sym-
pathetic, for our man is overcome

and only refuge he can find is in
corrective fantasy: 1916
with Thomson gun in one hand, Thomson girl
in other, doffs his cap he, take his leave,

and head to France to shoot up several Germans.
(Ignore the fact that he’s a pacifist,
and closest he has come to shoot a gun
is his excessive use of bullet points;

it’s his fantasy, for Christ’s sake!)) Tom, he linger for a while, then go home.
```

---

## IC-1722: Transgender Reflections (A Collection)

- Title: Transgender Reflections (A Collection)
- Author (byline): Alex Peach, Sam Rush, Ethan Smith and Miles Walser
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1346
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alex Peach
Book: Published On-line
ISBN: N/A
Publisher: Thinkqueerly.com
Date (Month/Year): April 30, 2018
Website: https://thinkqueerly.com/sticks-and-stones-
fa6d3161d8cc
Author: Sam Rush
Book: Published On-line
ISBN: N/A
Publisher: Medium.com
Date (Month/Year): April 30, 2016
Website: https://medium.com/@poetrylyrics/sam-rush-
neverland-c8ff067e3f44
Author: Ethan Smith
Book: Published On-line
ISBN: N/A
Publisher: EveryDayFeminism.com
Date (Month/Year): Feb 20, 2016
Website: https://everydayfeminism.com/2016/02/letter-to-
girl-i-used-to-be/
Author: Miles Walser
Book: Published On-line
ISBN: N/A
Publisher: Outspoken Word Poetry
Date (Month/Year): November 24, 2015
Website:
http://outspokenwordpoetry.blogspot.com/2015/11/lillian-
miles-walser.html
```

### Introduction (context only: never use it for content warnings)

```text
According to the Human Rights Campaign, in 2021, state legislatures have introduced more than 100 bills that aim to curb the rights of transgender people across the country. From bathroom bans to youth sports restrictions – most of these bills affect transgender youth, a group that researchers and medical professionals warn is already susceptible to high rates of suicide and depression.

It seems that our country is devolving into a system of labels to define and isolate. When the truth of the matter is: every person in our society has value and every person should be treated with respect. “He/his; she/her or even they/them” – even these small words are important.

In this collection, Transgender Reflections, Alex Peach, Sam Rush, Ethan Smith and Miles Walser raise their voices to illuminate the person behind the label – people who are transgender are people first.
```

### Performance text (classify this)

```text
Sticks and Stones by Alex Peach Sticks and stones may break my bones but words will never hurt me. Bones can heal. Scratches, grazes, even gunshot wounds, they can heal. But the scars on the inside, the ones that no one can see — the words swirling around in people’s heads, ripping their insides out — those hurt. Those create scars.

Neverland by Sam Rush

When I was a little boy, I played Peter and rescued Wendy from Captian Hook and the crocodile's

tick, tick, tick. Meanwhile, the swallowed clock in my abdomen counted down minutes 'til my insides would betray me.

I carved symbols of manhood into never land trees, symbols I could never carve quite deep enough into me, and prayed my bark would scar quick.

When I was a little boy I played Peter. Peter always dressed in clothes made out of

leaves. Lost boys!
Little lost boys! Follow me!
Little lost boys dressed in the skins of the things they killed,
filled the forest with dancing little lots boy half-breeds.

When I was a little boy I learned little girls were pretty,
like lanterns, but not to be placed on the ground,
except when stronger light by house fire was needed,
having half-lives, at best.
I learned little girls in love thought less, and less clearly
that a glint in the eye was a chance,
an opportunity.
I learned elephants in your bedroom could
swallow secrets without first asking to sit on your chest.

When I was a little boy, I knew time would one day grow the weakness inside of me into blooming rot and I would wake up seeping. See when I was a little boy, I played Peter, I played Peter, but should have known it could only ever be make-believe. I could only ever be "Little lost boys! Lost boys? Follow

me!" I could only ever be Little Lost Boy dressed in the skins of

others,
I could only ever behalf-breed,
'cause when I was a little boy, I felt shrapnel hit daily
at this woman I would one day grow into being.

I have spent years clawing pieces from this body
I have fought to wake up seeing attached
to fingers I clawed freedom from and dug ditches with
and threw pitches out of.

When I was a little boy, I had little boy mouth and little boy

teeth and little boy tongue. I could little boy speak, but never learned how to hide my

little boy eyes
from all that’s lost when little boys see,
like how little talk there is to little boys
about the kind of strong little girls have to be.

A Letter to the Girl I Used to Be by Ethan Smith

Dear Emily, Every time I watch baseball, a voice I no longer recognize

whispers, “Ethan, do you remember? When you were gonna be the

first girl To play in the major leagues? Seattle Mariners. Rally cap.” But to be honest, Emily, I don’t. Dad told me that like it was someone else’s bedtime story. But I do know you had that drive, Didn’t let anyone tell you to wear shorts above your knees, Didn’t care if boys thought your hair fell on your shoulders

just right.

But with girls, sleepovers meant the space between your

shoulder and hers
Was a six-inch fatal territory.
The year you turned eleven
Was the first time you said out loud that you didn’t want to

live anymore.
In therapy, you said you wouldn’t make it to 21.
On my 21st birthday, I thought about you;
You were right.
At nineteen, you started to fade.
I tried to cross you out, like a line in my memoir
I wished I could erase completely.
And maybe I’m misunderstanding the definition of death,
But even though parts of you still exist,
You are not here.
Most of my friends have never heard your name until now.
I’ve been trying to write this letter for six months.
I still can’t decide if it should be an apology or not.
But now you will never hear “Emily Smith” announced at a

college graduation, Get married, give birth.

When the prescribed testosterone started taking effect, My body stopped producing the potential for new life every

month. I thought about your children, how I wanted them, too. I let a doctor remove your breasts so that I could stand up

straighter.
Now even if I somehow had those children, I wouldn’t be
able to nourish them.
My body is obsolete,
Scarred cosmetic, but never C-section.
I was four days late;
They will never be grandparents.
I was one week late;
They will never hold their lover’s sleeping figure.
I was eleven days late;
They will never breathe in a sunset and sunrise in the same

night.
I was two weeks late;
They will never learn to jump rope.
I was three weeks late;
They will never shout, “Watch, Mommy! Watch me on the

slide!”

I was two months late; A piece of us will never wrap their arms around our leg for

comfort,
Or just to keep them from falling down.
And I am . . . sorry that this process is so slow, and all you
can do is wonder if you ever had a place.
You did.
You still do.
Don’t forget that.

Yours, Ethan P.S. I never hated you.

Lillian by Miles Walser

I will name you Lillian because to me it sounds like running through a garden and with every step you take in life I want you to feel as beautiful as the flower I’ll call you. And don’t worry about your mother: whenever I meet her, I’ll convince her I deserve naming

rights. But more importantly, Lillian, you will inherit from me the

one thing
the world will let me give you.
I can’t hand you my curly hair or blue eyes,
so you will have the name that has followed me
from birth certificate to driver’s license to passport,
all the while knowing it was never really mine.
Your middle name will be Olivia.
For years I hated the name;
it burned through the paper of any official document I filled

out, seared my ears when it escaped the tongue of a stranger, and annihilated my entire body anytime I had to incorrectly

introduce myself. But Lillian, I understand what happened now. See, I am just the middleman; the accidental address on the

package. The name was given to me, to hold onto for you,

my future daughter. For you I keep it safe, protected from people who gawk at

me, not understanding why my short hair and masculine

appearance
can’t match the sweet femininity in the name.
Or people who do understand and hate me for it,
attacking the way I bypass the barrier of biological sex
because I know that what I feel is more important than

what I see in the mirror. And people who think I should conform to the name I was

given, ignoring everything I know about myself, the same people who will someday hate our family because

of me.

But through it all, Lillian, always remember that I love you. I’ve never met you, but I love you. My future daughter. So I hold the name under my shirt, against my chest, and with every heartbeat the syllables provide me a new sense of rhythmic direction. Because I know I’m moving towards you. The name Olivia no longer hides in the back of my throat but floats off my tongue. A promise of beauty; a promise of purpose. A promise of

you, my future daughter. Someday, Lillian Olivia, after you’ve mastered the art of the

two-wheeled bike, I’ll take you to the top of the tallest hill in town and we’ll

soar down,
secretly wishing we could take off into the rushing wind
and at the bottom I’ll tell you that
that feeling was how your father felt,
knowing someday, you’d be in his world.
And he’d finally get to give you your name.

(Neverland and A Letter to the Girl I Used to Be)
```

---

## IC-1723: The Triune Tale of Diminutive Swine

- Title: The Triune Tale of Diminutive Swine
- Author (byline): John Branyan
- Work: Not specified
- Publisher: Independently Published
- Publication date as stated: July 2020
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 717
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Branyan
ISBN: 979-8664574470
Publisher: Independently Published
Date (Month/Year): July 2020
KS State Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
What if the Three Little Pigs was retold in Shakespearean English? And what if the third pig, just to mix things up a bit, spoke good ol' American English? Wouldn't that be the best fairytale ever? The Triune Tale of Diminutive Swine by John Branyan
```

### Performance text (classify this)

```text
In time past, though not long ago, there lived pigs.
In stature . . . little.
In number . . . three.
Who being of an age both entitled and inspired to seek

their fortune. Did set about to do thusly.

When they had traveled a distance, pig numbered first

spake. Saying, "Harken brethren, heed this tempestuous

realm."

"Tarry we long from hearth and home we shall fare, I

fear, [snort] not well." And so being collectively agreed but individually

impelled, The diminutive swine set about each to erect for himself

an abode. Pig numbered One did construct his house from straw. Pig numbered Two did likewise. Though, rather, not from straw, instead from sticks. Meanwhile, unique in his imaginings, pig numbered Three

did erectus his domicile, Stalwart and garish, a structure made from brick

entirely.

Soon there happened along, as is frequently the scenario

in classic tale of protagonist pig, or redhooded child

. . . A wolf. Carnivorous nature in full season he called out to the

straw ensconced swine. Saying, "Pray thee, little pig, grant me entrance."

But pig One recalled with sage foreboding that, "He is mad who trusts in the tameness of a belly-pinched

wolf." And responded immediately, "Nay! It shall not be!" "Indeed, not by whit or whiskered jowl!"

Prepared for this most expected response, the wolf

replied immediately. "Then steel thyself little pig." "Forthwith shall I endeavor by employing means both

huffing and puffing to dismantle yon flaxen

fortress." Whereupon there issued forth from the wolf an exhale

of gale proportions, That quickly rendered straw hovel to dregs and dross

and carried aloft piglet and shattered quarters both.

Exposed now to claw and fang, piglet One made haste,

wolf in pursuit,
To the stick festooned sanctum of peccary secondary.
Causing pig Two to cry out in dismay,
"Well! This knots my knickers!"
"The marshaling of feral wolf to my doorstep is nowhere

among those endeavors amenable or congenial."

"A thousand pardons," squealed One. "T'would seem the beast's maim-full breath has purged

me of home and sound judgment alike!"

The mighty maelstrom of the wolf's exhale splattered

second swine's shack and shortened his

sanctimonious scolding simultaneously. "Lo! And Behold!" squealed Two. "Stand we now amid wooden wreckage tremulous and

vulnerable." "With nary a strategy for eschewing the canine

devourer looming in deadly proximity."

"Strategy!" squealed One. "While 'tis noble to contemplate tactical

particularities,"

"Pressed as we are with the time restraint forbidding

detailed strategical conversations," "I would urge we RUN!"

"Wee wee wee wee wee wee wee!"

Whether by their own fleet-footed competence or the

wolf's winless attitude, The diminutive swine arrived at their ultimate kindred

neighbor's inexpungeable brick ingress unscathed. Upon the third pig's door with urgent hooves they

pounded. Calling out, "Unbar this entrance and with haste we

beseech thee!"

The third pig hailed from the American Colonies. And possessing a vocabulary substantially less robust

than his impromptu visitors, replied, "Say what?"

"Seek we sanctuary!" they implored on the verge of

hysteria. "Lest we fall forthwith to the ravenous appetency of

yonder approaching carnivore!"

Still confounded by their importunate words, pig Three

did render ajar his portal. Whereupon One and Two spilled through and collapsed

beyond the threshold, enervated.

"So, y'all just wanted to come in?" "You could'a said that."

The sinister hiss of the wolf could once again be heard

outside. "Pray thee, pigs, grant me entrance."

"The wolf!" said One and Two.

"Wolf?" said Three. "What'd ya suppose he wants?"

"He seeks to gain purchase within." "Indeed he would occupy this very alcove were he but

afforded the most meager of opportunities."

"Right." "I'm just gonna go ask him what he wants."

"Under no circumstances!" squealed Two, flinging self

bodily against the portal. "There is naught to be gained accosting external

opponent." "Save our own immediate demise!"

"What did you say about my Momma?"

House and occupants were again engulfed in a malevolent

blast of wolfish wind. The foundation shook, the frame rattled. And lo, to the astonished eyes of piglet and encroaching

scoundrel alike, Stood the third pigs lodging, undaunted.

[Aside] Good news for you pig fans.

Aghast and dismayed, pig Two queried of Three. "How does against such relentless and torrential

onslaught this domicile endure?"

Pig Three, puffed out chest, tapped a hoof to the

hearth and responded. "It's American Made."
```

---

## IC-1724: Troll and Dear Invisible Men

- Title: Troll and Dear Invisible Men
- Author (byline): Shane Koyczan and Musa Okwonga
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1012
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shane Koyczan
Book: Silence is a Song I Know all the Words To
ISBN: 978-0991971848
Publisher: Stickboy Press
Date (Month/Year): 2014
Book can be purchased from the author's website at
https://www.shanekoyczan.com/merch-store
Author: Musa Okwonga
Book: Eating Roses for Dinner
ISBN: N/A
Publisher: Nomadic Books
Date (Month/Year): 2016
Must purchase from author on his website at
https://okwonga.bigcartel.com/product/eating-roses-for-
dinner-poems-by-musa-okwonga-2006-2015
```

### Introduction (context only: never use it for content warnings)

```text
Before the digital age, bullies occupied playgrounds, classrooms and walks home after school. Today, the internet has created new places for ‘trolls’ to hide.

This poem by Shane Koyczan takes a poignant looks at the pain caused by online bullies – also known as ‘trolls.’ These digital trolls hide behind anonymous usernames on sites such as YouTube or Instagram, insulting random people and urging suicidal kids to kill themselves.

Troll by Shane Koyczan
```

### Performance text (classify this)

```text
Troll
Once upon a time, you and all your kind
lived underneath bridges
had ridges for ribs that dropped off into empty

chests as if your hearts were all stolen treasures as if an excavation crew were hired to dig up and

remove the part of you that let you feel and while the world above you invented the wheel

you stayed put knowing that would one day roll over top of you to

get to where it's going you had an endlessly flowing supply line of food you began to brood over humanity and made meals

of our hope as if crushing our spirits would make your mirrors

cast better reflections than the ones they gave as if the only way you could save yourselves was to make the world ugly so no one would notice you

hided in it you learned to knit pain into a kind of camouflage treated hope like a mirage that you could use to

lure in your next meal you lived off our fears, you could taste what we

feared and every night, as the moon at bedtime stories on

sunlight you took darkness as an invite to head out into the

woods
you curled your hands into wrecking balls
your breath became squalls, you made rocks rumble,
you made land shiver, you made boys and girls pray that

someone would deliver them from you
we told them, you aren't real
and then one day, the world changed
but you all stayed the same
just migrated from living underneath bridges to living

underneath information superhighways days and nights became meaningless, each already deep

in chest became an abyss no one would ever find the

bottom of concepts like love fell into your gravity we turned ourselves into life preservers hoping to save

as many as we could but the fathers who guarded closet doors and the

mothers who secured the floors under beds all shook their heads not knowing how to deal with

you you, who crept into our lives, with tongues like knifes

stabbing your words into our skin you began to begin uploading yourselves into our homes you had computer screens for eyes and software for

bones you turned your hate into stones and hurled them at beauty, as if you couldn't bear to see

anything other than ugly anything different you had fingernails like flint and scraped them against

decency hoping we would be the ones to all catch fire you all had smiles like one-way barbed wire not meant to

keep us out, but to keep us in
always like a firing pin, you spoke in explosions
it isn't cute
it isn't funny
you talked strangers into death
and laughed
and as each family learns to graft skin over the wounds

you gave them, you helm yourself into the scar you have coaxed the sober back into bars, handed out

cigars at memorials offered nooses, cliffs, and pills to those who

unfortunately found you before they found
help
you praised suffering
waltzed in between tragedies, gracefully dipping

miseries as if we would be somehow
impressed by the dexterity of your animosity
you cheered on rape
dashed through police tape as if it were the finish line in

a race on who could be awful
first
even now
you somehow see this as an invitation to turn your

keyboards into catapults wondering which one of you can be the first to hate us

best
your loathing
already dressed in riot gear
ready to incite rage
as if each message board is a stage who you recite

hostility turning freedom of speech
into freedom of cruelty
we are stuck with you
the same way you are stuck with you
your mind is glue and it keeps malice fastened there like

cheap wallpaper
we were once upon a time told that none of you exist
we dismissed you as make believe or myth, now
on only with resolve
we can no longer afford to tell ourselves, that you aren't

real we will not let you make your dinners out of the things

we feel.

TRANSITION For people (particularly women) who suffer abuse online at the hands of trolls, this next poem raises some interesting and reassuring points. While trolls can cause a lot of pain by failing to recognize the real humans they are insulting, it can be easy when you’re under attack to forget that the trolls are real humans too. Humans with enough fear and emptiness in their lives to drive them to set up these anonymous accounts in the first place. Dear Invisible Men by Musa Okwonga.

Dear Invisible Men

Dear invisible men,
Who tweet women endless threats of rape,
Who are you?
Are you married fathers of two?
Are you teens crowded round a friend’s phone in a

canteen or KFC?
Are you pausing between texting your first love,
To set yourself up as an egg,
And post fresh hate?
Where are you as you type this?
Is your girlfriend asleep in your arms,
As you peer over her shoulder at your phone?

How did this become your sport?
You are not proud of what you do;
If you were, you would not care who knew.
This is strange:
You loudly announce pride in your prejudice
But your invisibility suggests your shame.
There is such an anger in you
That it cannot be cloaked with jokes.
I pity the mirror that has to reflect your misery,
Since it must see so much.
Because the women are everywhere now,
Aren’t they?
They weren’t just content in your beds,
Now they’re not just in your clubs,
Or in the eyes and hearts of other men;
The women are in your classrooms, boardrooms and DJ

booths,
They are obstructing you, or ignoring you,
Not needing you to improve.
Swiftly, they are sweeping you from every stage,
And the only place you feel safe
Is in one-hundred and forty characters of rage.
I doubt that, as you type, you will ever pause
To think that, while you promise terror,
The greatest fear is yours.
```

---

## IC-1725: Urges

- Title: Urges
- Author (byline): Poetri
- Work: Russell Simmons Def Poetry Jam on Broadway ... and More; Pg 153-156
- Publisher: Atria
- Publication date as stated: Aug 2003
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 793
- Already set (do not supply): none

### Source block (context only)

```text
Author: Poetri
Book: Russell Simmons Def Poetry Jam on Broadway ...
and More; Pg 153-156
ISBN: 978-0743476218
Publisher: Atria
Date (Month/Year): Aug 2003
```

### Introduction (context only: never use it for content warnings)

```text
The tantrums of a child who has no self-control can test even the most patient parent. However, when you're trapped in a crowded grocery store, making intense eye contact with a stranger during a meltdown or at a family dinner where everyone is pretending not to notice, these fits can be . . . socially devastating.

But don’t despair! These delightful toddler explosions can become slightly less frequent. Your child only needs to learn self-control instead of launching straight into chaos like a tiny, screaming banshee. Simple, right?

(on the brink of losing control) Right! Children should learn self-control, but sometimes . . . sometimes even adults just can’t control the -- Urges by Poetri
```

### Performance text (classify this)

```text
(Pg 153-156) I have the urge to jump over the counter at

McDonalds and
make my own Chicken McNuggets.
Cause I’m tired of telling them that I want them fresh and
I’ll wait the five minutes and
they still give me some hot, nasty, microwave, re-cooked

ones!

I have the right mind to slap the lady that tells me, “They are fresh.” No, they’re aren’t! Don’t you ever have the urge to just punch people? Sometimes for no reason, but especially when they do or

say something stupid. Too bad, I think sometimes, that my nice body doesn’t

react to my mind’s first reactions.

Cause whenever I walk into a library, I have the urge to start yelling. Then I wanna punch the first person that tells me,

“Shhhh, this is a
library.”
Like I don’t know!
I have this cruel urge to slap anyone that says libary. It’s

a library!

I have this weird urge to walk into Supercuts and demand

a haircut, even though I know they don’t cut black folk hair.

My urges are mean. They’re like my evil twin. Like I have the urge to go grab that booty right there. Everyone who knows me, knows I would never do that,

though. I have the drive to go rob a bank on broke days or go steal some money out of a cash register on some

days. Thank God I would never actually do that. Yet, am I criminal for thinking criminal thoughts?

I have the urge to go stand on the 405 freeway and hold my hand up and see how many cars I can get to stop. I have the urge to get hit by one of those cars to see who would come to my funeral. Just cause I have the desire to find out who really loves

me. . . do you?

Am I the only one? Do other people think about doing

things that they would
never do?
Am I the only one that says to myself. . . What if?
What if I did this? What if I did that?

What if I stood in the middle of the Beverly Center buck

naked?

Okay, maybe you don’t think that and
maybe that was just a little too much information,
but you know what am I saying.
What if we all acted out our urges?
I’d be dead or in jail, right now, or in insane asylum with

Unsane. Trying to refrain from thinking that I’m on the Midnight

train to Georgia, with Glady’s Knight and one Pip, with a busted lip, and a

messed up hip, still talking ‘bout that trip on the Midnight, man, we done

flipped it if we acted out our impulses.

I have the urge to keep rhyming like that. I have the urge to become a cop so that I can arrest other

cops. I have the itch to tell the IRS that they can keep calling

and sending mail, but I’m not gonna pay them the money I owe until I get the

money.
I have the longing to tell telemarketers to kiss my a**!
I have the urge to splurge, no work, just play all day,
walk around cussing all day,
but I can’t do that. I won’t do that.
I’m a full fledge Christian. At least I try to be.
That doesn’t mean I don’t have urges.
That doesn’t mean I don’t slip and fall sometimes. . . okay

a lot of times. I have the urge to slap people that criticize us when we do

fall. When we fall victims to our urges, our desires, our sins.

Not all my urges are bad and cruel and senseless.
I have some nice urges, some sad urges,
things I need to do urges, things I want to believe urges.
Like I have the urge to believe that things really happen

like they do in the movies. Soon as I step out of the movie theater, reality erases

that urge.

I have the urge to ask you out.
Shyness always blocks that one.
The urge to cry in public,
my manhood bullies that away.
The urge to sing. . .
Yolanda Adams or Kurt Carr and the Kurt Carr singers.
I usually act on this urge and
don’t let me put Michael Jackson in the walkman.

Urges are a funny thing. Can you judge a man by his

urges? If so, then I am a pretty weird guy, leading a double life. But, I don’t think so, urges are what they are. Quick thoughts thrown at our brain from whichever angle. When we decide to act on these urges good or bad, then

we become them. Most of us rationalize and think. And thank GOD that most of us don’t act on all of all

urges.
```

---

## IC-1726: Voices of the American Indian

- Title: Voices of the American Indian
- Author (byline): Chrystos and Maurice Kenny
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 788
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chrystos
Book: This Bridge Called My Back
ISBN: 978-1438454382
Publisher: State University of New York Press
Date (Month/Year): March 2015
Author: Maurice Kenny
Book: Carving Hawk: New & Selected Poems, 1953-2000
Page 109
ISBN: 978-1893996502
Publisher: White Pine Press
Date (Month/Year): 2002
```

### Introduction (context only: never use it for content warnings)

```text
The 2020 murder of George Floyd at the all-too-familiar hand of police brutality has created much needed discussions on the continuing racial disparities in America. But still, Native Americans are left to wonder, will they get left out of this important conversation too?

The Native American population is small and their voices — not always heard . . . “Who killed George Floyd?” Everything and everyone that contributes to ongoing institutional discrimination. Blacks, Latinos, Native Americans -- the voices rise. Can you . . . will you listen?

The poems "I Walk in the History of My People," by Chrystos and “They Tell Me I am Lost by Maurice Kenny are about pain. The pain that divides the privileged from the suffering, the whole from the broken.
```

### Performance text (classify this)

```text
I Walk in the History of My People by
Chrystos
There are women locked in my joints
for refusing to speak to the police
My red blood full of those
arrested, in flight, shot
My tendons stretched brittle with anger
do not look like white roots of peace
In my marrow are hungry faces who live on land the
whites don’t want
In my marrow women who walk 5 miles every day for
water
In my marrow the swollen faces of my people who are
not allowed
to hunt
to move
to be
In the scars on my knee you can see the children torn
from their families
bludgeoned into government schools
You can see through the pins in my bones that we are
prisoners of a long war
My knee is so badly wounded no one will look at it
The pus of the past oozes from every pore
The infection has gone on for at least 300 years
My sacred beliefs have been made pencils, names of
cities, gas stations
My knee is wounded so badly that I limp constantly
Anger is my crutch
I hold myself upright with it
My knee is wounded
see
How I Am Still Walking

They Tell Me I am Lost by Maurice Kenny

my feet are elms, roots in the earth
my heart is the hawk
my thought the arrow that rides
the wind across the valley

my spirit eats with eagles on the mountain crag and clashes with the thunder

the grass is breath of my flesh and the deer is the bone of my child

my toes dance on the drum in the light of the eyes of the old turtle

my chant is the wind
my chant is the muskrat
my chant is the seed
my chant is the tadpole
my chant is the grandfather

and his many grandchildren sired in the frost of March and the summer noon of brown August

my chant is the field that turns with the sun and feeds the mice and the bear red berries and honey

my chant is the river that quenches the thirst of the sun

my chant is the woman who bore me and my blood and my flesh of tomorrow

my chant is the herb that heals
and the moon that moves the tide
and the wind that cleans the earth
of old bones singing in the morning dust

my chant is the rabbit, skunk, heron
my chant is the red willow, the clay
and the great pine that bulges the woods
and the axe that fells the birch
and the hand that breaks the corn from the
stalk
and waters the squash and catches stars

my chant is a blessing to the trout, beaver and a blessing to the young pheasant that warms my winter

my chant is the wolf in the dark
my chant is the crow flying against the sun
my chant is the sun
sleeping on the back of the grass
in marriage

my chant is the sun while there is sun I cannot be lost

my chant is the quaking of the earth angry and bold

although I hide in the thick forest
or the deep pool of a slow river
though I hide in a shack, a prison
though I hide in a word, a law
though I hide in a glass of beer
or high on steel girders over the city
or in the slums of that city
though I hide in a mallard feather
or the petals of the milkwort
or a story told by my father

though there are eyes that do not see me and ears that do not hear my drum or hands that do not feel my wind and tongues which do not taste my blood

I am the shadow on the field
the rain on the rock
the snow on the limb
the footprint on the water
the vetch on the grave

I am the sweat on the boy the smile on the woman the paint on the man

I am the singer of songs and the hunter of fox

I am the glare on the sun the frost on the fruit the notch on the cedar

I am the foot on the golden snake
I am the foot on the silver snake
I am the tongue of the wind
and the nourishment of grubs

I am the claw and the hoof and the shell I am the stalk and the bloom and the pollen I am the boulder on the rim of the hill I am the sun and the moon the light and the dark

I am the shadow on the field

I am the string, the bow and the arrow
```

---

## IC-1727: Walt Whitman Strides the Llano of New Mexico

- Title: Walt Whitman Strides the Llano of New Mexico
- Author (byline): Rudolfo Anaya
- Work: Anaya Reader
- Publisher: Warner Books
- Publication date as stated: April 1995
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1290
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rudolfo Anaya
Book: Anaya Reader
ISBN: 978-0446670777
Publisher: Warner Books
Date(Month/Year): April 1995
```

### Introduction (context only: never use it for content warnings)

```text
In "Walt Whitman Strides the Llano of New Mexico,"

(retired English professor) Rudolfo Anaya examines the impact of teachers and teaching on the lives of students, especially first-generation college students and minority students. In our “No Child Left Behind” society, Anaya’s words speak clearly of the plight of the Chiano student to succeed in an educational world that has for too long closed the doors of opportunity.
```

### Performance text (classify this)

```text
“Chicano Child Enters University!" the papers cried.

Miracle child! Strange child!

Dark Child!

Speaks Spanish Child! Has Accent Child!

Needs Lots of Help Child! Has No Money Child!

Needs A Job Child! Barrio Child!

Poor People's Child! Gente Child!

Drop Out Child!

I met Walt, kind old father, on the llano,

that expanse of land of eagle and cactus Where the Mexicano met the Indio, and both met the tejano, along the Rio Pecos, our River of blood, River of Billy the Kid, River of Fort Sumner where the Dine suffered, River of the golden Carp, god of my gods.

He came striding across the open plain,

There where the owl calls me to

the shrine of my birth,

There where Ultima buried my soul-cord, the

blood, the afterbirth, my destiny.

His beard, coarse, scraggly, warm, filled with sunlight, like llano grass filled with grasshoppers, grillos, protection for lizards and jackrabbits, rattlesnakes, coyotes, and childhood fears.

"Buenos dias, don Walt!" I called. "I have been

waiting for you. I knew you would one day leap

across the Mississippi!

Leap from Manhattas! Leap over Brooklyn Bridge!

Leap over slavery!

Leap over the technocrats!

Leap over atomic waste!

Leap over the violence! Madonna!

Dead end rappers!

Peter Jennings and ungodly nightly news!

Leap over your own sex! Leap to embrace la gente

de Nuevo Mexico! Leap to miracles!"

I always knew that. I dreamed that.

I knew you would one day find the Mexicanos of my land, the Nuevo Mexicanos who kicked *** with our Indian ancestors, kicked *** with the tejanos, And finally got their *** kicked by politicians! I knew you would find us Chicanos, en la pobreza, Always needing change for a ride or a pint, Pero ricos en el alma! Ricos en nuestra cultural Ricos can suenos y memoria!

I kept the faith, don Walt, because I always knew you could leap continents! Leap over the squalor! Leap over pain and suffering, and the ash heap we Make of our Earth! Leap into my arms.

Let me nestle in your bigote, don Walt, as lance nestled in my abuelo's bigote, don Liborio, Patriarch of the Mares clan, padre de mi mama, Farmer from Puerto de Luna, mestizo de Espana y Mexico, Cat61ico y Judfo, Moro y india, frances y mountain man, hombre de la tierra!

Let me nestle in your bigote, don Walt, like lance nestled in the grass of the llano, on summer days, a child lost in the wide expanse, brother to lagarto, jackrabbit, rattlesnake, vulture and hawk. I lay sleeping in the grama grass, feeling the groan of the Earth beneath me, tierra sagrada! Around me, grasshoppers chuffing, mockingbird calling, meadowlark singing, owl warning, rabbit humping, flies buzzing, worms turning, vulture and hawk riding air currents, brujo spirits moving across my back and raising the hair of my neck, golden fish of my ponds tempting me to believe in the gods of the earth, water, air and fire. Oriente, poniente, norte, sur, y yo! Dark earth groaning beneath me, sperm flowing, sky turning orange and red, nighthawks dart, bats flitter, the mourning call of La Llorona filling the night wind as the presence of the river stirred, called my name: "Hijo! Hiiiii-jo!"

And I fled, fled for the safety of my mother's arms.

You know the locura of childhood, don Walt That's why I welcome you to the llano, my llano, My Nuevo Mexico! Tierra sagrada! Tierra sangrada!

Hold me in the safety of your arms, wise poet, old poet, Abuelo de todos. Your fingers stir my memory.

The high school teachers didn't believe in the magic of the Chicano heart. They fed me palabras sin sabor when it was your flesh I yearned for. Your soul. They teased us with "Oh, Capitan, My Capitan!" Read silently so as to arouse no passion, no tears, no erections, no bubbling love for poetry.

Que desgracia! What a disgrace! To give my soul only

one poem in four years when you were a universe!

Que desgracia! To give us only your name, when you were Cosmos, and our brown faces yearned for the safety of your bigote, your arms!

Que desgracia! That you have to leap from your grave, Now, in this begetting time, to kick ass with this country which is so slow to learn that we are the magic in the soul! We are the dream of Aztlan!

Que desgracia! That my parents didn't even know your name! Didn't know that in your Leaves of Grass there was salvation for the child. I hear my mother's lament: "They gave me no education!" I understand my father's stupor: "They took mi honor, mi orgullo, mi palabra."

Pobreza de mi gente! I strike back now! I bring you don Walt to help gird our loins! Este viejo es guerrillero por la gente! Guerrillero por los pobres! Los de abajo!

Save our children now! I shout. Put Leaves of Grass in their lunchboxes! In the tacos and tamales! Let them call him Abuelo! As I call him Abuelo!

Chicano poets of the revolution! Let him fly with you As your squadrons of words fill the air over AztLin! Mujeres chicanas! Pull his bigote as you Would tug at a friendly abuelo! His manhood is ours! Together we are One!

Pobreza! Child wandering the streets of Alburque! Broken

by the splash of water, elm seed ghost, lost and by winds

of spring mourned, by La Llorona of the Rio Grande

mourned, outcast, soul-seed, blasted by the wind

of the universe, soul-wind, scorched by the

Grandfather Sun, Lady Luna, insanity, grubs scratching

at broken limbs, fragmented soul.

I died and was buried and years later I awoke from

the dead and limped up the hill where your

Leaves of Grass lay buried in library stacks.

"Chicano Child Enters University!" the papers cried.

Miracle child! Strange child! Dark child!

Speaks Spanish Child! Has Accent Child!

Needs Lots of Help Child! Has No Money Child!

Needs a Job Child! Barrio Child!
Poor People's Child! Gente Child! Drop Out Child! "I'll
show you," I sobbed, entering the labyrinth of
loneliness,

dark shadows of library, cold white classrooms.

You saved me, don Walt, you and my familia which held

Me up, like a crutch holding the one-leg Man,

Like Amor holding the lover,

Like kiss holding the flame of Love.

You spoke to me of your Manhattas, working men and women, miracle of democracy, freedom of the soul, the suffering of the Great War, the death of Lincoln, the lilacs' last bloom, the pantheism of the Cosmos, the miracle of Word.

Your words caressed my soul, soul meeting soul, You opened my mouth and forced me to speak! Like a cricket placed on dumb tongue, Like the curandera's healing herbs and Touch which taught me to see beauty, Your fingers poked and found my words! You drew my stories out. You believed in the Child of the Llano.

I fell asleep on Leaves of Grass, covering myself with your bigote, dreaming my ancestors, my healers, the cuentos of their past, dreams and memories.

I fell asleep in your love, and woke to my mother's tortillas on the comal, my father's cough, my familia's way to work, the vast love which was an ocean in a small house.

I woke to write my Leaves of Llano Grass, the cuentos of the llano, tierra sagrada! I thank the wise teacher who said, "Dark Child, read this book! You are grass and to grass you shall return."

"Gracias, don Walt! Enjoy your stay. Come again. Come Every day. Our nifios need you, as they need Our own poets. Maybe you'll write a poem in Spanish, I'll write one in Chinese. All of poetry is One."
```

---

## IC-1728: War and Peace – A Collection

- Title: War and Peace – A Collection
- Author (byline): Israeli, Palestinian and One American Poet
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1175
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tzippi Shahrur
Book: After the First Rain: Israeli Poems on War and
Peace
ISBN: 978-0815605249
Publisher: Syracuse University Press
Date (Month/Year): Feb 1998
Also Online at
https://www.pressenterprise.com/2023/11/17/the-poetry-
of-war-and-peace-by-israeli-and-palestinian-poets/
Author: Amir Gilboa
Book: After the First Rain: Israeli Poems on War and
Peace
ISBN: 978-0815605249
Publisher: Syracuse University Press
Date (Month/Year): Feb 1998
Author: Mosab Abu Toha
ISBN: On-line Transcript
https://www.theatlantic.com/books/archive/2023/11/poem-
mosab-abu-toha-younger-war/675944/
Publisher: The Atlantic
Date (Month/Year): Nov 9, 2023
Author: Amir Gilboa
Book: After the First Rain: Israeli Poems on War and Peace
ISBN: 978-0815605249
Publisher: Syracuse University Press
Date (Month/Year): Feb 1998
Also online at
https://www.pressenterprise.com/2023/11/17/the-poetry-
of-war-and-peace-by-israeli-and-palestinian-poets/
Author: Nadine Murtaja
ISBN: On-Line Transcript
https://www.thenews.com.pk/magazine/us/1129276-
poets-corner
Publisher: The International News
Date (Month/Year): Posted Oct 16, 2023
Author: Joseph Fasano
ISBN: On-line Transcript
https://www.upworthy.com/powerful-poem-parenting-in-
war-zone
Publisher: Upworthy.com
Date (Month/Year): October 25, 2023
```

### Introduction (context only: never use it for content warnings)

```text
How many times? How many wars? How many times must history repeat itself, creating wounds that will never heal and generations of victims who know nothing but violence and revenge. So many times, humanity has promised itself – never again and yet here we are – Again.

I cannot be silent about the innocent civilians taken hostage in Israel and fleeing for their lives in Gaza. With so many political and military actions tearing us apart we have to remember what ties us together. Our humanity. Our hope for a better future. If there is a choice between War and Peace . . . I will always choose peace.

War and Peace – A Collection by Israeli, Palestinian and
```

### Performance text (classify this)

```text
A Soldier Wept on the Radio by Tzippi Shahrur

(Israeli)

On the radio a soldier was weeping,
“I’ve never killed a human being before,”
and amplified sobbing shook me.
And it was no longer necessary
to be ashamed.
Soldier,
what strength you had
to weep in the listeners’ numbed ears,
“I’ve never even killed an ant,” you pleaded.
Well, who hasn’t. . . but a man. . .
So I was with you
on the radio in that unsung hour
between a rock song and the news
when you mourned your enemy
into a microphone that was still alive.

one American Poet And My Brother Said Nothing (aka My Brother Was Silent) by Amir Gilboa (Israeli)

My brother came back from the field
Dressed in gray. And I was afraid that
My dream might prove false, so at once
I began to count his wounds.
And my brother said nothing.

Then I rummaged in the pockets of the trench coat
And found a field-dressing, stained and dry.
And on frayed postcard, her name –
Beneath a picture of poppies.
And my brother said nothing.

Then I undid the pack
And took out his belongings, memory by memory.
Hurrah, my brother, my brother, the hero,
Now I’ve found your decorations!
Hurrah, my brother, my brother, the hero,
I shall proudly hymn your name!
And my brother said nothing.
And my brother said nothing.

His blood was crying out from the ground.

Also Online at https://azm.org/yom-hazikaron-readings/

TRANSITION Mosab Abu Toha, a Palestinian refugee and celebrated poet wrote this poem last year, reflecting on his childhood under Israeli military occupation. Released by Israeli forces on November 21, 2023, he is currently struggling to survive in a United Nations refugee camp, with his wife and three children.

Younger Than War by Mosab Abu Toha (Palestinian)

Tanks roll through dust, through eggplant fields.
Beds unmade, lightening in the sky, brother
jumps to the window to watch warplanes
flying through clouds of smoke
after air strikes. Warplanes that look like eagles
searching for a tree branch to perch on,
catch breath, but these metal eagles
are catching souls in a blood/bone soup bowl.
No need for radio.
We are the news.
Ants’ ears hurt with each bullet
fired from wrathful machine guns.
Soldiers advance, burn books, some smoke
rolled sheets of yesterday’s newspaper, just like they did
when they were kids. Our kids
hide in the basement, backs against concrete pillars,
heads between knees, parents silent.
Humid down there, and heat of burning bombs
adds up to the slow death
of survival.
In September 2000, after I had bought bread for dinner,
I saw a helicopter firing a rocket
into a tower as far from me as my frightful cries
when I heard concrete and glass fall from high.
Loaves of bread went stale.
I was still 7 at the time.
I was decades younger than war,
a few years older than bombs.

Truce by Zelda Mishkovsky (Israeli)
A simple motion of the hand
cancels the torture, a motion
belonging to a suicide wolf—
a zealous youth who suddenly
was fed up with hate
because his soul revealed:
hatred lies
hatred lies
hatred lies—
and the force
of that thought, swelling with
the voice of childhood,
of miracles, broke through
to an untried path. The primordial
goodness welled up in him
and he saved the prisoner.
A river burst forth
from the Eden of his inwardness.
He offered the prisoner water, restoring
him in the desert. Slowly the monster
of revenge recedes and fresh
worlds appear, overflowing with water.
Alas! They both know:
This is not the whole truth,
this is a small truce in a green
island, that island which is
beyond every nation, whatever
its origin.
But on this island, in a dark cave,
Peace opened its eyes.

TRANSITION

In 2018 around 30 young and aspiring poets came together to form the Gaza Poets Society. In May 2021 their meeting place, a library and the largest bookstore in Gaza, was the target of an Israeli missile strike and completely destroyed. Nadine Murtaja, one of the Gaza poets was 18 then and wrote this poem in response to the missile strike. It documents the eeriness of life under siege, recording how, even during bombardment, hope persists: Today, according to her Facebook page she is a dental student at Al-Azhar University.

We Walk on The Shattered Glass of Our Broken Windows by Nadine Murtaja (Palestinian) There, on the other side, time changes, hours pass, and it gets darker, the sky takes off its dim dress, then the morning arrives, but here where I live and breathe, life wears its black dress constantly, to mourn the labor of my land, which took a long time. Here, the hanging clock in my room is broken, and not only this one, everyone’s clock is broken here, my mother keeps saying: everyone is waiting for the elixir we’ve had it with grief and agony, in this holy land we sleep and wake up to sounds of bombing and shooting, so the first light of day rises in the evening, lighting up the sky with the blood of martyrs, here death sleeps not far from us, we all walk towards freedom, towards hope, we walk on the shattered glass of our broken windows, we walk on stones that once were a house, carrying stories and secrets, we walk with the screams of children, and the groans of mothers pulsing over and over in our ears.

TRANSITION

What would you do to help a child – any child – feel safe in a time of war. Imagine holding them in your arms as you hide behind a pile of rubble. What words would you whisper to a child under siege?

Words Whispered to a Child Under Seige by Joseph Fasano (American)

No, we are not going to die.
The sounds you hear
knocking the windows and chipping the paint
from the ceiling, that is a game
the world is playing.
Our task is to crouch in the dark as long as we can
and count the beats of our own hearts.
Good. Like that. Lay your hand
on my heart and I'll lay mine on yours.
Which one of us wins
is the one who loves the game the most
while it lasts.
Yes, it is going to last.
You can use your ear instead of your hand.
Here, on my heart.
Why is it beating faster? For you. That's all.
I always wanted you to be born
and so did the world.
No, those aren't a stranger's bootsteps in the house.
Yes, I'm here. We're safe.

Remember chess? Remember
hide-and-seek?
The song your mother sang? Let's sing that one.
She's still with us, yes. But you have to sing
without making a sound. She'd like that.
No, those aren't bootsteps.
Sing. Sing louder.
Those aren't bootsteps.
Let me show you how I cried when you were born.
Those aren't bootsteps.
Those aren't sirens.
Those aren't flames.
Close your eyes. Like chess. Like hide-and-seek.
When the game is done you get another life.
```

---

## IC-1729: The Watch that Ends the Night: Voices from the Titanic

- Title: The Watch that Ends the Night: Voices from the Titanic
- Author (byline): Allan Wolf
- Work: Not specified
- Publisher: Candlewick Press
- Publication date as stated: Oct 2011
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1317
- Already set (do not supply): none

### Source block (context only)

```text
Author: Allan Wolf
ISBN: 978-0763637033
Publisher: Candlewick Press
Date (Month/Year): Oct 2011
```

### Introduction (context only: never use it for content warnings)

```text
April 14, 1912 -- An eerie night on the North Atlantic. The ocean, which is almost never still, was calm. Thousands of stars curtained the sky -- a backdrop to the human drama taking place. The Titanic was sinking slowly into the freezing sea. Nearly 1,500 people died that night. None of the rest survive today. But after more than a century, the disaster has never faded from the world’s imagination. Why? What made this disaster more memorable than all the others?

Other disasters were either too big or too small. They happened too fast, or too slowly. The Titanic sank in two hours and 40 minutes. Its cast of characters represented the human race – every rank and station – and they had time to see what others were doing and to think carefully about what they could do, or should do, morally.

The Titanic is remembered not for the horror of the disaster, but for what it teaches us about real people making the ultimate decisions of their lives: Should I take a seat in a lifeboat or give it to someone else. Should I send my wife and children, or should our family stay together? Should I save myself or try to rescue others?

The Watch that Ends the Night: Voices from the Titanic by Allan Wolf
```

### Performance text (classify this)

```text
John Snow – The Undertaker (Pg 45) “And so we begin.”

(Preface) My name is John Snow.
You could say that my living is death.
I am the undertaker.
I have come for the bodies.
(Pg 45) I admit to myself what I knew at the first sight of

them: Those are no seagulls. Those are bodies.

My God. My God. My God.
Bodies scattered for miles, in every direction.
Bodies as far as my indifferent eyes can see.
(Pg 88) Occasional errant corpses float solo here and there:
a lone woman (unchaperoned) lists to her side;

her right ear dips into each wave as if listening
for the water to speak her name. She wears
an intricate silk nightgown – robin’s-egg blue --
that billows at the surface.
The gown makes the sound of flapping winds,
but there are no birds. No angels.

Harold Lowe – The Junior Officer
(Pg 15) Be aware that on these big passenger vessels,
the “crew” are mostly window washers,
waiters, bellboys, and stewards . . . Oh,
they’re nice enough to have around
if you need to have your pillows fluffed,
but they aren’t of much use in a real crisis.
When it came time to report back to Commander Bartlett,
the White Star Line’s marine superintendent,
I said,

“We have tested and inventoried the lifeboats, sir.

And we find them stocked and ready.”

But I was thinking,

God help us if we actually need them,

since half the crew won’t know

which end of an oar goes in the water.

E.J. Smith – The Captain
(Pg 16) Do not speak to me of lifeboats.
Titanic has twenty lifeboats all told.
Four boats more than regulations require.
A stable ship like Titanic is life boat enough.

Of course I am not so foolish as to call her unsinkable. But I will say this: it would take a fool to sink her. I may be many things, but I am no fool.

(Pg 96) I will say this with the certainty my thirty years at

sea allow any absolute disaster involving the passengers is

inconceivable. Whatever happens, there will be time enough before the vessel sinks to save the life of every person on

board. Bruce Ismay – The Businessman

(Pg 17) Lifeboats? Why clutter a ship’s boat deck with lifeboats? First-class passengers would rather see the sunrise.

The Iceberg
(Pg 7) I am the ice. I see tides ebb and flow.
I’ve watched civilizations come and go,
give birth, destroy, restore, be gone, begin.
I watched as Abraham and Moses spoke.
I watched as Christ was nailed upon the cross.
I am the ice. I’ve seen the ebb and flow.

I carved out massive valleys as I moved.
At last the frozen river mad its way
and calved me with a splash in Baffin Bay.
Since then I’ve traveled southward many weeks,
for now that my emergence is complete,
there is a certain ship I long to meet -- Titanic
(Pg 121) Titanic leaves the land behind.
The Viking, Spaniard, Frenchman, German, Brit;
the rich, poor, blessed, cursed, brilliant, daft, or dim;
some of them make it, and some of them do not.
Indifferent to all that, the Iceberg floats.
The pinnacle of these humans’ ingenuity
means nothing to the Iceberg’s cold enormity;
the largest moving thing man can devise
is but a trifling dust caught in my eyes.
As if she were no larger than a pea,
she shrinks into the vastness of the sea.

Fredrick Fleet – The Lookout (Pg 202) Me job as lookout allowed me to watch all kinds of people: poor, well off, and bloody rich. Titanic’s crew ain’t so different from the passengers. The first-class passengers ain’t so different from the second-class or the third. They all use the loo. They all go in to dinner. They all laugh and cry. They all have a future. They all have a plan. They all hold hands with their little ones. And from where I sits in the crow’s next, a rich man and a poor man looks equally small.

The Iceberg (Pg 283)I am the ice. My next maneuver barely makes a

sound.
As you rush through darkness to my side,
the ice has flipped, exposing only black.
Black ice; clam seas; no wind; a moonless sky.
Could Fate provide a better place to hide?
I see her, but she does not see me.
The lookouts on her mast can’t make me out.
Make haste, now. Hurry. Bring heir hearts to me.
And do let’s get acquainted as you wish.
I hear the clock hands tick.
Shhh. Tick. Tick. Tick. Tick. Tick . . .

Fredrick Fleet – The Lookout

(Pg 290) CLANG! CLANG! CLANG!
I keep my eyes fixed
on the monster emerging from the night.
“Iceberg! Iceberg, straight ahead!”

E.J. Smith – The Captain
(Pg 302) “UNCOVER THE BOATS!”
I was giving out order left and right. But I really had no plan.
Two thousand two hundred and eight souls.
Twenty boats.
The mathematical disparity stung my brain.
(Pg 325) “Women and children, please! Women and

children!”
Harold Lowe – The Junior Officer
(Pg 310) Finding passengers willing to get into the boat
proved difficult. Not that I can blame them.
Descending in a boat is a dangerous thin,

And the likelihood of Titanic actually sinking --
well, the very idea was ridiculous at the time.
I admit that the first lifeboat was only half full,
but what was I to do, pull out my pistol and force people?
“Lower away! Lower away! Lower away!”

Bruce Ismay – The Businessman
(Pg 348) I was in the right place at the right time.
You’d make me your scapegoat
because I took a descending boat.
Was I to let it pass me by?
There was a space. An empty seat.
What would it serve, then not to fill it?
Is it my moral duty to stay with the ship?
Yes, other had been turned away.
Yes, other men had been denied.
I took no part in that.
In fact, I helped the women in
and then stepped back while the ladies sat.
Decorum dictates you must die;
common sense requires you live.
I’ll choose the time and place I face
my moral responsibility.
I was in the right place at the right time.

The Iceberg
(Pg 367)The hull cannot withstand the water’s weight.
And at long last, she slips into the deep.
And where the great Titanic used to be,
behold the souls left floating on the sea.
(Pg 368-369)

god help us so cold

our father who art in heaven over her children

please hey you in the boats

Love you my darling hold my hand

bring back the boats We’ll stay together

we’re over here my god Follow my voice can’t stop shaking Come back daddy will protect you

so cold Come back hurts to breathe

cannot swim We’re over here my god

help us Are they coming back so cold

someone please

Harold Lowe – The Junior Officer

(Pg 377-378) The mighty Titanic was gone.
I could hear (as well as anyone)
the terrible cries of those dying in the water;
I wanted to be sure that none of these lifeboats attempted
an ill-considered rescue that would result in more deaths.
Some women demanded we go back.
“I would rather die than do nothing.”
“I think it is our moral duty.”

I wanted to be clear that we were NOT rushing in to the

rescue.
My boat was already dangerously overcrowded
and it would take just one swimmer,
Swinging a leg up onto the side, to capsize us all.
Yes, many of our boats had empty spaces,
but what good are fifty seats when there are
fifteen hundred fighting each other to fill them?

Let me be quite firm when I say this:
Had any of us rowed a boat into that swarming mass,
Which was alive with thrashing limbs and clawing hands,
we all of us would have wound up dead.
To do so would have been suicide.
And even if it were remotely possible to do so,
who would you choose to come aboard and live?
Who would you choose to stay behind and die?
```

---

## IC-1730: The Watts Experiment

- Title: The Watts Experiment
- Author (byline): Adriel Luis
- Work: How to Make Juice, Pg 79
- Publisher: First Word Press
- Publication date as stated: 2006
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: SUBJECT B, SUBJECT A
- Teaser before the introduction: Yes
- Spoken words (computed): 752
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adriel Luis
Book: How to Make Juice, Pg 79
ISBN: 978-0977913602
Publisher: First Word Press
Date (Month/Year): 2006
```

### Introduction (context only: never use it for content warnings)

```text
A little history . . . Watts is a neighborhood in southern Los Angeles. Longstanding resentment by Los Angeles's working-class black community over discriminatory treatment by police and inadequate public services

(especially schools and hospitals) exploded on August 11, 1965, into what were commonly known as the Watts riots. Between 1989 and 2005, police reported more than 500 homicides in Watts, most of them gang-related and tied to wars over control of the lucrative illicit market created by illegal drugs. This poem was penned during that time and is a tragic tale about Black and Asian conflict in the neighborhood known as Watts.

The Watts Experiment by Adriel Luis.
```

### Performance text (classify this)

```text
We have TWO SUBJECTS of observation
(and we don’t really need to give them names because
they’ll both be dead by the end of the poem)
So we’ll just label them as follows:

SUBJECT A is a 16-year-old black man with a broken lisp.

At age 12, sirens blared his name and six pigs surrounded.

Open palms to back of brown-flesh skull
Legs spread waist-length
See, SUBJECT A fit the description. But not knowing
so, he asked the cop

“What did I do wrong???”
But answered to baton against back of knees,
toppled body
Tooth cracked on concrete

And since then, SUBJECT A hasn’t been able to pronounce his words correctly.

His tongue stumbles over words with the “s” sound helplessly.

Words like “strength.” And ”soul.” And “happiness.”

So no one takes SUBJECT A seriously when he speaks. But not like anyone ever really did.

SUBJECT B is a 43-year-old Korean man (and I think you know where this is going)

The scent of freedom was strong enough to coax a family of 3 across the Pacific. But now SUBJECT B sells bubble gum and beer in a corner store in Watts. He hands people change through a bullet-proof face.

Folks always wonder why Mr. Subject B won’t smile.

But after 17 years of wiping down the same dingy iron-bar window, there’s just not much to be happy about. But hey, he can’t complain.

He sells enough Coca-Colas to pay the rent. And he sells enough lottery tickets to put food on the table.

His 18-YEAR-OLD-SON has been helping him out for the past 12 years, stocking liquor bottles in refrigerated cases. Ever since he was forced into this dust-ridden store. SUBJECT B has been dreaming of rice terraces that his eyes won’t ever kiss again. Dreaming of the home village where his name meant something. But like I said we’re not paying attention to names this time.

***** Today the sky cringes with smog and brokenness. Rusty copper bells rattle as SUBJECT A enters the store. It’s hot, so he grabs a Coke and a Snickers bar for his girl. (It isn’t the fanciest anniversary present, but he’s adding a home-made slow jams mixtape so the gift will have some character.)

SUBJECT B watches him from the counter. Despite the fact that he recognizes every Black face that enters the store, he can’t help but be nervous.

Because of the taunts. Because of the anger.

Because of the BLACK FISTS that picketed his store 2 weeks back, when the Black-owned store 2 blocks down closed. “THESE DAMNED KOREANS NEED TO GET OUT OF OUR NEIGHBORHOODS!”

His ears echo their cries that swore that these rallies were fueled by a love that these foreign exploiters can’t feel. But SUBJECT B gave up his home so his son could eat a hot meal. SO if that’s not love, then what is?

SUBJECT A has been standing there for a while now.

SUBJECT B scrambles for the words but he just can’t piece them together. He doesn’t mean to be rude, but it’s the only English mood that he’s ever been taught.

SUBJECT B: Buy now or get out! Buy now or get out!

SUBJECT A doesn’t want to hear it. He’s been labeled as a thug inappropriately one too many times. Their eyes touch once.

SUBJECT A: What’s your problem, man?????

SUBJECT A is pissed.

SUBJECT B is scared.

SUBJECT A steps forward.

SUBJECT B grabs the nine from behind the counter – DEAD AIM ON BLACK MAN.

SUBJECT B (gun cocked back, sweat drips, fist shakes): Get out now!

But SUBJECT A has never been one to punk out like that.

SUBJECT A (takes another step forward): I have money, see? I have money, see??

But both can’t understand the words coming out of the other’s mouth.

2 subjects
2 speech impediments
Struggling over 1 language
Demonstrating 500 years of socialization.

Shouts continue, sirens approach. With all the
commotion, SUBJECT B’s 18-YEAR-OLD-SON bursts
in through the back, gun in hand --
DEAD AIM ON BLACK MAN.

Shouts continue
Sirens approach
18-year old son
Gun in hand
Shouts continue
Sirens approach
18-year old son
Gun in hand
. . . TWO SHOTS FIRED

But SUBJECT A is thinking 2 seconds ahead.

He jumps aside and SUBJECT B takes 2 bullets to the chest.

Dead silence.

Sirens approach.

18-year-old-son.

Gun in hand.

Dead silence.

Sirens approach.

Rusty copper bells PIGS enter. OLD KOREAN MAN down. BLACK MAN standing. 6 shots fired. BLACK MAN down.

Red and blue spotlights. Cameras in the sky. Another story of Black and Asian conflict. Tonight, the sky bleeds of distortion. The news will paint a picture of it. The 2 SUBJECTS will be replaced. The scene will play again.

This is the Watts Experiment. Thank you for watching.
```

---

## IC-1731: We Rise, We Resist, We

- Title: We Rise, We Resist, We
- Author (byline): Not specified
- Work: Not specified
- Publisher: Crown Books for Young Readers
- Publication date as stated: Sept 2018
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 871
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wade and Cheryl Willis Hudson (eds)
ISBN: 978-0525580423
Publisher: Crown Books for Young Readers
Date (Month/Year): Sept 2018
```

### Introduction (context only: never use it for content warnings)

```text
Hope is what remains when the lights go out and the levees break, when institutions crumble, when all the exits are blocked and we become lost children waiting for a savior who may never come. Hope is what whispers

(whisper) “things can change.” Something better is waiting if we just have the courage to hold on.

It is hard not to cling to hope these days, to wish for a world that feels safer, fairer and kinder. We want to believe our actions matter; that we can nudge the world, however slightly, toward more freedom, opportunity, equality, love and joy.

And yet, when we look back at how far we’ve come, it is difficult not to wonder if anything has truly changed. Some days it feels like we are falling back decades, even centuries, into our cruelest and most paranoid past. Do you have hope that things can change?

Poetry from We Rise, We Resist, We Raise our Voices edited by Wade and Cherly Willis Hudson
```

### Performance text (classify this)

```text
Raise our Voices Wade and Cheryl Willis Hudson (eds)

What Shall We Tell You? by Wade Hudson (Pg 4)

What shall we tell you when our world sometimes seems

dark and uninviting?

What shall we tell you when hateful words that wound

and bully are thrown like bricks against a wall, shattering

into debris?

What shall we tell you when respect for others and

treating others as we wish to be treated appear as

yesterday’s borrowed wish?

What shall we tell you when our differences are juggled

like fragile eggs that could be smashed at a moment

impulse?

What shall we tell you? What shall we tell you?

We shall tell you that love, like cream in milk, will rise to

the top and hatred and distrust will be revealed as

imposters.

We shall tell you that peace, desirable like a restful night

after a long day at play, is not far away. Reach for it.

We shall tell you that respect for others, like a delicious

ice cream bar dripping on holding fingers, tastes better

than contempt.

We shall tell you that we love you, all of you! And

because we love you, we will be there to help bring light

to dark places.

We will be there with peace and justice as our weapons

and love as a soothing salve to comfort and embrace.

We shall tell you that because we will be there for you,

always be there for you, it will be all right! It will be all

right!

Drumbeat for Change by Kelly Starling Lyons (Pg 30) This world feels upside down sometimes, like a twisted house of mirrors where

people in charge are bullies,
where protestors of racism are pummeled,
where being who you are can put your life on the line.
What do we do with the worry, the hurt, the rage?

We turn it into something bigger than us. We turn it into change.

Together, we are a mountain no one can destroy.
Having faith doesn’t mean we are fearless.
It means we believe and press on
Toward love.
Toward equality.
Toward a safer, stronger future.
We press on and stay true to what we know is right.

Throughout history, kids like you were right there.
With picket signs and petitions.
With heart and humility.
With bravery and brilliance.
They changed this world for the better.
And you will too.

Tell your story.
To anyone who will listen.
To hear it yourself.
You matter.
You matter.
You. Matter.

The drumbeat of hope will always drown out howls of

hate . . .

When you feel angry or afraid, remember what you hold
inside.
Kindness.
Courage.
Compassion.
The power of people who made a way out of no way.
Who persevered and toppled injustice.

March to that drumbeat of hope.
March and know you are never alone.
Standing up and speaking out,
pressing for justice,
having each other’s backs,
we will create change.

Where are the Good People? by Tameka Fryer Brown
(Pg 56-57)
Life’s not always fair and sometimes it’s scary.
When safe spaces aren’t safe,
when protectors harm us,
when leaders try to lead us toward fear and hate,
there’s nothing fair or reassuring about that.

Maybe it would be helpful to know
these aren’t the first troubling times
our world has seen,
that none has ever lasted forever.

Tyrants rise and fall;
bad guys win, then lose;
evil gets overtaken by good
when good people stand together against it.

Who and where are the good people?

They’re all around us every day
telling truths, seeking justice, persisting.
They are the helpers, the listeners,
the lovers of everyone.

Changemakers – that’s what they’ll call us
tomorrows from now
if you and I fight for fairness starting today.
Do you believe that we can?
I do too. Action is power . . .

A Talkin’-To by Jason Reynolds (Pg 75)
I could tell you all the bad things,
all the bad things that cut and scare
and howl and growl and gnash and
bear teeth, bright and sharp that
glint in the moonlight.

I could tell you all that’s frightening,
all that’s frightening and lurking
and looming and hiding in the brush,
razor-hair pricked up on the back
of something too sly to see.

I could tell you about all the loud things,
all the loud things that scream
and shriek and shred our ability to hear
each other, the beasts behind screens,
Scrolling banners of bully-banter.

I could tell you all the things,
all the things that are trying to tell you
how you should run,
but I am about you above all things,
so I’d rather tell you one thing and one thing only:
Everything bad and frightening and loud
will always hide when you hold your head up,
will always hid when you hold your heart out,
will always sing a shrinking song
when you fly.

Drumbeat for Change by Kelly Starling Lyons (Pg 30) (Refrain) This world feels upside down sometimes, like a twisted house of mirrors where

people in charge are bullies, where protestors of racism are pummeled, where being who you are can put your life on the line. What do we do with the worry, the hurt, the rage? We turn it into something bigger than us. We turn it into change.
```

---

## IC-1732: The Wellfleet Whale

- Title: The Wellfleet Whale
- Author (byline): Stanley Kunitz
- Work: Contemporary American Poetry
- Publisher: Houghton Mifflin Company
- Publication date as stated: March 1991
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 742
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stanley Kunitz
Book: Contemporary American Poetry
ISBN: 978-0395432310
Publisher: Houghton Mifflin Company
Date (Month/Year): March 1991
```

### Introduction (context only: never use it for content warnings)

```text
One day late in the summer of 1968, the Pulitzer Prize-winning poet Stanley Kunitz spotted a magnificent finback whale cavorting through the water near his home on Cape Cod, Massachusetts. During the night, the whale ran aground on the rocky sands, and Kunitz, along with a growing crowd of onlookers, stood vigil as the marooned creature fought for its life. “Finally, on the next morning, while I was about one foot away from it, it opened its eyes and stared at me,” Kunitz recalled in an 1981 interview with the New York Times. “There was an act of recognition. Then it gave a great groan and died.” So moved was Kunitz that he scribbled some thoughts for a future poem in his notebook, but it would be thirteen long years before those thougths crystallized into one of his most admired poems – The Wellfleet Whale by Stanley Kunitz.
```

### Performance text (classify this)

```text
You have your language too, an eerie medley of clicks and hoots and trills, location-notes and love calls, whistles and grunts. Occasionally, it’s like furniture being smashed, or the creaking of a mossy door, sounds that all melt into a liquid song with endless variations, as if to compensate for the vast loneliness of the sea. Sometimes a disembodied voice breaks in, as if from distant reefs, and it’s as much as one can bear to listen to its long mournful cry, a sorrow without name, both more and less than human. It drags across the ear like a record running down.

No wind. No waves. No clouds.
Only the whisper of the tide,
as it withdrew, stroking the shore,
a lazy drift of gulls overhead,
and tiny points of light
bubbling in the channel.
It was the tag-end of summer.
From the harbor’s mouth
you coasted into sight,
flashing news of your advent,
the crescent of your dorsal fin
clipping the diamonded surface.
We cheered at the sign of your greatness
when the black barrel of your head
erupted, ramming the water,
and you flowered for us
in the jet of your spouting.

All the afternoon you swam
tirelessly round the bay,
with such an easy motion,
the slightest downbeat of your tail,
an almost imperceptible
undulation of your flippers,
you seemed like something poured,
not driven; you seemed
to marry grace with power.
And when you bounded into air,
slapping your flukes,
we thrilled to look upon
pure energy incarnate
as nobility of form.
You seemed to ask of us
not sympathy, or love,
or understanding,
but awe and wonder.

That night we watched you
swimming in the moon.
Your back was molten silver.
We guessed your silent passage
by the phosphorescence in your wake.
At dawn we found you stranded on the rocks.

There came a boy and a man
and yet other men running, and two
schoolgirls in yellow halters
and a housewife bedecked
with curlers, and whole families in beach
buggies with assorted yelping dogs.
The tide was almost out.
We could walk around you,
as you heaved deeper into the shoal,
crushed by your own weight,
collapsing into yourself,
your flippers and your flukes
quivering, your blowhole
spasmodically bubbling, roaring.

In the pit of your gaping mouth
You bared your fringe work of baleen,
a thicket of horned bristles.
When the Curator of Mammals
arrived from Boston
to take samples of your blood
you were already oozing from below.
Somebody had carved his initials
in your flank. Hunters of souvenirs
had peeled off strips of your skin,
a membrane thin as paper.
You were blistered and cracked by the sun.
The gulls had been picking at you.
The sound you made was a hoarse and fitful bleating.

What drew us to the magnet of your dying?
You made a bond between us,
the keepers of the nightfall watch,
who gathered in a ring around you,
boozing in the bonfire light.
Toward dawn we shared with you
your hour of desolation,
the huge lingering passion
of your unearthly outcry,
as you swung your blind head
toward us and laboriously opened
a bloodshot, glistening eye,
in which we swam with terror and recognition.

Voyager, chief of the pelagic world,
you brought with you the myth
of another country, dimly remembered,
where flying reptiles
lumbered over the steaming marshes
and trumpeting thunder lizards
wallowed in the reeds.
While empires rose and fell on land,
your nation breasted the open main,
rocked in the consoling rhythm
of the tides. Which ancestor first plunged

head-down through zones of colored twilight
to scour the bottom of the dark?
You ranged the North Atlantic track
from Port-of-Spain to Baffin Bay,
edging between the ice-floes
through the fat of summer,
lob-tailing, breaching, sounding,
grazing in the pastures of the sea
on krill-rich orange plankton
crackling with life.

You prowled down the continental shelf,
guided by the sun and stars
and the taste of alluvial silt
on your way southward
to the warm lagoons,
the tropic of desire,
where the lovers lie belly to belly
in he rub and nuzzle of their sporting;
and you turned, like a god in exile,
out of your wide primeval element,
delivered to the mercy of time.
Master of the whale-roads,
let the white wings of the gulls
spread out their cover.
You have become like us,
disgraced and mortal.
```

---

## IC-1733: What Animals Can Teach Us

- Title: What Animals Can Teach Us
- Author (byline): Maria Mazziotti, Walt Whitman, Mary
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 976
- Already set (do not supply): none

### Source block (context only)

```text
Author: Maria Mazziotti Gillian
Book: Silence is an Empty House
ISBN: 978-1935520894
Publisher: NYQ Books
Date (Month/Year): Sept 2013
Author: Walt Whitman
Book: Song of Myself
ISBN: 978-0486414102
Publisher: Dover Publications
Date (Month/Year): Feb 2001
Author: Mary Oliver
Book: Red Bird, Pg 11
ISBN: 978-0807068939
Publisher: Beacon Press
Date (Month/Year): April 2009
Author: John O’Donohue
Book: To Bless the Space Between Us, Pg 73-74
ISBN: 978-0385522274
Publisher: Doubleday
Date (Month/Year): March 2008
Author: Jacqueline Jaffee
ISBN: On-Line Transcript Only
Publisher: Duke University
Date (Month/Year): July 13, 2020
Website: https://dukeengage.duke.edu/how-pets-teach-
us-empathy-a-poem/
TRANSISTION
Author: Maryalicia Post
ISBN: On-Line Transcript Only
Publisher: Your Daily Poem.com
Date (Month/Year): N/A
Website:
http://www.yourdailypoem.com/listpoem.jsp?poem_id=27
21
```

### Introduction (context only: never use it for content warnings)

```text
This is a difficult time. As we continue our lives in ways we never thought possible – socially distanced, isolated, and coping with a pandemic; as we watch our nation struggle with the racial injustice we have yet to solve, and as conflicts are escalating into wars world-wide, there is a lesson to be learned. A lesson in humanity from a source we consider less than human. A lesson from the animals.

AA Milne once said . . . “Some people talk to animals. Not many listen though. That’s the problem.”

What Animals Can Teach Us – A Collection including poems by Maria Mazziotti, Walt Whitman, Mary Oliver, John O’Donohue, Jacqueline Jaffee and Maryalicia Post
```

### Performance text (classify this)

```text
Oliver, John O’Donohue, Jacqueline

Jaffee and Maryalicia Post

What Animals Teach Us by Maria Mazziotti On the Discovery Channel, I watch a documentary on elephants set in sub-Saharan Africa. The mother has

given
birth to a calf who is weak and unable to stand. Every time
the calf tries . . . her legs fold under her
and her body sinks. The mother keeps trying to help the

calf
to stand, supporting the calf with her trunk . . .
The announcer tells us another smaller elephant who joins
the mother and the calf is the calf’s older sister. She does

not want to leave the mother and the calf alone. This is what

animals teach us about family, these elephants so huge they could crush

us in a minute; they teach us how to care for one another.

The mother is trying repeatedly to get the calf to stand, until finally she

is strong enough . . . to stand alone. Isn’t this what we want for our children, to

carry them and lift them until they are ready to stand on their

own?

I Think I Could Turn And Live With Animals by Walt Whitman

I think I could turn and live with animals, They do not sweat and whine about their condition, They do not lie awake in the dark and weep for their sins, Not one is dissatisfied, not one is demented with the mania

of owning things, Not one kneels to another, nor to his kind that lived

thousands of years ago, Not one is respectable or unhappy over the whole earth.

Straight Talk from a Fox by Mary Oliver

Listen says fox it is music to run
over the hills to lick
dew from the leaves to nose along
the edges of the ponds to smell the fat
ducks in their bright feathers but
far out, safe in their rafts of sleep.

It is music to wander the black back roads
outside of town no one awake or wondering
if anything miraculous is ever going to
happen, totally dumb to the fact of every
moment’s miracle.

Don’t think I haven’t
peeked into windows. I see you in all your seasons,
arguing, talking about God
as if he were an idea instead of the grass,
instead of the stars. . .

What I am, and I know it, is responsible, joyful, thankful. I would not give my life for a thousand of yours.

To Learn From Animal Being by John O’Donohue

Nearer to the earth's heart,
Deeper within its silence:
Animals know this world
In a way we never will.
We who are ever
Distanced and distracted
By the parade of bright
Windows thought opens:
Their seamless presence
Is not fractured thus.
Stranded between time
Gone and time emerging,
We manage seldom
To be where we are:
Whereas they are always
Looking out from
The here and now.
May we learn to return
And rest in the beauty
Of animal being,
Learn to lean low,
Leave our locked minds,
And with freed senses
Feel the earth
Breathing with us.
May we enter
Into lightness of spirit,
And slip frequently into
The feel of the wild.
Let the clear silence
Of our animal being
Cleanse our hearts
Of corrosive words.

May we learn to walk Upon the earth With all their confidence And clear-eyed stillness So that our minds Might be baptized In the name of the wind And the light and the rain.

How Pets Teach Us Empathy by Jacqueline Jaffee

Perspective is everything
Our perspective defines our worldview
The way we were raised
The way we have been taught to see others.

Perspectives for some are stagnant
Even if they don’t make sense
They remain the same
Because of a refusal to listen.

Perspectives for others are fluid
For the open-minded, limits are boundless
Liberating
Insightful.

Human connection has long been
Something celebrated, something that is needed
At the core of humanity, and yet
It’s still a profound obstacle in society.

How do we overcome this barrier?
This relentless cycle of division?
Of exclusivity?
How do we foster empathy?

We look to a second source.
We look to the companions that
Have been our friends for centuries
That have brought out the qualities that make us human.

When we welcome pets into
Our private space, our home
We learn kindness
We learn to care for someone else.

When we give our pets food
Water and toys
A bed to sleep in
We learn to be attentive to someone else’s needs.

When we give our pets love
Cuddle them when it storms
Scratch that spot just behind the ear
We learn compassion.

A pet teaches us so much
Morality, the way we want to be treated
The way we should treat others
And the relationships that spring from reciprocated love.

If we could all
Open our hearts to each other
In the same way we open our hearts to pets
The world may be a little brighter.
If we could
Listen, respect one another
Love one another, uplift one another
Empathy can become second nature.

“Some people talk to animals. Not many listen though. That’s the problem.”

And so I vow to listen – to listen and make the following commitment . . . won’t you join me? I will . . .

Life Lessons from My Dog by Maryalicia
Post
Greet each morning like a welcome surprise,
each family member as if they lite up my world
Delight in what I have to eat, in the freedom to walk
and if confined to old paths
sniff out something interesting each day
If it’s bright, relax in a patch of sunlight
If it’s dark, curl up in my favourite chair
Yawn and stretch when it suits me
Bark only when necessary
Be happy for a pat on the back and a soft word
Don't think about yesterday
or tomorrow
Give love and watch it come back
```

---

## IC-1734: What Shall I Tell My Children About Atlanta?

- Title: What Shall I Tell My Children About Atlanta?
- Author (byline): Ntozake Shange, Langston
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1217
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ntozake Shange
Book: The Aunt Lute Anthology of U. S. Women Writers,
Vol. 2: The 20th Century (eds Lisa M. Hogeland
and Shay Brown) Pgs 1076-1078
ISBN: 978-1879960770
Publisher: Aunt Lute Books; Vol 2 edition
Date (Month/Year): Oct 2007
Author: Langston Hughes
Book: The Collected Works of Langston Hughes,
Volume 1 (1921-1940), Pg 138+
ISBN: 978-0826213396
Publisher: University of Missouri Press
Date (Month/Year): 2001
Author: Margaret Burroughs
On-Line Transcript:
https://www.poetryfoundation.org/poems/146263/what-
shall-i-tell-my-children-who-are-black-reflections-of-an-
african-american-mother
Publisher: Poetry Foundation
Date (Month/Year): Originally Written in 1963
2003 National Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
What do you think of when I say Atlanta, Georgia? Gone with the Wind . . . peaches . . . beautiful plantation mansions? Atlanta has a rich history – but it wasn’t always peaches and plantations.

Today, I want to take you back to Atlanta in the early 1980’s. Between 1979 and 1981, at least 28 poor, black children vanished from Atlanta's streets, their bodies turning up days or weeks later — strangled, asphyxiated, shot, bludgeoned, stabbed. Most of the child murders remain unsolved. Why?

What Shall I Tell My Children About Atlanta? – A Collection by Ntozake Shange, Langston Hughes and Margaret Burroughs
```

### Performance text (classify this)

```text
Hughes and Margaret Burroughs

About Atlanta by Ntozake Shange

(Pgs 1076-1078) Cuz he’s black & poor
he’s disappeared
the name waz lost the games werent played
nobody tucks him in at night/ wipes traces
of cornbread & syrup from his fingers
the corners of his mouth
cuz he’s black & poor / he’s not
just gone
disappeared one day
& his blood soaks up what’s awready red
in atlanta

no ropes this time no tar & feathers werent no parades of sheets fires & crosses nothing/ no signs

empty bunkbeds
mothers who forget & cook too much on Sundays
just gone / disappeared
cuz he’s black & poor he’s gone
took a bus / never heard from again
but somebody heard a child screaming

& went right on ahead children disappearing / somewhere in the woods /

decaying just gone / disappeared / in atlanta

mothers are always at the window watching caint nobody disappear right in fronta yr eyes but who knows what we cd do when we’re black & poor we aint here no way / how cd we disappear? who wd hear us screaming?

say it was a man with a badge & some candy say it was a man with a badge & some money say it was a maniac cd be more n sticks n stones gotta be more than stars n stripes children caint play war when they in one. caint make believe they dyin/when they are caint imagine what they’ll be / cuz they wont just gone / disappeared

oh mary dont you weep & dont you moan oh mary dont you weep & dont you moan HOLLAR i say HOLLAR cuz we black & poor & we just disappear

we cant find em jesus cant find em til they seepin in soil father reekin in soil they bones bout disappeared they lives aint never been bleeding where the earth’s awready red dyin cuz they took a bus & mama caint see that far out her window the front porch dont go from here to eternity & they gone just disappeared

but somebody heard them screaming
somebody crushed them children’s bones
somebody’s walkin who shd be crawling
for killing who aint never been
cuz we black & poor / we just be gone

no matter how sweet/ no matter how quiet
just gone
be right back ma
going to the store mother dear
see ya later nana

& the soil runs red with our dead in atlanta
cuz somebody went right on ahead
crushing them lil bones / strangling them frail wails
cuz we black & poor
our blook soaks up dirt
while we disappearing

mamas keep looking out the door saying “i wonder where is my child / i wonder

where is my child”
she don’t turn the bed back cuz she knows
we black & poor
& we just disappear / be gone

oh mary dont you weep & dont you moan
oh mary dont you weep & dont you moan
i wonder where is my child
i wonder where is my child
nothing / no signs
in atlanta

TRANSITION

For generations, Black Americans have been operating under an inherited suspicion that no one will care if the worst happens to them. If 28 white children were murdered in Atlanta, would the police response have been the same? Would the response today be different? Do Black lives matter? – Yes. Do Poor lives matter? - Yes. The hard question is: To what degree? Kids Who Die by Langston Hughes Kids Who Die by Langston Hughes (Pg 138) This is for the kids who die, Black and white, For kids will die certainly. The old and rich will live on awhile, As always, Eating blood and gold, Letting kids die.

Kids will die in the swamps of Mississippi
Organizing sharecroppers.
Kids will die in the streets of Chicago
Organizing workers.
Kids will die in the orange groves of California
Telling others to get together.
Whites and Filipinos,
Negroes and Mexicans,
All kinds of kids will die
Who don’t believe in lies, and bribes, and contentment
And a lousy peace.

Of course, the wise and the learned
Who pen editorials in the papers,
And the gentlemen with Dr. in front of their names.
White and black,
Who make surveys and write books
Will live on weaving words to smother the kids who die,
And the sleazy courts,
And the bribe-reaching police,
And the blood-loving generals,
And the money-loving preachers
Will all raise their hands against the kids who die,
Beating them with laws and clubs and bayonets and bullets
To frighten the people—
For the kids who die are like iron in the blood of the

people—
And the old and rich don’t want the people
To taste the iron of the kids who die,
Don’t want the people to get wise to their own power,
To believe an Angelo Herndon, or even get together

Listen, kids who die—
Maybe, now, there will be no monument for you
Except in our hearts
Maybe your bodies’ll be lost in a swamp.
Or a prison grave, or the potter’s field,
Or the rivers where you’re drowned like Leibknecht
But the day will come—
You are sure yourselves that it is coming—
When the marching feet of the masses
Will raise for you a living monument of love,
And joy, and laughter,
And black hands and white hands clasped as one,
And a song that reaches the sky—

The song of the life triumphant Through the kids who die.

What Shall I Tell My Children Who Are Black by Margaret Burroughs (Excerpt)

What shall I tell my children who are black
Of what it means to be a captive in this dark skin
What shall I tell my dear one,
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
```

---

## IC-1735: What We’ve Been Taught to

- Title: What We’ve Been Taught to
- Author (byline): Not specified
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1255
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jesse Parent
Online Transcript:
https://artistsofutah.org/15Bytes/sunday-blog-read-jesse-
parent/
Publisher: Artists of Utah.org
Date (Month/Year): Utah Arts Magazine, Jan 24, 2016
Author: Danez Smith
Chap Book: hands on ya knees
ISBN: N/A
Publisher: Penmanship Books
Date (Month/Year): 2013
Author: Crystal Valentine
Online Transcript:
https://anthology.getlituniverse.org/poemdetail/267/
Publisher: Get Lit Universe.org
Date (Month/Year): Mar 2016
Performed the 2016 Women of the World Poetry Slam,
Pratt Institute Campus, 200 Willoughby Ave, Brooklyn
NY 11205 (March 9-12, 2016)
```

### Introduction (context only: never use it for content warnings)

```text
Through satire, reclamation, and sharp critique, these poems challenge the long-standing portrayal of a white Jesus, exposing how faith has been shaped by power, culture, and control.

What begins as humor quickly turns into a reckoning. Layers of history, like the Shroud of Turin, are peeled back to reveal a figure rooted not in European imagery, but in a brown body born of an oppressed people.

This is a collection about identity, distortion, and the consequences of rewriting religious history. It asks us to reconsider what we’ve been taught to see . . . and what it has cost us not to question it.

What We’ve Been Taught to See – A Collection with poems by Jesse Parent, Danez Smith and Crystal Valentine
```

### Performance text (classify this)

```text
See – A Collection with poems by Jesse Parent, Danez Smith and Crystal Valentine

White Jesus

(with a pronounced European accent) Hey, everybody!
It’s-a me – White Jesus!
I’ve come to break baguettes
and share some cab sav with some
of my favorite sinners!
You guys!

I know what you’re thinking, “Hey, White Jesus, what’s with that crazy accent?” Well, just like the rest of White Jesus, it’s vaguely European and depends on your frame of reference. After all, God may have created us all in His image but White Jesus gets created in the image of those who are trying to make a sale!

I mean, who doesn’t have a nice painting
of White Jesus in their homes?
Or a nice little sculpture
of yours truly with some lambs,
or maybe me as a baby in a manger
with White Mary and White Joseph
and White Angels and White Shepherds
and some vaguely non-white Wise Men?
I mean they had to travel a long way
into the lands of Caucasia to bring me all
these smelly gifts.

White Jesus just works better as a present
when he looks like the rest of the family.
Didn’t your Grandmother say she
tracked your genealogy back to the
House of David?
Just like White Jesus, lineage is important!
Watch as I get nailed to your family tree
and you wash me white, root and stem,
and slake my thirst with a sponge
soaked in vinegar wine
to sour my history.
Trade my sandals for Birkenstocks,
my coiled hair for long auburn locks,
my rough linen for white sheets,
I mean, who doesn’t love wearing white sheets?

Just like your family tree
I’m a self portrait
of poor white Renaissance guys
who can only afford a mirror for a model.

Can you imagine how great it has to feel to get a whole religion to worship your image? Carve all my sculptures from marble or alabaster, Make me as White as Sushi Burrito or Great Harvest flatbread.

Let anyone who doesn’t look like White Jesus know that no matter how Christ-like they live their lives they will never look like salvation. Tell them about the blackness of their souls. How much can that weigh someone down? Gesture at all the stained glass and tell them how beautiful the light looks coming through my creamy complexion. Twist up any Bible verse you need to justify my supremacy. Tell them the Mark of Cain is their dark skin color. Show them all the paintings of white Adam and Eve as proof of your flesh’s primacy. I am the Exodus from Egypt. This is what Palestine probably looks like, right? No refugee ever looked like me.

Keep citing the fact of scripture and the evidence of illustrations.

Now look at-a me, again!
White Jesus!
Doesn’t my accent seem so much less crazy
in comparison to the rest of me?

Black Jesus Writes a Letter to White Jesus Hi, you might not know who I am, but my name is Jesus. Jesus Christ of Nazareth

of Mary

of God

Son of God
Born in a brown wooden manger.
Born with my mother's eyes --
My mother's brown eyes

with skin of bronze (that means brown)

with hair of wool (that means nappy)

My name is Jesus.
Jesus, whose Father begat the world
Whose mother begat him
Without the seed of an Earthly man
Whose father planted the last seed of Eden inside a girl
Who hadn't been entered yet
Like a temple whose husband
Hadn't cried out for God in there yet.
Yeah, that Jesus!
How you is?

See I've heard a rumor . . . I've heard you’ve been walking around bearing my cross. I've seen the pictures

eyes blue as a man that dies and stays dead

skin white as his bone once the flesh cascades off

hair – long, blonde and straight as the people that pierce spear and nail into the light of

this world . . . Me What kind of martyr are you? I died for this planet. You died for a chance to plaster the face of Europe (the land that destroyed it) on the body that saved it. My blood did not run so it could be bleached away. I'm the stain of Heaven on everyone's soul.

God's son -- Water Runner -- Healer Much realer than you could ever be.

The scapegoat.

The original black sheep.

Most popular Lynch victim of all time My color is no coincidence . . . I had to be black to save you all from your own

darkness. When I rose up, it was never meant for anybody to lie in

my place.

So you tell me . . . When you saw the rock moved, Did you wait at the mouth of the cave for the painter to

show up?

Did you find all the pictures of me and smear them with

glue? When your people conquered the world in my father's

name (without asking),
Did you cover me in the hide of some dead King
to hide the ugly secret of your savior
underneath the flesh of the one that you really worship?

Jesus, if we can call you that, I'm simply asking you to rub the white out off all those pictures of you.

Show them the me underneath all that.

Show them that the world was born and reborn

in the body of the darkest continent.

Show them that salvation don't always come. In the light, correct yourself or be your own Messiah. Pass on, then tell your cold flesh to resurrect Then you can walk in my soul.

I did not die so that you could die

--Me (Black Jesus)

Performed at First Slam of 2012

The Artists' Quarter 408 St. Peter Street, St. Paul, MN

55102; Jan 2012

Transcript can be found online at https://www.youtube.com/watch?v=0kPYg6oufgQ

And the News Reporter says “Jesus is White”
She says it with a smile
Like it’s the most obvious thing in the world
So sure of herself
Of her privilege
Her ability to change history
Rewrite bodies to make them look like her

She says it the same way politicians say racism no longer exists The same way police officers call dead Black boys thugs The same way white gentrifiers call Brooklyn home

She says it with an American accent
Her voice doing that American thing
Crawling out of her throat
Reaching to clasp onto something
That does not belong to her

I laugh to myself

What makes a Black man a Black man?
Is it a white woman’s confirmation?
Is it her head nod?
Is it the way she’s allowed to go on national television
And auto correct the Bible and God himself,
Tell him who his son really was?

What makes a black man a black man:
The way reporters retell their deaths like fairytales
The way their skulls split across pavement
The way they cannot outrun a bullet
The way they cannot inherit privilege

How can she say Jesus was a white man when he died the blackest way possible?

With his hands up
With his mother watching,
Crying at his feet
Her tears nothing more than gossip
for the news reporters or prophets to document
With his body left to sour in the sun
With his human stripped from his Black

Remember that?
How the whole world was saved by a Black man
By a man so loved by God,
He called him kin
He called him Black

Now ain’t that suspicious? Ain’t that news worthy? Ain't that something worth being killed over?

*written in response to Fox News host Megyn Kelly’s 2013 declaration that Jesus was a white man.
```

---

## IC-1736: When the Bough Breaks, Dive

- Title: When the Bough Breaks, Dive
- Author (byline): Andrea Gibson
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1005
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andrea Gibson
Book: Pole Dancing to Gospel Hymns, Pg 82-84
ISBN: 978-0981521305
Publisher: Write Bloody Publishing
Date (Month/Year): June 2008
Author: Andrea Gibson
Book: Pole Dancing to Gospel Hymns, Pg 46-48
ISBN: 978-0981521305
Publisher: Write Bloody Publishing
Date (Month/Year): June 2008
```

### Introduction (context only: never use it for content warnings)

```text
Every day, the suffering of so many is brought home to us through TV and social media: A thirteen-year-old girl dies of leukemia. Brown-skinned families flee for their lives, seeking asylum in countries who refuse them entry.

Teachers use their bodies as human shields to protect students from another school shooting. A tsunami kills thousands of unsuspecting vacationers. Palestinian children kneel in the cinders of missile heads. How do we continue to take in the tragedy surrounding us without giving up all sense of hope? Andrea Gibson in her poems “When the Bough Breaks” and “Dive” gives us a unique perspective of coping when life doesn’t rhyme.
```

### Performance text (classify this)

```text
Dive
(Pg 46-48) Life doesn't rhyme.
It's bullets. . . and wind chimes.
It's lynchings. . . and birthday parties.
It's the rope that ties the noose
and the rope that hangs the backyard swing.

It's wanting tonight to speak the most honest poem I've ever spoken in my life not knowing if that poem should bring you closer to living or dying.

When the Bough Breaks (Pg 82-84) . . . I’m standing in an auditorium behind a

microphone
reading a poem to four hundred Latino high school kids
who live with the breath of the INS
crawling up their mothers’ backbones
and I am frantically hiding my scars
‘cause the last thing I want these kids to know
is that I ever thought that my life was too hard.

I’ve never seen a bomb drop.
I’ve never felt hunger.
I’ve also never seen lightning strike
but I know we’ve all heard the thunder
and it doesn’t take a genius to tell something’s burning.

“Please call me by my true name,
I am the child in Uganda all skin and bone.”
Do we remember the rest?
And, “Jesus Wept.”
Jesus wept, but look at our eyes,
dry as the desert sand
dusting the edges of our soldier’s wedding bands.

Do you know children in Palestine fly kites
to prove they’re still free?
Can you imagine how that string
must feel between their fingers
as they kneel in the cinders of US-made missile heads?
You can count the dead by the colors in the sky.

The bough is breaking. The cradle is falling. Right now a six-year-old girl is crouched in a ditch in

Lebanon wishing on falling bombs.

Right now our government is recording the test scores of Black and Latino 4th graders to see how many prison beds will be needed in the year 20**.

Right now there’s a man on the street outside my door with outstretched hands full of heartbeats no one can hear. He has cheeks like torn sheet music, every tear-broken crescendo falling on deaf ears. At his side there’s a boy with eyes like an anthem no one stands up for.

Our insanity is not that we see people who aren’t there.
It’s that we ignore the ones who are.
‘Til we find ourselves scarred and ashamed
walking into emergency rooms at two am
flooded with a pain we cannot name or explain,
bleeding from the outside in.
Our skin is not impervious.

Cultures built on greed and destruction do not pick and choose who they kill.

Do we really believe our need for Prozac has nothing to do with Fallujah, with Kabul, with the Mexican border with the thousands of US school kids bleeding budget cuts that will never heal to fuel war tanks?

Thank god for denial.
Thank god we can afford the makeup
to pile upon the face of it all.
Look at the pretty world.
Look at all the smiling people,
and the sky with a missile between her teeth
and a steeple through her heart
and not a single star left to hold her

and the voices of a thousand broken nations saying, “Wake me, wake me when the American dream is over.”

Combined with Anything by Andrea Gibson

Dive (con’t) (Pg 46-48) Last night I prayed myself to sleep, woke this morning to find god's obituary scrolled in tears on my sheets then walked outside to hear my neighbor erasing ten thousand years of hard labor with a single note of his violin and the sound of the traffic rang like a hymn as the holiest leaf of autumn fell from a plastic tree limb, beautiful and ugly.

Like right now I'm needing nothing more than for you to

hug me
and if you do I'm gonna scream like a caged bird.
Life doesn't rhyme.
Sometimes love is a vulgar word.

I've heard saints preaching truths that would have burned me at the stake. I've heard poets telling lies that made me believe in

heaven.

Sometimes i imagine Hitler at seven years old, a paint brush in his hand at school thinking, “What color should i paint my soul?”

Sometimes I remember myself
with track marks on my tongue
from shooting up convictions
that would have hung innocent men from trees.

Have you ever seen a mother falling to her knees
the day her son dies in a war she voted for?
Can you imagine how many gay teen-aged lives were saved
the day Matthew Shepherd died?
Could there have been anything louder
than the noise inside his father's head
when he begged the jury, “Please don't take the lives
of the men who turned my son's skull to powder.”
And I know nothing would make my family prouder
than if I gave up everything I believe in
but nothing keeps me believing
like the sound of my mother breathing.
Life doesn't rhyme.
It's tasting your rapist's breath
on the neck of a woman who loves you more
than anyone has loved you before
then feeling holy as Mary
beneath the hands of a one-night stand
who's calling somebody else's name.

It's you never feeling more greedy than when you're handing out dollars to the needy.

It's my not eating meat for the last ten years then seeing the kindest eyes I've ever seen in my life on the face of a man with a branding iron in his hand and a beat-down baby calf wailing at his feet.

It's choking on your beliefs.
It's your worst sin saving your life.
It's the devil's knife carving holes into your soul
so angels will have a place to make their way inside.
Life doesn't rhyme.
Life is poetry, not math.
All the world's a stage
but the stage is a meditation mat.
You tilt your head back.
You breathe.
When your heart is broken you plant seeds in the cracks
and you pray for rain.
And you teach your sons and daughters
there are sharks in the water
but the only way to survive
is to breathe deep
and dive.
```

---

## IC-1737: When the Towers Fell

- Title: When the Towers Fell
- Author (byline): Galway Kinnell
- Work: The Best American Poetry 2003
- Publisher: Scribner Poetry
- Publication date as stated: Aug 2003
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1193
- Already set (do not supply): none

### Source block (context only)

```text
Author: Galway Kinnell
Book: The Best American Poetry 2003
ISBN: 978-0743203876
Publisher: Scribner Poetry
Date (Month/Year): Aug 2003
```

### Introduction (context only: never use it for content warnings)

```text
September 11, 2001. On that morning, Nineteen Islamist terrorists affiliated with al-Qaeda hijacked four commercial passenger jet airliners. The hijackers intentionally crashed two of the airliners into the Twin Towers of the World Trade Center in New York City, killing everyone on board and many others working in the building. Both buildings collapsed within two hours, destroying at least two nearby buildings and damaging others. The hijackers crashed a third airliner into the Pentagon. The fourth plane crashed into a field near Shanksville in rural Somerset County, Pennsylvania, after some of its passengers and flight crew attempted to retake control of the plane, which the hijackers had redirected toward Washington, D.C. There are no survivors from any of the flights. Excluding the 19 hijackers, 2,974 people died in the attacks. The overwhelming majority of casualties were civilians, including nationals of over 90 different countries.

When the Towers Fell by Galway Kinnell
```

### Performance text (classify this)

```text
From our high window we saw the towers with their bands and blocks of light brighten against a fading sunset, saw them at any hour glitter and live as if the spirits inside them sat up all night calculating profit and loss, saw them reach up to steep their tops in the until then invisible yellow of sunrise, grew so used to them often we didn’t see them, and now, not seeing them, we see them.

The banker is talking to London.
Humberto is delivering breakfast sandwiches.
The trader is already working the phone.
The mail sorter has started sorting the mail.

...povres et riches

...poor and rich
Sages et folz, prestres et laiz
Wise and foolish, priests and laymen
Nobles, villains, larges et chiches
Noblemen, serfs, generous and small
Petiz et grans et beaulx et laiz
Short and tall and handsome and homely

The plane screamed low down lower Fifth Avenue lifted at the Arch, someone said, shaking the dog walkers in Washington Square Park, drove for the north tower, struck with a heavy thud, releasing a huge bright gush of blackened fire, and vanished, leaving a hole the size and shape a cartoon plane might make if it had passed harmlessly through and were flying away now, on the far side, back into the realm of the imaginary.

Some with torn clothing, some bloodied,
some limping at top speed like children
in a three-legged race, some half dragged,
some intact in neat suits and dresses,
they straggle out of step up the avenues,
each dusted to a ghostly whiteness,
their eyes rubbed red as the eyes of a Zahoris,
who can see the dead under the ground.

Some died while calling home to say they were O.K. Some died after over an hour spent learning they would die. Some died so abruptly they may have seen death from within it. Some broke windows and leaned out and waited for rescue. Some were asphyxiated. Some burned, their very faces caught fire. Some fell, letting gravity speed them through their long moment. Some leapt hand in hand, the elasticity in last bits of love-time letting — I wish

I could say — their vertical streaks down the sky happen more lightly.

At the high window, where I’ve often stood
to escape a nightmare, I meet
the single, unblinking eye
lighting the all-night sniffing and lifting
and sifting for bodies, pieces of bodies, anything that is not
nothing,
in a search that always goes on
somewhere, now in New York and Kabul.

She stands on a corner holding up a picture
of her husband. He is smiling. In today’s
wind shift few pass. Sorry sorry sorry.
She startles. Suppose, down the street, that headlong
lope...
or, over there, that hair so black it’s purple...
And yet, suppose some evening I forgot
The fare and transfer, yet got by that way
Without recall — lost yet poised in traffic.
Then I might find your eyes...
It could happen. Sorry sorry good luck thank you.
On this side it is “amnesia,” or forgetting the way home,
on the other, “invisibleness,” or never in body returning.
Hard to see clearly in the metallic mist,
or through the sheet of mock reality
cast over our world, bourne that no creature ever born
pokes its way back through, and no love can tear.

The towers burn and fall, burn and fall — in a distant, shot, smokestacks spewing oily earth remnants out of the past. Schwarze Milch der Fruhe wir trinken sie abends Black milk of daybreak we drink it at nightfall wir trinken sie mittags und morgens wir trinken sie nachts we drink it at midday at morning we drink it at night wir trinken und trinken We drink it and drink it This is not a comparison but a corollary, not a likeness but a lineage in the twentieth-century history of violent death — black men in the South castrated and strung up from trees, soldiers advancing through mud at ninety thousand dead per mile, train upon train headed eastward made up of boxcars shoved full to the

corners with Jews and Gypsies to be enslaved or gassed, state murder of twenty, thirty, forty million of its own, atomic blasts wiping cities off the earth, firebombings the same, death marches, starvations, assassinations, disappearances, entire countries turned into rubble, minefields, mass graves. Seeing the towers vomit these black omens, that the last century dumped into

this one, for us to dispose of, we know they are our futures, that is our own black milk crossing the sky:

wir shaufeln ein Grab in den Luften da liegt man nicht eng

we’re digging a grave in the sky there’ll be plenty of room to lie down there

Burst jet fuel, incinerated aluminum, steel fume, crushed marble, exploded

granite, pulverized drywall, mashed concrete, berserked plastic,

gasified mercury, cracked chemicals, scoria, vapor
of the vaporized — wafted here
from the burnings of the past, draped over
our island up to streets regimented
into numbers and letters, breathed across
the great bridges to Brooklyn and the waiting sea:
astringent, miasmic, empyreumatic, slick,
freighted air too foul to take in but we take it in,
too gruesome for seekers of the amnesiac beloved
to breathe but they breathe it and you breathe it.

A photograph of a woman hangs from a string
at his neck. He doesn’t look up.
He stares down at the sidewalk of flagstone
slabs laid down in Whitman’s century, gutter edges
rasped by iron wheels to a melted roundedness:
a conscious intelligence envying the stones.
Nie staja sie, sa.
They do not become, they are.
Nie nad to, myslalem.
Nothing but that, I thought,
zbrzydziwszy sobie
now loathing within myself
wszystko co staje sie
everything that becomes.

And I sat down by the waters of the Hudson,
by the North Cove Yacht Harbor, and thought
how those on the high floors must have suffered: knowing
they would burn alive, and then, burning alive.
and I wondered, Is there a mechanism of death
that so mutilates existence no one
gets over it not even the dead?
Before me I saw, in steel letters welded
to the steel railing posts, Whitman’s words
written as America plunged into war with itself: City of the
world!...
Proud and passionate city — mettlesome, mad, extravagant
city!
words of a time of illusions. Then I remembered
what he wrote after the war was over and Lincoln dead:
I saw the debris and debris of all the dead soldiers of the
war,
But I saw they were not as was thought.
They themselves were fully at rest — they suffer’d not,
The living remain’d and suffer’d, the mother suffer’d
And the wife and the child and the musing comrade
suffer’d...

In our minds the glassy blocks succumb over and over into themselves, slam down floor by floor into themselves.

They blow up as if in reverse, exploding downward and outward, billowing through the streets, engulfing the fleeing.

As each tower goes down, it concentrates into itself, transforms itself infinitely slowly into a black hole

infinitesimally small: mass without space, where each light, each life, put out, lies down within us.
```

---

## IC-1738: When We Come to It, We Must Do Something

- Title: When We Come to It, We Must Do Something
- Author (byline): Maya Angelou, Neil Hilborn and Rudy Francisco
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1473
- Already set (do not supply): none

### Source block (context only)

```text
Author: Maya Angelou
Book: The Complete Poetry of Maya Angelou, Pg 218-219
ISBN: 978-0812997873
Publisher: Random House
Date (Month/Year): March 2015
Author: Maya Angelou
Book: The Complete Poetry of Maya Angelou, Pg 269-271
ISBN: 978-0812997873
Publisher: Random House
Date (Month/Year): March 2015
Author: Neil Hilborn
ISBN: On-Line Transcript
https://everythingandnothingdotin.wordpress.com/2018/04/
02/this-is-not-the-end-of-the-world-by-neil-hilborn/
Publisher: WordPress.com
Date (Month/Year): April 2, 2018
Author: Rudy Francisco
Book: Helium Pg 91-94
ISBN: 978-1943735198
Publisher: Button Poetry
Date (Month/Year): Nov 2017
```

### Introduction (context only: never use it for content warnings)

```text
I watch the news. I hear the stories of the homeless, the migrants fleeing war-torn countries, the women fighting once again for equal rights. And I feel sad. And angry. And hopeless. But feeling is only one step.

The ability to connect empathically with others—to feel with them, to care about their well-being, and to act with compassion—is critical to our lives, helping us to get along, work more effectively, and thrive as a society. Once empathy is activated, compassionate action is the most logical response.

When We Come to It, We Must Do Something – A Collection of poetry by Maya Angelou, Neil Hilborn and Rudy
```

### Performance text (classify this)

```text
Human Family by Maya Angelou (Pg 218-219)

I note the obvious differences
in the human family.
Some of us are serious,
some thrive on comedy.

Some declare their lives are lived
as true profundity,
and others claim they really live
the real reality.

The variety of our skin tones
can confuse, bemuse, delight,
brown and pink and beige and purple,
tan and blue and white.

I've sailed upon the seven seas
and stopped in every land,
I've seen the wonders of the world
not yet one common man.

We love and lose in China, we weep on England's moors, and laugh and moan in Guinea, and thrive on Spanish shores.

We seek success in Finland,
are born and die in Maine.
In minor ways we differ,
in major we're the same.

I note the obvious differences between each sort and type, but we are more alike, my friends, than we are unalike.

Francisco.

A Brave and Startling Truth by Maya Angelou (Pg 269-271)

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

When we come to it When the curtain falls on the minstrel show of hate And faces sooted with scorn are scrubbed clean When battlefields and coliseum No longer rake our unique and particular sons and daughters Up with the bruised and bloody grass To lie in identical plots in foreign soil

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
We come to it. “

This is Not the End of the World by Neil Hilborn

I’ve been hearing that the world is ending. I’ve heard it so much these days, I can either completely ignore it or never leave my house again, that is if I actually left my house for things that don’t directly enable me to keep my house.

See, I’ve been thinking about driving nowhere. I’ve been thinking about becoming a box inside a locked room inside a dark house at the dark end of the street.

I want to go away until I’m gone. It takes so much less energy to not exist than it does to exist and get burned. I’ve been burned so much I’m not me anymore, I’m a stupid puppet version of me. I’ve got strings that lead to nowhere, nothing is pulling me. I wish someone would drag my hand out of hiding and sign my name on the dotted line.

There are days that I cannot find the sun even though it’s right outside my goddamn window, when getting out of bed feels like the key in the doomsday machine, so on those days, this is what I tell myself: Whatever you’re feeling right now, there is a mathematical certainty that someone else is feeling that exact same thing. That is not to say you’re not special, this is to say thank god you aren’t special.

I have kissed no one goodnight. I have launched myself from tall places and hoped no one would catch me. I have ended relationships because suddenly, I was also exposed.

Isolation is not safety, it is death.
If no one knows you’re alive, you aren’t.
If a tree falls in a forest and no one’s around to hear it, it
does make a sound but then that sound is gone.

I’m not saying you will find the meaning of life in other people, I’m saying other people are the life to which you provide the meaning. See, we’re wrong when we say, “I think therefore I am,” the more we say it, the more it sounds like “I think therefore I will be.”

You cannot think yourself into a full table.
You cannot think and make walls and a roof appear around
you.
I have thought and thought myself into corners made of
words and nightmares.
And what has it gotten me but more thoughts.
A currency that only buys more currency.

So please, if you want to continue existing, do something. Learn to make clouds using only your breath. Build a house even if every wall leans to the left. Love it anyway, just like a season, just like a child. Love how you hate yourself sometimes because, goddamn, at least there’s still something to hate.

I know how easy it is to think and keep thinking until you’re the last person left on earth, until the world becomes no larger than the space between your bed and the light switch.

But I hear the world is ending soon. When we go, and we’re all going to go, I will be part of it.

Complainers by Rudy Francisco (Pg 91-94)

The following are true stories.

May 26th, 2003, Aron Ralston was hiking, a boulder fell on his right hand. He waited four days, then amputated his arm with a pocketknife.

On New Year’s Eve, a woman was bungee jumping in Zimbabwe. The cord broke, she then fell into a river and had to swim back to land in crocodile infested waters with a broken collarbone.

Claire Champlin was smashed in the face by a five-pound watermelon being propelled by a slingshot.

Matthew Brobst was hit by a javelin.

David Striegl was punched in the mouth. By a kangaroo.

The most amazing part about these stories is when asked about the experience they all smiled, shrugged, and said “I guess things could have been worse.”

So go ahead. Tell me that you’re having a bad day. Tell me about the traffic. Tell me about your boss. Tell me about the job you’ve been trying to quit for the past four years. Tell me the morning is just a town house burning to the ground and the snooze button is a fire extinguisher. Tell me the alarm clock stole the keys to your smile, drove it into 7:00 AM, and the crash totaled your happiness.

Tell me! Tell me! Tell me, how blessed are we to have tragedies so small it can fit on the tips of our tongues?

You see, when Evan lost his legs, he was speechless. When my cousin was assaulted, she didn’t speak for forty-eight hours. When my uncle was murdered, we had to send out a search party to find my father’s voice.

Most people have no idea that tragedy and silence have the exact same address.

When your day is a museum of disappointments hanging from events that were outside of your control,

when you find yourself flailing in an ocean of “Why is this happening to me?”

when it feels like your guardian angel put in his two week notice two months ago and just decided not to tell you,

when it feels like God is just a babysitter that’s always on the phone,

when you get punched in the esophagus by a fistful of life,

remember that every year two million people die of dehydration so it doesn’t matter if the glass is half full or half empty, there’s water in the cup.

Drink it and stop complaining.

Muscle is created by repeatedly lifting things that have been designed to weigh us down. So when your shoulders feel heavy, stand up straight and lift your chin – call it exercise.

When the world crumbles around you, you have to look at the wreckage and then build a new one out of the pieces that are still here.

Remember, you are still here.

The human heart beats approximately four thousand times per hour. Each pulse, each throb, each palpitation is a trophy engraved with the words “You are still alive.”

You are still alive. Act like it.
```

---

## IC-1739: Where to Begin

- Title: Where to Begin
- Author (byline): Cleo Wade
- Work: Not specified
- Publisher: Atria Books
- Publication date as stated: Oct 2019
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 915
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cleo Wade
ISBN: 978-1982138790
Publisher: Atria Books
Date (Month/Year): Oct 2019
This poem was originally presented in 2017 as a TedTalk –
the transcript can be found here:
https://www.ted.com/talks/cleo_wade_want_to_change_the
_world_start_by_being_brave_enough_to_care/transcript
```

### Introduction (context only: never use it for content warnings)

```text
Technology. Isn’t it wonderful? We carry smart phones that alert us to the latest details of disease, disaster, and destruction, only one click away!

. . . . from a constant stream of anxiety-inducing information. (beat)

Whatever political beliefs we hold and whatever causes we support; we can all agree that we’re living in a moment of grand-scale uncertainty. For some of us, our feelings are fuel for action. For others, it drives us to seek distraction or escape.

When the state of the world overwhelms you . . . take a moment, take a breath, and make a change.

Where to Begin by Cleo Wade
```

### Performance text (classify this)

```text
The world will say to you,
"Be a better person."
Do not be afraid to say, "Yes."
Start by being a better listener.
Start by being better at walking down the street.
See people.

Say, "Hello."
Ask how they are doing and listen to what they say.
Start by being a better friend,
a better parent, a better child to your parents;
a better sibling, a better partner.
Start by being a better neighbor.
Meet someone you do not know and get to know them.

The world will say to you,
"What are you going to do?"
Do not be afraid to say,
"I know I can't do everything,
but I can do something."
Walk into more rooms saying,
"I'm here to help."
Become intimate with generosity.
Give what you can give and do what you can do.
Give dollars, give cents, give your time,
give your love,
give your heart, give your spirit.
The world will say to you,
"They are the enemy."

Love enough to know
that just because someone disagrees with you,
it does not make them your enemy.
You may not win an argument,
you may not change a mind,
but if you choose to,
you can always achieve the triumph of radical empathy --
an understanding of the heart.

The world will say to you,
"We need justice."
Investigate.
Find truth beyond the stories you are told.
Find truth beyond the way things seem.
Ask, "Why?"
Ask, "Is this fair?"
Ask, "How did we get here?"
Do this with compassion.
See yourself in others.
Recognize that your justice is my justice,
and mine is yours.

The world will say to you,
"I am violent."
Respond by saying,
"I am not.
Not with my words and not with my actions."

The world will say to you,
"We need to heal the planet."
Start by saying, "No, thank you. I don't need a plastic bag."
Recycle, reuse.
Start by picking up one piece of trash on your block.

The world will say to you,
"There are too many problems."
Do not be afraid to be a part of the solutions.
Start by discussing the issues.
We cannot overcome what we ignore.
The more we talk about things,
the more we see that the issues are connected
because we are connected.

The world will say to you,
"There is so much hate."
Devote yourself to love.
Love yourself so much that you can love others
without barriers and without judgment.
When the world asks us big questions that require big
answers,
we have two options.
One: to feel so overwhelmed or unqualified, we do nothing.
Two: to start with one small act and qualify ourselves.

No one nominated Harriet Tubman to her purpose,
to her mission, to her courage.
She did not say, "I'm not a congressman
or the president of the United States,
so how could I possibly participate in the fight to abolish
a system as big as slavery?"
She instead spent 10 years making 19 trips,
freeing 300 people,
one group of people at a time.
Think about the children of those 300 people,
the grandchildren, the great-grandchildren and beyond.

Our righteous acts create immeasurable ripples in the endless river of justice.

Whether it's Hurricane Katrina, Harvey, Irma or Maria,
people did not say,
"There is so much damage. What should I do?"
They got to work on what they could do.
Those with boats got in their boats
and started loading in every woman, man and child they
came across.
We spend so much time
thinking we don't have the power to change the world.
We forget that the power to change someone's life is
always in our hands.
Change-making does not belong to one group of people;
it belongs to all of us.
You don't have to wait on anyone to tell you
that you are in this.
Begin.
We don't have to be heroes,
wear a uniform,
call ourselves activists
or get elected to participate.
We just have to be brave enough to care.

I went to the birthday party of a man named Gene Moretti.
It was his 100th birthday,
which means he lived in the United States through the
Depression, World War II,
the struggle for workers' rights,
the achievement of a woman's right to vote,
the Civil Rights Movement,
a man on the moon, the Vietnam War
and the election of the first black president.
I sat with him, and I said,
"Gene, you have lived in America for 100 years.
Do you have any advice during these current times?"
He smiled and said to me simply, "Yes.
Be good to as many people as possible."
And as he danced with my mother,
in a room full of generations of his family
I realized that he had not just given me advice,
he had given me the first step
that every single one of us is capable of making
if we want to create a real, wholehearted impact
on the world around us, right now.
"Be good to as many people as possible."

CLOSING

So today, I dedicate myself to embody the immortal words of Michael Jackson: (You may choose to sing to speak)

I'm gonna make a change

For once in my life

Gonna make a difference

Gonna make it right

I'm starting with the man in the mirror

I'm asking him to change his ways

If you wanna make the world a better place

Take a look at yourself and then make a change

Won’t you join me?
```

---

## IC-1740: A White Blouse from The Road from Hiroshima

- Title: A White Blouse from The Road from Hiroshima
- Author (byline): Marc Kaminsky
- Work: Not specified
- Publisher: Simon and Schuster
- Publication date as stated: Sept 1984
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1260
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mark Kaminsky
ISBN: 978-0671530556
Publisher: Simon and Schuster
Date (Month/Year): Sept 1984
```

### Introduction (context only: never use it for content warnings)

```text
*On the morning of August 6, 1945, the American B-29 bomber, the Enola Gay, dropped an atomic bomb on the Japanese city of Hiroshima. By that date an estimated 300,000 Japanese civilians had already died from starvation and bombing raids; but Japan’s leaders refused to capitulate.

The bomb exploded directly over a surgical clinic. And although less than 2% of the bomb’s uranium achieved fission, the temperature at ground level reached 7,000 degrees in less than a second. The bomb vaporized people half a mile away, killing 80,000 people instantly.

For Americans the end of World War II appears to be in sight. For the Japanese, the horror was just beginning. This is the story of one of the people who survived the initial blast . . .

A White Blouse from The Road from Hiroshima by Marc Kaminsky
```

### Performance text (classify this)

```text
Questions (Pg 15)

If I shriek
who will hear me . . .
if I speak normal
words in the normal order
Who will hear me
if I make poems
of what I saw and heard on the road
from Hiroshima
will I disturb
the dead
will I
be a merchant of our disaster
if I fail
to work all the horror
into a play
of voices in which the living and the dead
live again
who will forgive me
A White Blouse (Pg 44-55)

1. Not aware
of what I was doing
I jumped
down to the track and braced
myself against it

somebody fell on top of me, screaming
a stream of pebbles lashed my face
trying to scream
my tongue fought an eerie
weight and I couldn’t
hear me

though I lay there shrieking with all my strength

I found
I had stuffed a handkerchief into my mouth
and covered my eyes and ears
with my hands

2. Even now
I can’t remember
how I threw off the bodies that boxed me in
and got to my feet
how I thrust aside
the passengers swarming
against me

how I climbed back onto the platform

I took one step, then another

but they came upon me
like lava they scalded they knocked me
off-balance they carried me
toward the burning cars

I hit against something hard

I threw my arms
around it
wrapped my legs around it
not aware
of what I was doing

I held on
as wave after wave beat against me
smashing my chin
against steel
pulling my arms from their sockets

my whole body racked
and numb
I clung
to that pillar

3. Eventually it was quiet
I tried to open my eyes
I through: Lord
why have you blinded me?
I through: this is happening in a dream

then I saw a light brown haze
obscure everything
a chalky ash
fell through the air
there wasn’t a soul on the platform

4. but their shoes! Hundreds
of shoes, left
and right separated
one from the other, confused
with clogs, strewn
among sandals and slippers
and all overturned
or turning this way
and that, half-buried
under a chaos of
hoods and parasols –

only the shoes and hats, shorn of their people!

like headstones and footstones marking

the mass of disappearance

5. and I the only one left?

6. Black smoke rising
here and there
and Nakahiro-cho where my parents lived
already in flames

apologizing in my heard I turned away from their home to seek shelter.

7. Walls on either side of the road town down stone walls and fences

around each of the houses
demolished
Brick walls, plasterboard, paneling, beams, blackened
window frames, rain doors, silk and gold
hand-painted screens

demolished!

leaving Yokogawa Station I couldn’t make out the road.

8. I walked through what had once been a house

and shreds of someone’s daily routine --
a clock, an ironing board, a photograph
of a sailor carrying a boy on his back --
were visible
under broken roof-tiles

pieces of white blouse and mattress shocked me, hanging from telegraph poles

I cried, “Anyone here?”

just as
I realized I
was together with the dead
woman in her bedroom

only we weren’t really inside the house

all the walls between outside
and inside missing
fire beginning to fan out before me
around me

everywhere was out-of-doors and cemetery

9. bits of sky fluttered into view, were swallowed and spat out elsewhere

light dropped through holes in the whirling cloudcover

and I was not alone

climbing through the remains of a bathroom

a boy clinging to an emergency bucket of sand

I went toward him, I wanted to take his hand

but he shivered away from me hugging his bucket

he must have grabbed it when earth went up in millions of pounds of light

he walked unconsciously
pressing
this weight against him
as if it could keep him
from floating off –

another strand of black smoke

10. And then
the debris was populated
naked
and half-naked men
and women
reeled against me

and a small voice under the wreckage –

only a pair of legs could be seen

but a group formed around the block of concrete that sealed her in

pushing in five different directions we couldn’t move it

“Forgive us,” the others said

but I stayed how long I can’t say, praying with her

“Help me
remove this stone,” I pleaded
as naked
and half-naked men
and women
collided and sank
amid the debris

then I too went away

11. One thing consoled me: my watch
was still ticking
it was 8:31! Only sixteen minutes
since the blast

I began counting footsteps timing my progress

12. 8:50 A.M. near Yokogawa Station

Again
it comes back to me: the sensation
that this was only
my dream –

the thatched roof on fire

the peasant and his wife
moved deftly to salvage their household
furnishings, item
by item

but carrying
a great lacquered chest of drawers
they go stuck
no matter how they turned
and angled it
they couldn’t come through

so they stood facing each other with most of their movable goods in their arms

the man taking a half-step to the left, slowly
the woman to the right
then back again
as if in a trance

a slow, solemn, mesmerizing dance in the open doorway as the cottage burned

nobody stopped to help them.

13. Crossing Misasa Bridge, 9:15 A.M.

From a distance
I could see only the woman, lying
on her side
half-blocking
the other end of the bridge

and the refugees, as they approached her, hesitated

one turned back and ran toward the burning city

“What is it?” I cried but she didn’t answer

“You’ll get past this,” I told myself “if you don’t look!”

but after counting a hundred steps
afraid
something bad was about to happen
I dropped my hands

and a baby girl was undoing the buttons of her mother’s blouse

I drew close
and I saw
her clutch at the breasts of a corpse
she looked up at me
terrified

What could I possibly do for her?

“Go on,” I said to my legs “step over the body and go on.”

14. On the other side, 9:20 A.M.

A girl my age
was standing with vacant eyes in the middle
of the road
the great wound in her forehead
like a pomegranate
cracked open
Instinctively
I ran
my fingers across the skin
of my face
when I looked
down at my hands
there was blood on them

so I got the mirror out of my emergency kit and located a small cut on my eyebrow

which I washed with spittle

then I did my hair
in a handkerchief
neatly
and went on.

15. 9:40 A.M. at the bank of the Nagatsuka

I was wearing a white blouse
with a blue pattern
miraculously it was free
of dirt
and it didn’t get torn

everyone else
was in rags and hut
a woman
with the flesh of her side scooped out
and her ribs exposed
seeing me thread my way through the crowd
in my nice clothes
asked, “Can you help me?”

but a man came between us
and admonished her, saying, “Everyone
has the same pain as you.
Endure it
and we will find shelter.”

16. 4:30 P.M.

I reached my aunt’s village

and I went to the river to wash my clothes

the moment I dipped my blouse in the water

it fell apart.
```

---

## IC-1741: Winter Sequences

- Title: Winter Sequences
- Author (byline): Diane Wakoski
- Work: Virtuoso Literature for Two & Four Hands
- Publisher: Doubleday
- Publication date as stated: March 1975
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 752
- Already set (do not supply): none

### Source block (context only)

```text
Author: Diane Wakoski
Book: Virtuoso Literature for Two & Four Hands
ISBN: 978-0385004633
Publisher: Doubleday
Date (Month/Year): March 1975
```

### Introduction (context only: never use it for content warnings)

```text
God is the master of beauty in unexpected places. All of us expect a rose to be beautiful. But sometimes we look at people, who don’t appear especially attractive or talented, and because we can’t “see” any beauty, we assume it’s not there. How shallow of us.

I believe every person and thing created by God is something beautiful; but unfortunately, half the time we make our judgment in one glance. We see the imperfections and not the possibilities. If we were to look hard enough, perhaps we would see the secret of unexpected beauty.

Winter Sequences by Diane Wakoski
```

### Performance text (classify this)

```text
The rain was as slight as
the sound of someone's breathing at night. The day in
the mountains pale grey.
We had brought good cheeses,
a Boursin I especially liked,
wine, and a Pinot Chardonnay,
some liverwurst, french mustard,
pears, apples

for a picnic.

But first we hiked a simple circuit trail
which led us through deep mulchy ground.
I found surprising fungi
and didn't have a field guide to identify them by. Tiny
orange balls
on needle stems.
Snowy white puffballs
looking as if some golfer had lost them,
even the old puffballs turning brown,
wearing prickly skins like sycamore fruit.
Step by step, as I walked along
picking out inky caps,
I kept my secret.
First I would ask myself,
could I tell it so that it captured the moment?
No.
Then thinking about it more and more
I just wanted to spill it.
But I've remembered too much about what I've learned
to really spill it.

I hold my secrets.
They are poems only I can read. In the dark
under the stars.
No, once it is a secret
there is no joy in telling.

Rain cleared one muddy spot on the grass across from
my office.
I walked by it looking closely for mushrooms.
There were none.

Can I tell you now without sounding like a fool?

The air is so cold it stretches across your face
paralyzing it,
making you think
a hard glue has dried there
and left your face immobile.
The sun is shining as brilliantly on the pyracanthus
as a piano performance of Rubinstein.
The scene could either be a palm-tree-lined street
in Los Angeles
with pink stucco houses, mock orange, and jasmine
bushes or a New England town,
covered with fresh snow
where the crunch of boots shakes
holly wreaths on the porch door.
Does it matter where you find beauty?
that it immobilizes you,
makes you want to stop the passage of time,
makes you define each object
Landscape, the most brilliant
and terrible kind of beauty
causing us to remember our mobility essence of life
and wish we might stand still,
just stand still.

White mushrooms, as large as the headlights on a car, Pure white. Flat as an operating table.

It is precision
that defines beauty.
Beauty
is either contrasts or subtleties,
the unexpected
or
the inevitable. This is a coda
for descriptive information:
not poetry.
White mushrooms.
Three of them, as large as the open lips of calla lilies.
Their brown perfectly ribbed gills
cool and fleshy,
touching, like the cool skin of someone you love

I kept thinking and holding my secret
to myself
as we hiked that trail
knowing that if as we stopped either in the climax
forest
or the field on the other side of the mountain
filled with foggy milkweed pods,
and striped green gooseberries,
that if I said,
"A few days ago I saw three mushrooms as big as the
headlamps of cars/
They were on a lawn across from my office.
I bent down on my knees to see if they were real, and

touching them ,
found they were cooler and softer than skin. A dolphin's
skin perhaps.
I thought they were a trick.
I did not believe they were real.
Some new plastic, perhaps, invented for rich
suburbanites.
I questioned whether they were real.
I wondered, if they were real, had someone
planted them there
to make a fool of me.
I asked myself whether I should pick them.
I pondered why, if they were real, no one
had already
picked them.
I bent down and touched them.
I was almost afraid of them.
I walked away and did not tell anyone.
I was afraid no one would understand
how beautiful they were,
no, how excited I was.
I still do not know if anyone can know. I still have not
revealed
my secret."
that if I said this,
anyone would understand.

When you remember
all the mushrooms or wild fungi
you have come upon by surprise
or
other
sudden-nesses,
a blue crocus
early
anxiously out of the snow,
it is no more exciting
than seeing that red male cardinal
flashing his wings against the snow of winter. Common,
like arterial blood.
The question becomes
how do we live with the secret of unexpected beauty?

Three cardinal feathers fallen against the snow. Jonathan's gleaming black dog, Pearl, running in the crystal park. My three mushrooms, like the beautiful white hands of the embroiderer, growing out of the earth.
```

---

## IC-1742: Women and Children First!

- Title: Women and Children First!
- Author (byline): Douglas W. Phillips
- Work: The Sinking of the Titanic and Great Sea Disasters
- Publisher: The Vision Forum, Inc.
- Publication date as stated: June 1998
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 924
- Already set (do not supply): none

### Source block (context only)

```text
Author: Douglas W. Phillips
Book: The Sinking of the Titanic and Great Sea Disasters
ISBN: 978-0966523300
Publisher: The Vision Forum, Inc.
Date (Month/Year): June 1998
```

### Introduction (context only: never use it for content warnings)

```text
After setting sail for New York City on 10 April 1912 with 2,223 people on board, the largest passenger steamship in the world, the Titanic, hit an iceberg four days into the crossing, and ultimately sank on April 15, 1912. 1,517 people died in the tragedy. The high casualty rate was due in part to the fact that, although complying with the regulations of the time, the ship carried lifeboats for only 1,178 people. A disproportionate number of men died due to the "women and children first" protocol that was enforced by the ship's crew. Women and Children First by Douglas W. Phillips.
```

### Performance text (classify this)

```text
I The North Atlantic icefields are perilous and rough, And only should be tested by those of sterner stuff; They’re filled with fearful hazards for nautical machines — Icebergs that look like mountains, with jagged peaks and mean. But on this eve in 1912 a monarch of the sea Traversed her waves with brazen strides amid a night of glee. “Unsinkable!” they called her, yes unsinkable, their claim; But pride, not strength, would give this ship a destiny of fame. Near half a hundred thousand tons — the largest ship at sea! A mighty maiden of the waves, in length: eight eighty-three.

A monument to science? No, a legacy of pride. A testimonial to those who needlessly would die.

II While children’s heads lay nestled warm and snug through midnight hours, And husbands huddled next to wives asleep in love’s sweet powers, In upper decks men smoked and sang and toasted with a drink, Not knowing that the virgin ship would soon begin to sink.

First rang the bells, then came the cries, and last the dreaded panic, And now all knew t’would be the end of R.M.S.Titanic. But in that hour of foul despair and fear unmitigated A manly Christian cry to all was quickly circulated: “Women and children first,” they cried, “Women and children first! To save your souls you must give your lives, Women and children first!” III Amidst the tumult and the toil of lives then gripped with fear, A holy calm prevailed on those whose hearts and minds were clear; The cause was right, the mission pure, the path uncompromised; The men must die that others live — the men must give their lives. No greater love hath any man than that he lay down life For family: for little ones, for dearest bride and wife.

What manly breast would shirk the call, or fail with any breath To give his life for womankind, a sacrifice of death. “Women and children first,” the cry, “Women and children first!” Some must live while others die; “Women and children first!” IV. As water surged upon the decks and chaos reigned supreme, The band played on sweet hymns to God, which quieted the screams. Some raised their hands, or cried aloud, while others genuflected, In fleeting hopes that dreams and lives might still be resurrected. Across the deck a thousand scenes of lives held in the balance, With prayers delivered unto God in heavenly reliance. While stokers, stewards, officers and gentlemen en masse All lifted women into boats without regard to class. Women and children first — the law! Women and children first. The men would act — No fight. No flaw. Women and children first. V. One faithful father searched the deck to find his family, And rushing forward grabbed a girl near tossing into the sea. But though this little golden hair was to the man a stranger, He strapped to her his own life vest to save the babe from danger. At last he saw the face he loved and pulled her from the throng, Along with tender tiny ones who thought him bold and strong. A little boy, a little girl — the world he held so dear, Were waiting ignorant that time would bring their darkest fear.

Women and children first-praise God!
Women and children first.
This principle we ever laud!
Women and children first.
VI.
Five minutes he had to say goodbye, five minutes then all
was lost,
But giving his life for the woman he loved was hardly a
weighty cost.
“To the boats! To the boats, my darlings,” said he, “to
the boats!” and his words did race,
Then low’ring them into those cradles of life, he paused
... just one more embrace.
And now he kissed those tender lips, and now he
squeezed the hands,
And now he hugged and spoke the last of love and
wedding bands.
“Be brave my love. Be brave my son. Be brave my little
dears.
God’s ways are just, Christ rules above, and faith must
hush our fears.

“Women and children first,” said he, “Women and children first; to be a man I must set you free. Women and children first!” VII. At last he said goodbye to eyes which longed for him and home, At last he watched them pull away to safety through the foam, In moments he would be submerged and ’neath the icy brine, Content to know his sacrifice had given them more time. Just yards away a mother gazed back at the sinking boat, Her children bundled in her arms, warmed by their mother’s coat. A prayer of hope upon her lips, a Bible in her hand, A testament of love, of faith, and of her husband’s stand. “Women and children first,” she wept. “Women and children first,”

Stroking the curls of the infant she’d kept,
“Women and children first.”
VIII.
Into the liquid tomb he fell, moments from paradise,
With one last grasp he clawed the waves and caught his
dear one’s eyes.
His frozen face, his numb-ed hands, his body stiff and
cold —
An ocean legacy of heroism told.
Down through the depths Titanic sank, and into her
watery grave,
Bound by such forces that God had decreed would
render the hulk its slave.
Downward she plunged though the darkness so cold,
taking no inventory
Of perishing hundreds who crowded her decks, bound
for Hell or Glory.
For women and children first they died,
For women and children first;
They put their faith before their pride,
For women and children first.
```

---

## IC-1743: Words Can Inspire or

- Title: Words Can Inspire or
- Author (byline): Not specified
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1046
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carlos Andres Gomez
Album: Fate by the Throat
ASIN: B001GQXTNC
Publisher: CD Baby
Date (Month/Year): 2008
Spoken Word lyrics can be found on-line only at
https://carlosandresgomez.tumblr.com/poems
Author: Natasha T. Miller
Book: Butcher (pg 26-27)
ISBN: 978-1943735907
Publisher: Button Poetry
Date (Month/Year): Feb 2021
Find out more about the individuals mentioned in this
poem here:
https://www.bbc.com/news/world-us-canada-52905408
(from 1st poem)
2020 National Qualifier - MS
```

### Introduction (context only: never use it for content warnings)

```text
Words have power. Their meaning crystallizes perceptions that shape our beliefs, drive our behavior, and ultimately, create our world.

A 21st century Jewish Rabbi shared this striking statement: “Words are singularly the most powerful force available to humanity. We can choose to use this force constructively with words of encouragement, or destructively use words of despair. Words have the ability to help, to heal, to hinder, to hurt, to harm, to humiliate and to humble.”

Today I offer these powerful words from Carlos Andres Gomez and Natasha T. Miller in a compilation I call Words can Inspire or Destroy.
```

### Performance text (classify this)

```text
Destroy Poems By Carlos Andres Gomez and Natasha T. Miller

Words Worth by Carlos Andres Gomez they say:

“sticks and stones can break bones

– but words can never hurt”

yet, I’ve seen stones and sticks

break lips and bones in hips

after words commanded such action

or seen violence in metaphor

or pushed in minds before

children were four years or four months old now

tell me – what are words worth?
children learn about subject, object, and predicate
symbolically constructing sentences
in American classrooms
where white students are taught as subjects
while black students are treated like objects
destined to be subjected to life sentences
because of semantic switch-ups that set statutory
precedence
now

tell me – what are words worth?
and then…it comes to
naming
uniqueness is distorted to be invisibility
– instead of celebrating them
beautiful names like
asangaiso, owusu, or tokufu
become “that black kid over there”

become “that gangster over there”

become “that n*** – right there” now

tell me – what are words worth?
then grammar school students
get ideology laced grammar lessons
memorizing
hegemonic definitions and connotations
through pictures and intonations
inflecting oppression with stapled tongues
and mute voice boxes
they start with socially constructed polarities
called antonyms
and end with
strategic synonyms
insidiously selling minds to white history
paid for with words
we tattoo into subconscious crevices of our consciences
and it all started for me with dichotomies
framing opposed pairs
with the
“good” as the former
and the
“bad” as the latter:
good and evil
light and dark
white and black
pure and tainted
civilized and savage
and then I was fed
with “synonyms:”
progress equals betterment
brown equals primitive
fat equals undisciplined
poor equals stupid
law equals justice
now

tell me – what are words worth?
we’re brought up to believe in
adverbs that modify actions
– used to euphemize and pacify them
passive voicing third hand revisions
like “millions of native peoples were killed…unintentionally”
– not by anyone in particular – but they died
or slave owners were “understandably controlling”
or “necessarily brutal”
and before we know it
nouns are becoming pronouns
without the people’s consent
like polytheistic students reading about
one capitalized God…
wondering which one overthrew the others
or Latinos learning of US anointing ourselves the
only Americans
or me – watching a propagandized phrase
like “the War on Terror”
granted legitimization through pronoun glory on CNN
now

tell me – what are words worth?
and some think these thoughts
apply only to English class
as if science and math
don’t derive from the same path –
an American past

that bleeds the wrath
of Industrial class struggles
and oppressive fads
that teach us socioeconomics
in math class
to pare down graphs
placing pairs in graphs
writing paragraphs in SATs
about SUVs
so we see –
the rich as deserving
and
those in need as perturbing
now

tell me – what are words worth?
our father is named Uncle Sam
our teacher is named Webster
our slave-master is named English
my name was stolen

before I was born

by a language that wasn’t and isn’t mine

TRANSITION

Now let’s get a bit more specific about words: Author Doug Williford explains: If my spouse comes to me in obvious pain and asks the question, “Do you love me?”, an answer of “I love everyone,” would be truthful, but also hurtful and cruel in the moment... So when a person of any race speaks up in a time of obvious pain and hurt and says, “Black lives matter,” a response of “All lives matter,” is truthful. But it is also hurtful and cruel in the moment.

Natasha T. Miller further explains in her poem “Ten Things You Sound Like…”

Ten Things You Sound Like When You Say ‘all lives matter’ in Response to Black Lives Matter by Natasha T. Miller

1. You invite me to a breast cancer awareness walk to honor your late auntie. I arrive wearing all red. You tell me that the colors are pink . . . and I say I know, but I don’t see the point in breast cancer awareness having its own walk when people are dying of AIDS too.

2. Your family pet goes missing. You post pictures of it all around your neighborhood. I come and post pictures of other people’s missing pets from around the world on top of the picture of your pet . . . well . . . because . . . you’re not the only one missing a pet.

3. I show up to your grandmother’s funeral and hand out my grandmothers’ obituaries. You ask why. Because you ain’t the only one that lost a grandma.

4. I go into a hospital and change all the intensive care unit signs to care unit signs because every life in the hospital should be cared for just the same. What makes intensive care unit patients think that their lives matter more than the life of Jenny on the first floor fighting a cold? Colds can kill too.

5. Your fiancé stands you up at the altar. As you’re crying, I get up and yell millions of people get broken up with every day. Stop whining.

6. I show up at the Alcoholics Anonymous meeting to get help for my cotton candy addiction. An addict is an addict. We all deserve help.

7. You say Caylee Anthony. I saw what about her, we still don’t know who killed little JonBenet.

8. I say Black lives matter. You say you don’t see color.

9. I say Dallas. You say blue lives matter. I say I thought you didn’t see color.

10. It sounds like when I say Black lives matter, and you say all lives matter. It sounds like when I say Black lives matter, and you say all lives matter. It sounds like when I say Black lives matter, you say all lives matter.

It sounds racist. It sounds inhumane. It sounds like all lives
matter, but when I say: (*Names added for recency)
*Daunte Wright
*George Floyd
*Breonna Taylor
Tamir Rice
Trayvon Martin

You say nothing.

now

tell me – what are words worth?
words are powerful
words are oppressive
words are liberating
words are ideology

and hegemony

and stories

and culture words…are priceless

but often undervalued
poured out endlessly with little thought
but always at a cost
so think before you talk…
and make sure
it’s worth it
```

---

## IC-1744: World’s Afire

- Title: World’s Afire
- Author (byline): Paul B. Janeczko
- Work: Not specified
- Publisher: Candlewick
- Publication date as stated: Feb 2004
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1291
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul B. Janeczko
ISBN: 978-0763622350
Publisher: Candlewick
Date (Month/Year): Feb 2004
```

### Introduction (context only: never use it for content warnings)

```text
On Thursday, July 6, 1944, as the afternoon performance of the Ringling Bros. and Barnum & Bailey Circus in Hartford. Connecticut had just begun; fire broke out in the southwest corner of the big top. The fire was fast and angry, killing 167 people - mostly women and children - in a matter of minutes. World’s Afire by Paul B. Janeczko brings this day vividly back to life through the eyes of those affected by the blaze.
```

### Performance text (classify this)

```text
Sam Tuttle, Camera Operator

I still remember that day,
how hot it was
even before the fire.
I brought my new 8mm movie camera
to see how it'd work
to see if I could catch something special.

I filmed the midway
the menagerie
scenes filled with smiling faces
kids shrieking for joy
jabbering with excitement
hawkers selling souvenirs.

I never had time to see the show.
I was aiming my camera
at the tent.
smiling
as I zoomed in and out
to capture the size of the big top.
That's when l saw the corner
of the tent flash into flames.

Then the screaming started
people streaming from the tent
faces pained with fear
as black smoke blossomed
over the tent
like a tree of death.
I'm not sure
how long I filmed.
Enough to capture too much terror.
I know that.

I watched it once.
Enough to sicken me again.
But when I reversed the film,
killing smoke vanished
flames flickered to nothing
people backed out of the big top
and boys screeched with joy
jabbered in excitement
girls skipped and twirled
in their summer dresses
mothers smiled to see their children
joyous
all in silence,
none knowing
they would be this happy
for the last time
in their lives.

Bill Conti, Parent

I yanked Danny
through the crowd.
Packed together,
we surged
except for those who fainted.
They got stepped on.
Couldn't help it
though I tried.
Dannv was crying
when we reached the chute.
I tossed him
over to the other side
yelled for him to run
to meet me at the car.
He wailed but went.
I couldn’t.

Not then
not with all the other kids
looking like small frantic dolls.
So I started tossing them
over the chute.
I didn't have to tell them to run.
I climbed atop the chute
grabbing any small hand
raised my way.
I just hauled them –
couldn't count how many
up and over.
Up and over.
Until my foot slipped.
I lost mv balance,
went down.
The crowd dragged me under
even though I raised mv hand
for help.

Dennis Mortimer, Firefighter

We laid nine hundred feet of hose
then another hundred and a half.
About a ton of hose.
But we all knew
we were too late.
There was no tent
just folding chairs
and bleachers blazing
like nobody’s business.
Too hot to get close
See, they dip
their chairs in paint
and hang the up to dry,
so as the years pass
they’re adding another layer of paint
eager to burn
But that's not half the problem
of the tent itself.
To keep the rain out
they coat the canvas
with paraffin mixed with gasoline,
laid on good and thick with stiff brooms.
Oh, that waterproofs it all right -
been doing it that way for years -
but what does it give you?
One huge candle
just waiting for a light.

William Harvey, State Trooper

As the bodies arrived at the armory
I tied green casualty tags to their toes.
We separated the bodies by sex
as best as we could tell
setting each on a sagging army cot.
Mostly women, though,
and older girls
filled three rows.
We put the children in one corner,
men in the middle.
Then I wrote a list for each victim:
any clothes or jewelry,
scars, tattoos,
dental work.
Anything that would help.

A soldier covered each corpse with an olive drab blanket as those searching lined up outside in the shade of the elms.

When they came
searching for their dead,
thev were escorted
by a state trooper and a nurse
to the area most likely to hold
their loved ones.
Nurses carried smelling salts.
We had three first-aid stations.
A rolling cart with coffee.
There was little noise.
Shuffling feet. sobs mainly.

The lucky ones found their dead in the first few rows of cots before they got to the back rows where bodies looked like solemn museum statues except faceless and black.

I had pity for the searchers
who couldn't recognize their dead
and needed to start
the march
again
at the first cot
shuffling and sobbing.

Dr. Rose Beekman, Fire Expert

Surprised?
Oh. I'm sure
they were surprised
that the fire spread
so fast.
a runaway train.
Roared like one, too.
How fast did it spread?
Let me put it this way:
some didn't have time
to scream for help
before flames shot up
the side of the tent
like a dragon roaring to life.

Did they have a chance?
Not really.
Not the ones closest to the fire.
It'd be like surviving a volcano.
Hair sizzled.
Skin burned.
The tent became a chimney,

How long did it last?
Six minutes. Mavhe ten.
Yes. I'm sure.
But for most it lasted
only long enough
to have the breath burned out of them.
Most of them were dead
long before black chunks of tent
fell on their bodies
like pieces of night.

Sallv Weissman, Nurse

Nothing I'd seen in the ER for seventeen years prepared me.

I'd seen burn victims
but these people . . .
I even thought -
God help me for saying it -
that the dead were the lucky ones.
It wasn't just the wounds -
the skin hanging off in sheets
peeled patches red as a good steak,
wounds weeping -
but the sounds -
children crying
parents wailing
shouting," Help my baby!" –
the smell
of roasted flesh.
But there is always one case -
ask any of the girls in the ER -
that breaks your heart
wide open.
One woman
her face smudged
but hard with fear
grabbed my wrist
as I rushed by.
"Please," she said,
"check on mv son.
He's my only one."
I had other patients to sec
but she wouldn't let go of my wrist
until I promised
to look for her boy.
I found him among the other children
just as his last breath puffed out.
I held my breath
let it out
brought it back
before I reported the death to a doctor
who'd inform the mother.
Hospital policy.
Which I was glad for,
not having the heart
to not tell her
I was there
for his final sigh.

Thomas Gallagher Detective, Hartford Police Department

Her face caught my eye.
She was pretty
mavbe six
about the age of m:· son.
Her green toe tag read # 1565.
Untouched by the fire
except for a burn
on her neck and face.

Blond hair,
shoulder length and curly.
I pictured her blue eyes.
Wearing black patent leather shoes
part of a white flowered dress,
she was placed in the first row
because everybody thought
she would be the first
one claimed.
She wasn't.
Over 175 went before her.
In fact, no one came for Little Miss 1565.
Except William LeBlanc.
He took her
to Morrisette Funeral Home
where they cleaned her face
combed her hair.
took two more pictures,
just in case.
Two days later, they laid her in a small white coffin.
the last one available.
No one came for her.
Le Blanc drove her to Northwood Cemetery
through the black iron arch
past rows of empty graves,
marked with gray stones
telling tales of men
who died far from home
Killed in Action
Missing at Sea -
their bodies as gone
as their hopes in life.

With all the burials -
fiftv-four at Northwood –
the gravediggers
weary and sweating
needed to do
some final digging
while a solemn crowd waited.
A reverend read the Twentv-third Psalm.
A rabbi read the Kaddish.
A priest read in Latin,
sprinkled holy water.

In the sun
I waited with her
while the others left.
Even as she was lowered
into the ground
and dirt thumped on her coffin
no one came for her.
In the sun
I waited with her.
```

---

## IC-1745: Yellow Bird and Say Yes

- Title: Yellow Bird and Say Yes
- Author (byline): Andrea Gibson
- Work: The Madness Vase
- Publisher: Write Bloody Publishing
- Publication date as stated: 2012
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1330
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andrea Gibson
Book: Pole Dancing to Gospel Hymns
ISBN: 978-0981521305
Publisher: Write Bloody Publishing
Date (Month/Year): June 2008
Author: Andrea Gibson
Book: The Madness Vase
ISBN: 978-1935904373
Publisher: Write Bloody Publishing
Date (Month/Year): 2012
```

### Introduction (context only: never use it for content warnings)

```text
Author Philip Pullman once said, “Children need art and stories and poems and music as much as they need love and food and fresh air and play. Children in every part of the world are starved for something that nourishes their souls in a way that nothing else ever could. Art, Music, Poetry . . . they not only reflect a nation’s identity; they create it. Paint your picture, sing your song, write your story and by doing so create a world you’ll be proud to pass on to the children.

Yellow Bird and Say Yes by Andrea Gibson
```

### Performance text (classify this)

```text
Say Yes (Pg 86-89)

When two violins are placed in a room
if a chord on one violin is struck
the other violin will sound the note.
If this is your definition of hope,
this is for you
For the ones who know how powerful we are,
who know we can sound the music in the people around us
simply by playing our own strings.
For the ones who sing life into broken wings,
open their chests and offer their breath
as wind on a still day when nothing seems to be moving
spare those intent on proving god is dead.
For you when your fingers are red
from clutching your heart so it will beat faster.
For the time you mastered the art
of giving yourself for the sake of someone else.

For the ones who have felt what it is to crush the lies and lift truth so high the steeples bow to the sky

This is for you

Yellow Bird (Pg 85-87)
Why is art the first class to be dropped
by any public school?
Why are music rooms empty in junior highs
from New York City to Nashville, Tennessee?
Like the war is worth funding but music isn’t?

Our culture is a prison.
And the only one with the key is little Emi Jones,
covering every inch of her standardized test
with the best number 2 pencil version of
a starry night anyone has ever seen
and yes, there is a humming bird in her chest.
Its wings are beating 80 times a second.
See … Doctor King did not write a speech
called I Have a Dream - he wrote a poem
called I Have a Dream.

I don’t know if God will have a purple heart,
but I know we have a bow we could pull above the strings
of a combat boot and make it sing
like the eyes of a 7-year-old boy
staring down the barrel of Apartheid’s loaded guns;
Screaming for the right to write stories;
to sing songs in his Mother’s tongue.

Point me in the direction of glory I will run towards a tiny hand in the most wounded

corner of Palestine,
dipping a brush into a can of yellow paint
to paint a feather on a wing on a wall that is so tall,
only yellow birds can escape.
And when they do, they carry
the hearts of little girls on their backs.
and when their wings flap, they make the sound of
anthems being replaced with sky.
And I swear, I could see their shadows
pass across your glowing face
the night you said you have never given birth to a child
but you tear every single time you write a poem.

We are growing our future with every borrowed pen I pray tonight we could write a rain that would fall like the tears at Folsom State Prison the day Johnny Cash smashed his guitar over apathy’s

head. The way Frida Kahlo* - in the prison of her own body - had whole years where she could paint nothing but red but she painted . . .

To the bars in the locked cells of her pores.
The same when saxophones in New Orleans
played music underwater,**
knowing some of those notes would rise up to the air
carrying people and hope to shore.

I don’t believe in the godliness of steeples,
but I believe in the stained glass
and every key on every organ that is desperate for light,
‘cause we are desperate for life -
for the sight of a captivated audience
refusing to be held captive in the thought
that they can only listen and watch.

Picasso said he would paint with his own wet tongue
on the dusty floor of a jail cell if he had to.
We have to create;
it is the only thing louder than destruction;
it is the only chance the bars are gonna break.
Our hands full of color
reaching towards the sky - a brush stroke in the dark --
It is not too late ,
That starry night - it is not yet dry.

*Find our more about artist Frida Kahlo here https://www.fridakahlo.org/ **Reference is to Hurricane Katrina (2005) – Find our more her https://www.history.com/topics/natural-disasters-and-environment/hurricane-katrina

Say Yes (Pg 86-89)

[So, you see . . . ] This is for the man who showed me
the hardest thing about having nothing
is having nothing to give,
who said the only reason to live is to give ourselves away.
So this is for the day we’ll quit or jobs
and work for something real.
We’ll feel for sunshine in the shadows,
look for sunrays in the shade.
This is for the people who rattle the cage that slave

wage built, and for the ones who didn’t know the filth until tonight but right now are beginning songs that sound something

like people turning their porch lights on and calling the homeless back home

This is for all the s*** we own,
and for the day we’ll learn how much we have
when we learn to give that s*** away.
This is for doubt becoming faith
for falling from grace and climbing back up.
For trading our silver platters for something that

matters, like the gold that shines from our hands when we hold each other.

This is for your grandmother,
who walked a thousand miles on broken glass
to find that single patch of grass to plant a family tree
where the fruit would grow to laugh.
For the ones who know the math of war
has always been subtraction
so they live like an action of addition.

For you when you give like every star is wishing on you, and for the people still wishing on stars this is for you too.

This is for the times you went through hell
so someone else wouldn’t have to.
For the time you taught a 14-year-old girl
she was powerful.
For the time you taught a 14-year-old boy
he was beautiful.
For the radical anarchist asking a republican to dance,
‘cause what’s the chance of anyone moving from right to

left
if the only moves they see are NBC and CBS.
This is for the no becoming yes,
for fear becoming trust,
for saying I love you to people who will never say it to

us.

For scraping away the rust and remembering how to

shine. For the dime you gave away when you didn’t have a

penny,
For the many beautiful things we do,
For every song we’ve ever sung,
For refusing to believe in miracles
because miracles are the impossible coming true
and everything is possible.

This is for the possibility that guides us
and for the possibilities still waiting to sing
and spread their wings inside us,
‘cause tonight Saturn is on his knees
proposing with all of his ten thousand rings
that whatever song we’ve been singing we sing even

more. The world needs us right now more than it ever has

before.
Pull all your strings.
Play every chord.
If you’re writing letters to the prisoners
start tearing down the bars.

If you’re handing out flashlights in the dark start handing out stars.

Never go a second hushing the percussion of your heart.
Play loud.
Play like you know the clouds
have left too many people cold and broken
and you’re their last chance for sun.
Play like there’s no time for hoping brighter days will

come. Play like the apocalypse is only 4…3…2… but you have a drum in your chest that could save us.

You have a song like a breath that could raise us
like the sunrise into a dark sky that cries to be blue.
Play like you know we won’t survive if you don’t
but we will if you do.
Play like Saturn is on his knees
proposing with all of his ten thousand rings
that we give every single breath.
This is for saying, YES.
This is for saying, YES.
```

---

## IC-1746: Yertle the Turtle

- Title: Yertle the Turtle
- Author (byline): Theodor Geisel (aka Dr. Suess)
- Work: Not specified
- Publisher: Tandem Library
- Publication date as stated: Nov 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 960
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theodor Geisel (Dr. Seuss)
ISBN: 978-0007173143
Publisher: Tandem Library
Date (Month/Year): Nov 2001
```

### Introduction (context only: never use it for content warnings)

```text
Although many people are unaware of the political basis for many of Geisel’s children’s books, the story of Yertle the Turtle closely parallels the story of Adolf Hitler during World War II. In fact, the original design of Yertle the Turtle had a moustache (before Dr. Seuss removed it, not wanting the symbolism to be too blatantly obvious). Hitler was the despotic ruler of Germany, before he decided to expand the country's wealth by means of force. Yertle the Turtle used turtles as his stepping stones to power, Adolf Hitler used the people of Germany, Italy, and the USSR as his. Welcome to the parable of Yertle the Turtle by Theodor Geisel (Dr Suess). He’s not just for children anymore . . . .
```

### Performance text (classify this)

```text
On the far-away island of Sala-ma-Sond, Yertle the Turtle was king of the pond. A nice little pond. It was clean. It was neat. The water was warm. There was plenty to eat. The turtles had everything turtles might need. And they were all happy. Quite happy indeed.

They were... until Yertle, the king of them all, Decided the kingdom he ruled was too small.

"I'm ruler," said Yertle, "of all that I see. But I don't see enough. That's the trouble with me. With this stone for a throne, I look down on my pond But I cannot look down on the places beyond. This throne that I sit on is too, too low down. It ought to be higher!" he said with a frown. "If I could sit high, how much greater I'd be! What a king! I'd be ruler of all that I see!"

So Yertle, the Turtle King, lifted his hand And Yertle, the Turtle King, gave a command. He ordered nine turtles to swim to his stone And, using these turtles, he built a new throne. He made each turtle stand on another one's back And he piled them all up in a nine-turtle stack. And then Yertle climbed up. He sat down on the pile. What a wonderful view! He could see 'most a mile! "All mine!" Yertle cried. "Oh, the things I now rule! I'm the king of a cow! And I'm the king of a mule!

I'm the king of a house! And, what's more, beyond that
I'm the king of a blueberry bush and a cat!
I'm Yertle the Turtle! Oh, marvelous me!
For I am the ruler of all that I see!"

And all through the morning, he sat up there high Saying over and over, "A great king am I!" Until 'long about noon. Then he heard a faint sigh. "What's that?" snapped the king And he looked down the stack. And he saw, at the bottom, a turtle named Mack. Just a part of his throne. And this plain little turtle Looked up and he said, "Beg your pardon, King Yertle. I've pains in my back and my shoulders and knees. How long must we stand here, Your Majesty, please?" "SILENCE!" the King of the Turtles barked back. "I'm king, and you're only a turtle named Mack." "You stay in your place while I sit here and rule. I'm the king of a cow! And I'm the king of a mule! I'm the king of a house! And a bush! And a cat! But that isn't all. I'll do better than that!

My throne shall be higher!" his royal voice thundered, "So pile up more turtles! I want 'bout two hundred!" "Turtles! More turtles!" he bellowed and brayed. And the turtles 'way down in the pond were afraid. They trembled. They shook. But they came. They obeyed. From all over the pond, they came swimming by dozens. Whole families of turtles, with uncles and cousins. And all of them stepped on the head of poor Mack. One after another, they climbed up the stack. Then Yertle the Turtle was perched up so high, He could see fourty miles from his throne in the sky! "Hooray!" shouted Yertle. "I'm the king of the trees! I'm king of the birds! And I'm king of the bees! I'm king of the butterflies! King of the air! Ah, me! What a throne! What a wonderful chair! I'm Yertle the Turtle! Oh, marvelous me! For I am the ruler of all that I see!"

Then again, from below, in the great heavy stack, Came a groan from that plain little turtle named Mack. "Your Majesty, please... I don't like to complain, But down here below, we are feeling great pain. I know, up on top you are seeing great sights, But down here at the bottom we, too, should have rights. We turtles can't stand it. Our shells will all crack! Besides, we need food. We are starving!" groaned Mack.

"You hush up your mouth!" howled the mighty King Yertle. "You've no right to talk to the world's highest turtle. I rule from the clouds! Over land! Over sea! There's nothing, no, NOTHING, that's higher than me!"

But, while he was shouting, he saw with suprise
That the moon of the evening was starting to rise
Up over his head in the darkening skies.
"What's THAT?" snorted Yertle. "Say, what IS that
thing
That dares to be higher than Yertle the King?
I shall not allow it! I'll go higher still!

I'll build my throne higher! I can and I will! I'll call some more turtles. I'll stack 'em to heaven! I need 'bout five thousand, six hundred and seven!"

But, as Yertle, the Turtle King, lifted his hand
And started to order and give the command,
That plain little turtle below in the stack,
That plain little turtle whose name was just Mack,
Decided he'd taken enough. And he had.
And that plain little lad got a bit mad.
And that plain little Mack did a plain little thing.
He burped!
And his burp shook the throne of the king!

And Yertle the Turtle, the king of the trees, The king of the air and the birds and the bees, The king of a house and a cow and a mule... Well, that was the end of the Turtle King's rule! For Yertle, the King of all Sala-ma-Sond, Fell off his high throne and fell Plunk! in the pond!

And tosay the great Yertle, that Marvelous he,
Is King of the Mud. That is all he can see.
And the turtles, of course... all the turtles are free
As turtles and, maybe, all creatures should be.
```

---

## IC-1747: You’re Only Old Once: A Book for Obsolete Children

- Title: You’re Only Old Once: A Book for Obsolete Children
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House, Inc.
- Publication date as stated: Feb 1986
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1227
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Seuss)
ISBN: 978-0394551906
Publisher: Random House, Inc.
Date (Month/Year): Feb 1986
```

### Introduction (context only: never use it for content warnings)

```text
Dr. Seuss' magic was in creating imaginary worlds for children. In his poems, children can use their imaginations and learn not to fear the real world. He exorcised the world's real monsters by filling it with his own--the Yuzz, the Wumbus, the Snee, and the Grinch.

Then at 82, just five years before his death in 1991, Dr. Seuss published his first book for adults. His same magical verse, helps our older population face up to the perils of hospitalization. Is it a children’s book? Well . . . the subtitle is “A Book for Obsolete Children,” and it may be truly useful in helping children understand the frailties and fears of their grandparents.

You’re Only Old Once by Theo Geisel (aka Dr. Seuss)
```

### Performance text (classify this)

```text
One day you will read
in the National Geographic
of a faraway land
with no smelly bad traffic.

In those green-pastured mountains
of Fotta-fa-Zee
everybody feels fine
at a hundred and three
‘cause the air that they breathe
is potassium-free
and because they chew nuts
from a Tutt-a-Tutt Tree.
This gives strength to their teeth,
it gives length to their hair,
and they live without doctors,
with nary a care.

And you'll find yourself wishing that you were out there
in Fotta-fa-Zee and not here in this chair
in the Golden Years Clinic on Century Square
for Spleen Readjustment and Muffler Repair.

Just why are you here?
You're not feeling your best . . .
you've come in for an Eyesight
and Solvency Test.

And if you're the type that gets finicky-finick,
at this point you'll try to get out of that clinic.
But they will outwit you as quick as a wink!
The Quiz-Docs will catch you!
They'll start questionnairing!
They will ask you point blank,
how your parts are all fairing.
And your grandfather's parts.
And please try to recall
if your grandma hurt most in spring or fall.
Did your cousins have dreadful wild nightmares at night?
Did they suffer such ailments as Bus Driver's Blight,
Chimney Sweep's Stupor, or Prune Picker's Plight?
And describe the main cause of your uncle's collapse.
Too much alphabet soup? Or martinis. perhaps?

And the next thing to know,
when you've finished that test,
is somehow you've lost
both your necktie and vest
and an Ogler is ogling
your stomach and chest.

Your escape plans have melted!
You haven't a chance,
for the next thing you know,
both your socks and your pants
and your drawers and your shoes
have been lost for the day.
The Oglers have blossomed
like roses in May!
And silently, grimly, the ogle away.

What those Oglers have learned
they're not ready to tell
Clinicians don't spout
their opinions pell-mell.
So you're back
with the vestibule fish for a spell.
Norval won't bring you comfort, you know.
But he's quite sympathetic as Clinic Fish go.

There you'll sit several hours, growing tenser each

second, fearing your fate will be worse than you reckoned, till finally Miss Becker, your beckoner beckons . . .

. . . to a booth where the World-Reowned Ear Man, Von Crandell, has perfected a test know as Bellows and Candle. If wind from the bellow can't blow out the flame, you failed! And you're going to be sorry you came.

You'll be told that your hearing's so murky and muddy, your case calls for special intensified study. They'll test you with noises from far and from near and you'll bet a black mark for the ones you can't hear. Then they will say, "My dear fellow, you're deafer than

most. But there's still hope, since you're not quite as deaf as a

post. We'll study your symptoms. We'll give you a call. In the meantime, go back and sit down in the hall."

So you'll find yourself talking to Norval once more. And Norval will think you're a bit of a bore because Norval has heard the same stories before.

To this fish you'll become
a plain pain in the neck
while you wait, once again,
for Miss Becker to beck.

But Miss Becker won't come.
With great swish and great swank
a wheelchair will come!
You've gained status and rank!
And Whelden the Wheeler will say with great pride:
"You have qualified, sir.
You are now certified
as a VIP Case.
You're entitled to ride!
Through thin and through thick
I'll be at your back side."

Dear Whelden will show you great sights as you go: Right now you are riding down Stethoscope Row. And I know that, like all our top patients, you're hoping to get yourself stethed with some fine first class

scoping.
So I'm sure you'll be simply delighted to hear
that in the Internal Organs Olympics last year
Doctors Schmidt, Smoot, Sinatra, Sylvester, and Fonz
won fifteen gold medals,
nine silvers,
six bronze!
For the moment, however, we'll by-pass this bunch.
There is plenty of time to see them after lunch.

You must see Dr. Pollen, our Allergy Whiz, who knows every sniffle and itch there is. Dr. Pollen will find, as he works on your case, if the face powder's wrong on your stepsister's face. He will check your reactions to thumb tacks and glue, catcher's mitts, leaf mold, and cardigans, too, nasturtiums and marble cake, white and blue chalks, anthracite coal and the feathers of hawks. Also corn on the cob. Also buffalo grease and how you react when you're stared at by geese. He'll take copious notes. Then I'll hazard a guess that he'll send you downstairs to see Dr. Van Ness. Van Ness has enjoyed a high rate of success in his pioneer work in the Study of Stress. So, you can be sure, he will stress you a trifle, then he'll send you around to see Dr. Van Eiffel. Dietician Von Eiffel controls the Wuff-Whiffer our Diet-Devising Computerized Sniffer on which you just simply lie down in repose and sniff at a good food as it goes past your nose. From caviar souffle to caribou roast, from pemmican patties to terrapin toast, he'll find out by Sniff-Scan the foods you like most.

And when that guy finds out
what you like,
you can bet it
won't be on your diet.

From here on, forget it!

Then, into the New Wing! We'll see Dr. Spreckles, who does the Three F's-Footsies, Fungus, and Freckles. And nextly we'll drop in on young Dr. Ginns, our A and S Man who does Antrums and Shins, and of course he'll refer us to Doctors McGrew, McGruire, and McPherson and Blinn and Ballew and Timpkins, and Tompkins and Diller and Drew, Fitzsimmons, Fitzgerald, and Fitzpatrick, too, all of whom will prescribe a prescription for you.

For your Pill Drill you'll go to Room Six Sixty-three,
where a voice will instruct you, "Repeat after me . . .
This small white pill is what I munch
at breakfast and right after lunch.
I take the pill that's kelly green
before each meal and in between.
These loganberry-colored pills
I take for early morning chills.
I take the pill with the zebra stripes
to cure my early evening gripes.
These orange-tinted ones, of course,
I take to cure my charley horse."

"I take three blues at half past eight
to slow my exhalation rate.
On alternate nights at nine pm
I swallow pinkies. Four of them.
The reds, which make my eyebrows strong,
l eat like popcorn all day long.
The speckled browns are what l keep
beside my bed to help me sleep.
This long last one is what l take
if l should die before l wake."

When at last we are sure
you've been properly pilled,
then a few paper forms,
must be filled
so that you and your heirs
may be properly billed.

Whereupon . . .
if you are smart,
there's a very good chance
that you'll meet soon again
with your socks, coat, and pants.

And you'll know,
once your necktie's back under your chin
and Norval has waved you Godspeed with his fin,
you're in pretty good shape
for the shape you are in!
```

---

## IC-1748: Abortion Poetry

- Title: Abortion Poetry
- Author (byline): Ally Sheedy and Gwendolyn Brooks
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1234
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ally Sheedy
Book: Yesterday I Saw the Sun
ISBN: 978-0671731304
Publisher: Summit Books
Date (Month/Year): Feb 1991
Author: Gwendolyn Brooks
Book: Afro-American Writing:
An Anthology of Prose and Poetry
ISBN: 978-0271038452
Publisher: Penn State Press
Date (Month/Year): 2010
```

### Introduction (context only: never use it for content warnings)

```text
Nearly 40 percent of teen pregnancies end in abortion. Many of these teen mothers feel a sense of relief that the ordeal is over. And, certainly, it is possible to continue with life without peers even knowing that a fellow teenager was pregnant. However, many teenagers find themselves feeling a sense of remorse later down the road. The idea that a life was terminated at a teen’s discretion can be an emotionally traumatic experience.

Local Anesthesia by Ally Sheedy
```

### Performance text (classify this)

```text
Local Anesthesia by Ally Sheedy I had an abortion yesterday. At 11:53 A.M. across from Central Park.

You know where it is. Near F.A.O. Schwarz and the Plaza Hotel. At the clinic.

I was awake for the whole thing cause I wanted to remember it. There was a Snoopy poster on the ceiling. It said "Smile."

Today I frown by the trophy case
and watch Laura go over her algebra homework.
No one in this school knows where I was.
Today I am just in class
and everyone is impossibly young.
They scraped my insides out.
There's a burning feeling between my legs
so I keep them crossed
and no one will know.

I'm a "fallen woman."

I'm not gonna lie to you.
I didn't want the kid.
This is not one of those songs about
the abortion blues.

I'm just sorry I had to
put myself
through it.
I didn't get my algebra homework done.
Not even close.
I was so scared about this ordeal
I spent the weekend on the suicide line.

"Hello," said a woman's voice.

"Do you need help?"

I wept.

"I'm so scared," I cried. "They're going to cut me up. They'll
tear me apart like tissue paper,
like spider webs, like bread.
It's not my fault. Do you understand?"

I put my forehead against the glass trophy case.
It is cool here.
We have so many swimming trophies
for a New York City school.
I wish I could shake him off me.
Not the guy. You know. Him.
The kid.
I know how hard he clutched me
from the inside
when they took him out.
Now he dances bodiless
tapping round my head
like rain.
I know you, he says. You are my mom.

The hallways are empty and Laura went to class. It's 12:22. He's been dead for over 24 hours.

I double over. Sick.

You don't know me, I say back to him.
I am an algebra student.
You don't know me.
I am someone's daughter.
You don't know me, baby.
I am a doper,
a compulsive liar,
I don't have a boyfriend,
never get picked for the basketball team.
I am sixteen.
Is this who you want for your mother?
I know you, he says back.
You're mine.
And yeah, I guess. I know.
I conceived this tyrant New Year's Eve
at the Hilton Hotel.
I knew it when it happened and that it was a boy.
I've read about this before in corny short fiction.
You know, in magazines like Complete Woman.
But it happened like a bolt
of electric lightning.
I felt it and I knew.

I'm a mother.

He - the guy - went out to the deli
and I looked out the window at the pouring rain.
I knelt there naked at 2:39 A.M.
and offered myself to the rhythm outside.
Wet New York City.
Happy New Year, rest of my life.
What am I going to do with the kid?
I was awake for my abortion
Because I wanted to remember it.
They put my legs in stirrups.
I was very still.

I looked up at the Snoopy on the ceiling
and prayed.
I'm letting you go, I said to the boy.
This is the way out.

The guy in the other room
who split the cost with me
is sleeping with my best friend.
He hopes we get done in time
to catch the 3: 15 movie at Loew's.
Superman.

All morning he cried 'cause he's a Catholic.
And I rocked him and told him, It's all right.
Later today he'll push against me hard
in the bathroom
and I'll let him
even though I'm bruised inside from ribs to thighs.

It was in the pamphlet-
Sex now can rip you open.
I read it, but I know they only meant
physically.

I need someone to hold me tightly so much.

So, you see, baby,
I'm giving you the way out.
I'm your mother and I want you to take it.
It's the only thing I'll ever tell you to do.
So, listen.

I was awake for my abortion because
I wanted to feel him leave me.
I wanted him to know why.
I did it 'cause I'm sixteen and
a compulsive liar.
I did it 'cause I need to be held too much
and I'm not a Catholic.
I did it because I don't have a father for you
and have only my body to give.
I have learned that this is not enough.

I was awake at 11:53 A.M. yesterday
for my abortion.
Undeveloped
Unevolved
one thing alone is clear
and it's my incompleteness.
Emotionally I know myself to be
the real fetus.

Silently repeating this I lay
and they took him out.
The only choice I knew
I could make.

When it was over I lay so still
they thought I was in shock.
But I was only saying good-bye
To him.
And you never can.

'Cause, child, I hear you in my head
and on you cry like rain
and I can feel you at my heart
inside I nurse you still.

TRANSITION

Teen pregnancies are not the only ones who result in a high rate of abortions. In “The Mother” by Gwendolyn Brooks the speaker mourns the loss of children aborted because of the poverty of the mother. Her desire to do what was best for her children and the finality of her decisions. The depiction of the narrator—honest, reflective, and self-aware— show a clear conflict between her desire to do what was best for her children and the finality of her decisions. The narrator is complicated—full of conflicting emotions regarding both herself and her lost children. The Mother by Gwendolyn Brooks The Mother by Gwendolyn Brooks

Abortions will not let you forget.
You remember the children you got that you did not get,
The damp small pulps with a little or with no hair,
The singers and workers that never handled the air.
You will never neglect or beat
Them, or silence or buy with a sweet.
You will never wind up the sucking-thumb
Or scuttle off ghosts that come.
You will never leave them, controlling your luscious sigh,
Return for a snack of them, with gobbling mother-eye.

I have heard in the voices of the wind the voices of my dim killed
children.
I have contracted. I have eased
My dim dears at the breasts they could never suck.
I have said, Sweets, if I sinned, if I seized
Your luck
And your lives from your unfinished reach,
If I stole your births and your names,
Your straight baby tears and your games,
Your stilted or lovely loves, your tumults, your marriages, aches,
and your deaths,
If I poisoned the beginnings of your breaths,
Believe that even in my deliberateness I was not deliberate.
Though why should I whine,
Whine that the crime was other than mine?—
Since anyhow you are dead.
Or rather, or instead,
You were never made.
But that too, I am afraid,
Is faulty: oh, what shall I say, how is the truth to be said?
You were born, you had body, you died.
It is just that you never giggled or planned or cried.

Believe me, I loved you all.
Believe me, I knew you, though faintly, and I loved,
I loved you
All.
```

---

## IC-1749: The Accident

- Title: The Accident
- Author (byline): Lisa Lewis
- Work: The Unbeliever
- Publisher: University of Wisconsin Press
- Publication date as stated: Oct 1994
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1197
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lisa Lewis
Book: The Unbeliever
ISBN: 978-0299144043
Publisher: University of Wisconsin Press
Date (Month/Year): Oct 1994
```

### Introduction (context only: never use it for content warnings)

```text
Three to four million women in the United States are beaten in their homes each year by their husbands, ex-husbands, or male lovers. If you complete the mathematical calculations, that is one abuse victim every 15 seconds. In “The Accident” by Lisa Lewis, we are allowed to hear the reflection of one such battered woman: A woman who survived by taking matters into her own hands. In this poem, strangers at a fast food restaurant bring memories of the author’s abuse and the result of that abuse to the surface. “The Accident” by Lisa Lewis.
```

### Performance text (classify this)

```text
I had no business there in the first place – I’m putting on weight – but the counter help was all smiles, Having survived the lunch hour crunch. My husband and I Ordered burgers and fries; I was in front, so I chose A seat on the far side, back to the window. I picked off two thin rings of onion; the fries were limp.

We were talking about some recent trouble, Something about the car, maybe, both of us Interested, me a little bit bitchy, so it was almost the way you turn Instinctively, say from a spider web in a darkened hall, How I looked across the restaurant and found her face, Left cheekbone swollen to a baseball, the same eye blackened, Heavy make-up, front tooth out in a jack-o-lantern grin As she tried to look friendly to the young waitress Her husband motioned over. He rested one hand On his wife’s shoulder, solicitous, the other waving A lit cigarette, a small man, dark-haired, now laughing aloud, Glancing at the uncombed head of his beaten wife again Turning her back to the room, though not crowded, All suddenly staring, reading the last few hours Of those lives in a horror of recognition. She cupped her hand shading the side of her face, You could see lumps of vertebrae through her t-shirt, And he kept on talking, smiling at her, with a slight tilt Of his head, as if saying poor baby, something happened to her, Good thing I’m here to take care of her, a car wreck, A bad one, a smash-up, and all of us looked And knew better. At the table with them was a little girl. The man, the woman, the five-year-old daughter – Even the man and the beaten woman had the same features, As people do who have lived together for years. I couldn’t see The child’s face. He was jotting a note on a small pad, The waitress’s name, as if to write a letter praising Her fine service, and she smiled through her horror, she Hardly more than sixteen, with clear pale skin. Next to us A woman in permed hair and suit rose to leave, lunch untouched, With her daughter. She carried a leather legal-size folder. We left soon after, heads turned, not looking, Because sometime the man and woman would go Home to the privacy of a city apartment, no neighbors Home all day to hear, but first I said, in the restaurant, Across the room where he couldn’t hear, If I had a gun I’d blow his brains out, and I thought of that moment Familiar from movies, the round black hole in the forehead Opening, the back of the skull blowing out frame by frame Like a baseball smashing a window, but no one near Would’ve even been bloodied because no one was standing anywhere Near him, his hand on the beaten woman’s shoulder Might as well’ve been yards from his body.

I was taught not to write about this. But my teacher, A man with a reputation who hoped I would make Good, never knew that I, too, have been hit in the face by a man. He knew only my clumsy efforts to cast what happened Into “characters,” and he loved beauty in poetry.

Maybe what I had written was awkward. Maybe my teacher Guessed what happened and forbade me writing it For some good reason, he cared for me, or he feared He too might’ve slapped my face, because I, like the character In that first effort, was bitching to the heavens and a redneck Boyfriend, and we argued outdoors, near a stack of light wood Used to kindle the stove like everyone has In the foothills of North Carolina. That day I railed Like a caricature of a bitching redneck woman, Hands on hips, sometimes a clenched fist, I was Bitching, I think, as he planned some stupid thing I hated, like fishing, pitching horseshoes, driving To visit his mother on Sundays, her tiny house Tangled in dirt roads, where she sat in the kitchen dipping snuff. Whatever he wanted to do was harmless, But so was my shrieking, my furious pleading, an endless loop Inside my head rolling I want to be rid of him, and he slapped me Across my open mouth, I felt myself shut up and staggered, Because he was a large man, and I was a large woman, He had to make sure he hit me pretty hard, Both of us strong and mad as hell, early One Saturday morning, when he wanted to do what he wanted to do And I wanted to keep him from it. He slapped me Twice, open-handed, knocking me, open-handed, to my knees In kindling, so my knees were scraped bloody and my hand Closed on a foot and a half of inch-thick pine, and I stumble up, Swinging, my eyes popping wide, till I grought it down Hard across his shoulder, I saw how the rage on his face Flashed to fear, just that quick, a second, or less, And he turned to run but he made the wrong choice, If he’d gone to the road I wouldn’t’ve followed, but he ran Inside my “duplex” apartment, an old country house Cut in two. So I cornered him upstairs and knocked him out. It was simple. He fell so hard, I thought I’ve killed him; I was throwing my clothes in a paper bag when I heard him Sobbing. In the bathroom mirror I found the black eye and lop-sided lip, And it seemed as if I might still take it back, the last ten minutes, The chase, the beating, the high-pitched screaming, The stubborn need to go fishing. But the make-up I disdained In those years – I had just turned twenty – didn’t do much To cover the bruises. His face was clear. The knot on his head Stopped swelling under ice. It was easy to tell him To get the hell out and only regret it every other minute Since there were no children, no marriage, even, And I was young and believed I had proven I was strong. I had beaten a man to his knees. Months later I would go to college and stay safely there for years, Not letting on to anyone the terrible thing I’d done, until I wrote That clumsy poem with the unbelievable characters, and now I’ve tried To do it again, this time with different characters, I’ve defied My teacher, who meant for me to learn to write well, Who meant for the world to think well of me, And I am not sorry. If he asked why I would say I had to do it, and that lie would be like the lie of living Without telling, till one day seeing the beaten face, What scared me most, the missing tooth, the tangled hair, the vertebrae, The daughter. There is no use thinking what it means About me to say this: I am not sorry. I might have killed That man. I might have blown his brains out.
```

---

## IC-1750: The Adoption Papers

- Title: The Adoption Papers
- Author (byline): Jackie Kay
- Work: Not specified
- Publisher: Bloodaxe Books
- Publication date as stated: Dec 1991
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2151
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jackie Kay
ISBN: 978-1852241568
Publisher: Bloodaxe Books
Date (Month/Year): Dec 1991
```

### Introduction (context only: never use it for content warnings)

```text
One in five children waiting to be adopted is from an ethnic minority and for them the wait is three times as long as for white children. Twenty per cent never find new homes.

Bi-racial author, Jackie Kay was born in 1961 to a white nurse from the Highlands and a Nigerian student studying agriculture at Aberdeen University. Her father returned to Nigeria, leaving her 19-year-old mother with a difficult decision to make: keep the child or put her up for adoption. Kay was ultimately adopted by a white Scottish couple.

Kay’s ability to address the personal issue of adoption as well as the added issue of race is eloquent, truthful and moving. The Adoption Papers by Jackie Kay
```

### Performance text (classify this)

```text
NOTE: This is a poem in 3 voices . . . each should be portrayed with a unique mannerisms, posture and voice. – Speakers are from Scotland, so some lines are written in that dialect.

• Red: Adoptive Mother (a white woman from

Scotland)

• Black: Daughter (a dark-skinned, bi-racial child --

adopted)

• Green: Birth Mother (a white woman from

Scotland who fell in love with a black man from

Nigeria)

*******************

I always wanted to give birth
do that incredible natural thing
that women do - I nearly broke down
when I heard we couldn't,
and then my man said
well there's always adoption
(we didn't have test tubes and the rest then)
even in the early sixties there was something scandalous
about adopting, telling the world your secret failure
bringing up an alien child,
who knew what it would turn out to be

I was pulled out with forceps
left a gash down my left cheek
four months inside a glass cot
but she came faithful
from Glasgow to Edinburgh
and peered through the glass
I must have felt somebody willing me to survive;
she would not pick another baby

I still have the baby photograph I keep it in my bottom drawer

She is twenty-six today my hair is grey

The skin around my neck is wrinkling does she
imagine me this way
I say to the man at the desk
I'd like my original birth certificate
Do you have any idea what your name was?
Close, close he laughs. Well what was it?

So slow as torture he discloses bit by bit my mother's name, my original name the hospital I was born in, the time I came.

Outside Edinburgh is soaked in sunshine I talk to myself walking past the castle. So, so, so, I was a midnight baby after all.

I am nineteen my whole life is changing

On the first night I see her shuttered eyes in my dreams

I cannot pretend she's never been my stitches pull and threaten to snap

my own body a witness leaking blood to sheets, milk to shirts

On the second night I'll suffocate her with a feather pillow

Bury her under a weeping willow
Or take her far out to sea
and watch her tiny eight-pound body
sink to shells and reshape herself.

So much the better than her body encased in glass like a museum piece

On the third night I toss I did not go through these months

for you to die on me now on the third night I lie

willing life into her breathing air all the way down the corridor

to the glass cot

The first agency we went to
didn't want us on their lists,
we didn't live close enough to a church
nor were we church-goers
(though we kept quiet about being communists).
The second told us
we weren't high enough earners.
The third liked us
but they had a five-year waiting list.
I spent six months trying not to look
at swings nor the front of supermarket trolleys,
not to think this kid I've wanted could be five.
The fourth agency was full up.
The fifth said yes but again no babies.

Just as we were going out the door I said oh you know we don't mind the colour. Just like that, the waiting was over.

This morning a slim manilla envelope arrives postmarked Edinburgh: one piece of paper I have now been able to look up your microfiche (as this is all the records kept nowadays). From your mother's letters, the following information: Your mother was nineteen when she had you. You weighed eight pounds four ounces. She liked hockey. She worked in Aberdeen as a waitress. She was five foot eight inches.

My eyes snatch pieces of news headlines strung out on a line: MOTHER DROWNS BABY IN THE CLYDE

November
The social worker phoned,
our baby is a girl but not healthy
she won't pass the doctor's test
until she's well. The adoption papers
can't be signed. I put the phone down.
I felt all hot. Don't get overwrought.
What does she expect? I'm not a mother
until I've signed that piece of paper.

The rhythm of the train carries me
over the frigid earth
the constant chug a comforter
a rocking cradle.
Maybe the words lie
across my forehead
headline in thin ink
MOTHER GIVES BABY AWAY

December
We drove through to Edinburgh,
I was that excited the forty miles
seemed a lifetime. What do you think she'll
look like? I don't know my man says. I could tell
he was as nervous as me. On the way back his face
was one long smile even although
he didn't get inside. Only me.
I wore a mask but she didn't seem to mind
I told her any day now my darling any day.

Nobody would ever guess.
I had no other choice
Anyway it's best for her,
My name signed on a dotted line.

March
Our baby has passed.
We can pick her up in two days.
Two days for Christ's sake,
could they not have given us a bit more notice?

I must stop it. Put it out my mind. There is no use going over and over.

I'm glad she's got a home to go to.

When I got home
I went out into the garden -
the frost bit my old brown boots –
and dug a hole the size of my baby
and buried the clothes I'd bought anyway.
A week later I stood at my window
and saw the ground move and swell
the promise of a crop,
that's when she started crying.
I gave her a service then, sang
Ye banks and braes, planted
a bush of roses, read the Book of Job,
cursed myself digging a pit for my baby
sprinkling ash from the grate.

Today I ring the counselling agency in Edinburgh. Can you start to trace through marriage certificates? It will take three weeks what do you expect from it. If she wants to meet me that's fine if she doesn't that is also fine

That night I turn it through till dawn
a few genes, blood, a birth.
All this bother, certificates, papers.
It is all so long ago. Does it matter?

She took me when I'd nowhere to go my mammy is the best mammy in the world OK.

Now when people say 'ah but
it's not like having your own child though is it',
I say of course it is, what else is it?
she's my child, I have told her stories
wept at her losses, laughed at her pleasures,
she is mine.

Maybe that's why I don't like
all this talk about her being black,
I brought her up as my own
as I would any other child
colour matters to the nutters;
but she says my daughter says
it matters to her

To be honest I hardly ever think about it
except if something happens, you know
daft talk about darkies. Racialism.
Mothers ringing my bell with their kids
crying You tell. You tell. You tell.
- No. You tell your little girl to stop calling
my little girl names and I'll tell my little girl
to stop giving your little girl a doing.

We're practising for the school show
I'm trying to do the Cha Cha and the Black Bottom
but I can't get the steps right
my right foot's left and my left foot's right
my teacher shouts from the bottom
of the class Come on, show
us what you can do I thought
you people had it in your blood.
My skin is hot as burning coal
like that time she said Darkies are like coal
in front of the whole class - my blood
what does she mean? I thought

she'd stopped all that after the last time my dad talked to her on parents' night the other kids are all right till she starts; my feet step out of time, my heart starts to miss beats like when I can't sleep at night – What Is In My Blood? The bell rings, it is time.

Sometimes it is hard to know what to say
that will comfort. Us two in the armchair;
me holding her breath, 'they're ignorant
let's have some tea and cake, forget them'.

Olubayo was the colour of peat
when we walked out heads turned
like horses, folk stood like trees
their eyes fixed on us - it made me
burn, that hot glare; my hand
would sweat down to his bone.
Finally, alone, we'd melt
nothing, nothing would matter
He never saw her. I looked for him in her;
for a second it was as if he was there
in that glass cot looking back through her.

Now my secret is the hush of heavy curtains
drawn.
I dread strange handwriting
sometimes jump when the phone rings,
she is all of nineteen and legally able.
At night I lie practising my lines
but 'sorry' never seems large enough
nor 'I can't see you, yes, I'll send a
photograph.'
I have had my grandmother's Highland number
for four months-now burning a hole in my filofax.

Something this morning gives me courage to close the kitchen door and dial.

My grandmother's voice sounds much younger 'I used to work ages ago with your daughter

Elizabeth, do you have her present address?' Sorry, she says, No, but one of the girls

will have it. She gives me another Highland number wishing me luck. What did you say your name was?

Thirty minutes later my mother's sister asks lots of questions - Where did you work?

How long ago was that? What age are you? Forty I lie. For a minute I thought ...

But if you're forty, you can't be.

I know she knows. The game's a bogey.

Actually I'm 26. I thought so love. I thought it was you. Mam knew too.

She just rang to warn me you'd ring. How are you? How's your life been?

I'll give her yours. She'll write. I'm sure you understand. I do. I do.

The Meeting Dream . . .

If I picture it like this it hurts less
We are both shy
though our eyes are not,
they pierce below skin.
We are not as we imagined:
I am smaller, fatter, darker
I am taller, thinner
and I'd always imagined her hair dark brown
not grey. I can see my chin in hers
that is all, though no doubt
my mum will say, when she looks at the photo,
she's your double she really is.

There is no sentiment in this living-room, a plain wood table and a few books. We don't cuddle or even shake hands though we smile sudden as a fire blazing then die down.

Her hands play with her wedding-ring, I've started smoking again. We don't ask big questions even later by the shore. We walk slow, tentative as crabs No, so what have you been doing the past 26 years. Just what are you working at, stuff like that.

Ages later I pick up a speckled stone
and hurl it into the sea,
is this how you imagined it to be?
I never imagined it.
Oh. I hear the muffled splash.
It would have driven me mad imagining,
26 years is a long time.

Inside once more I sip hot tea
notice one wood-framed photo.
The air is as old as the sea.
I stare at her chin till she makes me look down.
Her hands are awkward as rocks.
My eyes are stones washed over and over.

If I picture it like this it hurts less

One dream cuts another open like a gutted fish nothing is what it was; she is too many imaginings to be flesh and blood. There is nothing left to say. Neither of us mentions meeting again.

*[but we never did meet . . . and that’s OK . . . maybe she’ll write . . . someday ] *Transition – not in the original poem

It's surprising how often it crops
up; that he or she didn't know anything about it
and now who is he or she really
do they love who they thought they loved
et cetera. You've got the picture.
Mine knew. As soon as possible
I always told her, if you ever want to,
I won't mind. I wasn't trying to be big
about it - if that was me, that's how I'd be.
Curiosity. It's natural. Origins.
That kind of thing. See me and her
there is no mother and daughter more similar.
We're on the wavelength so we are.
Right away I know if she's upset.
And vice versa. Closer than blood.
Thicker than water. Me and my daughter.

I wrapped her up in purple wrapping paper
And threw her down the old well near here.
Years - she's been in my drawer
Faded now, she's not a baby any more
Still pitch dark. It didn't matter.
I know every bend. I've no more terror.

Her sister said she'd write me a letter.
In the morning I'm awake with the birds
waiting for the crash of the letter box
then the soft thud of words on the matt.

I lie there, duvet round my shoulders
fantasising the colour of her paper
whether she'll underline First Class
or have a large circle over her 'i's.

She took me when I'd nowhere to go my mammy is the best mammy in the world OK.
```

---

## IC-1751: The Afflicted Girls

- Title: The Afflicted Girls
- Author (byline): Nicole Cooley
- Work: Not specified
- Publisher: Southern Illinois Univ Press
- Publication date as stated: April 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1037
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nicole Cooley
ISBN: 978-0809323098
Publisher: Southern Illinois Univ Press
Date (Month/Year): April 2000
```

### Introduction (context only: never use it for content warnings)

```text
Wallace Stevens once observed that "poetry is a scholar's art." Nicole Cooley’s book of poetry entitled “The Afflicted Girls” melds both poetry and research to examine the events of Salem in 1692 from a variety of perspectives--the accusers', the accused's, bystanders'--those whose lives were forever changed by the accusations, trials, and executions. The Afflicted Girls by Nicole Cooley studies first, the accused witch, Tituba. Like the colored race generally and especially of the tropics, Tituba was a believer in the occult.
```

### Performance text (classify this)

```text
The sky is a palm spread open, sheltering nobody. An egg-yolk yellow moon floats over the cage of men in the middle of Bridgetown’s market: a display of runaway slaves. When I walk along the margin

of the beach, I don’t look at them. I don’t look at Gift of God, the waiting ship, its principal cargo salted fish, sugar, slaves. Instead I watch the water stutter against rocks.

In Salem, the New World sticks to my tongue
like wool. I can’t breathe
in the Reverend’s house. I can’t sleep
in the bed beside his daughter,
her flushed skin limned with sweat
in the cold room.

Each morning, Family Prayer, a circle of bowed heads as the Reverend explains the fallen world, this land infected by black devils.

Afterward I walk to the marsh to watch the water separating here from home. The sky shuts its fist.

In the dark, feel along the edge
of history’s body
to find the place in which local legend
becomes the truest story.

Touch the small, painful ache where myths originate. Rub your fingers on it like a scab.

TRANSITION We know that Tituba had been brought to Massachusetts from Barbados and enjoyed a reputation in the neighborhood for her skills in the magic arts. According to Charles Upham

(1867) The details of her statement cover nearly the whole ground of them. While indicating, in most respects, a mind at the lowest level of general intelligence, they give evidence of cunning and wariness in the highest degree. The Examination of Tituba

Court: Tituba what evil spirit have you familiarity with

Tituba: none

Court: why do you hurt these children

Tituba: I do not hurt them

Court: who is it then

Tituba: the devil for ought I know

The Reverend’s hand spreads open over my back.
He could reach inside
my body, drag words from my lungs,
force my silence out.

His fingers circle my wrists. His ribs lock over mine, press me against the pantry wall. His voice, pure threat. Confess.

Upstairs, his daughter spins and twists in bed, calls out my name.

Later I will hold her tightly while she shudders in my lap.

Court: doe you see who it is that torments these children now

Tituba: yes it is goode good she hurts them in her own shape

Court: & who is it that hurts them now

Tituba: I am blind noe I cannot see

Find the gap, the rip in the paper. Pull out the stitches. Stretch open the loops of thread.

Wait in the pantry, the garden where she once waited. Follow the path’s wet slate to the harbor.

Stand on the rocks and let go of the story. The body sinks to the soft ocean floor.

Here is the fallen world. Here is the village
where children choke and cry out
in their sleep, as her voice breaks
in the shore’s throat, as fiction spins into fact.

TRANSITION

Can the historians be trusted . . . are the facts as we know them truly facts or were they perhaps altered by well meaning Puritan ancestors to cloak the truth in mystery. After all, the ink fades quickly in “The Waste Book”

must always be recopied twice, the pen a shovel turning the earth’s surface, opening

the page to another version of history. In the meetinghouse a man corrects

church records, head bent to the paper that will offer us this past, this

story while at the end of another century a woman watches her study window

like a movie screen, her garden’s beds turning to torn, yellowed paper. She is ready

to erase her own story, cross out her voice, blur her words to nothing

but stiff ink. What relief, she thinks, to step outside her body, to leave herself, to transcribe the archive’s directions:

one or two words missing.
name illegible, possibly John.
name completely missing.
this whole last line has been struck out.

as if only the voices hold her own speech together, as if the voices cancel out her own.

In the other century, pages stack and settle as the man works alone all night, retracing

parish records like a repeated prayer:

August 28 by an Order from the Governor and Council was observed as a day of Fasting and Prayer, to seek mercy from God in relation to the present afflicted state of things in both Englands.

We should know the woman is all wrong when she calls the past an empty

plate she can rinse clean, snow-covered road she watches from her window.

No -- each page marks a plot, a burial ground, each word a seed needling the dirt.

TRANSITION

Joining Tituba as one of the accused was Dorcas Good, who had been seen by the girls flying around the countryside on her "pole," and who was sneaking into their bedrooms at night and biting them. A cunning witch, Dorcas Good must have been, and apparently wise beyond her years. When accused sorceress Dorcas Good joined her mother Sarah in Ipswich jail, she was only 5 years old. Nicole Cooley proposes a bleak future in the life of this young child in Torn, 1710.

Far from the thatched roof of my father’s house I lean into the wind swallow

cold in order to remember the glare of light on ice outside the jail’s window

Petition for Damages September 13, 1710
The humble representation of Will’m Good of the
Damage {torn}
by reason of the sufferings of his family {torn}
supposed Witchcraft
to remember Mother Sister while Father
waits in the house where I don’t

live waits at the table alone plates set along the edges for No Family

being chain’d in the dungeon so hardly used and terrifyed {torn} she hath ever since been very chargeable having little or no reason to govern herself {torn}

Now in these woods far from my father I live in this body that isn’t mine

O Roof O Field of Snow O Father’s Bone White Plate O Mother Sister

Fear seeps under the door of my father’s house to the place at the table where he writes

Out here I have the voice that I won back -- nothing but emptiness --

O No Family No Mother No Sister Dead
```

---

## IC-1752: After the Bowling Stopped

- Title: After the Bowling Stopped
- Author (byline): Thadra Sheridan
- Work: Rattle Poetry Magazine
- Publisher: Rattle Poetry Magazine
- Publication date as stated: Summer 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: LOS ANGLES, INDIANAPOLIS, CHICAGO, ASHLAND
- Teaser before the introduction: No
- Spoken words (computed): 652
- Already set (do not supply): none

### Source block (context only)

```text
Author: Thadra Sheridan
Book: Rattle Poetry Magazine
ISBN: N/A
Publisher: Rattle Poetry Magazine
Date (Month/Year): Summer 2007
```

### Introduction (context only: never use it for content warnings)

```text
Just broken up with your boyfriend? Just gone on a date and wonder why he/she never calls you back? Do you feel sad and lonely and just sit there not knowing what to do? It’s happened to the best of us. If there was only a way to fix this problem, so you don’t have to feel this way. Well, there is! Write it down! Create art! Author a poem! That’s what Thadra Sheridan did when nothing else seemed to work . . . “After the Bowling Stopped.”
```

### Performance text (classify this)

```text
Last night,
this guy played guitar on stage,
and it made me think of you, because
you play guitar on stage.
So I spent the next fifteen minutes
running a mental slide show.

LOS ANGLES: You gave me half of your egg salad sandwich.

INDIANAPOLIS:
You grab me, because
the smell of gasoline on my fingers
turns you on.

CHICAGO:
We play Ferris Bueller and
follow a kids’ tour group
at the Institute of Arts.

ASHLAND:
You bowl five strikes in a row.
Etcetera, etcetera…
I find this still happens a lot.
Someone’s wearing shoes, so
I think of you, because
you wear shoes.
You drink beverages.
YOU BREATHE AIR!
You can see how this might be a problem.
Sometimes I just
blurt your name out loud in my apartment
for no reason
like a Tourette’s outburst,
and I’m supposed to write this
poem about you,
because I keep saying I’m a poet.
And I’ve been trying
for the three years since you stopped
bowling in my presence, but it keeps coming out like,
I hate you, I hate you
I wish I’d never agreed to
date you.
or
The day you left,
the sun set for the last time,
the trees wilted,
and happy little creatures ceased to scurry.
or
My heart
is a block of frozen, solid, petrified, cold, really hard ice
without you.
or
I don’t need you.
Never did.
I CAN OPEN MY OWN PICKLE JARS!!!

Oh, I can write volumes
about every little
one-night-stand-pointless-encounter-waste-of-saliva
I’ve tried to replace you, but
you?
You’re drying up the ink in
all my favorite pens.
You’re hiding all my journals and
shorting out my keyboard.
You are the quintessential block.

You are the ultimate writer’s block, if…
No, wait, that one works.
The point is,
I know you can eat a whole egg salad sandwich,
but I appreciate the gesture.
And that stretch of 90/94
from Chicago to Rockford has
never been the same
since I drove it home from the end of time.
And when you stayed over this past spring,
you slept on the couch,
took a shower,
and left.
But it took me three days
to take your towel out of the bathroom
and five more to wash it.
I find I can’t really write about something
until I have a little
distance perspective, but you’re still
mashed up against me like a Siamese twin.
And the kicker is
I can’t even say I want you back.
You were all shades of fiasco.
I was only on your mind if I was
waving my arms in front of you.

And you only gave me the sandwich because you were
BEING SUCH AN JERK
So if you asked,
would I take you back?
Yeah I totally would.
And that pisses me off.
But if I was with you right now, I’d be
sitting in some hotel in New York,
getting my butt kicked at Scrabble, or
pitching a makeshift baseball game in
Gettysburg, Pennsylvania.
And my debt would be twice as ridiculous.
And I’d weigh a hundred pounds, because
you supplement eating and sleeping and
not in any good way.
But I wouldn’t be here.
I wouldn’t be
running my stupid life.
You are the rockstar me I’m
too impatient to wait for.
And you’ve got nothing to do with anything.
Most of my friends don’t even know what you look like.
So you’re all mine.
And a terrible kisser
and a really sore loser.
And I suspect you’ll
litter my life with
unfinished pages about the
empty spaces you
left in my apartment
for years to come.
And tonight,
when someone asks to borrow a guitar pick,
or uses the words,
and
or
the
I’ll think of you;
snapshot something somewhere
away from here and today.
Not much I can really do about that, just
thought I’d mention it, because
it was on my mind.
```

---

## IC-1753: The Andrew Poems (New Cutting 2/12/2024)

- Title: The Andrew Poems (New Cutting 2/12/2024)
- Author (byline): Shelly Wagner
- Work: Not specified
- Publisher: Texas Tech University Press
- Publication date as stated: January 1994
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1298
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shelly Wagner
ISBN: 978-0896723191
Publisher: Texas Tech University Press
Date (Month/Year): January 1994
```

### Introduction (context only: never use it for content warnings)

```text
It was the nightmare every parent fears. On a summer Virginia evening, Shelly Jones Wagner was pushing her five-year-old son in a tire swing in the backyard, idling away the hours between dinner and bedtime. She left him only for a moment, but when she returned Andrew had disappeared. He was found later that night, drowned in the river behind their home.

Shelly began writing to help her cope with the intense feelings of grief and loss. Her words were ultimately published in The Andrew Poems, a book of narrative poetry that has comforted and inspired thousands of parents and other determined survivors.

The Andrew Poems by Shelly Jones Wagner
```

### Performance text (classify this)

```text
(Pg 10-11) When I told the police I couldn’t find you,
they began a search that included everything,
even the boxes in the house.
They made me raise every lid.
I told them you would never stay in a box,
not with all the commotion.
You would have jumped out,
found your flashlight
and wanted to join the search.
Poor Thomas, leading men
who didn’t know us
through neighbors’ garages
where you never played,
hoping they were right
and we were wrong
and he would find you
and snatch you home by the hand
so the police cars would
get out of our driveway
and the divers would
get out of our river . . .
That’s not what happened.

(Pg 12-13) Near midnight,
your grandfather came into your room
where Thomas and I had waited.
He said you had been found
and they needed something to cover you,
not for the cold – it was summer,
not for your comfort – too late;
but to wrap the small, wet body
as with a shroud.
I grabbed your bedspread,
gave it to your grandfather.
He left your room
carrying your white spread
draped in his arms
like a child.

I’d rather remember you
wet from your bath.
After you wiggled into your pajamas
you would climb on the hamper
to see yourself in the mirror,
comb your wet hair straight back
and ask if that made you look famous?
With affirmations,
I would carry my legend to his room.

Had I gone outside that night, no one would have let me bathe you, wash the mud from your cheeks . . . You could not come back to your room.

But I wonder, did the river sweep your wet hair straight back and make you famous?

(Pg 36) A simple question,
Never a problem before.
“Do you have any children?”
Really a simple question.
Easy. I Say, “Yes,” but
What do I say to “How many?”

“Two,” my hard-headed
Heart always says.
One is dead.
Must I say only one?
Absolutely not – I have two
Sons.

[Memories of] Mice . . . (Pg 5-6)
A life parallel
behind our refrigerator --
a mother raising her two baby mice.
Her children played where they shouldn’t.

Thomas, my nine-year-old man-of-the house, set the trap with cheese. Three-year-old Andrew wandered in as we lay the loaded trap on the floor; I perched him on the kitchen counter with the impossible command, “Do not move.” Thomas and I armed ourselves with a mop and a broom and jumped up on the ledge with Andrew.

The babies sashayed down the alley
between the refrigerator and cabinet.
Like children on a jungle gym,
they climbed over the locking bar,
Slipped across the spring,
ate the orange cheese.
When they heard us laughing
the mice jumped off,
too small to trip the trap,
too young to know the danger.

Andrew went to his room,
returned with his toys.
He parked two Matchbox cars
in front of the refrigerator,
set up a tiny picnic table
with two chairs and an umbrella,
then set the table with cheese.

And Television (Pg 14-15)
He watched “The Young and the Restless.”at lunch,
eating peanut butter and jelly
with his grandmother
and “The Price is Right
was his favorite.
If I wanted him
to come in from the yard
all I had to do was call,
“Andrew Minton! Come on down!”
One day, in response to the silly summons,
he leapt into my arms,
clasped my face between his hands,
and planted a huge smooch
right on my lips.

He hopped down explaining, “That how they do it on the ‘Young and the Restless.’”

(Pg 41-42) I remember the funeral director saying,
“We have only two caskets for children.
They are four feet six inches long.
I know which one you will want.”

There it was – closed --
in front of the church --
blue, handsome, shiny, cold.
But I had seen the velvet cushions
at the funeral home --
clean, soft, silver.
We put stuffed animals
and poem all around you --
you lying there in the box
just longer than you.

(Pg 10) (echo) I told them you would never stay in a box, not with all the commotion.

(Pg 15) After everyone was gone
I walked to the river.
Standing there
I looked up at the sky
as one does when addressing the dead,
“Andrew Minton, come on down.”

(Pg 17) You drowned on Thursday.
We buried you on Saturday.
Your brother’s birthday was Sunday.
Someone brought a cake with twelve candles.
Your brother smiled bravely;
thanked everyone for their gifts,
Including the brightly striped beach chair
with a matching towel.
For a moment Thomas tried
to amuse us.
He wrapped the colored towel
around his shoulders
and sat in his striped chair.
He was a sight. Some laughed.
But to me it looked like Joseph’s coat
of many colors – proof that a son was dead.

(Pg 24 -25) After the death of my child,
I believed it possible
that clothing, toys, rooms,
even shoes
could become shrines.
I carried his little pairs of shoes
full of holes and memories
to the trash.
Hearing the garbage truck coming,
I made myself watch as the contents of the can
were tossed into the truck.
For weeks I had nightmares.
I dreamed of going to the dump
to search for them,
find them and bring them home.
The shoes are gone –

But not all of them.
Andrew, I kept my favorites:
my favorite teddy bear slippers
and your reliable red rubber boots.
Today, the shoes
are lined up in pairs
like left-facing and right-facing griffins
on guard under your mother’s bed.

I wish I had your loafers
with your lucky pennies in them.
You were buried wearing those.
(Pg 26) I put off buying him men’s clothing,
but for Easter
he wanted a tie – a red one
and a nav blue blazer.
Now, just under six years old,
he is buried wearing it forever --
as old a man as he will ever be.

(Pg 28) Someone offering comfort said,
“This will pass.”
I recoiled like a slapped child,
fearing if the grief were to fade,
I would be left with nothing.

[But] What If? (Pg 78) What if the divers had surfaced empty-handed? What if someone had found him just sitting in a tree. He would have been wide-eyed watching the flurry of lights He would have loved the flashlights of those on the shore shining in all directions like gleaming swords.

He would never have forgotten
the blue lights on the police cars swirling
like the moonlit wake of the rescue boat.
The boat’s searchlights and acrobatic divers
would seem to any child a circus act.
Had he jumped from the tree and come running,
the search would have been no more than a midnight

cruise, the black hearse would not have come for his body, the helicopter pilot could have killed his floodlight, the media would have abandoned their story, and his grandmother never learned from the eleven o’clock news that her youngest grandson was missing from our yard. Embracing him, would I have scolded him or covered him with kisses of sweet relief?

(Pg 15) (echo) “That how they do it on the ‘Young and the

Restless.’”

(Pg 78) Definitely kisses. probably never would have scolded him again at all. Would I have let him sleep with me?

He asked to every night at bedtime. No, that was not his place. His room was across the hall where I could see him. But he did drown and he is not in his room anymore. Since that evening when he did not come when I called:

(Pg 10) (echo) “Andrew Minton! Come on down!”

(Pg 78) Since that evening, every night – he is in bed with me.

(Pg 31) I lie down
pull the river up
around my ears . . .
how natural he looked,
how peaceful,
as though he were only sleeping.

(Pg 36) (echo) “Do you have any children?” Two. I have two sons.
```

---

## IC-1754: Angles of Vision

- Title: Angles of Vision
- Author (byline): Roseann Lloyd
- Work: War Baby Express
- Publisher: Holy Cow!
- Publication date as stated: May 1996
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 756
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roseann Lloyd
Book: War Baby Express
ISBN: 978-0930100681
Publisher: Holy Cow!
Date (Month/Year): May 1996
```

### Introduction (context only: never use it for content warnings)

```text
In this poem, Roseann Lloyd, addresses a very hidden and personal war, one waged internally against emotions. Emotions brought about by her brother’s suicide, her father’s abuse and her struggle to cope with life’s trial and tribulations. Despite the heart-breaking subject matter, Ms. Lloyd’s work as a poet has always been in honor of community, healing, beauty, and laughter. Her poems about incest have helped to heal a community of men and women whose fates delivered them into the wrong hands.... We all see the world through different Angles of Vision by Roseann Lloyd.
```

### Performance text (classify this)

```text
Tim O’Brien, author of The Things They Carried, perhaps explains it best: “In any war story, but especially a true one, it’s difficult to separate what happened from what seemed to happen... The angles of vision are skewed. When a booby trap explodes, you close your eyes and duck and float outside yourself . . . The pictures get fumbled . . . you tend to miss a lot. And then afterward, when you go to tell about it, there is always that surreal seemingness, which makes the story seem untrue, but which in fact represents the hard and exact truth as it seemed.”

when I'm walking it's
the movement that counts
thinking whatever
flits across my mind
the way a cat tracks
each purple shadow
catching the grass
& when I'm walking I let myself
think about the doctors
who thought my symptoms indicated a tumor
buried deep
inside my head the headaches the tunnels of dazzling
light
the weeping
breasts their hands wrapped my chest and legs in a
blanket
of lead a grasshopper's thorax I was held down like
when my father
was on top of me & my mind couldn't skip around
they turned my head
by the chin
like a lover positioning it so they could see
what was wrong with their pinpoints
of invisible light
& when I'm walking
I can see those x-rays they showed me mainly what you
see is skull
a chalky shadow something you think you don't get
until you're dead & bone clean dead & buried
like my brother
who got buried
the year before his hair was thick & curly
I never saw his skull I felt dead then
I couldn't think
about death couldn't say the word incest
which was buried
with all my feelings
held down by my
thorax
of symptoms headaches blinded vision weeping
breast milk no connection to anything
not even my moon my husband's body
heavy & remote
& he strange as my father my brother's gaunt hip-bones
graceful as a girl walking through
my mind all the days I couldn't get up
off the couch
& when I'm walking I can see the gone days those days
on the couch we lived in the mountains
then my husband's sunlit body didn't want any part of
maniacal fathers
dying brothers not any part of the truth I could only see
in the screen of nightmares glimpses
in the morning
light it was then
I started walking
walking the muddy
back roads across
the floodplain & up through the fat thistles of the
purple knapweed & up
even farther to the canyon walking up to the
cedars & pines
up to the cold
streams & with each step the headaches
receded memories came rushing in
like the cold water like the spring
floods swelling
the valley floor
& when I'm walking I let myself remember her that
young woman with downcast eyes
covered by the long blond hair-the woman
I used to be & I
welcome the remembering how I made her
say the words out loud in plain English without the
benefit of metaphor: my Father sexually assaulted my
body
my Father beat
down his sons
my youngest brother refused to fight in Asia but he
died from the Asian flowers blooming in his veins-
that's no metaphor that is the flower of addiction
what we thought was beauty was really pain:
don't tell the secrets
death rhymes with incest they're the family twins!
my father is a Gemini-
do you see how fast
I'm walking life back
into my scared stiff body that always did what it was
told & when I'm walking I can
even think about
all the dead weight
that kept me down
the thorax of
symptoms the doctors' bewilderment the rules
& threats in the name of love black-outs numb hands
nightmares hands & fists & silence & fear
of all of the above
& I'm not afraid any more when I'm walking
I forgive the men the violence their bodies
have expended on mine all their rage & grief-
I let them have
their lives & when I'm walking I let myself have mine I
let myself think
of my friends & my lover the men unafraid to look me in
the face unafraid
to see the damage
my brothers
I have to keep moving
& there's no more headaches even in the city I'm
walking up the canyon walking with my brother's lovely
hips up through
the knapweed up to
the purple lupine the fringed gentian the scarlet gilia
& on up to the shooting stars walking into my life walking
up the canyon I never
reach the end of
```

---

## IC-1755: Anorexia Rarely Begins with Bones – A Collection

- Title: Anorexia Rarely Begins with Bones – A Collection
- Author (byline): Blythe Baird
- Work: If my Body Could Speak
- Publisher: Button Poetry
- Publication date as stated: Feb 2019
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1124
- Already set (do not supply): none

### Source block (context only)

```text
Author: Blythe Baird
Book: If my Body Could Speak
ISBN: 978-1943735471
Publisher: Button Poetry
Date (Month/Year): Feb 2019
```

### Introduction (context only: never use it for content warnings)

```text
Anorexia rarely begins with bones. . . it begins with numbers: calories, pounds, minutes, and the quiet belief that hunger is an achievement. In the United States, *nearly 28.8 million people will experience an eating disorder in their lifetime. Yet the illness often hides in plain sight; less than 6% of people with eating disorders are medically underweight, meaning many sufferers are praised for the very behaviors that are harming them.

The poems in this collection move through that contradiction: the way starvation can be mistaken for discipline, the way praise can deepen sickness, and the slow, difficult work of learning that survival, not smallness, is the real measure of health.

Anorexia Rarely Begins with Bones – A Collection of poems from If My Body Could Speak by Blythe Baird
```

### Performance text (classify this)

```text
Relapse (Pg 70-71) Sometimes I miss being sick

The grimiest part of me wishes I had stayed In that familiar city of grey and mental illness and whatever the opposite of healing is where there was nothing to laugh about but plenty to write about

I've considered myself to be recovered
from my eating disorder for three years
But I still write about it in present tense
When a friend at dinner makes a casual
comment on calories, the scoreboard
in my head illuminates with numbers again.

For once, I don’t want to write
about this. For the first time, I am embarrassed
Instead of proud
of all the mad things I have done
for happiness.

Once I cut a ribbon the size I wanted to be and wore it around like my waist like a bracelet

Bathroom scales make me feel
nostalgic
Like a scrapbook,
I flip through snapshots of my sickness,
the suppers of tobacco smoke
and red lipstick
how I used to pack my lunchbox with
floss and teeth whitening strips
Sometimes, I still paint my nails
when I’m hungry. I can’t eat
until the polish is dry.

I don't want to go into more detail
because what if you mistake this poem
for an instruction manual?
I don't know how to talk
about the rabbit hole
without accidentally inviting you
to follow me down it

When the Fat Girl Gets Skinny (Pg 3-6) the year of skinny pop and sugar-free jello cups we guzzled vitamin water and vodka

toasting to high school and survival
complimenting each other’s collarbones
trying diets we found on the internet:
menthol cigarettes, eating in front of a mirror,
donating blood.

replacing meals with other practical hobbies like making flower crowns or fainting

wondering why I haven't had my period in months

why breakfast tastes like giving up

or how many more productive ways I could have spent my time today

besides googling the calories in the glue of a US envelope

watching America's Next Top Model like the gospel,

hunching naked over a bathroom scale shrine, crying into an empty bowl of Cocoa Puffs

because I only feel pretty when I'm hungry

if you are not recovering, you are dying.

by the time I was sixteen, I had already experienced being clinically overweight, underweight, and obese.

as a child, fat was the first word people used to describe me,

which didn’t offend me until I found out it was supposed to.

when I lost weight, my dad was so proud he started carrying my before-and-after photo

in his wallet.

so relieved he could stop worrying about me getting diabetes.

he saw a program on the news about the epidemic with obesity

says he is just so glad to finally see me taking care of myself.

if you develop an eating disorder when you are already thin to begin with,

you go to the hospital.

if you develop an eating disorder when you are not thin to begin with, you are a success story.

so when I evaporated, of course everyone congratulated me on getting healthy.

girls at school who never spoke to me before stopped me in the hallway to ask how I did it.

I say, I am sick. They say No, you are an inspiration.

How could I not fall in love with my illness?

With becoming the kind of silhouette people are supposed to fall in love with?

why would I ever want to stop being hungry

when anorexia was the most interesting thing about me?

so, how lucky it is, now,
to be boring
the way not going to the hospital
is boring.

the way looking at an apple and seeing only an apple, not sixty

or half an hour of sit-ups is boring.

My story may not be as exciting as it used to be, but at least there is nothing left to count.

the calculator in my head finally stopped.

I used to love the feeling of drinking water on an empty stomach

waiting for the coolness to slip all the way down and land in the well

not obsessed with being empty but afraid of being full.

I used to take pride in being able to feel cold in a warm room.

now, I am proud I have stopped seeking revenge on this body.

this was the year of eating when I was hungry without punishing myself

and I know it sounds ridiculous, but that sh** is hard.

when I was little, someone asked me

what I wanted to be when I grew up,

and I said

small

I Didn’t Always Salivate Over Skeletons
(Pg 8) I come over to play at my friend’s house
& a chandelier of bones answers the door.
I can see each careful metal detail
of her braces poking clearly
through the skin above her top lip.
she steps on a Wii Fit balance board
& her frame is so wispy
that the system cannot detect a body.
she & I used to be fat
together

We shared whole pans of brownies
while our mothers shared concerns
regarding our weight.
we understood the many ways
a mother’s shame
can haunt a daughter’s body.

an image of this friend at a waterpark in 7th grade is still imprinted in my mind:

she jumps, jangling her arms and legs in excitement. she looks exactly like the flat skeletons hung during Halloween when you yank the string at the top of its skull, causing its glow-in-the-dark bones to clink and clank like chimes.

for years after, this was the last moment I can remember seeing an emaciated body & genuinely feeling worry instead of envy.

Eat
(Pg 72) When recovery is not all yoga mats and tea
and avacados, it is work. It is remembering
that sucking on ice cubes does not count as
supper. Body, forgive me. It is not healthy
to drink so much water that your body
becomes a bathtub your organs float in
like loofahs. Body, forgive me. Trying
to ignore the caloric calculator in my head
is like trying to ignore television subtitles
and sometimes I just cant. Body, forgive me.
Killing yourself slowly is still killing yourself.
wanting to die is not the same as wanting
to come home. Recovery is hard work.
Not wanting to die is hard work. Every time
you asked if I was full I heard fat, but I am
trying too hard not to do that. I am trying
not to search for the nutrition label on the back
of a birthday candle box. I am trying not to dab
my pizza with a napkin. I am trying to stop doing
things that don’t make any sense. Body,
forgive me. I am trying. I am trying. I am
still trying.
```

---

## IC-1756: Are You a Good Witch or . . .

- Title: Are You a Good Witch or . . .
- Author (byline): Not specified
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 945
- Already set (do not supply): none

### Source block (context only)

```text
Author: Anna Sandy-Elrod
On-line Magazine: The Florida Review
https://cah.ucf.edu/floridareview/article/when-i-
am-dorothy-gale/
Publisher: University of Central Florida
Date (Month/Year): Unlisted
Author: Marisca Pichette
On-line Magazine: Strange Horizons, Issue 29
http://strangehorizons.com/poetry/are-you-a-
good-witch/
Publisher: Strange Horizons.com
Date (Month/Year): November 29, 2021
Author: Evan J. Peterson
On-line Transcript:
https://thebushwickbookclubseattle.com/wizard-of-
oz-inspired-poetry-from-evan-j-peterson-because-of-
the-wonderful-things-she-does/
Publisher: The Bushwick Book Club Seattle
Date (Month/Year): Performed at the 42nd annual
Northwest Folklife Festival. May 2013
Author: Amanda Gorman
On-line Transcript:
https://www.youtube.com/watch?v=BPOVo3_pyos
(Transcript available)
Publisher: YouTube.com
Date (Month/Year): November 26, 2024
```

### Introduction (context only: never use it for content warnings)

```text
In 1939 Frank L Baum’s book was forever captured on film in The Wizard of Oz. But it was more than the leap from black-and-white to technicolor that fascinated viewers. The question “Are you a good witch or a bad witch?” lives on in the canon of the Ozian world.

And yet the question itself is problematic. It forces a simplistic, binary view of people, ignoring the complexity of intentions and motivations. Even Dorothy struggles to answer. Instead replying “I’m not a witch at all.”

In Wicked (the book, the Broadway musical or the recently released movie), the question of good and evil is phrased a bit differently: “Are people born wicked or do they have wickedness thrust upon them?” For often what we perceive as wickedness is often rooted in pain, prejudice and misunderstanding.

Are You a Good Witch or . . . including the poems When I am Dorothy Gale by Anna Sandy-Elrod, Are You a Good Witch by Marisca Pichette, Because of the Wonderful Things She Does by Evan J. Peterson and Do Us Good by Amanda Gorman
```

### Performance text (classify this)

```text
Pichette, Evan J. Peterson, and Amanda Gorman

When I am Dorothy Gale by Anna Sandy-Elrod

The curtain comes crashing down
and there I am, ruby-footed and murderous,
doing it all for the bloated shadow
of a little man. How foolish I have been
again and again, poppy-cocked
and clumsy, letting the boom of a voice, the cast
of a giant, tease me into storming
the castle to take what I never lacked. What is
more incarnadine: the glitter of these
shoes or the myth of blood now on my hands.
I look at the man and he looks back,
the fury of being caught pinking his cheeks.
I am not the heroine, and I know that
too late. He has no power to give me, after all,
the fading of his theatrics, and if he did,
I understand he’d keep it. We all fell for green,
called it real. There’s no place like money.
There’s no seduction like a beast of sewn-up skins,
a cotton ball on fire, a thrown voice
that tells us what we want to hear. Which of us
escapes? He told the lie; I did the killing.

Are You a Good Witch by Marisca Pichette

Are you a good witch or a bad witch?

As if there’s an answer

earned, inscribed

in bubbles

reflecting an inverse

crown.

Whip-stitched into the lining
of that question I see good
and bad like rhinestones
dressing up inevitability.

Are you a (pause) witch or a (pause) witch? You are a witch.

I am a witch.

You are my witch and I

am yours.

We wave wands or
broomsticks, conjuring
stars or demons or cramps
waiting for diamonds to stop
houses from falling
on our heads.

No water for us, cup covered on the bar

iced coffee only,

to be safe to be dry to be
un-toxicated
un-blamable
inflammable.

Perched on the lip of a bubbling cauldron I’ve spent decades learning how best to melt.

How to slide out of sight
into the creases between the red light
and the green--
Sopping streets,
salt spraying
witches on car tires
witches on sidewalks
witches in oil puddles
witches staining heels
hems faces cuffs—

following instead of being followed, trailing in defiance of being trailed.

Witches melt from clubs to hearts to doorsteps, spreading dark spots to remind the world

that magic really does exist.

Because of the Wonderful Things She Does by Evan J. Peterson

Oh, Dorothy. You slap lions & defeat witches,

you help grown men
become kings,
you help fake
wizards get clean,
you dry their tears

on your gingham dress—big jobs

for an eight-year-old. The Scarecrow learned

to strategize, & the Tin Man always

loved, grieved
over crushing a bug.
& the Lion
ever had courage,
lacked only confidence

till Oz, the Great And Terrible Fraud, slipped him

a syrupy placebo. But you, Dorothy?

You never truly had the power to take yourself

home. Sure, the shoes— those silver, tap-dancing

teleporters, but they’re not yours. Home was always

beyond you, as you took care of marvelous men.

Men who don’t eat nor sleep but weep into your skirts—

ain’t that just like a man? (ain’t you too young to know?)

And of course there’s your curious habit of killing people

by accident. What Oz himself couldn’t do,

nor the Good Witch of the North. Pig-tailed assassin,

you freed slaves, Winkies & Munchkins,

a sort of reverse
John Wilkes Booth.
You kill with scrub water,
you kill with your house.
You kill

like a girl. & that humbug, that huckster, that flimflamming

grifter, that shuffler, that hustler, that swindler

duped you. Oz, that papier mache puppet head,

pressed you to kill. Here’s rope, so hang:

no hot air balloon ride on your bucket list.

Just cute shoes
to walk you back
to bleak, flat
Kansas: happy
dust-bowl,

Dorothy, you Not-Queen of Oz.

Do Us Good by Amanda Gorman

Are we
born wicked or
do we have wickedness thrust upon us?
Are we born bad, or brave?
There is a world we miss when we misbehave,
But we miss just as much when we misconstrue.
When we distrust what is different and detest what is

new.

History is written by the victors,
and villains are embittered by the forcible and the few.
But through how we live, our children learn:
What we earn when we're earnest
and what we forge when we forgive.
Only with a decency do we discover:
People are not born evil,
we are born equal;
Green,
not with envy, but what we envision in each other:
A sentimental mankind finding ourselves even in the dark.
There is a goodness that knows in our hearts,
No one is wicked at birth.
We are born to light the wick of the earth.
We are all that girl:
When something changes within us,
something changes in this vast world.
We will never be the same;
This feeling, fervid as a flame has a name:
Unadulterated loving;
Rushing,
Flooding.

Together we will stare down the emerald tower;
We will not cower.
We will not let our power take over us.
But let ourselves take back our power.
We won’t just say we're sorry now.
Rejoicify that we're glad and grateful just to be seen and

not listened to.
We'll dream, soar into the blue, rise up to a new reality,
Because defending the good is how we defy gravity.
So if you dare to find us, look to our West-turned eyes!
Everyone won't do good deeds.
But all deserve the chance to try;
To be understood as we should.
And if this they would mourn as wicked.
Then let this wicked do us
good.
```

---

## IC-1757: Ball and Chain Record Store

- Title: Ball and Chain Record Store
- Author (byline): Ellyn Maybe
- Work: Word Warriors, Pgs 242-250
- Publisher: Seal Press
- Publication date as stated: Oct 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1309
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ellyn Maybe
Book: Word Warriors, Pgs 242-250
ISBN: 978-1580052214
Publisher: Seal Press
Date (Month/Year): Oct 2007
```

### Introduction (context only: never use it for content warnings)

```text
Set in a soul-crushing California record store in the 1960’s, this poem captures a wild, fast-paced meeting between a quirky clerk and a "granola-eating" activist who refuses to use plastic bags. Their conversation quickly spirals into an exchange of "indie" credentials; but when the store manager demands the clerk stop chatting and perform her job like a mindless corporate robot, her new friend inspires her to stage a mini revolution, trading retail rules for a sense of wonder and radical empathy.

Even in a boring job, you can find "Hope" in a world that feels crushing. You, too, can choose to be a hero in bell-bottoms and party like it’s 1969!

Ball and Chain Record Store by Ellyn Maybe
```

### Performance text (classify this)

```text
(Pgs 242-250) Someone came into the ball and chain
record store I work at
and said no bags
a waste of plastic.

I said yes.

You must be a granola-eating, left-wing, dig-goth, post-modernist, watch a lot of Billy Jack movies, Arlo Guthrie type.

He said yes.

I smiled.

I dream of Tom Waits fingerpainting
lightbulbs on my holiday wreath
and I'm Jewish, pretty weird huh?
I celebrate Tiny Tim's birthday
with a parade of dancing deadheads
some who never sleep and some
who never go to the bathroom.

His T-shirt said have you hugged a rainforest today?

I said I love the planet but it's an unrequited love.

He told me babe, you’re bringing me down.

When I was born my first word was ohmmm....

In kindergarten I organized the pacifists
to demand we don't have to read
from Dick, Jane, and Spot books.
Too generic.

I demanded we get American Indians to talk about what's real.

And I gave them my nap mat
‘cause it's their land
and I gave them my peanut butter
and jelly sandwich cause
the buffalo have been murdered
and they need protein.

He blushed with passion and said tell me you.

Well, the first fifteen years of my life I thought Barry Manilow was a sex symbol.

Needless to say I got a late start at being one with the cosmic heartbeat.

He gave me one of those looks
like I better get this girl
some Jack Kerouac books to read fast
before she suffers the confusion
of not knowing there's other existences
besides the banal.

I put my hands on my hips and squealed
I read On the Road
and the letters of Allen Ginsberg to Neal Cassaday
and vice versa.

He said on Monday, Wednesday, and Saturday I'm a part-time Marxist.

He took out a beanie put it on his head and began to chant.

All of the sudden he began to sing the minimum wage workers' song

(not an actual song; make up the melody)
"the walls are full of faces
the minimalls are full of neon
the bitter bite the hands that feed them
the food is a mixture of bone, blood,
and snails
man is a cannibal."

I said wow! you are the sort of guy who says right on and really means it.

You probably only drink the milk
of socially conscience cows
who voted Crosby, Stills, Nash, and Young
for president.

He screamed, oh chick, my life changed in 1962 when I realized the Constitution was written without women, blacks, Indians, and poor white men in mind.

That was not okay.

I became the Jackson Pollack of feminism.

I threw paint of outrage everywhere.

I was a man who identified with Billie Holiday and Ernest Hemingway.

I was a traveler.

So what brings you into this
San Fernando Valley air conditioned
intellectually malnourished record store
with the exactlys?

We open exactly at 10:00 Close exactly at 10:00 No matter what our karma.

Damn it's so crass, you can't even rent The Last Waltz here.

He said I'm in a competitive mantra makers bowling league.

We have weavers, chess players,
avant-garde stamp collectors
and Hell's Angels.
Inventors all.

We bowl whenever the spirit moves us.

With any luck we'll be playing the New Age/lawyers/used car salesmen league again real soon.

Hippies and New Age people are like the difference between Bob Dylan and Bob Hope.

He smiled and said do you want to bowl?

We are definitely into strikes for the betterment of the worker.

We need someone who looks like she could walk into the woods and find incense without getting poison ivy.

You look like Van Morrison when you pout your lips.

You could be part of the father, son and the holy ghost *meshuganeh athletic league.

Besides I love you.

I started to weep.
Tears of Bas Mitzvah cake
and tears of being the last kid picked
for field hockey in gym class.

Authentic tears.

Nobody ever said all that to me before.

I guess I kinda do have Van Morrison's mouth.

Why hadn't anyone ever noticed?

I said I love you.

But every free moment I moonlight at Hairy Krishna Organic Coiffures and Tea Salon.

We use
no chemicals
no dyes
no sprays
no comb
no brushes

Hell, you look pretty much the same going out as going in.

He said what's a nice girl like you doing living in a Republican administration like this?

The manager of the record store comes over and says

You know the movie Fahrenheit 451?

Corporate has ordered us to burn it.

Get to it!

Don't give me your damn whimpering Joan of Arc eyes.

Lots of people would love to have your job.

I scream pig! PIG!

You give barnyard animals a bad name.

Cops are Pigs!

Intolerants are Pigs!

Bigots are Pigs!

Everybody who does it and says they're just doing their job is a Pig!

Everybody who does it to someone else knows what they are.

This is my first day at the record store.

I guess if they want to have a quiet complacent yes sir type of employee they ought to ask different questions on the application.

Like do you conform?

Like do you care this is a stolen land?

Like do you believe in playlists?

Like do you believe in yourself?

Do you mind waking up alone rather than being beaten up with fists?

Do you see the government is beating us up
as bad as a knife in our elbows
as bad as a slur in our ears
as bad as a rape
when we just wanted to be held.

And all they ask is
can you work part-time?
and what days can't you work?
and they say whom do we contact
in an emergency?

I said cause you need to ask that constitutes an emergency.

The hippie said my name is Hell's Bells but you can call me hope.

He said I dug you.

Now I dig your whole being.

It's strange,
No matter how many nights I wake up unhappy
there is still a possibility of rising
into a change so easily.

The outlaw lives in a world where when he sees a mirror he sees a hero.

And all heroes put their bellbottoms on one leg at a time.

Let's face it, How can you trust money when there are politicians' faces printed on it.

Money is sexist.

The only women on so-called American currency which is really Turtle Island to the Indians is Susan B. Anthony and they stopped making those real fast.

Is money worth killing for?

Is money worth dying for?

I ran through the store singing
about William Blake's eyebrows
and Walt Whitman's bellybutton
saying everything is alive
and everything is sort of adorable.

I took paperclips and gave them loving vegetarian families who needed someone.

I took the bathroom sink and gave it a hug.

I freed all the rubberbands!

And I said to all the plastic bags
I will never burden you
with films weighing you down,
Perry Como cassettes,
or even a piece of Jerry Garcia's beard.

Well maybe.

But I will never staple a bag for you brought love.

Most people tell me it was all the pop tarts I ate.

Some people tell me it was because I was a liar.

And I said I'm too honest to be anybody's best friend

But at times nobody believes this hippie ever even came by.

There are
no lingering peace signs
no incense
no tea bags

Yet I still can't even believe Abbie Hoffman is dead.

So my strengths and pains are in my sense of wonder.

All I know is I don't believe in wearing sandals and argyle socks together.

And when I needed it most, hope was here.

Change must not be too far behind.
```

---

## IC-1758: Barbie in Therapy

- Title: Barbie in Therapy
- Author (byline): Denise Duhamel
- Work: Kinky
- Publisher: Orchises Press
- Publication date as stated: March 1997
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1093
- Already set (do not supply): none

### Source block (context only)

```text
Author: Denise Duhamel
Book: Kinky
ISBN: 978-0914061618
Publisher: Orchises Press
Date (Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
Long before Greta Gerwig ever handed Barbie an existential crisis on the big screen – “Barbie in the real world? That’s impossible.” -- poet Denise Duhamel imagined Barbie as a perpetually smiling heroine who could barely name a feeling and who worried more about her therapy outfit than her trauma.

But after intense introspection led by therapist Dr. Midge, that once anxious doll becomes a raging, hilarious revolutionary, smashing her tiny appliances and shedding every fake accessory.

Duhamel’s Barbie poems deliver a sharp, witty prequel to the Barbie Movie’s awakening only messier, louder, and with far fewer musical numbers.

Barbie in Therapy by Denise Duhamel
```

### Performance text (classify this)

```text
BARBIE IN THERAPY (Pg 68-69) During the first visit, Dr. Midge asks Barbie to

relax and talk a little bit about her past. But Barbie, the quintessential people-pleaser, doesn’t know

how
to do anything but smile. She’s afraid
to tell Dr. Midge about the violence
of where she’s come from: so many rolling heads
just like her own tumbling down a factory conveyor belt.
Her first pain was her hair being sewn
with a needle onto her bald scalp.
She never had time for any kind of childhood.
Not quite an orphan, yet not quite part of a family,
Barbie finds she’s been given so little vocabulary
to talk about her feelings. Try, coaxes Dr. Midge,
tapping her pen on her pad. I feel . . . frustrated,
Barbie finally says, bursting into what would be sobs
If she possessed tear glands. What do I wear
to therapy? Barbie wants to know. Dr. Midge
recognizes her client’s question as avoidance,
but answers anyway believing in not pushing too fast.
Sweatpants are good, Dr. Midge says, or anything loose
so you can feel comfortable lying on the couch.
Dr. Midge asks Barbie to draw a picture of herself
to use as a springboard, something for them to talk about.
Barbie renders herself perfectly, just as she appears
on the packaging she comes in. Dr. Midge is thrown –
She’s used to having anorectics draw themselves as blobs,
or the heavier women scratching out little stick figures.
You are quite an artist, Dr. Midge praises, double-checking
to see if Barbie has included all her limbs.
I have a little pallet at home, Barbie says.
It came with an easel, smock, and beret.
Really? Asks Dr. Midge, interested. Barbie answers,

dejected,
Yes, but there’s no real paint, so what’s the point?
That must make you angry, coaxes Dr. Midge.
No real food in your fridge. No real hay
For your palomino’s western stable.
Barbie asks her shrink to explain what anger is,
and Dr. Midge suggests several good books.
She gives Barbie therapy-homework, asking her to punch
her pillows every night before she goes to bed.
Barbie writes out her first check, hoping
that just around the corner, she’ll get to the real issues
which are full and fleshy, and anything but plastic.

BARBIE IN THREAPY, PART II (Pg 80 Excerpt) Barbie is starting to become dependent on Dr. Midge’s every word. The patient asks her doctor: What should I do about exercise? Run in place each

morning or jump on my personal trampoline? In conversation with other Barbies, she often starts sentences with My therapist says . . . The other dolls notice she has a certain glow that she hadn’t had before, but Barbie’s sisters aren’t crazy about all her changes. She’s begun, every once in a while, to say no, not wanting to share her fantasy clothes because of something called boundaries. Barbies past

comes back
to her in flashes, like mini-deaths:
little boys poking their sticky fingers;
Pet dogs gnawing on her hands.
And just how is she supposed to feel about Ken?
Sometimes he’s a soda jerk, a book worm, a mere bowling

partner. Then other times she’s thrust next to him – he in a tux, she in a wedding dress . . .

BARBIE’S FINAL TRIP TO THERAPY

(Pg 86-88) There’s nothing wrong with me!
There’s something wrong with society!
Barbie screams, gutturally, the way human babies do
when they’re hungry. Over the months, her voice
has grown from tinny to raspy,
tentative to commanding, deepening every time Dr. Midge

comments
about Barbie’s newest breakthrough.
Barbie has learned that depression is nothing
but anger turned inward, so now, as she lashes
out towards the world, she giggles, too,
because the expulsion of energy feels so good.
If she were a lazier doll, Barbie would wait
for the world to change. Because
she is so well-preserved, she’d still look the same
one hundred, even two hundred years from now –
if that’s how long it takes to get the E.R.A. passed,
if that’s how long it takes for women to be safe on the

streets.
But afraid those days for her kind will never come
when the results of her activism seem slow or null,
Barbie wishes she could immediately skip over to the

afterlife – hoping Mattel’s manufactured her a toy-soul that isn’t sold separately. Never really having felt full-fledged suicidal, Barbie talks about this longing with her therapist on her last visit. Dr. Midge is reassuring – all great thinkers ponder what will happen after death. Dr. Midge is confident Barbie is ready to strike out on her own and recaps her patient’s psychological

accomplishments and growth, the doctor saying she’s learned quite a lot about herself as well. With a firm handshake, the two dolls

try
to say goodbye at the end of the hour, then fall
into each other’s less professional hugs.
Barbie will miss her shrink, but Dr. Midge, preparing
her client for separation, has taught her
to also include other women in her life.
Barbie’s begun hanging out with Lisa Sliwa,
The national director of the Guardian Angels.
The two will be interviewed for magazines, proposing all

men
who rape should be castrated. Barbie is sick
of taking cabs at night, of double-locking the back door
to her Furnished Glamour Home before she ascends the

spiral
staircase to her bedroom. She knows more women
go to see therapists than men, that more women
have been locked up in looney bins,
so a combination of history and current events
prompts her to smash her three thimble-size saucepans.
After her final therapy session, she crushes
her tea kettle that never learned how to whistle
with the pointed heel of her pump. She tosses
the toaster out of the picture window
of her Sweet Roses Living Room. Then, out
with the tasteless make-believe toast. Her poodle
and daisy apron, her MBA briefcase,
her Oscar De La Renta dresses. Sick of posing
as anything but herself, she’s even tired
of the oversized shirts she’s borrowed from Kin.
That same night, she takes a midnight jog, past her lawn
which looks as though it’s been set up
as a garage sale of fashion accessories. She’s naked
as the first day she was made in the factory,
as naked as Eve, as Lady Godiva, as naked as Jane
when she took off her animal skins
to escape the jungle and her bad marriage with Tarzan.
Barbie is as vulnerable as Cinderella
in that split second between her dissolving rags
and the instant gown her Fairy God Mother bestowed her.
```

---

## IC-1759: Because I am Furniture

- Title: Because I am Furniture
- Author (byline): Thalia Chaltas
- Work: Not specified
- Publisher: Viking Juvenile
- Publication date as stated: Apr 2009
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2110
- Already set (do not supply): none

### Source block (context only)

```text
Author: Thalia Chaltas
ISBN: 978-0670062980
Publisher: Viking Juvenile
Date (Month/Year): Apr 2009
```

### Introduction (context only: never use it for content warnings)

```text
We often hear stories from the perspective of those who are abused, but what does it feel like to be the one child in the family who is ignored, forgotten, and left feeling powerless to help the ones you love? What is it like to have no voice? Anke is the youngest of three siblings. Welcome to her life of silence . . . and bear witness . . . Because I am Furniture by Thalia Chaltas
```

### Performance text (classify this)

```text
I am always there. But they don't care if I am because I am furniture.

I don't get hit
I don't get fondled I
don't get love
because I am furniture.

Suits me fine. (pg 3)

Quiet and earnest, he is squatting in front of me. I hunch on the couch.

"I know you think you want to play volleyball.

--- aren't I already?

Competition creates a false sense of empowerment,

an I’m better than you euphoria

believe me. I know.
I wouldn't want you to get caught up in that,
the hunger for control over others.
When I was young blah blah blah blah

My eyes watch his thin lips moving against

each other in silence,
and I know
that Darren and Yaicha were right
when they once used our father to teach me the

meaning of the word hypocrite. (Page 51-52)

Dinner.

He knocked Darren onto the linoleum.

I don't remember his arm swing, just Darren and his chair -- eight tangled limbs on the floor.

No reason that I could see.

But my father picked up his reasons and his

plate and went to eat in the living room.

Darren picked up his chair and himself and we are now eating in customary ice-age silence. (pg 5)

His Anger stands alone
stands erect
in the
middle of the room.

We step gently around it, a terrifying totem pole bristling beaks, pinions, talons.

I can't remember when it started when firm hand

became

fisted liege

became

feral

tyrannical

rage

more important than

the rest of us,

but
it didn't used to be this way
and that
keeps us tied to him,
guessing,
teetering,
waiting,
while stepping around
his Anger
in the
middle of the room. (125-126)

He's losing it bad tonight,
the second time this week,
chasing Yaicha out of the kitchen
holding his chair over her head-

she cowers on the living room rug.

I am close behind mom, but it's not like I can ever do anything.

No one sees me.

Mom gets him to stop,

with taut and twisted face, open hands, before the chair comes down.

Yaicha runs.

He sits down, tired, and says to mom, "I'm sorry you had to see that."

Inevitable that he does it.

But he doesn't really want a witness. (page 19-20)

My Father,
Who Art Not in Heaven,
and never will be,
sometimes
doesn't come home
from work
until two a.m.

and for his own reasons goes to my sister's room

before he goes to his own bed.

I don't want to
hear
know
live here.

I am scared for her but I am so glad he doesn't

come to my room. (Page 39-40)

Little packet by Yaicha's bed

I've seen them before--

Marci takes the pill before school

laughing in the girls' room,

proof of her

extracurricular

activities

But I overheard Yaicha tell her friend she's a virgin,

never even had a boyfriend,

so I don't get it.

And she storms in snatches the packet raging about privacy.

Bubbling panic I go on the offensive –

"Why should you take the pill?"

My insides shred as she glares a full minute

and I stand my ground
wanting her to tell me
tell me
anything,

but when I see pain
forming
on her retinas
I decide I don't want to know.
I run. (109-110)

I mean, WHY can't she just tell on him? It's just words.

Just open her mouth and out come those words.

And then he'd be stopped.

Right? (pg 163)

Darren came into the kitchen
this morning,
black circles
around wavering eyes,
and he wouldn't look at any of us.

Mom said he was sick

but he's not sick. I've seen this a few times before

always after he and my father fight

and then my father "talks" to him in private

in his room for hours

but most of the time I don't hear their voices (page 146-147)

Why am I not good enough?

At least he loves Darren and Yaicha in some way

even if it's horrible, he shows them attention

and I am furniture
I get nothing
nothing
nothing
no
thing

or
at times I get
a knife-edge glimpse of
something scary.

I think that it is supposed to be good, that I get less from him

but I feel . . . worth less. (105-106)

. . . and i'm jealous!
with a sick
acidic
burbling
bile
i want what they have

as horrible
curdling
vile
as it is
darren and yaicha get more
than
me. (pg 235)

Yanking jeans over sweaty skin,
I come out of my room,
Darren comes up the stairs,
and our father comes from the bathroom,

a damp bath towel dangling

from forefinger and thumb.

"Whose." he intones at me in the hallway,

"is this?"

Darren holds out his hand. "Mine," he whispers.

Our father looks surprised. Did he think it was mine?

He breathes in, launches the offensive at Darren. "HOW MANY TIMES HAVE I TOLD YOU TO

HANG THIS ... "
louder and louder
words crushing together
in a piling roar
"YOU THINK YOU CAN JUST DO WHAT YOU

WANT ... " "I AM THE ONE WHO KNOWS WHAT'S GOOD

FOR YOU ... "

I want to make him turn to me yell at me

I want to yell at him

I am here

right here

I am not furniture --

But when his hand
smothers Darren's face with the wet towel,
shoving him hard into the wall,
I am backing away. (177-179)

Yaicha is crying gently in the bathroom. (pg 231)

It just occurred to me.

It's her choice.
Yaicha chooses not to tell anyone
and Darren does too
and Mom.

Am I the only one bothered by this? I mean bothered enough to think about it?

So all the pressure is on me,
the Youngest and Most Bothered.
Or maybe I am just
outside enough,
being the footstool observing from the corner,
that I have a view of reality.

And I can't stand it anymore.

Why me? I don't need this crap

Then why don't I tell on him?

If they don't, why don't I? Because.

Because I am safe this way, silent unnoticed.

Because my family would crack snap shatter

like pine boughs in an ice storm jagged pieces scattered, irreparable,

and there would be no family and I don't want that on my head.

What we have is better than that.

Right? (239-240)

TRANSITION

Confusion, feelings of worthlessness, fear . . . such strong feelings can only be locked inside for so long. A catalyst is all that is needed to force these emotions to the surface – It is then that the “furniture” finds a voice - - A branch can bend only so far before it breaks . . . And once Anke develops a friendship outside her family, Angeline becomes that catalyst and Anke finds her voice.

"Your father must have
info like that."
Angeline is at me
again.

Mom is making me work with her on topics for government

"He must have
books and books,"
Angie is pleading.
"He's a professor."

I'm not asking him for anything.

I want to say,

Get over your goddamn crush,

Angie,

you have no idea

who he is. But my jaws clamp.

" I'll call him." she offers.

Well why not? She's already more a part of my family than I am. (266-267)

I am annoyed
when Angeline comes,
clutching her pale pink sweater,
breathlessly spilling
that we could pick up government law info
at my father's office.

"He said 'Sure’” she squeals.
He’ll leave a folder on his desk because,
sigh,
"he might have a meeting."
She is is briefly bereft.

I say I’ll meet her in the lobby

"Oh, I told him I'd go, I don't mind."

Grrrr.
He is my father.
"No, I'll meet you," I throw at her
retreating back
but she's gone.

"Why don't you just frickin' move in with us,"

I say out loud.

I'll be glad when this government thing is over, this annoying extracurricular supposed honor that forces me to spend even more time with Angeline. (300 - 301)

I'm a little late getting to my father's building.

I scan for Angeline in the lobby then sprint up the three flights. Coming to the DR. LARUS FELD etched on his

frosted door,
Tapping lightly,
turning the knob,
the door swings in silence, fangs of light

glinting in the glass.

Then I hear -- I hear something soft crying somewhere.

Angeline?

Sneakers on carpet,

carpet,

carpet,

lean around the bookcase. –

My
father with a small smile
leaning toward the armchair,
zipper on its way clown,
Angeline, her skirt tweaked,
swelling closing one eye,
pleading softly, no, no.

"NO!"
Dr. Feld is shock still.
I take another lungful,
"NO!"

Angie slides to standing,

gathering her book bag,

running for the exit. Raising brows, he mocks me, but, dammit, he will hear me,

"NO!"

Slamming by the bookcase
tearing through the doorway
pounding down the stairwell,
no-no-no-no,
NO--NO--NO. (302-304)

By the brook
with a crunch of fine ice,
I double over,
dry heaves
on my knees.

What did I see? What did I see in his office?

How could he, to poor Angeline?

I sink onto a rock near the water,
taking a blood-red
maple leaf
and dunking it under,
holding it beneath the frigid liquid.

Poor Angie.

She was supposed to be outside our

house of horrors
and I let her in.
I should have kept her away from him.
He went outside.

And the tears burst through
heavy as mercury,
heated by guilt,
and I take the leaf out of the water,
sobbing.

Angeline, Angie, I'm sorry (306-307)

Pushing open the bathroom door I take two steps toward Yaicha who is wrestling with her hair.

"I saw him hurt Angeline."

The brush stops moving.

"At his office today." Small sounds

like a dying cricket come from Yaicha's lips. “I’m sure you were mistaken." she says

to her brush.
"MISTAKEN?
I know who Angie is, Yaicha.
I know who our father is, Yaicha.
He hurts people, he hurts you,

you never do anything!" My claws scrape the wall paint.

She turns with soft rabbit eyes. "He'll kill me."

"He's already doing that!"
I am growling, grabbing her sleeve,
"Every day,
every day he rips you open,
chips off pieces week by week,
till a few years from now you are not even a

mouthful of sawdust.
A drawn-out killing.
Well, I'm tired of all of us doing nothing.
He has to be stopped."

Yaicha's eyes have flinched a few times but soften again. "Nobody can stop him."

"Nobody can stop him?
Good.
To him I have always been
Nobody." (311 - 313)

They all swivel to me -- Mom, Darren, and Yaicha --

Footfall, Darren frozen, eyes on the baseboard, Yaicha melted against the stereo cabinet, as he steps lightly up the stairs.

"Sorry I couldn't give you
a ride home,"
he says to me,
sliding into the living room
with his briefcase,
"I had a meeting.”

His eyes dare me. Dare me. (319-320)

Slow motion twitching

twitching

hissing burning

blood pushing

itching skin

pushing out

something scary

pushing out something stronger.

(321)

I stand behind his chair. "Liar,"

under my breath.

His eyebrows rise,

pupils sharpen.

"You weren't at a meeting,"

take a breath, gain speed, bursting,
"You were with Angie in the office.
I saw you. I saw you.
You clamp us down,
you think no one knows.
You hurt my brother! My sister!

You hurt my friend! Small trusting prey, huh? You could have chosen to hurt me!

But I'm not worth enough I never am

and you picked poor Angie,

you were going to RAPE her,

I SAW YOU TRY TO RAPE ANGIE,

you f***ing MONSTER!"

I shove his chair forward

with the force of my words,

the wooden leg touches

his foot.

Stillness. Shaking.

White-faced, cold,

slowly

he picks it up by the seat.

Suddenly spinning the chair in air

he smashes it on me hard –

with a great crack
I go down,
splinters of wood
splinters of bone
my leg showing bone,

and finally I roar. (322-323)

Where is the safe, cuddling daddy who sang “I’m Being Swallowed by a Boa

Constrictor" to me

when I had a fever?

Was that man molted off
like scales that no longer
lie smoothly
around the shape of what he has become?

I want my daddy back.

Too bad for me. (316)

He's been arrested.

In jail.

Such an odd disconnect

to feel so relieved and so guilty,

yet so cold about the whole thing, like concrete, like a nuclear reactor decommissioned

and left by itself to withstand the

winter.

I wonder if he has to wear one of those

bar-striped suits. (329)

I did it.
I filed
a restraining order
against
my own father.

He's out on bail and needs more than restraining.

But it's
a damn good
start,
and
I did it. (331-332)
```

---

## IC-1760: Bitter Creek Junction

- Title: Bitter Creek Junction
- Author (byline): Linda Hasselstrom
- Work: Land Circle
- Publisher: Fulcrum Publishing
- Publication date as stated: Nov 1991
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1362
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
All cruelty springs from weakness. The philosopher Seneca made this observation more than 2,000 years ago and still it rings true today. As women we are physically weaker than our male counterparts and for an incomprehensibly large portion of our society, this weakness spontaneously combusts into cruelty in the form of domestic violence. In a country where the amount spent to shelter animals is three times the amount spent to provide emergency shelter to women from domestic abuse situations, it is little wonder that women are forced unthinkable survival strategies. Want to know more? Travel with me to Linda
```

### Performance text (classify this)

```text
As usual, the shortcut proves
longer than the map promised.
I cross the railroad tracks
and nothing looks familiar anymore
I dry my forehead on my sleeve.
Clench my jaw, teeth grinding grit.

How long has it been? Not long enough. Two men in a beat-up white sedan once followed me on the interstate. They passed a dozen times, edging closer. When I drove fast, hoping to flush out a cop with radar, they kept pace, easing ever closer. For miles I looked for a ranch house, gas station, any place I might find help or haven. Side by side we raced along the highway, doing eighty. The fender of the white car grazed mine as they passed again.

I’d had enough. The driver dropped back beside me once more, smirking while the other man whooped, “Pull over, honey!” I laid the barrel of my pistol flat across my steering arm, and watched his tires. One inch closer and I’d pull the trigger. No need to aim. The white car shot away. Years later I still grip the steering wheel, remembering, my knuckles white.

Hasselstrom’s Bitter Creek Junction.

Rattling on a pole, a crumpled sign
announces, “Gas Bar” beside a fuel pump’s
broken concrete base. I stand
in waist-high weeds to fill the tank.
Three beat-up pickups nose against the wall,
boxes full of chain and oily rags.
A skinny cat slumps at a corner.

I step through the open door and pause,
dazed by the dark inside, the smell
of beer gone flat, spoiled food.
The place is half groceries, half saloon.

“Git out of her way!”
A gaunt man shoulders me aside
to slap a toddling girl.
He grabs her arm, and shakes her
while her dark eyes reach for mine.
“Pay attention when I talk to you!”
He yanks her hair to make her face him.
“How much?” he says. Shoves the girl away.
“I’m talkin’ to you, Blondie. How much gas?
I don’t have no way to know that
from in here.”

“Nine fifty-five,” I say, and notice
the woman in the gloom behind the bar.
She sets beer before three men,
who turn their head to look at me.

Her long dark hair hangs straight,
not hiding bruises on her eyes and cheeks.
She takes the bill I give her,
hands me coins in change and never
once looks up. The child clings to her skirt.

At the bar, one man elbows another,
spins around to leer at me,
his legs spread wide. He grins
and scratches slowly. “Saturday night!”
one says. “Time to party!”
The jowly one points his bottle at me,
yelps, “Party enough for all of us right there.”
I yank my cap low, getting ready
for the ceaseless prairie crosswinds.
I plant my feet apart and take the time
to squint and glare at every man.

Cans and bottles rattle in the back room. The man yells, “Yer brat’s been drinkin pop again, squaw. I’ll tan her hide!” The three men laugh.

The child stands at my knee, looking up. I dig for the ten in my pocket as I kneel. “You’re a good girl,” I say, and slip the folded bill into her muddy little hand. Smoothly, she makes the money vanish without a glance behind her.

I grip my car keys like a weapon
in my right hand, open the car door
with my left. I turn the ignition
while I shift, and the men inside stand up.
I spin the steering wheel and gun it,
clang gravel off the signs and pickup windows.
One tough woman howls a challenge
from my stereo. Roaring up the access road,
I drop between two trucks,
lock the needle at eighty-five.
I keep up with the convoy
while I watch for headlights
to follow me from Bitter Creek.

Bonnie Raitt joins me running west.
She rides shotgun, crooning songs
of freedom, blues about the men
who have abused and left us all,
and what we hope will happen to them.
While my car burns the costly fuel
from Bitter Creek, I sing so loud
I know I’m trying not to think,
don’t want to guess how many times
she’s been called a squaw.
I want to pray for that woman,
for the child, even for the man.
Sisters! Pray for the souls of the damned,
but teach your daughters to be brave.

As I drive a shaft of light
across that black and stony plain
I brood about the woman and her daughter.
I know some deer hunter
may one day stumble on their bones
scattered in an icy gulch.

I grind my teeth and dream revenge,
test the polished edge of rage against my fear.
I chase the sunset’s light,
carve a path through shadows,
leaving tracks I hope that she will follow.

************************************************** *********

A woman must be smart
to survive, must understand
when her time has come.
She can’t take more abuse
than her daughter can stand.
Already the child’s eyes are dim.

While she plans defection,
a cunning woman will pretend servility,
endure the snickers,
endure the men who prod and pinch
with eyes and fingers.
When he slaps her while they watch
she won’t grab the scattergun under the bar.
She’ll scurry. Bend. Think.
Not yet. Not yet.
Still, in a land of drunken homesteads,
dead-end roads and desert dust,
a woman often learns
she’ll have to help herself.

She might spread old blankets
over the couch, cast them wide and thick.
When he staggers toward their bed,
she could tell him it’s her time of month,
wave him toward the other room.
Steady and sober, she’ll tuck
the child in early, close the door.
Then wait. Wait until he snores.

She might ease from the covers,
slide her feet over the floor
to keep the loose board quiet.
Put on a pair of his gloves.
Take the big moss agate from the shelf.
Tie a towel around it.
Make knots to fit her hands.
Swing the weight to test
its mass against her arm.
Standing by the couch, she’ll breathe
deeply of his sweat and smoke.
Steady herself. Swing.
Strike between the eyes.
More than once. Then stop.
Push his stench out of her lungs and
listen for his breath. She won’t
take time to sob or stare.
She’ll drop the rock beside his head.
Wrap the blankets tight.
Without a light, she’ll drag him to the pickup.
Drop the tailgate, haul him up.
Cover him with his own tarp,
still bloody from the last poached deer.

Be sure he has the shovel he used
to bury the guts.
Gloves on, headlights off,
she’ll pick a dirt road
pounded every day by a hundred pickups
headed for an oil field or a trona mine.
She knows the roads.

She’ll drive deep into the desert,
come home before the day dawns red,
nothing but a shovel rattling
in the truck’s bed. Park his truck
the way a drunk would leave it,
sleep sound beside her child.
At daylight she’ll inspect the couch,
the ground around the door,
the pickup box. If she sees blood,
she won’t wash it out– he wouldn’t.
Maybe she’ll do as he did every fall,
shoot a dozen of the starving cats,
throw them in the pickup box
to swell and stink until she hauls
the weekly trash out to the rubbish pile.
If anyone asks about the man,
she’ll stay in her familiar shadow.
Shrug. Say little. She didn’t notice.
She closed the bar, went to bed
as usual. He was drinking
with some woman, some drillers,
roughnecks she never saw before.
Didn’t come to bed. That's all she knows.
She won’t mention the bruises
on her face, on the child’s arm.
They’ve all been here to drink
when he was slapping her around.
She’ll run the bar the way she always did,
add the money to her hideout cash.
Stay out of trouble. Maybe move
next summer. Find some place
where she can walk in sunshine
with her daughter,
humming an old blues tune.

—written for the battered woman at the place I call Bitter Creek for her protection.
```
