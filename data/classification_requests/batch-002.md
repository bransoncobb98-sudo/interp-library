# Classification request: batch 2 of 63 (40 records, IC-0041 to IC-0080)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-002-reply.json`.

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

## IC-0041: There Will Come Soft Rains

- Title: There Will Come Soft Rains
- Author (byline): Ray Bradbury
- Work: The Harper Anthology of Fiction
- Publisher: Addison-Wesley Pub Co
- Publication date as stated: Jan 1997
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2223
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ray Bradbury
Book: The Harper Anthology of Fiction
ISBN: 978-0673396341
Publisher: Addison-Wesley Pub Co
Date (Month/Year): Jan 1997
```

### Introduction (context only: never use it for content warnings)

```text
Published in 1920, Sara Teasdale’s poem "There Will Come Soft Rains" envisions an idyllic post-apocalyptic world in which nature continues peacefully, beautifully, and indifferently after the extinction of humankind.

But Ray Bradbury’s future is quite different and much less peaceful. The future is now! Alexa, Siri, and Google Assistants have expanded their abilities and technology reigns supreme. Smart homes cater to our every need . . . until society destroys itself and a radioactive glow fills the skies.

There Will Come Soft Rains by Ray Bradbury
```

### Performance text (classify this)

```text
There will come soft rains and the smell of the ground,

And swallows circling with their shimmering sound;

And frogs in the pools singing at night,

And wild plum trees in tremulous white;

Robins will wear their feathery fire,

Whistling their whims on a low fence-wire;

And not one will know of the war, not one

Will care at last when it is done,

Not one would mind, neither bird nor tree,

If mankind perished utterly;

And Spring herself, when she woke at dawn

Would scarcely know that we were gone.

In the living room the voice-clock sang, Tick-tock, seven o'clock, time to get up, time to get up, seven o'clock! as if it were afraid that nobody would. The morning house lay empty. The clock ticked on, repeating and repeating its sounds into the emptiness. Seven-nine, breakfast time, seven-nine!

In the kitchen the breakfast stove gave a hissing sigh and ejected from its warm interior eight pieces of perfectly browned toast, eight eggs sunny side up, sixteen slices of bacon, two coffees and two cool glasses of milk.

"Today is August 4, 2026," said a second voice from the kitchen ceiling, "in the city of Allendale, California." It repeated the date three times for memory's sake. "Today is Mr. Featherstone's birthday. Today is the anniversary of Tilita's marriage. Insurance is payable, as are the water, gas, and light bills."

Somewhere in the walls, relays clicked, memory tapes glided under electric eyes.

Eight-one, tick-tock, eight-one o'clock, off to school, off to work, run, run, eight-one! But no doors slammed, no carpets took the soft thread of rubber heels. It was raining outside. The weather box on the front door sang quietly: "Rain, rain, go away; rubbers, raincoats for today…" And the rain tapped on the empty house, echoing.

Outside, the garage chimed and lifted its door to reveal the waiting car. After a long wait the door swung down again.

At eight-thirty the eggs shriveled and the toast was like stone. An aluminum wedge scraped them into the sink, where hot water whirled them down a metal throat which digested and flushed them away to the distant sea. The dirty dishes were dropped into a hot washer and emerged twinkling dry.

Nine-fifteen, sang the clock, time to clean.

Out of warrens in the wall, tiny robot mice darted. The rooms were a crawl with the small cleaning animals, all rubber and metal. They thudded against chairs, whirling their mustached runners, kneading the rug nap, sucking gently at hidden dust. Then, like mysterious invaders, they popped into their burrows. Their pink electric eyes faded. The house was clean.

Ten o'clock. The sun came out from behind the rain. The house stood alone in a city of rubble and ashes. This was the one house left standing. At night the ruined city gave off a radioactive glow which could be seen for miles.

Ten-fifteen. The garden sprinklers whirled up in golden founts, filling the soft morning air with scatterings of brightness. The water pelted windowpanes, running down the charred west side where the house had been burned, evenly free of its white paint. The entire west face of the house was black, save for five places. Here the silhouette in paint of a man mowing a lawn. Here, as in a photograph, a woman bent to pick up flowers. Still farther over, their images burned on wood in one titanic instant, a small boy, hands flung into the air; higher up, the image of a thrown ball, and opposite him, a girl, hands raised to catch a ball which never came down.

The five spots of paint—the man, the woman, the children, the ball—remained. The rest was a thin charcoaled layer.

The gentle sprinkler rain filled the garden with falling light.

Until this day, how well the house had kept its peace. How carefully it had inquired, "Who goes there? What's the password?" and, getting no answer from lonely foxes and whining cats, it had shut up its windows and drawn shades in an old-maidenly preoccupation with self—protection which bordered on mechanical paranoia.

It quivered at each sound, the house did. If a sparrow brushed a window the shade snapped up. The bird, startled, flew off! No, not even a bird must touch the house! The house was an altar with ten thousand attendants, big, small, servicing attending, in choirs. But the gods had gone away, and the ritual of the religion continued senselessly, uselessly.

Twelve noon.

A dog whined, shivering, on the front porch.

The front door recognized the dog voice and opened. The dog, once huge and fleshy, but now gone to bone and covered with sores, moved in and though the house, tracking mud. Behind it whirred angry mice, angry at having to pick up mud, angry at inconvenience.

For not a leaf fragment blew under the door but what the wall flipped open and the copper scrap rats flashed swiftly out. The offending dust, hair, or paper, seized in miniature steel jaws, was raced back to the burrow. There, down the tubes which fed into the cellar, it was dropped into the sighing vent of an incinerator which sat like evil Baal in a dark corner.

The dog ran upstairs, hysterically yelping to each door, at least realizing, as the house realized, that only silence was there.

It sniffed the air and scratched the kitchen door. Behind the door the stove was making pancakes which filled the house with a rich baked odor and the scent of maple syrup.

The dog frothed at the mouth, lying at the door, sniffing, its eyes turned to fire. It ran wildly in circles, biting at its tail, spun in a frenzy, and died. It lay in the parlor for an hour.

Two o'clock, sang a voice.

Delicately sensing decay at last, the regiments of mice hummed out as softly as blown gray leaves in an electrical wind.

Two-fifteen.

The dog was gone.

In the cellar, the incinerator glowed suddenly and a whirl of sparks leaped up the chimney.

Two thirty-five.

Bridge tables sprouted from patio walls. Playing cards fluttered onto pads in a shower of pips. Martinis manifested on an oaken bench with egg-salad sandwiches. Music played.

But the tables were silent and the cards untouched.

At four o'clock the tables folded like butterflies back though the paneled walls.

Four-thirty.

The nursery walls glowed.

Animals took shape: yellow giraffes, blue lions, pink antelopes, lilac panthers cavorting in crystal substance. The walls were glass. They looked upon color and fantasy. Hidden fills clocked though well-oiled sprockets, and the walls lived. The nursery floor was woven to resemble a crisp, cereal meadow. Over this ran aluminum roaches and iron crickets, and in the hot still air butterflies of delicate red tissue wavered among the sharp aroma of animal spoors! There was the sound like a great matted yellow hive of bees within a dark bellows, the lazy bumble of a purring lion. And there was the patter of okapi feet and the murmur of a fresh jungle rain, like other hoofs, falling upon the summer-starched grass. Now the walls dissolved into distances of parched weed, mile on mile, and the warm endless sky. The animals drew away into thorn brakes and water holes. It was the children's hour.

Five o'clock. The bath filled with clear hot water.

Six, seven, eight o'clock. The dinner dishes manipulated like magic tricks, and in the study a click. In the metal stand opposite the hearth where a fire now blazed up warmly, a cigar popped out, half an inch of soft gray ash on it, smoking, waiting.

Nine o'clock. The beds warmed their hidden circuits, for nights were cool here.

Nine-five. A voice spoke from the study ceiling: "Mrs. McClellan, which poem would you like this evening?" The house was silent.

The voice said at last, "Since you express no preference, I shall select a poem at random." Quiet music rose to back the voice. "Sara Teasdale. As I recall, your favorite…"

There will come soft rains and the smell of the ground,

And swallows circling with their shimmering sound;

And frogs in the pools singing at night,

And wild plum trees in tremulous white;

Robins will wear their feathery fire,

Whistling their whims on a low fence-wire;

And not one will know of the war, not one

Will care at last when it is done,

Not one would mind, neither bird nor tree,

If mankind perished utterly;

And Spring herself, when she woke at dawn

Would scarcely know that we were gone.

The fire burned on the stone hearth and the cigar fell away into a mound of quiet ash in its tray. The empty chairs faced each other between the silent walls, and the music played.

At ten o'clock the house began to die.

The wind blew. A falling tree bough crashed through the kitchen window. Cleaning solvent, bottled, shattered over the stove. The room was ablaze in an instant!

"Fire!" screamed a voice. The house lights flashed, water pumps shot water from the ceilings. But the solvent spread on the linoleum, licking, eating, under the kitchen door., while the voices took it up in chorus: "Fire, fire, fire!"

The house tried to save itself. Doors sprang tightly shut, but the windows were broken by the heat and the wind blew and sucked upon the fire.

The house gave ground as the fire in ten billion angry sparks moved with flaming ease from room to room and then up the stairs. While scurrying water rats squeaked from the walls, pistoled their water, and ran for more. And the wall sprays let down showers of mechanical rain.

But too late. Somewhere, sighing, a pump shrugged to a stop. The quenching rain ceased. The reserve water supply which had filled baths and washed dishes for many quiet days was gone.

The fire crackled up the stairs. It fed upon Picassos and Matisses in the upper halls like delicacies, baking off the oily flesh, tenderly crisping the canvases into black shavings.

Now the fire lay in bed, stood in windows, changed the colors of drapes!

And then, reinforcements. From attic trapdoors, blind robot faces peered down with faucet mouths gushing green chemical.

The fire backed off, as even an elephant must at the sight of a dead snake.

Now there were twenty snakes whipping over the floor, killing the fire with a clear cold venom of green froth.

But the fire was clever. It had sent flame outside the house, up through the attic to the pumps there. An explosion! The attic brain which directed the pumps was shattered into bronze shrapnel on the beams.

The fire rushed back into every closet and felt of the clothes hung there.

The house shuddered, oak bone on bone, its bared skeleton cringing from the heat, its wire, its nerves revealed as if a surgeon had torn the skin off to let the red veins and capillaries quiver in the scalded air. Help, help! Fire! Run, run! Heat snapped mirrors like the first brittle winter ice. And the voices wailed. Fire, fire, run, run, like a tragic nursery rhyme, a dozen voices, high, low, like children dying in a forest alone, alone. And the voices fading as the wires popped their sheathings like hot chestnuts. One, two, three, four, five voices died.

In the nursery the jungle burned. Blue lions roared, purple giraffes bounded off. The panthers ran in circles, changing color, and ten million animals, running before the fire, vanished off toward a distant steaming river . . . Ten more voices died.

In the last instant under the fire avalanche, other choruses, oblivious, could be heard announcing the time, cutting the lawn by remote-control mower, or setting an umbrella frantically out and in, the slamming and opening front door, a thousand things happening, like a clock shop when each clock strikes the hour insanely before or after the other, a scene of maniac confusion, yet unite; singing, screaming, a few last cleaning mice darting bravely out to carry the horrid ashes away! And one voice, with sublime disregard for the situation, read poetry aloud in the fiery study, until all the film spools burned, until all the wires withered and the circuits cracked.

The fire burst the house and let it slam flat down, puffing out skirts of spark and smoke.

In the kitchen, an instant before the rain of fire and timber, the stove could be seen making breakfasts at a psychopathic rate, ten dozen eggs, six loaves of toast, twenty dozen bacon strips, which, eaten by fire, started the stove working again, hysterically hissing!

The crash. The attic smashing into kitchen and parlour. The parlour into cellar, cellar into sub-cellar. Deep freeze, armchair, film tapes, circuits, beds, and all like skeletons thrown in a cluttered mound deep under.

Smoke and silence. A great quantity of smoke.

Dawn showed faintly in the east. Amount the ruins, one wall stood alone. Within the wall, a last voice said, over and over gain and again, even as the sun rose to shine upon the heaped rubble and steam:

Today is August 5, 2026, today is August 5, 2026, today is . . .
```

---

## IC-0042: Twilight: Los Angeles, 1992

- Title: Twilight: Los Angeles, 1992
- Author (byline): Anna Deavere Smith
- Work: Not specified
- Publisher: Anchor Books
- Publication date as stated: March 1994
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1518
- Already set (do not supply): none

### Source block (context only)

```text
Author: Anna Deavere Smith
ISBN: 978-0385473767
Publisher: Anchor Books
Date (Month/Year): March 1994
```

### Introduction (context only: never use it for content warnings)

```text
The 1992 Los Angeles riots, also known as the Rodney King uprising or the Rodney King riots, were sparked on April 29, 1992 when a predominately white jury acquitted four police officers accused in the videotaped beating of black motorist Rodney King when he resisted arrest following a high-speed car chase. Thousands of blacks in the Los Angeles area joined in what is known as a race riot involving acts of law-breaking including looting, assault, arson and murder. In all, 53 people died during the riots. Anna Deavere Smith offers a stark insight into the complex and pressing social, economic, and political issues that fueled the flames in the wake of the Rodney King verdict by dramatizing her interviews with a racially diverse population at the scene of the riots. Travel back to me now to . . . . . Twilight: Los Angeles, 1992 by Anna Deavere Smith.
```

### Performance text (classify this)

```text
Elvira Evers, General Worker and Cashier, Canteen Corporation

With a baby bottle in her hand. At her kitchen table. A black woman from Panama in her forties. Children can be heard off stage. A Panamanian accent. She has a gold front tooth.

So it was like a carnival out there
and I say
to my friend Frances
"Frances, you see this?"
and she said, "Girl, you should see
that
it's getting worst."
And I say, "Girl, let me take my butt
up there before something happen."
And, um,
when somebody throw a bottle
and I just. . .
then I felt
like moist,
and it was like a tingling sensation, right?
And I didn't like this,
and it was like itchin',
and I say, "Frances, I'm bleedin'."
And she walk with me to her house.
And she say, "Lift up your gown, let me see."
She say, "Elvira, it's a bullet!"
I say, "What?"

I say, "I didn't heard nothin'."
She say, "Yes, but it's a bullet."
She say, "Lay down there. Let me call St. Francis and tell them that you been shot
and to send an ambulance."
And she say,
"Why you?
You don't mess with none of those people.
Why they have to shoot you?"
So Frances say the ambulance be here in fifteen minutes.
I say, "Frances,
I cannot wait that."
I say,
"I'm goin'!"
So I told my oldest son, I say,
"Amant, take care your brothers.
I be right back."
Well, by this time he was standing there, he was crying,
all of them was crying.
What I did for them not to see the blood
I took the gown and I cover it
and I didn't cry.
That way they didn't get nervous.
And I get in the car.
I was goin' to drive.
Frances say, "What you doin'?"
I said, "I'm drivin'."
She say, "No, you're not!"
And we take all the back streets,
and she was so supportive,
because she say, "You all right?
You feel cold?
You feel dizzy?
The baby move?"
She say, "You nervous?"
I say, "No, I'm not nervous, I'm just worried about the baby."
I say, "I don't want to lose this baby."
She say, "Elvira, everything will be all right." She say, "Just pray." So there was a lot of
cars, we had to be blowing the horn.
So finally we get to St. Francis
and Frances told the front-desk office, she say,
"She been shot!"
And they say, "What she doin' walkin'?"
And I say, "I feel all right."
Everybody stop doin' what they was doin'
and they took me to the room
and put the monitor to see if the baby was fine
and they find the baby heartbeat,
and as long as I heard the baby heartbeat I calmed down,
long as I knew whoever it is, boy or girl, it's all right,
and
matter of fact, my doctor, Thomas, he was there
at
the emergency room.
What a coincidence, right?
I was just lookin' for that familiar face,
and soon as I saw him
I say, "Well, I'm all right now."
Right?
So he bring me this other doctor and then told me,
"Elvira, we don't know how deep is the bullet.
We don't know where it went. We gonna operate on
you.
But since that we gonna operate we gonna take the baby out
and you don't have to
go through all of that."
They say, "Do you understand
what we're saying?"
I say, "Yeah!"
And they say, "Okay, sign here."
And I remember them preparing me
and I don't remember anything else.
Nella!
No.

(Turns to the side and admonishes the child)
She likes company.
And in the background
I remember Dr. Thomas say, "You have a six-pound-twelve-ounce little girl. "
He told me how much she weigh and her length
and he
say, "Um,
she born,
she had the bullet in her elbow,
but when we remove. . .
when we dean her up
we find out that the bullet was still between two joints,
so we did operate on her and your daughter is fine
and you are fine."

(Sound of a little child saying "Mommy")
Nella!
She wants to show the baby
Jessica.
Bring the baby.

(She laughs) Yes, yes.

We don't like to keep the girls without earrings, we like the little girls
to look like girls from little.
I pierce hers.
When I get out on Monday,
by Wednesday I did it,
so by Monday she was five days,
she was seven days,
and I
pierced her ears,
and the red band is just like for evil eyes.
We really believe in Panama. . .
in English I can't explain too well.
And her doctor, he told,
he explain to me
that the bullet
destroyed the placenta
and
went through me
and she caught in her arms.

(Here you can hear the baby making noise, and a bell rings) If she didn't caught it in her
arm,
me and her would be dead.
See?
So it's like
open your eyes,
watch what is goin' on.

Mrs. Young-Soon Han, Former Liquor Store Owner (Korean)

When I was in Korea
I used to watch many luxurious, Hollywood-lifestyle movies; I never saw any poor men,
any black,
maybe one housemaid.
Until last year
I believed America is the best.
I still believe it.
I don't deny that now
because I'm victim,
but
as
the year ends in '92
and we were still in turmoil
and having all the financial problems
and mental problems.
Then a couple months ago
I really realized that
Korean immigrants were left out
from this
society and we were nothing.
What is our right?
Is it because we are Korean?
Is it because we have no politicians?
Is it because we don't
speak good English?
Why?
Why do we have to be left out?

(She is hitting her hand on the coffee table) We are not qualified to have medical treatment. We are not qualified to get, uh, food stamps

(She hits the table once) not GR

(Hits the table once) no welfare.

(Hits the table once) Anything. Many Afro-Americans

(Two quick hits)
who never worked,
(One hit)
they get
at least minimum amount

(One hit) of money

(One hit) to survive.

(One hit) We don't get any.

(Large hit with full hand spread) Because we have a car

(One hit) and we have a house.

(pause six seconds)
And we are high taxpayers. (One hit. Pause fourteen seconds) Where do I finda [sic]
justice?
Okay, black people
probably
believe they won
by the trial?
Even some complains only half right.
Justice was there.
But I watched the television
that Sunday morning,
early morning as they started.
I started watch it all day.

They were having party and then they celebrated,
all of South Central,
all the churches.
They finally found that justice exists
in this sodety.
Then where is the victims' rights?
They got their rights
by destroying innocent Korean merchants.
They have a lot of respect,
as I do,
for
Dr. Martin King?
He is the only model for black community.
I don't care Jesse Jackson.
But
he was the model
of nonviolence.
Nonviolence?
They like to have hiseh [sic] spirits.
What about last year?
They destroyed innocent people.

(pause five seconds) And I wonder if that is really justice

(And a very soft" ah" after "justice," like "justiceah," but very quick) to get their rights in this way.

(pause thirteen seconds)
I waseh swallowing the bitternesseh,
sitting here alone and watching them.
They became all hilarious

(pause three seconds)
and, uh,
in a way, I was happy for them
and I felt glad for them.
At least they got something back, you know.
Just let's forget Korean victims or other victims
who are destroyed by them.
They have fought
for their rights

(One hit simultaneous with the word "rights") over two centuries

(One hit simultaneous with" centuries")
and I have a lot of sympathy and understanding for them. Because of their effort and
sacrificing,
other minorities, like Hispanic
or Asians,
maybe we have to suffer more
by mainstream,
you know.
That's why I understand,
and then
I like to be part of their
'joyment.
But.. .
that's why I had mixed feeling
as soon as I heard the verdict.
I wish I could
live together
with eh [sic] blacks,
but after the riots
there were too much differences.
The fire is still there
how do you call it?
igni. . .
igniting fire.

(She says a Korean word, "Dashi yun gi ga nuh") It canuh burst out anytime.

Twilight Bey, Organizer of Gang Truce

So a lot of times when I've brought up ideas to my homeboys, they say, "Twilight,
that's before your time,
that's something you can't do now."
When I talked about the truce back in 1988,
that was something they considered before its time,
yet in 1992
we made it
realistic.
So to me it's like I'm stuck in limbo,
like the sun is stuck between night and day
in the twilight hours.
You know,
I'm in an area not many people exist.
Nighttime to me
is like a lack of sun,
and I won't affiliate
darkness with anything negative.
I affiliate
darkness with what was first,
because it was first,
and then relative to my complexion.
I am a dark individual,
and with me stuck in limbo,
I see darkness as myself.
I see the light as knowledge and the wisdom of the world and

understanding others,
and in order for me to be a, to be a true human being,
I can't forever dwell in darkness,
I can't forever dwell in the idea,
just identifying with people like me and understanding me and mine. So twilight
is
that time
between day and night,
limbo;
I call it limbo.
```

---

## IC-0043: A Week in the Life of Death

- Title: A Week in the Life of Death
- Author (byline): David Gavin
- Work: Living Easter through the Year
- Publisher: Liturgical Press
- Publication date as stated: 2005
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1187
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Gavin
Book: Living Easter through the Year
ISBN: 0814631525
Publisher: Liturgical Press
Date(Month/Year): 2005
```

### Introduction (context only: never use it for content warnings)

```text
Who on earth was this Jesus of Nazareth, then? How come we make such world-shattering claims about him? A Week in the Life of Death by David Gavin
```

### Performance text (classify this)

```text
Monday. Dear Diary: It’s me again - Death. The big D. What a day! Busy, busy, busy. Bit like yesterday. And the day before. And the day before that. Tragic cases really. Some so beautiful. Some so young. Oh, I nearly wept, you know – but in the end I didn’t bother. Well, must finish. Busy evening ahead.

Tuesday. Dear Diary: I suppose you think it’s a bit soft, Death writing a diary. But I don’t really get to stop and meet anyone to chat. Oh, I meet people. I meet everyone. Met them all, the great philosophers, the great religious leaders. Great wits, great thinkers. (Great twits, great stinkers.) But it’s all so brief and to the point. Always. ALWAYS!

Wednesday. Dear Diary: Two big battles fought today. One in, oh – Er, thingamy and another in, Wherever-it-is. Now myself, I prefer famines and plagues – then you get a good steady business over a period. Battles – well, you’re rushed off your feet! D’you know, diary. I can’t understand these people. They spend half their time scared stiff of me and trying to avoid me, and then they have a battle! Tuh!

Thursday. Dear Diary: Death. The final frontier where Captain James T. Kirk must boldly go! I’m pretty impressive really, don’t you think? It’s the ultimate statistic, you know: one in one die. … Yes, I like that – the ultimate. THE ULTIMATE.

Friday. Dear Diary: The ultimate here. Interesting day today. A carpenter’s son from Nazareth. Been a lot of fuss about him. Died well (Thoughtful – then snaps out of it) if you can die well! A bit like saying, ‘I failed well’. A bit like saying, ‘I swallow dived off a 100 foot cliff into the yawning mouth of a great white shark and got full marks for style’. Huh!

Saturday. Dear Diary (Slower): Funny feeling today. Like when you’ve eaten something that doesn’t agree with you. Still, death must go on! Yes, that’s a much more sensible saying: ‘Life must go on’ – that’s drivel! Not in my experience. Life must – life must grovel! (Pause) But I do feel strange.

Sunday - Easter Sunday – AD 30. (As if sick) : Dear Diary: (Looks straight ahead shocked and as if swearing) JESUS CHRIST! Death of death, and Hell’s destruction!

At first sight, he was no more than a wandering preacher – perhaps a prophet like the prophets of old; calling people to take God more seriously than they’d been used to; gathering a little band of followers – but nobody to be taken very seriously, certainly no threat to the authorities.

But then, some odd stories started circulating. Healing people. Healing them even on the Sabbath – when the religious leaders told everyone that doing things like that on the Sabbath wasn’t allowed for human beings. Why, even God himself had rested on the seventh day! And then he started telling people that their sins were forgiven. Who did he think he was? Surely he knew that only God could forgive sins?

No wonder his little band of followers started asking who he was. Who he really was, that is. He must be someone very special.

There was a moment of insight once, early in the morning on the top of a mountain, when three of them had an unearthly experience and seen him enveloped in a superhuman glory. After that, they really did begin to think that something was afoot.

But then, it had begun to go wrong.

He came into Jerusalem at the head of a demonstration. He challenged the Temple authorities and trashed their money-tables. And that really did start the opposition going. At supper on the Thursday evening, he talked about spilling his blood, but being remembered for ever because of it. That night, one of his own group led the police to where he was, and it was clear that the net was tightening round him.

The disciples began to think that, after all, they had been fooled. Peter may have seen the glory on the Mount of the Transfiguration, but in the courtyard that Thursday night he lost his nerve completely, and swore he had never known the man from Nazareth.

And the Temple authorities knew all along that they had a trouble-maker to get rid of, or else there might be a riot.

They didn’t recognize who he was. As he was being killed, Jesus was heard to pray for his executioners - ‘Father, forgive them; they don’t know what they’re doing.’ As St Paul was to say a few years later, the rulers of this present world didn’t know the hidden wisdom of God. If they had, they wouldn’t have crucified the Lord of Glory. The disciples didn’t know, either, or they wouldn’t have scattered. And Thomas certainly didn’t know, or he’d have believed the others when they told him what they’d seen on the first Easter evening.

It took a long time for the message of Easter to strike home. For forty days the disciples were huddled together, waiting for the tap on the door that’d tell them they were under arrest, like Jesus’d been under arrest. They needed to be visited by the risen Jesus – not once, not twice, but many times – before the implications of what’d happened were obvious enough for them to go out onto the streets and tell everyone about it.

But in the end they were convinced; so convinced, that nothing could stop them. It was true that Jesus was the death of death and hell’s destruction. His death on the Cross wasn’t the end of everything, but the beginning. When he’d said that the bread and the wine were his body and his blood, he meant that his life would go on for ever, and those who ate the bread and drank the wine in remembrance of him would be part of that life for ever.

‘I am convinced’, said St Paul, ‘that nothing can separate us from the love of God – not death, nor life, nor things present nor things to come, nor height nor depth nor anything else in all creation.’ Death cannot separate us from the love of God. Oh, yes; death still happens – and for some people, it will be harder than for others. The Resurrection of Jesus doesn’t stop us dying. But death can’t any longer separate us from the love of God. Because of the Resurrection, we know that the way to death is no longer a one-way street – Jesus has come back. And it is no longer a dead end – we go on from death to life eternal.

Death of death, and hell’s destruction.

Do we recognize that? Or are we like Thomas, thinking that the Good News of the Gospel is just too good to be true? Or like Peter in the High Priest’s courtyard, ready to be embarrassed if there’s any danger of being recognized as a follower of Jesus?

Pray God to give you the conviction to believe that Jesus really is the death of death and hell’s destruction; pray that he may give you the courage to act on that conviction when the time comes to bear witness to the truth of the Resurrection.

Because Christ is risen! He is risen indeed! Alleluia!

Thanks be to God. Amen.
```

---

## IC-0044: Widows and Children First!

- Title: Widows and Children First!
- Author (byline): Harvey Fierstein
- Work: Torch Song Trilogy
- Publisher: Samuel French, Inc.
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ARNOLD, MA
- Teaser before the introduction: No
- Spoken words (computed): 2034
- Already set (do not supply): none

### Source block (context only)

```text
Author: Harvey Fierstein
Book: Torch Song Trilogy
ISBN: 978-0573690105
Publisher: Samuel French, Inc.
```

### Introduction (context only: never use it for content warnings)

```text
Two things you should know:

1) Arnold is the gay son of a Jewish mother who is an expert at avoiding the truth.

2) He and his partner Allen had plans to adopt a son from the foster care system . . . a

teen-age boy named David who social services felt would benefit from have two well-

adjusted gay parents, to help him deal with his own homosexuality.

Unfortunately for everyone, Allen did not live to see the adoption through. And now Arnold’s mother, still grieving the death of her own husband has arrived for a visit. The stage is set for . . . Widows and Children First! By Harvey Fierstein
```

### Performance text (classify this)

```text
ARNOLD: [Coming out of kitchen and speaking to David (off-stage)] Did your teacher happen to mention how Oscar Wilde came to be imprisoned? He was in jail for being gay.

MA: [Embarrassed] Arnold, I can't find the oil.

ARNOLD: In a minute, Ma. See, ten years earlier, the Parliament passed a law against homosexuality. And Oscar Wilde had this young lover named . .

MA: Arnold, could you please give me a hand?

ARNOLD: Just a second. His name was Lord Alfred. Now, Lord Alfred's father found out about them and started causing scenes in public; chasin' 'em outta hotels and stuff.

MA: For God's sake, Arnold. Could you change the subject?

ARNOLD: [Annoyed] I'll finish later. [Goes back to kitchen] I wish you wouldn't interfere like that; it's very embarrassing.

MA: Excuse me, but listening to that is very embarrassing.

ARNOLD: I'm sorry you feel that way, but I have a responsibility to his education.

MA: I am sure that the people who put him here did not have that kind of education in mind.

ARNOLD: The people who put him here had exactly that kind of education in mind. And I'll thank you not to interfere.

MA: I am only suggesting that you should consider the huge responsibility you've taken on here.

ARNOLD: You think I'm unaware of it?

MA: Then act like it. You should be setting an example for the boy.

ARNOLD: And I'm not?

MA: Not when you talk like that, you're not. You've got to consider what you say to him for the remaining time. He's at an impressionable age. After all it's only for a few more months.

ARNOLD: What's for a few more months?

MA: He's here on a nine-month program, right? And he's already been here six months, so . . .

ARNOLD: And what do you think happens then?

MA: He leaves.

ARNOLD: David is here on a nine-month program, but after that, if we agree and the Bureau of Child Welfare allows, I will legally adopt David. And believe me, Ma, if I have anything to say about it, he's not leaving. [Ma tries to say something, she is angry, confused, frustrated. She throws down whatever is in her hands and sits on couch. Arnold follows and stands staring at her. Sits next to her. Pause] Is this it? We gonna sit and stare into space?

MA: You want I should do a Bubble Dance? Frankly, Arnold, you've done a lot of crazy things, but this . . . ?

ARNOLD: Adopting David is not a crazy thing. It's a wonderful thing that I'm very proud of.

MA: If you're so proud how come you were too ashamed to tell your mother? Everything else you tell me. You shove your sex-life down my throat like aspirin; every hour on the hour. But six months he's been here and not a word. Why?

ARNOLD: Ma . . . Y'know, you're not the easiest person in the world to talk to.

MA: What did I say? Do I tell you how to run your life? You want to know why you didn't tell me about this? I'll tell you why: Because you knew it was wrong.

ARNOLD: That's not true.

MA: No?

ARNOLD: No! This isn't something I decided to do overnight. We put in our application more than two years ago.

MA: Who "we"?

ARNOLD: Alan and I.

MA: The two of you were going to do this together? Now I've heard everything.

ARNOLD: That's what I love about you; you're so open minded.

MA: Alright. So, Alan's not here. Why's the kid?

ARNOLD: Because with everything else I forgot about the application. Then, one day, the phone rang. It was the foster parent program and they had David for us. I told them what happened to Alan and they said I could probably take David anyway.

MA: And you said, "send him on over."

ARNOLD: Not at first. But then I thought it all through, called them back and said yes . . . On a trial basis.

MA: I'm glad you got a money-back guarantee, but you still haven't told me why you wanted him.

ARNOLD: Because I was tired of widowing. Widow-ing . . . feeling sorry for myself, cursing every time I passed a couple walking hand in hand, watching Tear Jerkers on T.V. knowing they could only cheer me up. Christ, of all the things going down here, I was sure that was the one thing I wouldn't have to explain.

MA: How should I know about Wida-whating? Did you ever say a word to me?

ARNOLD: I didn't think I had to. Christ, it's only been three years since daddy died.

MA: Wait, wait, wait, wait, wait. Are you trying to compare my marriage with you and Alan? [Haughty and incensed] Your father and I were married for thirty-five years, had two children and a wonderful life together. What loss did you have? You fooled around with some boy. You have the nerve to compare that to a marriage of thirty-five years?

ARNOLD: You think it doesn't? Ma, I lost someone that I loved very much . . .

MA: So you felt bad. Maybe you cried a little. But what would you know about what I went through? Thirty-five years I lived with that man. He got sick, I brought him to the hospital and you know what they gave me back? A paper bag with his watch, wallet and wedding ring. How could you possibly know what that felt like. It took me two months until I could sleep in our bed alone, a year to learn to say "I" instead of "we." And you're going to tell me you were "widowing." How dare you!

ARNOLD: You're right, Ma. How dare I. I couldn't possibly know how it feels to pack someone's clothes in plastic bags and watch the garbage pickers carry them away. Or what it feels like to forget and set his place at the table. How about the food that rots in the refrigerator because you forgot how to shop for one? How dare I? Right, Ma? How dare I?

MA: [Starting over his speech and continuing until her exit] May God strike me dead! Whatever I did to my mother to deserve a child speaking to me this way. The disrespect! I only pray that one day you have a son and that he'll talk to you like this. The way you talk to me.

ARNOLD: [Over her speech] Listen, Ma, you had it easy. You have thirty-five years to remember, I have five. You had it easy, Ma. You lost your husband in a nice clean hospital, I lost mine out there. They killed him there on the street. Twenty-three years old laying dead on the street. Killed by a bunch of kids with baseball bats. [Ma has fled the room. Arnold continues to rant.] Children. Children taught by people like you. 'Cause everybody knows that queers don't matter! Queers don't love! And those that do deserve what they get! [He stops, catches his breath, sits down] [Long pause while Arnold composes himself] . . . . Ma, I'm sorry I lost my temper. Please come out here. We can't talk like this.

MA: [In doorway] You don't want to talk, you want to fight.

ARNOLD: You wanna sit down?

MA: [Wandering over to the couch] I'm sitting. [Warning] And don't holler at me. People say things they don't mean when they holler and you've already said quite enough.

ARNOLD: I won't holler. You just hit a raw nerve. We won't discuss Alan. Only David.

MA: So discuss.

ARNOLD: Why don't you tell me what you already know, and we'll go on from there.

MA: Let me think. He's an orphan . . .

ARNOLD: He's not an orphan. He was a battered child. They took him away from his parents. This is his third foster home. The first brought him back. The second he ran away from. So . . .

MA: Arnold, darling, open your eyes. Don't you see how ridiculous this is? I've been here less than a day, already I've seen you let him miss school, hang out on the street, go out without dinner . . .

ARNOLD: This isn't Little Lord Fauntleroy we're talking about here. If this kid decided I was coming down too hard on him, he'd pack and take off and I'd never get him back again.

MA: So you let him run wild?

ARNOLD: No. But I don't beat him up either. I teach him. I advise him, I try to set an example for him . . .

MA: Some example. Arnold, look, you live the life you want. I don't say a word. This is what you want. But think about the boy. He told me he loves you. He sees you living like this . . . don't you think it's going to affect him?

ARNOLD: Ma, David is gay: the whole purpose of placing him here was for him to grow up with a positive attitude about his homosexuality.

MA: That's it. [Stands] I'm finished.

ARNOLD: You think this is easy for me? Look; my hands are shaking. I've been like this for days knowing you'd be coming and we'd have to talk about this.

MA: Because you knew I'd show you how wrong you are.

ARNOLD: I'm not wrong.

MA: No? Tell me something: How old was your friend Alan when you met him?

ARNOLD: Seventeen.

MA: Seventeen. Seventeen and you were doing God knows what together. Now tell me; how old is this "son" of yours?

ARNOLD: I have no intention of sleeping with him if that's what you're driving at.

MA: I had no intention of having a homosexual for a son. So, look where intentions get you. Arnold, do what you want. You want to live like this? I don't care anymore. You're not going to make me sick like you did your father.

ARNOLD: I made my father sick?

MA: No; he was thrilled to have a fairy for a son! You took a lifetime of dreams and threw them back in his face.

ARNOLD: What lifetime of dreams? He knew I was gay for fourteen years.

MA: What? You think you walk into a room, say, "Hi Dad, I'm queer," and that's that? You think that's what we brought you into the world for? Believe me, if I'd known I wouldn't have bothered. Arnold, you're my son, you're a good person, a sensitive person with a heart, like your father, and I try to love you for that and forget this. But you won't let me. You've got to throw me on the ground and rub my face in it. You haven't spoken a sentence since I got here without the word "Gay" in it.

ARNOLD: Because that's what I am. You want a part in my life? I am not going to edit out the things you don't like! There is nothing I need from anyone except love and respect. And anyone who can't give me those two things has no place in my life. [Breath] You are my mother, and I love you. I do. But if you can't respect me . . . Then you've got no business being here.

MA: You want me to leave? I'm leaving. You want me to fight? I'm too tired. You want me to change? I'm too old and I can't. I can't, I can't, I can't. So you do what you have to do, and I'll do what I have to do and I hope you're satisfied. [Arnold groans] You can't put all the blame on me. It's not fair. Your “friend” Alan . . . How was I supposed to know?

ARNOLD: Why? You would have understood?

MA: Maybe. Maybe not. You can't know for sure. But I flew up for the funeral and you never said a word.

ARNOLD: So you could've done what? Tell me he's better off dead?

MA: Or maybe I could've comforted you. Told you what to expect. You and your "widowing." [She turns to leave, stops, takes a breath. One last try.] You've got an unusual way of looking at things, Arnold Beckoff.

ARNOLD: Runs in the family. Ma, I miss him so much.

MA: Give yourself time, Arnold. It gets better. But, Arnold, it won't ever go away. You can work longer hours, adopt a son, fight with me . . . whatever, it'll still be there. It becomes part of you, like wearing a ring or a pair of glasses. You get used to it and it's good . . . because it makes sure you don't forget. You don't want to forget him, do you? [Arnold shakes his head] So, it's good. [Pause] I guess that's what I would have said . . . if I'd known.
```

---

## IC-0045: Zooman and the Sign

- Title: Zooman and the Sign
- Author (byline): Charles Fuller
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: June 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ZOOMAN, RACHEL, REUBEN, JACKSON, VOICE OVER, GRACE
- Teaser before the introduction: Yes
- Spoken words (computed): 1541
- Already set (do not supply): none

### Source block (context only)

```text
Author: Charles Fuller
ISBN: 978-0573618451
Publisher: Samuel French, Inc.
Date (Month/Year): June 2003
```

### Introduction (context only: never use it for content warnings)

```text
Two distinct but intersecting worlds: One is the place where 15-year-old Zooman prowls the streets, mugging old ladies and cutting people who get in his way. The other is where the members of the Tate family, hard-working, decent people with blue collar jobs, try to make a life for themselves in a neighborhood overwhelmed by violence and distrust.

When 12-year-old Jinny Tate is murdered the two worlds collide and the Bystander Syndrome, (that’s what it's called when a person witnesses a crime, emergency or an individual in need of help and does nothing) becomes shockingly real.

Zooman and the Sign by Charles Fuller
```

### Performance text (classify this)

```text
A young black man steps forward, looking at the audience contemptuously. He is wearing a mesh and plastic, green and white baseball cap tilted to the side. A red T-shirt, with the inscription "ME" on it, hangs outside a pair of slacks or dungarees designed with two large pockets, one on each side. He is wearing high top sneaks. There are several thin gold and silver chains around his neck.

ZOOMAN: (Pg 3) (Casually) I just killed somebody. Little girl, I think. Me and Stockholm turned the comer of this street? -- and there's Gustav from uptown, and this little b**** has to be sittin' on her front steps playin' jacks! But I had tol' Gustav if I eva saw [him] around the Avenue, I'd blow him away. (Shrugs) So I started shootin' and she jes' got hit by one of the strays, that's all. She ain't had no business bein' out there. That street is a war zone -- ain't nobody see her, we was runnin'! And in that neighborhood you supposed to stay indoors, anyway! (Pause) She was in the wrong place at the wrong time -- how am I supposed to feel guilty over somethin' like that?

RACHEL: (Pg 4) I keep seeing her, Reuben -- feeling her all over the room. And I want to reach out and straighten her hair, touch her dress. And I know she's gone- (Pg 7-8) (She is quiet for a moment) This morning, she got up -- took her forever to get her clothes on. She messed around with her food. I told her I was going to call you if she kept it up. But I made her go outside, Reuben -- I made her!

REUBEN: This is not your fault.

RACHEL: She just got on my nerves so bad - I told her three times to clean up that mess she left in her room -- three times! (Quietly) You shoulda been here.

REUBEN: I'm here now -- and I was here the weekend . . .

RACHEL: (Interrupting) Are you going to stay this time or leave -- or what? Because I really can't take it, Reuben! It's too much to ask me to do by myself right now -- I can't deal with this! (Saddened again). I just feel so damn empty! I keep expecting her to come stomping down the stairs—or hear her music playing! How do you get used to an empty room? (Pause) Reuben? You remember the time she put on all my makeup? You shoulda seen her that day -- lipstick from one end of her face to the other -- powder in her hair -- cologne all over – (Shakes her head) She was so much a girl! (beat) (Pg 9) She's the baby, Reuben -- how could they take the baby? (She begins to cry) (The doorbell rings – Reuben opens the door).

JACKSON: (Pg 13-14) Hello, I'm Donald Jackson -- I live down the street? My wife, she was in the back hangin' clothes when it happened. By the time she got to the front door, them boys was halfway up the block. She didn't see nothin'-and me, I was at work, -- but my wife said there was something y'all might want to know- Cop told her he went to every house on the block and not one person claim they saw anything.

REUBEN: What? There's forty-fifty families around here!

JACKSON: It seemed strange to my wife too, 'cause she said when she came outside, everybody in the block was on their porch. About half on your side, and most of them on my side.

RACHEL: (Pg 15) (Shouting) They were all out there! I saw Mrs. Smith standing by her front door. Dottie Henson was hanging out her window! They all saw it. They were all outside when those boys ran through here! They watched her die! (Breaks down crying) I saw them! I saw them! I saw them! ***** Scene*****

ZOOMAN: (Pg 16) When you got nothin’ to do, come to the Zoo! (Quieter) First couple hours are the worse. The big, blue fools are probably sweeping the neighborhood by now, picking up everybody in sight. (Sudden mood swing) I got up this mornin' and felt like killing somebody! So what? Gustav is just lucky it ain't him! (beat) I got picked up twenty-one times las' year! Every time somebody black did somethin' and the cops didn't have a name? They busted me! All young n*****s look alike! I was in Juvenile "D" eighteen months. (Pause) (Pg 17) Tomorrow's my little sista's' birthday! Not my sista here -- a half sista in Birmingham -- she'll be ten. She's down there with my fatha's people. ***** Scene*****

REUBEN: I'm tellin' you, Rachel, it was like they didn't know me! Mr. Davis, and Gibson down the street? They didn't even answer the door! I go down the street to Julius Williams' house, and he acts like he didn't know we had a daughter! Not one damn person on the block claims they saw anything! (Pg 18) What happens if the police catch the boys they think did it, and nobody comes forward to identify them? They go free? Me and Rachel been livin' here fifteen-sixteen years! Jinny was born on this block! And they all act like strangers -- what's wrong with them?

RACHEL: (Pg 22) I don't want to live here anymore! You can't walk the streets -- And nobody gives a damn! I even had to call the police myself -- leave my baby because I didn't hear a siren! They stood on their porches with their mouths open! What if it had been Grace's little girl, Denise? Or Mr. Davis' granddaughter Phyllis? (On the verge of tears) (Pg 24) Reuben, I think I'm just gonna explode and die in a minute! And keep exploding -- and dying, and dying -- over, and over, and over. *****Scene – 3 days later after Jinny’s funeral*****

REUBEN: (Pg 26) Losing Jinny was like waking up and discovering the sun had a hole in it. She had a way of smiling at you, made you feel somebody had given you a gift. I wanted to see her grown -- bring a boy around here for me to meet -- do something-be something! Twelve years old ain't nothin'! (Slight pause) So, I went downtown this morning, and had this sign made to hang over our porch. Get these folks off their asses. It sure can't hurt nobody. But maybe it'll make somebody come forward. (hangs the sign – he looks up)

VOICE OVER: THE KILLERS OF OUR DAUGHTER JINNY ARE FREE ON THE STREETS BECAUSE OUR NEIGHBORS WILL NOT IDENTIFY THEM! *****Scene – a day later*****

GRACE: (Pg 31-32) (Doorbell rings, outside) Rachel. It's me honey, Grace! (Rachel opens the door) How you feelin', girl? I just dropped by to pay my respects. I think I woulda went out of my mind if it hada been Denise-I don't know how you can stand it. They'd-a had to carry me to the hospital! They'd-a had to strap me down! (Pause, then business-like) I am really sorry it happened, Rachel. (Pg 33) I want to ask you one thing. Why did you let Reuben hang that sign? He's got people around here climbing the walls! Don't none of them appreciate it -- they planning to hold a block meeting about it. (Pause) And the truth is, it makes the whole street look bad. Thing like that lumps the good with the bad -- and every time you tum around black folks are saying something terrible about each other! "We can't get together -- our men ain't no good -- everywhere we live is a slum!" And Reuben's sign makes this look like the worse place in the world! That's y'alls private business!

RACHEL: Seems like a killing on the block would be everybody's business. . .

GRACE: The Tates ain't no better than nobody else! I didn't see the Tates get excited when those hoodlums raped Lou Jefferson's little girl -- or robbed my place! Why should anybody go out of their way for them? I didn't hang up no sign!

RACHEL: (Pg 35) Get the hell out of here, Grace - Get out! (Grace exits angrily; Reuben enters) (Pg 39-40) I’m sick of that sign! We're supposed to be in mourning -- We lost Jinny three days ago -- why are you doing this now?

REUBEN: Rachel, that sign hasn't hurt anybody unless they feel guilty.

RACHEL: It is making people hate us, Reuben! You're making this a sideshow!

REUBEN: The sideshow was the day they ran through here, shot up the street, killed our daughter, and nobody on this block did anything about it! (Pg 47) That sign doesn't come down until someone comes forward. (Pg 49-50) It’s the principle of the thing. (Phone rings, Reuben answers) Hello? 'Who? Sergeant. Harrison? (Listens, then quietly hangs up; he turns to Rachel) They caught one of 'em -- he's fifteen. (Disturbed) There were two of 'em. They picked up some kid named Stockholm and he told on the other one -- boy they call Zooman.

I never thought of them as that young. *****Scene*****

ZOOMAN: (Pg 40-41) It's no fun being on the run. But I happen to know, if a black kills a black, and they don't catch you right away, they liable to forget about it (Slight pause) I ain't really worried yet. But them signs? Ain't nobody ever pulled that before! Killings, rapes, drugs - goin' on every day and nobody says nothin'! (Pg 42) Who [does] he think he is? Sendin' people afta me, like I'm some animal! If he wants to blame somebody -- you don't leave no little girl sittin' on her steps by herself nowadays! He shoulda known better -- what kinda fatha is he? (Pause) (Pg 54) I'll be off your streets soon, don't worry -- I just got one more thing to do. (Zooman starts boldly toward the Tate house, hollering, a knife in his hand) Hey! This is Zooman out here! (He reaches up and begins to rip and tear at the sign) Don't nobody do this shit! You don't send people after me! You hear that? This is Zoo man you [messin’] with! Come on out! (Shots are fired through the window of the Tate residence. The shot hits Zooman and knocks him down) I'm Zooman. F*** you! (Zooman dies)

RACHEL: (Pg 56) Oh, Reuben -- oh my God, Reuben.

REUBEN: I know, baby. I know.

VOICE OVER: (as Reuben hangs another sign on his porch) HERE, LESTER TOHNSON WAS KILLED. HE WILL BE MISSED BY FAMILY AND FRIENDS. HE WAS KNOWN AS ZOOMAN
```

---

## IC-0046: Fighting Stance

- Title: Fighting Stance
- Author (byline): Frank Smith
- Work: Fighting Stance
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ROWAN
- Teaser before the introduction: No
- Spoken words (computed): 2868
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
A Dramatic Monologue

Written by Frank Smith SCENE I Karate Dojo.

(Polished wood floors. Two walls full of mirrors. The third wall: a window looking onto a quad.) ROWAN.

(ROWAN (22), perfect posture on the verge of seeming physically impossible, wears a karate gi, practicing the primary level Shotokan karate kata, Heian Shodan.)

ROWAN: (Counting to ten in Japanese as he goes through his punches and kicks, nailing each.) Ichi…ni…san…shi…go…roku…shichi…hachi…ku…juu. KI-YAH!!! (Noticing the audience, he bows gracefully, before wiping sweat off his brow.) ‘Sup. I’m Rowan. SEMPAI Rowan. That sounded formal. It just means I’ve been doing karate longer than you all. But, umm…I’m sorry to say that you missed the training today. Better absent than late, I guess? Katrine Sensei does NOT like it when people are late. As in…she threatens them with bodily harm. (Seeing the audience’s worry.) I’m kidding – she doesn’t actually do that. Harm. She just threatens it. See, karate is all about self-defense. Not offense. Fighting is the absolute last resort. We’re not about picking fights here. And Shotokan karate in particular has a bit of…reverence to it. Because you know the power you wield is dangerous. And that you only use it in very extreme circumstances.

(Rowan starts to pack up to leave…then smiles, looking at the audience.)

ROWAN: I feel bad that you came all this way, though. I could lead you through a training if you want. I’m not an instructor. But I am a purple belt! AKA an ADVANCED…intermediate student. So I could definitely show you a couple things. Would you like that? (He drops his bag.) Okay, great. Let’s do it. How did you find out about the training, by the way? Did you see us at the activity fair? That’s how I found out about karate last year. Before that, I used to do…well, nothing, quite honestly. I don’t know, though. I think it was something about, knowing I was going to turn 21 later that year – and also starting drinking for the first time – that made my Mom say: Rowan. You live in New York City. It’s dangerous out there. And you need to learn how to defend yourself. So, I figured: let’s see what the college activities fair has on offer. And that’s where I met the Shotokan karate club. More specifically: I met Tylan. I know…weird name, right? Sounds like Tylenol. His parents couldn’t decide between Tyler and Dylan, so…they chose both! That was sort of his thing, getting the best of both worlds. He had red hair, but he also had blue eyes. I’ve always loved blue eyes, and he had these crystal blue ones that were just…piercing. Those, he got from his Dad. The red hair, he got from his Mom. It’s not the most common look, red hair and blue eyes…but then again, Tylan isn’t the most common person.

(Rowan starts stretching. He gestures for the audience to do the same.)

ROWAN: You want to get nice and limber before we get into any real training. Trust me, you will be in pain tomorrow…but it’s a proud pain. That’s sort of what being friends with Tylan was like. Proud pain. I’m talking a lot about him, huh? Sorry! I’m a sharer. I first noticed Tylan from afar – those eyes, that hair. I walked right up to him at the activities fair. I asked him point-blank: are those contacts you’re wearing? They were that blue! They didn’t even look real. He says yes, calls me an idiot – which I find funny, for some reason – then asks me what I know about karate.

I say not much, other than what I’ve seen on Power Rangers. And he says, well then, I have a lot to teach you, kohai. That means younger student. Which is what you all are to me.

(Rowan stops stretching.)

ROWAN: Okay, nice and stretched out? Good. First thing I’ll teach is how we move in karate. Crescent stepping. It’s like this. (He demonstrates, squatting down and arcing his feet out as he moves.) I know it seems awkward, but you get used to it after a while. Just…practice, okay? (He observes the audience moving.) Yeah, it’s a start. When I first did it, I looked ridiculous. But Tylan helped out a lot. He’d stand next to me at every training, saying I was his personal kohai. He’d watch, whisper suggestions – which sometimes made Katrine Sensei mad – but it helped me get better faster than all the other students. Tylan was a green belt, which is a degree below what I am now. But from how confident he was, you would’ve sworn he was a 1st degree Black Belt. He was only a year older than me…but he seemed like he knew so much more. I actually turned 21 on a day where we had a karate training. And when it’s your Birthday in the club, you get to spar against all the other members. Everybody has one shot, so it’s up to you to defend yourself. Obviously, I was newer, and most people got in a good punch or kick. Tylan took it easy on me: he went for the face. But the face block – one of the first things I’ll show you all –

(Rowan demonstrates, arcing his arm up from below his waist to over his head. He gestures for someone in the audience to punch, before blocking it flawlessly.)

ROWAN: It’s a pretty effective block. So, since I have a September Birthday, I’m pretty much the only one of my friends who had turned 21 already. Except Tylan, who was a year older than me. And he said, “Come on, Kohai, I’m getting you drunk.” And what could I say? He was my sempai, my older student. Saying no to getting wasted with him would have been…highly disrespectful! Besides, my Mom had always taught me to be gracious to people who show you kindness. And he was definitely showing it to me. With beer, with a chicken salad, with another beer, with a shot, with another shot. And since I had literally never had a drop of alcohol before in my life, that was enough to get me pretty litty. Now, as some of you may have guessed from the way I talk about Tylan – I had a crush on him. I had no idea if he could tell or not. But see, I wasn’t exactly out to anyone yet. Not because I felt like they’d be MEAN to me…but I worried they wouldn’t be NICE. And that was enough to keep me closeted. As it is with a lot of young queer people. But Tylan, who treated me like a king? Wow. That was more than I ever could have hoped for. It felt like being kissed a thousand times, all over. And that is when he brought up kissing. He said that a 21st Birthday was a lot like New Year’s. And that I deserved to get a kiss. We walked around, talking to girls. No one seemed interested. Neither was I. Just when I was ready to give up, he asked me: have you ever been kissed by a guy before? I said no. He stared at me. For a long time. It was awkward. And…attractive. I asked: have YOU ever been kissed by a guy before? He said yes. Who was it, I asked? A friend, he answered. And…what was it like, I questioned, my heart beating into my throat at this point. He said pretty nice. I smiled, a really dopey, still pretty drunk smile, and said: I’ll have to take your word for it. And he said: you don’t have to take my word for it. He walked right up to me. Looked me straight in the eye. Moved his face toward mine. Hand on my cheek. A few fingers on my neck. And…that was my first gay kiss. But, you know when you’re gay, like I am: it was just…my first kiss. And it was a pretty great one. I think. Like I said, I was DRUNK, so…I’ll have to take my word for it.

(Rowan demonstrates a stomach block by holding up his wrist, then thrusting it down.)

ROWAN: And that’s how you defend a strike against your stomach. Don’t worry, we’ll move on to actual attacks soon. Like I said: defense is the priority. Perceiving the threat. Reacting only when you must. Speaking of reactions: I was a little surprised when all we did after the kiss was…walk home. Though I did get a sweet check-in text from Tylan of, “Tonight was so much fun. More soon, please. Of all of it.” I woke up the next morning, the most excited for karate training. I showed up a few minutes early, looked around…no Tylan. It’s now only a minute before we start – no Tylan. He showed up JUST before Katrine Sensei started us off. Good for him, because she would have threatened to kick his ass so hard. Then, you know, not actually done it. But that day, he wouldn’t stand next to me. He stood as far away as he could. And it was quite honestly one of my worst trainings ever. I kept wondering what I did, what I said, if I was just a drunk, gay mess, and I did something awful to him. After practice, he FLED. That night, I heard a knock at my door: it was Tylan. My roommates kind of gave me eyes, like, he doesn’t SEEM like he’s here to study. And Tylan noticed, so quickly ushered me into my room. Without my even having to ask, he said he was sorry for how he avoided me at karate training. He ran a hand through his perfect red hair. Blinked at me with those beautiful blue eyes. But…he wasn’t out yet. Neither am I, I said. Yeah, he said, but with you, people, like…they know. They don’t with me. Ouch, I said. Not that it should have been an ouch. But coming from him, it felt like it. He said he was glad he could tell right away with me…it’s how he knew it’d be okay to kiss me. I smiled. ‘Cause he was right. So, we kissed again. He said, “Just think of us like agents: secret, sexy agents.” I REALLY liked the sound of that. So, we kissed again. And again. And…

(Rowan raises his arm, and swings it around in front of his face.)

ROWAN: So this is a mid-range block. Can be used for the face, or the stomach, depending on – you know, where you block. Tylan and I, we went on with this “sexy, secret agents” game for about a month. I come to think of him as my boyfriend – though he wouldn’t call ME that – but his kisses…were perfect. I loved running my hand through his hair. Smelling him, especially after training. I was smitten. And sometimes at training, he’d say he had to use the bathroom – at the same time that I had to use the bathroom – and on our way back to training, we’d kiss out in the hallway. But as soon as someone would show up, we’d stop, and act like we never even saw each other. It didn’t totally bother me. It didn’t feel like what I’d want to do forever. But what we had was nice, I thought. I didn’t perceive the threat. One training, we snuck off for a bathroom trip, followed by a hallway kiss. I really did have to pee that time. Only, when we started to kiss…Katrine Sensei was there. She’d gotten suspicious of how we always ran off at the same time. Worried we were doing something we shouldn’t. I guess she was right. I tried to cover, saying I know what it looks like, but we were just hugging. Katrine Sensei could see exactly what was happening. She said it’s no big deal, whether it was hugging, or…she didn’t care. No one did. I’m so relieved, I just burst out: yeah, who cares if you’ve kissed a guy before, right? Katrine Sensei laughed. I had NEVER seen her laugh. Tylan scowled. I had NEVER seen him scowl. He said HE’D never kissed a guy. He turned on me and said: have YOU? Because if you have. It’s gross. I didn’t even know what to say to that. I just felt…well, gross. Thank God for Katrine Sensei, telling us both to get back inside, and take separate bathroom breaks from now on. Because if she hadn’t prevented us from talking further…I might have broken up with him right then and there. Of course, I didn’t, because why would I learn my lesson that early, right?

(Rowan checks in with the audience. Seeing they’re ready, he nods, and throws his first punch – it’s swift and powerful.)

ROWAN: And when it comes to attacking – we’re finally there, yay! – you’re not here to do some martial arts movie style beatdown. It’s about being swift, and deadly. One strong punch to the face or gut – your opponent is incapacitated, and you can escape. Escaping isn’t always that easy, though. I was absolutely furious with Tylan after how he acted in front of Katrine Sensei. I think I stomped all the way back to my dorm. In fact, I know I did, because a few random girls pointed it out to me. Giggling…but also asking me if I was okay. And I thought: why are these random strangers able to show me kindness? But my boyfriend, who won’t even call me that, can’t? I raced into my room. None of my roommates were home, fortunately, which was good. I couldn’t face them. I was way too embarrassed. Embarrassed I let myself be treated like that, embarrassed at how much they knew – or didn’t know. Heard a knock at the door. I didn’t answer. Phone buzzed. I didn’t answer. Phone rang. For five minutes straight. Finally, I answered the door, and it was…Katrine Sensei. This would be like if you were Catholic, and God stopped by your room, when you were expecting…well, your boyfriend. She said it’s none of her business, what’s going on between Tylan and me, but that she hoped, sincerely hoped, that I was getting out of it just as much as I was putting in. I thanked her, closed the door, and just… broke down sobbing. I wasn’t getting enough out of it. I knew I wasn’t. I knew that all along.

(Rowan focuses in before performing a powerful kick. He laughs, watching the audience try.)

ROWAN: The power is really supposed to come from your legs. Not your back. That’s the whole point of doing the crescent stepping. To teach you how to stay grounded. Draw your power from the Earth. From within. To support your back and spine. We all need a little help with our back-bones. So it was time for another training. Tylan once again waited until the very last minute to show. I walked over to him. In no uncertain terms, I laid out how wrong it was for him to act like I was a stranger. He said “You knew what we were: secret, sexy agents.” Nothing more, nothing less. As far as the world was concerned, he was straight. And both he and I needed to keep up that appearance. I looked him in the eye and said: either you’re straight, or I’m your boyfriend. You don’t get the best of both worlds. I started to walk away. He grabbed me by the arm. Hard. Don’t walk away from me, he said. Don’t you ever walk from me. I’m frozen. Stuck in the whirlpool of those beautiful blue eyes. That tousled, fiery red hair. Katrine Sensei had to walk up and physically pull us apart. Time to train, she said. Tylan went to the opposite end of the lineup. I walked up and stood right next to him. But said nothing. Yet. And wouldn’t you know it? That day just happened to be Tylan’s Birthday. Meaning we all got to take a shot at him. I was kind of reluctant. But Katrine Sensei said Tylan and I deserved the exact same treatment. (Rowan acts out all the following movements.) I rushed up to him. He had trained me well – I landed a hit. So did he. It was harder than it needed to be. I went for a kick. I missed on purpose, but he still blocked me pretty aggressively, almost throwing me down to the floor. Then, he went to punch me square in the face. And…I blocked it perfectly. He went for it again. I blocked every single time. I perceived the threat. Shocked, spitting mad, Tylan got in my face, and whispered: “How dare you do this to me. Your Sempai. Your…boyfriend.” I stepped away and said, loud enough for the whole room to hear: “You are nothing to me.” Katrine Sensei was ready to break things up, but she didn’t have to. Tylan stormed off, face dripping from sweat, or tears, or both – he never came back to train. Ended as a green belt, which I have now surpassed.

(Rowan performs the remainder of the first kata, Heian Shodan, that the audience’s arrival interrupted at the start.)

ROWAN: One last thing we have to talk about when it comes to Shotokan karate: kimei. It means spirit. It’s what separates a good day of training from a great day. If you’ve watched Power Rangers, like me, and remember all the AY-YAH! and KI-YAH! the Rangers would yell: that’s kimei. Spirit. The feeling that no matter what, you’ll be able to perceive a threat, and defend yourself accordingly. With the power from your own body, as well as that of your friends and allies. Which we now are, my kohai. Come on, give me a good yell. I’ll teach you Heian Shodan, the kata I just completed. But the thing that’s more important than any individual move is kimei. Do you have it? Can you show me some? (Off the audience’s response.) Then say it with me. Throw out a punch, a kick, or any kind of block, and kimei it up, kohai. One-two-three: KI-YAH!

THE END.
```

---

## IC-0047: I Have Recently Returned from Killing the Second Hitler

- Title: I Have Recently Returned from Killing the Second Hitler
- Author (byline): J. Gone
- Work: I Have Recently Returned from Killing the Second Hitler
- Publisher: Mushroom Cloud Press
- Publication date as stated: August 15, 2024
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1785
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
Author’s Notes Different schools and organizations have different rules about hateful language. This play can be performed under its alternative title, “I Have Recently Returned from Committing a Great & Horrible Deed,” if necessary. However, the language in the play around “The Second Hitler” should not be changed.

It is the author’s intent that this play can be performed by an actor of any gender. As such, when the main character refers to himself as resembling an “uncle,” this line can be changed to “aunt.” In addition, the genders of the spouses can be changed in the text of the story, if the performer desires. No further changes are permitted.

I Have Recently Returned from Killing the Second Hitler by J. Gone

People who now live, rejoice! The dark pool of possibility sitting in the shadow of your heart can remain hidden, for now. You do not need to extract the best or worst of yourself and perform great and terrible deeds merely to survive. Isn't that nice? To have a day where you will not be challenged to pick between a life of evil or a deed of martyrdom. Because. I have done a such deed on your behalf, and ask, briefly, for your undivided attention.

I have just returned from time-traveling into the past, where I killed a young American girl who was to become the Second Hitler.

The mission to kill the Second Hitler was not my idea. Its desperate architects only brought it to me as their plan neared completion. They did not choose me for any particular skill I possessed. Rather, I bore an uncanny resemblance to my target’s close uncle, as he appeared 30 years ago. That coincidence allowed me a better chance to get in close to her, where I could engineer her downfall.

It was an easy choice for me. All my friends and loved ones were dead or banished. The few souls I knew alive, if they were not being tortured for information, were broken or in hiding. A few of course were the torturers.

This was six months ago. A different six months ago.

When most of you were dead. When a few of you held the whip, the chain. Maybe one of you still fought. There were not many of us.

I had no choice but to go backwards and kill this six-year-old girl.

The death went off as planned, well-choreographed. I was not nervous about the outcome. Had I been discovered, I would have set off a small explosive as a back-up option. Knowing all that would happen if the Second Hitler lived, I had no problem with the possibility of sacrificing myself to stop her.

I did receive a small shock when I raised my hand to do the deed. I should not have been surprised at what I saw. It's logical that if I looked like the girl’s uncle, she would look like me. But it turns out, the second Hitler looked just like my daughter. The act would have been disorienting only for the reason of surreal resemblance, were it not for the additional time traveler’s consideration that killing this young girl would irrevocably change the future, perhaps wiping out the actions that led to my daughter’s conception and erasing her as well. Therefore, as my hand continued to move, I looked into the second Hitler’s eyes and also seemed to look in my daughter’s eyes for the last time.

I remained in the past long enough to watch the little girl die. We were alone. I had to be sure. At first, I regarded her coldly as the life ran out of her. A monster, larval. But. Was that life good or evil now? Was she still as innocent as my daughter? So, I held the second Hitler’s small hand as she left the world untouched by what she would become.

The device the architects created only brought me to the past for a certain, preset length of time, after which it returned me here. They had timed it perfectly. I heard commotion in the hall just before I felt the great heartache of time travel take my body and pull me forward through a billion new choices toward the new world. When I arrived here, the device dissolved.

I am pleased to report that the Second Hitler remains dead in our time. Her passing at age 8 is recorded as an accident in the official records and archived newspapers, and I found no follow-up articles regarding suspected foul play.

Thanks to this action, her reign of terror, under which we all lived - and many of you died - never came to be. I am reluctant to go into detail about how and what she did. History, as she proved, replicates itself so cleverly. All I will say is, no terror is impossible. Lay out all the worst things you can think of happening to you, or to your family, or to your country. Can you truly discount any of them taking place? Only by the rules of reasonable doubt and denial can we live without unending fear. Certainly, my mind will not find that peace again.

As for her political movement, that caused the deaths of tens of millions of you, it still exists, but in such a different form that I find it laughable. Some of the names of its members I recognize, obviously. As her adherents they would be butchers, but now they are only bureaucrats. She drew the evil out of them and put it on display for the world.

My partners, the women who invented the time-travel device, both live different lives, having never been called upon by terrible circumstances to develop their technology. They did not share the details of the device with me, so I would be of no help to someone who attempted to recreate it - or, perhaps more accurately, attempted to create it now for the first time. I have honored their request not to try.

I went to one of the inventor’s talks, on a matter related to entropy and neutron fields. Though she did not know it, she was explaining a part of the technology that had saved the world. Two of the greatest heroes stood in the room, she and I, but she didn’t know that. I dare not tell her.

I didn’t feel like a hero at all. After you’ve done something, good or bad, that cause and effect exist in the past, forever chasing each other in a loop, cat and mouse. The scientist’s work made that connection between the entropy and fields: Cause and effect are manipulated, until you can climb them like ladders back to what had happened long ago. Going back in time through all that happening feels like being squeezed through a tiny cave, decisions crushing you on every side.

I did speak to the scientist after her talk when she came off the stage. I said, doctor, I had a different family in a different universe. She looked at me with pity, though there was the crimson sparkle of wonder. I suppose she knew what her work could mean, even in this timeline. Tell me more, she said, but I told her I promised that I would not. She smiled and snapped back into a polite handshake. She’d prepared for this moment, in a daydream here or there.

And I bet many of you have daydreamed of killing someone evil to save the world. As far as you know, that’s all I’m doing. Describing a rather vivid daydream. As far as I know, none of this happened. If you have only your memory, and no other record of something important, then you must have tremendous trust in yourself. Faith that you believe in what you did.

Memory is faith, too. That what you did was real, was your choice. Memory is faith that, right or wrong, you would do it again.

Now that I’ve returned from killing the Second Hitler, my life, too, is changed. I find myself married to a different woman, with a new daughter. They seem like wonderful people, and I am looking forward to getting to know them. Fortunately, they have been very supportive of me and my new circumstances. They insist on it, because, they say, we have been a loving family for many years.

Since I returned from the past, I have often been tempted to contact my previous wife, but I would not know how to introduce myself. I miss her, of course. It would be hard for me, to see her, because the children we had together never existed. I bear that terrible fact for the sake of the world. The hardest part of carrying out my mission was knowing I could be erasing them. Up until the moment I returned, I held out hope that even in this new future, my wife and I would have found our way to each other, through some other story, and that my children would still greet me. Time doesn’t work that way, though. Most things, you only get one chance.

For my children, it was at least a better fate than being killed in the reign of terror.

There is one friend, who died early in the early troubles, who I was so happy to find alive again. He had no idea why I was crying so much when I saw him.

Such happy reunions are happening all over. Perhaps between you and your family and friends. Though you don't know it. If you see someone you love when you leave this room, be sure to hug them as though they died a horrible death in the gulags of an alternate world. That’s a good feeling we can always have, the escape from the embrace of a parallel universe. That our worst fears are only that.

I know for a fact that evil repeats itself. No one ever stops it completely. I tell my story only to give hope to those who face it the next time it returns. In the meantime, enjoy what you have been given. Who knows, you might be the other inventor responsible for the gift. You may have to make a choice, like I did.

I will not be answering further questions about the alternate timeline, for your sake and mine. I am taking some time off, to get to know my new family, and all that is different about our new world.

And perhaps, one day, I will go back to that lake, deep in the woods, where I used to spend the summers with my lost wife and our two dead children.
```

---

## IC-0048: It’s A Girl Problem

- Title: It’s A Girl Problem
- Author (byline): Josephine Kelly
- Work: It’s A Girl Problem
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: RUSSELL
- Teaser before the introduction: No
- Spoken words (computed): 1431
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
RUSSELL: (a normal teenage boy)

Snap out of it!

Look you just can’t make me. It is my power – my life.

Knock, Knock. Who's there? Nana. Nana who? Nana your business.

It’s a joke my sister told me at dinner.

To give you an accurate account of my problems would mean I have to understand it, acknowledge it, accept it.

Which I don’t -...have a problem.

I am a Lacrosse Player. I am very active, and I don’t need this right now. I train for speed - my father always says “remember you have to have explosive speed for both defense and offense maneuvers. Focus Russell Focus. Footwork behind the net.” Our mascot is a Tiger - the New Haven Tigers. (chants) NHHS NHHS...I don’t watch foot work videos any more – not here.

Here, (signals the place he is in) they watch other training videos...

One video says it’s (the reason he has been placed) like spotting a tiger in the jungle. Tigers are very stealth and difficult to see and when you do – it’s too late... Mauled. When I think of “mauled by a tiger” I think about surviving – but I don’t think you do. Survive. I don’t think I am the Siegfried and Roy of eating disorders. Look them up on the internet.

Knock. Knock. Who's there? Tank. Tank who? You're welcome.

Look, I just want what every other high school boy wants - girls - and there is nothing wrong with wanting to look good. I’m trying for a six pack – right here (pats stomach) just buff up. There is nothing wrong with that.

I have no idea what or why they are saying what they do, and I have thought about this hard. God, I hate eating with the family. It’s like living under a microscope. I just want to tell my parents to shut up!

I am not sitting around watching TV. I’m active - busy. I run after dinner – I get my homework done. They (the doctors) say that it could be based on obsessive and compulsive school work. Hey, you try taking my schedule – AP Bio and Literature - Straight A’s! And I am good at Lacrosse. So, I don’t know what my dad’s problem is.

College is just around the corner and I must be ready. I want to play Lacrosse in college – I think I’m good enough.

So, I blacked out... I just haven’t been feeling well. It is not a big deal. They all are caught up - like those pictures that you look at and there is a hidden picture behind it? Only I wish they would stop staring my way. I am not out of focus.

It’s a forced eating plan. No way. What right do they have to take that control away from me? They call me a perfectionist, but I say my brain is firing and my body is in sync and my power is beautiful. Why can’t they see that? I am winning at it. There are good fats and bad fats – hidden sugars – I know about these things – this isn’t a spiral down, its knowledge. It’s healthy living. I weighed myself last night and again this morning, so I know what I’m doing. I know the calories and what I’m eating. I keep constant track of them. I don’t need a forced eating plan!

So, I slam the door and just want to be left alone. I don’t have a problem. I don’t have a problem. I... start to cut myself.

I have to be Superman on the outside, but on the inside I feel like an empty shell. But this - I can control – this takes me out of my shell - the pain . . .

Snap out of it.

But I can’t - So I cut myself. I don’t know - cutting creates something inside me that is here and now and I don’t have to think about my Dad and how disappointed he is in me... State Championship son! . . . And he hates me.

Snap out of it! It’s a girl’s problem.

He yells that just before I slam the door to my bedroom. (he cuts himself)

So here I sit in the New Haven adolescent psychiatric Ward for eating disorders.

Who am I? This can’t be who I am... In my reading, I come across this story.

There was this boy named William Brooksbank. He was an athlete – like me – only he’s a swimmer. He won a state championship at age 10. In this article, it had early pictures of his with these chubby cheeks, but as he aged you can see his face just get gaunter and gaunter. His skin just stretched tighter and tighter across the angle of his skull. He was this living skeleton. And his parents paid a fortune in medical bills trying to get him help. But at age 22 he just lied down and died of cardiac arrest. . . At the time of his death he weighed 55 pounds. 55 pounds...His dad said, he watched him commit suicide for 11 years.

I am not William Brooksbank... it won’t be 11 years.

It would be easy to cut too deep... Let’s not go there – Dare we make plans.

Instead let’s talk about the Food Rules – yes - rules to literally live by. It is in the manual given to us when my parents dropped me off here.

1. Arrive on time – be in the dining room when meal trays arrive. There is this fifteen-minute window of medication time – where the cart would just come rolling in (makes the wheel sounds of the cart) and you could hear the sound of anxiety in every deep breath.

All the seating here is random and each day we must look for our tray. Random - unless they know you are tricky or new and then you would get a seat near the nurse.

2. Time starts – once everyone is seated the nurse would write the time on this white board – we would get a start time and the time we would have to be finished by. We had 35 minutes for each meal and 15 minutes for each snack. If you did not get your meal finished, then it is marked as incomplete.

3. Feet on the floor at all times – our hands visible on the table at all times. You get 1 napkin because you might try to hide food in one.

4. No hats, caps are to be worn – no clothes with pockets or book bags - really it said knap sacks but who says that? -because once again you can hide food.

5. We would leave our trays on the table with the napkin on it – if your napkin wasn’t there you would get checked.

6. No food talk – ever – somehow those nurses could hear you say, “I like oranges.” And their heads would pop in and you would hear No Food Talk!

7. No cutting of food into smaller bits. Like you can’t cut a banana and put it on your toast. Some people have triggers about mixing food.

8. Eat your food in the correct order. Entree before dessert. Salad before or with entree. The exception is breakfast when fruit is not considered a dessert.

9. No unprescribed foods. Like the vending machine or coffee shop food.

10. No drinks can be brought in by family members.

The time I hate is post meal hour. We all have to sit in this room after every meal. If you had to go to the bathroom during the meal – Too bad – if you went during this time so did a nurse.

Then its therapy.

I mean they keep saying we wouldn’t be there if we didn’t need it. We wouldn’t have been accepted into the program if we didn’t need it. But that’s crap. My dad put me here.

They say remember your goals – well, I don’t have any goals, that my dad didn’t give to me.

I am this shell. His shell. My dad stands on the sidelines of my life yelling for me to do better. Be better. (building in anger) Nothing I do is good enough or right enough or ...man enough...

My dad is afraid I’m a fag. Gay. Homosexual. This is a girl’s disease. And I’m weak for needing help. I am a failure.

I wish my dad would just listen to me – just be able to hold the space. To be the man that could love me - for me. I don’t have a problem. My dad does.

Anorexia nervosa is about shame.

Knock. Knock. Who's there? Police. Police who? Police stop telling these awful knock knock jokes!

(He makes one final cut to his wrist. Looks at his wrist and then turns it toward the audience and looks at directly at them.)

My parents went to see Siegfried and Roy at Las Vegas – I mean that was before the tiger got him. Look up tiger mauling on the internet. Once they get you, it’s deadly.
```

---

## IC-0049: My All-Time Favorites

- Title: My All-Time Favorites
- Author (byline): Frank Smith
- Work: My All-Time Favorites
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JANET, JANE
- Teaser before the introduction: No
- Spoken words (computed): 3274
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
A Dramatic Monologue

Written by Frank Smith SCENE I Mrs. Phelan’s House.

(Potted plants in every corner. Well-lit thanks to all the windows. Photos of a big, nice guy, ED.) JANET PHELAN.

(JANET PHELAN (75), born to be an educator, with a bright, soothing wardrobe, smiles as she answers the door.)

JANET: Hello! Yes, hello there. Umm…you’ll have to forgive me. When you called on the phone, I thought for sure I’d recognize you. Yet I don’t! It’s actually an uncommon skill, you know. Being able to recognize students you haven’t seen for 20 years. But when you’ve worked with elementary schoolers as long as I have, you get a good sense for how their faces will look as they grow. I guess that’s partly because I get so many visits, years later, from nice students like you. No, no, don’t tell me who you are. I’d like to figure it out. Keep it our little guessing game. It shouldn’t take me that long. I’m very good at this. Well, all right, then, come on in! Come inside already. It’s winter in Montpelier. No need to catch frostbite for the sake of being polite.

(Janet ushers her guest, who will remain unseen, indoors. She gestures for him to have a seat, before serving him a plate of cookies. She then puts a teapot on the stove.)

JANET: I’ll just get the tea. Yes, those are the same snickerdoodle cookies I used to make for all of you! Oh, aren’t you sweet. Well, it’s not exactly the same recipe…I don’t make them with quite as much sugar when I’m just making them for myself, and…friends. Do you mind if I call you a friend? The way I see it, once you graduate, I’m no longer your teacher. I’m officially your friend. Uh-huh. That’s the law. And so along those lines: please, please, please stop calling me Mrs. Phelan. It’s Janet now. So! You said you graduated from 4th grade in 2000? Oh, I remember that class very well. And not just because we were all so worried about Y2K, which ended up being NBD. I just learned that means No Big Deal. Oh, is it that old? Oh my. I tend to be a little behind the times. 10-year-olds aren’t necessarily the movers and shakers when it comes to pop culture. Though I do know more about Tik Tok than you might think. There’s this one young lady, Morgan Bullock, who Irish step dances. She is talented! She faced some discrimination for being Black, but she overcame the odds. That was true of a number of people in the Class of 2000. Some truly excellent students who struggled with quite a bit of adversity. Honestly, and I’d say this even if you weren’t here, several of my all-time favorite students were from that class of yours. Oh, sure, there were the trouble-makers. There always are. I can tell from looking at your eyes that you weren’t one of them, though. The trouble-makers, you do try to help. Some, you can. Some, you can’t. The high-achievers, they rarely need help. Sometimes they do, though. And when you can’t help them…well, I have to be honest with you. I find it crushing.

(Janet takes the teapot off the stove and pours them both a cup of tea.)

JANET: So, class of 2000. Let’s see, who were some of the standouts. Oh! I can tell you one right away. James Garner. Same name as the actor. That always tickled me. He was such a little heartbreaker, even back then. The girls in class would come and tell me how they took Cotillion classes with sweet James. You remember. The manners, and the dances. Those girls would race, actually race, to see who would get to dance with him each song. Wonder what happened to him.

(Janet nearly scalds herself while laughing at what her guest says.)

JANET: You’re kidding me! Three divorces? I guess he really couldn’t make up his mind about those girls. You’re not James, are you? Oh, phew. I’d feel much worse about what I just said if you were. No, I know it wasn’t that bad. I only might have swapped out a few words here and there, were you he. Let’s see, who else did I love. Oh, I know! Little Alison Baker. Just the tiniest little thing! But so much energy. So much! Always making speeches to the rest of the class. And resolving disputes for the other students. A real politician in the making. And you don’t need to tell me what became of her. I already know! I just cast my ballot to re-elect her as our mayor. She has done a tremendous job taking care of dangerous intersections all over town. That’s an important issue for me, locally. Children can so easily get hurt at those things. Oh my. One did, a few years before you. Clayton O’Malley. Poor dear. Such a sweetheart. Ran into traffic, and…oh. I can’t even bear to talk about it. He was such a talented flute player. One of the only students I ever met who could make the recorder sound beautiful. Simply an incredible child. Oh! Another one I adored: Thanh Pham. A trans girl. Now she knew her geography. I don’t think I ever saw her get one wrong. Not even when she won the State Competition! A real superstar. You don’t know what she’s up to, though? Oh, that’s too bad. But I’m sure she’s well.

(Janet chews on a cookie. She then notices her guest’s plate.)

JANET: I’m sorry, did you want a few more? It’s perfectly all right. I baked several dozen. It’s more than I need for my class on Monday. Take as many as you want. All right, then! I suppose everyone is allowed to watch their figures these days. (Gesturing to a picture.) My Ed was never big on that, as you can probably tell. He loved to eat! And to watch others eat. Now I’m quite the baker, but Ed was the real chef in the house. There wasn’t a single cuisine he couldn’t replicate perfectly. Truly a remarkable man. Miss him every day, but…he’s teaching middle schoolers in Heaven, now. I’m sure of it. Oh, that’s not to say…well, of course, middle schoolers do pass away, but…rarely. Much more often, they come to visit, like you are. It brings the greatest joy to us educators. We always hope we did a great job with you. But once you leave…we don’t know.

(Janet slides away her plate.)

JANET: Oh, look! Now you’ve got me counting carbs. You are such a terrible influence. Or perhaps a wonderful one. My, my. The Class of 2000. There was, umm, another student I lost track of. Well, of course, there are several. Soccer star Johnny Chao. Heard he got injured in high school, but kept playing anyway. Couldn’t get him to take class seriously, but who needs to, when you’ve got that much skill, I suppose. Eric Lopez. I hope he still sings. What an angelic voice. And, umm…I don’t suppose you ever heard from little Nate Abbott once he moved? I expect not. It’s all right. That happens every now and then. Students move away. But in his case, well…I have to tell you, I get worried sometimes. I know that might sound silly. Plenty of students never get in touch again. The majority don’t, in fact. Even though e-mail has made it easier than ever! But, umm, Nate. Well. It’s one of the few times I can remember that I wasn’t entirely sure I handled the situation right. Because even 20 years ago – I already had 30 years of experience. So, I was fairly certain my decisions were usually the correct ones. That, and I had been hearing that 50 was the new 30, so I figured I was in the prime of my life! Little Nate Abbott. Brilliant painter. And mathematician. He had it all. And you so rarely see that. So rarely.

(Janet takes the plates, and puts them in the sink.)

JANET: No, no, please, I’ll get them later. You are my guest. Sit, please. Sit. I know I’m about to. (She takes a deep inhale, enjoying the comfort of the seat.) Can you believe I’ve had this recliner since you all were in my class? It’s true. I seem to remember you were someone who was always on time. Nate, though. He was always running 5 minutes late, at least. One of his few noticeable flaws. Such an adorable little face. Rosy cheeks. Chubby ones. That’s why when he came in with one cheek looking rosier than usual – scratched and bloody, actually – I took notice. I immediately took him aside while the other students practiced telling time on the clocks I handed out. I remember, because Susie Lefkowicz kept insisting there was no difference between 3:30 and 9:30 while I was trying, really trying, to get Nate to open up. I pride myself on not losing my temper, but that girl! How could she have known, though. How could any of us have known. What I was trying to do. What I was worried about. I finally convinced Susie to leave us alone by offering her a lime green Jolly Rancher. Her favorite flavor. Mine too, actually. And then I asked Nate: what happened to your cheek, sweetheart? At first, he simply smiled back. Said that was the same color his cheeks always were. It sounded very…rehearsed. I asked him again if anything was the matter. Said he was allowed to say anything he wanted to me, and there would be no punishment. He then told me that he was painting right before school this morning. That explained the marks, AND why he was late. I gently touched his cheek, and…it wasn’t paint. That was when I saw it. His lip quiver. His eye twitch. But as soon as it started, it stopped. He said he must have forgotten: his cat scratched him. And then he walked over to explain to Susie why 9:30 was a different time of day. Like the selfless little gentleman he was.

(Janet returns to the sink a moment.)

JANET: Maybe I should wash these now. Before the crumbs stick to the plates. You know how it is. Cinnamon, sugar. They’ll be stuck like glue. No, but you’re a guest. Those can wait. I’m so sorry. (She returns to her seat.) Well, naturally, Nate’s explanations didn’t exactly set me at ease. Now, only his mother, Lilah, had ever come to parent teacher conferences before. She said that her husband – goodness, I don’t think I can even remember his name – was always busy working late at the firm. Family law. Ironic. So I gave Lilah a call, said I’d like to discuss a special gifted program for Nate. Would she mind coming in? Yes, I know that was the tiniest bit deceptive. But when it comes to matters like…these…sometimes bringing people in under optimistic auspices is the way to go. So Lilah came to visit, wearing a beret. Like a real Parisian. I’m not making a joke – she painted in Paris before settling down in Vermont. I guess that’s where Nate got his talent from. It was in his DNA. So were other things. I told Lilah that while I did think Nate belonged in a gifted program…there was another reason she was there. The mark I saw on his cheek. And she did that same lip quiver, that same eye twitch that I saw Nate do. She asked me what Nate said. I didn’t take that bait. I’m a real Jessica Fletcher when it comes to protecting my children. I said that I was simply interested in what had happened. She said that she was sorry, but she couldn’t actually remember anything unusual happening the night before. She closed her eyes, said she was thinking…though to me, it looked more like praying. When she opened her eyes: the tears were gone. Her lips settled. And her words were resolute: she couldn’t recall anything odd happening to Nate. But she was so grateful that I was paying close enough attention to him to question whether something might be wrong. With more teachers like me in the public school system, the world would be a better place. But it wasn’t a compliment. It was a cop-out.

(Janet fetches the tea pot and pours more tea for her guest.)

JANET: I don’t think I’ll be having any more tea, myself. I’m feeling a little bit jumpy all of a sudden. Caffeine can do that to you! You enjoy, though. Let’s see, where was I. Yes, of course. After the meeting. Well, Nate came to school, late as usual. Much later. About an hour later. And when he did arrive, he was wearing sunglasses. I’m sure I don’t have to tell you this, but no one wears sunglasses in Montpelier in November. I asked Nate to take them off. He wouldn’t. I then TOLD him to take them off. I do so detest being firm, but I had to see whether he was hiding something. He refused. What I did see, though, were tears streaming from under his sunglasses. That sweet, talented, ten-year-old boy. He begged me, please, just let me do my times tables. I’ll be good, I swear I will. I won’t make any noise. Just don’t make me take off my sunglasses, Mrs. Phelan. (Takes a moment to inhale.) I let him keep them on while he got settled, and started his worksheet. Once I could tell he was in a good rhythm – smiling, joking with Susie – I did ask if he wouldn’t mind taking them off. I thought I had found my moment, but right away, the tears returned. And in much greater quantity. I asked him to step into the hall with me. He said no. Asked why he was being punished. I assured him he wasn’t, he really wasn’t. At this point, the entire class had ground to a halt, to watch the two of us interacting. And finally, right as I was about to, I swear to you, get on my knees and plead with him to take off his sunglasses – little Susie Lefkowicz ripped them off his face. Just like that. One swift grab, and they’re on the floor. And there was Nate: sobbing tears from those big, beautiful, horribly bruised, ten-year-old eyes.

(Janet gets up, then sits back down again.)

JANET: I’m not sure why I even got up right then, I just…I can’t seem to sit still. Well, I’m sure you know, as much as I wished to respect the privacy of Nate, and his mother Lilah – I had to act. Morally, ethically, legally. I was bound to report what I’d seen. So, I set a meeting with the Principal. Which of course involved the police. And both of Nate’s parents were required to attend. This was the first – and only – time where I met Mr. Abbott. And I will never forget what I saw. No tearing eyes. No quivering lip. Just a dreadful, horrible stare. The kind of eyes you see in your worst nightmares, where the Devil shows up. He had those. Devil eyes. No matter what anyone said, that was the only face Mr. Abbott wore the entire meeting. But he didn’t speak. His wife Lilah behaved completely differently from when I’d seen her last. She said, Mrs. Phelan, this is an outrage. How dare we accuse her and her husband of such a thing. Nate was an artist like her, he had an active imagination, and there was no reason to think that it was anything other than…and I SCREAMED. I screamed like I have never screamed in my life. I screamed, “You are hurting this child. One, or both of you, is hurting this child. He is young. He is beautiful. He is innocent. What is the matter with you!? I hope that only one of you is hurting him, for his sake. And I hope whoever is letting him get hurt thinks long and hard about the kind of person that allows that to happen in their home, to their child.” I turned blood-red. I don’t know what color Lilah was – she hid her face. And HE wore that Devil’s stare. The police asked me to leave. I wouldn’t. So, the Principal gently escorted me into the hall. Thanked me profusely, but said they could handle things now. I TRUSTED that what went on behind that door was right.

(Janet rocks herself in her chair, losing her composure.)

JANET: I’m not a mother. You know that. At least not in the traditional sense. But my students.

You, Clayton, Nate. All of them. They are…what they mean to me is…I just can’t describe it properly. I try. But I can’t. Little Nate Abbott didn’t come back to school. Ever again. There are some weeks where I wake up, hoping to see his name show up in my inbox. Praying that it will. I don’t think about any other student that way. But what more could I have done for him? Truly. I’m asking. I couldn’t have had a softer touch. The abuse would have continued. I couldn’t have been firmer. Because then, he may have disappeared sooner. Why can’t they all call? Students need to know how much I care. How much I want them all to be okay. Why couldn’t Nate call? Could Nate be…like Clayton…I can’t bear to think of it. How could I do this? No. How could THEY? It’s all so wrong. I’m sorry, Nate. I’m oh so sorry. You’ll never know how sorry I am.

(Janet takes her guest’s teacup and puts it in the sink. She returns to her seat, breathing heavily.)

JANET: I didn’t even ask if you were done. How thoughtless of me. Oh, you were. Oh, good. That makes me happy to hear. I don’t suppose – I know there’s no reason to think that you would, but – is there any chance you’ve ever heard from Nate, Richie? Yes, I figured it out a few minutes ago. Richie Loze. The boy who never met a chessboard he couldn’t conquer. With long, flowing hair his parents refused to cut, an attitude as liberal as those lovable hippie parents who raised him. I’ll tell you how I could tell: you still have those adorable red cheeks… (Realizing.) Oh my goodness. No, you’re not Richie. You couldn’t be. Richie had that mark over his eye, from when he fell in the gravel, that day after playing Off the Wall with the fifth graders. No. Is there a chance…are you… (The guest finally reveals his identity: Janet sobs joyous tears.) You are. My goodness, you are. Oh, of course. Little Nate Abbott. But you’re not so little anymore. And those cheeks certainly aren’t chubby. Oh. You go by Nathaniel now. Is that right. Goodness. And here I was, prattling on…well. That’s in the past. Tell me. Please, tell me, my friend. Tell me everything. Really! I see. So, you’re telling me that, because of what I said, in that meeting, your mother had the courage to pack up and leave. To escape your father. You had to change your name and address, so he wouldn’t find you. And now, your father’s passed. Is it terrible if I say good riddance? Oh! I’m so glad you said it first. And now you’re okay. You’re all okay. Is that right! You and your mother? An exhibition together? Of course, I’d love to see it. Well, yes, I certainly would love to meet your family. What a pure joy that would be. Uh-huh. A little boy of your own. Oh, that’s adorable. Little Nate Abbott II. And a girl…really. Come on, you’re pulling my leg, now. Really? Janet? Little Janet Abbott? Why? I was only…well. That is very flattering indeed. Thank you, my boy. Thank you. Can I…come on. You don’t even need to ask.

(Janet gets up and gives Nate a big, emotional hug.)

JANE: Oh, of course. I’ve kept you so long. Let me pack you up a few extra cookies. Please, Nate…I mean, Nathaniel. I insist. You can give them to your boy. And your wife. Sonia, was it? As long as she’s not watching her figure like I now am. Thanks to you!

(Janet packs up a container of cookies and hands it to him.)

JANET: All right. You be on your way now. Please tell everyone I say hello. Sonia. Nate Jr. Lilah. Janet. Oh, and umm…Nathaniel? I very much do mean it when I say: come back anytime.

THE END.
```

---

## IC-0050: A New World

- Title: A New World
- Author (byline): Gabriella Diaz
- Work: A New World
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1299
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
When I paid for my mother to come to this country, it was the happiest day of my life. My mother, she was not happy. She was leaving the only thing she’d ever known, her beautiful homeland, her friends and, to her, even her memories. She was not happy, but she was proud. Proud that we were doing it, bettering ourselves. And to my mother, being proud of your life was more important than being happy while you live it.

Opportunity knocked in the U.S. I could hear it all the way across the ocean. Knock knock knock knock knock. My husband would find a job, our children would go to school, and college. Each of these thoughts knocked on my brain, drove me to find a way.

And the doctors here, in the U.S. they would help my mom. With her arthritis. Her constant cough. Her bladder infections. Such great doctors in America, and they would help my mother, help her be comfortable, the way she deserved. Well then, as soon as we got here, we took her to a couple doctors. Generalists and specialists. She charmed them, both the one who spoke Spanish and laughed at her jokes, and the one who spoke English and admired her strength. She would curse the Spanish doctor when they examined her aching joints, and then say, "The devil is in my blood, so I have to let him out by cursing because I am too old to dance!"

The third doctor we took her to, was to talk about some of her memory problems. She had been having trouble remembering things, like my daughter’s name. Back home, no one worries about this. It’s normal. Here, though, the doctor was concerned, he ran tests.

A month after my mother arrived in this country, we were told she had Alzheimer’s. That meant a lot of things. But to me, it meant only one thing: the life I had finally made for her, she would have almost no time to enjoy it.

It was ok for two years. We saved money fast, my husband, my brother and I, and bought a house and started renting rooms to tenants. My mother had her own little apartment. None of the tenants spoke Spanish, but they liked her, they would smile and try to chat while she swept the front porch or sat looking at the yard and road. Sometimes, she seemed a little confused, or lost, but no worse than any of us if we’re tired. One couple had a baby while they stayed with us, and my grandmother cooed over it like it was her own grandchild. Whenever I watched it, I would smile, but I would also here another thought knocking on my brain, knock knock knock knock knock, eager to come in, something I did not want to think quite yet.

I had another child, Marco. Lola and Marco. My grandmother loved Marco, although sometimes she would call him Jorge, my brother's name. She would ask him if he was going to work in the city for the sugar companies. She meant back home. That wasn't so bad, because you could laugh about it. But what was bad were those times you would show her the baby, and she wouldn't understand at all. Her eyes went blank, like a cloudy sky at night, no stars, no twinkle of recognition.

I had gotten us all over here, so I could figure this out, right? I had a whole plan, here is how we could teach her to remember the kid’s names, or find them quickly. I go in one morning to start, and I say hello, and she looks at me and says, “who are you?” And then every day, every hour, she would forget something new. My husband, her son, that we had moved to the U.S., that she was not a young woman. A week later I found her at the front door, with her bags packed. She was looking at the road, hopefully. “Where are you going, mama?”

She said, “I’m waiting for Luis.”

“Luis?”

“Yes, from the vocational school. We are going on a date.”

Luis, her high school sweetheart. She was waiting for him to come and take her out. She had forgotten my father, too. That she was ever married. “Marriage? I think maybe, if Luis likes me enough and my mother likes him...” That was her response when I asked about dad.

I would still let her outside to sweep the front walk. She insisted. And then people started showing up at my front door. My new friend Nancy, from two blocks away. She found my mother wandering down the sidewalk. The father of two teenagers next door, who came to complain that my mother had been screaming at his children in Spanish for fifteen minutes about how scandalously they were dressed. And then, two construction workers. They had come back to their van for lunch to find my mother inside, with a bag, asking them when they were leaving for the town next door - next door to where she grew up. It seemed if Luis was not going to come for her, she would go to him.

We went through three nurses, each of whom my mother cast off like junkyard dogs. She spat on one, and stole another's phone, calling random numbers and asking if they knew their friend was a prostitute who poisoned old ladies. All of them quit within a month.

When I finally locked her in her room, the tenants complained. She would knock at her door, from thie inside, day and night, getting louder when they walked by. Very fast and insistent, Knock, knock, knock, knock, knock, knock. I even tried... tying her down at night, but then she started yelling... I had to let her knock. My kids were scared, too. Even if you knew it was only her, you could not shake the feeling that there was a ghost behind that door.

She is suffering so much. She can’t take care of herself. She doesn’t understand that, though, so she tries, and she just suffers more. And she doesn’t know I want to take care of her. Yesterday, I brought her lunch, she asked why I was poisoning her. Did I want her money, or her jewelry? She doesn’t have either, anymore. Why do we live past a certain point, when life has nothing left for us? A slow burn of those energies that once fueled everything, now they just need to be used up.

I was thinking about that when I came across my son in the back yard. He had a grasshopper trapped under a glass. “Let him out, or he’ll suffocate!” I almost fell over when I said it. It was like opening the door, between the thinking part of your mind, and the feeling part, in the back, that usually stays closed, doing what it wants. And it had been up to something. It had thought the most forbidden thought.

My mother, so helpless, just a tiny grasshopper waiting to be eaten. Waiting to suffocate under the weight of the world. Knocking on that glass, knock knock knock knock.

Sometimes, you have to help nature along. With compassion.

Something is knocking on the other side of her door. Knock, knock, knock, knock. Is it still her? I haven’t checked in a while. I don’t remember who she was. All I see is a little grasshopper.

There’s so much left in this world for me. My children will go to college and succeed in their new country. Opportunity awaits them. I even heard someone say it here, an idiom, for when life offers you something new: Opportunity knocks. Knock, knock, knock, knock.
```

---

## IC-0051: AN EVENING WITH JULIA MAGGIANO

- Title: AN EVENING WITH JULIA MAGGIANO
- Author (byline): Bridget Grace Sheaff
- Work: AN EVENING WITH JULIA MAGGIANO
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: PLAYWRITING CREDITS, CARRIE
- Teaser before the introduction: No
- Spoken words (computed): 2501
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
A 10-minute one woman show

By Bridget Grace Sheaff

Bridget Grace Sheaff: DC AREA DIRECTING: Parlor Room: Burst; Monumental Theate: Infinite Future; Perisphere Theater: Tartuffe; Nu Sass Productions: Exit Carolyn; We Happy Few: The Dog in the Manger, A Midnight Dreary; Spooky Action Theatre: Motherless Children; Source Festival: Static, The Physics of Now, Ball Drop; REGIONAL: Cape May Stage:Merry Melodies, Savage in Limbo. ASSISTING: Constellation Theatre: The Wild Party. Signature Theatre: Titanic; Spooky Action Theatre: Collaborators; Theater J: Sons of the Prophet; Rorschach Theatre: very still & hard to see. Cape May Stage: Mistakes Were Made, Other Desert Cities, Blithe Spirit, Moon Over Buffalo.

PLAYWRITING CREDITS: The Strand: And Maybe a River Will Come; The Fine Arts Association: An Evening with Julia Maggiano; Nu Sass Productions:The Next Table; Ohlone College: Exit Interview; Gallery Players: Art of Preservation. As a playwright, she has published many written works, including Perfect, Forgive and Forget, love letter to my home town, A Chance of Rain, The Days of Peanut Butter and Honey Sandwiches, Idle Hands, Kissing Lessons, It’s Not About the Hair, Danny's How-to-Vlog, The Art of Preservation, The Next Table, and Decisions. Bridget Grace is the casting director and associate producer with We Happy Few Productions and the Casting Manager with Spooky Action Theatre Company. BA 2014, The Catholic University of America. www.bridgetgracesheaff.com

A note on form: Ellipses (...) are thoughts not being completed but not necessarily a trailing off. More like shifts in focus rather than intrigue or lack of energy. Think of them as internal pauses. A dash (-) is a self stop. When she self-edits, that’s when she completely reverses direction.

Lights come up on a stage set for a one-woman show. There is a high stool, a microphone, a bottle of water. The stage sits empty for just enough too long. CARRIE enters, hesitant and nervous as all get out, but in a rush. She steps up the the microphone.

CARRIE: Um, hi, hello. (mic feedback) Uh, wow. Sorry, I don’t… my name is Carrie. I’m um, clearly I’m not Miss Maggiano. I know that. You know that. She knows that, ha, she DEFINITELY knows that. Miss Maggiano is not... She’s, uh, she’s running SERIOUSLY late. Stuck in traffic, we hope. Um… so, I’m her understudy?

(pause)

Right. So. Right. I agree with you. I don’t know why she has an understudy on a one woman autobiographical play that she wrote and directed and produced and starred in and yadda yadda yadda. Except maybe for such an occasion… like this one… right now. And even then, I don’t…. I don’t get it either, really.

But it does seem weird for me to get up and tell you her story because… you came to see her and not me. That’s part of the appeal of “An Evening with Julia Maggiano,” right? “From the mouth of the star herself.” It’s on the poster. And, obviously, I’m not the star herself. And I don’t have her mouth either. (reeling) Sorry. That was a weird thing to say.

(pause)

I’m gonna be honest, I didn’t even really memorize the play because I thought it was so, uh, ridiculous that the woman even wanted an understudy for her play. I told Jim, the, uh, sorry, he’s the stage manager, (pointing to the back) he’s up there, I told him that there was NO WAY that I was EVER going onstage as an understudy because… because that’s an insane thing. I was like “Jim, this is insane. She’s insane. Sure, she has five Tony nominations and she’s a legend of the American theatre and she once played opposite Richard Burton, but she’s MUY LOCA!”

(pause)

I minored in Spanish.

I’m, um, stalling. Sorry. No, I’m not sorry. Women apologize too much. That’s what everyone says. And so then I feel like apologizing for apologizing too much and then... But that’s not about me. Right? That’s not… it’s about Julia Maggiano. Julia… Maggiano…

Should be here… by now…

So, okay, I know a little bit of the show. I can do the opening monologue part, anyway. If you want. So, okay, for like context I think you have to understand that when Miss Maggiano comes onstage, she’s wearing this, uh, it’s this black nightie, essentially. It’s silky and it’s lacy and it’s-it’s actually really classy. And she’s barefoot. And she’s holding a whisky glass and she looks amazing because she spent like an hour on her makeup or whatev- she probably doesn’t want you to know that, now that I think about it. Sorry. Anyway- So she walks onstage after the lights have come up and she says… I’ll do it, hold on, I got it.

CARRIE walks off slightly to make an entrance. She dons the Miss Maggiano persona and struts on like she owns the world. Her Miss Maggiano impression is smoky and sultry and, as far as we can tell, spot on. She walks center and plants at the microphone. She takes in the audience, snorts almost haughtily and begins. When CARRIE speaks as Miss Maggiano, the lines are in bold.

“I’ve only ever had one great love in my life and that was... the theatre!” (CARRIE drops character and talks to the audience) Right? That’s like chilling. And identifiable, right? Anyway, so she starts and we are like “I’ve only ever had one great love in my life and that was… the theatre! You wouldn’t understand it. They always say that you never understand true love until you have children. Well, pardon my French, but that is sheer bull-honky!” Okay, so she says something other than bull-honky… but I just… There’s some really strong language throughout and I don’t want to… It’s all her. She has a mouth like a sailor, let me tell you. You should hear her when there is mustard on her sandwich.

(pause)

Personally, I like mustard. But anyway. So, she basically does this whole first bit where she is talking about how she never got married and never had children and she doesn’t feel bad about it at all. She’s all “The only regret I have is that my mother didn’t live long enough to realize she would never be a grandmother.”

(Long pause. This line has upset CARRIE.)

She’s not the nicest lady. I don’t know, it seems like she didn’t have the greatest relationship with her parents. I had really great parents. Julia- Miss Maggiano, I mean… I don’t think I’m supposed to call her Julia. I mean, I feel like I could. I am supposed to pretend to be her. That is the job of an understudy, right? To fill in? But… I don’t know. I don’t really feel like she and I have all that much in common.

Sorry, this is too much information, isn’t it? But I can see Jim in the booth telling me to keep stalling. You can’t see him, because he’s behind you. Don’t turn around, he hates that. No, really, don’t. (trying to get the audience’s attention) No, no, no wait, okay, um… okay. I just broke up with someone! Great… that got your attention.

Uh… I wasn’t really going to talk about this because… I’m not really supposed to talk about myself up here. Sorry. I was just… Jim really doesn’t like people looking at him.

Okayokayokay, you keep turning around, so fine. FINE. So, there was this guy. And he was my best friend. And he was… he was probably the love of my life, really, and we broke up. That’s it. That’s the story. It’s just like every other story of every other break up. It’s really not that interesting. I’m sorry.

No, I’m not sorry. I’m not sorry that it’s not interesting because I don’t care if you don’t find it interesting because this isn’t my play anyway so what do I care if you are interested. This is Julia’s fault. She’s the one who isn’t here doing her job.

You know, there’s this part in the play, she’s basically talking about her work and she has this section- “You can tell right away who is good and who is coasting by how they treat their work in the theatre. Those who treat it like a game or like a blind date, (makes throat slitting sound) ffttt! But, those who treat it like their craft, when it’s the thing that makes them get up in the morning, they are the ones who make something extraordinary.”

I hate that. I do. I hate it. She says stuff like that all the time, but you know how she got famous? Her mother paid a director for her first real acting gig. That’s absolutely true. Absolutely. (pointing to the booth) Jim, shut up, don’t even. It’s true. She was 15 and she auditioned for Our Town and her mother PAID for her to play Emily. I swear it’s true. She told me. She told me when she gave me the job she was like, “Caroline, the theatre is a tricky business. Look at me. My mother scrimped and saved and when the opportunity came along paid my ticket into this business. If you don’t have that… well. A credit as my understudy could get you one step closer to doing this the old fashioned way. With grit and sheer will.”

That’s not in the play. That actually happened to me. And my name’s not Caroline, but whatever. And so, yeah, sure, whatever, I’ll understudy for the Gloria Swanson doppleganger. No biggie.

Pete… that’s my… was my guy that I broke up with… Pete was like “Carrie, you don’t want to do this, why are you? Why are you sacrificing your time when you could be doing something big with your life?” And he never got it. Really. He’s not in theatre. So he never really got what it was like to go to an audition and to look at the people across the table who were judging everything you were saying and doing and to just feel so…

Sorry. I don’t really want to talk about this. And you don’t really want to hear about it, so let’s talk about Miss Maggiano some more. Um, so, her mom wasn’t always the best influence on her. And she talks about this in the play, so I know it’s okay to talk about. Unlike the paying for the Our Town thing… Don’t spread that around, okay?

Yeah, but, her mom… she sounds like a scary woman. Like she gave Julia diet pills and antidepressants and really just… really just screwed her up a lot, ya know. She has a lot of resentment. Julia, not her mom. Her mom died when Julia was like… I think she says she was 25, right? Jim?

I’m 25 now. How does a 25-year-old get an understudy job for a fifty-fiiii--- (halfway through realizes she shouldn’t say Julia’s real age) forty year old. She’s forty.

(trying too hard to save it) She doesn’t look a day over 37, does she?

But, man, to lose your mom that early? Even, like… even if you didn’t like your mom, still. I like my mom. A lot. I love my mom. I can’t imagine being without her. Like, when I broke up with Pete, she was the first person I called and she was so great. She was so supportive and compassionate. She told me I had plenty of time.

Plenty of time to have kids and start a family, she meant. Though… She never tells me I have plenty of time to have a career and be an actress. She’s always like “Are you sure? What about money, Carrie? What about babies, Carrie?”

Maybe she doesn’t really think I have plenty of time after all. And I know, I know she wants to be a grandmother. It’s all she talks about with my brother and his wife. And they can’t have kids. It’s a whole… thing. So it’s just me.

Julia says in the play, “Alone is the place where I thrive. Alone is where I live. Some people vacation in being alone, but I have been paying the mortgage there my whole life.” She doesn’t say loneliness… Just alone… Where the hell is Julia?! This is so unprofessional. And inconsiderate. I mean, yeah, whatever, she thought she had hired someone to cover for her if something like this happened, but what did she really think was the best outcome here? And to not even call?

You know that Maggiano isn’t even her real last name? It’s Bianchi. I don’t know why she changed it, but she did. I don’t get stage names. I feel like the name you are born with says something about you and if people can’t handle that then like, what are we even doing in this business in the first place?

Pete didn’t get why I didn’t want to take his last name when we got married. (She stops. She closes her eyes) Sorry. I just said “when we got married.” And clearly we are not. Getting married. And we’re not a “we” either. We’re not even a “when” anymore. Anyway. He didn’t get it and I tried to explain that it wasn’t some like feminist statement or anything it’s just that if I got gigs and started to really have a career in this thing, then I didn’t want my name to change because your name is your brand. Right? You all showed up today because you thought you were going to see Julia Maggiano. “Julia Maggiano. The name just glides off the tongue, doesn’t it?” She says that in the play, too.

And, okay, I’m sorry. I’m really sorry. I know you paid good money for these seats and you came to see Julia and I should be giving you Julia but you don’t want watered-down-Julia from some heartbroken kid who doesn’t know what it is like to do this career for longer than 20 minutes. You don’t. I promise you you don’t. You want Julia! Julia who has preserved and come out the other side. Julia who has seen it all and done it all and said it all. Julia who is… I mean…

She’s like, everything all the time. She’s a hurricane to be around and I admire her. So much. But, when you aren’t looking at her, and Jim, Jim can back me up on this, when you aren’t looking, she has the saddest eyes I have ever seen.

Just… heartbroken. “I don’t need anyone else to be happy. Applause gets me there.”

(choking up. Taking a second.) Sorry.

Jim is waving me down. I think Julia is here. Um… she’s gonna need a minute to get ready and I’m sure she has just an amazing, crazy story for where she has been and why she is late. So… if you all could just, sit tight for a second. She’ll be right out. Okay? Don’t… don’t tell her… okay? She’s just… you know what, whatever, you can tell her. She should know what I said. I don’t… I don’t care, I’m done. Thanks. Okay. It’ll be just a minute.

CARRIE takes a second to see the stage, to feel what it is like to be onstage in front of people, and then exits. The stage is bare. Lights out. END OF PLAY.
```

---

## IC-0052: God, If You’re Really Out There

- Title: God, If You’re Really Out There
- Author (byline): Cynthia Riebesell
- Work: God, If You’re Really Out There
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2302
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
Characters:

Alana Grant (pronounced Ah-lah-nah) Henry Grant Pastor Jones (can be any gender)

Author's note: The piece you’re about to read takes place in 2001 right after the 9/11 attacks. 50,000 employees worked in the World Trade Center buildings. Yet, when the Hijacked planes of the September 11th attack hit the towers, only 20,000 were busy working at their desks. Of those 20,000, only 3,500 died. People argue that it was God who spared all those other lives. So does this mean he was also responsible for the thousands of people who lost their lives? This one question haunted Alana’s mind. After her husband’s death in the 9/11 attack she begins to question the entire existence of god. While saying her husband’s eulogy, she publically releases her isolated feelings and battles her faith in ‘God, if you’re really out there’.

Setting: After 9/11 attacks on New York City’s Twin Towers, inside a church for the funeral of Henry Grant who was in the buildings.

……………………………….............................................................................................................

Curtain Rises to:

(Outside the church door, Alana stands, dreading to make her steps through the door)

Pastor Jones: Alana? Are you ready?

(Alana glances at him, then looks forward, obviously looking like she’s not ready, but does not say anything)

(Pastor Jones touches Alana’s shoulder in a sentimental way, and walks into the church)

(Alana stands there and takes a very deep breath, then wipes her eye where a tear was falling down her cheek)

(Lights dim and lights rise to Pastor Jones standing at the church’s podium at the front of the church.)

Pastor Jones: Today we gather to say our final goodbyes to an extraordinary man, Henry Grant. During this difficult time, God watches over us all, more than he ever has before. He’s before us, easing all of the pain we feel in our hearts and souls. As each difficult day passes, he makes the next easier to bear. When I was 10 years old, my grandmother died. I hadn’t really been exposed to death prior to that event, so I didn’t fully understand the situation. I remember my mother came up to me and said, “You’re Grandma Jones is in a much better place now, honey.” I didn’t quite understand what she meant. Did she mean Grandma was on vacation? Was Grandma relocated to live in a more scenic place? I didn’t think anything of it, until the day of her funeral arrived. I remember looking around at all the people in the church. They were hugging each other, with tears falling from their eyes. During that time, the biggest question in my mind was ‘why?’ Why were people sad? Why were they crying? However, like a bullet, I soon had my question answered. My grandmother’s casket made me realize this ‘better place’ was referring to death. I stared at her casket, completely ignoring the pastor’s sermon, wondering how death could mean a ‘better place’, and as if reading my mind, the pastor then said, “She is in a better place. With no pain, she rests in God’s arms.” A week ago, on September 11th, our country’s people took hands and prayed for any kind of miracle. God has provided that miracle. He made Henry’s pain go away, and made his trip to Heaven a painless journey. He’s up there, in Gods arms, spreading his humor and witty persona among all the others whom we have lost in our lives. He is in a better place. With no pain, he rests in God’s arms. Now, let us hear Alana’s eulogy for her husband. (Looks at Alana and directs her forward by saying...) Alana.

(Alana gets up from her seat and walks to the front podium)

Alana: (awkwardly, unknowing how to greet the mass of people) Hello. (She then looks down at her note cards which has her prepared speech written on it)(Takes a deep breath and smiles) Henry and I met in high school during our sophomore year. He was on the debate team and I was on the school newspaper. I was writing an article about the state debate tournament, which Henry was competing in. I remember watching him debate with the other panel members. From his performance, I knew he would be the perfect person to interview about the tournament, so after the tournament, I managed to get an interview with him. Flashback

Henry: You know, I’ve been on the debate team for a long time now, but never have I been bored. There’s always something new to learn and there’s never a moment when you can just relax with the impression that you’ve got this debate in the palm of your hand. I’m always at the balls of my feet, ready for that particular competitor to hit me with an argument, which I hadn’t already thought of.

Alana: It sounds like you’re really passionate about this activity, Henry. What else are you passionate about?

Henry: Well, don’t laugh, but I am pretty damn passionate about Pac Man. I could play it for hours. You know, someday they are going to begin to tell us that we are too reliant on technology. That’ll be the day! But really, did you know that there are over 200 Pac Man products?

Alana: Holy cow!

Henry: It’s incredible! What about you? What are you passionate about?

Alana: Well since you admitted an embarrassing passion—

Henry: Hey! Mind your Pac-MANners! It’s not embarrassing! It’s… (Pause) Okay, yes, it’s embarrassing…Well c’mon, what’s yours?

Alana: Um, Well… I have about 56 posters of John Cusack all over my bedroom walls…

Henry: (laughs) Now THAT’S passion.

Alana: (giggles) I know.

Henry: Hey, do you wanna go get some pizza?

Alana: I’d love to.

Henry: Well come on then, I’ll drive. Hey did you know that the creator of Pac Man generated Pac Man’s shape after removing a slice from his large pizza?

End of Flashback

Alana: Somewhere in between the conversation involving his love for Pacman and mine for John Cusack, I realized he was the one for me... We dated through the rest of high school, practically glued to each other’s hips. After we graduated, he proposed. We got married and moved out of Minnesota to live in the one place him and I always dreamed about, New York City. Being with him in the city that never sleeps was ironically like living in a dream with him. (Smiles and laughs, thinking about the memories) He was such a goofball. I remember this one time; we had been walking down the sidewalk on the corner of Broadway, arguing about something.

Henry: Alana, I’m sorry… I didn’t mean what I said. Your mother isn’t a witch. I’m sure her soup is wonderful. I highly doubt she adds poison to it whenever we’re over at her house… (Almost sarcastic) C’mon Alana, stop walking away from me… (Grabs Alana’s arm) I’m sorry.

Alana: No, Henry. You’re always making jokes like that about her! It’s not fair, you know she loves you and treats you wonderfully.

Henry: (under his breath) When you’re in the room, yes.

Alana: I heard that, Henry! You’re unbelievable.

(Keeps walking away, Henry doesn’t move—instead he gets on his knees and begins singing)

Henry: BABY COME BACK! YOU CAN BLAME IT ALL ON ME!

(Alana turns around and rushes back to shut Henry up.)

Alana: Henry! What do you think you’re doing?!

Henry: I WAS WRONG AND I JUST CAN’T LIVE WITHOUT YOU!

Alana: Stop singing right now! You’re making a scene!

Henry: Forgive me then!

(Alana hesitates, Henry notices)

Henry: ANY KIND OF FOOL COULD SEE!

Alana: Ok, ok! (Giggles) But only if you stop singing!

End of Flashback

Alana: He was an awful singer… (Alana smiles real big, but slowly the smile fades and she sets down her note cards and begins to talk from her mind rather than her prepared speech) Talking about all these memories really makes me realize how much we’ve gone through…Now, he’s gone.

For a week now, I’ve been sitting alone in our apartment. All of Henry’s things sit in the exact same place he left them. His check book, which he had forgotten to take to work, sits on the kitchen counter. The shirt he had worn the night before the attack, hangs on the bedpost, and I can still smell his cologne on it. Even his half eaten pop tart still sits on the kitchen table. Everything I do, or see reminds me of him. I still feel as though he’s going to come walking through that door at any moment but I know he never will. It’s just me now. What have I got to believe in anymore? God? This guy, (points to cross behind her) on the cross? I mean, what has he done? (Pauses, controls temper) You know, I’ve never been that religious. Growing up, my family and I only attended church during the holidays. We never prayed. We never sang religious songs. But I still held the belief that there was something—anything-- beyond this world. I believed that there was some kind of higher power, perhaps in some alternate universe. Not necessarily ’God’, but just some kind of almighty being. But now, I don’t know what to believe.

(beginning to tear up) We were having a great morning. I remember Henry being so excited about this idea that he was going to pitch to corporate.

Flashback

Alana: You’ve got this honey!

Henry: All the work is about to pay off! We’ll finally be able to afford that apartment. We’ll be able to start a family.

Alana: Let’s not get ahead of ourselves, dear. You get through that meeting first.

Henry: I love you so much, Alana.

Alana: I love you too, Henry. Go get em’!

Henry: Ah, I love you, I love you, I love you! (Hugs her tight)

Alana: Go! You’ll miss your meeting! I’ll be here… And maybe when you get home tonight I’ll finally have that 6th chapter finished in my book.

Henry: I’m so proud of you, baby. Today is going to be such a wonderful day, for the both of us!

Alana: (smiles and looks at Henry happily) Alright, honey. Get going. I love you! Good luck!

End of Flashback

Alana: He ran out the door, with such a happy bounce in his step. He kissed me goodbye and left for work. If only I’d known it’d be the last time I’d ever see him. Ever feel him. Ever hear his voice. Couldn’t ‘God’ have warned me? Somehow? At about 8:30 AM, I got a call from Henry. He was telling me that corporate had loved his idea and they‘d love to promote him to upper management. I remember thinking to myself; we’re really going to make it. We have such a bright future ahead of us. We hung up, and literally no more than 20 minutes later, my phone began ringing again. It was Henry. However, the only sound I could hear was his breathing. It was slow and raspy, as if something was blocking his airway. I knew something was wrong, but before I could say anything, the sound of sirens began echoing from the streets. I looked out our apartment window and saw black smoke filling the sky. I turned on the TV to see if there was any news about where the smoke had been coming from and on the screen; the Twin Towers were being shown. The north tower had smoke flooding from it, as if there was a giant explosion, and that’s when I realized (pause as if visualizing it) it was Henry’s office. I started screaming and begging for him to tell me if he was alright. I wanted him to assure me that he was safe and out of the building. But when he finally spoke, the only thing he said was,

Flashback

(Lights fade slightly; still able to see Alana)

Henry: (spotlight goes on Henry) (Alana also mouths these words but Henry actually says them) Alana, I love you.

(Henry’s spotlight goes black, and Alana’s light goes back to normal)

End of Flashback

Alana: But before I could respond, the line was cut, leaving only a dial tone left to be heard. I looked at the TV and saw the tower slowly beginning to fall. Floor, by floor, by floor. And I just stared, hoping that when I closed my eyes to blink, I’d open them to find all of this to be just a figment of my imagination…But I blinked and I blinked and nothing. This terrible, awful act of terrorism was reality. Henry, a kind, sweet, huge hearted man was the victim of such cruelty. I mean, how could someone so marvelous be killed by something so dreadful? (Sadness turns to anger) On the internet, I’ve read stories about how god delayed people from getting to work on time. Like for example, one lady’s alarm clock didn’t go off, so she wasn’t at work when she was supposed to be. This one guy got a blister on his way to work, so he had to stop at a drugstore to buy a Band-Aid. And for another guy, it was his turn to bring the donuts, but I guess he got to eat them all by himself. I mean, if these stories really are Gods doing, then he prevented about 16,000 people from being to work on time, resulting in their lives being spared. Then why couldn’t Henry have been one of those people? Where was God for Henry? (Alana stares into space with tear soaked eyes, she begins to reflect)

Flashback

Henry: Aren’t those clouds just beautiful next to that blue sky?

Alana: Yes, they are. It’s so easy to forget to look up every once in a while and when you finally do, it’s like a breath of fresh air.

Henry: It’s incredible. (looks away from looking at the sky to face Alana) Alright, I’ve got another one… if you had to choose would you travel to Malaysia or Romania?

Alana: (thinking…) mmmm…good one. I think Romania….Alright, my turn? Would you ever take your life to save someone else?

Henry: You know, sometimes I think about that. I think about whether or not I would run into a burning building to save someone… Or if I’d give my heart to you, if the doctors said you had very little time left. Yes, yes, I believe I would. Because I’ve already felt all the happiness in the world—living here, in this city, with the love of my life-- and knowing that I could give someone else a chance to keep living on in happiness, for some reason, makes me feel really good. (sees the hurt reaction Alana has thinking about the small chance she might lose him on her face and says…) But you know what; it’s so peaceful, being here with you. Let’s not think of a future where we’re apart. Let’s think of right now, under these clouds...

End of Flashback

Alana: (looking in the same direction she was with tears in her eyes and then faces her audience again) You know, if Henry were here, he’d probably scold me for only worrying about him. Knowing him, he probably would have wanted me to be happy that those thousands of lives were spared at all. And I am! But Henry isn’t alive. And to be able to accept that doesn’t seem humanly possible for me at this point. But until I find the courage to move on, I have but one last thing to say. A prayer. (Pause and look up to the sky as if talking to God)(Spotlight on Henry begins to go on and he looks at Alana) God? If you’re really out there, I think you owe me a small favor. Just please, please tell Henry one thing for me. I love you too. (Alana keeps gaze towards the sky, as Henry smiles at her) (After a few seconds, lights go down)

Curtain falls End of play
```

---

## IC-0053: H for Hercules

- Title: H for Hercules
- Author (byline): Taren Pfitzer
- Work: H for Hercules
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1021
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
Taren Pfitzer

Hercules, a large middle-aged man, steps onto the stage.

Mmmhmm.. Yup all gone. See?

(Opens mouth. A beat, then he spits out the pill hiding in the side of his mouth)

Oh, well hi there? You’re new here aren’t you? Well hi, my name’s.. uh…. uh… You know I think it starts with an H. Henry, or Harrison, or.. well it doesn’t really matter. So whatchya in here for?

What ain’t you gonna talk? You’re not deaf or something are you? (tests audience hearing) Well fine. If you ain’t gonna talk then I’ll just have to do the talking for the both of us. I love to talk. Hell, talkin’ is my favorite thing. Or at least it is one of my favorite things. You see I like to find new favorite things; it keeps life interesting. That’s what I’m here for: liking things. My favorite things.

So what kind of pills do you have to take? I have to take these blue ones with a white stripe, and well, they’s the reason I can’t remember my name. My doctors all tell me “Well we can tell you your name” and I tell them “nope! H is fine thank you”. H is the best letter as far as I’m concerned. Do you have a favorite letter?

Well what about a favorite thing? Really? You still ain’t gonna talk? Ok. Well I’ll tell you what my newest favorite thing is. It’s great. It’s this brand new thing called Netflix. Now I know what you’re thinking: “Now H, Netflix ain’t a new thing; it’s been around for a real long long time now”. No it ain’t. I ain’t never heard about before so it’s new to me. And you wanna know what my favorite thing to watch is? Hercules. Oh I love that movie. You see Hercules is the story of a young man who is forced to drink poison because of the devil and has to save the life of a girl, ALL TO BECOME A HERO! I love that movie.

I used to watch it all the time with my little girl.

You see it was her favorite movie too, ‘cause her name is Meg just like the girl from the movie’s name is Meg. I don’t… I don’t like talking about her too much..

uh…. I’m sorry. I get sort of emotional on account of these pills. Not the blue ones with the white stripe but these other ones. These white ones. You know, the ones I just “took”. I don’t like those pills. Those pills make me feel sad. They make me feel weak. And I tell my doctors “I don’t want to feel sad or weak… and.. and you can’t make me!”. My wife used to make me feel sad and weak. That’s what lead me to find one of my, other, favorite things.

Alcohol.

You see alcohol was what made me feel like Hercules. I could take anything that my devil of a wife would hash out at me. But then she wised up… she learned she couldn’t hurt me anymore so she…. she… ahhh that doesn’t matter. You know? I like you. I’m glad we’re best friends now. My doctor keeps telling me I should make more friends. Jesus it’s like I’m a little kid again. I probably said the exact same thing to my little Meghan. She always had problems making friends. I think it was because of my wife. She’d always put her down, make her feel bad about herself. I remember there was this one time she was yellin’ at meg for something she did. She was yellin’ because Meg didn’t do something just right, it wasn’t perfect. I remember getting out of my chair and saying “Yeah? Hell, when have you ever been called perfect?”.

You wanna know what my wife did then? My devil of a wife? She looked me right in the eyes and said:

(as his wife) “If you ever tell me how to treat my daughter again. If you EVER talk back to me again… I’ll call the police. I’ll call ‘em up and tell them that you just hit me and that you’d been threatening to hit me ever since we been married. You wanna see your little girl again? Then SHUT. UP.”

I bet you could guess what I did then?

Nothin’. I. Did. Nothin’. I drank my anger away. Then my wife did something that... shook me to the core. She turned to my little girl and said:

(as his wife) “You see that Meghan? Your daddy’s no hero. No he’s a sad drunk. He’s sorry excuse for a man.”

I like to think that I’m nice man. Always treated my little girl like the princess she is, even when I was drunk. But when my wife said that. Something in me just...

Snapped. I got up out of my chair, went up to my wife and said “You wanna tell the cops I hit you? Fine. Let’s give you something to talk about.” And I hit her. I hit her over, and over, and over again, and I couldn’t stop. My little girl is grabbing my leg screaming.

(as his daughter) “Daddy stop it! She didn’t mean it! JUST STOP!”

But I couldn’t stop. I had to beat the devil. And that’s what I told my lawyer. I told him I had to beat the devil; and my lawyer told the judge I was not “competent enough” to knowingly hurt someone. That my “delusions” was brought on by my addiction to alcohol. That’s why I’m here! That’s why I can’t ever see my little girl again. That’s why to her, I’ll never be a hero. I’ll never be Hercules. Well you know I may not be Hercules; but I know how he feels. I know what it feels like to be ripped out of your home, forced to drink poison because of some devil, and how hopeless it can feel when you’re trying to save somebody you care about.

(Chuckles) Hell, maybe I am Hercules, I don’t know. But what I do know is, is that I like you and I like this whole talking thing. Who knows? Maybe this, is going to be one of my new favorite things.

END
```

---

## IC-0054: History Lesson

- Title: History Lesson
- Author (byline): Dan Trickseven
- Work: History Lesson
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1742
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
Let me tell you a joke. My friend Jake killed himself last week. A couple weeks ago now, about a month before the end of our junior year in high school. So here’s the punchline: Jake texted his suicide note. It was, technically, a suicide text. But he'd just gotten a new iPhone, and they made him change his number. Why he got a new phone the day before he killed himself, I don't know. It’s not like the phone survived the fall. So why’d he bother getting it? I know his parents didn’t buy it for him, Mr. Stonebridge is the friendly miser type, and Mrs. Stonebridge wouldn’t know an iPhone from a WiiMote if her life depended on it.

So Jake got a new phone just in time to text all his friends his suicide note. Which meant he had to reenter all the numbers of his contacts. And he entered mine wrong. So after it happened, everyone knew. And they were scared to call me because they thought I'd know, I was Jake’s friend, obviously I got the text, and if I needed to talk or whatever, I'd call them. But I didn't get the text because Jake put it in his phone wrong, so it wasn't until 24 hours later some idiot girl I barely knew posted on my facebook wall a simple "sorry" and I posted back "sorry for what" and this girl sent me such an angry message that I finally called our other friend, Mark. He forwarded me the text.

Here let me read it to you. You won’t believe what Jake wrote. (he opens his phone.) Oh, no. Wait, sorry. I deleted it. I forgot that.

What did it say? You know, I only read it once. I thought I kept it. Maybe I hit the wrong button, or something. I was upset. Maybe I thought I wouldn’t want to read it again. Well, I’ll just have Mark forward it to me again... (he stares at the phone.) Later.

So, I’m not going to make you wait until the end, to figure out why Jake did it. I hate when they do that, in movies and such. Show you the dead body but then you have to wait the whole time to figure out why he’s dead.

My friend killed himself because he was in love with his teacher. How do I know this? Well, get this, the Stonebridges asked me to help go through Jake’s things. I guess his parents were a little afraid. They pretended like they were being nice, you know, Jake would want me to go through his stuff, but I knew they were afraid. I was glad to help, you know, you like to feel useful at times like this, when I am realizing no one is useful because there is absolutely nothing useful to do. I knew Jake’s writing pretty well. It was typical insane guy stuff. In 8th grade he wrote a whole novel about a squadron of heavily armed hamsters fighting an unbelievably violent war against a dark legion of ghost ferrets. But I mean, that’s not like suspicious or anything. if I had a friend who didn’t think it was funny to see an evil ferret’s head get blown off, then I would have been suspicious.

I was surprised when I found Jake’s journal. I would have never pegged him for the journal-keeping type. It was between two stacks of school notebooks in a bin under his bed, disguised, quite cleverly, as yet another school notebook filled with notes about the War of 1812, otherwise known as the war fought just so we could learn about it in school, fail a pop quiz about it, then never think about it again for the rest of our lives. I only opened it because I literally could not remember a single thing about the War of 1812, and I wanted to read about it in Jake’s ridiculous notes, which usually added things like “he was the only President who attributed his success to eating a smoothie made of dog turds in the morning,” again, pretty brilliant.

So anyway, two pages into the notes, it’s suddenly his journal. He seemed like a typically unhappy teenager. Life will never be complete, has no meaning, etcetera. I know what you’re thinking. That he should have gotten help, that he spiraled into despair. But as I read through it, the opposite was true. The entries got happier and happier as they went along, because more and more they were about Mrs. Carmichael, the aforementioned history teacher with whom, it is now clear to me, Jake was becoming quite intimate, the translation of that sarcastic teenage phrase being they were humping.

Anyway, let me read the key entries.

Today Mrs. Carmichael caught me looking at her, again. Except when I looked back to see if she’d really caught me, she was staring back, kind of smiling. I smiled back, then I felt like a dumbass so I looked back down and tried to do my quiz. I failed the quiz. Mrs. Carmichael handed it back to me at the end of class with an A on it. I covered it up. I was embarrassed, I didn’t want anyone to see she had given me credit on the wrong answers.

It proceeds from there. Two weeks later.

I walked Mrs. Carmichael to her car. We were talking about the Quiz Team. She said we should all have practice at her house. The whole team should come over. I could tell she wanted just me to come. I told her I wasn’t sure if I could come next weekend. Then she got really mad, said I wasn’t dedicated to the team or whatever. I thought girls got crazy but Mrs. Carmichael was at another level. No wonder Dad sometimes spends nights away from us, if Mom is like that. But I told Mrs. Carmichael I’d definitely come. She smiled and I smiled back without looking away.

Are you hoping that Jake wrote about that night at Mrs. Carmichael’s? Well he most certainly did, and I think he did it while he was still drunk!

Oh man, oh man that was fun. Me and Tammy (That’s Mrs. Carmichael) we talked through everything. She’s such a cool teacher. She really got me. She got my life, she’s been through it all. And she’s so cool! Like a cucumber. A frozen cucumber. With smooth skin. Like a cucumber.

Drunk Jake was apparently fascinated by this image. Obviously things were heating up. He goes on, from a few days later.

Damn I did not think it would be like that. In her car, parked by the empty mall. Her hair was like midnight gold and I had it in my hand. Damn damn damn. Love, when it comes, is extraordinary. I did not think I would be so corny but I can’t help myself. I want it so much, everything. She told me I was her dream come true. I told her the same thing.

And then of course, at the very end, things went bad. Jake didn’t write about it, per se; but those of us with three brain cells can put two and two together from this entry.

I guess dreams never quite come true. I guess happiness is an illusion, and we’re all here to suffer. Whatever. I guess when you have something you have to hold onto it really tight. Because you’re going to lose it. It’s going to die. That’s how the world works. It gives you things so it can take them away. Or even worse it gives you them so you can fail at them.

She must have dumped him, or chickened out was the right word. No surprise here, that Jake was the strong one, and this harpie was a coward. She was not there for Jake. She was only doing it for herself, and she didn’t realize. And then Jake saw himself like the War of 1812, something that happens, and everyone forgets about. He saw himself as useless, when all he really was, was hurt. And listen to the last thing Jake wrote.

I think I can still make it work. I think I can still show her that our love is strong enough. If I am strong enough to do it, our love is proven RIGHT.

I didn’t tell anyone what I saw in Jake’s journal. The day after I read the journal, I looked up where Mrs. Carmichael lives. And I drove there, kind of in a trance.

So there I was at Mrs. Carmichael’s house. What was I gonna say? Obviously, there’s the conventional play where I yell at her for Jake. Tell her she reached her hands up inside him and twisted until everything broke, until what we loved about Jake oozed out into the ground in little Jake-smelling puddles. But I couldn’t handle either reaction that she would have.

I drove away. I didn’t tell anyone. Not even you, really. The names are changed and there’s an actor up here, saying these words right now. No one will know about Jake and her. It’s not a big deal. What stopped me from ever telling anyone, like Jake’s parents or the authorities or whomever you deem appropriate to know about such a relationship, was that I could not stand thinking that suddenly it would not be about Jake anymore. That suddenly, Jake’s life, and Jake’s death, would be about him and Mrs. Carmichael. No one would talk about Jake without talking about her, no one could remember Jake without thinking about what happened. And I thought that would be unfair. I wanted Jake to be Jake, forever.

And of course she never said anything. Like I said, a coward.

Is that all the time we have? (He looks at his phone) Oh wait, I have the note. Here in my deleted folder, I forgot it had one of those. So do you want to hear it? Yes, you do. You sat here and listened to me hoping I’d get to something like that. So here goes.

From Jake Stonebridge, 10:43pm.

I love u all. Its the right thing 2 do. Miss u already. Wasnt meant for this world I have 2 much luv and nowhere for it to go. Will send it 2 u from beyond always.

Jake, buddy. I feel your love right now. But you were wrong, man. We always had a place for your love.
```

---

## IC-0055: How to Eat Cat Food with Dignity

- Title: How to Eat Cat Food with Dignity
- Author (byline): Clint Snyder
- Work: How to Eat Cat Food with Dignity
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1196
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
A Dramatic Interpretation (Male/Female)

By Clint Snyder

JAIME You look like a nice person, someone that would never judge me too harshly, so I'll tell you a secret. It's a little embarrassing, so you have to promise not to laugh… I ate cat food for breakfast for a whole month one time. Bet you weren't expecting that, huh? I bet you thought “Oh, they probably eat a pint of ice cream every night and bawl their eyes out to some sappy vampire teen angst movie.” Nope. Cat food. And it wasn’t fancy feast either, it was the cheap kind and in case you were wondering, yes, there is a difference in taste.

I walked into the kitchen one morning and I saw it there on the plate. I stared at it for a minute or two, then my dad said, "Go ahead, and eat your breakfast." I wasn’t exactly sure what it was at first, and then it hit me…

My Dad had lost his job about six months ago and we had been struggling ever since. Eating ramen, spaghetti-Os and canned food from the church, but they had been low lately and last time we showed up they didn’t have anything for us. We didn’t have any family we could rely on and my mom has passed a few years back. Thankfully my parents were able to pay off the house before it happened. She had been sick for a long time and the medical bills almost wiped them out before all this. That was it. I was just me, my stupid brother, my stupid father and this big stupid empty house. Oh, and the cat food that reeked.

(Sticks out toungue in disgust.) My dad must have saw me because he got defensive… He always talks a lot when he gets uncomfortable. "Well, yeah… it's cheaper than regular food and it tastes just the same. Back in the army we ate all kinds of things, rats, dogs, whatever we could find. Besides, Fred seems to like it." I'm not eating it. This is humiliating and if mom were still here… if mom were still here she wouldn’t make us." "I said sit down and eat." (Stern.) That was harsh for him. It caught me off guard, so I sat down and surrendered myself to the lumpy oozing meat perfectly shaped to the can it came from. It tasted surprisingly bland, like a little bit of bad tuna mixed in with a lot of sawdust or wet chalk. After the first couple bites it stops tasting like anything, then it went down a lot easier. My brother Fred likes to be called Freddie. He has been Freddie the past three Halloweens in a row and not just because we can't afford a new costume. He really likes it. Nightmare on Elm Street is his favorite movie, which may be strange for a seven year old, but Fred is imaginative and according to him that's the best thing to be. He likes Freddie's ability to punish wrongdoers of the town, or as he likes to put it, "I like to stab bad guys." (High-Pitched.) And while most people might find Freddie to be that bad guy, he only seems to kill lazy teenagers that lie around the house drinking, doing drugs and sleeping too much and besides as my brother put it, " Good guys always win and Freddie always wins, even if the bad guys think they got him. There's always another movie." He has a point.

I've gotten pretty good at hiding the fact that we're poor. If a friend wants to come over then I just say my parents don't like having people over or my house is just really dirty. Eventually they'll cave and we can go over to their house, where they have really nice stuff and stuffed raviolis for dinner. Another important thing to do when you don't have any money is to brush your teeth a lot, even if you don't have toothpaste. Your teeth should look perfect. (Shows off teeth.) Smell is the strongest sense connected to memory and if people remember you as the smelly kid, you're not going to have friends. And you can use baking soda to brush your teeth. .

My brother was always much more vocal about his concerns about money. On his last birthday he said, "This is the regular Freddie claw. I already have one. I wanted the light up sound effects claw. What do you expect me to do, run around punishing my enemies without cool lights and sound effects?!" He did already have the regular claw. He wore it to breakfast every morning. Watching him try to pick up his fork with that thing on was the highlight of my day and made the cat food bearable.

Even after my dad lost his job, he was still out looking for a job or food for us by the time my brother and I got out of school, making us both latchkey kids. I wear my key as a sort of badge of honor.

Freddy’s school is right down the street from mine and we meet up, then walk the nine blocks home. So, like usual, one day a few weeks ago we met up and he was about half a block in front of me using his claw to attack everything, mostly squirrels. Since he didn't get the "light-up sound effects" glove, he provided his own sound effects. (Imitating Freddie) "Shlink! Shlink! You're dead now." The squirrels were genuinely terrified.

“Jaime.” “Yeah, Freddy?” “My stomach hurts.” I stopped. I could see he looked pale, I don’t know why I didn’t see it before. “It hurt all day, but I didn’t want to say anything because they would take me to the hospital, dad’s always says hospitals are expensive and that’s where mom… where she…” My whole body went numb and I felt the whole world slip away around us. “I don’t want to die Jaime…”

His words hit me like a punch. “ That’s not going to happen Freddy… what happened to mom, that was different. You should have said something!” I don’t know why I was yelling. I shouldn’t have been angry, it just made him cry more.

I walked with him twenty blocks to the hospital, crying and fighting all the way. The people at the front desk gave us a hard time for not having insurance and kept asking where my Dad was, but when they saw how much pain Freddy was in the doctor eventually saw him. He said that we were lucky, Freddy had Appendicitis, so they prepped him for surgery and removed his appendix.

When I met my Dad in the waiting room. He asked if Freddy was alright. I said yes and burst into tears… Something inside me had clicked. Dad didn’t say anything about moneym because it didn’t matter. In that moment there was just me, Freddy and my Dad. That’s all there ever was, but we had been so focused on money for so long… wasting our time together… I guess I can live with eating a little cat food every now and then, as long as I can share it with my family.
```

---

## IC-0056: Jack, The Lionheart

- Title: Jack, The Lionheart
- Author (byline): Bobby Lebeda
- Work: Jack, The Lionheart
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 3543
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
AUTHOR’S NOTE

Dedicated to my brother.

CHARACTERS David Richardson: 20 Years- Old, Older Brother of Jack, Star football player

Jack Richardson: 15 Years- Old, Overweight, Angry, Suffers from a severe form of Autism

David’s Dad: 55 Years- Old

SETTING

Blank Stage

TIME

Present Day

Jack, The Lionheart

SCENE 1

DAVID RICHARDSON looks at a photograph. He smiles then frowns. He sets the photograph

down.

David: You know, everyone has that one thing they hate, it could be anything really- Spiders, NASCAR, politics, Sally Marsh after she rejects your invitation to homecoming publicly. It could be anything. For me, it's small talk. I absolutely hate it. Not because I hate people... though there is a very small number of people I'd like to spend more than 5 minutes with, but it's just so awkward. You know? I know it's the common thing to do, but people never know when they're going to hit a topic that you just don't want to talk about. I'm sure everyone has something that the second someone mentions it you quickly, switch the topic to, "so how's that weather today? It's just so... weather-y..." People will ask about the usual. Your likes, your dislikes, where you go to school, what you want to do with your life, your hobbies, your family... your family… that's when I talk about the weather. (He looks at the photograph again. He takes a breath then sets it down).

People will ask about my family and I always end up lying. They'll ask if I have any brothers or sisters... it's just easier to tell them no, then to explain to them the whole situation. The situation about my brother. Sometimes it's easier to lie than to tell truth especially if you've never told the full truth to anyone before. I’ve always wanted to, but never have. I know they’ll look at me differently and someone will get over dramatic about what happened- but damn it, I’m tired of talking about the weather.

It’s funny; I always wanted someone to play with. When I was just 2 and learning how to talk, I begged my parents to give me a brother. They told me that they couldn't just give me a brother. It wasn't that easy. I then asked where babies came from. They began to stutter and started talking sports- that was their topic changer. In a few months my mom was pregnant. I personally thought there was a monster growing inside my mom's belly. I was terrified and would run whenever she would enter the room, so her monster belly wouldn't eat me. To comfort me, my mom pulled me up close to her and she said, “Sweetie, this will be your brother. We’re going to name him Jack. In two months he’ll be born. You two will love each other. We’re going to be a big happy family.” My mom held me tight, so tight, I didn’t think she’d ever let go.

Two months later, when I was 3, my brother Jack was born. I was excited to have a brother though I thought he looked like a lizard because he was all red and scaly. New born babies aren't cute, they're ugly, but you just can't tell that to a woman who just went through 36 hours of labor that her child looks like a lizard... I guess it's understandable why she was mad at me, but her anger didn't matter. I was just so excited to have a brother. It was going to be life changing. I'd have someone to play with all the time. When he was old enough to walk, I called him Jack, the Lionheart. You know after Richard the Lion Heart. My mother was a history teacher, and when we were young, instead of watching cartoons she’d put on history documentaries. By the time I was 5 I could tell you anything you wanted to know about every communist dictatorship. But, like I said, Jack was Richard The LionHeart, my dog was his faithful stead Mao Ze-dog, and I of course was Genghis Khan. Together we would fight dragons, save the princess, and if we had time conquer all of China. That was a typical day for us. (He pantomimes fighting with a sword) It was fun.

Jack had normal development, up until around 18 months all of a sudden things he could do he wouldn't do anymore... like he forgot how to brush his teeth, he would stop making noise all together, and he would throw huge temper tantrums... After a few months of this my parents took him to a doctor... and more doctors. After a while we diagnosed with a unique form Autism Spectrum Disorder. This was in the 90's before, Autism really had become prevalent. I had no idea what it meant... When I was told meant he had a super power that made it easier to fight all those dragons. He’s “super power” ended up to be much worse. Now normal cases of Autism really aren't that bad, usually it just means a lack of understanding of social cues, repetitive behavior and a few other minor characteristics. Sometimes you may not even know if someone has it- They could just be the awkward kid. My brother's case was the most severe anyone had ever seen. They didn't know if he would ever talk normally... and he never did. I never had a normal conversation with him. I had conversations with him, but they were imaginary, just like our adventures.

As we grew older my brother and I would slay fewer dragons. I mean... he never really did any slaying, but I'd pretend he would be. Jack the Lionheart, with his super power of autism, could slay any dragon! It was the only way I could keep him normal in my head. I mean not everyone has a brother who can slay dragons and have the superpower of autism... He did all sorts of weird things which I found hilarious. He didn't like the feeling of clothes, so he'd run around naked. One time my dad had a dinner party for people at his work. Everyone was dressed fancy. My brother ran into the room completely naked. My parents were horrified especially when my brother ran over to my dad's boss and ate his cake. At least he kept life interesting. (Pause)

Soon Jack and I stopped out adventures altogether. I found a new love- football. I would play all the time. I wanted to be the quarterback for my high school football team. Not to brag, I was pretty good. Even when I was just in middle school, high schools all over were trying to get me to play on their team. My mom would take me to all the schools no matter how far. She was there for every practice. She always found time for me. It was one of the most exciting times of my life. She was amazing. Everything you could want in a mother. It looked like my life was heading in the right direction. That was when my life began to change course and I began to talk about the weather much more.

Puberty is different for everyone. For me, it meant that I no longer had any control over my body and would knock things over all the time. It also meant that my voice would crack every time I talked to a girl. When I asked Sally Marsh to the homecoming dance, I said “Sally will you go to home (voice crack) coming with me?” It wasn’t my smoothest moment.

For my brother it was difficult. It's hard enough being normal going through puberty... but for someone with Autism, who can barely understand the world to begin with, he began to react violently. In psychology there are these terms: the Id, Ego and Superego. The super ego is what society thinks you should act. The Id is how your natural instincts. Your ego is balance between the two. The best way to describe it is that my brother was all Id. He couldn’t comprehend what society thought, so he had no ego or super ego. His mind couldn’t understand when something didn’t feel right, or when he didn’t get something he wanted. This caused him to go into fits where he would hit and attack anyone around him... including himself. I remember one morning, my dad was away for the weekend and I was sleeping. I heard this scream, I woke up. It was my mom. She shouted, “David, I need help.” I ran into the room. It was my brother trying to hit her. I rushed over and put him in a headlock, “Jack, stop! This is not okay. This is now how we treat out family.” His “episodes” were fine in the beginning, he was small, but after he grew to be 6 feet weighed 300 pounds, it became more challenging to handle.

My brother loved junk food. He would always want to eat and we couldn't tell him no because... he'd get angry and hit us. Maybe we were weak. I don't know, but there's only so many times that your brother can attack you, so eventually you just learn to let it go. There are only so many times your son can hurt you. It was hard on my parents, I wanted to help them, but they said "it was their problem" they "created" the monster and to let them deal with it. There's only so many time you can deal with the sound of waking up to your mom screaming because she's being attacked by your brother and only so many times you can deal with your son. My mom wanted to put him in a home, but I dad said no to the idea. He wanted to believe he could be a good father, no matter the circumstances. He said he’d never give up on Jack. My mom and dad would argue about it all the time. I remember I was getting ready to leave for practice and I heard them yelling. My mom said, “It’s not safe for anyone with him here. He can hurt us, David and himself.” My dad said “Damn it, he’s our son we will take care of him. We can do this.” “Bill, we can’t do this any longer.” “Do it for Jack.” “I can’t do this any longer.” “Find a way” “You always have to get your way, don’t you Bill?” My mom had a tear roll down her face, and she saw me in the corner. “Oh David, your dad and I were just discussing sports. Are you ready for practice? I put your Gatorade in the car already” The whole car ride we were silent. I was excited because the next day was my birthday. (Pause)

The next morning my mom came into my room really early. She had a sad look on her face. She came in with a present. She looked me in the eye and said, " David... you know I love you right?" and I said "Yes of course, I love you too" "Well, sometimes we have to do what's best for us, do you understand?" I had no idea what she meant, but I didn't want to disagree with her, so I said "Sure." She handed me my gift, it was brand new cleats. I had been asking for these cleats for years and they were super expensive. I hugged her and she kissed me on the cheek. She left crying. I had no idea why. I was very confused. But I understood later.

That was the last time I saw my mom. It was just too much for her to deal with my brother. She left. Last I heard she just moved in with a nice new man and a "better family" so that's good. Good for her .My dad held strong though. He was making good money, but he knew it was best to make sure that we were financially stable. He picked up a second job. He pulled me aside one day and said “Son, I'm going to need you to step up. I know you have a lot on your plate, but you need to be here after school to watch brother.” So I did. I didn't see friends, and I didn't do anything extracurricular, I even quit football. The one thing that made me so happy. Every day after school I'd get my brother off the bus and I'd watch him until my dad came home late at night. I did it for my dad. Family was always so important to me; I’d do anything for them.

At first it was fine; I tried really hard to teach him things. I spent the better part of one summer teaching him how to swim. Which I was able to. Then I tried a more difficult task, to teach him how to talk. I started with something simple... Jack say, I love you. He said, “Pizza.” The only words my brother would ever say were food. I mean it was only a few words he knew and he always said them wrong. I still tried. Jack say I love you. (Silence) Jack... say I love you! (Silence) Jack do you love me? Say I love you. (Silence) “Damn it Jack.” (Pause) Jack, I know somewhere in that brain of yours, you love me right? Jack, do you love me? I can’t just give up my life for you if you don’t love me back. (Jack starts crying) Jack, you don’t need to cry, I’ll get you some food. I’ll get you pizza, your favorite. (Walks over to the counter) Here Jack, here’s some left over pizza. Here you go. (He feeds Jack the pizza, Jack bites his fingers) Ouch, damn it. You don’t love me, do you? If you did you wouldn’t do this to me. Here, take your damn pizza.

It got worse. Teachers at school thought my dad was abusing me from all the bruises I had. I could have told them about Jack, but I didn’t want anyone to know. I wanted to keep strong. I didn’t want to look weak. I wanted to be strong like my dad. We took him to a specialist. It cost only 400$ an hour and all she did was give medication. Valium. If he got aggressive give him Valium. That's what she told us to do. Every time he got aggressive I gave it to him. After taking it a few times brother realized that he liked the feeling the pills gave him. Even if he was having an episode, he still would take it. He viewed it like candy. We kept it locked away, so he couldn’t get it.

When things got tough I'd try to think of the good times. Like when we were slaying dragons and conquering China, “Jack, the Lionheart and me Genghis Khan!” But it got hard... a little too hard. I know I told my dad I would be there for the family, but I began to understand why mom left. One day he came home and I was exhausted. I walked up to him. “Dad, I can’t do this anymore.” “Son I know it’s hard, but you can do this. We need this money. It’ll be fine. “I understand financial security, but Dad, what about emotional security? What about the security of your own son? Do these bruises look secure to you? How about me giving up everything, dad? How about letting mom leave?” “What did you just say to me?” “Dad, she left because of you.” “No, she left because she didn’t want to try hard enough for this family. Now go to bed. Be strong David, for the sake of this family.”

As far as I was concerned, I had no family. That's one of the reasons I loved football, I was a part of a team. I suddenly would have a family of dozens. There were hundreds of fans cheering for me. I wasn’t alone… but the cheering stopped. The football family disappeared. My real family was broken. I tried to keep strong. I pretended, like so many people do, that I was fine! I could do this! Some people do fine being alone, but not me. I guess sometimes we're not as strong as we think we are.

It was a Wednesday afternoon. I had just failed a test because I had no time to study because I was hiding from him the day before. I was in a bad mood... but so was he. He came into the house and hit me. Then he bit me. I ran off. Then he bit himself. He was screaming at the top of his lungs. I had never hit Jack. I was always good, but this was getting to be too much. I tried to remember, Jack, the Lion heart and our adventures... the good times... but then I remembered that all those good times were made up. I was tired of hiding from him. I walked to him and he hit me... and hit me... but this is what I wanted. I wanted to excuse to fight back. And I fought. I slapped him across the face. I punched him. I punched. His nose started bleeding. He kept crying.

"Jack, do you think it’s fun? Having to be hit all the time. You keep hitting your own damn brother. I know you don't understand, but damn it I'm your brother, doesn't that mean anything to you? No of course it doesn't. I gave up everything, my friends, football and this is what I get in return? A house with no mom, and no father who is there. It's all because of you!" I walked over and got the Valium... I looked at it. I mean... if this could calm him down for a little while, why not a long time? Why not forever? No more fear of being hit by him. I gave him one dose. My brother at least understood that the medication would make him feel better, so he always took it willingly. I gave him a second dose... and third... and fourth... The rest of the bottle. My brother relaxed and walked to another room.

After my brother got violent he would always do this one thing; the one thing my brother would do that would convince me that he had some emotion was after he would get aggressive he would come over and try to apologize. Obviously he wouldn't say anything, but he'd hold your hand as if he knew he did a bad thing. He walked over to me and held my hand. I just sobbed. "I'm sorry Jack... I love you" and for the first time ever he said.

Jack: I love you.

David: Those were the last words he ever said. In that moment, I looked into his eyes. In that moment I realized, that all Jack wanted was what we all wanted. To be understood. He couldn't communicate like the rest of us. That made him angry. He just wanted to understand what was going on. In that moment, I realized I was a horrible brother.

When the cops came I told them that I had given him one dose and I forgot to close the lid. I told them I had taken a nap. And during that nap he must have taken the rest. I explained how when he didn't feel well he would take the pills because he knew it would make him feel better. He just must have taken too much, not knowing what it would do to him. Now normally I'd probably get in a lot of trouble for something like this or at least questioned, but because he was so disabled, they didn't really care. Authority figures tend to ignore the "weird" ones.

No one really knows what happens. Not even my dad. I thought my brother was a monster. But really who is the monster? Maybe, I'm just like my mom, doing what's best for me. Or maybe I’m like my dad and I’ll ignore when people hurt, when I hurt. I haven’t talked to either of them in a while. We all just kind have kept our distance since the incident. I'm living my own life now. I made it onto my college football team. It looks like I'll start varsity next year. Although in the end, I don't know if it really matters. I personally think, we only have hobbies to distract us from what hurts.

If I told people this, they wouldn't believe me. Everyone thinks I'm such a happy person. That's the problem with happy people; no one really knows what they're hiding inside. Ever notice how comedians, always seem to have the most depressing lives? I think it's the same for people who smile a lot. We just all have different ways of coping. I'll keep smiling, so no one knows about Jack. This is why I hate small talk. No one ever really wants to know the true answer. They just want words to drown out the silence, so when people ask about my family. It's just a lot easier to lie. I tell them that, I am an only child. That way, they'll have to never know about Jack, the Lionheart. (Looks to the sky) Jack, I hope the weather is good up there.

END OF PLAY
```

---

## IC-0057: Living in Color

- Title: Living in Color
- Author (byline): Andrew Messer & Jake Nyberg
- Work: Living in Color
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1399
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
Alex: Have you ever seen what an actor looks like onstage, under the bright spotlights, without any makeup? Every flaw, every imperfection, every splotch of color on their face is highlighted. When you put makeup on, you cover those up. I mean, you can use the light to create shadow, and colors to illustrate...you’re telling a story. I like makeup. It’s a new story each time. Sometimes, though, you’re just writing the final pages of a story someone else has been writing. But the process is the same, you know. Doing makeup on the dead is just like doing makeup on actors.

It’s difficult to find someone that’s never been to a funeral. Funerals are constant reminders of our own mortality, yet we try extremely hard to make the dead seem alive. We put pressed suits and fresh dresses on our loved ones, and if you’ve ever looked closely, their hair is combed, and their face is placid, and covered with gentle layer of makeup. Everybody dies, but not everybody lives.

Living In Color

by Andrew Messer and Jake Nyberg

Doing makeup on the dead is not that different from doing makeup on actors, except the dead usually complain less. (chuckles, starts applying makeup, and this continues) Of course, I didn’t start out just doing makeup. I wanted to be an actor, you know? I was going to give it a shot. But that ship sailed, and sunk. I love makeup, you know? I really do. I just never thought I’d end up working back in the same little town I grew up in. But, I needed work, and the mortuary needed help.

It took me about a month to get over the whole dead-body-makeup thing, but once I got comfortable with that, it was easy. Use colors, shades, create a look. Create a performance. That’s what I love, the performance.

My first performance was in “West Side Story.” It was my junior year of high school. After my audition, the director stopped me, said he really enjoyed my audition, and asked why I had never been there earlier. I laughed and made some excuse about being a late bloomer or something. The truth was, I hadn’t had the courage.

Oh, it wasn’t stage fright. See, the theatre season and the football season conflicted. Performing in a play meant not performing on the field, and that was unacceptable to my father. Auditioning for a play meant working up the courage to tell my father that I didn’t want to play football anymore. (quickly) So, I did that, I auditioned, and I won a decent role. I loved performing. I mean, first it was “West Side,” then there was “Fame” and then I landed a role in “Our Town.” I loved every minute of stage time, and every performance. And I had always liked doing my own makeup. (pauses)

The families are asked to provide a photo and, if they desire, some general directions for me to work from. Most of the photos are from years ago…ages ago—their wedding, the birth of their children, or a birthday, perhaps, their happiest days. (looks at a tag) Doris Carlson. (shows her photo) See? Her wedding. A beautiful dress, and a beautiful smile. (reads) “Please capture the radiance of her smile.” Of course, it’s been sixty years. Her teeth are gone and her eyes will be closed…but...

After my final two years of high school, I was sold on theatre. I wanted to go to college, and I was going to be a theatre major. My father wasn’t happy with that. He believed I had already ruined my chances of a football scholarship, and he never let me forget it. And there was no way that he was going to let me give up the last remaining slivers of hope on college football by pursuing theatre.

“You’re not going.”

It was never a question, it was always a statement. If I wasn’t going to play football, I wasn’t going to go to college. But he couldn’t control that. I applied, and I was accepted.

“I’m not going to pay for it. You’re on your own.”

I knew that. That assumption had been made. So, I went off to college, declared my major right from the start, and worked my ass off to pay for the tuition, the books, and fees for costumes, scripts, auditions, and…makeup. But I was doing it. I kept in touch with the folks. Usually when I called, it was my mother who picked up,and I never even spoke to my father. When he picked up the phone, he went and got my mother. (sardonically laughs) Obviously, my mother and I grew closer during those years. She even made it to a few of the big performances I had at the college. I always had the glimmer of hope that he might come along. He never did.

In fact, in my last year there, I had the lead role in “All My Sons.” My mother was ecstatic, and she came to the opening performance. I kept thinking he’d show. I mean, it was my last college show. I kept thinking he’d surprise me, just once. (sardonic, again) Of course, he stayed true to form, and stayed home. Of all the years, and all the performances he refused to come to, that one hurt the most…but that night, there was someone else in the audience. An talent agent. He was waiting for me outside the stage door after the show. He was a real agent, and he was from New York. He told me that if I ever ended up in the Big Apple, I should call him. I could see it. My name in lights. “Starring Alex McMahon!”

(looking down at body) Hmm, something’s not right here. (snaps fingers softly) It’s the blush. The blush is a little…off. (adjusts blush) I swear, it’s the blush that does it. Everything else sort of relies on the blush. It’s the last little addition, but at the same time, it’s the largest component.

Two months after I graduated, I made the big move. I called the agent, and he agreed to try and find me some auditions. As the months went by, I had a few auditions, but nothing major. I wasn’t earning much--I was mostly doing clerical grunt work—and I had a hard time staying ahead of the bills. Then, about a year after I moved out there, I started making callbacks. I had a few callbacks, and then I had a few callbacks…and then I had a few callbacks.

I never made it. I never could make the cut and land a role. And then, I was broke. I had no options. I was evicted, and I didn’t have any long-term work possibilities, so, I came back here. Back home. The first thing I had to do was ask my parents for a loan, and then the past came rushing back, with all the things that had been left unsaid for years.

“What happened?”

‘I don’t know, Dad, I guess New York happened.”

“Oh, and you couldn’t take it. I’ve known it for years, but your mother and you were so content to see you go off and try and find whatever it was you thought that acting had for you. But I could have told you years ago that you were wasting your time. But no, you wanted to go off and be one of those theater faggots!”

(Alex is silent)

That was it. The money changed hands and I found a cheap apartment, and we never spoke after that. Then I found a good job here at the mortuary, and those skills that I had developed backstage for years came in handy. (smiles slightly) My mother and I still speak every once in a while. She calls. In fact, just yesterday, and she still doesn’t know I work here, and after everything…I prefer it that way.

Sometimes, all we have to work with is the photo. Usually, I don’t even meet any of the family. The mortician himself usually deals with the family and the funeral details. All I get is the photo, maybe the short request on the back. There’s never any story. (picks up photo, shows photo) Jack McMahon. It’s a photo of him holding his infant son. (looks at the back of photo)

“Please, make my husband look this proud.”

I can do it, Dad. I can make you look that proud. But you still have one final performance. (looks down) You look good, Dad. You look damn good.
```

---

## IC-0058: Mother’s Day

- Title: Mother’s Day
- Author (byline): A.J.J. Bourque
- Work: Mother’s Day
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1251
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
Based on true events

If you listen really closely you can almost hear the ocean when you breathe in and out. Sometimes when it’s quiet, and I’m alone, I think about my grandparents’ house near the beach, and the summers I spent there as a kid. I haven’t been back since I was sixteen. A lot can change in a few short years.

It’s four o’clock. Ellen’s on TV. Mom’s drifting in and out of consciousness, but a part of her mind must know she’s on. The steady cadence of her heart monitors slows with every joke, rolling like the tide: in . . . and out . . . .

I’ve been picking up extra shifts at the paint store. Four hundred dollars. All I need is four hundred dollars and this all goes away.

This was never the plan. Not at nineteen. Not now . . . Now, at the absolute worst moment of all; now when Mom needs me most . . . when I need her.

But . . . I can’t involve her. Not with this. She’s got enough to think about already.

So, I don’t tell Mom. She doesn’t need to know. No one needs to know. Just four hundred dollars. I can do this. I can get through this.

You know, she asked me about it once. We were doing laundry, and she was watching me out of the corner of her eye, and then she turned to me, and said, “Leah, honey . . . are you pregnant?”

And what was I going to say? I mean, how many times has she said, “Just look at that, girls: another teen mom-to-be. Don’t they know they’re throwing their lives away? It’s a shame. Just a real shame.”

So I lied. “No, ma’am,” I said, and we haven’t spoken of it again. Because there’s nothing to say. In a few weeks, there won’t be anything left to say.

But . . .

But then I think about how it happened, and I’m mortified. You know, he tried to put this all on me. Can you believe that? He said that it “wasn’t his problem,” and that I was “manipulating him.” As if I would choose this at nineteen. As if I could make it happen all by myself. But no . . . of the two of us, he chose. He wanted this, and I . . . I just tried to think about the ocean, and the beach, and just . . . breathe.

I waited until two months after to take the test. I figured . . . I mean, I couldn’t tell— If I had said something then— If I had gone to the hospital, or called the police, or told someone right then . . . it would have made it all real. Every bit of it. And I can’t let it be real. Because, you know, I always thought it had to be a stranger to do this to a woman. I never thought it could be a “friend.”

But that’s fine. It’s fine. You know, I’ve got it under control. I’m fine, I’ll just take care of it, and that’ll be that, and we just won’t speak of it. So I’ve been picking up extra shifts? So what? That is perfectly normal, thank you very much. I mean, I’m a teenager. I need stuff. That’s not so unusual, right? I mean— Just four hundred dollars, I— I can have that in a few weeks, I— No, it’s fine. I’m okay. I’m calm. I’m fine. Really.

But . . .

You see, the thing that nobody ever tells you about certain “problems” is that the farther along— I mean— you know, the longer you wait, the more expensive it is. So . . .

by the time I was going to have the money, more weeks had passed, and the price had gone up. It’s almost funny. I guess you can put a price on—

But, you know, that’s fine, it’s . . . It’s not the end of the world, I— I’ll be okay. I can get through this, I can . . . I’ll be . . .

Hey, you know, Mom— Mom has been, you know, she’s getting stronger, and her tests look good, and she’s, she’s pulling right along, just— just watching funny movies, and playing with the dogs, and . . . and being a Mom to Megan and I.

So, that’s good. That’s good news. That’s something to celebrate, but, you know . . . for me— for both of us—time keeps on ticking, and . . .

Sometimes, when I’m alone, and the steady beat of Mom’s monitors tells me she’s asleep, I go into my room, close my eyes, ball up my fist and . . . I just close my eyes, make a fist and . . . And then I stop, and I wait, listening for any sound in the hall, any sign that I’m not alone, that someone is watching over me, that someone might find out.

Megan’s at work, or out with her friends, and Dad got out long before this became his problem. It’s just the four of us tonight: Mom and her monitors, and me and my problem.

I hate you. I. Hate. You. I hate you for putting me through this. I hate you, who chose this, and I hate you for doing this to me now. And I hate . . . myself . . . for not doing anything about it. Well, there is plenty I can do about it. I can just go to the medicine cabinet right now and I can do something about it, I can— Is that Megan? Is she outside the door?

“Just a minute!”

No answer. Good. Nobody has to see. If I hide the marks under my clothes, then nobody has to see. Oh, they can check my wrists all they want. They won’t find anything there. But my hips?

N—No, I can’t. I can’t do this. I— no. NO.

I’ll just . . . I’ll just breathe. And I’ll— you know, I’ll just take it one day at a time, and I’ll just make a little trip out of town when it’s time. Just another hospital in another town, and no one needs to know. Just breathe.

You know, between working and being there for Mom, time gets away from me. Days turn to weeks, and weeks into months. Mom grows thinner, and I . . . I mean it’s perfectly normal for a girl my age to wear, you know, baggy clothes all the time. I mean, who doesn’t love a hoodie three sizes too big? It makes you feel safe, you know? Like wearing this big, squishy armor. Like having these arms wrapped around you. And anyway, this isn’t about me. Okay? It’s about Mom. It’s about getting Mom well again, about getting her what she needs, and—

And time is getting small now. Any day now I’m going to make that trip to the hospital, and that will be it.

Mom’s going downhill fast, but she’s alert enough to ask me again, all slow and coherent, “Leah . . . are you pregnant?”

“No, ma’am.”

“You know you could tell me if you were, honey. We’d get through it together.”

“. . . No ma’am.”

The day arrives. I’m climbing in my truck by seven. I’m at the hospital by eight, and by noon . . . by noon a perfect little miracle has happened . . . for someone else’s family.

I am trembling, and raw, but I can’t stay here. I can’t afford to waste any amount of time feeling sorry for myself, because my mother needs me, and if I don’t get out of here right now and go to her . . . No, it’s fine. I’m fine. I’ll just take deep breaths . . . and think of the ocean. Just one breath after another . . . and think of the ocean.
```

---

## IC-0059: Not specified

- Title: Not specified
- Author (byline): Not specified
- Work: Not specified
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1044
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
“My Perfect Feet”

Andy Hobin

(A horribly disfigured man enters and slowly addresses the audience.)

ROBERT

I was sitting in my squad car at a red light when an intoxicated motorist rear-ended me at 40 miles an hour, and my car went up in flames. I was stuck inside that steel fireball for two minutes. Count that. One… two… three… I survived that. My body was covered with third and fourth degree burn. Fourth. When I was a Boy Scout, I was taught that there were only three degrees of burns. Fourth – apparently subject matter too troubling for a young boy’s mind to have to contemplate. I survived that. Lucky me.

(He contemplatively massages his shoulder.)

I endured over

everything thirty hours of surgery that first week. Surgery on . You see these two fingers? These two finger were actually fused together before a doctor had them surgically separated. People hear about something like my fingers and they usually ask me something along the lines of, “Did it hurt when your fingers were stuck together?” To which I would respond, “…No. Actually,

(He chuckles.) it helped me swim a little faster. I always try to tell a joke. Makes people feel more comfortable when they talk to me. That’s the same reason I tell them about my feet.

(He smiles broadly.)

My feet were completely untouched by the flames. They’re perfect. They’re actually part of the reason I’m here. See, a couple of weeks after the accident they finally let my wife, Maura, in to see me. And I was wrapped head to toe in bandages, I couldn’t speak, I was just… there. And Maura’s making small talk and I hear her getting closer to the bed as she’s speaking… and then she stops and for a second all there is is just the blip… blip… blip… of the heart monitor. And suddenly she kneeling and weeping and clutching my feet. She just kept saying “I love you. I love you. I love you so much…” I felt her tears on my bare feet like… like she was washing my feet. And I knew right then that I was going to get through this. And I was going to do it for her. Well.

Three months and multiple, multiple surgeries later, I come home, and everyone’s calling me a “hero!” And an “inspiration!”

And I’m thinking to myself, hot damn! You know? I mean, I didn’t go to college, I didn’t vote in the last election, hell, this one time back in the day, some guy was talking shit about a girl I was running around with, so I slipped a bunch of Visine in his

potent beer. Visine has a chemical in it that is an extremely laxative. And I’m the “inspiration!” You see, it’s still me. Still the same old Robert, oh that crazy friggin’ Robert… Still me. I’m just trapped under this layer of scars. Still me, but I can understand why Kelly, my five year old daughter, acted… the way that she did.

We tried to prepare her for me the best would could, Maura and me, really we did. But I don’t know what hurt worse: her crying and crying and crying, or that look on her face like she could not believe that it was me under that skin. Like she didn’t even recognize me. That first day she hid herself away, and I felt bad for her, you know? So I let her hide. Figured she’s come out when she was ready. Well, three days later and still no contact from my little girl, I had had enough. So that night after Maura put her to bed, I went into her room and sat down in the dark, and I said, “Kelly, honey, are you still afraid of me? And she said, “Just don’t turn the light on, Daddy.” It was okay to talk

good just as long as we left the light off. I just… it felt so to be able to hear about her day, what she did at recess, what she had for lunch, all that little stuff. But I still felt like I was on the outside looking in. Like I was looking through glass. Look, but don’t touch. That’s what really got to me.

And Maura. One night in bed, I reached over and put my hand on her back, and she jumped when I touched her. She just smiled and said that I surprised her, but I couldn’t help but wonder if was

(He regards his hand.) the sheer element of surprise itself, or the feeling of my rough, coarse skin against her bare back. And how do you know?!

This went on. Talking to my daughter in the dark, never knowing if my wife is repulsed by my touch, and one day I woke, went into the bathroom, looked in the mirror and realized that this is it. For the rest of my life, people will be polite when they speak to me and stare as I walk away, and I can rehabilitate my body, but never my place in the world. There were the pills, right there in the medicine cabinet, but I couldn’t do it. Not yet. So I go down to the kitchen to get a drink and as I’m

(He pulls a opening the refrigerator, something catches my eye. small remote from his pocket, aims it into the audience, and gives it a click. A simple crayon drawing of a mother, father, and daughter is projected over the wall.)

It was this picture, with yesterday’s date on it. Mommy, Kelly… and Daddy. Look at me. I’m just Daddy again. No scars, nothing. And suddenly Kelly’s standing there, I didn’t see her come in, and she says, “Do you like it, Daddy?” I can hardly speak. I say, “Yes honey, very much, it’s very beautiful.” And she smiles and walks out of the kitchen. That was the first time since coming home that my daughter has spoken to me outside of her dark room. I looked at that picture and I knew right then that my baby girl loved me. And I looked down at my feet - my beautiful, beautiful bare feet – and I remembered feeling my wife’s tears, and I knew that we

kept are not only put here on this earth, but here for a purpose. People still stare. I mean, that’s the inevitable. But you… you. You talk to me. You look past the scars and you learn my purpose. I have my life because I have my love. And I am so very alive. I am alive.
```

---

## IC-0060: Remember One Word

- Title: Remember One Word
- Author (byline): Tammie Peters
- Work: Remember One Word
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1597
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
Tammie Peters

You are my lawyer, no? You will help me stay in America.

Yes, it has been a very long journey. But I had no other choice.

You want to know my story? My cousin told me to say “asylum.” It is supposed to be a magic word. Asylum. You know?

Okay. I am Inez. I grew up in Honduras, in San Pedro Sula. Do you know it? It is a very bad place. I could not stay any longer or I would die. The maras would get me.

We did not always worry about the maras. Mi familia had a small home — it was very nice, it even had a real floor, not dirt like our neighbors. My mama was beautiful and she found lovely pieces of cloth to hang on the plain walls to make the rooms pretty.She would sing to us with the voice of an angel. My papa was strong and he worked for the factory. He was tall and had a very bushy mustache that would tickle me when he carried me. And he had a beautiful booming voice that sounded like thunder in a rainstorm. And there were two of us children: me and my older brother, Tomas. We lived happily together in our little home. I had a sweet little doll, who was all mine.

But then the troubles began when I turned 10.

My papa became angry at the government. He would talk about how bad President Sosa was for the country. He would complain about how weak the government had become. He would come home from work and tell us about bribes he saw officials take. He saw the military chafarote beat a man on the streets until he passed out. Papa was furious and he wanted to change things. He wanted to organize the workers, maybe call a strike. Mama begged him not to do anything. The next day, Antonio, a neighbor who worked with papa, ran into our home, gasping, “He’s dead. Your husband was yelling about corruption and the chafarote shot him.”

Oh, papa!

That left mama alone with the two of us. Mama had to find work. There weren’t many choices; she went to the maquila to make panties. Mama didn’t sing much after that. Her job didn’t pay very much, but when she worked we ate pretty well. When there was no work for her, Tomas and I went “hunting.” Sometimes, we got food from the church — Americanos would sent us arroz, powdered milk, frijoles. That’s when I learned about how kind the Americanos are. Sometimes we could get stale bread from the bakery. There were times when there was no food — so we’d make up games to keep our minds off of our hunger.

One of my favorite games was to pretend to be explorers and search for treasure amid the garbage. Sometimes we would find small shiny objects that had once been parts of a lamp or a bit of broken jewelry, and Tomas would make things for me and Mama. He wanted to dress her up like a princess, he said. He wanted her to feel special. So he would find little bits of wire and abandoned beads or broken bits of glass and then create wonderful little pieces of art: necklaces, earrings, pins . . . he was very talented. We knew that one day he would become a famous jewelry make or an artist with a gallery. Mama always showed the neighborhood women Tomas’s newest works. That’s how he cut his hand once. He was rummaging through some trash and the lid of a tin can cut his hand: a semi-circle just where the thumb connects. It wasn’t deep -- we were able to stop the bleeding quickly. But the scar: a perfect half-circle. Tomas called it his smile -- his hand always smiled at him and at the world. He was like that.

Tomas was 13 at the time. He wanted to work--to provide money for mama--, but there were no real jobs for such a young boy, unless he joined the maras, the gangs.

There were two maras in our area: Mara Salvatrucha and Calle dieciocho. You may have heard of them as MS13 and 18th Street. They were very bad. They moved cocaine through our city, and they bought and sold girls. They would threaten shop owners with beatings if the shop owners didn’t pay them part of the money they made. Sometimes, they would kill shop owners. They would pull girls out of their homes and rape them in the streets. Sometimes they would do that to the mothers. . . Or the grandmothers. They were constantly at war. We never went out after dark. Every night, after sundown, we all heard the gunfire. Sometimes, in the morning we would find new bullet marks in the side of our little house.

We all knew the stories of what happened to boys who wouldn’t join them. They might be tortured with dripping battery acid, or they might have several bones broken. Or. . . something.

Tomas didn’t want to join a gang. He hated what they did. He hated the violence. He wanted to work to earn money. He wanted to create beautiful things.

Both gangs pressured him. One day, he even spit on the boy who delivered the message. That was a huge mistake. That night, Tomas did not come home after the sun set. We waited all night, and worried about him. Mama held the bits of jewelry he created in her hands, caressing them like small totems, using them as a rosary to pray to the saints. But he never came in the door. I tried to sleep, but it was too hard -- Tomas and I had shared a bed forever. How could I sleep without his protective arm around me?

The next morning, we gingerly opened the door and found a basket with a top on it, sitting outside. It was a big basket, like for laundry -- but it wasn’t ours. I picked up the lid, and in the basket were body parts: hands, arms, feet, and the like, all neatly cut apart and put in the basket. On one hand I saw the smiling scar from Tomas’s run-in with the tin can.

Mama called to me: “Inez, what do you see?”

How could I describe this to her? How could I tell her about the basket and the hand. As it was, I didn’t have to. She pushed past me to look for herself.

Mama collapsed onto her knees. “Dios mio! My Tomas! My baby! What have you done?” She got sick and tried to throw up. She fell to the ground, sobbing. I put the lid back on the basket and held her as hard as my small body could. She was shaking. There was nothing more I could do, so I just held her and cried with her.

But then I heard another sound: boys playing futbol. It seemed so wrong — how could they be playing while we mourned my brother? It was too early in the morning--no neighbors were up getting water, no men were on their way to work. The street was supposed to be quiet, but these boys were playing a game! They were having fun while mi hermano, my dear brother was here, torn apart in that grisly basket. Couldn’t he get a little respect? Couldn’t we have a few minutes to mourn before confronting the world? I wanted to scream, “STOP PLAYING! THIS IS NO TIME TO HAVE FUN! DON’T YOU UNDERSTAND?! MY BROTHER IS GONE AND THERE IS NO JOY IN THE WORLD. GO HOME!” But the words wouldn’t form and no sound came through the terrible lump in my throat.

I looked up--trying to find my voice, trying to show them the pathetic hatred in my eyes--and took a few moments to focus. I recognized some younger gang members. They were laughing and calling to each other. But something was not right, something was out of place. As my brain continued to focus on the boys, my horror grew and grew: they were playing futbol with something that wasn’t a ball. It was oddly shaped. The colors were wrong. It was the cabeza, the head of Tomas! They were kicking around my brother’s head!

At that point, I passed out.

That day, my mama was determined to have me leave San Pedro Sula as soon as I could. Why? Por que the gangs would come after me next. If I were lucky, I would be a messenger or courier. But more likely, I would be one of “their” girls, to be raped whenever they wanted. Or I would be sold to someone who would use me for the same purpose. There are very few jobs for girls. If I refused, I would end up like Tomas. Even if I agreed, I might still end up dead, the sister of Tomas who spit on one of them. What kind of life would that be? No life. If I go home, I will be raped or killed -- it is that simple.

Mama has a cousin living in Houston; his name is Hector Chacon. He can take me in and give me a place to stay. Mama wrote to him so he knows am coming. He told me to say the word “asylum” to the Americans if I got here. Please don’t make me go back. Please let me stay. If you send me to Honduras, I will surely die. Won’t you help me?
```

---

## IC-0061: Revolution

- Title: Revolution
- Author (byline): Steve DuBois
- Work: Revolution
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1490
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
[ARNOLD kneels at stage center, clad in a tattered wool overcoat, well-worn leather boots, and a cloth cap; his hands are wrapped in rags to ward off the cold. Beside him is a flintlock musket and a large canvas pack, the contents of which—salt pork, a jar of flour, a canteen, minie balls and gunpowder cartridges, flint and tinder, change of clothes—are scattered around him. As the lights come up, he glances up in surprise.]

Well! This is…different.

You’ll excuse my disheveled appearance, I hope. Not what one would expect of a prosperous New Haven trader, let alone a general of the colonial army. Nor is a snowbound wilderness trail an ideal location to receive guests. But then, I seldom have visitors. It’s been a long while—centuries, in fact--since anyone has cared to keep company with the likes of me.

It was different once. Once, they called me a hero of the revolution.

Heh…“Revolution”. Take a long look at that word; a good general examines the ground before entering into battle. The enemy has set a trap for you--do you see it? You’re taught to think of revolutions in terms of progress, in terms of steady movement forwards. Ah, but…

[He traces a circle in the air]

…revolution. The movement isn’t progressive, it’s circular. It revolves. Like the wheel of a cart or the head of a screw. Destiny’s coin, flipping in midair. Turning, turning. The wheel turns, but in the end, it always comes back to the same place.

[Intro here.]

It’s freezing out here. Let’s see if I can at least get a fire going.

[As he speaks, he limps around his camp, gathering materials together and attempting to start a fire. He is active and energetic, almost to the point of being spastic at times, though he winces every time he puts weight on his left leg.]

All the contents of my soldier’s pack, scattered here in the snow. Not my nature to be so disorganized. Whatever you think of me, know I did nothing without a reason. The revolution —well, no man can say we weren’t provoked. Imagine it: to sail your vessel to the West Indies with a cargo purchased on credit, never seeing your Peggy or your sons for months at a time, with your entire fortune bound up in the hold, knowing that the slightest mishap would reduce your family to destitution. To slip safely into port: you’ve done it. Your skills and your nerve have been the making of you. The profits await.

And there stands the man, in his finery, with a smirk on his face, and a stamp in his hand. This man waits to assess the value of your goods, and to take the tenth part of it for himself, and for his King.

Sibi totique, that was my motto in trade. “For myself and for all.” For all--of course! I was ever-eager to serve! But there’s a contract in it, do you see? An equal exchange! This man with the stamp, with his smooth, uncallused hands—what has he risked? Was it any wonder that we rose in revolution?

And was it any wonder that I was in the vanguard? Oh, don’t think I don’t know what you’ve made of your legendary “founding fathers”. That’s my fate, you see. To know everything that occurs in the nation I midwived into existence. Franklin, the icon of enlightenment and reason. Washington, the living god. Hamilton, the… rap musician? I can’t make heads or tails of that one.

But while they were bickering and jabbering in Philadelphia, I took action. In the fall of ’75, I embarked on my most ambitious enterprise. A midwinter invasion of Canada! The sheer audacity of it! And it almost worked! If it hadn’t been for a freak storm, we would have beaten the British forces to the capital of Quebec. The whole continent in American hands! The flip of history’s coin. How different things might have been.

Instead—trapped outside the walls. Smallpox running rampant, no provisions or hope of reinforcement. Shot twice through the leg and sent packing back to the south, fighting off the British at every turn. Blood in the snow—my own, and that of my brave boys. A month earlier Congress had called me the “American Hannibal”; now, they condemned me as a “glory-hunter.”

And then came the letter from home. Peggy, whom I’d abandoned on all those trading voyages. Peggy, whom I’d left behind as I marched off in search of liberty and glory. She was gone. A sudden fever. My sons, motherless.

So be it. Sibi totique. In war, we must all endure losses. My sons I left in the care of my sister. I accepted Congress’ scorn, accepted their assignment as a subordinate to that flatulent, indolent imbecile, Gates, at Saratoga. And while he sat in his tent, talking politics with a captured British officer, we broke the British lines! Charging the redoubts on horseback, at the head of my troops, straight forward into the cannonfire! A British officer would later say that there “seemed to shoot out from me a magnetic flame that electrified my men and made heroes of all within the sphere of my influence.”

Truth was, I was blasted out of my mind on rum. We all were. Somebody brought a barrel into camp…but no matter! We crushed them utterly and brought the French into the war on the side of the Colonies. We won the war that day! Every ounce of the liberty you enjoy, you owe to me, and to those brave boys! Those brave, drunk boys!

But I never saw the victory. A volley of musket fire brought down my horse—right on top of this same damned leg, can you believe it? Shattered it, like ice under a hammer. Those butchers in the medical tent left it two inches shorter than the other. Every step, forevermore, a jolt of agony. Every stride a new, fresh hell.

I wrote to Congress. My neglected business was a ruin, my debts astronomical. My sister and my sons shivered in a stripped house, unable to afford so much as a cord of firewood! And those worms in Philadelphia would not authorize a cent to reimburse me! They said my charge —the charge that won America’s liberty--had been “unauthorized”! Instead they awarded a gold medal to General Gates, “the hero of Saratoga.”

What would you do? I had sacrificed everything! My fortune! My family! My goddamned LEG, for Christ’s sake! I had made myself a cripple in the service of my country! And yet I had been undermined at every turn by men who never lifted a musket, by those schemers and speechifiers, those slave-holding “champions of liberty”!

Sibi totique! For others, AND for myself! I had spent too much time at the bottom of the wheel, being ground beneath it. It was time for things to turn!

So…yes. Yes, I did it. I…changed sides. I sold the British the plans for the defense of West Point.

I sold them all. All those boys, who bled and died at my command—I sold their sacrifice. All the men who’d praised my courage, and defended my honor in the corridors of power— Schuyler, Washington--I sold their faith in me, and made them look like fools. My honor, the respect of my countrymen, my eternal reputation—I sold it all. From trader, to soldier, to trader again—round and round goes the wheel.

I provided for my family. I turned my back on all I had loved. I went into exile and into infamy. And I went to my deathbed expecting hell. Instead…

[Arnold gestures broadly at his surroundings.]

...I woke up here.

And perhaps this is hell. Because every morning I wake up on this trail, in the freezing cold, and I hoist my burden, and I limp onwards. Just as my boys did in the winter of ’75. I am fated to know all that occurs in the nation I left behind. But of my own ultimate destination I have no idea. I know only that my march will continue, day after day, century after century, so long as America endures. Every morning, I will awaken on this trail, to find the wheel has come around to the same place again. A never-ending revolution. An eternal reminder that no man may escape the circle of his own character.

I deserve this. I don’t deny it. But it’s not all I deserve.

You’ll tell them, won’t you? Take my story back with you. The whole story. I was a traitor, yes. But that’s not all I was.

A pleasant diversion, this. And now, if you’ll excuse me…

[Arnold shrugs the pack onto his shoulders, then turns his back.]

…I have a long walk ahead.

[He limps away.]
```

---

## IC-0062: Sister of Mercy

- Title: Sister of Mercy
- Author (byline): Clyde Hendrickson
- Work: Sister of Mercy
- Publisher: Mushroom Cloud Press
- Publication date as stated: 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2237
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
[A teenage girl. She sits at a table with a few items on it, in a blank room.]

This is the bronze star the Army gave my brother for bravery. It was awarded to him posthumously, for actions above and beyond the call of duty. “Posthumously,” in case you didn’t know, means “after his death.” I’m not sure if the Army considers dying above and beyond the call of duty. [joking] Seems more like a dereliction of duty to me.

Some people seem to think that I should be angry that the army gave my dead brother a medal for bravery. Like, it doesn’t make up for his death. Not even close. But I think you should get a medal for bravery. Being brave is hard, and not many of us are up to the task. What my brother did, maybe it was heroic, maybe it was stupid, but it was definitely brave. And it inspired me. I’ve never been that brave. Not to sound like a douche, but, maybe if some of us were as brave as he was, he wouldn’t have needed to go over there in the first place.

Bravery is what got me here, telling you the story. Well, the telling ain’t brave. It’s stupid. But what I did, was brave. Brave the way my brother was. Or maybe brave like the terrorist who shot my brother was.

I wasn’t thinking about bravery at my brother’s funeral. I was thinking about the story my parents loved to tell about him, when he was three. This was before I was born. He was having his first piece of fried chicken ever, that my dad had cut up for him. He ate it, chewed it up slowly, and then spit it out. “Tastes like mommy’s shoes!” He said. And both my parents laughed, it was a silly thing to say. But my mom stopped laughing. She was thinking, that morning, she hadn’t been able to find her favorite sandals. It was the second pair that had gone missing recently and she was pretty mad. She said, “Honey, do you eat mommy’s shoes?” And my brother just giggled like crazy. My dad just looked confused. Then they went to my brother’s room, and looked under his pile of stuffed animals. And there were the shoes, chewed on like my brother was a Labrador puppy or something! They tried to get mad at him but they just laughed and laughed. My brother still won’t eat fried chicken, and my mom still keeps her shoes on the top shelf of her closet, though there’s no proof my brother’s habit continued.

That was basically the only good story I ever heard about him as a baby. I wonder if my parents will talk to me more about him now. Or will we never speak of him again? So far, I can’t tell.

It was my dad who started crying first, at the funeral. None of us are criers. We’re all real believers in Christ, you know, and we have this natural, Jesus-kind-of happiness that comes over us as soon as one of us gets sad. If something bad happens, we know God had a reason. When my brother died, we knew he was with the lord. On the way to the funeral, we sang a song my brother loved, an oldie, “Who wrote the book of Love,” that song always made him cheer right up. My dad was singing the loudest. So it took a lot to get my dad to start crying.

It took a band of protesters showing up at my brother’s funeral to make my dad cry. To be specific. It was when one of them shouted into a megaphone, “Your son died because you love fags!” And then the priest was praying and we got “America is paying for its sins.” By the time they started singing “Lords gonna burn these fags in hell” I was crying too, but out of rage. I violently sneezed, I was physically ill.

Apparently, Pastor Melville and his extended family do this at funerals of soldiers across the country. They think the whole country’s being punished for its sins. Even the families that are good Christians, like mine, and even for all the good things we do. Pastor Melville thinks we’re evil, and weak. He doesn’t know about our bravery.

I actually started shouting at them. I was shouting for them to go away, I interrupted the pastor’s prayer. I was so mad. My dad grabbed me but I broke free, I stormed towards the Melvilles, I was screaming at them. And they were laughing at me. One of them was singing, they were all smiling. “Look at the little demon get mad. Back to hell, Demon, with your faggot-loving brother!” That’s what Pastor Melville said to me. My brother’s Army friends picked me up and carried me away.

You might be wondering why I’m telling you all this from a jail cell. Well, that’s the point of this story. That’s where it’s headed.

The rage that got in me when I saw those protestors didn’t leave. Night after night it haunted me. I did not mourn for my brother, I did not help my parents, I did not go back to school. I was consumed by rage. I had to do something.

In high school, we read Dante’s Inferno. It’s pretty intense, it led to a couple nightmares of being frozen in ice for all eternity. I remember always this one part, where Dante meets someone in hell he knows is still alive. And he tells Dante that sometimes, people are so bad, devils come and take them to hell, and replace them on earth with a monster, before they die. After I first thought of killing those people, Pastor Melville, and his family, I couldn’t stop. It tortured me, that memory, and the memory of my dad crying, and the idea that maybe they were right, maybe my brother was in hell. And I could only think of revenge and death. I think I might have gone to hell at that very moment when I decided to kill one of them. Ever since, I’ve just been half-demon. I’m condemned, definitely. If you went to hell now, I would already be there.

It was easy to track down Pastor Melville and his family online. They preach out of their compound in Tennessee. They live there. And god bless this country, it was so easy to buy a gun. The gun show dealer was so proud of me for being a woman standing up for my rights.

I got to the Melville compound in the early evening. I knew they were leaving for a protest. They put it in on their blog. I saw them leave, in two vans, windows open. They were singing hymns. Piled in the back of the last vans were their signs. “United States of Faggots” I read. They were gone. The sun set. I went in the house, to see what I could do. I had my gun, and a can of gasoline. I figured I’d just burn it to the ground. The gun was for my protection.

I was on the second floor when I heard something. A cough. One of them was still home. The adrenaline rush was indescribable. I was so excited. I knew I was going to kill whoever I found, man, woman or child. It was a teenage boy, actually. About my age. I came in the room. I wish I could say I found him praying, but he was just sitting there, looking out the window, blowing his nose. Like a real person.

If you’re wondering, he did look at me before I shot him in his goddamn head. Sorry for swearing.

Sitting there in the house, next to the dead body, I thought of my brother. One time after school he took me to 7-11 to get a Slurpee. We were talking about the usually boring stuff. When we were standing outside, letting the sun battle the brain freeze from the drinks, I thought of something that had happened that day at school. “Hey, at school today, we found out one kid was a gay faggot because he touched another kid’s butt on purpose!” My brother turned to me. He looked really angry, almost like he wanted to shake me. He said, “Mercy, I don’t like those folks any more than you do, but I don’t hate ‘em. Don’t call them names. Don’t ever do that. That’s just hate.” I’m not sure I said the word “faggot” out loud again until I told you all about the protestors, what they said. And next to that dead body, thinking about my brother’s love, I cried. I cried, and cried, with real sadness this time. Then, with the sadness gone, the rage gone, I was empty. I pointed the gun at myself, but my bravery was gone.

After I realized I would find no peace, I called the police myself. I didn’t lie to them. I had no trouble telling them my story, briefly. It was my parents I couldn’t talk to. I couldn’t get a word out, I just cried. And they didn’t smile, either. I don’t think they were singing songs on the way to the prison. I don’t think they know what God was thinking this time. I don’t want to know what He had in mind.

[She picks up the bronze star again.] They’re not going to give me a medal. So this one is for me and my brother. We’re both just as stupid, we’re both heroic, we’re both brave. I took this before I left, and I kept it. The prison officers, they had sympathy for me, they let me keep it. I’m going to keep it until the end. I’m not much of a fighter, but those girls in prison better watch out if they try and touch this medal. Although, I guess as a teenage killer, I already have a pretty tough reputation. I got this medal for it.

I told the police one lie, though. And I lied to you, too. I told them that I found the boy, and as soon as I saw him, I shot him. But that wasn’t true. He wanted to chat. He was happy to talk to me, even after he saw the gun, even after he knew exactly why I was there.

“Do you know who I am?” I asked him.

He shook his head.

“You were at my brother’s funeral the other day.”

“Praise Jesus,” he cried out in loud whisper. “Have you come to bring me to the Lord?”

“I think I have,”

“You can do nothing to my faith, demon, whatever you do to my body.” He had fallen to his knees. He put out his arms, to receive a blessing.

“I’m not a demon, I’m only a sinner,” I needed him to know the difference. Because sinners are supposed to deserve mercy, and compassion. That’s what I’d been taught.

“Hate the sin,” I said, “Love the sinner.”

“Think about the order,” he replied. “You must hate first, and then love.” “You’ll never love,” I said. “You wouldn’t know how!”

“I’m sorry if I can’t love faggots and queers and whores and heathens like you can. I can only love God.”

“God is in all those people.” I’m sorry, I’m shaking now as much as I was then.

“Satan is in them!” He hissed back.

“He’s in you too!”

“I know,” he said, “and I thank you. You’re about to take him out, for good.” He smiled that sweet, sure smile. God I wish I hadn’t felt that he could be right. Maybe we are all sinners.

“If your brother had repented, maybe that sand devil that shot him might have taken Satan out too.”

“How do you know if he repented?”

“He’s a sinner, like you.”

I turned away, “Judge not, lest ye be judged.”

He was laughing. Laughing. “What’s so funny?”

“God is judging. He judged your brother in blood. I know he’s a sinner.”

I turned back to him.

“Then why are you about to die?”

He smiled.

“Did you know my brother’s name?”

He looked at me with real eyes for the first time. He was surprised.

“I did not,” he said.

“You attacked at random,” I said. “Like a dog.”

“Vengeance finds a way.” He wasn’t sure. He wondered what else he didn’t know.

“My brother’s name was Alex.” I realize I haven’t told you all that either. Alex was my brother. He died and got a medal for his bravery.

(She is looking at the killer again.)

“He died because he was brave. Maybe that’s why you are dying too.”

He smiled again. “I am dying for the Lord.”

“What’s your name?” I asked.

“Tom Melville.”

“I’m going to kill you, Tom.”

I cocked the gun. He looked away. “Satan, get behind me!”

And then I thought about my brother. When he would walk me to the playground and push me on the swings, higher than anyone else would, as I laughed and cried with joy. He was pushing me now. I felt the wind around me, the tears in my eyes, I put the gun in this kid’s face and I said,

“Lord Jesus Christ, have mercy on us, we are nothing but poor sinners.”
```

---

## IC-0063: Taller To-day Copyright 2006 by Edith Kirkby.

- Title: Taller To-day Copyright 2006 by Edith Kirkby.
- Author (byline): Not specified
- Work: Taller To-day Copyright 2006 by Edith Kirkby.
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1322
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
Taller To-day by Edith Kirkby

I suppose that stalling…will not make much of a difference, so…because the fact that what happened happened…happens to…I think I’ll stop here while…okay, I’m going to…I know I’m going to end up telling you everything eventually, about love, about her…eyes, and laugh…she would laugh…ridiculously hard at things that weren’t quite funny…it might just be me…but, Joseph Heller, Voltaire…wouldn’t make her laugh…and then I’ll start talking about…the…do you ever feel like going into a large crowded area, some urban… vicinity, and…yelling, “I love you” to the whole crowd all at once, or sometimes individually, hoping that someone will affectionately return your love, and you’ll be able to drop everything at that time and forget all your past loves and run away that one beautiful someone?…because I don’t either. That can be a rhetorical question.

This is what I need to show you. I really hope you’ll like this…but don’t read into that…

This is Auden. Auden’s poetry…is…great…these are the collected works as…selected by Edward Mendelson…who…I don’t know who he is…but…he’s brilliant…obviously…page thirty-three …May…the name of the poem…“May with its light behaving stirs vessel, eye and” there are better ones in here…so I’ll read…A Walk After Dark…this is good…”A cloudless night like this/ Can set the spirit soaring/ After a tiring day/ The clockwork spectacle is/ Impressive in a slightly boring/ Eighteenth century way”…it’s so pretentious…it’s…I love it. Um…anyway…at the time I was…well…a lot of things…but…I was…studying literature…at Columbia University…in the city of New York…and, if you’re going to study past your bachelors…don’t…don’t study literature…I did…but, please don’t do it. Why would you want to interpret and reinterpret literary masterpieces that have already been beaten to death by pretentious nineteenth century scholars who said things like “Well, I believe the Aeneid of Virgil is biblically allegorical under the guise of Homeric principles”? But…I studied literature…and I don’t necessarily regret it. But…I don’t want to talk about that…um…

She…I might as well give her a name now…she has a name but…her name is Jill…Jillian…Jillian Warner. And she was beautiful…um…I was twenty-three and she was twenty-one…she was studying engineering…talk about pretentious, especially at Columbia…and, um…

When we met…it was perfect. I mean…in retrospect…if there was a love song playing…and if our eyes rose in slow motion…we would have been in an Academy-award winning film…. just for that scene. We were in the library right off of 114th Street…and I’m going through my daily readings of literary criticism on…Thomas Hardy…it was Mayor of Casterbridge…and as I’m reading about deterministic disputes on Michael Henchard and worrying about my next three…page…written…response…

Sorry…she was fifteen feet away…at least…from me…and…reading some advanced Calculus or engineering book on finite mathematics…and…our eyes meet…she looks down…I don’t…which might’ve been creepy…but…uh…no, it wasn’t…she looked so happy…and her eyes were…perfect…

As you can probably guess, it was love at first sight. Not love…but…fervor…no…that’s, that’s too sensual…anyway, we were friends….we became friends from that meeting…Me and Jill. Or Jill and I…or…She lived in an apartment with three roommates on Riverside Drive, five blocks from my apartment, and generally we used to meet at some time in the evening when we were both tired of stuttering…studying….speaking of stuttering…and…we would just walk, and talk, and…it was wonderful.

She had these deep blue eyes that were so telling. She would smile with her eyes. And for the first few months I knew her she would never frown with them. Her hair was…she was absolutely gorgeous. We never…it’s funny…we never got into any conversations with one another about past loves or friends we had had earlier in life, but I think…um…I was…I had to be her only love. It’s funny how much you can know a person without being able to recite or list off facts about the person.

I met her in September of that year. And in February we started to officially be involved in…a relationship…of sorts. It was snowing…again…a perfect, cinematic moment…that anybody would want…she…snow is slowly coming down…we had been walking for an hour or so…and we both stop and…consciously peek through…some branches of this tree…looking at the streetlight in focus. And we just stayed there…for as long as it took for us both to realize how like-minded we had just proven ourselves to be. That’s when you know you’ve met her…when you establish this deep…um…connection that…if you put words to it…might ruin…something about it.

Well, anyway, despite the short amount of time I had been dating Jill, I loved her. That’s also really strange, when you hear yourself uttering those words…what with love…and…how silly and fickle it is…there are a lot of things better than love. Horseback riding, for example…I hate horseback riding, forget about that…snow, snow is better than love. When it snows, all the children walk out on the sidewalks when school is cancelled, building snowmen…and throwing snowballs at grumpy men, their mothers come out with hot chocolate, fresh off the stove…snow is better than love. But, the first time I experienced snowfall after Jill…um…even though it was five months after…I hated it.

She…uh…called things off, so to speak…one of those, ‘it’s not you it’s me’ monologues on the value of independence and the mutual appreciation of a long lasting friendship, despite the clarity I offered her when I told her that I needed her, that she was a source of beauty and…encouragement to my otherwise…literature-filled life. That was May. May twenty-third.

The past few weeks had been strange, what with finals and her getting and not getting into graduate schools, or whether she wanted to work for a year…or…I don’t know…

Her old roommate called…me…last August…saying that there had been an accident…one of those massive off-roaders had hit their Mazda…and…Jill’s father was in critical condition…and Jill had died instantly…from the impact…

She had actually died a few days earlier, the funeral was in California the day I found out…I was working that summer in the City…so…

That’s just pitiful…she was the one to cut off connections with me that summer, and I wasn’t allowed to grieve her at all…because to her parents…everybody else…it didn’t matter that I was in love with her…um…but…not be able to say anything…and to grieve passively…it feels like…

Auden. I’m telling you, when you feel miserable, it’s Auden who’ll help you out. Funeral Blues: “Stop all the clocks, cut off the telephone,/ Prevent the dog from barking with a juicy bone,/ Silence the pianos and with muffled drum/ Bring out the coffin, let the mourners come.”

I’ll skip down to the fourth stanza: “The stars are not wanted now: put out every one;/ Pack up the moon and dismantle the sun;” Dismantle the sun…great line…sorry…”Pour away the ocean and sweep up the wood;/ For nothing now can ever come to any good.”

That’s page fifty of the Mendelson selection. W.H. Auden. Wystan Hugh Auden. Jill gave me this book. For…Valentine’s Day.
```

---

## IC-0064: Thomas More Doesn’t Know Me

- Title: Thomas More Doesn’t Know Me
- Author (byline): Sarah Weiner
- Work: Thomas More Doesn’t Know Me
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1809
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
“I would rather be honest than clever.” Thomas More said that in Utopia. He’s a philosopher. Well, if I’m being honest, I have an issue with honesty. It’s not that I lie to people. I mostly just lie to myself. Denial is more than just a river in Egypt, you know [*buh dum tsh* finger guns*]. Ok so here I go—honesty time. I guess I should start by not hiding my emotions behind 10 layers of sarcasm and puns… [considering this] no that’s too far. I’m not ready for that level of sincerity. Actually, if we’re on the topic of philosophy then here’s some relevant honesty for you—studying philosophy doesn’t make you special and it definitely doesn’t mean you’re morally superior to anyone else. [Getting heated] Further, Jean-Paul Sartre is a piss poor writer—yeah, I said it—and as much as I enjoyed reading Utopia; why couldn’t Thomas have just gotten to the damn point instead of burying his true feelings about communism under a fat load of syntax variations and convoluted Latin bullshit. That’s not very “honest” of you, Tommy. How can you possibly lecture me about honesty when you pull stunts like that? [mockingly] “I’d rather be honest than clever,” oh please; of course, you want to be clever. Not just that—you want everyone in the room to know just how clever you are. Why else would you become a philosopher? I hate philosophers, [calming herself] but I get it. Being able to insult Sartre and quote More in the same breath does make you feel powerful which is a nice change because I often don’t feel very powerful at all…it’s the opposite really. That’s half the reason I started studying philosophy in the first place. Power and spite. [laughing a little] Pleasant, I know.

[reluctantly- she clearly does not want to talk about this] My best friend—uh well—he was my best friend. We don’t talk much anymore. He’s the one who introduced me to philosophy. Mickey Krone. I usually just called him Krone or Mick, [starting to have fun with it] but he was also K-dog, Mick Jagger, Mickey Mouse, Mickereno, OR when I wanted to make him extra uncomfortable I would call him Mick-daddy. The internet really ruined that word for us, but I have the sense of humor of a 9-volt battery, so I still think it’s funny. [remembering fondly] I remember exactly how we first met. I went to a party with some friends. There were only about 25 people there, but the way he ran at me when I walked in…you would think I was the hot new toy on black Friday. It was startling, but I appreciated the boldness of it. I’d like to say we had a pleasant conversation but Mickey… he’s an intense guy. I don’t mind that. I can be intense too, [this is funny to her] but that conversation felt more like an interrogation of my political views. He had this spark in his eye when he was challenging me. It was like he was trying make me angry, but it wasn’t really working because I genuinely enjoy debating policy despite us having polar opposite views. I’m capitalist scum and he’s one step short of a dirty communist, but that didn’t matter. It was fun and he’s easy to talk to. Later, we raided the kitchen to make peanut butter sandwiches.

Now since I’m trying to make Thomas More proud, I should be honest and admit that I had a crush on him pretty much then on [defending what she just said] but it’s not like I wanted to be his girlfriend. He already had one of those which shouldn’t be surprising. He’s a real smooth talker. Every word out of his mouth was like a dare, pushing you to expand your mind; to think more critically. And he would listen so intently you could be fooled into believing you were saying something profound and absurdly clever even if it was just what you ate for breakfast that morning.

But if you really want to know about Mickey, you need to see him in his full form. I snuck into a round to watch him debate once. I technically wasn’t supposed to be there but come on! How could I resist? The other team was running their mouths like lightning, fumbling with their papers. They were messy. Not our boy, Mick though. His language was chosen carefully and deliberately—every move, pre-meditated. It was like watching a nature documentary where the black widow waits in silence as her captured prey flails desperately before striking with perfect accuracy and grace. It was fascinating to watch him make the other team hate him and the judges fall in love with him at the same time. [catching herself] Ah but Mr. Thomas More says honesty is more important that cleverness so I should also mention that he was constantly trying to psycho-analyze me which is super annoying especially because he was usually wrong, and it just made him sound like a pretentious douche nozzle. He got it in his head that just because he’s a philosophy major, he automatically understands me better than I understand myself. [trying to be fair] Even still, he is the smartest person I know…or at least he was really good at pretending to be. That’s the thing about philosophy. It makes it hard to tell if the guy laying upside on your couch ranting on Cicero is actually a genius or just a very talented con artist.

[really does not want to get into this] I guess it’s time for me to explain what happened, right? Why we don’t speak anymore. I’ve stalled long enough. It was just about a year ago now. I was having a royally crap week. Life was hitting me with everything it had: school stress, friend drama, family chaos, and I was not handling it well. So, Mick came over to my apartment to cheer me up.

I’m lying on the floor having a break down (as I do) and Mick’s sitting next to me telling me what I’m feeling (as he does) and I’m just hanging onto every word hoping it will ground me for a moment. Except, I feel like I’m drowning and he’s really less of an anchor and more like driftwood. Then…he stops talking. That’s alarming because he loves the sound of his own voice, [it’s like she’s experiencing this all over again] but he was just sitting there staring at me…until…well he kissed me. I think I was supposed to be happy. I mean, he was my best friend whom I also had feelings for. That’s like something out of a frickin’ John Greene novel. But I was not in the right headspace for this to happen let alone deal with his pissed off girlfriend. So, I pushed him off. I told him no, and he laughed at me. He laughed at me. “ Oh come on, Em. I know you like me. You should really be more honest with yourself” [shocked, infuriated] I should really be more honest with myself? Spoken like a true philosopher. That’s the thing about Mick…once he decides how you feel, that’s that. There’s no telling him otherwise. No matter how loudly you scream “how can you possibly know how I feel!? I told you no. Why is that not enough?” he won’t hear you. He decided I wanted him…and his judgement is final. Like I said, he’s an intense guy and sometimes…it’s scary. Watching the black widow is only fun until you’re the one caught in the web.

Everything that followed is fuzzy. I couldn’t tell you exactly what happened if I wanted to. I just froze. I couldn’t move. I couldn’t speak. I used to hear stories about women who were raped, and their abuser was set free because the woman didn’t fight back. [letting this sink in] I understand that now. Then, there was the pain. If I didn’t know any better, I might have thought someone lit me on fire. I wish someone had. Then there was nothing. Just black and it was over.

He accidentally left behind his copy of “Being and Nothingness”. (You know that 500 page, needlessly complicated trash fire of a book written by none other than Jean-Paul Sartre.) I feel like there’s some irony hidden in that. There were little notes and things written in the margins. I don’t know why, but I read it. It made me feel like I was doing something productive I guess…I felt like I had control again, but that was really just me lying to myself.

We didn’t speak for almost a month after that. Eventually I got up the nerve to confront him…but he didn’t understand why I was upset. I told him he raped me. He disagreed. “You’re just confused. If you had been more honest with yourself from the beginning, you wouldn’t feel this way,” that’s what he said. [feeling defeated] Your friends aren’t supposed to do this to you. Strangers are the ones I should be afraid of.

[taking a breath] I would like to say I was shocked that he would treat me like this…but in hindsight, it makes sense. There’s another quote from my good ol’ friend Tommy that says, “as robbers prove sometimes gallant soldiers, so soldiers often prove brave robbers”. [almost laughing but bitter] I was standing around all this time with my head up my ass thinking I had a soldier on my side while the bastard was robbing me blind. In all seriousness, I didn’t know him as well as I thought I did, but now? Now I see him for what he is. Mickey Krone is a con artist and a damn good one. So good, in fact, that he conned himself. He spends all his time telling others who they are and how they feel so he never has to face who he is and how he feels. I pity him more than anything. He can lie all he wants, but deep down he knows what he did, and he has to live with himself. I used to obsess over what happened—trying desperately to think of something I could have done to stop it, but what does that matter anymore? There’s no happy ending to this story. There can’t be. Even if more people had believed me and Mickey got what he deserved, I was still raped by the guy I trusted more than anyone. I was raped, and nothing can change that. All that’s left is to move forward. It’s time for me to be my own “gallant soldier”. So here I am—speaking my truth, being honest. And honestly, I think Thomas More would be proud of me. Eh but who cares what he thinks? [with a smirk] He’s just a philosopher.
```

---

## IC-0065: 13 Things about Ed Carpolotti

- Title: 13 Things about Ed Carpolotti
- Author (byline): Jeffery Hatcher
- Work: Three Viewings
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Oct 1996
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: VIRGINIA
- Teaser before the introduction: No
- Spoken words (computed): 1896
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jeffery Hatcher
Book: Three Viewings
ISBN: 978-0822214946
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Oct 1996
```

### Introduction (context only: never use it for content warnings)

```text
Allen Ball once said, “In order to be successful one must project an image of success at all times.” In relationship to friends, family, business, etc. one must never, in essence, let his guard down. In 13 Things about Ed Carpolotti, however, newly widowed Virginia Carpolotti gets some shocking news - her “successful” husband Ed left her in perilous debt to shady bankers, mobsters, and embezzlers.

As Virginia’s picture-perfect world unravels, we discover how fragile one’s heart can become and the hidden strength behind a love that transcends death.

13 Things about Ed Carpolotti by Jeffery Hatcher
```

### Performance text (classify this)

```text
VIRGINIA: (Pg 45-46) (Upbeat and energetic) Ed always said I couldn’t keep my mouth shut. Well, he didn’t always say it. I think he said it once. He was never a talker. Even before we were married. He’d clam up at dinners, parties. He knew I hated him being so quiet. I’d say to him! “Ed, at least look like you’re talking to me!”

So he tried. Whenever he didn’t have anything to say, he’d turn to me and start to mutter: “Mary had a little lamb,” he’d say. And I’d come back, “His fleece was white as snow.” “And everywhere that Mary went.” You get the idea. People thought we had quite a rapport!

Well. Ed gave up smoking four months before he died. He had his first heart attack on Halloween, his second on Thanksgiving, and he died just before Christmas. Well, he loved holidays. When we brought him back to the funeral home, the undertaker’s assistant asked us if there was anything else he could do to make Ed look more natural? (beat) (Pg 47-48) Natural? He’s dead, wearing bifocals and a hairpiece, what’s going to help the illusion of reality here?

I can’t remember where or when I met Ed. Tootie Vaughn would remember. Tootie’s my best galfriend, and she remembers things like this. All I remember was living at home with Mother and Daddy and then there was Ed. Mother and Daddy did not approve. I had to sneak out of the house to see him once. Mother and Daddy thought I’d gone with Tootie to see My Friend Irma Goes West, but I’d gone out with Ed. When I got back Tootie was in our living room with a guilty look on her face, and Daddy quizzed me about where I’d gone. I lied of course. Said I “had so gone to the movies.” Daddy said “Prove it,” so I made up an entire plot for My Friend Irma Goes West. I went to see [it] and was surprised to learn just how close I’d got! (beat)

I wasn’t there when he died. No one was. Three AM, a week before Christmas. The nurses said he didn’t make a sound when the aneurysm hit. They said with the dementia that set in following the second cardiovascular infarction, he was lucky. (beat) I guess. He recognized Debbie once towards the end, but he thought we were in Las Vegas. He thought I was his mother. One night he saw a cow in the room standing behind me.

Lucky -- Yeah, I’d like to die in Las Vegas with my mother and a cow too. (beat)

(Pg 49-50) It was three days before I could get down to the office. The way the will’s written I’m president of “Ed Carpolotti, Inc.” President. Debbie asks me over the phone if my “first official act will be to recognize Cuba.” (she laughs a trill)

I laugh . . . like I know what the hell she’s talking about.

Ed’s secretary, Joy, showed me what our attorney said I needed to see. The construction business had been bad the past year or so. But the files showed assets. “We’ll be fine,” I said to Joy.

And Joy just looked at me. I went to see our attorney the next day. I depend on Danny Spahr, but it’s hard to invest a lot of authority in the little boy who used to deliver your milk. Danny -- Daniel, excuse me -- and I talk for a while. Then Danny takes out a file marked, “BANK.”

“Virginia, did Ed ever ask you to sign anything over the last year? Any papers? Documents?” (she touches her neck) “I was always signing something or other. Ed was such a one-man band, wheeling and dealing” . . . (to audience) I told Tootie about the papers when I visited her last April. Could she have told?

“Virginia, did you sign anything that looked official?” He delivered our milk. You can’t lie to a blue-eyed boy who used to deliver your milk. I nod. He hands me the papers from the file. Business loans to “Ed Carpolotti, Inc.” secured with every asset of the company. Business loans – signed personally. Which means – since Ed got me to sign the papers – that I am now personally responsible for these loans – over half a million dollars.

Danny tells me that Ed was behind in payments. Six months behind. The bank has frozen my assets. Frozen, Danny goes on to explain is a euphemism. They’re going to take my money. Unless I can pay off the loan . . . within the week.

What I do next I have never done before in my life. I run away. (pause)

(Pg 51) I go home to the house on Bray Barton. There are three messages waiting for me on the answering machine. The third is from a voice I don’t know well.

“Gin, hey, this is Dino, like ta’ talk to ya’ gimme a call.” (beat – to audience) Well, that’s what he said. I find his number in Ed’s book, call him back. “We have some business to discuss, Gin. (Pg 52-53) See, Ed, he wanted to sell me half of this landfill he owned. I think he needed the money and I told him, I said, ‘Hey, Ed, I don’ think I wanna buy into a partnership, but tell ya’ what: I’ll loan you some money at a good percentage. How much ya need? And Ed told me. And I give it to ‘im.” “How much did you give him? “Half a million” “At what percentage?” “50. Do you have the money, Gin?” Dino is the owner of Smith Trucking. They own no trucks and there has never been a Mr. Smith. (beat) I have to call somebody. Someone in the family who can help. I pick up the phone and dial Ed’s brother Frank. (Pg 54-56) I start my speech about Danny, about [the bank] about Dino. Finally, I stop. And then Frank speaks:

“Virginia, you know, Ed was a real wheeler-dealer.”
(a stricken look) “How much money did he borrow [from you]?”
“Three hundred thousand – at 18% -- I was his brother and truth be told I’m taking a
beating”
I explain to Frank I have no cash, no savings, nothing that’s not frozen.

“You have the house. [My son] Randy’s getting married next month – always loved your house . . .” I look at the answering machine – • Danny, who says we have to have a meeting, and he’s willing to come to the house. • [The Bank], saying Mr. O’Klock wants to see me, and he’s willing to come to the house. • Dino, who wants to come by the house with a friend named Vinnie. • Lorraine, [Frank’s wife] who knows of an apartment for rent behind the shopping mall. • Joy at the office – Do I have any ideas on how to make this week’s payroll? (pause) I start upstairs to bed. As I go through the hall towards the steps, I stop. Under the front door is a manilla envelope, shoved halfway through. I take the envelope upstairs to my bedroom, lock the door. Ed’s hairpieces watch me as I open [it]. (pantomimes, looks confused) It’s a white piece of paper with letters pasted on it -- like a kidnapper’s ransom:

“I HAVE A LIST OF THIRTEEN THINGS ABOUT ED CARPOLOTTI. EMBARRASSING TO HIM AND TO OTHERS. HAVE ONE MILLION DOLLARS READY BY THIS FRIDAY. OR I WILL RELEASE THE LIST. TELL NO ONE.”

(Pg 57) (pause – during this next section Virginia becomes increasingly angry, hurt, confused and desperate) What is it about these men? Who built their businesses and grew their families and died so frightened and alone? Who could never tell their wives their secrets – their fears? I am beginning to understand the sin of failure. Who do you go to when you have committed that? Your lawyer? Your banker? Your brother? No one absolves failure. No one lights a candle. You go mad. A cow with your mother in a room in Las Vegas. He had run out of ideas, plans, wheeling and dealing.

I’m a widow. I owe three times as much money as I thought I had in the world. I’m supposed to be drinking gin and tonics; we are supposed to buy new cars after our husbands die. or buying a new car, you know. [Instead] I lay out my silver, my china, my crystal, my jewelry, everything I have on the dining room table. . . it won’t come close to what I need. Friday is two days away. There are 46 messages on the answering machine, I do not return the calls. (She begins to hold herself and rocks back and forth)

(Pg 58-59) I haven’t told a soul, I am screaming so slowly, so dimly, so no one can hear. Where did I meet my husband? Why can’t I remember when and where I met my husband?

(She shuts her eyes, stops rocking, and makes a decision) I pick up the phone and dial Tootie Vaughn. I fall apart and I tell her everything. It’s amazing how the deadlines come on the same day. The bank’s deadline. Smith Trucking. Frank. The note. I am sitting in my sunroom at 8:30 a.m. waiting for the hordes to descend upon my door. It helped to tell Tutti about everything, about the list. And she promised not to tell a soul. I am frightened. But I am ready -- Let ‘em come! The first call came at 9:00 a.m.

“Yo, Gin, Dino here. Hey! This list thing. Whaddaya say we call it even huh? Square one. Zero-zero. Don’t call back.”

The next call came at ten forty-two. “Virginia, Frank here. Randy and Courtney will be living at home for the foreseeable future. Call if you need. Tootie Vaughn says hello.”

Tootie! Tootie’s blabbed to everybody. And the idea of that list has scared them off! What’s in that list? (Pg 60-61) For the rest of Friday, I wait for another demand from the author of the note. But it does not come that Friday. Or the next Friday, or the Friday after that. Since the loans have been forgiven and the creditors quieted, Danny says I will have some money to invest, retire on, buy a new car.

(briskly) Within the month, we begin to dissolve the business, sell off the assets. Joy —[Ed’s secretary] — handles most of the work. I just sign the papers. As I sign the last one; Joy [comes in] holding a manila envelope, just like the one that was slipped under my door. “It’s from Mr. Carpolotti,” she says. Then she walks away -- quickly.

(Virginia opens the envelope, takes out a piece of paper) Inside is a list. (she reads aloud)

1. I have never loved any other woman but you.
2. I cannot look at your hand without wanting to hold it.
3. I wanted to build you a house but you loved the one we drove by, I never had the
chance to change your mind.
4. In my wallet, I keep a picture of you when you were ten years old; I fall in love with
you again every time I see it.
5. I think about you every night before I go to bed so I can dream of you in my sleep.
6. My Friend Irma Goes West is the best movie I never saw.
7. I have always understood our child more than she could ever imagine.
8. We met at the Green Mill Luncheonette on February 22, 1955.
9. I am writing this in St. Joseph’s Hospital. I am less scared than tired.
10. I have made mistakes.
11. But I think this last plan will work. Joy has my instructions
12. You could never keep your mouth shut. I knew you would tell Tootie Vaughn about
the list and she would tell the world.
13. Mary had a little lamb.
```

---

## IC-0066: 2.5 Minute Ride

- Title: 2.5 Minute Ride
- Author (byline): Lisa Kron
- Work: 2.5 Minute Ride and 101 Humiliating Stories, Pgs 5-39
- Publisher: Theatre Communications Group
- Publication date as stated: May 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LISA, DAD
- Teaser before the introduction: No
- Spoken words (computed): 1648
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lisa Kron
Book: 2.5 Minute Ride and 101 Humiliating Stories, Pgs 5-39
ISBN: 978-1559361811
Publisher: Theatre Communications Group
Date (Month/Year): May 2000
```

### Introduction (context only: never use it for content warnings)

```text
You know that sound . . . the clack, clack, clack of the wheels on the track as the roller coaster inches you toward the first drop. That sound builds suspense -- builds anxiety -- until all of a sudden, you’re at the top and facing your ultimate demise at the bottom of the first drop. At least with roller coasters you know the ride won’t be very long and the likelihood of surviving the experience is very high. Now imagine you hear that same sound again, but this time you aren’t at an amusement park . . . The year is 1937. The track is for an overcrowded train car and the clack, clack, clack is bringing you closer and closer to Auschwitz. This time it’s not a . . .

2.5 Minute Ride by Lisa Kron
```

### Performance text (classify this)

```text
The sound of a slide projector advancing to the next slide, a woman holding a clicker describes the “slides” (just squares of colored light, not actual pictures) She describes what she sees.

LISA: (Changes slide) (Pg 5) These are my father’s parents. I never knew them actually. My father left his hometown in Germany in 1937, by himself, when he was fifteen years old, as a part of a program to get all the Jewish children out of Germany. I’m making a videotape about my father – about his experiences – well, actually about this trip we took together to his hometown and then to Auschwitz.

(Changes slide) (Pg 6-7) This is my father and his father in the synagogue where his father was the teacher in the Jewish school. This was taken a few days before my dad left Germany to come to the United States. When he came here, he lived with a foster family in Connecticut and received letters from his parents about once a week, until one week, instead, he received a letter from the Red Cross informing him that his parents had been deported to the Litzmannstadt Ghetto in Poland. That was the last time he heard from them.

(Changes slide) This is a letter my father received in 1947 from a man who had been with his parents in the Ghetto. I had it translated and it says, “Unfortunately, I must inform you that your parents were among the first transports sent to Auschwitz.” So, the other part of this trip was Auschwitz where neither of us had ever been before. The trip was so much more than either of us had imagined and when I returned I decided to make this video. My father has so many incredible stories – I wanted to make a record.

(Changes slide) (Pg 8) This is Lansing, Michigan where I grew up, where my parents still live. [I went back home] to shoot some interviews with my dad, and then also to accompany my entire family on our annual trip to the Cedar Pointe Amusement Park in Ohio, where my dad loves to ride the roller coasters. [I] wanted to get that on tape as well. (Pg 11) At the entrance to the Magnum there are signs which say under no circumstances is this ride suitable for people who are elderly, diabetic or have heart conditions. My father can’t read the signs because, in addition to having all the conditions listed, he is also legally blind. I tell him what it says. (to dad) Are you sure this is a good idea?

DAD: I don’t have to do anything. All I have to do is sit there.

LISA: (Changes slide, laughs) (Pg 18-19) Cedar Point has more roller coasters than any other amusement park in America – and every year they add a new one. Here you can see me and my dad standing in front of the Demon Drop which is a three-story free fall. Dad asked and asked and asked about it. All of a sudden it dawned on me. (to dad) Do you want to ride the Demon Drop?

DAD: Oh. Well, if that’s what would make you happy.

LISA: It’s hard . . . it’s hard to describe a three-story free fall. It’s not bad, really. It’s not good. It’s just like – (a sudden shocked exhalation of all the air in her lungs, as if kicked in the stomach) When it was over, I was speechless, I was aghast. I looked at my dad. He was grinning. A crazy sort of a grin.

(Pg 19-20) [And now we’re] in Poland. I don’t speak Polish. I don’t speak German either. One time we stop to ask a man for directions and when he answers me I start to laugh. Right in his face. How absurd it is that I’m listening to him as if I had the vaguest idea what he is saying. He says something like, “Blah, blah, blah. Pointy, pointy, point. Polish, Polish, Polish, Polish . . “ In the direction of Auschwitz. (Pg 22) What month was it? October. So cold.

Dad and I, we’ve been waiting for this our whole lives. We don’t know how to feel. Tomorrow we’ll be at the place where his parent’s bodies lie. No, they were burned. Will we step on their ashes? Will we see a wooden pallet where they slept? Will they be hovering above the place, watching us? Have they waited all this time for their little boy to come and say good-bye to them? (Pg 23-24) What will I do, I thought, if my father cries? I’ve never seen him cry.

(Changes slide) (Pg 24) We go on the Mean Streak, a new wooden roller coaster with a 2.5 minute ride. And as soon as we take off, I know that it’s a mistake. Dad is clinging to the bar and he has a look on his face like a horse in a fire. I think, Oh my dear God, what have I done? This is really going to kill him. 2.5 minutes is a really long time on a roller coaster if you are having a good time. If you think the experience is killing your father it’s a really, really long time. For a split second I can see [the headlines] Bizarre Murder! [Daughter] Forces Blind Holocaust Victim on Roller Coaster! I’m so relieved when we get to the end, I want to carry him to the first-aid station. He stumbles out of the car. Walks right up to the video camera, as if for a post-game interview, and says, “That one was the best!” And then he asks me if I want to go again.

(Changes slide) We read every word of every exhibit. I have to read them out loud to Dad,
of course. (to Dad) Okay. This is a poem by a woman named Zofia Grocho-o-wal-ska
Abromowicz. It says:
1944.
Wheels speed along the tracks
rushing toward the victory of crime,
transporting, transporting people to gas,
people to a cremator,
people to a petrol sprayed pyre.
Smoke floats, thick, foul smoke . . .

(Seeing the next line, her face crumples. A sob comes out. She turns and overs her face) (to audience) I bury my head in my father’s shoulder. He pats my back. He’s okay. He’s a good dad. I feel shaky and helpless, but pull myself together. (turns back to the poem) People burn people here.

(Changes slide) (Pg 25-28) In the afternoon we drive three miles to the second camp – Birkenau. Here there is no sun. This is malevolent ground. They give us a map and we go exploring. The day alternates between a feeling of horror and a feeling we’re at Disney. We look at the map and say, “Well, where should we go next? To the pits where they buried bodies in mass graves or the fields where they piled them up and burned them.” We have to laugh. Especially at the bookstores which we refer to as the Auschwitz gift shop. We make gruesome jokes about what gifts they might sell . . . lamp shades and soap. I actually go into one of the shops to buy a book but it’s full of pictures and I walk out. (a long sill pause – an almost unbearable silence as she realizes the thing she’s about to say) I’d been so afraid I wouldn’t feel anything here. (the silence hangs as she realizes) I think that was my biggest fear.

(Changes slide) You already know what this looks like, right? (Changes slide) You’ve seen these images before. (Changes slide) You don’t need me to describe this to you. (Changes slide) Even if you’ve never been there, you’ve seen the History Channel . . . Sophie’s Choice . . . Shindler’s List! (Changes slide) You know what? That’s exactly what it looks like. The films from the liberation of the camps with the bulldozers and the bodies. Right? (Changes slide) You all know what this looks like.

I feel like I’m evading the issue here, but I don’t know what the issue is. Yes! Yes! I wanted to tell you about our trip. No. No! That’s not my point! I wanted to tell you about my father! (pause, stunned at her own revelation. She has no idea what to say next. This should be a truly horrible moment- she drops the clicker) But . . . I don’t know. I really don’t know. He’s . . . a guy . . . You know, he’s an ordinary guy. He’s my dad. (she speaks softly and intently, needing to make a connection so the audience hears and understands what she is about to say)

Do you know what he told us when we were growing up? He told us many times, “If it weren’t for the good fortune of being born a Jew I might have become a Nazi.” And then he’d tell us this story: he’d gone to school with a boy named Lohmann who was the only other boy in his class who didn’t wear a Hitler youth uniform. My father wasn’t allowed to wear one, of course, because he was a Jew, and he was beaten by the other boys for that, but Lohmann didn’t wear one because he refused. “I often wonder,” my father would tell us, “I often wonder.

If I had had the opportunity to wear that uniform if I would have had the courage of Lohmann? I’m lucky to be a Jew so I didn’t have to make that choice.” (stops herself, suddenly realizing she has gone too far and her intensity has become overwhelming) Aahh. I can’t tell you his stories. I don’t have any filter for them. I can hear the myth and the awe creep into my voice. I keep inhaling and I don’t exhale, something like that. You should go to Lansing and meet him. He’ll cook you dinner! I am so not kidding. (laughing through tears)

(Pg 37-38) I have a checklist in my head: things I have to do before my father dies. Number one: look him in the eye and tell him that I love him. Check. Number two: go with him to see the place where his parents were killed. Check. Number three: make this video about his life.

Taping him in his study, at his office, in the park. I’ve been trying to look at the videotape. It’s excruciating. He’s lived in Michigan for forty years. He eats in front of the TV. He takes a fitness class at the community college. His life in Lansing doesn’t quite match up. The edges are blurred. Then we go to Germany and my father was home. He’s in focus here, I thought. He’s in context. (picks up clicker) (Changes slide) My father is a small man. He smells like lavender. He wears a suit.

(Pg 39) When I was in college I was taught that if you are standing near a piece of furniture on stage you should put you hand on it be cause that will make you look bigger. Well, [that’s what I’m doing] . . . I’m putting my hand on my father’s life.
```

---

## IC-0067: 9 Parts of Desire

- Title: 9 Parts of Desire
- Author (byline): Heather Raffo
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Jan 2006
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: UMM GHADA, THE DOCTOR, HUDA
- Teaser before the introduction: No
- Spoken words (computed): 1031
- Already set (do not supply): none

### Source block (context only)

```text
Author: Heather Raffo
ISBN: 978-0822220978
Publisher: Dramatists Play Service
Date (Month/Year): Jan 2006
```

### Introduction (context only: never use it for content warnings)

```text
On February 13, 1991, the US military fired laser-guided "smart" bombs into a large civilian shelter in al-Amiriyya, a residential neighborhood in Baghdad. The bombing killed 408 civilians. The invasion of Iraq and the liberation of Kuwait had begun. But it would be 12 years before Saddam Hussein is removed from power and executed for crimes against humanity.

Heather Raffo in her play 9 Parts of Desire gives voice to the diverse population of Iraqi women, struggling to survive . . . struggling to be heard.
```

### Performance text (classify this)

```text
UMM GHADA: (Pg 28) I named my daughter Ghada.
Ghada means tomorrow.
So I am Umm Ghada, Mother of Ghada.
I live in yellow trailer
outside Amiriyya bomb shelter

I was inside
with nine from my family
talking, laughing
then such a pounding, shaking
everything is fire
I couldn't find my children
I couldn't find my way out

In the whole day later I am searching, searching charred bodies bodies they were fused together the only body I did recognize is my daughter Ghada so I did take her name [with so much pride] I am Umm Ghada, Mother of Ghada. TRANSITION Iraq is a world that exists far beyond what we see on our television screens. And since the early 1990’s the women of Iraq have borne often silent witness to all that has unfolded in the Middle East. Today their silence is broken by the voices of Umm Ghada, the caretaker of the Amiriyya shelter, now a museum to honor the dead; a doctor who has returned to her homeland to serve her people; and Huda, an elderly political rebel who fled Iraq during the time of Saddam Hussein. It is said that history is written by the victor. But perhaps, just perhaps, history is a compilation of many realities.

THE DOCTOR: (Pg 20-21) [nauseated, she throws up; washes her hands, then dries them. She is exhausted] I'm sorry, it's probably just the smell of the sewage backing up in the ward. I feel fine, fine, let's go on, it's just . . . Damn it! I lost her, the baby should be dead, not her. God she had enough, she had three girls at home, but she insisted, hoping for a boy. What am I supposed to tell her husband? Here, it's your first-born son, sorry he has two heads?

More than ultrasound, incubators, Panadol, anything, I need some -- who can I ask? Just this month, I've started counting: six babies no head, four abnormally large heads, now today another one with two heads. Such high levels of genetic damage does not occur naturally. These things . . . you see them in textbooks.

HUDA: (Pg 19-20) Some in the opposition praise America one hundred percent
Personally, I have my doubts about American policy,
still I prefer chaos to permanent repression and cruelty
Saddam was the worst enemy to the people

He beheaded seventy women for being prostitutes, but he made them prostitutes.

Saddam’s stooges, they’d kidnap a woman
just going from her car to her house,
and take her as a slave, sex lave
or house slave when they were in their hideouts,
and when they’d finish with her
he would go to her family saying “She is a prostitute”
and he’d behead her and put her head in the street.
There was no law if you are a prostitute -- you are beheaded.
So, what chaos is worse then this?
Let it be chaos at least something will come out of it.

UMM GHADA: (Pg 29-31) [enters the shelter; it is the first time we see her subtle limp]
This is Amiriyya bomb shelter.
Here, on the ceiling, you can see
charred handprints and footprints
from people who lay in the top bunks.
And here a silhouette of a woman
vaporized from heat.
This huge room became an oven,
and they pressed to the walls to escape from the flames.
In the basement too
bombs burst the pipes
hot water came up to five feet
and boiled the people.
the walls are stuck with hairs and skin.

The U.S. said they thought this is
communication center for military.
Myself,
I think they were testing bomb --
these bombs had never been used before, but it is special
two-bomb design for breaking only a bomb shelter.

HUDA: (Pg 39-41) Let the young ones living there have a chance with the policies
but they are too afraid to speak up
they are shell-shocked, all these girls
they go backward
they abandon their education and now,
now they are wearing the veils.
Their grandmothers are more liberated than them.

I wanted, we all wanted Saddam to go during the Gulf War.
that was our moment – the people made this big rebellion --
sixteen of the eighteen provinces fell
and they were sure America would help them

But America turned its back. America made a no-fly zone
but when they saw Saddam going with his helicopters
to execute his own people
they allowed him to fly. It was a bloodbath,

Saddam killed tens of thousands, trucks full,
and buried them just mass graves.
Then the worst thirteen years’ suffering --
This what do you call it? Hisar? Embargo?

And it made Saddam stronger and the country more backward and religious.

THE DOCTOR: (Pg 21-22) And the cancers, I've never seen them before in Iraq, girls of seven, eight years old with breast cancer. I told this girl, ten years old, she came in, she thought her breasts were developing but it was only on one side. It was the cancer. But it's toddlers even with breast cancer, more than one cancer in the same patient, whole families all suffering from cancer –

And what can stop it? I mean the children, they play at the sites even when they're fenced off, they take the bullets to school to show their classmates what they collected from America. One came in wearing a bullet around his neck-a bullet tipped in depleted uranium around his neck.

It's in all the water, it’s in the food, but if it's airborne like they say -- It could be depleted uranium, or chemicals that were released from the bombings during the Gulf War. They say the radiation is at eighty-four times the safety limit. But who can clean it? Ever? We will have this depleted uranium for what-four thousand years? How many generations is that growing up handicapped?

It's better, maybe, death -- I don't care, honestly I don't care what I say. I'm a little ashamed of myself but it sickens me. We won't survive it, I won't, I'm a doctor, if I can't do anything. We all trained in the West, I could have been anywhere, I came back. We had the best hospitals in the Middle East, everyone was coming to us, and what are we now? We're the experiment.
```

---

## IC-0068: After the Wink

- Title: After the Wink
- Author (byline): Carolyn Steele Agosta
- Work: After the Wink and Other Stories (Pgs 1-7)
- Publisher: Carolyn Steele Agosta
- Publication date as stated: December 2011
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1794
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carolyn Steele Agosta
Book: After the Wink and Other Stories (Pgs 1-7)
ISBN: 978-0982956120
Publisher: Carolyn Steele Agosta
Date (Month/Year): December 2011
```

### Introduction (context only: never use it for content warnings)

```text
You know, sometimes a wink is really just a nervous tic, a sudden twitch of muscles contracted in error by a misguided neuron, an accident of synapses gone awry. The muscles keep twitching until something clicks over and they smooth out, like a skip in an old 45 rpm record, and everything goes back to normal. After the Wink by Carolyn Steel Agosta.
```

### Performance text (classify this)

```text
WOMAN: (Pg 1-7) It starts out so harmlessly. I don't really mean anything by it, I'm just in one of those moods. I mean, when you're 42 years old and have 3 kids and a husband and responsibilities, who figures on finding excitement, too? Other than bad excitement, like when you have to hit the brakes hard and all your blood vessels get a quick yee-ha. It's true, I've been noticing men a lot lately. Their arms, particularly. Don't ask me why, but I've suddenly become fascinated with men's arms. Forearms, lightly furred, with those lines of tendons and the swell of muscle below the elbow that women just don't have. And men's hands, square and capable. I see them everywhere. In restaurants, at gas stations, in the middle of the aisle at the freakin' K-Mart, for god's sake. It's embarrassing to know I'm lusting in Lawn & Garden. It's not just the young men either, mind you. I've been noticing older men, too. Men in their 40's and 50's, men who maybe think no woman is looking at them that way any more. Mostly I like the ones who still have plenty of hair and rugged looking faces, who look like they still get some, you know? Ponytails too, on older men, catch my attention. Here's a guy who thinks young, I figure. I could be wrong. Maybe he's just a guy who hates going to the barber.

WOMAN: Anyway, I'm sitting there at the coffee shop, I'm reading a book by Robin Hemley and it makes me laugh out loud. I look around to see if anyone notices and there's a man smiling at me. He's good-looking too. He's sitting at one of the tables, reading a magazine, and it's not just any magazine, not about motorcycles or computers or entertainers, it's the New Yorker. The guy's literate, for crying in the sink. I give him a little smile. Going back to my reading, I shift in my seat, cross my legs, straighten my back a little. Knockers up, my aunt used to say. I rest my chin on my hand, arching my neck a little. That's body language for "I'm interested". Or something like that. A customer near the front makes a huge mess by dropping her coffee, the tray clattering to the floor. I take a quick glance at Mr. Attractive and he's looking at me. So I smile. And then, God help me, I wink. Now it's just a little wink, just an acknowledgement that he's there and I'm there and we both see the humor of the situation and that, perhaps, we're somehow both a little more in the know than the average joker and already have this little connection, but that's all it is. I swear. But it's enough. Because next thing I know, he's picking up his coffee and his New Yorker and he's coming over to me, doing that little raised eyebrow thing to ask if he can join me and I'm nodding, nodding, thinking I don't quite believe this. He asks me about my book and I ask him about his magazine and I mention, modestly, that I'm a writer and he mentions, modestly, that he's a musician, and even though we're really a bookkeeper and a systems analyst, we understand that we're not defined by our paying jobs. I tell him my name and he tells me his and it's one of those names I always admired. He has a little bit of curly black/grey/white hair coming out of the collar of his shirt. His eyes crinkle at the corners and his forearms flex as he leans forward on his elbows to talk to me in low tones that require that I lean forward too. I smile to show my dimples and hope that I don't have coffee breath and we keep talking. About books and music and the theatre. About the way that parking is getting impossible in this town and how traffic is ridiculous. He mentions that he lives near South Park and I mention that I'm over by the university and pretty soon our coffee is cold and it's somehow gotten to be an hour later. It's really time for me to leave and he walks me to my car, which thank heavens is decently clean, with no McDonald's Happy Meal figures on the front seat. He mentions that he's going to the poetry slam next Friday because his friend is playing flute for some poet and I mention that I've never been to a poetry slam and he says I should try it. So I say maybe I will and I drive away with my hands perspiring on the steering wheel. I have no complaints about my husband, that has to be understood. He's loving and thoughtful and sexy and he picks up his socks and puts down the toilet seat. But on Friday night I'm at the damn poetry slam, trying to look like I'm enjoying it but really keeping an eye out for Mr. Handsome only I don't see him and feel like a fool and I'm just getting ready to leave (I mean it, I'm only giving it five more minutes) when he walks in. And he winks at me. The place is crowded and noisy, people are talking to each other and completely ignoring the woman in purple tights and purple hair who is bellowing some poem about spaghetti, and when he takes my elbow and leads me away to a quieter corner, a little thrill runs right up my arm. He asks if I want to get out of there and I nod and suddenly my knees are way too loose and I'm afraid that if I walk, they'll bend backwards, the wrong way, which would not be attractive at all. I manage to pull myself together and we get in our cars and I follow him to a bar, which is quiet and low-lit and has a nice band playing oldies. We talk and dance and his arms go around my waist, which has mostly been used to apron strings and babies' monkey legs and my husband's arms. Which are also nicely hairy and brown and have those good flexy muscles. Which I'm trying not to think about just like I'm trying not to mention that both Mr. Gorgeous and I are wearing wedding rings. Because we are, and we're not kidding ourselves that this is anything but an exercise in visibility.

You see, it seems to me that after 40, you become invisible. Oh, you're still there and people see you but they don't really SEE you. They see this person whose daughter is now an adult and whose mother is now a child and who's supposed to hold everything together. A person who couldn't possibly have desires and doubts and unfulfilled longings. A person who is still, improbably, perhaps imperceptibly, a person. I take a good look at Mr. Still-Has-It and I can see that he still loves rock'n'roll and still would look good behind the wheel of a Corvette and still has a bit of anxiety about how he looks to a younger woman. Which I am, to him. So I smile and flirt and he flirts back and it feel real good. We dance and I think about how strange it is to be in the arms of someone else, another man, a man who is a bit taller and bulkier than my husband, with a different voice and different lips and different eyes. It feels so weird, and then it feels even weirder when he kisses me, which he does, right there in the middle of the dance floor. I haven't kissed another man on the lips in over 20 years and now his mouth is on mine, and it's different, a different touch and taste and style. More than that, it's real, I'm really here and I'm doing this thing. I start to shake, start to vibrate like a tuning fork, until he probably thinks he's such a good kisser. I'm just shaking with fear because I realize that I'm thinking about a lot more than kissing and that scares the hell out of me. He laughs a little, softly, in a pleased sort of way, and I blush all the way to my fingernails, and we go back to the table. He's looking at me and I think, yes, look at me. I'm not ready to be old, to have all my fun behind me. I want to shimmy when I dance, and wiggle when I walk. I want a man to look at me and get a little yee-ha of his own. Then I begin to think that maybe this is why people cheat in the first place. To have this warm glow that comes from someone else's eyes. To remember who they are and not to be the person that everyone thinks they are and, a little bit, not to be the person they know they are.

I look at him too. I see a man who's just as scared as I am of becoming invisible. Or being seen as past it, on the far side of manhood, as being old. So I reach across the table and take his hand (good hands, wide and blunt-fingered, the hands of a man who can fix things). I stroke his wrist and tell him without saying it that he's still pretty sexy-looking and makes my mouth water. I think about all the things I've never done and all the things I'll never be, and I wonder if it's too late. A rush goes through me, starting with my lips, making them feel warm and full, and I think, damn, what a hell of a time for my first hot flash. But it's not a hot flash. It's the realization that I'm not going to do a thing. Because among all those things I wanted to do with my life, this wasn't on the list. I give Mr. It-Might-Have-Been a quick kiss on the cheek. I'll have daydreams for a while about him, play with thoughts that should send me to confession, and keep the memory of his kiss for those days when I can't jump-start my own desires. I drive home and sit for a moment in the car, looking up at the light in the bedroom window. You know, sometimes a wink is really just a nervous tic, a sudden twitch of muscles contracted in error by a misguided neuron, an accident of synapses gone awry. The muscles keep twitching until something clicks over and they smooth out, like a skip in an old 45 rpm record, and everything goes back to normal. The way it should be, I guess. The way it is. The way the music plays best.
```

---

## IC-0069: Aftermath

- Title: Aftermath
- Author (byline): Jessica Blank and Erik Jensen
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Sept 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SHAHID, BASIMA
- Teaser before the introduction: Yes
- Spoken words (computed): 1695
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jessica Blank and Erik Jensen
ISBN: 978-0822224303
Publisher: Dramatists Play Service
Date (Month/Year): Sept 2010
```

### Introduction (context only: never use it for content warnings)

```text
March 20, 2003 - American missiles hit the Iraqi capital, Baghdad, signaling the start of the US-led campaign to topple Saddam Hussein. President George W. Bush called the war in Iraq "one of the swiftest and most humane military campaigns in history." Yet thousands of Iraqi civilians were killed or injured during the three weeks of fighting from the first air strikes on March 20 to April 9, 2003, when Baghdad fell to U.S.-led Coalition forces.

As Americans watched the war unfold on television, the human factor of the Iraqi people became lost. This selection brings voice to two average citizens who were trapped in the war zone of Baghdad in 2003: Shahid, a young translator in his mid-twenties and Basima, a wife and mother. Both were overwhelmed in the . . .

Aftermath by Jessica Blank and Erik Jensen.
```

### Performance text (classify this)

```text
Pacing of this selection should be slow “Shell-shocked” – The American missiles were completely unexpected by the citizens of Iraq.

SHAHID: Under Saddam, it’s not like we all walked down the streets of Baghdad in grey suits, like, grim faces, heads hanging down. We’re Iraqis, we’re not Russians. But we knew where the red lines were. We knew what would upset who. . We know that if we kept our nose off politics, if we didn’t insult Saddam, then: “happily ever after” We had some space.

BASIMA: (Lights up on Basima, early thirties, sweet and a big shy. A loose scarf over her hair. She wears a cross) Anee Basima Jabar / Ummi hinana, hem, bes ma tehchi / My mother doesn’t want to come out – Her brain injury, you know. She made us some coffee, though. Unless you’d prefer – (Smiles) Okay. So, we’ve been in Jordan almost two years now.

Back in Iraq, growing up, our life was sweet: big house, school, ya3ni, mother, father, kids, normal everyday things. Once, when my father was at work, my sister and I called and said the house is on fire, hurry up, come home! And he “buh buh buh buh” comes home like he’s on fire, and he says, “There’s nothing wrong with the house! What have I told you about lying?” My sister and I said, “We just missed you.” Many fathers would get angry, but ours just laughed. The best was Christmas. Even a month before, we would be getting the tree ready. Lights, ornaments, teddy bears, Papa Noel. In the morning all our cousins would come – so many. Second cousins, third cousins, fourth cousins. And, you know, one of those cousins I wound up marrying. (Confiding) We had a -- (To Shahid) Il hub il awal

SHAHID: Oh, ah, um – (to us) A Crush

BASIMA: (Nods) – since childhood. Sometimes he’d come by: “I saw this girl and I saw this other girl.” I’d get so jealous that I’d break things in the house! During the engagement, that whole year you can’t imagine all the things I broke because of him. Should I show you guys his picture to see? (Pulls a picture from an envelope) I was pregnant in this picture. (Looks at the photo) He’s got a beautiful face, eh?

SHAHID: Saddam’s religion was loyalty. He killed many many people because of this. He even killed his own brother-n-law when he opposed him. If Saddam appeared on TV, the father couldn’t say anything bad, because his son might say something in school. See under Saddam, the father was even afraid of his own son. Everyone was watching everyone. And everyone knew he was being watched

BASIMA: I think – most Americans don’t know what a bomb sounds like. You don’t feel your eardrums, from the sound, ya3ni. Every explosion we thought the world would crumble on top of us. Every strike . . . is an earthquake. For nine days, the whole family hid out in one room with no windows. And then, when we finally went out again – (Beat To Shahid) Mah agdar awsuf shikilha, reehatha, goolelhum, (I can’t describe what it looked like, the smell) tell them, okay –

SHAHID: Ma tigdareen tuwasifeen il – (You want me to describe the?) (In English) Okay. (To us) You know, the streets were full of corpses. People couldn’t stand the stench, so they started to dig, right in the dirt, wherever they could, to bury people wherever they were laying. You know, the Iran-Iraq War, the Kuwait War, they weren’t in the cities; men went away to fight. It was “over there.” But here – the smell – (Beat) You don’t get that from TV. Imagine: Iraq has been isolated for decades, it’s the first time most Iraqis see foreigners. People started coming to Baghdad from all over the world: not just soldiers, ya3ni: journalists, humanitarians, et cetera.

BASIMA: In the beginning, we would find letters in the garden. They would say, “This is an Islamic country. You Christians are not welcome here.” It’s in an envelope, sometimes typed, sometimes handwritten. No name, no signature, but there’s a bullet with it. But, ya3ni, threatening letters were so widespread at the time. You know, this was normal. And we couldn’t flee like, come to Jordan, or Syria, or something – you can’t just pick up the pieces and do that. I mean, we’re seven of us and I’m pregnant. We didn’t think that it would get to the point of . . . (She trails off)

SHAHID: Me, personally I became a refugee at the end of 2005. I left after I was kidnapped by the police. Don’t be nervous; not American police – Iraqi police. Still nervous? (Beat) Okay, “Iraqi police,” let me explain. When the American army first cam, they dismantled all the Iraqi army and police, leaving a void. Then, they appointed a governing council made of two parties that had been outlawed by Saddam. So these parties put their militias in uniform, and they called them the “Iraqi Police.” If they want, they could take you, beat you, whatever. All using the police uniform and official mechanisms. (Beat) So, there are two kinds of gangs in Iraq; there are non-governmental gangs and there are governmental gangs. You know not everybody got along all the time. Saddam had exploited these – undercurrents, between people, for twenty-five years. And the Americans – they don’t understand all these splits: Sunni, Shi’a, Jewish, Christian, Kurd. Our humanity is drifting from their humanity in four or five different directions. So far that you can’t reach either side. If it means your life, at some point, you can’t keep a foot on both banks. Everyone’s pulling at you to make a choice: this side, that side, or you drown (Pause) This seems to me an unnatural way to live.

BASIMA: I gave birth in July. Our first child. And when he was two months old, it came time for us to get him vaccinations. (Long beat) So – we were on the way to the doctor’s with the baby. Everyone came in the car, me and my husband and my mother and my son and my sister – because my sister was just seventeen, we couldn’t leave her alone in the house, someone, the militias . . . could come into the house and . . . (She can’t say it) . . and hurt her. In the car, we were all just happy with the baby and fussing, would this vaccination go okay, would he cry, would he feel better. And then, all of a sudden – ya3ni, sound, and heat, lots of heat. And the smell of burnt hair and flesh. And pain. The car shook, hard, and right away I lost my sight. I don’t know how I got out of the car. I couldn’t see. The thing I could hear most was the sound of my husband’s voice. I just followed the sound back to him.

He wanted to get out of the car but his legs were fused to the seat. I tried to get him out, but he was heavy, I couldn’t I couldn’t. I felt the fire start to eat at my hands I tried to get him out, I tried, but I couldn’t (Beat) So I left. I called for whoever could help me. I was yelling at the top of my lungs. But there wasn’t any person, there wasn’t anybody. It was as if the world had ended. And then another explosion, and screaming and yelling. And then my husband’s voice disappears. I hear bullets from every direction. And I’m barefoot, and I can’t see and I don’t know what to do so I just sit down. There’s nobody there. Nobody nobody. It is as if Baghdad has been emptied of people. Of course, you know, this accident was on television. They showed me like – my blouse was open. My clothes were burned off. And I’m asking, what happened where’s my husband, my son, my mother, my sister. One Muslim guy, do you know what he says to me? He says (Clearly mocking) “They went to Allah.” From ten-thirty ‘til twelve-thirty I was in the street. After two hours I heard the blades of a helicopter. Americans came, they were speaking English. They were checking out what the car bomb was. It was a long time ‘til they came to me. I was secondary. But whatever I can say about the . . . accident wouldn’t be enough. (she needs a break)

SHAHID: Iraq had been at war, more or less, for the last twenty-five years. With Iran, with Kuwait, with Saddam, the sanctions, now . . . daily bombings. Daily. Everyone in the county has traumatic stress. It’s normal IF everyone has the problem, it’s not really a problem, is it? It’s just life.

BASIMA: At the hospital, I keep asking where my family is. Because the guy in the street that said they “Went to Allah,” he was kind of talking out of his ass, you know. When I would regain consciousness, I felt myself sticking to the sheets. I didn’t have any skin. I was naked, I didn’t have clothes on. I would find pieces of shrapnel in the bed. They came out when I was sleeping, ya3ni? My whole body was shrapnel. My hands, my shoulders, my face. This eye has a piece of metal in it still, but this one they fixed. So I would go into the bathroom and catch myself in the mirror. And I would be afraid of my own face When I would wake up I would ask my father, how is everyone? Where are they? What’s the news? He would say, “They’re fine. Your mom’s right next to you, you see her, right there.” He would laugh and tell stories, keep me happy. He’d say –

SHAHID: “Zoujich, ibnich wa ukhtich – Il Amrikan akhtouhum ila mustashfa ahsan / Sema3tee il Helicopter.”

BASIMA: (Overlapping) “Your husband, your son and your sister – the Americans took them to a better hospital. You heard the helicopter. . . Real bullshit, ya3ni. After a while, I stopped asking, so I could just stay in the story he was telling me. But after a month and a half I couldn’t take it anymore. I needed to know. My father was holding it all so it wouldn’t show, because I was getting my strength from him. But the second I found out the truth – my sister, my husband, my baby – my father broke down. I don’t blame my father, though. I was the one what wanted him to lie to me.

Ya3ni when it’s Christmas now I remember how we used to be, and it – (Beat) I don’t celebrate anymore. We have left everything behind: our kings, our stories, our possessions, our wealth. I have been – we have been – inthulmat -?

SHAHID: Darkened
```

---

## IC-0070: Age of Consent

- Title: Age of Consent
- Author (byline): Peter Morris
- Work: Not specified
- Publisher: Methuen Publishing, Ltd
- Publication date as stated: Sept 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: STEPHANIE
- Teaser before the introduction: No
- Spoken words (computed): 1990
- Already set (do not supply): none

### Source block (context only)

```text
Author: Peter Morris
ISBN: 978-0413771865
Publisher: Methuen Publishing, Ltd
Date (Month/Year): Sept 2003
```

### Introduction (context only: never use it for content warnings)

```text
Drew Barrymore, Lindsay Lohan, Miley Cyrus . . . all child stars who entered the world of entertainment early and effectively gave their consent to a life that no child should have to experience. Their parents traded their childhoods for fame and fortune, but at what expense? In Age of Consent by Peter Morris, Stephanie is an abusive mother who is bound and determined to climb the showbiz ladder on the back of her six-year-old daughter, Racquel. It seems Stephanie is willing to sacrifice everything for stardom . . . even to the point of delivering her daughter into the hands of a pedophile. Can a child ever give their consent to be judged and treated as an adult? Age of Consent by Peter Morris
```

### Performance text (classify this)

```text
STEPHANIE: I don’t want to overstate my case here, nor do I want to whinge (whine). But it must be said, it’s not easy to be a single mother. Especially at my age. I mean, I was nineteen when I had her. I’ve no family to speak of, to lend a hand in raising her, and as for being a single mummy, the gentleman in question seemed to think of his role largely in terms of anonymous sperm donation, conducted under slightly less hygienic conditions than usual. The silence from that man is deafening and, to be fair, I’m not really sure where he is now.

But what it comes down to is money, right. And that’s when I started thinking . . . child-rearing, such as it is . . . you’ve just got to be firm and communicate in one-syllable commands, and then the rest of it’s down to breeding and grooming. I mean, not that Raquel is dog-like in any way, but let’s face it. Child Stars, yeah? The only difference between a prize poodle and [a child star] is the length of the ringlets. With some discipline I could put Raquel’s natural maturity and outgoingness to a good use. I mean, I want Raquel to be the best she can be.

So I made the decision. I quit my job to concentrate on Raquel’s career. Although, as her agent, and manager, it has to be said that I’ll always be working harder than she does; but you have no idea how energized I am. I am completely happy spending my days teaching Raquel to sing and to dance. I finally feel like a mother.

Raquel, with only a minimum of coaching from me, rally – she’s a natural – got cast as the littlest Darling sibling in Peter Pan! I have taught her to steal a scene so gracefully that you don’t even see her doing it. A chill went over me, as I stood in the wings, as Raquel waited to enter. I didn’t even smile as I leaned down and whispered into her ear: “T and T, Raquel.”

And she just looks up at me and whispers, “Teef and tits, Mum, teef and tits!” (page 3) So she grins. And thrusts. And then she enters. And all eyes are on her.

************

Princess Raquel and I are not currently speaking. She’ll come round. Anticipating their misbehavior is part of the training. Then, when it occurs, you just starve them into submission. I mean, I don’t know what Princess R had to eat today, but there’s no food in the house. I don’t feel guilty. Give that girl an inch and she takes a mile. You could say she’s spoilt. But if I have spoilt her, it’s only because it’s part of the plan.

See, I take Raquel to places that are to la-di-da for us, really. But what I’m hoping to do is to force her to acquire the taste for it. So that then she has to work harder, for the rest of her life, to satisfy that craving. I gather that’s the way international drug dealers operate. It’s not like I fritter away the money she’s earning. But if you let it sit in the bank it does take the edge off, doesn’t it? She needs a reason to get out of bed in the morning. She’ll be a much more eager performer if she has to sing for her supper, essentially.

But she’s become so . . . gloomy, lately. I don’t understand it. I wonder if it’s overwork. I’d suspect it was overwork, only I maintain a far more punishing schedule than she does. I’m the one who’s responsible for every appointment, every meet-and-greet, every audition that she ruins for us, by refusing to sparkle. Raquel and I get into these . . . stand-offs, really. It just feeds on itself and gets worse and worse. Because I will take her in for our first audition of the day, and she’ll already be in a bad mood, and then she’ll bollocks (screw) up the audition and that makes me livid, and so we just end up like now. It’s no surprise that we aren’t speaking.

I mean, today was unforgivable really. They’re changing casts, right? In Les Miz. And you can’t imagine how hard I fought to get the audition. I coached Raquel into poignant perfection, with choreography and everything . . . (She sings, with her own choreography)

There is a castle on a cloud, I like to go there in my sleep, Nobody shouts or talks too loud . . . *

I mean, you know the show. And that’s what I said to Raquel before she went on, I said, I want you to make them weep -- I don’t want there to be a dry seat in that your when you’re through. And I gave her a Chinese burn and pushed her on to the stage.

And she was . . . spellbinding. Little hairs on the back of my neck standing up. And I realized that Raquel does honestly, honestly have what it takes. . . Until the last verse. When she actually started to cry, and it was a nice effect, but then she stopped singing and just started saying “Mummy, Mummy” . . . and it just . . . evaporated. That magic. It’s clear that she’s not really a pro. She’s only six, but if she can’t do it now, when is she going to do it? That’s what enrages me. I mean, here she is, she sings that song like the world is going to end . . . then she starts crying for her mummy! Raquel ruined it for herself. I was just mortified. So when we got out the stage door, I pulled her aside and said, “Raquel, I can’t have you calling me mummy in front of all those professionals. Stop letting me down and maybe I’ll want to be your mummy, you spiteful little bitch.”

She says, “Fine, I don’t want to call you Mummy anymore.” So I said, “Well, I am your mummy and you’ll call me Mummy when I tell you to.” I slapped her cross the face and she fell over. She didn’t cry, though. I mean, I am proving that she has nerves of steel, ‘cos she didn’t even bat an eyelid. Six years old, can you believe it?

**************

I don’t know what’s got into her. Things just get worse and worse. I don’t know what side of the nature-nurture debate this will put me on, but I now have definitive proof that a six-year-old girl can be a raging hysterical bitch. Terrifying. And the only thing that runs through my head is, bloody hell, she doesn’t even have hormones in her yet. I might need to have her put down for the public good in a few years.

And her latest technique? For domestic terrorism? Wetting the bed. It’s absolutely foul. This is the third time we’ve had it this week, so now I’m simply refusing to change the sheets. I mean, that’s not normal, is it? It’s ingratitude, is what it is. And as far as I’m concerned, ungrateful little girls have made their bed to lie in.

*************

For the first time I’m thinking it might be possible . . . that dreams might actually come true! Raquel and I have now learned there is a God and his name is Desmond Varady. [We] just happened to be sitting on the grass in a little park. When I want to sun myself, I bring her along and she plays in the dirt or something. And we were sitting there, when a distinguished-looking older man came strolling up and just started . . . looking at Raquel. And she didn’t even look her best. That’s star quality. And then he said to me, “Madam, you have a beautiful daughter.” So I shook his hand and said, “Dunn, actually, Miss Stephanie Dunn, and this is Raquel.” And then he reached into the pocket of his suit and extracted a business card . . . Desmond Varady. Director. Film and Television. And I though, hell, this is the answer to our prayers, he’s a bloody director! And before I know, Mr. Varady has cast Raquel as the featured role in a Persil advert (commercial)!

In the studio, I had girls in sleek black jumpers bringing me espresso. Someone even massaged my shoulders. And Mr. Varady was so attentive to Raquel. And the money! Let’s just say the contract was very, very generous. And says Des, he’d very much like to work with Raquel again. Make her part of his stable, he put it.

When we first go to the studio, I had to fill out a whole sheaf of forms giving my permission for Raquel to be filmed. Finally I get to a sheet that says “Consent.” As in parental consent. But I said, “Ooh, Mr. Varady, does this have something to do with the age of consent? Because I’m not as young as I look, you know.”

And Mr. Varady took my hand, and tickled his fingers across my palm, and he smiled and said, “Miss Dunn . . . we’re living in an age of consent.” I’m sure I don’t know what that means, but he certainly has lovely teeth.

***************

Imagine raising your child so well that she responds to your demands before you make them. Imagine being so successful as a parent that you find your little ones start becoming, slowly and silently, what you want. I had been so angry with Raquel. The number of things she did for sheer spite, like talking back, and the [wetting the bed] pissing. But now . . . she’s like a dream of perfect obedience. When we did our next advert [commercial] with Desmond, this time for Toys ‘R’ Us, she didn’t say a word the whole time. Apart from her lines. It’s like she’d finally understood what I wanted from her. And Desmond, well, he’s perfectly enchanted with his little leading lady. He said to me, “Miss Dunn, you realize that I intend to continue using your daughter indefinitely. Provided that she and I can maintain the proper working relationship we now enjoy.”

So I sat her down when we got home and I said, “I know you get it in your head to be Little Miss Contrary sometimes, but don’t you dare. Mr. Varady can make us rich. So you do whatever he asks. He tells you to jump, you say how high.” Raquel didn’t say anything. Didn’t even nod. But I knew she understood.

And [then] we had Raquel filming a spot for Sunny D in Tuscany! They even flew me out. Raquel flew business class with Desmond. I sat in economy – but it’s all right. I said to Desmond in the evening as we waited out on the terrace, and Raquel was taking a bit too long in the bathtub for my liking. Thinks she’s a star now. I said to Desmond, “This is a country for romance. A passionate man like you. I know you feel it. “ And he said, “Miss Dun. Passion is the air I breathe.” [Then] Raquel turned up and was staring at us, in that way she has these days, kind of accusatory and macabre, popping her eyes at you.

This morning they decided not to film for some reason, [so] Desmond comes up, carrying a small hamper, and says, “Miss Dun . . . where’s Raquel?” She was hiding under the patio table, so we fetched her out and Desmond said, “Little lady, I’ve come to invite you for a picnic.” Raquel seemed a bit reluctant. And off they went. I think he knows a good thing when he sees it. He can’t stop praising Raquel. And as I watched them walk down to his car, him with the picnic hamper, and her with her little hand reaching up to clutch his pinky finger, I just thought . . . He’s done so much. I know I’ll never forget this man. And Raquel won’t forget it either.

As for now. . . You have no idea how nice it is to be alone.
```

---

## IC-0071: Agnes of God

- Title: Agnes of God
- Author (byline): John Pielmeier
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: June 1982
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: AGNES, DOCTOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1609
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Pielmeier
ISBN: 978-0573630224
Publisher: Samuel French, Inc.
Date (Month/Year): June 1982
```

### Introduction (context only: never use it for content warnings)

```text
Agnes of God by John Pielmeier
```

### Performance text (classify this)

```text
AGNES: (singing off stage) *Gratias agimum tibi propter magnam gloriam tuam. Domine Deus. Rex coelestis. Deus pater omnipotens. Domini Fili unigenite. Jesu Christe

DOCTOR: (Pg 3-4) (Speaking over Agnes) The baby was discovered in a wastepaper basket with the umbilical cord knotted around its neck. The mother was found unconscious by the door to her room, suffering from excessive loss of blood. She was indicted for manslaughter and brought to trial. Her case was assigned to me, Doctor Martha Livingstone, as court psychiatrist, to determine whether she was legally sane. I wanted to help this young woman, believe me . . .

DOCTOR: (Pg 17) Hello. I’m Doctor Livingstone. I’ve been asked to talk to you. May I?

AGNES: (Pg 20-22) You want to talk about the baby, don’t you?

DOCTOR: Would you like to talk about it?

AGNES: I never saw any baby . . . I think they made it up.

DOCTOR: Do you remember the night they said it came? Did it hurt?

AGNES: Yes.

DOCTOR: Where did the baby come from?

AGNES: They say it came from the wastepaper basket.

DOCTOR: But where did it come from before that?

AGNES: From God.

DOCTOR: After God, before the wastepaper basket.

AGNES: I don’t know what you’re talking about! Everybody wants to talk about the baby, but I never saw the baby, so I can’t talk about the baby, because I don’t believe in the baby! Nobody listens to me! (Silence) (Pg 24) Where do you think babies come from?

DOCTOR: From their mothers and fathers, of course. Before that, I don’t know.

AGNES: Well, I think they come from when an angel lights on their mother’s chest and whispers into her ear. That makes good babies start to grow. Bad babies come from a fallen angel. (Silence) Bad babies cry a lot and make their fathers go away and their mothers get very ill and die sometimes. Mummy wasn’t very happy when she died and I think she went to hell. (Silence) (Pg 33) But she watches. She listens.

DOCTOR: (Pg 42-46) Agnes, have you ever thought of leaving the convent? For something else?

AGNES: Oh no. There’s nothing else. It makes me happy. Just being here helps me sleep at night.

DOCTOR: You have trouble sleeping?

AGNES: I get headaches. Mummy did too. She’d lie in the dark with a wet cloth over her face and tell me to go away. Oh, but she wasn’t stupid. Oh no, she was very smart. She knew everything. Things nobody else knew. She told me I would enter the convent, and I did. She even knew about this.

DOCTOR: How did she know . . . about this?

AGNES: Somebody told her.

DOCTOR: Who?

AGNES: You’ll laugh.

DOCTOR: I promise I won’t laugh. Who told her?

AGNES: An angel. When she was having one of her headaches.

DOCTOR: Do you believe that your mother really saw them?

AGNES: No. But I could never tell her that. She’d get angry. She’d punish me.

DOCTOR: How would she punish you?

AGNES: She’d . . . punish me.

DOCTOR: Did you love your mother?

AGNES: Oh, yes. Yes.

DOCTOR: Did you ever want to become a mother yourself?

AGNES: I could never be a mother. I don’t think I’m old enough. Besides, I don’t want a baby.

DOCTOR: But if you did want one, how would you go about getting one?

AGNES: From someone who didn’t want a baby.

DOCTOR: Like you?

AGNES: No! Not like me. A mistake.

DOCTOR: How did your mother get you?

AGNES: A mistake! It was a mistake!

DOCTOR: Is that what she said?

AGNES: You’re trying to get me to say that she was a bad woman, and that she hated me, and she didn’t want me, but that is not true, she was a good woman, a saint, and she did want me. You don’t want to hear the nice parts about her—all you’re interested in is sickness!

DOCTOR: Agnes, I cannot imagine that you know nothing about sex. . .

AGNES: I can’t help it if I’m stupid.

DOCTOR: . . . that you have no idea who the father of your child was . . .

AGNES: They made it up! It’s not my fault!

DOCTOR: . . . and that you don’t believe that you carried a child!

AGNES: It was a mistake!

DOCTOR: What, the child?

AGNES: Everything! Nuns don’t have children!

DOCTOR: Agnes. . .

AGNES: Don’t touch me like that! Don’t touch me like that! (Agnes lashes out at the doctor, who moves away) I know what you want from me! You want to take God away. You should be ashamed! They should lock you up. People like you! (Long beat)

DOCTOR: (Pg 55) (to audience) I wanted to free Agnes – I wanted to make her well.

AGNES: I’m not sick!

DOCTOR: (Pg 57-62) But you’re troubled, aren’t you?

AGNES: That’s because you keep reminding me. If you go away, then I’ll forget.

DOCTOR: And you’re unhappy.

AGNES: Everyone’s unhappy! You’re unhappy, aren’t you?

DOCTOR: Sometimes, yes.

AGNES: Only you think you’re lucky because you didn’t have a mother who said things to you and did things that maybe weren’t always nice, but that’s what you think, because you don’t know that my mother was a wonderful person, and even if you did know that you wouldn’t believe it because you think she was bad, don’t you?

DOCTOR: Agnes.

AGNES: Answer me! You never answer me!

DOCTOR: Yes, I do think your mother was wrong, sometimes.

AGNES: But that was because of me! Because I was bad, not her!

DOCTOR: What did you do?

AGNES: I’m always bad.

DOCTOR: What do you do?

AGNES: (in tears) I breathe!

DOCTOR: What did your mother do to you? (No answer) If you can’t tell me, shake your head, yes or no. Did she hit you? (Agnes shakes her head “No”) Did she make you do something you didn’t want to do? (Agnes nods“Yes”) Did it make you uncomfortable to do this? (Agnes nods“Yes”) Did it embarrass you? (Agnes nods“Yes”) Did it hurt you? (Agnes nods“Yes”) What did she make you do?

AGNES: No.

DOCTOR: You can tell me. She’s dead. She can’t hurt you anymore.

AGNES: She can. She watches, she listens.

DOCTOR: Agnes, I don’t believe that. Tell me. I’ll protect you from her.

AGNES: She. . . makes me. . . take off my clothes and then. . . she makes . . . fun of me.

DOCTOR: She tells you you’re ugly? (Agnes nods“Yes”) And that you’re stupid.

AGNES: Yes.

DOCTOR: And you’re a mistake.

AGNES: She says. . . my whole body. . . is a mistake. She says. . . if I don’t watch out. . . I’ll have a baby. And then. . . she touches me down there with her cigarette. (Silence) Please, Mummy. Don’t. I’ll be good, I won’t be your bad baby anymore. (Silence)

DOCTOR: Agnes, dear, I want you to do something. I want you to pretend that I’m your mother. Only this time, I want you to tell me what you’re feeling. All right?

AGNES: I’m afraid.

DOCTOR: (She takes Agnes’ face in her hands) Please. I want to help you. Let me help you. (Silence) Agnes, you’re ugly. What do you say to that?

AGNES: I don’t know.

DOCTOR: Of course you do. Agnes, you’re ugly. What do you say?

AGNES: No, I’m not.

DOCTOR: Are you pretty?

AGNES: Yes.

DOCTOR: Agnes, you’re stupid.

AGNES: No, I’m not.

DOCTOR: Agnes, you’re a mistake.

AGNES: I’m not a mistake! I’m here, aren’t I? How can I be a mistake if I’m really here? God doesn’t make mistakes. You’re a mistake! I wish you were dead! (shocked silence, then Agnes begins to cry. The doctor takes her in her arms)

DOCTOR: Agnes, I’d like to ask a favor of you. You can say no, if you don’t like what I’m asking. I’d like permission to hypnotize you. There are some things that you might be able to tell me under hypnosis that you aren’t able to tell me now. (to audience) The hypnosis took weeks to achieve, not minutes. An hour a day . . .

AGNES: (Pg 77-79) I’m frightened!

DOCTOR: Don’t be. I cannot make you say or do anything you do not wish to say or do. Sit back and relax. Imagine that you are listening to a chorus of angels. Breathe freely and deeply. Close your eyes, Agnes. When I count to three, you will wake up. Can you hear me?

AGNES: Yes.

DOCTOR: Good. Would you like to tell me why you’re here?

AGNES: Because I’m in trouble.

DOCTOR: What kind of trouble?

AGNES: (Agnes struggles, then says) I had a baby. I was afraid.

DOCTOR: Why were you afraid?

AGNES: Because I wasn’t worthy.

DOCTOR: To be a mother?

AGNES: Yes. (she begins to cry softly)

DOCTOR: (Pg 81-83) All right, Agnes, I’m going to ask you to open your eyes. When you do, you will see your room at the convent. It is the night about four months ago when you were very sick. All right, Agnes, let’s go to your room. Ready? What do you see?

AGNES: My bed. A crucifix.

DOCTOR: Anything else? (Silence) Agnes? What do you see? Something different? Something that’s not normally in the room?

AGNES: A wastepaper basket. (Silence)

DOCTOR: Do you know who put it there?

AGNES: No.

DOCTOR: Why do you think it’s there?

AGNES: For me to get sick in.

DOCTOR: Are you ill?

AGNES: Yes. (Pg 84-85) Oh God! (she holds her stomach in a contraction) Oh my God. Water. . . it’s all water!

DOCTOR: Why doesn’t anyone come?

AGNES: They can’t hear me. Get away from me. Go away! I don’t want you here!

DOCTOR: Is someone in the room with you? Agnes?

AGNES: Don’t touch me! Don’t touch me! Please! Please don’t touch me! (Contraction) You want to hurt my baby! You want to take my baby! (Screams and contraction) It’s not my fault, Mummy. It’s a mistake, Mummy. (Pg 105) Your fault! It’s all your fault!

DOCTOR: (Pg 85) Agnes, it’s all right. It’s all right. It’s me. Doctor Livingstone. It’s all right.

(Agnes relaxes)

AGNES: (Pg 105-108) (softly) I hate him. I hate him for what he did to me.

DOCTOR: Tell us who he is so we can find him and stop him from doing this to other women. Who did this to you?

AGNES: God! God did it to me! It was God! And now I’ll burn in hell because I hate Him!

DOCTOR: Agnes, you won’t burn in hell. It’s all right to hate him. (beat) Agnes, what happened to the baby? It was alive, wasn’t it? Wasn’t it?

AGNES: YES!!! (Silence) I don’t want to remember.

DOCTOR: Mother Miriam was with you, wasn’t she? You saw it all, didn’t you? (no response) What did she do? (Silence) Agnes, what did she do?

AGNES: (Simply and quietly) She left me alone with that little. . . thing. I looked at it and thought, this is a mistake. But it’s my mistake, not Mummy’s. God’s mistake. I thought, I can save her. I can give her back to God. (Silence)

DOCTOR: What did you do?

AGNES: I put her to sleep. I tied the cord around her neck, wrapped her in the bloody sheets, and stuffed her in the trash can.
```

---

## IC-0072: Aimee

- Title: Aimee
- Author (byline): Mary Beth Miller
- Work: Not specified
- Publisher: Dutton
- Publication date as stated: May 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ZOE, AIMEE
- Teaser before the introduction: Yes
- Spoken words (computed): 1688
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mary Beth Miller
ISBN: 978-0525468943
Publisher: Dutton
Date (Month/Year): May 2002
```

### Introduction (context only: never use it for content warnings)

```text
Aimee by Mary Beth Miller
```

### Performance text (classify this)

```text
ZOE: I don’t know if I can [talk] about what happened and come out whole – alive. I don’t know if I can look back. Besides, if I tell it, who will listen? No one believes us – the kids, that is. They all think we have it so great and that this is the best times of our lives. When people tell me that, I want to puke. If this is the best time of my life and I’m going to spend the rest of my life looking back at this, then I should just end it all right now. (long beat) Oh, Aimee, I didn’t mean that. . . I’ll start with the way it was. . .

ZOE: She stared out the window and blew a long trail of smoke that floated from her lips to her hair, then spread into the air, thin curls of smoke heading for the crack in the window. (to Aimee) Is it worse lately?

AIMEE: What?

ZOE: You know

AIMEE: Say it.

ZOE: (to audience) I froze, unable to speak and stared at her. Even then I couldn’t say the important things. I couldn’t face ugly truths. Aimee had never really been explicit about what happened in her house. She dropped hints, but she never said outright what was going on. She and her stepmother didn’t get along, that I knew. In front of people, her stepmother was as nice as sugar, but I had always known she abused Aimee. But now, as I looked at Aimee’s eyes – her cheeks – her shaking hands, I wondered if I knew anything.

AIMEE: What do you want to know? The details?

ZOE: No, Aimee. I thought she knocked you around. Hit you, stuff like that.

AIMEE: Yeah, she does if I don’t do what she says.

ZOE: Does she say mean things?

AIMEE: Don’t all parents?

ZOE: Aimee, don’t you want to talk about it?

AIMEE: You know what I want to talk about? I want to talk about my cat. And you know what? No one wants to talk about her. ‘She’s just a cat.’ ‘You can get another one.’ No one says ‘Wow! You and that cat go back a long way. She remembers what it was like before, when your real mother lived with you, when your dad didn’t walk around with blinders on, when you knew you were safe in your own bed. She slept with you night after night . . . soothing you even when your parents fought. And when your mother left? When she ran off? Did your cat try to tell you that everything would be okay? Did she act like nothing bad had happened? Tell me that!

ZOE: (to audience) She stopped, her shrill voice echoing. She looked at me for a long time before she fell against me and cried. I rubbed my hands up and down her back. She rocked with me a while, then she stiffened.

AIMEE: (stiffening) Don’t touch me.

ZOE: Her voice came from some inner place I had never glimpsed. (to Aimee) What does she do to you, Aimee. Tell me. (to audience) She needed to say it. Her eyes were hollow, empty of feeling. There was something dead inside her, something cold and frozen that never felt the heat of anything. She hid it most of the time. But it was the only thing in her eyes when I asked my question.

AIMEE: Nothing that unusual. Lots of girls do it. It helps them when they get married.

ZOE: (to audience) She sounded strange, so far away – not in distance, but in time. She sounded young, childlike. Images I’d never dreamed of tumbled from her lips, of her stepmother and her . . . “games.” “Games” she called it when Aimee was young, then “preparation.” Now she used threats – that she’d tell Aimee’s dad about it, that she’d touch her brother like that. Threats Aimee knew were real. Because Aimee had seen her destroy her family, had seen her drive her mother away across the county, had seen her steal her brother’s affection from her, had made Aimee into a problem child for her father. And all the while her stepmother remained an icon of her church, her community her family.

No one would believe Aimee. Not a soul. Things like that don’t happen. Things like that never happen, especially in families like theirs. There was no physical proof. There wouldn’t be semen to test for. Was there any way to test for female stuff? Secretions? Probably, but that would mean telling, and Aimee’s empty face told me that she wasn’t going to do that. (to Aimee) So what do we do?

AIMEE: What I’ve been trying to do all along. Die.

ZOE: (to audience) My mind always stops when I remember her simple response . . . “Die.” It’s too hard to face. I didn’t have the energy for this, not tonight, not ever. I pulled the spread off the other bed and covered her up. “Sleep,” I said. I turned off the light and lay down on the empty bed. Her breathing slowed, then became inaudible. She fell asleep. I climbed under the covers of my bed and allowed myself to sleep . . . . .

I woke to see Aimee creeping back into the room.

AIMEE: I’m scared. I’m scared . . .

ZOE: Everything will be fine.

AIMEE: I don’t think I could have come this far without you as my friend. Will you stay with me tonight? One last time?

ZOE: (to audience) Something inside me jerked awake, something I had let sleep – warning lights, sirens, bells, everything started clambering in my jittery mind. (to Aimee) What do you mean, Aimee? One last time?

AIMEE: I need to end it, and I can’t. Not without your help. Not without you here. It’s so dark and scary doing it alone.

ZOE: No, Aimee. Not that. You’re my best friend. I can’t live without you. I’ll help you live . . . not here . . . if that’s what you want. I’ll support you any way I can. Tell them I’ve seen her come for you. Tell them I’ve seen her beat you. Tell everyone about what happened until they believe it, but I need you alive. Aimee, your dad will be home tomorrow, and we’re going to tell him what’s going on. You won’t have to tell him, I will. I’ll support you one hundred percent.

AIMEE: Then support me how I want you to support me. I can’t do it your way. I’m tired. Tired of everything . . . I have to sleep. But you have to stay with me so I can do this.

ZOE: No, I will not help you kill yourself. (to audience) I still didn’t at that point have much of a clue about what exactly she was talking about. Did she mean help her slice her wrists? Hold her hand while she did? Watch her die? I’d check the bathroom for razors now. (to Aimee) I’m going to the bathroom.

AIMEE: Bring me the bottle on the sink . . . I want to take something.

ZOE: (to audience) My mouth went dry. Drier than when she had asked me to help her die . . . (to Aimee) What bottle?

AIMEE: Bottle on the sink. Very important. Stepmother should never leave sleeping pills out with kids in the house. Never. (Aimee laughs, a deep gagging laugh)

ZOE: (to audience) I raced for the bathroom. I thought I just needed to hide the bottle, that she hadn’t taken anything or done anything. The mirror over the sinks had been shattered. Mixed with the mirror’s shards were pieces of the drinking glass – she must have thrown it at the mirror. I also saw fragments of what appears to be family photo albums. Every picture of her stepmother had been cut into tiny fragments. There were no pictures of Aimee anywhere. But the bottle was there. I was almost unaware of my tears as I picked it up . . . There was no rattle of pills. (calls out) Aimee! (to audience) She had already taken the pills. I felt devoid of hope. (calls out) Aimee! (to audience) . . . I need to get to Aimee. I needed to get help.

(calls out) Aimee! (to audience) She wasn’t answering. She was lying face down on the bed. Her back rose, fell, rose, fell, but slowly . . . too slowly. I rolled her over and came face to face with despair. A long trail of vomit slithered down the side of the bed. I had planned on making her throw up, but she already had. It was the only thing I knew to do that would slow things down and get some of the drugs out of her system. (to Aimee) Oh God! Oh God! . . . Aimee! How much of this stuff did you take? Answer me! Answer me! (to audience) But she didn’t. She couldn’t. (to Aimee’s lifeless body) Damn you! Damn you for this! (to audience) I raised her head, tried to support her with my shoulder while I cradled her from behind. I tried to make her vomit again. That’s when her bladder let go. Later, I learned that this is a normal part of death when someone takes sleeping pills.

I was screaming, shrieking, moaning. I thought someone would hear me. Some jogger, somebody walking a dog. I couldn’t see the clock. Couldn’t let go of Aimee. She was gurgling now, and I thought I should lay her down. My screams weren’t even making Aimee twitch. I screamed on and on, and eventually, when Aimee’s eyes were fixed and dilated, when she was cold and blue and filthy and beginning to stiffen up in my arms, someone heard. There was a pounding on the door, but I would have had to let go of Aimee to let them in. And I couldn’t. I just kept screaming, incoherent rages against God and county, and everyone in between . . . (in anguish) She’s dead. She’s dead. Aimee’s dead. (to audience) I quit screaming. I waited. I slipped away. I stopped thinking, stopped reacting like a human being. I became still, cold, dead inside. I still feel that way most of the time. . . .

I can’t say mad at Aimee. I want to, but I can’t. She was, is, my friend, and he needed far more than I could give her. I couldn’t or wouldn’t understand what she needed – so maybe’s she’s wherever she is now, screaming silent screams of anger back at me because I didn’t help her . . . But I was scared . . . scared of every sad and angry word she said. It terrified me to imagine her in a coffin and dead and not on the other end of the phone when I needed to talk. So I didn’t think it could happen.

Friends don’t commit suicide. They don’t die.
```

---

## IC-0073: Alias Grace

- Title: Alias Grace
- Author (byline): Margaret Atwood
- Work: Not specified
- Publisher: Anchor
- Publication date as stated: October 1997
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: GRACE, DR. JORDAN, MRS. QUENNELL, DR. DUPONT, REV. VERRINGER
- Teaser before the introduction: Yes
- Spoken words (computed): 1917
- Already set (do not supply): none

### Source block (context only)

```text
Author: Margaret Atwood
ISBN: 978-0385490443
Publisher: Anchor
Date (Month/Year): October 1997
Rock of Ages hymn: https://www.youtube.com/watch?v=gM7gt_cSxjw
The Rose of Tralee (Irish folk song): https://www.youtube.com/watch?v=Xo2Q74VN7IU
```

### Introduction (context only: never use it for content warnings)

```text
The bodies were found in a cellar. Thomas Kinnear, the owner of the home, had been shot in the left side of his chest. Nancy Montgomery, his housekeeper and mistress, was struck in the head with an axe and then strangled. It was the summer of 1842 and conspicuously absent in the wake of the murders were two domestic servants: 20-year old James McDermott and 16-year old Grace Marks. The pair appeared to have fled Kinnear's home wearing clothing belonging to the deceased. They are quickly caught and charged with the murders. Dr. Simon Jordan, an up-and-coming expert in the burgeoning field of mental illness, is hired. His mission? To find out what really happened on the day of the killings. Was Grace the evil instigator of the murder plot or was she an unfortunate and vaguely stupid girl who had fallen victim to an overwhelming male villain in James McDermott? Based on a true story . . . this is Alias Grace by Margaret Atwood
```

### Performance text (classify this)

```text
GRACE: (Pg 309-310) Nancy said we was both to leave after the next day, and she had the money to pay us. She said that Mr. Kinnear was in agreement with her.

DR. JORDAN: Did you believe that?

GRACE: As regards McDermott, I did. But not as regards myself.

DR. JORDAN: Not yourself?

GRACE: She was afraid that Mr. Kinnear would come to like me better than her. She was in the family way, and it often happens like that with a man; (voice gradually grows more coarse; rate of speaking slows – as if another persona has taken over Grace’s speaking voice) and they’ll change from a woman in that condition to one who is not, and it’s the same with cows and horses; and if that happened, she’d be out on the road, her and her bastard. (voice shifts back to Grace’s gentle cadence) It was plain she wanted me out of the way. I don’t believe Mr. Kinnear knew a thing about it.

DR. JORDAN: What did you do then, Grace?

GRACE: I cried, Sir. In the kitchen. It was at this time that McDermott said he had a secret, and I promised not to tell. Once having promised such a thing, I was bound by it. (whispering and shocked) He said he was going to kill Nancy with the axe, and strangle her as well, and shoot Mr. Kinnear when he came back and take the valuables; (back to normal tone) and I was to help him.

DR. JORDAN: You did not warn anyone?

GRACE: Please don’t make fun of me, [Dr. Jordan], it is very distressing, and doubly so considering what I am being asked to remember. . . . (Pg 312) And I did warn Nancy! While she was brushing out her hair, I said, McDermott wants to kill you.

She laughed and said, I expect he does. I would not mind killing him, either. There is no love lost between us . . . Then I knew there was nothing I could do to save her.

GRACE: (Pg 312) That night Mary Whitney appeared to me in a dream.

DR. JORDAN: (pg 102) Who is Mary Whitney?

GRACE: Mary Whitney, Sir?

DR. JORDAN: It is written underneath your portrait. At the front of your confession. Grace Marks, Alias Mary Whitney.

GRACE: Oh, yes. It is not a good likeness of me.

DR. JORDAN: And Mary Whitney?

GRACE: Oh, that was just the name I gave, Sir, at the tavern in Lewiston when James McDermott was running away with me. He said I should not give my own name, in case they came looking for us.

DR. JORDAN: And did you give any name that came into your head?

GRACE: Oh, no, Sir. Mary Whitney was once a particular friend of mine. (Pg 148) [She] helped in the laundry [at the home of my previous employer]. (Pg 149) I liked her at once. Next to me she was the youngest one there. (Pg 150) I was often astonished at the words that came out of her mouth, as many of them were quite coarse; it wasn’t that I’d never heard such language before, but I was surprised to hear it from a girl, and one so young and pretty, and so neatly and cleanly dressed. (Pg 177) I did not know she was going to die . . . . (long silence; Grace is lost in thought)

DR. JORDAN: [You were telling me about your dream . . . ]

GRACE: (Pg 312-313) That night Mary Whitney appeared. It was not the first time; she’d come before, but never to say anything. She was holding a glass tumbler in her hand, and inside it was a firefly, trapped and glowing with a cold and greenish fire. Her face was very pale, but she looked at me and smiled. Then up ahead I saw Nancy, on her knees, with her hair fallen over and blood running down into her eyes. Around her neck was a white cotton kerchief printed with blue flowers, and it was mine.

DR. JORDAN: (Pg 314) You dreamt this before the event? (writing feverishly)

GRACE: Yes, sir. And many times since. That was why they put me away.

DR. JORDAN: Away?

GRACE: (looking down at her hands) Into the Asylum, sir. Because of the bad dreams.

DR. JORDAN: (gently) Only the dreams?

GRACE: They said they were not dreams at all, sir. They said I was awake. But I do not wish to say any more about it. (Dr. Jordan steps out of the scene)

DR. JORDAN: (to audience) (Pg 373) Grace’s amnesia seems genuine enough, or so I have come to believe, in the light of my previous clinical experience. On the other hand, although she can’t seem to remember the murder, she has a minute recollection of the details surrounding it. (Pg 377) I must admit I’ve been baffled. What she says has the ring of truth; her manner is candid and sincere; and yet I can’t shake the suspicion that, in some way I cannot put my finger on, she is lying to me. (exits)

TRANSITION Months pass as Grace is questioned by Dr. Jordan. She tells the same tale over and over, lacing her tale with dreams she recalls – dreams about the murdered victims. But a person can’t be convicted based on their dreams . . . or can they? It was then Dr. Jordan developed a plan.

GRACE: (Pg 381-382) When Dr. Jordan comes back, I am to be hypnotized. Dr. DuPont is to do the hypnotizing, and others will watch and listen. [They] said I need not be afraid, as I will be among friends who mean well, and all I will have to do is go to sleep when Dr. DuPont tells me to. When I am asleep they will ask me questions. In this way they hope to bring back my memory. (Grace steps into scene, rigidly, her lips pressed together, she is obviously afraid)

DR. JORDAN: (Pg 397) (Grace pantomimes Dr. Jordan’s description) Du Pont turns the lamp down low and begins his procedure. First he suggests heaviness, drowsiness; then he tells Grace that her limbs are floating, drifting, that she is sinking down, down, down, as if through water. His voice has a soothing monotony. Grace’s eyelids droop, she is breathing deeply and evenly. He asks: “Are you asleep, Grace?”

GRACE: Yes.

DR. JORDAN: “Good,” he says. “Let us proceed.” (to Dr. DuPont) (Pg 399-404) Ask her whether she ever had relations with James McDermott.

GRACE: (laughs in a tone that doesn’t sound like her own) Relations, Doctor? What do you mean? Really, Doctor, you are such a hypocrite! You want to know if I kissed him, if I slept with him, if I was his paramour! Is that it?

DR. JORDAN: (shaken) Yes. (to audience) I was expecting a series of mere yes’s and no’s dragged out of her. Not such crude mockery. This voice cannot be Grace’s; yet in that case, whose voice is it?

GRACE: So I’ll tell you. Yes. I would meet him outside, in the yard, in my nightdress, in the moonlight. I’d press up against him, I’d let him kiss me, and touch me as well, all over, Doctor, the same places you’d like to touch me, because I can always tell, I know what you’re thinking when you sit with me. But that was all, Doctor. That was all I’d let him do. I had him on a string, and Mr. Kinnear as well. I had the two of them dancing to my tune!

DR. JORDAN: (a horse creak) Why?

GRACE: I would breathe like this. (uttering a high moan) I would twist and twine. After that, he’d say he’d do anything. (laughing) But why? Or, Doctor, you are such a curious man! Curiosity killed the cat, you know.

DR. JORDAN: Ask her if she was in the cellar of Mr. Kinnear’s house on Saturday, July 23rd, 1843.

GRACE: Yes, I was in the cellar.

DR. JORDAN: Ask her if she saw Nancy there.

GRACE: Oh, yes, I saw her. As I can see you, Doctor, from behind the veil. And I can hear you too.

DR. JORDAN: Was she alive? Was she still alive, when you saw her?

GRACE: (sniggering) She was partly alive. Or partly dead. She needed (a high twittering) to be put out of her misery.

DR. JORDAN: Did you help to strangle her?

GRACE: It was my kerchief that strangled her. (giggling) Such a pretty pattern it had on it! It was a shame to lose that kerchief; I’d had it such a long time. It was my mother’s. I should have taken it off Nancy’s neck. But James wouldn’t let me have it, nor her gold earrings neither. There was blood on it, but that would have washed out. . . . The kerchief killed her. Hands held it. She had to die. The wages of sin is death. And this time the gentleman died as well, for once. Share and share alike! (Gleeful)

MRS. QUENNELL: Oh, Grace. I thought better of you! You have deceived us!

GRACE: Stop talking rubbish. You’ve deceived yourselves! I am not Grace! Grace knew nothing about it! (Grace begins to hum/sing) Rock of ages, cleft for me, Let me hide myself in thee! Let the water, and the blood . . (see link at the end of this selection for song)

DR. JORDAN: You are not Grace . . . If you are not Grace, who are you?

GRACE: (continues singing) Cleft for me . . Let me hide myself, in thee . . .

DR. DUPONT: You must answer. I command it!

GRACE: (whispering) You can’t command. You must guess!

MRS. QUENNELL: I know you are a spirit. They can speak through others, in the trance. This one is speaking through Grace. But sometimes they lie, you know.

GRACE: I am not lying! I am beyond lying!

MRS. QUENNELL: It may be James McDermott, come here to sully Grace’s reputation. To accuse her.

GRACE: Not James, you old fraud!

MRS. QUENNELL: Nancy, then. They are often rude. They call us names. Some are angry – those earthbound spirits who cannot tolerate being dead.

GRACE: Not Nancy, you stupid fool! Nancy can’t say anything, she can’t say a word, not with her neck like that. Come, Doctor . . . You like riddles. You know the answer. I told you it was my kerchief, the one I left to Grace, when I, when I . . . (begins singing again: The Rose of Tralee – See link at the end of this selection for a link to the song) Oh, no, ‘twas the truth in her eye ever dawning, That made me love Mary . . . .

DR. JORDAN: Not Mary. Not Mary Whitey

GRACE: (no longer teasing) I told James to do it. I urged him to. I was there all along! But Grace doesn’t know, she’s never known! They almost hanged her, but that would have been wrong. She knew nothing! I only borrowed her clothing for a time.

DR. JORDAN: Her clothing?

GRACE: Her earthly shell. Her fleshly garment. But I wouldn’t want to hurt her. (pleading) You mustn’t tell her!

DR. JORDAN: Why not?

GRACE: You know why, Dr. Jordan. Do you want to see her back in the Asylum? I liked it there at first, I could talk out loud there. I could laugh. I could tell what happened. But no one listened to me. (a small, thin sob) I was not heard.

DR. JORDAN: Grace, stop playing tricks!

GRACE: (hesitantly) I am not . . . I am not . . . Grace.

DR. JORDAN: Is that really you? Are you telling the truth? Don’t be afraid.

GRACE: You see? (wailing) You’re the same, you won’t listen to me, you don’t believe me, you want it your own way, you won’t hear . . . (trailing off into silence)

DR. DUPONT: Grace . . . Grace Marks, can you hear me?

GRACE: (in her normal voice) Yes.

DR. DUPONT: I am going to bring you up now. You are floating up, up. You will not recall what happened here. When I snap my fingers, you will awake. (Snaps fingers)

GRACE: (stirring and opening her eyes, she smiles like a dutiful child) I must have been asleep.

DR. DUPONT: (gently) You may feel a little dizzy. It is frequently the case. Mrs. Quennell, would you see that she is placed in a bed chamber where she may lie down. (Grace exits)

REV. VERRINGER: (Pg 405) Two hundred years ago, [we] would not have been at a loss. It would have been a clear case of possession. Mary Whitney would have been found to have been inhabiting the body of Grace Marks, and thus to be responsible for inciting the crime, and for helping to strangle Nancy Montgomery. An exorcism would have been in order. TRANSITION But medicine had made many advancements by the mid 1800’s and no exorcism was performed. Grace’s death sentence was commuted to life in the Asylum and in the mind of the public, justice was done.

GRACE: (Pg 5) It’s 1851. I’ll be twenty-four years old next birthday. I’ve been shut up in here since the age of sixteen. I am a model prisoner and give no trouble. If I am good enough and quiet enough, perhaps after all they will let me go; but it’s not easy being quiet and good, it’s like hanging on to the edge of a bridge when you’ve already fallen over; you don’t seem to be moving, just dangling there, and yet it is taking all your strength.
```

---

## IC-0074: Always . . . Patsy Cline

- Title: Always . . . Patsy Cline
- Author (byline): Ted Swindley
- Work: Not specified
- Publisher: Ted Swindley, Inc.
- Publication date as stated: 1990 (Revised 08/09)
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LOUISE - VOICE-OVER, PATSY, LOUISE, TOGETHER
- Teaser before the introduction: Yes
- Spoken words (computed): 2031
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ted Swindley
ISBN: N/A
Publisher: Ted Swindley, Inc.
Date (Month/Year): 1990 (Revised 08/09)
```

### Introduction (context only: never use it for content warnings)

```text
On September 8, 1932 a very special little girl entered this world. Her given name was Virginia Patterson Hensley. Many years later, the world would come to know her as County Music sensation- PATSY CLINE. This selection “Always…Patsy Cline” is more than a tribute to the legendary country singer who died tragically at age 30 in a plane crash in 1963. It’s based on a true story about Cline’s friendship with a fan from Houston named Louise Seger, who befriended the star in a Texas honky-tonk in l961, and continued a correspondence with Cline until her death. The show’s title was inspired by Cline’s letters to Seger, which were consistently signed “Love ALWAYS… Patsy Cline.” By Ted Swindley
```

### Performance text (classify this)

```text
LOUISE - VOICE-OVER: Well, friends, let's not keep you waiting any longer tonight. Let's have a swell Grand Ole Opry welcome for our special guest star, Miss Patsy Cline [Music cue]

PATSY: Howdy everybody, and welcome to the Grand Ole Opry!

Honky Tonk Merry-Go-Round
I'M ON A HONKY TONK MERRY-GO-ROUND
MAKING EVERY SPOT IN TOWN
STARTING OUT EARLY, COMING HOME LATE
EVERY NIGHT WITH A BRAND NEW DATE

I'M ON A HONKY TONK MERRY-GO-ROUND
ACTIN' LIKE A FOOLISH CLOWN
STILL RACIN' THOSE BLUES THAT YOU LEFT WITH ME
WONDERIN' IF I'LL EVER BE FREE

LOUISE: Now the first time I ever heard Patsy Cline sing it wasn't on the Grand Ole Opry. No, the first time I ever heard Patsy Cline sing she was in my livin' room. That was in January, 19 and 57. Well this particular momin', I was doin' the dishes, as usual, but subconsciously, I was listening to that television. When all of a sudden I heard this voice that absolutely stopped me in my tracks. I said, " My God, that sounds like I've always wanted to sing." So, I threw the spoons and forks in the kitchen sink and went tearing into the living room to see who it was.

I said, "Get outta my way kids." and I looked and there was this chunky little country girl leaning back and leadin' into a wonderful country song called "Walkin' After Midnight" and I'll tell you I have never heard a voice that impressed me so. [Music cue – Louise acts like she’s watching her on the TV]

PATSY: I GO OUT WALKIN' AFTER MIDNIGHT
OUT IN THE MOONLIGHT JUST LIKE WE USED TO DO
I'M ALWAYS WALKIN' AFTER MIDNIGHT
SEARCHIN' FOR YOU

LOUISE: That TV audience went wild. Then [Arthur] Godfrey said, "Well, little lady, I hope that record sells like hotcakes." And then Patsy said,

PATSY: "I just hope it sells like records."

LOUISE: And it did! Well, she must have been on that show every morning for about two weeks, and every morning you would find me right in front of that TV, waiting. [She does the "TV pose" as if she is watching the TV staring up mesmerized] One day, Godfrey said "Now here's a little girl from Virginia that I think you're going to be hearing a lot from." Then she just dropped out of sight. But I never forgot that voice and I never forgot the feeling it gave me.

By 1961, I was divorced, Yahoo!, hallelujah! And I had taken a job as an electronics technician. Well, we can't all be hairdressers! Anyway, the man I worked for loved country music, and he used to keep the radio in the lab tuned to one of our leading country music stations. Anyway, one day, all of a sudden, I heard that voice again and it absolutely stopped me in my tracks. Well they didn't say who it was, so I called the radio station to find out and they said, "That was Patsy Cline singing "I Fall to Pieces." Well, I called Hal Harris, the local disc jockey, right while he was on the air and I said, "HEY [Very Bossy], you play that one again for me.", and he did. [Music cue]

PATSY: I FALL TO PIECES EACH TIME! SEE YOU AGAIN I FALL TO PIECES HOW CAN I BE JUST YOUR FRIEND

LOUISE: Patsy's music made me feel so alive every time I heard it. I nearly worried that poor man at the radio station half to death. I'd call him every afternoon four or five times a day and everyday he'd say, "Louise, I just played your song.", and I'd say, "Well, flip her over and play the other side and in an hour play my song again." Well, this went on for about two months. Well one day I called in my request, as usual, and he said, "Oh, incidentally, she's coming to town. She's going to be over at the Esquire Ballroom next Friday night."

So I told my bunch, I said, "We're gonna wear our western clothes and we're gonna get there at 6:30." My boyfriend said, "For Cryin' in a bucket, Louise, the band don't even start until 8:00." I said, [emphatically] "I DON'T CARE, WE'RE GONNA BE THERE AT 6:30." Sometimes you just have to talk to them that way.

(During the rest of Louise’s speech, Patsy continues to softly hum “I Fall to Pieces” as she does a check of the stage and instruments, check music, mics and lights, etc. Toward the end of the speech, Patsy leaves the stage and goes to a juke box in the corner of the bar)

When we went stompin' in out there, they were still cleaning the place. Except for the people at the bar we were the only ones there. Well I picked us out a table right in front of the bandstand. My boss said, [note: Louise affects a voice for her boss as a high pitched nasal old man.] "Damn, Louise, we won't even be able to hear ourselves talk." I said, "HEY!- we did not come here to hear ourselves talk. We come here to hear Miss Patsy Cline."

We'd been sittin' there about 15 minutes when I saw this girl come in across the way. She walked across the dance floor and sat down by the juke box. [PATSY sits on the barstool] She looked so lonesome sitting there. I was the only one watching her, nobody else was paying her any attention at all.

PATSY: It Wasn’t God Who Made Honky Tonk Angels
AS I SIT HERE TONIGHT THE JUKEBOX PLAYING
THOSE TUNES ABOUT THE WILD SIDE OF LIFE
AS I LISTEN TO THE WORDS THEY ARE SINGING
IT BRINGS MEMORIES WHEN I WAS A TRUSTING WIFE

LOUISE: She took off her rain coat [PATSY does so] and laid it on the back of the chair. She had on a pale pink two-piece cotton suit. Well something in my mind went DING! DING! DING! Why, it was just like our minds were talking to one another, like she was saying, "Hello, I'm, Patsy Cline, who are you?" As I looked at her sitting there in that nearly empty ballroom, I wondered what that honky-tonk merry-go-round life of hers is really like. [Louise watches Patsy intently] [Sings softly] SHE'S ON A HONKY-TONK MERRY-GO-ROUND [from opening song] So I just picked myself up [LOUISE hoists her bosom up and makes a beeline to PATSY, but then approaches her very timidly] and I walked right on over to her, I said, "Excuse me, Miss Cline.”

PATSY: (looking at Louise and smiling) Yes? (Patsy extends her hand for a handshake, which Louise shakes rather exuberantly)

LOUISE: My name’s Louise and I just want you to know how fond I am of your music. And I was wondering, if you don’t mind and if you have the time, Would you just stop by our table and say hello? (to audience) Now y’all listen up, ‘cause you aint gonna believe what she said next.

PATSY: Well, why don’t I just come over there and sit with y’all?

LOUISE: (screaming and almost fainting) OH MY GOD, WE WOULD BE THRILLED! Patsy, come on over and sit down with us.

PATSY: Well, help me out with this song first. Come on In And Make Yourself at Home NOW COME ON IN AND SIT RIGHT DOWN AND MAKE YOURSELF AT HOME

TOGETHER: COME ON IN AND SIT RIGHT DOWN AND MAKE YOURSELVES AT HOME. (Louise is clapping as they both dance a do-si-do -- As the song ends, Patsy exits.)

LOUISE: Lord . . . take me now! Well, my friends nearly fell off of their chairs. Patsy come over and sit down and in now time at all we were talking to one another like we’d known each other all of lives, she was no stranger to us. After a while, Patsy asked me if I would do her a favor. She wanted to know if I would go up there and stand by the drummer and make sure he didn’t rush her. YES MA’AM, I COULD SURELY DO THAT . . .

(Louise takes her place on the stage and instructs the drummer as to the correct rhythm. Louise gets into the music and her physical moves are big and bold. Lots of arm, hip and leg movements for comic effect)

PATSY: Your Cheatin’ Heart
YOUR CHEATING HEART WILL MAKE YOU WEEP
YOU'LL CRY AND CRY AND TRY TO SLEEP
BUT SLEEP WON’T COME THE WHOLE NIGHT THROUGH
YOUR CHEATING HEART WILL TELL ON YOU

(Louise holds the final cut-off for the ban before ending the song with a final big comic move.) (laughing) Good job, Louise!

LOUISE: (nonchalantly in her new role as manager and music director) Thanks, Patsy. You did good too.

PATSY: (to audience and especially Louise) Lord’s a mercy. I ain’t doing too bad for a girl who can’t even read notes and don’t even know what key she sings in. I feel like I’ve come a long way from working in a drug store during the day to help support my momma and then singing in clubs at night in Winchester Virginia. Next month I go up to Las Vegas. I’ll be doing four shows a day seven days a week. And I’ll tell ya, this cat’s ass will be draggin’ the bottom out of that desert (Both Patsy and Louise share a laugh) Oh, it’s a great life. I don’t want to get rich. I just want to live good. Right, Louise?

LOUISE: You betcha! (to audience) Well, Patsy brought the House down. That place was filled with people just screaming and yelling. People were stomping and hollering for more. She signed autographs and a lot of her fans took pictures.

PATSY: Louise, honey, I have got to go, I’ve got to catch a plant to Dallas tomorrow.

LOUISE: You’re never going to get a taxi out here this time of night. We’ll take you, but first we’re going to my house for some bacon and eggs. (to audience) and I want you to know that lady come right in MY kitchen and stood right alongside me frying up the bacon and eggs, just as big as you please. It was just like finding the sister I never had. When we finished eating, me and Patsy just sat around MY kitchen table and poured out hearts out. We talked about children . . . and husband problems, broken hearts, loves lost, loves found. We sounded like two people writing country songs.

PATSY: Louise, I think the good Lord broke the mold when he made you.

LOUISE: Yeah, you’re right about that! [Then] Patsy told me about her marriage. She said she and Charlie weren’t getting along too well. She told me about the hell raising arguments they would have and I knew only too well how she must be feeling. (Patsy sings the following song as an internal monologue about her troubled marriage)

PATSY: Crazy
CRAZY, I'M CRAZY FOR FEELING SO LONELY
I'M CRAZY, CRAZY FOR FEELING SO BLUE
I KNEW, YOU'D LOVE ME AS LONG AS YOU WANTED
AND THEN SOMEDAY
YOU'D LEAVE ME FOR SOMEBODY NEW

LOUISE: We traded stories until the wee hours of the morning. Then Patsy said . .

PATSY: Louise, honey, I truly have enjoyed it but I’ve really gotta go, I’ve gotta catch a plane to Dallas tomorrow. Thank you for everything Louise – I want your address cause I don’t want us to lose touch.

LOUISE: Goodnight, Patsy (Louise exits)

PATSY: Just a Closer Walk (Patsy prayerfully sings. She is a woman with many struggles and
her life is not as easy as it may seem)
JUST A CLOSER WALK WITH THEE
GRANT IT, JESUS, IS MY PLEA
DAILY WALKING CLOSE TO THEE
LET IT BE, DEAR LORD, LET IT BE
LET IT BE, DEAR LORD, LET IT BE (Patsy exits)

LOUISE: So we exchanged addresses, but you know how it is, you figure, yeah, well,that will be the end of that. I’ll never hear from her again. [But] you know what? In less than two weeks, I received the first in a long series of letter and telephone calls from Miss Patsy Cline. I tell you something, that country gal was a winner. (Louise takes out a letter and reads silently while Patsy does the voice over)

PATSY: . . . I’m going home next Tuesday and while there, they are proclaiming a Patsy Cline Day in my hometown. Ain’t that a kick in the head? The Mayor is gonna be there and recognize me and so one. Anyway, it sure is a good feeling. I can’t really believe it. I still want all of you to come down and see us at the Opry. Hope to see you again soon.

TOGETHER: Love, Always . . . Patsy Cline.

LOUISE: One morning about two years later, I was driving to work and they come on the radio and said that Patsy Cline had been killed in an airplane crash on her way back to Nashville.

She was thirty years old. It had only been six years since I first heard Patsy sing on the Arthur Godfrey show.

PATSY: (off-stage) I GO OUT WALKIN' AFTER MIDNIGHT
OUT IN THE MOONLIGHT JUST LIKE WE USED TO DO
I'M ALWAYS WALKIN' AFTER MIDNIGHT
SEARCHIN' FOR YOU

LOUISE: That’s been a long time ago, but I still call that radio station and I still ask them to play Patsy Cline for me. And as I look at the letters that she wrote to me, I remember . . . and I know she meant it when she signed each and every one of them Love . . . Always . . Patsy Cline.
```

---

## IC-0075: Amanda and the Wounded Birds

- Title: Amanda and the Wounded Birds
- Author (byline): Colby Rodowsky
- Work: Visions: 19 Short Stories by Outstanding Writers for Young Adults, Pg 78-86
- Publisher: Delacorte Press
- Publication date as stated: Oct 1987
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: AMANDA, MOM, MR. BURNSIDE, RECEPTIONIST, EMMA HART
- Teaser before the introduction: Yes
- Spoken words (computed): 1319
- Already set (do not supply): none

### Source block (context only)

```text
Author: Colby Rodowsky
Book: Visions: 19 Short Stories by Outstanding Writers for Young Adults, Pg 78-86
ISBN: 978-0385295888
Publisher: Delacorte Press
Date (Month/Year): Oct 1987
```

### Introduction (context only: never use it for content warnings)

```text
Many daughters of emotionally absent mothers spend their entire childhood trying to win their mom's love and approval instead of focusing on themselves. As a result, they grow up not knowing who they are, what they want from life, or even what they enjoy doing. They might feel empty, alone, and aimless, which often leads to anxiety or depression. Can Amanda break through to her mom and have the courage to ask for what she needs, or will her mom’s focus forever be tied to her patients rather than her daughter?

Amanda and the Wounded Birds by Colby Rodowsky
```

### Performance text (classify this)

```text
AMANDA: (Pg 78-86) It's not that my mother doesn't understand, because she does. In fact, she understands so well that half the time she goes around with a glazed look in her eyes and forgets to get her hair cut and that we're almost out of toilet paper. She makes her living understanding. You see, my mother is Emma Hart, a psychotherapist, which means that she tries to help people who call in to her on the radio; find ways of dealing with their problems.

AMANDA: I never will forget that first show. I mean, there was my mother's voice coming out of our kitchen radio, sounding slightly frantic and giving those first callers more than they bargained for. It wasn’t long before people opened by saying, "I didn't think I'd ever get through to you." After only a month on the air the Emma Hart Show went from one hour to two.

Mom really cared about the people who telephoned her, and almost from the beginning she was calling them her "wounded birds." Not on the air, of course, and never to anyone but me.

MOM: I hope my wounded bird with the abusive husband will get herself into counseling. The wounded bird with those children who walk all over her had better learn to assert herself before it's too late.

AMANDA: And I learned not to joke around: once I referred to one of her callers as a fractured canary and almost started World War III. Mom was busier than she had ever been before, what with traveling and lecturing and doing guest shows from other cities. Sometimes I felt that life was nothing but a revolving door. Mom going out while I was coming in. I know there are some kids who would've thought I was lucky, but the thing about my mother is that she's okay ... And I wanted to see more of her. Besides that, I needed to talk to her. I don't know why, but all of a sudden it seemed that things were piling up around me. No major crises, you understand. • My friend Terri has a secret crush on my boyfriend Josh. If she does, it would be a disaster, because how could we really be friends anymore? But then again how could Terri and I not be friends? • Then there's Miss Spellman, my English teacher, who has this really atrocious breath and is forever leaning into people as she reads poetry in class. Imagine somebody breathing garbage fumes on you as she recites - Emily Dickinson If something doesn't happen soon I may never like poetry again. • And . . . I was coming out of gym on my way to study hall when Mr. Burnside, the guidance counselor, stopped me and started asking me what my career goals were and had I decided what I wanted to major in in-college. What I said, only politer, was that how did I know what I wanted to major in when I didn't even know where I wanted to go to college? Mr. Burnside got a wild look in his eyes and started opening and closing his mouth so that all I could see was a shiny strand of spit running between his top and bottom teeth while he lectured me on how I was going about this whole college thing the wrong way. He said I should come into the guidance office and let him feed me into the computer - well, not me exactly, but stuff like my grades, extra-curricular activities, and whether or not I needed financial aid

MR. BURNSIDE: And what does your mother say? You'll certainly have it easier than anybody else in your class - living with Dr. Emma Hart. (chuckling) She'll get right to the Hart of it. Anybody else'd have to call her on the telephone.

AMANDA: Anybody else'd have to call her on the telephone . . . Why not? Why not? And pretty soon why not? changed to when? I practiced in the shower making my voice huskier than usual and just a little breathless, hoping that it would sound sincere. Once I'd made up my mind to call Dr. Emma Hart, I began to feel like a wounded bird myself, and I was suddenly awfully glad that she cared about them the way she did. (on the phone) I put the call in just before eleven on the Monday morning of spring vacation. I heard my voice, as if it were coming from somewhere far away, giving my name as Claire ... it's my middle name, and outlining my problem. And all of a sudden, I was talking to my own mother and telling her how I couldn't talk to my mother. . . Dr. Hart let me go on for a while and then she broke in and said that it was important for me to know that my concerns were as real as anybody else's. What I had to do was be really up-front with her and let her know how I felt. Then she suggested that I make a date with my mother for lunch so that I could tell her (Mom) exactly what I'd told her (Dr. Emma Hart). The only trouble was that as soon as Mom got home that day, I knew it wasn't going to work. She was sort of coming unglued. It had been a bad day.

MOM: Thank heavens you've got it all together.

AMANDA: Talk about guilt. Right away I knew I was going to break rule number one: I wasn't going to be able to be up-front. I couldn't take what was already one rotten week for Mom and dump my problems, which seemed to be getting bigger by the minute, on her. I felt like I was going to explode. By Friday I knew I needed another talk with Dr. Hart.

RECEPTIONIST: Hold on. Dr. Hart will be with you soon.

AMANDA: And there was Dr. Emma Hart again. And suddenly there I was. unloading about how what she had suggested wasn't going to work.

EMMA HART: Why not? Did you try?

AMANDA: Yes - no. (to audience) Then I was going on again all about Miss Spellnan, the guidance counselor; and how maybe my best friend had a thing for my boyfriend. I said that my mother was swamped, preoccupied, distracted. And then it happened. (to Emma Hart) The thing about my mother is that she has all these wounded birds who have really important problems, and they take all the time she has. (to audience) A silence ballooned up between us and was so loud I couldn't hear anything else. When Mom finally spoke, her voice sounded choked, as if she had swallowed a gumball.

EMMA HART: We've been talking to Claire this morning, who is really Amanda. And one of the things we talk a lot about on this show is saying what you have to say even if that's not always easy. Are you still there, Amanda? (strangled affirmation from Amanda) If I know Amanda, she would rather have run away, or hung up, but instead she did something harder. She hung on. Amanda is my daughter, and it seems we have some things to talk about, so what I’m going to do is to ask my assistant to make a reservation for lunch at the Terrace Garden. If you hurry, Amanda, I'll meet you at 1:30. So we can talk.

AMANDA: And we did: about Miss Spellman, and Terri, and how it's okay not to know now what I want to do with the rest of my life. We talked about saving the whales, and our two weeks at the shore this summer, and how someday we're going to Ireland. About books and movies and the time in fourth grade when I got the chicken pox and Mom caught them from me. And we talked about how we had missed talking to each other and what we could do about it. We sat there all afternoon, until the light streaking in the windows changed from yellow to a deep, burning gold and the busboys started setting the tables for dinner.
```

---

## IC-0076: The Amish Project

- Title: The Amish Project
- Author (byline): Jessica Dickey
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Nov 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CAROL, SHERRY, EDDIE, ANNA, VELDA
- Teaser before the introduction: Yes
- Spoken words (computed): 1628
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jessica Dickey
ISBN: 978-0573698880
Publisher: Samuel French, Inc.
Date (Month/Year): Nov 2010
```

### Introduction (context only: never use it for content warnings)

```text
Grief and guilt follow the survivors of any tragedy. None of us can bring back the victims of the Murrah Building bombing in Oklahoma City or the World Trade Center or the stolen lives of five murdered children in a Pennsylvania schoolhouse in 2006. Nothing can erase the horrible experience of the five girls who survived that day.

At 10:25 a.m. on October 2, 2006, a gunman entered an Amish one-room schoolhouse in the Old Order Amish community of Nickel Mines, PA. Forty minutes later, he shot ten young girls, killing five, then turned the gun on himself. What occurred in the wake of this tragedy stunned the nation. How do you forgive the unforgivable?

The Amish Project by Jessica Dicky is an unforgettable account of the Nickel Mines shooting and its aftermath, seen through the eyes of multiple characters.
```

### Performance text (classify this)

```text
Characters:
Carol: Widow of the gunman
Eddie: The gunman
Sherry: A non-Amish community member
Anna: One of the slain schoolgirls
Velda: 6-years old; one of the slain schoolgirls.

CAROL: (Pg 12-13) I was in the grocery store this morning and it occurred to me for the first time . . . I was in the hygiene aisle or whatever, trying to find a moisturizer with the um, SPF or whatever . . . No one tells you that even when you’re mourning, you still worry about wrinkles. So now you know. So I’m reading the labels about the UVA and the UVB and wham! Just like that. I think, Just because it’s written on the label doesn’t mean it’s true. Something can be written down, FDA approved, FBI protected, and that doesn’t make it true.

You can put your hand on a Bible and swear to tell the truth, and still lie. The Bible. And then you think, well what is the Bible? How is that any different from the bright yellow words on the cover of my Advil that says “Eliminates pain”? The Bible: “Proof of God.” Really?

Think of the sickest thing you’ve ever read. Right now. Do it. It was true, wasn’t it? It was something that really happened. What happens to a person when you live in a world where you can’t believe anything, and the things you don’t want to believe are actually true?

You can swear right in front of everyone you have ever know that this person – this person before you – is The One. You promise to stand by them and love them, and nurse them – Right there – cheap tux, white dress, swear in front of your family and friends. Don’t make it true.

(Pg 15) (as newscaster) This just in! Widow of crazed schoolhouse gunman buys a lotion with an SPF. Here at the BS Channel we have the exclusive interview. Now Carol Stuckey, why did you choose a lotion with an SPF? (as herself) Well, Craig, I realized if I’d taken better care of my skin and prevented wrinkles from my face, maybe my husband wouldn’t have tried to molest little Amish girls (pause) (as newscaster) Uh huh, and how do you like the SPF lotion so far? (as herself) Oh, it’s awesome.

SHERRY: (Pg 18-20) We moved to Nickel Mines about 20 years ago. We have a little farm ‘bout 4 miles out of town. On October 2nd, 2006, I read the headline across CNN – Man Enters Amish Schoolhouse And Opens Fire. They kept showing these images over and over again. It was a birds eye view: Amish families gathering in a green field, The white ambulances with red lights circles around the white schoolhouse. Tiny rectangles of bodies covered in sheets. Then the shocking details began to emerge. This just in: He was the local milkman. He only shot the girls. At least three dead. White ambulances. White schoolhouse. Bodies covered in sheets. He intended to molest them. He shot himself. Death toll now six. This just in: The Amish request that the medical condition of the remaining girls be withheld. They extend forgiveness to the gunman. They extend condolences to the gunman’s family. Green field. White. Red. White. I thought – What kind of SICKO could do this???!

CAROL: (Pg 20-21) The boys seem kind of numb. I sometimes think they’re the ones who are dead. Little ghosts. I keep my expectations low. That they sit at the table and eat their cereal, that’s enough. That somehow I managed to put two bowls, two spoons, a box of Frosted Flakes, that’s Joshy’s favorite, a box of Cocoa Puffs, that’s Jeremy’s favorite, on the table with milk, and they sit and eat it, and somehow get out the door to the carpool for the sitters, is a miracle to me. A total miracle. That’s a laugh – I’m talkin’ about miracles. You wanna hear a miracle? I still love my husband . . . I miss him. (Pg 27) He wrote: “Dear Carol. I’m sorry that I won’t see the boys grow up. You’re a good mother and I know it will be hard for you now. I hope you can forgive me for that. Please understand and try to forgive me. Tell the boys that I love ‘em. Tell ‘em – I wasn’t all bad.”

SHERRY: (Pg 28) If you were a decent wife those poor girls would be alive today.

CAROL: Some woman came up to me in the grocery store, perfectly normal looking woman came up to me . . . put her cart next to my cart and said, If you were a decent wife those poor girls would be alive today. She said:

SHERRY: There is a fresh hell where you’ll join your SICKO husband.

CAROL: And for some reason I laughed. Oh, I ran to the parking lot, smeared moisturizer over my face, scratched myself over and over again. But in the moment I laughed. You do things like that when you’re losin’ your mind. (Pg 30) It was the word. Sicko. Sicko. Sicko. Sicko. (Pg 33) There’s a fresh hell where you’ll join your sicko husband. I’m sure she’s right.

SHERRY: (Pg 18) Man Enters Amish Schoolhouse And Opens Fire. . . . (Pg 33) Oh, I ain’t proud of it, but come on now, you was thinkin’ it too. You been seein’ it on the news – these pitchers of the schoolhouse and the Amish in their buggies, but to be here, where it all happened, and see those poor people . . . Believe me, I ain’t never said somethin’ so mean in my entire life. But all day I’d been watchin’ the news and feelin’ so sick ‘n’ sad, and I saw her there in the grocery store, and somethin’ just snapped. (Pg 34) Don’t get me wrong – I ain’t exactly stickin’ up for the Amish, but we gotta draw the line somewhere. I mean, can you imagine – Oh, that’s alright, Sicko! You just go right ahead, do whatever you want, we’ll FORGIVE YA. What’s that say to all the other Sickos?!! And don’t tell me a WIFE don’t know SOMETHIN’ like THAT!

EDDIE: (Pg 35) I used to watch ‘em while I did my rounds. You ever seen ‘em? I mean, a whole flock of ‘em – in a field or crossing the road? Their little legs in their stockings, and the little bib things they wear, the way their hair twists up and disappears into their little bonnets . . . it’s like – all that beauty, all that pink, tucked away under there, hidden. Like a clean secret. They sort of scatter as you come near. But once in a while if you wave, one of ‘em will wave back (Eddie waves to Anna)

ANNA: (waves back) (Pg 36-37) He came into the school while Miss Emma was preparing the blackboard for a spelling exercise. He has a gun. He makes the boys leave and Miss Emma leave. He barricades the front door. He tells the girls to line up along the chalk board. There are ten of us. He ties our wrists with plastic ties, and our feet. I started praying to God, trying to feel how God would want me to behave – but my heart is racing. The police are pulling up around the school. Everything is getting louder and louder. Sweat pours down his face. We are lined up against the chalkboard, wanting our mammas. Waiting. (Pg 38) Sir, please shoot me first!

EDDIE: I wanted to have the girls! But the police arrived real fast – I don’t know how – so fast – I didn’t get to have the girls. So I shot ‘em.

ANNA: Sir, please shoot me first!

EDDIE: I shot ‘em! Each one. In the head. Then I shot myself.

VELDA: (singing and Amish hymn) O, God our Father/ O, Open me / With your love / Teach me to forgive / With your love.

CAROL: Got back from the store and the Amish were here. Spent all morning with me. There were about five of ‘em here, huddled here together in the living room. (Pg 39) The women wear those bonnets and cotton dresses, and the men have the blue shirts with suspenders and hats, like another planet. (Pg 41) They brought food. They were very polite. They kept deferring to me, to my grief. I wanted to say, stop. Stop. (Pg 42-43) I asked [them] how they were, how [their] little girls were. And [they] looked at me and said (gently taking on another voice) “We must trust in God now. (back to her own voice) Is that right? Trust in God. Have you turned on the TV lately? Oh you haven’t? You don’t believe in TV? Well isn’t that nice for you. Lemme fill you in: Shit like this happens every day. And the scary thing is, as mortified as I am by my husband’s actions – Eddie wasn’t a bad guy. He wasn’t the Devil. He just couldn’t keep his darkness down anymore, and it ate him. It ate him and those poor little girls, and now it’s eating me. And you can say that’s Evil, but the truth is – that’s all of us. That’s the world. We’re all just a few bad days from SICKO and that’s not Satan, that’s the truth. It lives in me and yes, it lives in you. And if you God is so great, then where was HE?!!! Where was your God when my husband took three guns, and plastic ties and drove over to Stultz Road?

VELDA: (Pg 46) (Drawing on a chalkboard) This is Anna, with her pretty pink lips. These are the ties on her wrists and feet. And the bullet. (Pg 48) This is Anna’s best friend, Marian. (Pg 49) This is my best friend Emma. She has red hair and she can hold her breath a LONG time. (She continues to draw each girl) This is Margaret – Um – She has the weirdest teeth. (Pg 50) This is Catherine. She’s a great singer. This is Elizabeth who talks ALL THE TIME, and her little sister Mary. Who never talks at all. And this is Dottie. She snorts when she laughs. And then – there’s Little Esther.

CAROL: (Pg 9) Man Enters Amish Schoolhouse And Opens Fire.

VELDA: (Pg 50-51) (Velda counts down the line of her drawings of the girls, pointing at each one, like a gunshot . . . ) One! Two! Three! Four! Five! Six! Seven! Eight! NINE! (She takes her place inside her drawing, holding her wrists and feet as if they’re bound) Ten. (She looks intently at the audience) Can you see Him? He’s here. God is here. Can you see Him? Can you see Him? Keep looking.
```

---

## IC-0077: An’ Push da Wind Down

- Title: An’ Push da Wind Down
- Author (byline): Lisa Harper
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NELLIE, MOMMA, HIRAM, HARRIET
- Teaser before the introduction: Yes
- Spoken words (computed): 2051
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lisa Harper
ISBN: 978-0573696657
Publisher: Samuel French, Inc.
Date (Month/Year): 1998
```

### Introduction (context only: never use it for content warnings)

```text
Set in rural Georgia from 1828 to 1838, An' Push da Wind Down follows a runaway slave as she heads north in search of freedom. Nellie, who cannot read, carries one thing: a roll of cloth napkins with letters written on them by her dead mother. On her way, she befriends Cherokee children and finds friendship, family, education and freedom in their village. Nellie and the Cherokees find strength in each other as the government threatens the Indians' liberty. The key to their freedom is ultimately found in the writing on the napkins. An’ Push da Wind Down by Lisa Harper
```

### Performance text (classify this)

```text
NELLIE: N-E-L-L-I-E? (MOMMA thinks she hears something move.)

MOMMA: Spells it free. Nellie be yo name. N-E-L-L-I-E.

NELLIE: N-E-L-L-I-E.

MOMMA: Da's it. See now, up nawth all da negras say it like dat. Dey say (Stately.) "Haudy sah, rna name be Nellie."

NELLIE: Dey say it like dat? ... Don't dey get wupped none with all dat (Mimicing MOMMA.) "Nellie" in 'em?

MOMMA: Cain't nobody gib ya da wuppin' up dere. Up dere ya got respect. An' don' be forgetin', don' neva look down at da groun'. Always put ya nose to da air. An' look dem dead in de eye. (MOMMA thinks she hears something move.) (Scared.) Sh- (Urgently.) We come too long a way ta be turnin' back now. Lawd Jesus, swing yo chariot low. Carrie us home lawd. (Beat.) (The sound of Barking Dogs fades in.) (Panic stricken.) No! come on, Nellie! We gotta run!

(MOMMA runs around a tree, dragging NELLIE behind her. MOMMA immediately breaks her ankle on an imaginary rock. She lets out a horrified scream. MOMMA tries to get up, but can't. She grabs her ankle. MOMMA pulls a tied roll of red cloth napkins from her apron pocket.) Nellie, heah! (MOMMA hands NELLIE the napkins.)

NELLIE: NO! What dis?! Come on Momma! Run!

MOMMA: (Commanding.) Dey my words to ya. When yousabe done wit readin' dese words, you free ... Dey's personal, Nellie. Don' nevah let nobody read 'em but chu. Run, Nellie! It best dey snatch me!

NELLIE: (Crying.) Momma!

(NELLIE looks at MOMMA stunned. Finally, she runs off crazily as Dogs Barking crescendos into blackout. MOMMA lets out a horrified scream. Silence.)

(Lights up on outside of Barrett cabin. HIRAM, a Cherokee man, notices another presence. He stands still and looks straight out over audience. He addresses the man as if he were in audience. HIRAM does not look him in the eye. He looks past him.)

HIRAM: Ah. Howdy sah. Yessah ... The name's Hiram, Hiram Barrett... This here's my land. I was just... choppin' my wood- Huh? No, sah. Haven't seen a nigger like that round these parts. I'll be certain to look out for her ... Ah, sir? You ... know you're not supposed to come this far into the woods, this here's Cherokee territory ... Good day to ya! Ain't seen no niggers today. (Silence) They're comin' closer, Harriet -- the catchers. Soon they'll want the land you're standing on. (NELLIE appears peeking from behind cabin.) You the nigger the catcher was lookin' for?

NELLIE: No, sah.

HARRIET: She looks strong, Hiram.

HIRAM: She brings danger here, Harriet. They're looking for her. Where'd you run from?

NELLIE: Be runnin' nawth from da Fortune plantation in abouts South Carolina.

HARRIET: Girl, you turned west. This is Georgia.

NELLIE: Truly?

HARRIET: Hiram, she will die in these woods. (NELLIE rocks and shakes her head. Lights fade except on NELLIE. All but NELLIE exit.) Nellie, I need help weaving. I will pay you. It will not be much, but you will at least have a place to stay. It is safer here than it is out in those woods.

NELLIE: Can you read Missy Harriet? My momma could. She could write too.

HARRIET: I can't read or write the white man's talk, only the Cherokee. Mr. Barrett, on the other hand, knows their way just fine.

NELLIE: You do, Mr. Barrett? You can help me ta read. See? I got dese heahn.

(HIRAM snatches the napkins. NELLIE stands paralyzed at first, then rocks herself as HIRAM speaks.)

HIRAM: Nellie, you reading is all the excuse they'll need to hang every one of us. They want us off this land. Little boy down the river just found gold. No excuses, Nellie. I won't give 'em even one. If you stay to help Mrs. Barrett, then you are to abide by the same laws here as you would outside these woods. You are forbidden to read. Is that clear? If you are gonna be with us you will learn the Cherokee ways and you will be Cherokee. No niggahs are living in my house.

NELLIE: You got some will callin' me a niggah. I ain't yo slave.

HIRAM: You may not be my slave but I'll take the whip to ya just as quick.

NELLIE: (Quiet, intense.) You take dat whip ta me an' I eucha so deep- You won' know wheah you en' and I begin.

HARRIET: (HARRIET crosses to HIRAM and gently snatches napkins from him. She crosses to NELLIE and gives them to her, keeping her back to HIRAM.) You will not be whipped, ever. You are my helper, not my slave.

(Silence ... ) NELLIE tries to put napkins in order. She stares at the napkins in silence till she breaks down and cries. Sound of MOMMA humming "Wade" fades in. NELLIE is held still by the music.)

NELLIE: Momma? Dat you? (Realizing the sound is only a memory, NELLIE rocks herself. She continues, pulling herself together.) I found some friends, Momma. Mightabe family ... 'ceptin' Mr. Barrett. I been thinkin' ... I be safe right here.... I ain't goin' nawth ... I be safe right heahn.

TRANSITION Nellie lives with the Barretts for many years, learning to read in secret so that someday she’ll be able to read the words Momma left her on the napkins.

MOMMA: (Commanding.) Dey my words to ya. When yousabe done wit readin' dese words, you free ... Dey's personal, Nellie. Don' nevah let nobody read 'em but chu.

NELLIE hums "Wade In The Water". NELLIE feels her MOMMA's presence and stops singing. NELLIE speaks out to audience as if she can see MOMMA out there.)

NELLIE: (Looking around.) I feel you ... I know you're here ... I can just about smell your spirit floatin' round me (Looking straight out and seeing MOMMA.) Oh ... I've been looking for you in my dreams. Where've you been all these years, Momma? … (Whispering.) I can't remember your face ... (HIRAM enters – controlled anger)

HIRAM: (Beat.) I go to town, today, to buy a new chisel. I hear the whispers. Hear them calling me red face, calling me nigger. I do nothing. I walk down the street.I feel the spit as I step into it. Then another glop lands on my cheek. I want to break something. Tear something. (Beat.) They made our cousins, the Chochtaw, walk a thousand miles, Nellie. They walked and died. They say the Creek are next. How much longer, Nellie, until we die? I want to be treated like a man. I grew up on this land with them. I am like them.

NELLIE: No you're not! You're Hiram Barrett. Hiram, Injun, poor, Barrett.

HIRAM: [My friend], Ole’ Lawrence . . . since you came, he turns his back to me. Today, I walk past [him] in that feed store talkin' to that yellow haired lady and smilin' at her and her smilin' at him. I want to yell into his face. I am family! See me!! Hear me!! He will not hear me because I am no longer Chero-kee. To him I'm just a nigger ... (Hiram exits)

NELLIE: (Beat.) I'll leave tonight. (she takes her Momma’s napkins from her pocket crosses to the tree. She unties the roll and ceremoniously lays the napkins out.) Where is north, Momma? ... Which way? "summah eighteen twenty four. dear nellie, ... i come up with da notion to writchu dis heahn letta"— (NELLIE stops reading frozen in fear. She slowly looks up and sees same imaginary man in audience that HIRAM saw earlier. She looks down as she speaks.) huh? ... naw, sah, I ain't no niggab run way ... na, got ma pass ... I... I... I be huh? ... come closab? ... (She does.) closab? (NELLIE moves closer. Now she is dangerously close. She continues timidly, cautiously.) Ya horse sho' do smell fine, sab ...

(NELLIE slowly raises her head with her eyes down till her face is almost facing the sky. She turns her head to the right as if commanded to. Then to the left. Then NELLIE turns around in a slow circle. Enter HIRAM.)

HIRAM: (Looking past him.) She's mine. I bought her in Charlestown ... last week ... I have the papers, at home ... what's what? (HIRAM looks down to NELLIE's hand holding the napkins.) Oh! Just some old rags we sent with the niggah to bring to Ole' Lawrence over yonder past the cotton patch ... He's in need of some rags, sah ... (To NELLIE.) Sarah ... Sarah?

NELLIE: Oh! Yessa, Massa.

HIRAM: You should know by now, the cotton patch is on the north side of the cabin. (To man, confiding.) You know these niggers ... gotta tell 'em things three and four times- (To NELLIE, pointing.) The north side, Sarah! The north side! (To man, confiding.) Dumb as a deer ... Sorry to cause you so much trouble. I will keep my eye out for the runaway. HIRAM. Good day, sah. (HIRAM watches him go. NELLIE remains frozen.) You can relax now ... He's gone. (Silence.)

NELLIE: Thank you ...

HIRAM: He saw you reading.

NELLIE: I don't know. I'mj ust so glad . . .

HIRAM: Put them in my hands, Nellie. Put them in my hands. Now. (HIRAM reaches for the napkins.)

NELLIE: No! Massa Barrett! No! Give me another chance. I promise I'll run tonight. NO! DON'T TAKE MY MOMMA FROM ME AGAIN! You hear me!? (HIRAM takes the napkins from Nellie’s hands by force)

HIRAM: You may stay, Nellie. Mrs. Barrett wants you ... and I cannot hurt her. If you speak of these napkins even once that will be the day you leave ... without them. They are watching us now. You will not endanger my family again.

(Hiram exits) *****

NELLIE: Eli taught me [to read[, Momma. Mr. Barrett, he gets the newspaper one time every moon. I comb it from back to front. I look for news about you. Course, I know white men ain't gonna take no intrest in a niggah lady swingin' from a tree. But I comb it just the same. (Beat.) Mr. Barrett has the napkins. (Beat.) I miss you ... you say ... "Read dem napkins, Nellie. Den you be free ... some parts of you is free, like yo' hands and yo' foots. You move dem wheresoevah ya wants dem ta go. But yo spirit still bound. Dem napkins gonna' free yone spirit." (Beat. ) Momma? Do you think freedom is flying? What happens if you fall from freedom? Can your wings break? (Beat, slowly, determined.) I'm gonna read, Momma. Read what you gave me. I know you're with me, Momma ...

HIRAM: (who has been listening – he enters hesitantly, then speaks) Look at the water, Nellie, how free it is. It glides along and dances around rocks and slips through the fingers of those who would want to control it. I want to be like that water. I don't want to be like the Choctaws who were forced to walk in bloody snow. I want to slip through the soldiers' grasp and live on this land forever. The long walk is coming ... (HIRAM takes the napkins andhands them to NELLIE.) Here ... (5 second pause.) ... Be free ... (Whispering.) Forgive me.

NELLIE: The last time I saw my momma she was huddled in a pile of leaves with blood drippin' from her head and feet. She was yelling ... I crossed a crick and hid under a pile a leaves. When I get my guts up ta look out I see them dogs tearin' at her flesh and my momma's not movin' ... they chewed my Momma ... Then the men beat her with a Sassafras branch they found near by. Those dogs licked the new blood holes in her back ... She cried ... lain' nevah see my Momma cry before that day.

HIRAM: Life is a trail of tears, Nellie. Loss ... walks close, our greatest enemy ... while grief... holds our hands ... our best friend. Listen, Nellie ... (NELLIE stares at him.) I'm sorry. (Hiram exits)

NELLIE: (To the napkins.) Whatchyou got ta say ta me, Momma? (NELLIE unwraps the napkins. She kisses them, and reads.) "summah, eighteen hundred and twenty four"-I was just six when she wrote this!-"dear Nellie, I come up wit da notion ta writchu dis heahn lettah 'cause anti sissy's baby milly jus' done been sold 'way. my mind go back ta ya. i's writin' dis heahn lettah so's you might knows i loves ya. yo' pappy jus' lef’, he went on back up to da big house. is dere he belong. not wit me, ... not wit you ... We called him "massa" ... he was yo' fathah." (To herself) No ... no ... (Momma takes over her story)

MOMMA: (Whispering.) Nellie, i gone tells ya a story, gone gib ya power such dat no thang is dis heahn worl' can evah touch ya soul. dey tells me, say way back in africa be peoples could fly. say dey lift dey hands up an' sail on da back o’ da wind. one day say da peoples wings be bound up by ones come from da sea. dey be force ta come ta a new land. cain' fly no mo'. masters make 'em trade dey wings fa hoes. say dey mix in with da othah africans an no body could tells 'em apart. say overseer break one bone in every african's body till finally dey needs de hoes jus' ta keep 'em standin'. dey work night and day. oversser cry out to da africans say ... 'faster ya black pigs! Move dat cotton, niggah!" den he wup em harder. no body can remember the magic words what made dem able ta fly back home in africa. so dey walk da rows a cotton. no body but one african calls hisself Abraham. say one day when da overseer whip be lickin' at da african foots an' da sun be burnin' down on de backs an' da bones be a breakiri', say one gal calls hersef Lydia cry out to ole' Abraham say "now, befoe anothah life be crushed! speak da words!' ole' Abraham runned over an take hold a Lydia's bloody hands an raise his arms ... KUM YALI KUM BUBA TAMBE!

NELLIE: (NELLIE places napkin on ground in front of her and lifts her arms as if to fly.) (whispering.) Kum Yali Kum Buba Tambe ...

MOMMA: den all aroun' him da words be whispered. say one by one da peoples stood straight, drop dey hoes in da field, lift dey arms up and push da wind down neaf 'em. till dey all feel dat african spirit rollin' tru dey arms. and dey rise up free as birds in a african sky. and dey fly far away to freedom. ... Look at me, Nellie. I be here. Kum Yali, Kum Buba Tambe, Nellie. It be where you come from. When you fly, Nellie, cain' no body touch ya spirit. Dey can put shackles on y!l foots and yokes 'round yo' neck, but when ya knows how ta fly, dey cain' nevah touch yone spirit. do ya have ears ta hear what I be speakin' to ya, Nellie? Fly nawth and spell yo' name free. NELLIE. (Beat... gravely.) My name is Nellie Lawrence. N-E-L-L-I-E. (Beat.) KUM YALI, KUM BUBA TAMBE!! (NELLIE breathes in deep and brings her arms down as if pushing the wind down. Whispering.) dey tell me ... way back in africa ... peoples could fly. say dey lift dey arms ... an' push da wind down low beneaf 'em ... and dey jus' rise up free as birds. an dey fly far away to freedom ... Gonna be free now ... gonna walk free ... somehow. (Silence. Fade to Black)
```

---

## IC-0078: And Then – Hanadi and Lynndie

- Title: And Then – Hanadi and Lynndie
- Author (byline): Amelia Arenas
- Work: The Best American Short Plays 2006-2007
- Publisher: Applause Theatre and Cinema Books
- Publication date as stated: April 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1887
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amelia Arenas
Book: The Best American Short Plays 2006-2007
ISBN: 978-1557837486
Publisher: Applause Theatre and Cinema Books
Date (Month/Year): April 2010
```

### Introduction (context only: never use it for content warnings)

```text
Suicide bombers are today’s weapon of choice. An action that was once so surprising, horrific, and terrifying has now become the daily fare of the nightly news. In terms of casualties, suicide attacks are the most efficient form of terrorism. From 1980 to 2001, suicide attacks accounted for 3 percent of terrorist incidents but caused half of the total deaths due to terrorism―even if one excludes the unusually large number of fatalities of 9/11. Into this boiling cauldron of terror, a new element has been added―women as suicide bombers. The success of suicide bombers considerably depends upon surprise and accessibility to targets. Both of these requirements have been met by using women. In her play And Then, Amelia Arenas has created a 1st person account of a female suicide bomber. Meet Hanadi Jaradat
```

### Performance text (classify this)

```text
I. Hanadi
[She reads from a piece of paper in front of a video camera. A Palestinian flag hangs in the
background.]
This is the last statement of Hanadi Jaradat, your martyr, spoken before the Haifa
operation.
Allah, Father of all things! Allah, the merciful ... ! [She drops the sheet.]
I was there.
The fire spread from my breast like thunder. But not a single one of those strangers died
before I did.
I was prepared.
Now they call me a terrorist. Yesterday, I was Hanadi.
* * * * *
And what ever happened to him - that good-looking, well-to-do boy I was supposed to
marry?
And what about that other one. Remember, Mother?
The one Father never let me talk to.
* * * * *
I feared the strength of a man's arms and my mother called me cold
because I couldn't stand the noise of children.
But that husband and those children I was to have one day
blew up with me last night.
Last night ...
My hunger for love
was not as great as my rage.
* * * * *
They said that mother collapsed when she saw my picture in the news. She thought I was
working late ...
Mother!
Don't look at those pictures! You won't find your child there. She's a ghost now.
She will be climbing the chestnut tree in your backyard forever.
* * * * *
Father,
Remember how you never let me go out?
I hid under the covers all night with a tiny mirror in my hand, playing with that dried-up
lipstick I found in Mother's trunk.
I wanted to be like the woman in those pictures - the one your father married and died
young.
The one from Jordan.
The one with the big hat
and a cigarette in her hand.
I used to think that
if I looked at her long enough without blinking, I could make her smile.
You never let me go out, Father. I was supposed to hit the books
and quit dreaming about faraway places and pretty ghosts.

And I did what you said. Didn't I?
* * * * *
As far back as I can remember, you've said again and again "This land is ours!
We have to be better than them.
They are the sort that suffers out loud. We are the sort that remembers."
Did you understand my death, Father?
Now you say that you won't ever mourn me because I made you proud.
Weren't you proud of me back then?
Do you ever cry for me now, Father?
* * * * *
And you, neighbor?
I once walked by your streets,
and you looked at me with a sly glance. I covered my head with a black scarf but I painted
my lips bright red.
You hid your girls in your houses
and your sons smoked under the elm tree while I was earning a living.
* * * * *
Look at me now, neighbor! LOOK!
Don't turn the TV off!
You don't have to peek
through a crack in your window anymore.
I am the girl your sons could have never married.
You can look at my mangled corpse and cry. Now I am your martyr.
I am a scar you'll flaunt.
Look at me, neighbor!
LOOK!
Memorize my horror.

I died for YOUR sons-
the ones who squatted all day long waiting for a job,
when I was at work.
* * * * *
I didn't put on the pretty dress and go to that party,
just as you said, Father.
I obeyed.
I dressed myself in the pride of your fathers. And I took with me
those loud words you spoke.
They were all with me last night. They were the fuel that turned me and those strangers
into a wave of blood.
* * * * *
Remember the wounded pigeon we brought home?
Remember how you made him better? We called him Ibrahim.
Remember how, a few days later, when I returned from school,
we found him stiff in that cardboard box?
Remember how I begged you,
"Father, make him better!"
But you didn't.
You couldn't.
We buried him in our backyard. I sat on your lap and cried.
But you didn't dry my tears. You said,
"The salt of sorrow shapes the soul."
You told me it was time to do my homework.
* * * * *
And Fadi? OURFADI!
He blew up with his homework in his hand. And you could not bring him back either.

* * * * *
I wish you had held me in your arms a little longer ... I wish I was buried in that cardboard
box.
Father!
Don't look away now!
Watch me!
I am a cloud of stench. Be proud of me! Listen to me!
ALLAH, FATHER OF ALL THINGS be proud of me!
THIS is my wedding day!
* * * * *
TRANSITION

Since the War on Terror began on 9/11, we've captured hundreds of Islamic terrorists along with the capture of Saddam Hussein himself. The War against Iraq has brought in thousands more prisoners with potential knowledge of upcoming terror attacks. Unfortunately, when a capture is publicized, terrorists quickly change locations, plans, and communication methods. Thus, any intelligence we can gather from such captures is only good for a short time. The question becomes, should we torture these captures to obtain the information while it's still good? In 2004, photographs of abuses at Abu Ghraib shocked the world. Seven people were charged, but the face of the scandal will always be Lynndie England, the 21-year-old private grinning at the camera. She wasn't the only woman soldier in the photographs - Sabrina Harman and Megan Ambuhl were both court martialled for their roles - but England was the most arresting looking, like a 14-year-old boy who shouldn't have been there in the first place. Her legal defense, that she was unduly influenced by Specialist Charles Graner, the father of her child and the only soldier still serving time for abuses at Abu Ghraib, was compounded outside the courtroom by assumptions about her background; that she came from a place where people didn't know better. In another excerpt from And Then by Amelia Arenas we hear Lynndie England’s story.

III. Lynndie
Hi there!
I'm Lynndie England. PRIVATE England!
I'm an American soldier!

Oops, sorry! I was an American soldier. And I kicked ass, damn it!
But where the hell am I now?
The stupid lawyers don't even let me talk in court. I could say a thing or two about my
"superiors" ...
I'm toast.
I'm twenty-one
but they'll put me away until I croak.
And, guess what? I'm pregnant.
As if I needed this ...
* * * * *
Oh! Gimme a break! We all did it.
Mike was there. Watching it all.
I was crazy about him, He was SO bad!
I used to look at him and think, wouldn't it be cool to be him?
* * * * *
They're making a big deal on account that I'm a woman. It's not like I'd never seen a gun,
OK?
I learned to shoot at nine.
Dad taught me how to hunt deer. And I was good at it, too.
But then we had to drag the dead thing into the van.
That was hard.
He let me ride in the back.
I wanted to look at the buck. He was so big!
His eyes were still open.
His tongue hanging out from his mouth.
I touched him.
He was still warm.

A beautiful thing, you know ...
If I live again, I want to be one of them, you know. A big buck. And I won't let anyone get
me, damn it. I'll fight back.
Anyway.
Dad would have killed me if he'd caught me petting it.
I just wanted to know what the deer thought when he froze, saw me point the gun at him
and heard the blast.
I asked Dad,
"What's gonna happen now
with the buck's kids and his wife?" What can I say, I was just a stupid kid.
Dad cracked up.
I was so pissed!
I jumped out of the van.
He goes, "How can you be so dumb! Deer don't have wives or kids. They're not like us.
They're beasts.
We've been killing them and eating them since God knows when.
So don't go stupid on me now. Get in the van!"
I thought, "Wait.
We don't even eat the whole deer.
We dump most of it over the cliff and let it rot."
Anyway.
It's not like he was mad or anything. Actually, when we got home he said, "You're a swell
kid, you know?
You wacked this one all alone.
Give Daddy a kiss!"
I hated Dad's kisses.
His mouth tasted like an ashtray full of whiskey. But I liked the way he looked at me.

Not at home, when we were out.
When we were out I did not feel like a girl.
* * * * *
That day Mom was a mess
when she saw my dress all bloody.
Just like the day I said
I was joining the army.
What does she know?
She's always baking something. Yakking on the phone with her friends. Watching soap
operas.
I had to get the hell out of that dump or else I'd end up like her.
* * * * *
Man, if you had seen the party they threw me! Billy left the gas station early,
Molly and Jake came
all the way from Norfolk.
And the kids from the factory came too.
I still had a hangover when I got to the base ... So, I get into that plane.
And then,
Iraq, baby.
Wow,
what a mess.
You had to see it! Bombs every day, Everywhere.
And those Arabs
spat in our faces when we walked by their homes. Two guys in my unit croaked.
Right there, practically in front of me. They were not even fighting.
Just guarding the streets.
That's how these animals pay us back. After we get that fat pig out of there and we're
trying to teach them how to live like human beings!
Animals! That's what they are!
* * * * *
One day we
took the creeps out of their cages.
We got them naked.
I held one of them on a dog leash. and put a panty over his head.
One of us took a leak on a guy's face and all that ...
So, what's the big deal?
The dogs were scary, though. I'll give you that.
But, hellooool It was IRAQ!
It's not like we were on vacation.
What do you think we got?
Stale hamburgers and flat beer. And what was going on every day? A LOT OF NOTHING.
Except another guy you just met got shot. The rest was all,
"Yes, sir! Yes, sir! Yes, sir!"
Oh, please.
Somebody has to look bad
so that it all looks good, I GUESS.
* * * * *
But wait, what was I talking about? Oh, yeah. The guy on the leash. At some point, I look
at him
and the coward covers his face
and starts crying like a baby.
Right there and then,
I thought of that buck I shot when I was nine. He never closed his eyes.
He kept staring at me even after he died.

I still see him sometimes in my head
and I get all sweaty.
I wish I could talk to him and tell him, "You're a real man.
Not like this scum here.
I didn't really mean to kill you, buddy. I was just a kid.
I don't even like venison."
* * * * *
Hey, what are you looking at? Did I offend you?
Well, pardon me, SIR.
```

---

## IC-0079: The Andrew Poems

- Title: The Andrew Poems
- Author (byline): Shelly Wagner
- Work: Not specified
- Publisher: Texas Tech University Press
- Publication date as stated: January 1994
- Event as filed: Dramatic Interpretation
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

Had I gone outside that night,
no one would have let me bathe you,
wash the mud from your cheeks . . .
You could not come back to your room.
But I wonder,
did the river sweep your wet hair straight back
and make you famous?

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
Thomas, my nine-year-old man-
of-the house, set the trap with cheese.
Three-year-old Andrew wandered in
as we lay the loaded trap on the floor;
I perched him on the kitchen counter
with the impossible command,
“Do not move.”
Thomas and I armed ourselves
with a mop and a broom
and jumped up on the ledge with Andrew.

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
He hopped down explaining,
“That how they do it on the ‘Young and the Restless.’”

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

He was a sight. Some laughed. But to me it looked like Joseph’s coat of many colors – proof that a son was dead.

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

[But] What If? (Pg 78)
What if the divers had surfaced empty-handed?
What if someone had found him just sitting in a tree.
He would have been wide-eyed watching the flurry of lights
He would have loved the flashlights of those on the shore
shining in all directions like gleaming swords.
He would never have forgotten
the blue lights on the police cars swirling
like the moonlit wake of the rescue boat.
The boat’s searchlights and acrobatic divers
would seem to any child a circus act.
Had he jumped from the tree and come running,
the search would have been no more than a midnight

cruise,
the black hearse would not have come for his body,
the helicopter pilot could have killed his floodlight,
the media would have abandoned their story,
and his grandmother never learned
from the eleven o’clock news
that her youngest grandson was missing from our yard.
Embracing him, would I have scolded him or covered him
with kisses of sweet relief?

(Pg 15) (echo) “That how they do it on the ‘Young and the

Restless.’”

(Pg 78) Definitely kisses.
probably never would have scolded him again at all.
Would I have let him sleep with me?
He asked to every night at bedtime.
No, that was not his place.
His room was across the hall where I could see him.
But he did drown and he is not in his room anymore.
Since that evening when he did not come when I called:

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

## IC-0080: Angel of Philadelphia

- Title: Angel of Philadelphia
- Author (byline): Allen Amundsen
- Work: Not specified
- Publisher: Brooklyn Publishers
- Publication date as stated: 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MARIAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1254
- Already set (do not supply): none

### Source block (context only)

```text
Author: Allen Amundsen
ISBN: 978-1932404159
Publisher: Brooklyn Publishers
Date (Month/Year): 2003
NOTE: No Longer in Publication
```

### Introduction (context only: never use it for content warnings)

```text
"I have a dream that one day this nation will rise up and live out the true meaning of its creed: 'We hold these truths to be self-evident, that all men are created equal.'" At the height of the Civil Rights Movement in 1963, these famous words were spoken from the steps of the Lincoln Memorial in Washington, D.C..

But Martin Luther King, Jr., was not the first to raise his voice from those steps with a message of hope for America's future. That distinction belongs to the world-famous contralto Marian Anderson, whose performance at the Lincoln Memorial on April 9, 1939, made a compelling case for the transformative power of music, and in a place typically associated with the power of words.

Angel of Philadelphia by Allen Amundsen.
```

### Performance text (classify this)

```text
NOTE: No Longer in Publication as of January 2017.

MARIAN: If someone would have told me that some day, I would be singing if front of seventy-five thousand faces . . . I would have called ‘em crazy. “Get out now. You’re out of your mind!” But there I was, standing at the top of the steps of the Lincoln Memorial, the giant white marble statue of ‘ol honest Abe himself looking down on me. I just knew any minute; someone would shout at me and ask me to leave. “What’s that colored girl think she’s doing?” But no one shouted. No one yelled. No one called me awful names. Only my voice: my instrument from God himself remained. And I sang with all of my heart that night.

(Sing opening lyrics of “MY COUNTRY TIS OF THEE”)

TRANSITION There was nothing overtly political in the selection of songs Anderson performed that day before a gathered crowd of 75,000 and a live radio audience of millions. But the message inherent in an African American woman singing "My Country 'Tis of Thee" while standing before the shrine of America's Great Emancipator was crystal clear.

MARIAN: I’m a Philly Girl. South Philadelphia to be exact--born and raised. Philly is known as the birthplace of freedom, the City of Brotherly love…well, when I was growing up, it was those things in name only. Every day, I felt this presence. I call it, The Glare. People, they had this stare, this gaze—it burrows into your skin. It hurts, sometimes, like tiny daggers cutting you down, piece by piece.

My mama and daddy did everything they could to shield us from hate. They did this by taking us to church. People often ask me how I found music…and I think back on it, and I really feel that it was music that found me!

God had a plan for me. I discovered my voice while singing in church. I was asked to be a member of the choir; then they wanted me to be a soloist; and then some of the older folks in the church insisted that I take my gift and go to music school. The congregation even took up a collection for me to pay for it! With their graciousness in my hand, I went downtown Philadelphia to one of the biggest and best music schools in the state. I walked into the Admissions office excited and hopeful. As I closed the door, all noises stopped—typewriters, conversations, even the phone seemed to quit ringing. There was a young blonde woman at the main reception desk. She had to have been at least twenty-one or twenty-two. Instantly I saw it in her eyes: The Glare. The tiny daggers, the non-verbal accusation: what are you doing here huh? What do YOU want colored girl? I politely walked up to her and asked about the application process. Her milky white face had turned pink and she wouldn’t look at me! Not once. I asked again, “How do I apply for the vocalist program?” She didn’t say anything except for sorry. We just don’t have room. Room for a black girl! I thought angrily to myself. I almost gave up…I almost let it crush my dreams. When God plants a dream in your mind, it’s hard to shake it off. I eventually found a teacher, the most famous teacher in Philadelphia, Giuseppe Boghetti. Giuseppe helped me hone my instrument and move my voice to higher plains. He said that a voice like mine came once in a thousand years, and that my contralto was from heaven. The Angel of Philadelphia. That’s what he called me.

Well, this Angel has flown everywhere, from New York City to Moscow. I even had fans! If someone would have told me, “Marian…girl, you’re going to be famous one day! Men and women all around the world will pay money just to hear you sing…” I would’ve told them they were crazy. But that’s what happened. The music found me. In spite of all of that---the traveling, the concerts, the audiences, the applause and admiration… the Glare never went away. The hateful stares, the cold gaze of white folks cut into me everywhere I went.

And I had some notoriety by the time I came back from my tour of Europe. I’ll tell ya- --Europe and America may be on different sides of the world, but they may as well be on different planets. In Europe, I never heard colored girl go home or had the n-word flippantly tossed at me; and I never saw The Glare. The Glare had gone away when I was in Europe. Only smiles, applause, and respect.

And then I come back to the states, this separate reality, this---this divided paradise where if you were black you’re nothing. I remember walking into the Continental in the Upper East Side. Walking in, I thought: this is New York. This is a well known hotel. There shouldn’t be any problems. The front desk clerk looked up from the check-in desk and did a double take. I watched him closely as he fumbled with his little box of reservation cards. The young man cleared his throat and told me he couldn’t find my reservation. He added they were completely booked. Sorry.

I had the honor of being invited to sing at Constitution Hall. I could not believe it. That room had special spirit to it--- freedom, inspiration, creativity, possibility. What a thrill it was…the first African American to perform there!

I went to meet a few key members of the Daughters of American Revolution, who owned the building. I stepped through the main foyer and into the events office. As soon as I set foot into the room… silence.

I explained that I was Marian Anderson and that I was scheduled to perform there in a few days. Their eyes were in shock, mouths agape, not understanding. I asked to speak with the director, but no, she wasn’t there and could you leave a telephone number or we’ll telegram you, blah, blah, blah. I was quickly rushed out. I did receive a phone call…canceling my show at Constitution Hall. They had a strict policy: no Negroes were allowed to perform. The Daughters of American Revolution had rules. And they excluded black people. Some revolution huh?

Back at the hotel the phone rang again. It was Eleanor Roosevelt. The Eleanor Roosevelt! The first lady! She adored my voice, she said. She was furious at the Daughters of American Revolution, she said. She resigned her membership to that group. She was determined to make things right. She wanted all of New England to hear me sing. And here I am. Easter Sunday, 1939. Standing at the steps of the Lincoln Memorial, the gigantic marble statue of ol Honest Abe staring down at me. I turned to look at his face, and I didn’t see The Glare cutting into me…I saw I nod of approval. I think if that statue of Lincoln could’ve smiled, he would have! I glanced back at the thousands and thousands of faces gazing at me. The Glare wasn’t there either. Only wide eyes, smiles, and joy.

If someone would’ve told me that some day, I would be singing in front of 75,000 people, I would of called ‘em crazy. But there I was. And the Glare was gone. Maybe forever. I closed my eyes and I sang… my voice, my gift from God, pierced the sky, the clouds, The Angel of Philadelphia had flown.
```
