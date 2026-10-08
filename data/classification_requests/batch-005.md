# Classification request: batch 5 of 63 (40 records, IC-0161 to IC-0200)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-005-reply.json`.

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

## IC-0161: Grey Gardens

- Title: Grey Gardens
- Author (byline): Doug Wright, Scott Frankel and Michael Korie
- Work: Not specified
- Publisher: Dramatists Play Service Inc.
- Publication date as stated: May 2008
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: EDITH, EDIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1240
- Already set (do not supply): none

### Source block (context only)

```text
Author: Doug Wright, Scott Frankel and Michael Korie
ISBN: 978-0822221814
Publisher: Dramatists Play Service Inc.
Date (Month/Year): May 2008
```

### Introduction (context only: never use it for content warnings)

```text
Welcome to the private world of the Beale ladies, outcasts of a wealthy and famously dysfunctional branch of the Kennedy dynasty—the Bouvier-Beales. Little Edie, born in 1917 was the family beauty, “surpassing even the dark charm of Jacqueline,” She was her mother’s crown jewel. Her debutante party in New York City was covered by The New York Times. She dated Howard Hughes and turned down marriage proposals from JFK’s oldest brother Joe Jr. and millionaire J. Paul Getty. They lived the life of American Royalty until Little Edie’s father left, divorcing her mother by telegram, from Mexico. He left his ex-wife Grey Gardens, a spectacular 28-room mansion with a view of the ocean. And this is where the story becomes something from a gothic novel. And this is where the story becomes something from a gothic novel.

Grey Gardens by Doug Wright, Scott Frankel and Michael Korie
```

### Performance text (classify this)

```text
EDITH: (Pg 62) Edie? Edie!!

EDIE: (Pg 2) I’ve found it, Mother Darling! I found your old record! (puts record on the
record player and begins singing)
She is the girl
Who has everything.

EDITH: EVERRRYTHING!!

EDIE: She has the world on a string

EDITH: ON A STRRR-ING!

EDIE: (appears from off stage. She primps, looking at herself in a hand mirror) Isn’t it wonderful?

EDITH: I recorded it in 1941. I was very serious about my singing; loved it!

EDIE: (Pg 69) Just listen to this! (as Edie speaks, Edith begins to prepare dinner for the feral cats living in their house) The Hamptons Bee. July 1972. “The elderly, bed-ridden Aunt of former first lady Jacqueline Kennedy, Mrs. Edith Bouvier Beale and her adult daughter, Miss Edie Beale, a former debutante, are living on Long Island in a garbage-ridden, filthy, 28-room room house with fifty-two cats, fleas, cobwebs, and virtually no plumbing. After vociferous complaints from neighbors, the Board of Health took legal action against the reclusive pair” (Pg 3) They’re calling us “cat ladies.”

EDITH: Here kitty!

EDIE: And our house. They’re saying Grey Gardens is a “public eyesore.”

EDITH: Grey Gardens is one of the most renowned homes in America! (singing again) SHE IS THE GIRL WHO HAS EVERYTHING . . .

EDIE: Remember? You sang this song for me. I was “The Girl Who Had Everything” . . . once.

*****(Flashback to 1941 – Little Edie’s engagement party)*****

EDITH: (Pg 4-6) SHE IS THE GIRL WHO HAS EVERYTHING . . .
TALENT AND BEAUTY SUBLIME . . . .!
. . . THE CROWDS AND THE CLAMOR
AROUSED BY HER GLAMOR
WILL FADE LIKE THE ECHO OF A CHIME

EDIE: (Jumps up and applauds) Mother Darling, what a charming song!

EDITH: The gift of music for your special day.

EDIE: It’s almost too much. Truly. Promise you won’t perform it for anyone but me.

EDITH: Why, Edie, whatever do you mean?

EDIE: Well, “The Girl Who Has Everything?” Honestly! What would people think! (Pg 8) (Edie speaks to the audience) She stopped my cotillion cold and performed all three arias from Faust. My graduation tea . . Carmen with a rose in her teeth. My birthday . . . she danced Salome! Wouldn’t it be an odd thing if – on your death certificate – it actually said that you died of shame? (Pg 16-17) (She notices a recital brochure on top of the piano)

EDIE: (holding it up) Why, Mother Darling, what’s this?

EDITH: Oh dear. You weren’t supposed to see that. It was meant to be a surprise – (She takes the brochure and admires it) (Pg 9) A musical recital in honor of Miss Edith Bouvier Beal and Mr. Joseph Patrick Kennedy, Jr. the 12th of July, 1941!

EDIE: You’re planning to sing?

EDITH: (Pg 18) Who knows if we’ll ever have another party?

EDIE: It’s just that Joe’s parents are coming, and they’re so terribly New England. I don’t expect they listen to music at all.

EDITH: Nonsense! I’m sure they’d be delighted. (Both characters overlapping)

EDIE: (Pg 19) Decorum, Mother, that’s all I ask! . . .

EDITH: Decorum? Oh, that’s rich! You’re a fine one to lecture me about propriety!

EDIE: When she doesn’t get exactly what she wants, she positively spits venom!

EDITH: Wearing lipstick to school- “temptation red” - at only thirteen; the whole town was talking!

EDIE: Pish posh, mother! You’ll say anything to be a dramatic, anything to garner attention.

EDITH: This very house was positively blanketed in adolescent shame.

EDIE: (Pg 20) Who’s engagement is this anyway? (Beat, then regretfully) (Pg 39-40) Mother, I-

EDITH: Don’t! (She puts down the brochure quietly on the table, spirit broken)

EDIE: (Edie feels horrible and picks up some sheet music from the piano – softly) Is this [one] on the bill? It’s one of my favorites.

EDITH: (Interrupting) Edie. Please.

EDIE: It’s the very first song you ever taught me. We used to sing it together.

EDIE: (Pg 41) (Singing – Edith perks up throughout the song)
WE’RE A BOWL OF PEACHES AND CREAM
THE DODGERS AND BROOKLYN
A PERMANENT TEAM
INDIA AND GANDHI
DAGWOOD AND HIS BLONDIE
TWO PEAS IN A POD

EDITH: (Pg 43) Oh, Edie. I’ve been monstrously selfish. All eyes should be on you, darling. You and Mr. Kennedy. (Edie exits – While Edith entertains the crowd including EDIE’s fiancée with a story) (Pg 50) Exquisite diver, our Edie . . . Her swimming costume clung to her like skin on a peach. Well, she went sailing into the water . . . and the seams split. Well, a lesser girl would’ve shrieked and run for cover. But not Edie! She swam the length of the pool. Twice! And when she climbed out, Mr. Kennedy, no one offered her even a towel. Edie walked right past them! She became the most talked about girl in town!

EDIE: (to audience - horrified) (Pg 52) What? No! She didn’t . . . she wouldn’t!

TRANSITION

From 1947 to 1952, Little Edie lived at the Barbizon Hotel for Women in New York City, hoping to land her “big break” in show business. Max Gordon, the successful Broadway producer, saw potential in Edie and invited her to audition for the Theatre Guild that summer. But it was not to be. In 1952, Big Edie called on Little Edie to return home from NYC. Her health was poor, and she needed someone to take care of her. For the next two decades, Edie and her mother lived in a fantasy world of their own creation. Re-living the past and ignoring the squalor

EDIE: (she speaks to the audience as she is feeding a hoard of cats) (Pg 79) I think the saddest thing was my not marrying. I missed out on everything . . .

EDITH: (Pg 83) Edieee!!!!

EDIE: I’m feeding the cats!! . . . (to herself) When am I going to get OUT of here??

EDITH: (Pg 84) EDIEEEE! (Pg 102) You know what I’d like? Some music. I’m happier when I’m singing than anything I’ve ever done since I was born. See if you can find . . . that song. The one I just adore . . .

EDIE: Oh, sure. (bitterly) “The Girl Who has Everything”

EDITH: No, heaven’s no . . . the flipside (Edith sings mean-spiritedly) (Pg 80) IS IT MY FAULT THAT YOUR CAKE FELL FLAT?

THAT YOU’RE UNMARRIED
BALD AND FAT?
AS THE WORLD WALTZED BY
AND EDIE SAT . . . .

EDIE: (Pg 80) Sometimes I think I have the saddest life . . .

EDITH: (Pg 128) Oh, Edie! Wouldn’t you like a cup of soup? With some oyster crackers? Wouldn’t it be too divine? Have a cup of soup with your mother won’t you?

EDIE: Which would you like, Mother Darling? The cream of tomato or the bisque?

EDITH: You choose.

(Edie notices the old record player and crosses to it, raises the lid, flips the record over and drops the arm. She then turns to her mother. She sways to the music and sings with a recording of her younger self)

EDIE: Will youuuu? (Pg 112) The last time I performed this song . . . when was it?

EDIE and EDITH TOGEHER: Will youuuuu? (Edith stops singing. She looks at Edie disapproving)

EDITH: You’re singing it incorrectly. Very ugly.

EDIE: Will youuuuuu?

EDITH: (pg 113) That’s not it! You’re waaaaay off. Go to the bottom of the class! Everything is perfectly disgusting on account of you! Bring me my radio? I have got to have some professional music!

EDIE: (Edie deliberately yanks the needle across the record, scratching it. The music stops) I stood for you all these years.

EDITH: Well, of course you did! You’d no place else to go –

EDIE: Not true! I was going to the White House! (Edith shakes her head) I was! With Mr. Joseph Patrick Kennedy.

EDITH: (Pg 114) Pick up a fresh paper: that’s yesterday’s news!

EDIE: He was keen for me, but you got rid of him because he came from a celebrated family.

EDITH: That’s the way! Pin it all on Mama!

EDIE: You got rid of him in fifteen minutes flat

EDITH: You did all that by yourself

EDIE: (To audience) She’s very mean to me!

EDITH: (Pg 115) I didn’t want my child to be taken from me! I’d be entirely alone!

EDIE: (Pg 116-118) I took care of you! I took care of this damn house for twenty-five years!

EDITH: You didn’t have to! After [your father] got his Mexican divorce, I wanted him to come home -- back to Grey Gardens! (Following lines are spoken over one another as each focuses on their narrative)

EDIE: As long as my father was alive –

EDITH: So we could be a family again, like other families

EDIE: He wanted to ruin my life!

EDITH: But Edie said “No”

EDIE: I was scared to death of him-

EDITH: She said she’d “leave the house forever”

EDIE: I didn’t want him here – screaming at me all the time: Take off that lipstick

EDITH: If Mr. Beale ever came back to Grey Gardens!

EDIE: Wash off that perfume

EDITH: She actually threatened to run away

EDIE: How dare you wear high heels

EDITH: If my husband - her father - came back!

EDIE: I didn’t need the humiliation

EDITH: Tell the truth, Edie

EDIE: I knew if [he] came back, I’d never get married!

EDITH: That’s not the reason!

EDIE: I’d never find a man!

EDITH: That’s not it at all!

EDIE: Mother please!

EDITH: (angrily warning) Edie! (delicately now) You needed to come home . . .

EDIE: (Steely and silent. Too much has been said. She plucks the radio up and takes it to her mother. Her voice is strained) Your radio, Mother Darling. (Edie exits)

EDIE: (Pg 123) (In the front yard, she stops at the garden gate)
Sings:
NEW WORLD AWAIT
JUST FLIP THE LATCH
AND THROUGH THE GATE
GO THROUGH THE GATE
THE GARDEN GATE
MY MOTHER’S GATE

(She stands, frozen. Try as she might, she cannot bring herself to flip the gate latch)

EDITH: (Pg 127) (As Edie stands mute and silent, from upstairs, we hear the familiar cry) Edie! What have you done? Where have you gone? (The call cuts through EDIE like a knife, but she does her damnedest to ignore it) I’m all alone! Edie! The radio; it’s gone dead. (Edie shudders in the evening air) Edie! I’m starving! I want my supper. I need your help!

EDIE: (A sigh of resignation and then) Coming, Mother Darling!
```

---

## IC-0162: Gwen and Gwen

- Title: Gwen and Gwen
- Author (byline): Nancy Kiefer
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: April 2017
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: GWEN, GWEN II, MOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 2056
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nancy Kiefer
ISBN: 978-0573630408
Publisher: Samuel French, Inc.
Date (Month/Year): April 2017
```

### Introduction (context only: never use it for content warnings)

```text
The voice . . . HER voice was back. Stronger than ever. And now Gwen not only could hear her . . . she could see her too. Life is often hard, but it’s even harder when you are battling a mental illness. Gwen and Gwen by Nancy Kiefer
```

### Performance text (classify this)

```text
Gwen stands in the center of the room, very nervous and waiting expectantly for something; phone rings; she takes the receiver off the hook, but it continues to ring. She grabs a broom to frantically sweep the floor. A pounding at the door; she looks at her watch)

GWEN: (Pg 15-17) Seven o’clock . . . seven o’clock . . . Estelle’ll call at nine . . . at nine. (Faces the door directly) I go nothing to say to you! I got my own apartment now! You’d just make fun of it, but it’s mine! And a job! A job you’d laugh at, but I got a job! (Pounding continues; phone begins to ring again) And I got a friend! Estelle is my friend, and you can say anything you want, but she’s my friend! And I’m gonna get my kids back, too! You can pound on the door and let the phone ring all night, but I won’t talk to you! I won’t!

(pounding on the door and the phone ringing stop; the door suddenly bursts open. Gwen II is standing in the doorway, annoyed. She enters the apartment and slams the door behind her)

GWEN II: What’s with you, Gweny? Don’t you believe in answering your phone anymore? Your neighbors aren’t going to appreciate it if you let your goddam phone ring all the time. They’ll report you and you’ll get your ass thrown out. Besides . . . what if it was him? What if he was trying to call you?

GWEN: (Weakly) . . . please . . . please go away.

GWEN II: Like hell! I need a home just as much as you do! You know what you are, Gwen? You are inconsiderate. You found a home for your kids. You found a padded cell for yourself to hide in. What about me, huh?

GWEN: I was not in a padded cell. I was in a group home.

GWEN II: (critically surveys the room) What a crummy dump this is. You’re in big trouble, Gweny.

(Looks at Gwen for a long time)

GWEN II: (Pg 17-18) You’re looking well, Gwen. Certainly better than when we parted company a year ago. So how’s the kids? They been split up and put into foster homes yet?

GWEN: Get out of here! This is my apartment.

GWEN II: Tell me about this Estelle woman.

GWEN: She was my social worker at the home. And she’s . . . she’s my friend.

GWEN II: If they took her paycheck away, would she still come around? Would she still be your friend? Let’s get her fired and find out.

GWEN: She’s going to call me at nine.

GWEN II: So what? Is that supposed to intimidate me? Am I supposed to be scared or something (Laughs) (Pg 20-21) So what happened to that broad who was supposed to move in here with you? How come she didn’t, huh?

GWEN: Billie . . . her name was Billie. She was . . . sad. She couldn’t take care of her children. Billie had to go back to the hospital. She had a relapse. But before that we shared a room in the group home. We talked a lot . . . watched television at night.

GWEN II: (cuts her off) Sounds like a real drag. Two losers who deserted their kids sittin’ around watchin’ the idiot tube and poppin’ antidepressants.

GWEN: You haven’t changed a bit, have you?

GWEN II: (Intensely) Did you really think you could put me in permanent cold storage, Gwen? That a few months in a padded cell with some soggy social worker tellin’ you that you’re really not a *screw*-up would get rid of me? (menacing whisper) All I did was wait . . . I just waited. (Gwen laughs nervously) (Pg 22) (threateningly) And don’t laugh at me, or I’ll slap that smile off your ugly face. Don’t laugh at me and don’t abandon me again. (Pg 25) (Hits Gwen across the face) Don’t you ever again pay some jailor to suppress me into nothingness so you can pretend for a few months that you’re sane! (She calms herself)

GWEN: (Pg 23) You are so jealous . . . so jealous!

GWEN II: (Pg 26) Yes, Gwen. I’m jealous . . . of everyone whose parents are kind and wise and who grew up smart and pretty and loved. I’m jealous of every woman he touched, every woman he wanted. (Pg 30) You are the guilt and I am the jealousy. You were always the one who felt certain that every time somebody got shit on, it was your fault. You were the one who took the blame and I was the one who hated. You were the martyr and I was avenger. What a pair, what a team.

GWEN: Get out! Just get out of here!

****** one week later******

GWEN II: (Pg 36-37) (tenses up and looks around the room, sniffing) I smell a rat! Someone’s coming.

GWEN: (Panicky) My mother?! My mother?! I don’t want to see her! I don’t want to talk to her! What should I do? (firm knock on the door) Go away! Go into the bathroom! Don’t talk to me! (GWEN II complies and exits) (Gwen answers the door) Mom . . . Mom . . . you didn’t call . . . I wasn’t expecting you.

MOTHER: (looks critically around the room)Good lord! (Pg 38-39) I know the rent’s cheap, but really Gwen. There must be rats and roaches here. No matter where we lived, Gwen, I always kept it clean. You’ve been here for over a week. Don’t tell me you haven’t had time to clean.

GWEN: Mom . . . it’s been hard for me. Hard to go back to work. I guess when I come home, I feel . . . I feel . . . depressed.

MOTHER: (Starting to clean) Everybody gets depressed, Gwen. Do you think you’re the only person? Besides, I thought that year you spent in that . . . home was supposed to make you well again. Your sister took your children in for an entire year!

GWEN: (Pg 40-41) I know I’ve been a big inconvenience to everyone, Mom. (Pg 41) I never expected Kathleen to take care of the kids forever.

MOTHER: Well, I should hope not. You had them, Gwen. You married a man I begged you not to marry and had children with him. I warned you he’d never support you. You wouldn’t listen, and now those children are your responsibility. Not your sister’s and certainly not mine.

GWEN: I can change . . .

MOTHER: . . . I hope so, Gwen. Men have affairs and leave their wives all the time. Life has to go on. I have never been able to understand why you allowed yourself to fall to pieces like you did.

GWEN: Mom . . . Mom . . I guess . . it was more than that. (starts to cry)

MOTHER: (Pg 42-43) (stops cleaning and looks critically and unsympathetically at GWEN) Snap out of it, Gwen. I did not come here to listen to you whine.

GWEN: I’m sorry. I’ve just . . .just got a lot of problems, Mom.

MOTHER: Well don’t blame them on me. You can’t go through life blaming other people for your problems, Gwen. At some point you have to take responsibility and shape up – or ship out.

GWEN: You’re right . . . you’re right (trying to stop crying) I’m grateful for everything you’ve one for me.

MOTHER: You’ve had your year of relaxation! Now it’s time to get back to work.

GWEN: (Astonished) I wasn’t relaxing, Mom. (Confused) Mom . . . Exactly what do you want me to do?

MOTHER: (Pg 44) I want you to stop thinking about yourself, Gwen. Think of your children. They are far more important than you . . . You were always look[ing] for attention. I think you’ve had enough for one year, don’t you? Your sister’s divorced and she’s been jilted by men, but she didn’t abandon her children. (a long beat)

GWEN: (Pg 45) (obviously fighting to remain civil) Mom . . . you getter go home. Dad might need you. I can finish this.

MOTHER: (Relieved Mother grabs her coats and prepares to leave) But will you? (Smiles coldly at her) I didn’t raise my children to live in pig pens. (Exits)

GWEN II: (explodes out of the bathroom) Get outta here, you bitch!!! (to Gwen) Just because there’s some obscure code of human ethics that says you’re supposed to feel gratitude towards your parents, you don’t have to go along with it! Name one thing she ever did for you! I hate her! Parenting skills of a f***** rattlesnake. People like her shouldn’t be allowed to breed.

GWEN: (Pg 47) I’m not like you . . . I can’t talk like you. (Pg 48-49) (repeating a litany she’s clearly said over and over) My mother is kind. She is thoughtful and caring. I’m not going to let you destroy the progress I made.

GWEN II: Progress? Look around you, Gweny. Look at this mess. Does this look like the home of a woman who’s made progress?

GWEN: (looks around her and then closes her eyes) . . . yes. Because all it means is that I’m out of the group home and on my own.. It doesn’t matter what the place looks like.

GWEN II: Where are your kids? You haven’t got the guts to call them! You still can’t stand up to your mother. You call that progress? (Pg 50) I get [so] tired of you, Gwen. I get tired of what a spineless, uninteresting loser you are! (to herself) Damn her. Damn her to hell!

GWEN: (Pg 51) (softly to herself) . . . and I’m going to get them back just as soon as I can . . .just as soon as I can . . . just as soon . . . (Pg 56) I want to see them . . . I do . . . [but] I don’t want them to see me like this. ***** one month later *****

GWEN II: (Pg 59) You’re stupid and you’re also a pathological liar!

GWEN: (Pg 60) Why do you talk like that?

GWEN II: I beg your pardon. I don’t talk like that. You talk like that. If somebody walked in here right now, who would they see? Just you, sittin’ around talkin’ to yourself. You’re becoming dysfunctional.

GWEN: (Angrily) Alright! Alright! And why am I dysfunctional? Does it have anything to do with your existence?

GWEN II: I come in when you let me in. I come in when you hate yourself and when your guilt is eating you up like a cancer. I’m all that’s left of your dreams. I’m the only one who can help you. (Pg 61-62) Did you ever read your chart in the nut house?

GWEN: No, they didn’t let us . . . why?

GWEN II: Well, I did. . . A serious personality disorder due to critically low feelings of self-worth who is potentially homicidal. (she looks dangerous)

GWEN: (Frightened) What’s that supposed to mean?

GWEN II: It means that son of a bitch who dumped us and got married to Miss Mummy Face with her CPA and her Volvo is finally, finally going to care about us when I point a gun in his sinking face!

GWEN: (Terrified) No . . . I couldn’t kill anybody . . . not anybody! (changing the subject) I want you to tell me why I don’t want to see my kids.

GWEN II: (Pg 63-64) You don’t want to see your kids, Gwen, because you hate your kids. You convinced yourself that he dumped you because of the kids. He was never a family man. You knew that. You got yourself knocked up twice, thinking that would make him stay with you, but it didn’t!

GWEN: (with increasing rage) . . . get out . . . get out of my house! Get out of my house!

GWEN II: Remember what you did that night you called him and she answered?

GWEN: I cried myself to sleep.

GWEN II: (Scoffs) You slapped the girl across the face, told her it was all her fault that he left you, and you didn’t feed either one of ‘em for three days. The girl went to school bruised and wearing dirty clothes. The boy sat in a corner and cried while you laid in bed in a drunken stupor, moaning over the fact that that stupid asshole left you. The school called the county child abuse authorities and next stop, Estelle’s nut house!

GWEN: (Pg 65) I do not hate my children!

GWEN II: (Pg 68) (dismissively) Get hold of yourself, Gweny. We need to think of something to do for entertainment this evening. Um . . . I know! Let’s tell each other secrets.

GWEN: I don’t have any secrets.

GWEN II: True. But I’ve got a few. They’re just oozing out of me. (She goes to the bed and reaches in between the mattress and pulls out a handgun.) Secret number one. (waves the gun in Gwen’s face) Remember this?

GWEN: (backs away in fear) No!

GWEN II: Sure you do. Last month? Meeting at the nut house. Sneak upstairs afterwards hopin’ that crazy Billie forgot to take her gun from beneath the floorboards. Well she forgot! (Pg 74-76) (forcing the gun into Gwen’s hands.)

GWEN: (Starts to cry) . . . I’m . . . I’m afraid . . . of you.

GWEN II: (Grabs Gwen’s hands and tries to get her to aim the gun at her head) Do it! Get it over with!

GWEN: (Struggling) No!

GWEN II: You’re a loser, Gwen, A Loser. He’s gone. He’s married . . .and he ain’t ever gonna call you again. Do it, Gwen. Put a dignified end to this . . this joke . . . this farce we’ve become.

GWEN: (in a very weak voice that begins to gain strength as she speaks) . . . things can change . . . people can make things change . . . we . . . we can reunite.

GWEN II: It takes a powerful chop to cut a person in two like this, but when it happens, there’s no point in going on.

GWEN: . . . people still fall in love . . . people still fall in love . . .

GWEN II: But not people like you . . . not people like us. (Gwen slowly raises the gun and points it at Gwen II. She shoots her) Now you’ve only got one bullet left. . . don’t miss. Embed it in what’s left of your brain. I’ll survive for a short time after you’re gone. I shall speak the last word. (Pg 77) A name . . . what’s the last name you want me to say, Gwen?

GWEN: (In control now . . . a long beat) Alright. Say your children’s names!

GWEN II: (turns away defiantly) I don’t have any children.

GWEN: (Pg 78) You are woman with two children, a son and a daughter. (She tosses the gun on the bed and commands) Say their names!

GWEN II: Say them yourself.

GWEN: (Pg 79-80) Say YOUR name . . . SAY IT!

GWEN II: (battling to stay in control she forces out the words) I am Gwen Kessler. I just got out of the nut house. My life has been an abysmal failure and I possess no foreseeable future. I am angry. I abused and neglected my children. I have a gun with one bullet in it . . .

GWEN: (Shoves her away) I am Gwen Kessler . . . and I have two children . . . Diane and David (Pg 82) I’m going to call my children!

GWEN II: (Pg 83) (Desperately trying to maintain control) You abandoned them! They hate you! You said it was their fault he left you! You wished you never had them!

GWEN: (with conviction) My children love me . . .and I’m going to call them.

GWEN II: (weakly) But what will we say? We hurt them! What will we say?

GWEN: (with strength as GWEN II fades) . . . we’ll say their names (Picks up the phone and begins to dial)
```

---

## IC-0163: Haiku

- Title: Haiku
- Author (byline): Katherine Snodgrass
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 1989
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NELL, LOUISE, BILLIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1943
- Already set (do not supply): none

### Source block (context only)

```text
Author: Katherine Snodgrass
ISBN: 978-0573632549
Publisher: Samuel French, Inc.
Date (Month/Year): 1989
```

### Introduction (context only: never use it for content warnings)

```text
A haiku is a short poem that expresses a single feeling or impression and typically contains three unrhymed lines of five, seven, and five syllables. In this selection, haikus becomes a bridge between a severely mentally handicapped daughter and her mother -- A way for Lulu to make a connection with reality and release the artist trapped inside her damaged mind. If only they can convince Lulu’s sister, Bebe, that it’s true. Haiku by Katherine Snodgrass
```

### Performance text (classify this)

```text
Scene opens with Louise rocking and flapping her hands. She is lost in her own mentally disabled word. Nell begins speaking . . . almost to herself rather than to Louise.

NELL: You were born in early winter. A breech baby. You tried to back into the world. I remember, the doctor had to pull you out. It was night when they finally brought you to me.

LOUISE: (still rocking and flapping – in a sing-song voice) November evening. / Blackbirds scull across the moon. / My breath warms my hands. (Nell write down Louise’s haiku, then check what she has written holding the paper two inches from her eyes)

NELL: John said you were too beautiful to live. It was true. You and Bebe together, you were like china dolls. Delicate, perfect. And then . . . I sensed it that day when I saw you through the window. Billie was on the swingset, and you were there. Outside. You were so quiet. You’d stared before, of course . . . as all children do. But this time, you were . . . different. I had to get down on my knees beside you. I touched your hair and then your face. . . Funny, I don’t remember being afraid.

LOUISE: (less rocking and flapping –sing-song voice is dying out to be replaced with a normal tone) Chainmetal swings clanging / In the empty schoolyard. / Silent summer rain. (Nell writes down this haiku and goes through the same process as before)

LOUISE: (in a normal voice – Louise is fully present) Tell me again about John. You haven’t talked about John in a long time.

NELL: John. All right then. John was tall and thin like Icabod Crane, only not so scared.

LOUISE: John wasn’t scared of anything. And [he] would rub Bebe’s back until she went to sleep. He smelled of soap and something . . . sweet?

NELL: (Drily) Sweet! Cigars. From Havana.

LOUISE: (retreating into her own world again as she repeats with Nell’s exact inflection – beginning to rock) Cigars. From Havana.

NELL: (Looks at her sharply) Let’s stop now. I think I should give you your medicine.

LOUISE: (struggles to stop rocking and maintain her connection - normal voice again) I’m not ready to go back. Please, not yet. I want to do more.

NELL: We’ve got to be careful.

LOUISE: (haltingly – she is clearly battling to maintain her clarity) But I can do it! I promise. Please, Momma, It’s like being smothered. Everything is so dim, and I can’t hear you properly. Or see you or touch you or . . . (Louise sees a bruise on Nell’s arm) Did I do that?

NELL: It’s not bad. (Nell touches the bandage on Louise’s forehead) Does this still hurt?

LOUISE: That was before, before I knew what to do. I can stop it, I know I can. I need to practice, you said so yourself. (beginning to rock and flap as she become more distressed)

NELL: Yes, I know what I said, but . . .

LOUISE: Let me see Bebe first.

NELL: Billie! My God, what time is it?

LOUISE: (Repeating) My God, what time is it? (Nell fishes in her pocket for a bottle of pills, urgently)

NELL: She’ll be here any minute. Sit quietly. You know we can’t wait too long. You’ll hurt yourself.

LOUISE: (sing-song voice) You’ll hurt yourself. (again pulls herself back) I mean no, I won’t and you promised I could talk to Bebe. You said I had to talk to her this time. That we could show her.

NELL: We will, we will. But she’ll be here any moment. (Holding out pills) I want you to take this now. (Louise retreats into her world and begins to rock and flap in ernest)

(Billie enters in a whirlwind)

BILLIE: Whew, I made it. (To Nell, ignoring Louise) How are you? You look exhausted. I knew you’d be surprised. Oh, and look what I found in a little shop in Boston. They had all three of your books, is that unbelievable? I brought something for Lulu, too. (Billing brings out a package from her bag and hands it to Nell.)

NELL: You did? Why, that was thoughtful. It’s wrapped so prettily, why don’t you let Lulu open it?

BILLIE: (Laughing nervously) Do we have time before dinner?

NELL: Billie.

BILLIE: I’m sorry. It’s just that she’ll like the wrapping paper better than the music box. (Crosses to Lulu) My God, what happened to her forehead? Is she banging her had again?

NELL: No, no, of course not. We just had a little accident.

BILLIE: Isn’t the medicine working? (Noticing Nell’s bruise) Did you get that bruise at the same time?

NELL: (Lying) Oh, this? This is nothing. I don’t even remember where it got it.

LOUISE: (Holding up her hands for a hug) Bebe.

BILLIE: God lord. Lulu, my love, you amaze me. (Louise and Billie hug)

NELL: She’s different than when you saw her last, isn’t she?

BILLIE: Because she hugged me? At least the medicine is doing that for her.

NELL: But don’t you think she’s really getting better thought? Honestly, look at her. Isn’t she more alert? She knew you, Billie. She wanted to touch you.

BILLIE: (Laughing) Mother. No! (to Louise) You never change, do you? (To Nell) No, I don’t see any difference, no, she’s not more alert, and no, she’s not getting any better.

NELL: You don’t understand. You can’t possibly know, you don’t see her every day. (long beat) I’m glad you’re here, Billie. I’m glad you came. I’ve been wanting to talk to you, but I haven’t had the courage until now. (silence, then frustrated) It’s my eyes.

BILLIE: Yes. That’s why I’m here. Doctor Dave called me. Don’t look so horrified. What did you expect him to do? Ignore it? (beat) What are we going to do? Will Daddy’s trust fund cover a nurse for Lulu?

NELL: No, and even if it would, I don’t want some stranger in my house caring for Lulu. I’ll do it myself.

BILLIE: How? How will you measure her medicine? What if she dirties her clothes? What if she has a reaction to the medicine? What if you were to fall, what would happen to Lulu? She couldn’t help you. She wouldn’t know what to do. Why, she wouldn’t even understand that anything was wrong.

NELL: I do not have to have someone here. I’ve managed this long. Besides . . . Lulu understands more than you know. Billie . . . I don’t write the haikus . . . Louise does . . .

BILLIE: That’s impossible

NELL: I swear it. It started two years ago. Right after we changed to that new medication. I was reading and Lulu was sitting next to the window and suddenly I realized that I’d forgotten to give her her pill. She turned to me and looked at me . . . really looked at me for the first time.

LOUISE: Mama? Do you forgive me Mama? Don’t mean to hurt you, but I get so scared as if . . . I get trapped, Mama. I try and I try, but I’m moving so slowly. I can’t tell you . . . (she gets stuck and there’s a growing panic to her voice and her demeanor – gradually increase of rocking and flailing) I can’t . . . I can’t . . . I can’t!

NELL: I had to give her her medicine then, but Louise had been there! She was so frightened. And then I remembered . . . The medicine . . . on that day it was late. So on the third day, again, I held back the pill, and again she was Louise!

BILLIE: This happened two years ago? Why didn’t you tell me? And the poetry?

NELL: It was October, just about dusk . . . I said to her “Concentrate, Lulu, you can stay if you want to. Look how beautiful the colors are . . (sing-song) Autumn evening:

LOUISE: (with same sing-song inflection - rocking) Autumn evening . . .

NELL: (sing-song) Woodsmoke

LOUISE: (imitate) Woodsmoke . .

NELL: (sing-song) Curling up wood . . .

LOUISE: (imitate) Curling up wood . . . (then finish without sing-song as the rocking and flapping ceases) swallows circle . . . . overhead.

NELL: She had finished it for me, you see. A Haiku. After that Lulu began making them up all on her own. Now I simply sit and talk and she creates. Billie, it’s as if she sees my thoughts, my innermost feelings, and then she translates them into images.

BILLIE: I thought they were yours.

NELL: I know you did. But no, I’m only the catalyst.

BILLIE: Catalyst. Is this every day? (Nell shakes her head) How long does it last?

NELL: Half an hour at the most. But she’s trying very hard. She wants to practice. She wants to be . . .

BILLIE: . . . Normal?

NELL: No. More than that. She wants to be extraordinary. And she is.

BILLIE: Mother, if this is true . . .

NELL: If . . . ?

BILLIE: I mean, when this happens . . . Why haven’t you told Dr. Dave about it?

NELL: No doctors and no more hospitals. They brought on this problem in the first place. If I hadn’t rushed her to the doctors so quickly, maybe she would have come out of it. If they didn’t have her taking all these drugs . . . Nobody knows what might have happened!

BILLIE: If that’s what you believe, take her off the drugs. We could put her in the hospital and have the drug levels monitored.

NELL: No. I told you, no hospitals.

BILLIE: But they could wean her off the drugs slowly, and then we could . . (Nell is shaking her head) Why not? Why not?

NELL: She needs the drugs. She’s not herself yet, so she needs them to . . . to protect her until . . .

BILLIE: What do you mean, protect her from what?

NELL: I told her you wouldn’t understand. I warned her, but she wanted me to tell you. She said we had to tell you.

BILLIE: I don’t believe it . . . .

(Flashback to BILLIE AND LULU as teens – Billie is teaching Louise about makeup.)

BILLIE: (To imaginary mirror) Now then, we need this, and this, and this. Okay, now you take the lipstick and you put in on like . . . that. See? Okay. Pucker up. (Billie puckers and Louise imitates her as Billie applies lipstick to Louise’s mouth then to her own) M-m-m-, luscious pink! Now then, you take this pencil. And don’t put it in your eye!

LOUISE: (Sing-song with lots of rocking and flapping) Don’t put it in your eye!

BILLIE: (To mirror, applying makeup to herself) You draw around the eye . . . underneath . . . above . . . but not too much. There. See?

LOUISE: (Sing-song with lots of rocking and flapping) Don’t put it in your eye!

BILLIE: Right. And now for the shadow. What color shall we use? Let’s use turquoise, or what about this purple? Yeah, let’s use the purple.

LOUISE: Yeah, let’s use the purple! (Billie puts it on for the mirror while Louise picks up turquoise and draws circles over her face, her cheeks and above her eyes).

BILLIE: Now, then, what’s next?

LOUISE: Now, then, what’s next? (Billie looks at Louise, whose face is covered with makeup) Oh, you!

NELL: (Enters) Billie, how could you! I thought you knew better than this. What were you thinking? Oh, Lulu, such a mess. It’ll take days for these colors to wear off. Why on earth? Here, hold her hands while I clean off this mess. For the final time, do not take it upon yourself to teach her. You leave that to me, or you can leave this house. Do you understand? (Billie runs off stage) I have no time to clean up after the both of you. Look at this, just look at it! Lulu, be still! Billie!

(End Flashback)

BILLIE: What do you want me to do?

NELL: I want for you, I need for you to write down the poems. To listen to her and believe in her so that she can be . . . who she is. The doctors don’t understand. The illness is still in control, so it’s only sheer will power that allows her to get out at all. If you don’t believe me, let me show you . . . . You can talk to her. We can help her, I know it. Louise? (There is no sign from Louise) Louise. (Louise still does not respond)

BILLIE: She doesn’t hear you.

NELL: Billie’s here, and you wanted to talk to her. Remember? (Nell turns Louise’s head toward Billie) You see? There. Now, Bebe, say something to her. Go on.

BILLIE: (Hesitantly) Lulu. It’s Billie.

LOUISE: Bebe.

BILLIE: Yes. Is it really you?

LOUISE: Is it really you?

BILLIE: I mean, is it true?

LOUISE: True?

BILLIE: (Trying again after looking at Nell for encouragement) It’s been a long time since I’ve seen you, Lulu. How . . . How are you?

LOUISE: How are you?

BILLIE: I’ve been fine, but how are you?

LOUISE: I’ve been fine.

BILLIE: (Giving up) She’s just repeating, Mother . . . No, no, say something else. Say anything else. Make up a poem. Can you do that for me, Lulu? Make up a poem. Please do that. (To Nell) What if I point out the window, will that help? (To Louise) Look, look out there. Winter’s nearly over. Mr. Turner’s daffodils are in bloom see?

NELL: Keep going, she’s listening.

BILLIE: One gray cloud lies just . . . over the trees across the southwest.

LOUISE: Over the trees one gray cloud lies . . .

BILLIE: She’s mimicking me.

LOUISE: . . . in my sister’s eyes.

NELL: There! Bravo, Lulu! Good girl! (Nell turns to Billie and sees her face) What.

BILLIE: She’s repeating. She says nursery rhymes with the same rhythm. She’s repeating what I say and what you say.

NELL: No. Louise? Help me now. We’ve got to make Bebe understand. Louise? Try just a little harder, baby. Concentrate now.

BILLIE: Please, please don’t! I’m asking you to stop.

NELL: Louise, answer me. Look at me and answer.

BILLIE: (Shouting) Mother stop! (Louise is startled by the shout and begins screaming and banging her head against her chair) Where is her medicine?

NELL: On the desk. Get the water. (Billie instead crosses to where she has put the music box and opens it for Louise to see. Louise immediately stops the banging and screaming and focuses on the music. Billie brings the pill and water glass to Nell) Now take this, Lulu. There. (Louise takes the pill calmly, fascinated with the music box).

BILLIE: Is this what always happens?

NELL: No, but sometimes we wait too long . . . I hate so to see her leave. (Beat) I know what you’re going to say. But every word I’ve told you is true. You heard it, but you didn’t want to believe.

BILLIE: That’s not true. I want to believe. Just don’t ask me to see something that isn’t’ there. Momma, I’m sorry, but I’ve tried before. I can’t keep trying and have it not be . . . not be true. It hurts too much. You talk to her as if . . .

NELL: . . . as if she’s real, as if she’s a person. And she is. Let me try tomorrow . . . I’m only asking you to let me try. Wait and see. You’ll do that, won’t you? Just that? For me?

BILLIE: (resigned and defeated) Yes, Momma. I think I can do that. (Billie crosses to the window and stands, looking out) I wish Daddy could be here. (Exits scene)

LOUISE: (alone on stage) Walking in his garden / Suddenly in the twilight / White hydrangea
```

---

## IC-0164: Handle With Care

- Title: Handle With Care
- Author (byline): Jodi Picoult
- Work: Not specified
- Publisher: Washington Square Press
- Publication date as stated: September 2009
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1859
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jodi Picoult
ISBN: 978-0743296427
Publisher: Washington Square Press
Date (Month/Year): September 2009
```

### Introduction (context only: never use it for content warnings)

```text
How far would you go to care for the ones you love? In the following selection, Willow O’Keefe is a little girl who has Type III osteogenesis imperfecta, also known as brittle bone syndrome. Her parents, Sean and Charlotte, have spent most of her life with sleepless nights, hospital bills, and stares from other parents who are luckier than they are. After going to Disney World, where Willow suffers a serious bone break, Sean and Charlotte decide to file a lawsuit against the park and the hospital, but it suddenly turns into a wrongful birth lawsuit against the OB/GYN who treated Charlotte during her pregnancy. The parents must testify that if they knew before birth that Willow had this disease, they would have aborted her. Told through the eyes of Charlotte, Willow’s mother; and Amelia, Willow’s sister, the trial takes a toll on their entire family. Handle With Care by Jodi Picoult.
```

### Performance text (classify this)

```text
Charlotte (Mom): (Pg 403) The movie that had been filmed to show a day in your life was the last bit of evidence that Marin would offer to the jury. It was the emotional counterpart to the cold, hard facts the actuary had given, about what it costs in this country to have a disabled child.

It began with an image of your face, reflected in the windowpane you were peering through. You weren’t speaking, but you didn’t have to. There was a lifetime of longing in your eyes.

The view panned out the window, then, to watch your sister skating on the pond.

Amelia (Sister): (Pg 17) I [can] imagine our parents saying, There Amelia goes, being difficult again.

(Pg 18-19) Pick ten strangers and stick them in a room, and ask them which one of us they feel sorrier for – you or me – and we all know who they’ll choose. It’s kind of hard to look past your casts; and the fact that you’re the size of a two-year-old, even though you’re five. I’m not saying that you’ve had it easy. It’s just that I have it worse, because every time I think my life sucks, I look at you and hate myself even more for thinking my life sucks in the first place. Here’s a snapshot of what it’s like to be me: Amelia, don’t jump on the bed, you’ll hurt Willow. Amelia, how many times have I told you not to leave your socks on the floor, because Willow could trip over them? Amelia, turn off the TV (although I’ve only watched a half hour, and you’ve been staring at it like a zombie for five hours straight). I know how selfish this makes me sound, but then again, knowing something’s true doesn’t keep you from feeling it. Charlotte (Mom): [The lawyer continued talking to Sean and me.]

Marin (Attorney): (Pg 64) I know how horrible this sounds. But the term wrongful birth is just a legal one. We don’t wish your child wasn’t born. We just think that, when a doctor doesn’t meet the standard of care a patient deserves, someone ought to be held responsible. Think of all the time and money that’s gone into taking care of Willow – and will go into taking care of her in the future. Why should you pay for someone else’s mistake? Charlotte (Mom): (Pg 60) What if it was someone’s fault?

For five years now I had loved you, hovered over you, held you when you had a break. So how could I admit to anyone – much less myself- that you were not only the most wonderful thing that had ever happened to me . . . but also the most exhausting, the most overwhelming?

Marin (Attorney): (Pg 91) If you file this lawsuit, you have to be able to swear – under oath – that if you’d known about your daughter’s illness earlier, if you’d been given the choice, you would have terminated the pregnancy. Is that going to be a problem?

Charlotte (Mom): Can you miss a person you’ve never known? Amelia (Sister): (Pg 121) The last time my parents had been fighting – which was, like, yesterday – you and I were in our bedroom, and we could hear them loud and clear. Words slipped under the door, even though it was closed: wrongful birth… testimony… deposition. At one point I heard the mention of television: Don’t you think reporters would get wind of this? Is that what you really want? and for a moment I thought how cool it would be to be on the news, until I remembered that being a poster child for dysfunctional family life wasn’t really how I wanted to spend my fifteen minutes of fame. They’re mad at me, you said. No. They’re mad at each other. Then we both heard Dad say, Do you really think Willow wouldn’t figure this out? You looked at me. Figure what out?

Charlotte (Mom): (Pg 71) Sean was the risk taker when it came to you. Then again, he wasn’t the one who was home most often when you had a break. Maybe I could convince him that two silly words like wrongful birth meant nothing when compared to the future they might secure for you. (Pg 104) It’s because we want her, because we love her, that I’d ever think about this in the first place. I’m not stupid, Sean. I know people are going to talk, and say I’m after a big settlement. They’re going to think I’m the worst mother in the world, the most selfish. But I don’t care what they say about me – I care about Willow. I want to know that she’ll be able to go to college and live on her own and do everything she dreams of. Does it really matter what everyone else says if I know why I’m doing it?”

Willow: (Pg 193) (whispering) You know how Mom always says that I can be anything when I grow up? That’s a lie.

Amelia: Why?

Willow: I couldn’t be a boy. And I couldn’t be Miss America.

Amelia: How come?

Willow: You can’t wear leg braces in a pageant.
Amelia: (to audience) I thought about those pageants, girls too beautiful to be real,
tall and thin and plastic-perfect. And then I thought of you, short and
stubby and twisted, like a root growing wrong from the trunk of a tree,
with a banner draped across your chest.
MISS UNDERSTOOD.
MISS INFORMED.
MISS TAKE.
That made my stomach hurt.

Charlotte (Mom): [This is what I tell the jury.] (Pg 359-360) I know what I look like to all of you. I know you think I’m in this for a big payday, that this is why I started this lawsuit.

It is about cost. But not the financial kind. I don’t sleep at night. (blinking back tears) I don’t sleep at night. I feel guilty when I laugh at a joke on TV. I watch little girls the same age as Willow at the playground, and I hate them sometimes – that’s how bitterly jealous I can get when I see how easy it is for them.

I made a promise to my daughter – I said, If you fight, I will, too. If you live, I will make sure your life is the best it can possibly be. That’s what a good mother does, right? (Shakes her head) The way it usually works, the parent takes care of the child, until years later, when the roles are reversed. But with Willow and me, I’ll always be the one taking care of her. That’s why I’m here today. That’s what I want you to tell me. How am I supposed to take care of my daughter after I’m gone?

Willow: (Pg 320-321) (wiping tears from her eyes) Mom wants to get rid of me because [I keep breaking]. I’m not the kind of kid anyone wants.

Amelia: What are you talking about? It’s not like you’re a serial killer. You don’t torture chipmunks or do anything revolting, except try to burp ‘God Bless America’ at the dinner table-

Willow: I only did that once. But think about it, Amelia. Nobody keeps things that get broken. Sooner or later, they get thrown away.

Amelia: Willow, you are not being sent off, believe me. And if you are, I’ll run away with you first.

Charlotte (Mom): (Pg 442) [Amelia] asked me not too long ago what the world would be like without Willow in it. So here’s what I think: if Willow had never been born, I’d still look for her in the aisles of the grocery store, or at the bank, or in the bowling alley. I’d stare at every individual face in a crowd, trying to find hers. There’s this weird part about having kids – you know when your family is finished, and when it’s not. If Willow hadn’t been born, that’s how the world would be for me – unfinished.

Amelia (Sister): (Pg 455) We all protected you, in our own ways. Dad blustered around, angry at anything that made life harder for you. Mom, well, she was apparently stupid enough to gamble everything in order to get more for you in the long run. And me, I guess I just lacquered a shell around myself, so that when you got hurt, it was easier to pretend I didn’t feel it, too. Charlotte (Mother): [The day the jury reached its verdict, I told] (Pg 465) you that this was finally over. I [told] you that you’d have everything you needed, for the rest of your life – and after mine ended. I [told] you that I had won, and that the verdict award[ed] damages in the amount of eight million dollars.

Willow: (Pg 469) Eight million is the number of dollars written on the big blue check that has been on our refrigerator for almost six months now. (Pg 471) My parents had never cashed the check. A lot of zeros didn’t mean anything really, except security – my parents could splurge a little, because if their funds ran out, there was a backup.

Charlotte (Mom): Tell you wat. Go get Amelia and we’ll figure out a plan of action. A movie, maybe. Be . . .

Willow: . . . careful. Yeah, I know. It was March, but still cold enough the ground still crunched under the soles of my boots. Amelia was probably in the woods . . . I hesitated as I came to the edge of the pond. (Pg 472) Right now, for the first time in months, I had no healing fractures, and I planned to keep it that way.

I’d never been allowed on the ice, and like most things that you aren’t allowed to do, it was all I thought about. I got down carefully on my hands and knees, and inched forward. I couldn’t get hurt this way.

[Then] there was a moan rippled across the surface of the pond. Suddenly, all around me, the ice became a spiderweb and I was the bug stuck at its center. As the water filled my nose and mouth, I closed my eyes and curled my fists around the things I knew for sure: That I was loved and that this time, it was not me who broke.

Charlotte (Mom): (Pg 475) For a long time, I could only see you sinking. I pictured you, with your skin pale blue and your hair streaming out behind you like a mermaid’s. I would wake up screaming, beating the mattress with my hands, as if I could reach through the ice and drag you to safety. . . I do not have the money anymore. It was yours, after all. I slipped the check into the silk lining of the coffin when I kissed you good-bye for the last time.

But that wasn’t you, no more than the skeleton you’d been given was you. You were more than that, lighter. You were the steam that fogged the mirror in the morning when Sean dragged me out of bed and forced me to take a shower. You were the crystals painting my car windshield after a night’s frost. You were the heat rising off the pavement like a ghost in the middle of the summer. You never left me. Here are the things I know for sure:

• When you think you’re right, you are most likely wrong.

• Things that break – be they bones, hearts, or promises – can be put back together but will never really be whole.

• And, in spite of what I said, you can miss a person you’ve never known.

• I learn this over and over again, every day I spend without you.
```

---

## IC-0165: Handler from Talking With

- Title: Handler from Talking With
- Author (byline): Jane Martin
- Work: Talking With
- Publisher: Samuel French, Inc.
- Publication date as stated: Feb 2011
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CARO
- Teaser before the introduction: No
- Spoken words (computed): 1165
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Martin
Book: Talking With
ISBN: 978-0573630217
Publisher: Samuel French, Inc.
Date (Month/Year): Feb 2011
```

### Introduction (context only: never use it for content warnings)

```text
"And these signs shall follow them that believe; In my name shall they cast out devils; they shall speak with new tongues; They shall take up serpents; and if they drink any deadly thing, it shall not hurt them; they shall lay hands on the sick, and they shall recover," —Mark 16:17-18

To outsiders, mainstream Christians included, snake handling seems foolhardy at best and deadly at worst. And despite commending their desire to be obedient to Scripture, Christians have argued that snake handlers are wrong to take Jesus' words in Mark 16:17-18 literally. His statement, they argue, is not a commandment and, what's more, intentionally putting oneself in danger is tantamount to tempting God.

In Handler from the play Talking With, Jane Martin brings to the stage a young girl who devoutly believes in the Penacostal religion that deifies the act of snake handling. Handler by Jane Martin
```

### Performance text (classify this)

```text
A young woman in a simple, country-print dress. On the floor before her is a handmade wooden box about two feet long and eighteen inches high with a sliding wire screen top.

CARO: My Dada* was gonna do this tonight but the Lord froze his face so he sent me. I learned this from my Dada and he learned it up from great Gran, who took it on from the Reverend Soloman Bracewood, who had him a mule ministry 'round these parts way back when. Dada taught Miss Ellie, my rna, and my brother Jamie ... he was in it too, 'fore he went for Detroit.

See, what I got in here is snakes. Lotta people don't like snakes. Gives it its nature, I guess. This here is water mocs. Jamie, he said they got the dirtiest, nastiest bite of all ... well, rattlers is yer biggest. Lotta venom. You milk you a rattler, you can half fill up a juice glass. Dada said Jamie should do rattlers, but he never. Did 'heads, copperheads. Now they're slower and safer but it ain't such a good show. You know those dang snakes smell like cucumbers? Well, they do. Miss Ellie, she favored mocassins. Dada too ... well, Dada he did all kinds, all ways. Your mocassin now, he's your good 01' boy snake. Flat out mean an' lots of get up n' go. Heck, they'll chase ya. They will. 01' Dada he didn't like Miss Ellie doin' 'em. 'You layoff them mocs 'fore they lay you down.' Made Miss Ellie laugh. Lotta handlers think mocassins are slimy. Couldn't get me to touch one. They'll do rattlers ... got him a nice dry feel. Little bit sandpapery. Rattler can find ya in the pitch dark though. They git on to yer body heat. Snake handlin'. All my blood does it. Only Dada an' me now though. Snake handlin', with the Holiness Church. Down where I come from we take God pretty serious. If you got the spirit, snake don't bite. If he bites you, you know you ain't got the spirit. Makes the difference real clear, don't it?

It's right there in the scripture ... Mark, Chapter 16, verses 17 and 18, 'And these signs shall follow them that believe. In my name they shall cast out devils; they shall speak in new tongues; they shall take up serpents; and if they shall drink any deadly thing, it shall not hurt them; they shall lay hands on the sick and they shall recover.' Don't figure it could be much clearer than that. There's some churches don't use snakes, use strychnine, powdered poison, same idea though. They mix it with Cherry kool-ade, sing 'em a hymrn , drink it off, and then just stand around waitin' to see if they fall over. Ain't much of a show. Not like snakes. Dada does fire but I can't do it. Pours some kerosene in a coke bottle, sticks a rag in the top and lights it up. Holds that fire under his chin, passes it down the arm, puts his hand in it, you know, that kind of stuff. He says there's people do blow torches down to Tennessee. I don't know. Jamie give it a try 'fore he went to Detroit. Just about burned his ass off. Sorry.

When I handle, I keep 'em in this box. Dada gimme this and some Heidi doll on my ninth birthday. Sometimes I'll just open up the lid and put my foot in or, uh, maybe stick it open side to my chest. There's some lay it to their face. I don't. Scares my eyes. Durin' service we take 'em right out, pass 'em around. It's more dangerous than a single handler. Snake gets to comparin' who got the spirit a whole lot an' who jes got it some. Somebody's jes about bound to come in second. Don't get me wrong now. Y' don't die every time yer bit. I been bit seven times. Four times by the same serpent. Dada says he got the sweet tooth for me. Dada been bit thirty-two times an' never saw him a doctor. Used to let me kiss him on the marks. Last one got him here. (Points to eye.) Froze him right up. Dada says he'll thaw but I don't know.

Day after Jamie took off Miss Ellie did mocassins standin' in the back of the pickup over to Hard Burley. Shouldn't ought to 'cause her mind weren't there. Coal truck backfired and she got bit. Snake bit her three more times 'fore she hit the ground. Dada layed hands on her but she died anyway. There was ten of us handled right there at the funeral. Snake handlin'.

Snake knows what you feel. You can fool a person but you can't fool a snake. You got the spirit, God locks their jaws. Keeps you safe. Tell you what though ... I don't believe in a God. Left me. Gone with Miss Ellie. I was handlin' when I knew it sure. Snake was jes comin' on down the line. Marita she yells out, 'The Lord. Lord's in me and with me. In me and with me.' Noah he was ululatin', talkin' in tongues. Couple of folks was rollin' and singing. Dada was doin' switch grips. Had Miss Ellie's weddin' ring on his little finger. And it came on me, heck, there ain't no God in here. There's just a bunch of shouters gettin' tranced. There ain't no God in here at all. 'Bout that time they layed that serpent to me. Felt fussy.

Nasty. Just lookin' for an excuse y'know? An' I was an empty vessel, worse nor a pharasee, grist for the mill. My blood went so cold I coulda crapped ice-cubes. Snake knew. Started to get leverage. So I said, 'Snake. You Satan' hand-maiden. You're right, there ain't no God in me. I'm just a woman, but I'm the only woman in my Dada's house and he needs me home. Outta his faith and his need, you lock yer jaws.' I let that snake feel a child's pure love and it sponged it up offa my hands and then 01' wiggley went limp. I tranced it. It was a real good service. Didn't nobody handlin' get bit. (Takes snake out of the box.) Yes, you got to believe. Holiness Church is dead right about that. Makes me wonder, you know? I git to lookin' at people and wonderin' if they got anything in 'em could lock a serpent's jaws. Any power or spirit or love or whatever. I look at 'em and I wonder, could they handle? Tell you what though, you can see it in a face. You can read it. You look me full in the face it don't take me 30 seconds. It's like I was the snake, some 01' pit viper, an' I can read yer heart. Maybe you could handle and maybe you can't, but there's but one sure thing in this world .. yer empty, yer gonna get bit.
```

---

## IC-0166: Hannah’s Gift

- Title: Hannah’s Gift
- Author (byline): Maria Housden
- Work: Not specified
- Publisher: Bantam Books
- Publication date as stated: July 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MARIA, HANNAH, DOCTOR, CINDERELLA, SOCIAL WORKER, CHILD
- Teaser before the introduction: Yes
- Spoken words (computed): 1263
- Already set (do not supply): none

### Source block (context only)

```text
Author: Maria Housden
ISBN: 978-0553381221
Publisher: Bantam Books
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
According to St. Baldrick’s Foundation, one in 285 children in the United States will be diagnosed with cancer before age 20. These children are true gifts. They have no interest in being victims. They change the lives of everyone they touch with their bravery, strength, compassion, optimism, and willpower. This is . . .

Hannah’s Gift by Maria Housden
```

### Performance text (classify this)

```text
MARIA: (Prologue) Looking back, I realize that my whole life pivots around a single moment: The Red Shoes. I was standing in a Stride-Rite children’s shoe store. Black or blue leather would coordinate with every outfit in Hannah’s preschool wardrobe. [But] Hannah had already decided . . . [she was] holding up a pair of red patent leather Mary Janes.

HANNAH: These are my shoes! (slipping her feet into the shoes)

MARIA: (smiling patiently) Those are lovely, but we need to buy something practical that will match the dresses in your closet.

HANNAH: But Mommy, red shoes go with everything. Besides . . . they fit me just perfect!!! (whispering) Just like Cinderella!

MARIA: Closing her eyes and extending her arms, Hannah began to dance, oblivious to everything but the shoes on her feet. (Beat) (Beyond Fear) The two of us were crossing the parking lot. Her red shoes tapped on the pavement as she walked beside me.

HANNAH: Mommy, do children ever die?

MARIA: I paused before answering. I wished I could tell her that children didn’t die. But I knew that wasn’t the truth, and I knew Hannah knew it too. (to Hannah) Yes, Hannah, sometimes children die.

MARIA: (Light in the Shadow) [It began] during our vacation in Michigan. We had taken Hannah to an emergency room. She had been complaining that it hurt to lie down. The doctor told us she had the flu and sent us away with Children’s Tylenol. Two days later, we took her to another hospital. The pediatrician tried to examine her abdomen but she screamed and refused to lie down and the doctor gave up, obviously exasperated.

DOCTOR: There’s nothing wrong with her; she’s just manipulating you. She has too much energy to be really sick. As far as I can see, she’s fine.

MARIA: Every bone in my body was telling me something was wrong, and yet, perhaps the doctor was right. Maybe I was just the inadequate mother of an overindulged child. (Beat) Now, [a third] doctor . . . He came into the room, flipped the switch on the light board, and slid the film under the clip. [There was] a large, dark shadow beneath the white outline of Hannah’s ribs. I felt like a profound failure.

DOCTOR: (A Deeper Silence) It’s called a Rhabdoid tumor of the kidney. It’s malignant, aggressive and rare.

MARIA: (Truth: A Special Medicine) The weight of the moment crushed against my chest. (to Hannah) Hannah, the doctors have figured out why you are feeling so sick. There is a lump in your tummy called a tumor. The doctors are going to take it out, and then give you medicines to try to make sure the bad cells don’t come back. (Beat) (Magic) A week after Hannah’s second surgery, and as a Make-A-Wish kid, Hannah qualified for an all-expenses-paid trip to Walt Disney World. Hannah performed two somersaults in the middle of the floor to celebrate. Cinderella’s castle was our first stop.

CINDERELLA: Hello, I’m Cinderella. What’s your name?

HANNAH: (in awe) My name’s Hannah. (quietly) I just had surgery. Do you want to see my scar? (She raises her dress)

CINDERELLA: (looking at Hanna’s scar, she then opens her arms wide to hug the little girl) Thank you for sharing that with me, Hannah.

MARIA: As she held Hannah, she looked at me, her eyes full of tears. It didn’t matter that Cinderella was a girl from Iowa. The joy we experienced in the meeting was real, and that was magic enough for me. (Beat) (Anticipation) Since the day Dr. Kamalaker told us Hannah had cancer, I had begun living the paradox of wanting to do anything to find a cure and needing to preserve the quality of time Hannah had left. I agreed to try the chemotherapy protocol once a week at the outpatient clinic.

SOCIAL WORKER: You realize that chemotherapy will severely compromise Hannah’s immune system. Preschool is definitely out of the question.

MARIA: I knew it was true. But to me, Hannah was a three-year-old first, and a caner patient second. (to the Social Worker) You don’t understand. After everything Hannah’s been through, I won’t take preschool away from her. She wants to ride on a bus and go on field trips with her friends. I’m willing to do anything to make that happen. (to audience) Hannah started preschool the week after her third birthday. (Nurse Katie and the Tea Party) Her friends exclaimed over her dress [and red shoes] and hardly seemed to notice the paper hospital mask or her lack of hair. (Beat) (Hannah’s Birthday) Soon it was Hanna’s birthday. When I asked how she wanted to celebrate the day she said:

HANNAH: I want a party with a Little Mermaid cake, not too much people and not too much gifts!

MARIA: The children had greeted Hannah shyly, tentatively. It was clear they had been reminded just before coming that Hannah had had surgery [again] and might still feel sick. Hannah had been the one to step into the moment and set us all straight.

HANNAH: Hey, you guys, do you want to see my scar? It’s just surgery! (she lifts the hem of her dress and, exclaims enthusiastically) My doctors gave me medicine and pizza!

CHILD: Ooooo . . . Ahhh . . . Wow! I want to have surgery! (pause) Can you still play?

HANNAH: Of course, you silly. This is a party, isn’t it?

MARIA: One of the mothers turned to me and whispered, “Is this okay with you?” And I smiled and shrugged. If it’s okay with her, it’s okay with me. (long beat) (Say Yes) [But] Less than a week after Easter, Dr. Kamalaker slid a piece of film under the clip of a lightboard and pointed to the spot where the cancer had metastasized. In a different place this time. Very close to Hannah’s spinal cord and wrapped around some very important veins. The doctors can’t take this one out. (On the Threshold) As Hannah’s tumor grew, so did the amount of morphine she required.

HANNAH: Mommy, I want you to carry me to my room

MARIA: It was the first time in days she had asked to go anywhere other than the bathroom.

HANNAH: Don’t put me down and don’t go it. I just want to look.

MARIA: The two of us stood on the threshold, watching dust dance in the late afternoon sun. The magic wand she had made at her birthday party almost a year ago lay in the middle of the floor. I wanted to wave it through the hush and bring everything back to life. (beat) I knew Hannah was saying good-bye, but I wasn’t ready. This room with its Barbie dolls and red patent leather shoes was Hannah. If I were to say good-bye to this, what part of her would be left? (long beat) (Everywhere I Am, There You’ll Be) Hannah hadn’t eaten more than a bite or two of solid food for almost a week. I was sitting at the foot of the bed, early in the day, when Hanna stirred and sat up slowly.

HANNAH: (wincing then smiling) Mommy, do you know that even if I go to Heaven, I’m going to come back? (deep moan of pain)

MARIA: Yes, Hannah, I know.

HANNAH: (deep moan of pain)

MARIA: (Silence) I jumped up, checking the morphine pump to make sure nothing had malfunctioned. Something had drastically changed. I decided to pick her up, not knowing what else to do. Hannah’s body continued to fight for twenty minutes, but some part of her already felt free. One moment she was alive and breathing; the next, she wasn’t. (beat) (Prologue) The truest measure of a life is not its length, but the fullness in which it is lived. (Everywhere I Am, There You’ll Be) In that instant I knew that, no matter what happened, there was a part of Hannah that would always be with me, something of her that would never die. It wasn’t a belief. It wasn’t a hope.

It was a knowing beyond the workings of my mind. (beat) I closed my eyes for a moment. And there, behind my eyelids, I saw something I could hardly believe: It was Hannah . . . radiant . . . laughing (Prologue) in red patent leather shoes. Closing her eyes and extending her arms, Hannah began to dance. May her story offer solace to those who suffer and inspiration to those who want the courage to live their own truth.
```

---

## IC-0167: Harriet

- Title: Harriet
- Author (byline): Elena Passarello
- Work: Animals Strike Curious Poses, Pgs 85-94
- Publisher: Sarabande Books
- Publication date as stated: Feb 2017
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: HARRIET, FITZROY, CHARLIE, DICK, TOM, JOHN, GEORGE, FLEAY, STEVE IRWIN
- Teaser before the introduction: Yes
- Spoken words (computed): 1221
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

You finally land in England a year later. Boxes of corpses – birds, plants, bugs, rocks – pass through his study. No tortoises. You were the only one he thought to keep, the remains of the others heaved overboard with the slop.

But that fall, in the draftiest room of the British Museum, you’ll find yourself shivering on a table with three other girls your age. All from the Beagle, four secrets stashed away in the gentlemen’s cabins. Even godly Captain FitzRoy had a Galapagos on the sly.

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

STEVE IRWIN: (posing for pictures with Harriet) Crikey! (a different pose) Crikey!

HARRIET: He holds a few poses for the crowd and their flashing eyeballs, hugging your neck, straddling you with outstretched arms and mouth open wide.

STEVE IRWIN: (singing) Happy birthday, dear Harry-ette!

HARRIET: At the edge of the pen, his long-haired wife grits her teeth. He skips over to the “Croco-seum” for an impromptu reptile freak-out. Watch him bound onto the stage, a baby croc in each hand, shaking them like maracas in the dusty breeze. Irwin tosses you a few pink flowers and the grimacing wife cuts a huge cake. She slices through your name as well as your age – the cause for all this celebrating. The number in icing read 1 – 7 – 5.
```

---

## IC-0168: Having Our Say: The Delaney Sisters’ First 100 Years

- Title: Having Our Say: The Delaney Sisters’ First 100 Years
- Author (byline): Emily Mann
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: May 1997
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SADIE, BESSIE, BESSIE AND SADIE
- Teaser before the introduction: Yes
- Spoken words (computed): 2731
- Already set (do not supply): none

### Source block (context only)

```text
Author: Emily Mann
ISBN: 978-0822215028
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): May 1997
```

### Introduction (context only: never use it for content warnings)

```text
Having Our Say: The Delaney Sisters’ First 100 Years by Emily Mann
```

### Performance text (classify this)

```text
Lights come up slowly on Sadie Delany. She stands straight and tall, addressing the audience.

SADIE: Bessie and I have been together since time began, or so it seems. Bessie is my little sister, only she's not so little. She is 101 years old, and I am 103. (Bessie enters.) You know, neither one of us ever married and we've lived together most all of our lives, and probably know each other better than any two human beings on this Earth. After so long, we are in some ways like one person.

BESSIE: How do you do! I'm Dr. Delany. Make yourself comfortable. Stay as long as you like. We won't charge you rent. (Bessie looks to the audience, eyes fiercely penetrating. They both laugh uproariously) Truth is, I never thought I'd see the day when people would be interested in what two old Negro women have to say. Life still surprises me. So maybe the last laugh is on me.

SADIE: You know, Bessie and I were in helping professions - she was a dentist and I was a high school teacher -

BESSIE: so we're not rich, but we get by.

SADIE: Papa always taught us that with every dollar you earn, the first ten cents goes to the Lord . . . The second ten cents -

BESSIE: . . . goes in the bank for hard times . . .

SADIE: And the rest is yours, but you better spend it wisely. Well, it's a good thing we listened because we're living on that

BESSIE and SADIE: (Together.) hard-time money now,

SADIE: and not doing too badly. We have lived in New York for the last seventy-five years, but Raleigh

BESSIE and SADIE: (Together.) will always be home.

BESSIE: Raleigh is where Mama and Papa met, as students at Saint Augustine's School,

SADIE: which was a school for Negroes. They got married in the campus chapel and raised all ten of us children right there at -

BESSIE and SADIE: (Together.) good old "Saint Aug's."

BESSIE: Papa became vice-principal and Mama was the matron, which meant she ran things day-to-day at the school. Our Papa became the first elected Negro bishop of the Episcopal Church, U.S.A.

SADIE: That's a long way for a man who was born a slave on a Georgia plantation, but if you had known Papa, you wouldn't be surprised. He was always improving himself, and he and Mama brought us up to

BESSIE and SADIE: (Together.) reach high.

SADIE: Bessie was what we used to call a "feeling child"; she was sensitive and emotional. She was quick to anger, and very outspoken.

BESSIE: And Sadie was a "mama's child."

SADIE: Yes, I followed my Mama around like a shadow. I always did what I was told. I was calm and agreeable.

BESSIE: She was shy.

SADIE: The way I see it, there's room in the world for both me and Bessie We kind of balance each other out. People learned not to mess with me from Day One.

SADIE: It's a wonder she wasn't lynched.

BESSIE: Well, I almost was, but that's another story. The thing is I know Sadie's going to get into Heaven, but I'm not so sure about me. I'm working on it, but it sure is hard to change.

SADIE: She has trouble with the idea of forgiving and forgetting.

BESSIE: That's right. You see, I can forgive, but I can't seem to forget. And I'm not sure the Lord would approve of that at all. I remember things that happened long, long ago that still make me madder than a hornet. I wish they didn't. Most of the people I'm still mad at are long dead and there are things I can tell you . . . (She stops herself) but Sadie will say, "Now Bessie, of the dead -

BESSIE and SADIE: (Together.) . . . say nothing Evil."

BESSIE: So . . . I try to be good. But the rebby boys tend to stand out, make themselves known. You don't know what a rebby boy is.

SADIE: That's what we call white racist men. It's short for rebel.

BESSIE: I'll tell you, the way those rebby types treat colored folks - well, it just makes me sick. Those rebby types don't give colored folks credit for a thing. They learn early to hate. Why, colored folks built this country, and that is the truth. We were the laborers, honey! We were the backbone of this country (She stops herself) Now, Sadie doesn't get all agitated like this. It's been a little harder for me, partly because I'm darker than she is, and the darker you are, honey, the harder it is. I wish I were more like her but I'm afraid I am a naughty little darky! Ha hal (Bessie laughs.) I know it's not fashionable to use some of the words from our heyday, but that's who I am! And who is going to stop me? Nobody, that's who! Ain't nobody going to censor me, no sir! I'm a hundred-and-one years old and at my age, honey, I can say what I want! The beginning of Jim Crow in North Carolina was the day that everything Changed.

SADIE: We already knew we were second-class citizens but those Jim Crow laws set it in stone.

BESSIE: At that time, many white people didn't think Negroes had souls. They wanted to believe that.

SADIE: And powerful white people were getting more and more nervous with the way colored people, after the Civil War, were beginning to get their piece of the pie.

BESSIE: The pecking order was like this: white men were the most powerful, followed by white women.

SADIE: Colored people were absolutely below them

BESSIE: and if you think it was hard for colored men, honey, colored women were on the bottom. Yes, sir! Colored women took it from all angles! We encountered Jim Crow laws for the first time on a summer Sunday afternoon.

SADIE: We were about five and seven years old at the time. There was a place in Raleigh not just for whites but for the whole city, called Pullen Park. The spring where you got water had a big wooden sign across the middle. (They gesture with their hands.)

BESSIE: On one side, the word "white" was painted,

SADIE: and on the other, the word "colored." What in the world was all this about?

BESSIE: We may have been little children but, honey, we got the message loud and clear.

SADIE: (Laughing.) But when nobody was looking, Bessie took the tin dipper and leaned over and scooped some water from the other side and said, "I'm goin' get me some white water!"

BESSIE: It tasted just the same. (They laugh. A beat.)

SADIE: Yes it did, but I'll tell you how I handled Jim Crow. There was a shoe store in Raleigh called Heller's. The owner was a Jewish man, very nice. If you were colored, you had to go in the back to try on shoes, and the white people sat in the front. It wasn't Mr. Heller's fault; this was the Jim Crow law. I would go in there and say, "Good morning, Mr. Heller, I would like to try on those shoes in the window." And he would say, 'That's fine, Miss Delany, go on and sit in the back." And I would say, "Where, Mr. Heller?" And he would say, "Back there." And I would say, "Back where?" Well, I'd just worry that man to death. Finally, he'd say, 'Just sit anywhere, Miss Delany!" And so I would sit myself down in the white section, and smile.

BESSIE: Lord! I hate when you play dumb like that! (Sadie laughs) Every time I encountered prejudice which was rubbed in my face under Jim Crow - I would feel it down to my core. (Very upset.) The words used to describe us most often were colored, Negro, black, and nigger. I've also been called jiggerboo, pickaninny, coon - you name it, honey. Some of these words are worse than others, and how mean they are depends on who is saying them and why. Personally, I don't use the word black very often to describe myself and my sister. To us, black was a person who was, well, black, and honey, I mean black as your shoe. I'm not black, I'm brown! Actually, the best word to describe me, I think, is colored. I am a colored woman or a Negro woman. Either one is OK. People dislike those words now. Today they use this term African American. It wouldn't occur to us to use that. We prefer to think of ourselves as Americans, that's all!

SADIE: There was an attitude among some Negroes that to be lighter-skinned was more desirable. But it was not something that was even discussed in our household. We were different shades, and it didn't make a bit of difference if you were white, black,

BESSIE and SADIE: (Together.) grizzly, or gray, you were you.

SADIE: Now Mama and Papa tried to protect us when we were small, but we were quite young when we learned colored folks were being murdered.

BESSIE: They were being lynched.

SADIE: Yes - we would hear the teachers talking among themselves about some poor Negro just walking down the side of the road, in the wrong place, at the wrong time.

BESSIE: Those rebby boys would just grab him and hang him from a tree, just for fun.

SADIE: It was like entertainment to those fellas.

BESSIE: The rebby boys would come in the middle of the night, and get him out of his bed and hang him up, in front of his wife and children. Sometimes they'd hang his whole family. Why, there was one story we heard of a pregnant colored woman who was hung from her feet, and they slit her abdomen open and let the fetus fall out -

SADIE: (Quietly overlaps Bessie) Lord have mercy!

BESSIE: and she and her unborn baby just died right there, like that.

SADIE: I don't understand any of this. I sometimes think maybe we were a little too sheltered. Why, I was almost afraid of men, really. I wasn't allowed to go downtown by myself until I was a grown girl and then I was always kind of jittery. You can imagine that when it came time for me to graduate from Saint Aug's, I didn't want to leave. The campus was the only home I'd ever known. But on graduation day, Papa said to me, "Daughter, you are college material. You owe it to your nation, your race, and yourself to go. And if you don't, then shame on you!" Well, it seemed to me that I had no choice but to go on with my schooling. But Papa said to me, to both of us, "Daughters, I have no money, and you mustn't take a scholarship. If you take a scholarship, you will be beholden to the people who gave you the money. You must make your own way." So I started looking for teaching jobs.

BESSIE: When we were teaching, we saw for the first time what life was really like for our people.

SADIE: Yes, Lord.

BESSIE: It made our hearts bleed.

SADIE: I realized I was a child of privilege and I had to share my good fortune. I kept remembering what Papa always said: ''Your mission . . . "

BESSIE and SADIE: (Together.) “. . . is to help somebody."

SADIE: Yes, those words kept me going.

BESSIE: This was just forty-five years after the Surrender, and most of these Negroes were in bad shape, honey. They needed help with the basics.

SADIE: You see, oftentimes, learning to read and write for the children was not the top priority. Teaching people about food preparation - like how to can food - was more important.

BESSIE: A lot of the time what those folks needed was inspiration.

SADIE: Yes, a little encouragement. That goes a long way.

BESSIE: I remember when I left home to teach. I was twenty years old. I'd never been away from home. Papa took me to the train station in Raleigh and I put on a brave front. But when that train pulled away from the station and I looked back and saw my Papa standing there, watching me, I thought I was going to die. I started to sob. I cried so hard that the people from the white car came to the colored car to get a look at this little darky just carrying on! Well, I'm embarrassed to say I created quite a commotion. The conductor came along and said, "What's the matter, did somebody die?" Now what'd he have to go and say that for? It was my girlhood that was dying and I knew it.

SADIE: Well it turned out you were the most exciting thing to happen to Boardman, North Carolina, in about a hundred years. Child, they'd never seen the likes of her! She'd walk through that town and the colored men would just stop and stare. They wouldn't say a word, they'd just take off their hats when she walked by.

BESSIE: (Laughs.) One time, I turned and said, 'Just what are you looking at?" They didn't answer. Finally, one of them said, "Why Miss Delany, we can't help it; you look just like a slice of Heaven." And I said, "Well, I ain't your slice of Heaven, so put your eyes back in yo' head. (Beat) We are not old maids. We are maiden ladies.

SADIE: Well, whatever we are, I have no regrets about it. I've had a good life, child . . . (thoughtful beat) Remember, it was on your way to your job in Brunswick - you came close to being lynched -

BESSIE: Oh, yes . . . that's right. I had to change trains in Waycross, Georgia. I was sitting in the little colored waiting room at the station, and I took my hair down and was combing it.

SADIE: She had hair down to here. (She indicates her knee.)

BESSIE: I was fixing myself up. I was going to my new job, and I wanted to look nice. There was no one in there except me and two colored teachers from New York who were traveling with me to Brunswick.

SADIE: So, there she was with her long hair down when this white man opened the door to the colored waiting room.

BESSIE: The white man stuck his head in and started, well, leering at me. He was drunk, and he smelled bad, and he started mumbling things. And I said, "Oh, why don't you shut up and go wait with your own kind in the white waiting room?"

SADIE: (Overlapping.) hmmmm . . . hmmmmmm . . . hm ... hmmmmmm . . . hmmmmmmm . . .

BESSIE: He slammed the door and I could hear him shouting at the top of his lungs outside, "The nigger bitch insulted me! The nigger bitch insulted me!"

SADIE: The two colored teachers slipped out the back and made a beeline for the woods.

BESSIE: Yes! They hid in the woods! I guess I can't blame them. Well, I could see a crowd begin to gather on the platform, and I knew I was in big trouble.

SADIE: Papa always said, "If you see a crowd, you go the other way."

BESSIE: I was just waiting for somebody to get a rope. Thousands of Negroes had been lynched for far less than what I had just done. But I just continued to sit on the bench, combing my hair, while that white man was a-carrying on! You see, if you act real scared, sometimes that spurs them on. Two things saved me: that glorious, blessed train rounded the bend, breaking up the crowd and giving me my way to get on out of there. And it helped that the white man was drunk as a skunk, and that turned off some of the white people. But I wasn't afraid to die! I know you ain't got to die but once, and it seemed as good a reason to die as any. I was ready. Lord, help me, I was ready.

SADIE: You were a fool to provoke that white man. You should have ignored him.

BESSIE: How do you ignore some drunk, smelly white man treating you like trash?

SADIE: Sometimes, it's better to put up with it, and live to tell about it. At the very least you should have run off into the woods with those other two teachers.

BESSIE: (To the audience.) I told you: I would rather die than back down, honey . . .

SADIE: You are lucky to be alive.

BESSIE: (After a beat) Sadie! You know what I’ve been thinking lately? All those people who were mean to us in our lives . . . Why, they’ve turned to dust, and here we are –

BESSIE AND SADIE: (Togther) Still here!

BESSIE: They’re turning in their graves while me and sweet sister Sadie are getting the last word . . . We’re having our say, giving our opinion.

SADIE: Lord ain’t it good to be an American.

BESSIE: I’ll tell you a little secret: I’m starting to feel optimistic. Maybe I’ll get into Heaven after all. I do have some redeeming qualities. I may have to hang on to Sadie’s heels, but I’ll get there.
```

---

## IC-0169: Here in This House

- Title: Here in This House
- Author (byline): Christopher Scarpo
- Work: Found in Fast Horse Plays, Round 5, Pg 23-31
- Publisher: Create Space Independent Publishing
- Publication date as stated: July 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: GIRL
- Teaser before the introduction: Yes
- Spoken words (computed): 1986
- Already set (do not supply): none

### Source block (context only)

```text
Author: Christopher Scarpo
Book: Found in Fast Horse Plays, Round 5, Pg 23-31
ISBN: 978-1491283189
Publisher: Create Space Independent Publishing
Date (Month/Year): July 2013
```

### Introduction (context only: never use it for content warnings)

```text
In the 1990s and 2000s, a Christian movement now known as “purity culture” reached its height in America. During this period, a prolific industry of purity-themed bibles, rallies and books emerged. Sales of purity rings increased, worn as a symbol of commitment to sexual purity. Purity pledges were signed by teenagers to demonstrate their vow of abstinence. Beyond abstinence, young Christians were encouraged not to date. Young women and girls were instructed to be careful how they dressed and interacted with others to avoid “tempting” men, and strict gender roles were encouraged. But a sheltered life does not necessarily lead to a safe life.

Here in This House by Christopher Scarpo
```

### Performance text (classify this)

```text
A sheltered teen - 16 years old

GIRL: (Pgs 23-31) It's not like I had huge plans for the summer or anything, but that did not mean I was all about spending a month in the wilderness at Happy Faces Summer Camp. Aren't camps for 12-year-olds, not high school kids? Whatever. Goodbye Fashion Square Mall and all night makeover parties with my friends and hello to spending a month in the forest, getting to know God better. And hello to bugs -- lots of bugs. Really big ones that always seemed to find a way into my cabin. But God says love all things equally, and I guess that includes centipedes. (beat) I've known God forever; but the whole point at Happy Faces was to help you get even closer to the Big Man Upstairs.

So, in between roasting holy marshmallows to go on sacred s'mores and swimming in the river filled with creepy underwater bugs, we spent lots of time reading the Bible and doing arts and crafts. We had to draw a picture of Jesus, but I can't really, like draw, so my picture of Jesus looked like a person with a stick body and a potato for a head. But I explained to the camp counselor that what really mattered was that you had to have Jesus in your heart, then he would forgive all of your sins, even drawing him to look like a potato. Oh my god, I totally love Jesus! The counselor told me that I shouldn't be saying, "Oh my god.” She looked at me with this really intense look and said something about me having some quiet time and drawing another picture of Jesus as a vegetable.

The two most amazing things I learned at Happy Faces Summer Camp were 1) God totally believes in me, and knows I can do anything, even if it seems tough and 2) He's gonna love me no matter what. I really like knowing that.

GIRL: So, anyway, school starts again and I decide that in between trying to get a 4.0 GPA and scoring fifteen hundred on the SAT, that I had another really big goal. "Mom, Dad, I think I'm ready to start dating." And Mom and Dad totally silent like . . . potatoes. Then, Mom tells me that Jesus wants me to focus on my grades and Dad tells me that I can date when I get married. I don't think my husband, or Jesus for that matter, would really be down with me dating after I got married! Then Dad tells me boys are really bad, and I'm getting the picture that Mom and Dad don't like boys at all -- no-way, no how, no go, no dating ever. Later that night, I had some quiet time with you-know-who and explained that now that I was a junior in high school, I should probably go on a date. And I think he understood, which was a huge relief. (beat) I know it's a sin to lie to your Mom and Dad but, uh, I thought about it. If I just didn't say anything then that wasn't lying at all, and Jesus would probably be okay with it.

The next day at school I talk to my two best friends and I explain that I'm ready to start dating. And Clarissa asks, “What about Jesus?” And Marissa asks, “What about your parents?” Jesus is totally fine with it and my parents don't need to know! Marissa suggests that we like have an audition or something. Drama club is for losers! And then Clarissa says we should start taking applications. Um, I'm not Burger King! Sometimes [they]are clueless. I decide there has to be an easier way. So, after 4th period, I go up to Lucky at his locker . . . (awkwardly nervous) "Hey, Lucky, hi! I was wondering if, well . . . if you would like go out on a date." I was nervous but I don't think he could tell. Everybody made such a deal out of this whole process and it was really easy.

Friday night comes and I change my outfit seven times and after looking in the mirror to make sure I didn't look like a potato, I like went out on my first date. I told my parents I had a school project to work on. We went to Grace's and I had a pineapple coke . . . I was really nervous. And Lucky wasn't weirded out at all. He told me how it is to be on the football team and how his older brother is a football star at college, and I looked at him, "very intently and nodded my head once every few words" -- that was some advice I got on this dating site. Then we held hands for a few minutes and then the date was over. And I’m thinking, that was not sinful at all. Maybe my parents just don't remember how dating is. I was grateful that Jesus had been able to guide me in the right direction. [But] I was really worried about asking Lucky on a second date. (beat, with excitement) Two days later, he asked me! Wow! And then he asks again, and again. (knowingly) According to GirlDate.com after date number five, you're boyfriend and girlfriend.

Okay, so it's Saturday night, and Lucky takes me to Red Lobster, which is really fancy for high school, right? So, I know this is going to be a special night. While we're eating our fried shrimp, he presents me this box. I unwrap it and there's these silver hoop earrings. Lucky tells me that he'd been saving up forever for them, and I'm thinking that they look a lot like the ones you can get at the drugstore for two dollars. But it's the thought that counts. And then, okay, get this, Lucky tells me that he loves me!

We drive around for a while; Lucky parks the car and tells me he wants to talk for a little while. I'm pretty nervous, so I say a little prayer, asking God to help me with the right things to say, 'cause I’m thinking, after tonight, Lucky is gonna be my husband someday. And then, Lucky tells me that tonight we're gonna do more than hold hands. (excited) Oh, my go . . . goodness! I'm gonna have my first kiss tonight. And just like I thought, Lucky starts kissing me. But, it's not like little peck kisses, it's like the open mouth kind and at first it was okay . . . but then I'm trying to back away. Lucky holds me by the back of my head and tells me, "I'm so glad you’re ready." If he meant ready for this, I am soooo not ready and maybe will never be ready. I'm saying to Lucky that this is enough for tonight but he's telling me he loves me over and over. I'm like, okay, I get it, roger that! But, and I don't even know how, his hands are under my shirt and pressing and squeezing and I'm thinking back to GirlDate.com. I say, "That's enough, Lucky. Please stop." But, I guess he was loving me so much right then that he didn't even hear me.

He was on top of me and his hands aren't under my shirt anymore, they're, uh . . . lower. He was pulling my jeans off. (crying) "Stop, Lucky. Please stop." And, then, he, um. . . he well, he was right there . . . right where he wasn't supposed to be at all. And there's a lot of pushing, and my whole body feels as flat as paper or like a really heavy rock. It hurt the worst of any hurt my body could feel . And all of a sudden, I feel my Mom and y Dad and Jesus too were in the backseat of Lucky's car, saying, "Tada! -- This is why." And then Lucky lifts himself off and his face is sweaty and gross. I don't think he even noticed I was crying, ‘cause he says, "That's how it's supposed to be. When you're in love." And he does his jeans up and um, he drives me home.

And um, we're both totally silent. I just go to bed, thinking when I wake up it's all gonna make sense, or just go away like a bad dream. But I wake up and it's even worse. I'm thinking, okay, so now I've had the dating experience, and we'll just move on from this, right? But within two days at school, everybody knows about it, and Marissa won't even sit next to me at lunch and after 4th period, somebody has left this sign on my locker that says . . . SLUT. Everywhere I walk a thousand voices whispering. When Clarissa finally talks to me, she tells me that Lucky broke up with me and he's dating Alexis now. Well, that's just great!

Lucky stops me on the way past his locker on the 4th day and asks me, "You know why they call me Lucky?" I'm just staring down, shaking my head, I can't even look at him. He opens his locker, and on the back wall, there's this list written in black sharpie pen. It's a list of girls’ names -- name after name, and at the bottom of the list, the last name -- the last name is mine. Lucky just smiles at me and says, (mockingly) "I love you." And then he starts laughing. I get home from school, and Mom and Dad are home from work already, which is not like them; they both usually work ‘til really late. It looks like Mom had been crying and Dad is not happy. Mrs. Henderson, she goes to our church, called my Mom. She knew all about everything. And my Mom asks me, "How could you do this to us?" And my Dad asks, "How could you do this to Jesus?" And I'm thinking, how could Lucky do this to me! My Dad backhands me across the face -- he hasn't done that for a really long time, and then he says that I have ruined my body and that no husband would ever want me. Basically, I'm going to hell, and that, here in this house, they can't have that. Then they're talking about what this is going to do to my little brother and maybe they're going to have to send me away. And they don't mean Happy Faces Summer Camp.

So, I came here because I know that God's house never closes. I haven't been here for a long time, and it's weird ‘cause my parents talk about God all the time, but we never come to visit his house -- like ever. This is the first time my brain has been quiet since this whole thing started. And I think God understands that I've been trying. I do want to go to a good college. And I realize that 3.9 isn't a 4.0 and that l really need to get a 1500 next time instead of a 1480; but the point is, I really try to do what my parents tell me. I just wanted to see a movie with a boy, you know? Maybe if Mom or Dad had told me about boys . . . well, l guess that doesn't really matter now, does it?

But, here in this house, I really think God thinks I’m beautiful and that I can do whatever I put my mind to. God and I are still good. And so I ask him, if maybe he can talk to my parents -- maybe explain that I'm sorry I let that stuff happen with Lucky. I didn't mean to. . . I totally didn't mean to. I wish it hadn't happened. (looks up at the windows) I forget how *beautiful* the stained glass is here. Everything in those pictures is perfect. I guess life just isn't sometimes, like when your picture of Jesus looks like a potato. I think I'm gonna just *be* here in the quiet for a little longer.
```

---

## IC-0170: How Did I Get Away with Killing One of the Biggest Lawyers in the State? It Was Easy

- Title: How Did I Get Away with Killing One of the Biggest Lawyers in the State? It Was Easy
- Author (byline): Alice Walker
- Work: You Can’t Keep a Good Woman Down
- Publisher: Mariner Books
- Publication date as stated: May 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1930
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alice Walker
Book: You Can’t Keep a Good Woman Down
ISBN: 978-0156028622
Publisher: Mariner Books
Date (Month/Year): May 2003
```

### Introduction (context only: never use it for content warnings)

```text
How Did I Get Away with Killing One of the Biggest Lawyers in the State? It Was Easy by Alice Walker
```

### Performance text (classify this)

```text
WOMAN: My mother and father were not married. I never knew him. My mother must have loved him, though; she never talked against him when I was little. It was like he never existed. We lived on Poultry street. Why it was called Poultry street I never knew. I guess at one time there must have been a chicken factory somewhere along there. It was right near the center of town. I could walk to the state capitol in less than ten minutes. I could see the top—it was gold—of the capitol building from the front yard. When I was a little girl I used to think it was real gold, shining up there, and then they bought an eagle and put him on top, and when I used to walk up there I couldn't see the top of the building from the ground, it was so high, and I used to reach down and run my hand over the grass. It was like a rug, that grass was, so springy and silky and deep. They had these big old trees, too. Oaks and magnolias; and I thought the magnolia trees were beautiful and one night I climbed up in one of them and got a bloom and took it home. But the air in our house blighted it; it turned brown the minute I took it inside and the petals dropped off.

WOMAN: Mama worked in private homes. That's how she described her job, to make it sound nicer. 'I work in private homes,' she would say, and that sounded nicer, she thought, than saying 'I'm a maid.' Sometimes she made six dollars a day, working in two private homes. Most of the time she didn't make that much. By the time she paid the rent and bought milk and bananas there wasn't anything left.

She used to leave me alone sometimes because there was no one to keep me— and then there was an old woman up the street who looked after me for a while—and by the time she died she was more like a mother to me than Mama was. Mama was so tired every night when she came home, I never hardly got the chance to talk to her. And then sometimes she would go out at night or bring men home—but they never thought of marrying her. And they sure didn't want to be bothered with me. I guess most of them were like my own father; had children somewhere of their own that they'd left. And then they came to my Mama who fell for them every time. And I think she may have had a couple of abortions, like some of the women did, who couldn't feed any more mouths. But she tried.

Anyway, she was a nervous kind of woman. I think she had spells or something because she was so tired. But I didn't understand anything then about exhaustion, worry, lack of a proper diet; I just thought she wanted to work, to be away from the house. I didn't blame her. Where we lived people sometimes just threw pieces of furniture they didn't want over the railing. And there was broken glass and rags everywhere. The place stunk, especially in the summer. And children were always screaming and men were always cussing and women were always yelling about something . . . It was nothing for a girl or woman to be raped -- l was raped myself, when I was twelve, and my Mama never knew and I never told anybody. For, what could they do? It was just a boy, passing through. Somebody's cousin from the North.

One time my Mama was doing day’s work at a private home and took me with her. It was like being in fairyland. Everything was spotless and new, even before Mama started cleaning. I met the woman in the house and played with her children, I didn't even see the man, but he was in there somewhere, while I was out in the yard with the children. I was fourteen, but I guess I looked like a grown woman. Or maybe I looked fourteen. Anyway, the next day, he picked me up when I was coming from school and he said my Mama had asked him to do it. I got in the car with him . . . he took me to his law office, a big office in the middle of town, and he started asking me questions about 'how do you all live?' and 'what grade are you in?' and stuff like that. And then he began to touch me, and I pulled away. But he kept touching me and I was scared . . . he raped me. But afterwards he told me he hadn't forced me, that I felt something for him, and he gave me some money. I was crying, going down the stairs. I wanted to kill him.

I never told Mama. I thought that would be the end of it. But about two days later, on my way from school, he stopped his car again, and I got in. This time we went to his house; nobody was there. And he made me get into his wife's bed. After we'd been doing this for about three weeks, he told me he loved me. I didn't love him, but he had begun to look a little better to me. Really, I think, because he was so clean. He bathed a lot and never smelled even alive, to tell the truth. Or maybe it was the money he gave me, or the presents he bought. I told Mama I had a job after school baby-sitting. And she was glad that I could buy things I needed for school. But it was all from him.

This went on for two years. He wouldn't let me get pregnant, he said, and I didn't. I would just lay up there in his wife's bed and work out algebra problems or think about what new thing I was going to buy. But one day, when I got home, Mama was there ahead of me, and she saw me get out of his car. I knew when he was driving off that I was going to get it.

Mama asked me didn't I know he was a white man? Didn't I know he was a married man with two children? Didn't I have good sense? And do you know what I told her? I told her he loved me. Mama was crying and praying at the same time by then. The neighbors heard both of us screaming and crying, because Mama beat me almost to death with the cord from the electric iron. She just hacked it off the iron, still on the ironing board. She beat me till she couldn't raise her arm. And then she had one of her fits, just twitching and sweating and trying to claw herself into the floor. This scared me more than the beating. That night she told me something I hadn't paid much attention to before. She said: 'On top of everything else, that man's daddy goes on the TV every night and says folks like us ain't even human.' It was his daddy who had stood in the schoolhouse door saying it would be over his dead body before any black children would come into a white school.

But do you think that stopped me? No. I would look at his daddy on TV ranting and raving about how integration was a communist plot, and I would just think of how different his son Bubba was from his daddy! Do you understand what I'm saying. I thought he loved me. That meant something to me. What did I know about 'equal rights'? What did I care about 'integration'? I was sixteen! I wanted somebody to tell me I was pretty, and he was telling me that all the time. I even thought it was brave of him to go with me. History? What did I know about History?

I began to hate Mama. We argued about Bubba all the time, for months. And I still slipped out to meet him, because Mama had to work. I told him how she beat me, and about how much she despised him -- he was really pissed off that any black person could despise him -- about how she had these spells . . . Well, the day I became seventeen, the day of my seventeenth birthday, I signed papers in his law office, and I had my mother committed to an insane asylum.

After Mama had been in Carthage Insane Asylum for three months, she managed somehow to get a lawyer. An old slick-headed man who smoked great big black cigars. People laughed at him because he didn't even have a law office, but he was the only lawyer that would touch the case, because Bubba's daddy was such a big deal. And we all gathered in the judge's chambers -- because he wasn't about to let this case get out. Can you imagine, if it had? And Mama's old lawyer told the judge how Bubba's daddy had tried to buy him off. And Bubba got up and swore he'd never touched me. And then I got up and said Mama was insane. And do you know what? By that time it was true. Mama was insane. She had no mind left at all. They had given her shock treatments or something . . . God knows what else they gave her. But she was as vacant as an empty eye socket. She just sat sort of hunched over, and her hair was white.

And after all this, Bubba wanted us to keep going together. Mama was just an obstacle that he felt he had removed. But I just suddenly -- in a way I don't even pretend to understand -- woke up. It was like everything up to then had been some kind of dream. And I told him I wanted to get Mama out. But he wouldn't do it; he just kept trying to make me go with him. And sometimes— out of habit, I guess -- I did. My body did what it was being paid to do. And Mama died. And I killed Bubba.

How did I get away with killing one of the biggest lawyers in the state? It was easy. He kept a gun in his desk drawer at the office and one night I took it out and shot him. I shot him while he was wearing his thick winter overcoat, so I wouldn't have to see him bleed. But I don't think I took the time to wipe off my fingerprints, because, to tell the truth, I couldn't stand it another minute in that place. No one came after me, and I read in the paper the next day that he'd been killed by burglars. I guess they thought 'burglars' had stolen all that money Bubba kept in his safe -- but I had it. One of the carrots Bubba always dangled before me was that he was going to send me to college: I didn't see why he shouldn't do it.

The strangest thing was, Bubba's wife came over to the house and asked me if I'd mind looking after the children while she went to Bubba's funeral. I did it, of course, because I was afraid she'd suspect something if I didn't. So on the day he was buried I was in his house, sitting on his wife's bed with his children, and eating fried chicken his wife, Julie, had cooked."
```

---

## IC-0171: How to Write a Fairytale

- Title: How to Write a Fairytale
- Author (byline): Cora Sorenson
- Work: Fast Horse Plays, Round 3, Pgs 29-33
- Publisher: Fast Horse Drama
- Publication date as stated: Aug 2012
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SEQUOIA
- Teaser before the introduction: Yes
- Spoken words (computed): 1683
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cora Sorenson
Book: Fast Horse Plays, Round 3, Pgs 29-33
ISBN: 978-0615694894
Publisher: Fast Horse Drama
Date (Month/Year): Aug 2012
```

### Introduction (context only: never use it for content warnings)

```text
According to the CDC, approximately 1 in 4 girls and 1 in 20 boys in the United States are victims of sexual abuse before the age of 18* (Centers for Disease Control and Prevention, 2024), and most of them know the person who hurt them. Most of them are told it’s love. Most of them are told to stay quiet.

Sequoiah is 17 years old and standing at the edge of the world. She has tried building her fairy tale out of foster homes and occasional trips for ice cream. She has tried to recognize her life as a ‘blessing’. But she’s come to realize a devastating truth: people and things are rarely, if ever, what they seem. Her life is not a fairy tale – and there is no knight in shining armor in her story. Not even Jesus will save her from the wolves.

How to Write a Fairytale by Cora Sorenson
```

### Performance text (classify this)

```text
Location: Top of the Golden Gate Bridge

SEQUOIA: (Pgs 29-33) (age 17; direct but contemplative; vulnerable but guarded) (to audience) I totally did not expect for it to be this cold up here. I’m like, freezing my a** off, ya know? I mean I would have brought a sweater or something if I’d known. So . . . umm . . . anyway, my point is that people and things are rarely, like, if ever exactly as they seem.

So, like, Jesus and I have been on speaking terms for years. I mean, of course, we fight as good friends tend to do, but I like to think that we always make up before bedtime. It was Grandma Rose who taught me about getting up close and personal with Jesus when I was like, I dunno, probably like six. Grandma Rose was one of the first foster parents I ever had. She died three days before my ninth birthday, when she spoke to me it was like her voice was going through some kind of weird machine. “Your heart knows where it must go, Sequoia. You know everything that’s true.” That was the last time I cried.

SEQUOIA: I was a little bouncing ball for the next three years, until I was like, about twelve, I guess. So, it was sort of like I’d hooked up with Jesus’ personal fax line or something when I got placed with the DeWitts, right? The DeWitts were mid-thirties; she was a teacher, he was some kind of business something-or-other. They lived like two hours away from San Francisco, nice house. Interesting developments for my fairy tale, you know? We celebrated “my placement” by going to a Farley’s ice cream parlor and I ate three scoops of lemon custard ice cream. They had put a huge framed picture of a Sequoia redwood tree in my new bedroom. I liked them . . . for a little while.

But then Mr. DeWitt celebrated “my placement” two months later by coming into my bedroom and doing disgusting things to me. His hand under my nightgown was at first ice cold and then as hot as an iron brand. And me, I thought, of course, that I had to nightmare-ing something terrible, right? That Grandma Rose had just told me one too many real fairy tales and that this particular night terror was just too bad that it felt real. So I blinked my eyes, right? Once, twice, thrice, here Dorothy clicks her ruby slippers until she finds herself at home, sleeping soundly. No such luck, little shrub girl. No such happy endings for you, silly girl. So, I keep blinking and his hand is still there, now as red hot as I’d think a cattle prod to be. And I’m thinking, I should have gotten Jesus on speed dial or something, because I’m praying. “Please don’t hurt me like this,” because now it’s actually hurting my body and I’m fighting as hard as I can to push and get up, but with his other hand he shoves me down so hard, I’m afraid I won’t be able to find my breath at all, right? Not at all, and then for a few seconds I fear that I’m not breathing, that I’m going to die right there in that bed with my Mr. DeWitt branding me like a cow with his red-hot touch, and I’m waiting to see the aliens with their yellow lights. But I didn’t die, and Mr. DeWitt keeps at it, until whatever he’d hoped to happen happens and then he’s gone. No words, just gone. And I’m changed, bruised permanent, I guess. Branded. Yeah.

So, I didn’t tell anyone until I met Rusty. Well, not met Rusty, because we didn’t actually meet until just a few days ago. But when I first encountered Rusty, I’d stay up late – chatting on the ‘net, and that’s how I found him. Rusty told me that he was my age and lived in San Francisco. We chatted for hours about everything. So, I told him about Mr. DeWitt and he told me that things were going to be okay. Fairy tale ending. Yeah. It was months before he agreed to send a picture of himself. But when he did . . . well, teenage angst or not, a hot boy is a hot boy. Dark eyes, dark hair, good stuff. It wasn’t that, though, seriously. I couldn’t even really think of that. It was just . . . having somebody who would listen. So, we’re talking, going on two years of chatting with Rusty every single night. And he finally agrees to meet me at this little sushi bar in the city. I’m gonna go, and, umm, things are gonna change.

So, umm, three days ago I took Mrs. DeWitt’s Chase Platinum and got on a Greyhound to make the trip. And so, I got here, to the city at, like, six thirty or so . . . and I was supposed to meet Rusty at seven. So I wandered around until I found the place, and I walked in, and I waited. And well, like a half hour later, this guy comes over to me, and he says, “Sequoia? And umm, you know what was really strange about this? This guy, well, he says, “I’m Rusty” and well, what’s really frickin’ strange is that this guy doesn’t have dark hair at all. No . . . umm, his hair is blonde. And this guy, well, this guy has strange grey blue eyes, like the ocean. And umm, the weirdest frickin’ thing of all is that this guy is like, well, he’s like, I dunno, forty years old. Yeah, that’s right. Weird, huh? And, uh, this is Rusty. It is. And, of course, he starts apologizing almost immediately. Explaining, that he couldn’t, uh, explain until I met him.

The next thing I knew, I’m going back to his room with him. Back with Rusty to this fancy hotel where they don’t even look twice in the lobby. So, we get up to this huge big room with paintings and lights and a big bathtub that you can walk right into. And uh, Rusty tells me that he loves me. Right. And uh, apparently, to talk. He brought along this bag of stuff . . . all kinds of things, I didn’t even know what some of it was. This was, of course, like, only if I wanted to. And um, my body is just like hot ice at this point. I’m just burning up through my skin, but I find what I need. It’s, uh, this little silky blind fold. And Rusty, whaever, is sitting on the edge of the bed, an so I take this little blind-fold thing and I tie it around Rusty’s head. And he’s saying, “Oh, Sequoia, what’s next?” And me, I’m just full of fire, and it’s like there’s a herd of cattle or something stampeding through that hotel room, and I’m thinking, “Yeah, what’s next for you, fair sir?” And um, I knew that I just had one good chance, ya know? Just one, for sure one, but I didn’t realize that those hotel telephones are that heavy. But as quiet as I could, I unplugged the thing from the wall and, well, I brought it down as hard as I could on Rusty’s head. And um, for as hard as heads are, it gave way so easy, like, umm, rotted fruit or something. And he didn’t come back up really, I guess I heard like a bubbling sort of sound and so I just brought it up and down up and down up and down a bunch of times and then there was this big quiet all around us. A gigantic quiet, and I was just all bathed in red, and umm, Rusty was very still. And somebody was talking there. Grandma Rose or someone, maybe Jesus, I guess. “Your heart knows where it must go, Sequoia.” I really didn’t have much to say back, ya know? And I knew that Rusty wouldn’t be getting on-line again anytime soon. I went and I showered and I walked out of the room and I, uh, I left the hotel.

People and things are usually not exactly as they seem. Have you seen that actor? Emile Hirsch? Cute, dark hair, yadda yadda. Rusty sent me a picture of Emile Hirsch. Did he think I was stupid? Ha. I knew. I knew before I ever left. Yeah. So um, sometimes there’s fairytales and sometimes there’s just crap, right? So, um, you kind of learn stuff when you spend hours alone on the internet. And one thing I learned was how to open up file indexes when people send you crap. So I got Rusty to email me more pictures, right? And the fourth or fifth time it was from a file where there were pictures of him and his wife and his kids . . . his, uh, his teenage daughter. Her name is Rose. I wonder how hot she feels sometimes. Sometimes you just do what you gotta do. Yeah. So, uh, one of the interesting facts I learned was that, last year, 47 people committed suicide by jumping from up here. On the Golden Gate Bridge. You see, I can’t seem to reach Jesus at all these days. I don’t have any frickin’ clue what the business plan is for me at this point. Who is supposed to be saving who?

(shifts to directly addressing Jesus) Hello? Frickin’, hello? If you’re talking, I have no frickin’ idea what you’re sayin’ there, buddy. . . seriously?

(to audience) How many trials? Wasps? Scorpions? I burn and then I . . . well, then I forget. When there’s nothing worth remembering, it kinda gets a little tough to figure out the point, ya know? (to Jesus) Don’t you remember? I’m six, kneeling by my bed, chatting with you like we’re old friends? But then you failed to bring my Mommy back. How hard do I have to hurt? How faithful did you expect me to be? (to audience) Only 18 have jumped this year. I’d be 19. If a Sequoia tree falls in the great Pacific and no one hears it, does it still make a sound? Do you hear me? Can you answer? Can anyone?
```

---

## IC-0172: Hump Day

- Title: Hump Day
- Author (byline): Lynda van Devanter
- Work: Home Before Morning: The Story of an Army Nurse in Vietnam
- Publisher: University of Massachusetts Press
- Publication date as stated: April 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LYNDA
- Teaser before the introduction: No
- Spoken words (computed): 1769
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lynda Van Devanter
Book: Home Before Morning: The Story of an Army Nurse in Vietnam
ISBN: 1558492984
Publisher: University of Massachusetts Press
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
Lynda van Devanter was an army nurse who served in Vietnam in 1969 and ’70 at the 71st evacuation hospital in Pleiku. She began and led the Vietnam Veterans of America’s Women’s Writing Project and counseled many other veterans. She died on November 15th, 2002 from a cancer as a result of exposure to Agent Orange. Her story lives on. “Hump Day” by Lynda van Devanter
```

### Performance text (classify this)

```text
LYNDA: The largest number of people I grew up with grew up with a sense that we had a mission. We had a purpose to our lives, and that we had a responsibility to give something back to this world, and I was part of a generation of Americans who were chosen to change the world. We were sure of that. It was only a matter of waiting until we all grew up. We were the kid next door, both men and women. What I saw in Vietnam was not men. What I saw in Viet Nam was boys. They were kids. They were generally 17, 18, and 19 years old. And for those of us who were women in Viet Nam, we were barely out of nursing school. We were basically these naïve, idealistic kids of the 50’s and 60’s who thought of Kennedy in the same breath with, “Ask not what your country can do for you, ask what you can do for your country.” We thought of Kennedy in the same breath with, “This generation will pay any price, bear any burden, to save this world for democracy.” I was a citizen of the greatest country in the world, and I was about to give part of my self to keep America great. We were carried along by the noble sentiments of John Fitzgerald Kennedy, and honest to God, I mean, it beat in my heart. It beat in all of our hearts. It really did. And so, nursing was the way that I was going to make my contribution to society. As we began our odyssey into Viet Nam, as we began our odyssey into the new people that we were eventually to become, it was a process that I think we had hoped we would be able to ease our way into, and it didn’t quite turn out that way. The day that I arrived in Viet Nam, I arrived in --- --- at the 90th replacement battalion, I learned that 2nd lieutenant Sharon Lane, who was a nurse on a ward at the 312th evacuation hospital at Cu Chi, had been killed that morning when a rocket had landed on her ward. I suddenly became very aware that women could in fact be in danger, and that this was no game anymore. Although the instructors back in basic had warned us what to expect, no amount of warning could ever have prepared me for the sheer numbers of mutilated young bodies that the helicopter kept bringing to the 71st. Dead bodies in glad bags were still being lined up outside the ER door, to be moved to the morgue as there was time. The moans and screams of so many wounded were mixed up with the shouted orders of doctors and nurses. So much for easing my way in.

What I came to realize was we developed a living, breathing relationship with Death as a human entity. Death became somebody who we had a relationship with, and Death became somebody to fight sometimes and welcome sometimes. And when we fought with Death, we fought tooth and nail. And we used every tool at hand, and a lot of times the only tool we had was cursing it out because we were so enraged at it. As each day passed, I found myself growing a harder and harder shell to protect my emotions. I started listening to the local discontents, who railed against Nixon, Congress, the Joint Chiefs of Staff, and the whole U.S. government. Every time another person died on my table, I came one step closer to agreeing with them. As each day passed, I found myself growing a harder and harder shell to protect my emotions. I started listening to the local discontents, who railed against Nixon, Congress, the Joint Chiefs of Staff, and the whole U.S. government. Every time another person died on my table, I came one step closer to agreeing with them. And one day I saw some dead American soldiers lying outside the morgue. They had been ambushed by an NVA unit. The butchers had cut off our soldiers penises and stuffed them into the GI’s mouths. I was outraged by the scene, but not as outraged as I became when I later saw a similar scene, only this time with dead Viet Cong.

During those months, I lost my direction and found myself becoming a person I would never have been before Viet Nam. Maybe, you would have said I was merely getting tough. Like thousands of Americans, I began calling the Vietnamese, both friendly and enemy, gooks. I would have thought I was above that sort of racism. After all, hadn’t I marched in the United States for civil rights like a good Catholic girl who believed all oppression was wrong? For each one of us, there was someone who seemed to personify what the war was, its futility, its desperation, and the worst of it, the parts of it that remained with us for the rest of our lives after returning, at least for every one of us, who I know of who was a woman who served in Viet Nam. Mine was a guy named Gene. It was a few days before my hump day, the exact middle of my tour when I would be over the hump. I was lost in a heavy sleep under my bed when the phone started ringing. Still half asleep, I listened to the worlds. More casualties, Van. We need you in surgery. There’s a bad one in the neuro room, she said. I need you to pump blood in there. Leading to the operating table was the largest trail of blood I had ever seen. I tried to walk quickly through it but slipped. When I regained my balance, my eyes were drawn to the gurney, where several people were transferring the wounded soldier from the green litter to the table. The lower portion of his jaw, teeth exposed, dangled from what was left of his face. It dragged across the canvas litter and then swung in the air as he moved from the gurney to the table. His tongue hung hideously to the side with the rest of the bloody meat and exposed bone. When he was on the table, Mac Schafner, the facial surgeon, dropped the lower jaw back into place. I held my breath to keep from getting sick. For a moment, I was glued to the spot. I thought I had gotten used to it all, but they kept getting worse. I wasn’t sure I could handle this one. But the shout of the anesthesiologist, Jim Castellano, snapped me out of my trance.

‘The son of a bitch is drowning in blood!’ he screamed. ‘Someone help me get a f---ing airway into him.’ A gurgling came from the soldier’s throat. Jim’s hands were quick. ‘Don’t you dare die, you motherf---er.’

There was an ugly, metallic coughing sound as the soldier bucked for breath.

‘Breathe, damn you!’

A barely audible sound escaped. ‘That’s it, soldier. Come on.’

In the middle of the confusion, the neurosurgeon came into the room. He looked at the soldier on the table and shook his head. His face was red. ‘Who the f--k woke me up for this GORK?’

‘The brain doesn’t look too damaged,’ Mac said. ‘You’re wasting your time.’

‘We can fix him,’ Mac insisted, ‘just give me a chance.’ ‘Bulls--t,’ the neuro guy said, ‘that sucker’s going to die and there’s not a f---ing thing you can do.’

He stormed out of the room. It was all just another simple job where I could turn off my mind and try to forget that we were working on a person, but this one was different. The young soldier was not about to let me forget. During one of my circuits around the table, I accidentally kicked his clothes to the side. A snapshot fell from the torn pocket of his fatigue shirt. The picture was of a young couple, him and his girlfriend, I guessed, standing on the lawn in front of a two story house, perhaps belonging to her parents. On the back of the picture was writing, the ink partially blurred from sweat: ‘Gene and Katie, May 1968.’ I had to fight the tears as I looked from the picture to the helpless boy on the table. Now a mass of blood vessels and skin, so lacerated that nothing could hold them together. I had always held the notion that given enough time, anything could be stopped from bleeding I pumped 120 units of blood into that young man, yet as fast I pumped it in, he pumped it out. After hours of work, Mac realized it was futile. The boy had received so much banked blood that it would no longer clot. Now he was oozing from everywhere. Slowly, Mac wrapped the boy’s head in layers of pressure dressings and sent him to post-op ICU to die. Gene and Katie, May 1968. While I cleaned up the room, I kept telling myself a miracle could happen. He could stop bleeding. Nothing was impossible. Please, God, help him. This wasn’t merely another casualty, another piece of meat to throw on the table and try to sew back together again. He had been real, Gene. When I finished making the room ready for the next head injury, the next young boy, I walked to post-op to see Gene. I held his hand and asked him if he was in pain. In answer, he squeezed my hand weakly. I asked him if he wanted some pain medication, and he squeezed my hand again. All the ICU patients had morphine ordered for pain, and I asked one of the nurses to give Gene his morphine intravenously, knowing that while it would relieve his pain, it would also make him die faster. I didn’t care at that point. I just wanted him to slip away painlessly, quickly, easily. I ran my finger over the edge of the picture before putting it into an envelope with his other possessions, then I walked outside, sat on the grassy hill next to post-op and put my head in my hands. I wouldn’t cry, I told myself. I had to be tough. But I knew a profound change had already come over me. With the death of Gene and with the deaths of so many others, I had lost an important part of myself. The Lynda I had known before the war was gone forever.
```

---

## IC-0173: I am Adam Lanza's Mother

- Title: I am Adam Lanza's Mother
- Author (byline): Liza Long
- Work: Not specified
- Publisher: Huffington Post
- Publication date as stated: Dec 16, 2012
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MOTHER, MICHAEL, SOCIAL WORKER
- Teaser before the introduction: No
- Spoken words (computed): 1493
- Already set (do not supply): none

### Source block (context only)

```text
Author: Liza Long
ISBN: Newspaper
Publisher: Huffington Post
Date (Month/Year): Dec 16, 2012
```

### Introduction (context only: never use it for content warnings)

```text
A horrific national tragedy occurred on December 14, 2012 -- the murder of 20 children and six adults at Sandy Hook Elementary School in Newtown, Connecticut – the tragedy has ignited a new discussion on violence in America. In kitchens and coffee shops across the country, we tearfully debate the many faces of violence in America: gun culture, media violence, lack of mental health services, overt and covert wars abroad, religion, politics and the way we raise our children.

Liza Long, a writer based in Boise, says it’s easy to talk about guns. But it’s time to talk about mental illness. While every family's story of mental illness is different, and we may never know the whole of the Lanzas' story, tales like this one need to be heard -- and families who live them deserve our help.

I am Adam Lanza's Mother by Liza Long
```

### Performance text (classify this)

```text
MOTHER: Three days before 20-year-old Adam Lanza killed his mother, then opened fire on a classroom full of Connecticut kindergartners, my 13-year-old son Michael (name changed) missed his bus because he was wearing the wrong color pants.

MICHAEL: (belligerent; angry) I can wear these pants!

MOTHER: (to Michael, calmly) They are navy blue. Your school’s dress code says black or khaki pants only.

MICHAEL: (insistent) They told me I could wear these. You’re a stupid b****. I can wear whatever pants I want to. This is America. I have rights!

MOTHER: (reasonably) You can’t wear whatever pants you want to. And you definitely cannot call me a stupid b*****. You’re grounded from electronics for the rest of the day. Now get in the car, and I will take you to school.

(to audience) I live with a son who is mentally ill. I love my son. But he terrifies me. (beat) A few weeks ago, Michael pulled a knife and threatened to kill me and then himself after I asked him to return his overdue library books. His 7- and 9-year-old siblings knew the safety plan -- they ran to the car and locked the doors before I even asked them to. I managed to get the knife from Michael, then methodically collected all the sharp objects in the house into a single Tupperware container that now travels with me. Through it all, he continued to scream insults at me and threaten to kill or hurt me.

That conflict ended with three burly police officers and a paramedic wrestling my son onto a gurney for an expensive ambulance ride to the local emergency room. The mental hospital didn’t have any beds that day, and Michael calmed down nicely in the ER, so they sent us home with a prescription for Zyprexa and a follow-up visit with a local pediatric psychiatrist.

We still don’t know what’s wrong with Michael. Autism spectrum, ADHD, Oppositional Defiant or Intermittent Explosive Disorder have all been tossed around at various meetings with probation officers and social workers and counselors and teachers and school administrators. He’s been on a slew of antipsychotic and mood-altering pharmaceuticals, a Russian novel of behavioral plans. Nothing seems to work.

At the start of seventh grade, Michael was accepted to an accelerated program for highly gifted math and science students. His IQ is off the charts. When he’s in a good mood, he will gladly bend your ear on subjects ranging from Greek mythology to the differences between Einsteinian and Newtonian physics to Doctor Who. He’s in a good mood most of the time. But when he’s not, watch out. And it’s impossible to predict what will set him off.

Several weeks into his new junior high school, Michael began exhibiting increasingly odd and threatening behaviors at school. We decided to transfer him to the district’s most restrictive behavioral program, a contained school environment where children who can’t function in normal classrooms can access their right to free public babysitting from 7:30-1:50 Monday through Friday until they turn 18.

The morning of the pants incident, Michael continued to argue with me on the drive. He would occasionally apologize and seem remorseful. Right before we turned into his school parking lot, he said . . .

MICHAEL: Look, Mom, I’m really sorry. Can I have video games back today?

MOTHER: No way. You cannot act the way you acted this morning and think you can get your electronic privileges back that quickly. (to audience) His face turned cold, and his eyes were full of calculated rage.

MICHAEL: Then I’m going to kill myself. I’m going to jump out of this car right now and kill myself.

MOTHER: (beat) That was it. After the knife incident, I [had] told him that if he ever said those words again, I would take him straight to the mental hospital, no ifs, ands, or buts. I did not respond, except to pull the car into the opposite lane, turning left instead of right.

MICHAEL: (suddenly worried) Where are you taking me? Where are we going?

MOTHER: You know where we are going.

MICHAEL: (frantically) No! You can’t do that to me! You’re sending me to hell! You’re sending me straight to hell!

MOTHER: I pulled up in front of the hospital, frantically waving for one of the clinicians who happened to be standing outside. (calling out to clinician) Call the police. Hurry!

(to audience) Michael was in a full-blown fit by then, screaming and hitting. I hugged him close so he couldn’t escape from the car. He bit me several times and repeatedly jabbed his elbows into my rib cage. I’m still stronger than he is, but I won’t be for much longer.

The police came quickly and carried my son screaming and kicking into the bowels of the hospital. I started to shake, and tears filled my eyes as I filled out the paperwork -- “Were there any difficulties with. . . at what age did your child. . . were there any problems with. . . has your child ever experienced. . . does your child have. . .”

At least we have health insurance now. I recently accepted a position with a local college, giving up my freelance career because when you have a kid like this, you need benefits. You’ll do anything for benefits. No individual insurance plan will cover this kind of thing.

For days, my son insisted that I was lying -- that I made the whole thing up so that I could get rid of him. The first day, when I called to check up on him, he said . . .

MICHAEL: (on the phone) I hate you. And I’m going to get my revenge as soon as I get out of here.

MOTHER: By day three, he was my calm, sweet boy again, all apologies and promises to get better. I’ve heard those promises for years. I don’t believe them anymore.

On the intake form, under the question, “What are your expectations for treatment?” I wrote, “I need help.” And I do. This problem is too big for me to handle on my own. Sometimes there are no good options. So, you just pray for grace and trust that in hindsight, it will all make sense.

I am sharing this story because I am Adam Lanza’s mother. I am Dylan Klebold’s and Eric Harris’s mother. I am James Holmes’s mother. I am Jared Loughner’s mother. I am Seung-Hui Cho’s mother. And these boys -- and their mothers -- need help. In the wake of another horrific national tragedy, it’s easy to talk about guns. But it’s time to talk about mental illness.

According to Mother Jones, since 1982, 61 mass murders involving firearms have occurred throughout the country. Of these, 43 of the killers were white males, and only one was a woman. (Suggested update 1/26/2026) According to Mother Jones, since 1982, 140* mass murders involving firearms have occurred throughout the country. Of these, 85 of the killers were white males, and only 4 were women. Mother Jones focused on whether the killers obtained their guns legally (most did). But this highly visible sign of mental illness should lead us to consider how many people in the U.S. live in fear, like I do.

When I asked my son’s social worker about my options, he said that the only thing I could do was to get Michael charged with a crime.

SOCIAL WORKER: If he’s back in the system, they’ll create a paper trail. That’s the only way you’re ever going to get anything done. No one will pay attention to you unless you’ve got charges.

MOTHER: I don’t believe my son belongs in jail. The chaotic environment exacerbates Michael’s sensitivity to sensory stimuli and doesn’t deal with the underlying pathology. But it seems like the United States is using prison as the solution of choice for mentally ill people. According to Human Rights Watch, the number of mentally ill inmates in U.S. prisons quadrupled from 2000 to 2006, and it continues to rise -- in fact, the rate of inmate mental illness is five times greater (56 percent) than in the non-incarcerated population. (Suggested update 1/26/2026) According to ** The Prison Policy Initiative: As of 2025-2026, over 37% to 44% of incarcerated people in U.S. state and federal prisons and local jails have a history of mental health issues, with up to 1 in 5 suffering from a serious mental illness. These high figures mean over 1 million people with mental health issues are currently incarcerated. With state-run treatment centers and hospitals shuttered, prison is now the last resort for the mentally ill.

No one wants to send a 13-year-old genius who loves Harry Potter and his snuggle animal collection to jail. But our society, with its stigma on mental illness and its broken healthcare system, does not provide us with other options. Then another tortured soul shoots up a fast-food restaurant. A mall. A kindergarten classroom. And we wring our hands and say, “Something must be done.”

I agree that something must be done. It’s time for a meaningful, nation-wide conversation about mental health. That’s the only way our nation can ever truly heal. God help me. God help Michael. God help us all.
```

---

## IC-0174: I am Nujood, Age 10 and Divorced

- Title: I am Nujood, Age 10 and Divorced
- Author (byline): Nujood Ali and Delphine Minoui
- Work: Not specified
- Publisher: Broadway Books
- Publication date as stated: 978-0307589675
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NUJOOD, PAPA, THAMER, MOTHER-IN-LAW, DOWLA, JUDGE, JUDGE 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1929
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nujood Ali and Delphine Minoui
ISBN: 978-0307589675
Publisher: Broadway Books
Date (Month/Year): 978-0307589675
```

### Introduction (context only: never use it for content warnings)

```text
With harrowing directness, Nujood tells of abuse at her husband's hands and of her daring escape. With the help of local advocates and the press, Nujood obtained her freedom—an extraordinary achievement in Yemen, where almost half of all girls are married under the legal age. I am Nujood, Age 10 and Divorced by Nujood Ali and Delphine Minoui
```

### Performance text (classify this)

```text
Suggested for performance by a young female student of middle-eastern descent. A middle eastern dialect example can be found at http://www.dialectsarchive.com/saudi-arabia-4

It was in Yemen, an extraordinary and turbulent country, barely ten years ago, that a little girl named Nujood was born.

A tiny wisp of a thing, Nujood is neither a queen nor a princess. She is a normal girl with parents and plenty of brothers and sisters. Like all children her age, she loves to play hide-and-seek and adores chocolate. She likes to make colored drawings and fantasizes about being a sea turtle, because she has never seen the ocean. When she smiles, a tiny dimple appears in her left cheek.

One cold and gray February evening in 2008, however, that appealing and mischievous grin suddenly melted into bitter tears when her father told her that she was going to wed a man three times her age. It was as if the whole world had landed on her shoulders. Hastily married off a few days later, the little girl resolved to gather all her strength and try to escape her miserable fate . . .

NUJOOD: In Khardji, the village in Yemen where I was born, women are not taught how to make choices. When she was about 16, Shoya, my mother, married my father without protest. And when he decided four years later to choose a second wife, my mother obediently accepted his decision. It was with that same resignation that I at first agreed to my marriage, without realizing what was at stake. At my age, you don’t ask yourself many questions.

One February evening in 2008, Aba—Papa—told me he had some good news.

PAPA: Nujood, you are to be married.

NUJOOD: The news came out of nowhere. I didn’t really understand. At first I felt almost relieved because life at home had become impossible. Aba had never been able to find full-time employment after losing his street-sweeper job, so we were always late with the rent. Aba was spending his afternoons chewing khat with neighbors. He claimed it helped him forget his troubles. It was during one of those khat sessions that a man of about 30 had approached him.

THAMER: I would like our families to be united

NUJOOD: . . . the man had said. His name was Faez Ali Thamer, and he worked as a deliveryman. My father accepted his proposal.

PAPA: It’s the best way to protect her. She won’t be raped by a stranger and become the prey of evil rumors. This man seems honest. He has promised not to touch Nujood until she’s older. Besides, we haven’t enough money to feed the whole family.

NUJOOD: My wedding preparations moved rapidly ahead, and I soon realized my misfortune when my future husband’s family decided that I must leave school. I loved school. It was my refuge, a happiness all my own.

In the back of the SUV waiting in front of our door, a short man was staring at me. He wore a long white zanna and had a mustache. His short wavy hair was mussed, and his face was poorly shaved. He was not handsome. This was Faez Ali Thamer!

When the motor rumbled to life and the driver pulled away, I started crying, silently, with my face to the window as I watched Omma grow smaller and smaller.

How relieved I felt when they led me to my room. A long woven mat was lying on the floor: my bed. I didn’t even need to put out the light to fall asleep. When the door crashed open, I was startled awake. I’d barely opened my eyes when I felt a damp, hairy body pressing against me.

“Please, I’m begging you, leave me alone,” I gasped.

THAMER: You are my wife!

NUJOOD: I leaped to my feet. The door was not completely closed, and spying a glimmer of light, I dashed toward the courtyard. “Help! Help!” I shrieked, sobbing. My voice rang in the night, but it was as if I were shouting into a void. I ran, panting for breath -- arms caught me, held me tightly, wrestled me back into the bedroom, pushed me down on the mat. I felt paralyzed, as if I had been tied down.

When he took off his tunic, I rolled into a ball to protect myself, but he began pulling at my nightshirt. He started to laugh, nastily.

THAMER: You are my wife. Now you must do what I want!

NUJOOD: Suddenly it was as if I’d been snatched up by a hurricane, flung around, struck by lightning, and I had no more strength to fight back. Something burning invaded the deepest part of me. No matter how I screamed, no one came to help me. It hurt, awfully. I shrieked one more time, I think, then lost consciousness.

I had to adjust quickly to a new life. I had no right to leave the house, no right to complain, no right to say no. During the day, I had to obey my mother-in-law’s orders: Cut up the vegetables, wash the floor, do the dishes. Whenever I stopped for a moment, my mother-in-law pulled my hair.

He left every morning and returned right before sunset. Each time I heard him arrive, the same panic seized my heart. When night fell, I knew what would begin again. The same savagery, the same pain and distress. On the third day, he began hitting me, first with his hands, then with a stick. And his mother egged him on. Whenever he would complain about me, she would tell him,

MOTHER-IN-LAW: Hit her even harder. She must listen to you—she’s your wife.

NUJOOD: I lived in permanent fear. Whenever I could, I would hide in a corner, lost and bewildered. One morning, worn down by all my crying, he told me he would allow me to visit my parents. At last!

PAPA: Nujood, you are a married woman now. You must stay with your husband. If you divorce your husband, my brothers and cousins will kill me! Honor comes first.

NUJOOD: I went to see Dowla, my father’s second wife, who lived with her five children in a tiny apartment across from our street. I poured out my heart to her, and my story seemed to affect her deeply.

DOWLA: (whispering) Nujood, if no one will listen to you, you must go straight to court. Ask to see the judge—his job is to help victims.

NUJOOD: My head is spinning—In the yard outside the courthouse, a crowd is bustling in every direction. No one sees me: I’m too small. I’m only ten years old, maybe not even that. Who knows?

Trembling, I latch on to the first passing veil, hoping to get the attention of the woman it conceals. “I want to talk to the judge.” Two big eyes framed in black stare at me in surprise.

“Follow me,” the woman finally says. The door opens onto a room full of people, and at the far end, behind a desk, a thin-faced man with a mustache. It’s the judge at last.

JUDGE: And what can I do for you?

NUJOOD: It is a curiously gentle voice. “I want a divorce.”

JUDGE: At your age? How can you already be married? And why do you want a divorce?

NUJOOD: I look him straight in the eye. “Because my husband beats me.”

It’s as if I had slapped him in the face. His expression freezes again. Point-blank, he asks me,

JUDGE: Are you still a virgin?

NUJOOD: I swallow hard. I’m ashamed of talking about these things. But in that same instant, I understand that if I want to win, I must. “No. I bled.”

He’s shocked. I can see his surprise, see him trying to conceal his emotions. Then he takes a deep breath and says,

JUDGE: I’m going to help you.

NUJOOD: I feel relieved. I watch him grab his phone with his shaking hand. With luck, he’ll act quickly, and this evening, I’ll be able to go home to my parents and play with my brothers and sisters, just like before. Divorced! Without that dread of finding myself alone, at nightfall, in the same bedroom with him.

A second judge joins us in the room, and he dashes my enthusiasm to bits.

JUDGE 2: My child, this might very well take a lot more time than you think. And unfortunately, I cannot promise that you will win.

NUJOOD: He says he has never seen a case like mine, because no little girl has, until now, showed up at a courthouse. . . . Do they realize that if I go home without any guarantee, my husband will come get me, and the torture will start all over again?

“I want to get divorced!” I frown fiercely to show I mean it. The sound of my own voice makes me jump.

JUDGE 2: According to Yemeni law, it is difficult for you to file a complaint against your husband and your father

NUJOOD: Like many children born in Yemeni villages, I didn’t have a birth certificate, and I was too young to initiate proceedings against anyone. A contract had been signed and approved by the men of my family. According to Yemeni tradition, it was valid.

JUDGE 2: For the moment we must act quickly. I suggest we place Nujood’s father and husband under temporary arrest. If we want to protect her, it’s better to have them in prison than at liberty.”

NUJOOD: Prison! Would Aba ever forgive me? I was consumed with shame and guilt.

*****************

NUJOOD: The great day has arrived. The courtroom is full—I have never seen so many cameras. Beneath my black scarf, I’m perspiring heavily. Deep down I feel frozen solid, unable to move. Just how does a divorce happen? What if the monster simply says no? If he begins threatening the judge?

I shiver: I recognize Aba and . . . the monster, escorted by two soldiers. The prisoners look furious. I find myself staring into Aba’s eyes. He seems so upset. “Honor,” he had said. Seeing his face, I begin to understand what that very complicated word means. I can see in my Aba’s eyes that he’s angry and ashamed at the same time. I’m so furious at him, but I can’t help feeling sorry for him too. The respect of other men—that’s so important here.

It’s the judge’s turn to speak.

JUDGE: Listen to me carefully. You married this little girl two months ago, you slept with her, you struck her. Is that true, yes or no?”

NUJOOD: I hold my breath. The monster blinks, then replies,

THAMER: Yes, But I was gentle with her, I was careful. I did not beat her.

NUJOOD: His answer is like a slap in the face, reminding me of all those other slaps, the insults, the suffering. “That’s not true!” I yell, beside myself with anger.

Everyone turns to look at me. But I’m the first to be astonished at my outburst. In the end, I am saved by the judge’s verdict.

JUDGE: The divorce is granted.

NUJOOD: My divorce has changed my life. When I go out in the street, sometimes women call to me, congratulating me. I recently returned to live with my parents. We all seem to be pretending to have forgotten what happened. My nightmares stopped a few weeks ago. Instead, I’ve been dreaming about school. When I grow up, I’ll be a lawyer, to defend other little girls like me.

Update: In April 2009, the Yemeni parliament raised the legal age of consent to 17, but it was overturned the next day. Today, Yemen is in political turmoil, and men can take brides of any age.
```

---

## IC-0175: I Can Hear My Soul Cracking

- Title: I Can Hear My Soul Cracking
- Author (byline): Slavenka Drakulic
- Work: A Memory, a Monologue, a Rant, and a Prayer, Pg 51+
- Publisher: Villard
- Publication date as stated: May 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1448
- Already set (do not supply): none

### Source block (context only)

```text
Author: Slavenka Drakulic
Book: A Memory, a Monologue, a Rant, and a Prayer, Pg 51+
ISBN: 978-0345497918
Publisher: Villard
Date (Month/Year): May 2007
```

### Introduction (context only: never use it for content warnings)

```text
In 1995, a paramilitary Serbian unit known as the Scorpions executed six unidentified civilian men. Four of them were underage; the other two, under 30. The soldiers filmed the executions to be used for educational purposes. A “how to” instructional video for executions, if you will.

Before the film footage was destroyed, a US film company created a documentary covering the Bosnian War. And the events of Srebrenica. More than 8,000 men and boys in and around the town of Srebrenica were killed – a massacre – a genocide.

Fast forward to 2005. Imagine flipping through the channels on your television only to come across film footage of your son’s execution. A son who had disappeared a decade earlier when he was only 16.

I Can Hear My Soul Cracking by Slavenka Drakulic
```

### Performance text (classify this)

```text
MOTHER: (Pg 51+) You ask me about my son? How I felt when I saw Azmir being killed? My child, how can I answer that kind of question? How can I tell you that? What words can I use to describe my pain? You say “killed,” and it seems to me that you feel nothing—how could you? He is only a name to you. But my whole body trembles when I hear it, just that one word. Azmir, my son, he was the soul of my soul. . .

But perhaps I should try to tell you that, for the sake of others who show remorse and have respect for my tragedy. And for the sake of other mothers like me, I know that they are many.

MOTHER: That day it was only the beginning of June but already very hot. Just like that July day in Srebrenica ten years ago, I thought as I put a dzezva with water for a coffee on a stove. My second coffee of the day. It was late afternoon, and soon my neighbor Amra will come home from work with her young daughter, Selma. Often I envied her for having a daughter; it is such a blessing to have a female child in a time of war. But I am wrong, of course. A woman’s curse is different, that’s all. I was grateful that Amra was helping me. I expected that the three of us would have a supper together and watch television, as we did every evening. Ten years passed. If Azmir had not disappeared, he would have been twenty-six now—a grown-up man, maybe even married. I still remember that he liked that dark-haired girl from his school class, though nowadays it would be difficult for them to marry.

She was a Serb. I like to imagine what would happen if he were here with me. I daydream about his job—he was so good with his hands—and a new house that he would surely be able to build. I like to daydream, imagining Azmir had the power to warm me and wake me up from a cold that I felt inside. That warmth used to keep me alive. But then immediately, I feel shame, the same feeling that I have experienced so many times, shame that I am alive and he. . . . Why? Why me? If someone had asked me to trade my life for that of my son, Azmir, I gladly would have done it. Not very tall and rather thin, he looked younger than his age—no more than a boy, really! This was the reason that I believed Azmir could be spared by soldiers. How wrong I was, I thought, embittered, sitting in the kitchen that afternoon. I slowly sipped my thick, strong coffee. See, I was convinced that I was reconciled with Azmir’s death long ago. Only I didn’t mention that ugly word, not even to myself. What else would keep him from coming back to me, calling me, for ten years? No way Azmir would not contact me somehow, through relatives, perhaps, he would find a way. My whole body told me that Azmir was no longer in this world, the same as his uncle, who was killed by Arkan’s soldiers when he visited Bijeljina at the very beginning of the war. At least I knew about him, I was certain, I was even able to get his body (for money, of course) and bury him properly. It is important to give people a burial; one should not be buried without a name, together with others in a mass grave. Why do we all have a name? We have it in life, and we should have it in death, that’s what I think. And I wanted to bury Azmir properly, if he was . . . Well. Although I felt Azmir’s end in my every muscle and bone, the truth is that I did not know for certain what had happened to him. And when. And where. It was not officially confirmed, or so I was told. In the last few years there were bones dug out, bones of thousands of men who were executed around Srebrenica.

Like other women, I went to identify remnants of my son. But a watch and a few photos and a piece of shirt I was shown, together with some darkened bones, were not his—odd how thin and fragile human bones look, as if eaten by earth, I thought. I remember letting out a big sigh, not knowing if I was relieved that these remains were not Azmir’s, or unhappy that I could not finally get over with the torture of living with uncertainty year after year. Thinking that his bones are shattered in the woods, that he is not buried, that some other mother—just like me—looks at someone’s things with fear and then relief. I was afraid that Azmir was not only dead but also lost for me, lost forever. So, that evening I was in the kitchen washing dishes after dinner with Amra and Selma, as usual. Just then I heard a voice from the TV in the living room saying something about Srebrenica. Ah, yet another program, I thought. I had seen a few in the years that passed, always with a knot in my throat while looking for the familiar face of Azmir and hoping that I wouldn’t see it. I was tired of this, not sure that I could force myself to watch anything that had to do with Srebrenica again. Ten years is a long time when you wait. Why look at that program, what could it tell me that I already didn’t know?

Yet I could not resist and went back to the living room and sat down. Amra was still there; Selma had gone back to their apartment. It was not a real film but some kind of a documentary, they said, and the picture was shaking, jumping. But I could see the Serbian soldiers in fatigue uniforms and red caps, their faces in front of the camera.

They were not even hiding, so sure they were of themselves, so arrogant. . . . And then I saw a group of four prisoners, young men with their hands tied in the back. The soldiers killed them just like that. It all happened so abruptly, so quickly, that I had no time to react, to switch off the TV set or something. But when another two prisoners appeared on the screen, I averted my eyes. I was not quick enough, though . . . because from the corner of my eye, I saw a familiar figure.

Instantly, I recognized my son, Azmir, his light brown hair, his hands, his shirt. He stood there for a short while with his hands tied back, bent slightly forward. Suddenly, I felt pressure in my chest, as if I were sinking into water—like when I was small and fell into a river. I gasped for air, but there was not enough. I could hear no sound, not even my heartbeat, nor could I utter a single sound. I was trapped in that water. In that room, in that picture on the screen, and there was no way out. I knew what was coming. When Azmir turned toward the camera with a frown on his forehead so familiar to me—because he used to frown like that when he was small and frightened, just before he would start crying—I tried to close my eyes. I had seen enough. But my own eyes betrayed me, and I stared while Azmir took a bullet and fell gently on his back. Now it all happened very, very slowly, or it only seemed so to me, I didn’t know any longer, nor did I care. I was still under the water with my lungs about to explode. Then I felt Amra shaking me gently, and I took a breath. I saw what I had seen so many times in my nightmares—but now, for the first time, I saw it to the very end. In my nightmare, there was never an end, and I would wake up wishing to know . . . the end. That evening I saw it. I know it now.

When I finally managed to close my eyes, I heard a strange sound coming from somewhere inside me. The sound of cracking, like cracking of ice in the springtime. “I can hear my soul cracking,” I said to Amra. She held me tightly in her arms for a while. That night, alone in my bed, I saw the same picture again and again. Not of Azmir’s death, but of his face, looking for help that did not come.
```

---

## IC-0176: I Love You, Dad (An Unsent Letter)

- Title: I Love You, Dad (An Unsent Letter)
- Author (byline): Grace Song
- Work: Yell-OH! Girls
- Publisher: Harper Collins
- Publication date as stated: July 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: GRACE
- Teaser before the introduction: Yes
- Spoken words (computed): 1451
- Already set (do not supply): none

### Source block (context only)

```text
Author: Grace Song
Book: Yell-OH! Girls
ISBN: 978-0060959449
Publisher: Harper Collins
Date (Month/Year): July 2001
```

### Introduction (context only: never use it for content warnings)

```text
Asian girls who have emigrated to the West with their families often feel torn between a reluctance to take on traditional roles and guilt over rejecting them . . . between the sense of independence Western society offers and the sense of obligation they feel not only to their parents, but to their parents' cultural values. And even as they strive for independence, they confront a society that often type-casts Asian women as meek and submissive. In I Love You, Dad by Grace Song . . . a young Asian woman tries desperately to put her conflicted feelings down on paper for her dying father.
```

### Performance text (classify this)

```text
GRACE: Dear Dad, I don't know why I'm writing this letter to you. It's probably because writing is easier than making you sit down with me for a serious father-daughter talk, since it's difficult for me to freely display my emotions around you. We discuss politics, religion, and education, but I can't remember ever saying "I love you" and giving you a warm embrace. I guess I thought that getting good grades in school was the best way of expressing my affection. Then, three months ago, you were diagnosed with liver cancer and I didn't know what to say. I've watched you sitting on the couch with a blank stare out the window, trying to conceal your worries and fears.

GRACE: Although we're close, we never had the kind of relationship where I could tell you about a new guy I met, or ask you for advice about problems I was having with close friends. Our relationship revolved around what was going on at school for instance, how many scholarships I could obtain in university. You encouraged me to strive for excellence in all aspects of my life and you always tried your best to give me everything I ever needed or wanted. We've shared good times, aside from the roughest period of my life when our relationship nearly ended.

Looking back I regret the grief I caused you but I hope you realize that the tension between us was largely due to generational differences. I know that my naiveté was a huge factor, but it was the pressure of learning to assimilate into two worlds bringing the mutually exclusive cultures (the East and the West) together- that was so overwhelming.

I didn't think you could understand what I was going through. Listening to your stories, it seemed like you were used to living according to a set of rules that everyone accepted. For instance, in Korea, students woke up bright and early to study and, not surprisingly, their typical day ended the way it began. They just studied more. Unlike our relationship, parents and their children shared the same mindset and methods of discipline, and the kids generally did as they were told. Immigrating to Canada wasn't easy. You set foot on foreign soil and immediately confronted new ideas. As traditional Korean parents you tried to keep your customs (the entire spirit) alive by teaching me the values your parents once taught you. Miscommunication led to confusion, and our relationship turned into a never-ending tug-of-war.

You put so much pressure on me to perform well in school. If my grades slipped the tiniest bit, it was time for you to pull out the "what-is-going-on-in-your-head?" lecture. You never failed to ask if I'd surpassed a smart Jewish boy who went to my school. ("Who got better grades this year, you or him?") And then we talked about my future. I thought that by becoming some big-shot lawyer, I'd be living your dream. You said that law was "in my blood" and went on about my "grandfather who was a great litigation attorney." I was glad that you thought I had the potential to become a successful lawyer, but you exerted so much pressure on me. I retaliated from time to time, yelling, "What if I don't become a lawyer! Will that make me less of a daughter?" But as usual, you ignored my emotional outburst. I usually surrendered, totally exhausted, with a pounding headache. I didn't see the point of arguing when it felt like everything I was saying was going in one ear and out the other.

The curfew you enforced also caused friction between us. My friends would constantly ask, "Why are your parents so strict?" My first reaction was to defend you and Mom. "They're not that bad, they let me stay out later on some nights." Of course that was totally untrue. I was always the first one to go home from a house party or a slumber party. I knew it was natural for parents to worry about their children, but you and Mom were so extreme, and l envied my friends, whose parents gave them more freedom.

Things started to change when I turned fifteen. Determined to break your rules, I was sneaking out of the house and meeting friends at karaoke bars and clubs. I experimented with beer and cigarettes, and started to hang out in predominantly Asian crowds. You forbade me to date because you thought it would distract me from my schoolwork, so I began to date people behind your back.

The guys I usually dated were either school dropouts or guys who were on the verge of failing out. My closest girlfriends were shallow, materialistic, and unmotivated to go to school. For some reason, though, I longed for their company. It was comforting to be in the presence of other young, second-generation Asian kids. They seemed to understand me in ways that you couldn't. When I came home, I wore a mask that concealed my true identity. Upon entering the house, the adventurous and humorous girl would disappear, instantly transforming into a quiet and submissive daughter.

I could see it in your eyes when I turned sixteen. You were worried. I was no longer the daughter you once knew. I had become somebody you barely recognized. To take control of the situation, you would deliver long-winded speeches at dinner table every night (if I were home). You eventually disconnected all the phones in the house, tore up all of my friends' pictures, and made me a prisoner in my own house. I kicked and screamed and spat evil words in your face; still, you didn't flinch. At the time I thought you wanted to make me miserable, when, really, you were saving me from failure.

In my self-absorbed state, I never considered the hardships you endured together so I was happy. You didn't make me pay for groceries, you paid my rent, and I never had to cook my own meals. While you and Mom were busy providing for me, I made you suffer.

I remember the night you told me to get out of the house. Mom cried silently, but refused to interfere, aware that it would probably cause more damage. In the heat of anger, I left home with one backpack slung over my shoulder, and you didn't stop me. Instead, you slipped away into your room, defeated.

Eventually, Mom found out where I was staying and, in a tired voice, she asked me to come back home. When I did, she burst into tears and told me that 1 was killing you. Every day, she said, you came home and walked straight toward the cupboard where the alcohol was kept. The condition of your liver worsened, but you didn't care. Drinking cased your mind and washed your sorrows away. You didn't say much to me when I came back, but Mom told me that you cried for the first time in a long time while I was gone.

Looking in the mirror, l saw an unhappy girl, fraught with anger, confusion, and guilt. l was headed in the wrong direction, and deep down inside, I knew that you were right. I needed to take control of my future. I needed new friends. I needed to start living for myself and not for others. At twenty-one, I haven't finished growing up, but I'm changing for the better. Aware that all of my actions have consequences, I now know that if I'm not careful, life can easily turn into a reckless roller-coaster ride.

During the last couple of years, since you've been fighting your illness, we've switched roles. Now that you are weaker and more vulnerable, I've taken on some of your responsibilities. I seldom have time to hang out with friends because I'm so busy helping you and Mom buy this or pick up that, but I don't mind. It's my turn to take care of you. Sometimes I feel like the cancer is my fault, and that your drinking was intensified by my wrongdoings, but I've gradually learned to change my perspective. Dwelling on the past is pointless, and right now, I just want to make sure that you're healthy today and tomorrow.

Thank you for your unconditional love, and for saving me from following the wrong path in life. You never wanted to give up on me, and you have done everything in your power to see me grow up to become a responsible and caring adult.

ln the past our struggles drove us apart, but now, our experiences have brought us closer than ever. l will never lose hope in you, Dad, just as you never lost hope in me. I love you.
```

---

## IC-0177: In My Hands

- Title: In My Hands
- Author (byline): Irene Gut Opdyke
- Work: Not specified
- Publisher: Knopf
- Publication date as stated: April 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1219
- Already set (do not supply): none

### Source block (context only)

```text
Author: Irene Gut Opdyke
ISBN: 978-0679891819
Publisher: Knopf
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
Irene Gut Opdyke received international recognition for risking her life by aiding and saving Jews during the Holocaust. She was presented with the Israel Medal of Honor, Israel's highest tribute, the Vatican has given her a special commendation; and her story is part of a permanent exhibit in the United States Holocaust Memorial Museum in Washington, D.C. Ms. Opdyke began to share her story only recently -- after hearing the Holocaust denounced as a hoax or propaganda. She now travels the country, speaking to groups large and small, old and young.. This is her story . . . In My Hands by Irene Gut Opdyke
```

### Performance text (classify this)

```text
NOTE: Should be presented with a pronounced Polish accent as an elderly woman recounts her memories . . .

I was twenty, and it seemed as though half my life had been wartime. Sometimes I felt like an old woman. I had seen terrible things, and terrible things had been done to me

Often—such as when a German officer made some rude, suggestive comment, or when I saw a child in the street who looked particularly thin and hungry—often I felt a great welling up of hatred and rebellion. It was not right, what I had seen and what had been done to me, and what I saw around me every day. In God’s name, it was not right! And yet I was relatively safe. I was well fed. I had my sister Janina with me. I knew that most people were not as well of as I was. If I felt so much anger and outrage, what must other people not so fortunate be feeling? Surely, the evil being done in my country must be a poison that would ruin the soil, tarnish the air, and foul the water. Sometimes, when I thought of the amount of hatred dwelling in Poland, I was surprised to see that the grass was still green, that the trees still flourished their leaves against a blue sky.

And yet they did. It is a terrible irony of was, that nature itself does not rebel when man turns against his brother. I have seen nightmares take place on beautiful spring days. The birds can hop from one branch to another, tipping their heads and honing their small beaks against the bark while a child dies in the mud below.

One Sunday in July we found our friend Helen and her mother in a state of barely controlled hysteria. They had heard a rumor that a large number of Jews from the Arbeitslagers and from surround areas had been rounded up by the SS and were being held in a nearby village. Helen begged us to go with her, to see if she could find her husband Henry among them.

Janina and I did not have to confer. The four of us hitched a ride on a farmer’s wagon and were soon in town, at the bus station. There were dozens of people waiting for the same bus, and from the bits and pieces of overheard conversation, we knew that most of them were on the same fearful errand.

As we waited in the sun for our bus, rumor snuck like a pickpocket through the crowd, stealing the hope from people’s hearts. At first, only isolated words stood out against the general murmur: Camps. Disappeared. All. Death squads. Then we heard whole phrases: Burned the synagogue. Shot the men. Orders from Berlin.

All of us in that crowd were fearful of what lay ahead, and yet when the bus finally came wheezing and grinding its gears down the street, we rushed forward as one body. The bus filled. It pulled away. We were all on it.

There was very little tlak as the bus made its way to our destination. There was nothing to say. When we arrived, we climbed down onto the hot pavement, and as if by some secret signal, like a flock of sparrows wheeling away across a church square, we all moved in one direction.

It was in the marketplace. The whole square had been fenced off. Behind the barbed wire stood hundreds of people whose yellow stars marked them as Jews. Trucks were unloading scores more, and as each man, woman, or child jumped down, bewildered and frightened, the black-uniformed SS men sorted them roughly: women and children one way, old men another, young men toward another mass of trucks. Outside the fence, friends and family members pressed against the wire, calling out names , crowding for a glimpse of a loved one.

Suddenly, several of the guards strode toward the fence, shouting at the crowd. “Raus! Raus verfluchte Schweine!” One of them slung the gun off his shoulder and began shooting into the air.

There were screams on our side of the wire, and people stumbled into one another. Some would not be chased away, but kept pressing forward. The man with the gun leveled it at us, and we broke in panic. We were all running, but when I heard Janina cry, I turned to help her.

“I’ve twisted my ankle!” she hasped, struggling to her feet.

Helen and I took her arms, and the four of us dodged through the crowd to a row of building lining the square. We slipped down an alley, and I found a door that stood ajar. Putting my shoulder to it, I shoved it wide, and we all hurried inside.

It was a house. It was someone’s house, but no one lived there now: furniture was broken, scattered across the floor. Broken dishes and glassware lay in piles, and dark squares on the wallpaper showed where pictures and paintings had been taken down.

“This is a Jewish home,” Helen said, turning around and around amid the wreckage. “This house has been raided.”

We heard more shouts and pounding footsteps on the street outside. Without speaking, we ran up the stairs and into a front bedroom. Janina hobbled to a window, and stood with her back to the wall so she could peek out sideways. We all did the same. We did not speak, but our hard breathing was loud in the empty room.

Below in the marketplace, the SS men had lined up facing the Jews, their guns gleaming in the sun. “Raus, Schweinhundjude! Schnell! Schnell!” Out Jewish pigs! Fast! Fast!

The gates were dragged open, and the Jewish prisoners were forced out through a gauntlet, while the guards beat at them with their rifle butts. And old man, tottering with a cane was not fast enough, and a guard shot him on the spot. In vain women tried to protect their small children from blows, men tried to shield their old fathers. But every time someone stumbled and fell under the beatings, shots rang out. The street was paved with bodies, and still the Jews were forced to march out over them.

We watched this from our windows in a paralysis of horror. We could do nothing but watch. We could not even pull back from the glass to keep hidden. An old rabbi carrying the Torah stopped to help a young woman with a shrieking toddler, and all three were shot. A graybeard in a faded uniform of the Polish army form the last war limped past the guards, and he, too, was not fast enough. The sun shone down on all of them, and the dust settled in pools of blood.

By this time, the four of us were crying uncontrollably. Helen was on her knees, sobbing in her mother’s arms. Janina turned her face away. But I watched, flattening myself against the window. As I pressed against the glass, I was an officer make a flinging movement with his arm, and something rose up into the sky like a fat bird. With his other hand he aimed his pistol, and the bird plummeted to the ground beside its screaming mother, and the officer shot the mother, too.

But it was not a bird. It was not a bird. It was not a bird.
```

---

## IC-0178: Incendiary

- Title: Incendiary
- Author (byline): Chris Cleave
- Work: Not specified
- Publisher: Anchor
- Publication date as stated: Sept 2006
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: WIFE, HUSBAND, RADIO ANNOUNCER, BOY, MENA, NURSE
- Teaser before the introduction: Yes
- Spoken words (computed): 2004
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Cleave
ISBN: 978-1400096688
Publisher: Anchor
Date (Month/Year): Sept 2006
```

### Introduction (context only: never use it for content warnings)

```text
On July 7, 2005, during the morning rush hour, four bombs were detonated in the center of London killing 52 and injuring over 770 others. Three IED’s exploded in underground stations and the fourth on a bus. The attacks were inspired by al-Qaeda and its ideology.

On that same day, Chris Cleave's debut novel was published: the fictional story of what happens after a bomb kills more than 1,000 people in a London soccer stadium as told through the eyes of a young mother. It is hard to imagine an uglier “literature echoes reality” coincidence.

Incendiary by Chris Cleave
```

### Performance text (classify this)

```text
WIFE: (Pg 29-30) (to husband) I wish you wouldn’t take the boy to the game. He’s too little. The violence makes me nervous.

HUSBAND: (laughing) Crowd violence at a football game. That’s a laugh considering I defuse bombs for a living. Listen love, football crowds aren’t how they used to be. It’s a family game now and anyway I’m a copper. I’m a big bloke I can handle myself.

WIFE: It’s not you I’m worried about. It’s the boy. He is 4 years old [and] still sleeps with Mr. Rabbit. (holds and interacts with Mr. Rabbit throughout the selection) (Pg 11) (to audience) I sewed Mr. Rabbit myself he was purple with green ears.

HUSBAND: (Pg 30) Oh for Christ’s sake, said my husband. You think I don’t look after him? You think I’d let anyone touch a hair on his head? I’d kill them first.

WIFE: Alright. But it still makes me nervous.

HUSBAND: Everything makes you nervous.

WIFE: (to audience) And he was right. Oh, god, he was absolutely right. I could feel death rushing towards us. (Pg 39-40) It was May 1st and the sky was blue and it was nice and warm just like you want it to be on May Day. My husband was carrying the boy on his shoulders and both of them were grinning like idiots. They were wearing their Arsenal shirts because it was Saturday -- the big day. They climbed in our old Astra and drove off. I never saw my husband or my boy again.

RADIO ANNOUNCER: (Pg 73) THE NUMBER OF CONFIRMED DEAD FROM THE MAY DAY ATTACK HAS RISEN TO 966 WITH DOZENS MORE STILL MISSING OR IN CRITICAL CONDITION.

WIFE: (Pg 76-77) They reckon 200 people died straight away -- blown to bits by the fragmentation bombs. I hope my husband and my boy were part of that 200. That’s a funny thing to say isn’t it? But that is what I hope. Because the 200 people who died straight away didn’t have to suffer.

After the first blast anyone who could still run did run. There was an inferno. Phosphorus raining down all around. It set fire to the seats. To the stands. To the clothes and skin of the fallen bodies. They reckon 500 people were crushed and burned to death while fire rained down. They would swing open the ambulance doors and blood would be an inch deep on the floor. They said some of the (pause) things (pause) that arrived on the ambulance stretchers didn’t really look like anything.

Dear Osama . . . (Pg 73) They kept calling it The Catastrophe. The BBC never did work out what to call the thing you’d blown up. After days of calling it the Emirates Stadium or Gunners Park, they gave up and started calling the whole thing May Day. Everyone did. Like you hadn’t just blown up a football ground you’d blown a hole straight through our calendar. I felt like I’d fallen through the hole.

BOY: (Pg 228) Mummy . . . Mummy, why don’t you help me?

WIFE: (Pg 4) You can see what a boy really is from the shape of the hole he leaves behind. I want you to feel that hole in your heart, Osama. Stroke it with your hands and cut your fingers on its sharp edges.

(Pg 163) Everything happened in the spring and it never stopped for one second. It was dirty and sad and anyone who wasn’t blown up and burned -- It was like we all became animals again. You could look at people on the bus and you’d almost see the fur bristling under their nice clean clothes. After May Day everyone was nervous. It wasn’t just me anymore.

(Pg 27) They say you are a FIEND, Osama, but like I say I don’t believe a word of it. I’ve seen you in your videos. You give me the shivers and you look like a gentleman. They say you believe in paradise. They say you believe that if your people kill anyone innocent then you’re doing them a favour because they will go to be with Allah. I wouldn’t know about that. My husband didn’t believe in Allah he believed in his kid and Arsenal football club.

(Pg 27-29) I always liked the football but my husband and my boy were mad for it. The fun used to start the night before. Before we put the boy to bed my husband would run around the flat with the boy on his shoulders. They would sing *1 NIL TO THE ARSENAL till the upstairs neighbours banged on the ceiling. After the singing the boy would be laughing and giggling like a lunatic. We couldn’t get him to sleep. (flashback to a memory)

BOY: Mum! Mum, mum, mum, come quick there’s something in my room.

WIFE: What is it? I’d say.

BOY: Nothing (giggling) I fooled you!

WIFE: (to audience) He was 4 years and 3 months old. You couldn’t be cross with him. That boy had such a beautiful smile. He was just pleased to be alive. (to boy) Go to sleep, little monster or you’ll be tired for the big game.

BOY: But I’m not sleepy mum,

WIFE: Go to sleep or I’ll have to fetch your father.

BOY: I’m not scared of him! My dad is the best dad in the world! He’s better than. Than. Than.

WIFE: Than what? Eh, little monster? What’s your dad better than?

BOY: (erupting in giggles again) Monkeys! My dad is better than monkeys!

WIFE: (Pg 11) (beat, then to audience) In the night my boy’s room smelled of boy. Boy is a good smell it is a cross between angels and tigers. My boy slept on his side sucking Mr. Rabbit’s paws. He went everywhere my boy went. (Pg 37) I’ve gone through a lot of changes since then Osama but if you looked very carefully and the light was right, I expect you could still see the memory of that happy time in me. Hidden but not quite invisible (beat) (Pg 11) Mr. Rabbit survived. still have him. His green ears are black with blood and one of his paws is missing. (beat) (Pg 101) A lot of things survived because they were trapped under bodies.

(gasp)

(Pg 29) It sounds silly, Osama, but sometimes I’m pleased your people blew them both up together. (Pg 117) All they found was their teeth and Mr. Rabbit.

(Pg 311) The only thing going through my head? My boy screaming with Mr. Rabbit in his pocket and his Arsenal shirt in flames.

BOY: (Pg 262) Mummy, save me!

WIFE: (Pg 295) (puts hands to her mouth to stifle a silent scream) His lovely ginger hair burned. Thick black tar dripping down his face. His skin raw with burns and one of his eyes boiled white as an egg.

(Pg 209) Mr. Rabbit stained black with my boy’s blood -- scars where his skin had burned through and his stuffing roasted brown and hard as crackling. (Pg 137-138) [They say] the Arabs are different from us. In the Iran/Iraq war they sent children to walk across the minefields. To clear a path so the grown ups could go and gas each other. They gave each kid a little metal key to paradise. The kids hung those keys around their necks. The grown-up Arabs told the little Arab children that there weren’t enough landmines to send all the kids to paradise. So the little children actually ran. Kids will believe anything you tell them . . . (long beat) (Pg 71-73) Well Osama I sometimes think we deserve whatever you do to us. Maybe you are right maybe we are infidels. Even when you blow us into chunks we don’t stop fighting each other. I suppose you were sitting out on the rocks before dawn listening to the goat bells when one of your men came over to you. Did he say, “Hey boss turn on the radio! We did it! We blew up Arsenal’s shiny new stadium1” ? Did you smile? Did you turn on the radio and listen to the death toll rise? (beat)

I fell unconscious and I stayed that way for 3 days. When I woke up in hospital. The sheets were very stiff and white. The radio was on in the ward. 912 dead it said. At first they said 700 dead but it went up and up. The survivors wouldn’t stop dying you see. They had so many bits blown off them they couldn’t really help themselves. There was a BRAVE 82 YR OLD GRAN in the bed across from me. She’d lost both eyes at the stadium and she was singing 1 NIL TO THE ARSENAL again and again and again. (covers ear, cradles Mr. Rabbit and wimpers, then gathers herself to continue the story)

(Pg 86-88) Mena was my favourite nurse. She was a nice girl. She was from the East. Kazakhstan or Uzbekistan or one of those Stans anyway. She’d sit on the end of my bed and we’d watch the sun rising. Mena used to hold my hand while we looked out over the city.

MENA: So many people down there. So many people under this sunrise. And all those people want is to get through today.

WIFE: Mena was like that. Philosophical. (contemplative beat) I’d definitely of killed myself if it hadn’t of been for her. (beat) Each morning [we] watched what they were doing to London. First, they stopped boats using the river. They just stopped them so you couldn’t blow up the Houses of Parliament, Osama. They drained the life out of the river till it was just an empty vein with police boats drifting up and down it like white blood cells. (Pg 102) For a whole week after May Day the airports stayed closed.

(Pg 88) What really changed the view though was the barrage balloons shining silver in the rising sun. It gave me the shivers. Mena gripped my hand and I could see the goose bumps on her arm.

MENA: This is grotesque. The world has gone crazy.

WIFE: It makes sense to me. I reckon it’s to stop them flying planes into the tall buildings.

MENA: (Pg 89-90) We turn London into a fortress? As if that could possibly stop the terror.

WIFE: (to audience) I could feel Mena’s hand trembling. I watched a tear run down the side of her nose. It stopped on her upper lip. (to Mena) If you had kids, you’d be all for anything they can do against the terrorists. It doesn’t matter if it’s logical when it’s your own kids.

MENA: It matters if you’re Asian. Look, my family is Muslim right. Do you have any idea what it’s been like for us? I don’t think you can imagine how it feels for me just to walk to work since May Day. To see the hate in people’s eyes when they look at me. I have become the enemy. There’s this one cafe I walk past on my way here. This morning this old man, he must have been 80, was reading the paper and the headline on the paper was THE CRUELTY OF ISLAM. He looked up when I walked past and he sneered at me. He actually curled his lips. That is the nature of this madness. It fills the sky with barrage balloons and people’s eyes with hate.

WIFE: (Pg 91-92) Mena gave me this lovely smile and touched her right hand to her heart.

MENA: I must go . . .

WIFE: I’ll see you tomorrow. (to audience) But I didn’t. In fact, I never did see Mena again. The next morning the sun turned up just like normal, but Mena didn’t. A new nurse came instead. (to nurse) What happened to Mena?

NURSE: They stopped her working. Muslim wasn’t she? Security risk. They suspended all of them from working as of midnight. This country’s finally starting to get it. Don’t get me wrong. I’m sure 99 percent of the Muslims are fine but if you can’t trust some of them you can’t trust any of them can you?

WIFE: But they can’t just stop all the Muslims from working.

NURSE: Oh, they haven’t. Only the ones who fly planes and work in hospitals or have access to information.

WIFE: (with great sorrow) The new nurse didn’t hold my hand. She didn’t watch the sunrise with me. (Pg 136) You really think it was Islam that killed my husband and my boy? [Mena] was the gentlest woman I ever met. Her god wasn’t a bombing god.

BOY: (Pg 271) Mummy, why are you crying?

WIFE: (to Mr. Rabbit) Mummy’s not crying darling. Mummy’s fine. She’s just got something in her eye. (Pg 235-236) Before you bombed my boy, Osama, I always thought an explosion was such a quick thing but now I know better. The flash is over very fast but the fire catches hold inside you and the noise never stops. . . I live in an inferno where you shiver with cold. This life is a deafening roar . . . but listen. You could hear a pin drop.
```

---

## IC-0179: The Insanity of Mary Girard

- Title: The Insanity of Mary Girard
- Author (byline): Lanie Robertson
- Work: The Best Short Plays 1978, Pgs 66-99
- Publisher: Chilton Book Company
- Publication date as stated: Jan 1978
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: FURIES, MARY, WARDER, MRS. LUM, GIRARD
- Teaser before the introduction: Yes
- Spoken words (computed): 1991
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lanie Robertson
Book: The Best Short Plays 1978, Pgs 66-99
ISBN: 978-0801966422
Publisher: Chilton Book Company
Date (Month/Year): Jan 1978
```

### Introduction (context only: never use it for content warnings)

```text
In the late 1700’s women were expected to be dutiful, subservient housewives, to take care of the children, and to keep order in the house. Men made all the decisions; women were simply expected to listen and obey. Divorce was not an accepted practice. But if a woman behaved in a way that opposed her husband or brought him dishonor, he could legally have her declared insane and have her committed. In the 1700’s many perfectly sane women ended up in asylums.

Mary Girard was both an opinionated and outspoken believer in equality. She railed against unjust practices. Today she would be called a leader; but in her time there were just vague whispers about . . .

The Insanity of Mary Girard by Lanie Robertson – based on a real-life story of a woman who spent the last 25 years of her life in a mental institution.
```

### Performance text (classify this)

```text
Mary Girard is bound in the Tranquilizing Chair – used for “excitable patients” who were believed to be insane. Leather straps bind down wrists, arms, chest and ankles. A square box swings down over the head. Mary is a very attractive woman, 29 years old. The Furies circle the chair and lift the box. Mary seems, at first, asleep or in a coma. Then she becomes agitated and strains against her bonds.

FURIES: (Pg 67) (tauntingly) Mary. Mary Girard. Mary. Girard.

MARY: (screams) Who are you? Stay away from me! No! Let me out of here. Set me free at once!

FURIES: Oh. She's so. Indignant. Quite the fine lady. Isn't she? No one would think. Her husband was. Well-to-do. Would they, Mary?

MARY: (Pg 68-69) Who are you? What are you? Tell me.

FURIES: We're no one. Nothing. Inmates of the asylum. Like you, Mary. Figments of your imagination. A puff. A poof. Of nothing. Nothing, nothing. (setting MARY free)

MARY: If you are nothing, then I must be mad. I can see you, hear you. (grabs at them but they elude her) Tell me where I am? And how long I've been here.

FURIES: (disappointed) That's too simple. It's no fun. You know that already. The Pennsylvania. Hospital. The same. As it was. This morning.

MARY: But I'm not crazy. You know I'm not.

FURIES: You must be! Mr. Girard had you admitted. As a lunatic, paying patient. The doctors have agreed. To keep you here. As long as Mr. Girard. Continues to pay. Quite a lucrative account.

MARY: (Pg 69-70) (as the FURIES laugh at her frustration) It's all a misunderstanding. When I see the doctors, when I speak to Mr. Girard, it will all be corrected. It's a mistake, I tell you. And that chair. I thought I'd go mad.

FURIES: She will. In time. She sounds. Stark raving. Mad. That chair is one of the. Prized possessions. And inventions of. Dr. Rush. He positively. Loves it. And. So do we.

MARY: I couldn't move. I couldn't see anything. And then my eyes began to tear and I couldn't wipe them. And there was such a roaring in my ears. I thought I would go . . . that it would drive me . . .

FURIES: You were only here. Experiencing the effects. Of the Tranquilizing Chair. It's the. Proper treatment. For your type. Of madness. Dr. Rush. Has invented. Two appliances. To be used for. The treatment of. The mad. The gyrator. Or revolving machine. That shakes them up. The other is. The tranquilizing chair. For types like you. Ones subject to claims of. Sanity.

MARY: (furious) How dare you speak to me like that. I'm Mrs. Stephen Girard! I don't have to tolerate your taunts and jeers. (Pg 71) Tell me how to get out of here. Please. Please!

FURIES: We can only. Show you. You have to start. At the beginning. By seeing. The warder of. The cells. *****Scene*****

WARDER: (Pg 72-73) (enters, he is about Mary’s age) Here ye go. In here, Mary. That's yer name, ain't it?

MARY: (haughtily) My name is Mrs. Stephen Girard. You will call me by that name if you address me again.

WARDER: Oh no, I don't. I calls ye Mary. I was told by Mr. Girard hisself I was to so call ye.

MARY: You don't understand. I came to see the doctor about a personal condition. Where is he, sir? (pause) I demand that you take me to the doctor at once!

WARDER: Snooty, ain't ye? Wants to see the doctor at once, do she? Well, doctors don't come round at once. They're due sometime week after next. I guess ye'll wait till then, all right.

(exits the cell, closing the door)

MARY: (Pg 74-75) What are you doing?

WARDER: Lockin' the door to yer new home. It's customary.

MARY: You can't keep me here. Where am I? Is this a prison?

WARDER: That's real insultin', that is. This is the Pennsylvania Hospital. An' ye are in the ward fer the mentally deranged. The place fer lunaticks, in plain speech.

MARY: But I'm not a lunatic.

WARDER: That's not fer ye or me to say. That's fer Mr. Girard to say. He be yer legal guardian an' he's the one who put ye here. By law whenever a legal guardian says the one they's guardian over is lunatick then we picks 'em up and puts 'em here. We got lots of women folks here whose helpmates has writ out a little letter sayin' they's lunatick. Seems to happen more to women folks 'count of the delicacy of thar minds.

MARY: Well, this has to be a dreadful mistake because no one has examined me. My husband said I was to come with you to see a doctor.

WARDER: Yep. That's what we tell most of 'em. "Jest goin' to the hospital to see the doctor." Works nearly every time. Sometimes tell 'em they're goin' to see the dentist. Jest for variety's sake. Lots of crazy folks looks jus’ fine when they come in. I give you ‘bout a month . . . I won’t be able to tell you from any of those others. (exits; Mary cries; FURIES enter)

FURIES: (Pg 76) Don't be. Upset. Mary. Mary.

MARY: I have to get out of here. I have to see someone, talk with someone. When will they let me see someone?

FURIES: But we can let you. See anyone. Just name the name. And instantly you'll see them.

MARY: I want to see my mother. (FURIES exit, Mrs. Lum enters)

MRS. LUM: Madam, you sent for me?

MARY: (pleading) Mother, I need you. (Pg 77-79) My husband abuses me.

MRS. LUM: For shame that you should give him cause. And double shame that you be brazen enough to tell it. There is nothing unusual in a husband's abusing his wife. It is the woman's place to be clever enough to seem to do his will whether she do or no.

MARY: And must the wife always bend to her husband's will, whether it be right or wrong?

MRS. LUM: It is the husband's place to rule his wife. The woman's to obey her husband. It is the Law.

MARY: Whose Law?

MRS. LUM: God's Law. When you married you vowed to honor and obey your husband, madam, 'till death do you part. Do you dare question the Law of God Himself?

MARY: If this is God's Law, as you say it is, why didn't you explain this Law to me before I married Mr. Girard? I was sixteen years old!

MRS. LUM: You knew what you were doing. You got the home you wanted and much more.

MARY: I have nothing, Madam, nothing!

MRS. LUM: Then you can only blame yourself. A wise woman never lets her husband know the distaste she may feel for him. You should have dissembled more and hidden whatever loathing you may have felt behind a display of feigned affection.

MARY: I would have been a liar.

MRS. LUM: You would have fared better. (pause)

MARY: I asked you here because I have desperate news. (pause) I am with child.

MRS. LUM: This is wonderful! Nothing in all the world can do more to please a childless man. Mr. Girard must be overjoyed.

MARY: I haven't told him. I fear what he might do to me, mother. It is not Mr. Girard's child.

FURIES: (swooping in as Mrs. Lum exits) (Pg 84) Whose baby is it, Mary? Yes, tell us, Mary. Tell us who the father is. Tell us. Tell. Tell.

MARY: The father is unimportant. He was someone warm and affectionate to me.

FURIES: You were untrue, Mary. You betrayed your husband. And broke your marriage vows. For shame. Shame, Mary. You will give birth to an evil thing. Only evil comes from evil.

MARY: I don't believe it. I don't believe you. You're trying to drive me mad.

FURIES: (Pg 88) Oh. We got us some cures here, Mary. Icy baths in winter. Splinters under the thumbnails. A white-hot iron on the soles of the feet for sanity.

MARY: But they would not do that to me, for they know I'm sane.

FURIES: How could they. Possibly. Know that?

MARY: Because it's true. (Pg 90) Bring Stephen Girard. Bring him now into this cell.

FURIES: No, no. Oh no, we must. Not. We can. Not. No, no, no.

MARY: Bring him! *****Scene*****

MARY: (Pg 91) Why have you done this to me?

GIRARD: I had no choice. You are insane.

MARY: Don't lie to me, Stephen. You know as well as I that I am sane. (Pg 92-93) When we met, I was sixteen, a servant carrying water through the streets. I laughed at everything then. And I was happy without even knowing it. Do you remember that girl, Stephen?

GIRARD: She does not exist, madam.

MARY: No. We destroyed her, you and I. (pause) Didn't you ever love her?

GIRARD: (nonchalantly) She was pretty. People noticed her. She was innocent, a trait few women have.

MARY: Innocent! And then she married you and thought she had gained the whole world, and in reality gained only this little room.

GIRARD: She had everything she should have wanted.

MARY: The cost was too great. I was prepared to give you everything, but you wanted nothing. What good is reason without affection?

GIRARD: If you wanted affection, you should have told me instead of making a public display of yourself.

MARY: Stephen, I made no attempt to hide my behavior from you. We differed in only one way. I didn't bring my lovers under your roof. I always maintained a respect for you and your pride. Perhaps I should not have done the things I did. But in that I am not alone. (Pg 94-96) When I was childless you blamed me. I felt I had cheated you out of a son. But it wasn't me. You couldn't put life in my body! (pause) I got more warmth from a stranger than you could ever give. It isn't my child that is loathsome to you, Mr. Girard, but the freedom of my mind. May God have pity on you, sir.

GIRARD: God? (pause; very calmly) I do not know if God exists. If I thought he did I would pray that he keep you here forever. As I cannot be sure of him, I will see to it myself that you endure a hell on earth. (exits)

MARY: (shouting after him) All right! But my baby will live!

FURIES: She thinks her child . . . Will give her comfort. Not so, Mary. Oh no, no. No. You betrayed your husband. And broke your marriage vows. For shame. Shame, Mary. You will give birth to an evil thing. We will now show you what is yet to be. (FURIES place a bundle in MARY'S arms)

MARY: She is so . . . so lovely. (to the child) If I ever doubted that you were worth so much suffering, forgive me. (To FURIES who gleeful) Why are you . . . laughing . . . laughing? Tell me. She will live, won't she?

FURIES: Oh yes. Doubtlessly. Most definitely. The question. However. Is. How long? It will not be. A longish. Life. Months. Mary. Yes. Months. Five. Five months. Yes. Yes.

MARY: No! Oh no! My little one.

FURIES: Five months. Is. Quite enough. Then buried. In an unmarked grave. That you will have in common. Mary. You too will be buried in an unmarked grave. Here. On the hospital grounds. You'll never leave these walls. Mary.

MARY: Good! That at least I delight to hear. The sooner the better will best suit me. If God has any mercy it will be soon. Tell me.

FURIES: Oh no, you'll have to guess.

MARY: A year? Two? Five? Surely no more than five.

FURIES: Yes, five! So clever is our Mary. Five. And twenty. Twenty. More.

MARY: Twenty more? Five and twenty years? I could not stand it.

FURIES: Well, most of it. Will be. There. In this chair. The Tranquilizing chair. The restraining chair. Bound down. Like the evil. Thing you are.

MARY: No! No! God would not permit it. He would not keep me living here in this hell hole for five and twenty years. (praying) Please dear God, sweet, sweet Jesus, be merciful to me and let me not stay here for such an age.

FURIES: Oh, isn't she funny! God won't hear you, Mary. Why should He? He's too busy. Besides He's set you up for it. It's God's jest, Mary. And the fool is. You!

MARY: Get away from me! I won't listen to you. (shouting her prayer) Please God, please!

FURIES: He made you beautiful. And you made the mistake of believing in your own beauty. It's been your doing. And your undoing.

MARY: (still praying) God, help me. Help me! (Pg 97) Where are you God? Please answer me.

FURIES: (taunting) Please answer me! Oh. Where. Are. You. God. God. God.

MARY: Stop it. Damn you. All of you. Where is He? And who is He? Is He another man? Then I'll have nothing to do with such a God. Damn you, God. I damn you!
```

---

## IC-0180: Isaac and Rose

- Title: Isaac and Rose
- Author (byline): Jared Boticelli
- Work: Fast Horse Plays, Round One, Pgs 25-31
- Publisher: Fast Horse Drama
- Publication date as stated: Sept 2011
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ROSE
- Teaser before the introduction: No
- Spoken words (computed): 1533
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jared Boticelli
Book: Fast Horse Plays, Round One, Pgs 25-31
ISBN: 978-0615603681
Publisher: Fast Horse Drama
Date (Month/Year): Sept 2011
```

### Introduction (context only: never use it for content warnings)

```text
VOICE OF MINISTER: Dearly beloved, we gather here today to honor the memory of Isaac

Keller, a beloved soul who touched our lives in countless ways . . . His sister, Rose has

prepared a few words in his memory.

Isaac and Rose by Jared Boticelli
```

### Performance text (classify this)

```text
ROSE adjusts a microphone stand before tapping it and saying . . .

ROSE: (Pg 25-31) Is this thing on? (beat) That was a joke. Funny, huh? Ok, well, maybe not. I thought, you know, make some jokes, warm my audience up a little bit. Maybe I could be like a stand-up Helen Keller. Well, I can talk though. Sort of. (speaks very slowly and with much exaggeration) Can you understand me? You're nodding, so I guess that's a yes. Let me tell you the biggest joke, though. The fact that I'm the one up here. But they asked that I talk about him and I . . . (beat) The deaf older sister pays tribute to her genius little brother. That was another joke. Ha. ha. ha. They would call that poetic irony, right? (stares out into the audience)

They asked me to tell you about him, so . . . He started playing when he was three. Really. Would climb right up onto the stool and would stare at the keys like he was studying them, and he would make up little songs. I was eight, almost nine then, and these things (motions to her ears, indicating her hearing aids) still worked a little. I could make out some of the songs. The things he was able to do with the piano by the time he was five, six, seven. Our parents both played and they were letting him listen to Wagner, Tchaikovsky, Bartok. By this time, I heard less and watched more. How about a nine-year-old who can play? Ha. His hands were too small to play those big octaves, so he would (motions crossing her hands over each other, as if playing. Closes her eyes) Rachmaninoff's 3rd Concerto. . . that was the last piece I can remember being able to hear him play. (shakes off the memory)

Jokes. Yes, we, well, I, I was talking about jokes. Maybe God likes to do experiments sometimes and see how good he can make someone. Isaac -- this perfect little person. Sitting at that big black piano, he looked like that big piano could just swallow him up whole. . . . Or the math he did in his head. Foreign languages. They tested him when he was, I don't know, seven or so, his IQ . . . (her voice fades off and she gazes out into the audience, perhaps as if she sees him) How do you compete with that? To have that kind of talent and then to be that . . . good. A good person. Humble. Kind.

Let's say something about my personality. Bitter. Angry. Impatient. Then think of the opposite and that's Isaac. I think I was in 5th grade when my teacher told me, "You are so smart, Rose. So smart. But you are so angry." Yeah, (clears her throat, recomposes herself) jealousy is a bitter, toxic disease. A poisonous weed that grows without end. I am it's victim. Powerless to it. A disease worse than the fever that screwed up my ears when I was a baby or that shut down my (gestures towards her right kidney) Well, we will get to that. (pause) To really talk about Isaac I think I have to talk about me. (a small, mirthless laugh and then she speaks quickly, almost garbling her words) Self-consumed. Self-involved. Self-centered. Self. Self. Self.

(a memory comes to mind) We were fighting; well, not fighting, because he didn't do that. I was being a horrible 15-year-old, throwing a fit . . . he was 10, I'd had some crap happen at school and I was angry, like always, and he told me (beat) I understand you. And I told him. I told him you don't. I. . . God, I pushed him into the pool. I did. (gestures as if holding Isaac under water) I pushed him under the water. He was so small. And I, I held him there. I didn't let him up. (to Isaac) "Do you, Isaac? Do you "understand" me? This is how it is. Can you hear me?!" (gestures releasing him -- lets out a long, slow breath) And I let him up. He was okay. Shaken up. But okay. My parents, always the loving, supportive mother and father, comforting us both. And he said, "I love you, Rose." No. You don't. You shouldn't. (pause as another memory comes)

He drew a picture of us sitting on a piano bench on the beach, and you can see the ocean in the background. He's playing and I'm looking out towards the waves. We look happy. People are rarely happy. Maybe God makes more mistakes than we want to admit. (another steady, long breath before refocusing on the audience)

High fevers. Crap ears. Inside parts that don't work well. My parents should have asked for a refund. Or at least an upgrade. I guess that's why they got Isaac. Good for them. They deserved him. I mean that. For every award that Isaac won, I had a new doctor or a new issue that needed attention. And, then the big one hit. The kidney’s main job is to remove the toxins out of the blood and mine were just really tired of doing that. (holds her side and pauses) They put you on a list. And they tell you to stay strong and be patient. Which is great advice while your internal organs betray you and your body rots. Crappy body. Rarest blood type. Poetic irony.

You spend a lot of time feeling sorry for yourself, and you're angry and sick, and sometimes you yell at your little brother when he lies down next to you, and you drum your fists over his back. (pause) And sometimes you let him curl up next to you and feel his heartbeat. (gasps, suddenly and unexpectedly.) And you pray to God to be forgiven and to be a better person. And you watch your little brother play the piano and you wish, you wish that you could hear him.

Our parents take us to the beach. I try to be decent, I do. But I just keep thinking that it's like a movie about the angry, dying deaf girl who gets taken to the seaside by her loving parents and genius little brother and they all bond and she becomes Pollyanna and . . . I'm no Pollyanna. (pause) Isaac, a teenager now, and I were walking along the beach and he told me (she silently mouths, You're my hero.) And I told him (speaks with anguish, as if she can barely get the words out), "No, Isaac. I'm not. I'm not anybody's hero. I am so angry. You have everything. Everything!" And I ran as fast as a sick girl can, leaving him standing there. He didn't run after me -- He just stood there, looking out over the sand towards the water. Life sucks compared to the movies. People are rarely truly happy. (pauses and then smiles, almost garishly and cracks a joke) Two gnomes walk into a bar. (pause) This isn't really a time for jokes.

Soon after the time at the beach, my number came up. Ding ding ding! The sun is coming up and it's just my Dad and me driving to the hospital. And he says some things but he's driving, so I can't see his lips. His eyes water and he looks older than before. And I think, all of this because of me. And it seems so unfair. They suit me up and after a while, I'm floating into a place with dark, black pools of liquid, dreaming that my ears are perfect again and I'm listening to Isaac play. Then my body goes heavy and I give way to the darkest sleep. (pauses and closes her eyes, placing her hands at her side, near her kidney. Her eyes open) You wake through a dark fog. My parents are there. Both are crying. And it's the loudest sobbing, although I can hear nothing but the huge silence. My side aches. My mouth is dry as sand, but I can barely drink. I choke. Mom and Dad are at my bedside. Their faces are broken puzzles. I ask for Isaac. My brother. My Isaac. They are both crying now, and it's like a boiling river inside of me, because I feel him there. I cannot survive this. I thrash so hard that the IV rips from my arm, and I'm on the floor and they are holding me. I'm 3 again with a fever so high that I'm burning up, a field of fire, a desert of flames, and I wonder if a river of tears could carry us away, out to the ocean and will we find Isaac there, whole, unharmed. I sleep. I hope to not awaken. (pauses to recover from her tears)

(softly) Isaac knew that I would have said no, would have fought it physically if I'd known. My parents didn't even try to talk him out of it and they never blamed me. I don't really know how that's even possible. He had a reaction to the anesthesia and he . . . um, he went to sleep. He was 15 years old. And this is what's left (she gestures down at her side) This is the part of him that he gave so that I could stay alive. I wonder sometimes -- What was Isaac's last thought as he slipped into that sleep? Fear? Anger? Regret? I cannot understand that generosity of spirit. Maybe I am incapable of it. Isaac gave me his kidney -- I did nothing to deserve this. (beat) A great movie of the week. (a short, mirthless laugh) Oh God . . . (has to pause)

So, thank you all for coming here today, for him. But he wasn't much for taking credit. He got nervous before he performed. He was shy, humble. He was the strongest and most beautiful person I have ever known and I am trying to be a better person, a good person, to . . . (pause) honor him.

If I hadn't been so angry, so unwilling to be happy, maybe I would have [been able to] to explain to him how much I loved him. (looks heavenward) Thank you, Isaac. I love you forever and ever. I'm sorry and I'm remembering what you told me. You knew so much for a little kid. You told me, even though something is tough, it doesn't mean it's impossible. So, I'm trying. It's hard but I'm trying.
```

---

## IC-0181: It’s a Baby

- Title: It’s a Baby
- Author (byline): Cara Restaino
- Work: The Best American Short Plays 2005-2006
- Publisher: Applause Books
- Publication date as stated: December/2008
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CARA
- Teaser before the introduction: No
- Spoken words (computed): 2775
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cara Restaino
Book: The Best American Short Plays 2005-2006
ISBN: 978-1557837141
Publisher: Applause Books
Date (Month/Year): December/2008
```

### Introduction (context only: never use it for content warnings)

```text
Can a baby born in the worst of situations actually be a blessing that provides unity? What if a family that appears put-together is actually hurting and a traumatic incident is exactly what they need to overcome it? Cara Restaino explores these questions by telling of the opportunities she had in her youth to learn from her sister’s mistakes. It’s a Baby, by Cara Restaino.
```

### Performance text (classify this)

```text
This is intended to be performed by one woman. She plays all characters. Distinctions are made through varying focal points, shifting voices, and adjusting postures. Other methods of character portrayal are open to interpretation .

CARA: The Virgin Mary. The holiest woman in the Catholic religion. [Pause.] One day an angel messenger came to Mary and told her that she was going to have the son of God. Surprise, it's a baby! A pretty important baby ... Then, two thousand years later, there is Stephanie. Stephanie Restaino, my sister. Three years ago, my sister thought she had a stomach virus. [Pause.] My sister had a baby. She didn't know she was pregnant until about twenty minutes before she had the baby. This, however, was NOT a virgin birth and there was no messenger. [Pause.]

You see, you have to understand my sister. She is different, unlike any person I have ever known.

When she was little, my sister had trouble spelling. She was a little ... slow ... concepts didn't come as fast to her as they did to other kids or to me, for that matter. I was a fast learner. But not Stef. My mother took matters into her own hands had been trying to get Stephanie to learn how to spell three letter words and then, one day, while in the car, my sister made an announcement. "I can spell a word!" My mother perked up, could it be there has been some sort of recognition? Could she have mastered phonics?

"Sex! S-E-X! Sex! SEX!" My mother swallowed hard. My eyeballs nearly fell out of my head.

[Long pause.]

She could spell, we realized. Though, in addition to being a little on the slow side, my sister had a curious interest in the subject.

This incident ... spelling sex in the car ... began a sort of tradition with my sister that remains true today. No, no, we weren't shocked.

School, in general, was hard for her. She struggled with keeping up, but she didn't let that hold her back. What she lacked in intellect she made up in sheer originality, making her mark in other ways. She had spiky hair and lime green eye shadow. She went by the name "Donut"-she was "round and sweet."

While other kids applied to Yale, Harvard, and, well, Rutgers, my sister decided to follow in my mother's footsteps and become a chef. She applied to the Culinary Institute of America and got in.

Not long after my sister arrived at the CIA, she fell in love with Jason. [Pause.] Jason was a triple threat. By the time I got to know him, he had a criminal record for armed robbery, which led him to a year stint at Riker's, a child with another girl, and a life threatening blood disorder. Although she had a good heart, my sister had bad judgment.

And, at the time they met, my sister Stephanie was still Donut ... very round ... and sweet. And Jason wasn't interested in the girl who looked like she eaten a bakery. They were just friends.

One weekend she came home and announced she was staying. And then, she began losing weight, fast. By that time, my parents opened the restaurant and she was working all the time. She was down over one hundred pounds. And, by the time Jason got out of the big house, my sister wasn't as big as a house anymore. She looked amazing, and I am sure that when he saw her for the first time, he was more than surprised.

Needless to say, love blossomed. They were with each other night and day. He lived in Queens, so my sister was out there almost every weekend. "Be careful!" my mother would yell to her. "Watch what you're doing!" she would call. She wasn't talking about driving either. Even if my sister could spell sex, didn't mean she knew how to be responsible with sex.

In July of that same year, we took a family trip, Jason included, to Cancun. Well, my sister and Jason were sick the entire week. They threw up from one side of Mexico to the other. After we got back, every so often my sister would be sick again-throwing up, stomachaches, etc.

And by December she was looking awful. She had these dark circles under her eyes and her hair was getting curly, which was strange because she had this thick poker-straight hair ever since she was a kid.

Every once in a while I'd catch her throwing up in the bathroom and she would swear that her stomach was just upset. She'd say, "I don't know ... ever since Mexico I haven't been right. Maybe I have a parasite or something." And then she'd go outside for cigarette. She's a tough girl. She looks tough, she acts tough, she talks tough. I believed her. But the fact of the matter was that she looked like shit.

Months went by like this, and by January 2003, she was in a bad state. She was working twelve-hour days and her skin had turned the color of a cold, fried veal cutlet. She was gray. I told her to stop smoking, to stop the late nights out drinking with her friends and actually go to bed early, but she ignored me. And on the Saturday before the most insane week of our lives, she worked all day. She made two cheesecakes during the afternoon, worked the line, and spun pies in between. Her friends came in around nine o'clock and she cooked dinner for them too. By the time she sat down she looked awful. But she helped them polish off two bottles of wine and several packs of cigarettes before she and Jason went home.

The next day, around four in the afternoon, my mom told her, "Go home. You look like shit. It's just Monday night, I can handle it. If you don't feel better, go over to the Immediate Care Center or something. .. but call me."

Everything seemed OK until around eight when Jason called to say that they were headed to the Immediate Care Center because she was really in pain. "This Mexico thing really got her," he had said. "Alright, alright. Just call us when you finish."

About an hour later they called to say that they were on their way to the hospital. When she and Jason walked into the ER, my sister gave her name.

"I'm Stephanie Restaino. I have a.... " But before she could finish, the nurse ushered her in and Jason took a seat in the waiting room.

She was poked and prodded by several nurses and doctors. Then, finally, the doctor said, "OK, we're either going to take you to Labor and Delivery or surgery." "Labor and Delivery? For what?" "Well, you're having a baby."

"No, I'm Stephanie Restaino. I have a stomach virus."

And instantly, she was surrounded by six doctors and two crash carts and a lot of silence. They knew she was pregnant. They knew she didn't know she was pregnant. And as they examined her, they could hear a heartbeat, but couldn't find the baby. My sister, as I said, was very thin. When they laid her on the table, her stomach was concave. And as the doctor listened for a heartbeat. They weren't sure, but toxins were released in her blood flow, lethal toxins that could kill both her and the baby if the situation wasn't handled fast.

In the meantime, a nurse was sent to retrieve Jason, who still had his black leather coat on as he sat watching Fear Factor.

"Are you Jason? Stephanie's boyfriend?"

"Yeah."

"Come with me, please."

She led him to the emergency room, where my sister was waiting. The nurse closed the curtain and my sister had to tell him what was going on.

"Jay, I'm having a baby." "You're pregnant?"

"No, I'm having a baby ... now." And before she could say anything else, the curtain flew open and the nurses tore off her clothes and shoved them into an elevator.

They told her that she would have the baby in about twenty minutes.

"Wait! I have to call my mom! She has to be here!'!"

She had no drugs ... a completely natural birth, but it wasn't easy. The baby was actually situated up in her rib cage, which accounted for the lack of a belly. The doctors had to actually work her down-she didn't want to budge!

Nevertheless, shortly before midnight on Monday,January 13, 2003, at 5 pounds, the baby was born. A girl. [Pause.]

Oh! But that's not the end of the story.

My parent’s the phone rang.

"Yeah, Stef." My dad had answered it. "Mommy? Yeah, she's here. Hold on." [Pause.].

"Stef? Stef! Where are you? Are you still at the hospital?"

"Yeah, Mom, I'm at the hospital."

"Did they admit you?"

"Yeah, Mom ... Mom, listen to me. Are you awake?" "Yeah, Stef. I'm awake. What's going on?"

"Mom ... I had a baby."

"What?"

"I had a baby ... it's OK ... it's a girl."

Dead air. Silence.

"Mom? Mom, you've got to come up here."

"OK, OK. We'll be there in a little bit."

"Mom, I'm scared."

"I know ... " [Pause.]

"No, I'm scared that Daddy is going to kill Jason." [Pause.]

"I know." She hung up the phone and turned to my father. "Somebody wanna tell me what is going on?"

My mother was trying to find the words to convey this information to this man in the most direct way possible.

So my mom looked at him and said, [Pause.] "Stefanie just birthed a baby.”

In an instant my father was standing. "I can't! I won't! I'll kill her! I'll kill him!"

And my mother, now completely out of character, took charge of the situation. "Listen! Listen to me very carefully. She is your daughter. This is her baby. She's not the first. She won't be the last. It's 2003. Get over it." And she stormed out of the room.

And my father called after her, "Where are you going?"

"I'm going to wake Cara."

Now, let's go back to me. Remember me? I was so tired. I didn't go out that night so that I could catch up on some much needed sleep. Yeah, so me. I was all schnuggly-wuggly in my bed having good dreams ... pleasant dreams where my door doesn't fly open to reveal my mother is standing in the doorway ... yelling ... loudly ...

"Cara! CARA! Wake up!" "What ... what's the matter?"

"Get up! Your sister is in the hospital."

"The hospital? Is she OK?"

"Fine. [Pause.] She had a baby. It's a girl." And then she just turned around and walked out of the room.

A baby?!? What the hell was she talking about-a baby? I fumbled for my glasses and went into my parents' room. My father was sitting at the edge of the bed staring at the wall.

"Wait, I don't understand. She had a baby?"

"A baby. Yes, a baby. She had a baby. Now hold this, I need to call your uncle. Your father is going to kill Jason."

I stood there is disbelief. I didn't know what to do next. I looked at my father.

"Dad? ... Dad? ... DAD! You gotta snap out of this. It's going to be OK. Everything is going to be OK." [Long pause.]

He didn't look up. He didn't even blink. He just stared at that wall.

My father was going to kill Jason. Yes, I believe that wholeheartedly. As he stared at that wall he thought about all the horrible, torturous things he would do to him. I could see his fury being projected onto the wall ... he nearly burned a whole right through it.

My mother wiped her mouth and walked over to my father. "You. Get up and get dressed. We have to get to that hospital and see our granddaughter."

He didn't look up. He just stood and grabbed his clothes.

We piled in our cars and made our way to see Stephanie. No one in the car uttered a single word ... not a sound. But silently, feverishly we prayed for… Jason.

We literally ran into the hospital and my mother got to the nurses’ station.

[Out of breath.] "I'm Josephine Restaino. Stephanie's mom." The nurse smiled at her. "Your daughter is on the 3rd floor."

As we got in the elevator, we could feel the tension. And then my father began shaking his head. "They're on the 3rd floor." "Yeah."

"Well, that's not good. I was going to throw Jason out the window. The third floor won't kill him. He'll break his arms and then I'll really have to support him."

Ah, humor. Lighthearted humor. There was hope!

Once we got off the elevator, Jason was waiting. When he saw us, he completely broke down. We all did. Who could believe this was happening? It was surreal. My father was the first one to go up to him. Jason could barely lift his head. And then he extended his hand. But my father grabbed him. And he hugged him and we all finally felt like we could breathe.

He told us the whole story. How my sister almost died. How the baby almost died. How we were experiencing a miracle.

He led us to my sister, who was lying in bed with a blanket over her ... over all of her ... even her face. My mother stood next to the bed.

"It's OK." And then we all cried some more.

They told us that they had chosen to name the baby Angelina. "Awww ... ," I said, "Little angel."

Angelina had no health problems despite the fact that my cigarette-smoking, wine-drinking, pill-popping sister went through what the doctors say was nine full months of pregnancy without a single prenatal vitamin, let alone doctor's visit. And Angelina is the smartest kid I have ever seen, regardless of her parents' inadequacies. I guess two negatives do make a positive.

It's been 3 years. I should catch you up on what's gone on. My niece is fine. She's a lot like my sister ... reeking havoc. But she's smart, like me ... she can spell dog.

Jason left almost a year ago. Turns out he was having an affair with my sister's best friend. Shit happens. He gave her the best thing he ever could have ... Angelina. My mother, who swore up and down that she would never be a Nana, is indeed Nana.

And in the most interesting turn of events, my sister has become something I never thought she could be. She has handled motherhood with a sense of wisdom that overshadows anything that has happened in the past. She is a brilliant mother who loves her daughter with that innate compassion that they say girls are born with. She has it. I always knew that I could outscore my sister on any test. I could write better, I could add better, I could certainly spell better. But I don't know if I'll ever be half the mother that she is.

And my dad, my dad and Angelina are inseparable. In the hardest, most trying times I think that my father looks at Angelina and knows that somehow she was sent to save him.

And me, I've been given a rare gift. I have been able to travel back in time to see my mother and father as young parents-how they were with me when I was a baby. The years melt away when they are around Angelina and I can see them with a sort of immortality that defies fact that time marches on. [Pause.]

I try to rationalize things. Why this happened. Why she came and why she came in the way she did. How what should be a beautiful blessed thing can turn into a tragedy. And how it could have been a tragedy for us. And beyond some deep, philosophical message, I've only this. You needed a messenger. I'm not sure what would have happened if my sister didn't make it to the hospital. If we didn't get that crazy phone call that changed everything. Nothing has been the same since ... nothing has been the same, but it has all been for the better. [Pause.]

The Virgin Mary gave us Jesus Christ ... my sister gave us Angelina ... not quite the same thing, and yet she has saved us in a way. And if you would, hear this story. Listen to the message, from me, your less than angelic messenger. We can get ourselves into some difficult situations. But everything happens for a reason.
```

---

## IC-0182: Jewel

- Title: Jewel
- Author (byline): Joan MacLeod
- Work: Not specified
- Publisher: Talonbooks
- Publication date as stated: March 2022
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: RADIO, MARJORIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1688
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joan MacLeod
ISBN: 978-0889224605
Publisher: Talonbooks
Date (Month/Year): March 2022
```

### Introduction (context only: never use it for content warnings)

```text
In 1982, the world’s largest mobile offshore rig, the Ocean Ranger, was drilling for oil off the Newfoundland coast. Since its 1976 launch, the big rig had weathered over 50 storms; designed for 115 mph winds and 110-foot waves, and everyone thought it could handle the storm that was brewing too. But at 1:00 a.m. on February 15, 1982, the crew sent a desperate mayday call. Nearby vessels arrived only an hour later to find rescue impossible on the freezing, tall waves. Of the Ocean Ranger’s 84 crewmembers, only 22 bodies were ever recovered. Autopsies confirmed they died from hypothermia, and the 62 missing were presumed to have met a similar fate. They were never recovered. Marjorie Clifford was widowed that day; this is her story. Jewel by Joan MacLeod
```

### Performance text (classify this)

```text
RADIO: (Pg 72) To Connie Brown: Happy Valentine’s. Wish I could be there with love from Stanley . . . (Pg 73) To Sally Harper: Happy Valentines. You are my one and only, love Frank . . . (Pg 71-72) and that's it for Message Time tonight. Happy Valentine's. And snuggle up to the one you love because it's a chilly thirty-three below in Fort St. John tonight.

MARJORIE: You hear that, Harry? Cozy up. (Marjorie turns off the radio and as she gazes at her wedding ring, she remembers) (Pg 69) Valentine's 1979. . . His face: high cheekbones, lashes like a woman's, black hair sticking out in a million directions. And at six minutes to midnight, he asked you . . . "Marry me, Marjorie." There's this land he's wanting to buy and no money for cattle yet, but the oil patch is right around the corner. He's got his welder's papers. The money will flow. Maybe five winters of working out then fulltime farming or ranching. He talks about buying a milk cow and you nearly pass out with the romance of it. Valentine's . .

(Pg 79) [But] today I was at the Co-op in town, buying groceries. And this kid who's working there yells from across the parking lot, "Hey Mitchell! What's got four legs, is three hundred feet tall and goes down on Newfoundland?" And this kid Mitchell looks real embarrassed because he knows who I am. I mean I am one hell of a famous widow, Harry. We're talking Time magazine. And this kid yells again, "What's a thousand feet tall, has four legs and goes down on Newfoundland?" This idiot, he yells it out (beat) "The Ocean Ranger!"

MARJORIE: (Pg 80-83) You know I always thought it was a ridiculous name -- the Ocean Ranger. When you first got the job, I panicked because I didn't know how to imagine you there. Usually, you were just up around Nelson and I knew I could jump in the truck and find you. But Newfoundland! Four thousand miles away. Right from the start it felt wrong. I mean we're supposed to be farmers and there you are out on this floating thing in the middle of the Atlantic Ocean. (beat)

When I got the call that you'd gone down, all I could think was that you were drifting, that you might get caught up in kelp or some current -- that you'd never arrive on something solid again. And I thought about that Harry, non-stop. Thought about that for fourteen months without a break.

I was living with my folks, and my mother signs me up for some god-awful thing called a grieving workshop. All this group stuff makes me mental. I mean this is a very private business if you ask me. Everyone wanting me to come to terms with this. And all I'm really wanting is for everyone just to leave me alone. Some church ran this thing and they're tossing scripture around like a volleyball. I mean as if that's going to fill my bed or help me make payments.

Okay, we got our money since then. After two years of drawn-out bullshit with lawyers and every time you open the paper, more stuff about the Ocean Ranger. [But] What I want, through the whole inquiry, is to narrow it down to one man. Leave me one man, up there on the top floor, behind some marble top desk. I want him to say "Yup, it was my fault -- the design flaws, the lack of survival suits, my fault about the evacuation procedure and that the lifeboats would've gone down in a lake. I screwed up. Big time."

I don't want to cause this man any harm. But I would like to place him aboard a drilling platform, after midnight in February, over a hundred miles from the coast of Newfoundland. An alarm calls this man from sleep and onto a deck that is pitch black and tipped over fifteen degrees and all covered in ice. The wind is screaming. Salt water and snow pelt his face. Nobody knows what to do. He is being lowered in a life raft with twenty other men, into a sea of fifty-foot waves. Then I would reach down and lift that man up from this terrible place just like the hand of God come to save him. Remove him from all that terror and certain death. I'd place him somewhere warm and dry. Take his shivering hand inside my own and turn his hand over and over and over. Until he sees it. His hand is the hand of God, and he could have gathered them all up. Saved eighty-four men from the North Atlantic. He chose not to. My sadness -- my husband's death -- it was hand-made by someone.

(Pg 84-85) Well, old friend. (MARJORIE looks at her ring) You don't have a heart and you don't have a memory anymore. I suppose that part's the truth. But I do. This summer . . . I'd just moved back here, and everyone was so worried that I'd go crazy again. And sure enough, that's when I started having these little night-time chats of ours. (long beat as she tries to reign in her emotion, then) *Damn* you, Harry! Dying and leaving me is about the most gutless thing anyone could ever do. (she breathes deeply and composes herself) That's called the Angry Phase, Harry. I think I'm starting to come out of it though. (beat)

I'll tell you a story. There is a guy teaching school here. He's a very nice man. Sort of shy. Or maybe it's lack of character. No. There's something quite good there. (Pg 86) His name is Gordon, Harry. His place is all cedar and the smell of wood makes me crazy. (She breathes in deeply through her nose, remembering)

That first winter with you in the cabin . . . We were just married, and I don't care a damn that there's no power or water and nearly no windows. That making coffee means half a day's work. But then I begin to notice everything; nothing is smooth, it's dark all the time, my clothes are alive with sawdust and the walls are alive with sap. So it starts. (Pg 89) Used to be I hated the night coming but it's alright now. I mean it's not out-and-out terror anymore. Not all the time at least. (She notices the time and shakes off the memory)

(Pg 87) Gordon asked me to stay overnight. But I didn't. I didn't stay overnight, but I did go to bed with him. I'm just telling you, not asking permission. Being held by living arms, brings home what a body must be like lifeless. How it is still your body that I know better than my own. All the women wanted the bodies found, all the families of the victims. I never thought it'd be like that. You'd think lost would be better than dead. A strand of hope, invisible thin. But it makes you crazy, never knowing a hundred percent. It was way harder in the long run.

(Pg 89-90) Just a few more things, Harry. Then I'm going to bed. They got me going to another widows' group twice a month. There's this one woman, around your mum's age. And she says that widowhood, it's like checking into a motel for one night. One night that lasts the rest of your life. Then this lady says that nothing feels like home anymore. It's like we're all just waiting to get to another place. And I thought -- right, Not that I think I'm going to another place. It's just that it feels like that . . . the waiting. (Pg 91) Sometimes I do feel like I'm just visiting here, not really able to get involved in anything. And very, very scared. But I’ll tell you something. I am beginning to feel again . . . I'm not just waiting, not anymore. Not held down by that sadness. I mean I know it's part of me, but it can't run the show forever. (MARJORIE looks at her ring) What do you think of that? My perfect jewel.

(She is again swept into a memory)

(Pg 92-93) Valentine's 1982. You are about to slam, face first, into such a storm. But not yet. Maybe it's still quiet out there, just for a moment. I hope so. It's just before noon. I come in the kitchen, the radio's on. And there it is. First one out of the gate, a Valentine's message, short and sweet and probably sent the day before but meant to be mine now. “To Marjorie Clifford . . . “ I carry it around inside, hold onto it all day. It sends me to bed warm. Loud and clear. You love me. You got through.

Then late that night another message, hand delivered by an embarrassed *police officer.* The rig has been evacuated. Evacuated. What does it mean? Bombed out villages, buildings. Living in an air raid shelter. Living. He has left the rig and is in a lifeboat. There is a bad storm, a fifty-foot sea. That's when I know. Anything that big and made out of water is a deadly thing. But don't think it or it will be true and my fault. My legs are weak. I grab hold of the counter and the kitchen floor moves like a raft underneath me. And there you are, clear as ice for a single moment. In a little boat, wearing that awful parka from Sears. The *police officer* catches me down on my knees on the cold linoleum. He shakes his head. This is very hard for him, trying to tell me that my husband is dead. But he doesn't tell me that. He says the rig has gone down and two of the lifeboats, but the third boat is still out there. That means you. I know it. But then this cop tells me not to have much hope. I should've listened to him. It would've made the next few days a lot easier. All that waiting and glued to the radio. (Pg 94) Then the names of the dead are read over the radio. [Nicholas Baldwin, Kenneth Blackmore, Thomas Blevins,*] Harry Clifford. Confirmed.

It's nearly midnight, Harry. Valentine's is coming to a close. Remember how I told you that first message sent me to bed warm? It's still there. A little bit. (MARJORIE removes her ring.) But wearing this forever. I don't think it's such a great idea anymore. (Pg 95) It always felt so mean that it had to be Valentine's Day, that it was the last day you were alive. But I'm not so sure anymore. This is what I'm sure of. You loved me. You got through.
```

---

## IC-0183: Jezelle the Gazelle

- Title: Jezelle the Gazelle
- Author (byline): Dominique Morisseau
- Work: Black Lives Black Words
- Publisher: Oberon Books
- Publication date as stated: April 2018
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JEZELLE, SPIDER
- Teaser before the introduction: Yes
- Spoken words (computed): 1400
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dominique Morisseau
Book: Black Lives Black Words
ISBN: 978-1786821515
Publisher: Oberon Books
Date (Month/Year): April 2018
```

### Introduction (context only: never use it for content warnings)

```text
In this selection three 12-year-olds make plans for an old-fashioned foot race – a race with all their parents and friends watching. You can’t get more childhood nostalgia and “American pie” than that . . . right? But race matters and so does perception and implicit bias.

Brian L. Wright explains*: Throughout the United States, Black boys tend to be viewed as troublemakers from a very young age. Adults often see Black boys as older and less innocent than their White peers (a practice called adultification), and their play is perceived as more dangerous and violent.”

Jezelle the Gazelle by Dominique Morisseau
```

### Performance text (classify this)

```text
JEZELLE - Black girl, 12-13 years old. Spunky. Sassy. Full of energy and wit.

JEZELLE: We was runnin' like the wind. Me, Rasheed, and Spider. Reason why we call him that don't match. We was gonna call him Skinny but it's already another Skinny J on the block and you can't do repeats. Rasheed say it's bad luck to kill a Spider so it's actually increasing his life expectancy for us to call him that so he liked it and it's cool.

We be racin'. Everyday on the block. Spider be third place always, but me and Rasheed be neck and neck. Last race was a tie if you ask me, but Rasheed swear he beat me. That's complete bull but wasn't no witnesses. "Get some witnesses!" I told him. So he did. Rematch. I'll be the only girl. It's cool, I'm used to it. I'm always the only girl.

Five dollar admission for the big race. That was Spider's idea. I tried to tell him you can't charge people for getting onto their own block. That's like what they did to the Indians and the Africans and whatever. But he say people willin' to pay. And if they willin', then it's stupid not to take it. If people wanna give you they money, it's like immoral or anti- American not to take it or whatever.

JEZELLE: The whole block start buzzin'. Race this Friday. Best runners in the 'hood. Come put yo' money down. Winner gets half of the pot. That was Spider's idea too. He say he get to keep the other half cuz chargin' people was his idea.

I'm gettin' that short sprint perfected cuz one day I'ma do Olympics. Gold medal baby. That's the long term. Short term I just wanna beat Rasheed. This was him against her. Pre-teen man against pre-teen woman. This is for Equal rights and Democracy. All women and men created equal. I'm like a Civil Rights runner. Game on.

No adults invited to the race, but we all got feelin's that they'll be watchin' from the windows. My mama offers to make me a "Jezelle the Gazelle" t-shirt. I tell her I don't do rhymes. That's corny. But she makes me one anyway. I got a feelin' she's not takin' this race seriously. This is life or death. This is for Democracy and Equal rights for the only girls on every block. This is for neighborhood pride and respect. This is for real. This is not a game. But Mama makes the shirt magenta. I love magenta. I wear it but I'm not smiling for pictures. A woman's gotta have her boundaries.

Race day comes. We in school just waitin' for the bell to ring cuz now other folks in class done heard and the $5 pot is up to like $100. I've been eyein' this new 10 speed at Greg's Bike Shop. It's magenta with yellow stripes. It's got Jezelle's name all over it. I'ma be rollin' that baby up the block right past Rasheed, like "Whassup yo! Need a lift???" I got this race.

Spider wasn't feelin' good this day. He kept walkin' slow and dragging his feet. He looked like something was type heavy on his mind. I asked him what was up. (BEAT)

SPIDER: We gotta move. To Cali. My aunt's house. My brother's in trouble. Some cops came by the house last night lookin' for him. He got these friends and . . . maybe they did somethin'. My mama said they the wrong influence. She can't take it no more. Said we gotta get out before they take us all under.

JEZELLE: It sounded like he was saying goodbye forever. I didn't know what to do. I just looked at him for a second. A really long second. Then I just kiss him. Right out the blue. Ain't even sure what came over me. I'm not the kissin' type. I was totally another Jezelle. I started to feel my eyes itch like they wanted to cry. But I didn't. Cuz I never cry. Not even when my heart is breakin'. I had a race to win.

Ready. Set. We was on the startin' line at the front of the block. Rasheed had gotten his hair cut. He looked fresh and clean. But so what. I had my magenta baby doll runner Jezelle the Gazelle t-shirt. My mama was lookin' through the window and wavin' --- CORNY. Another mama, one uncle, Skinny J's father, and Ms. Jefferson--they was all lookin' out their windows. Everybody was there. And almost 20 kids from school. This had turned into the biggest race of my life. I stretched my calves. Rotated my ankles. Grabbed my elbow behind my back. No mistakes.

Spider was gonna run too. Just for kicks. Everybody knew he was no match for me and Sheed. But he was just runnin' behind us, for ol' times sake. Burnt Skin Ernie was holdin' the banner at the other end of the block. I was keepin' my eyes on the prize. Skinny J called it: On your march. We corrected him. On your marks. Get set. I was sweatin' now. GO!!!!!!

We was runnin' like the wind! I could feel myself like elevatin' almost. My lungs was on fire. All sound disappeared. All I could hear was my own heartrate. My own feet bouncin' against the street. Didn't see Rasheed in sight. It was me! I was in the lead! I pulled in closer. Closer! BANG! My body tore through the sheet that said WINNER. I looked back to see the crowd cheering. I could hear their voices like sirens. (PAUSE)

But that wasn't cheers. That was screaming. And it wasn't a sound effect. It was real sirens. And Rasheed wasn't on my heels. He was behind me. Far far behind me. On the ground. Not moving. Not moving. Not moving. And Spider. . . Spider. . . wasn't in third place. He wasn't running either. He was on the ground. Not moving. Not moving. Not moving.

And the screams were sirens. And the sirens were screams. And there was a police on foot. And he had a gun. And I couldn't breathe. I couldn't even breathe. And I just sat on the ground. Not a winner. Not anything anymore. Just a runner gasping for air. . . gasping gasping for air. (LONG BEAT)

My mama cried and I didn't. She kept shaking her fists in the air. . . All I could make out was fragments. It sounded like she forgot how to speak in real sentences. "Those boys didn't do" and 'Just running a race." and 'Ain't all running from crime" and "Didn't nobody hear" and "Had the wrong boys!" and "Weren't even the same age!" I stopped listening and closed my ears. But sirens kept going. All night. All through my dreams. And I couldn't stop running.

(BEAT)

Two weeks after the big race, I went back to school. It was strange without 'Sheed and Spider. Everybody kept askin' me if I was ok. All the teachers kept askin' me if I needed to talk. I didn't say nothin'. I don't know if I'll ever say nothin' again.

My mama came to pick me up. She didn't want me walkin' by myself. Not while things are still so fragile, she said. Not while people are out there upset and confused. They killed Spider and Sheed. They were chasin' those boys that hang with Spider's brother. They said they went running around our block. They said they had just robbed a store. Nobody has seen those boys. They must be hiding good. But Rasheed and Spider. . . everybody saw. And the officers said they yelled STOP. Said they yelled it three times. But nobody heard nothin'. We were runnin' a race. Nobody heard nothin'. But everybody saw. (BEAT)

I still go to the track. One day I'ma do Olympics. Gold metal. One day I'ma be able to run without bein' afraid. But somedays still, when my feet are movin' fast and I can hear the wind in my ears, I look back to see who's runnin' after me. I look back to see who's left behind. I look back to wipe a tear from my eyes. . . even though I never cry. . . and then I look ahead and keep runnin'. For Rasheed. For Spider. For Equal rights. For Democracy. For the only girl on every block. For Civil Rights. And for everybody still in the race.
```

---

## IC-0184: Johnny Behind the Deuce

- Title: Johnny Behind the Deuce
- Author (byline): Lydia Lunch
- Work: One on One
- Publisher: Applause Theatre and Cinema Books
- Publication date as stated: 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SCENE, TIME, WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1021
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lydia Lunch
Book: One on One
ISBN: 1557837007
Publisher: Applause Theatre and Cinema Books
Date(Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
Johnny is covered in scars which are self inflicted. He cuts himself again and again. You may be wondering why someone would intentionally harm themselves. Many people who cut themselves, do this in an attempt to try and release all the emotions they are feeling internally. Others may feel so numb, that seeing their own blood when they cut themselves, helps them to feel alive because they usually feel so dead inside. Some people find that dealing with physical pain is easier than dealing with emotional pain.

Self-injury is also used as a way to punish oneself. Some people have such hatred for themselves and their bodies that they will carve demeaning names on their bodies as a way to remind themselves of how terrible they are. Whatever form of self-injury is used, the person is usually left with a peaceful and calm feeling afterwards.

The following selection; however does not focus on Johnny, but rather on Lydia and the pain she feels as someone who loves a self-mutilator, someone who wants desperately to help, but cannot reach into the depth of Johnny’s pain. Johnny Behind the Deuce by Lydia Lunch
```

### Performance text (classify this)

```text
WOMAN, late 30s, beautiful but weary, dressed in tight white slip and '50s-style Fredrick's of Hollywood high-heeled bedroom slippers enters stage right, finishing a cocktail. Soft amber light shadows the stage. Monologue is tender and reflective.

SCENE: A stage

TIME: The present

WOMAN: You can't save anyone from themselves. You will lose everything by attempting to play savior. You will never heal the wounded. You cannot repair the damage already done by selfish parents, vicious ex-lovers, child molesters, tyrants, poverty, depression or simply chemical imbalance.

You can't undo psychic wounds, bandage old scars, kiss away ancient bruises. You can't make the pain go away. You can't shout down the voices in people's heads. You can't make anyone feel special. They will never feel beautiful enough, no matter how beautiful they are to you. They will never feel loved enough, no matter how much you adore them.

You will never be able to save the battered from battling back at a world they've grown to hate. They will always find a way to pick up where the bullies have left off. They will in turn become bullies. They will turn you into the enemy. They will always find a new method in which to punish themselves. Thereby punishing you.

No matter how much you've convinced yourself that you have done absolutely everything in your power to prove your undying devotion, unfaltering commitment, and unending encouragement, you will never be able to save a miserable bastard from himself. The wounded will always find a way to spread their pain over a vast terrain, like an emotional tsunami which devastates the surrounding landscape. An ever expanding firewall which will singe everything and everyone in its wake. The longer you love a damaged person the more it will hurt you.

They will mock your generosity, abuse your kindness, expect your forgiveness, try your patience, sap your energy and eventually kill your soul. They will not be happy until you are as miserable as they are.

Then their incredible self-loathing will be justified by the perpetuation of a cycle from which there is little recourse. Once you enter their free fall, it will be virtually impossible to turn your back on them. You will be racked with guilt, frustrated by your own impotence and made furious forever buying into their bullshit in the first place. Of course the more damaged, the more charismatic. The more brilliant. The more sexually intoxicating. The more dangerous to your own mental health.

I have spent months, possibly years, comatose on park benches, tracking the periphery of playgrounds, skulking through shopping malls, falling asleep in the library trying to capture and trap a fleeting image.

The image of a young boy, at just the right moment in his life, that transient fleeting second when the right amount of natural light falls on the hollows of his cheeks, casts an effervescent glow, a splash of sunlight dancing on the lips, to rebirth within me, at least for an hour or two, that blossom of purity etched deep within their innocent smile.

There's something about how fine their bones are. Under their flesh. The possibility of shattering them under my need. Skin pulled tight around bony joints. The flattering reflection of my own beauty divorced of disease, my multiple sicknesses, a withering away abated. Transformed into a healing tonic, a sexual salvation, vacation from the devastation that has ringed the wellspring of my life.

Not that I could ever forget how much of my life has already been melted away. How much I gave up, gave over, wasted. How much has already been stolen. Destroyed. How many rope burns have left their browning residue around my heart strings. You don't have to fight yourself too hard to fall in love at least for half an hour, 20 minutes, 2 days, a week, with a young boy who finds in you the love they never found in their own mother's arms. And reciprocates it twofold. I'll play Mommie. I need to and I'm good at it. There's nothing to lose and what it is you gain is their life force, a transformation, resurrection, a reckoning, a day off from playing wet nurse in the trauma unit nursing damage junkies back to health.

But I'm too far gone now, too messed up. Broken down, battered. Nothing left inside my angel's saving graces, that busted little cherub with dirty feet and greasy wings whose tender ruby rich kisses have resuscitated so many burning embers and dying remains that I have become a mortician's re-animator, stuck forever in that purgatory limbo essence that so many dying men have come to rub their poison against.

Even my breath has become toxic. An aerosol taint of glue, sugar water, paint fumes, dead roses and runoff. But young boys don't know that yet. Don't see it, can't smell my true essence over the sweat of their own passion. Over the smell of their own vinegar, salt water taffy, dirty towels, steam heat. They wouldn't recognize it even if they did. They have no reference point. No landmarks. No track record. No wars under their belt.

No idea what it's like to inhabit this fleshy prison of blood and bones, entombed as if in an unnamed Nuremberg Cathedral which forty years later still remains swept to the side of a blood stained street, the bones of her confessional stacked helter skelter shattered under the steel rods, the rebar of the enemy pilot jets who blew in one day with the taste of her death on their breath, and in their wake, there she still stands, torn to little pieces praying to be glued back together again.

Praying for resurrection, for redemption. Praying with blind faith and stupid adoration to a cruel and vindictive god that does not exist, that one day the wounds will heal-That a dark angel will tumble down from the heavens, your name on his lips, and with a single kiss, the multiple fractures where memory and madness commit soul murder will cauterize. Will mend. Dissolve. But as with most prayers, I'm wasting my breath.
```

---

## IC-0185: Kennedy’s Children (Wanda)

- Title: Kennedy’s Children (Wanda)
- Author (byline): Robert Patrick
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: WANDA
- Teaser before the introduction: Yes
- Spoken words (computed): 2863
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Patrick
ISBN: 978-0573611261
Publisher: Samuel French, Inc.
Date (Month/Year): 1998
```

### Introduction (context only: never use it for content warnings)

```text
The Presidential motorcade is approaching now – the cheers are growing nearer. It’s a beautiful day here in Dallas, despite a light rain, and the people have turned out by the thousands to welcome their leader. President Kennedy’s political enemies warned that there would be hostilities and riots, but listen to those cheers! Yes, there is the motorcade, and there’s the President’s car; we can tell because you can see Mrs. Kennedy’s pink dress. They’ve left the bubbletop off the limousine in spite of the rain, so they can see the people, and the people can see them, and they love them! . . . . Then gunshots . . . . . . Kennedy’s Children by Robert Patrick.
```

### Performance text (classify this)

```text
WANDA: For me, it was the most important day of my life. I measure everything as happening before it, or after it. I remember every detail, every instant, every little bit of information as it came in.

WANDA: I was - at my desk. It was - lunchtime. The executives had gone out. I was in a hurry to finish page — 44! - of the - May-June issue of 'Salon Hair Styles.' Oh, not that I wrote it or edited it or anything. I just pasted the captions to the photos before they sent it out to the press. It was an exacting job though; I had to be very neat. One time I smeared some glue, and when we got the covers back for the January-February issue, the model on the cover looked like she had a runny nose. But, anyway, I was pasting up these photos, and the Fashions Editor kept interrupting me to show me her real Chanel suit from Paris-and I had to pretend to be interested because she drank something awful - I didn't drink in those days - and she was lifting up her skirt to show me how the hemline was kept in place with little chains sewn into the hem-and all I was really thinking about was my raspberry yogurt in the cooler section of the water fountain-and I had just had this horrible affair with this fellow who worked in the stockroom-and he hadn't shown up for four days -I was feeling really awful. (She looks out the window at the rain.) And I remember, it was a grey, grey day here in New York. And then-all of a sudden-all of a sudden Mr. Kanowsky, the Advertising Sales Manager. came bursting in! He was a little cross-eyed and always looked crazy. Anyway, he came bursting in, red-faced and excited, and he said, "Quick! Turn the radio on! The President's been shot in Dallas!"

Well, none of us believed it. I mean, none of us could conceive it. We just sat looking at him, and I guess we thought he was drunk or having palpita-tions-he was awful fat--and he said "Did you hear me? Turn on the radio!" So Carrie, the Accounts Payable lady, said, "Now cool it, Mr. Kanowsky, I'll turn the radio on," and he got a little frantic and said terrible things to her, and the Fashions Editor said a couple of unpleasant things to. him, and they were squabbling with each other right across me, and then Carrie's radio started up and the newscaster was saying-oh, I want to get this just right-saying, " ... reported that three Negroes were seen running from the overpass and two rifles have been confiscated in the immediate area," and how the President was going to be all right because they got him right to the hospital, and the Dallas Police were throwing a cordon around the entire area. And then suddenly we couldn't hear any more, because outside it seemed that every auto horn in the city had started blowing, and there was even a crash like somebody had driven right off the street onto the sidewalk, and the phones in the office began to ring-everyone of them, all at once, instantly, began to ring!

We all stayed at the office for the whole rest of the day, right into evening, with nobody working except Carrie, who didn't have any relatives. The minute you'd hang a phone up, it would ring again, and everybody who called was listening to a different station, and getting a different version, and people from other offices would pop in and tell us what they'd just heard and one man, a middle-aged, respectable man who ran the yachting magazine in the next office, came in bawling, just crying like a baby, crying, "Oh, my God, it's a Communist plot, it's the end of the world!" And the news kept coming in, and you'd get one picture of the whole situation straight in your mind, and then all of a sudden there would be this new piece of information and it would all change, and somebody would break down crying, and they couldn't find the Vice- President-they thought all the politicians were going to be assassinated and I don't know what all. And then, at last, very quickly afterwards, not an hour, I think, although it seemed so much longer, they said the President was out of danger and everything was okay. And then the bells starts ringing, every church bell in New York started ringing, and we knew that he was dead.

(She rises, goes to bar for a refill. After a pause.) I was the first one to say it. I was washing Lena, the Accounts Receivable girl's face, because she was crying and had smudged ink all over her face, so I was right by her phone when it rang, and I picked her phone up, and it was my mother, saying, "Wanda, come home! He's going to be all right! They just said so!" And the Fashions Editor fell out of her office with this big drunken smile on her face and a bottle in one hand, yelling, "J.F.K.'s gonna pull through!" And that's when the bells started ringing. And none of them were Catholic, so they didn't know what it meant, and they were all smiling and grinning like fools, and I said, "He's dead. The President is dead. God rest his soul." (Returns to her table.)

Within a few hours – do you remember this? -within a few hours one of the major magazines ha d a special edition out on the newsstands, and of course, within a few days they all did. Mr. Kanowsky ran around and bought everything, every paper, every magazine, he tape-recorded the radio stations, he even ran down-as soon as they announced the President was dead-he ran down and bought a color TV set-just ran down and came right back up carrying it. Puffing and red-faced. And we all watched-but it was all just chaos. Mr. Kanowsky has it all in scrapbooks, everything, all the rumors and confusions, and then all the-you know- Oswald stuff-and all the conflicting reports-and he was even taping from the TV later he didn't go home for three days-he was even taping the TV soundtrack-when Ruby-did that awful thing. When he sealed the truth off from us forever by firing a single shot--the lips of the one man who might have told us all about it, closed forever by one single little bullet shot . . . or was it two?

I couldn't go on working in that kind of job any more, after it happened. I remember the next night, walking along Broadway, and how weird it was to see the theatres all closed-and all these hundreds of color photographs of J.F.K. in the store windows. Somebody must have made a fortune selling those photographs because they were everywhere instantly or maybe people had had them all along and you just didn't notice them. It was like-like the sun had begun to eclipse. Everyone was scared of a chain of assassinations, or a war, but by the next day, nobody was afraid any more. That had passed, and it had become just--disbelief. In Saint Patrick's cathedral-or outside it, I never got in, the crowds were so big - hundreds of thousands of people were saying prayers for him. The whole world had loved him, you see, so much. The entire human race went into mourning. Kings and queens came to his funeral. All the TV channels had the same things on for four whole days. They even gave us the day off to watch.

It's ridiculous to talk about an event like that from the point of view of somebody like me. I mean, what difference does it make in the long run how I felt about it? I used my savings to finish another year at CCNY-that's City College of New York enough so that now I have my temporary teaching certificate and can work as a substitute teacher. I just thought-if all of us who believed in him don't go out and try to do some good, then his death was completely-completely in vain. Oh, of course I'm not comparing my little contribution to what he might have done if he had lived. If he had lived, he would have stopped the war. If he had lived, he would have solved the race problem. If he had lived, he would have found some way to bring us all together. I know that there are people who are cynical who say he didn't accomplish much in those-"Thousand Days"-but I always say to people like that, I say (With mounting anger.) "Oh, yes? Yes? Yes? Oh, yes? And exactly what have you accomplished?

Looking back to the first time I heard about him-and her-I remember that they had found a way of life we could all imitate. He worked so hard. He was inspiring, encouraging, and of course, so handsome and young - young for a President. And she . . . Well, I was always very fond of her, too. I don't look well, dressed the way she dressed, and I think maybe she let their publicity people-they had their own publicity people, you know-I think maybe she did let those advisors talk her into looking, well, maybe a little less distinguished than she might have looked. The Fashions Editor used to say, before it happened and even afterwards-she'd look at pictures of Jackie and she'd say, "She looks like a collage of Doris Day's wardrobe, Elizabeth Taylor's makeup, and Natalie Wood's hairdo." I don't think that was kind. I'm sure if she had been a private person, Jackie would have dressed with more restraint and taste. But after all, she was our ambassadrix to the world and I suppose she had to dress in a way that would appeal to people in the mass.

When they were alive - I mean when she was alive-when he was alive, you could never resist reading about them. He could read a half-dozen books a day, and he had been a war hero. And, you know, it was him that popularized the James Bond books. It's true. They weren't that popular at all until he mentioned to a reporter that he liked them and then, well, do you remember how suddenly everyone was reading James Bond? And she was very responsible for starting a certain "look" among young women. Politician's wives since her have all tried to dress nicely. And, oh, do you remember that record, "The First Family?" That was so popular. It had all sorts of jokes-good natured jokes, really-about him and her and his brothers and just everybody. Drugstores and supermarkets had stacks of it beside their cash-registers. And he wrote books, too, and one of them won the Pulitzer Prize, really, when he was still just a Senator. And she, when she was still a student, won the Vogue Magazine Prix de Paris for her article on "My Favorite Artists I Would Most. Like' To Have Known From The Past." They were remarkable people! Everything they touched turned to gold!

He was from a wealthy family, of course, but they had made their money themselves, and they were still, you know, rough, charming, brawling Irishmen, whereas she was from very "old money" as they call it, and she would have been a career girl, a photographer, if they hadn't met. They were so happy. They loved that musical "Camelot," the story of a distant, beautiful, forgotten kingdom where there was always sunshine and justice. Camelot. "Don't let it be forgot, That once there was a spot, For one brief shining moment, That was known as Camelot." Camelot. I think maybe we all had a glimpse of Camelot—once just once-in our own lifetime-before it crumbled.

They made "Camelot" into a movie, but it wasn't really very-I mean, it was just a medieval pageant, it didn't have the tenderness and the beauty and the sense of-you know-something that could really happen. And it was-you know-very sexy really dirty, for a musical. I didn't watch the second half at all. People don't seem to-I would have thought there would have been a lot of letters in the newspapers about it-about them messing up the President's favorite musical. But there weren't. I guess people had forgotten little things like that. In fact-when you walk down on Orchard Street, the pushcart street down in the Village where you can buy a lot of things cheap? Well, one time I was down there after some movie actress died-I don't even remember her name, although my mother was quire broken up about it-and they had replaced all the pictures of him with pictures of her. It was-horrible. You know how stores have the pictures in the frames they're trying to sell? I mean it's the frames they're trying to sell, not the pictures? Well, instead of having him in the frames, or even him and Bobby Kennedy and Martin Luther King-they had these pin-up photos of the girl who had just died.

Just because-well, not for any reason! Just because she had died! I mean people seem to remember, they seem to care, but they seem to have gotten things all mixed up

You hear stories now-and I don't mean just the stories about how it wasn't really Oswald who killed him, but it was really Johnson, or it was really Nixon, or Cubans, or oil millionaires, or Communists, or Ruby, or all of them together-or how the avantgarde threatre people put on all those awful parodies of Shakespeare-or how the sincere Shakespeare people in the park revived anything that had the killing of a king in it. I think some of those people mean well, but it sure is funny how they all do seem to be making a buck out of it-isn't it? No, I mean that you hear stories that make you wonder just how well people remember. I mean stories like-that Jackie was paid a million dollars to stay with him because they really hated each other. Or that they were both homosexual. Or that he had a movie-actress mistress. Or that he was in the pay of big industry, or-things that nobody could know, anyway, even if they were true. And you wonder: why do people even want to speculate about such things? When there's so much good to remember? When, above all, the beauty that never even got to happen is still there, waiting for us all to build! What right have they got to talk against her? How can they blame her for getting married again? My God, just to get away from all the people that try to make her into some kind of a pin-up girl, or clown! When she was there! Right there beside him! Closer than anybody in the world!

But there are some of us who still try-who still try to go on. My work-I'm going to have a full teaching license in just another three years-I'm work-ing with subnormal-what they call subnormal children, out in Jersey. It's very hard to try to help them into the world. They are of minorities, children whom the culture has forgotten, children of twelve who can't speak because they have never been spoken to in their homes, children who are afraid of things they can't even name, children without love or hope. Some of them may never be able to join the human race. But I can try. Today I mentioned to them something - something about him-and not one of them, not a single one of them, even knew who he was, It was, for a moment, as if he had never been. I tried to show them that famous Life magazine with the color photos of the-assassination-but it excited one of them too much, and two of the others just went crazy at the pictures of the blood-so, I wound up instead just telling them about Camelot. Without the sex stuff between Guinevere and Lancelot, of course. It's almost the same story. If I'd wanted to, I suppose I could even have told them the story of Christ, and it would have been almost the same story .

And yet, even after they understood the story, it was hard to make them see why it had all been so wonderful. There's no one like that now, they can't even imagine anyone like that, they're used to the idea that the world is just a swamp of violence and crooked politics and unexpected death and ugliness everywhere. They can't understand that there was time, a space of several years, when everyone loved someone, someone bigger and better than other people. They can't understand that all the people-everyone in the world-loved him. All. But one.
```

---

## IC-0186: Kindling

- Title: Kindling
- Author (byline): Cathleen Sakamai
- Work: Fast Horse Plays: Round 7, Pg 15-21
- Publisher: Create Space Independent Publishing
- Publication date as stated: Aug 2015
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHILD, SHE
- Teaser before the introduction: Yes
- Spoken words (computed): 1535
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cathleen Sakamai
Book: Fast Horse Plays: Round 7, Pg 15-21
ISBN: 978-1514339466
Publisher: Create Space Independent Publishing
Date (Month/Year): Aug 2015
```

### Introduction (context only: never use it for content warnings)

```text
Children depend on their parents to protect them and keep them safe. But unfortunately, this is not always the case. According to the National Children’s Alliance: More than 600,000 children are abused in the U.S each year.* But the ramifications don’t stop when a child is rescued from an abusive situation. While bruises, cuts, and broken limbs will eventually heal, emotional trauma takes a lifetime to overcome.

If only you could un-read those pages in your life’s book, or if there was a way to erase the images and flashbacks that come to your mind. Sadly, these traumas are burned into the very fiber of your being and sometimes scars never heal.

Kindling by Cathleen Sakamai
```

### Performance text (classify this)

```text
CHILD: (Pg 15-21) (pointing) Look at that girl's face, Mommy. What's wrong with her?

SHE is a woman in her late twenties to early thirties. She appears normally dressed, casual and calm. SHE addresses the audience directly.

SHE: I want to say (beat), I don't know, sweetheart. I don't know what's wrong with me. We walk around with our histories bolted to us like suicide bombs, like they could detonate in an hour or tomorrow . . . Or right now. You know what I mean, right? Do you ever feel like that?

SHE: She gave me an assignment. My therapist, that is. She said that I should write all of it down. And the "it", of course, was everything that troubled me. She told me to start small. Irritations, right? But there's so much that's irritating. And the more I started to think about what was irritating, the more irritated I started to feel about it, and then I started to feel like some kind of self-pitying freak, which I'm not, and . . . Okay. I'll just give you a couple off the list:

I'm irritated when I'm running late for work and the line at Starbucks is longer than usual, and I'm waiting and there's eight people in front of me, and it gets to the last person in front of me and she's gets up there to the register and she . . . she just stares up at the menu board thing like it's the first time she's ever seen it . . . and I think, "what have you been thinking about for the last ten minutes while we we're all standing here waiting?" She's standing there, it's like she's deliberating over a major life decision. I mean, I don't make this stuff up. And it makes me feel unkind, which I'm not, or I hope that I'm not at least, and . . .

Well, this sort of goes into this same one on the list, but let's say this same woman, right, this woman who takes fourteen minutes to decide on a tall mocha, she catches my eye as she leaves the register, and no matter how intensely irritated I am, I smile, because I always try to, and . . . well, she just looks away.

I'm not a violent person. Honestly. I catch spiders in water glasses in my kitchen and take them out to the backyard. But sometimes, I just want to slap people. Make them feel something, right? You smile at someone, some random stranger at the grocery store, or waiting at a light, or passing on the sidewalk, and they either just gaze back or look away. And I think, it just takes a millisecond. Just a blink, right? That's all it takes to move the muscles of your mouth to smile back. And people -- a lot of people -- they just can't be bothered to do that. But I try to make that effort. When people look at me. When they do. I don't want to lose that kindness.

So, I'm making my list, my canon of vexing issues, so to speak, and the list is growing longer and longer, and I'm realizing that all of these things, these terrible irritants are about other people. And that worries me, I guess. I start to think about what other people might put on their lists.

Would you put the leaky faucet in your guest bathroom on your list? I bet you would. But I didn't. Would you put your bills, how much you owe on your student loans on your list? I have an idea that you would. I didn't. And I owe a lot of money on my student loan. I just put people. And I started thinking, I guess, about my kindness.

And I started thinking about Matthew.

Matthew. Never Matt. Always Matthew. I never asked him why.

We dated for almost a year. And, yes, he treated me well. He was respectful and kind and we laughed together and had shared interests and all those things that are supposed to make it work, right? But I treated him well too. I want you to understand that. I did. And then, about a month ago, we're sitting down on the sofa, and he's poured me a glass of wine -- and something about this is feeling terribly staged -- and I'm thinking, this is it, he's going to propose to me.

But that wasn't it at all. What he does propose is that I explain to him. Explain. And this man who I believed was patient, and was kind, he's suddenly using words like distant and aloof, and I'm thinking, very quickly now, that, no, that's not it at all, I'm funny and charming, but I don't say these things to him, instead I go hot and I know that I'm just boiling over and I'm screaming at him, I'm screaming that I'm not ready and that he doesn't deserve an explanation. I scream at him, and I say awful things. I tell him that I don't have to explain.

And Matthew is very quiet. And he says, "You're right. You don't."

And I awoke the next morning to a grey sky, my throat tired from the tears and the yelling, and I was alone. Matthew had taken his things and left a note on the bedside table. And I screamed as loud as I could because I wanted to fill the whole house up with my words. And there was no one there to scream or whisper back.

And that was irritating. I was irritated. But I would still smile at you on the street. You betcha. I would.

We walk around with our histories bolted to us like suicide bombs, like they could detonate in an hour or tomorrow . . . Or right now. You know what I mean, right? Do you ever feel like that? It's like that bomb detonated when I was thirteen-years-old and the shrapnel landed and grew up around itself. A bizarre garden. A wasteland.

I do not want to explain these things. I want to forget them. But my therapist, with her kind eyes, her gentle tone, she tells me that I can unlock these rooms, that I can allow some space. She asks me about being thirteen. And I hate this. It feels like I'm being pushed under water and I'm kicking and fighting to come up for air. My lungs are full. I'm breaking apart. Detonated.

I'm thirteen. The gangplank between girl and not-quite, right? My mother remarried when I was little, my father was gone, non-existent, whatever. But my mother's husband, my step-father, Nicholas, he had always been there. And my mother, I mean, she drank and she was difficult, but Nicholas, he was always there. My track meets, school plays, whatever. Nick was there. I loved him so much.

I'm thirteen. My mother sits me down, she's been drinking, and she tells me that she knows what's been going on between Nicholas and I. That I'm getting older and that he's been coming in to see me at night and that I'm a woman now, and that I wanted it. And I try to answer and she hits me across the face until I'm bleeding and I can't get away from her . . . she was not kind. (SHE gestures to her face.)

You're wondering if it's related? There's usually an explanation. Two nights later, I awoke to my bedroom filled with flames. I couldn't get out. Like kindling thrown to the flames. They had to come in to get me. She started the fire in my bedroom. About 60% percent of my body was covered in third degree bums. The worst were on my face.

Little children in grocery stores say, Look at that girl's face, Mommy. What's wrong with her? And I want to say back to them, I don't know, sweetheart. I don't know what's wrong with me.

Sometimes scars don't heal. We carry around so much baggage. It breaks our backs to heave it around with us. Sometimes I just want someone to smile back. You might if you knew. You might if you looked like this.

It practically makes me physically sick to say it, but Nicholas never touched me. Never so much as looked at me wrong. I miss him terribly. I do.

I look in mirrors sometimes and imagine how I might have looked . . . Are you ever grateful for being normal? I think, more than anything, that's what irritates me. I just want to be normal. I just want the kindness here (gestures to her smile) to be here (gestures to her heart) too. I don't think that's a lot to ask.

When I smile at you, I want you to smile back. It's like being invisible. I just want you to see me. I want you to look at me, I want you to make eye contact with me, and see me.

That's what I wanted from Matthew, but I didn't know how to ask. The note he left on my bedside table was simple:

I want to know you, but you have to let me. When there's room in your heart for me, please call me. III be waiting. Love, Matthew

I'm trying. I'm trying so hard. I want to love and be loved. I want to be seen.
```

---

## IC-0187: Kissing Doorknobs

- Title: Kissing Doorknobs
- Author (byline): Terry Spencer Hesser
- Work: Not specified
- Publisher: Laurel Leaf
- Publication date as stated: November 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: TARA, MOTHER, DAD, MR. JACOBSON, THERAPIST
- Teaser before the introduction: Yes
- Spoken words (computed): 1862
- Already set (do not supply): none

### Source block (context only)

```text
Author: Terry Spencer Hesser
ISBN: 978-0440413141
Publisher: Laurel Leaf
Date (Month/Year): November 1999
```

### Introduction (context only: never use it for content warnings)

```text
In adolescence, there are many things that seem out of my control - juggling school obligations, teacher and parent expectations, and finding time to just be a kid.

In the novel Kissing Doorknobs, based on real-life experiences, Tara has the same issues. Up until the time Tara was eleven years old, she thought her life was pretty much ordinary. Tall, blond, good grades, sister and parents, and enough anxieties to keep her company. But Tara’s anxieties turned into rounds of habits that plagued her life and family, a result of OCD that wasn’t diagnosed until after years of questioning her sanity.

Having no control in finding our solutions can be exhausting as seen in Kissing Doorknobs by Terry Spencer Hesser.
```

### Performance text (classify this)

```text
TARA: (Pg 12-13) Step on a crack, break your mother’s back! The first time I heard that stupid rhyme was when I was eleven years old and still in possession of my own thoughts. At first I thought the rhyme was stupid.

But [then] I couldn’t stop hearing it in my head over and over again. Eating dinner - Step on a crack, break your mother’s back! Doing homework - Step on a crack, break your mother’s back! Having a conversation - Step on a crack, break your mother’s back! Falling asleep - Step on a crack, break your mother’s back!

Nine syllables. Uneven. I hate that.

Not long after I heard that moronic rhyme for the first time, I suddenly couldn’t take my eyes off the sidewalk. Anyone who saw me quietly counting cracks would know that something was seriously wrong with me.

To and from school. Counting. Sweating. And, of course, worrying. About my mother’s spine. About my sanity. About being seen. And about being interrupted.

TARA: (Pg 18) [When I was little], I always woke up screaming from nightmare[s]. Usually, by the time I opened my eyes, my mother was already by my side, stoking my hair.

MOTHER: “I hate dream monsters too. But that’s all they are. Dream monsters.”

TARA: Letting kindness get that near to pain is like giving a fire some oxygen. Each time it happened, I cried harder and harder as my eczema secretly spread to my torso. Eczema is a red, scaly rash that can crop up anywhere, anytime, and itch so badly that you want to scratch if off with a chain saw. My eczema, like my worries, seemed to come and go regardless of nightmares or the terrible kindness.

(Pg 20) Kindergarten was hell. After a few months, I got over my separation anxiety. But other things started to bother me. I lived in dread of fire drills and emergency evacuations.

(Pg 30) I worried so much that I worried about worrying.

(Pg 21) There were parent-teacher and counselor meetings about my fears, but no one seemed to feel confident about what to do. And so, unable to rely on adults in my life to save me, I turned my attention to God.

(Pg 35-36) Then, one freezing day in winter, while waiting for the bell to ring, I heard someone say, “Step on a crack, break your mother’s back!” and my entire life changed.

No matter how hard I tried, I couldn’t not think the monotonous, scary refrain… and once I began to count cracks, I couldn’t stop.

(Pg 44-45) [But] I decided to save as many souls as I could in my own small way. From that moment on, anytime anyone swore or took the Lord’s name in vain, I said a prayer for their soul and punctuated my plea with the sign of the cross.

My family found my new quirk very irritating. My father tolerated it as another in my series of what he referred to as stages. My mother wasn’t so philosophical. After a few months of it, she was pretty hostile.

Like the time she kicked the car door shut because she had groceries in both arms and got her skirt stuck in the door.

MOTHER: “Son of a b--- already!”

TARA: I instantly came to her aid. “Our Father who art in heaven, hallowed be thy name…”

MOTHER: “Cut it out! Damn!”

TARA: This time [I] was silent. But she saw me make the sign of the cross.

MOTHER: “I’m warning you…”

TARA: Unpacking the groceries, my mother caught me murmuring a Hail Mary.

MOTHER: “Cut it out, Tara. PLEASE.”

TARA: But I couldn’t. “...and blessed is the fruit of thy womb…”

MOTHER: “Cut it out, I said! If I see you doing that one more time, I’m going to punish you… severely… Dammit!”

TARA: I was halfway through the sign of the cross and muttering an “Our Father…”

(Pg 48) A few days later, my parents sent me to see a shrink. I’d been counting cracks for almost a year, but it was the praying that couldn’t be tolerated. (Pg 69) I missed the way we all used to be, so badly that I felt sick.

(Pg 72) To take our minds off our problems, [my family] decided to go to a carnival together. [Earlier that day, my mother had told me,]

MOTHER: (Pg 71) “I’ve been patient, but from now on, every time I see you make the sign of the cross, I’m going to slap you silly.”

TARA: (Pg 72) Mounting the stairs to the Octopus ride, I reflexively performed a quick sign of the cross. I didn’t even really know that I did it. But my mother did. She grabbed my arm so violently I almost fell off the platform.

MOTHER: “Do that on the ride and I’m going to kill you.”

TARA: (Pg 73) As the carnival worker strapped Greta and me in, my mother and I locked eyes. I crossed myself. Not just once but again and again for the duration of the ride.

“Why, Tara? Why?” was all my sister said, but I didn’t answer her. I just kept praying and watching my mother even when we were upside down.

When the ride stopped, I knew I was a dead girl walking.

My mother picked me up by my arms, grabbed both my shoulders and shook me and shook me and shook me, crying harder than I did the entire time.

(Pg 88) For the most part, [by] eighth grade, I was normal. I rarely counted cracks or prayed anymore.

[For Christmas, my grandparents came over for dinner.] (Pg 94) The house smelled great, and everyone was standing around the table admiringly. (Pg 95-96) My dad said,

DAD: “Okay, everybody can sit down where they’re standing.”

TARA: As everyone began to sit down, I went ballistic. “What’s going on? Everybody is in the wrong places! You don’t sit there! You sit there! Like always. Mom sits there like always! And Gramma and Grampa sit there, please! Please! Come on, Greta, you sit there like always… and [I] sit here… just like always! What’s wrong with you guys? Huh? What are you trying to do to me! Come on, Daddy! Pleeeeeze sit there. Mom! Please! Please! Just like always! Just like always. It’s got to be just like always!”

My grandparents looked more scared than I did. My mom’s tears of pride had turned to fountains of pain. It was my father who spoke first.

DAD: “Jesus, Mary and Joseph!”

TARA: “Our Father who art in Heaven -”...

DAD: “That’s it!”

TARA: My dad knocked a chair on its side and stormed out.

(Pg 100) One day in late January, I stopped in front of the doorknob in our living room and… froze.

Before I knew what was happening, I had placed all ten of my fingers on the doorknob in a little circle with the exact same pressure… [and then] brought those fingers to my lips.

I spread my lips out as wide as I could and touched all ten of my fingers to my lips with the exact same pressure. It was the birth of a ritual that would be repeated many, many times. From that day on, I was compelled to perform that ritual almost any time I came in contact with my front door. If I slipped and applied more pressure with one finger than another, or if a finger fell off my lip, I’d have to do it all over again. (Pg 134) A new ritual.

(Pg 100) “Why? Why!? WHY?” my mother asked over and over, as if she was stuck on Replay.

(Pg 110-111) It was a warm spring night and my dad was watching television. I was trying to get out the door so [I] could hang out at the park. Of course, in order to get out the front door, I had to touch the doorknob and my lips. Usually I had to do it thirty-three times. Thirty-three perfect times, and at least a half hour later than I’d planned on leaving, I could finally slip out. Usually. . . I felt [my father] staring at me.

DAD: “Was it something your mother and I did? Tara . . . please. I love you, Tara, We all do. Please stop. Please.”

TARA: The doorbell rang. My father and I were both startled. I didn’t stop my ritual, although I did try to speed it up. Eighteen. Nineteen.

DAD: “Answer the door! Answer the damn door. Can’t you just stop it for once? Stop it. Just stop it!”

TARA: I couldn’t stop. I was so nervous I lost count just as he picked me up, moved me to the side and opened the door. It was Allan Jacobson, my father’s old friend from college who was also the local high-school science teacher. As I looked at my dad’s frightened face, I burst into tears. Giant tears. And my daddy took me in his arms and rocked me. Then he did something I’d never seen before. He began to cry too. We cried. And rocked. And cried.

After my dad and I calmed down, Mr. Jacobson started asking me questions that nobody had ever asked me before.

MR. JACOBSON: (Pg 112) “What does it feel like when you do that thing with the doorknob, honey? Do you do it a certain number of times? I have a boy in my class, a little older than you, who I think has a similar problem.”

TARA: [My new therapist explained.]

THERAPIST: (Pg 123-124) “I’m sure she acts pretty crazy. Imagine how you’d act if you were trapped in an endless loop of repetitive obsessive thoughts accompanied by an anxiety so powerful you’d do anything . . . perform any compulsive act . . . just to make it go away. We don’t know what causes it. Maybe genetics. Maybe stress, trauma, or other injury. Although the behavior has been around as long as man, the research is new. The longer a person has been a slave to OCD, the harder it is to make him or herself risk freedom. Why don’t we move ahead with behavior therapy. If that proves inadequate on its own, then we’ll consider medication.”

TARA: (Pg 132-134) No matter how passionate I was, or how strong I decided to be, behavior therapy was very, very hard. I lost a lot of battles. It had been months and I was still involved in a terrible thirty-three-step dance involving my lips, fingers, and a doorknob. I also still counted cracks and prayed. Not all the time. But enough of the time to doubt that I’d ever win the war for my freedom. And on the good days, when I felt as if I was making progress - I was scared then, too.

[Walking home with my friends one day], I stepped on every crack I could find. I felt nervous, dizzy, sick, but I did it.

When we passed the hardware store, I ran inside. Standing in front of a wall of doorknobs, as a test, I ran my hand across a few of the doorknobs. I felt nothing.

(Pg 18) [When I was little], I always woke up screaming from nightmare[s].

(Pg 142) I think I figured out my dream. As I look at it now, it’s kind of obvious. That monster was my OCD. It came out of nowhere, blocked out my world and threatened to crush me. I was paralyzed.

(Pg 148) But [I] didn’t fold or drop out. [I] summoned the courage to play the cards life had dealt [me]. Reluctant, insecure warrior but warrior all the same. And [I’m not] alone.
```

---

## IC-0188: Know My Name

- Title: Know My Name
- Author (byline): Chanel Miller
- Work: Not specified
- Publisher: Viking
- Publication date as stated: Sept 2019
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHANEL
- Teaser before the introduction: Yes
- Spoken words (computed): 2164
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chanel Miller
ISBN: 978-0735223707
Publisher: Viking
Date (Month/Year): Sept 2019
```

### Introduction (context only: never use it for content warnings)

```text
One night in January 2015, two Stanford University graduate students biking across campus spotted a freshman thrusting his body on top of an unconscious, half-naked woman behind a dumpster. A California jury found 20-year-old Brock Allen Turner, guilty of three counts of sexual assault. Facing a maximum of 14 years in state prison, Turner was sentenced to only 6 months in county jail and probation. The judge said he feared a longer sentence would have a “severe impact” on Turner, a champion swimmer who once aspired to compete in the Olympics.

At that time, Chanel Miller, the victim, was known to the world as Emily Doe. Her impact statement was viewed by 11 million people within 4 days; it was translated globally and read on the floor of Congress; it inspired changes in California law and the recall of the judge in the case. Thousands wrote to say that she had given them the courage to share their own experiences of assault for the first time. Now she reclaims her identity to tell her story of trauma, transcendence, and the power of words.

Know My Name by Chanel Miller
```

### Performance text (classify this)

```text
CHANEL: (Pg 7) (to audience) In this story, I will use Brock Turner’s name, but the truth is he could be Brad or Brody or Benson, and it doesn’t matter. This is an attempt to transform the hurt inside myself, to confront a past, and find a way to live with and incorporate these memories. I want to leave them behind so I can move forward. My name is Chanel. I am a victim, I have no qualms with this word, only with the idea that it is all that I am. However, I am not Brock Turner’s victim. I am not his anything. I don’t belong to him.

CHANEL: (Pg 284-285) (to audience) On January 17th, 2015, it was a quiet Saturday night at home. My dad made some dinner and I sat at the table with my younger sister who was visiting for the weekend. I was working full time and it was approaching my bed time. I planned to stay at home by myself, watch some TV and read, while she went to a party with her friends. Then, I decided it was my only night with her, I had nothing better to do, so why not, there’s a dumb party ten minutes from my house, I would go, dance like a fool, and embarrass my younger sister.

I made silly faces, let my guard down, and drank liquor too fast not factoring in that my tolerance had significantly lowered since college. The next thing I remember I was in a gurney in a hallway. I had dried blood and bandages on the backs of my hands and elbow. A deputy explained I had been assaulted. I was asked to sign papers that said “Rape Victim. ” On that morning, all that I was told was that I had been found behind a dumpster, potentially penetrated by a stranger, and that I should get retested for HIV because results don’t always show up immediately. But for now, I should go home and get back to my normal life.

(Pg 52) In rape cases it’s strange to me when people say, Well why didn’t you fight him? If you woke up to a robber in your home, saw him taking your stuff, people wouldn’t ask, Well why didn’t you fight him? Why didn’t you tell him no? He’s already violating an unspoken rule, why would he suddenly decide to adhere to reason? What would give you reason to think he’d stop if you told him to? And in this case, with my being unconscious, why were there still so many questions?

(Pg 287) One day, I was at work, scrolling through the news on my phone, and came across an article. In it, I read and learned for the first time about how I was found unconscious, with my hair disheveled, long necklace wrapped around my neck, bra pulled out of my dress, dress pulled off over my shoulders and pulled up above my waist, that I was butt naked all the way down to my boots, legs spread apart, and had been penetrated by a foreign object by someone I did not recognize. This was how I learned what happened to me, sitting at my desk reading the news at work. I learned what happened to me the same time everyone else in the world learned what happened to me -- This can’t be me, this can’t be me -- I kept reading. In the next paragraph, I read something that I will never forgive; I read that according to him, I liked it. I liked it.

And then, at the bottom of the article, after I learned about the graphic details of my own sexual assault, the article listed his swimming times. She was found breathing, unresponsive with her underwear six inches away from her bare stomach curled in fetal position. By the way, he’s really good at swimming. Throw in my mile time if that’s what we’re doing. I’m good at cooking, put that in there, I think the end is where you list your extracurriculars to cancel out all the sickening things that’ve happened.

(Pg 288) I thought there’s no way this is going to trial; there were witnesses, there was dirt in my body, he ran but was caught. He’s going to settle, formally apologize, and we will both move on. Instead, I was told he hired a powerful attorney, expert witnesses, private investigators who were going to try and find details about my personal life to use against me, find loopholes in my story to invalidate me in order to show that this sexual assault was in fact a misunderstanding. (Pg 289) I had no power, I had no voice, I was defenseless. My memory loss would be used against me. His attorney constantly reminded the jury, the only one we can believe is Brock, because she doesn’t remember. That helplessness was traumatizing.

(Pg 290) After a physical assault, I was assaulted with questions designed to attack me, to say see, her facts don’t line up, she’s out of her mind, she’s practically an alcoholic, she probably wanted to hook up, he’s like an athlete right, they were both drunk, whatever, the hospital stuff she remembers is after the fact, why take it into account, Brock has a lot at stake so he’s having a really hard time right now.

(Pg 80) When a woman is assaulted, one of the first questions people ask is, Did you say no? This question assumes that the answer was always yes, and that it is her job to revoke the agreement. To defuse the bomb she was given. But why are they allowed to touch us until we physically fight them off? Why is the door open until we have to slam it shut?

(Pg 291) (to defendant) [For] future reference, if you are confused about whether a girl can consent, see if she can speak an entire sentence. You couldn’t even do that. Just one coherent string of words. If she can’t do that, then no. Not maybe, just no. Where was the confusion? This is common sense, human decency.

(Pg 293-297) (to audience) In the end, his unsupported statements and his attorney’s twisted logic fooled no one. The truth won, the truth spoke for itself. You are guilty. Twelve jurors convicted you guilty of three felony counts beyond reasonable doubt, that’s twelve votes per count, thirty-six yeses confirming guilt, that’s one hundred percent, unanimous guilt. This is not a story of another drunk college hookup with poor decision making. Assault is not an accident. (to defendant) Somehow, you still don’t get it. Somehow, you still sound confused.

You said, “Being drunk I just couldn’t make the best decisions and neither could she.” Alcohol is not an excuse. Is it a factor? Yes. But alcohol was not the one who [raped me]. Having too much to drink was an amateur mistake that I admit to, but it is not criminal. Everyone in this room has had a night where they have regretted drinking too much. Regretting drinking is not the same as regretting sexual assault.

You said, you are in the process of establishing a program for high school and college students in which you speak about your experience to “speak out against the college campus drinking culture and the sexual promiscuity that goes along with that.” Campus drinking culture. That’s what we’re speaking out against? You think that’s what I’ve spent the past year fighting for? Not awareness about campus sexual assault, or rape, or learning to recognize consent. Campus drinking culture. Down with Jack Daniels. Down with Skyy Vodka. If you want to talk to people about drinking go to an AA meeting. You realize, having a drinking problem is different than drinking and then forcefully trying to have sex with someone? Show men how to respect women, not how to drink less. Drinking culture and the sexual promiscuity that goes along with that. Goes along with that, like a side effect, like fries on the side of your order. Where does promiscuity even come into play? I don’t see headlines that read, Brock Turner, Guilty of drinking too much and the sexual promiscuity that goes along with that. Campus Sexual Assault. There’s your first PowerPoint slide. Rest assured, if you fail to fix the topic of your talk, I will follow you to every school you go to and give a follow up presentation.

Lastly you said, “I want to show people that one night of drinking can ruin a life.” A life, one life, yours, you forgot about mine. Let me rephrase for you, I want to show people that one night of drinking can ruin two lives. You and me. You are the cause, I am the effect. If you think I was spared, came out unscathed, that today I ride off into sunset, while you suffer the greatest blow, you are mistaken. Nobody wins. We have all been devastated, we have all been trying to find some meaning in all of this suffering. Your damage was concrete; stripped of titles, degrees, enrollment. My damage was internal, unseen, I carry it with me. You took away my worth, my privacy, my energy, my time, my safety, my intimacy, my confidence, my own voice, until today . . . You made me a victim. In newspapers my name was “unconscious intoxicated woman,” ten syllables, and nothing more than that. For a while, I believed that that was all I was. I had to force myself to relearn my real name, my identity. To relearn that this is not all that I am. That I am not just a drunk victim at a frat party found behind a dumpster, while you are the All-American swimmer at a top university, innocent until proven guilty, with so much at stake.

While you worry about your shattered reputation, I refrigerated spoons every night so when I woke up, and my eyes were puffy from crying, I would hold the spoons to my eyes to lessen the swelling so that I could see. I can’t sleep alone at night without having a light on, like a five-year-old, because I have nightmares of being touched. I used to pride myself on my independence, now I am afraid to go on walks in the evening, to attend social events with drinking among friends where I should be comfortable being. It is embarrassing how feeble I feel, how timidly I move through life, always guarded, ready to defend myself, ready to be angry.

(Pg 298-299) You do not get to shrug your shoulders and be confused anymore. You do not get to pretend that there were no red flags. You have been convicted of violating me, intentionally, forcibly, sexually, with malicious intent, and all you can admit to is consuming alcohol. Do not talk about the sad way your life was upturned because alcohol made you do bad things. Face the consequences of putting my pain into question, of making us wait so long for justice. Someone who cannot take full accountability for his actions does not deserve a mitigating sentence.

(Pg 300) (to audience) He has been found guilty of three serious felonies and it is time for him to accept the consequences of his actions. He will not be quietly excused. He is a lifetime sex registrant. That doesn’t expire. Just like what he did to me doesn’t expire, doesn’t just go away after a set number of years. It stays with me, it’s part of my identity, it has forever changed the way I carry myself, the way I live the rest of my life.

(Pg 301) To girls everywhere, I am with you. On nights when you feel alone, I am with you. When people doubt you or dismiss you, I am with you. I fought every day for you. So never stop fighting, I believe you. As the author Anne Lamott once wrote, “Lighthouses don’t go running all over an island looking for boats to save; they just stand there shining.” Although I can’t save every boat, I hope that by speaking today, you absorbed a small amount of light, a small knowing that you can’t be silenced, a small satisfaction that justice was served, a small assurance that we are getting somewhere, and a big, big knowing that you are important, unquestionably, you are untouchable, you are beautiful, you are to be valued, respected, undeniably, every minute of every day, you are powerful and nobody can take that away from you.

(Pg 280) Hold up your head when the tears come, when you are mocked, insulted, questioned, threatened, when they tell you you are nothing, when your body is reduced to openings. The journey will be longer than you imagined, trauma will find you again and again. Do not become the ones who hurt you. Stay tender with your power. Never fight to injure, fight to uplift. Fight because you know that in this life, you deserve safety, joy, and freedom. Fight because it is your life. Not anyone else’s.

Emily Doe’s Victim Impact Statement was originally published by Katie J.M. Baker in Buzzfeed News on June 3, 2016.
```

---

## IC-0189: The Last Flapper

- Title: The Last Flapper
- Author (byline): William Luce
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Oct 1990
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: VOICE, ZELDA, VOICES
- Teaser before the introduction: Yes
- Spoken words (computed): 1478
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Luce
ISBN: 978-0573691683
Publisher: Samuel French, Inc.
Date (Month/Year): Oct 1990
```

### Introduction (context only: never use it for content warnings)

```text
Zelda Fitzgerald was a cultural icon of the 1920s. Dubbed the ‘first American flapper by her husband F. Scott Fitzgerald; she wore short skirts, listened to jazz and flaunted her disdain for what was considered acceptable behavior. But Zelda also suffered from a form of mental illness and spent the last decade of her life at Highland Hospital, a North Carolina sanitarium. Based on her letters and stories, this is her story.

The Last Flapper by William Luce
```

### Performance text (classify this)

```text
VOICE: (Pg 11-13) (As nurse) Attention, nursing staff. The recreation room is being painted, so please remind patients that the party tonight is in the cafeteria.

ZELDA: (ZELDA enters the dimly lighted office of Dr. Carroll) Dr. Carroll? (Surprised) He's not here. (To audience) It's three o'clock, isn't it? (Looks into the hall, then turns back to the room) Dr. Carroll, come out, come out, wherever you are.

VOICE: (As nurse) Your attention, please. Dr. Carroll has been called away on an emergency. His afternoon appointments are cancelled

ZELDA: Hallelujah! No three o'clock inquisition! (Checks the hallway. Returns to the desk. With a letter opener, she begins prying open the locked file drawer) Thank you, Doctor, don't mind if I do. (Drawer opens; finding files) "Highland Hospital. Robert S. Carroll, M.D. Confidential." (Smiling) Not anymore. (Riffling through files) Here's Katie's. All she does is wander around, yelling . . . "Would somebody call me a cab?" (More files) Here's George's. (Opening and reading) "Permit patient the use of cosmetics on all but visiting days." (To audience) George is a long, tall man who roams the halls in evening gowns. He says his father wanted a boy; his mother wanted a girl. I guess they were both satisfied. (More files) "Fitzgerald, Zelda." (Begins to silently read. Several beats. Angrily, she hurls her file to the floor)

ZELDA: (Pg 14) (Picks up pages at random studies each page and lets it fall again. Reads aloud) "Fitzgerald, Zelda. Schizophrenic. Patient rebels against authority. Do not stir up the patient. Relieve her of having to make decisions, which aggravates her disorder. Avoid confrontation." (To audience) Excuse me for smiling. People think I've thought of something witty. The fact is, my smile is uncontrollable, and it terrifies me. I'm simply a neurotic woman who's reached the end of her physical resources and is exhausted.

(Pg 15-16) (Picks up another sheet of paper from the floor and peruses it. It prompts a memory) I was always an excitement eater. When I was a child, I phoned the fire department. "Hello, Mr. Fireman? There's a little girl stuck on top of a house! The gray and white one at Six Pleasant Avenue. Hurry!" I got the ladder, climbed onto the roof, kicked the ladder away and waited. The fire engine came clanging down the street, and the neighbors ran out to see what the hell was - (Suddenly distracted) Do you know something else? Nobody's ever sent me a get-well card. Isn't that rotten? "Sorry you've gone insane, Zelda." Even that would do. But not a word. (beat) (Pg 17-18) And I can't dance. They won't let me. "No dancing, Mrs. Fitzgerald." Now you talk about therapy. That could really help me. But Dr. Carroll says that's part of my problem. Just because my husband went and blabbed to him about Paris, and how I made myself sick going to ballet class eight hours a day. Scott couldn't realize that dancing was my refuge from the chaos in our lives. (beat)

(lost in another memory) (Pg 23) (Now the young Zelda with a southern accent. She jumps up, extending her left hand) (To Mamma) Mamma! Oh, looka here. It's from Scott. (Pause) It's an engagement ring, Mamma. It's his mother's. Isn't it grand? (Pause) Oh, Mamma, I'm practically nineteen. (Gazing at the ring) And it fits, Mamma. (Dreamily) Mrs. Francis Scott Fitzgerald. It sorta says "soon" to me. Just sings it. Oh, just wait til’ I wear it Saturday night to the Country Club dance.

(Emerges from her memory to speak eloquently to the audience) (Pg 26) In Montgomery in 1920, there was a time, a quality, that pertained to nowhere else. It began about half past six on an early summer evening, with the flicker and splatter of the corner streetlights going on. And it lasted till the great incandescent globes were black with moths and beetles, and the children were called to bed from the dusty streets, and the grownups sat out on the porches, talking. (Pause)

(Reverts to young Zelda. In her mind, she is being fitted for her wedding dress) (Pg 27) (To Mamma) Oh, Mamma, this'll be the prettiest wedding dress ever! (Twirls with excitement) Scott says we're gonna be married in St. Patrick's Cathedral, in the rectory. (soft smile; she speaks again to the audience) (Pg 29-30) Scott says when he first saw me in 1918, he thought my hair looked honey-yellow. I remember the dress I was wearing -- white silk with a chiffon tunic floating over it. And a large-brimmed hat as big as a manhole cover. And long streamers down my back. And a fan. Oh, my, a genuine Southern belle. He was beautiful as men are not meant to be, with violet eyes and dark lashes and a straight nose and sensitive mouth.

(Pg 31-32) (Now the young Zelda, she becomes flirtatious) (To Scott) Francis Scott Fitzgerald? What a remarkable name. Are you related to Francis Scott Key, the man who wrote that awful song that nobody can sing? (Pause) You are? Well, don't be offended, Lieutenant, but I hope it never becomes our national anthem. Woodrow Wilson's the only one who likes it, and he's such an ol' coot. You don't like it, do you? (Pause) You do? Maybe I should listen to it a few more times with that in mind. (Pause) My name is Zelda Sayre. Z-E-L-D-A. I got named after a gypsy queen in a novel Mamma was reading just 'fore she had me.

(long beat as her memory jumps in time, there is a marked change in her demeanor) Scott, why did you marry me? (As Scott) Because you have some sense of the seriousness of life. (To Scott) Seriousness? (To audience) Me? (To Scott) Why, I'm the original Flapper, my silly Goofo. I'm down there in black and white in your own novels as a proud and selfish little fool. There isn't a serious bone in my body. Remember? (to audience) During that time, I bobbed my hair, lost my Southern accent and went into battle.

(laughs rather uncontrollably) I jumped into a fountain in my evening clothes and rode down Fifth Avenue one hot summer evening on top of a taxi. We both did. (To Scott) Didn't we, Scott? (To audience) I was on the hood and he was on the roof.

(Pg 49) I had a bad reputation, all right. I smoked rabbit tobacco in a com-cob pipe, and if there wasn't any gin, I drank corn liquor cut with coke. (Pg 46) (As Mama) No lady ever steps out the front door without fastening her gloves. And no lady ever lets her bare feet touch the floor. We are genteel Southern ladies, and don't you forget it. (Pg 49)

(chastised; to Mamma, quietly) Yes, Mamma.

(She shakes off the melancholy and speaks with great animation to the audience) In Montgomery there was this ice-cream parlor on Dexter Avenue. Harry's Place. It was the local jelly joint. All the boys gathered there. I called them my "Jelly Beans." They just loafed around. You know how boys do when they don't have dates. Once they drove by the house, yelling my name: Zelda! Zelda! Zelda! I ran out on the veranda. (Calling) My Jelly Beans! All my beautiful Jelly Beans! I love you! (To audience) Daddy was home and he was livid. He said, (in father’s voice) "Your personal conduct is outrageous! How dare you make a spectacle of yourself!" (To Daddy defiantly) I don't care. I've got a right to do anything I want! (she wilts, and a deep melancholy comes over her)

(Pg 33) Here's to the Flapper, who's growing old at last. She's come to none of the predicted bad ends but has gone where all good flappers go - into marriage and boredom and convention. (bolstering her strength) Who gives a damn about convention? Not me. The world isn't going to suffocate me. That's what this flapper's all about. Climb to the top and live high. And if the fine's a heavy one, what the hell! There's only one act of significance. You take what you want when you want it! (Pause)

(Pg 35) (To audience, bewildered) Dear God, that desperate nostalgia to be young. It's so painful. I used to say to myself, "Zelda, you'll be all right for another five years. You'll be pretty that long. It takes a good fifty years for time to batter down a woman's looks and crumple her charm." Look at me! The glamorous Mrs. F. Scott Fitzgerald and her Elizabeth Arden face - gone to pot.

(Pg 50-51) (Hears a voice in her head that captures her attention) No, Doctor, I do not want to talk about my husband. Anyway, he's dead. He died eight years ago. A heart attack in Hollywood. (Reminiscing) Scott was the prophet of his generation. The Jazz Age. And - and - (She gropes for the next idea, her thoughts are disjointed, and she becomes increasingly agitated) And I'm fed up with these wistful, tragic silhouettes of Scott and Zelda. People want to bank on gods? Well, that's too bad! (clutching her hands to her face, she feels the pain; sobbing) He came home last night, and he smashed me in the nose. He broke down the bathroom door and punched me in the nose. (Pg 55-57) (her sobbing is replaced by anger) He says I've failed him. Well, it's just barely possible he's failed me, the sonuvabitch. (To Scott) No, Scott, I am not reproaching you. You blamed me when you couldn't write, when you know the real reason was you were out half the night with the boys, drinking yourself unconscious. (Pause as she listens to a voice in her head) No, goddamn it, you let me finish! You whined about your lonely struggle against gifted and talented writers, and how I was only a third-rate writer and a third-rate ballet dancer. If that was true, then why the hell did you put your name on my short stories? Why did you help yourself to my diaries and letters?

VOICES: Help!

ZELDA: Did you hear that?

VOICES: Help! Help! Help!

ZELDA: I used to hear voices only once in a while, but now I hear them all the time. "Help!" they cry. (Impatiently) Oh, I know they're inside me! Don't you think I know that?

VOICES: (As Scott) Zelda! Zelda! Zelda!

ZELDA: (Screaming) Scott, I'm here! Come and get me! Please, come and get me!

(Crumples, sobbing. Long beat, then quietly to audience) Nobody, not even the poets, can measure how much a heart can hold. But hearts perish in public institutions.

CLOSING

That night, March 10, 1948 – a fire broke out at Highland Hospital. Witnesses could hear the harrowing, desperate screams of women on the top floor where flames held them hostage and consumed their lives. There was no way out—some of the windows were locked, others were barred by heavy chains. Zelda and four other women on the top floor, having been given strong sedatives to induce sleep, died in the blaze.
```

---

## IC-0190: Learning How to Walk

- Title: Learning How to Walk
- Author (byline): Jason Sheets
- Work: Turning Points: 30 Pieces for Oral Interpretation, Pgs 141-145
- Publisher: Tichenor Publishing
- Publication date as stated: Jan 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: WHITNEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1423
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jason Sheets
Book: Turning Points: 30 Pieces for Oral Interpretation,
Pgs 141-145
ISBN: 978-0742117013
Publisher: Tichenor Publishing
Date (Month/Year): Jan 2001
```

### Introduction (context only: never use it for content warnings)

```text
When life takes an unexpected turn and someone you love becomes disabled, the challenges faced by both people in the relationship can be overwhelming. In this selection, a young couple are involved in a horrible car accident and are now faced with a future that looks dramatically different from the one they had envisioned. Can Tony learn how to walk again, or will Whitney learn how to walk away?

Learning How to Walk by Jason Sheets
```

### Performance text (classify this)

```text
WHITNEY: (Pg 141-145) All I remember from the incident are five still-frames, mentally stored as black and white images.

Frame # 1: Tony is driving down the road. He spills part of his Taco Bell burrito on his new shirt. I reprimand him. We laugh.

Frame #2: A loud crash. Darkness beyond anything I've ever seen before. It's like I'm miles back into a cave, only darker.

Frame #3: My mother tells me she's glad to see me wake up. She is arranging flowers in the room. She tells me to rest.

Frame #4: My mother tells me I'll be OK, but begins to cry when she states that Tony is not as fortunate. A feeling of death enters my heart.

Frame #5: My friend Tricia tells me that Tony did not die, but can no longer walk. He'll need your strength, she says. I say I will do whatever I can to help.

That is all I can remember from the incident that changed my life forever. I wish I knew more. I wish the images were at least in color.

WHITNEY: Tony and I met when I was 18 and he was 21. Ironically, because of my AP credit and his momentary lapses of reason, we were both sophomores. I'd never dated much. People asked me -- that wasn't the problem. The problem was me: I noticed things. My mother had divorced when I was eight, and she told me to watch out for men. Never settle, she told me. And you could bet I listened to my mother.

But Tony was different. lt took him three months, four sly winks, and a blatantly written note from Tricia to make him finally ask me out. I suppose people marveled at his lack of focus, his carefree nature. I saw it as indelible charm.

Everything interested him. l absolutely detest the "I am a sponge" analogy that so many others overuse, but Tony really was. He soaked up the nuances of movies, of relationships, of me. By the time my 19th birthday rolled around, it was clear: I planned on falling in love once in a lifetime, and Tony would be that one time.

I would like to say that the day of the accident somehow had special connotations to me. Perhaps I'd had an eerie feeling. Perhaps we'd just said we'd always go everywhere together. Perhaps we'd had some moment that defined the day. But there was no real irony to the events. We were riding in the car on the way to my hometown, a truck veered past the median, and then the darkness. It took me 3 days before I could finally see Tony. He was wrapped in countless bandages, but that scene-stealing smile was still there. I'm glad you 're OK, he said. You too, I replied before I realized what I was saying. Tony just looked at me with adoration: At least I have you, he responded.

Unbeknownst to most of the population, I believe doctors have to take a class in medical school that teaches them how to properly double-speak. It took me three more days before I could finally get the man to say that, yes, his brain is fine, but no, he'd never do the two-step with me again. It was only after I cleared the double-speak that the reality of what was happening really kick[ed] in. My life became a series of daily rituals. At nine o' clock I would start my journey to the hospital. If there was one thing I was leery of, it was hospitals. I used to find excuses to keep me from going. The truth was I couldn't stand the smell. The attitude. The feeling of unsettled completion of life that occurred every day. Now, my fear of hospitals and my love for Tony has been unbearably linked. When I think of Tony, l imagine the smell of hospitals. l imagine death. I wanted to vomit. Sometimes, I did.

But of course, the doctor is wrong. Tony will walk. He'll walk. Of course he will. It happens all the time in the movies. Doctor says: "I'm sorry, there's just no hope." Patient: "But I can if I try hard enough." Three months later he walks. He does. It happens in the movies. And what are movies? A reflection of real life. Right?

So now I find myself in Tony's house. I've dropped out of school, I have all my calls and mail forwarded. People refer to me as "Nurse Whitney." It was cute for a while. Now I find the title impeccably accurate. The only real difference is that after l wash his face, or feed him or bathe him, he tells me he loves me and I return the feelings. When most nurses get off work, they would go home. We stay up and watch television together and discuss our future. He wants to marry me. He tells me: We can still have the fairy tale. I say, Of course we can sweetheart I always said I'd only fall in love one time and you are the one I love. He follows this by saying I've been the best and that he' lucky to have someone who's willing to make the sacrifice. After he says that I feel strangely worse.

I tell Tony everything. Everything, but my dreams. For the first few months, I dreamt that he'd walk again. Now, I dream of leaving. I dream of running away from all my family and friends who would tell me I was being selfish, and I would spend the rest of my life on some lonely beach reading.

I dream he will say: Whitney, I don't love you anymore. Please go. I dream it. And I never tell anyone. Ever.

l figure the equation and try to re-figure it for a different answer. I never get one. I've [even] started making a list of the ways I could leave. Just in case one could actually be plausible.

1.) I could say I can't afford to stay.
2.) I could say I found someone else.
3.) I could say it's not right of me to dominate his time.
4.) I could say there was a doctor in India who's supposed to have a cure. I'II go find out.

5.) I could kill myself for thinking these things about the man I love. 6.) I could say I'm not worthy of him because of my evil thoughts -- That one could be plausible.

When I tell him I'm leaving, he does not look shocked, or stunned, or even surprised. He merely says OK, and then I feel ten times worse. For months, I'd pictured this traumatic scene where I announce my intentions and he begs and pleads with me to stay. He offers me the world and I walk away. Instead, he says OK.

OK, so now I have to explain myself. See, my mother always told me to never settle and always wait for the fairy tale. And you were the fairy tale, Tony! You were my prince that was set to sweep me off my feet and never look back. You were everything. The looks. The smile. The wit. The "sponge" of life that soaked up everything that it has to offer. You were it. You were it. But, see Tony, princes walk. They pick me up and carry me over the threshold on our wedding day. They play football with our children. They go for late night jogs with me when the rest of the world is driving me nuts. They do it all, Tony. That's the fairy tale. That's my fairy tale.

Tony now has a tear running down his cheek and I say to myself are you happy now? Is this the way it's supposed to play out? Is this the way the movie ends?

He says: I wish you all the best. If you need me, you know where I'll be.

I don't know if he's trying to be funny or vindictive, so I leave. I cry.

Life is a series of trades. You give something to get something. Fifty cents: a Pepsi. A compliment: a promotion. I made the biggest trade of all. I traded love for freedom. And now I'm left to ask: Did I make the right choice? And I like to think I can find the answer, but I can't. All I can think is that in the fairy tales, you get both. In the fairy tale, you get everything.
```

---

## IC-0191: Letters to a Student Revolutionary

- Title: Letters to a Student Revolutionary
- Author (byline): Elizabeth Wong
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Jan 1996
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BIBI, CHORUS, KAREN, BOSS, SOLDIER
- Teaser before the introduction: Yes
- Spoken words (computed): 2558
- Already set (do not supply): none

### Source block (context only)

```text
Author: Elizabeth Wong
ISBN: 978-0871296450
Publisher: Dramatic Publishing
Date (Month/Year): Jan 1996
```

### Introduction (context only: never use it for content warnings)

```text
Two young women . . . worlds apart in culture forge a friendship that lasts throughout the years. Who would have guessed that a chance meeting would lead to a long-distance bond that in a very small way could bring the cultures of Asia and the U.S. to a greater understanding of one another.

Letters to a Student Revolutionary by Elizabeth Wong
```

### Performance text (classify this)

```text
BIBI: (to audience). I was touring China with Mom and Dad. I took to the streets of Beijing. Wandered into Tiananmen Square-a hungry look in my eyes, a vain hope in my heart. No place is truly civilized without Mickey D and a drive-up window.

CHORUS: (to audience). Summer 1979. Tourism was still so new in China.

KAREN: (enters, pushing an old coaster bicycle -- to audience). I am on my way home from the factory. End of the graveyard shift. It is already hot like hell. Do I say that right? Yes, I think so. What harm is there to practice a little English?

BIBI: (to audience). Oh look. Grandmothers with ancient faces, pushing bamboo strollers like shopping carts. (She peeks into the strollers.) Ahhhhh, sweetest little babies with wispy, fuzzy, spiky hair.

KAREN: (to audience). I will go up to her and speak to her. We will make beautiful sentences together.

KAREN: Hello.

BIBI: Oh, hello.

KAREN: Please. Not so loud. (Beat.) Are you?

BIBI: (whispers). I am. How can you tell?

KAREN: Ahh. (Pause.) Your hair.

BIBI: Completely unnatural, I know. It's called a permanent. Every time I go to the salon, they want to give me the same old, tired thing-the classic bob and bangs, exactly like yours.

They tell me, "You look so cute. A little China doll, that's what you are." So I say, "Aldo, baby darling, perm it. Wave it. Frizz it. Spike it. Color it blue." It's unusual, don't you think?

KAREN: (starts to touch BIBI’s sleeve; then withdraws shyly). Here we have only a few colors. Grey and blue and green. May I ask what is your name?

BIBI: Bibi. My name is Bibi. (They reach to shake hands. but before they touch, BIBI and KAREN freeze. (to audience). Our conversation lasted about two, three minutes, tops. (The two women move away from each other. BIBI shouts.) That's Los Angeles, California. U.S.A. 90026. Can you remember all of that?

KAREN: (nods vigorously. To self). Yes, I will remember.

BIBI: (to audience). She didn't even tell me her name.

CHORUS: Bibi went back home to California, U.S.A. And that was the beginning of a most un-comfortable correspondence.

KAREN: (writes). Summer, 1979. My dear American friend ... (Scratches out, starts again.) My dear new friend. Greetings from Beijing. (KAREN sits back, stares into space.) . . . I met you in Tiananmen Square. It is a happy feeling I have . . . to have you for a secret friend, a special friend. I have much stupidity since I realized I never told you my name.

BIBI: (to KAREN). Karen? Karen is a good name.

KAREN: (To audience.) I chose my new name in secret. Where you live, you can be open about such matters. But here we must do everything in secret. Bibi, you have such freedom. I have no freedom. None whatsoever. I was meant to be born in the United States, to live in freedom like you. Do you understand? (Beat.) Two days after I met you, my boss at the factory where I am in the accounting department, asked to speak to me. I am taken to a small room in the basement. This is not a good sign.

BOSS: (kindly, as if to an errant child). You were seen talking to an American. Now, don't be afraid. You may talk to Westerners now. But you must not listen to what they say. You must not get any ideas. (Recites by rote.) Good citizens have only ideas that also belong to The State. The State is your mother. The State is your father. The State is more than your mother or your father. Do you understand?

KAREN: I said, "Yes." But in my heart, I do not understand. I have never understood why I cannot speak my opinions. (Resignedly.) But this is China. (Beat.) I think, Bibi, I want to be having freedom like you. Perhaps you, Bibi, will pay $10,000 for my airplane ticket and my living in California. I will work and work and work and pay you back. I look forward to your favorable response. Your friend, Karen.

BIBI: She's nothing to me and I'm nothing to her. I could care less. I'm not political. And I resent that she is trying to make me responsible for her freedom. I'm barely responsible for my own. (Beat.) January, 1980. Dear Karen, I am so sorry it's taken me nearly six months to write you back. (To audience, resolutely.) I would have answered you sooner, but I was unsure about how to respond to your letter . . . Karen. I don't know what possessed me. But two months ago, I did go to the office of the Immigration and Naturalization Service.

KAREN: Bibi, did you talk about me? Will you help me, Bibi?

BIBI: Karen, the government told me I was not a suitable sponsor. To be a sponsor, I have to prove I can support you as well as myself. Karen, I'm just starting out in life. I don't have much in the way of money.

KAREN: So when you are rich, you can sponsor me, yes?

BIBI: Karen, I really don't think I can do more. I mean, I don't even know you. I'm sorry. Sincerely, Bibi.

CHORUS: Karen continued to write to Bibi. Long letters about her life in China. Her longings for America. [She] would bring up the subject every now and then. Bibi tried to ignore [it], but finally got fed up.

BIBI: Winter, 1980. Dear Karen, You may ask me if you wish. But please do not bring my parents into this. They are not rich. The streets here are not paved with gold. They are paved with concrete, sweat, hard work and struggle. My mother and father struggle every day.

KAREN: Spring, 1981 . . . You asked about my mother. My mother is dead.

BIBI: When did she die?

KAREN: When I was very young. Near my house, next to the pig pen, there is a rice field. (Pause.) My mother is in the field. I see her. (Waves.) MaMa! "Bao Bao gay ni dai fan lail" [Your baby brings you your lunch.] (Beat.) Wait! Who is that? It is the commissaire! -- the man who reports everything.

BIBI: I see him.

KAREN: He is shaking my mother. Why is he doing that? Where is he taking her? MaMa! MaMa! (Pause.) I just watched my mother as they took her away.

BIBI: I'm sorry.

KAREN: The cat eats the mouse. He doesn't apologize for doing what is in his nature to do. She was punished. Not for stealing, but for resisting. If the mouse struggles, the cat grips tighter, first with one paw, then with two. The only thing the mouse can do is escape, run away. As fast as you can. If you can. Public execution is part of our daily lives, part of our education process.

CHORUS: Bibi and Karen continued their correspondence, but sporadically. About once or twice a year.

BIBI: (to audience). Fall, 1986. Mmmm. (Beat.) You know what, Karen? Sometimes, I wish someone would tell me: This is what you are good at, Bibi, so go and do it. This is the man who is good for you, Bibi, marry him.

KAREN: You wouldn't listen anyway, and you know it.

BIBI: No, I probably wouldn't. (To KAREN.) How is . . . ?

KAREN: Lu Yan? Lu Yan is the only guy I've ever . . . how you say? . . .

BIBI: Slept with?

KAREN: No . . . he is the first man I ever dated. Not much choice here in China, even though we are very many millions of people.

BIBI: Choice! Talk about choice. Shall I regale you with tales from the darkside? Dates from hell? By my calculations, I would say I've met a total of, or had a disastrous dinner or ahem, et cetera, et cetera, with at least 127 men of assorted shapes and sizes and denominations. And colors. Don't forget colors.

KAREN: I am getting married during the Mid-Autumn Festival. I'm not sure I want to be married . . . I want to do and see so much, but my world is so small.

BIBI: Here in America, we are free, free to choose our lovers and make our own mistakes. The most wonderful thing about freedom, Karen, is you get plenty of rope with which to hang yourself. Wait! Did you say getting married? How wonderful. It is wonderful, right?

CHORUS: Lu Yan and Karen were married in the fall of 1986. Karen's father and brother gave as a dowry to Lu Yan's family, two live chickens, eight kilos of pig's intestines, 500 steamed buns, a sea lion bicycle, 20 kilos of fish, and 10 cartons of American cigarettes.

KAREN: Winter, 1987. Dear Bibi, Lu Yan is always telling me what to do. Married life isn't what I thought. His mother tells me how to wash his shirts, how to make a dinner. She complains I do not concentrate, as my head is always spinning in the clouds. I do not know who I am.

BIBI: Spring, 1988. Dear Karen, I have changed newspapers five times in the past three years. It's easier to move up by moving out, but I'm getting a little tired of moving around. West Coast, East Coast. No place feels like home. Home doesn't even feel like home. Everywhere I go, I ask myself the question, "Who am I?" "How do I fit in?" The answer changes as fast as my address.

KAREN: Summer, 1988. Dear Bibi, I am a flower that will never open, never to be kissed by a bee. I want to open. I want to feel the sting of freedom. More and more, I feel bitter towards my life and my uselessness. I go to work, I have ideas to improve my job, and no one listens to me. I am a nobody. And I want to be a somebody.

BIBI: (to KAREN). Do you realize, Karen, we've been friends for almost ten years?

KAREN: And for ten years, you have not listened to one word I have said. I thought my marriage would make a solution, but it doesn't. It is not what I wanted for my life. Bibi, you know my heart. But you won't help me. I want to count for something. I can count for something in California.

BIBI: (sincerely). Here or there, your struggle is my struggle. No matter where we are, the struggle is the same. I'm trying not to run away from my problems. Why can't you be happy where you are?

KAREN: Why can't you? You live in a democracy, the individual can vote. You can count for something.

BIBI: What elementary school book did you read that from? My vote counts?

KAREN: That's right. You have the luxury to be selfish. To think of only yourself. You live in Paradise, and I live in hell.

BIBI: Well, Karen, it can be hell living in Paradise.

KAREN: (ignoring). I want democracy. Democracy for me. Freedom of speech. Freedom to chose. (Short pause.)

BIBI: Freedom to be confused. (Beat.)

KAREN: At least you have incentives to strive for a better life. But here whether I work one hour or ten hours, it's all the same. You just don't know what it's like.

BIBI: Can I help it if good ideals are polluted by extremists and dictators? Health care for everybody. Jobs for everybody. Everyone EQUAL under the law. Everyone working towards the greater good. And here's a novel concept people actually caring about the well-being of other people. In America, we call that welfare, and anyone on it is seen as a slackard and a mooch. In China, it's called social responsibility.

KAREN: If you think China is so good, you should come and live here. Bibi, I think you must be a communist at heart.

BIBI: Karen, I just can't afford anything right now. I'm unemployed-again. I quit. And I'm glad I did. I had names, addresses, quotes. And the paper wouldn't print it. We're having an election here, Karen, and an African-American is on the ballot. Quote, "I'd never put a black man in office." Quote: "No negro is going to run this country." Next morning, I read the paper, the quotes are gone. So, I storm into the managing editor's office during a budget meeting. Everybody was there. I said, "Hey what is this?" Why are you sanitizing the news, making it all pretty and clean for public consumption? I strenuously object. I have been so naive. So, in short, Karen, I quit.

KAREN: How lucky you are. You get to live your own life, your way.

BIBI: Sure I'm lucky. I get to fight my battles alone and unsupported, at work and at home. I'm a lone wolf howling, and no one listens.

KAREN: Bibi, I have been thinking about what you say about America. And I think you are right. You see, Bibi, my country is changing and I have a new hope for a better life. And, I no longer wish to come to be an American like you. (Beat.) But I will always be your friend . . . (to audience). May, 1989. Dear Bibi, Here I am sitting in a tent in Tiananmen Square. For the first time in my life, I believe I can be a somebody, I believe my contribution will make a difference. I believe freedom will not grow out of theory but out of ourselves. We are fighting for a system that will respect the individual. The government must listen to us. All we want is a dialogue. A conversation. We want an end to censorship. We want an end to corruption. We are the voices of tomorrow. And our voices will be heard.

BIBI: May, 1989. Dear Karen, I've been watching the television reports. Everybody always asks me how I feel about what is happening in China. I'm so envious of your power-of how you have caused your government, caused the world to take notice. But I am also concerned about your naiveté in striving towards a foreign ideal. I do believe change will come, but it must be at your own pace. I am not sure America is the proper model for the new China that you want. Perhaps you should look to make a Chinese democracy. Karen, are you listening? Because right now, I think that to be a somebody in China is suicide. I don't mean to dampen your spirits, but I am worried. Please, please be careful.

KAREN: We are lying on the floor. Students on a hunger strike. Most of us are women. We haven't eaten in days, and I will not until I have my freedom. A clean division between what we want and what the government stands for. A clear break. On June 4, 1989. Tanks, armored personnel carriers and trucks full of troops marched into Tiananmen Square. Many of us linked arms, and tried to stand in their way.

SOLDIER: Be a good Chinese and go home. Go home and save your life. This is China. This is not the West. Be a good Chinese and go home.

KAREN: Tanks marched forward and crushed the first row. We marched forward. Run! Get out of the way. Run! Blood everywhere.

SOLDIER: Soldiers, forward. Students, comrades! Be good Chinese and go home. This is China.

This is not the West.

KAREN: The statue fell. Everyone was running. (screams). You animals! (lights out.)

TRANSITION This year, *Insert Year*, is the ______ anniversary of the Tiananmen Square protests. And even today, the Chinese government continues to detain suspected activists and take measures to censor any mention of the event on the Internet.

BIBI: On that day, as I watched the news, as world events marched into my living room. For the first time in my life, I knew . . . I felt . . . Chinese. And as days passed, I searched my TV set, changing channels, looking for news reports. Nothing, nothing coming out of China. Just a black curtain of silence.

CHORUS: Statistics on the death toll have been confusing. The Chinese Government says less than 400 people were killed, and only 23 of them were students. But according to unofficial reports, at least 5,000 died, and at least 30,000 people were reportedly injured. And China and America have begun a policy of selective historical amnesia.
```

---

## IC-0192: Light and Hope

- Title: Light and Hope
- Author (byline): Bethany Van Delft
- Work: The Moth Presents All These Wonders (Pg 293-299)
- Publisher: Crown/Archetype
- Publication date as stated: March 2017
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BETHANY
- Teaser before the introduction: No
- Spoken words (computed): 1615
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bethany Van Delft
Book: The Moth Presents All These Wonders
(Pg 293-299)
ISBN: 978-1101904404
Publisher: Crown/Archetype
Date (Month/Year): March 2017
```

### Introduction (context only: never use it for content warnings)

```text
My daughter's beauty often takes my breath away: Sparkling green eyes that are the same color as her Daddy's, an enormous smile and a laugh so infectious that the hardest of hearts melt in response, whisper-soft hair that has just the slightest curl and she gives the best hugs – the ones that make your all warm and fuzzy inside. I love my daughter so much! But I didn’t always feel this way . . . for a very long time, I was crying daily and desperately searching for . . .

Light and Hope by Bethany Van Delft
```

### Performance text (classify this)

```text
BETHANY: (Pg 293-299) I had a perfect pregnancy. I saw a maternal fetal specialist every week. And every week the doctor and nurses would gather around the ultrasound and look at the baby and say, "What a perfect baby. This is a miracle at your age."

I spent nine months wondering what this was going to be like. What was it going to be like to give birth? What was it going to be like to see this person I had been growing all this time? Especially-what was that rush of love that new mothers talk about? What was that going to be like? And of course, being a standup comedian, I relished the new market that motherhood was going to thrust me into. But most of all, the thought of leaving the house one day as the two of us and coming back home as a family filled me with wonder.

When the time came, they told us to prepare for a very long labor. But no, I pushed for twenty minutes. And Lucia Esperanza was born at 10:59 p.m. that evening.

They put her on my chest, and I soaked in this little person I'd been carrying around. I saw her little chin and her heart-shaped mouth, her button nose and her folded ears. I saw her almond eyes, and my heart stopped.

I asked my husband, Jayme, "Does she look like she has Down syndrome?" Instead of the rush of love, I felt a wave of fear and anxiety. They brought me to our recovery room, and they took the baby to do some routine tests. My fear turned to panic, and I finally rang for the nurse, hysterical.

I was like, "Why is it taking so long? Is there something wrong? What is wrong with my baby? Can you bring her back to me?" She brought back the baby, but I was terrified.

The next day the pediatrician came in our room, and he said, "Congratulations! Your baby is perfect." It was such a relief. I could breathe again.

He said, "Her Apgar score was great." And her hearing was fine. And she had ten fingers and ten toes and . . . . he suspected that she had Down syndrome.

He gave us a packet with a number on a Post-it note on top for us to call. As he was leaving, he said, “ You know now is the time to have these babies, what with all the research. I mean, some of them even read."

We spent our days in the hospital in the room with the door closed, and the shades pulled. At night Jayme slept in the single bed with me, behind me. And he held me really tight. I think he held me so tight so I wouldn't fall out of the bed from crying so hard.

It was confirmed. She had trisomy 21, which is three copies of her twenty-first chromosome instead of two. That first few weeks was just a blur of tears and forms and doctors' appointments and lists I made of all the things that were never going to happen now -- all the things that she would never do.

I slept on the couch with her for four months, with her skin on my skin, so she could feel loved. But every time I looked at her, all I thought is, Where is my baby? Whose baby is this? When do I get to see my baby?

I had begged Jayme to please let me change her name. Esperanza was my grandmother's name, and Lucia was just a cute reason to call her Lulu. Together it means light and hope. But I didn't call her Lucia. I didn't call her Lulu. I didn't call her anything, because she wasn't my baby.

Jayme went back to work, and I was a wreck. I was pining for the little family that I thought we'd be, for the home that I thought we'd have.

I felt deeply, deeply ashamed that I wanted a baby at my age and didn't get the testing. But the tests come with a risk of miscarriage. And I had already had two miscarriages after the age of forty. I was terrified to have another miscarriage and maybe never have a baby. So Jayme and I told each other that, no matter what, this was our baby, and everything would be fine. But now I knew that, for me at least, that was not true.

I lay in bed at night with my stomach in knots, and the broken record playing in my head: I cannot do this. I am not cut out to be this kind of mother. I knew that no matter [what], she had to be cared for. She had to be raised. It wasn't her fault I felt the way I did. She didn't deserve to suffer for it.

Robot Bethany kicked in. I went to every conference, every workshop, every lecture about Down syndrome. I read so many books, and I went to every specialist appointment, and asked a hundred questions.

At night I'd watch YouTube videos of children with Down syndrome reciting the alphabet, or playing guitar, or driving a car, until I fell asleep.

I learned what sorts of activities could benefit children with Down syndrome. I took her to music classes . . . to swim classes . . . to the museum, to play groups, all with typical kids, as if that would make the world see her that way.

One mom said to me, "But why don't you have her with her own kind?"

I thought of Jim Crow, and I thought how separate is never equal. Only equal is equal. And I told that mom, "She is a child. This is her own kind."

*******

At the time I was still performing. There was a burgeoning market for mom comedy, so I just kept writing about new-mom things, never about what my personal challenges were.

I landed an audition for a mom TV comedy in Los Angeles. I went. The audition was fine. But as I was walking out, I heard the other mom comics having a conversation.

One said, "I mean, you know my kid's a little retarded, right?" They all laughed.

She said, "I mean, you've seen her, right? You have to admit she's a little bit Downsy."

My heart broke into a million pieces, but I didn't put the comics in their place. I made an excuse. I told myself that sometimes comedians say really nasty things (like that time a comedian said to me, "Aren't you too old to be pregnant? Isn't your baby gonna be retarded?").

Back at home my loneliness consumed me, and it turned to anger. Anger at family members who lived a mile away from me, but were never around. At friends who disappeared. At friends who were there, but acted as if everything was fine. I was angry at anyone who had a typical child, or a typical baby, or anybody who was pregnant and joyful.

My anger turned to despair; I was completely hopeless. Doing the right thing for the baby was my only motivation, and I went from activity to activity like a zombie.

I felt that I couldn't be the mother that she needed me to be, and be a good wife to Jayme. I told him that I wished I could move out. But really, I wished I would just die, so they could find someone better.

Then some friends invited us to vacation with them in Key West, with friends of theirs. It was all couples, with no children. I was very worried about being the one to bring the kid to the party, especially our child.

I didn't know what the couples had heard about her. I didn't know what they would think of her. I had no idea what to expect.

I gravitated to one woman in particular, and over the course of seven days, I told her everything. I told her how I was afraid that I wasn't doing enough for the baby and that I would never be able to do enough for her.

She didn't judge me. She didn't say, "Well, at least .." or "It could be worse .... " She just listened. She said that things were going to be however they were going to be-because of us and in spite of us. And that was such a relief to hear her say. She lifted a weight off my soul.

On the last day, the baby played with everyone. She threw her beach ball, and they'd catch it, and everyone would cheer. They said this was the best day of the vacation.

I had watched them get to know her, and I watched her through their eyes. She was hilarious. She was fun, she was warm, she was smart, and she definitely did things when she wanted to. She was our Lulu. Our light, and our hope.

And once I stopped fearing being this kind of mom, I realized that all moms cry a lot. All moms doubt their ability to raise [a] child. All moms worry about the future.

I used to wish I could go back in time and get that test after all, but now I wish I could go back in time and allow myself to feel the joy that a new mother feels. Because that's what I was.

We still go to our music classes, and we still go to our playgroups and the museums, with typical kids. And we go to places just for kids with Down syndrome, too.

After our long days filled with fun, we come back to the apartment. When I put my key in the door, Lulu always says, "Home, Mama." And I say, "Yes, Lulu. We are home."
```

---

## IC-0193: The Lights of Hollywood

- Title: The Lights of Hollywood
- Author (byline): Janet O’Neill
- Work: Turning Points
- Publisher: Tichenor Publishing, Inc.
- Publication date as stated: 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ACTRESS
- Teaser before the introduction: Yes
- Spoken words (computed): 973
- Already set (do not supply): none

### Source block (context only)

```text
Author: Janet O’Neill
Book: Turning Points
ISBN: 978-0742117013
Publisher: Tichenor Publishing, Inc.
Date (Month/Year): 2001
```

### Introduction (context only: never use it for content warnings)

```text
From the earliest days of Hollywood, women have been stage managed and manipulated by older men in powerful positions. The idea that female actresses, hoping to “make it big” in Hollywood, are required to accept the attentions of older male studio executives and producers, is as old as the Hollywood hills. It’s called “the casting couch” – and everyone has heard of it. But why? Why is there even a euphemism for this extreme form of sexual harassment? I’m young, I’m female, I want to see my name in lights . . . But this? This HAS to change.

The Lights of Hollywood by Janet O’Neill
```

### Performance text (classify this)

```text
ACTRESS: So you want to know why I'm here? I'm an actress. I came to Hollywood to see my name in lights. I came to act and that's what I do. For $40, I pretend to want a guy named Jack-knife. I pretend he doesn't remind me of my father. I act as if I want it. Badly. I close my eyes and pretend I'm dead. It's an advanced skill.

ACTRESS: My trip to Hollywood was destined. It was my fate. My senior year I played the role of Emily in Our Town and everyone said I was born for the stage. Are you thinking of acting for a career?, they'd say. Yes, I was. I was good. Even my drama teacher said so. When the next year rolled around and people started scurrying off to the various community colleges of the Tennessee area, I made a different trip. Hollywood. Truth be told, I wasn't in love with the acting. I never viewed it as some great art. I didn't even care about being adored on stage. It was the way they treat you when you're off stage that attracted me. The wine. The compliments. The parties. The lights.

My first audition. I was petrified. I never thought I would be, but as soon as the person before me started reading the same monologue from Our Ton, I realized I was merely a number. I had to be different. A star. I had to make them remember me. And you can bet I did that. I gave my monologue. Loudly. It was big. Then, for a reason I still can't rationalize, the words became jumbled. When I was supposed to say "Butternut tree", I said "Butternut bread". I'm sure it was a great promotion for the company. When I was supposed to say "Earth, you're too wonderful" I said "Ed, you're too wonderful". Damn my tenth-grade boyfriend! But my first audition was over. I didn't even look for call-backs. The answer was written in their laughter. They aren't laughing with you, they're laughing at you, I told myself.

Seasons changed quickly, yet California always appeared to look the same. One bad audition became two, became three, became ten. I lowered my sites. There's a ladder to climb in Hollywood. It starts with community theater, paid local theater, commercials, bit parts, TV, and then motion picture. As usual, I tried it backwards. I started with motion pictures . . . descended to community theater. They put me on stage crew. I was in charge of the lights. If only they knew.

My first break. While serving a sandwich to a man in a coffee shop, a man asked me to see him later. Said he was an agent. Oldest line in the book. I bought it. Turned out he really was. I got a job. An acting job. A real acting job. OK it was two lines in a commercial for Sunshine shoes, but it was a start. It wasn't my name in lights, but it was my face on TV. If I'd owned a TV, I would have seen it myself.

But, as fate would have it, the agent was too good to be true. Another of his clients got a job on One Life to Live out of New York and he went, too. Only about six nice people in Hollywood and a soap opera just took one of them. But he'd taught me well. I knew how to get a job now. I knew important people. Agents. Directors. One director I met was Kevin Stone. While serving a sandwich, I got him to notice me. "I'm the shoe girl!", I proclaimed too proudly. "Yes", he said, "You're very talented". Me? Talented? Sure. That's right. I forgot. He gave me his card and an appointment. Discovery was at my doorstep.

The next day, I came in for a preliminary interview. I read for a role. A lead role in a small, but artistic movie. The lead! We read scene after scene and I didn't stumble once. No butternut bread. No ex-boyfriend named Ed. Just me - putting my name in lights. I was so excited and then he said: OK, let's see your body. What? The role requires several nude scenes. Let's see your body.

Slowly, I took off all but my bra and underwear. Let's try this on more time. I need to see your body. I wanted the part so that's what I did. I wanted my name in lights, so that's what I did. I showed him my body. The next thing 1 knew he was on top of me. I wanted to tell him to be gentle, but my throat was dry. l kept thinking of my name in lights, but it wasn't enough. I kept thinking that I needed to please him, but I couldn't. He just kept on, acting as if I wasn't even there. Like this was his right. Like this was supposed to happen. Like it always happened. And I know this sounded crazy, but I screamed for my mom. I screamed for home. I screamed for anywhere but here. Not this. Not like this. It was my first time.

I was not raped that day, but I was violated.

And that's how I got here. No part. No movie. I'm not sure one even existed. But I learned a skill. Lie back; close your eyes; pretend you're dead. That's what I do. I develop my skills to take care of myself. But now I'm late. I mean I'm late. Now taking care of myself may not be enough. What am I gonna do? I find another man. I lie back. I close my eyes. Only this time I envision the lights. My name in lights. I see the brightness and then it fades to black.
```

---

## IC-0194: Lily

- Title: Lily
- Author (byline): Matt Buchanan
- Work: Not specified
- Publisher: Brooklyn Publishers
- Publication date as stated: 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MANNEQUIN, LILY, TINA, AMY
- Teaser before the introduction: No
- Spoken words (computed): 1687
- Already set (do not supply): none

### Source block (context only)

```text
Author: Matt Buchanan
ISBN: 978-1600032691
Publisher: Brooklyn Publishers
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
Time and time again we are told of the epidemic of loneliness in this country. According to Jeannette Kupfermann, researcher for The Daily Mail, one in ten people over-65 feels chronically lonely all the time, yet most suffer in silence, through fear of appearing a nuisance.

More often than not, these are not old people cut off from their families or left alone without surviving relatives. Many have family who are simply too caught up in their own lives to make time for them.

In Lily by Matt Buchan a mannequin in a dress-shop window forms a special friendship with the lonely old woman who stares through the window at her every day.
```

### Performance text (classify this)

```text
MANNEQUIN: You probably think I lead a pretty glamorous life and I guess you’re right. It’s not too bad, getting to wear all the latest styles, always the pinnacle of haute couture. But don’t envy me so easily. Sure, my clothes are always new, always expensive. But I never have any say in what I wear. Other people always choose my outfits, and some of them have very strange taste. Last Christmas I had to wear this hideous red and purple thing with what looked like tinsel streamers on the shoulders. And how would you like being dressed and undressed by strangers all the time? And it’s not like they treat you with respect. Once they took all my clothes and left me there, totally naked, for almost an entire day. Right in the window! Fortunately, I’m not anatomically correct or somebody would have been arrested. But the shame. Actually, I think it’s worse because I’m not anatomically correct. Somehow all that smooth, featureless plastic feels even more naked. That was probably the most mortifying day of my life, unless it was the time they were having a sale in Menswear and some genius decided to borrow me. They took my regular hair, gave me a bad male wig, and put me in a suit. What a disaster! I may not have all the bits and pieces, but I do have a shape. Wig or no wig, I do not look like a man! At least it was just guys shopping over there and they mostly don’t notice anything.

What’s even worse is I can’t shut my eyes. People watching is fine, and I do have a great view from my window on Main Street, but haven’t you ever not wanted to look at something? Something disgusting or upsetting? And you can look away. You can shut your eyes and pretend it’s not there. Or even just something embarrassing. Like, okay—most of the time it’s bright enough in my window and people can see right in, but during morning rush hour when the sun slants directly on my glass my window looks like a mirror from the outside. And people use it like one. Here’s a news flash for you: My window may look like a mirror to you, but from my side it’s still a window. I do not need to see you picking spinach quiche from your teeth or checking to see if your tongue is coated. It’s embarrassing! I don’t really mind people checking their hair, and sometimes it’s kind of funny to watch guys slow down to check their full-body profile, but it’s also kind of pathetic. Still, you do meet some nice people.

I met Lily about seven years ago. It was around New Year’s and I was wearing a really gorgeous ball gown. It was pale peach silk, feathery light, and cut a little like those “flapper” dresses they used to wear during Prohibition—only more formal. It was just getting dark and this really, really old lady stopped outside my window. She was a little stooped and a little chubby, with sweet snow-white curls poking out of a knit hat and bright little button eyes. She was wearing a knit shawl over a wooly coat that had been mended several times and carrying a clumpy purse and a mesh shopping bag.

She stood and gazed at me for a long time. Well, that’s nothing new—people do it all the time, and it was a beautiful gown. Then I saw that she had tears in her eyes. Slowly her arms came up until she looked like she was holding a dancing partner. Her stoop seemed to vanish, and she began to sway gracefully to music I couldn’t hear. Pretty soon she was waltzing back and forth on the sidewalk. People were hurrying past but it was like she couldn’t see them. They dodged out of her way, some of them annoyed and some with indulgent smiles, and she danced. When she finally stopped her face was shiny. She pressed her face against the glass for a last look and then walked slowly and a painfully down the street. A little while later she came back the other way with a few groceries in her mesh bag and she waved to me as she passed.

She came back the next day about the same time, with the same mesh bag and the same faraway look in her eyes. She stayed for a few moments then went on her way. A little while later she came back by with her day’s groceries.

I decided to call her Lily. I don’t know—she just seemed like a Lily to me—kind of soft and lovely and a little sad. She came by every day. Sometimes she only stayed for a moment or two, but she always stopped. Once every two weeks she’d cross the street to the little Automated Teller Machine booth at the bank.

Lily talked to me, too. She always told me what she thought of the clothes.

LILY: Oh, my dear! (shaking her head) That’s not you at all, dear! Whose idea was that, I wonder?

MANNEQUIN: That was usually when I was wearing something modern and revealing. She loved the really formal things best.

LILY: Oh, yes! (smiling brightly and giving a little clap of hands) That is gorgeous, isn’t it, dear? I wish I were you!”

MANNEQUIN: She never seemed to expect me to talk back. Sometimes people passing by would hear her and give her a look, but she ignored them and so did I.

I used to try and imagine the story of her life. I imagined a tragic love story. Her lover went down with the Titanic or died in the war overseas. I imagined she was a dancer in a speakeasy and stabbed her boss when he tried to get fresh. I imagined her as a faded movie star still trying to hang onto the lost glory. Somehow all the stories I imagined were a little sad.

I knew she had a family because I’d seen pictures. She carried a thick album in her handbag. Most of the photos were of a young woman and a small girl. Her granddaughter and great-granddaughter. She showed me the pictures at least once a week, chattering away proudly about their achievements. I learned that her granddaughter was a lawyer and sometimes sent her money, and that her great-granddaughter played the cello. But the stories never changed, and there were never any new photos. Not in six years. I began to think she’d made them up.

That’s why I was so surprised the day she brought her granddaughter to meet me. She was a little later than usual, but then here she came, with a grumpy-looking middle-aged lady in tow. It was prom season and I was in a ball gown.

LILY: There, you see! Isn’t it lovely? It’s perfect!

TINA: (impatiently) Yes, Gran, it’s very nice, but it’s a little old-fashioned. I think Amy wants something more modern.

LILY: Nonsense. Don’t you listen to her, dear. You look lovely, and not a bit old-fashioned.

TINA: (Looking around to see if anyone was staring) Honestly, Gran, you can be so exasperating! Can we go?

MANNEQUIN: Lily’s granddaughter was with her for several days. She seemed grumpier and in a bigger hurry every time I saw her, but I’d never seen Lily happier. I was sorry when she was gone and Lily was alone again.

LILY: (apologetically) Tina’s a good girl, really. She’s just got a lot on her plate. Little Amy is a dear, but she’s a handful. You know what teenagers are like. And, too, she’s a career woman. It was nice of her to visit her stuffy old Gran, even if it was only for a few days. I do wish she’d brought Amy along.

MANNEQUIN: After that it seemed like Lily was slowing down every day. One night a couple of months later she was a little behind schedule and it was dark when she shuffled across the street to the bank. It was raining steadily. I watched her disappear into the little ATM booth, wondering how much money her “career woman” granddaughter sent her. Then I saw the man. He was watching the door of the bank like a lion staking out a water hole. Inside my head I was shouting, “Stay inside! Lily, don’t come out!” But she did and I had to watch. I watched helplessly as my friend Lily was shoved roughly against the wall. She let him have her wallet without a struggle but when he tried to take the photo album she put up a fight. She scratched his face and she screamed. People started looking and one or two came running. The man panicked, shoved her hard into the wet street, and ran. And I watched helplessly as my friend Lily careened into the path of that taxi and its tires slid across the slick pavement. After the ambulance and emergency vehicles left, I saw Lily’s photo album wash into a storm drain.

It took a long time to get over losing Lily. Every afternoon I expected to see her. Wondered why she was late. Suddenly remembered. But I gradually got used to the idea that she wasn’t coming back. Lily became just a pleasant memory of an old friend, until one day almost a year later. It was prom season again, and I was wearing an old-fashioned gown very much like the one I had on the day I first met Lily. I hadn’t thought about her in weeks, when, suddenly, there she was, staring into my window with her bright, twinkling eyes. Except it wasn’t Lily. Lily was dead, and besides, this was a very young woman—maybe eighteen—and she didn’t even really look like Lily, except her eyes. She was much taller, and elegantly thin.

AMY: Mom! (calling over her shoulder as she stares at the mannequin)

MANNEQUIN: A slightly harassed-looking woman came up to her. It took me a minute to recognize Lily’s granddaughter, Tina.

AMY: You see! I told you! It’s perfect!

MANNEQUIN: Tina stood beside her daughter in my window for a long time. Tears streamed down her face. Inside, where no one could see, I cried too.
```

---

## IC-0195: Lusus Naturae

- Title: Lusus Naturae
- Author (byline): Margaret Atwood
- Work: McSweeney’s Enchanted Chamber of Astonishing Stories
- Publisher: Vintage Books
- Publication date as stated: 2004
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2147
- Already set (do not supply): none

### Source block (context only)

```text
Author: Margaret Atwood
Book: McSweeney’s Enchanted Chamber of Astonishing Stories
ISBN: 1400078741
Publisher: Vintage Books
Date(Month/Year): 2004
```

### Introduction (context only: never use it for content warnings)

```text
The doctor told us the name of the disease, which had some Ps and Rs in it and meant nothing to us. He’d only seen a case like me once before and he wanted to take me away to the city, so other doctors could look at me, but my family refused. “She’s a lusus naturae,” he’d said. “Freak of nature. It’s Latin. Like a monster. It’s nobody’s fault.” Lusus Naturae by Margaret Atwood
```

### Performance text (classify this)

```text
What could be done with me, what should be done with me? These were the same question. The possibilities were limited. The family discussed them all, lugubriously, endlessly, as they set around the kitchen table at night, with the shutters closed, eating their dry whiskery sausages and their potato soup. If I was in one of my lucid phases I would sit with them, entering into the conversation as best I could while searching out the chunks of potato in my bowl. If not, I’d be off in the darkest corner, mewing to myself and listening to the twittering voices nobody else could hear.

“She was such a lovely baby,” my mother would say. “There was nothing wrong with her.” It saddened her to have given birth to an item such as myself: it was like a reproach, a judgment. What had she done wrong?

Our family had always been respected, and even liked, more or less. It still was. It still would be, if something could be done about me.

“The doctor says it’s a disease,” said my father. He liked to claim he was a rational man. He took the newspapers. It was he who insisted that I learn to read, and he’d persisted in his encouragement, despite everything. I no longer nestled into the crook of his arm, however. He sat me on the other side of the table. Though this enforced distance painted me, I could see his point.

“Then why didn’t he give us some medicine?” said my mother. My grandmother snorted. She had her own ideas, which involved puffballs and stump water. Once she’d held my head under the water in which the dirty clothes were soaking, praying while she did it. That was to eject the demon she was convinced had flown in through my mouth and was lodged near my breastbone. My mother said she had the best of intentions, at heart.

Feed her bread, the doctor had said. She’ll want a lot of bread. That and potatoes. She’ll want to drink blood. Chicken blood will do, or the blood of a cow. Don’t let her have too much. He told us the name of the disease, which had some Ps and Rs in it and meant nothing to us. He’d only seen a case like me once before, he’d said, looking at my yellow eyes, my pink teeth, my red fingernails, the long dark hair that was sprouting on my chest and arms. He wanted to take me away to the city, so other doctors could look at me, but my family refused. “She’s a lusus naturae,” he’d said. “Freak of nature. It’s Latin. Like a monster.” He thought I couldn’t hear, because I was mewing. “It’s nobody’s fault.”

“She’s a human being,” said my father. He paid the doctor a lot of money to go away and never come back.

“Curse or disease, it doesn’t matter,” said my older sister. “Either way, no one will marry me if they find out.” I nodded my head: true enough. She was a pretty girl, and we weren’t poor, we were almost gentry. Without me, her coast would be clear.

In the daytimes I stayed shut up in my darkened room: I was getting beyond a joke. That was fine with me, because I couldn’t stand sunlight. At night, sleepless, I would roam the house, listening to the snores of the others, their yelps of nightmare.

They’d told the neighbors I had a wasting illness, a fever, a delirium. The neighbors sent eggs and cabbages; from time to time they visited, to scrounge for news, but they weren’t eager to see me: whatever it was might be catching.

It was decided that I should die. That way I would not stand in the way of my sister, I would not loom over her like a fate. “Better one happy than both miserable,” said my grandmother, who had taken to sticking garlic cloves around my door frame. I agreed to this plan, as I wanted to be helpful.

The priest was bribed; in addition to that, we appealed to his sense of compassion. Everyone likes to think they are doing good while at the same time pocketing a bag of cash, and our priest was no exception. He told me God had chosen me as a special girl, a sort of bride, you might say. He said I was called on to make sacrifices. He said my sufferings would purify my soul. He said I was lucky, because I would stay innocent all my life, no man would want to pollute me, and then I would go straight to Heaven.

He told the neighbors I had died in a saintly manner. I was put on display in a very deep coffin in a very dark room, in a white dress with a lot of white veiling over me, fitting for a virgin and useful in concealing my whiskers. I lay there for two days, though of course I could walk around at night. I held my breath when anyone entered. They tiptoed, they spoke in whispers, they didn’t come close, they were still afraid of my disease. To my mother they said I looked just like and angel.

My mother sat in the kitchen and cried as if I really had died; even my sister managed to look glum. My father wore his black suit. My grandmother baked. Everyone stuffed themselves. On the third day they filled the coffin with damp straw and carted it off to the cemetery and buried it, with prayers and a modest headstone, and three months later my sister got married. She was driven to the church in a coach, a first in our family. My coffin was a rung on her ladder.

Now that I was dead, I was freer. No one but my mother was allowed into my room, my former room as they called it. They told the neighbors they were keeping it as a shrine to my memory. They hung a picture of me on the door, a picture made when I still looked human. I didn’t know what I looked like now. I avoided mirrors.

My mother would bring me my potatoes and bread, and my cup of blood, and take away the chamber pot. Once she used to brush my hair, before it came out in handfuls; she’d been in the habit of hugging me and weeping; but she was past that now. She cam and went as quickly as she could. However she tried to hide it, she resented me, of course. There’s only so long you can feel sorry for a person before you come to feel that their affliction is an act of malice committed by them against you.

At night I had the run of the house, and then the run of the yard, and after that the run of the forest. I no longer had to worry about getting in the way of other people and their futures. As for me, I had no future. I had only a present, a present that changed – it seemed to me – along with the moon. If it weren’t for the fits, and the hours of pain, and the twittering of the voices I couldn’t understand, I might have said I was happy.

My grandmother died, then my father. My mother sank further into despair. “My poor girl,” she would say, though I was no longer exactly a girl. “Who will take care of you when I’m gone?”

There was only one answer to that: it would have to be me. I began to explore the limits of my power. I found I had a great deal more of it when unseen than when seen, and most of all when partly seen. I frightened two children in the woods, on purpose: I showed them my pink teeth, my hairy face, my red fingernails, I mewed at them, and they ran away screaming. Soon people avoided our end of the forest.

A stranger made an offer to buy our farm. My mother wanted to sell and move in with my sister and her gentry husband and her healthy growing family, whose portraits had just been painted; she could no longer manage; but how could she leave me?

“Do it,” I told her. By now my voice was a sort of growl. “I’ll vacate my room. There’s a place I can stay.” She was grateful, poor soul. She had an attachment to me, as if to a hangnail, a wart: I was hers. But she was glad to be rid of me. She’d done enough duty for a lifetime.

Once the new people had moved in, it was no trouble to get rid of them. I knew the house better than they did, its entrances, its exits. I could make my way around it in the dark. I became an apparition, then another one; I was a red-nailed hand touching a face in the moonlight; I was the sound of a rusted hinge that I made despite myself. They took to their heels, and branded our place as haunted. Then I had it to myself.

Inside our house, I tried a mirror. They say dead people can’t see their own reflections, and it was true; I could not see myself. I saw something, but that something was not myself: it looked nothing like the innocent, pretty girl I knew myself to be, at heart.

But now things are coming to an end. I’ve become too visible. I was picking blackberries in the dusk, at the verge where the meadow met the trees, and I saw two people approaching, from opposite sides. One was a young man, the other a girl.

The two of them looked furtive. I knew that look – the glances over the shoulder, the stops and starts – as I was unusually furtive myself. I crouched in the brambles to watch. They met, they twined together, they fell to the ground. Mewing noises came from them, growls, little screams. Perhaps they were having fits, both of them at once. Perhaps they were – oh, at last! – beings like myself. I crept closer to see better. They did not look like me – they were not hairy, for instance, except on their heads, and I could tell this because they had shed most of their clothing – but then, it had taken me some time to grow into what I was. They must be in the preliminary stages, I thought.

What a consolation it would be to me if I, too, could join in! Through the years I had hardened myself to loneliness; now I found that hardness dissolving. Still, I was too timorous to approach them.

One evening the young man fell asleep. The girl covered him with his cast-off shirt and kissed him on the forehead. Then she walked carefully away.

I detached myself from the brambles and came softly toward him. There he was, asleep in an oval of crushed grass, as if laid out on a platter. I’m sorry to say I lost control. I laid my red-nailed hands on him. I bit him on the neck. Was it lust or hunger? How could I tell the difference? He woke up, he saw my pink teeth, my yellow eyes; he saw my black dress fluttering; he saw me running away. He saw where.

He told the others in the village, and they began to speculate. They dug up my coffin and found it empty, and feared the worst. Now they’re marching toward this house, in the dusk, with long stakes, with torches. My sister is among them, and her husband, and the young man I kissed. I meant it to be a kiss.

What can I say to them, how can I explain myself? When demons are required someone will always be found to supply the part, and whether you step forward or are pushed is all the same in the end. “I am a human being,” I could say. But what proof do I have of that? “I am a lusus naturae! Take me to the city! I should be studied!” No hope there.

I am of a forgiving temperament; I know they have the best of intentions at heart. I’ve put on my white burial dress, my white veil, as befits a virgin. One must have a sense of occasion. The twittering voices are very loud: it’s time for me to take flight. I’ll fall from the burning rooftop like a comet, I’ll blaze like a bonfire. They’ll have to say many charms over my ashes, to make sure I’m really dead this time.

Perhaps in Heaven I’ll look like an angel. Or perhaps the angels will look like me. What a surprise that will be, for everyone else! It’s something to look forward to.
```

---

## IC-0196: A Manhattan Romance

- Title: A Manhattan Romance
- Author (byline): Joyce Carol Oates
- Work: Faithless: Tales of Transgression (Pg 209-220)
- Publisher: Perennial Press
- Publication date as stated: June 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MOMMA, DADDY, POLICE
- Teaser before the introduction: Yes
- Spoken words (computed): 1410
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joyce Carol Oates
Book: Faithless: Tales of Transgression (Pg 209-220)
ISBN: 978-0060933579
Publisher: Perennial Press
Date (Month/Year): June 2002
```

### Introduction (context only: never use it for content warnings)

```text
Divorce is a highly stressful and emotional experience for everyone involved, but children often feel that their whole world has turned upside down. Custody battles, child support and visitation rights are terms that no small child can fully understand. And for a father with limited visitation rights, a stressor that may become too much to bear. Manhattan Romance by Joyce Carol Oates
```

### Performance text (classify this)

```text
NARRATOR: (Pg 209-220) That wild day! I’d woken before it was even dawn; I seemed to know that a terrible happiness was in store. I was five years old [and] feverish with excitement when Daddy came to pick me up for our Saturday adventure as he called it.

MOMMA: (whispering) If you said you were sick, you wouldn’t have to go with – him.

NARRATOR: For she could not utter the word Daddy, and even the words your father made her mouth twist. (to Momma) Momma, I’m not sick! I’m not! (to audience) So the doorman sent Daddy up.

MOMMA: I wish you didn’t have to leave me, darling, but it’s the terms of the agreement- it’s the law.

NARRATOR: These bitter words It’s the law fell from Momma’s lips each Saturday morning. And then Momma leaned over me and kissed me; I loved Momma’s perfume and her soft-shining hair but I wanted to push away from her; I wanted to run to the door, to surprise Daddy, who took such happiness in being surprised; I wanted to say to Momma, I love Daddy better than I love you, let me go! Because Momma was Momma, but Daddy – there would never be a man so handsome and radiant as Daddy.

NARRATOR: Our driver that day was an Asian man in a neat dark uniform and gloves. Daddy no longer drove his own car. His enemies had taken his driver’s license to humiliate him, he said. They could not defeat him in any way that mattered, for he was too strong for them and too smart.

Other Saturdays, we’d gone to Radio City Music Hall, we’d seen Beauty and the Beast on Broadway; we’d seen the Big Apple Circus at Lincoln Center. Daddy liked me to smile and laugh, not to worry; not ever, ever to cry. He’d had it up to here (drawing a forefinger across her throat, like a knife blade) with crying, he said.

DADDY: Today, Princess, we’ll buy presents. That’s what we’ll do -- “store up riches.”

NARRATOR: Christmas presents? I asked.

DADDY: Sure. Christmas presents, any kind of presents. For you, and for me. Because we’re special. (smiling) You know we are special, Princess, don’t you? And all your life you’ll remember your Daddy loves you? --That’s the one true thing.

NARRATOR: Yes Daddy, I said. For of course it was so.

Daddy bought me a dark blue velvet coach, a beautiful silk scarf and a white-gold wrist watch studded with tiny emeralds. For all these wonderful presents, Daddy paid in cash. I knew it was strange for Daddy to be paying out of thick-stuffed envelopes in his inside coat pockets. No one else paid in such a way. [But, he] no longer used credit cards, he said he refused to be a cog in the network of government surveillance, he said; they would not catch him in their net; he would not play their ridiculous games.

Next, we went to the Museum of Modern Art, where Daddy lifted me to his shoulders and carried me into a large, airy room. There were tears in Daddy’s eyes as he held me in his arms -- his arms that trembled slightly – to gaze at an enormous paintings -- several paintings -- broad beautiful dreamy-blue paintings of a pond and water lilies; Daddy told me that these paintings were by a very great artist named “Mon-ay” and that there was magic in them; he told me that these paintings made him comprehend his own soul, or what his soul had been meant to be; for as soon as you left the presence of such beauty, you devoured by the crowd.

When we left the museum, I was dazed with exhaustion. I could not have said how long Daddy and I had been shopping, on our Saturday adventure; yet I loved it, that strangers observed us, and remarked how pretty I was; and to Daddy sometimes they would say, Your face is familiar, are you on TV? But Daddy just laughed and kept moving, for there was no time to spare that day.

Years later I would learn that, that afternoon, a warrant for Daddy’s arrest had been issued by the Manhattan district attorney’s office; by some of the very people for whom, until a few months ago, Daddy had worked. It would be charged against him that as a prosecuting attorney, Daddy had misused the powers of his office and blackmailed others, embezzled funds, and committed perjury. . . such charges were made against Daddy, such lies concocted by his enemies who had been jealous of him for years and wanted him destroyed. One day I would learn that New York City police detectives had come to Daddy’s apartment to arrest him but hadn’t found him. Momma told them that Daddy would be bringing me back home at 5:30 pm, or in any case he’d promised to do so; if they waited for him in the lobby downstairs would they please please not arrest him in front of his daughter. And now an alert was out in Manhattan for Daddy, he was a “wanted” man.

So exhausted! Daddy scolded me, carrying me into the lobby of the Hotel Pierre, [where he] booked a suite for us on the sixteenth floor. You could look from a window to see the apartment building on Central Park South where Momma and I lived. Once we were inside the suite Daddy bolted the door and slid the chain lock in place. There were two TVs and Daddy turned them both on. He turned on the ventilator fans in all the rooms. He took the telephone receivers off their hooks.

DADDY: (breathing hard, eyes rapidly shifting) Princess! Get up please. Don’t disappoint your Daddy.

NARRATOR: Daddy found a can of apple juice in the mini bar, poured it into a glass and added something from another little bottle.

DADDY: Princess, this is a magic potion. Drink!

NARRATOR: And so I did. A hot hurting sensation spread in my mouth and I started to choke. Daddy pressed the palm of his hand over my mouth to quiet me. I was sickish now and I was frightened; but I was happy, too; I was drunk with happiness from all we’d done that day, Daddy and me. I had never had so many presents before. I had never understood how special I was before and afterward when they asked me if I’d been afraid of my Daddy I would say no! No, I hadn’t been! Not for a minute! I love my Daddy I would say, and my Daddy loves me.

[I heard] pounding at the door. And men’s voices calling . . .

POLICE: Police! Open up Mr. _____“

NARRATOR: . . . saying Daddy’s name as I’d never heard it before. Daddy was excited and angry and he had a gun in his hand -- I knew it was a gun, I’d seen pictures of guns – and he was waving [it] as if the men on the other side of the door could see him. There was a film of sweat on his face. I had never seen my Daddy so furious calling to the policemen

DADDY: I’ve got my little girl here, my daughter -- and I’ve got a gun.

NARRATOR: But they were pounding at the door; they were breaking down the door; Daddy fired the gun into the air and pulled me into another room.

DADDY: I’ll use it, I’m not afraid – I’m not going to prison – I can’t! I’ve got my little girl here, you understand?

NARRATOR: Daddy pushed me down, panting. I was too scared to cry, [but] Daddy was crying. We were crouched in the farthest darkest corner of the room. The magic potion had made me sleepy and sickish; it was hard for me to stay awake.

POLICE: “Mr. _____ , surrender your weapon, will you? Toss it where we can see it, will you?

NARRATOR: Daddy’s face was streaked with tears like something melting. And still the voice said, calmly, so loud it seemed to come from everywhere at once,

POLICE: Mr. _____, you’re not a man to harm a little girl, we know you’re a good man, you’re not a man to harm anyone.

NARRATOR: And suddenly Daddy said . . .

DADDY: Yes! Yes, that’s right. (to daughter in a high happy voice) Princess, your Daddy loves you, that’s one true thing. Never forget, that’s the one true thing in your life of mostly lies. Good-bye, Princess!”

NARRATOR: Daddy placed the barrel of the gun deep inside his mouth. And Daddy pulled the trigger.

So it ended. It always ends. But don’t tell me there isn’t happiness. It exists, it’s there. You just have to find it, and you have to keep it, if you can. It won’t last, but it’s there.
```

---

## IC-0197: Marla, You’re On

- Title: Marla, You’re On
- Author (byline): Julianne Bernstein
- Work: More One-Act Plays for Acting Students
- Publisher: Meriwether Publishing
- Publication date as stated: July 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MARLA
- Teaser before the introduction: No
- Spoken words (computed): 1106
- Already set (do not supply): none

### Source block (context only)

```text
Author: Julianne Bernstein
Book: More One-Act Plays for Acting Students
ISBN: 1566080878
Publisher: Meriwether Publishing
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
MARTHA: You know, this whole “audition” thing, really wears on you after a while. You wait and you wait and you wait until you get one maybe, minute-and-a-half shot to leave an impression on somebody who doesn’t know or care who you are unless you can show them exactly what they want then and there. And then, one out of a million times…you get a call back. A wonderful, glorious call back. This just happens to be that one time, and tomorrow, I’ll be prepared, I’ll be ready for when that director to say “Mala, You’re On” by Julianne Bernstein.

(MARLA enters clutching a script. She closes the door behind her, takes off her jacket. She crosses to the window, opens it a little, and looks out. She doesn't see what she is looking for so she crosses to the couch and settles herself down into it as if she is about to watch her favorite old movie and does not want to be disturbed.)
```

### Performance text (classify this)

```text
MARLA: (Reading) "The Center of My Soul: A Two-Character Play in Three Acts." One more. One more reading. And it's mine. (She looks Stage Right toward the window. Crosses to it for a better view.)

(Out the window) Damn! Thought maybe the police pulled you in by now. Well, get out of here you horny high-riser! You don't impress me. Go down to the diner on Seventy-ninth Street. Meet some of the customers I wait on. You'll see. Now, move away from there. Thank you! (Toward the window) Go park yourself in front of Sharon's apartment. She's probably prepping for tomorrow as well. No. She won't. I won't. I will not let Sharon Beedles get this part. I will not. I can understand her landing that national commercial. OK, she's the Madonna of Maiden form, there's no denying. But this part. No. I will not let Sharon Beedles get this part. The only other blond, five-foot, one-inch green-eyed* actress looking for work. And she happens to be queen of the D-cups. Probably has an agent handling each one. (She takes off the note attached to the script and reads it.)

"Miss Thompson. Read over act three, scene two for final reading tomorrow." Final reading. Final audition. Final chance at any part ever again. (Pause) No, Marla, stop this.

(Reading) Act three, scene two. "Elizabeth's bedroom. Elizabeth is seated on her bed with Victor looking down at her. She reaches up to Victor's face, pulling him down to her. They kiss." Nice, I like that. I can see it, too. (As she reads the following line of dialog, MARLA’s talent as an actress should reveal itself clearly. She is a very good one, who knows what she is doing.)

(Still reading) "Don't go away this time. This is for you." (She repeats the line as she crosses to the refrigerator exploring different ways of saying it. She looks toward the window shouting out the line exuberantly and confidently.)

No! Not for you! This is for - what?! Binoculars?! Some help. (She pulls down the shade.)

(Reading) "She reaches up to Victor's face pulling him down to her. They kiss. They kiss again. She unbuttons her blouse, exposing her breasts." (She stops. Rereads.) " ... unbuttons... exposing her... " Oh. OK, her breasts. My... breasts. Yes. B-R-E-A-S-T (Pause) S. (She rereads the note.)

"Act three, scene two." Right. "Final reading... tomorrow." I'll give Sharon a call and congratulate her. (Pause) Wait a minute. It's only part of the scene. Just ... part of the scene. A natural part... of a scene. (A man whistling from outside the window is heard. She runs over and lifts up the shade.)

Hey! What are you whistling for? Maybe if you were serious, I'd - hey, you've been out there almost two weeks, now. The same thing every day for two weeks. Every single day. (Softly) Except for last Friday. What happened? (Pause) Nothing! Nothing! I didn't say... a thing. (She pulls down the shade and goes back to the script and rereads it. She starts to unbutton her blouse saying the line "Don't go away this time. This is for you." She then tries to lift it over her head but stops midway.)

Hey, uh ... I was going to call the police, but I-I'll give you a chance to explain first. (Pause) Well? (Pause) I see you scrapped the binoculars. You don't need them. I mean, there's only - (Looking down) - two taxi lanes between us. (Pause) And why don't you come out from around the side there? I mean, it looks like you're hiding ... or you're uncomfortable or something. Are you? Well ... uh ... see, I'm an actress, see, and I've almost got it. This part in this play. A real play in a theatre, you know? Finally. The thing is '" is that I have to take off my blouse. See, I need you to - You know, acting is really funny. Because most of the time when you're acting, it seems so real that it's not acting. it's more like... trying different ways to work out the same ... real... things. Oh, I don't know. You're disgusting. My boyfriend would never behave that way. Well, Bob's not exactly my boyfriend. He's this guy I've been seeing. For about three weeks now. Twice. I've been seeing him ... twice. Hey. Hey! (She goes and picks up the phone.)

Hi, Bob? It's me, Marla. You know. The casting call. The industrial for G.E. I read for the stupid housewife. Yeah. Yeah. (Pause) Right. I enjoyed it. I mean I thought they'd never call our numbers but I didn't mind waiting. Talking. Anyway, thanks for the coffee. Howard Johnson's across the street. Remember? (Pause) I can't believe I spent all my change on subway tokens. Anyway, I need someone to help me take off my blouse. No! I mean - what I mean is - there's this part. This scene. I mean - (Pause) Yeah. Me, too. I gotta go, too. Listen. Uh... maybe we'll see each other or something. Maybe we'll do lunch again. (Pause) Oh. No problem. I love that place. It was my pleasure. Yeah. (She hangs up and looks out the window. Pause) Uh ... wait a minute. Don't go away. (She crosses away into her living room.) No. I can't. He stares. A starer. Two weeks. All he's done is watch me. Look at me. And now he's ... doing the same thing. Watching ... looking ... (She goes back over to the window.)

Hey, you changed your shirt. Nice shirt. I like the color. They call it rhubarb, I think. I love food colors. You know watermelon, tangerine, champagne... Anyway, I told Bob how I felt. That I thought that there was something really good between us and we should give it a shot. From the way his artichoke salad reappeared on his plate, I don't think he agreed. (Pause) See, it's a two-character play. Two people together ... on stage ... together. And in the third act, they're nude. Making love, I suppose. But not right there on stage, though. We allude to the fact. Suggest it, you know? See, acting isn't really acting. I mean, in the script the two characters ... don't ever really do it. They actually don't ever come close. Because the lights go black and they play is over. So if they don't ever do it, what the hell is the point? (Pause) Where are you going? Are you coming back? (She remains at the window and waits for him to return.)

I don't need him, anyway. (She crosses to a record player.) Where's that old Sinatra record? (She searches through a pile of records and pulls one out. She puts it on. It is old and scratched and it starts to skip. She takes the needle off, carelessly scratching the needle along the grooves.)

Maybe the lights. (She goes over to the lights and turns them off) No. Dim. Dim. Don't go completely off. (She turns them back on.) I can't even set a mood. (She goes back toward the window.)

Hey, there you are. I am going to get this job, tomorrow. Because I'm sick of staying home every Saturday night practically making love to a script. Yeah. I do. I mean, when I pick up a script, you know, I'm real gentle-like. You don't want to push anything. If it's not good ... right ... you don't want it. It feels wrong. Because it is wrong. Wrong. See, if you're good enough at what you're doing, you know, the acting - making the acting, real, and the real, actual. It's fantastic. Because you get to be so much like the role you're playing that in a lot of ways you're not really there. And you don't have to worry about anything. Even the morning after. You know, the sequel? When you turn over. The damp Sears pillow against your cheek. And you open your eyes and don't know where the hell you are, and that's when the camera's coming in for a close-up. The script. Right next to you. Between the sheets. Lying face up. Open to the last page of the scene you were working on the night before. Sometimes, though, it's closed. Back to the beginning. Page one. Staring you in the face. (Pause) Sorry. Show's over. You can go now. Sorry.

(She walks away from the window. She stops, picks up the script, turns back to the window, looks out and smiles a half smile of recognition and relief She takes a deep breath and the lights fade to black as she starts to unbutton her blouse, repeating the line, "Don 't go away this time. This is for you.“)
```

---

## IC-0198: Master Class

- Title: Master Class
- Author (byline): Terrence McNally
- Work: Not specified
- Publisher: Penguin Group
- Publication date as stated: Dec 1995
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MARIA
- Teaser before the introduction: Yes
- Spoken words (computed): 2027
- Already set (do not supply): none

### Source block (context only)

```text
Author: Terrance McNally
ISBN: 978-0452276154
Publisher: Penguin Group
Date (Month/Year): Dec 1995
```

### Introduction (context only: never use it for content warnings)

```text
Maria Callas was a Greek-American soprano, and one of the most renowned and influential opera singers of the 20th century. Callas's most distinguishing quality was her ability to breathe life into the wide range of characters she portrayed. Critic Conrad Osborne says it also contained the seeds of her vocal decline. Callas lacked the formal training in proper technique to sustain her ambitious repertoire; and her voice was already starting to fail her by the time she was in her 40s — quite young for an opera singer.

In Master Class by Terrence McNally we join Maria Callas at the end of her career. After losing the strength of her voice, she decides to use her knowledge of opera to teach at Julliard. This is a snapshot of her teaching technique and a brief glimpse into the heart of who Maria Callas really was: Master Class by Terrence McNally
```

### Performance text (classify this)

```text
NOTE: This selection requires the actress to sing lines from Verdi’s Macbeth in Italian. At the end of this selection, you will find a link to the actual aria as sung by Maria Callas, as well as the translation of the aria. Consultation with an opera instructor is recommended.

MARIA: (Grand entrance, with bows to unheard applause, she “quiets” the phantom crowd) No applause. We’re here to work. You’re not in a theatre. This is a classroom. This is a master class. Singing is serious business. We’re going to roll up our sleeves and work. I appreciate your welcome but enough is enough.

MARIA: (looking at index cards she has been carrying) Who’s next? Lady Macbeth, Tosca, Lucia. I must say, what these students lack in voice and technique, they make up for in self-confidence. Don’t laugh. That’s important. Well, we shall see what we shall see. Next victim! That was a joke. My last one, I promise. (To 2nd Soprano) Avanti, Avanti! Don’t linger. If you’re going to enter, enter. If you don’t want to be out here, go away. Now who have we here?

2nd SOPRANO: Sharon Graham

MARIA: So Sharon Graham. What are you going to sing for us? 2nd SOPRANO: Lady Macbeth?

MARIA: The Sleepwalking Scene, I suppose. 2nd SOPRANO: No, “Vieni! T’affretta,” I thought.

MARIA: Ah, the Letter Scene! Well, that’s something. They usually all want to start with the Sleepwalking Scene. You’re humble, like me, that’s good. So. This is her entrance aria, yes? 2nd SOPRANO: Yes.

MARIA: So what are you going out here? Go away. We don’t want to see you yet. 2nd SOPRANO: You want me to go off and come back out?

MARIA: No, I want you to enter. You’re on a stage. Use it. Own it. This is opera, not a voice recital. Anyone can stand there and sing. . An artist enters and is. 2nd SOPRANO: It thought you said this was a classroom.

MARIA: (withering look) Astonish us, Sharon. 2nd SOPRANO: How do I do that?

MARIA: You can start by not entering as Sharon Graham. Enter as Lady Macbeth. Enter as Shakespeare’s Lady Macbeth. 2nd SOPRANO: I’ll do my best.

MARIA: And Sharon, may I say one more thing? That’s a beautiful gown, obviously. We’ve all been admiring it. 2nd SOPRANO: Thank you.

MARIA: But don’t ever wear anything like that before midnight at the earliest and certainly not to class. We’re talking about what’s appropriate. This is a matter class, not some Cinderella’s ball. Eh? Off you go now. And come back as her. Come back as Lady. (2nd SOPRANO exits.) Sometimes we just have to say these things, eh? I auditioned for Edward Johnson at the old Met wearing a red and white polka-dot dress, white gloves, a blue hat with a veil and what I later learned were known as “Catch me / your “F”-word-me” pumps. I’m sorry, but that’s what they were called. I was overweight and looked like and American flag singing Madame Butterfly. She’ll thank me one day. Are we ready? Begin. (Accompanist begins to play. Maria listens hard, making sounds along with it, rather than actually singing the notes). The curtain is flying up now. No Sharon yet. This is an interesting choice for an entrance. I was onstage at this point. (The music stops. No sign of the 2nd SOPRANO) Sharon? We’re all waiting. Excuse me. (She leaves the stage and comes back a moment later) No Sharon. She’s gone. If her skin is that thin, she’s not suited for this career. It’s not like I said anything about her voice. I didn’t even let her open her mouth. Next student! (2nd Soprano comes back onto the stage) 2nd SOPRANO: I’m back! (Maria looks at her blankly) I’d like to try again. I’ve been in the ladies room throwing up. I must have . . . (Maria holds up her hand to stop 2nd Soprano from going into further detail) So should I go out and come in again? (Maria nods) I’ll yell when I’m ready! (2nd Soprano exits) (Off) I’m ready! (accompanist begins entrance music again – 2nd Soprano enters at the appropriate moment. The music stops and she begins to sing) “Nel di della vittoria io le incontrai. Stupito io n’era per le udite cose;”

MARIA: Where’s your letter? You’re meant to be reading a letter. 2nd SOPRANO: I was pretending to hold one. Couldn’t you tell?

MARIA: I don’t want pretending. You’re not good enough. I want truth. This is a letter. (She seizes a piece of paper and thrusts it at Sharon.) What are you saying? 2nd SOPARNO: I’m saying “I met them on the day of victory. I was rapt in wonder at the things I heard. When the King’s messengers hailed me as Thane of Cawdor”

MARIA: Put some wonder in your voice! Thane of Cawdor! It’s what she’s dreamed of.

2nd SOPRANO: Thane of Cawdor! “A prediction made by those same seers who foretold a crown upon my head. Keep deep in your heart these secrets. Addio.”

MARIA: Do you know this speech in Shakespeare? 2nd SOPRANO: I’ve read the play, of course, but that was in high school.

MARIA: You want to sing this music without knowing your Shakespeare! 2nd SOPRANO: I’m not an actress. I’m just a singer.

MARIA: Do you think Verdi composed it without knowing his Shakespeare? Vergogna, Sharon, shame. And that wasn’t an entrance. You came on but it wasn’t an entrance. An entrance is everything. It’s how we present ourselves to an audience. It’s how we present ourselves in life. I’ll show you an entrance. You can set the scene for our colleagues. Just read from the score. (She quickly leaves the stage. The 2nd Soprano picks up and reads from Maria’s score. The accompanist begins again.) 2nd SOPRANO: “Scene Two. The grand hall in Macbeth’s castle. There are several rooms leading off it. There is a grand staircase descending from the floor above. There are two small thrones. It is night. A violent storm is raging. Thunder. Lightning. Rain. Curtain. Lady Macbeth enters at the top of the stairs. She is magnificently arraigned. She is reading a letter. (Maria has entered as Verdi’s Lady Macbeth, reading a letter.)

MARIA: “Nel di della vittoria io le incontrai. Stupito io n’era per le udite cose;”

(Maria begins to sing the first lines of Lady Macbeth’s recitative. What comes out is a cracked and broken thing. A voice in ruins. It is a terrible moment.) (Angrily) Go on, you’re the student here. Not I. And see how important a prop is? 2nd SOPRANO: You hardly looked at the letter.

MARIA: (condescendingly) She has it memorized. She’s read it over and over and over. My choice. Not Verdi’s. Not Shakespeare’s. Callas. You think you can do that now? 2nd SOPRANO: Not like you.

MARIA: I don’t want it done like me. I want it done like Verdi. With music. This isn’t a play. 2nd SOPRANO: “Ambizioso spirit tu sei Macbetto.”

MARIA: There’s two “t’s” in Macbetto. I want to hear them. 2nd SOPRANO: Mac –

MARIA: Don’t repeat, keep going! 2nd SOPRANO: “Alla grandezza aneli, ma sari tu malvagio?”

MARIA: “You would be great, but will you be wicked?” Ah, there’s the question! Don’t even think of stopping! You are Lady Macbeth! (Maria circles the 2nd Soprano, working with her) Use this introduction to focus yourself. Why are you moving your hand? Never move your hand unless you follow it with your heart and soul. 2nd SOPRANO: How do I know when to move at all?

MARIA: The composer tells you. It’s all in the music. Now! 2nd SOPRANO: “Vieni! T-affretta! Accendere”

MARIA: Bite into those words. Spit them out. 2nd SOPRANO: “Ti vo’ quell freddo core!”

MARIA: Let yourself go. Who are you saving it for? The melody broadens here. Let it through you. 2nd SOPRANO: “Le profetesse il trono.”

MARIA: The throne of Scotland has been promised to him! What is he waiting for? This is important to you! You make we want to shake you, Sharon! 2nd SOPRANO: Ascendivi a regnar. Che tardi?”

MARIA: What are you waiting for? Acccept the gift. Take what I’m giving you.

2nd SOPRANO: Che tardi? Accetta il dono, Ascendi, ascendi, ascendivi a regnar.”

MARIA: Rise and rule. Rise and take your place in this world. This isn’t just an opera. This is your life. Am I right? So what happens here? Hurry up, you’re running out of steam. 2nd SOPRANO: Someone comes in an

MARIA: Not someone. Noone is someone. 2nd SOPRANO: A servant.

MARIA: Now you’re talking! 2nd SOPRANO: He tells her that the king, Duncan! Will be at their castle that very evening.

MARIA: Is Macbeth with him? 2nd SOPARANO: Yes!

MARIA: And how does that make her feel? 2nd SOPRANO: Happy?

MARIA: Don’t keep looking at me for answers, Sharon. Tell me, show me. Vite, vite! What is she going to do about it? 2nd SOPRANO: She’s going to sing a cabaletta!

MARIA: She’s going to kill the King! Do you know what that means? 2nd SOPRANO: Yes, it’s terrible.

MARIA: Not to her! Do you believe women can have balls, Sharon? 2nd SOPRANO: Some women. Yes, I do!

MARIA: Verdi is daring you to show us yours, Sharon. Will you do it? 2nd SOPRANO: Yes!

MARIA: Tonight! It’s now or never. She’s going crazy here. It’s all in the music. Listen to those dissonances. Don’t act, listen. It’s always in the music, Sharon. Don’t look at me for help. Listen to Verdi, listen to Shakespeare.

2nd SOPRANO: Or tutti sorgete, ministry infernali
Che al sangue incorate –
Spingeti I mortali! Che al sangue incoret mortali!
Tu note ne avvolgi –
Di tenebra immota”

MARIA: Is there anything you would kill for, Sharon? A man, a career? 2nd SOPRANO: Not off the top of my head.

MARIA: You have to listen to something in yourself to sing this difficult music. These people really existed. Lady Macbeth. Or don’t you believe that? Eh? This is all make-believe to you? 2nd SOPARANO: I’ve never really through about it.

MARIA: That’s because you’re young. You will. In time. Know how much suffering there can be in store for a woman. 2nd SOPRANO: But you were young when you first sang Lady Macbeth.

MARIA: I was never young. I couldn’t afford to be. Not to get to where I was going. Anyway. Enough of that. You came back. You had mut. That’s something. Do you know that German word? It means courage. I had to know it when I sand Fidelio for the Germans during the Occupation during the way. It was at the Theatre Herod Atticus in Athens. I was 18 years old. I needed lots of mut that day. Mut. 2nd SOPRANO: DO you want me to do it again?

MARIA: Yes! Off you go now (2nd Soprano exits) And this is for all of you: there are no short cuts in art, no easy ways. This isn’t life, where there are so many. There is no being at center stage as if by magic. There is always an entrance first, just as there is always an exit after. Art is about those transitions. There is only discipline, technique and mut. Are you ready back there? What is her name? Are you ready back there, Sharon?

2nd SOPRANO: I think so.

MARIA: Don’t think, don’t hope, do. Mut, Sharon, mut. Every eye is on you. 2nd SOPRANO: “Nel di della vittoria io le incontrai. Stupito io n’era per le udite cose;”

MARIA: (steps out of scene) Let me be her. That sound of the curting parting. The stage dust. Don’t breathe it in. They see me. “Who is this fat Greek girl we never heard of making her debut?” Ah! The silence. It’s time. Begin. “Nel di della vittoria io le incontrai. Stupito io n’era per le udite cose;”

MARIA: That’s who I am! This voice. Ah, Verdi! Ah, Shakespeare! Ah, my own ambition. IN less than one year I’ve become the Queen of La Scala. That has to count for something. La Divina. Imagine being called La Divina. I am La Divina. Listen to that! I’ve won. I’ve made something of myself. 2nd SOPRANO: (breaking into her thoughts) Mme. Callas?

MARIA: Sshh! Listen, they’re applauding. Never move on your applause. It shortens it. 2nd SOPRANO: No one was applauding. You told them not to.

MARIA: (sadly, broken) I would never tell anyone that, ma chere. The worst part about being a teacher is being misunderstood. Applause is what we live on. Sometimes it’s the only thing we have. . . . (hardening her outer shell again) I think you have a lovely voice. [But] it takes more than a pretty voice to build a career. 2nd SOPRANO: I wish I’d never done this. I don’t like you. You can’t sing anymore and you’re envious of anyone younger who can. You just want us to sing like you, recklessly, and lose our voices in 20 years like you do. Well, I won’t do it. I don’t want to. I don’t want to sing like you. I hate people like you. You want to make the world dangerous for everyone just because it was for you. (She leaves – awkward silence)

MARIA: So. I think we should stop here. Miss Graham thought I wanted her to sing like Maria Callas. No one can sing like Maria Callas. I am very upset. I’m hurt. As strange as it may seem to some of you, I have feeling too. Maybe this whole business of teaching is a mistake. Do not think singing is an easy career. It is a lifetime’s work; it does not stop here. Whether I continue singing or not doesn’t matter. What matters is that you use whatever you have learned wisely. Think of the expression of the words, of good diction, and of your own deep feelings. The only thanks I ask is that you sing properly and honestly. If you do this, I will feel repaid. (She gathers her things and exits. Blackout)
```

---

## IC-0199: A Medal for Willie

- Title: A Medal for Willie
- Author (byline): William Branch
- Work: Black Drama Anthology
- Publisher: Plume
- Publication date as stated: June 1986
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MRS JACKSON
- Teaser before the introduction: No
- Spoken words (computed): 746
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Branch
Book: Black Drama Anthology
ISBN: 978-0452009028
Publisher: Plume
Date (Month/Year): June 1986
```

### Introduction (context only: never use it for content warnings)

```text
Mrs. Jackson is the mother of a Black American soldier killed in action while fighting in the Vietnam War. The stage of the auditorium of a Black high school in a Southern town following the presentation to Mrs. Jackson of her son’s medal for bravery by a three-star general from Washington and local White officials. She has changed her mind and tries to give the medal back. They ask her why . . . A Medal for Willie by William Branch.
```

### Performance text (classify this)

```text
MRS JACKSON: Why? All right then. I’ll tell you why. You asked me. Now I’m gonna tell you [She begins quietly and builds in intensity, a tower of strength and emotion.] I didn’t want to go through with this program an’ all, to begin with. But standin’ here just now, readin’ off them words, I knew I just can’t! I can’t be that much of a hypocrite, not even for Willie. You all ‘spect me to ‘cept this medal and read that speech you had all ready for me, say, “Thank you kindly, suhs,” and then go home an’ be happy about the whole thing. But I can’t! I can’t go through with this, this big LIE.

Yes, I said a lie. What has all your fine talk ever meant to Willie. He walked around this town nearly all his young life and nobody cared. You Jim-Crowed him and shunned him and you shoved him off in a corner. You gave him a third-rate schoolin’ and when he wasn’t quiet like a mouse, you put him out in the street. You looked down on him and kept him down ‘cause he was black and poor and didn’t know no better than to believe that was the way things is supposed to be!

Yes, my Willie was dumb in a lotta ways. He didn’t know nothin’ ‘bout no I-de-lol-logies or whatever you calls it. He wasn’t fightin’ ‘cause he hated anybody. He joined the Army ‘cause he couldn’t get a decent job here. Willie thought if he did what they told him in the Army and he didn’t get in no trouble, maybe someday he could come back home and walk down the street and be somebody. Willie tried so hard, he got himself killed. But he didn’t know. ‘Cause even while you-all’s here supposed to be honorin’ Willie, you keep talkin’ ‘bout keepin’ things the way they always is. Willie didn’t want things to stay the way they is. ‘Cause it always meant he come out holdin’ the short end of the stick - the Jim Crow end, the poor folks end.

That’s why this is all such a big lie. You-all here ain’t really honorin’ Willie. You here tryin’ to tell yourself that you been right all along. That the way you been doin’ things is perfectly okay ‘cause you can get boys like Willie to go out and fight and die for you and never know the difference. And you tryin’ to use me and my dead boys’ memory to make out like everybody’s all satisfied here in the land of the free, that we’s all one big happy family. Who’s just tickled to death with the American Way!

Well, I don’t know nothin’ ‘bout no other kinda way. I ain’t never been on no trips to Europe or Russia or China or any of them places that I hears the man talk about on the radio, and I don’t know what they does anywhere else. But I do know a whole lot ‘bout right here from my whole life of experience. And I say I don’t like everything the way it is! And it’s high time - way past time that a lot more changes were made! So that folks like my boy and your boy will have the same chance as anybody else to grow up and enjoy life and live like decent fold without no holdbacks ‘cause they’re colored.

Yes, Willie’s dead and gone now, and I’m proud he was brave and helped save somebody else ‘fore he got killed. But I can’t help thinkin’ Willie died fightin’ in the wrong place.

[Quietly intense] Willie should had that machine gun over here!

So you can take this medal back on up to Washington and tell them I don’t want it! Take it back. Pin it on your own shirt! Five it to the ones who keeps this big lie goin’ and send boys like my Willie all over the world to die for some kinda freedom and democracy they always gets the leavin’s of! You done a pretty good job. You had folks fooled a long time with all this honey-talk, an’ you even had me readin’ off your words for you. But I done woke up! I knows what you’re tryin’ to do and I ain’t gonna let you do it to me no more! Here! Take it back! [She hurls the medal at the General.]
```

---

## IC-0200: Medea Redux

- Title: Medea Redux
- Author (byline): Neil LaBute
- Work: Bash - Latterday Plays, Pgs 75-94
- Publisher: The Overlook Press
- Publication date as stated: Nov 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 2957
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil LaBute
Book: Bash - Latterday Plays, Pgs 75-94
ISBN: 978-1585670246
Publisher: The Overlook Press
Date (Month/Year): Nov 1999
```

### Introduction (context only: never use it for content warnings)

```text
Medea by Euripides is a tale from Greek mythology which illustrates how the relentless pursuit of vengeance can be taken to its furthest extreme. In the story, Medea is driven by a passionate desire to right the wrongs done to her -- she sacrifices even her own children in the pursuit of revenge.

In this selection, Medea Redux by Neil LaBute, our tragic heroine tells a police investigator her tale of what she feels is ultimately revenge. But we are left to question whether her actions are those of vengeance or are driven by the damaged mind and soul of an abused 13-year-old, who once placed her unfailing trust in a teacher . . . a middle school teacher.

Medea by Neil LaBute
```

### Performance text (classify this)

```text
WOMAN: (Pg 75-94) . . . can I just speak? 's that okay? I mean, I'll talk about, but . . . I got 'a sort of ease into it, you know? 'cause I was never, like, this major talker or anything . . . like to keep things to myself. Some people'd call it "private" or whatever, but it's more like just being sort'a "inward" right? I'm an inward kind 'a person . . .

WOMAN: I think it depends a lot on the way you grow up, you know, family and all, and I just ended up more inward than anything . . . it's interesting, you know, how things'll work out. Well, not "out," I guess not so much that as maybe just "through" right? Things get worked through . . . or work themselves through. We probably don't have all that much to do with it. We like to think we do, though, right? God, like we're in on all the big planetary decisions you know? but, uh-uh . . . you wanna know what I feel, I think we're just spinning around out here, completely out 'a whack and no way of ever getting it right again, I mean, back on track or whatever . . . just can't do it. see, we been doing things wrong for so long now that it all starts to feel okay after a while, you know, like this is how it oughta be. (beat) there's a Greek word for that . . . I learned it in school. He taught it to me . . . well, I guess I more like "heard" it from him, if I'd 'a learned it I could tell you what it is, right? Yeah. I know it's Greek, though, I caught that much, but I don't remember what it was . . . (thinks quietly) no . . . 's too long ago now. Had something to do with the world, the whole thing, coming off its axis or something, going off in the wrong direction from how it's all supposed to be. And it’s the fault of people. or "mortals," that's what my teacher said, "mortals are to blame." See, he said it was simply the fact that - and I never could understand this, maybe I just didn't listen good enough, that was the usual problem-but he said it all stemmed from just our being mortal. Right? (beat) So, then every problem we got is from being mortals. Explain me that . . .

You know a lot of times I just couldn't make clear what was coming out'a his mouth. He was really smart, though, had, like, two college degrees or something, and still wanted to work at public school. I kind 'a admired that. I was in his class, one of 'em, his first year. 's great . . . he took us, my class anyway, on a bunch 'a stuff, field trips, like museums, and up to Chicago one time. That was fun.

You know what's funny? He hit on me; my teacher did, on one of those trips. Yeah. . . scared me! I didn't even know what he was doing at first - I mean, okay, I did, but I was, like, thirteen - and that's just not what you're expecting at that age. Well, maybe it never is . . . he came up behind me at the observation tank, right, where they've got the sharks and everything . . . (beat) well, I'm keeping my eye on this one big hammerhead, and he's darting in real close to the glass, suddenly, I feel all this weight up against me. My teacher is pushing me forward with his body, up onto the observation windows, and I can't move. He never said anything while it was happening, I mean, to me - I could hear him whispering something about the "tragic nobility of sea creatures," some shit like that - and all I can see, I can't turn at all, the way he's got me held there, all I can see is this shark, the one I'd been watching, coming out of the murk and sweeping past me, again and again . . . He turns past the glass at the last second and his eye just sort'a rolls back all white as he passes . . . that was scary. I've never forgotten it. That feeling. His weight on me, and watching as that hammerhead just kept circling around... (beat) well, what the hell, it's easy to scare a kid. Right?

Anyway, he wouldn't look at me after that, my teacher, not even a glance, the whole rest of the trip. And he was always real nice before, and funny to me . . . I mean, not in a bad way, not like inappropriately so, I don't think, but - no, I wasn't even a "teacher's pet" or whatever - he was just sort'a open with me. Jokes, and showing me pictures in magazines, like, we were starting to be friends, I thought. At least sort of friendly. Because it's hard, I think, for a teacher in school, like Junior high, where nobody cares, so, if you meet a person who is actually interested, like I was, and I really was - I wasn't the smartest or remembered the most, like I said, but - I was genuinely interested in things. I wanted to learn, right, I felt like I needed to comprehend a little about the universe, you know? I did. 'Cause it intrigues me. The way it works. Yeah. (beat) and I think a teacher can pick up on that. And he just responded to it . . . so, we started to sort 'a hang out a bit . . . just at school. The library, or looking at slides in the resource center. Lunchtimes. (beat)

I mean, I was thirteen, okay; it was nice to have somebody look at you and not say to pick up your socks . . . something like that. Let's face it; thirteen's a pretty bad age, right? (pause) He did give me a ride home, though. From school. He did do that. I mean, nothing, not a look on the outing, sits way away from me on the bus, but back at our building, see, he's responsible for us, and all the parents are there, this is a Friday, and my dad doesn't show. We go into the office, call his work, nothing at home, and he doesn't come. Half-hour goes by, nobody at school but us. Sitting there on the curb, waiting for my dad. Finally he says, my teacher, he said he'd run me home if I'd like that's what he said, "if you'd like that." (beat) in the car, like this was yesterday, I recall he had this woman singing on the tape player, real soft and painful, I remember, 'cause I had to ask who this was. I mean, this was not the Bee Bees and I'd never heard anything like it. So fragile-sounding, you know? First thing he'd said to me, I mean, practically, in five hours is "Billie Holiday." And he smiled, and he says, "She's all I ever listen to." And then, "you kind of remind me of her, you know? You always seem just a little bit sad. Smiling, but sad. I like that. . . (beat)

What did that mean? You know? Because, listen, you don't say stuff like that to a thirteen-year-old, okay? You just don't, uh-uh, 'cause she'll be yours for life. I mean it. if you do, she will be . . . (Pause) not in front of my house, but down from it, a block maybe, he pulls over, there's a florist shop and he parks in the little lot they have there . . . he kissed me. . . I really don't wanna, umm, elaborate too much on, well, you know, cover all the relationship stuff a whole lot, 'cause if you've talked to him you know it already, anyway, right? Maybe more than you want to . . . (beat)

We started seeing each other, you know, as much as a junior high school teacher and a thirteen-year-old can see each other. And I know what you're thinking, or have thought it to each other, laughing and stuff, that it's my own fault or that he was some type 'a molester, whatever, but you wouldn't really be true about that. We, umm . . . just liked each other. (pause) My fourteenth birthday . . . 's in March, he, umm, picked me up at the library, and we went driving. I asked where but he said, "It's a surprise," so I sat back the sun roof was up, it's a real nice day out, and just kind 'a drifted off to the sound of the wind rushing by. The wind and Billie Holiday singing sad on the back speakers . . . (stops, gathering her thoughts). When we got to Chicago, he drove straight to the lake, to this pier where he'd rented a boat for us, beautiful red speedboat, and God; it was so exciting for me! He just kept doing things like this, and there's a picnic basket and it was great, just great . . . to be out there, in the water, on this boat with him, it was just real lovely . . . (beat)

He gave me a bracelet, it was all wrapped up, in wax paper, inside my sandwich! Yeah, you believe that, he'd hollowed out my bread and put my present inside there, and I loved that, that was just cute . . . and I got, ahh, this beautiful, like, picture book of Greek stories, mostly of Euripides, 'cause, see, he felt Euripides was the most, what, "humanistic . . . had, like, the most humanity of the Greek writers. He said he was the one most at war with this . . . (beat) Still can't think of that word, but he was the guy who was really angry about the world being all messed up just because we happened to be mortals . . . anyhow, it had a bunch 'a nice drawings and he said I'd like it even more as I got older... (beat) I still have it.

(silence)

I, umm . . . found out about the baby, that I was going to have one, in late April, the 23rd, I guess, and I didn't cry. You know, but sometimes you can go along, years even, and not feel like you're growing up at all, and then there's times when you age a ton, like, in a couple'a seconds. You know? So, I found out and went straight to his place, I mean, called first, but went there and we discussed it all. Talked a long time . . . (beat) we talked, like I said, and, you know, he seemed, and this caught me, 'cause I didn't know what he'd think, but he was all excited! Not yelling, and said he loved children, could think of nothing better than having a son or something. Said we'd have to be careful I mean, we both understood the situation - but I promised him I wouldn't tell anybody who the father was. I said I'd keep our secret . . . we made a pledge together, there on his sofa, and I kept it. (beat)

He told me that day, he said he had to go away for a couple weeks, just the end of summer, he was finishing up another of his degrees at Delphi, that's a university, and then we'd, you know, make some plans. (beat) That was hard, 'cause I was scared, I'm not gonna pretend I wasn't, but getting his degree was a big thing, and could help us, too, he said , , , and so we talked for awhile, and we kissed. God, you know for being this big guy, he was really gentle to me . . . (beat) Okay. Umm, what else? Ahh . . . when I found out he'd left his position at school - this was by a fluke, anyway, I was at the general office during the summer, bringing them a vaccination report on my brother, and the lady there, the secretary, said, "oh, I heard about your arts and sciences teacher at Gardner," my school, "we're sure sorry to lose him, aren't we?" I didn't hear much else, really, just that she said, "Well, I suppose they need good teachers in Phoenix as much as they do anywhere . . . “ (beat)

But there's a bunch 'a crap you don't need to hear twice, and I don't want your sympathy, okay, I don't, so we'll skip the hardship stuff about when I did tell my family, and being pulled out 'a school, the move to my aunt's house . . . sound familiar? I told you before, or if I didn't, I meant to . . . this story's nothing special; really, practically the only part that's of any interest is that it happened to me . . . you know? (beat)

Anyways, Billie, that's my son, Billie, "William," whatever . . . was born. A beautiful boy. Just great, and although every mom goes off on that, he was. I mean it. He's great, and, umm, I give birth and a bunch'a years pass. Okay? I did finally make contact with his father, sent a couple letters, and he wrote me back right away, this was, ohh, maybe a year, eighteen months later and asked if I could understand. Not forgive . . . understand. (beat) I, ahh, let him know that our pact was still safe, and this wasn't, like, some money thing, I just wanted him to have, if he wouldn't mind so much, a sort 'a relationship with Billie, through the mail or whatever. I knew there was nothing for us, well, you know, not after that . . . but I'd send pictures and stuff, we ended up doing it through a postal box, and he got to know his son that way. That's how it happened. A few presents now and again, and he had a son, and the son's mother loved him, and kept the secret all while the father was away. (long pause)

The rest you know . . . on his fourteenth birthday, Billie and me, we rented a car - we were living in Utah by then, out with some Mormon relatives at that point - and we drove to Arizona to meet his father. We'd planned this, the two of us, by letter, and agreed it'd be just the one time . . . he was, umm, you know, married by this time, married and teaching in Phoenix. No children, though, isn't that funny? No kids 'cause his wife had a part of her uterus, I guess, some thing, that wouldn't work properly. I thought that was the only real sad part 'a all this - so, it'd just be this once, at a motel that he'd picked in town. One time when we'd all sit down and see each other. Again. At least, the two of us, again . . . (beat)

We met at the room. 's a terribly hot day, at least for December it was, ’s how I remember it, anyway, and we were tired from the travel, but he was there and it was this big moment for Billie, 's all excited, and we even hugged, and it was in that second, as he leaned in to kiss my cheek, his head turned toward me and maybe it was just the light, the sun coming in the room, but I saw something there, there in his eyes . . . he loved this boy, all that he'd said to me years ago, it was true about kids. He loved 'em. But also . . . he was satisfied. I could see that, satisfaction on his face . . . because he'd gotten away with it all. That's what I saw, shining in his eyes, as he moved forward to kiss me. He'd beaten fate . . . and gotten away with it. (beat)

After dinner he said he wanted to see us again before we left. He had to run to school for about an hour, a science fair, I guess, but he'd be back. He promised he'd be right back. The last time I saw him, there at the door, he mentioned that word, that . . . umm, well, whatever, he said it and smiled, as he stepped out onto the balcony he smiled to me and whispered, "Maybe it's not our fault after all. I mean, we're just human, right?"(pause).

Billie was already in the bathroom and I could hear the water running. He was in his bath. God, he loved the tub! Since he was tiny, he loved it. So, I knew he was in there, the water filling up around him, and "lady day" - 's what he liked to call Billie Holiday, playing on his tape player. "Stormy weather." I, ahh, went into the room, the bathroom, and I could see him there, through a little opening in the liner he had pulled shut, eyes closed and the steam coming up.

He didn't really struggle, couldn't actually, the shock of it, I suppose, when the recorder first hit the water . . . there was really only a quick kind 'a snapping sound, like the pop of a flashbulb or whatnot, and then the softer sound of him, Billie, as he kicked a second or two in the water. I turned the taps off a little later . . . (beat)

After, I just sat there, on the linoleum, and watched him, lying in that cloudy pool of bath water. His eyes open and so still. (pause) “Adakia," that's the word. The word I was trying, you know, that's it. "The world out of balance." I knew it'd come to me, if I waited long enough. I was picked up in Vegas, at a restaurant, you're aware of that, though, obviously . . . and brought back here. And that's it. So, now you know. I mean, what you really wanted, anyway, right? Now you know . . . yes. I planned it, yes. But . . . maybe longer than you thought, huh? Lots longer . . . (laughs to herself). But I’ll tell you. Tell you what gets me through today, the next hour . . . it's him. (pause) I can almost see 'em, you know, I can, down there in Phoenix. Can't be consoled, right, the truth all spilled out now like it is, and all these tears running down, yelling up at the sky, these torrents of tears and screaming, the top of his lungs, calling up into the universe, "Why?! Why?!!" over and over. (beat) but you know what? In my fantasy, there's never an answer. Uh-uh. There never is . . .
```
