# Classification request: batch 36 of 53 (40 records, IC-1801 to IC-1840)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-036-reply.json`.

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

## IC-1801: Her Cruising Car: Portrait of 2 Small Town Girls

- Title: Her Cruising Car: Portrait of 2 Small Town Girls
- Author (byline): Nikki Giovanni
- Work: The Collected Poetry of Nikki Giovanni
- Publisher: HarperCollins Publishers
- Publication date as stated: Jan 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1018
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nikki Giovanni
Book: The Collected Poetry of Nikki Giovanni
ISBN: 978-0060724290
Publisher: HarperCollins Publishers
Date (Month/Year): Jan 2007
```

### Introduction (context only: never use it for content warnings)

```text
Thomas Wolfe once wrote: “Something has spoken to me in the night...and told me that I shall die, I know not where. Saying: "[Death is] to lose the earth you know for greater knowing; to lose the life you have, for greater life; to leave the friends you loved, for greater loving; to find a land more kind than home, more large than earth.” He also said in that wrote in that same novel (You Can’t Go Home Again) – “Some things will never change. Some things will always be the same. Lean down your ear upon the earth and listen.” But was Wolfe right, or wrong? Nikki Giovanni ponders this dilemma in her poem “Her Cruising Car.”
```

### Performance text (classify this)

```text
There is nothing . . . that can be said . . . that can frighten me . . . anymore . . . Sadden me . . . perhaps . . . disgust me . . . certainly . . . but not make me afraid . . . It has been said . . . Learn What You Fear . . . Then Make Love To It . . . dance with it . . . put it on your dresser . . . and kiss it good . . . night . . . Say it . . . over and over . .

. until in the darkest hour . . . from the deepest sleep . . . you can be awakened . . . to say Yes . . .

She never learned . . . no matter how often people tried . . . that it was hers . . . the fear and the Life . . . the glory of the gamble . . . It was her quarter . . . she had to pick the machine . . . She never understood . . . simple duty . . . knowing only to give all of herself . . . or none . . . There was no balance . . . to her triangle . . . though three points . . . are the strongest mathematical figures . . . no tingle . . . when struck . . . no joy . . . in her song . . . no comfort in her chair . . . war/always war . . . with who she was . . . who she wanted to be . . . and what they wanted . . . of her . . .

One reason I think . . . I am qualified . . . to run the world . . . though my appointment is not imminent . . . is when I get . . . what I want . . . I am happy . . . It is surprising to me . . . how few people are . . . When they win . . . like Richard Nixon or John McEnroe . . . they are unhappy . . . when they lose . . . impossible . . . One reason I think . . . I have neither ulcers nor nail biting habits . . . is I know to be careful . . . of what I want . . . I just may get it . . .

She was never taught . . . that everything is earned . . . that Newton was right . . . .for every action there is an equal and opposite reaction . . . Interest is obtained . . . only on Savings . . . .Personality is developed . . . only on risk . . . What is sought . . . must first be given . . . We please others . . . by only allowing them access . . . to that part of ourselves which is public . . . If familiarity breeds contempt . . . use breeds hatred . . .

Turtles . . . the kind you find in pet stores . . . the kind Darwin met on Galapagos . . . grow to fit the environment . . . There are . . . .probably . . . some genetic limits . . . but a small turtle . . . .in a small bowl . . . will not outgrow . . . her home . . . Flowers . . . will rise . . . .proportionate more to the size . . . of the pot . . . .than the relationship of sun . . . to rain . . . Humans seldom deviate . . . If she hadn't been a small town girl . . . with a mind and heart moulded absolutely . . . to fit the environment . . . she might have developed . . . a real skill . . . a real desire . . . to discover herself . . . and her gifts . . . As it was . . . as it is . . . she simply got used . . . and used to using . . .

She was never a loner . . . .never made . . . .to understand that life . . . .in fact . . . is a solitary journey . . . that only -one- . . . was going to St. Ives . . . that no one held her bag . . . while the old woman traveled to Skookum . . . that the little Red Hen and the Engine That Could . . . did it themselves . . . She was . . . let's face it . . . the leader of the pack . . . the top of the heap . . . .cheerleader extraordinaire . . . .She was very popular . . . sought after by all the right people . . . for her jokes . . . her parties . . . .her parents' car . . . The telephone was invented . . . just for her . . . She set up the friendships . . . the going steadys . . . the class officers . . . yearbook staff . . . Who's-In-Who's-Out . . . through the witch wire . . . Nothing could happen . . . without her input . . . She actually thought . . . it was important . . . who went with whom . . . to the junior prom . . . But somebody had to pick up the fallen streamers . . . sweep the now scarred dance floor . . . turn out the lights before they could go home . . .

We were born . . . in the same year . . . our mothers delivered . . . by the same doctor . . . of the same city . . . in the same hospital . . . We were little chubby girls in pink . . . passing cigarettes at the lawn parties . . . My mother made me play . . . with her . . . and hers . . . with me . . . We didn't really mind . . . we shared the same friends . . . hers . . . and the same ideas . . . mine . . . Maybe I became . . . too accustomed . . . to the sameness . . . It was certainly easier . . . for me to shed . . . her friends . . . than she to shed . . . my notions . . . Our mothers belonged . . . to the same clubs . . . Our fathers tracked . . . the same night devils . . . They all had the same expectations . . . from. . . of . . . at . . . or to . . . us . . . I liked to brood . . . she didn't . . . She liked to laugh . . . I didn't . . . I thought I was ugly . . . she didn't . . .

Pots are taught to not call kettles Black . . . people who live in glass houses . . . don't throw stones . . . small town girls learn early . . . or not at all . . . that they can make a life all . . . or abort the promise . . . One of us tried . . . one of us didn't have to . . . To each . . . according to her birth . . . from each according to her ability . . . Which is bastardized Marx . . . but legitimate bourgeoisie . . . She was never caring . . . She never learned to see . . . beyond her own windshield . . . that there were other people on the sidewalk . . . other cars . . . on the road . . . She drank . . . too much . . . for too long . . . Maybe in the back of her mind . . . or heart . . . or closet . . . .there was a sign saying: There-Is-More-Than-This . . . but she wouldn't pull it put . . . put it up . . . or even acknowledge that some things . . . many things . . . were missing . . . I accept . . . if not embrace . . . the pain . . . the sign on my car says: I Brake For Gnomes . . . the one in my heart reads: Error In Process—Please Send Chocolate . . .

Into the rising sun . . . .or setting years . . . accustomed to the scattered friends littering the road . . . she drives on . . . with the confidence of small town drivers who know every wayfall . . . towards the smaller minds . . . . . around the once hopeful lovers . . . into the illusion of what it is . . . to be a woman . . . through the delusion that trip necessitates . . . never once slowing . . . .to ask Did I Hurt You . . . May I Love You . . . Can I/May I Please Give . . . You A Lift . . . With the surety . . . of one who never had to walk . . . .she accelerates . . . toward boredom . . . secure in the understanding . . . that everybody knows her . . . and would be unlikely to ticket . . . her cruising car . . . She was my friend . . . more than a sister . . . really . . . a part of the mirror . . . against which I adjust . . . my makeup . . . I have no directions . . . but here is a sign . . . Thomas Wolfe was wrong . . . Maybe it will be read . . .
```

---

## IC-1802: The Hill We Climb

- Title: The Hill We Climb
- Author (byline): Amanda Gorman
- Work: Not specified
- Publisher: Viking Books
- Publication date as stated: March 2021
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 715
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amanda Gorman
ISBN: 978-0593465271
Publisher: Viking Books
Date (Month/Year): March 2021
```

### Introduction (context only: never use it for content warnings)

```text
In the words of Amanda Gorman . . . "Poetry is a weapon. It is an instrument of social change . . . one of the most political arts out there because it demands that you rupture and destabilize the language you're working with. Inherently, you are pushing against the status quo . . . for it's that tradition of truth-telling."

On a cold winter day in January 2021 - Inauguration Day -- Gorman did her truth-telling on the steps of the United States Capitol as the youngest known inaugural poet.

Her message is one of hope and unity but refuses to turn a blind eye to the civil unrest within our great country. You see, Ms Gorman had written about half of this selection but only finished her message on the night of the riot.

The Hill We Climb by Amanda Gorman
```

### Performance text (classify this)

```text
When day comes we ask ourselves,
where can we find light in this never-ending shade?
The loss we carry,
a sea we must wade
We've braved the belly of the beast
We've learned that quiet isn't always peace
And the norms and notions
of what just is
Isn't always just-ice
And yet the dawn is ours
before we knew it
Somehow we do it
Somehow we've weathered and witnessed
a nation that isn't broken
but simply unfinished
We the successors of a country and a time
Where a skinny Black girl
descended from slaves and raised by a single mother
can dream of becoming president
only to find herself reciting for one
And yes we are far from polished
far from pristine
but that doesn't mean we are
striving to form a union that is perfect
We are striving to forge a union with purpose
To compose a country committed to all cultures, colors,
characters and
conditions of man
And so we lift our gazes not to what stands between us
but what stands before us
We close the divide because we know, to put our future
first,
we must first put our differences aside
We lay down our arms
so we can reach out our arms
to one another
We seek harm to none and harmony for all
Let the globe, if nothing else, say this is true:
That even as we grieved, we grew
That even as we hurt, we hoped
That even as we tired, we tried
That we'll forever be tied together, victorious
Not because we will never again know defeat
but because we will never again sow division
Scripture tells us to envision
that everyone shall sit under their own vine and fig tree
And no one shall make them afraid
If we're to live up to our own time
Then victory won't lie in the blade
But in all the bridges we've made
That is the promise to glade
The hill we climb
If only we dare
It's because being American is more than a pride we inherit,
it's the past we step into
and how we repair it
We've seen a force that would shatter our nation
rather than share it
Would destroy our country if it meant delaying democracy
And this effort very nearly succeeded
But while democracy can be periodically delayed
it can never be permanently defeated
In this truth
in this faith we trust
For while we have our eyes on the future
history has its eyes on us
This is the era of just redemption
We feared at its inception
We did not feel prepared to be the heirs
of such a terrifying hour
but within it we found the power
to author a new chapter
To offer hope and laughter to ourselves
So while once we asked,
how could we possibly prevail over catastrophe?
Now we assert
How could catastrophe possibly prevail over us?
We will not march back to what was
but move to what shall be
A country that is bruised but whole,
benevolent but bold,
fierce and free
We will not be turned around
or interrupted by intimidation
because we know our inaction and inertia
will be the inheritance of the next generation
Our blunders become their burdens
But one thing is certain:
If we merge mercy with might,
and might with right,
then love becomes our legacy
and change our children's birthright
So let us leave behind a country
better than the one we were left with
Every breath from my bronze-pounded chest,
we will raise this wounded world into a wondrous one
We will rise from the gold-limbed hills of the west,
we will rise from the windswept northeast
where our forefathers first realized revolution
We will rise from the lake-rimmed cities of the midwestern
states,
we will rise from the sunbaked south
We will rebuild, reconcile and recover
and every known nook of our nation and
every corner called our country,
our people diverse and beautiful will emerge,
battered and beautiful
When day comes we step out of the shade,
aflame and unafraid
The new dawn blooms as we free it
For there is always light,
if only we're brave enough to see it
If only we're brave enough to be it
```

---

## IC-1803: How Far We’ve Come – A Collection

- Title: How Far We’ve Come – A Collection
- Author (byline): William Butler Yeats and Nicole Blackman
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1178
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Butler Yeats
Book: The Yeats Reader
ISBN: 978-0743227988
Publisher: Scribner
Date (Month/Year): Aug 2002
Author: Nicole Blakcman
Book: Blood Sugar
ISBN: 978-1888451344
Publisher: Akashic Books
Date (Month/Year): May 2002
```

### Introduction (context only: never use it for content warnings)

```text
The role of women in society at the turn of the 20th century was vastly different than it is today. They were not allowed to vote, had no property rights, were rarely allowed to work outside the home, or to gain a college education. Women were very dependent on men. Written just after the turn of the 20th century, A Pray for My Daughter portrays how a father hopes that instead of growing up to be a very beautiful woman, his daughter should be blessed with the attributes of a virtuous and great soul. She should be well-mannered and full of humility rather than being strongly opinionated, to avoid intellectual detestation that could drown her in misery. Travel back in time with me to view a different world for women. A Prayer for My Daughter by William Butler Yeats.
```

### Performance text (classify this)

```text
A Prayer for My Daughter

Once more the storm is howling, and half hid
Under this cradle-hood and coverlid
My child sleeps on. There is no obstacle
But Gregory's wood and one bare hill
Whereby the haystack- and roof-levelling wind,
Bred on the Atlantic, can be stayed;
And for an hour I have walked and prayed
Because of the great gloom that is in my mind.

I have walked and prayed for this young child an hour And heard the sea-wind scream upon the tower, And under the arches of the bridge, and scream In the elms above the flooded stream; Imagining in excited reverie That the future years had come, Dancing to a frenzied drum, Out of the murderous innocence of the sea.

May she be granted beauty and yet not
Beauty to make a stranger's eye distraught,
Or hers before a looking-glass, for such,
Being made beautiful overmuch,
Consider beauty a sufficient end,
Lose natural kindness and maybe
The heart-revealing intimacy
That chooses right, and never find a friend.

Helen being chosen found life flat and dull
And later had much trouble from a fool,
While that great Queen, that rose out of the spray,
Being fatherless could have her way
Yet chose a bandy-leggèd smith for man.
It's certain that fine women eat
A crazy salad with their meat
Whereby the Horn of Plenty is undone.

In courtesy I'd have her chiefly learned;
Hearts are not had as a gift but hearts are earned
By those that are not entirely beautiful;
Yet many, that have played the fool
For beauty's very self, has charm made wise,
And many a poor man that has roved,
Loved and thought himself beloved,
From a glad kindness cannot take his eyes.

May she become a flourishing hidden tree That all her thoughts may like the linnet be, And have no business but dispensing round Their magnanimities of sound, Nor but in merriment begin a chase, Nor but in merriment a quarrel. O may she live like some green laurel Rooted in one dear perpetual place.

My mind, because the minds that I have loved,
The sort of beauty that I have approved,
Prosper but little, has dried up of late,
Yet knows that to be choked with hate
May well be of all evil chances chief.
If there's no hatred in a mind
Assault and battery of the wind
Can never tear the linnet from the leaf.

An intellectual hatred is the worst,
So let her think opinions are accursed.
Have I not seen the loveliest woman born
Out of the mouth of Plenty's horn,
Because of her opinionated mind
Barter that horn and every good
By quiet natures understood
For an old bellows full of angry wind?

Considering that, all hatred driven hence, The soul recovers radical innocence And learns at last that it is self-delighting, Self-appeasing, self-affrighting, And that its own sweet will is Heaven's will; She can, though every face should scowl And every windy quarter howl Or every bellows burst, be happy still.

And may her bridegroom bring her to a house Where all's accustomed, ceremonious; For arrogance and hatred are the wares Peddled in the thoroughfares. How but in custom and in ceremony Are innocence and beauty born?

Ceremony's a name for the rich horn, And custom for the spreading laurel tree.

TRANSITION Today, 100 years after Yeats penned the Prayer for his daughter, the world, especially the world for women is drastically different. There is no doubt about it...women all over the world are on the move. Women, responding to a vivid inner calling to make a contribution, are finding a stronger voice. Women of every generation, race, nationality, and ability are poised in potential. It is simply time for "nice girls" everywhere to come out from crouching behind good manners, and standing up with dignity, evolve into women of honor. The prayer for daughters of the 21st century might sound something like this: Daughter by Nicole Blackman Daughter

One day I'll give birth to a tiny baby girl and when she's born she'll scream and I'll make sure she never stops.

I will kiss her before I lay her down and will tell her a story so she knows how it is and how it must be for her to survive.

I'll tell her about the power of water
the seduction of paper
the promise of gasoline
and the hope of blood.

I'll teach her to shave her eyebrows and mark her skin.

I'll teach her that her body is
her greatest work of art.
I'll tell her to light things on fire
and keep them burning.

I'll teach her that the fire will not consume her, that she must take it and use it.

I'll tell her to try anything fight with, pray with anyone, just as long as she feels something.

I'll help her do her best work when it rains.
I'll tell her to reinvent herself every 28 days.
I'll teach her to develop all her selves,
the courageous ones,
the smart ones,
the dreaming ones
the fast ones.

I'll teach her that she has an army inside her that can save her life.

I'll make sure she always carries a pen
so she can take down the evidence.
If she has no paper, I'll teach her to
write everything down on her tongue.
I'll help her to see that she will not find God
or salvation in a dark brick building
built by dead men.
I'll explain to her that it's better to regret the things
she has done than the things she hasn't.

I'll teach her to write her manifestos on cocktail napkins.

I'll teach her to talk hard. I'll tell her that her skin is the most beautiful dress she will ever wear.

I'll tell her that people must earn the right to use her nickname, that forced intimacy is an ugly thing.

I'll make her understand that she is worth more with her clothes on.

I'll tell her that when the words finally flow too fast
and she has no use for a pen
that she must quit her job
run out of the house in her bathrobe,
leaving the door open.
I'll teach her to follow the words.

I'll tell her to stand up
and head for the door
after she makes love.
When he asks her to
stay she'll say
she's got to
go.

I'll tell her that when she first bleeds
when she is a woman,
to go up to the roof at midnight,
reach her hands up to the sky and scream.

I'll teach her to be whole, to be holy,
to be so much that she doesn't even
need me anymore.
I'll tell her to go quickly and never come back.
I will make her stronger than me.

I'll say to her never forget what they did to you and never let them know you remember.

Never forget what they did to you and never let them know you remember.
```

---

## IC-1804: How to Stay Bitter Through the Happiest Times

- Title: How to Stay Bitter Through the Happiest Times
- Author (byline): Anita Liberty
- Work: Not specified
- Publisher: Villard
- Publication date as stated: June 2006
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1571
- Already set (do not supply): none

### Source block (context only)

```text
Author: Anita Liberty
ISBN: 978-0812976199
Publisher: Villard
Date (Month/Year): June 2006
```

### Introduction (context only: never use it for content warnings)

```text
Humiliating her ex-boyfriend Mitchell in public was a perfectly satisfying career for Anita Liberty, but then she had to go and do something she swore never to do — she got over it. Then, to make matters worse, she fell blissfully in love. And now she’s really got problems. What do you do when you are "an angry performance poet" who suddenly finds herself "perilously close to true happiness?"

How to Stay Bitter Through the Happiest Times by Anita Liberty
```

### Performance text (classify this)

```text
(Pg 3) I am Anita Liberty – Anita Liberty! I am the mouthpiece for the scorned masses. I am the self-appointed spokesperson for the bitter. I am the performance poet who made a name for herself by devoting her entire career to humiliating her ex-boyfriend, Mitchell, in public when he left her for a woman named Heather. I’m a cult heroine, dammit! But now I’m totally messed up.

(Pg 16-17) He seemed nice

He was smart

And funny.

And cute.

I liked his clothes.

So . . . you had one good date. With someone who seemed normal. But seemed is the operative word here. You never know. You just never know. I dated someone for three and a half years who seemed normal. And then he wasn’t anymore. In fact, he turned out to be extremely abnormal. First impressions mean nothing.

(Pg 18-19) He called the next day.

He left me a message saying that he had a really nice time and asking when he could see me again. Huh? I’m confused. I just seems so . . . so . . . normal.

(Pg 20) He cooked me dinner.

Which was good.

And nothing he said irritated me.

Not slightly.

Not once

And he kissed me.

That felt nice.

(Pg 23) We saw a movie and he held my hand.

He smiled at me a lot.

He told me I was beautiful.

He bought me a bottle of ginger ale

On the way home.

That’s my favorite soda.

Guess what?

It’s his, too.

(Pg 38) I’m confused. It’s been so long since I’ve even wanted to pursue a relationship that I’ve forgotten how to proceed. It’s all making me very, very tense. (PG 42) Thing I wanted before I don’t want anymore because they don’t’ involve him.

I want to pay his rent. I want to lik his stamps and scramble his eggs.

I want to gaze at him adoringly, Even though if anyone sees me it will completely ruin my reputation.

I want to write the kinds of poems
he deserves to have written about him.
Poems that exalt him.
Poems that boost his confidence.
Poems that publicly glorify him.

I walk down the street And think about how much I love him and I feel good about all humanity.

Who the hell am I ?!?!!!!!?
I don’t recognize myself.
I’m not the same person I was before I met him.
I‘m totally losing my identity.

(Pg 44-45) Well. I’m allowed to enjoy the fact that I’m so close to being happy. I know it won’t last and maybe that’s why I’m savoring it. These rose-colored glasses will shatter. Problems will arise. Flaws will surface. Reality will set in. I would be nervous, but I’ve never been one to shy away from reality.

(Pg 48) I performed tonight for the first time in front of Good Date. Afterward, people gathered around me, praising, adulating, fawning. I appreciated the accolades, but I wanted to find Good Date. I wanted his adulation, his fawn. I approached him and silently practiced a humble response to his reverence:

“No, really, you really liked it?

You thought it was amazing?

Come on, the best thing you’ve ever seen on stage?

That can’t be true . . .

When I got to him, he took me in his arms and kissed me deeply.

“So, what’d ya think?” He tells me he thought it was great.

“And?” I smile.

“And I have a few notes.

“NOTES?”

“Yeah,” he says. “We can talk when we get home.”

We’re gonna talk when we get home, all right. Because clearly he doesn’t understand that the last person who tried to give me notes . . . was the first person who tried to give me notes.

(PG 50-51) . . . he said he wasn’t criticizing, he just had a few “suggestions.” I told him it was too early in our relationship for him to be giving me advice about my work, when I’d been doing my work just fine without him for years. He said that maybe I just couldn’t handle constructive criticism and hat that was a good thing to know about me. I said that maybe he was just threatened by my talent and my success and that that was a good thing to know about him. I then asked him what “suggestions” he had. And, ya know, they weren’t bad. The guy actually had some good ideas. He then went on to tell me, in detail, how funny and smart I was, etc.

(PG 55) I’m the poster girl for the Society to Mistrust the Longevity of a Romantic Relationship (better known as SMLRR) And, yet, here I am. Trusting again. Loving again.

They’re going to revoke my membership. And getting reinstated is a bitch.

(Pg 119) We moved in together. No proposal. No promises. Nothing. He told me not to worry, that he wasn’t going anywhere. Whew. That’s a relief. I just feel like I’m having relationship déjà vu.

I’ve been here before.
I’ve given up my apartment.
I’ve trusted my instincts.
I’ve trusted someone.

Boyfriend’s right. There’s no reason to worry. Why would I worry? IT’S NOT LIKE THE LAST TIME I MOVED IN WITH SOMEONE HE TURNED OUT TO BE A SOCIOPATH OR ANYTHING.

(Pg 120) I’m going crazy. Every week that goes by, every romantic dinner, every time Boyfriend reaches for me lovingly, I think, “this is it. It’s about to happen. He’s going to . . . ask me to marry him.” I can’t help myself. I can’t stop the train I’m on. I loathe the woman I’ve become.

(Pg 134) I told you so. What is it about those four words that makes Them roll so deliciously off the tongue?

I told you so I told you so.

Left over from the playground
taunting other kids,
Recognizing the position of power
That being able to see into the future affords you.

I knew it!

I was right!
I’m psychic.
I saw it coming, even if no one else did.
Especially if no one else did.

(Pg 133) We’ve decided to take a break. I said I didn’t want to go on if this wasn’t the real deal. He said he didn’t want to feel pressured into making one of the biggest decisions of his life.

(Pg 139) If you’re in a great relationship

with someone who respects you

and you’re ready to get married,

But the person you’re with isn’t,

Break up with him.

That way you’ll eliminate

Any possibility of getting hurt.

Or being happy

(Pg 142) I have to give him his space. I’m not going to call him. He’ll call me when he’s ready. Right? I just have to patient and wait. (Long pause) Okay. I called him. What? I waited. For sixteen whole minutes. He’s coming over tonight. (Pg 145) . . . . I’m engaged! I have a fiancé. I’m going to have a husband. But first I’m going to have a wedding!!! I’m getting married. I’m getting married!

(Pg 152) And I’m understandably concerned about how that will affect my work.

(Pg 176) All of a sudden, this whole “getting married” thing seems like a terrible idea. [Why? Because] Our parents must meet. The deal must be approved, notarized and ordained. Fiancé and I would literally rather eat spoonfuls of live ants than sit through an evening of polite conversation with the four people who are responsible for our existences. What if they hate each other? Or, worst-case scenario, what if they get along? Plech. I don’t want our parents to be in cahoots with one another. Cahoots make me cringe.

(Pg 177) I was starting to have time to waste in therapy.
Filling forty-five minutes was becoming difficult.
Now I won’t have to worry.
Nifty.

(Pg 199) Everyone is annoying me. Everyone. My family, my friends and oh, the King of Infuriation . . . Fiancé. They can all just go to hell. I don’t want to have a wedding anymore Fiancé and I are fighting like howler monkeys and I just can’t imagine that I’m going to look over at him on our wedding day and think, “I’m so lucky to be marrying you” More likely I’m going to look at him and think, “You’re and ass-clown. Why am I marrying an ass clown?” I hate Fiancé because he asked me to marry him and it now seems like some horrible, awful mistake. We started writing our vows last night. . .

(Pg 200) [Here’s what I came up with] I don’t know what you’re expecting from me, but I can’t promise to be nice and supportive for ever

and ever in every possible scenario and situation. I just can’t. You know I don’t like to make promises I

can’t keep.
However, I can vow to try.
And I will try. Hard.
I vow that I will try to be nice and supportive.
Although, if I’m being completely honest,
some days I might try harder than others.

(Pg 210) My wedding day was a perfect day
Our wedding day was a perfect day.
It was transcendent and pure.
That day changed my standards dramatically.
Because now I know what it’s like to experience a

perfect day. Not alone. Together.

(Pg 3) I have no reason to be angry anymore. And that makes me angry. I built my entire career on being angry. It’s what I do. It’s who I am. What was I thinking?? I was thinking what society wanted me to think – that happy was the goal. Little did I know that being happy would make me so miserable. (Pg 215) . . . this time the end is a happy one. A terribly, terribly happy one.

[Oh, calm down. I’ll be back. Just imagine what I’ll be like when I have someone camped out in my uterus for nine months . . . It won’t be pretty!]
```

---

## IC-1805: How to Translate a Joke and Mama

- Title: How to Translate a Joke and Mama
- Author (byline): Emtithal (Emi) Mahmoud
- Work: Sisters Entrance (Pg 37 and Pg 108)
- Publisher: Andrews McMeel Publishing
- Publication date as stated: May 2018
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 964
- Already set (do not supply): none

### Source block (context only)

```text
Author: Emtithal (Emi) Mahmoud
Book: Sisters Entrance (Pg 37 and Pg 108)
ISBN: 978-1449492793
Publisher: Andrews McMeel Publishing
Date (Month/Year): May 2018
```

### Introduction (context only: never use it for content warnings)

```text
Events in 2021 and 2022 have conspired to crush the rights and dignity of millions of women and girls world-wide:

Recently, a man in Pakistan set his house on fire, killing his daughters and grandchildren to protect his “honor” from the social repercussions of an inappropriate marriage. Female judges and lawyers, now obsolete entities in the Taliban regime of Afghanistan, are hiding in fear of torture and death and females can no longer attend educational facilities. In Iran, the violent arrest of a woman was captured on video, depicting her capture with a dog-catcher’s pole, before being thrown in the back of a van for her inappropriate display of a hijab. She later died in the custody of the “morality police.” And in the US, women are losing the right of choice as Roe v Wade is overturned.

In the words of the poet, “My greatest dream for the future is that one day my poetry will become a marker of how things used to be --“a relic of history.”

Sudanese born, Emi Mahmoud cries out for the oppression all women face in How to Translate a Joke and Mama.
```

### Performance text (classify this)

```text
How to Translate a Joke (Pg 37)
A man walks into the market,
looking for a date.
He asks the village playboy for help.
The village playboy says:
"Watch and learn."

He walks up to a girl selling honey and says: "Do you have any honey, honey?" She swoons. Gives him honey and a kiss.

He walks up to a woman selling flowers:
"Do you have any flowers, you rose?"
She melts. Gives him flowers and a kiss.
He walks to a third woman.
"Do you have any sugar, sugar?"
She practically dies. Gives him sugar and kisses him twice.

The playboy comes back. "Your turn, stud."

The man apprehensively walks up to a woman selling dairy and says: "Do you have any milk, cow?"

Realize that humor transcends all boundaries. That laughter is a language that knows no borders. That this joke that I learned in Arabic, makes perfect sense in English and French and in any other language. Realize that we call women cows in every language.

Realize that humor leaves little room for questions, and even less room for victims, and even less room for apologies.

Realize that in one version of this joke,
the man is looking to pick up girls.
In another he's looking for a wife.
In a third, he's looking for an answer.
And maybe the cow slaps him.
Or the cow asks him to leave and he tries again.
Or she walks faster, clutches her purse.
Or maybe she threatens him and is jailed for treason.
Or maybe the cow sues him.
And the case is dismissed.
Or they settle . . . down.

We are willing to say offensive more than we say

dangerous. As if harm isn't transitive. As if it isn't something you do to another person.

We like to pretend that I am not as uncomfortable alone
on the streets of New York as I am on the streets of Nepal.
That a stroll in Philly or Indiana or Minnesota,
doesn't bring as many stares as in India or Sudan or Egypt.
That violence is a third-world-problem.
That it isn't here. Hiding. In a conversation.
Or in a bouquet. Or a market.
That not being alone makes a difference.
If they don't get the joke, say it again.
Smile more this time. Repeat the punchline.
Pause for dramatic effect. Use jazz-hands if you have to.
Laugh.

In another version,
that man walks into a market looking for a date,
and leaves with an unwilling woman.
A bounty. That in my language I am a sweet.

And if not that, a decoration. A flower. A gift.

He walks up to the girl selling honey. She gives him her eyes. Her arms. Her silence.

He walks up to the girl selling sugar. She practically dies.

He walks up to the girl selling flowers.
Calls her a rose. Strips all her thorns.
Sticks her in a bouquet.
She fights. He breaks her.
Calls her a dead thing.
She melts. Is trampled in the market.
There are four women in the joke.
None of them speak.

Realize that humor transcends all realities.
That laughter is a language that knows no borders.
That this joke I heard in Arabic,
hurts just as much in English and French
and in any other dialect.

Mama (Pg 108) I was walking down the street when a man stopped me and

said, Hey yo sistah, you from the motherland? Because my skin is a shade too deep not to have come from

foreign soil
Because this garment on my head screams Africa
Because my body is a beacon calling everybody to come
flock to the motherland

I said, I’m Sudanese, why? He says, ‘cause you got a little bit of flavor in you, I’m just admiring what your mama gave you

Let me tell you something about my mama She can reduce a man to tattered flesh without so much as

blinking
Her words fester beneath your skin and the whole time,
You won’t be able to stop cradling her eyes.
My mama is a woman, flawless and formidable in the same

step. Woman walks into a warzone and has warriors cowering at

her feet
My mama carries all of us in her body,
on her face, in her blood and
Blood is no good once you let it loose
So she always holds us close.

When I was 7, she cradled bullets in the billows of her

robes. That same night, she taught me how to get gunpowder out

of cotton with a bar of soap. Years later when the soldiers held her at gunpoint and

asked her who she was She said, I am a daughter of Adam, I am a woman, who

the hell are you?

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

my flavor is mutiny It is burden, it is grit and it is compromise And you don’t know compromise until you’ve rebuilt your

home for the third time Without bricks, without mortar, without any other option

I turned to the man and said, My mother and I can’t walk the streets alone
```

---

## IC-1806: I Believe in Anarchy from Emma Goldman: Love, Anarchy and Other Affairs

- Title: I Believe in Anarchy from Emma Goldman: Love, Anarchy and Other Affairs
- Author (byline): Jessica Litwak
- Work: Women Heroes: Six Short Plays from the Women’s Project
- Publisher: Hal Leonard Corporations
- Publication date as stated: 1987
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 614
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jessica Litwak
Book: Women Heroes: Six Short Plays from the Women’s
Project
ISBN: 0936839228
Publisher: Hal Leonard Corporations
Date (Month/Year): 1987
```

### Introduction (context only: never use it for content warnings)

```text
At 10:00 on the night of September 9th, 1901, Emma Goldman was arrested for her alleged complicity in the plot to assassinate President McKinley. Emma took pride in being one of the few female anarchists of her time. The revolutionary fire that consumed Emma was fueled in part by anarchy, but also by her love affair with Alexander Berkamn. Her passions lie in her beliefs. She above all can declare without doubt “I Believe in Anarchy” by Jessica Litwak.
```

### Performance text (classify this)

```text
I believe in anarchy
freedom
free love
speech.
I believe in America Courage.
People.
Pride.

I believe there is great work to do.
Now.
However we can.
I believe that governments abuse their power.
Now and always.
I believe the future is in our hands.
I believe in dreamers.
Children. Streamers.
Confetti.
That dancing is important
I believe
that if America has entered the war to make the world
safe for democracy,
she must first make democracy safe in America.
I believe in peace.
Beauty .
Duty.
I believe people must be free to express themselves
differently
in liberty.
I believe in passion. In art.

In anarchy.
That women must make choices about their lives as
wives.
mothers
lovers.
That America should not stick her nose into other
people's business.
I believe
in revolution coming next,
in sex
Tolstoy
a brand new age.
Duse on stage.
I believe in Russia's cries,
in open eyes,
the President lies.
I believe in anarchy.
In Freud's interpretations.
Humanity. Salvation.
I believe in action. Strikes.
The likes
of which we've still not seen.
I believe in honesty.
Good food. Wine. Hard work. Happiness. Radiance.
The free child.
Oscar Wilde.
Sasha's smile.
Defiance. Pride.
I believe anarchism is a process-not a finality.
I believe in the spark
a light in the dark.
History is eternal recurrence-and people
are still tearing
each other apart
after all these years.
We fools go on. . .
believing
in life. Equality. Freedom.
The American people.
A wakening.
Liberation. Emancipation.
Dreams.

Ideals.
Anarchy
I believe in standing alone, grown
woman. Making her own choices. Her
face held high, not afraid to die.
I am proud of my beliefs and
I believe...
no matter what anyone says about me
I believe in the masses
in destroying the classes.
I believe in tenderness
In common sense-the declaration
Of independence.
I believe in Max, Johann,
Fedya. Alexander Berkman.
I believe in anarchy. . . and
Nietzche says:
"That which is born out of love
always takes place beyond good and evil."
Upheaval. Starting fresh.
Making a mess.

I believe in moving.
Not losing.
Hope.
In coping with these hard but wonderful times.
Lines of people allover the world
Holding each other, helping each other.
Protesting war. Shouting for. . .
freedom, free love, speech. . .
I believe in anarchy. . .
"The philosophy of a new social order based on liberty
unrestricted by man-made law."
I believe in fun.
Running, screaming, dancing, leaping, laughing, kissing,
wishing.
Making it real.
I believe in love.
Again and again.
Women and men. Women
and all the men in my life. . .
I believe in living for today.
Strong. Resilient. Gay.

Paving the road.
I believe our enemy is the dying past. . . and we are the
glowing future...
I believe in we.
I believe in me.
You, her, him, them (as long as they're us) not to
mention everybody who
doesn't know
yet. . . I believe in charm.
Strong arms.
The great alarm . . .
here's to social harmony.
And all the men in my life.
I believe in going ahead.
I believe in America.
I disbelieve in authority. Invasion. Coercion and force.
Oppression, violence, marriage, divorce.
I believe in the absence of government. . .
in people running their own lives.
Children. Not deprived
Of love.

Free love. And the freedom
of dreaming. . . and making dreams live.
The pleasure to give
a warm hand
to the next man. Fortified
with courage and will.
Pulling each other up the hill.
I believe in anarchism.
The new world.
Women and men
beginning again. I believe
in patriotism of the soul.
Our role
in the liberation of mankind.
I believe in the spiritual
political
economic
revolution of life. Strife.
I believe in doing whatever it takes
to make
it happen.
```

---

## IC-1807: I Don’t Want to be Crazy

- Title: I Don’t Want to be Crazy
- Author (byline): Samantha Schutz
- Work: Not specified
- Publisher: Scholastic, Inc.
- Publication date as stated: Aug 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1443
- Already set (do not supply): none

### Source block (context only)

```text
Author: Samantha Schutz
ISBN: 978-0439805193
Publisher: Scholastic, Inc.
Date (Month/Year): Aug 2007
```

### Introduction (context only: never use it for content warnings)

```text
According to the National Institute of Mental Health, Anxiety disorders are the most common mental illness in the US, affecting 40 million adults every year. Sure, everyone experiences feelings of anxiety and even panic sometimes. It’s a natural response to stressful or dangerous situations.

BUT for someone with a panic disorder, overwhelming emotions appear regularly and for no apparent reason. Instead of seeking help, most struggle to hide the attacks, fearing that they will a best be judged by those around them, and a worst be deemed “crazy” by society.

I Don’t Want to be Crazy by Samantha Schutz
```

### Performance text (classify this)

```text
(Pg 1-2) I can’t believe
no one else can hear
I am screaming
inside my head.

Things are moving so fast.
I am going to die.
I am going to die.
I am going to die.
My hands are shaking.
I try to squeeze them, try to make it stop,
but now my fists are shaking,
and this shaking is working its way through me.
It must look like I am having a fit.
I want to let the scream out,
but I think if I start,
I’ll never stop.

It's not supposed to be like this.
I am too young to die.
I don’t know how to make this end,
and if it doesn’t, I’ll have to go to a hospital,
be medicated, force-fed soft foods.
I am not that person.

I am not. I am not.

(Pg 7-8) Applying to college was a disaster.
My parents had their choice for me,
and I had mine.
But since they were paying the bills ,
there was no room for compromise.

We fought about my application essay for weeks>
It has to be perfect --
revised and reread dozens of times,
market up in red pen
until it was bloody.

In the end my personal statement
was more my mother’s than my own
and fiction became fact
because it sounded better.

It's been like this
for as long as I can remember --
writing and rewriting homework,
book reports, and papers
until they were not mine --
until they were perfect.

(Pg 12) I can’t wait
to get out of this room
out of this house
with all its rules,
out of this neighborhood
where everyone knows each other.

*****

(Pg 22-23) Living with Sarah the first few weeks
is like an extended sleepover party.
Our dorm room isn’t big,
but I can be anything I want here.
No one has to know
that I wasn’t popular in high school,
that I’ve never stayed out all night.

I’m taking art classes, writing classes, dance classes -- all the things there was no room for before.

I reread Anais Nin’s journals

(Pg i) It takes courage to push yourself to places that you

have never been before . . . to test your limits . . . to

break through barriers. And the day came when the risk

it took to remain tight inside the bud was more painful

than the risk it took to blossom – Anais Nin

And write in my own.

But . . .
(Pg 36-39) I can’t sit still in class.
I can’t hear what the teacher is saying.
All I can hear is my voice in my head
telling me that things are not right --
that I am not right.
It feels like something is trying to push its way out of me,
out of my chest.

I have to get out of here. (coughing)
I fake a coughing fit and leave
I’m trapped – stuck inside of this shaking, sweating body.
The only place that seems save
is the bathroom.
Sitting in the stall, with my chest on my thighs,
I try to breathe,
But the more I think about my breathing,
the more I feel like I can’t breathe.
It feels like my insides are melting.
This must be what it feels like the moment before you die.

I have been telling myself that these feeling are new, but they aren’t.

I felt it the firs time junior year.
It felt like my chest caved in
and I couldn’t tell the difference
between the bass in the music
and a car alarm going off outside.
I couldn’t get my mind to stop racing.

It happened again, before college.
I was in Staples with my dad,
shopping for school supplies.
All of a sudden the ground felt soft
and the sounds around me
were too fast and too slow
at the same time.

I though I would lose control,
do something crazy – start screaming
right there in the pen aisle.
My dad would know.

Everyone would know.

Now this feeling follows me
everywhere I go.
It clings to me,
Makes my skin crawl.
It sits with me in class,
whispers in my ear,
tells me that I shouldn’t be here.
(Pg 45) I have resigned myself
to the fact that I have gone insane.
I am too tired
to keep fighting
the empty feeling in my stomach
and the buzzing in my head.

This was not supposed to be how things turned out. There were steps taken, expectations -- a specialized kindergarten and elementary school, a prestigious private high school summer study program disguised as camp.

This is not how things are supposed to be.
(Pg 47) I am in Health Services again,
waiting for the nurse to look me over,
to take my temperature,
listen to my heart and lungs<
To tell me that I am okay,
when I see a poster on the wall
that says, “Having Panic Attacks?

For the first time in weeks
things make sense
(Pg 50-51) Panic attacks are
feelings of dying,
going crazy,
losing control of emotions and behavior.
I have the urge to
escape of flee.

Sometimes I have five a day. This is my life.

*****

(Pg 130-131) Backed up against the brick wall, I cannot trust this body. I run inside, slam the door shut, and get into bed.

The bathroom light is on
And the door is open.
I hear it . . .
You will get up and put your head in the toilet.
What will my parents think in the morning
when I’m found dead,
head in the bowl?
In my head I hear, This is not a choice.
I tell myself over and over,
I am stronger than you, stronger than you,
stronger than you.

(Pg 40) Please God make this feeling stop.
I can’t take it.
Breathe. Breathe. Breathe.
Make it stop. Please. (Beat)

(Pg 131) I am scared of myself,
I tell my therapist.
I don’t think
I want to kill myself, I say.
She tells me this is common
for people who have anxiety disorder.

(Pg 68) Little yellow pills
for the one who cannot control her adrenaline, her fear
Little yellow pills
for a child who cannot deal with being an adult.
Little yellow pills
to make me forget.
(Pg 53) Klonopin 0.6 mg
I take one in the morning
and one at night.
It makes me sleep,
makes the panic a voice in the distance --
loud enough to hear,
but quiet enough to ignore.

(Pg 218) My therapist wants to know
how my panic attacks serve me.
I don’t understand.
He wants to know what I gain from them.
Gain?
He thinks they serve a purpose.
I still don’t understand.
Is he saying that I do this to myself
To avoid situations I don’t want to be in?
To myself?
I am crying as I talk
and there must be little threads of spit
connecting my upper and lower jaw.
To myself?
I have never heard anything so awful in my life.

(Pg 243) Why would I do this to myself?
Why would I inflict this much pain,
turn my life upside down,
twist my stomach in knots,
run from friends, family?

(panic attack begins; breathing to try to control it) (Pg 246) Long slow breaths. Deep breaths.

(Pg 241) No one said I was going to be this sad. No one said I would still be crying.

I am so lonely,
Every day is the same --
trying to move slower than the rest,
To not be so angry,
so serious in the morning,
to not make myself crazy.

(Pg 258) I am scared to sleep
I am scared to eat.
I am scared to move.
And all this turns my stomach
and reminds me how alone I am
and how pitiful it is
that I need someone to love me,
to wrap me up and make me feel safe<
and how pathetic it is
that I can’t find someone, anyone
to do that for me. (Long beat)

(Pg 267-228) I wonder what my life would be like
if I’d never had anxiety disorder.
At first I think,
I’d be Miss America.
I’d be the happiest person
with the brightest smile on the face of the earth>
But the more I think about it,
The more scary life with out panic seems.
My life has been governed by anxiety.
It fills up my time.
I only know how to live like this --
with this feeling in my stomach.

When I have a panic attack
the voice in my head says
anything can happen.
I will go insane,
I will die,
I will start screaming.

(Panic attack begins and she speaks as she tries to control it
with breathing)
I try to tell myself that that voice isn’t real,
but it’s hard.
The voice is very convincing . . .

(Pg 2) It's not supposed to be like this.
I am too young to die.
I don’t know how to make this end,
and if it doesn’t, I’ll have to go to a hospital,
be medicated, force-fed soft foods.
I am not that person.
I am not.
I am not.
```

---

## IC-1808: I’m Not Giving My Black Back!

- Title: I’m Not Giving My Black Back!
- Author (byline): Jewel Diamond Taylor
- Work: Sisterfriends
- Publisher: Quiet Time Publishing
- Publication date as stated: Feb 1998
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 476
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jewel Diamond Taylor
Book: Sisterfriends
ISBN: 978-1884743061
Publisher: Quiet Time Publishing
Date(Month/Year): Feb 1998
```

### Introduction (context only: never use it for content warnings)

```text
A common belief about Black women is that they are triply disadvantaged due to their gender, their ethnicity, and their poverty. An alternative perspective on Black women portrays them as strong, resilient, and adaptive in their ability to cope with adversity, support their families, and develop avenues of self-esteem and self-actualization. Ironically, both views reflect the realities of Black women's experience in America. On the one hand, they have been victims of discrimination, economic exploitation, and social rejection for over 370 years. On the other hand, they have overcome many of these barriers through developing a set of cultural attitudes, a pattern of coping strategies, and a series of help-seeking behaviors which have enabled them to survive and sometimes thrive in a frequently hostile, exploitive, and unsupportive environment. Jewel Diamond Taylor speaks in the collective voice of resilient black women throughout the nation in “I’m Not Giving My Black Back!”
```

### Performance text (classify this)

```text
I'm Not Giving My Black Back! I'm not giving up my greens or my grits or saying “girl” and putting

my hands on my hips. You see... Life for me ain't been no crystal stair and I'm not giving up Rosa Parks, Fannie Lou Hamer, Mary McCleod Bethune, Sojourner Truth, Madame C J. Walker, Toni Morrison or Dr. Maya Angelou, ‘cause you see, I am a phenomenal woman and I'm not giving my black back.

I'm not giving up my crown, waves, braids, curls, locks, kinks, scarves or Muslim garb.

I'm not giving up sitting in Ma's kitchen
eating peach cobbler or sweet potato pie
and hearing her ask me, “How you doing
baby”? I'm not giving up going to “You Buy,
We Fry” on Fridays, or bar-b-ques on
Saturday playing bid whist and slammin’
those dominoes. I'm not giving back
Harriet Tubman's train, Soul Train,
Coltrane or the midnight train to Georgia.

Now, you can meet me at the function, at the junction but I still won't give up B.B. King, the Whispers, Fancy Ms. Nancy, Lena Horne, the Philadelphia Sound, Motown or the Temptations. ‘Cause you see, it's the way we do the things we do, like building the pyramids that still stand made by our forefathers’ hands where the diamonds, oil, silver and gold are buried in our rich dark land.

I'm not giving my black back! I'm happy being nappy with my wide hips and my wide nose and the rich melanin in my skin. I love putting lotion on my ashy legs. Oh, I'm happy being nappy and being in the skin that I'm in. I won't deny or forget my ancestors who lay in a wet grave at the bottom of the sea in the middle passage from slave trade.

And I won't give up on our youth of today who still need a way made. I won't give back Miles even though he didn't smile. I won't give back Marvin Gaye, Richard Pryor, Phyllis Hyman, Billie Holiday or Billy Eckstein, Jackie Robinson or Jackie Wilson. I won't give back the electric slide, Alvin Ailey, Bojangles or Debbie Allen. You think I'd give up reading my Jet, Ebony, Essence, Emerge, Black Enterprise, Heart and Soul or Upscale magazines?

For we are a colorful people. Like Curtis Mayfield sang, we are a people that are “darker than blue. “ We are honey, cinnamon, mahogany and chocolate. We are REDD Fox, James BROWN, Barry WHITE, The Mothers of the Church dressed in WHITE, The Color PURPLE, the Lady Who Sings the BLUES and we are Al GREEN with love and happiness.

Oh, NO... I'm not giving my black back! I'm not giving back Maxine (Waters), Martin, Medgar, Malcolm, Mandela, Marley, Marcus, Muhammad Ali, Michael (Jordan) or the Million Man March. I'm not giving my black back! Lift up the black woman's spirit.
```

---

## IC-1809: Imaginary Mambo

- Title: Imaginary Mambo
- Author (byline): Margarita Engle
- Work: Totally Middle School: Tales of Friends, Family, and Fitting In (Pg 97+)
- Publisher: Delacorte Press
- Publication date as stated: Aug 2018
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1145
- Already set (do not supply): none

### Source block (context only)

```text
Author: Margarita Engle
Book: Totally Middle School: Tales of Friends, Family,
and Fitting In (Pg 97+)
ISBN: 978-1524772208
Publisher: Delacorte Press
Date (Month/Year): Aug 2018
```

### Introduction (context only: never use it for content warnings)

```text
Margarita Engle’s mother is from Cuba and her father is from California. As a child she traveled back and forth to the island, moving seamlessly between two cultures and languages. But beginning in 1963, American travelers were prohibited from traveling to the island. Hostility between the two countries was like a wall in the ocean; creating, as she described it, “a monstrous before and after” in her life. It is her hope that through poetry we can experience a shared empathy – an empathy which can lead to compassion across cultures. And that we can begin to search for and find our similarities rather than our differences.

Imaginary Mambo by Margarita Engle
```

### Performance text (classify this)

```text
(Pg 97+) I sort of know how to dance, so moves aren't

the challenge that scares me. It's that partner thing -- waiting to be chosen, standing

alone on the sidelines
with my nervous mind and nerdy glasses.
I've seen enough PG-13 movies to know
that contact lenses, cool clothes, a sassy attitude, and

clipped-short blond hair always work like magic, attracting the perfect no-losers-allowed hot football player who somehow boasts both muscles

and brains. Well, guess what -- I'm not blond, my idea of fotbol is

soccer,
and I can't actually dance
even half as well as the rest of my family.
My parents and never-nervous party-girl primas/cousins

were all made on the dance-crazy island of Cuba, while I was born here, far from all those legendary drummers who pound out

exhilarating beats on every street corner in La Habana. Whenever I have to perform my own shy sort-of-dancy

thing at family gatherings-birthdays, quinceaneras, and

wedding receptions
I'm never as relaxed as when I'm alone
in front of a mirror, with nothing but music,
my heartbeat,
and any one of a thousand imaginary boys I know how to

invent.
They're all experts, smart but cute too, and most
importantly, easy to follow
as they lead, spinning me all over
our imaginary dance floor.
If only one of those boys existed!
I'd take him to next week's dreaded
dreadful
deadline-looming
first-in-my-lifetime
Middle School Mixer.

One week to go.
Seven days.
One hundred sixty-eight hours.
Ten thousand eighty minutes.
Six hundred four thousand eight hundred endless

agonizing

seconds. Should I get sick, skip the dance, delay this ordeal until

Winter Formal . . . or practice with my primas, get lessons from Mami and

Papi, maybe steal a boat and row to the island, where relatives I've never met will probably be eager to teach me? But what if they just make fun of me, Cuban-style, by giving me a nickname that sticks forever, something

clever that means "dorky," "clumsy," "awkward,"

"klutzy," or worst of all: "wannabe." Cubans and Cuban Americans don't live on the

same planet. Islanders are born dancing, while here we grow up

watching TV, playing video games, staring at screens,

instead of talking to living, breathing people.
SIX MORE DAYS NOW.
All the overwhelming hours at school
seem impossible, but somehow, I get through the shame of
sitting alone at lunch,
and by the time I go to my aunt's house
in the evening, dancing with my cousins seems so
intimidating that I secretly grow anxious

dizzy

delirious with fear.

FIVE DAYS.

I don't even try.
FOUR DAYS.
THREE DAYS.
ONLY TWO MORE DAYS!
The connection to my arms and legs
shuts down, as if someone has switched off all the lights

in the entire world. So I give up, and go to the nursing home to visit Abuela, because she suffered a stroke not very

long ago, and she still needs lots of company

to keep her connected to her own arms and legs. It's in the brain, she explains as we stand side by side

in front of a physical therapy clinic mirror while she

practices her balancing exercises,
perched on one foot like a flamingo.
It's not easy!
I almost fall.
Try it.
You'll see.
Standing on one leg for more than a few seconds is

tricky.

Abuela needs to learn how to walk again, because the

stroke made her brain forget where her feet are

located in space,
so she gazes downward as she recites
heel, toe, heel, toe, reminding herself
to do first things first, placing one heel
on the floor, then slowly, carefully lowering those toes.
Afterward, we talk.
The blood clot in her brain took away English,
so we're limited to her first language, but I manage to

tell her with Espanol and gestures just how worried I am about the mixer -- a word I translate as mezcladora,

one of those big trucks that stir up wet stuff and

gravel to make hard, gray concrete, like a roadway leading into

the unknown. Ay, como me encantaba bailar! my grandma says with a

sigh -- Oh, how dancing enchanted me!
I smile for the first time in days.
It's so easy to be poetic in Spanish.
Her memories seem to float in the air like feathers.

If only I could feel that weightless and graceful. No es facil, she says -- It's not easy. That's the only phrase any Cuban ever uses when faced

with a problem, and even though the words might

sound pessimistic,
it's really so much more hopeful
than claiming that a goal is impossible.
She leans on her walker as we stroll down a hallway,
gazing out windows at a garden with a fountain.
All in the brain.
Not easy, but possible.
You have to practice, Abuela tells me,
adding, so that you can teach me, because I'm sure I've

forgotten. How could my grandma forget her dance moves? She's

always been able to do the best rumba, conga, or

mambo at any party. That night, when I go home, I stand in front of my mirror, wondering how I'll get

through tomorrow. DANCE DAY! The gym looks huge, even though it's the same size

as always.
A table with punch and cookies.
Balloons on strings, drifting toward the ceiling.
Boys stand around in clusters, while girls

jump up and down, wave their arms, and giggle, until finally, someone I recognize from math class pulls me into the girl crowd, where I hop like a three-year-old, suddenly feeling exhilarated, relieved to discover that no one else knows paired-up-

partner steps,
so there's no pressure to follow a sweaty boy.
Later, when boys start to join in,
my apprehension returns, but at least it's not real horror

anymore, just his right hand on my waist, my left hand on his shoulder, and our other fingers clasped in air. He's nothing like the thousand boys I've imagined. Just a shy kid who looks worried as he watches his feet. We do a little shuffling thing, pretending we know where we're going until the slow music ends and everyone goes back to jumping around in time to a fast song, having fun, laughing, maybe even secretly imagining that we're good at this, experts like Abuela in her memory,

floating

and feathery,

our minds filled
with no es facil -- it's not easy
possibilities.
ONE WEEK AFTER DANCE DAY.
Okay, so I didn't end up with a boyfriend or dance skills,
but now I hang out with the girl from math class, and at

lunchtime we eat in a crowd of proud nerds, and starting tomorrow, I plan to practice walking, talking

Spanglish, and dancing to old Cuban music
with my lonely grandma.
The thing about new possibilities is:
It feels so good to share them.
```

---

## IC-1810: In the Marvelous Dimension

- Title: In the Marvelous Dimension
- Author (byline): Kate Daniels
- Work: Four Testimonies (Pg 29-44)
- Publisher: Louisiana State University Press
- Publication date as stated: April 1998
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1380
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kate Daniels
Book: Four Testimonies (Pg 29-44)
ISBN: 978-0807122594
Publisher: Louisiana State University Press
Date (Month/Year): April 1998
```

### Introduction (context only: never use it for content warnings)

```text
The San Francisco earthquake occurred on October 17, 1989, at 5:04 pm. It only lasted 15 seconds, but in that time the upper deck of the Nimitz Freeway collapsed, crushing vehicles and trapping their occupants. Mary and her children were on that freeway. This is their story.

Excerpt from In the Marvelous Dimension by Kate Daniels
```

### Performance text (classify this)

```text
(Mary)
I picked the kids up
at 4:45, as usual.
As usual, they were antsy
and fighting. Rose tore a hole
in her new knee socks
kicking Justin in the backseat.
Timmy sucked his thumb in the corner.
Then Justin wailed at another
abuse from Rose and I was just about
to yell, Goddamnit, shut up for once,
when the whole thing went. I mean
the whole thing, the whole world,
I thought.

(Mary)
Goddamnit, shut up for once . . .
The car tilted, the road
buckled up and then something was falling
down on us with a horrible screaming.
I guess I stopped driving and turned
to my children with a face of horror.
I reached past the seatbelt for Timmy,
my baby, and that's when it hit us.
My hand, pressed by the roof, pinned
his leg to the seat and he screamed.
Blood flowed down. Rose, my sweet
little Rose, was already gone.
I couldn't find her beneath
the bulged-down roof. Justin and Timmy,
they looked to me. They didn't understand
I was not in charge. I'd always been
their only God. They looked to me.
They wanted me to lift them up
and wipe them clean, to mend
with tenderness their shattered bodies.
But I was pinned in place. Blood
started seeping from Justin's
mouth. Timmy never spoke again.
And then I knew everything: how we
were going to die and how it didn't
really matter in the scheme of things.
My babies' suffering wouldn't matter.
It was a board game of gigantic
proportions. Our tokens
had been shaken out on the playing board
at 5:04 pm on the 17th of October
in the year of our Lord, 1989.

My baby was the last
one to go. And the last
shall be first. I hope
it's true. My children
dead around me,
I couldn't think of anything to do
but sing the lullabies I sang
when they were infants in their cradles

(Insert lullaby lyrics here singing) You are my sunshine . . . my only sunshine You make me happy when skies are gray and I was sending them away to oblivion for the night.

(Unknown)
I couldn't believe it
when I heard this little voice
singing.
You’ll never know dear, how much I love you
Please don’t take my sunshine away.
The voice was coming from a dark blue
Toyota squashed almost flat.
When I shone the flash over it,
I could see the dark pool of blood
beneath. In the dark, I could
smell it. I yelled out, Ma'am-
I'm here to help you, and the song
stopped for a moment. Then a voice,
not little at all, harder than any
I've ever heard, said from deep in the wreck,
You might as well go away. Nobody
can ever help me again.

(Mary)
People have actually asked me
what I thought about in there,
if I figured I would get out,
if I knew the children were dead.
The answer is: when I knew
the children were dead, I didn't want
to get out, couldn't get out
anyway. I was in there
forever with my three little lambs,
the smell of their blood,
and their dead faces, filled with questions,
looking at me.

It suddenly struck me that I believed the unbelievable.

The freeway had apparently
fallen down on top of us.
My children were dead
and dying. My head was locked
into position to watch that.
The only way to not see
was to close my eyes.
But my baby lived
a long time, I think.
I had to look at him
as long as he survived,
to say those things that mothers
say, It's OK, Mama's here, it will be
all right. All the while
I was not exactly remembering
my past, but feeling
the future. It had a shape now.
I knew what I was doing
and what I believed.
I was watching
all three of my children
die. More than ever
before I believed
in God. He was there
in that car. He caused
it, He saw it. And when
it was over, He'd gotten
what He wanted.
One more fearful
citizen bowed down
and kissed His feet.
And then, goddamnit,
I led my babies right up.
I put their little hands
in His, and delivered them over
for eternity to Him.

(Unknown)
I was at the sink
and drinking my second cup
of coffee when the story
about that woman and her three
dead children came on the news.
I screamed
when I heard it, the saw
and all. How they had to
blindfold her, what they told her
they were doing.
I screamed about this world
men built.

(Mary)
I never went to college
but I know now there's something
more than this world we see.
Trapped in that car, I felt it
when Timmy, Rose, and Justin
expired. They just left, and for awhile
I went with them. We eased
right out of that wreck
and floated in a void
-- a marvelous dimension –
like big flecks of ash
freed from a fire.
That's why it didn't matter
when they took their bodies.

They had left them already, and were part of me again, as they were to begin with, making me bigger.

Their father came over
from the city for the funeral.
He was drunk and terrified
to look at me. I wasn't drunk
and I wasn't scared. People looked
at me like I was a monster -- dry
eyed and calm. But if they'd
touched me, they would have known:
hard as metal on the outside, empty
as a suit of armor within.

(Unknown)
I can't imagine
going through that.
Can you? Watching
your own kids die.
Life
could never be the same,
could it? How
could you bear it? How
could you live?

(Mary)
I live somewhere else
now. With them. It's not
in space, not
in time. It's pure
feeling, spread out
like jelly on a warm piece
of bread, sinking down
out of sight, the sweetness
still there, sodden
and hidden.

(Unknown)
Those newscasters
stood in front of the freeway
and broadcast their pithy little
stories every evening while people
were dying inside. Now that's
my definition of indecent.

(Mary)
A preacher came to see me afterwards.
He asked me not to be
so angry, to forgive God,
to try to see it as part
of a plan I could not understand.
I just looked at him and he saw something
in my eyes that scared him: those three
little babies, frightened as bunnies. I can't imagine
your pain, he finally said. I wouldn't try to.
Can your affliction bring you closer
to Christ? Can you be with Him
in your suffering? And then I did something
I'll never regret: I laughed
in his face, I brayed like a donkey.

(Unknown)
Like everyone else, I watched it
on television for three straight days.
There was nothing a person like me
could do. The twentieth century
caved in finally. The earth
taught cement a permanent
lesson. Now, it's not
that I'm phobic. It's just
that I've seen postmodern light.
We're all insane
to live this way.

(?)
The earth settled.
The waters calmed.
The planet twirled in the heavens
unconcernedly
again.

(Mary)
When the priest raises
the pale white Host
something really does
happen if you want
to believe. If you don't,
it might still happen
anyway. Right?
Your past wiped out
by the force of the mystery.
The future emerging
from one huge moment . . .

Once, at a student play
in seventh grade,
the whole backdrop collapsed
with the wheezy singing
of nails being forced
from cheap wood. Frayed ropes
dangling like live snakes
and sawdust rising in a smoky haze.
When the scene settled,
Reality was where
it had always been:
right there, lurking
behind the drapes:
a cinderblock wall
painted pale green and a red door
marked Emergency Exit chained shut.
For once, nothing
but an empty stage separated
me from It. I was
It, and It was this:
several million tons of concrete roadway
and steel beams smashed
down on top of
approximately 274 live human beings
when the San Andreas Fault flexed a tiny muscle.
39 died, including my children. I
survived. Hundreds
took part in the rescue effort.
The rest of you -- Christ
have mercy -- watched on TV.

The red door
was chained shut.
We went through it
anyway.
```

---

## IC-1811: It’s About Transformation

- Title: It’s About Transformation
- Author (byline): Not specified
- Work: Word Warriors, Pgs 340-350
- Publisher: Seal Press
- Publication date as stated: Oct 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1226
- Already set (do not supply): none

### Source block (context only)

```text
Author: Turiya Autry and Walidah Imarisha
Book: Word Warriors, Pgs 340-350
ISBN: 978-1580052214
Publisher: Seal Press
Date (Month/Year): Oct 2007
```

### Introduction (context only: never use it for content warnings)

```text
Spoken Word poets Turiya Autry and Walildah Imarisha create magic with their voices -- anthems, alive with rhythm, fire, and unapologetic pride. They call out the myths and stereotypes placed on Black women and replace them with voices that demand to be heard, seen, and celebrated.

This performance of their poetry isn’t about entertainment, it’s about transformation.

Supa Soul Sistas and No You Don’t Know Me by Turiya Autry and Walidah Imarisha
```

### Performance text (classify this)

```text
Imarisha (aka Good Sista/Bad Sista)

Supa Soul Sistas (Pgs 340-345)

i always wanted to be a superhero marvel comic book
character
action packed thrill a minute type of girl
just hug my curves and hold your breath

but i'd do it with a twist, cause i didn't want to be no wonder woman or bionic woman and i definitely didn't want to be invisible woman (I did that every day)

no, i wanted to be a black female superhero
kicking a** and looking damn good
i wanted to be storm from the x-men
command the elements with a single thought
shake entire continents with my wrath
and quiet the fiercest monsoons

i used to wish to be storm
so when some stupid *person*
asked me why i was so angry
my eyes would widen
with the awesome power of nature

i would raise my hands above my head
power pulsating in between my fingertips
i would make the sky darken and rumble my answer
and then from the bowels of the clouds
a lightning bolt would flash

i knew then that no known image of black women,
created by white men
(of course)
could satisfy my longing to be a superhero
i would have to figure it out for myself
i would have to make myself over into . . .

a supa sooooooulllllll sista!

that's right the white man will not be saving the universe this time not Willis, not Schwarzenegger, not Ash Ketchum, and not that bratty whiny Skywalker

instead the next superhero is a sister
and not the generic, ratings are going down
we need something to perk up the show
safeway select of superheroes
generic brand of freedom fighter

no, this will be a sister who can fly above the chains of ignorance and whip out the tongue lashing of a lifetime

"you think you know me?
i call upon the forces of Isis and Harriet Tubman
Sojourner Truth and Nefertiti
Assata Shakur and Cleopatra
to reign down the fury of centuries of oppression
degradation and silence on your head
because we will not be silent anymore

or maybe my power would be held captive trapped like an angry storm cloud whipping out of my

head
my hair would rise up around me like a cobra's hood
spitting venom and years of pent up frustration
of not good enough, not light enough, not white enough
and you can touch it if you want to
but I can't be responsible for the consequences!
instead,
i'll be responsible for conquering corporate dominance
ending racial profiling with a swift crackdown
coming soon to a theater
(and streets) in your town!
then I can tap into my special super empathy powered
third eye . . .
and I . . .
sense. . .
racism nearby . . .

damn, girl, that ain't a super power that's just simple common sense!

you're right! every black woman action figure or not comes equipped with that option

KAPOW

take that for slavery

and that's for segregation and that's for integration

that's for the glass ceiling
and that's for that futuristic movie
where i am still Aunt Jemima
talking bout "have a cookie and you'll feel better"
and this is for my not ever being able to find
flesh colored pantyhose
or my hair care products at the corner store

KABLAM!

knocked that smirk right off the face of patriarchy rewrote history and started my own galaxy beyond the silver surfer's reach cause you know he be trying to gentrify that s*** and no the chief of police can't page us with a strobe light shaped like an afro pick shining on the night's sky Charlie won't be on the intercom and if he tries to page us tell him we've decided to stop moonlighting as angels cause we've come down to earth and pawned our wings

cause we are Supa Soooooooullll Sistas and you just found your way onto the bad side of our hair

No You Don’t Know Me (Pgs 345-350)

Black folks Woman

Colored Women

African American I am

Black We are

Mulatto Names

Darkie Titles

Mammy Assigned

High Yella But who are we

Jezebel Really?

N****

People are always trying to categorize us, demystify us. Flatten us and straighten us and define us our parameters. But they really don't have a clue.

Don't I know you? You look so familiar!

No you don't know me! I didn't used to sit next to you in second period math class I wasn't friends with your second cousin's best friend And no you didn't see me on Soul Train But thanks for asking

Black

I am the universe before the stars

Fertile chamber of things to come

Buried secrets

Deep beneath the ground

Deep beneath the deck of slave ships named jesus

We multiply and reproduce

A mass movement coming from the underground

Grassroots taking over the landscape

We clone ourselves in preparation for the slave

insurrection

Do you get confused when More than one black person enters the room?

Colored

I am muted brown

Child of Ham

Searching for a sign

To point me in

The right direction

But that path is labeled whites only.

How can you know me when you're afraid to get

close to me?

Is it a genetic drift
That pushes you
To the other side of the elevator every time I get on?
If you think you're scared now, you should hear what we

say when you're not around . . .

You know, Portland is the whitest major city in amerika We used to be number two but now Omaha has that honor! Moving on up! (Moving on down!)

Surrounded

Don't get me wrong . . .

Trapped behind every lines

I'm not a racist . . .

Closing in from all sides

I mean some of my best friends are . . .

May day! May day! This is not a drill!

I repeat this is not a drill

This is reality!

It's just that every once in a while We would like to get away! I mean, they even show up at reggae shows! Bomba Clot!

We may be only 3 percent of Oregon's population But goddamnit, we're taking over!!!

We don't have any smiles for you today
We're throwing in our masks
We're not going to steppin fetchit for you anymore
The minstrel show is over!

And for as much as we remain silent with our thoughts, Seems like white folks don't have problems expressing

what they think:

It's not like you're black; it's more like you're white . . .

Oh you speak so well!

You're so lucky. It's like you have a year round tan!

You're so angry. Why are you so gosh darn angry?

Can I touch your hair?!

HELL NO!!!!!!!!!!!!!!!!!!!

Tonight on the six o'clock news
An epidemic of jungle fever is running rampant
Spreading throughout the nation
Causing white boys to get pretty bold!

You know, white girls just don't do it for me.

I don't know why.

I don't date anything lighter than a cinnamon.

Baby, can I get some of your brown suga?

Interracial relationships
From the slave quarters to the big screen
Wasn't part of Martin's "I Have a Dream"
Look, Black isn't some two-hour movie
Starring Oscar award winning performances
Or some thirty-minute laugh track sitcom
Where widened grins mask our suffering.

We are more than MTV personifications twenty-first-century reinterpretations of slave plantations

Forget everything Good Times ever taught you About black folks:

DYNOMITE!
And just listen . . . really listen
So when you say that you "know me"
You can say it with honesty.
```

---

## IC-1812: Jocasta

- Title: Jocasta
- Author (byline): Ruth F. Eisenberg
- Work: Angles of Vision: An Introduction to Literature (Biddle, Arthur W. and Fulwiler, Tony (eds).
- Publisher: McGraw-Hill
- Publication date as stated: Dec 1991
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2305
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ruth F. Eisenberg
Book: Angles of Vision: An Introduction to Literature
(Biddle, Arthur W. and Fulwiler, Tony (eds).
ISBN: 978-0070052147
Publisher: McGraw-Hill
Date (Month/Year): Dec 1991
```

### Introduction (context only: never use it for content warnings)

```text
Laius and Jocasta were king and queen of Thebes, a town in Greece. Laius received an oracle from Delphi which told him that he must not have a child with his wife, or the child would kill him. One night, however, a drunken Laius disregarded the prediction and soon a son was born. To thwart the prophecy, Laius and Jocasta decided to kill their baby. In those days, it was usual to leave an unwanted or defective baby in the wilderness. Laius ordered the baby, Oedipus, to have his feet pierced and to be exposed on Mount Cithaeron. A kindly shepherd, hearing the child’s cries, rescued him and took the baby to King Polybus and Queen Merope of Corinth who raised him to adulthood. The rest as they say is history . . . Greek history . . . but only from the male perspective. In Jocasta by Ruth F. Eisenberg
```

### Performance text (classify this)

```text
we delve into the story from the viewpoint of wife, mother and mortal sinner.

I When she learned the king’s power,

Jocasta lost delight in being queen.

Laius was a cold, dry man. Looking at him
brought the image of her baby, his feet
pierced and bound, her baby left to die
on the mountain slope. They would
have no other children.

I remember Laius drunk that night, crying For Chrysippus, the source of his curse. Wanting his boy, he took me instead and threw me on my back to have his way. I am fifteen and afraid to resist and tell myself it is my husband’s right; the gods decree a wife obey her spouse.

Sober, Laius recalls Apollo’s threat:
Our son will kill him, beget upon me.
Nine months drag like oxen ploughing.
With icy eyes Laius watches me swell.
I fear the gods and beg Hera, for a girl,
but as foretold, I give birth to a son.
Laius takes the child to bind its feet.
The baby cries, and Laius turns away.
He summons a servant and orders me to hand
my baby over, threatening me when I cry.
The king will keep his own hands clean.

At the public altar, Laius

offered bulls and lambs in ritual
slaughter. The everburning fire raged
so the offerings charred, and Jocasta
trembled at the gods’ displeasure.

Upon the gates this dawn, a strange creature appeared and woke all Thebes. In raucous voice She cried, “A riddle. Who’ll solve my riddle?”

At first our people came to gawk, then marvel. Some trembled, children hid their heads and cried. I’ve heard old tales the minstrels sing of her, but never did expect to really see a Sphinx – part woman, bird, and lion too . . . And what she asks is strange as well: four legs, then two, then three. What can it be? No one

The Sphinx brought pestilence and

drought. Rivers and streams ran dry, vines
shriveled. But until her riddle was solved,
the creature would not leave. On the gates
she stayed, her destructive song echoing
from empty walls.

My life is a toad. All day and all night The Sphinx. We cannot escape her song. Song! More like wail or whine or scream. Laius is useless as always. Deceitful man, I hate him, hate his touch.

The land is parched; flocks die. Our people haggard, starving, plead to ease their distress. What can we do? Mortals cannot make the rain. I suggest Laius seek Apollo’s help. To get away, he welcomes the idea to go to Delphi and proclaims a pilgrimage.

On the sunswept road to Delphi,

Laius was killed. The servant reporting
the death begged Jocasta to let him tend
flocks in the hills. Sending him on his way,
She shut herself in the place.

The prophesy was false. How can that be if gods control all things? For surely chance does not . . . No, no. Yet Laius killed our son and not the other way. That sin diseased his soul. I bless the gods that I, at last am free.

I dream of my baby night after night. He is dancing for the gods with bound feet. I do not understand how he can dance so. When he jumps, he trips, falling in a heap. The gods just laugh and turn away to drink. I sit raveling knots. The knots become rope. I wake shaking and muffle my tears in the sheets.

II

“Man” answered the young stranger

whose red hair caught the sun’s rays,
and the riddle was solved. True to her
promise, the Sphinx dashed herself to
death. Thebes was free.

Hailing their hero, the people

elected Oedipus king. Gratefully, he accepted the rule and with it the hand of Thebes’ queen, Jocasta.

I see young Oedipus in radiant sunlight, Apollo blinding me to all but young and vital strength. Deep in myself I feel a pulsebeat, something asleep begins to wake, as though a dormant seed sends up a shoot, opens a leaf. That’s how Aphrodite touches me. I love this youth. My sun, I rise to him and rise with him.

From a land of rock and misery, Thebes

became a bower. Brilliant poppies dotted the land. The wells filled, crops flourished, and the flocks grew fat again.

Before the people’s eyes, Jocasta

became young. Her dark hair gleamed, her eye was bright and her laughter cheered the halls of the palace.

Oedipus has become my Apollo warming my days and nights. I am eighteen again with poppies in my hair. I am the poppies, bright little blooms with milk in them. Like them, I seem to spring from rocky ground. Like their color and his hair, our love flames.

Sweet Aphrodite, you rush through me, a stream until you burst like foam that crests the sea. your blessing washes what was once a barren ground. I walk among the roses, feel your blush upon my cheeks. Oh lovely goddess, I send you swans and doves.

Thebes prospered these years:

The gnarled olive bent lower with fruit.

Lambs frisked in the fields and pipers’
songs rang through the hills. Jocasta had
four children. Psalms of joy were sung
and danced for the gods.

With four children, the hours run away. Their hunger, games and tears take all my time. In bed, with Oedipus, I sleep in peace. He was at first my headstrong bull, but now he is what a man, a king, should be.

I like to see him walking in the yard, his funny stiff gait, his hair burnished by Apollo’s brilliant rays.

Mine turns gray but he doesn’t seem to mind. Our love has brought to me the joy I missed when I was young and thought I’d never know.

At last, I lay to rest my little boy, his shadow vanished now from all my dreams.

III Years of plenty at an end, Thebes

was inflicted with drought. The earth burned as crops withered, cattle and sheep sickened.

While days were once too short, now each one drags A slow furrow, the earth heavy with heat, Lament and prayer. When I go the fields The women clutch my gown and plead my help. Too many children sicken. The healthy droop. At home, the girls sit listless, my sons tangle While Oedipus complains his ankles twinge. He limps and growls just like a wounded pup.

Jocasta, very gray now, walked

With a more measured step. More than A loving wife, she was also counselor To Oedipus.

Blaming himself because the land is parched, Oedipus frets alarmed he’s failed the gods In some unknown way, searching within himself. In turn, I pray, lighting fire after fire, But none burn true. I call on Aphrodite And offer her doves, but they flap their wings And peck each others’ eyes. When I ask Apollo To dim his eye, his answer scalds.

No relief at hand, Oedipus sought

Aid from Delphi. The report came back A confusing riddle about Laius’ death.

Suspecting treason, Oedipus feared Conspiracy against his own throne.

Oedipus needs someone to blame. He calls Creon traitor, Tiresias false seer. I take him in my arms and stroke his hair. He tells me what Tiresias has foreseen.

I laugh and tell him I too once believed That prophesy controlled our lives, that seers Had magic vision the rest of us did not. I tell the story of Laius, how it Was foretold he would die at his son’s hand And how that baby died when one week old.

As I speak I feel so strange, as though my tale Came from another life about someone else.

My words do not comfort, they flame new fears. He relates what drove him from home, tales that he Would kill his father and bring rank fruit from his mother’s womb. He fears he has been cursed. Dear gods, how can I comfort him?

IV

From Corinth, a messenger

Brought news of Polybus’ death, The king whom Oedipus called father.

You say that Polybus is dead. Dar I Greet death with joy? Can that be blasphemy?

My heart flies into song: His father’s dead – My Oedipus lives safe. Hi sprophesy Is false. Is false as Laius’ was. Oh bless Your fate, dear love, you need no longer fear.

Corinth wished Oedipus to return

And rule. Fearing he would sleep with
His mother, Oedipus refused. Nothing
To fear, the messenger assured. Merope
Was a barren woman.

Jocasta began to tremble. Her hands

Rose to cover her mouth.

What’s this? What’s this? What words do I hear? How can I shut his silly mouth, tell him Go. Leave. We will not heed your words. My tongue stops, rooted in my mouth. I look at Oedipus. He does not see Me watching him. His face is strained, his eyes Are glaring blue. I try to stop the questions. “Oedipus, I beg you, do no hear this out.”

When Oedipus insisted, the

Messenger told the story of the king’s
Infancy – how he, a shepherd then,
Had helped to save the king’s life
When a baby, a baby with bound feet

Oh God. Oh cold, gold God. Apollo, You chill me. My mind is ice, and I hear My mouth say freezing words to Oedipus. To my husband. My Son. “God keep you from The knowledge of who you are. Unhappy, Oedipus, my poor, damned Oedipus, That is all I can call you, and the last thing I shall ever call you.”

V

Her face ashen, Jocasta rushed

Into the palace, her hands showing her The way to her own quarters. She Ordered the guards to let no one in.

Ignoring all offers of help, she commanded Her women to leave her alone.

I can’t believe. I can’t believe. Oh God. He is my son. I’ve loved my son but not As mother should, but in my bed, in me. All that I loved the most, his youth that made Our love the summer sun, wrong, all wrong. Vile. He caressed me here and here. And I Returned his touch. Odious hands. My flesh Crawls with worms.

My God, we’ve had four children.

In her chamber, she looked at her

Bed, sat on it, then jumped up as though
Stung. Covering her eyes with her hands,
She shook her head back and forth, again
And again, her body rocking.

Oh, Oedipus, what good was our love if It comes only to shame? To children whom All Thebes can curse? Such children, even ours, Are rightly damned.

Although we could not know who we were And loved in innocence, still we are monsters In the eyes of god and man. Our names will mean Disgrace and guilt forever.

Walking to her dressing table,

She stood before it picking up small
Objects: combs, a gold box, a pair of
brooches. Noticing a bracelet given her
by her father when she was a bride,
she let forth a dreadful groan.

Oh Laius, Laius, you brought this on me. My fate was sealed my wedding day. Chrysippus Was innocent as I; for you this curse Was uttered, a curse that falls on me. Oh, That I must bear the shame, that I must be Destroyed by your corruption. And our son, Because you sinned, is ruined, damned.

My marriage day . . . what choices did I have? As many as the night you came to me. The only choice a woman has is that she wed accepting what the gods and men decree. It is not just. It never can be right.

Moving decisively, she walked to the

doors and bolted them, straining against
their heavy weight. The women on the other
side called to her, but again she bade them
go away.

Falling on her knees, she pummeled

her stomach as though to punish her
womb. As she did, she called her child-
ren’s names, one name, Oedipus, again
and again.

I thought him buried, forgotten. But no, for countless days and nights these many years he’s thrust himself on me instead. My bed once stained with birthing blood is now forever stained; what once was love become a rank corruption.

Rising painfully, sore, she turned

to the small altar in her chamber.

Smashing a jar which held incense, she began in a voice of char to call on Apollo and Aphrodite.

As she raised her eyes, she raised

her fist and shook it against the silent air.

Apollo, you blinded me to his scars, His age, any resemblance to Laius. And you, Aphrodite, cruel sister of the sun, Set my woman’s body afire, matching my Ripe years and hungers with his youth and strength. Paralyzing my mind, you inflamed my heart.

The years I prayed to you and praised you Were all charade. You so enjoyed my dance. We are your fools to trifle with, your joke.

We tremble to question what the future holds. As though it matters, we think asking will spoil Our luck, but your injustice mocks all hope.

I hear a change pounding inside my head. Five babies. Five abominations. As though a chorus raises call to prayer. Five babies. Five abominations.

No call to prayer. It is a call to curse The gods. No longer will I be their fool.

From her robe, she removed her

Braided belt. As she looped its strands,
She heard, from the courtyard, a man’s
Voice scream in anguish. Undeflected, she
Tied the necessary knots, slipping the loop
Back and forth. Satisfied, she settled
The noose around her neck.

Five babies cursed by heavenly whim, Cursed in their lives without chance or hope, Mothers ought not love their children so.

Gathering her skirts, she climbed Up on the stool.

And wives be more than merely bedside pawns. Those who cannot shape their lives are better Dead.

She stepped onto the air.
```

---

## IC-1813: Kitchen Talk and Black Ice

- Title: Kitchen Talk and Black Ice
- Author (byline): Jessica Care Moore
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 944
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jessica Care Moore
Book: The Alphabet Versus the Ghetto
ISBN: 978-0965830874
Publisher: Moore Black Press
Date (Month/Year): June 2003
Author: Jessica Care Moore
PoemHunter.com
(An NSDA Approved website for interp)
https://www.poemhunter.com/poem/kitchen-talk-2/
https://www.poemhunter.com/poem/black-ice-5/
```

### Introduction (context only: never use it for content warnings)

```text
Black women are often invisible in American public life―and even when they’re seen, they’re not heard. But one poet is challenging the status quo. No longer will black girls face a symbolic silent death. They have a collective voice in Jessica Care Moore - an internationally known poet, publisher, performer and artist who has found her voice. It rings out strong and true – showing black girls everywhere how to live.

Black Ice and Kitchen Talk by Jessica Care Moore
```

### Performance text (classify this)

```text
(Pronounced JE-si-kah Care MOOR)

. . . black girls are dying Because no one showed them how to live . . .

(From Warriors Walk Alone)

Kitchen talk

we cook with ntozakes recipes
we weave word quilts
we hide our stories inside our belly
we are the soft place language breathes before it's
pushed into sound
we are the whisper in the hush of crowds
we read eyes
we are warriors traveling without fear
or are we just a myth?
maybe black girls don't really exist at all
perhaps we are the vicious rumor
circling at the center of twice bitten snakes
maybe our mommas never taught us to bake
and this is the ancient secret that will save the world
that some black women can't fry chicken
or barefoot and pregnant is okay
if your husband paints your toes & pours your tea
we are the lie of rape the molestation of memory
creeping into our subconscious when someone says
he loves you after you've fallen out of love with him
or maybe this life is all just a fairy tale
and ndambi's little girl blue is the truth
cause words have hurt me deeper than any
blunt object or bullet chasing me down a detroit street
hell, we can duck or out run the hot steel
I'd rather pull a fast approaching word out from the air
and make your whole body stand still
make worship what you will
I wish for simplicity in moments
pray they'll understand why after six years
you still need to hear them to say how they feel
why you pretend to not put your pride
in the way of your walk
why your hair grease fried those eggs
& the last dollar to your name bought a sunflower
cause you are collecting dirt under your nails
and taking wolf dancing classes on Friday nights
anything but serve the ones who refuse to praise you
who defecated on your grandmommas spirit
the smell follows us, but our noses have fallen off
or we have carved them up to take a better picture
still, we flip the pans and draw blood for aunt jemima
tomorrow morning, we will promise to protest the sun
we will beg for the night to save us & do cartwheels with
angels
who know damn well, our wings are still in the shop
but if you just give us some time - we will recover
like a child growing in her sleep, we are wiser after we
dream of being
awake . . .

TRANSITION Awake and wiser . . . black women have grown in the proverbial silence. Today 19 black women serve in the US House of Representatives, ensuring that the voice of black women in America will be heard. But still there are challenges to be faced. A storm is brewing with a strong possibility of . . . . Black Ice.

Black Ice

we slippery, invisible
our freedom is frozen
cracking like leather whips
under your feet

there is a winter weather advisory
in the south
they are running
out of salt!

there is a police radio advisory
in the south
they are running
out of cotton!

no more fabric to support the confederate so now the black kids can't wear fubu to school let's design a nation from red dye and yellow # 5 let's teach the children how to lie let's make the truth real hard to find

there is a fire storm advisory
in the south
they are running!!!
out of reasons
to burn the books and wave the flags
we can't walk through the snow
when icicles dance inside our shoes
that's why daddy always seemed so cool
why the hot comb burns were a rights of passage
why god allows rain to turn to acid
& devils night fires never burned down my crib
why a summer longing never forgets the winters end

there is a thunderstorm warning in the south

they are running!!!
out of water
to blast the fish people on the street
the niggas have turned to mermaids
their blood is a river of riots swimming
inside the sidewalk
bits of salt - blood fill the city ocean
the urban middle passage
laced with stolen beats & mtv pocketbooks
there is a starvation alert
in the south
black mothers are running
out of spices, salt, and water
they cannot cook and their sons are dying
they have greens to clean and they don't own any grass
their daughters are being born, already raped
innocence was exchanged for their eyes
so now they can't see themselves in the future
today an estimated one million blind black girls
are afraid to leave their block

there is a tornado warning in the south black people are running!!!

in circles at the speed of light
twistin' and shoutin' and dancin'
around the death penalty
genocide is leveling the homes
of the black middle class
the ghetto is no longer a geographic location
the deaf wind is flying into our naive right ear
and out the liberal liars left
you think hiding in the basement
behind velvet rope couches
will save you new niggas?
there is a national time warning
in the south, black people are
running backward
sankofa style, moon walking
with dry sticks burning their palms
toward their forever chriogenic history
5-year olds are hitting their teachers in the head
with rubber bands and demanding african centered
curriculums
in all public schools
in detroit, south africa, medina green, oakland
in atlanta, chicago, harlem, the children of brazil
are running for shelter

we are running in search of an unbetrayed earth
we are running from the weather our ancestors created
and we still haven't found a safe place
to drive down 85 south
without sliding on our elusive legacy
hiding inside patches

of invisible black ice
```

---

## IC-1814: The Last Goodbye

- Title: The Last Goodbye
- Author (byline): Maria Williams
- Work: Not specified
- Publisher: Poetry Soup.com
- Publication date as stated: January 14, 2024
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1091
- Already set (do not supply): none

### Source block (context only)

```text
Author: Maria Williams
Website:
https://www.poetrysoup.com/poem/the_last_goodbye_1616287
ISBN: Published On-line
Publisher: Poetry Soup.com
Date (Month/Year): January 14, 2024
Written for the Poetry Contest: Titanic - Fare Thee
Well sponsored by Tom Woody
```

### Introduction (context only: never use it for content warnings)

```text
An iceberg was spotted around 11:30 pm on April 14th, 1912. The great Titanic turned course and appeared to graze past, but in reality, the mighty vessel had sustained great damage from below.

The ship began its 2-hour and 40-minute descent to the bottom of the ocean while Catherine penned . . .

The Last Goodbye, a narrative poem by Australian poet Maria Williams
```

### Performance text (classify this)

```text
15th April 1912 My dearest Charles,

I am writing you this letter in the cold, early morning hours.

By tomorrow, you will be reading about the most luxurious ocean liner, Titanic, lying in a wreck at the bottom of the ocean. Meeting its doom in the merciless greed of the icy waters, sucking it slowly, savouring every trinket, devouring jewels and rare gems, gold-rimmed crockery, crystal glasses and decanters, fine silk couture and expensive leather boots.

My dearest, I can only imagine how horrified you will feel reading all this and how you will go through this depressive state of blaming yourself. Can I beg you not to, PLEASE?

When I heard the first distress horn, I had hoped it was only minor. However, as I watch, I realise the problem is far more severe.

An hour has passed, and I see families cling to each other, crying. Crew members rush around, trying to calm and reassure us that help is coming, instructing us to form lines.

In their panicked state, passengers heedlessly jostle and push, adding to the chaos. Lifeboats are lowered, and orders bellowed.

In their attempts to give first-class passengers preference, fights break out. Social status and wealth are now immaterial as illusions of grandeur dissolve in panic.

Brave young boys and men allow their sisters, wives, mothers, and elderly to use the first lifeboats that row away alarmingly quickly.

Passengers hurrying past glance strangely at me writing this letter. Perhaps I am still in denial. Yet I cannot fathom how this perfectly engineered, unsinkable masterpiece can do such a mundane thing as sink.

Remember how we excitedly followed the news of its progress over the months in the making, Charles? Something that hadn't been considered was striking an iceberg.

I must admit the hysteria, startling explosions, followed by shooting flames and fires breaking out amid the distress horns blaring, are frightening me out of my wits. The gravity of the situation hits home as I watch horrified people jumping into the icy ocean.

I read somewhere that in icy conditions, hypothermia sets in about fifteen minutes and death in about thirty. I shudder to imagine the fate of the poor souls in the water. They would be frozen in this cold North Atlantic water quicker than they know.

One poor woman has even strapped her child to her waist, suckling at her breast as she jumps.

The liner is belching out volumes of black smoke. It is in stress and tilt mode, making it hard to write and even harder to see my writing under the flickering light as I cling to my paper and pen. All the while, the ship is mournfully shuddering, groaning and sinking.

People scream as things start to break off and slide towards the ocean. I strap myself in the chair. I watch a man get hit on his head by a monstrous metal pole dead before he even hits the deck, his wife screaming, holding on to him. All this, I watch from my chair the horrific events unfolding.

Some passengers cling to each other, others strap themselves to anything anchored, and some hopefuls point to a ship far away, comforting, hoping and praying aloud.

Ominous as it sounds, Charles, I know it won't get here in time for the unfortunates in the water. I try not to look at them. All the lifeboats have gone, some only half-filled. I say a prayer that they make it.

Charles, you are my rock; a year ago, to the day when Billy passed from a strange and sudden illness, I wished for my own death. It took on your part to pull me out of my own selfish depth of despair. I found myself very slowly, over the months of patience and love from you, gradually adjusting to the fact that life goes on. I wanted to live again. Eager to unshackle chains to the addiction of pain, I slowly emerged as my old self under your care, stronger. You put your own feelings on hold to help me through it all. I have never loved you more than I do now.

You convinced me to take this cruise of a lifetime, spending your hard-earned money on a first-class ticket for me, a luxury we could hardly afford. Still, in your unselfish way, you insisted, and as the idea grew on me, I eagerly looked forward to the cruise and meeting up with my sister in New York.

After sitting here for nearly two hours, watching, writing, and waiting, I realise that help will not get here in time for us. I should feel gloomy, but I feel an eerie calm prevalent in the air descending.

Is it Divine Intervention?

I look around at some of the other passengers.

They sense it, too. It seems we are all resigning ourselves to our outcome. Que Sera, Sera

Looking at my clothes, I realise I am well and truly drenched. My boots soaked right through, yet oddly, I feel warmth like a gentle caress embracing me as the haunting strains of the music 'Nearer my God to Thee' float to my ears.

Throughout this whole ordeal, the brave musicians have played their soulful music. One has even strapped his instrument to his chest.

I look up at the sky. My God, Charles, I have never seen the stars sparkle so brightly,

They seem to be unpicking seams as they burst through the canopy of black velvet folds. What a celestial show they are putting on as they watch us face our miserable outcome, Or is it?

Puzzling as it seems, my heart fills with peaceful joy. I don't fear death's cold embrace anymore.

Unexpectedly, the warmth of a small hand slips into mine; I feel him before seeing his bright light twirling and spinning, getting larger before my eyes, gaining momentum by the second.

Oh, Charles, it is Billy; it is our son.

How can it not be?

Though lost to mortal sight, believe it, he is here, a manifestation of love. A beacon of Hope with a promise of a sanctuary beyond The love I feel cannot be described.

Eagerly, I reach for the metal flask. In it, I will slip this letter to you and toss it in the sea.

My love, my complete trust lies in it somehow finding its way to you.

From the depths of my heart, thank you for loving me and sending me home, Charles.

All my love till we meet again

Catherine
```

---

## IC-1815: Learning to Swim

- Title: Learning to Swim
- Author (byline): Ann Turner
- Work: Not specified
- Publisher: Scholastic, Inc.
- Publication date as stated: 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1174
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ann Turner
ISBN: 978-0439153096
Publisher: Scholastic, Inc.
Date (Month/Year): 2000
```

### Introduction (context only: never use it for content warnings)

```text
Summer --- an innocent time when little girls should be joyfully picking blueberries with their mothers, playing with their brothers, and learning to swim with their fathers. And those memories are there, but there are other memories too . . . memories of drowning, secrets, fear and finally . . . telling Learning to Swim by Ann Turner
```

### Performance text (classify this)

```text
We are packing the car
to go to the summerhouse
everything is in bits and pieces.
Nicky and I are fighting
over the seat but I
am not moving,
I am sitting on my pink
swimming ring that Daddy says
I don't need anymore
because I am big enough,
old enough,
and fast enough
to swim on my own.

Nicky and I climb down
the knobby path to Dresser's Pond.
Daddy holds my hand.
"Don't be afraid."
My pink swimming ring
on the grass
used to keep
the black water below.
Now I cannot see my toes
and flail my arms,
churn the water to a froth,
but the water tugs at me
willing me to go under.
Daddy shouts again, "You can do it!"

I kick my feet,
suck in a breath,
and for a moment,
I sail above
the drowned leaves!
We are running races
in the meadow
with the kids from down
the street -- Kevin, Lonny, Angie –
legs pumping,
hands swinging,
my feet blur
as I pull ahead of
everyone
my breath works
my heart works
my legs work
and I shout when I win.

Kevin, Lonny, and Angie all live
in a little green house
with a fat mother,
hair greasy in her face,
frying donuts,
and their father is thin
and shabby with an open mouth
shouting
we are runmng away
somehow I am always It
looking for a place to hide
from their feet and their hot
breath going by.

"I'll read to you,"
Kevin whispers,
"a secret time for us
and never, ever tell."
He takes my hand
and leads me up the stairs.
But in my hot, yellow room
the book falls to the floor
and he jams his hands
inside of me
and takes out his private parts
that I didn't ever know
could look so huge and strange,
telling me to touch him
in a hard, breathless voice,
and I didn't even know
I could say
no.

I tried to swim
today
thrashing in the water
but clouds covered the
sun there was no pink
ring to keep me safe,
and I could not keep my head
above water.
Daddy pulled me out,
thumped my back,
and said, "Next 'time,
Annie, next time."

It is happening again
your hand is out
holding mine
the book is in your other
hand
we are disappearing
up the stairs
and Peter waves to me
from his playpen.
He can't talk so he
can't tell
(I promised not to!)
and after it is all over
I whisper in his
baby ear
and push my face
into the couch cushions
so no one can see.

I am holding it all
inside like when I am sick
and running to find a bathroom
the words are crowding behind
my lips bursting to get out
so bad my lips ache
but I can't. You said no
not ever not nohow
and you bunched your fist
in my face.
But my dolls know,
Jenny, Amanda, and Fuchsia.
At night
I tell them what you did
and they are sad for me
with their wide-open eyes
and surprised mouths.

I tried to swim
today
thrashing in the water
but the clouds covered the
sun there was no pink
ring to keep me safe,
and I could not keep my head
above water.
Daddy pulled me out,
thumped my back,
and said, “Next time,
Annie, next time.”

I thought a secret was
a cookie hidden in a hand,
like the one you hold now
as you lead me up the stairs.
My feet drag
they know what is waiting
at the top
but I am too small
to say no
only my body is so
slow it is waiting
for someone to notice
I am going away.

"Come on, Annie, What’s wrong?" Daddy holds out his hand it is not like the other hand taking me away but still I will not go in. The water looks gloomy and dark with shadows I will be swallowed up the drowned leaves will cover my mouth. I ask for my ring back and sit on the grass.

I am scribbling
with a crayon
on a crinkly piece
of paper
you have a rain of fire
on your head
your arms are
stumps
your feet
burned off
when Mother asks,
"What is it, Annie?"
words flyaway
and she looks at me
with worried eyes.

She asked me today,
"What book does Kevin read
up in your room?"
My eyes blinked,
my tongue stuck
to the top of my mouth
on the words I'd been waiting
to say
each one hurt
like a splinter
yanked out
and before I was done
she grabbed me up and we cried
and cried
until
there were no more
words to tell.

Mother is jamming on
her walking shoes,
jerking the laces tight,
"Annie, stay here.
Kevin will never hurt you
again."
She slams out the
door but I am afraid
of the green house
the lips the hands and him.

I wait on the porch
watching
my stomach clenches in
until I see the top of her head
getting bigger, rounder
then all of her running up the drive
her short hair flying,
and when she holds me
her skin burns.

Daddy took my hands
today, swinging me high
over the hurting plants
in Grandma's rock garden
he settled me on his knee
his safe smell was all
around
and he told me he knew
that he was so sorry he would
drink up every bit of water in
Dresser's Pond if that would
make it all unhappen
it can't
every bit of water
is in my eyes
I sit on his warm lap
and put my head
under his chin.

Grandpa left me a letter
in the old knothole
by the stone pillars.
I reached in and pulled out
the note covered with blue
words:
"You are my fairy girl
with brown curls
and impish smile
and a laugh like a cloud."
For a moment
I felt like one - airy,
light as mist,
floating up the drive.

Daddy held my hand
as we scrambled down
the path to Dresser's Pond.
We waded in together,
and I thought of white, bony
things I could not see,
of a lake octopus waiting
to sucker its tentacles
around my skinny legs.
Daddy said,
"You are learning to swim,"
and I let go of his hand.
"I am learning to swim,"
I chanted
and when the bottom
fell away,
I bobbed on top,
my face like a white flower
before me.

Listen.
Telling is what matters,
You have to catch
the words you're been hiding
inside or keeping in a dark
hurting ball in the middle
of your stomach that make you
sick
but pulling the words up
and out, spilling them
across the floor, the table,
dropping them into someone’s
surprised face that
is what matters
and after this time
and the next one day
you will fee! so
light and airy
your stomach will
uncoil
your face
unclench
and you will fee!
Like yourself
again.
```

---

## IC-1816: Lessons We Learn as Women

- Title: Lessons We Learn as Women
- Author (byline): Amanda Lovelace, Clementine von
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1088
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amanda Lovelace
Book: The Witch Doesn’t Burn in This One
ISBN: 978-1449489427
Publisher: Andrews McMeel Publishing
Date (Month/Year): March 2018
Author: Sierra DeMulder
Book: The Bones Below
ISBN: 978-0984251537
Publisher: Write Bloody Publishing
Date (Month/Year): March 2010
Author: Clementine von Radics
ISBN: 978-1449479701
Publisher: Andrews McMeel Publishing
Date (Month/Year): April 2016
Author: Amanda Lovelace
Book: The Witch Doesn’t Burn in This One
ISBN: 978-1449489427
Publisher: Andrews McMeel Publishing
Date (Month/Year): March 2018
```

### Introduction (context only: never use it for content warnings)

```text
No woman’s experience is universal, yet the world somehow manages to teach women universal lessons. The world teaches women how to pretend. I have done it many times. I have done it when I have wanted to say something but decided that it would be too “unladylike” or too aggressive or come from my mouth as a female. And so I have let many things go, and have kept quiet. I have silenced my voice for the sole reason that I am female. Today, my voice will be heard along with the voices of Amanda Lovelace, Clementine von Radics and Sierra De Mulder in this collection of poetry I call Lessons we Learn as Women.
```

### Performance text (classify this)

```text
Radics and Sierra DeMulder

Some Destruction is Beautiful by Amanda
Lovelace
The ground --
it ignites
wherever
a woman’s
foot
comes down

& if you’re not careful,

the
very same
thing
could

happen to you --some destruction is beautiful

Paper Dolls by Sierra DeMulder

We are taught from the moment we leave our pink nurseries we are collapsible paper dolls: light to hold, easier to crumple. That as women, our worth lives secretly wrapped in lace and cotton panties, our fragility armored in pepper spray and mace. They say one in three women will be raped or sexually abused in their lifetime. I am one of three daughters. Imagine each victim is an acrobat. Her sanity, a balancing act. Our response is the unfailing safety net. We never expect to see her across the wire. You weren’t just violated, we tell her, you are an empty museum, a gutted monument to what used to hold so much worth. With best intentions we tell her to reclaim it, put a price tag on her rape and own it. Don’t stand too tall, don’t act too strong. We will name you denial. Come back when you are ready to crumble like your bones are made of chalk. You can only laugh cutely or cry beautifully, so cry beautifully. We will catch you.

We are calling it theft,
as if he could pluck open your ribs like cello strings,
pocket your breasts, steal what makes your heart
flutter
and tack its wings to his wall.
Some days you will feel dirty.
Some weeks you’ll remember how hard it is to breathe in
public,
but know this:
the person who did this to you is broken. Not you.
The person who did this to you is out there,
choking on the glass of his chest.
It is a windshield
and his heartbeat is a baseball bat:
regret this, regret this.
Nothing was stolen from you.
Your body is not a hand-me-down.
There is nothing that sits inside you holding your worth,
no locket that can be seen or touched,
fucked from your stomach to be left on concrete.
I know it’s hard to feel perfect
when you can’t tell an Adam’s apple from a fist.
Some ashtray of a man picked you to play his Eden
but I will not watch you collapse.

INTRODUCTION The 2nd lesson the world teaches women is to always see themselves through the eyes of men. If you’re too loud, the world says no man will put up with that. If you’re too quiet, men will be bored. Women can’t be too intelligent, or men will keep their distance. Women can’t be too much of anything. But they can’t be lacking in anything either. While men just strive to be decent, the world expects women to strive to be perfect. But you know what? Women can be loud, quiet, intelligent, strong and self-assured. This is the lesson we as women must teach our daughters . . . And let the teachings of the world be stilled.

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
Despite everything, I really believe people are good at
heart.

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

But I Owe Something to Myself Too by
Amanda Lovelace
this is
an overdue
love letter
to each
& every
woman
who walked
these fields
before me
&
made
the path
soft enough
for me to
walk through
to get to
the side
they could
never reach.
for that,
I owe you
so much.
--but I owe some things to myself, too.
```

---

## IC-1817: Lit (or: To the scientist I am not speaking to any more)

- Title: Lit (or: To the scientist I am not speaking to any more)
- Author (byline): Cristin O’Keefe Aptowicz
- Work: Dear Future Boyfriend
- Publisher: Wordsmith Press
- Publication date as stated: 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 690
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christin O’Keefe Aptowicz
Book: Dear Future Boyfriend
ISBN: 978-1893972346
Publisher: Wordsmith Press
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
It’s easy to make gender generalizations: Men are stubborn, women are clingy. Men love violent movies; women prefer romantic comedies. These are cultural clichés that are slowly changing, but there is still some tendency for men and women see the world and communicate differently. Research at the Ned Herrman Group suggests that most men are more predominately left-brained which means that their thinking style is more logical. They tend to focus on problem and solutions. Women, on the other hand, tend to be more right-brained, with an emphasis on communication and emotion. This left- or right-brain dominance affects all kinds of everyday interactions and exchanges. Cristin O’Keefe Aptowicz takes a look at this dichotomy from a woman’s perspective in Lit or To the Scientist I am not Speaking to Any More.
```

### Performance text (classify this)

```text
Don’t say you didn’t see this coming, Jason.

Don’t say you didn’t realize this would be my reaction and that you never intended for me to get all worked up, because if that were true, then you are dumber than Lenny from Mice and Men, blinder than Oedipus and Tierus put together and can feel less than a Dalton Trumbo character.

You put the Dick in Dickens and the Boo in kowski and are more Coward-ly then Noël.

But you don’t understand any of these references,
Do you, Jason? Because you ‘don’t read’.
You are a geology major and you once told me
That, ‘Scientists don’t read popular literature,
Cristin, we have more important things to do’.

Be glad you don’t read, Jason,
because maybe you won’t understand this
as I scream it to you on your front lawn,
on Christmas Day, brandishing three hypodermic
needles,
a ginsu knife and a letter of permission
from Bret Easton Ellis.

Jason, you are more absurd than Ionesco.
You are more abstract than Joyce,
more inconsistent than Agatha Christie
and more Satanic than Rushdie’s verses.

I can’t believe I used to want to Sappho you, Jason. I used to want to Pablo Neruda you, to Anais Nin And Henry Miller you. I used to want to be O for you, to blow for you in ways that even Odysseus’ sails couldn’t handle. But self-imposed illiteracy isn’t a turn-on.

You used to make fun of me being a writer, saying ‘Scientists cure diseases, what do writers do?’

But of course, you wouldn’t understand, Jason.
I mean, have you ever gotten an inner thirsting
for Zora Neale Hurston?
Or heard angels herald for you
to read F Scott Fitzgerald?
Have you ever had a beat attack for Jack Kerouac?
The only Morrison you know is Jim, and you think
you’re the noble one?

Go Plath yourself.

Your heart is so dark, that even Joseph Conrad couldn’t see it, and it is so buried under bullshit that even Poe’s cops couldn’t hear it.

Your mind is as empty as the libraries in Fahrenheit 451. Your mind is as empty as Silas Marner’s coffers. Your mind is as empty as Huckleberry Finn’s wallet.

And some people might say that this poem
is just a pretentious exercise
in seeing how many literary references
I can come up with.

And some people might complain that this poem is, at its core, shallow, expressing the same emotion again, and again, and again. (I mean, there are only so many times you can articulate your contempt for Jason, before people get bored.)

But you know what, Jason? Those people would be wrong.

Because this is not the poem I am writing to express my hatred for you.

This poem is the poem I am writing because we aren’t
speaking,
and it is making my heart hurt so bad, it is all I
can do just to get up off the floor sometimes.

And this is the poem I am writing instead of writing the ‘I miss having breakfast with you’ poem, instead of writing the ‘Let’s walk dogs in our old schoolyard again’ poem.

Instead of the ‘How are you doing?’ poem, the ‘I miss you’ poem, the ‘I wish I was making fun of how much you like Garth Brooks while sitting in front of your parents’ house in your jeep’ poem, instead of the ‘Holidays are coming around and you know what that means: SUICIDE!’ poem.

I am writing this so that I can stop wanting to write the ‘I could fall in love with you again so quickly if only you would say one more word to me’ poem.

But I am tired of loving you, Jason ‘cause you don’t love me right.

And if some pretentious-ass poem can stop me From thinking about the way your laugh sounds, about the way your skin feels in the rain, about how I would rather be miserable with you, than happy with anyone else in the world.

If some pretentious-*** poem can do all that? Then I am gone with the wind, I am on the road, I have flown over the ****** cuckoo’s nest, I am gone, I am gone, I am gone.

I am.
```

---

## IC-1818: Loose Woman and You Bring Out the Mexican in Me

- Title: Loose Woman and You Bring Out the Mexican in Me
- Author (byline): Sandra Cisneros
- Work: Loose Woman
- Publisher: Vintage Contemporaries
- Publication date as stated: March 1995
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 919
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sandra Cisneros
Book: Loose Woman
ISBN: 978-0679755272
Publisher: Vintage Contemporaries
Date (Month/Year): March 1995
```

### Introduction (context only: never use it for content warnings)

```text
To understand the meaning behind these poems, it is essential to know a little about the poet's background. Sandra Cisneros was born and raised in the Midwest, to a Mexican father and a Mexican-American mother. The only daughter of seven children, she and her family lived alternately in Chicago and Mexico City, in poor neighborhoods where American culture became interspersed with her family's Mexican heritage.

Loose Woman by Sandra Cisneros is at once a self-portrait and a statement of defiance. In it, Cisneros acknowledges how others see her and simultaneously rejects and accepts those assumptions. The world has mistaken her as a bitch, a beast, a macha, while she views herself as a fiercely independent and strong woman
```

### Performance text (classify this)

```text
Amorcito Corazón (p. 52) Sweetie Heart

Ya no eres You are no longer mi amorcito my sweetie, ¿verdad? are you?

ya lo supe. I already knew it. ya lo sé. Already you know

Fuiste You were
y ya no eres. And you are no longer.
Fuimos We were
y se acabó. And it’s over.

¿Cómo les diría? How you say? ¿Cómo se explica? How is it explained?

Te conocí I met you ¿y ahora? and now?

no. not.

*Introduction suggested by Heidi Trevithic of Denver, Colorado, and used for the CO State Finalist presentation Loose Woman (pp. 112-115)

They say I’m a beast. And feast on it. When all along I thought that’s what a woman was.

They say I’m a bitch. Or witch. I’ve claimed the same and never winced.

They say I’m a macha, hell on wheels,
viva-la-vulva, fire and brimstone,
man-hating, devastating,
boogey-woman lesbian.
Not necessarily,
but I like the compliment.

The mob arrives with stones and sticks to maim and lame and do me in. All the same, when I open my mouth, they wobble like gin.

Diamonds and pearls
tumble from my tongue.
Or toads and serpents.
Depending on the mood I’m in.

I like the itch I provoke. The rustle of rumor like crinoline.

I am the woman of myth and bullshit.
(True. I authored some of it.)
I built my house of ill repute.
Brick by brick. Labored,
loved and masoned it.

I live like so.
Heart as sail, ballast, rudder, bow.
Rowdy. Indulgent to excess.
My sin and success—
I think of me to gluttony.

By all accounts I am a danger to society. I’m Pancha Villa.

I break laws, upset the natural order, anguish the Pope and make fathers cry.

I am beyond the jaw of law. I’m la desperada, most-wanted public enemy. My happy picture grinning from the wall.

I strike terror among the men.
I can’t be bothered what they think.
Que se vayan a la ching chang chong!
For this, the cross, the Calvary.
In other words, I’m anarchy.

I’m an aim-well,
shoot-sharp,
sharp-tongued,
sharp-thinking,
fast-speaking,
foot-loose,
loose-tongued,
let-loose,
woman-on-the-loose
loose woman.
Beware, honey.

I’m Bitch. Beast. Macha. Wachale! Ping! Ping! Ping! I break things. TRANSITION Cisneros at once embraces and redefines the notion of Mexican womanhood while creating a compelling lyricism in her writing. Through her writing, she is telling the world to watch out, stand back, don't get in my way. You Bring Out the Mexican in Me . . . .

You Bring Out the Mexican in Me (pp. 4 – 6) *NOTE – words in blue italics are defined in the glossary at the end of this selection

You bring out the Mexican in me.
The hunkered thick dark spiral.
The core of a heart howl.
The bitter bile.
The tequila lagrímas on Saturday all
through next weekend Sunday.
You are the one I'd let go the other loves for,
surrender my one-woman house.

Allow you red wine in bed,
even with my vintage lace linens.
Maybe. Maybe.
For you.

You bring out the Dolores del Río in me.
The Mexican spitfire in me.
The raw navajas, glint and passion in me.
The raise Cain and dance with the rooster-footed devil
in me.
The spangled sequin in me.
The eagle and serpent in me.
The mariachi trumpets of the blood in me.
The Aztec love of war in me.
The fierce obsidian of the tongue in me.
the berrinchuda, bien-cabrona in me.
The Pandora's curiosity in me.
The pre-Columbian death and destruction in me.
The rainforest disaster, nuclear threat in me.
The fear of fascists in me.
Yes, you do. Yes, you do.

You bring out the colonizer in me.
The holocaust of desire in me.
The Mexico City '85 earthquake in me.
The Popocatepetl/Ixtaccíhuatl in me.
The tidal wave of recession in me.
The Agustín Lara hopeless romantic in me.
The barbacoa taquitos on Sunday in me.
The cover the mirrors with cloth in me.

Sweet twin. My wicked other,
I am the memory that circles your bed nights,
that tugs you taut as moon tugs ocean.
I claim you all mine,
arrogant as Manifest Destiny.
I want to rattle and rent you in two.
I want to defile you and raise hell.
I want to pull out the kitchen knives,
dull and sharp, and whisk the air with crosses.
Me sacas lo mexicana en mi,
like it or not, honey.

You bring out the Uled-Nayl in me.
The stand-back-white-bitch in me.
The switchblade in the boot in me.
The Acapulco cliff diver in me.
The Flecha Roja mountain disaster in me.
The dengue fever in me.
The ¡Alarma! murderess in me.
I could kill in the name of you and think
it worth it. Brandish a fork and terrorize rivals,
female and male, who loiter and look at you,
languid in your light. Oh,

I am evil. I am the filth goddess Tlazoltéotl.
I am the swallower of sins.
The lust goddesss without guilt.
The delicious debauchery. You bring out
the primordial exquisiteness in me.
The nasty obsession in me.
The corporal and venial sin in me.
the original transgression in me.

Red ocher. Yellow ocher. Indigo. Cochineal.
Piñón. Copal. Sweetgrass. Myrrh.
All you saints, blessed and terrible,
Virgen de Guadalupe, diosa Coatlicue,
I invoke you.

Quiero ser tuya. Only yours. Only you. Quiero amarte. Atarte. Amarrarte. Love the way a Mexican woman loves. Let me show you. Love the only way I know how.
```

---

## IC-1819: The Lost Children

- Title: The Lost Children
- Author (byline): Randall Jarrell
- Work: The Complete Poems
- Publisher: Farrar Straus Giroux
- Publication date as stated: April 1981
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 639
- Already set (do not supply): none

### Source block (context only)

```text
Author: Randall Jarrell
Book: The Complete Poems
ISBN: 978-0374513054
Publisher: Farrar Straus Giroux
Date(Month/Year): April 1981
```

### Introduction (context only: never use it for content warnings)

```text
A mother’s tasks are to create a unity with her child and then, piece by piece, to dissolve it. Yet, most mothers suffer as they cut the psychic umbilical cord that ties them to their children: the wish to preserve these childhood ties is inherent in the term motherhood and is one of the roles biggest challenges. Elizabeth Lawrence once said “There is a garden in every childhood, an enchanted place where colors are brighter, the air softer, and the morning more fragrant than ever again.” It’s no wonder that mothers mourn the passing of their children’s childhood. The Lost Children by Randall Jarrell.
```

### Performance text (classify this)

```text
Two little girls, one fair, one dark, One alive, one dead, are running hand in hand Through a sunny house. The two are dressed In red and white gingham, with puffed sleeves and sashes. They run away with me. . . But I am happy; When I wake I feel no sadness, only delight. That, somewhere, they still are.

It is strange
To carry inside you someone else's body;
To know it before it's born;
To see at last that it's a boy or a girl, and perfect;
To bathe it and dress it; to watch it
Nurse at your breast, till you almost know it
Better than you know yourself---better than it knows
itself.
You own it as you made it.
You are the authority upon it.

But as the child learns
To take care of herself, you know her less.
Her accidents, adventures are her own,
You lose track of them. Still, you know more
About her than anyone except her.

Little by little the child in her dies. You say, " I have lost a child, but gained a friend." You feel yourself gradually discarded.

She argues with you or ignores you
Or is kind to you. She who begged to follow you
Anywhere, just so long as it was you,
Finds follow the leader no more fun.
She makes few demands; you are grateful for the few.

The young person who writes once a week
Is the authority upon herself.
She sits in my living room and shows her husband
My albums of her as a child. He enjoys them
And makes fun of them. I look too
And I realize that girl in the matching blue
Mother-and-daughter dress, the fair one carrying
The tin lunch box with the half-pint thermos bottle
Or training her pet duck to go down the slide
Is lost just as the dark one, who is dead, is lost.
But the world in which the two wear their flared coats
And the hats that match, exists so uncannily
That, after I've seen its pictures for an hour,
I believe in it: the bandage coming loose
One has in the picture of the other's birthday
The castles they are building, at the beach for asthma.

I look at them and all the old sure knowledge
Floods over me, when I put the album down
I keep saying inside: "I did know those children.
I braided those braids. I was driving the car
The day that she stepped in the can of grease
We were taking to the butcher for our ration points.
I know those children. I know all about them.
Where are they?"

I stare at her and try to see some sign
Of the child she was. I can’t believe there isn’t any.
I tell her foolishly, pointing at the picture,
That I keep wondering where she is.
She tells me, “Here I am”
Yes, and the other
Isn’t dead, but has everlasting life. . .

The girl from next door, the borrowed child,
Said to me the other day, “ You like children so much,
Don’t you want to have some of your own?”
I couldn’t believe that she could say it.
I thought: “Surely you can look at me and see them.”

When I see them in my dreams I feel such joy. If I could dream of them every night!

When I sit and think of my dream of the little girls It’s as if we were playing hide-and-seek. The dark one Looks at me longingly, and disappears; The fair one stays in sight, just out of reach No matter where I reach. I am tired As a mother who’s played all day, some rainy day. I don’t want to play it anymore, I don’t want to, But the child keeps on playing, so I play.
```

---

## IC-1820: Love Passes Beyond the Incredible Hawk of Innocence

- Title: Love Passes Beyond the Incredible Hawk of Innocence
- Author (byline): Diane Wakoski
- Work: Emerald Ice: Selected Poems 1962-1987, Pgs 97-103
- Publisher: Black Sparrow Press
- Publication date as stated: Jan 1988
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1208
- Already set (do not supply): none

### Source block (context only)

```text
Author: Diane Wakoski
Book: Emerald Ice: Selected Poems 1962-1987,
Pgs 97-103
ISBN: 978-0876857458
Publisher: Black Sparrow Press
Date (Month/Year): Jan 1988
```

### Introduction (context only: never use it for content warnings)

```text
It has been said that as long as people suffer, there will be poetry; that part of what a poem does is try to make sense of the experience -- to find meaning in the suffering.

Poet Diane Wakoski summed up the process of writing poetry: “First comes the story. Then comes the reaction to the story. Then comes the telling and retelling of the story.”

In this autobiographical poem, Wakoski tells the tale of how innocence is lost in an abusive relationship. Love Passes Beyond the Incredible Hawk of Innocence is dedicated to her first husband S. Shepard Sherbell.
```

### Performance text (classify this)

```text
Innocence is suffering and the loss of that innocence is something to fear . . .

(Pg 97-103) The stairs will forget your footsteps;

the rain will wash away all the invisible

spots where you’ve stood;

my hair will not curl in the places

you’ve touched it;

& newspapers will be printed each day

mentioning neither of our names.

I had passed through the spinal doors
of 2 hospitals,
breathing ether
and passing clots of blood like

soft-backed

red-black

beetles,

each as large as a thumb.

I had eaten the bones of children and washed dishes for the world. I had lived in jails,

the bars made of clocks striking 9 to 6

with overtime on Saturdays;

prison jobs stacking paper over my head

filled with complaints,

irritating as a dog locked up in a room and constantly

barking,

each piece of paper/thousands a day /

had to be individually smiled to

till the weight fell down at night

and the smiles crumbled like dry crusts of bread. I had stood up to the insults of national enemies.

junior high school principals

and assistant principals

who lived their lives by 24 lesson plans a week

aim

motivation

pivotal questions

procedures

summaries

and retarded my own heartbeats with the

frustration

of retarded readers.

I had fallen in love with the sharp edges of razor blades that will cut the flesh of your arms so fast you don’t feel

any pain.
I had signed my name in blood
in a thousand registers
and found that people laughed at my penmanship,
or criticized its execution.

I had spent years in alchemical experiments, and only singed my hands until they looked like a winter poplar at dusk.

But it was not until I met you, my husband for two short years, whose love was like the full moon on a night of total

eclipse,
whose mind was like a flash flood,
whose eyes were like the sound of coyotes in the
Southern

California
hills 20 years ago,
whose words were a fire escape in a burning building,
whose boldness lifted me as a hawk would a snake

before he flings it

down on the ground

to bash the life out of it, whose madness captured me

in the collapsing tunnel of my own defenses; that world that had bled me,

jailed me,

starved me,

laughed at me,

rejected me,
was one I could feel
at last
getting at me,
as you might feel the
hot smokey air from
a burning room creeping under the door crack
in the room where you’ve been defending yourself;
it was not until I met you
that the door broke down

-- or I opened it --
and my innocence was consumed,
burned away.
Those of you who are listening to me now,
some walk leaving your prints in snow,
or soot from burning buildings,
some in jade from the stylized places you travel,
or ink that you’ve spilled in keeping accounts,
you know, I cannot doubt,
how indefinable the borders of countries are,
how easy to walk and find yourself having been in two

countries or
two states, sometimes one foot in one,
the other foot in another,.
You know how the worst ravages of childhood
in some ways never touch you,
while a feather or a leaf falling by chance as you walk on

the street
at a later time, may bruise you
break your arm,
or destroy your life.
When we are innocent,
we know nothing about innocence,
live everything the hard way.
And it protects us.
It seemed to me as if I had been through all the possible
terrors; and meeting this one man
would relieve them all.
But that leaf, that feather,
something
must have pushed down my door.
No longer did the crystal pane surround me.
No longer could it protect me.

No longer could I walk in those same
impossible places
without realizing
their danger.

And that is the secret

-- if the word could be used to mean

reason

formula

explanation
of why I can’t have you
in my life
anymore,
why I can’t dream of you like a sunset

wringing out over the hills & a face

reds, golds

purples, why I can’t even desire you or credit you with the magnificent passion you have.

You hurt me. You locked me in a room and took away my glasses when

you found me reading a book by a man you hated; you pounded my head against the floor when I wouldn’t

change my name; you tried to lock me away in a mental institution when I

wanted to
go to a writers’ conference for two weeks,
you called up my old friends and said you’d castrate them
if

they
talked to me;
you hit me in the mouth every time I disagreed with you;
you would not let me answer the phone or open my own

mail; you threw out poems & letters that were from or about

other men; you created enormous debts and ridiculed me for worrying

about them; you made me feel guilty about everything in a way even an

evil parent
could not have been able;
you hurt me,
and each time I wondered,
“What have I done wrong this time?”
And as long as I retained my innocence,
I believed I needed you,
felt I wanted you,
could not,
would not,
terminate the madness;
it was you,
in fact,
who had to do that,
sent me away
& knew it was final.

I have reached the age of 30.
but feel each moment of my life
has been clawed out
as if I were making a hole around
myself,
in which I could breathe.
Every freedom paid for once & again.
But suffering protects people.

Keeps them involved in the situation at hand. Does not allow the mind to wander or become cynical.

Innocence is suffering,
and the loss of that innocence is something to fear.
But the poem can take its place
in this world.

Jewels dropped on the stairs

or growing on bushes & trees

remind me of your unreality.

The ivory-braceleted hand

picking up a pomegranate

which when opened

gleams,

with its rows of translucent seeds,

ready to be transplanted,

as a new kind of heart.

This could be my different life.

the faces on letters which bite at my

fingers

when I tear the paper

and read out words, hard as green

walnuts,

that would stain my fingers if I could

touch them

are your voice

which left such stains, long & streaked

across

my face.

The lesson of innocence:

that love is not inevitable

but must, like other good things

be chosen

to make any sense.

Not only the stairs
but my ears, muffling as soft towels,
will forget your footsteps.
The only traces rain will not wash away
are the jade prints left in Chinese poems.

Old hair falls out of old follicles
and more grows in.
The newspaper is not the poem
of our time.
Remember the walls of hospitals.
Every flower is a diary.
A mountain is a history; our bones
may constitute,
if we’re lucky,
an interesting story.
Love passes over innocence,
beyond the incredible hawks which is the world
ready to tear us apart,
teaches us the meaning of something
once it is past.
```

---

## IC-1821: Make Up and Fat is Not a Fairy Tale

- Title: Make Up and Fat is Not a Fairy Tale
- Author (byline): Nikki Giovanni and Jane Yolen
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 302
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nikki Giovanni
Book: The Selected Poems of Nikki Giovanni 1968-1995
ISBN: 978-0688140472
Publisher: William Morrow
Date (Month/Year): Jan 1996
Author: Jane Yolen
Book: Once Upon a Time (She Said)
ISBN: 978-1886778610
Publisher: NESFA Press
Date (Month/Year): Aug 2005
```

### Introduction (context only: never use it for content warnings)

```text
We live in a very superficial society. It is very easy to fall into the trap of looking only at the surface of people, things, and ideas without taking the time and effort to delve deeper into them. This is where the adage "Don't Judge a Book By Its Cover" comes from. Literally, you cannot tell the quality of the contents of a book just by looking at the material used to hold it together. A book with a plain cover and simple title may be more important, more entertaining, or more useful than a book bound in a flashier manner.

This metaphor can be extended to many situations in life. Perhaps the best example is the relationships between people. Both Nikki Giovanni and Jane Yolen approach this metaphor from very different perspectives: Make-up and Obesity.

It is easy to fall in the trap of believing the most beautiful, shiny, or flashiest object is inherently "better." Only by maintaining strict self-discipline can we force ourselves to put these prejudices aside and look deeper into everything we do.

So, Ladies . . . . wash off your make-up and put on those comfy pants . . . . be your true self with Make Up by Nikki Giovanni and Fat is Not a Fairy Tale by Jane Yolen.
```

### Performance text (classify this)

```text
Make Up
we make up our faces
for lots of reasons
to go to the movies
or some junior prom
to see ice hockey
or watch the Dodgers come home again
defeated

going to the grocery store
only requires lipstick
while a bridge game
can mean a quick trip
to the hairdresser for a touch up

i clean my makeup
before going to bed
alone
and if my mood is foul
i spray the sheets
with Ultra Ban

most faces are made up
before the public is faced
whether male female or child
it's always so appropriate
doncha know
to put a little mascara
around the eyes

we make up fantasies to face life
we need to believe
we are good on the job
or at least in the bed

we make up lies
to impress people
who are making up lies
to impress us
and if either took all
the make up off
life would not be
worth living

we make up excuses
to say i'm sorry –that-
forgive me –because-
and after all didn't i tell you
-why-

and i make up with you
because you aren't strong
enough to reach out
to say
come home i need you

Fat is Not a Fairy Tale

I am thinking of a fairy tale,
Cinder Elephant,
Sleeping Tubby,
Snow Weight,
where the princess is not
anorexic, wasp-waisted,
flinging herself down the stairs.

I am thinking of a fairy tale,
Hansel and Great,
Repoundsel,
Bounty and the Beast,
where the beauty
has a pillowed breast,
and fingers plump as sausage.

I am thinking of a fairy tale
that is not yet written,
for a teller not yet born,
for a listener not yet conceived,
for a world not yet won,
where everything round is good:
the sun, wheels, cookies, and the princess.
```

---

## IC-1822: Me Too – A Program

- Title: Me Too – A Program
- Author (byline): Andrea Gibson and Pages Matam
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1369
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andrea Gibson
Book: Pole Dancing to Gospel Hymns, Pg 36-39
ISBN: 978-0981521305
Publisher: Write Bloody Publishing
Date (Month/Year): June 2008
Author: Pages Matam
Book: Viral, Pg 37-38
ISBN: 978-0989641517
Publisher: Button Poetry
Date (Month/Year): Dec 2013
```

### Introduction (context only: never use it for content warnings)

```text
According to RAINN, the Rape, Abuse & Incest National Network, every 68 seconds someone in the U.S. is sexually assaulted; and every 9 minutes, that victim is a child. But what is more tragic is that only 25 of every 1,000 predators will end up in prison. (https://www.rainn.org/statistics)

Sexual violence permeates our culture, from violent rape scenes in movies and on TV, to near-daily stories of sexual assaults on college campuses that go unreported to law enforcement. Remember Larry Nassar? A former Olympic physician convicted of sexually abusing more than 500 women. Or how about former President Donald Trump who has been publicly accused of sexually assaulting more than 15 women and was recorded boasting about his abusive conduct?

As controversial, embarrassing or taboo as it is to speak about, the #MeToo Movement has struggled to give voice to those devastated by rape and sexual assault. Today I raise my voice . . . .

Me Too – A program comprised of 2 poems: Blue Blanket by Andrea Gibson and Pinatas by Pages Matam.
```

### Performance text (classify this)

```text
Rape is a coward hiding its face in the make-up of silence, a murderous fruit that grows best in the shadows of taboo.

–Pages Matam Blue Blanket by Andrea Gibson

(Pg 36-39) Still there are days when there is no way, not even a chance, that I’d dare for even a second glance at the reflection of my body in the mirror and she knows why.

Like I know why she only cries
when she feels like she’s about to lose control.
She knows how much control is worth,
knows how much a woman can lose when her power to

move is taken away

by a grip so thick with hate it could clip the wings of Isis, leave the next eight generations of your blood shaking.

And tonight something inside me is breaking, my heart beating so deep beneath the sheets of her pain I could give every tear she’s crying a year, a name, and a face I’d forever erase from her mind if I could.

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

I’ll show you the light in you that made that wish come true. . . “

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

Pinatas by Pages Matam

(Pg 37-38) To the man on the bus I overheard tell a woman in conversation, presumably a friend, “You are too ugly to be raped.”

Dear man on the bus,
Tell the one in five women of this country
they are beautiful, their four counterparts
spared torment ugly.

Tell the one in three women of this world that you will not make piñatas of their bodies. Watch morsels of them spill greedily to the famished smiles of your ignorance shaped like bloodthirsty children. How your words broke them open like a shattered papier mâché cradle, their blood flowed like candy until hollow insides, their jaws mangled into misfortune from when they tried to scream for legs torn crucifix, loud cry of eyes muted. Tell them how beautiful their silence is.

Dear man on the bus,
from smothering cat-calls
to a quickened pace of trek home:
Raped with a dress on,
Raped without a dress on,
Raped as children who couldn’t even dress themselves.
Tell them how ugly their consent was.
Tell the depression, the post-traumatic stress,
the unreported. Tell Mahmudiyah*,
a footnote in the history of crimson Iraqi sands,
how beautiful the military’s silence is,
clocked in how we don’t ask and they
didn’t tell in the name of country.

Tell Elizabeth Fritzl**
how pretty the flame of her skin was,
turning her father into a torturous moth of incest
‘til she gave birth to seven choices she never had.

Dear man on the bus,
Tell my 11th grade student Lauren
that she wanted it, her beauty had them coming.
Tell my 7th grade student Mickayla
that she wanted it, her beauty had him coming.
Tell my 3rd grade student Andre
that he wanted it, his beauty had him coming.
Tell the 8-year-old me
the God in me I loved fiercely was so gorgeous
that cousin twice my age
wanted to molest the Holy out of me,
peeled raw, until I was as ugly as she was.

Rape is a coward hiding its face
in the makeup of silence,
a murderous fruit that grows best
in the shadows of taboo,

a Vietnam prostitute with red, white and blue skin. A murmur of bodies left vacant by the souls that spend years, pills, poems, and even death trying to learn how to reclaim them.

Dear nameless assailant,
How this bus carries the burden
of your stick and blindfold patriarchy
that has only taught you to treat women
like ceiling-strung jugs. Violence claws up
from your throat like a monstrous accomplice
to the 97 percent that will never see jail.

Dear man on the bus, As these words fall out of your mouth,

“You are too ugly to be raped.” I pray no one finds your children beautiful enough to break open, making a decorative, silent spectacle out of

them.

(combined with People You May Know by Kevin Kantor)

IL State Qualifier KS State Qualifier

(combined with People You May Know by Kevin Kantor)

* The Mahmudiyah rape and killings involved the gang-rape and killing of a 14-year-old Iraqi girl and the murder of her family by United States Army soldiers on March 12, 2006. Other family members killed included her 34-year-old mother, 45-year-old father, and six-year-old sister.

** In 1984, Fritzl lured his 18-year-old daughter Elisabeth into his cellar where he drugged her and raped her repeatedly. After telling his own wife that Elisabeth had run away and joined a cult, Fritzl managed to keep his daughter prisoner in the soundproof basement for 24 years. Josef fathered seven children with his own child in the small cellar where he installed cramped living quarters including a kitchen and bathroom.
```

---

## IC-1823: Meditations for a Savage Child

- Title: Meditations for a Savage Child
- Author (byline): Adrienne Rich
- Work: The Fact of a Doorframe
- Publisher: WW Norton and Co, Inc.
- Publication date as stated: Jan 1994
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 839
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adrienne Rich
Book: The Fact of a Doorframe
ISBN: 978-0393310757
Publisher: WW Norton and Co, Inc.
Date (Month/Year): Jan 1994
```

### Introduction (context only: never use it for content warnings)

```text
In a world where language and naming are power, silence is oppression. Silence is violence. It is an identity in agony, screaming but not heard – and the scar is visible mark – “a hieroglyph for a scream.” In Meditations for a Savage Child, Adrienne Rich compares a feral child struggling to adapt to an alien society of words and expectations to her own struggle as a female poet to use the limited language available to express her savage thoughts in a male-dominated world. Meditations for a Savage Child by Adrienne Rich.
```

### Performance text (classify this)

```text
(Prose passages are from J-M Itard’s account of The Wild Boy of Aveyron, as translated by G. and M. Humphrey)

I. There was a profound indifference to the objects of our pleasures and of our fictitious needs; there was still . . . so intense a passion for the freedom of the fields . . . that he would certainly have escaped into the forest had not the most rigid precautions been taken . . .

In their own way, by their own lights
they tried to care for you
tried to teach you to care
for objects of their caring:

glossed oak planks, glass

whirled in a fire

to impossible thinness
to teach you names
for things
you did not need

muslin shirred against the sun

linen on a sack of feathers

locks, keys

boxes with coins inside they tried to make you feel the importance of

a piece of cowhide

sewn around a bundle

of leaves impressed with signs
to teach you language:
the thread their lives
were strung on

II When considered from a more general and philosophic point of view, these scars bear witness . . . against the feebleness and insufficiency of man when left entirely to himself, an in favor of the resources of nature which . . . work openly to repair and conserve that which she tends secretly to impair and destroy.

I keep thinking about the lesson of the human ear
which stands for music, which stands for balance --
or the cat’s ear which I can study better
the whorls and ridges exposed
It seems a hint dropped about the inside of the skull
which I cannot see
lobe, zone, that part of the brain
which is pure survival
The most primitive part
I go back into at night
pushing the leathern curtain
with naked fingers
then
with naked body

There where every wound is registered as scar tissue

A cave of scars!
ancient, archaic wallpaper
built up, layer on layer
from the earliest, dream-white
to yesterday’s, a red-black scrawl
a red mouth slowly closing

Go back so far there is another language
go back far enough the language
is no longer personal
these scars bear witness
but whether to repair
or to destruction
I no longer know.

III It is true that there is visible on the throat a very extended scar which might throw some doubt upon the soundness of the underlying parts if one were not reassured by the appearance of the scar . . .

When I try to speak my throat is cut And, it seems, by his hand

The sounds I make are prehuman, radical the telephone is always ripped-out

and he sleeps on Yet always the tissue grows over, white as silk

hardly a blemish maybe a hieroglyph for scream

Child, no wonder you never wholly trusted your keepers

IV

A hand with the will rather than the habit of crime had wished to make an attempt on the life of this child . . . left for dead in the woods, he will have owed the prompt recover of his wound to the help of nature alone.

In the 18th century infanticide
reaches epidemic proportions:
old prints attest to it: starving mothers
smothering babies in sleep
abandoning newborns in sleet
on the poorhouse steps
gin-blurred, setting fire to the room
I keep thinking of the flights we used to take
on the grapevine across the gully
littered with beer-bottles where dragonflies flashed
we were 10, 11 years old
wild little girls with boyish bodies
flying over the moist
shadow-mottled earth
till they warned us to stay away from there
Later they pointed out
the venetian blinds
of the abortionist’s house
we shivered

Men can do things to you was all they said.

V

And finally, my Lord, looking at this long experiment . . . whether it be considered as the methodical education of a savage or as no more than the physical and moral treatment of one of those creatures ill-favored by nature, rejected by society and abandoned by medicine, the care that has been taken and ought still to be taken of him, the changes that have taken place, and those that can be hoped for, the voice of humanity, the interest inspired by such a desertion and a destiny so strange – all these things recommend this extraordinary young man to the attention of scientists, to the solicitude of administrators, and to the protection of the government. 1. The doctor in “uncle Vanya”:

They will call us fools,

blind, ignorant, they will

despise us.

devourers of the forest

leaving teeth of metal in every tree

so the tree can neither grow

nor be cut for lumber

Does the primeval forest

weep

for its devourers

does nature mourn

our existence

is the child with arms

burnt to the flesh of its sides

weeping eyelessly for man

2. At the end of the distinguished doctor’s

lecture

a young woman raises her hand:

You have the power

in your hands, you control our lives --

why do you want our pity too?

Why are men afraid

why do you pity yourselves

why do the administrators

lack solicitude, the government

refuse protection,

why should the wild child

weep for the scientists

why
```

---

## IC-1824: Meeting Less Than Expectations – A Program

- Title: Meeting Less Than Expectations – A Program
- Author (byline): Sharon Olds and Maia Mayor
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 818
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sharon Olds
Book: Poetry Speaks: Who I Am (Pg 68)
ISBN: 978-1402210747
Publisher: Sourcebooks Jabberwocky
Date (Month/Year): March 2010
Author: Maia Mayor
Book: Get Lit Rising (pg 8)
ISBN: 978-1582705767
Publisher: Simon Pulse/Beyond Words
Date (Month/Year): October 2016
```

### Introduction (context only: never use it for content warnings)

```text
Most, if not all of us, have high expectations for ourselves. We want to win the race, be at the top of our class for academics, or score the job that will help us pay the bills. When we fall just short of those goals, we take it hard. But what makes it even harder is when the people we love, those we call family who are there to support us, criticize and make us feel guilty for not meeting expectations. How are you to grow and have a positive attitude going into the next hurdle when the ones fighting alongside you are fighting against you? Through the poems “The Talk” by Sharon Olds and “Perfect” by Maia Mayor, we are encouraged to take advice, but to also do what is best for us.
```

### Performance text (classify this)

```text
The Talk by Sharon Olds
In the sunless wooden room at noon
the mother had a talk with her daughter.
The rudeness could not go on, the meanness
to her little brother, the selfishness.
The eight-year-old sat on the bed
in the corner of the room, her irises distilled as
the last drops of something, her firm
face melting, reddening,
silver flashes in her eyes like distant
bodies of water glimpsed through woods.
She took it and took it and broke, crying out
I hate being a person! diving
into the mother
as if
into
a deep pond—and she cannot swim,
the child cannot swim.

Perfect by Maia Mayor
Is there something wrong with you?
A loose screw or two that ruined your ability to
function?
Why are you always so tired?
Your life is uninspired and small; all you do is sprawl
on the couch
with outstretched limbs like a sloth in slow-motion.
Where is your devotion to succeed, Maia?
Did it drift out your window with the smoke from
your weed?
Do I need to force feed you discipline ‘til you finally
concede?
I cook and I clean and I don't stop ‘til the soles of
my feet bleed.
But I'm fine.
I'm perfect.
Be perfect, Maia.
Be perfect like me.

Stop wearing those god-awful ripped pants and that lipstick like a whore with double-d implants. You only get one chance. Stop acting like a cat with nine lives left. Stop committing yourself to songs and stories and spoken slam bullshit in a world where degrees and PhD's impede the need for poetry. And stop chewing on your nails. No wonder you've never attracted any males. Why do you do that? Do you like the taste? Are they sweet? You can't eat sweets, Maia. You're ruining your teeth like you're ruining your life. My teeth are perfect. Clean and pristine.

They gleam like the golden halo above my perfectly
conditioned head.
I don't need sugar, Maia.
I am above sugar.

Why are you down here, Maia? Why are you down here when you need to be up here? Up here with the ones who have a promising career Who listen when information goes in one ear and doesn't come out the other. You'll never be up here, Maia. You act as if the act of listening is a crime or you would have heard me the six hundred and sixty-sixth time I told you to STOP CHEWING ON YOUR NAILS. Stop chewing on your nails like a goddamn piece of trash. You can't be trash, Maia.

You have to be perfect. Be perfect like me.

I get up at 5 in the morning every day.
I start my day the same way worried that I'll
collapse
as my bones start to decay from cleaning up your
scraps.
Why is your room such a mess?
The clothes go in the hamper, Maia.
Not displayed on your bed like your lack of morals.
Not littered on the floor collecting more dust than
my withered expectations.
You disregard my rules with stubborn contempt
in a substandard attempt at teenage rebellion.
But you can't be a rebel, Maia.
You're not interesting enough.
You need to obey and say 'yes' and 'okay'
You need to do it with a smile on your less than
average face.
You need to try harder, Maia.
Make it wider, Maia.
Why don't you know how to smile?

You disappoint me, Maia.
You never appreciate what I do for you.
You never try to be a winner.
And you never eat your dinner.
You never eat the dinner I consistently provide for
you
as I constantly remind you of the life I set aside
for you.
That meal doesn't pay for itself.
I don't care if it's ideal, stop telling me how you
feel.
You need to eat it.
Eat it all.

Eat it at a reasonable time with a glass of milk.
You need milk, Maia.
You need calcium like you need a catalyst for
growth.
You'll never grow to be tall.
Be tall like me.
I drink my milk, Maia.
Drink your milk.
Be tall.
Be perfect.
Be perfect like me.

You need to pay more attention, Maia.
Stop daydreaming, Maia.
Stop staring at the ceiling as if your one redeeming
quality lies hidden in the plaster.
You need to organize your life.
Your life is a disaster
Just like your room.

Just like your teeth.
Just like your future,
Which will soon come to an end if you don't put
down that pen.
You need to stop writing, Maia.
Your life is not a book.
Don't give me that look, Maia.
I'm just trying to help you.
I'm just trying to love you.
I'm just trying to love you.
You have to let me love you
so that you can be perfect.
Be perfect like me.
```

---

## IC-1825: Memoirs of a Nun on Fire

- Title: Memoirs of a Nun on Fire
- Author (byline): Philomene Long
- Work: The Outlaw Bible of American Poetry
- Publisher: Thunder’s Mouth Press
- Publication date as stated: Nov 1999
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1178
- Already set (do not supply): none

### Source block (context only)

```text
Author: Philomene Long
Book: The Outlaw Bible of American Poetry
ISBN: 978-1560252276
Publisher: Thunder’s Mouth Press
Date(Month/Year): Nov 1999
```

### Introduction (context only: never use it for content warnings)

```text
Philomene Long was born in Greenwich Village. Among the very first sounds she heard were those of poets howling their poems and jumping out the windows. At the age of eighteen she entered a convent as a wild teenager. After five years behind cloister walls she escaped in the middle of the night down the side of a mountain to Venice West where she lived among the poets, saints, and mad ones. This is her autobiographical poem . . . Memoirs of a Nun on Fire by Philomene Long.
```

### Performance text (classify this)

```text
"You are worldly, Sister Marie Philomene," the Mother
Superior had said in the parlor
bent over me, tall, angular, aristocratic
like the silhouette of a praying mantis.
"Even your voice, its inflections. Worldly."

At that I was to kneel on the spot. Kneel with no excuses. Blind obedience.

Drop to the floor like a swatted fly.

Eyes lowered, lips closed. I wiggled. My veil fluttered. My knees bent a little, then locked. I would not.

Back straight, head erect,
my eyes wide, cool, and I hope vacant,
I stared into her triangular face. I turned. Left through
the dim corridors of no time or season.

In my room I reached through the silence, and as if
from a great height,
watched my hands take the scissors,
begin to cut name tags off veils,
stockings, underwear. Everything.

All over the room,
threads and scraps of my name,
"Sister Marie Philomene" like tiny white clouds far
beneath my feet.

I knew I would leave that night. Just walk out. Five years within this cloister. An enclosure of silence. Latin. Eyes fixed to the floor. Black robes, medieval gestures. In the most secret recesses, a thousand daily deaths.

At the end of the hall the life-size crucifix. Christ's
bruised knee,
the level of our lips.
A well-kissed knee.

Through these corridors
we glide through our own ghosts.
Muted light. Fluid movements.
Everything clean. Silent and clean.
"I have loved, 0 Lord, the beauty of Thy house."

But here some things feel dirty.
Like in my dreams.
In the convent I do not dream of the good sisters. Each
night it is a dark man who follows me.

He is tall, thin, and wears black. All black.
His half smile is repulsive.
He wants to kiss me. Every night in my dreams.
Sometimes he removes my veil,
runs his fingers through my hair.
Once he does kiss me.
I am frightened. I tell another sister.
She says the dark man is myself.

And then-the night I was seduced
by God disguised as a fat black fly.
As a Bride of God I was told to experience the Mystical
Union I must make my mind empty, an erased
blackboard.
I contemplate the blackness of space,
the millions of light years between the stars.
I stretch my mind until it is no longer fixed anywhere.

I became the Bride of the Expansive Black. I kiss it. Marry it. Its deep silence.

But it is difficult to contemplate the Immensity while enduring a small but persistent itch.

Daily I work shoveling the convent's garbage into the incinerator. The flies and yellow jackets are very friendly. At times the golden insects cover my black serge habit like a jeweled mantle, as the flies circle my head. At first I do not know a fly, that one fly has crept into my ear to rest. I suppose it has awakened, confused, and is trying to escape. Lost deep within my ear canal, it buzzes with mounting intensity. Its buzz is as loud and wide as the universe I am contemplating. Finally, I know it is not God, but only a fly. Or is it God disguised as a fly? Is it the buzz of God?

The fly buzzes with growing desperation.
As the fly's delirium grows, so does mine
given the heat, the perspiration,
the itchy habit, and
the frantic buzzing of that fly. That Fly?

When it emerges into my outer ear I open the side of my head gear and the fly flies out. At this moment, this very moment, I see it at the corner of my eye an enormous black fly. It hangs in mid-air as if to look at me for a moment. The most beautiful fly I've ever seen

But what did the nuns see as they sat silently behind me
everyone motionless except one nun and
a hovering fly besides her?
I will never know. No one ever mentions it.
No one ever mentions anything personal.

Beat. Beaten. Beatific.
I am on my knees before the bed, the crucifix.
This particular night is exceptionally dark.
It is this night I am to understand I am a poet.
Saturday night. Time to whip ourselves again.
I wonder is Cardinal McIntyre doing this?

But I will do it right this time. Five years within the convent and I have not yet done it right. Each time the hand that holds the chains has exerted its own will. I say to the night, "I will tonight. I will beat myself until I bleed."

My body, mind-one thing
I raise the chain high up. Higher.
That way it will come down with greater force
to beat, beat. To beat, to be beaten. Higher. Faster.
Body, mind, chain-one thing. One will.
To strike repeatedly. To beat to blood.

It ends. I run my fingers over my back. There is blood. For the first time-blood.

A small amount. But I did it. "Beautiful blood," I say. I remove my habit.

I run my fingers over the spot. Yes. It is blood. Beatific blood. Beatific spot. Slowly, I turn in awe to see it. It, indeed, is beautiful. But it, my beatific spot. . . is a mosquito bite!

I stand in the center of the room. Let loose a mighty laugh. "Beatific mosquito! Beatific bite!"

I, who have been the Bride of flies,
have become the Bride of mosquitoes.
"Holy proboscis! Probe of fire!"
(Didn't Saint Rose of Lima, out among the mosquitoes
so that they might bite her, say their hum sounded to
her
like a choir of angels?)

"0 Holy Night! The mosquitoes are quietly biting Little fly. Great night."

If you would have looked into this dark corner, you would have found Philomene, a Philomene who no longer hid her heart under crossed arms,

Hers was a song of . . .
No, it was deeper even:
it was a prayer, as the priest mutters
from the altar holding up the Host.
Her heart thumping in this forgotten corner as she
prayed. You would see her dare to look at her own body,
in the stark black night
Her body, golden serpentine,
glowing cheeks, glistening eyes, crimson tongue
In this night of black finger, her slick long body rising
rising in the blackness-slowly, very slowly turning,
turning in the unseeing dreadful hole of night.
The night, its burning lips, the night of kisses.
She danced. Burning bride of God.
In the Grand Silence, you could hear Philomene whisper,
"I am a poet."

But I will always be a nun.

Always in my dreams I am a shabby nun. There are flies
under my habit
and my robes are in bits and pieces.
I will always have an affinity for the extreme.
Even now I prefer the company of a St. Francis of Assisi
taking his clothes off in public,
or St. Simeon Stylites
who sat for years atop a high column,
or St. Joan of Arc
who heard voices and dressed in men's clothes.
Even now I prefer to live among
the poets, saints and mad ones of Venice West.
I know no other way but to leap
into the Holy Fires.

Burn. Burn. Must burn.
```

---

## IC-1826: Mirror to Her Mouth from House Arrest

- Title: Mirror to Her Mouth from House Arrest
- Author (byline): Anna Deavere Smith
- Work: House Arrest and Piano: Two Plays
- Publisher: Anchor
- Publication date as stated: April 2004
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 706
- Already set (do not supply): none

### Source block (context only)

```text
Author: Anna Deavere Smith
Book: House Arrest and Piano: Two Plays
ISBN: 978-1400033577
Publisher: Anchor
Date (Month/Year): April 2004
```

### Introduction (context only: never use it for content warnings)

```text
In 1996, The MacArthur Foundation awarded Anna Deavere Smith a prestigious fellowship, saying she “has created a new form of theatre — a blend of theatrical art, social commentary, journalism and intimate reverie.” These words of praise are epitomized by this selection: Mirror to Her Mouth from House Arrest . . . a true story of Paulette Jenkins, whose boyfriend abused her and her daughter. One night the man beat Paulette’s daughter so badly that she died. This is Paulette’s story as told to Anna Deavere Smith during an interview at the Maryland Correctional Institution for Women and brought to life on stage in Mirror to Her Mouth from House Arrest.
```

### Performance text (classify this)

```text
*NOTE – Use caution when entering this selection in the Poetry category. The selection is from a stage play, written in verse form, and may not meet the rules governing Poetry in every state.

I began to learn how to cover it up
because I didn't want nobody to know that this was
happening
In
my home.
Ya know.
I wanted everyone to think that we were a normal family
and I mean
we had all the materialistic things.
But that didn't make my children pain any less.
I ran out of excuses about how we got black eyes
and busted lips and bruises
me and the kids.
I didn't have no more excuses.
But it didn't change the fact that it was a nightmare
for my children.
It was a nightmare.
And I failed them.
Dramatically.
Because I allowed it to continue on and on and on.
And that night that she got killed,
and the intensity that grew and grew and grew.
Until one night,
we came home,
from getting drugs,
and he got angry with Myeshia
and he started beating her.
And he just continued to beat her,
he had a belt, he would use a belt.
I'm just speaking of the particular night she died.
And he beat her
and he put her in the bathtub.
And I was in the bedroom.
But before all this happened,
four months before she died,
I thought I could really fix this man
so I had a baby by him!
Insane?
Thinking that
if I gave him his own kid
he'll leave mine alone.
And it didn't work.
We wound up with three children.
But the night that Myeshia died.
I stayed in the room with the baby.
And I heard him,
just beating her,
just beating her,
like I said he had her in the bathtub,
and every time he would hit her,
she would fall.
And she would hit her head on the tub.
I could hear it.
It happened continuously,
repeatedly.
(Whispering. )
And I dared not to move.
I didn't move.
I didn't even go see what was happening.
I just sat there and listened.
And then later
(SHE sucks her teeth.)
he sat her in the hallway
and
told her just set there
and she set there for 'bout
four to five hours
and then he told her to get up
( Crying.)
and when she got up she said she couldn't see.
(Whispering, crying.)
Her face was bruised.
And she had a black eye.
All around her head was just swollen.
Her head looked like it was two sizes of its own size.
I told him to let her go to sleep and he let her go to
sleep.
(Whispering. )
The next morning she was dead.
He went in and checked on her for school.
And he got very excited.
And he said
"She won't breathe!"
I knew immediately that she was dead.
'Cause I went in
I didn't even want to accept the fact that she was dead.
So I went and took a mirror to her mouth.
There
was no-thing coming out of her mouth.
Nothing.
He said
"We cannot let nobody know about this,
so you got to help me."
And I agreed.
I agreed.
I didn't dare tell anyone.
'Cause I had been keeping it a secret
for years and years.
And it just seemed like secondhand to me
to keep a secret.
That night,
we went to the mall
and we told the police
that she had been missing.
We told like the security guards of the mall
that we had like lost her.
Ya know we fabricated this story and I went along with
it.
And we told him that she had been missing.

But she wasn't missing.
So after that
we left the mall
and we told them what she had on
that night.
We got her dressed in the exact same thing
that we told the police that we had put on her.
And we got the baby
and we drove like out to
(Hear her getting the slightest bit tired here.)
I-95.
I was so petrified
and so numb
all I could look
was in the rearview mirror.
And he just laid her right on the shoulder of the
highway.
My own chile.
I let that happen to.
```

---

## IC-1827: Missing Natalie and Victim

- Title: Missing Natalie and Victim
- Author (byline): Nicole Blackman
- Work: Blood Sugar
- Publisher: Akashic Books
- Publication date as stated: May 2002
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1692
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nicole Blackman
Book: Blood Sugar
ISBN: 978-1888451344
Publisher: Akashic Books
Date (Month/Year): May 2002
```

### Introduction (context only: never use it for content warnings)

```text
Each year, more than 1 million children are reported missing. This is a staggering number, but it doesn’t take into account the trauma faced by the overlooked sisters and brothers of those abducted whose family are irrevocably changed. This selection, Missing Natalie by Nicole Blackman brings to life the struggle of one young girl to come to terms with the abduction of her twin sister.
```

### Performance text (classify this)

```text
Missing Natalie

Most of my friends don't know I was born a twin. She was born sixty-three seconds before me. Her name was Natalie. We came here together. She left without me.

We shared a room and split it down the middle. I put all my posters up on my side, and she put hers up on the other. One day we decided to wallpaper the room with Superfriends wrapping paper and Elmer's glue. Mom wasn't too crazy about that.

She was patient, I was bossy. She wanted to be a gymnast, I wanted to be an actress. But we both liked horses and we liked to draw. We mixed up things like ketchup and cough syrup and tried to get someone to eat it. Natalie and I would climb trees in our backyard and plan the houses we would build next to each other so we could visit when we had families of our own. We picked out the names for our husbands, for our children. When you're a twin, you have a shadow.

We were in the supermarket looking at the toys. Mom was picking up some shampoo and cat food. There was a doll that I really wanted so I ran a couple aisles over to ask Mom. She told me I already had too many dolls and sent me back to get Natalie so we could leave the store. It all happened in a minute.

This is the part where I'm supposed to tell you that your life can change forever in sixty-three seconds. But you already know that, don't you?

On the surveillance camera, you can see Natalie walking out of the store with a man. He's not forcing her, but we don't know why she's going with him. She turns around for a second like she's saying goodbye. At least that's what we think it means.

We've gone over the video hundreds of times. It's burned in my mind like the Zapruder film. Even now I could draw it for you, with the time code on the bottom of the screen and everything. I'm twenty-four now. She's frozen at nine.

When she was gone a month, I put our beds together and put a blanket across them when I slept.

They sent me to a child psychologist for a long time. She made me draw my "feelings." Let's draw your feelings now. What do your feelings look like? I wanted to strangle her. Instead, I drew for an hour so she'd shut up. I used only the black markers and drew me and a burned-out hole for Natalie. That's me, and that's Natalie. The psychologist analyzed the drawings and talked to my parents. She's having a very difficult time. Losing Natalie has left a void in her life. Well, duh. You could have just asked me and saved yourself a lot of time. You want to know how I feel? You want to know what's going on? Someone stole my sister. Someone f***** stole my sister. How many drawings do you want me to make? They stopped making me go to the psychologist after that.

I never saw Dad cry, but something was sacrificed after it happened. He drinks alone now sometimes. He never used to do that.

The police give us a report every three years now or something, and tell us the case is still open, as if that's a help. They try to tell me sometimes that since they never found a body, she might be alive. Right. Like there's nowhere on earth to hide a body. If she was alive, I'd know. If anyone would know I'd know, and I haven't felt her near me in a long, long time.

They put me under hypnosis. I told them the man was wearing a navy-blue corduroy jacket, had brown work boots on, smelled of grease and never looked at me. The case is still open.

Four months after she disappeared, it was our tenth birthday. I told Mom to forget about it but she insisted ... she always had a birthday party for us ... we had to go on with a normal life. The day of the party we hung up balloons and streamers and Mom pretended Natalie was away somewhere, like it was a surprise. I sat there and waited. I waited all day.

Nobody came. All the kids who used to come to our parties now said they couldn't. Sometimes their mothers called and cancelled, like abductions were contagious and they didn't want their kids to catch it too.

That night Mom and I sat in the kitchen and ate a box of sugar cookies and talked about Natalie. We didn't have anymore birthday parties after that. It became the birthday ritual. We would eat a whole box of sugar cookies and talk about Natalie for hours. It was our way of keeping her close. We do it every year. Dad still doesn't know.

My parents refused to move after Natalie disappeared. We need to be here when she comes back. Otherwise, how will she find us?

We just want to know what happened. It's like watching a scary movie and the film breaks in the last fifteen minutes and they try to make everyone go home. We just want to know what happened.

Most of my friends don't even know I was born a twin. She was born sixty-three seconds before me. Her name was Natalie. We came here together. She left without me.

TRANSITION According to the Office of Juvenile Justice and Delinquency Prevention . . . The murder of an abducted child, particularly by a stranger, is a rare event. There are estimated to be about 100 such incidents in the United States each year. The victims are typically “average” children, leading normal lives, and growing up in normal families. Just like Natalie, the vast majority of them are girls, with the average age between 11 and 12 years old. Natalie was just a bit younger. This is her story . . . Victim by Nicole Blackman.

Victim I feel the motion of the car before I open my eyes. The air is blue-black, brown-black, black-black. Smell of gas, oil, animals. I'm in the trunk. My wrists and ankles tied. My mouth is taped and it almost covers my nose but I can breathe barely. I must have been here for hours, everything's stiff and my head throbs like someone's drumming on china. The car stops. He turns off the motor - there are no traffic sounds. No people sounds. No wind. What place has no wind?

I turn my head towards the sounds
like people watch radios when something terrible happens.
My palms are sweating. Where am I?
The trunk squeaks as he lifts it up and the sun blinds me. He
almost looks like a faceless Jesus surrounded by light.
He pulls me out of the trunk and bangs my head against the
door. I try to cry out, but it comes out like a hum.
He drags me, half-standing, along a dirt road into a house. I
can't see any other houses and it looks like a farm.
The screen door bangs behind me
and I feel a deep, deep pressure inside me. All the rules
have changed here.
I'm dragged down a hall like a bag and I look for a phone,
other doors. Nothing but bare floors and brown boxes in
small rooms.
He pulls me into the bathroom
and I almost crack my head as he pushes me onto the floor.
Tilts his head to the side
and gazes at me as if I was a pet, then walks out.
I'm lying there for a long time, trying to get the tape off of
me. My eyes are tearing. I don't make a sound.
I can't get up and I keep rolling from side to side, trying not
to make noise.
I've got to get him to talk to me.
If I can get this thing off my face I can talk to him. I'll tell
him my name.
Have you killed other women in here?
I'm thinking that you've got hundreds of them
nailed down, hung on walls, hanging from ceiling fans and
swinging dead in summer wind.
Why did you pick me?
If I had stayed to finish at the library
I would have been there 20 minutes longer maybe I'd have
been OK.
Would have rushed into the house,
books piled up in my arms like a baby, and blurted
explanations why I was sorry. So sorry I'm late everyone.
Would you have waited for me anyway? Would you have
picked another woman?
Would I have read about her in the paper and said Oh my
god, I was there that night...
and called all my friends in a panic.
Telling them then how much I loved them
as if I'd never have the chance again.

I wonder what everyone is doing now. Putting up signs. Showing my picture on the evening news. Calling old friends. Maybe I'm not even considered missing yet. The family will fall apart and my parents will go crazy. Slowly. My brother will be so quiet at the funeral and insist the casket be closed. (I never even told anyone what kind of funeral I wanted when I died.) Maybe years from now they'll find my skeleton on the floor here and they'll have to use dental records to identify me. My family will say At least we know now. We always hoped she was alive somewhere. We just hope she's in peace. When I sleep my dreams are crazy - I'm flying over fields. I don't think I sleep for more than 20 minutes and when I wake up, it feels like I'm wider a heavy blanket. I'm still here. As I wake up I hear a dog barking in the distance and I think I'm in my parents' house in South Carolina. When I open my eyes, there's a shotgun pressed between them.

I'll never get married.
I'll never have kids.
I'll never go to Europe.
I'll never learn to play piano. I'll never write a book.
The last thing I hear is a click.
```

---

## IC-1828: My Brother’s Funeral - A Collection

- Title: My Brother’s Funeral - A Collection
- Author (byline): Megan Falley
- Work: The Redhead and the Slaughter King
- Publisher: Write Bloody Publishing
- Publication date as stated: Oct 2014
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1233
- Already set (do not supply): none

### Source block (context only)

```text
Author: Megan Falley
Book: The Redhead and the Slaughter King
ISBN: 978-1938912450
Publisher: Write Bloody Publishing
Date (Month/Year): Oct 2014
```

### Introduction (context only: never use it for content warnings)

```text
It has taken me a long, long time to come to the realization that when the person you love becomes an addict, they are no longer the person you love. You can spend your nights trying to understand addiction, and how somebody can transform into a person so horrific right before your own eyes, but there is no understanding it.

My Brother’s Funeral – A Collection by Megan Falley
```

### Performance text (classify this)

```text
An Apology To My Brother

I'm sorry I spill your secrets
like an overfull goblet of wine.
I'm sorry I think they're mine mine mine.
I'm sorry that I love you
the way a shadow loves its body-
that I always sniff your hair.
I'm sorry that in the poems I name you Needle.
In the poems I name you Pill.
I'm sorry it's always recovering,
never recovered.
That I'm still nervous when you call.
That I think it's for bail.
I'm sorry that when you say I love you
I wait for the but,
I'm sorry I always write about you
as if you are dead.

It's just-
I spent so many years
preparing for that funeral.
All my dresses are black.

Golden Boy
My brother's hair
looked like someone cooked a porridge
comprised entirely of sunshine
and poured the bowl over his head.
It was a yellow traffic light
that everyone slowed down for.
They complimented my mother,
told her she was lucky.
He was a dandelion of a boy
but when we picked him up
after his first day of High School-
he demanded we take him to the barbershop.
This memory comes before heroin
became a household name.
Before I found
my piggybank slaughtered-
my brother's mouth filled
with more pills than teeth.
He slammed the door as he stormed
into the $7 barber.
Alone, he growled.
I was six years old and did not know
what this meant,
but I saw my mother's eyes
in the rearview mirror-
she knew what happened when dandelion boys
asked for the lawnmower.
He returned to the passenger side
years older than he was when he left it,
switched the channel on the radio
to something harder, faster,
twisted the volume knob up to
drown the words no one was speaking.
Back in the barbershop,
someone swept up
that gold-spun miracle
and threw it away.
My mother knew a war
was going to come,
the way animals know before rain.
The way they know,
but can do nothing
to stop it.

TRANSITION

I felt a Funeral, in my Brain, / And Mourners to and fro / Kept treading - treading - till it seemed / That Sense was breaking through.

Emily Dickinson penned these lines more than a hundred years ago. But as Megan Falley imagines funeral situations for her brother, Dickinson’s words echo . . .

The First Ceremony
If I was the family florist,
I'd be responsible for the apology of lilies.
If I was the lawyer,
I'd be expected to pay for it all-
the party of black.
If I was the chef,
they'd ask me to feed
those who cannot imagine eating.
But I am the writer-
not the star of the funeral,
but its narrator-
here to translate the language of grief
into simple, digestible metaphor.
To wield euphemisms.
Turn addiction into grip on reality.
Turn overdose into sudden, unfair.
My mother can melt
like a satin witch into her corner of the pew,
my father can do what men do:
prove his strength, become a pallbearer.
But I'm the emcee
at my brother's last big party
so I recite his eulogy
to shampoo bottles,
haven't sung in the shower for years.
My brother bangs
on the bathroom door,
says, Hurry up - [what’s] taking so long?
I do hurry up.
I want him to love me.
There's still dirt on my skin, though. There's still soap in
my hair.
TRANSITION
Or maybe Sean’s funeral will be like this . . .

The Second Ceremony
We bury him with his baseball cards
because that's what he has left,
what his life amounted to.
The electronics sold.
The house turned to soot
at the whim of one cigarette.
Even the girls figured him out.

We bury him with his friends
outside the funeral home,
too scared to enter,
sweating like burned spoons.
We replace his face in its forever bed
with each of theirs,
their pockmarked arms and rotted smiles.
We bargain with the god of too late.
We bury him in his father's suit,
which was too big for him before
and ridiculous now,
but nobody buys a new suit for the dead.
We leave him
to lie in his potential.
I bury him with a picture of me.
Don't bother to tape the jagged,
toothy edge back together.
He ripped himself out on purpose-
and look how I'm smiling in the photo.
Look
how I'm leaning

on nothing.

TRANSITION The images get bleaker and bleaker as Sean’s addiction worsens . . .

The Third Ceremony
I am the only one at your funeral.
I fill the vase with the right flowers
and press my face into them,
but only smell your cigarettes.
I recite the obituary
that I've been saving for this occasion
ever since the summer
you started putting fireflies
on your tongue
and winning contests for cruelest hands.
I admit, it's a flawless performance,
gifted to an empty room,
but I can't help but hate you
for not cracking
an embalmed smirk
during the funny parts.
I carry your casket alone
which is also an exercise
I've been training for.
The hearse is the only one
waiting for me to finish.
There will be no procession,
no cars following behind.
You've left no shadow.
Pawned all the people
who could have been here
for highs even you knew weren't worth it.
I am relieved-
the worst is over.
I received the phone call,
confirmed your body.
I open a black umbrella,
blame you for the rain.
TRANSITION
And then there’s a ray of hope . . . Rehab seems to be
working and images of Sean’s funeral shift again to the way
it should be . . . the way Megan Falley hopes it will be. Her
mind whispers “Please, Sean . . . let rehab work this time.”

The Last Ceremony
The widest church in town is still
too small to fit everyone who has loved you
through its heavy doors,
so we hold two funerals.
No one wears black.
We wear your sports jerseys from high school.
We wear the t-shirts you collected
from the marathons
you ran to raise awareness for addiction.
Your grandchildren wear the sheets
from the forts you built with them,
cut into capes.
Your wife does not cry,
she feels lucky to have loved you.
You live on in every wrinkle.
You gave her those smile lines
she wears like jewelry.
The men from the meetings tell stories about you saving
them,
yanking them from their own syringes and vomit,
they name their kids after you.

There are so many boys named Sean,
Sean.
I wish our father was here to see this,
but maybe he's waiting up there
with a catcher's mitt,
maybe there's a baseball
whizzing through the air for you.
I know you'll catch it.
In the casket,
you are older than rain,
just as exquisite.
There is not a shadow
of pain on your face.
You learned the science of
turning it to joy.
I remember the day,
decades ago,
when you told me I was your best friend.
I could have died right then,
but we were given the gift
of years, and dinners, and holidays,
and children,
and forgiveness
which is sweeter than any liquor.
This is the first of your funerals
where no one asks me to make the speech.
I just sit in the front row and weep,
and am not sad.
I am the least sad I have ever been.
```

---

## IC-1829: My Mother Learns English

- Title: My Mother Learns English
- Author (byline): Patricia Smith
- Work: The Spoken Word Revolution
- Publisher: Sourcebooks, Inc.
- Publication date as stated: April 2003
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1211
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patricia Smith
Book: The Spoken Word Revolution
ISBN: 978-1402200373
Publisher: Sourcebooks, Inc.
Date (Month/Year): April 2003
```

### Introduction (context only: never use it for content warnings)

```text
"Y'all" isn't welcome . . . And forget about "fixin'," as in getting ready to do something, people with strong Southern accents are often perceived as "slow and dimwitted." But it's "sort of a shame" that people should feel the need to soften or even lose their accents. Patricia Smith laments the loss of personal culture as her very Southern mother becomes determined to fit into the Northern culture . . . language and all in “My Mother Learns English.”
```

### Performance text (classify this)

```text
An anxious immigrant at 64, my mother is learning

English. Pulling Sears Best cinnamon stockings to a roll beneath

her knees, sitting that Baptist ski slope of a hat on her head, she rides the rattling El train to a steel spire in

downtown Chicago, pulls back her gulp as the glass elevator hurtles upward and comes to sit at a gleaming oak table across from a pinstriped benevolent white angel who has dedicated two hours a week to straightening the black, twisted tongues of the

afflicted. It is this woman’s job to scrape the moist infection of Aliceville, Alabama from my mother’s throat.

“I want to talk right before I die,” my mother says, “Want to stop saying ‘ain’t’ and ‘I done been’ like I just

got off the boat.” My mother has never been on a boat. But 50 years ago, a million of her, clutching strapped

cloth suitcases and peppery fried chicken in waxed bags, stepped off the buses at the Greyhound depot in

Chicago, eagerly brushing the stubborn red dust from their

shoes. “We North now,” they all said, still in their southern

tongues, as if those three words were vessels big enough to hold it all, all those dreams with bulging seams, dreams that spilled over the borders of sleeping, dreams that hurt the eyes with their feverish glow, dreams that got drunk on sweet water and whispered promises. My mother’s northern dreams were simple, but huge— she thought it a modern miracle to live in a box stacked upon other boxes, a tenement apartment where every surface smelled of Lysol and effort, and plum roaches, cross-eyed with spray, dragged themselves

across freshly washed dishes, dropped dizzily from the ceiling into our food, our beds. Mama’s huge dream required starch stiff pinafores, orlon sweaters with stitched

roses and A-line skirts in the color of winter. There had to be

a tavern on the corner with a jukebox where men begged forgiveness in gravel voices and a comfortable stool by the door, where mama could sit and look like a Christian who was just leaving. She needed a job that didn’t

involve soil or branches, in a factory where she could work in a straight line with other women, repedida, repedida,

repedida, no talking allowed, their heads drooping with dreams. Within walking distance of wherever she lived, there had to be a Baptist Church where she could pull on the white gloves of service and wail to the rafters when she felt

the hot hand of the Holy Ghost pressing insistent at the

small of her back. Yes, Jesus had to be there—He had

blessed her journey so far, quickened her step, stroked her free of the Delta. She was His child, building herself anew here where the burning of her hair was a ritual and she’d given up wearing pants because the Lord said she should. Her dreams for the most part realized, my mother now

busies herself preparing for burial, stashing away a dollar here, a dollar there, to pay for her own coffin, not wanting to

bother me, as she says, with that nonsense. She instructs me

not to spend lots of money putting her under, and once again

sternly relates the story of the dutiful daughter who neglected

details, so her dead mother’s body was sent to church #1 while everyone waited to mourn in church #2. If that

happened, chile, I’d be so embarrassed. No mother, I think, you

would be so dead, but I don’t dare actually bring this to voice because Annie Pearl Smith is not a fan of humor. She is retired now after 40 years working in a candy

factory, making malted milk balls, hot dog gum and candy corn. She’d been gone from the place for a year before she

could scrub the stark sugar smell out of her skin. When my

father was murdered, almost 25 years ago, mama and I gazed at each other across a huge yawning chasm, we had no idea one about the other. I had spent so many hopeful years dousing my father in my dreams and he had listened

while my mother cursed a comb through my nappy hair, nagged me to sit up straight, checked my grades, led me to church, and grabbed the switch when I sassed. She didn’t talk unless talking was necessary. Now she says it hurt her that I gave him everything. So, of course, now I want to get to know her. I know she doesn’t believe men ever landed on the moon, that the whole thing was staged in some Arizona desert because American folks are stupid that way and always

will be. I know she had a hysterectomy and never told me. I know that her motto was Always be respectful of

white folks.
I know she only thinks she is dying soon, because it is
fashionable when you are old and black and Christian
to think so. I know that I never realized
that the way she spoke
was ever a problem
for anyone
especially her
especially me
My mother’s voice:
--It’s like cornbread, buttery and full of places for heat

to hide. --When she is angry, it curls into a fist and punches

straight out. --When she is scared, it gathers strength and turns

practical, matter-of-fact, like when she is calling

her daughter to say they found your father this

morning, someone shot him and he is very dead. --She can’t sing, not a lick, not at all. When she tries,

her voice cracks and collapses and loses all

acquaintance with a key, and every Sunday morning it’s my mother’s voice that’s the loudest, unleashed and

creaking toward glory.

--When my mama talks, the sound of it is flat and broad

and wild with unexpected flowers, like fields in

Alabama.

--She has never been grammatically correct. Her rap is

peppered with ain’t gots and don’t have nones and

I done beens and she be’s and he be’s the way

mine is when I’m sweet color among coloreds and

don’t have to worry about being graded. I see no

shame in this. You can’t do wrong in the process

of unwrapping a dream. Turns out now one of my mother’s leftover dreams Is to wash history from her throat, to talk like a woman got some sense and future, to talk English instead of talking wrong Yes, I am a poet, privy to the shoes of others,

But I want my mother to be my teacher
To talk to me, one colored girl to another
To warm me up with double negatives
To take me down south
And leave me there
But I pick up the phone these days
and she is on the other end,
precisely using her new mouth.
She forgets sometimes, of course, but she
is proud of what she remembers, and it hurts
me to hear her effort, the sum of all her dreams
this one dream, whizzing us back to that moment
50 years ago, on the Greyhound bus headed for
the Windy City from Alabama—
my southern mother in one seat, dead since Memphis,
and my northern mother in the seat next to herself,
lost in that mean, unreachable dream.
```

---

## IC-1830: An Open Letter to John Ashcroft, Attorney General of the United States

- Title: An Open Letter to John Ashcroft, Attorney General of the United States
- Author (byline): Claire Braz-Valentine
- Work: Not specified
- Publisher: San Francisco Call (Newspaper)
- Publication date as stated: Monday, May 24, 2002
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 559
- Already set (do not supply): none

### Source block (context only)

```text
Author: Claire Braz-Valentine
ISBN: N/A
Publisher: San Francisco Call (Newspaper)
Date (Month/Year): Monday, May 24, 2002
```

### Introduction (context only: never use it for content warnings)

```text
On January 28, 2002, Attorney General John Ashcroft, announced that he spent $8000 of taxpayer's money for drapes to cover up the exposed breast of The Spirit of Justice, an 18ft aluminum statue of a woman that stands in the Hall of Justice. The aluminum Art Deco statue dates from the 1930s when the Great Hall in the Justice Department was built as a grand, two-storey room to be used for department events and ceremonies. Every such narrow-minded and prudish action deserves a response, so here it is . . . An Open Letter to John Ashcroft, Attorney General of the United States by Claire Braz-Valentine.
```

### Performance text (classify this)

```text
John, John, John,
you've got your priorities all wrong.
While men fly airplanes into skyscrapers,
dive bomb the pentagon,
while they stick explosives into their shoes,
and then book a seat right next to us,
while they hide knives in their luggage,
steal kids on school buses,
take little girls from their beds at night
drive trucks into our state capital buildings,
while our president calls dangerous men all over the
world
evildoers and devils,
while we live in the threat of biological warfare
nuclear destruction,
annihilation,
you are out buying yardage
to save Americans
from the appalling
alarming, abominable
aluminum alloy of evil,
that terrible ten foot tin tittie.
You might not be able to find Bin Laden
But you sure as hell found the hooter in the hall of
justice.

It's not that we aren't grateful
But while we were begging the women of Afghanistan
To not cover up their faces
You are begging your staff members to
Just cover up that nipple
To save the American people
From that monstrous metal mammary
How can we ever thank you?

So, in your office every morning
in your secret prayer meeting
while an American woman is sexually assaulted every 6
seconds
while anthrax floats around the post office
and settles in the chest of senior citizens,
you've got another chest on your mind.
While American sons arrive home in body bags
and heat seeking missiles
fly around a foreign country
looking for any warm body
you think of another body.

And you pray for the biggest bra in the world John
because you see that breast on the spirit of justice
in the spirit of your
own inhibited sexuality.
And when we women see
our grandmothers, our mothers, our daughters, our
granddaughters,
our sisters, ourselves,
when we women see that
statue the spirit of justice
we see the spirit of strength
the spirit of survival.
While every day
we view innocent bodies dragged out of rubble
and women and children laid out
like thin limp dolls
and baptized into death as collateral damage
and the hollow eyed Afghani mother's milk has dried
up underneath her burka
in famine in shame
and her children are dead at her breast.

While you look at that breast John
that jug on the spirit of justice
and deal with your thoughts of lust
and sex and nakedness
we see it as a testimony motherhood
And you see it as a tit.

It's not the money it cost.
It's the message you send.
We've got the right to live in freedom.
We got the right to cheat Americans out
of millions of dollars and then
just not want to tell congress about it.
We've got the right
to drop bombs night and day
on a small country that has no army,
no navy, no military at all,
because we've got the right to bear arms
but we just better not even think
about not the right to bare breasts.
So now John you can be photographed
while you stand there and talk about
guns and bombs and poisons
without the breast appearing over your right shoulder
without that bodacious bosom bothering you
and we just wanted to tell you
in the spirit of justice
in the spirit of truth
John
there is still one very big boob left standing there in
that picture.
```

---

## IC-1831: Our Culture Hates Fat People - A Collection

- Title: Our Culture Hates Fat People - A Collection
- Author (byline): Rachel Wiley and Donna Ashworth
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1044
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rachel Wiley
Book: Nothing is Okay
ISBN: 978-1943735303
Publisher: Button Poetry
Date (Month/Year): March 2018
Author: Donna Ashworth
Book: Life
ISBN: 978-1785304446
Publisher: Black and White Publishing
Date (Month/Year): October 2022
```

### Introduction (context only: never use it for content warnings)

```text
Poet and body positive activist Rachel Wiley wants to change the way we look at fatness. For years as a performer and poet, Wiley did not address this topic, she said,“I think I subconsciously thought, ‘Oh, if I don’t talk about my fat, nobody else will notice.'”

The time to be silent has passed. An article in Scientific American* puts it best: “We can no longer pretend that being less likely to be hired . . . being paid less, receiving biased medical treatment, being socially excluded and bullied are attempts to help people “be healthier.” These are the direct consequences of living in a culture that vilifies and fears fat bodies and that treats the people living in them as morally lesser beings.”

Our Culture Hates Fat People – A Collection by Rachel Wiley and Donna Ashworth, including For Fat Girls Who Considered Starvation When Bulimia Wasn’t Enough, The Fat Joke and When You Cannot Bear Your Body
```

### Performance text (classify this)

```text
For Fat Girls Who Considered Starvation When Bulimia Wasn’t Enough by Rachel Wiley

(Pg 76-77) Mom says that my teeth are perfect Perfect brother has just gotten braces on his top four front

teeth
a tiny railroad bridge connecting nothing
and mom says that my teeth are perfect.
At last my quiet mouth, the overlook, the swallowed
feelings have all paid off
and cultured something perfect
and mine.
My mouth is a music box
stuffed with pearls.

Perfect brother is tall
and lean
eats whatever he wants.
One time a whole box of oatmeal cream pies.
But it is clearer each day that my baby fat
is no longer baby fat
but just fat
It is clearer each day that I will not be a ballerina.

I had wanted to be a ballerina. My mouth is a music box A small girl spins gracefully at the back of my throat

on point I am sure if I can just reach far enough back I could still

have her grace I reach for her every night after dinner while the bathtub

fills.

Until one day the health teacher shows us a photo
of a mouth crammed full of broken, yellowed dishes
says that a side effect of Bulimia
is ruined teeth
but Mom said that my teeth were perfect.
And my perfect is a ransom I cannot bring myself to pay
for the spinning girl
so I swallow her
and then nothing more for 4 whole days.
My mouth is a music box,
plays a low gear grinding that puts me to sleep.

When I do not wake up any closer to being a spinning girl encircled in pink tulle but rather still a ravenous hollow encircled in overgrowth I sneak down to the pantry and devour an entire box of oatmeal cream pies in the dark before going upstairs to brush my perfect teeth 1 at a time.

The Fat Joke by Rachel Wiley

(Pg 22-23) The old joke goes: Patient walks into the doctor’s office and says, “Doctor it hurts when I move my arm like this, what should I do? and the doctor says, “So, don’t move your arm like that”

Now,

Fat Girl walks into the doctor’s office and says, “Doctor

it hurts when I move my arm like this, what should I do?” and the

doctor
says, “Have you considered weight loss surgery?”
Fat Girl walks into the doctor for a flu shot
and gets a lecture about BMI
Fat Girl walks into the doctor’s for an earache and gets

asked if she’s ever eaten a salad Fat Girl walks into the doctor’s office with a spider bite

and the doctor obsesses over how low her blood pressure is --

low, for such a fat person anyway – and insists on checking it 3 times

before he believes it, has to be reminded of the purple mass of

throbbing spider
venom that brought her here in the first place
Fat Girl walks into the doctor’s to ask about antidepressants
and gets prescribed exercise instead
Fat Girl walks into the doctor’s office for a standard 3-

month followup appointment and the doctor says, “Have you considered

that weight
loss surgery?
Fat Girl gets tired of only ever being diagnosed as fat
so Fat Girl stops walking into the doctor’s office.

Fat Girl walks to the store
and has insults flicked at her like still-lit
cigarettes from passing cars
Fat Girl walks onto a crowded bus and stands because she

does not wish to share a seat and make anyone else uncomfortable

Fat Girl logs onto the internet, gets comments from

keyboard doctors
that claim concern for her health
suggests crash diets
suggests flat-tummy tea
suggests diet pills that would stop fat girls’ heart, but fat

girl will have
died trying to get thin
Fat Girl walks into the world and says,
“World it hurts to exist like this.”
World says, “So stop existing like that”
World says, “have you considered weight loss surgery?”
Would rather she slice herself open than to exist as she

does
side-effects be damned
Despite all of this, Fat Girl still manages to love her fat body
World says, “Stop glorifying obesity.”
Fat Girl walks up to World, says, “I do not owe you

shrinking, you know. I do not owe you thinness, attempted thinness,

or desired thinness because you assume thinness equals health. I do

not owe you health, perceived or otherwise, to receive basic respect. I

am deserving of existence. I am deserving of care. I am

deserving of first no harm done.” World says, “That is the best joke we’ve heard all day.”

When You Cannot Bear Your Body by Donna Ashworth

The days when you cannot bear to exist within your own

body, are the days you must really sit there and feel the

vessel you live in. Consider its structure, the layers, the insides. The many miraculous functions it carries out in every

moment. If it lives with disability, consider the pressure that brings to

each and every sinew.
If it is fighting illness, imagine that war within you.
Stare at your body, absorb it. Touch it.
Let the feelings of shame and disgust engulf you, and then
send them away to the universe to dispose of.
You are not your body.
You are a guest in your body and you are currently rejecting
it daily, hourly.
This rejection creates disfunction and estrangement.
It is little wonder you feel uncomfortable within your own
skin.
You are.
You, my friend, did not ruin your body, or let yourself go.

You are merely living, and life takes its toll, as it absolutely
must.
The days when you cannot bear to exist within your body,
are the days when your body needs you, so very much, to
check in.
To accept.
To apologize.
To connect.
To befriend.
Be grateful, as every guest should be.
Be tidy, be respectful, be clean.
But most of all, be good company.
You are not here for long.

NOTE: Only the 2 poems by Rachel Wiley were presented for the Award History listed.

* Source information for information contained in the introduction:

Article Title: Fat is Not the Problem Stigma Is
Authors: Linda Bacon and Amee Severson
Magazine: Scientific American
Posted On-line: July 8, 2019
https://blogs.scientificamerican.com/observations/fat-is-
not-the-problem-fat-stigma-is/#
```

---

## IC-1832: Poem About My Rights

- Title: Poem About My Rights
- Author (byline): June Jordan
- Work: The Heath Anthology of American Literature, Fifth Edition
- Publisher: Houghton Mifflin College Div
- Publication date as stated: August 2005
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 920
- Already set (do not supply): none

### Source block (context only)

```text
Author: June Jordan
Book: The Heath Anthology of American Literature, Fifth
Edition
ISBN: 978-0618714117
Publisher: Houghton Mifflin College Div
Date (Month/Year): August 2005
```

### Introduction (context only: never use it for content warnings)

```text
In West Virginia, a 20-year old African American woman is raped, tortured and brutalized for more than a week by six whites. In Saudi Arabia, a US-client state, a victim of gang-rape is herself sentenced to six months in prison and 200 lashes. Around the world, women of all classes face a crushing oppression that weighs like a mountain on their backs and that seeps into the most personal aspects of their daily lives. But, mountains can be moved and the everyday can be revolutionized. This powerful poem by June Jordan begins by describing one of the most pervasive and universal expressions of women’s oppression — the fear of walking alone at night — and develops into an all-around exposure of the oppressive family unit and capitalist imperialism and ends with a righteous call to resist. Poem About My Rights by June Jordan.
```

### Performance text (classify this)

```text
Even tonight and I need to take a walk and clear
my head about this poem about why I can't
go out without changing my clothes my shoes
my body posture my gender identity my age
my status as a woman alone in the evening/
alone on the streets/alone not being the point/
the point being that I can't do what I want
to do with my own body because I am the wrong
sex the wrong age the wrong skin and
suppose it was not here in the city but down on the
beach/
or far into the woods and I wanted to go
there by myself thinking about God/or thinking
about children or thinking about the world/all of it
disclosed by the stars and the silence:
I could not go and I could not think and I could not
stay there
alone
as I need to be
alone because I can't do what I want to do with my own
body and
who in the hell set things up
like this
and in France they say if the guy penetrates
but does not ejaculate then he did not rape me
and if after stabbing him after screams if
after begging . . . and if even after smashing
a hammer to his head if even after that if he
and his buddies *sexually attack* me after that
then I consented and there was
no rape because finally you understand finally
they *screwed* me over because I was wrong I was
wrong again to be me being me where I was/wrong
to be who I am
which is exactly like South Africa
penetrating into Namibia penetrating into
Angola and does that mean I mean how do you know if
Pretoria ejaculates what will the evidence look like the
proof of the monster jackboot ejaculation on Blackland
and if
after Namibia and if after Angola and if after
Zimbabwe
and if after all of my kinsmen and women resist even to
self-immolation of the villages and if after that
we lose nevertheless what will the big boys say will they
claim my consent:
Do You Follow Me: We are the wrong people of
the wrong skin on the wrong continent and what
in the hell is everybody being reasonable about
and according to the Times this week
back in 1966 the C.I.A. decided that they had this
problem
and the problem was a man named Nkrumah so they
killed him and before that it was Patrice Lumumba
and before that it was my father on the campus
of my Ivy League school and my father afraid
to walk into the cafeteria because he said he
was wrong the wrong age the wrong skin the wrong
gender identity and he was paying my tuition and
before that
it was my father saying I was wrong saying that
I should have been a boy because he wanted one/a
boy and that I should have been lighter skinned and
that I should have had straighter hair and that
I should not be so boy crazy but instead I should
just be one/a boy and before that
it was my mother pleading plastic surgery for
my nose and braces for my teeth and telling me
to let the books loose to let them loose in other
words
I am very familiar with the problems of the C.I.A.
and the problems of South Africa and the problems
of Exxon Corporation and the problems of white
America in general and the problems of the teachers
and the preachers and the F.B.I. and the social
workers and my particular Mom and Dad/I am very
familiar with the problems because the problems
turn out to be
me
I am the history of rape
I am the history of the rejection of who I am
I am the history of the terrorized incarceration of
my self
I am the history of battery assault and limitless
armies against whatever I want to do with my mind
and my body and my soul and
whether it's about walking out at night
or whether it's about the love that I feel or
whether it's about the sanctity of my *private parts* or
the sanctity of my national boundaries
or the sanctity of my leaders or the sanctity
of each and every desire
that I know from my personal and idiosyncratic
and disputably single and singular heart
I have been raped
be-
cause I have been wrong the wrong sex the wrong age
the wrong skin the wrong nose the wrong hair the
wrong need the wrong dream the wrong geographic
the wrong sartorial I
I have been the meaning of rape
I have been the problem everyone seeks to
eliminate by forced
penetration with or without the evidence of slime and/
but let this be unmistakable this poem
is not consent I do not consent
to my mother to my father to the teachers to
the F.B.I. to South Africa to Bedford-Stuy
to Park Avenue to American Airlines to the hardon
idlers on the corners to the sneaky creeps in
cars
I am not wrong: Wrong is not my name
My name is my own my own my own
and I can't tell you who the hell set things up like this
but I can tell you that from now on my resistance
my simple and daily and nightly self-determination
may very well cost you your life
```

---

## IC-1833: Poetry of Bonnie Parker

- Title: Poetry of Bonnie Parker
- Author (byline): Bonnie Parker (ed Alexander Baron)
- Work: Not specified
- Publisher: Alexander Baron
- Publication date as stated: 1990
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1341
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bonnie Parker (Ed Alexander Baron)
ISBN: 978-0978998967
Publisher: Alexander Baron
Date (Month/Year): 1990
```

### Introduction (context only: never use it for content warnings)

```text
To many ordinary citizens during the Great Depression, bank robbers were seen as victims of injustice driven to commit crimes -- folk heroes wreaking vengeance on a callous economic system. The notoriety of Bonnie and Clyde was bolstered by wild shootouts with police, spectacular car chases, and the romance of two lovers outside the law. But the truth of the situation wasn’t nearly so romantic. Both Bonnie and Clyde had spent time in prison before their famous shoot out and were small time gangsters. During Bonnie’s first prison stint, she penned the poem The Story of Suicide Sal which shows her initial fascination with the gangster lifestyle at the young age of 21.
```

### Performance text (classify this)

```text
The Story of Suicide Sal

We each of us have a good "alibi" For being down here in the "joint"; But few of them really are justified If you get right down to the point.

You've heard of a woman's "glory" Being spent on a "downright cur," Still you can't always judge the story As true, being told by her.

As long as I've stayed on this "island," And heard "confidence tales" from each "gal," Only one seemed interesting and truthful -- The story of "Suicide Sal."

Now "Sal" was a gal of rare beauty,
Though her features were coarse and tough;
She never once faltered from duty
To play on the "up and up."

"Sal" told me this tale on the evening
Before she was turned out "free,"
And I'll do my best to relate it
Just as she told it to me:

I was born on a ranch in Wyoming;
Not treated like Helen of Troy;
I was taught that "rods were rulers"
And "ranked" as a greasy cowboy."

Then I left my old home for the city
To play in its mad dizzy whirl,
Not knowing how little of pity
It holds for a country girl.

There I fell for "the line" of a "henchman,"
A "professional killer" from "Chi";
I couldn't help loving him madly;
For him even now I would die.

One year we were desperately happy;
Our "ill gotten gains" we spent free;
I was taught the ways of the "underworld";
Jack was just like a "god" to me.

I got on the "F.B.A." payroll
To get the "inside lay" of the "job";
The bank was "turning big money"!
It looked like a "cinch" for the "mob."

Eighty grand without even a "rumble" -- Jack was last with the "loot" in the door, When the "teller" dead-aimed a revolver From where they forced him to lie on the floor.

I knew I had only a moment --
He would surely get Jack as he ran;
So I "staged" a "big fade out" beside him
And knocked the forty-five out of his hand.

They "rapped me down big" at the station, And informed me that I'd get the blame For the "dramatic stunt" pulled on the "teller" Looked to them too much like a "game."

The "police" called it a "frame-up,"
Said it was an "inside job,"
But I steadily denied any knowledge
Or dealings with "underworld mobs."

The "gang" hired a couple of lawyers,
The best "fixers" in any man's town,
But it takes more than lawyers and money
When Uncle Sam starts "shaking you down."

I was charged as a "scion of gangland"
And tried for my wages of sin;
The "dirty dozen" found me guilty --
From five to fifty years in the pen.

I took the "rap" like good people,
And never one "squawk" did I make.
Jake "dropped himself" on the promise
That we make a "sensational break."

Well, to shorten a sad lengthy story,
Five years have gone over my head
Without even so much as a letter--
At first I thought he was dead.

But not long ago I discovered
From a gal in the joint named Lyle,
That Jack and his "moll" had "got over"
And were living in true "gangster style."

If he had returned to me sometime,
Though he hadn't a cent to give,
I'd forget all this hell that he's caused me,
And love him as long as I live.

But there's no chance of his ever coming,
For he and his moll have no fears
But that I will die in this prison,
Or "flatten" this fifty years.

Tomorrow I'll be on the "outside"
And I'll "drop myself" on it today;
I'll "bump 'em" if they give me the "hotsquat"
On this island out here in the bay...

The iron doors swung wide next morning
For a gruesome woman of waste,
Who at last had a chance to "fix it,"
Murder showed in her cynical face.

Not long ago I read in the paper
That a gal on the East Side got "hot,"
And when the smoke finally retreated
Two of gangdom were found "on the spot."

It related the colorful story
of a "jilted gangster gal."
Two days later, a "sub-gun" ended
The story of "Suicide Sal."

TRANSITION

Bonnie and Clyde remained at large until a Texas posse ambushed them on May 23, 1934. Dying together in a proverbial hail of bullets—the Texas lawmen fired over 187 rounds into the couple—helped perpetuate the romance surrounding their short, desperate, and destructive lives.

But during their crime spree, Bonnie Parker sent poems and photographs to newspapers, heralding the Barrow Gang’s exploits and defending her honor. Her poem The Story of Bonnie and Clyde (aka The Trail’s End), depicts the pair as populist desperadoes, misunderstood and star-crossed lovers driven to a life of crime.

The Story of Bonnie and Clyde (aka The Trail’s End)

You’ve read of the tale of Jesse James –
Of how he lived and died,
But if you’re in need
Still of something to read,
Here’s the story of Bonnie and Clyde.

No Bonnie and Clyde are the Barrow gang,
And I’m sure that you all will have read,
How they rob and they steal,
And the lowlife who squeal
Are found dead with a slug through the head.

There are lots of untruths to these write ups, For they’re neither as ruthless as that, Though their nature is raw And they hate all the law – The stool pigeons, the spotters and rats.

People say they are cold-blooded killers, Claiming they are both heartless and mean, But I say this with pride, That when first I met Clyde He was honest and upright and clean.

But the law fooled around,
Kept on sending him down,
And kept locking him up in a cell,
Until he said to me:
“I will never be free,
So I’ll meet a few of them in Hell.”

The road they took was dimly lighted,
There were no highway signposts to guide,
But they made up their minds
If the roads were all blind
That they wouldn’t give up till they died.

The road’s growing dimmer and dimmer,
Until sometimes you hardly can see,
But it’s fight man to man,
Get as far as you can,
For they know they can never be free.

From heartbreak many people have suffered,
And from weariness many have died,
But take it in all,
People’s troubles are small
Till they end up like Bonnie and Clyde.
If a lawman is shot down in Dallas,
And they haven’t a clue or a guide,
If they can’t find a fiend,
They just wipe their slate clean
And announce it was Bonnie and Clyde.

There are only two crimes in this country They’ve not tried to pin on Barrow’s mob, It’s said they had no hand in the kidnap demand Nor the Kansas City depot job.

A newspaperboy said to his buddy:
“I wish Bonnie and Clyde would get jumped,
In these awful hard times
We would make a few dimes
If a handful of cops would get bumped.”

The police haven’t go the report yet,
But I heard from Clyde only today,
He said: Don’t start no fights,
Cos we ain’t working nights,
We’re joining up with the NRA.

From Irving to West Dallas viaduct
Is what’s known as the Great Divide,
Where the women are kin,
And the men are real men,
And they won’t “stool” on Bonnie and Clyde.

If they tried to act like decent citizens
And rented a nice little flat,
About the third night
They’d receive an invite
From a sub-machine gun’s rat-tat-tat.

They don’t think they’re too tough or desperate,
They realize the law always wins,
They’ve been shot at before,
But they neither ignore
That death must be the price of their sins.

Some day soon they will go down together,
And they’ll bury the two side by side,
To few it’ll be grief,
To the law a relief . . .
But it’s death for Bonnie and Clyde.
```

---

## IC-1834: Portrait of a Bulimic

- Title: Portrait of a Bulimic
- Author (byline): Ally Sheedy
- Work: Yesterday I Saw the Sun
- Publisher: Summit Books
- Publication date as stated: February 1991
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 704
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ally Sheedy
Book: Yesterday I Saw the Sun
ISBN: 978-0671731304
Publisher: Summit Books
Date (Month/Year): February 1991
```

### Introduction (context only: never use it for content warnings)

```text
Ally Sheedy, a member of the Brat Pack, who you may remember from The Breakfast Club and Saint Elmo’s Fire, was a precocious child. She didn’t start off wanting to be an actress, however; her first love was dance. She began studying with the American Ballet Theatre when she was 6, and performed professionally with the company well into her adolescence. In high school, she bridged the gap into acting when she began to do commercials and also when she spiraled down into the depths of bulimia – a potentially deadly disorder in which one binges and purges in a desperate attempt to be thin. According to the U.S. National Eating Disorders Association, approximately 4.7 million females and 1.5 million males suffer from bulimia.

Portrait of a Bulimic by Ally Sheedy
```

### Performance text (classify this)

```text
She lay on the heavy crocheted bedspread looking at her distended stomach.

I have done it again, she thinks.

She rolls to her side feeling
the bloat
the skin
stretched so tightly
over her abdomen she fears
it will rupture.

A beached pink whale.

She can't move can't think can't speak

a whole box of chocolate

Piece after
gooey
gummy
rich
piece
stuffed into
my mouth

faster and faster and faster until
I can't taste
or chew
or stop
only endlessly repeat
hand to mouth
hand to mouth
hand to mouth

Chocolate from my employers I am a dancer she thinks-then laughs-and cries and tries to lean over the side of the bed and vomit all her insides out.

If they could see me now, she thinks They'd wonder why they ever thought of hiring me. They'd certainly want their chocolate back. In its original condition.

She lies back on the pillows and closes her eyes.
She sees herself as the Rose
dancing in the musical garden
promoting feminine deodorant.

What good fortune
a windfall
landing this
commercial.

A dancing rose Fasting for three days Starving for two weeks

So high so empty so alive.

How did I lose it?

She feels for weight under her chin around her hipbones inside her thighs.

She feels the fat cells accumulating senses them growing in big globs all over her body.

She can't move.

It was just yesterday . . . she spent the night twirling in sparkling pink sequins and a tight-waisted gauze skirt.

Such fine bones, said the director.
Such a tiny waist.
She nods, glows, dances up a storm
High on caffeine and saccharine and her own slight
self.

3 A.M. -- Dizzy with exhaustion, reeling with success, taking off her

makeup.
I did it!
I am a dancer -- I look like one, act like one –
I have won!
No one has guessed a single solitary thing about me.
The prized pink dress hangs limply on its hanger.

She is in her underwear.
Dusty mirror.
tired sweat-streaked weak
sunken stomach
ribs
thin arms.
I did it, she says. There is no joy, only tenuous relief.

Behind the cold cream
half-hidden
half-eaten
an old package of Hostess powdered donuts.

a hand frozen in mid-air.
No, she says. No.
a small panic moving in her stomach
No.

Squelching stuffing stop crying hunger in my body -- dance clothes into my gym bag a silent ongoing chant: you can't you mustn't you are not

allowed

Good-bye, dressing room
Good-bye, commercial
Good-bye, rose dancer
and pink dress that isn't hers
that she'll never wear again.

Tomorrow I won't be pretty, pink, and fine-boned.
Tomorrow I'll just be myself
smoking, auditioning again, and in a black leotard.
I can't get those steps
always off the beat
never on top of anything.
endlessly tired -- falling short of the mark –
isn't that another definition of sin?
dieting and dieting and dieting

she pinches her body and sees it fat
sees it ugly wide and clumsy
it never changes no matter what she does
desperately does

Then today she lost it.

Walked into a waiting room filled with glowing girls. She was sure they had looked at her funny. You are nothing, said their eyes. You are a stick of wood, a mannequin, nothing. I am transparent, she realized. I have yet to appear. Yet to be recognized and gladly welcomed.

At the doorstep of her cold dark apartment
A box of chocolate lay waiting.
Thank you, said the note.
I am Alice in Wonderland.
One side makes you smaller and the other makes you tall.
Eat me, said the note.

Oh, please -- just one -- oh, please . . . They sent it to me! Tearing through it, eating up the thought, the sweat,

and leotards
glowing girls and sparkling pink dresses
but alive finally
madly greedily terribly ALIVE.
Eating everything in the world and squashing and getting

it
grabbing it stuffing it in and down
I hate you, she said.
I'll kill you, she said with each exhilarating sinful and

angry chocolate bite.

Now she lies on the bed. Sick and once more passing slowly into oblivion. Oh, how I hate you.

I close my eyes.
```

---

## IC-1835: The Princess Saves Herself in This One

- Title: The Princess Saves Herself in This One
- Author (byline): Amanda Lovelace
- Work: Not specified
- Publisher: Andrews McMeel Publishing
- Publication date as stated: Feb 2017
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 875
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amanda Lovelace
ISBN: 978-1449486419
Publisher: Andrews McMeel Publishing
Date (Month/Year): Feb 2017
```

### Introduction (context only: never use it for content warnings)

```text
But this collection of poetry is a story of rising from the ashes of abuse – of surviving. The fact is, a knight in shining armor may never arrive to save you . . . you may be the one who has to save yourself.

The Princess Saves Herself in This One by Amanda Lovelace.
```

### Performance text (classify this)

```text
(Pg 5) ah, life-
the thing that happens to us
while we're off somewhere else
blowing on dandelions

& wishing ourselves into the pages of our favorite fairy tales.

(Pg 1) warning: this is not a fairy tale.
there is no princess.
there is no damsel.
there is no queen.
there is no tower.
there are no dragons.
there is simply a girl
faced with the difficult task
of learning to believe in
herself.

(Pg 11) the queen
my mother smiled
as she offered
a cube of
sugar
in her upturned palm.
greedily,
i accepted.
i reached inside my mouth,
delicately placing one (just one)
on the center of my tongue, & i clamped down.
salt.
that is what abuse is: knowing you are going to
get salt
but still hoping for sugar for nineteen years.

- you may be gone, but i still have a

stomachache.

(Pg 15) there are some mothers who will warn you to never ever

(ever ever)
touch the stove,
but there are
some mothers who
will drag you right to it
kicking & screaming, laughing
as they
watch the flames lick at your fingertips.

- when you're taught to see the world through

fire, nothing looks safe.

(Pg 10) the little girl
isn't listening to you-
she's way too busy staring out the window,
fantasizing about
a world of
magical accidents, flying envelopes,
screeching owls, adoring giants,
brooms that
do more than sweep,
friends who are always loyal,
& a train
that will take her
to an enchanted place far far far
away from
here.

- put under a lifelong spell.

(Pg 34) birds can't
fly away when you
clip
one of
their wings.
you
weren't satisfied with just clipping one of
my wings.
you tore both
out from the root
to make sure i could
never fly anywhere
ever
again.

- mother & daughter.

(Pg 186) just because they don't hit you
doesn't mean it isn't
abuse.
wouldn't you think it
a crime
to look up at
the night sky & tell
the stars
that they have no sparkle?
guess what? you shine brighter
than all the starlight
there has
ever been
or ever
will be.

- emotional abuse is still abuse.

(Pg 41) you may
not have left (many) bruises on my skin,
but you left giant blackberry bruises all over
my soul.

- i still wonder who i would have been.

(Pg 154) i hope you
can find it in your heart
to be proud
of the woman
i have become in spite
of
you.

- still hoping for sugar instead of salt.

TRANSITION

And yet, despite everything; we will always yearn for the love of our mothers. Time heals all wounds, right? Wrong. Sometimes, time is stolen from us and there is no time to heal those relationships. Then what do you do? What do you do if you are only 19 and your mother, no matter how horrible she was, is no longer there?

(Pg 65) you will think
your parents are
shatterproof until one day
you find out
t h e y a r e n ' t.

- what it really means to lose your innocence.

(Pg 62) my
mom
told the nice doctor
she was seeing starbursts
in her eyes
& they were almost beautiful
to her-
like the
fourth of
july
had decided to come early.
the doctor hesitated before
breaking the news to her.
"those aren't stars.
it's cancer."

- forty years a smoker.

(Pg 64) when your mother begins to forget your
name,
you begin
to wonder
if you exist
at all.

- stage 4, terminal.

(Pg 88) an image: a girl
with bruises underneath her eyes
from sleeping too much or too little.
a girl
with a
brokenhearted cat permanently
cradled in her
arms.
a girl
ignoring the piles of treasured books
surrounding
all sides
of her.
a girl
unable to bring herself to cry because if she
finally cries then that means
it really happened.
is
there
such a
thing
as
dead mother's day?

(Pg 78) i was the one
who found your body
(you were nowhere
to be found),
mouth opened
wide enough
to suck all the oxygen from the room,
wide enough
to plant lilies in,
wide enough to have been calling my name-
that is, if only you remembered it.

- i want to forget, forget, forget.

(Pg 102) i am
caught between mourning
you
&
thinking
your death saved
me.

- will you ever be able to forgive me?

(Pg 96) f*** the idea that there is such a thing
as destiny,
that there exists
some kind of mysterious master plan, that there
is a god who simply
does not
give us anything we cannot handle.
the pain
did not
make me
a better person. it did not
teach me not to take anything for granted.
it did not
teach me anything except how
to be afraid
to love anyone.
1 am
far too
young
to be so broken
&
if i could go back in time
& give
myself
her childhood back,
i would.

- what was the point? (Pg 103) the princess jumped from the tower & she learned that she could fly all along.

- she never needed those wings.

(Pg 1) this is not a fairy tale.
there is no princess.
there is no damsel.
there is no queen.
there is no tower.
there are no dragons.
there is simply a girl
faced with the difficult task
of learning to believe in
herself.

(Pg 182) repeat after me: you owe no one your forgiveness.

- except maybe yourself.

(Pg 153) i am
A lioness
who is no longer
afraid to let the world
hear her roar.
```

---

## IC-1836: Renovation

- Title: Renovation
- Author (byline): Naomi Shihab Nye
- Work: You & Yours: Poems
- Publisher: BOA Editions, Ltd.
- Publication date as stated: 2005
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 959
- Already set (do not supply): none

### Source block (context only)

```text
Author: Naomi Shihab Nye
Book: You & Yours: Poems
ISBN: 978-1929918690
Publisher: BOA Editions, Ltd.
Date(Month/Year): 2005
```

### Introduction (context only: never use it for content warnings)

```text
Put together one very run-down house, a deserving family, several opinionated designers, seven days and what do you get? The answer is Extreme Makeover: Home Edition. The lives of the lucky families are forever changed when they learn that they've been selected to have their home walls moved, their floors replaced and even their facades radically changed. And America has been consumed with the need to watch the events unfold for the last 6 years! When Naomi Shihab Nye faces her own minor home improvement project, the built in frustrations become more than just a personal challenge . . . they become a reason to reflect on the situations of families in her home country of Palestine. It truly takes reflections on those less fortunate than our selves to make us appreciate what we do have. Renovation by Naomi Shihab Nye.
```

### Performance text (classify this)

```text
It cheered me that the man and woman ripping our house apart were a married couple. Maybe this meant they would be more careful with things. Delia neatly packed all the belongings from the rooms where mold was detected in large cardboard boxes marked KITCHEN ITEMS and BATH – the mugs, spatulas, pots and pans, towels, bottles of shampoo. Chico draped large sheets of plastic from the 13-foot high ceilings for “containment.” Then they both donned plastic space suits and face masks and began smashing the hundred year old green and white tile of the kitchen counter and the blue Mexican bird tile in the bathroom to take it out. The mold was under wood and sheet rock. It likes to eat adhesive. A very subversive guest. Goodbye familiar cracks and rounded edges. Goodbye heavy wooden drawers and stained porcelain bathtub. Our neighbors looked scared when they saw the spacemen in the yard. We moved out for five weeks.

Old is not a very glamorous topic, but it could be growing inside anybody’s walls at any moment, finding its own safe harbor of moist secrecy, spreading and thickening in green or black creepy glory. You could have it too. We had mostly green but a little black. It gave me asthma even before it started sneaking out of a hole in the ceiling over the bathtub. Thanks to a leak in the roof and two other unrelated leaks in two wall-pipes we had it. Our hundred-year-old cottage was sabotaged. But considering all the possibilities for leakage in this world, it amazes me that more things don’t leak. It amazes me that poop goes into the poop pipe and relatively clean water comes out of the faucet. It all amazes me. I know some people who have had to bulldoze their entire houses and throw away all their belongings thanks to mold. Delia called me into the front yard to see the boards from our bathroom wrapped in plastic. She pointed. There, there it is. See those little black and green spots? It is going away now. We are hauling it to the DUMP. You won’t have it any more.

So we moved back into our house without any running water or toilets, it was like camping out at home. We ate peaches and icy cherry tomatoes from a big bowl. We drank coffee and made rum drinks in the afternoons, trying to replicate the happy hour at the hotel down the street, but it did not feel as fun. We drove around in the summer heat through traffic to gaze at tile and bathroom fixtures in too many stores and talked to carpenters and lighting experts and tried to make decisions. There are some people in the world who are good at doing this. We are not among them. And then we waited. Fore someone to come measure. Fore substances to arrive from different directions. For things not to be broken. For them to be re-ordered. For someone to be able to put them in. Renovation involves mostly waiting. For the electrician who knows you cannot deal with those wires yourself. For the evangelical electrician’s helper who looks uncannily like my gynecologist. For the diverter switch to arrive at a plumbing warehouse. For windows. For the counter installers who asked, how do you make a rose bush have more roses? What does it want and need? We started receiving mysterious catalogues like “Rest Room World.” During all this, the Palestinians overseas were being confined to their homes, if they had homes, or to their shacks, rooms, tents, and hovels. They could not go out to buy fresh oranges. They could not go to school.

More houses were being seized and demolished daily. The word “demolished” sounds softer than it is. But in the documentary movie “Gaza Strip” you can hear the terrifying crashing sounds of giant bulldozers as they knock down houses a hundred years old. One gets tired of saying or hearing the words but it keeps happening. The whole time we were putting our house back together, more Palestinians were losing their homes. They saw their fathers blindfolded, hauled off to prison in buses. They saw their friends gassed by poison, blown up, intestines strewn in the dust. Their mothers wailing and bloody. Why is this almost never considered news? Sometimes where everything comes from is just as critical as where everything in going.

I hate this, said the teenager we live with, one rare night when I asked him to help me wash and rinse dishes in a pan in the yard. We had had company for dinner. It was fun to have company with no running water or bathroom. They were a little taken aback. I poured water over their hands from a pitcher. They tried not to look at all the boxes piled up in the dining room. The teenager scraping plates said, how long is this going to go on? Don’t some people get their whole houses rebuilt in, like, a week? Why is it taking so long for this to be completed?

Just think, I said to him. (This is never a good idea to say to a teen person, but I said it anyway.) Just consider someone coming and taking our house away, while we’re in the middle of fixing things, while everything is a mess. How would you feel? They would say your room is their room. Your computer is now their computer. Or they would blow up your room and say, Ah, too bad, we call it security, no one cares if you suffer.

What are you talking about? he said. I’d call the police! What if you had no phone lines? What if the police had no power? Stop talking like this. The mosquitoes are killing me. I hate washing dishes.
```

---

## IC-1837: Rumpelstiltskin

- Title: Rumpelstiltskin
- Author (byline): Anne Sexton
- Work: Transformations, Pgs 17-24
- Publisher: Mariner Books
- Publication date as stated: Feb 2001
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 832
- Already set (do not supply): none

### Source block (context only)

```text
Author: Anne Sexton
Book: Transformations, Pgs 17-24
ISBN: 978-0618083435
Publisher: Mariner Books
Date (Month/Year): Feb 2001
```

### Introduction (context only: never use it for content warnings)

```text
Fairytales have a power few realize. The stories shape many of our fantasies as children; but they also condition us to accept traditional gender roles. Anne Sexton understood their power and influence as she transformed the tales into her own unique poetic voice.

Her poetic rendition of Rumpelstiltskin takes a grim and twisted approach to the already Grimm and twisted original. More than just a child’s fairytale . . . lying beneath the surface whispers a commentary on the burdens and fears of women in a society shaped by men.

Rumpelstiltskin by Anne Sexton
```

### Performance text (classify this)

```text
(Pg 17-24) Inside many of us
is a small old man
who wants to get out.
No bigger than a two-year-old
whom you'd call lamb chop
yet this one is old and malformed.
His head is okay
but the rest of him wasn't Sanforized?
He is a monster of despair.
He is all decay.
He speaks up as tiny as an earphone
with Truman's asexual voice:
I am your dwarf.
I am the enemy within.
I am the boss of your dreams.
No. I am not the law in your mind,
the grandfather of watchfulness.
I am the law of your members,
the kindred of blackness and impulse.

See. Your hand shakes.
It is not palsy or booze.
It is your Doppelganger
trying to get out.
Beware. . . Beware. . .

There once was a miller
with a daughter as lovely as a grape.
He told the king that she could
spin gold out of common straw.
The king summoned the girl
and locked her in a room full of straw
and told her to spin it into gold
or she would die like a criminal.
Poor grape with no one to pick.
Luscious and round and sleek.
Poor thing.
To die and never see Brooklyn.

She wept,
of course, huge aquamarine tears.
The door opened and in popped a dwarf.
He was as ugly as a wart.
Little thing, what are you? she cried.
With his tiny no-sex voice he replied:
I am a dwarf.
I have been exhibited on Bond Street
and no child will ever call me Papa.
I have no private life.
If I'm in my cups the whole town knows by breakfast
and no child will ever call me Papa
I am eighteen inches high.
I am no bigger than a partridge.
I am your evil eye
and no child will ever call me Papa.

Stop this Papa foolishness,
she cried. Can you perhaps
spin straw into gold?
Yes indeed, he said,
that I can do.
He spun the straw into gold
and she gave him her necklace
as a small reward.
When the king saw what she had done
he put her in a bigger room of straw
and threatened death once more.
Again she cried.
Again the dwarf came.
Again he spun the straw into gold.
She gave him her ring
as a small reward.
The king put her in an even bigger room
but this time he promised
to marry her if she succeeded.
Again she cried.
Again the dwarf came.
But she had nothing to give him.

Without a reward the dwarf would not spin.
He was on the scent of something bigger.
He was a regular bird dog.
Give me your first-born
and I will spin.
She thought: Piffle!
He is a silly little man.
And so she agreed.
So he did the trick.
Gold as good as Fort Knox.

The king married her
and within a year
a son was born.
He was like most new babies,
as ugly as an artichoke
but the queen thought him in pearl.
She gave him her dumb lactation,
delicate, trembling, hidden,
warm, etc.
And then the dwarf appeared
to claim his prize.

Indeed! I have become a papa!
cried the little man.
She offered him all the kingdom
but he wanted only this -
a living thing
to call his own.
And being mortal
who can blame him?

The queen cried two pails of sea water.
She was as persistent
as a Jehovah's Witness.
And the dwarf took pity.
He said: I will give you
three days to guess my name
and if you cannot do it
I will collect your child.
The queen sent messengers
throughout the land to find names
of the most unusual sort.
When he appeared the next day
she asked: Melchior?

Balthazar?
But each time the dwarf replied:
No! No! That's not my name.
The next day she asked:
Spindleshanks? Spiderlegs?
But it was still no-no.
On the third day the messenger
came back with a strange story.
He told her:
As I came around the corner of the wood
where the fox says good night to the hare
I saw a little house with a fire
burning in front of it.
Around that fire a ridiculous little man
was leaping on one leg and singing:
Today I bake.
Tomorrow I brew my beer.
The next day the queen's only child will be mine.
Not even the census taker knows
that Rumpelstiltskin is my name...
The queen was delighted.
She had the name!

Her breath blew bubbles.

When the dwarf returned
she called out:
Is your name by any chance Rumpelstiltskin?
He cried: The devil told you that!
He stamped his right foot into the ground
and sank in up to his waist.
Then he tore himself in two.
Somewhat like a split broiler.
He laid his two sides down on the floor,
one part soft as a woman,
one part a barbed hook,
one part papa,
one part Doppelganger.
```

---

## IC-1838: Rwanda

- Title: Rwanda
- Author (byline): Ai
- Work: Vice: New and Selected Poems
- Publisher: W.W. Norton
- Publication date as stated: June 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 810
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ai
Book: Vice: New and Selected Poems
ISBN: 978-0393320183
Publisher: W.W. Norton
Date (Month/Year): June 2000
```

### Introduction (context only: never use it for content warnings)

```text
Beginning on April 6, 1994, Hutus began slaughtering the Tutsis in the African country of Rwanda. As the brutal killings continued, the world stood idly by and watched the slaughter. Lasting 100 days, the Rwanda genocide left over 800,000 Tutsis men, women and children dead. Since bullets were expensive, most were killed by machetes or clubs. Many were tortured before being killed. Some of the victims were given the option of paying for a bullet so that they'd have a quicker death. To further degrade the Tutsi, Hutu extremists would not allow the Tutsi dead to be buried. Their bodies were left where they were slaughtered, exposed to the elements, eaten by rats and dogs.

In Rwanda by Ai – we are thrust into the center of the genocide and experience the horror through the eyes of a young girl. Rwanda by Ai.
```

### Performance text (classify this)

```text
My neighbor used to come to our hut,
bringing melons so sweet
I thought I should not eat them,
because I would die
and haunt my family like a ghost
with hard, black seeds for eyes.
One day, he brought his uncle and two friends
and they asked my father to go outside with them.
I thought he had come to get permission to marry me
and I was glad because I loved him,
even though he wasn't a member of my tribe,
nor as educated as I was.
I wanted to stay,
but my mother gave me a basket of clothes
to wash at the river.
She said, “Don’t come back,
Until they are as clean as the Virgin Mary’s soul.”
“Mother,” I said, “I’ll never come back then.”
“Shall I take my brother?” I asked,
as he ran to my father’s side.
I was laughing, when she hissed, “Run,”
And I did because she frightened me.
As I rounded the hut,
I heard the tat, tat, tat, from guns
Like the one the soldiers carry.
I ran faster, still holding the basket.

It was frozen to my hands
And I still held it, even as I jumped in the river.
I thought I would die, so I closed my eyes.
When something bumped against me,
I opened them and saw my father’s body.
As he floated past me,
His arm hooked around my neck,
Almost taking me under
And I released the basket.
I reached for my father, as bullets hit the water
And I dove under him.
His body shielded me, until I couldn’t breathe
And had to break the surface for air.
When I crawled onto the riverbank,
I hid in the grass behind the church.
Finally, when I was sure no one was around,
I beat on the rectory door,
Until the priest opened it. “Hide me, Father,” I begged.
Once inside, I was overjoyed to see my mother.
She told me when my neighbor shot at her,
She pretended to be dead
And while he dumped my father in the river,
She escaped and came here,
Hoping I had survived.
She said we needed another place to hide,
But she could only find a small closet-size space
Behind the alter, covered by a sheet of tin.
Only one of us could fit, so she made me go in
And covered the hold again.
When I heard screaming, I kicked the tin aside
And saw my mother on fire.
I tried to help her, using only my hands,
But when she was completely covered in flames,
I broke the stained-glass window
With a statue of Saint Joseph and climbed out.
As I crawled back to the river,
A shiver of wind passed over me
Through the grass and trees.
When I stopped to rest,
Fear coiled around me like a snake,
But when I told myself I would not let them kill me,
It took the shape of a bird and flew away.

I crawled back to the church,
Because I wanted to find my mother’s ashes,
So I could bury them,
But my way was blocked by the rebels,
So I waited until dark.
Maybe I slept. I don’t know.
When I heard my neighbor’s voice,
It was as if I had awakened from a dream.
Relief flooded over me, until I sat up
And saw him standing above me, holding a machete.
“Sister,” he said, “I won’t hurt you.”
I knew he was lying and I tried to get away,
But I was too weak
And he fell on top of me, tearing at my clothes.
When he was finished raping me,
I thought he would kill me,
But he only brought the machete close to my head,
Then let it fall from his hands.
Dawn had come to the village
With more killing on its mind.
I heard screams and pleas for mercy,
Then I realized those sounds were inside me.
They would never leave.
Now I am always talking to the dead.
Their bones are rattling around in my head.
Sometimes I can’t hear anything else
And I go to the river with my son and cry.
When he was a few days old,
I took him there for the first time.
I stood looking at the water,
Which was still the color of blood,
Then I lifted him high above my head,
But my mother’s bones said, “Killing is a sin,”
So I took him home
To raise him as if he really is my son
And not the issue of my neighbor,
Who has returned to torment me
With skin that smells like burning flesh,
But in my heart I know
Both his mother and father died long ago
And left this orphan to grow like a poisoned flower

beside the open grave that was my country.
```

---

## IC-1839: Shapechangers in Winter

- Title: Shapechangers in Winter
- Author (byline): Margaret Atwood
- Work: Morning in the Burned House
- Publisher: Houghton Mifflin Harcourt
- Publication date as stated: 1995
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 760
- Already set (do not supply): none

### Source block (context only)

```text
Author: Margaret Atwood
Book: Morning in the Burned House
ISBN: 978-0395825211
Publisher: Houghton Mifflin Harcourt
Date (Month/Year): 1995
```

### Introduction (context only: never use it for content warnings)

```text
My grandparents have a marriage I greatly admire. While I’m sure that grandma and grandpa have their share of differences, they seem to really enjoy being with each other. They’ve been married for 40 years, and despite the graying hair, wrinkling skin and widening waists, their affection appears to have deepened. In fact, they even seem to embrace the aging process! They have always seemed so in sync.

Everyone talks about people growing and changing over time. And I’m sure the same is true of a marriage. Circumstances change. New situations arise. Marriages need to adjust.

How could the terms of a marriage contracted at 25 possibly be the same at 50 or 60 or 70? It makes sense that marriages need to be flexible. But facing the need to change can be frightening and threatening. Shapechanging in Winter by Margaret Atwood.
```

### Performance text (classify this)

```text
1. Through the slit of our open window, the wind comes in and flows around us, nothingness in motion, like time. The power of what is not there. The snow empties itself down, a shadow turning to indigo, obliterating everything out there, roofs, cars, garbage cans, dead flowerstalks, dog turds, it doesn’t matter. You could read this as indifference on the part of the universe, or else a relentless forgiveness: all of our scratches and blots and mortal wounds and patched-up jobs wiped clean in the snow’s huge erasure.

I feel it as a pressure,
an added layer:
above the white waterfall of snow
thundering down; then attic, moth-balled
sweaters, nomadic tents,
the dried words of old letters;
then stairs, then children, cats and radiators, peeling
paint,
us in our bed, the afterglow
of a smoky fire, our one candle flickering;
below us, the kitchen in the dark, the wink
of pots on shelves; then books and tools, then cellar
and furnace, graying dolls, a bicycle,
the whole precarious geology of house
crisscrossed with hidden mousetrails,
and under that a buried river
that seeps up through the cement
floor every spring,
and the tree roots snouting their slow way
into the drains;
under that, the bones
of our ancestors, or if not theirs, someone’s,
mixed with a biomass of nematodes;
under that, bedrock, then molten
stone and the earth’s fiery core;
and sideways, out into the city, street
and corner store and mall
and underpass, then barns and ruined woodlands,
continent
and island, oceans, mists
of story drifting
on the tide like seaweed, animal
species crushed and blinking out,
and births and illnesses, hatred and love infra-
red, compassion fleshtone, prayer ultra-
violet; then rumours, alternate waves
of sad peace and sad war,
and then the air, and then the scintillating ions,
and then the stars. That’s where
we are.

2.
Some centuries ago, when we lived at the edge
of the forest, on nights like this
you would have put on your pelt of a bear
and shambled off to prowl and hulk
among the trees, and be a silhouette of human
fears against the snowbank.
I would have chosen fox;
I liked the jokes,
the doubling back on my tracks,
and, let’s face it, the theft.
Back then, I had many forms:
the sliding in and out
of my own slippery eelskin,
and yours as well; we were each other’s
iridescent glove, the deft body
all sleight-of-hand and illusion.
Once we were lithe as pythons, quick
and silvery as herring, and we still are, momentarily,
except our knees hurt.
Right now we’re content to huddle
under the shed feathers of duck and goose
as the wind pours like a river
we swim in by keeping still,
like trout in a current.
Every cell
in our bodies has renewed itself
so many times since then, there’s
not much left, my love,
of the originals. We’re footprints
becoming limestone, or think of it
as coal becoming diamond. Less
flexible, but more condensed;
and no more scales or aliases,
at least on the outside. Though we’ve accumulated,
despite ourselves, other disguises:
you as a rumpled elephant—
hide suitcase with white fur,
me as a bramble bush. Well, the hair
was always difficult. Then there’s
the eye problems: too close, too far, you’re a blur.
I used to say I’d know you anywhere,
but it’s getting harder.

3.
This is the solstice, the still point
of the sun, its cusp and midnight,
the year’s threshold
and unlocking, where the past
lets go of and becomes the future;
the place of caught breath, the door
of a vanished house left ajar.

Taking hands like children
lost in a six-dimensional
forest, we step across.
The walls of the house fold themselves down,
and the house turns
itself inside out, as a tulip does
in its last full-blown moment, and our candle
flares up and goes out, and the only common
sense that remains to us is touch,

as it will be, later, some other
century, when we will seem to each other
even less what we were.
But that trick is just to hold on
through all appearances; and so we do,
and yes, I know it’s you;
and that is what we will come to, sooner
or later, when it’s even darker
than It is now, when the snow is colder,
when it’s darkest and coldest
and candles are no longer any use to us
and the visibility is zero: Yes.
It’s still you. It’s still you.
```

---

## IC-1840: Shrinking Women and Revenge of the Crazy Wimmin

- Title: Shrinking Women and Revenge of the Crazy Wimmin
- Author (byline): Lily Myers and Leah Harris
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1480
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lily Myers
Book: Viral
ISBN: 978-0989641517
Publisher: Button Poetry
Date (Month/Year): Dec 2013
Author: Leah Harris
Book: Word Warriors
ISBN: 978-0786750726
Publisher: Seal Press
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
There is a pull in our society to mute a woman’s voice until it coos. To control it. To silence it. And still, she speaks. She tries to be heard. But often her voice is ignored, or belittled, mocked, critiqued or shouted down. Should she speak up and risk being seen as “pushy,” “opinionated,” or God forbid . . . “a feminist?” Or does she accept the status quo, hold her tongue and simply “shrink?” Shrinking Women by Lily Myers
```

### Performance text (classify this)

```text
Maya Angelou once said: A wise woman wishes to be no one’s enemy; [but] a wise woman refuses to be anyone’s victim . . . You see, according to Leah Harris, “Words have the terrible power to dehumanize and destroy, but they also have the tremendous power to heal and rebuild that which has been destroyed.”

Shrinking Women

Across from me at the kitchen table, my mother smiles

over red wine that she drinks out of a measuring

glass. She says she doesn’t deprive herself, but I’ve learned to find nuance in every movement of her

fork. In every crinkle in her brow as she offers me the

uneaten pieces on her plate. I’ve realized she only eats dinner when I suggest it. I wonder what she does when I’m not there to do so.

Maybe this is why my house feels bigger each time I

return; it’s proportional. As she shrinks the space around her seems increasingly

vast. She wanes while my father waxes. His stomach has

grown round with wine, late nights, oysters, poetry. A

new girlfriend who was overweight as a teenager, but

my dad reports that now she’s “crazy about fruit.”

It was the same with his parents; as my grandmother became frail and angular her

husband swelled to red round cheeks, round stomach and I wonder if my lineage is one of women shrinking making space for the entrance of men into their lives not knowing how to fill it back up once they leave.

I have been taught accommodation.
My brother never thinks before he speaks.
I have been taught to filter.
“How can anyone have a relationship to food?” He asks,

laughing, as I eat the black bean soup I chose for its

lack of carbs.
I want to tell say: we come from difference, Jonas,
you have been taught to grow out
I have been taught to grow in
you learned from our father how to emit, how to

produce, to roll each thought off your tongue with

confidence, you used to lose your voice every other

week from shouting so much I learned to absorb I took lessons from our mother in creating space around

myself I learned to read the knots in her forehead while the

guys went out for oysters and I never meant to replicate her, but spend enough time sitting across from someone and you

pick up their habits

That’s why women in my family have been shrinking for

decades. We all learned it from each other, the way each

generation taught the next how to knit weaving silence in between the threads which I can still feel as I walk through this ever-growing

house, skin itching, picking up all the habits my mother has unwittingly

dropped like bits of crumpled paper from her pocket on her countless trips from bedroom to

kitchen to bedroom again, Nights I hear her creep down to eat plain yogurt in the

dark, a fugitive stealing calories to which she does

not feel entitled. Deciding how many bites is too many How much space she deserves to occupy.

Watching the struggle I either mimic or hate her, And I don’t want to do either anymore but the burden of this house has followed me across the

country I asked five questions in genetics class today and all of

them started with the word “sorry”. I don’t know the requirements for the sociology major

because I spent the entire meeting deciding whether

or not I could have another piece of pizza
a circular obsession I never wanted but
inheritance is accidental
still staring at me with wine-stained lips from across the

kitchen table.

TRANSITION Once the chains of silence are broken; finding our true voice is fraught with pitfalls. Silenced anger turns inward resulting in lowered self-esteem, self-loathing and a myriad of mental health issues. Leah Harris is the daughter of two parents who were diagnosed with schizophrenia at an early age. Leah, too, was once a suicidal mental patient who spent most of her adolescence in and out of psychiatric institutions – medicated into silence. Finally at the age of 18, she made the decision to reject the drugs and diagnoses and to strike out on her own – a noncompliant, crazy girl. The following poem was presented at a National Conference on women and psychiatric oppression. Revenge of the Crazy Wimmin by Leah Harris Revenge of the Crazy Wimmin the man's always had a plan to slow down the velocity of woman's journeys to lower the volume of woman's voices saying hush now honey be calm be still the powers that be saying there's an appropriate level for your grief and there's a healthy range for your rage and when woman exceeds the emotional speed limit society put on the brakes

and the more things change
the more they stay
the same
they use the same tactics
but they just change the names

back in the middle ages
they burned unruly women at the stake
and out of the ashes of their bones and flesh
rose the Enlightenment and Reason fresh
and the white men declared
there's no such thing as witches
they're just crazy psycho-bitches
but we certainly can't let them run free
lock 'em up and throw away the key
yeah they said: lock 'em up and throw away the key

cause there's nothing scarier than a woman mad and/or
aware of her own magic
tragic how much violence is done
in the name of science
to ensure our silence

in Victorian times they located suffering in our uterus in the blood in the soft internal organs took our pain our righteous rage they called it "hysteria" and then Dr. Freud ignored women's horror stories herstories of abuse and rape and took a justified hatred of the penis and called it envy (he sold more books that way)

what they call paranoia
we call reality hitting us hard
when we name the forces all around
conspiring to keep us down
when we deny the diagnoses of our masters
when we refuse to be sick, defective, diseased,

disordered, disturbed
when we dare to proclaim our humanity
when we accuse them of insanity
they call it "lack of insight"
into our condition

but we got an insight that'll blind you

we know something about our conditions
and how we came to be confined:
our husbands our kids they wanted our house our money
yeah it's kinda funny how it goes down
we were visionaries who shared our visions with the

wrong people we were too poor too butch too ugly too far-gone on the

mean streets
we seen *things* nobody should ever have to see
we got raped got beat got tortured by strangers and
the ones who claimed to love us
and when life comes apart at the seams
when the castles of our dreams implode
we chase the needle in search of the next high
put on a skirt, *sleep with* who we have to just to get

by
and when our demons chase us till
we break up
from the pure exhaustion of being alive
and you're lucky if you survive, honey
yeah, you're lucky if you survive

first: there's a diagnosis for every tragedy then they sign the forms lock us up put us in solitary shame us call us names tell us we won't amount to

nothing
wrestle us down to the ground with their male arms
"treat" us -- tie us up naked bruised and shaking
dope us up with their drugs so we can't stand
can't write can't paint can't think can't speak
wrap us in white sheets (when we ain't dead yet)
take our babies from us
lobotomize us sterilize us electroshock us
rape us kill us
saying this is for your own good
this is for your own good
this is for
your own good

this is for all the mamas daughters sisters lovers

friends
who ended up behind bars
and this is for every woman who died alone
in a locked cell
this is for every woman who's ever survived hell
and emerged to tell the tale to her sisters
our voices thick with saliva and blood speaking
truth my sisters truth my fellow witches unreasonable

women yes we are "acting out" cackling at the scourge of normalcy as defined by the men waging endless war a la 1984 we diagnose them with "mass destruction disorder" and write out a prescription for the maximum dose of justice

and out on the horizon
gather the storm-clouds of our retaliation
in a collective conflagration
we are rising up
picking up the scattered pieces of what shattered
building and birthing out new visions for the generations

to come
with our rage of the ages
the force of our breath
we are shaking off death
and taking in life
the crazy wimmin
gonna have the last laugh someday
and it's gonna be
loud
```
