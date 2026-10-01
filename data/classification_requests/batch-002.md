# Classification request: batch 2 of 2 (5 records, IC-0041 to IC-0045)

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
