# Classification request: batch 7 of 63 (40 records, IC-0241 to IC-0280)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-007-reply.json`.

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

## IC-0241: Pretty Fire

- Title: Pretty Fire
- Author (byline): Charlayne Woodward
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Jan 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARLAYNE, MOM, ALLIE, MAN, MAN 2, GRANDMOTHER, CHILD 1, CHILD 2, CHILD 3, GRANDFATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1211
- Already set (do not supply): none

### Source block (context only)

```text
Author: Charlayne Woodward
ISBN: 978-0822219422
Publisher: Dramatists Play Service
Date (Month/Year): Jan 2003
```

### Introduction (context only: never use it for content warnings)

```text
It was a carefree world of children, imagining a future with endless possibilities . . . but Charlayne and her sister must learn why they're different from the white, pop-cultural icons like Shirley Temple and Aunt Jemima. Let me show you all the glorious paradoxes of childhood summers with grandparents in the Jim Crow South. Nostalgic memories of an all-black neighborhood full of sensual delights -- from squishy red Georgia clay to the cries of seafood peddlers . . . all is perfect through childhood eyes until we are forced to see the pain, hostility and the “pretty fire” of adversity lying just beneath the surface.

Pretty Fire by Charlayne Woodward
```

### Performance text (classify this)

```text
CHARLAYNE: One day, when Allie and I were watching old black and white movies, Mommy walked into the living room and turned off the TV. She said,

MOM: Ladies, tell me, what would you like to be when you grow up?

CHARLAYNE: (raising her hand) Me first, Mommy, me first. I want to be . . . Shirley Temple. Yes, Mommy . . . I need to be Shirley Temple! Oh, Mommy, I want to live in a big white marble house with a huge spiral staircase that goes all the way up to heaven! And I will stand at the top of this staircase, right next to my happy negro butler! All dressed up in tux and tails and clean white gloves! And together we will come tap-dancing down the staircase . . . (singing and tap-dancing) Shabalabala! Shabalabala! I wish to live in a land of cotton, Old times there are never forgotten, Look away, look away, look away Dixieland.

(finishes with a flourish and freezes in a minstrel pose) Then Allie broke in

ALLIE: (raising her hand) Mommy, I want to be the happy negro maid, Mommy! Oh, Mommy! I want to be in charge of everything! Especially the big, wonderful kitchen, Mommy, and I will thaw out all the turkeys and all the hams, and I will bake them up and serve them out on the veranda to . . . (serving an audience member) the Colonel . . . and . . . (serving Charlayne) to my sister . . . Shirley Temple!

CHARLAYNE: (singing and tap dancing) In Dixie land I’ll take my stand To live and die in Dixie . . .

CHARLAYNE: We loved “Dixie” . . . because “Dixie” meant the South. And the South meant our grandparents -- Grace Harris and Joe Harris. They lived in Dixie. As a matter of fact, in my neighborhood, everybody’s grandparents lived in Dixie! When summertime came, nobody cared about which camp you were going to. Day camp . . . Overnight camp . . . please! The subject never even came up. As far as we were concerned, we were all going down to Dixie, where our grandparents spoiled us silly! As far as we were concerned, Dixie meant Freedom!

Daddy would drive that black Ford over those red clay road and pull up right in front of Grandmama’s yard. Grandmama and Granddaddy would be up on the front porch, waving and throwing kisses. Allie and I’d rip ourselves out of the car and they would come down those stairs and smother us with hugs and kisses and I just knew . . . this was gonna be a summer of love!

My parents only stayed in Dixie for one week because there was this man in Dixie that my mother didn’t like.

MOM: (troubled, angry) I tell you, Woody. I can’t take this. I’m not used to this anymore. I tell you. I just can’t stand Jim Crow!

CHARLAYNE: So after a week Daddy drove Mommy back to Albany. Then we had our grandparents all to ourselves, for the whole summer. I tell you, everything was different in Dixie! People had different jobs in Dixie! Wonderful jobs. Jobs like . . . picking beans and picking corn and picking cotton. Yes! And if you didn’t want to pick your own food, the food came to you. There was this man that drove a big green truck.

MAN: (driving, singing out) Okra! Pecans! Watermelon! Okra! Pecan! Watermelon!

CHARLAYNE: Then, there was this wee, little man who wore a big straw hat that fell over his eyes. He came pushing a heavy cart.

MAN 2: (pushing cart along) Crabs, lobster, shimps! I got your shimps here! Crabs, lobster, shimps! I got your shimps here!

CHARLAYNE: All of a sudden, in the middle of a bright, sunny day, the whole sky would just open up and buckets and buckets of rain would pour down on us . . . while the sun was still shining. My grandmother would let us play in this rain . . . barefoot! And the red clay road in front of Grandmamma’s house turned into red clay mud. Do you know how it feels like to have some red clay mud squishing in between your toes? Heaven!

I tell you, my grandmother was our hero! She was afraid of nothing! She would sit us on the front porch and teach us “life lessons.”

GRANDMOTHER: (Grace Harris, a tall, dignified woman with a strong voice, paces back and forth) Never let anybody have the last word if you know you right! Okay, repeat after me.

(Grandmother’s voice turns into Charlayne’s voice at the / ) Never let anybody have the last word / if you are right.

CHARLAYNE: I tell you, my grandmother was our hero. She was afraid of nothing!

One evening just before dark, we were all outside playing in the road. The next thing we knew, parents and grandparents were grabbing children left and right, and whisking them off into their houses.

CHILD 1: What’s the matter?

CHILD 2: What did we do?!

CHILD 3: I’m sorry.

CHARLAYNE: Allie and I din’t know what to do, so we just went and stood up under that pecan tree across the road from Grandmamma’s house. Soon, Grandmamma came out on her porch looking for us. (waving and calling out) Over here, Grandmamma! We’re over here!

Grandmamma ran down those steps, raced across that road, grabbed us both by the arms, pulled us into the house, and threw us up against the wall, under the windowsill. (to Grandmother) What’s the matter, Grandmamma? What did we do?

GRANDMOTHER: Sssssh! Pray!

CHARLAYNE: But what are we praying for?

GRANDMOTHER: Ssssh! I said pray now!

CHARLAYNE: Granddaddy was seated right in front of us, in his rocking chair, facing the window. He had his glasses on, his Bible open on his lap, and he was praying.

GRANDFATHER: The Lord is my Shepard, I shall not want. He maketh me to lie down in green pastures; he leadeth me beside the still waters. He restoreth my soul . . . Yea, though I walk through the valley of the shadow of death, I will fear no evil. . .

CHARLAYNE: Grandmamma was sitting just in back of Granddaddy, against the opposite wall, but on the floor, just like us, facing us. We all just sat there as it got darker and darker. Soon, night replaced the day.

We just sat there until it was pitch black! And then I heard it: WHOOOOOOOOOOSH! (excited) Then we saw them flickering, flickering, in Granddaddy’s glasses. Allie and I had to peek out that window. (turns around, kneeling) Only our eyes, only our eyes . . . above that windowsill! And there it was! Not two, like in Granddaddy’s glasses, but one great big Jesus Christ cross! Flaming! Burning in the black night! (arms outstretched; awestruck she speaks to the cross) Beautiful . . . . ! Pretty fire . . .! Pretty fire . . . ! (applauds softly)

Suddenly, my grandmother came from nowhere. She yanked us around and shoved us back up against that wall. She looked right into our faces and said . . .

GRANDMOTHER: That is not pretty! That is ugly! That is the ugliest thing you will ever see!

(pause)

CHARLAYNE: I looked into my grandmother’s face . . . filled with fire . . . and for the first time in my life, I saw . . . that Grandmamma was afraid (pause) She sat there with us all through the night as we watched that cross burn. (long pause) But everything was different this morning. All through breakfast, nobody spoke. Not one word.

When breakfast was over, Allie and I went out on the front porch and we looked up and down that road . . . Not a soul was out. (pause) We walked down that red clay road. Down to the bottom, down past Miss. Minnie’s, to the ditch. (notices the charred cross)

And there it was. It was . . . big. Oh, it was much bigger than it looked from Grandmamma’s window. And it was . . . black . . . with charcoals stuck to it all the way to the top. And . . . it had a horrible smell . . . Grandmamma was right . . . It was ugly. (sings in a painful angry dirge)

I wish to live in a land of cotton, Old times there are never forgotten, Look away, look away, look away, Dixieland.
```

---

## IC-0242: Pride and Joy

- Title: Pride and Joy
- Author (byline): Paul Rudnick
- Work: The New Century
- Publisher: Dramatists Play Service
- Publication date as stated: Feb 2009
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: HELENE
- Teaser before the introduction: Yes
- Spoken words (computed): 1364
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Rudnick
Book: The New Century
ISBN: 978-0822223153
Publisher: Dramatists Play Service
Date (Month/Year): Feb 2009
```

### Introduction (context only: never use it for content warnings)

```text
Pride and Joy by Paul Rudnick
```

### Performance text (classify this)

```text
Lights up on Helene Nadler, an attractive Long Island matron. Helene is smartly dressed and accessorized; she's a proud, intelligent, well-spoken woman. She can be gracious, charming and, when necessary, enraged. She speaks to the audience.

HELENE: (Pgs 9-16) Good evening. Hi. My name is Helene Nadler, and if I seem a little nervous, it's because this is my very first time here at a meeting of the Massapequa chapter of the Parents of Lesbians, Gays, Bisexuals, the Transgendered, the Questioning, the Curious, the Creatively Concerned and Others. Of Color. With Colds. No, I'm sorry, I'm kidding, maybe we should just call this group, "Why Jimmy Has No Friends." I'm kidding! Because we are all proud, because we are all special. And I am here to tell you, to prove to you, that I am the most accepting, the most tolerant, and the most loving mother of all time. Bar none. You hear me?

HELENE: Oh, I know what you're thinking, each and every one of you, you're thinking your child was different, your little bubbe went through tough times, your little sweetheart was a total nightmare and you were still warm and nonjudgmental and loving and hugging and giving them self-esteem – well . . . You are nothing. And you will bow down! (Pulling herself together.)

I'm sorry. It's just, well, you'll see. What I've been through. It all started ten years ago, with my eldest child, my daughter, Leslie. "Leslie" - what was I thinking? She was twenty-two, she said, "Mother" - so I knew it wasn't happy talk, "Mother, I have something to tell you. I'm a lesbian." And I took a deep breath and I said, Leslie - look at yourself You're a professional tennis player, you have two cats, named Alice and Mrs. Dalloway, you live with a female social worker and you have the same haircut as a twelve-year-old Amish boy. Of course you're a lesbian. I've been telling you that for years. Helen Keller would know you were a lesbian, from the stubble.

And she was so happy, she said, so you don't hate me? And I said, of course I hate you, but not because you're a lesbian.

I hate you because you're so boring. Why can't you be like Melissa Etheridge or Ellen Degeneres, okay, it's always pants, but at least they're Prada. They're cute! They're fun! And we're both thrilled, because it's all out in the open, we're free, we're clean, well, not their apartment. I said, girls, what is that aroma, kitty litter and patchouli? Is that some new Glade spray, Country Fresh Lesbian? Jodie Foster Number Five? But I don't care, I still visit, I sit on their couch, because I am the most loving mother of all time! Wait.

One year later, my middle child, my son, Ronnie, he comes to me. "Ronnie" - do I learn? And he says, Mom, I have something to tell you. And I say, you're gay, it's swell, no problem, Angels, Elton John, Will and Grace - I loved that show, it was adorable, it was like if Pottery Barn sold people. But Ronnie says, no, it's not that. He says, I was born into the wrong body. And I say, so was I, it's called Atkins, get over it. And he says, no, I was born into the wrong gender. I was meant to be a woman. And I have to sit down. I mean, Ronnie is six three with a beer gut and hairline problems, and all I'm thinking is, Ronnie, which woman? Ed Asner? And he says, Mom, can you imagine what it's like, always feeling so uncomfortable, so totally out of place, he says, Mom, think how you felt when we had to spend Passover with Daddy's family, in New Jersey, and I say, Ronnie, chop it off! If you want a vagina, here's the Visa!

So a year later, I'm riding high, I'm thinking, look at my beautiful family, there's Leslie and Marsha, that's her partner, they announced it in the Times, did you see the photo? "Dennis the Menace Marries Opie." And they're having a baby. They wanted to make sure it was multicultural, so at the sperm bank they requested Vietnamese, Jamaican or Nigerian, I said, great, they can just attach the sperm to the menus and slide it under the door. But I'm thrilled for them, and in comes Ronnie, excuse me, Veronica, in her pale yellow ruffles and her pearls, and I just think - she's lovely. And I'm so proud of her. And where do you find a wrap skirt in that size? And then she says, and Mom, I want you to meet someone, my girlfriend, Renee. And in walks this pretty little thing, she's a flight attendant on United, and I say, excuse me, and Veronica says, and I'm also a lesbian. And I pause and I say, Ronnie, didn't you take the long way around? And she, see, I said she, she says, no, when I was a man, I could never enjoy sex with a woman, but now that I'm a woman, I think it's the most beautiful experience ever. And I'm thinking, Jesus Christ, for what we spent on hormones, I could've had a new kitchen. And Marsha starts eyeballing Renee and Veronica's getting all huffy, and Leslie's got morning sickness, and I'm about to jump out the window but I go to the powder room, I splash some water on my temples and I say, Helene - you can do this. You are the most incredible, loving mother on earth, you can go for the gold, for the platinum, and I burst back into the room and I say, you are all so wonderful and so special. And Leslie touches my hand. And I think, so many people's children, they hide everything. They live separate, secret lives. They're like strangers. I love those children.

And that night, after everyone leaves, I turned to my husband and I said, Morris, I gave birth to perfect children - what did you do to them? And he said, they're still perfect, and I said, sure, if we're making a documentary. What should we call it - Guess What's Coming to Dinner? Hide Your Pets? And he said, don't drive yourself crazy, and I said, but they're our children, doesn't it bother you? And he says, not one bit, and I ask, but why not? And he says, because whenever they come over, I just turn off my hearing aid. And I said, oh my God, and he asks, but who's that big girl, the one who looks like Ronnie?

And he said, come to bed, but I couldn't sleep, and then it's three A.M. and I fell to my knees and I cry out to God! I say, why me? I go to temple, I pay my taxes, our housekeeper has health insurance, and probably my best diamond earrings! And then I felt ashamed, I felt hopelessly conventional, but goddamnit, I still wanted an answer! And then, just as I was finishing my third all-butter French crumbcake, I had - a vision. Sugar shock, maybe, carb coma, fine - but there she was! An Asian woman, a Chinese, in the little black outfit, standing right near my breakfront. And she said, I am the mother of Chang and Eng, the famous Siamese twins.

And the mother, she says, when my boys were born, I also cried out. I said, why are my children so different, so odd, so - hard to shop for? And I wanted to comfort her, can you imagine, Siamese twins? All I kept thinking about was -long car trips. And the twins are in the backseat and they're fighting, he touched me, he called me a name - and you can't separate them. But the mother, she said, when my babies were born, I looked at them wriggling in their cradle, like paper dolls made of flesh, and through my heartache, a thought arose - at least, they will never be alone. And I thought to myself, I thought of my children, with all of their mishegas, maybe all they're doing is finding very individual, very new, and very irritating ways - not to be lonely.
```

---

## IC-0243: Prima Facie

- Title: Prima Facie
- Author (byline): Suzie Miller
- Work: Not specified
- Publisher: Nick Hern Books
- Publication date as stated: Oct 2022
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: TESSA, DEAN, JULIAN, PROSECUTOR, JENNA
- Teaser before the introduction: Yes
- Spoken words (computed): 2079
- Already set (do not supply): none

### Source block (context only)

```text
Author: Suzie Miller
ISBN: 978-1839040641
Publisher: Nick Hern Books
Date (Month/Year): Oct 2022
```

### Introduction (context only: never use it for content warnings)

```text
Tessa Ensler loves her job – fighting to defend those pleading not guilty. Gaining freedom for men accused of rape and sexual assault. Innocence until proven guilty is, after all, the bedrock of a civilized society. But when Tessa is raped by a coworker, she is forced to confront the stark reality that the law was not written for victims, and that she is the one on trial.

Prima Facie by Suzie Miller
```

### Performance text (classify this)

```text
In the police station the morning after the rape.

TESSA: (Scene 9) I’m led into an interview room. I’ve only ever seen video footage of rooms like this one. Watching a client’s interrogation while sitting with my feet on the desk in chambers. All my sass and outrage at the police tricks played. It’s different when you’re in here. I’m cold, shivering. I want to ask for a woman, I need to. But I just want to get it over with. (The questions start; we hear only Tessa’s answers)

Tessa Jane Ensler. (beat) I wanted to report – Because I think – Because I WAS… Something happened. To me. I was sexually assaulted. And I want to – (beat) Julian Brookes. (beat) No, we work together. (beat) I don’t know, about five years. (beat) Um. A relationship? Tonight wasn’t the first time we’d. . . been together but we weren’t – no, not a ‘relationship’.

Then I have to describe the rape. I don’t want to be a victim, damaged. Nope. No, I want to be a survivor, but. . . I don’t know. I don’t know. Humiliation. Distress. What did I do wrong? Was I foolish? What should I have done?

(Scene 11) My phone beeps. A text. Oh god. It’s him. It’s Julian: “Hope you’re okay after everything? I’m heading off.” -- (to audience) After everything? Is he worried about what he did? What if I’m overreacting? I’m not. I’m not. (beat) Julian can’t just get away with it! Can he? Pretend it didn’t happen? (Scene 14) I’m terrified, how will I ever go back to work – with Julian there?

TESSA: (Scene 7) (flashback to the rape) Jules meets me at the Japanese place on the corner. We talk work, life, books, everything, pour sake for each other. We leave. Pick up some wine, grab gelato from the posh place up the road. When we get in, we both grab a spoon and dig into the gelato box together, feeding each other. We kiss. We drink some more. We move into my room, head to the bed, we seem to fall into having sex. It’s nice, until . . . I feel this, this overwhelming desire to vomit.

I feel everything hideous. Vomiting. The dank smell of the toilet bowl. I must have been there for. . . a while. I feel him carry me to the bed. Julian’s face kissing mine. I can’t kiss like this. I still feel ill. He’s on top of me but his hand is on my face. (to Julian) Hang on . . . No. I can’t breathe. Stop! (to audience) And . . . and he’s inside me, it’s rough and painful. (re-living the memory) This is not happening. Not happening. But I can’t scream, his hand is over my mouth. I try to bite his hand, I writhe around and try and kick him, I can’t breathe properly. It goes on and on. Searing pain inside of me. I am crying silently. And there is just this strange denial, Julian slumped on top of me. I struggle out of the bed, I vomit and vomit and vomit. Then I brush my teeth. I scrub my body. (long pause)

(using her ‘court’ voice) ‘Did you invite him to your home, to your bed?’ (to audience) I see my life, the one I have built, my career. My career! . . . What do I do now? Be a witness in my own courtroom?

(Scene 3) (flashback) First day, University law school. Cambridge. 200 faces. Society tells us that law school means you’re important. The dean stands, telling us

DEAN: You are the ones who will change the country. (beat) But. . . Look to your left. Look to your right. Look back at me and hear this. One of the three of you will not make it -- you will fail. You are not friends, you’re fighting each other. The game starts now.

Never assume anyone is telling you the truth – even yourself. There is no real truth, only legal truth. Don’t trust your gut instincts. You will get it wrong if you think you know what will happen. (beat)

TESSA: (Scene 4) The law is there to protect everyone. Protect those who accuse, protect those who are accused. Just test the law. Test it. Test it. But there’s always that question: How do you act for someone you KNOW did it!? A lawyer’s job is not that grand – uh uh – the job is not to KNOW. It’s to NOT know. My role is defense, the prosecutor prosecutes; we each tell a story and the judge and the jury DECIDES which story they believe. (Scene 6) In sexual assault cases it’s usually just one person’s word against another’s. Yes, the sex act happened; but was it consensual? The defense doesn’t have to prove she did consent; you just have to point out that HE DID NOT KNOW there was NO CONSENT.

I remember this one case. This woman, Jenna, looked me square in the face and said ‘I’m not getting anything out of this, I don’t want to be here. I’m just doing this to protect other women from this man.’ (beat) My job is to point out holes in the story. I her version of the story in court. Jenna lost. (beat) [But] What if he did it? I got him off. Shit. Can’t think like that, the prosecutor should have done a better job!

(Scene 8) (The courtroom -- Tessa is different now. Less articulate. Less confident. She gets worse once the cross-examination begins) This is me, Tessa Ensler, without my barrister robe. This is what it feels like. Same court, no armour. I’ve been waiting for 782 days, since that first day at [the police station] and now today is the day. Three years at university, one year of bar school, and seven years of practice. I have always believed that before the law there is justice.

(Scene 11) My life is in the hands of the police, the CPS, the court system. I have no control. But there’s this person inside me, the girl who fought and fought to be seen. Look left, look right, who won’t make it? She’s brave and if I do nothing, I think I could lose her. (Scene 12) Berating myself: ‘You didn’t scream or kick enough. -- You froze, in the middle of it all you just froze – what’s wrong with you? -- Julian’s a good barrister, he does lots of pro bono work, what are you doing to him? -- What if he really thought you were consenting?’ (arguing with herself) The law says you can’t do this to a woman. Can’t hold her down, ignore her, keep her trapped while you push – while you, you, push yourself inside of her. You can’t rape and then pretend it was consensual. Can you!?

(to audience) The trial will run for three days. And it is only me giving evidence, not Julian. Today Julian is pleading not guilty. But Julian is not stupid, he’s just convinced himself and all the people he has asked to write letters of support for him that I am lying. He has convinced himself he is the victim. While I’m forced to relive it all IN FRONT OF EVERYONE. Why? He is the one who did this to me; but I’m the one on trial. (Scene 13) Julian’s able to listen to everything -- sitting back knowing he will not have to say a word. (Scene 14) (in anguish) You raped me. You held me down and . . .

(Flashback to days after the rape in the court foyer) I have to face Julian after he’s been arrested. Court foyer.

JULIAN: (to Tessa) How could you do this to me? I held your hair while you vomited for christsakes. Are you out of your mind?

TESSA: You know what happened.

JULIAN: Whatever it was, I’m not a criminal, Tessa. And God, you’re not a victim or anything! You’ll destroy my career.

TESSA: (end flashback - in court) In my head I’m cross-examining myself, using my own defense skills to doubt my own story. I realize I have been doing this for two years and fifty-two days. Finding fault in my story.

DEAN: (Scene 3) (echoing in her head) There is no real truth, only legal truth.

TESSA: (Scene 15) (arguing with herself) I will not question my memory. I will not minimize what happened, I will not embellish. I know what happened that night.

PROSECUTOR: Did you make it clear to Mr Brookes you were not consenting to sex?

TESSA: I did. I told him no. Stop. I . . . I tried to push him away.

PROSECUTOR: Did you . . . scream?

TESSA: I tried but his hand was over my mouth. (to audience) More questions. More details. More humiliation. This is me, giving my testimony in court. [Then] the defense counsel stands slowly. This is it. The cross-examination. (Scene 16) And I realize they’re trying to say that I was mistaken, I wasn’t actually pinned down, and of course I could breathe. In fact, the hand on my mouth must have been mine, saving him from my bad vomit breath.

(to defense attorney) No. No. I tried to get away. I said no, I struggled. It was his hand on my mouth. (to audience) I can feel a terrible wrong being done to me right now. This line of questioning is making me look confused. Because I am, I am, I’m really confused. And then I remember. Right there in court, I remember. (to defense attorney with clarity, body and voice shaking) Julian had both of my wrists in one of his hands, pulled high above my head. And his other hand over my mouth and my nose – I could barely breathe. (to audience) My eyes on Julian now. How dare you? How dare you?

(Scene 17) (finding her voice, she speaks to the jury directly) Julian Brookes’ council will tell you, the jury, about what Mr. Brookes might have lost. But I will tell you what I have lost; I have lost my dignity and my sense of self. I have lost my career path, friends, peace of mind, my safety. But most of all, I have lost my faith in the law, the system I believed would protect me. The system I dedicated my life to. (to audience) After 782 days, I have found my voice. It’s a different voice, but it’s mine. Confident. Like a lawyer. (takes breath slowly; in and out) I see all the women who came before me and the ones who will come after. I see Jenna.

JENNA: I’m not getting anything out of this, I’m just doing this to protect other women.

TESSA: (to the jury) I am here in a unique position. Usually I stand at the bar, but now I am in this courtroom as a witness -- a victim. I have questioned women in sexual assault cases on the assumption that the evidence can be delivered in a clean, logical package. But now I have seen through my own attempts that it can’t be. The experience of sexual assault is not remembered in a neat, consistent, scientific parcel. And because of that, the law often finds the evidence “unbelievable.”

All my professional life I have participated in a system that has done this to women. I have suggested time and time again that a witness can be “mistaken” in their evidence. Before I would suggest that “she was confused.” I would point out inconsistencies as proof of doubt -- would tell the jury they couldn’t possibly be “sure.” (beat) Now I know, this is not right. This is not “reasonable.” Now I know that when a woman says “no,” when her actions say “no,” it is not a subtle unreadable thing at all. When a woman has been violated, it is a corrosive wound, one that begins with terror and pain deep in the body, then overtakes the mind, the soul. As a victim-survivor, the rape and perpetrator are vividly recalled -- the peripheral details not so clearly. If a woman is rattled by re-living the nightmare in court, if a woman’s experience of the rape is not the way the court likes it to be, then we conclude that she is prone to exaggeration. And it is because of this that she is so often disbelieved. So here in court, I want to call it out.

The law of sexual assault spins on the wrong axis. A woman’s experience of sexual assault does not fit the male-defined system of truth. So, it cannot be truth -- cannot be justice. The law has been shaped by generations and generations of men. (beat) There was a time, not so long ago, when courts did not “see” non-consensual sex in marriage as rape, did not “see” that battered women fight back in a manner distinct from the way men fight. Yet once we “see” we cannot “unsee” can we? Now I “see” through my own experience.

We have it all wrong when it comes to sexual assault. [But] the law is defined by us, constructed by us, in light of all of our experiences. The truth is that one in every three women are sexually assaulted, and their voices need to be heard. They need to be believed, for justice to be done. (to audience) One in three women. Look to your left, look to your right, one of us… (beat) I know the jury won’t find Julian guilty. But a weight has been lifted. (Scene 18) I am broken. But I am still here. And I will not be silenced.
```

---

## IC-0244: The Property Known as Garland

- Title: The Property Known as Garland
- Author (byline): Billy Van Zandt
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SETTING, VOICE, JUDY, ETHEL GUMM, STUDIO BOSS, YOUNG JUDY, MAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1794
- Already set (do not supply): none

### Source block (context only)

```text
Author: Billy Van Zandt
ISBN: 978-0573642395
Publisher: Samuel French, Inc.
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
According to Fred Astaire, Judy Garland was "the greatest entertainer who ever lived." But how did she become such a talented, internationally beloved, living legend? Through diet, nicotine, orthodontics, and drugs -- stimulants to keep her going and depressants to help her sleep -- Judy Garland was created to be a movie money maker. She worked 18 hours a day, 6 days a week as “the property” of MGM, sacrificing her soul to a ravenous public and uncaring industry in exchange for fleeting moments of joy found in front of the camera and on stage.

Her talent was legendary. Her story, more electrifying than you'd ever imagine. In this fictional account, Miss Garland takes us down the yellow brick road of her incredible life. It is March 1969, backstage at a theatre in Copenhagen as Judy Garland prepares for another star performance. In fact, this turns out to be her last concert: she tragically dies of a drug overdose three months later.

Born Frances Ethel Gumm, she became . . . The Property Known as Garland by Billy Van Zandt
```

### Performance text (classify this)

```text
SETTING: Star dressing room -- Falconre Center, Copenhagen, Denmark, March 25, 1969.

VOICE: (Pg 7) Miss Garland? Miss Garland? One hour, Miss Garland.

JUDY: (Pg 12-13) (JUDY’s mind drifts. She takes her cigarette and crosses to the dressing table . . distant) I have no intention of going on tonight. (Pours drink and toasts herself) Hello. I’m Judy Garland and I’m an alcoholic. Can you imagine? (Laughs) One of my husbands took me to an AA meeting once. Because he was a drunk! It was so – funny. He got livid because I sat there the entire meeting with a flask of Chivas on my lap. While all those people went on and on about how miserable their lives were. I mean, really. I’ll tell you why they were all so miserable. They needed a drink. That would’ve cheered them right up. Did you ever go to one of those things? You just sit there and sit there and listen to these tortured souls spilling out their troubles like a “who-has-the-most-pathetic-story contest.” Ye-Gods.

(Pg 15-17) (Judy stares at herself in the mirror) I have a very strange body. I’m all legs with this hump thing here and no neck to speak of. But I do have a lovely nose. Don’t you think? I have good eyebrows. And a good nose. That’s not much to go on. Mr. Louis B. Mayer, who ran Metro-Goldwyn-Mayer . . . used to refer to me as “the fat one” and “the hunchback.” And not behind my back either. He’d do it right on the set. He’d say, “Do you see this little girl? Look what a star I’ve turned her into. She used to be a fat little hunchback. Isn’t that right, Judy?” And I’d have to answer, “Why, yes, Mr. Mayer. I suppose it is.” So I have a bit of an inferiority complex about my looks. When I auditioned for M-G-M, I was thirteen years old, and someone asked my mother why I had never been under contract to a studio before, and –

ETHEL GUMM: Take a good look at her and figure it out for yourself.

JUDY: So, you see. I’m just a hopeless case. My entire career people have been trying to find ways to camouflage me, or make me pretty. They’ve put rubber pieces in my nose and capped my crooked teeth and changed my hairline and my color. They stuffed me into canvas body stockings to give me a waist. They put shoulder pads here and here. And when I did my TV show, they even built me a, well, a “rear end.” I may have million dollar legs, but in some trunk somewhere I also have a six hundred dollar ass.

But I do what they tell me. I’m conditioned. (Taking sip) Back at Metro, my primary function was to work. As long as I worked, the studio’s investment in the “property known as Garland” paid off. If I got fat I couldn’t work. And therefore I couldn’t get fat. (Judy stands next to the dressing table) They had this clothes dummy at the studio – a great, fat clothes dummy. And they’d make me stand next to it and stare into the mirror.

STUDIO BOSS: Take a good look at yourself, Judy. Now look at this big, fat, clothes dummy. Which one do you want to be? A big fat dummy, or a star?

YOUNG JUDY: I want to be a star.

STUDIO BOSS: Good girl. From now on make sure she gets nothing but chicken soup in the commissary.

JUDY: And that’s what they gave me. Every day at noon. For thirteen years. Chicken soup. And water. Like a prisoner’s menu. Now? Even the sight of a chicken? Instant throw-up.

It’s a chore being Judy Garland. You know how many people pull at me? Demand things of me? Write about me? How many drag queens imitate me? How many people tell my children they know me? They know me. They know Judy Garland. “Poor Judy. She tried to kill herself over four thousand times, you know.”

Well, I’m not as helpless as people think! I’m really not. (Pg 18) I’m not in Kansas anymore, folks. But no one wants to hear that. I’ll always be Dorothy Gale – just can’t get away from “her.”

MAN: Could you sign this for my daughter?

JUDY: Of course, darling. (Flashes as a camera goes off)

VOICE: Judy/Judy/Over here! (More flashes) Judy! / One picture? / One more!

JUDY: Thank you, pussycat. (Flash of a camera) I am so sick of saying thank you! (Beat) I’ve spent years and years and years trying to please people. My mother. Mr. Mayer. You! And no matter how hard I try, I’m constantly written about like I’m some sort of unfit person. Well, I’m not. I’m not! I’m not some sort of a joke. Yet people think I’m either a drunk, or a drug addict or. . . It’s a Goddamned wonder I’m not! But I’m not. I’m just me.

(Pg 19) (sarcastically) I made my debut in 1782. Back home in Grand Rapids where I was born. My darling father owned the theater there. And our whole family performed in vaudeville between the movies. Back then I was Baby Gumm. I was four years old. My mother was a hideous wicked woman. I was just a child, but that never mattered. If I was sick or something and didn’t want to go onstage, she didn’t care. She’d just say, “Get out there and sing or I’ll wrap you round the bedpost and break you off short!” Joan Crawford had nothing on her, believe me.

(Pg 21-24) When we lived in Lancaster . . . California? . . . if I got too much applause during our shows, my sisters would catch jars full of bees and then after the show, they’d lock me in a room and open the jars.

I had to survive Mother cheating on my darling father with our next-door neighbor. A ghastly made man who eventually left his paralyzed stroke-victim wife for my mother. A match made in hell. I loathed him.

YOUNG JUDY: How can you do this to Daddy?

ETHEL GUMM: Do what to Daddy?

YOUNG JUDY: I know what goes on with you and Mr. Gilmore

ETHEL GUMM: You don’t know as much as you think you do.

YOUNG JUDY: What don’t I know?

ETHEL GUMM: Your father is a homosexual, Judy. Why do you think we left Grand Rapids?

JUDY: Imagine telling a five-year-old girl that about her father. There’s the real Wicked Witch of the West. (Judy begins to prepare her make-up for the stage) Two months after I signed with Metro, Daddy went to the hospital with what turned out to be spinal meningitis. I didn’t know how bad it was or I would’ve spent every second by his side. But Mother didn’t tell me.

ETHEL GUMM: You go do your radio job, Judy. Never mind, Daddy. He’ll be fine. We don’t want M-G-M to think you’re difficult, now do we?

YOUNG JUDY: But Mama . . .

ETHEL GUMM: Judy, do you know what it took for me to get you this goddamn studio contract? How many fat, hunchbacked girls do you think they’re signing over there? Now get in the car and go sing.

JUDY: Right before I went on the air, I got a phone call saying they were placing a radio beside Daddy’s bed. And right then I knew. Daddy was dying. (Proudly) And so I went on. And I sang for Daddy for the last time.

* YOUR EYES MADE THE SKY SEEM BLUE AGAIN
WHAT ELSE COULD I DO AGAIN
BUT KEEP REPEATING
THROUGH AND THROUGH
I LOVE YOU, LOVE YOU . . . . .
It was the song I auditioned for M-G-M with. And one of the first songs Daddy ever taught
me. . . . Daddy died the next morning.

Life’s very peculiar. Mother married Mr. Gilmore on November 17, 1939. It was her forty-sixth birthday. And the anniversary of my father’s death. That was the most awful thing that ever happened to me. My mother marrying that awful man the same date that my Daddy died. (Pg 25) The only nice thing I will say about my mother is that she taught me not to be cruel to my own children. I should be grateful for that, I suppose. After my darling Daddy died, M-G-M more or less adopted me.

(Pg 36) They worked us six days a week from eight in the morning until three in the morning – for fifteen straight years. You’d finish one picture on Saturday and start your next picture on Monday. It was a schedule no one should’ve had to endure. Least of all a thirteen-year-old girl. And I had no one to fight for me. My darling father was gone. My mother did as she was told. (sips her wine) (Pg 37) That’s when they started giving me pills to keep me awake, and pills to go to sleep. And diet pills. They gave them to everybody. To keep us going, you know? Everyone thinks it’s such a “Garland” thing, but every actor in Hollywood took them.

(Pg 40) She never watched out for me, my mother. Never. After sixteen years and no time off, I was at the end of my rope. I was holding on by a thread, mind you. And they put me into another picture . . . “Annie Get Your Gun.” Just to get out of work one day, I slashed my wrists. Not deep. But enough. It was all very hysterical. There was blood everywhere. And people were screaming. But I did get the day off! (Beat) And then for no Goddamn reason at all, they fired me.

(Pg 41) Is it any wonder I ended up in a “nuthouse”? My very first – you always remember your first, don’t you? -- They put me in my own little bungalow (Framing her face with her hands, a la “A Star is Born”) – I was a movie star, after all. The entire time I was in there, my mother only called me once.

ETHEL GUMM: There’s something wrong with your brain, do you know that?

JUDY: Wicked old witch. (Beat) (Pg 44) What do you do after you give everything there is to give and it’s not good enough? Well, I just fell apart. (She laughs) (Pg 47) What have I learned from all this? (Thinks, then) Hell if I know. I’m just lucky I’m still here, I guess. All in all, I’m a very lucky woman. (Rising) I’ve got my children. I have my audiences. And for once in my life, I’m finally with a man who loves me. Me. Not my voice – because it’s gone. Not my money – because I didn’t have any when I met him, and I don’t have any now. He loves ME. Whether I sing or dance or whether I don’t. And he thinks I’m pretty. (finishes lipstick, into mirror) Me. Pretty. You hear that, Mama? (Beat)

(Pg 49) Recently, one of the reporters asked me if I’d do it all over again. “You bet your life, Buster. With all the same mistakes, too.” I was put on this earth to give. To give my heart and soul to my audiences. I can’t do any less. I really can’t. I never will. (She hears applause from stage area) You’ll never know this kind of love, Mama. It’s the one thing you couldn’t take from me. (Motions off) That’s mine! They love me. Hunchback and crooked teeth and insecurities and all. And that love is mine! Alone! I love them! And I need them! But you know something? They need me too! (Judy enters the stage)
```

---

## IC-0245: Push

- Title: Push
- Author (byline): Sapphire
- Work: Not specified
- Publisher: Alfred A. Knopf, Inc
- Publication date as stated: June 1996
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: PRECIOUS
- Teaser before the introduction: No
- Spoken words (computed): 2023
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sapphire
ISBN: 978-0679446262
Publisher: Alfred A. Knopf, Inc
Date (Month/Year): June 1996
```

### Introduction (context only: never use it for content warnings)

```text
A black street girl, sixteen years old and pregnant, again, with her father's child, speaks. In a voice that shakes us by its language, its story, and its unflinching honesty, Precious Jones records her journey up from Harlem's lowest depths. . . For Precious, miraculously, hope appears and the world begins to open up when a courageous black teacher bullies, cajoles, and inspires her to learn to read, to define her own feelings and set them down in a diary: to discover the truth of her life.

Push by Sapphire
```

### Performance text (classify this)

```text
PRECIOUS: When I get to school early sometimes I just sit in front part on the black plastic couch that need tape where it cut and the yellow foam pads show through. School start at 9 o'clock. The secretary get here at 8:00 a.m. I don' get here before that' cause the door locked and I would have to wait in the lobby downstairs. Which I don't like.

Our room is nice. Nicer since we have one day where we come in "raggedy" and bring our own cleaning stuff'n posters, pictures, 'n plants from home 'n fix up our room. Ms Rain say bring something of YOU! I bring picture of Abdul and plant from Woolworth on 125th Street. It growed. Leaves big. Ms Rain done changed its pot three times.

Ms Rain get here 'bout 8: 15 or so, usually right behind or in front of Rita or Rhonda. They bofe erly birds too. Ms Rain jus' give whoever here the keys from her purse to open up our classroom while she do whatever she do-fix coffee, git books from supply room-stuff like that. By 8:30 a.m. early birds good to go! Room quiet sunny. We just open our notebook, Ms Rain usually say something like, You got 10 or 15 minutes 'fore the "rabble" get here. Yeah, I don't know exactly what is the rabble. She jus' joking for Jermaine and them who hit the door roun' 9:05 a.m. Always a little late, always complaining 'bout something-the weather, train, what the newspaper say.

Me, I, just look at the sun coming in through the front window. Pretty soon it move around and come in through the side window. I like the routine of school, the dream of school. I wonder where I be if I had been learning all those years I sit at LS. 146. Favorite book? Maybe it's our book, the big book with all our stories in it. Not mine yet. I'm just putting stuff in my journal now.

Telling time is easy. Fractions, percents, multiplying, dividing is EASY. Why no one never taught me these things before. Rita say, All people with HIV or AIDS is innocent victims; it's a disease, not a "good," a "bad." You know what she mean? Well, thas good' cause I don't. I cannot see how I am the same as a crack addict. Rita kiss my forehead, hold each my cheeks with her hands, look me in my eyes, "Negra," she say, her eyes big like babies', black black eyes. ''You don't see now but will. You will."

I don't know how I will, I don't even know what she's talkin' about. She's talking about Life, Ms Rain say. Well, I don't know what life is all about either. I know I'm eighteen, magic number. And my reading score is 2.8. I ask Ms Rain what that mean. She say it's a number! And can't no numbers measure how far I done come in jus' two years. She say forget about the numbers and just keep working. The author has a message and the reader's job is to decode that message as thoroughly as possible. A good reader is like a detective, she say, looking for clues in the text. A good reader is like you Precious, she say. Passionate! Passionately involved with whut they are reading. Don't worry about numbers and fill in the blank, just read and write!

I'm changing. Things I don't care about no more: if boyz love me, extensions, new closes what I care about is: STAYING HEALTHY, sex, notebook, writing poems

Ms Rain say don't always rhyme, stretch for words to fall like drops of rain, snowflakes-did you know no two snowflakes is alike? Have you ever seen a snowflake? I haven't! All I seen is gobs of dirty gray shit. You mean to tell me that nasty stuff is made of snowy flakes. I don't believe it.

Each day is different. All the days is gobbed together to make a year, all the years gobbed together to make a life. I have a secret. Secret is, I mean I think Rita and Ms Rain halfway know but they too nice to get any further in my business than I want them in. I mean I have kids. But I never have a guy, you know like that. It never usta be on my mind. All I want before is Daddy to leave me alone! But now I think about that, you know, that being a cute boy. I think about that and I think about being a poet or rapper or an artist even. It's this guy on one-two-five, Franco, he done painted pictures on the steel gates that's over almos' all the store windows. At night you walk down and each one is painted different. I like that better than museum.

It's so many different ways to walk the few blocks home. Turn a corner and you see all different. Pass 116th 'n Lenox, more abandoned land, buildings falling down. How it git so ugly is people throw trash all in it. City don't pick it up; dogs doo doo. Ugliness grow multiplied by ten. Keep walkin' down Lenox to one-twelve you pass projects. I never did live in projects. I live in 444 Lenox Avenue almost all my life. Where I live before that house I don't know, maybe wif my grandmother.

I got session wif counselor today. Last week we try to figure out how long I been infected. People at retard place say Lil Mongo don't got it. She say that could mean Daddy get AIDS pretty fast from time he first infected to time he die? 'Cause if Lil Mongo don't got it maybe he didn't have it 1983 when she born. Then after she born he go away a long time. So maybe I get it eighty-six, eighty-seven? Counselor say, I'm on top now. I'm young, is got no disease and stuff, not no drug addict. I could live a long time, she say. I ask her what's a long time. She don't say.

I think some of the girls at Advancement House know I am . . . am positive. I mean wifout trying I know some of they bizness. They never was too friendly; since Mama come wif her news, they even less friendly. But who cares? I'm not tight wif these girls in the house. They got problems, come in room and steal. I know I ain' the only one that got it, even though that's how it feels. But I'm probably the only one get it from they daddy. Counselor, Ms Weiss, say she try to find out as much about Daddy for me as she can.

How much I want to know? And for what? I tell counselor I can't talk about Daddy now. Daddy sick me, disgust me, but still did that to me. I nawshus in my stomach and I think I want it back, the smell of the bedroom, the hurt-he slap my face till it sting and my ears sing separate songs from each other, call me names.

I wait for him get off me. Lay there stare at wall till wall is a movie, Wizard of Oz, I can make that one play anytime. Michael Jackson, scarecrow.

Afterward I go bafroom. If I go to insect support group what will I hear from other girls. I bite my fingernails till they look like disease, pull strips of my skin away. Get Daddy's razor out cabinet. Cut cut cut arm wrist, not trying to die, trying to plug myself back in. I am a TV set wif no picture. I am broke wif no mind. No past or present time. Only the movies of being someone else. Someone not fat, dark skin, short hair. A pink virgin girl. A girl like Janet Jackson, a sexy girl. A girl for value.

I hate myself when I think of Daddy. Hate wif a capital letter. Counselor say, "Memories." How is something a memory if you never forgit? But I push it to the corner of my brain.

I exhausted, I mean wipe out! What kinda chile gotta think about a daddy like I do? But I'm not a chile. I'm a mother of a chile myself!

In school we had to memorize a poem like the rappers do. And say it in front the class. Everybody do real short poems except me and Jermaine. She do poem by lady name Pat Parker. I get up to do my poem, it's by Langston Hughes, I dedicate it to Abdul. Introduce myself to the class (even though everybody know me). I say my name is Precious Jones and this poem is for my baby son, Abdul Jamal Louis Jones. Then I let loose:

MOTHER TO SON
Well, son, I'll tell you:
Life for me ain't been no crystal stair. It's had tacks in it,
And splinters,
And boards tom up,
And places with no carpet on the floorBare.
But all the time
I'se been a-climbin' on,
And reach in' landin's,
Ana tumin' comers,
And sometimes goin' in the dark Where there ain't been no light.
So boy, don't you turn back.
Don't you set down on the steps
'Cause you finds it's kinder hard. Don't you fall now
For I'se still go in', honey,
I'se still climbin',
And life for me ain't been no crystal stair.

And after I finish everyone goin', Yeah! Yeah! Shoutin', Go Precious! And clapping and clapping and clapping. I felt very good.

Ms Rain say write our fantasy of ourselves. How we would be if life was perfect. I tell you one thing right now, I would be light skinned, thereby treated right and loved by boyz. Light even more important than being skinny, you see them light-skinned girls that's big an' fat, they got boyfriends. Boyz overlook a lot to be wif a white girl or yellow girl, especially if it's a boy that's dark skin wif big lips or nose, he will go APE over yellow girl. So that's my first fantasy, is get light. Then I get hair. Swing job, you know like I do with my extensions, but this time it be my own hair, permanently.

Then, this part is hard to say, because so much of my heart is love for Abdul. But I be a girl or woman-yeah girl, 'cause I would still be a girl now if I hadn't had no kids. I would be a virgin like Madonna. I would be a different Precious Jones.

So there if I have a fantasy it be how I look. Ms Rain say I am beautiful like I am. Where? How? To who? To not have no kids mean I woulda had a different life. Counselor ask me one time is it the kids or is it I get raped to have' em. Bofe; 'cause even if I not raped, who want a baby at twelve! Thas how old I was when I had Little Mongo.

What is a normal life? A life where you not 'shamed of your mother. Where yur friends come over after school and watch TV and do homework.

Where yur mother is normal looking and don't hit you over the head wif iron skillet. I would wish for in my fantasy a second chance. Since my first chance go to Mama and Daddy.

Ms Rain always saying write remember write remember. Counselor say talk about it, talk about it-the PAST. What about NOW! At least wif school I am getting' ready for my future (which to me is right now).

I don't know why I don't like counselor but Ms Rain say TALK, it gonna make things better whether I like her or not. But you know she jus' another social worker scratching on a pad. I know she writing reports on me. Reports go in file. File say what I could get, where I could go-if I could get cut off, kicked out Advancement House. Make me feel like Mama.
```

---

## IC-0246: Rabbit Hole

- Title: Rabbit Hole
- Author (byline): David Lindsay-Abaire
- Work: Not specified
- Publisher: Theatre Communications
- Publication date as stated: Sept 2006
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: HOWIE, BECCA, VOICE OF DANNY, NEWS REPORTER
- Teaser before the introduction: No
- Spoken words (computed): 1038
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Lindsay-Abaire
ISBN: 978-1559362900
Publisher: Theatre Communications
Date (Month/Year): Sept 2006
```

### Introduction (context only: never use it for content warnings)

```text
Eight months ago, in a happy suburban home, the family dog darted out of the front yard. And Danny followed - right into the path of an oncoming car. It was an "accident," -- But that just means that no one is to blame but everyone feels guilty. The journey through grief is different for all of us . . . We each take our own path. There is no right or wrong way to grieve. Rabbit Hole by David Lindsay-Abaire
```

### Performance text (classify this)

```text
HOWIE: (Pg 14) You want more wine?

BECCA: No, I’ve had two already.

HOWIE: Half a glass . . . (he empties the rest into her glass and lowers the lights in the room)

BECCA: What are you doing?

HOWIE: My eyes are sore, staring at that computer all day.

BECCA: (Pg 15-18) How was squash?

HOWIE: Good. I lost but it was good

BECCA: How’s Rick? . . . . and Debbie? Did Rick mention her?

HOWIE: You can call her, you know. You can call Debbie.

BECCA: I don’t wanna call her. She should call me.

HOWIE: She’s uncomfortable, Bec. If she hasn’t called you, it’s because she doesn’t know what to say.

BECCA: How about “Hey, Becca, how you doing? Haven’t seen you in a while. I would’ve been there for her if God forbid something had ever happened to Robbie or Em. I wouldn’t have vanished the way she did.

HOWIE: If you’re pissed, you should call her and tell her . . . Okay, let it go.

BECCA: Let what go?

HOWIE: Whatever’s making you tense. You should try to relax a little. (He moves to massage her shoulders and starts to kiss her neck)

BECCA: What are you doing?

HOWIE: I’m trying to relax you – something wrong with that?

BECCA: I see what this is. Dimming the lights . . . plying me with liquor . . . . You’re trying to seduce me.

HOWIE: Am I? (moves in again romantically)

BECCA: Alright, Romeo (pushes him away) Enough.

HOWIE: Jesus, Bec . . . it’s been almost eight months. (Beat)

BECCA: I’m just not ready yet, Howie. I’m sorry if you think that’s abnormal.

HOWIE: I thought it was nice. That’s all. I was trying to make things nice.

BECCA: Well . . . you can’t. I’m sorry, but things aren’t “nice” anymore.

HOWIE: (Pg 19-20) -- then . . . maybe we should try again. (Beat)

BECCA: Oh for godsakes, Howie . . . Is that . . . Is that what this was?

HOWIE: No. No, of course not. It just . . . it might be something to talk about at some point.

BECCA: I . . . I can’t. I’m sorry. I can’t have that talk. (Becca exits, Howie watches her go, then goes to the TV cabinet and pulls out a videotape and pops it in.)

VOICE OF DANNY: Did you see me, Daddy?

HOWIE: (speaks along with the video) I did.

VOICE OF DANNY: No, you didn’t. I’m invisible. I have magic.

HOWIE: (speaks along with the video) Down, Taz . . . Oh, I didn’t realize. (lights fade) ******** A few weeks later***********

(Howie clicks on the TV and hits play on the VCR. We hear a documentary on tornadoes playing. [ ] words in red are not printed in the original script )

NEWS REPORTER: [Last year was the strongest storm season in a decade . . . ] (Howie is confused. Something isn’t right. He ejects the tape, examines it, puts it back in and hits play again [An F5 Tornado is the most damaging wind force]

HOWIE: (Pg 32-34) What is this? Becca? Becca!?!! (Becca enters – Howie is beside himself)

BECCA: What’s the matter?

HOWIE: The television. What is this?

BECCA: (Looks to TV) It’s the Discovery Channel. The tornado program. I recorded it for you. What’s the matter?

HOWIE: It’s Danny’s tape. You recorded over Danny’s tape. Jesus, Becca! It’s the only copy!

BECCA: Well, I didn’t do it on purpose. (Howie looks at her skeptically) You think I recorded over Danny’s tape on purpose?

HOWIE: You took the paintings off the fridge. Danny’s paintings. And shoved them in a box.

BECCA: For safekeeping

HOWIE: You’re trying to get rid of him. I’m sorry, but that’s how it feels to me sometimes. Every day, it’s something else. It feels like you’re trying to get rid of any evidence he was ever here.

BECCA: (It’s as if she’s been slapped) The paintings are downstairs. In a box. You can look at them whenever you want.

HOWIE: The clothes. His shoes.

BECCA: We don’t need all that stuff. Why would we keep –

HOWIE: Taz. Sending Taz to your mother’s!

BECCA: There was a lot going on, Howie. We couldn’t deal with the dog.

HOWIE: If I hadn’t bought the dog –

BECCA: And if I hadn’t run inside to get the phone, or if I had latched the gate –

HOWIE: I left the gate unlatched!

BECCA: Well, I didn’t check it. (Retreats a bit) I’m not playing this game again, Howie. It was no one’s fault

HOWIE: Not even the dog’s . . . Dogs chase squirrels. Boys chase dogs.

BECCA: Are you telling me or yourself?

HOWIE: He loved that dog! . . . And you got rid of him!

BECCA: Right, like I got rid of the tape. I get it.

HOWIE: He was a reminder.

BECCA: Yes, he was a reminder. So what? I wanted one less reminder around here. (Pg 19) I can’t move without – I mean, Jesus, look at this. (grabs a toy from the shelf)

Everywhere. (grabs a kid’s book from a stack of magazines) Here: “Runaway Bunny” for godsake. The puzzles. The smudgy fingerprints on the doorjambs.

HOWIE: I like seeing his fingerprints.

BECCA: Because you don’t have to sit and stare at them day in and day out. You get to escape. You get to go to work. . . . I left all that to be a mom.

HOWIE: (Pg 18-19) (after a pause) I think you should see someone. (Beat) I know you’re not one for therapists, but I think you should. We could go together if that’s help. Or maybe you could try the group again.

BECCA: No. (Pg 29) A room full of God-freaks.

HOWIE: They’re not God-freaks.

BECCA: Most of them are, Howie. That’s all they talk about. God’s plan. My favorite is “God needed another angel.” What is that? He’s God! Why can’t he just make another angel? It pisses me off. Trying to find some ridiculous meaning in – “Hey look, I stepped in shit, it must be part of God’s plan.” How nice they all have something that makes them feel a little better. Like I don’t feel bad enough. I’ve gotta go and have that rubbed in my face? [God’s] a sadistic prick.

HOWIE: (Pg 34-35) (long silence) You have to stop erasing him! I’m not [just] talking about the tape, Becca! It’s Tax, and the paintings, and the clothes and it’s everything! You HAVE - TO - STOP!

BECCA: Do you really not know me, Howie? Do you really not know how utterly impossible that would be? To erase him? No matter how many things I give to charity, do you really think I don’t see him every second of every day? That tape was an accident. And believe me, I will beat myself up about it forever. Like everything else that I could’ve prevented but didn’t.

HOWIE: That’s not what I want, Bec. It’s not what I’m talking about.

BECCA: No? Because it feels like it is. It feels like I don’t feel bad enough for you. I’m not mourning in the right way. But let me just say, Howie, that I am mourning as much as you are. And my grief is just as real and awful as yours.

HOWIE: I know that.

BECCA: You’re not in a better place than I am, you’re just in a different place. And that sucks that we can’t be there for each other right now, but that’s just the way it is.

HOWIE: His stuff is all we have left. That’s all I’m saying. And every bit of it you get rid of –

BECCA: I understand that. You don’t wanna let go of it. I understand, Howie.

HOWIE: Do you? Do you? (No response) Something has to change here. Because I can’t do this . . . like this. It’s too hard. (Beat) it’s too hard. (Howie exits, leaving Becca alone.)
```

---

## IC-0247: Rattle Rattle

- Title: Rattle Rattle
- Author (byline): Wendy Maclaughlin
- Work: More One-Act Plays for Acting Students
- Publisher: Meriwether Publishing
- Publication date as stated: July 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DOCTOR, SALLY
- Teaser before the introduction: No
- Spoken words (computed): 1732
- Already set (do not supply): none

### Source block (context only)

```text
Author: Wendy MacLaughlin
Book: More One-Act Plays for Acting Students
ISBN: 1566080878
Publisher: Meriwether Publishing
Date (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
(Intro should be said out of character…as narration)

DOCTOR: Psychology is a very difficult field to be involved in.

SALLY: No two people think in exactly the same way

DOCTOR: And although the situations of patients may be similar, no two patients react the same.

SALLY: But the hardest part…

DOCTOR: not becoming a patient yourself.

BOTH: “Rattle Rattle”

SALLY: By Wendy Maclaughlin
```

### Performance text (classify this)

```text
(DR. WAVERLY enters SALLY's room. She is propped up in bed with a drawing pad in front of her. She draws staring intently into the mirror. He observes her for a moment.)

DOCTOR: How're we doing today?

SALLY: Don't know about you but I'm disjointed.

DOCTOR: (Writing) Disjointed?

SALLY: Like everything's turned inside out.

DOCTOR: (Writes.) Ummm. Inside out.

SALLY: Why do you repeat what I say?

DOCTOR: I'm trying to understand how you feel.

SALLY: Rattled. Rattled. (Angry) Rattled!

DOCTOR: You're in a hospital, Sally.

SALLY: Liar.

DOCTOR: I never lie, Sally. You may not like what I say but I promise you, I don't lie. Lying is abhorrent to me.

SALLY: Who are you?

DOCTOR: I'm your doctor. Dr. Waverly.

SALLY: You a real doctor?

DOCTOR: I'm your psychiatrist.

SALLY: I'd rather have a real doctor. What's that thing hanging round your neck?

DOCTOR: This is a stethoscope. To listen to your heart. See?(Shows it to her.)

SALLY: Know what I see?

DOCTOR: I'd like you to tell me.

SALLY: I see a psychiatrist trying to act like a real doctor. (Stares into the mirror and draws.)

DOCTOR: And what do you see in that mirror, Sally?

SALLY: My face, stupid.

DOCTOR: It's a very nice face.

SALLY: Ugly. All of me is ... ugly.

DOCTOR: Do you remember what happened yesterday?

SALLY: I wet my pants.

DOCTOR: No.

SALLY: In first grade I did. Now why'd I do that? I knew better.

DOCTOR: Do you remember the scissors?

SALLY: What was I doing with scissors?

DOCTOR: Chasing your father.

SALLY: There was this girl. Six years old. She'd hide behind the crack in the door, get her mother's eye, go like this, (Beckons with her finger) then peek around the corner, roll her eyes, smack her lips and say... guess what?

DOCTOR: What?

SALLY: You know.

DOCTOR: No I don't.

SALLY: (Sing song) Time to eat.

DOCTOR: (Probing) She was six years old?

SALLY: Long as you nursed you weren't supposed to get PG.

DOCTOR: PG?

SALLY: (Loud) Pregnant! Mother didn't want to get pregnant again now did she? You're about the dumbest doctor I ever met. How many children do you have?

DOCTOR: One. A boy. A very good boy. Makes straight A's. Going to be a lawyer.

SALLY: Do you love him?

DOCTOR: More than anything in the world.

SALLY: Does he love you?

DOCTOR: He lives with his mother. Yes, I think he does love me. However, I'm aware that his mother would tell you a different story.

SALLY: My mother was in labor twenty-nine hours and she was sick from the first month I was in her tummy. He told me often enough.

DOCTOR: How'd that make you feel?

SALLY: He didn't say she didn't love me. He just said she didn't want me. You can only do so much what with the farm, five children and one on the way. But she was glad to have me after I got here, I'm sure of that.

DOCTOR: You were sure she was glad.

SALLY: (Strong) Very sure. I got sick a lot. Asthma, scarlet fever. Mommie let me stay with her on the sleeping porch. Daddy slept ... somewhere else. All I could eat was chicken soup. Mother made so much chicken soup it came out her ears. I don't like chicken soup much. Do you? They probably wanted to throw me out with the whole batch. What'd they want with another baby anyway? Especially a (Exaggerates) girl. They feed girls to alligators in China.

DOCTOR: That's hard for a girl to understand, isn't it? I'm sorry.

SALLY: If it makes you feel bad I won't tell you any more.

DOCTOR: I guess I'm just a little surprised you aren't sad about what you're saying.

SALLY: Why should I be sad? It's already happened.

DOCTOR: Does anything make you sad?

SALLY: There was this retarded boy in school. He never smiled. The boys were supposed to wear red beanies, the girls green beanies. One day he came to school wearing a green beanie. Everyone laughed. He was so happy. That's about the saddest thing I can think of.

DOCTOR: Does it make you want to cry?

SALLY: I never cry. Even when someone dies. What's there to cry about? They're going home. Every day you pick up the paper and read something about mothers abandoning their babies. Now that's something to cry about. Well, I wasn't abandoned, now was I?

DOCTOR: No, Sally, you weren't abandoned.

SALLY: Mother nursed me so you know she wanted me. I know she wanted the best for me and she knew the best for me was not to be born right then. If I hadn't been born right then, I'd have had a chance to go to someone who really wanted me. See, I'm sure she knew I'd understand. Why would I be nursing my doll if I didn't understand.

DOCTOR: Do you still nurse your doll?

SALLY: Do you still play doctor?

DOCTOR: Tell me about your doll.

SALLY: Wendy had long curls and sky blue eyes. We did all my chores together. We loved to gather eggs, reach under their soft white breasts, feel the warm, smooth, oval shells. I took her everywhere, even to the rabbit hutch that time I tried to kill myself.

DOCTOR: Do you want to talk about that?

SALLY: (Holds out wrists.) See this? I cut myself with a razor. Not very deep. Then I rubbed rabbit dung into the cut places. Thought I'd get lockjaw and die.

DOCTOR: I'm glad you didn't.

SALLY: Then another time we went out in the snow, took off our clothes, lay down and made snow angels. We were supposed to get pneumonia and die but the only one to die was Wendy. Her funeral was so beautiful. I put daisies over her eyes, a butterfly landed on her nose and all the birds sang ... Wendy. She got her name from Peter Pan. She was Peter Pan's mother. (Draws.)

DOCTOR: What're you drawing?

SALLY: My face. I look in the mirror real hard, try to see what I'm thinking. I draw every freckle, every eyelash ... (Shows him the drawing.) Does it look like me?

DOCTOR: Yes it does. You're quite an artist. Looks like you're flying.

SALLY: Flying in space. Like Peter Pan. Flying free forever ...forever ... and forever. Sometimes I draw when I get mad. Scared.

DOCTOR: What kind of things make you mad? Scared?

SALLY: Oh you know... dark nights, shadows on the wall, doorknobs rattling ... men playing cards, beer stink, Mommie crying ... he shouting, "Why'd that kid have to come into our life." I put the pillow over my head. After it got quiet I sneaked downstairs, got my crayons and drew till the sun came in through the window.

DOCTOR: Would you show me those pictures?

SALLY: Too ugly. Burned 'em. (Challenging) You wanna draw?

DOCTOR: I can't draw a straight line.

SALLY: Better if you don't. All you do is look in that mirror there. The mirror where you and the others watch me.

DOCTOR: You're a very smart girl, Sally.

SALLY: Girls have to be twice as smart as boys.

DOCTOR: That doesn't seem fair, does it?

SALLY: Lucky it isn't hard. (Pats chair.) Sit down. Right here. (Hands him paper and pencil.) First thing you gotta do is look in the mirror and get a feeling.

DOCTOR: (Looks into mirror.) Don't spend a lot of time looking at myself in the mirror.

SALLY: This isn't about looks. About feelings. Think about something that makes you sad. That isn't much of a feeling. Try getting mad. Come on, Doctor, let your blood boil. Come on, you can do better than that. Yell. Scream. I hate you. I hate you. (Screams.) I hate you. (Works herself into a frenzy and starts hitting him.) I hate you... I hate you... I hate you!

DOCTOR: (Protects himself with a pillow.) Go on. Go on.

SALLY: (Pounding pillow) Disgusting... stinking ... drunken ... pig. Stay away... get out ... gooooooooo ...

DOCTOR: Good girl. Hit me harder.

SALLY: (Piercing scream) Baaaaaastaaaard! (Slumps down exhausted.)

DOCTOR: (After a pause, a gentle touch) Sally.

SALLY: (Jumps like a rabbit.) Don't you touch me.

DOCTOR: (Calming) OK, Sally. It's OK.

SALLY: Stupid. You're a stupid doctor. You haven't drawn one line. Sit there. Take your pencil, put it down on the paper. Now look at yourself and get mad. Draw!

DOCTOR: (Looks into mirror, draws and carefully explains.) In the art of psychiatry we speak of transference...

SALLY: Grit your teeth, wrinkle your forehead. Good.

DOCTOR: People take their feelings ...

SALLY: Stare.

DOCTOR: ... emotional reactions and patterns ...

SALLY: Don't look at the paper.

DOCTOR: ... they live out with their mother, father ...

SALLY: You're thinking too much.

DOCTOR: ... and project them onto the doctor.

SALLY: Don't blink your eyes.

DOCTOR: Sometimes even the doctor begins to feel...

SALLY: What you see is going down your arm ...

DOCTOR: ... respond like the very people the patient has created.

SALLY: ... right onto the paper.

DOCTOR: We begin to become ...

SALLY: Your feeling will start to come out ...

DOCTOR: ... what the patient thinks ...

SALLY: ... all over the paper.

DOCTOR: ... rather than what we really are.

SALLY: Let it flow.

DOCTOR: So...

SALLY: Slow and easy.

DOCTOR: Perhaps...

SALLY: (Low) Good.

DOCTOR: I've ah ...

SALLY: (Whispers.) Magic.

DOCTOR: I... can't believe it.

SALLY: What?

DOCTOR: I... look like my father.

SALLY: He looks sad.

DOCTOR: He was sad.

SALLY: Why?

DOCTOR: He wanted me to be perfect.

SALLY: That can do it.

DOCTOR: When I wasn't he made up stories to make everyone think he was.

SALLY: Did he love you?

DOCTOR: He wanted me to be a surgeon. He thought all psychiatrists were crazy. "No one has the ability to look into another mind. Nor the right."

SALLY: Do you love him?

DOCTOR: One day after I got a C in science he sat me down and whispered very precisely, "I don't know how to tell you this and your mother will deny it but I am not your real father."

SALLY: (Fascinated) Was it true?

DOCTOR: Another story but I swore to kill myself before I'd end up like him.

SALLY: You ever try?

DOCTOR: Almost everyone has thought of trying.

SALLY: But did you do it?

DOCTOR: Well... I ... ah ...

SALLY: Did you? Did you? (Pause) You gonna tell stories like your father?

DOCTOR: Once. Once I tried to kill myself.

SALLY: Do you want to talk about that?

DOCTOR: One rainy night I drove my car into a wall. Expected the engine to come back and smash my chest. It didn't.

SALLY: Isn't that always the way. (Resumes drawing.) Funny.

DOCTOR: What's funny is how often we become what we hate.

SALLY: (Long pause) I didn't kill him did I?

DOCTOR: No.

SALLY: I misremember some.

DOCTOR: Do you remember what happened yesterday?

SALLY: They were laughing.

DOCTOR: Who was laughing?

SALLY: He and those men.

DOCTOR: What were they laughing at?

SALLY: He was showing them my pictures. Then he called me Mommie's name. Told them I was his new wife. It made me sick. I was so mad I ran to my room, got my scissors, crawled under the bed and held my breath. Then later the door knob rattled. Rattled. Then he ... he ... I forget.

DOCTOR: Do you hate your father, Sally?

SALLY: Hate is strong.

DOCTOR: Yes.

SALLY: Mommie says ... he's lonely.

DOCTOR: Are you lonely?

SALLY: Not when I draw. When I draw I go inside to a secret place. A place connected to pretty things.

DOCTOR: What pretty things?

SALLY: Oh you know... birds ... flowers ... Wendy and the farthest star.

DOCTOR: Is that a good place to be?

SALLY: I'm happy there.

DOCTOR: I'm glad, Sally. Very glad. (Checks watch.) Well, I have to go. I'll see you tomorrow… I'd like another drawing lesson.

SALLY: OK.

DOCTOR: (Starts to leave.) Good-bye, Sally.

SALLY: Doctor Waverly?

DOCTOR: Yes.

SALLY: Next time you draw in the mirror, forget all that stuff about your father.

DOCTOR: In psychiatry we try to remember.

SALLY: Better to forget.
```

---

## IC-0248: Real Women Have Curves

- Title: Real Women Have Curves
- Author (byline): Josefina Lopez
- Work: Not specified
- Publisher: Dramatic Publishing
- Publication date as stated: Dec 1995
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: PLAYWRIGHT, ANA, CARMEN, PANCHA, ESTELA, ROSALI, CALLER, ESTELLA
- Teaser before the introduction: Yes
- Spoken words (computed): 1405
- Already set (do not supply): none

### Source block (context only)

```text
Author: Josefina Lopez
ISBN: 978-0871297259
Publisher: Dramatic Publishing
Date (Month/Year): Dec 1995
```

### Introduction (context only: never use it for content warnings)

```text
Join me today in the small garment shop of Estela Garcia and maybe you’ll understand Real Women Have Curves by Josefina Lopez.
```

### Performance text (classify this)

```text
PLAYWRIGHT: (Pg 6) In the US undocumented people are referred to as “illegal aliens” . . . which conjures up the image of extraterrestrial beings who are not human, who do not bleed when they’re cut, who do not cry when they feel pain, who do not have fears, dreams and hopes . . . Undocumented people have been (and still are) used as scapegoats for so many of the problems in the US, from drugs and violence to the economy. I hope that someday this country recognizes the very important contributions of undocumented people and remembers that they too came to this country in search of a better life.

NOTE: Words in Spanish are in bold print. A glossary of Spanish terms appears at the end of this selection

ANA: (Pg 10) (to audience as she writes in her journal) Monday, September 7 . . . I don’t want to be here! I only come because my mother practically drags me out of bed and into the car and into the factory . . . Is it selfish of me not to want to wake up every morning at 6:30 am, Saturdays included, to come work here for 67 dollars a week? Oh, but such is the life of a Chicana in the garment industry. Cheap labor . . . I can’t believe I’ve ended up here. I just graduated from high school. Most of my friends are in college. It’s as if I’m going backwards. I’m doing the work that mostly illegal aliens do. No . . . “undocumented workers” . . . or else it sounds like these people come from Mars. Soon I will have my Temporary Residence Card. Then after two years, my green card. I’m happy to finally be legal, but I thought things would be different.

CARMEN: (pounding on the door) Ana, open the door! Hurry! He’s following me! (Ana opens the door and Carmen hurries in nervously.) (Pg 14) I saw a van! La migra! (Ana quickly shuts the door and they hide, waiting to be discovered . . . after a few seconds)

PANCHA: Pero, why are we hiding? (Pg 15) Let those men in their van come! We’re all legal now! (the women begin their work shift, sewing, ironing. They talk as they work)

ESTELA: I’m not.

ANA: But you went with me to get the fingerprints and the medical examination.

ESTELA: I didn’t send them in. (Beat) I have a criminal record.

CARMEN: (Pg 16) Estela, what did you do?

ESTELA: I was arrested for illegal possession of . . .

PANCHA: A gun?!

ESTELA: A lobster . . . out of season! I almost got handcuffed and taken to jail. Trying to “abduct” a lobster is taken very seriously in Santa Monica. And I’m being sued for not keeping up with my payments on the machines. I thought I could make the monthly payments if everything went as planned.

CARMEN: Pos que paso?

ESTELA: (Pg 17) We never finish on time, so the Glitz company doesn’t pay until we do. We get behind, they don’t pay, and I can’t pay those pigs that sold me those machines. They’re taking me to court. . . And if I appear in court, they’ll find out that I don’t have any papers.

ANA: (Pg 22) How much do they pay us for making these dresses? (she holds one up)

ROSALI: Estela, we get thirteen dollars for these, no?

ANA: How much do they sell them for at the stores?

ESTELA: They sell them at Bloomingdale’s for about two hundred dollars.

ANA: Dang!

ESTELA: (Pg 32) Let’s get to work. A trabajar! (She turns on the radio) RADIO (VOICE OVER): (Pg 33-34) For those who just joined us today we are discussing abusive spouses. We have our last caller on the line.

CALLER: I want to know how I can talk to my husband when he gets angry.

RADIO (VOICE OVER): How long has he been abusive?

CALLER: He tells me if I did whatever he asked he wouldn’t have to hit me. But I do what he says and it’s still not good enough. Last time he hit me because . . .

CARMEN: Pobre mujer, I’m lucky mi viejo doesn’t hit me.

ANA: Lucky? That woman should leave her husband.

PANCHA: You think it’s that easy?

ANA: No, she’s probably dependent on him financially, or the church tells her to endure, or she’s doing it for the children. But we can’t allow ourselves to be abused anymore. We have to realize that we have rights! We have the right to control our bodies. No more!

CARMEN: (Pg 57) When your Apa would leave me in Mexico to go to el norte, he would leave me pregnant so no man would look at me and desire me. I was always scared of him. And I let myself get fat after you were born hoping he would be disgusted by me and not touch me anymore.

ANA: Why didn’t you just say “No.”?

CARMEN: Because, M’ija, I was never taught how to say no. (beat, change of subject) (Pg 12) give me your secret, Rosali. Maybe this way I can lose this ball of fat! (She squeezes her stomach) You can’t even see my waist anymore. (Ana laughs) Why do you laugh? You’re getting there yourself. When I was your age, I wasn’t as fat as you. And look at your chichis! They must wight five pounds each! (Pg 58) Why don’t you lose weight? Young girls should try to make themselves as attractive as possible.

ANA: Why? You’re overweight too.

CARMEN: But I’m already married.

ANA: Is that it? Make myself attractive so I can catch a man?

ESTELA: (sarcastically) Ana, listen to them, learn now, “or you’ll end up like Estela.” (Pg 59) I want to be taken seriously, to be considered a person. With Andres, on our date . . . I got all fixed up. (twirls) He said, “I don’t care if you’re fat. I like you even better; more to grab.” That got me so angry! I though he was interested in me because he was impressed that I owned this factory. That “I’m smart” . . . When am I going to meet that man who will see the real me?

ROSALI: I’ve felt fat ever since I can remember.

ESTELA: Rosali, you’re not fat.

ROSALI: Of course, I am. Look at my nalgas . . .and my hips! I look like a cow. RADIO (VOICE OVER): (Pg 41) The time now is 2:35 pm. Twenty illegal aliens were captured today at the Goodnight Pillow Factory.

PANCHA: That’s only a few blocks away!

RADIO (VOICE OVER): The owner was fined up to 2,000 dollars per alien . . .

CARMEN: Estela, call the Glitz company and ask them, no, demand that they pay you for the last order of dresses. Even if they were late, they still have to pay us.

ESTELA: I don’t want to be too pushy. They’re the only company that has been willing to give us a contract.

CARMEN: Then do it for Pancha and Rosali. You haven’t paid them and las pobrecitas can’t even buy groceries.

ESTELLA: (She thinks about it, then decides to be brave and do it) (Pg 42) Hello, this is Estela Garcia . . . No, but we’re almost finished. I know . . . I know. . . I’ve got a lawyer working on that . . . I’ll get it to you by next week . . . Okay, Mrs. Glitz . . . I’m sorry. (she hangs up, her face expresses worry and fear)

CARMEN: Que te dijo la vieja?

ESTELA: She asked about my proof of employment papers again. She warned me that if la migra shuts us down, she won’t pay us for all the work we’ve done. I’m going to get deported. I’ll lose everything I’ve worked for, the factory . . . my self-respect.

PANCHA: (Pg 56) How many more dresses to finish, Estela?

ESTELA: Fifteen (counting dresses on the rack) 184, 185, 186. We only need 14.

CARMEN: (Pg 61) (and suddenly Carmen has a idea) Estela, I’ve been thinking . . You know what we could do? We could copy the patterns for these dresses and make the dresses for ourselves.

ROSALI: Jaime could sell them in the flea market!

ANA: That’s a great idea! Why don’t we make them in larger sizes too?

PANCHA: We could probably sell more if we made them in larger sizes.

ESTELA: And from there, if we make more money than what we’re making now, maybe we can rent a place downtown and start a boutique!

PANCHA: You could go to school and study fashion design and design our dresses!

ESTELA: I could do that . . . (She grins) (Pg 64) Large sizes?! (she picks up a measuring tape and begins taking her own measurements)

SPOKEN TRANSITION - The women head home for the day, but not Estela – She works through the night – and the next day . . .

ESTELLA: (Pg 67-68) (with new-found determination she dials the phone) Mrs. Glitz? This is Estela Garcia. I wanted to tell you that you are a mean, wicked, unsympathetic, greedy, rude. . . Capitalist! We quit . . .

CARMEN: What have you done?

PANCHA: You got us fired, didn’t you?

ESTELA: No, we quit! (Estela laughs) Don’t worry. I got us a contract with Senor Vasquez!

ANA: (Pg 69) (steps out of scene to speak to audience) As for me . . . I wrote an essay on my experience and was awarded a fellowship to New York University! (beat) I always took their work for granted. I was going to be better than them. I wanted to show them how much smarter and liberated I was. But in their subtle ways, they taught me about resistance. About a battle no one was fighting for them except themselves. About the loneliness of being women in a country that looks down on us for being mothers and submissive wives. With their work that seems simple and unimportant, they are fighting… Perhaps the greatest thing I learned from them is that women are powerful, especially when working together. [When I came back from school] plans for making the boutique were no longer a dream, but a reality. (She picks up a jacket and puts it on) Now I wear original designs from Estela Garcia’s boutique, “Real Women Have Curves.”
```

---

## IC-0249: ReBirth

- Title: ReBirth
- Author (byline): Lisa Soland
- Work: One on One: The Best Women’s Monologues for the 21st Century
- Publisher: Applause Theatre and Cinema Books
- Publication date as stated: October 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SCENE, TIME, DORIS
- Teaser before the introduction: Yes
- Spoken words (computed): 1445
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lisa Soland
Book: One on One: The Best Women’s Monologues for the 21st Century
ISBN: 1557837007
Publisher: Applause Theatre and Cinema Books
Date(Month/Year): October 2007
```

### Introduction (context only: never use it for content warnings)

```text
The population of the United States is aging rapidly. More and more Americans are facing retirement, dealing with social security concerns and end-of-life issues. Although we don’t like to think about it, each of us has a terminal condition.. Some have five weeks, others decades. But every one of us has only so much time to live. Coming to terms with your own death puts life in perspective. You see more clearly what’s important and what’s not. As a result, you are more likely to focus on values and goals close to your heart. Surprisingly, you may even find that you feel calmer and more alive. The process is one that Lisa Soland calls “Rebirth”
```

### Performance text (classify this)

```text
A 76-year-old widow from Boston, DORIS carries a shopping bag and purse. She is spunky, thoughtful and, at times, humorous.

SCENE: A congressional hearing room in Washington, D. C. The audience represents the committee.

TIME: The present

DORIS: You want to know how many people I don't feel like a "little old-lady" with? None. Not a single one. So I went. I went. And I went.

(Beat) They called it "The Rebirth." And I thought, "Well, good. That's just what I need because all of my life I've seen endings. A rebirth would be nice for a change." My husband - Max Junior...? Not that he was much of a junior, in fact, if you'd seen him in the private places a marriage tends to allow two people to see each other. . . (Suddenly) Well, he died you know. Just up and died. Sleeping peacefully one night, so peacefully I looked at him, his face right beside mine so closely, so closely that I noticed there was no more air coming out of his nose. That big, beautiful, hairy nose and no more air. What a panic.

(DORIS crosses to table.) My mother's death-quiet, too, on the outside. Not so quiet on the inside. Cancer.

(Places purse on table then takes hanky out of sweater pocket and blows nose) I thought my parents would never die, says the old, gray-haired woman... (Patting her hair back into place) ... which I thought would never be gray. Youth. Ha! A little bottle of Clairol can go a long way.

(SHE spots SAMUEL’S tie on table and rolls it up neatly.) I promised my husband he would never be married to a gray-haired woman and I plan to keep that promise.

(To audience, proudly) I'm 76.

(Singing, and miming playing the trombone) "Seventy-six old bones lead the big parade!" And I can't tell you how that happened either. I lost track of the last 50. Gone, like the 50 pounds my mother lost before she left me. (Really asking these questions) Where does it go? The 50 years? The 50 pounds? Where did she go? Like light. When it turns dark, where does the light go? Well, these 76 old bones can tell you through experience that when it's dark here, it's light somewhere else and soon, very soon, it gets light again.

(DORIS sits in chair) Death. I was always afraid of it, you see. Because I'll be last. When you're first, you're okay, because you're leaving those you know. You've got them all around you and you're leaving them. They're pretty much screwed but you... I imagine you're okay. But when you're last, you don't know anyone anymore. They've all died, so you leave alone and you enter. . . what? And you don't know if anyone's going to be there either. I mean, you read the books. They say you go through some tunnel and you leave the dark and go towards the light, some blinding light, but what if no one's there waiting for me?

(Beat) Sometimes I imagine my mother there, with her calico apron on, telling me to soak my grape nuts before I eat them so I won't crack my teeth. And I wonder about Max?

(Beat) It's been so long I would think their souls would have all moved on by now. (Feeling her loneliness.) No one I know will be there.

(Rising, SHE moves to edge of chair and mimes being her mother) My mother's spirit is probably off working on the United Nations council, passing thoughts about crunchy cereal into the shallow minds of our world leaders.

(SHE shrugs) Who knows? (Beat) In my breath work session, I became a star up in the sky. And I realized that that's all they were, we were, is bright light, all ashine, bursting into massive expansiveness. I felt very free and peaceful and aware that Max's death was nothing but that-a passing into expansiveness. From his big, hairy nose to the sky in one, short breath.

(After a thought)

I guess that can be kind of scary if you're not ready. Leaving what you know, to go . . . where?

(Really asking the audience) Where? I have no grandchildren. Imagine that. I look like a Hallmark greeting card and I have no grandchildren. The odds were against me seeing as I had no children. (Crosses to purse on table) I did actually, but she disowned me. (Beat) No, I disowned her. (Gets wallet out of purse and shows photo of daughter to audience.) Here. See? She was stubborn. Stubborn as a one-eyed mule. You can spot it in the eyes. Just like her father. (Shows photo.) She kept telling me that she could never burden me with the raising of her child. I said, "What? Your child?! What makes you think it's yours? Maybe it's mine, given to you. Through you. Meant for me but given to you." She said that she was going to abort it. That she had no choice. So I have no grandchildren. (Closes wallet and puts it back in purse.) I don't mind leaving nothing behind, really, it's not leaving with anything that bothers me. (DORIS sits on edge of stage.) After the tour of the stars, my mind seemed to settle on one, particular incident that actually happened to me, in real life, when I was nine. But I got to re-live it all again, speeding before my mind like a three-dimensional hologram. (Beat) I used to love to climb this one particular tree, down the hill behind our farmhouse. I think it was a walnut tree. (Thinking.) Yes. (Becoming the tree with her arms.) It had the type of limbs that swooped way down near the earth but it was also very tall. Very tall. When I climbed, I felt as though I were getting nearer and nearer to heaven. (DORIS rises and, becoming the little girl, SHE starts to climb.) One day I was feeling very rambunctious, so I tried a branch that any other day I would have passed by. I just had to go a little bit further. I wrapped my fingers around it and began to pull my little 62-pound body upwards, towards the sky. Mid-way, I saw a little, tiny crack starting to form in a place of the branch that mattered. I was aware that it was about to give way and it sure enough did. I fell. My mother's warnings flashed through my mind and I wished I'd listened to her just this one time' cause I was a good five stories about the ground. (To audience) Now, this is the part I didn't remember until the breath work. I must have blocked it out or something, but I knew I was going to hit hard, so I left. I left my body. And right then, as I made that instant decision, I reached my hand upwards, and there was my father, reaching down out of heaven. (To audience) I hadn't seen him in years. He had died of liver disease when I was six but here he was catching me, midfall. I smiled at him and he asked me in his mind, without speaking, why I hadn't listened to my mother. I told him that she often tried to keep me from doing things that I had an enormous curiosity about. Without speaking again, he said that I would now have to make my own decisions in life, about what was safe and what was not. And I cried. (A very bright light slowly comes up full on DORIS.) I remember crying but not because of the fact that I was now going to have to grow up, but because my father was lit up like a candle on Christmas Day, so bright I could hardly look at him. (Becoming the child again.) All the stories my mother tried to paint for me about him throwing things, drinking, could not have possibly been true' cause there was my daddy. He was there, in heaven. (Continuing the story) He cradled me in his arms and pointed to the ground below, where my physical body lay, knocked out flat and said, "You've got your whole life waiting for you down there. Are you ready for it?" (Beat) I wrapped my legs around his stomach and the next thing you know, I'm lying on the ground with a splittin' headache that could have killed a plow horse. (Poignantly) My mother died later that same month. (Beat.) That was my first experience with this light when I was six and I got to remember it in my breath work. The same light that surrounded my father that day will lead me down that tunnel. But not because I'm going to fall from a tree... (Plainly to audience.) ... because I'm going to die. (SHE gathers her purse and shopping bag.) Well, I'm old and that's the way life is. People don't want to hear it, but it's true. Despite all my positive thoughts on the subject and Deepak Chopra... I am still going to die. Not quite yet, however. Part of me thinks it sucks and part of me accepts it. And I bounce back and forth between the two about 76 times a day. (Singing and miming playing the trombone.) “76 old bones..." I have noticed however, since I've been doing these sessions that I accept it more times than naught. And that's a real blessing. (Crossing downstage to audience.) Spending time with you young people helps too, because you have so much life in you-so much...living left to do that it reminds me of dying. Sounds like a dichotomy, doesn't it?
```

---

## IC-0250: Rodeo from Talking With

- Title: Rodeo from Talking With
- Author (byline): Jane Anderson
- Work: Talking With
- Publisher: Samuel French, Inc.
- Publication date as stated: April 1983
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BIG EIGHT
- Teaser before the introduction: Yes
- Spoken words (computed): 1146
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Anderson
Book: Talking With
ISBN: 978-1880399200
Publisher: Samuel French, Inc.
Date (Month/Year): April 1983
```

### Introduction (context only: never use it for content warnings)

```text
Rodeos started as a form of entertainment and show of expertise among horse-owners. In the beginning, riders’ skills were truly tested -- Those who performed well were respected for their skills by their peers and the audience. In Rodeo by Jane Martin, Big Eight understandably laments the loss of the early days of Rodeo when players performed for the sake of pride and not for earning money or gaining popularity. Rodeo from Talking With by Jane Martin.
```

### Performance text (classify this)

```text
A young woman in her late twenties sits working on a piece of tack. Beside her is a Lone Star beer in the can. As the lights come up we hear the last verse of a Tanya Tucker song or some other female country western vocalist. She is wearing old worn jeans and boots plus a long-sleeved workshirt with the sleeves rolled up. She works until the song is over and then speaks.

BIG EIGHT: Shoot - Rodeo's just goin' to hell in a handbasket. Rodeo used to be somethin'. I loved it. I did. Once Daddy an' a bunch of 'em was foolin' around with some old bronc over to our place and this ol' red nose named Cinch got bucked off and my Daddy hooted and said he had him a nine-year-old girl, namely me, wouldn't have no damn trouble cowboyin' that horse. Well, he put me on up there, stuck that ridin' rein in my hand, gimme a kiss and said, "Now there's only one thing t' remember Honey Love, if ya fall off you jest don't come home." Well I stayed up. You gotta stay on a bronc eight seconds. Otherwise the ride don't count. So from that day on my daddy called me Big Eight. Heck! That's all the name I got anymore . . . Big Eight.

BIG EIGHT: Used to be fer cowboys, the rodeo did. Do it in some open field, folks would pull their cars and pick-ups round it, sit on the hoods, some ranch hand'd bulldog him some rank steer and everybody'd wave their hats and call him by name. Ride us some buckin' stock, rope a few calves, git throwed off a bull and then we'd jest git us to a bar and tell each other lies about how good we were.

Used to be a family thing. Wooly Billy Tilson and Tammy Lee had them five kids on the circuit. Three boys, two girls and Wooly and Tammy. Wasn't no two beer rodeo in Oklahoma didn't have a Tilson entered. Used to call the oldest girl Tits. Tits Tilson. Never seen a girl that top-heavy could ride so well. Said she only fell off when the gravity got her. Cowboys used to say if she landed face down you could plant two young trees in the holes she'd leave. Ha! Tits Tilson.

Used to be people came to a rodeo had a horse of their own back home. Farm people, ranch people -lord, they knew what they were lookin' at. Knew a good ride from a bad ride, knew hard from easy. You broke some bones or spent the day eatin' dirt, at least ya got appreciated.

Now they bought the rodeo. Them. Coca-Cola, Pepsi Cola, Marlboro damn cigarettes. You know the ones I mean. Them. Hire some New York faggot t' sit on some ol' stuffed horse in front of a sagebrush photo n' smoke that junk. Hell, tobacco wasn't made to smoke, honey, it was made to chew. Lord wanted ya filled up with smoke he would've set ya on fire. Damn it gets me!

There's some guy in a banker's suit runs the rodeo now. Got him a pinky ring and a digital watch, honey. Told us we oughta have a watchamacallit, choriographus or somethin', some ol' ballbuster used to be with the Ice damn Capades. Wants us to ride around dressed up like Mickey Mouse, Pluto, crap like that. Told me I had to haul my butt through the barrel race done up like Minnie damn Mouse in a tu-tu. Huh uh, honey! Them people is so screwed-up they probably eat what they run over in the road.

Listen, they got the clowns wearin' Astronaut suits! I ain't lyin'. You know what a rodeo clown does! You go down, fall off whatever-the clown runs in front of the bull so's ya don't git stomped. Pin-stripes, he got 'em in space suits tellin' jokes on a microphone. First horse see 'em, done up like the Star Wars went crazy. Best buckin' horse on the circuit, name of Piss 'N'Vinegar, took one look at them clowns, had him a heart attack and died. Cowboy was ridin' him got hisself squashed. Twelve hundred pounds of coronary arrest jes fell right through 'em. Blam! Vio con dios. Crowd thought that was fun-nier than the astronauts. I swear it won't be long before they're strappin' ice-skates on the ponies. Big crowds now. Ain't hardly no ranch people, no farm people, nobody I know. Buncha disco babies and dee-vorce lawyers - designer jeans and day-glo Stetsons. Hell, the whole bunch of 'em wears French perfume. Oh it smells like money now! Got it on the cable T and V-hey, you know what, when ya rodeo yer just bound to kick yerself up some dust- well now, seems like that fogs up the ol' TV camera, so they told us a while back that from now on we was gonna ride on some new stuff called Astro-dirt. Dust free. Artificial damn dirt, honey. Lord have mercy.

Banker Suit called me in the other day said "Lurlene. . ." "Hold it," I said, "Who's this Lurlene? Round here they call me Big Eight." "Well, Big Eight," he said, "My name's Wallace." “Well that's a real surprise t' me," I said, "Cause aroun' here everybody jes calls you Dumbass." My, he laughed real big, slapped his big ol' desk an' then he said I wasn't suitable for the rodeo no more. Said they was lookin' fer another type, somethin' a little more in the showgirl line, like the Dallas Cowgirls maybe. Said the ridin' and ropin' wasn't the thing no more. Talked on about floats, costumes, dancin' chor-eog-aphy. If I was a man I woulda pissed on his shoe. Said he'd give me a lifetime pass though. Said I could come to his rodeo any time I wanted.

Rodeo used to be people ridin' horses for the pleasure of people who rode horses-made you feel good about what you could do. Rodeo wasn't worth no money to nobody. Money didn't have nothing to do with it! Used to be seven Tilsons riding in the rodeo. Wouldn't none of 'em dress up like Donald damn Duck so they quit. That there's the law of gravity!

There's a bunch of assholes in this country sneak around until they see ya havin' fun and then they buy the fun and start in sellin' it. See, they figure if ya love it, they can sell it. Well you look out, honey! They want to make them a dollar out of what you love. Dress you up like Minnie Mouse. Sell your rodeo. Turn yer pleasure into Ice damn Capades. You hear what I'm sayin'? You're jus' merchandise to them, sweetie. You're jus' merchandise to them.
```

---

## IC-0251: Roe

- Title: Roe
- Author (byline): Lisa Loomer
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: Sept 2019
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SARAH, LINDA, FLOWERS, FLIP BENHAM, RONDA, NORMA, AILEEN, JUDY, DOCTOR, TOGETHER, MCCLUSKEY, JUSTICE BLACKMUN, NORMA AND SARAH, PRO-LIFE WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1781
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lisa Loomer
ISBN: 978-0822238010
Publisher: Dramatists Play Service
Date (Month/Year): Sept 2019
```

### Introduction (context only: never use it for content warnings)

```text
Roe v Wade is not just a case. It’s not just a ruling. This is what happens when a country argues over who gets to choose and who must pay the price. Roe by Lisa Loomer
```

### Performance text (classify this)

```text
SARAH: (Pgs 11-13) (Lights come up on Sarah Weddington, early 70s) Good evening. My name is Sarah Weddington. I was the lawyer who argued Roe v. Wade. (From Loomer’s revised Prologue 2022) And tonight, I deliver its obituary. (with great passion) Every day new abortion laws are written in our country. But all of these laws tell a woman the same thing: You have no right to control over your own body. We, the government, have that right. We have the right to cause you economic or psychological harm . . . We will incarcerate any doctor who seeks to help you . . . And we don't care if you were incested or raped. (pained) You know, I always wonder . . . We argue about Roe, some of us vote solely on this issue . . . But how many of us even know what was said in the case? Well, I'd like to tell you the story of Roe. And since history is the result of shared experience. . . And is a reflection of multiple points of view -- that are affected by race, religion, gender, sexuality, and class . . . I think it's essential that all persons involved in Roe be here to testify!

LINDA: (passionately) Linda Coffee for the plaintiff -- the truth is, it's about choice!

FLOWERS: (outraged) Robert Flowers, representing the great State of Texas -- it's about murder pure and simple-

FLIP BENHAM: Flip Benham, head of Operation Rescue -- the truth is, it's not your body, so it's not your choice!

RONDA: Can you see the little hands, the precious feet? Suddenly, the one woman who has not spoken, lets out a whistle, and the others fall silent. Norma, 69, steps forward to the audience.

NORMA: Hey, y'all, I'm Norma McCorvey. I was the plaintiff. I Am Roe! (Sarah looks at Norma. Norma looks at Sarah and smiles) Well, sugar, how 'bout this? How 'bout you tell your story, I tell mine?

SARAH: (after a beat; with dignity) Norma? As long as we get to the truth? Fine.

NORMA: (Pg 14-15) Okay y’all, Dallas, 1970. I was a bartender at the Red Devil – Oh – did I mention this was a Girls’ Bar? (begins to serve drinks to a woman sitting at the bar) Aileen!

AILEEN: You seen your doctor?

NORMA: Know what that doctor told me? “See a lawyer.” Adoption lawyer. [But] I was workin’ the bar tonight, talkin’ to a customer, know what she told me? Did you know there is a way for me to be not pregnant, Aileen?

AILEEN: (laughs) You never heard of an abortion?

NORMA: Where I come from? Louisiana? A voodoo woman gives you something to drink, says some mumbo jumbo . . . didn’t work when my mom got knocked up with me, so how would I know? Can you give me the name of a doctor?

AILEEN: Not that kind of doctor. It’s against the law.

NORMA: You’re a nurse, Aileen – All I’m askin’ for’s a name! (steps out of scene to speak to the audience) (Pg 16) And while I was raisin’ hell in Dallas . . .

SARAH: In Austin . . .

JUDY: (Pg 19) Sarah has been doing legal research for an underground referral service so women can get safe abortions and steer clear of the back-alley guys.

SARAH: We’ve all heard the horror stories about illegal abortion. 5,000 women dying a year!

JUDY: We all agree the law has to change. And in order to do that in Texas, someone has to challenge the law that makes abortion illegal. I think that should be Sarah.

SARAH: Are you crazy? I’m only a couple years out of law school! I’ve never tried a contested case!

NORMA: (Pg 37) (interjects from the sidelines) Your first case? Gee, no one bother to tell me!

SARAH: (Pg 20-21) (beat) Look, I know you’re right, Judy, someone should do this . . . (with increasing emotion) I met a girl last week. Willa. Fifteen. She took a bus to Dallas, was met by a guy who blindfolder her and drove her to a man who did abortions in his basement. $800 at the door. He ordered her to take off all her clothes and lie down on a table. (beat) He raped her. And she felt that, if she wanted the abortion, she’d better just let him. She was fifteen! No anesthesia. He inserted a coat hanger, jabbing it around till he pierced the fetal sack. (continues with passion) And some women just do it themselves! Lysol, turpentine, telephone wire, broken Coke bottles. No woman should have to go through these things!

JUDY: You just argued yourself into taking the case. ***** Doctor’s Office*****

NORMA: Look, I been to a place in Oak Cliff. Blood all over the floor, roaches . . . And the smell.

DOCTOR: (patiently) Norma, I believe I told you “no” on the phone.

NORMA: You delivered both my babies, you had plenty of business offa me. If you can’t do it, gimme the name of someone who can.

DOCTOR: Maybe you should have thought about consequences before you got pregnant for a third time? I am not in the business of killing babies! Shame on you for even – do you understand that any doctor who would do such a thing would go to jail? Either raise this baby yourself (with disdain) as an unmarried woman or find your child some decent parents. **** Pizza Parlor *****

TOGETHER: (Pg 24-27) (to audience) And the first meeting on Roe v Wade took place in Columbo’s Pizza Parlor on Mockingbird Lane.

NORMA: in Dallas.

SARAH: (to audience) Linda Coffee was in my class at law school, and I knew I’d need a huge amount of help. (greeting Norma) Hi! You must be Norma! I’m Sarah Weddington. So glad to meet you! (she notices the bandanna wrapped above one of Norma’s knees) I like your bandanna.

NORMA: Oh, that just means I don’t have a girlfriend. (enjoying this) I’m a lesbian?

SARAH: Of course. How many months pregnant are you, Norma?

NORMA: Uh, ‘bout two and a half?

LINDA: (steps out of scene) I’d just like to say something about “history” here. We want to give a fair account of what happened here. Norma, in her book, says she was 2 ½ months pregnant. And Sarah, in your book, it was more like 4 . . . Well, how pregnant was she?

SARAH: You were at least 4 months –

NORMA: 2 Months! (to audience) Alternative facts –

LINDA: (to audience) My point is that it’s really hard to talk objectively about history, about the “truth.” Let’s continue.

SARAH: (Pg 28) Do you have family?

NORMA: Got a mother! But we never been close (laughs) Hell, I though my name was “Ugly Stupid” ‘fore I knew what the wors meant. I still can’t do nothin’ right for that woman. And I tried ‘cause she’s got my daughter –

SARAH: You have – a daughter?

NORMA: Melissa. She’s five.

SARAH: I see. And you say your mother has custody?

NORMA: I say my mother stole Melissa. Told me she was gonna put my baby on her health insurance. Next thing I know: “You got five minutes to pack up your shit ‘cause you just gave up your daughter.” (awkward pause)

SARAH: (Pg 30) We need a pregnant woman who wants an abortion to challenge the Texas Law. Do you want an abortion, Norma?

NORMA: Well, yeah! I’m not here for the pizza!

SARAH: You wouldn’t have to use your own name. Usually, people use “Jane Doe” but there’s a Mary Doe in a related case, we could use . . . Jane Roe? You wouldn’t even have to appear in court.

NORMA: So I’m Jane Roe? And then I could get my abortion?

SARAH: (beat, carefully) Norma. The law takes time I can only promise you that we will do our best. (both step out of scene and speak the audience)

NORMA: (Pg 32) She let me believe I could get my abortion.

SARAH: Norma McCorvey was in her second trimester when we met. She became a plaintiff in the case so that future generations of women would have the right she was denied. (Norma starts to pound her very pregnant stomach)

MCCLUSKEY: (Pg 33) (to audience) Despite her efforts to self-abort, Norma gave birth that summer. (Pg 22) [I’m] Henry McCluskey, a lawyer who specialized in adoptions and, like Norma, also gay. People like us generally hid their sexual orientation in those days.

NORMA: (Pg 34) (deadened; to no one) They gave me a shot to dry up my milk. But the nurse f***ed up and brought it to me at feeding time. (pained she turns away)

MCCLUSKEY: (taking the baby in his arms) I arranged the adoption – a closed adoption. No one’s heard anything about the child known as the Roe Baby since. (beat) Oh – it was a girl. *******

SARAH: (Pg 41) (to audience) Finally . . . October 1972 – (Pg 46) the *Supreme Court* sent the decision. . .

JUSTICE BLACKMUN: (Pg 49) (to audience) Justice Harry Blackmun. According to my obituary, I would receive hate mail for the rest of my life. (Pg 48) (turns to the order at hand – the Supreme Court’s ruling) The Court has recognized that a right of privacy does exist under the Constitution. And is broad enough to encompass a woman’s decision whether or not to terminate her pregnancy.

SARAH: (reading the ruling in her office) Yes!

JUSTICE BLACKMUN: Each state may also properly assert important interests in protecting potential life.

SARAH: (to Blackmun) To be clear . . . the fetus is “potential” life?

JUSTICE BLACKMUN: The compelling point is viability. When the fetus has the capability of life outside the mother’s womb. The state may prohibit abortion, from the second trimester on except when it is necessary . .

SARAH: (reading) “To preserve the life or health of the mother.” (To Blackmun) Damn! State regulation could be a big problem in the future!

JUSTICE BLACKMUN: The word “person,” as used in the 14th Amendment, dos not include the unborn. (exits)

NORMA: (Pg 49) (with wonder) They passed that law – that Roe versus Wade?

NORMA AND SARAH: (Norma speaks it to herself, Sarah aloud) The right to choose is the law of the land!

SARAH: (to audience, triumphant) And that was the case. Now let’s talk about what’s happened to the law since. (Pg 50) The 80s – Reagan says he wants to “rectify the tragedy of Roe v Wade.” He says that, over his dead body will a pro-choice Judge ever be appointed to the Supreme Court.

NORMA: (Pg 51) I see all them college-girl feminists on the TV going on about Roe? I mean, shit I am Roe – and I never got nothin’ out of it, not an abortion, nothing’!

FLIP BENHAM: (Pg 56) (to audience) Flip Benham, Head of Operation Rescue. (turns to confront Norma) (Pg 66) Norma McCorvey? How does it make you feel that 35 million babies have died because of you? (Pg 67) Only sin will prevent you from entering the Kingdom of God, Miss Norma.

NORMA: That what you Rescuers told that abortion doctor in Florda ‘fore you put a bullet in his head.

RONDA: (Pg 68-69) (outside an abortion clinic, perhaps holding a picket sign; introduces herself to audience) Ronda Mackey – Operation Rescue volunteer. (steps in front of a woman headed to an abortion clinic) Oh, hon, you don’t want to go in there. Let me show you something (shows photos) This is a 9-week-old baby. He’s smiling, can you see that. (vehemently) No one could tell me that this was a “fetus” and not a human being. Hon. . . Your child is a gift! *******

SARAH: (Pg 70) Decades ago, the Supreme Court gave American women the legal right to choose. But the fate of Roe depends on who is on the Supreme Court at the time.

PRO-LIFE WOMAN: (Pg 89) You liberals – the same folks who stood in front of schools to protest segregation, to protect the rights of black children? Can’t you see where’ standing in front of clinics to protect the rights of all babies.

SARAH: If abortion goes against your beliefs, don’t have one! Just don’t try to force your beliefs – and your choice – on everyone else.

PRO-LIFE WOMAN: (Pg 90) A child is not a choice!

SARAH: (Pg 94-95) In 2016, a pro-choice woman ran for president. Won the popular vote. . . and lost the election. In 2018, a president who’s vowed to overturn Roe made his second appointment to the Supreme Court.

NORMA AND SARAH: No matter what else I have done with my life . . . My obituary will always read

SARAH: (Proud) She was the lawyer who argued Roe v Wade!

NORMA: (Broken) She was Jane Roe.

SARAH: As for the law itself? . . . . CLOSING

TOGETHER: On June 24, 2022, the U.S. Supreme Court eliminated the constitutional right to obtain an abortion -- casting aside 49 years of precedent that began with Roe v. Wade.
```

---

## IC-0252: Ronald Reagan Hates Your Ugly Mother

- Title: Ronald Reagan Hates Your Ugly Mother
- Author (byline): Carl Sasoon
- Work: Fast Horse Plays, Round 4
- Publisher: Fast Horse Drama
- Publication date as stated: Aug 2012
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: WOMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1765
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carl Sasoon
Book: Fast Horse Plays, Round 4
ISBN: 978-0615711379
Publisher: Fast Horse Drama
Date (Month/Year): Aug 2012
```

### Introduction (context only: never use it for content warnings)

```text
Tourette syndrome is a condition that affects the brain and nerves, causing people to make repeated movements and sounds that they cannot control. The symptoms usually begin in childhood and will normally become less severe as one enters adulthood. But in 10-15% of cases, the tics become even worse. These attacks can be severe, disabling and last from 15 minutes to several hours. And those minutes can change your life.

Ronald Reagan Hates Your Ugly Mother by Carl Sasoon
```

### Performance text (classify this)

```text
The woman is in her mid-twenties or so, verbal, a crowd-pleaser and trying desperately to be funny. Her speech and body are characterized by Tourette's Disorder- her speech is interrupted by vocal tics as indicated by bold italics. She is often plagued by motor tics as well, eye blinking, and uncontrollable head, shoulder, hand and body movements.

WOMAN: Okay, nice crowd. Full house, it looks like. And I'm sure that you're all ready to laugh, which is good news, because I'm pretty funny . . . looking. Ha. Okay. Don't hold back on my account.

See, the first time I went in to see a psychiatrist, I told him, "Doctor, I am so depressed and lonely. No one will talk to me, everyone just runs away because I'm so funny looking. Can you help me?" And he says, "Sure I can! Just come over to this coach and lie face down. Okay. Problem solved."

So, a few weeks later I call him back up because I'm really worried about my daughter, right? And so he tells me to stop stressing out so much and he puts me on tranquilizers. I go back in to see him a couple of weeks later and I tell him that I'm feeling much better. Much calmer. And he says, "How's your daughter?" And I say, Who cares?"

Two guys walk into a bar and there's maggots crawling through your filthy brain. Two guys walk into a bar and one giddy-up, giddy-up, giddy-up! Ahh . . . that joke wasn't very funny. I never get to the punchline anyway.

WOMAN: So, here's the thing. You can't take it personally. With Tourette's, the tics just come out of nowhere, anytime, anyplace, anywhere ... with anyone. So, even if I happen to call you "the son of a bleeding donkey" or a "toilet licker," well, it's not you, it's me. It really is. The "toilet licker" one came out about twenty-five times the very first time I met my mother-in-law.

Tourette's. Not responsible. It's not like I even have to plan a whole evening of jokes, because I can be really funny without even trying. People don't really understand Tourette's Syndrome. That's the problem. They think it's some crazy on the bus who screams four-letter words all day long, uncontrollably. Actually, you scream and whisper and shout all kinds of things all day long. And, as an extra bonus, your body freaks out and does weird crap all the time. And- wait for it- there's no cure! Nice. Really, nice.

They say that as many as three percent of the world's population may have Tourette's, which I find really strange, because the other ninety-seven percent is sure a whole lot of people. I feel like I've met a lot of people, but, let me tell you, that three percent, they must all be hiding or something. Any of you? Huh? Sir, you look like you gremlins crap on the heads of broken grandmas, bozo-breath, might be a three-percenter, you think?

My husband was definitely part of the ninety-seven percent. Yes, past tense.

Was. No, he's not dead. When he told me that he was leaving me, I said, "Julius Caesar pasted wall-paper to your brain”, and he said . . . nothing, for quite a while. He was just very quiet. We sat there in the silence in the dark and, uh, I was really grateful for our refrigerator, of all things. Because instead of listening to that awful sound of the silence, I listened to the damn humming of that refrigerator. And it was comforting. Coldness comes in like black death and vomit. And when I started to cry, I turned away from him, because I did not want him to see. And when he did speak he talked a lot about how hard he had tried and that it wasn't that he didn't love me, and I guess, it just sounded like a lot of nonsense to me. Is that selfish? I don't mean it to be. Because, if he was trying, then what did he think I was spending every moment crayons are so delicious in the summertime of my life doing? Trying to control...this. You spend your life trying. You do. And you just can't run fast enough to get out in front of it. It always wins. And I just kept listening to that damn refrigerator and he just kept talking. He did say that he would "allow" me to see my daughter. That was how he said it. "Allow me." How kind of him.

Sorry. This has been a real downer. So, another guy goes to the psychiatrist and he says, "My wife thinks she's a chicken. Can you help us?" And the Psychiatrist asks how long this has been going on. And the man says, "About two years." And the Psychiatrist asks why it's taken them so long to get help. And the man just shrugs and says, "We needed the eggs." Chicken? Eggs? The woman .. headlights take you straight to hell. The headlights take you straight to hell. Hell to headlights. Headlights. Headlights. No no no no no no no no. Old MacDonald had a farm and then he goes to outer space and eats all of Aunt Edna like a gummy bear. No no no no no. They call that a . . . fit. A tic fit. Hysterical, huh? It's like your body gets stuck and the tic just replays on a loop. It's like you're trapped. Watching yourself from the outside or something but you cannot stop. That was a short one. They can last fifteen minutes. An hour, even. I'm on a medication that's supposed to help control them, make them less severe.

So, uh, my daughter. She's wonderful. Just wonderful, really. So healthy, so . . . well. She was the one who told me that it was okay to laugh about my "oogly booglies." That's what she named them and I just thought that was so cute, you know? And I just thought that for a six-year-old to have that sort of maturity my little pony rides off into the sunset and then you'll go to sleep forever and awareness. And so, you see, being a mother is everything to me. Because it meant I could be normal. I could be part of the ninety-seven percent. It didn't matter that the rest of the world thought I was crazy, because I had someone who needed me. . . who loved me and wouldn't leave me.

And, you see, I had been doing so well. I hadn't had a fit in . . . months, probably. The new medication was working and uh, she had been with me for the weekend. I didn't usually drive her, but my, ex-husband had a flat tire, and I was doing so well, I mean I had been driving again, for months, you see and it wasn't far. This was last winter and the weather was awful Peter Piper is an ugly son of a serial killer and I was nervous, but I knew that I could do it. I knew it would be just fine. We were about half-way there when I felt it coming. Like feeling a sneeze that's corning, I think, or an itch that you have to scratch or you'll just go crazy. And so, I pulled over, onto the side, like I know to do, and my daughter, she knew too. She said, "Mommy, the oogly booglies are corning. I love you."

And, you see, I had a fit. A very bad you should choke a chicken with a death hammer fit. And it just kept going, like it was going to last forever. And she was watching me, my daughter was. And I could see in her eyes how scared she was, me screaming and my body flailing around like that, but I could not help myself. I could not stop. And, uh, so, she told me she was going to get help, that we needed help and I was shaking my head as best as I could, but I watched her, like I was paralyzed, and I watched her hand open the door handle of the car and I watched her get out, and I could not stop her, I couldn't, I would have, dumb little bumblebee, stings you in your black heart, you know that I would have, but, uh, the car did not see her. Couldn't see her in the dark, with the snow.

And my fit ended, and she was lying there so still. And I held her, and I sang to her, just like I did every night. Because we were just like normal people when I sang to her and I would make everything alright. Everything would be just fine. "Hush little baby, don't say a word. Mama's gonna buy you a mockingbird. And if that mockingbird won't sing ... " But everything was not fine. And there was so much blood. And they had to pull me away from her. I would not let her go. I had to tell her that I loved her. That she was my little girl. That I would love her forever. Did she know that?

You don't ever stop being a mother. Not ever.

In case it's escaped you, which is totally possible, given that you're all crazy, this isn't a comedy club. Maybe you've noticed that we're all wearing hospital gowns, we're surrounded by nurses . . . Or . . . the doors are locked. We can't leave. None of us can leave. That's okay, though . . . Old MacDonald had a loony bin and now he's got your sister's number. At least I know that I belong here. This is where I deserve to be.

I'm never leaving here because I can't get well. I don't want to leave here, and I won't. No one is safe around me. Not really safe, you know? But sometimes, I think, you get a do-over. You get a chance to make a "wrong," "right." Do you know what I mean? Ronald Reagan hates your ugly mother. And this time, I'm going to be perfect. I am.

They've told me that I'm going to get to see her, in here. It's like my daughter's corning back. My husband, ex-husband, whatever, he says that he'll come too. And I'm going to keep them safe from the oogly booglies. I am. Tick tock tick tock tick tock out of time sucker. I am going to do it all right this time. "Hush little baby, don't say a word..."
```

---

## IC-0253: Ruined

- Title: Ruined
- Author (byline): Lynne Nottage
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MAMA, CHRISTIAN, OSEMBENGA, SALIMA, SOLDIER, KISEMBE
- Teaser before the introduction: Yes
- Spoken words (computed): 1682
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lynne Nottage
ISBN: 978-0822223900
Publisher: Dramatists Play Service
Date (Month/Year): 2010
```

### Introduction (context only: never use it for content warnings)

```text
The Congo – a country devastated by civil war, where an estimated 48 women are raped every hour . . . Where the death toll has reached over 5.4 million – the deadliest conflict since World War II. Today, it is still one of the most dangerous places on Earth. And in the heart of the conflict, we find Mama Nadi’s brothel – a safe haven for a few women who have escaped the villages. But how can a war be resolved when all factions are prone to unbridled violence? How can a country and its people be anything other than . . . Ruined by Lynn Nottage

(Pg 29-31) Commander Osembenga, a pompous peacock of a man in dark sunglasses, a gold chain, and a jogging suit, struts into the bar. He wears a pistol in a harness. Osembenga stands erect waiting to be acknowledged.)
```

### Performance text (classify this)

```text
Characters: Christian (traveling salesman),
Osembenga (head of government forces),
Kisembe (head of rebel forces)
Soldier (rebel)
Mama (owner of the brothel)
Salima (a prostitute sold to Mama by Christian)

MAMA: (pg 8-10) (Impatiently.) What did you bring me?

CHRISTIAN: Go on. Take a peek in the truck.

MAMA: How many?

CHRISTIAN: Three.

MAMA: I don’t know. They look used. Worn.

CHRISTIAN: C’mon, Mama. Take another look. You’ve said it yourself business is good. (Mama considers, then finally.)

MAMA: Okay, one. That one in front. (Points) How much? How much for the one?

CHRISTIAN: It’s been a good week, and I’ll tell you what, I’ll give you two for the price of one. Why not?

MAMA: Are you deaf? No. Tst! I don’t need two more mouths to feed. (then reconsiders) But, I’ll only pay for one. (Yelling.) Josephine! Josephine! Take them out back. Get them washed and some proper clothing. . . (to Christian) Did you at least tell them this time?

CHRISTIAN: Yes. They know and they came willingly. Salima is from a tiny village. She was captured by rebel soldiers; the poor thing spent nearly five months in the bush as their concubine. She says her husband is a farmer, and from what I understand, her village won’t have her back. Because . . .

MAMA: And the other?

CHRISTIAN: Sophie. Sophie is . . . is . . . Look, militia did ungodly things to the child, took her with . . . a bayonet and then left her for dead. And she was – ruined.

MAMA: (Flirtatiously.) Good evening.

OSEMBENGA: It is now. (He gives the place a once-over.)

MAMA: Can I get you something?

OSEMBENGA: Bring me a cold Primus. A pack of cigarettes, fresh. (Mama produces a chair for Osembenga, then she fishes into the cooler for a beer.)

MAMA: Monsieur, I must ask you to leave your bullets at the bar, otherwise you don’t come in.

OSEMBENGA: And if I choose not to.

MAMA: Then you don’t get served. I don’t want any mischief in here. Is that clear? (Osembenda is charmed by her tenacity. He laughs with the robust authority of a man in charge.)

OSEMBENGA: Do you know who I am?

MAMA: I’m afraid you must edify me. And then forgive me, if it makes absolutely no difference. Once you step through my door, then you’re in my house. And I make the rules here. (Osembenga laughs again.)

OSEMBENGA: All right, Mama. Forgive me. (Osembenga makes a show of removing the bullets from his gun and placing them on the table.) And who said I don’t respect the rule of law?

MAMA: Monsieur, I don’t recall seeing you here before. What brings you to mon hotel?

OSEMBENGA: Jerome Kisembe, the rebel leader. (Osembenga studies her face to gauge the response.) You know him, of course.

MAMA: I know of him. We all know of him. His name is spoken here at least several times a day. We’ve felt the sting of his reputation.

OSEMBENGA: So, you do know him.

MAMA: No, as I said I know of him. His men control the road east and the forest to the north of here.

OSEMBENGA: Is that so?

MAMA: Yes, but you must know that. (Osembenga speaks to Mama, but he is clearly addressing everyone in the audience.)

OSEMBENGA: This Jerome Kisembe is a dangerous man. You hide him and his band of renegades in your villages. Give them food, and say you’re protecting your liberator. What liberator? What will he give the people? That is what I want to know! What has he given you, Mama? Hm? A new roof? Food? Peace?

MAMA: Me, I don’t need a man to give me anything.

OSEMBENGA: Make a joke, but Kisembe has one goal and that is to make himself rich on your back, Mama. (Osembenga grows loud and more forthright as he speaks.) He will burn your crops, steal your women, and make slaves of your men all in the name of peace and reconciliation. Don’t believe him. He, and men like him, these careless militias wage a diabolical campaign. They leave stains everywhere they go. And remember the land he claims as his own, it is a national reserve, it is the people’s land, our land. And yet he will tell you the government has taken everything, though we’re actually paving the way for democracy.

MAMA: I know that, but the government needs to let him know that. But you, I’m only seeing you for the first time. Kisembe I hear his name every day.

OSEMBENGA: Then hear my name, Commander Prestige de Bembe Osembenga. (A moment. Mama absorbs the news, she seems genuinely humbled.) You will hear my name quite a bit from now on.

MAMA: Commander Osembenga, forgive me for not knowing your name. Karibu. [Welcome.] It’s a pleasure to have such an important man in our company.

OSEMBENGA: You are a practical woman, I know that you have the sense to keep your doors closed to rebel dogs. Am I right?

MAMA: (an aside to audience) (Pg 51) My doors are open to everybody. And that way trouble doesn’t settle here. (to Osembenga) Of course. (calling for one of her girls) (Pg 16) Salima! Salima, come!

SALIMA: (Salima, disgusted, bristles at the sound of her name. She reluctantly approaches and does a little shimmy for Osembenga) So, “gangsta,” you wanna dance with me? . . . .

(Osembenga responds and then freezes in place as Salima steps out of the scene he will exit as Salima begins her story) . . . (Pg 22) (to audience) Sometimes their hands are so full of rage that it hurts to be touched. (long pause as Salima remembers the past) (Pg 45-46) Do you know what I was doing on that morning? I was working in our garden picking the last of the sweet tomatoes. I put Beatrice down in the shade of a tree, because my back was giving me some trouble. The sun was about to crest, but I had to put in another hour before it got too hot.

CHRISTIAN: (pg 28) (Christian enters and also addresses the audience in a separate but interlocking monologue) It’s scaring me. I was just by Yaka-Yaka. When I was there six months ago, it was a forest filled with noisy birds, now it looks like God spooned out heaping mouthfuls of earth! It’s been ugly, but never like this. Not here.

SALIMA: (Pg 45-46) It was such a clear and open sky. This splendid bird, a peacock, had come into the garden to taunt me, and was showing off its feathers. I stooped down and called to the bird. “Wssht, Wssht.” And I felt a shadow cut across my back, and when I stood four men were there over me, smiling, wicked schoolboy smiles.

CHRISTIAN: (Pg 50) (with urgency) Listen, listen to me. I saw a boy, take a machete to a man, sever his neck, a clean blow and lift the head in the air like a trophy.

SALIMA: (Pg 45-46) “Yes?” I said. And the tall soldier slammed the butt of his gun into my cheek. Just like that. It was so quick, I didn’t even know I’d fallen to the ground. Where did they come from? How could I not have heard them?

CHRISTIAN: (Pg 50) Men were hollering. “We strong warriors, we taste victory. We will kill!”

SALIMA: (Pg 45-46) One of the soldiers held me down with his foot. He was so heavy, thick like an ox and his boot was cracked and weathered like it had been left out in the rain for weeks. His foot was so heavy and it was all I could see, as the others . . . “took” me. My baby was crying. She never cried, but she was crying, screaming. “Shhh,” I said. “Shhh.” And right then (Salima closes her eyes.) A soldier stomped on her head with his boot. And she was quiet. (A moment. Salima is overcome with grief.)

CHRISTIAN: (Pg 50-51) Oh shit, my hand, my hand is still shaking. This . . . this man Osembenga is evil. He plays at democracy. But we have to pretend that all this ugliness means nothing. We wash the blood off with buckets of frigid water, and whitewash our walls.

SALIMA: (Pg 45-46) I fought them! I did! But they still took me from my home. They took me through the bush, raiding thieves. F**** demons!

SOLDIER: “She is for everyone, soup to be had before dinner,”

SALIMA: They tied me to a tree by my foot, and the men came whenever they wanted soup. I make fires, I cook food, I listen to their stupid songs, I carry bullets, I clean wounds, I wash blood from their clothing, and, and, and … I lay there as they tore me to pieces, until I was raw … five months. Five months. Chained like a goat. These men fighting … fighting for our liberation. Still I close my eyes and I see such terrible things. Things, I cannot stand to have in my head. How can men be this way? (A moment.) How did I get in the middle of their fight? What did I do? I must have done something. (Salima fades offstage as Kisembe, leader of the rebel forces enters, zipping his pants)

MAMA: (Pg 51-52) Kisembe, I hope my girls gave you good company.

KISEMBE: Very. It is good to be back, Mama. Where’s everyone?

MAMA: You tell me. It’s been this way for a week. I haven’t seen but a handful of miners.

KISEMBE: It is Commander Osembenga. He is giving us some trouble. His men set fire to several of our mining villages. They took machetes to anything that moves. This is their justice. Believe me, when we find Osembenga and his collaborators, he will be shown the same mercy he showed our people.

SALIMA: (Mama fades back into Salima to finish her story) (Pg 45) Five months in the bush, passed between the soldiers like a wash rag. Used. (Pg 47) I walked into the family compound expecting wide open arms. An embrace. Five months, suffering. I suffered every single second of it. And he, the man I loved since I was fourteen chased me away with a green switch. (Pg 45) He called me a filthy dog, and said I tempted them. Why else would it happen? I was made poison by their fingers, that is what he said. He had no choice but to turn away from me, because I dishonored him. (Pg 47) He was too proud to bear my shame . . . but not proud enough to protect me from it. (Salima fades)

KISEMBE: (Pg 52-53) They say we are the renegades. They bring soldiers from Uganda, drive us from our land and make us refugees . . . and then turn us into criminals when we protest or try to protect ourselves. I wish [I] could stay all day, but duty calls. (Exits)

MAMA: (Pg 57) You men kill me. You come in here, take your pleasure, and then wanna judge the way I run my “business.” The front door swings both ways. I don’t force anyone’s hand. My girls, ask them . . . ask them, they’d rather be here, any day, than back out there in their villages where they are taken without regard. They’re safer with me than in their own homes.

OSEMBENGA: (Enters) (Pg 62) This soldier said he saw Jerome Kisembe here.

MAMA: This soldier is liar.

OSEMBENGA: Where is Kisesmbe? (Frightening. Menacing) Tell me where I can find Kisembe.

MAMA: I don’t know where he is . . . (to audience with ferocity) (Pg 57) I didn’t come to here as Mama Nadi, I found her the same way miners find their wealth in the muck. I stumbled off of that road without two twigs to start a fire. I turned a basket of sweets and soggy biscuits into a business. I don’t give a damn what any of you think. This is my place, Mama Nadi’s! (Pg 59) Let all the mother-hating soldiers fight it out. ‘Cuz in the end do you think that will change anything here?

A resource with background information regarding the Congolese conflict and examples of the dialect for this selection can be viewed here and is highly recommended https://www.youtube.com/watch?v=NXvZdTvQGiI&index=1&list=PLF6F07EC529297AF2
```

---

## IC-0254: Runs Girl

- Title: Runs Girl
- Author (byline): Chinelo Okparanta
- Work: Happiness Like Water, Pg 67+
- Publisher: Mariner Books
- Publication date as stated: Aug 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ADA, MAMA, NJIDEKA
- Teaser before the introduction: Yes
- Spoken words (computed): 1670
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chinelo Okparanta
Book: Happiness Like Water, Pg 67+
ISBN: 978-0544003453
Publisher: Mariner Books
Date (Month/Year): Aug 2013
```

### Introduction (context only: never use it for content warnings)

```text
‘Runs Girl’ is the Nigerian term for escort. Someone who willing to offer sex or companionship to any man in exchange for material things: expensive clothes, mobile phones or in Ada’s case treatment for her dying mother. What would you be willing to do to save the ones you love?

Runs Girl by Chinelo Okparanta
```

### Performance text (classify this)

```text
ADA: (Pg 67+) The year Mama fell sick was the year Njideka confessed to me that she was a runs girl. I should have known. She walked around campus with shiny silk blouses hanging low on her shoulders, her stilettos making tiny dents in the earth. Maybe [Runs Girls] had always been around. Maybe I only noticed them that year, with their expensive outfits and accessories – money written all over their bodies – because Mama was falling apart, and there was almost nothing I could do.

ADA: It began with pain on the shoulder. Mama decided that for dinner we would have some goat meat in pepper soup, with more than the normal amount of utazi leaves. The leaves made the soup bitter. Mama said that the bitterness, in combination with the pepper, would chase the pain away.

But the next day she could barely move her left hand. We should have gone to the hospital straight away, but Mama said to hold off. They would charge us 2,000 naira just to see the doctor. That was the amount they charged the last time we went, when Mama was having all those sweats, followed immediately by chills. That time, the doctors ran their tests and told her she was fine. 2,000 naira wasted and nothing fixed. Besides, Mama was certain it was nothing a little praying and Bible reading couldn’t fix.

There was still a little glow from the sun in through our parlour, which was where we prayed every evening, kneeling on the tile floor:

MAMA: Happy is the man whom God correcteth: therefore despise not thou the chastening of the Almighty:

ADA: Her voice shook as she read.

MAMA: For he maketh sore, and bindeth up: he woundeth, and his hands make whole. (shriek)

ADA: And then she let out a piercing shriek: a sound I hope I never hear again for as long as I live. The pain was somewhere on her back, between the upper shoulder and the lower back. She could feel it also in her front. Just like what she would expect a heart attack to be, except there was no indication that her heart was the part in which the crumbling was taking place.

In the end it was I who forced her to go to the hospital. We walked out the door early the next morning, taking small steps, my hands fastened securely around her waist. I should have told her I loved her. But how? Aside from prayers and practical exchanges, we rarely even talked those days just before she fell ill. I was busy with my studies, and she was busy with the market. And so there were silences, as if we no longer valued spoken words, as if spoken words were gaudy finishes on a delicate piece of art, unnecessary distractions from the masterpiece, whose substance was more meaningfully experienced if left unornamented.

Mama used to tell jokes and we’d laugh out loud as if we were the only people in the world. That Mama disappeared soon after Papa died and left us to fend for ourselves in a world where it was hard for a woman to do so honestly. Her mind was always on the market; how we would make money from the crops she sold to pay for this and for that. Of course, I understood her worry.

A bald-headed doctor unbuttoned her shirt. It was easy to see that there was redness and swelling in the area around her left shoulder. And where her sternum met the clavicle, just beneath her neck, there was a bulge. Next were the X-rays. There were no fractures in the bone but an abscess – a localized fluid collection – had formed in Mama’s shoulder, a sign of infection in the area. She would have to be admitted to the hospital.

I stayed at home with her for weeks after she was discharged. My first day back at [the University] was about a month into Mama’s illness. Outside of the lecture halls, I gazed at the other students, the wealthy ones who wore shiny shoes on their feet and, on their ears, tiny Bluetooth headsets. The girls swayed their hips as they walked, hands dangling limply at their sides, as if they had no care in the world. Their patent leather handbags glistened, only a little less sparkly than the sequins on their stilettos. They drove Hondas and Jeeps. Their cellphones were always ringing, and they’d walk around saying, ‘Darling’ or ‘Sweetheart’, their voices turning more and more saccharine as they spoke. Such good humour must have been the soothing effect of having so much money, I thought, the effect of having so little to worry about. After all, there were only a few problems in life that money could not fix.

I was sitting on the cement steps of our classroom building when Njideka came to me. And so, I told her Mama was in pain, and the doctors did not know the cause.

NJIDEKA: You need good doctors. Private doctors, not those underpaid teaching hospital doctors who are always going on strike

ADA: I shook my head bitterly and rolled my eyes at her. We could not even afford the teaching hospital doctors. How would we afford the private doctors? (to Njikdeka) Mama says it’s the curse of the black bird. We’ll just stick to praying for now. (to audience) And I told her honestly, that we had no money.

NJIDEKA: (commanding) Go to the private doctors. I know a good one. I’ll help you out.

ADA: Her voice was more vibrant than ever that afternoon. And I latched on to each and every one of her words, her intonations, because there was freedom in them, the way they rang out confidently, without restraint, without worry. Nothing like words between Mama and me.

primary patrons were the Yahoo Boys -- the ones who rolled into town in sleek cars and with pockets full of cash, even American dollars. She also told me about the mugus, the older men, oil executives. They bought her jewellery and paid for her recharge cards, sometimes as much as 20,000 naira per month!

NJIDEKA: The just want you to have private dinners with them. Sometimes, they just want to look at and have an intelligent conversation with a pretty woman. You’re a pretty girl. Or at least you can be. And I know of a man who would love a girl like you. You could pay for your Mama’s bills with the money.

ADA: (angrily) Abeg, comot from here! (to audience) [I was] shocked that she would even suggest such a thing for me. She could do as she pleased. But to go so far as to involve me in her sinful ways, that was another thing. (to Njikeda) God forbid!

She took out a handful of plastic-wrapped packets from a small box which she had brought from the room.

NJIDEKA: Condoms, just in case.

ADA: I didn’t say I’d do it. It’s sinful! (to audience) and I walked out the door. (to audience) We prayed again that night and Mama read again from Job.

MAMA: Despise not thou the chastening of the Almighty: For he maketh sore, and bindeth up: he woundeth, and his hands make whole.

ADA: That night, Mama asked that I helped her to bathe. She squeezed her eyes shut each time the cloth touched her skin. It didn’t matter how gentle I was. That night, it was hard to tell what the droplets on her face were: tears from so much pain and suffering, or merely splashes of bath water.

would do it just one night. To get the money for Mama. I could take her to a specialist. If I did well, I could bring in 500 dollars or more. American dollars. Njideka had said that most of the men wanted nothing beyond dinner and maybe a kiss.

The man arrived in a BMW. It was supposed to be a simple dinner. But he stopped the car in a place that I did not recognize. He asked me to untie my dress. I began to cry, begging him to take me back home.

Then all his weight was on me. I screamed, but it was dark all around, empty space like an open field. Who could have heard? He dropped me off several blocks away and I walked home, many kilometres on bare feet, holding the sequined heels that Njideka had lent me. I found the stash of bills in my purse as I walked. One thousand dollars. All that money, because he must have known that I had never been with a man. The work of the devil -- but it was more than enough to pay for Mama’s visits to a specialist.

I returned Mama was kneeling by the sofa, her arms and chest resting on its cushion, as if in the middle of praying. Mama! Do you hear me? Mama!’ She did not respond. And then suddenly I was turning her around, checking for breath. And there was none. We buried her in the cemetery not too far from our flat, the same place where we buried Papa.

Sometimes I go to the cemetery to visit Mama and Papa. On days when I’m overwhelmed by shame, I go in the evening or at night, as if the darkness will somehow mask the shame. And I remember the days before Papa died, and if I listen carefully, sometimes I can hear Mama’s laughter ringing out, somewhere far away from the cemetery. Sometimes I think that if I were placed in a valley full of bones, I would create a new Eve, create her from a new set of bones. And I would cause breath to enter in, and this new Eve would live. [She] would walk amongst the trees of the garden and drink from the river. And again, she would eat the forbidden fruit. But she would not be cast away from the garden. She would be given the opportunity, just once, to ask for forgiveness. And she would be forgiven.

(she prays) For he maketh sore, and bindeth up: he woundeth, and his hands make whole.
```

---

## IC-0255: Sacrifice

- Title: Sacrifice
- Author (byline): Joyce Carol Oates
- Work: The Perfectionist and Other Plays
- Publisher: Ecco Press
- Publication date as stated: 1995
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MURIEL, EDDIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1984
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joyce Carol Oates
Book: The Perfectionist and Other Plays
ISBN: 0452267015
Publisher: Ecco Press
Date(Month/Year): 1995
```

### Introduction (context only: never use it for content warnings)

```text
Coping with divorce - whether you've been through one or witnessed one -- is difficult, and often, downright ugly. Divorce causes people to say and do things that would normally be out of the realm of possibility. It sometimes causes people to do the unthinkable and unacceptable. It is a territorial battle where both people lose to some degree. It is a battle that causes casualties. The decision is always a Sacrifice by Joyce Carol Oats.
```

### Performance text (classify this)

```text
MURIEL: Can you imagine?-bragging to my own brother Ray he's gonna do such things! To me! to me, he's married to, has kids with! Not even ashamed or anything! CAN YOU IMAGINE! (A pause) Oh sure I got a lawyer-in self-defense. Now he's got one too! (Deep shuddering breath) And all we owe-! MURIEL pauses. Moves closer to audience. A sly, hectic, determined smile as she draws a knife out of a pocket-a sharply honed twelve-inch steak knife with a gleaming blade.

MURIEL: (Whispering, wild-eyed) You think I can't do it, huh? You just watch. (Laughs) MURIEL contemplates the knife, testing possible grips-overhand, underhand. MURIEL hides the knife again.

MURIEL: (As if pleading) I've been Eddie Fitzroy's wife for nine years and-now what? (A pause) Back to-what? My parents' house? My old room? Like I never had any kids, never been-loved? (Fierce) Well, I sure got kids. And all this, here- (A wave of her hand, indicating her home, property) -maybe the bank owns it but I'm sure here, and any son of a bitch wants me out is gonna have to carry me out. (Incensed) Had to get a lawyer, to protect myself-his lawyer's saying he can file for bankruptcy, so I get-nothing. No place to live no alimony no child support, maybe-can you believe it? (Wiping face with a tissue) Eddie Fitzroy, that everybody likes so much. 'Cause he's good-looking and was a quarterback for Ashland High and grins a lot, laughs easy-the bastard. Nine years.(Grimmer, calmer, "fatalistic" tone) You see it on TV all the time-women rising up against their oppressors. Oh, yes! (A pause)

MURIEL: (Distractedly) Saying he loved me-us-so much. Well-I know for a fact he did. All those years he did. I started putting on weight when I had Dwayne, he never minded-I'd swear. I minded more, going on one diet after another and making myself sick and Eddie would hug me and say, You look real nice to me, Muriel. Was he lying? HE WAS NOT LYING. I swear. (Angry smile) This, what I'm gonna do-strike to the heart!- (She pats the knife in her pocket) -is no rash crazy-lady act. No sir it's "premeditated." Oh yes! (Laughs) I got my defense all prepared-"PREMEN-STRUAL-TEN-SION-SYN-DROME"-you hear about it all the time. Even in the Pennysaver Shopping News. (Laughs) I read this article, underlined it, memorized it, threw it out-you bet I'm not that stupid, keeping it on the premises for the police to find.

MURIEL: (Sudden anger) "Gonna take Muriel to the cleaners"-huh? Can you believe it? Just 'cause he's out of work he don't give a shit for his own kids can you believe it! I'm just so ashamed, what am I s'posed to do, wear a paper bag over my head?-the rest of my life here in Ashland where I was born same as him God damn him! (A pause) A man like that, he loved his wife so, he near-about fainted when I was in labor, both times-like, like he was in labor. And that was no joke, either. He was.

MURIEL: (Softer tone) He was that way with the kids, too. He'd hug them sometimes squeezing the breath out of them, hurting them so they'd get scared. They'd think Daddy was playing but Daddy wasn't. "I love you honey, I love you"-he'd say to Dwayne, and to Junie. I'd hear him. Like it was some kind of prayer. (A pause) I guess you'd have to say he was a good father, sort of a nervous father but a good one, up till maybe a year ago. (Wistful smile) Maybe they all are-menfathers-real nice-up to the day when they're not. MURIEL speaks passionately, as if the profound mystery at the heart of her experience is something that must be communicated, yet cannot be; she has lost the edge of her aggression and rage, and speaks almost reverently.

MURIEL: So-one day-one night-a few years ago-I'd gained maybe thirty pounds by then-we were in bed and, with Eddie, it was like always, him holding me so tight, except this time he really hurt me- and I panicked and shoved him away, I put on the light and looked at him, "Are you crazy," I said, my teeth were chattering I was so scared, "-what is it?" and Eddie's staring at me like he doesn't know me, this look on his face like he's a wild man or something, so now I was scared. (A pause) "Honey," I said, "-better tell me: what is it?" (A pause, then, breathless) So he told me. (A pause) You won't believe what he told me!

FLASHBACK

EDDIE: This cousin of mine, Bobbie-he was five years old when it happened. I was nine, and he was five. It was an accident, him drowning-that terrible way. But my fault. (A pause) We had these sleds-both of us, new sleds-Christmas sleds-- and Bobbie broke through the ice and (Breathless, speaking too rapidly, EDDIE must stop and try again). Bobbie was. . . a nice kid. (A pause. Stares at his hands, flexes his fingers) It's hard to talk. I hate talking. Any kind of serious talk. You can't do it, so why try. (Tries to control himself) O.K., there was this big long hill--cow pasture-we'd sled down-to the creek. We took our sleds down the hill but we weren't supposed to go out on the creek even when it was frozen because, in the middle, sometimes, the ice was thin. I'd take my sled out, though, and Bobbie didn't tell on me, he was scared, watching me sled out onto the ice then steer to the side, quick, before the ice cracked. (Dreamily, as if sledding, steering; a look of rapt, childish concentration) There was a feeling I'd get if the ice was thin, here- (He indicates the pit of his belly, scrotum)-so I'd know. One day I was teasing Bobbie, I guess, and he followed me out onto the ice, but instead of steering to the side like I did he went straight out and right away the ice started cracking and he was screaming and his sled broke through, he was in the water, screaming, this freezing water that's black, and running fast-and I grabbed hold of him by the arm-got down on my stomach on the ice to try to keep it from breaking more-but I couldn't pull him out he was screaming, "Don't let me go! Don't let me go!"-Jesus, I'll remember it all my life. (A pause) He tried to grab onto me too, and pull himself out of the water, but he couldn't, and I couldn't get him out, the ice was breaking, the water was pulling him away, I don't know how long I had hold of him, by the wrist-ten minutes? five?-till my fingers froze and I just... had. . . to . . . let. . . him. . . go. (A pause) (Self-loathing) He was screaming, he didn't want to die. There was nobody but me to save him, nobody in the whole world but me, a nine-year-old kid, and. . . I had to let him go. (A pause) So he died, he drowned. I saw him go. I could see his body go. (A pause) (Trying to be matter-of-fact) Well-that was it. Bobbie died, aged five; I was to blame. All the years I was growing up I'd hear him screaming. I hear him now-it's always there. (A distant look) (Half-sobbing) I let him go. I couldn't save him.

MURIEL: (Embracing him) It wasn't your fault! I never knew, that poor little boy, but it wasn't your fault, Eddie, you were such a little boy yourself.

EDDIE: I-I guess it comes over me, sometimes. I sort of black out. I don't know where I am. (Dazedly, blinking) Except-there's you. (Pleading, as if for forgiveness) Muriel, I love you so much. I love you so much. I want to take care of you, you and the kids, forever and ever I'd give my life for you, I love you so. You believe me, don't you? You love me, don't you? Muriel? I swear to God I won't let you go, I won't let you go, Muriel, all my life I'll take care of you, I'll show you-you and the kids. Jesus, I love you so much.

[Pause as flashback fades and the mood is immediately shattered.]

MURIEL: (Desperate, flurried, appealing to audience) You heard him! his exact words!-"All my life I'll take care of you!" You heard him! You heard him! You heard him! The liar! I know we had some hard times together lately. Buying things on credit-both of us to blame. Then, other things,-"marital problems."

(Embarrassed, tries for brazen cheerfulness) Well, we all have them, huh?- "marital problems." You're married, that's what you have. Don't we? (Peering at audience; a pause) We'd been seeing a marriage counselor. So, yeah, I thought things were looking hopeful. Then, one day, instead of sitting down for supper, he looks at me, his face gets all funny, his eyes, and he says he can't do it,-so I say, "Can't do what?" and he says, "I want out, Muriel, I can't hack it, I want out-"

MURIEL: (To audience, childlike pleading) Y'know what I wish?-we could go on trial, that's what I wish! Him, and me! "A jury of one's peers!" (A gesture at the audience) Then justice would be done! (Hugging herself tightly) I read the Bible, now. I'm a sinful woman but I mean to exact justice. This morning, so early! I opened my Bible my grandma gave me-first words I read were-

(MURIEL shuts her eyes, lets her head fall back, an expression of ecstasy on her face) Psalm 68: "Let God arise, let his enemies be scattered: let them also that hate them flee before him." In her ecstatic trance, MURIEL draws the knife out of her pocket. Caresses it. "PRE-MED-I-TATED"-"PRE-MEN-STRUAL." (Laughs) The jury can decide who's the murderer! MURIEL, hiding the knife in the folds of her clothing, or behind her thigh, confronts EDDIE

MURIEL: (Surprisingly soft, pleading, girlish tone) Eddie, hon-wait. The school bus will be here in twenty minutes. The kids

EDDIE: (Guiltily) I can't. As EDDIE tries to ease away, MURIEL clutches his shirtsleeve.

MURIEL: Eddie, I love you-how'm I gonna live without you?

EDDIE: Christ, Muriel, you're making it so hard

MURIEL: (Sobbing) Eddie, honey, I'll lose weight-I will! I'll look like I used to! I'll go back to work! I won't bug you about things! Dwayne and Junie, they'll be good-they promised! Wait and see them, they'll tell you themselves

EDDIE: (Sweating, desperate to escape) Muriel, let me go, huh? Muriel, for God’s sake LET ME GO!

MURIEL: (Raw, unmitigated yearning) I LOVE YOU-HOW CAN I "LET YOU GO!" MURIEL crouches, cunning, feet apart, and brings around the knife-gripping it underhand so that, if she swings it, the upward arc will bring its blade into EDDIE'S abdomen. You think I can't? You think I can't? You think I can't? MURIEL feints with the knife. We're better off dead, both of us.

EDDIE: Muriel, don't talk that way. Hon, listen (Wild laugh) What if the kids see you! Jesus!

MURIEL: (Panting) Let them! I want them to! I'll go on trial! I'm not ashamed! Promised you'd take care of us all your life-never let us go like you let your little cousin go-Murderer! That little boy you let drown, you liar, stinking hypocrite

EDDIE: (Angrily) Bobbie's got nothing to do with you!

MURIEL: How can you let me go, after all that? A tense pause.

EDDIE: (An outburst) Because-I don't love you any more. There is another tense pause. MURIEL realizes it is hopeless; she lowers the knife.

MURIEL: (Sudden flat, ironic tone) Then-get the hell out, mister. She gestures with the knife, waving him away MURIEL stares after him. Just when we think that MURIEL is resigned, she loses control; stabs the floor with the knife, sobbing. Ugly thing, Muriel!-poor sad cow, Muriel! Take that, Muriel! Die! SCENE BREAK

MURIEL: (As if confiding in a woman friend) So, well! That's that. (Laughs, embarrassed) Muriel tried. Muriel sure did. I lost three pounds this week-that's a start. (A pause) I guess my weakness is-I know right from wrong. My parents taught me to be good. (Shrugs) Probably couldn't stab Hitler, if he was standing in front of me. If that's goodness or just weakness, I don't know. One thing I know-you can't hurt another person to fix up your own life. Except, hell-I'd've liked a jury-"one's own peers." So you could explain it to me. Explain Eddie to me. How a man loves you, and the love wears out. How you love him-and that passes too. Like the black water's carrying us all away? Is that it? (A pause) Maybe you can explain it . . . ? I'm just trying to understand.
```

---

## IC-0256: Scraps

- Title: Scraps
- Author (byline): Jane Martin
- Work: Talking With
- Publisher: Samuel French, Inc.
- Publication date as stated: April 1983
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1010
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Martin
Book: Talking With
ISBN: 0573630216
Publisher: Samuel French, Inc.
Date (Month/Year): April 1983
```

### Introduction (context only: never use it for content warnings)

```text
Though rewarding, being a stay-at-home mom isn’t easy. In fact, many women are surprised to find it’s the hardest job they’ve ever had. Days spent without a single adult conversation, quieting your child’s screams in the store, cleaning bloody knees, carpooling, disciplining, doing laundry, changing diapers, packing lunches, cleaning house and planning meals may leave you wondering, “Is this really worth it?” The “I’m just a mom” syndrome attacks routinely, suggesting the world is moving on without you while you watch Barney with your 3-year-old.

What happens when your children are old enough not to need the constant attention? In Scraps by Jane Martin we find an extreme case of a stay-at-home mom coping with her unnoticed and unappreciated status. She escapes into a fantasy life in which she reinvents herself as a character from Oz (perhaps her childhood link to a daughter who no longer needs her). She describes herself as "something between a rag doll and a rainbow." This reference ties into her obsession with the Land of Oz as her escape. The comic overtones of this piece make her common tragedy that much richer. Scraps by Jane Martin.
```

### Performance text (classify this)

```text
The lights come up on a woman in a multi-colored patch-work costume. Red, blue, green, yellow. Button eyes, yarn hair, pearls for teeth. It is the Patchwork Girl of Oz. She is using a stand-up vacuum cleaner. She turns it off and looks at the audience.

I spend more and more time in Oz. Since I’ve turned thirty-five Since Suzanne is in high school. This is Scraps. I had a dressmaker do it. It’s not the only one I have. I have Ozma, I have Dorothy, I have Glinda the Good Witch. I’m even beginning to go out in this stuff. The midnight Rocky Horror Show, St. Patrick’s Day parades. I went down one night to a gay bar and they waived the cover charge. Always as Scraps. My face doesn’t show. Jack doesn’t even know I have the books. He sure as hell doesn’t know I do this. You know about the Patchwork Girl? It’s the seventh Oz book. She was made from a patchwork quilt by Dr. Pipt, the crooked magician, to be his servant. He sprinkled the “powder of life” on her. But what nobody realized is that Ojo had dumped a bunch of cleverness into the Patchwork Girl’s head. Too much for her to be satisfied as a servant. So she set off for the Emerald City with Ojo and the Transparent Glass Cat with the ruby heart and pink brains and the Living Phonograph. They called her Scraps and sometimes Patches.

I wish I was clever. Oh, I know how to hid nail holes with toothpaste, and how to spray cut flowers with hair-fix to make them last longer, but I’ve never had a job because I don’t know how to do anything. I mean anything they pay you for. I’m not too good at learning new things either. I just freeze up or something.

God, I loved the Oz books when I was a kid. Do you know the countries? Well you know the Munchkins. Everybody knows the Munchkins. The Winkies where everything’s yellow. Jack Pumpkinhead, the Tin Woodman, The Scarecrow, they all have their castles there. Gilliken Country, Quadling Country. I can get around better in any one of those places than I can in downtown Cleveland. When Jack goes I just sit looking out the window for a long time and then I close the drapes and spend the day in Oz. I can clean and stuff and still be there. Jack doesn’t understand why I put yellow linoleum in the kitchen.

Nobody dies in Oz. No matter what’s happening to you Ozma watches on her magic picture and you always get saved. Listen, there are great bad guys! Old Mombi, The Gnome King, The Skeezers. You think I’m ill don’t you? You want to send me to group therapy or self-improvement seminars or off to take night classes towards a law degree. God I hated school! How could anybody like it? Hell, you can live a whole life and never have to subtract. Have you noticed that nobody ever talks about anything? I bet I haven’t heard anybody talk about anything in two years. God knows Jack doesn’t. In the morning he reads me the cereal boxes out loud. He thinks I’m boring. He wouldn’t think I was so boring if he came home and found me in this. What would he do I wonder? Call his mother for advice. She’d tell him to buy me a Cuisinart and an exercycle.

I live in Oz. I see it all. I’ve gotten so I can smell it. “Two or three hours walk along this trail brought Ojo and Scraps to a clear level country where there were a few farms and some scattered octagonal houses, all bright Quadling red and smelling of peppermint.” I can live in that sentence for a full 3 hours. You know what? I like that a lot better than life.

Someday I’ll be at the front door when Jack comes home. The Chevette will pull up and he’ll have the week’s chart, the Southeastern sales figures, the demographics under his arm. And there I’ll be to give him a nice kiss, holding the spatula, me, Scraps. “You certainly are a wonder, my dear, and I fancy you’d make a splendid pin cusion. If you belonged to me, I’d wear smoked glasses when I looked at you.” (SHE takes the “SCRAPS” head off) But I do belong to you Jack. I’m your helpmeet, your homemaker.

The thing that frightens me is I’m getting flashbacks, just like combat or acid.

We had some people over. Jack had bought an Atari. You know, those television computer space games? Asteroids, Space Invaders, Cosmic Cadet. God, I hate the sound of it. They were talking about municipal bonds or something. We were all around the T.V. with the pretzel mix. Jenny, Allen, Marty, Turk, Jack, me. And I went to Oz. I was in trouble and I was being rescued from a whirlpool by this Ork . . . a bird with four wings, four legs and a propeller tail, and I guess Jack was talking to me and I didn’t answer. He had to shake me. I really didn’t know where I was. I ruined his best score in the Atari. I suppose he’ll leave me when he finds out. Take the Irish setter. He’s the provider. Jesus, I’ll have to make a living, won’t I? Maybe Ozma will see me in her Magic Picture. Then they’ll send the Scarecrow to come and get me and we’ll ride the Sawhorse all the way back to the Emerald City. We’ll lunch with the Hungry Tiger and the Cowardly Lion. And the Scarecrow will say, “Why here’s a right curous creation, midway between a ragbag and a rainbow. Why my dear, (SHE puts the “SCRAPS” head back on and sings.) you are quite bedazzling!” The scarecrow has the very best brains the Wizard ever made. Perhaps we’ll be married. Kizzle-Kazzle Kore The Wolf is at the door There’s nothing to eat But a bone without meat And a bill from the grocery store. (She freezes for a beat and then begins vacuuming.)
```

---

## IC-0257: Secrets

- Title: Secrets
- Author (byline): Walt Vail
- Work: Not specified
- Publisher: Brooklyn Publishing Company
- Publication date as stated: 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARLIE, DIEDRE, FATHER
- Teaser before the introduction: No
- Spoken words (computed): 1049
- Already set (do not supply): none

### Source block (context only)

```text
Author: Walt Vail
ISBN: 978-1930961371
Publisher: Brooklyn Publishing Company
Date (Month/Year): 1998
```

### Introduction (context only: never use it for content warnings)

```text
ACTRESS: In the words of Samuel Johnson: "We cannot tell the precise moment when friendship is formed. As in filling a vessel drop by drop, there is at last a drop which makes it run over; so, in a series of kindnesses there is at last one which makes the heart run over."

ACTOR: Children of domestic violence however have few friends . . . friends share secrets which is the first lesson victims of child abuse learn. Never tell. No matter how hard she tries to deny it, Deidre is in desperate need of a friend.

ACTRESS: If only she could trust someone. But she believes that if anyone really knew her, they’d realize what an awful person she is. That’s what her Dad told her anyway.

ACTOR: Nothing in life is free.

ACTRESS: Everything has a price. To have a true friend, I’d have to sacrifice my

TOGETHER: Secrets by Walt Vail
```

### Performance text (classify this)

```text
CHARLIE: Deidre.

DIEDRE: Yes? I have to finish this term paper.

CHARLIE: Can I help?

DIEDRE: I’d rather do it myself.

CHARLIE: I like you, Deidre.

DIEDRE: Charlie, I go steady with David.

CHARLIE: Why David?

DIEDRE: He doesn’t make unreasonable demands on me.

CHARLIE: And I do? How’s your father treating you?

DIEDRE: I’m sorry I told you that, Charlie. It’s not your concern. I shouldn’t have spoken. (beat) My father treats me okay. He’s not drinking.

CHARLIE: He’ll start up again. Like my old man. Drinks, then starts swinging.

DIEDRE: Your father hits you?

CHARLIE: Not since I got bigger that him.

DIEDRE: I can’t hope for that, I guess.

CHARLIE: (looks closely) You’ve got another bruise.

DIEDRE: I turn black and blue if someone breathes on me.

CHARLIE: He’s beating you up all the time. You think I can’t see that?

DIEDRE: Please, Charlie. Don’t tell anyone!

CHARLIE: I couldn’t sleep last night, Deidre. All I could think of was a guy that weighs 180 pounds beating up on a small, defenseless girl. You know what could happen if he hits you too hard?

DIEDRE: I don’t want to talk about it.

CHARLIE: (pause) You want to pretend it isn’t happening?

DIEDRE: It isn’t happening. He’s been calm. Charlie, my father earns a living for our family. If I make trouble for him, he could lose his job.

CHARLIE: Before your mother died…did he beat her too?

DIEDRE: They had their arguments, like any married couple. In the bedroom at night, I’d hear her cry out, as if she was having a nightmare.

CHARLIE: Deidre, your father is sick.

(As she remembers, D has a flashback. She reverts back to a little girl. D sways back and forth in a rhythmic manner, quietly humming or singing a tune. C changes his stance and attitude into one much older than himself, as C plays D’s father)

FATHER: Daddy’s songbird be singin’?

DIEDRE: (voice of a child) For Mama. I’m singin’ for her. Do ya think she can hear me?

FATHER: Dunno. She barely heard me when she was alive.

DIEDRE: How is me and Peggy gonna get raised now, without Mama?

FATHER: You’ll have to look after Peggy. You’re the lady of the house now, Deidre. I’m counting on my little songbird.

DIEDRE: Me? I can’t do it like her. I ain’t Mama.

FATHER: You’re responsible now. There’s rent to pay. You do a good job, You got to do a good job, ya hear? Rent’s not free no more. Rent’s not free. ******Flashback ends*****

DIEDRE: My father’s not sick, exactly. Men have frustrations.

CHARLIE: The heck we do! I’d never hit a woman. And my father may have beat me, but he’d never dare hit my mother. I’d break his head if he ever did.

DIEDRE: I guess that’s why I told you, Charlie. I just sensed you’d understand. I wasn’t trying to get you angry. When I graduate from high school in two more years, I’ll get a job. I’ll get a place of my own, and I’ll take Peggy with me. I’ll be a mother to her.

CHARLIE: How old is Peggy?

DIEDRE: She’s eleven.

CHARLIE: When did he first hit you?

DIEDRE: I was (beat) eleven. Right after mother died. He was alone. . .

CHARLIE: When you wear out, he’ll start on Peggy. A job won’t be enough. You need money to go out on your own.

DIEDRE: I know where to get it, if necessary. [My father] has a lot of cash. He doesn’t trust banks.

CHARLIE: So, steal it and get out now! He can’t say anything. You could turn him in for abuse!

DIEDRE: I can’t steal his money!

CHARLIE: He owes it to you! I’ll go with you.

DIEDRE: You’re not my boyfriend.

CHARLIE: You don’t like David. You go with him for convenience because he’s stupid and harmless, and he doesn’t really care about you. Not like I do! (beat) How much has the old man got? Tell me where it is, and I’ll steal it for you. Give me the key, and I’ll go in while he’s working. I’ll smash a few windows to make it look like a break in.

DIEDRE: Forget it!

CHARLIE: If I had some of that money—do you know what I’d do? I’d solve this problem for you.

DIEDRE: How much money do you need?

CHARLIE: A thousand dollars. I’ll get a place of my own. Then you can join me and bring your sister. Another town, another state. You and Peggy can go to school there, wherever it is. And I’ll get a job.

DIEDRE: I’ll think about it. Now let me do my schoolwork. I have to be home early today.

CHARLIE: Something more is bothering you, I can tell. You act like you don’t want to be noticed, like you have a secret. I know, because I have my own secrets. I’m like you.

DIEDRE: No one’s like me, Charlie. No one.

CHARLIE: Have you ever thought about killing yourself?

DIEDRE: No, I think about surviving. I work hard at staying alive. You mustn’t think about killing yourself. God wouldn’t like it.

CHARLIE: You believe in God? If there is a God, he’s playing a big joke on all of us.

DIEDRE: No, he’s just testing us. He gives us the answers, if we recognize them. (beat) We all grow up.

CHARLIE: No, we don’t. Some of us never make it. Something happens—a car accident, an drug overdose.

DIEDRE: Don’t get morbid.

CHARLIE: I think there’s something you’re not telling me.

DIEDRE: I have plenty of secrets. More than any girl my age should have.

CHARLIE: (pauses, as D. drifts deeply in thought) Deidre? Deidre? ******Flashback *****

DIEDRE: (shielding her sister) I know it’s been a tough day, Daddy. Don’t! Come on. Please! You don’t need to. There’s one more beer left. Maybe if you drink it, you can go to sleep.

FATHER: (in a rage) Out of my way, girl! You can go to your room. Daddy is giving you permission to leave. Now get your butt out of here before I stop feeling so generous!

DIEDRE: Take it out on me. It’s my fault! Whatever happened, I did it!

FATHER: I spawned a crazy girl. Can’t hear nothin’. Now move before you find yourself sleepin’ in the backyard. Rent on this trailer ain’t free, ya’ know.

DIEDRE: (tries to hold him back) I know, Daddy. But you can’t. She’s only ten. Get out of here, Peggy!!!

FATHER: (grabs her by the collar) You can go to your room, or I can EVICT you. Understand!?! ******Flashback Ends *****

CHARLIE: Deidre…Deidre?

DIEDRE: (painfully) I can’t promise anything for sure, but…

CHARLIE: Trust me.

DIEDRE: I do. But, we’re . . . friends, that’s all. I wouldn’t want to hurt or upset you. But, I’ll get you the money. We have one chance. . . and you’re it, Charlie.

CHARLIE: I won’t let you down.

DIEDRE: You don’t really know me. If you did, you wouldn’t like me. I’m not a very nice person. You’ll find that out before long, Charlie. Life swallowed me up long ago. (pause, a distant look in her eye) No matter which way I turn, rent ain’t never gonna be free.
```

---

## IC-0258: The Shape of a Girl

- Title: The Shape of a Girl
- Author (byline): Joan MacLeod
- Work: Not specified
- Publisher: Talonbooks
- Publication date as stated: Feb 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BRADIE, ADRIENNE, SOFIE, AMBER
- Teaser before the introduction: Yes
- Spoken words (computed): 1391
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joan MacLeod
ISBN: 978-0889224605
Publisher: Talonbooks
Date (Month/Year): Feb 2002
```

### Introduction (context only: never use it for content warnings)

```text
For girls, childhood was once a time of carefree days of friendships and make believe. But times have changed and mean girl issues that never emerged until middle school are now becoming prevalent as early as 2nd grade.

*According to Erik Stangvik, a top executive at No Bully, one of America’s top anti-bullying advocacy groups “Young girls, often operating under a ‘pack mentality,’ isolate and banish their targets from the tribe, making them feel as if they don’t belong. They gossip and start rumors and call the other girls names. It’s nothing short of psychological warfare.

And whether you are the bully or part of the group who sees it happening and says nothing, you could be part of the bullying monster in . . .

The Shape of a Girl by Joan MacLeod
```

### Performance text (classify this)

```text
BRADIE: [Pg 29-30] [It is second grade and] we are in love, we are all forever in love -- piles and piles of ponies. Little brushes for their tiny pink manes, their purple tails. We spend hours drawing them, me and Adrienne and Amber. We call ourselves by our new names in secret: [Adrienne is] Rainbow Rider, [Amber is] Lucky Lady, and [I am] Thunder. Sofie is the new girl in grade two. Her horse name is Gypsy. [But] Sofie doesn't just fall in love with horses; she gallops out to the playground for recess; she talks by doing whinnies and stomping her feet; she never cares about who sees.

ADRIENNE: Good little horsie.

BRADIE: We love Sofie the horse. We make tiny braids all over her head; we paint rainbows on her cheeks.

BRADIE: [Pg 30-31] And then one day, one normal un-special day Adrienne comes to school and announces . . .

ADRIENNE: It's penalty day!

BRADIE: We don't know what penalty day is.

ADRIENNE: On penalty day one girl is chosen and everyone is mean to that one girl for the whole day.

BRADIE: Why? Adrienne doesn't know. It's just a part of school. At first penalty day is hard to figure out. There are a lot of rules. The person we have to be mean to has fleas of course. Everyone has to write FP for flea proof on their hand.

By the end of grade four penalty day had become as complex as World War Two. But who the enemy was had become entirely simple. I don't know why it was Sofie. It just was.

ADRIENNE: [Pg 34-35] No one is to have contact of any kind with IT from first period until lunch. If you have to address IT do so during homeroom. On the school bus IT has to sit on the fourth seat on the left. If IT talks to any boys, IT will be dealt with by me. Case closed. IT will make no comments and will not be allowed to look at me anymore as of now.

SOFIE: Don’t call me that

ADRIENNE: (mimicking) Don't call me that.

AMBER: What if she . .

ADRIENNE: IT

AMBER: What if IT has to go to the bathroom?

BRADIE: Adrienne ignores her and turns her back on Sofie, to show us she means business. Adrienne always means business.

[By middle school] There is a brand-new code every day. [Pg 41] Sofie is accused of watching the girls get undressed in gym. [Pg 35-36] Adrienne is lifting up her tee-shirt. She is wearing a white bra covered in tiny pink flowers. Mine is identical. Adrienne watches Sofie. Sofie yanks up her blouse. She is wearing a rolled up undershirt.

ADRIENNE: God, look at IT!

SOFIE: It’s a sports bra.

ADRIENNE: IT thinks that's a bra.

BRADIE: Sofie doesn't have a clue. She has no sense of how to avoid anything.

ADRIENNE: A sports bra is a defense against guys. The really high-end sports bras repel guys, totally impenetrable. A good sports bra will catapult guys across the room. THAT is NOT a sports bra. It's a little Miss Undie shirt. Gross.

SOFIE: Ha ha.

BRADIE: Another one of Sofie's bad habits, haha-ing all the time. And all of a sudden everyone is laughing and Sofie is allowed to be our friend again. [Pg 37-38] So you probably didn't notice how still she was, with her eyes straight ahead. The girls across from her were chanting but you'd have to listen hard to hear it. [Pg 39] Girls are getting meaner.

[By the time we are in high school] [Pg 34] Part of me gets it. And I hate it that I do. But right now, if you put me in a room filled with girls, girls my age that I've never seen before in my life -- I could divide them all up. I could decide who goes where and just where I fit in.

[Pg 52] I have no idea why I feel I have to keep tabs on Sofie. I just do. She's a regular girl. But this girl, this regular girl, [Pg 50] she doesn't know, doesn't get the plot, doesn't understand her part. So it starts.

[Pg 52-56] Sometimes I follow her around. She has no idea; she has always been a fairly clued out individual. I go to the bus shelter after she's left to check it out. There are little rocks lined up along the sides and she's carved her initials S.G. into the seat. No doubt it all is charged with meaning in the world of Sofie. I watch Sofie board the bus, always first on so that she can sit directly behind the driver.

[Then] just when you think it was all ancient history it starts again -- three weeks ago, in the girls bathroom. Right after home room. I walk in. I'm not doing anything, I'm minding my own business, I just have to pee. Sofie is there. Applying this goofy blue eyeliner in a goofy blue line. Then guess-who comes kicking her way out of the end cubicle. Adrienne's been crying; her eyes are rabbity pink. No doubt there has been some new atrocity between her and [her boyfriend] Justin. Let's go. That's me, trying to head her off but Adrienne has already seen Sofie. A girl in the shape of a monster A monster in the shape of a girl.

ADRIENNE: What are you looking at?

BRADIE: Sofie goes blank. She turns and fixes her sights on the tampon machine.

ADRIENNE: I asked you a question.

BRADIE: But Sofie is still in statue mode, uninhabited. No doubt Sofie's entire school life is an out of body experience. Adrienne drops her Atlas on Sofie's foot. Sofie doesn't blink.

ADRIENNE: Pick it up. I said pick it up.

BRADIE: Do something, say something, anything, fight. Do something, say something, anything, fight. . . But Sofie just bends over. And I hate her. As soon as she does it, I know she's lost. Adrienne kicks Sofie down on all fours. All the work she'd put into being invisible, down the drain.

ADRIENNE: Lovely. Sofie the horse.

BRADIE: Sofie tries to get up and Adrienne's boot comes down in the center of Sofie's back.

ADRIENNE: Did I say you could get up?

BRADIE: Sofie tries to turn her head around but Adrienne grabs her by the shirt.

ADRIENNE: Maybe the horse needs a drink of water.

BRADIE: Adrienne pulls Sofie over to the toilet. And yes, finally. Sofie's head is turning, twisting away from Adrienne and . . . turning toward me.

SOFIE: Braidie, please.

BRADIE: You do what you have to do. You look down. Like this. And then you navigate your way to the door using only your peripheral vision.

After school, when I get on the bus, Adrienne is waiting for me. (to Adrienne) Adrienne. What happened? (to audience) But she does’t know what I’m talking about, can’t remember, just a regular day. (to Adrienne) What happened to Sofie?

ADRIENNE: Nothing happened.

BRADIE: I see the empty seat behind the driver on the bus, Sofie's seat. A tremor starts; my hands are shaking. And Adrienne is gone; the friend I loved is gone. All that's left is the shape of a girl. A girl in the shape of a monster A monster in the shape of a girl.

The driver lets me off. I walk back to school. I go right into the girls' bathroom. I hear a sound from the last cubicle. Sofie is sitting on the lid of the toilet. Her lips all puffed up and purple. When she sees who it is, she covers her head. . . She's acting like I'm going to hit her, which is so crazy. I never did anything.

[Pg 50] The ones who watched. Maybe they were so glad to not be that girl that they don’t even know how to imagine shouting stop. Maybe they think silence is the ticket, the only way to never end up like the girl [who] looked up and begged for help.

[Pg 56] Sofie rocks back and forth then all of a sudden, she smashes her head into the side of the stall.

We did a good job. Even Sofie hates Sofie.

[Pg 58] And I understand for the first time what I have to say: I wish to report the behavior of . . . I'm scared. Scared for the safety of another girl. That she might do something crazy. Her name is Sofie. She has been treated in a despicable way by many people . . . including me.
```

---

## IC-0259: The Shape of Things

- Title: The Shape of Things
- Author (byline): Neil LaBute
- Work: Not specified
- Publisher: Faber and Faber, Inc.
- Publication date as stated: Nov 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: EVELYN, ADAM, JENNY
- Teaser before the introduction: Yes
- Spoken words (computed): 1653
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Labute
ISBN: 978-0571212460
Publisher: Faber and Faber, Inc.
Date (Month/Year): Nov 2001
```

### Introduction (context only: never use it for content warnings)

```text
How far would you go for love? For art? What concessions would you make? What price would you be willing to pay? Such are the painful questions explored by Neil Labute in The Shape of Things -- A modern retelling of the fall of man.
```

### Performance text (classify this)

```text
EVELYN: (To audience) Good evening. I promise to make this presentation as quick and painless as possible. My task tonight is to unveil my semester’s work. . . Oh, I almost forgot . . . and this is fairly personal, so please indulge me. (beat) I was given an engagement ring two days ago and I haven’t answered the guy yet (Show ring on finger) . . . so I wanted to do it this evening. (To Adam) Here goes. This is a beautiful stone and an amazing gesture on your part. By the time I’m through here, I promise that you’ll have your answer . . .

EVELYN: I present to you this, my newest work. It is a human sculpture on which I’ve worked these past eighteen weeks, and of whom I’m very proud. The piece itself – him – is untitled. I first spotted my chosen base material . . . it’s so funny not to use names! Sorry, but a lawyer actually told me I had to say that, ‘base material’ . . . on January 9, the fifth day of winter semester. I created a scenario that would allow for our seemingly random connection. *****Scene*****

(EVELYN stands near a stretch of velvet rope. She has a can in one hand and stares up at an enormous human sculpture. ADAM steps across the barrier and approaches her)

ADAM: . . . you stepped over the line, miss? Ummmm, you stepped over . . .

EVELYN: I meant to step over . . .

ADAM: What? Yeah, I figured you did. I mean, the way you did it an all, kinda deliberate like. you’re not supposed to do that.

EVELYN: I know. That’s why I tried it . . . to see what would happen.

ADAM: I’m what happens, I guess. I have to walk over, like I’ve done, and ask you to take a step back.

EVELYN: And if someone doesn’t, what then?

ADAM: Hell, I dunno . . . I’m off in, like, ten minutes, I’d probably just stand here, make sure you didn’t touch anything. Hey, you’re not gonna mess up my weekend with this, are you?

EVELYN: I wasn’t planning on it, but . . . I’m not completely against it, either.

ADAM: See, if you get all crazy, then I gotta write up a report and stuff, I’m here till six, six-thirty easy, and I have a second job to get to. . . step back behind the line there . . . I’d appreciate it.

EVELYN: No. sorry, I can’t. I’m building up my nerve, and if I go back over, I’ll probably be a big wuss about it and take off . . .

ADAM: About what? The ‘wuss ’part, I mean . . .

EVELYN: I was going to do something to the nude. Mess it up or . . . paint a big (gestures) on it, but whatever . . .

ADAM: (beat) . . . so, right over the leaves there, or just a free-floating number.

EVELYN: probably anatomically correct. I mean, if you’re gonna do it, why not . . .

ADAM: . . . do it right? Absolutely. *****Scene*****

EVELYN: The hair, the glasses, the excessive amount of weight offered a number of physical areas that made him unique and perfect for this project. A short list of alterations I’ve induced would include eating better and losing weight – some twenty-five pounds or more *****Scene*****

ADAM: . . . . You amaze me.

EVELYN: I’m glad. (beat) and you amaze me, you do. Look at you!

ADAM: It’s just a little jogging.

EVELYN: No, it’s not. It’s not just that . . . you’re running, you’re eating better. Are you still lifting?

ADAM: Yeah . . . I mean, I didn’t today, but . . . .

EVELYN: Do you like doing it?

ADAM: Honestly . . . No. It totally hate it! (they laugh)

EVELYN: So why would you . . . ?

ADAM: Because you suggested it. Which is kinda pathetic, but true . . .

EVELYN: You shouldn’t do something you don’t wanna do.

ADAM: Yeah, you should. Why not? If it’s for some one . . . I mean, I’m doing it for you.

EVELYN: I gave you a couple ides and you’re changing your entire life. I’m very proud of you.

(Adam freezes in scene and Evelyn steps out to resume her presentation)

EVELYN: . . .the purchase of contact lenses *****Scene***** Adam and his friend Jenny in the park

JENNY: You are getting cuter by the day. What is that girl doing to you?

ADAM: Lots . . . she’s amazing, really.

JENNY: What happened to your . . . are you wearing . . . Adam, are those contacts?

ADAM: Yeah, contacts.

JENNY: My god, this from the former ‘tape around the nose thing-y’ champion.

ADAM: That was only for a week, that one time!

JENNY: Still, you’ve gotta admit . . .

ADAM: I do, it’s amazing. I feel better . . .

JENNY: Better? You’re like, this totally hot guy now . . . (beat) I always thought you were handsome, anyway, but I didn’t think you’d go in for the makeover thing.

ADAM: Me either. Who knew? (Adam freezes in scene and Evelyn steps out to resume her presentation)

EVELYN: A complete change in hairstyles and significant wardrobe alterations as well. He even tattooed his body for me, without asking . . . in a highly questionable place. *****Scene*****

ADAM: I can show you something . . . just a little thing I had done. For you.

EVELYN: Wait, what . . . show me. (he looks around and lowers his pants to show his backside) “EAT” . . . lemme guess . . . you couldn’t afford the “me.”

ADAM: No, you goof! Your initials: Evelyn Ann Thompson. Like it?

EVELYN: I do. I like it. And I love the gesture . . .

ADAM: “Love” is a big word.

EVELYN: I know. That’s why I used it. . . (Adam freezes in scene readjusting his pants and Evelyn steps out to resume her presentation) These are surface items, to be sure, but if I, in fact, tell you that I’m going through with it and marrying the guy, you’d probably all shake my hand and say, “Wow, how can I do that to my boyfriend?” But this, I’m afraid was not done out of love or caring or concern . . . this was a simple matter of can I instill “X” amount of change in this creature, using only manipulations as my palette knife? I coaxed, made suggestions, created the illusion of interest and desire, but never said, ‘please do this.’ Not once. As my subject became handsomer, firmer and more confident, his actions became more and more . . . questionable. He had work done to his face, cosmetic surgery at age 22, and insisted to those around him that he had merely fallen down. *****Scene*****

ADAM: (To audience as if speaking with friends, gesturing to his nose) I hit it and, you know . . . I banged it pretty bad at home and so I had the doctor look at it. But he didn’t . . . operate or anything. The bandage is from that . . . (Adam freezes in scene touching his nose and Evelyn steps out to resume her presentation)

EVELYN: He was willing to give friends up when asked, walk away from them without any further contact . . . and as stated earlier these corrections culminated in an offer of marriage to me, this coming from a confirmed, albeit young, bachelor.

*****Scene*****

(We enter the scene in the middle of an argument between Evelyn and Adam – the reason for the argument is unimportant, just the conclusion)

ADAM: So, tell me what to do and I’ll do it. . . I just, I just don’t wanna lose you.

EVELYN: You’re sure . . . ?

ADAM: I am so sure. I love you . . .

EVELYN: Anything I say?

ADAM: Anything.

EVELYN: (without emotion) Give up [your] friends, both of them. No explanation. Don’t see them or speak to them again, not ever. That’s the proof to me about how you feel . . .

ADAM: Evelyn . . . that’s . . .

EVELYN: Once should always be careful when asking to be put to a test. . . so what’s it gonna be, Adam?

ADAM: . . . and if I don’t . . . ?

EVELYN: These things end. I mean, in life, at least . . . Final answer? (Adam stares at her for a long moment)

ADAM: . . . I choose you. (Adam freezes in scene after dropping to one knee as if to propose and Evelyn steps out to resume her presentation)

EVELYN: He has then been utterly and totally refashioned as a person (beat) He’s gotten more interesting, more desirable, more normal. In a word, better. He is a living, breathing example of our obsession with the surface of things, the shape of them. (to ADAM – taking off the ring) This was a startling and unexpected gesture, but obviously, I can’t accept. (To audience) I have no feelings of remorse for my actions, the manufactured emotions . . . none of it. I have always stood by the single and simple conceit that I am an artist. Only that. Art must be created, whatever the cost. (beat) @ith that in mind, I present you with my untitled sculpture. Thank you. (she hands Adam the ring, takes a short bow and steps out of the light.) *****Scene***** At the reception after Evelyn’s presentation

ADAM: . . . not a big "modern art" crowd, I guess, huh?

EVELYN: Look . . .

ADAM: Please don't "Look,” me now, okay, or I might not make it through this. . . (beat) Just refer to me as "it" or "untitled," it'll help me keep some perspective here. . . (wanders over and pours some punch. Stuffs a few cookies in pocket. Shoves three in mouth and chews them down.). . . that's gonna shoot some piece of data all to s***, isn't it?

EVELYN: Doesn't matter now, do what you want. . . you're finished.

ADAM: "You're finished." Wow. (considers) Most people just say, "Hey, sorry, can't marry you." And they say it in private. . .

EVELYN: . . . yeah, that might've been a bit too far.

ADAM: Oh shit, you are so beyond "far" that you're in danger of hitting Uranus.

EVELYN: (Smiling) See, you're still funny....

ADAM: Just stop, alright? I was never funny, or good-looking or clever. I was nothing until you started . . . I admit it. No-thing. But you know what? I was absolutely fine with that. . .

EVELYN: . . . listen, I know my work relied on not telling you what was going on, but I. . .

ADAM: Here we just call it lying. . .

EVELYN: I did lie to you, yes . . . Sorry.

ADAM: You're sorry? Well, that's good. . . I figured I was gonna have to really work to get that one out of you.

EVELYN: I'm not sorry. I mean, not for what I've done. I just feel bad that you're so upset. . . I just want to keep it as truthful as possible.

ADAM: (laughing) That'll be different. . .

EVELYN: . . . you're so angry. . . What'd I do wrong? (beat) Seriously, tell me. . .

ADAM: You don't see this as wrong?! You honestly have no concept here. . . Look, I’m not gonna stand here. . .

EVELYN: The exercising? Or was it the new clothes that really bugged you? Everything I did made you a more desirable person. People began to notice you. . . take interest in you.

ADAM: Well, lucky me.

EVELYN: (beat) Look, if you hadn't been here tonight, hadn't heard all this stuff. . . wouldn't you still be happy? Waiting at home for me, hoping this went well. . .

ADAM: That's not the point. . .

EVELYN: Yes, it is! It's the total point. All that stuff we did was real for you, therefore it was real. It wasn't for me, therefore it wasn't. It's all subjective, Everything.

ADAM: Not love. Not cruelty. Seriously? . . . Don't fool yourself and think that this is "art." 'kay? It's a sick joke, but it is not "art."

EVELYN: Is that right?

ADAM: (beat) You know, when Picasso took a s***, he didn't call it a "sculpture." He knew the difference. That's what made him Picasso. You oughta at least realize there's a price to it all...you know? Somebody pays for your two minutes on CNN. Someone always pays for people like you. And if you don't get that, then you're about two inches away from using babies to make lamp shades and calling it "furniture." (beat) Tell me, though. Was any of it true? Not the things we did, or the kind words or whatever. . . but any of it?

EVELYN: . . . No. Not really. Sorry.

ADAM: (Sarcastic) Don't be. Hey, it's. . . Art.
```

---

## IC-0260: Sickened

- Title: Sickened
- Author (byline): Julie Gregory
- Work: Not specified
- Publisher: Bantam Books, Inc.
- Publication date as stated: Sept 2004
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JULIE, MOM, DOCTOR, NURSE
- Teaser before the introduction: Yes
- Spoken words (computed): 2111
- Already set (do not supply): none

### Source block (context only)

```text
Author: Julie Gregory
ISBN: 978-0553381979
Publisher: Bantam Books, Inc.
Date (Month/Year): Sept 2004
```

### Introduction (context only: never use it for content warnings)

```text
A young girl is perched on the cold chrome of yet another doctor’s examining table, missing yet another day of school. It’s four o’clock and she hasn’t been allowed to eat anything all day. Her mother, on the other hand, seems curiously excited. She checks her teeth once more for lipstick, and as the doctor enters, shoots the little girl a warning glance. This child will not ruin her plans . . . Munchausen by Proxy is a type of child abuse in which a parent exaggerates, fabricates, or induces symptoms of a medical condition in a child that leads to unnecessary and potentially harmful medical care. Julie Gregory was a victim . . . and this is her story:

Sickened by Julie Gregory.
```

### Performance text (classify this)

```text
JULIE: (Pg 3) For starters, I was a sick kid. Bean-pole skinny, I bruised easy and wilted in a snap. Kids in school used to walk straight up to me and ask point-blank if I was anorexic. But I wasn’t; just sick. And Mom bent over backwards trying to find out what was wrong with me. It wasn’t just that I had a heart problem. It was everything rolled into one, bleeding together with so many indistinguishable layers that to get to the root of it was impossible, like peeling off every layer of an onion, and when I got old enough to peel the onion myself, every layer made me cry.

MOM: (Pg 4) Look, dammit, this kid is sick, all right? Just look at her. And so help me God, if she dies on me because you can’t find anything wrong with her, I’ll sue you for every sent you got.

JULIE: Her voice trailed after any doctor who said no more tests could be done, stalked him down the corridor, sliced through the silence of the hallway. (to Mom) Don’t worry, Mom. It’s okay. We’ll go find another one.

MOM: Look, I’m sacrificing my life to find out what the hell is wrong with you. So stop *screwing* it up when we get in here by acting all normal. Show them how sick you are, okay?

JULIE: (Pg 23) Today, I’m back at [the doctor] getting seen for my headaches. Mom and I sit in the examining room, waiting.

MOM: How do you act when you’re sick, Julie? Show me.

JULIE: (slouches, limbs dangling, tongue out and bottom lip away from her teeth, a glazed expression on her face)

MOM: That’s right. Now what do you think the doctor is going to say if he comes in here and you’re sitting up and all smiling? Do you think he’s going to believe me that you’re sick? You got to show him how sick you are. (Doctor enters)

DOCTOR: So you say Julie’s been running a fever along with some sore throats? (taking notes in Julie’s chart)

MOM: (Pg 26-27) Well, I’ve caught it up at a hundred and one, but it seems to be low grade all the time and she has these, oh, I don’t know what you’d call them, headaches, I guess, don’t you Julie?

JULIE: I look between both of them. What is a headache exactly? Is it when my eyes hurt? Is it when I’m dizzy on the bus? I’m trying to guess, hoping it’s the right answer. (to Mom and Doctor) I’m not really sure.

MOM: Jesus, Julie, we’ve been seeing you sick and you’ve been telling me you’ve had headaches in the car all this week. Remember when you’ve been carsick? (to Doctor) There’s got to be something wrong with a kid that doesn’t even remember how sick she was just yesterday. (to Julie) Julie, stop wasting the man’s time and tell him what’s going on with you. (threateningly) I mean it!

JULIE: (Pg 28-29) Another week has gone by and nothing has changed. Mom and I sit in [the doctor’s] office waiting for Dr. Phillips.

MOM: Now, we’re going to tell Dr. Phillips about the dull pains in your head, right about (pushes fingers into Julie’s skull, hard) here. I don’t want any kind of fiasco like we had the last time, okay? I’m the mom: I know what’s going on here. So if he asks you questions, you just let me answer.

JULIE: Dr. Phillips breezes in and apologizes for our wait. Mom gives him an update on my allergy diet and pulls out her list of new symptoms. I sit in my sick pose. As she runs down the symptoms, I know some of them aren’t true. (Pg 30) No, I don’t have a sore throat every day, just yesterday. No, my fever last night wasn’t way up to 102. No, I don’t go to the school nurse every single day . . . [In fact] (Pg 32) it was usually after Mom slipped the little white pill under my tongue that my migraines got worse.

MOM: I can tell you’ve got a headache coming on. Here, open up. Lift your tongue. Goooood.

JULIE: Sometimes I about threw up. Most times I just needed to climb back into bed . . . (Pg 50-51) [Three years pass and] when fifth grade begins, Dr. Phillips prescribes us more migraine medicine and gives us the names of specialists who can see me for the rest of my symptoms. He tells us we should [find] somebody who can handle a case that’s as complicated as mine’s getting. And then he leaves. He just walks right out before Mom is even done running down the list she brought.

MOM: I can’t believe that. Did you see him, Julie? He just walked out on us! Well, if he’s going to treat me like that, Jesus!

JULIE: (resigned) Don’t worry, Mom, we’ll just go find another one. (Pg 52) (to audience) That night Mom curls up on the sofa, with her grocery store reading glasses hanging on to the tip of her nose, cornering through the pages of the thick Medical Journal for Home Use Manual. (to Mom) Whatcha doing, Mommy?

MOM: Well, you’re sick again, hon, and this book is helping Mommy figure out what’s wrong with you. You got a lot of the symptoms in here, but there’s all kinds of tests that’ll help us rule out some of the more serious diseases.

JULIE: [Later that night] (Pg 84-86) the doorknob on my bedroom door slowly squeaks open. Mom tiptoes to the edge of my bed. That’s when I notice the gun in her mouth. (Julie enters flashback ad responds immediately with a look of horror) She looks at me with her tear-streaked, puffy face, her eyes terrified like an animal in a chute, and raises her hand to cock the trigger. “Mommy, Mommy, Mommy!” (to audience) I shoot from under the covers and start crying on cue. Mimic and match. If I mirror her with an appropriate response, she’ll be distracted from the gun.

MOM: (she slides the gun out of her mouth) You want me to kill myself, don’t you? You hate me. I’m such a bitch, such a nag as your father says, and you hate me, that’s what he says.

JULIE: She drops the gun to her lap. I cling around her like a baby monkey. (To Mom) Mom, if you don’t live then I can’t live. Okay? Okay? Who would take care of me when I’m sick; who would take me to the doctor? (to audience) I hang on to her, slipping the gun so lightly from her lap she doesn’t notice, sliding it under my blankets. (To Mom) It’s okay, it’s okay, Mom. (to audience) And the harder I cry, the less my beautiful mother, who I could never live a second without, does. And then she stops altogether, straightens up, gives my knee a little squeeze and says

MOM: (in an upbeat mood; cheerful) Hey, thanks for listening, Sis. You better get to sleep now, honey.

JULIE: And she leaves me on the edge of my mattress with a loaded gun under my covers. [*Spoken Transition -- A few weeks later]

DOCTOR: (Pg 97-101) There’s a substantial difference in Julie’s heart rate when she stands up from when she’s at rest, Ms. Gregory.

MOM: (to Julie) Tell her how out of breath you are, Julie. (to doctor) She’s always out of breath around the farm, Dr. Kate. Jesus! (slaps her knee) This explains everything. (to Julie) You look like you’re about ready to pass out, hon. Don’t you feel like you could pass out?

DOCTOR: I think we might have something for the hospital here, something that could be detected with simple EKG or a heart exam. They might even want to attach something called a Holter monitor on her overnight to see the longer rhythms of her heart. I’ll call over to the cardiac unit and get you set up.

MOM: Yess – Yeeeessss! (gleefully) Finally, we’re getting somewhere. (to Julie) I knew there was something major going on with you!

JULIE: We’re going to the hospital! At last, I’ll just take one medication that will fix everything. I’ll have friends, be in sports, go to movies. And I’ll be a real kid and not miss school anymore. I’ll do good in school like before I got sick. I’m [only] failing because there’s always something wrong with me.

[*Spoken Transition -- After the cardiac tests]

DOCTOR: (Pg 101) Well, Ms. Gregory, we’ve got good news. The Holter monitor shows no significant findings that lead us to believe Julie has a heart condition requiring further tests.

MOM: What? What do you mean, you can’t find anything. This kid had a racing heart and was out of breath all the time. Are you trying to tell me that this kid is normal? That I’m making this up? Well, let me tell you. I’m going to find a doctor competent enough to find out what’s wrong with her, you understand me?

JULIE: (Pg 104-105) The older I got, the worse I got. My possible conditions expanded to include genetic disorders and heart valve malfunctions. And the medications to treat them piled up in the kitchen cabinets. Sometimes I don’t take any, sometimes I get a double dose. I just feel sick all the time. Queasy, nauseated, clammy, stupid. . . By the time I was in Junior High, Mom decided I was allergic to a lot of things.

MOM: Julie, what the heck are you doing with those [eggs]? You know you’re allergic.

JULIE: I slide the eggs back and reach for the bacon.

MOM: At-at-at, we just got done telling Dr. Kate how meat makes you sick. Why don’t you just have a bowl of Sugar Pops? But use the powdered milk, just enough to get them wet, you could be lactose intolerant.

JULIE: (Pg 111) How long can you starve without side effects? If everyone around you tells you you’re sick, if they keep testing you for what’s making you sick, do you think, when you’re thirteen, that you aren’t? You feel sick, right? You can’t keep up; you’re tired. Is it the wrong mediation that makes you sick? Or the three different kinds you take all at once? . . . . (Pg 113-114) We’re on our way to a new cardiologist. This will be the third and if he can’t find anything, Dr. Kate says it’s probably not my heart.

MOM: I’ll show those goddam no-good sons a bitches at the hospital that I’m not crazy. You are sick, goddammit, you’ve got a heart problem. (glaring at Julie) C’mon now, let’s get in there, and I mean now, goddammit. You are going to tell him what’s wrong with you. Sharp chest pain. Shortness of breath. You got it? [*Spoken Transition -- So more tests are run and when the results come back . . . ]

DOCTOR: (Pg 115-116) Well, it looks like what we’ve got here is a possible case of periodic rapid heart action.

MOM: Does that mean we’ll have to go in for open-heart? I mean seriously, I’m not opposed to it if we can really find out what’s going on here. I’ve been reading up on a new pediatric valve syndrome, and . . .

DOCTOR: Oh, no, I don’t think we’re going to need that. What we really should do is some more tests under the close eye of hospital staff. Could we get Julie into Ohio State for a week and run a comprehensive assessment? [*Spoken Transition -- After 4 days in the hospital]

NURSE: (Pg 121-124) We’re going to have to shave you now, honey. Down here. (pats for Julie’s pubic bone)

JULIE: What? I’m done, I’m going home. I don’t have anything down there! (covering her private parts) I’m here for my heart!

NURSE: Tomorrow they’re going to make a little incision in the vein of your arm and the artery of your thigh and run some electrical connectors into the values of your heart so they can see it on TV.

JULIE: (to audience) This has got to be a mistake. How did this happen? They’re going to cut me. (breath quickens, as Julie’s eyes widen in horror – To nurse) You, you can’t do this to me. You can’t do it . . . My mother is making it up! (long horrified pause then to audience) I can’t believe I blurted that out. My mother loves me. There’s something wrong with me. If I wasn’t sick the doctors wouldn’t keep trying to fix me . . . Maybe I was acting sicker because [mom] slammed my head against the inside of the window on the way home if I didn’t show them how sick I was.

NURSE: (puzzled) Be back in a sec. Let me see what’s going on.

JULIE: Mom’ll be furious! . . . I don’t care. I can run away. Find a new family. . . . [No,] Mom knows what she’s doing. She’s the one who sees my symptoms.

(Pg 131) Heart surgery, iodine injections, tubes shoved, slits sliced, blood drawn. These things change a kid. You forget what you were like before they cut you, before they shaved you. You only look to the future when they’ll find what’s wrong so it can all be over; the tests, the trying, the meds you swallow without knowing why.

[Today, as an adult] (Pg 221-222) I cry from the guilt of betraying my mother, for not keeping the shroud of her secrets. I have been writing about what it feels like to be cut open while your mother’s tight, thin smile mouths, “Doctor’s orders, honey.” And to believe you are genuinely ill because that is what everything in your world mirrors back to you. I still told myself that it was okay, it really wasn’t that bad . . . [after all,] if a doctor couldn’t decipher what she did, how could I?
```

---

## IC-0261: Silver Water

- Title: Silver Water
- Author (byline): Amy Bloom
- Work: Come to Me: Stories
- Publisher: Perennial Press
- Publication date as stated: April 1994
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: VIOLET, MOTHER, THERAPIST, ROSE, FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1746
- Already set (do not supply): none

### Source block (context only)

```text
Author: Amy Bloom
Book: Come to Me: Stories
ISBN: 978-0060995140
Publisher: Perennial Press
Date (Month/Year): April 1994
```

### Introduction (context only: never use it for content warnings)

```text
Silver Water by Amy Bloom
```

### Performance text (classify this)

```text
VIOLET: (Pg 87-100) My sister’s voice was like mountain water in a silver pitcher. After we went to [the opera], when she was fourteen and I was twelve, she elbowed me in the parking lot and said, “Check this out” And she opened her mouth wide and her voice came out, so crystalline and bright that all the departing opera-goers stood frozen by their cars, unable to take out their keys until she had finished.

That’s what I like to remember . . . That before her constant tinkling of commercials and fast-food jingles there had been Puccini and Mozart and hymns so sweet you expected Jesus to come down off his cross and clap. That before there was a mountain of Thorazined fat, swaying down the halls in sweatpants, there had been the prettiest girl i Landmark Junior High. To me, Rose, my beautiful blond defender, was perfect.

VIOLET: She had her first psychotic break when she was fifteen. She had been coming home moody and tearful, then quietly beaming, then she stopped coming home. She would go out into the woods behind our house and not come in until my mother went after her and stepped into the briars and saplings and pulled her out, blank-faced, her sweater covered with crumbled leaves, her jeans smeared with dirt. After three weeks of this, my mother said to my father:

MOTHER: David, she’s going crazy. She needs a hospital.

VIOLET: Rose was in hospitals, great and small, for the next ten years. She had lots of terrible therapists and a few good ones. The worst family therapist we ever had sat in a pale green room with us, read Rose’s file in front of us and then watched in alarm as Rose began crooning, beautifully, and slowly massaging her breasts. My mother and I laughed, and even my father started to smile. This was Rose’s usual opening salvo for new therapists.

THERAPIST: I wonder why it is that everyone is so entertained by Rose behaving inappropriately.

VIOLET: Rose burped, and we all laughed. This was the seventh family therapist we had seen, and none of them had lasted very long.

THERAPIST: What do you think of Rose’s behavior, Violet?

VIOLET: I don’t know. Maybe she’s trying to get you to stop talking about her in the third person.

ROSE: That was not a successful intervention, Ferret Face.

VIOLET: He did look like a blond ferret, and we all laughed again. The day we met our best family therapist started out almost as badly. We scared off a resident and then scared off her supervisor, who sent us Dr. Thorne. Dr. Thorne was good for us, Rose moved into a halfway house, took her meds, lost about fifty pounds, and began singing at the A.M.E. Zion Church, down the street from the halfway house.

At first, they didn’t know what do to with this big blond lady, dressed funny and hovering wistfully in the doorway during their rehearsals, but she gave them a few bars of “Precious Lord” and the choir director felt God’s hand.

Rose and the choir’s contralto, Addie Robicheaux, laid out their gold and silver voices and wove them together in strands as fine as silk, as strong as steel. And we wept as Rose and Addie, in their billowing garnet robes, swayed together clasping hands until the last perfect note floated up to God. Rose would still go off from time to time and the voices would tell her to do bad things, but Dr. Thorne or Addie or my mother could usually bring her back . . . [And then] after five good years, Dr. Thorne had an aneurysm and died.

Rose stopped taking her meds, and the halfway house wouldn’t keep her after she pitched a patient down the stairs. My father called the insurance company and found out that Rose’s new psychiatric coverage wouldn’t begin for forty-five days. I put all of her stuff in a garbage bag, and we walked out of the halfway house.

My father convened a family meeting:

FATHER: This is going to be difficult--not all bad, but difficult--for the whole family, and I thought we should discuss everybody’s expectations. I know I have some concerns.

ROSE: (with lowered eyes, as she frantically pulled at her clothing) No meds!

VIOLET: My father looked in despair at my mother.

MOTHER: Rosie, do you want to drive the new car?

ROSE: (face lighting up, she speaks manically) I’d love to drive that car, I’d drive to California, I’d go see the bears at the San Diego Zoo, would take you, Violet, but you always hated the zoo. Remember how she cried at the Bronx Zoo when she found out that the animals didn’t get to go home at closing?

MOTHER: If you take your medication, after a while you’ll be able to drive the car. That’s the deal. Meds, car.

ROSE: You got yourself a deal, darlin’.

VIOLET: I was living about an hour away then, teaching English. I went home every few days for dinner. I called every night:

FATHER: (On the phone, quietly) It’s very hard. We’re doing all right, I think, Rose has been walking in the mornings with your mother and she watches a lot of TV. She won’t go to the day hospital, and she won’t go back to the choir. I’m sorry, sweetheart, don’t mean to depress you.

VIOLET: I stayed away all week, afraid to pick up my phone. On Sunday, I came in the early afternoon, to help my father garden. We weeded and staked tomatoes while my mother and Rose were down at the Lake. I didn’t even go into the house until four, when I needed a glass of water. Someone had broken the piano bench into five neatly stacked pieces and placed them where the piano bench usually was.

FATHER: We were having such a nice time, I couldn’t bear to bring it up.

VIOLET: What did Mommy say?

FATHER: She said, ‘Better the bench than the piano.’ And your sister lay down on the floor and just wept. Then your mother took her down to the lake. This can’t go on, Vi. We have twenty-seven days left, your mother gets no sleep because Rose doesn’t sleep, and if I could just pay twenty-seven thousand dollars to keep her in the hospital until the insurance takes over, I’d do it.

VIOLET: All right. Do it. Pay the money and take her back.

FATHER: I would if I could. The policy states that she must be symptom-free for at least forty-five days before her coverage begins. Symptom-free means no hospitalization.

VIOLET: Jesus, Daddy . . . She hasn’t been symptom-free for forty-five minutes.

FATHER: It’s the only one I could get for long-term psychiatric. (near tears, he places his hand over his mouth, to block whatever he was about to say, and goes back out to the garden).

VIOLET: He stayed outside and I stayed inside. Rose and my mother came home from the lake. My mother kissed me lightly and told Rose to go up to her room and change out of her wet pants.

ROSE: (eyes growing very wide) Never. I will never. . .! (Begins rocking violently)

VIOLET: She knelt down and began banging her head on the kitchen floor with rhythmic intensity, throwing all her weight behind each attack. My mother put her arms around Rose’s waist and tried to hold her back. Rose shook her off, not even looking around to see what was slowing her down.

MOTHER: Violet, please . . .

VIOLET: I threw myself onto the kitchen floor, becoming the spot that Rose was smacking her head against. She stopped a fraction of an inch short of my stomach.

ROSE: (stopping her violent rocking) Oh Vi, Mommy, I’m sorry. I’m sorry don’t hate me! (she rushes from the room wailing)

VIOLET: Dinner was filled with all of our starts and stops and Rose’s desperate efforts to control herself. She could barely eat and hummed the McDonald’s theme song over and over again, pausing only to spill her juice down the front of her smock and begin weeping.

ROSE: (Rocking and chanting) I want to go to bed, I want to go to bed and be in my head. I want to go to bed and be in my bed and in my head and and and and . . . .

FATHER: Okay, okay, Rose. It’s okay. I’ll go upstairs with you and you can get ready for bed. Then Mommy will come up and say good night too. It’s okay, Rose.

VIOLET: My father reached out his hand and Rose grasped it, and they walked out of the dining room together, his arm around her middle. [A short time later] my father came into the kitchen and signaled to my mother. They went upstairs and came back down together and we went to sit on the porch and listen to the crickets. I don’t remember the rest of the evening, but I remember it as quietly sad, and I remember the rare sight of my parents holding hands, sitting on the picnic table, watching the sunset.

I woke up at three o’clock in the morning. I went down the hall and looked into Rose’s room, for no reason. She wasn’t there. I could feel her absence. I went outside and saw her wide, draggy footprints darkening the wet grass into the woods. (in a loud whisper) Rosie. Rosie, it’s me. Are you here? Are you all right?”

I almost fell over her. Huge and white in the moonlight, her flowered smock bleached in the light and shadow, her sweatpants now completely wet. Her head was flung back, her white, white neck exposed like a lost Greek column. Her breathing was very slow, and her lips were not as pink as they usually were. Her eyelids fluttered.

ROSE: (whispering) Closing time . . .

VIOLET: I believe that’s what she said. (Long beat) I sat with her, uncovering the bottle of Seconal by her hand, and watched the stars fade. When [they] were invisible and the sun was warming the air, I went back to the house. My mother was standing on the porch, wrapped in a blanket, watching me.

MOTHER: Warrior queens . . . I raised warrior queens.

VIOLET: She kissed me fiercely and went into the woods by herself. Later in the morning she woke my father, who could not go into the woods, and still later she called the police and the funeral parlor. She hung up the phone, lay down, and didn’t get back out of bed until the day of the funeral. (Long beat) My mother played the piano and Addie sang her pure gold notes and I closed my eyes and saw my sister, fourteen years old, lion’s mane thrown back and eyes tightly closed against the glare of the parking lot lights.

(Quietly sing first stanza of “Precious Lord, Take My Hand” hymn; Lyrics and Music by Thomas A. Dorsey)

Precious Lord, take my hand
Lead me on, let me stand
I'm tired, I’m weak, I’m lone
Through the storm, through the night
Lead me on to the light
Take my hand precious Lord, lead me home.

https://www.youtube.com/watch?v=fRGTR_wUje8
```

---

## IC-0262: Sixteen

- Title: Sixteen
- Author (byline): Maureen Daly
- Work: Twenty Grand Short Stories
- Publisher: Bantam
- Publication date as stated: 1963
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1501
- Already set (do not supply): none

### Source block (context only)

```text
Author: Maureen Daly
Book: Twenty Grand Short Stories
ISBN: B000MOQK3U
Publisher: Bantam
Date(Month/Year): 1963
```

### Introduction (context only: never use it for content warnings)

```text
One could fall in love many times during the course of a lifetime, but the first rush of love always holds a special place in our hearts. The novelty of the feeling, like the first drops of dew on an untouched leaf, makes it special and unforgettable. Author Maureen Daly (only sixteen herself) wrote the short story Sixteen which subsequently won the O. Henry award for literature. Set in the 1950’s, the same period in which she was a teen, she speaks from the heart as she paints a vivid portrait of first love. Many assume that her work is autobiographical. Sixteen by Maureen Daly.
```

### Performance text (classify this)

```text
N

ow don't get me wrong. I mean, I want you to understand from the beginning

that I’m not really so dumb. I know what a girl should do and what she shouldn't. I get around. I read. I listen to the radio. And I have two older sisters. So you see I know what's what. I know it's smart to wear tweed skirts and tight fitting sweaters and ballerina shoes. And I know that your hair should be short with that look of careful carelessness, and the peasant hankie should be draped cleverly around your neck, fastened with a ring. Now, me, I never wear a hankie, it makes my face seem too wide. I'm not exactly too small-town either. I read the Broadway columns. You get to know what New York boy is crazy about what Hollywood actress on the West Coast and what starlet is currently the prettiest and who eventually, will play Joan of Arc. It gives you that worldly feeling. I know that it is absolutely forbidden to wear colored ankle-socks with high-heeled shoes or use Evening in Paris perfume with a tweed suit. But this isn't what I wanted to tell you. I just wanted to give you the general idea that I'm not so dumb. It is important that you understand that.

You see, it was funny how I met him. It was winter night like any other night. And I didn't have my chemistry done either. But the way the moon silvered the twigs and the snow-drifts, I just could not stay inside. The skating rink isn't far from our house - you can make it in five minutes if the side walks aren't slippery, so I went skating. I remember it took me a long time to get ready that night because I had to darn my skating socks first. I don't know why they are always wear out so fast - just in the toes, too. And then I brushed my hair hard, so hard it clung to my hand and stood up around my head.

My skates were hanging by the back door all nice and shiny, for I'd just gotten them for Christmas and they smelled so queer. My dog walked with me as far as the corner. She panted along beside me and her hot breath made a frosty little balloon on the end of her nose. The night was breathlessly quiet and the stars winked down like a million flirting eyes. It was all so lovely.

It was all so lovely; I ran most of the way and it was lucky the sidewalks had ashes on them or I would have slipped.

I had to cut across someone's back garden to get to the rink, and I was out of breath when I got to the shanty - out of breath with running and with the loveliness of the night. Shanties are always such friendly places. There was a delicious smell from the iron stove. Girls burst through the door laughing with snow on their hair. A boy grabbed the hat from a blonde and stuffed it into an empty shoe.

It didn't take me long to get my own skates on and I put my shoes under the bench - far back where they wouldn't get knocked around and would be easy to find when I wanted to go home. I walked out on my toes into the night air.

It was snowing a little outside - quick, eager little flakes that melted as soon as they touched your hand. I don't know where the snow came from for there were stars out. Or maybe the stars were in my eyes and I just kept seeing them every time I looked up into the darkness. I waited a moment. You know, to start to skate at a crowded rink is like jumping on a moving merry-go-round. Once in, I went all right. At least, after I found out exactly where the rough ice was. It was "round, round, jump the rut, round, round, jump the rut, round, round - ."

~ II ~

A

nd then he came. All of sudden his arm was around my waist so warm and tight

and he said, "Mind if I skate with you?" and then he took my other hand. That's all there was to it. Just that and then we were skating. It wasn't that I had never skated with a boy before. Don't be silly. I told you before I get around. But this was different. He was smooth! He was a big shot up at school and the best dancer in town. Don't you see? This was different.

At first I can't remember what we talked about, I can't even remember if we talked at all. We just skated and skated and laughed every time we came to that rough spot and pretty soon we were laughing all the time at nothing at all. It was all so lovely.

Then we sat on the big snow bank at the edge of the rink and just watched. It was cold at first, even with my skating pants on, sitting on that hard heap of snow, but pretty soon I got warm all over. He threw a handful of snow at me and it fell in a little white shower on my hair and he leaned over to brush it off. I held my breath. The night stood still.

Then he sat up straight and said, "We'd better start home." Not "shall I take you home?" or "Do you live far?" but "We'd better start home." See, that's how I knew he wanted to take me home. Not because he had to but because he wanted to. He went to the shanty to get my shoes. "Black ones", I told him. "Same size as Garbo's." And laughed again. He was still smiling when he came back and took off my skates and tied the wet skate strings in a knot and put them over his shoulder. Then he held out his hand and helped me up from the snow bank. I brushed off the seat of my pants and we were ready.

It was snowing harder now. Big, quiet flakes that clung to us lovingly. It was all so lovely that I was sorry I lived only a few blocks away. He talked softly as we walked as if every little word was a secret. "Did I like swing and did I plan to go to college next year and had I a cousin who knew his brother?" A very respectable sort of conversation and then finally - "How nice I looked with snow in my hair and had I ever seen the moon - so close?" and then we were home.

The porch light was on. My mother always puts the porch light on when I go away at night. And we stood there a moment by the front steps and the snow turned pinkish in the light and a few feathery flakes settled on my hair. Then he took my skates and put them over my shoulder and very, very close to my cheek softly said, "Good night now. I'll call you," he said.

I went inside then and in a moment he was gone. I watched him from my window as he went down the street. I could hear him whistling softly and I couldn't tell if it was he or my heart whistling out there in the night. And then he was gone, completely gone.

I shivered. Somehow the darkness seemed changed. The stars were hard little lights up in the sky and the moon had a sharp yellow glare. The air was suddenly cold and the wind wiped out his footsteps. Everything was quiet.

But he'd said, "I'll call you." That's what he said, "I'll call you." I couldn't sleep all night.

And that was last Thursday. Tonight is Tuesday. Tonight is Tuesday and my homework is done and I darned some stocking that really didn't need it, and I worked a cross-word puzzle and I listened to the radio and now I'm just sitting. I'm just sitting because I can't think of anything else to do. I can't think of anything, anything but snowflakes and ice skates and a yellow moon and Thursday night. The telephone is sitting on the corner table with its old black face turned to the wall. I don't even jump when it rings any more. My heart still prays but my mind just laughs. Outside the night is still - so still I think I'll go crazy. And so I'm sitting here and I'm not feeling anything. I'm not even sad because all of a sudden I know. I can sit here now and forever and laugh and laugh while the tears run salty in the corners of my mouth. For all of a sudden, I know, I know what the stars knew all the time - he will never, never call - never.
```

---

## IC-0263: Small Great Things

- Title: Small Great Things
- Author (byline): Jodi Picoult
- Work: Not specified
- Publisher: Ballantine Books
- Publication date as stated: Oct 2016
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: RUTH, KENNEDY, PROS. ATTORNEY
- Teaser before the introduction: Yes
- Spoken words (computed): 2363
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jodi Picoult
ISBN: 978-0345544957
Publisher: Ballantine Books
Date (Month/Year): Oct 2016
```

### Introduction (context only: never use it for content warnings)

```text
Ruth Jefferson is a labor and delivery nurse with more than 20 years’ experience. During a shift, she begins a routine checkup on a newborn, only to be told a few minutes later that she’s
```

### Performance text (classify this)

```text
RUTH: (Pg 323-324) (to audience) We all do it, you know. Distract ourselves from noticing how time’s passing. We throw ourselves into our jobs. We fill up our gas tanks and do the grocery shopping so that the weeks look the same on the surface. If you only see the path that’s right ahead of you, you don’t obsess over when the cliff might drop off. Some of us never learn. And some of us learn earlier than others. (Deep breath in through her nose, she holds it and then releases it through her mouth)

KENNEDY: (Pg 326) (to audience) Bad things happen to good people every day. (Pg 195) (to Ruth, breezily) Well, first, do you prefer the term black or African American or people of color?

RUTH: (Beat) People of color.

KENNEDY: Frankly, I don’t even see color. I mean, the only race that matters is the human one, right? (Ruth presses her lips tightly together)

been reassigned. Why? In the voice of the father, TURK BAUER: (Pg 21)“I don’t want her or anyone who looks like her touching my son!” (silent beat) The hospital complies and flag the baby’s chart: (Pg 43) NO AFRICAN AMERICAN PERSONNEL TO CARE FOR THIS PATIENT. But the next day, the baby goes into cardiac distress while Ruth is alone in the nursery. She hesitates before performing CPR and, as a result, is charged with murder. Kennedy McQuarrie, a white public defender, takes her case, and insists that mentioning race in the courtroom is NOT a winning strategy. (shake head and sigh) (Pg 464) Yes, talking about racism is hard to do, and yes, we stumble over the words - but we need to have this discussion . . . because then, more will overhear, and - I hope - the conversations will spread.

Small Great Things by Jodi Picoult

***As the trial concludes***

KENNEDY: (Pg 392-395) I don’t think you should get on the stand.

RUTH: You promised . . . You promised I could say my piece.

KENNEDY: [The judge] threw out the murder charge. The worst-case scenario – a conviction of negligent homicide carries almost no jail time . . . and honestly our medical evidence was so strong that I’d be shocked if the jury doesn’t acquit. We’ve created reasonable doubt. That’s all we have to do to win. The jury hands back the verdict, and you go get your job back. You get to pretend this never happened.

RUTH: You think I can pretend this never happened? I see this every day, everywhere I go. You think I’m going to just walk in and get my job back? You think I’m not always going to be that black nurse who caused trouble.

KENNEDY: Ruth, I’m 99 percent sure this jury is going to find you not guilty. What more could you possibly want?

RUTH: (crosses her arms in determination) You still have to ask?

KENNEDY: (to audience) I know what she is talking about. Namely, everything I refused to talk about in court: what it is like to know that you are a target, because of the color of your skin. What it means to work hard, to be an impeccable employee, and have none of that make a difference in the face of prejudice.

RUTH: I know how the law works, Kennedy. You have to put me on the stand if I ask you to. So I suppose the question is: Are you going to do your job? Or are you going to be just one more white person who lied to me?

KENNEDY: What the hell? Now is not the time to stand on principle. If you get on the stand and start talking about race, you’ll erase the lead we currently have. You’ll be talking about issues that will alienate [the jury] and make them uncomfortable. Plus, the fact that you’re upset and angry . . .

RUTH: (Pg 407-408) I am angry. I have been angry for years. I just didn’t let it show. 365 days a year, I have to think about not looking or sounding too black, so I play a role. It’s exhausting. It’s so goddamned exhausting. But I do it, because I don’t have bail money. I do it because I have a son. I do it because if I don’t, I could lose my job. My house. Myself.

So instead, I work and smile and nod and stay silent and pretend to be satisfied, because that is what you people want – no – need me to be. And the great, sad shame is that for too many years of my sorry life, I have bought into that farce. I thought if I did all those things, I could be one of you. (beat) You told me you could represent me, Kennedy. You can’t represent me. You don’t know me. You never even tried. (deliberate beat – then with conviction) (Pg 395) You are putting me on that stand tomorrow or (Pg 408) you’re fired.

KENNEDY: (to audience) (Pg 395) And just like that, I know I’m going to lose this case.

**** The next day in court – Kennedy calls Ruth to the stand ****

KENNEDY: (Pg 401-404) When did you next see the baby?

RUTH: Saturday morning. I was in the nursery when the baby’s new nurse brought him in for a circumcision. I assumed it all went normally. Then Corinne grabbed me and asked me to watch over him because another one of her patients had to be rushed to the OR. Protocol required that the baby be monitored.

KENNEDY: When you first saw the baby, how did he look?

RUTH: Beautiful . . . But a few moments later I saw that his skin was ashen. I could see he was having trouble breathing.

KENNEDY: What did you do in that instant, Ruth?

RUTH: I started tapping his feet, trying to get him to respond.

KENNEDY: When you’d been told by your supervisor to not touch that baby?

RUTH: I had to . . . It’s what any good nurse would do. But I heard footsteps. I didn’t know what to do. I thought I’d get in trouble if someone saw me interacting with the baby . . . so I wrapped him up again and stepped back. Marie walked into the nursery. She asked me what I was doing. (long pause) I said I was doing nothing.

KENNEDY: You lied . . . when you were questioned by the police, you stated you did not engage in any resuscitative efforts for that baby. Why?

RUTH: I was afraid I was going to lose my job. Every fiber of my being told me I had to help that infant . . . but if I lost my job . . .

KENNEDY: So you basically faced either assisting in malpractice, or violating your supervisor’s order?

RUTH: It was a lose-lose situation. The code team was called in. My job was to do compressions. I did my best, we all did, but in the end it wasn’t enough. (softly at first, but with a growing bitterness) It’s funny. You think you’re a respected member of a community – the hospital where you work, the town where you live. But it was just an optical illusion. I was never a member of any of those communities. I was tolerated, but not welcomed. I was, and will always be, different from them. And because of the color of my skin, I will be the one who’s blamed.

KENNEDY: Nothing further . . .

PROS. ATTORNEY: (Pg 405-407) (approaching the witness box) At the moment that baby died deep down, you didn’t really give a damn, right, Ruth?

RUTH: Of course, I did!

PROS. ATTORNEY: (aggressively, voice rising as she physically moves into Ruth’s space) Ah, but this was the baby of a white supremacist. The baby of a man who called into question your ability to do your job simply because of the color of your skin. You resented Turk Bauer, and you resented his baby, didn’t you?

RUTH: (as the Pros. Attorney continues, overlapping) You’re wrong . . . I never thought that . . .

PROS. ATTORNEY: Or maybe you were thinking: This baby doesn’t deserve my help. His parents don’t want me touching him because I’m black, and they’re gonna their wish.

RUTH: (growing more and more agitated) That’s not true . . .

PROS. ATTORNEY: (Still on the attack) You were thinking: I hate his racist parents! Or maybe it was I hate this baby because I hate his racist parents.

RUTH: (holds her hands to her head) No! I was thinking that baby was better off dead than raised by him (she points to Turk Bauer –realizes what she has done and places a shaking hand over her mouth . . . silence)

*****

KENNEDY: (Pg 407) (to audience) I grab Ruth’s wrist as soon as we are dismissed and drag her to the conference room. (angrily to Ruth) Congratulations. You did exactly what you weren’t supposed to do, Ruth. Are you happy you got up on the stand to testify? All the jury is going to see now is an angry black woman. One who was so pissed off and vengeful that I wouldn’t be surprised if the judge regrets dismissing the count of murder. You gave those jurors every reason to believe you were mad enough to let that baby die before your eyes.

RUTH: (sneering) Look at you. You’re so proud of being a public defender and working with people of color. (breathing heavily) Prejudice goes both ways, you know. There are people who suffer from it, and there are people who profit from it. Who died and made you Robin Hood? Who said I ever needed saving. Here you are on your high horse, telling me I screwed up this case that you worked so hard on; patting yourself on the back for being an advocate for a poor, struggling black woman like me . . . but you’re part of the reason I was down on the ground to begin with. (she exits)

KENNEDY: (Pg 415) (frustrated, angry – she calms herself and reflects) Maybe I’m wrong. I’ve spent months telling Ruth that a criminal lawsuit is no place to bring up race. If you do, you can’t win. But if you don’t, you are perpetuating a flawed system, instead of trying to change it. That’s what Ruth has been trying to say, but I haven’t listened. She’s brave enough to risk losing her job, her livelihood, her freedom to tell the truth, and I’m the liar. I told her race isn’t welcome in the courtroom, when deep down I know it’s already there. It always has been. Just because I close my eyes doesn’t mean it’s gone away . . . Ruth accused me of wanting to save her. But she doesn’t need saving. Who am I to give advice when I haven’t lived her life?

**** The following day – Kennedy’s Closing argument****

KENNEDY: (Pg 428-429) Ladies and gentlemen, I told you when we started this case that it was about Ruth Jefferson being presented with an impossible choice: to do her job as a nurse, or to defy her supervisor’s orders. But this case is about a lot more. Out of all the people who interacted with Davis Bauer during his short life, only one is being charged with a crime: Ruth Jefferson. I spent an entire trial skirting a very important question: Why?

RUTH: (Pg 49) (as Kennedy gives her closing arguments, Ruth speaks her mind to the audience) Are we gonna talk about it, or are we gonna pretend nothing’s wrong? (Pg 43) NO AFRICAN AMERICAN PERSONNEL TO CARE FOR THIS PATIENT

KENNEDY: (Pg 429) Ruth is black. That rubbed [the baby’s father] the wrong way. He can’t stand black people, or Asian people, or gay people, or anyone who isn’t like him. He set into motion a chain of events that would lead Ruth to becoming a scapegoat for the tragic death of his son. I don’t think it’s right to ignore the truth any longer.

RUTH: (Pg 170) They put me in chains. Just like that, they shackle my hands in front of me, as if that doesn’t send two hundred years of history running though my veins like an electric current. As if I can’t feel my great-great-grandmother and her mother standing on an auction block. They put me in chains, and my son – who I’ve told, every day since he was born, You are more than the color of your skin – my son watches.

KENNEDY: (Pg 431) I bet you feel uncomfortable right now. You know, so do I. It’s hard to talk about this stuff without offending people, or feeling offended.

RUTH: (Pg 238) You say you don't see color … but that's all you see. You're so hyperaware of it, and trying to look like you aren't prejudiced, you can't even understand that when you say race doesn't matter all I hear is you dismissing what I've felt, what I've lived, what it's like to be put down because of the color of my skin. (beat)

KENNEDY: (Pg 430-431) [You see] There is a difference between active and passive racism. Active racism is telling a nurse supervisor that an African American nurse can’t touch your baby. It’s snickering at a black joke. But passive racism? It’s noticing there’s only one person of color in your office and not asking your boss why. It’s reading your kid’s fourth-grade curriculum and seeing that the only black history covered is slavery, and not questioning why. It’s defending a woman in court whose indictment directly resulted from her race. . . and glossing over that fact, like it hardly matters.

RUTH: (to Kennedy, who continues unaware of Ruth) (Pg 237) You told me this lawsuit isn’t about race. But that’s what started it. And it doesn’t matter if you convince the jury I’m the reincarnation of Florence Nightingale—you can’t take away the fact that I am Black. The truth is, if I looked like you, this would not be happening to me.

KENNEDY: (Pg 430) I know you’re thinking: I’m not racist. I doubt there are many of you who believe that black people are so inferior they should not even be able to touch a white baby. But even if we took every white supremacist on the planet and shipped them off to Mars, there would still be racism. That’s because racism isn’t just about hate. We all have biases, even if we don’t think we do.

RUTH: (to audience) (Pg 43) I don’t have a problem with white people. I live in a white community; I have white friends; I send my son to a predominantly white school. I treat them the way I want to be treated – based on their individual merits as human beings, not on their skin tone.

KENNEDY: (Pg 431) (sighs) If you’ve asked yourself what this trial is really about, you know it’s more than just whether Ruth had anything to do with the death of one of her patients. In fact, it has very little to do with Ruth. It’s about systems that have been in place for four hundred years. Systems meant to make sure that people like Turk Bauer can make a heinous request as a patient, and have it granted. Systems meant to make sure that people like Ruth are kept in their place . . .

RUTH: (Pg 432) (stunned) After months of telling me that race doesn’t belong in a court of law, Kennedy McQuarrie took the elephant in the room and paraded it in front of the judge. She squeezed it into the jury box, so that those men and women couldn’t help but feel the pinch. What Kennedy said – it’s been the narrative of my life . . . but I could have screamed it from the rooftops, and it wouldn’t have done any good. For the jurors to hear it, really hear it, it had to be said by one of their own.
```

---

## IC-0264: Small Mercies

- Title: Small Mercies
- Author (byline): Cora Sorenson
- Work: Fast Horse Plays, Round One
- Publisher: Fast Horse Drama
- Publication date as stated: Sept 2011
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JOSEPHINE
- Teaser before the introduction: No
- Spoken words (computed): 1484
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cora Sorenson
Book: Fast Horse Plays, Round One
ISBN: 978-0615603681
Publisher: Fast Horse Drama
Date (Month/Year): Sept 2011
```

### Introduction (context only: never use it for content warnings)

```text
It got to a stage where I didn’t know what the truth was and what was a lie. (Beat) I told him to stop, but he wouldn’t. (Beat) I pushed him away, but he pushed me back. (Beat) I looked in the eyes of my children and know that they watched every bit. I changed. (Beat) I began to believe that it was my fault; like I was on this rollercoaster and I couldn’t get off. (Long beat) But, we had our good times . .

Domestic violence is one of the hardest situations a person can go through. You love your other half so much that you excuse his behavior when you shouldn’t. No one deserves to be abused, and no one should stay with an abuser, but sometimes it’s not so easy to just walk away. The time is the early 1940s . . . things were different then. Josephine Smythe explains how she was always taught to be thankful for

Small Mercies by Cora Sorenson
```

### Performance text (classify this)

```text
JOSEPHINE: The secret to happiness? To whose happiness? Yours? Mine? I can't claim to be an expert on anyone else's life but mine. When you've lived to 85, you've earned the right to call it a history, I think.

Routine. Expecting the expected. There is a comfort in that. Peace, I suppose. I like knowing what to expect. Surprises are . . . disquieting.

I was married on May Day, 1935. I had a beautiful white dress and there were so many wonderful flowers. My mother told me that I was the most glorious bride that she had ever seen. And I knew that I was marrying the handsomest man on earth. These film stars that all the young girls go all goofy over these days? Those men couldn't shake a stick compared to my Robert. He held my hand and told me that he would protect me, that he loved me. Oh, and how I loved him. My whole heart was filled up with that love and on that day, I was complete. I was everything I had ever dreamed of being. And he did, he treated me like I was his everything. We lived on the west coast then, and we would go out dancing. We loved jazz music, and he would turn me on the dance floor, and I would close my eyes and let myself fall into him during those minutes. Those trumpets and trombones and clarinets were all playing for me. And he held me, my Robert. It's very difficult to articulate a love quite like that. A love that . . .

And oh, of course I had my dreams. I thought maybe I could be a nurse or a teacher or even an air hostess, but, you see, I had committed to him, and I agreed to stand behind my word. Because my word was what I had, you see? We wanted, more than anything, to start a family. We were blessed with a beautiful baby girl. Clara passed two weeks after she was born. Her heart was not fully developed. It was . . . damaged. She was so precious. Born with a full head of beautiful, thick hair. I had long dark hair when I was younger. And Robert and I would go walking through the gardens in the city, and he knew the scientific names of all of the flowers, and he knew how much I loved the flowers. And we walk through the roses and the gardenias and the rhododendrons and it was like we were dancing again, I could almost hear the piano and the . . .

I just need a small drink of water. I was injured while carrying Clara. I fell, but. . . I went . . . Forgetting would be a small mercy, perhaps. But, then, we are not to forget the things that brought us to our place today, now are we? Any of them? I suppose I might simply say it. Let me tell you, I've tried so many times to remember what it was that I had disagreed with Robert about that evening. It was in the summer, and I was several months along with Clara. I don't remember what it was, or I can't, or that part of my brain refuses to. I told him, "No," about something, and he struck me so hard in the stomach that I fell backwards down our staircase.

I do remember the thump-thump-thump of my body as I went down the stairs, like percussion, like this was some sort of dance gone wrong. And I remember, I felt like the spirit had been struck clean out of me. That was what hurt the most of anything that I could possibly imagine. And so there was a bit of a haze for a few moments there, sort of. . . sprawled out at the bottom of the stairs, and I went very quickly to a. . . a very different place altogether, a place where Robert and I were dancing in the middle of a very big garden and he was holding me so close, the life I wanted. The life I had expected to have. But I did not get to stay in that place. I looked up and Robert's face was there, above me, but it was not the face I knew. I did not know that he could be that ugly. And I closed my eyes until he made me get up. To see if I was bleeding.

What is the secret to happiness? I could have lost Clara that night, but something much bigger than me made certain that I was able to hold my little girl. That I was able to hold her for 13 days and 7 hours. . . Hold her and sing to her, "Hush little baby, don't you cry..." There are small mercies in this life.

How does one continue to love another at their own expense? I do not know the answer. I know that there were still small moments. Spaces of reprieve, I believe you could call them. Moments in time where I still saw the Robert that I had married, the man I had committed my life to. I did not know how to betray that commitment, and I did not know what had changed in him. It is very important to me that you understand that. And how I needed to believe that it was some failing, some sort of short-coming on my part. I tried to make everything just so. But there is no perfection that is flawless enough to overcome that kind of rage. A wrinkled shirt. A cup of coffee turned cold. A spot on the counter. All insignificant in their own regards and each one enough to inspire vengeance. To bring about the ugliness. His exaggerated consequences for my misdeeds. Broken wrists, arms, toes, ribs. He kicked me until I couldn't breathe. He split my lips so badly I feared that they would never heal. I always went back to the garden, dancing, dancing . . . How does a woman forsake her dignity in such a fashion?

I brought two handsome boys into the world. Beautiful, strong, healthy boys. And I protected them. It becomes easier to. . . endure when you have young babies sleeping in the next room over. I would have given everything I had to protect them and keep them safe. It is never enough.

Robert left for the war in 1941. I had dreams of leaving with the boys and going somewhere so far away. I thought perhaps I really could become an air hostess and that, somehow I could take the boys with me on the flights, and I would use expensive face powder and lip stain to cover up the bruises, and I would roll the cart down the narrow little aisle and turn to see my boys, strapped into their booster seats, waving at their Mama. Proud of their Mama. Now these really are the rants of an old lady.

Robert wrote me letters while he was away. He was very regular about that. Very routine. And they were wonderful letters.

Dearest Josie,

I do not know that I could live a single day without you. Protect yourself until I can return home . . . Robert.

Protect myself? Protect myself? I had to protect myself from you, Robert. I had to believe that I would not be killed at the hand of the man I loved. I had grown terrified you see, of the simplest things, the most everyday, commonplace things. Lit cigarettes as instruments of rage. Anything heavy that could be thrown. To bruise. To hurt. To make bleed. The inside of me was bleeding. I loved him so much and yet I felt so useless. So small. The safest I ever was was when you were away. I wanted so badly to pretend that he had changed. That he would return home as the man I married. (Beat)

It was such a cold day for September. The boys were not home from school yet and a man wearing a uniform arrived at our door. "Ma'am, are you Mrs. Robert Smythe?" And I recall that it was so impersonal. So directly to the point, "The United States Army regrets to inform you that your husband, Sergeant Robert P. Smythe lost his life while serving."

I do not precisely know how many emotions can stand together in a single moment. I know that I lied down on the floor of our bedroom, and I wept. I wept for the years that would not be returned to me. For broken bones and parts of my body that had long since healed and the soul that never would. I wept for Clara and the boys. And most of all I wept because I was happy that my husband would not be coming home. And, because of that, in mind, we could dance forever in the garden, while the band played on and on . . .
```

---

## IC-0265: Sold

- Title: Sold
- Author (byline): Patricia McCormick
- Work: Not specified
- Publisher: Hyperion
- Publication date as stated: Sept 2006
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LAKSHMI, AMA, FATHER, BAJAI, AUNTIE, UNCLE, MUMTAZ, OLD MAN, SHAHANNA, PUSHPA, ANITA
- Teaser before the introduction: Yes
- Spoken words (computed): 1659
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patricia McCormick
ISBN: 978-0786851713
Publisher: Hyperion
Date (Month/Year): Sept 2006
```

### Introduction (context only: never use it for content warnings)

```text
Statistically Nepal is one of the poorest countries in the world. Desperate to survive, families feel forced to extreme measures to survive. Each year, nearly 12,000 Nepali girls are sold by their families into a life of sexual slavery in the brothels of India.

Meet Lakshmi. She is 13 years old and this is her story. Sold by Patricia McCormick
```

### Performance text (classify this)

```text
*LAKSHMI: (Pg 8) My stepfather's arm is a withered and useless thing. Broken as a child when there was no money for a doctor, his poor mangled limb pains him during the rainy months and gives him great shame. No one, he says, will hire a one-armed man. *Ama says we are lucky we have a man at all. She says I am to honor and praise him, respect and thank him for taking us in after my father died.

LAKSHMI: (Pg 48-49) I put the baby in a basket on my back and go about my chores. [Ama’s] steps are slow and heavy, and she stops often in her work to shake her head and sigh. At noon, I warm the remains of yesterday's soup, feed it to the baby, then tighten my waistcloth so my own hungry stomach will think it is full. Then I go in search of Ama and find her weeping. (to mother) "What is it, Ama?" Ama wipes her cheek with the hem of her shawl.

AMA: Your stepfather has said you must go to the city and earn your keep as a maid.

LAKSHMI: (to mother) “This is good news, Ama," . . . (to audience) my voice full of a boldness I did not know I had. (to mother) “There will be one less mouth to feed here, and I will send my wages home." (Pg 52-55) (to audience) The next morning my stepfather brings me to Bajai Sita's store.

FATHER: (to Bajai) Lakshmi wants to go to work in the city.

BAJAI: (to Lakshmi) Are you willing to do whatever is asked of you?

LAKSHMI: I nod. She goes behind a curtain and returns with the stranger in the yellow dress. The woman looks me over head to toe, then addresses my stepfather.

AUNTIE: How much do you want for her?

LAKSHMI: My stepfather squints. He takes in the costly fabric of the woman's dress, the baubles on her ears, the silver bangles on her wrist. "One thousand rupees," he says. There are not that many rupees in the world!

AUNTIE: (circling and inspecting Lakshmi) She has no hips. And she's plain as porridge. I'll give you five hundred.

LAKSHMI: I do not understand. I can carry a load of firewood so heavy it would put a man to shame, and my legs are sturdy enough to climb the mountain a dozen times in one day. What does it matter that I have no hips yet? My stepfather says he knows the going rate for a young girl like me.

FATHER: (to Bajai) No less than eight hundred.

LAKSHMI: My stepfather counts the money, then counts it again.

BAJAI: (to Lakshmi) Your family will get nothing, not one rupee, if you do not obey your new auntie. Do you understand?

LAKSHMI: (to audience) I don't. I don't understand at all. A great deal of money has just been paid for work I have not yet done. But I nod. (Pg 72-73) Auntie takes me into one of the rooms.

AUNTIE: (disdainfully) Take off those filthy hill clothes.

LAKSHMI: She holds out a pink dress of cloud fabric and a pair of shoes. I cannot imagine how I will walk freely in such a long, flowing gown, or how I will be able to haul the firewood and scrub the floors in such a fine and flimsy dress. TRANSITION And so Auntie takes Lakshmi to a larger village where once again she is Sold.

LAKSHMI: (Pg 74-75) Auntie is speaking to a man in a tongue I do not understand. It seems as though they are talking about me now. The man points to me and asks Auntie a question. The answer, as best I can tell, is the number 12. "How old are you?" he says in my language. I tell him I am thirteen. He wheels around and slaps Auntie across the face, and she turns from a woman of queenly bearing to a frightened child. I fall to my knees and beg the man to forgive me.

Auntie names a price as high as a mountain. The man spits. Auntie goes high. The man goes low. I do not know what they have agreed to. But I do know this: he gives her nearly enough money to buy a water buffalo. TRANSITION Alone with yet another stranger, Lakshimi still believes she is being taken to her new job as a maid in the large Indian city of Kolkata.

LAKSHMI: (Pg 90-91) Finally, we tum down an alley and arrive in front of a metal gate held fast with a heavy chain. Uncle takes a key from his vest, opens the lock, and hurries me inside. This place is dark as a cave, and it smells of liquor and incense. As my eyes adjust, I see a dozen sleeping girls, some in the comers, some on rope cots. (to Uncle) “What kind of place is this?"

UNCLE: Happiness House. Auntie Mumtaz will explain it all to you.

LAKSHMI: In the weak morning light, I see that the girls are wearing dresses of every color. They have heavy silver bangles on their wrists and ankles, and earrings of gold and jewels. Their eyes are painted with black crayon, and their lips are drawn on like red chilis. (Pg 92-94) Inside a darkened chamber, a fat woman in a purple sari lounges on a cot. She has folds of flesh like roti dough at her waist, and a face as plump as an overripe mango. She surveys me head to toe, then spits.

MUMTAZ: How much?

UNCLE: Fifteen thousand.

LAKSHMI: Uncle goes high, the woman goes low. Eventually Uncle shrugs and gives up. The woman takes a record book out from inside the folds of her dress. She writes down the number 10,000. (long beat) I don't know why I am in this strange house. It seems as though this Auntie Mumtaz is my new mistress. She is a strict one, to be sure, but I will prove myself to her. And then my mother will have a new dress, shoes for the cold season, even a new shawl made of the finest yarn. My little brother will have fruit and curds twice a day and a jacket of yak fur. (Pg 102-104) Mumtaz studies me.

MUMTAZ: Are you ready to go to work?

LAKSHMI: I nod and say yes, then nod again, although I do not understand how these city people do their chores in such fine clothes. I follow Mumtaz down a hallway lined with tiny rooms. We pass by girls sitting cross-legged on the floor. Girls drawing on tiger eyes. Girls spraying themselves with flower water. We go up some stairs, down another hallway, then into a room where an old man is lying on a bed. His skin is yellow and he has tufts of hair poking out from his ears. Mumtaz speaks kindly to him and I wonder if he is sick. Mumtaz points to me and says something to the old man. He licks his palm and smoothes down his hair. Something is not right here. I don't know what is going on, but it is not right, not right at all. Mumtaz pats the edge of the bed.

MUMTAZ: Don't be afraid. Come here, now.

LAKSHMI: I don't move. Her voice turns hard.

MUMTAZ: Get over here, you ignorant girl.

LAKSHMI: Then Mumtaz flies at me. She grabs me by the hair and drags me across the room. She flings me onto the bed next to the old man. And then he is on top of me, holding me down with the strength of ten men. He kisses me with lips that are slack and wet and taste of onions. His teeth dig into my lower lip. Underneath the weight of him, I cannot see or move or breathe. He fumbles with his pants, forces my legs apart, and I can feel him. I gasp for air and kick and squirm. He thrusts his tongue in my mouth. And I bite down with all my might.

OLD MAN: Aghh!

LAKSHMI: . . . and I am running. Running down the hall, past the other girls, losing my fancy city shoes along the way. TRANSITION

But this is only the beginning; starved, beaten and drugged, Lakshmi is eventually broken and moved from a locked room into the general population of girls. She learns from them everything she needs to know to survive.

LAKSHMI: (Pg 141-143) While Anita and Pushpa stand in front of the mirror, painting their faces, Shahanna explains everything to me.

SHAHANNA: Before, when you were in the locked room, Mumtaz sent the customers to you. Now, you must do what it takes to make them choose you. Tell the customers that you are 12 or Mumtaz will beat you senseless. Do whatever the customer asks of you. Otherwise, he will beat you senseless. Then he will do whatever he likes and leave without paying.

PUSHPA: Always wash yourself with a wet rag after the man is finished. This will keep you from getting a disease. Once a month a government woman comes to the back door with a basket of condoms. Take a handful and hide them under your mattress. If an old man is at the door, bat your eyelashes and act the part of a little girl. He will pay extra for this. Press your shawl to your nose with the back of your hand when you must bring a dirty man to your bed. He will leave nothing but his smell, the stink of sweat, and hair oil and liquor and man. But you can use your shawl to block the worst of it.

LAKSHMI: Anita turns away from the mirror, transformed from a crooked-faced country girl into a tiger-eyed city woman.

ANITA: There is another way to use a shawl.

LAKSHMI: I cannot tell from her always-frowning face if she is being kind or cruel.

ANITA: [The] new girl, the one in your old room . . . Yesterday morning Mumtaz found her hanging from the rafters. (long beat)

LAKSHMI: (Pg 192) A few days later I pass by a mirror. The face that looks back is that of a corpse. Her eyes are empty. She is old and tired. Old and angry. Old and sad. Old, old, a hundred years old. I speak to her. "My name is Lakshmi," I tell her. "I am from Nepal. I am 13 years old."
```

---

## IC-0266: Sorry

- Title: Sorry
- Author (byline): Dori Appel
- Work: Even More Monologues for Women by Women (Pgs 3-6)
- Publisher: Heinemann
- Publication date as stated: March 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: THERESA
- Teaser before the introduction: Yes
- Spoken words (computed): 1181
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dori Appel
Book: Even More Monologues for Women by Women (Pgs 3-6)
ISBN: 978-0325002477
Publisher: Heinemann
Date (Month/Year): March 2001
```

### Introduction (context only: never use it for content warnings)

```text
Therapy gives you more control over your life. You become more conscious of your self and your behavior. You become more honest with yourself. You begin to take the driver's seat in your life and take control - rather than be controlled by other people or events. Your personal power increases. You become aware that you have choices. You run the show and no longer have to feel Sorry for everything that happens.

Sorry by Dori Appel.
```

### Performance text (classify this)

```text
(Theresa Barnes, a woman in her late thirties, speaks from a ward in a mental hospital, addressing the audience as though speaking to fellow patients. Throughout the monologue, moments of forthrightness and humor vie with those of confusion, despair, and rage.)

THERESA: (Pg 3-6) Two o'clock. Free time on the funny farm, everybody, and I suggest you spend it with me. It will do you more good than watching the soaps, more good than the Tuesday afternoon sing-a-long, more good than chair caning class. Chair caning! Where did they think up that one? We're mentally ill, not blind!

Hey, you ever think about how you got crazy? Or do you just imagine that the little gears inside your brain just somehow jumped the track? I think about it a lot. That's one thing about being in this place, you get some time to think. And I'll tell you something-I believe being crazy may be the final and perfect expression of what we've been trained for all our lives.

Think of it this way-what's the thing we say the most? Come on, girlfriends, help me out. (She points.) Right! "I'm sorry." Whatever it is, whoever's upset, it's something for you to apologize for. You drank the last Pepsi, or the dog peed on the rug, or your husband lost his keys, or your kid didn't get invited to somebody's party, or it rained or it didn't, and it seems like you ought to say, "I'm sorry."

THERESA: And what's everybody say to us when we're upset? (She points.) You got it-"It's all in your head." If they hurt your feelings, you're too sensitive-it's all in your head. If they make you mad, they didn't mean anything-it's all in your head. If you get scared, there's nothing to be afraid of-it's all in your head. And the backaches and night sweats and stomach and skin problems that don't ring the right bells on the medical testing machines, they're in your head, too. (Beat)

And so now we're crazy, and everything bothers us, and it's all in our heads, and we're really sorry to boot!

(In a reproving and slightly condescending voice) "It's a sickness like any other sickness, Mrs. Barnes. There's nothing to be ashamed of." (In her own voice) That's the social worker, who has, of course, already read every humiliating detail of why you need to be here. No shame, no blame, and no reason to think that anyone stuck you in this place just to shut you up. (In the reproving and reasoning voice) "The hospital is just a little time-out."

(In her own voice) Sure, why not? I put my kids in timeout sometimes. When they're bad. And I tell them it's for their own good. You put the bad kid in the room and you say, "You have to stay there until you can behave yourself." And then you shut the door. (Beat) Stay right there, crazy lady, until you can remember how to be . . . a lady. The job description's pinned to the back of the closed door.

But somewhere there's a bad little girl who isn't afraid of being left alone in that dark room. She'd just sit there, and when her husband came-oh no, that's no good. (She laughs.) Little girls don't have husbands, do they? (Beat) Woe be to the one who does not emerge from the closed room remorseful, who will not say "Sorry" when they finally let her out. They've got the evidence: the buckets of tears, the meals not cooked, kids not cared for, husbands suffering from insufficient marital relations. (Beat) Evidence. Evidence. The groove worn in the mattress during the sleeping days, the varnish worn off the floor during the nonsleeping, pacing nights. The razor blades, the empty bottles of pills. (Beat) Sorry. I'm sorry. Love, honor, obey, and be sorry.

You want to know why they sent me here? Just because I stopped being sorry and started getting- Well, it was clear that I wasn't myself. A woman in her right mind doesn't scream like a banshee at the drop of a hat, and break every dish in the kitchen cabinets, and cut all the cords off the household appliances. My husband was annoyed, of course. But he worries about me, he wants me to get well-and the staff is very encouraging. The very first day I was here, I was sitting on the bed and watching my sad-looking feet hanging down, and that nurse with the big, round, smiley face came in with a lunch tray. She gave me an extra big smile as she set it down and told me how I was going to be back on my feet real soon. I knew what she meant. (As the nurse, with the voice of an evil witch) "You're going to be cooking and cleaning and jumping to meet everybody's whim and demand before you've even caught your breath! The moment your insurance runs out, you're gone!" (As herself, rather matter-of fact) After I threw the custard from the lunch tray in her face, I learned about a new version of time-out: The Quiet Room. Nothing in it but a mattress on the floor. While I was locked up in there, I thought about what I'd done. It wasn't nice. So, I wrote "Sorry" on the wall with my own crap.

Then on the weekend my husband Sandy came, looking some combination of miserable and guilty, and he told me how he and the kids missed me and wanted me home. And I really was sorry. I wasn't angry anymore, and I cried all the rest of the day, and everybody here started being much nicer to me. When the doctor came to see me, he told me that a lot of women these days are angry about their roles. "Well," I said, "Maybe they've been given a stale one."

He kept on talking, of course, but I didn't listen. I was thinking about the Quiet Room when they locked me in there. Only it was different. It wasn't that bare room with the mattress that I was thinking about. It was a little girl's bed room, all frilly blue and white. (She drifts into her fantasy.) A little girl is being sent to her room for being bad. She can't come out until she's sorry. They close the door, and as soon as they're gone, she hops off the bed and crouches down so she can see under it. She picks up the blue organdy ruffle that matches the curtains and pillow shams that her Mommy and Daddy got her because she's their special little girl, and she reaches under there and hauls out a big old ax! She runs her finger over the blade carefully, just to make sure it's sharp. And then, SMASH! There go all the nice storybooks, and the dollhouse with its tiny furniture, and SMASH! There goes the white painted dresser holding her neatly folded clothes, and the bed posts off the bed. And SMASH! She chops down that closed door and she bursts out free! And she tells everyone,

"I'm not sorry! Not one bit!" (Shaken, she returns to the present and regains control though she is still in the grip of strong emotion. She glances at her watch.) Free hour's just about up, isn't it? That person from the community college is supposed to come and tell us about all their adult noncredit courses. I doubt that they've got the one I want. What I want is a course on the social history of apology. I want to know the origins of the word "Sorry." That's what I want to study, and I want it for credit. Full credit.
```

---

## IC-0267: Southern Utah: Another Tragedy (From Hurricane)

- Title: Southern Utah: Another Tragedy (From Hurricane)
- Author (byline): Erin Cressida Wilson
- Work: More Monologues for Women by Women
- Publisher: Heinemann Drama
- Publication date as stated: Aug 1996
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ESTHER
- Teaser before the introduction: No
- Spoken words (computed): 1373
- Already set (do not supply): none

### Source block (context only)

```text
Author: Erin Cressida Wilson
Book: More Monologues for Women by Women
ISBN: 978-0435070229
Publisher: Heinemann Drama
Date (Month/Year): Aug 1996
MN State Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
In the 1950’s conflict in Korea caused the United States to consider testing nuclear weapons on a continental testing site in order to maintain U.S. nuclear weapons superiority. On 27 January 1951, a one-kiloton bomb dropped from an airplane and detonated over Frenchman Flat marked the beginning of atmospheric nuclear testing in Nevada.

Relatively few residents were aware of or concerned about nuclear testing when the first mushroom-shaped cloud rose into the western skies and drifted to the northeast, but the cloud figuratively remains over southern Utah and Nevada to this day. Residents live with every day what the cloud left behind that the eye could not see. There are no southwestern Utah neighborhoods or communities that have not been touched by the tragedy of cancer or birth defects or lingering bitterness over human and financial losses. Southern Utah: Another Tragedy from the play Hurricane by Erin Cressida Wilson
```

### Performance text (classify this)

```text
ESTHER: I saw my first mushroom on a field trip. Miss Hansen took us to the edge of town and had us put our ears to the glass windows as we watched the mushroom cloud in the distance. I thought right there and then, I thought, "I'm marrying a man who works on those clouds, gonna hitch myself up with a fella who works those sky mushrooms." And that's exactly what I went and did. Yup. So now I'm worth one hundred thousand dollars! If I get the right kind of cancer that is. But then I'll never see that money. My family might, but I got no kin to speak of.

Now I don't claim to know much because I don't, but you know, they asked a bunch of kids, down there at the Hurricane Junior High School, they asked these kids, you know, if they believed that there was such thing as the Holocaust. Well, you know their answer was "No." "No, no, no" was the firm answer of theirs. They thought it was a myth like the Easter Rabbit or Santy Claus. Well, they used their skin for lamps, made shades with human flesh, knocked out their teeth for gold, you know, and they would take their hair and make wigs. But how you gonna convince a kid from Hurricane, Utah that that really happened? We're good at forgetting. Painting over the sore spots. Hey, but I'm stupid.

Well, now, this is something, you know, Graham, my husband, he excavated the ground after the nuclear tests used to go off, you know, cleared the area, and brought cans of water to the soldiers. Water's the best thing to wash off with in cases of radiation exposure. Just plain water. That's right. And sometimes, there'd be these days when they'd stop him from entering. They'd stop him in his car. They were waiting for the wind to shift, that's right, they were waiting for the wind to change. So it could blow east. Towards Southern Utah, Hurricane, St. George, and the likes. But not towards California and Los Angeles. That's a fact. Because California was a real place, a real place back then where things were happening. But in any case, the point is that this land here, in Utah, that my grandfather homesteaded and had took away from him in the Great Depression, this land was designated by the United States government as, and I know this now, as perfect and useless, yes. Disposable. The land. The people. A place you might throw out your used razor blades.

It's not my husband I mourn so much, but don't get me wrong, cause I do, it's my daughter, born with her heart outside her body. Now you know I'm stupid ‘cause I don't know why, but I always return to this land, return to Hurricane, where the rocks have faces and the wind is hot, where the dry heat and the sulfur springs make you high. Around here the streams bubble hot, there are prehistoric fossils, the bottom of the ocean was here once, you can find shells up there, and there's a good road up there you can go up to the mesa with a six pack and watch the meteors. But what I love the most is that underneath this beauty lurks the memory and reality that the grass will turn brown under your feet and that if you hold your fingers up you can see your bones. And you can taste it, sure, taste it on your tongue, like metal . . . like sex, the sky is pink. And now the moonlight is even too bright for me and these eyes. You think I got a hair left on my head? You think my teeth ain't real? They discovered they were hollow, that's right, no nerves, no blood, as they pulled them out, one by one, and gave me a new set to drop into a glass of water each night.

Oh, it's silly, but I remember learning, in the encyclopedia it was, I remember learning that crocodiles, they make hundreds of teeth their whole life, hundreds of teeth-wish I did-they just fall out and grow back, fall out and grow back, and they uhm, they, the men, they would take the teeth, this was back at the turn of the century or some such time, they used to take the teeth and cause they were hollow, they filled them with gunpowder, this is a fact, and used them as ammunition, as bullets, imagine. Crocodile teeth as ammunition. I feel like they stuck those crocodile teeth in my head and turned my skin the color of the rainbow, pulled my scalp up with the comb and cut my voice box, cut it right out of me.

Can you imagine burning rabbits running across a field, and sheep, homes split down the middle and cattle on fire, poison milk, children born with no faces, just large holes, the heat of seven suns, 125 atomic blasts detonated in Nevada between '51 and '62, each one about the same size as that Chernobyl. And my voice box cut right out of me. I never was a very good talker anyway, but I always knew how to think, quietly, to myself, stupid, but I thought, as I straightened the cuffs on Graham's pants leg before throwing them into the washer, the poison dust from his cuffs on my fingers, the taste of the pink cloud, like sex, and I am quiet, and I think you can hear me Claire, hear my loud whisper, your heart I touched in my hand when you were born, outside your body and how you did not live to see twenty-four hours ... your face, a hole your heart, in the stones, your touch, in the stream, your torso in the stars, your hair in the wind on my lips, your face .....

I think she'd be thirty years old now, she would be. He'd be sixty. Ha!

One dusk I saw a flock of mourning doves flying. A flock of mourning doves. And they had just flown by the light of a mushroom, that spitfire light of the mushroom, and they just dove, these mourning doves, they just dove straight into the light and died, kamikazied, a whole flock of mourning doves were blinded by this light that they relentlessly stared at. Maybe they was smart. You see, they thought the light was water, that it was the water that would hold them. But you could say I was one of those mourning doves. Or just stupid. Just staring into that light over and over and over and over again. Proud to be a part of it I guess. Or just proud to be able to accept anything that comes my way. I'm worth one hundred thousand dollars with the right kind of cancer. But don't listen to me. If I knew then what I know now, well ... when you're dumb you're dumb. Right?

Claire, I'm happy. I don't watch the news, I don't take no bull, I'm a survivor and you know, Honey, do you know, you never got to see that mushroom, but it was like heaven, it was like heaven above. In that trailer, next to that butte, the glass and the heat of the day, the shudder of the window and the look of heaven, man-made heaven in the sky, in the south of Utah, in the mid-I950S, the baldness of neighbors, things you could not conceive, squinting our eyes up to Salt Lake City as we wondered the half life of atoms. And I think in this tiny town, I think about how we marvel at the news of war and in a way feel filled by it cause it's over there, over there, and Hitler, he's not just over there, he's way back then. Why it is that they chose this land I will never know and why it is that we don't count I'll never know, but we bombed our own country. But when you're dumb you're dumb, right. Hey, I'm no activist. I'm just sitting in this bar, right, drinking this beer, right, quiet as a mouse. Shhh.
```

---

## IC-0268: Speak

- Title: Speak
- Author (byline): Laurie Halse Anderson
- Work: Not specified
- Publisher: Puffin
- Publication date as stated: April 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MELINDA
- Teaser before the introduction: Yes
- Spoken words (computed): 1191
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laurie Halse Anderson
ISBN: 978-0374371524
Publisher: Puffin
Date (Month/Year): April 2001
```

### Introduction (context only: never use it for content warnings)

```text
At the end of the summer before she enters high school, Melinda attends a party at which two bad things happen to her. She gets drunk, and she is raped. Shocked and scared, she calls the police, who break up the party and sends everyone home. She tells no one of her rape, and the other students, even her best friends, turn against her for ruining their good time. By the time school starts, she is completely alone, and utterly desolate. She withdraws more and more into herself, rarely talking, cutting classes, ignoring assignments, and becoming more estranged daily from the world around her. Few people penetrate her shell; one of them is Mr. Freeman, her art teacher, who works with her to help her express what she has so deeply repressed. When the unthinkable happens--the same upperclassman who raped her at the party attacks her again- -something within the new Melinda says no, and in repelling her attacker, she becomes whole again.

Speak by Laurie Halse Anderson
```

### Performance text (classify this)

```text
MELINDA: I am Outcast. I don’t do parties. No thanks. I trot out excuses: homework, strict parents, tuba practice, late-night dentist appointment, have to feed the warthogs. I don’t have a good track record with parties. I am not going to think about it. It was ugly, but it’s over, and I’m not going to think about it.

MELINDA: There is no point looking for my ex-friends. Our clan, the Plain Janes, has splintered and the pieces are being absorbed by rival factions.

Her eyes meet mine for a second. It’s Rachel. “I hate you,” she mouths silently. She turns her back to me and laughs with her friends. I bite my lip. My lip bleeds a little. It tastes like metal. I need to sit down.

The Homecoming pep rally, and Heather drags me into the freshman section of the bleachers. The girl behind me taps me on the shoulder with her long black nails. She had heard Heather introduce me. “Sordino?” She asks. “You’re Melinda Sordino?”

I turn around. She blows a black bubble and sucks it back into her mouth. I nod. Heather waves to a sophomore she knows across the gym. The girl pokes me harder. “Aren’t you the one who called the cops at Kyle Rodger’s party at the end of the summer?”

A block of ice freezes our section of the bleachers. Heads snap in my direction with the sound of a hundred paparazzi cameras. Another girl chimes in. “My brother got arrested at that party. He got fired because of the arrest. I can’t believe you did that. Asshole.”

I have worked so hard to forget every second of that stupid party, and here I am in the middle of a hostile crowd that hates me for what I had to do. I can’t tell what really happened. I can’t even look at that part myself.

IT is my nightmare and I can’t wake up. I’m hanging a poster outside the metal-shop room when IT creeps up. Little flecks of metal slice through my veins. IT whispers to me.

I can smell him over the noise of the metal shop and I drop my poster and the masking tape and I want to throw up and I can smell him and I run and he remembers and he knows. He whispers in my ear.

“Freshmeat.” That’s what IT whispers.

IT found me again. I thought I could ignore IT. There are four hundred other freshmen in here, two hundred female. Plus all the other grades. But he whispers to me. Andy Evans. He’s a creep. He’s a bastard. Stay away!!!!! He should be locked up. He thinks he’s all that. Call the cops

Rachel got us to the end-of-summer party, a cheerleader party, with beer and seniors and music. She blackmailed her brother, Jimmy to drive us. We were all sleeping over at Rachel’s house. Her mother thought Jimmy was taking us roller-skating.

Most people hung at the edge of the lights. They looked like models. I felt like such a little kid. Rachel found a way to fit in. I tasted a beer. It was worse than cough medicine. I gulped it down. Another beer and one more, then I worried I would throw up. I walked out of the crowd, toward the woods.

A step behind me. A senior. And then he was talking to me, flirting with me. This gorgeous cover-model guy. His hair was way better than mine, his every inch a tanned muscle, and he had straight white teeth.

Flirting with me! Where was Rachel - - she had to see this! He took my hand and pulled me close to him. I breathed in cologne and beer and something I couldn’t identify. I fit in against his body perfectly, my head level with his shoulder.

He wrapped one arm around my back. His other hand slid down to my butt. I thought that was a little rude, but my tongue was thick with beer and I couldn’t figure out how to tell him to slow down. This is what high school was supposed to feel like. Where was Rachel? She had to see this!

He tilted my face up to his. He kissed me, man kiss, hard sweet and deep. Nearly knocked me off my feet, that kiss. And I thought for a minute there that I had a boyfriend, I would start high school with a boyfriend, older and stronger and ready to watch out for me. He kissed me again. His teeth ground hard against my lips. It was hard to breathe.

“Do you want to?” He asked

What did he say? I didn’t answer. I didn’t know. I didn’t speak.

We were on the ground. When did that happen? “No”. No I did not like this. I was on the ground and he was on top of me. My lips mumble something about leaving, about a friend who needs me. I can hear myself - - I’m mumbling like a deranged drunk. He is so heavy. There is a boulder on me.

I open my mouth to breathe, to scream, and his hand covers it. In my head, my voice is as clear as a bell: “NO I DON”T WANT TO!” But I can’t spit it out.

I’m trying to remember how we got on the ground and where the moon went and wham! Shirt up, shorts down, and the ground smells wet and dark and NO! - I’m not really here, I’m definitely back at Rachel’s, crimping my hair and gluing on fake nails, and he smells like beer and mean and he hurts me hurts me hurts me and gets up....and zips his jeans....and smiles.

The next thing I saw was the telephone. I stood in the middle of a drunken crowd and I called 911 because I needed help. All those visits from Officer Friendly in second grade paid off. A lady answered the phone, “Police, state your emergency,” and I saw my face in the window over the kitchen sink and no words came out of my mouth. Who was that girl? I had never seen her before. Tears oozed down my face, over my bruised lips, pooling on the handset. “It’s OK,” said the nice lady on the phone. “We have your location. Officers are on the way. Are you hurt? Are you being threatened?” Someone grabbed the phone from my hands and listened. A scream - - the cops were coming! Blue and cherry lights flashing in the kitchen-sink window. Rachel’s face - - so angry - - in mine. Someone slapped me. I crawled out of the room through a forest of legs. Outside, the moon smiled goodbye and slipped away.

I walked home to an empty house. Without a word.

IT happened. There is no avoiding it, no forgetting. No running away, or flying, or burying, or hiding. Andy Evans raped me in August when I was drunk and too young to know what was happening. It wasn’t my fault. He hurt me. It wasn’t my fault. And I’m not going to let it kill me. I can grow.
```

---

## IC-0269: Spoonface Steinberg

- Title: Spoonface Steinberg
- Author (byline): Lee Hall
- Work: Not specified
- Publisher: Methuen Publishing, Ltd
- Publication date as stated: Nov 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SPOONFACE
- Teaser before the introduction: Yes
- Spoken words (computed): 1912
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lee Hall
ISBN: 978-0413748706
Publisher: Methuen Publishing, Ltd
Date (Month/Year): Nov 2000
```

### Introduction (context only: never use it for content warnings)

```text
“Out of the mouths of babes” -- In this selection, a special child confronts her impending death with stoical grace and with a belief in the glory of God. She speaks of loss, separation, sparks and death with a sense of innocent, baffled wonderment. May it help you find your own “spark.”

Spoonface Steinberg by Lee Hall
```

### Performance text (classify this)

```text
SPOONFACE: (Pg 3) I was never right ever since I was born - this means that I do very bad writing and that I can't speak proper and that I am backwards and that I am a special child - but why is a mystery for what they have not got an answer - I was in the hospital and when Mam looked at my face she noticed that it was round - and everyone came and looked at my face - and they laughed and said I was Spoonface because my face it was round as a spoon and when you look into a spoon you see this face just like mine- and that is how I came to be Spoonface Steinberg…

SPOONFACE: (Pg 5) I think I was always backwards ever since I was born - but nobody knows for sure - all the experts with all their computers and all the doctors who poke in your ear and look into your brain and all the people who do the quizzes and all questioners and such like - they all said no one can know can ever know for certain. (beat) I cannot go to a proper school as I am not allowed on account of my brain - but I am quite a special little girl, though.

(Pg 6) I believe that I was supposed to be backward - I believe it was all part of what is supposed to be - and when I was born God came and touched me on my head - and made me me.

One day I started to do the numbers. Dad came back from the university and he was with a calculator for doing the marks. He was sat doing the marks when he said two numbers and I went 42- because it was the answer of the two numbers - and then he goes - goodness me - and then he said two more numbers and I said 147- which was another answer- and then he (Pg 7) did more and more - and some of the answers he had to do on the calculator - and then he started shouting of Mam - and Mam came running as if there was something bad - but it was only me doing the numbers and I did more and more and Mam kissed me and was crying and Dad was laughing- and Mam said he had to stop- and I said what was it that had made her cry?- and she said that it was because of the numbers and never in the world did they know I could do the numbers - but I could do them now-and I was a genius - and it was of my brain.

And then I had to do them in front of a doctor - and then the doctor said - if Spoonface can do numbers then she can do dates - and then I did some - this is how I do it- what is the day of July the 4th 2010? - Saturday - amazing, absolutely amazing- and that is how I do the dates and they have to look it up in a book as soon as I've said the answer and there it is - and they say how do I know so many numbers? and I say I don't know- and how do I know so many dates? - and I also say I don't know - but it's just obvious like colours and that is why. (Pg 8) So this is all because I am autistic. (long beat)

(Pg 9-10) When I first started feeling funny that is when I still had hair - there was hardly nothing wrong except I was tired a bit - but then Mam was very worried that I was thinner and thinner and one day I might fade away to a speck - and that I was looking peaky - but because I'm backwards then I wasn't very good at saying what is wrong- so she took me straight to the doctor in case I disappeared- and the doctor looked at me like this (makes a serious face) ... and he said - 'Oh deary me, Spoonface will have to go straight to the hospital' - which is where I went. They were all very nice to me and the doctors held on to my hand and they all smiled which means something is wrong – (Pg 11) The doctor said that I was going to die. only they said there was hope - that there was always hope - and anyway, it would take a long time for me to die so we went home for some tea - and Mam said that even if I (Pg 12) was supposed to die there would still be hope 'cos there was millions of people that were saved by God everyday - so it was better not be too worried about it- so I said I wasn't worried and we had fish fingers.

(Pg 17-19) Doctor Bernstein said that I should be very brave because when his Mam was little she was very brave as well even though she was in a concentration camp. Concentration camps were these places where they took Jewish people to burn - this is what the doctor said - he said that there were loads of people and they all had to sleep on one bunk and that- and the Nazis shot them and then they starved them and it was horrible for his poor Mam because she was just little - in the whole history of the world there has never been anything as awful as the concentration camps, but what happened to the poor people there was to show that they never gave up hope - and that never mind the worse thing that could happen to people they could not stop them from being human beings - some of the little children were skinnier than I am now with the cancer, and all that was wrong with them was they didn't eat just this soup what didn't have any vegetables in it - and they'd just be standing there and their Mammies and Daddies would be bashed - like there was one little girl who was with her Mam and the soldier came and hit her Mam on the head and shot her and then she died and the poor little girl just had to stand there - that little girl was the Mam of the doctor- and there were millions and millions of people like this - so in comparison to me it is much worse- and I felt sorry for the doctor when he told me these things as he had a little cry in the corner of his eye- and he never said any of this to scare me he said all of this to help me because the whole lesson of the stories was that little children were braver than everybody else this was the lesson - that no matter how bad it is for us while we are dying it is still a wonderful thing that we are alive –

This is what the doctor said- and he said when the soldiers came and took the poor little children to the ovens and the poor children and everything thought they were going for a wash but everybody knew really that they were going to get gassed - because they had seen the smoke of burning bodies - then the children were waiting outside and all the little children wrote things on the walls - on the walls of the gas chamber where they were about to be cooked. And some little children wrote poems- and some little children drew pictures- and even today you can see the pictures of butterflies on the outside - little but-terflies that were flying up to God - beautiful butterflies with tender wings that would brush their faces and kiss them better before they flew careful little butterflies in all the death and the mud and everything- and that day when he told me this I cried for the butterflies and the little children - and all their sad faces drifting up to heaven.

(Pg 22) I started getting even worse than I was- really woozy and everything - this time they said they would give me this special thing in my arm and that would make me sick and have diarrhea and all my hair would fall out – (Pg 23) and every day I was sicker and sicker and I goes to God - Please God, why are you making me so sickly? - and I never found out because he never said - then I was quite depressed - and my eyebrows fell out. (Pg 24) The good news was that my hair would grow- but the bad news was I was still full of cancer and there was nothing to be done - all the chemicals and everything was useless.

(Pg 25) And when we went home the doctor gave me this book to me- but I can't read so I had to get Mam to read it to me- and then I found all this stuff out - like you had to pray to God - and that this would help get on his good side and even if you did die then he'd look out for you afterwards - (Pg 26) [See] when the world was made, God made it out of magic sparks - everything that there is, was all made of magic sparks and the whole point of being alive - the whole point of living is to find the spark- (Pg 28-29) if only you could see the spark then there was a meaning - because what was the meaning of anything? - if you were going to die, what was the meaning? (thoughtfully) The meaning was if you found the spark - then it would be like electricity - and you would glow like a light and you would shine like the sparks and that was the meaning it wasn't like an answer or a number or any such - it was glowing- it was finding the sparks inside you and setting them free.

And the meaning wasn't that I was going to die but that I was still alive- and I could make everybody shine and I thought, if I wasn't scared of when I wasn't born why would I be scared of when I wasn't existed at the other end- you can't feel the end or touch the end- 'cos it was just nothing- the end of things is not the problem 'cos there was really no ends to find - that was the meaning there are no real ends- only middles, and even if I was at the end I was still in the middle - 'cos it wouldn't know it was the end then - because it would be ended - so everything is in the middle - even if it was at the middle of an end - it didn't matter because I'm in it. In the middle of the middle was sparks - the sparks what would save me- the sparks what I could make shine - the sparks that knew there was no more endings - the sparks what would be as a huge light in the world and the sparks would fly up and take me to heaven.

(Pg 33-34) Sometimes it is scary - but to think that I'll not be is impossible because I'm here- and when I'm not here there'll still be radios and beaches and sunshine and walks in the rain and films and music and my Mam and Dad and flowers. - and there isn't even a hole somewhere where I used to be - and apart from people what remember me and what I was like there is nothing missing from when I was here - there is no space in the universe where people have dropped out- it is all filled in as full as ever.

(Pg 29) [See] the sparks? The sparks . . . fly up and take me to heaven.
```

---

## IC-0270: Staph Infection from Commencement

- Title: Staph Infection from Commencement
- Author (byline): Clay McLeod Chapman
- Work: Commencement
- Publisher: Original Works Publishing
- Publication date as stated: 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SARAH, MITCHELL
- Teaser before the introduction: Yes
- Spoken words (computed): 1984
- Already set (do not supply): none

### Source block (context only)

```text
Author: Clay McLeod Chapman
Book: Commencement
ISBN: 978-1934962657
Publisher: Original Works Publishing
Date (Month/Year): 2010
```

### Introduction (context only: never use it for content warnings)

```text
The inspiration, if you want to call it that, of this selection was not the Columbine High School killings but the Virginia Tech massacre, one gunman, 32 dead, April 16, 2007, Blacksburg, Virginia. In that case, there was a lot of anger and resentment toward the mother of the shooter. How could she have not known? How could she not have seen this coming? How could she not have stopped it? In actual life we never hear about the parents of the killer, but in Staph Infection, from the play Commencement, by Clay McLeod Chapman we do.
```

### Performance text (classify this)

```text
Sarah Havermeyer, forty-one

For the rest of my life, I will be haunted by the horror and anguish my son caused. I cannot look at a child in a grocery store or on the street without thinking about how my son's schoolmates spent the last moments of their lives. My son changed everything I believed about myself, about God, about family, and about love. I think I believed that if I loved someone as deeply as I loved him, I would know if he were in trouble. My maternal instincts would keep him safe. But I didn't know. And my instincts weren't enough. And the fact that I never saw tragedy coming is still almost inconceivable to me.

SARAH: They gave me my own waiting room. Hid me in the pediatric wing, far away from the other families. It’s much quieter at this end of the hospital. Less hectic here. Less parents, less press. Spent the last hour simply listening to the hum of fluorescents over my head.

Went over to the window on a whim once, lured in by the camera flashes. The parking lot’s all gone now. It’s suddenly engulfed in a forest of transmission antennas, budding up from the roofs of these news vans. The network call letters look like initials of young couples carved into the bark of each tree. KBCW-TV plus WGBO-4. WDBJ-7 hearts WSLS-10 4-eva . . . .

When Mitchell was much younger, he and a handful of kids from the neighborhood all went out into the woods behind our houses to play a game of hide-and-seek. When it was Mitchell’s turn to be it, he leaned his head against his own tree just as everyone else had before him. Closed his eyes and counted to a hundred. By the time he turned back around, he found himself facing the woods all alone. Ready or not, here I come – echoing through the trees. But what Mitchell didn’t realize – and why would he, really – was that everybody else had already run home by then. Didn’t stop him from playing, though. Peeking behind each tree. Searching for his friends.

An hour went by before I was on the phone with the neighbors, asking if they knew where Mitchell was. But none of their kids would say, shrugging their shoulders. When there weren’t any parents left to call, I took to the woods myself. Flashlight in hand. Finally found him leaning against a tree, huddled into himself. Shivering. Poor thing caught pneumonia that night. Had to take him to the hospital, waiting in this same room.

SARAH: Want to tell me what happened?

MITCHELL: No.

SARAH: We can keep it between you and me, if you’d like. Promise I won’t tell.

MITCHELL: I don’t want to talk about it.

SARAH: There are never any magazines here. Nothing but coloring books flung across the floor. Crayons scattered all around, like shell casings discharged from a rifle. Every color of the rainbow falling to the floor, round after round after round . . .

Not that I feel like reading right now. Simply had that reflex to flip through something. Get my mind off things. Picked up a coloring book without even realizing what it was at first, skimming the pictures just to pass the time. Glancing at all the empty animals, empty cartoon characters. Page after page. Their blank bodies filled in with scribbles, crayon spread everywhere. No consideration for coloring in the lines, whatsoever. You’d think they’d all been shot, every animal hemorrhaging Crayola across the page. Their splatter pattern in Razzle Dazzle Rose or Tickle Me Pink.

The amount of times I’ve sat here over the years, waiting amongst all the other mothers – I’ve lost county by now. They blend together after a while. All the check-ups. The mumps. Flu shots. Chicken pox. Not to mention ear infections. A tonsillectomy. A sprained wrist. The list just goes on and on . . . It’s a wonder my son even reached high school. How any of our children made it this far.

Not that the news is saying anything. Not until the police notify the next of kin. The reporters have been recycling the same information for hours now, the live coverage sounding stale already.

No names yet. Just numbers.

Last time I had to wait this long, it was because Mitchell had swallowed something he shouldn’t have. Marbles. Started complaining about his tummy aching at the dinner table, refusing to finish his macaroni – so the very next day, I brought him in for an X-ray. And sure enough, there they were – a constellation of bright white contrasting against that ghastly black of his stomach. The negative image of a half dozen glass pellets settled into his belly. A grape cluster tethered together in pale veins.

Benjamin Pendleton had put him up to it. Said he’d be his best friend if he swallowed the whole set, all ten marbles. And to think that Mitchell had almost made it, more than halfway there – determined to earn Benjamin Pendleton’s approval, to win this position as his pal, bestest friends, only giving up once his throat constricted itself, his own esophagus refusing to swallow anymore, no matter how hard he tried, no matter how hard he forced himself to eat one more, just one more, begging with his own throat to let him injest just one last marble before stumbling back home, sick to his stomach. To prove his worth. As a friend to Benjamin.

SARAH: Want to tell me who put you up to this?

MITCHELL: No.

SARAH: Mitchell – you’re only hurting yourself by not saying anything.

MITCHELL: I don’t want to talk about it.

SARAH: The police have been ushering all the parents in through the rear entrance of the hospital, away from the camera crews. The second I saw Wendy Pendleton in the hallway, barely able to even stand on her own two feet – I knew why she was here. Recognized her right away, even though we hadn’t spoken to each other in ages. Not since our sons were in the third grade together.

Her eyes had glazed over. Nothing but a pair of marbles settled into each socket, flickering under the fluorescents. Felt like I was staring at a teddy bear. Not some mother who’d just identified her son.

They’ve placed a police officer right outside my door. For my protection, they say. They’re worried some wandering father might find me here, hiding amongst the stuffed animals. The jig saw puzzles. The coloring books with the mottled corners, their pages sticking together from all the constant gnawing. Seems as if children choose to chew through these books rather than read them. The edges are still wet, even after office hours have come and gone for the day. The pulp rubs right off between my fingers. I’m thinking of the poor puzzle with its missing pieces, all of them dissolving inside some sick kid’s stomach. Nurses have to sanitize these toys at the end of every day, spraying them down with disinfectant. They have to kill off the bacteria before the following morning – before it starts up all over again. Once child will pass along their germs to whoever puts the same stuffed animal’s filthy limb into their mouth next. They’ll end up catching something completely different than whatever it was they walked in here with.

Seems fitting to be sitting here then. Almost like old times. Wouldn’t be so surprised if a nurse were to walk in any minute now, calling out Mitchell’s name – The doctor will see you now.

But none of the nurses will even come near me now. Won’t look me in the eye. Passing them all in the hallway, they’d simply bow their heads. Focus on the linoleum rather than face me. As if they were afraid? Of me?

The press is about to take my boy away from me. This is my last chance to have him all to myself, the way I want to remember him --- before I have to give him up. Let him go.

I’m imagining some reporter sifting through the yearbook, flipping from page to page just to find his photograph. Before long, Mitchell’s face will be broadcast all over the news – which is unfortunate, since he never took his class pictures seriously. He’d never tell me what day they were being taken, just so I couldn’t force him to dress up. Look nice for his picture. By the time I’d find out, it was always too late. They would’ve already snapped off the shot. If I ever wanted to order any photos for the rest of the family, I’d have to buy these wallet-sized prints of him in one of his ratty t-shirts. His hair all tussled. Refusing to smile for the camera.

Can’t even bring myself to look at his yearbook now. Seeing him there, surrounded by the rest. Their faces clumped together, grinning all round him. Nothing but an obituary now – the whole yearbook. This grim assembly of smiles.

The world will weep for the children of Midlothian High – but no one will weep for mine. I’ll have to cry for my child alone. You won’t find his name amongst the others. HE’s been omitted from the list of victims. Not that he was ever invited into their club anyways. Mitchell was never asked to play with the rest. They’ll say it was my son who took their children away – but what none of these parents are willing to admit is that their sons and daughters took my child away from me long before today. Mitchell had the bruises to prove it. Half of our trips to the hospital were for fractures that magically happened on their own. Sprained wrists that mysteriously appeared out of nowhere, no explanation whatsoever. Black eyes that looked like black holes, swallowing up my son, the distance deepening within his gaze.

Every time, every time I’ve had to sit here in this room, I’ve lost a little bit more of my son. It was only a matter of time before there was nothing left of him to take back home.

SARAH: Can we talk?

MITCHELL: . . . Why?

SARAH: Want to tell me what’s been on your mind lately?

MITCHELL: No.

SARAH: Anything happening at school?

MITCHELL: No.

SARAH: What about –

MITCHELL: Mom.

SARAH: Can’t we just chat? Just for a minute?

MITCHELL: There’s nothing to talk about.

SARAH: There’s plenty.

MITCHELL: Just let it go, mom.

SARAH: Please, honey . . .

MITCHELL: I said no. Just drop it, alright?

SARAH: All I want is to sit with the rest of the parents. I want to wait amongst the other mothers. To mourn with them. I’ve lost my child, too. Why can’t I sit with them?

We deserve to wait together.

Found a stray puzzle piece at my feet, softened with some child’s saliva. There’s no telling what the picture’s of. Has a fleshy complexion. Even feels like flesh, the cardboard all soaked in spit. Its interlocking tabs are so flimsy, they’ll flap back and forth whenever I rub my fingers over them.

Came across another piece tucked just behind the leg of my chair. Same color, same wet texture. The two pieces fit together perfectly.

Suddenly the picture’s coming into view. Here’s a piece of his cheek. A tooth, A shard of his skull, a clump of his hair matted down in blood. Fragments of his face, the skin still adhered to the bone.

I’m picking up what’s left of him off the floor. The hundreds of tessellating flecks of flesh and bone, blown off at close range. Passing the time working on this jigsaw puzzle of my son’s face, just to get one last look at him. High muzzle velocity. When Mitchell was done, he slipped the gun over his tongue. The blast reached through the roof of his mouth. Ruptured all the soft tissue before bursting through the back of his skull, sending puzzle pieces all over the classroom wall.

Kids will put anything into their mouths.
```

---

## IC-0271: Steel Magnolias

- Title: Steel Magnolias
- Author (byline): Robert Harling
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: June 1995
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: M’LYNN, SHELBY, ANNELLE
- Teaser before the introduction: No
- Spoken words (computed): 1821
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Harling
ISBN: 978-0822210788
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): June 1995
```

### Introduction (context only: never use it for content warnings)

```text
M'Lynn is excited to welcome home for the holidays her newly married daughter, Shelby. Shelby, who is diabetic, has come to tell her family that she's expecting a baby and knows her mom is going to be upset because of the danger to her health. Steel Magnolias by Robert Harling
```

### Performance text (classify this)

```text
M’LYNN: How are you, honey?

SHELBY: I'm so good, Mama. Just great.

M’LYNN: You're looking well. Is Jackson at the house?

SHELBY: No. You know how twitchy he gets. I sent him to look for stocking stuffers.

M’LYNN: Good thinking.

SHELBY: Uh. Jackson and I have something to tell you. We wanted to tell you when you and Daddy were together, but you're never together, so it's every man for himself. I'm pregnant.

M’LYNN: Shelby?!

SHELBY: I'm going to have a baby.

M’LYNN: I realize that.

SHELBY: Well…is that it? Is that all you're going to say?

M’LYNN: I...what do you expect me to say?

SHELBY: Something along the lines of congratulations.

M’LYNN: Congratulations.

SHELBY: Would it be too much to ask for a little excitement? Not too much, I wouldn't want you to break a sweat or anything.

M’LYNN: I'm in a state of shock! I didn't think ...

SHELBY: In June. Oh, Mama. You have to help me plan. We're going to get a new house. Jackson and I are going house hunting next week. Jackson loves to hunt for anything.

M’LYNN: What does Jackson say about this?

SHELBY: Oh. He's very excited. He says he doesn't care whether it's a boy or girl...but I know he really wants a son so bad he can taste it. He's so cute about the whole thing. It's all he can talk about ... Jackson Latcherie Junior.

M’LYNN: But does he ever listen? I mean when doctors and specialists give you advice. I know you never listen, but does he? I guess since he doesn't have to carry the baby, it doesn't really concern him.

SHELBY: Mama. Don't be mad. I couldn't bear it if you were. It's Christmas.

M’LYNN: I'm not mad, Shelby. This is just...hard. I thought that...I don't know.

SHELBY: Mama. I want a child.

M’LYNN: But what about the adoption proceedings? You have filed so many applications.

SHELBY: Mama. It didn't take us long to see the handwriting on the wall. No judge is going to give a baby to someone with my medical track record. Jackson even put out some feelers about buying one.

M’LYNN: People do it all the time.

SHELBY: Listen to me. I want a child of my own. I think it would help things a lot.

M’LYNN: I see.

SHELBY: Mama. I know. I know. Don't think I haven't thought this through. You can't live a life if all you do is worry. And you worry too much. In some ways it's a comfort to me. I never worry because I know you're worrying enough for the both of us. Jackson and I have given this a lot of thought.

M’LYNN: Has he really? There's a first time for everything.

SHELBY: Don't start on Jackson.

M’LYNN: Shelby. Your poor body has been through so much. Why do you deliberately want to ...

SHELBY: Mama. Diabetics have healthy babies all the time.

M’LYNN: You are special. There are limits to what you can do.

SHELBY: Mama. Listen. I have it all planned. I'm going to be very careful. And this time next year, I'm going to be bringing your big healthy grandbaby to the Christmas festival. No one is going to be hurt or disappointed, or even inconvenienced.

M’LYNN: Least of all Jackson, I'm sure.

SHELBY: You are jealous because you no longer have any say-so in what I do. And that drives you up the wall. You're ready to spit nails because you can't call the shots.

M’LYNN: I did not raise my daughter to talk to me this way.

SHELBY: Yes you did. Whenever any of us asked you what you wanted us to be when we grew up, what did you say?

M’LYNN: Shelby, I am not in the mood for games.

SHELBY: What did you say? Just tell me what you said. Answer me.

M’LYNN: I said all I wanted was for you to be happy.

SHELBY: O.K. The thing that would make me happy is to have a baby. If I could adopt one I would, but I can't. I'm going to have a baby. I wish you would be happy, too.

M’LYNN: I wish I...I don' t know what I wish.

SHELBY: Mama. I don't know why you have to make every thing so difficult. I look at having this baby as he opportunity of a lifetime. Sure, there may be some risk involved. That's true for anybody. But you get through it and life goes on. And when it's all said and done there'll be a little piece of immortality with Jackson's looks and my sense of style...I hope. Mama, please. I need your support. I would rather have thirty minutes of wonderful than a lifetime of nothing special. (Pause) Please don’t tell anybody yet. I wanna tell daddy first.

TRANSITION

Shelby has her baby – a beautiful little boy and only 3 months premature, but with the birth came some additional complications

SHELBY: The doctor’s just been trying to strengthen my veins (shows bruises on her arms) They’re in terrible shape. It’s my dialysis. It’s not any big thing. No big thing. Don’t look at me like that. Having Jack Junior put too much strain on my kidneys and not they’re kaput. That’s all. The doctors said this would probably happen. I’ll just have a kidney transplant and I’ll be fine. There are people at dialysis that have been waiting for years. But I’m lucky. I don’t have to wait anymore. Mama’s going to give me one of her kidneys.

M’LYNN: We havent’ known that long. We were all just tested last week. I’m the closest match. There are four categories for an organ match. I matched the best.

SHELBY: Swimsuit, evening gown, talen and personality interview. . . . I’m sorry . . . that’s Tommy’s joke. I think it’s very funny.

M’LYNN: I was just so relieved it was me. The boys are young. I would never want them to go through it. And who would want one of Drum’s mean old organs? But! The best thing about all this is that with all the tests and tuff, I have discovered I have the constitution of someone ten years younger. How about that!

SHELBY: My operation’s simple. Mama’s is awful. They basically have to saw her in half to get the kidney. It’s major, major surgery for her.

M’LYNN: They do it on “Circus of the Stars” all the time.

SHELBY: (with a sad smile at her mother’s joke) There have been more than enough tears.

M’LYNN: I’m happy. Look at the opportunity I have. Most mothers only get the chance to give their child life once. I get a chance to do it twice. Poor Shelby . . . .

SHELBY: (firmly) Don’t say that. I have my baby. I’m very happy. If this is a part of the price I have to pay, then I have to pay it. I can deal with it . . .

TRANSITION

Nearly a year later . . . . and the price to be paid turns out to be much higher than expected. . . Annelle, a friend of the family, tries to provide some comfort

M’LYNN: After the transplant failed, she went back on dialysis -- She’d been doing fine the last few months. But last Monday, everything went wrong. It was like dominoes. They thought they could correct things with a little surgery. As they wheeled her down, she said, “Mama. I’m going to feel so good when this is over.” They gave her the anesthetic.

ANNELLE: In a way she was right. Maybe she knew she was going to be with her king.

M’LYNN: (a little shaken) Yes, Annelle. Maybe so.

ANNELLE: We should be rejoicing.

M’LYNN: You go ahead. I wish I could feel that way. I guess I’m a little selfish. I’d rather have her here.

ANNELLE: Miss M’Lynn. I don’t mean to upset you by saying that. You see, when something like this happens, I pray very hard to make heads or tails of it. I think in Shelby’s case, she wanted to take care of that baby, of you, of everybody she knew . . . and her poor body was just worn out. It wouldn’t let her do everything she wanted to do. So she went on to a place where she could be a guardian angel. She will always be young. She will always be beautiful. And I personally feel much safer knowing she’s up there on my side. I know some people might think that sounds real simple and stupid . . .and maybe I am. But that’s how I get through things like this.

M’LYNN: (gentler) Thank you, Annelle. I appreciate that. Shelby, would not want us to get all mired down and wallow in this. She would look on it as just one of life’s occurrences.

SHELBY: I'm going to have a baby. (echos)

M’LYNN: We should deal with it the best way we know how . . . and get on with it.

SHELBY: Would it be too much to ask for a little excitement? (echos)

M’LYNN: That’s what my mind says. I wish somebody would explain that to my heart.

(BEAT – remembering)

SHELBY: Mama. I want a child of my own. I think it would help things a lot. (echoes)

M’LYNN: I couldn't leave my Shelby. I just sat there and kept pushin' the way I always have where Shelby was concerned.... I was hopin' she'd sit up and argue with me. Finally we realized there was no hope.

SHELBY: Mama. You can't live a life if all you do is worry. And you worry too much. In some ways it's a comfort to me. I never worry because I know you're worrying enough for the both of us. (3choes)

M’LYNN: They turned off the machines. (Pause)

SHELBY: Mama. Diabetics have healthy babies all the time. (echoes)

M’LYNN: Drum left.. couldn't take it. Jackson left. (Slight "laugh") I find it amusin'.. men are supposed to be made outta steel or somethin. I just sat there. I just held Shelby's hand.

SHELBY: No one is going to be hurt or disappointed, or even inconvenienced. (echoes)

M’LYNN: Oh God.. I realize as a woman how lucky I am! I was there when that beautiful creature drifted into my life.. and I was there when she drifted out of it. It was the most precious moment of my life... [Sighs]

SHELBY: And when it's all said and done there'll be a little piece of immortality with Jackson's looks and my sense of style...I hope. (echoes)

M’LYNN: I'm fine.. I'm fine.. I'm fine.. I'm FINE! [sobbing/screaming]

SHELBY: Mama, please. I need your support.

M’LYNN: I could jog all the way to Texas and back.. but my daughter can't!! She never could!! Oh.. God . . . I'm so mad I don't know what to do!! I wanna know why! I wanna know WHY Shelby's life is over!! I wanna HOW that baby will EVER know how wonderful his mother was.. Will he EVER know what she went THROUGH for him? Oh God I wanna know WHY? WHY? Lord...I wish I could understand!

SHELBY: I would rather have thirty minutes of wonderful than a lifetime of nothing special. (echoes)

M’LYNN: No...NO...NO!! It's not supposed to happen this way! I'm supposed to go first!! I've always been ready to go first! I don't think I can take this.. I.. I don't think I can take this! I just wanna hit somethin'! I just wanna hit somebody.. till they feel as bad as I do!! I just wanna hit something!

SHELBY: But you get through it and life goes on. (Echoes)
```

---

## IC-0272: Stolen Moments

- Title: Stolen Moments
- Author (byline): Janet O’Neill
- Work: Turning Points
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SUSAN, WOMAN, RICKY, AUNT, FATHER, GINA
- Teaser before the introduction: Yes
- Spoken words (computed): 1119
- Already set (do not supply): none

### Source block (context only)

```text
Author: Janet O’Neill
Book: Turning Points
Publisher: Tichenor Publishing
ISBN: 978-0742117013
Date: 2001
```

### Introduction (context only: never use it for content warnings)

```text
In 1967 the Supreme Court ruled in Loving v. Virginia that marriage bans between whites and blacks was unconstitutional, but before that interracial marriages were illegal in 16 states.

By 1995 interracial marriages were more common and far more accepted than they had ever been. But that didn’t always make it easy.

1995: The year a jury found OJ Simpson “not guilty” for the murder of his ex-wife Nicole. Seinfeld was the most popular television show on 1 of the only 3 major networks. And Men were from Mars and Women from Venus. Black and white relationships were no longer taboo . . . But Susan’s family and friends still had some issues.

Stolen Moments by Janet O’Neill
```

### Performance text (classify this)

```text
SUSAN: I've gotten used to the snickers. The whispering. The name calling. The seven-year-old girl who just points and says Mommy! Look! I know Ricky and I are a scandal. Still, it stuns me when a woman approaches me at a restaurant and says:

WOMAN: Didn't know you liked dark meat.

SUSAN: What do you say? Well, actually I'm a vegetarian? It never works. So I smile. Shake my head. And return to my seat. Skin pigment. It can be hell.

SUSAN: Ricky and I met at the Wash-n-Save Laundromat. He had this aloof look, like nothing could touch him and yet a magnetic charm that made you want to try. Our first conversation was pretty ironic:

SUSAN: Hey, I don't think you want to do that

RICKY: Do what?

SUSAN: (to Ricky) Well, you need to separate your clothes. You're mixing your white and your coloreds.

SUSAN: After dating for a few months, the mixing of the colors and the whites had taken on a much deeper meaning. No one approved. A glare from the parking attendant. A reprimand from my aunt:

AUNT: That's fine if you want to mix for a while, but always meet in a public place. Nothing gets stolen that way, dear.

SUSAN: And of course, there was the resonating response from my father:

FATHER: I don't have anything against Blacks. I think everyone ought to own one.

SUSAN: I kept using the line: It's 1995. People aren't going to tolerate that racist talk. Never seemed to make a difference.

Ricky and I didn't date on the assumption that we'd act like we're colorblind. Race did matter. Everyone else thought so and that made it an issue. But, we were in love. Race became another thing that we could talk about. See, when you're in love, you don't ignore things about the other person. You admire each aspect of them. You cherish them.

And it was love. I'd never been in love before, but if this wasn't it, I didn't even want to know how giddy I'd be when the real thing came along. We'd spend time in the park; watch old M*A *S*H* re-runs; talk all night and then call in sick so we could let the moments linger. Ricky loved me. No doubts. No questions asked. Which is why, when my best friend Gina approaches me with her patented, “We gotta talk,” I could hardly believe that the topic was my so-called "dysfunction."

GINA: What are you thinking? Do you have any idea what people are saying about you?

SUSAN: Let me guess. I'm betraying my race, slumming it, got jungle fever, and if I said the" N" word, I could list a string of adjectives created from it. Who cares?

GINA: Fine. Who cares what they're saying. Here's what I, you best friend, am telling you. Get out. Please. Susan, it's just not right. I'm no Klansman or anything, but I just don't think you know what you're doing . . .

SUSAN: God, Gina. I expected this from my parents. But you? It's 1995. No. You understand me. It's 1995. (Beat; to audience) You know how Bryan Adams sings about the Summer of '69 being the best time of his life? The Summer of '95. It was the best time for me. Despite it all, Ricky and I had fallen deeply in love. So deeply, that when I discovered I was pregnant, I was honestly overjoyed. Really. I told Ricky about it. He agreed; it was a blessing.

RICKY: Guess I'm going to have to make you legit.

SUSAN: Are you asking what I think you are?

RICKY: Not yet. I gotta wait and do it up special. But don't make any plans at New Years.

SUSAN: (to audience) There I was. A not-yet-wed pregnant woman in a relationship no one approves of, and yet all I could say was Sweetheart, that sounds wonderful. I was about to get married. Be a mom. Do it all. Wow. No turning back now. I thought of my father. No turning back now. I thought of Gina, my church, my coworkers. No turning back now.

August was spent in a mad rush between doctor’s appointments, titanic shopping sprees, and stacks of catalogs to be perused in the late afternoons, and, oh yes, stealing moments with Ricky. I was eating for two. Shopping for a wedding. It was exhausting. I collapsed in bed - thoroughly spent; thoroughly satisfied.

Then one morning in early September, Ricky went out early to get doughnuts. Chocolate long johns. A dozen. We were skipping work again. I loved it. He left at 7:30.

8:00: Ricky hadn't returned. 8:30: nothing. 9:00: nothing. I called his friends, my friends, his family - no one had seen him. At 9:43, the call came. I knew something awful had happened. I couldn't pick up the phone, so I just listened to the machine.

Ricky was dead. Dead. Dead. It was a car crash. There was no brake fluid. He had slammed into a tree. It appeared that the car had been tampered with. And that was it.

And you know I could have been thinking a million things like my poor Ricky, should I call his parents? Should I go see him? What do I do? But instead, all I could think was: he was driving my car. It was supposed to be me. It was meant for me. It should have been me. I mean, that's kind of tough to grapple with. Did Ricky die because of lack of brake fluid and the placement of a tree? Or did he die because he loved me? Because someone didn't approve. I mean, it couldn't have been that, right? I mean, it's 1995.

Two events shaped my October: the crash was found not to be an accident, and I lost my baby in its first trimester. The revelation of the crash just confirmed what I knew all along; the revelation of the baby was a strange mix of feelings between this black hole of emotion and an unsettling sense of relief. I felt this incredible void because I'd lost the last part of Ricky I had left. I felt relief that our child would never have to experience the hatred people felt for his Black father, merely hoping for a few seconds of peace.

I became a loner. I didn't see family. I didn't see Gina. I quit my job. But, I spent my time thinking of these people, asking myself one question: Who did it? Who took it all away?

In the end, all I had was the moments. Stolen moments of one summer with a man. A Black man, but a man just the same. Moments in the park. Moments holding hands. Moments forever remembered in black and white.
```

---

## IC-0273: Stop the War from The Syrian Monologues! Personal Stories of Syrian Refugees in Jordan

- Title: Stop the War from The Syrian Monologues! Personal Stories of Syrian Refugees in Jordan
- Author (byline): Fatmeh Al Zoubi, translated by Iman Aoun
- Work: The Syrian Monologues! (Pgs 10-13)
- Publisher: ASHTAR Theatre Part of the Social Phycology Program Care – Jordan) June 2015
- Publication date as stated: 2016
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: FATMEH
- Teaser before the introduction: No
- Spoken words (computed): 1250
- Already set (do not supply): none

### Source block (context only)

```text
Author: Fatmeh Al Zoubi, translated by Iman Aoun
Book: The Syrian Monologues! (Pgs 10-13)
ISBN: on-line transcript
https://louisville.edu/theatrearts/images-1/The-Syria-Monologues-script.pdf
Publisher: ASHTAR Theatre
Part of the Social Phycology Program Care – Jordan) June 2015
Date (Month/Year): 2016
```

### Introduction (context only: never use it for content warnings)

```text
According to estimates from the Syrian Observatory for Human Rights, more than 600,000 people have been killed since the start of the Syrian Civil war in March 2011.

For nearly 14 years the Syrian people have suffered unimaginable horrors as the government, led by President Bashar al-Assad, perpetrated crimes against humanity and war crimes, brazenly violating international norms and treaties. For millions of Syrians the overthrow of the Assad government by opposition forces in December 2024 presents a historic opportunity to transition away from repression and to potentially reunite with loved ones who fled the country.

As of 2024, the United Nations reports more than 7.4million are currently internally displaced, with more than 6.2 million living as refugees abroad in Jordan, Lebanon, Turkey and Europe.

For Fatmeh Al Zoubi, mother of a 3-year-old with another child on the way, fleeing the al-Assad regime was the only option. In her own words . . . from The Syrian Monologues! Personal Stories of Syrian Refugees in Jordan
```

### Performance text (classify this)

```text
FATMEH: (Pg 10-13) When I used to go to my university exams in Damascus, I would take my child with me. There were many checkpoints on the road and sometimes I wouldn’t be able to return home, even though it was only 140 km away. So, I would take him to make sure he’s safe. If the soldiers attacked my town, Taher would be with me under my wings. I will be breathing the same air with him, eating the same food together and at night he will be sleeping in my arms peacefully. When I wake up his innocent face will be the first thing I see.

We used to leave at dawn from my hometown Al-Musayfirah to reach Daraa and then Damascus. This journey would take five hours in each direction due to all the imposed checkpoints that were run by either the army or the rebels. When the bus left my town, it carried 14 people including me and my child. After 3km, the first checkpoint and with it the suffering begins; a long and hard waiting time until the checking is over, one car after another until we get our turn. This happens at every checkpoint until we arrive in Damascus.

[My] little boy knew many war games, especially how to act; yes to act. How can a toddler less than 3 years old act? Taher, my little boy, used to distinguish between checkpoints. He would know which one is for the State Army and which one for the Freedom Army. When we were stopped by the State Army, he would put his little head out of the window and shout: “God, Syria, Bashar only, God protect the army.” When the commander heard him, he laughed, approached him and asked: “What’s your name? How old are you? Where are you going? Do you love Syria? Do you love Bashar?” And when my son finished answering; the commander would laugh and ask the soldiers to open the checkpoint and give way to the bus.

We were all saved because of him. No one was arrested or asked to show his/her ID card, and we passed quickly. After 40 km, the bus is stopped again at a checkpoint for the Freedom Army, so Taher started yelling: God, Syria, Freedom only, May God protect the Freedom Army.” He did this at every checkpoint we encountered until we arrived in Damascus, and every time the soldiers would laugh and allow us to pass without searching us. This saved his innocence, protected his dreams and guaranteed his mother’s way to her exams safely and peacefully.

[But] the clashes accelerated and I had to make the decision to get to a safer place. I decided to leave my country, my family and my dreams. I took my children; one in my arms and the other in my womb; left my house and reached the first point of my immigration saga. I was in Al-Tayba area, still breathing my country’s oxygen, walking over its soil and breathing the same air as my loved ones. Every time I heard the sounds of the army’s boots and bombs, fear would eat my heart up. I would panic for those I left behind and for those I carry in my arms and in my belly.

I reached the first point of my exodus. We were put in an old house that had cracked walls like our shattered dreams and ruined doors like our torn souls. Its windows were sealed and every time I looked at them, I wondered; would they ever open? Would we ever get our freedom? Would the war end? I waited very long before night fell and we were able to leave that house to our escape journey. I forgot my coat in that grim house, I tried to get back for it, but the smuggler refused. I did not want the coat because it was cloudy and the wind was blowing off our bones; I wanted my coat because the smell of my father was still on it. He brought it for me, with tears in his eyes, worried about my unknown future. How I wish to go back to my father’s arms.

A woman’s voice, about my mother’s age, woke me up saying: “Come on, we’re starting to walk.” I started sobbing and was not able to distinguish between my tears and the rain, as if heaven was embracing my weeping, and the sound of the wind was surrounding the cry of my broken soul. I was terrified; I started asking myself: “What kind of stupid decision I made? Would I reach a safe haven? What would happen if I’m not able to cross over the war zone?” An internal voice cried: “You have promised your child.”

The smugglers started to yell: “Stop the babies from crying, they have to sleep so the soldiers won’t hear us and attack. Do not talk.” I was carrying my child and a small bag filled with his clothes. His brother’s heart inside me was beating every minute in my ears. The night was dark and fear was dominating everyone.

One could see the misery in the faces of the worried people. We were 5 men and 6 women with their children. All we were able to hear was our heartbeats filled with fear and the sound of our steps and those of our children, walking slowly and silently. The route was rough, filled with stones and thorns. All of a sudden, we heard the cry of a baby longing for his mother’s milk. The smugglers started screaming at the mother: “Hush him, hush him up” and they changed our way into the wood to reduce the sound of the screaming baby. We sat under the trees, while the smugglers covered the mother and the baby with blankets.

We continued our journey. My child was still in my arms. I started to feel his weight getting heavier. My body was collapsing. We arrived at the high hill that we had to cross. A man came through the darkness, covering his face with the Syrian flag, and told me: “You have to climb the hill.” I said: “I cannot, I’m pregnant.” His tone changed: “Why didn’t you tell me?” He took my child and we crossed over the hill, our feet stumbling towards the Jordanian border.

The sound of the children’s footsteps during our journey is still alive in my memory. Their steps scattered and scared, yet light and innocent like their dreams, in the beginning. . .

To all the leaders of the world: Stop the war in my country. Stop the bleeding, stop it.

I hereby declare in all the languages of the world: I miss my country, my home, and my children. I miss my university that used to feed my knowledge.

Stop the war.

I miss the walls of my destroyed house, my broken mirrors, and my scattered furniture. I miss the ground in front of my door and the flowers planted in my garden.

Stop the war, the destruction and the killing.

I miss the dream of my country that was shredded by the wounds, the pain and the war. I miss my memories, my happiness, and my wishes. I miss 25 years I spent in my country.

Stop the war, stop the massacres; I’ve been waiting too long on the pathways of hope and in the alleys of dreams. Stop the war.

I want to miss the sounds of missiles and tanks.
```

---

## IC-0274: Sudden Acceleration

- Title: Sudden Acceleration
- Author (byline): Dan Nigro
- Work: Winchelsea Dround and Other Plays
- Publisher: Samuel French
- Publication date as stated: 1992
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MOLLY
- Teaser before the introduction: No
- Spoken words (computed): 925
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dan Nigro
Book: Winchelsea Dround and Other Plays
ISBN: 978-0573625985
Publisher: Samuel French
Date (Month/Year): 1992
```

### Introduction (context only: never use it for content warnings)

```text
Who knew that when Henry Ford created the Model T that it would develop into something that has a mind of its own? Man’s inventions often reflect man himself. His brilliance, his power and his insanity. AND this was never more true than for Molly and her family; when a simple gift turned into a life changing experience. Sudden Acceleration by Dan Nigro
```

### Performance text (classify this)

```text
MOLLY: I remember the day my husband brought home the new car. Something cheaper would have done us just as well, but he has the money, and he wanted to surprise me. He’s always been a very considerate and loving person. Our little boy was excited too. It smelled so nice. New cars smell like god’s study. It was a pleasure to drive, handled wonderfully. Men would flirt with me in traffic. There were no problems, everything is microchip now. It’s amazing, all that possibility locked in such a tiny universe. Imagine my surprise, when on a bright spring day, as I prepared to go to the store, I needed flour I think it was, I waved goodbye to my little boy, got in the car, turned the key, it started right away. It was still in park. And then suddenly the car, like a creature from a nightmare, the car lurched forward violently into my little boy, who had been a good twenty feet away, and pinned him into the back of the garage wall. The moment I felt the car jump forward I jammed my foot down on the brake, but it just ignored me, it ignored me completely. It kept ramming, ramming itself into my child, who now remained pinned between the car and the garage wall. Again, and again while I screamed and pressed down on the brake as hard as I could and later I discovered I had broken two bones in my foot.

He later died in the hospital. I remember his face looking at me. He didn’t say anything but I know what he was thinking. “Mommy, why did you do that, why did you do that to me, why mommy?”

There was a police investigation, of course. Mechanics couldn’t find anything wrong with the car. Our mechanic said that in the old days when something was wrong you could find it and fix it. Things were mechanical; you know how things worked. But these new cars, this new technology, its all Spooksville, Spooksville.

You don’t know what it’s going to do, and when it does, you don’t know if it’s going to do it again. Everything is so tiny. It’s all probability. Nothing is certain. Uncertainty is at the core of things. The police called it an accident. But my husband couldn’t let it rest there. He sued the car company, there was a trial, and I had to tell my story again and again, reliving it each time. It was horrible. But we thought it was the right thing, because if this could happen to us, it could happen to anybody, anybody’s child, anybody’s husband or wife. And in the course of all this, we meet hundreds of people, with the same upscale cars, and the same thing had happened to them. One man’s car lurched into reverse while it sat running and empty, while driverless, it smashed into the front window of someone else’s house. Another woman went through two fences and a tool shed, all the while with her foot on the brake the whole time. There were a series of further investigations and tests. It took months, then years. I told my story again and again.

The car company people hired a battalion of famous and very expensive lawyers to prove that they were not at fault. The ridiculed us for our ignorance of the technology. They were shocked that we would try to extort money from them, to get rich off the death of our child. Commission was set up. But by this time had lost all out money to litigation. We lost our house, we lost everything. The car company wined and dined the members of the commission. Money changed hands, backs were washed favors were done. The big boys take care of each other. The commission ruled that the cars had been engineered perfectly. There was nothing wrong with the cars. Tragic accidents like the one that had caused the car I was driving ram repeatedly into my little boy were simple acts of human error. I had mistaken the gas pedal for the brake. It was my fault. The Car Company declared blameless. My husband began to drink. On TV, the car company hired famous actors that I had admired to drive their cars and tell how safe they were. Certain design changes were made quickly. I watched the TV. I sat there. My husband had stopped talking to me altogether. We no longer slept in the same room. Then today I figured out what I was going to do.

I will go to the corporate headquarters of the Car Company. I will watch outside the building for the president of the company. I’ve seen news footage on him coming in and out. There is a certain wall he passes along every day to get to his car. When I see him come out, I will step on the gas and drive him directly into the wall, again and again, until this man is cut in half. And when it’s all over, I will sit in my car and wait till the police come and when they ask what happened, I will say, WOOPS. So sorry. I must have mistaken the gas pedal for the brake. It was just a simple error. Perhaps they could get their high paid engineers, and their lawyers and their beautiful spokes people to put this poor gentle man back together again. It certainly was not intentional. It was just another example of sudden acceleration.
```

---

## IC-0275: The Susan Smith Tapes

- Title: The Susan Smith Tapes
- Author (byline): R.M. Vaughan
- Work: The Monster Trilogy: Plays
- Publisher: Coach House Press
- Publication date as stated: 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SUSAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1502
- Already set (do not supply): none

### Source block (context only)

```text
Author: R.M. Vaughan
Book: The Monster Trilogy: Plays
ISBN: 978-1552451328
Publisher: Coach House Press
Date (Month/Year): 2003
```

### Introduction (context only: never use it for content warnings)

```text
At the age of 23, Susan Smith was convicted for murdering her two sons, 3-year-old Michael and 14-month-old Alexander. The case gained worldwide attention, after she claimed that a black man stole her car and kidnapped her sons. That was a lie.

The defense argued during the sentencing phase of the trial that difficult life circumstances and depression led Susan to a failed suicide attempt, a suicide attempt that resulted in the “unfortunate” deaths of her children. On the night of their deaths, Mrs. Smith parked her car on a steep incline leading to the lake. She let go the hand brake, reconsidered and pulled it up again, then let it go and – in some instinct for survival – jumped from the car, allowing it to roll into the lake, and drowning her children inside. How, many people wonder, was that a suicide attempt?

The jury rejected the death penalty and instead sentenced her to life in prison . . . to remember . . . in a tiny cell with the ghosts of her dead children.

The Susan Smith Tapes by R.M. Vaughan in which the infamous young mother tries to recapture the public’s attention by auditioning for talk shows from her prison cell.
```

### Performance text (classify this)

```text
SUSAN: Miss Oprah, I hope you still remember me. My name is Susan Smith and I did an evil thing. (She stops the camera, rewinds for a few seconds, then starts again) Miss Oprah, I know you still remember me. My name is Susan Smith. Evil things happened to me.

[Smith sets up a video camera on a tripod between herself and the audience]

SUSAN: (Tape 1) Hello, Miss Oprah? I hope you can see me all right. I don’t photograph too well. I mean, with these lights and all. And the white – white makes me look fat. Miss Oprah, I’m sending you this tape because I think maybe you never got near my last letter. It came back all bent up and ragged like a worn-out mop and I don’t like to think you’d treat a heartfelt letter that way. Funny thing was, when I make the word ‘heart’ I don’t spell it out h-e-a-r-t but I draw it directly on the paper, like a valentines heart (draws heart with finger in the air), I always done that, since I don’t remember when – and, well, when my last letter came back, somebody, well, somebody mean, took my letter an cut out every one of my signature hearts. Why do people do these things? Guess some folks can’t forgive and forget.

Miss Oprah, I’m scared. So what, everybody’s scared. I learned that here. But I’m scared of history. What are people gonna say about me in the future times? Miss Oprah, a lot of untrue stories have been said about me and I need to have my time to make my say. I was a good mother to Michael and Alex, right up till the bad time. Those boys was always clean and dressed sharp and they never went hungry one minute of their lives. That is my truth. Can’t nobody take that achievement away from me.

Momma still talks about the day you came down from Chicago to visit the lake where my boys went to Glory. I wish you hadn’t brought your cameramen to the lake, though, because it’s such a pretty lake and now the whole world only sees the bad side of the location. Maybe you and me can work together to make that old lake shine again. I am good on TV, I come across natural. (End of Tape 1)

SUSAN: (Tape 2) Mr. Springer, my name is Susan Smith. You did a show on me a few years back, and I’m just saying thank you again. I guess you can tell I’m still in prison. I gained some weight since you saw me last, from the sittin’ all day.

Kinda a relief, just to let go. If I’m healthy, I thank the Good Lord for my fortune.

Mr. Springer, when the incident I done involving my two boys came out, there was a whole team of folks at the county District Attorney office workin’ day and night to fix me for the electric chair but they lost. Listen to me! Of course they lost, ‘cause here I am alive and jawin’ away like a TV talk show person myself. I saw you done a whole program on the badness of the death penalty, and I was thinking you should do another one because the issue is very large in the minds of many people. I can help out, if you like.

When my boys was killed, I took responsibility. I was slow to it, I admit, but eventually I come around to the truth. People say the bet ways I can pay back for my boys is for me to go on over to the other side myself, but there’s more than one way to make amends. I want to come on your show and tell young mothers my story, so’s they can learn from my example. If the State of South Carolina up and hauled me to the electric chair, they ony get a one-shot deal on the example of my life. That’s a sinful waste of the human spirit.

I been practicin’ my set piece, and now I would ask you to hear it out. (She reads from a sheet of paper). My name is Susan Smith, and I have experienced great tragedy in my life. The death of a child is every mother’s worst all-time day and nighttime nightmare. The death of two children is double that plus some traumas nobody can name. I am here today to tell all you kind people that human life is precious and unreplaceable. I know because I will ever hear my baby boys’ voices again. I will never see them goin’ off for the first day of school, never help them with learnin’ their times tables, never go down to the front porch to meet their girlfriends and never hold their own babies in my arms. Life is cruel and beautiful too, but the cruellest day in the world came when circumstances situated to take my babies from me. Even after I am dead and gone I can still hold my head up high to the sky above and say no matter what I am a mother, and that is a no-refund deal. (She sets the paper down) What do you think?

Mr. Springer, I don’t deserve to die. My boys and me, we had a special bond. We was like people who can talk to each other without saying a word, them gifted people with angel powers. I couldn’t walk away from that power, Mr. Springer, nobody in the world could. My mother love was too strong. Them boys woulda spent the rest of their lives wondering why they was so bad that their momma put herself at the bottom of the lake rather than be with them. I would have put a curse on my own children had I gone to Glory before my time. I admit to my shame I wanted to commit suicide, but I did not leave my boys abandoned, I did not take the easy road and leave my babies to make on in the world without a mother.

I made a choice, for my babies. That’s what folks is afraid of, the deep-down feelin’ they got that they don’t wanna hear talkin’ to them – the voice that says Susan Smith done right, horrible right, but right. It’s too hard to bear. I made a choice, in a second, in a half a minute, and it moved the world to tears. Anybody wants to come kill me better look around and ask hisself when was the last time he sacrificed like I sacrificed for my babies. Most people won’t even put a sick dog down, they’s so selfish. I am not afraid to cry on Wednesday so I can smile on Sunday. All my life, I have always looked to the horizon, not the trail. Sometimes I think I am the bravest woman I know. (End of Tape 2)

SUSAN: (Tape 3) You may not remember me – but my name is Susan Smith. I never wanted this kind of national attention, but I got it anyway, so I may’s well get in my say in the story. Miss Walters, I believe life is about decisions. Have you ever made a decision that took only a couple of minutes but changed the rest of your day? I did. If you want to show this video on the 20/2 show, I won’t mind.

When I left my home on Tuesday, October 25, 1994, I was very emotionally distraught. I was a girl in a woman’s body. I couldn’t sort our my needs. I understand that now. My boys – Michael, he’s three, and Alex, the baby, he’s fourteen months – got in the back of the car like always. Michael says, “Lock the doors, Momma!” – he always said that. It was our automobile safety game. I showed him how to fix his baby brother into the car seat so that he was safe and snug as a Eskimo papoose.

We drove around for four hours, the boys were asleep. I wanted to see the lake, the lake is so alive. If you go at night, you can watch the catfish jump for bugs and it makes you feel energetic. The lake’s full of catfish. But lately folks don’t eat them like they used to, they say the lake’s poisoned forever. People are full of hate.

I say by the side of the lake while the boys slept and snored and talked baby dream talk to each other and I thought to myself, I want to die. It just came over me, the death pull. I’m like that, just get taken away by emotions. I felt I couldn’t be a good mom any more. But I didn’t want my children to grow up without a mom. I had to end our lives to protect us from any grief or harm.

The car when in no trouble. The mud around the lake is so slick. Michael woke up for a minute. “Where we goin’, Momma?” He never said another word, smart as can be. “I love y’all! I love y’all! I love y’all!” He knew.

My name is Susan Smith. Evil things happened to me.
```

---

## IC-0276: Tamam

- Title: Tamam
- Author (byline): Betty Shamieh
- Work: Talk to Me: Monologue Plays
- Publisher: Vintage
- Publication date as stated: Dec 2004
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2044
- Already set (do not supply): none

### Source block (context only)

```text
Author: Betty Shamieh
Book: Talk to Me: Monologue Plays
ISBN: 978-1400076154
Publisher: Vintage
Date (Month/Year): Dec 2004
```

### Introduction (context only: never use it for content warnings)

```text
Nelson Mandela once said “When a man is denied the right to live the life he believes in, he has no choice but to become an outlaw.”

Everyone has heard of the Israel-Palestine conflict. Everyone knows it's bad, that it's been going on for a long time, and that there is a lot of hatred on both sides. We’ve heard of and live in fear of jihadists. We know the history of the persecution of Jewish people now living in Israel. We know the words “holocaust” and “the final solution.” But we are removed . . . so removed from the daily conflict that it is almost impossible to understand how citizens of these countries, these two conflicting cultures, struggle to survive on a day to day basis.

In Tamam by Betty Shamieh, we hear firsthand from a young woman, the sister of a Palestinian suicide bomber, about her culture, her life, her fears and her family. Taman by Betty Shamieh.
```

### Performance text (classify this)

```text
My name is Tamam. It means enough.

I was called that because my family wanted no more

daughters.
I am the last of seven sisters, good luck for the family.
After me, there were two brothers
and now there is only one.

Why do we rejoice when a boy is born?

Because we from Gaza understand the power of might.
The strong make the rules,
name the cities,
and decide who live in them,
or so they think.
We know what it means to be weak,
to cement a settlement of resentment,
brick by brick,
in our own ravaged hearts and shell-shocked minds,
with every corner
littered with bullets, tear gas canisters,
they say "Made in Pennsylvania" on them.

Times like these call for soldiers. The ones we had have fallen.

A birth of a girl is different from a boy.
A girl is a gift that's too precious,
a reminder that soft things don't last long
in our world.
Parents here fool themselves,
thinking a boy child has at least almost
a fighting chance.

I want to talk about something smaller than me that became bigger.

I want to talk about my brother.

Don't believe the stories you've heard.
I was far more religious than he.
I never had the heart to wake him to pray.
He was hoping to study medicine in Iraq
while building Israeli settlements in Gaza
so we could eat.
I let him sleep through the call.

He was caught with a rock in his hand
and a curse on his lips.
I went to the jail to visit my brother.
Most of my people looked at the Israeli guards,
with every ounce of hatred a human heart can hold,
their faces twisted not like they tasted something bitter,
like something bitter was forced down their throats.

I was smarter than that.

I knew I must navigate through the maze of might,
and did my best to be kindly, polite.
Hoping perhaps that I would
remind them of a Rachel or Sarah or Ruth
that they knew or would have liked to know.
So when they beat my brother,
that thing that started out smaller than me and got bigger,
they would lighten their touch.

I am a pretty woman.
It's not a compliment, it's not a boast.
It's a fact.
Looks are a commodity, an asset, a possession I happen to

possess.
It's why my grandmother said no,
when my sister's brother-in-law asked for my hand.
The family that was good enough
for my plain sister wasn't good enough for me.
I'm a pretty woman.
It's not a boast.
It's a fact.

And I smiled my best smile
when the soldiers opened the gate for me.
Weighed down with baskets of food,
I brought extra,
hoping to create the illusion
that that dirty jail was one place
where there was enough and extra for all
the guards to eat twice.
Otherwise, my brother would get none,
unless there was enough and extra.

They thanked me for the food and they raped me in front

of him,
forcing my brother's eyes open so he had to watch.
They wanted to know something
that he preferred not to tell them.
They skewered the support for their argument into my

flesh.

I'm told that their torture specialists who study the "Arab"

mind
realized rape would enrage our men.
Enraging a man is the first step on the stairway
that gets him to a place
where he becomes impotent,
helpless.

They not only refer to us as the cockroaches,
they examine us, experiment upon us,
as if we were that predictable, that much the same,
that easy to eradicate.
Their studies show the Arab men value the virtue of their

womenfolk, Their studies show something within me was supposed to

be inviolate.

Say what you want about Arab men and women
and how we love one another,
There is one thing that's for certain.
There are real repercussions for hurting a woman in my

society. There are repercussions.

When the first hand was laid upon me, we both screamed. The evolutionary function of a scream is a cry for help, they tied down the only one who could so I silenced myself. That was the only way to tell my brother I didn't want him to tell.

I flinched when I had to,
but I kept my breathing regular.
My brother tried to look every other way,
but realized I needed him,
to look me in the eyes
and understand.

They thought making us face one another in our misery would break us.

But we were used to misery. It's like anything else, you can build up a tolerance for it.

Someone once told them what they wanted to know, so they released my brother two weeks later.

That's when he built something
more intricate than the human heart,
hugged it to his chest,
and boarded a bus that was going nowhere and every-

where. The day he did it, he told me over breakfast-

"Oppression is like a coin maker.
You put in human beings,
press the right buttons and
watch them
get squeezed, shrunk, flattened
till they take the slim shape of a two-faced coin.
One side is a martyr, the other a traitor.
All the possibilities of a life get reduced to those paltry

two.
The coin is tossed in the air
it spins once for circumstance,
twice for luck,
and a third time for predilection
before it lands flat.
The face that points down
towards hell
determines not only who you are,
but how you will become that way."

What he was really saying was good-bye.

Had I known, I would have said something more than
"It's interesting
you think oppression
makes us turn into a form of money, a currency.
How odd."

Listen, I don't agree with killing innocent people
under any circumstances, ever.
The irony is
there were Palestinians who were Israeli citizens on that

bus too. My brother wasn't counting on that. No one was counting on that.

I want to feel sorrow when anyone is suffering, No matter who they are or what their people have done to

mine,
no one's life should be snuffed out.
I am the kind of human being
who refuses to get high on the drug of hate.
In my opinion, that's the only kind of human being there is.

In other words, no one is going to reduce me to a coin.

There are absolutes, it's wrong to kill, period. And since the Israelis have killed five times the number of

my people,
as we have killed theirs,
I think they are five times as wrong.
It's hard to feel sad for them sometimes,
but I swear to you that I try my best.
But it's not easy.
They complain they can't go to a pizza parlor
while they bomb us in our homes.

I should have known what my brother was bound to do, I could have stopped him.

I said every time he went out to face their guns with our

rocks.
"Don't go.
Let's achieve peace by peaceful means.
Let's use nonviolence.
Don't be a pawn.

What kind of fool would face a gun with a rock?
Let others risk their lives.
They can never truly win.
They could kill every Palestinian and the wind will howl ~

our names and the rocks will" rise up ,nd throw themselves,"

I'd always say, "Don't go."
But I didn't say,
"You are the most precious thing in the world to me.
The fact that you exist makes the earth spin on its axis,
it's rolling for joy because you are here.
The sun shows up to see you,
and the moon chases the sun off to be in your sky
and none of them love you like I do, brother.

Not even close.

There is no goal, no political means,
worth wrenching your life from mine.
If Palestine is Utopia, Palestine is already here.
Palestine is my brother being by my side
and screaming for joy when I have my firstborn
and living long and laughing loud with me
over hot tea and warm bread,
each morning,
which is all we can afford
but, if you are by my side, is more than enough.

If you think this is a gift for me,
the box will be empty, brother.
How can it not be?
Everything will be empty, if you're not here.

Don't hurt yourself and others in my name or for my sake.
I will not forgive you if you leave me.
I will not be comforted.
I will not be."

Instead I said, "don't go," and I didn't say it loud.

They bulldozed our house
because you blew up that bus.
In all this, I didn't realize what true fear, true dread, was
till I watched our younger brother
watching them destroy our home,
witnessing each swoop and scoop,
with more anger in his eyes than I had ever seen in yours.

I was engaged to be married
to the love of my life and the richest man in Gaza.
My father went to his house
and told his father what had happened to me.
He didn’t want scandal if we went ahead and married
and it was found I was not . . . . as I was before.
My love left me,
because of his father’s insistence.
His mother, who never liked me anyway,
took him and married him to a girl from her town.
He moved to London with her
and I haven’t seen him since.

I try to convince myself
that I wouldn’t want to be married to a man
who could ever betray me.
I try to convince myself I’m better off without him.

Try is the operative word. His cowardice was a violence that hurts and haunts me more than what the guards did to

me. Because I have no one to blame but my own people, Which is as hard to do as blaming yourself.

I married my sister’s brother-in-law, who was made aware that I was not . . . as I was before.

My youngest brother went to Iraq the week before my first child was born. He went to study engineering.

I’m worried about him. Our friends there say he disappears for months at a time. He never tells me where he goes or when he’ll return.

I’m worried about him.

My husband and I understand each other, which is not exactly a good thing. My husband never lets me live it down that my family

once rejected him, He calls me a whore when he is angry and stuck-up when he is not.

He get angry often,
Especially when I tell him he is worthless and not a man
when he can’t find enough food.
It’s the only way to make him steal it.
Like I said before, we understand one another.

I think of my first love who deserted me.
Every day, I visualize a new way I’d tell him
what a traitor he was to leave me,
in case I happen to ever see him again.
It makes me sad that,
though he wronged me in more ways than one,
He’ll only have ears to listen to the first words I say.

You only get one chance to tell people they are wrong, You get that chance because it takes people a minute or

two
to realize your’e telling them stuff they don’t want to hear.
Then, they shut you out,
thought they might be still standing before you,
Smiling,
they make sure the door between the ear and the heart is

locked And they forever take away your key.

Because they know if they keep listening,
they might not change,
but it will be a little harder
to stay the same.

If I saw him today, I would tell him: “You should have married me. I was still a virgin, even after what the Israeli soldiers did to

me. I was still a virgin, because I don't consider the men who raped me human

and,
if you had any inkling of what a true man was
or how to be one,
neither would you."

My name is Tamam. It means enough.
```

---

## IC-0277: Teenage Waistland

- Title: Teenage Waistland
- Author (byline): Abby Ellin
- Work: Not specified
- Publisher: Public Affairs
- Publication date as stated: 2005
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1896
- Already set (do not supply): none

### Source block (context only)

```text
Author: Abby Ellin
ISBN: 1586482289
Publisher: Public Affairs
Date(Month/Year): 2005
```

### Introduction (context only: never use it for content warnings)

```text
If your son or daughter is overweight, if you and your family struggle with "food issues," you've probably had your fill of news about the "childhood obesity epidemic." Abby Ellin, a journalist and former fat-camp attendee, has an abiding compassion for overweight kids. In "Teenage Waistland" she shares the story of her family's attempts to "save her" from obesity and explores how they might have done it better. Teenage Waistland by Abby Ellin.
```

### Performance text (classify this)

```text
I was ten the first time I stepped on a scale. It was the summer of 1978, and I was visiting my grandmother in Florida.

Each morning I woke up in her big bed and she smothered me with kisses. "Good morning, beautiful!" she'd sing, and ask what I wanted for breakfast. She'd set up a tray for me while I lounged in bed and watched Phil Donahue. In the afternoon, Grandma and I would go for our daily two-mile walk, past the golf course. On the way home we'd stop there to weigh ourselves on the gigantic outdoor scale. "Girls have to be thin and beautiful," Grandma would say, always linking the two adjectives together. "The world judges on first appearances."

The routine was the same every day: we'd wait in line behind the old ladies while they handed their packages to their husbands, who seemed tolerant and bored. The women stepped on and off, and then Grandma got on. She didn't look like you'd expect a grandmother to look, soft and round and smelling of gingerbread. No, this Grandma was all sharp angles and points; her make-up and hair carefully arranged, her clothes stylish and neatly pressed. She was interested in modern art, theater, movies, clothes, she took great pride in her appearance, especially her weight. She was skinny, and the needle hovered around 120.

Then it was my turn. Was I ever really fat? Well, no, I suppose. Not technically. As a child I was a gymnast, muscular, firm; my greatest pleasure was going to gymnastics and coming home to a large cheese pizza, oil dripping on my leotard and tights. I loved peppermint stick ice cream, fruit-flavored jelly beans, Duncan Hines chocolate frosting.

I can't recall a time when I wasn't conscious that fat was bad. My mother had taped a picture onto the refrigerator of an obese woman rifling through a freezer, a warning of the dangers lurking behind that door. My older sister and I were constantly cautioned by my mother and grandmother never to gain weight. In our minds, getting fat was a terrible tragedy, the worst fate to befall a person. Fat was ugly, undignified, a sign of weakness and failure. But though I was aware of this, I never really worried about it. I could inhale tons of food and burn it off at the gym. Fat, like fatal car crashes or terminal illnesses, was something that happened to other people.

I'm not quite sure how the weight- gain began; it built up gradually, tentatively, so slowly I hardly noticed. My interest in food acquired an obsessive quality that, looking back, seems like the early seeds of an addiction. Not surprisingly, food stopped being a source of pleasure and became, instead, the enemy. My body will never be as slight as Kate Moss's (will anyone's?), but as an adolescent I yearned for nothing more than matchstick legs and pelvic bones as sharp as steak knives.

I desperately wanted to be thin, but I resented the sacrifice. One of my few delights was eating--why deny myself? (After the initial horror of 9/11 dimmed, my philosophy was, "Well, if the terrorists are going to get us, we might as well eat...")

5 years later, when I was 15, my Florida grandmother came to visit. As usual, she looked wonderful, her nails newly manicured, her clothes freshly pressed. She kissed me hesitantly, her hands kneading the strange new flesh on my shoulders and back. She was horrified.

Later, I overheard her telling my mother that I'd gotten "tremendous." At dinner, I reached for a second slice of kugel, and my grandmother slapped my hands away. "You don't need another," she said. "How can you let yourself go like this? You've got such a gorgeous face--don't you want boys to like you? Don't you care what people think when they see you?"

"Ma, don't," my mother said, dipping an apple sliver into a bowl of honey.

"You've got to get hold of yourself," Grandma continued. "You need to lose fifteen pounds or else you can't come to Florida this Christmas."

"But why?" I said, tears burning my eyes. "Who cares what I weigh?"

"Because the world judges on first appearances," Grandma snapped. "Don't argue with me. It's my home and I don't want you there unless you look the way you're supposed to."

"But it's a big state," I stammered, trying to joke. "I can fit."

"No," she said, and I knew she meant it. I was devastated. I'm sure my grandmother meant well, and was only doing what she thought was helpful. Over the next few months she clipped diets from magazines and mailed them to me. Her favorite was the Weigh of Life, a program that incorporated fruits, vegetables, and lots of protein into a daily regimen. Her passion was militant. "You really have to look at this as a way of life," Grandma said over the telephone. "You've got to think of fattening foods as poison--things that will kill you if you eat them."

My mother tried to help. She cooked low-fat, low-calorie meals, weighed and measured everything on my plate. She labeled the food in the refrigerator. Healthy stuff had my name taped on it, the more fattening stuff was for my father, brother, or "company." I tried to be good, tried to eat salads without dressing and only one slice of pizza. And yet I constantly wondered why I was depriving myself.

Would lead roles come my way if I got thin? Would the National Merit Scholarship people call me? Would guys pound on my door until it caved in? Part of me doubted this, while another part "did" believe my life would magically transform itself once I knocked off ten pounds. And so I kept trying, but that would only last a few days. Then my body would feel weak and sluggish and my thoughts would focus on what I wanted to eat and what I couldn't eat and why I couldn't eat it. Sometimes the hunger was so bad I'd rummage through my mother's purse and pluck out a ten- or twenty-dollar bill. I'd stuff it into my pocket and head to the nearest supermarket, buying boxes of Twinkies and bags of jelly beans. I buried them in my middle drawer, beneath my bras and collection of foreign currency, locking my bedroom door while I ate.

I wasn't the only one who hid food. Every so often I'd open a cabinet, a storage bin, and find chocolate or donut holes stuffed into brown paper bags. Once I even discovered an apple pie in the trunk of mother's Cadillac. I'd slip the goodies inside my shirt and sneak upstairs to my room. The next day I'd shove the wrappers in my knapsack and toss them into a garbage can at school. One day I came home from school to find my mother waiting for me, an empty box of Devil Dogs in hand. "Where the h ell did this go?"

I shrugged and flipped my palms, looked her straight in the eye. "How would I know? I didn't even know you had that," I lied. "Ask your other children."

My mother laughed sadly. "Ray's too young, and you know your sister wouldn't eat that. She won't eat anything."

That was true. While I was getting bigger, my sister was still wasting away, her bones sticking out like wire hangers, her belt cinched twice around her waist. She'd lock herself in her room for hours, doing sit-ups and leg lifts. She'd actually removed the mattress from her canopy bed, installed a weight set where the bed used to be, and slept on the floor. Why my parents let her do this still puzzles me. I guess it was easier to give in than to fight.

At mealtimes my mother's eyes would dart between my plate, which was full, and my sister's, which was organized like a closet: chicken in one compartment, peas in another, mashed potatoes in a third. She chopped her food into sixteenths, chewed each piece twenty times, careful not to let her fork touch her lips. She still exercised daily, running five, six times around the reservoir.

"Where did you hide that?" I asked, trapping her. "'Why did you hide that?"

My mother looked at me and then at the empty box of Devil Dogs, back and forth, back and forth, as if the answer lay in the space between. "Because you're fat," she said finally. "I love you, but you're fat."

I jerked backwards, as if she had punched me in the gut. "Then how can you love me?"

Did she worry about me? And if not, why did she give me so much grief for being overweight? "I didn't worry that you'd get sick because you were fat, but I worried that you would suffer the consequences of a society that viewed slenderness as desirable," she said. "I didn't know what to do. I did the best I could."

"The best I could. The best I could." At the time, that wasn't enough, but now that I'm older I get it. I understand her frustration, and her inability to do the "right" thing. Is there "ever" a right thing when it comes to parenting?

I'm betting this sounds familiar to you, too, especially if you are or have ever been a fat kid. If you're the parent of one you might see yourself in my mother, faced with a child who has some kind of weight problem, and not knowing what to do. And so you try anything and everything: modeling calorie-conscious behavior; storing healthy food in the cupboard; supporting his or her efforts to diet and exercise; trying behavior modification and setting up rewards for success. But you mainly succeed in making your kid feel bad, ugly, angry, guilty, and miserable.

Only now, with friends stumbling through parenthood, do I really get what my own folks had to deal with and how absolutely flummoxed they were. You never know how your kid is going to turn out, but I doubt my parents expected their two daughters to spend their adolescences fixated on weight. It's fascinating, if you think about it: My sister and I both received the same messages about fat, but we handled them so differently. What made me internalize them one way and her go the other route? What made her shun food, and me run toward it? And what the hell should my parents have done for either of us? It must have been heartbreaking for them, desperately wanting to help their kids while being utterly incapable.

Not that I let them off the hook completely. I spent years condemning my folks (well, mostly my mother) for even making food an issue in the house. If my mother had her own issues under wraps, I believed, my sister and I would never have had to suffer. I still believe this is true, but I don't resent my mother--or even my grandmother--anymore. Now that I'm older, I feel bad for them, for all of us. It's hard enough just to survive on this planet; most people are simply doing the best they can. Yes, some people absolutely have no business reproducing. But the average person--my own parents, you--truly wants what's best for their kids. If they only knew what that was, or how to bring it about, things would be a lot easier.
```

---

## IC-0278: These Shining Lives

- Title: These Shining Lives
- Author (byline): Melanie Marnich
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: June 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DR. DALITSCH, CATHERINE, TOM, MR. REED, CHARLOTTE, VOICE OVER, REPORTER 1, REPORTER 2
- Teaser before the introduction: Yes
- Spoken words (computed): 1308
- Already set (do not supply): none

### Source block (context only)

```text
Author: Melanie Marnich
ISBN: 978-0822224488
Publisher: Dramatists Play Service
Date (Month/Year): June 2010
```

### Introduction (context only: never use it for content warnings)

```text
It was the early 1920s and one of the most sought-after jobs for young women in America involved something exciting and brand new: Radium. Sparkling, glowing, and beautiful, radium was also, according to the company, completely harmless. It would make watch faces glow in the dark. And so, an excited Catherine Donahue found her dream job at age 19 and was hired by the Radium Dial Company. It was a marvelous. . . until it wasn’t.

Throughout American history, women have fought for better wages, equal rights, and safer working conditions. The Radium girls of the 1920s brought about the first legal case in which an employer was held responsible for the health of its employees. In the words of author Audre Lorde . . . [This is] “for those women who do not speak, for those who do not have a voice because we are taught to respect fear more than ourselves. We’ve been taught that silence would save us, but it won’t.”

Based on true events, this is These Shining Lives by Melanie Marnich
```

### Performance text (classify this)

```text
DR. DALITSCH: (Pg 46) . . . your fractured jaw resulting from a tooth extraction and the subsequent infection in the tooth’s socket, in addition to anemia . . .

CATHERINE: (Pg 9) This isn’t a fairy tale . . .

DR. DALITSCH: (Pg 46) . . . the severe pain in your legs, the hard ridge that has formed along the underside of your jaw . . . is a direct result of . . .

CATHERINE: (Pg 9) It’s not a tragedy . . .

DR. DALITSCH: (Pg 47) Did they warn you? Did they protect you?

CATHERINE: (Pg 9) It’s something else . . . (Pg 10) I’m Catherine Donohue. I live in Ottawa, Illinois. I have two children [and] a husband that I love . . . (Pg 11) And we started like this. ******

(Catherine and Tom at home; she’s getting ready for her first day of work)

TOM: (Pg 11-12) Well, aren’t you the prettiest thing?

CATHERINE: Be honest. How do I look? (Strikes a pose) Do I look like a girl worth 8 cents a watch? Who knows, maybe I’ll make more than you someday. (Pg 13) I want to know what it feels like to make eight dollars a week. I want to know. Just once. I want to be that person. For a while. (she struggles to fix the collar of her dress). Tell me I can do this. Tell me I’ll be good enough.

TOM: You can do it. But you won’t be good enough. You’ll be great.

(Catherine’s 1st day of work at the Radium Dial Company)

MR. REED: (Pg 14-16) Morning, girls. I’d like you to meet Catherine Donohue. (as he ushers Catherine to her work station, he addresses another worker) Charlotte? Painting the dials . . . how it’s done.

CHARLOTTE: (demonstrating) Alright. It’s easy. See? You take your little brush here, twirl it between your lips to make a point, then dip it into the powder here. Paying attention?

CATHERINE: (mimicking Charlotte’s actions) Point . . . dip . . . and then you paint. Like this.

(She paints a number, shows Mr. Reed and puts the brush back in between her lips) Why does it shine? (Reacts to the taste) It tastes awful. Is it okay? Getting this stuff in our mouths.

MR. REED: It’s more than okay. [Radium] is medicinal. (Pg 17-18) Think you can do it?

CATHERINE: Oh, I can do it. I’m sure!

CHARLOTTE: She’ll be great, Mr. Reed. (Mr. Reed exits) *******

CATHERINE: (Pg 18) (speaks to the audience) And I was. My twos swooped and dipped. My fives were flawless. And my twelves? (gestures for extraordinary) (Beat) I walked home that night in the dark. Ten years ago, a girl like me couldn’t even vote, let alone make this kind of money. But now? (enters the apartment and removes her coat to greet Tom, who is in the kitchen making dinner) (Pg 23) You beat me home.

TOM: (Pg 18) Your hair! (Catherine touches her hair) It’s shining. Your dress (She touches her dress) Your hands, your eyelashes, your mouth. You glow.

CATHERINE: It’s the dust. From the paint . . . for the watches.

TOM: (Pg 23-24) (Pre-occupied with getting dinner on the table) Your mom just left. The kids didn’t take their nap, so they’re monsters. Hungry monsters. (He sets the table haphazardly) Dinner’s not going to be good . . . I didn’t really know how to. . .

CATHERINE: (Pulling a small box out of her handbag) A little something. To make up for it.

TOM: (Takes the box) For me? Don’t think you can just bribe me with gifts. I’m not that kind of girl. (Opens the box and is wow’d by the gift) Wait. Yeah, I am. (Takes a pocket watch from the box and opens it) Wow. You just bought me off with a pocket watch.

CATHERINE: (Proudly) I painted it. The numbers.

TOM: It’s . . . perfect! *******

CATHERINE: (Pg 32-33) (to audience) When I started, I thought it would only be for a while . . . Six years. (Beat) And like that, time passes. (Long beat) Before we noticed . . .

VOICE OVER: 218,723 watches later . . .
*******
Tom and Catherine’s apartment. Catherine is in the bathroom, washing the radium dust from her
hands and arms. She is in obvious pain as Tom enters

TOM: (Pg 33-35) Katie? I’m home. Helluva day. I drop my lunch off the twenty-second story. I could eat a horse. (Tom enters the bathroom and clicks on the light, Catherine responds negatively, but Tom doesn’t notice) How was work? How many watches you paint today?

(He pats her on the check, again Catherine responds in pain, but Tom doesn’t notice)

CATHERINE: (without any energy to her voice) One seventy-five.

TOM: (continuing in his happy-go-lucky tone) How are the kids? You hungry? You want me to start dinner? You look tired, no offence.

CATHERINE: Tom? Look at me. You see anything different?

TOM: Just my beautiful Katie

CATHERINE: Turn off the light. (he does so and she holds up her hands, showing her palms, then returns to the sink, washing furiously to try to remove the glow)

TOM: It’s just the dust. Like always. It’ll wear off. It’s fine.

CATHERINE: But it’s not just on my skin anymore. It’s in my skin. Tom, it’s in my body. I ache, Tom. My bones. My legs, my back.

TOM: (refusing to see or hear) Maybe this job’s getting too hard for you. Maybe you’re just tired like any working stiff.

CATHERINE: I’m not some little doll, Tom! It’s not too hard for me. There’s something wrong and I don’t know what it is!

TOM: (blows her off) Your hands are dirty! So what? (starts to walk away)

CATHERINE: Don’t you dare walk away from me!

TOM: (losing his temper) Listen, I’m tired too!. If this job’s getting to you, don’t come home and take it out on me, okay?! Every day I’m up there doing the high-wire act, worried that I won’t see you and kids again just because I moved an inch in the wrong direction. I told you the day you started that work is work! So we ache! So we’re tired! That’s what you signed up for, Katie! Remember, you wanted this job. (a beat of quiet)

CATHERINE: I’m telling you. (She experiences a sudden shooting pain in her arm and cries out loud) There’s something wrong with me. And I. Am. Scared.

TOM: (Pg 39-40) Maybe it’s the cold, the damp.

CATHERINE: (Still doubled over in obvious pain) You know what would be great? If you’d actually believe me instead of making excuses. There’s something wrong. It’s not the weather. I’m not working too hard. God, I’m so tired. ******* Mr. Reed’s office at Radium Dial

MR. REED: (Pg 44-45) Ah, Mrs. Donohue. Come in, come in.

CATHERINE: You wanted to see me?

MR. REED: You’re missing too much work, Mrs. Donohue . . . I have to let you go.

CATHERINE: What? No! Only a few days. Not that many. No more, I promise, no more. Just let me –

MR. REED: (cutting her off) This is a good place for girls. For healthy girls. I’m sorry.

CATHERINE: You’re really firing me? For being sick?

MR. REED: I remember the day you started, Katie. You fit right in. And you didn’t rock the boat. I suggest you don’t start now. I’m sorry you got sick. I’m sorry I have to let you go. It’s my job. It’s business, you know.

CATHERINE: No, it’s not. It’s a crime! *******

CATHERINE: (Pg 42) My bones [were] breaking . . . I couldn’t lift my little girl. I could barely cross the room. (Pg 46-47) No doctors in our town would see us. So we had to go to the city. (Scene shifts to the doctor’s office)

DR. DALITSCH: Catherine . . . the fainting spells and destruction of your teeth [is] connected to the malignancy of your hip and necrosis of your jaw (Sees that she doesn’t understand this word) Necrosis means . . . localized death of living tissue. To the best of my knowledge this is a direct result of radium poisoning. (Catherine breaks down into tears)

CATHERINE: (pulling herself together) Tell me . . . is Radium poisoning . . .

DR. DALITSCH: Terminal. *******

CATHERINE: (Pg 50) (alone on stage. The sound of a ticking watch in the background. As she speaks to the audience, she has more and more trouble moving her jaw, we see her physically deteriorate in pain) This is the sound of a mother’s heart breaking. (Long pause) This is the sound of her falling apart. (Long pause) This is the sound of time (beat) running out. (Long pause) I am going to die. (beat) (Pg 62) I’m not afraid of death. Really, I’m not. (Long pause) I’m just afraid of how I’ll get there. . . (Long pause)

(to audience) (Pg 52-53) Women like me don’t stir up trouble. We play nice and do what we’re told. (With strong conviction) [But] a big part of me wonders what it would feel like to hire the best lawyer I could find and go get / those sons of . . . [So we did] (Pg 56-57) (to audience) Our case went to court. Our story went to press. And the press went to town.

(through each of the reporter’s statements, the audience can see Catherine wither away)

REPORTER 1: A travesty is unfolding just outside of Chicago, where several disgruntled women are accusing a beloved company of foul play . . .

REPORTER 2: . . . allege that Radium Dial knowingly compromised their health, safety and lives.

REPORTER 1: . . . fired for poor performance.

REPORTER 2: . . . Radium Dial is known for paying generous wages to unskilled workers.

REPORTER 1: . . . . in spite of community pressure to step aside.

REPORTER 2: . . . grasping for a payday.

CATHERINE: (Pg 65) I won my case six times. The Radium Dial Company appealed six times. After losing all six, the company appealed to the United States Supreme Court . . .

REPORTER 1: (Pg 62) Mrs. Donohue came to the hearing today supported by her husband. Once healthy and alert, she weighted only 71 pounds and could hardly stand alone. . . .

TOM: (to audience) (Pg 65) She died 21 days later – [NOTE: This first line is spoken by one of Catherine’s co-workers (Pearl) in the original script – could be presented as a voice over before Tom speaks] (He takes out the pocket watch Catherine gave him, winds it slowly, looks at it for a moment, then speaks) (Pg 64) Do you know they pulled bones out of her body while she was still alive . . . Lifted them right out. (He starts to cry) Could you tell me what I’m going to do with all this goddamn time? (He caresses the watch and puts it back in his pocket.)

CATHERINE: (we hear the ticking of a clock, the ticking becomes a heartbeat . . then it stops. Silence, then Catherine speaks) (Pg 10) They say you see a light But you don’t. You see your life flash before your eyes. You see your story. Beginning . .

TOM: (Pg 11-12) Well, aren’t you the prettiest thing?

CATHERINE: (Pg 10) and middle . . .

TOM: (Pg 35) (angry) I told you the day you started that work is work! So we ache! So we’re tired! That’s what you signed up for, Katie! Remember, you wanted this job.

CATHERINE: (Pg 10) And the end . . .

TOM: (Pg 50) (Taking her hand, he speaks emotionally) No one on earth can hold a candle to you . . . No one in heaven will come close.

CATHERINE: (Pg 66- 67) And time stood still for just a minute, just for us . . . and we were (beat) shining.
```

---

## IC-0279: The Thief of Tears

- Title: The Thief of Tears
- Author (byline): Jeffrey Hatcher
- Work: Three Viewings
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARLIE, MAC, GRANDMA, MOURNER, DAD, JACK, MORTON
- Teaser before the introduction: Yes
- Spoken words (computed): 1578
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jeffrey Hatcher
Book: Three Viewings
ISBN: 978-0822214946
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Meet Mac -- a coffin robber, a pretend mourner who can bend down to kiss the deceased goodbye and stand up with two ruby earrings in her closed mouth. Today she is at the wake of her own grandmother with more than mourning in mind. See, Grandma has a ring . . . but coming home again may be more than Mac bargained for. Thief of Tears by Jeffrey Hatcher
```

### Performance text (classify this)

```text
Lights up on Mac, an attractive woman between the ages of 35 and 45. Mac wears black. Lots of sparkling rings on her fingers.

CHARLIE: (Pg 32) (we pick up in the middle of a imagined talk show) How'd ya' get your start in - well - I guess we'd have to call it – heck . . . corpse-robbing, right?

MAC: Right you are, Charlie. Weel, it was like this: I had just moved from Stockbridge to L.A., I was broke. A friend of mine died, a bad death. I hadn't been to a funeral in a long time, and they'd put me in charge of accessorizing him for the viewing, but his wrists were so small, his watch wouldn't fit, so I put it in my purse. It wasn't until three days after the funeral that I realized I still had the watch. I was gonna give it back ... but it was a Rolex in a rough week. And anyway give it back to whom? So I rationalized keeping the watch ... then selling it ... then finding ways to do it again. It's kept me in high five figures for eight years now. Never caught, knock on wood.

CHARLIE: But gosh is there anything you won't steal?

MAC: Sure. A wedding ring. A friendship ring. A decoder ring. There are limits. (Beat – to audience) (Pg 34) Let me go back. (Pg 31) Thomas Wolfe once wrote: “You can't go home again." (Beat.) Thomas Wolfe was a putz, of course you can go home again, they make you go home, all the time - endlessly . But this time is different. I'm going to get something from this trip. (Beat) (Pg 30) [So . . . ] She's dead. My grandmother, Nettie James is dead. This is my moment. My destiny has called me. (Pg 29) I've been stealing jewelry off corpses for years, Grandma'll be a cinch.

MAC: (Pg 33) I arrive over the river and through the woods to grandmother's funeral. Inside the parlor, the first viewing has begun. (Pg 34-38) They're all acting - well - they're acting as if someone has died. Nettie James was 103 years old. This funeral has been in rehearsal so long it's had replacement casts. (Pause) Let me go back. (takes photo from her purse) In the photograph I've brought with me from L.A. a beautifully coiffed woman in her sixties holds the hand of an equally beautifully-coiffed five-year-old girl with red eyes from crying. It's 1963, and I'm not going to go to the beauty parlor. I'm screaming in the back of the big blue Packard, and my grandmother has decided to calm me down by taking me into the big department store, The Hub. She holds my hand, and when we enter, hundreds of shop clerks rush to greet us, bending, grovelling, rubbing their hands. They give her presents. Something especially important seems to come from Morton Lincoff from jewelry – something wrapped in a box.

GRANDMA: You see? If you're nice to people, they'll give you things. Tell you what: you be a good girl today when you get your hair done, and Nettie’ll give you what's in this box.

MAC: And she opens it. Inside is a beautiful tear-shaped ring. It seems to sparkle with every jewel in the planet. I've never seen such color, so many facets, such light. I will do anything to get this ring. So I am a good girl, and I do calm down, and I get my hair done. And when it's all over, and we're back at Norton Place, I ask my grandmother, "So where's my present?" And Nettie says

GRANDMA: Oh, that was just something I said. You can't always get what you want.

MAC: And the ring goes on her finger. Let me go back. . . The family returns to the parlor where the second viewing has begun. The crowd around the coffin has gone on a coffee break, so I make a bee-line for the casket. I peer in at my grandmother. A voice nearby murmurs:

MOURNER: She looks good.

MAC: I nod. (She looks like Stalin.) Her hands are folded, touching, one over the other. She always wore the dinner ring on her right hand, aaannnd ... that's the hand I cannot see. How am I going to find out if she's wearing that ring?

DAD: Mac, we have a problem. Nettie's new will left instructions specifying certain pieces of jewelry she wanted to be buried with. The funeral home won't take responsibility for the pieces overnight. Their policy is to have the family do the physical removal from the body and keep the jewels at home until morning. Now, your mother is in no state to do it. We'd like you to do it, Mac. (Beat.)

MAC: (falsely) Oh. I couldn't. (strategically reconsiders) All right, sure. (She looks at the audience as if to say "This is where you came in.” and speaks to audience) I've been stealing jewelry off corpses for years, Grandma'll be a cinch. I go to my grandmother. I remove the jewelry. I very deftly flip her left hand off her right. There is no tear-shaped dinner ring. Her fingers are bare. I pat her down like a cop at the airport. It's not there. Nothing. (Pause) In a daze, I go back to Norton Place very alone. I'm in the pink room of my grandmother's home, in the pink bed that's been mine since I was a child.

In the darkness, I dream of Jack. Jack in our house in Stockbridge, holding hands with Paul and Lainie at his side. (Pg 34) Let me go back.

JACK: (Pg 38) Why can't you love the littlest things? The things you can hold in your hand. What do you want from this world?

MAC: There are so many things you can't get or hold on to. Like color, and facets, and light. And then - in the dream - Jack takes my hand ... and says:

JACK: Is that why you tried to kill yourself? (Pause.)

MAC: Yes. I left our bed and I went into the garage, and I sat in the car in the cold, cold night and turned on the ignition. I tried. Didn't work out the way I'd planned. (Pause.) (Pg 34) Let me go back. (Pg 38) The next morning ... I call the airport to get the soonest possible flight back to L.A. My bags are in the BMW outside the funeral home. Inside ... I'm at my post for the third and final viewing ... I notice a tiny bald man. It's Morton Lincoff from The Hub! He's ancient now - like Yoda. And he says to me:

MORTON: Where is that husband and those two kids?

MAC: (Pg 39) (at if by rote) I am not married now. My husband never fixed the kitchen door.

MORTON: (puzzled, but continues) You know, I remember you coming into the store with your grandmother - must have been thirty years ago - the day you were going to get your first hair done .. Your grandmother had come in to pick up a ring your grandfather had me design. Beautiful thing. The one she's wearing right now."

MAC: You mean the, the tear-shaped ring?

MORTON: Yes! Your grandmother had sent it in to be cleaned before she died. I just give it back to Mister Funeral. Your grandmother, she wanted she should be buried with it, and who are we to argue with the dead?

MAC: It's there. It's there. Why shouldn't I take it? It was, by rights - it was by rights . . . mine. And I need - I want - (Pg 34) (shakes off her thoughts) Let me go back. (Pg 39-40) The service is about to begin. The family is to pay its last tributes. One by one. (Pause) It's worked for me a billion times, it'll work for me again. No one dare stop the emotional grand-daughter from her final embrace. I grip the side of the casket. I lean my face to hers. I kiss her cheek - and place my hand upon her hand. Her ring is harder to remove than I had hoped, as if the finger's swelled. I pull. Nothing. I twist. Nothing. I do not want to break her finger. It is an occupational hazard, and I don't want my grandmother to be my first "snapper." And then I look down. Because Nettie's eyes - my grandmother's eyes - are wide open and watching me.

MAC: Grandma?

GRANDMA: Why have you been lying to my old friends about that family of yours? Tell Grandma where that husband of yours is and my two great-grandchildren.

MAC: (Pg 34) Let me go back. (Pg 40) I look for my family - my family! - and there's no one in the room! (shouting) My husband never fixed the kitchen door! . . . . (long pause, the quietly to the audience) (Pg 41) And after I fell asleep in the garage, I finally woke up at the hospital in Stockbridge and I asked where is my husband, where is my daughter, where is my son ... they explained to me ... that because the kitchen was attached to the garage, and because the kitchen door had never been fixed, the door had opened, and the air from the garage had drifted into the house and into the bedrooms and my family - my husband, my children, my littlest things ... it had killed my family ... while I slept. (begins working on the ring again)

Let me go back. Let me go back! Let me go back! And the ring comes offl

(Beat.)

MAC: I did not die the day I tried to kill myself. They buried my family before I had a chance to touch them, hold their hands one more time. Jack's wedding ring. Lainie's friendship ring. Paul's decoder ring. But I am alive, and my grandmother's ring is cold to my touch. It is not what I want or need. (Pg 42) (Pause. Mac kneels and begins to remove her rings, until by the end, of the next speech, she looks like a mourner from the old country, dressed in black.)

In Stockbridge, Massachusetts, where I lived for years, there is a place where my other family is buried. I have not yet visited them. But I know the way there. (long pause) Tears freeze in the cold. When they hit the stone they break into a shattering of colors and facets and light. I gather them close to me, and I am warm like a thief in the night. (Slow fade end of play.)
```

---

## IC-0280: This is My Audition Monologue

- Title: This is My Audition Monologue
- Author (byline): Sara Zarr
- Work: Geektastic: Stories from the Nerd Herd, Pg 319-328
- Publisher: Little, Brown Books
- Publication date as stated: June 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: RACHEL
- Teaser before the introduction: Yes
- Spoken words (computed): 1533
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sara Zarr
Book: Geektastic: Stories from the Nerd Herd,
Pg 319-328
ISBN: 978-0316008105
Publisher: Little, Brown Books
Date (Month/Year): June 2010
```

### Introduction (context only: never use it for content warnings)

```text
This is My Audition Monologue by Sara Zarr
```

### Performance text (classify this)

```text
RACHEL: (Pg 319-328) I wrote it. (beat) I know we’re supposed to pick something from a (airquotes) quote-unquote known work by Shakespeare or Chekhov, or one of those monologues in the drama room, but I looked at them and honestly there’s nothing that shows my range or says anything about who I am that will be memorable. And that’s what I need: to be memorable. Because, and I’m not trying to embarrass you, but you’ve had trouble remembering my name since I started auditioning freshman year. So obviously I need to take a new approach.

Look at the audition form and look at my face: Rachel Banks. Not Rochelle, not Ruthie, not Melissa -- I really don’t understand where you got that last one, but you have called me Melissa at least three times. So, my goal here is to be memorable. [So] . . .

RACHEL: You can start timing me . . . now. (deep breath) Scotty King got electrocuted while running the light board. It sounds like a joke, I know, but I’m saying that he got electrocuted. While running the light board. I’m saying that he died, during the second act of Miracle Worker when Julie-Ann Leskowitz had gotten so good at playing blind, deaf, and dumb that she didn’t stop her scene, even though the lights flashed and everyone heard the sizzling noise from up in the booth and Annie Sullivan stopped and said, “Oh my God, Scotty,” because she knew about the leak in the auditorium roof and Scotty’s belief that bare feet were good luck and we were having one of those late spring storms and there were puddles and drips everywhere, and she put it all together faster than any of us. And we stopped the show and people filed out, a lot of them not realizing what had happened and asking if they’d get a refund. Seriously, who asks for a refund for a seven-dollar high school play? I’m sorry, I’m still making it sound like a joke. You don’t know this about me, since you’ve never taken the time to know anything about me, but I use humor that way. It relieves the tension. Unless someone is actually dead, like Scotty, in which case it just ends up sounding sick and insensitive.

You know all this, of course, you were there. What you may not realize is that it was supposed to be me. (beat) Now it doesn’t sound like a joke. Now it sounds like I’m trying to get attention or turn the focus away from Scotty’s tragedy on to me.

If it had been me, would anyone have noticed? One, I’m obviously not memorable. I’ve never gotten a part. I audition every single time, and this is the mistake I’ve made. On the part of the audition form where it says: In the event you are not cast in the play, would you be willing to work behind the scenes on this production? I always put a checkmark in the YES box. Every time I see that question I think to myself:

Rachel, don’t check yes. DO NOT CHECK IT!

What happens is the part of me that would rather mop up Julie-Ann’s sweat or de-crust the greenroom furniture than not have anything to do with the play panics and I check YES. Yes, use me. Yes, abuse me. Yes, make me post call times in my own blood, I will do it. I will do anything, anything to be in the general vicinity of this auditorium every single day, including weekends.

Hence the trying-something-new-and-memorable ploy of writing my own audition, hoping it will help me relax (and it kind of is, now that I think about it). When I do the lines in my room and no one is watching, I’m so, so good and that isn’t bragging. When I practice in my room, I’m Sarah Bernhardt, I’m Julie Harris, I’m Dame Judi Dench, for real. Then I get in front of you and anyone else who might be in the room, I am so bad. So truly bad. Even I know how bad I am.

When there are lines, I say the wrong ones at the wrong time, in a total monotone, and I don’t know what to do with my hands, and one time I drooled. I was staring at the page with my mouth sort of agape I guess, because I lost my place, and this string of drool, sparkling in the stage lights, oozed right out.

This is why I check the YES box [and] how I ended up running lights. When I hand-picked Scotty to be my lighting assistant, my intent was not to kill. Originally, he wasn’t supposed to be running the board at all. Originally, he would have been my errand boy, my cue keeper, my clipboard peon. [But] I didn’t want to do lights. What I wanted was to be onstage; but since that didn’t happen, I hoped that while Scotty took care of things, I could spend a little more time with the actors and soak up some of their actory personalities.

Ever since I checked my first YES box, I’ve been stuck in this limbo between techie and performer. Unlike the techies, I do not own seventeen different black T-shirts. I do not spend my weekends scouring yard sales for the perfect Agatha Christie ashtray or Oscar Wilde table lamp. At the same time, I know I’ll never be one of those sparkling, chosen, beautiful oddballs that have “The Second I Turn Eighteen I’m Moving to New York” written all over them. I think too hard before I talk. I haven’t considered how I look from all angles. I can’t break into songs from Spring Awakening at the drop of a wool stocking. I have never dared to wear an item of clothing that strays from my jeans-and-cardigan comfort zone.

Which is why I put Scotty on the board and tried to spend a little more time with the Chosen. I thought if I want to be an actor so bad maybe I could at least try to act like an actor acts. Fake it ’til you make it. Most people do not look at Rachel Banks and think: Drama Nerd. Most people do not look at Rachel Banks and remember that Rachel Banks is her name.

The funny thing is I thought drama would be a place where being not like the others was okay, but it turns out you have to be not like the others in a way that is exactly like the others who are not like the others.

This is why I’m not doing that stupid piece from Butterflies Are Free for my audition and instead am trying to tell you who I am because let me assure you, I will never be one of them. Not in the way you expect me to. For one thing I don’t have that thing, that instinct that tells me about vintage tube tops and asymmetrical hair. But I know that doesn’t matter, that someday some director, some boy, some anybody, will like me plain and in my cardigan and not be blind to me just because I’m not aggressively DIFFERENT.

If I do this, if I leave this school and go on to study theater or go on auditions out in the real world and start getting parts, it’s not going to be because I am oh so delightfully quirky and wear unmatched shoes and tiaras around town. It’s going to be because I love it, and because I have paid my dues and been willing to check that YES box every time if only so that I can watch and learn and get out of here and finally become the real Rachel who will then go out and claim the parts that are out there waiting for me. I have what the rest of these girls do not. Passion.

Some might say I shirked my responsibilities by putting Scotty on the board at the last minute. But I figured since you don’t remember my name you wouldn’t really care if it were me or Scotty or the Queen of Sheba actually running the board, while the other one of us stayed backstage on the headset.

I know it wasn’t my fault. I know I don’t have any real responsibility for Scotty’s death, that it was a freak accident. And I also can’t help but think Scotty’s death was a sign, someone up there telling me:

• Stop checking the YES box. • Stop being willing to stay behind the scenes when what you want is to be in the scenes.

I’ve only got one more year and I’ve proved my dedication. The fact that I’m even here auditioning after what happened proves that I know the basic truth of plays and life: The show must go on. Even when it’s hard to watch the show going on without you.

I’ll take any part, I will; and if it’s Onlooker #8, I will be the best Onlooker #8 this town has ever seen. But if you can’t find a part for me, I’m going to walk away. I’m not going to hang around in the shadows anymore. This time you’ll remember my name.
```
