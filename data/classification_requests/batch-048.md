# Classification request: batch 48 of 53 (40 records, IC-2281 to IC-2320)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-048-reply.json`.

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

## IC-2281: Light and Hope

- Title: Light and Hope
- Author (byline): Bethany Van Delft
- Work: The Moth Presents All These Wonders (Pg 293-299)
- Publisher: Crown/Archetype
- Publication date as stated: March 2017
- Event as filed: Prose
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

## IC-2282: Lily

- Title: Lily
- Author (byline): Matt Buchanan
- Work: Not specified
- Publisher: Brooklyn Publishers
- Publication date as stated: 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1761
- Already set (do not supply): none

### Source block (context only)

```text
Author: Matt Buchanan
ISBN: 978-1600032691
Publisher: Brooklyn Publishers
Date (Month/Year): 2007
*Note: Also found on-line at
http://www.childdrama.com/samplelily.html
```

### Introduction (context only: never use it for content warnings)

```text
Time and time again we are told of the epidemic of loneliness in this country. According to Jeannette Kupfermann, researcher for The Daily Mail, one in ten people over-65 feels chronically lonely all the time, yet most suffer in silence, through fear of appearing a nuisance.

More often than not, these are not old people cut off from their families or left alone without surviving relatives. Many have family who are simply too caught up in their own lives to make time for them.

In Lily by Matt Buchan a mannequin in a dress-shop window forms a special friendship with the lonely old woman who stares through the window at her every day.
```

### Performance text (classify this)

```text
You probably think I lead a pretty glamorous life and I guess you’re right. It’s not too bad, getting to wear all the latest styles, always the pinnacle of haute couture. But don’t envy me so easily. Sure, my clothes are always new, always expensive. But I never have any say in what I wear. Other people always choose my outfits, and some of them have very strange taste. Last Christmas I had to wear this hideous red and purple thing with what looked like tinsel streamers on the shoulders. And how would you like being dressed and undressed by strangers all the time? And it’s not like they treat you with respect. Once they took all my clothes and left me there, totally naked, for almost an entire day. Right in the window! Fortunately, I’m not anatomically correct or somebody would have been arrested. But the shame. Actually, I think it’s worse because I’m not anatomically correct. Somehow all that smooth, featureless plastic feels even more naked. That was probably the most mortifying day of my life, unless it was the time they were having a sale in Menswear and some genius decided to borrow me. They took my regular hair, gave me a bad male wig, and put me in a suit. What a disaster! I may not have all the bits and pieces, but I do have a shape. Wig or no wig, I do not look like a man! At least it was just guys shopping over there and they mostly don’t notice anything.

What’s even worse is I can’t shut my eyes. People watching is fine, and I do have a great view from my window on Main Street, but haven’t you ever not wanted to look at something? Something disgusting or upsetting? And you can look away. You can shut your eyes and pretend it’s not there. Or even just something embarrassing. Like, okay—most of the time it’s bright enough in my window and people can see right in, but during morning rush hour when the sun slants directly on my glass my window looks like a mirror from the outside. And people use it like one. Here’s a news flash for you: My window may look like a mirror to you, but from my side it’s still a window. I do not need to see you picking spinach quiche from your teeth or checking to see if your tongue is coated. It’s embarrassing! I don’t really mind people checking their hair, and sometimes it’s kind of funny to watch guys slow down to check their full-body profile, but it’s also kind of pathetic. Still, you do meet some nice people.

I met Lily about seven years ago. It was around New Year’s and I was wearing a really gorgeous ball gown. It was pale peach silk, feathery light, and cut a little like those “flapper” dresses they used to wear during Prohibition—only more formal. It was just getting dark and this really, really old lady stopped outside my window. She was a little stooped and a little chubby, with sweet snow-white curls poking out of a knit hat and bright little button eyes. She was wearing a knit shawl over a wooly coat that had been mended several times and carrying a clumpy purse and a mesh shopping bag.

She stood and gazed at me for a long time. Well, that’s nothing new—people do it all the time, and it was a beautiful gown. Then I saw that she had tears in her eyes. Slowly her arms came up until she looked like she was holding a dancing partner. Her stoop seemed to vanish, and she began to sway gracefully to music I couldn’t hear. Pretty soon she was waltzing back and forth on the sidewalk. People were hurrying past but it was like she couldn’t see them. They dodged out of her way, some of them annoyed and some with indulgent smiles, and she danced. When she finally stopped her face was shiny. She pressed her face against the glass for a last look and then walked slowly and a painfully down the street. A little while later she came back the other way with a few groceries in her mesh bag and she waved to me as she passed.

She came back the next day about the same time, with the same mesh bag and the same faraway look in her eyes. She stayed for a few moments then went on her way. A little while later she came back by with her day’s groceries.

I decided to call her Lily. I don’t know—she just seemed like a Lily to me—kind of soft and lovely and a little sad. She came by every day. Sometimes she only stayed for a moment or two, but she always stopped. Once every two weeks she’d cross the street to the little Automated Teller Machine booth at the bank.

Lily talked to me, too. She always told me what she thought of the clothes. “Oh, my dear,” she’d say with a shake of her curly white head, “That’s not you at all, dear! Whose idea was that, I wonder?” That was usually when I was wearing something modern and revealing. She loved the really formal things best. “Oh, yes!” she’d exclaim with a bright smile and a little clap of her hands. “That is gorgeous, isn’t it, dear? I wish I were you!” She never seemed to expect me to talk back. Sometimes people passing by would hear her and give her a look, but she ignored them and so did I.

I used to try and imagine the story of her life. I imagined a tragic love story. Her lover went down with the Titanic or died in the war overseas. I imagined she was a dancer in a speakeasy and stabbed her boss when he tried to get fresh. I imagined her as a faded movie star still trying to hang onto the lost glory. Somehow all the stories I imagined were a little sad.

I knew she had a family because I’d seen pictures. She carried a thick album in her handbag. Most of the photos were of a young woman and a small girl. Her granddaughter and great-granddaughter. She showed me the pictures at least once a week, chattering away proudly about their achievements. I learned that her granddaughter was a lawyer and sometimes sent her money, and that her great-granddaughter played the cello. But the stories never changed, and there were never any new photos. Not in six years. I began to think she’d made them up.

That’s why I was so surprised the day she brought her granddaughter to meet me. She was a little later than usual, but then here she came, with a grumpy-looking middle-aged lady in tow. It was prom season and I was in a ball gown. “There, you see! Isn’t it lovely?” Lily said. “It’s perfect!”

The woman seemed impatient. “Yes, Gran, it’s very nice, but it’s a little old-fashioned. I think Amy wants something more modern.”

“Nonsense,” twinkled Lily. “Don’t you listen to her, dear. You look lovely, and not a bit old-fashioned.”

The woman looked around to see if anyone was staring. “Honestly, Gran, you can be so exasperating! Can we go?”

Lily’s granddaughter was with her for several days. She seemed grumpier and in a bigger hurry every time I saw her, but I’d never seen Lily happier. I was sorry when she was gone and Lily was alone again. “Tina’s a good girl, really,” she told me almost apologetically one day after she was gone. “She’s just got a lot on her plate. Little Amy is a dear, but she’s a handful. You know what teenagers are like. And, too, she’s a career woman. It was nice of her to visit her stuffy old Gran, even if it was only for a few days. I do wish she’d brought Amy along.”

After that it seemed like Lily was slowing down every day. One night a couple of months later she was a little behind schedule and it was dark when she shuffled across the street to the bank. It was raining steadily. I watched her disappear into the little ATM booth, wondering how much money her “career woman” granddaughter sent her. Then I saw the man. He was watching the door of the bank like a lion staking out a water hole. Inside my head I was shouting, “Stay inside! Lily, don’t come out!” But she did and I had to watch. I watched helplessly as my friend Lily was shoved roughly against the wall. She let him have her wallet without a struggle but when he tried to take the photo album she put up a fight. She scratched his face and she screamed. People started looking and one or two came running. The man panicked, shoved her hard into the wet street, and ran. And I watched helplessly as my friend Lily careened into the path of that taxi and its tires slid across the slick pavement. After the ambulance and emergency vehicles left, I saw Lily’s photo album wash into a storm drain.

It took a long time to get over losing Lily. Every afternoon I expected to see her. Wondered why she was late. Suddenly remembered. But I gradually got used to the idea that she wasn’t coming back. Lily became just a pleasant memory of an old friend, until one day almost a year later. It was Prom season again, and I was wearing an old-fashioned gown very much like the one I had on the day I first met Lily. I hadn’t thought about her in weeks, when, suddenly, there she was, staring into my window with her bright, twinkling eyes. Except it wasn’t Lily. Lily was dead, and besides, this was a very young woman—maybe eighteen—and she didn’t even really look like Lily, except her eyes. She was much taller, and elegantly thin.

“Mom!” the girl who wasn’t Lily called over her shoulder, not taking her eyes off me. A slightly harassed-looking woman came up to her. It took me a minute to recognize Lily’s granddaughter Tina.

“You see!” cried Amy—because it must be Amy. “I told you! It’s perfect!”

Tina stood beside her daughter in my window for a long time. Tears streamed down her face. Inside, where no one could see, I cried too.
```

---

## IC-2283: Love First, Teach Second

- Title: Love First, Teach Second
- Author (byline): Joan Clayton
- Work: Chicken Soup for the Teacher’s Soul
- Publisher: HCI
- Publication date as stated: 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1090
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joan Clayton
Book: Chicken Soup for the Teacher’s Soul
ISBN: 978-1558749788
Publisher: HCI
Date (Month/Year): 2002
```

### Introduction (context only: never use it for content warnings)

```text
Attention Deficit Hyperactivity Disorder (ADHD) is one of the most common behavioral disorders among children. Between 3 and 5 percent of all children, as many as 2 million, may suffer from this condition. The most common recommendations for teachers in dealing with ADHD students is to establish control: be consistent, follow definite rules, discipline offenses immediately, offer explanations for what rule was violated and be willing to listen to their side of the story and to reward success: use stickers, post points on a chart, shake hands, smile, use verbal praise. In Love First, Teach Second by Joan Clayton, this veteran teacher has seen it all and tried it all, but nothing is effective her struggling first grader, Mary. Then she has an idea, and amazing and wonderful idea. Love First, Teach Second by Joan Clayton
```

### Performance text (classify this)

```text
“You’re going to have Mary in your room?” a fellow teacher asked. Her voice conveyed apprehension, as she added, “I feel sorry for you.”

“She’s on medication, you know,” another teacher warned. “You will be, too, before the year’s over!”

I’d heard similar comments during my eighteen years of teaching, but usually these first-grade children turned out to be normal in every respect.

So I began the year with calm assurance that I could handle whatever came.

Was I in for a surprise!

A few days before school started, Mary and her mother dropped by to “get acquainted.” Golden blonde hair fixed to perfection cascaded down the little girl’s back. Large, beautiful blue eyes gazed into mine. Between the outbursts from Mary, which frequently interrupted the conversation between her mother and me, I learned that Mary needed medication for both hyperactivity and asthma. She would need to take one pill after lunch.

Her mother agreed that the office would keep the medicine, and I would send her for it every day after lunch. Mary’s mother graciously volunteered as room mother. I was delighted.

Then came the first day of school.

Mary made her bouncy entrance and dropped purses, tablets, marking pens, hair barrettes and gimmicks of all kinds. Every time I turned around, it seemed that some child was crawling under a table to retrieve Mary’s loot.

Whispering seemed impossible to Mary. She frequently blurted out her thoughts. “The answer is ahhhh. . . one. No two . . . No, threeeeeee!”

I knew the scene by heart. She scrubbed vigorously with her eraser, usually tearing the paper, then started the whole procedure with a fresh sheet of paper, again and again.

One day, completely exasperated, I voiced my complaints to the office secretary.

“Mary’s medication doesn’t seem to help at all.”

“What medication?” the secretary questioned. “She hasn’t been in for it since school started.”

“I send her for her pill every day after lunch.” I protested, “and she comes back assuring me that she has taken it.”

After that, I began sending a child I could depend on with her to see that she took her pill. Even with resumption of her daily medication, I still had to deal with Mary’s repeated outbursts.

One day, after constant shushing, isolating and reprimanding, I stopped the class and said, “All right, Mary, come to the front. Take all the time you need to talk, wiggle or whatever, so you can settle down and we can get back to work.”

Always before, this drastic method had worked. The student, embarrassed, would stand silently and be more than happy to sit down and resume working.

But not Mary. At first she jumped up and down, growling like a caged bear. Then she pounded on the desks with her fists, screaming like Tarzan in the jungle. The children loved the show as Mary alternated between growling, screaming and laughing. This encouraged her to show off even more. After five minutes of these antics, I could stand no more. This little girl had outsmarted the teacher!

In the weeks that followed, I gave rewards, praise and reinforcement of positive behavior, when I could find any. Nothing seemed to work.

At the end of one particularly harassing day, I dismissed the children and slumped in the chair behind my desk, totally defeated. I had tried everything.

Everything, that is, except prayer!

With my head on my desk, I prayed, “Lord, help me with this child. Show me the key. Where have I missed it?”

In utter exhaustion, I dozed off. When I awakened a few minutes later, my frustration and weariness had disappeared. Two words kept coming to my mind: “Love her.”

I was well aware that those who are the hardest to love are often the ones who need it the most. But I thought I had worked through this, and that I already loved her.

Yet, those two words, “love her,” lingered in my mind. And they were there when I awakened the next morning.

“Lord,” I prayed, “I already love her, so I’m going to take those to words to mean that I’m to love her . . . with hugs.”

I hurried to school that morning, bursting with anticipation. God had answered, and I was eager to see God’s plan unfold. When the bell rang, Mary bounded in with enough energy for the whole class. I gave her paper to write her spelling words on, and she jumped ten frog jumps to her seat.

Then she began to write and spell out loud, “D-o-w-n. Ddddd ooooo wwww nnnnnnn!”

“Mary, come to my desk, please,” I said quietly.

With tow hops, a skip, a side two-step and three giant steps backward, Mary obeyed my command.

Silently, I pulled her toward me and held her close. In my thoughts, I was praying, “Lord, help this little child to calm down. Take away whatever is causing her hyperactivity.” I continued this tactic. Sometimes these sessions lasted five minutes with no one saying a word. It was just Mary and I holding each other. It was just Mary and I holding each other. The other children watched silently and seemed to understand. If Mary’s behavior got out of control, we stopped and hugged, just Mary and I, while the class waited patiently and lovingly. There were times we did this four or five times a day.

One week later, Mary’s reading teacher came running across the hall. “Whatever has happened to Mary? She isn’t the same child!”

“It’s called prayer and hug therapy,” I explained. “I silently pray for her every day, and before I let her come to the reading class, I stop the children, hug her and say a silent prayer.”

“Well, don’t ever stop!” the teacher exclaimed.

In just a few short weeks, Mary’s behavioral change was noticed by other staff members, too.

I knew in my heart that God was leading.

It is now spring. Last fall seems long ago. Now it’s hard to think of Mary as ever having had problems. She acts perfectly normal in every way. When she raises her hand to answer a question, but instead says, “Teacher, I love you,” I say a silent prayer of thanksgiving.

In a few minutes the bell will ring, and the children will come in – each with different needs. As I pass out their papers, I will pray silently for these little lives that have blessed mine so abundantly.

“Lord, bless this child today. Help me always to love first ad teach second.”
```

---

## IC-2284: Love Sees No Colors

- Title: Love Sees No Colors
- Author (byline): Susan A. Eldred
- Work: Teen Ink Love and Relation
- Publisher: HCI Teens
- Publication date as stated: April 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 664
- Already set (do not supply): none

### Source block (context only)

```text
Author: Susan A. Eldred
Book: Teen Ink Love and Relation
ISBN: 978-1558749696
Publisher: HCI Teens
Date (Month/Year): April 2002
```

### Introduction (context only: never use it for content warnings)

```text
As recently as 1967, marrying a person of another race was considered to be illegal in at least sixteen states of the United States. Thanks to the Loving Decision, a ruling made by the U.S. Supreme Court, these laws have been overturned and people are free to date and marry whom they like without condemnation. Regardless of the legal status of interracial dating and marriage, however, society’s mores are difficult to overcome. How can we teach our society that Love Sees No Colors by Susan A. Eldred
```

### Performance text (classify this)

```text
I am scribbling this story on a worn-out notepad I found in my bag. The pages are unbelievably wrinkled, and my pen is running out of ink. My head is spinning. Actually, I think that I am developing a slight migraine.

I am in Tokyo (yes, Tokyo, Japan), sitting on a bench in one of their well-celebrated gardens, writing. I am always writing. I suppose it is my therapy.

I am writing about you. I am smiling just with thinking. Can you remember the day we first met? I can honestly say I was not that interested in you, nor were you in me. Honestly, I gave you and three other people my number (bet you didn’t know that). You called first. I’m glad you did.

And so we started talking – I, in analogies. Isn’t it funny how I’ve always talked in analogies? You were pretty forward and honest; I admired that. There are a lot of fake people in this world. You were real to me, and right off the bat, I loved you for that. You tolerated my analogies (understood a few of them, too) and encouraged me – challenged me – to speak my mind. I had been hiding behind them, and you, being the perceptive individual you are, saw right through me. I became vulnerable to you, and you to me, but we didn’t take advantage of each other, as some people might.

Sometimes, when I’m walking down a street, whether in the city or my own town, I wonder how people see me. Our world is composed of stereotypes – each person carries his or her views like a shield. Isn’t it funny how people are afraid of differences? But when we were together, I never wondered what people thought. It just didn’t matter. You were a Columbian boy, clean-cut and good looking, who loved football. I was a light-haired, light-skinned Catholic-school girl who loved art and writing. I hadn’t the foggiest idea about football.

Life was sweet. But, of course, as there always is a silver lining, there can also be a thunderstorm. I began to notice some of my friends’ lack of support. My best friends (even though some did not agree with interracial dating) were still supportive. But some strongly opposed it. I tried to explain my problem to you, but I just couldn’t speak. Isn’t it ironic how such a verbal person can become mute at such imperative times? I remained silent as it grew worse.

You are wondering what got worse? First, people began to make jokes. They were horrible, yet I blamed their cruelty on “ignorance.” I use “ignorance” as an excuse when, in reality, ignorance is quite often a choice.

The incident that I remember most vividly (even to this day) happened in chemistry class. One lab period we were working with chemicals including iodine. Iodine taints your skin black or dark brown if you come in contact with it. My teacher warned us about it. She didn’t want us to stain our uniforms.

A few minutes later, I heard a loud voice recommend that I dye my skin black so I could be like my boyfriend. I froze.

That is all I can think of now: those words. I hear them almost every day, sometimes over and over like a bad dream, a broken record. Those were not words of ignorance; those were words of hate. And it makes me so sad, so sad.

But I am glad that we have not let them win. Isn’t it funny how people can take something as simple and beautiful as love and turn it into a struggle? I can honestly say that I would gladly repeat all those nights I cried myself to sleep. A friendship like yours is worth more than any of that . . . much, much more.

And so, maybe we have won; I am not ashamed to come forward and say that I love you with all my heart, and that it would never matter to me whether you were white . . . black . . . or purple. Because love, my friend, sees no colors. Love sees no colors.
```

---

## IC-2285: A Lynching in Stereoscope

- Title: A Lynching in Stereoscope
- Author (byline): Stephanie Dickinson
- Work: The Best American Nonrequired Reading 2005
- Publisher: Mariner Books
- Publication date as stated: Oct 2005
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1297
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephanie Dickinson
Book: The Best American Nonrequired Reading 2005
ISBN: 978-0618570485
Publisher: Mariner Books
Date (Month/Year): Oct 2005
```

### Introduction (context only: never use it for content warnings)

```text
Let the story of Ciz and Alp (last name unknown) be told . . . Sometimes lynchings became mass spectacles with a circus atmosphere. Children often attended these public lynchings, and it was common for postcards to be sold. These postcards became popular enough to be an embarrassment to the government, and the postmaster officially banned them in 1908. However, the lynching postcards continued to exist through the 1930's.

Records exist from Waco, Texas in 1916 of a postcard showing the burned body of Jesse Washington,. Washington was a 17-year-old retarded farmhand who had confessed to raping and killing a white woman. He was castrated, mutilated, and burned alive by a cheering mob that included the mayor and the chief of police. A tree supported the iron chain that lifted him above the fire. . . Wailing, the boy attempted to climb up the skillet hot chain. For this, the men cut off his fingers. On the back of the postcard, was a hand written note: "This is the barbeque we had last night.”

Let the story of Ciz and Alp (last name unknown) be told. . . A Lynching in Stereoscope by Stephanie Dickinson
```

### Performance text (classify this)

```text
I lift the stereoscope to my face. True old-timer amusement. The card photograph is of a bare-foot corpse. Hanging from a bridge, a pretty woman in a calico dress. I can see the ripples in the brown river, and almost her the sluggish gurgling. A postcard. Etched into the corner “Copyright 1934 – Arkansas – unmailable.” At the edge of the photograph is another hanging body, smaller then the woman’s. Badly burned, too burned to tell what sex it is. I breathe deeply. Take the card out of the stereoscope. Who is she? Why did they hang her on this afternoon?

Today is soap-making day. The ninety degrees are crowding me as I push my head through the dress neck, and pull the comb through my wild hair that needs three hands to tie it back. I press the tin mirror close to my face and hunt for the light in my eyes, like once I searched for my son’s father. I was thirteen then. Now I’m twenty-five and I stand four feet eight inches tall.

“Alp, rise and shine, my sweet potato pie.” I sing to my son still asleep behind the curtain that divides the room.

Suddenly the hairs stiffen on my upper lip. The eyes in the back of my head see the dog on the stop. A white bloodhound. . . panting. A scream knots my throat. “Shoo,” I say to the bloodhound. “What do you want with me?” When I turn to the screen the dog is gone, and Alp is rubbing his sleep face. He’s a big boy, almost six feet tall and just going on twelve. Sweet natured with dimples . . . give him a white peach and he’s happy for a week.

And then [I] see fifty townspeople walking in the stun through the black walnuts and buckthorn and crabapples. What do they want? They must be going after someone. Maybe one of the croppers stole something. “What can I do for you?” I call out. I recognize Sheriff Garner. His deputies have regular redbone hounds tugging at leashes. The redbones sniff their way . . . “We’ve found the dog,” the square-headed deputy shouts. “Know who this her dog belongs to? R.E. Lee Wilson.”

My blood ices. Mr. R.E. owns the air I’m breathing. Sheriff Garner walks toward me, rocking the upper part of his body. “This dog was trailing the boy who molested a nine-year-old girl. Happened this morning!”

“My boy’s been with me all day. The folks around here can tell you.” Alp steps out of the kitchen and three or four town men in suspenders and straw hats hustle him over to where I am. “Listen. Whatever he done, whatever you say he done, I did it. He didn’t do anything.”

“We’re going to make us a trial. This animal took down his pants in front of a nine-year-old girl.”

They dunk Alp’s hand into the scalding soap. His scream rises to the treetops. First time he ever pees himself since he was a baby.

Names fly. Killers, castrated pigs, dirt shack dung, coons.

The steel-spectacled deputy hits my boy in the mouth. Alp shudders like a dog shaking off ditch water. Men push through the deputies. Men push through the deputies, a bunch of cotton shirts, old-fashioned neck-pieces. “Make the bastard talk about what he did to R.E. Lee’s girl!”

I jump between them and Alp, cover him with as much of me as I can muster. A boot picks itself up, hell banging my hip. The flat of another lands solid in the small of my back.

“Leave the woman be,” Sheriff Garner bellows.

A female cries, “Cleanse the sin from R.E. Lee’s child.”

I crawl to Sheriff Garner’s pant leg. “Let my son be. I swear he’s good.” My heart’s rasping. “My boy’s been with me all day.”

The spectacled deputy takes off his belt. “Lets tend to the boy.” One after another the men come, taking turns whipping. None hide their faces. My son’s eyes swell shut. At least he’s saved from seeing. The deputy dunks my son’s other hand in the soap. This time Alp’s scream digs a hole in the ground.

“Let’s take them to the river.” They push me after my son. Red water’s leaking from Alps forearms where the skin is ripped. I scream. They ball a handkerchief and stick it in my mouth. Let me go with him. He’s afraid of when the weather changes too many times in one day, he’s afraid of ladders and birds. They hold me back. They tie him up and pile on the kindling. Fifty, now there’s a hundred streaming past me. Laughers, jerkers, spitters. They crash into the woods. A newspaperman takes out his tablet. “We’re just swatting a few mosquitoes. That’s not news.”

I’m not afraid anymore. They’re burning my son. I hear his screams. They must pull him from the fire to savor him. For thirty minutes my baby howls. Alp, it’s your mama, honey love. You’re named Alp after those cold tall mountains far away. Go there in your mind. They burn him slow.

I feel a yank as they cord my wrists behind my back. Someone rips my apron. Let’s go swimming, sweetheart.” They walk me to the bridge. Last sun ripples in the sluggish current. This is the river Alp was baptized in.

My heart is gone when they push a charred thing past me in a wheelbarrow. The thing has no legs. It raises up on its haunches, reaching out, no hands on the ends of it blackened wrists.

A man with a whiskey nose croaks, “ I’m going to write the boys down there in Delight. Tell them about the barbeque we had this afternoon.”

Townspeople crowd both sides of the river. There’s a bunch behind me. Someone is playing an accordion. Someone is selling rock candy.

“Make way, make way, R.E. Wilson’s on his way.” And then I see the man who owns the dirt where they make me set my feet.

“This is the boy who done it, R.E.” They push the blackened thing in the wheelbarrow at him. A burnt offering. He has a golden boy and girl with him, a twin set.

Devil is the name I give the one who puts a rope around my neck. A man ties my torn apron. For an instant I think kindness. Then his hands fill my pockets with pebbles. Alp, they’re going to hand you too, even if you’re already dead. A stone hits me in the stomach, then a stick. I raise my face, even as a peach pit hits my forehead. A rope has been tied to a joint, the noose end coils in the dust.

My ashy son hangs over the water; my son who has no hands is buried in the air on the summer vines. The photographer is moving closer, his camera like a box lunch at an ice cream social. “Let’s see you do a jig, Ciz.” Is it true when they take a photograph at the moment of death, that’s where your soul stays?

I drop. Ripples of heat rise from the trees. I’m listening to the leaves turn over, tinkling, showing off their silver undersides.

“Does it hurt, Mama?” Alp asks. I spit the handkerchief from my mouth, a honeydew voice flows through my tongue – we’re the angels, not the murdered ones.

The blond children play on the riverbank. The girl looks out from behind her brother, half-smiles, and ducks. Peek-a-boo, I see you. Wind caresses. A sickle moon waits in the sky. Barn swallows offer up pitifully glad songs.

I blink and walk out into air. Giver, let me live.
```

---

## IC-2286: A Manhattan Romance

- Title: A Manhattan Romance
- Author (byline): Joyce Carol Oates
- Work: Faithless: Tales of Transgression (Pg 209-220)
- Publisher: Perennial Press
- Publication date as stated: June 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MOMMA, DADDY, POLICE
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
Divorce is a highly stressful and emotional experience for everyone involved, but children often feel that their whole world has turned upside down. Custody battles, child support and visitation rights are terms that no small child can fully understand.

And for a father with limited visitation rights, a stressor that may become too much to bear.

Manhattan Romance by Joyce Carol Oates
```

### Performance text (classify this)

```text
(Pg 209-220) That wild day! I’d woken before it was even dawn; I seemed to know that a terrible happiness was in store. I was five years old [and] feverish with excitement when Daddy came to pick me up for our Saturday adventure as he called it.

MOMMA: (whispering) If you said you were sick, you wouldn’t have to go with – him.

For she could not utter the word Daddy, and even the words your father made her mouth twist. (to Momma) Momma, I’m not sick! I’m not! (to audience) So the doorman sent Daddy up.

MOMMA: I wish you didn’t have to leave me, darling, but it’s the terms of the agreement- it’s the law.

These bitter words It’s the law fell from Momma’s lips each Saturday morning. And then Momma leaned over me and kissed me; I loved Momma’s perfume and her soft-shining hair but I wanted to push away from her; I wanted to run to the door, to surprise Daddy, who took such happiness in being surprised; I wanted to say to Momma, I love Daddy better than I love you, let me go! Because Momma was Momma, but Daddy – there would never be a man so handsome and radiant as Daddy.

Our driver that day was an Asian man in a neat dark uniform and gloves. Daddy no longer drove his own car. His enemies had taken his driver’s license to humiliate him, he said. They could not defeat him in any way that mattered, for he was too strong for them and too smart.

Other Saturdays, we’d gone to Radio City Music Hall, we’d seen Beauty and the Beast on Broadway; we’d seen the Big Apple Circus at Lincoln Center. Daddy liked me to smile and laugh, not to worry; not ever, ever to cry. He’d had it up to here (drawing a forefinger across her throat, like a knife blade) with crying, he said.

DADDY: Today, Princess, we’ll buy presents. That’s what we’ll do -- “store up riches.”

Christmas presents? I asked.

DADDY: Sure. Christmas presents, any kind of presents. For you, and for me. Because we’re special. (smiling) You know we are special, Princess, don’t you? And all your life you’ll remember your Daddy loves you? -- That’s the one true thing.

Yes Daddy, I said. For of course it was so.

Daddy bought me a dark blue velvet coach, a beautiful silk scarf and a white-gold wrist watch studded with tiny emeralds. For all these wonderful presents, Daddy paid in cash. I knew it was strange for Daddy to be paying out of thick-stuffed envelopes in his inside coat pockets. No one else paid in such a way. [But, he] no longer used credit cards, he said he refused to be a cog in the network of government surveillance, he said; they would not catch him in their net; he would not play their ridiculous games.

Next, we went to the Museum of Modern Art, where Daddy lifted me to his shoulders and carried me into a large, airy room. There were tears in Daddy’s eyes as he held me in his arms -- his arms that trembled slightly – to gaze at an enormous paintings -- several paintings -- broad beautiful dreamy-blue paintings of a pond and water lilies; Daddy told me that these paintings were by a very great artist named “Mon-ay” and that there was magic in them; he told me that these paintings made him comprehend his own soul, or what his soul had been meant to be; for as soon as you left the presence of such beauty, you devoured by the crowd.

When we left the museum, I was dazed with exhaustion. I could not have said how long Daddy and I had been shopping, on our Saturday adventure; yet I loved it, that strangers observed us, and remarked how pretty I was; and to Daddy sometimes they would say, Your face is familiar, are you on TV? But Daddy just laughed and kept moving, for there was no time to spare that day.

Years later I would learn that, that afternoon, a warrant for Daddy’s arrest had been issued by the Manhattan district attorney’s office; by some of the very people for whom, until a few months ago, Daddy had worked. It would be charged against him that as a prosecuting attorney, Daddy had misused the powers of his office and blackmailed others, embezzled funds, and committed perjury. . . such charges were made against Daddy, such lies concocted by his enemies who had been jealous of him for years and wanted him destroyed. One day I would learn that New York City police detectives had come to Daddy’s apartment to arrest him but hadn’t found him. Momma told them that Daddy would be bringing me back home at 5:30 pm, or in any case he’d promised to do so; if they waited for him in the lobby downstairs would they please please not arrest him in front of his daughter. And now an alert was out in Manhattan for Daddy, he was a “wanted” man.

So exhausted! Daddy scolded me, carrying me into the lobby of the Hotel Pierre, [where he] booked a suite for us on the sixteenth floor. You could look from a window to see the apartment building on Central Park South where Momma and I lived. Once we were inside the suite Daddy bolted the door and slid the chain lock in place. There were two TVs and Daddy turned them both on. He turned on the ventilator fans in all the rooms. He took the telephone receivers off their hooks.

DADDY: (breathing hard, eyes rapidly shifting) Princess! Get up please. Don’t disappoint your Daddy.

Daddy found a can of apple juice in the mini bar, poured it into a glass and added something from another little bottle.

DADDY: Princess, this is a magic potion. Drink!

And so I did. A hot hurting sensation spread in my mouth and I started to choke. Daddy pressed the palm of his hand over my mouth to quiet me. I was sickish now and I was frightened; but I was happy, too; I was drunk with happiness from all we’d done that day, Daddy and me. I had never had so many presents before. I had never understood how special I was before and afterward when they asked me if I’d been afraid of my Daddy I would say no! No, I hadn’t been! Not for a minute! I love my Daddy I would say, and my Daddy loves me.

[I heard] pounding at the door. And men’s voices calling . . .

POLICE: Police! Open up Mr. _____“

. . . saying Daddy’s name as I’d never heard it before. Daddy was excited and angry and he had a gun in his hand - - I knew it was a gun, I’d seen pictures of guns – and he was waving [it] as if the men on the other side of the door could see him. There was a film of sweat on his face. I had never seen my Daddy so furious calling to the policemen

DADDY: I’ve got my little girl here, my daughter -- and I’ve got a gun.

But they were pounding at the door; they were breaking down the door; Daddy fired the gun into the air and pulled me into another room.

DADDY: I’ll use it, I’m not afraid – I’m not going to prison – I can’t! I’ve got my little girl here, you understand?

Daddy pushed me down, panting. I was too scared to cry, [but] Daddy was crying. We were crouched in the farthest darkest corner of the room. The magic potion had made me sleepy and sickish; it was hard for me to stay awake.

POLICE: “Mr. _____ , surrender your weapon, will you? Toss it where we can see it, will you?

Daddy’s face was streaked with tears like something melting. And still the voice said, calmly, so loud it seemed to come from everywhere at once,

POLICE: Mr. _____, you’re not a man to harm a little girl, we know you’re a good man, you’re not a man to harm anyone.

And suddenly Daddy said . . .

DADDY: Yes! Yes, that’s right. (to daughter in a high happy voice) Princess, your Daddy loves you, that’s one true thing. Never forget, that’s the one true thing in your life of mostly lies. Good-bye, Princess!”

Daddy placed the barrel of the gun deep inside his mouth. And Daddy pulled the trigger.

So it ended. It always ends. But don’t tell me there isn’t happiness. It exists, it’s there. You just have to find it, and you have to keep it, if you can. It won’t last, but it’s there.
```

---

## IC-2287: The Men Who Killed Me

- Title: The Men Who Killed Me
- Author (byline): Marie Louise Niyobuhungiro
- Work: The Men Who Killed Me: Rwandan Survivors of Sexual Violence (Anne-Marie de Brouwer and Sandra Ka Hon Chu, eds) Pgs 29-34
- Publisher: Douglas and McIntyre
- Publication date as stated: Sept 2009
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MARIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1575
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marie Louise Niyobuhungiro
Book: The Men Who Killed Me: Rwandan Survivors of
Sexual Violence (Anne-Marie de Brouwer and
Sandra Ka Hon Chu, eds) Pgs 29-34
ISBN: 978-1553653103
Publisher: Douglas and McIntyre
Date (Month/Year): Sept 2009
```

### Introduction (context only: never use it for content warnings)

```text
In the 100 days of genocide that ravaged Rwanda in 1994, one million people were killed and as many as 500,000 women and girls were raped. No one was spared. Grandmothers were raped in front of their grandchildren; young girls witnessed their families being massacred before being taken as sex slaves. Nearly all the women who survived were victims of sexual violence or were profoundly affected by it. An astounding 70 percent are HIV-positive. In Rwanda’s social and cultural climate, survivors who speak out face discrimination and isolation.

Marie Louis Niyobuhungiro is one of the victims of Rwanda. Bear witness not only to the crimes she and her countrymen endured, but to the incredible courage that has allowed her to survive and flourish.

From The Men Who Killed Me: Rwandan Survivors of Sexual Violence edited by Anne-Marie de Brouwer and Sandra Ka Hon Chu; this is the testimony of Marie Louise Niyobuhungiro
```

### Performance text (classify this)

```text
Born:1975 (day and month unknown)

Birthplace: Shyorongi, just outside Kigali MARIE: (Pgs 29-34) People think I am crazy because I am always crying, and I do not blame them for thinking so. I am always angry, and I do not sleep at night. I hoped secretly that I would die during the genocide, but being among other survivors within a survivors’ organization has brought me comfort and hope. I feel like I have a family now, and I am very grateful for that.

MARIE: Before the genocide, we were a family of eight children—five girls and three boys. I was the fourth child in the family. My father was a teacher, and my mother was a farmer. We lived in Shyorongi, just outside Kigali. There were many Tutsi families in Shyorongi; we had only one Hutu neighbour. Although he was our neighbour, that Hutu hated us, especially my father, because we were Tutsi. In 1991, my father was poisoned, and I suspect that the Hutu neighbour who hated him so much did it. When my father started to feel sick, he went to a traditional clinic. After his death, my mother asked the people at the clinic what my father had died of, and they told her that he had been poisoned. Today, our former Hutu neighbour and all his family are in prison for crimes they committed during the genocide.

On April 6, 1994, when President Habyarimana died,. almost three hundred Tutsi had found refuge in the Catholic church of Mboza.

We arrived at the church at about ten in the morning, and a few minutes later the Interahamwe and far soldiers started shooting. They had guns and shot all the men. I fell, and some dead bodies fell on top of me. I was all covered with blood. I heard screams and babies crying, but I was unconscious for most of the time the attack was continuing.

The next day, they came back to kill those who were not yet dead. There was blood all over me, and the killers thought that I was dead, too, so they left me there, lying among those dead bodies. Once I had regained consciousness, all I could see were a lot of bodies lying around the church. The stench of blood was thick in the air. Except for one of my sisters, all my other relatives died during this attack at the church. Out of three hundred people in the church, only five had survived. I felt completely empty. I had no thoughts and felt nothing, nothing at all.

After the Interahamwe left the second time, I left the church. My sister and I went in different directions, because we felt that even if one of us was killed, the other one might have a chance to survive. I fled in the direction of a nearby forest and ran into an Interahamwe on the road, who asked me where I came from. I recognized him as a fellow churchgoer named Ntirenganya. I told him that I had lost my way and was just wandering around. He said that he had finished killing for the day, so others would kill me, not him.

After that close encounter, I spent three days hiding in the bushes. On the fourth day, I went to the house of an uncle, who had not yet had an opportunity to flee, because his wife had just given birth. He and his wife had already been warned by their neighbour, an Interahamwe, to leave their house immediately; they would not have much longer to live otherwise. Together with my uncle’s relatives, I left his house that night. But, at the gate in front of his house, we ran into a group of Interahamwe militia. They took the girls among us and brought us to a nearby roadblock in order to kill us.

Every far soldier or Interahamwe we met on the way made an insulting speech or had a rod to beat us with. One of them said that the girls should be brought to the Twa, who were often ridiculed in Rwanda and considered stupid and worthless. At some point, a far soldier picked me out of the group and took me to a nearby bush. I don’t know what happened to the other girls I was with.

This soldier raped me. After he was done with me, he took me to a house and told the owners of the house to keep me safe, so that he could rape me every time he came. He told them if anything happened to me he would kill them. Every time he came to the house after that, he took me to the forest to rape me. Over five days, I was raped five times a day. The rapist didn’t say anything to me. In the forest, the local people often saw me being raped by this man. The local people, an Interahamwe militiaman and other Hutu would watch the soldier rape me and did not even raise their little finger to stop it. They didn’t care, because I was Tutsi. They were silent. The far soldier who did this to me was so old -- about forty -- and so savage. It was the very first time I saw what a man was capable of doing.

After those five days, the old man brought me to a lady called Mukandoli, who was an Interahamwe too, and I stayed there. She didn’t care about my situation. She didn’t say anything, except when she sometimes ordered me to go out and farm. I stayed with this lady for one week. Then another far soldier came and told Mukandoli that his colonel wanted me.

When I arrived at the far camp, the colonel had the “manners” to ask me if I wanted to sleep with him. But I knew that whatever answer I gave, the outcome would be the same, and that I would end up in his bed if he had one. I said no and ran into the bushes. His soldiers spent the whole night looking for me, but they didn’t find me.

A little later, I saw a house and entered it. The house appeared to be an Interahamwe’s harem, full of Tutsi women and girls. There were about ten teenage girls in the house, all between about sixteen and twenty years old. The far soldiers who were looking for me found me there and took me back to the colonel. On the way back, they asked me to sleep with them. I told them I could do that the next day. While they were still discussing this, I managed to escape, and I walked all the way to Ruhengeri, which was already under the control of the RPF.

For two weeks, I hid myself during the day and walked during the night. I ate nothing and hid in the bushes. When the RPF went to Kigali, I followed them. I walked just behind them, back to my place of birth. I occupied a house that belonged to owners who had fled the country, because my family house had been destroyed during the genocide. To make a living, I dug the fields for a farmer. Later, a fund for survivors was established, which provided me with a bit of support. I lost four brothers and sisters during the genocide, and one sister died of kidney failure right afterwards. Before the genocide, I had never been intimate with a man, and yet now I have gotten to know many without my consent. Even after the genocide, in 2000, a neighbour came to my house, forced my door open and raped me. There was no use screaming, because no one lived close by. I became pregnant as a result of this rape, and the child died immediately upon birth. The doctors then pressured me to take an HIV test, and I discovered I am HIV positive.

I live in very bad conditions because I didn’t go to school. I have no job and am too weak now to dig the fields. I get food from an organization that helps me to survive. I have had four children since the genocide, all from different fathers. The father of one of my children is a neighbour, and the others have jobs in the neighbourhood. I never see them. I only had sex with each of them once. Luckily, my oldest three children are not HIV positive, but my youngest child has not been tested yet. I wish I could give my children some more support, including buying them school materials and clothes. I am always sick, sometimes because of HIV and other times because of the beatings I endured during the genocide. I was hit on my knees and head with a club and I suffer from severe headaches now. I don’t think I can forgive the far soldiers or the Interahamwe. I don’t want to hear about reconciliation. I accused them in the gacaca courts, including the one who raped me, those who participated in the killings in the church and those I saw at the roadblock, but now they are being released. Gacaca courts do not bring justice. I think the best punishment those men could get is the death penalty, because they killed others, too. We need justice. The génocidaires should not be released. I shared my testimony in order to help establish justice, and I hope it will do that.
```

---

## IC-2288: Missing Natalie and Victim

- Title: Missing Natalie and Victim
- Author (byline): Nicole Blackman
- Work: Blood Sugar
- Publisher: Akashic Books
- Publication date as stated: May 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: CAUTION
- Teaser before the introduction: Yes
- Spoken words (computed): 1719
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
CAUTION: These two selections are prose poems. Although they have won awards as PROSE -- we recommend checking with your tournament before entering this selection in the PROSE category.

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

## IC-2289: Mockingbird

- Title: Mockingbird
- Author (byline): Kathryn Erskine
- Work: Not specified
- Publisher: Philomel
- Publication date as stated: Apr 2010
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MRS. BROOK, CAITLIN, DOCTOR, NEWS REPORTER, LADY, MRS. BROOKS, DEVON, MRS. JOHNSON, DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 2058
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kathryn Erskine
ISBN: 978-0399252648
Publisher: Philomel
Date (Month/Year): Apr 2010
```

### Introduction (context only: never use it for content warnings)

```text
In Caitlin’s world everything is black and white. Anything in between is confusing. That’s the stuff her brother, Devon, always explained. But now Devon is dead, and Caitlin’s dad cries . . . A LOT. She wants to help, but as a ten-year-old girl with Asperger’s syndrome, she doesn’t know how. Then one day, on the news, she hears the word CLOsure and her life’s goal becomes a quest to find just that.

Mockingbird by Kathryn Erskine, who’s own daughter, Fiona, has Asperger’s as well.
```

### Performance text (classify this)

```text
(Pg 34) Sometimes I read the same books over and over and over. What’s great about books is that the stuff inside doesn’t change. People say you can’t judge a book by its cover but that’s not true because it says right on the cover what’s inside And no matter how many times you read that book the words and pictures don’t change You can open and close books a million times and they stay the same. They look the same. They say the same words. Books are not like people. Books are safe.

(Pg 10-16) Dad says it’s time to go back to school so here I am. Back in Mrs. Brook’s room. Sitting at the little round table. Mrs Brook says people have a hard time understanding me because I have Asperger’s so I have to try extra hard to understand them and that means working on emotions.

MRS. BROOK: Hi, Caitlin. So how are you? How are you feeling? (Caitlin sighs heavily and avoids making eye contact with Mrs. Brook) I think you’d like to forget about the painful events you’ve been through. The funeral must have been very difficult.

I wonder what she means. We sat in church. It was not very difficult. Everyone spoke so quietly I could barely hear them and almost no one talked to me. No one laughed like crashing glass and there was no lightning movement and no one appeared out of nowhere and nothing happened suddenly.

MRS. BROOK: Let’s Talk About it. (Caitlin turns her head away so she can’t see Mrs. Brooks anymore) I know it’s difficult but you can’t keep it all inside. Did you cry at the funeral?

CAITLIN: (Shaking her head) Dad cried. Please stop asking me questions.

MRS. BROOK: Caitlin. Your father is sad.

CAITLIN: Why?

MRS. BROOK: He misses Devon.

CAITLIN: Oh. MISS is a strange word. There is MISS like MISS Harper the principal. There is MISS like you will MISS your bus if you don’t hurry because you have to step on every crack. And there is MISS like dead.

MRS. BROOK: You’ll miss [Devon] but he’ll always be with you. Just in a different way.

I don’t want him around in a different way. I want him around in the same way. The way he was before. When he makes me popcorn and hot chocolate. And he tells me what to say and what clothes to wear and how not to be weird so kids won’t laugh at me. That’s the Devon I want. Not one who is floating around in the air. (Pg 63) At home I think about Devon’s Heart. I close my eyes and remember some of the things that happened on The Day Our Life Fell Apart. That’s what Dad calls it. After we came home from the hospital that night – with no Devon – Dad was yelling and kicking the furniture and the walls and shouting. Why? Why? WHY? Until I screamed at him: STOP IT! STOP IT! STOP IT! I press myself against the sofa and squish my eyes tight and even though I try not to I remember being at the hospital. People dressed in green pajamas and paper slippers said to Dad:

DOCTOR: We tried but we couldn’t close your son’s chest. His Heart – there was nothing left – there was nothing we could do. Nothing we could do.

(Pg 37) A gunshot wound to the Heart is almost always fatal. (Pg 65-71) [Dad] comes back into the living room and turns on the TV and stands there looking at it.

NEWS REPORTER: (with a microphone in his hand) I’m at the courthouse where the remaining killer from the Virginia Dare Middle School shooting has just had his preliminary hearing. The hearing found that there’s enough evidence against him to be put on trial for the murders of teacher Roberta Schneider and young students Julieanne Morris and Devon Smith. That horrific shooting was a devastating blow to this small community.

Dad goes to the bathroom and throws up. The camera switches to a lady sitting inside at the news desk.

LADY: We’ll hear more about this story later but isn’t it good that we now have closure.

I don’t think there is anything good about any of it. And I wonder how CLOsure can help. And what it is. I look up CLOsure and it says: the state of experiencing an emotional conclusion to a difficult life event such as the death of a loved one. I squeeze my Dictionary tight against my chest. I can hear Dad crying, so I close my eyes and plug my ears. [The next day] I wait all morning for my Mrs. Brook time. (to Mrs. Brook) Closure. How do I find it?

MRS. BROOK: Caitlin. Is this . . . are you talking about the news? The boy from the shooting? (she clasps her hands together, takes a deep breath and lets it out. Slowly. She closes her eyes)

CAITLIN: (to audience) Is she praying? (to Mrs. Brooks) This isn’t church.

MRS. BROOKS: I know. I’m thinking. Sometimes the process of a funeral and burial and doing things like putting wreaths on grave sites help give Closure.

CAITLIN: Devon was cremated so that will not work for me.

MRS. BROOKS: Sometimes talking can help both you [and your Dad] a lot. Talking about your feelings.

CAITLIN: That will not work for me. I don’t like Let’s Talk About It. – Is there anything else? (to audience) I start shaking my hands because the world is spinning and if I shake my hands faster than the rest of the world then the world’s spinning doesn’t seem so fast.

MRS. BROOKS: It’s something you have to find for yourself because everyone is different. We all have to find our own special way.

CAITLIN: (with a big sigh.) Fine. I will figure it out myself. (Pg 74-80) When Dad drives me home from school, I stand in front of Devon’s door. Whenever I don’t know what to do I go to Devon’s room and ask him. I REALLY want to know about Closure. Except Devon’s not here. But his room is. I haven’t been inside since Dad slammed the door on The Day Our Life Fell Apart. When I push my head into the soft blue blur of his room I can smell him and feel him. (Smiling) It’s like pure Devon in here. I see it. My hidey-hole. The best place in the world. The corner between the foot of his bed and his dresser. He even used his Boy Scout knife to carve my name underneath his dresser. (crouching down to see the underneath side of the dresser, Caitlin runs her fingers over her name) It’s not my real name. It’s Devon’s name for me which is Scout. It’s from To Kill a Mockingbird. It has two kids in it: Jem and Scout. They are a brother and a sister. The first time we watched To Kill a Mockingbird I waited through the whole movie for the dad to shoot a mockingbird. No one shot a bird for the whole entire movie. Devon said the title makes perfect sense and this is what it means:

DEVON: It’s wrong to shoot someone who is innocent and was never going to hurt you in the first place. You shouldn’t hurt innocent people Scout. That’s what it means.

I guess the evil school shooters didn’t listen in English class because they did not Get the meaning of that book at all. (Pg 148) [A few days later] my class goes to the computer lab. Mrs. Johnson says we have free time and can look up any topic we want to learn more about as long as it’s not computer games. I remember I should be researching Closure so I look it up and this is what I find: the act of bringing to an end; a conclusion – example: They finally brought the project to closure. I see Devon’s Eagle Scout project in my head. (Pg 2) It’s the chest Dad and Devon are making so he’ll be ready to teach other Boy Scouts how to build a chest. (Pg 149) I think about how much he wanted to finish it and become an Eagle Scout. And how he was going to teach me how to do woodworking too. And then I start shaking my hands fast and my heart is pounding in my ears. (Caitlin begins moaning)

MRS. JOHNSON: Caitlin are you all right?

CAITLIN: (Screaming loud enough for Devon to hear up in Heaven) I GET IT! I GET IT! I GET IT! I GET IT! (long pause, then, to audience) Now I know how to experience an emotional conclusion to a difficult life event. TRANSITION As excited as Caitlin is about finishing Devon’s Eagle Scout project, it’s difficult for her dad.

CAITLIN: (Pg 162-163) (to audience) Dad sighs and looks at the sheet covered chest in the corner for the first time ever and I want to start shaking my hands but I know that does not make Dad happy so I sit on them instead. (to Dad) Dad, I want to finish the chest. I want to get to Closure.

DAD: (quietly) I know

CAITLIN: You need to get to Closure too. (Dad nods) (To audience) I think about what Devon would say. (To Dad) You have to Work At It Dad. You have to try even if it’s hard and you think you can never do it and you just want to scream and hide and shake your hands over and over and over.

DAD: (wipes his eyes, as his body begins to shake with controlled sobs. He covers his face with his hands and tries to compose himself. He sniffs twice and then turns to Caitlin) How did you get to be so smart?

CAITLIN: (Shrugging) I’m really working hard on finesse.

DAD: Do you really want to do this? You think this will bring us Closure.

CAITLIN: (shaking her head) No. I know it will.

DAD: (Blowing a little air out of his nose, he nods and sighs heavily) Maybe we can make something good and strong and beautiful come out of this.

CAITLIN: (To audience) Good and strong and beautiful. I like those words. They sound like Devon.

DAD: Okay. Let’s do it.

CAITLIN: (Pg 202-204) (to Dad) Do you remember that movie?

DAD: What movie?

CAITLIN: To Kill a Mockingbird. It’s a good one isn’t it?

DAD: It’s been a long time since I’ve seen it but it was one of the best.

CAITLIN: Devon liked it too.

DAD: (clearing his throat and clenching and unclenching his hand) Yes, he did.

CAITLIN: Do you think I’m like Scout?

DAD: The little girl in the movie? (nods) Very much.

CAITLIN: You’re like Atticus. He was brave.

DAD: Thank you. (sighs again) I wish I were more like Atticus. [But] Honey . . . we have to live in the real world. I like you as Caitlin.

CAITLIN: But you said the movie was the best.

DAD: For a movie. But this is real life. A movie isn’t as good as real life. It can’t even compare.

CAITLIN: (To audience) Dad is wrong about that. A movie is better than real life because in the movies only the bad guys die . . . . TRANSITION And so the work on Devon’s Eagle Scout Project – Devon’s Chest begins

CAITLIN: (Pg 187-188) What is a Dad-oh?

DAD: (smiling a half smile) Day-doe. And it’s a grove in a piece of wood.

CAITLIN: (To audience) He is staring to smile. I know what that means. Closure must be coming! . . . So I Work At It (to Dad) I like Dad-oh better. Here’s the screwdriver, Dad-oh. Would you like a glass of water, Dad-oh? Can I help you, Dad-oh?

And his lips curl up on the left side every time. Closure is a very good thing to see. After Dad-oh goes to bed, I sneak into Devon’s room and borrow his Boy Scout knife. I slide my head under the chest and look for the perfect spot. I carve in big letters on his chest, just like Devon did for me: SCOUT! (Pg 212) [We worked on it together for weeks and now] our chest is almost done. I draw what I want to carve into the top part of it. The bird is gray and black and white and has a long tail. Her head is tilted up and her beak is open like she’s singing. She is beautiful. I run to the living room to show it to Dad.

DAD: (taking the drawing with one hand and rubbing his chin with the other – puzzled) It’s not . . . It doesn’t look [like an] eagle.

CAITLIN: It’s not an eagle. It’s a mockingbird.

DAD: (tiling his head to one side) I thought it was an eagle because this is Devon’s Eagle Scout project.

CAITLIN: It’s a mockingbird . . . like in the movie. Remember? Because Devon was like Jem. And I’m like Scout. And you Dad – you’re like Atticus. (Pg 218-219) (Caitlin suddenly begins to cry and can’t stop) Dad-oh! Dad! Oh Dad!

DAD: (pushing the hair from Caitlin’s face) What is it Caitlin?

CAITLIN: (between sobs) Devon . . . . Devon.

DAD: I know. It hurts. You miss him. I miss him.

CAITLIN: But I’m not crying for ME! I’m crying for Devon! I’m crying because I feel bad for HIM!

DAD: (smiling through his own tears) Now you know what it’s like to feel for other people.

CAITLIN: (To audience) I look over at Devon’s chest and it makes me feel good. (to Dad) We did a great job on it, didn’t we Dad? We made something good and strong and beautiful.

DAD: (nodding) We sure did. Devon would be very proud.

I nod too. I think about Devon and how he would show it to all the Scouts and tell everyone how we made it and how we used it to find Closure. That’s when I feel my mouth turn into a grin and my hands start shaking so hard I have to leap off the sofa and jump around the room because just shaking my hands isn’t enough for all the excitement. . . I finally Get it! I Get It! I GET IT!
```

---

## IC-2290: Music Lessons

- Title: Music Lessons
- Author (byline): Sarah Vowell
- Work: Take the Cannoli
- Publisher: Simon and Schuster
- Publication date as stated: April 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ACCIDENTAL LESSON #1, ACCIDENTAL LESSON #2, ACCIDENTAL LESSON #3, ACCIDENTAL LESSON #4, ACCIDENTAL LESSON #5
- Teaser before the introduction: Yes
- Spoken words (computed): 1696
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sarah Vowell
Book: Take the Cannoli
ISBN: 978-0743205405
Publisher: Simon and Schuster
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
Today, some of the coolest kids on campus can be found playing a tuba or beating a snare drum on the football field during halftime. Once considered the domain of dorks and geeks, students are now actually eager to be a part of their high school marching band. Unfortunately this was NOT always the case. Do you remember what it meant to be a band member when you were in high school? Music Lessons by Sarah Vowell.
```

### Performance text (classify this)

```text
It was autumn in America. A fine hot Indian summer day. Pretty high school girls sat on bleachers with the sun shining in their pretty hair, watching handsome high school boys play football. And then, it was halftime, which is where I came in . . . I was in marching band.

I had a foot-tall, fake fur black hat, with the "shako," strapped under my chin. It not only prevented me from breathing, it rendered me and my comrades in the horn section unstable, so that even though my job was to march around as some kind of sick metaphor for teenage military precision, I moved through time and space with the grace and confidence of a puppy walking on a beach ball. Because of my double shortage of strength and coordination, I barely passed gym. But somehow, I was supposed to lift a baritone horn that measured twice my body weight, blow into it while reading microscopic sheet music, step in a straight line while remembering left foot on beats one and three, right foot on beats two and four, and maneuver myself into cute visual formations. Halfway through the halftime program, I had to break formation, drop my baritone horn on the field, and sprint to the fifty-yard line. At midfield I picked up my mallets and -- this is what they had been waiting for -- I pounded out a xylophone solo on a little Latin-flavored number called "Tico Tico." My polo shirt-clad nemesis Andy Heap stood up in the stands screaming, "Whooooo! Whoooo!” This was the same Andy Heap, I might add, who earlier in the week in music history class had delivered an oral report on Tchaikovsky's lady friend, calling her Mimi throughout (even though her name was Nadya). Andy Heap was apparently smart enough to publicly humiliate me during "Tico Tico," he just wasn't smart enough to know that the abbreviation "Mme." stands not for Mimi, but "Madame." I only had a second to stick out my tongue at Andy when I finished "Tico Tico," because I had to let go of the mallets, rush over to my baritone-again, and I'm back in formation with the low brass for the finale. I was getting academic credit for this, to wear that uniform to play those songs. I was getting graded. Which begs the question: What exactly was I supposed to be learning? What was marching band supposed to teach me? Because marching isn't a particularly applicable skill in later life. Here then, some lessons -- actually useful ones -- I accidentally learned while pursuing music.

ACCIDENTAL LESSON #1: MARXISM FOR TENTH GRADERS Once a week, the best band kids played with the orchestra. I played the bass drum in orchestra, which meant that I never got to play. My par-ticipation ratio was something like seventy-five measures of rest per one big bass wallop. This gave me plenty of time to contemplate the class warfare of the situation. Here's what I figured out: Orchestra kids wear tuxedos. Band kids wear tuxedo T-shirts. The orchestra kids, with their brown woolens and Teutonic last names, had the well-scrubbed, dark blond aura of a Hitler Youth brigade. These were the sons and daughters of humanities professors. They took German. They played soccer. Dumping the fluorescent T-shirts of the band kids into the orchestra each week must have looked like tossing a handful of Skittles into a box of Swiss chocolates. But nothing brings kids together like hate. The one thing the band kids and the orchestra kids had in common was a unified disgust for the chorus kids, who were, to us, merely drama geeks with access to four-part harmony.

ACCIDENTAL LESSON #2: BIOLOGY AS DESTINY In seventh grade, I started band. I wanted to play the drums. My parents, who lived with me -- as was the custom in Montana -- did not want me to play the drums. So I picked the next loudest instrument instead -- the trumpet. How I loved my trumpet, the feel of it in my hands, its very volume and shine. I especially loved the illicitly named spit valve. In eighth grade, a teacher told me about this good old trumpet player I might like so I went out and bought one of his records. And every night, for over a year, I went to sleep listening to it, the same songs over and over, trying to figure out why Louis Armstrong was so moving, so funny, so good. I got caught up in this superstar talent of his right around the time I was beginning to suspect that I didn't have it, talent that is.

There was another problem which I discovered about three years into my trumpet career. I found out that the reason I had shoddy tone and trouble hitting the high notes was because of the shape of my jaw. I felt my life was more or less over. I was outraged that a person's fate could depend on something as arbitrary as the angles of her teeth. And not only that, I had to switch to a brass instrument with a bigger mouthpiece-the baritone horn. The baritone horn. Like, trumpets are played by Miles Davis and baritones are played by nobody.

ACCIDENTAL LESSON #3: HE'S SCHROEDER, l'M CHARLIE BROWN One of the reasons I knew I wasn't God's gift to music was that I went to school with him -- the living, breathing personification of entertainment -- Jon Wilson. Jon Wilson could play the piano. Like REALLY. PLAY. THE PIANO. He knew all the crowd-pleasing keyboard favorites. Kids would come up to him and request the Charlie Brown theme song or Van Halen's "Jump" so often I'm surprised he didn't roll a baby grand with an empty milk carton on tour into the junior high cafeteria and play for tips during lunch. The thing that bothered me about Jon Wilson, who was actually a pretty nice guy, was that people loved him! Loved him! And our friendly competition heated up when we both got serious about writing music. By fifteen, I was composing orchestral scores which went unperformed for the most part, and justifiably so. They were difficult, unlistenable, and wildly pretentious. Jon Wilson, on the other hand, wrote sentimental, professional quality love songs a la Lionel Richie and sang them after school in the band room to his fan base of swooning females. Pish-posh, I thought, alone in my two-by-three soundproof practice module that was more than roomy enough to accommodate my admirers. I was convinced that real artists were the kind that nobody understood, much less liked, which was pretty reassuring since nobody liked me. Or my music.

ACCIDENTAL LESSON #4: WHEN DOVES CRY From the time I was twelve until I finished high school at eighteen, my poor parents' calendar was blackened by an ambitious roster of concerts and recitals averaging at least one per month. They were always so gushy in their support, it never occurred to me that they might have preferred to avoid junior high school gymnasium performances of the theme from Rocky. They acted as though their world revolved around my sister and me, so that's what we believed. I remember one night, after an eighth-grade band concert, I caught a glimpse of pencil marks on my father's rolled-up program. He told me that he checked off each movement of each piece as it ended. Obviously because he was counting the seconds until he could go home. At the time, I took it badly. I was offended that he had so little regard for the seriousness of our thoughtful, well-rehearsed interpretation of "What Do You Do with a Drunken Sailor." Now, I see those pathetic little checkmarks as heart-shaped symbols of his love. Everyone says that love requires the utmost honesty, but that's not entirely true. Once I knew that my father was suffering for my sake -- really suffering -- I learned that love, especially the parental kind, requires the heartwarming sacrifice that can only accompany fake enthusiasm.

ACCIDENTAL LESSON #5: BIRTH OF THE COOL So: I was doomed at the trumpet. I was also acceptable at the baritone, shaky on the xylophone, and putrid on the piano. But there was one instrument for which I had an innate knack, an instrument I could play with some semblance of grace . . . the recorder. I taught myself to play it, and by fourteen, I was perhaps the youngest member of the American Recorder Society. I found out about an amateur ensemble that met once a week in my town. The members of the Bozeman Recorder Ensemble, as we were called, in-cluded a retired high school music teacher, two Montana State University math professors, and a number of housewives, one of whom had a daughter in my grade. I was the only member under the age of forty and most of them would have been eligible for the senior citizen discount at the music store. I played with them for a couple of years, until my pals Margaret and Leota and I broke off to form our own trio. At school, in all those actual hours of actual classes with actual teachers, music felt more like a job. Playing with Leota and Margaret was the first time -- the only time -- I actually enjoyed playing music. We played gigs, too, at the library, at street fairs. Imagine playing an Elizabethan ballad on the street with your two friends who happen to be older than your parents. You might look up from your music stand and notice one of your schoolmates staring on in horror. Andy Heap, for instance. But you know what? You don't care. You might even smile at him. And this is the most important lesson of marching band, of public displays of recorder. To withstand embarrassment. Maybe even seek it out. To take nerdiness to its most dizzying extremes, and stand before my peers with my head held high. To stick out my tongue at the Andy Heaps of the world, run back to the baritone horn of life, and blow mighty and proud. CLOSING [TRUMPET NOISE/FANFARE] Today, I salute all band members who were dedicated to their craft long before being a “Band Geek” was cool.
```

---

## IC-2291: My Boyfriend’s Back and There’s Gonna be Laundry

- Title: My Boyfriend’s Back and There’s Gonna be Laundry
- Author (byline): Sandra Shamas
- Work: Sandra Shamas: A Trilogy of Performances
- Publisher: Mercury Press
- Publication date as stated: Mar 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SANDRA, GUSHING WOMAN, FRANK
- Teaser before the introduction: Yes
- Spoken words (computed): 2067
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sandra Shamas
Book: Sandra Shamas: A Trilogy of Performances
ISBN: 978-1551280448
Publisher: Mercury Press
Date (Month/Year): Mar 1998
```

### Introduction (context only: never use it for content warnings)

```text
Being single sucks. Feeling as if you are not wanted, wondering if you are, in fact, too needy, expect too much, or aren’t worthy of being with anyone period. It’s a battle virtually every woman has had to conquer. But Sandra Shamas brings this single-womanhood dilemma home better than anyone else. Join me for a couple of weeks in the life of a single woman and I think you’ll recognize exactly where she’s coming from.

My Boyfriend’s Back and There’s Gonna be Laundry by Sandra Shamas
```

### Performance text (classify this)

```text
SANDRA: I'd like to start the evening off by offering you a performance art piece. I'm holding in my hands a sturdy pair of men's cotton briefs. Now, many of you won't even recognize these; so nice and flat and white, like this. Maybe I can help you recognize them, if I wad them up into a tight angry little ball. Maybe you'll recognize them better in their natural habitat: the floor.

SANDRA: Now, when you go to the magazine rack and you see the entire world of magazines that are available to women, all these magazines are pretty much the same. There's a wide variety of topics on each cover. You find "Fashion Tips," "Thin Thighs in 30 Days," "Lose 30 Pounds in Two Weeks," or little psychological pieces like "Five Things Men Fear." Inevitably, on the front cover of one of these magazines, there'll be an article entitled something like, "The Joy of Being Single." Biggest oxymoron in the world. A contradiction in terms. Like "jumbo shrimp," or "military intelligence.”

Now, these articles are there to help you be better at being single. 'Cause you're just not doing a good enough job. And they make suggestions to single women like, "take brisk walks," and "don't be afraid to dine alone." Have you ever done this? Have you ever dined alone? Okay. You go. You're upright. You're bathed. You're dressed. You're standing in front of the "Please wait to be seated" sign. The hostess comes over with a fan of menus, and she gives you that "Oh, you-poor-piece-of-s***, you-couldn't-find-anybody-to-eat-with-you" look, takes you to a table for two by the toilet, hands you one menu, and then abandons you. Because whatever you've got might be catching.

I eat over the sink. I dine alone with the sink. The nice, stainless steel placemat for one. I take the pot off the stove. I go to the sink. And I dine alone! But when I decided to be single, I envisioned my singledom to be a lot more romantic. In my singleness, I was a little taller, and willowy. And I wore a lot of white, gauzy cotton clothes that wafted around me. And my hair was shorter, but tawny-coloured. And I don't even know what colour that is. But whenever I read a Harlequin romance, the heroine always has "green, flashing eyes, and tawny hair." I WANT IT! So, what happens? What happens? You know, I turned my head away for a second, and into my life walks this guy. The one. He was, the one. How did I know he was the one? Because when I looked at this guy, I heard an operatic version of Star Trek music in my head. He was tall and lean and blond, blue-eyed, funny, bright, articulate . . . and younger. You get them young, you can train them. And his name was Frank. I fell in love with Frank. Now, I don't know about you, but when I fall in love, I give my brain . . . AWAY.

Nobody -- especially other single women -- wants to be around a woman who has just fallen in love. No. Well, you know why. It's because her voice goes up three octaves, it takes on a sickening sing-songy quality, and the sum total of her conversation is:

GUSHING WOMAN: And then you know what else he said? And he's so funny, and he's so smart. And, also, he's not like any man I've ever met before in my whole life. And he's so smart and he's so funny. You know what he said?

SANDRA: AH, SHUT UP! So there I was. I was in love love love love love. So, one day, the phone rings. "Hello." (It's Frank.) "Hiyee. How are you? What? Oh, I'd love to get together. It's so funny' cause I was just thinking about you and then the phone rings. Weird, eh? .. What? No, let's get together. I'd love that. Let's have coffee. Yeah . . . I know where it is . . . Yeah. I can be there in fifteen minutes . . . No problem. Okay. Bye . . . What? Oh, I'd love to talk to you, too . . . Okay . . . I'll see you there in fifteen . . . Okay. Bye-bye. . ." (pause) "Uh? No, you hang up first. Okay, we'll count together. "One . . . two . . . " I go to the cafe. Frank is already there. He is already sitting at a table for two. He has already ordered coffee. He's very handsome. And so I go and sit across from him. "Hello!" And he says seriously,

FRANK: Hi . . . um . . . thanks, ah . . . thanks very much for coming.

SANDRA: No trouble.

FRANK: Look, um . . . there's no easy way for me to say this . . .

SANDRA: Oh, then don't say it.

FRANK: Yeah, um . . . you know, ah . . . you know, I've, ah . . . I've been doing some thinking. . . and, ah. . . something I want you to know, it's not you, you know. But I really feel like things are going way too fast for me right now and I'm not ready, at all, to make any kind . . . of emotional . . . com . . . mit. . . ment.

SANDRA: Well, sing along if you know the words. Right away all the blood in my body went right into my head, and I could hear my heart in my ears. And nausea. And I'm looking right at him as hard as I can, I'm looking dead at him, and all I see is his mouth moving and no sound coming out. That voice in my head and says,

VOICE IN S’s HEAD: "DON’T LET *HIM* SEE YOU CRY!”

SANDRA: Tears come. (to herself) I can't help it. I can't help it.

VOICE IN S’s HEAD: STAND UP!

SANDRA: Okay. I'm up . . .

VOICE IN S’s HEAD: GO TO THE DOOR!

SANDRA: I don't know where the door is!

VOICE IN S’s HEAD: IT'S OVER THERE!

SANDRA: Oh, please. Please. What if he changes his mind?

VOICE IN S’s HEAD: HE HASN'T GOT A MIND TO CHANGE! GET OUTTA HERE!

SANDRA: So, where do you go? Where do you go when somebody says, "I'm not here for you anymore? Sorry!" Where do you go? Well, I don't know about you, but I like to turn my head down the path of self-destruction.

I'm diggin' in. I'm diggin' in for Stinky Pyjama Time. Stinky Pyjama Time. Maybe you know it. It does not have to be pyjamas. It can be bad track pants. Regardless, the outfit is a legged garment with the crotch way down around your knees. And you wear that with a completely mismatched top. Oh, [and] we never bathe during Stinky Pyjama Time. We never shave our legs. And if you're in SPT long enough, you can actually get the hair on your legs to start doing that giant kelp action in the tub.

Two weeks. Two weeks go by, and every day, I walk up and down the hall, crying. Sometimes, the phone would ring. I would answer it, but before I could talk I'd have to cough up a big hairball so the words could come out.

(on the phone) Hello? Oh, hi, Maria . . . No, no, man, I can't go out. . . Oh, yeah? . . . Yeah? . . . Where did you see him? . . . Oh, you had a party? At your house? . . . I didn't know you were having a party . . .

Oh, yeah? . . . Maria, did it look like he was with somebody? . . . Oh, yeah? . . . Did it look like he'd been crying for two weeks?"

No.

Now, whenever I want to take my mind off love lost, I do the laundry. I don't know what it is; I think it's just my need to be clean or to be in the basement communing with trolls. One or the other. Or both.

Now I'm still deep in Stinky Pyjama mode, but the light at the end of the tunnel comes by way of a fresh basket of laundry I've just done. So, the ironing board goes up. The iron starts getting hot. And I'm rummaging around in the basket . . . and whose shirt comes out? Frank's.

So, I lay it really lovingly on the ironing board, and I think, Okay, he'll see that this shirt is not at his house, and he'll come here. And he'll come here and he'll see that it's here and that I ironed it, and he'll say, "Oh, Sandra, I should never have left you because you're such a good ironer.

NEVER! Never, never, ever has a man gone for a woman because of her domestic prowess.

So, I'm at the board and I'm feeling so sad. And I'm crying and crying, and I'm thinking, It's me. It's because if me. If I were way more excellent, he would never have left. That's it. If I were way more excellent, he would never have left.

Think of something else! Think of something else . . . The phone rings. I shuffle over. "Hello." (It's Frank) "Oh, hello . . . No, I don't mind you calling . . . No, I wasn't doing anything, I was just, um . . . standing . . . How am I? Oh, I'm fine . . . Couldn't be better . . . Meet you for coffee? .. Yeah, I suppose I could meet you. . .in fifteen minutes . . . " (I catch a whiff of myself) "Make it sixteen . . . Okay . . . Bye."

Come on, Sandra, pull yourself together . . . C'mon. You can do it. . . I wanna go because I wanna see him but I don't wanna go because I'm afraid. No, I'm gonna cry . . . No. No. No crying. No crying!

So, I'm out the door, going towards the cafe, and I'm doing that shuffling, crying s***, you know, where there's heavy snot bubble action. I'm afraid to see him, but then I figure, he can only dump me once. I get to the cafe, and Frank is already sitting there at our table for two. He's already ordered coffee. He's very handsome, and he's beckoning for me to join him, so I do.

So, I sit across from him, and he says,

FRANK: Hi. Hi. It's really good to see you. You know . . . the last two weeks have been pretty hard on me. I was at the bookshop and I saw a book you were looking for and I knew you would love it and . . . uh . . . I couldn't call you. And late at night if I couldn't get to sleep, I'd go for a walk and sometimes I'd pass in front of your house and I'd see the light on in the living room and I'd think, maybe if I just looked in the window, I'd get to see her. . . . the truth of it is . . . I didn't expect to miss you . . . and I did. And I know I've got no right to ask, and I know I sound like a jerk, . . . but, is there any way you can see past what's happened and maybe give us a second . . . SANDRA: "YES!" . . . chance?"

SANDRA: You know, I like to think I hesitated a milli-second on that. So, we sat and we talked and talked and talked and talked and when the waitress came over, I put my brain on her tray. We had coffee after coffee after coffee and Frank quickly said

FRANK: Listen, do you want to go for a walk?

SANDRA: And we went out into that near perfect autumn night: clear, stars, crisp, beautiful. We walked and talked and walked and we ended up in front of my house. (to Frank) Gee, Frank, you know . . . do you feel like coming in and having a coffee? (to audience) So, we both go into the house and it's incredibly awkward. A remarkably awkward moment: we're standing in the living room and we both have our coats on. So Frank says, in an effort to break the ice,

FRANK: Why don't we see what's on TV?

SANDRA: Yeah, that's a great idea. (to audience) And we both reach down for the converter at the very same time, and our hands touch, and there's like this arc of electricity. Frank says,

FRANK: THE LAST ONE TO THE BEDROOM'S A DIRTY ROTTEN EGG!

SANDRA: And the bed has fresh sheets. I just did the laundry. Sometimes, God says "Yes."

The next morning, he had an early call, and he was gone at about seven. So I was alone in bed, and I was in that warm, rosy glow that only women really know. And I was so happy that my boyfriend was back. (Yay! Yay!) And I sat up in bed to start my day, and I just happened to look down on the floor. And there, there in the corner of the bedroom, on the floor, was his dirty underwear. And I thought to myself, Oh, I get it. My boyfriend's back, and there's gonna be laundry.
```

---

## IC-2292: My Left Breast

- Title: My Left Breast
- Author (byline): Susan Miller
- Work: The Best American Short Plays 1993-94
- Publisher: Applause Theatre Books
- Publication date as stated: 1995
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1428
- Already set (do not supply): none

### Source block (context only)

```text
Author: Susan Miller
Book: The Best American Short Plays 1993-94
ISBN: 978-1557831996
Publisher: Applause Theatre Books
Date (Month/Year): 1995
```

### Introduction (context only: never use it for content warnings)

```text
Every 13 minutes a woman dies of breast cancer. It is little wonder then that the fear of breast cancer takes a considerable emotional toll on many women. Because breast cancer is so common, almost person has known at least one woman who has been diagnosed with breast cancer, and many have lost friends or relatives to the disease. Consequently, breast cancer is, perhaps, the most feared illness among women.

And how do you face your fear . . . . George Carlin once stated “Those who dance are considered insane by those who can't hear the music.” But perhaps it’s not insanity . . . perhaps it is just one way to cope with the fear. At least it seems so for Susan Miller in her autobiography . . . My Left Breast.
```

### Performance text (classify this)

```text
NOTE: This cutting met the requirements for

PROSE by the National Speech and Debate

Association in 2008. Rules governing the PROSE

category have changed over time and this selection

no longer meets the requirements for PROSE by

the NSDA as it is a monologue from a play.

State rules governing PROSE vary from state to

state, so please verify your state’s current rules

before competing with this selection in the PROSE

category.

[I COME OUT DANCING. Then, after a moment.]

The night before I went to the hospital, that's what I did. I danced. [Indicates breasts.] One of these is not real. Can you tell which? [Beat.]

I was fourteen the first time a boy touched my breast. My left breast, in fact. I felt so guilty with pleasure I could hardly face my parents that night. [Beat.] Anyhow, breast cancer.

The year it happened my son was eight. He looked at my chest, the day I told him. We had these matching Pep Boys tee shirts. You know - Manny, Mo, and Jack. He looked at my chest and said, "Which one was it? Manny or Jack?"

"Jack," I tell him.

"What did they do with it?"

"I don't know."

He starts to cry. "Well, I'm going to get it back for you1"

Now he is twenty and I am still his mother. I am still here. We are still arguing. He is twenty and I wear his oversized boxer shorts with a belt and he borrows my jackets and we wear white tee shirts and torn jeans and he says, "Why don't you get a tattoo."

"A tattoo?"

"Over your scar. It'd be cool." [Beat.] Here's what I wear, sometimes, under my clothes. [Show BREAST PROSTHESIS to audience.] Don't worry. It's a spare. [Beat.]

When you go for a fitting, you can hear the women in the other booths. Some of them have lost their hair and shop for wigs. Some are very young and their mothers are thinking: Why didn't this happen to me, instead? And there's the feeling you had when you got your first bra, and the saleswoman cupped you to fit. Cupped you and yanked at the straps. Fastened you into the rest of your life. [Beat.]

I miss it but it's not a hand. I miss it but it's not my mind. I miss it but it's not the roof over my head. I miss it but it's not a word I need. It's not a sentence I can't live without. I miss it, but it's not a conversation with my son. It's not my courage or my lack of faith. [Beat.] I miss it.

A man I know said to me, Lesbians are the Chosen people these days. No AIDS. I said, Lesbians are women. Women get AIDS. Women get ovarian cancer. Women get breast cancer. Women die. In great numbers. In the silent epidemic. He said, I see what you mean. [Beat.] I miss it but I wouldn't have to if anyone paid attention to women's health care.

The surgeon in Los Angeles said it was a fibroadenoma. "Someday you might want to have it removed," he said. "But no rush. It's benign." I watched it grow. Then in New York, I saw another surgeon. He said, "What have you been told?"

"Fibroadenoma, " I say.

"Well, I'm concerned," he said. "I want to biopsy it."

You know how when everything is going right, you figure it's only a matter of time until that bus swerves on to the sidewalk or you finally make it to the post office to buy stamps and that's the day a crazed postal worker fires his Uzi into the crowd.

Everything was going right for me. I had just won an Obie for a play at the Public Theatre. I had a contract for my first novel- I was in the beginning chapters. And a new relationship.

The gynecologist said it was a gland. When it didn't go away, she sent me to the surgeon who said it was something it wasn't.

All of this happened at the beginning of a new decade. When we would all lose our innocence. It was 1980. In New York. I heard the Fourth of July fireworks from my hospital bed. I was thirty-six. I was too young. People were celebrating. And they were too young for the plague that was coming.

There were two positive nodes. I went through eleven months of chemotherapy and I had only one more month to go. But at my next to the last treatment, after they removed the IV, the oncologist and his nurse looked at me with what I distinctly recognized as menace. I thought, they're trying to kill me. If I come back again, they'll kill me. I never went back.

There are those who insist that certain types of people get cancer. So I wonder, are there certain types of people who get raped and tortured? Are there certain types who die young? Are there certain types of Bosnians, Somalians, Jews? Are there certain types of gay men? Are there certain types of children who are abused and caught in the crossfire? Is there a type of African American who is denied, excluded, lynched? Were the victims of the Killing Fields people who couldn't express themselves? And one out of eight women - count 'em folks - just holding on to their anger? This is my body - where the past and the future collide. This is my body. All at once, timely. All at once, chic. My deviations. My battlescars. My idiosyncratic response to the physical realm. The past deprivations and the future howl.

I am a One Breasted, Menopausal, Jewish Mom and I am the topic of our times. I am the hot issue. I am the cover of Newsweek, the editorial in the paper. I am a best seller. And I am coming soon to a theatre near you. Excuse me, I need to scream now. [SCREAMS.]

That was good. But what I really want to do is break a chair. [Beat]

I have destroyed so much property in my mind. I have smashed so many plates against the wall, ripped so many books from cover to cover. In my mind, I have trashed apartments, taken all the guilty parties to court. Done damage for damage done. But I'm the accommodating patient. I move on. Get over it. Exercise restraint. I am appropriate. [Beat]

I miss it but there is something growing in its place. And it is not a tougher skin. [Beat.] The doctor says my heart is more exposed now. Closer to the air. You don't have any protective tissue, she says. I hardly need a stethoscope to hear it beat. I cherish this scar. It's a mark of experience. It's the history of me. A permanent fix on the impermanence of it all. A line that suggests I take it seriously. Which I do. A line that suggests my beginning and my end. I have no other like it. I have no visible reminder of the baby I lost. Or the friend. No constant monument to the passing of my relationship. There is no other sign on my body that repeats the incongruity and dislocation, the alarm. A scar is a challenge to see ourselves as survivors, after all. Here is the evidence. The body repairs. And the human heart, even after it has broken into a million pieces, will make itself large again.

My son did get it back for me. In a way. Not the year it happened. But the year after that and the year and the year and the year after that. [Beat.]

It was little league that saved me. It was Jeremy up to the plate. It was Gabe Goldstein at second. It was Chris Chandler catching a pop fly. It was Jeremy stealing home. It was providing refreshments and washing his uniform. It was trying to get him to wear a jock strap. It was screaming, "Batter. Batter. Batter." It was Jeremy pitching the last out with the bases loaded. It was the Moms. The Moms and Dads and the coolers. It was the hats we wore and the blankets. It was driving him home from practice. It was his bloody knees. It was the sun going down on us, watching our sons and daughters play and be well. [Beat.] This was the cure for cancer.

I miss it, but I want to tell all the women out there, that we are still beautiful, we are still powerful, we are still sexy, we are still here.
```

---

## IC-2293: My Sergei

- Title: My Sergei
- Author (byline): Ekaterina Gordeeva
- Work: Chicken Soup for the Couple's Soul
- Publisher: HCI
- Publication date as stated: 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 958
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ekaterina Gordeeva
Book: Chicken Soup for the Couple's Soul
ISBN: 978-1558746466S
Publisher: HCI
Date (Month/Year): 1999
```

### Introduction (context only: never use it for content warnings)

```text
In the former Soviet Union, the sports establishment, charged with producing winners for the greater glory of the empire, had almost unlimited power over the athletically gifted. Children as young as five or six were identified, sent to special schools and given rigorous training in the sports in which they were expected to excel. Two such youngsters were Ekaterina Gordeeva and Sergei Grinkov, paired as skaters by their teachers when they were 11 and 14. As time passed and their joint career led to international championships, they fell in love and married. Their success culminated in Olympic gold medals in 1990 and 1994. And then, suddenly, Grinkov died of a heart attack in 1995 at age 28. The story of their love and their happiness together is deeply moving. My Sergei by Ekaterina Gordeeva
```

### Performance text (classify this)

```text
Not long ago I heard someone ask a friend, “If you had to live your life over again, what would you do differently?” I’ve thought about this, and for me, I’d like to live my life over again backward. Any day I’m living now, I would exchange for any day in the past because I know that for me to find the kind of happiness I had with Sergei isn’t possible. It’s like trying to find the comet that was in the night sky last spring, which passes Earth once in seventeen thousand years. No matter what lies ahead, the best years of my life will have been with my Seriozha, and those years are now laid to rest.

God took Sergei without warning – a heart attack on November 20, 1995. I lost my husband and best friend. I lost my favorite thing to do, because now I had no skating partner. It’s like I was living in a fairy tale before, and now I’ve been abandoned in a wild forest.

That is what life with Sergei was like, a fairy tale. It began the year I turned eleven. The pairs coach where I had skated since I was four, told me to come early to practice one day. He had chosen a skating partner for me. I was very excited because I knew it was going to be Sergei.

As a pairs skater, you have to learn everything you learned as a singles skater over again because you have to align your body with your partner’s. Sergei and I practiced the jumps endlessly. I was never scared of the lifts because I always felt very safe in Sergei’s arms. I’m not sure why, but once we were paired, I always believed Sergei was the only one who could skate with me.

Several years passed, we both grew up and we began preparing for the 1988 Olympics. As the games approached, everything became a little more stressful, a little more intense. In mid-November, during practice for an exhibition, Sergei caught his blade in a soft rut in the ice while holding me aloft and dropped me. The first part of my body to hit the ice was my forehead.

I didn’t feel any pain at first, then my entire head felt like it was splitting apart. I blacked out and was driven to the hospital. I ended up staying for six days. I’d suffered quite a serious concussion. I was mad at Sergei because I thought this fall was his mistake. Then, there was a knock on the door, and it was Sergei.

He was carrying a dozen roses, and he was very, very upset. Sergei continued to visit me at home every dat. When at last I could skate again, I immediately noticed a change in the way he was holding me. Something had happened in those two weeks, and I realized that his thoughts for me had changed. Before we had been like two skaters. After that, we were a pair.

I wondered, why me? Why am I so lucky? I was so young and small and shy, and Sergei could have had any nice long-legged girl. Why should he choose me? I believed he would love me just for a little while, and then it would be over.

We went on to win the gold medal at the 1988 Olympics in Calgary, Canada. And the following year Sergei and I were married, and our daughter, Daria, was born a year and a half later. Then in 1994 we won our second Olympic gold medal. The first gold medal we had won for the Soviet Union. This one we won for each other.

In 1995, we were training in Lake Placid for a fifty-five-city tour with the Stars on Ice. At the beginning of the program, I’m on one knee, and Sergei is on one knee, and we are face-to-face. I put my head on his shoulder, and I remember that his T-shirt smelled very clean. So I said, “Humm, smells good.” And he said, “Yes, it’s clean” Just that. They were to be his last words.

Then we started to skate. We did the early movements – the camel spin into a lift. The full orchestra was just coming in. Sergei was gliding on the ice, but he didn’t do the crossovers. His hand didn’t go around my waist for the lift. I thought it was his back, which had been bothering him for some time. He was bent over slightly, and I asked him, “Is it your back?” He shook his head a little. He tried to stop, but he kept gliding into the boards. He was dizzy, but he didn’t tell me what was happening. Then he bent his knees and ay down on the ice very carefully.

I kept asking what was happening. “What’s wrong, Seriozha? What’s the matter?” But he didn’t tell me. He didn’t speak at all.

Marina, our choreographer, stopped the music. When she came over to him, she knew right away it was something with his heart. It looked like he couldn’t breathe anymore. She told me to all 911, and she started doing CPR on him. I was so scared. I was screaming. I don’t know what. I forgot all the words in English. I couldn’t remember the word for help. I ran, crying, to get someone to call 911 for me.

By the time I got back, everyone was around Sergei, and the medical people were working on him, trying to get his heart going. Then the medical people were taking him in the ambulance, and I only had time to get my skates off and pick up Sergei’s bag.
```

---

## IC-2294: My Son, Ryan

- Title: My Son, Ryan
- Author (byline): Jeanne White
- Work: Chicken Soup for the Mother’s Soul
- Publisher: Health Communications, Inc.
- Publication date as stated: Oct 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1258
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jeanne White
Book: Chicken Soup for the Mother’s Soul
ISBN: 978-1558744608
Publisher: Health Communications, Inc.
Date (Month/Year): Oct 1997
```

### Introduction (context only: never use it for content warnings)

```text
Ruth Bell Graham once said, “As a mother, my job is to take care of what is possible and trust God with the impossible.” For not mother did these words ring more true than for Jeanne White the mother of Ryan White. But who was Ryan White? He was an American teenager from Kokomo, Indiana who became a national poster child for HIV/AIDS in the United States, after being expelled from middle school because of his infection. A hemophiliac, he became infected with HIV from a contaminated blood treatment and, when diagnosed in December 1984, was given six months to live. Doctors said he posed no risk to other students, but AIDS was poorly understood at the time, and when Ryan tried to return to school, many parents and teachers in Kokomo rallied against his attendance. A lengthy legal battle with the school system ensued, and media coverage of the case made White into a national celebrity and spokesman for AIDS research and public education. Surprising his doctors, Ryan lived five years longer than predicted and died in April 1990, one month prior to his high school graduation. My Son, Ryan by Jeanne White.
```

### Performance text (classify this)

```text
It has been seven years since my son, Ryan White died. Ryan had hemophilia, and he contracted AIDS from a blood product that hemophiliacs take to help their blood clot properly. This was before anyone really knew very much about AIDS. He was only 13 years old when he was diagnosed. The doctors told us then that Ryan would be lucky if he lived another six months.

Ryan lived six more years and was “the kid who put a face to the AIDS disease and helped to educate the nation.” President Clinton said that about my Ryan on the day that he signed the reauthorization of the Ryan White CARE Act. The Act provides medical and support services, medicine, home nursing and outpatient care to hundreds of thousands of people in America living with HIV. I know Ryan would be so happy that his life, and his death, have helped so many people.

In the beginning, when we first found out that Ryan had a fatal disease, I was totally and utterly devastated. I was a single mother of two kids who meant everything to me, and my son, my first-born, was going to die. I didn’t think I could go on. Then, on top of that nightmare, we had to deal with the ignorance, fear and hatred that surrounded AIDS at that time.

Ryan wanted to go back to school, but the school wouldn’t allow him to return. Parents were afraid their children could catch AIDS from being in the same room with Ryan. We fought for him to go to school and we won, but the community hostility and pressure were too much for our family. We decided to move to another town.

At Ryan’s new high school, it was a completely different story. The students actually went out of their way to welcome him: They organized AIDS education classes and arranged counseling to conquer any fear that still remained in any student. Educating the public about this disease became Ryan’s life, his career. Ryan became an international spokesperson for AIDS, appearing on television and in magazines and newspapers around the world. This helped to give meaning to what had happened to our family and ease some of our pain.

We learned to live with AIDS. The nightmare of the disease is that it brings you one powerful infection after another. I thought every cough, every fever might be his last. With AIDS, you never know whether a symptom is serious or mild. The patient is sick and then gets well, and no sooner does he get well than he is sick again.

Ryan was almost always in a good mood. Even when he had to go to the hospital, he’d try to give me a smile when I walked in the door. However, sometimes if he couldn’t do something – go to a particular concert, or meet some exciting people, or travel to an interesting place because he was too sick to too tied up with school – he’d get pouty and upset. Then I might scold him. He’d feel contrite and apologize right away. Maybe write me a note or send me a card.

A sick person would have to be downright saintly never to give in to crankiness. And if you’re the one giving care, you can’t ever take an angry outburst personally – because it’s really the illness spreading or the medication speaking and not the true loving heart inside.

One day Ryan just grabbed my hand and started swinging it.

“Now, Ryan, when you do something as nice as this, you must want something.”

“I don’t want anything. Can’t a son hold his mother’s hand?”

“Come on now, Ryan . . . “

“No, really, Mom. I want to thank you for all you’ve done for me. Standing by me like you’ve done.”

No one can ever take those words away from me. No one can ever take away what I felt that day as a mother.

I remember someone once asked me, “How do you live, Jeanne, day to day, knowing that your son is going to die?”

I answered, “We don’t think about death. We don’t have time for it. IF you allow it into your life, it will eat you up. You have to go on with your life, making the most of every day and every hour.”

Finally the time came when Ryan’s body couldn’t keep going. When Ryan was dying, the hospital staff must have thought we were insane. Here’s this comatose kid, on life support, with a half-crazy mother calling his name, talking to him while he slept. He probably couldn’t hear a thing, but we brought him music. He couldn’t’ see a thing, but we stood precariously on chairs, hanging decorative posters and banners on the walls above the screens and the wires and the bleeping monitors. We didn’t want to give up on him.

Yet as I stood there watching Ryan’s thin little body, I knew there was nothing more anybody could do. Before he drifted into unconsciousness, Ryan had told me, “If you think there’s a chance, Mom, go for it.” We did. Until the last second, we went for everything we could.

I leaned down close to him and whispered, “It’s okay, son. You can let go.”

Then he died. They revived him for a few minutes. Momentarily he would die again: I knew that perfectly well. I knew there was no chance. But still, to have to call the battle lost . . . it was a moment of inexpressible sorrow for me and my family.

“If you want, you can tell them no more,” a close friend said. “It’s up to you, Jeanne.”

I talked to my parents, and to Ryan’s sister, Andrea. Then I told the doctors, “No more,.”

Dr. Marty Kleiman, who had taken care of Ryan from the beginning, who helped him live for almost six years when other physicians predicted that he would die in six months, went out and made the announcement that my boy had passed away in his sleep, without pain.

The sparkle was gone.

Now, seven years later, the sparkle is slowly returning. My state of mind is like the dawn these days. I look forward to everything. I love being married. My new husband, Roy, has made my life fun again. My daughter, Andrea, has grown into a strong, smart, beautiful person. I look forward to everything our life has in store for us – adventures, travels, grandchildren. On the edge of the sky just beyond a cloud, I think I really see the end of the plague of AIDS. Every day, people whose lives once seemed to be finished are bursting with new health. The cure is coming. It’s almost here. I feel that I will live to see it. What greater gift can anyone receive than this sense of happy anticipation?

The garden has been my therapy. Here among the flowers and the bright fruit, when the light is brand new and everything is fresh and wet and the leaves are beaded up with dewdrops, I work in the household of nature and refresh my spirit. It seems to me that every weed I pull is a bit of grief I am learning to set aside, a tear I’ve weeded out so that good cheer can grow again.

I see in the faces of the flowers all the friends I have lost: I see my son’s face. They are beautiful in the new morning, opening like smiles and shining with hope.

Thank you, Lord, for another day.
```

---

## IC-2295: My Stepmother, Myself

- Title: My Stepmother, Myself
- Author (byline): Garrison Keillor
- Work: Happy to Be Here
- Publisher: Penguin Books
- Publication date as stated: April 1990
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NEWSCASTER, SNOW, GRETEL, CINDERELLA
- Teaser before the introduction: Yes
- Spoken words (computed): 1449
- Already set (do not supply): none

### Source block (context only)

```text
Author: Garrison Keillor
Book: Happy to Be Here
ISBN: 978-0140131826
Publisher: Penguin Books
Date (Month/Year): April 1990
```

### Introduction (context only: never use it for content warnings)

```text
My Stepmother, Myself by Garrison Keillor
```

### Performance text (classify this)

```text
NEWSCASTER: (Pg 183-188) Recently in Pennsylvania, a woman was dismissed from her job and driven over a cliff by an angry mob of villagers carrying flaming torches and hurling sharp rocks after they learned that she was married to a man who had custody of his three children by a previous marriage.

In California, soon after her marriage to a prince, Sharon Mittel was shut up in a dungeon under the provisions of the Cruel and Unnatural Parent Act, which allows the immediate imprisonment of a stepparent upon the complaint of a stepchild. The prince's oldest daughter accused Sharon of slapping her. She now faces a series of tests to prove her innocence. She also must answer some riddles.

Are these merely two isolated incidents? Or are they, as a new and exhaustive report on stepmothers points out, fairly indicative?

"The myth of the evil stepmother is still with us. Stepmothers are still associated with the words cruel and wicked, which has made them easy targets for torture and banishment as well as severely limiting their employment, particularly in professions such as nursing, social work, and education. In general, stepmothers are not only underpaid and underemployed but also feared and despised."

Recently, three stepdaughters whose relationships with their stepmothers are well known agreed to speak out and set the record straight. Because each has suffered from publicity in the past and is trying to lead a normal a life, only first names will be used.

SNOW: The story the press told was that I was that I escaped from stepmother and was taken in by dwarves and she found me and poisoned me with an apple, and I was dead and the prince fell in love with me and brought me back to life and we got married, et cetera, et cetera. And this is what I believed right up to the day I walked out on him. I felt like I owed my life to Jeff because he had begged the dwarves for my body and carried it away and so the apple was shaken loose from my throat. That's why I married him. Out of gratitude.

As I look back on it, I can see that that was a very poor basis for a relationship. I was traumatized, I had been lying in a coffin under glass for years, and I got up and married the first guy I laid eyes on. The big prince. My hero.

Now I can see how sick our marriage was. He was always begging me to lie still and close my eyes and hold my breath. He could only relate to me as a dead person. He couldn't accept me as a living woman with needs and desires of my own. It is very hard for a woman to come to terms with the fact that her husband is a necrophiliac, because, of course, when it all starts, you aren't aware of what's going on -- you're dead.

In trying to come to terms with myself, I've had to come to terms with my stepmother and her envy of my beauty, which made our relationship so destructive. She was a victim of the male attitude that prizes youth over maturity when it comes to women. Men can't dominate the mature woman, so they equate youth with beauty. In fact, she was beautiful, but the mirror (which, of course, reflected that male attitude) presented her with a poor self-image and turned her against me.

But the press never wrote the truth about that. Or about the dwarves. All I can say is that they should have been named Dopey, Sleepy, Slimy, Sleazy, Dirty, Disgusting, and Sexist. The fact is that I knew the apple was poisoned. For me, it was the only way out.

GRETEL: When Hansel and I negotiated the sale of book rights to Grimm Bros., he and I retained the right of final approval of the manuscript and agreed to split the proceeds fifty-fifty. We shook hands on it and I thought the deal was set, but then his lawyers put me under a spell, and when I woke up, they had rewritten the contract and the book too! I couldn't believe it! Not only did the new contract cut me out but the book was pure fiction.

Suddenly he was portrayed as the strong and resourceful one, a regular little knight, and I came off as a weak sister. Dad was shown as a loving father who was talked into abandoning us in the forest by Gladys, our "wicked" stepmother. Nothing could be further from the truth.

My brother was a basket case from the moment the birds ate his breadcrumbs. He lay down in a heap and whimpered, and I had to slap him a couple times hard to make him walk. Now the little wiener makes himself out to be the hero who kept telling me, "Don't cry, Gretel." Ha! The only crying I did was from sheer exhaustion carrying him on my back.

As for Dad, he was no bleeding heart. He was very much into that whole woodcutter/ peasant/ yeoman scene -- cockfighting, bullbaiting, going to the village to get drunk and watch a garroting or a boiling -- don't kid yourself! Gladys couldn't send us to our rooms without his say-so. The truth is that he was in favor of the forest idea from the word go.

What I can't understand is why they had to lie about it. Many parents left their children in the forest in those days. It was nothing unusual. Nowadays, we tend to forget that famine can be a very difficult experience for a family. For many parents, ditching the kids was not only a solution, it was an act of faith. They believed that ravens would bring morsels of food, or that wolves would take care of the kids, or a frog would, or that the fairies would step in. Dwarves, a hermit, a band of pilgrims, a kindly shepherd, somebody. And they were right.

I don't mean to say that it wasn't a trying experience, an emotional experience. It was. And yet there isn't a single documented case of a child left in the forest who suffered any lasting damage. You look at those children today and you will find they are better people for having gone through it. Except for my brother, that is. The little jerk. He and my father live in luxurious manors, and I live above an alchemist's shop in a tiny garret they call a condo. As for Gladys, she was kicked out without so much as a property settlement. She didn't even get half of the hut.

I guess, back then, I wasn't prepared to see that Gladys, in proposing the forest as a viable alternative, was offering me independence at a very early age. I wish I had been able to thank her.

CINDERELLA: A woman in my position does not find it easy to "come out of the palace," so to speak, and to provide intimate details of her personal life. I do so only because I believe it is time to put the Cinderella myth to rest once and for all -- the myth that one can escape housework by marrying a prince.

The truth is that I am busier than ever. Supervising a large household staff -- cooks, maids, footmen, ladies-in-waiting, a bard or two -- is hard work. Often I find myself longing for the "good old days" when my stepmother made me sweep the hearth.

We see each other almost every day -- she comes up here and we play tennis or I go down there for lunch - - and we often reminisce and laugh about our little disagreements. She is one of my best friends. Other people treat me like royalty, but she treats me like a real person. My husband won't let me touch a broom, but I go to her house and she puts me to work! I love it. I tell her, "Mother, you're the only one who yells at me. Don't ever stop." And I mean it. Anger is real. It's honest.

Honesty is a rare commodity in a palace, and that is why so many "fairy-tale" marriages end up on the rocks. You wouldn't believe the amount of fawning and flattering that goes on! Between the courtiers bowing and scraping and the suppliants and petitioners wheedling and whining, and the scheming of bishops and barons, not to mention the sorcery and witchcraft, the atmosphere is such that it's terribly hard for a man and a woman to establish a loving, trusting, sharing type of relationship . . . It's true that we lived happily ever after, but believe me, we have had to work at it!
```

---

## IC-2296: New York Regional Mormon Singles Halloween Dance

- Title: New York Regional Mormon Singles Halloween Dance
- Author (byline): Elna Baker
- Work: Not specified
- Publisher: Dutton Adult
- Publication date as stated: Oct 2009
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ELNA, MOTHER, FATHER, FRIEND, RANDOM MALE, CHURCH MAN, DAVE
- Teaser before the introduction: Yes
- Spoken words (computed): 1924
- Already set (do not supply): none

### Source block (context only)

```text
Author: Elna Baker
ISBN: 978-0525951353
Publisher: Dutton Adult
Date (Month/Year): Oct 2009
```

### Introduction (context only: never use it for content warnings)

```text
New York Regional Mormon Singles Halloween Dance by Elna Baker -- where the costumes are creative, the rules are strict, and the dating pool is deeply committed to not touching you.
```

### Performance text (classify this)

```text
(hum or sing “Party in the USA” by Miley Cyrus *)

ELNA: (Pg 12) (stuffing a cookie in her mouth) [Welcome to the] New York Regional Mormon Singles Halloween Dance. That’s right -- it’s a Halloween dance for all the single Mormons between the ages of 18 and 30 who live in the tristate area. That’s a lot of virgins in one room. And I’m one of them.

Tonight I’m dressed like a Queen Bee. The best part of my costume is my stinger. I bought a black funnel from the hardware store and stuck it on my butt. (turn and wiggle) Genius! I was certain that some Mormon guy was going to see me and fall head over heels in love. I joked to my friends that the Queen Bee was going to find a drone. Instead, I’m by myself at the punch bowl stocking up on Oreo cookies. When I’m wrong, I’m wrong and strong.

The worst part is, I should’ve known better. This is my 4th New York Regional Mormon Singles Halloween Dance in a row -- a lame dance held in a church gym. Every year, I come hoping to meet “The One.” And every year, I leave by myself, vowing never to come again. But by the time 365 days have passed, I’ve completely forgotten this commitment. In the end, I am here for one reason and one reason only: I want very much to fall in love.

ELNA: (Pg 12-13) [That’s right!] The dance rules. The most important one, announced over the pulpit on Sunday, is that there is to be no cross-dressing or wearing of masks. I understand the logic behind no cross-dressing, though I doubt that if a man were to dress like a woman at this function he would suddenly realize his true identity. But masks? Two: there is to be no inappropriate dancing or lascivious behavior. That’s why there are too many lights overhead and only “safe” songs like “Cotton-eyed Joe” on the sound system. (**dance and sing/hum a few lines from the song). When slow songs do play people joke that you should be able to fit Old Testament, New Testament, The Book of Mormon, Doctrine and Covenants, and Pearl of Great Price between you and your partner. . . or you’re dancing too close.

If it weren’t already painfully obvious, these events are organized to facilitate marriage. How else would we Mormons meet, marry, then make more Mormons? (Take that, Sally and your seashells on the seashore.) Contrary to popular belief, there are Mormons who live in New York City. I don’t know how many of us there are all together, but there are probably 800 single Mormons and at least 20,000 former Mormons.

I moved to New York to go to NYU for acting (strike a dramatic pose) (Pg 14-15) My parents wanted me to go to BYU, Brigham Young University, in Provo, Utah. They were worried that if I didn’t go to BYU, I’d stop being Mormon, and I wouldn’t meet anyone to marry. Well, they were right about the second part. When I got my letter of acceptance to NYU, my mother was terrified, so she sat me down for a mother-daughter talk. (they begin packing Elna’s suitcase)

MOTHER: (nervously) Elna, the first thing that will happen when you move to New York is, you might start to swear. And swearing will lead to drinking. And drinking will lead to doing drugs. (beat) And Elna, (pursing her lips) what would you do if a lesbian tried to make out with you? (crosses her arms, waiting for an answer)

ELNA: (holding back laughter) I was used to her saying words like church calling and relief society. Not the word lesbian, let alone lesbian and make out in the same sentence. It was awesome!

If you followed my mother’s logic, each step was a progression toward becoming more of a sinner. First I’d swear, then I’d drink, then I’d do drugs. By that point I was getting used to the narrative, so I assumed sex with men would be next. But no—my mother skipped that altogether and jumped to my becoming a lesbian. Did my mother honestly think that I had a better chance with a woman than a man? (composing herself; to mother) I’d say, ‘No, thank you . . . lesbian.’

MOTHER: (rolling her eyes) There are these clubs in New York where men pay larger women to dance with very little clothing on; don’t do that.

ELNA: (to audience) Great, my mom thinks I’m moving to the big city to become a lesbian stripper. Apparently, when she told me I was “special,” this is what she meant. (Pg 16) That’s when my mother saw it, among my tightly folded clothes: a rainbow scarf. It reminded me of Punky Brewster in a retro eighties sort of way.

MOTHER: (snatching it out) You can’t wear this in New York! Everyone will think that you’re gay.

ELNA: (to audience) My mother thought gay people had a monopoly on rainbows. In my opinion rainbows are for everyone, like unicorns. (to mother) Mom, I’m not gay.

MOTHER: I know, but you should avoid the appearance.

ELNA: (to audience) I tried to get my scarf back. I explained how cold I would be without it. I even tried to usher her into this century by explaining that wearing rainbows didn’t automatically mean a person was gay. The Lucky Charms leprechaun was not necessarily a homosexual. The Care Bear with the rainbow on his tummy did not have a life partner. He didn’t even have genitals. Eventually my mom gave me money to buy a new scarf. But she was not, under any circumstances, going to let me take the rainbow scarf to New York City.

(Pg 15) My father sat me down a few days later for another leaving-the-nest talk. His advice was a little different.

FATHER: Elna, never forget these three things. Number One: Never wear a dead man’s socks. Number Two: Never let ’em see you sweat. And Number Three: Never touch a fat man’s stomach.

ELNA: (exaggerated confused look) That was all the advice I was given before moving to New York City. (Pg 17) When I walked into my dorm room, the first thing I noticed was a big rainbow flag hanging on the wall. The only way it could have possibly gotten better would have been if my roommate walked in smoking a cigarette and offered to give me a lap dance. I’d never actually met a lesbian until I met Lisa. It turned out Lisa had never met a Mormon until she met me. And despite all the things we were supposed to be, we hit it off right from the start.

(Pg 18-19) I guess this probably isn’t the kind of stuff most Mormons would even acknowledge. But then again, I’ve always been different from most Mormons. Mormonism can sound pretty farfetched: Joseph Smith digs up golden plates and translates them into a book, The Book of Mormon. This book ends up being a history of the ancestors of the Native Americans, who originated in Jerusalem and believed in Jesus. When you write it all out like that you can’t help but reconsider. Once I tried explaining it to a friend. I went into all the things that I believed. I thought I was doing a good job explaining everything until he said . . .

FRIEND: So basically according to you, Pocahontas was actually a Jew?

ELNA: (Pg 123-124) (distracted by events at the dance) Ohhhh! It’s time for the talent show!

RANDOM MALE: (rapping with a microphone)
Hey brothers and sisters, Listen to me,
I’m talking to you religiously,
My Mormon Rap will make you see,
That I’m as funky as Donny and Marie.
Mormon, Mormon Rap, Do the Mo-mo-mo-mo-
mormon Rap.
I’m a fine young man, I’m living clean,
Don’t smoke, Don’t drink, If you know what I mean.
Flipp’n, fetch’n, scruddle-dee-me,
Jiminy cricket, and fiddledy-dee!

ELNA: (clapping politely, then turns to the audience) [Where were we? . . . Oh yes,] (Pg 19) The miracles one is expected to believe in the Mormon faith are no different from the miracles you are supposed to believe in any faith. My problem is I was always a skeptic.

When I was four and my mom first told me the story of Moses parting the Red Sea with his hands, I looked at her and said, “Yeah right, Mom.” My mother tried to convince me that Moses had indeed parted a sea just by lifting his arms. I rolled my eyes and patted her on the knee like she was a crazy person.

By the age of six, I was already asking my mother, “When do we graduate from church?” To my dismay I was told that the word to describe being done with church was not “graduate” – it was death.

And I wasn’t exactly enthusiastic about getting baptized. Mormons are baptized at eight years old. According to my parents and teachers, when you were baptized you were washed clean. So why get baptized at eight? None of us had done anything. Why not wait until we were seventy? That way you could lead a fun life, do whatever you wanted to, and have a Get Out of Jail Free card at the end.

(Pg 21-22) When I was 19, I read The Book of Mormon cover-to-cover for the first time. And while I was reading it, I felt like I was leading a better life and making better choices. But [if] I’m being honest. I think most religious people experience just as much doubt as they do faith. And I don’t think doubting makes you bad. I think it makes you smart. (Pg 144) If everyone based their faith on common sense no one would be religious— faith is totally illogical.

(Pg 22) A few Sundays ago, some idiot stood up in church and started talking about how we were having such a mild autumn. He went on and on about how pleasant the weather was and then jumped to,

CHURCH MAN: So really if you think about it, it’s a sign that Jesus Christ [is] coming soon.

ELNA: And so began my usual downward spiral: The weather is warm because of climate change not because Jesus is on his way. How can I belong to a church where people believe such crazy things? I mean, nowhere in The Book of Mormon does it say mild autumn equals Jesus, but technically I’m supposed to believe in the second coming. Do I? I don’t know. How can I possibly sign my name to something I don’t entirely agree with?

(distracted again) Oh, hold on. A guy, Dave, totally hot, just made eye contact with me. He’s dressed as Paul Bunyan, which would be cool if 2 other guys hadn’t also thought of it. Wait, I think he’s walking in my direction. Oh, my gosh, he is. What do I do? Okay. Just play it cool. Show him your stinger.

(adjust slightly and wiggle stinger)

DAVE: (Pg 23) How’s it going?

ELNA: (flirting awkwardly) Fine. Where’s Babe?(Dave looks incredibly confused) Paul Bunyan traveled with a blue ox.

DAVE: I’m not Paul Bunyan. (annoyed) I’m Brigham Young! (struts off)

ELNA: (choking on a cookie and calling after him) Sorry, the fake beard threw me off. (to audience) I should’ve stopped there, but instead I added . . . (calling after Dave) So the women who’ve been congregating around you all night, they weren’t your multiple wives? (to audience) I thought this was pretty funny. Dave didn’t even laugh. Mormons don’t know how to laugh at themselves. (beat)

(Pg 25-26) After four years of being a Mormon in New York, I’ve become a reluctant spokesperson for my faith. I’m constantly answering questions or explaining my religion. Every question is about whether I’m a polygamist, whether I’ve had sex, whether I wear magic underwear, and whether I believe in dinosaurs. For the record: I’m not a polygamist, I have not had sex, I don’t wear magic underwear, and I do believe in dinosaurs.

[But] there are Mormon stereotypes: Mormons have big families; they’re from Utah; they wear modest clothes; they’re friendly, naive people; they have white teeth; and they’re Republican. But that list only scratches the surface.

(Pg 29) I [just] am a Mormon in New York. A Mormon in New York seeking another Mormon in New York. Which brings me back to: The New York Regional Mormon Singles Halloween Dance. (Pg 161) [This is] the year I meet the Morman man of my dreams. (digs down deep for courage . . .) (Pg 89) Let’s Dance! (sing and do a few dance moves to the Macarena***)
```

---

## IC-2297: Not the Phil Donahue Show

- Title: Not the Phil Donahue Show
- Author (byline): Kelly Cherry
- Work: The Society of Friends: Stories
- Publisher: University of Missouri Press
- Publication date as stated: Sept 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1555
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kelly Cherry
Book: The Society of Friends: Stories
ISBN: 978-0826212436
Publisher: University of Missouri Press
Date (Month/Year): Sept 1999
```

### Introduction (context only: never use it for content warnings)

```text
The Mother / Daughter relationship is one of the most complex relationships that exists in our society. Mothers want things for their daughters: weddings and grandchildren and lives that other people won’t judge. Mothers want their daughters to go to college and have careers and be proud of who they are. All of these desires become threatened when a daughter confides in her mother that she is gay. Not the Phil Donahue Show by Kelly Cherry
```

### Performance text (classify this)

```text
This is not the Phil Donahue show; this is my life. So why is my daughter, who is 20 years old and, to me, so heartbreakingly beautiful that I think that for the sake of the health of the entire world and probably universe she shouldn't be allowed out of the house without a cardiologist at her side, why is my daughter standing in my doorway telling me she's a lesbian?

If I say it's a phase, that she'll outgrow it, she'll peel herself from the wall like wallpaper and exit, perhaps permanently,

If I say honey, that's great, nonchalant and accepting as history, I could be consigning her to a life that I'm not sure she really wants—maybe she's just testing me. Maybe this is just a phase.

It is five o'clock. It's already been a long day, which I have spent as I spend most of my days—nursing patients to whom I have let myself get too close. But I'm always home from my shift at the hospital by four-thirty, while lan stays late after school to devise lesson plans, tutor the sluggardly, confer with parents.

Now the front door swings open and it's lan. Isabel has not moved from her post in the doorway between us.

"Hi, Shel," lan says to me. "Hi, Belle," he says to my daughter. "Nice to see you."

He wants so much for her to let him enter her life. He has no children of his own—he wants to be, if not a second father, at least a good friend.

"Isabel has an announcement," I say

"I'm in love," I hear her say behind my back.

"Hey, that's great," lan responds and I realize how unfair we have been to him, we have set him up for this.

"With a woman," she says.

Girl, I want to correct her. With a girl.

"Oh," lan says. "Well, why isn't she here? When do we get to meet her?"

And I remember: this is why I married him. Because he puts people ahead of his expectations for them. Because he doesn't create a crisis where there isn't one.

But this is a crisis. If she were his daughter, he'd realize that.

As soon as Ian suggested we meet, Isabel raced out of the house and brought her back for supper.

Judy is not what I expected. For one thing, she's pretty— almost as pretty as my daughter.. It is easy to see why Isabel has fallen in love with her; in fact, I don't see how anyone could not fall in love with either of them—so why shouldn't they fall in love with each other?

"They are children," I say to lan in the kitchen, after they have vanished into the night.

"Isabel's almost 21," he says. "You've got to start getting used to the idea that she's grown up. She has her own life to live."

"That's easy for you to say."

He slams the silverware drawer shut. "No, it isn't, Shelley. As a matter of fact, it's very hard for me to say, because I know you're upset and you're going to take it out on me. It would be much easier for me not to say anything, but someone has to keep you from making a big mistake here."

"Call Nelson. Maybe he can keep you from going off the deep end."

I look at lan; I pick up the phone; I dial. It rings. "Nel?" I say. "I need to talk to you. Can you meet me at Porta Bella?"

"In 20 minutes," he says. "Listen, I know what it's about. Everything's going to be all right."

"She told you first?" I ask. I can't help it, I'm hurt.

"It's hard on her, our divorce," he says. "I'm happy things have worked out for you with lan, but you must realize she senses a barrier there now. There's not the same unimpeded access to you that she had."

"Do you think she's doing this just to get back at me? Will she grow out of it?"

"I think it's the real thing, Shelley," he says. He smiles. "I think she's in love . . . She's still our little girl."

"She always will be," I agree. "And she's free to be herself. It's just that, well, weren't you counting on grandchildren someday?"

"I wouldn't rule out the possibility yet," he says. "A lot of lesbians have children, one way or another. I think she wants to have children someday."

The next day . . . . . Gloved and gowned, I duck into Reed's room.

Reed has AIDS. He has been here before, during two other episodes of acute infection. This time he has pneumonia. This time, when he leaves here, he will go to a nursing home to die.

Reed lies there on his back, with his eyes shut, as if drifting farther and farther from shore.

"Reed," I say to call him back.

I believe the dementia that occurs in 80 percent of AIDS patients has begun to manifest itself, but it's hard to say. I don't know what Reed was like before he became an AIDS patient.

I pull up a chair and sit beside him. The skinnier he gets, the more room his eyes take up in his face. He winks at me.

"Hello, Shelley," he says.

"I thought for a minute you'd forgotten me."

"I still have my mind, Shelley, It's just my body that's going."

I don't contradict him. He knows everything there is to know at this point about his disease. He knows more about it than I do—like many AIDS victims, he has read the research, questioned the doctors, exchanged information. At the limits of knowledge, the issue becomes belief, and I figure he has a right to choose his beliefs. Reed believes he will lick his illness.

I look at the body that's going: He has lost more weight since his last hospitalization, despite a rigorous fitness plan. His cheekbones are as pointy as elbows. His brown eyes have lost some of their laughter. When I pick up his hand to hold it, it doesn't squeeze back. There are sores on his arms—the giveaway lesions of Karposi's Sarcoma. K. S. , we say around here. I take his pulse, the wrist between my fingers and thumb not much bigger than a sugar tube.

"Reed," I ask him, "are you sorry you're gay?" I almost say were. As in were gay. Or sorry you were gay.

"Because of this?"

"No. Just—if there were no such thing as AIDS, if nobody ever died from it, would you be glad to be gay?"

"How can I answer that? How can I pretend Eddie never died?"

Eddie was his lover; he died of AIDS two years ago, in California. Reed came back home, but his parents, small dairy farmers in northern Wisconsin, have been unable, or perhaps unwilling, to look after him.

Tears leap to his eyes, those tears, and others to mine., "Why are you interrogating me about my feelings like this? This is not the Phil Donahue show! This is my life!"

I understand that. All over America, people are struggling to prove to themselves that their lives are more than television, that their lives are real, the real thing.

I think of all the things he might have said, the true profanity of his condition, and it seems to me that no words could ever be as shocking as "Phil" and "Donahue" and "Show," words that have brought America into this hospital room

I don't care what kind of life Isabel leads, so long as she gets to lead one.

I think of my beautiful daughter, her grumpy spirit caged by the circumstances of her own sexuality and her mother's, and of how it will one day—soon, I think—be freed, free to be itself.

Not that I wouldn't prefer things to be otherwise; not that I am exactly happy about my daughter's choice. I wouldn't go so far as that—not yet. I love her too much not to know that the day will come when I will feel however I must feel in order to keep her in my life.

Sometimes I think of the whole world as a kind of hospital, the earth itself as a patient.

There are days, now, when so much seems to be slipping away. Even the things one tends not to think of, like the walnuts. The walnuts are slipping away, going off to be stockpiled by squirrels. The green of summer is slipping away, hiding its light under a bush or a bushel of autumn leaves. There are dreams that slip away in the middle of the night, losing themselves forever in some dark corner of the subconscious. There are stars that are disappearing even as we look at them. There are mothers and fathers and children, all of them slipping away like the fish in the pond, going down deeper for winter. And you reach out to hold on to your child, and she is slipping away, going off into some life that is not your life, and you are afraid to see her go because you know, you know how far it is possible to go, how far it is possible for things to slip away.
```

---

## IC-2298: Nothing but a Smile

- Title: Nothing but a Smile
- Author (byline): Laurie Notaro
- Work: The Idiot Girls’ Action-Adventure Club
- Publisher: Villard Books
- Publication date as stated: July 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MOTHER, LAURIE, SISTER, BF, LADY
- Teaser before the introduction: No
- Spoken words (computed): 1120
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laurie Notaro
Book: The Idiot Girls’ Action-Adventure Club
ISBN: 978-0375760914
Publisher: Villard Books
Date (Month/Year): July 2002
```

### Introduction (context only: never use it for content warnings)

```text
In middle school – even in high school, getting changed for gym class is a workout in itself to avoid anyone seeing anyone else naked. Many girls line up to change in the few bathroom stalls. I’m not that extreme, but I certainly use some contortionist moves to never be topless in front of my classmates. No one gets fully naked in the locker rooms and we certainly don’t walk around in the nude.

But in the “real world” things are a bit different . . . Maybe adults are more confident about their bodies . . . but Holy Kamole! I’m just saying . . . the next time you go to the Y or your local gym be prepared to avoid eye contact. ARGHHHH!

Nothing but a Smile by Lori Notaro
```

### Performance text (classify this)

```text
It was my first real day at the new gym, since I had been blackballed from the community college fitness center when they found out I smoked. Eager to start a new habit that would shrink my butt from a couch to a love seat, I was going to begin exercising. I had just opened my locker and had slapped on the new lock I had bought at Target the day before, when it happened.

She walked by me, then headed toward a bench across the aisle. Standing in front of me was a naked lady, fresh from the shower. A completely naked lady. With no clothes on. I don't even know what my first instinct was. I don't think I had one. Al I knew was that a naked lady was standing in front of me, and I was staring at her being naked. I guess I just couldn't believe it. I had never really seen a naked lady before, except for one time when I was five, and my mom let our hippie neighbor, Honey, take me shopping with her and her five-year-old daughter. Honey took both of us into the dressing room with her, and before I knew what was happening, there was Honey's left "lentil" just hanging there, wide out in the open. I looked at Honey's daughter, who didn't seem too bothered by it, but personally, I was horrified. I was five AND I was a Catholic. The whole thing was just DIRTY. I felt as if I had just witnessed something unholy and shameful, and I never told anyone that filthy secret, not even at confession, until just now. I'm sorry that I kept this from you, Mom, but it's true. I saw Honey's lentil. I felt dirty then, and I felt dirty now. It was happening all over, but not only were there lentils, there were things my mother never taught me the names of, but then again, I was a little sheltered. Until I was a junior in high school, my mom insisted that the Kotex pads under the bathroom sink were special sponges she used to clean the toilet. The naked lady, now bending over to dry her legs off, was showing me a whole other view, like her marshmallows. "Just what is going on here?" is what I wanted to say to the naked lady, because I didn't know this woman. I had no business seeing her NAKED, especially since there was a bathroom stall several feet away. I had no right, and, furthermore, I had no idea when I paid for my gym membership that I had also joined a nudist colony. Who could be that free? I thought. Who could be that free that they could just strut around "in all candor" in front of other people? Who has that much self-esteem that they could bare it all and not burst into tears? I mean, I have trouble walking from the bath mat to the shower without any clothes on, let alone put on a show for a bunch of strangers. My bra doesn't come off until the sun goes down, and that's the law. I feel perverted if my dog catches a glimpse of me in all my glory, let alone someone I've never even met. When I have to go to the gynecologist, I have to practice sitting on the edge of my bed with no pants on for a week before my appointment, just to get ready. Obviously, the naked lady had no such problems. I didn't know what to do, and I was so freaked out that I forgot the combination to my new lock. I went home and called my mother.

MOTHER: (from the other end of the phone) You saw a streaker? That is just disgusting. And there was a bathroom stall five feet away? Some people are raised like animals, barnyard animals! They never heard of Sodom and Gomorrah?

LAURIE: (shaking head) I don't know.

MOTHER: When your sister and I joined that gym last year. there were so many of them walking around that I just had to stop going. It was like a topless bar! I felt like I should be handing out dollar bills! 'Here's one for you, here's one for you . . . ' The last thing I need is to see strangers' lentils! How do I tell that to a priest? You should just stay home and run in place like I do. Then my sister got on the phone.

SISTER: Once, when I was in the locker room, I met a friend of mine that owed me money for a lunch, and she wrote me a check right then and there. Com-pletely naked.

LAURIE: What did you do?

SISTER: I cashed the check and bought a Tae- Bo videotape. And I run in place when no one else is home. I can't go to the gym anymore. There's so many naked people around that I feel like I'm in a porno movie. And as for my friend, well . . . I can't eat lunch with someone like that. She can be wearing seven sweaters and a parka, but she'll always be naked to me.

When my boyfriend came home from work that night, he asked me about my first day at the gym, but I told him how the naked lady scared me so badly I had to go home.

BF: You thought she was dirty, didn't you?

LAURIE: Yes, Yes, I did. He just shrugged his shoulders and said,

BF: So? It's a gym, Laurie. People have to take showers. And you're kind of . . . repressed. I can't believe you've never seen a naked lady before.

LAURIE: Well, it's not like all of us girls go into the Gap dressing room, take off our clothes, and chase and tickle one another.

BF: What about your family? You never saw any of them naked? I gasped, sucking in a breath so hard it nearly knocked me backward.

LAURIE: (slowly) We're a very careful people. We don't believe in naked!

BF: It's very normal to be naked in the locker room. (trying to calm her down) If you go back, you're probably going to see more naked people.

LAURIE: Yeah? Well, I'm not playing games with them. And I'm not wiping off anybody's back! A couple days later, I got up enough courage to go back to the gym. I was getting ready to put my new lock on my locker when I heard an elderly, grandmotherly voice call out to me.

LADY: (gently) Dear? Young lady? Could you please help me? I've dropped my comb, and I can't seem to reach it.

LAURIE: Oh, sure. I picked it up and started to hand it to her, but as I looked up into her sweet little grandmother face, I saw that the only thing she was wearing was a smile.
```

---

## IC-2299: Now I Need a Place to Hide Away

- Title: Now I Need a Place to Hide Away
- Author (byline): Ann Hood
- Work: New York Times
- Publisher: New York Times
- Publication date as stated: February 26, 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1533
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ann Hood
Book: New York Times
ISBN: Newspaper
Publisher: New York Times
Date (Month/Year): February 26, 2006
```

### Introduction (context only: never use it for content warnings)

```text
The music of the Beatles embraced the emotions of a nation; the power of their lyrics speak just as clearly to us today as they did 40 years ago, urging us to take notice, take time, be aware of our feelings. Today I urge you to take the time to smell your babies shampooed hair...and touch their little hands and faces and hold them close to you...for such is the time old women and men rejoice and can only look back and remember the sweet smile of a child. Now I need a Place to Hide Away by Ann Hood
```

### Performance text (classify this)

```text
It is difficult to hide from the Beatles. After all these years they are still regularly in the news. Their songs play on oldies stations, countdowns and best-ofs. There is always some Beatles anniversary: the first No. 1 song, the first time in the United States, a birthday, an anniversary, a milestone, a Broadway show. But hide from the Beatles I must. Or, in some cases, escape. One day in the grocery store, when “Eight Days a Week” came on, I had to leave my cartful of food and run out. Stepping into an elevator that’s blasting a peppy Muzak version of “Hey Jude” is enough to send me home to bed.

Of course it wasn’t always this way. I used to love everything about the Beatles. As a child I memorized their birthdays, their tragic life stories, the words to all of their songs. I collected Beatles trading cards in bubble gum packs and wore a charm bracelet of dangling Beatles’ heads and guitars. For days my cousin Debbie and I argued over whether “Penny Lane” and its flip side, “Strawberry Fields Forever,” had been worth waiting for. I struggled to understand “Sergeant Pepper”; I marveled over the brilliance of the White Album. My cousins and I used to play Beatle wives. We all wanted to be married to Paul, but John was O.K. too. None of us wanted Ringo. Or even worse, George.

It was too easy to love Paul. Those bedroom eyes. That mop of hair. Classically cute. When I was 8, I asked my mother if she thought I might someday marry Paul McCartney.

“Well, honey,” she said, taking a long drag on her Pall Mall. “Somebody will. Maybe it’ll be you.”

In fifth grade, in a diary in which I mostly wrote, It is so boring here, or simply, Bored, only one entry stands out: I just heard on the radio that Paul got married. Oh, please, God, don’t let it be true.

It was true, and I mourned for far too long.

Of course by the time I was in high school, I understood my folly. John was the best Beatle: sarcastic, funny, interesting looking. That long thin nose. Those round wire-rimmed glasses. By then I didn’t want to be anybody’s wife. But I did want a boy like John, someone who spoke his mind, got into trouble, swore a lot and wrote poetry.

WHEN I did get married and then had children, it was Beatles’ songs I sang to them at night. As one of the youngest of 24 cousins, I had never held an infant or baby-sat. I didn’t know any lullabies, so I sang Sam and Grace to sleep with “I Will” and “P.S. I Love You.”

Eventually Sam fell in love with Broadway musicals and abandoned the Beatles.

But not Grace. She embraced them with all the fervor that I had. Her taste was quirky, mature.

“What’s the song where the man is standing, holding his head?” she asked, frowning, and before long I had unearthed my old “Help!” album, and the two of us were singing, “Here I stand, head in hand.”

For Grace’s fourth Christmas, Santa brought her all of the Beatles’ movies on video, a photo book of their career and “The Beatles 1” tape. Before long, playing “Eight Days a Week” as loud as possible became our anthem. Even Sam sang along and admitted that it was arguably the best song ever written.

Best of all about my daughter the Beatles fan was that by the time she was 5, she already had fallen for John. Paul’s traditional good looks did not win her over. Instead she liked John’s nasally voice, his dark side. After watching the biopic “Downbeat,” she said Stu was her favorite. But since he was dead, she would settle for John. Once I overheard her arguing with a first-grade boy who didn’t believe that there had been another Beatle.

“There were two other Beatles,” Grace told him, disgusted. “Stu and Pete Best.” She rolled her eyes and stomped off in her glittery shoes.

Sometimes, before she fell asleep, she would make me tell her stories about John’s mother dying, how the band met in Liverpool and how when Paul wrote the tune for “Yesterday,” he sang the words “scrambled eggs” to it.

After I would drop Sam off at school and continue with Grace to her kindergarten, she’d have me play one of her Beatles tapes. She would sing along the whole way there: “Scrambled eggs, all my troubles seemed so far away.”

On the day George Harrison died, Grace acted as if she had lost a friend, walking sad and teary-eyed around the house, shaking her head in disbelief. She asked if we could play just Beatles music all day, and we did. That night we watched a retrospective on George.

Feeling guilty, I confessed that he was the one none of us wanted to marry.

“George?” Grace said, stunned. “But he’s great.”

Five months later, on a beautiful April morning, Grace and I took Sam to school, then got in the car and sang along with “I Want to Hold Your Hand” while we drove. Before she left, she asked me to cue the tape so that as soon as she got back in the car that afternoon, she could hear “You’ve Got to Hide Your Love Away” right from the beginning. That was the last time we listened to our Beatles together.

The next day Grace spiked a fever and died from a virulent form of strep. Briefly, as she lay in the I.C.U., the nurses told us to bring in some of her favorite music. My husband ran out to his car and grabbed “1” from the tape deck. Then he put it in the hospital’s tape deck, and we climbed on the bed with our daughter and sang her “Love Me Do.” Despite the tubes and machines struggling to keep her alive, Grace smiled at us as we sang to her.

At her memorial service 8-year-old Sam, wearing a bright red bow tie, stood in front of the hundreds of people there and sang “Eight Days a Week” loud enough for his sister, wherever she had gone, to hear him. That evening I gathered all of my Beatles music — the dusty albums, the tapes that littered the floor of my car, the CD’s that filled our stereo — and put them in a box with Grace’s copies of the Beatles’ movies. I could not pause over any of them.

Instead I threw them in carelessly and fast, knowing that the sight of those black-and-white faces on “Revolver,” or the dizzying colors of “Sergeant Pepper,” or even the cartoon drawings from “Yellow Submarine,” the very things that had made me so happy a week earlier, were now too painful even to glimpse. As parents do, I had shared my passions with my children. And when it came to the Beatles, Grace had seized my passion and made it her own. But with her death, that passion was turned upside-down, and rather than bring joy, the Beatles haunted me.

I couldn’t bear to hear even the opening chords of “Yesterday” or a cover of “Michelle.” In the car I started listening only to talk radio to avoid a Beatles song catching me by surprise and touching off another round of sobbing.

I TRIED to shield myself from the Beatles altogether — their music, images, conversations about them — but it’s hard, if not impossible. How, for example, am I supposed to ask Sam not to pick out their music slowly during his guitar lessons?

Back in the 60’s, in my aunt’s family room with the knotty-pine walls and Zenith TV, with my female cousins all around me, our hair straight and long, our bangs in our eyes, the air thick with our parents’ cigarette smoke and the harmonies of the Beatles, I believed there was no love greater than mine for Paul McCartney.

Sometimes now, alone, I find myself singing softly. “And when at last I find you, your song will fill the air,” I sing to Grace, imagining her blue eyes shining behind her own little wire-rimmed glasses, her feet tapping in time. “Love you whenever we’re together, love you when we’re apart.” It was once my favorite love song, silent now in its White Album cover in my basement.

How foolish I was to have fallen so easily for Paul while overlooking John and George, to have believed that everything I could ever want was right there in that family room of my childhood: cousins, TV, my favorite music. But mostly I feel foolish for believing that my time with my daughter would never end. Or perhaps that is love: a leap of faith, a belief in the impossible, the ability to believe that a little girl in a small town in Rhode Island would grow up to marry Paul McCartney. Or for a grieving woman to believe that a mother’s love is so strong that the child she lost can still hear her singing a lullaby.
```

---

## IC-2300: One of those Hideous Books where the Mother Dies

- Title: One of those Hideous Books where the Mother Dies
- Author (byline): Sonya Sones
- Work: Not specified
- Publisher: Simon and Schuster
- Publication date as stated: April 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 880
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sonya Sones
ISBN: 978-0689858208
Publisher: Simon and Schuster
Date (Month/Year): April 2004
```

### Introduction (context only: never use it for content warnings)

```text
Once upon a time there was a girl whose life fell apart before it began. This girl wasn’t a princess from a fairytale or a heroine from one of those adventure novels. She didn’t want it, but her life seemed to follow the plot of “One of those Hideous Book where the Mother Dies” by Sonya Sones.
```

### Performance text (classify this)

```text
CAUTION - This is a Novel in Verse. We recommend checking with your regional, state or national tournament before entering this selection in PROSE. The UIL (Texas) and KSHSAA (Kansas) have deemed this selection to be Poetry.

I'm not that depressed,
considering that this
gigantic silver bullet with wings
is blasting me away from my whole entire life,
away from Lizzie Brody,
my best friend in the world,
away from Ray Johnston,
my first real boyfriend.
Not that depressed,
considering I've been kidnapped
by this monstrous steel pterodactyl
and it's flying me all the way to L.A.
to live with my father
who I've never even met
because he's such a scumbag
that he divorced my mother
before I was even born.
I'd say I'm doing reasonably well,
considering I'm being dragged
three thousand miles away from all my friends
and my school and my aunt Duffy
and the house I've lived in ever since I was born,
three thousand miles away from my mother,
and my mother's grave,
where she lies in a cold wooden box
under six feet of dirt,
just beginning to rot.
I'm not that depressed
considering that I'm trapped
on this jumbo poison dart
shooting me away from everything I love,
and there's this real weird guy
sitting in the seat right behind mine,
who keeps picking his nose
and eating it.
Depressed?
Who? Me?
Aunt Duffy Drove Me to the Airport
And there was a second there
when I actually considered
getting down on my hands and knees
and begging her not to put me on this plane,
begging her not to send me away,
pleading with her to let me stay in Boston
and live with her instead.
But Duffy's so nice that I knew she'd say yes
and I knew that that would make me feel
like crawling under a boulder,
because her apartment just has
this one microscopic bedroom
and now that she's finally
got herself a new boyfriend,
the last thing she needs
is to have her fifteen-year-old niece
permanently camped out in her living room,
which is barely even big enough
to fit her couch.
So I contained my urge to grovel.
My Mother Hated Flying
Especially after September 11th.
She used to squeeze my hand so hard
during takeoffs and landings
that she'd cut off my circulation.
She'd screw her eyes closed and whisper this silly
prayer someone taught her once.
Something about manifold divine blessings being unto
the plane or the universe or some hippie-dippy thing like
that.

And if there was even a teensy bit of turbulence —
forget it.
She'd start apologizing to me
for every mean thing she'd ever said
or done or even thought about doing.
This morning,
when the plane was lurching down the runway
and I didn't have Mom's hand to hold,
my heart flung itself up into my throat.
And for a minute there,
I couldn't even breathe.
I didn't know how much
I depended on
being depended on
by her.
Peach Fuzz
When the flight attendant
leans in to ask me
if I'd like something to drink,
and the sun splashes across her face,
I notice
all these tiny little
blond hairs on her cheeks,
and tears rush into my eyes.
My mother had them, too.
I used to tease her about them.
Called it her peach fuzz.
It used to make her laugh.
If I could reach out
and stroke those little hairs
on the flight attendant's face,
without totally freaking her out,
I'd close my eyes
and I'd do it right now.
I'd touch my mother's cheek
one more time.
Maybe You're Wondering About It
But that's just tough.
Because I'm not even going to go in
to how she died.
Let's just say she knew that she was sick,
that she felt it burrowing,
felt it gnawing at her insides.
But the doctors wouldn't listen.
And when they finally found it,
there was nothing they could do.
Nothing she could do.
Nothing I could do.
Nothing.
Let's just say
she wasted away into a toothpick,
and leave it at that, okay?
That after a while
she was just a shadow
lying there on her bed.
Oh.
And I guess we can say
that I was holding her hand
when it finally happened.
I Love to Read
But my life better not turn out
to be like one of those hideous books
where the mother dies
and so the girl has to
go live with her absentee father
and he turns out to be
an alcoholic heroin addict
who brutally beats her
and sexually molests her
thereby causing her to become
a bulimic ax murderer.
I love to read,
but I can't stand books like that.
And I flat out refuse
to have one of those lives
that I wouldn't even want
to read about.
And Speaking of Fathers
As soon as I was old enough
to notice that I didn't have one,
I started asking questions.
Like, "Where's my daddy?"
And, "How come Lizzie has a daddy,
but I don't?"

Mom's face would sort of slam shut
and all she'd say was,
"He divorced me before you were born."
If it wasn't for my aunt Duffy
I'd never have even found out
who my father was.
```

---

## IC-2301: Out There

- Title: Out There
- Author (byline): Jo Ann Beard
- Work: Boys of My Youth, Pgs 144-151
- Publisher: Back Bay Books
- Publication date as stated: Jan 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1503
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jo Ann Beard
Book: Boys of My Youth, Pgs 144-151
ISBN: 978-0316085250
Publisher: Back Bay Books
Date (Month/Year): Jan 1999
```

### Introduction (context only: never use it for content warnings)

```text
Have you ever wanted to embark on a solo road trip as a woman, but talked yourself out of it for what seems like a million reasons? News reports of women violently attacked, carjacked, robbed, raped, or worse simply because they were driving alone. Decomposing bodies discovered by hikers and hunters, their bodies long abandoned. Images taped to tollbooth windows: Missing! Reward offered for her safe return. And yet despite the fear, many women still choose to travel alone, balancing their desire for independence with the need to stay safe . . .

Out There by Jo Ann Beard
```

### Performance text (classify this)

```text
(Pg 144-151) It isn't even eight A.M. and I'm hot. I'm fifty miles from the motel and about a thousand and a half from home, in a little white Mazda with 140,000 miles on it. I'm all alone in Alabama, with only a cooler and a tape deck for company. It's already in the high 80s. Yesterday, coming up from the keys through Florida, I had a day-long anxiety attack. I kept thinking I saw alligators at the edge of the highway.

There were about four hundred exploded armadillos, too, but I got used to them. They were real, and real dead. I'm running away from running away from home. I bolted four weeks ago, leaving my husband to tend the dogs. He doesn't love me anymore, it's both trite and true. After thir-teen years he came to realize that the more successful he got, the less he loved me. That's how he put it, late one night. He won that screaming match. He said, gently and sadly, "I feel sort of embarrassed of you." I said, "Of what? The way I look? The way I act?" And he said, softly, "Everything, sort of." And it was true.

Well, I decided to take a trip to Florida. Key West for four weeks, writing and seething and striking up conversations with strangers. I had my 35th birthday there, weeping into a basket of shrimp. Boy, do I need a cup of coffee.

At the end of this trip I will have driven 3,999 miles all alone, me and the windshield, me and the radio, me and the creepy alligators. Don't ask me why I didn't get that last mile in. I didn't though, and 4,000 sounds like a lot more than 3,999 does; I feel sort of embarrassed for myself.

My window is broken, the crank fell off in Tallahassee on the way down. In order to roll it up or down I have to put the crank back on and turn it slowly and carefully, using one hand to push up the glass. So, mostly I leave it down.

I'm on a little four-lane blacktop running through the Alabama countryside. It's pretty, too, better than Florida, which was billboards and condos built on old dump sites. This is like driving between rolling emerald carpets. You can't see the two lanes going in the opposite direction because there's a screen of trees. I'm starting to get in a good mood again.

Little convenience store, stuck out in the middle of nothing, a stain on the carpet. I'm gassing up, getting some coffee. My shirt is gaping open and I have nothing underneath it, but who cares, I'll never see these people again. What do I care what Alabama thinks about me. This is an unusual attitude for me. I'm practicing in anticipation of being dumped by my husband when I get back to Iowa.

I swagger from the gas pump to the store. I bring my coffee cup along and fill it at the counter. Various men, oldish and grungy, sit at tables eating eggs with wadded-up toast. They stare at me while they chew. I ignore them and pay the woman at the counter. She's smoking a cigarette so I envy her.

When I leave, the men are still staring in a sullen way. I rearrange all my junk so I have everything handy, choose a Neil Young tape, pop it in and then move back out on the highway. Back to the emerald carpet and the road home. Iowa is creeping toward me like a panther.

All I do is sing when I drive. Sing and think. On the way down I would weep uncontrollably, but I'm past that now. Now I suffer bouts of free-floating hostility, which is much better. I plan to use it when I get home.

A car swings up alongside me so I pause my singing until it goes past. People who sing in their cars cheer me up, but I'd rather not be caught doing it. On the road, we're all singing, picking our noses, embarrassing ourselves wildly; it gets tiresome. I pause and hum, but the car sticks alongside me so I glance over. It's a guy. He grins and makes a lewd gesture with his mouth. It's disgusting. (demonstrates, tongue darting in and out, quickly) A python testing its food.

Who do these men think they are? I've had my fill of it. He picked the wrong day to mess with me! I give him the finger, slowly and deliberately [then] take a sip of coffee.

He's still there. I can't believe this! He followed me from that convenience store. He has on a fishing hat with lures stuck in it. I saw him back there, but I can't remember if he was sitting with the other men or by himself. He's big, overweight, and dirty. His passenger-side window is down. He begins screaming at me.

The road is endless, there is nothing, no cars, no anything. The other two lanes still invisible behind their screen of trees. I'm all alone out here. With him -- screaming and screaming at me, reaching out his right arm like he's throttling me. I speed up. He speeds up, too, next to me. We're only a few feet apart, my window won't roll up. He's got slobber on his face. I slam on my brakes and for an instant he's ahead of me, I can breathe, then he slams on his brakes and we're next to each other again. [And] he's screaming he wants to kill me -- screaming and screaming. I stare straight ahead, hands at ten and two.

The front end of his car is moving into my lane. He's saying he'll cut me with a knife, how he'll do it -- I can't listen. The front end of his Impala is about four inches from my little white Mazda. I am absolutely terrified.

[But] I refuse to give him an inch. If I do, he'll have me off the road in an instant. I speed up, he speeds up, I slow down, he slows down. If I give him an inch, he'll shove me off the road get his hands on me, then the end will begin in some unimaginable, unspeakable style. There will be blood, he won't want me to die quickly. I cannot let him push me over onto the gravel. His car noses less than two inches from mine; I'm getting rattled. My God, he can almost reach me through his window; he's moved over in his seat, driving just with the left hand. I move toward the center of the car, carefully, without swerving.

In the rearview mirror a speck appears. Don't look, watch your front end. I glance up again; it's a trucker. Suddenly a road appears on the right, a dirty and rutted thing leading off into the trees. He hits the brakes, drops behind, and takes it. In my rearview mirror I see that the license plate on the front of his car is buried in dried mud. That road is where he was hoping to push me. He wanted to push my car off the highway and get me on that road. He was hoping to do what maniacs, furious men do to women alongside roads, in woods.

By force of will, I slow down to 65, and wait for the truck to overtake me. As it moves in front of me I speed up enough to stay two car lengths behind it. It says England on the back, ornate red letters outlined in black. England.

That guy chased me on purpose, he hated me, with more passion than anyone has ever felt for me. Ever.

Out there are all those decomposing bodies, all those disappeared daughters, discovered by joggers and hunters, their bodies long abandoned, the memory of final desperate moments lingering on the leaves, the trees, the mindless stumps and mushrooms. Images taped to tollbooth windows, faces pressed into the dirt alongside a path somewhere.

I want to roll my window up, but l'd have to stop and get the crank out and lift it by hand. I'm too scared. He's out there still, waiting behind the screen of trees. I have to follow England until I'm out of Alabama.

(thinking aloud) Green car, old Impala, unreadable license plate; lots of rust. Seat covers made out of that spongy stuff, something on the dashboard, a coffee cup or a sad Jesus. The fishing hat with a sweat ring around it right above the brim. Lures with feathers and barbs. I've never been so close to so much hatred in my whole life. He wanted to kill me. Me, of all people. Me.

I got onto the interstate, had the nerve to pee in a rest area, adrenaline running like an engine inside me, my keys threaded through my fingers in case anyone tried anything.

(beat)

(thinking aloud) I didn't do anything to earn it -- his anger. I didn't do anything.
```

---

## IC-2302: Painting Fires

- Title: Painting Fires
- Author (byline): Cole Sutterland
- Work: Fast Horse Plays – Round 1
- Publisher: Fast Horse Drama
- Publication date as stated: Sept 2011
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1754
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cole Sutterland
Book: Fast Horse Plays – Round 1
ISBN: 978-0615603681
Publisher: Fast Horse Drama
Date (Month/Year): Sept 2011
```

### Introduction (context only: never use it for content warnings)

```text
It’s a beautiful Saturday afternoon and our speaker has set up her art booth at a local craft fair. Her paintings are beautiful and reflect all aspects of her life.

It’s been said that art reflects life . . . but what happens when the line between reality and fantasy becomes blurred? For most of us, daydreaming is a virtual world where we can rehearse the future, explore fearful scenarios or imagine new adventures without risk. For others, however, the draw of an alternative reality is an escape from a devastating reality – a coping mechanism that permits them to continue . . . Painting Fires by Cole Sutterland.
```

### Performance text (classify this)

```text
The speaker is at a craft fair with the paintings she has completed. Allow time for her to listen to customers before she responds to them. She gets lost in her own thoughts and voices them aloud as customers move away.

(to a customer) . . . . That is so nice of you. I get a little funny about my work, I guess, and, I don't know, flustered or something. Have you been a couple of blocks down the sidewalk? There's some amazing, really amazing painters here. No, I, mean. That's very sweet of you, but these are just pictures of my life. If I haven't seen it, I can't paint it. I remember hearing that old saying about "write what you know," and I'm a terrible writer, so I guess I just "paint what I know." There isn't anything very special about it.

(to audience) This is, um, where my son and I go to find our Christmas tree every year. Sort of single mom, have to know how to use a saw. I never did a very good job, and I would always tell my son, "I guess that's what dads are for," and he would laugh. He always names the trees and then holds a little service to honor their passing when New Year's comes. I can't remember the tree's name that year. Or what my son got me. . . he always asks for the funniest things, though. Kids, you know. A book of maps. A new collar for his puppy. A tape recorder.

What kid asks for a tape recorder for Christmas? We don't have much, so . . . (to a customer) No, no, it's not sunset, there's just a bit of smoke or something on the horizon. Fire season. Oh, thank you so much. It's just a painting of our house. Blue and white. Small. Simple. But very happy. Like our lives, I guess you would say.

I'm so sorry. It's not for sale. No, I, I just can't. That's very generous of you, but it isn't finished yet. I'm sorry. That's of my son and his dog, Buddy. Big mutt. (to audience) My son was walking home from school one day and just like in the movies, Buddy followed him home. And he stayed. Right by Buddy's side. He does look sad there, I guess. He should be happy, warm by the fireplace, with his master. I guess, well, you see, we had been living with someone, we aren't, now, but we were then, and he didn't like Buddy barking. It annoyed him, he said. I stood my ground, though. And Buddy stayed. He stayed . . . forever. My son's father died when he was a baby and it was just the two of us for years.

And we were very happy. I sang to my son every night before he went to sleep. His favorite was the one about the . . the . . . picnic . . . do you know that one? But then, when I met John, I thought that . . . I'm sorry, I'm rambling, I know, I just, I'm trying to explain about the painting of the house.

I met John and, at first, he did all of the right things. Flowers for me. Little league games with my son. And then, well, I guess sometimes things change so slowly that you don't even realize it until it's too late. And then you get stuck, I guess. Yeah, it's a forest fire. Nature's version of a do-over. The fire splits open the cones and they say that the trees grow back stronger and taller. But it takes a long time. So, I got stuck. John would come home from work and his nights were spent in front of the TV. He brought a permanent winter with him and we didn't really speak much anymore. It was like my son became an imposition, like a gnat that one might bat away out of annoyance. Angry words. Cold stares. I love my son very much. We didn't spend much time at home anymore. I brought that winter into our home and I let him stay. I'm sorry, I'm boring you, babbling on like this.

(to a customer) . . . I love that one too. Yeah, it's my son after the spelling bee. (to audience) We spent hours in the evenings, just the two of us, on long drives practicing for it. I've never seen a ten-year-old so dedicated to something. I couldn't believe it. Words that felt like they were thirty letters long and he would just go over and over them. He only missed one word, right at the end. I was so excited. I was holding my breath. I was just so proud of him though. I . . . I'm sorry, I don't remember the word exactly. It was . . . I don't even really remember what it meant, that word.

Oh, I would love for you to meet him too. That would be wonderful. No, I don't think he'll be able to come down tonight. I've been waiting, but. . . He's with Buddy, somewhere. No, no. I don't think I'm a very good mother at all. Oh. I don't know if I can finish the picture of the house tonight. I'm so sorry. I. . . well. I can't finish it because I still don't know how that story ends.

I guess, I didn't want us to be stuck anymore, you see. I was only going to be gone for just a little while. Just a bit. And, I . . . left my son and Buddy, they were watching TV in the living room and John, he was asleep on the couch, just like he always was. And I kissed my son on the top of his head and told him I'd be right back. Just right back. So, a little while later, my son, he calls me and he tells me that Buddy had started barking at John and well, John had told my son to "go upstairs right now and take the damn dog with you. And close your windows." And so, I told my son that it was okay, that everything was finally going to be okay and that he and Buddy just needed to wait upstairs and I would be home soon. And I just needed him to have everything ready. And he said, "I love you, Mom. I will." And then, you see, there was a line at the place and then, my credit card wouldn't work and it took longer than it should have, much longer. And by the time I got back and I turned up our street, you see, I couldn't even get close to our house, there were so many cars and . . .

I parked, and I ran, and I could see. I wanted to close my eyes and just pretend it away. But I could see. Just as I see it now. Fire is everywhere now. Great tongues of red and awful orange fingers. Like the fire was hungry, consuming our little blue and white house, turning it black, eating it. This was our summer. And I tried. I tried to walk in, because if I could just get in there, be there with him, hold him. I fought them so hard. But they wouldn't let me in. And so I screamed my son's name until all I could hear was the roaring.

Do you understand now? It needs red and orange to be finished. I can't finish it that way. They found my son upstairs, in the corner of his bedroom. He was holding Buddy.

The windows in his room were already too hot to touch. But Buddy was there, with my boy. Buddy stayed with him, with my little boy. After John sent them upstairs he, um, he lit a cigarette and then, he, he just fell asleep. And John, he walked out the front door and he took that cold winter with him. While my boy was upstairs. . . So I paint him and I keep him with me that way. All that we had and all that we'll never have. If I paint his high school graduation, then there he is, cap and gown, and I'm in the bleachers, cheering. I paint him on his wedding day. He looks so handsome. I . . . I just needed another thirty minutes and then we were going to go away. Sometimes I wonder if we did and this is just another place that I don't really understand. An in-between place.

I, I don't even know what I'm saying anymore. (to a customer) I'm sorry that painting isn't for sale, but thank you for all your kind words. (to audience) Maybe my son will stop by later. Maybe he'll bring Buddy. I wait, you see. I wait, and I wait and I wait. I'll wait forever until I get to see him again. But, for now, I keep a little piece of him with me until I get to see him again, you know? Until he shows up . . . After it happened, that thing I was talking about, I got to go and pick a few things up. Just a few. And, um, there was that tape recorder. The one I gave him for Christmas. And um, he'd recorded himself, and I listen to it now, anytime we're apart for a little while. I listen to it all the time, actually.

Hi Mom, it's me, your little monster. I thought it would be kind of cool to keep a record of stuff on here and maybe give it to you when I go away to college or something. So, today I wanted to say thank you for letting me keep Buddy. He says thanks for his neat blue collar. I know John hates him, but he’s good to have around.

John was better today. I know you feel bad, Mom, but it’s not that bad. But if we ever do want to go away, we can plan out places we could go with the maps.

You're better than a Mom and a Dad put together. Seriously. We’d be fine, I’d protect you.

And that word I missed – it’s palliate – it means, “to make a mistake better.” I can spell it now.

And I know you said you wouldn’t be able to sing to me anymore when I leave him, but that’s not true. I’ll call you and you can – you can sing, *“If you go out in the words today, you’re sure of a big surprise. For every bear that ever there was will gather there for certain, because today’s the day the teddy bears have their picnic.”

Anyway, I love you Mom. Don’t worry so much about me.
```

---

## IC-2303: Paper Things

- Title: Paper Things
- Author (byline): Jennifer Richard Jacobson
- Work: Not specified
- Publisher: Candlewick Press
- Publication date as stated: Feb 2015
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: KEISHA, LINNIE, ARI, MS. FINCH, GAGE
- Teaser before the introduction: Yes
- Spoken words (computed): 1544
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jennifer Richard Jacobson
ISBN: 978-0763663230
Publisher: Candlewick Press
Date (Month/Year): Feb 2015
Cutting compliments of
Heather Whitney, Norfolk Public Schools, NE
*With minor adjustments by the 4N6 Fanatics staff to
ensure correlation with the original text.
```

### Introduction (context only: never use it for content warnings)

```text
Family is important, but at what price? Before Ari’s mother died, she made Ari promise to stick with her older brother, Gage. So when Gage decides he can no longer live with their bossy guardian, Janna, Ari leaves with him. There’s just one problem - they have nowhere to go. Couch-surfing between friends’ apartments and homeless shelters, Ari struggles to stay strong for her brother and keep up with schoolwork in order to be accepted into the prestigious Carter Middle School. Through this heart-wrenching struggle of homelessness, view one child’s experience in the novel “Paper Things” by Jennifer Richard Jacobson.
```

### Performance text (classify this)

```text
(Pg 105-106) Ever since I can remember, I’ve had this theory that when each person is born, he or she is given an imaginary sack with the same number of happy moments, horrible-news moments, and please-let-me-die-now embarrassments. So, while some people may have a bunch of bad moments all in a row, in the end, we’ll all be even. [My friend] Sasha tells me that’s a ridiculous way of thinking. “Think of people who are starving, or who live in countries where there is war. They suffer more.” But I like to think that even those people might get to experience the same number of joys in their lives as everyone else. And on the flip side, people whose lives seem perfect might also be suffering in ways we don’t see.

But maybe [she’s] right. Maybe that is a ridiculous way of thinking. Yet sometimes, when it feels like all my troubles are piling up - Mama getting sick and dying, Janna and Gage fighting all the time, maybe missing out on the chance to go to Carter - it helps to think that there are only so many bad times in my sack. That sooner or later the good things will have to take over.

KEISHA: (Pg 127) “Is Ari using some new product in her hair? Or is that… grease?”

LINNIE: (Pg 128-129) “She smells, too.” Is she joking? I put my head down just a little lower, trying to smell my pits. She’s not joking, I stink. How could I help it? The bus stop was practically a whole mile away from where [Gage and I] slept last night. I was running as fast as I could, but my shoe has started to flap where the stitching is coming out, and it falls off easily. (Pg 6-7) I look over at Sasha’s desk - something I do about fifty times a day - but she’s not in her seat. My best friend is down on Walnut Street, acting as one of the safety patrol leaders. It’s one of the fifth-grade leadership roles. You have to demonstrate leadership to get into Carter Middle School.

Two months of school to go and I still haven’t been chosen to do any of the leadership jobs. Not safety patrol, not tutoring, not shelving books in the media center. And I have to get into Carter. Have to. Only problem is, it’s a school for the starry gifted, and I seem to have lost all my shine. [Why does Carter matter so much to me anyway?] (Pg 86-87) Mama wanted me to attend Carter. It had been one of [her] dying wishes. Everyone in my family went to Carter - Mama, Dad, Gage, even Janna. ******* (Pg 24) “What do you need for homework?” Gage asks when he picks me up at Head Start (Pg 163) I volunteer there in the afternoons.

ARI: (Pg 24) Library; I need to research a famous American. (Pg 9) My social studies grade is the pits. I did lousy on both quizzes and I haven’t been able to finish the outline of my biography. (Pg 27) [When we get there], Gage marches directly to the Maine Times to read the want ads, like he does every time we come. He doesn’t have a regular job but goes wherever someone needs him. Lobstermen are always glad to see him on fish market days. Tomorrow he’ll probably be the dishwasher at the nursing home (Pg 28) I hope Gage finds a full-time job soon. What he didn’t realize when we left Janna’s is that landlords won’t rent to you if you don’t have a regular paycheck, no matter how much you’ve saved for the first and last month’s rent. (Pg 77-78) Who is hiring? Jiffy Lube, but Gage says they want someone with experience. It’s not that Gage doesn’t want to work - he works harder than anyone. And he really, really wants to get a job so we can get an apartment. It’s just that he hates it when he asks and people tell him no. (Pg 252-253) I pull out my application to Carter. There they are again - those spaces on the application that demand an address. I suppose I could write in Brigg’s address, [Gage’s friend from school], but that might get him in trouble. I could put Chloe’s address, [Gage’s girlfriend], but what if Gage and Chloe break up? I could write in Janna’s address, but the last thing I want is my acceptance or rejection letter being sent to Janna’s place. We need an apartment! We need to figure this out! ****** (Pg 262-263) The line outside the soup kitchen isn’t long [tonight]. I’m standing behind Gage, waiting to enter the basement of the stone church and thinking about the first question on the Carter Middle School application: How would other people describe you? I try to think of one-word answers that people I know might give: Persistent. Hardworking. Disappointing. Sneaky. (Pg 265) And that’s when I see Keisha [from my class], standing at the back of the room, volunteering, ladling soup to the masses. Volunteering at the soup kitchen o n the exact night Gage and I decide to come by.

ARI: (to Gage) I’m not hungry - I don’t feel good – I’ll wait outside. (Pg 268-269) The last thing I need is for word to get out that I eat at the soup kitchen. People would start asking questions, or start gossiping about me being dirty, smelly, and someone who eats with the homeless. ***** (Pg 285) “We’re not homeless,” I [tell myself], but what does it mean to be homeless?

I think of the people that I pass on the streets, the ones who are huddled against buildings or standing on curbs, asking for money, sometimes talking to themselves. They’re homeless. I think of the girls at the Lighthouse who talk about which shelters had the nicest beds. They’re homeless, too. Homeless people are people who don’t have homes. . . Like us, I realize. *****

MS. FINCH: (Pg 295-297) (waking Ari in class an speaking softly) Ari, would you mind staying for a few minutes at the end of class? When it’s just me and Ms. Finch, she walks over to her desk and retrieves a paper bag from the bottom drawer.

MS. FINCH: “You see, I bought my niece a new pair of shoes, but they didn’t fit her. If you like them and they fit, you’re welcome to have them.”

(Ari holds them in both hands, her mouth hanging open) My fingers barely work as I pull off my old shoes, and I wonder if everyone has noticed how ratty they are. Maybe this is an act of charity, but I decide I don’t care why Ms. Finch is giving them to me. I’m just grateful that she is. And suddenly I’m crying. ****** (Pg 301) Stay together always. That’s what Mama said. That was the promise! But I think that both Gage and I know deep down that it’s not the promise that’s making us hold on to each other so tightly. It’s the fear of letting go. (Pg 307-308) Before I really even know what I’m doing, I pick up the phone and dial Janna’s number. Gage will be mad . . . and hut. But I’ve made up my mind. I’m going home. When [she] picks me up and I grab my backpack, she says, “Is that all you need?” I nod but think no. No, I need so much more than what is in my backpack. I need a homemade dinner, a warm shower, shampoo that smells like strawberries, a cozy bed. I need a place to keep my things, a place to do homework. I need a routine, a regular bedtime. I need rules, all 465 of them! [Later, Gage comes to Janna’s to check on me.]

ARI: (Pg 314) I need you to know something. (takes a deep breath) I didn’t call Janna because I didn’t want to be with you anymore. I loved being with you. But here at Janna’s . . . here I get to be a kid. Just a kid.

GAGE: (Pg 245) It’s not your fault. It’s mine. I’m the one who lied to Janna and said we had an apartment. I’m the one who dragged you all over the city, carrying all your belongings in your backpack. I’m the one who can’t give you more than Cheerios for breakfast and lunch. ****** (Pg 344) That night, I work on the application for Carter Middle School. Fortunately the blanks for address and name of guardian are now easy to fill in. For one of the questions, I write about my experience working with the kids at Head Start. I stare at the last question, the one that basically asks you to describe what sets you apart from your peers, what makes you special - what makes you Carter material.

(Ari takes a deep breath and begins writing) (Pg 336) I know what it’s like to be an outsider, to feel like you don’t belong. For six weeks, my brother and I were homeless. We slept on couches and at the shelter and even in a car. We did the best we could. I was too embarrassed to tell anyone what was going on. I didn’t want to be different. ***** (Pg 367-368) Everyone said that we would get our letters from Carter on Saturday. So imagine my surprise when I get home on Friday and there is the letter on the counter.

(Ari opens the letter and reads): “Dear Ms. Hazard, It is with great pleasure that we offer you a place at Carter Middle School for the next three years…” I got into Carter. Despite the dip in my grades. Despite telling the application people about being homeless. Despite it all - or maybe, really, because of it all - I’ve been accepted.
```

---

## IC-2304: Pastels and Crayons

- Title: Pastels and Crayons
- Author (byline): Aleeza Kazmi
- Work: The Moth Presents Occasional Magic (Pgs 240-246)
- Publisher: Crown
- Publication date as stated: March 2019
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ALEEZA, MISS PENNINGTON, MOM, BOY
- Teaser before the introduction: No
- Spoken words (computed): 1471
- Already set (do not supply): none

### Source block (context only)

```text
Author: Aleeza Kazmi
Book: The Moth Presents Occasional Magic
(Pgs 240-246)
ISBN: 978-1101904428
Publisher: Crown
Date (Month/Year): March 2019
```

### Introduction (context only: never use it for content warnings)

```text
Bins filled with colored pencils and crayons are placed in the center of tiny tables. It’s the prelude to one of the first art projects of any elementary school career – the self-portrait. The kids are to select the colors of their choice to create the best reflection of themselves . . . An odd exercise for children of color. You see, the world is filled with images where beauty is communicated as a mostly white ideal. The conflict for children of color: Draw yourself with ethnic features and admit belonging to a group of “others,” or with Caucasian features to align with the white image of beauty. How do you present yourself to the world; and conversely, how does your world see you?

Pastels and Crayons by Aleeza Kazmi
```

### Performance text (classify this)

```text
ALEEZA: (Pg 240-246) I was six years old in the first grade, and I was sitting at a table with my three best friends. We were all really similar. All of our moms bought us clothes from the Children’s Place, we all liked to play house during recess, and all our names started with the letter A. It was Ashaya, Alicia, and Aleeza.

We were working on a first-grade icebreaker project, which our teacher, Miss Pennington, had assigned to us. It was gonna be self-portraits that we could hang up on the wall and get to know each other’s faces and names. I was really excited for this project. I knew it was really special because there were three drafts. And we were working on the final draft, which was going to be colored in.

I was super stoked for this. Over the summer my mom had bought me this coloring book that taught me all these great techniques for how to draw properly, and I finally mastered coloring inside the lines. I was so excited to show my friends my new skills. I was basically young Picasso.

I also knew this was a special project because we were using oil pastels. I loved oil pastels —they’re really soft, so I would pinch off a little bit and melt it between my fingers. They were expensive for my public school in New York City, and so each table got one box. And each box had one of each color, so you had to be patient and wait for your color.

At this point I had colored in my shirt blue and the background green, and there was a little tree. I had drawn in all the features of my face, which the book had taught me to do first. I had drawn in my lips and my nose, and I was ready to color in my face.

All my friends had used the peach oil pastel to color in their faces, and since we were basically all the same girl, I would use peach, too. So finally, when it was available, I picked it up, and I started drawing so slowly, going around my lips and my eyes and coloring in all one direction. I was watching as the oil pastel melted into the paper and my face came alive, and I colored inside the lines.

When I looked down, it was like I was looking into a mirror. This girl I had just drawn was exactly how I saw myself. I felt my teacher, Miss Pennington, over my shoulder.

Miss Pennington loved it when people drew well, and so I was getting ready for her to praise me, to say, Aleeza, that is the most beautiful self-portrait I have ever seen.

I’m gonna hang it above my desk so everyone who comes in can see it. Instead, Miss Pennington says

MISS PENNINGTON: Aleeza, that’s not your color.

ALEEZA: I’m confused by this, because I don’t understand how colors can belong to people. But before I can find a way to ask her, she’s gone to the oil-pastel box and started looking for it. She doesn’t find the color that she’s looking for, and so she goes to the crayon bin.

Now, every school had this infamous crayon bin that had bits and pieces of gross crayons that had been rolling around in that bin forever, and I never went to the crayon bin. Nonetheless, Miss Pennington is rummaging through it, and she reaches in, and she pulls out this little nub of a brown crayon that’s unwrapped and gross.

And she hands it to me.

I’m still really confused by all this, but I notice my friends are staring at me, and my heart is beating really fast, and I want this to be over. So I just grab the crayon, and I start coloring in my face, and I’m going in all different directions. But wax crayon and oil pastel don’t mix together. They don’t belong on the same paper. So it doesn’t matter how hard I’m pushing, because I can’t get the crayon to stick, and I’m coloring outside the lines.

When I look down at the paper, I am this grotesque monster that can’t decide if she wants to be peach or brown.

And I want to beg Miss Pennington, please don’t hang this up. I’ll do it all over again. I’ll use the colors that you want me to.

But before I can find the right words, she’s taken my self-portrait and put it into a pile with all my even-toned peach friends, and it gets hung up.

That night I go home and I ask my mom why I wasn’t allowed to use peach. And she explained it as best you can to a six-year-old who’s just gone through an identity crisis.

MOM: You know, I’m not peach, and your dad isn’t peach. And since you’re our daughter, you’re not peach either.

ALEEZA: But this confused me even more, because my parents are just like my peach friends’ parents. They sound the same. They make the same small talk at school pickup. But they’re apparently not the same. And everyone seems to understand this concept of color. I’m not getting it, and I don’t want my mom to think that I’m stupid. So I don’t ask her anything further, and I try to not think about it.

But it wasn’t that easy. A couple months later, we had a day called International Day. We had it once a year at my elementary school, where everyone would dress up in the traditional clothing of the country that they’re from or that their parents are from and then march around the school. It was meant to celebrate diversity and heritage.

I hated International Day.

First off, my mom is from Afghanistan and my dad is from Pakistan, so each year I’d have to alternate who I marched with.

But no matter who I was marching with, they always seemed to understand the traditions better than I did, or they spoke Urdu or Farsi, which I did not. And so even though we were the same color, I didn’t belong with them completely, just like I apparently didn’t belong with my peach friends.

I didn’t know where I fit, and I was stuck in this color limbo.

But I finally graduated elementary school and moved on to sixth grade and thought I had left this whole concept of colors behind me. So, on the first day of sixth grade, I was really excited. It was a brand-new start, and we were all trying to get to know each other by asking questions, like “Where’d you go to elementary school?” and “What’s your favorite book?”

And this one kid comes up to me and says,

BOY: What race are you?

ALEEZA: I had never been blatantly asked this question before, and so I didn’t have a prepared answer. I thought back to Miss Pennington and that brown crayon, and I told him, “I’m brown.” He gets this confused look on his face, and he says,

BOY: What do you mean you’re brown? Brown isn’t a race.

ALEEZA: And I couldn’t believe it. I couldn’t believe that I had finally said “I’m brown” and it still wasn’t enough. And then this little six-year- old girl deep inside of me gets angry. And then I get really angry. And then I’m screaming at him. (to boy) You know what? If I say I’m brown, then that’s it! I’m BROWN!

And he never spoke to me again.

Which was fine, because I had finally found the words to stand up for myself, and I had finally come to terms with who I was.

I want to say that was the end of it, that because I was, you know, okay with who I was, that I never had to stand up for myself or defend my race again. But that just wasn’t true. I was growing up in post- 9/11 New York City, where being brown put me in this category of “other,” and I have been questioned about who I was many times after that.

I had to reaffirm over and over that “I’m brown, I’m brown, I’m brown,” because nothing anyone says to me will ever make me question that again. I’ve worked so hard to love the skin I’m in, and nothing anyone says can take that away from me.

Today if you ask me to draw a self-portrait, I’d draw a confident young woman who’s proud of her Afghan and Pakistani heritage, who is a proud American. And I would find the most beautiful, soft brown oil pastel to color in my face. No one would have to tell me to pick it up. It would be my first choice.
```

---

## IC-2305: Perfect Circle

- Title: Perfect Circle
- Author (byline): Carly Johnstone
- Work: The Moth, Pg 220-228
- Publisher: Hyperion
- Publication date as stated: September 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1735
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carly Johnstone
Book: The Moth, Pg 220-228
ISBN: 978-1401311117
Publisher: Hyperion
Date (Month/Year): September 2013
```

### Introduction (context only: never use it for content warnings)

```text
Carly Johnstone was a survivor – a strong young woman who proves the quote from Mary Anne Radmacher: “Courage doesn’t always roar. Sometimes courage is the little voice at the end of the day that says I’ll try again tomorrow.” This is her story -- A story of a family bound together, not by blood, but by choice.

Perfect Circle by Carly Johnstone
```

### Performance text (classify this)

```text
(Pg 220-228) I was sixteen [and] my life had been a lesson in negatives. I had been a lesson in what not to do. My mantra had been “How not to be my mother.” My mother was a prostitute, and I had grown up with her, and many other prostitutes, and the men that handled them. When she died in the 1980s, like so many from AIDS, I went into foster care. [It was] a year and a half before my mother’s parents, my grandparents, took me in under duress . . . people who don’t want children probably shouldn’t have them. They lasted about five years with me before they threw in the towel, retired to Florida, and put me in a Southern Baptist children's home.

[After] about a year and a half there I thought, I could do better than this. I could raise myself. I mean, the bar was pretty low. I studied a lot, took a lot of tests, and graduated high school two and a half years early. I got on a Greyhound and went back to New Jersey, because that's where I grew up and that's where I felt safe. I started college at a local com-munity college. I got my first full-time job with full health benefits, and I got my first place. And by the end of my sixteenth year, a wrench was thrown in the works. I was pregnant.

I knew a few things right off the bat: I wasn't going to abort. It wasn't because of some misbegotten belief in God or because I'm pro-life, because I'm not. I desperately wanted this baby; I always wanted a family -- something that was mine and pure and good and whole.

I wanted it, but I couldn't keep the promises I had made to myself about having a family. That whole mantra about not being my mom; I couldn't give this kid a home. I couldn't give a life without fear or want. And so I had to find another solution. I looked at traditional adoption, but I couldn't have a kid grow up the way I did, with so many questions about who I was and where I came from. And I looked at fostering, but again, you know, I had traveled that road. It hadn't really gone so well.

Finally, someone explained open adoption. It means that the adoptive parents want an ongoing relationship with the mother; and the mother -- she gets to choose the parents. And I thought, I can do this. I can do this.

So, I attacked this like I attack everything else in my life, like a research paper. I made a lot of calls and took a lot of notes, and I finally found an agency that could meet my criteria.

I had three. My first was that it had to be a same-sex couple, because, at this time, it was a little harder for them to adopt. Additionally, I realized that if I ever found anyone to settle down with, it would be another woman. I never wanted that to be an issue.

Number two: they had to not have any extreme religious affiliation. I had had religion shoved down my throat, and I thought faith should be a choice.

Number three: they had to want an interracial child as their first choice. The father of this baby was black, and I was half very white and half something very brown. I didn't want it to be something they settled upon because they couldn't find a perfect blond-haired, blue-eyed baby, or because they were trying to better their karma.

Even with those narrow parameters, I had over two hundred couples that were viable choices, and each of them had a brochure. Each brochure was full of pictures of their family and friends and their homes, and information about how well educated they were, how much support they had, and how financially stable they were.

Eventually I found a couple that I really liked. Their names were Gwen and Gretchen. They lived in Portland, Maine, which was far enough for me. I didn't want them to be too close, because I knew I might be a stalker mom, and I didn't want to find myself on a playground. So they were close enough that I could get there if I needed to, but also far enough away that I couldn't run there in ten minutes.

They came down from Maine to meet me. Gretchen is tall and strong and unflappable, and Gweny is tiny and sweet and nurturing. And I liked them, and they liked me, which was really important because they had to deal with me for a really long time, and a lot of people had not really hung in there.

I knew they were the right ones.. And we waited the wait of expectant parents. Eventually we found ourselves in this delivery room, and after twenty-three hours of labor, I gave birth to an eight-pound, six-ounce baby boy. And he was perfect. And he was whole. And he was so beautiful.

I had forty-eight hours with him, and I sang him every song I knew. (insert brief song here) I tried to say hello to him, and I tried to say good-bye. And at the end of that forty-eight hours, I brought him downstairs, and helped them strap him into a car seat, and I watched these strangers drive away with my baby.

I hoped I had made the right choice. I hoped they were the right people. I hoped he would forgive me.

Up until this point I had never cried, but when I went home, I finally did. I shattered. I broke into a million pieces. I looked at my body, this seventeen-year-old body that should be healthy and strong and young, and it was broken too. I had stretch marks that looked like purple claws. My stomach that had so recently been filled with life was flaccid and dead. My breasts were heavy, hard, swollen and leaking, trying to feed a child that wasn't there, a baby that was gone.

And I didn't know what to do. I had had such a good start, but I stopped living the mantra of how not to be my mother. I did my best to prove I was just as bad as her. I was someone that could give away a baby. I was the person that could throw away a child. And after never drinking and never smoking and never doing anything bad, that's all I did for the next three or four years. I tried to destroy myself as quickly as possible.

After four years, I made my way to Maine. I finally got up the courage to visit this family that had my child. I went to their home, and it was beautiful., The kitchen was the kind of place where everyone goes to tell their story and friends meet. And all I saw was everything I wasn't; all I saw was a bar I would never meet. And I watched these people raise a child that I was incapable of holding or touching or saying "I love you" to, because I didn't know how to do that. I didn't know how to do it for myself; I didn't know how to do it for him. I just hadn't been given those tools in my life.

I did realize on that trip that I had to be someone who -- when this kid was old enough to ask questions -- was worthy of being asked.

I went home, and I stopped doing all of those horrible things to myself. I made better friends and started building my own family of supporters. Eventually I got better, and every year in August I would visit them, and every year it was a little easier to talk, and it was a little easier to share, and it wasn't so terrible when people stared at me and said, "You look just like him."

When he was turning nine, I was invited to a seminar about an hour north of Portland. We were asked to bring something we needed to get rid of, and I had a lot. But the one thing that I had to really get rid of was this idea that I was Henry's mother (that's his name, Henry), because I wasn't.

There's a big difference between the person that gives birth to you and the people that raise you. I knew that from my own life; it just took me a long time to learn that lesson for myself.

After [the seminar I] went to Portland. This [seminar] hadn't changed me as a human being, it had just changed my perception. I realized these people -- these wonderful people who did such an amazing job raising this brilliant kid -- had given me the only blueprint I had. They had given me the foundation for what a family should be, what love was and loyalty, and what a mother could be. What two moms could be. I left there, and it was the first time I did not cry all the way to Boston and scream until New Jersey.

The year he was turning ten, I found I was pregnant again, but this time it was different because I had spent years trying to build a real family. The people in my life were so excited because this baby was the first in our family of friends. I was still poor, and I hadn't completed my education, but I wasn't alone. I had wonderful friends; and they called, and they wrote, and they filled a storage space with baby things.

When my daughter was born, everything was so different.

Henry carries a picture of Asha in his wallet. (I named her Asha; it means "hope".) My son will be fourteen this year, and in April, when Asha turned four, he came with his mother, Gretchen, to our house and shared our home and stayed with our family and all the people that chose to be there, and I watched him hold her and play with her. I saw them as part of my family for the first time, really understanding that they were part of me too. I watched this beautiful, brilliant, strong boy carry his beautiful, brilliant little sister and realized that he had become a part of the net that would hold her up.
```

---

## IC-2306: Personally

- Title: Personally
- Author (byline): Janet O’Neill
- Work: Turning Points: 30 Pieces for Oral Interpretation (Pg 71-73)
- Publisher: Tichenor Publishing
- Publication date as stated: Jan 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: GRANDMA
- Teaser before the introduction: No
- Spoken words (computed): 982
- Already set (do not supply): none

### Source block (context only)

```text
Author: Janet O’Neill
Book: Turning Points: 30 Pieces for Oral Interpretation
(Pg 71-73)
ISBN: 978-0742117013
Publisher: Tichenor Publishing
Date (Month/Year): Jan 2001
```

### Introduction (context only: never use it for content warnings)

```text
Once upon a time . . . in an archaic era before social media and the internet, one way to meet people was to post a personal ad in *gasp* the newspaper!

For those who have never seen a personal ad, they were like your Match.com bio. You said a few words about yourself and let the world know what or who you were looking for.

My grandmother was telling me all about it the other day. She did it lots of times. She says she did it for the thrill. And back then she was ashamed she had to resort to such tactics just to meet someone. She explained:

GRANDMA: When you post in a newspaper, you only

have 80 characters. If what you say is not really you, if

it's shallow, that's OK -- blame the medium. The

newspaper personal ad is a dare, it's a risk. A

baseball card says more about someone's life than this

feeble ad. But that's the way it's gotta be.

This is the story my grandmother told me . . . Personally by Janet O’Neill
```

### Performance text (classify this)

```text
GRANDMA: (Pg 71-73) My biggest problem had been deciding what to put in the ad. How do you describe yourself in three lines or less? I was determined not to use the same stale lines like, "I like to have fun." Tell me, who doesn't like to have fun? If someone were to say that they didn't like to have fun, that would tell me something. It would tell me to stay away. I settled on a conservative ad:

"33-year-old who likes romance novels, gardening, and charity work seeks a man of similar age and similar interests. Interested in friendship first. We'll see if anything develops."

So I went home and waited for something to develop.

My ad ran in the newspaper for the next five days. What had started as an empowering experience had quickly become one of the most humbling experiences of my life. I got two responses. A newspaper with a circulation of over two million, and I got two responses. The first was a 36- year-old man who was looking for some "love and affection" while his wife was out of town, and the second thought Patrick Buchanan was the way of the future. That was it. I tried to laugh it off. Sara took me out for Haagen-Daaz and I kept my chin up. The ad ran for another week.

The next day I got a response. A 31-year-old schoolteacher who loved to travel, read mystery novels, and watch Woody Allen movies. We went out for a drink, which quickly evolved into dinner. . . and a movie. . . and a carriage ride. OK - so it was 20 degrees out and the carriage ride made my legs numb, but his heart was in the right place. He dropped me off, gave me a warm kiss, and said, "I love you." I love you? He's known me for five hours and already he loves me? I've been in love once in my whole life. The next day he called to see if I wanted to go dancing. I said I can't. He asked why. I said, "Because you love me."

I went out with this guy, Jason, the other day. Said he had an important job with a large cooperation. This was kind of true. It seems the company that makes Cool-Whip has an 800 number which you can call and ask questions. He was the man who answered the phone. That's right - I'm on a date with the Cool-Whip man! What kind of questions do you think he gets asked all day? "OK, we've got the pie and the Cool- Whip. . . now what do I do?"

The next guy seemed awfully young. He claimed to be 28. He looked younger than some of my friend's children. He picked me up and we went to dinner. At McDonald's. Just me, him, and the Hamburglar. He says he likes to do this because it takes the pressure off the first date. Guess it's hard to feel nervous when you're eating a McRib sandwich. We went to his place, I said, "Hi!" to his mother, and he left to take a phone call. His wallet was just sitting there -- I had to look! I saw his license: 19. Now what do I do? I gave him a peck on the cheek, and politely said, "This isn't going to work. You're just too mature for me." He smiled and said, "That's ok. You aren't the first chick to say that." He called me a chick - it was definitely time to go.

Cool-Whip man called me yesterday. Said he's been thinking a lot about me. I've got him whipped. Get it? Whipped.

His name was Jimmy. He didn't give a last name. He said second names were for second dates. He took me out for drinks and then we end up at his place. He's crawling on top of me, making me feel like a piece of meat. I say stop. Please stop. He does not force himself on me. Instead, he slaps me. Hard. Then he makes a fist and hits me harder and harder and harder and then he stops and says, "Thanks for the drinks. Here's some cab fare."

The entire concept of the personals baffles me. We ask to be judged by our suitors in three lines or less. We pay to do it. All because the thought of ending up alone is too scary to comprehend. I decided that maybe my ad wasn't good enough, so I jazzed it up a little. Maybe I was attracting the wrong people. No one. So I changed it again. No one. And again. No one. I changed my age, my religion, my hair color. No one.

And the more that I degraded myself by going out with these losers, the more desperate I got. I laughed at jokes that weren't funny. I went to bars that made my skin crawl. I slept with men who left in the middle of the night and referred to me as a "good piece of a**." I cried.

Now I find myself at my friend Sarah's dinner party. I'm sitting with eight other people: four couples and me. I then realize that it may always be this way: an odd number of people, X number of couples plus me. I find that because of this, I often sit at the head of the table since I don't have someone to sit next to. I guess that could make me feel important, but I know that I'm in the spotlight for the wrong reason.

Just once, I wish that I had someone to introduce to others. Just once I wish that I had someone to date, to love, to fight with, to go home to my parents with. Sure, I'd love for it to last forever, but I'd settle for just once.
```

---

## IC-2307: A Phone Call

- Title: A Phone Call
- Author (byline): Auburn Sandstrom
- Work: The Most Presents All These Wonders
- Publisher: Crown
- Publication date as stated: March 2017
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1406
- Already set (do not supply): none

### Source block (context only)

```text
Author: Auburn Sandstrom
Book: The Most Presents All These Wonders
ISBN: 978-1101904404
Publisher: Crown
Date (Month/Year): March 2017
```

### Introduction (context only: never use it for content warnings)

```text
During a personal crisis, it can be difficult to know what to do. Especially if you are alone – because many people have no support system they can turn to. But would you talk to a stranger? Would you cry out for help?

A Phone Call by Auburn Sandstrom tells the story of her own personal crisis and how and unknown voice in the dark brought her back from the brink.
```

### Performance text (classify this)

```text
NARRATOR: The year is 1992, Ann Arbor, Michigan. I’m curled up in a fetal position on a filthy carpet in a very cluttered apartment. I’m in horrible withdrawal from a drug that I’ve been addicted to for several years now.

In my hand I have a little piece of paper. It’s dilapidated because I’ve been folding it and unfolding it, to the point that it’s almost falling apart. But you can still make out the phone number on it.

I am in a state of bald terror. If you’ve ever had an anxiety attack, that’s what this felt like.

I’d been having a nonstop anxiety attack for the last five years. And I’d never been in a darker or more desperate place than I was that night. My husband was out running the streets, trying to get ahold of some of the stuff that we needed, but I knew if he succeeded, he was not going to share.

And if I could, I would jump out of my own skin and run screaming into the streets to get what I need. But right behind me, sleeping in the bedroom, is my baby boy.

Now, I wasn’t going to get a Mother of the Year award in 1992. In fact, at the age of twenty-nine, I was failing at a lot of things.

NARRATOR: I had started out fairly auspiciously. I was raised in comfort and privilege. I was that girl who had the opera lessons, spoke fluent French, and had her expensive undergraduate college paid for. I was that person who, when my checking account ran out, would say something to my parents and two hundred dollars would magically appear.

I know, when the revolution comes, kill me first, right?

So I had the year abroad. I had the master’s degree. I was, you know, pedigreed.

But in my twenties, I ended up in Ann Arbor, Michigan, and I started noticing things like poverty and racism and unconscionable injustice. And that people like me were mostly causing it. It was a huge revelation for me.

I came to the conclusion that the thing I needed to do with my privilege and all the comfort that I’d had all my life was to destroy it. Rip it in half. Spit on it. Set it on fire.

And you know, every time I’ve come to a major faulty conclusion in life, the man comes right after who will help me live it out. And this time was no different. He was beautiful—a radical, revolutionary, poet from Detroit.

I was twenty-four, he was forty, and I was smitten, in love. It was so exciting—who he was, how he talked, the way he looked at the world. And it was beautiful for a while, until he introduced me to one of his old activist friends, who introduced us to the drug I was now addicted to.

I had tried to change my affiliations and transform myself. I had wanted to shed my class. I would have shed my race if I could have.

But instead of transformation, you have me going ninety miles an hour down I-94 with my poet, in a car full of alcohol and illegal drugs. The baby’s in a car seat (it’s probably not a regulation car seat). He’s covered in candy and chocolate, because you have to keep the baby entertained while you’re taking care of your business, getting yourself some relief.

This particular night it was bad because, if we were to have been pulled over, we were both on parole. So we would’ve both been locked up, and our child would have been taken from us.

Underneath my withdrawal and terrible anxiety was a sure knowledge that I was leading the life that was going to lead to me to losing the most precious thing I’d ever had in my life, which was that baby boy.

I was so desperate at that moment, that I became willing to punch the numbers into the phone.

The phone number was something my mother had sent me. Now, mind you, I hadn’t been speaking to my parents or anybody else for three, four, five years.

But she’d managed to get this number to me by mail, and she said, “Look, this is a Christian counselor, and since you can’t talk to anybody else, maybe sometime you could call this person.”

Now, I think it goes without saying that I wasn’t hanging real tight with that sort of thing in those days. But I was so anxious and in such a desperate state. I was emaciated, covered in bruises.

I punched in the numbers. I heard the phone pick up. I heard a man say

MAN: Hello.

NARRATOR: Hi, I got this number from my mother. Uh, do you think you could maybe talk to me?

I heard him shuffling around in the bed, you know? You could tell he was pulling some sheets around himself and sitting up. I heard a little radio in the background, and he snapped it off, and he became very present.

MAN: Yes, yes, yes. What’s going on?

NARRATOR: I hadn’t told anybody, including myself, the truth, for a long, long time. And I told him I wasn’t feeling so good and that I was scared and that things had gotten pretty bad in my marriage.

Before long I started telling him other truths, like I might have a drug problem, and I really, really love my husband, and I wouldn’t want you to say anything bad about him, but he has hit me a few times. And there was a time when he pushed my child and me out into the cold and slammed the door behind us.

And then there was a time when we were going sixty miles an hour down the highway, and he tried to push us out of the moving vehicle.

I started telling those truths. And this man didn’t judge me. He just sat with me and was present and listened and had such a kindness and such a gentleness.

MAN: Tell me more. . . . Oh, that must hurt. . . . Oh.

NARRATOR: And do you know, I’d made that call at two in the morning. And he stayed up with me the whole night, just talking, just listening, just being there until the sun rose.

By then I was feeling calm. The raw panic had passed. I was feeling okay. I was feeling like, I can splash my face with water today, and I can probably do this day.

I wouldn’t have cared if the guy was like a Hare Krishna or a Buddhist—it didn’t matter to me what his faith was. I was very grateful to him, and so I said, “Hey, you know, I really appreciate you and what you’ve done for me tonight. Aren’t you supposed to be telling me to read some Bible verses or something? Because that’d be cool, I’ll do it, you know. It’s all right.”

MAN: (laughing) Well, I’m glad this was helpful to you.

NARRATOR: And we talked some more, and I brought it up again. I said, “No, really. You’re very, very good at this. I mean, you’ve seriously done a big thing for me. How long have you been a Christian counselor?” There’s a long pause. I hear him shifting.

MAN: Auburn, please don’t hang up. I’ve been trying not to bring this up. . . . I’m so afraid to tell you this. But the number you called . . . You got the wrong number.

NARRATOR: Well, I didn’t hang up on him, and we did talk a little longer. I never would get his name or call him back. But the next day I felt this kind of joy, like I was shining. I think I’ve heard them call it “the peace that passes understanding.” I had gotten to see that there was this completely random love in the universe. That it could be unconditional. And that some of it was for me.

And I can’t tell you that I got my life totally together that day. But it became possible to get some help and get the hell out. And it also became possible as a teetotaling, semi-sane, single parent to raise up that precious, chocolate-covered baby boy into a magnificent young scholar and athlete, who graduated from Princeton University in 2013 with honors.

This is what I know. In the deepest, blackest night of despair, if you can get just one pinhole of light . . . all of grace rushes in.
```

---

## IC-2308: Plain Girl Versus the Demon

- Title: Plain Girl Versus the Demon
- Author (byline): Amy Poehler
- Work: Yes, Please, Pg 15-28
- Publisher: Dey Street
- Publication date as stated: Oct 2014
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: AMY
- Teaser before the introduction: Yes
- Spoken words (computed): 1281
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amy Poehler
Book: Yes, Please, Pg 15-28
ISBN: 978-0062268341
Publisher: Dey Street
Date (Month/Year): Oct 2014
```

### Introduction (context only: never use it for content warnings)

```text
Recently, Glamour Magazine did a survey of approximately 300 women asking them to share their thoughts about their bodies. Surprisingly, or perhaps not, 97% of the women reported having at least one “I hate my body” moment.

Amy Poehler explores this mental state in Plain Girl Versus the Demon from her memoir Yes, Please.
```

### Performance text (classify this)

```text
AMY: (Pg 15-28) I hate how I look. That is the mantra we repeat over and over again. Sometimes we whisper it quietly and other times we shout it out loud in front of a mirror. I hate how I look. I hate how my face looks my body looks I am too fat or too skinny or too tall or too wide or my legs are too stupid and my face is too smiley or my teeth are dumb and my nose is serious and my stomach is being so lame. Then we think. “I am so ungrateful. I have arms and legs and I can walk and I have strong nail beds and I am alive and I am so selfish and I have to read Man’s Search for Meaning again and call my parents and volunteer more and reduce my carbon footprint and why am I [so] self-obsessed [and] ugly. No wonder I hate how I look! I hate how I am!”

AMY: That voice that talks badly to you is a demon voice. This very patient and determined demon shows up in your bedroom one day and refuses to leave. You are six or twelve or fifteen and you look in the mirror and you hear a voice so awful and mean that it takes your breath away. It tells you that you are fat and ugly and you don’t deserve love. And the scary part is the demon is your own voice. But it doesn’t sound like you. It sounds like a strangled and seductive version of you. Think Darth Vader or an angry Lauren Bacall. The good news is there are ways to make it stop talking. The bad news is it never goes away. If you are lucky, you can live a life where the demon is generally forgotten, relegated to a back shelf in a closet next to your old field hockey equipment. You may even have days or y ears when you think the demon is gone. But it is not. It is sitting very quietly, waiting for you.

[It] is patient. It says, “Take your time.” It says, “Go fall in love and exercise and surround yourself with people who make you feel beautiful.” It says, “Don’t worry, I’ll wait.”

And then one day, you go through a breakup or you can’t lose weight, or you look at your reflection in a soup spoon and that slimy bugger is back. It moves its sour mouth up to your ear and reminds you that you are fat and ugly and don’t deserve love

I had a lucky childhood. My demon didn’t live in my room. My demon just walked around my neighborhood. I grew up with a naturally pretty but very earthy mother who never told me to put on makeup or change my outfit. I didn’t have the king of mother who flirted with my friends or wore tight jeans.

In middle school I was small and flat chested, which was also a lucky break. You can kind of slip around unnoticed that way, which is exactly what you want. I was made fun of for being short, but it was mostly by boys who were shorter than me. I rarely brushed my hair and I was skinny. I bordered on being a tomboy, but not enough to be labeled one. It was a wonderful but short-lived time when I was in my body but not critical of it. If you ever want to see heaven, watch a bunch of young girls play. They are all sweat and skinned knees. Energy and open faces. My demon would receive my school picture and maybe gently suggest I “do something about those eyebrows,” but for the most part it left me alone. I felt safe in the middle – a girl who had a perfectly fine face but no one that drew any attention.

Then I started caring about boys and the demon pulled into my driveway. Once high school started, I began to see the real difference between the plain and the pretty. Boys, who were going through their own battles started to point out things about me I hadn’t yet noticed. One told me I looked like a frog. Some told me I smiled like a Muppet. A senior told me to stop looking at him with my “big, weird eyes.” I looked in the mirror at my flat chest and my freckles and heard a sound. It was the demon, suitcase in hand. He moved in and demanded the top bunk.

I cannot, in good faith, pretend I have fallen in love with how I look. The demon still visits me often. I wish I could tell you that being on television or having a nice picture in a magazine suddenly washes all of those thoughts away, but it really doesn’t. I wish I were taller or had leaner hands and a less crazy smile. I don’t like my legs, especially. My nose is great. I like my giant eyes, but they can get crazy. My hair is too thin for my liking.

[But] I had already made a decision early on that I would be a plain girl with tons of personality, and accepting it made everything a lot easier. If you are lucky, there is a moment in your life when you have some say as to what your currency is going to be I decided early on it was not going to be my looks. I have spent a lifetime coming to terms with this idea and I would say I am about 15 to 20 percent there. Which I think is great progress. I am not underestimating the access I get as a Blond, white lady from America.

Decide what your currency is early. Let go of what you will never have. People who do this are happier.

Being considered beautiful can be tough. Beautiful people can get objectified and underestimated. They didn’t do anything to earn their genes so they have to struggle to prove they are more than their hot bods. People assume they are happy, and most times this is not true. Plus, some beautiful people get a little addicted to being told they are beautiful and have real trouble when they get older, get less attention, or have their spouse cheat on them with someone considered “plain.”

Hopefully as you get older, you start to learn how to live with your demon. It’s hard at first. Some people give their demon so much room that there is no space in their head for love. They feed their demon and it gets really strong and then it makes them stay in abusive relationships or starve their beautiful bodies. But sometimes, you get a little older and get a little bored of the demon. Through good therapy and friends and self-love you can practice treating the demon like a hacky, annoying cousin. Maybe a day even comes when you are getting dressed for a fancy event and it whispers, “You aren’t pretty,” and you go, “I know, I know, now let me find my earrings.” Sometimes you say, “Demon, I promise you I will let you remind me of my ugliness, but I will check in later.”

Other times I take a more direct approach. When the demon starts to slither my way and say bad *stuff* about me I turn around and say, “Hey, Cool it. Amy is my friend. Don’t talk about her like that.” Sticking up for ourselves in the same way we would one of our friends is a hard but satisfying thing to do. Sometimes it works.

Even demons gotta sleep.
```

---

## IC-2309: Puppy

- Title: Puppy
- Author (byline): George Saunders
- Work: Tenth of December
- Publisher: Random House Trade Paperbacks
- Publication date as stated: Jan 2014
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 3037
- Already set (do not supply): none

### Source block (context only)

```text
Author: George Saunders
Book: Tenth of December
ISBN: 978-0812984255
Publisher: Random House Trade Paperbacks
Date (Month/Year): Jan 2014
```

### Introduction (context only: never use it for content warnings)

```text
Marie and her family search for a new addition to the family: a puppy for the kids. However, what they find at the house of Callie (the puppy’s owner) is far from cute or cuddly and the puppy is the least of their worries. “Puppy” by George Saunders
```

### Performance text (classify this)

```text
Twice already Marie had pointed out the brilliance of the autumnal sun on the perfect field of corn, because the brilliance of the autumnal sun on the perfect field of corn put her in mind of a haunted house—not a haunted house she had ever actually seen but the mythical one that sometimes appeared in her mind (with adjacent graveyard and cat on a fence) whenever she saw the brilliance of the autumnal sun on the perfect etc. etc., and she wanted to make sure that, if the kids had a corresponding mythical haunted house that appeared in their minds whenever they saw the brilliance of the etc. etc., it would come up now, so that they could all experience it together, like friends, like college friends on a road trip, sans pot.

But no. When she, a third time, said, “Wow, guys, check that out,” Abbie said, “O.K., Mom, we get it, it’s corn,” and Josh said, “Not now, Mom, I’m Leavening my Loaves,” which was fine with her; she had no problem with that, Noble Baker being preferable to Bra Stuffer, the game he’d asked for.

Well, who could say? Maybe they didn’t even have any mythical vignettes in their heads. Or maybe the mythical vignettes they had in their heads were totally different from the ones she had in her head. Which was the beauty of it, because, after all, they were their own little people! You were just a caretaker. They didn’t have to feel what you felt; they just had to be supported in feeling what they felt.

Still, wow, that cornfield was such a classic.

“Whenever I see a field like that, guys,” she said. “I somehow think of a haunted house!”

“Slicing Knife! Slicing Knife!” Josh shouted. “You nimrod machine! I chose that!”

Speaking of Halloween, she remembered last year, when their cornstalk column had tipped their shopping cart over. Gosh, how they’d laughed at that! Oh, family laughter was golden; she’d had none of that in her childhood, Dad being so dour and Mom so ashamed. If Mom and Dad’s cart had tipped, Dad would have given the cart a despairing kick and Mom would have stridden purposefully away to reapply her lipstick, distancing herself from Dad, while she, Marie, would have nervously taken that horrid plastic Army man she’d named Brady into her mouth.

Well, in this family laughter was encouraged! Last night, when Josh had goosed her with his GameBoy, she’d shot a spray of toothpaste across the mirror and they’d all cracked up, rolling around on the floor with Goochie, and Josh had said, such nostalgia in his voice, “Mom, remember when Goochie was a puppy?” Which was when Abbie had burst into tears, because, being only five, she had no memory of Goochie as a puppy.

Hence this Family Mission. And as far as Robert? Oh, God bless Robert! There was a man. He would have no problem whatsoever with this Family Mission. She loved the way he had of saying “Ho HO!” whenever she brought home something new and unexpected.

“Ho HO!” Robert had said, coming home to find the iguana. “Ho HO!” he had said, coming home to find the ferret trying to get into the iguana cage. “We appear to be the happy operators of a menagerie!”

She loved him for his playfulness—you could bring home a hippo you’d put on a credit card (both the ferret and the iguana had gone on credit cards) and he’d just say “Ho HO!” and ask what the creature ate and what hours it slept and what the heck they were going to name the little bugger.

In the back seat, Josh made the git-git-git sound he always made when his Baker was in Baking Mode, trying to get his Loaves into the oven while fighting off various Hungry Denizens, such as a Fox with a distended stomach; such as a fey Robin that would improbably carry the Loaf away, speared on its beak, whenever it had succeeded in dropping a Clonking Rock on your Baker—all of which Marie had learned over the summer by studying the Noble Baker manual while Josh was asleep.

And it had helped, it really had. Josh was less withdrawn lately, and when she came up behind him now while he was playing and said, like, “Wow, honey, I didn’t know you could do Pumpernickel,” or “Sweetie, try Serrated Blade, it cuts quicker. Try it while doing Latch the Window,” he would reach back with his non-controlling hand and swat at her affectionately, and yesterday they’d shared a good laugh when he’d accidentally knocked off her glasses.

So her mother could go right ahead and claim that she was spoiling the kids. These were not spoiled kids. These were well-loved kids. At least she’d never left one of them standing in a blizzard for two hours after a junior-high dance. At least she’d never drunkenly snapped at one of them, “I hardly consider you college material.” At least she’d never locked one of them in a closet (a closet!) while entertaining a literal ditchdigger in the parlor.

Oh, God, what a beautiful world! The autumn colors, that glinting river, that lead-colored cloud pointing down like a rounded arrow at that half-remodeled McDonald’s standing above I-90 like a castle.

Thank you, Lord, she thought, as the Lexus flew through the cornfield. You have given me so much: struggles and the strength to overcome them; grace, and new chances every day to spread that grace around. And in her mind she sang out, as she sometimes did when feeling that the world was good and she had at last found her place in it. Yes. Awesome. It was still solved so perfect.

There was plenty for him to do back there. A yard could be a whole world, like her yard when she was a kid had been a whole world. From the three holes in her wood fence she’d been able to see Exxon (Hole One) and Accident Corner (Hole Two), and Hole Three was actually two holes that if you lined them up right your eyes would do this weird crossing thing and you could play Oh My God I Am So High by staggering away with your eyes crossed, going “Peace, man, peace.”

When Bo got older, it would be different. Then he’d need his freedom. But now he just needed not to get killed. Once they found him way over on Testament. And that was across I-90. How had he crossed I-90? She knew how. Darted. That’s how he crossed streets. Once a total stranger called them from Hightown Plaza. Even Dr. Brile had said it: “Callie, this boy is going to end up dead if you don’t get this under control. Is he taking the medication?”

Well, sometimes he was and sometimes he wasn’t. The meds made him grind his teeth and his fist would suddenly pound down. He’d broken plates that way, and once a glass tabletop and got four stitches in his wrist.

Today he didn’t need the medication because he was safe in the yard, because she’d fixed it so perfect.

He was out there practicing pitching by filling his Yankees helmet with pebbles and winging them at the tree.

He looked up and saw her and did the thing where he blew a kiss.

Sweet little man.

Now all she had to worry about was the pup. She hoped the lady who’d called would actually show up. It was a nice pup. White, with brown around one eye. Cute. If the lady showed up, she’d definitely want it. And if she took it Jimmy was off the hook. He’d hated doing it that time with the kittens. But if no one took the pup he’d do it. He’d have to. Because his feeling was, when you said you were going to do a thing and didn’t do it, that was how kids got into drugs. Plus, he’d been raised on a farm, or near a farm anyways, and anybody raised on a farm knew that you had to do what you had to do in terms of sick animals or extra animals—the pup being not sick, just extra.

That time with the kittens, Jessi and Mollie had called him a murderer, getting Bo all worked up, and Jimmy had yelled, “Look, you kids, I was raised on a farm and you got to do what you got to do!” Then he’d cried in bed, saying how the kittens had mewed in the bag all the way to the pond, and how he wished he’d never been raised on a farm, and she’d almost said, “You mean near a farm” (his dad had run a car wash outside Cortland), but sometimes when she got too smart-assed he would do this hard pinching thing on her arm while waltzing her around the bedroom, as if the place where he was pinching were like her handle, going, “I’m not sure I totally heard what you just said to me.”

So, that time after the kittens, she’d only said, “Oh, honey, you did what you had to do.”

And he’d said, “I guess I did, but it’s sure not easy raising kids the right way.”

And then, because she hadn’t made his life harder by being a smart-ass, they had lain there making plans, like why not sell this place and move to Arizona and buy a car wash, why not buy the kids “Hooked on Phonics,” why not plant tomatoes, and then they’d got to wrestling around and (she had no idea why she remembered this) he had done this thing of, while holding her close, bursting this sudden laugh/despair snort into her hair, like a sneeze, or like he was about to start crying.

Which had made her feel special, him trusting her with that.

So what she would love, for tonight? Was getting the pup sold, putting the kids to bed early, and then, Jimmy seeing her as all organized in terms of the pup, they could mess around and afterward lie there making plans, and he could do that laugh/snort thing in her hair again.

Why that laugh/snort meant so much to her she had no freaking idea. It was just one of the weird things about the Wonder That Was Her, ha ha ha.

Outside, Bo hopped to his feet, suddenly curious, because (here we go) the lady who’d called had just pulled up.

Yep, and in a nice car, too, which meant too bad she’d put “Cheap” in the ad. Abbie squealed, “I love it, Mommy, I want it!,” as the puppy looked up dimly from its shoebox and the lady of the house went trudging away and one-two-three-four plucked up four dog turds from the rug.

Well, wow, what a super field trip for the kids, Marie thought, ha ha (the filth, the mildew smell, the dry aquarium holding the single encyclopedia volume, the pasta pot on the bookshelf with an inflatable candy cane inexplicably sticking out of it), and although some might have been disgusted (by the spare tire on the dining-room table, by the way the glum mother dog, the presumed in-house pooper, was dragging its rear over the pile of clothing in the corner, in a sitting position, splay-legged, a moronic look of pleasure on her face), Marie realized (resisting the urge to rush to the sink and wash her hands, in part because the sink had a basketball in it) that what this really was was deeply sad.

Please do not touch anything, please do not touch, she said to Josh and Abbie, but just in her head, wanting to give the children a chance to observe her being democratic and accepting, and afterward they could all wash up at the half-remodelled McDonald’s, as long as they just please please kept their hands out of their mouths, and God forbid they should rub their eyes.

The phone rang, and the lady of the house plodded into the kitchen, placing the daintily held, paper-towel-wrapped turds on the counter.

“Mommy, I want it,” Abbie said.

“I will definitely walk him like twice a day,” Josh said.

“Don’t say ‘like,’ ” Marie said.

“I will definitely walk him twice a day,” Josh said.

O.K., then, all right, they would adopt a white-trash dog. Ha ha. They could name it Zeke, buy it a little corncob pipe and a straw hat. She imagined the puppy, having crapped on the rug, looking up at her, going, Cain’t hep it. But no. Had she come from a perfect place? Everything was transmutable. She imagined the puppy grown up, entertaining some friends, speaking to them in a British accent: My family of origin was, um, rather not, shall we say, of the most respectable . . .

Ha ha, wow, the mind was amazing, always cranking out these—

Marie stepped to the window and, anthropologically pulling the blind aside, was shocked, so shocked that she dropped the blind and shook her head, as if trying to wake herself, shocked to see a young boy, just a few years younger than Josh, harnessed and chained to a tree, via some sort of doohickey by which— she pulled the blind back again, sure she could not have seen what she thought she had—

When the boy ran, the chain spooled out. He was running now, looking back at her, showing off. When he reached the end of the chain, it jerked and he dropped as if shot.

He rose to a sitting position, railed against the chain, whipped it back and forth, crawled to a bowl of water, and, lifting it to his lips, took a drink: a drink from a dog’s bowl.

Josh joined her at the window. She let him look. He should know that the world was not all lessons and Nintendo. It was also this muddy simple boy tethered like an animal.

“So what were you guys thinking of naming him?” the woman said, coming out of the kitchen.

The cruelty and ignorance just radiated from her fat face, with its little smear of lipstick.

“I’m afraid we won’t be taking him after all,” Marie said coldly.

Such an uproar from Abbie! But Josh—she would have to praise him later, maybe buy him the Italian Loaves Expansion Pak—hissed something to Abbie, and then they were moving out through the trashed kitchen (past some kind of crankshaft on a cookie sheet, past a partial red pepper afloat in a can of green paint) while the lady of the house scuttled after them, saying, wait, wait, they could have it for free, please take it—she really wanted them to have it.

No, Marie said, it would not be possible for them to take it at this time, her feeling being that one really shouldn’t possess something if one wasn’t up to properly caring for it.

“Oh,” the woman said, slumping in the doorway, the scrambling pup on one shoulder.

Out in the Lexus, Abbie began to cry softly, saying, “Really, that was the perfect pup for me.”

And it was a nice pup, but Marie was not going to contribute to a situation like this in even the smallest way. Simply was not going to do it.

The boy came to the fence. If only she could have said to him, with a single look, Life will not necessarily always be like this. Your life could suddenly blossom into something wonderful. It can happen. It happened to me.

But secret looks, looks that conveyed a world of meaning with their subtle blah blah blah—that was all bullshit. What was not bullshit was a call to Child Welfare, where she knew Linda Berling, a very no-nonsense lady who would snatch this poor kid away so fast it would make that fat mother’s thick head spin. Callie shouted, “Bo, back in a sec!,” and, swiping the corn out of the way with her non-pup arm, walked until there was nothing but corn and sky.

It was so small it didn’t move when she set it down, just sniffed and turned over.

Well, what did it matter, drowned in a bag or starved in the corn? This way Jimmy wouldn’t have to do it. He had enough to worry about. The boy she’d first met with hair to his waist was now this old man shrunk with worry. As far as the money, she had sixty hidden away. She’d give him twenty of that and go, “The people who bought the pup were super-nice.”

Don’t look back, don’t look back, she said in her head as she raced away through the corn.

Then she was walking along Teallback Road like a sportwalker, like some lady who walked every night to get slim, except that she was nowhere near slim, she knew that, and she also knew that when sportwalking you did not wear jeans and unlaced hiking boots. Ha ha! She wasn’t stupid. She just made bad choices. She remembered Sister Carol saying, “Callie, you are bright enough but you incline toward that which does not benefit you.” Yep, well, Sister, you got that right, she said to the nun in her mind. But what the hell. What the heck. When things got easier moneywise, she’d get some decent tennis shoes and start walking and get slim. And start night school. Slimmer. Maybe medical technology. She was never going to be really slim. But Jimmy liked her the way she was, and she liked him the way he was, which maybe that’s what love was, liking someone how he was and doing things to help him get even better.

Like right now she was helping Jimmy by making his life easier by killing something so he—no. All she was doing was walking, walking away from—

Pushing the words killing puppy out of her head, she put in her head the words beautiful sunny day wow I’m loving this beautiful sunny day so much—

What had she just said? That had been good. Love was liking someone how he was and doing things to help him get better.

Like Bo wasn’t perfect, but she loved him how he was and tried to help him get better. If they could keep him safe, maybe he’d mellow out as he got older. If he mellowed out, maybe he could someday have a family. Like there he was now in the yard, sitting quietly, looking at flowers. Tapping with his bat, happy enough. He looked up, waved the bat at her, gave her that smile.

Yesterday he’d been stuck in the house, all miserable. He’d ended the day screaming in bed, so frustrated. Today he was looking at flowers. Who was it that thought up that idea, the idea that had made today better than yesterday? Who loved him enough to think that up? Who loved him more than anyone else in the world loved him? Her. She did.
```

---

## IC-2310: R2, Where are You?

- Title: R2, Where are You?
- Author (byline): Tig Notaro
- Work: The Moth Presents All These Wonders
- Publisher: Crown Archetype
- Publication date as stated: March 2017
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1622
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tig Notaro
Book: The Moth Presents All These Wonders
ISBN: 978-1101904404
Publisher: Crown Archetype
Date (Month/Year): March 2017
```

### Introduction (context only: never use it for content warnings)

```text
Tig Notaro was a little-known comedian from Mississippi until a catalogue of tragedies changed her life – in 4 months. She was diagnosed with a potentially fatal condition called C. Diff. That’s where bacteria attacks the intestinal lining. Her mother, after a fall at home, lapsed into a coma and died. And her yearly mammogram revealed invasive cancer in both breasts. Her stand-up comedy took on a new tone that launched her to stardom. In R2, Where are You? Tig Notaro remembers her mother’s death and the impact it had on her and her stepfather.
```

### Performance text (classify this)

```text
(Pg 134-139) When I was little, I made a mess of my room, like any other child. The difference between me and other kids was, the person overseeing my cleanup was my stepfather, Rick. Rick was an attorney and in the military. He was very stoic, removed, emotionless.

I used to joke and say that he was kind of like C- 3PO, but with less emotion. And then it dawned on me recently that that joke actually doesn't make any sense, because C-3PO is very emotional.

He's like, "R2, where are you?!' You know? My stepfather was never in a panic looking for me the way C-3PO was looking for R2.

So cleaning up my room -- I was given an allotted time, and then Rick would come in, and whatever was out of place, he would put in a large trash bag. And then he'd lock it in the trunk of the car. Then I had to do chores to earn money to buy my toys back.

I know, it sounds harsh - because it is.

But to be fair, they were priced fairly. I could buy an entire Millennium Falcon, windup Evel Knievel, and stuffed monkey for like a nickel each. Totally reasonable.

But Rick, he was hard-core.

Meanwhile, my mother was very emotional and passionate and affectionate. She was wild and funny. She was originally from southern Mississippi and was raised in a very conservative house.

She was always wanting to make sure that I knew that the most important thing in life was to be happy. And she just supported anything I did. Anything I did was so cool, and I always looked adorable, and everything was just great, you know?

Even down to my dropping out of high school. My mother would brag to people.

She was like, "Yeah, Tig dropped out, you know? She's doing her own thing."

My own thing? I had nothing going on. I was working at a pizza parlor or selling po' boys. That was me "doing my own thing."

But then I found stand-up comedy, and I immediately had focus in my life. I was so passionate and excited about it.

And my mother, she didn't care if I was in some dingy club in Middle America or on TV, she just thought I was cool. As long as I was happy, she was happy.

Rick told me that my career was a waste of my time and a waste of my intelligence, and he thought that I should be a doctor or a lawyer. He suggested that I quit comedy and go to business school. Even just a couple of years ago, when my career was going fine, and I was making good money.

I said, "So you're telling me if I quit comedy and go to business school, something I'm not at all interested in, and end up working in a cubicle in an office somewhere, with the life sucked out of me, you would support that?"

He said, "Absolutely."

It was like, wow, okay.

Although my mother was very supportive of me, we certainly had our differences and problems. I remember one time a decade ago being on the phone fighting, and when the argument wasn't going anywhere, when I was midsentence, she just abruptly handed the phone to Rick.

He said, "Tig, your mother doesn't want to talk to you," and he just hung up on me.

I kept calling back, no answer. It was so frustrating and stifling. This March my phone rang, and the word PARENTS popped up on my caller ID. I was like, Oh, this is probably my mother calling to wish me a happy birthday. Because a couple of days before was my birthday, and I had missed her call.

But when I answered the phone, it was Rick. And Rick has only called me like two times in my entire life.

One was to tell me . . . I have no idea what that was about.

But the second time was this time, and he was calling to tell me that my mother had fallen and hit her head and was not going to make it.

I immediately pictured her lying in a hospital, just barely hanging on, saying, "Call Tig. Tell her to come to Texas to say good-bye."

I said, "Can I talk to my mother? Put her on the phone."

And he said, "No. You can't ever talk to her again."

My mother had suffered massive brain hemorrhaging, with zero chance of recovery. It was really so intense to process that-that I would never be able to talk to her again.

I've reflected a lot recently about that phone call over a decade ago when we were arguing, and I've thought about how I know my mother would give anything in the world to be able to come back to talk to me.

I always think that if somebody could be like, "Okay, you can come back, but you have to come back to that phone call where you're fighting with Tig," there would be zero fighting. It would be only I love you's and I'm sorry's from both of us.

After my mother's funeral, we left Mississippi, our hometown where she was buried, and we were driving back to Texas. My brother and my uncle were in one car, and Rick and I were in the other.

He said, "Tig, I want to talk to you about something."

And I was like, Oh, great. What could this be? I'm not in the mood.

He said, "I wanted to talk to you about that time that you said that I hurt your feelings. The time when I told you you should go to business school."

I said, "Oh, yeah. That hurt my feelings, but what really hurt my feelings was telling me my career was a waste of my time and a waste of my intelligence. That was hurtful."

And he started to cry. The robot started to cry.

He said, "I was wrong, and I wanted to apologize for that. I never understood you as a child. I didn't get you at all, and I tried to project onto you my life and my route, and I expected you to take that exact same route. And I'm realizing that it's not the child's responsibility to teach the parent who they are. It's the parent's responsibility to learn who the child is, and I didn't do that, and I'm sorry."

And I'm crying, too. I said, "So are you saying that if I said I was going to quit comedy and go to business school, you wouldn't support that anymore?"

He said, "Absolutely not. Comedy is the only thing in the world that you should be doing."

And I was like, Oh, my gosh. I didn't even realize that I needed that so desperately, to hear that. And the only thing that really bums me out is that my mother wasn't there to hear him tell me that.

This Thanksgiving I went to Texas, and we actually spent it with Rick's side of the family. I needed to get away and just be by myself, and I decided to drive to my mother and Rick's house. When I pulled up into the driveway, I had a full-on breakdown, just sobbing in the driveway, because I was like, Oh, my gosh, my mother is not in that house.

And of course I knew that, but it just really hit me in the driveway. Then I walked inside, and the house still smelled like her. And everything was just so quiet. I was looking around, and still photos that were framed just seemed so still - moments in time caught and gone forever. All the photos were still placed where my mother had placed them over the years.

I started opening drawers, because I wanted to just see something of my mother's. She would write little notes to herself, like, "Dentist 2:00 p.m. tomorrow." And she was an artist, and she would sketch me perfectly on a napkin when I was just sitting around, and so I was looking for those kinds of things in the drawers, and there wasn't anything in there.

I went to open a closet, and there's nothing there. I found nothing in any drawers or closets, and I started going around the house, just running around, trying to find something. Then I was in this panic and crying even harder.

Rick had gutted the house like he had when I was a child with a trash bag.

Everything was gone, and I was like, That is it. I am done with this person. I couldn't believe I had fallen for that conversation, and I was so ready to write him off immediately. I was done.

I called him on my cell phone, and he said, "Hello, Tig, how are you doing?"

I said, "Not good. Not good. All of my mother's things are gone, and so are my childhood things."

He said, "Hold on a minute. Go into my bedroom. Go into my closet," and he started directing me.

I was like, "Yeah?"

He said, "Look at the top shelf."

And up there he had placed my mother's things, and my childhood things. I opened the box. She was a dancer, too, and there were her ballet slippers and photos.

I was like, "You're lucky."

And although before March, when the word PARENTS popped up on my caller ID, it represented my mother and Rick. Now when the word PARENTS pops up on my caller ID, it's only Rick.

We have very different cleanup techniques, but I'm learning to get used to that.
```

---

## IC-2311: The Rapture of Caanan

- Title: The Rapture of Caanan
- Author (byline): Sheri Reynolds
- Work: Not specified
- Publisher: Berkley Trade
- Publication date as stated: April 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1218
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sheri Reynolds
ISBN: 978-0425162446
Publisher: Berkley Trade
Date (Month/Year): April 1997
```

### Introduction (context only: never use it for content warnings)

```text
Grandpa Herman, founder of The Church of Fire and Brimstone and God's Almighty Baptizing Wind, has a flock to tend to -- his congregation, where some mimic Herman's steadfast and unnerving faith, and some who occasionally stray from the righteous path. And perhaps the most surprising stray of all is his granddaughter, Ninah. Fourteen-year-old Ninah, who finds difficulty in controlling her first adolescent stirrings, manages somehow convince herself the things she does with her prayer partner, James, is nothing more than learning about Jesus's love through each other. And once the community finds out, the whole system of the Church is shocked to a halt. "The wages of sin is death," says Grandpa Herman. The rapture has come. The Rapture of Caanan by Sheri Reynolds.
```

### Performance text (classify this)

```text
“Tell me the story, Nanna,” I used to beg my grandma, leaning against her in the porch swing.

“You don’t want to hear that old story, Herman shouldn’ta never put it in that sermon.”

“Please tell it, you tell it better than Grandpa.”

My grandpa Herman Langston was founder and preacher of The Church of Fire and Brimstone and God’s Almighty Baptizing Wind. I think when he was trying to come up with a name for it, he just couldn’t make up his mind, so he put all his ideas together and nobody said a thing.

“We’ve all sinned in the eyes of God, My own wife Leila turned her back on God. She saw her own mother engaging in sins of the flesh and did not tell. And on the say that her own mother pulled out a rifle and shot her father through the back so she could live in sin with a boy young enough to be her son, did she call out to God? No.”

I don’t think that anybody know exactly how Grandpa Herman came up with his brand of Christianity. In the summers, we worked the fields all day. By the time supper came, we were so weary that even breathing felt like work. I had fallen asleep at the table.

“Did you say your prayers young lady?” Mamma asked. “Before you fell asleep?”

“I didn’t mean to fall asleep.”

“Don’ talk back. Did you say your prayers Ninah?”

“No, ma’am.”

Then Mama led me to bed. When she pulled back my covers, there were cockleburs and sandspurs scattered all over my sheets. I knew there would be. I couldn’t sleep for a long time. The prickles were sticking in my back. I guess I deserved it.

Sometimes the children could get permission to go horseback riding. One afternoon we were out in the woods, with me and Mustard and James on one horse. The girls always got sandwiched between the boys, and that day I was protected by Mustard from the front and James from the back.

“Let’s take then to the top and run down fast.”

“Don’t do it Mustard,” James warned from behind me.

But Mustard kicked the mare and she took off.

“Ninah, tell him to stop.”

But I didn’t want him to stop. It wasn’t that I wanted the horse to get hurt. I was too busy trying to memorize the way James’ legs felt around my backside, hanging on, the way his arms felt buckled around my middle.

All that winter James and I came together as prayer partners. We prayed like never before.

One Saturday night, we went to the choir loft. James led me through the little swinging door, and we knelt on the second row.

“Lord, I’ve been praying and praying about this, and I know you’ve given Ninah something to say to me.” “”I’m here, God. I’ve been praying for this too. I want to be the one to give James your special instructions for his life.”

“Lord, I’m not sure that I’m feeling you right, but I want to.”

And then he kissed me like a waterfall, and I kept my mouth wide open.

“Ninah, this can’t be right. We have to pray.”

“God, I think we’re getting mixed signals. You have to lead us cause we don’t’ know what to do.”

And then I kissed him.

“Ninah, we have to pray!”

“That’s what we’re doing.”

I ran my lips across his eyelid. And then God spoke. Really fast. And then I knew him like I’d never known him before.

Grandpa Herman gave another sermon, an angry one about Hell.

“Fornication is ground for being thrown out of the community. Fornication is grounds for being tossed sidelong off the streets of Jasper, through the Pearly Gates, and into the Great Lake of Fire.”

I peeked over at James, who sat at the other side of the table. He was staring blankly. I tried and tried to will him to look at me, but he didn’t. Inside, I felt the worst lonely I’d ever known.

We were on the far side of the barn, stretched out on our backs, looking up at dark sky pocked with clouds.

“Do you ever worry that what we do sometimes during prayers could be considered…fornicating?”

“No.” I lied. “What we’re doing is different. It’s just a part of prayer.”

I didn’t know what to do. I’d taken something beautiful like our prayers and turned them into something horrible – just so I could keep feeling good. And I didn’t feel good.

I knew that I was probably having a baby. Then I got to thinking that maybe it was Jesus’ baby – because if we really hadn’t been sinning and had only been knowing Jesus through each other, then it couldn’t be anything but Jesus’

I decided I’d better tell James about it.

“I’m, you now, with child.”

“Ninah, you can’t be.”

“I am.”

“Oh hell, fire and damnation. Ninah, they’re gonna kill us.”

“Even if it’s Jesus’ baby?”

“It’s my baby Ninah. Not Jesus’.”

“But if I was knowing Jesus through you, then you were just the vehicle.”

“Oh, for God’s sake, Ninah.”

“You mean you don’t think it was Jesus – when we touched?”

“No. It was me and you, sinning like crazy.”

“But even at first?”

“It was me and you.”

“If you knew we weren’t being Jesus for each other, then why’d you deep doing it?”

“I didn’t think God would let it happen. I didn’t know something so awful could come from something so nice.”

I saw Mustard stretched out on a drag, already asleep even though it was barely dark. I peeked into the barn, calling James, but he wasn’t there either.

“Did you find him?”

“No.” “Well, James probably snuck off to the pond to cool down.”

“You think so? He was expecting me.”

“Yeah, maybe he forgot.”

“Well, I’m real worried about him.”

Ten minutes later, I was sitting behind Mustard on a horse, trotting through the woods. I was almost sure James wasn’t swimming.

Mustard stopped the horse near an old tree that had fallen into the pond. I hopped off right away, climbed into the tree.

“James.”

Mustard bolted towards me. By the time he reached me, I had already picked up the piece of rope I found running along the length of the tree.

Mustard grabbed the rope behind me, and we both pulled, and Mustard told me it might just be a sunken boat and I cried because the other end was too heavy to be the kind of boat you can float in a pond.

Finally we pulled a massive piece of tree out of the water. I could see a body tied to it. I stood on the trunk looking down at James, his mouth gaping. I was suddenly still, and I didn’t hear Mustard say, “Give me the rope,” until he’d already pulled it from my hands.

Some people say you can’t change history, but that isn’t entirely true. We did it at Fire and Brimstone. James didn’t take his own life. He drowned on a hot night, caught on a root in the bottom of the pond. Nobody ever mentioned that he was tethered to that sunken tree with thick deliberate knots.
```

---

## IC-2312: The Rememberer

- Title: The Rememberer
- Author (byline): Aimee Bender
- Work: The Girl in the Flammable Skirt, Pgs 3-8
- Publisher: Anchor
- Publication date as stated: Aug 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ANNIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1126
- Already set (do not supply): none

### Source block (context only)

```text
Author: Aimee Bender
Book: The Girl in the Flammable Skirt, Pgs 3-8
ISBN: 978-0385492164
Publisher: Anchor
Date (Month/Year): Aug 1999
```

### Introduction (context only: never use it for content warnings)

```text
In a world ruled by intellect, everything sharpens into angles and proofs, and slowly (almost politely) the heart learns to quiet itself. We become so devoted to logic that we begin a kind of “reverse evolution,” shedding our compassion, love and relationships in exchange for a more logical precision. And with this shedding comes the dissolution of what makes us human.

Before we notice, we’ve traded a heart for a plan, and something vital inside us goes dim . . . not extinct, but waiting in the dark for us to remember that a life perfectly reasoned can still feel profoundly empty.

The Rememberer by Aimee Bender
```

### Performance text (classify this)

```text
ANNIE: My *boyfriend* is experiencing reverse evolution. I tell no one. I don't know how it happened, only that one day he was my *boyfriend* and the next he was some kind of ape. It's been a month, and now he's a sea turtle. I keep him on the counter, in a baking pan filled with saltwater. "Ben," I say to his small protruding head, "can you understand me?" and he stares with eyes like little droplets of tar and I drip tears into the pan, a sea of me.

ANNIE: He is shedding a million years a day. I am no scientist, but this is roughly what I figured out. I went to the old biology teacher at the community college and asked him for an approximate timeline of our evolution.

According to him, the whole process should take about a year, but from the way things are going, I think we have less than a month left.

At first, people called on the phone and asked me where was Ben. Why wasn't he at work? Why did he miss his lunch date with those clients? His out-of-print special-ordered book on civilization had arrived at the bookstore, would he please pick it up? I told them he was sick, a strange sickness, and to please stop calling. The odd thing was, they did. They stopped calling. After a week the phone was silent and Ben, the baboon, sat in a corner by the window, wrapped up in a drapery, chattering to himself.

The last day I saw him human he put his head in his hands and sighed. He was sad about the world. This was not unusual. He was always sad about the world. It was a large reason why I loved him. On his last human day, he said, "Annie, don't you see? We're all getting too smart. Our brains are just getting bigger and bigger, and the world dries up and dies when there's too much thought and not enough heart." He looked at me pointedly, blue eyes unwavering. "Like us, Annie," he said. "We think far too much."

I sat down. I remembered how he *once* woke me up in the middle of the night, led me outside to the stars and whispered: Look, Annie, look . . . there is no space for anything but dreaming. I listened, sleepily, wandered back to bed and found myself wide awake, staring at the ceiling, unable to dream at all. Ben fell asleep right away, but I crept back outside. I tried to dream up to the stars, but I didn't know how to do that. I tried to find a star no one in all of history had ever wished on before, and wondered what would happen if I did.

What did I wish for? I wished for good. That's all. Just good. My wishes became generalized long ago, in childhood; I learned quick the consequence of wishing specific.

I took him in my arms, my sad man. See, we're not thinking, I whispered into his ear, we're not thinking at all and he pressed his head into my shoulder and held me tighter. Afterwards, we went outside again; there was no moon and the night was dark. He said he hated talking and just wanted to look into my eyes and tell me things that way. I let him and it made my skin lift, the things in his look. Then he told me he wanted to sleep outside for some reason, and in the morning when I woke up in bed, I looked out to the patio and there was an ape sprawled on the cement, great furry arms covering his head to block out the glare of the sun.

Even before I saw the eyes, I knew it was him. And once we were face to face, he gave me his same sad look and I hugged those enormous shoulders. I didn't even really care, then, not at first; I didn't panic and call 911. I sat with him outside and smoothed the fur on the back of his hand.

We sat on the lawn together and ripped up the grass. I didn't miss human Ben right away; I wanted to meet the ape too, to take care of *him* like a son, a pet; I wanted to know him. . . but I didn't realize he wasn't coming back.

Now I come home from work and look for his regular-size shape walking and worrying and realize, over and over, that he's gone. I pace the halls. I chew whole packs of gum in mere minutes. I review my memories and make sure they're still intact because if he's not here, then it is my job to remember. I think of the way he wrapped his arms around my back and held me so tight it made me nervous and the way his breath felt in my ear: right.

When I go to the kitchen, I peer in the pan and see he's some kind of salamander now. He's small. "Ben," I whisper, "do you remember me? Do you remember?" His eyes roll up in his head and I dribble honey into the water. He used to love honey.

This is the limit of my limits. You don't ever know for sure where it is and then you bump against it and bam, you're there. Because I cannot bear to look down into the water and not be able to find him at all, to search the tiny waves with a microscope lens and to locate *Ben*, the one-celled wonder, bloated and blind, brainless, benign, heading clear and small, into nothingness.

I put him in the passenger seat of the car, and drive him to the beach. Walking down the sand, I nod at people on towels, laying their bodies out to the sun and wishing. At the water's edge, I stoop down and place the whole pan on the tip of a baby wave. It floats well…

Ben the salamander swims out. I wave to the water with both arms, big enough for him to see if he looks back. I turn around and walk back to the car.

Sometimes I think he'll wash up on shore. A naked man with a startled look who has been to history and back. I keep my eyes on the newspaper. I make sure my phone number is listed. I walk around the block at night in case he doesn't quite remember which house it is. I feed the birds outside and sometimes before I put myself to bed, I place my hands around my skull to see if it's growing, and wonder what, of any use, would fill it if it did.
```

---

## IC-2313: Residents and Transients

- Title: Residents and Transients
- Author (byline): Bobbie Ann Mason
- Work: Shiloh and Other Stories
- Publisher: Modern Library
- Publication date as stated: Aug 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1807
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bobbie Ann Mason
Book: Shiloh and Other Stories
ISBN: 978-0375758430
Publisher: Modern Library
Date (Month/Year): Aug 2001
```

### Introduction (context only: never use it for content warnings)

```text
This is the story of a woman caught in a moment of transition. Her husband, Stephen, is in Louisville, searching for a new house. She is supposed to sell their home and move to Louisville, but there is a part of her that wants to remain in her hometown. In addition, Mary finds herself caught between two men: her lover, Larry, and her husband.

She vacillates between two different lives, unable to choose her future. Residents and Transients by Bobbie Ann Mason
```

### Performance text (classify this)

```text
Larry is our dentist. When I saw him in the post office earlier in the summer, I didn't recognize him at first, without his smock and drills. But then we exchanged words-"Hot enough for you" or something like that-and afterward I started to notice his blue Ford Ranger XII passing on the road beyond the fields. We are about the same age, and he grew up in this area, just as I did, but I was away for eight years, pursuing higher learning. I came back to Kentucky three years ago because my parents were in poor health. Soon after I returned, I met Stephen, and we were married within a year.

"I can't imagine living on a street again," I said to my husband. I complained for weeks about living with houses within view. I need cornfields. When my parents left for Florida, Stephen and I moved into their old farmhouse, to take care of it for them. I love its stateliness, the way it rises up from the fields like a patch of mutant jimsonweeds. I'm fond of the old white wood siding, the sagging outbuildings. But the house will be sold this winter, after the corn is picked, and by then I will have to go to Louisville.

The cats came with the farm. When Stephen and I appeared, the cats gradually moved from the barn to the house. They seem to be my responsibility, like some sins I have committed, like illegitimate children. The cats are Pete, Donald, Roger, Mike, Judy, Brenda, Ellen, and Patsy. Reciting their names for Larry, my lover of three weeks; I feel foolish. Larry had asked, "Can you remember all their names?"

"What kind of question is that?" I ask, reminded of my husband's new job. Stephen travels to cities throughout the South, demonstrating word-processing machines, fancy typewriters that cost thousands of dollars and can remember what you type. It doesn't take a brain like that to remember eight cats.

"No two are alike," I say to Larry helplessly. We are in the canning kitchen, an airy back porch which I use for the cats. Larry strokes a cat with one hand and my hair with the other. He says he has never known anyone like me. He calls me Mary Sue instead of Mary. No one has called me Mary Sue since I was a kid.

Larry started coming out to the house soon after I had a six-month checkup. I can't remember what signals passed between us, but it was suddenly appropriate that he drop by. When I saw his truck out on the road that day, I knew it would turn up my lane.

"I brought you some ice cream," he said.

"I didn't know dentists made house calls. What kind of ice cream is it?"

"I thought you'd like choc-o-mint."

"You're right."

"I know you have a sweet tooth."

"You're just trying to give me cavities, so you can charge me thirty dollars a tooth."

I opened the screen door to get dishes. One cat went in and another went out. The changing of the guard. Larry and I sat on the porch and ate ice cream and watched crows in the corn. The corn had shot up after a recent rain.

"You shouldn't go to Louisville," said Larry. "This part of Kentucky is the prettiest. I wouldn't trade it for anything."

"I never used to think that. Boy, I couldn't wait to get out!" The ice cream was thrillingly cold. I wondered if Larry envied me. Compared to him, I was a world traveler. I had lived in a commune in Aspen, backpacked through the Rockies, and worked on the National Limited as one of the first female porters. When Larry was in high school, he was known as a hell-raiser, so the whole town was amazed when he became a dentist, married, and settled down. Now he was divorced.

Larry and I sat on the porch for an interminable time on that sultry day, each waiting for some external sign-a sudden shift in the weather, a sound, an event of some kind-to bring our bodies together. Finally, it was something I said about my new filling.

Stephen is on the phone. It is 3:00 P.M. and I am eating supper-pork and beans, cottage cheese and dill pickles. My routines are cockeyed since he left. "I found us a house!" he says excitedly. His voice is so familiar I can almost see him, and I realize that I miss him. "I want you to come up here this weekend and take a look at it," he says.

"Do I have to?" My mouth is full of pork and beans.

"I can't buy it unless you see it first."

"I don't care what it looks like."

"Sure you do. But you'll like it. It's a three-bedroom brick with a two-car garage, finished basement, dining alcove, patio-"

"Does it have a canning kitchen?" I want to know. Stephen laughs. "No, but it has a rec room."

I quake at the thought of a rec room. I tell Stephen, "I know this is crazy, but I think we'll have to set up a kennel in back for the cats, to keep them out of traffic."

"Aren't you carrying this a little far?" Stephen asks, sounding worried. He doesn't suspect how far I might be carrying things. I have managed to swallow the last trace of the food, as if it were guilt.

Now Stephen is talking about our investments and telling me things to do at the bank. When we buy a house, we will have to get a complicated mortgage.

"The thing about owning real estate outright," he says, "is that one's assets aren't liquid."

"Daddy always taught me to avoid debt."

"That's not the way it works anymore."

The other day Larry took me up in a single-engine Cessna. We circled west Kentucky, looking at the land, and when we flew over the farm I felt I was in a creaky hay wagon, skimming just above the fields. I thought of the Dylan Thomas poem with the dream about the birds flying along with the stacks of hay. I could see eighty acres of corn and pasture, neat green squares. I am nearly thirty years old. I have two men, eight cats, no cavities.

It is a hot summer night, and Larry and I are driving back from Paducah. We went out to eat and then we saw a movie. We are rather careless about being seen together in public. Larry wears a cloudy expression of love. Everything about me that I find dreary he finds intriguing.

"In the wild, there are two kinds of cat populations," I tell him. "Residents and transients. Some stay put, in their fixed home ranges, and others are on the move. They don't have real homes. Everybody always thought that the ones who establish the territories are the most successful. They are the strongest, while the transients are the bums, the losers."

"Is that right? I didn't know that." Larry looks genuinely surprised. I think he is surprised at how far the subject itself extends. He is such a specialist. Teeth.

I continue bravely. "The thing is-this is what the scientists are wondering about now-it may be that the transients are the superior ones after all, with the greatest curiosity and most intelligence. They can't decide."

"That's interesting." He is the most relaxed man I've ever known. "None of that is true of domestic cats," Larry is saying. "They're all screwed up."

"I bet somewhere there are some who are footloose and fancy free," I say, not believing it. I think of living in Louisville. Stephen said the house he wants to buy is not far from Iroquois Park. I'm reminded of Indians. When certain Indians got tired of living in a place-when they used up the soil, or the garbage pile got too high-they moved on to the next place.

Larry says then, "Do you want me to stop coming out to see you?"

"What makes you ask that?..

"I don't have to be Einstein to tell that you're bored with me."

"I don't know. I still don't want to go to Louisville, though."

"I don't want you to go. I wish you would just stay here and we would be together."

"I wish it could be that way," I say, trembling slightly. "I wish that was right."

We round a curve. The night is black. The yellow line in the road is faded. In the other lane I suddenly see a rabbit move. It is hopping in place, the way runners will run in place.

Its forelegs are frantically working, but its rear end has been smashed and it cannot get out of the road.

By the time we reach home I have become hysterical. Larry has his arms around me, trying to soothe me, but I cannot speak intelligibly and I push him away. In my mind, the rabbit is a tape loop that crowds out everything else.

Inside the house, the phone rings and Larry answers. I can tell from his expression that it is Stephen calling. It was crazy to let Larry answer the phone. I was not thinking. I will have to swear on a stack of cats that nothing is going on. When Larry hands me the phone I am incoherent.

"Listen," I say in a tone of great urgency. "I'm coming to Louisville to see that house. There's this guy here who'll give me a ride in his truck-"

Stephen is annoyed with me. He seems not to have heard what I said, for he is launching into a speech about my anxiety.

"Those attachments to a place are so provincial," he says. "People live all their lives in one place."

"What's wrong with that?"

"You've got to be flexible," he says breezily. "That kind of romantic emotion is just like flag-waving. It leads to nationalism, fascism-you name it; the very worst kinds of instincts. Listen, Mary, you've got to be more open to the way things are."

Stephen is processing words. He makes me think of liquidity, investment postures.

After I hang up, I rush outside. Larry is discreetly staying behind. Standing in the porch light, I listen to katydids announce the harvest. It is that kind of night, mellow and languid, when you can hear corn growing. I see a cat's flaming eyes coming up the lane to the house. One eye is green and one is red, like a traffic light. Her blue eye shines red and her yellow eye shines green. In a moment I realize that I am waiting for the light to change.
```

---

## IC-2314: The Resurrection of Wonder Woman

- Title: The Resurrection of Wonder Woman
- Author (byline): Eleanor Vincent
- Work: At the End of Life, Pg 233
- Publisher: In Fact Books
- Publication date as stated: March 2012
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ELEANOR, DR. CARR, NURSE, WIFE
- Teaser before the introduction: Yes
- Spoken words (computed): 1607
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eleanor Vincent
Book: At the End of Life, Pg 233
ISBN: 978-1937163044
Publisher: In Fact Books
Date (Month/Year): March 2012
```

### Introduction (context only: never use it for content warnings)

```text
More than 105,000 people await transplants in the United States today. Each day, on average, eighteen of them die waiting. If you had to answer the question “Would you consider organ donation?” for your nineteen-year-old daughter, how would you respond?

The Resurrection of Wonder Woman by Eleanor Vincent
```

### Performance text (classify this)

```text
ELEANOR: Pink from her bath and aglow with excitement, three-year-old Maya perched on the edge of the bathtub. I stretched out my arms and she jumped, landing in the white terrycloth towel I held out. Wrapping her in the towel, I draped a dry towel over my own shoulders and led her into our game. The towels became two white capes. We ran from one end of our apartment to the other as our capes billowed behind us. Together we called, “Wonder Woman! Wonder Woman!” Exulting in our superpowers, we imagined we wore magic bracelets on our wrists and golden lariats around our waists, just like our heroine. The fantasy of being all-powerful ended at the side of Maya’s bed, where I helped her into her nightgown and tucked her in, a little girl again. It was the 1970s, and I made a point of reading bedtime stories about exceptional women to her so that Maya would dream of daring and of genius. I hoped one day my daughter would become a woman who embraced her own power.

Sixteen years later, after a daredevil stunt left Maya in a coma, I wished I’d told her more cautionary tales.

ELEANOR: Maya’s accident had happened three days earlier on a hot April afternoon. She had hiked to a meadow laced with oat grass and wildflowers. A ravine full of scrub oak and laurel trees tumbled down to a dry creek bed. One of her friends dared her to ride bareback on a horse they found there unfenced and unsecured. The animal reared and threw Maya to the ground with such force that she never regained consciousness.

I walked toward my daughter’s bed, past the curtains surrounding families bent over other silent forms. After seventy-two hours of nursing my hope, willing my daughter to recover, an impossible thought dawned— Maya might not make it. When I reached her bedside, I trembled with this new possibility. I took her hand in mine. (to Maya) Sweetheart, it’s Mom. I’ve been telling you that you will get well. But maybe that’s not right; maybe what I want isn’t what matters . . . You decide, honey. I won’t hold you back.

(to audience) As I stood looking down at the beautiful young woman she had become, I knew I had no magic bracelet, no supernatural powers. Neither did she.

I leaned into her and whispered the biggest lie of my life, never doubting she could hear me. (to Maya) I’ll be all right, sweetheart, if you need to go.

As my determination dissolved, I wanted to throw myself across her chest and give in to hours of unsuppressed weeping. But then I had a new thought: If I break down, it will be too hard for her to die. My task now is to let her go.

Maya’s chest rose and fell. The ventilator hissed, the monitors beeped, a fiber optic cable snaked into her skull to measure the pressure inside her brain. A few hours later, her temperature soared.

DR. CARR: We did all we could. Would you consider organ donation?

ELEANOR: The question hung in the air for a long moment. In that instant I saw my baby the day she was born, pink and bald, her eyes squinting up at me as if the light might blind her. I saw my diabetic mother plucking at the sheets on her deathbed as her kidneys failed. I pictured families in other hospital conference rooms waiting for bad news. “Yes,” I heard myself say. The love and energy I had poured into my daughter, her very life, must continue. I could no more accept that Maya was truly dead than I could fly to the moon or allow any vital part of her that could save another human being to go to her grave.

I trembled uncontrollably. I was about to give my daughter away in pieces. If I had fought harder, could I have held her here?

******

ELEANOR: Across the San Francisco Bay, I later learned, a figure shrouded in white lay on a hospital bed, near death. The man’s heart failure was so profound that his fingernails had turned blue. This man, comatose and oxygen-starved, was a blip on the computer screen of the national donor registry. Along with four thousand others on the heart transplant list, he was waiting for someone to die so that he could live. By his side, his wife watched the rise and fall of her husband’s chest, the backs of her hands wet with tears she rubbed away without noticing. She turned her back on her husband’s bed and prayed for a miracle. She didn’t know it, but her prayer had just been answered in another hospital only thirty miles away on the other side of the San Francisco Bay.

Our donor coordinator was a young nurse, not many years older than Maya. She read me a list of Maya’s vital organs as if they were car parts, asking permission to salvage each one.

NURSE: Do you give consent for her corneas?

ELEANOR: Yes.

NURSE: Do you give consent for her lungs?

ELEANOR: (in agony) Look, I can save us both a lot of agony . . . Just take it—take it all.

NURSE: (shaking her head) The law requires that I must go through each one . . . I know this must be hard for you.

ELEANOR: It is unbearable. (balling her hands into fists she smiles sardonically) I am going to initial each of these blanks and sign this form here at the bottom. Then we are both going to agree that we did this legally. But I am not going to sit here while you read me a list of my daughter’s organs. You have my permission to take anything that will save lives or reduce pain. Just don’t make me stay here another minute. *****

ELEANOR: As a “biomort,” or a “beating heart cadaver,” Maya was suspended in a nether world between life and death. Her brain would never function again, but with life support, her heart continued to beat and her chest rose and fell, filled with mechanically produced oxygen. Within minutes, “life support” became “organ support.” The ventilator still distended her mouth, but the cable that had run from the computer into her bandaged skull was gone. I slid my right hand under her shoulder and gazed down at her serene young face, playing with her warm fingers, now utterly still. My chest tightened as if something was squeezing the air from my lungs. I looked down at my lovely, lovely girl. (to Maya in a whisper) I love you, Maya. You are as beautiful to me as the day you were born. I’m letting you go now with all my heart, with all my love. (to audience) I put my head on Maya’s chest. The rise and fall of her mechanically powered breath was like a whoosh of ocean tide—in and out, in and out. The steady drumming of her heart filled my senses. At last, I raised my head. There would be no last breath to signal the end. I simply had to walk away and leave her. I could not contemplate what would come next . . . A few hours later, surgeons began to “harvest” my daughter’s organs and tissues, work that continued through the night. I allowed doctors to take a hacksaw to my daughter’s chest. They broke open her rib cage to extract her heart, her liver, and her kidneys.

******

ELEANOR: Twelve days after Maya died, I received a letter from our transplant coordinator, the young nurse I had treated so curtly. She told of the miracles that resulted from my decision. Maya’s kidneys had been flown across the country to the Boston area. Her liver had gone to a thirty-eight-year-old woman with a rare form of liver disease. She was the mother of a seven-year-old daughter and would have died without the transplant. Maya’s corneas had restored sight for two people in the Bay Area.

I burst into tears when I reached the paragraph about Maya’s heart. It had been given to a fifty-four-year-old businessman. Tucked between the folds of the letter I found a note from his wife. She had not signed her name, but I could hear her voice through her words.

WIFE: My children and I want to express how thankful we are to you for the gift of life you have given us. My husband is getting better every day and the children, eight and twelve years old, have another chance to grow up with a father. We will pray for you and your daughter every day.

ELEANOR: She signed it, “The Receiving Family.” (beat) During the months that followed I would often pull out that ivory card with its neat, spiky letters and reread it, as if I could balance my grief against another family’s joy, as if it were ballast enough. *****

ELEANOR: Perhaps Maya was Wonder Woman, after all. She lived long enough to express her daring and genius more than most mortals. Maya was a gifted young actress. The day before her accident, she had learned about her acceptance as a community college transfer student into the UCLA School of Theater, Film, and Television, an honor granted very few. She was offered a full scholarship. She had been out celebrating, riding a strange horse bareback in a remote field.

She flew to the ground with her dreams and her beauty intact and lost consciousness instantly. The last time I spoke with her was the morning of the accident. I ruffled her hair on my way out the door. (to Maya) I’m so proud of you, honey. (to audience) She grinned up at me from the armchair where she was perched, still in pajamas, and gave me a Top Gun–style thumbs up.

(pantomimes this with a huge smile) “Love you, Mom,” she said. (beat) Love you too.
```

---

## IC-2315: Return from the Depot!

- Title: Return from the Depot!
- Author (byline): Elizabeth Crane
- Work: When the Messenger is Hot
- Publisher: Back Bay Books
- Publication date as stated: Jan 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1674
- Already set (do not supply): none

### Source block (context only)

```text
Author: Elizabeth Crane
Book: When the Messenger is Hot
ISBN: 978-0316608466
Publisher: Back Bay Books
Date (Month/Year): Jan 2004
```

### Introduction (context only: never use it for content warnings)

```text
The shock that is felt after the death of a parent may continue for weeks, months, or even years. “Forgetting” that your loved one is gone, you may expect her to walk in the door or to be on the other end of the line when the telephone rings. And each time it happens, you’re confronted once again with the brutal reality that she is gone forever. Denial is an understandable defense against that brutal reality. It blunts the impact of the loss and allows you to process those overwhelming feelings more gradually. On one level you recognize that your mother has died; on another level you’re unable to grasp all the ramifications of that harsh and unwelcome reality. In Return from the Depot! The self-defense of denial takes on a more ominous tone, one that brings the speaker to the brink of sanity itself.

Return from the Depot! by Elizabeth Crane.
```

### Performance text (classify this)

```text
Naturally, there are people who think I need counseling. They tell me that I’m in denial. They say “I’m here for you.” They say “You can call anytime just to talk.” They say, “Three years is a long time, it might be time to let go.” I’m not angry with them. Some of them have lost people too. But there’s something they don’t understand. My mother is coming back!

Denial, anger, bargaining, depression, acceptance. As I said, the collective belief is that I’m stuck in the denial phase when in fact, my belief is that this is just a big mistake that will eventually be straightened out. If anything, I’m in phase two (anger) because I have quite a bit of a bone to pick with whoever’s in charge and frankly I’d be willing to strike all kinds of bargains if I knew who that was. But it’s hard to be depressed when you know with absolute certainty that sooner or later the person who everyone else things is dead is coming back. There’s nothing to be depressed about. And there’s certainly nothing to accept.

I went to psychics. I thought a psychic would be the first to see my point of view, to say, “Of course it was a terrible mistake,” and that they would then immediately locate the perpetrators of the mistake, that they would say something like. “You need to go speak with Fritz Miller in the accounting department. He’ll give you the appropriate paperwork and straighten the whole thing out.” But they don’t; they, too, offer earnest sentiments and tilted heads and the best they’ll do is say, “She wants you to know she’s fine. She’s in a better place.” And when I’d ask for the exact location of the better place they say things like “the other side,” which isn’t of much use, and I spent a lot of time trying to figure out the other side of WHAT?

I’ve been back at work since shortly after the funeral, more earnest looks and whispers, and I try to keep her house up as best I can, which is sometimes hard because I live in Chicago and the house is in New Jersey, but I go back a few times a year and I have a gardener and a housekeeper come every once in a while so the place will look nice when she gets back.

My mother’s friends and family grieved. They sobbed, they went to groups, the accepted. I waited. And as it turned out, I was right. Mom came back.

Things were a little different than I expected.

She’d been waiting in a bus depot sixty miles southeast of Minot, North Dakota. She was told that there were delays. That there were weather problems. That there were engine problems. That there were traffic problems. I said, “For three years?” She said, “Tell me about it. Then she said, “Finally they admitted there was a mix-up with my ticket.” “Your ticket?” I said. “Yes,” she said, “I only got a one-way.” I asked how she got there. She said, “There’s a tunnel system underground that shuttles people out of graveyards when mistakes like these are made that go to this bus depot in North Dakota, and from there you’re supposed to get a ticket back to wherever you came from. But in this case another mistake was made.”

“I knew it!” I said. Mom, I’m just so glad to see you.”

“I’m glad to see you too, sweetheart,” she said. “Is there any mail.”

I tried to explain that everyone on the planet besides me had thought she was dead all this time, thus the lack of mail.

“Well, Christ,” she said, “that’s quite an assumption to make.”

“I know!” I said.

Anyway, the neighbors saw us in the yard and of course they were beside themselves, because unlike me, no one was expecting this. The Marksons next door, whose son I used to babysit, walked over crying hysterically, and seemed confused. Mom tried to explain just as Ginny the religious fanatic from up the street walked by with her dog, screaming at the sight of my mother. She crossed herself and actually fell down on the grass screaming some prayers or something. Later that day we figured it was Ginny who called the local news stations, because suddenly there were half a dozen trucks. My mother invited them in, the reporters, put on a big pot of coffee, and held a press conference in the living room. She explained the whole story about the bus depot and not one of them asked any kind of pressing question about how unbelievable the story was, suddenly everyone seemed to have no questions about what they wanted to institutionalize me for saying not too long before They were like, “Bus depot, underground shuttle, sure.” And she had the death certificate, and she told them if there was any question at all to call the doctors, and the minister who gave her eulogy, and everyone who came to her funeral and saw her in the coffin three years ago looking pretty dead. And they did check that all out and it was all verified although there was curiously no evidence of the bus depot in question or for that matter any other returned-from-the-dead people. But no one questioned that my mother bas back. She obviously was.

Out of all the hoopla came an unexpected bonus as far as my mother was concerned. She became a celebrity. She went on talk shows. She gave interviews. It seemed to extend past the allotted fifteen minutes. And then it happened. My mother got an offer to have her own TV show, a sitcom based on her life/death/return from the bus depot. That’s what they called it, actually. Return from the Depot! Featuring my mom as herself, Lindsay Wagner as Ginny the religious fanatic and Alyssa Milano playing me. I know!

Of course the show was a big hit. At the end of the show’s first season they brought in Alan Thicke for a guest spot and he fell madly in love with Mom right away. It took her all of about three months to agree to marry him. I couldn’t blame her for wanting to be with someone. But I was a little jealous. All that time I’d been waiting for her to come back, I thought we’d get to spend more time together. I had a long time to think about how stupid I’d been so many time, what a waste of time it was, blaming her for everything that was wrong in my life. I thought if she came back I’d be a better daughter. I thought she’d be a better mother. I thought, dying and coming back, especially after being gone so long, it would have to change things. You would just naturally want to make things right.

So I eventually went back to Chicago. Mom would call once every week or so to say hi. But [when] I called Mom from my cell phone, Alan answered. I asked if Mom was there and he said, “Who?” and I said, “Mom, your wife, Mrs. Thicke” and he said, “I don’t know who you are or how you got this number young lady.” So I called her at work, but the woman who answered sounded an awful lot like Mrs. C from Happy Days, and she was pleasant with me but she hung up as soon as she said, “I think you have the wrong number.” I called the Marksons, who said, “Sweetie, we thought you let this go already.” I called Ginny the religious fanatic who said something about “messing with god’s will” and said a Hail Mary and hung up on me. I looked at the TV Guide for the listing for Return from the Depot! And there was a big ad for the show with a picture of Mrs. Cunningham with the rest of the cast, no mention of my mother, and no indication that she was just replaced or something. It seems clear she was never there.

Now, I know what you’re thinking . You’re thinking this is the part where I realize that my mother is not coming back, the part where I snap out of my denial and realize that there will be no big reunion, that she will not send me vitamins or make me chicken soup again when I’m sick. Where I realize that we will never decorate another Christmas tree . . . where I understand that I will never get to show her the home movies from my childhood that Dad put on video that I forgot to bring to Jersey the last time before she died. . . Where I understand that I will never get to tell her that even though she was compete crazy that I would never in a million years want any other mom. . . the part where I realize that I will never get to ask her all the questions I wanted to ask her . . . what was it like for her when Granma died? The part where I understand why my mother wasn’t there to help me get through my mother’s death, because it still make perfect sense to me that anyone would need their mom at a time like that. But it isn’t. I flew to North Dakota. I rented a car and drove to every bus station south of Minot and showed people pictures of my mom. I was pretty close to giving it up just out of exhaustion. Finally, I found a guy who said there had been someone there who looked like her, and I ended up explaining the entire situation. Finally he said, “That’s a sad story. I’m really sorry that happened to you.” And it was hard to tell whether he really believed me or not, but he could obviously tell that I needed someone to believe me, and I’m grateful to him for that.

Mom hasn’t come back again . . . . Yet.
```

---

## IC-2316: Retwisting the Ties that Bind

- Title: Retwisting the Ties that Bind
- Author (byline): Lisa C. Moore
- Work: Souls of My Sisters: Black Women Break Their Silence, Tell Their Stories . .
- Publisher: Dafina Books
- Publication date as stated: Oct 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1571
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lisa C. Moore
Book: Souls of My Sisters: Black Women Break Their
Silence, Tell Their Stories . .
ISBN: 978-1575666532
Publisher: Dafina Books
Date (Month/Year): Oct 2000
```

### Introduction (context only: never use it for content warnings)

```text
You never know what other people are dealing with. You never know how your actions may affect another person. You never know what driving forces were present during someone's childhood or formative years. You never know what deeper thoughts and intentions lurk in someone's heart and mind. Lisa C. Moore knows this better than anyone and in Retwisting the Ties that Bind, she examines these concepts as they relate to the relationship she had and has with her mother. Retwisting the Ties that Bind by Lisa C. Moore.
```

### Performance text (classify this)

```text
I do not trust my mother.

But then, she never trusted hers.

Let me be clear: I love my mother. I love who my mother is finally becoming, a more whole person than she was when I was growing up. Someone who is learning to love herself, who is finally growing up herself.

I love my mother’s mind, how quick and agile and curious and cunning it can be. I love my mother’s tongue, how she turns perfectly innocuous English language into sharp, cutting words aimed at those who do her wrong. I can only wish I was that smart, had such great timing. I’m working on it.

I love how my mother loves to play games – whether they be board games or the big boys’ games – learning the ins and outs of them and becoming masterful. I’m in training to run with the big boys myself, and she takes great delight in that.

I love the elegance of my mother, how she holds her hands, the way she angles her long neck, the way she holds her head high. I admire the fullness of her lips. I think I’ve inherited some of these things.

But what I also seem to have inherited is a mistrust of people. Starting with my mother.

I have just finished a fantastic novel about mother-daughter-mother reincarnation. It made me cry at the end, at the daughter with the grandmother’s memories, coming back to comfort the mother. I wonder at the act of taking a child in one’s arms to comfort. So many women I know talk of their mothers as if their mothers are their best friends. But I can’t recall any instance of being comforted in my mother’s arms. Caged is more the feeling.

What am I missing?

Did she ever feel comforted in her mother’s arms?

Trust comes from unconditional love.

I’ve heard stories about my grandmother. Of how she would yank elbows off the wooden edge during mealtime to teach that rule of the dinner table. She is a witty and elegant woman, and a stickler for manners, rules. I don’t remember ever seeing her take my mother in her arms; physical contact was rare, save for the hello and good-bye hug. I don’t remember her saying anything comforting to my mother at all, actually. When we’d visit, I remember her usual tone as more of a “you deserve what you get.” I always thought it was for marrying beneath her “station in life.”

My mother was not taught to love herself. She was born out of wedlock in a time when such things were a sin, a stain on the child as well as the parents. And when her sister came along later, born within the safety of a marriage, the inevitable comparisons began. This much my mother has told me.

Feeling not quite “as good as,” not “enough,” and certainly never “better than,” how can a little girl learn to love herself? I know these things are passed on.

Trust comes from feeling comfort and stability and reliability. I never turned to my mother for those things. After too much disappointment, I stopped asking early on for rides to school, from school, to anywhere. I learned how to catch the bus, and learned the inherent freedom from asking and not getting. When my mother offered to take me anywhere, I refused. I preferred the bus driver’s schedule – I knew he’d be at the corner at 7:46 a.m. I asked my father for things, because sometimes things promised by my mother – money, clothes, shoes – didn’t come through, and the not coming through was always at the last minute.

Did her mother not follow through on promises? Did her mother promise her anything?

Because my mother had to work to make ends meet, I cleaned house, cooked, braided my sisters’ hair, washed clothes, fed children. My mother tells a story of her father requiring that the bathroom sink be cleaned and dried after every use. She tells me this as if to say, “You don’t have it that bad.”

This story never comforted me.

Did she ever feel comforted? What about her mother, my grandmother? Who comforted her, told her she was loved, taught her to love herself? Who showed her, through consistent behavior, that she could rely on her mother’s words and actions? Who taught her to pass it on – or not? Did she ever learn?

During my years of mothering my sister, I’ve learned you can’t give love if you don’t love yourself first, but my mother was ill equipped for the rigors of parenting. You have to give and give and give, and have enough left over to give to yourself. She didn’t have that. I was lucky; I learned about consistency and reliability from my father.

A respect for boundaries yields trust.

When I was in fifth and sixth grades, I kept a diary. Once some kids in class stole it from my purse and read it aloud to the class, snickering at my attempts at describing my body’s newfound changes. I was devastated, and subsequently kept to myself in school. A few years later, in ninth grade at a new school, I took up a journal again, only to discover my mother was reading it regularly and asking me about certain passages. I gave it up for good then – at least until I was in my late twenties. She said it was the only way she would know what was going on in my head, since I didn’t volunteer information. My mother’s quest for knowledge about her excessively quiet daughter made me dig in my heels, learn to be secretive about private thoughts, phone calls, writing, desires.

Now I’ve learned to relax a little- not be on one extreme or the other. But little things still trigger the mistrust, such as my sister looking through my mail and asking who the sender is, borrowing something without asking, or even just asking. Any semblance of what I consider too much curiosity is cause for alarm.

Did her mother respect her boundaries? Were any set?

Lack of trust yields an incomplete sense of self.

A memory: of talking to my younger teenage sister, who still lived at home, while she detailed the latest hurt from my mother. But my sister reacted, talked back, something I never dared do. I kept repeating, “You said that to her?” And she kept saying, “Yeah! Who does she think she is? I wouldn’t do that to her!” I sat there amazed at my sixteen-year-old sister’s womanish audacity, defying authority.

After I hung up, I had a sudden memory of me being awakened in the middle of the night by my mother. I may have been about ten. She shook me awake, told me to get my ass up, why didn’t I finish cleaning the kitchen, “You left dishes in the sink.” She was tired, and yelling; I was stunned at the vehemence of her words. “I work all day for you, and I come home and can’t even get y’all to keep the house clean! What good are you? HUH?” And I slowly began to walk to the kitchen to wash the offending dishes. I don’t remember crying. I do remember feeling wooden.

But some twenty years later, I have burst into tears, crying at the fact that I never remember feeling angry. And I feel incredibly angry now, angry like my sister did. Questioning, like my sister had. Sad. And thinking, what other parts of my childhood did I lose? How many memories have I blocked because I wasn’t allowed to feel, to express my feelings?

I’m sure my mother has a different memory, if she has one at all.

But my mother has told me her memories of me learning to read at age three. Me crawling out onto the roof of the house as a baby, how scared she had been to come upstairs to check on me in my crib and find that I had crawled out of the window next to the crib and onto the roof.

I try to imagine the terror of a new mother finding her child sitting with a few of New Orleans, with the protective crib sides down. I can’t do it.

There are some good things. Because lack of trust produces an almost paralyzing fear of the unknown – having no control over what’s going to happen – I’ve had to force myself to take great leaps of faith, like publishing a book, starting grad school, moving to new cities where I don’t know a soul, traveling by myself, being comfortable with being alone. Having to depend on me, myself, and I. Learning to love myself. I am learning to trust my intuition.

My mother admires this about me, says she is proud of me, wishes she could do the same.

When will she learn?

I do not trust my mother.

But I am working on building an adult relationship with her, which is what I’m hoping for. It’s a slow process. My instincts run counter to it. The childhood I’m rebuilding for myself doesn’t include her. I am rediscovering emotions I never thought I’d own, like playfulness, anger. But we have learned to dance around my childhood and hers, and are coming to grips with being adult black women who are irrevocably tied to one another.
```

---

## IC-2317: The Screaming Woman

- Title: The Screaming Woman
- Author (byline): Ray Bradbury
- Work: Stories of Ray Bradbury
- Publisher: HarperCollins Publishers, Inc
- Publication date as stated: Jan 1983
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1801
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ray Bradbury
Book: Stories of Ray Bradbury
ISBN: 978-0586054857
Publisher: HarperCollins Publishers, Inc
Date (Month/Year): Jan 1983
```

### Introduction (context only: never use it for content warnings)

```text
The Screaming Woman by Ray Bradbury
```

### Performance text (classify this)

```text
My name is Margaret Leary and I’m ten years old. I’ve got a nice father and mother, except they don’t pay much attention to me. Anyway, we never thought we’d have anything to do with a murdered woman. Or almost.

When you’re just living on a street like we live on, you don’t think awful things are going to happen, like shooting or stabbing or burying people under the ground, practically in your back yard. And when it does happen you don’t believe it. You just go on buttering your toast or baking a cake.

It was noon in the middle of July. I was just walking along, across the empty lot behind our house, when all of a sudden it happened.

I heard the Screaming Woman.

I stopped and listened.

It was coming up out of the ground.

A woman was buried under the rocks and dirt and glass, and she was screaming, all wild and horrible, for someone to dig her out.

Then I started to run. I fell down, got up, and ran some more. I got in the screen door of my house and there was mama.

“Mama . . . There’s a Screaming Woman in the empty lot. . . We got to dig her out. She’s buried under tons and tons of dirt and if we don’t dig her out she’ll choke up and die.”

“I’m certain she can wait until after lunch,” said Mama.

“Mama, don’t you believe me?”

“Of course dear, now wash your hands and take this plate of meat in to your father.”

I went into the dining room “Hi, Dad, there’s a Screaming Woman in the empty lot . . . We’ve got to get picks and shovels and excavate, like for an Egyptian mummy”

“I don’t feel like an archeologist, Margaret.” Said Father. “No, some nice cool October day, I’ll take you up on that.”

“But we can’t wait that long,” I almost screamed. My heart was bursting and here was Dad, putting meat on his plate, cutting and chewing and paying me no attention.

“Dad, you just gotta help. I’ll give you all the money in my piggy bank!”

“Margaret, tell you what . . . after lunch, I’ll come out and listen to your Screaming Woman, free of charge, But you must eat.

Lunch was a million years long. Everybody moved in slow motion, like those films you see at the movies. It was so slow. I wanted to scream, “Hurry! Oh, please!”

But no, I had to sit, and all the while we sat there slowly, slowly eating our lunch, out there in the empty lot (I could hear her screaming in my mind. Scream!) was the Screaming Woman all alone.

“There we are,” said Dad, finished at last.

“Now will you come out to see the Screaming Woman?” I said

“Speaking of the Screaming Woman,” said Mother, “Charlie Nesbitt and his wife Helen had another fight last night”

“That’s nothing new,” said Father. “They’re always fighting.

“If you ask me, Charlie’s no good,” said Mother. “Or her either.”

“Oh, I don’t know,” said Dad. “I think she’s pretty nice.”

“You’re prejudiced. After all, you almost married her.”

“Dad,” I said

“Charlie has got a terrible temper” said Dad.”Remember when Helen had the lead in our high-school play? She wrote some songs for it herself. That was the summer she wrote that song for me. Let’s see, how did it go?” (HUMMING)

“Dad,” I said.

“You’d better take your daughter out in the back lot before she collapses.” said Mother, “You can sing me that wonderful song later.”

The empty lot was still empty and hot and the glass sparkled green and white and brown all around where the bottles lay.

“Now, where’s this Screaming Woman?” laughed Dad.

“Listen,” I said. We listened. “Shhh . . . Wait.” We heard the wind in the trees. That was all.

“Margaret, “ said Father. “ I suggest you go lie down and put a damp cloth on your forehead.”

“But she was here,” I shouted. “I heard her, screaming and screaming and screaming. See, here’s where the ground’s been dug up. I called frantically at the earth. “Hey there, you down there!”

“Margaret,” said Father. This is the place where Mr. Kelly dug yesterday, a big hole, to bury his garbage.”

“But during the night,” I said, “someone else used Mr. Kelly’s burying place to bury a woman. And covered it all over again.”

“Better not stay out here too long,” said Dad. “It’s hot.” Dad walked off.

I stamped on the ground. “Darn.” I said. The screaming started again.

I ran to the garage, got a couple of shovels and ran to the empty lot. I started to dig, and all the while I dug, the Screaming Woman screamed. . . .

It was hard work. I knew I’d be doing it all afternoon and maybe I wouldn’t finish in time. What could I do? Run tell other people. But they’d be like Mom and Dad, pay no attention. I just kept digging, all by myself.

About ten minutes later, Dippy Smith came along the path through the empty lot. He goes to my school.

“Hi, Margaret what are you doing?”

“Digging for the Screaming Lady.”

“I don’t hear no screaming.”

“You wait a while and you will. Still help me dig”

“I don’t dig unless I hear a scream”

We waited. A scream came out of the ground.

“Hot dog! Give me a shovel.”

We kept digging, and then a shadow fell across us.

“Hey, you kids, what you think you’re doing? It was Mr. Kelly, the man who owned the empty lot. “Shovel that soil right back into that hole!”

My heart started beating fast again.

“But Mr. Kelly, there’s a Screaming Woman-”

“I’m not interested. . . . Go on now, fill it up and get home before I give you my foot!”

I turned to Dippy, “He’s the one, and he buried Mrs. Kelly here. There’s only one thing to do . . . call the police.”

We ran for the corner store telephone.

The police knocked on Mr. Kelly’s door five minutes later. Dippy and I hid in the bushes, listening.

“Mr. Kelly?”

“Yes, sir, what can I do for you?”

“Is Mrs. Kelly at home?”

“Yes Sir, Hey Anna!”

Mrs. Kelly came to the door.

“I beg your pardon, but we had a report that you were buried out in an empty lot, Mrs. Kelly”

We both ran.

“What’ll we do now?”

“We don’t dare go near that empty lot again.”

“So long,” said Dippy. I was left all alone, no one to help me. There was only one last thing to do. I went from house to house, all down the street. I rang every bell and when the door opened, I said, “Hello, Mrs. So-and-So, you’re looking fine today.” And once I saw that the lady of the house was home, I went on down the street.

I was about to give up when I knocked on the door of Charlie Nesbitt. Instead of Mrs. Nesbitt, or Helen as my father caller her, coming to the door, why it was Mr. Nesbitt, Charlie, himself.

“Oh,” he said. “it’s you, Margaret. What can I do for you?”

“I’d like to see your wife”

“Well, she’s gone out to the store,” he said.

“I’ll wait,” I said, and slipped in past him. I sat down in a chair. “My, it’s a hot day,” I said, trying to be calm, thinking about the empty lot and air going out of the box and the screams getting weaker and weaker.

“Listen, kid,” said Charlie, coming over to me, “My wife won’t be back. Not today, that is. She’s gone to the store, like I said, but, but, she’s going on from there to visit her mother. Yeah. She’s going to visit her mother, in Schenectady. She’ll be back, two or three days, maybe a week.”

“That’s a shame,” I said. “I wanted to tell her there’s a woman buried over in the empty lot, screaming under tons and tons of dirt.”

Mr. Nesbitt dropped his cigarette. . . .“Well, I’ll tell Helen when she comes home, your story.

“Thanks. It’s a real woman.”

“How do you know it is?”

“I heard her.”

He tried to be casual. “Say kid, you, eh, you say anything about this to anyone?”

“Sure, I told lots of people.”

“Anybody doing anything about it?”

“No, “ I said. “They won’t believe me.”

“He smiled. “Of course. Naturally. You’re nothing but a kid. Why should they listen to you?”

“I’m going back now and dig her out with a spade,” I said. “I got to go.”

“Plenty of time for that,” he said, quite. “Let’s play a game of black jack, it’s more fun than Screaming Women.”

I knew what he was trying to do. He was trying to keep me in his house until the screaming died down and was gone. He was trying to keep me from helping her. I knew what his plan was. He’d sneak down in the middle of the night and dig up his wife, and take her somewhere else and bury her, good. He finally let me go because he thought that by now the air must all be gone from the box.

I went back to the empty lot and hid in some bushes. What could I do? Tell my folks? But they hadn’t believe me. Call the police on Charlie Nesbitt?

But he said his wife as away visiting. Nobody would believe me!

The screaming had stopped. It was so quiet I thought I would never hear a scream again. I bent down and put my ear against the ground.

And then I heard it, way down, way deep, and so faint I could hardly hear it.

The woman wasn’t screaming any more. . She was singing. Something about, “I loved you fair, I loved you well.” It was sort of a sad son. Very faint. And sort of broken.

I walked to my house and opened the front door.

“Father, she’s not screaming anymore. She’s singing now. And she’ll be dead soon if you don’t listen to me. She’s out there there, singing: “I loved you fair, I loved you well. . . ”

Dad’s face grew pale. “Where did you hear that song?” he shouted.

“Out in the empty lot, just now”

“But that’s Helen’s song, the one she wrote, years ago, for me! You can’t know it. Nobody knew it, except Helen and me. I never sang it to anyone. Oh, my God!” cried Father, and ran out the door.

The last I saw of him he was in the empty lot, digging, and lots of other people with him, digging.

I felt so happy. I wanted to cry. I dialed a number on the phone and when Dippy answered I said, “Hi Dippy. Everything’s fine. Everything’s worked out. The Screaming Woman isn’t screaming anymore”
```

---

## IC-2318: The Sea Turtle Hospital

- Title: The Sea Turtle Hospital
- Author (byline): Karen E. Bender
- Work: Refund: Stories, Pg 191
- Publisher: Counterpoint
- Publication date as stated: Nov 2015
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: INTERCOM VOICE, MISS SAMSON, AUNT, KEISHA, SHAWNTE, EMPLOYEE
- Teaser before the introduction: Yes
- Spoken words (computed): 1476
- Already set (do not supply): none

### Source block (context only)

```text
Author: Karen E. Bender
Book: Refund: Stories, Pg 191
ISBN: 978-1619026230
Publisher: Counterpoint
Date (Month/Year): Nov 2015
```

### Introduction (context only: never use it for content warnings)

```text
Trapped . . . For many struggling families in America, the word “trapped” can literally describe every aspect of their lives. Trapped in a cycle of poverty, Trapped by health issues beyond their control. Trapped by drug addiction, by the color of their skin, trapped by the very society in which they live. And for many, this state is multi-generational.

In this selection, a struggling kindergarten teacher realizes that she and her students are very similar to the damaged sea turtles they visit at . . .

The Sea Turtle Hospital by Karen E. Bender.
```

### Performance text (classify this)

```text
INTERCOM VOICE: Lockdown. School is currently in lockdown.

The lockdown at Arthur Elementary was the second at the school this week. Mrs. Reeves told me to lock the door and draw the blinds while she got the better (safer?) job of herding the kids into the reading nook. The school shut down, locking windows and doors, supposedly allowing no one in or out, when there were reports of violence in the neighborhood. The first lockdown of the week happened after a [student] at the nearby junior high stood up during algebra class, brought out a hammer, and started whacking his classmates. And today, there was the brisk, almost office-like pop of gunshots two blocks away. I had worked here for a year and a half, and the lockdown protocol still messed me up, the click of the lock, the brisk, absurd drawing of the blinds, as though the thin plastic provided any protection from anything. The kindergartners crouched, knees to chest, in their uniforms, the blue pants and crisp white collar shirts. They were good at making themselves tiny, even the larger ones.

MISS SAMSON: (trying to sound hopeful about the collective future) Remember to get your permission slips signed for our exciting field trip to the sea turtle hospital next week! Keisha climbed into my lap. We crouched there for ten minutes. Twenty. Thirty. [Then] there was the sound of a woman’s heels. My heart picked up. Principal Williams unlocked the door. By four p.m., the traffic circle was empty and all the children were shipped off to their various hopes and catastrophes. The only one still here was Keisha Jones. She calmly chewed on one of her many dark brown braids.

MISS SAMSON: Who’s picking you up today? Your mom? Your dad? Your aunt? She raised her shoulders and dropped them. We walked back into the office where I called her home.

MISS SAMSON: This is Miss Samson, Keisha’s teacher. She’s still at school. We wondered who was coming to pick her up.

AUNT: Oh. Sorry, I guess it was supposed to be me—”

MISS SAMSON: Is her mother around?

AUNT: She’s on second shift at the hospital.

MISS SAMSON: Is anyone else here who could pick her up?

AUNT: I sprained my foot, miss, and I can’t walk.

There were various heartbreaking excuses, relatives who were assigned pickup but had been arrested, the ones who had fallen asleep in front of the TV, broken down cars . . . but mostly the reason people missed school pickup were dreary—the assigned person was at work. Everyone was always at work. The first job, the second job, etc. and there was another kid sitting there, waiting.

MISS SAMSON: I’ll drive her home. . Keisha jumped up and pumped her fist with joy, as though she’d won a raffle. [See] Keisha had decided I was good. I had done nothing but give her a little attention. We sat and sounded out words together. I see a c-at. The c-at is s-oft. She was the best one in class, my speed reader.

KEISHA: (heavy sigh) I don’t want to go home yet . . . I knew where she lived; it was a brick development that, with its white columns, broken glass on the sidewalk. Groups of men hanging out midday, cars with towels covering broken windows. Some of the kids who lived there ate double breakfasts in the cafeteria because they hadn’t eaten any dinner the night before.

KEISHA: I’m hungry. Really hungry.

MISS SAMSON: Do you want me to pick up some dinner? It’ll just take a sec.

KEISHA: Sure! Yes! I pulled into the first eatery I saw, and we piled out. The register worker, whose nametag said Shawnte, [was] a young woman with gold metallic eye shadow.

SHAWNTE: (suspiciously) Keisha! Who you with?

KEISHA: This is my teacher.

MISS SAMSON: I’m giving her a ride home.

KEISHA: My momma’s working and my aunt hurt her foot, and everyone was working but my teacher took me home . . . .I want the junior thickburger with onion rings and a strawberry shake! Keisha pulled one, two, three napkins out of the dispenser, spread them into a sort of tablecloth on the plastic table.

MISS SAMSON: How do you know Shawnte?

KEISHA: She dated my brother.

SHAWNTE: Here we are. Shawnte, set the burger in front of Keisha, who grabbed [it] and started wolfing it down.

SHAWNTE: How’s your dad?

KEISHA: (in between bites) He went to a hotel. When he started talking really fast.

MISS SAMSON: (gesturing for a private conversation) What happened?

SHAWNTE: (whispering) Schizo or something. No insurance, no meds. Couple days ago, he broke the TV. I looked at Keisha, finishing the onion rings, and I imagined. [Then] she sat on my lap while I read a book: Sea Turtles

MISS SAMSON: Turtles lay about 120 eggs in a nest. After hatchlings come out, they head to the sea. Only a lucky few survive. The pictures showed the turtles swimming. They looked like people who had not quite become people, but were trying, floating, with their tiny almost-arms.

KEISHA: I want to see one. (adamantly) Now. Please! I want to see something new. She looked at me, expectantly. The sea turtle hospital was about twenty minutes from here. I was a kindergarten teacher. I knew nothing—that much I had learned these last few months. [But] her belief was a gift.

MISS SAMSON: Hon, me too. I was now a teacher on a mission; I was going to show her the sea turtles, something miraculous and new. I thought, I should not be taking her on a field trip at 6:30, I should call her aunt and tell her where we were, and I felt a flutter of panic that I had not just driven her home. I was about to call her aunt and tell her not to worry. [But] I thought, I am a part of this, I am a part of Keisha’s life— My hands trembled on the steering wheel; I didn’t want to be wrong or unreasonable, but I wanted her to see the sea turtle. The sea turtle hospital was a single room that held about ten enormous bathtubs. There was a chart marked PATIENTS on the wall. It featured a list of unlikely turtle names, such as BING, MAXINE, and HUGH. There was Bing, who had a hook stuck in his ear, [and] Maxine, who had run into a fishing boat and seemed perpetually shocked as she floated in her tub, staring at us with her unblinking black eyes.

EMPLOYEE: Our goal is to release them back to the sea. It’s the greatest feeling . . . When you know it’s where it needs to be, when it pushes the water with its flippers… Keisha gazed at Melissa with interest. It was as though the girl was trying to interpret what the woman was really saying about the world.

KEISHA: Can I touch? She walked us to the largest tank, where a turtle swam around. He kept bumping into the sides, turning, swimming and bumping again.

EMPLOYEE: (looking as though she were about to cry) Hugh’s in good health, but he’s blind. He was caught in a fishing net and a fisherman banged him on the head so hard he can’t see. Turtles can live over a hundred years. his is where he needs to live for his whole life.

KEISHA: This wasn’t in my book. Save him. He needs a better tub! A bigger one. So he doesn’t bump his head! (begins to cry, she kicks the ground hard)

MISS SAMSON: (in a firm teacher’s voice she takes Keisha’s hand and leads here away) Let’s go. She broke away from me and ran out the door into the parking lot. Keisha ran from the sea turtle hospital, and she could have kept going, through the parking lot, my god, onto the road, but she didn’t; she stopped. When I reached her, she was crying, breathing hard. I knelt in front of her and grabbed her hands. This was not what I wanted to happen, not the happy, triumphant girl I had imagined bringing to her front door; I had wanted her to have seen something good.

MISS SAMSON: (softly) It’s okay . . . It’s okay—

KEISHA: (taking a large gulp of air as her sobs subside) Tell me . . . Tell me what kind of tub he should get. [And so] I told her . . . big, a mile long, with slides in places to make it fun. It would have special pools with rocks. Maybe there could be other nice turtles in there that would be his friends.

KEISHA: Maybe a smart doctor might invent special drops that could cure his blindness and then Hugh could paddle out to sea.

MISS SAMSON: Maybe we would all gather at the shore and watch him swim out, with his perfect new vision. He will remember how to swim, and he will float into the blue, deep water.

KEISHA: Floating . . . He would like that. She nodded. The sky above us was so dark and seemed weighted, as though holding back something invisible and enormous. I knelt in the crumbling asphalt while her small hands gripped mine and I waited for her. And then she got back into the car and I drove her home. It was 7:50 p.m. when I pulled to the curb of Keisha’s apartment. Keisha waited for me to come around the car and grabbed my hand, and we started walking toward Apartment 3A. (Long pause) Lockdown . . . currently in Lockdown.
```

---

## IC-2319: Secret Girl

- Title: Secret Girl
- Author (byline): Molly Bruce Jacobs
- Work: Not specified
- Publisher: St. Martin's Griffin
- Publication date as stated: Feb 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1335
- Already set (do not supply): none

### Source block (context only)

```text
Author: Molly Bruce Jacobs
ISBN: 978-0312364069
Publisher: St. Martin's Griffin
Date (Month/Year): Feb 2007
```

### Introduction (context only: never use it for content warnings)

```text
Secret Girl is the memoir of Molly Bruce Jacobs, attorney-turned-alcoholic who at age 38 first meets her sister, Anne, age 35. Anne was the family secret. Institutionalized at birth for hydrocephalus, she was supposed to die. Instead, she made such great progress her doctors wanted to discharge her. But Anne's blue-blood parents wouldn't hear of it, and ignored the repeated pleas to bring their daughter home.

In this selection "Brucie" Jacobs learns she has a secret sister for the first time. It is one of those extraordinary moments when you realize that your family history is a lie and you're forced to retrace your memories and re-evaluate their meaning. Secret Girl by Molly Bruce Jacobs.
```

### Performance text (classify this)

```text
"What would you say if I told you that you have another sister?" my father asks Laura and me.

It is 1967. I am thirteen, Laura is ten. We are staying overnight at a motel somewhere in California's Death Valley. On summer vacation, we've just driven from San Francisco and will spend about a month driving home cross- country, visiting the Great Salt Lake, the Grand Canyon, a dude ranch in Montana, and other places I imagine would thrill most any child.

My parents and Laura and I have almost finished dinner in the motel restaurant. Tired after being in the car all day, my mind is swirling with images of the desert. From the car, basins of sand surround us beneath the hot iron of sun. My mouth watering for a cold Coke, and in between bouts of my hogging the Barbies and leaving Laura one of those flat-staring Ken dolls, as much fun to play with as an ice pick, I watch the mirages that glisten and steam off the ribbon of road sizzling ahead. Every now and then, my eyes fasten on the desert's huge greenish gray cacti that sprout pale pink blossoms from thorny tendrils. I wonder how such a prickly plant could grow such delicate, soft things.

But what I will remember most clearly about this drive is the stifling heat. Relentless, it hangs heavy in the air. The station wagon we rented in San Francisco -- like most cars back then -- has no air-conditioning.

"Open your window, Brad," insists my mother, fanning her face with her hands. "Girls, you too."

But Laura and I ignore her. Dice has already explained we're better off with the windows closed, and Laura and I still believe that his judgment is infallible. "You'll only be letting more heat in," Dice tells my mother again, more firmly this time.

When finally in the late afternoon we stop at the motel, Laura and I clamber out of the backseat and race to the pool. We beg Dice to take us swimming before dinner -- which he does, while our mother settles into a chair by the pool to read one of the library books she has brought on the trip.

Now Dice's question hovers above our small round table like some strange desert bird bewildered among the plastic potted plants. This is one of Dice's jokes, I think, glancing over at him to read his expression. But no, he's serious, I sense at once. I see it in the steady, concentrated look of his green eyes which are fixed on nothing in particular -- just the air in front of him -- in the scissorlike rigidity of his fingers holding the cigarette he has just lit, and in the grave set to his lips. What could he mean? What is he getting at?

I sneak a look over at Laura, but all her attention is on Dice. Staring at him, her small, round face has a dumbfounded, wide-eyed look of astonishment. She's waiting for him to say more, too.

As for my mother, for an eyelash of a second, a mixture of fear, sorrow, and something bitter flits across her face. Her complexion, usually reddish (from high blood pressure, I will learn later), is paling into a washed-out shade of gray, while her lips, neatly polished, are pressed together tight as two church doors. Her eyes on the white tablecloth in front of her as if she's studying some intricate pattern visible only to her, she doesn't look up.

Sensing that Dice is waiting for one of us to say something, I grope for words. Almost anything will do, I tell myself.

But before I can think of what to say, the waitress brings four white bowls full of green Jell-O topped with cold whipped cream for dessert, tea for my mother, and coffee for Dice. While the waitress busies herself about the table, the silence grows unbearably awkward. Either Laura or I, I don't remember who, finally blurts out something like, "What do you mean ... a sister?"

Dice waits until the waitress has left before he answers.

And then the shock comes.

"Well, you do have another sister, girls," he says, crossing one leg over the other, and sucking smoke into his lungs. As if bracing himself to go on, he leans back in his chair and clears his throat. "She's mentally retarded. She was born with a disease called water-on-the-head."

I try hard not to show it, but I am stunned. I'm not sure what has jolted me more, the news that I have another sister, or that she is mentally retarded. Both are unfathomable to my thirteen-year-old brain.

Dice is speaking again, and glancing at Laura. "She's your twin, Laura. Her name is Anne."

Laura stiffens as if she's been stung and opens her mouth to say something. But no words come out.

Poor Laura, I think to myself, this must be weirder for her than it is for me. She's got a retarded *twin.* Is Laura going to get water-on-the-head someday, too?

Dice goes on, and, in a methodical tone of voice, gives us the bare outlines of Anne's story. She lives with other retarded children in a hospital, he tells us. "But she's happy. She's better off there with her own kind than at home." I hear him say this several times that night, and I wonder why he is repeating it.

When Dice finishes, his words don't feel real. How could we have another sister? Where is she? And what does she do all day? Can she talk? Walk? What is it like to be retarded? Why didn't he tell us about her earlier; why *now* while we're on vacation? Did Mummy know he was going to tell us? Does Nanny know about her? But tonight, instead of asking the questions tearing through my mind, I keep a grown-up, solemn look on my face, and pretend not to care.

Laura, silent, looks bewildered, while my mother, the tension in her body unmistakable, is still staring at the table as if she's in another world. I, too, feel speechless. Still, the strain of emotion in the air is like water slowly rising all around us. Hoping to dilute it with an innocuous question, I ask where the hospital is, and what its name is.

Dice's answer gives me another shock. I hear him say in a matter-of-fact tone that Anne lives at Rosewood. It can't be, I think, horrified. Rosewood is just around the corner from Garrison Forest, the private girls' school where I'm now in seventh grade. Every once in a while, my carpool goes by Rosewood, and one or another of my friends in the car makes some crack about the "retards" who live there. I've never hesitated to join the laughter that follows. At times, I've even initiated a cruel remark or two. Now I silently swear that I won't say anything bad about retarded people ever again.

Still, images of Anne haunt me that night, keeping me awake. Every time I close my eyes, I see a grotesque creature with a head the size of a watermelon, her cowlike breasts the picture of obscenity. She's tucked away in the back of a closet as if she were something less than human. But the girl in the closet is screaming, shrieking in my thoughts for help; if anyone hears, they pay her no attention.

Laura, beside me in the huge double bed, is snoring lightly. Though tempted to wake her, I don't. We hardly spoke after dinner -- stunned and exhausted, we fell straight into bed. It doesn't occur to me to seek comfort from my parents in the adjoining room. Only if I were sick would I even consider disturbing them at night. I hug my knees tight to my chest and close my eyes to shut out the images of Anne, but the sound of a little girl's crying won't go away.
```

---

## IC-2320: A Series of Helpful Post-it Notes I Left Around the House for My Husband This Week

- Title: A Series of Helpful Post-it Notes I Left Around the House for My Husband This Week
- Author (byline): Jenny Lawson
- Work: Let’s Pretend This Never Happened: A Mostly True Memoir
- Publisher: Berkley
- Publication date as stated: March 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1231
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jenny Lawson
Book: Let’s Pretend This Never Happened: A Mostly
True Memoir
ISBN: 978-0425261019
Publisher: Berkley
Date (Month/Year): March 2013
```

### Introduction (context only: never use it for content warnings)

```text
Okay, so I was looking for relationship ideas and I came across a website that suggested leaving post-it notes with special little messages for your spouse, just (air quotes) “to let him know that you are thinking of him.” What I wonderful idea! We are both so busy we often don’t have time to sit down and talk to each other. So I rifled through the junk drawer and found a nice pad of post-it notes . . . let the relationship-building begin!!

A Series of Helpful Post-it Notes I Left Around the House for My Husband This Week . . . from Let’s Pretend This Never Happened by Jenny Lawson
```

### Performance text (classify this)

```text
Dear Victor: This bath towel was wet and you left it on the floor and it was the last clean one in the house. I’m pretty sure this is how tuberculosis is spread. I’m writing all this in my blog in case I end up dead because of your carelessness.

Dear Victor: There is a pile of business suits for the dry cleaner’s that have been in the closet for five months. You work from home. [WTF?], Victor?

Dear Victor: Why is cleaning up cat vomit always my job? Was I not here when we picked from the job jar? Is there a job jar at all? Because I’d like to redraw. Also, I’m aware that you always have to clean out the litter box, but that’s because at any moment my IUD could fail and I could accidentally get pregnant and then get that cat-poop pregnancy disease, and our baby would be born with no arms or legs. Is that what you want, Victor? For our baby not to have arms? You are so selfish.

Dear Victor: You make me sick. Why in God’s name wouldn’t you just throw away the empty pizza box when you were done with it? Are your arms broken? Do you have some sort of disease I don’t know about that makes you blind to empty pizza boxes?

Dear Victor: Okay, I just remembered I was the last one to make pizza, so I guess I left this box out. Still, I’m leaving out the note anyway so you can learn from it. Bad, bad Victor.

Dear Victor: I do not appreciate your leaving passive-aggressive addendums to my helpful Post-it notes. In fact, they are the opposite of helpful. They are just bitter.

Dear Victor: If you leave wet towels on the ground again I will stab you.

Dear Victor: You can’t take clothes out of the dryer without telling me and just dump them on the bed in a heap. When I find them they’ve usually cooled off, and then I have to put them all back in the dryer with a cup of water, and then rerun the dryer so all the wrinkles come out, and then sneak each article of clothing out one at a time and hang it up. It’s called “a method,” Victor. Stop judging me.

Dear Victor: No, actually, I don’t know how to use an iron. Because we don’t own one. How have you never noticed this before?! The dryer is our iron, Victor. Also, I would appreciate it if you would talk to me directly instead of yelling at me on a Post-it. These Post-its are for educational purposes. Not to draw lewd caricatures of hands pointing menacingly at me. Also, you’re supposed to point with your index finger. This is basic pointing etiquette.

Dear Victor: I’ve poisoned something in the fridge. Good luck with that.

Dear Victor: I’m sorry. I think I might have PMS. I don’t know what’s wrong with me.

Dear Victor: That was an apology, you a**h***! Now there are two things poisoned in the fridge. Because you don’t know how to accept an apology.

Dear Victor: I am so sorry you are sick. I swear I was just kidding about poisoning s*** in the fridge. I mean, I did leave the yogurt out for, like, a half a day, but that was really more by accident because I was so distracted by the wet towel on the floor. If anything, you brought this on yourself. Once again, I apologize.

Dear Victor: I love you but I’m getting kind of weak from hunger, and I know you said you didn’t poison anything, but every time I take a bite of something you leer and laugh suspiciously and I have to spit it out. I can only assume this is probably how Gandhi felt when he wasn’t allowed to eat. (Here’s a hint: He felt stabby.)

Dear Victor: Okay, first of all, you don’t know that Gandhi went on a hunger strike on purpose. For all we know he was avoiding poisoning too. The people who survive are the ones who write the history, Victor. Not the people who die of hunger because their husbands may or may not have poisoned all the food in the house. Except guess what? This is all going on my blog, so I can document this in case people find my emaciated body later and demand justice. There will be a reckoning and it will be brutal and swift.

Dear Victor: Great. Now we’re out of Post-its. I’m writing this on the towel you left on the ground this morning, since we obviously have no respect for towels anymore. I’m going to the grocery store for more Post-its, and I’m going to eat unpoisoned Triscuits straight out of the box while I’m there, so I will return fresh and renewed. Also, the cat vomited in the hall and I am not cleaning it up. I have had enough, Victor. And so has the cat. Whom I’m assuming you poisoned.

Dear Victor: The cat and I are leaving you. You can have the dog. Also, I’ve decided not to go get Post-it notes after all, because I’m no longer speaking with you, so I’m just writing this on your hand towel. You will never hear from me again.

Dear Victor: The dog started whining when I told him he had to stay with you, so I’m taking him too.

Dear Victor: Yes, actually I was holding a bag of dog treats when I told him he had to stay with you, but I don’t think that had anything to do with his reaction. Also, we’re running out of dish towels, so this will be my last message to you.

Dear Victor: Okay. Fine. You can have the dog. I tried to put him in the car and he peed on me. You two deserve each other. I am writing this on the dog because it seemed fitting. Also I couldn’t find packing peanuts for the booze, so I just drank it all. YOU WILL MISS ME SO MUCH ONCE I’M SOBER ENOUGH TO WAKE UP AND DRIVE AWAY.

Dear Victor: Wow. That . . . really got out of hand. I’m sending this cat in as a peace offering. I forgive you for all the stuff you wrote on the walls about my sister, and I’m going to just ignore all the stuff you wrote about my “giant ass” (turn cat over for rest) because I love you and you need me. Who else loves you enough to send you notes written on cats? Nobody, that’s who. Also, I stapled a picture of us from our wedding day to the cat’s left leg. Don’t we look happy? We can be that way again. Just stop leaving wet towels on the floor. That’s all I ask. I’m low-maintenance that way. Also, this cat needs to go on a diet. I shouldn’t be able to write this much on a cat and still have room left over.

Epilogue: Victor forgave me and we all lived happily ever after, except for the cat, who had to have his leg amputated, but that was less from the infection and more from his poor circulation because he was so fat. He kind of brought it on himself too. But now he’s less fat. By, like, a whole leg.

(Disclaimer: Most of this was exaggerated, except for the part where Victor left a wet towel on the floor. That totally happened. I’m still working through it.)
```
