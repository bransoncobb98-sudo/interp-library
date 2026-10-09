# Classification request: batch 35 of 53 (40 records, IC-1761 to IC-1800)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-035-reply.json`.

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

## IC-1761: Black Mother Praying

- Title: Black Mother Praying
- Author (byline): Owen Dodson
- Work: Black Voices: An Anthology of African-American Literature
- Publisher: New American Library Classics
- Publication date as stated: April 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 741
- Already set (do not supply): none

### Source block (context only)

```text
Author: Owen Dodson
Book: Black Voices: An Anthology of African-American
Literature
ISBN: 0451527828
Publisher: New American Library Classics
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
In this selection a mother, examines the negative situation that her sons will face as they return home from war. Through her examination of the society in which she lives, she uncovers the powerful contradictions found in a racist society during wartime. She is very outspoken in her awareness of the unfair treatment of black soldiers who are sent overseas to guarantee freedoms in which they do not even have at home. Her out lash at the severity of racism at home is the significant base for her dissent and examination of her own son’s purpose and role in war. She correlates racism directly with “hate” and shows how there isn’t any real freedom where hate abides. Black Mother Praying by Owen Dodson is dedicated to Negro mothers everywhere and especially to his own mother, Lillian C. Dodson
```

### Performance text (classify this)

```text
My great God, You been a tenderness ta me,
Through the thick and through the thin;
You been a pilla ta my soul;
You been like the shinin light a morning in the black
dark,
A elevator ta my spirit
Now there’s a fire in this land like a last judgment,
And I done sat down by the rivers a Babylon
And wept deep when I remembered Zion,
Seein the water that can’t quench fire
And the fire that burn up rivers.
Lord, I’m gonna say my say real quick and simple:

You know bout this war that’s bitin the skies And gouging out the earth. Last month, Lord, I bid my last boy away ta fight. I got all my boys fightin now for they country. Didn’t think bout it cept it were for freedom Didn’t think cause they was black they wasn’t American; Didn’t think a thing cept that they was my only sons. And there was mothers all over the world Sacrificin they sons like You let Yours be nailed To the wood for men ta behold the right.

Now, I’m a black mother, Lord, I knows that now, Black and burning in these burnin times.

I can’t hold my peace cause peace ain’t fit ta mention
When they’s fightin right here in our streets
Like dogs – mongrel dogs and hill cats.
White is fightin black right here
Where hate abides like a cancer wound
And Freedom is writ big and crossed out:
Where, bless God, they’s draggin us outta cars
In Texas and California, in Newark, Detroit,
Blood on the darkness, Lord, blood on the pavement,
Leavin us moanin and afraid.
What has we done?
Where and when has we done?
They’s plantin the seeds a hate down in our bone marrow
When we don’t want ta hate.

We don’t speak much in the street where I live, my God,
Nobody speak much, but we thinkin deep
Of the black sons in lands far as the wind can go,
Black boys fightin this war with them.
We thinkin deep bout they sisters stitchin airplane
canvas
And they old fathers plowin for wheat
And they mothers bendin in wash tubs,
They brothers at the factory wheels.
They all is bein body beat and spirit beat
And heart sore and wonderin.

Listen, Lord, they ain’t nowhere for black mothers ta
turn.
Won’t You plant Your Son’s goodness in this land
Before it too late?
Help these men ta see they losin while they winnin
Long as they allow theyselves ta lynch
In the city streets and on country roads?

When can I pray again,
View peace in my own parlor again?
When my sons come home,
How can I show em my broken hands?
How can I show em they sister’s twisted back?
How can I present they land ta them?
How, when they been battling in far places for freedom?

Better let em die in the desert drinkin sand Or holdin onta water and shippin inta death Than they come back an see they sufferin for vain.

I done seen a man runnin for his life, Runnin like the wind, from a mob, ta no shelter. Where were a hidin place for him?

Saw a dark girl nine years old
Cryin cause her father done had
The light scratched from his eyes in the month of June.
Where the seein place for him?
A black boy lyin with his arms huggin the pavement in
pain.
What he starin at?
Good people, hands up, searched for guns and razors and
pipes.
When they gonna pray again?

How, precious God, can I watch my son’s eyes When they hear this terrible?

How can I pray again when my tongue Is near cleaving to the roof of my mouth? Tell me, Lord, how?

Every time they strike us they striking Your Son; Every time they shove us in, the cornerin they own children. I’m gonna scream before I hope again. I ain’t never gonna hush my mouth Or lay down this heavy, black, weary, terrible load Until I fights ta stamp my feet with my black sons On a freedom solid rock and stand there peaceful And look out into the star wilderness of the sky And the land lyin about clean, and secure land, And people not afraid again.

Lord, let us all see the golden wheat together, Harvest the harvest together Touch the fullness and the hallelujah together.

Amen
```

---

## IC-1762: The Black Tactic and 10 Things I Want to Say to a Black Man

- Title: The Black Tactic and 10 Things I Want to Say to a Black Man
- Author (byline): Marion Amponsah and Jennifer Falu
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 840
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marion Amponsah
Book: Part Three: A Selection of Poems from The
American Poetry Review's High School Program,
Young Voices
ISBN: Magazine
Publisher: American Poetry Review
Date (Month/Year): July 1, 2008
Author: Jennifer Falu
ISBN: 978-0978969592
Publisher: Penmanship Books
Date (Month/Year): April 2009
```

### Introduction (context only: never use it for content warnings)

```text
To have a good life, do you have to be white? Sometimes it seems so. . . Black and brown men are regularly stereotyped, silenced, and blamed for the oppression they face. And while any person with a shred of common sense knows that using the “N” word is not socially acceptable today, many words act as substitutes for the slur that has come to define race relations in America. These words and phrases are united by a hurtful message: Black people don't deserve to be treated with respect – they are and will always be the “other.”

Thug, Inner-city, Ghetto, Oreo, Uppity, You people, Shady – all just words that have become America’s coded language drowning in a sea of negative stereotypes. And often times, left with few alternatives, black males are pressured to adopt . . . The Black Tactic by Marion Amponsah
```

### Performance text (classify this)

```text
The Black Tactic
Black males are often pressured and blackmailed by black
males to act black.
To re-enact a lack of intelligence and beauty
But in turn fills the brain with that of being negligent and
moody
The black tactic
Enact a crack addict with bad habits

Days later his back is in a jacked casket
That's what the blackmail sells
Not to mention almost endless years in a jail cell
They fail well

It’s the white man’s fault they blame and phrase well
They will never be independent
They will never be able to manage
They will never be able to speak proper English
Slang their disabled language

Bang, Bang, Bang, the shots are definitely capable from
these black savages
Bandages loosely put on
Just years ago they were struggling with hardships but they
still face challenges
Bad their behavior never good
Shooting Hustling Killing
They all live in ghettos
They all live in projects
They all live in bad neighborhoods
Always the last
They remain in lower class

Confliction their nerves clash
Addiction to herbs and grass
From success exclude blacks
Their welfare is wrecked
Support from the government

Food stamps and welfare checks
Brains frail with no respect
Assured to be black is a much scarier life
They have thrown away their future burying light
Is this automatically a barrier?

To have a good life I have to be white.
Why not reject the role or the character
Tell the directors
To live positive my skin doesn't have to be light or white
Acting black is impossible
It doesn't require becoming a Ghetto, Imprisoned, Violent,
Crack Addicted, being
Those are just the stereotypes!

TRANSITION In 1963 . . . . Martin Luther King spoke these visionary words: “I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin, but by the content of their character” 40 years later . . . have we achieved his dream? We’ve made progress . . . yes, but there is still so much negativity and criminal suspicion associated with being a black male. Skin color, for a black man, is like a personal prison, something he has no control over. No one should be made to feel ashamed of being a black man – As Dr. King lamented over 40 years ago . . . each man should be judged based on the content of his character, and not just based on the color of his skin. 10 Things I Want to Say to a Black Man by Jennifer Falu.

10 Things I Want to Say to a Black Man One, I wish I could place your arms in a box.

For those long winter nights where the warmth of a blanket just isn’t enough.

Shop online for the cheapest time machine.

Travel back to a time where you were respected.

Back to the beginning where God used your rib to create woman.

Two, your eyes tell a story that you hide behind Stunnah Shades.

Your ears, hidden behind Beats.

While girls are screaming for your attention wearing mini skirts, and tops that expose their wombs to a world that doesn’t care about their babies.

Three, I apologize for the Soulja Boys, Chris Browns, and Wakas

Who call women materialistic female dogs, think it’s okay to hit them, and thinks being hoodrich makes them real men.

I honor you, for standing up for what you believe in,

Especially since the rest of the world’s belief system is slightly skewed.

Four, your voice is like thunder, sharp, with a low rumble, as though demanding the attention of the closest ear.

Five, I’m sorry for the women who make you feel like less than a man.

Many of us compare you to the type of men who’ve abandoned us.

Six, you’re beautiful, so beautiful that no female could ever take your place.

In a time where women have given up on you,

Just remember you were created in God’s image.

So I look to you, and I see God’s face

through eyes of a woman who shares your rib.

Seven, when I was born my father held me in the palm of his hand.

I admire you hands, they hold the secret to strength and peace.

Strength in the scars from years of hard work.

Peace in the gentle way you hold the women that you love.

The same strength and peace that God had when he molded you.

Eight, when we get married, I’ll mow the lawn, to show you just how much I disagree with the normal flow of things.

Forget about the grass allergy that would attack my immune system.

Let my love for you be the antihistamine that counteracts against the stereotypes.

Nine, my son will know his father from birth.

There’s nothing more heartbreaking than a child who suffers from an absent father.

Not because he’s absent minded, but because the mother is absent hearted.

Ten, never let anyone tell you that you’re less than amazing.

Our families need you more now than ever.
```

---

## IC-1763: A Black Woman Speaks of White Womanhood

- Title: A Black Woman Speaks of White Womanhood
- Author (byline): Beah Richards
- Work: Nine Plays by Black Women
- Publisher: Signet
- Publication date as stated: Aug 1986
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1567
- Already set (do not supply): none

### Source block (context only)

```text
Author: Beah Richards
Book: Nine Plays by Black Women
ISBN: 978-0451628206
Publisher: Signet
Date (Month/Year): Aug 1986
```

### Introduction (context only: never use it for content warnings)

```text
Beah Richards is best known as an American actress. Born in Vicksburg, MS, in 1920, Richards studied at Dillard University in New Orleans before pursuing an acting career on-stage in New York City. A Black Woman Speaks: And Other Poems was published in 1974 as a collection of 14 poems. In the preface to the book of poetry, Richards spoke of the need to "see how it is that blacks and whites agree so little culturally." Her views on the impact of a segregated society and on the prejudices against women are clear in her verse. She speaks to white women, urging them to remember "history," and she cites women of both races as victims of white supremacists.

A Black Woman Speaks of White Womanhood by Beah Richards
```

### Performance text (classify this)

```text
A Black Woman Speaks . . .
Of White Womanhood
Of White Supremacy
Of Peace
It is right that I a woman
black,
should speak of white womanhood.
My fathers
my brothers
my husbands
my sons
die for it; because of it.
And their blood chilled in electric chairs,
stopped by hangman’s noose,
cooked by lynch mobs’ fire,
spilled by white supremacist mad desire to kill for profit,
gives me that right.

I would that I could speak of white womanhood
as it will and should be
when it stands tall in full equality.
But then, womanhood will be womanhood
void of color and of class,
and all necessity for my speaking thus will be past.
Gladly past.

But now, since ‘tis deemed a thing apart
supreme,
I must in searching honesty report
how it seems to me.
White womanhood stands in bloodied skirt
and willing slavery
reaching out adulterous hand
killing mine and crushing me.
What then is this superior thing
that in order to be sustained must needs feed upon my
flesh?
How came this horror to be?
Let’s look to history.

They said, the white supremacist said
that you were better than me,
that your fair brow should never know the sweat of slavery.
They lied.
White womanhood too is enslaved,
the difference is degree.

They brought me here in chains.
They brought you here willing slaves to man.
You, shiploads of women each filled with hope
that she might win with ruby lip and saucy curl
and bright and flashing eye
him to wife who had the largest tender.
Remember?
And they sold you here even as they sold me.
My sisters, there is no room for mockery.
If they counted my teeth
they did appraise your thigh
and sold you to the highest bidder
the same as I.

And you did not fight for your right to choose
whom you would wed
but for whatever bartered price
that was the legal tender
you were sold to a stranger’s bed
in a stranger land
remember?
And you did not fight.
Mind you, I speak not mockingly
but I fought for freedom,
I’m fighting now for our unity.
We are women all,
and what wrongs you murders me
and eventually marks your grave
so we share a mutual death at the hand of tyranny.

They trapped me with the chain and gun.
They trapped you with lying tongue.
For, ‘less you see that fault-
that male villainy
that robbed you of name, voice and authority,
that murderous greed that wasted you and me,
he, the white supremacist, fixed your minds with poisonous
thought:
"white skin is supreme."
and therewith bought that monstrous change
exiling you to things.
Changed all that nature had ill you wrought of gentle
usefulness,
abolishing your spring.
Tore out your heart,
set your good apart from all that you could say,
think,
feel,
know to be right.
And you did not fight,
but set your minds fast on my slavery
the better to endure your own.

'Tis true
my pearls were beads of sweat
wrung from weary bodies’ pain,
instead of rings upon my hands
I wore swollen, bursting veins.
My ornaments were the wip-lash’s scar
my diamond, perhaps, a tear.
Instead of paint and powder on my face
I wore a solid mask of fear to see my blood so spilled.
And you, women seeing
spoke no protest
but cuddled down in your pink slavery
and thought somehow my wasted blood
confirmed your superiority.

Because your necklace was of gold
you did not notice that it throttled speech.
Because diamond rings bedecked your hands
you did not regret their dictated idleness.
Nor could you see that the platinum bracelets
which graced your wrists were chains
binding you fast to economic slavery.

And though you claimed your husband’s name still could not command his fidelity.

You bore him sons.
I bore him sons.
No, not willingly.
He purchased you.
He raped me,
I fought!
But you fought neither for yourselves nor me.
Sat trapped in your superiority
and spoke no reproach.
Consoled your outrage with an added diamond brooch.
Oh, God, how great is a woman’s fear
who for a stone, a cold, cold stone
would not defend honor, love or dignity!

You bore the damning mockery of your marriage
and heaped your hate on me,
a woman too,
a slave more so.
And when your husband disowned his seed
that was my son
and sold him apart from me
you felt avenged.
Understand:
I was not your enemy in this,
I was not the source of your distress.
I was your friend, I fought.

But you would not help me fight
thinking you helped only me.
Your deceived eyes seeing only my slavery
aided your own decay.
Yes, they condemned me to death
and they condemned you to decay.
Your heart whisked away,
consumed in hate,
used up in idleness
playing yet the lady’s part
estranged to vanity.
It is justice to you to say your fear equaled your tyranny.

You were afraid to nurse your young
lest fallen breast offend your master’s sight
and he should flee to firmer loveliness.
And so you passed them, your children, on to me.
Flesh that was your flesh and blood that was your blood
drank the sustenance of life from me.
And as I gave suckle I knew I nursed my own child’s enemy.
I could have lied,
told you your child was fed till it was dead of hunger.
But I could not find the heart to kill orphaned innocence.
For as it fed, it smiled and burped and gurgled with content
and as for color knew no difference.
Yes, in that first while
I kept your sons and daughters alive.

But when they grew strong in blood and bone
that was of my milk
you
taught them to hate me.
Put your decay in their hearts and upon their lips
so that strength that was of myself
turned and spat upon me,
despoiled my daughters, and killed my sons.
You know I speak true.
Though this is not true for all of you.

When I bestirred myself for freedom
and brave Harriet led the way
some of you found heart and played a part
in aiding my escape.
And when I made my big push for freedom
your sons fought at my sons’ side,
Your husbands and brothers too fell in that battle
when Crispus Attucks died.
It’s unfortunate that you acted not in the way of justice
but to preserve the Union
and for dear sweet pity’s sake;
Else how came it to be with me as it is today?
You abhorred slavery
yet loathed equality.

I would that the poor among you could have seen through the scheme and joined hands with me.

Then, we being the majority, could long ago have rescued
our wasted lives.
But no.
The rich, becoming richer, could be content
while yet the poor had only the pretense of superiority
and sought through murderous brutality
to convince themselves that what was false was true.

So with KKK and fiery cross
and bloodied appetites
set about to prove that “white is right”
forgetting their poverty.
Thus the white supremacist used your skins
to perpetuate slavery.
And woe to me.
Woe to Willie McGee.
Woe to the seven men of Martinsville.
And woe to you.
It was no mistake that your naked body on an Esquire
calendar
announced the date, May Eighth.
This is your fate if you do not wake to fight.
They will use your naked bodies to sell their wares
though it be hate, Coca Cola or rape.

When a white mother disdained to teach her children
this doctrine of hate,
but taught them instead of peace
and respect for all men’s dignity
the courts of law did legislate
that they be taken from her
and sent to another state.
To make a Troy Hawkins of the little girl
and a killer of the little boy!

No, it was not for the womanhood of this mother that Willie McGee died but for a depraved, enslaved, adulterous woman whose lustful demands denied, lied and killed what she could not possess. Only three months before another such woman lied and seven black men shuddered and gave up their lives. These women were upheld in these bloody deeds by the president of this nation, thus putting the official seal on the fate of white womanhood within these United States. This is what they plan for you. This is the depravity they would reduce you to. Death for me and worse than death for you.

What will you do?
Will you fight with me?
White supremacy is your enemy and mine.
So be careful when you talk with me.
Remind me not of my slavery, I know it well
but rather tell me of your own.
Remember, you have never known me.

You’ve been busy seeing me
as white supremacist would have me be,
and I will be myself.
Free!
My aim is full equality.
I would usurp their plan!
Justice
peace
and plenty
for every man, woman and child
who walks the earth.
This is my fight!

If you will fight with me then take my hand
and the hand of Rosa Ingram, and Rosalee McGee,
and as we set about our plan
let our wholehearted fight be:
PEACE IN A WORLD WHERE THERE IS EQUALITY.
```

---

## IC-1764: Blue Blanket

- Title: Blue Blanket
- Author (byline): Andrea Gibson
- Work: Pole Dancing to Gospel Hymns, Pg 36-39
- Publisher: Write Bloody Publishing
- Publication date as stated: June 2008
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 733
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andrea Gibson
Book: Pole Dancing to Gospel Hymns, Pg 36-39
ISBN: 978-0981521305
Publisher: Write Bloody Publishing
Date (Month/Year): June 2008
```

### Introduction (context only: never use it for content warnings)

```text
If you don't want to be raped . . .

• Wear only modest clothing, covering all portions of your

body that might be deemed provocative: shoulders,

knees, stomach.

• Avoid swaying your hips when you walk,

• Always travel in groups; never walk anywhere alone

• Stay sober always; intoxicated women are asking for it.

When it comes to rape prevention nearly every article written is aimed at what women can do to protect themselves from potential rapists. The implied message is that if you put yourself in a compromising position, you shouldn’t be surprised if you are raped. In other words . . . “It’s your fault.”

Andrea Gibson addresses this societal misfocus of blaming the victim in her poem “Blue Blanket”
```

### Performance text (classify this)

```text
(Pg 36-39) Still there are days when there is no way, not even a chance, that I’d dare for even a second glance at the reflection of my body in the mirror and she knows why.

Like I know why she only cries
when she feels like she’s about to lose control.
She knows how much control is worth,
knows how much a woman can lose when her power to

move is taken away

by a grip so thick with hate it could clip the wings of Isis, leave the next eight generations of your blood shaking.

And tonight something inside me is breaking,

my heart beating so deep beneath the sheets of her pain I could give every tear she’s crying a year, a name, and a face I’d forever erase from her mind if I could.

But how much closer to free would any of us be
if even a few of us forgot
what too many women in this world cannot.
And I’m thinking, “What the hell would you tell your

daughter?
Your someday daughter
when you have to hold her beautiful face
to the beat up face of this place
that hasn’t learned the meaning of
STOP.

What would you tell your daughter of the womb raped

empty,
the eyes swollen shut,
the gut too frightened to hold food,
the thousands upon thousands of bodies used?

It was seven minutes of the worst kind of hell. Seven. And she stopped believing in heaven.

distrust became her law,
fear her bible,
the only chance of survival . . .
don’t trust any of them.

Bolt the doors to your home,
iron gate your windows,
walking to your car alone
get the key in the lock like
please please please please open
like already you can feel
that five-fingered noose around your neck
two hundred pounds of hatred
digging graves into the sacred soil of your flesh
please please please please open
already you’re choking for your breath
listening for the broken record of the defense,
Answer the question,
Answer the question.
Answer the question, miss!

Why am I on trial for this?
Would you talk to your daughter,
your sister, your mother like this?
I am generations of daughters, sisters, mothers,
our bodies battlefields, war grounds
beneath the weapons of your brothers’ hands.

Do you know they’ve found landmines
in broken women’s souls?
Black holes in the parts of their hearts
that once sang symphonies of creation
bright as the light on infinity’s halo?

She says, “I remember the way love
used to glow on my skin
before he made his way in
now every touch feels like a sin
that could crucify Medusa, Kali, Oshun, Mary
bury me in a blue blanket so their god doesn’t know I’m a

girl,
cut off my curls,
I want peace when I’m dead.”
Her friend knocks at the door,
“It’s been three weeks,
don’t you think it’s time you got out of bed?”
“No, the ceiling fan still feels like his breath,
I think I need just a few more days of rest, please.”

Bruises on her knees from praying to forget.
She’s heard stories of Vietnam vets
who can still feel the tingling of their amputated limbs.
She’s wondering how many women are walking around this

world feeling the tingling of their amputated wings, remembering what it was to fly, to sing.

Tonight she’s not wondering
what she would tell her daughter.
She knows what she would tell her daughter.
She’d ask her, “What gods do you believe in?
I’ll build you temple of mirrors so you can see them.
Pick the brightest star you ever wished on.
I’ll show you the light in you
that made that wish come true. . . “

Tonight she’s not asking you what you would tell your

daughter. She’s life deep in the hell, the slaughter, has already died a thousand deaths with every unsteady

breath,
a thousand graves in every pore of her flesh
and she knows the war’s not over,
knows there’s bleeding to come,
knows she’s far from the only woman or girl
trusting this world no more than the hands
trust rusted barbed wire.

She was whole before that night.
Believed in heaven before that night,
and she’s not only one.
She knows she won’t be the only one.
She’s not asking what you’re gonna tell your daughter.
She’s asking what you’re going to teach
your son.
```

---

## IC-1765: The Blue Dress

- Title: The Blue Dress
- Author (byline): Reginald Gibbons
- Work: Slow Trains Overhead: Chicago Poems and Stories, Pg 78-86
- Publisher: University of Chicago Press
- Publication date as stated: May 2010
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1834
- Already set (do not supply): none

### Source block (context only)

```text
Author: Reginald Gibbons
Book: Slow Trains Overhead: Chicago Poems and
Stories, Pg 78-86
ISBN: 978-0226290584
Publisher: University of Chicago Press
Date (Month/Year): May 2010
```

### Introduction (context only: never use it for content warnings)

```text
According to the National Coalition Against Domestic Violence, an estimated 1.3 million American women are victims of physical assault by a husband or boyfriend each year. The majority of these women continue a relationship with their abuser. But why? Why do battered women stay? The answer given in the 1920s was that battered women were of low intelligence or mentally retarded. In the '40s it was determined that women did not leave because they were masochistic. By the '70s the experts claimed that a woman stayed in an abusive situation because she was isolated from friends and neighbors, had few economic resources, and was terrorized into a state of "learned helplessness" by repeated abuse.

But you see, the answer is not the problem . . . the
```

### Performance text (classify this)

```text
[I remember the night] . . .
(Pg 84 - 85) you tore my new blue dress
that you couldn't tell from silk
right off my back, left me
naked in a corner with my hands
up and you yelling at me
I spent too much of your money,
said I wouldn't
leave you alone,
made me get in the closet
and locked me in there, shouted
through the door if I ever
tried to leave you, you would
cut me so bad, no one
would want me, while I cried
into a torn rag of my dress,
all ruined and lost and wasted.

That was for you, that dress, to make you happy, make you want to be with me.

problem is the question itself. "Why doesn't she just leave?" When we ask that question first, we lose sight of the criminal and the crime and begin to place blame on the victim. The Blue Dress by Reginald Gibbons (Pg 78 – 86) You tore it off my back.

But I'm not good
at telling a story -- you'd shut
me up by saying that --
so I guess I can't tell this one,
that had to do with the way
I once used to feel
when someone like you
who had done a rough kind
of work -- work that can kill you
if you're not careful -- talked
to me like my listening
was important to him.

And listened
to me, too, made me feel
I could be the gentleness
he needed after bad
times -- someone who'd grown
up hard and alone, like you,
or gotten through the war
alive. . . But I don't feel
the same about you any-
more, or nearly anyone,
any man, I've known.
I thought when I met you
and it was exciting to me
to be with you, it was
more life I was getting --
and it was less.

But you said I was special,
I was the best of all
the girls -- the women -- you'd had,
the sexiest, I turned you on
the most. That's what I'd
remember when I'd want
to leave you,
when you'd been
after me again, like always
drunk, hunting me or saying
you'd kill me. I'd try remembering
that nobody else ever told me
I was special or beautiful,
and I thought it was loving
me that made you say it --
I know I'm not pretty
the way some women are,
the way some were that you
would look at twice and make
me forget what you'd done
and want you for myself again.

But it was just being
scared that kept me from leaving,
you saw to that many times.
And I did used to love you,
I did love your kisses,
love that touch you had for me,
holding my face in your hands,
squeezing my shoulders for me,
the way you'd rub my tired legs
and how you'd put your hands
on *me*, that was so careful,
I thought, not to hurt.
And my gripping you as hard
to me as I could,
and you'd say I was the best of all
of them, the best and the best
till the waves of it hit --
I'd float for a long
second or two and then it
slams through, so sweet.

But you'd hit me. Just sitting
together in the apartment and you'd
jump up and hit me yelling
"Don't do that!" and I don't
even know what it is.
You used your belt on me,
you threw me down the stairs
more than once and locked
me out alone for hours
and I never knew anyone
in the building who I could
go to, I'd just stay down
near the front door inside,
people would come in and go out
and hold the door for me
but I'd say no, I was
waiting

for someone. . .

Till you came down to look.
When you made up to me
I was so happy to have
you back -- back to yourself --
and we'd go out dancing,
you'd know everybody there
and those friends of yours would always
pretend that nothing's wrong.
I felt grateful to them
for treating me so friendly,
so polite, so respectful. Nice.
And they could laugh with me,
in a way you couldn't, or wouldn't.

The preacher says to talk. So I do and he listens and doesn't say very much.

He still thinks that all
the bad came from you, that
everything bad that was done,
you did -- which I'm not going
to tell him any different.
All he knows about that
night is you chased me
downstairs and into the street
at 3 a.m. with me
in my nightgown in the cold and no shoes
and you with the sharp kitchen
knife in your hand, yelling
you were going to cut me.

You never even knew how
afraid I was to go
to sleep and afraid to wait up
for you, too, but what would
you have cared, in those moods –
I went crazy wondering
what you'd do when you came in,
turning like a mean dog
and trying to get me when you
could barely stand up and had
to hold onto the furniture
to walk across the room.

I don't know how you
were able all of a sudden
to move so fast that night,
the state you were in, and the knife
in your hand. Then when you stopped
in the middle of the dead
street and said it was over
and turned around and started
back, I don't know why
I followed you home, either.

I watched you real carefully
when you got into bed
with your clothes on and you put
the knife under your pillow
and said to me that if I
wanted to kill you while you
were sleeping, there it was.

I waited one more hour
watching the clock go slow,
afraid you'd wake up
sick out of your alcohol sleep
and with one of your nightmares.
Then I had to reach under
your pillow to find the knife
and I cut my finger on it --
I almost cried out
but I realized that what I was
was so mad at you that
all of a sudden I wanted
to beat you hard as I could
with my fists and scream
and it still makes me crazy and I
wish I had done it --
instead. But I didn't
make a sound, just held
my cut finger that I couldn't
look at and looked at you
for a long time, trying
to guess where in you was your heart.

I had a thought and I
went back to the kitchen to put
a bandage on my cut and hold
it till it stopped bleeding
and only throbbed and I called
the police. Come over here
right now, I told them, I'm
going to kill him, and I gave
the address, the apartment,
the floor, the bedroom. . . I wanted
a bunch of them in case
they had to save me from
what you might do while you
were dying.

Or maybe what I wanted was what they did.

I took the knife and went
first to unlock the door
for when they'd come, wondering
how long it would be. I stood
in the doorway to our room
counting to two hundred
in my mind and then counted
again, and heard them stamping
and running up the stairs
so loud I thought they'd wake you
and I ran to stab your
chest holding the knife in both hands.

It slipped sideways and tore
your shirt down your ribs
and only cut you some.
You jumped and opened your eyes
but it didn't seem like you
could see me and I stabbed you
again and it slipped again,
I couldn't make it go
into you, but too late to stop.

When the cops pulled you off of me -- I don't know where the knife went -- know what?

I had to run onto the back
landing outside and pull
the door shut, that always
locks, lock myself out
because you were yelling
Help me, Esther, help me
please God Esther, help,
they're killing me, Esther!
I would have rushed back
and killed those cops to get
them off of you.

Then the noise was gone away. I was trying to figure out how to get back in, freezing and crying in my nightgown, they must have taken you away and what would happen to you and how could I get you out somehow when I heard two shots from the street around front.

I don't know what they've said
you did -- when they came up
calling for me and let me
into our place and told me
what had happened to you
I couldn't seem to hear them.

What I thought of while they
were talking and talking and waiting
for me to say something
that I wasn't going to say
was how I'd last seen one
of them at your back holding
you by the collar the way
you grabbed mine the night
you tore my new blue dress
that you couldn't tell from silk
right off my back, left me
naked in a corner with my hands
up and you yelling at me
I spent too much of your money,
said I wouldn't leave you alone,
made me get in the closet
and locked me in there, shouted
through the door if I ever
tried to leave you, you would
cut me so bad, no one
would want me, while I cried
into a torn rag of my dress,
all ruined and lost and wasted.

That was for you, that dress,
to make you happy, make
you want to be with me.
All I had was a physical
need in my body, for you,
and wanting you to say
you loved me and be nice
the way you used to be.
I kept thinking that if
I was nicer to you
you'd get better, you'd be
all right again, and I'd
be special to you, like before.

Now nothing can change ever
between us, we'll always
be stuck where we were that night.
Only I'm the only one
to feel it, you can't.

The preacher will tell me I
should forgive you now,
should let it go, should come
to church once in a while,
I look at him and see
another man looking at me.
You used to tell all your
stories to your friends, the hard
knocks you'd had -- you said
harder than mine. Is this
story good enough, you think,
for me to tell it? But you
aren't listening, you can't
answer me, you never did,
you're not here but you won't
go away, and you can't
give me back what you took
if you're dead. If you could
give me back that one dress
then you could give me everything,
even the way one time you put
your hand in my hair after
you had hit me and said
Please don't cry, sugar, don't,
honey, stop crying, please,
I promise to you that
I'll never do it ever again.
```

---

## IC-1766: The Bridge Poem and Women Don’t Riot

- Title: The Bridge Poem and Women Don’t Riot
- Author (byline): Kate Rushin and Ana Castillo
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 651
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kate Rushin
Book: This Bridge Called My Back
ISBN: 978-0913175033
Publisher: Kitchen Table--Women of Color Press
Date (Month/Year): February 1, 1984
Author: Ana Castillo
Book: I Ask the Impossible
ISBN: 978-0385720731
Publisher: Anchor Books
Date (Month/Year): March 2001
```

### Introduction (context only: never use it for content warnings)

```text
"The disease to please," as psychologist Harriet Braiker likes to call it, is a form of addiction. Just as a drug addict seeks drugs, a people pleaser seeks approval. We should help others and try to make them happy. But, the need to please others at all cost at all times, and be everything to everyone are actions of a desperate person. In these two poems The Bridge Poem by Kate Rushin and Women Don’t Riot, we experience the inner turmoil and external consequences facing women who have experienced this disease first hand.
```

### Performance text (classify this)

```text
The Bridge Poem
I've had enough
I'm sick of seeing and touching
Both sides of things
Sick of being the damn bridge for everybody

Nobody
Can talk to anybody
Without me
Right?

I explain my mother to my father my father to my little sister My little sister to my brother my brother to the white feminists The white feminists to the Black church folks the Black church folks To the ex-hippies the ex-hippies to the Black separatists the Black separatists to the artists the artists to my friends' parents...

Then I've got to explain myself To everybody

I do more translating Than the Gawdamn U. N.

Forget it I'm sick of it

I'm sick of filling in your gaps

Sick of being your insurance against The isolation of your self-imposed limitations Sick of being the crazy at your holiday dinners Sick of being the odd one at your Sunday Brunches Sick of being the sole Black friend to 34 individual white people

Find another connection to the rest of the world Find something else to make you legitimate Find some other way to be political and hip

I will not be the bridge to your womanhood
Your manhood
Your human-ness
I'm sick of reminding you not to
Close off too tight for too long

I'm sick of mediating with your worst self On behalf of your better selves

I am sick
Of having to remind you
To breathe
Before you suffocate
Your own fool self

Forget it Stretch or drown Evolve or die

The bridge I must be
Is the bridge to my own power
I must translate
My own fears
Mediate
My own weaknesses

I must be the bridge to nowhere
But my true self
And then
I will be useful

Women Don’t Riot

Women don't riot, not in maquilas in Malaysia, Mexico, or
Korea,
not in sweatshops in New York or El Paso.
They don't revolt
in kitchens, laundries, or nurseries.

Not by the hundreds or thousands, changing sheets in hotels or in laundries when scalded by hot water, not in restaurants where they clean and clean and clean their hands raw.

Women don't riot, not sober and earnest,
or high and strung out, not of any color,
any race, not the rich, poor,
or those in between. And mothers of all kinds
especially don't run rampant through the streets.

In college those who've thought it out
join hands in crucial times, carry signs,
are dragged away in protest.
We pass out petitions, organize a civilized vigil,
return to work the next day.

We women are sterilized, have more children
than they can feed,
don't speak the official language,
want things they see on TV,
would like to own a TV--
women who were molested as children
raped,
beaten,
harassed, which means
every last one sooner or later;
women who've defended themselves
and women who can't or don't know how
we don't--won't ever rise up in arms.

We don't storm through cities, take over the press, make a unified statement, once and for all: A third-millennium call-- from this day on no more, not me, not my daughter, not her daughter either.

Women don't form a battalion, march arm in arm
across continents bound
by the same tongue, same food or lack thereof,
same God, same abandonment,
same broken heart,
raising children on our own, have
so much endless misery in common
that must stop
not for one woman or every woman,
but for the sake of us all.

Quietly, instead, one and each takes the offense,
rejection, bureaucratic dismissal, disease
that should not have been, insult,
shove, blow to the head,
a knife at her throat.
She won't fight, she won't even scream--
taught as she's been
to be brought down as if by surprise.
She'll die like an ant beneath a passing heel.
Today it was her. Next time who.
```

---

## IC-1767: The Butcher’s Wife Poems “Shelter”, “The Butcher’s Wife” and “My Name Repeated on the Lips of the Dead”

- Title: The Butcher’s Wife Poems “Shelter”, “The Butcher’s Wife” and “My Name Repeated on the Lips of the Dead”
- Author (byline): Louise Erdrich
- Work: Jackight
- Publisher: Owl Books
- Publication date as stated: Feb 1984
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1224
- Already set (do not supply): none

### Source block (context only)

```text
Author: Louise Erdrich
Book: Jackight
ISBN: 978-0805010473
Publisher: Owl Books
Date (Month/Year): Feb 1984
```

### Introduction (context only: never use it for content warnings)

```text
It is the turn of the century in a German-American immigrant settlement. Mary Kröger marries the butcher, Otto, after his first wife -- who is also Mary's best friend -- dies, asking her to take care of Otto and their four sons. Shelter from “The Butcher’s Wife” section of Jacklight by Louise Erdrich
```

### Performance text (classify this)

```text
Shelter

My four adopted sons in photographs
wear solemn black. Their faces comprehend
their mother’s death, an absensce in a well
of empty noise, and otto strange and lost.
Her name was Mary also, Mary Kroger.
Two of us have lived and one is gone.
Her hair was blond; it floated back in wings,
and still you see her traces in the boys:
bright hair and long, thin, knotted woman’s hands.
I knew here, Mary Kroger, and we were bosom friends.
All graves are shelters for our mislaid twins.

Otto was for many years her husband,
and that’s the way I always thought of him.
I nursed her when she sickened and the cure
feel through at Rochester. The healing bath
that dropped her temperature, I think, too fast.
I was in attendance at her death:
She sent the others out. She rose and gripped my arm
and tried to make me promise that I’d care
for Otto and the boys. I had to turn away
as my own mother had when her time came.
How fe do not return in memory
and make us act in ways we can’t explain.
I could not lie to ease her, living, dying.
All graves are full of such accumulation.
And yet, the boys were waiting in New York
to take the first boat back to Otto’s folks
in Germany, prewar, dar powers were at work,
And Otto asked me on the westbound bus
to marry him. I could not tell him no --
We help our neighbors out. I loved him though
It took me several yeas to know I did
from that first time he walked in to deliver
winter food. Through Father Adler’s kitchen,
He shouldered half an ox like it was bread
and looked at me too long for simple greeting.
This is how our lives complete themselves,
as effortless as weather, circles blaze
in ordinary days, and through our waking selves
they reach, to touch our true and sleeping speech.

So I took up with Otto, took the boys and watched for them, and made their daily bread from what the grocer gave them in exchange for helping hi. It’s hard to tell you how they soon became so precious I got sick from worry, and woke up for two months straight And had to check them, sleeping, in their beds, and had to watch and see each breathe or move

before I could regain my sleep again.

All graves are pregnant with our nearest kin.

TRANSITION

Lives were short-lived at the turn of the century and Otto

soon dies as well, leaving Mary, the Butcher’s Wife a widow

– a widow who once loved her husband, but who seems to

have difficulty mourning the passing her drunken spouse.

The Butcher’s Wife

1

Once, my braids swung heavy as ropes.

Men feared them like the gallows.

Night fell

When I combed them out.

No one could see me in the dark.

Then I stood still

Too long and the braids took root.

I wept, so helpless.

The braids tapped deep and flourished.

A man carne by with an ox on his shoulders.
He yoked it to my apron
And pulled me from the ground.
From that time on I wound the braids around my head
So that my arms would be free to tend him.

2 He could lift a grown man by the belt with his teeth. In a contest, he'd press a whole hog, a side of beef. He loved his highballs, his herring, and the attentions of

women. He died pounding his chest with no last word for anyone.

The gin vessels in his face broke and darkened. I traced

them
Far from that room into Bremen on the Sea.
The narrow streets twisted down to the piers.
And far off, in the black, rocking water, the lights of

trawlers Beckoned, like the heart's uncertain signals, Faint, and final.

3 Of course I planted a great, full bush of roses on his

grave. Who else would give the butcher roses but his wife? Each summer, I am reminded of the heart surging from

his vest, Mocking all the high stern angels By pounding for their spread skirts.

The flowers unfurl, offering themselves, And I hear his heart pound on the earth like a great

fist, Demanding another round of the best wine in the house. Another round, he cries, and another round all summer

long, Until the whole damn world reels toward winter drunk.

TRANSITION

After Otto dies Mary is left to deal with Sherriff Rudy J. V. Jacklitch, whose courting she does not encourage, until he crashes his truck and dies cursing her. Nevertheless, Mary hears HER name destroyed by the townspeople. My Name Repeated on the Lips of the Dead

My Name Repeated on the Lips of the Dead

Last night, my dreams were full of Otto’s best friends. I sat in the kitchen, wiping the heavy silver, and listened to the losses, tough custom, and fouled

accounts
of the family bootlegger, county sheriff:
Rudy J.V. Jacklitch, who sat just beside me,
wiping his wind-cracked hands
with lard smeared on a handkerchief.

Our Pekinese-poodle went and darkened his best wool trousers, and he leapt up, yelling for a knife!

These are the kinds of friends
I had to tend in those days:
great, thick men, devouring
Fleisch, Spaetzle, the very special
potato salad for which I dice
onions so fine they are invisible.

Rudy J.V. Jacklitch was a bachelor, but he cared for his mother, a small spider of a woman – all fingers, She cove red everything, from the kettle to the radio, with a doily. The whole house dripped with lace, frosting fell from each surface in fantastic shapes. When Otto died, old Rudy came by with a couple jugs for the mourners’ supper. He stayed on past midnight, every night the month after he would bring me a little something to put the night away.

After a short while I knew his purpose. His glance slipped as the evening and the strong drink wore on.

playing cribbage I always won,
a sure sign he was distracted.
I babbled like a talking bird,
never let him say the words
I knew were in him.

Then one night he came by,
already loaded to the gills,
rifle slung in the back window
of his truck: Going out
to shoot toads. He was peeved
with me. I’d played him all wrong>
He said his mother knew just what I was.

The next thing I heard that blurred night
was that Rudy drove his light truck
through the side of a barn,
and that among the living
he stayed long enough
to pronounce my name, like a curse
through the rage and foam of his freed blood.

So I was sure, for a time and a time after,
That Rudy carried
my name down to hell on his tongue
like a black coin.

I would wake, in the deepest of places,
and hear my name called.
My name like a strange new currency they read:
Mary Kroger
with its ring of the authentic
when dropped
or struck between their fingers.
How I feared to have it whispered in their mouths!

Mary Kroger
growing softer and thinner
till it dissolved
like a wafer under all that polishing.
```

---

## IC-1768: Carlotta’s Confession

- Title: Carlotta’s Confession
- Author (byline): Donald Hall
- Work: Old and New Poems
- Publisher: Mariner Books
- Publication date as stated: July 1990
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 799
- Already set (do not supply): none

### Source block (context only)

```text
Author: Donald Hall
Book: Old and New Poems
ISBN: 978-0899199542
Publisher: Mariner Books
Date (Month/Year): July 1990
```

### Introduction (context only: never use it for content warnings)

```text
Our Father, Who art in heaven, hallowed be Thy name; Thy kingdom come; Thy will be done on earth as it is in heaven. Give us this day our daily bread; and forgive us our trespasses as we forgive those who trespass against us; and lead us not into temptation but deliver us from evil. Amen.

O my God, I am heartily sorry for having offended you and I detest all my sins, because I dread the loss of heaven and the pains of hell. But most of all because I have offended you, my God, who are all good and deserving of all my love. I firmly resolve with the help of your grace, to confess my sins, to do penance and to amend my life. Amen.

Carlotta’s Confession by Donald Hall
```

### Performance text (classify this)

```text
"My grandfather's name was Augusto,

'ow-goose-toe' the way he said it. He sailed from Sicily, Palermo

to Newark, when he was fifteen and not quite five feet tall.

With American food, with the remarkable effluents of New Haven, Connecticut,

and the gun factory, he stretched out to five-foot-one.

At thirteen I was two inches taller than my grandfather - Carlottina

the Giantess - and I daydreamed of becoming a nun. Augusto caressed us,

teased us, screamed at us, and praised us - as long as we went

to Mass; I adored my grandfather and when he died, named my first child Augustus.

Gus was eight for the divorce; Mary, who is Maria now, was three

and contented. My boyfriends teased Gus and brought him presents;

on weekends it was Harry's girls. I was miserable and called it adventure.

Devils the nuns had described vividly for us jabbed forked tails

into me, and for every jab I took my revenge by destroying something else:

I had a late abortion; I married again - for six weeks.

From the third grade on, Gus spent more hours in the principal's office after school

than he did on the playground. I got him into Country Day at ten:

They expelled him for fighting. He was twelve the first time

the police called me; at fifteen, larceny and a year in reform school. Then

no more school and no jobs that lasted: Gus never finished anything

except a joint or a pint of wine. He never went back to a shrink

for a second appointment. Of course he made resolutions; there was a sweetness

to him that broke my heart, and my heart always broke

with his resolutions. When he was twenty he resolved to kill himself:

Naturally we argued about it; sometimes I won the arguments,

but a week later - I made pasta every Sunday night - he'd return

with more reasons. Sometimes with a new job or girl he'd drop the subject;

then there'd be another disaster and he'd disappear for a week.

On a wet Sunday a month ago – after he lost a good job

and signed up for welfare again, and moved in again with a girlfriend

who cheated on him - he telephoned me to say goodbye; he had said goodbye

many times before but this time he called his own bluff -

and he failed again. The shoplifted .22 caliber target pistol left him

in Intensive Care on his back with his eyes open and his left

cheek twitching every nine seconds. They had hooked him up to a machine

but he lay staring beyond my fury and my love forever.

For two weeks I sat beside him all night while machines breathed

for him, rasping and hissing like metal cats. In my head I kept arguing with him:

Now the argument ran to pulling or not pulling the plug. What a quarrel!

Once as I drove home from the hospital at midnight

for a little induced sleep before a court session in the morning,

my mind ran a movie, like those scenes in pantomime that they show

behind titles: I watched myself tiptoe into Gus's hospital room

in a gray light; then I glanced over my shoulder to see that no one followed;

then I suffocated him. The next morning the old judge delivered

his order; after supper, with Maria holding me, I kissed Gus

a last time. The head nurse turned the switches off one by one.

By one. Very, very slowly his heartbeats, visible on the green monitor,

blipped farther apart. One breath a minute. Two minutes. Then there were none.

Next afternoon we buried him in the non-denominational

(meaning Protestant) graveyard. For three days I felt gay; then the guilt:

Repeatedly I went over his life from the beginning, finding

that my errors ruined his life, fault breeding fault breeding fault:

selfishness, lust, cruelty, greed, malice, laziness, pride. I married myself

to failure, now I was failure's widow. I tried going to church, say

what you like, where I hadn't gone since my first divorce: My tongue grieved

for my grandfather's wine and wafer. First, I needed to make my confession,

my litany of error, and I told the young priest how

I had broken each of the commandments except the one that forbids us to kill.

The moment I heard myself speak I laughed aloud - but I didn't

laugh with amusement: Carlotta the mother who aborted one child

and daydreamed strangling another. For penance he said - a Hail Mary.

Hail Mary, full of grace. Our Lord is with thee. Blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen.

'Your sins are forgiven,' he said."
```

---

## IC-1769: Cat Got Your Tongue?

- Title: Cat Got Your Tongue?
- Author (byline): Sonya Sones
- Work: Sixteen: Stories About That Sweet and Bitter Birthday (Pg 120-168)
- Publisher: Broadway Books
- Publication date as stated: May 2004
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2707
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sonya Sones
Book: Sixteen: Stories About That Sweet and Bitter
Birthday (Pg 120-168)
ISBN: 978-1400052707
Publisher: Broadway Books
Date (Month/Year): May 2004
```

### Introduction (context only: never use it for content warnings)

```text
The day we turn 16 is a magical day, full of good wishes and birthday cake. For Bria this is also the day for newfound love and a cat that might steal her heart before she has the chance to give it away.

Cat Got Your Tongue by Sonya Sones
```

### Performance text (classify this)

```text
*NOTE: written in poetry form but included in a prose anthology. Check the regulations for your tournament for the appropriate category in which to enter this selection.

It Feels Just Like I Dreamed It Would (Pg 120-168)

My skin misting all over, my T-shirt clinging to me, my breath coming in short, soft gasps,

my heart hip-hopping in my chest, my hands trembling and reaching out,

my fingertips buzzing as I take hold of it,
gripping it for the very first time,
slipping around it as if it were a trophy—
my very own driver’s license!

Everybody Sing!

Happy Birthday to me, Happy Birthday to me, Happy Birthday, dear Bria,

Happy Birthday
to deliriously happy, totally independent,
sixteen-year-old, licensed-driver
me!

Actually, My Real Name Isn’t Bria

It’s Umbria.
And just in case you’re wondering why
I have such a bizarre yet fabulously exotic name
it’s because my parents named me
after a region in Italy.

Which, supposedly,
is the very region in which I was conceived.
So, as you might well imagine,
every day I thank my lucky stars
that I wasn’t conceived
in Oxnard.

My Parents Told Me That It Happened in a Car

Not that I had even the eensy beensiest desire to know that.

Mom says maybe that’s why learning how to drive came so easily to me.

So That Means

That even if my big brother, Paris (can you guess where he was conceived?), wasn’t twenty-one years old,

it’d still be okay for me to be the one driving us up to Aunt Ginger’s place for my birthday luau

(her idea, not mine),

Levitating to My Luau in Paris’s Mustang

Shooting through the night
like an arrow on the wind,
we’re zooming past the orchards
with the top down.

Breezing down the road,
listening to rap,
my fingers have to tap,
have to dance to the music of the ride.

The car and I are one,

I could drive like this for hours,
I could drive us anywhere,
drive us right up past the moon
to the stars.

Both of Us See It

This bullet of fur,

this tiger-striped shadow, this smudge, this blur

that darts from the dark

We see it streak out. But it’s just

too sudden, too fast,

too—!

I Slam on the Brakes

Slam them so hard that wheels scream, rubber burns.

“Oh, no!” I gasp. “Did I hit it? I didn’t hit it. Did I?”

Paris doesn’t answer. He doesn’t need to.

I already know.

I know. But I don’t want to know.

And I sure don’t want to turn around and see it lying in the middle of the road. But I swivel in my seat and there it is—

a mangled mound of tiger-striped fur, one delicate paw extended out of the heap, as though caught in mid-swipe,

a small white moth fluttering above it in the blood red glow of the tail lights

as if trying to coax the little cat to life, trying to lure it back to the chase—

I rest my forehead n the steering wheel and cry.

I Guess Paris Must Feel Pretty Sorry for Me

Because he doesn’t even call me Dumbria.
He just reaches over and switches off the ignition,
silencing the CD and filling the night
with the sudden echoing choir of crickets.

He lets me cry it out for a few minutes. Then he hands me a Kleenex, tousles my hair, and says, “Geez, Bria.

I know you aren’t particularly fond of kitties, but don’t you think you’ve gone just a tad too far this time?”

Now I’m laughing instead of crying. And thinking to myself how much I love my brother.

But then that gets me thinking about the people who probably loved that cat.

And I break down all over again.

Paris Sighs

Then he puts his arm around me and says, That there wasn’t anything I could do.

“Believe me,” he says, totally deadpan. “Even if a good driver had been driving the car, the same thing would have happened.”

It takes me a second to realize that I’ve just been insulted. Then I start laughing again.

He says, “Well, we better get going or we’ll be late to your birthday luau.”

So I blow my nose one last time, switch on the ignition, shift into drive,

And flee from the scene of the crime.

Two Minutes Later

We pull up in front of Aunt Ginger’s house.
Paris commends me on my courage,
my fortitude,
and my parallel parking.

We head toward the front door,
but before we can even knock,
it sweeps open and Aunt Ginger yanks us inside,
hurling herself into our arms.

It’s like being hugged by an unusually friendly octopus who just happens to be wearing a hula skirt and one of those bras made out of coconuts. (Ouch! Ouch!)

“Aloha, my darlings!” she cries,
flinging a lei over each of our heads.
“I want you to meet Leon,
my fifth and final husband.”

Leon stops strumming his ukulele
and steps forward to pump both our hands.
He’s a Buddha-esque little man dressed only in a pareo,
with a belly as round as his gleaming bald head.

“Which one is the birthday girl?” he says with a grin.
This is apparently Leon’s subtle way
of letting us know that he’s noticed
the length of my brother’s hair.

“I am,” Paris says,
with a seductive bat of his eyelashes.
This totally cracks Leon up.
“You’re going to get along great with my son!” he says.
His son? No one said anything about a son.

Flynn Walks Through the Door

Suddenly I’m staring deep into a pair of swimming-pool-blue eyes,

these huge, dreamy, heavy-lidded miracles fringed with a forest of feathery black lashes.

I’m just
standing here
dumbstruck,
and my heart starts dancing the hula.

I’ve Read About This Sort of Thing Happening
This hokey love-at-first-sight thing,
this sparks-flying-fireworks-exploding-
ohmigod-I-think-I’m-about-to-melt-into-a-puddle-
right-here-and-now-
all-over-the-floor thing.

But I never thought it would ever happen to me.

Or That When It Did

It would be with a boy named Flynn.

I Let My Eyes Drift Down to Flynn’s Lips

“Hau’oli la hanau momona ‘umi kumaono,” he says. “Huh?” I say. “It’s Hawaiian for ‘Happy Birthday, sweet sixteen.’ I’ve been practicing.”

“Wow . . .” I say, temporarily stunned into monosyllables by the husky sound of his sexy voice. But a second later I manage to pull myself together and purr, “I love it when you talk Hawaiian to me.”

Then Paris says, “Hey, Flynn.
Can you teach me the Hawaiian words for
‘How about them Lakers?’”
And Flynn cracks up, as Leon herds us into the kitchen.

Aunt Ginger Tells Us She’s Been Secretly Yearning

To throw me a luau for my sixteenth birthday,

Then she slips on an apron and asks my brother to help her chop the onions and tomatoes for the lomi lomi salmon.

Leon opens the oven to check on the kalua pig. He asks Flynn to peel the sweet potatoes. I offer to set the table, and head out onto the patio.

Alone at last, under a full moon, with my fantasies of Flynn . . .

I’ll be setting out the plates when he’ll come up behind me and whisper in my ear, so near that I’ll feel the tingle of his breath on my skin.

“Do you need any help, Bria?” But I won’t answer. I’ll just lean back, pressing my body tightly to his.

He’ll wrap his arms around me, holding me so close that I’ll feel his heartbeat’s wild drumming.

Then he’ll start kissing my neck,
my shoulders,
my—
“Do you need any help, Bria?”
I whirl around—
Ohmigod!

It’s Flynn.

I Can Feel My Cheeks Flushing Hibiscus Pink

“Sure,” I say,

“How about if you put out the napkins,” I say,
trying my best to sound nonchalant,
“and I put out the plates?”
“Okay,” he says.

I begin circling the table, placing a dish in front of each chair.

Wherever I go,
Flynn goes, too,
gliding along next to me
as though we’re doing the tango.

He begins passing me
the little paper umbrellas for the glasses.
That’s when it happens—
his fingertips brush my wrist!

Suddenly, this quivery sort of shiver
flutters all through me
and Flynn takes a step closer,
his fingers finding mine, lacing us together.

“Hey, kids,” Paris calls.
He’s standing in the kitchen doorway smirking,
with his arms crossed over his chest,
one eyebrow raised.

“Can you give us a hand grating these coconuts?”

I Muddle Through the Next Half Hour

Avoiding eye contact, avoiding any contact with Flynn the Magnificent.

Because it’s entirely too weird to be falling for him While his father is watching, not to mention my aunt and my nosy big brother,

who for some strange reason has decided that his baby sister is off-limits to every boy on the entire planet.

When We Finally Head Out onto the Patio to Eat

Flynn practically breaks into a trot to grab the seat next to mine. This totally goose-bumps me.

We Share a Secret Smile That Lasts a Nanosecond

Then, Flynn slithers his hand into mine under the table, and a dizzying current of energy surges between us.

“So, Flynn,” Paris asks,
“were you in Maui with your father when he met Ginger?”
But Flynn doesn’t answer.
He doesn’t even appear to have heard the question.

That son of yours,” Aunt Ginger says fondly,
resting her head on Leon’s shoulder,
and smiling across the table at Flynn.
“He’s such a daydreamer.”

“What’s the matter, boy?” Leon asks gently.
“Cat got your tongue?”
“Hey, speaking of cats,” Aunt Ginger says,
“has anyone seen Bitsy?”

Did she just say “speaking of cats”?!
“Who . . .” I ask warily, “. . . is Bitsy?”
Aunt Ginger heaves a dreamy sigh and says,
“Only the most wonderful kitty on the face of this earth.”

“She really is terrific,” Leon says.
“I wonder where that little rapscallion could be.
It’s not like her to be late for supper.
She’s always home by eight . . .”

I check my watch— It’s 8:25!

My Heart Freezes in Mid-beat
Under the table, Paris grabs my other hand.
We sneak a quick peek at each other.
He’s obviously thinking what I’m thinking.
I squeeze his hand in panic.
Paris knocks back the rest of his Mai Tai in a single gulp.

“I hope that dear little cat hasn’t gotten herself
into any trouble . . .” Aunt Ginger says.
And a line creases her forehead.
“Don’t you worry, doll,” Leon says.
“I’m sure our Bitsy’s just fine.”

“She better be,” Flynn says,
finally emerging from his love trance.
“I’ve gotten way attached to the Bitster.
I can’t wait for her to get home
so you can see her, Bria.”

“Me neither,” I barely manage to croak.
As Aunt Ginger’s eyes start misting over.
“You know,” she says, “if it weren’t for Bitsy,
I never would have even met Leon.”

Then she tells us this long story about how she was taking a walk on Hamoa Beach in Maui, and she was feeling so sorry for herself,

because there she was, all alone in this tropical paradise, letting this fabulously deserted beach go to waste,

when she heard this tiny mew coming from behind her.

So she turned around and there was this scruffy kitten, following right along after her.

“She could easily fit into a single one of my footprints,” Aunt Ginger says. “She was such an itsy-bitsy little thing.”

“Hence . . . the name?” Paris asks, with a visible lurch of his Adam’s apple. “Exactly,” Aunt Ginger says,

not seeming to notice his oddly strangled tone of voice.

There’s a Question Burning in My Throat

A question that has to do
with whether or not
a certain little wonder cat is tiger-striped.
But I’m way too scared to ask it.

“I figured she was lost,” Aunt Ginger continues.
“So I picked her up and started knocking
on all the doors of the houses nearby
to try and find her owner.”

“When Flynn and I answered our door,” Leon says,
“there was this absolutely gorgeous woman
standing there,
holding this scrawny little feline in her arms.”

Well, apparently,
one thing led to another,
and the three of them spent the rest of the day together,
searching to no avail for the kitten’s owner.

But before the moon rose that night,
Leon was in love with Aunt Ginger.
And they all were in love
with Bitsy.

“Which Was Totally Strange for Dad and Me,” Flynn Says

“Because both of us had always been allergic to cats.
“But Dad and I decided that we’d rather spend
the rest of our lives on antihistamines
than have to give up the Bitsinator.”

And Flynn
squeezes my left hand,
while Paris
squeezes my right one.

My Stomach’s Doing the Jitterbug

then, Paris (says) “What does the Bitserino look like, anyway?”

“Yeah,” I say hopefully. “What color is she? Gray? Calico?”

“Nope,” Flynn says, pulling out his wallet, like a proud father, to show me her picture.

She’s a cute little tiger-striped thing.”

No!

Suddenly I’m choking on my lau lau. Or is that my heart that’s stuck in my throat? Paris and Flynn start slapping me on my back.

“Dang hairballs,” Paris says. And everyone laughs. Even Paris and me.

But anyone who took a close look at either one of us would be able to see the ohmigod!!! in our eyes.

Flynn Reaches for My Hand Again

Let’s take a walk to see if we can find Bitsy, okay?”

Find Bitsy?! Oh, man . . .

“Sure,” I gulp, as Flynn takes my hand and yanks me out the front door,

before Paris even sees where we went.

I Try

To steer Flynn in the opposite direction from the scene of the crime.

But he says that Bitsy sometimes visits
the cat that lives at the apple farm
a few blocks down the road,
so we ought to check there first.

Now it’s just the full moon dappling the lawns, the echoing of the cricket choir, and Flynn’s long, warm fingers entwined with mine, as we stroll together through the summer night lit with stars and fireflies and possibilities . . .

The only problem is that every step we’re taking is leading us closer and closer still

to a certain heap of roadkill.

“Here, Bitsy, Bitsy, Bitsy . . .”

Flynn’s calling softly to her, in that husky voice of his—

that voice that practically makes me swoon.

One block . . . Two blocks . . .

Now Flynn’s telling me stories about his life. Funny ones.

Stories that make me like him even more than I already did.

The sound of his laugh, the feel of his hand, those lips, those lashes . . .

“Here, Bitsy . . . Here, Bitster, Bitster, Bitster . . .”

Three blocks . . . Four blocks . . .

But I Can See It in the Distance Now

I can just make it out at the far end of the block— the lump that’s lying in the middle of the road! The poor little kitty that I snuffed out . . .

Then, without warning, Flynn slows to a stop and pulls me around to face him.

But I keep my eyes trained on the ground. Because if I look up into his, I know what will happen.

And I can’t let that happen. Can I? Can I?

He Takes a Step Closer to Me

And brushes his lips against my forehead. “Flynn,” I whisper. “Yeah?” he whispers back.

“There’s something I have to tell you.”

“What is it, Bria?” he asks. “Is there someone else?” “No,” I say, closing my eyes tight.

“It’s nothing like that . . . It’s . . . it’s about your . . . your . . .”

Suddenly, something brushes against my ankle. I leap back and then I see it—

it’s something furry, something soft, something tiger-striped!

“Bitsy!”

Flynn cries, “Where have you been?” scooping her up and burying his face in her fur. “We’ve been looking all over for you.”

“Bitsy . . . ?!” I gasp.

“But . . . but I thought . . . Ohmigod! Bitsy! It’s you!”

“Mew,” Bitsy says matter-of-factly, gazing at me with her big yellow eyes.

I lean in to rub my cheek against the softest fur in the universe and then I find Flynn’s lips

and kiss him!
```

---

## IC-1770: The Choices of Pregnancy and Motherhood Collection

- Title: The Choices of Pregnancy and Motherhood Collection
- Author (byline): Anne Sexton and Audre Lorde
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1026
- Already set (do not supply): none

### Source block (context only)

```text
Author: Anne Sexton
Book: All My Pretty Ones
ISBN: 978-0395081778
Publisher: Houghton Mifflin
Date (Month/Year): April 1962
Author: Anne Sexton
Book: Poetry Out Loud: The Anthology
ISBN: 978-1881505112
Publisher: National Endowment of the Arts
Date (Month/Year):
Author: Audre Lorde
Book: The Oxford Anthology of African American Poetry
ISBN: 978-0195125634
Publisher: Oxford University Press
Date (Month/Year): Oct 2005
```

### Introduction (context only: never use it for content warnings)

```text
“You’re pregnant . . . but you have a number of options.” Options . . . What a perplexing word. Abortion, Adoption . . . Keep the Baby. The options . . . . sounds so simple . . . . just make a choice.

We live in a society that ignores the painful consequences of abortion. As one woman said: "We were convinced that the abortion was the best thing rather than the right thing." Men and women who have experienced it are urged into denial, so they do not talk about and process the normal feelings of anxiety, fear, shame, guilt and grief which often follow the abortion. When such emotions are denied and buried, they will often resurface having been magnified by time. Anne Sexton focus on the emotional ramifications of The Abortion.
```

### Performance text (classify this)

```text
The Abortion by Anne Sexton

Somebody who should have been born is gone.

Just as the earth puckered its mouth, each bud puffing out from its knot, I changed my shoes, and then drove south.

Up past the Blue Mountains, where Pennsylvania humps on endlessly, wearing, like a crayoned cat, its green hair,

its roads sunken in like a gray washboard; where, in truth, the ground cracks evilly, a dark socket from which the coal has poured,

Somebody who should have been born is gone.

the grass as bristly and stout as chives, and me wondering when the ground would break, and me wondering how anything fragile survives;

up in Pennsylvania, I met a little man, not Rumpelstiltskin, at all, at all...

he took the fullness that love began.

Returning north, even the sky grew thin like a high window looking nowhere. The road was as flat as a sheet of tin.

Somebody who should have been born is gone.

Yes, woman, such logic will lead to loss without death. Or say what you meant, you coward...this baby that I bleed.

TRANSITION Many of us have seen glimpses of mothers who have recently surrendered their baby for adoption. Sometimes the mother is euphoric over the birth of her beautiful son or daughter and tries to focus on that joyous event and "be brave". She may say at least she managed to save her baby from abortion. She may do her best to go on with her life, believing that she will soon get over it and go on with her life. Sometimes the mother has a complete breakdown or turns to drinking or drugs to try to ease her suffering over this tremendous loss. Just remember the privilege of having the Option if you are an Unknown Girl in the maternity Ward by Anne Sexton.

Unknown Girl in the Maternity Ward by Anne Sexton

Child, the current of your breath is six days long.
You lie, a small knuckle on my white bed;
lie, fisted like a snail, so small and strong
at my breast. Your lips are animals; you are fed
with love. At first hunger is not wrong.
The nurses nod their caps; you are shepherded
down starch halls with the other unnested throng
in wheeling baskets. You tip like a cup; your head
moving to my touch. You sense the way we belong.

But this is an institution bed. You will not know me very long.

The doctors are enamel. They want to know
the facts. They guess about the man who left me,
some pendulum soul, going the way men go
and leave you full of child. But our case history
stays blank. All I did was let you grow.
Now we are here for all the ward to see.
They thought I was strange, although
I never spoke a word. I burst empty
of you, letting you learn how the air is so.
The doctors chart the riddle they ask of me
and I turn my head away. I do not know.

Yours is the only face I recognize. Bone at my bone, you drink my answers in. Six times a day I prize your need, the animals of your lips, your skin growing warm and plump. I see your eyes lifting their tents. They are blue stones, they begin to outgrow their moss. You blink in surprise and I wonder what you can see, my funny kin, as you trouble my silence. I am a shelter of lies. Should I learn to speak again, or hopeless in such sanity will I touch some face I recognize?

Down the hall the baskets start back. My arms fit you like a sleeve, they hold catkins of your willows, the wild bee farms of your nerves, each muscle and fold of your first days. Your old man’s face disarms the nurses. But the doctors return to scold me. I speak. It is you my silence harms. I should have known; I should have told them something to write down. My voice alarms my throat. “Name of father—none.” I hold you and name you bastard in my arms.

And now that’s that. There is nothing more that I can say or lose. Others have traded life before and could not speak. I tighten to refuse your owling eyes, my fragile visitor. I touch your cheeks, like flowers. You bruise against me. We unlearn. I am a shore rocking you off. You break from me. I choose your only way, my small inheritor and hand you off, trembling the selves we lose. Go child, who is my sin and nothing more.

TRANSITION Parenting (the OTHER OPTION) can be one of life’s most joyous experiences. And can bring with it many rewards: the warmth of cuddling with a baby; proudly watching as a toddler takes a first step, or tearfully putting your little one on a school bus for the first time! However, parenting can also be the hardest, most demanding job you’ll ever undertake. It means being responsible for the care and nurture of a child for at least 18 years. It requires dedication, patience, and sacrifice. Sounded so easy at the beginning didn’t it. “You’re pregnant . . . but you have options – Options that will affect you for the rest of your life. New that I am Forever with Child by Audre Lorde.

Now that I am Forever with Child by Audre Lorde

How the days went
while you were blooming within me
I remember each upon each---
the swelling changed planes of my body
and how you first fluttered, then jumped
and I thought it was my heart.

How the days wound down
and the turning of winter
I recall, with you growing heavy
against the wind. I thought
now her hands
are formed, and her hair
has started to curl
now her teeth are done
now she sneezes.
Then the seed opened
I bore you one morning just before spring
My head rang like a fiery piston
my legs were towers between which
A new world was passing
Since then
I can only distinguish
one thread within running hours
You, flowing through selves
toward You.
```

---

## IC-1771: Cloud of Witnesses, All Saints Day

- Title: Cloud of Witnesses, All Saints Day
- Author (byline): Roseann Lloyd
- Work: War Baby Express
- Publisher: Holy Cow! Press
- Publication date as stated: May 1996
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1110
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roseann Lloyd
Book: War Baby Express
ISBN: 978-0930100681
Publisher: Holy Cow! Press
Date (Month/Year): May 1996
```

### Introduction (context only: never use it for content warnings)

```text
According to the Family Violence Prevention Fund, On average, more than three women a day are murdered by their husbands or boyfriends in the United States and women experience two million injuries from intimate partner violence each year. Many of these women are mothers who often go to great and courageous lengths to protect their children from abusive partners. In fact, research has shown that the non-abusing parent is often the strongest protective factor in the lives of children who are exposed to domestic violence. However, growing up in a violent home may be a terrifying and traumatic experience that can affect every aspect of a child’s life, growth and development. Roseann Lloyd has dedicated her poem Cloud of Witnesses, All Saints Day to the 18 Minnesota women who were murdered by their partners in 1989 and the 27 women who were murdered in 1990, and to their children. Cloud of Witnesses, All Saints Day by Roseann Lloyd.
```

### Performance text (classify this)

```text
1 Thanksgiving again, my daughter and I are coloring, making shapes by tracing around our hands.

She is making a turkey, her fingers are feathers now, bright and brown, burnt sienna, maize, and umber.

I'm drawing rings on my fingers, emeralds and gold, and when I start on the matching bracelet, I'm startled

to see my wrist so small on the cardboard, looking like it belongs to a girl no older than 12.

How can it be mine, this woman no longer a girl? I've put on weight, but I still have small bones.

2
His hands were even beefier than when we were
married. Meathooks.
How did I ever manage to escape without any broken
bones?

The question was: Could we talk about our daughter's health with a third party present?

When she's at your house, I said, is she getting beat up? Has she seen you

hitting anyone else? You sound like a battered wife, he said.

I said, That's because I was one. Fear rose in my throat, red blotches spread across my neck.

His face was an odd combination of blankness and broken edges, as though he'd been informed he had cancer of the brain.

He turned to face the therapist. She never went in for x-rays.

The therapist asked me to relate one incident, I picked the first time, the argument about keeping the dog.

Don't you see, he said, I can't apologize - I don't remember. I have no emotional content

for what she's saying He seemed to have no memory of

the other therapists we went to, each one saying Hitting a woman is never acceptable.

It's possible it's true, he said. I was always on edge in those days

.
3
He was always careful not to break my glasses.
Careful to hit me on the back of the head, to pound the
fleshy
stomach, the uterus, the fat of my back.
Careful not to hit our daughter when she was snuggling
on my lap.

Overweight means I don't feel vulnerable. My wrists give me away.

The first time he hit me: Thanksgiving, 1971. The term battered wives first used in research: 1974.

He used to be so careful, in surgery, tying tiny sutures. An expert, he knew how to leave no marks that show.

The drawing of my hand looks like it belongs to a 12- year-old, playing dress-up. Rings on her fingers, bells on her toes.

It was a shock to feel the floorboards, wind knocked out of me. Like a child, I thought, how can someone who loves me do this?

In The Times Book Review, Jean Stafford, in braids, frowns like a troubled girl, her husband, a batterer, stern beside her.

When I left him, I moved in with another man for protection. It was the only way I knew to handle my fear.

Now I'm ready at any moment to dial 91l. I wouldn't hesitate to take a knife to him without warning.

I've gained weight, but my bones are still small. There's no fear in my body, I say, but the weight stays put.

I've never told anyone before-I can't
remember how he looks naked.
Our daughter didn't make plaster handprints in
kindergarten.
I can see her hands, strong and sturdy even then.

The phrase rule of thumb comes from old English law -- wife-beating allowed if the stick's no bigger than his thumb.

When I told the story of how he beat me up, why, and how, his face cracked like neglected plaster in an empty house.

I could never believe it was happening. It was always a shock to be slammed sideways against a door.

He was careful not to break my glasses. Bruises-raw umber-don't show on the back of the head.

They told me it was good that I'd left when she was three. But the body never forgets, the body of the marriage.

A boy in the hospital named our daughter Lady of the Woods. She fell in love with crafts, working with her hands.

She made collages out of leaves, burned flowers into leather. I dreamed of blue and green hands floating along a red wall.

Sometimes life hangs on by a fragile thread. When she got out of the hospital her face was the color of milk.

It's the forever of it that I can't get used to, Tess cried, placing her black moon bracelet on our daughter's wrist.

For years I hated my Bride Doll. I was ashamed. Now she sits in honor, in her Chinese gold Lounging Pajamas.

Another woman said to me only this week: I dread Thanksgiving coming I was in such danger in my marriage.

50% of murdered American women are killed by their own husbands.

How can their daughters continue on?

In 1971, I was too scared to leave, knowing most women are not killed until they're on the run.

In 1976, they wouldn't give me a restraining order: doctors don't jeopardize their careers, they said.

As I packed, he said, you're lucky to be getting out alive. After that, whenever I left the house, I checked for cars, guns.

In 1981, my retinas detached themselves. The eye doctors wanted to know how many times I'd been hit in the head.

Overweight means I don't feel vulnerable. But my wrists give me away.

In 1988, a bill was proposed to the Minnesota
Legislature:
if a man shoots his wife in Deer Season, it's a
misdemeanor.

The body never forgets. Fear travels with me, at daycare, in the parking ramps.

Yesterday a grandmother's bones were found in the river willows. She was last seen at the Rosedale Mall, four months ago.

In the next town, a doctor shot his wife in the head. She was holding her children by the hand, walking out the door.

Danger is everywhere but we know that Rosedale is not where the worst danger lies.

It is difficult to determine the cause of death when only the bones are found.

Our daughter wears bells, ankle bracelets, silver rings. Her room, red and pink, with crystals and plants, her new life.

Her father can wander in his memory loss as I do in mine. I know why I've forgotten his naked body.

Doctor, lawyer, white-collar thief ... Why are educated men excused when they're

offenders?

Life hangs by a fragile thread.

At any moment it can snap, like the wishbone on

Thanksgiving.

When she got out of the hospital, we went to the Garden

of Eden.

She bought perfume made of cucumbers and honeydew.

She is bringing herself back to life.

All the whys dissolve into mystery.
```

---

## IC-1772: Collapse the Economy and Book of Rules . . .

- Title: Collapse the Economy and Book of Rules . . .
- Author (byline): Megan Falley, Olivia Gatwood and Nomy Lamm
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1075
- Already set (do not supply): none

### Source block (context only)

```text
Author: Megan Falley and Olivia Gatwood
ISBN: N/A
Publisher: Champagne in a Paper Cup
Date (Month/Year): June 13, 2016
Author: Nomy Lamm
Book: Word Warriors: 35 Women Leaders in the Spoken
Word
ISBN: 978-1580052214
Publisher: Seal Press
Date (Month/Year): Oct 2007
```

### Introduction (context only: never use it for content warnings)

```text
We women have been on diets for a while now. We know all the fashion and make-up tips and have read countless articles about being "the goddess" and "feminine power."

Yet we still feel insecure, distrustful of our bodies, and frequently sabotage ourselves by taking on too much. We are women and it’s time to cancel that gym membership and throw away those self-help articles!

Did you know that studies predict that if women stopped buying cosmetic products and services, every economy in the world would collapse overnight. This is a call to . . . Collapse the Economy by Megan Falley and Olivia Gatewood
```

### Performance text (classify this)

```text
Collapse the Economy Let’s cover our scented tampons in hairspray, light them

on fire, and throw them at Maybelline’s headquarters.

Let’s take all our leftover lotions and soaps and make the world’s largest slip-n-slide down Capitol

Hill.

Weight Watchers will have a whole new meaning, like, just wait and watch as I burn this *place* down.

Imagine — what could we do with all these Spanx? Probably make some sort of catapult to launch

our skin-softening bath bombs into enemy territory. Victoria’s Secret? Is that she’s GOING OUT OF

BUSINESS.

I have picked at my body like a scab. I have squeezed at my face in the mirror

until no more me could come out of me. I changed my outfit eight times before I got here.

Oh you thought we were gonna stop at burning bras? Well then you shouldn’t have given us so much flammable

shit.

Tampons, pads, even you Diva Cups, will be a thing of the past. Tonight, we paint the town red.

Are you gonna put those fake eyelashes on for me? No? Then I don’t want them.

Does that shampoo also come with the photoshop you used on the model? No? Then I don’t want it.

*Here’s to you*, Summer’s Eve. I’d rather NOT smell

like Island Splash or Delicate Blossom because what does that even smell like?

That’s not even a real scent. *I’m* already vajazzled enough.

Let’s throw out our razors and grow our hair as long as rivers.

How beautiful it will be to take the money I spend to be pretty for you, make my hair soft for you, my nails like candy for you, give myself skin cancer for you,

go under the knife for you and stop giving the 76 cents back.

There were days i spent hours crying in the dressing room. Days I didn’t leave

the house in case someone had a camera for fear of becoming another before picture.

So thank you, Cosmo for giving me 472 more beauty tips to completely ignore.

Thank you for all of this lipstick to write I AM FLAWLESS on the wall.

Thank you for the cover up, the vanishing cream.

Thank you for making us invisible that way, you’ll never see us coming.

Order book on-line at http://www.lulu.com/shop/megan-falley-and-olivia-gatwood/collapse-the-economy/paperback/product-22750832.html

TRANSITION We are dedicated, talented, brilliant women. Most of the time, we don’t know our brilliance. We are certain we “aren’t ready” to take on that next bigger role. We are more attuned to the ways we aren’t qualified than to the ways that we are. We wait for someone to validate, promote or discover us. Sound familiar? That’s because we’ve been coached by our society and have learned the . . . Book of Rules: A Girls Guide to Doing What You’re Told by Nomy Lamm

Book of Rules: A Girl’s Guide to Doing What You’re Told (Pg 210-2012)

Part 1.

you don't get to decide what you are what happens is, you are nothing, and then you pop out and the doctor says "boy" or else "girl" and that's that. for the rest of your life you are trying to be "boy" or

else "girl."

if you are very lucky, you will be called a man and you will feel like a man and everyone else will think you are a man and you will do all the things that real men are supposed to do and you will score lots of chicks. then you will be on top of the world, the pinnacle of success, a very powerful person. this is a catch-22

though, because if you are called a man and you feel like a man and everyone thinks you are a man and you do all the

things that real men are supposed to do, then chances are you are a a**hole [jerk] and i hate you.

if you are called a woman and you feel like a woman and everyone else thinks of you as a woman and you do

all the things that real women are supposed to do, then you are

probably miserable.

if, like most people, you lie somewhere in between or

beyond, then you are also probably miserable. (tough life.)

Part 2. The First Thing You Have to Do if You Want to Be a

Woman Is Be Pretty.

this is simple. To be pretty, all you need is to fulfill at least three of

these requirements: (a) a great tan; (b) long legs (two of them); (c) blonde;

(d) perky t*** [gesture to chest]; (e) button nose; (f) smooth skin; (g) slender waist;

(h) stare dumbly; (i) you are a doll; (j) a shimmery lipgloss; (k) a can of

diet coke; (l) a short skirt; (m) be on television

okay, count your points.
don't worry if you didn't quite make it
being pretty is all in the mind.
do this exercise:
every night before you go to sleep,
look in the mirror and say
"please god, you can take away all my friends and family,
make me into a moron,
send me to hell when i die, just please,
make me as beautiful as tori spelling."
if you don't want to look like tori spelling then too bad

for you because it doesn't work any other way. when you wake up you will be pretty.

Part 3.
your body is a whole entire beautiful magical universe
of its own, exactly right and perfect.
i know that this is not what you have been taught, but it

is

The Truth. how could anything so incredible ever be denigrated, scoffed at, invaded, discounted, spat on, violated,

ridiculed?
your body is magic.
what you are thinking now is:
why was i told to look at charts, diagrams, scales
and teen magazines to tell me what is wrong with me?
why wasn't i told to trust myself?
why did they make me feel like a horrifying ugly pathetic
puking loathsome monster,
if the truth is that i am magic?

as woman, you must learn to identify as an object. you must learn to be objectified, made ugly and

disgusting, but not in a way that is powerful or frightening to them-you will be made ugly in a putrid, rotting way.

your soul is the first to rot. then your heart, then your mind, then your flesh . . . whatever is left is the magical part that will live forever. this is the part of you that is eternal. your silicone implants.
```

---

## IC-1773: Contradictions-Tracking Poems

- Title: Contradictions-Tracking Poems
- Author (byline): Adrienne Rich
- Work: Your Native Land, Your Life: Poems
- Publisher: W. W. Norton & Company
- Publication date as stated: October 1993
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1385
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adrienne Rich
Book: Your Native Land, Your Life: Poems
ISBN: 978-0393310825
Publisher: W. W. Norton & Company
Date (Month/Year): October 1993
```

### Introduction (context only: never use it for content warnings)

```text
In the words of Adrienne Rich: The most notable fact our culture imprints on women is the sense of our limits. The most important thing one woman can do for another is to illuminate and expand her sense of actual possibilities. Through her poetry . . . . Rich chronicles her evolving understanding of intimacy. Her poetry expresses not only the experiences of a woman, a feminist, and a lesbian, but the experiences of all human beings working to maintain intimate relationships in a difficult world. Contradictions – Tracking Poems by Adrienne Rich
```

### Performance text (classify this)

```text
Look: this is January the worst onslaught
is ahead of us Don't be lured
by these soft grey afternoons these sunsets cut
from pink and violet tissue-paper by the thought
the days are lengthening
Don't let the solstice fool you:
our lives will always be
a stew of contradictions
the worst moment of winter can come in April
when the peepers are stubbornly still and our bodies
plod on without conviction
and our thoughts cramp down before the sheer
arsenal of everything that tries us:
this battering, blunt-edged life

Heart of cold. Bones of cold. Scalp of cold. the grey the black the blond

the red
hairs on a skull of cold. Within that skull
the thought of war the sovereign thought
the coldest of all thought. Dreaming shut down
everything kneeling down to cold intelligence
smirking with cold memory
squashed and frozen cold breath
half held-in for cold. The freezing people
of a freezing nation eating
luxury food or garbage
frozen tongues licking the luxury meat
or the pizza-crust the frozen eyes
welded to other eyes also frozen
Heart of cold Intelligence of cold
My country wedged fast in history
stuck in the ice

I'm calling you up tonight
as I might call up a friend as I might call up a
ghost
to ask what you intend to do
with the rest of your life. Sometimes you act
as if you have all the time there is.
I worry about you when I see this.
The prime of life, old age
aren't what they used to be;
making a good death isn't either,
now you can walk around the comer of a wall
and see a light
that already has blown your past away.
Somewhere in Boston beautiful literature
is being read around the clock
by writers to signify
their dislike of this.
I hope you've got something in mind.
I hope you have some idea
about the rest of your life.

I feel signified by pain
from my breastbone through my left shoulder
down through my elbow into my wrist is a thread of pain
I am typing this instead of writing by hand
because my wrist on the right side
blooms and rushes with pain
like a neon bulb
You ask me how I'm going to live
the rest of my life
Well, nothing is predictable with pain
Did the old poets write of this?
--in its odd spaces, free,
many have sung and battled --
But I'm already living the rest of my life
not under conditions of my choosing
wired into pain
rider on the slow train

Night over the great and the little worlds
of Brooklyn the shredded communities
in Chicago Argentina Poland
in Holyoke Massachusetts Amsterdam

Manchester

England
Night falls the day of atonement begins
in how many divided hearts how many defiant
lives
Toronto Managua St. Johnsbury
and the great and little worlds of the women
Something ancient passes across the earth
lifting the dust of the blasted ghettos
You ask if I will eat and I say, Yes,
I have never fasted
but something crosses my life
not a shadow the reflection of a fire
I came out of the hospital like a woman
who'd watched a massacre
not knowing how to tell
my adhesions the lingering infections
from the pain on the streets
In my room on Yom Kippur they took me off morphine
I saw shadows on the wall the dying and the
dead
They said Christian Phalangists did it
then Kol Nidre on the radio and my own
unhoused spirit trying to find a home
Was it then or another day
in what order did it happen
I thought They call this elective surgery
but we all have died of this.
Violence as purification: the one idea.
One massacre great enough to undo another
one last-ditch operation to solve the problem
of the old operation that was bungled
Look: I have lain on their tables under their tools
under their drugs from the center of
my body
a voice bursts against these methods
(wherever you made a mistake
batter with radiation defoliate c ut
away)
and yes, there are merciful debridements
but bums turn into rotting flesh
for reasons of vengeance and neglect.
I have been too close to septic too many times
to play with either violence or non-violence.

Lately in my dreams I hear long sentences
meaningless in ordinary American
like, Your mother, too, was a missionary of poets
and in another dream one of my old teachers
shows me a letter of reference
he has written for me, in a language
I know to be English but cannot understand,
telling me it's in "transformational grammar"
and that the student who typed the letter
does not understand this grammar either.
Lately I dreamed about my father,
how I found him, alive, seated on an old chair.
I think what he said to me was,
You don't know how lonely I am.

The problem, unstated till now, is how
to live in a damaged body
in a world where pain is meant to be gagged
uncured un-grieved-over The problem is
to connect, without hysteria, the pain
of anyone's body with the pain of the body's world
For it is the body's world
they are trying to destroy forever
The best world is the body's world
filled with creatures filled with dread
misshapen so yet the best we have
our raft among the abstract worlds
and how I longed to live on this earth
walking her boundaries never counting the
cost.

In a bald skull sits our friend in a helmet
of third-degree bums
her quizzical melancholy grace
her irreplaceable self in utter peril
In the radioactive desert walks a woman
in a black dress white-haired steady
as the luminous hand of a clock
in circles she walks knitting
and unknitting her scabbed fingers
Her face is expressionless shall we pray to her
shall we speak of the loose pine-needles how
they shook
like the pith of country summers
from the sacks of pitchblende ore in the tin-roofed
shack
where it all began
Shall we accuse her of denial
first of the self then of the mixed virtue
of the purest science shall we be wise for
her
in hindsight shall we scream It has come to this
Shall we praise her shall we let her wander
the atomic desert in peace?

You know the Government must have pushed them to
settle,
the chemical industries and pay
that hush-money to the men
who landed out there at twenty not for belief
but because of who they were and were called
psychos
when they said their bodies contained dioxin
like memories they didn't want to keep
whose kids came out deformed
You know nothing has changed no respect or
grief
for the losers of a lost war everyone hated
nobody sent them to school like heroes
if they started sueing for everything that was done
there would be no end there would be a
beginning
My country wedged fast in history
stuck in the ice

The Tolstoyans the Afro-American slaves
knew this: you could be killed
for teaching people to read and write
I used to think the worst affliction
was to be forbidden pencil and paper
well, Ding Ling recited poems to prison walls
for years of the Cultural Revolution
and truly, the magic of written characters
looms and dwindles shrinks small grows
swollen
depending on where you stand
and what is in your hand
and who can read and why
I think now the worst affliction
is not to know who you are or have been
I have learned this in part
from writers Reading and writing
aren't sacred yet people have been killed
as if they were

You who think I find words for everything
this is enough for now
cut it short cut loose from my words.
You for whom I write this
in the night hours when the wrecked cartilage
sifts round the mystical jointure of the bones
when the insect of detritus crawls
from shoulder to elbow to wristbone
remember: the body's pain and the pain on the
streets
are not the same but you can learn
from the edges that blur O, you who love clear
edges
more than anything watch the edges that blur
```

---

## IC-1774: From . . . Courage: Daring Poems for Gutsy Girls

- Title: From . . . Courage: Daring Poems for Gutsy Girls
- Author (byline): Gypsee Yo (Jonida Beqo); Mindy Nettifee;
- Work: Courage: Daring Poems for Gutsy Girls
- Publisher: Write Bloody Publishing
- Publication date as stated: March 2014
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1401
- Already set (do not supply): none

### Source block (context only)

```text
Authors: Gypsee Yo (Jonida Beqo); Mindy Nettifee;
Jeanann Verlee and Daphne Gottlieb
Book: Courage: Daring Poems for Gutsy Girls
ISBN: 978-1938912207
Publisher: Write Bloody Publishing
Date (Month/Year): March 2014
```

### Introduction (context only: never use it for content warnings)

```text
Courage is not a random act of bravery . . . running into a burning building or fighting crime. It is not reserved for heroes, or soldiers or men. Today, I’d like you to think about the concept of courage in a different way. Something I’ll call “everyday courage.”

Everyday courage is choosing to be brave when we are scared. Everyday courage is working to be better today than we were yesterday. Everyday courage isn't a destination - it's a choice. A choice that boys are often applauded for, and a choice that girls and women make quietly multiple times a day. A million times in their lives.

Envision these poetry snapshots of everyday courage and you may just see yourself, your mother, your sister, your friend.

These are poems from Courage: Daring Poems for Gutsy Girls by Gypsee Yo, Mindy Nettifee, Jeanann Verlee and Daphne Gottlieb
```

### Performance text (classify this)

```text
Jeanann Verlee and Daphne Gottlieb

Girl with Red Bicycle By Gypsee Yo (Jonida Beqo) (Pg 160)
The girl with the red limping bicycle
and scraped knees and hands wipes
tears with the hem of her dress, sore alone.

By now she knows boys
will always push her out
of the way, rather than lose
to a girl who is good at everything.

Boys, brothers, cousins, and friends
immune to the spell of blooming flowers
on summer frocks, unimpressed
with quick tongue and wit, tell her
the likes of her all die alone.

No man would chain his heart to hers, an anchor diving too deep to rescue.

The strap of her torn sandal,
unstitched like her pride, tugs her
ankle by the reins on the long way
home, that humbling walk across hot
pavement soft as bruised flesh.

Across the rooster yard of boyhood cacophony the bicycle chain drags on the ground like a white flag.

But she squeezes her fists until knuckle-white hands become walls her pride can lean on.

Let them sweat trying to catch my hair in the wind. I will ride.

I don't care if their feet never leave the shore. I will always dive, headfirst and unafraid.

No matter how deep the anchor plunges I will always rescue myself.

The First Time I Hit a Boy by Mindy Nettifee (Pg 64) It doesn't matter that I smile too big and too much, or that my looks shout warning like a poodle shouts guard

dog: he was dumb enough to say cruel things about my sister to my face. Hey, how come you turned out so pretty and she turned out so butt ugly? and then POP! KABLAM! or, you know, however the comic book boys would say it – I swung. Hard. And did not miss.

There's not much else to the story.
I'd never met my fist, and then I did.
I was twelve.
I had barely tasted anger.
It was like a mouth full of copper pennies.
Hate wishes.

The other kids just froze there in circle around us, their mouths opening on their hinges then rusting there. It hurt like hell when his braces grated my knuckles, and we both cried out like girls, though he squeaked more from trying to hold it in and looked genuinely hurt when he asked what did you do that for?

I was speechless, because I knew, but I didn't know.
I was as surprised as he was
to find I had fuses, to discover them blown.
Everyone stared and stared for the longest time
and then a few of the other boys started to laugh,
doubled over even.
There was a trickle of coins on the sidewalk
and then, then he was changed forever.

Fury and pity flickered on and off in me. This was also the first time I learned there were a thousand strangers inside of me. Some of them were violent. The only one with an answer to his question hadn't yet learned to speak.

Swarm by Jeanann Verlee (Pg 73) Learn how to say "no."

Cram that word inside your mouth, the whole thing, make sure all of it gets in there. Let it walk on your tongue. Practice with it in the mirror, push it out, make faces, learn to love the salt and bitter of it. Teach it to perch on your lip, buzz, collect pollen from your sugary gloss. Make it swarm between your cheeks.

Then, when the days come (there will be many) where he pushes too hard, speaks too sweetly, when the hand at your thigh draws a thump in your stomach, when the gremlin inside whispers it's not worth the fight, says you can barter for your worth tomorrow, when your ribs shrink, when he unfurls his Almighty Smile, when four come at you at once, when you love someone else, when the bar is closing and your name becomes Take What I Can Get, when the girls hate you anyway, when you want him until the burn if only he wore a different face --

pull back your lips, bare the teeth you have sharpened to their perfect points, flick your stinger tongue, set free your swarm.

Disciple by Mindy Nettifee (Pg 147-148)
The best advice I ever got about how to heal
came from a beleaguered camp counselor
who found herself suddenly surrounded
by a flock of heaving sobbing twelve year old girls.
It had been billed as a session on conflict resolution,
an alternative to wood cookie crafts, or horseshoes,
and maybe she should have seen it coming,
how water seeks the cracks in any dam.

One girl had been brutally sexually assaulted
by the preschool director, and had not slept
through the night alone since.
One had been molested by her foster brother,
who sliced his arms with scissors in the bedroom dark.
One had been strangled by her own mother,
who later found God and apologized,
and then punished her for not offering up

the fish and loaves of forgiveness instantly,
the forgiveness which her mother had been promised
by some pastor that she deserved now, and would receive
through the mysterious machines of grace;
the kind that multiplied and magnified and
fed the endless hunger at the center of things.
There were other stories.
Abuse is a word that sounds powerful in your head
and goes limp the moment you speak it,
hanging like a soaked wet curtain
around the things we cannot bear to know.
I don't remember the counselor's name, or
what she looked like, just that she was an enormous
buoy of a woman. That her voice was deep
and calm and quavered at all the right turns.
That she sat in a way that trained gravity.

How unprepared she must have felt, to see the sharks swimming in our eyes, to have been handed the heavy anchors of our trust. What well of strength did she draw from? What inheritance of bedrock and granite and spine? What gospel stolen from the bent melted steel of kitchen

knives? She absorbed every blow of every word. When we had finished, when we were softened

by confession, she took a breath and began.
Without getting into the kind of details that get attention,
she told us the story of her own early ruin,
of the lifetimes of gentle obligation it left in its wake.

The heart and the mind and the body
might never align on the requirements of joy.
The mind must be taught patience with the heart.
The heart must learn faith from the body.

The body must be tended lovingly and unwaveringly, an

infant. The heart will take its own sweet time, and cannot be

rushed.
"Just fake it 'till you feel it," she told us,
and like that, gave us permission
to put on the tight masks of adulthood,
to build walls around what was
too tender and shocked;
to survive.

In Case You Ever Need It, It is Here by Daphne Gottlieb (Pg
74-75)
Take this as yours
Rip this from the book
or make a copy
fold it in half
and half again
and put it in your wallet
or between the mattress and the box spring
or taped under your desk
so it is there
if.

Know this: what happened
to your body
to your head
to your heart
is not your fault.
It is not something you
deserved or caused.

It is like blaming yourself
for someone hitting your hand
with a hammer.
(if that person is you,
put the hammer down.
Let it be an accident.
Let it be the end.)

The body, heart, brain knows
how to heal. It knows how to knit
back together. How to suture
and secure. Let it do what it does.
Your body is yours. Your body
will always be yours.

You are not what happened. Your whole life is not just this. You do not speak a language made of this, this is not your name.

Your name is your own.

Let your name be
The name of someone who
can do the unthinkable:
Stands up and keeps moving.
You are standing. You are taking
a shower and eating breakfast.
You are going to classes
or going to work. You are doing
impossibly hard things. Keep going
and keep going and there
is summer. Laugh even if it is
with rage. Open your mouth
and your fists. Tell the truth.
Tell a friend. Listen to someone
else's heart. It is beating
a miracle. You are
Both here.

When scars are new, They shine. Be all the glitter You need.
```

---

## IC-1775: Credo

- Title: Credo
- Author (byline): Craig Lucas
- Work: What I Meant Was
- Publisher: Theatre Communications Group
- Publication date as stated: June 1999
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1219
- Already set (do not supply): none

### Source block (context only)

```text
Author: Craig Lucas
Book: What I Meant Was
ISBN: 978-1559361590
Publisher: Theatre Communications Group
Date (Month/Year): June 1999
```

### Introduction (context only: never use it for content warnings)

```text
It used to be all the rage to write a "personal creed." When "honor" wasn't looked at as something to avoid, "compassion" wasn't an indication of weakness, and "armed forces" weren't something to avoid at all costs, men and women took the time to figure out what make themselves tick. Determining what you believe, what you value, and where you want to place your time and effort can give you a certainty about your life like nothing else can. Determining what you're all about...your mission statement, if you will...makes it so you know in advance what you will and won't do in life. What’s your Credo by Craig Lucas.
```

### Performance text (classify this)

```text
It's Christmas eve, I go out with the dog. Jim and I have just broken up. I've just been to an AA meeting Where a woman got up And said she had no friends, Her best friend is her VCR And it's broken.

I came home to the hole where the sofa was.
There's no Christmas tree either.
I can't stand the thought of sweeping up all the dead
needles
And dragging the carcass out to the street
To join all the other dead trees
With what's happening to the rain forest.
I know the two aren't connected,
But anyway, I pull up a folding chair
And heat up a piece of cold pizza.
This, I think, is the low point.
The walls show little ghosts where the pictures once
were.
I go out.

Did I tell you I didn't get my Christmas bonus?
Well, I wasn't expecting it,
But I haven't been able to take Apple to the vet about
her problem,
So she dribbles a little across the lobby,
Past the doorman who isn't smiling at me;
I'm sure it's because I haven't given him his Christmas
bonus,
But maybe's it's the trail of urine, too,
I don't stop to ask.
I smile bravely
And step outside where it has of course started to rain.
.
And people are running and looking very upset.
Surely the rain isn't that bad.
I turn
There's been an accident on my corner
I snap my head away,
I know if I look there'll be a baby carriage there
ln the middle of the street.
I refuse to look.
They certainly don't need another person standing
around not doing anything.
I put my mind ... Where can I put my mind?
Vienna.
Where Jim has gone with the woman he left me for.
You can't escape these thoughts.

All I know is her name.
Her name ... is Carmella.
Apparently.
And I believe that she has had a sex change.
As far as I know, this has no basis in fact,
But I believe it as firmly as-I believe
That there is nothing wrong with New York City
That can't be solved at least in part by keeping
Cardinal John J. O'Connor out of city politics
And back doing what he really does best
Which, if we are to take his word for it, is:
Exorcisms.

Where,
Where can I put my thoughts?
Ecuador.
My parents are in Ecuador.
They asked me to join them,
And I said
No, Jim and I would be spending the holiday together.
I hope that he and Carmella are caught
In the crossfire of some terrorist ...
No, I don't .
Not really. But you know:
The sort of thing you see
On the evening news.
If you have a TV
Or a phone.
Jim stopped paying the bills months ago,
As a kind of secret warning of what was to come.
But I refuse,
In my bones I refuse
To see myself as a victim.
I have gotten myself into this.
I allowed him to talk me into maintaining a joint bank
account.
Every time a little voice in my head would say
Watch out.
He's cute,
But he's not that nice.
Beneath it all,
Behind the charm,
His chin,
That first night,
And then again in Barbados,
Beneath it all
Is him.
I alone took each and every step
Which brought me here
To this street corner
In the rain
On Christmas eve
With my dog whose urinary infection
I cannot afford to fix.
And at that moment, my friends,
My dog squats.
And the worst thing that has ever happened to me
Unfolds before my very eyes.
A wire, loose plug from somebody's Christmas
decorations
Carelessly strung in front of their little tea shop ...
Electrocutes my dog.
And she falls immediately dead
On the sidewalk
In a sputter of sparks ...
And the lights go out all down the front of the tea shop.
And a man comes out:
"What did you do?"
And I drop to my knees, unafraid,
Let me die, too,
Electrocute me.
And I embrace my dog, Apple,
Whom I have had for sixteen years.
She is my oldest friend.
She has seen me in my darkest, most drunken days.
She has been to every corner of my life,
She growled at the dogs on the dog food commercials.
She has been across the country and back.
Apple, I'm not afraid to say, is the purest,
Most uncomplicated expression of love I have ever
known.
And she has been killed by an electric current
In the last sick days of her valiant existence.

The man stares at me from above.
"Oh my god" he says.
He can't believe it
Any more than I can believe it.
Come in, he says.
We carry Apple into the shop.
To me she smells good,
But to some people she does not.
It's been too cold to bathe her.
It's hard for one person to hold her in the shower.
She doesn't like the water.

The man offers me the only thing he has.
Tea.
We talk
And he assures me that the accident on the corner
Did not involve a child.
And no one was killed.
What to do now with Apple?
I can't cry anymore.
I have cried so much the last two weeks
I can't cry for her now.
And I know ...
In some way I see all at once that
Jim was not really good enough for me,
That I will meet someone else.
And even if I don't I will have
An extraordinary and rich and complicated life.
It is entirely up to me.
I will most likely survive all the roadblocks and the
detours.
As my dad always says:
"Life can be rough, but think about the alternative."

But then again
He's never been sick a day in his life.
He hasn't ever had to struggle just to stand
Or been unable to stop himself from peeing
Where he knows he shouldn't
And doesn't want to,
But there it is in a stream,
Surprising him and me.

He's never had to look up
With big sorrowful eyes which say:
"I had no idea.
Don't yell."

No.
I only hope that 1 will go as quickly as Apple
When the time comes.
And if I don't,
I will absolutely,
I know I will face that bravely
And with dignity.
I know.
And if,
For some unforeseen but totally justified reason,
I can't,
And I am making a complete ass of myself,
Saying things I wouldn't ever say
And acting childishly
And turning into a prude
And a conservative
And am being a complete drag on everyone
For months and years,
I know my friends will forgive me.

And if for some equally valid and twisted,
But ultimately logical reason,
They don't
Or they can't,
Or they're all dead by then,
Or it's August and they're away
Then I will forgive them,
Right?
The same way I forgave myself
For yelling at Apple the first time she peed
Before I realized what was going on.

And if. ..
Again, if I can't,
And everything is entirely for shit
And I can't even find my way to the end of a sentence ...
And ... you can fill in all the blanks ...

That will be fine, too.
```

---

## IC-1776: Crescent Moon Like a Canoe

- Title: Crescent Moon Like a Canoe
- Author (byline): Marge Piercy
- Work: The Moon is Always Female
- Publisher: Knopf
- Publication date as stated: March 1980
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 701
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marge Piercy
Book: The Moon is Always Female
ISBN: 978-0394738598
Publisher: Knopf
Date(Month/Year): March 1980
```

### Introduction (context only: never use it for content warnings)

```text
Marge Piercy credits her mother with making her a poet. She was an emotional, imaginative woman full of odd lore and superstitions. She read voraciously and encouraged her daughter to do the same. Enormously curious , she urged her daughter to observe sharply and remember what she observed. As Piercy grew older and became more independent, they fought viciously. Finally, Piercy left home at seventeen and recalls that she and her mother were not really in sustained harmony until very late in her mother’s life. Her mother died in 1981. Crescent Moon Like a Canoe is a sad, courageous and moving poem that is not only about Piercy’s mother but about her own motives for poetry. This poem is both wide open and fully controlled, flexible, tender, clear-sighted and compassionate – It is an act of forgiveness. Crescent Moon Like a Canoe by Marge Piercy
```

### Performance text (classify this)

```text
This month you carried me late and heavy
in your belly and finally near Tuesday
midnight you gave me light and life, the season
Kore returns to Demeter, and you suffer
and I cannot save you though I burn with dreams.

Memories the color of old blood,
scraps of velvet gowns, lace, chiffon veils,
your sister's stage costumes (Ziegfeld
didn't stint) we lingered together, you
padding in sneakers and wash-worn housedresses.

You grew celery by tucking sliced off
bottoms in the soil. You kept a compost
pile in 1940. Your tomatoes glowed
like traffic signals in the table-sized yard.
Don't kill spiders, you warned.

In an asbestos box in Detroit where sputtering
factories yellow the air, where sheets
on the line turn ashen, you nurtured
a backyard jungle. Every hungry cat
wanted to enter and every child.

You who had not been allowed to finish
tenth grade but sent to be a frightened
chambermaid, carried home every week
armloads of books from the library
rummaging them late at night, insomniac,

riffling the books like boxes of chocolates searching for the candied cherries, the nuts, hunting for the secrets, the formulae, the knowledge those others learned that made them shine and never ache.

You were taught to feel stupid; you
were made to feel dirty; you were
forced to feel helpless; you were trained
to feel lost, uprooted, terrified.
You could not love yourself or me.

Dreamer of fables that hid their own
endings, kitchen witch, reader of palms,
you gave me gifts and took them back
but the real ones boil in the blood
and swell in the breasts, furtive, strong.

You gave me hands that can pick up
a wild bird so that the bird relaxes,
turns and stares. I have handled
fifty stunned and injured birds and killed
only two through clumsiness, with your touch.

You taught me to see the scale on the bird leg, the old woman's scalp pink as a rose under the fluff, the golden flecks in the iris of your eye, the silver underside of leaves blown back. I am your poet, mother.

You did not want the daughter you got.
You wanted a girl to flirt as you did
and marry as you had and chew the same
sour coughed up cud, yet you wanted too
to birth a witch, a revenger, a sword
of hearts who would do all the things
you feared. Don't do it, they'll kill
you, you're bad, you said, slapping me down hard
but always you whispered, I could have!
Only rebellion flashes like lightning.

I wanted to take you with me, you don't
remember. We fought like snakes, biting
hard at each other's spine to snap free.
You burned my paper armor, rifted my diaries,
snuffed my panties looking for smudge of sex,

so I took off and never came back. You can't imagine how I still long to save you, to carry you off, who can't trust me to make coffee, but your life and mine pass in different centuries, under altered suns.

I see your blood soaking into the linoleum,
I see you twisted, a mop some giant hand
is wringing out. Pain in the careless joke
and shouted insult and knotted fist. Pain like knives
and forks set out on the domestic table.

You look to men for salvation and every year
finds you more helpless. Do I battle
for other women, myself included,
because I cannot give you anything
you want? I cannot midwife you free.

In my childhood bed we float, your sweet
husky voice singing about the crescent
moon, with two horns sharp and bright we would
climb into like a boat and row away
and see, you sang, where the pretty moon goes.

In the land where the moon hides, mothers
and daughters hold each other tenderly.
There is no male law at five o'clock.
Our sameness and our difference do not clash metal
on metal but we celebrate and learn.

My muse, your voice on the phone wavers with tears. The life you gave me burns its acetylene of buried anger, unused talents, rotted wishes, the compost of discontent, flaring into words strong for other women under your waning moon.
```

---

## IC-1777: The Cry of the Children . . . Listen to Me

- Title: The Cry of the Children . . . Listen to Me
- Author (byline): Elizabeth Barrett Browning and Ralph Roughton, MD
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1647
- Already set (do not supply): none

### Source block (context only)

```text
Author: Elizabeth Barrett Browning
Book: Aurora Leigh and Other Poems
ISBN: 978-0140434125
Publisher: Penguin Classics
Date (Month/Year): May 2006
Author: Ralph Roughton, M.D
Book: The 8th Habit: From Effectiveness to Greatness
ISBN: 978-0762428533
Publisher: Running Press Miniature Editions
Date (Month/Year): May 2006
```

### Introduction (context only: never use it for content warnings)

```text
Can you hear it? Echoing from the cavernous history that is ours? Echoing across oceans and cultures? Please listen . . . it’s The Cry of the Children by Elizabeth Barrett Browning.
```

### Performance text (classify this)

```text
The Cry of the Children

Do ye hear the children weeping, O my brothers, Ere the sorrow comes with years? They are leaning their young heads against their mothers, And that cannot stop their tears. The young lambs are bleating in the meadows, The young birds are chirping in the nest, The young fawns are playing with the shadows, The young flowers are blowing toward the west— But the young, young children, O my brothers, They are weeping bitterly! They are weeping in the playtime of the others, In the country of the free.

Do you question the young children in their sorrow,
Why their tears are falling so?
The old man may weep for his tomorrow,
Which is lost in Long Ago;
The old tree is leafless in the forest,
The old year is ending in the frost,
The old wound, if stricken, is the sorest,
The old hope is hardest to be lost:
But the young, young children, O my brothers,
Do you ask them why they stand
Weeping sore before the bosoms of their mothers,
In our happy Fatherland?

They look up with their pale and sunken faces,
And their looks are sad to see,
For the man's hoary anguish draws and presses
Down the cheeks of infancy;
"Your old earth," they say, "is very dreary;
Our young feet," they say, "are very weak!
Few paces have we taken, yet are weary—
Our grave-rest is very far to seek.
Ask the aged why they weep, and not the children,
For the outside earth is cold,
And we young ones stand without, in our bewildering,
And the graves are for the old."

"True," say the children, "it may happen
That we die before our time.
Little Alice died last year—her grave is shapen
Like a snowball, in the rime.
We looked into the pit prepared to take her:
Was no room for any work in the close clay!
From the sleep wherein she lieth none will wake her,
Crying 'Get up, little Alice! it is day.'
If you listen by that grave, in sun and shower,
With your ear down, little Alice never cries;
Could we see her face, be sure we should not know her,
For the smile has time for growing in her eyes:
And merry go her moments, lulled and stilled in
The shroud by the kirk-chime.
It is good when it happens," say the children,
"That we die before our time."

Alas, alas, the children! They are seeking Death in life, as best to have; They are binding up their hearts away from breaking, With a cerement from the grave. Go out, children, from the mine and from the city, Sing out, children, as the little thrushes do; Pluck your handfuls of the meadow-cowslips pretty, Laugh aloud, to feel your fingers let them through! But they answer, "Are your cowslips of the meadows Like our weeds anear the mine? Leave us quiet in the dark of the coal-shadows, From your pleasures fair and fine!

"For oh," say the children, "we are weary,
And we cannot run or leap;
If we cared for any meadows, it were merely
To drop down in them and sleep.
Our knees tremble sorely in the stooping,
We fall upon our faces, trying to go;
And, underneath our heavy eyelids drooping,
The reddest flower would look as pale as snow.
For, all day, we drag our burden tiring
Through the coal-dark, underground;
Or, all day, we drive the wheels of iron
In the factories, round and round.

"For all day the wheels are droning, turning;
Their wind comes in our faces,—
Till our hearts turn, our heads with pulses burning,
And the walls turn in their places:
Turns the sky in the high window blank and reeling,
Turns the long light that drops adown the wall,
Turn the black flies that crawl along the ceiling,—
All are turning, all the day, and we with all.
And all day, the iron wheels are droning,
And sometimes we could pray,
'O ye wheels,' (breaking out in a mad moaning)
'Stop! be silent for today!' "

Ay, be silent! Let them hear each other breathing
For a moment, mouth to mouth!
Let them touch each other's hands, in a fresh wreathing
Of their tender human youth!
Let them feel that this cold metallic motion
Is not all the life God fashions or reveals:
Let them prove their living souls against the notion
That they live in you, or under you, O wheels!
Still, all day, the iron wheels go onward,
Grinding life down from its mark;
And the children's souls, which God is calling sunward,
Spin on blindly in the dark.

Now tell the poor young children, O my brothers, To look up to Him and pray; So the blessed One, who blesseth all the others, Will bless them another day. They answer, "Who is God that He should hear us, While the rushing of the iron wheels is stirred? When we sob aloud, the human creatures near us Pass by, hearing not, or answer not a word. And we hear not (for the wheels in their resounding) Strangers speaking at the door: Is it likely God, with angels singing round Him, Hears our weeping any more?

"Two words, indeed, of praying we remember, And at midnight's hour of harm, 'Our Father,' looking upward in the chamber, We say softly for a charm. We know no other words except 'Our Father,' And we think that, in some pause of angels' song, God may pluck them with the silence sweet to gather, And hold both within His right hand which is strong. 'Our Father!' If He heard us, He would surely (For they call Him good and mild) Answer, smiling down the steep world very purely, 'Come and rest with me, my child.' "But, no!" say the children, weeping faster, "He is speechless as a stone: And they tell us, of His image is the master Who commands us to work on. Go to!" say the children,—"up in heaven, Dark, wheel-like, turning clouds are all we find. Do not mock us; grief has made us unbelieving— We look up for God, but tears have made us blind." Do you hear the children weeping and disproving, O my brothers, what ye preach? For God's possible is taught by His world's loving, And the children doubt of each.

And well may the children weep before you!
They are weary ere they run;
They have never seen the sunshine, nor the glory
Which is brighter than the sun.
They know the grief of man, without its wisdom;
They sink in man's despair, without its calm,—
Are slaves, without the liberty in Christdom,—
Are martyrs, by the pang without the palm,—
Are worn as if with age, yet unretrievingly
The harvest of its memories cannot reap,—
Are orphans of the earthly love and heavenly.
Let them weep! let them weep!

They look up with their pale and sunken faces, And their look is dread to see, For they mind you of their angels in high places, With eyes turned on Deity;— "How long," they say, "how long, O cruel nation, Will you stand, to move the world, on a child's heart,— Stifle down with a mailed heel its palpitation, And tread onward to your throne amid the mart? Our blood splashes upward, O gold-heaper, And its purple shows your path! But the child's sob in the silence curses deeper Than the strong man in his wrath."

TRANSITION Unfortunately the narrative Browning penned nearly a century ago has NOT become a distant memory of atrocity for ALL nations of the world. Today, an estimated 250 million children between the ages of five and 14 still work, half of them full time, and tens of millions work under conditions that threaten terrible harm to their physical, moral, and intellectual development. The problem is urgent, but distant from our own lives in the United States today. Within our nation’s boarders THIS type of abuse has been virtually eliminated; however, a less public form of abuse continues to plague our children: breaking spirits, emotionally crippling the next generation of adults just as surely as toiling in the mines killed and disfigured our children 100 years ago. The children still are weeping . . . Listen to Me by Ralph Roughton, M.D.

Listen to Me

When I ask you to listen to me
and you start giving advice,
you have not done what I asked.
When I ask you to listen to me
and you begin to tell me why I shouldn't feel
that way, you are trampling on my feelings.
When I ask you to listen to me
and you feel you have to do something to
solve my problem, you have failed me,
strange as that may seem.

Listen! All I asked was that you listen,
not talk or do --- just hear me.
Advice is cheap: 10 cents will get you both Dear Abby
and Billy Graham in the same newspaper.
And I can do for myself. I'm not helpless.
maybe discouraged and faltering, but not helpless.
When you do something for me that I can and need
to do for myself, you contribute to my fear
and inadequacy.

But when you accept as a simply fact that I do
feel what I feel, no matter how irrational,
then I can quit trying to convince you and can
get about the business of understanding what's
behind this irrational feeling.
And when that's clear, the answers are
obvious and I don't need advice.

Irrational feelings make sense when we understand what's behind them. Perhaps that's why prayer works, sometimes, for some people --- because God is mute, and He/She doesn't give advice or try to fix things. "They" just listen and let you work it out for yourself.

So please listen and just hear me. And, if you want to talk, wait a minute for your turn, and I'll listen to you.
```

---

## IC-1778: Dark Daughter

- Title: Dark Daughter
- Author (byline): Nicole Blackman
- Work: Blood Sugar, Pg 88+
- Publisher: Akashic Books
- Publication date as stated: May 2002
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1378
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nicole Blackman
Book: Blood Sugar, Pg 88+
ISBN: 978-1888451344
Publisher: Akashic Books
Date (Month/Year): May 2002
```

### Introduction (context only: never use it for content warnings)

```text
*According to the Medical Director of the Child Mind Institute, Harold Koplewicz, in the US, 17 million young people have been diagnosed with a mental heal disorder by the age of 18. Girls, in particular, are struggling. The CDC reports that in 2021 one in three had seriously contemplated suicide – an increase of 60 percent in 10 years. But despite the growing numbers, few seek care or support due to the deeply ingrained stigma that still surrounds mental health treatment.

In Dark Daughter by Nicole Blackman, we are allowed into a personal and very frank conversation the speaker has with her mother. The words are dark, often brutal, but undeniably an honest insight into her struggle.

Dark Daughter by Nicole Blackman.
```

### Performance text (classify this)

```text
(Pg 88+) I am not of this family, I know that now and I am not of your skin. When you slit your wrists, you bled red.

When I slit mine, I bled mud, You and your pills will search for me search for my

salvation,
will question the beginning of when I first fell and
offer explanations to explain me away.
The cloak of the neighbors, the neighbors
is all that causes you to quiet me.

No, you never ask about these brain movies.
No, you never talk me down from the balcony.
I count steps (sixteen from closet to bed)
and breaths taken in a day.

Cold numbers are warm comfort to me
as you can no longer comfort your dark daughter.
Every morning I am a new me and
select my persona from a deep closet.

I swoop down stairs
on fire, on stage.
Stop accusing me mother, I did not choose this.
No human hopes for a touch of mercury on the mind.

Some people don't go crazy.
Some of us were always there.
While you were having breakfast I was having visions
and I am slowly being rocked away from you.

Me, this baby that still wails away with no cause. I am slowly being rocked away from you. Four years ago, in the middle of dinner, I interrupted

and said Pardon Me, But I Can Feel Pain In The Ends Of My Hair.

You put down your fork then, you put down your fork
and fixed your attention on a girl grown wild
when you weren't looking.
Take away my hands, they weigh too much.
This body is not me, it's just where I live for a while.

I am more lucid when I give in
and I disintegrate regularly.
The crazier I am the stronger I am.
Feel the cells shift.
Listen to the bones slide.

You hold me like a kite with a too long string.
Once I hit sky you'll let go.
I've begun my descent into self, into soul.
I've begun my descent and everything's fine
I've begun my descent and can't get off of the train.
I've begun my descent and you cannot come with me.

I look up to the showerhead, waiting for water. Cold shock hits hard and slams night through bones and skin and soul and brain and what was me. Shudder and tremble and grasping the railing.

Damn your therapies
that leave me gasping
that turn me twice before I talk
leaving me with a long longing.
Self-help therapy helps no one.

Notebooks will not help me spew disease.
Medication cannot get me out of my head.
You cannot liberate me from this.
I am this.

With a delicious shove I went over.

And you are lucky, mother, you are lucky.
I don't know the reason I am the way I am
so I wander round the house without a map
saying I am not this, I am not that, but I do not know
what I am.

The doctors define me by saying what my problem is

not but throw up their hands when faced with a brain beyond the radar, a gray lump more formidable than their garden of books.

Give me some quality time with a trio of experts
tops in their field.
Don't hold me down, I'm not doing anything.
I'm just thinking.

I ask angels for prayers to string into a necklace and
wear round my neck.
I lean against walls waiting for the day
when they open up and I fall in.

I am light with an awful lightness and drum my way through night.

I am not rid of this fungus, all the doctors will not cut it
away.
No surgeon will open my brain and let the wrong leak
out.
If they drill my skull the demons might escape
might take hold of their million dollar hands,
might hold on and bite down hard.

Don't you wish I was an abortion, mother?
Don't you churn at night and wish you had the choice
again?
Don't you dream of laying a pillow on my face
and throwing me out with the trash in the morning?

I will rise up at midnight.
I will rise up and put on my wings to sweep over you.
I will rise up and hover in sky, in night.
I will rise up and forgive you your trespasses.

Use your hands and get me out of the straps. Sign the forms and set me free. Say you do not understand me, but you believe me, mother. Release me from this white white white room unlike heaven.

Brain highways lead back to spine, back to the problem. I'm crawling out of this wrecked car but no one really wants to see me get up and walk away. Trying to think takes up too much time.

The most the doctors hope for is to discover that my lunacy is new is nameable with my last name, is discoverable for their medical books. I might be an award, I might be an article, I might be a non-profit organization. I might be noble but I am a loss to everyone involved.

If the bad side of you kills
and takes over the good side
is it a little murder?
Would anyone notice?

The neighbors say
We're so sorry to hear that
your daughter's brains
are dripping out her ears.

Am I crazy?
I am free with a horrifying freedom
and my world is full of flowers
and flame.

My typewriter scurries in the middle of the floor like a rat and the bedsheets rise up, waves in a cold ocean. Moonbeams are crystal bars that nail me to the bed and cobwebs vibrate into scary nets for when I fall.

I am a thirty foot spire of unhuman girlstone
standing on top of the shoulders of unclaimed ghosts.
I am everything you fear
you will become.

Crash through queen glass and say I was right all along. Rock this skeleton that has no use for blood or sense. Throw stones at me so I can build a crazy house. Stuff me with paper so I am full of nothing and therefore new.

I want to shave my head. Get closer to the shrine. Find out why this globe at the top of my body rules the rest of me so wrong. I want to touch the disease. I want to know where I've been hit.

I have nothing to miss, no memories to wander over.
I rub my arms over the spackled walls and
wait for them to tip over
become floor, become sky.

You come up to my room
quietly, on the pretense of a lie
and touch the door
with scared, careful hands.

You want your heavy heart
to be relieved of 110 pounds
of bad choices
and bad memories.

This little problem is mine
I'll give it a name
I'll give it somewhere to stay
I'll take care of it.

I'll watch it grow up and take over
I'll take care of it now because I can
I guess that makes me my own little mother,
mother.

Don't try to open the door, mother, this poem is all mine. Finally, something is mine and makes sense.

With a delicious shove, I go over again. Big words reach up!

I swim over that wet line
and keep swimming.
I dig fingernails into stars
and feel my feet lightly brush planets.

Drummers thunder in my skull because there is no heartbeat to confuse them. The thumps rock me against chair. Color TV hums. Pillow shreds. Window releases. Cat opens mouth, spits out bible.

I will come back in splinters
in blood in your hand.
I am looking through lightbulbs
and the storms keep coming.
The walls are crawling now, the candles are cracked.
I am listening for my breath in the paper.
Am clean, on fire.
Feels like water breaking.

All this is sleek and cut and fast.
I am to go free.
I am throwing up snow
I am spitting out keys.
This is a hate house
and you're breathing me in
you're breathing this sickness in.
Now I'm inside you again.

It's time to go and all my words make me strong

Mother, I'm already gone.
```

---

## IC-1779: The Day that was That Day!

- Title: The Day that was That Day!
- Author (byline): Amy Lowell
- Work: Selected Poems of Amy Lowell
- Publisher: Houghton Mifflin Co
- Publication date as stated: 1928
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1301
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amy Lowell
Book: Selected Poems of Amy Lowell
ISBN: B000IE9X9W
Publisher: Houghton Mifflin Co
Date (Month/Year): 1928
```

### Introduction (context only: never use it for content warnings)

```text
Many a farm wife has been driven to near insanity by the unending monotony of her life. In The Day that was That Day! By Amy Lowell, Minnie is to the point of considering suicide to end the monotony. The Day that was That Day! By Amy Lowell.
```

### Performance text (classify this)

```text
The wind rose, and the wind fell, And the day that was that day Floated under a high Heaven.

“Home! Home! Home!”
Sang a robin in a spice-bush.
“Sun on a roof-tree! Sun on a roof-tree!”
Rang thin clouds
In a chord of silver across a placid sky.

Rachel Gibbs stepped up the path
To pass the time of day
With Haywood Green’s Minnie.
“My, ef she ain’t shut the door!
An’ all the breeze this side the house too.
She must like to stew.
Minnie,
Minnie,
You ain’t gone out have yer?
I’ll skin my knuckles ef I knock agin.
I wonder did she lock the door—
Well, I never!
Have you gone hard o’ hearin’?
Have you—
Minnie, child, what’s the matter?
Why do you look like that?
What you doin’?
Speak, I tell yer!
What you hidin’ that cup for?
God A’mighty, girl, what you doin’ with wood-alcohol
In a drinkin’-cup?
Here give it ter me,
An’ I’ll set it on the table.

Set down, Minnie dear,
Set right here in the rocker
An’ tell me
What ails yer to be wantin’
To drink stuff like that?
There, there, you poor lamb.
Don’t look so scared.
Just tell me all about it,
An’ ease your heart.
Minnie, I’ll have to shake yer
Ef you don’t stop starin’
In that dretful way.
Poor Dear,
You just lay your head up agin me
An’ let me soothe yer.

Poor little thing. Poor little thing.”

“Don’t, don’t, Rachel,
I can’t bear it.
I’m a wicked woman,
But I jest couldn’t stand no more.”

“No more o’ what?
Ain’t yer Pa good to yer?
What’s come over yer, Minnie?
My! I’m jest as sorry as I can be.”

“Oh, it ain’t nothin’ like that.
An’ don’t be so good to me,
You’ll make me want to cry agin,
An’ I can’t cry.
I’m all dried up,
An’ it’s like squeezin’ my heart sick
To want to cry, an’ can’t.”

“But what is it? Ain’t yer never goin’ ter tell me?”

“Why there ain’t nothin’ to tell ’Cept that I’m tired.”

“Now, look-a-here, Minnie, No one don’t drink poison jest ’cause they’re tired.”

“I didn’t drink it, as it happens.”

“No, you didn’t, ’cause I come in an’ stopped yer. But I’m mighty afeered you would have. Lord, it makes me shudder.”

“I guess yer right,
I would have.
An’ I wish you’d ha’ let me be.
Now it’s all to do over agin,
An’ I don’t know as I’ll git the courage a second time.
I guess you ain’t never been right down tired, Rachel.”

“Well, never to the poison point, no, I haven’t. But what’s gone wrong to wear yer out so?”

“The cat’s sick.”

“Minnie Green, was you takin’ poison ’Cause you got a sick cat? That’s down-right foolishness.”

“Yes, it does sound so.
But I couldn’t face nussin’ her.
Look here, Rachel,
I may be foolish, or mad, or jest plain bad,
But I couldn’t stan’ another thing.
I’m all fretted now
An’ more’s one too many.
I can’t go on!
Oh, God! I can’t go on!
I ain’t got no more’n most women,
I know that,
But I fuss a lot more.
There’s al’ays the same things
Goin’ roun’ like the spokes to a cart-wheel,
Ef one ain’t a-top it’s another,
An’ the next comin’ up all th’ time.
It’s breakfast, an’ dinner, an’ supper,
Every day.
An’ the same dishes to wash.
I hate them dishes.
I smashed a plate yesterday
’Cause I couldn’t bear to see it
Settin’ on the sink waitin’ fer me.
An’ when I go up to make Father’s bed
I git seasick
Thinkin’ I’ll have to see that old check spread agin.
I’ve settled it,
An’ twitched it this way an’ that,
For thirty year,
An’ I hate the sight o’ the thing.
Sometimes I’ve set an hour on the stair
Ruther’n go in an’ touch it.

Oh, my God! Why couldn’t yer let me be?
Why’d you have to come interferin’?
Why?
Why?”

“Thank the Everlastin’ Mercy I did! But, Minnie, how long’s this been goin’ on? I never had no idea anythin’ was wrong.”

“I don’t know.
For ever an’ ever, I guess.
Rachel, you can’t think how hard it is for me
To set one foot after the other sometimes.
I hate lookin’ out th’ winder,
I’m so tired o’ seein’ the path to the barn.
An’ I can’t hardly bear
To hear Father talkin’ to the horses.
He loves ’em.
But I don’t love nothin’
’Cept the cat,
An’ cats is cold things to cling to,
An’ now mine’s sick!”

“Don’t take on so, Minnie.
She’ll get well.
There, you rest awhile;
You can tell me afterwards.”

A wind rose, and a wind fell, And the day that was that day Hung against a turning sun.

The robin sang “Home! Home! Home!”
In an up-and-down scale of small, bright notes.
The clouds rang silver arpeggios
Stretched across a pleasant sky.

“I wish I loved somethin’, Rachel.”

“Bless your heart, Child, don’t you love your father?”

“I suppose so. But he don’t mean nothin’ ter me.

He don’t say nothin’ I want ter hear.
My ears is achin’ to hear words,
Words like what’s written in books,
Words that would make me all bright like a spring day.
I lay awake nights
Thinkin’ o’ hearin’ things,
An’ seein’ things.
I’m awful tired o’ these hills,
They crowd in so.
Seems sometimes ef I could see the ocean,
Or a real big city,
’Twould help.
Kind o’ lay my eyes out straight for a while,
Everythin’s so short here
My eyes feels crinkled.
I love laylocks,
But I git so tired o’ watchin’
The leaves come and the flowers
Every year the same,
I’d like to root ’em up.
I’ve set an’ set in the kitchen evenin’s awful late,
Fer not bein’ able to git up and light the lamp
To go ter bed.
I’m all lead somehow.
I guess ef anybody did say anythin’
I’d be deaf
Jest with listenin’ so long.
I’m plumb tired out.”

“Look-a-here, Minnie, Why don’t you go away Fer a spell?”

“Me go away!
Oh, no, I couldn’t never do that.
I couldn’t go no place.
I can’t hardly git over to Dicksville
Fer my week with Aunt Abby now.
I’m all wrong away from home.
I can’t do nothin’!
Nothin’ at all.
I’m so awful tired.”

“Minnie, did you ever love anybody? Any man, I mean?”

“No, Rachel, I never did.
I know that sounds queer, but it’s a fact.
I’ve tried to think I did,
But ’twarn’t true.
I hadn’t hardly no time for men-folks,
Mother was sick so long,
And then there was Father.
I never was much account with ’em anyway,
But I suppose I might ha’ had one
Ef I’d fixed my mind so.
But I al’ays waited.
An’ now I’m through waitin’,
I’m through waitin’ fer anythin’, Rachel.
It’s jest go, go, go,
With never no end,
And nothin’ done that ain’t to do over agin.
There now it’s six o’clock,
And I must be gittin’ supper.

You needn’t move that cup, Rachel.
I ain’t a-goin’ to touch it.
I’ll jest keep on now till the Lord takes me
An’ I only hope he’ll do it soon.”

The robin flew down from the spice-bush
And pecked about for worms.
The clouds were brazen trumpets
Tumbled along the edge of an apple-colored sky.
The shadow of the house
Fell across the path to the barn
Confusing it with the grass and the daisies.

A wind rose, and a wind fell, And the day that was that day Vanished in the darkness.
```

---

## IC-1780: Dear Girl

- Title: Dear Girl
- Author (byline): Aija Mayrock
- Work: Not specified
- Publisher: Andrews McMeel Publishing
- Publication date as stated: Aug 2020
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1008
- Already set (do not supply): none

### Source block (context only)

```text
Author: Aija Mayrock
ISBN: 978-1524856175
Publisher: Andrews McMeel Publishing
Date (Month/Year): Aug 2020
```

### Introduction (context only: never use it for content warnings)

```text
Against all evidence, American men have come to believe that the world --economically, socially, politically—is tilted against them. Sure, 88% of Fortune 500 CEOs are men*, and so are 72% of Congressmen**. Men still earn significantly more money than women for the same work, and men have an unbeaten 45 and 0 record of winning the American Presidency. Even so, findings from the August 2022 American Perspective Survey show that nearly 45% of men ages 18-29 believe they are facing gender-based discrimination.***

When you’ve been on top for a few thousand years, even small moves toward diversity, equality and inclusion can feel like discrimination.

So today, I speak to women – women who have persevered even after Roe v Wade was overturned by a Supreme Court that was 66% male. In the words of the great Ruth Bader Ginsburg: It’s a woman’s right to control her own destiny. To be able to make choices without the big brother state felling her what she can and cannot do.”

Dear Girl by Aija Mayrock
```

### Performance text (classify this)

```text
Dear Girl,
open your eyes.
We have come so far it's easy to resign.
We've got "equality"
but public policy shows the contrary, honestly.
One in six women could be raped in their lives
and it's mostly seen as a victimless crime.
What should every girl know?
You are not some puppet in a puppet show.
Expose the double standards,
the hypocrisy, the hate.
It is never too late.
This is the moment of girls taking the reins.
It is Time's Up.
It is Me Too.
It is everyone from me
to you
who has spoken
or stayed silent
but strong.
And for every survivor who speaks
only to be met
with intimidation, investigation, and disbelief:

Dear Girl,
you will be believed.
If not by Senate floors and investigators,
we will hear you, Dear Girl,
we will see you, Dear Girl,
we will stand by you.
For the survivor three thousand miles away or the one next

door,
you are heard.
Justice will not always prevail
but we will continue to fight
tooth and nail.
You are heard.
So that our sisters and daughters will never be asked,
rather
harassed,
whether they wanted it,
regretted it,
or just forgot.
Believe me,
no one forgot.

Dear Everyone,
grab ahold of your voice.
It is time to make a choice
to believe survivors
to pay us all the same
to give women of color equal access and opportunity
to protect the safety of trans girls every day.
Make the choice to change the climate,
make the choice not to stay silent.
This is not the era of girls,
this is the future of girls.

Dear Mother,
I see your fears baked into how you raised me.
I see them tremble from your lips as you warn me.
I know you are terrified of the world that could swallow

me whole.
But Mother, you need not fear,
because even if I am swallowed up,
I will kick until I am spit back out.
I will fight with the fists you gave me.
I will shout from the gut you built for me.

Dear Mother,
you need not worry.
For I am the warrior you always dreamed you'd have.
I will not go down fighting
because I will not go down at all.
When a girl is born into a world
where she has no control over her body,
she learns to live in a body that is not hers, but owned

by the state.
She grows up to believe that obedience is her middle name.
When a girl is born into a world
that does not value her body,
she learns to exist on the periphery of society
as if growing into her spine is too much to ask for.
Your cruelty is no match for my spirit.
Try to break me
and you will see
love that pours like blood from my wounds.
To break me, you would have to make me hate,
and like I said,
your cruelty is no match for my spirit.
You tell your daughter that she is being emotional,

irrational,
yet you tell your son that he is being strong, smart;
you are teaching your daughter to doubt her feelings,
to question her beliefs.
And so when she is mistreated,
she will think back to what was said
under your roof
and believe those gut feelings we speak of
are merely irrational thoughts,
while your son believes every thought he has is fair and

right.
Be careful how you raise your daughters.
Be careful how you raise your sons.
When you teach your daughter
that her body is only pure untouched,
you are teaching her
that she can be ruined at the hand of man.
Raise your daughters like you raise your sons;
the inequality did not begin with her birth,
the inequality begins when you choose to raise your

daughter in a box labeled "ladylike" and your son, in no box, with no label.

She has a fire that you can see when you look into her eyes, flames swallow up her self-doubt. She always runs toward the storm; nothing scares her more than turning down a challenge, nothing scares her more than taping down her wicked

tongue.
I am the woman I am today
because my father never clipped my wings,
even in disagreement.
I hear his voice,
all pride and no shame, say --
"And, yes, that is my daughter."
And so I soar.
I soar.
I soar.

Dear Girl,
I wish I could hold you and say
the world will protect you.
But I know it will not,
and in some way,
you, too, know it will not.

Maybe that's why when people tell you, "You're too young to understand," you smirk with that twinkle in your eye.

White women, show up for your sisters of color.

Straight women, show up for your lgbtq+ sisters.

Women,
show up,
have the guts
to overlook differences,
because really
the difference is
as drastic as
progress
or
no progress.
We can't afford to divide each other.
Since early days
we are taught
to compare and compete
with one another.
You are not devalued
even if
the woman next to you
appears to be perfect.
You are not devalued
if your sisters
are achieving
greatness.
You are always of value
if you
value
you.

Dear Sisters,
Show up for those
you might not know
or understand.
Show up for those
you might not
like at all.
Show up for all of us.

Dear Girl,
You were not born to please,
you were brought here to
disrupt, awaken, and speak truth,
to ease the pain scattered around
and so when you are told to quiet down,
I hope you grow louder.
You might believe the words you speak are weak,
but the echoes of words
can start revolutions.
No good revolution came from
safety and security;
revolution begins when you leap into the unknown
and shout from the rooftops:
I am here. Alone or surrounded by thousands. I am here.

And I am not going anywhere.
```

---

## IC-1781: The Death of Innocence

- Title: The Death of Innocence
- Author (byline): Nikki Giovanni
- Work: Acolytes: Poems, Pgs 13-16
- Publisher: William Morrow
- Publication date as stated: Jan 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: MAMIE TILL-MOBLEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1758
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nikki Giovanni
Book: Acolytes: Poems, Pgs 13-16
ISBN: 978-0061231315
Publisher: William Morrow
Date (Month/Year): Jan 2007
```

### Introduction (context only: never use it for content warnings)

```text
In 1955, when 14-year-old Emmett Till traveled from his home in Chicago to stay with a great-uncle in Tallahatchie County, Mississippi., his mother was nervous. Though the
```

### Performance text (classify this)

```text
This selection is listed as a Prose Poem and contained in Giovanni’s book of poetry. Check with your tournament for to determine in which category to enter this selection: PROSE or POETRY MAMIE TILL-MOBLEY: (Pg 16) I wanted the world to see what they did to my boy. I wanted Emmett's death to be the last death. I wanted Emmett's death to kill American innocence. I wanted Emmett's death to be not only the death of my boy but the death of innocence. I wanted Mississippi, I wanted America, to give us justice. And I prayed that I would live long enough to see it.

world was changing — the Brown v. Board of Education decision had come the year before — the Deep South was still a dangerous place to be black. The murder of Emmett Till was evidence of the decades-old codes of violence exacted upon Black men and women for breaking the rules of white supremacy. But rather than bending to the intimidation and psychic horror caused by the savage murder, Till’s family, along with national newspapers and civil rights organizations – including the NAACP used his death to strike a blow against racial injustice and terrorism.

Death of Innocence by Nikki Giovanni

MAMIE TILL-MOBLEY: (Pg 13-16) It must have been the waiting. The waiting had to be the worst of it. The only possible, the only possible, the very only possible thing worse than the waiting might be couldn't be would be the waiting being over. The knowing. The knowing they had killed your boy. Not killed. Killed could be an automobile accident. He could be walking down the road with that sort of doo-wop walk he developed as a result of being a breech birth with a knee caught against his chest almost choking him to death before he had a chance to live or that limp could be a result of polio. You had to be grateful that the only scar left was that limp and, of course, that stutter. That stutter that was so frustrating to him because he didn't want to stutter, the other kids would tease him; he wanted to talk strong and manly like he imagined his Daddy did. He wanted to be strong and take care of his mother. And be wonderful and great and show the world how wonderful he was. Yes. Maybe he was walking down the road on the way back to Uncle Mose's house. Dreaming as he was prone to do. Not just daydreaming like some children sitting in a window on a rainy day wanting to go out but dreamy like he had plans like he was talking to someone from somewhere else. Just not paying attention. How many times had you tried to teach him: Pay attention, Bo. And he smiled that baby-ish smile, that sweet smile, that I'm a good boy Mama smile and said "okay" and went right on not paying attention. Not killed. This was, after all, Mississippi. Killed could be, most likely was, probably was two or three or four mean white boys riding around in a pickup truck. Emmett was on the road alone maybe going to Bryant's to get some bubble gum or some nickel candy maybe some of those windmill cookies 2 for 5 cents and those poor Mississippi crackers were jealous of his shoes and his pants and his white shirt that he wore like he saw a picture of his Daddy wearing a white shirt with the sleeves rolled up. He had the ring on LT May 25, 1943. His Daddy's ring. He was almost big enough to wear it on his ring finger. It was just a little too big so he had wrapped it. Those jealous Mississippi crackers, four or five, maybe six boys riding around in a pickup truck looking for something to do to any girl they could find alone or somebody Black too small to defend himself. Maybe those jealous crazy Mississippi boys grabbed him and wrestled him down. Maybe they hit him and kicked him and threw him in the river. They didn't know they didn't care that he couldn't swim and maybe they watched him flailing and they laughed and drove off and my baby tried and tried but the water pulled him down and he had to give up his spirit. Maybe that's what they mean when they say killed. Emmett was missing. That's what the phone call in the middle of the night said. That he was missing. Mose put his wife on the Chicago train then went calling on everyone who might could help. They didn't want to call me or Mama too early maybe it could get solved without having to make that call. But they had to call. Emmett is missing. Mr. Bryant and Mr. Milam came to get him in the middle of the night. It was 2:00 A.M. and that's not an hour people come to get you when they only intend to teach you a lesson; that's the hour they come when they intend to murder you. There was someone else in the truck. A woman. There was a Black man in the truck bed. "It's Mr. Bryant, Uncle Mose. Open the door." No shame. No sense that there was anything to hide. "I want the boy from Chicago. The one who did all that talking." They offered to pay. They offered to whip him good. They said he was simple-minded and didn't know what he was saying. They said please. But they took my boy. "You don't need no socks, boy. Get on out here." "I never put on shoes without socks," he said. Never understanding the danger. Just a fourteen-year-old boy trying to impress his Mississippi cousins. They would laugh at his stutter; they would ape his doo-wop walk. He wanted to show them he wasn't afraid. Talk to that woman in the store, if you're so tough. She's a white woman. If you so tough in Chicago. talk to that woman. They knew. They knew the danger. They knew he would probably take a good whipping from somebody: Mr. Bryant, Uncle Mose. Somebody would show him that just because he was from Chicago his Mama was from Webb and they were from Money, and this is Mississippi and the cousins knew how this system worked not the cripple stuttering boy from Chicago. With his ring and his pants and his soft shoes and his white shirt. And that hat on the side of his head. They would show him. Never thinking three days later there would be a knock at the door. At first nobody knew. Whatever was said was said. The Black community held its breath, but Bryant was away taking fish or crabs or something with his half-brother J. W. Milam. Milam was a mean cracker. Bragged he knew how to take care of niggers. Didn't hesitate to show anyone. Three days passed and nothing was said. But Bryant came home. Tired. Unhappy. With not much more money than he left with. Working too hard for a good-looking white man and not making much money. Some little Black Judas whispered: What you going to do about that boy from Chicago who did all that talking to your wife? Carolyn Bryant hadn't said a word about it. She knew what would happen. She didn't have to be a nice person, a concerned person, a person with a conscience. She just knew what would happen and she didn't want it on her plate. Milam's wife who stayed with Carolyn while the men were away trying to make a little extra money knew what would happen. She knew what her husband would do. She knew what he did to her; she knew what he did to the children. She didn't want it on her plate. But some little Black Judas without even the thirty pieces without even a piece of candy or a cookie. Some little jealous Black Judas whispered to Bryant: What you going to do? Did he think there would be a show? That Bryant would take Emmett to the front of the store. strip his shirt off and give him five or ten lashes? Did he think it would be fun to see my boy, a fourteen-year-old. a barely fourteen-year-old cry for mercy? Did he think that would make his life in Mississippi any better? What could he have been thinking? But whatever he was thinking, it couldn't have been that Bryant and Milam would take Emmett out at 2:00 A.M. throw him in the back of the pickup and take him to Milam's barn. No one would think they would strip his clothes off of him to make fun of his penis. No one would think they would handle him like they did. That they would beat him and beat him and then the cutting started. Then they beat him, and Emmett's eye popped out. There was blood, Emmett's blood all over that barn. The Black man beat him, too. Just so the white men could think he would not testify against them. Finally, mercifully, they put a bullet in his head. But I know my baby was gone way before that. I know Jesus reached into that barn and took Emmett away. I know they sat on a cloud and watched the horror but Emmett was not in that barn when they started putting things in every orifice that they could. Emmett was not in that barn when they started the cutting. No. Emmett was not in that barn. They wrapped the barbed wire around what was left of his neck and told that Negro to attach it to the cotton-gin fan. They hauled his body to the Tallahatchie River. Even they must have known what a horrible thing they had done. Even they must have been ashamed. But, no, killed did not describe what they did to my boy. Three days later when his body was found they wanted to bury him in Mississippi. I wanted him home in Chicago. I wanted the world to see what they did to my boy. I wanted Emmett's death to be the last death. I wanted Emmett's death to kill American innocence. I wanted Emmett's death to be not only the death of my boy but the death of innocence. I wanted Mississippi, I wanted America, to give us justice. And I prayed that I would live long enough to see it.
```

---

## IC-1782: Defining Your Worth – A Collection

- Title: Defining Your Worth – A Collection
- Author (byline): Savannah Brown, Dustin Lang and Shasparay Lighteard
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1155
- Already set (do not supply): none

### Source block (context only)

```text
Author: Savannah Brown
ISBN: On-Line Transcript
Publisher: NSDA 2014 Light the Stage Spoken-Word
Poetry Showcase (2014 NSDA Tournament)
Date (Month/Year): Jan 27, 2015
https://www.youtube.com/watch?v=N-ezbk0AOCI
Author: Dustin Lang
ISBN: On Line Transcript
Publisher: You Tube.com
Date (Month/Year): Feb 16, 2014
https://www.youtube.com/watch?v=NNf9RS0UJxc
Author: Shasparay Lighteard
ISBN: On Line Transcript
Publisher: TedxYouth@Austin
Date (Month/Year): May 13, 2016
https://www.youtube.com/watch?v=Q9VxIaF0TUM
```

### Introduction (context only: never use it for content warnings)

```text
Author Stephen Chbosky, in his novel The Perks of Being a Wallflower, wrote: “We accept the love we think we deserve.”

But let’s face it: Cynicism and pessimism are becoming a staple of our society. Blame social media, blame politics, blame the pandemic. The fact is, it has become harder and harder to believe that we are worthy, that we deserve love and we are not, should not and cannot be defined by the world around us.

Defining Your Worth – A Collection including What Guys Look for in Girls by Savannah Broan, I Have Worth by Dustin Lang and Love Yourself by Shasparay Lighteard.
```

### Performance text (classify this)

```text
What Guys Look for in Girls by Savannah Brown

When I first learned that no one could ever love me more

than me a world of happiness previously unseen was discovered because somewhere along the line of aging and scrutiny

and time
I was taught to despise myself
but i made sure I kept myself beautiful so someone would
love me someday
so i could belong to someone someday
because that's the most important thing a little girl could

ever want . . . right?

What Guys Look for in Girls by Savannah Brown
(Cont’d)
I was 13 the first time i was embarrassed about my body
of course it would not be the last
I remember stuffing my bra in the morning
tears stinging my eyes
hoping, praying to something that I could look beautiful
enough today braces and all
for the ruthless boys who mercilessly told me I was

worthless because my boobs weren’t big enough and i would go home and put on a sweatshirt with my eyes

closed
denying myself the right to be shown myself
because I didn't dare want to insinuate beauty in regards to
something so insulting as my body.

But, I mean, we all end up with our heads between our

knees because the only place we’ll ever really feel safe is inside

skin we've been taught to hate by a society that shuns our awful confidence and feeds us

our own flaws and sometimes when i need to meet the me that loves me.

I can't find her
a reminder that the mirror is meant to be a curse
so I confine her in my mind
but when he or she shouts, “Let me out!”
we are allowed to listen.

But it’s met by a chorus of conceited, egotistical narcissists But since when was self-solicitude a sin? Since when was loving who we are made an offense by

morons who do not matter?

change this physicality and that one don't you dare shatter the notion that you could ever be anything beyond paper fine flesh and flashy teeth and

fingernails
echoic accusations of Not good enough
Never good enough
Have you ever felt so numb that it hurts?
Entertain me . . . or . . .

You can't surrender to them you gotta remember you're the only thing you'll ever truly

have
and no i don't mean your body
because someday that will go bad no matter what you do
I mean you.

I mean the way your bright eyes go wild when you smile and your laughter's so melodic it’s a song I mean the way your creativity’s compass that leads you to

what you love and you don't need any miracle cream to keep your

passions smooth hair free and you don't need any diet pills to slim down your

kindness and when you start to drown in these petty expectations you better reexamine the miracle of your existence; because you are worth so much more than your waistline. You’re worth the beautiful thoughts you think and the daring dreams you dream, but sometimes we forget that

because we live in a world where the media
pulls us from the womb, nurses us and
teaches us our first words
Girls: soft, quiet. pretty
Boys: manly, muscles, pretty
But i don't care whether it's your gender, your looks, your
weight, your skin or where your love lies
none of that matters
because standards don't define you.

You don't live to meet the credentials established by a

madman.

You're a treasure whether you want to believe it or no.t And maybe that's what everyone should start looking for

I Have Worth by Dustin Lang (Excerpts)

From the day I was born I had one question that plagued

my mind And it wouldn't leave me so in my late night hours I would try to find a kind of answer that would satisfy this

uncertainty of mine Do I have worth?

So I did all I could to prove that I did
I practiced, I prepared, and I performed
Sometimes I performed well and my worth appreciated
And I knew it because others would tell me
They told me that I mattered
They told me that I was valued
They told me that I was seen

But there was a dark side to these reactions . . .
Sometimes I failed
Sometimes I performed poorly and my worth depreciated
And I knew it because others would tell me
They told me that I messed up
They told me that I had no value
They told me that I was clearly seen or rather that my

mistakes were

So the thought that plagued my mind It never declined it only increased like a plus sign Do I have worth?

I may fail 100 times, I may fail 1000 times, I may fail 10,000

times But nothing will change the truth that has liberated this

heart of mine I have worth And today I boldly proclaim the conclusion to the question

that crushed me like cancer
Then freed me when I found the answer
That I have worth
And so do you

Love Yourself by Shasparay Lighteard (Excerpts from her TedxTalk)

I'm the girl they told to be a little quieter in the choir I'm the girl that never quite learned how to whisper I'm the girl that usually takes a step back from the mic

You wouldn't believe it,
but when I was younger I was a quiet thing
I knew how to make a meal out of silence
but I've grown to refuse to swallow
Now I have dangerous lips and a pretty smile
that conceals my sharp tongue
I'm often told I have a big mouth
I talk too much
I'm loquacious
Don't know how to shut my trap
I'm too loud . . . Too much

They say, “Girl, you got too much bark.
We put dogs to sleep for not knowing how to hush.
We make examples of those who refused
to be broken.”

We learn early that being loud is a bad thing We used our whisper voices and played the silent game ‘Cause Chatty Cathy is never welcome at the table Women learn how to be digestible How to sit . . . smile . . . be taken and be grateful

Silence can be painful
I've refused to quell myself for anyone else
Someone once told me I would never be married
if I did not learn my place
To her I say: My megaphone
of a throat has too much girth for a leash
Do not expect soft when there is only growl and grit
Ain't no lullabies left in my throat.
When I sing, best believe it is my soul crawling from the

light

(Singing) Do you know why the caged bird sings? Do you know why the caged bird sings?

I speak because I have to
I speak for the many who don't
who continue to be silenced
who are constantly shushed
I speak for them because I know how it feels
```

---

## IC-1783: Domination of Black and Cobra Lilies in the Supermarket

- Title: Domination of Black and Cobra Lilies in the Supermarket
- Author (byline): Wallace Stevens and Diane Wakoski
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 671
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wallace Stevens
Book: The Emperor of Ice-Cream and Other Poems
ISBN: 978-0385004633
Publisher: Doubleday
Date (Month/Year): March 2005
Author: Diane Wakoski
Book: Virtuoso Literature for Two & Four Hands
ISBN: 978-0385004633
Publisher: Doubleday
Date (Month/Year): March 1975
```

### Introduction (context only: never use it for content warnings)

```text
The distinctive eye-like pattern of the peacocks regal tail feathers symbolizes the all-seeing power of God to many Christians. The peacock also represents immortality and resurrection, for it was believed that the flesh of the peacock never spoiled. When peacocks cry, then, the logical question is against what are they protesting? Wallace Stevens paints a wonderfully symbolic image of peacocks crying in response to the inevitable coming of night – Or on a deeper level: God crying out against the universal symbol of evil and death . . . . . . Domination of Black.by Wallace Stevens
```

### Performance text (classify this)

```text
Domination of Black

At night, by the fire,
The colors of the bushes
And of the fallen leaves,
Repeating themselves,
Turned in the room,
Like the leaves themselves
Turning in the wind.
Yes: but the color of the heavy hemlocks
Came striding.
And I remembered the cry of the peacocks.

The colors of their tails
Were like the leaves themselves
Turning in the wind,
In the twilight wind.
They swept over the room,
Just as they flew from the boughs of the hemlocks
Down to the ground.
I heard them cry -- the peacocks.
Was it a cry against the twilight
Or against the leaves themselves
Turning in the wind,
Turning as the flames
Turned in the fire,
Turning as the tails of the peacocks
Turned in the loud fire,
Loud as the hemlocks
Full of the cry of the peacocks?
Or was it a cry against the hemlocks?

Out of the window,
I saw how the planets gathered
Like the leaves themselves
Turning in the wind.
I saw how the night came,
Came striding like the color of the heavy hemlocks
I felt afraid.
And I remembered the cry of the peacocks.

TRANSITION Diane Wakoski uses the cries of Stevens’s peacocks to derive some insight into her own tendency toward tears. Society often views crying as a sign of weakness, rather than a protest of injustice. However, in spite of mixed feelings about tears, poets and novelists have known intuitively that crying is somehow good for us. For example, Shakespeare wrote: "To weep is to make less the depth of grief." And Tennyson once wrote about a woman who learned her military husband was killed: "She must weep or she will die." But, perhaps the best advice about tears comes from Charles Dickens, who has Mr. Bumble, in Oliver Twist, declare that crying "opens the lungs, washes the countenance, exercises the eyes, and softens down the temper. So cry away." Even if it’s over something as insignificant as Cobra Lilies in the Supermarket by Diane Wakoski.

Cobra Lilies In The Supermarket for Wallace Stevens

I wonder
as I am driving to the Market Basket why I have lived
my life
as I have.

The mother of my third husband -a blond blue-eyed singer, she was

told me
I was a crybaby
because,
at the time,
I was crying.
She said
you should fix up your life and then not cry
about it.

My own mother said, referring to my fourth husband who left me

"What are you crying for?
Buy your own house so that the next one who leaves you
won't be able to take your home away."
And she too said,
"You always were
a crybaby."

When I cry now
it is usually in anger. But
sometimes
I still cry in pain. Then I hide myself in rooms where no
one can see me.
I bought a house
but cannot live in it.
My fifth husband says he would leave me
before living there,
and since he is a nice man
( or perhaps it is just thatI am older)
I didn't cry,
nor have I recently been called
a crybaby.

I stilI live in other people's houses, listen to their music, live out of suitcases.

Driving to the supermarket in the rain today, shopping
for someone else's dinner,
I wondered if anyone ever felt
he had a home
other than in his head.

I was tantalized with the cobra lily sitting next to the
oranges & avocados like a purple clenched fist
unrolling its tongue
but unwilling to speak to me, I thought.

When I studied the piano
I always cried at my music lessons. My teacher stopped
criticizing me. I heard that secretly she called me a
crybaby.
I gave up piano
Took up voice instead.
Now,
my lessons are concerts
where crying is considered an art.
I shout,
I speak,
I whisper,
and at last again
I can cry.
This time
no one taunts me
but other crybabies;
and when I am alone
I defend myself with poetry:
"I remember the cry of the peacocks."
```

---

## IC-1784: Eva Braun: Tea for Two and Two For Tea

- Title: Eva Braun: Tea for Two and Two For Tea
- Author (byline): W.D. Snodgrass
- Work: Not For Specialists
- Publisher: BOA Editions
- Publication date as stated: 2006
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 726
- Already set (do not supply): none

### Source block (context only)

```text
Author: W.D. Snodgrass
Book: Not For Specialists
ISBN: 978-1929918775
Publisher: BOA Editions
Date(Month/Year): 2006
```

### Introduction (context only: never use it for content warnings)

```text
Hitler’s mistress, Eva Braun, received no public recognition and often felt badly neglected. Her small revenges included singing American songs, her favorite being “Tea for Two.” Having to chosen to die with Hitler in his safety bunker in April of 1945 as the American Troops advanced across Europe, she appeared quite serene during the last days. This poem explores the possible thoughts of Eva Braun as she prepares for her death. Eva Braun: Tea for Two and Two for Tea by W.D. Snodgrass.
```

### Performance text (classify this)

```text
Lines in italics should be sung to the tune Two for Tea: See the following link to hear the song: http://www.youtube.com/watch?v=y0zc7x434Aw

Tea for two And two for tea

I ought to feel ashamed Feeling such joy. Behaving like a spoiled child!

So fulfilled. This is a very serious matter.
All of them have come here to die. And they grieve.
I have come here to die. If this is dying,
Why else did I ever live?

Me for you

And you for me

We ought to never flaunt our good luck
In the face of anyone less fortunate --
These live fools mourning already
For their own deaths: these dead fools
Who believe they can go on living . . .

And you for me Alone.

Who out of all of them, officers, ministers,
These liars that despise me, these empty
Women that envy me -- so they hate me –
Who else of them dares to disobey Him
As I dared? I have defied Him to His face
And He has honored me.

We will raise

A family

They sneer at me – at my worrying about
Frau Goebbels’ children, that I make fairytales
For them, that we play at war. Is our war
More lost if I console these poor trapped rabbits?
These children He would not give me . . .

A boy for you A girl for me

They sneer that I should bring
Fine furniture down this dank hole. Speer
Built this bed for me. Where I have slept
Beside our Chief. Who else should have it?
My furs, my best dress to my little sister --
They would sneer even at this; yet
What else can I give her?

Can’t you see

How happy we would be?

Or to the baby
She will bear Fegelein? Lechering dolt!
Well, I have given her her wedding
As if it was my own. And she will have
My diamonds, my watch. The little things you
Count on, things that see you through your
Missing life, the life that stood you up.

Nobody near us To see us or hear us

I have it all. They are all gone, the others -- The Valkyrie; and the old rich bitch Bechstein; Geli above all. No, the screaming mobs above all. They are all gone now. He has left them all. No one but me and the love-struck secretaries -- Traudl, Daran – who gave up years ago.

No friends or relations

On weekend vacations.

That I, I above all, am chosen – even I Must find that strange. I who was always Disobedient, rebellious – smoked in the dining car, Wore rouge when he said we mustn’t. When he ordered that poor Chancellor Schuschnigg Was to starve, I sent in food.

We won’t have it know, dear, That we own a telephone, dear.

I who joined the Party, I who took Him
For my lover just to spite my old stiff father –
Den Alten Fritz! – and those stupid nuns.
I ran my teachers crazy, and my mother – I
Held out even when she stuck my head in water.
He shall have none but me.

Day will break

And you will wake

We cannot make it through another month; We follow the battles now on a subway map.

Even if the Russians pulled back --
His hand trembles, the whole left side
Staggers. His marvelous eyes are failing.
We go out to the sunlight less each day. We live
Like flies sucked up in a sweeper bag.

And start to bake A sugar cake

He forbade me to leave Berchtesgaden,
Forbade me to come here. I tricked
My keepers, stole my own car, my driver Jung.
He tried to scold me; He was too
Proud of me. Today He ordered me to leave,
To go back to the mountain. I refused.
I have refused to save my own life and He,
In public, He kissed me on the mouth.

For me to take

For all the boys to see.

Once more I have won, won out over Him
Who spoke one word and whole populations vanished.
Until today, in public, we were good friends.
He is mine. No doubt
I did only what He wanted; no doubt
I should resent that. In the face
Of such fulfillment? In the face
Of so much joy?

Picture you

Upon my knee;

Tea for two

And two for tea . . . .
```

---

## IC-1785: Fat Shaming: The Other Side

- Title: Fat Shaming: The Other Side
- Author (byline): Kathy Appelt, Georgia Me, Rachel
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1505
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kathi Appelt
Book: Poems from Homeroom
ISBN: 978-0805075960
Publisher: Owlet Paperbacks
Date (Month/Year): Sept 2010
Author: Georgia Me
Book: Russell Simmons Def Poetry Jam on Broadway
ISBN: 978-0743476225
Publisher: Simon and Schuster
Date (Month/Year): 2005
Author: Rachel Wiley
Book: Fat Girl Finishing School
ISBN: 978-0989009225
Publisher: Timber Mouse
Date (Month/Year): Oct 2014
Author: Melissa May
Book: SparkleFat
ISBN: 978-0692225417
Publisher: Words Dance Publishing
Date (Month/Year): May 2014
```

### Introduction (context only: never use it for content warnings)

```text
All people are created equal—that is, unless they’re fat. Although overweight and obesity affect two-thirds of Americans, overweight people are presumed lazy, undisciplined, dishonest and unintelligent. In fact, 61% of our population see no harm in making negative remarks about a person’s weight. But now, overweight people are speaking out against fat shaming. This compilation is called Fat Shaming: The Other Side and features poems by Kathy Appelt, Georgia Me, Rachel Wiley and Melissa May.
```

### Performance text (classify this)

```text
Wiley and Melissa May

The Fat Girl by Kathy Appelt

She’s already reached into her backpack four times in fifteen minutes.

Four times, silently
at her metal desk against the wall,
she’s slipped her hand
into the bright blue canvas pouch.

No one sees her, hears her
open the cellophane bags of
Twinkies, M&M’s, Chee-tos
her true companions.

Ever since they forgot her real name somewhere around the fifth grade she’s certain she’s become invisible.

Without her real name
to identify her, then
who’s to say she took
the missing peanuts
and crème-filled Oreos?

She thinks someday she’ll shed this skin she wears in layers and float away

down a river

on a cloud but right now it’s all she can do to stay away from that backpack.

Right now she’s trying hard
to find her real name
sew it on her left pocket
in threads above her heart
so no one will forget again.

INTRODUCTION Our society views thinness as a symbol of hard work, self-discipline and willpower—values we have come to revere above all else. So people who are overweight are simply lacking in self-discipline, right? Did you know that two in five women say they would trade three to five years of their lives to achieve their ideal weight? But the reality is that many causes of obesity are beyond the individual’s control.

-- genetics, economic status, upbringing and the way parents talk to their children about weight all have a bearing on obesity.

Full Figure Potential: A Fat Girls Blues by Georgia Me

Out of money looking for a snack
Then I see little Debbie’s face on a pack
Smiling, enticing me, inviting me to have a taste
With haste I race to the destruction of my waist
As the sugar sets in so does the disgust I feel
Wishing I had the power of will
Or hoping someone would kill this gluttonous monster

which rules my eyes Which is bigger than my stomach so we fill my belly with

pies And cakes, by-products, additives and other shit It’s hard for me to quit, sweets are a quick hit My diet includes fried everything, all kinds of pork People asking if I’ve been visited by the stork See it’s looked at as a sin to be fat without children or a

medical condition So it leaves a girl fishing, for an excuse to stop the

abuse I endure every day in every way through ridicule and

personal shame Unwanted attention and fame from the group of young

men who holler “Big Drawers” As I pass by I start to cry, the wind dries my eye But nothing can heal this scar left on my esteem Praying this order is a dream or better yet a nightmare For it’s too hard to bare this constant scar as my

reality A complete disregard for humanity Not seen as human, more like insane or having no self

control
She can’t even pass up a jelly roll
Not seen as beautiful, look at the folds and gut the
cellulite thighs and out of shape butt
Not seen as strong “She can’t go long, she’ll be down

before the end of the song”
My personal demons are hard by themselves
Comparisons to pigs, elephants and whales
You might look at me and see lazy and weak
Giving no second thought, that before you an angel may

speak You can't see the beauty besides the pretty face You don't see the warmth of my heart which provides a

safe place
Or a home where not only love roams
For myself and others which light has not been shown
See I realized, I'm more than a body, I have a spirit and

a mind Which through divine knowledge told me it's about time

for me to love who I am
And decline those devils who try to steal my joy
I'm conquering my foes like Helen of Troy
And with the same spirit I make the world hear this
Love who you are be the best that you can be
Your spirit will soar and the whole world will see
Your strength, your beauty and your heart
The ignorance of others won’t pierce like a dart
Let those who worship aesthetics live a pathetic life
No substance, no feelings, self-inflicted strife
If they can't see the beauty of my soul
I know I'm beautiful in the eyes God beholds
See, I know at times I may get knocked down or even,

doubt my ability But I’ll look in the mirror and say I’m wonderful with

humility Now we’re supposed to respect everyone with different

choices, beliefs and hues But who gives a damn about a fat girl’s blues?

INTRODUCTION Obesity is the last frontier in tolerable prejudices, even against children. Discrimination based on age, race, religion, sexual preference and gender identity is illegal. However, it is not illegal to discriminate against people based on their weight. We do it every day.

Do you really think that the overweight person you see at the grocery store, at the mall or the restaurant WANTS to be that size? Do you really believe they haven’t tried every diet on the market, considered surgery or even suicide to stop being the size they are? We are so quick to fat shame . . . Leaving those people who struggle praying for something different.

Pre-Flight Prayer of a Fat Girl by Rachel Wiley

Pray, let us be thankful for the well trained smile of the

flight attendant it may be the only one pointed at us on this day Let us not be embarrassed to request the seat belt

extender
but rather rejoice in its being.
Let us pray for a seat that sits not on an aisle
but a window so we may cling to the plane wall
in attempt to make ourselves small
enough
Let us also move our bodies as little as possible enduring
cramp and ache alike
so as not to be a burden unto our seatmate.
And blessed be that seatmate who does neither sigh nor

scorn when our hip sneaks over the line of the armrest Yay, let us never book with SouthWest for they will send us into exile for not being fruitful and purchasing 2 seats to contain our bounty when only 1 can be afforded. Pray, let us ignore the glances when the pilot announces the craft is overweight and must sit flightless while luggage is rearranged for

balance. Lo, Let us not look to the magazine models tucked into the seat backs like hymnals as anything holy Pray, let us remember we are beautiful in our bounty Pray most of all that we forgive ourselves And smooth the creases of apology we have folded our delicate bodies into on this day Come home and stretch out across our beds like the unpacking of a suitcase full of all the best

souvenirs.
Our bones are racks of the kitschiest key chains.
Our bellies, magnificent snow globes.
Look and rejoice at everything we managed to get home

safe.

INTRODUCTION So . . . If people are so bothered by the stigma of being obese, why don’t they just lose weight? As anyone with a history of dieting knows, it’s extremely difficult to lose weight and even more difficult to keep it off. Sure, blaming the victim frees everyone else of responsibility. But my dream is that one day the great divide between the beautiful and the ugly will cease to be and people will be judged not for the size of their skin, but by the content of their character.

Fat Girl by Melissa May

So the poet tells me, all cloaked in beautiful words and
authentic Albanian eyebrows
that she make clothes for bodies,
not bodies for clothes
My body sits folded in a wicker chair like
two pallets of rising dough.
I pray she can’t see my navel tremble.

I tell her, I have been the fat girl in over a dozen schools.

I sit all token-like in their hall of fame, except --
they don’t give awards to punch lines
So I repeat the code of conduct like a mantra, even
years
after the cap and gown have yellowed in the Oklahoma
Sun.
Do not like boys.
Do not go for seconds.
Do not draw attention.

See I know what a body feels like when it changes from
vessel
to funeral shrouds,
To sarcophagus.
I have been buried alive for so long,
I’ve forgotten what the sun
tastes like.

But they’re allowed to hate me.
Even now, strangers on the street
Are allowed their sharp-tongue judgment, their sound
effects.

Being this big is fuel for the last appropriate hate crime. It is stand-up acceptable in its pretty designer suit— Size medium, pressed in brand new shoes.

It’s my fault.
I will never curve like a comma around the bodies
of people I am not allowed to love,
I’m supposed to settle for anyone who
can stomach my punctuation.
```

---

## IC-1786: Fat Skinny Joke

- Title: Fat Skinny Joke
- Author (byline): Rachel Wiley and Blythe Baird
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1052
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rachel Wiley
Book: Nothing is Okay
ISBN: 978-1943735303
Publisher: Button Poetry
Date (Month/Year): March 2018
Author: Blythe Baird
Book: If my Body Could Speak
ISBN: 978-1943735471
Publisher: Button Poetry
Date (Month/Year): Feb 2019
```

### Introduction (context only: never use it for content warnings)

```text
“Health” is something we focus on a lot in today’s society. Fat burning supplements, new diets, exercise programs, eating “clean” — we designate certain things as “healthy,” which makes them desirable.

Fat??? = non-desirable. But is being overweight always a conscious choice to be non-healthy? When it comes to weight, multiple factors are at play, many of which are beyond a person’s control: genetics, childhood habits, medical conditions, and hormones.

This collection, Fat/Skinny Joke by Rachel Wiley and Blythe Baird explores two ends of the body image spectrum. Obesity and anorexia.
```

### Performance text (classify this)

```text
Fat Joke
(Pg 22-23) The old joke goes:
Patient walks into the doctor’s office and says, “Doctor it
hurts when
I move my arm like this, what should I do?” and the doctor
says, “So don’t move your arm like that.”
Now,
Fat Girl walks into the doctor’s office and says, “Doctor, it
hurts
when I move my arm like this, what should I do?” and the
doctor
says, “Have you considered weight loss surgery?”
Fat Girl walks into the doctor’s office for a flue shot
and gets a lecture about BMI
Fat Girl walks into the doctor’s office for an earache and
gets asked if
she’s ever eaten a salad
Fat Girl walks into the doctor’s office with a spider bit and
the
doctor obsesses over how low her blood pressure is – low
for such a
fat person anyway – and insists on checking it 3 times
before he
believes it, has to be reminded of the purple mass of
throbbing spider
venom that brought her here in the first place
Fat Girl walks into the doctor’s office to ask about
antidepressants
and gets prescribed exercise instead
Fat Girl walks into the doctor’s office for a standard 3-
month followup
appointment and the doctor says, “Have you considered
weight
Loss surgery?”
Fat Girl gets tired of only ever being diagnosed fat
so Fat Girl stops walking into the doctor’s office
Fat Girl walks to the store
and has insults flicked at her like still-lit
cigarettes from passing cars
Fat Girl walks onto a crowded bus and stands because she
does not
wish to share a seat and make anyone else uncomfortable
Fat Girl logs onto the internet, gets comments from
keyboard doctors
that claim concern for her health
suggests crash diets
suggests flat-tummy tea
Suggests diet pills that would stop fat girl’s heart but fat girl
will have
died trying to get thin
Fat Girl walks into the world and says,
“World, it hurts to exist like this.”
World says, “So stop existing like that”
World says, “Have you considered weight loss surgery?”
would rather she slice herself open than to exist as she
does
side-effects be damned
Despite all of this, Fat Girl still manages to love her fat body
World says, “Stop glorifying obesity.”
Fat Girl walks up to World, says, “I do not owe you
shrinking, you
know. I do not owe you thinness, attempted thinness, or
desired
thinness because you assume thinness equals health. I do
not owe you
health, perceived or otherwise, to receive basic respect. I
am
deserving of existence. I am deserving of care. I am
deserving of first
no harm done.”
World says,
“That is the best joke we’ve heard all day.”

But it’s a joke that is decidedly un-funny. You hear “anorexia” and you think bone-thin young women -- scary-skinny runway models with emaciated figures. But according to Dr. Leslie A. Sim, clinical director of the Mayo Clinic’s eating disorders program, people with a history of obesity are at “significant risk” for developing anorexia.

When the Fat Girl Gest Skinny by Blythe Baird

When the Fat Girl Gets Skinny

(Pg 3-6) the year of skinny pop and sugar-free jello cups we guzzled vitamin water and vodka

toasting to high school and survival
complimenting each other’s collarbones
trying diets we found on the internet:
menthol cigarettes, eating in front of a mirror,
donating blood.

replacing meals with other practical hobbies
like making flower crowns
or fainting
wondering why I haven't had my period
in months

why breakfast tastes like
giving up
or how many more productive ways
I could have spent my time today
besides googling the calories
in the glue of a US envelope
watching America's Next Top Model
like the gospel,
hunching naked over a bathroom scale shrine,
crying into an empty bowl of Cocoa Puffs
because I only feel pretty
when I'm hungry
if you are not recovering,
you are dying.
by the time I was sixteen, I had already experienced being
clinically overweight, underweight, and obese.

as a child, fat was the first word
people used to describe me,
which didn’t offend me until
I found out it was supposed to.
when I lost weight, my dad was so proud
he started carrying my before-and-after photo
in his wallet.
so relieved he could stop worrying
about me getting diabetes.
he saw a program on the news
about the epidemic with obesity
says he is just so glad to finally see me
taking care of myself.
if you develop an eating disorder
when you are already thin to begin with,
you go to the hospital.
if you develop an eating disorder
when you are not thin to begin with,
you are a success story.
so when I evaporated, of course
everyone congratulated me
on getting healthy.

girls at school who never spoke to me before stopped me in the hallway to ask how I did it. I say, I am sick. They say No, you are

an inspiration.
How could I not fall
in love with my illness?
With becoming the kind of silhouette
people are supposed to fall in love with?
why would I ever want to stop
being hungry
when anorexia was the most
interesting thing about me?
so, how lucky it is, now,
to be boring
the way not going to the hospital
is boring.
the way looking at an apple
and seeing only an apple, not sixty
or half an hour of sit-ups
is boring.
My story may not be as exciting as it used
to be, but at least there is nothing left
to count.
the calculator in my head
finally stopped.
I used to love the feeling of drinking water
on an empty stomach
waiting for the coolness to slip all
the way down and land in the well
not obsessed with being empty
but afraid of being full.
I used to take pride in being able to feel
cold in a warm room.
now, I am proud I have stopped
seeking revenge on this body.
this was the year of eating
when I was hungry

without punishing myself
and I know it sounds ridiculous,
but that shit is hard.
when I was little,
someone asked me

what I wanted to be when I grew up,

and I said

small
```

---

## IC-1787: The Father

- Title: The Father
- Author (byline): Sharon Olds
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1179
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sharon Olds
Book: The Father
ISBN: 978-0679740025
Publisher: Knopf
Date (Month/Year): April 1992
Author: Sharon Olds
Book: The Gold Cell
ISBN: 978-0394747705
Publisher: Knopf
Date (Month/Year): February 1987
Author: Sharon Olds
Book: The Sign of Saturn
ISBN: 978-0436200298
Publisher: Secker and Warburg
Date (Month/Year): March 1991
Author: Sharon Olds
Book: The Sign of Saturn
ISBN: 978-0436200298
Publisher: Secker and Warburg
Date (Month/Year): March 1991
Author: Sharon Olds
Book: The Father
ISBN: 978-0679740025
Publisher: Knopf
Date (Month/Year): April 1992
```

### Introduction (context only: never use it for content warnings)

```text
Sharon Olds grew up in San Francisco, the daughter of an abusive, alcoholic father. But when her father is diagnosed with uncurable throat cancer, she begins to examine not only his rapid decline, but their relationship. This collection highlights the complicated and difficult relationship we often have with parents, death and illness and is an unbelievably powerful journey of love and hate. The Father by Sharon Olds
```

### Performance text (classify this)

```text
His Stillness
The doctor said to my father, “You asked me
to tell you when nothing more could be done.
That’s what I’m telling you now.” My father
sat quite still, as he always did,
especially not moving his eyes. I had thought
he would rave if he understood he would die,
wave his arms and cry out. He sat up,
thin, and clean, in his clean gown,
like a holy man. The doctor said,
“There are things we can do which might give you time,
but we cannot cure you.” My father said,
“Thank you.” And he sat, motionless, alone,
with the dignity of a foreign leader.
I sat beside him. This was my father.
He had known he was mortal. I had feared they would
have to
tie him down. I had not remembered
he had always held still and kept quiet to bear things,
the liquor a way to keep still. I had not
known him. My father had dignity. At the
end of his life, his life began
to wake in me.

Late Poem to My Father

Suddenly I thought of you
as a child in [your father’s] house, the unlit rooms
and the hot fireplace with the man in front of it,
silent. You moved through the heavy air
in your physical beauty, a boy of seven,
helpless, smart, there were things the man
did near you, and he was your father,
the mold by which you were made. Down in the
cellar, the barrels of sweet apples,
picked at their peak from the tree, rotted and
rotted, and past the cellar door
the creek ran and ran, and something was
not given to you, or something was
taken from you that you were born with,
so that even at 30 and 40 you set the
oily medicine to your lips
every night, the poison to help you
drop down unconscious. I always though the
point was what you did to us
as a grown man, but then I remembered
that child being formed in front of the fire, the
tiny bones inside his soul
twisted in greenstick fractures, the small
tendons that hold the heart in place
snapped. And what they did to you
you did not do to me. When I love you now,
I like to think that I am giving my love
directly to that boy in the fiery room,

As if it could reach him in time.

TRANSITION

Children are incredibly susceptible to parental influence and neglect. As a result, growing up with an alcoholic parent can have serious consequences in both the short-term and the long-term. In Saturn, Olds recalls an image of her father lying on a couch, consuming his child (like the Olympian god) by indifference.

Saturn
He lay on the couch night after night,
mouth open, the darkness of the room
filling his mouth, and no one knew
my father was eating his children. He seemed to
rest so quietly, vast body
inert on the sofa, big hand
fallen away from the glass.
What could be more passive than a man
passed out every night--and yet as he lay
on his back, snoring, our lives slowly
disappeared down the hole of his life.
My brother's arm went in up to the shoulder
and he bit it off, and sucked at the wound
as one sucks at the sockets of lobster. He took
my brother's head between his lips
and snapped it like a cherry off the stem. You would
have
seen
only a large, handsome man
heavily asleep, unconscious. And yet
somewhere in his head his soil-colored eyes
were open, the circles of the whites glittering
as he crunched the torso of his child between his jaws,
crushed the bones like the soft shells of crabs
and the delicacies of the genitals
rolled back along his tongue. In the nerves of his gums
and
bowels he knew what he was doing and he could not
stop himself, like orgasm, his
boy's feet crackling like two raw fish
between his teeth. This is what he wanted,
to take that life into his mouth
and show what a man could do--show his son
what a man's life was.

TRANSITION

Faced with her father’s eminent death, Olds struggles with feelings of both love and hate, brokenness and forgiveness.

The Struggle

When the minister would come into the hospital room
my father would try to sit up, he would cry out
Up! Up! For us to raise his bed-head, then
silently he would wrestle himself
up, sweating, he would end up
leaning n the pillows, panting, a man, erect.
The minister would kiss him, they would pray, then chat,
he would hold his eyes open unblinking,
rigid adherent to the protocol of the living,
he would sit for the whole visit, and then,
the minute the man was out the door, cry
out Down! Down! And we would lower him
down, and he would pass out.
Later the doctor would pay a call and as
soon as my father saw that white coat
he would start to labor up, desperate
to honor the coat, at a glimpse of it he would
start to stir like a dog who could not
not obey. He would lurch, pause,
then thrust up slowly and unevenly, like a
camel, a half-born animal – the way,
they say, his soul will pull itself up
out of his dead body and wobbingly
walk. And then, one day, he tried,
his brain ordered his body to heave up,
the sweat rose in his pores but he was not
moving, he cast up his eyes as the minister
leaned to kis him, he lay and stared, it was
nothing like the night he had lain on the couch passed
out, nothing. [For] Now he was alive . . .

Beyond Harm

A week after my father died
suddenly I understood
his fondness for me was safe – nothing
could touch it. In that last year,
his face would sometimes brighten when I would
enter the room, and his wife said
that once, when he was half asleep,
he smiled when she said my name. He respected
my spunk – when they tied me to the chair, that time
they were tying up someone he respected, and when
he did not speak, for weeks, I was one of the
beings to whom he was not speaking,
someone with a place in his life. The last
week he even said it, once,
by mistake. I walked into his room
‘How are you’ and he said ‘I love you
too.’ From then on, I had
that word to lose. Right up to the last
moment, I could make some mistake, offend him,
and with one of his old mouths of disgust he could
re-skew my life. I did not think of it much,
I was helping to take care of him,
wiping his face and watching him.
But then, a while after he died,
I suddenly thought, with amazement, he will always
love me now, and I laughed – he was dead, dead!
```

---

## IC-1788: The Father of My Country

- Title: The Father of My Country
- Author (byline): Diane Wakoski
- Work: Emerald Ice: Selected Poems
- Publisher: Black Sparrow Press
- Publication date as stated: April 2005
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 925
- Already set (do not supply): none

### Source block (context only)

```text
Author: Diane Wakoski
Book: Emerald Ice: Selected Poems
ISBN: 978-0876857441
Publisher: Black Sparrow Press
Date (Month/Year): April 2005
```

### Introduction (context only: never use it for content warnings)

```text
A child's abandonment by a parent is perhaps the most grievous loss a child can suffer. It's worse than a parent's death because, in most cases, a parent's death is not willed by the parent. The Father of My Country by Diane Wakoski address this family crisis from a confessional mode—it deals with a private subject (in this case, family problems) in a public way. There is a feeling of taboo about the subject, and though the poem is not necessarily true in a literal sense, it does give the impression of being drawn from life. The Father of My Country by Diane Wakoski.
```

### Performance text (classify this)

```text
All fathers in Western civilization must have
a military origin. The
ruler,
governor,
yes,
he is
was the
general at one time or other.
And George Washington
won the hearts
of his country—the rough military man
with awkward
sincere
drawing-room manners.

My father;
have you ever heard me speak of him? I seldom
do. But I had a father,
and he had military origins—or my origins from
him
are military,
militant. That is, I remember him only in uniform. But of
the navy,
30 years a chief petty officer,
always away from home.

It is rough/hard for me to speak
now.
I'm not used to talking
about him.

Not used to naming his objects/ objects that never surrounded me.

A woodpecker with fresh bloody crest
knocks
at my mouth. Father, for the first
time I say
your name. Name rolled in thick Polish parchment scrolls,
name of Roman candle drippings when I sit at my table
alone, each night,
name of naval uniforms and name of
telegrams, name of
coming home from your aircraft carrier,
name of shiny shoes.
name of Hawaiian dolls, name
of mess spoons, name of greasy machinery, and name of
stencilled names.
Is it your blood I carry in a test tube,
my arm,
to let fall, crack, and spill on the sidewalk
in front of the men
I know,
I love,
I know, and
want? So you left my house when I was under two.
being replaced by other machinery (my sister), and
I didn’t believe you left me.

This scene: the trunk yielding treasures of

a green fountain pen, heart shaped mirror,

amber beads, old letters with brown ink, and

the gopher snake stretched across the palm tree

in the front yard with woody trunk like monkey skins,

and a sunset through the skinny persimmon trees. You

came walking, not even a telegram or post card from

Tahiti. Love, love, through my heart like ink in

the thickest nibbed pen, black and flowing into words

You came, to me, and I at least six. Six doilies

of lace, six battleship cannon, six old beerbottles,

six thick steaks, six love letters, six clocks

running backwards, six watermelons, and six baby

teeth, a six cornered hat on six men's heads, six

lovers at once or one lover at sixes and sevens;

how I confuse

all this with my

dream

walking the tightrope bridge

with gold knots

over

the mouth of an anemone/tissue spiral lips

and holding on so that the ropes burned

as if my wrists had been tied

If George Washington
had not
been the Father
of my Country
it is doubtful that I would ever have
found
a father. Father in my mouth, on my lips, in my
tongue, out of all my womanly fire,
Father I have left in my steel filing cabinet as a name on
my birth
certificate, Father I have left in the teeth pulled out at
dentists’ offices and thrown into their garbage cans,
Father living in my wide cheekbones and short feet,
Father in my Polish tantrums and my American speech,
Father, not a
holy name, not a name I cherish but the name I bear,
the name
that makes me one of a kind in any phone book because
you changed it, and nobody
but us
has it,
Father who makes me dream in the dead of night of the
falling cherry
blossoms, Father who makes me know all men will leave
me
if I love them,
Father who made me a maverick,
a writer,
a namer,
name/father, sun/father, moon/father, bloody
mars/father,
other children said, “My father is a doctor,”
or
“My father gave me this camera,”
or
“My father took me to
the movies,”
or
“My father and I went swimming,”
but
my father is coming in a letter
once a month
for a while,
and my father
sometimes came in a telegram
but
mostly
my father came to me
in sleep, my father because I dreamed in one night that
I dug
through the ash heap in back of the pepper tree and
found a diamond
shaped like a dog, and my father called the dog and it
came leaping
over to him and he walked away out of the yard down the
road with
the dog jumping and yipping at his heels,

my father was not in the telephone book
in my city;
my father was not sleeping with my mother
at home;
my father did not care if I studied the
piano;
my father did not care what
I did;
and I thought my father was handsome and I loved him
and I wondered
why
he left me alone so much,
so many years
in fact, but
my father made me what I am,
a lonely woman,
without a purpose, just as I was
a lonely child
without any father. I walked with words, words, and
names,
names. Father was not
one of my words.
Father was not
one of my names. But now I say, “George, you have
become my father,
in his 20th century naval uniform. George Washington, I
need your
love; George, I want to call you Father, Father, my
Father,”
Father of my country,
that is,
me. And I say the name to chant it. To sing it. To lace it
around
me like weaving cloth. Like a happy child on that shining
afternoon
in the palm tree sunset with her mother’s trunk yielding
treasures,
I cry and
cry,
Father,
Father,
Father,
have you really come home?
```

---

## IC-1789: Fathers and Mothers – A Collection

- Title: Fathers and Mothers – A Collection
- Author (byline): Sarah Freligh
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1164
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sarah Freligh
ISBN: On-Line Magazine
https://www.cleavermagazine.com/our-fathers-by-
sarah-freligh/
Publisher: Cleaver Magazine.com
Date (Month/Year): September 23, 2021
Author: Sarah Freligh
ISBN: On-Line Transcript
https://sapphostorque.com/2017/04/09/poem-a-
day-sarah-freligh/
Publisher: Sapphos Torque.com
Date (Month/Year): April 9, 2017
Author: Sarah Freligh
Book: Sad Math
ISBN: 978-0913785645
Publisher: Moon City Press
Date (Month/Year): Dec 2015
Author: Sarah Freligh
ISBN: On-Line Magazine
https://www.thesunmagazine.org/issues/440/selected-
poems-sarah-freligh-issue-440
Publisher: The Sun Magazine.org
Date (Month/Year): Issue 440. August 2012
Author: Sarah Freligh
Book: Sad Math
ISBN: 978-0913785645
Publisher: Moon City Press
Date (Month/Year): Dec 2015
```

### Introduction (context only: never use it for content warnings)

```text
Parents, whether they are biological, adopted, step-parents or a parental figure you chose; they become your anchors -- calm voices in a sea of doubt, beacons of love.

And losing them, regardless of how old you are when that happens, is “something like driving through a plate-glass window. You didn’t know it was there until it shattered. And for years to come, you’re picking up the pieces, down to
```

### Performance text (classify this)

```text
Our Fathers

Our fathers rise at five and whistle out the door carrying thermoses of black coffee and lunches our mothers have packed for them—bags of corn chips and sandwiches made of meat and cheese. Our mothers tuck notes into the wrap of waxed paper.

◊ Weekends our fathers box-step us around the living room or somersault us from their shoulders into the deep end of a swimming pool. Sometimes our fathers will lock themselves away and listen to the Tigers on the radio or slide under cars until they’re called to wash up for dinner.

◊ Our fathers are men. What our mothers say when we ask why our fathers never cook or change diapers. Restless men, they say. Later they’ll say it with rolled eyes. Men, they will say. Our only inheritance.

the last glassy splinter.” – Saul Bellow, Nobel Prize for Literature Fathers and Mothers – A Collection by Sarah Freligh

Our Fathers (con’t)

Our fathers rise at five and whistle out the door carrying thermoses of black coffee and lunches our mothers have packed for them—bags of corn chips and sandwiches made of meat and cheese. Our mothers tuck notes into the wrap of waxed paper.

◊ Weekends our fathers box-step us around the living room or somersault us from their shoulders into the deep end of a swimming pool. Sometimes our fathers will lock themselves away and listen to the Tigers on the radio or slide under cars until they’re called to wash up for dinner.

◊ Our fathers are men. What our mothers say when we ask why our fathers never cook or change diapers. Restless men, they say. Later they’ll say it with rolled eyes. Men, they will say. Our only inheritance.

◊ On summer nights our fathers gather with other fathers in back yards to drink and bitch about the foreman, the infernal factory clatter. They brag about the muscle cars they’re building, the flex and thrum of their big engines.

◊ Some of our fathers die drunk in head-ons or face down on the factory floor, their rotted hearts knotted as pine trees. Some of our fathers carry their coffins and try not to cry.

◊ Our fathers circle the padlocked gate of the Ford plant carrying signs they shake at the scabs who have stolen their jobs. Our fathers walk in snow and rain, raise clenched fists at the cars that honk past them. They stay out late drinking beer, roll home long after we’re in bed.

◊ Our fathers are shut down, laid off. They drink beer from cans that they crush in their hands and leave on the coffee table for us to clean up. Our mothers tiptoe around our fathers, steer clear of their simmer and filth. They whisper over the slosh of the dishwasher about how hard it is for a man not to work.

◊ After the Ford plant closes, our fathers go back to school at night. Shaved raw and choked by neckties, they stare down the glare of computer screens. Other fathers disappear into the dark bars downtown, lit by the flicker of TV screens and the thunder of fights.

◊ We grow up, go away, marry men who are not our fathers, men with soft hands and clean fingernails. Men who read stories to their daughters about cloth rabbits and moons and spiders that die alone.

◊ Our fathers get old and then older. Soon enough they’re headlights on a wall, there and gone. Shadows, then ghosts.

So I Call My Mother On Sunday

So I call my mother on Sunday
every Sunday, though I don’t say
how are you anymore because I know
she’s dying and each day will be worse
than the day before. Her liver’s rotting
the way an apple goes bad, swelling
as it softens and maybe smells sweet
as fruit does before you toss it.
I ask her how the weather is, snowing
like crazy here, about the traffic
at the bird feeder. She likes to watch
the small birds, chickadees and nuthatches,
not so much the sparrows though
today she says the minister’s there
and she’s planning her funeral. She wants
to be cremated. She wants an urn
and the family to bury her, no one else
in attendance. A memorial service, maybe
sandwiches after. It’s been snowing
every day for a week now, I say, we’re knee
deep in it. Did you hear me, she says
and I tell her it’s such heavy snow
to shovel every hour I get so tired
of shoveling, god, I want to cry.

from The Beginning of Something is Always the
End of Another
. . . .I know this will end in ashes
at a cemetery where we stood
over my mother’s urn, hugless, useless
hands dangling from our dumb arms
while on the hill above us a guy wearing
soiled khakis lounged in a golf cart,
waiting for us to understand this was it,
the end, we needed to leave already
so he could finally begin to dig.

Safe After we buried my mother, we told stories in the room where she’d died. The hospital bed was gone, the love seat tucked flush with the window again, long sofa shoved against the wall like always, the same sofa where she’d fall asleep watching baseball while she waited for me to come home from some high-school date, and once, when I wasn’t home by midnight, she threw a raincoat over her flannel pajamas and drove around until she found me behind the Big Boy with the second-string quarterback. All the way home and for an entire week, I was punished by silence, a vast black void of disgust. The last time I saw her, I wanted her to speak to me, to lock the front door and turn off the last light, to follow me upstairs, having made the house safe for the night. But she didn’t know who I was.

Wondrous

I’m driving home from school when the radio talk turns to E.B. White, his birthday, and I exit the here and now of the freeway at rush hour,

travel back into the past, where my mother is reading to my sister and me the part about Charlotte laying her

eggs and dying, and though this is the fifth time Charlotte

has died, my mother is crying again, and we’re laughing at her because we know nothing of loss and its sad math, how every subtraction is exponential, how each grief

multiplies the one preceding it, how the author tried seventeen times to record the words She died alone without crying, seventeen takes and a short walk during which he called himself ridiculous, a grown man crying for a spider he’d spun out of the silk thread of invention — wondrous how those words would come back and make

him cry, and, yes, wondrous to hear my mother’s voice ten years after the day she died — the catch, the rasp, the gathering up before she could say to us, I’m OK.
```

---

## IC-1790: Fierce Fairytales (Female Strength)

- Title: Fierce Fairytales (Female Strength)
- Author (byline): Nakita Gill
- Work: Not specified
- Publisher: Hachette Books
- Publication date as stated: Sept 2018
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1116
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nakita Gill
ISBN: 978-0316420747
Publisher: Hachette Books
Date (Month/Year): Sept 2018
```

### Introduction (context only: never use it for content warnings)

```text
Cinderella; Snow White; Sleeping Beauty and Wendy Moira Angela Darling. *snort in disdain* Traditional fairytales are rife with cliches and gender stereotypes. The heroines are beautiful, kind, helpful, compassionate . . . helpless, naïve, submissive and weak. It’s time we moved these tales into the 21st century, where women are so much more. Women are powerful. Women are fierce.

Today you’ll hear the innermost thoughts of Pandora as she battles the evils of humanity; you’ll be encouraged to find your voice by Poseidon’s daughter Ariel; and you’ll find your strength with Gretel; not Hansel and Gretel . . . just Gretel. Because women are so much more than fairytales make them out to be. Women are powerful. Women are fierce.

Fierce Fairytales by Nakita Gill
```

### Performance text (classify this)

```text
Question the Fairytale (Pg 148)

What if Cinderella had an attitude problem and Snow White just liked the idea of strangers and poisons too much?

What if the Little Mermaid always enjoyed human

company more than her own kind's and Sleeping Beauty just liked her solitude more than human touch?

What if the only rabbit hole Alice ever fell down was a terrible mistake with an awful substance, never discussed as such?

What if they locked Wendy away for hallucinating about Neverland and a boy who never grew up?

What if fairytales aren't as innocent as they sound and even princesses aren't perfect?

What if I told you that your damage doesn't define you and the way you survive is no one else's damned business?

The Moral of Your Story (Pg 117)

This is how they lie to us: Love, love so selflessly that you change the world.

The truth is brutal:
if you care this way
the world will gut you mercilessly.
And harsher still:
all of this love you hold
is too selfless.

Yes, my dear, too selfless exists no matter how much they deny it.

You see, you have been
taught to give too much
without wanting anything back.
What no one tells you
is this constant sacrifice
is designed to keep you pliant.

It is designed to keep you weak and one day it will devastate you.

And what good are you destroyed to anyone, to anything, especially to your own truth?

Pandora's Mind (Pg 103)

Seeking the secret potion to happiness inside the rooms of my mind may as well be walking through all the chambers of Pandora's box.

In there, religion nodded knowingly,
'Confess every sin, all of them,
lay your heart before God, you will feel lighter.'
I tried it but I also kept sinning,
so the light never came —
-- as my common sense pressed her fingertips together,
'Keep a journal and put all of your feelings
inside it,' and I made an effort, I really did,
but my feelings are so many that even
a hundred journals later I am not empty –

-- as social expectation interjected,
'What you need is a husband with strong hands
and he can take out all the sadness shelves
that are lined up inside your head.' But it doesn't know that
these shelves just build themselves back up –

-- as my depression politely informed me,
'No one is really going to love you,
you are too difficult to love anyway.'
And I tried and tried to make myself more loveable,
But in the process I just lost myself—

-- as my anxiety screamed in annoyance, 'Worry about other things like the moon moving farther from the earth every year or your mother's heart or‘ And all I know now is how to worry about dead stars and money at the same time –

-- as social conditioning tried to educate me,
'Perhaps things like dreaming to be a writer
when you could do something sensible is the problem.' And
I tried my best to silence myself,
but my voice was too strong –
-- yet a little voice inside me called Hope said softly,
'Millions of good people die unhappy every year,
not a single one of them is coming back
to give the world a chance to change
and deserve them.'

And it reminded, 'Maybe living your truth may not make you happy all the time, but it will make you happy every day.'

And it believed, 'Perhaps stand for what you believe in, even if you are the only one in the whole room.'

And it whispered, 'Perhaps the secret to your own happiness lies inside the owning of who you are, even broken.'

So I mixed the roots of hope together inside an inkwell, filled a pen, and finally wrote my truth.

An Older and Wiser Little Mermaid Speaks (Pg 81)

There are so many ways to lose a voice.
An uncomfortable laugh, don't make a scene
what will people say about you
what will people say about us.

I ask you now,
do women pray to softer-spoken gods than men do?
Do men pray louder and more
unapologetically than women ever have?

We are taught not to speak and if we do
be pliant, be passive, be soft, be sorry.
You are better as water anyway.
Water is supposed to simply adapt.

I ask you now, as the granddaughter of Poseidon
who gave up her fins and voice for love,
not to trade your magic in for anyone.
Do not make sacrifice the ritual of your womanhood.

I teach my half-sea girls that their voices
are the most powerful things they can use,
to let the word 'no' become the charm
they need to help them take up space often.

Now the mermaids are becoming sirens,
for sirens are monsters who never feel compelled and
monsters, unlike girls and mermaids,
know how to protect themselves well.

Gretel After Hansel (Pg 73)

Did anyone ever tell you what happens if you kill a witch before you grow up? That you leave a part of yourself in that storybook

place,
saccharine sweet with bitter memories?
You are half fairytale, half girl,
with parents who chose to abandon you,
a brother who swore he would never leave
then found a wife and left you.
And here you are, picking yourself apart
breadcrumb by breadcrumb,
trying to learn how to swallow survival,
but a part of you never left the witch's door.
You still have the grit and determination
that stopped a child-eating monster
in her tracks; that wasn't Hansel, that was you.
And damaged though you are, that girl is still there.
Our stories don't begin and end
because men we once trusted have left them,
we were made whole to start with,
independent tales of strength and madness.
What I am trying to say is, Gretel,
you define yourself, without your brother;
you define yourself with your courage,
which was already imprinted on your bones.
No one taught you how to survive,
darling, you did that on your own.
Even without him, you can bring down monsters.
Believe me. You can still bring down monsters.

Once Upon a Time II (Pg 4)

It is up to you to rise again from the fragmented shards your foes left of you.

You must lift a sword with reborn strength and take on the demons in your ribcage.

You must devastate the chains every violent person has brutally placed on you.

And you must show them all how they were simply characters in your story.

But you, you are the author of this spellbinding tale built of hope and bravery.

Out there may be monsters, my dear. But in you still lives the dragon you should always believe in.
```

---

## IC-1791: First Writing Since

- Title: First Writing Since
- Author (byline): Suheir Hammad
- Work: Word Warriors
- Publisher: Seal Press
- Publication date as stated: Oct 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1507
- Already set (do not supply): none

### Source block (context only)

```text
Author: Suheir Hammad
Book: Word Warriors
ISBN: 978-1580052214
Publisher: Seal Press
Date (Month/Year): Oct 2007
```

### Introduction (context only: never use it for content warnings)

```text
In 2000, Suheir Hammad was just an obscure writer and occasional college student putting in work on the New York poetry circuit and taking to the streets for a variety of political causes. Then terrorists attacked her city – the infamous 9/11 terrorist attack. The 28-year-old responded the only way she knew how: She jotted down a poem, “First Writing Since.” Amid the ocean of print inspired by That Day, perhaps no other collection of words has so succinctly articulated the strange confluence of being both Muslim and American in that moment in history. First Writing Since by Suheir Hammad.
```

### Performance text (classify this)

```text
1. there have been no words.
i have not written one word.
no poetry in the ashes south of canal street.
no prose in the refrigerated trucks driving debris and
dna.
not one word.

today is a week, and seven is of heavens, gods, science. evident out my kitchen window is an abstract reality. sky where once was steel. smoke where once was flesh.

fire in the city air and i feared for my sister's life in a way never before. and then, and now, i fear for the rest of us. first, please god, let it be a mistake, the pilot's heart failed, the plane's engine died. then please god, let it be a nightmare, wake me now. please god, after the second plane, please, don't let it be anyone who looks like my brothers.

i do not know how bad a life has to break in order to kill. i have never been so hungry that i willed hunger i have never been so angry as to want to control a gun over a pen. not really. even as a woman, as a palestinian, as a broken human being. never this broken.

more than ever, i believe there is no difference. the most privileged nation, most americans do not know the difference between indians, afghanis, syrians, muslims, sikhs, hindus. more than ever, there is no difference.

2. thank you korea for kimchi and bibim bob, and corn tea and the genteel smiles of the wait staff at wonj -- smiles never revealing the heat of the food or how tired they must be working long midtown shifts. thank you korea, for the belly craving that brought me into the city late the night before and diverted my daily train ride into the world trade center.

there are plenty of thank yous in ny right now. thank you for my lazy procrastinating late ass. thank you to the germs that had me call in sick. thank you, my attitude, you had me fired the week before. thank you for the train that never came, the rude nyer who stole my cab going downtown. thank you for the sense my mama gave me to run. thank you for my legs, my eyes, my life.

3. the dead are called lost and their families hold up shaky printouts in front of us through screens smoked up.

we are looking for iris, mother of three. please call with any information. we are searching for priti, last seen on the 103rd floor. she was talking to her husband on the phone and the line went. please help us find george, also known as adel. his family is waiting for him with his favorite meal. i am looking for my son, who was delivering coffee. i am looking for my sister girl, she started her job on monday.

i am looking for peace. i am looking for mercy. i am looking for evidence of compassion. any evidence of life. i am looking for life.

4. ricardo on the radio said in his accent thick as yuca, "i will feel so much better when the first bombs drop over there. and my friends feel the same way."

on my block, a woman was crying in a car parked and stranded in hurt. i offered comfort, extended a hand she did not see before she said, "we're gonna burn them so bad, i swear, so bad." my hand went to my head and my head went to the numbers within it of the dead iraqi children, the dead in nicaragua. the dead in rwanda who had to vie with fake sport wrestling for america's attention.

yet when people sent emails saying, this was bound to happen, let's not forget u.s. transgressions, for half a second i felt resentful. hold up with that, cause i live here, these are my friends and fam, and it could have been me in those buildings, and we're not bad people, do not support america's bullying. can i just have a half second to feel bad?

if i can find through this exhaust people who were left behind to mourn and to resist mass murder, i might be alright.

thank you to the woman who saw me brinking my cool and blinking back tears. she opened her arms before she asked "do you want a hug?" a big white woman, and her embrace was the kind only people with the warmth of flesh can offer. i wasn't about to say no to any comfort. "my brother's in the navy," i said. "and we're arabs." "wow, you got double trouble." word.

5. one more person ask me if i knew the hijackers. one more motherfucker ask me what navy my brother is in. one more person assume no arabs or muslims were killed. one more person assume they know me, or that i represent a people. or that a people represent an evil. or that evil is as simple as a flag and words on a page.

we did not vilify all white men when mcveigh bombed oklahoma. america did not give out his family's addresses or where he went to church. or blame the bible or pat robertson.

and when the networks air footage of palestinians dancing in the street, there is no apology that hungry children are bribed with sweets that turn their teeth brown. that correspondents edit images. that archives are there to facilitate lazy and inaccurate journalism.

and when we talk about holy books and hooded men and death, why do we never mention the kkk?

if there are any people on earth who understand how new york is feeling right now, they are in the west bank and the gaza strip.

6. today it is ten days. last night bush waged war on a
man once
openly funded by the cia. i do not know who is
responsible. read
too many books, know too many people to believe what i
am told. i don't give a fuck about bin laden. his vision of
the
world does not include me or those i
love. and petitions have been going around for years
trying to get
the u.s. sponsored taliban out of power. shit is
complicated, and i
don't know what to think.

but i know for sure who will pay.

in the world, it will be women, mostly colored and poor. women will have to bury children, and support themselves through grief. "either you are with us, or with the terrorists" -- meaning keep your people under control and your resistance censored. meaning we got the loot and the nukes.

in america, it will be those amongst us who refuse blanket attacks on the shivering. those of us who work toward social justice, in support of civil liberties, in opposition to hateful foreign policies.

i have never felt less american and more new yorker -- particularly brooklyn, than these past days. the stars and stripes on all these cars and apartment windows represent the dead as citizens first -- not family members, not lovers.

i feel like my skin is real thin, and that my eyes are only going to get darker. the future holds little light. my baby brother is a man now, and on alert, and praying five times a day that the orders he will take in a few days time are righteous and will not weigh his soul down from the afterlife he deserves.

both my brothers -- my heart stops when i try to pray -- not a beat to disturb my fear. one a rock god, the other a sergeant, and both palestinian, practicing muslim, gentle men. both born in brooklyn and their faces are of the archetypal arab man, all eyelashes and nose and beautiful color and stubborn hair.

what will their lives be like now?

over there is over here.

7. all day, across the river, the smell of burning rubber and limbs floats through. the sirens have stopped now. the advertisers are back on the air. the rescue workers are traumatized. the skyline is brought back to human size. no longer taunting the gods with its height.

i have not cried at all while writing this. i cried when i saw those buildings collapse on themselves like a broken heart. i have never owned pain that needs to spread like that. and i cry daily that my brothers return to our mother safe and whole.

there is no poetry in this. there are causes and effects. there are symbols and ideologies. mad conspiracy here, and information we will never know. there is death here, and there are promises of more.

there is life here. anyone reading this is breathing, maybe hurting, but breathing for sure. and if there is any light to come, it will shine from the eyes of those who look for peace and justice after the rubble and rhetoric are cleared and the phoenix has risen.

affirm life.
affirm life.
we got to carry each other now.
you are either with life, or against it.
affirm life.
```

---

## IC-1792: For Colored Girls Who Have Considered Suicide . . .

- Title: For Colored Girls Who Have Considered Suicide . . .
- Author (byline): Ntozake Shange (En-toe-ZAK-kay
- Work: Not specified
- Publisher: Bantam Books, Inc.
- Publication date as stated: 1980
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: CHARACTER
- Teaser before the introduction: Yes
- Spoken words (computed): 1473
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ntozake Shange
ISBN: 978-0553133073
Publisher: Bantam Books, Inc.
Date (Month/Year): 1980
```

### Introduction (context only: never use it for content warnings)

```text
Let me take you back to the late 60’s/early 70s and just how difficult it was to be a black female at the time. Facing hardships and continuing to survive despite horrific experiences, being black as well as female placed these women in a double minority. In For Colored Girls Who Have Considered Suicide Ntozake Shange shares the good and bad personal experiences of women of color. First to share her perspective is the Lady in Blue . .
```

### Performance text (classify this)

```text
SHONG-gay)

Character: Lady in Blue

i'm outside manhattan

i used ta live in the world

then i moved to HARLEM

& my universe is now six blocks
when i walked in the pacific
i imagined waters ancient from accra/ tunis
cleansing me/ feeding me
now my ankles are coated in grey filth
from the puddle near the hydrant

my oceans were life
what waters i have here sit stagnant
circling ol men's bodies
& broken lil whiskey bottles
left to make me bleed

iusedta live in the world
now i live in harlem & my universe is six blocks
a tunnel with a small train
ican ride anywhere
remaining a stranger

icd stay alone
a woman in the world
then i moved to
HARLEM
icome in at dusk
stay close to the curb

wdnt be good
not good at all
to meet a tall short black brown young man fulla his
power
in the dark
in my universe of six blocks

iusedta live in the world
really be in the world
free & sweet talkin
good mornin & thank-you & nice day
uh-huh
ican't now
ican't be nice to nobody
nice is such a rip-off
reglar beauty & a smile in the street
is just a set-up

ihadda right to the world
then i moved to harlem for the set-up
a universe
six blocks of cruelty
piled up on itself
a tunnel
closin
we deal wit emotion too much
so why dont we go on ahead & be white then/
&make everythin dry & abstract wit no rhythm & no
reelin for sheer sensual pleasure/yes let's go on
&be white/ we're right in the middle of it/ no use
holdin out/ holdin onto ourselves/ lets think our
way outta feelin/ let's abstract ourselves some
families
&thinkin wont do me a bit of
good tonite/ i need to be loved/ & havent the audacity
to say
where you are/ & dont know who to say it to
one thing i dont need
is anymore apologies
igot sorry greetin me at my front door
you can keep yrs
idont know what to do wit em
they dont open doors
or bring the sun back
they dont make me happy
or get a mornin paper
didnt nobody stop usin my tears to wash cars
cuz a sorry
iam simply tired
of collectin

i didnt know

i was so important to you'
i'm gonna haveta throw some away
icant get to the clothes in my closet
for alla sorries
i'm gonna tack a sign to my door
leave a message by the phone

'if you called

to say yr sorry

call somebody

else

i dont use em anymore'
ilet sorry/ didnt meanta/ & how cd i know abt that
take a walk down a dark & musty street in brooklyn
i'm gonna do exactly what i want to
&i wont be sorry for none of it
letta sorry soothe yr soul/
i'm gonna soothe mine
you were always inconsistent
doin somethin & then bein sorry
beatin my heart to death
talkin bout you sorry
well
iwill not call
i'm not going to be nice
iwill raise my voice
&scream & holler
&break things & race the engine
&tell all yr secrets about yrself to your face
&i will list in detail everyone of my wonderful lovers
&their ways
&i wont be sorry for none of it
iloved you on purpose
iwas open on purpose
istill crave vulnerability & close talk
& i'm not even sorry bout you bein sorry
you can carry all the guilt & grime ya wanna
just dont give it to me
icant use another sorry
next time
you should admit
you're mean/ lowdown /trifin/ & no count straight out
steada being sorry alla the time
enjoy being yrself
ifound god in myself
&i loved her/ i loved her fiercely
& this is for colored girls who have considered

suicide/ but are movin to the ends of their own rainbows TRANSITION While the Lady in Blue struggles to adjust to a life in Harlem, surrounded by values and a society very different from what she has known . . . While she struggles to come to terms with what she is willing to accept and what she wants for herself , The Lady in Yellow relates a quite different reality: The celebration of her graduation from high school . . .

CHARACTER: Lady in Yellow

it was graduation nite & i waz the only virgin in the
crowd
bobby mills martin jerome & sammy yates eddie jones &
randi
all cousins
all the prettiest niggers in this factory town
carried me out wit em
in a deep black buick
smellin of thunderbird & ladies in heat
we rambled from camden to mount holly
laughin at the afternoon’s speeches
& danglin our tassles from the rear view mirror
climbin different sorta project stairs
movin toward snappin beer cans &
GET IT GET IT THAT’S THE WAY TO DO IT MAMA
all mercer county graduated the same nite
cosmetology secretarial pre-college autoshop & business
all us movin from mama to what ever waz out there
that nite we raced a big ol truck from the barbeque
stand
trying to tell him bout the party at jacqui’s
where folks graduated last year waz waitin to hit it wid
us
i got drunk & cdnt figure out
whose hand waz on my thigh/but it didn’t matter
cuz these cousins martin eddie sammy jerome & bobby
waz my sweethearts alternately since the seventh grade
& everybody knew i always started cryin if somebody
actually
tried to take advantage of me
at jacqui’s
ulinda mason was stickin her mouth all out
while we tumbled out the buick
eddie jones waz her lickin stick
but i knew how to dance
it got soo hot
vincent ramos puked all in the punch
& harly jumped all in tico’s face
cuz he was leavin for the navy in the mornin
hadda kick *** so we’d all remember how bad he waz
seems like sheila & marguerite waz fraid
to get their hair turnin back
so they laid up against the wall
lookin almost sexy
didnt wanna sweat
but me & my fellas
we waz dancin
since 1963 i’d won all kinda contests
wid the cousins at the POLICE ATHLETIC LEAGUE
DANCES
all mercer county knew
any kin to martin yates cd turn somersaults
fore smokey robinson cd get a woman excited
we danced
doin nasty ol tricks i’d been thinkin since may
cuz graduation nite had to be hot
& i waz the only virgin
so i hadda make like my hips waz inta some business
that way everybody thot whoever was gettin it
was a older man cdnt run the streets wit youngsters
martin slipped his leg round my thigh
the dells bumped "stay"
up & down-up & down the new carver homes
WE WAZ GROWN
WE WAZ FINALLY GROWN
ulinda alla sudden went crazy
went over to eddie cursin & carryin on
tearin his skin wid her nails
the cousins tried to talk sense to her
tried to hold her arms
lissin **** sammy went on
bobby whispered i shd go wit him
fore they go ta cuttin
fore the police arrived
we teetered silently thru the parkin lot
no un uhuh
we didn’t know nothin bout no party
bobby started lookin at me
yeah
he started looking at me real strange
like i waz a woman or somethin/
started talkin real soft
in the backseat of that ol buick
WOW

TRANSITION And although every black women has her own unique experience, they also are united by their color and gender in a world that too often marginalized their existence. The Lady in Brown makes a final plea for black women in America. Listen carefully for humanity unites us all.

CHARACTER: Lady in Brown

dark phrases of womanhood
of never havin been a girl
half-notes scattered
without rhythm/no tune
distraught laughter fallin
over a black girl’s shoulder
it’s funny/it’s hysterical
the melody-less-ness of her dance
don’t tell nobody don’t tell a soul
she’s dancin on beer cans & shingles
this must be the spook house
another song with no singers
lyrics/no voices
& interrupted solos
unseen performances
are we ghouls?
children of horror?
the joke?
don’t tell nobody don’t tell a soul
are we animals? have we gone crazy?
i can’t hear anythin
but maddening screams
& the soft strains of death
& you promised me
you promised me...
somebody/anybody
sing a black girl’s song
bring her out
to know herself
to know you
but sing her rhythms
carin/struggle/hard times
sing her song of life
she’s been dead so long
closed in silence so long
she doesn’t know the sound
of her own voice
her infinite beauty
she’s half-notes scattered
without rhythm/no tune
sing her sighs
sing the song of her possibilities
sing a righteous gospel
let her be born
let her be born
& handled warmly.
& this is for colored girls who have considered suicide
but moved to the ends of their own rainbows.
```

---

## IC-1793: From First Glance to Goodbye – A Collection

- Title: From First Glance to Goodbye – A Collection
- Author (byline): Sabrina Benaim
- Work: Depression and Other Magic Tricks
- Publisher: Button Poetry
- Publication date as stated: Aug 2017
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1203
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sabrina Benaim
Book: Depression and Other Magic Tricks
ISBN: 978-1943735204
Publisher: Button Poetry
Date (Month/Year): Aug 2017
```

### Introduction (context only: never use it for content warnings)

```text
Sabrina Benaim’s Depression and Other Magic Tricks feels like opening an old journal you thought you’d burned. Every page humming with the ghosts of those you once loved too much. She doesn’t just talk about loss, she makes the emotions pulse like a heartbeat, and she shows how memories, no matter how much we try to fold them away, keep finding their way back to us. The poems “it starts”, “unrequited in nine acts” and “how to fold a memory” take us from love’s first glance to its final good-bye.
```

### Performance text (classify this)

```text
with a spark that makes static electricity look like longing. i am spellbound by the smoke billowing from his Belmont

cigarette.
like i am staring at his Belmont cigarette sat
snug between his lips like i wish my name
would. he is so cool. he is like the king of ice cream

sandwiches. like i wish my tongue was a drawbridge to his castle. his heart is a stubborn pistachio. like i want to crack it

open.
i want to play his heartstrings like a harp,
or rip out his heartstrings & like braid them into a bracelet.
like decorate me. i want to wear him.

unrequited in nine acts (Pg 49-51)

the question hangs a hook through my pink cheek. how did you do that thing that you did to my heart?

because isn't the real tragedy how you found yourself in one another. how you took one brief look into the mirror of her, turned around, and walked away?

the girl's arms are empty, but her fists are filled with the laughter of ghosts. watch their fitful ridicule each time she cries over love less real than they are.

there are baseballs falling out of my mouth. each ball a name of a body i reached for in the dark to find myself. a parade of honest names slipped from the grip of my loose glove jaw. the love i want is a basketball. i had these thumping in the chest when it is my turn to step up to the plate. i do not swing, i do not swing.

her name is a wooden ship to try and force it into his glass bottle. heart would only break her.

a montage of all the times i wished you had taken my hand and then, when you didn't, and the moment passed a montage of all the places i wished myself far far away to: portland, barcelona, basically any place i have never seen your smile.

what is the name of a place that everyone can see is burning, but no one can feel the effects of the smoke or the heat of the flames except the place? and that place is not a place but a person and that person is the i in my poems. only it's my real-life body that aches, and isn't that love not being able to see the explosion even though you are the one holding the bomb and the bomb is also you?

the girls hair turns to forget-me-nots and time. her bones softened to willow branches, her skin flakes may believe.

her chest is now a cabinet of well stacked cigar boxes. caskets carrying memories she is slow turning to ash. in lieu of conversation she passes smoke. the girl collect seashells up turns them into bowls filled them with dried lavender and amethyst in hopes of luring someone new. still remembering is her favorite pastime. she cannot hold her heart up without trembling, so she hides it away in bottomless midnight's, which are her grief, but are also her lust. the girl is now a girl who is also a whale full of unoccupied space and it's tragic how she displaces her emptiness with loneliness. how she wants and wants and wants, and needs to know why why the boy might want to live so far away from her now, when his house is just a couple blocks south of ten minutes, and all that space lays still loud as a snails cry. wouldn't i know about crawling up inside oneself? wouldn't i know about a body full of waiting and a floor clean as a plate in a cupboard holding nine other plates on top of it? how it's also unbearable... holding love. how it makes the girl feel helpless this period of heavy pockets of change her heart is unwilling to make?

did you hear me? i said i love you. i said i still love you. Still. . . you.

how to fold a memory (Pg 32-34) our brains remember the infliction of pain, be it physical, psychological, or emotional. we remember this hurt as means to avoid it in the future.

let’s start at the beginning.
i remember the shape of my hand held while in yours,
like origami prayer, or flower petals returning home.
i remember the rose petals falling from your fingers,
leading from the doorway to the bedroom like a
trail of breadcrumbs, or drops of blood.
the scent of cinnamon, how you would sprinkle in into my
coffee
like fresh ground snowflakes.
i can't cinnamon in my coffee
without getting hungry for your laughter.
i am hungry for your laughter, but my mouth tastes like the
slow
dissolve of the last i love you that refused to leave it.
i remember the river, how we danced to the sound of it
rushing,
how you hummed radiohead in harmony.
that song haunts my house of cards, i wish it would
collapse.
i wish i could forget how i got here,
how did i get here? i was carried in the teeth
of your charm, or i walked.
i marched. i was a turning cheek parade.
i wasn't paying attention to the highlighted route,
or there was no map, i got lost.

with every journey back into our past, it becomes harder

to find our way there.

our brains are constantly rerouting the paths, rewriting

what we remember.

let's go to the end -
it was by little sugar creek, in the warm kentucky breeze,
we stood off unfolding in silence.
in silence, it's hard o tell what the other person
is thinking without looking them in the eyes.

you would not look me in the eyes. so, by little sugar creek, i let the warm breeze reach you in place of my origami hands.

ever since, i have been practicing forgetting.
i've kissed the sky more times than i ever kissed you.
i inhale purple haze in an attempt to smoke out the
correlation
between you and the scent of cinnamon.
i drink as if i am trying to save the world from drowning.
to get my memories so drunk,
they might forget themselves by morning.
but the trauma of daydreaming.
the curse of muscle memory; my body keeps your secrets.

how do i teach my mouth to shake out the reflection of your etch-a-sketch a smile? my wrist, to forget the swoops and arcs of your name? my ears, to hear songs without the ghost of you inside of them?

worse, i cannot tell in these spasms of remembering, if the past tense keeps slipping in to my present, or if my present keeps slipping into the past. still, my body wears your fingerprints like a home address. i lose memories like baby teeth, but you are a stubborn molar, refusing to leave.

we cannot control what we remember,

but we can control how we remember.

i shake cinnamon into my coffee, & i don't think of you.
i write your name over and over so that it no longer has any
meaning.
i fold memories of you, craft them paper wings,
in hopes one day they might drift into amnesia,
& you might leave me,
without a trace.
```

---

## IC-1794: Generations and Do the Math

- Title: Generations and Do the Math
- Author (byline): Meliza Banales
- Work: Word Warriors
- Publisher: Seal Press
- Publication date as stated: Oct 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1039
- Already set (do not supply): none

### Source block (context only)

```text
Author: Meliza Baneles
Book: Word Warriors
ISBN: 978-1580052214
Publisher: Seal Press
Date (Month/Year): Oct 2007
```

### Introduction (context only: never use it for content warnings)

```text
Meliza Banalez, a Latina slam poet explains: “When the word "diversity" is brought up in Latino circles, it's often a dirty word; in the U.S., it has a history of dismissing us as people or chalking up our collective differences as "other" or "not normal," "normal," of course, being white. For example, I learned growing up, and especially in college, that "diversity" was often seen by most people of color as "teaching the white, normal people to politely deal with the not-so-normal people of color."

In her poems Generations and Do the Math, she graphically depicts what it has meant for her to grow up in the US in a family that struggled to maintain an image that they weren't as poor or as brown or as migrant as they seemed.
```

### Performance text (classify this)

```text
Generations
Before men and women were going on strike,
standing on the frontlines with Cesar Chavez screaming,
"Si se puede!"
Yes We Can
my great-grandfather was starting his own revolution,
teaching himself to read and write by rummaging

through schoolyard trashcans for used spelling books and old newspapers. Great-Grandfather came over from Michoacan, Mexico,

to pick cotton in California.
He even helped build the Kansas City Railroad
but ended up being too Mexican
to ride the trains that flew across the tracks of his

hard labor.

And who would have thought My father, little brown hands picking grapes in the

Fresno heat would be the first in our family to graduate high school and end up building satellites for NASA.

And still
you, Mr. Landowner,
can sit
the owner of lives
and tell me
that we are replaceable.
That somebody's gotta go out there and pick that fruit
because there is a cake that your mother is baking
that needs the perfect sized strawberries.

That we don't deserve more than a fifteen-minute break

a day because
money doesn't grow on trees,
money
doesn't grow
on trees.

Well neither does blood. Neither do brown hands. Neither does strength, neither does courage, neither do

weaknesses.

You ask me, the third generation of the brown blood gone white if I am ashamed of this heritage and I can tell you

Senor,
I don't hear shame calling me in my sleep.
I don't hear shame in 3 AM phone calls to my father,
"Papi, I'm working three jobs and I just can't take it

anymore." "Papi I get down on my knees every day not to pray to

God but to clean up after people's shit, and I just can't take

it anymore."
"Papi, I'm not gonna make my rent again next month
and I am livin' just enough for the city,
and I just can't take it anymore."

I don't hear shame when my father tells me, "Mija, haven't you learned by now that there are fields

of soldados,
soldiers swimming through your veins."
"Mija, there are fields of reasons
why the universe only gives you as much as you can

carry." "Mija, there are fields of things that your heart already

knows."
And this I know:
I have crawled across the backs of men and women
just so I could climb back into the womb of a mother

country
so that I could be reborn and say to you,
You do not plant these seeds.
You do not own these roots.
Your government does not birth this fruit.

So don't tell me how I don't understand the taste of the sweetest red

grapes
on a sunny August morning because trust me
They are filled
with the blood and sweat of three generations of Aztec

warriors. And I've come to know what the truth tastes like.

Do the Math The equation goes something like this: one white mother plus one brown father divided by two

different worlds equals a daughter. Give or take a decimal the American dream turns out to

be: two half-white children, two full-brown children, one small house in LA, four jobs divided by two high school educated parents The quality of life is high though the means is low.

The numbers vary from memory to memory. Like three. Three times a week I clean houses in rich neighborhoods

to make my way. Folding sheets is difficult. Every house has one rich

white lady with two dozen sheets times four beds which equals ten ways to fold the

sheets so that they're perfect.

Learning to fold sheets at least three to six ways means I can clean three to six houses a week which equals rent, tortillas, and lettuce for the month.

Going into one. One night a week I go-go dance in a cage in a Hollywood

nightclub. Ten dollars an hour plus tips. I'm only eighteen back then and already I know the

equation for lust: One bare ass in face gets a twenty, one crotch-drop

earns a fifty, one tongue licking cage bars while slowly gyrating hips equals I am the first in my family to go to college.

Then there's five. Five times a day I prayed through my seven-year-old

body that my father would lose his Spanish accent. I was convinced that if he did he could get a better job

and we
wouldn't be poor anymore.
I was convinced he just wasn't trying hard enough to say
"signals" instead of "singles" or "video" instead of

"bideo."

Five times a day I sent my other prayers, my secret

prayers that I was thankful for looking the most white in a

family of coffee-colored children. How I prayed that my brown blood wouldn't seep

through my white skin
so that I could
learn English, get an education
make my parents proud of half-white, half-brown

accomplishment.

Five times a day times seven days a week plus two small

hands clenched together in fear and ignorance equals a lifetime of trying to make halves a whole.

You see, it's all in the numbers.

These numbers that haunt my dreams, make my past into

single digits which have no common denominator.

Just once I'd like to write an equation for all the things

I could never write about.

For the three times my father took off work from three

different jobs to see me in the school play. For the first and last time my sister told her abusive

ex-husband that she didn't need
him anymore
and meant it.
For the hundreds of times I saw my parents laugh
until the tears rolled down their cheeks,
even in a neighborhood of drugs and gangs.

For that one moment, I did see my father cry when I, the first in my family, received my college

degree.

I'm writing a formula for all the numbers that have

fallen on me.

Fifteen sunrises in three different states, eight million breaths in one kiss, 185 poems in eight years –

I am writing an equation. Using the universal language of numbers to describe ten

thousand ways that something can mean everything.

It's just all in how you do the math.
```

---

## IC-1795: Godhuli: The Hour of Seeing (A Collection)

- Title: Godhuli: The Hour of Seeing (A Collection)
- Author (byline): Chitra Banerjee Divakaruni
- Work: Black Candle: Poems about Women from India, Pakistan and Bangladesh
- Publisher: Calyx Books
- Publication date as stated: Jan 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1243
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chitra Banerjee Divakaruni
Book: Black Candle: Poems about Women from India,
Pakistan and Bangladesh
ISBN: 978-0934971751
Publisher: Calyx Books
Date (Month/Year): Jan 2000
```

### Introduction (context only: never use it for content warnings)

```text
These poems pull back the curtain on the traditional South Asian wedding to show the terrifying risks women often face in arranged marriages. How a system built on family honor and "dowry gold" can quickly turn a woman into a prisoner or a victim. It is a chilling progression: a young bride is handed over to a stranger with "opaque eyes," another’s value is literally weighed on a scale by her in-laws, her life bartered for social standing. And the third a prisoner in her own home, required to produce only a male heir. It is time for . . .

Godhuli: The Hour of Seeing – A Collection of poems by Chitra Banerjee Divakaruni
```

### Performance text (classify this)

```text
The Arranged Marriage (Pgs 14-15)
The night is airless-still, as
before a storm. Behind the wedding drums,
cries of jackals from the burning grounds.
The canopy gleams, color
of long life, many children.
Color of bride-blood. At the entrance
the women have painted the sign
of Laxmi, goddess of wealth, have put up
a blackened pot to ward off
the witch who lives beyond
the sheora forest and eats
young flesh.

Guests from three villages
jostle, make marriage jokes. A long
conch blast for the groom’s party,
men in dhotis white as ice. Someone runs to them
with water of rose, silvered betel leaves,
piled garlands from which rise
the acrid smell of marigolds.
The priests confer, arrange wood and incense
for the wedding fire. The chants begin.
Through smoke, the stars
are red pinpricks, the women’s voices
almost a wailing. Uncles and Brothers
carry in the bride, her face hidden
under an edge of scarlet silk, her trembling
under the wedding jewels.

The groom’s father
produces his scales and in clenched silence
the dowry gold is weighed. But he smiles
and all is well again. Now it is godhuli,
the time of the auspicious seeing.
Time for you, bride of sixteen,
mother, to raise the tear-stained face
that I will learn so well,
to look for the first time into
your husband’s opaque eyes.

Burning Bride (Pgs 57-60)
For the victims of dowry deaths in India
1. In the beginning was fire,
the color of sunrise
through coconut palms,
the color of my wedding sari.
Festive with smell of incense,
the flames flicked playful tongues.
Stumbling to match his unfamiliar gait,
I walked with him
seven times round the fire
while wedding guests threw flowers.

The whisper of fire, secret, enigmatic, I hear it under the brahmins’ rising chants, under the shehnai music flooding our bed like the molten moon. Fire, too, his eyes, his touch. His breath a whispered fire. And my sari spilled on the floor that volcano night redgashed, a tide of lava.

2. The day after the wedding
they took off my jewelry, weighed it.
When it came up short
of my father’s promise,
they looked at me.
Their eyes glowed pale as coals.

I wrote my father, but I knew already.
The last cow sold,
two sisters left to marry off.
There was no more for my dowry.
They got rid of the servant
who broke coals for the kitchen,
put me to work in that room, windowless,
where slabs lay piled
black on black dust.
Fire in the chest,
each indrawn breath a stabbing flame
as I strained to swing the hammer.

I wrote once more,
again knowing the reply.
If I left my husband’s home
the family name would be black,
my sisters left unwed.
I did not write again.
Fire deep in the empty belly,
lying on the dark bedroom floor,
touching my wet face,
not knowing blood from tears.

Had I died,
he could have married again,
a good wife,
one with a dowry.
But though they prayed,
though we all prayed,
I did not die.

3. I saw them bring the kerosene last night
under the thin crescent
of the failing moon.
They hid the tins
in the women’s house, where we spend
the defiled days each month.
They will do it next week
when it is my time,
the dark time of my blood.

I know what happens.
Last month I saw the body
of the night-watchman’s new wife.
They gave her a grand funeral,
a hundred guests.
But under the piled jasmines,
the golden sandalpaste,
was the indecent gash of pink,
the skin crisped away,
the smell of charred flesh,
unmistakable,
lodging deep in my belly.
I smell it as I wait.

Did they hold her down, struggling,
oozing the dark oily stain?
Did they silence her cries,
rough hand clamping across lips,
so the only sounds
were the sharp rasp of a match
and the quick blue hiss of fire
leaping in a night turned sudden red.

Sudha’s Story (Pgs 45-49) 1. He saw her first at the Festival. Flaming in scarlet silk she danced the Tillana unfaltering. The tabla played faster. Her braid whipped the air, black lightning, as she spun. Her feet were a blur of light. The people could not stop clapping.

He sent word through the matchmaker. Her parents were delighted. An officer at Delhi, and she a small-town girl, not even out of college. They sold the village home for a grand wedding. All the relatives came.

In the bride-bedroom
he asked her to dance.
As she swayed, arms raised,
In the love dance of Radha,
he turned her to him, wound the braid
around her throat.
From now on, you dance
only for me.
His lips kissed shut
the surprise in her eyes.

2. On the honeymoon at the Taj Mahal,
he laughed at her delight
in the translucent tombs
and pulled her close. But at night
his fingers tightened on her naked shoulders.

I saw how you looked at the guide, how you smiled. Next day he took her home.

He told her to put away her textbooks.
He knew what went on in college.
All those young women
flirting with men.
Not my wife.

Each morning, leaving for work,
he locked her in. All day
she walked the large house, room
by room by room. Leaned her head
against the windowbars to cool the burn.
Evenings, he brought gifts --
a new sari, perfume --
made her wear them to bed.

Her parents’ letters were full of praise. A promotion already, such a generous husband, all the relatives are dying of envy. She crushed them in her fists, did not reply.

Nights she dreamed of escape, body
swinging limp-necked on a rope
from a huge hook in the ceiling.
when she woke, the ceiling
stretched above her, endless,
always empty.

3. When he found her throwing up,
mornings, he laughed and crushed
her to his chest. Now my mark’s
on you, in you, bearing my name.
He filled her nightstand with vitamins,
took her to the best doctors.
Let her sleep alone. Her belly
rounded, pulsed in a silver haze.
Days and nights spun away.
Until he flung the test results
in her face. This isn’t
my child. No one in my family
fathered girl-children, ever. Tell me who
you slept with, who.
He left her on the floor.

The crack of the door-bolt ricocheted a long time in her skull.

That night the tonic tasted strange.
She woke retching,
doubled with cramps. Pain
jabbed at her belly
like broken Glass. Poison,
she thought, then felt the blood,
its thin sticky flow.
He watched from the door, eyes
like dead moons. Next day
he sent her parents
a regret telegram.

When his sleeping breath rasped
the dark, she stole to his bedroom door,
bolted it from outside. Poured
the cooking kerosene.
From her wedding-trunk, she shook out
her dance costume: gold anklets,
red silk. The flames took
the curtains and chairs,
moved their mouths along the carpet.
She began the Nataraja,
dance for the world’s burning end.

My right foot balances
on a wheel of fire.
I swing the left across
the trembling air.
My palm holds up the sky,
which will fall
when I turn my wrist. The drums
die away. In the black quiet,
only the flames.
blood streaked, they whisper to me
in my daughter’s voice.
```

---

## IC-1796: Gravity and Testimony

- Title: Gravity and Testimony
- Author (byline): Maura O’Connor
- Work: The Outlaw Bible of American Poetry
- Publisher: Thunder’s Mouth Press
- Publication date as stated: Nov 1999
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 954
- Already set (do not supply): none

### Source block (context only)

```text
Author: Maura O’Connor
Book: The Outlaw Bible of American Poetry
ISBN: 978-1560252276
Publisher: Thunder’s Mouth Press
Date (Month/Year): Nov 1999
```

### Introduction (context only: never use it for content warnings)

```text
We turn on the radio, we flip on the television, but when the song is over, or the movie ends our emptiness returns. We grow up in the paradigm that life consists of what we observe going on around us, on the surface of the earth. However, this Surface Life soon becomes mundane, so we seek to fill it up with things and activities. Yet this too becomes insignificant. Eventually we feel the emptiness of our lives and see the hollowness of our existence. So we begin to search for meaning . . . the following two poems, Gravity and Testimony give us insight into Maura O’Connor’s search for meaning.
```

### Performance text (classify this)

```text
Gravity

Today I am fragile
pale
twitching
insane and full of purpose.

I'm thinking we tend our illnesses
as if they are our children:
fevered
screaming
demanding attention and twenty dollar bills, hours we
could have spent
with the television on.

Faith is a series of calculations made by an idiot savant. I'm in love. I'm alone in this city of painted boxes stacked like alphabet blocks spelling nothing.

There are things I know:
trees don't sing
birds don't sprout leaves
the sky never turns to wine
roses bloom because that's what roses do, whether we
write poems for them
or not.

I concentrate on small things:
ivy threaded through chain link,
giveaway kittens huddled in a soggy cardboard box, a fat
man blowing harmonica
through a beard of rusty wires
brown birds chattering furiously on power lines.

I try not to think about
lung cancer, AIDS,
the chemicals in the rain;
things I can't imagine any more than a color I've never
seen

My heart is graffiti on the side of a subway train, a shadow on the wall made by a child. Nothing has been fair since my first skinned knee I believe death must be.

I cling to love as if it were an answer. I go on buying eggs and bread, boots and corsets, knowing I'll burn out before the sun.

I'm thinking of
the days I tried to stay awake
while the billboards and T.V. ads
for condoms, microwave brownies, and dietetic jello
lulled me to sleep.

A brown-eyed girl once told me a secret that should have blown this city into a mass of unconnected atoms Our sewage is piped to the sea. Beggars in the street are hated for having the nerve to die in public.

Charity requires paperwork, Relief requires medication

as if we were the afterthoughts of institutions greater than our rage.

Gravity chains us to the asphalt with such grace we think it is kind.

We all go on buying lottery tickets, Diet Coke and
toothpaste
as if the sky over our heads
were the roof of a gilded cage.

We provide evidence that we were here: initials cut into cracked vinyl bus seats, into trees growing from squares in concrete, a name left on a stone, an office building, a flower, a disease, a museum a child.

Tonight the stars glitter like rhinestones on a black suede glove.

In the coffin my room has become,
I talk to God
about the infrequency of rain
about people who can't see the current of gentleness
running under the pale crust of my skin.

I tell him under
the jackhammer crack, the diesel truck rumble, even the
clicking sound traffic lights make switching from yellow
to red,
there is a silence
swallowing
every song,
conversation,
every whisper made beside graves.

I tell him I can't fill it with dark wine, blue pills, a pink candle lit at the altar

God doesn't answer. God doesn't know our names.

He's only the architect designing the places we occupy
like high rise offices or ant hills
I know this
the way I know
sunrise and sunset
are caused by the endless turning of the Earth.

Testimony

These days
I cover my face with bottled skin and scented creams
stain my lips the color of rose juice wear black
my eyes deepen

The man who once called me that girl in the white shirt

He carried me home in a magician's casket cut me in two I came out whole

I'm a kindness to climb into a Dresden doll found in the basement of a burnt house

These days
I buy the book with the ugliest cover comb the thick
orange hair
of the innocent child
I never was

While my heroes are knocked down like pinatas while we wear surgical gloves to the laying on of hands

I've folded suicide in four
laid it on a bare white shelf
someday it may gather dust
I might toss it away like an old dishrag I'm young
green as bread mold

I'm seeking witness

I want the testimony of Hitler Stalin the shadows on the bricks of Nagasaki

These days the newspapers serve a menu of clay pigeons bring your own bullets

I want to ban the colors of the television the perfect
thighs
and plastic wishes
I want to burn Jesus leaflets
and wear his sandals

I'm taking it all off in the bars of my rib cage

While the politicians find work for each idle child while two terminal patients place bets on the existence of God

These days
I show the years when I didn't want to live in the gray
spokes of my iris
I'm coming apart like a ten-cent toy

I carry my head under my arm like a rag doll

I want to sleep in the ruin of last night's makeup I want ancient recipes over instant rice

I want to find the hummingbird graveyard I want to fill my mouth with black beetles and walk the edge of Eden

I need a new commandment

I will collect single bars of old songs I will weep a page of black ink I will be an unprotected witness

My country serves three-day notice
to the starving
my country's hands are tattooed
on the belly of a battered child
my country sleeps in the snow of the television after its
anthem is played

Let's burn the country and keep the flag

This night is falling in pieces this moon is cream on a raisin sky

I will evolve thick skin and filter I will plan my next breath

I will watch the four riders foam their horses into glue

It isn't over yet
```

---

## IC-1797: Grito de Vieques and Commonwealth

- Title: Grito de Vieques and Commonwealth
- Author (byline): Aya de Leon and Tato Laviera
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 735
- Already set (do not supply): none

### Source block (context only)

```text
Author: Aya de Leon
Book: Word Warriors
ISBN: 978-1580052214
Publisher: Seal Press
Date (Month/Year): Oct 2007
Author: Tato Laviera
Book: AmeRican
ISBN: 978-1558853959
Publisher: Arte Publico Pr
Date (Month/Year): March 2003
```

### Introduction (context only: never use it for content warnings)

```text
Vieques, a small island that is part of Puerto Rico, has been under U.S. Military occupation since 1941. During that time, the island and its occupants have been subjected to continuous U.S. military exercises with live ammunition, including radioactive material. In April 1999, two bombs missed their target and killed David Sanes-Rodriguez, a civilian security guard. This incident touched off the most recent wave of resistance in Vieques and throughout the Puerto Rican community at large. Grito de Vieques or “My Name is Vieques” by Aya de Leon
```

### Performance text (classify this)

```text
Grito de Vieques

My name is Vieques.
I am a Puerto Rican girl.
My stepfather is the United States.
He comes into my room at night to do his business.

My name is Vieques.
I used to dream that Spain, my real father, would come
back and rescue me.
But he's gone for good.
I have only the faint and echoing voices
of Africana and Taina ancestors telling me that
I can survive this.

My name is Vieques.
When my body started to change,
my stepfather dressed me in a clingy, itchy dress.
"Smile," he told me. "Smile at the nice foreign military
man," and pushed me toward him.
The military man was not nice.
His skin was pasty. His breath smelled.
I couldn't understand his language.
He came into my room and did his business.

My name is Vieques. Sometimes my stepfather sells me to whole groups. He calls them allied forces.

I fought back the best I could with chains and live bodies and fishing boats. It happened anyway.

My name is Vieques.
I am still fighting back.
I am bigger and stronger now.
I have put a church, an encampment,
a struggle up at my bedroom door.
My stepfather can't get in.
He has not been able to do his business for months now,
longer than I ever dreamed.

My name is Vieques. Without the shock of constant bombardment, the numbness is subsiding.

I look at my body and see the devastation.
Lagoons, like self-esteem, have dried up to nothingness.
My womb is wilting with radiation
from illegally used uranium ammunition.

Where my skin was once lush and soft, I am scarred. Old tanks, like cigarette burns, dot my flesh. Unexploded bombs, like memories, may detonate in the future when chosen lovers touch me in the wrong spot or without warning.

My name is Vieques.
The numbness is subsiding.
Tender shoots of grass push up toward the sky.
A lizard sneaks back to sun itself on a chunk of shrapnel.
A butterfly alights on a rusted-out jet.
Fish slowly make their way back toward my shores,
no longer reverberating with shockwaves of violation.
My name is Vieques.
This is my body.
It may be worth eighty million dollars a year to you,
Yanqui,
but it is priceless to me.

My door is barred.
I have burned the clingy, itchy dress.
The encampment grows stronger.
The lizards, the grass, the fish, the butterflies stand
with me.
I'll never be the same,
but I'll never be yours again to do your dirty business.

My name is Vieques and I will be free.

TRANSITION Ever since the United States invaded Puerto Rico in 1898 and then was handed the island by Spain as part of the settlement for the Spanish-American War, the island’s people — American citizens since 1917 — have been continuously put in situations where they are simultaneously auditioning for statehood, agitating for independence, and making the very best of living in limbo. Tato Laviera calls this limbo the “commonwealth stage of life.” Commonwealth by Tato Laviera.

Commonwealth
no, not yet, no, not yet
i will not proclaim myself,
a total child of any land,
i’m still in the commonwealth
stage of my life, wondering
what to decide, what to conclude,
what to declare myself.
i’m still in the commonwealth
stage of my life, not knowing
which ideology to select.
i’m still in the commonwealth
stage of my life, all of us
caught in a web of suspension,
light-years away from the indians’
peaceful enclaves.
i’m still in the commonwealth
stage of my life, observing the many integrated
experiences
we took everything
and became everybody else.
i’m still in the commonwealth
stage of my life, but there’s
not enough hatred in our hearts
to kill each other or to draw
blood for too long, ours
is a mental search
carved through a mainstream of options
but yet, somewhere
in the commonwealth, we all yearn
to feel our strengths,
to show our ultimate,
to find common wealth among us,
to close our eyes,
to find the total silence, silencio, silence,
to find ... not one thing that unites us,
even in silence we are still
in the commonwealth stage of our lives,
so let’s touch hands, friends and foes,
and stay together to hear each other’s
sounds just for one moment, let’s stay
tucked together, and maybe then, less
options, maybe then, hope.
```

---

## IC-1798: Guenevere and Helen of Troy

- Title: Guenevere and Helen of Troy
- Author (byline): Sara Teasdale
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1209
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sara Teasdale
Book: Modern Arthurian Literature (Ed Alan Lupack)
ISBN: 978-0815308430
Publisher: Routledge
Date (Month/Year): May 1992
Author: Sara Teasdale
Book: Love Songs
ISBN: 978-1417923489
Publisher: Kessinger Publishing Co
Date (Month/Year): Dec 2004
```

### Introduction (context only: never use it for content warnings)

```text
Consider . . . . The forbidden lovers of Arthurian legend, Queen Guenevere and Sir Lancelot, could not ignore their feelings for each other. Driven by desire, they betrayed King Arthur and became lovers, causing the fall of Camelot.

Or . . . . . One of the most well known tales of ancient Greek mythology -- Helen of Troy. Many believe that her spellbinding beauty played a key role in one of the most famous battles of all time – the Trojan War. She symbolizes the Greeks’ view that attractiveness, although a superficial aspect of someone, is a strong force which can bring with it the power to corrupt.

Beauty and desire two concepts highly valued by people throughout history. Sara Teasdale in her poems Guenevere and Helen of Troy explores the perceptions of each of these women – did they feel responsibility for the terrible conflicts initiated in their names? Listen carefully as Guenevere speaks . . . .
```

### Performance text (classify this)

```text
Guenevere
I was a queen, and I have lost my crown;
A wife, and I have broken all my vows;
A lover, and I ruined him I loved: --
There is no other havoc left to do.
A little month ago I was a queen,
And mothers held their babies up to see
When I came riding out of Camelot.
The women smiled, and all the world smiled too.
And now, what woman's eyes would smile on me?
I still am beautiful, and yet what child
Would think of me as some high, heaven-sent thing,
An angel, clad in gold and miniver?
The world would run from me, and yet am I
No different from the queen they used to love.
If water, flowing silver over stones,
Is forded, and beneath the horses' feet
Grows turbid suddenly, it clears again,
And men will drink it with no thought of harm.
Yet I am branded for a single fault.

I was the flower amid a toiling world, Where people smiled to see one happy thing, And they were proud and glad to raise me high; They only asked that I should be right fair, A little kind, and gowned wondrously, And surely it were little praise to me If I had pleased them well throughout my life.

I was a queen, the daughter of a king.
The crown was never heavy on my head,
It was my right, and was a part of me.
The women thought me proud, the men were kind,
And bowed right gallantly to kiss my hand,
And watched me as I passed them calmly by,
Along the halls I shall not tread again.
What if, to-night, I should revisit them?
The warders at the gates, the kitchen-maids,
The very beggars would stand off from me,
And I, their queen, would climb the stairs alone,
Pass through the banquet-hall, a loathed thing,
And seek my chambers for a hiding-place,
And I should find them but a sepulchre,
The very rushes rotted on the floors,
The fire in ashes on the freezing hearth.
I was a queen, and he who loved me best
Made me a woman for a night and day,
And now I go unqueened forevermore.
A queen should never dream on summer eves,
When hovering spells are heavy in the dusk: --
I think no night was ever quite so still,
So smoothly lit with red along the west,
So deeply hushed with quiet through and through.
And strangely clear, and deeply dyed with light,
The trees stood straight against a paling sky,
With Venus burning lamp-like in the west.

I walked alone amid a thousand flowers,
That drooped their heads and drowsed beneath the dew,
And all my thoughts were quieted to sleep.
Behind me, on the walk, I heard a step --
I did not know my heart could tell his tread,
I did not know I loved him till that hour.

Within my breast I felt a wild, sick pain, The garden reeled a little, I was weak, And quick he came behind me, caught my arms, That ached beneath his touch; and then I swayed, My head fell backward and I saw his face.

All this grows bitter that was once so sweet, And many mouths must drain the dregs of it. But none will pity me, nor pity him Whom Love so lashed, and with such cruel thongs.

TRANSITION And from a similar situation separated by time and country . . . . Helen of Troy . . .

Helen of Troy
Wild flight on flight against the fading dawn
The flames' red wings soar upward duskily.
This is the funeral pyre and Troy is dead
That sparkled so the day I saw it first,
And darkened slowly after. I am she
Who loves all beauty -- yet I wither it.
Why have the high gods made me wreak their wrath --
Forever since my maidenhood to sow
Sorrow and blood about me? Lo, they keep
Their bitter care above me even now.
It was the gods who led me to this lair,
That tho' the burning winds should make me weak,
They should not snatch the life from out my lips.
Olympus let the other women die;
They shall be quiet when the day is done
And have no care to-morrow. Yet for me
There is no rest. The gods are not so kind
To her made half immortal like themselves.
It is to you I owe the cruel gift,
Leda, my mother, and the Swan, my sire,
To you the beauty and to you the bale;
For never woman born of man and maid
Had wrought such havoc on the earth as I,
Or troubled heaven with a sea of flame
That climbed to touch the silent whirling stars
And blotted out their brightness ere the dawn.
Have I not made the world to weep enough?
Give death to me. Yet life is more than death;
How could I leave the sound of singing winds,
The strong sweet scent that breathes from off the sea,
Or shut my eyes forever to the spring?
I will not give the grave my hands to hold,
My shining hair to light oblivion.
Have those who wander through the ways of death,
The still wan fields Elysian, any love
To lift their breasts with longing, any lips
To thirst against the quiver of a kiss?

Lo, I shall live to conquer Greece again,
To make the people love, who hate me now.
My dreams are over, I have ceased to cry
Against the fate that made men love my mouth
And left their spirits all too deaf to hear
The little songs that echoed through my soul.
I have no anger now. The dreams are done;
Yet since the Greeks and Trojans would not see
Aught but my body's fairness, till the end,
In all the islands set in all the seas,
And all the lands that lie beneath the sun,
Till light turn darkness, and till time shall sleep,
Men's lives shall waste with longing after me,
For I shall be the sum of their desire,
The whole of beauty, never seen again.
And they shall stretch their arms and starting, wake
With "Helen!" on their lips, and in their eyes
The vision of me. Always I shall be
Limned on the darkness like a shaft of light
That glimmers and is gone. They shall behold
Each one his dream that fashions me anew; --
With hair like lakes that glint beneath the stars
Dark as sweet midnight, or with hair aglow
Like burnished gold that still retains the fire.
Yea, I shall haunt until the dusk of time
The heavy eyelids filled with fleeting dreams.

I wait for one who comes with sword to slay -- The king I wronged who searches for me now; And yet he shall not slay me. I shall stand With lifted head and look within his eyes, Baring my breast to him and to the sun. He shall not have the power to stain with blood That whiteness -- for the thirsty sword shall fall And he shall cry and catch me in his arms, Bearing me back to Sparta on his breast. Lo, I shall live to conquer Greece again!
```

---

## IC-1799: Hands: For Mothers Day

- Title: Hands: For Mothers Day
- Author (byline): Nikki Giovanni
- Work: The Selected Poems of Nikki Giovanni
- Publisher: Morrow, William and Co
- Publication date as stated: Jan 1996
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 765
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nikki Giovanni
Book: The Selected Poems of Nikki Giovanni
ISBN: 978-0688140472
Publisher: Morrow, William and Co
Date (Month/Year): Jan 1996
```

### Introduction (context only: never use it for content warnings)

```text
Perhaps you have heard the story of the young boy who always made his mother wear gloves out in public because he was embarrassed at the unsightly deformity of her hands. During a presentation by the teachers and parents at his school, however, he made a discovery that would forever change his perspective.

His mother shared the story that when the young boy was a baby, the family house caught fire in the middle of the night. In her effort to save her baby boy, the mother’s hands were badly burned as she fought the flames to rescue him from his crib. The young boy approached his mother with tears streaming down his cheeks, and he slowly removed the gloves from her hands. As he stroked her deformed hands, he said to her, “these scars are symbols of your love for me, and I am so proud of them. To me, they are the most beautiful hands in the world.”

Hands: For Mothers Day by Nikki Giovanni
```

### Performance text (classify this)

```text
I think hands must be very important . . . Hands: plait hair . . . knead bread . . . spank bottoms . . . wring in anguish . . . shake the air in exasperation . . . wipe tears, sweat, and pain from faces . . . are at the end of arm which hold . . . Yes hands . . . Let’s start with the hands . . .

My grandmother washed on Mondays . . . every Monday . . . If you were a visiting grandchild or a resident daughter . . . every Monday morning at 6:00 a.m. . . . mostly in the dark . . . frequently in the cold . . . certainly alone . . . you heard her on the back porch starting to hum . . . as Black Christian ladies are prone to do . . . at threshold . . . some plea to higher beings for forgiveness and the power to forgive . . .

I saw a photograph once of the mother of Emmett Till . . . a slight, brown woman with pill box hat . . . white gloves . . . eyes dark beyond pain . . . incomprehensibly looking at a world that never intended to see her son be a man . . . That same look is created each year . . . without the hat and gloves, for mothers seals are not chic . . . at the Arctic Circle . . . That same look is in vogue in Atlanta, Cincinatte, Buffalo . . . for much the same reason. . . During one brief moment, for one passing wrinkle in time, Nancy Reagan wore that look . . . sharing a bond, as yet unconsummated . . . with Betty Shabazz, Jacqueline Kennedy, Coetta King, Ethel Kennedy . . . The wives and mothers are not so radically different . . . It is the hands of the women which massage the balm . . . the ointments . . . the lotions into the bodies for burial . . . It is our hands which: cover the eyes of small children . . . soothe the longing of the brothers . . . make the beds . . . set then tables . . . wipe away our own grief . . . to give comfort to those beyond comfort . . .

I yield from women whose hands are Black and rough . . . The women who produced me are in defiance of Porcelana and Jergens lotion . . . are ignorant of Madge’s need to soak their fingernails in Palmolive dishwashing liquid . . . My women look at cracked . . . jagged fingernails that will never be adequately disguised by Revlon’s new spring reds . . . We of the unacceptably strong take pride in the strength of our hands . . .

Some people think a quilt is a blanket stretched across a Lincoln bed . . . or from frames on a wall . . . a quaint museum piece to be purchased on Bloomingdale’s 30-day same-as-cash plan . . . Quilts are our mosaics . . . Michelle-Angelo’s contribution to beauty . . . We weave a quilt with dry, rough hands . . . Quilts are the way our lives are lived . . . We survive on patches . . . scraps . . . the leftovers from a materially richer culture . . . the throwaways from those with emotional options . . . We do the far more difficult job of taking that which nobody wants and not only loving it . . . not only seeint its worth . . . but making it lovable . . . and intrinsically worthwhile.

Through trite . . . it’s nonetheless true . . . that a little knowledge is a dangerous thing . . . Perhaps pitiful thing would be more accurate . . . through that too is not profound . . . . The more we experience the human drama . . . the more we are to understand . . . that whatever is not quite well about us will also not quite go away . . .

Sometimes . . . when it’s something like Mother’s Day . . . you really do wish you were smart enough to make the pain stop . . . to make the little hurts quit throbbing . . . to share with Star Trek’s Spock the ability to touch your fingertips to the temples and make all the dumb . . . ugly . . . sad things of this world ease from memory . . . It’s not at all that we fail to forgive others for the hurts we have received . . . we cannot forgive ourselves for the hurts we have meted . . . So . . . of course . . . we use our hands to push away rather than to pull closer . . .

We look . . . in vain . . . for an image of mothers . . . for an analogy for families . . . for a reason to continue . . . We live . . . mostly because we don’t know any better . . . as best we can . . . Some of us are lucky . . . we learn to like ourselves . . . to forgive ourselves . . . to care about others . . . Some of us . . . on special occasions . . . watch the ladies in the purple velvet house slippers with the long black dresses come in from Sunday worship and we realize man never stood up to catch and kill prey . . . . man never reared up on his hind legs to free his front parts to hold weapons . . . WOMAN stood to free her hands . . . to hold her young . . . to embrace her sons and lovers . . . WOMAN stood to applause and cheer a delicate mate who needs her approval . . . WOMAN stood to wipe the tears and sweat . . . to touch the eyes and lips . . . that woman stood to free the arms which hold the hands . . . which hold.
```

---

## IC-1800: Harriet

- Title: Harriet
- Author (byline): Elena Passarello
- Work: Animals Strike Curious Poses, Pgs 85-94
- Publisher: Sarabande Books
- Publication date as stated: Feb 2017
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: HARRIET, FITZROY, CHARLIE, DICK, TOM, JOHN, GEORGE, FLEAY, STEVE IRWIN
- Teaser before the introduction: Yes
- Spoken words (computed): 1223
- Already set (do not supply): none

### Source block (context only)

```text
Author: Elena Passarello
Book: Animals Strike Curious Poses, Pgs 85-94
ISBN: 978-1941411391
Publisher: Sarabande Books
Date (Month/Year): Feb 2017
```

### Introduction (context only: never use it for content warnings)

```text
With a face that everyone fell head over heels for, a pair of bright eyes that had seen more than we will ever know and the most affectionate and gentle nature, Harriet stole hearts every day. She passed away peacefully on June 23, 2006, leaving behind countless admirers and an impressive, unforgettable life. From an unrequited love affair with Charles Darwin himself to heartbreak at Steve “Crocodile Hunter” Irwin’s Australian Zoo, Harriet was 175 years old at the time of her death. She weighed 330 pounds and was roughly the size of a dinner table. This is her story, and what a story it is . . .

Harriet by Elena Passarello
```

### Performance text (classify this)

```text
Portray the character of Harriet with tortoise mannerisms.

HARRIET: (Pg 85) When the HMS Beagle drops her anchor in 1935, get under the biggest frond in sight as fast as you can. Dozens of hungry sailors will jump ship, spears in hand, many lancing their first turpin within minutes. Others will follow the highway of tracks to the higher points of the island, where hill-dwelling turpin grow longer, saltier necks. In a few hours, they’ll all trudge back to ship, hefting dozens of your kinds in makeshift stretchers of oars and canvas. Three men to every heavy shell.

Tuck yourself in, little girl. Be still. Don’t hiss. There’s not enough meat under your dinner-plate shell to merit the tedious chore of turpin gutting.

HARRIET: (Pg 85-94) And then, a set of lighter steps. A pair of clean pants, a slight cough: the “Ship Nauralist” . . . Charlie (Charles Darwin) He’ll clear away the brush, pick you up in his small, soft hands. “Tortise,” he’ll call you, not “turpin.” (mouth closed, taps tongue twice and hiss) How fancy.

He will name you “Harry,” but some part of him knows you’re all woman. His delicate touch, as he flips you and runs his fingers along your soft, salty underbelly. Delight in how he hand-feeds you pink flowers. Back in the cabin, he will sketch you by lamplight. He will coax your neck from the shell and tickle it, measure it, memorize it, muttering “Amazing.” Try to whisper back to him – Charlie.

You were a catch. Nothing he could find in Africa or the West Indies, and certainly not in England. When he eyes your unique shell, a wildness stirs in him.

As the sailors plow through the other tortoises on the Beagle – sometimes 3 adults every day – rest easy. They’ll slice each neck in one blow, gulping the gallons of fresh water that spill from each gullet. But remember Charlie’s promise to take you away from all this. Sure, he joins the crew in sipping your old neighbor at dinnertime, but he’s doing it to keep you safe, to not arouse suspicions. You’re not dinner; you’re different.

Captain FitzRoy thought he’d hired a seminarian-turned-science-man to prove the world made in seven days. A few nights with you, however, and Charlie’s become a charlatan. They fight, but Charlie leaves you out of it. Instead they talk finches:

FITZROY: The islands are as old as Genesis.

CHARLIE: No, these islands are young and as they multiply, the finches change their beaks to serve it.

FITZROY: Serve an island, not our God?

HARRIET: If we can adapt to an ever-changing island, who says we can’t adapt for love. Adaptations, after all, are nothing more than labor: fueled by chemistry, successful only when lauded by a mate. It’s always something love-born. For we were not born to mate and die. We were not born to duplicate the image God threw together long ago. We were born to surprise God as we catch up to the morphing rocks and malleable seas on our own volition.

You finally land in England a year later. Boxes of corpses – birds, plants, bugs, rocks – pass through his study. No tortoises. You were the only one he thought to keep, the remains of the others heaved overboard with the slop. But that fall, in the draftiest room of the British Museum, you’ll find yourself shivering on a table with three other girls your age. All from the Beagle, four secrets stashed away in the gentlemen’s cabins. Even godly Captain FitzRoy had a Galapagos on the sly.

DICK: (tucks her head into her shell and weeps) I’ve been out in the garden since October. He took a wife the week we docked. A wife!

TOM: At least he doesn’t have kids yet. His brats use me for pony rides.

HARRIET: John Gray, the museum’s Keeper of Zoology, declares your lot too young to assess scientifically.

JOHN: Sorry, Charlie. Maybe in thirty, forty years. But these finch specimens – yes!

HARRIET: Charlie turns away and faces the bird box on the opposite table. (to Charlie) Oh, God, wait for me, Charlie. I’ll grow faster. I know I can figure something out. (to audience) He’ll move you in with his doped-up brother and wed his nervous, pious cousin, devoting his days either to her or the finches. He takes her in a carriage and brand-new hat to the Zoological Society of London, but hides you in a hatbox and in his cheap “B Notbook” he wouldn’t dare be seen with in public. Instead of words like “marry,” “companion,” he write you words like “specimen.”

Soon wifey will banish you and the other mistresses to Whitehall where London’s gales freeze you into a state of perpetual hibernation. Tom dies. Surely somebody will see you’re sick and get you the hell out of there – away from her, from him, from that notebook that has changed him so.

GEORGE: (wheezing) You’re better off without him. Those scientific types are all the same – emotional incapable of seeing past their own needs. They’re only married to their work. Damn freak.

HARRIET: When George sleeps, you stare at the initials the whaler carved in her shell. Within a year, she’s dead. And all the talk is of Charlie – visitors, botanist, apprentices. His book, his finches, his revolution. And eventually his last words.

CHARLIE: I am not the least afraid to die.

HARRIET: (bitterly) Not, “my love” or even “my notebook” or -- God be merciful – “my tortoise.” Wickham, the new captain of the Beagle takes you to Australia’s Brisbane Botanic Gardens. So that’s it, babe. You’re forty years shy of middle age and it’s over. It’s 1893 and Dick, the ol’ girl from the Beagle is the only other tortoise left. Three floods in 13 days. Mines explode. Bridges collapse.

DICK: If this keeps up, they’ll start eating us again.

HARRIET: Around you, strange things in dirty pens: a muskrat with swim fins who lays leathery eggs in the mud (beaver), a huge dog that hops and keeps its pups in a furry pocket (kangaroo), a hissing dog with the teeth of a tiger (wolf). And in the center of it all, Master Fleay, another naturalist born a century after Charlie, and the first to give you a lady’s name.

FLEAY: (giving a tour) I’ve saved the best for last. Isn’t she a beyoot? Harriet is her name. Used to belong to Darwin, she did, back in the last century. But now she is mine, all mine. *****flash forward*****

HARRIET: A dry field with a fence. The sun is relentless; the women wear trousers and no hats. Many of them sport square, beetle-black faces with one shiny eye. (camera) When the eyes blink, it makes daytime lightning. A fully grown man in short pants, named Irwin, hops to either side of you, his hair stuck to his forehead in wet, blond drips.

STEVE IRWIN: (posing for pictures with Harriet) Crikey!

(a different pose) Crikey!

HARRIET: He holds a few poses for the crowd and their flashing eyeballs, hugging your neck, straddling you with outstretched arms and mouth open wide.

STEVE IRWIN:(singing) Happy birthday, dear Harry-ette!

HARRIET: At the edge of the pen, his long-haired wife grits her teeth. He skips over to the “Croco-seum” for an impromptu reptile freak-out. Watch him bound onto the stage, a baby croc in each hand, shaking them like maracas in the dusty breeze. Irwin tosses you a few pink flowers and the grimacing wife cuts a huge cake. She slices through your name as well as your age – the cause for all this celebrating. The number in icing read 1 – 7 – 5.
```
