# Classification request: batch 33 of 53 (40 records, IC-1681 to IC-1720)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-033-reply.json`.

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

## IC-1681: The Second Coming

- Title: The Second Coming
- Author (byline): Ken Siegmann
- Work: Will Work for Peace
- Publisher: Zeropanik Press
- Publication date as stated: 1999
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1633
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ken Seigmann
Book: Will Work for Peace
ISBN: 978-0966645910
Publisher: Zeropanik Press
Date (Month/Year): 1999
```

### Introduction (context only: never use it for content warnings)

```text
What if that actually happened? What if Jesus were to return today, not to bring about the end-times, but for a quick visit to reaffirm his existence for believers and offer the world a much-needed message of peace and charity? How would America react to Jesus’ return? The Second Coming by Ken Siegmann
```

### Performance text (classify this)

```text
1

The second coming arrived on Broadway and 42nd Street just before New Years Eve. He stood in his robe, scraggly beard and sandals, appearing a little dazed, or maybe just ethereal. He looked like he belonged there.

"Where is this place?" he asked a passerby in Times
Square.
"What!" said the incredulous man. "Who the f***
are you?"
"Jesus," said the second coming.
"Hey," said the incredulous man, "no need to curse,
but
you do look like him."
He directed the second coming to Madison Ave.

The second coming stepped out of a cab on Madison a few blocks from Grand Central Station. He had no money, but even a New York City cab driver respects a good miracle. A sign said, "The J. Walter Thompson Agency." The second coming entered.

Sitting before the man who would become his agent, the second coming explained about God and Salvation and Peace and how much God loved purple flowers. The agent thought he was nuts. But there was something compelling about this man in his robe, scraggly beard and sandals, appearing a little dazed, or maybe just ethereal.

"Maybe we should call the Pope," said the agent.
"Who," asked the second coming?
"It's too complicated to explain.
Maybe we should call a news conference."

The agent called the New York Times and the New York Post and the Washington Post and the Daily News and the National Enquirer, the American Spectator, ABC, NBC, CBS, CNN, The Christian Broadcasting Network, the Christian Science Monitor, various Web site providers, the White House, and his mother.

The second coming and his agent stepped out of a
cab
in front of St. Patrick's Cathedral (it was the
agent's idea).
The second coming looked at the tall spired
building.
The cross made him wince. He looked down at his
feet,
rubbed his hands together, scratched his forehead.

"Where is this place," asked the second coming? "St. Patrick's Cathedral," said the agent. "It's a church." "A what?" "It's too complicated to explain."

It was a slow news day, so lots of reporters came for the second coming. They brought notebooks and tape recorders and microphones on boom stands and cameras, satellite uplinks technicians, toys and perfect haircuts.

The second coming stood on the steps of St.
Patrick's Cathedral.
He explained about God and Salvation
and Peace and how much God loved purple flowers.

The reporters held their notebooks
like they were covering a stump speech,
but there was something compelling about this man
in his robe, scraggly beard and sandals,
appearing a little dazed, or maybe just ethereal.

"What's your position on abortion," someone asked? "On what," asked the second coming? "Baby killing," said the man from the Christian Broadcasting Network. "It's a sin to kill babies."

And the headline read:
"The Second Coming Has Come, Condemns
Abortion."
The agent was pleased with the coverage.
The second coming was confused.

An editorial in the New York Times cautioned.
The Christian Science Monitor applauded.
USA Today ran an eight-inch story with color
charts of
Jerusalem and Bethlehem.
CNN tried to get him on Larry King Live.
Someone called the President.
Someone called the Vatican.

The agent booked a suite at the Trump Plaza. The second coming preferred to sleep with the homeless on a steam grate in front of Tiffany's. He talked to the homeless of God and Salvation and Peace and how much God loves purple flowers, until a policeman rousted him and said he couldn't sleep there. So he slept on a bench in Central Park.

2

The second coming was not good news to the Vatican. The Pope made oblique, noncommittal statements about "this figure who has appeared" and tried to keep his options open. He worried.

The President weighed the political benefits of embracing the second coming, and the possibility that the second coming was a scam. He knew about scams.

The President ordered the FBI to do a background
check
on the second coming's agent and the CIA
to look for coded messages in his words
about God and Salvation and Peace
and how much God loved purple flowers.
He worried.

The Christian Coalition liked his stance on abortion, and so embraced him immediately. They printed millions of voter guides with a check box for which candidates supported the second coming and which ones did not. They didn't worry. They felt righteous.

The media fumed because
the second coming didn't do interviews.
So they interviewed scholars and pundits,
rabbis and priests, monks and nuns,
and mothers superior. Peter Jennings walked
through virtual reality sets of Jerusalem and
Bethlehem.

Geraldo called it "the greatest story since O.J." Steven Bochco plotted the TV series. The networks looked for sponsors.

Birkenstock brought out a new line of sandals like the ones the second coming wore. Ralph Loren marketed a now familiar looking robe. Trendy students and rock n' rollers grew scraggly beards and hung out at Tower Records. Kids went to school with second coming lunch boxes. The agent collected royalties. The second coming slept in Central Park and attracted crowds.

3

The second coming made the agent nervous. The agent experienced a spiritual awakening. He started to spend more time in Central Park and less time at second coming headquarters in his Plaza suite. The agent still wore his blue suit, white shirt, red tie and black shoes, but he thought of giving up his cellular phone and his beeper.

The agent tried to get the second coming to read The New York Times and watch CNN. The second coming listened to the homeless who came to hear him talk about God and Salvation and Peace and how much God loved purple flowers.

4

The second coming's second news conference drew reporters from around the world. They brought notebooks and tape recorders and microphones on boom stands and cameras, satellite uplinks technicians, toys and perfect haircuts. They snarled traffic all over Manhattan.

"Would you clarify your position on abortion," a reporter asked? "I have no position on abortion," said the second coming. "But it was reported that you said..." "That was incorrect. My agent will supply you with a transcript." The second coming was no longer confused.

A Gnostic scholar asked, "Can you put an end to speculation that you had relations with Mary Magdalene?" "Yes, I can," said the second coming. The crowd leaned forward. "Stop speculating."

"The Pope has refused to declare that
you are the legitimate second coming."
"Render unto the Pope what is the Pope's.
When he leaves his castle and gets down here
in the streets with the rest of us,
then he'll have an opinion worth considering."

Asked about welfare reform, he said: "We should not turn our backs on the poor." On the Middle East: "Those people have never gotten along." On Rwanda: "Feed the people and there will be peace." On Newt Gingrich and Bill Clinton: "Father forgive them. They know not..." On the Christian Coalition: "They're using my name without my permission." On premarital sex: "Is this something new?" On homosexuality: "Is this something new?" On the current state of the world: "It's pretty much as I left it, just more crowded." "Why have you come back?"

"Because it's time."
"Thank you for coming."
The second coming walked back to the park.
It started to rain. Nobody moved.

The New York Times headline read: "Second Coming
Slams Pope,
Supports Abortion Rights."
The National Star headline read:
"Jesus and Mary: The Inside Story,"
which was also the name of the NBC miniseries.

The second coming appeared on Oprah and Larry King, Today Show and Good Morning America. He skipped Jenny Jones. He gave interviews to C-SPAN, the Wall Street Journal, the New York Times, Wolf Blitzer and Dev Null. His Web site, www.secondcoming.com, got more than a million hits a week.

Planes landed at Kennedy Airport.
Thousands of people flocked to Central Park.
The networks worried about ratings.
The mayor worried about crowd control.
The President worried about his image.

The Pope worried about his power.
He called the President on a secure line.
The Christian Coalition was pissed.
They printed new voter guides.

5

Just before Christmas the stores were empty. Toys stayed on the shelves. Expensive jewelry stayed in its case. Nobody bought gift certificates for McDonald's Happy Meals. The churches were cavernous.

Nobody rode elevators, sat at desks, made important phone calls, sent faxes or e-mail, negotiated deals, underwrote offerings, invested in the internet, speculated about the future of Apple Computer, shopped at Safeway, cleaned the executive bathroom, reviewed the R&D budget, tweaked the distribution system, downsized, upsized or rightsized.

The Conference Board reported Consumer Confidence was at an all-time high.

Consumer Spending was at an all-time low. The economy neared collapse.

The second coming taught from his bench in Central Park in his robe, scraggly beard and sandals appearing a little dazed, or maybe just ethereal. He fed the masses.

6

The President never mentioned the second coming by name. He didn't appear to be concerned. Neither did prime ministers, monarchs, bishops and the Christian Coalition, who held secret teleconferences on secured lines.

7

The second coming knew the day had come.
He did nothing different.
His hands started to bleed. His feet hurt. He got
headaches.
His side ached.
He said nothing.

The second coming sat in silent contemplation before a crowd of half-a-million. Everybody prayed and munched on manna.

The second coming barely noticed the glint in the
tree.
He turned to face God.
It was like slow motion--
the bullet coming towards him.
He spread his arms,
looked toward Home.
"Insanity," he thought, "is doing the same thing
over and over
and expecting different results."
"God, my God," he said. "why does this keep
happening to me?"
```

---

## IC-1682: See Through

- Title: See Through
- Author (byline): Andrea Gibson
- Work: Pole Dancing to Gospel Hymns, Pgs 65-68
- Publisher: Write Bloody Publishing
- Publication date as stated: June 2008
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 786
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andrea Gibson
Book: Pole Dancing to Gospel Hymns, Pgs 65-68
ISBN: 978-0981521305
Publisher: Write Bloody Publishing
Date (Month/Year): June 2008
```

### Introduction (context only: never use it for content warnings)

```text
(Big breath and hold it; let it out in a gush) A bus full of white children in Boulder, Colorado. White privilege as far as the eye can see. Yes, I said it – “white privilege” – but what does that even mean? Spoiled rich kids? No.

White privilege describes the advantages that white people have based on their skin color. You could be poor as “dirt”

(as my daddy used to say) but if you happen to be born white, your skin color has given you a built-in leg up over people of color.

It's difficult for adults to understand the concept, so how do you explain “white privilege” to a group of children? Andrea Gibson ponders this dilemma in her poem See Through
```

### Performance text (classify this)

```text
(Pg 65-68)
We're on our way back to school from gymnastics class.
The kids are singing John Lennon's Imagine
at the back of the bus,

(sing) * . . . Imagine no possessions . . . I wonder if you can . . . No need for greed or hunger . . . A brotherhood of man . . . Imagine all the people . . . Sharing all the world.”

Jesse stops herself mid-verse,
stretches her arm across the aisle like a sunbeam,
tugs at the hem of my shirt and asks,
“What does hatred mean?”

Jesse's five years old.
Anything I say, she's going to believe.
But I realize I don't know the answers.
I don't know what hatred means.
I could guess and say it's the opposite of love.
I could guess and say,
“Jesse, hatred is wanting nothing but white faces
on our private-school bus.”

But Jesse isn't white yet. Go ahead and ask her.

“What color are you, Jesse?”

“Well, it looks like I'm pink.”

Shane thinks he's orange. Skylar says she's tan. Rhett says he's see-through.

“See, you can see how my veins are blue but they're red when i bleed.”

And I wish there was no such thing as springtime.
‘Cause I don't trust the machines
that will one day be planting seeds in these gardens
teaching them that some people are flowers
some people are weeds,
rip the weeds by their roots
ignore their screams
tilt your own face to the sun
take what you want,
you are the chosen ones.

I wanna tell Jesse that Sitting Bull was wrong when he said that white people are liars and thieves.

I wanna tell her we didn't come like a time bomb,
gunpowder on our breath,
teeth built like bullets,
that this land didn't weep when our feet
first mercilessly hit the ground.
I don't wanna say we drowned and maimed the children,
sliced long strips of their skin for bridal reigns.

I don't wanna say the moon was slain,
the constellations dispersed like shrapnel.
Jesse, mothers killed their babies, then killed themselves
when they saw our faces on the horizon
and all that we left was a trail of tears.

But if I have to say that
I wanna say our boats stopped there.
I wanna say the waves never saw the sails of slave ships,
never heard the sound of chain links,
but Jesse, think slaughterhouse.
Think people branded, suffocating, foaming at the mouth.
Can you imagine what kind of pain you would have to

endure
to throw yourself overboard 1200 miles out to sea?
Lungs gratefully exchanging breath for saltwater,
gratefully trading life for death.

Can you imagine being chained to your dead daughter?
How many days would it take you to stop
searching her hands for lifelines?
To stop searching her fingertips for memories of sunshine?
To stop searching her wrists for a pulse,
for just some sign of time turning backwards
to when you just knew
people would never do things like this?

And jesse this
is not just a picture of our history,
not just a picture of our past.
We've been hundreds of years
measuring the size of their hearts
by the size of our fists,
erecting our bliss on the broken backs of dark skin.
The present is far from gift wrapped.

Ask mothers in the Bronx
chasing rats out of their babies’ cribs.
Ask the fathers of the kids
whose lives we exchange for cheap gas.
Ask our prisons why jail bars always come in black.
Ask the woman in Thailand whose cancer build our laptops.
Ask the Mexican man working in a field fertilized by nerve

gas. Ask his daughter when she's born without fingers or hands to pray with.

(ask me how long I could keep going with this list) God might be watching, but we are not.

You are white, Jesse
There are bodies dangling
from the limbs of your family tree.
Our people pull people from their soil like weeds.
Breathe in our story.
Force yourself to hold it in your lungs
‘til you can hear our hymns sung beneath white sheets.
Feel yourself fire as they shout.
Do not look away as bullet enters heartbeat.
Now breathe out.
This is where we come from.
This is still where we are.
Now, where will we go from here?

I don't believe we're hateful.
I think we're just asleep.
But when we wake we can’t call up the dead and say,
“Sorry, we were looking the other way.”

There are names and faces behind our apathy,
eulogies beneath our choices.
There are voices deep as roots
thundering unquestionable truth
through the white noise that pacifies our ears.
Don't tell me we can't hear.
Don't tell me we don't hear.
When the moon is slain,
when the constellations disperse like shrapnel,
don't you think it's time
something changed?
```

---

## IC-1683: Self-Evident

- Title: Self-Evident
- Author (byline): Ani DiFranco
- Work: Ani DiFranco: Verses
- Publisher: Seven Stories Press
- Publication date as stated: September 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1100
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ani DiFranco
Book: Ani DiFranco: Verses
ISBN: 978-1583228234
Publisher: Seven Stories Press
Date (Month/Year): September 2007
```

### Introduction (context only: never use it for content warnings)

```text
We hold these truths to be self evident . . . . • Some 3000 people died in the attacks on the World Trade Center. • Over 3000 people died in the bombing of Afghanistan. • Unknown hundreds of immigrants have been detained and deported. • Over 1.3 million people have joined the ranks of people in the US who are living under the poverty line, and the nation's poverty rate is increasing for the first time in eight years. • A man who was not popularly elected president has declared war on the world.

And where did it all begin . . . September 11, 2001. New York City . . . Soon after the terror attacks, Ani DiFranco began a poem that she ended up calling, "Self Evident."
```

### Performance text (classify this)

```text
yes,
us people are just poems
we're 90% metaphor
with a leanness of meaning
approaching hyper-distillation
and once upon a time
we were moonshine
rushing down the throat of a giraffe
yes, rushing down the long hallway
despite what the p.a. announcement says>
yes, rushing down the long stairs
with the whiskey of eternity
fermented and distilled
to eighteen minutes
burning down our throats
down the hall
down the stairs
in a building so tall
that it will always be there
yes, it's part of a pair
there on the bow of noah's ark
the most prestigious couple
just kickin back parked
against a perfectly blue sky
on a morning beatific
in its indian summer breeze
on the day that america
fell to its knees
after strutting around for a century
without saying thank you
or please

and the shock was subsonic
and the smoke was deafening
between the setup and the punch line
cuz we were all on time for work that day
we all boarded that plane for to fly
and then while the fires were raging
we all climbed up on the windowsill
and then we all held hands
and jumped into the sky

and every borough looked up when it heard the first
blast
and then every dumb action movie was summarily
surpassed
and the exodus uptown by foot and motorcar
looked more like war than anything i've seen so far
so far
so far
so fierce and ingenious
a poetic specter so far gone
that every jackass newscaster was struck dumb and
stumbling
over 'oh my god' and 'this is unbelievable' and on and on
and i'll tell you what, while we're at it
you can keep the pentagon
keep the propaganda
keep each and every tv
that's been trying to convince me
to participate
in some prep school punk's plan to perpetuate
retribution
perpetuate retribution
even as the blue toxic smoke of our lesson in retribution
is still hanging in the air
and there's ash on our shoes
and there's ash in our hair
and there's a fine silt on every mantle
from hell's kitchen to brooklyn
and the streets are full of stories
sudden twists and near misses
and soon every open bar is crammed to the rafters
with tales of narrowly averted disasters
and the whiskey is flowin
like never before
as all over the country
folks just shake their heads
and pour

so here's a toast to all the folks who live in palestine afghanistan iraq

el salvador

here's a toast to the folks living on the pine ridge
reservation
under the stone cold gaze of mt. rushmore
here's a toast to all those nurses and doctors
who daily provide women with a choice
who stand down a threat the size of oklahoma city
just to listen to a young woman's voice

here's a toast to all the folks on death row right now awaiting the executioner's guillotine who are shackled there with dread and can only escape into their heads to find peace in the form of a dream

cuz take away our playstations
and we are a third world nation
under the thumb of some blue blood royal son
who stole the oval office and that phony election
i mean
it don't take a weatherman
to look around and see the weather
jeb said he'd deliver florida, folks
and boy did he ever
and we hold these truths to be self evident:
#1 george w. bush is not president
#2 america is not a true democracy
#3 the media is not fooling me
cuz i am a poem heeding hyper-distillation
i've got no room for a lie so verbose
i'm looking out over my whole human family
and i'm raising my glass in a toast

here's to our last drink of fossil fuels
let us vow to get off of this sauce
shoo away the swarms of commuter planes
and find that train ticket we lost
cuz once upon a time the line followed the river
and peeked into all the backyards
and the laundry was waving
the graffiti was teasing us
from brick walls and bridges
we were rolling over ridges
through valleys
under stars
i dream of touring like duke ellington
in my own railroad car
i dream of waiting on the tall blonde wooden benches
in a grand station aglow with grace
and then standing out on the platform
and feeling the air on my face

give back the night its distant whistle
give the darkness back its soul
give the big oil companies the finger finally
and relearn how to rock-n-roll
yes, the lessons are all around us and a change is waiting
there
so it's time to pick through the rubble, clean the
streets
and clear the air
get our government to pull its big dick out of the sand
of someone else's desert
put it back in its pants
and quit the hypocritical chants of
freedom forever

cuz when one lone phone rang
in two thousand and one
at ten after nine
on nine one one
which is the number we all called
when that lone phone rang right off the wall
right off our desk and down the long hall
down the long stairs
in a building so tall
that the whole world turned
just to watch it fall

and while we're at it
remember the first time around?
the bomb?
the ryder truck?
the parking garage?
the princess that didn't even feel the pea?
remember joking around in our apartment on avenue D?

can you imagine how many paper coffee cups would have
to change their
design
following a fantastical reversal of the new york skyline?!

it was a joke, of course
it was a joke
at the time
and that was just a few years ago
so let the record show

that the FBI was all over that case
that the plot was obvious and in everybody's face
and scoping that scene
religiously
the CIA
or is it KGB?
committing countless crimes against humanity
with this kind of eventuality
as its excuse
for abuse after expensive abuse
and it didn't have a clue
look, another window to see through
way up here
on the 104th floor
look
another key
another door
10% literal
90% metaphor
3000 some poems disguised as people
on an almost too perfect day
should be more than pawns
in some asshole's passion play
so now it's your job
and it's my job
to make it that way
to make sure they didn't die in vain
sshhhhhh....
baby listen
hear the train?
```

---

## IC-1684: The Seven Deadly Sins

- Title: The Seven Deadly Sins
- Author (byline): Yusef Komunyakaa
- Work: Talking Dirty to the Gods
- Publisher: Farrar, Straus & Giroux
- Publication date as stated: 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 597
- Already set (do not supply): none

### Source block (context only)

```text
Author: Yusef Komunyakaa
Book: Talking Dirty to the Gods
ISBN: 978-0374272555
Publisher: Farrar, Straus & Giroux
Date (Month/Year): 2000
```

### Introduction (context only: never use it for content warnings)

```text
The Seven Deadly Sins, when mentioned, conjure up ancient tales of dark deeds and dark characters, like Faustus and Mephistopheles. Dr. Faustus supposedly sold his soul to the devil, the evil Mephistopheles and, in so doing, made himself prey to all types of corruption and degradation.

In his descent into wickedness, the ruined Faustus committed all of these deadly sins: pride, envy, gluttony, lust, anger, avarice, and sloth. These sins were considered deadly because they led Faustus, or any man or woman who would commit them onto a path from which there was no return.

One at a time, Yusef Komunyakaa takes a somewhat unique poetically approach to The Seven Deadly Sins.
```

### Performance text (classify this)

```text
Pride Crowned with a feathered helmet, Not for disguise or courtship Dance, he looks like something Birthed by swallowing its tail, Woven from a selfish design & guesswork. As if masked With a see-through caul From breast to hipbone,

His cold breath silvers
Panes of his hilltop house
Into a double reflection.
Silhouetted almost into a woman,

He can beg forgiveness now
As he leans against a window
Overlooking Narcissus’s pond
Choked with a memory of lilies.

Envy
Icarus imitated the golden plover,
Drawn toward a blue folly
Above, looping through echoes
Of a boy's prankish laughter,
Through an airy labyrinth
Of conjecture. A lifetime
Ahead of Daedalus, with noon sun
In his eyes, he outflew the bird's

Equilibrium, wondering how this Small creature of doubt braved The briny trade winds. Surely, In a fanfare of uneclipsed wings

Driven by dash & breathless style, He could outdo the plover's soars & dares. But he couldn't stop Counting feathers against salty sky.

Gluttony
In a country of splendor & high
Ritual, in a fat land of zeros,
Sits a man with string & bone
For stylus, hunched over his easel,
Captured by perfection.
But also afflictions live behind
Electric fences, among hedges
& a whirlwind of roses, down

To where he sits beside a gully
Pooling desires. He squints
Till the mechanical horizon is one
Shadowplay against bruised sky,

Till the smoky perfume limps
Into undergrowth. He balls up
Another sheet in unblessed fingers, always
Ready to draw the thing that is all mouth.

Lust
If only he could touch her,
Her name like an old wish
In the stopped weather of salt
On a snail. He longs to be
Words, juicy as passionfruit
On her tongue. He'd do anything,
Would dance three days & nights
To make the most terrible gods

Rise out of ashes of the yew,
To step from the naked
Fray, to be as tender
As meat imagined off

The bluegill's pearlish
Bones. He longs to be
An orange, to feel fingernails
Run a seam through him.

Anger We can cut out Nemesis's tongue By omission or simple analysis. Doesn't this sin have to marry Another, like a wishbone

Worked into meat, to grow
Deadly? Snared within
The blood's quick night,
Our old gods made of sex

& wit, of nitrate & titanium,
Hurl midnight thunderbolts
& lightning. Are we here
Because they must question

Every death in an alley,
Every meltdown? We know
We wouldn't be much, if thorns
Didn't drive light into wet blooms.

Avarice
At six, she chewed off
The seven porcelain buttons
From her sister's christening gown
& hid them in a Prince Albert can

On a sill crisscrossing the house
In the spidery crawlspace.
She'd weigh a peach in her hands
Till it rotted. At sixteen,

She gazed at her little brother's Junebugs pinned to a sheet of cork, Assaying their glimmer, till she

Buried them beneath a fig tree's wide,

Green skirt. Now, twenty-six, Locked in the beauty of her bones, She counts eight engagement rings At least twelve times each day.

Sloth (after all it is an animal too!) If you're one of seven Downfalls, up in your kingdom Of mulberry leaves, there are men Betting you aren't worth a bullet,

That your skin won't tan into a good Wallet. As if drugged in the womb & limboed in a honeyed languor, By the time you open your eyes

A thousand species have lived
& died. Born on a Sunday
Morning, with old-world algae
In your long hair, a goodness

Disguised your two-toed claws
Bright as flensing knives. In this
Upside-down haven, you're reincarnated
As a fallen angel trying to go home.
```

---

## IC-1685: Shake the Dust

- Title: Shake the Dust
- Author (byline): Anis Mojgani
- Work: Solomon Sparrows Electric Whale Revival
- Publisher: Write Bloody Publishing
- Publication date as stated: Sept 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 626
- Already set (do not supply): none

### Source block (context only)

```text
Author: Anis Mojgani
Book: Solomon Sparrows Electric Whale Revival
ISBN: 978-0978998998
Publisher: Write Bloody Publishing
Date (Month/Year): Sept 2007
```

### Introduction (context only: never use it for content warnings)

```text
Charles Dickins once said: “Reflect on your present blessings, of which every man has many; not on your past misfortunes, of which all men have some.” In other words, leave the past behind. Whether we like to admit it or not we all are living today with some emotional baggage. While some may have more deeply rooted baggage that affects their day to day living we can all recognize within us those times in our lives which continue to affect the way we think, our view of our self worth and the way we interact with others around us. It might have been a time when someone told you that you weren't smart enough, maybe someone commented about your looks or you made some bad choices. Whatever it is that baggage may well be holding you back from allowing you to become the person you are meant to be. Anis Mojgani, two- time National Poetry Slam winner, pays tribute to anyone who has struggled in the past and urges everyone to Shake the Dust by Anis Mojgani.
```

### Performance text (classify this)

```text
This is for the fat girls This is for the little brothers

For the former prom queen
And for the milk crate ball players
This is for the school yard wimps
And the childhood bullies that tormented them
Shake the dust.

This is for the benches and the people sitting upon them. This is for the bus drivers driving a million broken hymns And for the men who have to hold down 3 jobs,

Simply to hold up their children.
For the nighttime schoolers
And for the midnight bike riders trying to fly
Shake the dust.

For the two year olds who cannot be understood because they speak half English and half god Shake the dust

For the girl whose brother is going crazy
For the gym class wall flower
And for the 12 year olds that are afraid of taking public
showers
For the kid who's always late to class because he
forgets the combination to his locker
For the girl who loves somebody else
Shake the dust.

This is for the hard men Who want love, but know that it won't come For the ones who are forgotten

For the ones whose amendments do not stand up for
For the ones who are told to speak only when they are
spoken to
And then are never spoken to
Speak every time you stand
So that you do not forget yourself
Never let a moment go by that doesn't remind you
That your heart beats 100 000 times a day
And that there enough gallons of blood
To make everyone of you an ocean

Do not settle for letting these waves settle
And for the dust to collect in your veins.
This is for the celibate pedophile who keeps on
struggling

For the poetry teachers And for the people who go on vacations alone For the sweat that drips of a Mick Jagger singing lips And for the shaking skirt on Tina Turners shaking hips And For the heavens, and for the hells through which Tina has lived

This is for the tired and the dreamers
And for those families that will never be like the
Cleavers
With perfectly made dinners, and songs like Wally and
the Beaver
This is for the bigots
This is for the sexists
This is for the killers
This one is for the big house jail sentenced cats
becoming redeemers
And for the springtime, that somehow always shows up
after every single winter

This is, This is for you.

Make sure that by the time the fisherman returns You are gone Because just like the days, I burn at both ends And every time I write, every time I open my eyes I am cutting out a part of myself Just to give it to you. So shake the dust and take me with you do

For none of this, has ever been for me
All that pushes and pulls
And pushes and pulls
Pushes for you
So grab the world by its clothes pins
And shake it out again, and again
And jump on top and take it for a spin
And when you hop off, shake it again

For this is yours
Make my words worth something
Make this not just another poem that I write
Make it like its heavy about us all
And walk into it, breathe it in
Let it crash through the halls of your arms
Like the millions of years, of millions of poets
Coursing like blood
Pumping and pushing, making you live

Shaking the dust
So when the world knocks at your front door
Clutch the knob tightly, and open on up
Run forward into its wide spread greeting arms
With your hands before you
Your fingertips trembling
Though they may be
```

---

## IC-1686: Shel Silverstein Program

- Title: Shel Silverstein Program
- Author (byline): Shel Silverstein
- Work: A Light in the Attic
- Publisher: HarperCollins
- Publication date as stated: Oct 1981
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1093
- Already set (do not supply): none

### Source block (context only)

```text
For Sale, Boa Constrictor, Sick, Smart and Where the
Sidewalk Ends
Author: Shel Silverstein
Book: Where the Side Walk Ends
ISBN: 978-0060256678
Publisher: HarperCollins
Date (Month/Year): Nov 1974
Invitation, Overdues, Prayer of the Selfish Child, How Not
to Have to Dry the Dishes, Wavy Hair, Deaf Donald and
Homework Machine
Author: Shel Silverstein
Book: A Light in the Attic
ISBN: 978-0060256739
Publisher: HarperCollins
Date (Month/Year): Oct 1981
```

### Introduction (context only: never use it for content warnings)

```text
Shel Silverstein is one of America’s most celebrated children’s poets. And while there is poetry appropriate for every age, the best lessons may come from the lines intended for children. With stanzas that make us laugh and reflect, Shel Silverstein wrote for kids -- and the kid inside all of us. In fact, the sheer joy I recall feeling while reading his poems is one of the fondest memories of my childhood. This collection of poetry comes from two of Silversteins’s popular publications: Where the Sidewalk Ends and A Light in the Attic.
```

### Performance text (classify this)

```text
“Listen to the mustn'ts, child. Listen to the don'ts. Listen to the shouldn'ts, the impossibles, the won'ts. Listen to the never haves, then listen close to me . . . Anything can happen, child. Anything can be.” -- Shel Silverstein

INVITATION
If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer. . .
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!

OVERDUES
What do I do?
What do I do?
This library book is 42
Years overdue.
I admit that it’s mine
But I can’t pay the fine –
Should I turn it in
Or hide it again?
What do I do?
What do I do?

PRAYER OF THE SHELFISH CHILD
Now I lay me down to sleep,
I pray the Lord my soul to keep,
And if I die before I wake,
I pray the Lord my toys to break.
So none of the other kids can use ‘em. . . .
Amen.

FOR SALE
One sister for sale!
One sister for sale!
One crying and spying young sister for sale!
I’m really not kidding,
So who’ll start the bidding?
Do I hear a dollar?
A nickel?
A penny?
Oh, isn’t there, isn’t there, isn’t there any
One kid who will buy this old sister for sale,
This crying and spying young sister for sale?

HOW NOT TO HAVE TO DRY THE DISHES
If you have to dry the dishes
(Such an awful, boring chore)
If you have to dry the dishes
(‘Stead of going to the store)
If you have to dry the dishes
And you drop one on the floor—
Maybe they won’t let you
Dry the dishes anymore.

WAVY HAIR
I thought that I had wavy hair
Until I shaved. Instead
I find that I have straight hair
And a very wavy head.

BOA CONSTRICTOR
Oh, I’m being eaten
By a boa constrictor
A boa constrictor,
A boa constrictor,
I’m being eaten by a boa constrictor,
And I don’t like it – one bit.
Well, what do you know?
It’s nibblin’ my toe.
Oh, gee,
It’s up to my knee.
Oh my,
It’s up to my thigh.
Oh, fiddle,
It’s up to my middle.
Oh, heck,
It’s up to my neck.
Oh, dread,
It’s upmmmmmmmmmffffffff…

SICK
“I cannot go to school today,”
Said little Peggy Ann McKay.
“I have the measles and the mumps,
A gash, a rash and purple bumps.
My mouth is wet, my throat is dry,
I’m going blind in my right eye.
My tonsils are as big as rocks,
I’ve counted sixteen chicken pox
And there’s one more – that’s seventeen,
And don’t you think my face looks green?
My leg is cut, my eyes are blue –
It might be instamatic flu.
I cough and sneeze and gasp and choke,
I’m sure that my left leg is broke –
My hip hurts when I move my chin,
My belly button’s caving in,
My back is wrenched, my ankle’s sprained,
My ‘pendix pains each time it rains.
My nose is cold, my toes are numb,
I have a sliver in my thumb.
My neck is stiff, my voice is weak,
I hardly whisper when I speak.
My tongue is filling up my mouth
I think my hair is falling out.
My elbow’s bent, my spine ain’t straight,
My temperature is one-o-eight.
My brain is shrunk, I cannot hear,
There is a hole inside my ear.
I have a hangnail, and my heart is – what?
What’s that? What’s that you say?
You say today is . . . Saturday?
G’bye, I’m going out to play!”

MY RULES If you want to marry me, here’s what you’ll have to do: You must learn how to make a perfect chicken-dumpling

stew.
And you must sew my holey socks,
And soothe my troubled mind,
And develop the knack for scratching my back,
And keep my shoes spotlessly shined.
And while I rest you must rake up the leaves,
And when it is hailing and snowing
You must shovel the walk . . . and be still when I talk,
And – hey—where are you going?

DEAF DONALD Deaf Donald met Talkie Sue But (sign language for I love you) was all he could do.

And Sue said, “Donald, I sure do like you.” But (sign language for I love you) was all he could do.

And Sue Asked Donald, “Do you like me too?” But (sign language for I love you) was all he could do.

“Good-bye then, Donald, I’m leaving you.” But (sign language for I love you) was all he could do.

And she left forever so she never knew That (sign language for I love you) means I love you.

SMART
My dad gave me one dollar bill
‘Cause I’m his smartest son,
And I swapped it for two shiny quarters
‘Cause two is more than one!

And then I took the quarters
And traded them to Lou
For three dimes – I guess he don’t know
That three is more than two!

Just then, along came old blind Bates
And just ‘cause he can’t see
He gave me four nickels for my three dimes,
And four is more than three!

And I took the nickels to Hiram Coombs Down at the seed-feed store, And the fool gave me five pennies for them, And five is more than four!

And then I went and showed my dad,
And he got red in the cheeks
And closed his eyes and shook his head –
Too proud of me to speak!

HOMEWORK MACHINE The Homework Machine, oh the Homework Machine, Most perfect contraption that’s ever been seen. Jut put in your homework, then drop in a dime, Snap on the switch, and in ten seconds’ time, Your homework comes out, quick and clean as can be. Here it is –“nine plus four?” and the answer is “three.” Three? Oh me . . . I guess it’s not as perfect As I thought it would be.

WHERE THE SIDEWALK ENDS
There is a place where the sidewalk ends
And before the street begins
And there the grass grows soft and white,
And there the sun burns crimson bright,
And there the moon-bird rests from his flight
To cool in the peppermint wind.

Let us leave this place where the smoke blows black And the dark street winds and bends. Past the pits where the asphalt flowers grow We shall walk with a walk that is measured and slow And watch where the chalk-white arrows go To the place where the sidewalk ends.

Yes we’ll walk with a walk that is measured and slow And we’ll go where the chalk-white arrows go For the children, they mark, and the children, they know The place where the sidewalk ends.
```

---

## IC-1687: Shosholoza and Hand-Me-Downs

- Title: Shosholoza and Hand-Me-Downs
- Author (byline): Sarah Kay
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1522
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sarah Kay
Book: No Matter the Wreckage
ISBN: 978-1938912481
Publisher: Write Bloody Publishing
Date (Month/Year): March 2014
Author: Sarah Kay
Book: No Matter the Wreckage
ISBN: 978-1938912481
Publisher: Write Bloody Publishing
Date (Month/Year): March 2014
```

### Introduction (context only: never use it for content warnings)

```text
The year was 1965. The apartheid government swooped into District Six, Cape Town, South Africa, forcibly removing its occupants and declaring the area a "whites-only" zone. The rich fabric of an impoverished but vibrant community was torn to shreds. Over 60, 000 people were wrenched from their homes, livelihoods, community centers and societal networks, and relocated to the bleak plains of the Cape Flats, several kilometers away. District Six in Cape Town posed a threat to the apartheid government, which was intent on enforcing "separate development" for different ethnic groups. Across the ocean, Martin Luther King was leading the Civil Rights march from Selma to Montgomery Alabama.

Shosholoza

(hear pronunciation here http://www.howtosay.us/pronounce-shosholoza/) by Sarah Kay
```

### Performance text (classify this)

```text
Shosholoza *NOTE: This poem begins and ends with the song “Shosholoza,” a Ndebele folk song that some hail as the “unofficial” or “second” national anthem of South Africa. It was sung by migrant workers in South African mines as a song of resistance and solidarity. The very rough translation is: Moving fast, moving strong, through these mountains like a rolling train to South Africa. You are leaving, you are leaving though these mountains like a rolling train from Zimbabwe.

Shosholoza, ku lezontaba stimela siphume South Africa Wenu yabaleka, ku lezontaba stimela siphume Zimbabwe

Noor Ebrahim had fifty homing pigeons.
He lived in District Six at the center of Cape Town.
Noor Ebrahim lived with fifty pigeons in District Six at
the center of Cape Town, where there were twelve
schools
and the Holy Cross Church, and the Aspeling Street
Mosque
and the Jews on Herrington Street. With the
immigrants and
the natives, the Indians and the Malays,
the Blacks and the Coloureds. Noor Ebrahim lived with
fifty pigeons
in District Six at the center of Cape Town, where there
was
Beikinstadt Bookstore and Parker’s corner shop; where
you could
buy bread and paraffin for the stove, fish oil, bulls-eyes
and almond rock; where you could walk to the public
baths,
pay a ticky, get a fifteen-minute shower, and find
yourself between
the gangsters and the businessmen bathing side-by-side,
right there,
at the corner of Clifton and Hanover Streets.
Nor Ibrahim lived in District Six at the center of Cape
Town
With fifty pigeons and his family.
Now watch.
Take 1 city: Cape Town
Divide it into 12 districts.
Now take one of them, District 6,
Add 70,000 people over time.
Divide that by the Group Area Act of 1950
and you wind up with what?

I’ll give you a hint. It’s the same as if you were to divide by race So you’re left with the remainder of 1 Apartheid Government and 1 declaration of 1966 which stated that from now on District 6 would be officially recognized as a designated whites-only area.

So no more Handover Street with the thick smell of curry coming from Dout’s café, and no more Janjura’s groceries, Maxim’s sweeterie, Waynik’s school uniforms, and the sound of children. Shoppers. Merchants. Buses. Laughter. Song. No.

At the end of all that, you are left with only bulldozers. Leveled buildings. Raised land. Broken glass and brick. Not even phantoms will haunt this ghost town, because even their floating figures are not white enough.

Noor Ebrahim moved the ten kilometers to Athlone. He packed fifty pigeons into their cages and left District Six at the center of Cape Town. He left the Peninsula Maternity Home where hundreds of coloured babies were born every year and the soda fountain where you could watch the ladies bring their laundry down to the public washhouse three times a week. He left his house on Caledon Street. Noor Ebrahim left his home on Caledon Street in District Six at the heart of Cape Town and moved the ten kilometers to Athlone.

He lived there for weeks, sometimes driving past the empty pit of land where District Six no longer stood. The winds blew hard, and they swept through the dust and the dirt and the broken glass until every blade of grass bent beneath the weight of what was no longer there.

After three months, the droppings at the bottom of the birdcages had become three layers thick. Noor Ebrahim decided it was time to let the pigeons fly free -- fly free so they could find their way back. He knew that not all of them would return that night. He knew that the next morning, some of those cages might not be as full. But he also knew that sometimes, gravity can become a little too comfortable. So that morning, Noor Ebrahim opened the doors on the cages, and the winds that swept through Cape Town swept through and lifted all fifty pigeons up into the air in a cloud of feathers, as if to say,

It does not matter how long we have been kept in cages. It does not matter how strong your gravity is. We were always meant to fly.

That night, Noor Ebrahim returned from work. He turned off the car, went around to the back of the house, and cried out in pain. Not a single bird had come back to him. The cages were lined with droppings and feathers, but no pigeons. The man who had watched them level his house to the ground without shedding a single tear, now felt his mind go cloudy and his ribcage felt as empty as the ones the bird had abandoned.

He got back into the car to take a drive and clear his mind.

As he drove down the long streets of Cape Town, the wheel moved beneath his hands and he found himself on the abandoned roads of District Six. And as he reached Caledon Street, Noor Ebrahim slowed to a stop. Because there on the empty plot of land where his house once stood, were pigeons. All fifty of them. Standing amongst the dust and the dirt and the broken glass, looking up at him as if to say, Where is our home?

South Africa. We sing a song of strength.
We go on like a rolling train forever.
We never let gravity become too familiar
Because we were always meant to fly.

Shosholoza, ku lezontaba stimela siphume South Africa Wenu yabaleka, ku lezontaba stimela siphume Zimbabwe

INTRODUCTION Apartheid in South Africa, the Civil Rights Movement in the U.S. . . . that was so long ago. Down through the ages racism has been an issue in almost every society.

Many Americans would like to claim that racism doesn’t exist anymore . . . not in our country; but the fact of the matter is . . . racism does and will continue to exist not only in America, but throughout the world. Why? Racism is a tradition that is passed down from one generation to the next – it is the anger spawned by focusing on the negative and seeing only the “differences.” Every culture . . . EVERY culture . . . is guilty of harboring some degree of racism – We wear it like . . . .

Hand-Me-Downs by Sarah Kay.

Hand-Me-Downs

I know you’ve taken to wearing around your father’s hand-me-down anger. But I wish that you wouldn’t. It’s a few sizes too big and everyone can see it doesn’t fit you, makes you look silly, hangs loose at all the wrong places, even if it does match your skin color.

I know you think you’ll grow into it: that your arms will beef up after all the fighting and it will sit on your shoulders if you pin it on the right places with well-placed conviction.

The bathroom mirror tells you, you look good, your fists look a lot more justified. When you dig your hands deep into the pockets, you’ll find stories he left there for you to hand out to the other boys like car bombs.

On days when everything else is slipping through your fingers, you can wrap yourself inside of this anger. This will keep you warm at night, help you drift off to sleep with the certainty that no matter what happens, it will still be there when you wake up.

The longer you wear it, the better it fits. Until some of those stories are your own. The holes in the sleeve are from the bullets you dodged yourself. When it rips, snags on a barbed wire fence or someone else’s family, don’t worry.

Your mother and your sister will mend it: patch the holes, sew the tears, replace a button or two. They will help you back into it and tell you how proud they are of you; how good it looks on you. The same way it looked on your dad and your granddad, too.

And on his father before him and on his father before him. But back then? Back then there was only sand. Until someone drew a line. Someone built a wall. Someone threw a stone.

And the crack in the skull that it hit fractured perfectly like twigs on the branches of a family tree, So someone

threw a stone back. And each fracture, each tiny break wound itself together into thread. The thread pulled itself around him, your great-great-great-great-somebody. And on the other side of the wall, they were knitting just as fast and theirs fit them just as well, only in a slightly different shade.

So I’m asking, when the time comes, who is going be the first to put down the needle and thread? Who is going be the first one to remember that their grandfather suffered just as many broken windows, broken hearts, broken bones? And the first time

you come down to dinner, and your son is sitting at the dining room table wearing your hatred on his shoulders, who is going to be the first to tell him it is finally time to take it off?
```

---

## IC-1688: Silence is Not an Option - A Collection

- Title: Silence is Not an Option - A Collection
- Author (byline): Christopher Michael and Denice Frohman
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1305
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Michael
ISBN: N/A
Publisher: Poem Hunter.com
Date (Month/Year): Posted March 17, 2017
On-Line Location:
https://www.poemhunter.com/poem/16th-street-baptist-
church-speaks-by-michael-christopher/
Author: Denice Frohman
ISBN: N/A
Publisher: SplitThisRock.org
Date (Month/Year): Posted Jul 22, 2016
On-Line Location:
https://www.splitthisrock.org/poetry-database/poem/the-
hour-dylann-roof-sat-in-the-church
```

### Introduction (context only: never use it for content warnings)

```text
Martin Luther King, Junior once said, “Our lives begin to end the day we become silent about things that matter.” Today I choose to raise my voice, silence is not an option.

The Baptist church on 16th Street in Birmingham, Alabama was known as “everybody’s church” -- a center for educational and intellectual activities. On September 15, 1963, members of the Ku Klux Klan planted a bomb at the church. It exploded just after Sunday services, killing four young girls and generating international outrage that provided the impetus for passage of the Civil Rights Act of 1964.
```

### Performance text (classify this)

```text
Note: Links to historical information about the events inspiring each poem can be found at the end of this selection.

16th Street Baptist Church Speaks by Christopher Michael

I was born in Birmingham, Alabama in 1911 on 16th

Street.
By born, I mean they finish my construction.
I was erected as an edifice to the Almighty
A place the worship.
A rally point for justice fighters
And a war room for the commanders of the cause.
I can name drop, but that would be rude:
Martin Luther King, Ralph David Abernathy.
Thousands of people release millions of
prayers beneath my roof.
I stood witness to hopes, dreams, marriages and baptisms.
But of all the dignitaries to grace my pews,
The most important, the most precious were Denise, Addy

Mae, Carolyn and Cynthia. Those 4 girls were visiting me for Sunday school or

something to like. There's a lot of turmoil in the old days. I could tell because of all the comings and goings and

whatnot.
Some fuss about integration.
Even our illustrious Governor, George Wallace, has
something to say about the issues of the day.
Let me see, I think what he said was: 'to stop integration,

Alabama needed a few first-class funerals.' Shortly after, a white gentleman placed a package under

my steps.
At the time I was over 50 years old and I had I grown to
know what the faces of men meant.
Each one told a story or revealed his heart.
I knew that was no gift set before me.
I could feel the spirit of the Lord shutter with grief and I
knew I had to do something, for those four little girls are

still within me.
Girls! Girls you gotta get! Get on from round here!
But maybe, if my steeple wasn't such a tower,
I could do more than babble.
I tried so hard.
I yelled with everything I had:
Girls! Girls you gotta get -- Get on home now!
But all they can hear was me moan and creak like I was

settling in my foundation. I was no longer like the servant Peter, I could not be their

rock. In that split second of eternity, I tried to contain the blast. I held back the wave of Satan's Hellfire like I hold on every

prayer whispered in my walls.
I used all my strength to stop the embers.
I refused the shards.
I stopped the splitters.
I bound every brick.
I subdued the mortar.
I stood in the gap in the twinkling of an eye,
My God needed to call them home.
And in that moment of forever, they felt the love of my

Lord!
But even eternity must end.
I could not hold back the blast forever and I realized
all I could do was blanket their bodies
in what was left of me.
Swallow them in my destruction.
Tuck them in with my dust.

I won't name the white supremacist who was convicted of

this horrific crime, But Denise McNair, Addy Mae Collins, Carole Robertson

and Cynthia Wesley transfigured into a spark,
that fans the plains of freedom!
And I,
I had the honor,
I had the . . .
I am so sorry that I could not save you.

TRANSITION

50 years later, America has evolved, hate crimes are a thing of the past, and we value our countries diversity. Right? . . . Not everyone . . .

On the evening of June 17, 2015, a mass shooter took the lives of nine African American people at a Bible study at Emanuel African Methodist Episcopal Church in Charleston, South Carolina. The massacre at a historic Black church deeply shook a nation already jaded by frequent gun violence and heralded the return of violent white nationalism in America.

The Hour Dylann Roof Sat in the Church by Denice Frohman I.

By now, you know their names, their cheekbones— the tender hands they offered when you walked in.

You know the quivering strength of prayer and the art of

making God listen. How faith can summon weary backbones into pyramids.

And you know that grace still lives in a church that’s had to

rebuild itself before— a church that’s cleaned more blood off the walls than you

have ever fantasized of.

That is to say, you’re not the first white boy to feel small and create chaos in someone else’s home.

This church is old – much older than you, wears the audacity of freshly coated white paint

as if to say any ill that smudges us will be for all to see.

Did you hear the echoes when you walked in? Did you feel

the pastor soothe the trepidatious voices of ghosts burnt and hung in the

name of better days?

So they opened their song for you – shared in head nod and

Bible verse – not knowing they let in what they spent so much time

praying out

tucked away nearly 400 years of lessons on what it means to let a white man get too close.

All the bullets in all the world belong to them, yet doors

softened for you— what an unearned miracle.

Do you know what it means to welcome a familiar terror

and hope it got enough God on it this time to leave you be? Is there some word greater

than “noble”?

Your predecessors hid their faces, threw Molotov cocktails

from afar but your ugly is the kind that gets to know what it's about

to kill.

In that hour, were you studying them like elk? Were you surprised when they prayed for you, even as you

preyed on them?

Did they greet you with too many, come on ins? Did you imagine abandoned prayers?

Did your teeth clench when they said, God forgives you? Did your jaw tighten when they said, Bless your heart?

Did their soft voices almost provoke the rage out of you?

Did you wonder how the hell they were still standing? Why god hadn’t made good on the fire next

time?

Did your skin itch when the congregation said your name like it was worth keeping?

Did you look at their hands? The folds of their skin? Did you panic then?

Did you forget who the animal was? Did you leave hoofed, and grunting with a new tail?

Did the gun begin to rattle? Did the heavy metal fever and sweat?

Did the script get hazy? Did you forget your lines?

Is that when you almost walked out?

How many crosses did you have to burn in your head to remember what you came for?

How many names did you have to unlearn?

II.

Did your hands turn black after you threw your gun down?

Did the bullets pull themselves out of their skin, and chase you out? Is that why you ran,

boy?

Why you could stay for Bible study, but not to see what

music God still offers the dead to keep them warm?

Did you hear your father say, good job son? Did you hear

America say, good job son? Did you hear every history textbook write your name?

Did you wink at the police when they searched your

pockets? Did you say, hey, brother? Did they say, hey, back?

When you realized they were enjoying you, was it then that

you shot them all? Was it then that you could not say you enjoyed them too?

When you see God, will he tell you how bad you smell? Will you say you already know?

A stench like this isn’t made overnight, takes a whole lot of hands and much longer than an hour.

Historical accounts of events referenced in each poem can be found here. 16th Street Baptist Church Bombing: https://www.history.com/topics/1960s/birmingham-church-bombing Emanuel African Methodist Episcopal Church Shooting: https://www.history.com/this-day-in-history/charleston-ame-church-shooting
```

---

## IC-1689: Simon Says (is Not a Game)

- Title: Simon Says (is Not a Game)
- Author (byline): Ashley Davis and Lakiyra
- Work: Not specified
- Publisher: Urban Word NYC
- Publication date as stated: 2016 National Poetry Slam Finals;
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 604
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ashley Davis and Lakiyra Williams
(aka Oompa)
https://www.youtube.com/watch?v=ZcBix3sUmXk
(video transcript published online March 13, 2021)
Select “More,” then “Show Transcript
Publisher: Urban Word NYC
Date (Month/Year): 2016 National Poetry Slam Finals;
Atlanta, GA
```

### Introduction (context only: never use it for content warnings)

```text
The game has begun. It looks harmless. After all, in elementary school, Simon Says is used to promote listening skills. But beneath the laughter, Simon Says quietly builds habits that mirror survival in prison: constant vigilance, strict obedience, and the suppression of personal needs. Through repetition and authority, the poem will challenge you to question how environments meant to educate can instead condition students to accept confinement, tracing a disturbing line between learning to listen and learning to submit.

Simon Says by Ashley Davis and Lakiyra Williams (aka Oompa)
```

### Performance text (classify this)

```text
Williams (aka Oompa)

You know how it goes . . .
When Simon says do an action, you do an action
But only do an action if Simon says . . . Ready?
Simon Says: Raise your right hand
Simon Says: Put your right hand down
Simon Says: Raise your left hand
Put your left hand down
Oh, y'all look good . . . okay
Simon Says: Put your left hand down
Now cross your arms.
No, Simon didn't say cross your arms
You need to make sure you're listening.
Okay, Simon Says: Smile. Show us your teeth.
You're only as valuable as you are able.
Simon Says: Raise your right hand again
Wave.
Why are you waving?
You don't know how to listen.
You must not be a good listener at home.
Simon Says: It's not time for a bathroom break.
You go when Simon says;
Eat when Simon says;
Leave this room when Simon says.
There's only one rule: Only do what Simon says
Simon Says: Only speak when you are told to speak.
Simon Says: Speak to your neighbor.
Now why isn't everyone speaking?
You chose to play this game,
Now you're choosing not to play . . .
How dare you ruin it for everyone else!

Simon Says: Still not time for a bathroom break
And stop asking.
Simon Says: You're not listening.
People that don't listen will never be successful.
You know what? They don't even care!
Just take out a book and shut up. Read.
Simon Says: Read.
Simon Says: It's time to file into the hallway now
One behind the other;
Straight silent line, tight to the right.
Simon Says: If you can't be silent,
How will you hear what Simon is telling you to do?
Silence! I said be silent!
Simon Says: Be silent!
Simon Says: Only 20 minutes to eat your lunch and
Be silent.
Eat faster! Eat faster!
Simon Says: Sit up straight and be still.
Simon Says: Tuck in your uniform.
You don't want to tuck in your uniform?
Go sit in the corner!
Simon Says: If you can't handle this classroom,
How will you handle your jail cell?
Simon Says: You will refer to it as Officer Simon from

here on.
And Officer Simon Says: Know your place.
Officer Simon Says: Show your teeth, boy.
You're only as valuable as you are able.
Officer Simon Says: Put your hand down.
We don't raise hands here.
There are no questions here.
Officer Simon Says: You must not be a good listener at

home. At this rate you'll not be going back home. Officer Simon Says: You will speak only when you are

told to speak
Officer Simon Says: Speak to your cell mate.
Now, why aren't you speaking?
You chose to play this game;
Now you're choosing not to play.
How dare you ruin it for everyone else.
Officer Simon Says: It's still not time for a bathroom

break Stop asking!

Officer Simon Says: You're not listening! People that don't listen will never be successful Officer Simon Says: It's time to file into the hallway

again.
One behind the other
Straight silent line. Tight to the right.
Officer Simon Says: If you can't be silent,
How will you hear what Officer Simon is telling you to

do?
Silence! I said be silent!
Officer Simon Says: Be silent!
Fix your uniform!
Fix your face when you're talking to me!
Clean your bunk, you animal.
Sit up straight!
I don't care if I didn't say Officer Simon Says.
Officer Simon said it, so sit up straight and be still!
Be still!
Be still!
Officer Simon Says: If you can't handle your jail cell,
How will you handle your casket?
```

---

## IC-1690: The Sneetches

- Title: The Sneetches
- Author (byline): Theo Geisel (aka Dr. Suess)
- Work: Not specified
- Publisher: Random House, Inc.
- Publication date as stated: Aug 1961
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: NARRATOR, STAR BELLIED SNEETCHES, MCBEAN, PLAIN BELLIED SNEETCHES
- Teaser before the introduction: Yes
- Spoken words (computed): 815
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Suess)
ISBN: 978-0394800899
Publisher: Random House, Inc.
Date (Month/Year): Aug 1961
```

### Introduction (context only: never use it for content warnings)

```text
At first glance, The Sneetches by Theodor Seuss Geisel feels like a simple children’s story -- bright creatures, ridiculous machines, and a problem as silly as stars on bellies. It invites us to laugh, to relax, to believe this is just another harmless rhyme.

But listen a little closer, and the humor starts to shift. Today division doesn’t feel trivial. It feels constant. It feels loud. It feels uncomfortably real, as people sort themselves into political and moral parties and question the worth of others . . . And that’s when the laughter at a silly children’s story gets quiet.

The Sneetches by Theodore Geisel (aka Dr. Suess)
```

### Performance text (classify this)

```text
NARRATOR: Now the Star-bellied Sneetches had bellies with stars. The Plain-bellied Sneetches had none upon thars. The stars weren't so big; they were really quite small. You would think such a thing wouldn't matter at all. But because they had stars, all the Star-bellied Sneetches would brag . . .

STAR BELLIED SNEETCHES: We're the best kind of Sneetch on the beaches.

NARRATOR: With their snoots in the air, they would sniff and they'd snort . . .

STAR BELLIED SNEETCHES: We'll have nothing to do with the plain-bellied sort.

NARRATOR: And whenever they met some, when they were out walking, they'd hike right on past them without even talking.

NARRATOR: When the Star-bellied children went out to play ball, could the Plain-bellies join in their game? Not at all! You could only play ball if your bellies had stars, and the Plain-bellied children had none upon thars. When the Star-bellied Sneetches had frankfurter roasts, or picnics or parties or marshmallow toasts, they never invited the Plain-bellied Sneetches. Left them out cold in the dark of the beaches. Kept them away; never let them come near, and that's how they treated them year after year.

Then one day, it seems, while the Plain-bellied Sneetches were moping, just moping alone on the beaches, sitting there, wishing their bellies had stars, up zipped a stranger in the strangest of cars.

MCBEAN: My friends . . .

NARRATOR: He announced in a voice clear and keen

MCBEAN: My name is Sylvester McMonkey McBean. I've heard of your troubles; I've heard you're unhappy. But I can fix that; I'm the fix-it-up chappie. I've come here to help you; I have what you need. My prices are low, and I work with great speed, and my work is one hundred percent guaranteed.

NARRATOR: Then quickly, Sylvester McMonkey McBean put together a very peculiar machine. Then he said . . .

MCBEAN: You want stars like a Star-bellied Sneetch? My friends, you can have them . . . for three dollars each. Just hand me your money and climb on aboard.

NARRATOR: They clambered inside and the big machine
roared.
It bonked. It clonked. It jerked. It berked.
It bopped them around, but the thing really worked.

When the Plain-bellied Sneetches popped out, they had
stars!
They actually did, they had stars upon thars!
Then they yelled at the ones who had stars from the start,

PLAIN BELLIED SNEETCHES: We're exactly like you; you can't tell us apart. We're all just the same now, you snooty old smarties. Now we can come to your frankfurter parties!

STAR BELLIED SNEETCHES: Good grief! We're still the best Sneetches, and they are the worst. But how in the world will we know if which kind is what or the other way 'round?

NARRATOR: Then up stepped McBean with a very sly wink, and he said . . .

MCBEAN: Things are not quite as bad as you think. You don't know who's who, that is perfectly true. But come with me, friends, do you know what I'll do? I'll make you again the best Sneetches on beaches, and all it will cost you is ten dollars eaches. Belly stars are no longer in style. What you need is a trip through my stars-off machine.

This wondrous contraption will take off your stars, so you won't look like Sneetches who have them on thars.

NARRATOR: That handy machine, working very precisely, removed all the stars from their bellies quite nicely. Then, with snoots in the air, they paraded about. They opened their beaks and proceeded to shout . . .

STAR BELLIED SNEETCHES: We now know who's who, and there isn't a doubt, the best kind of Sneetches are Sneetches without.

NARRATOR: Then, of course those with stars all got frightfully mad. To be wearing a star now was frightfully bad. Then, of course old Sylvester McMonkey McBean invited them into his stars-off machine. Then, of course from then on, you can probably guess, things really got into a horrible mess.

All the rest of the day on those wild screaming beaches,
the Fix-it-up-Chappie was fixing up Sneetches.
Off again, on again, in again, out again,
through the machine and back round about again,
still paying money, still running through,
changing their stars every minute or two,
until neither the Plain- nor the Star-bellies knew
whether this one was that one or that one was this one
or which one was what one or what one was who!

Then, when every last cent of their money was spent, the Fix-It-Up-Chappie packed up and he went. And he laughed as he drove in his car up the beach. . .

MCBEAN: They never will learn; no, you can't teach a Sneetch!"

NARRATOR: But McBean was quite wrong, I'm quite happy to say, the Sneetches got quite a bit smarter that day. That day, they decided that Sneetches are Sneetches, and no kind of Sneetch is the BEST on the beaches. That day, all the Sneetches forgot about stars, and whether they had one or not upon thars.
```

---

## IC-1691: Somewhere in Germany

- Title: Somewhere in Germany
- Author (byline): Buzzy Enniss
- Work: Letting Myself Go
- Publisher: Write Bloody Publishing
- Publication date as stated: March 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 742
- Already set (do not supply): none

### Source block (context only)

```text
Author: Buzzy Enniss
Book: Letting Myself Go
ISBN: 978-0978998943
Publisher: Write Bloody Publishing
Date (Month/Year): March 2007
```

### Introduction (context only: never use it for content warnings)

```text
What defines a person? Is it our DNA, where we grew up, or is it the family we are born into? I am struck by the question of what is an identity. Who are we without the people, places and things that surround us? Does my name define me, the place I live or the family I come from? Does my country or the planet define me? Who does God say I am? Will that answer suffice when all around me seems changed? Buzzy Enniss explores this concept of how a person is defined in his poem “Somewhere in Germany.”
```

### Performance text (classify this)

```text
Somewhere in Germany A woman invented a thing.

A thing that you do not yet know about.

She invented a microscope so powerful that it can sink directly past skin And look deeper into cells than ever before.

Now you know about the thing.

It has revealed that people are actually made up of words.

Baffled doctors and embarrassed scientists Have completed the connection of this microscope to a monitor.

The insecure are running frantically to wait in the line that leads to the lens That will display their hopefully amazing words on the monitor.

Many people have ended up feeling sad as they realize their words are the same as The person’s right before them and directly after them.

JEANS, COFFEE, TV, next please JEANS, COFFEE, TV, next please JEANS, COFFEE, BOOKS – Hey, congratulations!

Some are confused because their words are in a foreign language. They’ve got Sanskrit fingernails scratching hieroglyphic foreheads As they frustratedly pull Swahili out of their scalp

They are learning that most people are simply misspelled and psychiatrists are trying to decode this new human alphabet. [Most psychiatrists are made of the word EXPENSIVE]

Some walked away proud knowing that their skin is made from copies of War and Peace and Tolstoy is cramming marathons into their shells.

A few ladies had sonnets falling from their hair and pretty haiku inside their eyelids.

One man had an entire back of free verse poetry and his left leg rhymed with his right.

One man’s stomach was actually the recipe for cheap beer. A few discovered that they are comprised of all punch lines and they have begun searching for those made up of all jokes.

In God We Trust is a very popular kneecap.

Countless noses are incorrect definitions of the word pretty while one child’s earlobe was made up of phrases that convinced her she could be a ballerina:

You can do it, you can do anything.

Most babies are blurred words from their mothers’ forearms While others were sadly blank.

This lens holds the memories of past victories and sins’ words worked into our skins and deeper:

The microscope zooms to the top layer and reveals who you are dating

and what you really think of them.

It zooms deeper and displays how you really feel about your parents.

It zooms deeper and reminds you about the people you still haven’t forgiven.

Deeper and you remember how you felt about God before you went to

college.

Deeper and you can remember your first birthday.

And then it gets to your core, into the most sacred word you hold.

It is at this point that most people look away from the monitor, take a breath, And exhale relief when they look back and see that it is actually a very good word.

People soon cry the word fear,
sweat the word pleasure,
Yawn the word ready,
Whistle the word thinking.

When they stretch, their muscles read

MY GOD I’M OUT OF SHAPE

I watched an old man quietly and slowly inch his way
under the lens.
He disrobed, stood naked and still with his eyes
clenched.
The monitor repeated itself with every movement of the
lens;
Forgive me . . . forgive me . . . forgive me
And please God, let me in.

But I, myself am choosing to wait my turn until the interest and curiosity of the public dissipates. That is when I will sneak into the lab where the Microscope Light Enhancer 2000 is resting on glossy moon tiles, I will turn it on.

The monitor might flash a couple of times to warm up as I step under the lens It will begin to spill what I hope to be an important dictionary onto the screen.

While I am waiting patiently for my words to appear,
I will begin to write down my best guesses of what my
words will be:
An honest list of flaws, triumphs,
Lessons learned with ease,
embarrassing memories,
things I have never been and now want to be,
sins, new habits to begin, sacred friendships gone and
wasted,
love, Dad, my blood is no longer bad,
Mom’s humor in my veins
the result of generational broken chains . . .

Before I finish my list, I will turn everything off and leave. I will want to smash it all and leave a note that says nobody needs this machine

but I won’t,
I will leave it alone,
and go somewhere beautiful
and finish my list myself.
```

---

## IC-1692: Songs from an Island

- Title: Songs from an Island
- Author (byline): Ingeborg Bachmann
- Work: The Vintage Book of Contemporary World Poetry
- Publisher: Vintage
- Publication date as stated: June 1996
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 516
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ingeborg Bachmann
Book: The Vintage Book of Contemporary World Poetry
ISBN: 978-0679741152
Publisher: Vintage
Date(Month/Year): June 1996
```

### Introduction (context only: never use it for content warnings)

```text
Pliny the Younger’s accounts of the eruption of Mount Vesuvius in 79 AD, tell a grim but detailed tale of destruction. . . . “We saw the sea sucked away and apparently forced back by the earthquake: at any rate it receded from the shore so that quantities of sea creatures were left stranded on dry sand. On the landward side a fearful black cloud was rent by forked and quivering bursts of flame, and parted to reveal great tongues of fire, like flashes of lightning magnified in size. . . . We had scarcely sat down to rest when darkness fell, not the dark of a moonless or cloudy night, but as if the lamp had been put out in a closed room. You could hear the shrieks of women, the wailing of infants, and the shouting of men; some were calling their parents, others their children or their wives, trying to recognize them by their voices. People bewailed their own fate or that of their relatives, and there were some who prayed for death in their terror of dying.” Centuries later Ingeborg Bachmann commemorates the power of nature and predicts future turmoil in her tribute titled Songs from an Island.
```

### Performance text (classify this)

```text
Shadow fruit is falling from the walls, moonlight bathes the house in white, and the ash of extinct craters is borne in by the sea wind.

In the embrace of handsome youths
the coasts are sleeping.
Your flesh remembers mine,
it was already inclined to me,
when the ships
loosened themselves from shore and the cross
of our mortal burden
kept watch in the rigging.

Now the execution sites are empty, they search but cannot find us.

When you rise from the dead,
when I rise from the dead,
no stone will lie before the gate,
no boat will rest on the sea.

Tomorrow the casks will roll toward Sunday waves, we come on anointed

soles to the shore, wash
the grapes and stamp
the harvest into wine,
tomorrow, on the shore.

When you rise from the dead,
when I rise from the dead,
the hangman will hang at the gate,
the hammer will sink into the sea.

One day the feast must come!
Saint Anthony, you who have suffered,
Saint Leonard, you who have suffered,
Saint Vitus, you who have suffered.

Make way for our prayers, way for the worshippers,
room for music and joy!
We have learned simplicity,
we sing in the choir of cicadas,
we eat and drink,
the lean cats
rub against our table,
until evening mass begins
I hold your hand
with my eyes,
and a quiet, brave heart
sacrifices its wishes to you

Honey and nuts for the children,
teeming nets for the fishermen,
fertility for the gardens,
moon for the volcano, moon for the volcano!

Our sparks leapt over the borders,
above the night fireworks fanned their
tails, the procession
floats away on dark rafts and gives
time to the primeval world,
to the plodding lizards,
to the carnivorous plant,
to the feverish fish,
to the orgies of wind and the lust
of mountains where a pious
star loses its way, collides with their face
and dissolves into dust.

Stand firm, you foolish saints.
Tell the mainland the craters aren't resting!
Saint Roch, you who have suffered,
oh you who have suffered, Saint Francis.

When someone departs he must throw his hat,
filled with the mussels he spent the summer
gathering, in the sea
and sail off with his hair in the wind,
he must hurl the table,
set for his love, in the sea,
he must pour the wine,
left in his glass, into the sea,
he must give his bread to the fish
and mix a drop of his blood with the sea,
he must drive his knife deep into the waves
and sink his shoes,
heart, anchor and cross,
and sail off with his hair in the wind.
Then he will return.
When?
Do not ask.

There is fire under the earth, and the fire is pure.

There is fire under the earth and molten rock.

There is a torrent under the earth, it will stream into us.

There is a torrent under the earth. it will scorch our bones.

A great fire is coming, a torrent is coming over the earth. We shall be witnesses.
```

---

## IC-1693: Sonnets for an Old Century – Cutting 1

- Title: Sonnets for an Old Century – Cutting 1
- Author (byline): Jose Rivera
- Work: Talk to Me: Monologue Plays
- Publisher: Vintage Books
- Publication date as stated: Dec 2004
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1147
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jose Rivera
Book: Talk to Me: Monologue Plays
ISBN: 978-1400076154
Publisher: Vintage Books
Date (Month/Year): Dec 2004
```

### Introduction (context only: never use it for content warnings)

```text
In a waiting room for the afterlife, we find a dreamscape filled with poignant and haunting monologues from recently deceased individuals. “Where do we go when we die?” And if you were to offer commentary regarding the life that you’ve lived, “What would you say?”

In this selection we hear from a woman and her husband, both with very different views about her life choices. Sonnets for an Old Century by Jose Rivera
```

### Performance text (classify this)

```text
WENDY JOHNSON (pg 121)

You stand here and make your statement.

That's it.

You want to fight with existence? Go for it. You want to scream? Knock yourself out.

Just remember: your words go out to the universe, all your words, to be, I don't know, recycled among the living -- like rain, like part of -- some ecology of the spirit.

It's the last and only time you have to give your side of the story, as far as I know.

ANA ORTIZ (pg 150)

There's somebody ... I don't know who he is ... I want to take this time to apologize to him. I don't know your name. I don't know what you look like.

You were in the Bronx about seven years ago. Let's see, it was outside the 180th Street shop on the Two, close to one in the morning. I don't remember the name of the street anymore.

But right there, under the elevated tracks, at the intersection, on the left as you go east, one night seven years ago ... I saw you. It was very dark there. All I wanted to do was to get home. So I'm walking fast 'cause I hate that street and I almost didn't see you. But I did see you.

Two men were holding you by the arms and they were slamming you headfirst into the front of a parked car. I couldn't see your face. The two guys were laughing. You fell to the ground. I only watched for a second.

I got out of there as fast as I could. I went home. I didn't call the cops. I didn't call for help. I didn't jump in to break it up. I didn't go back later to see if you were okay. I didn't do nothing but run. Protect my ass.

For a second I actually convinced myself that you guys were playing some kind of game, maybe you were just kids.

I'm sorry. If you're out here. If you're
hearing this. I was the one who walked
away that night and left you there and I
haven't been able to stop thinking about
you in seven years and I thought, here,
now, this would be the time to say I was
sorry. This would be the time.

Please forgive me, sir. Please forgive me.

TRANSITION But apologies mean little, and definitely won’t change the fate of your soul, unless the apology leads to a change. Listen as the speaker’s husband describes the woman he married. Time has definitely made a difference, but in her attempts to redeem herself, did she simply go too far?

ROBERT MONTANO (pg 145)

My wife ...

... she gave her old clothes to a local church
... she knew the mailman's birthday ...
she gave to UNICEF ...
she sent passionate faxes to elected officials ...
she knew the first
twelve Shakespeare sonnets by heart ...
she said good-bye to tollbooth people ...
"bye-bye tollbooth person!" ...
she returned her library books on time ...
she visited her eternal grandmother
every faithful summer ...
the old woman's one remaining pleasure ...
incontinent, toothless, unhappy ...
connecting her granddaughter,
through endlessly repeated anecdotes,
to the history written in her blood ...

. . . she swore she'd buy herself a gun
and shoot herself in the head
before she'd put up with an old age like this ...
we planned to get ancient together
and. do. the joint-suicide thing ...

... but there was a guy ...

... a guy who washes car windows
in front of the bank in our neighborhood ...
young guy ...
filthy ...
heroin ...
always had a skateboard ...
she'd drive up to the bank ...
give him a dollar to clean the windshields ...

. . . they'd hang out and talk ...
they did this every Saturday morning ...
he's very good-looking ...
despite the filth ...

... she used to shoot up, so she understood ...

I thought they were in love ...
they had "a thing" ...
I waited in the car as they laughed ...
she once gave him a twenty,
got in the car, crying ...
she said, "I just heard the saddest story" ...

... his new tattoo ...
I swore it was her name
surrounded by a crown of thorns ....
the woman he couldn't have ...
I wanted to kill this man . . .
he was pathetic ...
smelled like a urinal ...
she got too close to him ...
I didn't want his clothes to brush her
clothes ... came home one day ...
there he is in the kitchen ...
merrily drinking coffee ...
he's talking to her about movies ...
big fan of Hitchcock ...

what the **** is going on here? ...
I wanted to unwind ...
I'm stuck with this putrid drug user
in my kitchen
pontificating about Strangers on a Train! ...

... we fought about it that night ...
I told her: "I come home ...
I can't even talk to you
because this addict is monopolizing you ...
all I want is equal rights here!" ...
she said,
"I already know what you're going to tell
me" ...
I stare at her ...
"I bore you? ...
is that it?" ...
"no," she said quickly ...
I didn't even stay in bed to hear more ...
she said, "these people need me" ...
"I don't need you?" ...

she said, "not in the same way" ...
"honey, I need you in profound ways" ...
she said, "yes I know" ...
"you're not going to save this man" ...

... I couldn't stop imagining them together ...
... I imagined they rode skateboards
together... panhandling in front of our
house ..
all our friends staring at her ...
and she'd look and sound happier
with him than she ever looked and sounded
with me ...
beneath the layers of traffic soot
and sidewalk dirt
her eyes were full of wisdom and fulfillment
and absolute freedom ...
the freedom only vaguely imagined
by the housebound ...
freedom to say "**** you" ...
to stare at the drivers
waiting for the light to change ...
she'd challenge them:
"hey you in the Lexus, are you moral?
empathic? ...
you think you are ...
you tell your children you are ...
in your prayers you boast that you are ...
yet here I am ...
LOOK AT ME ...
I'm staring into the deepest tunnels
of your heart
and I'm not seeing **** ...
you want me gone ...
you hope I fall off the edge
of the known world ...
fall painlessly into oblivion
while you drive to your appointments" ...

... she wanted that power ... and that power was something she could only get from him ...

... then he disappeared ...

... after that we would drive together ...
anywhere ...
didn't matter ...
there they were ...
like an army of vampires,
bloodless, in their rags and filth ...
they knew about her ...
they sought her out ...
she radiated goodness and they wanted it ...
they wanted to drink from her kindness
like it was an ancient tribal river ...
to suck her down into their limbs ...
to own her ...

... my wife .. . actually began to disappear in front of my eyes ... I watched helpless as she gave away scraps of herself ... first the excess ...

then the vital tissues ... until she disappeared completely from my sight ... down into the tortured piranha pit of the homeless ...

... away from me ...
happy ...
alive ...
and finally at home.
```

---

## IC-1694: Sonnets for an Old Century – Cutting 2

- Title: Sonnets for an Old Century – Cutting 2
- Author (byline): Jose Rivera
- Work: Talk to Me: Monologue Plays
- Publisher: Vintage Books
- Publication date as stated: Dec 2004
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1507
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jose Rivera
Book: Talk to Me: Monologue Plays
ISBN: 978-1400076154
Publisher: Vintage Books
Date (Month/Year): Dec 2004
```

### Introduction (context only: never use it for content warnings)

```text
In a waiting room for the afterlife, we find a dreamscape filled with poignant and haunting monologues from recently deceased individuals. “Where do we go when we die?” And if you were to offer commentary regarding the life that you’ve lived, “What would you say?”

Sonnets for an Old Century by Jose Rivera
```

### Performance text (classify this)

```text
WENDY JOHNSON (pg 121)

You stand here and make your statement.

That's it.

You want to fight with existence? Go for it. You want to scream? Knock yourself out.

Just remember: your words go out to the universe, all your words, to be, I don't know, recycled among the living -- like rain, like part of -- some ecology of the spirit.

It's the last and only time you have to give your side of the story, as far as I know.

ALENE DAWSON (pg 187)
My son had his first day of public school Monday.
We had him in a private school in Van Nuys
but it was a little too far away for us,
too expensive, and he'd come home all sad,
saying, “How come there are no
brown faces in my school, Mom?"
So we finally got him into a magnet in Echo Park
-- prestigious --
and there was an assembly Monday
and on the stage the principal got up
to talk to the new students and said,
"Okay kids, now don't you be bringing in
no guns to school in your backpacks!

Hear that, children?
I want no guns, no knives,
no chains in your lockers
or in your backpacks
or on your person.”
This is the principal!
This is a magnet school in the humanities!
And she says,
"Stay close to the school,
don't wander away from campus.
There have been drive-bys in this area
so don't leave the school grounds!"
I'm thinking, oh my God!
It's getting out of control.
We're at war.

Citizens killing citizens.

We don't need the government to bomb the city.
We do it to ourselves,
taking the knife to cut open the throats
of our own children,
and then when we're out of hand,
when we're too good at that,
the police are brought in,
like an occupying army, you know,
jackboots all polished up,
hardware all glistening,
big robocop shoulders,
nightsticks ripping open the heads
of our little boys, it makes me crazy.
'Cause you know, it's all their fault!
The economy bad?
It's the black kids!
Air pollution?
The black kids did it!
The dollar down against the yen?
You know who to blame! God!
Made me want to take a rock
and hurl it at some politician,
some bozo running for Mayor,
any of those quicktongued hypocrites
assigned to protect the citizens,
'cause, no, I didn't feel protected,
I felt exposed, all opened up,
like some criminal was pointing
his Saturday Night Special at me
and every day I sensed those trigger fingers
out there and I was at the end
of their sights and they were just watching me,
waiting for the right split second
to send a little ounce of screaming steel
into the back of my brain!
God! God! It was not to be believed!
Being a woman in this city, sometimes,
oh my God,
I needed some help!
Especially when my boy went
out that door, you know?
And my imagination has created his killer,
some sweating overanxious rookie cop,
too afraid to piss straight,
slamming into my child at the wrong time,
in the wrong place, 'cause he's thinking,
"Of course, boy's in a gang, it's natural,
they run in packs,
those boys up to no good, you bet.
But what'd you expect?
It's a genetic thing with the black kids,
they're innately less intelligent,
but don't talk to me,
it's already proven,
there are statistics,
it's testable,
they're naturally more comfortable
with a .45 in their hands
than a volume of Faulkner."
So why the hell not cut the school budget?
Why not send them off
to some genocidal death in the penitentiary?
It's a waste of good American tax money
trying to educate these
unteachable black kids!
Jesus Christ! It's time to build
another super-prison,
you know, with a hundred nautilus machines
and hot tubs and libraries,
'cause, let's face it,
it's a whole lot nicer on the inside
than the corner of Florence and Normandie.
Going to jail is a good career move!
Oh God! If I wasn't a peaceful woman
I would've thrown rocks!

Trouble is, I don't think enough people
believe in the multiplicity of God.
Not enough people understand
God's great face has a nose
and eyes of a thousand shapes and sizes
and all of us, down to the last ugliest
and lowest person, we are all the living,
walking text of God.
Yes, the life story of God is
written into each one of us:
we are the pages in the book of God's mind.
And if we'd just take the time
we'd be able to read God
in each other's faces,
read the funny lines as well as the lines
of wisdom and healing --
because the Word of God
isn't written in the Bible, no,
the Word of God is written in your mirror
and on your brother's black face
and in your son's blue eyes.

TRANSITION And that little boy . . . Alene Dawson’s son . . . an child immigrant from the poverty-stricken country of Nicaragua, found a better life in America. Yes, there was racism; yes, there were people who didn’t want another immigrant in the U.S. . . . and he reached his teen years without his mother . . . but it was better . . . until it wasn’t. This is his story in that great waiting room for the afterlife.

RICK COCA (Pg 129)
I was waiting outside the house
for almost an hour.
My novia (girlfriend) was working in this house.

Anglo family. Watching their children. They were supposed to get back by eleven thirty.

It was past midnight. We didn't think they'd want me in their house so I waited in the car on the street in front.

I drove a small and dented Toyota.
The neighborhood was rich.
Big houses, not too much happening at
night. Dead and dark.
Sometimes you see coyotes looking for food.
Or an opossum crawling across the road.

Animals fascinate me.
Where I grew up you lived with animals.
You understood their habits.
You paid attention to what they needed
or they would die.
If they die, you die.

I watched them being born! I got used to blood and birth.

My mother taught me to kill chickens
with my hands.
You grab them around the neck and then
you spin them around.
They struggle and some of them can really
cut you bad if you're not careful.
When I was a child I loved to kill them like that.

Later I butchered pigs.
I pretended the pig was a condemned man,
a murderer, rapist, with no soul,
who never repented,
and spit at the priest giving him Last Rites
and mocked the sacraments
and the family of the victim,
boasted he raped little girls.
I held the knife tight.
Looked at the struggling, confused pig.

Imagined the rapist or the unrepentant
murderer and I was chosen by the court to
execute this scum. I never smiled.
I never let the pig's --
I mean the prisoner's –
screams distract me.
I plunged the knife into its soft throat –
far as it could go --
and I cut and cut and the animal screamed
like a man and I imagined
the bleeding prisoner
finally understanding the meaning of his crimes,
repenting, fearing God,
believing in God's wisdom,
God's punishment, which I carried out.
I was the messenger of God,
the word of God, I said,
"Don't kill," "Don't rape," "Don't sin," . . .
I was the terrible messenger
and this knife was my message.
I took myself very seriously
when I was ten years old.

To this day, animals fail to move me with their dying, their breeding -- so what? The coyotes hurrying through these bigshot Anglo neighborhoods at night, ignoring me in my Toyota as I wait for my girlfriend -- so what?

I waited out there nearly an hour.
I was low in my seat,
thinking of my youth in Nicaragua
among animals.
It was dark and quiet.
I was about to fall asleep.
Far away I heard a car.
It wasn't going fast.
I thought "No."
I didn't move.
I could feel the sweat in my hands.
I thought "No!'
I waited and decided to sit up.
The police lights shot on,
red and blue swirls colliding in my face,
my stomach turning into boiling water,
my mouth dry.
Two men got out.
One of them shined a flashlight in my face.
I waited.
The other cop stood behind the first
and he waited.
Man's eyes were cold.
Man's eyes stared right into me.
I turned my head
and wouldn't look in his eyes
as the other one told me to get out of the
car very, very slow,
hand on his gun,
the night very still,
coyotes long gone,
scared away by the action, instinctual.

I stood there and explained what my business was on this street and one of the cops looked at me the way I used to look at the pigs I was about to slaughter, cold, convinced of my higher duty, the spokesman of God, the messenger, the punisher, the death-bringer.
```

---

## IC-1695: Soon

- Title: Soon
- Author (byline): James Harms
- Work: The New Young American Poets: An Anthology
- Publisher: Southern Illinois Univ Press
- Publication date as stated: March 2000
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 717
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Harms
Book: The New Young American Poets: An Anthology
ISBN: 978-0809323081
Publisher: Southern Illinois Univ Press
Date(Month/Year): March 2000
```

### Introduction (context only: never use it for content warnings)

```text
As mere mortals we are extremely uncomfortable with death. The thought of our own mortality terrifies us but perhaps the thought of our loved ones dying scares us even more. One of my favorite quotes about life an death is by Robert Fulghum: I believe that imagination is stronger than knowledge - myth is more potent than history - dreams are more powerful than facts - hope always triumphs over experience - laughter is the cure for grief - love is stronger than death. This poem by James Harms allows us insight into the thoughts of a husband who know his wife is soon to die. Soon by James Harms
```

### Performance text (classify this)

```text
He had always supposed he would die first, before her, though he didn't think about it much. It was like a secret learned and then forgotten, a letter that hurts and is hidden away in a trunk. But he had always assumed that one of many gifts she would give him would be to bury him, and that was that, though now and then, as he cleaned her hair from a drain or sliced an apple into wedges for lunch, placing half on a yellow plate for her, eating the rest as he stood reading her shopping list taped to the refrigerator, now and then he thought of how much harder it is to be left behind, and for a while he'd feel an ache in his hands, as if he were trying to hold onto something too tightly. Twenty-five years ago she was already twenty years younger than he, sitting outside his office, her name on a sheet of paper tacked to the door, her name with others, each listed by the hour: it was always 3 o'clock with her, always Wednesdays. And he loved her immediately, though of course, he hadn't known it right away. Perhaps one day, as she pulled her books from a bag and began to ask a question, pointing at a line in a poem, perhaps he thought of how much harder it would be for her, perhaps he thought this before he'd ever kissed her, before he noticed how her glance left a streak on his cheek for days, as if her thoughts could touch, could leave the small bruises love leaves early on. But even then there was nothing he could do about it. Once, years after, he awoke from a dream where he had watched her from a stand of black oaks as she dropped a daisy in his grave. And later, still dreaming, he had circled in the air above their bed as she tossed loosely in the sheets without him like an empty cup blown with paper down the street; she had been wearing a shirt he'd left dirty in the hamper. She wrapped her arms around his pillow as though it were a sack of stones, as though it held her in place on the earth, kept her from rising to join him. And when he drifted on her breath out the open window he had reached to grab the curtains; he had wanted to stay with her, though he was nothing then, a breeze, his hands passing through the thin fabric like smoke through a screen. And for the rest of the dream he wandered through their town disrupting leaves gathered in the gutters, cooling a hot cheek here and there: a breeze. He never told her of his dream. Sometimes he watched her from the porch as she stooped and straightened in the small side garden. He watched her pull the carrots from the earth, how she shook them gently before dropping them in the basket. She wore around her neck a small woven sack on a string, and in it kept a quarter: if ever far from home and stranded she could call. But she was never far from home. And the sack lifted away from her breast as she bent to pull a weed; it swung back and forth like a hypnotist's watch; she took it off only to sleep. And when he awoke before her each morning he thought of her alone in the empty house tending to the three cats, winding the clocks, the few things he now did, stacking logs on the front porch each October, phoning for oil when the furnace went cold, filling the feeder by the kitchen door. And of course it hurt him to imagine her alone, as it hurts him now to imagine what becomes of those who go, or worse, of those who stay behind as wind, as small eddies of air. He gathers the laundry in piles, wonders where she kept the bleach. He lifts the sash, lets in a soft wind hoping for the smell of lilacs, though it's early yet, only April. He will have to wait for lilacs, and for whatever she planted in the garden. It is too soon to know for sure what is there.
```

---

## IC-1696: Speaking Truth – A Collection

- Title: Speaking Truth – A Collection
- Author (byline): Shel Silverstein, Barbara K. Bassett and Maya Angelou
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1275
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shel Silverstein
Book: Falling Up
ISBN: 978-0060248024
Publisher: HarperCollins
Date (Month/Year): Jan 2006
Author: Barbara K Bassett
Book: Chicken Soup for the Woman's Soul: Stories to
Open the Heart and Rekindle the Spirit of Women
ISBN: 978-1623610432
Publisher: Backlist, LLC
Date (Month/Year): Aug 2012
Author: Maya Angelou
ISBN: 978-0679748380
Publisher: Random House
Date (Month/Year): Feb 1993
```

### Introduction (context only: never use it for content warnings)

```text
Henry David Thoreau once said, “We are constantly invited to be who we are.” So why it is so difficult to find our voices, to speak our truth? Fear – we fear rejection, we fear judgment, we fear becoming assertive and powerful.

But perhaps Audre Lorde said it best: “The speaking will get easier and easier. . . And at last you’ll know with surpassing certainty that only one thing is more frightening than speaking your truth. And that is not speaking.”

Transformation - A Collection of Three Poems: The Voice by Shel Silverstein; Angela’s Word by Barbara K. Bassett and On the Pulse of Morning by Maya Angelou
```

### Performance text (classify this)

```text
The Voice by Shel Silverstein

There is a voice inside of you
that whispers all day long,
'I feel that this is right for me,
I know that this is wrong.'
No teacher, preacher, parent, friend
or wise man can decide
what's right for you - just listen to
the voice that speaks inside.

Angela’s Word by Barbara K. Bassett

When Angela was very young, age two or three or so, her father and her mother taught her never to say “NO”. They taught her that she must agree with everything they said, and if she didn’t, she was spanked and sent upstairs to bed.

So Angela grew up to be a most agreeable child; she was never angry and she was never wild; she always shared, she always cared, she never picked a fight, and not matter what her parents said, she thought that they were right.

Angela the angel did very well in school. And, as you might imagine, she followed every rule; her teachers said she was well-bred, so quiet and so good, but how Angela felt inside they never understood.

Angela had lots of friends who liked her for her smile; they knew she was the kind of gal who’d go the extra mile; and even when she had a cold and really needed rest, when someone asked her if she’d help, she always answered “yes.”

When Angela was thirty-three, she was a lawyer’s wife. She had a home and family, a nice suburban life. She had a girl of four and a little boy of nine, and if someone asked her how she felt, she always answered, “Fine.”

But one cold night near Christmastime when her family was in bed, she lay awake as awful thoughts went spinning through her head; she didn’t know why, and she didn’t know how, but she wanted her life to end; so she begged Whoever put her here to take her back again.

And then she heard from deep inside, a voice that was soft and low; it only said a single word and the word it said was . . . NO.”

From that moment on, Angela knew exactly what she had to do. Her life depended on that word, so this is what her loved ones heard:

“NO, I just don’t want to; NO, I don’t agree; NO, that’s yours to handle; NO, that’s wrong for me; NO, I wanted something else; NO, that hurt a lot! NO, I’m tired, and NO, I’m busy, and NO, I’d rather not!”

Well, her family found it shocking, her friends reacted with surprise; but Angela was different, you could see it in her eyes; for they’ve held no meek submission since that night three years ago when Angela the angel got permission to say NO.

Today Angela’s a person first, then a mother and a wife. She knows where she begins and ends, she has a separate life. She has talents and ambitions, she has feelings, needs, and goals. She has money in the bank and an opinion at the polls.

And to her boy and girl she says, “It’s nice when we agree; but if you can’t say ‘NO’, you’ll never grow to be all you’re meant to be. Because I know I’m sometimes wrong and because I love you so, you’ll always be my angels even when you tell me ‘NO.’

TRANSITION

And so as individuals we find our voices; but we too must listen. Listen to the truth of those around us. Listen to the still quiet words of nature. Maya Angelou provides hope and gives voice to the quiet truth of . . . . (Start first line of the following poem here)

On the Pulse of Morning by Maya Angelou

A Rock, A River, A Tree
Hosts to species long since departed,
Marked the mastodon,
The dinosaur, who left dried tokens
Of their sojourn here
On our planet floor,
Any broad alarm of their hastening doom
Is lost in the gloom of dust and ages.

But today, the Rock cries out to us, clearly, forcefully,
Come, you may stand upon my
Back and face your distant destiny,
But seek no haven in my shadow.
I will give you no hiding place down here.

You, created only a little lower than
The angels, have crouched too long in
The bruising darkness
Have lain too long
Face down in ignorance.
Your mouths spilling words

Armed for slaughter. The Rock cries out to us today, you may stand upon me, But do not hide your face.

Across the wall of the world, A River sings a beautiful song. It says, Come, rest here by my side.

Each of you, a bordered country,
Delicate and strangely made proud,
Yet thrusting perpetually under siege.
Your armed struggles for profit
Have left collars of waste upon
My shore, currents of debris upon my breast.
Yet today I call you to my riverside,
If you will study war no more. Come,
Clad in peace, and I will sing the songs
The Creator gave to me when I and the
Tree and the rock were one.
Before cynicism was a bloody sear across your
Brow and when you yet knew you still
Knew nothing.
The River sang and sings on.

There is a true yearning to respond to
The singing River and the wise Rock.
So say the Asian, the Hispanic, the Jew
The African, the Native American, the Sioux,
The Catholic, the Muslim, the French, the Greek
The Irish, the Rabbi, the Priest, the Sheik,
The Gay, the Straight, the Preacher,
The privileged, the homeless, the Teacher.
They hear. They all hear
The speaking of the Tree.

They hear the first and last of every Tree
Speak to humankind today. Come to me, here beside the
River.
Plant yourself beside the River.

Each of you, descendant of some passed
On traveller, has been paid for.
You, who gave me my first name, you,
Pawnee, Apache, Seneca, you
Cherokee Nation, who rested with me, then
Forced on bloody feet,
Left me to the employment of
Other seekers—desperate for gain,
Starving for gold.
You, the Turk, the Arab, the Swede, the German, the
Eskimo, the Scot,
You the Ashanti, the Yoruba, the Kru, bought,
Sold, stolen, arriving on the nightmare
Praying for a dream.

Here, root yourselves beside me.
I am that Tree planted by the River,
Which will not be moved.
I, the Rock, I the River, I the Tree
I am yours—your passages have been paid.
Lift up your faces, you have a piercing need
For this bright morning dawning for you.
History, despite its wrenching pain
Cannot be unlived, but if faced
With courage, need not be lived again.

Lift up your eyes upon
This day breaking for you.
Give birth again
To the dream.

Women, children, men,
Take it into the palms of your hands,
Mold it into the shape of your most
Private need. Sculpt it into
The image of your most public self.
Lift up your hearts
Each new hour holds new chances
For a new beginning.
Do not be wedded forever
To fear, yoked eternally
To brutishness.

The horizon leans forward,
Offering you space to place new steps of change.
Here, on the pulse of this fine day
You may have the courage
To look up and out and upon me, the
Rock, the River, the Tree, your country.
No less to Midas than the mendicant.
No less to you now than the mastodon then.

Here, on the pulse of this new day
You may have the grace to look up and out
And into your sister’s eyes, and into
Your brother’s face, your country
And say simply
Very simply
With hope—
Good morning.
```

---

## IC-1697: “Stand Back” said the Elephant, “I’m Going to Sneeze!”

- Title: “Stand Back” said the Elephant, “I’m Going to Sneeze!”
- Author (byline): Patricia Thomas
- Work: Not specified
- Publisher: HarperCollins
- Publication date as stated: April 1990
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 989
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patricia Thomas
ISBN: 978-0688093389
Publisher: HarperCollins
Date (Month/Year): April 1990
```

### Introduction (context only: never use it for content warnings)

```text
All the animals are in a panic. The elephant's sneeze would blow the monkeys out of the trees, the feathers off the birds, the stripes off the zebra. Even the fish and the fly, the crocodile and the kangaroo, know what a catastrophe that sneeze would be. "Please don't sneeze!" they beg. . . . Knowing the havoc it will cause, all the animals try to prevent the elephant from sneezing. “Stand back,” said the elephant, “I’m going to sneeze!” By Patricia Thomas
```

### Performance text (classify this)

```text
“Stand back,” said the elephant,
“I’m going to sneeze!
I hate to alarm you,
But I don’t wish to harm you.
My friends, I fear
It’s clear . . .
Oh, dear,
You’d better stand back, I’m going to sneeze.”

“Oh no, oh no!”

Cried the buffalo.
“You’re so big and strong
And your trunk is so long,
Your sneezes send everyone flying along,
Bumping and thumping down a pathway and trail,
Bouncing and jouncing head over tail,
Tumbling and bumbling . . .
Your sneeze is a gale . . . .
Or a hurricane!
I hate to complain.
But please,
Don’t sneeze!”

“No, no, please,
Don’t sneeze,”
Cried the monkeys in the trees.
“You make such a breeze
When you sneeze.
The last time you blue us right out of the trees.
The branches began to bend and to sway
And some of us landed so far way
We didn’t get back until the next day.

The leaves all went whirling
And tumbling and swirling,
And the flowers
Shook for hours
The last time you sneezed.
Even a cough
Would knock some of us off.
Oh, please,
Don’t sneeze!”

With a shriek
The parrot opened his beak.
“The elephant says he’s going to sneeze!”
“Oh, Elephant, please!” cried the birds in the trees.
“The last time you sneezed we lost every feather.
We didn’t know whether
We’d ever get back together.
Every parakeet
Was bare as a sheet
From his head to his feet.
What’s more, all the whales
Had peacock’s tails,
And the wings of the cockatoo
Were stuck on the kangaroo.
You must confess
It was quite a mess,,
Very confusing
And not too amusing.
Even a snuffle
Makes our feather ruffle.
Oh, please,
Don’t sneeze!”

“Fly, fly,” called the birds to the bees. “The elephant says he’s going to sneeze.”

“Oh, no,” buzzed the bees.
“Not a sneeze! Not a sneeze!
The last time he blew off our stings
And our wings
And we had to make do
With rose thorns and glue.
Furthermore . . . what a shock
We all had to walk . . .

On our knees,
If you please,
(And that’s hard on bee’s knees)
While our wings grew back in.
What a sin!
Oh, please,
Don’t sneeze!”’

“Beware, beware,” Called the bees to the bear. “The elephant says he’s going to sneeze.”

“Oh, please,
Not a sneeze,”
Said the bear,
“That’s not fair.
I declare,
The last time he sneezed he blew off all my hair,
And left me so bare
I spent the whole winter in long underwear –
Nothings so sad as a bear that is bare.
The poor giraffe
(Don’t laugh)
Almost bent in half,
And the alligator’s snout
Was turned inside out
The last time he sneezed.
A sniff or a snuff
Is bad enough . . .
But a sneeze!
Oh, please,
Don’t sneeze!”

I’ don’t suppose
You could hold your nose,
Or wait awhile?”
Asked the crocodile
With a sad little smile.

“Oh my, Do try,” Said the fly.

“We wish,”
Said the fish,
“You would
If you could.
The last time you blew off all the scales
From our heads to our tails,
And our gills
Got the chills
Our skin
Is so thin.
If you do it again
We’ll freeze!
Oh, please,
Don ‘t sneeze!”

Then zebra yelled, “Yipes,
You’ll blow off my stripes,
Plus lots and lots
Of the leopard’s spots,
And all of the snakes will be tied up in knots!”

The hippopotamus
Said, “A lot of us
Will fall right on our bottom-us
If you sneeze.
So please,
Don’t sneeze.”

“I’m sorry, my friends,” said the elephant sadly,
“About all of this I do feel badly.
If I could keep from sneezing I’d do it gladly.
But I have such a twitch
In my trunk, and an itch,
Plus a bit of a tickle,
And even a prickle.
You must run fly, and hop.
I’m afraid I can’t stop.
I would
If I could,
But there’s nothing to do . . . .
Ah . . .
Ah . . . “

“BOO!”

Shouted a little gray mouse
Jumping out of his house.
He stood right up on his little tiptoes,
Stuck out his tongue, and wiggled his nose.

“Eek!” shouted the elephant, jumping up in the air,
“That’s a mouse! That’s a mouse standing there!
I must hid in a tree
Before he gets me
Or jump in the lake
For goodness sake!
Don’t scare me!
Please spare me!”

The mouse laughed, “Oh, pooh!
Now what could id do?
A little thing like me to a big thing like you?
I only wanted to give you a scare,
And it worked as sure as you’re standing there.
Elephant, think about it, please!
You completely forgot to sneeze!”

“Well, what do you know?”
Laughed the elephant. “That’s so!
It’s astounding,
Confounding.
As I live and breathe!
I don’t think I really have to sneeze.”
He began to giggle, “He, he, he, he!
That’s the funniest thing that has happened to me!
Ha, ha, ha! Ho, ho, ho!”
The elephant shook from his head to his toe.
He ho-hoed, and ha-haed.
He giggled and guffawed.
He chortled and chuckled
Until his knees buckled.

He sat down and rolled from side to side. In fact, the elephant laughed till he cried. He laughed till the ground was shivering and shaking And all of the trees were quivering and quaking. The monkeys came tumbling out of the threes, And the strings fell off every one of the bees. The bird’s feathers went flying To goodness-knows-where, All of the hair Fell off of the bear.

The giraffe
Bent in half,
And the alligator’s snout
Turned inside out.
The fish lost their scales
From their heads to their tails.

The zebra yelled, “Yipes!
There go my stripes!”
While the hippo went thump
Right on his plump . . . . you-know what!

And into a puddle
The mouse went . . . ker-plop!
Then he sat up and shouted,
“This simply must stop!
We’re terribly glad you don’t have to sneeze
But if you must laugh, laugh softly.

Oh, Elephant, please!”
```

---

## IC-1698: A Standardized Education?

- Title: A Standardized Education?
- Author (byline): Olivia Fantini and Suli Breaks
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1628
- Already set (do not supply): none

### Source block (context only)

```text
Author: Olivia Fantini
ISBN: On-Line Transcript Only
Publisher: Poem Transcripts, Word Press
Date (Month/Year): March 20, 2016
Web link:
https://poemtranscripts.wordpress.com/2016/03/20/on-
standardized-testing-olivia-fantini/
Author: Suli Breaks
ISBN: On-Line Transcript
Published as Audio Spoken Word Poetry
Audio Album: Dorm Room: An Audio Story, Track 10
Publisher: Amazon Music
Date (Month/Year): July 14, 2013
Web Link: https://genius.com/Suli-breaks-i-will-not-let-
an-exam-result-decide-my-fate-annotated
```

### Introduction (context only: never use it for content warnings)

```text
“What you know matters far less than what you can do with what you know,” says Harvard education specialist Tony Wagner. You see, knowledge is available on every Internet-connected device and instant answers can be found on Google. Tests that focus on content knowledge - the tests most often and easily standardized - disengage and, ultimately, disadvantage students. Keep in mind, we’re talking about the average, the standard, student. Throw in those speaking English as a second language and the disconnect makes even less sense.

On Standardized Testing by Olivia Fantini
```

### Performance text (classify this)

```text
On Standardized Testing by Olivia Fantini

Good morning boys and girls.

Welcome to the sixth grade National Assessment of Educational Progress.

Technological devices, which provide an unfair advantage, are not permitted.

If you are in possession of such a device, including but not limited to, cell phones, iPods, tablets, calculators, white privilege, parents with a college education, or a household annual income above the poverty line, please power it down now and raise your hand.

The proctor will return your device at the end of the testing period.

One: If Peter reads at a rate of two hundred words per minute in the fourth grade of a local private school, and his reading level is growing exponentially, how long will it take Peter to read all seven of the Harry Potter books?

I ask the ESL specialist what resources are available for my students who have just immigrated to the U.S. She sends me a link to an online language program none of my students can afford.

Two: If Monica reads twenty words per minute in English and thirty words per minute in Spanish, in the sixth grade of the best public middle school in Providence, how long will it take her to read to read the five-hundred-word article on “The Failings of Public Education?”

I ask the ESL specialist what resources are available for a student who spent fourth and fifth grade in a refugee camp. She tells me her boss will reach out to the family.

He never does.

Three: Students who are not proficient readers by the end of third grade are four times less likely to graduate from high school by age nineteen.

At poverty, these students become thirteen times less likely to graduate on time.

Multiply by one out of ten high school dropouts spends time in prison, divide by racism, take the square root of reality, subtract irrational numbers and unreal dreams, where will Monica be in five years?

Please put down your pencils and close your testing booklets. Wait silently while the white teacher, who grew up in a wealthy suburb and has never taken a standardized test, collects your materials.

Feels like a cog in the bowels of the things she despises, begins another letter to the ESL specialist who has stopped responding . . . Gives up and addresses it to herself:

Dear Olivia,

Do not think you know their struggle because you drive into their neighborhood every morning at seven and back to the east side at four.

Do not think you see through the window what they see; you are not looking through the same window. You will never be looking through the same window. It is impossible to shed a heritage of privilege. Examine your reflection in the window.

Do not try to give your students a voice by lending your own.

Your job is not to tell their story, but to be a microphone held to their lips; a stepping stool; a cheerleader.

Olivia, do not stop teaching. Do not move to a school in the suburbs. Do not switch to private education. Do not write an end to this poem, Olivia.

This isn’t over.

TRANSITION

In 2011, Google, rated one of the best US companies to work for by Forbes magazine, released the results of a study called Project Oxygen. The study found that from an employer standpoint “… G.P.A.’s and test scores are worthless as a criteria for hiring,”

But don’t the standards of the classroom prepare students for the standards of the real world? Unfortunately, in many cases the answer is NO. Today’s job landscape is changing so fast, it is imperative for young professionals to be able to solve problems creatively and think critically. The capacity to innovate is far more important than academic knowledge. Are we too busy forcing students to color in the correct bubble on a standardized test to prepare them for the real world? We should be teaching HOW to think, not WHAT to think, because . . . You see, knowledge is available on every Internet-connected device and instant answers can be found on Google.

I Will Not Let an Exam Result Decide My Fate by Suli Breaks

I Will Not Let an Exam Result Decide My Fate by Suli Breaks

Right now There is a kid finishing Parents' Evening in a heated

discussion with his mother Saying, why does he have to study subjects he will never

ever use in his life? And she will look at him blank-eyed, stifle a sigh, think for a

second and then lie She'll say something along the lines of: "You know to get a good job, you need a good degree and these subjects will help you get a degree, we never had this opportunity when I was younger" And he will reply: "But you were young a long time ago, weren't you mum?" And she won't respond although what he implies makes

perfect sense that society's needs would have changed

since he was 16 But she will ignore him, grip his hand more sternly and drag

him to the car What she doesn't know is that she didn't ignore him just to

shut him up She didn't lie because they are just returning him from

Parents' Evening And an argument in the hallway would look bad on her

resume She won't lie because she had just spent the last one hour

convincing a stern face teacher that she would ensure

that her child studies more at home No! She will lie simply, because she does not know any

better herself Although all her adult life, she has never used or applied

Pythagorean theorem, Pathetic fallacy, and still does not

know the value of "X" She will rely on society to tell her that her child, who has

one of the sharpest minds in the school, is hyperactive,

unfocused, easily distracted and wayward

Students! How many equations, subjects and dates did you memorize

just before an exam never to use again? How many "A" grades did you get, which were never asked

for when applying for a job? How many times have you remembered something 5

minutes just after the teacher said: "Stop writing" Only to receive your results a month later to realize that

you were only 1 mark short of the top grade? Does that mean remembering 5 minutes earlier would've

made you more qualified for a particular job? Well, on an application form it would have We all have different abilities, thought processes,

experiences and genes So why is a class full of individuals tested by the same

means?

So that means Cherrelle thinks she's dumb, because she

couldn't do a couple sums And if this issue is not addressed properly, it then becomes

a self-fulfilling prophecy Then every school has the audacity to have policy on

equality Huh, the irony!

Exams are society's methods of telling you what you're

worth But you can't let society tell you what you are Cause this is the same society that tells you that abortion is

wrong, but then looks down on teenage parents! The same society that sells products to promote natural

hair, looks and smooth complexion with the model on

the box, half photoshopped, and has fake lashes and hair

extensions
With pastors that preach charity, but own private jets
Imams that preach against greed, but are all fat
Parents that say they want "educated kids" but constantly

marvel at how rich Richard Branson is Governments, that preach peace, but endorse war, that say

they believe so much in the importance of higher

education and further learning Then why increase tuition fees every single year? I believed Miss Jefferson when she took me into the office, said that my exams would be imperative to my success Because we were taught to always follow when Miss

Jefferson led Then I took Jefferson out of the equation and learned to

think for myself I realized, we were always taught to follow when misled Huh, the irony!

Test us with tests, but the finals are never final Because they never prepare us for the biggest test which is

survival!
And what I suggest is fairly outlandish
So I don't expect everyone to understand this
Except for the kid that knows what it feels like to be worth

no more than that D or that A that you get on results day And the ones whose best stories were never good enough

for your English teacher Because apparently you missed out on key literary

techniques
Did not follow the class plan,
And the language was too "informal" for him to understand
But then he'd reference Hamlet and Macbeth
And you'd fight the urge to express your contempt by

partially clenching your fist with only your medium finger

left protruding in the middle of your hand And asking if he was aware that Shakespeare was known as

the innovator of slang Or the kid at the back of the class who thinks: "Why am I studying something that doesn't fuel my drive?" But when confronted with a math problem his eyes come alive

So this one is for my generation, the ones who found what they were looking for on Google, the ones who followed their dreams on Twitter, Pictured their future on Instagram, accepted destiny on Facebook. This one's for my "failures" and "dropouts", for my

unemployed graduates, my shop assistants, cleaners and

cashiers with bigger dreams, My self-employed entrepreneurs, my world-changers and

my dream-chasers! Cause the purpose of "Why I hate school, but love

education" was not to initiate a worldwide debate, But to let them know that whether 72 or 88, 44 or 68, We will not let exam results decide our fate.
```

---

## IC-1699: Stepanek Poetry Collection

- Title: Stepanek Poetry Collection
- Author (byline): Matthew Joseph Thaddeus Stephanek
- Work: Hope Through Heartsongs
- Publisher: Hyperion Books
- Publication date as stated: January 2002
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 823
- Already set (do not supply): none

### Source block (context only)

```text
Author: Matthew Joseph Thaddeus Stepanek
Book: Hope Through Heartsongs
ISBN: 978-0786869442
Publisher: Hyperion Books
Date (Month/Year): January 2002
```

### Introduction (context only: never use it for content warnings)

```text
In the words of former US President Jimmy Carter, “Matthew Joseph Thaddeus Stepanek reminds us how easy it is to forgive others, to find something amazing even in the most trivial things and to celebrate the little gifts of life each day.” Mattie, as he is best known throughout the world, began writing poetry at age three and since birth has suffered from a rare form of muscular dystrophy. In the poems “The ME Poem”, “Circle of Happiness”, “Heartsong”, “About Living” “MDA Summer Camp Is”, and “About Heaven”, Mattie confronts his mortality through the power of words that inspire and enrich the human spirit.

Mattie died June 22, 2004.
```

### Performance text (classify this)

```text
I am Mattie J.T. Stepanek.
My body has light skin,
Red blood, blue eyes, and blond hair.
Since I have mitochondrial myopathy,
I even have a trach, a ventilator, and oxygen.
Very poetic, I am, and very smart, too.
I am always brainstorming ideas and stories.
I am a survivor, but some day, I will see
My two brothers and one sister in Heaven.
When I grow up, I plan to become
A daddy, a writer, a public speaker,
And most of all, a peacemaker.
Whoever I am, and whatever happens,
I will always love my body and mind,
Even if it has different abilities
Than other people’s bodies and minds.
I will always be happy, because
I will always be me.

The “ME” Poem
Magic of Heartsongs,
Afraid of a memory and the dark,
Truthful and sincere,
Teacher of peace,
Inspiring, intelligent, lover of ice crea,
Enthusiastic and ebullient
Sunset watcher, shell and rock collector,
Tiger in Martial Arts,
Excited about celebrating life,
Playful, prayerful, patient,
Always ready with a hug and smile,
Never at a loss for words,
Energetic (like the Energizer Bunny)
Keeps on reading and writing
And reading and writing…
This is me!

Circle of Happiness
I am a little kid
For you to love.
I am a little kid
For you to hug and kiss.
I am a little kid
For you to say,
“You are so special,
Yes you are” to.

I am a little kid
For all of those things
And more.
And when you
Feel and say and do
All of those things,
I will be a little kid
Who will love you.
I will be a little kid
Who will hug and kiss you.
I will be a little kid
Who will say to you,
“You are so special, too,
Yes you are.”
I will be a little kid
Who will do all of those things
And more.
And that is what
Happiness
Is all about.

Heartsong
I have a song, deep in my heart,
And only I can hear it.
If I close my eyes and sit very still
It is so easy to listen to my song.
When my eyes are open and
I am so busy and moving and busy,
If I take time and listen very hard,
I can still hear my Heartsong.
It makes me feel happy.
Happier than ever.
Happier than everywhere.
And everything and everyone
In the whole wide world.
Happy like thinking about
Going to Heaven when I die.
My Heartsong sounds like this - -

I love you! I love you!

How happy you can be!

How happy you can make

This whole world be!

And sometimes it’s other
Tunes and words, too,
But it always sings the
Same special feeling to me.
It makes me think of
Jamie, and Katie and Stevie,
And other wonderful things.
This is my special song
But do you know what?
All people have a special song
Inside their hearts!
Everyone in the whole wide world
Has a special Heartsong.
If you believe in magical, musical hearts,
And if you believe you can be happy,
Then you, too, will hear your song.

About Living
Although I am
Greatly anticipating
Going to Heaven
When I die,
I would really like
To finish my life
On earth as a mortal
For a long time first.
But,
I know that life
On earth is limited.
And,
I know that Life
In Heaven is eternal.
So,
Every day,
No matter who we are,
What we do, or
Where we are,
We must celebrate
The gift of life on earth
While we have it,
For ever.

MDA Summer Camp Is
MDA Summer Camp is
…A place where kids wish
Onto paper that is placed into
Balloon-carried baskets,
Then hopefully pray as
Their thoughts and dreams
Ascend into the heavens.
MDA Summer Camp is
…A feeling of friends
Helping friends,
Whoever they are,
However they are,
Wherever they are,
For whatever reason,
Just because they are.
MDA Summer Camp is
…An understanding
That the worth of a person
Should never be measured
By number of years lived, or
By physical or mental abilities,
But by the strength of spirit.
MDA Summer Camp is
….A time for commemoration,
And liberation,
And rejuvenation,
And celebration,
In spite of the realities of life.
…Thank God, that
MDA Summer Camp IS.

About Heaven
Now, I will tell you about Heaven.
Where is Heaven?
It is way over there, and
It is way over there, and
It is way over there, too.
It is everywhere.
What does it look like?
It looks like school, and
It looks like a farm, and
It looks like a home.
It looks like Everything.
What does it sound like?
Well,
I really don’t know,
Because I am just
A little big boy
With a brother,
And another brother and sister,
And a friend,
Who live in the
Everywhere and Everything of Heaven.
But perhaps,
Heaven sounds like
Forever.
```

---

## IC-1700: Stereotypically Asian -- A Program

- Title: Stereotypically Asian -- A Program
- Author (byline): Candace Chiang and Alex Dang
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 984
- Already set (do not supply): none

### Source block (context only)

```text
Author: Candace Chiang
Newspaper: The Daily Californian
Website:
https://www.dailycal.org/stereotypically-asian-poem
Publisher: Dailycal.org
Date (Month/Year): November 5, 2017
Author: Alex Dang
Book: You Can Do Better
ASIN: B00YSYVI5A
Publisher: Where Are You Press
Date (Month/Year): Jan 2014
Transcript of poem also available on-line at
https://www.poemhunter.com/poem/what-kind-of-asian-
are-you/
Performance at the National 2013 Poetry Slam can be
viewed here:
https://www.youtube.com/watch?v=VoP0ox_Jw_w&t=8s
```

### Introduction (context only: never use it for content warnings)

```text
Many young Asian-Americans struggle with their bi-cultural identities -- expected to adhere to multiple sets of norms, none of which quite fit. On one hand, they’re encouraged to embrace American culture and shed ties to their Asian heritage. On the other hand, they’re expected to maintain their ethnic identity and keep their parents' traditions alive. Failure to live up to either set of expectations can sometimes lead to a fear of rejection, being ostracized. even an identity crisis of sorts.

Just what does it mean to be . . . Stereotypically Asian – A Program with poems by Candace Chiang and Alex Dang
```

### Performance text (classify this)

```text
Stereotypically Asian by Candace Chiang
when i was 14, i
consoled a crying friend
over her math grade.
she laughed
self-deprecatingly.
“am i even asian, then?”

when i was 15, i
helped a friend in math every day.
she wasn’t doing well,
no matter how much effort she put in. one day,
frustrated, she announced her hatred for the school,
for the area and its culture,
for silicon valley.

when i was 16, i learned that a friend was depressed, maybe even borderline suicidal.

when i was 17, i was talking to my friend when she let spill that she wanted to pursue the humanities and ranted that she was the only goddamn asian in this school, in the bay area even, who didn’t want to pursue stem.

people call asians the “model minority.”
we’re associated
with being smart
and generally overachieving, videos of amazing performers
waved off with a, “well, he’s asian,” comment that
apparently
explains everything.
we’re all upper-middle class who make
lots of money in big corporations.
we all score incredibly on tests,
go to top-100 colleges and successful careers.
we’re heterosexual, complacent and apolitical.
we have small eyes, faces that white men
sometimes find attractive.
we’re east asian,
chinese, japanese, korean.
we’re the “model minority.”

and so asians are lumped into one huge category,
and stereotyped.
but many of us are dirt poor.
but asians are ethnically more diverse than
chinese, japanese, korean
(even if some are now classified as
pacific islanders, because they’re different
from the image people associate “asian” with).
but hand in hand with this stereotype is
a culture of ever-increasing stress, pressure, overwork,
and an intense fear of failure —
a culture people are failing to address.
but we aren’t represented in government.
but when you’re asian and applying for
colleges, jobs, positions,
you’re forced to find ways to “stand out”
and prove yourself to be different
from the stereotype, because apparently,
no one wants that.

in many cases, i’m probably a stellar example
of the “model minority.”
i’m at a top college. i did well in school.
i’m even pursuing computer science, and so supposedly,
i will land a six-figure job right out of college.
but that barely tells you anything about me,
about my experiences,
about my interests,
and if i am going to be judged and
have my voice dismissed because i fit the “asian”
stereotype,
i will tear apart these notions of me.

What Kind of Asian are You? by Alex Dang
So she said to me: "What kind of Asian are you?" And I
said back . . .
“That's a loaded question.
What kind of Asian do you EXPECT me to be?
Because any way you slice that egg roll,
I'm still pretty much whatever you want to see.”

I've played many a Far East stereotype:
awkward math genius,
cold and calculated Kung-Fu expert,
assistant to "Dr. Jones, you crazy!"
You want me to drive? How so?
I can give you
Tokyo Drift,
Jeremy Lin
Mario Kart,
Tiger Woods,
and Blinker left on for about half a mile
I am the foremost expert on
all things Asian.
The Mejii era and the ban of the Samurai?
Done.
Confuciusism versus Daoism? I'll give it to you with no
slant!
What's the difference between Asian stereotype
1 and 2?
WELL LET ME TELL YOU.
Let me tell you anything YOU
want to know about my culture
Let me tell you in a Mulan-esque soliloquy
of me staring in the mirror asking
Who IS that girl staring that I see?
Let me tell you about Jackie Chan
and Bruce Lee and how they are related
BY BLOOD to me
Let me tell you about being so marginalized
it's to the point of "I really CAN'T believe
that's Asian!"
Let me tell you about derogatory terms
and origins of words such as chink and gook
Let me tell you about the struggle
of Asian parents not knowing the language
so we ate pet food because it was cheaper
Let me tell you about the job of interpreter
when you're still playing with LEGO blocks but
you're English is already that much better
than your guardians
Let me tell you about honor and dignity
Let me tell you about a society that
projects us as nothing but the secondary role
and never the leading man.

Let me tell you all the things you don't want
to know.
Like how chink comes from
the clanking of metal to railroads
as the slaves built train tracks for
this country to be connected.
Like how the zipperhead down the street
is called that because of the way our heads
split open when struck with assault weapons
or how the Jeeps ran over and left marks
across corpses and someone clever thought
that we were only good to unzip.
Like how every time you lump an Asian person
into one culture is systematically making us
assimilate into an America we thought was
better than our war torn home and every time you
confuse me
with some other nationality that I might share similar
features to is stripping away my individuality
And I still feel the shame of being Asian
the heat and pious dedication
of June 11th 1963
the envy of blonde hair
and blue eyes
And I still remember thinking where all the
boys that looked like me on TV were
the broken words
of my mother and father stage diving
off my tongue
the anger I felt when those
kids thought I'd get them sick
And I still feel the ash of the incense burn
my hands
when I prayed for my family
And I still remember thinking my skin
was what I was worth
And I still feel the ironwork of my bones
grow stronger with every train of thought
that
passes by
And I still feel pride
And I still feel heritage
And I still feel Chinese
And I still feel Vietnamese
And I still feel American
And I still feel
```

---

## IC-1701: Stories I Ain’t Told Nobody Yet

- Title: Stories I Ain’t Told Nobody Yet
- Author (byline): Jo Carson
- Work: Not specified
- Publisher: Orchard Books
- Publication date as stated: April 1989
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: VOICE 1, VOICE 2, VOICE 3, VOICE 4, VOICE 5
- Teaser before the introduction: Yes
- Spoken words (computed): 1188
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jo Carson
ISBN: 978-0531058084
Publisher: Orchard Books
Date (Month/Year): April 1989
```

### Introduction (context only: never use it for content warnings)

```text
In the middle of the breathtaking scenic views, rivers, waterfalls, green hills, and quaint historic towns, lies a part of Appalachia overlooked and unseen. Hidden places where people live in conditions that rival any urban slum.

There is a lesson here that possessions, careers and carefully landscaped properties do not bring happiness. It is something that comes from within.

Stories I Ain’t Told Nobody Yet by Jo Carson
```

### Performance text (classify this)

```text
VOICE 1: MOTHER
(Pg 93) I am asking you to come back home
before you lose the chance of seein’ me alive.
You already missed your daddy.
You missed your uncle Howard.
You missed Luciel.
I kept them and I buried them.
You showed up for the funerals.
Funerals are the easy part.

You even missed that dog you left.
I dug him a hole and put him in it.
It was a Sunday morning, but dead animals
don’t wait no better than dead people.

My mama used to say she could feel herself runnin’ short of the breath of life. So can I. And I am blessed tired of bury in’ things I love. Somebody else can do that job to me. You’ll be back here then; you come for funerals.

I’d rather you come back now and got my stories.
I’ve got whole lives of stories that belong to you.
I could fill you up with stories,
stories I ain’t told nobody yet,
stories with your name, your blood in them.
Ain’t nobody gonna hear them if you don’t
and you ain’t gonna hear them unless you get back home

When I am dead, it will not matter how hard you press your ear to the ground.

VOICE 2:
(Pg 29) Mountain people
can't read,
can't write,
don't wear shoes,
don't have teeth,
don't use soap,
and don't talk plain.
They beat their kids,
beat their friends,
beat their neighbors,
and beat their dogs.
They live on cow peas,
fatback and twenty acres
straight up and down.
They don't have money.
They do have fleas,
overalls,
tobacco patches,
shacks,
shotguns,
foodstamps,
liquor stills,
and at least six junk cars in the front yard.
Right?
Well, let me tell you:
I am from here,
I'm not like that
and I am damned tired of being told I am.
TRANSITION
Jo Carson sincerely believes that all lives speak truths worth
listening to . . . she intentionally sets out to elevate common
people, their stories and their language to the level of art,
without denying their authenticity. . .

VOICE 3:
(Pg 5) It’s gettin’ to where
you can’t give a person nothin’ anymore
and it’s too damn bad.
Now, my neighbor
could look the devil in the eye
and say no thanks he didn’t want to go to hell,
while at the same time
tryin’ to slip Jesus Christ a couple of dollar bills
For the free give of salvation.
He’s a hard man
and he’s about to drive me crazy.
Fifty cents he puts in my mailbox,
or a dollar or somethin’,
and all I did was give his wife
a couple of tomoatoes
and a mess of old string beans.

And they ain’t rich
Then, yesterday, I picked a half a bushel
of them little ol’ zucchini squash
and I carried over five or six
and put them on his porch
with a note that said,
“These are a present.”
Present was underlined.
and today,
there’s a dollar in my mailbox.

The man don’t understand
he’s doin’ a favor
when he takes and eats them damn zucchini,
and when he pays me for ‘em,
when he pays me for ‘em
it’s me ends up beholden to him.

TRANSITION According to the most recent U.S. Census, Appalachia has the lowest median household income in the states with a staggering 41.5 per cent of residents falling below the poverty line. But residents take pride in their community's history; and locals are driven to help one another through hard times.

VOICE 4:
(Pg 7) I spent the first years of my life
sittin’ on what we called splinter benches
‘cause we were too poor for store-bought furniture.
You scooted, you got splinters
My mama used to cry
‘cause she wanted a bed with a real mattress
for Grandma Lynn to die on.
Turned out Grandma Lynn didn’t need it.
She died mid-sentence at the women’s circle
But the first money I ever earned
I got Mama a store-bought mattress.
Daddy bought her two straight-back chairs
so she and him could sit proper at the table.
It was her birthday.
I never seen anybody since
mad so happy by a gift.

When Daddy finally found regular work
first thing they did was ride down to McEnniss’s
and chose a houseful of fancy stuffed furniture.
Bought it on time, had it delivered, and paid for years.
The day it came, Mama and I stood out back
bustin’ the old stuff with an ax.
Mama said if they couldn’t pay for their bed
she’d rather sleep on the floor than have that one back.
We burnt furniture for kindling all that winter.
Mama’d say, “Here goes the table, Charlie!”
and she and Daddy’d laugh and raise their coffee cups
to toast their new prosperity.

Turns out we burnt what could have been
my fortune in antiques. [I] collects ‘em.
-- primitive;
it’s the very stuff my mama didn’t like,
and now I’m supposed to fix it so it don’t ruin clothes
instead of bust it up.
I don’t mind, might as well be this as something else,
but if I do get to heaven, if I do get to meet my mama again,
I don’t know how in this world or that one
I’m gonna explain why I still go splinters in my seat.

TRANSITION “Trailer trash” - Those two words hit me in hard. Throughout my life they’ve been directed at most everyone I knew and loved. My people had been reduced to two ugly words. I’m here to tell you, it doesn’t matter how much money you were raised with, or how you were raised, or what kind of accent you have: a whole lot of people in the world assume that if you are Appalachian, you are the same as that image they have of “trailer trash.” They are not trash. They are mothers, fathers, families . . .. They are my people.

VOICE 5:
(Pg 89) I watched the first sunrise
I remember seeing last week.
I am thirty-five.
I’m up at sunrise, I have
a job that ruins my wrists
and two children.
By sunrise, I am already busy.
Once, I sat awake for
a month of sunrises
that began with a call
from the youngest: Mama..,.,
The child got sick
he would not open his eyes.

His room faced west. I watched—I counted—sunsets. He is thirteen now and mows for spending money. So, Saturday, my husband and I left the house before dawn. It was my birthday, my choice, my present, we went fishing. I love fishing. The pain was in my wrists but casting a fishing line is not the same as dis-assembling chickens— that’s their word for it– on a factory line. My job. There we sat, me shivering, In the dark with the crickets and a rim of bright pink lit the mountains so quickly I didn’t notice it coming. It looked like an accident. What’s that? I asked. This sounds so foolish now. That light. “The dawn,”

my husband said and laughed.
I wept, I couldn’t stop myself,
I don’t ever remember seeing
a sunrise before.
“Happens every morning,
where on earth you been?” he asked.
Cutting up chickens.
Raising children.
```

---

## IC-1702: The Story of Our Lives

- Title: The Story of Our Lives
- Author (byline): Mark Strand
- Work: Selected Poems by Strand
- Publisher: Atheneum Books
- Publication date as stated: 1981
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1264
- Already set (do not supply): none

### Source block (context only)

```text
Author: Strand, Mark
Book: Selected Poems by Strand
ISBN: 978-1857541908
Publisher: Atheneum Books
Date: 1981
```

### Introduction (context only: never use it for content warnings)

```text
We don’t write the story of our lives alone. Every one of us could draw the arc of our through-line and people it, at the critical moments, with both antagonists and heroes – moments of crushing defeat, and moments of deliverance. Our lives are stories of sometimes-uncertain salvation, and we are not through, yet with The Story of Our Lives by Mark Strand
```

### Performance text (classify this)

```text
1
We are reading the story of our lives
which takes place in a room.
The room looks out on a street.
There is no one there,
no sound of anything.
The tress are heavy with leaves,
the parked cars never move.
We keep turning the pages, hoping for something,
something like mercy or change,
a black line that would bind us
or keep us apart.
The way it is, it would seem
the book of our lives is empty.
The furniture in the room is never shifted,
and the rugs become darker each time
our shadows pass over them.
It is almost as if the room were the world.
We sit beside each other on the couch,
reading about the couch.
We say it is ideal.
It is ideal.

2
We are reading the story of our lives,
as though we were in it,
as though we had written it.
This comes up again and again.
In one of the chapters
I lean back and push the book aside
because the book says
it is what I am doing.

I lean back and begin to write about the book.
I write that I wish to move beyond the book.
Beyond my life into another life.
I put the pen down.
The book says: "He put the pen down
and turned and watched her reading
the part about herself falling in love."
The book is more accurate than we can imagine.
I lean back and watch you read
about the man across the street.
They built a house there,
and one day a man walked out of it.
You fell in love with him
because you knew that he would never visit you,
would never know you were waiting.
Night after night you would say
that he was like me.
I lean back and watch you grow older without me.
Sunlight falls on your silver hair.
The rugs, the furniture,
seem almost imaginary now.

"She continued to read.
She seemed to consider his absence
of no special importance,
as someone on a perfect day will consider
the weather a failure
because it did not change his mind."
You narrow your eyes.
You have the impulse to close the book
which describes my resistance:
how when I lean back I imagine
my life without you, imagine moving
into another life, another book.
It describes your dependence on desire,
how the momentary disclosures
of purpose make you afraid.
The book describes much more than it should.
It wants to divide us.

3
This morning I woke and believed
there was no more to to our lives
than the story of our lives.
When you disagreed, I pointed
to the place in the book where you disagreed.
You fell back to sleep and I began to read
those mysterious parts you used to guess at
while they were being written
and lose interest in after they became
part of the story.
In one of them cold dresses of moonlight
are draped over the chairs in a man's room.
He dreams of a woman whose dresses are lost,
who sits in a garden and waits.
She believes that love is a sacrifice.
The part describes her death
and she is never named,
which is one of the things
you could not stand about her.
A little later we learn
that the dreaming man lives
in the new house across the street.
This morning after you fell back to sleep
I began to turn the pages early in the book:
it was like dreaming of childhood,
so much seemed to vanish,
so much seemed to come to life again.
I did not know what to do.
The book said: "In those moments it was his book.
A bleak crown rested uneasily on his head.
He was the brief ruler of inner and outer discord,
anxious in his own kingdom."

4
Before you woke
I read another part that described your absence
and told how you sleep to reverse
the progress of your life.
I was touched by my own loneliness as I read,
knowing that what I feel is often the crude
and unsuccessful form of a story
that may never be told.
"He wanted to see her naked and vulnerable,
to see her in the refuse, the discarded
plots of old dreams, the costumes and masks
of unattainable states.
It was as if he were drawn
irresistably to failure."
It was hard to keep reading.
I was tired and wanted to give up.
The book seemed aware of this.
It hinted at changing the subject.
I waited for you to wake not knowing
how long I waited,
and it seemed that I was no longer reading.
I heard the wind passing
like a stream of sighs
and I heard the shiver of leaves
in the trees outside the window.
It would be in the book.
Everything would be there.
I looked at your face
and I read the eyes, the nose, the mouth . . .

5
If only there were a perfect moment in the book;
if only we could live in that moment,
we could being the book again
as if we had not written it,
as if we were not in it.
But the dark approaches
to any page are too numerous
and the escapes are too narrow.
We read through the day.
Each page turning is like a candle
moving through the mind.
Each moment is like a hopeless cause.
If only we could stop reading.
"He never wanted to read another book
and she kept staring into the street.
The cars were still there,
the deep shade of trees covered them.
The shades were drawn in the new house.
Maybe the man who lived there,
the man she loved, was reading
the story of another life.
She imagine a bare parlor,
a cold fireplace, a man sitting
writing a letter to a woman
who has sacrificed her life for love."
If there were a perfect moment in the book,
it would be the last.
The book never discusses the causes of love.
It claims confusion is a necessary good.
It never explains. It only reveals.

6
The day goes on.
We study what we remember.
We look into the mirror across the room.
We cannot bear to be alone.
The book goes on.
"They became silent and did not know how to begin
the dialogue which was necessary.
It was words that created divisions in the first place,
that created loneliness.

They waited
they would turn the pages, hoping
something would happen.
They would patch up their lives in secret:
each defeat forgiven because it could not be tested,
each pain rewarded because it was unreal.
They did nothing."

7
The book will not survive.
We are the living proof of that.
It is dark outside, in the room it is darker.
I hear your breathing.
You are asking me if I am tired,
if I want to keep reading.
Yes, I am tired.
Yes, I want to keep reading.
I say yes to everything.
You cannot hear me.
"They sat beside each other on the couch.
They were the copies, the tired phantoms
of something they had been before.
The attitudes they took were jaded.
They stared into the book
and were horrified by their innocence,
their reluctance to give up.
They sat beside each other on the couch.
They were determined to accept the truth.
Whatever it was they would accept it.
The book would have to be written
and would have to be read.
They are the book and they are
nothing else.
```

---

## IC-1703: The Storyteller’s Silence

- Title: The Storyteller’s Silence
- Author (byline): Nikki Giovanni
- Work: Not specified
- Publisher: William Morrow
- Publication date as stated: Jan 2007
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 824
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nikki Giovanni
ISBN: 978-0061231315
Publisher: William Morrow
Date (Month/Year): Jan 2007
* Gele (pronounced gay_lay) is a term for a woman's head
wrap. This piece of clothing can be as simple as a scarf-like
head-tie or bandana.
```

### Introduction (context only: never use it for content warnings)

```text
Imagine being torn from your family … forced to walk hundreds of miles until you reach the sea on the West African side of the Atlantic Ocean. You are stripped of your name, your identity, of every right a human being deserves. The European ship that you are forced to board, is filled with a multitude of black people chained together, with scarcely room to turn. Death and disease are all around and only one in six will survive this journey and the brutal, backbreaking labor that follows… The Storyteller’s Silence by Nikki Giovanni
```

### Performance text (classify this)

```text
Poems have serious business to do
Poems have to tell the truth
They need to remind people of our sacred duty
To remember the captured people whom we

called Slaves
To remember they believed in tomorrow
They believed in us
They believed in the power of a serious poem
To carry our story forward
Poems are serious business
And only serious people
Should apply

(From Serious Poems by Nikki Giovanni; Acolytes, 2007)

There must have been a silence.
Not a moan, not a mumbling word. But a silence.
The shock. The absolute disbelief.
The incredible stunning astonishing gaping shame.
At capture.
The incomprehensible knowledge that the sun stood still.
The stars extinguished their twinkles.
The winds and the rains fled underground.
The moon withdrew its comforting glow.
Not only the silence of different languages.
Different images.
Different words for the same objects.

The holocaustic silence of the unthinkable now made

manifest.
The captured did not understand their captors.
Nor each other.
They only understood the chains. The whips.
The desecrations. The destructions. The horror.
Yet that should not. Could not.
Have been the reason for silence.

Maybe there was nothing more to say.

The long lines on the trips to the coast.
The babies crying. Then being thrown into the bush.
Or run through with a bayonet.
The mothers screaming. And fighting back.
And being murdered also.
The animals that lived the trail of the slavers.
Grew used to everything coming easy.
Grew expectant. And fat. And lazy.
Grew more evil.
In their own imaginations.

Grew impossible to live with.
Themselves. Anyone else.
Grew crazy in the trade. Of human flesh.
And human souls.
Prayed at the river. Tithed to the church.
Searched their Bible.
And still went in the night to the captured.
And still sought relief and understanding.
And still tried to justify.

Someone had to look. To remember.

The screaming commands. The cracking whips.
The kicking boots indicating time:
To go to the big ships.
To be brave and strong.
To find a way to stay human.
Some will jump. And some will expire.
Some will kill their captors. And some will escape.
But most will find themselves. On an auction block.
Being intruded upon.

Being violated.
Being branded and corralled.
But the spirit stayed.
And the heart remembered.
They were silent because there were no words to

express it.

The salt of the tears.

The salt of the blood.

The salt in the wounds.

All knew.
It cannot be unusual.
That the slaves left no written records.
They were denied rudimentary materials.
But they sang a song. And they preached a service.
And their story was codified. And sanctified.
And passed along.
And the second voice of the people ripped from Africa.
Whipped into the New World.
Molded on the plantations.
Came from their feet.

The feet spoke clearly when they ran away.
And they ran away. And away. And away
so much that the South had to make America safe
for slavery by passing The Fugitive Slave Law
which would not have been needed.
If the slaves had not spoken so loudly.
Through Gabriel Prosser.
Through Denmark Vesey.
Through Nat Turner.
Through the Underground Railroad.
They spoke so loudly.
A man named John Brown.
Who wanted his sons. To be free men. Heard them.
Prayed about it. Took his sons. And led the charge.
Against Harpers Ferry.
Against the corrupt federal government.
Against his own white skin.
And started the war. That freed the slaves.
That offered to free America.
If America hadn't been too venal.
Too stupid.

Too arrogant. To understand what a gift had been offered.

It is not unusual that so few found a way.

It is unusual that so many did.

And out of the hearts. And hopes.
Out of the souls and salvation. The words tumbled.
The words ran to the riverside.
Shouted from the mountains.
Wove themselves into blankets.
Wrapped themselves in Gelees*.
Whispered in the night. A freedom song.
A brave and wondrous story not of survival but of

triumph.
Through thunder and fire.
Through gentle rain.
Through heavy, violent winds.
Through magnolia breezes.
The Americans who were once captured and enslaved.
The Americans who were once considered a little less

than chattel. The Americans who didn't want to come and

were not happy to be here.

Now became not the voice of the slaves.

But the voice of America. It is not nearly so unusual that the printed word is

spoken. But that the spoken word is printed.

Stamped.
Paginated.
Made available. To the world.
To tell the story. Of a person.
Of a people.
Of the undeniable will.
To prevail.

So we come to these voices.
To Zora Neale Hurston.
To Langston Hughes.
To Richard Wright.

To Gwendolyn Brooks. To Lorraine Hansberry. To all of us who are ...

in the mighty words of Martin Luther King, Jr.
Free At Last! Free At Last!
Free to break our Silence.
Free to tell our story.
Free to love and laugh.
```

---

## IC-1704: Suicide Note(s) – A Collection

- Title: Suicide Note(s) – A Collection
- Author (byline): Ellen Hopkins, Ebukun Gbemisola
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1051
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ellen Hopkins
Book: Impulse
ISBN: 978-1416903574
Publisher: McElderry Books
Date (Month/Year): Jan 2007
Author: Ebukun Gbemisola Ogunyemi
Book: The Lost Poets: Suicide Notes
ISBN: 978-1799078135
Publisher: Independently Published
Date (Month/Year): March 7, 2019
Author: Janice Mirikitani
Book: The Oxford Book of Women's Writing in the
United States
ISBN: 978-0195132458
Publisher: Oxford University Press
Date (Month/Year): 1999
Author: Daisy Bojorquez
Book: The Lost Poets: Suicide Notes
ISBN: 978-1799078135
Publisher: Independently Published
Date (Month/Year): March 7, 2019
```

### Introduction (context only: never use it for content warnings)

```text
Talking about suicide is difficult . . . I get it. But according to experts, what we say or don't say, and how we say it, makes a difference. Our words matter to those struggling with thoughts of ending their own lives and to those reeling from the loss caused by suicide. Regardless of race, gender, or culture . . . silence makes matters worse and that’s why it's time to talk about . . . .

Suicide Note(s) – A Collection by Ellen Hopkins, Ebukun
```

### Performance text (classify this)

```text
Ogunyemi, Janice Mirikitani, and Daisy Bojorquez

Impulse by Ellen Hopkins (excerpts from a novel written in verse)

Wish

You could turn off

The questions, turn

Off the voices,

Turn off all sound Yearn

To close out

The ugliness, close

Out the filthiness,

Close out all light. Long

To cast away

Yesterday, cast

Away memory,

Cast away all jeopardy. Pray

You could somehow stop

The uncertainty, somehow

Stop the loathing,

Somehow stop the pain

Gbemisola Ogunyemi, Janice Mirikitani, and Daisy Bojorqueza

The first cut
Wasn’t the deepest.
No, not at all.
It was like the others,
A subtle rend of anxious skin,
A gentle pulse of crimson,
Just enough to hush the demons
Shrieking inside my brain
But this time they wouldn’t
Shut up. Just kept on
Howling, like mama,
When she was in a bad way.
Worst thing was, the older
I got, the more I began to see
How much I resembled mama
Falling in and out of the blue,
Then lifting up into the white
That day I actually
Thought about howling
So I gave myself to the knife,
Asked it to bite a little
Harder, chew a little deeper.
The hot, scarlet rush
Felt so delicious
I couldn’t stop there.
The blade might have reached
Bone, but my little
Brother, Bryan
Barged into the bathroom,
Found me leaning against
Grandma’s new porcelain
Tub, turning its unstained
White pink.
You should
Have heard
Him scream.

I hate this feeling
Like I’m here, but I’m not.
Like someone cares.
But they don’t.
Like I belong somewhere
Else, anywhere but here,
And escape lies just past
That snowy window,
Cool and crisp as the February
Air. I consider the streets
Beyond, bleak as the bleached
Bones of wilderness
Scaffolding my heart.
Just a stone’s throw away.

Selections from this novel in verse received the following
awards:
2008 National Qualifier
2010 National Qualifeir

Ebukun’s Suicide Note by Ebukun Gbemisola Ogunyemi (Better known at Ibukunwrites)

. . . A Nigerian storyteller and creative writer, she writes to shed light, bring light, hope and restoration. . .

This is the suicide note
I never wrote on days when I
Tried taking my own life but chickened out.
This is the exhaustion I couldn’t put into words
because I had absolutely nothing to pour
too stressed to write
I just wanted to leave
No one wants you when you’re here but
everyone suddenly wants you to stay when you’re gone
I told myself
I had no loved one to write to
Whatever they made of my demise, I could care less
but I guess I was mad
I was mad about the love I constantly sought but
never got.
But isn’t this life
Isn’t my life worth more than a protest?
Isn’t this life given to me for a reason?
Isn’t this life mine and no one else’s for a reason?
Yes, I thought as much.
The reason I have to fight this hard is because
I have the ability to survive
so today and every other day, I’ll choose to stay
this space is mine, this space belongs to me
so I just don’t get to walk away
So today and every other day
I’ll choose to stay, I’ll chose to fight
I’ll resist the urge to die and fight one last time
until there are no wars – no wars to be fought.

Suicide Note by Janice Mirikitani . . . An Asian American college student was reported to have jumped to her death from her dormitory window. Her body was found two days later under a deep cover of snow. Her suicide note contained an apology to her parents for having received less than a perfect four point grade average. . .

How many notes written. . .

ink smeared like birdprints in snow.

not good enough

not pretty enough

not smart enough
dear mother and father.
I apologize
for disappointing you.

I’ve worked very hard,

not good enough
harder, perhaps to please you.
If only I were a son, shoulders broad
as the sunset threading through pine,
I would see the light in my mother’s
eyes, or the golden pride reflected
in my father’s dream
of my wide, male hands worthy of work
and comfort.
I would swagger through life
muscled and bold and assured,
drawing praises to me
like currents in the bed of wind, virile
with confidence

not good enough

not strong enough

not good enough
I apologize.
Tasks do not come easily.
Each failure, a glacier.
Each disapproval, a bootprint.
Each disappointment,
ice above my river.
So I have worked hard.

not good enough
My sacrifice I will drop
bone by bone, perched
on the ledge of my womanhood,
fragile as wings.

not strong enough
It is snowing steadily
surely not good weather
for flying—this sparrow
sullied and dizzied by the wind
on the edge.

not smart enough
I make this ledge my altar
to offer penance.
This air will not hold me,
the snow burdens my crippled wings,
the tears drop like bitter cloth
softly into the gutter below.

not good enough

not strong enough

not smart enough

Choices thin as shaved

ice. Notes shredded

drift like snow

on my broken body,
covers me like whispers
of sorries
sorries.
Perhaps when they find me
they will bury
my bird bones beneath
a sturdy pine
and scatter my feathers like
unspoken song
over this white and cold and silent
breast of earth.

Daisy’s Suicide Note by Daisy Bojorquez . . . Despite having a mental illness and a difficult life, she was able to survive and is now an artist and poet living in Southern California. This poem was written to comfort those in need and to help them hang on for one more day. .

Finally,
I just wanted the pain to stop.
But . . .
Did I really just do this?
Oh my God . . .
Wait . . .
My life is passing by my eyes.
I see my parent’s faces.
I see my best friend’s face.
I see the face of my love.
Wait . . .
Now I see them crying.
Sobbing.
I see them blaming themselves.
All of a sudden I don’t know if I want this . . .
This was supposed to be release for me . . . for them . . .
I thought I was just a heavy burden . . .
No one complete understood.
The pain and the sadness that engulfed me each day . . .

But they still loved me.
My live continues to leave me. . .
Oh my God I was wrong . . .
What did I . . . . . . . .
```

---

## IC-1705: Sweet Jesus: Strange Faith

- Title: Sweet Jesus: Strange Faith
- Author (byline): Ron Koertge
- Work: Sweet Jesus: Poems About The Ultimate Icon; Section: Strange Faith
- Publisher: Anthology Pr
- Publication date as stated: Oct 2002
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1154
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ron Koertge
Book: Sweet Jesus: Poems About The Ultimate Icon;
Section: Strange Faith
ISBN: 978-0972055901
Publisher: Anthology Pr
Date(Month/Year): Oct 2002
```

### Introduction (context only: never use it for content warnings)

```text
Sweet Jesus is an odd and refreshingly lively anthology of poems about Christ from the best of our contemporary poets. The poem rages, laughs, wonders, and loves as it reflect son Christ. It breathes in moments with which any reader can identify. This poem locates Christ in our world. He is here, with us, in this mysterious life. This poem bears powerful witness to that truth. Sweet Jesus: Strange Faith by Ron Koertge.
```

### Performance text (classify this)

```text
If you exist, I said. Send me a pony. Immediately Jesus appeared in my bedroom. I got off my knees. You heard my prayer! He quoted himself. "Except ye see signs and miracles, you will not believe." Be reasonable, Jesus. It's hard to just take Your word for it. "But I'm here. In your bedroom. Isn't that enough?" So, is the pony outside?

It was supposed to be Arts and crafts for a week, but when she came home with the Jesus Saves button, we knew what art was up; what ancient craft. She liked her little friends. She liked all the songs she sang when they weren't twisting and folding paper into dolls. What could be so bad? Jesus had been a good man and putting faith into Good men was what we had to do to stay this side of cynicism. The other sadness.

Ok, we said. One week. But when she came home singing Jesus loves me, the bible tells me so, it was time to talk.

We're Jewish. we don't believe in Christ. If God wanted us to worship Jesus, he would have arranged for us to be born into an Italian family.

There are a few stories about Jesus as a child, but there are no stories about him as a teenager. Did he make his bed without being told, or was he the kind of boy who jumped out from behind bushes, scaring girls on their way to the well. Making them drop those picturesque amphoras.

Late last night on State Street, I saw Jesus. Or at least a good facsimile. Hustling. He had it all. The hair, the beard, the piercing eyes, the hot glare of a man with hidden wounds. But his righteous anger sabotaged his efforts. Nobody slowed their cars to wave him over. Nobody loitered at the corner, looking back. A mad girl dies, giving birth to a bastard son. Who, instead of being left to starve, is trained by her uncle to work with wood. By ten, the boy is muttering to the desert air, telling strangers to bow down, I'm King David's heir. His designs sell so briskly, that his uncle tolerates his eccentricities.

Could I tell her, Jesus doesn't love you? Could we say the bible is a great book certain people use to make you feel bad? We sent her back without a word. It had been so long since we believed. So long since we needed Jesus as our nemesis and friend, that we thought he was sufficiently dead. That our children would think of him like they do of Lincoln or Thomas Jefferson.

He was probably a cool kid. One all the others looked up to. It wasn't only that he said he wouldn't live very long. A lot of the other guys said that. Especially those who drank too much wine, and raced their donkeys. But Jesus was different. While everybody else partied by the Dead Sea, he'd take his rowboat out, step right off the bow, and sink, like a stone. Then he'd swim back in all mad. His friends could tease him out of a bad mood, though, and pretty soon, he'd change water into beer, and make one hot dog feed everybody. Girls liked him, but he wasn't into them. Though, no way was he like Obadiah, who made his own curtains.

A year after the uncle dies, the boy, now thirty-three, is jailed. For vagrancy. Sentenced to death, he hears God whispering, My son. The next day he's crucified as he shrieks God's vengeance down. Joking and laughing, Roman soldiers raise his cross exactly as an earthquake hits. Houses fall flat. Dust blocks the sun. The carpenter dies raving, but one witness, Matthew, the storyteller, sets to work. Judas, who owes him money, makes the perfect villain in this tale. He brings in virgin birth, stars above a manger, wise men, and a holy child. As well as a few miracles, including one where the woodworker turns water into wine, and feeds a crowd with just one fish. Then he speaks Matthew's own thoughts on sin, faith, and treating others as you'd like to be treated. Friends make him tell his story again and again. It's your best work, they say. Truly inspired.

I tried to scan him, but not catch his eye. I was compelled, but not at all attracted. His hands, shoved in the pockets of his grimy, low slung jeans, could not be checked for glowing wounds. His sandaled feet, looked like they might pollute almost any water they would walk on. His chest was bare, his side was bruised, but whole. He was as fascinating as a three-car-crash jamming the world's most mundane freeway.

I have nothing against him. He was probably a very nice man. You have to give him credit for trying. A lot of people still believe he's the son of God. I don't know what he had against his real father, but if you ever did that to me, said you were somebody else's son, I'd be insulted.

There seems no reason he should die. His hands are pierced by holes too tidy to have kept hard untorn muscles as they writhed on spikes. No reason, and yet, Christ's eyes are swollen with it, his mouth hangs slack with it. Death. Most Christs return, but this one's flesh. He isn't coming back.

Halfway up the hill, Jesus has a change of heart, makes a break for it. The cross goes down, and he's off. The angry mob right behind him, chasing the trail of his stigmata. The chase scene is long, and of course, the Romans join in, crashing chariots into peddlers. But Jesus is fast, and winds his way through back alleys, and straight into the heat of the desert. The mob tries to bear down, but they're mostly drunk, and as noted, Jesus is fast. When capture looks hopeless, they stagger as one, shrug, and say, Ah, let's forget the whole thing.

On parents' night, there were the arts and crafts all laid out like appetizers. We took our seat in the church, and the children sang a song about the ark, Hallelujah, and one in which they had to jump up and down for Jesus. I can't remember ever feeling so uncertain about what's comic. What's serious. Evolution is magical, but devoid of heroes. You can't say to your child, Evolution loves you. The story stinks of extinction, and nothing exciting happens for centuries. I didn't have a wonderful story for my child. On the way home, in the car, she sang the songs. Occasionally standing up for Jesus. There was nothing to do but drive, ride it out, and sing along, in silence. But then, it occurred to us. You can't teach disbelief to a child. Only wonderful stories. And we didn't have a story nearly as good.
```

---

## IC-1706: Symbols of the Holocaust (A Poetry Compilation)

- Title: Symbols of the Holocaust (A Poetry Compilation)
- Author (byline): Jesse Parent
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
Author: Pastor Martin Niemooler
Book: Then They Came For Me
ISBN: 978-0465097869
Publisher: Basic Books
Date (Month/Year): Sept 18, 2018
Author: Jesse Parent
Book: To the Baby in My Belly (You Were Delicious)
ISBN: e-book
Publisher: Jesse Parent
Date (Month/Year): 2010
Can be purchased on-line at
http://www.jesster.net/store.html
Author: Jennifer Roy
ISBN: 978-0761463108
Publisher: Two Lions
Date (Month/Year): June 2014
Author: Elie Wiesel
Book: Night (Pg 106)
ISBN: 978-0374500016
Publisher: Hill and Wang
Date (Month/Year): January 2006
```

### Introduction (context only: never use it for content warnings)

```text
Today I, (insert name) speak out . . . Symbols make up a significant part of any cultural fabric. They have the power to transform a concept into a reality, to speak without words and to effect emotional responses from each and every one of us.

Symbols of the Holocaust – A Poetry Compilation by Pastor Martin Neimooler, Jesse Parent, Jennifer Roy and Elie Weisel.
```

### Performance text (classify this)

```text
First They Came by Pastor Martin Niemooler

First they came for the Communists
And I did not speak out
Because I was not a Communist
Then they came for the Socialists
And I did not speak out
Because I was not a Socialist
Then they came for the trade unionists
And I did not speak out
Because I was not a trade unionist
Then they came for the Jews
And I did not speak out
Because I was not a Jew
Then they came for me
And there was no one left
To speak out for me.

Hooked Cross by Jesse Parent

Little brother, look what they’ve done to me.

For millennia
I have woven myself into humanity’s dreams,
raced comet-like across their collective consciousness.
As basic as a circle,
a hooked cross.
A child of lines
and busy hands.
Simple. Recognizable.
They called me Swastika.

I was everywhere. Even in the one place I wished I wasn’t.

I admit I was jealous of you, little brother
and the star you rose up on.
For I was just a hooked cross,
glossed over on cracked claypots,
and deerskin teepees,
hidden along with kisses on the collars
of Chinese children
ironically, to protect them from evil spirits.
All of Asia blended me into their backgrounds,
Jainism, Buddhism, Hinduism.
I could tell you where any temple was.
A sun symbol.
A heart’s seal.
Eternity.
A minor celebrity on one continent,
a child’s absent doodle on the rest.

He took me West, little brother,
told me to point right and lean,
hold the pose.
Shone a bright, white spotlight on me
while I danced on a red carpet.
They all waved at me, little brother.
I got caught up in the rush
To become a major celebrity.

It was too late to turn back They slaughtered each other under my hooked shadow, the smoke of their flesh darkening my form. I let them make me into something horrible, simple, recognizable, detestable.

Humanity’s dreams no longer idly trace my form
in innocent doodles.
Countless millennia may never wash away
the stench on my lines
no matter which way I turn.
A minor celebrity on one continent,
a symbol of hatred on the rest.
So many killed while I waved over them,
their murderers justifying themselves
by the meaning they put into my shape.
They killed for me.

You don’t have my hooks, little brother,
but we have the same parents,
the same simplicity of lines.
We have had different men who have defined us,
even if we have both been worn by popes.
My body count is well over 6 million, little brother.

Pray they do not start counting up the ones that were killed for you.

TRANSITION

The Swastika wasn’t the only symbol of the Holocaust. The Star of David is a symbol we all know -- two overlaid equilateral triangles forming a six-pointed star.

Yellow Star (excerpt) by Jennifer Roy

(Pg 3-8) Fall 1939 I, [Sylvia Perlmutter], am four and a half years old, going on five, Hiding in my special place behind the armchair in the parlor, Listening.

The worry of grown-ups fills the air, “Must we go, Isaac?” Mother says to my father.

“We must leave right away,” Papa says. “This city is
unsafe for Jews.”
My mind freezes
On one word –
Jews.
Jews.
We are Jews.

I am Jewish, but that is all I know.
What does it matter that we are Jews?
It is wartime.
We are Jews.
The Nazis closed down
a small section of the city.
They said it is swarming
with infectious disease,
but still,
they ordered all Jews
to leave their homes
immediately
and move into that space.
It is called a ghetto.
All the Jews?
That must be more than one hundred!

(One hundred is the largest number I know.)

Papa corrects me. “Over one hundred thousand people, maybe twice that.”

Orange
is the color of my coat
with matching muffler
that I got as a present
before the war.

Yellow
is the color of
the felt six-pointed star
that is sewn onto my coat.
It is the law
that all Jews have to wear the
Star of David
when they leave their house,
or else be arrested.

I wish I could
rip the star off
(carefully, stitch by stitch, so as not to ruin my lovely
coat),
because yellow is meant to be
a happy color,
Not the color of hate.

TRANSITION

In 1939 the Germans invaded Poland. Two hundred and seventy thousand people were isolated in the Lodz ghetto. In 1945 the ghetto was liberated. Only 800 walked out of the ghetto. Of those who survived only twelve were children. Sylvia Perlmutter was one of them.

In the words of George Santayana, “Those who cannot remember the past are condemned to repeat it.” The world must never forget what the Jewish people endured.

Never Shall I Forget Elie Weisel

Never shall I forget that night, the first night in camp, that turned my life into one long night seven times sealed.

Never shall I forget that smoke.

Never shall I forget the small faces of the children whose bodies I saw transformed into smoke under a silent sky.

Never shall I forget those flames that consumed my faith for ever.

Never shall I forget the nocturnal silence that deprived me for all eternity of the desire to live.

Never shall I forget those moments that murdered my God and my soul and turned my dreams to ashes.

Never shall I forget those things, even were I condemned to live as long as God Himself.

(From the opening poem)
They came for the Jews
And I did not speak out
Because I was not a Jew

CLOSING

Swastikas . . . Yellow Stars . . . . Ghettos . . . . Concentration camps . . . . Smoke under a silent sky. . . Never should WE forget.
```

---

## IC-1707: The Taking of Room 114 (A Hostage Drama in Poems)

- Title: The Taking of Room 114 (A Hostage Drama in Poems)
- Author (byline): Mel Glenn
- Work: Not specified
- Publisher: Lodestar Books
- Publication date as stated: Mar 1997
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: STUDENT, MR. WIEDERMEYER, NEWSPAPER CLIPPING, EYEWITNESS, BYSTANDER, MR. WEIDERMEYER
- Teaser before the introduction: Yes
- Spoken words (computed): 1402
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mel Glenn
ISBN: 978-0525675488
Publisher: Lodestar Books
Date (Month/Year): Mar 1997
```

### Introduction (context only: never use it for content warnings)

```text
Students in Mr. Wiedermeyer’s senior history class are in for a shock when they attend one of their last classes of the year. They are held hostage by their teacher as police, and school administrators try to understand the puzzling notes Mr. Wiedermeyer slips under the door.

The Taking of Room 114 by Mel Glenn
```

### Performance text (classify this)

```text
CHERISE GRAHAM (Channel 5, Local News Anchor): (Pg 25) We interrupt our regular broadcast to bring you this late-breaking story. Police have been called to Tower High School to investigate a possible hostage situation. According to our sources, a senior history class has been taken over by a person or persons unknown. There are no reports of any injuries. There are no reports of any bombs. Police and emergency personnel are in the process of evacuating the building. As soon as we can, we will be bringing you a live update . . .

ROGER DUNLOP (Assistant Principal): (Pg 22) (with continued knocking on the door) Mr. Wiedermeyer, would you mind opening it up, please? Are you OK? Is the class OK? (no answer) Is any unauthorized person with you? Please open the door. Mr. Wiedermeyer. SHERWOOD COWLEY (Principal): (Pg 23) (on school intercom) Mr. Wiedermeyer. I don’t know how long we can let this situation continue. Mr. Wiedermeyer, can you hear me? Mr. Dunlop, you called the police, didn’t you? GLORIA MESSINGER (Teacher’s Aide): (Pg 20) I tried to collect his attendance. Mr. Wiedermeyer never keeps his door locked. Then I looked down and found this note. I think he’s gone off the deep end. MR. WIEDERMEYER (Note #1): (Pg 21) It starts slowly: A cough here, a cackle there, A dropped book, a pushed chair. Of themselves, separate moments in an ordered universe. But in progression, measured beats to a crescendo of chaos.

He hit me,
He took my pen,
She pushed me . .
Or, I have to go to the bathroom,
I need to see the nurse,
I gotta find my counselor,
I must talk to the coach.
Or, Can I make up the homework?
Can I make up the test?
Can I make up the term?
Yes, my children,
You all did it,
Including you, Michael.
You all did it.
Don’t worry, it’s so quiet now, you can hear an eraser
drop.
They’re giving me their undivided attention.
I couldn’t possibly let them go.
ROGER DUNLOP (Assistant Principal): (Pg 22) Mr.
Wiedermeyer. Who’s Michael?
SHERWOOD COWLEY (Principal): (Pg 26) Thank you for
coming so quickly, gentlemen.

Detectives Balinger and Picardi, is it?
Of course I know him.
Yes, he is hardly ever absent,
Though last year about this time,
He was out for a week, maybe two,
For some personal business, I think.
Yes, more than 20 years, a lifetime of teaching.
Yes, Ms. Messinger, what is it?
Another note?
MR. WIEDERMEYER (Note #2): (Pg 27)
You have been unruly,
And the usual punishments
That are meted out for violation
No longer work.

STUDENT: (Pg 71) Hey, man, you got my freakin’ bus
pass?
What you mean, you don’t have it?
I’m supposed to get it, understand?
I’m not interested in no reasons.
I told you, I want that freakin’ pass.

MR. WIEDERMEYER (Note #2): (Pg 27)
Zeroes,
Phone calls home,
Detention, suspensions,
Can’t shake you out of your
Comas of indifference.
What’s on your minds?

STUDENT: (Pg 71) So go call my mother,
See if I care.
The only think she’s gonna tell you is
How come he didn’t get his freakin’ bus pass?
So where is it?
MR. WIEDERMEYER (Note #2): (Pg 27)
I think I’ll keep you a while longer.
You, too, Michael.
Just to find out.
HARRY BALINGER (Police Captain) (Pg 29)
You read the headlines
That are forgotten the next day:
“Student Goes Berserk in Dorm”
“Teen Kills Teen for Bicycle”
“Mother’s Boyfriend Drowns Tot”

Private tortures
Ending in public spectacle.
Serpentine demons
Strangling common sense.
Mr. Wiedermeyer,
What set you off?
What memories were triggered,
What words were said
That pushed you over the edge?
KATHLEEN GENNARO (Student): (Pg 76)
You can’t tell me what to do.
You can’t push me around.
I’m gonna sit where I want.
JUSTIN SINGLEBERRY (Student): (Pg 139)
(raising his hand) Mr. Wiedermeyer,
Let us out of here, please.
I have an appointment.
MR. WIEDERMEYER (Note #1): (Pg 21)
I have to go to the bathroom,
I need to see the nurse,
(Note #7) (Pg 145) I speak.
Who listens?

I teach.
Who cares.
Term after term after term.
There is little I can do to turn the tide.
There is little I have done to make a difference.
VINNIE DELVECCHIO (Parent): (Pg 160) What does he
have to complain about?
Do I get the summers off?
Do I get out at three?
As I cash my unemployment check . . .
Tell me, what does he have to complain about?
What other job is so respected?
FRANK PICARDI (Emergency Unit): (Pg 161) He mentioned
a Michael – who’s that?

HARRY BALINGER (Police Captain): Someone in his class?
I’m not sure (sound of a gunshot)
EDDIE KELLERMAN (Student): (Pg 155)
My God, he’s gonna kill us.
He’s gonna kill us all.
FRANK PICARDI (Emergency Unit): (Pg 161) What was
that? Sounded like a gunshot?

HARRY BALINGER (Police Captain): Hold your fire, I
repeat, hold your fire. If we rush in now, he might kill
everyone.
MR. WIEDERMEYER (Note #8): (Pg 162)
An accident, repeat, an accident.
I’m not too familiar with guns,
Not like Michael –
I was just practicing loading and unloading
When it went off.
All the students are fine.
No one got hurt, but
I do believe some of the student ar thirsty.
Do you think you could send a student with some
water?
I was just loading and unloading the gun.
I was deciding whether the bullet was for me
Or someone else.
I really need a few more minutes to make up my
mind . . .
HARRY BALINGER (Police Captain): (Pg 163)
That’s it, that’s our in,
I want a Nike-wearing,
Walkman-hearing,
Slang-talking,
Pistol-packin’,
Baby-faced cop.
Who can recognize both
The goodness of a man’s heart and
The darkness of his soul,
And quickly decide
Whether to talk to the guy
Or take him out
We got anybody like that?
JAMES SANCHEZ (Police Officer): (Pg 167)

(speaks to audience as he re-enacts)
He was at his desk when I entered,
Lecturing frozen-in-headlights students
On some provisions of the Constitution.

MR. WIEDERMEYER: (with gun pointed at a student) Michael, can you answer that?

JAMES SANCHEZ (Police Officer): No Michael, they all
knew –
I saw the gun in his hand,
Pointed first at the class, then at his head.

MR. WIEDERMEYER: (with gun pointed at the officer) What is your name?

JAMES SANCHEZ (Police Officer): A crazy thought – (to Mr. Wiedermeyer) Michael. . .

MR. WIEDERMEYER: (motioning with the gun) Michael? How wonderful you look. Come here, my boy.

JAMES SANCHEZ (Police Officer): He pointed his gun at
me. (to Mr. Wiedermeyer, gently)
Got a present for you, Pop. Here in my bag . . .
I quickly pulled out my service revolver
And (gunshot) . . . shot him in the shoulder.
PATTI BENNETT (Student): (Pg 169) He was gonna kill us.
I swear he was gonna kill us.
ANDREW CURRAN (Student): (Pg 171)
Why didn’t I do anything?
I was so close to the man.
I could’ve knocked the gun away.
I did nothing --
Yeah, I know nobody did anything.
That doesn’t help me.

COSMO GENNARO (Parent): (Pg 178)
I’m glad the bastard’s been shot.
He got what he deserved.
Nobody cares what happens in there,
As long as the kids are off the streets.
My own daughter who got locked up with that maniac
Ain’t learnin’ nothin’ she can use.
How did they let that man
Become a teacher in the first place?
Don’t they screen out wackos?
I’m glad the bastard’s been shot.
He got what he deserved.
FRANK PICARDI (Emergency Unit): (Pg 179)
I want to show you what we just found
In Wiedermeyer’s locker:
A poem and a newspaper clipping
Dated about a year ago.

NEWSPAPER CLIPPING: (Pg 181) Police divers recovered the body of a local man, Michel Wiedermeyer, 27, who earlier had braved the rough water, ignoring repeated attempts by people onshore to call him back.

EYEWITNESS: He must have been trying to kill himself.

NEWSPAPER CLIPPING: An autopsy will be performed. Police officials refuse to speculate on whether this was a suicide or a tragic accident. Mr. Wiedermeyer’s parents are enroute to claim their son’s body.

BYSTANDER: No parent should outlive his child. You never recover from that.

MR. WEIDERMEYER: (Pg 180) (Poem entitled For Michael)
Somewhere before the end,
Somewhere between childhood and adulthood,
I lost you.
Somewhere between your first word and last work,
I did not hear you.
For other children I taught my subject.
Some listened,
Most didn’t.
What did I teach them, give them?
What did I teach you, give you?
Oh, Michael,
I should have taught you how to save yourself.
I gave you everything I had.
It wasn’t nearly enough.

HARRY BALINGER (Police Captain): (Pg 182)
You read the headlines in the newspaper,
The headlines that will be forgotten by tomorrow:
“Teacher Goes Beserk; Holds Class Hostage; Shot
Down by Police; Children Safe, but Shaken.”
Private tortures
Ending in public spectacle
Serpentine demons
Strangling common sense.
Mr. Wiedermeyer,
I realize the pain you went through,
To a degree.
Yet, if I were one of the students,
EDDIE KELLERMAN (Student): (Pg 155)
My God, he’s gonna kill us.
He’s gonna kill us all.
HARRY BALINGER (Police Captain): (Pg 182)
I’d never forgive.
If I were the judge, I’d never let you out.
But, if I were your friend,
I’d say to you in your cell,
Think of the good days
When you were younger and Michael was alive
And the world was bright with promise.
Go in soft peace, Mr. Wiedermeyer,
Go in soft peace . . .
```

---

## IC-1708: A Tale of Starvation

- Title: A Tale of Starvation
- Author (byline): Amy Lowell
- Work: Sword Blades and Poppy Seed
- Publisher: BiblioLife
- Publication date as stated: Jan 2009
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1091
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amy Lowell
Book: Sword Blades and Poppy Seed
ISBN: 978-1103029273
Publisher: BiblioLife
Date (Month/Year): Jan 2009
```

### Introduction (context only: never use it for content warnings)

```text
The reason still puzzles me, but we humans have a tendency to focus on the negative in events, circumstances, and people. We have a tendency to count our misfortunes and all the things that are lacking before we count our blessings. This poem by Amy Lowell illustrates just such an outlook on life and how uncovering one bit of beauty in the world can transform a person. Truly, we starve for beauty in life, but in realizing the beautiful, we can feed our soul. Our whole perspective can change. A Tale of Starvation by Amy Lowell.
```

### Performance text (classify this)

```text
There once was a man whom the gods didn't love, And a disagreeable man was he. He loathed his neighbours, and his neighbours hated him, And he cursed eternally.

He damned the sun, and he damned the stars,
And he blasted the winds in the sky.
He sent to Hell every green, growing thing,
And he raved at the birds as they fly.

His oaths were many, and his range was wide,
He swore in fancy ways;
But his meaning was plain: that no created thing
Was other than a hurt to his gaze.

He dwelt all alone, underneath a leaning hill,
And windows toward the hill there were none,
And on the other side they were white-washed thick,
To keep out every spark of the sun.

When he went to market he walked all the way
Blaspheming at the path he trod.
He cursed at those he bought of, and swore at those he
sold to,
By all the names he knew of God.

For his heart was soured in his weary old hide,
And his hopes had curdled in his breast.
His friend had been untrue, and his love had thrown him
over
For the chinking money-bags she liked best.

The rats had devoured the contents of his grain-bin, The deer had trampled on his corn, His brook had shrivelled in a summer drought, And his sheep had died unshorn.

His hens wouldn't lay, and his cow broke loose, And his old horse perished of a colic. In the loft his wheat-bags were nibbled into holes By little, glutton mice on a frolic.

So he slowly lost all he ever had,
And the blood in his body dried.
Shrunken and mean he still lived on,
And cursed that future which had lied.

One day he was digging, a spade or two,
As his aching back could lift,
When he saw something glisten at the bottom of the
trench,
And to get it out he made great shift.

So he dug, and he delved, with care and pain,
And the veins in his forehead stood taut.
At the end of an hour, when every bone cracked,
He gathered up what he had sought.

A dim old vase of crusted glass,
Prismed while it lay buried deep.
Shifting reds and greens, like a pigeon's neck,
At the touch of the sun began to leap.

It was dull in the tree-shade, but glowing in the light; Flashing like an opal-stone, Carved into a flagon; and the colours glanced and ran, Where at first there had seemed to be none.

It had handles on each side to bear it up,
And a belly for the gurgling wine.
Its neck was slender, and its mouth was wide,
And its lip was curled and fine.

The old man saw it in the sun's bright stare
And the colours started up through the crust,
And he who had cursed at the yellow sun
Held the flask to it and wiped away the dust.

And he bore the flask to the brightest spot, Where the shadow of the hill fell clear; And he turned the flask, and he looked at the flask, And the sun shone without his sneer.

Then he carried it home, and put it on a shelf,
But it was only grey in the gloom.
So he fetched a pail, and a bit of cloth,
And he went outside with a broom.

And he washed his windows just to let the sun
Lie upon his new-found vase;
And when evening came, he moved it down
And put it on a table near the place
Where a candle fluttered in a draught from the door.
The old man forgot to swear,
Watching its shadow grown a mammoth size,
Dancing in the kitchen there.

He forgot to revile the sun next morning
When he found his vase afire in its light.
And he carried it out of the house that day,
And kept it close beside him until night.

And so it happened from day to day.
The old man fed his life
On the beauty of his vase, on its perfect shape.
And his soul forgot its former strife.

And the village-folk came and begged to see
The flagon which was dug from the ground.
And the old man never thought of an oath, in his joy
At showing what he had found.

One day the master of the village school
Passed him as he stooped at toil,
Hoeing for a bean-row, and at his side
Was the vase, on the turned-up soil.

"My friend," said the schoolmaster, pompous and kind,
"That's a valuable thing you have there,
But it might get broken out of doors,
It should meet with the utmost care.

What are you doing with it out here?"
"Why, Sir," said the poor old man,
"I like to have it about, do you see?
To be with it all I can."

"You will smash it," said the schoolmaster, sternly right,
"Mark my words and see!"
And he walked away, while the old man looked
At his treasure despondingly.

Then he smiled to himself, for it was his!
He had toiled for it, and now he cared.
Yes! loved its shape, and its subtle, swift hues,
Which his own hard work had bared.

He would carry it round with him everywhere, As it gave him joy to do. A fragile vase should not stand in a bean-row! Who would dare to say so? Who?

Then his heart was rested, and his fears gave way, And he bent to his hoe again. . . . A clod rolled down, and his foot slipped back, And he lurched with a cry of pain.

For the blade of the hoe crashed into glass, And the vase fell to iridescent shards. The old man's body heaved with slow, dry sobs. He did not curse, he had no words.

He gathered the fragments, one by one,
And his fingers were cut and torn.
Then he made a hole in the very place
Whence the beautiful vase had been borne.

He covered the hole, and he patted it down, Then he hobbled to his house and shut the door. He tore up his coat and nailed it at the windows That no beam of light should cross the floor.

He sat down in front of the empty hearth, And he neither ate nor drank. In three days they found him, dead and cold, And they said: "What a queer old crank!"
```

---

## IC-1709: Tales from a Child of the Enemy: Words and The Master Race

- Title: Tales from a Child of the Enemy: Words and The Master Race
- Author (byline): Ursula Duba
- Work: Tales from a Child of the Enemy
- Publisher: Penguin Group
- Publication date as stated: April 1997
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1319
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ursula Duba
Book: Tales from a Child of the Enemy
ISBN: 978-0140587876
Publisher: Penguin Group
Date(Month/Year): April 1997
```

### Introduction (context only: never use it for content warnings)

```text
Ursula Duba is a non-Jewish German born in Germany shortly before the outbreak of WWII. She grew up in postwar Germany knowing nothing about the atrocities committed by her people during the War. Finally at the age of 19 she began to learn the history of Nazi Germany, and was changed forever. These poems are brutally honest in their examination of the prejudices and stereotypes of both the German and Jewish peoples.
```

### Performance text (classify this)

```text
Words
bold letters
on top of the page
declare
this newsletter is dedicated
to all those
who perished
in the Holocaust
the German man,
now living in the USA
is proud of his efforts
to pay homage
to the victims of the Shoah
on the anniversary
of kristallnacht
but i am disturbed
by the word perish
in this dedication -
it conjures up images
of people dying in earth quakes
in a storm out on the open sea
in a hurricane or a tornado -
the word perish
does not tell me
about open ditches
rapidly filling up with the corpses
of innocent men women and children
shot by members of the einsatzgruppen and the
Wehrmacht
it doesn't show me piles of emaciated bodies
deliberately starved to death
it doesn't show me ss guards
using victims for target practice
nor does it display the twisted bodies
of people who died
at the hands of doctors
who performed cruel experiments
in the name of science
there are no gas chambers
crematoria
or perpetrators
weren't Jews Gypsies and non-Aryans
murdered
i ask the German man
yes of course
the victims of the Holocaust
were murdered
he answers
taken aback
by my question
but this word
sounds so aggressive
he says with dismay
after several days
of back and forth
on the telephone
the German man decides to delete the entire sentence
on top of the newsletter
rather than using the word murdered
in his dedication to the victims
of the Shoah
while discussing this
with several friends
we take note
that a lengthy article
in a leading magazine
had recently informed us
that most of the victims
of the massacres in Rwanda
had been hacked to death
by their Hutu neighbours -
no euphemisms there
as to how these victims died
and on discussing the
three million Cambodians
who died in the killing fields -
the language is quite clear -
they were starved to death
or brutally murdered
by the Kmer Rouge
On further probing
no one suggests
that John F. Kennedy and
Martin Luther King perished -
both were assassinated
a few weeks later
i ask a Holocaust survivor
what words would properly describe
the actions by which
six million died
they were exterminated
he says
without hesitation
this word immediately reminds me
of my first months
in an apartment in Brooklyn
and the discovery of cockroaches
in my kitchen cupboards
honey
my next door neighbour
had told me then
look in the yellow pages
under exterminator
recently
i heard Mike Wallace of 60 minutes
refer to all those who were lost
in Auschwitz
the word lost
makes me think
of my fear
of getting lost in foreign cities
on my travels abroad
when even maps
are of limited value
in those countries
which use different alphabets
the word also
calls up images
of thick forests
where hapless travelers
get lost
and i am reminded of
the story of Hansel and Gretel which used to make me
appreciate
the safety of our crammed house
when i was a child
what with the twice a day roll-call
and the meticulous record keeping
of the German and Austrian concentration camp
commanders
the chance of being lost in Auschwitz
or any other concentration camp
were very slim
my friend Dalia
explains to me
whose mother was gassed on the first day
of their arrival in Birkenau.

TRANSITION Adolf Eichmann was the SS leader in charge of masterminding the transportation of Jews from all over Europe to the murder factory at Auschwitz. He was captured at the end of World War II, but managed to escape from an internment camp and disappear. In May 1960 Israeli secret service agents captured him in Argentina and smuggled him to Israel, where his trial attracted worldwide attention. Many Holocaust survivors gave detailed testimony about the horrors of the Nazi death camps. Eichmann was found guilty, sentenced to death, and hanged on May 31, 1962. The Master Race and Words by Ursula Duba from her book Tales from a Child of the Enemy focuses on the emotional issues surrounding the Holocaust and the long term effects on the children of its victims and survivors.

The Master Race
during a brisk walk
along the shoreline
Werner tells me
how devastated he was
when classmates called him
a Nazi
during the Eichmann trial
in their new home in Chicago
to which they had emigrated
in the early fifties
from their home town Bremerhaven
in north Germany he was sixteen at the time of that
trial
had learned English well
since his arrival in 1951
and had been raised
with pride in his heritage
by his Nazi parents
even though their house in Bremerhaven
had turned into rubble
during WWII
two uncles had died
at the Eastern front
and one in captivity in Russia
after the war
and there was nothing left
of the family business
which had supplied
......
to the war effort
his father and mother
looked with pride
on their two sons and two daughters
all of them tall
blond
blue-eyed
and athletic
his father hardened himself
with cold showers
in the morning
endurance was emphasized
and crying not tolerated
all of them were spurred on
to participate in vigorous and competitive sports -
let's show those soft Americans
what we Germans can do
was their father's continuous battle cry
even though his father's pipe dream
of becoming rich in America
and showing off to his impoverished family
back in Germany
was not materializing -
one scheme after another had gone bust
and Werner was ashamed
of their shabby apartment
and the hand-me-down clothes
he had to wear
his parents had no friends
and he and his siblings
were discouraged to bring classmates
back home
because his father was suspicious
of all Americans
even the blond and blue-eyed ones
after all
Americans believed in the melting pot
he told them
you could never know
what inferior genes
were lurking in their bodies an insult to humanity
he used to call this mixing
of people from different countries
and nothing good would come out of it
he declared frequently
don't forget
he used to lecture his children
we are the master race
and far superior to anybody else
he blamed Hitler's defeat
on the Conspiracy of World Jewry
and on all those Germans who had not sufficiently
supported Hitler and The Thousand Year Reich
when he came home
from his menial job
after washing down his schnapps with several beers
he insisted they listen to him
when he told them
about the ancient Nordic gods
who hadn't believed in weakness and mercy
and he instructed them
that only the master race
was entitled to rule the world
and that all others
were destined to do their bidding
and to obey them
during the Eichmann trial
discussed at great length
on television in the newspapers and at school
Werner was horrified
about the atrocities committed by his people
in his country
he joined a peace group in college
broke with his father
became a teacher
and devoted himself to many worthy causes
during the next thirty years
eventually
Werner participated in a training program
to teach hard core criminals
conflict resolution
and now spends most of his free time
in a maximum security prison
I see his eyes light up
when he talks about the bonds
he has formed with those inmates
and hear his pride
in having been able
to help the prisoners learn reading and writing
besides conflict resolution
I am touched by Werner's compassion
and caring
for those prison inmates
but miss the mentioning
of the victims
of the perpetrators
who raped assaulted and committed robberies and
murders
and what do the inmates
think of your work
I ask Werner
the tall blond blue-eyed athletic man
stops his brisk walk
for a moment
and tells me
looking at me with pride and joy
they treat us like gods
```

---

## IC-1710: Television Poetry Program

- Title: Television Poetry Program
- Author (byline): Todd Alcott, Shel Silverstein and Roald Dahl
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1269
- Already set (do not supply): none

### Source block (context only)

```text
Author: Todd Alcott
Book: The Spoken Word Revolution
ISBN: 978-0321328953
Publisher: Longman
Date(Month/Year): 2003
Author: Shel Silverstein
Book: Where the Sidewalk Ends
ISBN: 978-0060586539
Publisher: HarperCollins
Date(Month/Year): January 2004
Author: Roald Dahl
Book: Charlie and the Chocolate Factory
ISBN: 978-0140328691
Publisher: Puffin
Date(Month/Year): October 1, 1998
```

### Introduction (context only: never use it for content warnings)

```text
You invite him/her in and he insists on staying for dinner. After telling off-color jokes to your family, he/she shamelessly flirts with your spouse as he/she starts a sales pitch. You tell yourself that you will insist he/she show some of his/her better qualities on hi/hers next visit. His/Her name? Television. And while h/she may indeed have some redeeming characteristics, you might want to ponder your relationship with this compelling little device. A Television Poetry Program by Todd Alcott, Shel Silverstein and Roald
```

### Performance text (classify this)

```text
Look at me. Look at me. Look at me, look at me. Look at me. Look at me. No no no, don't look over there, there's nothing over there, look at me, look at me, look at me. Are you looking at me? Is everybody looking at me? Do I have your attention? Good.

Dahl.

TELEVISION Don't get me the wrong idea. I'm not trying to take over your life. You need, what? What do you need? You need to, what? Go to the bathroom? Fine. Get up, go to the bathroom, come back look at me. You need, what? You need to get something to eat? Fine. Get up, go to the kitchen, get something to eat, come back, look at me. You need to, what, sleep? Fine, get up, go to bed, go to sleep, get up, come back look at me. Okay. So we have an agreement. You will do what you absolutely need to do, and when you're done, you will come back and look at me. Don't worry about your schedule. I am here for you. I am here for you. Twenty-four hours a day, seven days a week, I am here for you. I am here for you. You need me, I'm here. Fair and foul, thick and thin, I am here for you. I am here for you. People try to tell you I'm bad? You tell them that I am here for you.

Twenty-four hours a day, fair and foul, thick
and thin, I am here for you. I am here for you.
People try to tell you I'm bad, know what it
sounds like to me? Sour grapes.
You see what I - hey, hey, hey, hey, hey no, don't
look over there, there's nothing going on over
there, look at me, look at me, look at me.
I've got stuff you wouldn't believe. Danger? !@#$%^&?
Action? Death? Thrills? Comedy? All here, all
in the next eight minutes.
Can you believe it? You can't. It's unbelievable.
You can't believe it because it's unbelievable.
It's a miracle.
Just keep looking at me. Just keep looking at me.
Just keep looking at me. Look at me, look at
me, look at me, look at me, look at me

TRANSITION Every year in April, an initiative (only somewhat successfully) sweeps the Nation: National TV-Turnoff Week! This annual event aims to give back what TV often takes away: our productivity, creativity, health, inter-personal relating, civic engagement, spiritual gift development and moral decency. In fact, studies have found that the average American child watches 1,197 minutes of TV each week while the average parent spends 38 minutes a week with their child in meaningful conversation. Something must be done . . . or our children may face the same fate as Jimmy Jet by Shel Silverstein.

Jimmy Jet and His TV Set

I'll tell you the story of Jimmy Jet --
And you know what I tell you is true.
He loved to watch his TV set
Almost as much as you.
He watched all day, he watched all night
Till he grew pale and lean,
From "The Early Show" to "The Late Late Show"
And all the shows between.
He watched till his eyes were frozen wide,
And his bottom grew into his chair.
And his chin turned into a tuning dial,
And antennae grew out of his hair.
And his brains turned into TV tubes,
And his face to a TV screen.
And two knobs saying "VERT." and "HORIZ."
Grew where his ears had been.
And he grew a plug that looked like a tail
So we plugged in little Jim.
And now instead of him watching TV
We all sit around and watch him.

TRANSITION Mike Teavee, a character in the Roald Dahl’s book Charlie and the Chocolate Factory is particularly obsessed with television. He likes to act out gangster shootings and becomes very angry if anyone stops him from watching TV, his parents included. Sound familiar. Child psychologists repeatedly warn our society of the perils of too much TV – warnings that often fall on deaf ears. Perhaps the message would be better accepted if delivered via Oompa Loompa. Their words of wisdom from 1964 still ring true today! Oompa Loompa Doompa De Do – I’ve got final message for you . .

Television

The most important thing we've learned,
So far as children are concerned,
Is never, NEVER, NEVER let
Them near your television set --
Or better still, just don't install
The idiotic thing at all.
In almost every house we've been,
We've watched them gaping at the screen.
They loll and slop and lounge about,
And stare until their eyes pop out.

(Last week in someone's place we saw
A dozen eyeballs on the floor.)
They sit and stare and stare and sit
Until they're hypnotised by it,
Until they're absolutely drunk
With all that shocking ghastly junk.
Oh yes, we know it keeps them still,
They don't climb out the window sill,
They never fight or kick or punch,
They leave you free to cook the lunch
And wash the dishes in the sink --
But did you ever stop to think,
To wonder just exactly what
This does to your beloved tot?
IT ROTS THE SENSE IN THE HEAD!
IT KILLS IMAGINATION DEAD!
IT CLOGS AND CLUTTERS UP THE MIND!
IT MAKES A CHILD SO DULL AND BLIND
HE CAN NO LONGER UNDERSTAND
A FANTASY, A FAIRYLAND!
HIS BRAIN BECOMES AS SOFT AS CHEESE!

HIS POWERS OF THINKING RUST AND FREEZE!
HE CANNOT THINK -- HE ONLY SEES!
'All right!' you'll cry. 'All right!' you'll say,
'But if we take the set away,
What shall we do to entertain
Our darling children? Please explain!'
We'll answer this by asking you,
'What used the darling ones to do?
'How used they keep themselves contented
Before this monster was invented?'
Have you forgotten? Don't you know?
We'll say it very loud and slow:
THEY ... USED ... TO ... READ! They'd READ and READ,
AND READ and READ, and then proceed
To READ some more. Great Scott! Gadzooks!
One half their lives was reading books!
The nursery shelves held books galore!
Books cluttered up the nursery floor!
And in the bedroom, by the bed,
More books were waiting to be read!
Such wondrous, fine, fantastic tales
Of dragons, gypsies, queens, and whales
And treasure isles, and distant shores
Where smugglers rowed with muffled oars,
And pirates wearing purple pants,
And sailing ships and elephants,
And cannibals crouching 'round the pot,
Stirring away at something hot.
(It smells so good, what can it be?
Good gracious, it's Penelope.)
The younger ones had Beatrix Potter
With Mr. Tod, the dirty rotter,
And Squirrel Nutkin, Pigling Bland,
And Mrs. Tiggy-Winkle and-
Just How The Camel Got His Hump,
And How the Monkey Lost His Rump,
And Mr. Toad, and bless my soul,
There's Mr. Rate and Mr. Mole-
Oh, books, what books they used to know,
Those children living long ago!
So please, oh please, we beg, we pray,
Go throw your TV set away,
And in its place you can install
A lovely bookshelf on the wall.
Then fill the shelves with lots of books,
Ignoring all the dirty looks,
The screams and yells, the bites and kicks,
And children hitting you with sticks-
Fear not, because we promise you
That, in about a week or two
Of having nothing else to do,
They'll now begin to feel the need
Of having something to read.
And once they start -- oh boy, oh boy!
You watch the slowly growing joy
That fills their hearts. They'll grow so keen
They'll wonder what they'd ever seen
In that ridiculous machine,
That nauseating, foul, unclean,
Repulsive television screen!
And later, each and every kid
Will love you more for what you did.
```

---

## IC-1711: Ten Patients, and Another

- Title: Ten Patients, and Another
- Author (byline): Rafael Campo
- Work: What the Body Told, Pg 61-71
- Publisher: Duke University Press Books
- Publication date as stated: Feb 1996
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: VIII
- Teaser before the introduction: Yes
- Spoken words (computed): 1197
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rafael Campo
Book: What the Body Told, Pg 61-71
ISBN: 978-0822317425
Publisher: Duke University Press Books
Date (Month/Year): Feb 1996
```

### Introduction (context only: never use it for content warnings)

```text
Medicine is about providing care to people. Yes, the core of medical education is science — anatomy, physiology, pathology. Yet patient care is more than just the memorization of facts and figures; it requires empathy, it requires the doctor to feel. They must remember that behind every “patient” lies a real human being — a mother, father, son, daughter, friend. Only when one looks beyond the patient and sees the person can physicians truly make a difference.

Ten Patients, and Another by Raphael Campo tackles the intersection of social and medical issues, addressing topics of alcoholism, child, sexual and drug abuse, domestic violence, AIDS, racial prejudice, homelessness, and homophobia. Doctors, while medically trained, often are ill-prepared to cope with the social issues they face. We must do better.
```

### Performance text (classify this)

```text
NOTE: Each stanza should be presented in a different persona (all stanzas are spoken by doctors or medical personnel within a hospital setting. Stanza VIII may be a phone conversation – Be creative in developing the characters)

I. Mrs. G (Pg 61-71)
The patient is a sixty-odd-year-old
White female, who presents with fever, cough,
And shaking chills. No further history
Could be elicited; she doesn’t speak.
The patient’s social history was non-
Contributory: someone left her here.
The intern found a bruise behind her ear.
She then became quite agitated, and
Began to sob without producing tears.
She’s resting quietly
On Haldol, waiting for a bed upstairs.

II. Jamal
The patient is a three-year-old black male,
The full-term product of a pregnancy
That was, according to his grandmother,
Unplanned and maybe complicated by
Prenatal alcohol exposure. Did
OK, developmentally delayed
But normal weights and heights, until last week
When he ingested what's turned out to be
Cocaine, according to the lab results;
His grandmother had seen him with
Some baby powder on his face and hands
Before he started seizing.
The nurse is getting DSS involved.
The mom? She left it on the kitchen table.
That's her -- the one who sings to him all night.

III. HK
The patient is a twenty-nine-year-old
Black man.
Upon returning from his shift – the patient is
A night nurse at a local hospital --
He was attacked by two assailants. Males,
White, late teens, shouting threats and epithets.
He thinks they followed him from work. He turned,
Attempting to respond, when he was struck
With two blunt objects in succession. One
Was glass; we know because some fragments were
Extracted from the wounds.
The surgeons didn’t want to operate
Until they had more information. CT scans
Revealed free blood inside the abdomen.
What’s scary is he isn’t even gay.

IV. Kelly
The patient is a twelve-year-old white female.
She's gravida zero*, no STD's.
She'd never even had a pelvic. One
Month nausea and vomiting.
No fever, chills, malaise.
Her school performance has been worsening.
She states that things at home are fine.
On physical exam, she cried but was
Cooperative.
Her pelvic was remarkable for scars
At six o'clock, no hymen visible,
Some uterine enlargement. Pregnancy
Tests positive times two. She says it was
Her dad. He's sitting in the waiting room.
*No previous pregnancies
V. John Doe
An elderly white male, unresponsive.
Looks homeless. Maybe he’s been here before.
No chart. No history. His vital signs
Were barely present, temperature was down
Near ninety, pressure ninety over palp;
The pulse was forty, best as they could tell.
They’ll hook him up to a monitor before
They warm him up. I didn’t listen to
His lungs—I bet I’d hear a symphony
In there. I couldn’t check his pupils since
His lids were frozen shut, but there were no
External signs of trauma to the head.
They found this picture of a woman with
Two tiny kids still pinned inside his coat.
It’s only three a.m. The night’s young. If
He’s lucky, by tomorrow he’ll be dead.

VI. S.W. Extending from her left ear down her jaw, The lac was seven centimeters long. She told me that she slipped and struck her face Against the kitchen floor. The floor was wet Because she had been mopping it. I guessed She’d had to wait for many hours since The clock read nearly midnight; who mops floors So late? Her little girl kept screaming in Her husband’s thick, impatient arms: he knocked Three times, each time to ask when we’d be done. I infiltrated first with lidocaine. She barely winced, and didn’t start to cry Until the sixteenth stitch went in and we Were almost through. I thought my handiwork Was admirable. I yawned, then offered her Instructions on the care of wounds. She left.

VII. Manuel
In Trauma 1, a gay Latino kid –
I think he’s seventeen – is getting tubed
For respiratory failure. “Sleeping pills
And Tylenol,” I translated for him
As he was wheeled in. His novio (boyfriend)
Explained that when he’d told his folks about
It all, they threw him out. Like trash. They lived
Together underneath the overpass
Of Highway 101 for seven weeks,
The stars obstructed from their view.
A viejita (old woman) from the neighborhood
Brought tacos to them secretly. Last night,
With eighteen-wheelers roaring overhead,
He whispered that he’d lost the will to live.
He pawned his crucifix to get the pills.

VIII: PP
Another Aids Admission. This one’s great:
They bring him in strapped down because he threw
His own infected s*** at them – you better bring
Your goggles! – and a mask, we think he’s got
TB. He’s pissed as hell. Apparently,
He wants to die at home but somebody
Keeps calling 911. A relative
Back home in Iowa, or some damn place.
Just keep him snowed with Ativan – believe
You me – you do not want to get to know
This *guy*. Kaposi’s* all over, stinks –
Incontinent of course. How long
Before you get down here? Because his nurse
Is driving me insane. Of course, we got
Blood cultures . . . yeah, a gas – OK, I’ll stick
him one more time. The things you do for love.
* Kaposi's sarcoma (KS) is a type of cancer that can form
masses in the skin

IX. Tommy
A twenty-one-year-old white man brought in
By ambulance – in hypotensive shock,
Shot in the back while buying drugs from three
Black men. The cord must be involved:
His legs are paralyzed,
And all sensation from below
The level of the entry site is lost.
They left him in the street for dead; I heard
Them say an alley dog was lapping up
His blook like milk when he was found. Before
He goes to surgery, he has to give
Informed consent, which he’s refused to do
Thus far. He states he’d rather die than be
Dependent on his family for care.
They’re questioning his competence, of course.
They’re waiting on his folks. His wife just stares.

X. Maria This *patient* gives us a confusing History. It sounds like she’s been pregnant Approximately thirty weeks, although She can’t recall her last LMP*. No pain, But bleeding for about two days. Of course She hasn’t had prenatal care, and God Only knows where the father is. She works Two jobs that keep her on her feet all day. She’s been in the United States six months, And doesn’t speak a word of English. Bet You she’s illegal. I think we need an ultrasound to tell us more. Her uterus can tell us more than she can. *Last Menstrual Period

XI. Jane Doe #2
They found her unresponsive in the street
Beneath a lamplight I imagined made
Her seem angelic, regal even, clean.
She must have been around sixteen. She died
Who knows how many hours earlier
That day, the heroin inside her like
A vengeful dream about to be fulfilled.
Her hands were crossed about her chest, as though
Raised up in self-defense; I tried to pry
Them open to confirm the absence of
A heartbeat, but in death she was so strong,
As resolute as she was beautiful.
I traced the track marks on her arms instead,
Then pressed my thumb against her bloodless lips,
So urgent was my need to know. I felt
The quiet left by a departing soul.
```

---

## IC-1712: Ten Thousand Stories – A Collection

- Title: Ten Thousand Stories – A Collection
- Author (byline): Margaret Walker, Amanda
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 933
- Already set (do not supply): none

### Source block (context only)

```text
Author: Margaret Walker
Book: This is My Century: New and Collected Poems,
Pg 6-7
ISBN: 978-0820345970
Publisher: University of Georgis Press
Date (Month/Year): Oct 2013
Also available on-line at:
https://poets.org/poem/my-people
Author: Amanda Gorman
ISBN: On-line Transcript
https://www.newsweek.com/read-amanda-gorman-new-
years-poem-new-days-lyric-full-1664343
Publisher: Newsweek.com
Date (Month/Year): Dec 30, 2021
Author: Lebohang Masango
ISBN: On-line Transcript
https://lebohangmasango.com/2021/05/21/ten-thousand-
stories/
Publisher: Published by the Author
Date (Month/Year): May 21, 2021
Video can be viewed here:
https://www.youtube.com/watch?v=UxFymU4R31U
```

### Introduction (context only: never use it for content warnings)

```text
Margaret Walker wrote the poem, “For My People,” in 1937 – almost 100 years ago. She addresses the history of African American slavery; the racism endured by people of color and the hope for a better future her people, my people manage to keep alive despite the odds stacked against them. You see, even then . . . stories mattered.

History is a story; culture is a story – stories told by many different people from many different perspectives. Listen . . . there is always a story. Stories that engage, inspire, heal and, just perhaps, bring humanity together to forge a better future. Stories are what we remember.

Ten Thousand Stories – A Collection containing For My People by Margaret Walker, New Day’s Lyric by Amanda Gorman and Ten Thousand Stories by Lebohang Masango
```

### Performance text (classify this)

```text
Gorman and Lebohang Masango

For My People by Margaret Walker

For my people everywhere singing their slave songs repeatedly: their dirges and their ditties and their blues and jubilees, praying their prayers nightly to an unknown god, bending their knees humbly to an unseen power;

For my people lending their strength to the years, to the gone years and the now years and the maybe years, washing ironing cooking scrubbing sewing mending hoeing plowing digging planting pruning patching dragging along never gaining never reaping never knowing and never understanding . . .

For the cramped bewildered years we went to school to learn to know the reasons why and the answers to and the people who and the places where and the days when, in memory of the bitter hours when we discovered we were black and poor and small and different and nobody cared and nobody wondered and nobody understood;

For the boys and girls who grew in spite of these things to be man and woman, to laugh and dance and sing and play and drink their wine and religion and success, to marry their playmates and bear children and then die of consumption and anemia and lynching;

For my people thronging 47th Street in Chicago and Lenox Avenue in New York and Rampart Street in New Orleans, lost disinherited dispossessed and happy people filling the cabarets and taverns and other people’s pockets needing bread and shoes and milk and land and money and something—something all our own;

For my people standing staring trying to fashion a better way from confusion, from hypocrisy and misunderstanding, trying to fashion a world that will hold all the people, all the faces, all the adams and eves and their countless generations;

Let a new earth rise. Let another world be born , , , Let a second generation full of courage issue forth; let a people loving freedom come to growth. Let a beauty full of healing and a strength of final clenching be the pulsing in our spirits and our blood. Let the martial songs be written, let the dirges disappear. . . [For this is a]

This poem only, paired with

I Hear a Rumbling by Margaret Walker

New Day’s Lyric by Amanda Gorman
May this be the day
We come together.
Mourning, we come to mend,
Withered, we come to weather,
Torn, we come to tend,
Battered, we come to better.
Tethered by this year of yearning,
We are learning
That though we weren't ready for this,
We have been readied by it.

We steadily vow that no matter
How we are weighed down,
We must always pave a way forward.
*
This hope is our door, our portal.
Even if we never get back to normal,
Someday we can venture beyond it,
To leave the known and take the first steps.
So let us not return to what was normal,
But reach toward what is next.
*
What was cursed, we will cure.
What was plagued, we will prove pure.
Where we tend to argue, we will try to agree,
Those fortunes we forswore, now the future we foresee,
Where we weren't aware, we're now awake;
Those moments we missed
Are now these moments we make,
The moments we meet,
And our hearts, once all together beaten,
Now all together beat.
*
Come, look up with kindness yet,
For even solace can be sourced from sorrow.
We remember, not just for the sake of yesterday,
But to take on tomorrow.
*
We heed this old spirit,
In a new day's lyric,
In our hearts, we hear it:
For auld lang syne, my dear,
For auld lang syne.
Be bold, sang Time this year,
Be bold, sang Time,
For when you honor yesterday,
Tomorrow ye will find.
Know what we've fought
Need not be forgot nor for none.
It defines us, binds us as one,
Come over, join this day just begun.
For wherever we come together,
We will forever overcome.
[Because]

Ten Thousand Stories by Lebohang Masango

I come as one, but I stand as 10 000 stories
10 000 journeys of
Flesh, heartbeat, voice, breath
Bloodlines running like rivers wild
Vessels of DNA criss-crossing this continent
As I stand firmly in the soil of my origin
I carry the hopes of Africa in my chest
And our defiant elders in my lungs
And we have always lived with our hearts towards the sky
We, phoenix-like rise, to new heights
Cradling the aspirations and dreams
Of our beautiful children
The visions of every little one
With imaginations as precious
And as agile as rain
Cradling waves of our narrative lineages
From the beginning to the present
Our stories are embellished on the great wings
Of tomorrow
So, when I speak, I do so as one, but I come as many
Because conjuring purpose and passion from pain
Has always been our people’s true alchemy
When we are all gone
These testaments will remain
The future ones will know us by our works of heart;
Our living art
Time will stand tall and bear witness to us in all
Our glory
Our beginning, middle and end
Is commanded by a spirit greater than anything
We have ever known
So, tell your story
Shout it from the rooftops
To the mountaintops
Let it reverberate through the universe
Take up space in places you have never been
Occupy new worlds
Stare down the sky and let them know that you
intend to leave this world as you came. . .
A collective kind of unconquerable
We come as one, but we stand as 10,000 stories
10 000 journeys of
Flesh
Heartbeat
Voice
Breath
```

---

## IC-1713: That Which We Take for Granted

- Title: That Which We Take for Granted
- Author (byline): Joy Harjo, Robert Wrigley, Elise
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 872
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joy Harjo
Book: Conflict Resolution for Holy Beings, Pg 14-15
ISBN: 978-0393353631
Publisher: W.W. Norton and Company
Date (Month/Year): January 2017
Author: Robert Wrigley
Book: Poetry Magazine, Vol. 162, No. 1, Pg 33-34
ISBN: Currently out of Print
Publisher: Poetry Foundation
Date (Month/Year): April 1993
NOTE: JSTOR and the Poetry Foundation have
collaborated to digitize, preserve, and extend access to
Poetry Magazine – Poem can be found on-line at
https://www.poetryfoundation.org/poetrymagazine/browse?
contentId=38610
Author: Elise Paschen
Book: The Nightlife: Poems
ISBN: 978-1597090278
Publisher: Red Hen Press
Date (Month/Year): May 2017
Author: Charlotte Mew
Book: Collected Poems and Prose, Pg 52
ISBN: 978-0415967570
Publisher: Routledge
Date (Month/Year): March 2003
```

### Introduction (context only: never use it for content warnings)

```text
Water, animal life, trees . . . Our native American ancestors recognized the value of nature. When did we, as a society, start taking our natural world for granted? The statistics are staggering. The US Environmental Protection Agency reports that Americans dump 16 tons of sewage into our waterways every minute. And according to the World Resources Institute, 100 animal species die each day due to deforestation.

Nature is all around us, yet we have become so intent on fighting each other that we seem to have forgotten the very planet that sustains us. Albert Einstein once said: “There are only two ways to live your life. One is as if nothing is a miracle. The other is as if everything is a miracle.”

That Which We Take for Granted – A collection containing Once the World was Perfect by Joy Harjo, Little Deaths by Robert Wrigley, The Tree Agreement by Elise Paschen and The Trees are Down by Charlotte Mew.
```

### Performance text (classify this)

```text
Paschen and Charlotte Mew

Once the World Was Perfect by Joy Harjo

Once the world was perfect, and we were happy in that

world.
Then we took it for granted.
Discontent began a small rumble in the earthly mind.
Then Doubt pushed through with its spiked head.
And once Doubt ruptured the web,
All manner of demon thoughts
Jumped through—
We destroyed the world we had been given
For inspiration, for life—
Each stone of jealousy, each stone
Of fear, greed, envy, and hatred, put out the light.
No one was without a stone in his or her hand.
There we were,
Right back where we had started.
We were bumping into each other
In the dark.
And now we had no place to live, since we didn't know
How to live with each other.
Then one of the stumbling ones took pity on another
And shared a blanket.
A spark of kindness made a light.
The light made an opening in the darkness.
Everyone worked together to make a ladder.
A Wind Clan person climbed out first into the next world,
And then the other clans, the children of those clans, their

children, And their children, all the way through time— To now, into this morning light to you.

Little Deaths by Robert Wrigley

Every minute or two, another moth
blunders through the candle flame – a dusty puff,
then silence. Some fall
half-sealed in wax, others spin
half-charred across the table.
By the handful every hour
I toss them in the stove.

How easy it is to live with
little deaths – mostly bugs,
the less musical birds, the cats
and rabbits we can’t avoid in our cars.

In the woods behind their summer camp
Pentecostal kids crucified frogs
to the trees. Three nails
and a sapling trunk, little fish-belly
amphibious Jesus..
There’s no accounting for this,
though I fear salvation
is an enterprise, grace the bottom line.

Tonight I’m alone at the cabin. There’s no blood on my hands, Now and then one of the candle-seared moths skitters off the table and the dog rouses and noses it until it’s dead.

A few of the livelier ones she’s eaten. Now she sleeps by the stove and sometimes whimpers and seems to run. I should out-live her by years, though I think of her dreams and wonder, whimpering that way, if she is the one who chases.

The Tree Agreement by Elise Paschen

The neighbor calls the Siberian Elm
a “weed” tree, demands we hack
it down, says the leaves overwhelm
his property, the square backyard.

He’s collar-and-tie. A weed tree?
Branches screen buildings, subway tracks,
his patch of yard. We disagree,
claim back the sap, heartwood, wild bark.

He declares the tree “hazardous.”
We shelter under leaf-hoard, crossway
for squirrels, branch house for sparrows, jays.
The balcony soaks up the shade.

Chatter-song drowns out cars below.
Sun branches down. Leaves overwhelm.
The tree will stay. We tell him “no.”
Root deep through pavement, Elm.

The Trees are Down by Charlotte Mew

—and he cried with a loud voice: Hurt not the earth, neither the sea, nor the trees—

(Revelation 7:3 KJV)

They are cutting down the great plane-trees at the end of

the gardens. For days there has been the grate of the saw, the swish of

the branches as they fall, The crash of the trunks, the rustle of trodden leaves, With the ‘Whoops’ and the ‘Whoas,’ the loud common talk,

the loud common laughs of the men, above it all.

I remember one evening of a long past Spring Turning in at a gate, getting out of a cart, and finding a large

dead rat in the mud of the drive. I remember thinking: alive or dead, a rat was a god-

forsaken thing, But at least, in May, that even a rat should be alive.

The week’s work here is as good as done. There is just one

bough

On the roped bole, in the fine grey rain,

Green and high

And lonely against the sky.

(Down now!—)

And but for that,

If an old dead rat Did once, for a moment, unmake the Spring, I might never

have thought of him again.

It is not for a moment the Spring is unmade to-day; These were great trees, it was in them from root to stem: When the men with the ‘Whoops’ and the ‘Whoas’ have

carted the whole of the whispering loveliness away Half the Spring, for me, will have gone with them.

It is going now, and my heart has been struck with the

hearts of the planes; Half my life it has beat with these, in the sun, in the rains,

In the March wind, the May breeze, In the great gales that came over to them across the roofs

from the great seas.

There was only a quiet rain when they were dying;

They must have heard the sparrows flying, And the small creeping creatures in the earth where they

were lying—

But I, all day, I heard an angel crying:

‘Hurt not the trees.’

From Poem #1: [You see] Once the world was perfect, and we were happy in that world. Then we took it for granted.
```

---

## IC-1714: Theophonic

- Title: Theophonic
- Author (byline): Dave Harrity
- Work: Saint Katherine Review, Volume 4, No 1 (pg 24)
- Publisher: Saint Katherine Press
- Publication date as stated: Spring 2014
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1119
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Harrity
Book: Saint Katherine Review, Volume 4, No 1 (pg 24)
ISSN: 2157-1759
Publisher: Saint Katherine Press
Date (Month/Year): Spring 2014
NOTE: The website for Saint Katherine Review can be
found at http://www.stkath.org/#!press-and-review/c1c4b
and the original copy of this literary magazine must be
ordered directly from Saint Katherine College.
Saint Katherine College Press publishes the Saint
Katherine Review, a quarterly literary journal of poetry,
fiction, creative nonfiction, brief non-fiction, and book
reviews. – this journal is published in hard-copy format.
```

### Introduction (context only: never use it for content warnings)

```text
Theophonic – “Theo” – of or relating to god and “phonic” of or relating to speech. So Theophonic is a word that means talking about god. And that’s exactly what this poem does. It talk about the relationship that we each have with god from the moment of our birth to the end of our days. Again and again the concept of fear is raised.

Psalm 56:3-4 says . . . When I am afraid, I put my trust in you. In God, whose word I praise, in God I trust; I shall not be afraid. What can flesh do to me?

Theophonic by Dave Harrity.
```

### Performance text (classify this)

```text
" ... to become as plain as a host

in the hands of everybody."

-Thomas Merton

To come into the world will always mean an imposition - you can't avoid the tangled energy very long before you see it means you must love your neighbor as yourself. Ropes braided and left on the ground,

a sacred circus, ashed
elocution of the mind: a ring
left incomplete. You won't be alive long enough
to see, but there are ways to separate
the ghost from the bone, the pain
from the nerve-

the way the soul
can be recovered from the body's iron. Like
knotted hair balled out from a brush or fingernails
clipped down to the quick:

the vanity
of caring for the shell-pumice stone, dusty filed skin.
* * *
Always in becoming flesh the process
is minute –

cairn worn and smoothed, tumbling

unnoticed.
* * *
The story just as small or simple-banner flecked
with purple stars, a desert sprawl and her
bare shoulders, his beard's wiry denim flush
against her cheeks.

How something came from nothing isn't
quite a miracle as much as attraction itself ringing
us together. And the obligations
buried deep that makes us stay and fall
in love.

And after that it's angels singing
or the small hands in the world. It's another
messiah, peripatetic star, or magus
from another place-and she

was so afraid.
* * *
And all of this isn't so much about god as it is
about how prayer comes
out of us-

and not about the words we say but how we breathe them out, burned into the world. * * * The wheeze of amniotic mess and blood for an entire night-exhausted, piled with the hay and gentle. A nativity you think you know, just more human, less to lose in desert stars: meconium of a resting king. Eyelids bled to crumpled sacks of stones; body branch-bent, frail and final, the gall of crucifixion ragged on the lip. Again, it is the thing you think you know: golgathan clear and crowds lose in the hanging. * * * This present promise of what we will become set back from sin-tower, triptych, dungaree: these things we make

to ascend, exalt, restrain. It's simple as a thorn, a skim of blood. A man carries his cross up the hill, so slight

a miracle compared to what they've seen, if beating bathed the clement ground clean, then it's almost finished:

the bright veil
of new blood ringing in the shape of what
was once a face - cheekbones bowed to
lacerated lips,
the widened ends and holes.

Skin less
defined than realized to be there. A wilted pelt
hung up on nails versus the sculpture
and the size-tower, triptych,

dungaree: the things we make to render names to life; the lives we live to live eternally. And we are so afraid ... * * * What bones there were were there just as our bones are: an absent rib, this crown of thorns. And on before the crowd he looked the same-weathered loincloth, punctured wrists half-wild, pangeaic metatarsals-soft sockets hold the eyes.

This is what makes it time to ask a question and

doubt
the answers that emerge: what sits
inside you on a throne deciding what is
and isn't god? How the body changes
as it goes - and rends the heart a useless
instrument.
* * *
The storm is calmed; the baskets filled.
A canvas glad of god and the name you've made.
To say it freely and finally allowed.

This wafer placed over the canyons of the palm, the way we take the marrow in - the way we then forget again. The cup enameled

to the teeth like we understand the process of the

thing-and the careful bearer spilling less than was ever spilt before. The rail leading back to

knees. There aren't colors enough to write it out in ink, to copy and to copy and to copy and –

bread of life

cup of salvation
-copy. This rail to feed for free. Amen.
We say. Amen. And walk
down remembering,
rivers to a sea.
* * *
How belief must be an edible absolution

and the body less and less afraid how of how it ends. Space possessed by what was now attentive with a fuller silence. The lamplit grains of words we can't pronounce.

And it's true that we should all be more
afraid.
* * *
This crowing morning, this lofted bell –
seeds to fall, a cup to pass from you.

Here's where you can put your fingers: the absence you can enter.

Engulfing griefs that should remember what you have become:

far away and out, waste steaming in the grass

of how the body makes its own waste. This is a vocabulary,

how to sketch in the outlined shadows splintered in the light of glass

or arrayed silhouettes of saints crossing knolls, spiraled iconography.

as the deer begin to munch again,
the cutbank feast in crosses.
* * *
What emerges when we tell ourselves

what we aren't going to become? Or you should know you will

become it,

what you wish you never were.
* * *
As if the clavicle's immediacy is diminished
by the skin,

instead it rises to a gentle hill to bear as this is what we've made.

All of this indefinite precision, interstices

filled up by the rain.

Think of it like this when you think of his hanging: what exactly can you know unless you cut it open?

Bones kissed through skin.

A moment in the desert when a brightness calls us

home, into a cave, into the running blankness of the sand.

What it means to animate is what it means to be

afraid.

These scapes across the small divide and leave the sheep to follow something greater, relax the

gables and the slings.

The walk is never close enough - the bearing left

unknown . . . * * * -and light will guide us home again, or to

another cave. Upright and walking; light into the world: so afraid that we'll be ruled by what we cannot see.

So kings send out their soldiers, and blood comes out as water. And the faithful paint it

on their doors-
but still a generation disappears.
* * *
Always when we know we know in flickering
frames-

dopplered movement unaccountable. Always known by what we're not or want by what we are or wish for what we

cannot have:

a line clipped in elision, forcing it to fit. * * * And it's impossible to know what you are

walking to or from: a cave or a grave. Comforted by light for sake of shadow-flurries

edged and absent in the world, detritus atoned, etched out between the self and

stars. A body wrapped in bands, the crushed

scraps of swaddling clothes. Unwrapped, lilted desert flowers, and you

never know what you're walking to or from.
```

---

## IC-1715: There are Too Many Saviours on My Cross

- Title: There are Too Many Saviours on My Cross
- Author (byline): Richard Harris
- Work: Not specified
- Publisher: Columbia
- Publication date as stated: 1973
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 591
- Already set (do not supply): none

### Source block (context only)

```text
Author: Richard Harris
Audio Format: Richard Harris: His Greatest
Performances
ISBN: N/A
Publisher: Columbia
Date (Month/Year): 1973
```

### Introduction (context only: never use it for content warnings)

```text
Realism, rather than romanticism, is an essential element in Christian judgment. Nowhere is this more true than in Northern Ireland, where a lethal mixture of nationalism, culture, religion and politics has been fermenting for nearly four centuries. Although its geography suggests that Ireland should be unified, there is not the remotest possibility of this happening within the foreseeable future..

Richard Harris spoke out quite frequently on his frustrations with the religious conflicts in Northern Ireland, which have spawned so much hatred and taken so many lives in the apparent name of religious differences. Like all great literature though, his poem There are Too Many Savior on My Cross rings true in a much broader context. The pain of decades, centuries of war over whose God is right comes so clearly through his words. And yet, we humans continue to war over God and whose side he is on... It must make God weep to see what is done in his name... There are Too Many Saviors on my Cross by Richard Harris.
```

### Performance text (classify this)

```text
There are too many Saviours on my cross, Lending their blood to flood out my ballot box With deeds of their own. Who put you there? Who told you that, that was your place?

You carry me secretly naked in your heart And clothe me publicly in armor, crying, "God is on your side," Yet, I openly cry, "Who is on mine? Tell me who?

You who bury your sons
And cripple your fathers,
Whilst you buried my father
In crippling his son.

The antiquated Saxon sword
Rusty in its scabbard of time, now rises,
You gave it cause in my name,
Bringing shame to the thorned head
That once bled for your salvation.

I hear your daily cries in the far off by-ways And your mouth pointing north and south And my Calvary looms again desperate in rebirth.

Your earth is partitioned but in contrition, It is the partition in your hearts, that you must abolish.

You nightly watchers of Gesthemane,
Who sat through my nightly trial,
Delivering me from evil,
Now deserted,

I watch you share your silver.
Your purse rich in hate
Bleeds my veins of love
Shattering my bone
In dust of the boxside
And the shank hill road.

There is no issue
Like the tissue of love.
No need as holy
As the palm outstretched
In the run of generosity.
No monstrosity greater
than the ache you inflict.

Who gave you the right to increase your fold And decrease the pastures of my flock? Who gave it to you? Who? And in whose name do you fight?

I am not in heaven.
I am here.
Hear me.
I am in you.
Feel me.

I am of you.
Be me.
I am with you.
See me.
I am for you.
Need me.
I am all mankind,
Only through kindness will you reach me.

What masked and bannered men
Can rock the ark and navigate a course
To their anointed Kingdom come?
Who sailed their captain
To waters troubled in my font.
Sinking in the sea of prejudice?

There is no virgin
Willing to conceive
In the heat of any bloody Sunday
You crippled children
Lying in cries on dirty streets,
Pushing your innocence
To the full flush face of Christian guns
Battling the blame on each other.

Do not grow tongues in your dying dumb wounds,
Speaking my name
I am not your prize and your death.
You have exorcised me in your game of politics.

Go home to your knees
And worship me in any cloth
For I was never tailored-made.
Who told you I was?
Who gave you the right to think it?

Take your beads in your crippled hands,
Can you count my decades?
Take my love in your crippled hearts,
Can you count the loss?
I am not orange.

I am not green.
I am a half ripe fruit,
Needing both colors to grow into ripeness
And shame on you to have withered my orchard

I in my poverty, alone without trust, cry,
"Shame on you,
And shame on you again,
And again for converting me into a bullet
And shooting me into men's hearts."

The ageless legend of my trial
Grows old in the youth of your pulse,
Staggering shamelessly from barricade to grave.
Filling in the book of history
My needless death one April.

Let me in my betrayal lay low in my grave, And you in your bitterness lie low in yours. For our measurements grow strangely dissimilar.

Our Father Who Art in Heaven, Sullied be Thy Name.
```

---

## IC-1716: Thidwick, the Big-Hearted Moose

- Title: Thidwick, the Big-Hearted Moose
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House
- Publication date as stated: Sept 1948
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1349
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Seuss)
ISBN: 978-0394800868
Publisher: Random House
Date (Month/Year): Sept 1948
```

### Introduction (context only: never use it for content warnings)

```text
What happens when well-meaning, productive types offer a (literal) free ride to those less willing to take responsibility for themselves? Consider the wide expanse of social services offered by American society today: welfare, public education, health services, (insert any variety of other public programs here). When does helping become enabling and when is enough enough?

In 1991, a few weeks before his death, friends asked Seuss if there were anything he might have left unsaid to all the children out there. Seuss replied, “The best slogan I can think of to leave with the kids of the U.S.A. would be ‘We can . . . and we’ve got to . . . do better than this.’

Thidwick, the Big-Hearted Moose by Theo Geisel (aka Dr. Seuss) is definitely more than a children’s story – it is a cautionary tale – for individuals and societies.
```

### Performance text (classify this)

```text
NOTE: Works by Theo Geisel (aka Dr. Seuss) have been identified as both POETRY and PROSE. Check your tournament rules to determine the category in which this selection should be entered.

Up at the Lake Winna-Bango . . . the far northern shore . . . Lives a huge herd of moose, about sixty or more, And they all go around in a big happy bunch Looking for nice, tender moose-moss to munch. Up at the lake Winna-Bango, one day, they were lunching, Just strolling along and enjoying their munching . . . (For the moose-moss that day was especially fine) . . . When it happened that Thidwick, the last moose in line, Saw a Bingle Bug sitting. The bug called out, “Hey! It’s such a long road, and it’s such a hot day, Would you mind if I rode on your horns for a way?” “Of course not!” smiled Thidwick, the Big-Hearted Moose. “I’m happy my antlers can be of some use. There’s room there to spare, and I’m happy to share! Be my guest and I hope that you’re comfortable there!” So the Bingle Bug picked out a nice easy seat and the moose went on looking for moose-moss to eat.

Well . . . An hour or so later, The bug heard a squeak, And he heard the small voice of a Tree-Spider speak. “I say!” said the spider, “you’ve got a nice place! That moose seems quite friendly, Has such a nice face . . . If I got on, too, Do you think he would mind. . ?”

“Hop aboard!” laughed the bug. “And I think that you’ll find that moose won’t object. He’s the big-hearted kind!” “I accept,” said the spider, with joy and delight.” And he started a web horn to the right.

While the spider was spinning, he heard a gay song And a fresh little Zinn-a-zu bird came along. He stopped. And he stared. And he chirped, “Well! Well!

WELL!
What a smart place to build! What a great place to dwell!
I’ve been living on trees ever since I was born,
But here’s something new! Why not live in a horn!
If there’s room there for two, then there’s room there for

three!” “There’s plenty of room!” laughed the bug. “And it’s free!” Thidwick stopped walking. What was all that talking? These guests had caught Thidwick the Moose unawares. “Hey!” he called out. “What goes on there upstairs?”

“Just building a nest, sir.” The Zinn-a-zu said, And began yanking hairs out of poor Thidwick’s head.

And he plucked out exactly two hundred and four! “Don’t worry,” he laughed. “you can always grow more!” Then he dozed off to sleep in his fine moose hair nest.

“This bird,” murmured Thidwick “is sort of a pest!
But I’m a good sport, so I’ll just let him rest,
for a host, above all, must be nice to his guest.
Besides, now, it’s getting quite late in the day
And surely tomorrow they’ll all go away.”

But, alas! The next morning the sun’s early light brought to Thidwick’s sad eyes a most unwelcome sight… “Meet my wife!” said the bird. “I was married last night. “And, perhaps by the way, I should mention to you that her uncle is coming to live with us, too. You’re a very fine host so I knew you’d be willing. . .” Then the uncle, a woodpecker, started in drilling!

All Thidwick’s friends shouted, “GET RID OF THOSE PESTS!” “I would, but I can’t.” sobbed poor Thidwick. “They’re

guests!”

“Guests indeed!” his friends answered and all of them

frowned. “If those are your guests, we don’t want you around! You can’t stay with us, ’cause you’re just not our sort!” And they all turned their backs and walked off with a snort.

Now the big friendless moose walked alone and forlorn, with four great big woodpecker holes in his horn. “What holes!” whispered Hernan, a squirrel, who spied

’em. “What holes to hide nuts in! Hmmm! Mind if I tried ’em?” “They’re yours!” called the woodpecker. “Get right inside

‘em! This big-hearted moose runs a public hotel! Bring your nuts! Bring your wife! Bring your children as

well!”
So the whole squirrel family all jumped on, pell mell.
And the very next thing the poor animal knew,
A Bobcat and turtle were living there, too!

NOW what was the big-hearted moose going to do? Well what would YOU do if it happened to YOU?

You couldn’t say “Skat!” ’cause that wouldn’t be right. You couldn’t shout “Scram!” ’cause that isn’t polite. A host has to put up with all kinds of pests, for a host, above all, must be nice to his guests. So you’d try hard to smile, and you’d try to look sweet and you’d go right on looking for moose-moss to eat.

But now it was winter and that wasn’t easy, for moose-moss gets scarce when the weather gets freezy. The food was soon gone on the cold northern shore of Lake Winna-Bango. There just was no more! And all Thidwick’s friends swam away in a bunch to the south of the lake where there’s moose-moss to

munch. He watched the herd leaving. And then Thidwick knew he’d starve if he stayed here! He’d have to go, too! He stepped in the water. Then, oh! What a fuss!

“STOP!” screamed his guests. “You can’t do this to us! These horns are our home and you’ve no right to take our home to the far distant side of the lake!” “Be fair!” Thidwick begged, with a lump in his throat.

“We’re fair,” said the bug. “We’ll decide this by vote. All those in favor of going, say ‘AYE,’ all those in favor of staying say ‘NAY’.” “AYE!” shouted Thidwick, but when he was done . . “NAY!” they all yelled. He lost ’leven to one. “We win!” screamed the guests, “by a very large score!” And poor, starving Thidwick climbed back on the shore.

Then, do you know what those pests did? They asked in some more! They asked in a fox, who jumped in from the trees, they asked in some mice and they asked in some fleas. They asked a big bear in and then, if you please, came a swarm of three hundred and sixty-two bees! Poor Thidwick sank down, with a groan, to his knees. And then, THEN came something that made his heart freeze.

Bullets came zinging right past Thidwick’s face! Guns were bang-binging all over the place! “Get that moose! Get that moose!” Thidwick heard a voice

call.

“Fire again and again and shoot straight one and all! We must get his head for the Harvard club wall!” Thidwick took to his heels with that load on his head! With five hundred pounds on his horns, the moose fled! He could have run faster without all those pests, but a host, above all, must be nice to his guests. Up canyon! Off cliff! Over wild rocky trail! With bullets bang-bouncing around him like hail! Up gully! Through gulch! And down slippery sluice, with his hard-hearted guests raced the soft-hearted moose! Then finally they had him!

Because of those pests, he had run out of luck,
because of those guests on his horns, he was stuck!
He gasped! He felt faint! And the whole world grew fuzzy!
Thidwick was finished, completely . . .or WAS he. . . ?
Finished…? Not Thidwick! DECIDEDLY NOT!
It’s true, he was in a most terrible spot,
But NOW he remembered a thing he’d forgot!
A wonderful something that happens each year
to the horns of all moose and the horns of all deer.
Today was the day, Thidwick happened to know . . .

That OLD horns come off so that NEW ones can grow!

And he called to the pests on his horns as he threw ’em, “you wanted my horns; now you’re quite welcome to ’em! Keep ’em! They’re yours! As for ME, I shall take myself to the far distant side of the lake!” And he swam Winna-Bango and found his old bunch, and arrived just in time for a wonderful lunch at the south of the lake, where there’s moose-moss to

munch. His old horns today are where you knew they would be. His guests are still on them, all stuffed, as they should

be.
```

---

## IC-1717: Thou Shalt Not Kill A memorial for Dylan Thomas

- Title: Thou Shalt Not Kill A memorial for Dylan Thomas
- Author (byline): Kenneth Rexroth
- Work: The Portable Beat Reader
- Publisher: Penguin Classic
- Publication date as stated: July 2003
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1690
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kenneth Rexroth
Book: The Portable Beat Reader
ISBN: 978-0142437537
Publisher: Penguin Classic
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
In one of his angriest poems Thou Shalt Not Kill: A memorial for Dylan Thomas, Kenneth Rexroth launches and indictment of what he believes America and its commercialism has done to poets Rexroth vents his rage in the militant terms usually reserved for combat. He sees the forces that lead to self destruction as a more dangerous enemy than those encountered on a battlefield. Why? Because they are so easily hidden or ignored. He places an emphasis on intentional suicides, particularly those who fail, and die slowly as a result of the failure.

Because “Timor mortis conturbat me,” which is Latin for the “fear of death confounds me.” I offer you Thou Shalt Not Kill by Kenneth Rexroth
```

### Performance text (classify this)

```text
I
They are murdering all the young men.
For half a century now, every day,
They have hunted them down and killed them.
They are killing them now.

At this minute, all over the world,
They are killing the young men.
They know ten thousand ways to kill them.
Every year they invent new ones.
In the jungles of Africa,
In the marshes of Asia,
In the deserts of Asia,
In the slave pens of Siberia,
In the slums of Europe,
In the nightclubs of America,
The murderers are at work.
They are stoning Stephen,
They are casting him forth from every city in the world.
Under the Welcome sign,
Under the Rotary emblem,
On the highway in the suburbs,
His body lies under the hurling stones.
He was full of faith and power.
He did great wonders among the people.
They could not stand against his wisdom.
They could not bear the spirit with which he spoke.

He cried out in the name
Of the tabernacle of witness in the wilderness.
They were cut to the heart.
They gnashed against him with their teeth.
They cried out with a loud voice.
They stopped their ears.
They ran on him with one accord.
They cast him out of the city and stoned him.
The witnesses laid down their clothes
At the feet of a man whose name was your name —
You.
You are the murderer.
You are killing the young men.
You are broiling Lawrence on his gridiron.
When you demanded he divulge
The hidden treasures of the spirit,
He showed you the poor.
You set your heart against him.
You seized him and bound him with rage.
You roasted him on a slow fire.
His fat dripped and spurted in the flame.

The smell was sweet to your nose.
He cried out,
“I am cooked on this side,
Turn me over and eat,
You
Eat of my flesh.”
You are murdering the young men.
You are shooting Sebastian with arrows.
He kept the faithful steadfast under persecution.
First you shot him with arrows.
Then you beat him with rods.
Then you threw him in a sewer.
You fear nothing more than courage.
You who turn away your eyes
At the bravery of the young men.
You,
The hyena with polished face and bow tie,
In the office of a billion dollar
Corporation devoted to service;
The vulture dripping with carrion,
Carefully and carelessly robed in imported tweeds,
Lecturing on the Age of Abundance;
The jackal in double-breasted gabardine,
Barking by remote control,
In the United Nations;
The vampire bat seated at the couch head,
Notebook in hand, toying with his decerebrator;
The autonomous, ambulatory cancer,
The Superego in a thousand uniforms;
You, the finger man of behemoth,
The murderer of the young men.

II
What happened to Robinson,
Who used to stagger down Eighth Street,
Dizzy with solitary gin?
Where is Masters, who crouched in
His law office for ruinous decades?
Where is Leonard who thought he was
A locomotive? And Lindsay,
Wise as a dove, innocent
As a serpent, where is he?

Timor mortis conturbat me.
What became of Jim Oppenheim?
Lola Ridge alone in an
Icy furnished room? Orrick Johns,
Hopping into the surf on his
One leg? Elinor Wylie
Who leaped like Kierkegaard?
Sara Teasdale, where is she?

Timor mortis conturbat me. Where is George Sterling, that tame fawn? Phelps Putnam who stole away? Jack Wheelwright who couldn’t cross the bridge? Donald Evans with his cane and Monocle, where is he?

Timor mortis conturbat me.
John Gould Fletcher who could not
Unbreak his powerful heart?
Bodenheim butchered in stinking
Squalor? Edna Millay who took
Her last straight whiskey? Genevieve
Who loved so much; where is she?

Timor mortis conturbat me. Harry who didn’t care at all? Hart who went back to the sea?

Timor mortis conturbat me.
Where is Sol Funaroff?
What happened to Potamkin?
Isidor Schneider? Claude McKay?
Countee Cullen? Clarence Weinstock?
Who animates their corpses today?

Timor mortis conturbat me.
Where is Ezra, that noisy man?
Where is Larsson whose poems were prayers?
Where is Charles Snider, that gentle
Bitter boy? Carnevali,
What became of him?
Carol who was so beautiful, where is she?

Timor mortis conturbat me.

III
Was their end noble and tragic,
Like the mask of a tyrant?
Like Agamemnon’s secret golden face?
Indeed it was not. Up all night
In the fo’c’sle, bemused and beaten,
Bleeding at the rectum, in his
Pocket a review by the one
Colleague he respected, “If he
Really means what these poems
Pretend to say, he has only
One way out —.” Into the
Hot acrid Caribbean sun,
Into the acrid, transparent,
Smoky sea. Or another, lice in his
Armpits and crotch, garbage littered
On the floor, gray greasy rags on
The bed. “I killed them because they
Were dirty, stinking Communists.
I should get a medal.” Again,
Another, Simenon foretold
His end at a glance. “I dare you
To pull the trigger.” She shut her eyes
And spilled gin over her dress.
The pistol wobbled in his hand.
It took them hours to die.
Another threw herself downstairs,
And broke her back. It took her years.
Two put their heads under water
In the bath and filled their lungs.
Another threw himself under
The traffic of a crowded bridge.
Another, drunk, jumped from a
Balcony and broke her neck.
Another soaked herself in
Gasoline and ran blazing
Into the street and lived on
In custody. One made love
Only once with a beggar woman.
He died years later of syphilis
Of the brain and spine. Fifteen
Years of pain and poverty,
While his mind leaked away.

One tried three times in twenty years To drown himself. The last time He succeeded. One turned on the gas When she had no more food, no more Money, and only half a lung. One went up to Harlem, took on Thirty men, came home and Cut her throat. One sat up all night Talking to H.L. Mencken and Drowned himself in the morning. How many stopped writing at thirty? How many went to work for Time? How many died of prefrontal Lobotomies in the Communist Party? How many are lost in the back wards Of provincial madhouses? How many on the advice of Their psychoanalysts, decided A business career was best after all? How many are hopeless alcoholics? René Crevel!

Jacques Rigaud!
Antonin Artaud!
Mayakofsky!
Essenin!
Robert Desnos!
Saint Pol Roux!
Max Jacob!
All over the world
The same disembodied hand
Strikes us down.
Here is a mountain of death.
A hill of heads like the Khans piled up.
The first-born of a century
Slaughtered by Herod.
Three generations of infants
Stuffed down the maw of Moloch.

IV
He is dead.
The bird of Rhiannon.
He is dead.

In the winter of the heart.
He is Dead.
In the canyons of death,
They found him dumb at last,
In the blizzard of lies.
He never spoke again.
He died.
He is dead.
In their antiseptic hands,
He is dead.
The little spellbinder of Cader Idris.
He is dead.
The sparrow of Cardiff.
He is dead.
The canary of Swansea.
Who killed him?
Who killed the bright-headed bird?
You did, you son of a bitch.
You drowned him in your cocktail brain.
He fell down and died in your synthetic heart.
You killed him,
Oppenheimer the Million-Killer,
You killed him,
Einstein the Gray Eminence.
You killed him,
Havanahavana, with your Nobel Prize.
You killed him, General,
Through the proper channels.
You strangled him, Le Mouton,
With your mains étendues.
He confessed in open court to a pince-nezed skull.
You shot him in the back of the head
As he stumbled in the last cellar.
You killed him,
Benign Lady on the postage stamp.
He was found dead at a Liberal Weekly luncheon.
He was found dead on the cutting room floor.
He was found dead at a Time policy conference.
Henry Luce killed him with a telegram to the Pope.
Mademoiselle strangled him with a padded brassiere.
Old Possum sprinkled him with a tea ball.
After the wolves were done, the vaticides
Crawled off with his bowels to their classrooms and
quarterlies.
When the news came over the radio
You personally rose up shouting, “Give us Barabbas!”
In your lonely crowd you swept over him.
Your custom-built brogans and your ballet slippers
Pummeled him to death in the gritty street.
You hit him with an album of Hindemith.
You stabbed him with stainless steel by Isamu Noguchi,
He is dead.
He is Dead.
Like Ignacio the bullfighter,
At four o’clock in the afternoon.
At precisely four o’clock.
I too do not want to hear it.
I too do not want to know it.
I want to run into the street,
Shouting, “Remember Vanzetti!”
I want to pour gasoline down your chimneys.
I want to blow up your galleries.
I want to bum down your editorial offices.

I want to slit the bellies of your frigid women.
I want to sink your sailboats and launches.
I want to strangle your children at their finger
paintings.
I want to poison your Afghans and poodles.
He is dead, the little drunken cherub.
He is dead,
The effulgent tub thumper.
He is Dead.
The ever living birds are not singing
To the head of Bran.
The sea birds are still
Over Bardsey of Ten Thousand Saints.
The underground men are not singing
On their way to work.
There is a smell of blood
In the smell of the turf smoke.
They have struck him down,
The son of David ap Gwilym.
They have murdered him,
The Baby of Taliessin.

There he lies dead,
By the Iceberg of the United Nations.
There he lies sandbagged,
At the foot of the Statue of Liberty.
The Gulf Stream smells of blood
As it breaks on the sand of Iona
And the blue rocks of Canarvon.
And all the birds of the deep sea rise up
Over the luxury liners and scream,
“You killed him! You killed him.
In your God damned Brooks Brothers suit,
You son of a bitch.”
```

---

## IC-1718: Three Little Cajun Pigs

- Title: Three Little Cajun Pigs
- Author (byline): Mike Artell
- Work: Not specified
- Publisher: Dial Books
- Publication date as stated: Sept 2006
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1501
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mike Artell
ISBN: 978-0803728158
Publisher: Dial Books
Date (Month/Year): Sept 2006
```

### Introduction (context only: never use it for content warnings)

```text
Cajuns were never long-term settlers in the city of New Orleans. A population always geared more to rural countryside; Cajuns settled in South Louisiana from the parishes west of New Orleans extending all the way to Texas. But their influence is felt throughout Louisiana, in their customs, food, music and storytelling.

So take a journey with me to Louisiana where the catfish are jumpin’ and the Three Little Cajun Pigs are making a roux . . . by Mike Artell
```

### Performance text (classify this)

```text
Characters:
Thibodeaux – (pronounced “TIB-boe-doe”)
Trosclair – (pronounced “TROSS-clair” or tross-CLAIR”)
Ulysse – (pronounced “you-LEASE”)

In south Loo-siana, where gators grow big,
Live t-ree Cajun pigs and an o’ mama pig.
Dem pigs was named Trosclair, and Thibodeaux too,
Ulysse was de oldest, dey all called him “Boo.”

One mornin’ dere mama done give ‘em som food And tell ‘em some news dat don’ make ‘em feel good. “It’s time dat you boys find you own place to stay; I t’ink dat you better start lookin’ today.

“Go build you a house of you own,” Mama say. “You’ll sleep dere tonight if you start right away.” So t’ree little pigs pack up all of dere clothes, Kiss Mama good-bye and den follow dere nose.

Dey walk for a while, and den Trosclair he say,
“I’ll build me a house, and I’ll do it today.
I’ll build it so fast jus’ like you never saw,
I’d do it right now if I had me some straw.”

Den jus’ up de road by de bayou dey see,
A big wooden sign dat been nailed to tree.
Dem pigs read de words on de sign and dey say,
“Look here! Dis straw’s free! You can take it away!”

“Go on,” Trosclair say, “I will catch up to you, I’ll build a straw house before you count to two.” Ol’ Boo roll his eyes and he make dem big sigh, And Thibodeaux say, “You look angry, Boo. Why?”

“Straw is okay if you making dem bed,
But when you build walls, you need somethin’ instead.
Houses for pigs got to be plenty strong
In case dat dem gator come crawlin’ along.”

Den jus’ up de road, guess what bot’ dem pigs see . . .
Somebody been cuttin’ some limbs off a tree.
And dere was a sign dat say, “Haul dese away.”
And Thibodeaux shout, “Dis is my lucky day!”

He grab all dem limbs and start workin’ so fas’,
His house halfway finished ‘fore too much time pass.
Ulysse, he start t’inkin’, “Dem boys got it wrong;
If you build a house, den it’s got to be strong.”

Ulysse shake his head and den he walk some more
And soon dat pig see just what he’s lookin’ for.
A whole bunch o’bricks was piled next to a sign
Dat say, “Need dese bricks? You can have ‘em, dat’s fine.”

Boo clear off a spot for his house made of brick.
He build dat house strong, and he make dem walls thick.
An’ while he was workin’, who come skippin’ by?
Dem two udder pigs, and dey laugh ‘til dey cry.

“Dem bricks sho’ look heavy. What’s wrong wit’ you, Boo? How come you don’t use straw or sticks like we do?” Boo frown and he say, “When dat gator come by, he’ll knock your house down wit’ his tail if he try.”

An’ speakin’ of gators, not too far away,
Somebody was watchin’ dem little pigs play.
Ol’ Claude, dat big gator, was in de bayou,
He see dem t’ree pigs and he watch what dey do.

Claude crawl out de water and hide in de grass,
And sit dere and wait ‘til dem first two pigs pass.
Den Claude jump in front of dem pigs and he say,
“I t’ink dat it’s time for some couchon de lait!”

Ol’ Claude start to chase de first pig dat he saw . . . Trosclair, he’s de one wit’ de house made of straw. Trosclair he run home and den shut dat door tight, He pull close dem curtains and turn off de light.

“Oh piggy,” say Claude with dat big gator smile,
“Could I come inside of you house for a while?”
Dat’s when Trosclair shout, “NO! I won’t let you in;
Not be all dem hairs dat I got on my chin.”

“Hmm. . . “ growl Ol’ Claude in dat deep gator voice. “Now pitty, you lef’ me wi’ no udder choice.” Ol’ Claude his and puff and he make his face frown, He wiggle a little and turn hisself roun’.

And WHACK! When dat gator done flip his tail hard,
Dat straw house go flyin’ all over de yard.
Trosclair look at Claude and he cry, “You so big,
You jus’ a mean bully. Why pick on us pig?”

“Ha ha,” Ol’Claude laugh. “Mon ami, don’ get made, Between you and me . . . dat straw house was some bad.” Den Trosclair he turn and as quick as a mouse, He run to where Thibodeaux build de stick house.

When Thibodeaux see Ol’ Claude chasin’ Trosclair,
He say, “Hurry up, you’ll be safe here, mon frer!”
Dey run in dat stick house and lock all de door,
Den peek out to see if Claude comin’ some more.

“Oh piggies, “say Claude with dat big gator smile,
“Could I come inside of you house for a while?”
Dem little pigs shout, “NO! We won’t let you in;
Not by all dem hairs dat we got on our chin.”

“Okay,” say Ol’ Claude, “you can have it your way, But I don’t like workin’ dis hard every day.” Ol’ Claude hiss and puff and he make his face frown He wiggle a little and turn hisself roun’.

And WHACK! When dat gator done flip his tail hard, Dat stick house go flyin’ all over de yard. Dat’s all dem pigs needed to scare ‘em to death, Dey jump up and run ‘til dey plumb outta breath.

Now, inside his house, Boo was busy fo’ true
He had a big pot and was makin’ a roux.
He stir dat roux good ‘cause Ulysse he done learn
You gotta keep stirrin’ or roux’s gonna burn.

Den out in de yard Ulyssee hear all dat noise, He t’ink to himself, “Now what’s wrong wit’ dem boys?”

Ulysse slam de door and he turn de big lock,
An jus’ when he did dat, he heard a soft knock.
Oh piggies,” say Claude with dat big gator smile,
“Could I come inside of you house for a while?”

Dem little pigs shout, “NO! We won’t let you in; Not by all dem hairs dat we got on our chin.”

So WHACK! Dat ol’ dagor done flip his tail hard, But dis time de house don’ fall down in de yard.

Ag’in and ag’in, Claude done hit it some more,
Den he gotta stop ‘cause his tail getting’ sore.
“I see dere’s a chimney. Dat’s how I’ll get in,
And den I’ll get all of dem hairs on your chin.

Trosclair start to whine, “What are we gonna do?” And Thibodeaus cry, “He will eat us fo’ true!” Boo shout at his brudders, “Get up off your seat! An’ bring me some wood. We gone turn up de heat.”

Outside dey hear Claude on dat roof scratchin’ roun’. He don’t climb so good and he keep fallin’ down. But finally he climb all de way to de top, He jump in de chimney, den let go and drop.

Now, Claude he don’ know ‘bout dat roux in de pot, But as he was fallin, he start getting’ hot. Ol’ Claude can’t slow down, and he t’ink, “Dis ain’t good. If I could get out of dis chimney, I would.”

But it was too late, Claude’s big tail hit de roux, And y’ll when it did, Claude don’t know what to do.

“Aiieee!” shout Ol’ Claude. “Someone help me tout de

suite. “My tail’s burnin’ up, won’t you please stop de heat?!”

Dem t’ree little pigs know what Claude tried to do,
But dey figure he learned his lesson fo- true.
Ulysse run and grab a big lid for dat pot.
Den put it on top so it won’t be so hot.

Claude’s tail cam out first and de pigs had to laugh ‘Cause dat gator was toasted on his bottom half. He walked out de door kinda funny and slow, He head down de road and de pigs watch him go.

“Ya’ll have a nice day,” Trosclair call wit’ a smile, Den Thibodeaux laugh, “Don’ come back for a while.” But big brother Boo got his arms folded tight. He ask, “Where ya’ll plannin’ on sleepin’ tonight?”

Dem two udder pigs dey start scratchin’ dere heads Dey ain’t got no house and dy ain’t go tno beds. Ulysse tell dem pigs, “Y’all can say here tonight, But we got to go and buld bot’ your house right.”

De very next day, Thibodeaux and Trosclair
Done build de best houses you seen anywhere.
Ulysse show dem how dey can build dat house strong
In case dat ol’ gator should come back along.

And speakin’ of gators, way down de bayou
A gator we know sure was hurtin’ fo’ true.
He got him an ice pack on his derriere
And where dem pigs live, he ain’t goin’ back dere.

Now, some of dis story is true and some’s not,
And which part is which, y’all . . . I guess I forgot.
But take my advice ‘cause I know dat it’s true:
When gators come roun’, cher . . . just make you a roux.
```

---

## IC-1719: Time, Temperature

- Title: Time, Temperature
- Author (byline): Jim Daniels
- Work: Letters to America: Contemporary American Poetry on Race
- Publisher: Wayne State University Press
- Publication date as stated: 1995
- Event as filed: Poetry
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1418
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jim Daniels
Book: Letters to America: Contemporary
American Poetry on Race
ISBN: 978-0814325421
Publisher: Wayne State University Press
Date (Month/Year): 1995
```

### Introduction (context only: never use it for content warnings)

```text
A predominantly Black city, Detroit has a long history of police brutality, housing inequality and racial struggles. In 1947, a brawl broke out between a white and black man in downtown Detroit. Igniting existing racial tensions, it resulted in a 24-hour riot and the deaths of 25 African - Americans and nine whites. Over twenty years later, Detroit was home to one of the most violent urban revolts in the 20th century – the Detroit Race Riot of 1967. Today, Detroit is still one of the poorest cities in the United States, and according to many the racial tensions have been resolved. In Time, Temperature Jim Daniels takes on the 1943 and 1967 Detroit riots and the continued pervasiveness of racism even within his own family.
```

### Performance text (classify this)

```text
1967, Detroit. My grandfather watches Tracer bullets zing past His window. The National Guard’s taken over Lillibridge School on the corner.

He remembers the strike at Packard

when they promoted blacks,

Then the riots in ’43,

How the crowds gathered on Belle Isle

just down the road, all the bloodshed

just down the road.

On the phone with my father, he is saying niggers And my father is saying Dad he is saying Dad stay in the house, stay away from the window.

My grandfather has his theories

why they can’t take the cold

Can’t skate can’t swim

why they can’t park their cars

why grape’s their favorite flavor

Why if you get bit by one with purple lips

it will kill you.

My father shakes his head into thick air
saying stay away, stay away.
A drop of sweat hits the dirty kitchen floor.
Dad, Dad. My father’s long sigh.



Eenie, meanie miney moe
catch a nigger by the toe
our toes wedged in a tight circle
to see who’d be It. My mother
wouldn’t let us say nigger.
She said say froggy.

We said froggy. The other kids said froggy?

She washed my mouth with soap. Where did you hear that word? Everywhere. Where?



1967. Eleven, I climbed on the garage
with my father’s camera. In the streaked photos
flocks of helicopters blotch the sky, nothing
like birds. I held on to the rough shingles
as the spinning blades roared above me.
Helicopters spilled guardsmen
onto the armory lawn on Eight Mile Road,
the border between Detroit and Warren.

We lived on that edge. Sirens wailed their crazy tune, no Motown Sound, nothing we could dance to.

Fear of heights seemed more real than what I heard on the radio, than rumors panting on the street: They’re at Belmont. They’re at Farwell Field. They’re crossing Eight Mile.

Getting up was easy. I needed help getting down, my feet dangling in air, the camera somersaulting down onto the grass.



Eight Mile Road. Six lanes wide. The long barbed shout, pale slab, sizzling fuse.

I didn’t know a black person till I was nineteen. I could have almost shouted from my porch.


Nigger pile. Riding nigger.
Nigger pile on Tony. Nigger beard.
Nigger stompers. Nigger-rigged.
Nigger-lipped. Niggered up. Nigger toes.
Niger Heaven. How far
you have to chase that nigger
to get that shirt? A fight, a fight
a nigger and a white.

Should I explain the terms, include an index
and glossary? Do we all possess
such footnotes, filed, hidden, backwards,
in code, watermarks revealed by light?

Plenty of words for hate around here. Like Eskimos with snow, we have our subtle distinctions.



Our fathers worked with their fathers
in factories in Detroit and Warren,
Brought their hate home in greasy lunch pails:
better watch out for that nigger.
That’s a nigger department.
Don’t help that nigger,
lazy nigger.

It spilled across the dinner tables,
through the muddy alleys,
across the concrete playgrounds,
into the schools, and we learned
our lessons well.



1974. Black students
from Pershing High two miles away
visited Fitzgerald, my school.
We asked them questions
in a room crowded with teachers
who prompted us in whispers.
So foreign even those translators couldn’t help.
Stilted as a high-school play.
Someone took pictures for the yearbook.

They filled our halls with a flavor
foreign and pungent. Some new kind of cooking
I wasn’t sure about.
The next day in class we sat glum
while a perky teacher preached brotherhood.
We knew better. They only brought
the nice ones, somebody said.



1975. I worked in a liquor store where we didn’t cash checks for blacks but sold them booze and cigarettes.

A man held a gun to my head
where’s your hiding place
where’s your ***** hiding place?
I said we don’t have a hiding place
he said *****, everybody
got a hiding place
I said we took it to the bank
he said I’m gonna kill you ********
where’s your hiding place?

We stood there, his gun brushing my temple. We looked each other in the eye: no recognition. He grabbed money from the register, took off down Eight Mile. I reached down and fingered the cigarette carton filled with checks and twenties. the boss called the cops.

Fingerprints on a can of Colt .45 and no clues or suspects. Colt .45, I said, figures.

I flipped through the mug shots: some nigger, I said.



Carl the gun collector handed out rifles to the neighbors in ’67: just in case just in case they cross Eight Mile. To protect our families and homes, he said. The right to bear arms. My father did not take one.

In 1974 under the threat of busing
neighbors took pledges
put signs in their windows
I will not send my kids.
I will keep my kids home.
My mother took no sign.

The Supreme Court ruled against
cross-district busing.
Neighbors smiled archly
no thanks to you, as if my mother
was a scab in this union town.



1980. In the department store,
those foam packing chips that last forever
poured from an overhead funnel
into gift boxes full

Kim’s dark skin
surrounded by the white, white foam.
Where all the black people worked,
along with me and another white kid.

We felt like robots down there,
filling and sealing. Till our eyes locked
in the hard stare of mannequins.
We ate lunch together
in the lounge. People talked.
It only took me a year to ask her out.
Dixie scowled. What are you doing?
This is Detroit you’re talking about.

We went to a movie in my part of town,
for coffee in her part.
I can’t remember what we saw
because I held her hand in the dark
and we were alone there just like
two white kids, or two black kids.

All night the stares bit into us
like tiny bugs we couldn’t see.
Walking to the car, I squeezed
her hand into a fist.
I guess you have to be rich
to get away with it, she said
and maybe she was right.

In her apartment, her child cried upstairs while we held each other on the couch.

Go home white boy, somebody yelled when I go in my car.



I said some nigger robbed the store
and the copy said What else is new?
Get a gun, he said.
The board tilts, and all the balls
roll into the same hole.

I felt bad, but I said it anyway.
My shrunken head, tiny eyes
sewn shut. There is no
immunization, no shot, no cure,
no pill, no magic, no saint,
no argument, no prophet,
no potion, no confession,
no gift, no miracle, no ***** miracle.

No.



Last summer, the dog next door scared away two black kids trying to break into my basement.

I saw them running away. A week later
the same two kids cased out a house
down the street. I stood at the door
watching, sweating, heart jumping.

I stepped out toward them. They said You keep following us you’re gonna get hurt. I said I’m only trying to protect my property. They said Listen man, you wanna get hurt?

No, I don’t want to get hurt. Yes, I have property now, An old house in this mixed neighborhood. Maybe I was afraid because they were black. Maybe they were angry because I was white. I tried to talk calmly but I know enough about being stoned to know they were stoned on something. Everybody stoned on something -- Stoned on history and hate.

Everybody got a hiding place.



Carl took his guns back
but they are someplace.
Carl moved away
but he is someplace.

I know Carl. His nose twitches with the gunpowder of his own hate.

They are someplace.



I am trying to be naïve.

An open fire hydrant in hot August
after an afternoon game at Tiger Stadium.
I am walking toward my car.
A young black kid, maybe six, is dancing
in his underwear in the cool spray
he is holding his wrists up toward the sky
as if to say take me, take me like this
and I am so hot I join him
dancing too in cutoffs and T-shirt

And I raise my arms above my head thinking yes, I would like to be taken like this and we dance under the same sun and there is room enough for both of us in the spray on Rosa Parks Boulevard in Detroit in Michigan in America
```

---

## IC-1720: To Survivors Everywhere – A Collection

- Title: To Survivors Everywhere – A Collection
- Author (byline): Sierra DeMulder
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Poetry
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 921
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sierra DeMulder
Book: The Bones Below
Contains Taxidermy and Misplacing Their Ring
Fingers
ISBN: 978-0984251537
Publisher: Write Bloody Publishing
Date (Month/Year): March 2010
Author: Sierra DeMulder
Book: Today Means Amen (Pg 91-93)
ISBN: 978-1449474119
Publisher: Andrews McMeel Publishing
Date (Month/Year): Feb 2016
```

### Introduction (context only: never use it for content warnings)

```text
The loss of a child may be the worst trauma a human being can experience. Though it’s not a terribly common experience in the United States — about 10,000 children between the ages of 1 and 14 died in 2018 — the horrific potential for losing a child looms large. And although reassuring, the numbers also make plain why the death of a child brings so much grief, and why it’s so feared, so painful, and so stigmatized.

To Survivors Everywhere – A Collection by Sierra DeMulder including Taxidermy, Misplacing Their Ring Fingers and Today Means Amen.
```

### Performance text (classify this)

```text
Taxidermy Five years after your daughter’s death, you still cry in the juniors’ section of department stores.

You preserve her bedroom like a taxidermist. Her unworn prom dress still hangs like a skinned mermaid in her closet.

Cancer entered your home like a greedy tenant,
drew himself into family portraits,
slept in your daughter’s bed,
swallowed all her blood cells.

It started with a headache. A fever,
your daughter melting like a popsicle.
It took you a week to tell your husband
about the blood in the toilet.

Sometimes, you wonder
if you never caught it,
could you have lived
as if it was never there?

As if saying that word instantly
drapes a shroud over your house.
Would it still have slept
like cremation in her bed?

The doctors spoke to you in time lines, as your daughter’s weight dropped like a countdown, a surprise party no one wanted to throw.

Once, when she was in the other room,
her blood being read like tea leaves,
the doctor suggested not to bother with college
applications.

You couldn’t bring yourself to tell her.
You couldn’t bring yourself to say it.
Sometimes you think she knew,
as she methodically filled out each question and box,
it was never for her.

There is still a stack of unsent applications
hidden like tumor in your dresser.
She kissed every envelope goodbye.
You couldn’t bear to send more of her away.

When she passed,
quietly like a note to God,
all you wanted was to swaddle her
in your arms like an infant, bring her home
from the hospital, fragile and new.

Breastfeed her back to life,
potty train and finger paint,
reteach her the alphabet,
retrace her first steps
back to you.

To lose a child is like giving birth in reverse. It is slow and it rips, planting a permanent lump in your throat.

When chemotherapy pulled out
the last of her hair, you started carrying
her baby teeth in your pocket: A reminder
things can grow back.

TRANSITION

And it’s true . . . some things can grow back, but so many other things fall apart.

Misplacing Their Ring Fingers
The summer my parents lost their marriage
like so many magnets kicked under the refrigerator,
my cousin and I named trees after babysitters
we never had. We lived in our bathing suits,
washed our hair in pond water and sunburned.

(Once, my mother slammed the screen
door so hard, I comforted the hinges.) I taught
my cousin how to make face paint out of spit
and dirt. She taught me to swim underwater.
(Once, I found my father weeping on the bed
they did not share anymore.) On the green carpet
of summer, we played until the cicadas, dressed
in dusk, called us to dinner. We kissed goodnight
and I ran home barefoot in the dark.

(Once, I sat between my parents and placed their hands in my lap like a seatbelt. I do not remember this.) To this day, walking at night on that creaking road still reminds me of wolves.

TRANSITION

So how do people survive so much pain, so much loss? Some people understandably crumble after traumatic events, while others seem to have an extraordinary capacity to rebound and survive. So, maybe this is the affirmation you need to hear at the end of a cruel day. Here's to survivors everywhere. Our traumas may be different; but loss, regardless of the form, is always traumatic . . . and, yet, we survive. Amen.

Today Means Amen
(Pg 91-93) Dear you,
Whoever you are,
However you got here,
This is exactly where you are supposed to be.
This moment has waited its whole life for you,
You are a solider,
Come home baby, it’s over,
You don’t need to suffer anymore.

Dear you,
This moment is a surprise party,
You are both hiding in the dark,
And walking through the door,
This moment is a Hallelujah,
This moment is your permission slip,
To finally open that love letter,
You’ve been hiding from yourself,
The one you wrote when you were little,
When you still danced like a sparkler at dusk,
Do you remember the moment you realized they were
watching?
When you became ashamed of how much light you were
holding?
When you first learned how to un-love yourself?

Dear you,
The word today, means amen in every language.
Today, we made it,
Today, I’m gonna love you,
Today, the box cutter will rust in the garbage,
Today, the noose will forget how to hold you,
Today,
Today.

Dear you,
And I have always meant, you.
Nothing would be the same if you did not exist.
You, who were once as small as a bouquet,
Who could sleep in the laughs of strangers,
Nothing would be the same if you did not exist.
You, who’s voice is someone’s favorite voice,
Someone’s favorite face to wake up to,
Nothing would be the same if you did not exist.

You, the teacher,
The starter’s gun,
The lantern in the night who offers not a way home,
But the courage to travel farther into the dark.

You, the friend,
The sacred chorus of ‘How can I help you?’
Who have felt more numb than holy,
More cracked than mosaic,
Who has known the tiles of a bathroom by heart,
Who has forgotten what makes you worth it.

You, the forgiven, The forgiver, Who belongs right here, in this moment.

You, this clump of cells,
This happy explosion that happened to start breathing,
And by the grace of whatever is up there,
You got here,
You made it, this whole way,
Through the nights that swallowed you whole,
The mornings that arrived in pieces,
The scabs, the gravel,
The doubt, the hurt,
The hurt, the hurt,
Is over today,
You made it,
You made it,
You made it,
Here.
```
