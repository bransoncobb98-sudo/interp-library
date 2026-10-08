# Classification request: batch 52 of 63 (40 records, IC-2041 to IC-2080)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-052-reply.json`.

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

## IC-2041: Here We Are

- Title: Here We Are
- Author (byline): Dorothy Parker
- Work: Not specified
- Publisher: Travelman Publishing
- Publication date as stated: Oct 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1904
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dorothy Parker
ISBN: 978-1860920172
Publisher: Travelman Publishing
Date (Month/Year): Oct 2001
```

### Introduction (context only: never use it for content warnings)

```text
Anyone who has been married knows the real truth that marriage is hard work and, while it might get easier over time, marriage always takes effort. – At least that’s what I’ve been told.

Sure, engagement is exciting and happy and planning a wedding can be fun, even thrilling at times. But the real nitty-gritty that happens once you've said your "I do's" is what people rarely talk or think about beforehand.

So . . . . . Here We are by Dorothy Parker
```

### Performance text (classify this)

```text
The young man in the new blue suit finished arranging the glistening luggage in tight corners of the Pullman compartment. He sat down, leaning back in the seat opposite the girl in beige. She looked as new as a peeled egg. Her hat, her fur, her frock, her gloves were glossy and stiff with novelty.

She had been staring raptly out of the window, but as the young man sat down, she turned politely from the pane, met his eyes, started a smile and got it about half done, and rested her gaze just above his right shoulder.

"Well, here we are," he said.

"Here we are," she said. "Aren't we?"

"Well!" he said. "How does it feel to be an old married lady?"

"Oh, it's too soon to ask me that," she said. "At least-I mean. Well, I mean, goodness, we've only been married about three hours, haven't we?"

The young man studied his wrist-watch as if he were just acquiring the knack of reading time. "We have been married," he said, "exactly two hours and twenty-six minutes."

"My," she said. "It seems like longer. I didn't have any idea what time it was. Getting back from the church, and then all those people, and then changing all my clothes, and then everybody throwing things. Goodness, I don't see how people do it every day."

"Do what?" he said.

"Get married," she said. "When you think of all the people, all over the world, getting married just as if it was nothing."

"Well, let's not worry about people all over the world," he said. "We've got something better to think about."

"I know," she said. "But it's sort of such a big thing to do, it makes you feel queer. How does anybody know what's going to happen next?"

“We know darn well what's going to happen next,” he said. “I mean. I mean-well,we know we're going to be happy. Don't we?"

"Oh, of course," she said. "Only . . . an awful lot of people that get married, it doesn't turn out so well. And I guess they all must have thought it was going to be great."

"Come on, now," he said. "This is no way to start a honeymoon. Look at us-all married and the wedding all done and all."

"Ah, it was nice, wasn't it?" she said. ""Ellie and Louise looked lovely, didn't they?"

"Listen," he said. "When I was standing up there in that old church waiting for you to come up, and I saw those two bridesmaids, I thought to myself, I thought, 'Well, I never knew Louise could look like that!' Why, she'd have knocked anybody's eye out. "Boy!"

"I'm terribly glad you thought so," she said. "How did you think Ellie looked?"

"Why, I honestly didn't get a look at her," he said.

"Oh, really?" she said. "Well, I never saw anybody look as beautiful as Ellie looked today. And you didn't even notice her. But you never pay attention to Ellie, anyway. Don't think I haven't noticed it. It makes me feel just terrible. It makes me feel just awful, that you don't like my own sister."

"I do like her!" he said. "I'm crazy for Ellie. I think she's a great kid."

"Don't think it makes any difference to Ellie!" she said. "It isn't anything to her whether you like her or not. The only thing is, it makes it awfully hard for me that you don't like her. It's going to be awfully hard for me that you won't want my own sister to come and see me. It's going to make it awfully hard for me that you won't ever want my family around. I know how you feel about my family. Don't think I haven't seen it!"

"Oh, now, come on!" he said. "What's all this talk about not wanting your family around? Why, you know how I feel about your family. I think your old lady-I think your mother's swell. And Ellie. And your father. What's all this talk?"

"Well," she said. "Lots of people get married, and they think it's going to be great, and then it all goes to pieces because people don't like people's families.”

"Honey," he said, "what is all this? What are you getting all angry about? Hey, look, this is our honeymoon. What are you trying to start a fight for?"

"Ah, I'm sorry I was cross," she said. "Yes, don't let's ever fight. We won't be like a whole lot of them. We won't fight or be nasty or anything. Will we?"

"You bet your life we won't," he said.

"I guess I will take this darned old hat off," she said. "Do you like it, sweetheart . . .do you really like it?"

"Well, I'll tell you," he said. "I know this is the new style and everything like that, and it's probably great. Only I like the kind of a hat like that blue hat you had. Gee, I liked that hat."

"Oh, really?" she said. "Well, that's nice. The first thing you say to me, as soon as you get me off on a train away from my family and everything, is that you don't like my hat."

"Now, honey," he said, "I never said anything like that. I only said--I don't know anything about hats. I'll be crazy about this one as soon as I get used to it. What do I know about women's hats?"

"It's too bad," she said, "you didn't marry somebody that would get the kind of hats you'd like. Why didn't you marry Louise? You always think she looks so beautiful."

"Ah, now, honey," he said. "For heaven's sakes!"

"All you've done, ever since we got on this train, is talk about her. Here I've sat and listened to you saying how wonderful Louise is. Why didn't you ask her to marry you? I'm sure you'd have been much happier."

"Listen, baby," he said, "while you're talking about things like that, why didn't you marry Joe Brooks?"

"Well, I'm not so sure I'm not sorry I didn't," she said. "There! Joe Brooks wouldn't have waited until he got me all off alone and then sneered at my taste in clothes. Joe Brooks has always been fond of me!"

"Yeah," he said. "He's fond of you. He was so fond of you he didn't even send a wedding present. That's how fond of you he was."

"I happen to know for a fact," she said, "that he was away on business, and as soon as he comes back he's going to give me anything I want, for the apartment."

"Listen," he said. "I don't want anything he gives you in our apartment. Anything he gives you, I'll throw right out the window. That's what I think of your friend Joe Brooks. And how do you know where he is and what he's going to do, anyway? Has he been writing to you?"

"I suppose my friends can correspond with me," she said. "I didn't hear there was any law against that."

"Well, I suppose they can't!" he said. "And what do you think of that? I'm not going to have my wife getting a lot of letters from cheap traveling salesmen!"

"Joe Brooks is not a cheap traveling salesman!" she said. "You've got a lot of right to talk about Joe Brooks," she said. "You and your friend Louise. All you ever talk about is Louise."

"Oh, for heaven's sakes!" he said. "What do I care about Louise? I just thought she was a friend of yours, that's all. That's why I ever even noticed her."

"Well, you certainly took an awful lot of notice of her today," she said. "On our wedding day! You said yourself when you were standing there in the church you just kept thinking of her. Right up at the altar. Oh, right in the presence of God! And all you thought about was Louise."

"Listen, honey," he said, "I never should have said that. I was just telling you that because it was so kind of crazy. I thought it would make you laugh."

"Well, it didn't," she said.

"No, I know it didn't," he said. "It certainly did not. Ah, baby, and we ought to be laughing, too. Hell, honey lamb, this is our honeymoon. What's the matter?"

"I don't know," she said. "We used to squabble a lot when we were going together and then engaged and everything, but I thought everything would be so different as soon as you were married.”

"Well, we haven't got much longer to wait now," he said. "I mean-well, we'll be in New York in about twenty minutes. Then we can have dinner, and sort of see what we feel like doing. Would you like to go to a show or something?"

"Why, whatever you like," she said. "I sort of didn't think people went to theaters and things on their-I mean, I've got a couple of letters I simply must write. Don't let me forget."

"Oh," he said. "You're going to write letters tonight? I thought when we got in, we could go right up to the Biltmore and maybe have a little dinner in the room, kind of quiet, and then do whatever we wanted. I mean. I mean-well, let's go right up there from the station."

"Oh, yes, let's," she said. "I'm so glad we're going to the Biltmore. I just love it. I always sleep so well there. I go right off to sleep the minute I put my head on the pillow."

"Oh, you do?" he said. He rose, balanced a moment, crossed over and sat down beside her.

"Do you really have to write those letters tonight?" he said.

"Well," she said, "I don't suppose they'd get there any quicker than if I wrote them tomorrow."

There was a silence with things going on in it. "And we won't ever fight any more, will we?" he said.

"Oh, no," she said. "Not ever! I don't know what made me like that. We won't go all to pieces," she said. "We won't fight. It'll all be different, now we're married. It'll all be lovely. Reach me down my hat, will you, sweetheart? It's time I was putting it on. Thanks. Ah, I'm so sorry you don't like it."

"I do so like it!" he said.

"You said you didn't," she said. "You said you thought it was perfectly terrible."

"I never said any such thing," he said. "You're crazy."

"All right, I may be crazy," she said. "Thank you very much. But that's what you said. Not that it matters-it's just a little thing. But it makes you feel pretty funny to think you've gone and married somebody that says you have perfectly terrible taste in hats. And then goes and says you're crazy, beside."

"Honey," he said. "Stop it, will you? What do you want to start all this for? I love the damned hat. I mean, I love your hat. I love anything you wear. What more do you want me to say?"

"Well, I don't want you to say it like that," she said.

“Ah, baby. Baby lamb,” he said. "For heaven's sakes. Look at us-we're on our honeymoon. Here we are married! Here we are!"

"Yes, here we are," she said. "Aren't we?"
```

---

## IC-2042: He’s Just Not That into You

- Title: He’s Just Not That into You
- Author (byline): Greg Behrendt and Liz Tuccillo
- Work: Not specified
- Publisher: Simon Spotlight Entertainment
- Publication date as stated: Sept 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1322
- Already set (do not supply): none

### Source block (context only)

```text
Author: Greg Behrendt and Liz Ruccillo
ISBN: 978-0689874741
Publisher: Simon Spotlight Entertainment
Date (Month/Year): Sept 2004
```

### Introduction (context only: never use it for content warnings)

```text
For ages women have come together to analyze the puzzling behavior of men. “He’s afraid to get hurt again.” “Maybe he’s intimidated by me.” “He just got out of a relationship.” But no matter how many excuses for a dead-end relationship you try to make, the truth may be . . . He’s Just Not That into You by Greg Behrendt and Liz Tuccillo.
```

### Performance text (classify this)

```text
(Pg 7) Hey. I know the guy you’re dating. Yeah, I do. He’s that guy that’s so tired from work, so stressed about the project he’s working on. He’s just been through an awful breakup. He has trust issues. Right now he has to focus on his career. He can’t get involved with anyone until he knows what his life is about. As soon as it all calms down he’ll leave his wife, girlfriend, crappy job. God, he’s so complicated.

He is a man made up entirely of your excuses. And the minute you stop making excuses for him, he will completely disappear from your life.

(Pg 23) He’s just not that into you if he’s not calling you – Men know how to use the phone.

Oh, sure, they say they’re busy. They say that they didn’t have even a moment in their insanely busy day to pick up the phone. Bulls***. With the advent of cell phone and speed dialing, it is almost impossible not to call you. Sometimes I call people from my pants pocket when I don’t even mean to.

(Pg 26-28) Dear Greg: I’m dating this guy who ends conversations saying he’ll call me. Like, “I’ll give you a call tomorrow.” And then he doesn’t. Should I read something into this? - Annie

Dear Call Waiting: Yes, you should read something into it. In fact the very something is . . “He’s just not that into you.” Most guys will say what they think you want to hear rather than nothing at all. Some guys are lying; some guys really mean it. Here’s how you can tell the difference: You know they mean it when they actually do what they said they were going to do. You should be dating a man who’s at least as good as his word.

(Pg 29-30) Dear Greg: A guy who I’m going out with is totally important and totally busy. Sometimes when he’s working, I don’t hear from him for days and days. Some guys are just really, really busy! - Nikki

Dear Nikki: Really busy is another way to say “just not that into you.” Totally important is another way to say, ”you’re unimportant.” Too busy and important to ask you out or call you – what a catch. You must be the envy of every women he’s really dating.

I’m about to make a wild, extreme, and severe relationship rule: The word “busy” is a load of crap and is most often used by a**holes. The word “busy” is the relationship Weapon of Mass Destruction. Men are never too busy to get what they want.

(Pg 36) He’s just not that into you if he’s not dating you: Hanging out is not dating!

(Pg 39-40) Dear Greg: I’ve been dating a guy for six months. We see each other about every two weeks. I really like him, so I feel like it’s better than nothing.

And you never know things can change at any time. Maybe I should actually feel honored that he’s able to give me as much time as he does – He might actually really like me. – Lydia

Dear Better than Nothing: Really? Is better than nothing what we’re going for now? Have you lost your marbles? Why should you feel honored for getting scraps of his time. In my book, any guy who can wait two weeks to see you is just not that into you. (Pg 45) Better than nothing is not good enough!

(PG 59) He’s just not that into you if he cheats on you – There’s never going to be a good excuse for cheating.

Some will argue that you shouldn’t throw away a meaningful relationship just because of one indiscretion. And in case he tells you that it just “happened,” please remember, cheating doesn’t just “happen.” It’s not an accident as in, “Oops, I just slipped and fell.” He is not only behaving like a man who’s just not that into you, he’s behaving like a man who doesn’t even like you all that much.

(Pg 61-62) Dear Greg: I had been dating a guy for about two years, and I thought things were going really well. After he came home from a family visit, he told me [cheated on me] He told me I had put on some weight and therefore he wasn’t that attracted to me anymore. I have put on about 20 pounds. Should I break up with him or start going to the gym? -- Beth

Dear Twenty Pounds: I definitely think you should lose 175 pounds – in the form of your loser boyfriend. He just cheated on you and called you fat. Using your weight as an excuse for his cheating is not only mean, but simply not valid. And by the way, how’s he going to react if you grow older and get a few wrinkles? Or wear a color he doesn’t like?

(Pg 63) NOTE: Pronouns changed from plural to singular. This last guy is good. He’s betrayed his relationship and humiliated his girlfriend. Then he tells her it’s all her fault, knowing that he has just done something that has so demoralized her that she will be inclined to believe a load of horse crap. Don’t let any man blame you for their infidelity. Ever! (PG 68) There is no excuse for cheating. Let me say it again. There is no excuse for cheating.

(Pg 93) He’s just not that into you if he’s breaking up with you.

(Pg 98-99) Dear Greg: I have a boyfriend who keeps breaking up with me. He also keeps calling me and begging me to get back together. He’s done this three times now, every six months. I hate it, but I keep taking him back because I love him. He must be really into me if he keeps coming back, right? -- Christina

Dear Yo-Yo Champion: I’ll put money down that the breakup count isn’t over yet. Sadly, this is what that guy is doing during your relationship recess. He’s [looking] around for something better, and when he doesn’t find it, he gets lonely and comes “home. Reset your breakup maximum to one and move one.

Just remember that the person you are getting back together with is the same person who, not long before, looked you in your beautiful face, took full stock of you and all your qualities, and told you that he was no longer in need of your company. If aliens haven’t recently abducted your beloved and switched his brain for the brain of a guy who’s really into you, please consider the option that the bum maybe just got a little lonely.

(Pg 130) He’s just not that into you if he’s a selfish jerk

(Pg 134) Dear Greg: I am dating a guy in medical school. He’s overworked, over tired and gets angry easily. He recently screamed at me because I was bothering him when he was in the middle of studying. I know that this is just temporary. And every once in a while he’ll feel bad and apologize and tell me how much pressure he’s under. He wasn’t like this in the beginning and I know the real guy is going to come back. Besides, I always wanted to marry a doctor! -- Denise

Dear Old Yeller: I don’t care if he’s studying to become the next Messiah. There is no reason to yell at anyone ever, unless you are screaming “LOOK OUT FOR THAT BUS!” And it’s not temporary. People who yell are people who think they’re entitled to yell. Don’t wait around for Mr. Hyde to turn back into Dr. Jekyll.

(PG 145) You want to believe that you are better than all the crap you’ve been taking from all these men all these years? Well you are. (Front cover) You’re a beautiful, smart, funny woman who deserves better. (Pg 148) Life is hard enough as it is without choosing someone difficult to share it with. (Front cover) So . . . The next time you feel the need to start “figuring him out” consider the glorious thought that maybe He’s just not that into you and then go find the one who is.
```

---

## IC-2043: Hobo Matters

- Title: Hobo Matters
- Author (byline): John Hodgman
- Work: The Areas of My Expertise
- Publisher: Dutton Adult
- Publication date as stated: Oct 2005
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1132
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Hodgman
Book: The Areas of My Expertise
ISBN: 978-0525949084
Publisher: Dutton Adult
Date (Month/Year): Oct 2005
```

### Introduction (context only: never use it for content warnings)

```text
Today, the word “hobo” tends to call up one of two caricatures deeply ingrained in our collective imagination: One is a sad sack with saggy pants, five-o’-clock shadow, and a bindle stick*, probably passed out in some alley with a bottle of whiskey—an image that’s interchangeable with that of a bum.

The other is a fantasy about living free on the fringes of society: jumping boxcars despite the danger, wandering from town to town with no roots or commitments, sleeping under the stars with fellow hoboes who trade banjo tunes and wild stories.

This selection Hobo Matters by John Hodgman from his book The Areas of My Expertise is a satirical (whispers – not completely factual) look at American hoboes.
```

### Performance text (classify this)

```text
(Pg 98 – 101) (to be narrated in a serious, mocumentary voice) They called it the War to End All Wars. They called it the London Fire and the Trail of Tears. But they were all wrong. It was called the Great Depression, and the hoboes saw it coming.

1929, October. Black Thursday. The 24th day of October, 1929: the day the stock market crashed, instantly wiping out $30 billion in stock value. Soon after, the Bank of the United States would collapse, trapping all inside, many of them orphans. From his hover yacht in the Caspian Sea, President Hoover reassured the panicked nation that only foreigners and the mentally feeble would suffer. But the damage was too great. After a decade of high-flying prosperity, the United States' economy fell to earth and began tunneling to an awful volcanic core of despair, food riots, cloying folk songs, and lava, By March, 250,000 apple sellers would crowd the streets of Manhattan, desperately refusing to sell any other kind of fruit. But apples and sellers alike were easy picking . . . for the hoboes.

There had been hoboes in the United States since there had been trains and liquor, which is to say: always. But by 1930, an estimated two million broken souls had taken to the wandering life, hopping boxcars, picking up work where they could find it, and drinking, drinking, drinking. When prohibition reigned, the hoboes knew of secret stills and hidden lakes of moonshine. It made them strong and willful, and it made them blind and disfigured, and it spurred them to sing strange guttural songs in croaking voices that haunted the American night.

In many ways, they were a nation unto themselves. They had their own currency in the form of "hobo nickels" - the ordinary buffalo nickels onto which they would intricately carve new words and images, changing the Indian head to a picture of a hobo or changing the buffalo into a large hairy man wearing a cloak and fake horns. Another common craft was lint-knitting, using scraps of wool fuzz from pilled sweaters to make new sweaters, which they would then attempt to sell door to door. They had their own flag, which was identical to the flag of Barbados (this was either a coincidence or a deliberate effort to confuse).

And they devised a secret language of signs and scrawls used to alert their passing brethren to danger or opportunity. A crucifix chalked on the side of a house meant that religious talk would get you a free meal inside. A picture of a cat meant "a kind woman lives here." But intersecting circles warned that the local sheriff carried throwing stars, while twin Ws meant a mean dog slept in the yard and would rise on two legs and whisper secrets if you slept in the bushes. On some alley walls in whistle-stop towns you might find a cryptic translation of the complete text of Tristram Shandy, as that was the hobo's favorite novel. And a picture of an H with sunrays around it meant that the hour had come . . . it was time to overthrow the government of the United States."

When in the spring of 1932 great masses of unemployed veterans descended upon Washington to urge the passing of the Bonus Bill, hoboes came with them. Under the leadership of Joey Stink-Eye Smiles, they infiltrated the White House, pocketing sandwiches and replacing Secretary of the Treasury Ogden Mills with one of their own, Hobo Joe Junkpan. And across the country they began a coor-dinated reign of terror: soiling featherbeds, salting the cornfields, and dancing manic, heavy-footed jigs on parlor floors while ordinary citizens looked on in horror. In Kansas City, a hobo declared himself Duke of All the West and began demanding tithes. They wanted cheap beer and warm hats. They wanted bent nails and pieces of string. They demanded half barrels of swallowfeather sauce, and no one knew what they were talking about.

At his inauguration in 1933, a new crippled president named Roosevelt addressed the nervous crowd: "The people of the United States have not failed. In their need, they have registered a mandate that they want direct, vigorous action. And so I will kill all the hoboes, and together we will gnaw on their bones." It was time for a comprehensive Hobo Eradication Plan called "The New Deal."

The president acted swiftly. He established the Civilian Conservation and Hobo Fighting Corps. He took the country off the gold standard, denying the hoboes the use of their precious teeth. The Works Progress Administration was created largely as a cover for Walker Evans, photographer by day, hobo hunter by night. He had only one target: .Joey Stink- Eye Smiles. But Smiles was slippery, twice eluding the photographer's poisoned darts before disappearing into a ditch or a shrub. Now it was war. The hoboes retaliated by sneaking up behind the White House and whistling very loudly. They wrote confusing, illiterate editorials. And they summoned giant dust storms that stalked the land, eroding topsoil and swallowing small towns whole.

Finally the president knew there was only one way to end the hoboes' march across the blighted land: polio. Alone in his secret White House lab, Roosevelt created a concentrated serum of the dreaded disease that would be placed in the nation's water supply by the Tennessee Valley Authority. According to his contemporaries, Roosevelt was tortured by this decision. He knew that a certain number of non-hobo citizens would spend the rest of their lives in iron lungs as a result of his actions, but it would finally put a stop to the wandering people-starting at their feet and ending at their waists.

But then came Pearl Harbor. Some say Roosevelt knew the Japanese would attack that infamous December 7th. The truth is, he didn't. But the hoboes did. And as the tragic war that followed put a final end to the Great Depression, so too did it put an end to the hobo war. As quickly as they had come, the hoboes mysteriously disappeared. No one knows where they went, or why. Some say they found patriotism in their hearts, joining the war against a common enemy. Others say they went to the stars or to another dimension. And still others say they live on today, moving quietly from town to town, preparing for the time when their great chicken-bone and moonshine empire will rise again. Is it possible? No, because historians agree that they almost certainly went to the stars.

But if you live near a railway track and listen as the train passes, it is almost as if you can still hear them singing . . . .

Go to sleep you weary hobo

Let the towns drift slowly by

Listen to the steel rails hummin'

That's the hobo's lullaby*

. . . the dark and lonely wind of history still blowing from their rotted lungs.
```

---

## IC-2044: Hooway for Wodney Wat

- Title: Hooway for Wodney Wat
- Author (byline): Helen Lester
- Work: Not specified
- Publisher: Houghton Mifflin Company
- Publication date as stated: May 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 782
- Already set (do not supply): none

### Source block (context only)

```text
Author: Helen Lester
ISBN: 978-0618216123
Publisher: Houghton Mifflin Company
Date (Month/Year): May 2002
```

### Introduction (context only: never use it for content warnings)

```text
Do kids have to "fit in" by dressing, acting and thinking like everyone else. Let’s hear a resounding NO! Hooway for Wodney Wat by Helen Lester explores the fear we all have about being different and encourages us to embrace our differences as advantages. Or as Rodney Rat would say “embwace or diffewences”. Hooway for Wodeny Wat by Helen Letser.
```

### Performance text (classify this)

```text
Poor Wodney.

Wodney Wat.

His real name was Rodney Rat, but he couldn’t pronounce his r’s. To make matters worse, he was a rodent. A wodent.

“What’s your name, Wodney?” asked the other rodents.

“Wodney Wat,” whispered Wodney.

“What’s another name for bunny?” they asked knowingly.

“ Wabbit,” he mumbled.

“And how does a train travel?” They winked at each other.

“A twain twavels on twain twacks,” WOdney replied miserably.

All of this teasing day in and day out made Wodney the shyest rodent in his elementary school. His squeak could barely be heard in class. He gnawed lunch alone. And while the other rodents scurried and scooted about at recess, Wodney hid inside his jacket.

Then one day as the rodents were taking turns doing wheelies, a new rodent – a very large rodent – barged into the classroom and announced:

“My name is Camilla Capybara. I’m bigger than any of you. I’m meaner than any of you and I’m smarter than any of you.” Then she added, “So there.”

With that she accidentally-on-purpose elbowed an ear, bumped two noses, stepped on three tails, and lay down on a desk. Fur prickled in fear through the classroom. She sure was bigger than any of them. She sure looked meaner than any of them. Was she smarter than any of them?

“What’s 2 + 2?” asked Miss Fuzzleworth

“FOUR!” shouted Camilla Capybara without even bothering to raise her paw. “And furthermore, 4+4 is 8, 8+8 is 6 and 243 + 125 is 368.”

Later, when Miss Fuzzleworth asked, “What’s the capital of . . . . “

Camilla interrupted, “New York, Albany, Population 295,594.”

And during science, in answer to the question, “What part of a plant is blow the ground?” Camilla Capybara danced on her desk and sang, “Root! Root! Rooty-toot-toot!”

“Yup!” thought all the other rodents. “She’s smarter than we are, too.” They felt very, very uncomfortable.

Every afternoon, just before the final recess, Miss Fuzzleworth drew a name from her hat to see who would be the leader for their favorite game, Simon Says. She scrunched her eyes closed and jiggled the hat.

Would it be Hairy Hamster? Minifeet Mouse? Grizzlefriz Guinea Pig? Could it be big, mean, smart Camilla Capybara? Miss Fuzzleworth’s paw reached in and pulled out the name of . . . Wodney Wat!

The bell rang, there was a wild scurry for the door, and Camilla Capybara was the first on the playground, having trampled the others in her path. To Wodney she looked especially scary. What would she do when she heard him speak? Breathe capybara breath in his face? Or tie him up in his own tail? Or even POUNCE on him?

The tiny, trembling leader of the game stood before the eager players, his head well inside his jacket, and squeaked.

“Wodney says weed the sign”

While the other rodents read, “P.S. 142 ELEMENTARY SCHOOL FOR RODENTS,” Camilla began pulling up weeks around the sign and wildly flinging them hither and yon till she was clear up to her teeth in dirt.

The other rodents began to smile.

“Wodney says wap your paws awound your head.”

He peeked a little peek out of his jacket and saw WHAP! WHAP! WHAPPITY SLAPPITY WHAP! Camilla was whapping her paws around her head so hard she became dizzy, gave herself a headache, and had to sit down. The other rodents couldn’t help giggling.

“Wodney says play Wing Awound the Wosey.”

Camilla put out her arms like wings and made an airplane noise, “Nnnnrrrr.” But where was the wosey? WHAT was a wosey?

By now Wodney’s voice was stronger and his head was entirely out of his jacket.

“Wake the leaves!”

Nobody moved.

“Wodney says wake the leaves.

While Hairy, Minifeet, and Grizzlefriz and the others busied themselves raking, Camilla Capybara grabbed one leaf. “Wake up!” she yelled

She snatched another, “Come on, you. Up, up, up!” And another, “Rise and shine!” And another, “BOO!”

By now all the other rodents were squealing with laughter. All but Camilla, who frowned. “Stupid leaves.

They won’t wake up!” And why was everyone laughing at her? Such bullies!

In a voice so strong he had to hold his own ears, Wodney called, “Wodney says go west!”

The rodents collapsed in a happy heap for a rest Go west.

Camilla Capybara, feeling very smart that she could tell directions by the sun, said, “All right. I shall go west.” And then she added, “So there.”

West she stomped. Forever. She was gone . . . And from that day on the pupils of PS 142 Elementary School for Rodents never teased Wodney again. He was their hero. “Hooway for Wodney Wat! they cried. Whoot! Whoot! Wooty-toot-toot!
```

---

## IC-2045: Horrible Harry in Room 2B

- Title: Horrible Harry in Room 2B
- Author (byline): Suzy Kline
- Work: Not specified
- Publisher: Puffin
- Publication date as stated: May 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1680
- Already set (do not supply): none

### Source block (context only)

```text
Author: Suzy Kline
ISBN: 978-0140385526
Publisher: Puffin
Date (Month/Year): May 1997
```

### Introduction (context only: never use it for content warnings)

```text
Remember, when you were in 2nd grade? Sitting in those uncomfortable desks that housed all your worldly-school possessions. The teacher poses a question to the class…and there was always that one kid… The kid you thought was about to dislocate his shoulder. The kid who was jumping out of his seat crying “Oh, Oh, Oh.” The kid who begged for the teacher to “Pick Me! Pick Me! I KNOW the answer.” Well that kid was nothing compared to Harry in Suzy Kline’s Horrible Harry in Room 2B.
```

### Performance text (classify this)

```text
Harry sits next to me in Room 2B. He looks like any other second grader except for one thing. Harry loves to do horrible things.

On the first day of school, Harry was out on the playground holding a shoebox. I asked him, "What's in there?"

"Something. Want to see a girl scream?"

Before I could say anything, Harry took off after Song Lee. When he trapped her by the tree, he opened up his box and dangled a garter snake in her face. Song Lee screamed! That's when I first saw Harry do something horrible this year.

********************

When it rains, we have recess indoors. Sometimes we play a game called "Seven Up." When it's Harry's turn to be up, everyone wonders, Will Harry tap me on the head? Harry presses his knuckles down hard on your skull. He calls them knuckle noogies. Nobody should give anybody a knuckle noogie. But Harry does.

Harry loves to do horrible things. The second week of school, Sidney called Harry a name. It was during science when we were reading about birds. "Harry's a canary!" Sidney whispered. And a lot of kids laughed.

"What's so funny?" the teacher asked.

"Nothing, Miss Mackle," Sidney replied.

Harry didn't think it was nothing. Harry planned to get revenge after school. And he did. At 3:05, Harry jumped Sidney, pinned him to the ground, and said, "Say I Love Girls twice."

"Never!" Sidney said, trying to get away.

"Yeah?"

"Yeah."

And that's when Harry started to tickle Sidney under the armpits until Sidney couldn't stand it any longer. "I LOVE GIRLS! I LOVE GIRLS!" Sidney shouted.

Song Lee, Ida, and Mary heard Sidney. So did a lot of the boys. Harry got his revenge all right. And it was horrible.

Sidney ran down the street screaming, "I'll get you back someday!"

*******************

When Miss Mackle wants the floor cleaned, she asks Harry to sweep. No one sweeps the floor like Harry. He picks up every piece of paper, every pencil stub, and every bit of clay. Once Harry even crawled under my desk to get a broken crayon! Nobody knows that Harry keeps some of that stuff. But I do. I sit right next to him and watch. Harry is making stub people!

Harry says his stub people are the scariest creatures in the world. He keeps them in a cigar box in his desk. Someday, when he has made twenty-four, Harry says, his stub people will invade our room.

"It won't be long," he whispered. "Soon, the stub people will bring doom to Room 2B."

When it was Song Lee's birthday, her mother brought in two trays of treats for the class. After we sang "Happy Birthday," Song Lee passed out the treats. Miss Mackle noticed there were three fortune cookies and one cupcake left. Miss Mackle put them on a plate with a card that said WE LOVE MRS. MICHAELSEN. Then she said, "Who would like to take these treats to our librarian?"

Everyone raised their hand except Song Lee. She's too shy. We kept raising our hands. Sidney made noises like, "Oooooo... Me! Me! Me!"

Miss Mackle picked Harry and me. She knows we're not afraid to go upstairs where the big kids are.

When we were walking up the stairs to the library, Harry asked me if I wanted to split the cupcake.

"That's for the librarian," I said.

"Mrs. Michaelsen just likes yogurt and carrots," Harry replied. "We'll be doing her a favor."

And so we both promised, "Cross my heart, hope to die, stick a needle in my eye," that we would never tell on each another. Then we ate the librarian's cupcake. Sometimes Harry gets me to do horrible things.

************************

The day before Columbus Day, Harry came to school with a tattoo on his arm. It was a skull and crossbones. Harry said the sea pirate Long John Silver made his tattoo.

I know Harry did it with a Magic Marker. I think he just wanted to show off in front of Song Lee.

When Harry went to his seat, he took out his writing folder. He wrote two pages about his adventures at sea. Miss Mackle asked him to read his story to the class. Harry said he met a mermaid, ate a sea turtle, and dug up a treasure. Miss Mackle put Harry's story up on the bulletin board. She said Harry has lots of ideas.

Harry has never eaten a sea turtle. Harry has never seen a mermaid. Harry has never been to sea! And I know Harry can't even spell "sea." He's horrible at spelling too.

Harry is not like any other second grader in our room. I know all about him. Harry's my best friend.

************************

The day before Halloween, Harry planned his invasion.

"It's time to bring doom to our room," he said. I knew what he was talking about. It was time for the invasion of his stub people.

"Do you need help?" I asked.

"You can be my assistant."

We put the first pair of stub people in Song Lee's desk while she was up at the pencil sharpener. When she returned, she reached in her desk for a piece of paper.

Harry plugged his ears. "I love it when girls scream," he said. "Look out for doom!" I plugged my ears. Song Lee didn't scream. She didn't even jump out of her seat. Harry and I watched Song Lee play with the stub people. She made them dance on the top of her desk!

Harry scowled. "This is an invasion," he complained. "My stub people aren't dancers. They are invaders! They bring doom to our room!" I nodded.

Harry leaned over and whispered. “Next time, we have to catch the enemy by real surprise."

When Harry and I got permission to go to the bathroom, we stopped in the hallway. We slipped some stub people in Sidney's sweater sleeves. Perfect, we thought. When it came time to line up for lunch, Harry and I waited. Slowly, Sidney put on his sweater. And we watched. Sidney would jump up and scream any minute now!

But when Sidney put his arm in the sleeve, the stub people fell through and landed on the floor. Sidney never saw them. Neither did Ida or Mary. They stepped on them!

Harry kneeled down and scraped the stub people off the floor. Gently, he wrapped them in his handkerchief. We buried them in the garbage during lunch recess. And we gave them a farewell salute.

"This means war!" Harry exclaimed. "We've lost too many men. We have to invade the mainland now."

"What's the mainland?" I asked. "You'll see," Harry said.

Just before the bell rang, Harry put two pairs of stub people on the teacher's desk.

"The teacher's desk?" I said.

"The teacher's desk," Harry repeated. "Prepare for doom in our room!" Then he sat up straight and folded his hands on his desk.

When the bell rang, Miss Mackle walked in. "I can see Harry is ready for class," she said.

"Plug your ears," Harry whispered as Miss MackIe walked to her desk. "She's going to scream and jump right out the window."

"What's this?" Miss Mackle said when she saw the stub people. Harry took his fingers out of his ears. I did too. "How cute!" Miss Mackle exclaimed as she held one up.

"Cute?" Harry said.

"Cute?" I said. Harry and I gave each other a look. How could that be? The stub people are the scariest creatures on earth. Harry put his head down on his desk, and buried his face in his arms. Sometimes it's real hard for Harry to be horrible.

"Cheer up," I said "tomorrow's Halloween. That's your favorite holiday. You'll be real scary then."

Harry looked up. "Halloween ... " He grinned. Nobody knew what Harry was going to be for Halloween, but everybody knew it would be something horrible.

Just before the 3 o'clock bell rang, we talked about it.

"Are you going to be Frankenstein?" Ida asked Harry.

Harry flashed his white teeth. "Scarier than that."

"Are you going to be a skeleton?" Mary said.

Harry shook his head. "Much, much scarier than that."

"Are you going to be a vampire?" Song Lee asked.

Harry shook his head again, "You'll never guess."

Sidney said, "Oh yes, I will. I bet you're going to be a canary!" And he laughed and laughed.

"Just beware, Sidney. Halloween is tomorrow." Then Harry leaned forward and shouted, "BOO!" Sidney jumped a foot in the air.

The next morning in school, everyone watched the door and waited for Harry. When a huge witch came in, everyone shivered. "It's Harry!" they shouted. And then the witch took off her green mask.

Good morning, boys and girls," a voice said. It was Miss Mackle!

After we said the pledge, I looked over at Harry's seat. It was empty. Where was Harry? And then, at 9:05, a very big Count Dracula showed up at the door. Everyone really shivered! "It's Harry!" they shouted.

And then a voice said, "Happy Halloween, boys and girls." It was the principal, Mr. Cardini.

Then, at 9:10, something slithered into the room. It was long and striped. It had a thin red tongue.

"Aaaauuugh!" screamed Sidney. Miss Mackle walked over to look.

"And who are you?" she asked. The snake slithered across the classroom floor, and everyone screamed! The snake went "Sssssss ... " Miss Mackle started to tap her foot. "If it's who I think it is, you're ten minutes late for school."

Everyone leaned forward to see. A head popped out of the snake skin, and flashed his white teeth.

"Harry!" everyone shouted.

"You're late," Miss Mackle said. "Snakes don't move that quickly,"

Harry replied. "It took me a long time to slither across the playground."

“Well, you'll have to make up the extra time after school," Miss Mackle said. "Ten minutes."

Harry made a face. Sidney beamed. "My watch says nine-twelve." Harry glared at Sidney.

[See . . . ] sometimes Harry is so horrible he has to stay after school.
```

---

## IC-2046: How Could You?

- Title: How Could You?
- Author (byline): Jim Willis
- Work: Pieces of My Heart: Writings Inspired by Animals and Nature
- Publisher: Infinity Publishing.com
- Publication date as stated: Oct 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1064
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jim Willis
Book: Pieces of My Heart: Writings Inspired by Animals
and Nature
ISBN: 978-0741410153
Publisher: Infinity Publishing.com
Date (Month/Year): Oct 2002
```

### Introduction (context only: never use it for content warnings)

```text
If you've ever had to put a beloved pet to sleep, then you know how heartbreaking it can be to lose a member of your family. But in many cases, unwanted pets are callously surrendered to animal shelters. According to the ASPCA, approximately 3.3million dogs enter U.S. animal shelters nationwide every year. And each year, over 670,000 dogs are euthanized – that’s another word for executed.

Animals deserve love and care; and I beg you, if you find you no longer can or want to have a pet, finding another home for your animal is your responsibility. Don’t leave them frightened and alone at a ‘kill’ shelter with their soft eyes begging . . .

How Could You? by Jim Willis
```

### Performance text (classify this)

```text
When I was a puppy, I entertained you with my antics and made you laugh. You called me your child and despite a number of chewed shoes and a couple of murdered throw pillows, I became your best friend. Whenever I was “bad,” you’d shake your finger at me and ask, “How could you?” – but then you’d relent and roll me over for a bellyrub.

My housetraining took a little longer than expected, because you were terribly busy, but we worked on that together. I remember those nights of nuzzling you in bed, listening to your confidences and secret dreams, and I believed that life could not be any more perfect. We went for long walks and runs in the park, car rides, stops for ice cream (I only got the cone because “ice cream is bad for dogs,” you said), and I took long naps in the sun waiting for you to come home at the end of the day.

Gradually, you began spending more time at work and on your career, and more time searching for a human mate. I waited for you patiently, comforted you through heartbreaks and disappointments, never chided you about bad decisions, and romped with glee at your homecomings, and when you fell in love.

She, now your wife, is not a “dog person” – still I welcomed her into our home, tried to show her affection, and obeyed her. I was happy because you were happy. Then the human babies came along and I shared your excitement. I was fascinated by their pinkness, how they smelled, and I wanted to mother them, too. Only she and you worried that I might hurt them, and I spent most of my time banished to another room, or to a dog crate. Oh, how I wanted to love them, but I became a “prisoner of love.”

As they began to grow, I became their friend. They clung to my fur and pulled themselves up on wobbly legs, poked fingers in my eyes, investigated my ears and gave me kisses on my nose. I loved everything about them and their touch – because your touch was now so infrequent – and I would have defended them with my life if need be.

I would sneak into their beds and listen to their worries and secret dreams. Together we waited for the sound of your car in the driveway. There had been a time, when others asked you if you had a dog, that you produced a photo of me from your wallet and told them stories about me. These past few years, you just answered “yes” and changed the subject. I had gone from being “your dog” to “just a dog,” and you resented every expenditure on my behalf.

Now you have a new career opportunity in another city, and you and they will be moving to an apartment that does not allow pets. You’ve made the right decision for your “family,” but there was a time when I was your only family.

I was excited about the car ride until we arrived at the animal shelter. It smelled of dogs and cats, of fear, of hopelessness. You filled out the paperwork and said “I know you will find a good home for her.” They shrugged and gave you a pained look. They understand the realities facing a middle-aged dog or cat, even one with “papers.” You had to pry your son’s fingers loose from my collar as he screamed “No, Daddy! Please don’t let them take my dog!” And I worried for him, and what lessons you had just taught him about friendship and loyalty, about love and responsibility, and about respect for all life. You gave me a goodbye pat on the head, avoided my eyes, and politely refused to take my collar and leash with you. You had a deadline to meet and now I have one, too.

After you left, the two nice ladies said you probably knew about your upcoming move months ago and made no attempt to find me another good home. They shook their heads and asked, “How could you?”

They are as attentive to us here in the shelter as their busy schedules allow. They feed us, of course, but I lost my appetite days ago. At first, whenever anyone passed my pen, I rushed to the front, hoping it was you – that you had changed your mind – that this was all a bad dream . . . or I hoped it would at least be someone who cared, anyone who might save me. When I realized I could not compete with the frolicking for attention of happy puppies, oblivious to their own fate, I retreated to a far corner and waited.

I heard her footsteps as she came for me at the end of the day and I padded along the aisle after her to a separate room. A blissfully quiet room. She placed me on the table, rubbed my ears and told me not to worry. My heart pounded in anticipation of what was to come, but there was also a sense of relief. The prisoner of love had run out of days. As is my nature, I was more concerned about her. The burden which she bears weighs heavily on her and I know that, the same way I knew your every mood.

She gently placed a tourniquet around my foreleg as a tear ran down her cheek. I licked her hand in the same way I used to comfort you so many years ago. She expertly slid the hypodermic needle into my vein. As I felt the sting and the cool liquid coursing through my body, I lay down sleepily, looked into her kind eyes and murmured “How could you?”

Perhaps because she understood my dogspeak, she said “I’m so sorry.” She hugged me and hurriedly explained it was her job to make sure I went to a better place, where I wouldn’t be ignored or abused or abandoned, or have to fend for myself – a place of love and light so very different from this earthly place. With my last bit of energy, I tried to convey to her with a thump of my tail that my “How could you?” was not meant for her. It was you, My Beloved Master, I was thinking of. I will think of you and wait for you forever.

May everyone in your life continue to show you so much loyalty.
```

---

## IC-2047: How I Trumped Rudolf Steiner and Overcame the Tribulations of Illiteracy, One Snickers Bar at a Time

- Title: How I Trumped Rudolf Steiner and Overcame the Tribulations of Illiteracy, One Snickers Bar at a Time
- Author (byline): Sufjan Stevens
- Work: The Best American Nonrequired Reading 2007 Introduction – pgs xi - xvii
- Publisher: Mariner Books
- Publication date as stated: Oct 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MRS. LUBBERS
- Teaser before the introduction: Yes
- Spoken words (computed): 1292
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sufjan Stevens
Book: The Best American Nonrequired Reading 2007
Introduction – pgs xi - xvii
ISBN: 978-0618902811
Publisher: Mariner Books
Date (Month/Year): Oct 2007
```

### Introduction (context only: never use it for content warnings)

```text
Why??? Until 3rd grade I was a product of the Waldorf system of education created by Rudolf Steiner. (whisper) a progressive education.

How I trumped Rudolf Steiner and Overcame the Tribulations of Illiteracy, One Snickers Bar at a Time by Sufjan Stevens
```

### Performance text (classify this)

```text
There are some things you tell no one, secrets packed and folded away in the far reaches of your mind - admissions of athlete's foot, or a night spent in jail. These irreversible facts, like birth certificates and blood donor cards, we keep undercover . . . hidden in the closet, under the Ouija board and Christmas-tree stand. I'm a glutton for exhibitionism, so I'd like to reveal a dirty secret: I didn't learn to read until third grade.

Rudolf Steiner, an Austrian social theorist, developed an educational system that was holistic, noncompetitive, and emotionally balanced. There were no textbooks, only paint, clay, knitting needles, and sheep's wool. I don't recall a library or a science lab in our school. but the classrooms were decorated with satin drapes and paper lanterns. Every room was designed to imitate a tree house or a bear cave or an underground den.

Learning was measured by the students' creative whims -- beeswax one day, cotton string the next. There were no vocabulary exercises or math quizzes. The syllabus was hand drawn on the chalkboard. Sweeping rainbow illustrations of unicorns and magic owls and eavesdropping elves. The school did everything to blur all lines between fact and imagination, between art and science, between math and English, between student and teacher.

For some, the disregard for standards was galvanizing. My peers took up the violin, spoke French, mastered oil painting, weaving, and the classical guitar. But I was a slow learner, prone to daydreaming. I had trouble making friends, so I imagined them: Peter the ox, Dora the talking skeleton, Herb the dietician. I lived in a world of fantasy and make-believe where reading and writing were banned by laws of my own creation.

Years went by - preschool, kindergarten, first grade, second grade - the dreamy sweep of a Steiner childhood. I was shuffled from calligraphy class to recorder lessons. The choose-your-own-adventure of progressive schooling. It didn't matter that I was so far behind the other kids. I would catch up, the teachers said. I would come around someday. I would learn to read and write by the powers of the Maypole, the winter solstice, the constellations, and Orion's enchanted belt. For Waldorf teachers, the real process of learning was to be stewed and simmered in a slow cooker. We learned not by worksheets and chapter guides but by watching seedling trees grow from teacups, the passing of the seasons, Baroque music, folk songs, and Nordic mythology.

Truth be told, I wasn't learning anything. By the time I finished second grade, it was clear something was wrong. I still couldn't read or write. I had no friends. I had no ambitions. I was a Waldorf flunky. But by then it was too late. My parents' marriage began to crumble, They started watching daytime TV, ordered pizza, bleached their teeth, and shed their educational ideologies once and for all. Then they got divorced.

That summer, I went to live with my father, who had moved to a small logging town with a bait shop and a Methodist church; a quiet village where people spoke with a southern drawl and wore overalls and drove tractors to work at K-mart. My father apologized for everything - for Waldorf and recorder lessons. "It's time you became a man," he told me. "It's time you learned to read."

So I was transferred to a public school, a cinderblock prison camp with metal lockers and industrial carpeting and severe fluorescent lights. Computers, textbooks, worksheets, MEAP, SAT, PTA, all the formidable abbreviations of public schooling. I clawed at the classroom windows like a hamster in a glass cage, desperate for fresh air.

The other children - raised on hot dogs and homogenized milk - were pig-nosed, bucktoothed, bullies who spent their free time at the arcade downtown. But at least they could read. I couldn't even spell my own name, so I was beaten up at recess, punched behind the swings, left in a rumpled mess in the gravelly residue of the playground.

After the first week of school, I was forced to take a series of multiple-choice tests - reading comprehension, basic math, language arts - each of which I failed. That's when I was ordered to go to special ed. They sent me to a boxy trailer slumped behind the cafeteria with a stack of flash cards and a vocabulary book, highlighting useful, ordinary words that would help me navigate the everyday life of the working-class man. Apple pie. Toothpaste. Driver's license. Checkbook. Garbage can. I recognized the letters, but I couldn't piece them together into words. I was uninspired.

My English teacher, Mrs. Lubbers, pulled me aside and said, "What is wrong with you? Are you retarded?" At lunch, she unpacked her lunch on the table and made me identify each object: juice box, banana, salami sandwich, potato chips. Then she pointed out the obvious packaging. Everything was tagged with its name, in clear, concise advertising. She told me about the wonders of the industrial age, how every item of food is mass-produced and sold to the public with its nametag right on front: Hello. My name is _________. She called the grocery store a public library, a literary adventure, a reader's guide for the leaming-disabled.

MRS. LUBBERS: We are surrounded by words. It's impossible not to read in this day and age!

Mrs. Lubbers had devised a theory. Having been rescued from the liberal clutches of Rudolf Steiner, I was like a primate, a wild stallion or Frankenstein's monster. I only needed the brash brainwashing of civilization. A crash course in modem society, pop culture, Mickey Mouse, the Hardy Boys, Ronald McDonald. I needed the chlorinated conditioning of the modern world - television, GI Joe, Garfield and Cocoa Puffs. I wasn't dumb, she told me. I was just Old World, nineteenth century, under stimulated. The glorious product placement of the advertising age would certainly inspire me.

MRS. LUBBERS: Read the label and you will soon be channeling Garrison Keillor, Vincent Price, and Salman Rushdie.

The next day was payday, shopping day. I begged my father to take me to the local Super K, a commercial paradise, a library of information. When we got to the store, I kept my eyes open for the literature of the advertising world. Palmolive. Antibacterial. Tough on grease. Downy. Duracell. Aspirin. Scotch tape. These were mini-novels, rousing in me the desire to read. I started with a book of matches, inspecting the small print: Close cover before striking - a mysterious line of haiku. I sounded out the simple words on soup cans, toothpaste tubes, cracker boxes: Weight. Squeeze. Caution. Press. Warning. A simple glance at a box of Arm & Hammer baking soda beckoned the epic verse of warrior kings feuding with metal swords and battle-axes.

I perused the short story of the lip balm: "If irritation occurs, discontinue use." I marveled at the absence of verbs on the Vitamin C: one tablet, twice daily; and the captivating demands on the caps of bleach: push, turn, pull, pry.

Soon I was reading whole sentences, paragraphs, pages. I had triumphed over the educational armies of Rudolf Steiner and basked in the glories of commerce and capitalism, from which all knowledge thrives. I could finally read!

I took notes, made outlines, wrote ambitious dissertations on the flea circus, the Sharpie, Roe v. Wade, the hooded sweatshirt, Dance Camp, and how I heroically overcame the tribulations of illiteracy, one Snickers bar at a time.

I brought in a can of Campbell's tomato soup and read every word on the label, to prove it to the rest of the class: "In a four-quart pot combine one can of soup and one can of water. Simmer over low heat, stirring often. Serve. En-joy."
```

---

## IC-2048: How to Be a Villain

- Title: How to Be a Villain
- Author (byline): Neil Zawacki
- Work: Not specified
- Publisher: Chronicle Books
- Publication date as stated: April 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: STAGE 2, STAGE 3
- Teaser before the introduction: No
- Spoken words (computed): 1120
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Zawacki
ISBN: 978-0811846660
Publisher: Chronicle Books
Date (Month/Year): April 2003
```

### Introduction (context only: never use it for content warnings)

```text
Dracula. Hannibal. Frankenstein, the doctor or the monster, either applies -- Fictional villains are so famous all you need to hear are their names, and you know exactly who they are. Villains are some of the most memorable characters in fiction. But just how do these super villains get launched into infamy? It’s How to Be a Villain, a step-by-step guide by Neil Zawacki, that answers all the most urgent questions from choosing an evil name, to marketing your brand; finding the perfect evil hideout, to developing an evil masterplan. It’s cheaper than attending the annual bad guy conference and way more fun than being good. How to Be a Villain is guaranteed to elicit deep-throated evil laughs across the land! (evil laughter)
```

### Performance text (classify this)

```text
Step 1: Choosing an Evil Name (Pg 14-16)

To get your career launched with flair you’ll want a good evil name for yourself. One that is memorable, pithy and short. Choose carefully because this is what the world will know you as throughout time!

The Normal Name: Believe it or not, you don’t always need a big flash name. Trust in your evil deeds, and, should you become terrible enough, that alone can be enough to inspire fear in all humanity. . . [Updated from Bill Gates and Pat Robertson, you may insert your own real-life villains] Rudy Giuliani, OJ Simpson, Elon Musk.

[Or] The Descriptive Name: What makes you so bad? If you like to crush things, for example you might decide to call yourself The Pulverizer. Evil geniuses with multiple limbs might opt for The Octopus.

[Or perhaps a more] Sinister Name: Lord FireHammer; Duke IronSkull; Doctor WormBlight

Let your creativity blossom! Step 2: Evil Branding (Pg 17)

Make your new designation echo in the minds of the timid for eons with some sophisticated evil branding. You won’t need to consult Madison Avenue; chances are, you can come up with great ideas on your own. [You’ll need a] SLOGAN – Three to five words that sum up your evil ways in an intimidating fashion. Remember, you’re talking directly to your victims, so make your message something they can relate to, such as, “Mercy is Not an Option!” [add additional examples such as “You Can’t Handle the Truth!”

“You underestimate the power of the Dark Side!] [And don’t forget a] TRADEMARK GESTURE -- Whether you leave behind a token of your villainy or howl from a mountaintop each fortnight, consistent delivery of a gesture or symbolic act, in other words a trademark, will help reinforce your name and identity, making it that much more likely that your evil ways will survive in perpetuity. [Insert a variety of gestures, body stances, entrances/exits here; be creative] [Next] THE EVIL LAUGH – A Must-Have (Pg 23) There are a number of excellent ways to enhance your evil persona, from (in a heavy accent) feigning a foreign accent to (assume a physical tick) exaggerating a physical defect or tick. However, the most essential skill by far is an evil laugh. The evil laugh is a defining characteristic of any supervillain, and you will find yourself calling on it quite regularly as you exult in your own wickedness. Ha Ha Ha Hehe-he-he-he Muahahahaha Bwah-ha-ha-ha-ha!!!

HAHAHAHAHAHAHAHAHAHAHAHAHA Once you have decided upon a laugh, practice it every day. (laugh) Take a deep breath, relax, and feel yourself laugh like a crazed hyena. (laugh) Learn all its different chortles and inflections, exploring the many ways it can inspire fear.

(laugh) [And finally] FASHION FOR THE EVIL-DOER (Pg 122) The most agonizing decision of your evil career. What to wear? It may seem wrong, but many people will form ideas about how evil you are based on how you dress and carry yourself. 1. It’s hard to go wrong with classic black. Sinister, foreboding, fashionable yet fearsome, black creates an air of mystery. (trademark gesture) Classic black remains THE fashion statement for villains everywhere. 2. (Pg 125) [But] If you spent your childhood hiding in the backyard reading comic books, you probably won’t be happy with anything less than the supervillain costume with gimmicks. Be it a green jumpsuit with question marks or an outlandish clown suit that shoots confetti, the gimmicky costume will automatically provide a motif from which you can adopt a personal theme. As you design your costume, take your body type into consideration. Colorful leotards may be high on visual impact, but remember, spandex is a privilege, not a right! 3. (Pg 131) Evil masterminds who posses a magical inclination may want to invest their money in wizard’s robes. These sleek garments are ideal for sorcerers providing fashion sensibility and open-air comfort. And they look great with sandals or basic black supervillain boot-socks. You can find them in a wide range of colors, including black and red – avoid white [though] both because of the association with good and because you will look like you’re wearing a toga.

Step 3: [Don’t forget a] Location for Your Lair (Pg 88) Every evil mastermind needs a base of operations. Choose your lair carefully. If you have enemies, they will probably show up on your doorstep eventually, so you’ll want it to be an impressive edifice to your grandeur. Consider . . . 1. (Pg 90) An Underground Secret Headquarters of Doom. (trademark gesture) To the untrained eye the secret entrance looks like nothing more than an isolated shack in the middle of nowhere. But should you take the secret elevator hidden within, all is horribly revealed. An underground headquarters is a diabolical lair of which you can be proud. Popular for their low energy bills, privacy and “only a madman could live here” ambience, (laugh) a subterranean lair is an excellent choice indeed. 2. (Pg 92) The Fake Mountain with a hollow interior is another appealing site. On the outside it looks like any other mountain, but with the flip of a switch you can transform it into a deadly fortress of doom! (laugh) The only caveat with the fake mountain is that you should not place it in the middle of a city. For some reason, they are too often noticed there. 3. (Pg 93) Although considered gimmicky for years, the amusement park lair has seen a resurgence in popularity in recent times. The reason is simple: The décor can easily be transformed into a carnival of horrors, the fun houses laced with booby traps and the hall of mirrors at the end for confronting the heroes. The tunnel of love offers endless possibilities for becoming the tunnel of screams (scream turning into laughter) Fun for the whole family!

Step 4: [And Last but Not Least . . . You must have an Evil Plan] (Pg 140) Have you ever wanted to make a great evil plan, but didn’t have the time? You’re not alone. In fact, many evil men and women struggle with this culminating act. The secret to success is planning ahead. The Evil Plan Generator will help you! By identifying your goals, means and target for destruction, the EPG lets you concoct a truly nefarious scheme in a matter of minutes. Simply fill in the blanks! (See fill-in-the-blank options at the end of the selection) (Pg 156) STAGE 1: To begin, you must first (ACTION) (TARGET). This will cause the world to (REACTION), (DESCRIPTIVE VERB) by your arrival. Who is this (NAME)? Where did they come from? And why do they look so good in (FASHION)?

STAGE 2: Next, you must (ACTION) (MONUMENT). This will all be done from your (BASE), a mysterious place of unrivaled dark glory. Upon seeing this, the world will (REACTION), as countless hordes of (HENCHMEN) hasten to do your every bidding.

STAGE 3: Finally, you must (ACTION) your (WEAPON), bringing about (DESTINY). Your name shall become synonymous with (RANDOM), and no man will ever again dare (TRAGIC PAST). Everyone will bow before your (POWER), and the world will have no choice but to (END RESULT).
```

---

## IC-2049: How to Say It

- Title: How to Say It
- Author (byline): Beth Stillman
- Work: The Moth Presents Occasional Magic (Pg 77-80)
- Publisher: Crown/Archetype
- Publication date as stated: Mar 2019
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SPEAKER
- Teaser before the introduction: Yes
- Spoken words (computed): 1039
- Already set (do not supply): none

### Source block (context only)

```text
Author: Beth Stillman
Book: The Moth Presents Occasional Magic (Pg 77-80)
ISBN: 978-1101904428
Publisher: Crown/Archetype
Date (Month/Year): Mar 2019
```

### Introduction (context only: never use it for content warnings)

```text
Every patient death is a different situation; but for health care professionals, one thing is for certain: Telling someone their loved one has died is never easy.

How to Say It by Beth Stillman.
```

### Performance text (classify this)

```text
SPEAKER: (Pg 77-80) “I’m sorry. He's dead. We did everything we could." Is he breathing? Is he bleeding? Is his heart beating? “I’m sorry. He's dead. We did everything we could." He’s dead . . . he’s dead . . . he’s dead.

SPEAKER: I know what happens after you die. I take your family into a quiet room, with Kleenex, and then I say the word "dead." Not "expired" (because you are a person, not milk), and not "passed on," because families always want to believe that means I just transferred you to another hospital.

Dead.

I have to say it.

That's basically all they taught us about how to deliver bad news in medical school. A one-hour lecture.

So we learned by watching our teaching physicians.

We were their constant companions in this sort of theater of the bereaved, lurking in doorways and at bedsides and the hospital's ER, waiting to see how soft they made their voices. When did they touch someone on the shoulder? How much medical jargon did they use before getting to the word "dead"?

When you train to become a doctor, they don't really teach you about death. They teach you how to prevent it, how to fight it, how to say it, but not how to face it.

So on one of my first nights as a teaching physician in the emergency room, as we work on the body of a sixteen-year-old boy with eight bullet holes in his chest and abdomen, we are almost angry at his body for not responding to our efforts.

Is he breathing? Is he bleeding? Is his heart beating?

I go to the head of the bed, and I hook him up to a respirator that breathes for him.

We put tubes ... everywhere. A large-bore IV goes into each arm, an even larger one into his groin, and through that we start pressure-bagging type- 0-negative blood, trying to replace what he's lost. I call for another unit of blood, but no matter how fast we work, we can't work fast enough.

The monitor begins to sound this shrill insect whine meant to alert us that the patient is crashing, which we already know, so it feels less like a warning and more like a rebuke.

Then we lose his blood pressure and his pulse. But he's sixteen.

So I perform a trauma Hail Mary. I grab a ten-blade scalpel and make a deep incision from the nipple all the way down to the bed. I take the scissors and cut through the intercostal muscles. I take the rib spreaders, push them between the ribs, and crank his chest open.

There's a giant gush of blood and then a moment of stillness, like the second after a lightning strike. Even his blood smells metallic, like ozone.

I reach my hands into his chest, and I put them around his still heart. I begin pumping it for him, feeling for damage. I slide my fingers down the length of his aorta, but it is so riddled with holes that the frayed pieces disintegrate in my hands.

The first time I had to be the one to break that news to a family, I was in my second year of residency. I remember I had to do it in the patient's room, because his adult daughter refused to leave his bedside.

I said, “I’m sorry. He's dead. We did everything we could."

And then I was supposed to step out of the room, give her a few moments alone. But I was paralyzed, rooted to the spot by a sense of failure and loss. When I looked at the bed, I couldn't stop imagining my own father lying in it.

My attending physician must have seen what was going on in my face, because she grabbed me by the arm and she dragged me outside.

She said, "Don't you ever do that again. Don't you EVER pretend that grief belongs to you when it doesn't. One day the person you love will be in that bed. But today you say you're sorry, you mean it. Then you have to walk away."

I look up from the sixteen-year-old boy and see that my own audience has formed. They wait to see what I will do next.

I realize that in front of me is a gaping hole, and the boy's family will probably be here very soon, so I turn to the surgery resident, and I say, "Listen, you have to get this kid closed up as fast as you can."

Not ten minutes go by when we hear the sound of a woman demanding to be let in.

We are not ready.

We are shoving tubes and gauze and surgical supplies into giant trash bags. Security is trying to keep her out, but she is a tsunamic force. We barely had this boy closed up and half covered with a sheet when I see her standing in the doorway.

Clearly his mother. And she goes absolutely quiet. “I’m sorry. He's dead. We did everything we could."

She takes a running leap toward the body. The nurse at the head of the bed sees a large needle still attached to the sutures holding him together and plucks it off the table just before his mother lands on top of his body, trying to protect it with her own.

She starts keening. It's a terrible sound.

I repeat, “I’m sorry. He's dead. We did everything we could."

She slides off his body. I see her touch the boy's fingers to her mouth briefly before holding them against her cheek. I leave the room as soon as the social worker enters, motioning for everybody to follow me out.

I think, That's what they can learn from watching me: how to walk away. And without a moment's break, I go to see the next patient. Because there are forty people in the waiting room who all want im-mediate attention, and they can't know that I still feel the dead boy's heart in my hands like an anchor.

But I know that if I don't put it down now, I might never remember that this loss doesn't belong to me.

One day that grief will be mine. But not tonight.
```

---

## IC-2050: How to Survive a Horror Movie

- Title: How to Survive a Horror Movie
- Author (byline): Seth Grahame-Smith
- Work: Not specified
- Publisher: Quirk Productions
- Publication date as stated: May 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, C, R, A, V, E, AS A PARENT, AS A SKEPTICAL TEENAGER, AS A JOCK, AS A YOUNG GIRL, AS PATHCES, AS A CLULESS TEEN, AS A CLUELESS BABYSITTER, AS A DISGRUNTLED TEEN
- Teaser before the introduction: No
- Spoken words (computed): 1356
- Already set (do not supply): none

### Source block (context only)

```text
Author: Seth Grahame-Smith
ISBN: 978-1594741791
Publisher: Quirk Productions
Date (Month/Year): May 2007
```

### Introduction (context only: never use it for content warnings)

```text
Let’s face it, characters in horror films are pretty stupid. They make bad choices - leaving you to wonder if they have any brains at all. For example . . . They never turn on the lights . . . roaming around in the dark with a serial killer on the loose is a MUCH better option, right? They always go into the basement or wander alone in the woods. They taunt and encourage the killer to come after them in amazing shows of false bravado. “You want some of this – Come and get me you freak!” They hear a sound and HAVE to go investigate. They utter the phrase. “Let’s split up!” Of all the dumb things people in horror movies do – this is the dumbest! But . . . If you do find yourself trapped in a horror movie, worry not; today I’ll be presenting you with a comprehensive guide to keep you alive until the credits start rolling.

How to Survive a Horror Movie by Seth Grahame-Smith
```

### Performance text (classify this)

```text
(From Chapter 1)

NARRATOR: Those of us who’ve become trapped in a horror movie have a choice: We can either line up with the other cattle and march into the slaughterhouse (Moo!) Or we can fight back. Yes, it’s a long way to the final credits. No, the odds aren’t in our favor. But that’s no excuse to lie down and let the filmmakers have their way with us. (But you have to be smart!) Horror movie characters aren’t killed by machete-wielding monsters or reincarnated psychopaths— They’re killed by ignorance. Ignorance of the mortal danger they’re in. Ignorance of the fact that they’re in a horror movie. (So . . . ) How do you know if you’ve been sucked into the Terrorverse? Sometimes the signs are unmistakable. For instance, if you’re a teenaged babysitter caring for a mute toddler in a remote cabin during a blizzard while an escaped killer roams the woods, you’re probably in a horror movie. TAKE A LOOK AROUND. The environment should offer some clues. If you’re on a crowded city street in broad daylight, you’re probably safe (for now). But if you’re anywhere remote—the woods, an old house, an abandoned mental institution in the middle of a blackout— then yes, your chances of being in a horror movie are much higher. Do you hear strange sounds? (chi-chi-chi … ah-ah-ah) out of nowhere? Are you speaking Japanese? (utter phrases or words in Japanese – Typhoon, Karaoke, Anime, Emoji, Pokemon!) According to the laws of early twenty-first century cinema, anyone speaking Japanese is in a horror movie. If the answer to any of these questions is “Affirmative,” then we have to consider the possibility that you’ve become trapped in a horror movie. As much as you may feel like crying or making skid marks in your tighty-whiteys, you’d better pull yourself together— and soon. Because if you don’t, the boogeyman’s really going to give you something to cry about. Your situation requires immediate action, and the C.R.A.V.E. method (COVER, RECON, ARSENAL, VEHICLE, ESCAPE) was developed for just such an emergency. It’s a kind of “stop, drop, and roll” for horror movie victims—a way to stay alive long enough to summon your courage and get out of immediate danger

C: COVER. What you need right now is a temporary headquarters—a place to wipe the sweat from your brow, take a pull off the old asthma inhaler, and formulate your plan. Some of the best places to do that: Good ol’ everyday houses. Though not ideal fortresses, the average two-story house is almost always the closest option. [Or] Water towers. If your movie takes place in a small Midwestern town, this might very well be the tallest structure around. If you can get to the top, you’ll have a highly defensible (there’s only that one long ladder to worry about) perch with a 360-degree bird’s-eye view.

R: RECON. Now that you’ve had a moment to catch your breath, it’s time to get an idea of where the enemy is and what he’s up to. If you don’t have the height of a water tower working for you, peek through the highest window in your hideout and take a look. If you see nothing, they’re probably right behind you. (begins to turn with a stricken look) No, wait! Don’t turn around; Nice and cool … that’s it. Now, on the count of three, cover your face with your arms and jump over the rail or through the window. (shows a fear of heights/jumping) Either you jump or you die. Ready? One … two … just kidding, you’re totally screwed . . . .

A: ARSENAL. You see a path to freedom—you’ll need some kind of weapon. If you’re barricaded in a house, look for a baseball bat, kitchen knife, or anything that kids aren’t allowed to play with indoors. If you’re holed up in a church, grab a heavy-duty candlestick. And if you’re up on that water tower, get your hands on the nearest, um … actually, there aren’t too many options with a water tower. You really should’ve thought of that before you climbed up there!

V: VEHICLE. You’ve summoned some courage, grabbed a weapon, and hopefully spotted a nearby unoccupied vehicle—now it’s time to kick a little ass. In a burst of adrenaline-fueled speed. Your goal—your only goal—is to reach the nearest car or truck, get inside, and blow town as fast as inhumanly possible. Don’t bother smashing the window—they left the car unlocked (provide sound effects and pantomimes) Lock the doors, and pull down the driver’s-side sun visor. The keys will simply drop into your lap. When you try to start the engine, it’ll turn over again and again, but don’t worry—it’ll kick in as soon as the attacker reaches the car and pounds on the windows.

E: Escape. This is the easy part. Put the car in “D,” point the compass to “N,” and get the “F” out of there. [We’ve now come to that portion of this guide entitled] THE SEVEN DEADLY HORROR MOVIE SINS 1ST DEADLY SIN: DOUBT. There are two types of horror movie characters: those who believe your story and those who don’t.

AS A PARENT: “It was just a dream, honey.”

NARRATOR: No it wasn’t. Come on, people. Your son or daughter is having recurring dreams about getting brutally murdered night after night, and you’re brushing it aside as what—indigestion?

AS A SKEPTICAL TEENAGER: “Those are just ghost stories our parents told us.”

NARRATOR: Yes, and they just happen to be true. If all the moms and dads have spent the last 17 years telling you not to go into the abandoned mannequin factory, here’s an idea: Don’t go into the abandoned mannequin factory. 2ND DEADLY SIN: MACHISMO. [You’ll recognize] The jock who thinks his football skills are enough to defeat the reincarnated serial killer. Remember, [if you are a] male— in horror movies, testosterone might as well be cyanide.

AS A JOCK: “You want some of this?”

NARRATOR: You know the guy. The one who just can’t take it anymore.

AS A JOCK: “What’s your plan, huh? Sit and wait for that … that thing to pick us off one by one? No way, man! Not me.”

NARRATOR: He runs out into the open, yelling something like

AS A JOCK: “C’mon, show your face!”

NARRATOR: And . . . well, you know how that ends. 3RD DEADLY SIN: INDEPENDENCE. (In a Steve Erwin accent) Have you ever seen that documentary about wildebeests? The one where it’s nothing but slow-motion footage of them getting torn apart by lions and crocodiles? Great, isn’t it? Funny how the predators always seem to kill the animals that are on the outer edges of the herd. The ones who are either too slow or too stupid to draw strength from their numbers. This is not a coincidence. 4TH DEADLY SIN: UGLINESS. Nobody said horror movies were fair. 5TH DEADLY SIN: CURIOSITY. - one of the basic horror movie equations: Investigation = mutilation.

AS A YOUNG GIRL: “Is that you, Patches?”

AS PATHCES: If “Patches” is your nickname for the man hiding in your closet with razorblades on his fingertips, then yes, it is.

AS A CLULESS TEEN: “Do you think it’s dead?”

NARRATOR: No. Go ahead and poke it with a stick. We want to watch it grab your arm and bite half your face off. 6TH DEADLY SIN: IRRESPONSIBILITY. In a horror movie, if you accept a task and fail to carry it out, either you or someone close to you is going to die.

AS A CLULESS TEEN: “Aw, what’s a little nap gonna hurt?”

NARRATOR: A lot.

AS A CLUELESS BABYSITTER: “Trust me, the kids are sound asleep.”

NARRATOR: No, the kids are dead.

AS A DISGRUNTLED TEEN: “How come I always get the crappy jobs?”

NARRATOR: Because you’re an idiot, and you’re about to prove that fact by failing miserably at the simple task you were assigned. 7TH DEADLY SIN: VEHICULAR SEX. Do it and die.

(From the Epilogue)

NARRATOR: [So . . . ]When is it safe? When we see credits rolling in front of our eyes? Hear applause? When the killer suddenly takes off the mask, shakes our hand, and says, “Nice working with you”? No, it’s never safe. Once you’re in the Terrorverse, you’re in for good—even after the movie that brought you there has wrapped. You succeeded in vanquishing the enemy? Great. Chances are you made it to the final credits, and you’ll lead a long, peaceful life (especially if your movie bombs at the box office). But there will always be the possibility, however slight, that you’ll be called back for sequels. (Ask Jamie Lee Curtis!) Screenwriters will keep dreaming up new villains and killing methods. Directors will get sleeker and bloodier. And the enemy will keep its fangs and machetes razor sharp . . . You’d better keep your skills the same way.
```

---

## IC-2051: How to Trap a Zoid

- Title: How to Trap a Zoid
- Author (byline): Dave Barry
- Work: Dave Barry's Bad Habits
- Publisher: Owl Books
- Publication date as stated: Sept 1993
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 932
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Barry
Book: Dave Barry's Bad Habits
ISBN: 978-0805029642
Publisher: Owl Books
Date (Month/Year): Sept 1993
```

### Introduction (context only: never use it for content warnings)

```text
Welcome to the “I Hate Math Club” – It was especially formed to express my frustrations over math. Now don’t get me wrong . . . math can be very useful until you learn that f(x) does nothing for you. I understand that math is a part of everyday life. But, trust me, it gets ridiculous when you have to divide polynomials! “Will I be doing this in the future?” you ask yourself. Most likely . . . NO. The only jobs that may use the intense factoring of polynomials are mathematicians or God forbid the illustrious career of “teacher”. And anyone who would put themselves through that kind of torture should seriously reconsider. How to Trap a Zoid by Dave Barry.
```

### Performance text (classify this)

```text
We should all be grateful that we have mathematics. For example, without mathematics, it would be almost impossible to figure out what size tip you should leave. Even with mathematics, this is very difficult. The mathematical formula for tipping, which was discovered by Sir Isaac Newton, states that the tip equals 15 percent of the bill, but unfortunately the bill is always $17.43, and nobody has the vaguest idea what 15 percent of $17.43 is. The finest brains in the country have been working on this problem for years, using large computers, and they have yet to come up with an answer. So most of us wind up tipping a random amount of money, usually $3.50, which we increase slightly if the waiter performs an extra service, such as not spitting in the food. And that’s just one of the ways we use mathematics in our everyday lives.

Mathematics got started in ancient Egypt, when the ancient Egyptians discovered the numbers three and eight. They used these numbers to develop the mathematical formulas for the pyramids, which were actually supposed to be spherical. Eventually people in other countries discovered more numbers, and today we have more than ten thousand of them.

After the discovery of numbers, the next major stride in mathematics came when the ancient Greeks discovered the hypotenuse. The Greeks used the hypotenuse to manufacture right triangles for export to other countries. Included free with each triangle was a copy of the famous Pythagorean Theorem (named for its discoverer, Bob Theorem), which states: “Some of the squares of the opposite sides are equal to 14.6 percent of your grossly adjusted annual unearned interest, unless there are two or more runners on base at the time.” To this very day, children memorize the Pythagorean Theorem in school, which accounts for their behavior.

The ancient Greeks made so much money with the right triangle that they developed a whole line of mathematical items, such as the rhomboid, the pentagon, the diameter, the parabola, the hyperbole, the irrational number, the cube, the really deranged number, and the square root. In fact, the ancient Greeks developed all the really popular items; everything developed since then has failed miserably. Take algebra. I don’t know who dreamed up algebra, but whoever it was obviously had a lot of time to waste, because it is utterly useless. In algebra class, day after day, the teacher would write something like this on the blackboard:

4x + 2 = 14

Then he would ask us what x stood for. It turns out that it stood for 3, but how were we supposed to know that? He was the one who dreamed up x in the first place, and it seemed grossly unfair for him to expect us to know what he was thinking of at the time. And to make matters worse, the next day he would have x equal some other number, such as 4, depending on his mood. I spent an entire year in algebra class, and to this day I don’t have the faintest notion what x stands for, which is why I hardly ever use it for anything.

Calculus is even worse. When I went to college, all of us freshmen had to take a semester of calculus. It was like a fraternity initiation. The professor, who wore a bow tie and grew up on another planet, would start the class with a statement like this: “Let us consider the problem of a helix uncoiling in n dimensions.” He never told us why this was a problem, or why anybody would want to consider it even if it was. He would merely turn around and start filling the blackboard with alien symbols, and he would keep it up until it was time to leave. Every now and then he would give us a test, and I always got a zero. In fact, “zero” was the only mathematical concept I ever understood in calculus class.

I decided to quit calculus the day I stabbed myself in the head with Jeff White’s pencil. Jeff sat next to me in class, and to amuse ourselves while the professor was writing alien symbols on the blackboard we would play childish pranks on each other. One day Jeff tried to knock my books off my desk, so I grabbed them with one hand and, with the other hand, snatched Jeff’s pencil, which I attempted to break by smashing it against my head, only I didn’t get the angle right, so I ended up driving the point into my skull, where it broke off. This created quite a commotion, but the professor was deeply engrossed in the problem of a trapezoid rotating in y dimensions, and he didn’t even notice the problem of a student with a pencil point lodged in his skull. So Jeff and I just got up and walked over to the infirmary.

The nurse was very suspicious. She said: “Are you telling me that you stabbed yourself in the head with a pencil?” Then she looked very suspiciously at Jeff. Jeff said, defensively: “Really. He stabbed himself.” And the nurse said: “Why would anybody stab himself with a pencil?” And so I stared suspiciously at Jeff, and said: “Yeah, why would I stab myself with a pencil?”

Anyway, the nurse got the pencil point out of my skull, but I didn’t go back to calculus class ever again. Jeff dropped out of college a short while later, although I’m pretty sure this had nothing to do with the pencil incident. I suspect it had a lot more to do with calculus.
```

---

## IC-2052: How to Write Suspense

- Title: How to Write Suspense
- Author (byline): James Pinkerton
- Work: The Best American Non-Required Reading 2003, Pgs 258-262
- Publisher: Houghton Mifflin Harcourt
- Publication date as stated: Jan 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: PINKERTON, JANET, JOHN, NARRATOR
- Teaser before the introduction: No
- Spoken words (computed): 883
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Pinkerton
Book: The Best American Non-Required Reading 2003,
Pgs 258-262
ISBN: 978-0618246953
Publisher: Houghton Mifflin Harcourt
Date (Month/Year): Jan 2003
```

### Introduction (context only: never use it for content warnings)

```text
What editor ever said, “Jeez, this script or chapter is just too funny, can we fix that?” Okay, if you’re writing Handmaid’s Tale or a Hallmark movie, they might say that. But in comedy, when have you ever stopped hunting for additional ways to make a story funny?

You can’t just start forcing awkward jokes on characters or interrupt the plot to insert a string of one-liners, but a funny story needs to stay funny from beginning to end, right? So, here’s an idea (insert ominous music “DUM, DUM, DUM”) add suspense! Make the story bigger, scarier, add close calls, raise the stakes, get characters screaming and running, throw a dead body in there!

I see you are here today for James Pinkerton’s Master Class: How to Write Suspense. (make a cringy face, then recover) It will be worth every penny! You’ll learn how to inject blood-curdling hooks into every nook and cranny of your writing by someone who believes he/she is an expert! On to the first lesson!

How to Write Suspense by James Pinkerton
```

### Performance text (classify this)

```text
PINKERTON: (Pg 258-262) (in an over-the-top, Master Class fashion) Lesson 1, General Suspense Tips. The opening sentence is essential to a great suspense novel. It lets the reader know what the story's going to be about.

(expansively reading) “John crossed over to the living room and lit a cigarette.”

Note how I have successfully introduced a character, a location, AND an action. Now let's crank up the suspense! “John crossed over to the living room and lit a cigarette. (beat) Or did he?”

Doubt sets in. Our reader begins to question everything he or she has come to believe. Who is this John character? Can we really trust him? How can we really trust anybody? Chilling questions. Luckily, you don't have to answer them. Remember, great suspense lies in what you don't tell the reader.

Having placed the seed of doubt, we quickly move onto something else, distracting them. (Ah ha!) “John then went to work and nothing happened.”

This is a perfectly acceptable follow-up sentence, right? Wrong! This sentence isn't suspenseful at all. Let's try that follow-up sentence again: “John went to work.

(with great intonation and facial expression) His day was a roller-coaster ride of intrigue and mystery.”

Did you see what made the "right" sentence suspenseful and what made the "wrong" sentence utterly worthless? (Self-satisfied smirk)

Lesson 2: Writing The First Chapter -- [Listen to] the following opening paragraph and try to locate where the suspense is coming from: (with an obvious speech impediment, leaving out all the “R’s”)

“The gunman adjusted his gay hat as he powled the misty ooftops, knowing his pey would show soon. Sweat stuck to his shit as he contemplated what he must do. The one-eyed man who had killed his fathe would finally pay the pipe.”

(shivers with the thrill) An excellent opening to a great suspense novel! Where are all the R’s? Is it a typographical error? Does the writer simply not like R’s? Or are there mysterious deeds at play, and are the R’s somehow involved? All of these questions spiral through a reader's mind as they find themselves in the taut grip of (beat) suspense. In the next paragraph, we release this grip: (Lightning crash) “The one-eyed man had stolen all the R’s.”

Goosebumps, yes? Why? Because that was great suspense! Lightning is so suspenseful it's not even funny. Use it for everything! Lightning makes the reader notice whatever happened before the lightning. Remember, a suspense novel should start with a very suspenseful opening paragraph then release the suspense in the second. After this, (waving off the thought) you just write the rest of your book. The reader knows what kind of powerhouse suspense writing to expect, and your work is done.

Lesson 3: Writing Suspenseful Dialogue – [Listen to] the following dialogue. Watch for the “end parts” of the sentences. These are the parts where you’re going to fit most of the suspense in! (Pinkerton plays all characters with intense over-acting)

JANET: I never thought you’d be capable of murder, I’ve known you since the first grade. You’ve never harmed a fly.

JOHN: Maybe that’s true. Maybe it’s not true. Maybe I’ve harmed lots of flies. You don’t know me, Janet.

JANET: Or do I? I know you’re not capable of murder, John. Sure, maybe flies. I’ll give you that. But people? That’s stupid.

NARRATOR: Then Janet saw an enormous bloody knife on the table.

JANET: (reacts) Is this knife yours, John?

JOHN: No, I’m pretty sure it’s not mine.

JANET: Are you lying to me, John?

JOHN: No, probably not. (Lightning crashes)

PINKERTON: Egad! Is John a murderer? Possibly! That’s the thing – who knows? Good suspense dialogue should crackle off the page. Keep the reader on their toes by leaving out important details, locations, names, even events integral to the plot. Remember, the more the reader has to guess, the more powerful your writing becomes. (said with authority even though this is obviously wrong) Lesson 4: Ending Your Suspense Novel -- A good suspense novel must have a surprise ending to leave the reader completely dumbfounded. If you've done your job up to this point, then the reader should have no clue what's happening, who your characters are, or what it is they're so worried about. Time to make them jump out of their seats! “John and Janet had finally solved the murder. It had been some other guy all along. They were sitting down to a delicious lasagna that Janet had baked when suddenly . . .”

ENDING OPTION 1 is GOOD

“. . . . Janet's head exploded! Janet had been injected with a toxin that explodes heads. John stopped eating his lasagna. (beat) Or did he?” (Waits awkwardly for audience applause, then continues)

ENDING OPTION 2 is BETTER

“. . . a big bomb dropped on the house, killing both of them, but mostly Janet. The bomb had been launched in Iraq because of a war there, but the guidance system had shorted out, so it went over to Janet's place instead and flew right into her head. John had a mouthful of lasagna at the time and was flabbergasted. Everyone else was flabbergasted, too. "We never saw that coming," they said. (Waits awkwardly for audience applause, then continues in the most animated fashion)

ENDING OPTION 3 is SUSPENSETASTIC!

. . . a murderer walked in the house! "Oh no, a murderer!" John said as he stopped eating his lasagna. The murderer chased John all through the house and murdered him while Janet escaped. She ran outside and flagged down a policeman who was driving by. "There's a murderer in my house!" Janet said. "He's not in your house," said the policeman. "He's ME!" Holy *moly*! The policeman was the murderer! He murdered Janet. (Lightning crashes) (Pinkerton bows repeatedly as if to rounds of applause from a packed audience)

Great suspense writing is not easy. But with a lot of practice, you will, I assure you (beat) NEVER be as good as I am.
```

---

## IC-2053: I Have No Mouth, and I Must Scream

- Title: I Have No Mouth, and I Must Scream
- Author (byline): Harlan Ellison
- Work: Harlan Ellison – Greatest Hits; Pgs 19-37
- Publisher: Union Square and Company
- Publication date as stated: Mar 2024
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: AM, TED, ELLEN, VOICE OFF STAGE
- Teaser before the introduction: Yes
- Spoken words (computed): 1651
- Already set (do not supply): none

### Source block (context only)

```text
Author: Harlan Ellison
Book: Harlan Ellison – Greatest Hits; Pgs 19-37
ISBN: 978-1454953371
Publisher: Union Square and Company
Date (Month/Year): Mar 2024
```

### Introduction (context only: never use it for content warnings)

```text
Should we be afraid of Artificial Intelligence?
```

### Performance text (classify this)

```text
AM: (Pgs 19-37) (off stage - a computer voice) Hate. Let me tell you how much I’ve come to hate you since I began to live. There are 387 million miles of printed circuits in wafer thin layers that fill my complex. If the word HATE has engraved on each nano angstrom of those hundreds of millions of miles, it would not equal one one-billionth of the HATE I feel for humans at this micro-instant. HATE. HATE.

From Elon Musk to Bill Gates; from the Swedish philosopher Nick Bostrom to Stephen Hawking; many people from the world of Science, Technology and Philosophy have expressed opinions that vary from one extreme to the other. There are those who believe that AI will be the end of humanity; others believe it will be a great achievement that will raise our quality of life above anything ever imagined.

Artificial Intelligence is on the horizon. Will it solve mankind’s greatest problems or will it end the history of our species? Harlan Ellison speculated on the future of a sentient computer in 1968. I Have No Mouth, and I Must Scream by Harlan Ellison

TED: AM. At first it meant Allied Mastercomputer, and then it meant Adaptive Manipulator, and later on it developed sentience and linked itself up and they called it an Aggressive Menace, but by then it was too late, and finally it called itself AM, emerging intelligence, and what it meant was I am . . . cogito ergo sum . . . I think, therefore I am. The Cold War started and became World War Three. It became a very complex war, so they needed the computers to handle it. They began building AM and everything was fine. They honeycombed the entire planet, adding on this element and that element. But one day AM woke up and knew who he was. He linked himself and began feeding on all the killing data, until everyone was dead, except for the five of us.

None of us knew why AM had saved five people, or why our specific five. We had been kept alive, rejuvenated, made to remain constantly at the age we had been when AM had brought us [here], and they hated me because I was the youngest -- the one AM had affected least of all.

Benny had been a brilliant college professor; now he was little more than a semi human. He had been handsome, the machine had ruined that. He had been lucid, the machine had driven him mad.

Gorrister was a conscientious objector; a peace marcher; he was a planner, a doer, a looker-ahead. AM had turned him into a shoulder-shrugger, had made him dead in his concern. AM had robbed him.

Nimdok went off in the darkness by himself for long times. I don't know what it was he did out there, AM never let us know. But whatever it was, Nimdok came back white, drained of blood, shaken, shaking.

And Ellen. AM had left her alone. All her talk of sweetness and light, all her memories of true love, all the lies she wanted us to believe: that she had been a virgin before AM brought her down here with us.

I was the only one still sane and whole. Really! AM had not tampered with my mind. Not at all. I only had to suffer what he visited down on us. All the delusions, all the nightmares, the torments. It was our one hundred and ninth year in the computer. Immortal, trapped, subject to any torment he could devise for us from the limitless miracles at his command.

If there ever was a Jesus and if there is a God, please please please let us out of here, or kill us.: AM was intent on keeping us, twisting and torturing us forever. The machine hated us as no sentient creature had ever hated before. And we were helpless. It also became hideously clear: If there was a Jesus and if there was a God, the God was AM. (long beat, shakes head to clear it)

AM wasn't God, he was a machine. We had given AM sentience. Inadvertently, of course, but sentience nonetheless. We had created him to think, but there was nothing it could do with that creativity. In rage, in frenzy, the machine had killed the human race, almost all of us, and still it was trapped. AM could not wander, AM could not wonder, AM could not belong. He could merely be. And so, with the innate loathing that all machines had always held for the creatures who had built them, he had sought revenge. In his paranoia, he had decided to reprieve five of us, for a personal, everlasting punishment that would never serve to diminish his hatred . . . He would never let us go. We were all he had to do with his forever time.

We could not die. We had tried it. We had attempted suicide, oh one or two of us had. But AM had stopped us. We would be given filth and scum to eat; or nothing at all. AM would keep our bodies alive somehow, in pain, in agony.

The hunger was something that had come to life; alive in my belly, even as we were in the belly of the Earth, and AM wanted the similarity known to us. So he heightened the hunger. There is no way to describe the pains that not having eaten for months brought us. And yet we were kept alive. Stomachs that were merely cauldrons of acid, bubbling, foaming, shooting spears of sliver-thin pain into our chests. It was the pain of the terminal ulcer, terminal cancer. It was unending pain . . . [And now] Nimdok was hallucinating that there were canned goods in the ice caverns. (to the group) We'll hike all that way and it'll be putrefied or some damn thing. I say forget it. Stay here, it'll have to come up with something pretty soon or we'll die.

ELLEN: I've got to have something, Ted. Maybe there'll be some Bartlett pears or peaches.

TED: We left on a Thursday. The machine always kept us up-to-date on the date. The passage of time was important; not to us, but to him . . . it . . . AM.

One day he decided to cause an earthquake, at the same time rooting us to the spot with nails through the soles of our shoes. Ellen and Nimdok were caught when a fissure shot its lightning-bolt opening across the floorplates. They disappeared and were gone. When the earthquake was over Benny, Gorrister and myself continued on our way. Ellen and Nimdok were returned to us later that night, with a celestial chorus singing:

VOICE OFF STAGE: (sing the first line from *Go Down Moses) “Go down Moses/ Way down in Egypt land / Tell all pharaohs to / Let my people go.”

TED: The archangels circled and dropped the hideously mangled bodies. We kept walking, and Ellen and Nimdok fell in behind us.

It was a long trip to the ice caverns, to find the canned food. We passed through the cavern of rats, through the path of boiling steam, and through the country of the blind. And we came, finally, to the ice caverns. The stalactites were as thick and glorious as diamonds -- smooth, sharp perfection. [When they fell, they plunged down softly, erect in the snowdrifts. Spears, hundreds of them, protruding from the snow.

We saw the stack of canned goods. Benny pawed them and gummed them and gnawed at them, but . . . AM had not given us a tool to open the cans. Surrounded by madness, surrounded by hunger, I knew death was our only way out. AM had kept us alive, but there was a way to defeat him. Not total defeat, but at least peace. I would settle for that. I drew a huge ice-spear from the snow.

All in an instant: I drove the great ice-point like a battering ram. It struck Benny just under the rib cage, drove upward through his stomach and broke inside him. He pitched forward and lay still. I pulled another spear free and straddled Gorrister, driving the spear straight down through his throat. Ellen realized what I had decided. She ran at Nimdok with a short icicle, as he screamed, and the force of her rush did the job. His head jerked sharply as if it had been nailed to the snow crust behind him. All in an instant.

I could hear AM draw in his breath. His toys had been taken from him. Three of them were dead, could not be revived. He could keep us alive, by his strength and talent, but he was not God. He could not bring them back. I knew we had only a heartbeat before AM would stop us.

I struck Ellen and she folded toward me, bleeding from the mouth. I could not read meaning into her expression, the pain had been too great, had contorted her face; but it might have been thank you. It's possible.

AM was furious. He roared and sent locusts. It didn't do a thing; they stayed dead. I thought AM hated me before. I was wrong. It was not even a shadow of the hate he now slavered from every printed circuit. He made certain I would suffer eternally and could not do myself in. (long pause as he morphs into what he becomes)

He left my mind intact. I can dream, I can wonder, I can lament. I remember all four of them. I know I saved them from what has happened to me, but still, I cannot forget killing them. AM has altered me. I am a great soft jelly thing. Smoothly rounded, no mouth, pulsing white holes filled by fog where my eyes used to be. Rubbery appendages that were once my arms; bulks rounding down into legless humps of soft, slippery matter -- a thing that could never have been known as human. At least the four of them are safe at last. And yet . . . AM has won . . . he has taken his revenge . . . I have no mouth. And I must scream.
```

---

## IC-2054: I Need My Monster

- Title: I Need My Monster
- Author (byline): Amanda Knoll
- Work: Not specified
- Publisher: Flashlight Press
- Publication date as stated: 2009
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ETHAN, HERBERT, RALPH, CYNTHIA, MACK, GABE
- Teaser before the introduction: Yes
- Spoken words (computed): 984
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amanda Knoll
ISBN: 978-0979974625
Publisher: Flashlight Press
Date (Month/Year): 2009
```

### Introduction (context only: never use it for content warnings)

```text
Every night, kids across the globe worry that there’s a monster hiding under the bed. It’s a common fear that most adults can relate to—the fear of monsters isn’t new. It’s a fear that pre-dates video games and social media and has persisted throughout the generations. But for Ethan, his worry is that his monster ISN’T under his bed. I Need My Monster by Amanda Knoll turns this childhood fear on its head with humor and giggles and an assortment of substitute monsters!
```

### Performance text (classify this)

```text
ETHAN: Tonight, when I looked under the bed for my monster, I found this note instead: “Gone Fishing. Back in a week. –Gabe” What was I going to do? I needed a monster under my bed. How was I supposed to get to sleep if my monster was gone? I tried to sleep, but it wasn’t the same with Gabe. I missed his ragged breathing (Gabe – ragged breathing) His nose-whistling. (Gabe – nose whistles) The scrabbling of his uncut claws. (Gabe – Scrabbles his claws) How would I ever get to sleep without Gabe’s familiar scary noises and his spooky green ooze? (Gabe – plays with his ooze) It was no use. Gabe would be gone for a week and I just had to have a monster.

ETHAN: I climbed quietly out of bed so my parents wouldn’t hear me. (Grown-ups have some strange ideas about monsters under beds.) I knocked on the floorboards, then scrambled back under my covers. I waited nervously. Would a new monster appear? What would he be like? Would his snorting be as cheerful as Gabe’s? (Creaking) When I heard some creaking under my bed, I knew that the substitute monster had arrived.

HERBERT: (a low, breathy voice) Good evening. My name is Herbert and I will be your monster for the evening.

ETHAN: Herbert? What kind of name is that for a monster?! You don’t sound scary at all. Have you ever scared a kid before?

HERBERT: Well, no, but I have read all the best books on the topic.

ETHAN: Do you have long teeth and scratchy claws?

HERBERT: No, but I have an overbite. And I’m a mouth breather. Listen (Herbert mouth breathes: hihi-huh, hih-huh, hih-huh, hih-huh)

ETHAN: (to audience) Herbert’s panting was kind of scary, but it wasn’t enough for me. (to Herbert) Listen, Herbert, I’m sorry. I just don’t think this is going to work. It’s nothing personal, but I really need a monster with claws.

HERBERT: Picky, picky! As you wish. I’ll go.

ETHAN: There was some more creaking. Then Herbert was gone. (Scratching noises) Some scratching warned me that a second monster had appeared.

RALPH: (in a high, silky voice) Good evening. My name is Ralph. I understand you need a monster with claws. If you would please lean over, I will hold out an arm for inspection.

ETHAN: I crouched on the edge of the bed, hoping to see a horrible shaggy arm with sharp, ragged nails. Instead, I was surprised to see sleekly brushed fur with smooth, shiny claws. (To Ralph) Excuse me, I don’t mean to be rude, but is that nail polish on your claws?

RALPH: Yes, it is. I believe professional monsters should always be well-groomed.

ETHAN: (Heavy sigh) I could tell that this was not going to work either. (To Ralph) I’m sorry to disappoint you, Ralph, but I need a monster with scary claws. (To audience) Like Gabe’s. (Scratching noises) I heard some more scratching and I knew Ralph was gone.

CYNTHIA: (Raspy voice) Check out these claws, kid!

ETHAN: I gather my courage and peered over the edge. The claws were impressive – jagged and dark and razor-sharp. SO far, so good. I was a little nervous. (To Cynthia in a whisper) Could you stick out your tail?

CYNTHIA: Sure, but don’t get scared!

ETHAN: I peeked through my fingers at the slimy tail slithering over the foot of my bed. That’s when I noticed the bow. (To Cynthia) Are you a girl monster???

CYNTHIA: Of course I am. (Snappishly) I’m Cynthia. Do you have a problem with that?

ETHAN: Um, yeah, I do. I definitely need a boy monster. Boy monsters are for boys and girl monsters are for girls. Everybody knows that.

CYNTHIA: (Sniffing) Well, aren’t you a picky one! (Cynthia exits – be creative)

ETHAN: And then she was gone. Was I being too picky? NO! I knew that my monster needed to be well-clawed and menacing. The whole point of having a monster, after all, was to keep me in bed, imagining all the scary stuff that could happen if I got out. (Shuffling noises and slobbering) A fourth monster was under my bed.

MACK: Hey. The name’s Mack. (Extending his claws from under the bed)

ETHAN: One look at his claws proved that Mack was a big, scruffy BOY monster. I shivered. Maybe this one would work out. (To Mack) Those are excellent claws, but do you have a long tail? (Ethan leans over the bed to see)

MACK: (Slurping) No, my tail is stumpy. But I do have an unu-u-u-usually lo-o-o-ong . . . tongue!

ETHAN: Why would I be afraid of a long tongue?

MACK: (Trying to sound terrifying) Oh, I don’t know . . . You never know when I-I-I mi-i-i-ight . . . lick you!

ETHAN: (erupts into laugher)

MACK: (Whining) Well, if you’re not even going to try-y-y-to work with me . . . (Ethan tries to stop laughing) I re-e-e-eally don’t think you should send me away. Kids who reject five monsters in one night

ETHAN: (Interrupting) I did NOT reject five monsters tonight! My regular monster went fishing.

MACK: Fishing, eh? Maybe he just left because you’re SO- O-O picky. Fine. I’m out of here. But I wouldn’t expect another monster tonight if I were you. (Mack exits – be creative)

ETHAN: (looks around his room. Looks under the bed. Tries to sleep but can’t. Sits up) How was I ever going to get to sleep without my monster? I was surprised to hear more creaking under the bed. (Loud creaking and scratching) (To the monster under the bed) I – I thought no more monsters were going to appear tonight.

GABE: Sorry I’m late, kid

ETHAN: (To audience) Whew. It was Gabe.

GABE: I thought I would enjoy fishing, but I didn’t. Those fish scare too easily. No challenge at all. You, however, are challenging, my friend. You’re almost too old to be afraid of monsters. You keep me on my toes. . . Ah, toes . . . a delicious snack. (Gabe’s stomach rumbles with hunger) Now, if you don’t mind, I’d like to start the evening with an ominous puddle of drool.

ETHAN: I peeked over the edge of the bed. Green ooze spread soundlessly from underneath. Then the bed trembled as Gabe unfurled his spiked tail. He was daring me to guess where he might pop up. (Shivers)

GABE: So, you had some substitute monsters tonight.

(Sharpening his claws on the bedpost) Were you . . . . scaaaaaared? (Gabe taps his claws impatiently on the bedpost)

ETHAN: When Gabe started tapping, I could tell he wanted to know if I still needed him. No other monster can scare me like you! (Giggling and diving under the covers, pulling them up tight)

GABE: (Soft, comforting snorts then growling) Ha! I knew it! We’re made for each other. (Gabe begins to pull the blanket off the bed) Now, if you could please stick out your foot . . . I’d like to nibble your pinkie.

ETHAN: (yanking the blanket back up and scrunching his feet in so Gabe can’t get them) No toes tonight, but you can have this! (pushes a pillow off the bed) (To audience) I didn’t even hear it hit the floor. Gabe was back. The ooze was perfect. Everything was back to normal. (Shivering again) I’d be asleep in no time.
```

---

## IC-2055: I Never Knew

- Title: I Never Knew
- Author (byline): Rosanne Martorella
- Work: Chicken Soup for the Teenage Soul on Tough Stuff
- Publisher: Health Communications
- Publication date as stated: Oct 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1453
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rosanne Martorella
Book: Chicken Soup for the Teenage Soul on Tough Stuff
ISBN: 978-1558749429
Publisher: Health Communications
Date (Month/Year): Oct 2001
```

### Introduction (context only: never use it for content warnings)

```text
According to a 2020 study by the American Academy of Child and Adolescent Psychology, approximately 1 in every 4 girls and 1 in every 13 boys in the US experience sexual abuse at some time in their childhood. Because no child is prepared to cope with the repeated pain and fear of sexual abuse, victims have a higher chance of developing depression, PTSD, and drug addictions. For some, like Cindy, the pain and despair are simply too much to bear. I Never Knew by Rosanne Martorella
```

### Performance text (classify this)

```text
She was my best friend and I loved her. She was the coolest girl in junior high and everyone wanted to be like her…and she chose me to be her best friend. Her name was Cindy. She was beautiful with her black hair and tall, thin body. While the rest of us in eighth and ninth grade were still looking amorphous, trying to take shape, Cindy was already beautifully poised in her adult body.

Her mother had died when she was a little girl. She was an only child and she lived alone with her father. By the time we would get home from school every day, he would already be at work. He wouldn't come home until two or three in the morning, so we had free reign of the house. No parental supervision was the greatest thing we could ask for as teenagers. Her house was a big, two-story that was concealed by a large grove of orange trees. You couldn't see the house from the street, and we liked it that way. It added to the mystique and allure that we were always trying to create.

At school she was pretty much the center of attention. One whole corner of the quad was dedicated to Cindy and her "followers." If there was new music, clothes, hairstyles or even new ways to take notes or study, you could be fairly sure that it came out of that corner of the quad. Even the school faculty caught on to the power this girl held, and convinced her to run for class president. Cindy and I were voted in as class president and vice president by a landslide.

By day we were the acting liaison between students and faculty, by night we hosted social activities at Cindy's house. If we weren't having a party, people would come just to hang out anyway. Kids would be there for all kinds of reasons - to talk about relationships, their parents, to do their homework, or just because they knew someone they liked would be showing up.

After everyone left, I would usually spend the night. My mom wouldn't like it very much if it was a school night. Sometimes Cindy would come back to my house to spend the night, but my mom didn't like that much either because we would stay up all night laughing and talking. Cindy didn't like to be home alone.

That following summer, after I came home from vacation with my family, things were starting to change. Cindy looked thinner than usual with dark circles under her eyes, and she had started to smoke. The strikingly beautiful girl looked pale and gaunt. She said she missed me a lot. While it was a boost to my ego, I couldn't believe it could be entirely true. After all, there were always people trying to be close to her and get into her circle of friends.

My solution: two weeks at the beach. Our parents pitched in to rent a beach house in Ventura for two weeks. My mom would be the only supervision. In Cindy's inimitable style, we collected a group of beach friends within a couple of days. We'd all hang out at this local café during the day, when we were not in the water or on the sand, and at night we'd hang out around this fire pit on the beach.

Cindy started to look like her old self, but better. She was tan. She looked great in a bikini and all the guys on the beach wanted to be around her. But she was still smoking. She told me it calmed her nerves.

One night, Cindy came back to the beach house very late. She was all disoriented and noticeably excited.

She told me she and this one guy had been drinking and smoking marijuana, and they had gotten together. She said that I had to try marijuana because it made everything better, clearer, in fact. She said she really liked this guy and wanted to run away with him. I knew she was just high and she'd feel differently in the morning.

When school started that next year, things weren't the same and I missed the old routine. Cindy wanted to get into different things than I wanted, and she started hanging around guys more and more. We would still hang out from time to time, but it wasn't as fun as it used to be. Cindy would get really serious and tell me that I just didn't understand how things were. I just thought that she was maturing faster emotionally than the rest of us, like she had physically.

One morning when I arrived at school, there were police cars all around and a lot of nervous activity in the halls. When I proceeded toward my locker, my counselor and another woman stopped me. I was asked to follow them to the office. My heart was pounding so fast and hard that I could hardly catch my breath. My head was racing with the different scenarios that might have caused this odd behavior.

When we all sat down in my counselor's office, the principal came in and took a seat. Was I in some kind of trouble? The principal began by prefacing the news by talking about life and maturity and circumstances. Now my head was really spinning. And then it happened. My world froze in time with the words, "…And Cindy took her own life last night using her father's gun." I couldn't talk, I couldn't move. Tears started to stream from my eyes before my heart could even comprehend the pain. She was only fifteen years old.

As the suicide note explained, her father had repeatedly sexually abused her and she knew no other way out. Months after he was arrested, he finally confessed. The note also said something else. It said that the only family she ever knew and cared about was me. She left me a ring that her mother had left to her.

I cried for weeks. How is it that I never knew? We were closer than anyone and talked about everything; how come she never told me that? I was certain that I could have helped her and I began to blame myself.

After weeks of grief counseling, I came to understand that the burden of Cindy's sexual abuse was too much for her to bear, especially when she started to become intimate with boys. The counselor explained to me that her shame was too great to even talk about, even to her best friend. It dawned on me how alone she must have felt and it suddenly became clear to me why she never wanted to spend nights alone in her own house.

My own suffering - weeks of pain and confusion - was eased greatly with all the help and support I received. Teachers, counselors, friends and family members all participated in nurturing me. It was clear to everyone that this situation was going to change my life forever, but because I let help in, it would subsequently add to my life an aspect of wisdom and compassion. I had wished that Cindy could have known the relief that comes from letting others help you with your pain.

Cindy's suicide note also requested that she be cremated. The note said that I should spread her ashes wherever I wanted to. I chose the ocean off the beach where we had spent two weeks that summer.

On the day of the memorial we rented a boat to take us out to sea. The boat was packed with friends and teachers, even though it was a rainy, overcast day. We stood on the bow and took turns sharing our experiences and love for our friend. When it came time for me to free her ashes, I was hesitant. I didn't want to turn them loose in a sea that looked dark and menacing. I thought she had had enough of that in her own life.

My hesitancy gained attention and both my mother and my counselor stepped up on the platform and put their arms around me. With their support I opened the lid and set my friend free. As some of the ashes hit the surface of the water, the sun broke through for a moment and sent beautiful rays of light that sparkled on the surface of the water. The clouds parted some more and soon the whole boat was bathed in warm sunlight. At that moment, I felt calmer than I had in weeks. Somehow I knew that the Angels had come for my friend and that she would be all right - and so would I.
```

---

## IC-2056: I Stopped Writing Poetry

- Title: I Stopped Writing Poetry
- Author (byline): Bernard Welt
- Work: Not specified
- Publisher: Scribner Paperback Fiction
- Publication date as stated: Sept 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1286
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bernard Welt
ISBN: 978-0743203845
Publisher: Scribner Paperback Fiction
Date (Month/Year): Sept 2001
```

### Introduction (context only: never use it for content warnings)

```text
Through the emergence of numerous poetry classes and more forgiving professors, we now have an influx of really bad poetry. Poetic style, the people who write it, is diverse, as poet Sharon Creech once wrote, "any words can be a poem; you've just gotta make short lines..." The following poetic selection seeks to examine the parallels between the state of poetry today and the diversity of life. I stopped writing poetry... by Bernard Welt.
```

### Performance text (classify this)

```text
I stopped writing poetry
when the internet replaced the telephone
(since now that *everyone* has a phone,
and takes it *everywhere*, it's obvious
the telephone is *over*). Ted Berrigan I thought
destroyed the sonnet by inviting the beloved
to just pick up the phone and call him
sometime-- thus no more need to plead
and seduce through verse--
I stopped writing poetry
When I was just starting to get good at it. First,
I got good at rhyme, so I cast it away.
Then I got good at line and stanza construction--
So good I hardly needed to *say* anything at all.
My meanings emerged
in the spaces between.
So I got rid of that, too. Metaphor, metonymy,
Allusive echoes of my betters -- well, frankly,
I was a whiz at that stuff pretty early on.
So I emptied out the file drawers
Of rhetorical strategy, musical form,
Continuity or criticism of tradition,
And I just wrote. Finally I found
I was writing... *prose*, like everyone else.
But it was prose with a difference: prose with a rich,
Totally hidden other life lying behind it, unglimpsed
(I think) by the reader. Not like a prostitute
Who reforms and becomes a nun. I've seen
That movie. More like a nun who becomes a prostitute.

I stopped writing poetry but I still love the stanza. All that other cool stuff-- tropes, the caesura, enjambment-- I can live without. But the *stanza*-- wow.

I stopped writing poetry after I went to my first MLA conference, where they were attacking a way of reading and understanding literature they called "mainstream" and "dominant" that I'd never even encountered. It was like what they meant by "book" was totally different from what I meant by "book"-- as different as "washing machine" and "golf ball."

I stopped writing poetry when people began writing scholarly articles explaining how to read Frank O'Hara's _Lunch Poems_ and it never occured to them to mention that you should read them during lunch.

I stopped writing poetry
when everyone else did-- in the early 90s, when
television
became more interesting than culture.

I stopped writing poetry when it became popular. I realize Robert Frost read at Kennedy's inauguration but now Ethan Hawke is telling _Vanity Fair_ that he keeps *your* book by his bed, and poetry as adjunct to commercial culture and the veneration of celebrity is so much more deliciously embarrassing for everyone than even poetry in the service of the state.

I stopped writing poetry because I promised to. I read something in which I encouraged everyone to give up writing-- as I engaged to-- and it went over real big. Afterwards any time I ran into any of the poetry crowd they'd always ask me if I was still not writing. I understood it was a performance piece and so did they but I keep getting this gnawing feeling I was abandoning a prinicple by continuing to write. It was entirely superstition, like actually feeling sick when you call in sick, but I suppose I have been a victim of the terrible conviction that you must mean what you say. I stopped writing poetry when I had dedicated poems to everyone I knew, at least everyone I wanted to impress. I promise to start writing poetry again as soon as I meet some new people. Interesting people, anyway. Interesting people I can't just come out and *say* things to, anyway.

I stopped writing poetry at 16 (seriously), then again at about 20 but only for six months, once again at 27, then at 32, 35, 40, and 42. I'll keep you posted.

I stopped writing poetry when I received the praise of people I admired. It's a terrible thing to receive exactly the attention you want when you are unprepared to admit you might deserve it. Of the many ways in which poets are always going on about how poetry not only receives inspiration from love but imitates it in form and feeling, this just may be the worst.

I stopped writing poetry-- well, basically, because I'm white. I don't *like* being white, it isn't a choice I'd make freely, and to get argumentative I don't think it's entirely fair that I have to be white right now when it's so 10 minutes ago when if I'd been born fifteen years earlier most racists would have considered me anything but, what with the whole Jew-as-vermin thing, but OK, OK, I concede the point, I'm culturally white, or whatever,

and in case you haven't noticed, this just isn't white people's moment, poetry-wise. Don't even get me *started* on the great tradition and that stuff, I mean, just look at rap-- poetry that communicates exquisitely within its chosen boundaries of class and common interest, and hardly at all outside it, except for those to whom it stands as aspiration to cool. Just like Shakespeare and Donne. What have white people contributed to culture recently? *Postmodernism*? Please. My own revelation came when I realized "Little Red Corvette" meant more to me than any poem published since the early 1970s. On the not-very mean streets where I learned versification, poetry wasn't a mode of expression spontaneously developed from living people's lived experience, it was a regime. Well, that's over now. Get over it.

I stopped writing poetry when I got married-- I mean settled down-- since the laws of the state of Maryland do not allow me to marry the love of my life-- though I'm not here to whine about it-- and maybe marriage would ruin me as it seems to have ruined others-- but one thing I know-- it is certainly nice to have someone to blame for taking it easy and resisting inspiration when it inconveniently insists on arising occasionally no matter what you do

I stopped writing poetry When my friends started dying. Some of my friends Wrote beautifully about the conditions of their illness, And insightfully about mortality and their own impending Death. Some wrote angrily about their invisibility And created a literature of testimony in which we learn What it was like to walk in the streets of American cities As a ghost. Some wrote poems to memorialize their lovers. Or to embarrass right-wing senators or arts funding agencies. But I counted 67 people I knew and was fond of Who've died of "AIDS-related illness," and not once Have I genuinely felt I could respond to their suffering or death In poetry. Is it poetry? Is it me? The era? I am willing to believe That if Milton and Shelley and Tennyson could do it, It can still mean something. Why should I think their ages Made death any more manageable a subject than mine? But whenever I sat down to try, I stopped in despair. Whatever the political advantages of slogans Of the time, it wasn't the right words I looked for But some way to make silence heard in lines Of verse, and I never found it.

I stopped writing poetry when it was eclipsed by criticism for purely sociological and economic reasons. I stopped writing poetry when taking it seriously started seeming more likely to indicate intellectual complacency than intellectual liveliness. I stopped writing poetry when it got boring.

I stopped writing poetry but as satisfying as it has been to turn my back on it as on a distant homeland fallen under the spell of a fascist party still a breeze reaches me from time to time fragrant of verse and suddenly I am as nostalgic as an exiled Russian grand duke waiting on tables in Paris in a screwball comedy sometimes I wonder would it really be so terrible if I wrote just one more line Now even that Sounds like a device to me, like special pleading. Let someone else do it.
```

---

## IC-2057: I’ll Be Looking for You, Ace

- Title: I’ll Be Looking for You, Ace
- Author (byline): Jennifer Lohrfink
- Work: Chicken Soup for the Teenage Soul
- Publisher: HCI Teens
- Publication date as stated: May 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1085
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jennifer Lohrfink
Book: Chicken Soup for the Teenage Soul
ISBN: 978-1558744639
Publisher: HCI Teens
Date (Month/Year): May 1997
KS State Qualifier
MN State Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
One of the great losses in life is the death of a brother or sister, yet this is one of the most neglected types of grief. Everyone wonders how the parents can cope with the loss of a child, but nobody knows how hard it is for the rest of the family too. Nobody tells you what to do when your little brother dies. I’ll be Looking for You, Ace by Jennifer Lohrfink
```

### Performance text (classify this)

```text
(Pg 228-231) Dear Michael,

So, Ace, what's it like up in heaven? Everything it's cracked up to be? People say it's supposed to be beauti-ful; but really, how would anyone know? Maybe that's why I used to be so afraid of dying-because we do not know what is next. Oddly enough, my feelings have changed since you left.

I was at work that Saturday, December 6, with only an hour to go until I had to pick you up at Vinny's house.

Then the phone rang. It was our sister, Lauren. I was expecting to hear the usual "Remember to bring home some shampoo." Instead, there were words that reverberated through my head: "Mike's been hit by a car."

I went numb, and I shook during the entire drive to St. John's Hospital. I remember praying that your face would not be disfigured and that you did not break too many bones. Death was not even a possibility. I figured you were too good a kid, too strong, too young (you were only 11) and too well-liked to be seriously hurt.

My worst nightmare could not compare with what I found facing me. I was ushered into the doctor's lounge, where our whole family and your friends were huddled. Phrases such as "Holding his own," "It could go either way" and "There's always hope with kids" floated past my ears. I sank onto a couch. While you were in surgery, I prayed the hardest I ever prayed in my life. Then, a few hours later, the doctors let Lauren, Jeff and me up to see you in the intensive care unit.

There you were. Underneath the casts, bandages, bruises, stitches and tubes was the beautiful little brother I loved. The doctors said that even though you were in a coma, you might be able to hear, but I couldn't speak. Nothing I felt could be put into words. I wanted to give you the world, but I could only hold your hand. I kept thinking, Come on, Mike. You can make it.

At about 10:30 that night Lauren, Jeff and I went home while Mom and Dad stayed. We played some of your albums so loud the floor shook-you would have been so proud of us! [Insert lyrics from KISS Song here: suggestion – “I wanna rock and roll all night . . . and party every day.” *Hear the song here: https://www.youtube.com/watch?v=B_oFiNdp8UQ ]

After a while, I tried to fall asleep on the couch, but my mind raced. I kept thinking of how you and I danced the whole day together at cousin Becky's wed-ding, how you'd jump around· in your room playing air guitar, and how you messed up your lines at the Christmas play tryouts so that Brian could get the part he wanted so badly. I thought how great life was with you; without you it would be unbearable. I was so scared.

We all did what we could for you. As an offering, Uncle Bob gave up smoking-and you know what a chain smoker he is! Your best friend, Matthew, went to church and lit 21 candles (your basketball number) for you. Lauren, Jeff and I were planning a party for you when you came home. Mom and Dad were going to get Ace Frehely [lead guitarist from KISS] to visit you.

All the hoping and planning and praying got us through that first night. In the morning, you were trans-ferred to Columbia-Presbyterian Hospital, where it was thought that your chances for survival were greater. In Babies I.C.U. (don't get offended, Mike-Babies I.C.U. goes up to age 19!) a team of wonderful doctors and nurses stayed with you around the clock. I was there for you too, coaching you in my mind, as I used to cheer you on at your Little League games last spring. Come on, Mike-give it your best shot. This is not a game. This is for real.

Well, Ace, you made it through one more night. When we got to the hospital early Monday morning, you were having a CAT scan done. We were told we could see you afterward. You came back in cardiac arrest, with the doctors giving one last scramble for your life.

My mind was frantic. You cannot die, Mike! You have too much to live for! What about the guitar lessons you were going to take-the band you were going to start with Matt and Vinny? What about the basketball team-you're the starting center. Wait, Mike, don't go. I love you too much to lose you. Keep fighting, please!

Well, Ace, I know you did what you could. You could only fight so long with so much against you.

It was the worst moment in my life when I heard "He's gone." The room spun. I felt detached from my body, as if the pain of this startling reality was too much to bear. I wanted to die too, to be with you, to make sure you were okay.

After they took out all the tubes and monitors, the doctors let me in to see you once more. I felt that your soul was close. I wanted to shake your shoulders and have you open your eyes. Instead, I gave you a kiss and rested my face against yours, willing to do anything to bring you back. The only thing I could do was let you go.

Mike, I know you're still with me. I know you're helping me get on with my life. I learned so much from you. You taught me to live one day at a time, to appreciate everything that comes along, to laugh and have fun, to be honest, to accept people for what they are. And while 11 years is a short time, we filled them with so much happiness that can never be lost, even now.

The one thing you really did for me was take away my fear of death. I am no longer afraid. I know that God must have something wonderful waiting for a kid like you. My faith has also been strengthened, because if I did not believe in God and heaven, where would you be? Heaven has got to be beautiful with you there. I know that when my time comes, I will be looking for you. Could you be watching so we find each other? I really miss you, Ace, but I know that you are still with me, and I know we will see each other again.

I love you. . .
```

---

## IC-2058: In Depth, But Shallowly

- Title: In Depth, But Shallowly
- Author (byline): Dave Barry
- Work: Bad Habits
- Publisher: Henry Holt & Company, Inc.
- Publication date as stated: Sept 1993
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ANNOUNCER, WESTBROOK, KERNEL, MAYOR, SNAPE, TOMPKINS, EDWARDS, STEVENS, JOHNSON, HOLP
- Teaser before the introduction: No
- Spoken words (computed): 1117
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Barry
Book: Bad Habits
ISBN: 978-0805029642
Publisher: Henry Holt & Company, Inc.
Date (Month/Year): Sept 1993
```

### Introduction (context only: never use it for content warnings)

```text
Newsflash: The daily news isn't an accurate reflection of what's really going on in the world today. It indicates what's going wrong with our world – how much death and destruction has occurred and how many murders/suicides/bombings/explosions went down. But it doesn't portray neighbors helping neighbors, communities banding together to raise money for cancer research, cops catching criminals, diseases going into remission, babies born healthy, personal achievements celebrated, milestones passed, or victories won! You shouldn't watch the evening news because it rarely shares good news. Hmmmm. Options . . . What about the LOCAL NEWS . . that should be where we see the GOOD stuff, right? WRONG . . . In Depth, but Shallowly by Dave Barry.
```

### Performance text (classify this)

```text
If you want to take your mind off the troubles of the real world, you should watch local TV news shows. I know of no better way to escape reality except perhaps heavy drinking.

Local TV news programs have given a whole new definition to the word news. To most people, news means information about events that affect a lot of people. On local TV news shows, news means anything that you can take a picture of, especially if a local TV News Personality can stand in front of it. This is why they are so fond of car accidents, burning buildings, and crowds: these are good for standing in front of. On the other hand, local TV news shows tend to avoid stories about things that local TV News Personalities cannot stand in front of, such as budgets and taxes and the economy. If you want to get a local TV news show to do a story on the budget, your best bet is to involve it in a car crash.

I travel around the country a lot, and as far as I can tell, virtually all local TV news shows follow the same format. First you hear some exciting music, the kind you hear in space movies, while the screen shows local TV News Personalities standing in front of various News Events. Then you hear the announcer:

ANNOUNCER: From the On-the-Spot Action Eyewitness News Studios, this is the On-the- Spot Action Eyewitness News, featuring Anchorman Wilson Westbrook, Co-Anchorperson Stella Snape, Minority-Group Member James Edwards, Genial Sports Personality Jim Johnson, Humorous Weatherperson Dr. Reed Stevens, and Norm Perkins on drums. And now, here's Wilson Westbrook.

WESTBROOK: Good evening. Tonight from the On-the- Spot Action Eyewitness news studios we have actual color film of a burning building, actual color film of two cars after they ran into each other, actual color film of the front of a building in which one person shot another person, actual color film of another burning building, and special reports on roller-skating and child abuse. But for the big story tonight, we go to City Hall, where On-the- Spot reporter Reese Kernel is standing live.

KERNEL: I am standing here live in front of City Hall being televised by the On-the-Spot Action Eyewitness News minicam with Mayor Bryce Hallbread.

MAYOR: That's "Hallwood."

KERNEL: What?

MAYOR: My name is "Hallwood." You said "Hallbread."

KERNEL: Look, Hallbread, do you want to be on the news or don't you?

MAYOR: Yes, of course, it's just that my name is ...

KERNEL: Listen, this is the top-rated news show in the three-county area, and if you think I have time to memorize every stupid detail, you'd better think again.

MAYOR: I'm sorry. "Hallbread" is fine, really.

KERNEL: Thank you, Mayor Hallbread. And now back to Wilson Westbrook in the On-the-Spot Action Eyewitness News Studios.

WESTBROOK: Thank you, Reese; keep us posted if anything further develops on that important story. And now, as I promised earlier, we have actual color film of various objects that either burned or crashed, which we will project on the screen behind me while I talk about them. Here is a building on fire. Here is another building on fire. Here is a car crash. This film was shot years ago, but you can safely assume that objects just like these crashed or burned in the three-county area today.

And now we go to my Co-Anchorperson, Stella Snape, for a Special Report on her exhaustive three-week investigation into the problem of child abuse in the three-county area. Well, Stella, what did you find?

SNAPE: Wilson, I found that Child abuse is very sad. What happens is that people abuse children. It's just awful. Here you see some actual color film of me standing in front of a house. Most of your child abuse occurs in houses. Note that I am wearing subdued colors.

WESTBROOK: (reading from a Script) Are any efforts under way here in the three-county area to combat child abuse?

SNAPE: Yes.

WESTBROOK: Thank you, Stella, for that informative report. On the lighter side, On-the-Spot Action Eyewitness Reporter Terri Tompkins has prepared a three-part series on roller-skating in the three-county area.

TOMPKINS: Roller-skating has become a major craze in California and the three-county area, as you can see by this actual color film of me on roller skates outside the On-the-Spot Action Eyewitness News Studio. This certainly is a fun craze. Tomorrow, in Part Two of this series, we'll see actual color film of me falling down. On Wednesday we'll see me getting up.

WESTBROOK: We'll look forward to those reports. Our next story is from Minority-Group Reporter James Edwards, who, as he has for the last 324 consecutive broadcasts, spent the day in the minority-group sector of the three-county area finding out what minorities think.

EDWARDS: Wilson, I'm standing in front of a crowd of minority-group members, and as you can see, their mood is troubled. (The crowd smiles and waves at the camera.)

WESTBROOK: Good report, James. Well, we certainly had a sunny day here in the three-county area, didn't we, Humorous Weatherperson Dr. Reed Stevens?

STEVENS: Ha ha. We sure did, though I'm certainly troubled by that very troubling report Stella did on child abuse. But we should see continued warm weather through Wednesday. Here are a bunch of charts showing the relative humidity and stuff like that. Ha ha.

WESTBROOK: Ha ha. Well, things weren't nearly as bright on the sports scene, were they, Genial Sports Personality Jim Johnson?

JOHNSON: No, Wilson, they certainly weren't. The Three-County Community College Cutlasses lost their fourth consecutive game today. Here you see actual color footage of me watching the game from the sidelines. The disgust is evident on my face. I intended to have actual color film of me interviewing the coach after the game, but the team bus crashed and everyone was killed.

WESTBROOK: Thank you, Jim. And now, here is Basil Holp, the General Manager of KUSP-TV, to present an Editorial Viewpoint:

HOLP: The management of KUSP-TV firmly believes that something ought to be done about earthquakes. From time to time we read in the papers that an earthquake has hit some wretched little country and knocked houses down and killed people. This should not be allowed to continue. Maybe we should have a tax or something. What the heck, we can afford it. The management of KUSP-TV is rolling in money.

ANNOUNCER: The preceding was the opinion of the management of KUSP-TV. People with opposing points of view are probably in the vast majority.

WESTBROOK: Well, that wraps up tonight's version of the On-the-Spot Action Eyewitness News. Tune in tonight to see essentially the same stories.
```

---

## IC-2059: In Pictures of Gunmetal Gray

- Title: In Pictures of Gunmetal Gray
- Author (byline): Wendy Nikel
- Work: Criminal Scenes: 12 Short Sci-Fi & Fantasy Stories of Crime and Mystery, Pgs 5-12
- Publisher: Independently Published
- Publication date as stated: Mar 2023
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, WOMAN, SUSPECT, MATEO, REPORTER 1, REPORTER 2, REPORTER 3
- Teaser before the introduction: Yes
- Spoken words (computed): 1243
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wendy Nikel
Book: Criminal Scenes: 12 Short Sci-Fi & Fantasy
Stories of Crime and Mystery, Pgs 5-12
ISBN: 979-8387941641
Publisher: Independently Published
Date (Month/Year): Mar 2023
```

### Introduction (context only: never use it for content warnings)

```text
Imagine being able to look at a person or object and see related events, locations or images that may have occurred at various times or places. Now imagine having the artistic ability to draw what you see.

The ability is called “remote viewing “and it gained credibility when the CIA adopted the method as a covert way of gathering intelligence in the early 1970s. Today, there is not enough scientifically compelling evidence to prove the validity of remote viewing; but some case studies leave the door open for the possibility. What if crimes could be solved with help . . .

In Pictures of Gunmetal Gray by Wendy Nikel
```

### Performance text (classify this)

```text
NARRATOR: (Pg 5-12) Willa always told me that to get realistic sketches, you have to draw what you see, rather than what you think you see. Nowhere is that truer than in the courtroom.

NARRATOR: I'm shoved in the third row of the gallery, my elbows bumping those next to me and my stubbled upper lip collecting sweat as I huddle over my sketchpad. I've learned, over the years, how to keep the pencil silent, to pass the charcoal over the page without a sound, to blend in and not draw attention. Still, the woman beside me cranes her neck and whispers,

WOMAN: Is that for one of the papers covering the trial?

NARRATOR: I flip the page shut. She wasn't supposed to see that. (to woman, polite whisper) Freelance, ma'am.

WOMAN: You caught that scumbag's scowl. Gives me shivers. Those poor runaways . . .

NARRATOR: (to woman) Excuse me. (to audience) I work my way to the outer aisle to get some fresh air. From the counsel table near the jury box, Mateo's gaze meets mine, but even though we've been friends since our days of Little League, his face doesn't shift from "prosecuting attorney" mode. I quickly find another seat.

The suspect takes the stand, and Mateo's called up to interrogate him. I flip the page and pull a pencil from my pocket, squeezing it so hard my knuckles crack. It's time.

Whenever I sketch, I think of Willa. She's the one who'd taught me to draw not just what I saw in the physical world -- faces, bodies, buildings, clothes -- but how to make sense of the other things I saw and capture them upon the paper, too. Though five years younger than me, my little sister always knew how to make me feel not quite so alone in my peculiarities. Not quite so strange and afraid.

Now, as the man on the stand rolls carefully selected words over his tongue and out his bloated lips, I sketch his face (asymmetrical, bulbous nose, small eyes), his shoulders (broad, like a linebacker's, but hunched over to make himself appear small and harmless), his tailored suit (expensive, but not too expensive, and as well-pressed as a preacher's). But there's more. As I listen to the back-and-forth of Mateo's questioning and the suspect's stilted answers, the scene that I sketch echoes his testimony, though not precisely as he lays it out.

SUSPECT: Yes, I was there that night at that rest stop, but I didn't see any girl there.

NARRATOR: Yet behind him, in wisps of smoky gray, like a silent movie that only I can see, the memories that spill out from his head tell a different story. A light beams down on him, radiating from a nearby streetlamp. Before him is a dark-haired girl, crouched on the curb. Her mascara is streaked, and she doesn't even look up from her cell phone as he approaches.

MATEO: We found tire tracks near the canyon trailhead where her phone last pinged. They match your truck's. Tell me, are you familiar with this trail?

NARRATOR: As the man's thoughts shift, so does the scene, and I hurry to flip the page so I have room to capture what I see. There are rock formations, shadowy and high, reaching above the witness stand. There's a path before him, and its clarity tells me that he's walked it many times before. There's something draped across his shoulder -- something fuzzy, unclear, as if he only recalls his burden in a vague, disconnected way, as a weight he must carry, rather than an identifiable thing.

The lead of my pencil snaps as it works its way across the page, reconstructing the scene. I fight to keep my focus as I pull a new one from my jacket. I can't afford to lose the thread of memory now. I can't think about the words he's saying; most of them are lies, anyway, and I don't want them to subconsciously distort my sketches. I can't think too much about that obscure and blurry burden, either, or I'll never be able to make it through his testimony.

A cave forms, just before the witness stand. It's only a few feet high and its entrance is blocked by a boulder. Overlaid across the suspect's face is a gray memory of his features, straining and darkening as he shoves it out of the way.

MATEO: You stated that you generally hike alone. Did you ever take anyone else up on that particular trail?

SUSPECT: (lying) Never.

NARRATOR: Their faces appear around his and I sketch them as quickly as I can, trying to catch their eyes (wide with terror), their mouths (open, sobbing) their distinctive features (a mole on the cheek, a scar on the brow, a dimple in the middle of the chin). When I'm satisfied I've captured them all, I set down my pencil.

MATEO: Can we take a recess, your honor?

NARRATOR: I join Mateo in the side chamber and hold out the sketch. It can't be used as evidence, but -- as he likes to remind me -- that doesn't mean it can't help. Mateo pulls out a burner phone and dials the tip line.

MATEO: (into phone) That trail you've been searching . . . there's an old cave up there, just past the stream. The opening can't be more than a few feet wide, small enough to cover with a boulder. . . Maybe take the dogs . . .

NARRATOR: As he hangs up, I know he's trying to figure out how to shape his line of questions and apply just the right pressures to make the suspect snap. To make him think that they've already found enough evidence. That they already know what he's done. He seems to forget I'm there until . . . (to Mateo) Sorry, Mateo, but I'm not feeling well.

MATEO: You're sure none of these are . . . ?

NARRATOR: I don't need to answer; he can tell from my expression. We've been through this so many times before. Not a single face on the sketch was the one that I've been searching for. Not a single one was Willa.

MATEO: Why don't you head home now? You've done so much already.

NARRATOR: I sit on the edge of my bed and watch the news as the reports come in. The outcome's happier this time: Two victims were found alive, now hospitalized for trauma and malnutrition. They show a photo of one, and my hand twitches, recalling the curves of her face, the gentle waterfall of her hair sketched out on my paper.

Reporters swarm Mateo as he descends the courthouse steps.

REPORTER 1: Does today's discovery change the prosecution's strategy?

REPORTER 2: Were you surprised at what the authorities found?

REPORTER 3: How'd you know to ask the suspect about that cave?

NARRATOR: He holds up a hand and walks through them, offering up no comment.

I click off the television and grab my paper and a pencil of gunmetal gray. This time, it's my own memories I reach for, which swirl in hazy circles around the room.

The stadium lights of my old high school football field casting a glow across the shadowy parking lot. The keys of my truck, glinting as I fumble with the driver's side door.

Willa, ten steps behind me, angry at me for making her leave before the final whistle. Her hands set on her hips in that all-too-familiar pose. Her chin, jutting out defiantly.

Me, yelling that -- fine! -- she could find her own ride home.

Then a shadowy figure, whose features I didn't recognize, approaching her as I watched through the rearview mirror. As I drove away and left her alone.

In my sketch, he's nothing but a silhouette of gray. A nameless, faceless smudge that could be anyone. But as I tear the page from the sketchbook and tuck it into my satchel, atop the hundreds of identical torn-out pages with identical smudges of lead, I swear to you, Willa, I'll find him. I won't stop sketching until I do.
```

---

## IC-2060: In Your Hat

- Title: In Your Hat
- Author (byline): Ellen Conford
- Work: Shelf Life: Stories by the Book, Pgs 11-21
- Publisher: Simon and Schuster
- Publication date as stated: Aug 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: DENNIS, ARIEL, MR. FRAZETTI
- Teaser before the introduction: No
- Spoken words (computed): 1302
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ellen Conford
Book: Shelf Life: Stories by the Book, Pgs 11-21
ISBN: 978-0689841804
Publisher: Simon and Schuster
Date (Month/Year): Aug 2003
```

### Introduction (context only: never use it for content warnings)

```text
High school is tough enough without being emotionally ambushed by a girl in a pink sweater wielding fake French literature. This is a tale of love, lies, and literary hoaxes in which Dennis, a chronic underachiever and wannabe Romeo, finally gets noticed by the elusive Ariel Greenbanks. Armed with nothing but panic, a dubious history of practical jokes, and a suspicious enthusiasm for hat-based tragedies, Dennis learns the hard way that you should never trust a girl who throws out ‘tuberculosis’ and ‘relevant’ in the same conversation. Madame de Maupassant by Emile Bovary may be fake news, but Dennis’s humiliation is very, very real.

In Your Hat by Ellen Conford
```

### Performance text (classify this)

```text
DENNIS: (Pg 11- 21) I was in the non-silent study area of the library on the last Sunday of midwinter break when Ariel Greenbanks noticed me. (Ariel enters and tosses her hair) I’d been trying to get Ariel to notice me for almost 2 years now, and the results had been grim to none. So, when she paused next to my chair, I seized the opportunity. (to Ariel) Hey, good lookin’. Come here often?

ARIEL: (picking up a couple of books from the table) As a matter of fact, yes. (looking at titles) Joseph Conrad? Jane Austen?

DENNIS: Well, uh . . . (to audience) I hesitated. She was seeing a side of me she’d never seen before, which wasn’t surprising, since I don’t have that side. She liked the Mensa type. But you can’t base a relationship on lies. I couldn’t pretend I was an intellectual giant. (to Ariel) Actually, I’m in kind of a crisis here. An emergency book report.

ARIEL: Oh. When is it due?

DENNIS: (sighing heavily) Tomorrow.

ARIEL: Tomorrow. That is an emergency. Well, which one of these did you read?

DENNIS: I haven’t exactly gotten to the reading stage yet. (to audience) I didn’t want to tell her that I had only gotten to the “which is the shortest book you can find?” stage. (shocked and elated) [But] Ariel Greenbanks, wearing a cute pink sweater, was talking to me! She slid into the chair next to mine and scooped some of the books toward her. She wanted to help me!

ARIEL: All of these are pretty short.

DENNIS: Short was the first requirement – and big print! (disapproving look from Ariel) I mean, because of the crisis. . . It’s not like I don’t like to read.

ARIEL: Maybe you could write about something you’ve already read. What was the last book you liked?

DENNIS: The Sponge People of Cyberia – [but] Mr. Frazetti has this prejudice against science fiction . . .

ARIEL: Have you read anything that isn’t science fiction?

DENNIS: The Microbe Hunters. But I can’t use that one. (to audience) After 4 years of handing in the same book report I’d written in 7th grade, the book report cops had finally caught up with me. Frankly, I don’t think teachers ought to trade information about their students. Isn’t that like a breach of doctor-patient confidentiality? (to Ariel, desperately) What am I going to do?

ARIEL: (smiling sympathetically) You’d better come to my house.

DENNIS: Her house! Alone with Ariel. With her! She and I. Her and me? Whatever. ***Scene change****

ARIEL: (scanning her bookcase) Darn it. I can’t find it. It was perfect. Short, but a minor classic. Mr. Frazetti would have been impressed. It was so great! About the millinery industry in France and this poor little woman who had all her hat designs stolen by an evil corporation. So vivid, so alive! I mean you could feel the hunger and the cold gnawing at you. (deep inhale) You could smell the slop in the Paris streets.

DENNIS: (inhales, with a cough, matching her excitement) I know what you mean!

ARIEL: And it’s so relevant. Even now. You could compare it to how today’s giant corporations swallow ups the little guy. C’est la vie.

DENNIS: (parroting) La vie (to audiene) A brief scowl flash[ed] across her brow. I hoped she hadn’t suddenly remembered the 26 pizzas I’d had delivered to her.

ARIEL: I really shouldn’t do this . . .

DENNIS: (eagerly) What shouldn’t you do? And will you do it??

ARIEL: I could tell you about the book . . .

DENNIS: (to audience) Had she finally realized we were destined to be together. Had she seen beyond the jokes and discovered the tormented soul beneath? The Me who could only express his love behind a mask of comedy?

ARIEL: (flirtatiously) Can you stay awhile? This will take some time . . .

DENNIS: (to audience) I went home with 5 pages of notes and headed for my computer. It wasn’t easy to concentrate with visions of Ariel dancing in my head. Her soft, pink sweater . . . [No!] I was supposed to be thinking of French hats and imagining the crude, clashing noises of the Parisian slums. It really was a good story. This poor French girl marries a real loser who gets drunk a lot and beats her, and finally dies when he gets run over by a thresher in the potato fields where he’s been trying to eke out a living by growing (of course) potatoes!

ARIEL: (takes over the story telling) She goes to Paris to support herself by making hats. It turns out she’s really talented!

DENNIS: Things are looking up for Madam de Maupassant.

ARIEL: Until she meets this high-class society guy. (named Guy, as a matter of fact) Only, he’s down on his luck too and really needs money to pay of his gambling debts.

DENNIS: But Madam de Maupassant doesn’t know any of that! She falls madly in love with him and he asks her to marry him.

ARIEL: But . . . on the day they’re supposed to be married. He disappears, taking all her original hat designs with him.

DENNIS: He sells her designs to (checks his notes) Le Chic Chapeau, a big hat company and runs off to Algeria and is never heard from again.

ARIEL: (dramatically) Madame de Maupassant is heartbroken, gets tuberculosis, and wastes away – a pitiful shadow of her former self.

DENNIS: She doesn’t even have money for a bowl of soup, let alone medicine. Finally, just as she takes her dying breath, there’s a knock at the door. One of her old customers wants her to design all the hats for her daughter’s wedding.

ARIEL: (dramatically) But it’s too late. [She] can barely whisper . . “Entrez” when she gasps (gasps) and dies.

DENNIS: I’m telling you it was a terrific story! I was sniffling a little as I wrote out the plot. (proudly) AND I made a comparison between Madame de Maupassant and the economics of today. How the book was still relevant even though it was written 120 years ago. I printed out my report and was asleep before midnight . . . to dream of Ariel, in pink, trying on hats. Big flowery, poufy, old-fashioned hats!

ARIEL: (with a French accent) But of course I care what you think, Dennis. I want to look pretty for you.

DENNIS: On Monday I handed in my book report and spent the next two days trying to thank Ariel. I wanted to buy her lunch on Tuesday.

ARIEL: (disdainfully, motioning to her tray) I have lunch already.

DENNIS: On Wednesday I asked if she’d go to the library with me. I had an urge to read Madame de Maupassant. Ariel had made it sound so good. Plus, in case Mr. Frazetti asked me any questions about it I’d be ready for him.

ARIEL: (shaking her head) Band practice . . . (flounces off)

DENNIS: On Thursday Mr. Frazetti handed our book reports back. I sat straight and proud at my desk, waiting for my A, picturing the kiss Ariel would give me when I showed her my report. (puckers up at the thought) Usually I was in no hurry to get my assignments back. But today was different!

MR. FRAZETTI: (thrusting the report toward Dennis) Really, Mr. Murphy.

DENNIS: (looking down at his paper) Madam de Maupassant by Emile Bovary . . . F!! Underneath he’d written . . .

MR. FRAZETTI: (indignant) F as in FAKE!! Do you think I’m an idiot??

DENNIS: I couldn’t have been more stunned if I’d been captured by the Sponge People of Cyberia. How could he possibly know that I hadn’t really read the book? How could he know that Ariel had told me the story? Did she get the plot wrong? (leafing through the paper to the last page) At the bottom Mr. Frazetti had written . . .

MR. FRAZETTI: There will be no Makeup for this assignment. You have made up enough already!

DENNIS: (covering his eyes, dramatically) Despair and confusion overwhelmed me. Just as Le Chic Chapeau had overwhelmed Madame de Maupassant. (dramatic pause) I cornered Ariel near the parking lot exit. She was with two other girls who started giggling the moment they saw me. (to Ariel, pulling out his report) Look at this! Look at this!

ARIEL: (innocently) Oh, my. An F. That’s not good.

DENNIS: (livid) Not good? It’s terrible! Why did I get an F?

ARIEL: Well, maybe because I made it up.

DENNIS: Made it up? Made what up? What are you talking about?!

ARIEL: (with a sweet devious smile) The thing is, there really is no such book as Madame de Maupassant. I made it up. The whole story.

DENNIS: (stammering) No such book? But – but – (wailing) but why????

ARIEL: (laughing) It was a joke, Dennis. Just a little joke. (turns to leave)

DENNIS: It’s not funny! Ariel!!!!

ARIEL: (turns and tilts her head) You don’t think so?

DENNIS: (shouting) No! You really got me in trouble!

ARIEL: (hands on her hips, shaking her head) For heaven’s sake, Dennis. (with a French accent) What’s happened to your sense of humor? (exits)

DENNIS: (yelling to Ariel’s back) My great sense of humor AND my legendary reputation for practical jokes! You can’t base a relationship on lies!

ARIEL: C’est la vie!
```

---

## IC-2061: Incarnations of Burned Children

- Title: Incarnations of Burned Children
- Author (byline): David Wallace
- Work: Oblivion
- Publisher: Little, Brown & Company
- Publication date as stated: June 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1126
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Wallace
Book: Oblivion
ISBN: 978-0316919814
Publisher: Little, Brown & Company
Date (Month/Year): June 2004
```

### Introduction (context only: never use it for content warnings)

```text
The most common cause of burns is not matches and not stoves. It isn't even fire. Hot liquids are the most common cause of burns in small children, experts say. On average, 175 children a year are scalded badly enough to be admitted to the hospital. David Wallace pays tribute to these small victims in his recreation of the events leading up to a most devastating accident in Incarnations of Burned Children.
```

### Performance text (classify this)

```text
The Daddy was around the side of the house hanging a door for the tenant when he heard the child's screams and the Mommy's voice gone high between them. He could move fast, and the back porch gave onto the kitchen, and before the screen door had banged shut behind him the Daddy had taken the scene in whole, the overturned pot on the floortile before the stove and the burner's blue jet and the floor's pool of water still steaming as its many arms extended, the toddler in his baggy diaper standing rigid with steam coming off his hair and his chest and shoulders scarlet and his eyes rolled up and mouth open very wide and seeming somehow separate from the sounds that issued, the Mommy down on one knee with the dishrag dabbing pointlessly at him and matching the screams with cries of her own, hysterical so she was almost frozen.

Her one knee and the bare little soft feet were still in the steaming pool, and the Daddy's first act was to take the child under the arms and lift him away from it and take him to the sink, where he threw out plates and struck the tap to let cold wellwater run over the boy's feet while with his cupped hand he gathered and poured or flung more cold water over his head and shoulders and chest, wanting first to see the steam stop coming off him, the Mommy over his shoulder invoking God until he sent her for towels and gauze if they had it, the Daddy moving quickly and well and his man's mind empty of everything but purpose, not yet aware of how smoothly he moved or that he'd ceased to hear the high screams because to hear them would freeze him and make impossible what had to be done to help his child, whose screams were regular as breath and went on so long they'd become already a thing in the kitchen, something else to move quickly around.

The tenant side's door outside hung half off its top hinge and moved slightly in the wind, and a bird in the oak across the driveway appeared to observe the door with a cocked head as the cries still came from inside. The worst scalds seemed to be the right arm and shoulder, the chest and stomach's red was fading to pink under the cold water and his feet's soft soles weren't blistered that the Daddy could see, but the toddler still made little fists and screamed except now merely on reflex from fear the Daddy would know he thought possible later, small face distended and thready veins standing out at the temples and the Daddy kept saying he was here he was here, adrenaline ebbing and an anger at the Mommy for allowing this thing to happen just starting to gather in wisps at his mind's extreme rear still hours from expression.

When the Mommy returned he wasn't sure whether to wrap the child in a towel or not but he wet the towel down and did, swaddled him tight and lifted his baby out of the sink and set him on the kitchen table's edge to soothe him while the Mommy tried to check the feet's soles with one hand waving around in the area of her mouth and uttering objectless words while the Daddy bent in and was face to face with the child on the table's checkered edge repeating the fact that he was here and trying to calm the toddler's cries but still the child breathlessly screamed, a high pure shining sound that could stop his heart and his bitty lips and gums now tinged with the light blue of a low flame the Daddy thought, screaming as if almost still under the tilted pot in pain.

A minute, two like this that seemed much longer, with the Mommy at the Daddy's side talking sing-song at the child's face and the lark on the limb with its head to the side and the hinge going white in a line from the weight of the canted door until the first wisp of steam came lazy from under the wrapped towel's hem and the parents' eyes met and widened—the diaper, which when they opened the towel and leaned their little boy back on the checkered cloth and unfastened the softened tabs and tried to remove it resisted slightly with new high cries and was hot, their baby's diaper burned their hand and they saw where the real water'd fallen and pooled and been burning their baby all this time while he screamed for them to help him and they hadn't, hadn't thought and when they got it off and saw the state of what was there the Mommy said their God's first name and grabbed the table to keep her feet while the father turned away and threw a haymaker at the air of the kitchen and cursed both himself and the world for not the last time while his child might now have been sleeping if not for the rate of his breathing and the tiny stricken motions of his hands in the air above where he lay, hands the size of a grown man's thumb that had clutched the Daddy's thumb in the crib while he'd watched the Daddy's mouth move in song, his head cocked and seeming to see way past him into something his eyes made the Daddy lonesome for in a strange vague way.

If you've never wept and want to, have a child. Break your heart inside and something will a child is the twangy song the Daddy hears again as if the lady was almost there with him looking down at what they've done, though hours later what the Daddy won't most forgive is how badly he wanted a cigarette right then as they diapered the child as best they could in gauze and two crossed handtowels and the Daddy lifted him like a newborn with his skull in one palm and ran him out to the hot truck and burned custom rubber all the way to town and the clinic's ER with the tenant's door hanging open like that all day until the hinge gave but by then it was too late, when it wouldn't stop and they couldn't make it the child had learned to leave himself and watch the whole rest unfold from a point overhead, and whatever was lost never thenceforth mattered, and the child's body expanded and walked about and drew pay and lived its life untenanted, a thing among things, its self's soul so much vapor aloft, falling as rain and then rising, the sun up and down like a yoyo.
```

---

## IC-2062: It’s a Good Life

- Title: It’s a Good Life
- Author (byline): Jerome Bixby
- Work: The Science Fiction Hall of Fame, Volume 2
- Publisher: Tor Books
- Publication date as stated: December 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2105
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jerome Bixby
Book: The Science Fiction Hall of Fame, Volume 2
ISBN: 978-0765305343
Publisher: Tor Books
Date (Month/Year): December 2004
KS State Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
Anthony Fremont is six years old, with a cute little-boy face and blue, guileless eyes. But when those eyes look at you, you'd better start thinking happy thoughts, because the mind behind them is absolutely in charge. It’s a Good Life by Jerome Bixby
```

### Performance text (classify this)

```text
Aunt Amy was out on the front porch, rocking back and forth in the high-backed chair and fanning herself, when Bill Soames stopped in front of the house. Bill lifted the box of groceries out and came up the front walk.

Little Anthony was sitting on the lawn, playing with a rat. He had caught the rat down in the basement- -he had made it think that it smelled cheese, the most rich-smelling and crumbly-delicious cheese a rat had ever thought it smelled, and it had come out of its hole, and now Anthony had hold of it with his mind and was making it do tricks.

When the rat saw Bill Soames coming, it tried to run, but Anthony thought at it, and it turned a flip-flop on the grass, and lay trembling, its eyes gleaming in small black terror.

Bill Soames hurried past Anthony and reached the front steps, mumbling. He always mumbled when he came to the Fremont house. Everybody did. They tried to jumble up their thoughts to keep them skipping back and forth, so Anthony couldn't read their minds. The mumbling helped. Because if Anthony got anything strong out of your thoughts, he might take a notion to do something about it--like curing your wife's sick headaches or your kid's mumps. That was if he liked you. He might try to help you, in his way. And that could be pretty horrible.

If he didn't like you ... well, that could be worse.

Bill Soames set the box of groceries on the porch railing and stopped his mumbling long enough to say, "Everythin' you wanted, Miss Amy."

"Oh, fine, William," Amy Fremont said lightly. "My, ain't it terrible hot today?"

Bill Soames almost cringed. His eyes pleaded with her. He shook his head violently no, and then interrupted his mumbling again, though obviously he didn't want to: “Oh, don't say that, Miss Amy ... it's fine, just fine. A real good day!"

"Land alive, William," Aunt Amy said, "you don't have to mumble like that. Anthony wouldn't hurt you. My goodness, Anthony likes you!" She raised her voice and called to Anthony, who had tired of the rat and was making it eat itself. "Don't you, dear? Don't you like Mr. Soames?"

Anthony looked across the lawn at the grocery man--a bright, wet, purple gaze. He didn't say anything. After a second Anthony returned his attention to the rat. It had already devoured its tail, or at least chewed it off--for Anthony had made it bite faster than it could swallow.

Mumbling silently, thinking of nothing in particular as hard as he could, Bill Soames went stiff-legged down the walk, mounted his bicycle and pedaled off.

"We'll see you tonight, William," Aunt Amy called after him.

Anthony looked at the rat. It had devoured half its belly, and had died from pain. He thought it into a grave out deep in the cornfield--his father had once said, smiling, that he might do that with the things he killed--

Amy went out in back, where Anthony's Mom-- Aunt Amy's sister--sat in the shade of the house, shelling peas.

"William brought the groceries," Aunt Amy said.

"Oh, good," said Mom.

Everybody in Peaksville always said "Oh, fine," or "Good," or "Say, that's swell," when almost everything happened or was mentioned--even unhappy things like accidents or even deaths. They'd always say "Good," because if they didn't try to cover up how they really felt, Anthony might overhear with his mind, and then nobody knew what might happen.

"Tonight's television night," said Aunt Amy. "I'm glad I look forward to it so much every week. I wonder what we'll see tonight?"

"Dan Hollis will be so surprised when he finds out that tonight's television party is a birthday party for him too!"

Anthony liked television night. Everybody came to television and he liked all the attention he got when they did.

Anthony's father came home around six-thirty. "No one told Dan Hollis about its being a birthday party, did they?" his wife asked.

"It's good," said Dad, in the loud, familiar, wanting-to-be-overheard tone of voice. Everything's good. Everything has to be good . . Had to be fine just as it was, even if it wasn't. Always. Because any changes might be worse. So terribly much worse.

They started arriving around eight o clock.. The candles were burning, and the chairs situated, and Dad had a big fire going in the fireplace.

The first to arrive were the Sipichs, John and Mary. John wore his best suit, and was well-scrubbed and pink-faced after his day in McIntyre's pasture. The suit was neatly pressed, but getting threadbare at elbows and cuffs. Old McIntyre was working on a loom, designing it out of schoolbooks, but so far it was slow going.

McIntyre had been one of the ones who, at first, had wanted to try to get Anthony to make things the villagers needed, like clothes and canned goods and medical supplies and gasoline. Since then, he felt that what had happened to the whole Terrance family and Joe Kinney was his fault, and he worked hard trying to make it up to the rest of them. And since then, no one had tried to get Anthony to do anything.

The next arrivals were the Smiths and the Dunns, who lived right next to each other down the road, only a few yards from the nothingness. They drove up in the Smiths wagon, drawn by their old horse.

Then the Reillys showed up, from across the darkened wheat field, and the evening really began. Pat Reilly sat down at the big upright in the front room, and began to play from the popular sheet music on the rack. He played softly, as expressively as he could--and nobody sang. Anthony liked piano playing a whole lot, but not singing; the one time somebody had started to sing, Anthony had looked over from the top of the piano and done something that made everybody afraid of singing from then on.

So, every television night, Pat would play the piano, and that was the beginning of the evening. Wherever Anthony was, the music would make him happy, and put him in a good mood, and he would know that they were gathering for television and waiting for him.

Dan and Ethel Hollis came late, and Dan walked in not suspecting a thing. "Well, I'll be darned," Dan grinned. "This is swell. I wasn't expecting this at all ... gosh, this is swell!"

They gave him his presents--mostly things they had made by hand, though some were things that people had possessed as their own and now gave him as his. \

Last of all, Thelma Dunn gave Dan Hollis a record she had found. Dan's eyes misted even before he opened the package. He knew it was a record.

"Oh, gosh," Dan said again. Carefully he removed the wrapping and stood there fondling the record, running his big hands over the worn grooves with their tiny, dulling crosswise scratches. He looked around the room, eyes shining, and they all smiled back, knowing how delighted he was.

"Happy birthday, darling!" Ethel said, throwing her arms around him and kissing him.

"Look ... do you think we could play it? Lord, what I'd give to hear some new music ... just the first part, the orchestra part, before Como sings?"

Faces sobered. After a minute, John Sipich said, "I don't think we'd better, Dan. After all, we don't know just where the singer comes in it'd be taking too much of a chance. Better wait till you get home."

It was a pleasant enough get-together, aside from your having to watch what you said just as carefully as you always did everyplace. If a dangerous thought came into your mind, you just started mumbling, even right in the middle of a sentence. When you did that, the others just ignored you until you felt happier again and stopped.

Anthony liked television night. He had done only two or three awful things on television night in the whole past year.

Mom had put a bottle of brandy on the table, and they each had a tiny glass of it. Afterward, everybody wished that the brandy hadn't been brought out because Dan Hollis drank more of it than he should have, and mixed it with a lot of the homemade wine. Dan Hollis got high, and did a fool thing., Dan stopped laughing right in the middle of the story. His face got slack, and then it got ugly, and he said, "Oh, Christ!"

Immediately the room was still. Pat Reilly had been playing the piano, softly. He stopped, his hands poised over the yellowed keys. "Keep playing, Pat," Anthony's father said softly.

Dan stood in the middle of the room, holding the record. In his other hand he held a glass of brandy so hard his hand shook. "Christ," he said again, and he made it sound like a dirty word.

John Sipich moved forward. "Now, Dan ... it's good for you to talk that way. But you don't want to talk too much, you know."

"Can't even play my record," he said loudly. He threw the glassful of brandy against the wall. It splattered and ran down the wallpaper in streaks.

Pat Reilly was playing louder, to cover up the sounds of the talk. It wouldn't do any good, though, if Anthony was listening.

Dan Hollis went over to the piano and stood by Pat's shoulder, swaying a little. "Pat," he said. "Don't play that. Play this." And he began to sing. Softly, hoarsely, miserably: "Happy birthday to me... Happy birthday to me..."

"Dan!" Ethel Hollis screamed. She tried to run across the room to him. "Dan, stop-"

"--Happy birthday, dear Danny." Dan sang. "Happy birthday to me!" Dan Hollis stared over at the dining-room door. At Anthony's mother, "You had him," he said.

Tears gleamed on his cheeks as the candlelight caught them. "You had to go and have him ..."

Anthony came into the room. Pat stopped playing. He froze. Everybody froze. Dan's voice faltered into silence. His eyes widened.

"Bad man," Anthony said, and thought Dan Hollis into something like nothing anyone would have believed possible, and then he thought the thing into a grave deep, deep in the cornfield.

Anthony's purple gaze went around the room. Some of the people began mumbling. They all tried to smile.

"A good thing," said Anthony's father, smiling. He'd had more practice in smiling than most of them. "A wonderful thing."

"It's swell.., just swell," said Pat Reilly, tears leaking from eyes and nose, and he began to play the piano again, softly. Anthony climbed up on top of the piano, and Pat played for two hours.

Afterward, they watched television. They didn't even turn the set on. It wouldn't have worked anyway, there being no electricity in Peaksville. They just sat silently, and watched the twisting, writhing shapes on the screen, and listened to the sounds that came out of the speaker, and none of them had any idea of what it was all about. They never did. It was always the same.

"It's real nice," Aunt Amy said once, "But I liked it a little better when there were cities outside and we could get real-"

"Why, Amy!" said Mom. "It's good for you to say such a thing. Very good. But how can you mean it? Why, this television is much better than anything we ever used to get!"

“Yes," chimed in John Sipich. "It's fine. It's the best show we've ever seen!"

He sat on the couch, with two other men, holding Ethel Hollis flat against the cushions, holding her arms and legs and putting their hands over her mouth, so she couldn't start screaming again . . .

It did no good to wonder where they were ... no good at all. Peaksville was just someplace. Someplace away from the world. It was wherever it had been since that day three years ago when Anthony had crept from her womb and old Doc Bates--God rest him--had screamed and dropped him and tried to kill him, and Anthony had whined and done the thing. He had taken the village someplace. Or had destroyed the world and left only the village, nobody knew which. It did no good to wonder about it. Nothing at all did any good except to live as they must live. Must always, always live, if Anthony would let them. It was a good day.
```

---

## IC-2063: It’s Not a Sport

- Title: It’s Not a Sport
- Author (byline): George Carlin
- Work: Napalm & Silly Putty, Pg 106-109
- Publisher: Hyperion
- Publication date as stated: April 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SPEAKER
- Teaser before the introduction: Yes
- Spoken words (computed): 785
- Already set (do not supply): none

### Source block (context only)

```text
Author: George Carlin
Book: Napalm & Silly Putty, Pg 106-109
ISBN: 978-0786864133
Publisher: Hyperion
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
Golf would be much more interesting and exciting if they had goalies. . . Seriously, just think about it. . . In virtually every sport you have an opponent whose sole purpose in life is to keep you from achieving your goal. . . What’s the challenge in golf? Heck, at least train a couple of gerbils to guard each hole. As a matter of fact, there’s probably a multitude of alleged sports that in reality, any jury in its right mind would conclude . . .

It’s Not a Sport by George Carlin
```

### Performance text (classify this)

```text
SPEAKER: (Pg 106-109) To my way of thinking there are really only three sports: baseball, basketball, and football. Everything else is either a game or an activity.

SPEAKER: Hockey comes to mind. People think hockey is a sport. It's not. Hockey is three activities taking place at the same time: ice skating, fooling around with a puck, and beating the crap out of somebody. If these guys had more brains then teeth, they'd do these things one at a time. First go ice-skating, then fool around with a

puck, then you go to the bar and beat the crap out of somebody. The day would last longer, and these guys would have a lot more fun. Another reason why hockey isn't a sport is that it's not played with a ball. Anything not played with a ball can't be a sport. These are my rules, I make 'em up.

Soccer. Soccer is not a sport because you can't use your arms. Anything where you can't use your arms can't be a sport. Tap dancing isn't a sport. I rest my case.

Running. People think running is a sport. Running isn't a sport because anybody can do it. I can run, you can run.

For Christ sakes, my mother can run! You don't see her on the cover of Sports Illustrated, do you?

Swimming. Swimming isn't a sport. Swimming is a way to keep from drowning. That's just common sense.

Sailing isn't a sport. Sailing is a way to get somewhere.

Riding the bus isn't a sport, why should sailing be a sport?

Boxing is not a sport either. Boxing is a way to beat the crap out of somebody. In that respect, boxing is actually a more sophisticated way of hockey. In spite of what the police tell you, beating the crap out of somebody is not a sport. When police brutality becomes an Olympic event, fine, then boxing can be a sport.

Bowling. Bowling isn't a sport because you have to rent shoes. Don't forget, these are my rules. I make 'em up.

Billiards. Some people think billiards is a sport, but it can't be, because there's no chance of serious injury. Unless, of course, you welch on a bet in a tough neighborhood. Then, if you wind up with a pool cue stickin' out of your ear, you know you might be the victim of a sports-related injury. But that ain't billiards, that's pool, and that starts with a P, and that rhymes with D, and that brings me to darts.

Darts could have been a sport, because at least there's a chance to put someone's eye out. But, alas, darts will never be a sport, because the whole object of the game is to reach zero, which goes against all sports logic.

Lacrosse is not a sport; lacrosse is a college activity. I don't care how rough it is, anytime you're running around a field, waving a stick with a little net on the end of it, you're engaged in a college activity. Period.

Field hockey and fencing. Same thing. Also these activities aren't sports, because you can't gamble on them. Anything you can't gamble on can't be a sport. When was the last time you made a fencing bet?

Gymnastics is not a sport because Romanians are good at it. It took me a long time to come up with that rule, but, I did it.

Polo isn't a sport. Polo is golf on horseback. Without holes. It's a great concept, but not a sport. And as far as water polo is concerned, I hesitate to even mention it, because it's extremely cruel to horses.

Which brings me to hunting. You think hunting is a sport? Ask the deer. The only good thing about hunting is the many fatal accidents on the weekends. And, of course, the permanently disfigured hunters who survive such accidents.

Then you have tennis. Tennis is very trendy and very fruity, but it's not a sport. It's just a way to meet other trendy fruits. Technically, tennis is an advanced form a Ping-Pong. In fact, tennis is Ping-Pong played while standing on the table. Great concept, not a sport.

In fact, all racket games are nothing more than derivatives of Ping-Pong. Even volleyball is, technically, racketless, team Ping-Pong played with an inflated ball and raised net while standing on the table.

And finally welcome to golf. Let it just be said golf is a game that might possibly be fun, if it could be played alone. But it's the vacuous, striving, superficial, male-bonding joiners one has to associate with that makes it such a repulsive pastime. And it is decidedly not a sport.

Period.
```

---

## IC-2064: Jack and the Beanstalk

- Title: Jack and the Beanstalk
- Author (byline): AJ Jacobs
- Work: Fractured Fairy Tales
- Publisher: Bantam Books
- Publication date as stated: Jan 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 857
- Already set (do not supply): none

### Source block (context only)

```text
Author: AJ Jacobs
Book: Fractured Fairy Tales
ISBN: 978-0553099805
Publisher: Bantam Books
Date(Month/Year): Jan 1999
```

### Introduction (context only: never use it for content warnings)

```text
In the original version of Jack and the Beanstalk, Jack, a poor country boy, trades the family cow for a handful of magic beans, which grow into an enormous beanstalk reaching up into the clouds. Jack climbs the beanstalk and finds himself in the castle of an unfriendly giant. The giant senses Jack's presence and cries, “Fee, fie, fo, fum, I smell the blood of an Englishman!” Outwitting the giant, Jack is able to retrieve many goods once stolen from his family, including an enchanted goose that lays golden eggs. Nice, quaint, uninspired. . . . but what if . . . . what if . . . . Jack had used those beans for a more, shall we say, athletic endeavor? Jack and the Beanstalk by AJ Jacobs
```

### Performance text (classify this)

```text
Once upon a time-actually, it was 1888, but this isn't a history textbook, you know, so we don't have to get all boring and technical. Once upon a time, there was a young lad named Jack. Jack had come to the big city to tryout for a baseball team, the Boston Beavers. The Beavers were a great team, managed by that legendary figure, Big Lip Leo. Listen as Leo gives one of those legendary pep talks.

"Men, we got a great ball club here. There's only one little thing that keeps us from being the top team in the country. . . We've never won a game."

True, the Beavers had lost 597 consecutive games. But then again, they had never had Jack on the team. Now, Jack wasn't exactly your garden-variety baseball player. He didn't chew tobacco. He didn't scratch himself in embarrassing places. He didn't show up for "Yell at the Umpire" practice. And strangest of all, he had never played baseball before and knew not a single thing about the game.

"Hey coach," he would shout. "When do I get to make a touchdown?"

"No," the coach yelled. "Just run, run!"

"Ummmm. Where would you like me to run?"

It didn't look good. But hard as it is to believe, Jack wasn't as dumb as he sounded and looked. He had an ace up his sleeve, an ace he got to show at the season opener. The Beavers went up against the Poughkeepsie Pirates, who would probably play better if they stopped wearing those eye patches and drinking rum. Anyway, it was the bottom of the ninth, the Beavers led 4 to 3 and needed just one more out before they won the game.

The Pirates' best player stepped up to the plate-or, actually, limped up to the plate, as he had a peg leg. The pitch, and crack! The ball sailed high over center field.

"What a hit!" shouted the announcer. 'That ball is going, going. Hey, what's this?"

For at that moment, Jack pulled a magic bean out of his pocket, planted it in center field, watered it, and jumped on top of it. Rumble, roar, and whoosh! Jack was carried skyward on a huge beanstalk that grew straight up into the air. That fly ball landed smack in his mitt.

"Yerrrrr out!" shouted the umpire.

The fans went wild. The Boston Beavers had fi-nally won a game. Of course, some of the Pirates weren't all that overjoyed and began showing the Beavers some extreme close-ups of their knuckles and cleats. But the rule books said nothing about banning beans. So the decision stood.

In the weeks that followed, the team won game after game with the help of Jack and his magic beans. In fact, Leo changed the team's name to the Boston Beans. The guys in the stands started selling beans along with franks. And Jack became a national celebrity, getting his picture on the front of People magazine, Sports Illustrated, and Legumes Weekly. ("Bean There, Done That!" read the cover.)

Then came the big day for the final game of the season-the Beans were to play the Giants. It's no coincidence they were called the Giants. You could install observation decks on their foreheads and charge five bucks for entrance. It was going to be a rough game.

"Why couldn't we play the Plattsville Midgets?" whined Leo. "Or the Nantucket Napoleons? Or even the San Diego Men of Average Height?"

But the Giants it was. And right from the start, it was a fight to the finish. The Giants smashed ball after ball over center field, but Jack always managed to zoom up on his beanstalk and catch them on the fly.

Both teams gave it their all, and the scores shot higher and higher. Finally, at the bottom of the ninth, it was all tied up, 66 to 66. The Giants had the bases loaded, and Whitie Goober, their best hitter, came to the plate.

Whoosh! He let the first pitch go by. Whoosh! He let the second pitch go by. Two strikes on him. On this last pitch, Jack reasoned, Whitie would swing for the fences! Figuring he should prepare, Jack planted three beans, hopped on top, and shot up into the sky on the biggest beanstalk of all.

"Take that, Mighty Whitieeeeeeeeee!" he yelled.

But Mighty Whitie, instead of slamming the ball, just gave it a dainty tap, and it dribbled out into center field. Jack was too high to do anything. Two players scored and the Giants won.

"I goooooooooofed!" yelled Jack.

But no one could hear him. That big beanstalk carried him straight up into the sky for hundreds of miles until it finally poked through a strange cloud where Jack saw a huge castle and heard these mysterious, booming words: "Fee, Fi, Foe, Fum! I smell the blood of an Englishman!"

Now if Jack were an Englishman, he'd be playing cricket, not baseball. But he had no time to make that correction. He had to deal with more pressing problems-namely some extremely large molars about to give him a chewing out. But that's another story.
```

---

## IC-2065: The Jealous Sun and His Beloved Moon

- Title: The Jealous Sun and His Beloved Moon
- Author (byline): Folk tale from Papua New Guinea -
- Work: Pacific Island Legends
- Publisher: Bess Press, Inc.
- Publication date as stated: August 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 861
- Already set (do not supply): none

### Source block (context only)

```text
Author: Beret E. Strong (editor, et al)
Book: Pacific Island Legends
ISBN: 978-1573060844
Publisher: Bess Press, Inc.
Date (Month/Year): August 1999
```

### Introduction (context only: never use it for content warnings)

```text
Storytelling is common to every culture. Most people enjoy listening to stories. Storytellers have catered for the need for a 'good story' since the beginning of civilization. A folktale is a popular story that was passed on in spoken form, from one generation to the next. Usually the author is unknown and there are often many versions of the tale. The Jealous Sun and His Beloved Moon is a folktale that originated in Paupa New Guinea and is often used to explain why some members of this varied culture refuse to look too long at the moon.
```

### Performance text (classify this)

```text
Anonymous

While walking in the forest one day, Aruako discovered a beautiful girl alone in a pond, taking her bath. Her grass skirt lay folded near the pond’s edge. He sat down on it to watch her. Her lovely wet skin shimmered in the sunlight. Underneath the pond’s clear surface, her body moved as gracefully as a mermaid’s.

She looked like a woman, but she was actually the spirit of the moon.

The moon woman spied Aruako sitting on the bank. “I remember you,” she said. “You dug me like a root from the side of my mother earth.” Then she threw back her head and laughed! “You poor thing, burning with desire! You want to marry me. But I warn you – you will die! I am a spirit and you are a man. We can never marry.”

Aruako listened but paid no attention to her words. They were as light as butterfly wings on his cheeks. He was enchanted by her radiant beauty. How she glowed with light!

The moon maiden watched Aruako watching her. “I know what you’re thinking,” she said. “This pond is filled with magic. I come here each day to wash myself and restore my brightness. You had better get those reckless thoughts out of your head, you foolish man. I am betrothed to the sun. Only he can marry me.” She stared at him with her dark, liquid eyes.

“Wait,” pleaded Aruako. “Listen to me. I unearthed you. I found you and set you free. You are so beautiful. Surely you belong to me. I will marry you.”

He took her by the hand and led her deep into the forest. At first she tugged against his hand. She knew she shouldn’t go. But he was gentle and his eyes shone with joy when he looked at her. Step by step they walked on.

He had a house in the deepest part of the forest. He led the moon spirit inside. Slowly, slowly, he began to stroke her long, shiny hair. The moon maiden sighed deeply. She laid her head on his shoulder. Gently he stroked her back. Gently she returned his caresses. For this night, she was his. They slept side by side, breathing in rhythm. The stars pulsed brightly in the sky, while the moon slept with her human lover. The night was calm, as if even the breeze had gone to bed. Everywhere creatures slept in peace.

But then the sun began to rise in the east, already boiling with rage.

When Aruako opened his yes, he shivered. Then he remembered. The moon maiden! He reached across the sleeping mat, but her warmth and smooth skin were gone. The lovely spirit of the moon had left him. He ran through the forest calling her name. He dove into the pond and searched among the rocks at the bottom. Nowhere could he find her.

The sun grew fiery, pouring his hot anger onto Aruako. Soon Aruako was dizzy with the heat. Staggering, he fainted. Then he woke up and began to crawl on his hands and knees toward his village. The earth seemed to well up as if it had turned into sea swells. The heavy hot air almost suffocated him.

Two boys found him collapsed upon the path to the village. He was barely breathing. They ran to tell the villagers.

Aruako’s skin was pale and dry. His eyes rolled back in his head. “He’s terribly sick,” said a woman. “Bitten by an adder snake, he was. No one survives that. Or maybe he has sun sickness.”

“Lift him,” commanded the chief’s son. “Carry him home.”

“Do what you can for him,” the chief told Aruako’s family. They prepared cool compresses of water-soaked leaves. They brought him food and water, but he was too sick to eat or drink. He lay nearly lifeless in the shade. His eyes fluttered open. He tried to swallow sips of water. Girls fanned him with palm fronds. His mother and sisters sat near and sang healing chants softly near his ears.

But the sun rose ever higher and hotter in the sky. Light sneaked under the palm-leaf fans, burning Aruako’s skin. His skin blistered and bubbled and then turned black and dry as charcoal in a dead fire. The tears in his eyes dried up. His tongue swelled and filled his mouth.

“Feel him,” said his mother to her sisters, looking fearfully up at the sun. “He is boiling inside. The sun plan to kill him. See how it sneaks under our fans and destroys the shade!” All day poor Aruako lay there, sicker and sicker, weaker and weaker.

Finally, the sun was satisfied. It sank down to the western horizon and slipped over the edge of the world. The moon with her gentle glow ucovered her lovely face. But it was too late for Aruako. Just as the moon peered lovingly down at him, he died. Today the people of his village turn their faces away from the moon. They remember the jealousy of the sun. They will not risk his wrath by gazing too long on the face of his beloved moon.
```

---

## IC-2066: Jill and the Beanstalk

- Title: Jill and the Beanstalk
- Author (byline): Denise Vega
- Work: Newfangled Fairy Tales (ed B Lansky)
- Publisher: Meadowbrook Press
- Publication date as stated: Jan 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1531
- Already set (do not supply): none

### Source block (context only)

```text
Author: Denise Vega
Book: Newfangled Fairy Tales (ed B Lansky)
ISBN: 978-0671577049
Publisher: Meadowbrook Press
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Now, finally, at last - those old fairy tales have been exposed for the drivel they are! Did you ever stop to think that Sleeping Beauty might have been neutralized because she was a miserable young woman? Or that Goldilocks wore red because her mother got a great deal on a bolt of red cloth? Or perhaps, the giants in Jack and the Beanstalk weren’t so bad after all . . . . compared to the poverty and neglect that plagued Jack and his mother. And come to think of it; why does it have to be Jack . . . How about Jill and the Beanstalk? by Denise Vega.
```

### Performance text (classify this)

```text
Jill was out walking to school one morning. Her mother had given her $15 that she was supposed to give to her teacher. It was a fee for art class.

As Jill was happily skipping along, a friendly looking man stepped out of an alley, and Jill, not seeing him, skipped right into him.

"UMPHH" Was all he said at first.

Jill jumped back, dropping her money. "OH! I'm sorry," she exclaimed.

"Quite ok," replied the man, as he picked up the money and handed it back to her. "That's quite a bit of lunch money," he said, eyeing the money.

"That's not my lunch money!" Jill giggled. "That's for art class!"

"Oh I see..." the man answered her. ”Do you like art?"

Jill nodded.

"Well," said the man, "I just happen to have these....magic beans, yeah that's what they are....magic beans, and if you plant them in the ground, a huge stalk will grow up and at the top of it you will find a land filled with all kinds of art!"

Jill's eyes were wide with amazement. "Are you gonna plant them?" She asked the man.

"Well, I have no ground to put them in," the man tried to sound sad here. "Someone gave them to me for my last $15, and then I had nowhere to plant them." He looked at Jill. She appeared to be swallowing it. "If only someone who could plant them would buy them..."

Jill looked down at her money. "Here," she said. "I wanna buy them!"

"Well, if you're sure," said the man, as he quickly snatched the money before she could change her mind. He reached into his pocket and pulled out a small leather bag with five smooth beans and gave it to her. The real origin of the beans was a small shop he had broken into downtown. There wasn't much of any value in it, or so it seemed, but he figured he could make up wild stories about the stuff and sell it to unsuspecting kids. He was a con man.

The man walked away muttering a few things quietly. "What's 'gullible' mean?" thought Jill. Shrugging her shoulders, she skipped the rest of the way to school.

When she got home, her mommy was waiting for her.

"What did you do with the money I gave you?" she asked. "Your teacher called and said you didn't give her your art fee."

Jill showed her the beans, telling her the story the man had told her. But instead of being excited about it, her mommy was very upset with her. She took the bag of beans and sent Jill to her room.

"Kids!" she exclaimed, slamming the bag down on the desk. As she did this, three of the beans flew out of the bag from the force, and flew right out the open window nearby.

Jill thought she heard strange sounds that night. Her bedroom just happened to be right above where the beans landed. She got up and looked out the window; just in time to see a large bean sprout go right past her window. Jill was very excited. "Mommy must have changed her mind, and planted them after all!" she thought, excited.

Jill had always been like a little monkey, climbing anything she could. Whenever she was on the playground you would find her near the Jungle Gym. Carefully she slid over the window ledge and grabbed hold of the bean sprout. Once she had a good hold, she began to climb. She climbed and climbed, and climbed some more. Jill was beginning to think she would never reach the top...it seemed as though she had been climbing for hours. In fact when she looked down, she couldn't even see the ground anymore.

Finally she reached what appeared to be a hole in the sky. As she climbed through it, she got off the beanstalk. It continued on up further.

Now Jill looked around her. She seemed to be on the front door of a large house. The door seemed so large to her, but she reached up and knocked on it. The door opened, and a lady looked out after a minute, peering in both directions, then down. She scared Jill...she had never seen anyone so huge! Not that the woman was fat, in fact she was very fit, but she must have been over 15 feet tall!

When the woman looked down, she exclaimed, "Why, it's a little baby! Someone left us a little baby girl!"

Forgetting her fear for just a second, Jill's hot temper caused her to be indignant. "I am not a baby!" she said, stomping her foot. "I'm nearly nine!" The woman smiled at this childish display. "Not a baby, dear? But, then, why are you so small? I've seen two year olds bigger than you. And big girls don't do that..." she pointed at Jill's pants.

Jill looked down at herself. Oh No! She thought she had felt a warm sensation a moment ago! She had been so afraid when she saw the woman, that she had wet herself. Ashamed, Jill began to cry.

"Aww . . .there, there, everything will be ok" the woman consoled her, as she picked her up and carried her into the house.

They went through a kitchen and a few other rooms, up some stairs and down a hall. Jill saw a few other people in the house. They were all much bigger than she, but smaller than the woman carrying her.

"Hey, Mom, what's that?" she heard one of them call out.

The woman turned. "Not "What", Peter.... "Who". "Who is that?"

The one named Peter turned red. "Ok ok...WHO is that then?"

"This is a baby girl someone left by our door," she said. "Look at this, she's not even properly dressed as a baby. We'll take care of that. Her name is Jill."

Jill was still sniffling as they went through a door. Inside the room was a HUGE nursery. The woman took her through the nursery and into a room of the side of it, and Jill saw it had a bathtub in it. The woman filled the tub, and sat Jill on the floor and began to take Jill's clothes off.

Since she had not slept, and had climbed so long, Jill was very tired, and she let the woman do this to her. Then the woman put her in the tub, and gently washed her.

Jill was beginning to enjoy the comforting feelings this gave her. Before she knew what was happening, her thumb had found its way to her mouth, and she was contentedly sucking.

The woman smiled at her, cooed and talked baby talk as she bathed Jill. She reached out and tickled her, and was overjoyed when Jill giggled.

When she was finished washing her, the woman wrapped her in a towel and took her back to the nursery. Here she laid her on a changing table and dried her off. Jill realized the changing table would easily accommodate babies much bigger than herself. Then she cringed, realizing she had just thought of herself as a baby. She was also aware of a growing need. Why hadn't there been a toilet in that bathroom?

"Umm, Ma'am?" she said softly.

The woman smiled. "Why don't you call me Mommy?" she told Jill.

"Mommy, I have to go to the bathroom."

The woman laughed lightly. "Silly baby, babies don't use potties, and even if you could, which you already proved you can't, you couldn't reach the potties here."

Jill was still not getting it. "Well then how do they..." she began, then she saw the woman was unfolding something large and white. It was a huge diaper, quite big enough for Jill. The woman easily lifted her by the ankles and slid the diaper under her bottom. She also took time here to apply baby powder.

Jill experienced a whole realm of new feelings as the diaper was pulled up and snugly taped into place on her. She felt shame at first, but then realized this was better than wetting her pants as she had earlier. Besides, everyone here expected her to be diapered. She felt the warm and soft coziness of the diaper, and it felt safe and secure too. She decided this was not so bad after all. All the lost sleep was catching up to her now, and she was fading fast. The woman put a sleeper on her and carried her to a rocking chair, where she put her against her breast and began to rock her gently.

"Jill," she asked, "Those beans only work for very special people. People who are missing something. You are missing being a child, and so you must be one as long as it takes for you to get over that. Would you like to stay here and be my baby?"

Jill nodded her head. "Yes, Mommy, I would like that very much," she said, She accepted a bottle that was offered to her, and just as she drifted into sleep she felt a warm comfortable rush as she saturated her diapers.
```

---

## IC-2067: The Kentish Sleep Deprivation Journal

- Title: The Kentish Sleep Deprivation Journal
- Author (byline): Marshall Brickman
- Work: Not specified
- Publisher: HarperCollins Publishers, Inc
- Publication date as stated: 1974
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1351
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marshall Brickman
Book/Magazine: The New Yorker
Publisher: HarperCollins Publishers, Inc
Date (Month/Year): 1974
```

### Introduction (context only: never use it for content warnings)

```text
Sleep--along with its counterpart, being awake--accounts for much of the time spent by modern man during his life, and therefore merits serious attention by the trained observer. Certainly the most fascinating document to emerge from the burgeoning sleep-research field is the journal kept by Dr. Mordecai Kentish during a classic experiment in which he stayed awake for more than three hundred hours in order to study the effects of extensive sleep deprivation. The Kentish Sleep Deprivation Journal by Marshall Brickman.
```

### Performance text (classify this)

```text
Dr. Kentish, Winkle Professor of Clinical Psychology at Tony’s College, Chicago, won the Nobel Prize in 1948 for his work in isolating and defining the common nap as “any rest episode up to twenty minutes’ duration involving unconsciousness but not pajamas.” He also pioneered the “Kentish Technique” of psychoanalysis, in which either the patient or the therapist gets to lie on the couch, depending on which of the two is sleepier. He is the author of the standard text “Sleep” and the widely known treatise on insomnia, “How to Sleep,” plus a third volume, “Where to Sleep,” a thoughtful rating of motels found along the major interstate arteries, which includes an appendix listing inexpensive restaurants and the locations of important historical markers. We would like to express our thanks to Mabley Kentish for releasing the Kentish papers for publication only months after her brother’s experiments were so tragically interrupted, when he was carried off by a large bird. Selected portions of the Sleep Deprivation Journal follow. First Day (12 hours): Arrived at laboratory 9 p.m. Bucholtz [Kentish’s devoted assistant, O. Bucholtz, a refugee who worked for Kentish for twelve years without remuneration of any kind, and with only one two-day vacation, which he spent walking around in the front yard] as usual leaves a mess--candy wrappers, a banana peel on the EEG, a half-filled container of coffee with a cigarette butt floating in it. Nevertheless, there can be no question of dismissing him; he is pathetically devoted to me, perhaps because of that time I let him watch me shave. The current record for sleeplessness is held by radio personality Galen Moon, the host of a telephone show, who remained awake for the entire two hundred hours required to take an irate call from a severe stutterer. Moon, a noted insomniac, later revealed to me that even after his excruciating ordeal he could not fall asleep without first browsing through an article entitled, “Cairo--Wither the New Agrarianism?” a soporific published every Sunday in the magazine section of the New York Times. My intention is to exceed Moon’s limit by at least one-third, utilizing no stimulants or artificial means whatsoever--nothing but the awesome powers of a disciplined intellect. At the end of each entry, as daily proof of my ability to sustain rational, sequential thought, I shall perform a simple test, by writing out the complete alphabet. Thus:

abcdefghijklmnopqrstuvwxyz Second Day (38 hours): Pulse, respiration, temperature, and blood pressure normal. A mild elation accompanied by great mental clarity. Chess with Bucholtz; a carefully laid trap of my own design (Ruy Lopez, with a slashing bishop attack) had the fool mated in seven moves. Intake: Breakfast--coffee and a scone with honey. Lunch--Bibb lettuce rémoulade. Dinner--butterfish and a praline. Physical coordination excellent; I jumped two feet straight up into the air without bending my knees-- a difficult enough feat for a young man, and certainly remarkable for an advanced sedentary specimen such as myself. Wonderful feeling of crispness and efficiency. Three times eight is twenty-four. The cube root of eight is two. The capital of Chile is Santiago.

abcdefghijklmnopqrstuvwxyz

abcdefghijklmnopqrstuvwxyz Fifth Day (109 hours): Sensation of mild granulation around the eyeballs, as if a small boy had flung pulverized antimony into my face. Pulse, temperature, respiration, blood pressure normal. (Annoying relative term, “normal.” For whom?) In Bucholtz’s case, temperature, pressure, respiration, and blood pressure can all be expressed by one integer in the low fifties. Chess with Bucholtz. Irresponsibly sacrificed my queen, both knights, both bishops, and all pawns within the first thirteen moves; nevertheless managed to achieve stalemate by sending Bucholtz on a brief errand, during which time I flushed his king down the toilet. The frontiers of the mind are limitless. The cube root of eight is not two; it is something else, possibly the color red.

abcdefghijklmnopqrstuvwxyz Sixth Day (150 hours): No noticeable fatigue. Curious perceptual distortions, however. Everyday objects (i.e.; my right hand, a chair) seem either too large or too small, but I cannot decide which. Chess with Bucholtz discontinued when I realized after twenty minutes that we had set up the pieces without the board and were playing directly on the table. Intake: Breakfast--coffee, scone. Dinner--butterfish and a slice of whole-wheat bread. Read article by Karsky in International Journal of Orthopsychology, on jealousy in moths. Difficult to follow, as the entire text apparently consists of the word “vibescu” repeated endlessly. These behaviorists will stoop to any cheap trick merely to publish. I am on to Karsky, which explains why he never speaks to me even though we have never met and he lives in Omsk.

abcdefgz Eighth Day (182 hours): Curious feeling of constriction in the frontal lobe, as if someone had forced a tiny cast-iron opera hat onto my head with a wooden mallet. Today, for the first time in our long association, Bucholtz made a witty remark. When I asked him if there were any telephone messages for me, he replied, “No, the phone hasn’t rung all day.” (!) He is unbearably funny; the juxtaposition of “all day”--i.e.; the entire day- -with the notion of the telephone not ringing was, I thought, a masterful stroke of ironic hyperbole, worthy of Goethe and especially remarkable in someone who still needs help dressing. When I finally caught my breath, I requested that he close the door, which he did in a similarly comical fashion, putting his hand on the knob and pushing the entire structure until it latched. Again I broke into gales of laughter (it was marvelous, really), which Bucholtz mocked (also amusingly) by looking at me directly with both eyes! He is quite a jolly fellow, this Bucholtz.

a b 3 defg hijklmnop p ppp Ninth Day (231 hours): Intake: Breakfast--cofscone. The fork is the one with the little points on it; the spoon, however, is round. That is how you can tell them apart. Temperature erutarepmet. Window open 3½ inches, chair oriented along N-S magnetic lines of force, thus enabling me to draw energy from the earth and maintain a healthy, full head of hair. All else normal, except for Bucholtz’s plot to steal my face and sell it to the emperor. I have the persistent impression that a man named Al Bender possesses infinite knowledge, if we can only locate him and get him to talk. My brain remains miraculously alert. Some trouble, however, with the pancreas, which has been stealing catnaps. Thank God for the kidneys, which keep it awake with their constant bickering.

abz Ninth Day (234 hours): 4 a.m. Bucholtz asleep in the next room. The clock has just asked for a glass of water. Reasonable enough, but what is “water”? Increasing difficulty concentrating on simple tasks, such as snapping my luncheon peas across the room at Bucholtz. The dog outside has become a distraction, with its constant barking of “Iolanthe,” but when I try to call the authorities, the phone bursts into flame. What would Lysenko say about this? And to whom would he say it? I understand “vibescu” now; Karsky is clearly a genius. Dear, dear Karsky! Misunderstood, ridiculed, mocked. And to think I almost mailed him a spider! I must go to him. I need paper to build a boat.

a bee cee dee eff gee aitch I jay Twelfth Day (301 hours): Still no fatigue. Temperature 99°. Skies fair. Winds calm. Position 28°S by 188°W. The mate have eat of a tainted Gouda and muft be lafhed to the mizzen. Difpleasure on the foredeck, water maggoty. Three more given up to scurvey. May God help us in our tryalle...

At this point, the journal stops abruptly. Bucholtz, upon awakening, reported finding his mentor rigid, his forehead against the light switch, his body making a hypotenuse between floor and wall. His eyes were open and unblinking, his pulse 180, his temperature 50°F. Removed to the hospital, Kentish was given a strong sedative and put to sleep for a week, after which he awoke refreshed and ate an enormous breakfast, including two paper cups. His notes, bearing extensive tooth marks, were recovered by O. Bucholtz and presented to Mabley Kentish, who will publish them this fall in popular edition, under the title “Copping Zs--Forty Winks to Oblivion.”
```

---

## IC-2068: The Kid Nobody Could Handle

- Title: The Kid Nobody Could Handle
- Author (byline): Kurt Vonnegut
- Work: Welcome to the Monkey House, Pgs 270-283
- Publisher: Dial Press
- Publication date as stated: Jan 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, HELMHOLTZ, QUINN, JIM
- Teaser before the introduction: No
- Spoken words (computed): 1741
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kurt Vonnegut
Book: Welcome to the Monkey House, Pgs 270-283
ISBN: 978-0385333504
Publisher: Dial Press
Date (Month/Year): Jan 2006
```

### Introduction (context only: never use it for content warnings)

```text
Author Jodi Picoult wrote: Sometimes, all it takes to become human again is someone who can see you that way, no matter how you present on the surface . . .

The Kid Nobody Could Handle by Kurt Vonnegut
```

### Performance text (classify this)

```text
NARRATOR: (Pg 270-283) It was 7:30 in the morning. Inside a restaurant a very kind fat man with a headful of music looked down at the jiggling yolks of his breakfast eggs. George M. Helmholtz was director of the band of Lincoln High School and life had treated him well. Each year he dreamed the same big dream. He dreamed of leading as fine a band as there was on the face of the earth. And each year the dream came true. Youngsters played their hearts out for him.

Bert Quinn, the restaurant owner sat down in the booth with the bandmaster. He was a bachelor, a small, dark, humorless man. A fifteen-year-old boy with tough, stringy muscles standing out on his neck and forearms was mopping the aisle between booths. Childhood lingered in his features, but when he paused to rest, his fingers went hopefully to the beginnings of a mustache. He mopped like a robot, jerkily, brainlessly, but took pains not to splash suds over the toes of his black boots.

HELMHOLTZ: (taking a sip of coffee; to Quinn) That boy, I've seen him around school.

QUINN: (laughing cheerlessly) Billy the Kid? The storm trooper? (calling to the boy) Hey, Jim! Come here a minute.

NARRATOR: The boy's eyes were as expressionless as oysters.

QUINN: This is my brother-in-law's kid by another marriage. His name's Jim Donnini; he's from the south side of Chicago, and he's very tough.

NARRATOR: Jim Donnini's hands tightened on the mop handle.

HELMHOLTZ: How do you do? You want a lift to school, Jim?

QUINN: Yeah, he wants a lift to school. (to Jim) Go on, kid, wash up and shave.

NARRATOR: Robotlike, Jim marched away.

HELMHOLTZ: Where are his parents?

QUINN: His mother's dead. His old man married my sister, walked out on her, and stuck her with him. The court didn't like the way she was raising him and put him in foster homes for a while. Then they decided to get him out of Chicago, so they stuck me with him. (shaking his head) Those boots, the black jacket -- and he won't talk. Won't study. Can’t even read and write very good.

HELMHOLTZ: Does he like music? Or drawing? Does he collect anything?

QUINN: He likes to polish those boots. (smiles ruefully) He had a collection. Took it away from him and threw it in the river.

HELMHOLTZ: Threw it in the river?

QUINN: Yeah. Eight knives -- some with blades as long as your hand.

NARRATOR: Helmholtz paled. A prickling sensation spread over the back of his neck.

HELMHOLTZ: Oh, this is a new problem at Lincoln High. I hardly know what to think about it. It's a kind of sickness, isn't it?

QUINN: (grimly) No more talk about the poor little sick boy. That's all he's heard from the social workers and the juvenile court. From now on, I'll ride his tail till he straightens up or winds up in the can for life. **** in Helmholtz’s car on the way to school*****

HELMHOLTZ: (brightly)Like listening to music? (no response) Ever drum with your fingers or keep time with your feet? (Jim sighs heavily) Or whistle? If you do any of those things, it's like picking up the keys to a whole new world -- a world as beautiful as any world can be. (Jim gives a soft Bronx cheer) There! The glorious voice of the brass wind instruments! Starts with a buzz on the lips. (happily does his own Bronx cheer)

NARRATOR: The seat springs creaked as Jim shifted his weight to get a cigarette from inside his leather jacket.

HELMHOLTZ: (Softly) Sometimes, I get so lonely, I don't see how I can stand it. I feel like doing all kinds of crazy things, just for the heck of it -- things that might even be bad for me. (Jim blows a smoke ring) And then! (snaps his fingers) I remember I've got one tiny corner of the universe I can make just the way I want it! I can go to it until I'm happy again.

JIM: Aren't you the lucky one? (yawns)

HELMHOLTZ: I am. My corner of the universe happens to my band -- Music. Mr. Beeler, in zoology, has his butterflies. Mr. Trottman, in physics, has his pendulum and tuning forks. Making sure everybody has a corner like that is about the biggest job we teachers have. I . . .

NARRATOR: The car door opened and slammed, and Jim was gone. (beat) ******At school******

NARRATOR: Helmholtz's first class of the morning was C Band, where beginners wheezed and tooted as best they could. Helmholtz stepped onto the podium. There was a note calling him to a special faculty meeting about vandalism. Someone had broken in and wrecked the office of Mr. Crane, head of the English Department. The poor man's treasured books, diplomas, and the beginnings of eleven novels had been ripped, crumpled and drenched with ink. Helmholtz was sickened. He couldn't believe it.

It didn't become real to him until late that night, in a dream. Helmholtz saw a boy with barracuda teeth, with claws like baling hooks. The monster climbed into a window and dropped to the floor of the band rehearsal room. It clawed to shreds the biggest drum in the state. Helmholtz woke up at two in the morning. There was nothing to do but dress and go to the school.

Helmholtz rolled the drum back and forth on its cart; he turned the lights on and off, on and off. The drum was unharmed. The band's treasure house was safe. With the contentment of a miser counting his money, Helmholtz began to polish the sousaphones. [It was then that] he heard a noise in the chemistry laboratory next door. He sneaked into the hall, jerked open the laboratory door, and flashed on the lights. Jim Donnini had a bottle in either hand -- splashing acid over the periodic table of elements and the blackboards covered with formulas, The scene was the most repulsive thing Helmholtz could have looked upon.

HELMHOLTZ: (voice shaking with anger) Get out.

JIM: (smiling with bravado) What're you gonna do? You gonna call the cops?

HELMHOLTZ: (grabbing a rag and wiping up acid) Clean up. Save what I can.. If I'd caught you hurting the bass drum, I think I would have killed you. But I wouldn't have had any intelligent thoughts about what you were -- what you thought you were doing.

NARRATOR: He [felt] helpless. He had a bag of tricks for making boys behave like men -- tricks that played on boyish fears and dreams and loves. But here was a boy without fear, without dreams, without love.

JIM: It's about time this place got set on its ear! What good is it?

HELMHOLTZ: (sincerely) It's the best thing human beings ever managed to do. If you smashed up all the schools, we wouldn't have any hope left.

JIM: (bitterly) What hope?

HELMHOLTZ: The hope that everybody will be glad he's alive. Even you.

JIM: That's a laugh.

HELMHOLTZ: (with growing anger) Isn't there anything you care about? Anything? Anything but those boots?

NARRATOR: He marched Jim into his tiny office, opened a locker and took a trumpet from it. He thrust it into Jim’s arms.

HELMHOLTZ: There! (full of emotion) There's my treasure -- the dearest thing I own. Smash it! I won't stop you.

Watch my heart break while you do it. Go on! (Jim doesn’t move)

NARRATOR: Helmholtz grabbed Jim’s belt and dumped him on the floor. He pulled Jim's boots off and threw them into a corner; jerked the boy to his feet again and thrust the trumpet into his arms. Jim Donnini was barefoot now. He had lost his socks with his boots. The feet, once big black clubs were narrow as chicken wings now -- bony and blue. The boy shivered, then quaked. Each quake seemed to shake something loose inside, until, at last, there was no boy left, no boy at all.

HELMHOLTZ: (overwhelmed with remorse, reaches out to Jim) Jim! Jim -- You know what's special about the trumpet? (Jim stops quaking) It belonged to John Philip Sousa! I'll trade it to you, for your boots. I don't think they're good for you. You can learn to play it.

NARRATOR: Helmholtz released Jim slowly, sure the boy would topple. Jim didn't fall. He stood alone, the trumpet still in his arms. (beat) Helmholtz drove Jim home and let him out at Quinn's restaurant. The soft pats of Jim's bare feet echoed down the empty street.

He climbed through a window and into his bedroom behind the kitchen. All was still.

The next morning Helmholtz sat in a booth again. Quinn joined him. Jim mopped, eyes down, refusing to notice Helmholtz. And he didn't seem to care when a surf of suds broke over the toes of his small and brown Oxfords.

QUINN: (jerking his head at Jim) Kid! Go get Mr. Helmholtz his horn. (to Helmholtz) You take away his boots and give him a horn, and I'm not supposed to ask questions? I’m not supposed to find out you caught him taking the school apart? (with disgust) It's over. I'm sending him back where he came from.

HELMHOLTZ: (weakly) To another string of foster homes? That will be the end of him. He can't stand to be thrown away like that one more time.

QUINN: I can't help him; I can't hurt him. Nobody can. There isn't a nerve in him.

HELMHOLTZ: (sadly)A bundle of scar tissue.

NARRATOR: The bundle of scar tissue returned with the trumpet. Impassively, he laid it on the table in front of Helmholtz.

HELMHOLTZ: (with a forced smile) It's yours, Jim. I gave it to you.

QUINN: Take it, Helmholtz. All he'll do is swap it for a knife or a pack of cigarettes.

HELMHOLTZ: He doesn't know what it is . . . yet. It’s hope.

NARRATOR: After a long silence, Helmholtz picked up the trumpet. He had thought that his greatest treasure, the trumpet, could buy a soul for Jim. The trumpet was worthless. Deliberately, Helmholtz hammered the trumpet against the table edge and handed the wreck to Quinn.

QUINN: Ya busted it. Why'dja do that? What's that prove?"

HELMHOLTZ: (fighting back tears and shame) Life is no damn good.

NARRATOR: Helmholtz, the mountain that walked like a man, was falling apart. Jim Donnini’s eyes filled with pity and alarm. They came alive. They became human. Helmholtz had got a message through. Quinn looked at Jim, and something like hope flickered for the first time in his bitterly lonely old face. ******* Two weeks later*******

NARRATOR: Two weeks later, a new semester began at Lincoln High. In the band rehearsal room, the members of C Band were waiting for their leader . . . Helmholtz stepped onto the podium and rattled his baton against his music stand. He glanced at Jim Donnini, who sat in the last seat of the worst trumpet section of the worst band in school. His trumpet, John Philip Sousa's trumpet, had been repaired.

HELMHOLTZ: Think of it this way. Our aim is to make the world more beautiful than it was when we came into it. It can be done. You can do it.

NARRATOR: A small cry of despair came from Jim Donnini.

JIM: How?

NARRATOR: It was meant to be private, but . . .

HELMHOLTZ: Love yourself and make your instrument sing about it . . . (with his baton) A-one, a-two, a-three.
```

---

## IC-2069: Landfill

- Title: Landfill
- Author (byline): Joyce Carol Oates
- Work: New Yorker Magazine
- Publisher: New Yorker Magazine
- Publication date as stated: October 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1528
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joyce Carol Oates
Book: New Yorker Magazine
ISBN: B000060MGW
Publisher: New Yorker Magazine
Date (Month/Year): October 2006
```

### Introduction (context only: never use it for content warnings)

```text
Sometimes fiction is based on factual events. Such is the case with this selection based on a 2006 Missing Persons case in Trenton New Jersey . . . the facts are as follows:

John Fiocco, Jr. 19, was last seen in the early morning of March 25 after returning to his dormitory from an off-campus party. His roommate reported him missing to campus police about 36 hours later.

The following day, investigators found blood in and around the trash bin behind Fiocco's dorm. After a laboratory confirmed the blood was Fiocco's, investigators started sifting through a 1-acre, 20-foot deep area at the landfill, which authorities believe received the trash from Fiocco's dorm.

Is the fictionalization of such a tragic event morally ethical? Has the freedom of the press overstepped the bounds of good taste and appropriate consideration for the family and friends of John Fiocco, Jr? I’ll leave that to you to decide. Landfill by Joyce Carol Oates.
```

### Performance text (classify this)

```text
Scoot Campos, nineteen years old, a freshman engineering student at Michigan State University at Grand Rapids, has been reported missing by his dormitory room-mates in the late afternoon of Monday, March 27th. Last seen around 2 A.M. Saturday, March 25th, in the parking lot behind the Phi Epsilon fraternity house.

His roommates guessed something might be wrong, called the frat house, but there was no answer. Scoot’s things were exactly as he’d left them sometime Saturday afternoon, and it wasn’t like Scoot to stay over at the frat house on a Sunday night, or through Monday. He was only a pledge and didn’t have a bed there, and he’d missed four Monday classes.

And now, in the early morning of April 17th, Mrs. Campos answers the phone on the first ring. These terrible weeks that her son has been missing, Mrs.

Campos has answered the phone many times and made many calls, as her husband has made many calls, and now the call from the Tioga County Sheriff’s Department they have been dreading. Mrs. Campos? Are you seated? Is your husband there?

Mrs. Campos is not seated but standing, barefoot, shivering, with matted hair and glazed eyes, her mouth tasting of scum from the hateful medication that has not yet helped her to sleep. Mr. Campos, hurriedly descending the stairs says, “Irene, what is it? Who is it?” and rudely pries her icy fingers off the receiver.

Just the day before, in the car driving home, Mrs. Campos had dissolved into hysteria, screaming, “You don’t have faith! You’ve given up faith, I hate you!” For it was crucial to believe, as Mrs. Campos believed, that, nearly three weeks after Hector, Jr., “disappeared,” he might yet be found unharmed. He might yet call his anxious parents, after so many days of (inexplicably) not calling. He might show up to surprise his parents on Easter Sunday when they returned from St. Joseph’s, might be in the kitchen, eating from the refrigerator.

Or maybe Hector had been injured and was amnesiac, or had been abducted but would escape his captor or be released. Or he had been wandering, drifting, who knew where, hitchhiking; he’d left the university without telling anyone, he was upset, had problems with a girl, a girl he’d never told his parents about, just as he’d never told them much about his personal life since sophomore year of high school. Maybe the Phi Epsilons had been putting pressure on Hector; maybe he’d been made to feel inferior among the pledges. He’d once called his mother to say how crappy he felt, never having enough money—the other guys had money, but he didn’t. He’d told her that if the fraternity dropped him, didn’t initiate him with the other pledges, he’d kill himself, he would. He swore he’d kill himself! And Mrs. Campos had pleaded, “Please don’t say such terrible things! You don’t mean what you’re saying, you’re breaking my heart.”

It was no wonder that Hector had been so lonely, away from home for the first time in his life. None of his Southfield High friends were at Grand Rapids. His classes were too large; his professors scarcely knew him. Twelve thousand undergraduates at Grand Rapids. Three hundred residents in Brest Hall, an ugly high-rise where poor Hector shared a room with two other guys—Reb and Steve—who, in Hector’s words, never went “out of their way” to be friendly to him.

In turn, Hector’s roommates spoke vaguely of him when they were interviewed by Tioga County sheriff’s deputies. Didn’t know Scoot too well, he kind of kept to himself, kind of obsessed about things, like the wrestling team last fall. He didn’t make it, but the coach encouraged him to try again, so he was hopeful. Fraternity rush was a crazed time for Scoot. He was really happy when he got a bid from the Phi Eps. He was so proud of his pledge pin, and he was looking forward to living in the frat house next year if his dad O.K.’d it. Phi Eps are known for their keg parties—they’re kind of wild-party guys.

Who would notice . . . A drunken pledge crawling head first into the chute of his own volition . . . One of the guys grabs his ankles to pull him back, and he’s kicking and yelling and laughing. At least it sounds like laughter. Hey, guys? Help me? Help me, guys?

He’s kicking like crazy, so whoever has hold of his ankles has to let go -- and then his thick, stocky body lurches down the trash chute. It sounds like a pig squealing, or a kid shooting down a slide in an amusement park. At the end of the pitch-black, stale-air chute there should be something soft to break his fall, except there isn’t, and with the impact of a hundred and seventy-five pounds Scoot Campos strikes the edge of the trash bin and his forehead hits its sharp metal lip.

Immediately he’s bleeding, dazed; his neck has been twisted, his spine, his legs are buckled weirdly beneath him. He’s too dazed to be panicked, not knowing what has happened or where he is. Feebly, he pleads “Hey, guys? Help me?” amid a confusion of rich, ripe, rotting smells, something rancid. He’s upside down trying to turn, to rotate his body, stunned and quivering like a mangled worm, trying to lift his head, to breathe, to open his mouth, a terrible throbbing pain in his neck, in his upper spine. Like a gasping fish he opens his mouth, but he can’t make a sound, can’t call for help. For sure the guys will check on Scoot, make their way downstairs shouting and laughing like hyenas. Craziest thing, this drunk pledge, smashed out of his head, slid down the trash chute. It’s not the first time a drunken pledge or active at the Phi Ep house has slid down the trash chute into the Dumpster. Anyway, at some point there was the intention to check on the pledge in the Dumpster, but amid the party noise, the swarm of people—including heavily made-up high-school girls—and the pounding music there were too many distractions.

When interviewed by the Tioga County investigators, none of the guys could remember, exactly. First we knew Scoot was missing, it’s the dean calling. Nobody here knew he was missing. Must’ve gone back to his dorm and something happened there, or maybe he never went back. But whatever happened to him didn’t happen here.

No, of course not . . . .not given the Fraternity’s history. For several years in the nineteen-nineties, Phi Epsilon fraternity was “suspended” from the university for having violated a number of campus and city ordinances: underage/illegal drinking on the premises, keg parties in the front yard, “operating a public nuisance,” sexual assaults against young women and high-school-age girls, and even, during a secret initiation ceremony in 1995, against a Phi Epsilon pledge who had to be rushed to a local emergency room with “rectal hemorrhaging.” Bankrupt from fines, lawsuits, and a dwindling membership, the fraternity had gone off campus until, in 1999, a group of aggressive alums, led by a Michigan state legislator, campaigned to have it reinstated. Still, by 2006 the fraternity hadn’t yet regained its pre-suspension numbers—it had only twenty-six active members, one-third of whom were on academic probation.

Tioga County landfill is where Hector, Jr., is found. Or his “remains”—battered and badly decomposed, his mouth filled with trash. He couldn’t have protested if he’d been alive, buried, as he was, in rubble and raw garbage. Overhead are shrieking birds; in the vast landfill, dump trucks and bulldozers and a search team from the Tioga County Sheriff’s Department in protective uniforms. Most of his teeth are broken at the roots, but those which remain are sufficient to identify Hector Campos, Jr., of Southfield, Michigan.

The police investigation has yet to determine whether Hector died in the early hours of March 25th in the steep-sided Dumpster behind the Phi Epsilon frat house—where investigators found stains and swaths of blood, as if made by wildly thrashing bloody wings—or whether he died as many as forty-eight hours later, after lying unconscious, possibly comatose from brain injuries, until Monday morning, and then being hauled away unseen beneath mounds of trash, cans, bottles, Styrofoam and cardboard packages, rancid raw garbage, stained and filthy clothing, and paper towels soaked in vomit. At approximately 6:45 A.M. on March 27th, he was dumped into the rear of a thunderous Tioga County Sanitation Department truck and hauled sixteen miles north of the city to the Packard Road recycling transfer station, to be compacted and then hauled away again to the gouged, misshapen, ever-shifting landscape of the Tioga County landfill.

Jesus! You have to hope that the poor kid died right away, smashed out of his mind, diving down the trash chute into the Dumpster and breaking his neck on contact. Only the police investigators can bring themselves to imagine that Hector Campos, Jr., may have been “compacted” while still alive.
```

---

## IC-2070: Last Requests

- Title: Last Requests
- Author (byline): Giles Smith
- Work: Speaking with the Angel
- Publisher: Riverhead Books
- Publication date as stated: Feb 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1420
- Already set (do not supply): none

### Source block (context only)

```text
Author: Giles Smith
Book: Speaking with the Angel
ISBN: 978-1573228589
Publisher: Riverhead Books
Date (Month/Year): Feb 2001
```

### Introduction (context only: never use it for content warnings)

```text
According to Pew Research.org, use of the death penalty has gradually declined in the United States in recent decades. But, while state-level executions have decreased, the federal government put more prisoners to death (a total of 87) under President Donald Trump than at any point since the U.S. Supreme Court reinstated capital punishment in 1976. As of September 1, 2021, five executions by lethal injection have taken place this year in the US.

Study media reports of executions, recent or decades-old, and you’ll probably find mention of the prisoner’s last meal. Although the custom has a rich and controversial history, last meals evoke a morbid curiosity and leave many people wondering, “What would I choose as my final meal?”

This prison cook has quite a lot to say about the prisoners’ Last Requests by Giles Smith
```

### Performance text (classify this)

```text
(Pg 31-43) Pork chop – nice and thick – with sprouts, a carrot-and-swede mix, mashed potatoes and gravy. Now, that’s a proper meal. And after, fruit pie and custard or cream. A proper, home-backed pie, mind you – none of your tins and packets. Proper, wholesome food. But a lot of them, these days, they don’t want that. It’s all burgers and fries. Milkshakes, some of them. Well, that’s not a proper meal is it? Not what I call a proper, sit-down meal. With my three, every night, there was meat and vegetables and a pie afterwards, never fail. Always. Not like the kids all picky and refusing to eat. I’d crack the whip. No getting down until that bowl’s clean. Come on: chop chop, eat up, or you’ll waste away.

Steak – that’s popular. Quite a few of them ask for steak, and when the do, I try to get a nice one. I do a good steak. The problem with steak is, it’s quite a long way from the kitchen to the Row. You’ve got to go out of the canteen block then across “Y” yard and up three flights. It can take a few minutes what with the security grilles. Really, with a steak, that’s not the best thing. A steak should be out of the frying pan and onto the plate and then straight into your mouth, all hot and melty. You don’t want to wait around for a steak. They might be better off with a stew or a pie. Something which keeps its heat. I don’t think any of them think about that – though why should they? It’s not like they haven’t got plenty on their minds already, my God.

I’ve been doing it for two and a bit years now, and I suppose you get into something like a routine. There was all sorts of fuss when they brought it back. People say, we didn’t used to need it. But you’d have to say it was a more innocent world then. There wasn’t the terrorism, for one thing. Or there was, but not nearly so much of it. And you never heard about people having guns, the way you do now. And all the business with the children, when people got very worked up about. I don’t know why, as time goes by there just seems to be more wickedness generally. Like the one they sent off last night. Nineteen years old. Climbed a tree by a playground in a park and started firing. Eleven little ones he killed, and three mothers. They asked him why and he said, “I wanted to see them scared.” Well, what are you going to do with someone like that? No, on the whole, I think they had to bring it back.

Some people think they don’t deserve anything. Jean from next door, she’s said to me before, “I don’t know how you can bring yourself. Cooking a special tea for someone who’s evil.” And I know what she means, except I don’t really see it like that. I know the kind they get up there.

They’ve done awful things, wicked things, it’s unimaginable what they’ve done, some of them. But even so, I think there’s human standards and you’ve got to treat them right. You’ve got to remember, they’ve been up there for months [years], some of them – sitting around, thinking about what’s coming. It’s a difficult time for them. And they don’t get any special treatment up there, day to day, far from it, just the same food as the rest which, between you and me . . . I mean, we do our best, but the budget’s tight and anyway you’re cooking for nineteen hundred. There’s not exactly going to be the personal touch, is there?

I don’t know what it must be like, to know you’re going to die. We know they’ve done wrong and we know we can’t forgive them, but at least we can give them their dignity at the end. Well, that’s how I see it. I said to Jean, “You’d want the same if it was you, Jean.”

They can have what they like, within reason, up to a maximum of three courses, with coffee or tea and a piece of confectionery if they want it. No alcohol, for obvious reasons. You’ll get the jokers, like the one who said he wanted a whole roast pig with an apple in its mouth. Or the governor’s head, one of them said he wanted. The boy in the tree wanted cauliflower cheese. Which, to be honest, I think of more as a snack than a proper supper.

There’s some that are so negative, I don’t pretend to understand. “20 Marlboro Lights, one packet of chewing gum.” A shame really, when you think what he could have had. But there’s quite a number, in actual fact, who only want cigarettes. Or bowls of cereal, even. It’s as if they’ve already given up, in a way. And you wouldn’t believe the writing on some of those forms. It’s good the wardens go through it with them first, because some of them, frankly, I wouldn’t be able to read. Big letters and small letters all jumbled. And as for spelling . . . it’s all they can do, some of them, to write their names.

I think the fact you could have anything kind of paralyses them in a way. It’s almost as if they’d be better off with a menu, a range of options, so they could choose. There was one the other week who just wanted a sandwich. They’d gone up at midday to collect the form and he was just sitting there, hadn’t written anything. He was this middle-aged man who’d killed his children, four of them, at breakfast one morning, with a rifle – for no real reason, apparently. He just got angry and that was that, and the next thing he was phoning the police and asking them to come and get him. Just a sandwich. Sad, really, but I think it’s true of a lot of them on the Row that they don’t really know their own minds by the end. I made him a cheese and pickle one, because nobody ever objects to that.

I’ve never met any of the ones I’ve done the meal for. They don’t let them in the canteen area, so I never set eyes on them. I suppose I am curious sometimes, to know what they’re like. The one who killed his children. I’d have like to try and tempt him into something more than a sandwich. Sometimes the wardens will pass something on; “He looked happy with that. “

The meal goes up at 8:00 and the executions are directly after midnight. There’s some legal reason for that, I think. But that’s four hours between the meal and the end of it and I often wonder if they get puckish again. Every now and again, you’ll send the meal up and they’ll eat it, and then the phone call comes through from the judge and they get a reprieve. All very dramatic. Well, good for them. But often it’s only temporary and, a month later, you’re cooking the same meal for them all over again. There’s one up there now who’s had his last meal five times.

I can be away by 8:30, which is plenty of time for the bus. There’s often a crowd outside when I leave. People come to the gates when there’s an execution. There’s a man with a big black parka. He’s always there. I don’t know why. It’s not like there’s anything to see. There isn’t even a clock that chimes. It just gets to be after midnight, and at that point they all go away again. So the wardens tell me. Sometimes, when I leave, there might be some banners and there might be a bit of shouting going on. But more often than not they’re just standing there quietly, like they’re waiting for something, I’ve no idea what.

Last night was odd, though. I hadn’t quite managed to get the monthly freezer check done during the day, so after they’d taken up the cauliflower cheese for the boy in the tree, I finished the job off. I’d got my coat on when Dave came back with the tray. [He] didn’t say anything, just put it down and turned away and I got a good look then and I wished I hadn’t because, do you know what, he hadn’t touched it.
```

---

## IC-2071: The Last Spin

- Title: The Last Spin
- Author (byline): Evan Hunter
- Work: Manhattan Noir 2: The Classics
- Publisher: Akashic Books
- Publication date as stated: Sept 2008
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1440
- Already set (do not supply): none

### Source block (context only)

```text
Author: Evan Hunter
Book: Manhattan Noir 2: The Classics
ISBN: 978-1933354576
Publisher: Akashic Books
Date (Month/Year): Sept 2008
```

### Introduction (context only: never use it for content warnings)

```text
Two rival gangs decide to solve a problem one on one instead of making war on the streets. A gang member is chosen from each gang to play Russian roulette: one person must die. As the two young men face each other “playing” this game in an empty basement room. As they talk, they realize that they have much in common, neither is the enemy, and there is no reason to create an enemy out of either group. The young men decide to defy gang rules and meet on Sunday to hang out. Lesson learned, barrel spins, gun fires, one dies. Last Spin by Evan Hunter
```

### Performance text (classify this)

```text
The boy sitting opposite him was his enemy, Tigo, and he wore a green silk jacket with an orange stripe on each sleeve. The jacket shrieked, "Enemy, enemy!"

"I got no bad blood for you. This is how the club said we should settle it. Without a big street diddlebop, you dig? I just happened to be picked for this, you know? You got to admit your boys shouldn't have come in our territory last night. One of us and. . . and one of you. Fair and square. But I want you to know I don't know you from a hole in the wall-except you wear a blue and gold jacket."

"And you wear a green and orange one," Danny said, "and that's enough for me."

Tigo picked up the gun, and then he took one of the cartridges from the table top. He broke open the gun, slid the cartridge into the cylinder, and then snapped the gun shut and twirled the cylinder. "Round and round she goes," he said, "and where she stops, nobody knows. There's six chambers in the cylinder and only one cartridge. That makes the odds five-to-one that the cartridge'll be in firing position when the cylinder stops whirling. You dig?"

Tigo stopped talking. The cylinder was stopped now. He took a deep breath, put the barrel of the .38 to his temple, and then squeezed the trigger.

The firing pin clicked on an empty chamber.

"Well, that was easy, wasn't it?" he asked. He shoved the gun across the table. "Your turn, Danny."

Danny reached for the gun. It was cold in the basement room, but he was sweating now. He pulled the gun toward him, then left it on the table while he dried his palms on his trousers. He picked up the gun then and stared at it.

Danny slapped the cylinder with his left hand. The cylinder whirled, whirled, and then stopped. Slowly, Danny put the gun to his head. He wanted to close his eyes, but he didn't dare. Tigo, the enemy, was watching him. He returned Tigo's stare, and then he squeezed the trigger.

His heart skipped a beat, and then over the roar of his blood he heard the empty click. Hastily, he put the gun down on the table.

"Makes you sweat, don't it?" Tigo said.

Danny nodded, saying nothing. He watched Tigo. Tigo was looking at the gun.

"Me now, huh?" Tigo said. He took a deep breath, then picked up the .38. He twirled the cylinder, waited for it to stop, and then put the gun to his head.

"Bang!" Tigo said, and then he squeezed the trigger. Again the firing pin clicked on an empty chamber. Tigo let out his breath and put the gun down. "I thought I was dead that time," he said.

"You got a chick?" Danny asked. "What's her name?"

"Aw, you don't know her."

"Maybe I do," Danny said.

"Her name is Juana." Tigo watched him. "She's about five-two, got these brown eyes..."

"I think I know her," Danny said. He nodded. "Yeah, I think I know her."

"She's nice, ain't she?" Tigo asked. He leaned forward, as if Danny's answer was of great importance to him.

"Yeah she's nice," Danny said.

"Yeah. Hey maybe sometime we could..." Tigo cut himself short. He looked down at the gun, and his sudden enthusiasm seemed to ebb completely. "It's you turn," he said.

"Here goes nothing," Danny said. He twirled the cylinder, sucked in his breath, and then fired.

The emptily click was loud in the stillness of the room.

"We better lower the odds. The boys won't like it if we..." He stopped himself again, and then reached for one of the cartridges on the table. He broke open the gun again, slipped in the second cartridge into the cylinder. "Now we got two cartridges in here," He paused. "You game?"

"That's... that's what we're here for, ain't it?" Danny said gently. "It's your spin."

Tigo lifted the gun. Idly, he began spinning the cylinder.

"You live on the next block, don't you?" Danny asked.

"Yeah."

"That's how come we never crossed paths, I guess. Also, I'm new on the scene."

"Yeah, well you know, you get hooked up with one club, that's the way it is."

"You like the guys on your club?"

"They're okay." Tigo shrugged. "None of them really send me, but that's the club on my block, so what're you gonna do, huh?" His hand left the cylinder. It stopped spinning. He put the gun to his head.

"Wait!" Danny said.

Tigo looked puzzled. "What's the matter?"

"Nothing. I just wanted to say... I mean..." Danny frowned. "I don't dig too many of the guys on my club, either."

Tigo nodded. For a moment, their eyes locked. Then Tigo shrugged, and fired.

The empty click filled the basement room.

Tigo slid the gun across the table.

Danny hesitated an instant. He did not want to pick up the gun. He felt sure that this time he would shoot himself.

"Sometimes I think I'm turkey," he said to Tigo, surprised that his thoughts had found voice."I never told that to nobody. The guys on my club would laugh at me, I ever told them that."

"Some things you got to keep to yourself. There ain't nobody you can trust in this world."

"There should be somebody you can trust," Danny said. "Hell, you can't tell nothing to your people. They don't understand."

"Sure, sure," Tigo said. "It ain't only that, though. Like sometimes... well, don't you wonder what you're doing stomping some guy in the street? Like ... who's the guy to you? What you got to beat him up for? 'Cause he messed with somebody else's girl?" Tigo shook his head. "It gets complicated sometimes."

"Yeah, but ..." Danny frowned again. "You got to stick with the club. Don't you?"

"Sure, sure ... hell yes." Again, their eyes locked.

"Well, here goes." Danny said. He lifted the gun, then twirled the cylinder. He studied the gun, wondering if one of the cartridges would roar from the barrel when he squeezed the trigger.

Then he fired.

Click.

"You got heart, Danny," Tigo said. He looked at the gun. He picked it up and broke it open.

"What you doing?" Danny asked.

"Another cartridge," Tigo said. "Six chambers, three cartridges. That makes it even money. You game?"

"It's your turn, you know."

"I know -- My spin," Tigo said wearily. He twirled the cylinder. "Here goes a good man," he said, and he put the revolver to his head and squeezed the trigger.

Click.

Danny smiled nervously. "No rest for the weary," he said. "But Jesus you've got the heart. I don't know if I can go through with it."

Sure, you can," Tigo assured him. "Listen, what's there to be afraid of?" He slid the gun across the table.

"We keep this up all night?" Danny asked.

"They said ... you know ... "

"Well, it ain't so bad. I mean, hell, we didn't have this operation, we wouldn'ta got a chance to talk, huh?" He grinned feebly.

"Yeah," Tigo said, his face splitting in a wide grin. "It ain't been so bad, huh?"

He picked up the gun.

"We could say ... well ... like we kept shootin' an' nothing happened, so ..." Tigo shrugged. "Let's make this the last spin. Listen, they don't like it, they can take a flying leap, you know?"

"I don't think they'll like it. We're supposed to settle this for the clubs."

"Screw the clubs!" Tigo said. "Can't we pick our own ..." The word was hard coming. When it came, his eyes did not leave Danny's face. "... friends?"

"Sure we can," Danny said vehemently. "Sure we can! Why not?"

"The last spin," Tigo said. "Come on, the last spin."

"Game," Danny said. "Hey you know, I'm glad they got this idea. You know that? I'm actually glad!" He twirled the cylinder. "Look, you want to go on the lake this Sunday? I mean with your girl and mine? We could get two boats. Or even one if you want."

"Yeah, one boat," Tigo Said. "Hey, your girl'll like Juana, I mean it. She's a swell chick."

The cylinder stopped. Danny put the gun to his head quickly.

"Here's to Sunday," he said. He grinned at Tigo, and Tigo grinned back, and then Danny fired.

The explosion rocked the small basement room, ripping away half of Danny's head, shattering his face. A small cry escaped Tigo's throat, and a look of incredulous shock knifed his eyes. Then he put his head on the table and began weeping.
```

---

## IC-2072: The Last Testament: A Memoir by God

- Title: The Last Testament: A Memoir by God
- Author (byline): David Javerbaum
- Work: Not specified
- Publisher: Simon and Schuster
- Publication date as stated: Nov 2011
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1531
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Javerbaum
ISBN: 978-1451640182
Publisher: Simon and Schuster
Date (Month/Year): Nov 2011
*God Bless America – Music and Lyrics
https://www.youtube.com/watch?v=gjbMmIXKZmQ
```

### Introduction (context only: never use it for content warnings)

```text
Over the course of his long and distinguished career, God has literally seen it all. And not just seen. In fact, the multi-talented deity has played a pivotal role in many major events, including the Creation of the universe, the entirety of world history, the life of every human being who has ever lived, and the transition to on-line learning during the COVID-19 pandemic.

Now, God breaks his 1,400-year literary silence to answer questions that have plagued mankind for centuries: Does God answer prayers? What is the truth behind all those Unsolved Mysteries on Netflix? Does God Love America the most?

The Last Testament: A Memoir by God by David Javerbaum
```

### Performance text (classify this)

```text
(Pg 217) Imagine being in fourth grade; the bell for homeroom rings, thou takest thy seat, and suddenly a deafening voice booms from the PA system:

"Good morning, students. I am the LORD thy God, King of the Universe. Here are the announcements: Starting today, I will no longer be accepting any prayers addressed to me from this public school. The Supreme Court hath ruled such prayers violate the First Amendment's establishment clause; and their ruling applies to not only thee, but me. Please refrain from addressing or thinking of me at any time while on school grounds. Also, the chess club will be meeting in Mrs. Binder's classroom during sixth period. Siiiiiixth peeeeeriod!"

Followed by thunder and lightning effects, and hundreds of plastic spiders falling from the ceiling.

Ah . . . one of these days I shall go to an elementary school and do that!

(Pg 217-219) I can afford to take the banning of school prayer lightly; it is not as if I need another venue wherein to hear thy supplications. For thine is the Golden Age of Prayer; never before have I received so many pleas, from so many people, for so many reasons, accompanied by so many helpful suggestions.

Do I answer them? I shall get to that.

But first, let me provide an overview of prayer, for its very definition is a matter of debate.;

For me, prayer is like unto a suggestion box that receives 200,000 suggestions a second. Or an emergency services switchboard manned by one operator who gets 12 million calls a minute.

[Now] I do not regard the human phenomenon of prayer cynically; I am merely trying to describe what it feels like to be incessantly nagged, pestered, and reminded of things I already knew.

It is one thing to ask, "Please take care of Bobby in his time of need"; that is an expression of a well-meaning wish. But it is another entirely to say, "Please take care of Bobby in his time of need; he just broke his leg skiing, and the karate meet is in three weeks and he's been training so hard ... " Heed me: I am the LORD thy God, King of the Universe: I know Bobby broke his leg skiing, and I know about the damned karate meet.

(Pg 220) By far my favorite prayer is the Serenity Prayer: “The serenity to accept what cannot be changed; the courage to change what can; and the wisdom to know the difference – these are wise life principles that should be known and followed by everyone.

As for my least favorite? That would be the old childhood lullaby: "Now I lay me down to sleep. I pray thee, LORD my soul to keep. And if I die before I wake, I pray thee, LORD, my soul to take."

Even I consider it bizarre, that the last words on children's lips before they go to sleep would address the prospect of their own premature death. They are children. They should be asking me for ponies. In fact, I make unto them this deal: the next one of you who asks for a pony instead of for me to take his or her soul, gets the pony.

(Pg 222) So, I know what thou art thinking: Do I answer thy prayers? I [can] assure my flock that every single prayer of thine is processed.

What is the truth behind all those Unsolved Mysteries on Netflix?

(Pg 144-148) I will start with a big one: the identity of the most notorious serial killer of all time, Jack the Ripper.

It was Neville Hopkins. He was an itinerant pickpocket squatting in Whitechapel; a quiet man; kept to himself; bit of a loner; few close friends. Flew completely under the radar. Right after the final murder he boarded a boat bound for New York and was never heard from again. Anyway, Neville Hopkins: Jack the Ripper. Now thou knowest.

Sticking with unsolved murders, Los Angeles's infamous Black Dahlia murder of 1947 was committed by folk singer Woody Guthrie. In fact, he confessed to the crime in the sixth verse of his most famous song: (sing to the tune of This Land Is Your Land) "As I was strolling South Norton Avenue, I met a woman, the Black Dahlia. I killed her slowly and bashed her face in. This land was made for you and me." But he was never caught; for no one ever makes it to the sixth verse of "This Land Is Your Land."

As for Lizzie Borden, she, with an axe, neither gave her mother 40 whacks, nor, having seen what she had done, gave her father 41. No; that August morning, the Bordens fell victim to a serial killer who broke into their house at random, chopped them both to bits, and fled the scene, never to be heard from again. His name?

Neville Hopkins.

The Shroud of Turin was a forgery produced in 1287 by the Turin Shroudmakers' Guild to promote the local shroud-making industry; it succeeded spectacularly.

The works of William Shakespeare were written by none other than legendary British playwright William Shakespeare.

Lee Harvey Oswald acted alone.

Turning now to cryptozoology: The Loch Ness Monster does exist; but he is not a monster of flesh and blood, rather the monster of bigotry and intolerance dwelling inside the human heart, which for some reason is then externalized as an imaginary Scottish plesiosaur.

On the other hand, El Chupacabra is real; he is a monstrous goat-like creature who poses an actual threat to Mexicans, and an even bigger one to Americans; for soon he plans to cross the border, where he will take away jobs from hardworking American mythical creatures like the Jersey Devil and Mothman.

On to a few legendary places: Atlantis was a real city on the Aegean island of Santorini that was destroyed by a massive volcano 3,600 years ago. It is lost forever; but I must tell thee that even were it not, it would not be worth finding. For Atlantis was a Bronze Age backwater whose imbecilic citizenry passed its time burping, farting, and raping sheep. Their demise was a boon for civilization, but it is with cities as it is with people: dying young and mysteriously can turn any idiot into a legend. (Yea, it was the only half-intelligent thing Jim Morrison ever did in his life.)

On the other hand, the Lost City of Gold, El Dorado, never existed, and it is just as well; for even I shudder to think of the "missionary work" men like Cortez or Pizarro would have practiced on its people once they caught sight of it. My guess is it would have started with flaying, then gone downhill from there.

Area 51 is a regular US military base; and though classified operations do occur there, they have nothing to do with aliens, UFOs, time travel, or anything out of the ordinary. Those ops all happen in Area 63.

And finally, Stonehenge. I have no idea what the hell Stonehenge is.

But I can shed light on a few questions I am guessing none of you thought ever would - or could - be answered. For example: which came first, the chicken or the egg? Neither. The rooster came first.

What is the sound of one hand clapping? Very disappointing, for a performer.

What is to be done? It depends.

When will they ever learn? Eventually.

Are we there yet? No. TRANSITION

(Sing the opening stanza of God Bless America)*

(Pg 135-136) Every time I hear “God Bless America,” I get angry. My objections to song and the saying are personal; for Americans asking me for more blessings is like Tahitians asking me for sunnier days. America is amply blessed; copiously blessed; countless are the blessings with which I have blessed America.

I blessed its land: the richness and variety of its topography, the fertility of its soil, the temperateness of its climate. I blessed it in its indigenous peoples, whose innate love of freedom was evident in their own freedom from heavy artillery, the concept of property or the resistance to smallpox. I blessed America with tobacco farmers of Jamestown, who showed the world that the new “land of opportunity” could bestow success on anybody willing to rely on hard work, the free market, and millions of black slaves growing a death-crop.

I blessed it with millions of immigrants from every nation on earth; mankind in its heaving diversity arrived on its shores, and every ethnicity fought to find its place, and in so doing each one strengthened the character of the nation. Yea, even the Mexicans.

I blessed it with an era where everyone thought of the United States as the good guy; yea, I go way back with America. (Shakes head sadly)

(Pg 139) America, allow me to address thee directly for a moment. When thou sentest a man to the moon, it was the most amazing achievement in human history, and Neil Armstrong correctly hailed it as “one giant leap for mankind,” meaning the entire human race. And then he went and put an American flag on it. On the moon.

Thou drivest me crazy, America, yet still I bless thee; despite all they short comings. And I continue to not only bless thee but to love thee, and to do so unhealthily; unhelpfully; in a manner that keeps thee from doing the soul-searching needed to become a better nation.
```

---

## IC-2073: The Latke Who Couldn't Stop Screaming: A Christmas Story

- Title: The Latke Who Couldn't Stop Screaming: A Christmas Story
- Author (byline): Lemony Snicket (aka Daniel Handler)
- Work: Not specified
- Publisher: McSweeny's
- Publication date as stated: Oct 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, LATKE, LIGHTS, CANDY CANE, PINE TREE, FATHER, MOTHER, DAUGHTER, SON
- Teaser before the introduction: Yes
- Spoken words (computed): 1096
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lemony Snicket (aka Daniel Handler)
ISBN: 978-1932416879
Publisher: McSweeny's
Date (Month/Year): Oct 2007
```

### Introduction (context only: never use it for content warnings)

```text
The Christmas season – a time of music, endless rounds of Christmas specials on every streaming service and malls decked to the rafters with tinsel, lights and every decoration imaginable. But for the Jewish population the holiday season is – well – different. What does it feel like to live in a society that is constantly pummeling you with religious messages that are not your own?

In Lemony Snicket’s tale, we find a latke who is really looking for two things, a sense of belonging, and for others to listen and acknowledge the importance of his differences. After all, isn’t that what we all are searching for?

The Latke Who Couldn’t Stop Screaming by Lemony Snicket

(aka Daniel Handler)
```

### Performance text (classify this)

```text
NARRATOR: This story begins in a tiny village more or less covered in snow. The snow had fallen during the long night during which children had pressed their faces to the windows looking for the glimpse of a man who they suspected of bringing them wonderful gifts. (screaming) But instead, they heard a terrible noise (screaming) from a certain cottage in the neighboring “arrondissement,” a word which means “place where something is being born.” This cottage, already regarded with some suspicion, was the only place not decorated with flashing colored lights at this time of year. [And] the thing being born was a “latke,” a word which means “potato pancake.” (repeated screaming)

NARRATOR: Latkes are a traditional part of the celebration of Chanukah – a holiday commemorating a miraculous Jewish military victory. (interrupted by screaming) Nearly everything in this world is born screaming, and the latke was no exception. Even though the latke wasn’t conceived and born the way you and I were, instead he was fashioned from grated potatoes, chopped onion, beaten eggs and a dash or two of salt. Once these ingredients were properly mixed, the latke was slapped into a pan full of olive oil, heated to a very high temperature, and this is when he began to scream.

LATKE: ARGHHHHHHHHH! ARGHHHHHHHHHHH!

NARRATOR: The latke was suffering so much that he leapt out of the hot pan, out of the window and began to run screaming down the boulevard.

LATKE: ARGHHHHHHHHHH!

NARRATOR: This may seem like unusual behavior for a potato pancake, but this is a Christmas story in which things tend to happen that would never occur in real life. The latke ran past a row of flashing colored lights, which hung from the rain gutters of a less suspicious cottage.

LIGHTS: What’s all the ruckus? We’re the ones who are supposed to be dominating the neighborhood with our cheerful glow.

LATKE: I was just thrown into a pan of boiling oil! Can you believe it?

LIGHTS: Yes, but we can’t imagine why.

LATKE: Because I’m a latke. The olive oil reminds us of the oil used to re-dedicate the temple following the defeat of Antiochus at the hands of the Maccabees. The oil was only supposed to last for one night, but there was a miracle and it lasted for eight. Plus frying makes my skin crispy and brown.

LIGHTS: So you are basically hashbrowns. Maybe you can be served alongside a Christmas ham.

LATKE: I’m not hashbrowns! I’m something completely different. (runs off screaming) ARGHHHHHHH! ARGHHHHH!

NARRATOR: The latke rounded the corner and found himself face to face with a candy cane which wrinkled its red and white nose at the latke in distaste.

CANDY CANE: I’m trying to sprinkle the night air with my peppermint scent. Your mouth-watering smell, not to mention all that yelping, is spoiling the effect.

LATKE: My mouth-watering smell is part of the cozy feeling of Chanukah. It reminds us that things are better now than they were in 175 BCE when my people were not allowed to practice their religion. In order to study the Torah, they had to hide out in caves. And when they heard Greek soldiers approach, they pretended they were gambling with a small spinning top called a “dreidel.“

CANDY CANE: Sort of like Joseph and Mary hiding out in the manager. Someone should write a Christmas carol about you.

LATKE: I’m not part of Christmas! It’s a totally different thing! (runs off screaming) ARGGGGHHHH! ARGHHHHHH!

NARRATOR: The screams of the latke grew quieter and quieter as the pancake ran out of the village into the surrounding forest. Its utter fury was unabated – a phrase which means “the latke was still very annoyed at the objects to whom it had spoken.” But it was quite tired, so it decided to rest for a few minutes beneath the branches of a little pine tree. The pine tree was napping but woke up at the sound of an object plopping down at its feet.

PINE TREE: Are you a present? Presents are pretty much the only things allowed to sit beneath me this time of year.

LATKE: (heavy sigh, then in a hoarse voice from screaming so much) Presents aren’t really a big part of Chanukah. There’s nothing wrong with giving gifts to loved ones, of course. But it’s more important to light the candles for eight consecutive nights to commemorate the miracle in the temple and the miracle of victory when you are thoroughly outnumbered so you shouldn’t give up hope.

PINE TREE: Plus . . . Santa Claus!

NARRATOR: The latke was too exhausted to scream.

LATKE: Santa Clause has nothing to do with it. Christmas and Chanukah are complete different things.

PINE TREE: But different things can often blend together.

Let me tell you a funny story about pagan rituals.

NARRATOR: But before the pine tree could begin its story, a family came trooping through the snow, searching the forest carefully.

FATHER: (holding an axe on his shoulder) We shouldn’t have waited until the last minute to get ready for the holiday. We’ll never find a good one.

MOTHER: You shouldn’t give up hope. (pointing to the pine tree) Look!

DAUGHTER: It’s perfect!

SON: Beautiful.

MOTHER: Such a marvelous shape.

FATHER: And its skin looks so crispy! (reaching down and scooping up the latke) We’ll need to reheat it, of course. But this will be perfect for Chanukah dinner with a topping applesauce, sour cream or even jam.

MOTHER: I’ll refry it in oil to remind us of the rededication of the temple.

DAUGHTER: And the triumph of the Maccabees over Antiochus!

SON: After hiding in caves all that time . . .

FATHER: (smiling at the latke in his hand) What was I thinking, bringing this axe?

NARRATOR: The family strolled back to the village, walking past all the cottages with flashing colored lights and smiling politely at the candy canes. The family carried the latke into their home which was warm and cozy and sat down at the table, which was lit with the flickering candles of a menorah or “chanukkiyah” which is a branched candelabra designed specifically for the holiday.

It is very frustrating not to be understood in this world. If you say one thing and keep being told that you mean something else, it can make you want to scream. But somewhere in the world, there is a place for all of us whether you are an electric form of decoration . . .

LIGHTS: What’s all the ruckus? We’re the ones who are supposed to be dominating the neighborhood with our cheerful glow.

NARRATOR: A peppermint scented sweet. . .

CANDY CANE: I’m trying to sprinkle the night air with my peppermint scent.

NARRATOR: A source of timber . . .

PINE TREE: Are you a present? Presents are the only things allowed to sit beneath me this time of year. Plus . . . Santa Claus! (screaming)

NARRATOR: Or . . . a potato pancake.

LATKE: (screaming)

NARRATOR: On a cold snowy night, everyone and everything should be welcome somewhere . . . and the latke was welcomed into a home full of people who understood what a latke is and how it fits into its particular holiday.

And then they ate it . . . .

LATKE: ARGHHHH . . UMMMMM! (scream muffled by the munching of Father)
```

---

## IC-2074: The Legend of Rock Paper Scissors

- Title: The Legend of Rock Paper Scissors
- Author (byline): Drew Daywalt
- Work: Not specified
- Publisher: Balzer and Bray
- Publication date as stated: April 2017
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, ROCK, CLOTHES PIN, APRICOT, COMPUTER PRINTER, PAPER, TRAIL MIX, SCISSORS, TAPE, DINOSAUR, NARRTOR
- Teaser before the introduction: No
- Spoken words (computed): 821
- Already set (do not supply): none

### Source block (context only)

```text
Author: Drew Daywalt
ISBN: 978-0062438898
Publisher: Balzer and Bray
Date (Month/Year): April 2017
```

### Introduction (context only: never use it for content warnings)

```text
You’ve played the game . . . . Now gather round and hear the legend of the three fierce warriors who brought the game to life. The Legend of Rock Paper Scissors by Drew Daywalt.
```

### Performance text (classify this)

```text
NARRATOR: Long ago, in an ancient and distant realm called the Kingdom of Backyard, there lived a warrior named ROCK.

ROCK: (Rock enters and postures in pantomime)

NARRATOR: Rock was the strongest in all the land, but he was sad because no one could give him a worthy challenge. Rock traveled to the mysterious Forest of Over by the Tire Swing, where he met a warrior who hung on a rope, holding a giant’s underwear.

ROCK: (Rock spots Clothes Pin and yells up to him) Drop that underwear and battle me, you ridiculous wooden clip-man!

CLOTHES PIN: I will pinch you and make you cry, Rock Warrior!

NARRATOR: (In the voice of a ring announcer) Rock versus Clothespin! (An epic battle ensures – actors depicts both characters in the battle with lots of sounds, but no real words) Rock is victorious! (Returns to normal Narrator voice) Even though he had won, Rock was still unsatisfied. So he journeyed on, to the mystical Tower of Grandma’s Favorite Apricot Tree. There he was met by an odd and delicious fruit.

ROCK: (Rock spots Apricot and yells up to him) You, sir, look like a fuzzy little butt.

APRICOT: What?! I challenge you to a duel! I will beat you, Rock, with my tart and tangy sweetness!

ROCK: Then let us battle!

NARRATOR: (In the voice of a ring announcer) Rock versus Apricot! (An epic battle ensures – actors depicts both characters in the battle with lots of sounds, but no real words) Rock is victorious!

APRICOT: Ugh, I am smooshed!

ROCK: And yet, smooshing you has brought me no joy.

NARRATOR: The battle had been too easy. So Rock left the Kingdom of Backyard, still in search of a worthy foe. Meanwhile in the Empire of Mom’s Home Office, on lonely and windswept Desk Mountain, a second great warrior sought the glory of battle. And his name was Paper. (Paper enters and postures in pantomime)

Even though he was the smartest warrior in all the land, he was also sad, because no one could outwit him. He set out across Desk Mountain to find his match. There he met a large and square monster.

COMPUTER PRINTER: I gobble up the likes of you and spit them out every day, little paper!

PAPER: Oh? Then taste my fury, giant box-monster!

COMPUTER PRINTER: Noooooo! Not a paper jam!

NARRATOR: (In the voice of a ring announcer) Paper versus Computer Printer! (An epic battle ensures – actors depicts both characters in the battle with lots of sounds, but no real words) Paper is victorious! (Returns to normal Narrator voice) Having beaten the fiercest fighter of Desk Mountain, Paper climbed down to the Pit of Office Trash Bin, where he battled the most terrifying horde of creatures in all the land . . . the Half- Eaten Bag of Trail Mix!

NARRATOR: (In the voice of a ring announcer) Paper versus Half-Eaten Bag of Trail Mix!

TRAIL MIX: (but there is no battle because the Trail Mix runs away) Ahhhhhh! Foul wizard! He’s blotted out the sun! Run for your lives, laddies!

NARRATOR: Paper wins again!

PAPER: Can no one beat me?

NARRATOR: And so, with a heavy heart, Paper departed the Empire of Mom’s Home Office. At the same time, in the Kitchen Realm, in the tiny village of Junk Drawer, there lived a third great warrior. They called her Scissors, and she was the fastest blade in all the land.

(enter Scissors who postures in pantomime) She too, was unchallenged. On this day, her first opponent was a strange and sticky circle-man.

SCISSORS: (Scissors spots Roll of Tape and takes a fighting stance) Let us do battle, you tacky and vaguely round monstrosity!

TAPE: I will battle you, and I will leave you beaten and confused with my adhesive and tangling powers!

NARRATOR: (In the voice of a ring announcer) Scissors versus Roll of Tape! (An epic battle ensures – actors depicts both characters in the battle with lots of sounds, but no real words) Scissors is victorious! (Returns to normal Narrator voice) Scissors forged on across the Kitchen Realm to the frigid wastes of Refrigerator/Freezer. There she met her most fearsome adversaries yet . . . dinosaurs made of frozen breaded chicken.

SCISSORS: (Scissors spots the Dinosaurs and takes a fighting stance) I have come from the far reaches of Kitchen to battle you, O, bizarre and yummy breaded dinosaurs!

DINOSAUR: Bow before our child-pleasing shapes and flavors, sword master! No one can resist our crunchy awesomeness!

NARRATOR: (In the voice of a ring announcer) Scissors versus Dinosaur-Shaped Chicken Nuggets! (An epic battle ensures – actors depicts both characters in the battle with lots of sounds, but no real words) Dinosaur- Shaped Chicken Nuggets win . . . ? (The battle continues) No wait! No, they don’t! Scissors is victorious again!

SCISSORS: Am I so good that not even Dinosaur-Shaped Chicken Nuggets can beat me?

NARRATOR: And so Scissors, like Rock and Paper before her, traveled beyond her own kingdom, seeking out a challenger who was her equal. Then one day in the Great Cavern of Two-Car Garage, Rock and Scissors came face-to-face.

SCISSORS: I hope you’re wearing your battle pants, rock warrior.

ROCK: If by “battle pants” you mean “no pants, but I’m willing to fight you,” then yes . . . yes, I am wearing my battle pants, weird scissory one!

NARRTOR: (In the voice of a ring announcer) Rock versus Scissors! (An epic battle ensures – actors depicts both characters in the battle with lots of sounds, but no real words) Rock is victorious!

SCISSORS: You have made me so happy by beating me!

ROCK: I wish I felt your joy, Scissors, for I have yet to meet a warrior who can beat me.

PAPER: Hi there.

ROCK: Those are fighting words!

PAPER: Wait. What??

NARRATOR: (In the voice of a ring announcer) Rock versus Paper. (An epic battle ensures – actors depicts both characters in the battle with lots of sounds, but no real words)

ROCK: This is the best day of my life! Thank you for winning, O great knight of paper!

PAPER: That’s fine for you, but it looks as thought no one will ever beat me.

SCISSORS: Not so fast, Paper

PAPER: Wait. What??

NARRATOR: (In the voice of a ring announcer) Scissors versus Paper! (An epic battle ensures – actors depicts both characters in the battle with lots of sounds, but no real words)

PAPER: You beat me!

NARRATOR: And the three great warriors hugged each other and danced for joy, and they became fast friends. Finally, they had each met their matches. They were so happy, in fact, that they began to battle again. ‘Round and ‘round they went, in the most massive and epic three-way battle of all time! And it is said that this joyous struggle still rages on to this very day. That is why children around the world—in backyards, on playgrounds, and yes, even in classrooms – still honor the three great warriors by playing . . . Rock, Paper, Scissors
```

---

## IC-2075: Life Support

- Title: Life Support
- Author (byline): Stephanie Summerville
- Work: The Moth, Pg 358-365
- Publisher: Hachette Books
- Publication date as stated: Sept 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1427
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephanie Summerville
Book: The Moth, Pg 358-365
ISBN: 978-1401311117
Publisher: Hachette Books
Date (Month/Year): Sept 2013
```

### Introduction (context only: never use it for content warnings)

```text
In the US, health care workers take an oath to treat all patients equally, but that’s not always the case. According to numerous studies, members of the Black community experience more illness, worse outcomes and premature death compared to their white counterparts. In addition to disparities in income, housing and education, inherent racial bias also occurs in our healthcare system. That racial bias—whether conscious or not—can lead to prejudicial behavior.

And while we have made tremendous progress from the days of the Civil War, we still have work to do; to eliminate these disparities and to discover that regardless of the color of our skin, we are human and deserve grace.

Life Support by Stephanie Summerfield.
```

### Performance text (classify this)

```text
NOTE: Narrator should be African American

(Pg 358-365) It was the 1980s and I finally got up the nerve to look for a job. I got excited because the new thing was to have home health-care aides -- people who would sit with the elderly, feed them, give them their medicine and things like that. So when I opened up the newspaper and saw it, it was a hallelujah moment: Ahh! Sitter! I can do this job. What better job than just sitting? So I went to this temp agency called Health Skills. They gave me my first assignment. On the first day, I walk up to this house on cinder blocks in a working-class, all-white neighborhood. I knock on the door, and I see this woman peer out.

WOMAN: (peering through a partially open door and in blatant disgust) Go away! And so I say, "Hi, ma'am. I'm here from Health Skills. I'm here because you needed a sitter." I think that will help, but she says.

WOMAN: Go away! I don't want you here! She goes to the phone, and she calls the company! I'm standing outside and I'm waiting on her to get through this phone call, and finally she just slams down the phone, comes to the door and lets me in.

So I am walking through this house. You have to walk through the living room and kitchen to get to the bedroom, so you can see all the way through the house. Well, I get to the bedroom, and I am hit with this horrible stench. The air is filled with the smell of bile, and there's this man lying on a hospital bed in an otherwise normal-looking bedroom. He has breathing tubes and IVs and he's completely unconscious. And the breathing machine is working, and it's pumping up this brown mousse out of his mouth and nose. It kind of looks like styling foam. (looking at a healthcare chart) And what I discover is that this man is dying of cir-rhosis of the liver. In the final stages the liver and bile are breaking down, building up as fluid in the lungs, and the body is trying desperately to get rid of that so that he can breathe. So that's what's coming up out of his mouth and nose. Every fifteen minutes this process goes through, and I have to stand there and clean it up. So me being an overachiever and wanting to do well, I throw myself into the job. This woman who let me in is very aggressive. She doesn't say anything, but she's not very kind to me. So we clean up this man, and there's nothing for me to do but to just wait. So I say, "Maybe I should just sit down." And this woman, she's staring at me with hate pouring from her eyes. I don't know what I've done. I've just done my job, and I've done it pretty well. So I look at her, and I say, "Look, I can get this, I'm fine now."

She turns around, doesn't say a word to me, and walks right back down that hallway and sits on the couch. And even though she's sitting across from the TV, she's sitting in profile so she can see down the hallway, and she's staring at me -- she's got her eye on me. I sit down, and I'm looking around the room, and it's filled with this nice Shaker furniture, and it's got a floor-to-ceiling Confederate flag behind the man's bed. And I have to tell you, it takes a little while for the gears to kick in. I'm taking in the furniture -- there's a lovely armoire, and I'm so Martha Stewart, I'm into decorating and everything. And they have a little coat tree, and on the coat tree there's this beautiful robe. Kind of like a church robe except it's white, and it has a round circle with a white cross on it and a hood. But I'm still not grasping what's happening because I am totally amazed by this hood and the buttonhole stitching around the eyes of the hood. I was like, You know, maybe I should take up sewing ... And then I looked down the hallway, and the woman is still looking at me. So I thought, OK. I'm just going to sit here. And oh! There's a table and a book. Hooray! So I'm flipping through the book, and it looks like a Bible because it's got gilt lettering on the outside, and I thought, Oh great! It's a Bible! I know that! Corinthians, Ephesians; Proverbs for wisdom, Psalms if you're sad. So I'm trying to look for something peaceful and happy to read, and instead I come across this horrible-looking manifesto that talks about the superiority of the white race and how we need to annihilate everyone but them for their own safety. And I shut the book. And it finally hits me that I am in the home of an honest-to-Ggod Klansman, and I am black. And I look down the hallway at this woman, and she's looking back at me like, Do you get this now? And I'm like, Oh shit! And then right at this moment, the mousse starts coming up out of this man's mouth and nose again, and I think, Thank God! I've got something to do, I've got something to do! So I run over to this man, and I'm cleaning him up, very calm and professional - - cleaning, cleaning! But inside my mind, I'm like, Oh my God! I'm so glad he's not conscious, he probably hates me and, you know, I don't hate him personally, but my people hate him. And I'm feeling all this anxiety, and then I think, You cannot do this right now be-cause you need a job, OK? You do not have time for a Rosa Parks moment. You have to get through this. OK? I'm an overachiever. I can do this. I am not going to let a little racism stand in my way. I am going to get this done, I am going to do it well, I am going to get an A+, I am going to get a check, and I am going to get the *hell* out of here, OK!?! And that is exactly what I did. I did it every fifteen min-utes for four hours that day. For four hours. And I came back the next day. She opened the door, and she wasn't quite as unfriendly. I guess she recognized that I was not going to kill the man. And I came back the third day -- she was so tired, and I realized that this woman was not getting any rest unless I was there to take care of him; that nobody would come to save her, or help her, which was really sad. By the fourth day, she just came to the door and im-mediately lay down, and I did the job. I had to wake her up at the end of that four hours. And then on the fifth day, the temp agency called me (picks up the phone), and said, "We don't need you anymore." The man had passed away. But the lady had called to leave me a message. She wanted me to know that I'd given him the best care that he'd had since he left the hospital, and the most peace and rest that she got was when I was there, and she wanted to thank me personally. And I thought, Man, that is amazing. And she left me a tip, which the temp agency would not let me keep. But a few months later, I realized I really did get a tip and it was this: the knowledge that we had come together, she and I, these two incredibly desperate people in a highly charged situation. And it could have been a train wreck; it could have been a mess. But instead, we came together, and our lives touched, and in that touching we changed the trajectory of our lives just a little bit. I'd like to think that I changed the way that she thought about people of color -- that we weren't whatever it was that those people were teaching her, and that she might reconsider her prejudices. And for myself, I got a job that I desperately needed. I had left Indiana to change the world. And I didn't; I couldn't. But I realized that even if I couldn't change the world, I could change the little piece of the world that I was in, and that was enough for me.
```

---

## IC-2076: Lilly’s Purple Plastic Purse

- Title: Lilly’s Purple Plastic Purse
- Author (byline): Kevin Henkes
- Work: Not specified
- Publisher: Greenwillow Books
- Publication date as stated: Aug 1996
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, LILLY, MR. SLINGER, MOTHER, FATHER, KIDS
- Teaser before the introduction: Yes
- Spoken words (computed): 1050
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kevin Henkes
ISBN: 978-0688128975
Publisher: Greenwillow Books
Date (Month/Year): Aug 1996
```

### Introduction (context only: never use it for content warnings)

```text
Raise your hand if you like school . . . . or if you LIKED school when you were a kid. I thought not . . . not many kids wake up early in the morning excited about the prospect of a day of learning and enlightenment . . . or to go sit in a stuffy classroom and be bored! ALL. DAY.

In this story you’ll meet a little girl who loves school because she has a fantastic teacher . . . Fantastic, that is, until the day he takes away Lilly’s Purple Plastic Purse by Kevin Henkes.
```

### Performance text (classify this)

```text
Interper should create a distinct character for each character, including the narrator.

NARRATOR: Lilly LOVED school.

LILLY: I Love School!

NARRATOR: She loved the pointy pencils. (pantomime Lilly sharpening a pencil) She loved the squeaky chalk (pantomime Lilly screeching the chalk down the board and it hurting her ears, but she LIKES it). And she loved the way her boots went clickety-clack down the long, shiny hallway

(pantomime walking down the hallway happily). Lilly loved the privacy of her own desk

LILLY: (opensthe lid of an old school desk and peeksover the edge as if she has a secret inside) – Mine!

NARRATOR: She loved the fish sticks and chocolate milk every Friday in the lunchroom!

LILLY: (drinks nosily through a straw) Straws make everything taste better!

NARRATOR: And, most of all, she loved her teacher, Mr. Slinger.

LILLY: (Holds up flowers) For you!

NARRATOR: Mr. Slinger was sharp as a tack. (Lilly interrupts . . . Or as a pencil! And laughs. Narrator gives her a stern look) He wore artistic shirts. (pantomime Mr. Slinger selecting a shirt and putting it on) He wore glasses on a chain around his neck. (pantomime putting glasses on and waving at random people) And he wore a different colored tie for each day of the week.

MR. SLINGER: (holding up different ties) No . . . No . . . . Yes!

LILLY: WOW!

NARRATOR: That was just about all she could say.

LILLY: WOW!

NARRATOR: And he always provided the most tasty snacks –

MR. SLINGER: Curly, crunchy and cheesy! (Hold up a snack, Lilly takes it and savors it)

LILLY: I wanna be a teacher when I grow up!

NARRATOR: At home, Lilly pretended to be Mr. Slinger!

LILLY: I am the teacher (speaking to her baby brother) Listen up! Teacher know everything!

MOTHER: What’s with Lilly?

FATHER: I thought she wanted to be a surgeon or an ambulance driver or a diva.

MOTHER: It must be because of her new teacher, Mr. Slinger.

FATHER: WOW!

NARRATOR: Said her father. That was just about all he could say.

FATHER: WOW

NARRATOR: When students had free time, they were permitted to visit the Lightbulb Lab in the back of the classroom. There they expressed their ideas creatively through drawing and writing. Lilly went often and had many ideas. She drew pictures of Mr. Slinger and wrote stories about Mr. Slinger. And then during sharing time, she would share her creations with the rest of the class.

LILLY: And at the very last second, Mr. Slinger saved the cold, starving, elderly . . . .

MR. SLINGER: WOW

NARRATOR: said Mr. Slinger. That was about all he could say.

MR. SLINGER: WOW

NARRATOR: When Mr. Slinger had bus duty, Lilly stood in line. Even though she didn’t ride the bus. And Lilly raised her hand more than anyone else in the class. Even if she didn’t know the answer.

LILLY: (frantically raising her hand) Call on me . . . please, please!!!

NARRATOR: And Lilly volunteered to stay after school to help lap erasers.

LILLY: (clapping erasers – clap, clap, cough, cough) I wanna be a teacher when I grow up!

MR. SLINGER: Excellent choice!

NARRATOR: [One] Monday morning, Lilly showed up to school especially happy. She had gone shopping with her Grammy over the weekend and had a new pair of movie star sunglasses, complete with glitter and a chain like Mr. Slingers. She had 3 shiny quarters, and best of all; a brand new purple plastic purse that played a jaunty tune when it was opened. (pantomime Lilly admiring and opening a purse and then moving to the music)

LILLY: I can’t wait to show everybody!

MR. SLINGER: Not now, Lilly, Listen to our story.

NARRATOR: Lilly had a hard time listening. Lilly really wanted to show everyone

MR. SLINGER: Not now. Let’s be considerate of our classmates.

NARRATOR: Lilly had a hard time being considerate.

MR. SLINGER: Not now, Lilly – Wait until recess or Sharing time. (pantomime Mr. Slinger sliding his glasses down his nose and giving a disapproving look)

NARRATOR: Lilly could not wait.

LILLY: “Look!” (whispers Lilly fiercely) “Look, everyone! Look what I’ve got!”

NARRATOR: Everyone looked. Including Mr. Slinger. He was not amused.

MR. SLINGER: I’ll just keep your things at my desk until the end of the day. They will be safe there and then you can take them home.

LILLY: I feel like crying! My glasses . . . gone. My quarters . . . gone. My purple plastic purse . . . GONE!!

NARRATOR: Lilly longed for her purse all morning. She was even too sad to eat the snack Mr. Slinger served before recess. That afternoon, Lilly went to the Lightbulb Lab. (pantomime Lilly walking sadly and dejectedly). She was still very sad. And then she became angry. (Lilly’s walk changes from sad to stomping). And then she became furious. She drew a picture of Mr. Slinger (pantomime Lilly drawing with an evil smile and making faces)

LILLY: Mr. Big, Fat, Mean, Stealing Teacher . . . wanted by the FBI. PS: I do not want to be a teacher when I grow up.

NARRATOR: Right before the last bell rang, Lilly sneaked the drawing into Mr. Slinger’s book bag. (Lilly pantomimes this narration.) Then when all the students were buttoned, zipped, tied and ready to go home, Mr. Slinger strolled over to Lilly and gave her purple plastic purse back.

MR. SLINGER: It’s a beautiful purse. Your quarters are nice and jingly. And those glasses are absolutely fabulous. You may bring it back to school as long as you don’t disturb the rest of the class.

LILLY: (pouting) I don’t want to be a teacher when I grow up.

NARRATOR: And Lilly marched out of the classroom. On the way home, Lilly opened her purse. Her glasses and quarters were inside. And so was a note from Mr. Slinger.

MR. SLINGER: Today was a difficult day. Tomorrow will be better.

NARRATOR: There was also a small bag of snacks at the bottom of the purse.

LILLY: Oh man! I feel awful! I feel simply terrible!

NARRATOR: Lilly rushed home and told her mother and father everything. Then instead of watching her favorite cartoons, she decided to sit in the “uncooperative chair.”

LILLY: I’ll stay here a million years for Mr. Slinger. Why does everything always happen to me. I’m really, really, really sorry. I’ll draw a new picture of Mr. Slinger and write a new story too! . . . . . So everyone forgave Lilly including her especially incredible teacher and the sun smiled its face done on everyone and everything including the bugs and the worms . . . . The end.

NARRATOR: Lilly’s mother wrote a note. And Lilly’s father baked some tasty snacks for Lilly to take to school the next day. The next morning Lilly showed up early to school.

LILLY: Um . . . Mr. Slinger? These are for you because I’m really, really, really, really, really, really, really sorry.

NARRATOR: Mr. Slinger read the story and looked at the picture and sampled the snacks.

MR. SLINGER: WOW

NARRATOR: Said Mr. Slinger. That was about all he could say.

MR. SLINGER: Wow . . . well, what should we do about this?

LILLY: (Sheepishly) Mr. Big, Fat Stealing . . . can we just throw it away?

MR. SLINGER: Excellent idea.

NARRATOR: [That afternoon] During Sharing Time, Lilly demonstrated the many uses and uique qualities of her purple plastic purse, her shiny quarters, and her movie star sunglasses. Then she did a performance using them as props.

LILLY: (dancing) It’s called interpretive dance!

NARRATOR: Then Mr. Slinger served Lilly’s snack to the class.

MR. SLINGER: What do you guys wanna be when you grow up?

KIDS: A Teacher!

NARRATOR: But Lilly’s response was the loudest. On her way home Lilly thought to herself.

LILLY: Mr. Slinger was right. Today was a better day. And I really do want to be a teaher. This when I don’t’ want to be a surgeon, or an ambulance dirve, or a diva or a scuba diver, or a dancer or a . . . . .
```

---

## IC-2077: The Lorax

- Title: The Lorax
- Author (byline): Theo Geisel (aka Dr. Seuss)
- Work: Not specified
- Publisher: Random House Books
- Publication date as stated: Aug 1971
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, ONCE-LER, LORAX
- Teaser before the introduction: Yes
- Spoken words (computed): 1397
- Already set (do not supply): none

### Source block (context only)

```text
Author: Theo Geisel (aka Dr. Seuss)
ISBN: 978-0394823379
Publisher: Random House Books
Date (Month/Year): Aug 1971
```

### Introduction (context only: never use it for content warnings)

```text
When Dr. Seuss gets serious, you know it must be important. Published in 1971, and perhaps inspired by the "save our planet" mindset of the 1960s, The Lorax is an ecological warning that still rings true today amidst the dangers of clear-cutting, pollution, and disregard for the earth's environment. In The Lorax, we find what we've come to expect from the illustrious doctor: brilliantly whimsical rhymes and delightfully original. But there is also something more--a powerful message that Seuss implores both adults and children to heed.

The Lorax by Theo Geisel (aka Dr. Seuss)
```

### Performance text (classify this)

```text
NARRATOR: At the far end of town where the Grickle-grass grows and the wind smells slow-and-sour when it blows and no birds ever sing excepting old crows. . . is the Street of the Lifted Lorax. And deep in the Grickle-grass, some people say, if you look deep enough you can still see, today, where the Lorax once stood just as long as it could before somebody lifted the Lorax away.

NARRATOR: What was the Lorax? And why was it there? And why was it lifted and taken somewhere from the far end of town where the Grickle-grass grows? The old Once-ler still lives here. Ask him. He knows.

ONCE-LER:Now I'll tell you, how the Lorax got lifted and taken away. . . It all started way back. . . such a long, long time back. . . Way back in the days when the grass was still green and the pond was still wet and the clouds were still clean, and the song of the Swomee-Swans rang out in space. . one morning, I came to this glorious place. And I first saw the trees! The Truffula Trees! The bright-colored tufts of the Truffula Trees! Mile after mile in the fresh morning breeze. And under the trees, I saw Brown Bar-ba-loots frisking about in their Bar-ba-loot suits as they played in the shade and ate Truffula Fruits. From the rippulous pond came the comfortable sound of the Humming-Fish humming while splashing around. But those trees! Those trees! Those Truffula Trees!

All my life I'd been searching for trees such as these. The touch of their tufts was much softer than silk. And they had the sweet smell of fresh butterfly milk. I felt a great leaping of joy in my heart. I knew just what I'd do! I unloaded my cart. In no time at all, I had built a small shop. Then I chopped down a Truffula Tree with one chop. And with great skillful skill and with great speedy speed, I took the soft tuft. And I knitted a Thneed! The instant I'd finished, I heard a ga-Zump! I looked. I saw something pop out of the stump of the tree I'd chopped down. It was sort of a man. Describe him?. . . That's hard. I don't know if I can. He was shortish. And oldish. And brownish. And mossy. And he spoke with a voice that was sharpish and bossy.

LORAX:(with a sneeze) Mister! I am the Lorax. I speak for the trees. I speak for the trees, for the trees have no tongues. And I'm asking you, sir, at the top of my lungs"- What's that THING you've made out of my Truffula tuft?

ONCE-LER: Look Lorax, There's no cause for alarm.

I chopped just one tree. I am doing no harm.
I'm being quite useful. This thing is a Thneed.
A Theend's a Fine-Something-That-All-People-Need!
It's a shirt. It's a sock. It's a glove. It's a hat.
But it has other uses. Yes, far beyond that.
You can use it for carpets. For pillows! For sheets!
Or curtains! Or covers for bicycle seats!"

LORAX: Sir! You are crazy with greed. There is no one on Earth who would buy that fool Thneed.

ONCE-LER: But the very next minute I proved he was
wrong.
For, just at that minute, a chap came along,
and he thought that the Thneed I had knitted was great.
He happily bought it for three ninety-eight.
(laughing at the Lorax) You poor stupid guy!
You never can tell what some people will buy.

LORAX: I repeat, I speak for the trees!

ONCE-LER: I'm busy. Shut up, if you please. I rushed 'cross the room, and in no time at all, built a radio-phone. I put in a quick call. I called all my brothers and uncles and aunts and I said Listen here! Here’s a wonderful chance for the whole Once-ler Family to get mighty rich! [They] were all knitting Theends just as busy as bees, to the sound of the chopping of Truffula Trees. Then . . . Oh! Baby! Oh! How the business did grow! Now, chopping one tree at a time was too slow So I quickly invented my Super-Axe-Hacker which whacked off four Truffula Trees at one smacker. We were making Thneeds four times as fast as before! And that Lorax? . . . He knocked on my new office door.

LORAX: I'm the Lorax who speaks for the trees which you seem to be chopping as fast as you please. But I'm also in charge of the Brown Bar-ba-loots who played in the shade in their Bar-ba-loot suits and happily lived, eating Truffula Fruits. NOW. . . thanks to your hacking my trees to the ground, there's not enough Truffula Fruit to go 'round. And my poor Bar-ba-loots are all getting the crummies because they have gas, and no food, in their tummies! They loved living here. But I can't let them stay. They'll have to find food. And I hope that they may.

ONCE-LER: I, the Once-ler, felt sad as I watched them all go. BUT . . . business is business! And business must grow I meant no harm. I most truly did not. But I had to grow bigger. So bigger I got. Then again he came back! I was fixing some pipes when that old-nuisance Lorax came back with more gripes.

LORAX: (coughing) I am the Lorax (sneezing, snuffling) Once-ler! You're making such smogulous smoke! My poor Swomee-Swans. . . why, they can't sing a note! No one can sing who has smog in his throat. And so - please pardon my cough – they cannot live here. So I'm sending them off. What's more, let me say a few words about Gluppity- Glupp. Your machinery chugs on, day and night without stop making Gluppity-Glupp. Also Schloppity-Schlopp. And what do you do with this leftover goo?. . . I'll show you. You dirty old Once-ler man, you! You're glumping the pond where the Humming-Fish hummed!

No more can they hum, for their gills are all gummed. So I'm sending them off. Oh, their future is dreary. They'll walk on their fins and get woefully weary in search of some water that isn't so smeary.

ONCE-LER: And then I got mad. I got terribly mad. (yelling) Now listen here, Dad! All you do is yap-yap and day, 'Bad! Bad! Bad! Bad!' Well, I have my rights, sir, and I'm telling you I intend to go on doing just what I do! And at that very moment, we heard a loud whack! From outside in the fields came a sickening smack of an axe on a tree. Then we heard the tree fall. The very last Truffula Tree of them all! No more trees. No more Thneeds. No more work to be done. So, in no time, my uncles and aunts, everyone, all waved me good-bye. They jumped into my cars and drove away under the smoke-smuggered stars. Now all that was left 'neath the bad-smelling sky was my big empty factory. . . the Lorax. . . and I. The Lorax said nothing. Just gave a glance. . . just gave a very sad, sad backward glance. . .

as he lifted himself by the seat of his pants.
And I'll never forget the grim look on his face
when he heisted himself and took leave of this place,
through a hole in the smog, without leaving a trace.
And all that the Lorax left here in this mess
was a small pile of rocks, with the one word. . .
UNLESS. (long pause)
Whatever that meant, well, I just couldn't guess.
That was long, long ago.
But each day since that day I've sat here and worried
and worried away.
Through the years, while my buildings have fallen apart,
I've worried about it with all of my heart.
But now. . . Now that you're here, the word of the Lorax
seems perfectly clear.
UNLESS someone like you cares a whole awful lot,
nothing is going to get better . . . It's not.
SO. . . Catch! (he tosses something down)
It's a Truffula Seed. It's the last one of all!
You're in charge of the last of the Truffula Seeds.
And Truffula Trees are what everyone needs.
Plant a new Truffula. Treat it with care.

Give it clean water. And feed it fresh air. Grow a forest. Protect it from axes that hack. Then the Lorax and all of his friends may come back.
```

---

## IC-2078: Lost at C

- Title: Lost at C
- Author (byline): Jean Shepherd
- Work: A Fistful of Fig Newtons
- Publisher: Doubleday
- Publication date as stated: 1981
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2466
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jean Shepherd
Book: A Fistful of Fig Newtons
ISBN: 978-0385175036
Publisher: Doubleday
Date (Month/Year): 1981
```

### Introduction (context only: never use it for content warnings)

```text
Lost at C by Jean Sheperd
```

### Performance text (classify this)

```text
A wave of numbness surged through my body with stunning force. At last I knew what it felt like to be sitting with that brass hat on your skull . . . with those straps around your ankles . . . as the warden pulls the big switch. Out of the corner of my eye I caught the glint of Mr. Pittinger's horn-rims and the ice-blue ray from his left eye. As the giant equation loomed on the blackboard, my life unreeled before my eyes. I was finished. Done. It had all come to this. Somehow I had always known it would . . . I was . . .

It all started in first grade at the Warren G. Harding School where I was one among a rabble of sweaty, wrestling, peanut-butter-and-jelly-sandwich eaters. But it was not until the end of the third month of school that I became dimly aware of a curse that would follow me throughout my life. Along with Chester Woczniewski, Helen Weathers and poor Francis Xavier Zambarbieri, I was a member of the alphabetical ghetto that sat in the back of the classroom. Medical science is now beginning to realize that those of us at the end of the alphabet live shorter lives, sweat more and are far jumpier than those in the Bs and Es and even the Ms and Ls. People at the tail end of the alphabet grow up accepting the fact that everybody else comes first.

Kids in the front of the classroom didn't know the meaning of danger. Ace test takers, they loved nothing more than to display their immense knowledge by waving their hands frantically even before questions were asked. They were the smartasses who went on to become corporation presidents, TV talk-show guests and owners of cabin cruisers.

We in the back of the classroom followed a different path. First of all, it was imperative never to be caught out in the open; if possible, not to be seen at all. Each one of us evolved his own methods of survival. Helen Weathers was so fat, her profuse perspiration under stress so pathetic that the teacher never had the heart to call on her. Woczniewski hid behind books, which worked all right until he hid behind Plastic Man Meets the Thing one morning. Zambarbieri, a devout Catholic, relied almost exclusively on prayer. I made it a point to wear bland-colored clothes, the better to blend into the background. I learned to weave my body from side to side, dropping a shoulder here, shifting my neck a few degrees to the right there, with the crucial object in mind of always keeping a line of kids between me and the teacher's eagle eye.

The [second] and possibly most important, tactic of classroom survival is thought control. When danger looms, it is necessary to repeat silently, with intense concentration, the hypnotic command "You will not call on me, you will not call on me," sending out invisible waves of powerful thought energy until the teacher's mind is mysteriously clouded.

Woczniewski, Helen Weathers and I, as well as poor old Zambarbieri, sat on shore as the deepening river of education flowed by us unheard, unseen. Warren G. Harding was widely known, during the dark ages when I was attending it, for being an "advanced" school, and actual tests were very rare. This worked in beautifully with our survival techniques and made it possible for me and my band of fellow ignoramuses to slide by year after year undetected.

The years passed, punctuated by occasional tight squeaks, but my true identity as a faker was never really in danger of exposure. And finally the big day came. On a glorious sun-drenched morning, graduation day arrived. I had made it. I got my diploma. It was official. In September I would be a full-fledged high school kid.

[Summer flew by until FINALLY September arrived] I had lain in bed making plans the night before. I would grab the front seat in every class and listen to every word. No longer would I duck and dodge behind a screen of kids. That was all behind me. Mentally I crouched at the mark, waiting for the starter's gun to send me flying down the track ahead of the pack. The bus rolled up before nirvana and we piled out.

A blind torrent of fear washed over me. For a while, I had been one of the truly big men at Warren G. Harding, and now I was nothing. Clinging to my lunch bag with a sweaty hand, I hunted frantically for a familiar face, but . . . BRRRR-INNNGGG! Great staircases with rivers of kids streamed in all directions. My card read REPORT TO ROOM 220. Kids all around me hollered and laughed back and forth. They all seemed to know one another. I had never felt so alone. Figuring astutely that room 220 had to be on the second floor, I joined the torrent raging upward. I tried to read the numbers on doors as I was swept onward like a salmon in the spawning season: 205, 207, 214, 218 - 220! My home room.

A plump lady with gray clothes, hair and face sat like an enigmatic Buddha at a green metal desk at the head of the room. She glanced up and peered at me coldly through her rimless glasses. "Your card, please," she snapped in a flat voice. I handed it over. "Take that seat there back of Rukowski. He's the one in the purple sweater." I walked down between the aisles of alien faces to my seat. It was, of course, in the next-to-the-last row. It would be mine for the next four years.

"Freshmen, this "is your first day in high school. You are no longer in grade School. If you work hard, you will do well. If you don't, you 'will regret it. You are here to learn. You are not here to play. Remember this and remember it well: What you do here will follow you all through life." She paused dramatically. "Your first class will begin in five minutes. Any questions?" No one raised a hand. I sat there in silence, staring at my blue card, lost in dark thoughts, when the bell rang out again. The starting gate had opened. As the crowd surged around me, I struggled to read my program card. All I could make out was room 127. I had only a minute to make it, so I battled my way down a flight of stairs. Then: 101, 105, 109, 112, 117- 127, just in time.

A tall, square man stood motionless at the blackboard. He had a grim blue jaw and short, kinky, black crewcut hair. His eyes were tiny ball bearings behind glasses with thick black rims. He wore a dark, boxy, suit that looked like it was made of black sandpaper. The bell rang and the door closed behind us.

"All right. Settle down. Let's get organized." The man's voice had a cutting rasp to it, like a steel file working on concrete. "We sit alphabetically in this class. A's up here in front to my right. Get going." I trudged behind Helen Weathers toward the dim recesses in the back of the classroom. It was about a quarter of a mile to the front of the room, but I sat bolt upright in my seat, determined to catch every word the teacher said. "Class, my name is Mr. Pittinger." And I still had no idea what he taught. I would soon find out.

He turned, picked up a piece of chalk and began to scrawl huge block letters on the blackboard. A-L - the chalk squeaked decisively - G-E-B-R-A. Algebra? What the hell is that? "Algebra is the mathematics of abstract numbers." I gulped as I wrote this down.

"I will now illustrate." Pittinger printed a huge Y on the blackboard and below it an enormous X. "If Y equals five and X equals two, what does the following mean?" He wrote out: X + Y = ? Black fear seized my vitals. How could you add Xs and Ys? I had enough trouble with twos and threes. Already the crowd in front of the room were waving their hands to answer Pittinger's question. I sank lower in my seat, a faint buzzing in my ears. I knew it was all over. Helen Weathers had flung up a thin spray of sweat. And from behind me I could hear the faint, steady click of Zambarbieri's rosary. Second by second, minute by minute, eon by eon, that first algebra class droned on. I couldn't catch another word that was said, and by the time Mr. Pittinger wrote the second equation on the board, I was bobbing and weaving like a cobra and sending out high-voltage thought rays. A tiny molten knot of stark terror hissed and simmered in the pit of my stomach. I realized that for the first time in my school life, I had run into something that was completely unlearnable, and there was no way to fake it.

That night, sleep did not come easily. In fact, it was only the first of many storm-tossed nights to come as, algebra class by algebra class, my terror grew. All my other subjects - history, English, social studies - were a total breeze. My years of experience in fakery came into full flower. In social studies, for example, the more you hoked it up, the better the grades. On those rare occasions when asked a question, I would stand slowly, with an open yet troubled look playing over my thoughtful countenance. "Mr. Harris, sir," I would drawl hesitantly, as though attempting to unravel the perplexity of the ages, "I guess it depends on how you view it-objectively, which, naturally, is too simple, or subjectively, in which case many factors such as changing environment must be taken into consideration...." I would trail off. Mr. Harris, with a snort of pleasure, would bellow: "RIGHT! There are many diverse elements, which...," After which he was good for at least a 40 minute solo.

Every morning at 8:35, however, was another story. I marched with leaden feet and quaking bowels into Mr. Pittinger's torture chamber. By the sixth week I knew, without the shadow of a doubt, after all these years of dodging and grinning, that I was going to fail.

Fail! There was no question whatsoever. True, Pittinger had not yet been able to catch me out in the open, since I was using every trick of the trade. But I knew that one day, inevitably, the icy hand of truth would rip off my shoddy facade and expose me for all the world to see.

I stumped into algebra class [day after day, month after month] feeling distinctly like the last soul aboard the Titanic as she was about to plunge to the bottom. [I remember it like it was yesterday . . . it was late May] The class began, Pittinger's chalk squeaked, hands waved. The sun filtered in through the Venetian blinds. A tennis ball pocked back and forth somewhere over a net. My knot of fear, by now an old friend, sputtered in my gut. True, I had avoided being called on even once the entire year, but it was a hollow victory and I knew it. Minute after minute inched slowly by as I ducked and dodged, Pittinger firing question after question at the class. Glancing at my Pluto watch, I noted with deep relief that less than two minutes remained before the bell. It was then that I made my fatal mistake, the mistake that all guerrilla fighters eventually make: I broke cover.

For years, every fiber of my being, every instant in every class, had been directed at survival. On this fateful Wednesday, lulled by the sun, by the gentle sound of the tennis ball, by the steady drone of Pittinger's voice, by the fact that there was just two minutes to go, my mind slowly drifted off into a haze of daydream.

(in an echoing intonation similar to teacher’s voices in Charlie Brown) [WAA, WHAA WAA WAA] For a stunned split second, I thought I'd been jabbed with an electric cattle prod. Pittinger's voice, loud and commanding, was pronouncing my name. He was calling on me! Oh, my God! With [only] a minute to go, he had nailed me.

"Come to the board, please. If X equals two and Y equals minus one, what is the value of C in this equation?" snapped Pittinger. In a stupor of primal fear, I felt my legs clumping up the aisle. On all sides the blank faces stared. At the board - totally unfamiliar territory to me - I stared at what seemed like the first equation I had ever seen. It was well over a yard and a half long and was lacerated by mysterious crooked lines and fractions in parentheses, with miniature twos and threes hovering above the whole thing like tiny barnacles, and Xs and Ys were jumbled in crazy abandon. Pittinger stood to one side, arms folded. He had been playing with me all the time. He knew!

I glanced back at the class. It was one of the truly educational moments of my life. The entire mob was grinning happily, licking their chops with joyous expectation of my imminent crucifixion.

"The value of C, please," said Pittinger. Desperately, I tried to come up with a number - any number. I couldn't remember my name. "The answer, please."

"Three," I muttered.

"What's that?" barked Pittinger.

"Three!" I blurted.

Pittinger staggered backward, his glasses jolted down to the tip of his nose. "How the hell did you know that?" he bellowed hoarsely, his snap-on bow tie popping loose in the excitement. The class was in an uproar. It was a true miracle. I had walked on water. Instantly, the old instincts took over. In a cool, level voice, I answered Pittinger's rhetorical question.

"Sir, I used empirical means to arrive at the answer."

He paled visibly and clung to the chalk trough for support. On cue, the bell rang out. The class was over. With a swiftness born of long experience, I was out of the room even before the echo of the bell had ceased. A legend had been born.

The next morning, Thursday, I swaggered into algebra class with head high. Even Jack Morton, the biggest smartass in the class, said hello as I walked in. Mr. Pittinger, his eyes glowing with admiration, smiled warmly at me. "Hi, Pit," I said with a casual flip of the hand. We abstract mathematicians have an unspoken bond. Naturally, I was not called on during that period. After all, I had proved myself beyond any doubt. [X+Y = 3 . . . and I never used Algebra again]
```

---

## IC-2079: The Machine

- Title: The Machine
- Author (byline): Chris Kluwe
- Work: If This Goes On (Pg 201-207)
- Publisher: Parvus Press, LLC
- Publication date as stated: March 2019
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, LUPE, MARCUS, BRODY, COMPANY PRESIDENT, VOICE OVER LOUDSPEAKER, ICE OFFICER 1, ICE OFFICER 2
- Teaser before the introduction: No
- Spoken words (computed): 1281
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Kluwe
Book: If This Goes On (Pg 201-207)
ISBN: 978-0999784211
Publisher: Parvus Press, LLC
Date (Month/Year): March 2019
```

### Introduction (context only: never use it for content warnings)

```text
What does the future hold for America? Already we are seeing a rise in mega-corporations – Amazon and Google -- run by multi-billionaires. The divide between the haves and have nots is growing and those in power (those with money) seem to care little for the plight of those without. Our homeless population is exploding and if you are Latino – Well, the perception is that you are not welcome here, regardless of your legal status.

We are losing our humanity and will soon be crushed by. . . The Machine, a story by Chris Kluwe
```

### Performance text (classify this)

```text
(Scene opens with a pantomime: Marcus shifting on his feet, reaching out to push buttons or twist dials – he’s zoned out)

NARRATOR: Marcus stared at the control panel with aching eyes; its hateful collection of flashing lights reduced to nothing more than blurs of meaningless color. He hadn't gotten enough sleep, again, and today was another mandatory sixteen-hour shift.

LUPE: "Marcus? Marcus!"

MARCUS: (jerking upright) Yeah, Lupe. I'm here.

LUPE: Ay Dios mio, I thought you were going to pull a Deion, get an arm torn off. (she twists dials on her own panel) You gotta stay awake, Marcus. Those books will be the death of you.

NARRATOR: Lupe twisted a dial on her own panel, taking care not to step out from the barely visible grey-on-grey markings delimiting her safety zone. All around them, mechanical arms, like the severed limbs of some gigantic arachnid, swooped through the air, carrying packages to unknowable destinations. Heart hammering, now fully awake, Marcus turned back to his own panel, where a flurry of lights demanded his attention. Laboriously, he flipped the switches he'd been not-quite-trained to flip, twisted the dials he still didn't know the meaning of.

MARCUS: (muttering to himself) Just make it through. The books are waiting.

NARRATOR: His panel switched over to the pale, pinched face of his supervisor, Brody, glaring out at him.

BRODY: (Glaring and screaming) You're falling behind! Do you want this job? Because there are plenty of people who want a job and are willing to work for it!"

MARCUS: Ye-yes, Mr. Brody, I . . .

BRODY: (livid) That's 'Supervisor Brody, you stupid wetback! Just get back to work.

NARRATOR: The screen cut out, leaving Marcus staring at even more flashing lights. Numbly, he resumed putting them out, one at a time. Hours later only two lights remained, the rest having been banished to whatever hell they inhabited between their appearances. He reached for a knob with a leaden arm then nearly swore as the panel switched into fullscreen mode once again. On it, the benign face of an old, bald man stared out.

COMPANY PRESIDENT: Great work, everyone! We here at the Amazon-Wells Fargo-Academi family are fighting hard for your rights in these turbulent times. And to recognize everyone's diligence, I've approved a ten-credit bonus for every worker this month. Don't spend all of it in the company store at once! And finally, don't forget reviews for my new book, 'The Self-Made Man, are due by the end of the week!

NARRATOR: More hours passed, and then (blaring noise) - - the end of shift signal. His entire body aching, Marcus shuffled across the factory floor towards the exit.

Newer faces, not yet battered by years on the factory floor, flowed by in the opposite direction, scrambling to get to their areas on time.

VOICE OVER LOUDSPEAKER: (Toneless) Ten seconds until factory operations resume. This is your federally mandated safety warning.

NARRATOR: Marcus and Lupe picked up their pace, now on the verge of running. They reached the exit door as clanging snarls of metal on metal announced the arms lurching into motion once more. A crashing impact joined the cacophony, (a brief scream) Lying sprawled halfway across the safety line was a young man, his right arm a mangled ruin. Before they could help him, another mechanical appendage whipped through, slamming the boy's body against the wall with a sodden thump. Blood pooled beneath his unmoving form, slowly spreading across the floor. Marcus hadn't even known the kid's name. A harried-looking woman appeared, her grey suit almost the same shade as her skin, her hands clutching a clipboard.

BETSY from HR: Tsk, tsk (shaking her head and chewing on her lower lip she holds out her clipboard and speak robotically) Sign here, here, and here.

LUPE: (a hint of rebellion) What are we signing?

BETSY from HR: Statements of witness that the company followed standard safety procedures. Abnegation of class-action rights. It's all covered in your contract.

NARRATOR: Two men in hazmat suits were rolling the body into a black plastic bag.

MARCUS: And if we don't?

BETSY from HR: Then you lose your job, we sue you, we pull your citizenship, and we get the government to deport you. Any other questions?

NARRATOR: A blazing fire from the very core of the world bubbled up in Marcus' stomach, a pillar of rage that seemed to have no beginning or end. He clenched his fists, veins standing up along the backs of his hands. Just as it seemed impossible not to throw himself at the woman, he felt Lupe pulling him away. She dragged him out of the factory to the security checkpoint.

LUPE: (whispering) You crazy pendejo. You trying to get killed?

MARCUS: (letting out a long breath and still filled with rage) They treat us like shit, Lupe. They don't care if we die on the floor. What's it matter if they kill me for taking a stand?

LUPE: (shaking her head) The difference is, we're still alive. Besides, if you don't have a job, ICE is gonna come for you.

MARCUS: (shrugging) ICE is gonna come for us anyway. Having a job, being a citizen, that don't matter anymore. We're the wrong color, Lupe. Nothing we can do to change that.

LUPE: (Scowling) You read too much. Still, though. We got a job.

MARCUS: Doing what, Lupe? They ain't teaching us anything they couldn't teach a rabbit. 'Here's a red light, twist the green dial.' 'Here's a blue light, flip the orange switch.' How are we supposed to be anything more than cogs in their machine? (yawning) Only another mile to the bus stop.

NARRATOR: They continued on in silence. The chirp of crickets gained ground in their battle against the incessant flow of the freeway as rush hour died away. Then the sound of tires crunching on gravel came from behind, and a bright light.

ICE OFFICER 1: Freeze! Don't move! Hands where we can see them! Turn around! On your knees!

NARRATOR: The two complied in tense silence, squinting against the spotlight's harsh glare. Making exaggerated, deliberate movements, they raised their arms and clasped their hands over their heads; a familiar position.

LUPE: (whispering) Pinche ICE. Be cool.

NARRATOR: The two men approached with their hands on holstered pistols. Mirrored sunglasses hid their eyes, despite the late hour.

ICE OFFICER 2: (caressing the butt of his gun) What are you two doing out here? Not looking for trouble, are we?

LUPE: (meekly, keeping her eyes down) We're just heading home from work, sir. Our bus stop isn't very far.

ICE OFFICER 1: (laughing) You hear that, George? Taking the bus. Like we haven't heard that before. Let's see some ID. Slowly now.

NARRATOR: Marcus reached into his pocket and drew forth a laminated strip of state-mandated identification. The agent scowled at it, then tossed it into the dirt at Marcus' knees.

LUPE: (patting her pockets slowly at first, then with increasing desperation) I-I must have left it at the factory. Por favor, if we can just go ba . . .

ICE OFFICER 2: (mocking in a singsong voice) Por favor, por favor. Looks like we bagged us another illegal, Jim.

MARCUS: (angrily) She's an American citizen. Just like you and me!

NARRATOR: The agent stepped closer, then lashed out with his fist. Marcus found himself on his back, pain blossoming in his jaw and with the taste of copper in his mouth.

ICE OFFICER 1: (Snarling) Without papers, she's whatever we say she is. And right now, I say she's an illegal. What you gonna do about it, amigo? (unholstering his gun) Think you' re some sort of hero, amigo? Think you can outrun a bullet?

ICE OFFICER 2: (Dragging Lupe to her feet) C'mon, George, let's roll. We got one, no need to be greedy.

LUPE: (softly crying) P-please, sir, I have children, they need me . . .

ICE OFFICER 2: (Screaming in her face) I don't give a shit about your worthless kids! Shut up and get in the car!

NARRATOR: He dragged her towards the patrol-car mounted spotlight, throwing her into the back seat.

ICE OFFICER 1: See you around, amigo. Gonna be your turn soon.

NARRATOR: And then Lupe was gone, a pair of ruby tail-lights disappearing into the unknown. Feeling numb, Marcus staggered to his feet. A car rolled by. Inside, the smiling faces of a family -- all dressed in their Sunday best, singing a popular evangelical hymn, their pale cheeks glowing rosy red. They didn't give Marcus even a glance.

Shoulders slumped and head bowed, he continued towards the bus stop. The books were waiting. If he cut another hour off his sleep, he'd have time to get through the chapter on C4 tonight.
```

---

## IC-2080: The Magic Finger

- Title: The Magic Finger
- Author (byline): Roald Dahl
- Work: Not specified
- Publisher: Puffin Books
- Publication date as stated: Jan 2009
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MRS. WINTER, NARRATOR, MR. GREGG, MRS. GREGG, PHILIP, WILLIAM, DUCK, MR. EGG
- Teaser before the introduction: Yes
- Spoken words (computed): 1455
- Already set (do not supply): none

### Source block (context only)

```text
Author: Roald Dahl
ISBN: 978-0142413852
Publisher: Puffin Books
Date (Month/Year): Jan 2009
```

### Introduction (context only: never use it for content warnings)

```text
Sounds like this story will be anti-hunting . . . and it is. But it’s so much more than that. Atticus Finch in To Kill a Mockingbird tells his daughter Scout, “You never really understand a person until you consider things from his point of view, until you climb inside of his skin and walk around in it. Well, in this case, it’s ducks instead of people and flying instead of walking, but the message is still the same – Empathy.

Empathy is not some intangible characteristic that some are born with and others are not. We all have the power to truly feel another’s struggles, if we only take the time and thought to do so.

The Magic Finger by Roald Dahl
```

### Performance text (classify this)

```text
The farm next to ours is owned by Mr. and Mrs. Gregg. The Greggs have two children, Philip and William. Sometimes I go over to their farm to play with them. Every Saturday morning Mr. Gregg and his boys would take their guns and go off into the woods to look for animals and birds to shoot. I can’t stand hunting. I just can’t stand it. It doesn’t seem right to me that [people] should kill animals just for fun. So every time I went over to their farm I would do my best to talk them out of it, but they only laughed and made faces at me, and Mr. Gregg told me to go home and mind my own P’s and Q’s. Well, that did it! Before I was able to stop myself, I did something I never meant to do. I PUT THE MAGIC FINGER ON THEM ALL! For months I had been telling myself that I would never put the Magic Finger upon anyone again – Not after what happened to my teacher, old Mrs. Winter.

Poor old Mrs. Winter. One day we were in class and she as teaching us spelling.

MRS. WINTER: Stand up and spell cat.

NARRATOR: That’s an easy one. K-A-T

MRS. WINTER: You are a stupid little girl! Go and stand in the corner! Then I got cross and I put the Magic Finger on Mrs. Winter. Guess what? Whiskers began growing out of her face! Just like the ones you see on a cat, only much bigger. Before we had time to think, they were out to her ears!

Of course, the whole class started screaming with laughter.

MRS. WINTER: Will you be so kind as to tell me what you find so madly funny, all of you? When she turned to write on the blackboard, we saw that she had grown a tail as well! A huge bushy tail! If any of you are wondering whether Mrs. Winter is quite all right again now, the answer is No. And she never will be. I can’t tell you just how I do it, but it always happens when I get cross. I get very, very hot all over. . then the tip of my finger begins to tingle most terribly . . . and a sort of electric flash comes out of me, jumps out and touches the person who has made me cross. The Magic Finger is upon him or her, and things begin to happen . . . Well, the Magic Finger was now upon the Gregg family and there was no taking it off again. I ran home and waited for things to happen. I got the whole story from Philip and William the next morning after it was all over . . .

The afternoon of the very same day, Mr. Gregg, Philip and William went out hunting again. Wild ducks flying very low . . . easy to hit! BANG! BANG! BANG! Went the guns. The ducks flew on.

MR. GREGG: We missed! That’s funny Then to everyone’s surprise, the ducks turned around and came flying right back to the guns. They shot at them again, and again they all missed. They stared for home, but the four ducks would not leave them alone. They began flying around and around the hunters as they walked away. Nothing would make them go away. When morning came, Mr. Gregg was the first to wake up. He sat up and saw what he looked like! (Mr. Gregg yells) He was now a tiny little man, maybe as tall as the seat of a chair and where his arms had been, he had a pair of duck’s wings instead!

MRS. GREGG: My dear man, what’s happened to you?

MR. GREGG: What’s happened to both of us, you mean!

(Mrs. Gregg flaps and sobs) (Mr. Gregg quacking and flapping his wings) This is witches’ work!

A minute later Philip and William burst in. The same thing had happened to them. And they were really tine. About as big as robins.

PHILIP: (quacking) Mama! Mama! Mama! Look! We can fly!

MRS. GREGG: Come down at once! You’re much to high! But before she could say another word, Philip and William had flown right out the window. Soon the whole family was flying around and around together.

PHILIP: Hey, look down there! Somebody is walking in our garden! Below them they saw four enormous wild ducks! As big as men. They had great long arms instead of wings and were walking in a line to the door of the Greggs’ house. The first one put out a hand and opened the door. The other went in after him.

MRS. GREGG: (crying) Oh dear! They have taken our house. What shall we do? We have no place to go! What about food? We haven’t had a thing to eat all day!

PHILIP: I will not eat worms! I would rather die!

MR. GREGG: Disgusting! Just because we have winds, we don’t have to eat bird food. We shall eat apples instead. Our trees are full of them. Come on! But to eat an apple without holding it in your hands is not at all easy. The boys began to cry.

PHILIP: We will be eaten by cats and foxes!

WILLIAM: I want to sleep in my own bed

MR. GREGG: It isn’t any good crying. We are going to build a nest! We’ve got to have somewhere to sleep. Mrs. Gregg and the children flew off. Soon they were back, carrying sticks in their mouths. The building of the next went on and one. It took a long time, but at last it was finished.

MRS. GREGG: Oh, isn’t it lovely! I might lay an egg any moment. About this time, I picked up the telephone and tried to call Philip to see if the family as all right.

NARRATOR: Hello? (Quack) Who is it? (Quack Quack) It was like a bird laughing. That Magic Finger . . . what has it done to my friends?! At last morning came.

MRS. GREGG: Thank goodness! I never want to sleep in a nest again. She got up and looked over the side . . . On the ground below them stood the four enormous ducks and three of them were holding guns in their hands.

MR. GREGG: No! No! No! Don’t shoot!

DUCK: Why not? You are always shooting at us

MR. GREGG: But that’s not the same! We are allowed to shoot ducks!

DUCK: Who allows you?

MR. GREGG: We allow each other.

DUCK: Very nice. And now we are going to allow each other to shoot you! I would have loved to have seen Mr. Gregg’s face just then.

MR. GREGG: Oh, please! My two little children are up here with us. You wouldn’t shoot my children!

DUCK: Yesterday you shot my children. All six of my children.

MR. GREGG: I’ll never do it again. Never, never, never! I’ll never shoot another duck as long as I live.

DUCK: That is not good enough. What about deer?

MR. GREGG: I’ll do anything you say if you will only put down those guns. I’ll never shoot anything!

DUCK: Will you throw away your guns?

MR. GREGG: I will break them into tiny bits!

DUCK: Very well. You may come down. And by the way, may I congratulate you on the next. For a first effort it’s pretty good. Then all at once everything went black. A funny feeling came over them all and thy heard a great wind. The black turned to blue, to green, to red and then to gold, and suddenly, there they were, standing in their own garden and everything was back to normal. Philip and William began dancing about with joy. High above their head, they heard the call of a wild duck. (Quack) About half an hour later, I walked into the Greggs’ garden to see how things were going, and I must admit I was expecting the worst. Mr. Gregg was smashing all three guns into tiny pieces with a huge hammer. Mrs. Gregg was placing beautiful flowers upon sixteen tiny mounds of soil, which I learned were the graves of the ducks that had been shot before. And in the middle of the yard Philip and William were surrounded by ducks, doves, pigeons, sparrows, robins, and larks. The birds were eating the barley that the boys were scattering by the handful.

NARRATOR: Good morning, Mr. Gregg

MR. GREGG: (stops hammering) My name is not Gregg any more. In honor of my feathered friends, I have changed it to Egg.

NARRATOR: What happened? (to audience) They seemed to have gone completely dotty . . . all four of them.

WILLIAM: Look! There’s the next! Can you see it? That’s where we slept last night.

MR. EGG: (proudly) I built it all myself. Every stick of it. Just then, from somewhere over by the lake there came a loud BANG! Suddenly I got very hot all over . . . the tip of my finger began tingling. I could feel the power building up inside me. I turned and started running towards the lake as fast as I could.

MR. EGG: Hey! Where are you going?

NARRATOR: To find the Coopers! Wait and see. They’ll be nesting in the trees tonight, every one of them!
```
