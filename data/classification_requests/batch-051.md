# Classification request: batch 51 of 53 (40 records, IC-2401 to IC-2440)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-051-reply.json`.

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

## IC-2401: Commercial Break

- Title: Commercial Break
- Author (byline): Augusten Burroughs
- Work: Magical Thinking: True Stories, Pgs 1-16
- Publisher: St. Martin's Press
- Publication date as stated: Oct 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: AB, MRS. AMES, MAN 1, DAD, DIRECTOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1612
- Already set (do not supply): none

### Source block (context only)

```text
Author: Augusten Burroughs
Book: Magical Thinking: True Stories, Pgs 1-16
ISBN: 978-0312315948
Publisher: St. Martin's Press
Date (Month/Year): Oct 2004
```

### Introduction (context only: never use it for content warnings)

```text
TV VOICE:
```

### Performance text (classify this)

```text
AB: (Pgs 1-16) When I was seven, I was plucked out of an uneventful life deep in darkest Massachusetts and dropped into a Tang Instant Breakfast Drink commercial. It was exactly like being abducted by aliens. I was a lonely kid with entirely imaginary friends. I played with trees. Then, one day during penmanship class, a white van pulled up in front of our little gray schoolhouse, and the men from Tang climbed out.

Enjoyed by consumers in more than 60 countries, Tang is one of Kraft’s most global brands and one of our largest. Kraft holds the number one position in powdered beverages in the world and our Tang brand is an important part of that portfolio. The combination of the great fruit taste of Tang, its nutritional benefits, convenience and affordable price has made it a favorite among millions. Since the early '80s, Tang has been launched in approximately 30 countries. And now back to your regular programming. . . Thanks for your attention during this Commercial Break by Augusten Burroughs.

AB: I was sitting in Mrs. Ames's tedious penmanship class looking out the window when the white van pulled into the circular driveway. Mrs. Ames noticed, too, because she paused in the middle of looping a “D”. Visitors were uncommon at our school. Especially visitors dressed in dark suits, wearing sunglasses, and carrying black brief-cases. When [Mrs. Ames] turned her ancient neck to the window, my mind added the sound effect of a branch creaking under the weight of snow before it snaps. I was quite sure that Mrs. Ames was one of the original settlers of the town. She once said that television was (imitating Ames) "nonsense, just a fad like radio."

MRS. AMES: (glaring at the class) Remain seated and do not talk. I shall return in a moment.

AB: A moment later, Mrs, Ames joined the men outside and, to my horror, smiled. I'd never seen Mrs. Ames smile before, and the thought had never occurred to me that such an act was even possible. But there it was, her mouth open in the white daylight, her teeth exposed. (smile as Mrs. Ames) One of the men stepped forward, removed his sunglasses, and said something to her. She touched her hair with her hand and laughed. I was horrified to see Mrs. Ames laugh. And then blush. To see her in such a state of obvious bliss was unbearable. I had to look away.

Eventually, Mrs. Ames walked back into the room, and I watched her legs, all plump and plastic-looking through her support hose. She wore high heels of an unfashionable style that made a sharp, angry sklack against the tile floor when she walked.

MRS. AMES: Children, children, may I have your attention please? (clapping her hands) "We have some very special surprise guests here today. These men are here to make a television commercial.

AB: Well, I almost peed. She might as well have told me that I never had to come to school again and I was free to hit anybody I wanted to, without being punished. I loved television commercials. The only reason I watched TV was so that I could see the commercials. Faberge Organics Shampoo: (imitating the commercial) "I told two friends. And they told two friends. And so on. . . and so on. . . and so on." Or my current favorite: (imitating the commercial) "Gee, your hair smells terrific!" I was also fond of the commercial with little dog chasing the chuck wagon underneath the kitchen sink.

MRS. AMES: (to the class) These men would like to put our schoolhouse in a commercial for Tang. Do any of you know Tang?"

AB: There were gasps in the room. Of course, we knew Tang, the orange crystalline powder that the astronauts brought with them to outer space. I loved Tang and would sometimes eat it by the teaspoon, straight from the jar. I loved the green label, the orange lid. The way the lid was extra wide and easy to unscrew. I even liked the paper eardrum that was over the mouth of the lid when you first opened the jar. You had to puncture the eardrum with a spoon, and printed on top was "Tang, Tang, Tang."

Mrs. Ames told us that the men wanted to use some of us in their commercial. Instantly, the students began raising their hands. Except for me. Some voice inside me said, "Don't do it. It's beneath you." Instead, I sat politely at my desk with my hands clasped firmly together. One thing was certain: I would be in their Tang commercial.

The interviews began in groups of three. When it was finally my turn, the men were tired, as evidenced by their loosened ties and the large wet spots that spread under their arms. They'd spoken to thirty kids and had notes piled on the table in front of them.

MAN 1: Hi guys. So do any of you want to be in a commercial? (AB nods vigorously) Good. So, I'm gonna tell a joke, and I want to see what it sounds like when you laugh. Ready? Okay. (raises voice and makes a comical face) Your mother wears army boots!

AB: (looks left, then right) Neither of the other kids laughed.

(laughs hysterically, then proudly) I was able to bring tears to my eyes. My face was flushed, my hands dripping with sweat.

MAN 1: Wow, you really liked that joke, did you? Do you kids like Tang?

AB: The other two kids nodded grimly. (to man, gushing) I love Tang! Only I like to make it with an extra scoop. Plus, you can put it in ice cube trays and then freeze it! (to audience) Where had that come from? I'd never in my life frozen Tang.

MAN 1: That's great! What's your name?

AB: Augusten?

MAN 1: Augusten. You were great. We want you.

AB: As soon as I got home, I sprinted up our gravel driveway and threw open the front door, screaming "I'm gonna be in a Tang commercial! I'm gonna be in a Tang commercial!" In preparation for my television acting debut, I watched commercials incessantly, committing them to memory and reciting phrases endlessly. (as if on camera. . .)

(in a high-pitched girl’s voice) Can I help you fry the chicken?

(different southern girl’s voice) I want to help! (imitating their mother) I don't fry chicken anymore. I use new Shake 'N Bake.

(mimicking another commercial) Let's get Mikey to try it. He won't eat it; he hates everything!

I loved to sing jingles. (singing) * “That great Pepsi taste. Diet Pepsi won't go to your waist. Now you see it. Now you don't. Oh, Diet Pepsi one small calorie. Now you see it. Now you don't.”

DAD: Son, what's the matter with you? If you don't stop that noise, you won't be in any commercial. You'll be back in your room practicing penmanship.

AB: Oh, Diet Pepsi one small calorie. Now you see it. Now you don't . . . (trailing off) This muted me, briefly. Long enough to contemplate his sudden death and wonder how I would ever be able to produce convincing tears. Onions, I'd heard, could do the trick if you applied just a small bit of the juice under your eye. I tried this myself, thrilled with the weepy, sincere results: (dramatically) Oh Dad! Boo-hoo-hoo. *****The next day at filming****

DIRECTOR: (angrily) CUT! Why is this so hard for you? All you have to do is say 'Hey, Mark, where are you going?' That’s all you have to say. Why are you having so much trouble with this?

AB: I don't know. Something is throwing me out of character.

DIRECTOR: What are you talking about You’re a kid in a school. . . playing a kid in a school!

AB: We’d been shooting for over an hour. It was a simple setup: I was walking behind a group of other kids when I suddenly see my friend, Mark. I pause, turn toward the camera without looking at it and say, "Hey, Mark, where are you going?" But I just couldn't do it. Each time I spoke my line, my voice sounded forced, pretentious, dishonest. These were concepts I'd gleaned from a copy of Acting: A Handbook of the Stanislavski Method, which I'd found on my mother's bookshelf.

The other problem was that I didn't feel I had found my character. Why was I walking down the hall? Was I going to class? Or coming from class? These were essential questions, and the director refused to provide answers.

DIRECTOR: Will you shut up and just walk! ACTION!

AB: And I began my walk down the hallway, fully aware of the camera trained on my every move. I concentrated hard on being normal. But I could feel it happening. Like being the passenger in a car speeding out of control, I was unable to stop myself. (in a high-pitched and overly rehearsed tone of voice) "Hey, Mark, where are you going?"

I waited for the director to again scream "Cut!" but instead there was silence. And then I felt a rush. Had I done it? Had I accidentally done it exactly right? (biting his lip to repress the smile)

DIRECTOR: Forget it. We'll fix it in the edit. This is a wrap! *****Scene change*****

AB: Finally the day arrived. My mother turned on the Today Show, and we watched for nearly an hour before it came on. I saw myself for a split second, in back of a bunch of kids. One girl said, "Hey, let's go get some!" and the scene cut to Mrs. Ames at home serving Tang to her grandchildren for the rest of the commercial. My line had been cut! Mrs. Ames hijacked the commercial!

Depressed, I walked down the hall to my room. (in a natural voice) “Hey, Mark, where are you going?" I realized at once that this is what the director had wanted all along. He didn't want passion, meaning, and nuance. He wanted an ordinary kid who would say six words. I decided, right there. I won't be a child actor for television commercials. Instead, I will be the one who thinks up the commercials in the first place. And then I will hire the director myself, and when he can't make the kid give me a passionate, meaningful, and nuanced performance, I'll fire him.
```

---

## IC-2402: Confessions of a Monolingual Americano

- Title: Confessions of a Monolingual Americano
- Author (byline): Carlos Sanchez
- Work: San Jose Mercury News
- Publisher: Not specified
- Publication date as stated: Wednesday, September 14, 1988
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1021
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carlos Sanchez
Book: San Jose Mercury News
ISBN: Newspaper
Date (Month/Year): Wednesday, September 14, 1988
```

### Introduction (context only: never use it for content warnings)

```text
Despite America’s claim to fame of being the “culture accepting melting pot” of the world, many minorities feel out of place in this country which still has a vaguely white supremacist attitude. This struggle for acceptance is examined in Confessions of a Monolingual Americano by Carlos Sanchez.
```

### Performance text (classify this)

```text
This is National Hispanic Heritage Week, so maybe it’s time I came out of the closet. Despite my Hispanic name and heritage, I can’t speak Spanish.

I’m the product of assimilation. Born American, taught American, I grew up denying I was anything but American.

So I once resented reminders of my ethnic past, reminders I wasn’t as white as some of my friends. My thoughts, my attitudes were the direct result of a decision my parents made long before I was conceived: to teach me basic American values – and to teach them in English.

My mother has a favorite story that illustrates how completely assimilated I was: As a first grader, I got into a fight with a little boy on the way home from school. When my mother found out and demanded to know why, I answered angrily: “Because he called me a Mexican!” I still remember the sting when she laughed and told me that I was.

I grew up in a solidly middle class neighborhood in East El Paso, Texas. Along with neighbors named Archuleta and Lopez, there lived the Bardens and Robertsons. We played hide and seek, went to John Wayne movies and, whenever we could sneak a towel out of the house, flew like Superman. We hated the Cisco kid. I grew up happy. I grew up content. I grew up white.

But as I began attending school, my ethnic innocence was slowly chipped away. I remember the disappointment when, during my first Spanish lesson I discovered my name was already Spanish and didn’t need to be translated.

I remember my daily humiliation when I found burritos instead of sandwiches in my lunch box. I remember the pain when my best friend Ernie announced one day that he didn’t like me anymore because I was Mexican.

From the story of the Alamo, where the villainous Mexicans killed those brave Texans, to the Clint Eastwood westerns, where a filthy Mexican lit a match by striking it against his rotting teeth, I learned to be ashamed of my culture.

And nowhere was that shame more apparent than with my grandmother. Mama, we’d call her, Juana Galavia de Escobar. Now ninety-five years old. Born an American citizen in 1893 in the Arizona territory. Moved to Mexico as a young bride of fifteen. Widowed three years later. Entered nursing. Got swept up in the Mexican Revolution. Married again. Returned to the United States.

Despite her citizenship, everything about this lady echoed of Mexico. From the food she ate to the saints she worshipped to the language she spoke, Mama was a constant reminder of a culture that I wanted no part of. We’d visit her weekly against my will.

She lived in a musty smelling adobe house in a rough, lower-class neighborhood that, save for the black family next door, was exclusively Mexican. Often, the only value these visits held for me was Mama’s back yard, a big, wonderful, dirt yard where entertainment possibilities were endless.

But to get to that back yard, I had to go through the kitchen, past Mama. I could never get by without her laughing at me. She’d stop me, then barrage me with incomprehensible questions or orders.

My bewilderment only seemed to make her laugh more. “Don’t you understand her?” my mother would ask, and, of course I couldn’t. I couldn’t speak Spanish. It’s taken me at least twenty years to understand why she was so amused. And I was only able to understand when I saw the situation from her perspective. Here was this little Mexican kid who thought he was white.

By the time I attended high school there was no denying my culture. But I still related to whites better than other Hispanics. I was a coconut, brown on the outside, white on the inside.

They were years of discovery, especially in a border town where all the vice money could buy – even for wide-eyed fifteen year olds – was just a car’s drive away in the red light district of the Mexican city of Juarez.

Even the negative images about my culture fed my psyche. Within the confines of the strip joints, sleaze bars and brothels that we visited regularly, every Mexican woman was a potential whore and every Mexican man was a potential thief.

It was with those experiences, inbred over eighteen years, that I left El Paso for college – and discovered what it really meant to be Mexican. It began with the realization that the people I gravitated towards, the environment that I felt the most comfortable with, the lifestyles that were most familiar, were white.

I realized, too, that relating to these whites was easy for me, not so for them. Not only was I Mexican, but I was one of a handful of Mexicans in my classes. Not only was I different, but I was the object of the very scorn that I had reserved for other Mexicans throughout my youth.

So I began to fight back. It began with a story I wrote for the college newspaper, detailing my experiences as I went through a fraternity rush in an attempt to join the rich, elitist organizations that were so often polarized from the rest of the campus.

The indignities I suffered, highlighted by being completely doused by buckets of beer as I stood in front of a group of laughing fraternity members, were etched into my psyche as permanent scars.

In the face of incidents such as these, it was self-defeating to be ashamed of my culture. To take shame in my background was to perpetuate the viciousness of these people’s attitudes.

To this day, I often feel like a lesser Hispanic, because I don’t speak Spanish fluently. The irony of that fact would make Mama laugh heartily, because the very assimilation that helped me succeed in my life is also working to undermine me.

The pressure to retain the language of my culture is now as powerful as the pressure to conform to the American culture. My parent’s generation needed night school to learn English. I need it to learn Spanish.
```

---

## IC-2403: Count Dracula

- Title: Count Dracula
- Author (byline): Woody Allen
- Work: The Complete Prose of Woody Allen; Pgs 238-244
- Publisher: Wings Books
- Publication date as stated: March 1991
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, BAKER’S WIFE, BAKER, DRACULA, MAYOR, KATIA
- Teaser before the introduction: Yes
- Spoken words (computed): 990
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: The Complete Prose of Woody Allen; Pgs 238-244
ISBN: 978-0517072295
Publisher: Wings Books
Date (Month/Year): March 1991
```

### Introduction (context only: never use it for content warnings)

```text
Now and then, everybody has a bad day. I bet even Mother Theresa felt cross sometimes. It happens to everyone.

You know you’re having a bad day when . . .

• You call your wife and tell her that you would like to eat out tonight and when you get home there is a sandwich on the front porch.

• Your 4-year-old tells you that it's almost impossible to flush a grapefruit down the toilet. • Today’s the day of the total eclipse, and no one reminded you . . . What’s wrong with that you ask? Nothing unless you are

Count Dracula by Woody Allen
```

### Performance text (classify this)

```text
NARRATOR: (Pg 238-244) Somewhere in Transylvania, Dracula the monster is sleeping in his coffin, waiting for night to fall. As exposure to the sun’s rays would surely cause him to perish, he stays protected in the satin-lined chamber bearing his family name in silver. Then the moment of darkness comes, and through some miraculous instinct the fiend emerges from the safety of his hiding place and, assuming the hideous forms of the bat or the wolf, he prowls the countryside, drinking the blood of his victims. Finally, before the first rays of his archenemy, the sun, announce a new day, he hurries back to the safety of his hidden coffin and sleeps, as the cycle begins anew.

NARRATOR: (simultaneously pantomime the narration as Dracula) Now he starts to stir. The fluttering of his eyelids are a response to some age-old, unexplainable instinct that the sun is nearly down and his time is near. Tonight, he is particularly hungry as he lies there, fully awake now, in red-lined Inverness cape and tails, waiting to feel with uncanny perception the precise moment of darkness before opening the lid and emerging, he decides who this evening’s victims will be. The baker and his wife, he thinks to himself. Succulent, available, and unsuspecting. The thought of the unwary couple whose trust he has carefully cultivated excites his blood lust to a fever pitch, and he can barely hold back these last seconds before climbing out of the coffin to seek his prey.

Suddenly he knows the sun is down. Like an angel of hell, he rises swiftly, and changing into a bat, flies pell-mell to the cottage of his tantalizing victims.

BAKER’S WIFE: (opening the door) Why, Count Dracula, what a nice surprise.

NARRATOR: He has once again assumed human form, charmingly concealing his rapacious goal.

BAKER: What brings you here so early?

DRACULA: Our dinner date. I hope I haven’t made an error. You did invite for tonight, didn’t you?

BAKER: Yes, tonight, but that’s not for seven hours.

DRACULA: (looking around the room puzzled) Pardon me?

BAKER: Or did you come to watch the eclipse with us?

DRACULA: Eclipse?

BAKER: Yes. Today’s the total eclipse.

DRACULA: What?

BAKER: A few moments of darkness from noon until two minutes after. Look out the window.

DRACULA: (with rising panic that he tries to mask) Uh-oh. I’m in big trouble.

BAKER: Eh?

DRACULA: And now if you’ll excuse me . . .

BAKER: What, Count Dracula?

DRACULA: (Frantically fumbling for the doorknob) Must be going-aha-oh god . . .

BAKER: Going? You just came.

DRACULA: Yes-but-I think I blew it very badly . . .

BAKER: Count Dracula, you’re pale.

DRACULA: Am I? I need a little fresh air. It was nice seeing you . .

BAKER: Come. Sit down. We’ll have a drink.

DRACULA: Drink? No, I must run. Er-you’re stepping on my cape.

BAKER: Sure. Relax. Some wine.

DRACULA: Wine? Oh no, gave it up-liver and all that, you know. And now I really must buzz off. I just remembered, I left the lights on in the castle -- bills’ll be enormous. . .

BAKER: (putting his arm around the Count in friendship) You’re not intruding. Don’t be so polite. So you’re early.

DRACULA: Really, I’d like to stay but there’s a meeting of old Romanian counts across town and I’m responsible for the cold cuts.

BAKER: Rush, rush, rush. It’s a wonder you don’t get a heart attack.

DRACULA: Yes, right-and now-

BAKER’S WIFE: I’m making chicken pilaf tonight. I hope you like it.

DRACULA: (smiling and pushing her aside) Wonderful, wonderful. (opens a closet door by mistake and walks in) Christ. Where’s the front door?

BAKER’S WIFE: (laughing) Ach, such a funny man, the count.

DRACULA: (forcing a chuckle) I knew you’d like that. Now get out of my way. (opens the front door and panics at the sunlight)

BAKER: Oh, look, the eclipse must be over. The sun is coming out again.

DRACULA: (slamming the front door) Right. I’ve decided to stay. Pull down the window shades quickly-quickly! Let’s move it!

BAKER: What window shades?

DRACULA: There are none, right? Figures. You got a basement?

BAKER’S WIFE: (affably) No, I’m always telling Jarslov to build one but he never listens. That’s some husband, my Jarslov.

DRACULA: I’m all choked up. Where’s the closet?

BAKER: You did that one already, Count Dracula. Unt mama and I laughed at it.

BAKER’S WIFE: Ach-such a funny man, the Count.

DRACULA: Look, I’ll be in the closet. Knock at seven-thirty.

(he steps in the closet and slams the door)

BAKER’S WIFE: Hee-hee--he is so funny, Jarslov.

BAKER: Oh, count. Come out of the closet. Stop being a big silly.

DRACULA: (from inside the closet comes the muffled voice of Dracula) Can’t. Please. Take my word for it. Just let me stay here. I’m fine. Really.

BAKER: Count Dracula, stop the fooling. We’re already helpless with laughter.

DRACULA: Can I tell you, I love this closet.

BAKER: Yes, but . . .

DRACULA: I know, I know . . . It seems strange, and yet here I am, having a ball. I was just saying to Mrs. Hess the other day, give me a good closet and I can stand in it for hours. Sweet woman, Mrs. Hess. Fat, but sweet . . . Now, why don’t you run along and check back with me at sunset.

NARRATOR: Now the mayor and his wife, Katia, arrive. They are passing by and have decided to pay a call on their good friends, the baker and his wife.

MAYOR: Hello, Jarslov. I hope Katia and I are not intruding?

BAKER: Of course not, Mr. Mayor. Come out, Count Dracula. We have company!

MAYOR: (surprised) Is the count here?

BAKER’S WIFE: Yes, and you’ll never guess where.

MAYOR: It’s so rare to see him around this early. In fact, I can’t ever remember seeing him around in the daytime.

BAKER’S WIFE: Well, he’s here. Come out, Count Dracula!

KATIA: Where is he?

BAKER’S WIFE: (impatiently) Come on out now! Let’s go!

BAKER: (apologetically) He’s in the closet. (knocking on the door) Let’s go. Enough is enough. The mayor’s here.

MAYOR: Come on out, Dracula. Let’s have a drink.

DRACULA: No, go ahead. I have business in here.

MAYOR: In the closet?

DRACULA: Yes, don’t let me spoil your day. I can hear what you’re saying. I’ll join in if I have anything to add.

NARRATOR: Everyone looks at one another and shrugs. Wine is poured and they all drink.

MAYOR: Some eclipse today.

BAKER: Yes. Incredible.

DRACULA: Yeah. Thrilling.

BAKER: What, Dracula?

DRACULA: Nothing, nothing. Let it go.

NARRATOR: And so some time passes, until the mayor can stand it no longer.

MAYOR: (forcing open the door to the closet, he shouts) Come on, Dracula. I always thought you were a mature man. Stop this craziness.

NARRATOR: The daylight streams in, causing the evil monster to shriek and slowly dissolve to a skeleton and then to dust before the eyes of the people present.

MAYOR: (Leaning down to the pile of white ash on the closet floor) Does this mean dinner is cancelled?
```

---

## IC-2404: Cubs

- Title: Cubs
- Author (byline): Patrick F. McManus
- Work: The Good Samaritan Strikes Again, Pgs 61-74
- Publisher: MacMillan
- Publication date as stated: Aug 1993
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: PATRICK, MR. TIDDLE, SCOUTS, ATTILA, PORKY, DANNY, TONY, LUCIFER, PEEWEE, GROVER, MRS. SLOCUM
- Teaser before the introduction: Yes
- Spoken words (computed): 1866
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick F. McManus
Book: The Good Samaritan Strikes Again, Pgs 61-74
ISBN: 978-0805029222
Publisher: MacMillan
Date (Month/Year): Aug 1993
```

### Introduction (context only: never use it for content warnings)

```text
Scouting has come a long way over the years. Today, the Boy Scouts has made strides to become more inclusive. Cub Scouts is, and I quote, “a program for children (both boys and girls) in kindergarten through fifth grade and their families that encourages learning, friendship—and most of all—getting out and having fun!”

But when Patrick McManus was a cub scout, it was boys ONLY and they used the word FUN too! Those were the days when FUN may have been more loosely defined. But seriously: a 5-mile hike with a backpack that weighed more than you and skinny-dipping in a frozen lake does not fit the FUN definition! Cubs by Patrick F. McManus
```

### Performance text (classify this)

```text
PATRICK: (Pg 61-74) I like to think I was just as good a Cub Scout as the next guy, the next guy being Grover Finch, who was about as miserable a Cub Scout as ever tied a granny knot and called it square. Our den could boast of boys clearly cut out for the scouting life, but I wasn’t one of them. Neither was Grover. He dropped out of Cubs shortly after the strange incident at Camp Muskrat. I think he may have received a dishonorable discharge, but I don’t know for sure.

PATRICK: One day in early spring, the scoutmaster of the local troop showed up at our [cub scout] meeting. Mr. Tiddle was a robust outdoorsman, shaped something like a barrel, but all bone and muscle. He lifted weights and did calisthenics just for the fun of it, but the strangest thing was that every New Year’s Day he would chop a big hole in the ice and plunge into the frigid water of Lake Blight.

MR. TIDDLE: (booming) Boys, I’ve got great news for you. A couple of the scouts from Troop Nine-oh-seven and I are going to take you Cubs on an overnight outing to Camp Muskrat this Saturday. How does that sound?”

PATRICK: We broke into cheers, with Grover cheering the loudest of all.

MR. TIDDLE: You all show up at the school at eight o’clock Saturday, and we’ll issue you sleeping bags and packs. For supper, we’ll treat you to a wiener roast.

SCOUTS: Yayyyyyyyy!

PATRICK: The next Saturday morning, about fifteen of us Cubs assembled at the grade school. Several station wagons were parked nearby. We assumed they were there to transport us to Camp Muskrat, located on a small lake five miles from town. Then we noticed that volunteered fathers were loading the station wagons with tents and other gear and supplies. We watched as the station wagons departed one by one, until none were left for us. Mr. Tiddle and two Boy Scouts, all three in their starched tan uniforms, strode briskly over to us.

MR. TIDDLE: (bellowing enthusiastically) Listen up, Cubs! We have a real treat for you. Scouts Lucifer and Attila have volunteered to serve as your leaders on the campout, and they have come up with a marvelous idea. Instead of riding to Camp Muskrat, you get to practice your hiking skills all the way out to the camp. Let’s have a big hand for these fine scouts.

PATRICK: (less than enthusiastic clapping) We stared up at the towering scouts, both of whom smiled benevolently down on us.

MR. TIDDLE: I leave you in their care. See you all at Camp Muskrat.

PATRICK: He got into his car and drove away. The two scouts watched his car until it disappeared around a corner. When they turned back to us, we were shocked. They had gown fangs and claws and their eyes glowed red with fiery light! We could tell from their gleefully evil expressions this was an opportunity they had waited for all their lives.

ATTILA: (mean and threatening) Hoist your packs and line up according to height, shrimps! No talking! Move it! Move it!

PATRICK: Startled, we hoisted our packs and scrambled into a ragged line.

PORKY: Hey, I just remembered. I’m supposed to go to the dentist today! See you guys later.

DANNY: I have to go to the bathroom. Be right back.

TONY: Me too. Be gone just a second.

LUCIFER: (snarling) Shut up, shrimps! Back in formation!

PATRICK: The would-be deserters shrank back into line.

LUCIFER: (screaming) Left face!

ATTILA: (bellowing) Forwarrrrrd! March! Hut two three four, hut . . .

PATRICK: Attila brought up the rear, apparently for the purpose of harrying the stragglers and shooting the wounded.

PEEWEE: (croaking) How much farther is it?

LUCIFER: (shouting) Four miles to go! Now close up that line! Hut two three four . . .

PATRICK: The hot spots of blisters began to glow inside our tennis shoes. Pack straps gnawed at our shoulders.

GROVER: (muttering) This ain’t a hike. It’s a death march

PATRICK: (to Grover) Somebody is going to pay for this. (to audience) Hours later we limped into Camp Muskrat and dropped to the frozen, snow-blotched ground. The fathers had set up the tents and then vanished with the blinding speed common to fathers volunteered for Cub Scout outings. Mr. Tiddle and the two scouts were now left alone with fifteen exhausted but surly Cubs, who sprawled in ominous silence, sullenly watching Attila, Lucifer, and Mr. Tiddle job about gathering wood for the evening campfire. The scouts and scoutmaster joked and laughed as if they hadn’t a care in the world. The air, however, was heavy with suspense, dark with foreboding. I crawled over to the remains of Grover and Peewee. (to Grover) Come up with anything for Lucifer and Attila yet?

GROVER: I’m thinking, I’m thinking. Everything I come up with is either too kind or too complicated. We need something simple but mean. I suppose we could steal their clothes so they would have to run around naked in the cold and maybe catch pneumonia and suffer horribly for a long time and then die terrible agonizing deaths.

PATRICK: The sun sank behind Muskrat Mountain, and a breeze wafted in off Muskrat Lake, chilled by rafts of sludgy ice still drifting about the surface. We put on sweaters and even coats and gathered around the fire that Lucifer and Attila had built into a small inferno. This was more like it.

PEEWEE: Are we camping yet?

PATRICK: Suddenly, Mr. Tiddle erupted from his tent with a towel thrown over his shoulder.

MR. TIDDLE: Any of you Cubs like to join me for a dip in the lake? What, no takers? (to Lucifer and Attila) How about you scouts? Like to refresh yourselves with a dip before supper? There’s a nice sandy beach down the shore a ways, and we don’t even have to chop through the ice. Just shove it out of the way.”

ATTILA: (shuddering) Why, we’d sure like to Mr. Tiddle. Sounds wonderful. But darn it all, we didn’t bring our bathing trunks.

MR. TIDDLE: (bellowing) Me neither. Ever hear of skinny-dipping? C’mon, lads. Race you out to the floating dock!

LUCIFER: (whining) Wow, okay then, Mr. Tiddle. Attila and I’ll be right there, as soon as we grab some towels. Hope we can find you in the dark.

PATRICK: The two scouts slouched off. We Cubs edged closer to the toasty campfire.

GROVER: This is too good to be true. Be back in a bit.

PATRICK: And [he] slipped off into the shadows. Scarcely had Grover vanished when the plot thickened. The headlights of a car illuminated the Camp Muskrat parking area for a moment, and soon Mrs. Slocum (our den mother) and another lady came picking their way down a trail to the campfire.

MRS. SLOCUM: Good evening, Cubs! You look like you’re having a wonderful time. I’m so glad! I think you all know my good friend Mrs. Teasdale. We thought we would join you for the wiener roast. Brought you a treat – marshmallows!

SCOUTS: Yayyyyyyy!

PATRICK: We pulled up a log for the ladies to sit on next to the fire. Just then Grover emerged from the woods, slapping his way through a cloud of mosquitoes.

GROVER: (whispering to Patrick) Snatched only one set of clothes and a towel. Was all I could find in the dark. I could hear them splashing around not too far from shore and thought they might spot me. Slipped the clothes into their tent. But either Lucifer or Attila is going to be in for a big surprise!

PATRICK: We sat around the fire telling ghost stories, but nothing compared to the horror that awaited us. Sooner than expected, Lucifer came rushing into the light of the fire.

LUCIFER: Wow, you guys are smarter than you look. That water is liquid ice. Just lucky I had the good sense to test it with my toe first– why, hello there, Mrs. Slocum, Mrs. Teasdale. Didn’t know you were coming for a visit.

GROVER: (whispering to Patrick and snickering) Attila’s the one. This could be good.

PATRICK: A minute later, Attila bounded into camp – fully clothed!

ATTILA: Wheweeee, that water’s cold! Chickening out is the better part of valor, I always say. I don’t know how Mr. Tiddle can stand it.

PATRICK: Grover stared grimly at Lucifer and Attila. Minutes dragged by. We sang a camp song. Mrs. Slocum and Mrs. Teasdale told about when they were little girls and had picked huckleberries in the hills above Camp Muskrat. And then . . . The monster roared out of the darkness so suddenly that several Cubs almost inhaled flaming marshmallows. For a moment I thought it was a Sasquatch, but it turned out to be Mr. Tiddle. He was stark naked, except for a little cedar bough he had twisted off a tree.

MR. TIDDLE: (booming) So, the old steal-the-clothes trick!

GROVER: (whispering to Patrick) I thought this might happen. You can have my bike and baseball glove if you want them.

PATRICK: (to Grover) Thanks, Grover. Hey, it’s been fun knowing you. (to audience) Then a surprising thing happened. Mr. Tiddle grabbed Lucifer and Attila by the hair, one with each hand.

MR. TIDDLE: Ha! Just as I suspected – hair’s not even wet! Well, I’ll just have to see what I can do about that.

ATTILA: Wait! LUCIFER: It wasn’t . . !

MR. TIDDLE: Oh, it wasn’t, was it? Well, we’ll just check your tent and see if we don’t find my clothes there.

PATRICK: Mr. Tiddle dragged the two scouts over to check their tent.

LUCIFER: See, your clothes aren’t . . . . NOOOOOOOO!

MR. TIDDLE: Aha! You two scalawags thought you could pull a fast one on me, did you?

PATRICK: He snatched up each of the scouts by the back of the belt and charged off toward the lake, one in each meaty hand. The screams were among the best and most satisfying I’ve ever heard, starting low and quavering but then rising in pitch and volume while still conveying great feeling and intensity right up to the moment of total immersion. We Cubs all agreed the performance was highly entertaining, spiritually enriching, and well worth a forced march. Recovering his little cedar branch, Mr. Tiddle strolled back to the fire chortling.

MR. TIDDLE: Please excuse my nudity for a minute, boys. I just wanted to make a point about practical jokes – oh, nice to see you, Mrs. Slocum, Mrs. Teasdale. Didn’t expect you ladies out this evening. The point I was making to the Cubs here is that people can play their little pranks, but in the end they have to pay the pipe – Ladies?

PATRICK: His lips froze in a grotesque smile over his big white teeth. He hunched over and tried to conceal himself behind the little bough. I sure would have felt embarrassed if I’d been standing there naked except for a little cedar bough and suddenly realized two ladies were sitting not ten feet away.

PEEWEE: Yeah. Then, as if that wasn’t bad enough, dumb ol’ Terry accidentally flicks his flaming marshmallow onto the cedar bough. That ol’ bough must have been dry as gunpowder, to flare up like that. Poor Mr. Tiddle,

PATRICK: I think both Mrs. Slocum and Mrs. Teasdale handled it pretty well. It was nice how they pretended not to notice Mr. Tiddle because of concentrating so hard on twirling their sticks over the coals, just as if roasting wieners was the most important thing in the world to them.

PEEWEE: It would have been better if they hadn’t let their wieners burn off and fall in the fire, though. They didn’t even seem to notice. Just sat there twirling them empty sticks round and round, an all the while Mr. Tiddle’s roaring and darting about like a madman.

PATRICK: Well, I guess that’s camping!
```

---

## IC-2405: The Cult

- Title: The Cult
- Author (byline): Jon Stewart
- Work: Naked Pictures of Famous People, Pg 81-92
- Publisher: Harper Collins
- Publication date as stated: Oct 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ME, LT JOHNSON, LT MCSHANE, LIEUTENANT JOHNSON, OTHER ROOM, FOLLOWER #1, FOLLOWER #3, FOLLOWER #4, FOLLOWER #2
- Teaser before the introduction: Yes
- Spoken words (computed): 1287
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jon Stewart
Book: Naked Pictures of Famous People, Pg 81-92
ISBN: 978-0688171629
Publisher: Harper Collins
Date (Month/Year): Oct 1999
```

### Introduction (context only: never use it for content warnings)

```text
The Cult by Jon Stewart
```

### Performance text (classify this)

```text
ME: (PG 81-92) (to audience) Considering the many feats of leadership in the twentieth century, from Churchill's morale-rallying speeches in World War II to Martin Luther King Jr.'s marches for racial equality during the sixties, the ones that I find most impressive are the Jonestown Massacre and Heaven's Gate. While Churchill and King inspired loyalty and devotion, they had the benefit of real issues and problems to play on. Getting people to buckle down during World War II or walk a couple of blocks with you on a sunny day in Alabama are impressive indeed, but getting people to kill themselves for no reason other than you think you saw something about it in a dream? (makes an impressed and wonder-filled “humph”)

Me . . . persuasive leader of a messianic cult? Would I have the strength? Would I be able to overcome my fear of death, zealous crowds and death by zealous crowds? Would I understand the intricacies of forming a tax-exempt organization?

ME: (to audience) We begin in the back room of my cult's compound – also known as my rent-controlled one-bedroom. My subjects have congregated on this day to witness our salvation. I have foretold a vision of the Rapture. At 4:00 P.M., Captain Crunch will spring to life from his resting place on the back of a cereal box and deliver us to our eternal bliss. It is 3:56 P.M.

LT JOHNSON: Leader . . . What a glorious day for our deliverance!

ME: (distracted by the time) Yes, yes. The day is glorious, although they say tomorrow's pollen count will be moderate to heavy.

LT JOHNSON: What care we of tomorrow, when salvation is but four minutes away.

ME: I'm just saying I would hate to go to our salvation with red itching eyes.

LT MCSHANE: But the Captain will deliver us from our earthly afflictions. You said!

LT JOHNSON: He knows what he said. Why must you always nag? He knows we --

ME: Fellas, please. With the air conditioning out, the last thing I need is the two of you making a ruckus.

LIEUTENANT JOHNSON: Tell us again, for the last time, the story of Captain.

ME: All right. But then you both have to finish unloading the dishwasher like I asked you yesterday.

LT JOHNSON: We're sorry, Leader. We just thought that with the Captain coming . . .

LT MCSHANE: We would have no more use for earthly dishes.

ME: So you want the Captain to eat off dirty dishes. Our savior of saviors, and you can't take the time?

LT MCSHANE: Were sorry, Leader. Please forgive our sinful ways. (They begin to kiss his feet)

ME: All right, fine . . . get up. C'mon. You're embarrassing me, you . . . (they get up) Anyhoo. (preaching) The Captain was an all-powerful, benevolent leader. His people lived in a state of constant bliss, with a little sugar rush thrown in for good measure. One day, while his followers were being sinful and lazy and arguing with each other, a mean leprechaun accused the Captain of stealing his Lucky Charms. The leprechaun put a spell on the Captain, confining him until the righteous among us could pull the sword from the rock, showing the Captain we were worthy of receiving his good graces.

LT JOHNSON: Leader? I have a question. If the Captain is all-powerful . . . How could the leprechaun put a spell on him?

LT MCSHANE: And what of the sword? I mean, I don't want to nitpick, but you never mentioned the sword before.

ME: You're gonna do this now? Huh? Three . . . two minutes to salvation and you're gonna do this now? Maybe you guys should have thought of this before you signed up, because if you're gonna nitpick, I got a living room filled with believers that would love to be lieutenants. Remember, at Salvation, the lieutenants get to carry the Captain's hat.

LT MCSHANE: No, Leader. Please don't be angry. It's just . . . I had never heard that thing about the sword before.

ME: Well, I just remembered it. Besides, you had no trouble swallowing the cereal box come to life part.

LT MCSHANE: That's true.

LT JOHNSON: And when the Captain comes he will relieve our earthly afflictions?

ME: Bingo.

LT JOHNSON: This cursed cleft chin will finally be gone.

ME: I keep telling you. That's considered a positive feature.

LT MCSHANE: And what of my leprosy?

ME: Your what? I thought that was dermatitis.

LT MCSHANE: (Showing his arms) This is dermatitis. (Lifting up his shirt) This is leprosy.

ME: Oh, my God (furiously rubbing his exposed skin) I hugged you in the Circle of Knowledge yesterday! Please get off the chair, nothing personal. I just had them redone and it cost a fortune . . . and I'll take the drinking glass, please . . . thank you.

OTHER ROOM: (From the other room a group chant begins.) CAPTAIN, WE ARE READY. 10 – 9 – 8. . .

ME: My watch still says 3:58. Imitation Rolex. (bangs watch on the table and puts it to his ear)

LT JOHNSON: Come, Leader, let us join the others so the Captain will see our solidarity.

ME: You guys go. I still have that . . . thing . . . in the oven. Wouldn't want the Captain's chicken to get dry.

LT MCSHANE: All right. See you in Nirvana. (They exit)

OTHER ROOM: (The chant goes on) 3 – 2 – 1 . . . (Then all is silent. The silence endures ... and then the Lieutenants re-enter the room)

LT JOHNSON: Uhh, Leader . . . can we have a word with you, please?

ME: Huh. Oh! Hey, how's the Captain?

LT MCSHANE: Everyone would like a word with you in the front . . . now.

ME: Sure, sure. (he is dragged into the front room) Hey, everybody! What can I do you for?

FOLLOWER #1: It is 4:02. And still the Captain remains on the box. Smirking at us.

ME: 4:02. Right. (frantically thinking of an explanation) Right . . . Oh my God. It's Daylight Saving Time, isn't it? In the Land of Plenty it's still 3:02. Silly mistake. I can't believe I --

FOLLOWER #1: You lied to us, Leader. You took advantage of us.

ME: Now let's not start hurling accusations. I mean, who among us can really cast the first stone? Lying, taking advantage. Those are serious allega . . . (A clamor arises from the followers) All right now, settle down, people. Remember, I'm still the one making up the seating chart for the rocket ship (They quiet) Heh, heh. Well. (beat) Are we out of onion dip? Let me run out and grab some quick, because the Captain's going to be here in about (checking watch) fifty-five minutes and you know he'll be hungry and . . . (They surround him ominously) Hey, c'mon. Why the long faces? The Captain's a little late. Christ. The guy's been on a box for . . .

FOLLOWER #3: You took all I had in the world. You destroyed my family. All I did was ask you for directions and before I knew what hit me, you had ruined me with your lies of a promised land of Crunchberries and honey . . .

FOLLOWER #4: Get him!! (General mayhem ensues. Lamps break, feelings are hurt.)

ME: People, please! Settle down! Now listen. I know you're disappointed that the Captain didn't show us the way to eternal salvation, but we still have cable till the end of the month, so let's show a little restraint here.

LT JOHNSON: Perhaps the Captain knew there were skeptics among us. Perhaps this is why he has forsaken us.

ME: Boom! Exactly. Couldn't have put it better myself. Damn skeptics. Maybe if you people hadn't balked at the bathroom tax none of this would . . .

LT MCSHANE: A suicide pact will convince the Captain of our sincerity. A suicide pact led by our leader. The Leader will die and we shall follow!

ME: Whoa. Whoa. Slow down there, chief. I mean, suicide . . . we could get in a lot of trouble for that.

LT JOHNSON: Suicide is the only Way!

ME: You never heard of a letter-writing campaign? Stop. This is madness! (The crowd hushes at his fervor)

FOLLOWER #1: You're stalling.

FOLLOWER #2: You're a staller and a liar.

ME: Look. You're all really mad at me, but . . . You wanted this. You needed this. It was your weakness that made this all possible. You didn't want to take responsibility for your own lives. You had to look to a savior to make it all better for you. I didn't do this to you, you did it to yourselves. You wanted to believe in an easy solution to the complex stresses and anxieties of your lives. I saved you from yourselves. (All is quiet in the room, then a warlike shriek goes up and the mob attacks)

Wait! Stop! Ow! Don't pull, it's not a toupee! . . .

(suddenly pointing to the cereal box) Oh my God! It's THE CAPTAIN! (The room goes silent as all eyes shift to the cereal box – a long beat; then he speaks with conviction) See? Do you see! The Captain hasn't moved, but for that one brief moment, we all believed again. We all believed in the possibility of our salvation. (Heads nodding, the believers are contemplating – He begins to back away toward the exit) Remember those days. The believing days. Those were good times. . . (He runs out with the crowd in hot pursuit)
```

---

## IC-2406: Cyclops

- Title: Cyclops
- Author (byline): David Sedaris
- Work: Naked
- Publisher: Little Brown and Company
- Publication date as stated: March 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2105
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Sedaris
Book: Naked
ISBN: 978-0316779494
Publisher: Little Brown and Company
Date(Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
This is going to hurt me more than it hurts you. . . .Just tell me the truth and you won't get in trouble.. . . When I was your age I walked 10 miles to school, up hill both ways, in the snow. . . .

I am sure most of us grew up thinking some of the things that our parents said were actually true. In reality, many were white lies that they told us to trick us into doing or believing something or better yet, to stop us from doing something!

David Sedaris’ father was no different . . . . . but the parental phrase “You’ll put your eye out!” became a much more involved story entitled Cyclops by David Sedaris.
```

### Performance text (classify this)

```text
When he was young my father shot out his best friend's eye with a BB gun. That is what he told us. "One foolish moment and, Jesus, if I could take it back, I would." He winced, shaking his fist as if it held a rattle. "It eats me alive," he said. "I mean to tell you that it absolutely tears me apart."

On one of our summer visits to his hometown, my father took us to meet this guy; a shoe salesman whose milky pupil hugged the corner of his mangled socket. I watched the two men shake hands and turned away, sickened and ashamed by what my father had done.

Our next-door neighbor received a BB gun for his twelfth birthday and accepted it as a personal challenge to stalk and maim any living creature: sunbathing cats, sparrows, slugs, and squirrels - if it moved, he shot it. I thought this was an excellent idea, but every time I raised the gun to my shoulder, I saw my father's half-blind friend stumbling forth with an armload of Capezios. What would it be like to live with that sort of guilt? How could my father look himself in the mirror without throwing up?

While watching television one afternoon my sister Tiffany stabbed me in the eye with a freshly sharpened pencil. The blood was copious, and I rode to the hospital knowing that if I was blinded, my sister would be my slave for the rest of her life. Never for one moment would I let her forget what she'd done to me. There would be no swinging cocktail parties in her future, no poolside barbeques or episodes of carefree laughter, not one moment of joy - I would make sure of that. I'd planned my vengeance so thoroughly that I was almost disappointed when the doctor announced that this was nothing but a minor puncture wound, located not on but beneath the eye.

"Take a look at your brother's face," my father said, pointing to my Band-Aid. "You could have blinded him for life! Your own brother, a Cyclops, is that what you want?" Tiffany's suffering eased my pain for an hour or two, but then I began to feel sorry for her. "Every time you reach for a pencil, I want you to think about what you've done to your brother," my father said. "I want you to get on your knees and beg him to forgive you."

There are only so many times a person can apologize before it becomes annoying. I lost interest long before the bandage was removed, but not my father. By the time he was finished, Tiffany couldn't lift a dull crayon without breaking into tears. Her pretty, suntanned face assumed the characteristics of a wrinkled, grease-stained bag. Six years old and the girl was broken.

Danger was everywhere and it was our father's lifelong duty to warn us. Attending the country club's Fourth of July celebration, we were told how one of his Navy buddies had been disfigured for life when a cherry bomb exploded in his lap. "Blew his balls right off the map," he said. "Take a second and imagine what that must have felt like!" Racing to the farthest edge of the golf course, I watched the remainder of the display with my hands between my legs.

Fireworks were hazardous, but thunderstorms were even worse. "I had a friend, used to be a very bright, good-looking guy. He was on top of the world until the day he got struck by lightning. It caught him right between the eyes while he was trout fishing and cooked his brain just like you'd roast a chicken. Now he's got a metal plate in his forehead and can't even chew his own food; everything has to be put in a blender and taken through a straw."

If the lightning was going to get me, it would have to penetrate walls. At the first hint of a storm I ran to the basement, crouching beneath a table and covering my head with a blanket. Those who watched from their front porches were fools. "The lightning can be attracted by a wedding ring or even the fillings in your teeth," my father said. "The moment you let down your guard is guaranteed to be the day it strikes."

In junior high I signed up for shop class, and our first assignment was to build a napkin holder. "You're not going to be using a table saw, are you?" my father asked. "I knew a guy; a kid about your size, who was using a table saw when the blade came loose, flew out of the machine, and sliced his face right in half." Using his index finger, my father drew an imaginary line from his forehead to his chin. "The guy survived, but nobody wanted anything to do with him. He turned into an alcoholic and wound up marrying a Chinese woman he'd ordered through a catalog. Think about it." I did.

My napkin holder was made from found boards and, once finished, weighed in at close to seven pounds. My bookshelves were even worse. "The problem with a hammer," I was told, "is that the head can fly off at any moment and, boy, let me tell you, you've never imagined pain like that."

After a while we began to wonder if my father had any friends who could still tie their own shoes or breathe without the aid of a respirator. With the exception of the shoe salesman, we'd never seen any of these people, only heard about them whenever one of us attempted to deep-fry chicken or operate the garbage disposal. "I've got a friend who buys a set of gloves and throws one of them away. He lost his right hand doing the exact same thing you're doing. He had his arm down the drain when the cat rubbed against the switch to the garbage disposal. Now he's wearing clip-on ties and having the restaurant waiters cut up his steak. Is that the kind of life you want for yourself?"

He allowed me to mow the lawn only because he was too cheap to pay a landscaper and didn't want to do it himself. "What happened," he said, "is that the guy slipped, probably on a pile of crap, and his leg got caught up in the blade. He found his foot, carried it to the hospital, but it was too late to sew it back on. Can you imagine that? The guy drove fifteen, twenty miles with his foot in his lap."

Regardless of the heat, I mowed the lawn wearing long pants, knee-high boots, a football helmet, and a pair of goggles. Before starting, I scouted the lawn for rocks and dog feces, slowly combing the area as if it were mined. Even then I pushed the mower haltingly, always fearing that this next step might be my last. Nothing bad ever happened, and within a few years I was mowing in shorts and sneakers, thinking of the supposed friend my father had used to illustrate his warning. I imagined this man jumping into his car and pressing on the accelerator with his bloody stump, a warm foot settled in his lap like a sleeping puppy. Why hadn't he just called an ambulance to come pick him up? How, in his shock, had he thought to search the weeds for his missing foot? It didn't add up.

I waited until my junior year of high school to sign up for driver's education. Before taking to the road, we sat in the darkened classroom, watching films that might have been written and directed by my father. Don't do it, I thought, watching the prom couple attempt to pass a lumbering dump truck. Every excursion ended with the young driver wrapped around a telephone pole or burned beyond recognition, the camera focusing in on a bloody corsage littering the side of the highway.

I drove a car no faster than I pushed the lawn mower, and the instructor soon lost patience.

"That license is going to be your death warrant," my father said on the day I received my learner's permit. "You're going to get out there and kill someone, and the guilt is going to tear your heart out."

The thought of killing myself had slowed me down to five miles per hour. The thought of killing someone else stopped me completely.

My mother had picked me up from a play rehearsal one rainy night when, cresting a hill, the car ran over something it shouldn't have. This was not a brick or a misplaced boot but some living creature that cried out when caught beneath the tire. "Shit," my mother whispered, tapping her forehead against the steering wheel. "Shit, shit shit." We covered our heads against the rain and searched the darkened street until we found an orange cat coughing up blood into the gutter. "You killed me," the cat said, pointing at my mother with its flattened paw. "Here I had so much to live for, but now it's over, my whole life wiped out just like that." The cat wheezed rhythmically before closing its eyes and dying.

"Shit," my mother repeated. We walked door to door until finding the cat's owner, a kind and understanding woman whose young daughter shared none of her qualities. "You killed my cat," she screamed, sobbing into her mother's skirt. "You're mean and you're ugly and you killed my cat."

"She's at that age," the woman said, stroking the child's hair.

My mother felt bad enough without the lecture that awaited her at home. "That could have been a child!" my father shouted. "Think about that the next time you're tearing down the street searching for kicks." He made it sound as if my mother ran down cats for sport. "You think this is funny," he said, "but we'll see who's laughing when you're behind bars awaiting trial for manslaughter." I received a variation on the same speech after sideswiping a mailbox. Despite my mother's encouragement, I surrendered my permit and never drove again. My nerves just couldn't take it. It seemed much safer to hitchhike.

My father objected when I moved to Chicago, and waged a full-fledged campaign of terror when I announced I would be moving to New York. "New York! Are you out of your mind? You might as well take a razor to your throat because, let me tell you something, those New Yorkers are going to eat you alive." He spoke of friends who had been robbed and bludgeoned by packs of roving gangs and sent me newspaper clippings detailing the tragic slayings of joggers and vacationing tourists. "This could be you!" he wrote in the margin.

I'd lived in New York for several years when, traveling upstate to attend a wedding, I stopped in my father's hometown. We hadn't visited since our grandmother moved in with us, and I felt my way around with a creepy familiarity. I found my father's old apartment, but his friend's shoe store had been converted into a pool hall. When I called to tell him about it, my father said, "What shoe store? What are you talking about?"

"The place where your friend worked," I said. "You remember, the guy whose eye you shot out."

"Frank?" he said. "I didn't shoot his eye out; the guy was born that way."

My father visits me now in New York. We'll walk through Washington Square, where he'll yell, "Get a look at the ugly mug on that one!" referring to a three-hundred-pound biker with grinning skulls tattooed like a choker around his neck. A young man in Central Park is photographing his girlfriend, and my father races to throw himself into the picture. "All right, sweetheart," he says, placing his arm around the startled victim, "it's time to get comfortable." r cower as he marches into posh grocery stores, demanding to speak to the manager. "Back home r can get this exact same cantaloupe for less than half this price," he says. The managers invariably suggest that he do just that. He screams at waiters and cuts in line at tony restaurants. "I have a friend," I tell him, "who lost his right arm snapping his fingers at a waiter."

"Oh, you kids," he says. "Not a one of you has got so much as a teaspoon of gumption. I don't know where you got it from, but in the end, it's going to kill you."
```

---

## IC-2407: Daddy’s Little Girl

- Title: Daddy’s Little Girl
- Author (byline): Jason Sheets
- Work: Turning Points, Pgs 153-157
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: DADDY, PRINCIPAL, DOCTOR, KATIE, NURSE
- Teaser before the introduction: Yes
- Spoken words (computed): 1490
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jason Sheets
Book: Turning Points, Pgs 153-157
Publisher: Tichenor Publishing
ISBN: 978-0742117013
Date: 2001
```

### Introduction (context only: never use it for content warnings)

```text
Katie’s favorite song is . . .
```

### Performance text (classify this)

```text
DADDY: (Pgs 153-157) When my daughter came home from school with bruises on her arms and back, I scheduled an appointment with the principal the next day. The principal reassured me:

PRINCIPAL: I can't imagine Katie is having any problems with bullies. She seems to be adjusting to junior high very well.

DADDY: After telling him to keep an eye out, the bruises got darker but the principal reported nothing. I took Katie to the doctor so we could document the bruises . . .

DOCTOR: Sir, I've taken the liberty to run some tests. The bruises are not the result of bullying. Your daughter has leukemia. Do you think we should tell her together?

DADDY: No . . . I'll tell her. (to audience) Katie and I had always done everything one-on-one. Daddy's little girl was about to embark on the fight of her life.

*(sings) Blue skies smilin' at me.
Nothin' but blue skies do I see.
Bluebirds singin' a song.
Nothin' but bluebirds all day long. . .
Blue days, all of them gone.
Nothin' but blue skies from now on.
Blue skies smilin' at me
Nothin' but blue skies do I see . . .
And we did. We tried to see the blue skies every single day
from that moment on.
Daddy’s Little Girl by Jason Sheets

DADDY: I hate diseases that you don't know how serious they are so you have to anticipate both the worst and best case scenarios. Like our neighbor -- diagnosed with Parkinson's disease. You have to say" Oh, I'm so sorry" and then go ask people if there is a cure. My aunt has diabetes. People think she's dying, but she lives a healthy life. We just aren't very informed on what constitutes three strikes.

Leukemia? For leukemia the answer is "kind of" and when you ask if it's three strikes, they make this face that suggests "we'll treat her and find out."

Katie is a daddy's girl by default. Her mother, as much as I love her, spends weeks at a time on assignment as a news reporter. That makes me not only father, but food supervisor, activities director, and special assignment counselor all at once. With only one child, I had the time and was more than willing to do it. Mothers bond during pregnancy; father's bond by choice. Now, sometimes it got awkward. She's a girl, after all. Suddenly, I'm thrown into bake sales:

KATIE: Daddy, can we make something besides Rice Krispie treats?

DADDY: Katie, no, we can't. Trust me, daddy is not possibly capable of more than this. Where's the marshmallow? (to audience) And I'm critiquing ballet recitals: (to Katie) Dear, you were the best. The way you. . . jumped around and all. On your toes! (to audience) Last summer, it was shopping for a training bra. (to Katie) This one looks like it'll provide some support.

KATIE: Dad!

DADDY: How about this colorful one over here?

KATIE: Dad!

DADDY: No matter how much I wasn't capable of handling the job, the job of loving her was my pride and joy. She says I'll be the best man at her wedding. (to Katie) Don't you think your groom should have that choice?

KATIE: Not if he wants to marry me!

DADDY: We talk about everything. Even the leukemia. Treatments come, treatments go. We talk about every moment. At least I think so. She may have moments she keeps for herself. If she does, I'm OK with that.

In the morning, I wake her for school and I hurriedly brush away all the excess hair she has lost during the night. She knows it's gone, but seeing it makes it more real, more final. The summer before she enters 9th grade, we find ourselves not shopping for a training bra, but instead shopping for a wig. God, what I would give for bra shopping right now! Donning her Notre Dame baseball cap, I realize that she fits her nickname. The Fighting Irish. Her mom was born in Dublin. Now, she was fighting. She fights; I grasp for control. I also pay for the wig. It doesn't look great. They make these things for adults.

KATIE: Dad, what do you think?

DADDY: (to audience) She asks as if she's playing dress-up, sorting through all of her possible outfits. (to Katie) You look beautiful, Katie. (to audience) She did. I wasn't lying. Even with the tawdry wig, Katie shined.

Treatments come, treatments go. Where they stop, nobody knows. Is it wrong that I'm joking? Rhyming? I mean, c'mon, I don't even know what to pray for. Do I want the treatments to continue? No. But do I want them to stop? Stopping could mean remission. It could also mean three strikes. So, I pray for neither, simply discussing them with Katie and dismissing them when she starts to cry. When Katie tells me she wants to go to the school dance, I hesitate as only a father can do.

KATIE: C'mon, dad! I even got a date. Keith Roush. He's dreamy looking. You'd like him.

DADDY: Trust me, if a pre-pubescent teen has targeted my daughter for his hormonal attacks, I don't like him. But, I have to admire his good taste. (to Katie) Can I chaperone?

KATIE: Sure, dad, it'll be fun. Keith wanted to know if you could drive us there anyway.

DADDY: (to audience) Prepping for the dance, I realize her mother should be here for this. I'm doing my best with the perfume and make-up. When it doesn't look great, I say: Why don't we go for the natural look?

Before we leave, I give her my lecture: (to Katie) Just remember, even though you're old enough to go out on a date, you'll always be (sings) **Daddy's Little Girl.

KATIE: Man, dad, you aren't going to sing that song again, are you? It's depressing. Makes me feel like I'm leaving you and we can't hang out anymore. Can you try something cheerier? What about the Blue Sky song?

DADDY: (to Katie) How about we go pick up Keith. He must be waiting. (to audience) At the dance, they do what is called "The Grand March." All of the couples get together, line up, and walk down the staircase to the dance floor. Patiently waiting as dozens of couples go by, I'm prepared to be proud of my Katie.

LOUDSPEAKER (Voice Over): Next, Katie Merrit and Keith Roush.

DADDY: Suddenly, I see her shoes hit the first step. Slowly, step by step, she comes into focus. The dress looks great and (shocked pause) And she's not wearing her wig.

Beaming like a choirgirl, my bald little girl comes down the stairs. She walks to me and says . . .

KATIE: I want them to like me for who I am. I've got no hair, no boobs, and no curves. So be it!

DADDY: Honey, you’re beautiful.

KATIE: I feel it!

DADDY: (to audience) Keith asks her if she wants to dance. Good boy.

Treatments come, treatments go. Then she gets sicker. Hospital stays come and go. Mom tries to stay home more. The only thing that doesn't come and go is Katie and I. Playing Rack-O on the hospital bed, I wonder how many more moments I will get. The unscientific answer: too few. (beat)

I greet Katie bright and early at 6:30. (to Katie, entering the hospital room with a tray) Rise and shine! What would you like today? Strained carrots or strained . . . Katie? Katie? (to audience) The nurse informs me:

NURSE: (softly) She's slipped into a coma.

DADDY: Katie? Katie? (to Nurse) Damn it, no! Damn it, no one is taking Katie!

NURSE: Sir, I'm sorry, but you knew this would happen soon. . .

DADDY: But it's not supposed to work out this way. I ask the doctor: (to Doctor) Will she live?

DOCTOR: We'll see.

DADDY: (panicked, to audience) That's not a no. That's a “We'll see.” That is a “We will see!!” (to Katie) Wake up. Wake up, Katie, your father is talking to you! You're in big trouble if you don't wake up right now! (praying) Oh, God. Please, God. We’re in big trouble if she doesn't wake up right now. (long beat)

(to audience) Six hours later, Katie passed away. Three weeks shy of sweet sixteen. I don't know what to do. Reinvent speaking with my wife?

On her birthday, I enter her bedroom for the first time. Her first place 4- H ribbon. The picture of her with Pluto at Disney World. Her wig. I spot a journal I have never seen before. In it, a note is addressed to me:

KATIE: (voice over) Dear Dad, If you are reading this and I'm still alive, put down the journal right now, you nosy butt! If you are reading this after I'm gone, read on.

I love you, dad. I'll miss my dad a ton, but I'll miss my best friend more. That's you, too, by the way! You've looked after me all these years, now I'll look after you from above. Sing to me every once and a while. I always like that.

DADDY: (tear-filled pause) Um, she always wanted that song that was cheerier what was it? Blue Sky? Oh yes, Blue Sky. (sings) Blue skies smilin' at me. / Nothin' but blue skies . . . (as he continues reading, he interrupts his tune) Oh, wait . . .

KATIE: PS: If you want to sing" Daddy's Little Girl" now, it's OK. It doesn't depress me anymore.

DADDY: This one’s for you, honey:

(sings)
**You're the end of the rainbow; You're my shining star,
You're sugar and spice;
You're everything nice and you're Daddy's little girl.
```

---

## IC-2408: Dance, Dance, Dance (from The Absolutely True Diary of a Part-Time Indian)

- Title: Dance, Dance, Dance (from The Absolutely True Diary of a Part-Time Indian)
- Author (byline): Sherman Alexie
- Work: The Absolutely True Diary of a Part-Time Indian
- Publisher: Little, Brown and Co
- Publication date as stated: Sept 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2011
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sherman Alexie
Book: The Absolutely True Diary of a Part-Time Indian
ISBN: 978-0316013680
Publisher: Little, Brown and Co
Date (Month/Year): Sept 2007
```

### Introduction (context only: never use it for content warnings)

```text
Arnie and Penelope are headed to the school dance. But in this selection the term “dance” implies a deeper meaning. Arnie is constantly having to dance around from place to place, from mask to mask (Indian and proud, poor and ashamed) It’s a constant struggle to fit into the two worlds he inhabits. But while American Indian children face some of the worst poverty in the nation -- some tribes report unemployment as high as 85%. -- remember, these amazing kids, culturally and spiritually rich, and filled with their own hopes and dreams are NOT defined by their economic situations. Dance, Dance Dance from The Absolutely True Diary of a Part-Time Indian by Sherman Alexie
```

### Performance text (classify this)

```text
Cutting is from Chapter 17 – Pages 118-129

Traveling between Reardan and Wellpinit, between the little white town and the reservation, I always felt like a stranger.

I was half Indian in one place and half white in the other. It was like being Indian was my job, but it was only a part-time job. And it didn't pay well at all.

The only person who made me feel great all the time was Penelope. Well, I shouldn't say that. I mean, my mother and father were working hard for me, too. They were constantly scraping together enough money to pay for gas, to get me lunch money, to buy me a new pair of jeans and a few new shirts. My parents gave me just enough money so that I could pretend to have more money than I did.

I lied about how poor I was. Everybody in Reardan assumed we Spokanes made lots of money because we had a casino. But that casino, mismanaged and too far away from major highways, was a money-losing business. In order to make money from the casino, you had to work at the casino.

And white people everywhere have always believed that the government just gives money to Indians.

And since the kids and parents at Reardan thought I had a lot of money, I did nothing to change their minds.

I figured it wouldn't do me any good if they knew I was dirt poor. What would they think of me if they knew I sometimes had to hitchhike to school?

Yeah, so I pretended to have a little money. I pretended to be middle class. I pretended I belonged. Nobody knew the truth.

Of course, you can't lie forever. Lies have short shelf lives. Lies go bad. Lies rot and stink up the joint.

In December, I took Penelope to the Winter Formal. The thing is, I only had five dollars, not nearly enough to pay for anything—not for photos, not for food, not for gas, not for a hot dog and soda pop. If it had been any other dance, a regular dance, I would have stayed home with an imaginary illness. But I couldn't skip Winter Formal. And if I didn't take Penelope then she would have certainly gone with somebody else.

Because I didn't have money for gas, and because I couldn't have driven the car if I wanted to, and because I didn't want to double date, I told Penelope I'd meet her at the gym for the dance. She wasn't too happy about that.

But the worst thing is that I was worried that people would make fun of me, right? And they probably would have if Penelope hadn't immediately squealed with delight when she first saw me walk into the gym.

"Oh, my, God!" she yelled for everybody to hear. "That suit is so beautiful. It's so retroactive. It's so retroactive that it's radioactive!"

And every dude in the joint immediately wished he'd worn his father's lame polyester suit. And I imagined that every girl was immediately breathless at the sight of my bell-bottom slacks. So, drunk with my sudden power, I pulled off some lame disco dance moves that sent the place into hysterics. Even Roger, the huge dude I'd punched in the face, was suddenly my buddy.

Penelope and I were so happy to be alive, and so happy to be alive TOGETHER, even if we were only a semi-hot item, and we danced every single dance.

Nineteen dances; nineteen songs. Twelve fast songs; seven slow ones. Eleven country hits; five rock songs; three hip-hop tunes. It was the best night of my life. Of course, I was a sweaty mess inside that hot polyester suit. But it didn't matter. Penelope thought I was beautiful and so I felt beautiful.

And then the dance was over. The lights flicked on. And Penelope suddenly realized we'd forgotten to get our picture taken by the professional dude.

"Oh, my God!" she yelled. "We forgot to get our picture taken! That sucks!" She was sad for a moment, but then she realized that she'd had so much fun that a

photograph of the evening was completely beside the point. A photograph would be just a lame souvenir.

I was completely relieved that we'd forgotten. I wouldn't have been able to pay for the photographs. I knew that. And I'd rehearsed a speech about losing my wallet. I'd made it through the evening without revealing my poverty.

I figured I'd walk Penelope out to the parking lot, where her dad was waiting in his car. I'd give her a sweet little kiss on the cheek (because her dad would have shot me if I'd given her the tongue while he watched). And then I'd wave good-bye as they drove away. And then I'd wait in the parking lot until everybody was gone. And then I'd start the walk home in the dark. It was a Saturday, so I knew some reservation family would be returning home from Spokane. And I knew they'd see me and pick me up.

That was the plan. But things changed. As things always change.

Roger and a few of the other dudes, the popular guys, decided they were going to drive into Spokane and have pancakes at some twenty-four-hour diner. It was suddenly the coolest idea in the world. It was all seniors and juniors, upperclassmen, who were going together. But Penelope was so popular, especially for a freshman, and I was popular by association, even as a freshman, too, that Roger invited us to come along.

Penelope was ecstatic about the idea. I was sick to my stomach. I had five bucks in my pocket. What could I buy with that? Maybe one plate of pancakes. Maybe. I was doomed.

"What do you say, Arnie?" Roger asked. "You want to come carbo-load with us?"

"Oh, I want to go, I want to go," she said. "Let me go ask Daddy."

Oh, man, I saw my only escape. I could only hope that Earl wouldn't let her go. Only Earl could save me now. I was counting on Earl! That's how bad my life was at that particular moment! Penelope skipped over toward her father's car.

"Hey, Penultimate," Roger said. "I'll go with you. I'll tell Earl you guys are riding with me. And I'll drive you guys home."

Roger's nickname for Penelope was Penultimate. It was maybe the biggest word he knew. I hated that he had a nickname for her. And as they walked together toward Earl, I realized that Roger and Penelope looked good together. They looked natural. They looked like they should be a couple. And after they all found out I was a poor-ass Indian, I knew they would be a couple.

Come on, Earl! Come on, Earl! Break your daughter's heart! But Earl loved Roger. Every dad loved Roger. He was the best football player they'd ever seen. Of course, they loved him. It would have been un-American not to love the best football player. I was angry and jealous and absolutely terrified.

"I can go! I can go!" Penelope said, ran back to me, and hugged me hard.

An hour later, about twenty of us were sitting in a Denny's in Spokane. Everybody ordered pancakes. I ordered pancakes for Penelope and me. I ordered orange juice and coffee and a side order of toast and hot chocolate and French fries, too, even though I knew I wouldn't be able to pay for any of it. I figured it was my last meal before my execution, and I was going to have a feast.

Halfway through our meal, I went to the bathroom. I thought maybe I was going to throw up, so I kneeled at the toilet. But I only retched a bit. Roger came into the bathroom and heard me.

"Hey, Arnie," he said. "Are you okay?"

"Yeah," I said. "I'm just tired."

"All right, man," he said. "I'm happy you guys came tonight. You and Penultimate are a great couple, man. Are you going to try out for basketball?"

I knew that practice started in a week. I'd planned on playing. But I didn't know if the Coach liked Indians or not.

"You think you're good enough to play varsity?" Roger asked.

"No way," I said. "I'm junior varsity all the way."

"All right," Roger said. "It will be good to have you out there. We need some new blood."

"Thanks, man," I said. I couldn't believe he was so nice. He was, well, he was POLITE! How many great football players are polite? And kind? And generous like that? It was amazing.

"Hey, listen," I said. "The reason I was getting sick in there is—" I thought about telling him the whole truth, but I just couldn't.

"I bet you're just sick with love," Roger said.

"No, well, yeah, maybe," I said. "But the thing is, my stomach is all messed up because I, er, forgot my wallet. I left my money at home, man."

"Dude!" Roger said. "Man, don't sweat it. You should have said something earlier. I got you covered." He opened his wallet and handed me forty bucks. Holy, holy. What kind of kid can just hand over forty bucks like that?

"I'll pay you back, man," I said.

"Whenever, man, just have a good time, all right?"

He slapped me on the back again. He was always slapping me on the back. We walked back to the table together, finished our food, and Roger drove me back to the school. I told them my dad was going to pick me up outside the gym.

"Dude," Roger said. "It's three in the morning."

"It's okay," I said. "My dad works the swing shift. He's coming here straight from work."

"Are you sure? I'll bring Penultimate home safely, man."

So Penelope and I got out of the car so we could have a private good-bye. She had laser eyes.

"Roger told me he lent you some money," she said.

"Yeah," I said. "I forgot my wallet."

Her laser eyes grew hotter. "Arnold? Can I ask you something big?"

"Yeah, I guess."

"Are you poor?"

I couldn't lie to her anymore. "Yes," I said. "I'm poor."

I figured she was going to march out of my life right then. But she didn't. Instead she kissed me. On the cheek. I guess poor guys don't get kissed on the lips. I was going to yell at her for being shallow. But then I realized that she was being my friend. Being a really good friend, in fact. She was concerned about me. I'd been thinking about her looks and she'd been thinking about my whole life. I was the shallow one.

"Roger was the one who guessed you were poor," she said.

"Oh, great, now he's going to tell everybody."

"He's not going to tell anybody. Roger likes you. He's a great guy. He's like my big brother. He can be your friend, too."

That sounded pretty good to me. I needed friends more than I needed my lust-filled dreams.

"Is your Dad really coming to pick you up?" she asked.

"Yes," I said.

"Are you telling the truth?"

"No," I said.

"How will you get home?" she asked.

"Most nights, I walk home. I hitchhike. Somebody usually picks me up. I've only had to walk the whole way a few times."

She started to cry. FOR ME! Who knew that tears of sympathy could be so sexy?

"Oh, my God, Arnold, you can't do that," she said. "I won't let you do that. You'll freeze. Roger will drive you home. He'll he happy to drive you home."

I tried to stop her, but Penelope ran over to Roger's car and told him the truth. And Roger, being of kind heart and generous pocket, drove me home that night. And he drove me home plenty of other nights, too.

If you let people into your life a little bit, they can be pretty amazing.
```

---

## IC-2409: Dangerous Pie

- Title: Dangerous Pie
- Author (byline): Jordan Sonnenblick
- Work: Drums, Girls and Dangerous Pie
- Publisher: DayBue Publishing
- Publication date as stated: May 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1679
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jordan Sonnenblick
Book: Drums, Girls and Dangerous Pie
ISBN: 978-0976103011
Publisher: DayBue Publishing
Date (Month/Year): May 2004
```

### Introduction (context only: never use it for content warnings)

```text
Children have been taught since the beginning of time to love their siblings. Those “only children” out there, count yourselves lucky because loving a sibling is hard. Especially when you have a brother like Jeffery: the cutest, sweetest, most embarrassing, and annoying child to ever walk the planet. “Dangerous Pie” by Jordan Sonnenblick
```

### Performance text (classify this)

```text
I guess a good starting point would be the longest journal I've ever written in English class. This was back in September, when I was pretty sure about life. The topic was "The Most Annoying Thing in the World," and we were supposed to write the usual one-page response to it. I sat there for a few minutes, staring at the back of Renee Albert, who's the hottest girl in the eighth grade, trying to concentrate. Unfortunately, all I could concentrate on was Renee Albert. Did I mention she's the hottest girl in the eighth grade? Miss Palma is always going on and on about brainstorming and lists and "prewriting," so I started a list of truly annoying things:

• Journal assignments

• Dull pencils

• The pencil sharpener smell

• Miss Palma's perfume

• Why doesn't Renee Albert ever look at me? Hot

girls who never look at skinny geeks

• Being a skinny geek

• Being a skinny geek named Steven

Just then I realized that Miss Palma was standing behind me, reading over my shoulder (I guess that's why I was being asphyxiated by her perfume). Thinking fast, I covered up my list, turned to her, and asked, "Miss Palma, can the journal be longer than a page?"

Sure Steven. Why? What are you thinking about creating here?

("Creating here." She actually said that. Don't English teachers just slay you? My mom is actually an English teacher, but that doesn't mean I don't find my own English teachers a bit odd.)

Well, I’m having trouble crafting my prose. (Yeah, "crafting my prose." Two can play this game. . .)

What’s your topic! Remember what I always say; “F.F.F!” (Stands for "Form Follows Function," don't you know.)

Hmm…I want to write about a good topic…I want to write about…(And then it hit me. The most annoying thing in my world is . . .)

My little brother Jeffery!

Anyway, here's what I wrote:

Having a brother is horrible. Having any brother would be horrible, I suppose, but having my particular brother, Jeffrey, is an unrelenting nightmare. It's not because he's eight years younger than I am, although that's part of it. How would you like to be King of the Planet for eight glorious years, and then suddenly get demoted to "Vice-King?" It's not because he's cuter than I am, although that's part of it too. I have mouse-brown cowlick-y hair, glasses that are about an inch thick and braces that look like I tried to swallow a train wreck. He has those perfect little-kid Chiclet-white teeth, 20-20 vision, and little blond ringlets like the ones on the angels you see on the posters in art class. It's not even because he hates me - he doesn't. The truth is that he idolizes me. And that's the problem: the kid follows me around like I'm Elvis or something. And while he's being much too cute and following me around, he also destroys all of my stuff, including my self-esteem and my sanity.

Take, for example, the "Dangerous Pie" incident. Jeffrey has known from an early age that the worst possible thing he can do to me is to touch my drum stuff. I have some rules about this: he may not PLAY the drums, he may not pretend the cymbals are shields and he is a knight, he may not hide IN the bass drum, and pretty much any Jeffrey-to-drumsticks contact is a massive no-no. But on one fateful afternoon last year, Jeffrey threw the rules out the window.

On the tragic day, I came home, said hi to Mom, glugged down some milk, and headed down to the base-ment to practice. I was in a particularly good mood, I remember, because Renee Albert had told me in P.M. homeroom that she liked my shirt. As this was such a grand occasion, I decided to take the Special Sticks down from their sacred perch and use them for my practice-pad warm-up. In case you didn't know this, a practice pad is a thick, dense, flat piece of rubber. Usually it's glued onto a piece of wood. You practice playing drums on it, because it feels a lot like playing on a real drumhead. Anyhow, the Special Sticks would be just an ordinary pair of my favorite sticks - Regal Tip 51’s with nylon tips - except that they have been autographed by my all-time drum hero, Carter Beauford of the Dave Matthews Band. I once saved up all my babysitting money for a couple of months, got two tick-ets to a drum clinic Carter Beauford was giving an hour and a half away in Philadelphia, and begged my Dad to take me for two weeks until he finally gave in. At the clinic, during what I like to think of as "The Two Glorious Minutes," Carter Beauford himself called me up front to demonstrate a double-stroke roll. After I did it, he said I had "nice technique," and signed my sticks, right there in front of a roomful of drummers! So I had spent quite a bit of blood, toil, tears, and sweat in order to get the Special Sticks.

But the Special Sticks weren't on their shelf.

Jeffrey!

I ran upstairs at top speed, hoping I would be in time, but knowing that the odds were stacked against me. I burst into the kitchen and found Jeffrey doing his 'cooking' thing on the floor. Pots and pans were everywhere-don't ask me how I had somehow not noticed this on my way downstairs the first time-and Jeffrey was stirring some pretend concoction in the deepest pot of all. With my Special Sticks. I advanced toward him, with what must have been a disturbing gleam of violence in my eye.

Jeffrey! Give-me-the-sticks.

But I'm just COOKING.

Give-me-the-sticks.

But the Dangerous Pie isn’t ready yet!

I don't care about your stupid four-year-old make-believe food.

Give-me-the-sticks!

But it’s REAL food!

And it was. Jeffrey's Dangerous Pie was a zesty blend of coffee grounds, raw eggs and their smashed shells, Coke, uncooked bacon, and three Matchbox racing cars.

The Special Sticks STILL smell funny.

Or maybe I should tell you about the "Please kill me Mom" affair. This fiasco happened after my All-City High School Jazz Band concert last June. Getting into the All-City band is a big, big deal, especially for a drummer - because there are six trumpeters, five saxes, four trombones, et cetera, but only two drummers. It was even a bigger deal for me last year, because I was the first seventh grade drummer EVER admitted into the All-City high school band. They even had to send a special van to the middle school just to get me and this girl named Annette Watson, who's the backup piano player. She's actually really good, but there's this twelfth grade guy who's been the main pianist since he was a freshman, and he's not about to get booted by a middle school girl in his senior year. She's funny, and she may be the only kid in the middle school who cares about music the way I do, but she's also kind of weird. It's like she's figured out how to play Beethoven and Thelonious Monk, but hasn't quite mastered the art of being a girl yet.

It's not easy being the youngest guy in the band, by the way. They make fun of me all the time about my age, my size, my braces, and the way I stick out my tongue when I play.

Anyway, my whole family came to the concert, and it was AWESOME. I had this huge drum feature in this Brian Setzer song called "Jump Jive an' Wail" and I nailed the whole thing. I usually practice at least an hour a day on my practice pad and another half hour on my drum set, plus I play in the marching band and the jazz group in school, AND we had been rehearsing twice a week for All City for a couple of months, AND I used to take lessons once a week, so I was playing great that night. So after the concert, my parents and Jeffrey came to the band room. They were all excited and everything, but Jeffrey was bouncing off the ceiling:

You’re a rock star Steven.

No, I'm a JAZZ drummer Jeffy.

MY BROTHER IS A ROCK STAR! MY BROTHER IS A ROCK STAR!

Just then, Renee Albert stopped right next to us to congratulate her boyfriend (we'll just call him Biff), a sophomore guitarist with an alarmingly perfect complexion and muscles like Sammy Sosa. Jeffrey saw Renee, and started to whirl toward her-she lives around the corner from us, and I guess not even four-year-olds are immune to her charms and wiles. It seemed to happen in slow motion; events were just crawling. Yet still I knew I would never have time to run across town to the local zoo, steal an elephant tranquilizer gun, run back, and fire it into Jeffrey's buttock before he could blurt out something that would mortify me and destroy my social status forever.

Life snapped back into full-speed, and Jeffrey shouted: Hey, Renee! MY BROTHER IS A ROCK STAR!

As Biff looked on with a sneer, Renee replied:

Really? I didn’t know that.

Yup, did you see his arms zooming around on the drums? It’s just like when he practices in the mirror.

Steven practices in front of a mirror?

Yeah! He does it in his underwear. The blue ones. Right Steven?

I sagged against my mom's shoulder and muttered: Please kill me, Mom.

My dad tried at that point to control the situation, but by now Jeffrey had drawn a little crowd of my band mates, who were just waiting to see what else he would reveal.

My brother is GREAT! Hey, Renee, do you want to hear a JOKE? What does I-C-U-P spell?

I give up.

Close the bathroom door! GET IT?

Dear Reader: Are you starting to see a pattern here?

Miss Palma gave me an "A" on the journal entry-she called it "droll" -so I guess I actually managed to get some use out of Jeffrey's antics before the chaos of this year started. Looking back on those days now, I'd have eaten the Dangerous Pie if I could have stopped October from coming.
```

---

## IC-2410: A Day No Pigs Would Die

- Title: A Day No Pigs Would Die
- Author (byline): Robert Newton Peck
- Work: Not specified
- Publisher: Random House Children's Books
- Publication date as stated: Dec 1994
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1261
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Newton Peck
ISBN: 978-0679853060
Publisher: Random House Children's Books
Date (Month/Year): Dec 1994
```

### Introduction (context only: never use it for content warnings)

```text
Some days it just doesn’t pay to get out of bed at all. We’ve all had “those” days. . . where every good turn gets shot down, and doing the right thing doesn’t gain us any reward at all. Unappreciated, taken for granted and ridiculed . . . But what if your nemesis isn’t human at all? A Day No Pigs Would Die by Robert Newton Peck.
```

### Performance text (classify this)

```text
I should’ve been in school that April day.

But instead I was up on the ridge near the old spar mine above our farm, whipping the gray trunk of a rock maple with a dead stick, and hating Edward Thatcher. During recess, he’d pointed at my clothes and made sport of them. Instead of trying into him, I’d turned tail and run off. And when Miss Malcolm rang the bell to call us back inside, I was halfway home.

Picking up a stone, I threw it into some bracken ferns, hard as I could. Someday that was how hard I was going to light into Edward Thatcher, and make him bleed like a stuck pig. I’d kick him from one end of Vermont to the other, and sorry him good. I’d teach him not to make fun of Shaker ways. He’d never show his face in the town of Learning, ever again. No, sir.

A painful noise made me whip my head around and jump at the same time. When I saw her, I knew she was in bad trouble.

It was the big Holstein cow, one of many, that belonged to our near neighbor, Mr. Tanner. This one he called “Apron” because she was mostly black, except for the white along her belly which went up her front and around her neck like a big clean apron. She was his biggest cow, Mr. Tanner told Papa, and his best milker. And he was fixing up to take her to Rutland Fair, come summer.

As I ran toward her, she made her dreadful noise again. I got close up and saw why. Her big body was pumping up and down, trying to have her calf. She’d fell down and there was blood on her foreleg, and her mouth was all thick and foamy with yellow-green spit. I tried to reach my hand out and pat her head; but she was wild-eyed mean, and making this breezy noise almost every breath.

Turning away from me, she showed me her swollen rump. Her tail was up and arched high, whipping through the air with every heave of her back. Sticking out of her was the head and one hoof of her calf.

Apron went crashing though the puckerbush, me right behind. I’d never caught up. But because she had to stop and strain, I got to the calf’s head and got a purchase on him.

He was so covered with slime, and Apron was so
wandering, there was no holding to it.
Apron was comfortable over a thousand, and it wasn’t
much of a tug for her.

As I went down, losing my grip on the calf’s neck, her hoof caught my shinbone and it really smarted. The only thing that made me get up and give the whole idea another go was when he bawled again.

I’d just wound up running away from Edward Thatcher and running away from the schoolhouse. I was feathered if I was going to run away from one darn more thing.

I needed a rope. But there wasn’t any, so I had to make one. It didn’t have to be long, just strong.

Chasing old Apron through the next patch of prickers sure took some fun out of the whole business. I made my mistake of trying to take my trousers off as I ran. No good. So I sat down in the prickers, yanked ‘em off over my boots, and caught up to Apron. After a few bad tries, I got one pant leg around her calf’s head and knotted it snug.

“Calf,” I said to him, “you stay up your ma’s hindside and you’re about to choke. So you might as well choke getting yourself born.”

Whatever old Apron decided that I was doing to her back yonder, she didn’t take kindly to it. So she started off again with me in the rear, hanging on for her dear life. But when Apron stopped to heave again I got the other pant leg around a dogwood tree that was about thick as a fencepost.

Now only three things could happen: My trousers would rip. Apron would just uproot the tree. The calf would slide out. Right? Wrong.

Nothing happened. Apron just stood shaking and heaving and straining and never moved forward a step. I got the other pant leg knotted about the dogwood; and like Apron, I didn’t know what to do next.

Her calf bawled once more, making a weaker noise than before. But all old Apron did was heave in that one place.

“You old bitch,” I yelled at her, grabbing a dead blackberry cane that was as long as a bullwhip and big around as a broom handle, “you move that big black smelly ass, you hear?”

I never hit anybody, boy or beast, as I hit that cow. I beat her so hard I was crying. Where I held the big cane, the thorns were chewing up my hands real bad. But it only got me madder.

I kicked her. And stoned her. I kicked her again one last time, so hard in the udder that I thought I heard her grunt. Both her hind quarters sort of hunkered down in the brush. Then she started forward, my trousers went tight, I heard a rip and a calf bawl. And a big hunk of hot stinking stuff went all over me. Some of it was calf, some of it wasn’t.

As I went down under the force and weight of it, I figured something either got dead or got born.

All I knew was that I was snarled up in the passel of wet stuff, and there was a strong cord holding me against something that was very hot and kicked a lot. I brushed some of the slop away from my eyes and looked up. And there was Apron, her big black head and her big black mouth licking first me and then her calf.

But she was far from whole. Her mouth was open and she was gasping for air. She stumbled once. I thought for sure I was going to wind up being under a very big cow. The noise in her throat came at me again, and her tongue lashed to and fro like the tail of a clock. It looked to me as if there was something in her mouth. She would start to breathe and then, like a cork in a bottle, some darn thing in there would cut it off.

Her big body swayed like she was dizzy or sick.

As the front of her fell to her knees, her head hit my chest as I lay on the ground, her nose almost touching my chin. She had stopped breathing!

Her jaw was locked open so I put my hand into her mouth, but felt only her swollen tongue. I stretched my fingers up into her throat-and there it was! A hard ball, about apple-size. It was stuck in her windpipe, or her gullet. I didn’t know which and didn’t care. So I shut my eyes, grabbed it, and yanked.

Somebody told me once that a cow won’t bite. That somebody is as wrong as sin on Sunday. I thought my arm had got sawed off part way between elbow and shoulder. She bit and bit and never let go. She got to her feet and kept on biting. That devil cow ran down off that ridge with my arm in her mouth, and dragging me half-naked with her.
```

---

## IC-2411: The Day the Voices Stopped

- Title: The Day the Voices Stopped
- Author (byline): Ken Steele
- Work: Not specified
- Publisher: Basic Books
- Publication date as stated: 978-0465082278
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: KEN, VOICE 1, VOICE 2, NEWSCASTER, HUGH DOWNS, BARBARA WALTERS, DAD, BABY BROTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1676
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ken Steele
ISBN: May 2002
Publisher: Basic Books
Date (Month/Year): 978-0465082278
```

### Introduction (context only: never use it for content warnings)

```text
For thirty-two years Ken Steele lived with the devastating symptoms of schizophrenia. The voices arrived without warning on an October night in 1962 when Ken was 14 years old. Derisive voices that continually said derogatory things to and about him. For thirty-two years, destructive voices inhabited his disordered mind, teasing him, mocking him, driving him time and again to the very edge of life. . . and daring him to take the final step. They commanded he kill himself in horrific ways. This is how Ken’s story began . . . The Day the Voices Stopped by Ken Steele
```

### Performance text (classify this)

```text
KEN: (Pg 1-2) The voices arrived without warning on an October night in 1962. I was 14 years old.

VOICE 1: Kill yourself. . . Set yourself afire

KEN: I stirred, thinking I was having a nightmare, but I wasn’t asleep; and the voices -- low and insistent, taunting and ridiculing --continued to speak to me from the radio.

VOICE 1: Hang yourself. The world will be better off. You’re no good, no good at all.

KEN: Terrified, I turned off the radio, got out of bed, and crept down the hallway in my bare feet. But the voices would not be tuned out. They accompanied me.

VOICE 1: You should die.

VOICE 2: (shrieking)You should never have been born!

KEN: They were talking to me. . . someone or something wanted me to die. Who was doing the talking? What was going on? I turned the handle to the door of my parents’ bedroom, looking for safety, but my mom and dad were sleeping soundly, and I was afraid to wake them. I knew they had to go to work in the morning. And even if I woke them, what would I say? The voices supplied an answer.

VOICE 1: Go right in! Tell your dad you’re afraid of the dark and then tell him about us. It will only confirm what he already knows -- that you’re different, a disappointment.

KEN: The voices were right: This was not a man to whom I could confide that I was hearing things.

KEN: (Pg 2-5) I wandered down the stairs of our tidy Cape Cod-style house to my grandmother’s bedroom. Emma Mae, my mother’s mother, was my best friend. I could tell her anything and she would still love me. As I turned the knob to her room, the voices in my head grew shriller and louder until I felt I was drowning in sound.

VOICE 2: Die, die, die. You’re worthless, no good. Do it now, not later!

KEN: I staggered into the living room and collapsed on the floor. My mother found me lying there in the morning. “What are you doing up so early?" she asked, shaking my shoulder. I remember thinking that my mother had arrived, like a lifeguard, to rescue me. Nw I was safe. But my relief was short-lived. The voices were still there, lower in volume and chattering in the singsong cadence that children use to taunt one another.

VOICE 1: Na na na na na / We’re still he-ere / You thought you got rid of us / No such lu-uck.

KEN: I felt bombarded by the noise and terrified by the strangeness of what was happening. Act normal, I told myself. I washed and dressed hurriedly. I went down to breakfast and forced myself to eat. My parents soon left for work, and, as she did every morning, Grandma let me television before I left for school. As I sat in front of the TV, all these people began to talk about me.

NEWSCASTER: Today, Kenny Steele will kill himself.

KEN: An electric shock ran through my body. Had I heard right? (uses remote to change the channel) Seconds later, Hugh Downs spoke to me

HUGH DOWNS: (deeper voice) Don’t kill yourself, Kenny. Don’t give up. Try not to do it.

KEN: Barbara Walters conducted a posthumous interview with me.

BARBARA WALTERS: Why did you kill yourself? she asked. Did you really mean to do it?

KEN: I raced out the door. The voices were screaming at me.

VOICE 2: Run, run, run, you coward!

KEN: I turned right and ran past the school building but did not go in. Instead, I headed for the forest next to the school. I hoped to hide from the voices among the dense foliage, but they found me and continued their diatribe.

VOICE 1: You’re worthless. . .

VOICE 2: Your parents don’t want you around anymore. . .

VOICE 1: You could leave home. . .

VOICE 2: Better yet, you could kill yourself. . .

VOICE 1: Yes, that’s it. That’s the answer. . . Die.

KEN: (defeated) I don’t know how long I lingered in the forest that day. (long beat) A couple of weeks later, Dad came home from work excited.

DAD: The president will be speaking about the Cuban missile crisis tonight. I want you to hear what he has to say about the Communists.

KEN: As President Kennedy spoke to the nation, my voices spewed obscenities at me. It was impossible for me to hear and understand what was being said. The President concluded his talk, and Dad began to speak to me.

DAD: What are they teaching you in school

VOICE 2: Don’t listen to your father. He’s no good.

DAD: about Khruschev and Cuba and about those

VOICE 1: Don’t answer his questions. . .

DAD: terrible Communists and their plan to ravage the world?

VOICE 2: Turn your back on him! Turn away now!

KEN: (Pg 6-8) That evening, the voices won out. As my father quizzed me about what we had seen on TV, what I knew, what I thought, I did as the voices directed

(overwhelmed, puts hands over ears and turns away)

Dad became enraged. “Go to bed without dinner,” he ordered me, stalking out of the living room. It was a punishment he rarely imposed.

VOICE 1: Ungrateful boy, now see what you’ve done.

VOICE 2: You’ve disappointed your father [again]. Your parents deserve a better son than you.

KEN: Soon they would have one. Some time after the voices first visited me, my mother and father told me they were expecting a baby. If I have to have a sibling, I prayed, let it be a sister. But the voices knew better. They had decided the baby would be a boy, and on several terrifying occasions they made it seem as if “he” were speaking to me.

BABY BROTHER: (whispering menacingly) I am coming, I’m going to be born. You have to leave. Take a radio into the bathtub and electrocute yourself . . . Jump in front of a car at night on Route 69. . . Pour charcoal lighter fluid over your body and set yourself afire. . . Hang yourself in the forest.

KEN: My brother was born May 10, 1964 – Joseph Robert Steele.

VOICE 1: He’s here now (laughing maniacally) Joey is the good son. He’s the one they wanted.

VOICE 2: It’s time for you to go . . . Stop hanging around.

KEN: Only two things, reading and writing, could tone the voices down. When I read, I entered the world of Huckleberry Finn; I’d suffer the growing pains of Holden Caulfield. The voices would become muffled. And so I read voraciously. I read my way through the last year of junior high school and wrote frantically, scribbling page after page before the voices took over. For three years, I managed to cover up what was happening to me, or so I thought. (Pg 9-12) But the voices were stepping up their demands that I destroy myself.

VOICE 1: No simple death for you! Guts and gore and a big mess. . . that’s the way you must take your life.

VOICE 2: Get out that door. . . Run, run, run. You’ve got to die.

KEN: And so I ran away from home. I ran to the same forest in which I had sought refuge the first time the voices had descended on me.

VOICE 1: Get a rope, twelve feet long and two inches thick.

KEN: I’d gone to a hardware store and bought the rope.

VOICE 2: Tie the noose with a sea knot, and make sure it’s tied tight

KEN: I practiced tying knots. At the direction of the voices, I had also taken a step stool from the basement and hidden it in the forest, covering it over with branches and leaves. I’d bought lighter fluid and matches and left them in a small locker that I’d hidden in the same area. When all the preparations had been made, the voices were pleased with me.

VOICE 1: Good, your suicide kit is complete.

KEN: That night -- the night I ran away -- I made three different attempts on my life. First, I got up on the stool, then tied the noose around my neck. But even though I tossed and thrashed about, I couldn’t manage to kick the stool away. I had failed. Tears streaming down my face, I located the charcoal lighter fluid and poured it on my head. I could not bring myself to light a match. The highway, I thought, half running, half dragging myself in my disoriented state about a mile to Route 69. My plan was to leap in front of a car. I stood at the side of the road. Headlights were coming at me. Now! I told myself, but then I noticed a spotlight atop the car. What if this was a police car? What if the police were coming for me? Panicked, I ran back from the road, back toward the school that sat dark and deserted in the summer night. I crouched behind the building, clinging to its hard concrete walls for what seemed like eternity.

The following morning, I rose and headed for home. Two state trooper cars were parked outside our house. Dad stood in our front yard, talking animatedly with the troopers. I froze in my tracks. My dad turned and saw me.

VOICE 2: They’re going to shoot you. See the guns in their holsters? Your dad is arranging to have you killed.

KEN: My parents had called the troopers, reporting me as a runaway who had threatened suicide. Now the officers wanted to escort me to the hospital. Dad convinced them to let him take me to our family physician, Dr. Sullivan, instead. It was growing dark and pouring when we drove to the appointment. Dr. Sullivan asked if he could speak with me alone. I have no memory of what the doctor said or did, but I clearly recall the looks of worry and confusion on my parents’ faces when the doctor called them back in.

Mom, Dad, and I returned home. Later that night, I heard my father speaking on the telephone. He was talking about me. He was telling the person on the other end that I had a very serious mental illness. It had a long name, and I remember wanting to know how to spell it. That way, I could look it up in the library and learn how to get rid of the voices..

I walked over to my dad and asked him if he would spell the disease. Dad leaned his forehead into his hand and handed me a small slip of paper. On it, there was one word, neatly printed in capital letters: (begins spelling aloud) S C H I Z O . . .

VOICE 2: (interrupting) Schizo – Schizo - Schizophrenia!

(laughter)
```

---

## IC-2412: Dear Amanda and Closure

- Title: Dear Amanda and Closure
- Author (byline): Steve Martin
- Work: Pure Drivel
- Publisher: 1999
- Publication date as stated: Hyperion
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1371
- Already set (do not supply): none

### Source block (context only)

```text
Author: Steve Martin
Book: Pure Drivel
ISBN: 978-0786885053
Publisher: 1999
Date (Month/Year): Hyperion
```

### Introduction (context only: never use it for content warnings)

```text
We've all been there. "What did I do wrong?" you ask yourself. "Was it something I said? Something I wore? My breath? How I kiss? You want reasons. You want answers. You want the truth. YOU CAN'T HANDLE THE TRUTH! Well, maybe you can, but why do you want it? To argue with her? To convince her she's wrong? How will you feel if she gives you a list of reasons she doesn't like you? You'll get your closure, but your self-esteem might take a hit. You'll also look desperate in the process. Dear Amanda by Steve Martin
```

### Performance text (classify this)

```text
DEAR AMANDA (Pg 26-29) Dear Amanda, This will be the last letter I write to you. I think we have made the right decision. Thank you for your love. We had a wonderful experience these past five months. I want you to know that our time together will live inside me in a special place in my heart. It is best if we do not phone or write.

Love always, Joey Dear Amanda, I dialed you last night because the Lucy pie episode was on and I knew you'd want to see it. Anyway, while I was leaving a message, I leaned on the phone and accidentally punched in your message-retrieval code. Sorry about that. Who's Francisco? Just curious.

Joey

Dear Amanda, I realized that I still had your set of six Japanese sake cups that I bought for you on our trip downtown and was wondering when it might be a good time to drop them off. You can give me a call at the usual number but maybe better at the office up till seven but then try the car or I'm usually home now by seven forty-five. I would like to get these back to you, as I know you must be thinking about them. This will be my last letter.

Regards, Joey Dear Amanda, It was a lucky coincidence that my cat leapt on your speed-dial button last night, as it gave us a chance to talk again. Afterwards, I was wondering what you meant when you said, "It's over, Joey, get it into your head." So many interpretations. Just curious. Oh, I found myself on your street last night and noticed a yellow Mustang that I don't remember ever being at your apartment complex. Is this the mysterious Francisco I've heard rumors about? No big deal. Just curious. I left one of the sake cups at your front door; it happened to be in my car. What was that loud music?

With respect, Joey

Dear Amanda, This will be the last letter I write to you. I hate to hurt you like this, but I'm seeing someone new. You'd like her. Her name is Marisa-she has the same number of letters in her name as you! Incidentally, I heard that Francisco had or is having a tax problem. Should I meet with him? I'm over it all now and would be glad to help.

Also, a word of warning: Latins. One woman is never enough. Just a thought.

Joey P.S. Do you have my red Pentel pen? I really need it. *Text* me when you get this.

Dear Amanda, This will be the last letter I write to you. I'm quite upset that you changed your phone without a forwarding number. There could still be emergencies, and I'm still in possession of those fancy upholstered hangers of yours. Marisa questioned me about them the other day, and it wasn't fun. They're probably too dear to you to throw out, as we bought them together at the swap meet the day your mother raved about me, saying I was "pleasant." Please come by and pick them up; they're seriously damaging my relationship with Marisa. A good time would be any Wednesday after five but not after seven, Fridays anytime except lunch, Monday is good, and the weekend, anytime. Also Tuesday. By the way, there's someone named Francisco trying to pick up girls on the Internet. Hmm . . . I wonder.

Joey

Dear Amanda, Valentine's Day is tomorrow, and I hope you don't mind my throwing this note through your window, as the post would be too slow. The rock it's tied to came from our desert trip! I'm wondering if you'd like to get together for a quick lunch on the fourteenth -- you can even bring Francisco if you want; maybe I could help him sort out his heavy urology bills. I need to get my letters back from you, and could you bring this one too? I could bring the hangers, and I also want you to have the photo of me nude skydiving. Can you let me know soon? I'm waiting outside on the lawn. This will be the last letter I write to you.

Love you always, Joey TRANSITION CLOSURE: The ending of a piece of one's life. Closure means finality; a letting go of what once was. Finding closure implies a complete acceptance of what has happened and moving on to something new. Obviously Joey had problems finding closure with Amanda. But the rest of his life could have been fine . . . except for one thing. He became obsessed with CLOSURE by Steve Martin.

CLOSURE (Pg 106-108)

Closure. I wanted it. Or I wasn't going to be able to move on.

The taxi had dropped me off fully ten blocks earlier than I had requested. Sixty-first instead of Seventy-first. Luckily, I had copied down the cab number in case for some reason I needed closure. This time I did. I called the taxi company from my cell phone. I told them what I wanted. "Some kind of closure," I said. "I need to get on with my life." They understood. Thus the day had begun.

[Then] it was a little matter of a short-change at the supermarket. One dollar and fifty cents. Not much, but as I stood there counting the change, realizing the mistake, I couldn't move on. I confronted the check-out girl.

"Oops," she said.

Oops? Oops? This was not closure. How was I to move on? I did not sense that the store was taking responsibility. The manager came over and took me aside. He understood closure. He apologized, and took responsibility. I was lucky. I could move on.

My [new] girlfriend Josie was already at the apartment. I had given her a key just two weeks earlier. I came in with the groceries. We put them away and ordered in. We watched the news. Murder, larceny, confidence games: so many people who couldn't move on. I kissed her and held her hand. I took her to the bedroom. I tried *you know*, but couldn't. Too many loose ends. But she wanted closure. I explained that because so many people in my life weren't taking responsibility, it became impossible for me to accept my own responsibility.

She understood. But she still wanted closure.

Two days go by. My movie theater free admission coupon is not being honored. A line forms behind me as I explain my situation to the ticket seller. I had called ahead to make sure it would be honored. They said it would be. Yet here I am, being embarrassed in front of strangers. Josie says, "Let's pay," and suggests that we move on. I cannot. I tell them I will need closure. The man selling tickets says the coupon people made a mistake, and they are the ones who will need to take responsibility.

"So you need closure," I say.

"Yes," he replies, "before we can move on."

"So my closure is dependent on your closure," I say.

"Yes."

Just then Josie says, "I need closure too, tonight." She pays. I move on, even though I am unable to move on.

We watch the movie. It is about Mary Queen of Scots. She was beheaded. At least she got closure.

When the movie is over, it says, "The end." We can go home.

“Pop” goes the champagne cork. Josie starts drinking. I start to worry. She starts kissing me. I am helpless. I can't move on. The phone rings and the machine picks up. It's the manager of the movie theater.

"I talked with the coupon people," he says, "they will issue a new coupon. I'm hoping now we can move on."

I smile at Josie. But something's still not right. I notice the answering machine blinking. I irritate Josie when I play back the message. It is the taxi company with a full apology. I can move on.

I give Josie closure. She snuggles next to me. A candle burns to the end and snuffs itself out. The moonlight trickles into the bedroom. I look at the bedroom door. It's ajar. I know what I need. [(whispers) C.L.O.S.U.R.E]
```

---

## IC-2413: Death by Scrabble

- Title: Death by Scrabble
- Author (byline): Charlie Fish
- Work: Dark Moon Digest - Issue Number 3
- Publisher: Dark Moon Books
- Publication date as stated: April 2011
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR
- Teaser before the introduction: No
- Spoken words (computed): 1277
- Already set (do not supply): none

### Source block (context only)

```text
Author: Charlie Fish
Book: Dark Moon Digest - Issue Number 3
ISBN: 978-0978792589
Publisher: Dark Moon Books
Date (Month/Year): April 2011
Also available online at East of The Web.com
https://www.eastoftheweb.com/short-
stories/UBooks/DeatScra.shtml
```

### Introduction (context only: never use it for content warnings)

```text
Board games imitate real life. For example, you have to cooperate and wait your turn. There are rules you have to follow. Someone will win and someone will lose. Because board games provide an opportunity to interact with people, they promote social skills. Board games bring people together, both young and old. Board games can strengthen bonds between family members . . . or. . . not . . .

Death by Scrabble by Charlie Fish
```

### Performance text (classify this)

```text
NARRATOR: It's a hot day and I hate my wife.

We're playing Scrabble. That's how bad it is. I'm 42 years old, it's a blistering hot Sunday afternoon and all I can think of to do with my life is to play Scrabble.

I should be out, doing exercise, spending money, meeting people. I don't think I've spoken to anyone except my wife since Thursday morning. On Thursday morning I spoke to the milkman.

My letters are crap.

I play, appropriately, BEGIN. With the N on the little pink star. Twenty-two points.

I watch my wife's smug expression as she rearranges her letters. Clack, clack, clack. I hate her. If she wasn't around, I'd be doing something interesting right now. I'd be climbing Mount Kilimanjaro. I'd be starring in the latest Hollywood blockbuster. I'd be sailing the Vendee Globe on a 60-foot clipper called the New Horizons - I don't know, but I'd be doing something

She plays JINXED, with the J on a double-letter score. 30 points. She's beating me already. Maybe I should kill her.

If only I had a D, then I could play MURDER. That would be a sign. That would be permission.

I start chewing on my U. It's a bad habit, I know. All the letters are frayed. I play WARMER for 22 points, mainly so I can keep chewing on my U.

As I'm picking new letters from the bag, I find myself thinking - the letters will tell me what to do. If they spell out KILL, or STAB, or her name, or anything, I'll do it right now. I'll finish her off.

My rack spells MIHZPA. Plus the U in my mouth. Damn.

The heat of the sun is pushing at me through the window. I can hear buzzing insects outside. I hope they're not bees. My cousin Harold swallowed a bee when he was nine, his throat swelled up and he died. I hope that if they are bees, they fly into my wife's throat.

She plays SWEATIER, using all her letters. 24 points plus a 50-point bonus. If it wasn't too hot to move, I would strangle her right now.

I am getting sweatier. It needs to rain, to clear the air. As soon as that thought crosses my mind, I find a good word. HUMID on a double-word score, using the D of JINXED. The U makes a little splash of saliva when I put it down. Another 22 points. I hope she has lousy letters.

She tells me she has lousy letters. For some reason, I hate her more.

She plays FAN, with the F on a double-letter, and gets up to fill the kettle and turn on the air conditioning.

It's the hottest day for ten years and my wife is turning on the kettle. This is why I hate my wife. I play ZAPS, with the Z doubled, and she gets a static shock off the air conditioning unit. I find this remarkably satisfying.

She sits back down with a heavy sigh and starts fiddling with her letters again. Clack clack. Clack clack. I feel a terrible rage build up inside me. Some inner poison slowly spreading through my limbs, and when it gets to my fingertips I am going to jump out of my chair, spilling the Scrabble tiles over the floor, and I am going to start hitting her again and again and again.

The rage gets to my fingertips and passes. My heart is beating. I'm sweating. I think my face actually twitches. Then I sigh, deeply, and sit back into my chair. The kettle starts whistling. As the whistle builds it makes me feel hotter.

She plays READY on a double-word for 18 points, then goes to pour herself a cup of tea. (to wife) No, I do not want one.

I steal a blank tile from the letter bag when she's not looking and throw back a V from my rack. She gives me a suspicious look. She sits back down with her cup of tea, making a cup-ring on the table, as I play an 8-letter word: CHEATING, using the A of READY. 64 points, including the 50-point bonus, which means I'm beating her now.

She asks me if I cheated.

I really, really hate her.

She plays IGNORE on the triple-word for 21 points. The score is 153 to her, 155 to me.

The steam rising from her cup of tea makes me feel hotter. I try to make murderous words with the letters on my rack, but the best I can do is SLEEP.

My wife sleeps all the time. She slept through an argument our next-door neighbors had that resulted in a broken door, a smashed TV and a Teletubby Lala doll with all the stuffing coming out. And then she bitched at me for being moody the next day from lack of sleep.

If only there was some way for me to get rid of her.

I spot a chance to use all my letters. EXPLODES, using the X of JINXED. 72 points. That'll show her.

As I put the last letter down, there is a deafening *BANG* and the air conditioning unit fails.

My heart is racing, but not from the shock of the bang. I don't believe it - but it can't be a coincidence. The letters made it happen. I played the word EXPLODES, and it happened - the air conditioning unit exploded. And before, I played the word CHEATING when I cheated. And ZAPS when my wife got the electric shock. The words are coming true. The letters are choosing their future. The whole game is - JINXED.

My wife plays SIGN, with the N on a triple-letter, for 10 points.

I have to test this. I have to play something and see if it happens. Something unlikely, to prove that the letters are making it happen. My rack is ABQYFWE. That doesn't leave me with a lot of options. I start frantically chewing on the B.

I play FLY, using the L of EXPLODES. I sit back in my chair and close my eyes, waiting for the sensation of rising up from my chair. Waiting to fly.

Stupid. I open my eyes, and there's a fly. An insect, buzzing around above the Scrabble board, surfing the thermals from the tepid cup of tea. That proves nothing. The fly could have been there anyway.

I need to play something unambiguous. Something that cannot be misinterpreted. Something absolute and final. Something terminal. Something murderous.

My wife plays CAUTION, using a blank tile for the N. 18 points.

My rack is AQWEUK, plus the B in my mouth. I am awed by the power of the letters and frustrated that I cannot wield it. Maybe I should cheat again and pick out the letters I need to spell SLASH or SLAY.

Then it hits me. The perfect word. A powerful, dangerous, terrible word. I play QUAKE for 19 points.

I wonder if the strength of the quake will be proportionate to how many points it scored. I can feel the trembling energy of potential in my veins. I am commanding fate. I am manipulating destiny.

My wife plays DEATH for 34 points, just as the room starts to shake.

I gasp with surprise and vindication - and the B that I was chewing on gets lodged in my throat. I try to cough. My face goes red, then blue. My throat swells. I draw blood clawing at my neck. The earthquake builds to a climax.

I fall to the floor. My wife just sits there, watching.
```

---

## IC-2414: Dinah, the Christmas Whore

- Title: Dinah, the Christmas Whore
- Author (byline): David Sedaris
- Work: Holidays on Ice
- Publisher: Back Bay Books
- Publication date as stated: Nov 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2199
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Sedaris
Book: Holidays on Ice
ISBN: 978-0316779234
Publisher: Back Bay Books
Date (Month/Year): Nov 1998
```

### Introduction (context only: never use it for content warnings)

```text
Embedded in our nation's core values is a spirit of community, generosity and a can-do attitude Every day we hear stories of people rising to the occasion and making a real difference: the retiree who volunteers at the local elementary school to help children learn to read; the woman down the block who watches out for her neighbor's kids after school — providing a snack, some wisdom and a home with a light on until parents return from a long day of work; the mothers and fathers in a neighborhood who coach Little League and soccer and teach kids about good sportsmanship and perseverance and teamwork. Who is your home-town hero. In Dinah, the Christmas Whore by David Sedaris, the author finds a new respect for his sister. Dinah, the Christmas Whore by David Sedaris.
```

### Performance text (classify this)

```text
It was my father's belief that nothing built character better than an after-school job. He himself had peddled newspapers and delivered groceries by bobsled, and look at him! My older sister, Lisa, and I decided that if hard work had forged his character, we wanted nothing to do with it. "Thanks but no thanks," we said.

As an added incentive, he cut off our allowance, and within a few weeks Lisa and I were both working in cafeterias. I washed dishes at the Piccadilly while Lisa manned the steam tables at K & W.

I didn't care for the heat or the noise, but other than that, I enjoyed my job. The work kept my hands busy but left my mind free to concentrate on more important matters. Sometimes I would study from the list of irregular Spanish verbs I kept posted over the sink, but most often I found myself fantasizing about a career in television. It was my dream to create and star in a program called Socrates and Company, in which I would travel from place to place accompanied by a brilliant and loyal proboscis monkey.

Maybe in Santa Fe I'd be hit over the head by a heavy jug and lose my memory. Somewhere in Utah Socrates might discover a satchel of valuable coins or befriend someone wearing a turban, but at the end of every show we would realize that true happiness often lies where you very least expect it. It might arrive in the form of a gentle breeze or a handful of peanuts, but when it came, we would seize it with our own brand of folksy wisdom. I'd planned it so that the final moments of each episode would find Socrates and me standing before a brilliant sunset as I reminded both my friend and the viewing audience of the lesson I had learned. "It suddenly occurred to me that there are things far more valuable than gold," I might say, watching a hawk glide high above a violet butte. Plotting the episodes was no more difficult than sorting the silverware; the hard part was thinking up the all-important revelation. "It suddenly occurred to me that…" That what? Things hardly ever occurred to me.

Like several of the other local cafeterias, the Piccadilly often hired former convicts whose jobs were arranged through parole officers and work-release programs. During my downtime I often hung around their area of the kitchen, hoping that in listening to these felons, something profound might reveal itself. "It suddenly occurred to me that we are all held captive in that prison known as the human mind," I would muse, or "It suddenly occurred to me that freedom was perhaps the greatest gift of all."

As Christmas approached, I found my valuable fantasy time cut in half. The mall was crazy now with hungry shoppers, and every three minutes I had the assistant manager on my back hollering for more coffee cups and vegetable bowls.

As the holiday season advanced, so did my impatience. Four days before Christmas we were seated in the dining room, celebrating Lisa's eighteenth birthday, when she received a phone call from what sounded like a full-grown woman with a mouth full of gravel. When I asked who was calling, the woman hesitated before identifying herself as "a friend.. I handed her the phone and watched as she carried it out into the carport, stretching the cord to its limit.

Lisa returned to the table in a hurried, agitated state, asking my parents if she might use the station wagon. "David and I should be back in an hour or so," she said, grabbing our coats from the front-hall closet.

"David who?" I asked. "This David's not going anywhere." I'd hoped to spend the evening in my bedroom, working on the pastel portrait of Socrates I planned to quietly give myself as an anti-Christmas present. We stood negotiating in the dark driveway until I agreed to join her, no questions asked, in exchange for three dollars and unlimited use of her new hair-dryer. Having settled that, we got into the car and drove past the brightly decorated homes of north Raleigh.

“Are we going to meet up with the mother of your boyfriend? How much do you have to pay her to allow him to go out with you? You have a boyfriend, is that it?"

She ignored my questions, quietly muttering to herself as she drove us past the capitol building and into a defeated neighborhood where the porches sagged and a majority of the windows sported sheets and towels rather than curtains. People got knifed in places like this, I heard about it all the time on my radio call-in shows. Had my father been driving, we would have locked all the doors and ignored the stop signs, speeding through the area as quickly as possible because that's what smart people did.

"All right, then." Lisa pulled over and parked behind a van whose owner stood examining his flattened tire with a flashlight. "Things might get a little rough up there, so just do what I tell you and hopefully no one will get hurt." She flipped her hair over her shoulder and stepped out of the car, kicking aside the cans and bottles that lined the curb. My sister meant business, whatever it was, and in that instant she appeared beautiful and exotic and dangerously stupid. LOCAL TEENS SLAIN FOR SPORT the headlines would read. HOLIDAY HIJINKS END IN HOMICIDE.

“Maybe someone should wait with the car," I whispered, but she was beyond reason, charging up the street in her sensible shoes with a rugged, determined gait. There was no fumbling for a street address or doorbell; Lisa seemed to know exactly where she was going. I followed her into a dark vestibule and up a flight of stairs, where without even bothering to knock, she threw open an unlocked door and stormed into a filthy, overheated room that smelled of stale smoke, sour milk, and seriously dirty laundry — three odors that, once combined, can peel the paint off walls.

This was a place where bad things happened to people who clearly deserved nothing but the worst. The stained carpet was littered with cigarette butts and clotted, dust-covered flypaper hung from the ceiling like beaded curtains. In the far corner of the room, a man stood beside an overturned coffee table, illuminated by a shadeless lamp that broadcast his shadow, huge and menacing, against the grimy wall. He was dressed casually in briefs and a soiled T-shirt and had thin, hairless legs the color and pebbled texture of a store-bought chicken.

We had obviously interrupted some rite of unhappiness, something that involved shouting obscenities while pounding upon a locked door with a white-tasseled loafer. The activity consumed him so completely that it took the man a few moments to register our presence. Squinting in our direction, he dropped the shoe and steadied himself against the mantel.

"Why if it isn't Lisa Sedaris. I should have known that bitch would call you."

I would have been less shocked had a seal called my sister by name. How was it that she knew this man? Staggeringly drunk, the wasted, boozy Popeye charged in our direction, and Lisa rushed to meet him. I watched then, cringing, as she caught him by the neck, throwing him down against the coffee table before gathering her fists and dancing in a tight circle, thoroughly prepared to take on any hidden comers. It was as if she had spent a lifetime dressed in a black gi, breaking two-by-fours with her bare hands in preparation for this moment. She never faltered or cried out for help, just gave him a few swift kicks in the ribs and proceeded to carry out her mission.

"Guard him!" Lisa yelled.

Guard him how? Who did she think I was? "Don't leave me," I cried, but she had already gone, and suddenly I was alone with this shattered man, who massaged his chest and begged me to fetch his cigarettes off the sofa.

I heard my sister's voice and looked up to see her fleeing the back room, dragging behind her a clownish, tear-stained woman of an indeterminate age. Her face was lined and puffy. The thick, fat, mottled body had a lot of mileage on it, but her clothing was unseasonable and absurdly youthful. While my mother's crowd favored holiday maxiskirts and turquoise squash-blossom necklaces, this woman had attempted to offset the ravages of time with denim hot pants and a matching vest that, fastened together by a cross-hatching system of rawhide laces, afforded a view of her sagging, ponderous breasts.

"Out!" Lisa shouted. "Hurry, now, step on it!"

I was way ahead of her.

Two young men passed down the sidewalk carrying a mattress, and one of them turned to yell, "Get that ho off the street!"

Had we been in a richer or poorer neighborhood, I might have searched the ground for a gardening tool, fearful that once again I might step on the thing and split my lip with the handle. Ho. I'd heard that word bandied about by the cooks at work, who leered and snickered much like the young men with their mattress. It took me a second to realize that they were referring either to Lisa or to her friend, who was squatting to examine a hole in her fishnet stockings. A whore. Of the two possible nominees, the friend seemed the more likely candidate. At the mention of the word, she had lifted her head and given a little wave. This woman was the real thing, and I studied her, my breath shallow and visible in the cold, dark air. Like a heroin addict or a mass murderer, a prostitute was, to me, more exotic than any celebrity could ever hope to be.

"Dinah, this is David. David, Dinah." Lisa made the introductions after we'd settled ourselves into the car. Apparently, the two of them worked together at the K & W and had come to know each other quite well.

"Oh, that Gene is a real hothead," Dinah said. "He's possessive, like I told you, but, Lord, that man just can't help himself from loving me. Maybe we'll just drive around the block a few times and give him a chance to cool off."

She stared thoughtfully at the street before asking, "Dinah, are you drunk?"

"Yes, ma'am, I am," the woman answered. "I surely am."

"And Gene was drunk, too, am I wrong?"

"A little bit drunk," Dinah said. "But that's his way. We like to get drunk in the winter when there's nothing else to do."

"And is that good for your work-release program? Is getting drunk and having fistfights something that's going to keep you out of trouble?"

Dinah snapped. “Hell's bells, girl, I never would have called if I'd known you was going to hassle me half to death. Turn around, now, I want to go home."

"Oh, I'm taking you home all right," Lisa said.

The sorry neighborhood receded into the distance, and Dinah turned in her seat, squinting until her eyes were completely shut and she fell asleep.

"Mom, this is Dinah. Dinah, this is my mother."

"Oh, thank goodness," my mother said, helping our guest out of her shoddy rabbit jacket. "For a moment there, I was afraid you were one of those carolers. I wasn't expecting company, so you'll have to excuse the way I look."

The way she looked? Dinah's mascara had smeared, causing her to resemble a ridiculously costumed panda, and here my mother was apologizing for the way she looked? I took her aside for a moment.

"Whore," I whispered. "That lady is a whore." I'm not certain what reaction I was after, but shock would have done quite nicely. Instead, my mother said, "Well, then, we should probably offer her a drink." When Dinah spilled her cocktail onto the clean holiday tablecloth, my mother apologized as though it had been her fault for filling the glass too high. "I tend to do that sometimes. Here, let me get you another."

Every gathering has its moment.. I had hated Lisa, felt jealous of her secret life, and now, over my clotted mug of hot chocolate, I felt for her a great pride. Up and down our street the houses were decorated with plywood angels and mangers framed in colored bulbs. Christmas would arrive and we, the people of this country, would gather around identical trees, voicing our pleasure with worn clichés. Turkeys would roast to a hard, shellacked finish. Were I to receive a riding vacuum cleaner or even a wizened proboscis monkey, it wouldn't please me half as much as knowing we were the only family in the neighborhood with a prostitute in our kitchen. From this moment on, the phrase "ho, ho, ho" would take on a whole different meaning; and I, along with the rest of my family, could appreciate it in our own clannish way. It suddenly occurred to me. Just like that.
```

---

## IC-2415: Edgy Rider

- Title: Edgy Rider
- Author (byline): Patrick F. McManus
- Work: Never Sniff a Gift Fish
- Publisher: Holt Paperbacks
- Publication date as stated: September 1984
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2409
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick F. McManus
Book: Never Sniff a Gift Fish
ISBN: 978-0805000313
Publisher: Holt Paperbacks
Date (Month/Year): September 1984
```

### Introduction (context only: never use it for content warnings)

```text
When asked “What do you want to be when you grow up?” one of the top 5 childhood answers is “a cowboy.”Most will never have this dream fully realized, but there’s still the prospect of living vicariously (spurs and all) through your children. “Edgy Rider” by Patrick F. McManus
```

### Performance text (classify this)

```text
As a child I constantly begged my father to buy me a pony. One day I extracted from him the promise that if he saw an inexpensive steed at the auction he would buy it for me. He came home with a pig.

"Where's my pony?" I demanded.

He pointed to the pig. "You're lookin' at it."

I named the pig Trigger.

Naturally, I was enraged. Other farm kids had their own ponies to gallop about on while I had to ride a stupid pig! On the pig's behalf, I'll say that he cared as much for being ridden as I did for riding him.

"Whoa, Trigger!" I'd scream at the pig.

"Oink oink squeeeeeeee!" he'd reply, and race along a barbwire fence in an attempt to saw me into four equal sections.

The great humiliation, though, was when my pony-owning friends would come over to play cowboys. The only one who sat short in the saddle, I always had to be the villain. "Hey, Podner," one of the guys would say to his sidekick, "I think ol' Black Bart is trying to sneak up on us--I just heard his horse oink!" Then they'd laugh.

That fall I had little trouble containing my grief when Trigger was transformed into hams and salt pork. Seldom does one have the opportunity of eating an adversary without being subjected to criticism. Nevertheless, I was still without a suitable steed.

Crazy Eddie Muldoon, who lived on a nearby farm and was also horseless, came up with the theory that cows might be employed as satisfactory mounts. The theory seemed reasonable enough to me, as any wild scheme did in those days, and I agreed to help him test it.

"Since it's my idea, I'll do the hard part,"

explained Crazy Eddie. "That means you get to ride the cow first and have all the fun."

This seemed uncharacteristically generous of him, and I inquired as to the exact nature of the "hard part." He said it consisted of studying the results of the experiment and thinking up ways by which the ride might be improved upon. "And I have to keep a watch out for Pa, too," he concluded. "He's down working in the bottom pasture right now. But we don't want him showing up while you're riding the cow. Understand?"

I understood. Mr. Muldoon was a burly Irishman with a volcanic temper, and he strongly objected to scientific experiments being conducted on his livestock.

With hands locked like sweating vise-grips around the bell collar, and every toe gripping cowhide, I stuck to the back of the Holstein like a hungry, sixty-five pound bobcat, which may have been exactly what the cow thought I was. During the first moments of my ride, I wondered vaguely if Mr. Muldoon's cows were equipped with burglar alarms, for there was a terrible din in my ears; only later did I attribute this fierce clanging to the cowbell.

About midway down the lane, I managed to unlatch my eyelids-a mistake, as I instantly realized, for the first thing I saw was a compounding of my troubles. There, plodding up the land toward us, possibly with nothing more on his mind than the question of what his wife had fixed for lunch, was Mr. Muldoon. Now, unknown to me, the barnyard antics of the Holstein had terrorized the rest of the herd, which was stampeding along immediately behind us. It was this wild and violent spectacle that greeted Mr. Muldoon.

Overcoming the momentary paralysis that accompanied his first sight of us, Mr. Muldoon exploded into furious activity, which consisted largely of jumping up and down and waving his arms. The clanging of the burglar-alarm cowbell prevented me from hearing what he was shouting, which was probably just as well. Perceiving that his efforts to flag down the herd were not only ineffective, but, if anything, were increasing the cows' RPMs, Mr. Muldoon turned and began to sprint ahead of us at a rate that under normal circumstances I'm sure I would have marveled at.

My dismount from the Holstein was facilitated by a low-hanging limb on a tree at the end of the land. I bounced several times, finally coming to rest in a posture similar to that associated with a lump of mush. Fortunately, I had landed beyond the exit of the land, and the herd of cows that thundered close behind showed the good sportsmanship of fanning out on both sides of me. Mr. Muldoon had not been so lucky. When he came hobbling up to see if I was still alive, I noted that he appeared to have been pressed in a giant waffle iron, and one none too clean at that. I choked out the story of the experiment to him, and he showed considerable interest in it, mentioning in passing that he could scarcely wait to debrief Eddie in the woodshed. Crazy Eddie, I might add, was at that very moment in the house busting open his piggy bank to see if he had enough money for a bus ticket to another state.

Years later, my own children began begging me for a horse. At the time, we lived in one of the humbler sections of suburbia, an area which, through some oversight of the planning commission, remained zoned for agriculture. This meant that it was legally possible for us to keep a horse on our two acres.

Contrary to popular opinion, it is remarkably easy to buy a horse, but only if you know absolutely nothing about horses. I found an ad in the classified section of the newspaper that stated: "Good kids' horse, $150." It seemed like a steal. Surely, I thought, at this very moment hordes of eager horse buyers are converging upon the foolish soul who is offering such a fantastic bargain. I dialed the number, and the man who answered--he spoke in the soft, country drawl I had expected--confirmed that indeed he was all but overrun with potential buyers.

"I don't want to sell Pokey to just anyone, though," he told me. "Since you sound like a man who knows horses, I'd be happy to bring him by your place so you can take a look at him."

I said I'd be delighted if he would do that and gave him the address of my spread. Scarcely had I hung up the phone than an old pickup truck with a horse in the back came rattling down my driveway.

A lanky cowboy emerged from the cab of the pickup. Extending a hard-callused hand, he said, "Name's Bill. You the man what's lookin' for a good kids' horse?" He dropped the tailgate of the pickup and ordered the horse, "Step out of there, Pokey." Amazingly, the horse backed up and stepped down out of the pickup. Then the cowboy scooped up our little three-year-old and set her on Pokey's back. I'll swear that horse turned and smiled affectionately at Erin. He walked ever so carefully around the yard, stopping every time she teetered one way or the other until the little girl recovered her balance, and then he'd plod on.

"What'd I tell you," Bill said. "Pokey's a great kids' horse."

There was no doubt about it. While Bill was lifting Erin back down, I was writing out the check. One little incident before Bill departed caused me some wonder about my purchase. As Bill was wringing my hand as though I had just saved his life, Pokey plodded softly up behind him. I assumed the horse was going to give his former master an affectionate goodbye nudge. Instead, he clamped half a dozen yellow teeth onto the cowboy's shoulder. I recall the smirking look in the horse's eyes as Bill danced about, silently mouthing curses as he reached back and twisted one of Pokey's ears until the animal unlocked its jaws. Bill grinned sheepishly, if you can imagine the grin of a sheep that has just been gnawed on by a coyote. "A little game Pokey and I play," he said.

I never saw Bill again. But I can say in all honesty, I really would have liked to, and preferably in some remote area where his shouts for help would have been to no avail.

Within a month, I could not look at Pokey without seeing "glue factory" written all over him. The only thing that saved him from taking up residence on the back side of postage stamps was that the children loved him. And, as far as I could determine, he loved the children. He lived with us for ten years, providing the children with almost as much pleasure as he did the tack-shop owner, the feed store proprietor, the farrier, and the veterinarian. I viewed him largely as a malevolent machine for transforming five-dollar bills into fertilizer for my garden.

I must admit that I had some ulterior motives in acquiring a horse. I did think that the horse might come in handy for elk hunting, so I went out and purchased some of the essential gear for that purpose.

[My wife] knows nothing about elk hunting, but even so I thought her response to my acquisitions was uncouth, to say the least. Personally, I find it unladylike for a woman to stagger about holding her sides while squealing hysterically.

"Laugh all you want," I told her, "but if you weren't so ignorant of the subject you'd know that nine out of ten elk hunters wear cowboy hats. Cowboy boots are the only safe footwear for stirrups--anybody knows that. And the brush on the sides of trails will tear your legs to pieces if you don't have a good pair of chaps. The leather vest--well, you'd just be surprised at how handy a leather vest is when you're hunting elk!"

"B-but the spurs!" she gasped. "The sp-purs!"

I didn't even try to explain the spurs. I mean, if a woman is so ignorant of elk hunting that she doesn't know about spurs, there's no point in trying to educate her.

It had been twenty years and more since I had ridden a horse, or a pig or cow for that matter, so before embarking on Pokey myself I considered it only prudent to study the horse's style while the children rode him about the two acres I now referred to in taverns as the "back forty." With the older children, he would gallop at a moderate gait around the fenced pasture, slowing for the corners and in general taking every precaution not to unseat the young riders. Several knowledgeable horsepersons who observed him thus in action told me I couldn't have found a better kids' horse. I would nod knowingly, chewing on a grass straw as I pushed my cowboy hat back with my thumb.

One day when the kids were off at school, I told Bun, "I think I'll take a little ride on Pokey, just to shape him up for elk season."

"I was wondering why you had your chaps on," she said. "Where are your--hee! hee!--spurs?"

"The spurs are for later," I said, ignoring her mirthful outburst. "Now, come on out to the back forty with me. I may need some assistance."

"Okay," she agreed, "but if you think I'm going elk hunting with you to help you get on and off your horse, you're crazy."

Perhaps it was fate that dictated I would have to suffer insults in my pursuit of horsemanship. The problem was, I had not yet been willing to mortgage the house in order to swing financing for a saddle. Since the children mounted the horse by using the board fence as a ladder, I figured I could do the same. This procedure, however, was made easier if someone held the horse's bridle while the mounting was taking place. I climbed the fence and, while Bun maneuvered the horse up close, I threw a leg over him. So far, so good. I took up the reins and told Bun to step back.

"Giddap," I said.

Nothing.

"Giddap!" I said louder.

Still no response whatsoever. I looked at [my wife]. She shrugged her shoulders.

Once more I shouted "Giddap," but this time I dug my heels into his flanks. Before my hat hit the ground at the starting point, we were at the far end of the back forty. But it was not so simple as that.

The smooth, rhythmic lope with which Pokey carried the children about the pasture had been replaced by a gait closely simulating the motion of a jackhammer--a thousand-pound jackhammer. My eyeglasses flew off, the fillings in my teeth popped loose, my vertebrae rattled like castanets. With the instincts of a natural horseman, I hauled back on the reins. Unfortunately, the motion of the horse had bounced me so far forward I had to stretch the reins far back behind me, and even then couldn't get the slack out of them.

For those unfamiliar with a horse's anatomy, there is a large bone at the point where the neck hooks on to the rest of him, technically speaking. I now found myself astraddle this bone, pounding against it at a rate of five times per second. On the scale of discomfort, this sensation rated somewhere between unbearable and unbelievable, thus motivating me to take defensive action. I flopped forward and wrapped both arms around the beast's neck, a move which had the purpose not only of enabling me to hold on but possibly to strangle the horse into submission. We arrived back at the starting point with me suspended from the horse's neck in the manner of a two-toed sloth from a limb. Pokey came to a reluctant halt, and I dropped to the ground. Calmly, I picked up my hat, beat the dust out of it on my chaps, and strolled over to [my wife].

"Want to see any more trick riding?" I asked.

Despite my air of nonchalance, the ride had taken its toll on me. Suddenly, in fact, I detected what I thought was the symptom of a heart attack--an excruciating pain in my shoulder. Then, collecting my wits, I reached back, got hold of an ear, and twisted it until Pokey unclamped his jaws.

Pokey was truly a great kids' horse. But he hated adults.
```

---

## IC-2416: Fat Boy vs the Cheerleaders

- Title: Fat Boy vs the Cheerleaders
- Author (byline): Geoff Herbach
- Work: Not specified
- Publisher: Sourcebooks Fire
- Publication date as stated: May 2014
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: CRIME REPORTER, GABE, JUSTIN, DEEVERS, MR. DEEVERS, CHEERLEADERS, SHAVER, KAILEY, OFF STAGE VOICE, OFFICER MCCOY, REPORTER
- Teaser before the introduction: Yes
- Spoken words (computed): 1463
- Already set (do not supply): none

### Source block (context only)

```text
Author: Geoff Herbach
ISBN: 978-1402291418
Publisher: Sourcebooks Fire
Date (Month/Year): May 2014
```

### Introduction (context only: never use it for content warnings)

```text
(sound effect from the opening of Law and Order, Special Victims Unit; “chuk, chuk”)

In the juvenile justice system soda-based crimes are considered especially heinous. At Minnekota Lake High School, the purchasers of these sodas are members of a rhythmically challenged squad known as the Marching Band. Their leader? Gabriel Johnson (aka Chunk). This is his story. (“chuk, chuk”)

Fat Boy vs the Cheerleaders by Geoff Herbach
```

### Performance text (classify this)

```text
CRIME REPORTER: (Pg v) Shortly before midnight on June 15th Gabriel Johnson, a sixteen-year-old from Minnekota, MN was apprehended outside Cub Foods. Johnson possessed $17.75 in small bills and change, which he confirmed had been removed from the vending machine at Minnekota Lake High School. Police suggested the alleged robbery was related to a larger conflict involving assault, vandalism, and defamation of character that has come to be known as the Spunk River War.

GABE: (Pg 1) (speaking to his attorney; very nervous) Ripping off the pop machine last night wasn’t meant to be funny. It was my duty to all the geeks, burners and oddballs in this school because that machine sucks. Why are you laughing? I robbed the machine all my myself. It was eighteen dollars, but I lost a quarter when Officer McCoy roughed me up. Look at my chin! I have scrapes all over my stomach and knees too.

(Pg 2) Stupid Pop machine. Stupid pop.

(Pg 7) Hey. Shouldn’t we be talking about how . . . how you're going to keep me from going to jail or something? I’m a little nervous about my crime. (listens for a moment) The whole story, huh? Okay. You asked for it . . .

GABE: (Pg 4-5) Here's the scoop, sir: Purchasers a pop at the Minnekota Lake High School are fat a**es, trailer park kids, addicted gamers and chicks who eat cigarettes for breakfast. Dozens of these kids went back for seconds. Some for thirds (me for instance). Two cheerleaders purchased from the machine, but they both bought diet. That diet stuff will kill you but not make you fat.

JUSTIN: (to Gabe) You drink a lot of pop, Chunk! I’m just sayin’. (indicating Gabe’s size)

GABE: Yeah. Really. I drank a ton of Code Red Mountain Dew every day – 4, 5 bottles – and the only pants that fit me were stretchy pants – elastic waistband, sir. (demonstrates the stretchiness of his waistband) Kids call me fat, butter ball, Eight-Butt Johnson. (Pg 39) Justin was the first person to call me Chunk. He said I looked like this fat kid in an 80s movie. (Pg 5) I knew pop was part of my issue. But see, I also thought it was part of my success. All the vending machine money went to fund the band! I love band! I love band so much . . . I'm a trombone player. That’s one awesome instrument, right? (mimes playing the trombone and marching with pizzazz) I was winning by buying all that pop!

(Pg 13) Okay. So Wednesday morning -- totally evil surprise. Parched, ready for my first Dew of the day, I strolled into the cafeteria and discovered that all pops had been jacked from a buck fifty to $2.25! No longer did I have the proper coinage for three Code Reds. I only had enough for 2. I couldn’t make it through a day on 2 Code Reds! Oh, no, no –

(Pg 17-18) After school Justin and I walked into the principal's office. Without my minimum 3 Code Reds, I was totally wiped and a bit confused and my muscles felt like bags of sand. Mr. Deevers wasn’t happy to see us. Maybe because he’s a central figure in a scheme to defraud students out of their hard-earned dollars?

DEEVERS: What do you guys want?

GABE: Justice!

JUSTIN: (raising his eyebrows, laughing) We're just curious about the sudden steep price increase on the pop machine.

MR. DEEVERS: Come on. Times are tough for education. We’re depending on those proceeds to fund a lot.

JUSTIN: Fund more than just the band?

DEEVERS: (fake smile) Well, ha, ha, there will be an announcement tomorrow. Ha-ha.

GABE: (Pg 20-21) The next day I tried to hold it together by overdosing on the Dew. I robbed Grandpa of 20 bucks. Plucked four 5-dollar bills from his wallet while he fried eggs. Part of the reason my grandpa lives with us is because he's poor. He invested all his money in this power drink called Tiger Lightning. It supposedly had the essence of tiger testicles in it. But the secret ingredient was actually a steroid. Tiger Lightning was sued by the government. Grandpa lost just about everything.

I poured Code Red down my throat all morning. At lunch, I was sweating, probably on the edge of overdosing. I could barely talk. (Pg 23) (bitterly, but with tremors) Turns out that money wasn't even going to my band!

Justin, me and a few others sat at a table in the cafeteria just as Kailey Kaus and the rest of the cheerleaders streamed into the room to put up posters all over.

CHEERLEADERS: [insert your favorite cheer here]

GABE: (Pg 25-26) (reading the poster) YES, THE RUMORS ARE TRUE! THANK YOU FOR SUPPORTING THE NEW DANCE SQUAD WITH YOUR POP PURCHASE! All around they had drawn hearts and stars and smiley faces. It made me want to puke!

(Pg 24) I stared at Kailey Kaus. Let me admit this right now, sir: I used to love her. Used to. Back in elementary school we were more than best friends. We were like a little husband and wife. I was Luke Skywalker and she was Princess Leia. I had a toy light saber (wields it for a moment, then enacts his memories) We attacked the Death Star – We can do it! We raised her dolls together – (in Kailey’s voice) Juniper has a runny nose, Luke, get a Kleenex!

(embarrassed, the returns to the present) I hate her now. She is my enemy. (Pg 25) Those girls laugh behind my back. I’m Eight-Butt Johnson, man. I’m a fat, stupid joke to them.

(Pg 26) (re-living his outrage) This is fraud! We've been bamboozled! Kailey Kaus!

JUSTIN: Don’t be so dramatic. Nobody’s hiding anything. Just relax.

GABE: Bamboozled! (Pg 33) My hands were shaking by that point. (calms himself) (Pg 32) We all got to the band room and Mr. Shaver told us not to take our instruments out.

SHAVER: (Pg 33) (takes a deep breath) I’m very sorry to say there will be no marching camp this summer.

GABE: (audible gasp) (Pg 95) Band has been my life. Who would I even be? Nobody. My horn playing is the only claim to any kind of excellence I’ve got. I really don’t do anything else. (Pg 35) (his worst imaginings begin to build) Maybe the marching band is losing its funding for next year . . . (Pg 154) Maybe the school’s replaced band camp with this, this, this, stripper camp for cheerleaders! (Pg 37) This means war! (launches his pretend light saber again) (Pg 130) Why are you laughing?

(Pg 64) Firstly, all funding for marching camp comes from the pop machine. Secondly, Shaver wouldn’t cancel it unless the money was gone. And thirdly, why cheerleaders? The same week the pop price goes up, the new dance squad is announced. (Pg 96) Who needs music at football games if there’s a bunch of girls in skirts jumping around.

(Pg 265) I'm getting our money back. I decided to redistribute all the money back to the people, just like Robin Hood, man! (beat) (Pg 282) [But] it was a terrible plan, sir – going to waltz into the school, take that money and leave without anyone knowing about it? (Pg 270) Then Kailey showed up. (brief cut to Kailey flipping her hair) (Pg 271) Was Kailey going to bring the whole Minnekota jock establishment down on my head? Was she setting up an ambush? (breaths in deeply, then squeaks) (Pg 280) Hi, there.

KAILEY: Gabe, I am the worst best friend you’ve ever had. I get pushed around by my mom. I get pushed around by [the cheerleaders] I’m so tired of all of these people, Gabe. I don’t want to take your band away (holding back tears) I want to be in your band.

GABE: I really don’t think she wants to be in the band, but that’s pretty sweet of her to say. (to Kailey, starstruck) (Pg 288) You’re pretty cool.

KAILEY: Not really. But now I’m with the leader of the rebellion. Gabe Skywalker, (Pg 281-282) I have a key and codes to the pop machine, we can use the force.

GABE: (Pg 289) (hums Star Wars music) We were Luke and Leia opening a security door in the Death Star. (beat) Of course, we’re stupid. We didn’t have a bag to put the money in. Luckily the change only contained quarters – 18 bucks. (Pg 293) The quarters jingled in my stretch pants pocket. (Pg 292) I took off. I ran! You can do this! I thought. (Pg 130) Why are you laughing?

OFF STAGE VOICE: (Pg 293) Gabe Johnston! Stop where you are! Stop running!

GABE: (skids to a breathless stop one hand in the air, the other holding up his stretchy pants) I stole the money! I stole the money!

OFFICER MCCOY: (Pg 295) (on his shoulder radio mic) Send a car. We got ourselves a little Spunk River ruckus going on. Gabe Johnson. Apprehended.

GABE: (Pg 296) [Turns out] McCoy was looking for me. Not because of the pop machine. Dad realized I was missing – didn’t even try to find me himself – called the cops! They were all looking for me because of Dad.

(Pg 299) Yeah, I'm grounded. I got arrested for robbing a pop machine. That’s a highly ground able business. (Pg 306) I had reporters grab me right away. They knew all about the Spunk River War. (Pg 300) Did you see the front page of the paper? “Fat Boy vs the Cheerleaders.” Better laugh than cry in this case because fat boy is a sexy headline.

(Pg 306) (softer and a bit sad) I was tired of being called names and I’d learned how crappy it is to call people names in general. (Pg 154) (echoing voice) “this, this, this, stripper camp for cheerleaders!” Even if you think those people don't care, they care and it hurts and robs people of their dignity.

REPORTER: (Pg 310-311) Because of Gabriel Johnson’s activism, the offending pop machine has been removed from the high school cafeteria. An increase in county property taxes will be on the ballot in the fall – to fund summer marching camp, a dance team, and most importantly, a healthy breakfast program for all schools.
```

---

## IC-2417: “Fever” from Drums, Girls and Dangerous Pie

- Title: “Fever” from Drums, Girls and Dangerous Pie
- Author (byline): Jordan Sonnenblick
- Work: Not specified
- Publisher: Scholastic Press
- Publication date as stated: Oct 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1971
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jordan Sonnenblick
ISBN: 978-0976103011
Publisher: Scholastic Press
Date (Month/Year): Oct 2004
```

### Introduction (context only: never use it for content warnings)

```text
It’s difficult to explain sickness, and even more so to accept and cope with it. Quite often those who play the audience in a sickness of a loved one have it the worst. A boy struggles with his baby brother’s cancer in “Fever” by Jordan Sonnenblick.
```

### Performance text (classify this)

```text
If you've never been dragged out of a middle-school dance by your mom, while she's wearing sweatpants and carrying your pajama-clad little brother over her shoulder, then you haven't had the same kind of life I'm leading this year.

As she rushed me to the car at breakneck speed, my mom told me what was going on:

We're going to the emergency room. Your brother has a fever.

I looked at the top of Jeffrey's sleeping head, and even in the dim school hallway lights I could see that his hair was all matted with sweat.

Why is that an emergency? What does it mean? Where’s Dad?

Dad is still at his dinner. I don’t know the name of the restaurant and his cell phone might be turned off. Any time your brother gets a fever from now on it’s an emergency. I don't know what this means. Get the door please.

She must have thought the situation was pretty urgent, though, because she usually won't leave the house in sweats, and I noticed she hadn't even taken the time to put shoes on Jeffrey. Also, she's the careful driver in our family on most days, but our ride to the hospital was like the Indy 500. I reached over and crammed Jeffy’s blanket between his head and the corner of his booster seat so he wouldn't get whipped around so much; my hand brushed against his forehead, and he was definitely ragingly hot.

The ER staff didn't mess around at all when we got there. As soon as my mom said the word "leukemia," there were doctors, nurses, and technicians swarming all over.

As they started to take Jeffrey's clothes off: he woke up. I guess he wasn't surprised to find himself in a hospital - both he and my mother seemed to have become used to this bizarre world. He responded to all of the commands that came his way - Tilt your head! Take three deep breaths! Lean forward, -with mute obedience. Until they laid him down, and went for his chest with a needle. Now, I knew that something had been done to Jeffrey's chest in Philadelphia; I had seen the two lines of stitches, and the round bulge under the skin of his ribs. I guess now was my moment to believe in the Port-a-Cath, which was an IV tube that had been surgically implanted under the skin a couple of inches above Jeffrey's right nipple.

Jeffrey pulled away from the doctor when he saw the needle, and asked in a little pathetic voice:

Can't we do the emm-lah?

I didn't know it then, but EMLA is a cream that makes your skin numb.

The doctor's voice softened then, and he almost whispered to Jeffrey: I'm sorry, Buddy. The EMLA takes an hour to work, and we can't wait. Then the doctor half-turned to me, and asked Jeffrey: Would it help if your brother held your band?

Jeffrey didn't respond at all, but he looked at me, and his eyes were brimming. I grabbed his hand, and let him sort of lean his head on my shoulder without sitting up from his pillow. I started the "You're OK, Jeffy" chant, and a nurse scrubbed the circle of skin over the port with yellowish-orange stuff. Then she broke open one of those sterile packets that needles come in, and took out a truly large one, which was bent in the middle at a ninety-degree angle. Jeffrey started to whimper, and the tears began to soak the shoulder of my shirt, but he didn't even flinch as the huge needle jabbed straight into his chest.

Jeffrey kept squeezing my hand really hard for a few minutes, until the blood specimens had all been taken and an IV line was hooked up to his port. I think we both fell asleep for a little while then. When I opened my eyes, the doctor was talking with my mom.

Evidently, Jeffrey had what should have been a simple ear infection, but his white blood cell counts were low because of the chemotherapy drugs he was on, so his body couldn't fight off germs very well. Jeffrey would need to spend a few days in the hospital getting antibiotics through his IV line in addition to his regular chemo medicines. My mom didn't look pleased.

He’ll be here until morning. We’ll put him on a pediatric floor for now, but we're going to have to transport him to a Children’s Hospital in Philadelphia and soon to get his fever down.

My mom started crying then.

I'm sorry Doctor, it’s just all this, all of a sudden, you know? We have very good insurance, but things add up. My husband isn’t…taking it well…

I hear you, Ma 'am. I'll be back around in a few hours –we’ll move you all up to a private room and then maybe you can try and get some rest.

Yeah, sure. My mom looked tired enough to sleep for a week, but I knew she wasn't going to get any rest.

My mom spent a few hours lying on a cot they had brought in, but I really don't think you could say she slept. Every hour or so some medical person or another came in to take Jeffrey's temperature, or attach a new bag to his IV, or do something that would ruin our rest.

At 2 a.m., my mom walked out of the room. I wanted to know what was going on, so after a couple of minutes, I followed her.

Hey, Mom. How long is this going to last?

They're going to run some nests next week. If he’s cancer-free by then, he’ll still be in treatment for a few years. Then, who knows?

Mom, what if he’s not cancer-free next week?

I don't know Steven. I just don’t know. By the way, I’m sorry that we ruined your night.

Right there in the hallway, I put my head in her lap. She stroked my hair for a while, and then she sent me back into the room:

Get some sleep, pal.

At about five in the morning, my dad came into the room (I guess my mom had gotten through to him by phone at some point). My parents spent a few minutes looking at Jeffrey's hospital chart, worked out the details of what needed to be done if my mom and Jeffrey were going to Philadelphia for a week, and went out into the hall to argue about something. I had a little while alone with Jeffrey. He looked really exhausted, but his fever was gone, and he was much more alert mentally than he'd been the night before. He asked me about my dance:

Did I ruin your night?

Mom asked me that, too. Jeffy, you didn't ruin my night. It was ruined from the start. You had a worse night than I did, anyway.

My parents came back in, and I started to get up and leave. Jeffrey asked me for a hug, and I gave him one.

Take care Jeffy, I’ll see you soon, right? Just remember not to throw food at the nurses. I don't want to get any complaint calls, OK?

Steven, I don’t throw food at…oh, it was a joke, right?

Yup, buddy boy. It was a joke. But seriously, no kissing the nurses on their lips, either. It messes up their makeup.

Eeeeeeewwwww!

It was about 7 a.m. when my Dad and I got home. I somehow made it to my bed, and collapsed into a near - coma that lasted until I got too hungry to sleep through lunchtime. It was probably noon or so when I made it to the kitchen. My dad was sitting there, looking stubbly and worn-down, eating a bagel without much of an expression on his face.

I just got the call from your mother. They're taking Jeffrey to Philadelphia in about two hours. She wants us to get his stuff together for him. Do you know what toys and clothed he likes? Can you help me?

My dad looked ashamed at this, like he had asked me to steal him a bottle of Jack Daniels or something.

Sure, Dad.

Your mother thought you seemed upset at the emergency room, and when they put the tubes in . . .

Dad, they didn’t just put tubes in. They stabbed him in the chest. They STABBED him!

I was stunned by what happened next, although I had to admit it was becoming a pretty common occurrence: I started to cry. And once I started, I couldn't stop. My dad wasn't necessarily going to win the Teddy Bear Society's Father of the Year Award, but for the first time in weeks, he reacted. He put his arm around my shoulders, and sort of squeezed me in. We must have stayed like that for a good twenty minutes. My dad finally broke the silence with an old family punch line: So, uhhh, how about those Knicks?

We chuckled awkwardly, but at least it was a chuckle.

Then we went upstairs and packed up Jeffrey's stuff. At the hospital, Jeffrey was looking fairly worried. My mom was out in the hall, arguing with the doctors in Philly on her cell phone. My dad stayed to talk with her, and I went right to my brother.

Hey, Jeffy, how ya feelin?

I'm okay. We had oatmeal for breakfast but it wasn’t as good as yours. I’m scared.

What are you scared about?

Mommy said that they might have to do another bone marrow tomorrow. It was supposed to be next time, but now it’s tomorrow. The bone marrow HURTS. And I might still be very sick if they give it to me early. They said they would do it in a month, and all the bad stuff should be gone. But what if they aren't gone yet? Then they have to give me more throw-up medicine. It’s NO FAIR!

Jeffy, I'm sure the doctors know what they're doing. They wouldn't do the bone marrow this early unless they thought it would be OK.

But it might not be OK. It might realty really not.

Well, buddy, you're in luck. Check out what I brought you. And with a flourish, I pulled his favorite Rescue Hero action figure out of his bag. Look! It’s Matt Medic. He’s here to protect you.

Matt Medic, I'm scared.

Don't be frightened, young man.

He always loved it when I pretended to be one of his toys, and Matt Medic was perfect for the occasion. He carried a huge plastic paramedic pack and a giant gun-like thing that we always pretended was some kind of vaccine syringe.

But what if I'm still very sick?

Well, son, let’s concentrate on my Matt Medic Shot Shooter. It’s full of magic anti-hurt stuff - guaranteed to save your bone marrow. Here we go.

And I used Matt Medic to give Jeffrey a "shot."

That ought to do it. Just remember, you never have to worry when Matt Medic is on the watch. And one other thing: don't kiss the nurses. It gets them in trouble!

My parents came into the room then, and we had the whole obligatory hugs-and-farewells scene. It was fairly touching, all things considered. We said we'd be back together again soon, and that everything would be fine, and at that moment, everyone in the family was united toward the common goal of getting Jeffrey well. The last thing I said to Jeffrey was: I'll see you in no time, pal. Just remember to listen to Matt Medic, and there will be no trouble! As things would turn out, though, there would be a lot more of both time and trouble before we were all in one room again.
```

---

## IC-2418: Forgive Me, Leonard Peacock

- Title: Forgive Me, Leonard Peacock
- Author (byline): Matthew Quick
- Work: Not specified
- Publisher: Little Brown Books for Young Readers
- Publication date as stated: Aug 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: LEONARD, SILVERMAN, GIRL
- Teaser before the introduction: Yes
- Spoken words (computed): 1670
- Already set (do not supply): none

### Source block (context only)

```text
Author: Matthew Quick
ISBN: 978-0316221337
Publisher: Little Brown Books for Young Readers
Date (Month/Year): Aug 2013
```

### Introduction (context only: never use it for content warnings)

```text
Today is Leonard Peacock’s 18th birthday. He is a loner, an outcast, a misfit and maybe one day he’ll believe that being different is okay, important even. But not today. Today he plans to commit suicide. Unless one caring teacher can convince him that the daily battle of not letting the world destroy you is worth the work.

Forgive Me, Leonard Peacock by Matthew Quick
```

### Performance text (classify this)

```text
LEONARD: (Pg 99) In elementary school the teachers always remembered your birthday. There were cupcakes and everyone sang in a way that made you feel really special and a part of something. There’s a reason the elementary teachers did that. It was important. (Pg 110) You know what? F*** Linda for forgetting my birthday. (Pg 9) Linda is my mother. I call her Linda because it annoys her. She says it “de-moms” her. But she de-mommed herself when she rented an apartment in Manhattan and left me all alone to fend for myself most weeks. She checked out of my life – maybe because it was too intense for her to handle. I don’t know. (Pg 110) (Emotions begin to build – a mix of anger and tears) How do you forget giving birth to someone eighteen years ago today? [It’s] IRRESPONSIBLE and selfish and culpable and inhumane and . . . (Pg 170) Let’s get this birthday party started!

LEONARD: (Pg 109-111) I want someone to figure it out to piece together all the hints I’ve been dropping all day long, for years and years even, but no one ever figures it out, and I’m beginning to see why people go mad and do awful things – like the Nazis and Hitler and Timothy McVeigh and Eric Harris and Dylan Klebold did. They all have a lot in common. I bet they felt lonely, helpless, FORGOTTEN, ignored, alienated, irrelevant, cynical and sad.

SILVERMAN: Leonard?

LEONARD: Herr Silverman looks into my eyes until I look back into his. (Pg 114) There have been days when Herr Silverman was the only person to look me in the eye. The only person all day long. It’s a simple thing, but simple things matter. (Pg 110-111) I plead with him using mental telepathy, thinking, “Please just move on. It’s my birthday. I only have a few more hours on this planet. Please. Be kind. Let me off the hook.” The uber-morons roll their eyes and exchange glances. [And] he moves on. (Pg 113) I mostly tune out and wait for class to end so I can be closer to the Leonard Peacock finish line. (Pg 114-115) [But] when the bell rings, I stay seated.

SILVERMAN: (closing the classroom door) So, you wanted to speak with me?

LEONARD: I reach into my backpack and pull out a small box. “This is for you.” It’s the Bronze Star medal my grandfather was awarded for killing some high-ranking Nazi back in World War Two.

SILVERMAN: (Pg 116) Why are you giving this to me?

LEONARD: I don’t know. But I want you to have it, okay? It’s important to me. Maybe you can keep it in your desk drawer and whenever you get to feeling like maybe teaching isn’t worth it anymore you can think of that crazy kid Leonard Peacock who loved your class and gave you [this] as a reward for being an excellent teacher.

Maybe it will help you keep going. I don’t know.

(Awkward silence)

SILVERMAN: (Pg 117) I’m just going to say this, Leonard, and I hope you won’t take offense. Sudden changes in appearance. You did cut your hair, right?

LEONARD: (Pg 11) I have [had] this signature really long dirty-blond hair that [hung] over my eyes and past my shoulders.

SILVERMAN: (Pg 117-118) Giving away treasured possessions. These are clear signs. Suicidal people often do these things. I’m worried you might be at risk. Are you trying to tell me something here today?

LEONARD: (looking down) Not really. I just wanted you to know how much your class means to me. (to audience) I reach down deep within myself and put on the Hollywood face. (smiles and laughs, then speaks to Silverman) I probably would want to kill myself if I didn’t get to spend time in this room every day. Your class is probably the only thing keeping me alive. (long silence) Can I ask you a personal question? (Pg 119) Why don’t you ever roll up your sleeves or wear a short-sleeve shirt?

SILVERMAN: You noticed that, huh? (pause) (Pg 120-121) Are you sure you’re feeling okay?

LEONARD: Yeah, I’m sure. I’m off to see my guidance counselor right now, actually. So even if I were messed up, super-counselor Mrs. Shanahan’ll fix me straight with a root beer lollipop before I leave the building, so no worries, right?

SILVERMAN: (writing down a number on a piece of paper) If I give you my cell phone number will you promise to call me if you feel like you’re going to kill yourself? Call me first so I can tell you the reason I never roll up my sleeves. I bet knowing the answer to that question will make you feel better, but let’s save it for when you’re feeling really bad.

LEONARD: He’s going above and beyond for me. And h e’s also breaking the rules – giving me his cell phone number. No other teacher in the building would do this. And it makes me so sad to think he’ll be really upset when he hears about my suicide.

SILVERMAN: So will you promise me that you’ll call if it gets worse – before you do anything rash? I’ll tell you the answer if you call. It’s a big secret. But I’ll tell you, Leonard, because I think you need to know. You’re different. And I’m different too. Different is good. But different is hard. Believe me, I know.

LEONARD: (Pg 122) If only the world were full of Herr Silvermans. But it isn’t. I don’t go to Guidance. No root beer lollipop today. I have a mission to complete. (Pg 129) I exit my town’s train station, and this girl I had never seen before stuck a piece of paper in my face.

GIRL: The way, the truth, and the light! Read all about it! Jesus Christ died for your sins! Jesus loves you.

LEONARD: (Pg 174) [NOPE!] Hellfire is not in the plans. Heaven is not in the plans. Uber-nothing. That’s what I want. Nothing. (Pg 197) I end up by the river under this little bridge. (Pg 200-206) I’ve got the gun to my temple now and I’m rubbing the side of my head into the metal O. I push the P-38’s mouth harder and deeper into the soft spot of my skull. It’s like the P-38 is an old skeleton key I’m trying to fit into an old padlock and when I make that connection I’ll hear a click and a door will open and I’ll walk through and be saved. (whispering) “Make the lock click, Leonard. You just have to squeeze your index finger and everything will be okay. The thoughts will stop. No more problems. You can finally just rest. I close my eyes. Time comes to a standstill. (screams) (Pg 208) F****!! I bang my fist against the concrete wall, but no matter what I do, no matter how hard I try, I can’t seem to get my trigger finger to work. I just can’t seem to blow my brains out. (searches frantically through his pockets for the paper that Herr Silverman gave to him, he finds it and dials the number on his cell phone – his breathing is ragged and filled with emotions, but as the phone begins to ring, his breathing quiets)

SILVERMAN: (Pg 209) Hello? . . . (silence) Hello? (silence) (then in a softer voice) Is this Leonard? (Silence) Just tell me where you are, Leonard. I’ll come to you. We can talk. I’ll tell you my secret. I’ll roll up my sleeves for you.

LEONARD: (Pg 211) (in a broken voice) It’s my birthday today. No one remembered. (to audience) It sounds so stupid and pathetic and little-kid whiny that I push the P- 38’s barrel into my temple again. (to himself) End this. Just pull the trigger. Make it easier for everyone.

SILVERMAN: Happy birthday, Leonard.

LEONARD: (to audience) Just two words. Happy birthday. It makes me feel like I’m not already gone. Like I’m still here. I lower the P-38 and tell him where I am. ***********

SILVERMAN: (Pg 216) Just give me the gun and everything will be okay.

LEONARD: No it won’t. That’s such a f***** lie! (Pg 41) [I’ve watched adults on the train going to their jobs in the city. They . . . ] just sit there or stand. No one talks. [They] grimly read the paper, angrily poke smartphone screens and barely even blink. I never want to be an adult. (Pg 216) You don’t lie, Herr Silverman. You’re better than the rest. You’re the only adult I really trust and look up to. So tell me something else, okay? Try again. (sarcastically)

SILVERMAN: (Pg 218-219) (steps closer to Leonard, takes off his coat and starts to roll up his right sleeve – he uses his cell phone to light his wrist) Take a look.

LEONARD: (to audience) I don’t see scars or needle marks or anything like that. It’s a tattoo of a pink triangle – what the Nazis used to label homosexuals in the concentration camps. I know because Herr Silverman taught us that. (To Silverman) Who did that to you?

SILVERMAN: I did it to myself.

LEONARD: Why?

SILVERMAN: I tried to be who I thought the world wanted me to be all through high school. Always trying to please everyone else – keeping my true self invisible. It took me 19 years to figure out who I was and another twelve or so months to admit it. I didn’t ever want to forget again. I tattooed my wrist with a symbol. So the answer would always be there. (Pg 220-221) (begins to roll up his other sleeve)

LEONARD: The words are printed in navy blue – simple block letters stacked in two rows. The message to himself and no one else. “First they ignore you, then they laugh at you, then they fight you, then you win.”

SILVERMAN: It’s often attributed to Gandhi. It [makes] me feel strong. [Gives] me hope. [Keeps] me going.

LEONARD: I’m not like you. (raises the P-38 to his temple again) This is me. Right here. Right now.

SILVERMAN: No, it’s not you at all. I’ve looked into your eyes when I lecture. I can tell you get it – you’re different. And I know how hard being different can be. But I also know how powerful a weapon being different can be. How the world needs such weapons. Gandhi was different. All great people are. And unique people such as you and me need to seek out other unique people who understand – so we don’t get too lonely and end up where you did tonight.

LEONARD: (Pg 223) [And then] I tell him everything. Every. Horrible. Stomach-wrenching. Detail. And I’m crying again because I just can’t help it. (Pg 225) (to Silverman) . . . I feel like I’m broken – like I don’t fit together anymore. Like I’ve overstayed my welcome here on Earth and everyone’s trying to give me hints about that constantly. I think that’s why my mom left for New York and why no one wants to talk to me ever. I’m worthless. (looks down at the P-38 and sighs) I can’t even kill myself properly.

SILVERMAN: That’s a good thing . . . That’s a beautiful thing. (Pg 228) Throw the gun in the river, Leonard. rust in the future. Go ahead. Do it. It’s okay. Things are going to get better. You can do the work. (long pause as Leonard considers his options)

LEONARD: I take three quick steps toward the water and throw the P-38 like a boomerang.
```

---

## IC-2419: Freak: A Semi-Demi-Quasi- Pseudo Autobiography

- Title: Freak: A Semi-Demi-Quasi- Pseudo Autobiography
- Author (byline): John Leguizamo
- Work: Not specified
- Publisher: Random House, Inc.
- Publication date as stated: Aug 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JOHN, MOMS, DOCTOR, DAD, HINDI GUY, JAMAICAN RASTA, KOREAN NEWSTAND GUY, POOCHIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1227
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Leguizamo
ISBN: 978-1573226936
Publisher: Random House, Inc.
Date (Month/Year): Aug 1998
```

### Introduction (context only: never use it for content warnings)

```text
(Very formally) John Leguizamo was born in Bogotá, Colombia. His father Alberto was a Puerto Rican realtor when met Leguizamo's mother, Luz.
```

### Performance text (classify this)

```text
(Cutting revised 1/29/2024)

JOHN: (interrupting) (Pg 2-3) I’ve changed my parents’ names to Fausto and Lala, to protect the innocent, namely me. And when I was born, my moms was in labor for forty-eight hours!

MOMS: Desgraciado, get this parasite out of me! Get it out of me now!!

DOCTOR: Push! MS. Liquidzamo, Mrs. Legs and amo, leg of lab . . . Just push ma’am!

DAD: I’m paying you, doctor! Why don’t you pull?

DOCTOR: I am pulling! He’s stubborn.

DAD: Then leave him in there. Get up, woman, we’re leaving,

JOHN: And they wonder why I have problems.

(Shrugs shoulders) I’ll let John tell it his way. Freak: A Semi-Demi-Quasi-Pseudo Autobiography by John Leguizamo

JOHN: (Pg 3-4) My parents left Latin American during the big plantain famine of the late sixties and when they arrived in New York City they had such thick accents they couldn’t even understand each other. My moms got all her English from watching television.

MOMS: Fausto, chock full of nuts is the heavenly coffee, they’re creepy and they’re cookie, that . . . that . . . that’s all folks!

DAD: Woman, what the hell did you just say?

MOMS: How should I know? I’m speaking English.

JOHN: (Pg 5-6) The shuttle from the airport said “Miserable and Huddled Masses” and my pops is like, “This is our bus,” so we jumped on and ended up in the present-day Ellis Island – Jackson Heights, Queens. Our tenement building was like the modern Tower of Babel. When I walked through the streets, I’d see every ethnicity under the sun.

HINDI GUY: You want curry candy?

JAMAICAN RASTA: You people multiply like roaches. Tinga linga ling. Hear the money ring.

KOREAN NEWSTAND GUY: This is not a library, You buy magazine or kick your a**!

JOHN: My parents worked twenty-eight hours a day, fourteen days a week. I’m not bad at math; it’s just that Latin people have to make the most of their time. But my pops always took time out of his busy schedule to tell us his own version of an American bedtime story.

DAD: Once upon a time there was a Little Red Riding Hood and she went into the woods and got a green card and lived happily ever after. Now shut up and go to sleep!

JOHN: (Pg 14-20) Now, our apartment was so puny it wished it were a project. It was a seventies nightmare; our walls were avocado green with brown linoleum and a nuclear orange shag rug. And the centerpiece, the piece de resistance of this mess, was our TV, my dad's pride and joy. It was sacred to him, because my pops could Latinize everybody in America; we would let the screen get real dusty so that everybody looked nice and dark and Spanish. He thought the more you watch it, the more you wear it out. Dad was operating under some kind of third-world logic.

DAD: Don't use my television and don't sit on my furniture unless we have important guests. Use the floor for sitting and the kitchen sink for eating. And we're not gonna buy any more food if you keep eating it! Food, I repeat, is for the guests and the animals. And I just brushed the dogs, so don't pet 'em! And get off the rug, I just vacuumed it. And stop sucking up all my oxygen -- I'm breathing it.

JOHN: My brother and I would be like, "Okay, Dad, okay." Every time my father had something important to say, the subway would go by. And it wouldn't have been a problem, but we shared a wall with the number 7 Train. He'd start lecturing us

DAD: I'm only gonna say this once. The most important thing I want you to do is. . .

JOHN: And sure enough the train would roar by, drowning him out

DAD: . . . or I'm gonna kick you’re a**!

JOHN: Paralyzed with fear, I'd say, "Okay, Dad-no problem." But as soon as my father was out of the house, my brother Poochie and I would be like a Navy SEAL operation. (to Poochie) Now, Poochie, it's 1800 hours, and the Prince of Darkness will be. . . (to audience) Poochie freaked out.

POOCHIE: Prince of Darkness? You didn't tell me nuttin' about no Price of Darkness. Na-ah, I'm not listening. (puts his hands over his ears and closes his eyes) Mamaku mamasa mama mamakusa . . .

JOHN: (yelling) Poochie! The Prince of Darkness is the man you know as Dad. Now you go put the bubble wrap under the rug so when Dad comes through the hall, we'll hear him. Now we're punishmentproof. We outsmarted that ignor-anus! What a maroon! What a suckerbutt! Ha ha! (dancing) Ungawa ungawa, Dad's away for two hours. A beep beep, we're TV freaks. Get stupid. Poochie, turn the TV on. (to audience) Then we'd settle down for a TV frenzy -- Spiderman, Underdog, Gigantor the space robot. Everything was great until I messed with the antenna. (pantomime Spiderman) I'd be swinging around in time to the Spiderman theme when suddenly. . . (freeze) SNAP! The blood drained out of my body and into the ground and back to Latin America. (wailing) Poochie, I broke the antenna! (think rabbit ear antennas on the top of the television)

MOMS: (climbing in through the window) John!

JOHN: (heavy sigh of relief) Luckily it was just my moms. Mom. Why are you climbing in through the window?

MOMS: The rent is due. What are you doing? You're sitting in the furniture. You're eating the food. Ay, dios mio, you broke the antenna!! Oh my God! I'm looking into the face of a dead boy.

JOHN: Moms had a knack for calming me down. (to Moms, hysterical begging) Mom, use me for cruel animal experimentation but don't let him get his hands on me!!!

MOMS: No, don't, don't. I'll miss you. But now I must distance myself. Come, Poochie, you're an only child now. Ciao. Get off me, John. Get off.

JOHN: Then all of a sudden, we hear the sound of snapping bubble wrap . . .

DAD: (cursing) Cono, que es toda esta mierda de bubble wrap, hijo de puta!

JOHN: So, I'm blowing and fanning the TV 'cause my pops would feel it for heat. And my moms goes into rescue mode

MOMS: (whispering) I'll take care of your father. (trying to distract Dad) Fausto, you look so ultra sexy. You look so sexy. Yes, you do. You and me. Okay?

JOHN: But my father wasn’t taking the bait.

DAD: Woman, I just wanna watch my television.

MOMS: Okay, then, why don't you go downstairs and play some pool. Hmm? Okay? Play some pool?"

JOHN: God bless my moms. We didn't have a downstairs. Pops turned on the TV.

DAD: I said no, woman. What’s all that static. I can't tell Sonny from Cher.

JOHN: I'll fix it! I'll fix it! (to audience) So I moved the good piece of antenna for all I was worth. (to Dad) Like this, Dad? Or this? Here?

DAD: Move the other one!

JOHN: (Pantomime frantically while speaking) So I pretended to move the broken antenna. I frantically shifted my body around while holding the broken antenna in place. (to Dad) There? Like so? Perfect?

DAD: Move away from that television. Get out of the room!

JOHN: Okay, I'm leaving the room, the neighborhood. . . (to audience) and as I head for the door, I trip. He sees the antenna came off in my hand. (to Dad, meekly) It's a spear and I'm a hunter? (to audience) I know what's coming next. My pops field-goals me with a kick across the room. Luckily, the nice hard brick wall broke my fall. And I remembered my comics and how Spiderman once said to Ironman: "To escape the pain, one must move toward the pain." And my soul thought, "Yeah, right!" and . . . BOOM . . . The first words out of my mouth said it all: (pointing) Poochie broke the antenna! Poor, slow, chubby Poochie. And I just stood there watching the only brother I had beaten with the antenna, and all I could think was, "Thank God it's not me!"
```

---

## IC-2420: Fruit at the Bottom of the Bowl

- Title: Fruit at the Bottom of the Bowl
- Author (byline): Ray Bradbury
- Work: Twice Twenty-Two
- Publisher: Buccaneer Books
- Publication date as stated: June 1994
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1844
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ray Bradbury
Book: Twice Twenty-Two
ISBN: 978-1568494302
Publisher: Buccaneer Books
Date (Month/Year): June 1994
```

### Introduction (context only: never use it for content warnings)

```text
“Fruit at the Bottom of the Bowl” by Ray Bradbury.
```

### Performance text (classify this)

```text
WILLIAM ACTON rose to his feet. The clock on the mantel ticked midnight. He looked at his fingers and he looked at the large room around him and he looked at the man lying on the floor. William Acton, whose fingers had stroked typewriter keys and made love and fried ham and eggs for early breakfasts, had now accomplished a murder with those same ten fingers.

He had never thought of himself as a sculptor and yet, in this moment, looking down between his hands at the body upon the polished hardwood floor, he realized that by some sculptural clenching and remodeling and twisting of human clay he had taken hold of this man named Donald Huxley and changed his physiognomy..

It was done. He could not change it back. The murder, the sculpturing of clay from warmth to coldness was done, and nobody knew.

Now what? His every impulse exploded him in a hysteria toward the door. Rush, get away, run, never come back, board a train, hail a taxi, get, go, run, walk, saunter, but get the blazes out of here!

His hands hovered before his eyes, floating, turning. They were ordinary hands. Not murdering hands at all-and yet not innocent. He seemed to find them miracles to look upon. It was not the hands as hands he was interested in, nor the fingers as fingers. In the numb timelessness after an accomplished violence he found interest only in the tips of his fingers.

The clock ticked upon the mantel. He knelt by Huxley's body, took a handkerchief from Huxley's pocket, and began methodically to swab Huxley's throat with it. Then he stood up. He looked at the throat. He looked at the polished floor. He bent slowly and gave the floor a few dabs with the handkerchief, then he scowled and swabbed the floor. Then he stopped. There was a moment when he saw the entire house, the mirrored halls, the carved doors, the splendid furniture; and, as clearly as if it were being repeated word for word, he heard Huxley talking just the way they had talked only an hour ago. Finger on Huxley's doorbell. Huxley's door opening.

"Oh!" Huxley shocked. "It's you, Acton."

"Where's my wife, Huxley?"

"Do you think I'd tell you, really? Don't stand out there, you idiot. If you want to talk business, come in. Through that door. There. Into the library." Acton had touched the library door.

"Drink?"

"I need one. I can't believe Lily is gone, that she-"

"There's a bottle of burgundy, Acton. Mind fetching it from that cabinet?"

Yes, fetch it. Handle it. Touch it. He did.

"Some interesting first editions there, Acton. Feel this binding. Feel of it."

"I didn't come to see books, I-"

He had touched the books and the library table and touched the burgundy bottle and burgundy glasses.

The fingerprints were everywhere, everywhere!

"Mind getting the burgundy, Acton, eh? The burgundy bottle, eh? With your fingers, eh? I'm terribly tired. You understand?"

A pair of gloves. . Before he did one more thing, before he polished another area, he must have a pair of gloves, or he might unintentionally, after cleaning a surface, redistribute his identity. Somewhere in the house there must be at least one pair of gloves. He would have until six in the morning, at the outside, when Huxley's friends were to pick Huxley up for the trip to the airport and Mexico City.

Acton hurried about upstairs opening drawers, using the handkerchief as blotter. At the bottom of the eighty-fifth drawer he found gloves. "Oh, my Lord, my Lord!" He slumped against the bureau, sighing. What a wicked plan it had been. Huxley had fallen to the floor, purposely! Oh, what a wickedly clever man! Down onto the hardwood floor had dropped Huxley, with Acton after him. They had rolled and tussled and clawed at the floor, printing and printing it with their frantic fingertips. Huxley had slipped away a few feet, Acton crawling after to lay hands on his neck and squeeze until the life came out like paste from a tube.

Gloved, William Acton returned to the room and knelt down upon the floor and laboriously began the task of swabbing every wildly infested inch of it. Inch by inch, inch by inch, he polished and polished until he could almost see his intent, sweating face in it. Then he came to a table and polished the leg of it, on up its solid body and along the knobs and over the top. He came to a bowl of wax fruit, burnished the filigree silver, plucked out the wax fruit and wiped them clean, leaving the fruit at the bottom unpolished.

"I'm sure I didn't touch them," he said. Which doors had he used tonight? He couldn't remember. Polish all of them, then. He started on the doorknobs, shined them all up, and then he curried the doors from head to foot, taking no chances. Then he went to all the furniture in the room and wiped the chair arms.

"That chair you're sitting in, Acton, is an old Louis XIV piece. Feel that material," said Huxley.

"I didn't come to talk furniture, Huxley! I came about Lily. "

"Oh, come off it, you're not that serious about her. She doesn't love you, you know. She's told me she'll go with me to Mexico City tomorrow."

"Huxley!" William Acton stared at the body. "Did you guess I was going to kill you? Did your subconscious suspect, just as my subconscious suspected? And did your subconscious tell you to make me run about the house handling, touching, fondling books, dishes, doors, chairs? Were you that clever and that mean?"

He washed the chairs dryly with the clenched handkerchief. Then he remembered the body-he hadn't dry-washed it. He went to it and turned it now this way, now that, and burnished every surface of it. He even shined the shoes, charging nothing.

While shining the shoes his face took on a little tremor of worry, and after a moment he got up and walked over to that table. He took out and polished the wax fruit at the bottom of the bowl.

Acton stood a long time feeling the red heart beat inside his shut eyes, within his head.. Got to hurry. Time, time. Only a few hours before those damn-fool friends blunder in!" He turned away.

He went to a writing desk at which Huxley had been seated earlier. He opened a drawer and took out what he was looking for. A little magnifying glass Huxley sometimes used for reading. He took the magnifier and approached the wall uneasily. "

Fingerprints.

"But those aren't mine!" He laughed unsteadily. "I didn't put them there! I'm sure I didn't! A servant, a butler, or a maid perhaps!"

He walked over to the bowl and took out the wax fruit and polished the ones at the bottom and put them back.

"I want to show you my Gregorian cutlery, Acton," Huxley had said. Oh, that casual, that hypnotic voice.

"I haven't time," Acton said. "I've got to see Lily-"

"Nonsense, look at this silver, this exquisite craftsmanship."

Acton paused over the table where the boxes of cutlery were laid out, hearing once more Huxley's voice, remembering all the touchings and gesturings.

Now Acton wiped the forks and spoons and took down all the plaques and special ceramic dishes from the wall itself. . . .

"Here's a lovely bit of ceramics by Gertrude and Otto Natzler, Acton. Are you familiar with their work?"

"It is lovely."

"Pick it up. Turn it over. See the fine thinness of the bowl, hand-thrown on a turntable, thin as eggshell, incredible. And the amazing volcanic glaze. Handle it, go ahead. I don't mind. ..

HANDLE IT. G0 AHEAD. PICK IT UP!

Acton sobbed unevenly. He hurled the pottery against the wall. It shattered and spread, flaking wildly, upon the floor.

An instant later he was on his knees. Every piece, every shard of it, must be found. Fool, fool, fool! he cried to himself, shaking his head and shutting and opening his eyes and bending under the table. He gathered them. Are they all here? He laid them all out neatly upon the shining polished table.

"A lovely bit of ceramics, Acton. Go ahead-handle it."

He took out the linen and wiped it and wiped the chairs and tables and doorknobs and windowpanes and ledges and drapes and wiped the floor and found the kitchen, panting, breathing violently. "I want to show you my house, Acton," said Huxley. "Come along. . . ." And he wiped all the utensils and the silver faucets and the mixing bowls, for now he had forgotten what he had touched and what he had not. Huxley and he had lingered here, in the kitchen, Huxley prideful of its array, covering his nervousness at the presence of a potential killer, perhaps wanting to be near the knives if they were needed. They had idled, touched this, that, something else-there was no remembering what or how much or how many-and he finished the kitchen and came through the hall into the room where Huxley lay.

He cried out.

He polished the floor wildly, He rolled the body over and cried on it while he washed it, and polished the bottom fruit of the bowl and washed the body and doorknobs and silverware and found the hall banister and followed the banister upstairs.

Three o'clock! Everywhere, with a fierce, mechanical intensity, clocks ticked! There were twelve rooms downstairs and eight above. He figured the yards and yards of space and time needed. One hundred chairs, six sofas, twenty-seven tables, six radios. And under and on top and behind. He yanked furniture out away from. walls and, sobbing, wiped them clean of years-old dust, and staggered and followed the banister up, up the stairs, handling, erasing, rubbing, polishing, because if he left one little print it would reproduce and make a million morel-and the job would have to be done all over again and now it was four o'clock! and his arms ached and his eyes were swollen and staring and he moved sluggishly about, on strange legs, his head down, his arms moving, swabbing and rubbing, bedroom by bedroom, closet by closet. . . .

They found him at six-thirty that morning. In the attic. The entire house was polished to a brilliance. Vases shone like glass stars. Chairs were burnished. Bronzes, brasses, and coppers were all aglint. Floors sparkled. Banisters gleamed. Everything glittered. Everything shone, everything was bright!

They found him in the attic, polishing the old trunks and the old frames and the old chairs and the old carriages and toys and music boxes and vases and cutlery and rocking horses and dusty Civil War coins. He was half through the attic when the police officer walked up behind him with a gun.

"Done!" On the way out of the house Acton polished the front doorknob with his handkerchief and slammed it in triumph!
```

---

## IC-2421: Geography of the Heart

- Title: Geography of the Heart
- Author (byline): Fenton Johnson
- Work: Not specified
- Publisher: Scribner
- Publication date as stated: June 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1422
- Already set (do not supply): none

### Source block (context only)

```text
Author: Fenton Johnson
ISBN: 978-0671009830
Publisher: Scribner
Date (Month/Year): June 1997
```

### Introduction (context only: never use it for content warnings)

```text
It is the story of two men: Larry, who has AIDS, and his partner, who does not. It is the story of a healthy man who freely loves an HIV positive man, knowing that he will inevitably have to usher him through to death. But through the pain and injustice of this disease, we learn how, in the end, love allows us to continue, even after death. Geography of the Heart, by Fenton Johnson.
```

### Performance text (classify this)

```text
On a summer evening, not long after Larry and I moved in together, when he was at his healthiest, and it was possible to believe that we would be given two or six or ten years together with the aging cat, we sat on the deck not long before sunset, watching fog peer over the hills. The moon, thinnest of Arabian crescents, was descending into the wired red cage of the radio tower that squats on Twin Peaks. Larry brought out the camera - he wanted to send his parents pictures of the view from the new apartment.

He took photos of the view, then we clowned for each other in front of the camera - more pictures for the overflowing box that now sits at one end of my desk.

Afterward we wrapped ourselves in blankets and watched as the moon freed itself of the radio tower and sank into the fog. We talked a little about this and that - nothing important; end-of-the-day partner talk. I wasn’t paying much attention. I was thinking about all kinds of pressing matters - work – deadlines. Somewhere in the middle of my thoughts he spoke up and said something like this: “Love is like a ripe peach. You take it when and where you find it, there’s no point in letting it sit around. If you’re lucky enough to come across it, you’d better enjoy it right there.”

Later that summer, when he grew really, evidently, seriously ill, I thought, as little as possible but inevitably, of what would become of me after he died. I figured, of course, that a relatively young person who’d lost a great love would have a chance at such love again – after all, that would be only fair.

Then Larry died, and time and more time passed, and I came to understand how fairness has nothing to do with how and when love arrives; that I can be grateful for love only when and while it’s happening, when it’s quite literally in the hand. ***************************

The last day, the first day.

No sleep.

In the middle of the night I phoned and reached Larry’s doctor in his San Francisco office, just as he was leaving for the day. His first question: “How could you let him get that sick?”

The next morning I carried Larry to the car. In the car: accelerator to the floor. Five hours to Paris. Larry slept. At a stop for gas he tried to use the bathroom but was too weak to stand. In Paris: lost, then boxed in a blocked one-way street. Sidewalk driving: bad directions.

At the American Hospital: I couldn’t locate the emergency entrance. I parked at the main door, left Larry in the car, and dashed up the stairs. “Mon copain est gravement malade avec le SIDA.” (My friend is gravely ill with AIDS). My words echoed in the small waiting area, or was it just my imagination. “S’il vous plait madame, je vous prie!” I was begging now. The silent watching waiting room. The receptionist called for emergency staff. Attendants came with a wheelchair and got Larry from the car. The receptionist pushed forms at us. Larry tendered his credit card and signed his name forming each letter with precision and care on a slip of paper whose carbon sits before me now, years later – his last signature.

The doctors: ”Tout va bien” (everything is fine) IV’s, private room, then the move to intensive care, waiting. Late in the evening I returned the car to the rental lot at deGaulle, then spent the night in Larry’s friend’s apartment.

No Sleep.

Next day: I phoned early. The intensive care unit’s head nurse: “Monsieur Rose se repose. Tout va bien.” (Mr. Rose is resting. Everything is fine.) Later I would discover that he had had a heart attack in the middle of the night – that he’d died and been revived. Visiting hours would begin at 2:15. I paced the apartment- might as well be at the hospital. I arrived there late morning and climbed the stairs to the intensive care ward. Entrée Interdite (Entry Forbidden).

His bed was straight across from the ICU door. He saw me and struggled to sit up. He tried to say something about the night before. I made him lie down, put my finger to my lips. “They’ll throw me out if they see me in here.” “Ne pleure pas.” he said – “Don’t cry.”

They saw me there. The head nurse, in forceful English ordered me to leave or she would call security. I left. I walked around an hour, two hours: Je pleure.

At exactly 2:15 I opened the ICU door. He was in the midst of a second heart attack. I saw the cardiac monitor rise, then fall, - the monitor alarm sounded – no one came. I stood frozen, watching, unbelieving, afraid to move for fear of being seen and thrown out. The monitor went dead, flatline.

No one came.

I waited. I waited. The monitor cried, a harsh flat plaintive hum. Zero zero zero.

No one came.

I moved to embrace him, and in my crossing to his bed I was spotted by the nurses’ station. A nurse moved towards me, then noticed the monitor’s blaring hum. Several nurses pushed me aside and rushed to his bed. They began the violent dance of CPR. I backed from the room.

I had no need to witness this.

Five minutes, ten, fifteen minutes. The doctor emerged. “Il vit encore?” I asked, unable to speak in either language any form of the evil word.

“Non. Il est mort. Je suis desole.”

The walls fell away, the floor fell from under my feet, the doctor was no longer there. I was alone, as alone as it was possible to be, falling into a well so deep I didn’t know how deep, falling. In this single moment, my youth fell away, I was no longer innocent, I was no longer young. I embraced all that I had been given and my arms closed on nothing. Now I was falling free, free falling, and as I fell, I thought of all those candles lit, all those wishes made—a painless death, a speedy death, a death with me at hand.

At the American hospital the nurses would not allow me to watch or help as they cleaned Larry after his death. I would not want to see him, they told me, in this state. And I acceded - did I have a choice? They had his body, on which I had no legal claim.

While I waited I thought, “I who have bathed his sores, wiped the sweat from his forehead, embraced him in passion and in need; I who have in some way risked my life to shepherd him to this death - I know his body as none of them know it: I want to know it once more, in the time of his death, but I’m denied this.”

I am, after all, only his friend. ***********************

A large grassy bank cradled in the oxbow bend of a river flowing through a deciduous place, curving past a hardwood forest of oak and hickory and walnut – the landscape of my childhood asserts itself, though here and there a redwood pierces the temperate forest’s profile and the stream runs clear and gravel-bottomed.

I have lived many years in northern California.

The riverbank is populated with men, men who have loved me and whom I’ve loved, and men whom I’ve wanted to love; men I wanted to date but hadn’t the courage or time to ask; men who rejected me, men whom I rejected; men I saw only once, on an airplane, in a bar, on a crowded bus, on a nearly empty beach, in a foreign land, in a classroom, in a church. Many of them are surely ill or dead, but they are all here, sons of the mothers of the world, alive and full of joy on the grassy bank of my heart, here at the cusp of their lives and somewhere in their midst sits Larry, my Larry. Young enough still to be beautiful, old enough to know the meaning of the coolness behind the sun’s warmth; old enough to know that every shadow promises night; old enough to know death.

I cross the river to join them.

We are gathered by a river where we have knowledge of time out side of time, of death outside of death, and there on the grassy green bank of my east-west heart, in the endless low-slanting sun, we give ourselves over to making memory, and remembering.
```

---

## IC-2422: Geometry of Despair: Venn Diagram

- Title: Geometry of Despair: Venn Diagram
- Author (byline): David James Poissant
- Work: The Heaven of Animals, Pg 124-139
- Publisher: Simon and Schuster
- Publication date as stated: March 2014
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2097
- Already set (do not supply): none

### Source block (context only)

```text
Cut from
Author: David James Poissant
ISBN: NSDA Approved Website
https://www.chicagotribune.com/news/ct-xpm-2006-10-29-
0610290005-story.html
Publisher: The Chicago Tribune
Date (Month/Year): October 29, 2006
Also published in
Book: The Heaven of Animals, Pg 124-139
ISBN: 978-1476729978
Publisher: Simon and Schuster
Date (Month/Year): March 2014
```

### Introduction (context only: never use it for content warnings)

```text
Geometry of Despair: Venn Diagram by David James Poissant
```

### Performance text (classify this)

```text
Every Wednesday, after dinner, Lisa and I fight the traffic to the nondenominational church across town. Here, for an hour, a dozen of us sit in a circle telling our same sad stories. Each week, Pam, our counselor, reminds us that it isn't a competition, that the goal of group therapy is not to outdo each. Hardship, she assures us, cannot be measured. But validation awaits those who tell the best stories.

What it comes down to is the following equation: If a train leaves Chicago at 60 miles an hour and another train leaves Atlanta at 80 miles an hour, when they both collide in Kentucky and everybody's babies die, who gets to be the saddest?

Every Wednesday [for an entire year] . . . There's Dot and Drew, whose son was decapitated when he tried to drive home after too many tallboys. Granted, a tragedy, but at least they had him for 18 years. And, hey, if they'd been better parents, who knows?

One week, a weepy, mascara-stained wreck of a woman stops by. She introduces herself as Jenna, tells us her story, and, for a moment, we have a winner. Her 3-month-old dies without explanation, and it isn't until a year later, that her husband admits to shaking the baby. In this way, three becomes two, then one.

Still, my wife says, it's not the same. Jenna has someone she gets to be mad at. Jenna has somebody she can blame. It's like when you're in grade school, Lisa says, and your friend gives you a present, then takes the gift back, only, here, it's God who's the Indian giver.

With SIDS, the despair isn't tied to regret or what-ifs or whose fault. With sudden infant death syndrome, the only thing you want to know--after you wake with the shock that you slept through the night, after you sit up and consider the silence; after you swallow your paranoia and go to the baby, only to feel the warm rush of panic flooding your chest, after the touching, the holding, the shouting, the signing, right here, on the dotted line--after it all, the only thing you want to know is why?

It's a question we ask each Wednesday, a question for which there is no answer. *****

The divorce rate for a couple who loses an infant child is 75 percent. Most couples split up inside of a year. Our own one-year mark [is now] just two weeks away, I've decided that Lisa and I are no exception. It's not that we've stopped loving each other, only that every time I look into Lisa's eyes, all I see is my little girl. The same goes for Lisa. The miracle, really, is that we've lasted as long as we have.

Lying in bed one tired Wednesday night after group, we consider the possibility of separating. It isn't the first time the subject's come up. Lisa hasn't bothered to wash her face before bed, and her eyes are still red and puffy. "You don't have to go, you know," she says. She takes my hand to show me she's taking me seriously, but I can tell she's exhausted, drained by the meeting. I can't face Lisa when she is crying. But, on Wednesday nights, with no emotion left, we can talk about my leaving like strangers discussing the weather.

"Actually," I say, "I kind of think I do."

"We could figure something out."

"No. Not really. You know that. Don't you?" I rub the back of her hand with my thumb.

"I'm just saying," Lisa says. "There's got to be a solution."

"But there isn't," I say. "What happened, it's going to haunt us as long as we're together."

"Maybe if we keep going to group ... " Lisa's voice cracks. She sinks deeper into the covers, lets go of my hand. Beside me, she suddenly looks very small.

"I'd still go with you," I say. "I'm not saying we should to get divorced. I'm just suggesting some time apart, a trial separation."

"Right. Because those always have such happy endings . . . You need time apart," she says. "Not me. You. You don't know what I need."

"What do you need?"

"I don't know," she says.

Both of us are silent for a minute. When I speak again, I choose my words with care. I say: "I just think that maybe I need to leave for a while, you know? Get some perspective. Figure things out."

Lisa sits up. She looks [at] me, and her eyes dance with anger. "Do you ever stop long enough to hear yourself speak?" she says. "Do you even listen to the crap that comes out of your mouth? Why can't you get this through your thick skull? There's nothing to figure out. You keep saying you want to figure stuff out, but what does that mean? It's not an equation, Richard. It doesn't balance on both sides. No matter how many ways you try to solve for X, it won't come out even. You'll wind up with less than you started with, every time."

I don't want to be the one to cry first, but, suddenly, I am.

"You can't escape what's happened by leaving this house," Lisa says. "The only thing you escape by leaving here is me." *****

Have you ever been to a baby's funeral? There's an absurdity to the pageantry: the miniature casket, the floral arrangements done up in pastels. I don't remember anything the minister said. I only remember I couldn't breathe.

Friends and relatives followed us home after the funeral. "You shouldn't be alone right now," everyone said. Lisa nodded, wearing a smile I'd never seen before and haven't seen since. She was determined to do whatever everyone thought was best.

In the midst of all this, Lisa and I started fighting. I wanted to be left alone. Lisa liked the company. I couldn't tell you what was said, but the argument escalated quickly, our voices competing with the din of the crowded living room. I screamed something. Lisa screamed something back. And then ours were the only voices left. In my mind, I was a bird with a broken wing, the neighborhood cats closing in.

"Please," I said. "Go away. Our baby just died. Please. Leave us alone."

"Why do you care?" Lisa snapped. "You never wanted her anyway. It's your fault! You didn't want her and she died!" Lisa collapsed into me, pressed her face to my chest, heaving. And, in that moment, I hated my wife. Her very touch repulsed me. *****

It's true though, what Lisa said. The pregnancy was not what people now call "planned," and I hadn't wanted the baby, not at first. The high school is where we met, where I'd been teaching geometry to teenagers for 10 years. Lisa was the new biology instructor in town.,

A month after the wedding, Lisa gave me the news. "Well, aren't you excited?"

Words tumbled around in my brain, all the words I knew I should say, the words you use for just such an occasion, but none found their way to my tongue.

"Fine," Lisa said.

Within days, though, my attitude changed. Soon enough, Lisa could see that I wanted the baby just as much as she did. Sure we had intended to wait a little longer, but so what? We were having a baby! I was going to be a father! Our daughter was born in June and we named her just that: June.

It was only after June died in July that the subject of my initial reluctance resurfaced. Lisa never mentioned it again, not after the outburst following the funeral, but it stayed with us, a green cloud hanging low in the house. When we fought, I felt her holding back, and, with every argument, I waited--am waiting still--for her to throw the accusation back in my face, as though death were a thing I wished upon our daughter when she was still in the womb. *****

I was the one who discovered June. It's why I don't sleep well at night, why morning sends me rocketing to the cradle that's no longer there, that, for weeks, held only a pillow, a pacifier, a yellow stuffed duck.

At first, Lisa wouldn't let me disassemble the cradle. So, one Saturday, when I knew she would be out for a while, I took the thing apart, packed the pieces into a box, labeled the cardboard with black Magic Marker, and carried the box up to the attic. When Lisa got home, [she] stopped, surveyed the room, and, for the longest time, stood very still.

"What's wrong," I asked, knowing full well the thing Lisa was missing.

"Nothing," she said.

Like everything else, it was easier to say nothing at all. *****

[This] Wednesday, we go to group as usual. It is to be my last night with Lisa. By morning, I've decided, I will be gone.

Pam opens with the usual prayer, the one that concludes with our standard chant: "Lord, grant us peace. Help us rejoice in the hope of your glory. And help us rejoice in our sufferings, because we know that suffering produces perseverance, perseverance character, and character the hope that springs eternal. Amen."

Pam asks who would like to share, and, immediately, Lisa raises her hand. I know that she is going to tell everyone that tomorrow marks the one-year anniversary of June's death.

Before I know what I'm doing, I stand. My chair tips back, falls to the floor behind me. I bellow: "Don't you get it? You people are so superstitious! You keep looking for reasons and meaning and signs! But the truth is, it doesn't mean anything! None of it means anything! There's no good reason for any of it. It's all just coincidence and bad luck and chance. Our kids are dead. We're not special. We're just unfortunate."

When I look up, Pam is in front of me. She places a hand on my shoulder, and, without meaning to, I fall to my knees.

"You're angry," Pam says. "But, I promise you, it gets easier. God will not give you more than you can bear."

A hand touches my face and I can tell, without looking, that it's Lisa's. The words are lost on me. But the sense of touch stays with me, even after I've left the church.

[That night] I fall right to sleep. It's not the same sleep as the last few hundred nights, that anxious, unchained sleep, so that night finds me in the attic, alone with the toys and the dresses and the little white shoes. Instead, nodding off, I feel something holding me down, heavy as light, silent as summer rain. It's like leaving purgatory at last, like sleeping the quiet sleep of the dead. *****

The next morning, I wake, look at the clock. It's nearly 9, impossible, now, to make my escape without causing a scene. I head downstairs, drawn by the smell of coffee. I pause on the bottom step, consider, again, the notion of leaving just to see what I will feel. But, at the thought, I feel neither sorrow nor relief, only the sweet tug of indecision.

In the kitchen, Lisa stands at the window. She is still in her bathrobe, a mug of coffee in one hand, the curve of her neck cradled in the other.

"Coffee?" Lisa says.

"Yes," I say, "please. Thank you."

Lisa moves to the cupboard, the stove, returns with a second cup. I reach out and the mug is hot in my hand. I twist the mug around, hold it by the handle.

"Lisa, I don't want to go." When I hear myself say it, I know it is true. Because it would be the easiest thing in the world to walk out that door. Because, in the end, it doesn't matter which one of us has suffered most, or what has been said, or how we've chosen to manage our sadness.

How do you graph the geometry of despair? Is sorrow, at its heart, a line or a circle? And what is a circle but a line that can't let go? Each of us charts our own path across sadness. Somehow, Lisa and I have met in the middle. At its midpoint, grief is a desert, and it's a long hike back to the basin. I take Lisa into my arms.

"Stay," she says. And it is as if there was never the need for a choice. "Stay," she says, and I do.
```

---

## IC-2423: Georgy Porgy

- Title: Georgy Porgy
- Author (byline): Roald Dahl
- Work: Collected Short Stories of Roald Dahl
- Publisher: South Asia Books
- Publication date as stated: June 1992
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2206
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roald Dahl
Book: Collected Short Stories of Roald Dahl
ISBN: 978-0140158076
Publisher: South Asia Books
Date (Month/Year): June 1992
```

### Introduction (context only: never use it for content warnings)

```text
Today’s society has become all about equal rights and knocking down double standards. The Maneater has taken the dating scene by storm and she’s doing it all in heels. Women have become more aggressive and have decided to take what they want instead of waiting to be chosen. This is all well and good, but NOT for the sanity of our main character. His fragile mind has concluded that the metaphor is more than a colorful description . . . How would you cope if you actually believed that women were the enemy, the attackers, the Man-eaters? Georgy Porgy by Roald Dahl.
```

### Performance text (classify this)

```text
WITHOUT in any way wishing to blow my own trumpet, I think that I can claim to being, at the ripe old age of thirty-one, a moderately well-matured and rounded individual. I speak Greek and Latin. And in addition, I have influenced the lives of others by the spoken word delivered from the pulpit.

Yet in spite of all this, I must confess that I have never in my life--well, how shall I put it?--I have never really had anything much to do with women.

Had I been even the slightest bit ashamed of my own personal appearance, then that might possibly have explained the whole thing. But I was not. On the contrary, and though I say it myself, the fates had been rather kind to me in that regard. Good heavens above, I had seen men who were perfect shrimps in comparison with me displaying an astonishing aplomb in their dealings with the fairer sex. And oh, how I envied them! How I longed to do likewise.

But such things were not for me. Alas, I had to spend my time avoiding them instead. And this, my friends, was easier said than done. My flock, you understand, contained an inordinate number of ladies. There were scores of them in the parish. I tell you I was jumpy as a squirrel.

The spinsters in my parish . . . It's an ugly word, isn't it--spinster? It conjures up the vision either of a stringy old hen with a puckered mouth or of a huge ribald monster shouting around the house in riding-breeches. But these were not like that at all. They were a clean, healthy, well-built group of females, the majority of them highly bred and surprisingly wealthy, and I feel sure that the average unmarried man would have been gratified to have them around.

But [not me] . . . and soon . . . They began to stalk me. I knew they were doing it. I could feel it happening although at first they did nothing definite to give themselves away. The first offender was Miss Elphinstone, a large woman with moles. I had dropped in on her during the afternoon to solicit a contribution towards a new set of bellows for the organ, and after some pleasant conversation, I told her not to bother to see me to the door and I went out into the hall to get my hat. I was about to reach for it when all at once I felt a bare arm sliding through mine, and one second later her fingers were entwined in my own, and she was squeezing my hand hard.

"Are you really so Very Reverend as you're always pretending to be?" she whispered.

Well! All I can tell you is that when that arm of hers came sliding in under mine, it felt exactly as though a cobra was coiling itself around my wrist. I leaped away, pulled open the front door, and fled down the drive without looking back.

The very next day we held a jumble sale in the village hall and towards the end of it I was standing in a corner quietly drinking a cup of tea when all of a sudden I heard a voice beside me saying, "Dear me, what a hungry look you have in those eyes of yours."

The next instant a long curvaceous body was leaning up against mine and a hand with red fingernails was trying to push a thick slice of coconut cake into my mouth.

"Miss Prattley," I cried. "Please!"

But she'd got me up against the wall, and with a teacup in one hand and a saucer in the other I was powerless to resist. I felt the sweat breaking out all over me and if my mouth hadn't quickly become full of the cake she was pushing into it, I honestly believe I would have started to scream.

A nasty incident, that one; but there was worse to come. The next day it was Miss Unwin. Now Miss Unwin happened to be a close friend of Miss Elphinstone's and of Miss Prattley's, and this of course should have been enough to make me very cautious. Yet who would have thought that she of all people. I don't propose to describe that encounter; it was too painful. And the ones which followed were no less savage. Nearly every day from then on, some new outrageous incident would take place. I became a nervous wreck. At times I hardly knew what I was doing. I started reading the burial service at young Gladys Pitcher's wedding. I dropped Mrs Harris's new baby into the font during the christening and gave it a nasty ducking. An uncomfortable rash that I hadn't had in over two years reappeared on the side of my neck; even my hair began coming out in my comb. The faster I retreated, the faster they came after me. Women are like that. Nothing stimulates them quite so much as a display of modesty or shyness in a man.

Is it me, I kept asking myself, who is unwittingly responsible for the shameless way in which these ladies are now behaving? Is it the gleam in my eye (which I cannot control) that is constantly rousing their passions and egging them on? Or is this brutal conduct of theirs inherent in the very nature of the female?

I decided to perform a simple experiment of my own invention, using rats. There were exactly equal numbers of males and females, six of each. I first isolated the sexes, putting them into two separate cages, and I left them like that for three whole weeks. When the three weeks were up, I took a large box that was divided across the center by a little fence, and I placed the females on one side and the males on the other. The fence consisted of nothing more than three single strands of naked wire with a powerful electric current running through the wires.

To add a touch of reality to the proceedings, I gave each female a name. The largest one was Miss Elphinstone. The one with a short thick tail was Miss Prattley. The smallest of them all was Miss Unwin, and so on. The males, all six of them, were ME.

I pulled up a chair and sat back to watch the result. After a while, the first male detached himself from his group and advanced gingerly towards the fence. He touched a wire and was immediately electrocuted. The remaining eleven rats froze, motionless.

There followed a period time during which neither side moved; but I noticed that while all the males were now staring at the dead body of their colleague, the females had eyes only for the males.

Then suddenly Miss Prattley could stand it no longer. She came bounding forward, hit the wire, and dropped dead. Now it was Miss Unwin who began to show signs of impatience. She snorted audibly and twitched a pink mobile nose-end from side to side. She advanced briskly to the wire, pushed her head through it, and was killed. [The remaining females perished in a similar manner.]

The five males stayed where they were, watching the slaughter.

I cannot tell you how much good it did me to watch this simple and rather ingenious experiment. In one stroke I had laid open the incredibly lascivious, stop-at-nothing nature of the female. I felt suddenly very strong and serene in the knowledge of my own innocence.

What I must do now, I told myself, was to weave around me a sort of invisible electric fence constructed entirely out of my own personal moral fiber. Behind this I would sit in perfect safety while the enemy, one after another, flung themselves against the wire. It was in this mood that I set off the very next day to attend Lady Birdwell's tennis party. All around me the little fence was up.

I walked towards the terrace where a group of nine or ten guests were settled comfortably in cane chairs, sipping their drinks.

“Let me fetch you a nice cooling glass of fruit cup" This last sentence came softly from someone just behind me -- a lady of singular beauty. Her name was Miss Roach. "I'm sure you must be tired after cycling all that distance," she was saying now. "I'll get you some," Miss Roach said, smiling at me pleasantly. She stood up and walked over to the drink table. I saw her slicing an orange, then an apple, then a cucumber, then a grape, and dropping the pieces into a glass. Then she poured in a large quantity of liquid from a bottle whose label I couldn't quite read without my spectacles, but I fancied that I saw the name JIM on it, or TIM or PIM.

It seemed a pity to gulp it down quickly after all the trouble Miss Roach had taken to make it, but it was so refreshing I couldn't resist. I had just finished my second big glass of fruit cup when I began to experience a most peculiar sensation. I seemed to be floating up out of my chair, and hundreds of little warm waves came washing in under me. Everything around me seemed to be bobbing up and down and swirling gently from side to side. It was all very pleasant, and I was overcome by an almost irresistible desire to break into song.

"Feeling happy?" Miss Roach's voice sounded miles and miles away, and when I turned to look at her, I was astonished to see how near she really was.

"Terrific," I answered. "I'm feeling absolutely terrific."

Her face was large and pink, and it was so close to me now that I could see the pale carpet of fuzz covering both her cheeks, and the way the sunlight caught each tiny separate hair and made it shine like gold. All of a sudden I found myself wanting to put out a hand and stroke those cheeks of hers with my fingers.

"Listen," she said softly. "How about the two of us taking a little stroll down the garden?" The very next thing I knew, I was sitting inside it on a kind of chaise-longue and Miss Roach was beside me, but I was feeling wonderful. She encircled me with her arms and squeezed my chest against hers so hard that it hurt.

Had Miss Roach or any other female tried to do this sort of thing to me an hour before, I think I would probably have fainted. I might even have died. But here I was now, the same old me, actually relishing the contact of those enormous bare arms against my body! Also--and this was the most amazing thing of all--I was beginning to feel the urge to reciprocate.

"Kiss me," she ordered, “Come on, kiss me."

At that moment, I saw her mouth. I saw this great mouth of hers coming slowly down on top of me, starting to open, and coming closer and closer, and opening wider and wider. I can only tell you that I had never in all my life seen anything more terrifying than that mouth. The strong arms were around me, pinning me down so that I couldn't move, and the mouth kept getting larger and larger, and then all at once it was right on top of me, huge and wet and cavernous, and the next second--I was inside it.

I remember screaming for help, but I could hardly hear the sound of my own voice above the noise of the wind that was caused by the throat-owner's breathing.

Far above me, outside in the open air, I could hear the distant babble of women's voices: "It's not true... "But my dear Mildred, how awful "The man must be mad . . . A sex maniac . . . Someone ought to write to the bishop." . . . . .

Oh dear, oh dear. Looking back on it now, some three weeks later, I don't know how I ever came through the nightmare of that awful afternoon without taking leave of my senses. But they didn't catch me then, and they haven't caught me yet, and if my luck continues to hold, I think I've got a fair chance of evading them altogether.

All the same, this isn't such a bad place, and I have made myself as comfortable as I possibly can. There is one thing here that pleases me greatly, and that is the walls. They are lovely and soft, like a sort of padding, and the advantage of this is that I can bounce up against them as much as I wish without hurting myself.

There are several other people about, but thank God, every one of them is male. For some reason or other, they all wear white coats, and they bustle around pretending to be very busy and important. Sometimes I get so angry and frustrated with them that I lose my temper and start to shout; and then they begin backing slowly away, and saying, "Now then. Take it easy. Take it easy, vicar, there's a good boy. Take it easy."

What sort of talk is that?
```

---

## IC-2424: Get Your Ya-Ya’s Out

- Title: Get Your Ya-Ya’s Out
- Author (byline): David Sedaris
- Work: Naked
- Publisher: Little Brown and Company
- Publication date as stated: March 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2027
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Sedaris
Book: Naked
ISBN: 978-0316779494
Publisher: Little Brown and Company
Date(Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
There’s an old cliche that says you don't marry a person but a family. In-laws are a fact of life, and they can be a great joy and support, or a force to be reckoned with. We've all heard the stories of the overbearing mothers-in-law: the overprotective fathers-in-law and the caravan of aunts, uncles, brothers, sisters and cousins that make up the typical Greek family unit. But you haven’t heard anything until you hear about David Sedaris’ grandmother in Get Your Ya- Ya’s Out.
```

### Performance text (classify this)

```text
It was for many years my family's habit to drive from North Carolina to western New York State to visit the relatives we had left behind. After spending ten days with my mother's family in Binghamton, we would drive the half hour to Cortland and spend an afternoon with my father's mother, the woman we addressed as Ya Ya.

Ya Ya owned a newsstand/candy store, a long narrow room fitted with magazine racks and the high, wall-mounted chairs the townspeople occupied while receiving their shoeshines. She lived above the store in the apartment my father had grown up in.

I recall one visit when she carried on about her recently deceased pet, a common goldfish she kept in a murky jar up on the apartment's only window ledge. Ya Ya had returned from work and, finding the jar empty, decided that the fish had consciously thrown itself out the window.

"He no happy no more and think to have a suicide," she said.

"Commit," my mother said. "He committed suicide. You don't have a suicide, it has you."

"He have the suicide and now I sad sometime." Ya Ya stared into the distance and sighed. I imagine she had spoken to the fish, had loved it the, best she knew how, but her affection, like her cooking, was devoid of anything one might think of as normal.

It was difficult to imagine her raising a child of her own, and chilling to realize that she had. As a baby my father had been confined to a grim corner of the newsstand, where he crawled on a carpet of newspapers, teething on nickels. He never had a bed, much less his own room, and considered himself lucky when the visitors left and he had the couch to himself. "Louie," she would say, patting the hair on my father's knuckles, "Louie and the girl"

"The girl" was what she called my mother. My parents had been married twelve years, and Ya Ya still couldn't bring herself to call her daughter-in-law by name. My father had made the mistake of marrying an outsider, and it was my mother's lot to suffer the consequences. She had somehow tricked him, sunk in her claws, and dragged him away from his people. It would have been all right for him to remain at home for the rest of his life, massaging worry beads and drinking bitter coffee, but to marry a woman with two distinct eyebrows was unpardonable.

"Tell the girl she can sit down now," Ya Ya would say to my father, pointing to a stool on the far side of the room.

"Tell the gnome I won't be staying that long," my mother would respond. "Her cave's a little on the dingy side, and I think I might have an allergy to her mustache."

My mother was pregnant with her sixth child when we received the news that Ya Ya had been hit by a truck. She'd stood wide-eyed in the center of the street, staring down an advancing eighteen-wheeler driven by someone bearing a remarkable resemblance to my mother. That was the way I pictured it. The truth was considerably less dramatic. It seems she had been bumped by a pickup as it backed into a parking space. The impact was next to nothing, but she'd broken her hip in the fall.

"That's a shame," my mother said, admiring her newly frosted hair in the bathroom mirror. "I guess now they'll have to shoot her."

My father flew to Cortland and returned announcing that once she recovered, Ya Ya would be moving in with us. "We'll move a few of the girls downstairs to the basement, and Ya Ya can take the bedroom across the hall from your mother and me, won't that be fun!" He tried his best to make it sound madcap and adventurous, but the poor man wasn't fooling anybody, least of all my mother.

"What's wrong with a nursing home?" she asked. "That's what normal people do. Better yet, you could lease her out to a petting zoo. Smuggle her aboard a tanker and ship her back to the old country, why don't you. Hire her a full-time baby sitter, enlist her in the Peace Corps, buy her a camper and teach her to drive - all I know is that she's not moving in here, do you understand me? There's no way I'll have her moping around my house, buddy, no way."

The longer she lived with us, the more distant my mother became. My father would return home at the end of the day and listen to bitter complaints delivered in two harsh languages; My mother offered to sell the baby, to take a parttime job picking tobacco - anything to raise enough money for a nursing home - but even the cat understood that my father could not place his mother in an institution. It was against his religion. Greeks just didn't do things like that. They were too cheap - that's what has always kept their families together. The conflict divided our family into two distinct camps.

The children formed a committee, meeting in the driveway to discuss our parents' certain divorce. It was reported by Scouts positioned outside the bedroom that my mother had thrown what sounded like an ashtray. A reconnaissance unit was sent and returned carrying a battered clock radio and the real estate section of the newspaper:, the margins penciled with our mother's trademark series of stars and checks. How many bedrooms did the apartment have? Who would she take with her when she left? If we went with our father and Ya Ya, we could be assured of our privacy - but what did it matter, when our mother's attention was what we lived for?

My mother had a wealthy aunt, a calculating and ambitious woman who had married the founders of two Cleveland department stores. The woman died paranoid and childless, leaving the bulk of her estate to my mother, her sister, and a handful of nieces. Having money of her own provided my mother with a newfound leverage. She took to wandering the house reading aloud from the various real estate brochures: "This one's got a full-sized redwood sauna, separate bedrooms for each of my children, and a view of the distant volcanoes. It reads 'Divorcees welcome, no Greeks allowed.' Oh, it sounds perfect! Don't you think?"

The money made her formidable, and within a month, it was decided that Ya Ya would be sent to a nursing home. My father packed her belongings into the station wagon, and we followed behind in my great aunt's Cadillac.

She went first to a private facility, where she shared a room with a sprightly, white-haired lunatic named Mrs. Denardo, who crept out of bed late at night to poop in the hamper and hide Ya Ya's dentures in the chilly tank of the toilet.

She left her apartment only to ransack the community garden, quietly sobbing in the lobby, drying her tears with the tissues used to sculpt the latest holiday display. This was not the picture Capitol Towers wished to present. It was suggested by the management that perhaps she might be more comfortable somewhere else. Legally she met their residency requirements, but spiritually she was just too dark. They began keeping tabs on her, looking for some technicality, and were overjoyed when she fell asleep late one afternoon and set a small fire with her neglected iron. Forced to leave Capitol Towers, Ya Ya took up residence at Mayview, a low brick nursing home located next door to the old county poorhouse. It was a sad place to spend the afternoon, so rather than endure the death rattle of her roommate, my father often brought Ya Ya to the house, where she sat in the carport, staring off into space until it got dark enough to catch a few moths.

She was joining us for dinner one night in the backyard when my father, trying to engage her in conversation, said, "Talk about your shockers, did I ever tell you that Ya Ya found her own brother dead in the middle of the road? The guy was slit from his chin to the crotch, murdered by rebels just. Her own brother! Can you imagine a thing like that?"

"I imagine it every day of my life," my sister Lisa said, tossing an olive pit onto my plate. "How come she has all the luck?"

"Was there a lot of blood?" I asked. "Did he crap in his pants? I hear that's what happens when you die. How old was he? What was his name? Was he cute?"

It was maddening, trying to get information out of her. Here she had a captive audience and a truly gruesome story but was unwilling to share it. My father had told us on several occasions that Ya Ya's marriage had been arranged. She had been sent as a young woman from her village in Greece to New York City, where she was forced to marry a complete stranger, sight unseen.

"Did you have a plan B in case he was deformed?" we asked. "When you finally met, did you kiss him or just shake his hand? How did you know he wasn't related to you? Did you ever date other guys?"

Each time we asked, our questions went unanswered. What we considered newsworthy was just another mundane detail of her life. Her husband, the man we addressed as Papou, had died when I was six years old. He had been in the newsstand late one night when intruders hit him over the head with a lead pipe, rupturing a vein in his head. He was carried to the hospital and died Christmas Day.

"Did you still open presents?" we asked. "After he died, did he crap in his pants? Did the thieves concentrate only on money or did they take magazines and candy bars while they were at it? Did they catch them? Did they go to the electric chair? After they were electrocuted, did they crap in their pants?"

"He go to Jesus now," Ya Ya would say. End of story.

I was in my second year of college when I received the news that Ya Ya had died. My mother called to tell me. My roommate was listening in, and because I wanted to impress him as a sensitive and complex individual, I threw myself onto the bed and made the most of my grief. "It can't be true," I cried. "It can't be true-hu-hu-hu-hu." My sobs sounded as if I were reading them off a page. "A-ha-ha-ha-ha-ha. A-hu-hu-hawhaw-haw-haw-haw."

I flew home to Raleigh the next day. My father had just lost his only mother, and I assumed that, like the rest of us, he felt nothing but relief. He'd been cut loose from his Greek anchor and could now drift freely through our invigorating American waters.

Ya Ya left behind no money or real estate, no priceless recipes or valuable keepsakes, nothing but a sense of release; and what sort of legacy is that? I can’t help but imagine she had started off with loftier goals. As a young girl in Greece, she must have laughed at private jokes and entertained crushes on young stonemasons named Xerxes or Prometheus. When told she would be sent to a new world, I hope she took a few hours to imagine a life of cakes and servants, where someone else would shine her shoes and iron the money. Life had sentenced her to die among strangers.

"When I get like that, I want you to shoot me, no questions asked," my mother whispered. "Disconnect the feeding tubes and shut off the monitors, but under no circumstances do I want you to move me into your basement."

We nodded at the casket - my brother, my sisters, and I - knowing that with her, it would never come to that. Our father, on the other hand would prove to be more difficult.
```

---

## IC-2425: Go Carolina

- Title: Go Carolina
- Author (byline): David Sedaris
- Work: Me Talk Pretty One Day
- Publisher: Back Bay Books
- Publication date as stated: June 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1815
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sedaris, David
Book: Me Talk Pretty One Day
ISBN: 978-0316776967
Publisher: Back Bay Books
Date (Month/Year): June 2001
```

### Introduction (context only: never use it for content warnings)

```text
Go Carolina by David Sedaris
```

### Performance text (classify this)

```text
Anyone who watches even the slightest amount of TV is familiar with the scene: An agent knocks on the door of some seemingly ordinary home or office. The door opens, and the person holding the knob is asked to identify himself. The agent then says, "I'm going to ask you to come with me."

They're always remarkably calm, these agents. If asked "Why do I need to go anywhere with you?" they'll straighten their shirt cuffs or idly brush stray hairs from the sleeves of their sport coats and say, "Oh, I think we both know why."

The agent came for me during a geography lesson. She entered the room and nodded at my fifth-grade teacher, who stood frowning at a map of Europe.. My capture had been scheduled to go down at exactly 2:30 on a Thursday afternoon. The agent would be wearing a dung-colored blazer over a red knit turtleneck, her heels sensibly low in case the suspect should attempt a quick getaway.

"David," the teacher said, "this is Miss Samson, and she'd like you to go with her now."

No one else had been called, so why me? I ran down a list of recent crimes, looking for a conviction that might stick. Setting fire to a reportedly flameproof Halloween costume, stealing a set of barbecue tongs from an unguarded patio, altering the word hit on a list of rules posted on the gymnasium door; never did it occur to me that I might be innocent.

"You might want to take your books with you," the teacher said. "And your jacket. You probably won't be back before the bell rings."

Though she seemed old at the time, the agent was most likely fresh out of college. She walked beside me and asked what appeared to be an innocent and unrelated question: "So, which do you like better, State or Carolina?"

She was referring to the athletic rivalry between the Triangle area's two largest universities. The question of team preference was common in our part of North Carolina, and the answer supposedly spoke volumes about the kind of person you either were or hoped to become. I had no interest in football or basketball but I found it best to ask which team my questioner preferred. Then I'd say, "Really? Me, too!"

Asked by the agent which team I supported, I took my cue from her red turtleneck and told her that I was for State. "Definitely State. State all the way."

It was an answer I would regret for years to come.

"State, did you say?" the agent asked. "I see." She led me through an unmarked door near the principal's office, into a small, windowless room furnished with two facing desks. It was the kind of room where you'd grill someone until they snapped, the kind frequently painted so as to cover the bloodstains.

"And what exactly are they, State and Carolina?"

"Colleges? Universities?"

She opened a file on her desk, saying, "Yes, you're right. Your answers are correct, but you're saying them incorrectly. You're telling me that they're collegeth and univerthitieth, when actually they're colleges and universities. You're giving me a th sound instead of a nice clear s. Can you hear the distinction between the two different sounds?"

I nodded.

It was the first battle of my war against the letter s, and I was determined to dig my foxhole before the sun went down. According to Agent Samson, a "state certified speech therapist," my s was sibilate, meaning that I lisped. This was not news to me.

"Our goal is to work together until eventually you can speak correctly," Agent Samson said. She made a great show of enunciating her own sparkling s's, and the effect was profoundly irritating.

The woman spoke with a heavy western North Carolina accent, which I used to discredit her authority. Here was a person for whom the word pen had two syllables. Her people undoubtedly drank from clay jugs and hollered for Paw when the vittles were ready — so who was she to advise me on anything? Over the coming years I would find a crack in each of the therapists sent to train what Miss Samson now defined as my lazy tongue.

My therapy sessions were scheduled for every Thursday at 2:30, and with the exception of my mother, I discussed them with no one. The word therapy suggested a profound failure on my part. Mental patients had therapy. Normal people did not. I didn't see my sessions as the sort of thing that one would want to advertise, my teacher liked to inform the entire class.

If I got up from my seat at 2:25, she'd say, "Sit back down, David. You've still got five minutes before your speech therapy session." If I remained seated until 2:27, she'd say, "David, don't forget you have a speech therapy session at two-thirty."

My sessions varied from week to week. Sometimes I'd spend the half hour parroting whatever Agent Samson had to say. We'd occasionally pass the time examining charts on tongue position or reading childish s-laden texts recounting the adventures of seals or settlers named Sassy or Samuel. On the worst of days she'd haul out a tape recorder and show me just how much progress I was failing to make. " None of the therapy students were girls. They were all boys like me who kept movie star scrapbooks and made their own curtains. "You don't want to be doing that," the men in our families would say. "That's a girl thing." Baking scones and cupcakes for the school janitors, watching Guiding Light with our mothers, collecting rose petals for use in a fragrant potpourri: anything worth doing turned out to be a girl thing. In order to enjoy ourselves, we learned to be duplicitous.

Our stacks of Cosmopolitan were topped with an unread issue of Boy's Life or Sports Illustrated, and our decoupage projects were concealed beneath the sporting equipment we never asked for but always received.

When asked what we wanted to be when we grew up, we hid the truth and listed who we wanted to sleep with when we grew up. "A policeman or a fireman or one of those guys who works with high-tension wires."

Symptoms were feigned, and our mothers wrote notes excusing our absences on the day of the intramural softball tournament-- a stomach virus or Ted that twenty-four-hour bug that seemed to be going around.

"One of these days I'm going to have to hang a sign on that door," Agent Samson used to say. She was probably thinking along the lines of SPEECH THERAPY LAB, though a more appropriate marker would have read FUTURE HOMOSEXUALS OF AMERICA. We knocked ourselves out trying to fit in but were ultimately betrayed by our tongues. At the beginning of the school year, while we were congratulating ourselves on successfully passing for normal, Agent Samson was taking names as our assembled teachers raised their hands, saying, "I've got one in my homeroom," and "There are two in my fourth-period math class."

Miss Samson instructed me, when forming an s, to position the tip of my tongue against the rear of my top teeth, right up against the gum line. The effect produced a sound not unlike that of a tire releasing air. It was awkward and strange-sounding, and elicited much more attention than the original lisp. I failed to see the hissy s as a solution to the problem. At school, where every teacher was a potential spy, I tried to avoid an s sound whenever possible. "Yes," became "correct," or a military "affirmative." " After a few weeks of what she called "endless pestering" and what I called "repeated badgering," my mother bought me a pocket thesaurus, which provided me with s-free alternatives to just about everything. Agent Samson was not amused when I began referring to her as an articulation coach, but the majority of my teachers were delighted. "What a nice vocabulary," they said. "My goodness, such big words!"

Plurals presented a considerable problem, but I worked around them as best I could; "rivers," for example, became either "a river or two" or "many a river."

It turned out that Agent Samson was something along the lines of a circuit-court speech therapist. She spent four months at our school and then moved on to another. Our last meeting was held the day before school let out for Christmas. My classrooms were all decorated, the halls — everything but her office, which remained as bare as ever. I was expecting a regular half hour of Sassy the seal and was delighted to find her packing up her tape recorder.

"I thought that this afternoon we might let loose and have a party, you and I. How does that sound?" She reached into her desk drawer and withdrew a festive tin of cookies. "Here, have one. I made them myself from scratch and, boy, was it a mess! Do you ever make cookies?"

I lied, saying that no, I never had.

"So," she said, "what are your plans for the holidays?"

"Well, I usually remain here and, you know, open a gift from my family."

"Only one?" she asked.

"Maybe eight or ten."

"Never six or seven?"

"Rarely," I said.

"And what do you do on December thirty-first, New Year's Eve?"

"On the final day of the year we take down the pine tree in our living room and eat marine life."

"You're pretty good at avoiding those s's," she said. "I have to hand it to you, you're tougher than most."

"I tried my best to work with you and the others, but sometimes a person's best just isn't good enough." She took a cookie and turned it over in her hands. "I really wanted to prove myself and make a difference in people's lives, but it's hard to do your job when you're met with so much resistance. My students don't like me, and I guess that's just the way it is. What can I say? As a speech teacher, I'm a complete failure." She moved her hands toward her face, and I worried that she might start to cry.

"Hey, look," I said. "I'm thorry."

"Ha-ha," she said. "I got you." She laughed much more than she needed to and was still at it when she signed the form recommending me for the following year's speech therapy program. "Thorry, indeed. You've got some work ahead of you, mister."

I related the story to my mother, who got a huge kick out of it. "You've got to admit that you really are a sucker," she said.

I agreed but, because none of my speech classes ever made a difference, I still prefer to use the word chump.. . . Go Carolina!
```

---

## IC-2426: The God File

- Title: The God File
- Author (byline): Frank Turner Hollon
- Work: Not specified
- Publisher: MacAdam / Cage
- Publication date as stated: August 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: GABRIEL, THE FEAR FILE, THE CANCER FILE
- Teaser before the introduction: Yes
- Spoken words (computed): 1784
- Already set (do not supply): none

### Source block (context only)

```text
Author: Frank Turner Hollon
ISBN: 978-1931561440
Publisher: MacAdam / Cage
Date (Month/Year): August 2003
```

### Introduction (context only: never use it for content warnings)

```text
What if everything you believed about God fell apart in a single moment? When Gabriel Black’s life collapses into a prison cell, fear and silence fills his mind and belief in God is less than comforting. So, Gabriel starts keeping track, collecting his thoughts and memories in a box he calls “The God File.” There must be some proof of God even in the brokenness of his life.

When everything is taken from you, is faith something you lose, or something you fight for?

The God File by Frank Turner Hollon
```

### Performance text (classify this)

```text
GABRIEL: (Pg 138) (praying) “Now I lay me down to sleep, I pray the Lord my soul to keep. If I should die before I wake, I pray the Lord my soul to take.”

(Pgs 6-13) (to audience) So you say you believe in God? So you say that you see evidence that God exists, and not only does he exist, that he cares about you? (bitterly) Spend almost 22 years in a maximum-security Alabama penitentiary for a murder you didn’t commit and then tell me God exists.

I was here 3 months before my mind would let me read, then I started reading anything with words. Anything. I read a book about a man with cancer. He was a doctor with a supportive wife and blue-eyed kids. His cancer was cured [and] he wrote about his proof of the existence of God and signs that the Lord had cured his cancer. It must be pretty easy to see signs of God’s existence when you’re a rich doctor with a wonderful wife and children, cured of cancer and writing stories about pretty visions.

[But] it would really be a test to find this evidence in a nasty place like this, with no real freedoms, surrounded everyday with fear, hopelessness, and people who live like rats. So, I started a file. The God file. A cardboard box filled with envelopes and notes. The file has gotten fat. A brown box kept underneath my bed. I’ve believed and disbelieved a thousand times.

GABRIEL: (Pg 6-13) My name is Gabriel Black. I was 25 years old when I first saw Janie. She was married and didn’t care. I had no direction; no purpose. She became my purpose. A living, breathing, everyday reason. I knew the moment I met her something bad would happen. I knew the whole thing was wrong when I decided to be with her. And the price I paid came a thousand decisions later, in an apartment on a Saturday morning.

Janie’s husband had called the day before. I imagined his fat-wheeled Ford truck driving past the apartment. He was bigger than me, unpredictable and pissed off. I imagine every night that he slept alone was a reminder of what he’d lost – Janie. (beat) Since the dawn of time men have been killing each other over *women.* We will kill each other faster of *women* than anything else, including food, shelter, even religion.

I was sitting on the couch at 8:30 on Saturday morning when the front door busted open. Janie’s husband’s shoulder hit the wood and the doorframe splintered. Janie came out of the bedroom, with a gun in her hand. There was no time to speak. Before my gaze lifted, she fired twice into his chest. I saw the holes explode open. Her husband fell to his knees, and his face cracked against the glass of the coffee table, which shattered into a million specks of light. And then it was quiet.

I will never understand the reasons I did what I did next. Love? Honor? Loyalty? (beat) I took the gun from her hand, wiped it clean, and holding it in my right hand, I fired once at the far wall to get the smell on my hands.

I looked at Janie, and said, “I killed him. You were in the bedroom sleeping; you heard the shots and came out. Wash your hands, someone will be here any second.” [She] didn’t hesitate. Turns out the gun was stolen. The apartment? In the dead man’s name. She met with him the day before. Could she have planned it? Known I would take the blame? She’s never come to visit me, ever. The only time I saw her again was in the courtroom 22 years ago. She sat stone-faced with the angry relatives of her dead husband.

Guilty. Capital murder. Life in prison without parole. (beat) Does God exist? I set out to look for God in the tiny details, to find out for myself. All I have is time . . . So, I put together a file, to look for God in the tiniest details. (shuffles through his box and selects a file folder)

THE FEAR FILE: (Pg 28-31) (he reads) The two most traumatic events in our lives are birth and death. The fear of each is a gift. Fear lets us know when we are in danger. It can’t be separated from our survival instinct.

(stops reading to tell his story) [But] once you start removing the fear, how do you know when to stop? The world is divided into warriors and non-warriors.

(Pg 39-43) The first time I was raped in this place, I thought about my daddy. I’d only been here a week – had no idea what it takes to survive. I was small and walked with a limp. I was selected for my weakness, like animals separate the herd. It ain’t got *nothin’* to do with pretty. There were three of them. I fought like a dog, bit and scratched, felt the punch shatter my ribs and suck the breath from my lungs. They thought it was funny.

When it happened the second time, I was ready. I fought until they thought I was done fighting, and then I cut the man with a piece of a razor. It was the last time they tried. The risk and the reward were no longer equal. You should have seen his face that split second from the time he saw what I had done until the pain shot up his backbone. (beat) Sometimes God hides Himself in the cracks between words. (Pg 65) They say that God never puts more on you than you can carry. When He does, when He goes too far, how will I know? (selects another file from the box)

THE CANCER FILE: (Pg 32-36) My mother died of breast cancer when I was 19. I came home from the Army on emergency leave. She had given me no warning. Maybe she had none. The doctor said, “The cancer is eating her up inside,” like he was angry. Like he couldn’t understand any more than I could why God would let evil black cells chew up my mother’s breast from the inside out and leave her choking up blood on the white sheets of someone else’s bed. They put crosses on the sides of highways where people die in car wrecks. Nobody put a cross in the hospital bed where cancer killed my momma. (long beat) Are we so afraid of cancer that we let it take who it wishes, as long as it leaves the rest of us alone. Abandoned by God for letting it do what it wants? (beat) [At least] Momma never had to see me in shackles. She never had to sit in the courtroom, torn between the love of her child and hatred. She never had to see me go to prison, or lie awake at night and wonder what unspeakable thing was happening to her boy in a prison shower.

(Pg 123) (long beat) I used to believe that the proof of God in suicide was my decision to choose AGAINST it every day. I know that the option is the gift. We don’t condemn the man in physical pain, with incurable cancer, when he takes his own life. But there’s pain in this world worse than any physical pain that might wrack this body of mine. God gave us a soul [and] with the soul comes the capacity to hurt worse than any animal or beast. Not only can we feel this pain, but we can understand it and put it in words. (struggles to contain the pain he feels) I have asked myself the question a million times, “If God gives me more than I can endure, how will I know?” He’ll bring me home, that’s how I will know. (beat; he begins to fashion a noose from his bed sheets and continues this process as he speaks)

(Pg 73-74) People seem to turn towards God when they have lost control of their lives. There is no place in the world like prison to make a person feel lost. I have watched men sit in their cells and read the Bible all day long. Every day I am told where I will sleep, when I will eat. My mail is opened, my room is searched. Others decide my choices of books, clothes, toilet paper, food.

[But] I have tried hard not to make my decisions about God from a position of fear or loneliness or loss of control.

(Pg 107-109) I have read books of theology and the history of religion. But the real evidence of the existence of God is my existence itself – the existence of a human being. They write that the definition of a Christian is the belief in Adam and Eve, and the definition of a nonbeliever is the person who has allowed the science of Darwinsim to rot his soul. It isn’t that easy. Or maybe it isn’t that complicated. (thoughtful) If I were God, I would use time to create my most wonderful creation, a person. God is in no hurry. The Earth, the oceans and other animals and plants existed before we did. The battleground of evolution and Adam and Eve? Same God, same idea, same tool. Only God could use time and only time could make a person, any person.

(Pg 152-154) In my years of keeping the God file, I have come to believe that the greatest evidence I have of God’s existence is not me, but is the search itself. I have to believe that God sent me on this search, and the search itself has nourished and sustained me. It’s the most obvious gift from God, and it has been in front of me every single day.

We’re taught to believe that there is a hierarchy in the closeness of God. (places the noose over his head) But at this moment, this exact moment, no one could be closer to God than I am. I can close my eyes and feel His arm around me, tight and sure, like I was a little boy again.

(long beat as he breathes in an out deeply) (Pg 129-130) We forget the stillness of silence. I search my memory for the sounds in my life that stand apart and can still make me feel the way I felt when I heard them for the first time: My mother crying (voice cracking with emotion) . . . (Pg 138) “Now I lay me down to sleep, I pray the Lord my soul to keep. If I should die before I wake, I pray the Lord my soul to take.” (Pg 129-130) The sound of my mother crying made me feel more worthless and alone than any sound in my life. I wish I could hear it one more time to know she was in the room next to me.

(he startles) The sharp sound of Janie’s gun firing the first bullet. (beat) The sound of the prison door closing behind [me] The heavy, iron vibration. This sound would be one I would always remember.

(Pg 156-157) (tightening the noose; he speaks as he loses consciousness) And I begin to move. Gently toward the soft, white light. Pulled by the strings of faith. And suddenly there is a sense of leaving something behind. . . (Pg 138) “I pray the Lord my soul to take.”
```

---

## IC-2427: Goin’ Fishin’

- Title: Goin’ Fishin’
- Author (byline): Chris Crutcher
- Work: Athletic Shorts: Six Short Stories
- Publisher: Harper Tempest
- Publication date as stated: Nov 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2072
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Crutcher
Book: Athletic Shorts: Six Short Stories
ISBN: 978-0060507831
Publisher: Harper Tempest
Date (Month/Year): Nov 2002
```

### Introduction (context only: never use it for content warnings)

```text
Goin’ Fishin’ by Chris Crutcher
```

### Performance text (classify this)

```text
There is a case to be made that from the time of birth our lives are made up of a series of losses and that our grace can be measured by how we face those losses and how we replace what is lost.

Lionel Serbousek lost his parents in a boating accident when he was fourteen years old. Though he continues to explore his passions, athletics and art-with fervor, he remains haunted by his memories of that day on the lake and "what could have been. . . ."

Like most of us, when his pain is the greatest, he covers it with anger, anger approaching rage. That rage has the power to consume.

My name is Lionel Serbousek. I'm a high school senior, an artist and a swimmer, and I'm also an orphan. I can tell no story about my life without telling this one first because it colors everything I do; everything I think.

I woke up on a bright Sunday morning almost 3 years ago to go fishing over in Lake Coeburn with my family, and everything was about as normal as it could be. At the beginning of that day things couldn't have been better, but by sundown I felt as alone as if I'd been hatched from an egg by the sun.

I think if human beings had even the slightest ca-pacity to foretell the future, we'd be a completely different animal. In the moment that I helplessly watched my family's death unfold before me, I wished I'd lived differently, done my chores on time, told no lies, eaten my vegetables, thanked my parents for giving me a room of my own, told them I loved them, been a better big brother for Kyle.

The person who killed my family was my best friend. His name is Neal Anderson. I still get a card every Christmas from his family, but I have avoided him like AIDS since the day of the accident.

Neal wasn't supposed to be driving his parents' boat that day.

********************************

My father was a head shaker. He was one of those adults who believe that if you take time to tell your children things, they'll grow up believing them and act accordingly. Anytime that failed to happen, Dad would simply shake his head slowly. With me, Dad shook his head a lot.

If I'd known Dad was going to die, I'd have made a special effort to decrease the number of times a day he felt compelled to shake his head. But I thought I had more time. I thought I had all of time.

Fishing was a metaphor for life with my father. It required patience, knowledge, and skill. It wasn't frivolous, and on a good day you were rewarded immediately for doing it right, though certainly there were no guarantees. You could kid around with him about some things, but fishing wasn't one of them.

***************************

That day we were dead still in the middle of the lake in early afternoon, fishing deeper water, when Neal and his buddies, at least two six-packs into the after-noon, decided to take a quick spin in his dad's Sun Runner. Nobody in our boat but me even saw them coming. I hollered; but Mom and Kyle were hauling in a fish, and Dad was shouting advice. They didn't even look up.

And I jumped. I jumped.

I've watched it over and over, always knowing if I'd stayed a little longer or yelled a little louder, I could have saved them.

Neal's boat cut ours in half. None of my family even bobbed to the surface. Kyle's shirt floated near the wreckage, and I dived as deep as I could, only to be surrounded by blackness. I didn't know it was Neal at the time, but I got hold of him and did my very best to drown him. I held him under with both hands on his throat, and it took all the other two had, plus help from a guy who saw it all from a passing boat, to pull me off.

Swimming saved me. I took out my pain on the water. The louder the whine of the approaching Sun Runner echoed in my head, the clearer the sight of splintering fiberglass and flying bodies, the harder I swam. And slowly but surely the searing edge began to dull. I don't know if time heals all wounds, but I know it at least slows the spiritual bleeding.

*****************************

Elaine -- she was there for me always after the accident. She sensed when my loneliness was ready to smother me and would show up with food or friends or just her wonderful self. I never loved her, not like a girlfriend; but I cried with her, and I told her everything. Elaine Ferral knows my soul, and more than anyone, she walked with me through the land-mined terrain of my grief.

I really thought I had it all in perspective, but then, about a week ago, Neal Anderson showed up at my door. I haven't seen him since the day he killed my family. And that's a good thing, because when things are at their worst, and I want someone to blame, Neal's my man.

I stared at him through my open door. "What do you want?"

"Can I come in?"

I barely recognized him, wouldn't have if I hadn't heard his voice. His dishwater brown hair was stringy and unkempt, hanging to his shoulders; his clothes were dirty and threadbare. I considered a moment and said, "No." I was instantly aware of my rage.

"Come on, man. I need to talk to you."

"Anderson, if I let you come in my house, I'll probably hurt you. In fact, I might anyway. You must be out of your mind. What the hell are you doing here?"

"Trying to give myself a chance."

"A chance to what?"

"To make it right."

"Anderson, turn around. Walk down those stairs. If you see me on the street, at a dance, or in a pizza place, or even at a gas station, stop what you're doing and run. I'll let you know if it's ever different."

He started down the rickety stairs, then turned back about halfway down. I noticed how thin he looked, how raggedy. All his athleticism, that confident gait he had was gone. He said, "I'm not leaving because I'm afraid you'll hurt me. Nothin' you could do to me would matter. I'm just leavin' because you want me to."

************************************

It was later that night when I realized how vicious I'd been. And it felt good. That night I realized it's my rage that's kept me alive over these three years, not friendships. Make no mistake about it; if I had been left alone in the water with Neal that day, I would have drowned him. And I have never trusted for a moment since what I might do if I ran into him. Now he was feeling some of what I've felt over the past three years, and for all I cared, he could waste away to nothing.

Shortly afterward, my phone rang. "Hello. Make it fast."

"Lionel, this is Vicki Anderson."

Neal's mom.

“Listen, Lion, I need to ask you a favor. A big favor. I'm calling about Neal. I know he came and saw you today."

"Yeah."

"Lionel, he's dying."

"Like my parents. My brother."

"Slower. Lion, I've never known what to say. I'm so embarrassed we haven't contacted you. I pray for you every night of my life. Neal's father has set up a trust for you . . .”

"Mrs. Anderson, money isn't going to bring my family back."

"If money could have brought your family back, we'd have already done that. It's just all we have."

"So what about Neal?"

"He needs you to forgive him."

"Won't happen. He killed my family."

"Lionel, he hasn't lived with us for more than six months. He's on the street. I think he's using drugs. I can't talk to him. He's dying, Lionel. Please, if not for him, then for me. For his father."

Until that moment I hadn't the slightest inkling of the true power of my hate. The sorrow that rose in my chest for Mrs. Anderson was crushed by it. I said, "Mrs. Anderson, I'm sorry. But do you know what it's been like inside me for the last three years? Do you know how many times I've watched my parents and my little brother get cut in two? Do you know how much I've missed them? Mrs. Anderson, if I thought I could spend fifteen minutes with my little brother starting at the moment of my death, I'd be gone tonight."

"I'm sorry, Lionel. I'm sorry I bothered you."

I snatched my Speedo and a towel out of the bathroom and headed for the pool at Frost. I started with twenty-five-yard butterfly sprints, giving myself fifteen seconds between. I have no idea how many I swam, but my chest and triceps were molten steel when I pushed off and saw a body knife into the water beside me. I finished the lap and looked up to see Elaine.

"Go ahead and leave, I'm okay. I want to be alone."

"Tough shit."

"Elaine, get out of here. I don't want to talk to anyone:'

"What're you gonna do, Lion? Beat me up? Like you did Neal Anderson. Or his mom."

"Hey, don't start. We go back a long way, but-"

"It's not a question of how far we go back. It's a question of if we'll go forward. You treated Neal Anderson like shit today."

"Neal Anderson is shit.”

"It's for sure no one could tell you anything. What would your dad say? I knew your dad, Lion, and he'd call game on this cheap bullshit in a second. And your mom-"

"You leave my mom and dad out of this! I'm warning you, Elaine."

"Wanna hit me, Lion? Go ahead. That do it for you? Maybe that's what you need. Start right here with me, Lion. Go ahead."

My fist clenched, and my upper lip vibrated like a jackhammer, and she punched me in the stomach so hard the wind blasted out of me like a released party balloon.

"You double up your fist at me you better be ready to I use it. You make me sick, Lionel Serbousek. When your family got killed, your friends gathered around you like angels. We spent the last three years making sure nothing touched you, treating you like some kind of boy in a bubble or something."

"You can cancel your friendship out anytime. What the hell is the matter with you, Elaine? Neal Anderson killed my family! If I ever quit hating him, I - I-I'll die right with them."

I dropped to the bleachers like a rock, dazed at what I had just heard myself say.

"Lion, remember the night you and Walker and Jeff and I drank all those beers and you took us out on the ice up at the lake? None of us knew the ice would hold-and it was four miles over icy two-lane roads to get there. You could have killed us. Easy. You were drunk out of your mind. What if you'd killed us, Lion, and you'd lived?"

"Yeah, well, I didn't. . . ."

"No, but you could have. What you did was more stupid than what Neal did. Only thing is, the universe caught him and it didn't catch you. That's the only difference. . . . . Think about it! Think about it, Lion! . . . . "You only get so long to be an idiot, Lion. Just so long to get decent again. Your time's about up."

**********************************

It was my third night searching for Neal. His gaunt face had haunted me since Elaine stalked away from me; Mrs. Anderson's pain over the phone had become real. And the thought of losing Elaine lay in my stomach like a sharp rock.

I searched more than an hour and was finally ready to leave and try again tomorrow nightwhen I saw a dim light between the slats of the wooden bridge.

"Neal?"

He looked up dreamily, eyes glazed. His mom was right about the drugs.

"Lion? I killed your mom and dad, man. And your little brother."

"Yeah. Look, Neal, I'm not over this yet, but we need to talk. Pack your stuff. Maybe you and me oughta go fishin'."
```

---

## IC-2428: Going Home

- Title: Going Home
- Author (byline): Jason Sheets
- Work: Turning Points, Pgs 131-134
- Publisher: Tichenor Publishing
- Publication date as stated: Jan 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MACK, MAN, CRAIG
- Teaser before the introduction: Yes
- Spoken words (computed): 1171
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jason Sheets
Book: Turning Points, Pgs 131-134
ISBN: 978-0742117013
Publisher: Tichenor Publishing
Date (Month/Year): Jan 2001
```

### Introduction (context only: never use it for content warnings)

```text
A recent study of people over the age of 60 reports that the condition they are most afraid of is Alzheimer’s. As people age, slight memory loss is normal; but Alzheimer’s is an irreversible, progressive brain disease that slowly destroys memory, causes erratic behavior and robs a person of their personality.

For someone in the early stages, the experience can cause fear. Suddenly, they can’t remember people they know or follow what others are saying. They can’t remember why they went to the store and may get lost when they are . . .

Going Home by Jason Sheets
```

### Performance text (classify this)

```text
NARRATOR: All the world's a stage, and all the men and women merely players: they have their exits and their entrances; and one man in his time plays many parts” (Pgs 131-134) Sometimes you laugh at yourself when you do it. After all, you have never even liked reading Shakespearean poetry. Still, every day from 9:00 until 10:00 in the morning you not only read it; you memorize it. You remember hearing that memo-rization keeps the mind active. You have given up on being physically active long ago, so you are making sure you can at least pride yourself on having a sound mind. You've heard all the jokes about it -- how you can meet new people every day and be able to hide your own Easter eggs. You have seen it happen to your friends. You have watched them slip away. You pray that you die before it happens to you.

NARRATOR: Through the years, you have found that few things in life last as long as you'd hope they would, whether that be your eyesight, your friends, your teeth. This is what makes Mack special. He's been your golf partner and beer buddy since you finished law school 35 years ago. He definitely has not grown old gracefully. He dons a baseball cap inscribed with the words "Old Fart" on it and he golfs in these knickers that people constantly complement him on. Secretly, they laugh at him.

Bigger memories are starting to elude him now. He used to lose track of the time or forget his score on a golf hole. Now, he's lucky to remember his tee time. After he hits the ball he forgets where it went. He wanders down the fairway near the woods, desperately searching. When you direct him to his ball, he informs you that he doesn't need your help and walks in another direction. You ask him where he is going.

MACK: Home, I'm going home."

NARRATOR: You nod "goodbye" and watch him walk away. He'll return tomorrow.

You think of Mack when you open the books of Shakespeare the next morning. You thumb through the pages for a poem to memorize. A short one today, you tell yourself; Jeopardy comes on at 9:30. The poem reads: "Shall I compare thee to a summer's day?" You find this to be drivel, but you memorize it anyway. It'll come in useful someday, you tell yourself. Whenever people need a Bingo break you'll pipe out a few lines of ol' Billy Shakespeare and they'll all be stunned. Sure, it'll happen.

The word "Alzheimer's" is a part of your everyday vocabu-lary. It's your worst fear. Still, you have no clue when it begins to happen to you. Instead, you make excuses. You send your daughter's birthday card to your son's address. Damn address book. At the gas station, you forget the gas hose is still attached to your car and drive off, tearing the hose in two. Even as gas is flying everywhere, the station attendant says it happens all the time. You believe him.

You admit that you certainly don't have a problem compared to Mack. He doesn't leave the house anymore.

You forget your wife's anniversary and this really bothers you because you remember buying her a bracelet. Y

A phone surveyor asks you to vote for [insert most recent candidate] for president. Sorry, you say, but you still think [insert most recent candidate] will get your vote.

Nine a.m. frustrates you more than any part of the day. You've been memorizing the same poem for 3 months now. You peek at the book -- just to get started: "Shall I compare thee to a summer's day?" You have no clue what comes next. It's that damn Old English, you say, it'll get you every time.

You find your wife's anniversary bracelet. It has an inscription: "Happy Anniversary, [insert year (3 years ago)] " You look at the calendar: [insert current year]. You look at the clock: 9:30. Time for Jeopardy.

Photographs now hold a special meaning for you. You wish you had taken more of them. Snapshots of your father’s hands. His smile. His jewelry. If you could actually take a picture of his laugh, you'd do that too.

Snapshots become a part of the daily schedule. They give you something that no one else can: instant memory. You look at them from 9:00 to 10:00 in the morning, during the hour you used to recite poetry. There was also some television show you used to watch, although you cannot recall its name. Whatever it was, it pales in comparison to the snapshots. Instant memory.

You feel as if the phone rings constantly. It always seems to be your son, Craig. He always asks the same question: "When are you going to come see your grandson?? Tyler needs to meet his grandfather. . . " What Craig fails to realize is that you have already tried to fly out to Seattle to see them once. You just couldn't find your way through the airport. Some places you can still navigate; you can find your way to church, to the park, to the store. Finding terminal B16 is a little beyond you at this point.

You will never go to Seattle; you'll never see Craig and Tyler; you'll never leave the neighborhood. At least you hope.

Three months later, you find that you are carrying a bag of groceries. Apparently, you have been to the store. It's autumn and the leaves are growing in technicolor. Yet, instead of looking at the vibrant autumn leaves, you are trying to find your way home. You find yourself walking on a baseball field. This isn't the way, but it does not occur to you. A man in his thirties in a Chicago Cubs baseball cap says,

MAN: Excuse me, sir. Are you lost??

NARRATOR: You are lost. You are desperately lost. "No."

MAN: Where do you live??

NARRATOR: I don't know.

MAN: Do you know your address?

NARRATOR: I don't know.

MAN: Is there someone I can call?

NARRATOR: You don't know. You just don't know. This man is firing questions at you like you are on . . . like you are on . . . like you're on Jeopardy.

MAN: Who are you?

NARRATOR: I don't know.

MAN: Where are you going?

NARRATOR: Home. I'm going home.

You're not dumb. You know you're in a nursing home. You know your son is talking to you.

CRAIG: See, this is your grandson, Tyler. Say 'hi' to your grandfather.

NARRATOR: You want to respond, to give your family some sort of acknowledgement, but words fail you again. What you feel and what you say are two different things. You want to say, "Hi, Tyler. I didn't used to be this way," but no words come out. You try to speak your thoughts through your eyes. You can't. Tyler is scared. He leaves.

You are left alone with Craig with nothing left to say. You look at him. He looks at you. He smiles and nods. He understands how much you care. You can close your eyes now. You are going home.
```

---

## IC-2429: Goliath

- Title: Goliath
- Author (byline): Simon Rich
- Work: Glory Days, Pg 167-187
- Publisher: Little, Brown and Company
- Publication date as stated: July 2024
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, NORMAL VOICE, ANNOUNCER’S VOICE, GOLIATH, REPORTER, DAVID, SHANA, JULES, SKEEBO, AUDIENCE, GOLAITH
- Teaser before the introduction: Yes
- Spoken words (computed): 1371
- Already set (do not supply): none

### Source block (context only)

```text
Author: Simon Rich
Book: Glory Days, Pg 167-187
ISBN: 978-0316569002
Publisher: Little, Brown and Company
Date (Month/Year): July 2024
SAWARD HISTORY
KS State Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
ANNOUNCER’S VOICE: Ladies and gentlemen . . . Children of all ages! Welcome to the Death Match!

NORMAL VOICE: We all know the story of David and Goliath. It’s the ultimate underdog tale. The scrappy kid. The giant bully. One sling, one stone, one perfectly placed shot . . . and boom! Sunday school legend . . . But what if that’s not exactly how it went down?
```

### Performance text (classify this)

```text
NARRATOR: (Pg 167-187) Goliath looked down at the familiar crowd of reporters. The reporters were vigorously wiping down their slates to make room for his sound bites. Goliath couldn't help but feel a tiny surge of pride. He'd been fighting people to the death for years, and somehow everybody was still interested.

ANNOUNCER’s VOICE: GOLIATH! Towering
warrior! Divorced dad of a 12-year-old who needs
private school. (beat) and . . .DAVID! Brave;
marketable; relatable! He’s got a fragrance line!

NORMAL VOICE: This is a story about fame, privilege, public opinion and what happens when history is written by whoever has the better manager.

ANNOUNCER’S VOICE: Because in this arena, the real weapon isn’t a stone!

NORMAL VOICE: (whispers) It’s publicity. (beat) Goliath by Simon Rich

GOLIATH: (calling on a reporter) You have question for Goliath?

REPORTER: What are your thoughts on fighting David?

GOLIATH: (unsure, scratching his beard) Who is David?

DAVID: (enters, floppy hair bouncing) Wow, this is so cool! A real-life press conference! So how does this even work? Do I call on people myself? Wow! Okay, I guess I'll start with ... Shana.

SHANA: The question we all want to know is, what makes you believe that a small, poor, unarmed child can defeat a well-known giant in a death match?

DAVID: I'm just grateful for the opportunity to fight at all. Growing up small, poor, and unarmed, I never imagined I'd ever get the chance to do anything noteworthy. It's all thanks to my mom. Being a single mother is no joke. If you ask me, she's the real underdog death fighter.

REPORTER: My question is about determination. Do you have it?

DAVID: (commanding the room) Great question. Yes.

GOLIATH: (baffled he’s not in the spotlight) That was two in a row for David. Usually, one question for Goliath, one for other death fighter, then Goliath speak again.

REPORTER: Okay, I've got one: How impressed are you by David?

GOLIATH: (confused) David is boy. Goliath is giant. We should not even be fighting.

SHANA: (solemnly, throwing a disapproving look at Goliath) David, how would you respond to Goliath’s hurtful statement?

DAVID: I ain't doing this for me. I'm doing it for all those kids in Bethlehem who get told every day of their lives, 'You'll never get to be a death fighter.' I'm fighting for Bethlehem, and D's always gonna rep the Beth, straight up. D's gonna be D. No fronting, no filter. Just some kid from the Beth, trying to shine. That's who I am. That's D.

GOLIATH: (saddened that no one was paying attention to him) Goliath hungry. Okay . . . Goliath go. ******

NARRATOR: Goliath ate a full-size pig (Goliath burps) It had been a long, strange day, but now he was at peace, sitting across from his 12-year-old daughter, Jules.

JULES: (in typical pre-teen giant fashion) Mom says you need to call the school. Something about tuition . . .

NARRATOR: Middle school so far had not been easy. The other kids made fun of her for the tiniest of things: her height, her width, the depth of her voice, the fullness of her unibrow, the crash of her steps, the unsettlingly audible sound of her eyeblinks. (Jules blinks awkwardly) Private school had seemed like the only option. [But] Goliath was in serious trouble. Gretchen had gotten almost everything in the divorce. His death fights paid decently, and there were some incentives built into his contract, like if he won in the first round. Even if he managed [to defeat] David, he still wouldn't be able to cover Jules's tuition. His only hope was to find an additional source of income. Luckily, he knew just where to start. ******

GOLIATH: (taking a seat in Skeebo’s office) Goliath never do endorsement before . . .

SKEEBO: Neither had David when he met me. Now the kid's hot! Signature sandal, signature tunic. They took a drop of sweat to make a fragrance and it sold out in a day. Kid's got a production company, D Street, started as a vanity label for his raps, now the Saudis want to invest. (beat) Let's get into it. I asked around town, put out a bunch of feelers with all kinds of brands. Unfortunately, there are no offers.

GOLIATH: (shaking his head in disbelief) Why not?

SKEEBO: The brands all want David. Do you realize he's gotten so popular that people are naming their kids after him? No joke. 'David' is becoming, like, a normal, common name.

GOLIATH: Why don't people like Goliath? Goliath has been winning for years.

SKEEBO: That's the problem. Audiences just don't find you appealing. They see David as way more authentic, root-able, and likable.

NARRATOR: Goliath growled in frustration. (Goliath growls) He understood why people sympathized with David. He was small and about to be murdered. But it's not like Goliath had it easy. If the public knew the pressure he was under, then surely their allegiances would change.

GOLIATH: Goliath will get endorsements. Goliath just need to show people real Goliath. ******* Shanna’s Talk Show*****

SHANA: My next guest is an undefeated death fighter who has represented Philistine for years. His next match will be against David, who represents everybody here as well as the one true God. Goliath, thanks for being with us . . . I understand there's something you would like to clear up.

GOLIATH: (clearing his throat, he has obviously prepared) People think Goliath have it easy. But really Goliath have things hard. (to audience earnestly) When Goliath was young, Goliath had to eat more food than other kids. Sometimes Goliath would have to sit at table 20 minutes longer than everybody else. So there is that. Also, it is not easy killing people. Sometimes, blood splashes onto Goliath's clothes and it is wet. And number three: it is hard for Goliath to buy pants. In conclusion: Goliath history's greatest victim.

AUDIENCE: Boo!

SHANA: Forgive me for being skeptical, because when I look at you, I don't see hardship. What I see, frankly, is a lot of privilege.

GOLAITH: (quick with a denial, he pleads to the audience) People think Goliath is rich, but Goliath is not rich. If you do not start worshipping Goliath, Goliath will not score cushy endorsement deals, and he will not even be able to send daughter to private school! He will have to send her to public school with poor people! People as poor as you!

AUDIENCE: (even louder and throwing sand) Boo!

NARRATOR: The truth was that other people decided who you were, and once they did you could never change their minds. **** The Day of the Death Match*****

(sound effects of trumpets blaring to announce the match)

GOLIATH: (flexing for the audience) Goliath have message for haters! Your beloved David is about to die! And not in a normal way! Think of craziest way you can think of! It will be crazier than that!

NARRATOR: Goliath rarely spoke before his fights, preferring to let his killing do the talking, but this time he'd screamed himself hoarse. And by the time he climbed into the ring, it was obvious his taunts had made an impact. David's normally buoyant blond bob lay flat on his head, matted down by sweat, and his bright blue eyes looked bloodshot.

DAVID: (calling to his manager) Yo Skeebo! Maybe we should postpone? (frantic breathing)

GOLIATH: (cracking his neck and stretching, he points at David) Goliath kill you soon!

DAVID: (fumbling for his slingshot, it wobbles in his hands as he slides in a pebble and feebly draws it back)

NARRATOR: The crowd fell silent; they knew this shot would be David's one chance.

GOLAITH: (in slow motion, watches as the stone drifts toward him)

NARRATOR: He thought about the trophies he had won, the belts he had hoisted. He thought about the way it felt to win a fight, the unmatchable clarity that could come only with victory, that sense, however fleeting, that you had been born for a reason. So far, his fights had all been easy. This one would be hard.

GOLIATH: (takes a deep breath as the pebble bounces harmlessly off his brow, then in an epic overacting flop . . . ) Ow! Goliath lose death fight! (he staggers to the ground)

NARRATOR: He knew it wasn't the kind of performance that would have passed muster in theater club, but the crowd seemed to buy it, screaming and crying in ecstasy.

DAVID: (celebrating his win) Yeah, bruh! All day!

NARRATOR: Goliath kept his eyes closed until the cheering faded into silence. When he finally opened them, Skeebo was smiling down at him, holding a sack of silver pieces. Their deal had been simple. In exchange for the dive, Goliath would receive an anonymous stake in D Street Productions going forward. As long as David's star continued to rise-and it assuredly would after this upset-Goliath could cover Jules's tuition indefinitely.

SKEEBO: (Holding payment out of reach as Goliath gleefully reaches for his payment) Hold up! You still gotta sign an NDA.

GOLIATH: What is NDA?

SKEEBO: (looks over his shoulder then whispers ominously) It means you can never tell anyone what happened here. Not the public, not the press, not David. Not even your own family!

NARRATOR: For the first time, Goliath pondered the full scope of what he had agreed to. This battle was the kind of thing people might remember. It was possible the public would even embellish his loss over the years, saying he'd died in the fight, or that David had cut off his head. Even Jules would grow up thinking he'd been beaten. His legacy of greatness would end, and instead, he would become a reference point for failure, an eternal symbol of humiliation. . .

GOLAITH: (contemplates for a moment, shrugs then signs with a flourish and grabs the cash; then to audience proudly, tapping his brow) Goliath have smarter idea.

(winks)
```

---

## IC-2430: Guess What? I Almost Kissed My Father Good Night

- Title: Guess What? I Almost Kissed My Father Good Night
- Author (byline): Robert Cormier
- Work: 8 Plus 1
- Publisher: Laurel Leaf
- Publication date as stated: March 1991
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2380
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Cormier
Book: 8 Plus 1
ISBN: 978-0440208389
Publisher: Laurel Leaf
Date (Month/Year): March 1991
```

### Introduction (context only: never use it for content warnings)

```text
OK . . . I’ll admit it . . . I never thought about my parents, especially my father, being “real” people. But the story I want to share with you made me stop and think. A lot. And I’ve come to the conclusion that people–all people–are fallible. Parents don’t have life completely figured out; sometimes they are winging it, just like their kids. And when I realized this, I realized I had to spend some quality time with my dad – as a “real” person.

Guess What? I Almost Kissed My Father Good Night by Robert Cormier
```

### Performance text (classify this)

```text
I’ve got to get to the bottom of it all somehow any maybe this is the best way. It’s about my father. I found out recently that my father is actually forty-five years old, and he has the kind of terrible job that fathers have -- an office manager for a computer equipment concern. He reads a couple of newspapers every day and never misses the seven o’clock news on television.

He’s five ten, weighs 160 pounds, has a tendency toward high blood pressure, likes his steak medium rare and has a habit of saying that “tonight, by God, I’m going to stay up and watch Johnny Carson,” but always gropes his way to bed after the eleven o’clock news, which he watches only to learn the next day’s weather forecast..

I’m Mike, almost sixteen and a sophomore in high school.

Now that you have gotten the basic details, I’ll tell you about that day last month. I was barrel[ing] through Bryant Park, a shortcut, the turf spring-soft and spongy under my feet and the weeping willows hazy with blossom. Suddenly I screeched to a halt, like Bugs Bunny in one of those crazy television cartoons. There he is: my father. Sitting on the park bench. Gazing out over a small pond. My father was deep in thought, like a statue in a museum. I looked at my watch. Two-thirty in the afternoon, for crying out loud. What was he doing there at this time of day? I was about to approach him but hesitated, held back for some reason—I don’t know why. Although he looked perfectly normal, I felt as though I had somehow caught him naked, had trespassed on forbidden territory. I drew back, studying him as if he were a sudden stranger. I saw the familiar thinning short hair, the white of his scalp showing through. The way the flesh in his neck has begun to pucker like turkey skin. Now, he sighed. I saw his shoulders heave, and the rest of his body shudder like the chain reaction of freight cars. He lifted his face to the sun, eyes closed. I tiptoed away.

At dinner that evening, I’m uncommunicative, thinking of all the science homework waiting in my room., I have this truly tremendous appetite and I eat too fast, like my mother says. But that evening I stopped eating altogether when my mother asked my father about his day at the office.

“Routine,” he said. I thought of the scene in the park. “Didn’t even have time for a coffee break,” he said, reaching for more potatoes.

I almost choked on the roast beef. He lied: my father actually lied. I sat there, terrified, caught in some kind of terrible no-man’s-land. It was as if the lie itself had thrust me into panic. I was bothered by his motive. I mean—why did he have to pretend that he wasn’t in the park that afternoon? And the first question came back to haunt me worse than before— what was he doing there, anyway, in the first place?

I found myself studying him across the table, scrutinizing him with the eyes of a stranger. But it didn’t work. He was simply my father. Looking exactly as he always did. He was his usual dull unruffled self, getting ready to take his evening nap prior to the television news. Stifling a yawn after desert. Forget it, I told myself. There’s a simple explanation for everything.

Let’s skip some time now until the night of the telephone call. Father never answers the phone. He lets it ring nine or ten or eleven times and merely keeps on reading the paper and watching television because he claims—and he’s right—that most of the phone calls are for me. Anyway, a few nights after that happening at the park, the phone rang about ten-thirty and I barreled out of my room because he and my mother get positively explosive about calls after nine o’clock on school nights.

When I lifted the receiver, I found that my father had already picked up the downstairs extension. There was a pause and then he said: “I’ve got it, Mike.”

“Yes, sir,” I said. And hung up.

I stood there in the upstairs hallway, not breathing. His voice was a murmur and even at that distance I detected some kind of intimacy. I returned to my room and I remembered that my mother was out for the evening, a meeting of the Ladies’ Auxiliary. Who had called him on the telephone at that hour of the night? And why had he answered the call in record time? Was it the same person he’d been waiting for in Bryant’s Park? Don’t be ridiculous, Mike, I told myself

Later, I went downstairs and my father was slumped in his chair, newspaper like a fragile tent covering his face. His snores capsized the tent and it slid to the floor. He needed a shave, his beard like small slivers of ice. His feet were fragile, something I had never noticed before; they were mackerel white, half in and half out of his slippers. He wasn’t mysterious: he was my father. And he snored with his mouth open.

Detective work -- detective work sent me investigating my father’s desk the next day. No one was at home. The desk was unlocked. I opened the drawers and checked some diary like type notebooks. Nothing but business stuff. Dull. But a bottom drawer revealed the kind of box that contains correspondence paper and envelopes. Inside, I found envelopes of different shapes and sizes and colors. Father’s Day cards he had saved through the years. I found one with a scrawled “Mikey” painstakingly written when I was four or five probably.

“Looking for something?” His shadow fell across the desk. I mumbled something, letting irritation show in my voice. I have found that you can fake adults out by muttering and grumbling as if you’re using some foreign language that they couldn’t possibly understand. And they feel intimidated or confused. Anyway, they decide not to challenge you or make an issue of it. That’s what happened at that moment. There I was snooping in my father’s desk and because I muttered unintelligibly when he interrupted me, he looked embarrassed while I stalked from the room as if I were the injured party.

[The next week, out of a deep sleep,] suddenly I awoke. My watch said one-twenty . . . in the morning. I went downstairs for a glass of orange juice. A light spilled from the den. He’s there: my father. Slumped in his chair. Like death. And I almost dropped dead myself. But his lips flutter and he produces an enormous snore. One arm dangles to the floor, limp as a draped towel. His fingers are almost touching a book that had evidently fallen from his hand. I pick it up. Poetry. A poet I never heard of. Kenneth Fearing. In the front of the book there’s an inscription. Delicate handwriting, faded lavender ink. “To Jimmy, I’ll never forget you. Muriel.” Jimmy? My father’s name is James and my mother and his friends call him Jim. But Jimmy? I notice a date at the bottom of the page, meticulously recorded in that same fragile handwriting—November 2, 1942—when he was young enough to be called Jimmy. By some girl whose name was Muriel, who gave him a book of poems. He stirs, grunting, clearing his throat, his hand like a big white spider searching the floor for the book. I replace the book on the floor and glide out of the room and back upstairs.

The following day, I [again] spotted my father. He was crossing the street, dodging traffic. I checked my watch: two-fifty-five. He paused in front of the Monument Public Library and disappeared inside. My father—visiting the library? He didn’t even have a library card, for crying out loud. As I stood here, I saw Laura Kincaid drive up in her new LeMans.

A quiet, dark green LeMans. Class. “If I had to describe Laura Kincaid in one word, it would have to be ‘class’” I’d heard my father say once. She is blond, her hair color of lemonade as it’s being poured on a hot day. I stood there, paralyzed.—trying to figure out why she was at this moment walking across the street, heading for the library, her hair a lemon halo in the sun, her nylons flashing as she hurried. Was she on her way to a rendezvous? Stop it, you nut, I told myself, even as I made my way to the side entrance.

And then I saw them. Together. My father wasn’t looking at the books or the shelves or the walls or the ceilings or the floor or anything. He was looking at her. Then, they laughed. It was like a silent movie. I mean—I saw their eyes light up and their lips moving but didn’t hear anything. My father shook his head, slowly, a smile lingering tenderly on his face. I His hand reached up and touched her shoulder. They laughed again. She indicated the books in her arms. He nodded, an eagerness in his manner. He didn’t look as if he had ever snored in his life or taken a nap after dinner.

Pressed against the metal bookshelf, I felt conspicuous, vulnerable, as if they would suddenly whirl and see me, and point accusing fingers. But nothing like that happened. She finally left, simply walked away, the books still in her arm. My father watched her go, his face in shadow, until she disappeared from view. I watched him for a minute or two as he stood there looking down, his eyes tracing the path of her departure as if she were still visible. I studied his face: was this my father? And then, this terrible numbness invaded my body, like a Novocain of the spirit, killing all my emotions.

At dinner, the food lay unappetizing on my plate. I had to fake my way through the meal, lifting the fork mechanically.

“Aren’t you feeling well, Mike?” my mother asked.

I leaped about five feet off my chair. I hadn’t realized how obvious I must have appeared: the human eating machine suddenly toying with his food— steak at that, which requires special concentration.

“I met Laura Kincaid at the library today,” I heard my father say.

“Was she able to get a copy of the play?” my mother asked.

“Two of them,” he said, munching. “I still think Streetcar Named Desire is pretty ambitious for you girls to put on.”

“The Woman’s Auxiliary knows no fear of Tennessee Williams,” my mother said in that exaggerated voice she uses when she’s kidding around.

“You know, that’s funny, Dad,” I heard myself saying. “I saw you in the library this afternoon and was wondering what you were doing there.”

“Oh? I didn’t see you, Mike.”

“He was supposed to pick up the play on my library card. But then Laura Kincaid came by…” That was my mother explaining it all, although I barely made out the words.

I won’t go into the rest of the scene and I won’t say that my appetite suddenly came back and that I devoured the steak. Because I didn’t. That was two days ago and I still feel funny about it all. Strange I mean. That first time in the park when he was sitting there. The telephone call. That book of poetry he reads late at night, “To Jimmy, I’ll never forget you. Muriel.” Laura Kincaid in the library. Not much evidence, really. Especially when I look at him and see how he’s my father all right.

Last night, I came downstairs after finishing my homework -- he had just turned off the television set. “We stood there in the half-darkness.

“Hey, Dad.” I didn’t plan to ask him. But it popped out. “I was looking through a book of yours the other day. Poetry by some guy named Fearing or Nearing or something.” I couldn’t see his face in the half dark. Keeping my voice light, I said: “Who’s this Muriel who gave you the book, anyway?”

His laugh was a playful bark. “Boy, that was a long time ago. Muriel Stanton.” He closed the kitchen window. “I asked her to go to the Senior Prom but she went with someone else. And so she gave me a gift—of friendship—at graduation. That’s a lousy swap, Mike. A book instead of a date with a girl you’re crazy about.” He smiled ruefully.

You see? Simple explanation for everything. And if I exposed myself as a madman, and asked him about the other stuff, the park and the telephone call, I knew there would be perfectly logical reasons. And yet. I remember that day in the library, when Laura Kincaid walked away from him. I said that I couldn’t see his face, not clearly anyway, but I could see a bit of his expression. And it looked familiar but I couldn’t pin it down.. All kind of crumpled up. Or was that my imagination?

“Mike. Everybody gets the blues now and then. Even fathers are people. Sometimes, I can’t sleep and get up and sit in the dark in the middle of the night. And it gets lonesome because you think of…”

“What do you think of, Dad?”

He yawned. “Oh, a lot of things.”

That’s all. And here I am sitting up in the middle of the night thinking of Muriel Stanton who wouldn’t go to the Senior Prom with my father. How he gets lonesome sometimes. And sits up in the night, reading poetry. I think of his anguished face at the library and the afternoon at Bryant Park, and all the mysteries of his life that show he’s a person. Human.

Earlier tonight, I saw him in his chair, reading the paper, and I said, “Goodnight, Dad,” and he looked up and smiled, but an absent kind of smile, as if he were thinking of something else, long ago and far away. . . and I felt like kissing him goodnight. But didn’t, of course. Who kisses his father at sixteen?
```

---

## IC-2431: Gym Class – Worst Game in the World

- Title: Gym Class – Worst Game in the World
- Author (byline): Paul Feig
- Work: Kick Me: Adventures in Adolescence, Pgs 121-139
- Publisher: Three Rivers Press
- Publication date as stated: Sept 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: FIEG, WENDELL, FEIG, NORMAN, STUDENT 1, STUDENT 2, STUDENT 3, KARL, RICK
- Teaser before the introduction: No
- Spoken words (computed): 2142
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Feig
Book: Kick Me: Adventures in Adolescence, Pgs 121-139
ISBN: 978-0609809433
Publisher: Three Rivers Press
Date (Month/Year): Sept 2002
```

### Introduction (context only: never use it for content warnings)

```text
Welcome to Middle School Gym Class! A time ripe with embarrassment! Admit it. You remember – Showering with a group of vicious peers -- Gym clothes that could stand on their own because no one EVER took them home to be washed. But nothing compared to Dodgeball . . . Bombardment . . . Killer . . . No matter what you call it, it is one of those games of childhood that you either loved or loathed. For the athletically superior, it was a chance to prove some semblance of macho superiority. For others, it was little more than an hour of getting mercilessly pummeled by flying rubber projectiles. Either way, it’s one of those experiences that you don’t soon forget. Let’s take a look back at this sadistic little part of physical education that left such a lasting impression on many of us.

Gym Class –Worst Game in the World from Kick Me: Adventures in Adolescence by Paul Feig
```

### Performance text (classify this)

```text
FIEG: (Pgs 121-139) There was one class that I never enjoyed, that I faced each day with stomach-twisting dread: gym class. I must admit that I didn't mind gym class as much when I was in grade school because, back then, it was literally just running around. We pretty much played easy games and never really worked up a sweat. And for that reason we were allowed to do it all in our school clothes.

When I got to junior high, however, I was confronted with something that I found quite disturbing -- gym clothes. You see, being told I had to wear gym clothes in PE class meant I had to change into them in front of my classmates. And this was not something that I wished to do. At all.

See, I was an only child, and so I never had to take my clothes off in front of anybody. Even my parents. Even when I took a bath, a thick layer of Mr. Bubble, my bath time guardian, made sure my in-tub nakedness would be hidden from any prying eyes. And then suddenly, thanks to a guy named Mr. Wendell, our new gym teacher, I was expected to show 100 percent of myself to a bunch of kids I had grown up with . . . who didn't like me. Where was Mr. Bubble when I needed him?

WENDELL: (sounding like a drill sergeant) All right, ladies. This is the locker room. You'll be changing over in this area, where the lockers are. And over here are the showers. Each of you will be required to shower after every class. No exceptions.

FEIG: I figured I must have died and gone to hell. That could be the only excuse for someone's telling me I was going to have to bathe in public. I take a shower every morning before I go to school. I shampoo and blow-dry my hair. I brush my teeth. I'm the cleanest seventh grader this school has ever seen. He can't possibly be talking to me. (to Mr. Wendell) Do we all have to shower?

NORMAN: Of course you do. What do you want to do? Stink all day?

WENDELL: All right, boys. Change into your gym clothes. We're gonna have a little fun on your first day.

FEIG: I guess I must have had an abnormal amount of hang-ups for a 12-year-old, because no sooner were the words “change into your gym clothes” out of Mr. Wendell's mouth than all my classmates just dropped their pants and changed. None of them really seemed to care that they were standing around in front of each other in their underwear. It was clear [that] I was going to have to put my modesty on hold and change in front of this group of alpha males. I let my mind remove itself to somewhere more pleasant as I took off my pants. And as soon as they were off, my face went white. I had forgotten about something. A few weeks earlier, my mother had gotten into a hobby called Cameo, which was the art of drawing designs and pictures on fabric with these special ink pens. And one of the first projects she undertook was to hijack a pair of my underwear and draw a big dark red butterfly right on the back. And that was the pair of briefs I had worn to school this day. I was frozen. Did anyone see it? My mind started to race, in full panic mode.

NORMAN: What is that?!

FEIG: The whole class was moving toward me, staring at the butterfly on the back of my underwear, all of them with stunned, incredulous looks on their faces.

NORMAN: Oh my God. It's a butterfly!

FEIG: All hell broke loose. Apparently, they'd never seen decorative underwear and the sight of it had turned them into the kids from Lord of the Flies.

WENDELL: (entering the locker room angrily) What the hell's going on in here?!

FEIG: I figured I was saved.

NORMAN: (pointing at Feig’s butt) Feig's got a butterfly on his underwear!

WENDELL: (raising an eyebrow) He does? Let's see it, Feig.

FEIG: So much for being saved. Mr. Wendell leaned over and took a good close look at my mother's handiwork.

WENDELL: A butterfly? That's lovely, Feig. Was it always there or did it use to be a cocoon? (laughing) All right, guys, all right, enough of this. Get dressed and get into the gym." (starting to exit, then turning back to Feig) Oh, and Feig? You can flutter out with the rest of them.

FEIG: Thanks, Mr. Wendell. You're really an inspiration to us all.

STUDENT 1: Hey, Feig, uh . . . nice butt-erfly

STUDENT 2: Does your dad have one on his underwear, too?

STUDENT 3: I bet that butterfly . . . uh . . . wishes that it . . . was . . . uh . . . that it didn't have to smell your butt all day.

FEIG: I was the last to finish changing, as I wondered if I could convince my parents to transfer me to an all-girls' school.

WENDELL: All right, everybody, being that this is the first official day of gym, I thought we'd do something a little different. The game I'm going to let you guys play is ... Killer.

FEIG: It was not going to be something good.

WENDELL: (pacing in front of the class) The object of the game is to be the last man left standing. Okay, in order to play Killer, you will be divided into two teams. Each team will take one side of the gym. Then, when I blow the whistle, you will throw the balls across the gym at the other team without crossing the center line. If you are hit by a ball, you're out. If you catch a ball, the person who threw the ball is out. Got it?

FEIG: Unfortunately, I did. And I realized that this was the last game in the world I wanted to play.

NORMAN: These balls are too big. (picking up a cantaloupe size rubber ball) When my brother and I play, we use tennis balls. They really hurt.

FEIG: Yes, I thought, that really does sound like more fun. Maybe if we're really good, one week Mr. Wendell will let us use golf balls and Chinese throwing stars.

WENDELL: (clapping his hands) All right, girls, grab a ball and choose a side.

NORMAN: Hey, Butterfly? You're dead!

FEIG: Oh great, I thought. I was about to be the star of my gym class's production of The Lottery. It was at this moment that I had to reflect on the question: "Ex-actly why do we have gym class in the first place?" Was it supposed to build morale? Self-esteem? To make us more confident about our bodies, our minds, and our abilities? That's what my father always told me, but if that was the case, then my school district was failing miserably. [One thing] was clear. Everyone in this gym wanted to see me dead. I guess putting a butterfly on your underpants was right up there with defiling the American flag.

Mr. Wendell walked out onto the floor, whistle in mouth. He took a deep breath . . . the whistle blew. And I descended into hell. BLAM! I suddenly realized that these "harmless" balls were actually lethal weapons, when thrown by my classmates. If competitive sports were supposed to inspire teamwork, then my butterfly underwear had apparently inspired this group of fun-loving lads into a lynch mob.

I knew one thing. I had to keep moving. Fast. (enacts the game as he speaks) The balls were coming in at a blinding rate. I ran back and forth with a sort of high-stepping circus-horse gait, arms and legs flailing wildly. Keep moving. Keep moving. That's all my brain could tell me to do. Life hadn't prepared me for this type of evasive action. BOOM! The next volley came in. I dodged the attack. A few of my "comrades" fell. They had been hit. Ha. I had survived the initial surge. Maybe I would be okay. BOOM! Another hit. BOOM!

BOOM! I felt like I was going to puke. BOOM!. Every time I looked around, I noticed that more and more of my teammates were gone, taken out by the Playground Balls of Death. And because of this, I was quickly on my way to becoming one of the last players left, an honor I definitely didn't want. Something had to be done.

Karl Scott was throwing the large ball at our team and then letting it rebound back to him. I figured that once that ball hit the bleachers, its velocity would be decreased, and I could then step in front of it and stop it from rebounding back across the gym. So, I ran in to get it. Karl Scott saw me coming.

KARL: You're dead, big-nose!

FEIG: He heaved the ball and I ducked at the last minute. BOOM! Great. This wasn't working. BOOM! He threw again. And again I ducked and let it go by. BOOM! Karl missed again. He was definitely getting frustrated now.

KARL: Give up . . . You know you're gonna get it.

FEIG: (with a false sense of bravado) From you, Karl? Not yet. Not without a fight. (to audience) Karl got a look of determination, wound up, and heaved the ball at me again, this time as hard as he could, delivering what he knew would be the Death Blow. The ball came straight toward my face. Suddenly, the world seemed to shift into slow motion. The ball was headed toward me, too fast to dodge, right on course to take my head off. I saw Karl Scott's face over the top of the ball. He had a real smug smile, happy to be the one to bring the Butterfly Boy down.

Then, suddenly, everything went back to normal speed. In a last futile act of self-preservation, I held my hands out in front of me and closed my eyes. I felt the ball break through my fingers, skid down my arms, and explode into my chest. Is this what it's like to be shot? I wondered. The force knocked me right off my feet. I slammed onto the ground, butt first, and hit my back against the wooden beams on the wall. A hot pain ran through my chest where the ball had hit. Everything was spinning from the shock.

Then, I heard something strange. Silence. Absolute silence. I looked down and saw that the ball he threw was still lodged between my arms and chest. I had caught it. Karl was out. Because of me, Karl was OUT. Oh my God, I thought, eyes wide. I did it! All right! They gotta respect me for this.

I immediately pictured a scene in the locker room with all of them coming up to me and giving me a "We're sorry we misjudged you, you're really an okay guy" speech and then singing "For He's a Jolly Good Fellow." Maybe they'd even all get butterflies cameoed on their underwear in a show of solidarity. Because, whether they wanted to admit it or not, I had just proven myself.

BOOM BOOM! I was thrown quickly back into reality when two balls slammed into the ground on either side of me. I was now the only one left on my team. Five of the enemy remained, their eyes trained on me. Definitely not the position I had been looking to get into. GET ME OUT OF HERE! They moved closer.

Well, here goes, I figured. I'm gonna get myself out. I threw the ball high in the air, right toward Rick Jones.

An easy catch, Rick. Just stick out your arms and you'll be the King of the Locker Room. Rick sidestepped out of the way, casually, right at the last moment. Then Rick looked at me and shook his head, scary calm on his face.

RICK: You ain't gettin' out that easy, Feig.

FEIG: Suddenly, I heard a whistle blow. It was Mr. Wendell. He was actually going to stop this. My persecution has ended! The man finally came through for me.

WENDELL: No borders, boys. The field is open. That means you don't have to stay on your side of the center line. So, c'mon, get in there and let's finish this game up.

FEIG: Oh, GREAT! The time had come. Life as I knew it was about to end. The five mouth-breathers surrounded me. I was dead. I looked over to the sidelines at my classmates, boys with whom I had grown up. I saw Mr. Wendell, the man put in charge of my physical development. I saw them all, the compassionless bunch. Would the sight of a trapped person, a cornered, defenseless animal, stir some sort of sympathy within them? There was nothing left to do. I officially hated these guys. I looked right at them.

(breathing heavily, nearly crying, high-pitched) "YEAH? WELL, F*** YOU ALL!

I stood there, panting, trying not to cry. I looked at the five assassins who surrounded me. Rick Jones reached out slowly . . . and lightly touched me on the arm with the ball he was holding.

RICK: (kindly) You're out, Feig.

FEIG: (gulping, chest heaving) . . . really? . . .

RICK: Uh-huh.

FEIG: (to audience) B-B-BLAM!!! The five surrounding balls exploded into my body. . . Everything went black. When I came to, Mr. Wendell told me I'd be in detention for a week. For swearing.
```

---

## IC-2432: Harris and Me

- Title: Harris and Me
- Author (byline): Gary Paulsen
- Work: Not specified
- Publisher: Yearling
- Publication date as stated: April 1995
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: HARRIS, NARRATOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1184
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gary Paulsen
ISBN: 978-0440409946
Publisher: Yearling
Date (Month/Year): April 1995
```

### Introduction (context only: never use it for content warnings)

```text
Have you ever been betrayed by someone? Usually it’s by people we don’t get along with, but sometimes we are bested by friends. In that situation, how do you retaliate? In this selection, Harris and Me by Gary Paulsen, the 11-year old narrator is madly in love with Harris’s cousin, Elaine. Harris, seeing that Elaine is going to take his best friend’s focus away from Harris during their summer, ruins the chances of the lovebirds getting together. So what is a friend to do? Why seek revenge, of course! Harris and Me by Gary Paulsen.
```

### Performance text (classify this)

```text
(Ch. 10 (Pg 127-134) - In which I discover love only to have my heart broken and in revenge I fry Harris’s business)

“I ain’t gonna do it.” Harris stood by the side of the barn, looking at the wire that came from an insulator near the door and led out into the pasture. The chickens hit it a few times, squawking and jumping with feathers flying, and even Buzzer, [the dog], accidently brushed the wire. When it popped him he took it as an attack and went after it, which of course made it worse and made him more angry so that he attacked harder, biting and clawing at the wire until finally he admitted defeat and walked away from the fence. Every hair on his body was straight out and I believe if anybody had crossed him right then he would have killed.

It was while Buzzer was fighting the wire that the idea came. We had tried touching it with the backs of our fingers and pieces of grass but the results were inconclusive. I had always been of a scientific nature, believed in the worth of experiments, and I wondered what would happen - watching Buzzer and the fence at war - if somebody actually peed on the wire. Specifically, I wondered what would happen if Harris peed on the wire.

I knew it would not be an easy experiment to conduct and set about doing it carefully. The subject would be reluctant - downright negative, as it turned out - and there would have to be some form of inducement so attractive that it would overcome the reluctance. As it happened I had the “dourty peectures.”

(dirty pictures) The power of these pictures to control and induce were beyond question. I believe if given enough of them Harris would have walked into a bonfire - indeed, I would have done the same thing. The quality of the pictures wasn’t great. They were black-and-white and small and grainy. But they worked. It was impossible to look at them and still breathe correctly. My dilemma was mostly one of quantity. I knew I could get the experiment to work, but with how much effort? How many pictures would it take?

I had, altogether, seven of them and since I was interested in them myself - purely from an artistic viewpoint, of course - I didn’t want to completely deplete the collection. I offered Harris one picture. It was not the best picture - the best picture I wouldn’t have released if Harris had bitten the wire and hung on with his mouth (something I considered suggesting when I remembered what he had done with the first love of my life) - but it was a good picture: accurate in detail, fundamentally sound as far as composition and educational benefits were concerned, and far reaching in its ability to promote advanced stages of hyperventilation.

HARRIS: “Nope. I ain’t gonna do it.” But his refusal was soft. I could sense the weakness in it and I countered. The picture I’d offered, plus one other, the one where it was possible to See It All.

HARRIS: “Well…”

NARRATOR: (to audience) I had him. (To Harris) “First the rules.”

HARRIS: “What rules?”

NARRATOR: “You have to pee right on the wire - not just pass over it - and you have to pee on it long enough to get the surge. Otherwise it’s not a deal.”

HARRIS: (studying the wire) “That thing put a sow on her knees…”

NARRATOR: (shaking his head) “She was off balance. Besides, two of the pictures for your very own - that’s a good swap.”

HARRIS: (thinking for a minute, then a heavy sigh) “All right. Go get the pictures.”

NARRATOR: (To Harris) “I’ve got them. (Showing him the pictures) So go ahead - pee on it.” (To audience) He unbuttoned his fly on his bibs and took his business out, then stood there, frowning. (To Harris) “What’s the matter?”

HARRIS: “It don’t work. Nothing’s coming out.”

NARRATOR: “Push a little.”

HARRIS: “I am. It’s scared. It don’t want to do it.”

NARRATOR: “If you don’t pee on the wire, the deal is off.”

HARRIS: “It’s like it knows what’s coming and don’t want to do it.”

NARRATOR: “Two pictures…”

HARRIS: “I’ll have to lie to it.”

NARRATOR: “Lie to what?”

HARRIS: “My business. I’ll just have to lie to it and start peeing over here, then swing around, make the dumb thing think everything is all right.”

NARRATOR: (to audience) He turned sideways, aimed away from the fence, and in a moment it started. (to Harris) “So turn. Before it’s done!”

HARRIS: “It ain’t that easy. Something in me won’t let it happen…”

NARRATOR: “Ahh heck, you’re going to run out.”

HARRIS: “No, I’m holding her back. Here, now…” He turned slowly until the stream of urine was only inches away from the wire, hung there for a second, then hit the wire.

HARRIS: “There, now are you hap -----” Later I would come to know a great deal about electrical things. I would understand that water is an excellent conductor of electrical energy but that urine, with its higher mineral content, is even better and what Harris did amounted to hooking a copper wire from his business to the electric fence. The results were immediate, and everything I would have hoped for from a standpoint of scientific observation, not to mention revenge.

In a massive reaction every muscle in Harris’s body convulsively contracted, jerking like a giant spring had tightened inside him. He went stiff as a poker, then soared up and over backward in a complete flip, arcing a stream that caught the afternoon sun so I swore I could see a rainbow in it. Nor did the spectacle end when he hit the ground. He landed on his side, both legs pumping, then sprung to his feet, running in tight circles holding himself and hissing:

HARRIS: “Oh-God-oh-God-oh-God-oh….” All in all it was well worth the investment and when he finally settled, leaning against the barn wall holding his business, panting loudly, I reached under my shirt to give him the two pictures. It was not to be, and the exact responsibility of who owed whom pictures would plague us the rest of the summer and perhaps does yet.

As I held the pictures toward Harris and he released his groin long enough to reach for them a shadow fell over us and I turned to see Louie, [the farmhand] standing there. He reached down with a crooked, filthy hand and took the pictures, held them up to the light, smiled toothlessly, and walked away toward the granary, putting the pictures in the top pocket of his bibs.

HARRIS: “Damn. You owe me two pictures.”

NARRATOR: “It wasn’t my fault. I held them out to you. Louie took them.”

HARRIS: “They wasn’t halfway. They wasn’t even close to halfway.”

NARRATOR: “They were over halfway.”

HARRIS: “You liar.”

NARRATOR: “I’m not lying. I handed the pictures over to you and you were reaching for them when Louie grabbed them. I did what I was supposed to do.”

HARRIS: “You did?! (grimacing in pain) I peed on the wire…” Later that night, lying in bed in the darkened room, I remembered him hitting the wire and started laughing.

HARRIS: “It ain’t funny. I’m all swoll up. It’s like my business was hit by lightning.”

NARRATOR: “It is too funny. You ran in little circles yelling . . . “Oh-God-oh-God-oh-God-oh….” Silence. Then…

HARRIS: “I think I saw him.”

NARRATOR: “Who?”

HARRIS: “Jesus, you dope. (pause) You still owe me two pictures.”

NARRATOR: “No, I don’t.”

HARRIS: “You do.”

NARRATOR: “Don’t.”

HARRIS: “Do.”
```

---

## IC-2433: Harry’s Story from 11/22/63

- Title: Harry’s Story from 11/22/63
- Author (byline): Stephen King
- Work: 11/22/63: A Novel
- Publisher: Gallery Books
- Publication date as stated: July 2012
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JAKE, HARRY, INTERCOM, AL, ELLEN
- Teaser before the introduction: Yes
- Spoken words (computed): 2249
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen King
Book: 11/22/63: A Novel
ISBN: 978-1451627299
Publisher: Gallery Books
Date (Month/Year): July 2012
```

### Introduction (context only: never use it for content warnings)

```text
Life-changing moments. Single acts that so profoundly affect your life, you know you’ll never be the same. Moments that have the power to transform lives and shape destinies. Jake Epping is moved by the raw honesty of Harry’s essay. But he never realized that Harry’s life-changing moment would become his too.

If you had a chance to go back in time and change history, would you do it? And what would happen if you did? Would you change . . .

Harry’s Story from11/22/1963 by Stephen King
```

### Performance text (classify this)

```text
JAKE: (Pg 18) I have never been what you’d call a crying man. My ex-wife, Christy, said that my “nonexistent emotional gradient” was the main reason she was leaving me. (Pg 19) I can only remember one time when I cried as an adult, and that was when I read the story of the janitor’s father. I was sitting along in the teachers’ room at Lisbon High School, working my way through a stack of themes that my Adult English class had written. The subject I’d assigned was “The Day That Changed My Life.” (Pg 20-21) There were no violins or warning bells when I pulled the janitor’s theme off the top of the stack, no sense that my little life was about to change. But we never know, do we? Life turns on a dime. I remember how his theme started. I remember it word for word. “It wasn’t a day but a night. The night that changed my life was the night my father murdirt my mother and two brothers and hurt me bad. He hurt my sister too, so bad she went into a comah. In three years she died without waking up. Her name was Ellen and I loved her very much.” It was when I got to the part about him crawling under the bed with blood running in his eyes that I began to cry. I had thought he was slower than the rest. Well, by God, there was a reason for that, wasn’t there? And a reason for the limp, too. It was a miracle he was alive at all. [Just] a nice man who would be a janitor for the rest of his life. Maybe once he could have been something different, but one night his life turned on a dime and now he was just a guy the kids called Hoptoad Harry because of the way he walked. So I cried and stroked a big red A+ on top of his paper.

JAKE: (Pg 24-25) Two years later, on the last day of the school year, Harry Dunning limped up to me after homeroom period and offered me his hand.

HARRY: I just want to thank you for everything

JAKE: You already did that, as I remember.

HARRY: Yeah, but this is my last day. I’m retiring. I’ll never forget that A-plus. I framed that, too. Got it right up beside my diploma.

JAKE: Good for you. (to audience) And it was. It was all good. His essay had been primitive art, but every bit as powerful and true as any painting by Grandma Moses. In spite of his grammatical lapses, Harry Dunning had written like a hero. On one occasion, at least. (Pg 26) The intercom on the wall cleared its throat.

INTERCOM: Mr. Epping, you have a phone call -- Al Templeton.

JAKE: (to audience) Al Templeton, owner of Al’s Diner. Curious as to why Al would call me. Ours had always been strictly a cook-and-client relationship. (goes to phone, punches in his extension)

AL: (Pg 27-28) Jake, I need to see you. It’s important.

JAKE: Can I ask—

AL: I expect you to ask plenty, and I’ll answer, but not over the phone.

JAKE: I promised I’d come down in an hour or so. And he hung up, without even a goodbye. Al’s Diner was housed in a silver trailer across the tracks from Main Street, in the shadow of the old Worumbo mill. I went up the steps, then paused. The sign WELCOME TO AL’S DINER, HOME OF THE FATBURGER! was gone. In its place was a square of cardboard CLOSED & WILL NOT REOPEN DUE TO ILLNESS. THANK YOU FOR YOUR BUSINESS OVER THE YEARS & GOD BLESS. What kind of serious illness came on in 24 hours? I left Al’s last night at 5:45 and he’d been fine. The door opened while I was reaching for the handle, and Al stood there looking at me, not smiling. Al was seriously ill. I could see that. (Pg 29) In the hours since I’d last seen him, Al Templeton appeared to have lost at least 30 pounds. Nobody loses 30 pounds in less than a day, nobody.

AL: How do you like the new me, Jake? I’ve got a lot to talk about and I think you’re the only one who might listen. (Pg 32) I want you to see something. It’ll be quicker that way. Only seeing isn’t the right word. I guess experiencing is a lot closer.”

JAKE: (Pg 33) He led me past the double grill, the sink, the FrostKing fridge and the freezer. He stopped in front of the dishwasher and pointed to the door at the far end of the kitchen.

AL: That’s it. Through that door. You need to find out for yourself.

JAKE: (Pg 34) I’d be lying if I said my heart didn’t kick into a higher gear when I turned the knob and pulled. But when Al reached past my shoulder and turned on the light, what I saw was—Well, a pantry. (to Al) How long is this going to take, Al?

AL: (Pg 36) I want you to give me your cell phone, your wallet, and all the money you have in your pockets, coins included. Please. Please, Jake. (Jake hands over the items) [And] It’ll take as long as you want, because it’ll only take two minutes. It always takes two minutes.

JAKE: (Pg 38) I did as he asked, feeling like the world’s biggest dope. One step . . . lowering my head to keep from scraping it on the aluminum ceiling . . . two steps . . . now actually crouching a little. A few more steps and I’d have to get on my knees. That I had no intention of doing, dying man’s request or not. (to Al) Al, this is stupid . . .

AL: (Pg 39-40) Go on. Nothing’s going to happen to you, buddy. Just go on.

JAKE: So I did. God help me, I did. And all at once there was a pop inside my head, exactly like the kind you hear when you’re in an airplane and the pressure changes suddenly. I was no longer in the pantry. I was no longer in Al’s Diner, either. I was outside but the diner was gone.

AL: (Pg 41) You can come back the same way you got there. Feel for the steps. Look around a little, then come back.

JAKE: It was Al’s voice, but very faint. (looking around incredulously) (Pg 48) On the left was a rack of newspapers. No New York Times, but there were copies of the Portland Press Herald and one leftover Boston Globe. The dates on both were Tuesday, September 9, 1958.

AL: (Pg 53) Relax Jake. You’re back. What do you think?

JAKE: How long was I gone?

AL: Two minutes. I told you, it’s always two minutes. And it’s always 11:58 A.M. September 9, 1958. Every trip is the first trip.

JAKE: You found this by accident?

AL: The first time, I actually fell down those stairs, like Alice into the rabbit-hole. I thought I’d gone insane. (begins violently coughing)

JAKE: (Pg 54) He can’t go on this way. He’s no more than a week from the hospital, and probably just days. And wasn’t that why he’d called me. Because he had to pass on this amazing secret to somebody before the cancer shut his lips forever.

AL: (Pg 65) You can go back, Jake. You can change history. Do you understand that? (Pg 83) John Kennedy can live. You can save him, Jake.

JAKE: And would that really make things better? There were no guarantees. I told him goodnight and left. [But] one more thought came before I dropped: (Pg 84) It wasnt a day but a night. The night that change my life was the night my father murdirt my mother and two brothers. . . . (Pg 85) I ran for my study. I don’t keep all student work, but I made it a habit of photocopying the best essays. I pulled open the bottom drawer and after 15 minutes, I found it . . . I never go see horra movies because on Halloween night in 1958 I lived thru one.

AL: (Pg 65) (Echoing) You can go back, Jake. You can change history. ******The Next Day at Al’s Diner *****

AL: (Pg 87) (reading Harry Dunning’s essay) Jesus! Son of a b*** killed his wife and three of his kids with a hammer?

JAKE: (Pg 89) It took Harry years to recover from that night. Could [his life] have been better? Yes. Can I make that happen? Based on yesterday, maybe I can. (Pg 90) If I can stop his old man from swinging that hammer. And the three other kids. Surely some of them will get married if they live to grow up. I want a better example of what happens when you change a watershed moment. I need that before I go monkeying with something as big as the Kennedy assassination. (Pg 116) Forty minutes later I was headed north to Derry behind the wheel of a 1954 Ford (Pg 165) In the weeks before Halloween, I came to believe that Derry wasn’t like other places. Derry wasn’t right. Something wrong, something bad. Certain empty houses that seemed to stare like the faces of people suffering from terrible mental illness. An empty playground with the roundy-round slowly spinning even though there were no kids to push it and no wind to turn it. It screamed on its hidden bearings. Something wrong, something bad. (Pg 167-168) I anticipated no problems when Halloween came. Dunning might come in his car rather than on foot, but I knew what it looked like. It would be after dark, according to Harry’s essay, but there were streetlights. Unless he was totally fixated on what he’d come to do, Dunning would almost certainly see me running at him. I had the pistol, but it was only dead accurate up to fifteen yards. I couldn’t wait until he actually got in the house because according to the essay, by the time Harry came out of the bathroom, all of them but Ellen were dead. I hadn’t traveled across more than half a century to save just one of them. (Pg 188) Ten minutes until the start of The New Adventures of Ellery Queen. How far along had Ellery Queen been when Dunning arrived? Harry’s theme hadn’t said, but I was guessing not long. (Pg 191-192) I heard a car moving far faster than any reasonable driver would have dared to travel on a street that was no doubt full of children wearing masks and carrying trick-or-treat bags. I knew who it was even before it screeched to a stop. Inside 379, Doris Dunning was sitting on the couch with Troy while Ellen pranced around in her Indian princess costume. Even if it kills me, I thought. Even then. Because this is now. This is them. The back door would be locked. I was so sure of this that I almost tumbled off the stoop when the knob turned and it swung outward. I stepped into a kitchen that still smelled of the pot roast Mrs. Dunning had cooked I heard her say “Frank? What are you doing here? What is that? Why have you. . . get out of here!” Then she screamed.

I ran through the arch and stopped there with my mouth open. Doris was on the living room rug. He had already broken her arm and dislocated her shoulder as well. He grabbed Ellen by her hair and heaved her. (shouting) DUNNING! STOP! (Pg 193) I pulled the trigger of the revolver. The bullet took him in the shoulder. He twisted sideways with the impact, then came on again.

HARRY: (as a child with his air rifle) Stop it, Daddy! Stop or I’ll shoot you!

JAKE: Arthur “Tugga” Dunning was crawling toward me, toward the kitchen. Dunning brought the sledge down on Tugga’s head. The boy’s face was obliterated. Bone fragments leaped high in the air. I fired again. (Pg 194) Dunning went down, feet in the living room, head in the archway between the living room and the kitchen. All of this happened in less than a minute; maybe only 30 seconds. Life turns on a dime, and when it does, it turns fast. (to Troy) Get out! Take your sister and get out!

JAKE: (Pg 196) I went into the bathroom, grabbed a towel, scrubbed my bloody face and stepped out into the kitchen. The boy who had brought me here was standing on the faded linoleum by the stove and watching me. Although it had probably been six years since he’d sucked his thumb, he was sucking it now. His eyes were wide and solemn, swimming with tears. Here was a boy who had just experienced something that would no doubt traumatize him, but he was also a boy who would never grow up to become Hoptoad Harry. Or to write a theme that would make me cry.

HARRY: Who are you, mister?

JAKE: Nobody. (to audience) He deserved more than that, though. The sirens were closer now, but I turned back. (to Harry) Your good angel. (to audience) Then I slipped out the back door and into Halloween night of 1958. *****

JAKE: (Pg 197) [When I returned to the diner] I thought of Harry, unhurt. And Ellen, who wasn’t deep in a coma from which she would never emerge. And Troy. And Doris. Her badly broken arm might hurt her for the rest of her life, but at least she was going to have a life.

(whispering) I did it, Al (to audience) But what had I done to 2011? (Pg 213-214) I dialed directory assistance. There was no listing for Doris, Troy, or Harold Dunning in Derry. As a last resort I tried Ellen. Halfway through the fourth ring, a woman answered.

JAKE: I knew your brother Harry a long time ago. I thought maybe I’d try to get in touch.

ELLEN: Well, I’m sorry to tell you this, but Harry’s dead. A long time ago. In Vietnam. During the Tet Offensive.

JAKE: Oh God, I’m so sorry. (to audience) I sat down, feeling sick to my stomach. I’d saved him from a limp and some mental fogginess only to cut his lifespan by forty years or so? Terrific. The surgery was a success, but the patient died.
```

---

## IC-2434: Homecoming King

- Title: Homecoming King
- Author (byline): Hasan Minhaj
- Work: Not specified
- Publisher: Scraps from the Loft.com
- Publication date as stated: (2017) Uploaded May 21, 2020
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: HASAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1629
- Already set (do not supply): none

### Source block (context only)

```text
Author: Hasan Minhaj
On-Line Transcript:
https://scrapsfromtheloft.com/comedy/hasan-minhaj-
homecoming-king-transcript/
ISBN: N/A
Publisher: Scraps from the Loft.com
Date (Month/Year): (2017) Uploaded May 21, 2020
```

### Introduction (context only: never use it for content warnings)

```text
Named to TIME's "100 Most Influential People in the World," Hasan Minhaj is a 1st generation American whose Muslim family immigrated her from India before he was born. And although he got his start as a stand-up comedian, he has come to be known for much more than his comedy. He draws on his personal history and the immigrant experience to explore America’s modern cultural and political landscape with depth and sincerity.

In fact, according to Lauren Feldman, associate professor at Rutgers’ School of Communication and Information, it is just this type of boundary-pushing “comedy [that] can play an important role in challenging people to address critical social issues.” *

I give you . . . Homecoming King by Hasan Minhaj
```

### Performance text (classify this)

```text
HASAN: My parents physically never saw each other. Years ago in a town in India, population 990,000 — that’s a small town — my dad heard a buzz in the streets about this woman named Seema, my mom. And, Seema was like the iPhone [insert latest iPhone model here]. “Have you heard of Seema? She’s slim. Her family owns a camera.” My dad was like, “A camera?” So, he runs to my grandfather’s house and lays it on the line. “I’m going to America. I want to marry Seema.” In ten minutes, the man married a woman he had never laid eyes on.

HASAN: So. my dad marries my mom, they come to the States, they have me, in Davis, California. But Davis was, like, super white. Roll call was a problem. It was a big deal for a lot of us. I would get, like, “Hanson Minaja . . . Sahan Minha . . . Saddam Hussein.” [beat] I’m not Saddam.

You know, they say every generation is defined by a great struggle or tragedy. So when 9-11 happened I was in high school. My dad sits everybody down. He’s like, “Hasan, whatever you do, do not tell people you’re Muslim or talk about politics.”

“Alright, Dad, I’ll just hide it. This [gestures to his skin color] just rubs off.”

We’re sitting there. Phone rings. I run, but my dad beats me to the phone. “Hello?”

I grab the second phone. I hear a voice. “Hey, you sand n*gger, where’s Osama?” He looks at me. “You can hear me, right? You dune coon. Where’s Osama? Hey, 2631 Regatta Lane, that’s where you live, right? I’m going to kill you.” Click.

And my dad’s looking at me. Do you ever see your parents, and you see the mortality in them? I’m looking at my dad and I see all five-seven of him. And that’s when I realize I’m a darapok. I’m a scaredy-cat.

We can speak two languages! I should have said something. I didn’t. We sit down. I hear “thud, thud, thud” outside. Me and Dad run outside and all the windows on the Camry, the immigrant car of choice, are smashed in. My backpack’s open. “They stole my stuff.” I’m mad. They know where we live, they’re timing this, so they’re watching us. I’m looking in the trees, the bushes . . . I look back, and my dad is in the middle of the road sweeping glass out of the road like he works at a barbershop.

“We’ve got customers. Log kya kahenge? We’ve got to clean this up.” Zen! Brown Mr Miyagi, just, like, not saying a word.

I’m like, “Why aren’t you saying something? I’m asking you, say something!”

He looks at me and goes, “Hasan. . . These things happen, and these things will continue to happen. That’s the price we pay for being here.”

We really are from two different generations. My dad’s from that generation where he feels like if you come to this country, you pay the American dream tax. You endure racism, and if it doesn’t cost you your life, pay it. There you go, Uncle Sam. But for me, I was born here. So I actually have the audacity of equality. I’m like, “I’m in Honors Gov. [takes out text book] I have it right here. Life, liberty, pursuit of happiness. All men created equal.” It says it right here, I’m equal. I’m equal. I don’t deserve this.

But as soon as I say that, he looks at me like I believe in Santa. “Hasan, you’ll never understand.”

“I’ll never understand? Dad, you’re the guy that will argue with the cashier at Costco when he doesn’t let you return used underwear. And now you want to be the bigger man? Now you’re like, ‘Let’s be reasonable with the bigots.’ What?” And then he just walks back into the house with glass in his feet. And I honestly don’t know who is more right. Maybe he’s right. Put your head down. Be a doctor, get a house in the burbs, let them call them whatever you want. But isn’t it our job to push the needle forward little by little? Isn’t that how all this stuff happens? I don’t know. The pendulum swings back and forth for me. And I know 9/11 is a super touchy subject. I understand. Because when it happened, everyone in America felt like their country was under attack. But on that night, September 12th, it was the first night of so many nights where my family’s loyalty to this country was under attack.

As immigrants we always have to put on these press releases to prove our patriotism. We’re auditioning. “We love this country, please believe me.” Nobody loves this country more than us.

I fell in love here. Six years old, Janice Malo. I saw her in the sandbox. I run up to her. First grade. “I love you!”

“You’re the color of poop.” That’s memory number one.

In the third grade, Miss Anderson said, “Write what you want to be.” Some kids were like, “an astronaut,” or “a firefighter.” I was like, “I want to be white.”

So, by my senior year of high school, I had yet to go to a school dance, I had been cut from the basketball team, and I had just got off this medicine called Accutane so my skin and face was peeling. I’m crushing life. Out here, killing it. But there was one bright spot, this girl named Bethany Reed. Her family had just moved from Nebraska to Davis, and we were in AP Calc together, but… we had chemistry.

One night she was like, “Hey, we always study at my house. Why don’t we study at your house?”

What, invite you over to my house? You walk in: “What language are you guys speaking? What’s that smell?”

I’m not going to open myself up to that. But I was like, “No, she’s different.”

“Mom, Dad, a school friend is coming over. Everyone, please be normal.”

My dad is like, “We are normal.” Killing me, you know what I mean? “Hasan, we’re normal. Be proud. You should be proud.”

We get there. We’re sitting at my living room table. My mom and dad are arguing in Hindi. My mom is frying pakoras. You’ve got to ease your way in. She’s from Nebraska. It’s all coming at this girl. It’s too much. So, I’m looking at her, like, “Don’t say anything. Please don’t say anything.” She looks up from her book, and she’s like, “You know what? This is really nice. We should do this more often.” And I look at her, and I’m like, “Oh, my God. I love you. You see me. I don’t got to change who I am? I can be me!”

She’s like, “Listen, you know, ever since my family moved from Nebraska, you’ve been my best friend. And you’re really special to me. This year wouldn’t be the same without you. So I was wondering, will you go to prom with me?”

The night of prom rolls around. I put on the JC Penney suit. Spray on the Michael Jordan cologne. Six puffs, one for each championship. You don’t want to overkill it with the MJ cologne. Don’t be tacky. I’m scaling down the side of my roof, scraping my knees. I jump off the roof. It’s like 20 feet. I jump off, I somehow land, I get on my bike. It’s beautiful, the sun is setting, it’s one of those gorgeous evenings. And I’m biking with my knees bowed out. So my slacks don’t get caught up in the chains. Fast enough to get there, but slow enough to not get pit stains. I’m balancing the corsage.

I get to her house. I park my bike. I’m walking up to the doorstep, and I’m about to ring the doorbell when I’m like, “Wait. 30 second time-out. Do you understand what’s about to go down? You’re about to go to prom with Bethany Reed. This is the American dream. This is what Dad fought for.” Ding-dong.

Mrs. Reed opens the door. She has this look of concern. And I look over her shoulder, and I see Jeff Burke putting a corsage on Bethany’s wrist. (long beat)

And she’s like, “Oh, my God, honey, did Bethany not tell you? Sweetie, we love you, we think you’re great. We love that you come over and study. But tonight is one of those nights . . . We have a lot of family back home in Nebraska and we’re going to be taking photos, so we don’t think you’d be a good fit. Do you need a ride home? Mr Reed can give you a ride home.”

And I was like, “No, I have my bike.” And I just biked home and played Mario Kart. That’s the nicest I’ve ever been dressed, playing Mario Kart. (long beat) The sad part is, I felt bad for being there. Who was I to ruin their picture-perfect celebration? You’ve seen movies. How many times do you see that on screen? And it’s not like they were yokels yelling “sand n*gger!” I could let that pass. I didn’t know that people could be bigoted even as they were smiling at you. It’s hard when you see people saying they love you but they’re afraid at the same time. And I didn’t know what that meant. (long beat)

Maybe we have a race problem. There is bigotry that happens every day because we’re too afraid of the Other. Someone who’s not in our tribe. I wish I could tell 18-year-old me, “Hey, man, don’t let this experience define you. It’s good people and bad people. Irrespective of creed, class, color, find those good people. Because love is bigger than fear.”
```

---

## IC-2435: How I Joined Mensa

- Title: How I Joined Mensa
- Author (byline): Steve Martin
- Work: Pure Drivel
- Publisher: Hyperion
- Publication date as stated: October 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 886
- Already set (do not supply): none

### Source block (context only)

```text
Author: Steve Martin
Book: Pure Drivel
ISBN: 978-0786885053
Publisher: Hyperion
Date (Month/Year): October 1999
```

### Introduction (context only: never use it for content warnings)

```text
I always thought Mensa was full of guys who are doomed to living at home and never date. Mensa parties would have, like, a few hundred super-geeky guys making unintelligible inside jokes, while three or four unattractive women walked around garnering worshipful attention. But no, those are Star Trek conventions. Mensa is, apparently, a place to meet people who get your jokes. The thing is, Mensa people think that the following joke is not only funny, but that nobody else gets it: What do you use to give a cat a pill? A caterpillar. Really. I get it. It’s just not very funny. But if you tell it and others laugh, and you’re at a party that claims only people with really high IQ’s are allowed . . . . . . then . . . . . Live long and Prosper. How I Joined Mensa by Steve Martin
```

### Performance text (classify this)

```text
I started with the phone book. Looking up "mensa" was not going to be easy, what with having to follow the strict alphabetizing rules that are so common nowadays. I prefer a softer, more fuzzy alphabetizing scheme, one that allows the mind to float free and "happen" upon the word. There is pride in that. The dictionary is a perfect example of over-alphabetization, with its harsh rules and every little words neatly in place. It almost makes me never want to eat again.

Joining Mensa means that you are a genius, and enables you to meet other members who will understand what the hell you are talking about when you say, for example, "That lamppost is tawdry." That's the kind of person they're after. Joining Mensa instills in one a courtly benevolence toward nonmembers, who would pretend to know what you know, think what you think, and stultify what you perambulate.

I worried about the arbitrary 132 cut-off point, until I met someone with an I.Q. of 131 and, honestly, he was a bit slow on the uptake.

I gave up on the phone book, which led me astray time and again with its complex passages, and then tried blind calling with no success. Next, 1-800-MENSA, which weirdly brought dead silence on the other end of the phone. A week later while volksvalking, I realized that "Mensa" didn't contain enough numerals to be a phone number, and knew it must be understood that any future member would be able to figure out the next two digits in the sequence. I tried dialing MENSANE, MENSAIL, MENSAFE, and MENSAAB, but got three rebuffs and a fax tone.

So it was neither rhyme nor reason that I stumbled into a party in my building when I inverted my floor number and got off at 21 instead of 12. Entering the party, I flipped back the Oushak rug and counted the knots per square inch. These people had money. I heard snippets of conversation: words like "feldspar" and "euonym" filled the air. In the corner, a lone piper played a dirge. Instantly, I knew where I was. This was a Mensa party.

That's when I saw Lola. She had hair the color of rust and a body the shape of a Doric column - the earlier ones, pre-invasion. She walked across the room carrying one of those rum drinks, slid herself onto the blue velveteen sofa, and endearingly poked herself in the face with her straw when she missed her mouth. If she truly was Mensa, she would have no problem with my introduction: "Please don't relegate me to a faraway lea," I ventured.

"I can see you've read Goethe, the Snooky Lanson translations," she countered. "Lozenge?"

I was putting her at around 140. Her look told me she was pegging me in the low 120s. My goal was to elevate her assessment and wangle a Mensa membership from out of her. Taking a hint from the soap operas, I talked to her with my back turned while staring out a window: "Wouldn't you rather parse than do anything?"

"Hail Xiaoping, the Chinese Goddess of Song," she rejoined. Lola then engaged in some verbal sparring that left me reeling. "This is quite an impressive apartment," she offered.

I saw a dictionary on its stand. O, how I longed to run to it and look up "impressive"! How I wanted to retort in Mensa-ese! But it was my turn, and I spoke: "I'm not sure if that's a compliment or an insult." I threw my head back, laughing, coughed out my lozenge, and watched it nestle into the Oushak. She asked me my name. "Call me Dor," I said. Later, I realized I'd meant Rod.

Lola and I sat and talked through the night. After the party, I held her and whispered, "I love that you're in Mensa." She whispered back, "I love that you're in Mensa, too." My temperature dropped to arctic. She told me her phone number, but, since it was all sevens, I couldn't remember it.

Most things one wants in life come when they are no longer needed. My membership was awarded exactly one year later, when I applied and became an honorary mensa "plaything." I sold my refrigerator and with the money went on a Mensa love-boat trip to Bermuda.

Embarking, I saw a woman standing aft, her back to me, slightly bent over a railing, looking very much the way a Doric column would look if it were bent over a railing. She turned and saw me, and I again saw my Lola. It was as though nothing had changed in a year, because we were both wearing the same things we wore on that night, still unwashed. She spoke: "Long time no see, Dor."

I corrected her, gaining the upper hand: "My name's not Dor."

"What is it?"

"It will come to me."

"Would you like to take a walk on the boatdeck?" she asked.

Boatdeck? Where is the damn dictionary when you need it.

She spoke: "I have only two years to live. Let's enjoy them while we slaver."

"Then slaver we shall, slaver we shall." I took her hand, and we turned eastward, toward the setting sun. "And, by the way, my name is Ord."
```

---

## IC-2436: i dreamed i was a baseball card

- Title: i dreamed i was a baseball card
- Author (byline): Richard Stockton Rand
- Work: Baseball Monologues edited by Lavonne Mueller (Pg 31-43)
- Publisher: Heinemann
- Publication date as stated: Aug 1996
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SPEAKER
- Teaser before the introduction: Yes
- Spoken words (computed): 1935
- Already set (do not supply): none

### Source block (context only)

```text
Author: Richard Stockton Rand
Book: Baseball Monologues edited by Lavonne Mueller
(Pg 31-43)
ISBN: 978-0435070212
Publisher: Heinemann
Date (Month/Year): Aug 1996
```

### Introduction (context only: never use it for content warnings)

```text
Who was your hero when you were 9 years old? When you were too little to be amazing, but your imagination could get you there anyway? Remember imagination . . . that’s what kids used before the internet! In your imagination, you could BE Mickey Mantle, or a sports announcer, or Bilbo Baggins from The Hobbit or even. . . invisible. Imagination was the ultimate escape. In this selection, we experience the world through the eyes of a young boy who is both idealistic and desperately trying to escape a situation he doesn’t quite understand. Can he save himself and his sister and hit one out of the park like Mickey Mantle, or is being invisible the only answer?

I Dreamed I was a Baseball Card by Richard Stockton Rand
```

### Performance text (classify this)

```text
SPEAKER: (Pg 31-43) I dreamed I was a baseball card. A baseball card. You pull out your stack. Start completely still. See him in your hand. Looking up at you. Flip. Heads. Flip. Heads. Heroes of the game. Flip. It’s in the fingers. Flip. Always the same. Forever. Mounds of baseball cards looking up at you. Take them home. Put ‘em in a shoebox. Hide ‘em under the bed - where I listened to them Yankees on my radio, cause my father didn’t trust baseball. I’d listen under the bed to night games at the Stadium. It was like being down in the Yankee dugout with the sound of a million people echoing in your ears. My sister could hear the crowd cheering clear out of my ear-plug, “The Mick just hit one out,” I’d say. That’s Mick -- The Mick. Mickey Mantle.

SPEAKER: The hush of the crowd, the voice of the Ole Redhead: “Full count on Mantle.” If you think hard enough you can make it happen. “He swings. It’s a fly to deep centerfield. It’s, IT’S, IT’S OUTTAhere! Mantle wins the game in the bottom of the ninth inning.” It works, too. That was me as Ole Red, The Redhead, Red Barber. I was honing my play by play skills – “Hard grounder to MacDouglas, over to Rizzuto who leaps over the sliding Stanky, back to first, double play!” -- for my future career as a Yankee broadcaster. This is after I got in the Hall of Fame for stealing the most bases, ‘cause I was fast, you bet, ‘specially when I was being chased.

And that’s how I found this hiding place. My dad was looking for me, and I’d slid under my sister’s bed. In winter, when I couldn’t get out, I needed a secret hiding space. That’s how I found under the bed. He was on his way to looking under there. He did look under there. But he didn’t see me. Know why?

Because I’m invisible. See, I seen this rip in the box spring and I could squeeze through perfect, like a secret passage. What a place! There were globs of cotton with springs sticking through ‘em and these boards I could lie down on perfect. And nobody found me. Never. Not ever. They looked, too. But I was invisible. Inside the boxspring I could sleep safe with my radio, and I’d dream I was a baseball card living inside the Hall of Fame. That’s how I saved myself.

Being invisible paid off in Little League too. I was #7, Mickey Mantle. Your number’s who you are. It was all in the number. Feel the Mick. Number 7 on my back. All through me, pinstripes, through my heart, and hurt.

The Mick’s always hurt. It’s in the knees. Can’t get out. I was The Mick. And nobody could pitch to me. To be a good pitcher you have to have good stuff and good control. And you got to be fast. When we were in trouble, I step to the mound. I was the short man. The Stopper. Got the ball in my hand. Turning. I look in to home. I knew what I had to do. Fastball. STEERIIIKE! Then I knew being little meant something.

I practiced pitching in my room ‘til my Mom’d say goodnight. Then, I’d sneak into my sister’s room, squeeze into the boxspring and turn invisible. My sister and I talked to each other through the mattress while they were fighting downstairs. I’d tell her how the game’s going like the Ole Redhead: “It’s back, back, back, back Ohhhhh-HO, Doctor! Mantle’s flagged it down by the monuments!” Then after the game, she’d read to me. And he’d leave us alone mostly, if we didn’t make no noise, ‘til one night.

. . . he comes in. Just stands there. Could feel him. Thought for sure he’d found me. But he’s watching her.

She pretends she’s asleep. It was a long time he stayed there. . . breathing. Could hear him . . . breathing. Feel his shadow. Then he sits . . . on the edge . . . of her bed, the mattress sagging damn near on top of me.

Then, every night he comes up, sits down: same time, Mom’s watching Johnny Carson, and he stares at her pretending she’s asleep. Then it starts. He’s moving the covers, whispering to her. She’s making sounds like trying to not make sounds. I hear laughing on TV downstairs, springs moving next to me. And the noises. I can’t . . . move. The mattress’s pressing down on me and they’re right there. So I turn invisible. Turn up the sound ‘til there’s only Yankee Stadium and the crowd screaming in my ear. Then it’s over. The mattress stops. Hear his shoes on the floor and he’s down the stairs humming like nothing happened. Mom never says nothing. Just sits watching Johnny Carson. Nobody says nothing. Every night it happens. ‘Til once, he’s coming up, she says, “What should I do?” “Hide,” I tell her. “Where?” she says. “Invisible.” “How?” “Little. Little. Like a dot!,” I tell her. But she couldn’t do it.

Footsteps on the stairs, humming like nothing’s going to happen. Then he’s there. Big heavy shoes. Staring. Sits. On the edge of her bed. Every night. Then it starts. I don’t want to be there, but I couldn’t leave her.

Then she thought of a way. It was getting cold, so she’d stay up all night putting her head out the window. And it worked. She got real sick. And she kept doing it ‘til the doctor quarantined her. Now nobody could touch her.

Pretty good thing. We rigged up two cans and a string through the bedroom windows and we planned our escape the whole time. I’d bring her meals up with secret notes under the grapefruit, and she’d roll her pills under the door for me to get rid of. Meals went in and plates came out for months she stayed sick. She was playing her cards right. Five months without going to school. She learned how to be invisible without even knowing it and now nobody could touch her. She stayed in there studying and got hundreds on all her exams!

But she started feeling better in the spring, and we knew we had to make a getaway plan. We got the idea from this book, The Hobbit, she read for English about these two guys that went off to find another world after where they lived stopped being safe. And boy, that sounded right for us. See, this Bilbo Baggins was the lead guy, and he lived in a place underground, like a . . . dugout. And he was a little guy, like a leprechaun, but baggy. And she reads to me all night about his adventures and we plan our escape.

We decide to write a letter to Mickey and we tell him everything. Then instead of going to school, I take her on the train up to Yankee Stadium. We sit in the bleachers and wait for The Mick to come out and take flies. We got the letter all ready for me to run out on the field. But he don’t come out. My sister and me went back home, but she got real sick from not having been outside all winter. They put her in the hospital the next day with a high fever. Seventh floor. Mickey’s number. She got so bad they had to put her in intensive care. They said she was gonna die.

Summer went into fall. The Yankees came in last place for the first time ever. One day, [Dad] took me to visit her cause she was having trouble remembering things. When I walked in she smiled right off, but no matter what she couldn’t recognize him. Over the next few months she had five operations. The doctors couldn’t understand why she kept rejecting her medication. It’s cause she wasn’t taking it! She went into a coma for days and she would call out in the night, “Ohhhhhh-Ho Doctor! Going Back, Back, Back, Going, Going . . . “ And I prayed to the leprechauns. Then one day she woke up. She told me ‘bout a dream. She was in great danger. The leprechauns came and took her on a train to heaven. She steps out into a bunch of clouds and this baseball’s heading right at her, and it’s a Mickey homerun. She reaches out to grab it and it’s me, my head, inside the baseball, saying “Don’t give up.” She was on and off for months, but she kept coming back.

My mother took me to visit her in the spring. It was a real warm day and the nurse said I could take her outside, so I rode her round the bases at the park across the street. I did the play by play and had her steal home with the bases loaded. Said it was the happiest day of her life. When we got back, the doctor asked her if she wanted to go home and she told him what happened . . . on the bed. He must have told my mother cause we went home and packed up her stuff quick while Dad’s at work. Then she flew away . . . with the leprechauns.

It was just me then. Waiting for him. To find out. I hear the garage. Then he comes up, asks how she is. It’s quiet. Something’s going to happen. I’m waiting . . . . She must be telling him. He starts moving . . . fast! Doors slamming! Then. Plates. Hitting the walls. I feel ‘em shake. ‘Til there’s no more plates. Then he’s up the stairs, in her room. Pulling drawers out, sees her clothes gone, slams her door, over and over. Doors slamming, over and over. Then he’s down, down to get her. “Don’t touch me!” [Mom] says. “I know what happened . . . up there. That stops him. Then nothing. Nothing. He just sits in the kitchen eating oatmeal and reading the paper.

But I can feel him down there getting mad, see him through the floor like a bomb moving. Then the doors start . . . . banging. Over and over. All night. But I’m ready for him, holding the bat, case he comes in. Practice my swing in the dark. SWING. See his face moving. SWING. The words coming out of his moth. SWING. The sound of the swoosh. SWING. And his head flies out of the ballpark . . .

I go to school to get somewhere safe. Stay late at the library, then ride the trains back and forth doing my homework or listening to the Yankess. “He’s going back, back, back . . .” Back home when he’s asleep and leave before he gets up. But one morning, he’s up the stairs in my room with a bat, standing over me screaming, and I don’t know what I did, but it’s bad. And I can’t move, can’t get the words out. And I’m waiting for it, waiting for him to finally hit me. Then I see the Mickey Mantle bat in his hands and I just want him to swing, just want him to hit me out like Mickey would at Yankee Stadium, so I could feel my head fly out of the ballpark, and not have to think anymore when he’s finally going to kill me. I say, ”Hit me.” But he don’t understand. “Hit me!,” I said. And he stops cause the voice is coming out of me loud, screaming, like his voice, and he’s scared. And it’s like I was him now, like he was me, little, little like me. And he can’t touch me. Nobody can touch me. Never. Not ever. Cause I ain’t invisible.
```

---

## IC-2437: I Like Guys

- Title: I Like Guys
- Author (byline): David Sedaris
- Work: Naked
- Publisher: Back Bay Books
- Publication date as stated: June 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2083
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Sedaris
Book: Naked
ISBN: 978-0316777735
Publisher: Back Bay Books
Date (Month/Year): June 1998
```

### Introduction (context only: never use it for content warnings)

```text
The topic of homosexuality has become a constant issue throughout our society. Many people believe that being gay is not acceptable for both religious and moral reasons. Growing up, David Sedaris struggled to find the common ground between being gay as well as being a normal teenager. He often resorted to the conclusion that you could not be both.

For David Sedaris, growing up in the late 60s and early 70s was not the typical fun and excitement as it was for other teenagers his age. Sedaris battled a secret that was looked down upon by all of society as well as the world around him. A secret that left him feeling shameful about his everyday life and constantly wishing he could do something, anything, to change it. I Like Guys by David Sedaris
```

### Performance text (classify this)

```text
Shortly before I graduated from eighth grade, it was announced that, come fall, our county school system would adopt a policy of racial integration by way of forced busing. My Spanish teacher broke the news in a way she hoped might lead us to a greater understanding of her beauty and generosity.

"I remember the time I was at the state fair, standing in line for a Sno-Kone," she said, fingering the kiss curls that framed her squat, compact face. "And a little colored girl ran up and tugged at my skirt, asking if she could touch my hair. 'Just once,' she said. 'Just one time for good luck.'

"Now, I don't know about the rest of you, but my hair means a lot to me." The members of my class nodded to signify that their hair meant a lot to them as well. They inched forward in their seats, eager to know where this story might be going. Perhaps the little Negro girl was holding a concealed razor blade. Maybe she was one of the troublemakers out for a fresh white scalp.

I sat marveling at their naïveté. Like all her previous anecdotes, this woman's story was headed straight up her *butt*.

"I checked to make sure she didn't have any candy on her hands, and then I bent down and let this little colored girl touch my hair." The teacher's eyes assumed the dewy, faraway look she reserved for such Hallmark moments. "Then this little fudge-colored girl put her hand on my cheek and said, 'Oh,' she said, 'I wish I could be white and pretty like you.'" She paused, positioning herself on the edge of the desk as though she were posing for a portrait the federal government might use on a stamp commemorating gallantry. "The thing to remember," she said, "is that more than anything in this world, those colored people wish they were white."

I wasn't buying it. This was the same teacher who when announcing her pregnancy said, "I just pray that my firstborn is a boy. I'll have a boy and then maybe later I'll have a girl, because when you do it the other way round, there's a good chance the boy will turn out to be funny."

" 'Funny,' as in having no arms and legs?" I asked.

"That," the teacher said, "is far from funny. That is tragic, and you, sir, should have your lips sewn shut for saying such a cruel and ugly thing. When I say 'funny,' I mean funny as in…" She relaxed her wrist, allowing her hand to dangle and flop. "I mean 'funny' as in that kind of funny." She minced across the room, but it failed to illustrate her point, as this was more or less her natural walk, a series of gamboling little steps, her back held straight, giving the impression she was balancing something of value atop her empty head. My seventh-period math teacher did a much better version. Snatching a purse off the back of a student's chair, he would prance about the room, batting his eyes and blowing kisses at the boys seated in the front row. "So fairy nice to meet you," he'd say.

Fearful of drawing any attention to myself, I hooted and squawked along with the rest of the class, all the while thinking, That's me he's talking about. If I was going to make fun of people, I had to expect a little something in return, that seemed only fair. Still, though, it bothered me that they'd found such an easy way to get a laugh. As entertainers, these teachers were nothing, zero. They could barely impersonate themselves. "Look at you!" my second-period gym teacher would shout, his sneakers squealing against the basketball court. "You're a group of ladies, a pack of tap-dancing queers."

The other boys shrugged their shoulders or smiled down at their shoes. They reacted as if they had been called Buddhists or vampires; sure, it was an insult, but no one would ever mistake them for the real thing. Had they ever chanted in the privacy of their backyard temple or slept in a coffin, they would have felt the sting of recognition and shared my fear of discovery.

I had never done anything with another guy and literally prayed that I never would. As much as I fantasized about it, I understood that there could be nothing worse than making it official. You'd seen them on television from time to time, the homosexuals, maybe on one of the afternoon talk shows. No one ever came out and called them a queer, but you could just tell by their voices as they flattered the host and proclaimed great respect for their fellow guests. These were the celebrities never asked about their home life, the comedians running scarves beneath their toupees or framing their puffy faces with their open palms in an effort to eliminate the circles beneath their eyes. Regardless of their natty attire, these men appeared sweaty and desperate, willing to play the fool in exchange for the studio applause they seemed to mistake for love and acceptance. I saw something of myself in their mock weary delivery, in the way they crossed their legs and laughed at their own jokes. I pictured their homes: the finicky placement of their throw rugs and sectional sofas, the magazines carefully fanned just so upon the coffee tables with no wives or children to disturb their order.

It was my hope to win a contest, cash in the prizes, and use the money to visit a psychiatrist who might cure me of having homosexual thoughts. Electroshock, brain surgery, hypnotism — I was willing to try anything. Under a doctor's supervision, I would buckle down and really change, I swore I would.

My parents knew a couple whose son had killed a Presbyterian minister while driving drunk. They had friends whose eldest daughter had sprinkled a Bundt cake with Comet, and knew of a child who, high on spray paint, had set fire to the family's cocker spaniel. Yet, they spoke of no one whose son was a homosexual. The odds struck me as bizarre, but the message was the same: this was clearly the worst thing that could happen to a person. The day-to-day anxiety was bad enough without my instructors taking their feeble little potshots. If my math teacher were able to subtract the alcohol from his diet, he'd still be on the football field where he belonged; and my Spanish teacher's credentials were based on nothing more than a long weekend in Tijuana, as far as I could tell. I quit taking their tests and completing their homework assignments, accepting Fs rather than delivering the grades I thought might promote their reputations as good teachers. It was a strategy that hurt only me, but I thought it cunning. We each had our self-defeating schemes, all the boys I had come to identify as homosexuals. We had long ago identified one another and understood that because of everything we had in common, we could never be friends. To socialize would have drawn too much attention to ourselves. We were members of a secret society founded on self-loathing. When a teacher or classmate made fun of a real homosexual, I made certain my laugh was louder than anyone else's. When a club member's clothing was thrown into the locker-room toilet, I was always the first to cheer.

At the end of the school year, my sister Lisa and I were excused from our volunteer jobs and sent to Greece to attend a month-long summer camp advertised as "the Crown Jewel of the Ionian Sea." I saw Europe as an opportunity to re-invent myself. I told myself that I would find a girlfriend in Greece. She would be a French tourist wandering the beach with a loaf of bread beneath her arm. Lisette would prove that I wasn't a homosexual, but a man with refined tastes. I saw us holding hands against the silhouette of the Acropolis, the girl begging me to take her accordion as a memento of our love. "Silly you," I would say, brushing the tears from her eyes, "just give me the beret, that will be enough to hold you in my heart until the end of time."

[But] camp was basically an extension of junior high school except that here everyone had an excess of moles or a single eyebrow. . . There was one boy at camp I felt I might get along with, a Detroit native named Jason who slept on the bunk beneath mine. Jason tended to look away when talking to the other boys, shifting his eyes as though he were studying the weather conditions. Like me, he used his free time to curl into a fetal position, staring at the bedside calendar upon which he'd x-ed out all the days he had endured so far. We were finishing our 7:15 to 7:45 wash-and-rinse segment one morning when our dormitory counselor arrived for inspection shouting, "What are you, a bunch of goddamned faggots who can't make your beds?"

I giggled out loud at his stupidity. If anyone knew how to make a bed, it was a faggot. It was the others he needed to worry about. I saw Jason laughing, too, and soon we took to mocking this counselor, referring to each other first as "faggots" and then as "stinking faggots." We were "lazy faggots" and "sunburned faggots" before we eventually became "faggoty faggots." We couldn't protest the word, as that would have meant acknowledging the truth of it. The most we could do was embrace it as a joke. Embodying the term in all its clichéd glory, we minced and pranced about the room for each other's entertainment when the others weren't looking. I found myself easily outperforming my teachers, who had failed to capture the proper spirit of loopy bravado inherent in the role. Faggot, as a word, was always delivered in a harsh, unforgiving tone befitting those weak or stupid enough to act upon their impulses. We used it as a joke, an accusation, and finally as a dare.

Nothing could match the cruelty and humiliation Jason and I soon practiced upon each other. He started a rumor that I had stolen an athletic supporter from another camper and secretly wore it over my mouth like a surgical mask. I retaliated, claiming he had expressed a desire to become a dancer. "That's nothing," he said to the assembled crowd, "take a look at what I found on David's bed!" He reached into the pocket of his tennis shorts and withdrew a sheet of notebook paper upon which were written the words I LIKE GUYS. Presented as an indictment, the document was both pathetic and comic. Would I supposedly have written the note to remind myself of that fact, lest I forget? Had I intended to wear it taped to my back, advertising my preference the next time our rented buses carried us off to yet another swinging sexual playground?

I LIKE GUYS. He held the paper above his head, turning a slow circle so that everyone might get a chance to see. I supposed he had originally intended to plant the paper on my bunk for one of the counselors to find. Presenting it himself had foiled the note's intended effect. Rather than beating me with sticks and heavy shoes, the other boys simply groaned and looked away, wondering why he'd picked the thing up and carried it around in his pants pocket. He might as well have hoisted a glistening turd, shouting, "Look what he did!" Touching such a foul document made him suspect and guilty by association. In attempting to discredit each other, we wound up alienating ourselves even further. Camp ended and I flew home. I like guys. The words had settled themselves into my features. I was a professional now, and it showed.

I returned to my volunteer job at the mental hospital, carrying harsh Greek cigarettes as an incentive to some of the more difficult patients.

"Faggot!" a woman shouted, stooping to protect her collection of pinecones. "Get your faggoty hands away from my radio transmitters."

"Don't mind Mary Elizabeth," the orderly said. "She's crazy."

Maybe not, I thought, holding a pinecone up against my ear. She's gotten the faggot part right, so maybe she was onto something.
```

---

## IC-2438: I Love Girl

- Title: I Love Girl
- Author (byline): Simon Rich
- Work: The Last Girlfriend on Earth
- Publisher: Back Bay Books
- Publication date as stated: Jan 2014
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2100
- Already set (do not supply): none

### Source block (context only)

```text
Author: Simon Rich
Book: The Last Girlfriend on Earth
ISBN: 978-0316219389
Publisher: Back Bay Books
Date (Month/Year): Jan 2014
```

### Introduction (context only: never use it for content warnings)

```text
(INTRO should be spoken very expansively, perhaps with a British accent) Greetings, my eloquent and verbose audience of (insert
```

### Performance text (classify this)

```text
number of audience members). Our vocabulary has become quite extensive over the years, with beautiful words like dalliance and evocative. Once upon a time, we were much less eloquent . . . Lord Byron’s

“She walks in beauty, like the night

Of cloudless climes and starry skies,

And all that’s best of dark and bright

Meets in her aspect and her eyes.” was once simply . . . . I Love Girl by Simon Rich.

Demeanor, body position, vocal qualities transform into the caricature of the early caveman.

I am Oog. I love Girl. Girl loves Boog. It is bad situation.

Boog and I are very different people. For example, we have different jobs. My job is Rock Thrower. There are many rocks all over the place and people are always tripping on them. So when I became a man, at age eleven, the Old Person said to me, “Get rid of all the rocks.” Since that day, ten years ago, whenever it is light outside, I am gathering rocks and throwing them off the cliff.

Boog’s job is Artist. When he became a man, the Old Person said to him, “Cut down the trees so we have space to live.” But Boog did not want to do this, so now he smears paint inside caves. He calls his smears “pictures.” Everybody likes to look at them. But the person who likes to look at them most is Girl.

I love Girl. There are many women in the world. By last count, seven. But she is the only one I ever loved. Girl lives on Black Mountain. It is called Black Mountain because (1) it is mountain and (2) it is covered in black rocks. Every day, Girl has to climb over the rocks to get to the river. It is too hard. So one day I decided, “I will clear a path from Girl’s cave to the river.”

I have been working on Girl’s path for many years, picking up the black rocks and carrying them away. I never throw her rocks off the cliff like normal rocks. Instead, I put them in a pile next to my cave. I like to look at the pile, because it reminds me of how I am helping Girl.

I am afraid to talk to Girl. If she found out it was me clearing all the rocks, I’m sure she would say something to me like “Hello” or “Hi there.” And then I would be in trouble. I am not so good at making words.

Boog is very good at making words. For example, last week he showed off his new picture at the Main Cave. Everyone was expecting it to be a horse or a bear (all his pictures so far have been horses, bears, or a mix of horses and bears). But this picture was not of any animal. It was just a bunch of red streaks. People were angry.

“I wanted animals,” the Old Person said. “Where are the animals?” It was bad situation. I thought that Boog would lose his job or maybe be killed by stones. But then Boog stood on a rock and spoke.

“My art is smart,” he said. “And anyone who does not get it is stupid.”

Everyone was quiet. We looked at the Old Person to see what he would say. The Old Person squinted at the red streaks for a while. Then he rubbed his chin and said, “Oh, yes, now I get it. It is smart. People who do not get it are stupid.” A few seconds later, everyone else got it.

The only person who did not get it was me. My beard began to sweat. I was scared that someone would ask me to make words about the picture. I headed slowly for the exit. I was almost out of the cave when Boog pointed his finger at me. “Do you like it, Oog?” Everyone stopped making words and looked at me. “Why don’t you explain it to us?”

I felt a burning on my skin. It was sort of like when you fall into a cooking fire and your body catches on fire. I looked at my feet and people started laughing. I looked up at Girl to see if she was one of the ones laughing. She was not (thank Gods). But she could hear all the other people laughing and that was just as bad.

The next day, I decided to become an Artist. “I am going to make a picture,” I told the others. “A good one.”

“Who are you going to show it to?” Moog said. “Your mother?” Everyone laughed.

“No,” I said. “I will show it to Girl.” No one made words after that.

I have never spoken to Girl, but one time she spoke to me. It was a long time ago, when we were still children.

It was the first day of school and we were learning to count. It was confusing. I am very good at some numbers. I understand “one” and “two” very well and I am O.K. with “three.” But when it gets to higher math, like “four” or “five,” I have trouble.

The Old Person had told us each to make a pile of five rocks. I did not know how many that was and it was getting to be my turn. It was bad situation. “Don’t worry,” she said. “I will help you.” The Old Person was about to look at my pile when Girl stood up and pointed into the forest. “Predator!” she yelled.

By the time we came back from the Hiding Cave, it was night. I wanted to thank Girl, but I did not know which words to make. So I said nothing.

Girl has a small head, so it is very strange how she fits so many things inside of it. She knows all the numbers: “six,” “eight”—you name it. But she also knows other things nobody else knows.

One time, I followed her down to the river. She was hunting fish in the normal way, by jabbing a stick in the water. After a long time, she caught a small flat fish. I assumed she would do the normal thing (rip off the head and eat the body), but instead she did the strangest thing I have ever seen. She put the stick— with the small fish still on it—back into the river. A short time later, she pulled the stick out. A bigger fish was on the stick. I do not understand how Girl did this.

But I have thought a lot about what I saw, and I have developed a theory: she is a witch who knows magic. Even though she is probably a witch, I still love her. My mother says that when you love someone you love them despite their flaws. For example, my father was not so good at hunting after a monster ate his arms. But my mother continued to love him.

Girl must really love Boog, because he has many flaws. He never smiles or shares his meat with other people. He is rude to the Old Person and will not rub his feet. Boog’s worst flaw, though, is that he disrespects Girl. He makes his voice big and snaps his fingers. It is like he is talking to a dog.

I decided to make my picture of a horse, because I knew that was a thing. It took a long time . . . my mother was watching over my shoulder the whole time and making words. “You are bad at this,” she said. “You should stop because you are bad.”

Finally, after many days of work, I finished my picture. I was about to add my handprint when I heard a familiar laugh. I turned around; Boog was there. “The picture is bad,” he said. “It stinks. I do not like it.”

I sighed. My plan had been to show my picture to Girl. But I started to worry that she would not like it. The reviews, so far, were not great.

Moog said, “It is the worst picture made yet by a human.”

The Old Person said, “I always knew you were dumb. It is known by everyone. But this picture makes me realize you are even dumber than it was believed.”

One of the main problems, people explained, was that I had not given the horse any legs. Also, I had given it hands, forgetting that a horse has no hands. I was proud of the picture when I painted it, but people’s words had made me ashamed. I decided it was best to destroy it, before Girl found out about it.

I grabbed some empty bladders and brought up water from the river. I was about to splash the painting when I heard that laugh again. “Don’t destroy it yet,” Boog said. “There is someone who wants to see it.” He grabbed Girl by the arm and thrust her in front of my picture. It was bad situation.

“Tell Oog what you think of it,” Boog said.

“I do not like it,” Girl said. “You are not smart. I love Boog and not you.” I stood there in silence. Hot water came out of my eyeballs.

Boog walked over to my pile of black rocks, picked one up, and hurled it against my picture. “Let’s go,” he said to Girl. She started to follow him. As she was leaving, she paused to take a rock from my pile. I was afraid she would throw it at my picture, like Boog had. But instead she held it up to her face and squinted at it, [then] followed him into the woods, still holding the rock in her hand.

My mother woke me in the night. “A monster is here to murder us,” she said. I nodded. This is usual occurrence.

We were silent for a while; soon, I heard a strange sound. The monster was throwing rocks against the cave, one after the other. I took my kill stick and headed outside. I saw a figure in the shadows and was about to charge it when the moon appeared suddenly between the clouds. “Girl?”

She was standing on the edge of the forest, a black rock in her hand. “Sorry if I scared you,” she said. “I came to say thank you.”

I was confused. “For what?”

“For clearing me a path.”

“How did you know it was me?”

“I took a rock from your pile and compared it with the ones on my mountain. They’re the same kind.”

I walked cautiously toward her. “Are you a witch?” I asked.

She laughed. “I’m not a witch! I just used common sense. I mean, there are thousands of black rocks piled up next to your cave.” I was still confused. She put her hand on my arm and the hairs on it stood up. “Thank you for clearing all the rocks,” she said, looking into my eyes. “It is a good path. You are good at clearing the rocks.” For the second time that night, hot water came out of my eyeballs. “I’m sorry I said those mean things about your picture,” Girl said. “Boog made me.”

“Does that mean you like my Art?” I asked.

She looked at my horse and hesitated. “It’s interesting,” she said. “But you know what I really like? Your rock pile.” She walked over to it. “It’s sort of like a sculpture.”

“What is sculpture?”

“Like a picture in three dimensions.”

Much time passed in silence. “I know I am not smart like Boog. I do not understand Art and I am bad with the numbers. But I will work hard to clear the rocks for you. And when you have child I will clear the rocks for the child. “ I paused to catch my breath. It was the most words I had ever made at one time.

“What about Boog?” she said.

I thought about it for a moment. “I will murder him,” I said. She smiled and kissed me on the cheek. It was like it had been in my dreams.

We made many words that night. Girl explained that she never really loved Boog. He just seemed like her only option. The other six men on earth, including me, had been too afraid. I confessed that I did not understand Boog’s last picture and she laughed. “No one did,” she said. “Not even Boog.”

The next day, I took a large rock and struck it against Boog’s head so that his skull cracked open and he died. Afterward, Girl and I went swimming. We have decided to have many children: one, two—maybe even a higher number.

I love Girl. Girl loves me. It is good situation.
```

---

## IC-2439: I’m Not Your Son, I am No One You Know

- Title: I’m Not Your Son, I am No One You Know
- Author (byline): Joyce Carol Oates
- Work: I Am No One You Know
- Publisher: HarperCollins
- Publication date as stated: 2005
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1543
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joyce Carol Oates
Book: I Am No One You Know
ISBN: 978-0060592899
Publisher: HarperCollins
Date (Month/Year): 2005
```

### Introduction (context only: never use it for content warnings)

```text
I’m Not Your Son, I am No One You Know by Joyce Carol Oates
```

### Performance text (classify this)

```text
DON'T MAKE EYE contact my brother warned. They'll be waiting just inside. Deftly my brother punched in the code he knew by heart. I had to be impressed, this was my younger brother and he seemed possessed of a grim knowledge of which I was ignorant.

A hefty double door with inset wire-lattice windows. Overhead, a video monitor. As soon as my brother punched in the code, the doors slid open and we stepped inside. Already the figures waiting just inside pressed forward. There were three of them. Dad won't be among them, my brother had promised. Yet my heart began to clamor, I felt sweat breaking out in all the pores of my clumsy body.

Hel-lo? Hel-lo? Son? Son? Son? Son?

The voices were calling to us, pleading. My instinct was to stop, to stare. An elderly woman with white hair lifting from her skull like electrified wire filings, a sunken-chested elderly man with a singed-looking face, a gnome-sized individual of no evident sex leaning on a walker and piping like an eager parrot, “Take me? Take me? Boys? Sons? I'm ready now. My things are ready. Take me with you? “ On his bony skull thick-lensed glasses were secured by an elastic band. The smell of them was acrid as the befouled wettish-rotting , straw in which goats dwell.

My brother yanked at me. Jesus! I told you come on.

Yet somehow in that instant I stood stone-still, unmoving. For these elderly strangers seemed to know me-how? They were pleading, scolding, bleating. Their faces were familiar to me in some way I could not comprehend. The white-haired woman had a fattish fallen body soft as a pudding but her eyes were vigilant, alert to insult. Here was a mother's voice-Dear? Dear? Come back here! Don't you walk away while I'm talking to you! Don't you walk away while I'm talking to you!-you could not ignore. And the others were crying to me, calling me Son. Son!

My brother pulled me away. Blindly we walked along the corridor.

Even now I wanted badly to look back. I wanted to explain, apologize. I'm not your son, I am no one you know. I was ashamed of myself. To turn away unheeding from another who begs you. But my brother was muttering in my ear, Keep moving. They won't follow us. They do this with everybody, I told you. It shook me up the first time, too. But you get used to it. They won't remember, see. They won't remember five minutes from now. Just don't make eye contact with them and you'll be fine.

I pushed my brother's fingers from my arm. Coldly I said, I don't like to be rude to old people.

We're not being rude for Christ's sake! It's what you have to do.

*****************

THE VISITWITH Dad -- My first at the Manor.

I'd stayed away for as long as I could but now I was here.

Dad, hi! H'lo Dad.

Hi Dad! Hey. Looking good Dad ...

Dad this is Norm, I'm Vince. You know ... Your sons. Hi Dad.

Your sons, Dad. Hey this is quite a place. Quite a ...

In this way the visit with Dad began with ebullient spirits and raised smiling voices.

This isn't Dad. This elderly man. Not Dad any longer. We could not look at each other, our eyes could not meet out of dread of Then we are not brothers, either. For we have no father any longer.

Patients like Dad were outfitted with unremovable bracelets around their left wrists with metal tags that, if brought through electronic detectors without clearance, set off alarms through the facility.

I was wondering how many times Dad had tried to escape, and when had been his last, or his most recent attempt. I was wondering how far the old man had gotten before the alarms went off. Before he was restrained. And how exactly was he restrained. Were physical restraints involved. Did strait jackets still exist.

I would not ask where Dad believed he was escaping to. The old house was gone. The past in which Dad had lived was gone. Nothing remained.

TIME FOR A walk? My brother was on his feet. I saw that his jaws were stubbled and that the stubble glinted gray. My younger brother, no longer young! When I spoke, which had not been often in Dad's room, my voice cut the air like an awkwardly brandished blade, a machete perhaps. I was remembering who the sunken-chested man was, I thought. Who the sunken-chested man had been.

Three of us on our feet. My brother led the way. We walked slowly. There was no hurry. My brother led us past a nurses' aide putting soiled diapers into a black plastic bag on a cart. The double door to the garden was unlocked. My brother was saying in his loud cheerful voice, Dad is one of the best gardeners here. Dad, show us your tomatoes.

In my right hand, somehow related to this strange cessation of time, was an elderly man's hand. It was a bony hand, unresisting. My brother gripped the elderly man's other hand in his left hand. Dad's hand trembled yet remained unresisting, like a hand made of slightly crumbling clay.

We were not alone in the garden. Other grown children were visiting with elderly adults. Never more than three individuals in a party, for too many visitors confuse the elderly residents. Before my brother had punched in the code to open the doors, he'd told me that Dad no longer recognized himself in mirrors, so don't expect him to recognize you.

I had not that expectation. I took my cue from my brother, I smiled. I had no expectations.

I was calm recalling: the sunken-chested man with the singed face, Mr. M_ who'd taught junior high math. He'd taught me, he'd taught my younger brother. More than thirty years ago he'd taught us. Mr. M_ was not a name I wished to recall. Mr. M_ had taught at Yewville Junior High for a long time before they'd made him retire. Under threat of a lawsuit, or an arrest.

Certain boys were Mr. M_'s targets. You could see why certain boys were not Mr. M_'s targets for he never dared single out any strong-willed or defiant boy, or any boy from a prominent family, and boys of limited intelligence he ignored; but you could not always predict which boys, out of a number of possibilities, he would choose to torment. Vulnerable boys, shy boys. Small-boned boys. Boys with girls' faces. Rarely homely boys. Never handicapped boys. Never Italian or Negro boys.

First he'd call on you in class and if you gave the right answer he'd call on you repeatedly until at last you gave a wrong answer. Once summoning me forward to his teacher's desk at the front of the room. Making of me a witness to his red-inked pen darting and swooping over my math test like a miniature deranged hawk. I had mis-numbered the questions! I was a careless boy! Might've had a grade of ninety-eight but now had a grade of forty-eight. Tears welled in my eyes. My nose ran. Disgusted Mr. M_ tossed a tissue at me. It might have been a used tissue, out of his baggy pants pocket. Wipe your nose, Mr. M_ said. Stand up straight, Mr. M_ said. What a careless boy you are, not nearly so smart as you think you are, I've got your number. For it was so, there were boys (but never girls, and we never wondered why) of whom Mr. M_ could boast I've got your number.

Almost time for dinner, Dad. My brother spoke brightly as if he'd made a new discovery, and it pleased him. I had forgotten that time wasn't fixed like concrete but in fact was fluid as sand, or water. I had forgotten that even misery can end.

Got your number, got your number. Just ahead the sunken-chested old man with the singed face, the thick-lensed glasses taped to his head, was leaning on his cane. Again we must pass close by him. He wished to block our way. Here was Mr. M- wizened as a scrawny child. His face had lost its fat, his cheeks were papery thin and flushed as if with fever. I saw how, as his eyes lighted upon us, Mr. M-'s expression turned hopeful, shrewd. For the first time I saw how his dentures glared like cheap porcelain.

“Boys? Take me with you? Take me with you?” He lurched near me, his palsied hand groped for my arm, and I shoved him from me. Mr. M_'s fetid breath in my face, that made me gag.

“Don't touch me,” I said. :You're not going anywhere with anyone, you old bastard. Your place is here, you get to die here.”

My brother turned an incredulous face to me. Yanking at my arm to pull me away from the tottering old man who gaped at me as if he hadn't heard a syllable of what I'd said.

Norm! For Christ's sake.

Why didn't you warn me, I asked my brother. You knew who he was.
```

---

## IC-2440: Joey Pigza Swallowed the Key

- Title: Joey Pigza Swallowed the Key
- Author (byline): Jack Gantos
- Work: Not specified
- Publisher: Square Fish
- Publication date as stated: July 2014
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JOEY, GRANDMA, MRS. MAXY, MOM, PRINCIPAL
- Teaser before the introduction: Yes
- Spoken words (computed): 1711
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jack Gantos
ISBN: 978-1454953371
Publisher: Square Fish
Date (Month/Year): July 2014
```

### Introduction (context only: never use it for content warnings)

```text
Meet Joey, a bright, good-hearted boy who struggles with ADHD. Joey knows he’s different—he has trouble focusing, sitting still, and making good choices, even when he wants to and his wild behavior often leads to trouble at school. But at home, things are no easier: his grandmother is manipulative and abusive, and his mother, though trying her best, has a history of drinking and instability – But he’ll get back to you on that . . .

Joey Pigza Swallowed the Key by Jack Gantos
```

### Performance text (classify this)

```text
JOEY: (Pg 3-4) At school they say I’m wired bad, or wired mad, or wired sad, or wired glad, depending on my mood and what teacher has ended up with me. But there is no doubt about it, I’m wired. One day, we were doing math drills in class and every time Mrs. Maxy asked a question, like “What’s 9 times 9?” I’d raise my hand because I’m really quick at math. But each time she called on me, even though I knew the answer, I’d just blurt out, “Can I get back to you on that?” Then I’d nearly fall out of my chair laughing. (laughing heartily) Can I get back to you on that? “Out in the hall,” she said. And the class cracked up.

JOEY: (Pg 7-9) My dad ran off when I was in kindergarten and my mom went after him. My grandmother raised me until this past summer. That’s when my mom finally turned around and remembered me. One morning she rang the doorbell. I wasn’t sure she was my mom because I didn’t even remember what she looked like.

I was a wired-up mess by the time Mom came back. By then everyone thought my grandma was the nutty old lady responsible for my bad behavior. But I am how I am because Grandma was born wired, and my dad, Carter Pigza, was born wired, and I followed right behind them. It’s as if our family tree looks like a set of high-voltage wires strung across a field from one steel tower to the next.

GRANDMA: Joey, I want you to pull your act together. You don’t want to turn out like your father, do you?

JOEY: (Pg 10-11) People who blame Grandma for my behavior are unfair to think that she was the crazy one and I was innocent. It was more that we were whacked-out partners. I’d be the Hulk and she’d be Doctor Doom and when the phone rang, we’d run at it screaming and yelling and slam into each other, and by the time one of us got the upper hand the person on the other end had hung up. (beat) Sometimes she could be funny. But not often. Most times she’d just get mad . . .

GRANDMA: Don’t touch. Don’t wiggle. Don’t run. Don’t yell!

JOEY: (Pg 12) After Mom came back Grandma got worse. She got meaner and she began to scare me. (Pg 15) She’d say the same thing over and over again:

GRANDMA: (Pg 14) You don’t know what you’re doing. You’re ruining everything. You never listen to me. I always said you were as dumb as dirt!

JOEY: (Pg 12-13) About a month before school started she got so mad at me she threw everything out of the refrigerator, yanked out the shelves and flung them across the floor.

GRANDMA: Now get inside and stay inside! I said get in or I’ll tell your mom!

JOEY: But I wouldn’t get in. I knew there were good rules and bad rules, and having a time-out inside a refrigerator was a bad rule. She should have been on meds. Big-time Grandma-sized meds. People just called her a batty old bird. But she was sick like me, only old, so her sickness was different. (thinking, then softly) (Pg 3) Can I get back to you on that? (shakes it off and gets lost in the story again) [Transition: Oh, yeah . . . So anyway, it was out in the hallway at school . . . ] (Pg 4-5) I stood in the hall for about a second until I remembered something I wanted to try. I had seen the Tasmanian Devil on TV whirling around like a top so I unbuckled my belt and pulled on the end really hard, as if I was trying to start a lawn mower. Before long I was bouncing off the lockers because I was dizzy too. I got going really fast and began to snort and grunt like the Tasmanian Devil (snorting and grunting) until Mrs. Maxy came out and clamped her hands on my shoulders. She stopped me so fast I spun right out of my shoes! (Pg 6) And we had a little talk about my behavior goals

MRS. MAXY: (Pg 25) Joey, there are limits in the classroom. And if you can’t live by the class rules then we’ll have to send you down to the special-ed class for extra help. We’ve talked to your mom about this.

JOEY: Okay (to audience) only saying the word because agreeing to stuff was the best way to make it stop. (to Mrs. Maxy) Okay. Okay! (takes some deep breaths to calm down) (Pg 28) [Transition: When I got home, Mom said] now let’s get you some medicine. She put a pill in my hand and a glass of water in the other, but before I could take the pill, she got the bottle of Amaretto.

MOM: (pouring it into a glass) See, Mommy has her own meds.(raises the bottle to Joey) It comes in a bottle.

JOEY: We clinked glasses and I took my pill. I could feel it going down my throat like a little white round superhero pill on its way to beat up all the bad stuff in me. Everyone said it would help. And it did. I felt like a normal kid for a while. But then my old self started to sneak up. (shakes head in bewilderment, long beat)

(Pg 30) I was sitting at my desk after lunch and Mrs. Maxy was writing a long list of spelling words. I was playing with the house key that was on a long string around my neck. (Pg 31) I was trying to train myself to swallow the key so I could slowly pull it back up from inside my belly, like I was fishing. It hurt because sometimes the key got caught sideways, but I just gave the string a tug and straightened it out. Since I was doing it after lunch, bits and pieces of food would stick to the key and around the string and I’d suck them off.

(Pg 32-33) Suddenly Mrs. Maxy swooped down on me. She yanked the string out of my mouth, took her sharp “teacher only” pointy scissors and cut the string and put the key in my T-shirt pocket.

MRS. MAXY: Keep your mind on your work.

JOEY: (Pg 3) Can I get back to you on that? (beat) So . . . my mind wandered and before long I didn’t remember about the string missing and I plucked the key out of my pocket and popped it into my mouth. (showing the key on his tongue and whispering to another student) What’ll you give me if I swallow this? (not waiting for an answer) I worked up my saliva and swallowed hard . . . I did it! (opens mouth to show it’s empty) Then I reached to pull the string . . . (panics when he can’t find it, he screams) Mrs. Maxy, I ate my key! (takes some deep breaths to calm down) (Pg 69) I was one of the special people. My mom said I was special, the nurse said I was special, and I was also in special ed. (Pg 73) Even though I’m difficult I’m very special and smart. (Pg 76) (shouting) Math drills are one of my strengths!

[Transition: Another day at school I stayed in at recess to] (Pg 72) make a million bumper stickers that say ‘Hate Is Not a Family Value.’ My mom saw one and said she wished she had a million to put on every car in the world. (Pg 73-75) I got the safety scissors and began to cut the poster board into bumpersticker-sized strips. But [it] was too thick and the scissors kept twisting. The bell rang, so when Mrs. Maxy got up from her desk to stand in the hall, I snuck up to her desk and grabbed her secret extra-sharp teacher scissors. I was racing back with scissors in my hand when it happened. I tripped and sort of dove through the air with the open scissors in front of me like some evil Big Bird’s beak when Maria walked sideways across my path. (look of shock and horror)

I thought I was the one who was screaming. But it wasn’t me. (getting excited) You should have seen the blood. It was like a pipe had burst. And she stood there shaking with her eyes wide open like she stuck her finger in the electric socket. I bent over and picked up the tip of her nose, which looked like a tiny piece of sliced banana. Then I stood up and pressed it back in place, but the blood sprayed out like a shower nozzle. (panics again, shrieking) I’m sorry! I’m sorry!

I tried to wrestle the scissors from Mrs. Maxy who had taken them from me because I wanted to cut my whole nose off to show just how sorry I was. But Mrs. Maxy wouldn’t let me have the scissors and she kept shouting, “Time out! Time out! Go to your corner!” But I was so nuts I couldn’t tell you the difference between a corner and a circle or a square. It was bad, and everyone was staring at me like I was a maniac killer. (begins to cry)

****Meeting with Mom and the Principal*****

PRINCIPAL: Because he has injured another student, he has to be suspended and receive mandatory counseling. That is school policy. The district special-ed bus will pick him up. Given Joey’s record, he was bound to end up at the center anyway. Maybe this is a blessing in disguise. What happens now is all up to him. . .

JOEY: (crying) (Pg 3) Can I get back to you on that? (Pg 90)

(long beat as he composes himself) I’m Joey Pigza. (Pg 51-52) I can have good days. (proudly) Entire days when I wake up and I’m calm inside like water when it’s not boiling. I just get dressed and eat breakfast, thinking about what I’d like to do with my day. And then the most amazing thing -- after I think about what I want to do, like read, or see a friend, or write a poem, I actually do all that stuff. (incredulously) I think it, then I do it. This is not how I usually operate. (rate of speech picking up quickly) Usually I wake up with springs popping inside my head, shoot out of bed and directly to the kitchen where I ricochet around after food, zing up the hall to the bathroom where I try to brush my teeth, but I brush mostly my lips and chin and then I explode across the living room and carom off the furniture until Mom gets a grip on me and wipes the toothpaste off my face and works a pill down my throat. From Ricochet Rabbit to Charlie Brown in no time flat. (long beat)

I love it when the meds work, and when I go to school and stay in my seat and kids don’t call me Zippy and teachers pat me on the head and give me gold stars and say nice things to me. (beat) (gathering up his courage) (Pg 73) Even though I’m difficult I’m very special and smart. (Pg 76) (he does a little dance and yells) Math drills are one of my strengths!
```
