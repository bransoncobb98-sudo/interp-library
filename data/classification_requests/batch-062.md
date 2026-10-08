# Classification request: batch 62 of 63 (40 records, IC-2441 to IC-2480)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-062-reply.json`.

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

## IC-2441: The Junkie and the Monk

- Title: The Junkie and the Monk
- Author (byline): Mike DeStefano
- Work: The Moth Presents Occasional Magic, Pg 224-231
- Publisher: Crown
- Publication date as stated: Mar 2019
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MIKE
- Teaser before the introduction: Yes
- Spoken words (computed): 1440
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mike DeStefano
Book: The Moth Presents Occasional Magic, Pg 224-231
ISBN: 978-1101904428
Publisher: Crown
Date (Month/Year): Mar 2019
```

### Introduction (context only: never use it for content warnings)

```text
On March 6, 2011, former heroin addict and stand-up comedian, Mike DeStefano died of a heart attack. He was 44 years old. Two years before his death, he recorded this heart-felt narrative for The Moth.

And although DeStefano masked his pain with comedy, the people closest knew him as a loving son and a man who healed souls as a drug and HIV/AIDS counselor. After all, it is our trials and tribulations that make us who we are.

The Junkie and the Monk by Mike DeStefano
```

### Performance text (classify this)

```text
MIKE: When I was a kid, I had a spark in me. I was happy. I always had a little bit of a flame going, and nothing could really knock it out. I went to Catholic school, but even the nuns couldn't extinguish the flame that dwelled inside me. (They tried.)

MIKE: At the time of this story, I was twenty-eight years old. I was in the Winn-Dixie supermarket shopping when this weird feeling came over me, and then I fainted, I blacked out. That had happened to

me before, but it was on purpose, with drugs. This time it was a little scary. I was in and out of consciousness. I knew something was wrong.

I ended up in the Palm Beach Gardens Medical Center. I had a tube in my nose, and I was in this in-credible pain. It turned out I had double-lobal pneumonia. And for a minute I was really concerned about myself. This was weird. I hadn't worried about myself for a few years, because at home my wife was dying of AIDS, and she was really sick.

All I could think was, I've gotta get out of this hospital.

I've gotta get home and take care of her. Because all I did was take care of my wife; that was my life, my job. And it wasn't a problem, I loved it.

So I was lying there, and the phone rang. It was my friend Jimmy, and he said, “Mike, Frannie was in a car accident. Car flipped five times on 1-95.”

No. She can't even walk. She's on so much mor-phine, there's no way. And, yet, I believed it, because I knew her. We were reformed drug addicts, recovering people. So even though she was suffering with AIDS, the morphine helped her feel better, and she probably just thought, Hey, I can drive.

I knew she was dead, so I laid back, and I was just like, Wow. Because, quite honestly, my life -- the drugs and the tragedy and people dying that I loved, and most of all, my wife being so sick after being off drugs for so long -- it just seemed really unfair. ***** All I knew about God was the one that I was told about as a kid, you know, God's watching. He knows. So I figured that the god who's doing this to me and my wife, I'm not gonna pray to him, you know? What am I gonna say? Can you help me? No. I'm gonna say, What are you doing? Get off the fence. Make a move. Kill us or help us. Do something.

That wasn't really working for me, so I went to this Buddhist place, because I saw an ad in the paper. I thought, I'm gonna go see. So I walk in, and they told me to take my shoes off. They were very sweet and kind, and they had a lot of compassion. This woman said, "Would you like to see the lama?"

I'm thinking it's an animal they've got somewhere, like a sheep type of thing, so I said, "What's a llama?" She said, "No, it's a Tibetan priest."

When she said the word "priest," I immediately thought of, you know, a scary Catholic priest . . . So I walk in there to meet this guy. He's a little man, and he's just sitting there, mumbling a chant, and I'm like, What's he doing? And she says: “He just prays and meditates. He's been doing that since he escaped Tibet with his family. He does this for twenty-some-odd hours a day. Come sit near him.”

I don't know about anyone else, but as a kid if I was in church kneeling and my knees didn't hurt, I was in trouble. Your knees had to hurt in order to be really praying right. So I actually got on my knees, like a good Catholic, and she goes, "No, relax, relax."

I put my hands out, and he took my hands. And when he touched me, I felt so relaxed. I wasn't scared. All the pain went away. I went there every day for a few weeks, meditating and praying. ***** Now I'm in the hospital, waiting for my friend to call me back with more news about my wife's accident. But I've got these Tibetan beads, and I'm thinking of this man, and I'm okay. He blessed these beads for me.

And the phone rings again. But it's not my friend, it's my mother, and she says, “Daddy has a brain tumor." Yeah, this was a bad day. This news just froze me. I took the beads, and I threw them. I was like, You know what? I've been a Christian, Catholic, angry person for twenty-seven years, and now I'm a Buddhist for like three weeks. I don't want that little bit of peace, man. It just makes the rest of life seem so much *worse*.

The phone rings again, so now I'm like, Okay, they are going to tell me my wife's dead. And it was Jimmy, but he said, "Mike, Frannie's okay. Relax."

She had actually been taken to the same hospital I was in, so I had to go visit her down in the emergency room. Will you give me a break here? My dad has a brain tumor, and I'm going to visit my dying wife down in the ER. She didn't die from flipping over the car, but she's gonna die soon anyway. I'm gonna go visit her now, and I've got pneumonia.

A couple of weeks went by, and she ended up in hospice. Young people don't like to die, you know? Not that old people do, but some old people can say, I had a good life. She didn't feel that way. She was pissed. She didn't wanna die. She was thrown out of hospice for not dying. This happened three times. But finally, this time, she died. I froze. I knew my father was now going to die, too, and I loved my father. We were so close.

Nine months after my wife died, I was out at a movie. I came home, and there was a voice mail from my brother, "Mike, pick up the phone. Mike, pick up the phone." Every time I heard him say "Pick up the phone," I felt a little more fear of what he was going to say. Finally he said, "Daddy's gone."

I'll never forget where I was. I was standing in front of my laundry machines, listening. And I felt my heart get ripped outta me. And that was it. The flame that I had as a kid -- all of it -- was gone, because now everyone had died.

I made arrangements to fly home the next day, and when I got on the plane, I decided that I was going to end my life. I was done. I wasn't telling anyone. It wasn't a threat, it was a decision that I'd had enough of this. There was nothing else to live for. I couldn't wait until the funeral was over, because that was when I was going to do it. I wasn't going to jump off a building or jump in front of a car. People haven't heard of overdosing on drugs?

But all my life God or the universe, or whoever’s running this thing, would always go, Yeah, it's really awful now. You're almost out of hope. But here's a little something nice to keep you going.

So . . . I went to the back of the plane to go to the bathroom. And the lama, the monk that I had met, is sitting in the back row. He sees me, and he put his hands out like he did before. What he was doing is called tonglen *. You have to have amazing karma, they say, to have a lama actually want to do tonglen with you. What they are doing is saying, Give me all your pain, and I'm gonna give you all my joy.

The reason he sat for thirty years in meditation was to open his heart so much that it gets as big as the ocean, so that if you pour some of your pain into it, it absorbs it. That's what his whole life was about. And it worked for me . . . I got home and I've got these Tibetan beads, and I'm thinking of this man, and I'm okay . . . He blessed these beads for me.

*Tonglen: an ancient Buddhist practice to awaken compassion. With each in-breath, we take in others’ pain. With each out-breath, we send them relief.
```

---

## IC-2442: Kidneys and Commitments

- Title: Kidneys and Commitments
- Author (byline): Gil Reyes
- Work: The Moth Presents All These Wonders, Pg 301-305
- Publisher: Crown/Archetype
- Publication date as stated: March 2017
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1361
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gil Reyes
Book: The Moth Presents All These Wonders, Pg 301-305
ISBN: 978-1101904404
Publisher: Crown/Archetype
Date (Month/Year): March 2017
```

### Introduction (context only: never use it for content warnings)

```text
Let’s talk statistics for a minute. According to Donate Life America, currently more than 90,000 people are on the national kidney transplant waiting list. Every 10 minutes, another person is added. That means these seriously ill individuals are . . .

1. Waiting for person with a healthy kidney to die

2. Hoping the deceased has agreed in advance to

donate their organs

3. Praying that the organ is a biological match

4. Undergoing costly dialysis 3 times a week;4 hours a

day just to stay alive.

But even though the process of live donor transplants was widely accepted in the 1950s . . . in 2021, 6,000 people in the US died while on the waiting list. If you want to become a living donor, contact a transplant center near you for an initial evaluation. You can save a life.

Kidneys and Commitment by Gil Reyes
```

### Performance text (classify this)

```text
(Pg 301-305) I'm sure the woman on the other end of the phone identified herself as being from the clinic I'd been to the day before. Maybe she said her name. Maybe she asked if I was sitting down. But I don't remember any of that. In my memory I just pick up the phone, and this voice says, "Go immediately to the emergency room. Your kidneys are failing."

And as I get up and get dressed, there's this voice in the back of my head saying, This is absurd. I'm in my twenties. I'm invincible. I'm immortal. I don't even need health insurance. . . I don't even have health insurance.

Sure, I'd been feeling bad for a while. But my swollen ankles, those were because I was waiting tables, working double shifts, trying to save up money, not because my body wasn't processing water waste, right? And those splitting headaches, those were because I was really stressed out, trying to get into grad schools, and not because your kidneys regulate your blood pressure.

When I had finally collapsed a few days before, I didn't have any more excuses. That was when my boyfriend, Sean, made me go to the clinic. Sean and I had been dating for a year and living together for a few months. It was moving a little bit fast, but either of us could go to grad school at any minute, so it was fine. We had sort of a day-by-day mentality. We were keeping each other just at arm's length.

In fact, I was able to convince him not to go with me to the emergency room. I mean, why should we both sit around all day waiting for some doctors to tell me that that's not what it is? That it's something else-something that can be fixed with a pill?

So, I went. Alone. Terrified, but hiding it well. And this trait of mine, this sort of crazy independence, maybe it stems from when I came out to my Southern Baptist mother from Alabama and my Catholic Hispanic dad from Texas, when I was a teenager growing up in Kentucky. If you're thinking this didn't go well, you're right . . . There were Bibles manifesting from nowhere (even though I'd been to church more than they had throughout my life). There was screaming and yelling, and I left that night thinking, I'm one of the damned. Because they told me, "You're going to hell."

We didn't speak for a while-over a year. And when we began to try to put our relationship back together, the damage was pretty done. How close can you get when there's this whole part of your life that somebody wants nothing to do with? I remember once, out of the blue, my dad, said, "I never want to meet anyone you're seeing. I don't ever want you to bring anybody home."

But as my emergency-room visit became a ten-day stay in the hospital, I had to let a lot of people know where I was. In fact, that hospital room was where my parents first met Sean. I learned my kidneys were functioning at less than 10 percent. I learned that I would probably have to go on dialysis.

If you don't know much about dialysis, it's a way to live. It's not a great way to live. It's not pleasant. It's very time-consuming. It's expensive. No, what you want in this situation is a living donor, a kidney donor. You could get on the national transplant list. That is going to take time, maybe years, waiting with a bag packed by the door. And cadaver kidneys have other issues; they're not the best choice. If you can get a living donor, though, usually family-somebody who's a perfect match-that's the ideal situation.

Well, my relationship with my parents had left me a little bit wounded. I had trouble trusting people. This is one of the things I was bad at in my twenties. It used to be at the top of the list. Now the top of the list was kidney function. But the not trusting people was still up there. I had this trouble with accepting help. And if you have trouble accepting help, imagine trying to accept a kidney.

People stepped up to get tested. My dad, despite our differences. My mother wasn't eligible. My best friend, his dad. Friends from college, high school, work. But there was one more person who really wanted to get tested: Sean. Talk about a commitment. He eventually wore me down.

He said, "You know, whatever happens, whether or not we're together in the future-if I can do this for you now, I want to."

As the months began to pass, and I did go on dialysis, and my father was disqualified as a donor because of kidney stones, I went on Social Security and food stamps because I was too weak to work. Friends were disqualified for various reasons.

I wasn't going to be going to grad school. I spent a lot of time thinking about how I was going from twenty to eighty overnight. Comparing blood-pressure medicines with my grandmother. I spent a lot of time alone, sleeping, mostly. But I remember this one day where I made it out to the park, and I was sitting alone. It was a cool day, a fall day. I was praying, meditating, considering this entire process. And I found this really strange peace that's hard to describe.

I found this kind of acceptance of myself, and where I'd been, and I thought, You know, it's fine. If this is what it is, if this is it, I'm okay with that. I can die in my twenties. I stopped praying to get better, and I thought about the thing that I'd want. If I could pray for one thing, it was to feel worthy of that love that I hadn't felt for so long. I stopped asking for time, and thought about time well spent.

It was December when Sean called me from work and said, "I have an early Christmas present for you." He was as good a match as my dad. He said, "Would you let me give you a kidney?" And I said, "Yes." And we spent time well. Sean's a big language geek, so we named it: Renee, after the renal system, and Renatus, for rebirth.

We would tell people, "We're having a kidney!" Our friends convinced us to have a party. We had a kidney shower. (Sean really wanted to register, but I thought that might be going a little far.) Nevertheless, people brought us gifts: pajamas for recovering, and bad movies. (Sean loves bad movies.) And we played games, like "kidney bean bingo" and "pin the kidney on Gil." We got this big red-velvet sheet cake shaped like a kidney. And we wore medical masks, and we cut it together, and fed each other pieces and took lots of pictures.

The day of the surgery came in May, and they had us both on gurneys, ready to go. We're surrounded by Sean's family and my family. My parents are there. And my mother starts crying. We never talk about this, but we cry the same way. We scrunch up our cheeks in the same way, and we hold back those tears. I can see it in her face when she's trying to work something out.

She leans down and takes Sean's hand and says, "Thank you." I think she's seeing him differently, and maybe she's seeing me differently.

The surgery goes great, and we recovered together for weeks and weeks in a strange little honeymoon . . . A year later we get a card in the mail. Now, it's not unusual for my mother to send cards. (She sends cards for the strangest occasions, even though they live fifteen minutes away.) But this one was addressed to Sean. It said what a blessing he is. And it recognized our anniversary. They asked us to go to dinner with them, like couples do with their parents.

And I never asked for any proof, because you're supposed to rely on faith, but I have a family where I have parents and a partner-a perfect match-where before I had a boyfriend. And a ten-inch scar across my abdomen to remind me every day that I am loved.
```

---

## IC-2443: Kissing Lessons

- Title: Kissing Lessons
- Author (byline): Joseph Weisberg
- Work: Sixteen: Stories About That Sweet and Bitter Birthday
- Publisher: Random House, Inc.
- Publication date as stated: 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1824
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joseph Weisberg
Book: Sixteen: Stories About That Sweet and Bitter
Birthday
ISBN: 978-1400052707
Publisher: Random House, Inc.
Date (Month/Year): 2004
```

### Introduction (context only: never use it for content warnings)

```text
OK – I’ll let you in on a secret, but you can’t tell anybody! It’s not just girls who feel awkward during their teen-age years – guys have confidence issues too. I know, I know, we don’t show it and we don’t talk about it and we posture a lot; but being a teen-ager is HARD! Especially when it comes to relating to girls. Let me tell you a story . . a confession really . . . I’ll call it . . . Kissing Lessons by Joseph Weisberg
```

### Performance text (classify this)

```text
The summer after seventh grade, I went to the Busby Berkeley Camp for the Performing Arts in Pinewood, Wisconsin. I went there because I liked to tap-dance. I liked to tap-dance because I had no friends, and when you have no friends, you gravitate naturally towards hobbies and interests which ensure that you will never have any friends.

The boys at Busby Berkeley were misshapen, bewildered, and talented. Beefo Kellner was tall and blubbery, spent most of his free time in his bunk clipping his toenails, and had a gorgeous tenor voice. Ed Waxman was squat, cross-eyed, and had numerous facial tics, but completely transformed into a sexy Brando-esque actor the moment he stepped onstage. Greg French had red hair gurgling up from his head like lava, never said a word to anyone, and tap-danced with grace and total abandon. The rest of us were hapless variations on these same themes.

The girls at camp were as perfect and put together as the boys were clunky and poorly assembled. Their hair was curled into loose ringlets that tumbled down to their shoulder blades, or blow-dried into lightly feathered Dorothy Hamill bowls. They wore diamond earrings and makeup with blue jeans. All of them came from the suburbs of Chicago-and they seemed more open and sexual than the city girls I was used to. They made no secret of the fact that boys were the center of their universe. And they flirted constantly. At home, nobody ever flirted with me, and now girls were winking at me from across rooms, giggling while they talked to me, hugging me. I felt like someone who's been raised by a colony of apes, then returns to civilization and suddenly finds himself surrounded by the species he is truly meant to love.

Our show that summer was How to Succeed in. Business Without Really Trying. I was cast as J. Pierpont Finch. My big number was a college fight song called "Stand Old Ivy" that J. Pierpont sings with his boss. After the song, I had to go over and kiss Rosemary, the leading lady.

Rosemary was being played by Suzi Tefler, the most beautiful, most popular, and tallest girl at camp. She was a foot taller than me. The idea of kissing her filled me with a constant, jittery dread. I had never kissed a girl, and I didn't really know how.

Everyone my age at camp was in the show, so they were all there, most of them sitting in the audience watching. I sang my song. Then I walked over to where Suzi Tefler was standing. I turned my back to the audience, closed my eyes, and moved my face towards her, praying that kissing would result.

I felt her breath. Then the electric tingle in front of her lips.

Then Suzi jumped back and at the top of her lungs yelled, "HE BIT ME!"

The audience burst into a loud, punishing laughter. It went on and on, and every time it seemed like it was dying down, it built up again. I wanted to run off the stage but knew it would be a mistake to surrender whatever tiny piece of ground I had left.

Manon Guastafeste was my best friend at camp that summer. Manon was short and hyperactive and had a big, beautiful nose on a Jewish-Mediterranean face. I had a crush on her, but she was going out that summer with Billy Zane. I accepted that I had no chance with her, and we settled into a friendship.

Manon saw how depressed I was after the biting incident. A few days later, as I was shuffling around the no-man's-land between the boys' and girls' cabins, she came up to me and said, "I've solved your problem."

"What do you mean'?" I said.

"I got Nina Steinberg to agree to give you kissing lessons." Nina Steinberg was our friend. And she was cute. Although the idea of kissing lessons wasn't particularly less terrifying than actual kissing, I said, "Okay."

"She'll meet you at Brigadoon tonight at nine o'clock." Every building at camp was named after an old musical. My cabin that summer was South Pacific. The dining hall was Carousel. And the prop shed was Brigadoon.

That night, I rubbed Old Spice deodorant on my underarms and put on my best T-shirt. I opened the barn doors to Brigadoon ten minutes early. The only light, from a street lamp on the basketball court outside, filtered in through one small window near the ceiling. I sat down on an old foot locker and waited. At nine o'clock, Nina slipped in through the bam doors.

She closed them behind her, then she came and sat down next to me on the trunk.

"Hi," she said.

"Hi."

We sat quietly for a little while.

"So you want to practice kissing?" she said.

"Ummm . . . yeah," I said.

She leaned towards me. I leaned towards her. And in the same instant, our lips were together. Then her lips were pressing and pulling. They were plump. And wet. She went back and forth between my top and bottom lips, taking each one between her lips and squeezing it. After a little while, I started squeezing back.

Then she turned her head sideways and came at me at an angle. She affixed her face to mine and her tongue darted into my mouth. It started moving in and out, this way and that, thick and fast. I lifted my tongue and sort of . . . blocked it. Then I started moving my tongue haphazardly, startled each time it collided with hers. In a place that felt like outer space, I thought, I'm French-kissing! Finally, Nina pulled away.

"Okay," she said. "You're a natural."

"Really'?" I said.

"Yeah, you're good at it."

I didn't believe her, but I was glad she said it. "Thanks," I said.

When I got home at the end of the summer, Manon called and told me her family was moving to Chicago, and she was transferring to New City Day School. We were going to be freshmen together. She shrieked and laughed about how great it was going to be. I was ecstatic, too.

***************

[The first day of school that fall] Manon came in the door. She scanned the entryway, and then her big, beautiful mouth spread wide when she saw me. She ran at me and threw her arms around me, jumping up and down while we hugged. "Oh my God! I can't believe you're here! I can't believe I'm here! I can't believe it! Oh my God! I can't believe this!"

I looked down into Manon's eyes and said, "You can't hang out with me."

"What do you mean '?" she said.

"Nobody likes me here. If you hang out with me, nobody'll like you, either."

"That's ridiculous!"

"No it isn't."

"We're hanging out all the time. You're my best friend."

"We can't."

"We're going to be together all the time."

I shook my head.

“This is crazy," Manon said. "I don't know anybody else. I love you!"

"No," I said.

Then I pointed to a group of popular girls clustered together across the hall. "They're popular," I said. "Go hang out with them."

"No," she said.

"Go."

"No, this is ridiculous."

"Go."

Manon looked up at me. She was crying, and she opened her mouth to say something. Then she turned and left.

I waited in the entryway for a little while, then went in to start high school.

************************

Junior year, I started to fall into people. First Kevin Dorst, who I was in chorus with, invited me out to dinner one night. Then Bill Fritz, who was on the soccer team with me, started sitting next to me in Latin class.

Once Bill and I were friends, becoming friends with the girls in the clique was as effortless and quick as a sponge soaking up water-one moment you were talking in the hall when they arrived en masse, the next you were sitting between them at Sarah's house and watching Days of Our Lives.

Manon had been a member of the clique since I had pointed her to it freshman year. Now we were around each other all the time again. Our friendship regrew from the old root. We went back to talking on the phone for hours. We sat next to each other in class and at lunch, we snuck away from parties for conspiratorial discussions of whatever was on her mind. We were constantly huddled together, talking about love, complaining about school, reminiscing about camp. The only thing we never discussed was our separation. There was an unspoken agreement between us that it hadn't happened.

Near the end of junior year, Manon and I were going to a party together. It was my sixteenth birthday, and I was vaguely entertaining the thought that it might be a surprise party for me. It was around eight o'clock, and we were parked on one of the quiet side streets of Lincoln Park. We were talking for a while before going in, in the way we always talked-her going on and on, me absorbing little bits and pieces of what she said.

At one point, when Manon was saying something I wasn't listening to at all, I saw her eyes narrow and focus in on me. "You know, you're a very confident guy," she said.

I sat up straight, and I looked over, and Manon was still talking. I felt something in my toes, and it started climbing, working its way up my body. A feeling of action. Of one fear breaking against another. I started moving across the seat. As I got closer, Manon turned her head and looked at me, all eyes now. And then I was there, and my lips were on hers. Her lips were there. And then they were gone.

She pressed the back of her head against the car window, went a little bug-eyed, and said, "What are you doing?"

I said, "I don't know. I'm sorry."

We sat there for a few minutes, silent.

Then Manon said, "Well, it's not a big deal." Surprisingly, I believed her.

A few minutes later, we walked into the party. Nobody yelled "Surprise!" There were boxes of pizza, Cokes, and Diet Cokes (which the girls called "Dokes"). After we finished eating, the room went black, and everyone started singing "Happy Birthday." Sarah and Cindy came in carrying a cake. In the dark light of the candles, I saw David's mouth wide open as he hammed up the song. Sarah's eyes locked on me, as if they were searching for something inside me. And Jonah, still eating a piece of pizza, brimming with optimism and joy. I didn't really know why these people had taken me in. But tonight they were singing to me. It didn't feel like love, but it felt like hope.
```

---

## IC-2444: The Kryptonite Kid

- Title: The Kryptonite Kid
- Author (byline): Joseph Torchia
- Work: Not specified
- Publisher: Henry Holt & Co
- Publication date as stated: 1980
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JERRY, MOM, DAD, SISTER MARY JUSTIN, ROBERT, BROTHER, NEIGHBOR GIRL, SISTER MADONNA
- Teaser before the introduction: Yes
- Spoken words (computed): 1320
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joseph Torchia
ISBN: 978-0030577987
Publisher: Henry Holt & Co
Date (Month/Year): 1980
```

### Introduction (context only: never use it for content warnings)

```text
Jerry Chariot’s often escapes his confusing and strict Catholic childhood by immersing himself in Superman comics. The problem is that Jerry believes the Man of Steel is real. After all, if God is real, why can’t Superman be real too?

But when Jerry decides to literally fly away from his troubled family, Sister Mary Justin, and the Catholic religion, he discovers the cost of his misguided devotion, and more surprisingly, how true heroism can come from the most unlikely places.

The Kryptonite Kid by Joseph Torchia
```

### Performance text (classify this)

```text
JERRY: (Pg 8-11) Dear Superman, Last night at supper I decided to tell my mom how Superman might be writing me a letter pretty soon. And my mom said . . .

MOM: There isn't any superman. He's just make believe like Goldilocks and Little Red Riding Hood.

JERRY: And I said that was really DUMB. Little Red Riding Hood is just a story and you're a real person except you're a SUPER person which is even better. That's what I said, you should have heard me. Right in front of my dad and everybody. (yelling to family) THERE IS TOO A SUPERMAN BECAUSE I CAN SEE HIM ON TELEVISION!

My dad pushed the chair back and stood up and I thought he was gonna hit me with the newspaper. Usually he hits me with his hand, but this time he picked up the newspaper, opened it up and put it right in front of me and said, "Who's that?" It was a picture of you, Superman.

DAD: See that? You can read. It says Superman is dead, it says he shot himself in the head." *

JERRY: I tried to read it, but my eyes were all watery and my nose was running, and I knew he was gonna hit me. I knew it. But I didn't care! I told him he was a LIAR and that that was the STUPIDEST thing I ever heard in my life! Nothing can kill Superman except Kryptonite. . . And that's when he hit me.

DAD: That guy on TV is just an actor. There isn't a Superman. There never was and there never will be.

JERRY: (Pg 15-17) Dear Superman, Pretty soon we’re gonna be making our First Holy Confession. We have to learn about sins and how to confess them. The other day, while we was in church, I couldn’t think of very many sins, so I decided to read the latest SUPERMAN #163. I was on page 4 when . . .

SISTER MARY JUSTIN: (whispering really loud) Jerome!

JERRY: I knew I was in for it.

SISTER MARY JUSTIN: (out loud – very loud) SUPERMAN IN CHURCH! IN CHURCH! YOU BETTER PRAY YOU DON’T GET HIT BY A CAR WHEN YOU LEAVE BECAUSE IF YOU DIE YOU’LL GO STRAIGHT TO HELL!

JERRY: She said [it] Like I had committed a Moral Sin which is the worst kind there is. It’s kinda like Green Kryptonite and it means you’re going to Hell. And let me tell you, Superman, Hell is a lot like Krypton on the day it blew up in GIANT SUPERMAN #22, page 10. It’s all hot and red and burning. And you sweat a lot and your skin starts on fire and you want to die but you can’t because you’re already dead.

SISTER MARY JUSTIN: SUPERMAN IN THE HOUSE OF GOD!

JERRY: And she grabbed the comic book and teared it up and threw it in the air. She said she was gonna tell the Principle (sic) and call my mom and dad and I better pray. (Pg 20) So far I have 677 Hail Marys and 12 Our Father Who Art in Heavens. Which is a LOT! (Pg 18) PS: You’re just as good as GOD and so I think it’s OK if you’re in his house. I know you wouldn’t mind if God was in your Fortress of Solitude. I just wanted to tell you in case you felt bad about what Sister Mary Justin said.

(Pg 60-61) Dear Superman, My mom’s got this towel which is REAL old so I figured she won’t miss it. I got a Magic Marker and put an S on the back of it – that stands for Super Jerry. I hope you don’t mind. And . . . And . . . And. . . I usually climb to the second branch [of Old Lady Holbrook’s apple tree] but this time I climbed to the third! I put my hands out in front of me and Robert, (Pg 17) he’s my bestfriend, said . . .

ROBERT: (Pg 61) ARE YOU READY? I’LL COUNT TO 3 OK?

JERRY: And I flew REAL good, Superman. Only I didn’t land too good and that’s why my foot still hurts. I can’t tell mom because she’ll get mad. I wasn’t supposed to be up that high. Especially with a cape on. But you just wait, Superman. I’ll do it. You’ll see. – Getting Super, Jerry (Pg 105-107) Dear Superman, my mom got almost as mad as my dad did. He didn’t even wait till we got in the house. He just held me up in the air and kept hitting and hitting me. Mom was yelling . . .

MOM: STOP IT STOP IT YOU’LL KILL THE BOY!

JERRY: And mom was crying like I was.

DAD: NOW GET IN THE HOUSE!

JERRY: I could hardly even walk. (beat) My mom and dad kept fighting long after I went to bed.

MOM: YOU DON’T HAVE TO BEAT HIM LIKE THAT!

DAD: I’LL DO WHAT I DAMN WELL PLEASE! SHUT UP BEFORE I HIT YOU TOO!

JERRY: And my dad hit her. Real hard. (beat)That’s why I couldn’t sleep. I really hate him, Superman. More than Luthor or The Joker or ANYBODY. If he ever hits my mom again . . .

(Pg 124-125) Dear Superman, I’m gonna fly, Superman, I’m REALLY gonna fly! I’m gonna jump off the roof of my apartment building and then fly all the way to Holy Redeemer Church and get my First Holy Communion in front of everybody. Robert said I should way until AFTER we get Communion and this way if something goes wrong then I’ll go to Heaven for sure. But I want to do it when EVERYBODY’S gonna see me. Boy are they gonna be surprised!

(Pg 128) Dear Superman, Sister Mary Justin was teaching us how to write poems. She told us to go home and write a poem about somebody we love a LOT like our mom or the Pope. (Pg 133) Well, I just got finished and it’s called “TO SUPERMAN” -- Roses are red / Your outfit is blue / I like you better / than Jesus the Jew. Amen (beat)

(Pg 137) Sister Mary Justin hated it so much she said she was gonna ask Father Ponti to say that I can’t get my First Holy Communion until NEXT year because I’m the WORST pupil she ever had in her life. (beat)

(Pg 140) My mom has been crying all afternoon. She’s so ashamed. I never seen her cry like that before – with such sadness. Because of ME. (long silence)

(Pg 156-157) Dear Man of Steel. [Today] I was standing on top of my apartment building and everybody was watching me and I had on my cape and I felt so good, and I felt so beautiful. I was just getting ready to leap in the air, when all of a sudden my mom yelled . . .

MOM: LOOK! UP IN THE SKY!

BROTHER: IT'S A BIRD!

NEIGHBOR GIRL: IT'S A PLANE!

ROBERT: NO -- IT'S SUPERMAN!

JERRY: (Pg 170-171) [Well, really. . .] EVERYBODY down below was running around and screaming and pointing up at me.

MOM: GODDAMNIT, JERRY, GET DOWN HERE!

BROTHER: AWW, HE’S CHICKEN ANYWAY!

JERRY: And I heard my dad’s feet pounding up the steps, climbing up on the roof, rushing toward me. Quickly! Urgently!

MOM: BE CAREFUL! OH MY GOD! MY GOD!

JERRY: And then I jumped, and (Pg 173) I found out I couldn’t fly. (Pg 177-178) I was falling through the air. But somebody was holding me in his arms. At first I thought it was [you] Superman -- that [you] had swooped down and tried to save me. But it wasn't. (beat) It was my dad.

[ When] he realized he couldn't reach me, he leaped. Like Superman. He caught me in mid-air. (Pg 176) He held me in his arms real tight, almost hurting me. He was crying. My dad was crying! (Pg 177-178) And he fell with me, in front of me, saving me from the sidewalk. But not the siren. (long beat) [When] I woke up, Sister Madonna was standing there, crying. Looking at me. Praying.

SISTER MADONNA: God forgive him. God forgive this child, this child.

JERRY: She was like a guardian angel. I wanted to tell her that I didn't hurt, that I was numb, I couldn’t feel anything. But words wouldn’t come out. I felt like somebody was sitting on my throat. I heard her (Pg 159) whisper to somebody that I broke my neck poor child. But I don’t believe it. (long beat)

I don’t believe in ANYTHING anymore, Superman. Not even you.
```

---

## IC-2445: The Last Rung on the Ladder

- Title: The Last Rung on the Ladder
- Author (byline): Stephen King
- Work: Night Shift, Pg 279-290
- Publisher: Signet Publishing
- Publication date as stated: 1978
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: LARRY, KITTY
- Teaser before the introduction: Yes
- Spoken words (computed): 1848
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen King
Book: Night Shift, Pg 279-290
ISBN: 978-0451170118
Publisher: Signet Publishing
Date (Month/Year): 1978
```

### Introduction (context only: never use it for content warnings)

```text
The Last Rung on the Ladder by Stephen King
```

### Performance text (classify this)

```text
LARRY: (Pg 279-290) I've been awake all night with it, with Katrina's letter. She could have put it on a postcard. There was only a single sentence below the "Dear Larry." But a sentence can mean enough. It can do enough.

We grew up eighty miles west of Omaha in a town called Hemingford Home-my dad, my mom, my sister Katrina, and me. I was two years older than Katrina, whom everyone called Kitty. She was a beautiful child even at eight, the year of the incident in the barn. It's her I want to tell you about.

LARRY: It happened one Saturday in early November. Mom was at a bake fair in Columbia City, and Dad had gone over to our nearest neighbor's (seven miles away) Dad left me a list of chores to do and told us not to get to playing until they were all done. But that wasn't long.

I remember that day very clearly. The sky was overcast and while it wasn't cold, you could feel it wanting to be cold. On a day like that, the only really nice place to be was the barn. It was warm and filled with a pleasant mixed aroma of hay and fur.

There was a ladder nailed to a crossbeam high up in the third loft, a ladder that went straight down to the main bam floor. We were forbidden to climb on it because it was old and shaky. Dad had promised Mom a thousand times that he would pull it down and put up a stronger one, but something else always seemed to come up.

If you climbed up that rickety ladder-there were exactly forty-three rungs, Kitty and I had counted them enough to know-you ended up on a beam that was seventy feet above the straw-littered bam floor. And then if you edged out along the beam about twelve feet, your knees jittering, your ankle joints creaking, your mouth dry, you stood over the haymow. And then you could jump off the beam and fall seventy feet straight down, with a horrible hilarious dying swoop, into a huge soft bed of hay.

It was a forbidden sport, all right. If we had been caught, my mother would have shrieked blue murder and my father would have laid on the strap. Because of the ladder, and because if you happened to lose your balance and toppled from the beam before you had edged out over the loose fathoms of hay, you would fall to utter destruction on the hard planking of the barn floor.

But the temptation was just too great. When the cats are away . . . well, you know how that one goes.

That day started like all the others, a delicious feeling of dread mixed with anticipation. We stood at the foot of the ladder, looking at each other. Kitty's color was high, her eyes darker and more sparkling than ever. (to Kitty) Dare you.

KITTY: Dares go first.

LARRY: Girls go before boys.

KITTY: Not if it's dangerous.

LARRY: I was ten that year, and thin as Scratch-the demon, almost ninety pounds. Kitty was eight and twenty pounds lighter. The ladder had always held us before.

I could feel it that day, beginning to shimmy around a little bit in the dusty barn air as I climbed higher and higher. As always, about halfway up I entertained a vision of what would happen to me if it suddenly let go. But I kept climbing until I was able to clap my hands around the beam and boost myself up and look down.

Kitty's face, turned up to watch me, was a small white oval. In her faded checked shirt and blue denims, she looked like a doll. (to Kitty) Hi. down there!

KITTY: Hi. up there!

LARRY: I stood up. Swayed back and forth a little. I could hear my own heartbeat as I began to inch along with my arms held out for balance. At last, I stood above the safety of the hay. There was a moment of anticipation. Then I stepped off into space, and as it always did, the sudden grip of gravity, yanking me down, making me plummet, made me feel like yelling: Oh, I’m sorry, I made a mistake, let me back upl Then I hit the hay, sort of swimming through it, until I could climb out onto the barn floor. I had hay down my pants and down the back of my shirt.

She was halfway up the ladder by then, her gold pigtails bouncing against her shoulder blades. I remember thinking that I didn't like the way the ladder was swaying back and forth. Then she was on the beam,

She stood, poising on the toes of her old low-topped Keds, hands out in front of her. And then she swanned. Talk about things you can't forget, things you can't describe. For a moment she seemed to hang in the air. She was Kitty, my sister, her arms swept behind her and her back arched, and how I loved her for that beat of time.

Then she came down and plowed into the hay and out of sight. An explosion of chaff and giggles rose out of the hole she made. I'd forgotten about how rickety the ladder had looked with her on it, and by the time she was out, I was halfway up again.

I felt the ladder moving beneath me and I could hear-very faintly-the whining rasp of old nails loosening up in the wood. And for the first time I was really, actively scared. I think if I'd been closer to the bottom I would have gone down and that would have been the end of it, but the beam was closer and seemed safer. Three rungs from the top the whine of pulling nails grew louder and I was suddenly cold with terror, with the certainty that I had pushed it too far. The fun of the game was gone.

I hurried out over the hay and dropped off. I came out to the middle of the barn to see Kitty hurrying up the ladder. I called: "Hey, come down! It's not safe!"

KITTY: It'll hold me. I'm lighter than you!

LARRY: Kitty! . . . But that never got finished. Because that was when the ladder let go. It went with a rotted, splintering crack. I cried out and Kitty screamed. The rung she was standing on gave way, and then both sides of the ladder split. Then it toppled, hitting the barn floor with a flat clap.

Kitty uttered a high, piercing scream. "Larry! Larry! Help me” I knew what had to be done, I saw right away. I was terribly afraid, but not quite scared out of my wits. She was better than sixty feet above me, her blue-jeaned legs kicking wildly at the blank air. I was scared, all right. I knew what had to be done. (to Kitty) Kitty! Just hold still, hold still . . .

She obeyed me instantly. Her legs. stopped kicking and she hung straight down, her small hands clutching the last rung on the ragged end of the ladder like an acrobat whose trapeze has stopped.

I ran to the haymow, clutched up a double handful of the stuff, ran back, and dropped it. I went back again. And again. And again. I ran back and forth, building a haystack where the foot of the ladder had been. It was a very small haystack. Back and forth. Back and forth.

KITTY: Larry, I can't hold on much longer!

LARRY: Back and forth. Back and forth. The haystack was as high as my chin now, but the haymow we had been diving into was twenty-five feet deep. I thought that if she only broke her legs it would be getting off cheap. And I knew if she missed the hay altogether, she would be killed. Back and forth.

I could hear the steady, rasping cry of the rung pulling free under her weight. Her legs began to kick again in panic, but if she was thrashing like that, she would surely miss the hay. (to Kitty) No! Stop that! Just let go! Let go, Kittyl (to audience) Because it was too late for me to get any more hay. Too late for anything except blind hope.

She let go and dropped the second I told her to. She came straight down like a knife. It seemed to me that she dropped forever, her gold pigtails standing straight up from her head, her eyes shut. She didn't scream. Her hands were locked in front of her lips, as if she was praying.

And she struck the hay right in the center. She went down out of sight in it- and I heard the thump of her body hitting the boards. It had been too loud, much too loud. But I had to see.

Starting to cry, I pounced on the haystack and pulled it apart. A blue-jeaned leg came to light, then a plaid shirt . . . and then Kitty's face. It was deadly pale, and her eyes were shut. She was dead. I knew it as I looked at her. The world went gray for me, November gray. And then she opened her eyes. "Kitty? Kitty?"

I picked her out of the hay and hugged her and she put her arms around my neck and hugged me back. "You're alive, you're alive, you're alive."

They let me in to see her just before bedtime. She looked at me so long and so lovingly that I was uncomfortable. Then she said,

KITTY: Hay. You put down hay. I didn't know what you were doing, I didn't dare look down, I was too scared. I had my eyes shut the whole time.

LARRY: You didn't know? Didn't know what I was doing? And when I told you to let go you . . . you just did it? Kitty, how could you do that?

She looked at me with those deep blue eyes.

KITTY: I knew you must have been doing something to fix it, You're my big brother. I knew you'd take care of me.

LARRY: It was the end, but somehow not the end. Somehow it never ended until nine days ago, when Kitty jumped from the top story of an insurance building in Los Angeles. I have the clipping from The LA. Times in my wallet. The headline reads: CALL GIRL SWAN-DIVES TO HER DEATH.

We grew up. That’s all I know, other than facts that don't mean anything. The only things that matter are that we grew up and she swanned from that insurance building, and that Kitty was the one who always believed the hay would be there. Kitty was the one who had said, "I knew you must be doing something to fix it." Those things matter. And Kitty's letter. (reading) Dear Larry, I’ve been thinking about it a lot lately . . . and what I’ve decided is that it would have been better for me if that last rung had broken before you could put down the hay. Your, Kitty

She was the one who always knew the hay would be there. And I wasn’t.
```

---

## IC-2446: The Last Supper, or the Dead Waiter

- Title: The Last Supper, or the Dead Waiter
- Author (byline): John Stewart
- Work: Naked Pictures of Famous People
- Publisher: Harper Collins
- Publication date as stated: Oct 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1771
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Stewart
Book: Naked Pictures of Famous People
ISBN: 978-0688171629
Publisher: Harper Collins
Date (Month/Year): Oct 1999
```

### Introduction (context only: never use it for content warnings)

```text
The Last Supper, or the Dead Waiterby John Stewart . . . This is The Manuscript of "Avram the Waiter"
```

### Performance text (classify this)

```text
The lack of information and interpretation concerning the life and times of Jesus Christ has, for years, frustrated scholars, theologians and lovers of information and interpretation. To date, the only notable published material on the subject is Franz Shecter's thorough yet ambiguous dissertation, "That Guy from the Thing." So little is known of Jesus because, as Shecter asserts, "He died a long time ago."

The virtual blackout has recently been lifted, in light of an astonishing discovery in the Sinai Peninsula. What is to date the only written account pertaining to the existence of Jesus Christ has been found. The manuscript contains explicitly reference to a dinner party Jesus had with twelve male friends. It is an eye-witness account penned by Avram the Waiter, who served the Christ party at the then-popular Jerusalem eatery, Jerry's.

So much for things being slow during Passover. It was April of 33 and as usual Jerry's was jammed. Jerry's was the "in" spot of the moment. Ever since Pilate started coming here the place has been packed with gawkers and wannabes. Personally, I could care less. You're a person, I'm a person. Doesn't matter if you're Augustus or Barabbas. You treat me with respect, you get good service. Anyway, I'm at the end of an eight-hour double, slopping kishke to drunken centurions, and in walks Jesus with his flock of hangers-on. "Here comes trouble," I say to Moishe the barback. We'd all seen Jesus and his little bunch of frat boys around town and believe me, not impressed. The Greeks invented a lot of great things- namely naked wrestling- but fraternities, or any other platonic organizations for that matter, weren't one of them.

So Luke, he's the skinny one with the greasy hair- oops, that's all of them- Luke says to me with a snotty attitude, "Table for thirteen…I believe it's under Christ." So I check the book. "Well, I can't find your reservation and besides, it looks like there's only eight of you here," I say to him. I'm telling the truth, by the way, not just being pissy. They didn't have a reservation and even if they did, I can't seat them if the whole party hasn't shown. Sorry, but it's not my rule. "They're coming. They'll be here. They got a little hung up. Holiday traffic," Luke says. You're kidding! Hung up in traffic? Well, that changes everything…please. Anyway, the guy's just checking out the scene, not even looking me in the eye. So all I say is, and Moishe will back me up on this, "You're welcome to hang out in the bar and wait for them…But I'm afraid-" and boom, he's on me. "Wait in the bar? You want us to wait in the bar. We're not waiting in the bar, little man." The way he was carrying on you'd have thought I asked him to bathe. (P.S. If Jesus is right and there is an afterlife, I hope they've got soap).

"Let me ask you something. What year is it?" Luke says. I know what he's going for but I play dumb. "What do you mean?" I ask innocently. You should have seen me, all wide-eyed and sheepish. Elijah caught my performance and said he was going to throw me a graduation party because it was obvious I no longer needed acting classes. "33 A.D." Luke says. I just let it hang there. "Anno Domini?...Year of the Lord," he says, giving the head nod over in Christ's direction. "You got me?" he says. So I turn to him real cool and go, "Well last time I checked my calendar it was still 3706." And then I snap my fingers and go back to marrying ketchups. Luke's jaw about hit the floor. Moishe turns and says, "Bathsheba one, Luke zero." It was really funny, but I wasn't just being a bitch. A lot of folks at Jerry's did still use the Hebrew calendar. And besides, with that attitude, those boys weren't' getting any special treatment from me. Jesus slips his tunic over his head just like the rest of us; I don't care who his father is.

I do have to admit I was a little scared. Some of these apostles are pretty rough trade, the blue-collar Nazareth crowd. And I think the others work out. They were pissed. Luke was yelling at me, saying if they don't get their table right away, Jesus would turn all our Chateau Lafite-Rothschild into low-grade zinfandel. "Do it!" I say. It's not like it's my wine.

Jesus' boys are in a bit of a frenzy, giving me the third degree. "What's your name?" "We want to talk to the manager!" "Fine," I say, "talk to the manager. Get me fired." I'm an artisan/poet. I'm putting up a night of spoken word in three weeks. I don't need to take shit from cult members. I should have gotten the Etruscan bouncer, Vito the Unreasonable. He'd have thrown them out on their apostles. So just as I'm about to hurl some sea salt in Peter's face, Jesus pipes up. "Boys," he says. "Please. The wise builder doesn't build on sand, but the foolish builder can't build on rock." I had no idea what he was talking about, but suddenly, the angry mob's all kittens and puppies. It's "Right, Rabbi." "Sorry, Rabbi." "Couldn't' have put it better myself, Teacher." Please! They're so affected. Jesus could have said, "Hey, look at me, I've got a banana up my ass!" and they would've acted like they just heard the word of God.

Finally, everybody shows up. It's nine o'clock. It's my last table, and the kitchen wants to close. So lucky me has to try and wrangle their order. It ain't easy. Matthew "has" to sit next to Jesus but John is having none of it, because his birthday's Monday and Jesus promised. Simon's blowing into his hand and pretending he farted. Mark and James are pouting because I carded them. Thomas wants a Caesar salad but doesn't believe it when I tell him you can hardly taste the anchovies in the dressing. Paul says he's lactose intolerant and claims if there's sour cream in his borscht, it's coming out of my tip. Judas sits glowering because no one will split and appetizer with him, and the rest of them just giggle at my ASK ME ABOUT OUR KUGEL! button. The way they behaved, I should have made them order off the children's menu.

If my ex-roommate hadn't just screwed me on last month's rent, believe me, I would've walked. I needed the shekels, but obviously none of these guys had ever waited tables. One of them actually snapped his fingers at me for a water refill. Not even to drink. He wanted to wash Jesus' feet! That's right, feet. Right at the table! It was enough to make Caligula nauseous. The only bev they ordered, one glass of house red. They all split it. Hello! Misers, party of thirteen.

At this point, I think they saw I was getting pissed and realized I would be handling their food. If you think that kind of thing doesn't happen in good restaurants all the time, you're kidding yourself. We had a bartender, Isaac, who had a special drink recipe for rude customers. I'll give you a hint: The magic ingredient is yak piss. You think I'm lying? He's a Bedouin and believe me those people could give a shit.

After I got them settled down, everyone ordered the lamb, except for John, who'd had Lamb for lunch. You'd have thought we were feeding the lions the way they attacked that thing. I hope Jesus is planning some commandments on table manners. Anyway, we got through dinner but you can be sure I had Carlos prepare a fatty cut, even though they asked for lean.

As far as Jesus goes, we'd all hear about the miracles he performs, but he actually seemed pretty normal. I've had friends who get a little success and immediately turn into assholes, but he was cool about it. My friend's sister caught him when he did two nights in Thebes. She said it was okay. He bent some spoons and guessed that one guy in the audience was thinking about changing jobs, but she said he was better when he was still with the Lepers. Jesus definitely did no miracles at his dinner, although one of the waiters who got his autograph said it cleared up his sinuses. No real pearls of wisdom either. Once, right before dessert, Jesus said to no one in particular, "Why do people park on a driveway and drive on a parkway?" It was kind of funny. Truthfully, Jesus spent most of the time asking people whether or not a beard would make him look smarter. There was a bit of a scuffle when Paul liked the idea but Judas thought it was trendy. I say cut the hair. Please. You're not a musician and it's very B.C.

Personally, when I found out one of those guys had betrayed Jesus, it didn't surprise me a bit. You can ask David son of Phil. I told him that night, "I would not trust these guys if I were Jesus." It's so obvious they're not really his friends. They're just hanging around him because he's famous. You should have seen them scatter when I brought the bill. "Can you cover me, Jesus?" "I'll get you next time, Jesus." "I gotta go drain the staff, Jesus!" I don't know how the Jesus puts up with it. Poor guy probably had to walk on water just to get some peace and quiet.

Not that it kept me up nights. Let's face it. Messiahs come and go. Just last week I had a creep on table five who claimed that if I followed him, I would enjoy eternal joy in a place called Utah. He said I could have as many wives as I wanted but not caffeine. Get real. Me? Choose women over coffee? Please. Still, I was sorry to hear what happened to Jesus. He was a good tipper.

Editor's note: After this piece was published it was brought to our attention that Avram's manuscript is not the only document pertaining to the life and times of Jesus Christ. A work titled "The New Testament" was sent to our offices along with a large number of other pertinent volumes. We regret this oversight. Also, upon great scholarly review, Avram's manuscript was found to be written in Magic Marker, an implement not discovered until the early nineteen hundred and fifties. Again, our regrets.
```

---

## IC-2447: Laws Concerning Food and Drink; Household Principles; Lamentations of the Father

- Title: Laws Concerning Food and Drink; Household Principles; Lamentations of the Father
- Author (byline): Ian Frazier
- Work: Lamentations of the Father: Essays, Pg 8-13 [Originally published in the Feb 1997 edition of The Atlantic Magazine]
- Publisher: Farrar, Straus and Giroux
- Publication date as stated: April 2008
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1218
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ian Frazier
Book: Lamentations of the Father: Essays, Pg 8-13
[Originally published in the Feb 1997 edition of
The Atlantic Magazine]
ISBN: 978-0374281625
Publisher: Farrar, Straus and Giroux
Date (Month/Year): April 2008
```

### Introduction (context only: never use it for content warnings)

```text
We’ve all heard of the 10 Commandments . . . You know the ones: Don’t murder, Don’t commit adultery, Don’t steal, Don’t covet. Yeah, most of them were DON’Ts, but a few were Dos, like Do Keep the Sabbath day holy and um . . . huh . . . I know there was one more. Do . . . Do . . . I got it! Do Honor your father and mother.

And that can be a challenge, right? Especially if your father is like the beleaguered one in this selection. He’s expanded a bit on the biblical cannon when he created the rules for his household.

Laws Concerning Food and Drink; Household Principles; Lamentations of the Father by Ian Frazier
```

### Performance text (classify this)

```text
FATHER: Of the beasts of the field, and of the fishes of the sea, and of all foods that are acceptable in my sight you may eat, but not in the living room. Of the hoofed animals, broiled or ground into burgers, you may eat, but not in the living room. Of the cloven-hoofed animal, plain or with cheese, you may eat, but not in the living room. Of the cereal grains, of the corn and of the wheat and of the oats, and of all the cereals that are of bright color and unknown provenance you may eat, but not in the living room. Of the quiescently frozen dessert and of all frozen after-meal treats you may eat, but absolutely not in the living room. Of the juices and other beverages, yes, even of those in sippy-cups, you may drink, but not in the living room, neither may you carry such therein. Indeed, when you reach the place where the living room carpet begins, of any food or beverage there you may not eat, neither may you drink.

But if you are sick, and are lying down and watching something, then may you eat in the living room.

FATHER: And if you are seated in your highchair, or in a chair such as a greater person might use, keep your legs and feet below you as they were. Neither raise up your knees, nor place your feet upon the table, for that is an abomination to me. Yes, even when you have an interesting bandage to show, your feet upon the table are an abomination, and worthy of rebuke. Drink your milk as it is given you, neither use on it any utensils, nor fork, nor knife, nor spoon, for that is not what they are for; if you will dip your blocks in the milk, and lick it off, you will be sent away. When you have drunk, let the empty cup then remain upon the table, and do not bite it upon its edge and by your teeth hold it to your face in order to make noises in it sounding like a duck; for you will be sent away.

When you chew your food, keep your mouth closed until you have swallowed, and do not open it to show your brother or your sister what is within; I say to you, do not so, even if your brother or your sister has done the same to you. Eat your food only; do not eat that which is not food; neither seize the table between your jaws, nor use the raiment of the table to wipe your lips. I say again to you, do not touch it, but leave it as it is. And though your stick of carrot does indeed resemble a marker, draw not with it upon the table, even in pretend, for we do not do that, that is why. And though the pieces of broccoli are very like small trees, do not stand them upright to make a forest, because we do not do that, that is why. Sit just as I have told you, and do not lean to one side or the other, nor slide down until you are nearly slid away. Heed me; for if you sit like that, your hair will go into the syrup. And now behold, even as I have said, it has come to pass.

Laws Pertaining to Dessert For we judge between the plate that is unclean and the plate that is clean, saying first, if the plate is clean, then you shall have dessert. But of the unclean plate, the laws are these: If you have eaten most of your meat, and two bites of your peas with each bite consisting of not less than three peas each, or in total six peas, eaten where I can see, and you have also eaten enough of your potatoes to fill two forks, both forkfuls eaten where I can see, then you shall have dessert. But if you eat a lesser number of peas, and yet you eat the potatoes, still you shall not have dessert; and if you eat the peas, yet leave the potatoes uneaten, you shall not have dessert, no, not even a small portion thereof. And if you try to deceive by moving the potatoes or peas around with a fork, that it may appear you have eaten what you have not, you will fall into iniquity. And I will know, and you shall have no dessert. On Screaming Do not scream; for it is as if you scream all the time. If you are given a plate on which two foods you do not wish to touch each other are touching each other, your voice rises up even to the ceiling, while you point to the offense with the finger of your right hand; but I say to you, scream not, only remonstrate gently with the server, that the server may correct the fault. Likewise, if you receive a portion of fish from which every piece of herbal seasoning has not been scraped off, and the herbal seasoning is loathsome to you, and steeped in vileness, again I say, refrain from screaming. Though the vileness overwhelm you, and cause you a faint unto death, make not that sound from within your throat, neither cover your face, nor press your fingers to your nose. For even now I have made the fish as it should be; behold, I eat of it myself, yet do not die.

Various Other Laws Bite not, lest you be cast into quiet time. Neither drink of your own bath water, nor of bath water of any kind; nor rub your feet on bread, even if it be in the package; nor rub yourself against cars, nor against any building; nor eat sand.

Leave the cat alone, for what has the cat done, that you should so afflict it with tape? And hum not that humming in your nose as I read, nor stand between the light and the book. Indeed, you will drive me to madness. Nor forget what I said about the tape.

Complaints and Lamentations O my children, you are disobedient. For when I tell you what you must do, you argue and dispute hotly even to the littlest detail; and when I do not accede, you cry out, and hit and kick. Yes, and even sometimes do you spit, and shout "stupid-head" and other blasphemies and hit and kick the wall and the molding thereof when you are sent to the corner. And though the law teaches that no one shall be sent to the corner for more minutes than he has years of age, yet I would leave you there all day, so mighty am I in anger. But upon being sent to the corner you ask straightaway, "Can I come out?" and I reply, "No, you may not come out." And again you ask, and again I give the same reply. But when you ask again a third time, then you may come out.

Hear me, O my children, and remember that I am that I am: before, after, and until you are twenty-one. Hear me then, and avoid me in my wrath, O children of me.
```

---

## IC-2448: The Legend of Spud Murphy

- Title: The Legend of Spud Murphy
- Author (byline): Eoin Colfer
- Work: Not specified
- Publisher: Miramax Books
- Publication date as stated: Sept 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: DAD, WILL, MARTY, MOM, DONNIE, HP, BERT, LITTLE BOY, SPUD MURPHY
- Teaser before the introduction: Yes
- Spoken words (computed): 979
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eion Colfer
ISBN: 978-0786855018
Publisher: Miramax Books
Date (Month/Year): Sept 2004
```

### Introduction (context only: never use it for content warnings)

```text
The name Spud Murphy strikes fear into the hearts of children everywhere. Grown-ups think she’s a kindly old librarian, but kids know the truth. They’ve heard all about the gas-powered spud gun she keeps hidden under her desk. Make so much as a sound in Spud’s library, and you could get spudded with soggy potatoes. Laugh out loud, and you may never be seen again.

The Legend of Spud Murphy by Eoin Colfer
```

### Performance text (classify this)

```text
(Will and Marty are rough housing, loudly playing pirates or cowboys or superheroes in an improv format until DAD puts a stop to it)

DAD: (Chapter 1) This is a madhouse.

WILL: And he’s the chief lunatic. (pointing at Marty)

MARTY: I’m not the one talking to dolls!

WILL: Action Man is not a doll.

DAD: (through gritted teeth) Quiet! There must be something we can find for you to do during the summer. Something to get you out of the house.

MOM: What about the library? (Will and/or Marty horrified expression)

DAD: Reading! It’s perfect. How can you cause trouble reading a book?

MOM: Yes, of course, it’s educational too.

MARTY: Don’t make us join the library. It’s too dangerous!

DAD: Dangerous? How could a library be dangerous?

MARTY: (whispering) It’s not the library. It’s the librarian.

MOM: Mrs. Murphy? She’s a lovely old lady.

WILL: She’s not a lovely old lady. She hates kids and she used to be a spy in the army. Tracking kids from enemy countries!

MOM: I’ve heard enough. You two are going to the library for the afternoon and that’s it. We’ll make sandwiches.

WILL: (to audience) Sandwiches wouldn’t be much use against Spud Murphy and her gas-powered spud gun. (Chapter 2) Of course our little brothers thought this was hilarious. (Chapter 1) Having one little brother is bad enough but having three? The trouble with little brothers is that they are never blamed for anything. All Donnie, Bert and HP have to do is bat their blue eyes and let their bottom lips wobble a bit and they are forgiven for everything.

DONNIE: (batting his eyes) Nice knowing you!

HP: (with a lisp) Yeth, Nithe knowing you.

BERT: (with a wobbly bottom lip) Can I have your Walkman?

WILL: Do you hear them, Mom? They’re teasing us already!

MOM: Oh, they don’t mean it. My babies!

WILL: Mom gave them a gummi bear each and I thought that my head would pop with the unfairness of it all. (Chapter 2) [Later that day] Mom dropped us at the library on her way downtown.

MOM: Okay, off you go, up the steps. I’ll just stay here to make sure you go inside.

WILL: (growling quietly as the boys exit the car) (to audience) I bet you’re thinking we were a pair of gutless chickens. But that’s because you think libraries are happy colorful places, where the librarians actually like children. That may be what most of them are like, but this one was different.

LITTLE BOY: (running from the library in tears) Don’t go in there! Don’t do it! I was one day late with Five Go to Smuggler’s Top. Just one day. And look what she did to me! (he runs away)

WILL: And just like that, the boy was gone, with only a puddle of tears to prove he had ever been there. We stayed there until Mom came up the steps. We had no choice but to go inside. (The boys enter the library and look around in fear) The library seemed to go on forever. Row after row of wooden bookshelves.

SPUD MURPHY: (behind the desk, she spoke with a voice like two pieces of rusted metal being rubbed together) What do you want? (Will and Marty quake with fear) I said, what do you want? (stamping a book vigorously with an ink stamp)(the boys approach the desk cautiously)

WILL: (to audience) Spud Murphy was big. Taller than my dad, and wider than Mom and my two aunties strapped together. (squeaking) Mom says we have to join the library.

SPUD MURPHY: Name?

WILL: M – M – Mrs. Murphy?

SPUD MURPHY: (Sighing) Not my name, dummy. Your names.

WILL: (shouting like an army cadet) William and Martin Woodman! (to audience) We surrendered our name and our address was next. Now Spud knew where we lived.

SPUD MURPHY: (fills in the library cards) Pink cards (handing them to the boys) Pink means you stay in the Junior section. (she leads them to a small section of the library . . . pointing) That is the Junior Section.

WILL: A single bookshelf with four rows of books. On the ground -- a small patch of carpet.

SPUD MURPHY: Do not set foot off that carpet until you leave. Whatever boyish idea enters your head, ignore it. Stay on the carpet or there will be trouble. (she bends over until her eyes are level with the boys) Is that understood? (she returns to her desk)

MARTY: (in library voices) (Chapter 3) What exactly did she mean? [Does] trouble mean a strict talking-to? Or [does] trouble mean being suspended by your fingernails over a pit of alligators? I need to know how much I can get away with!

WILL: I don’t need to know. I’ll just sit here and pretend to read.

MARTY: No wonder Action Man is your only friend. I am an actual hero type. I am prepared to take risks! (Marty checks to see if Spud can see him) She can’t even see us. We can do whatever we want!

WILL: What are you going to do?

MARTY: I’m going to switch a few books. The best way to mess with a librarian is too put things back in the wrong place. By the time she finds out, we’ll be home watching cartoons. (Marty sneaks off the carpet and begins switching books)

WILL: (to audience) He switched almost every single book in the section. Mysteries with romance, adventure with bird-watching! Suddenly a shadow fell across my brother. (Spud Murphy looms behind Marty) It was Spud.

SPUD MURPHY: I knew it! (Marty squeaks like a kitten) I can always tell a troublemaker. I took one look at you Martin Woodman and I knew you’d be off that carpet before I was back at my desk.

MARTY: I’m sorry, Spu – Mrs. Murphy. I’ll never leave the carpet again.

SPUD MURPHY: Too late for that. Since you’re already off the carpet, you can fix the damage you’ve done, and maybe I won’t tell your mother how you set off the fire alarms.

MARTY: But . . . I didn’t!

SPUD MURPHY: I know you didn’t. And I’m sure your mother will believe that. Unless, of course, you’ve been in trouble before.

WILL: (to audience) He’d met his match. Two hours and fourteen paper cuts later, Mom was outside, waiting in the car. We were almost safe . . .

MARTY: That wasn’t so bad. I’ve had teachers meaner than her! (Marty stops at the exit and turns to make a beeline for Spud’s desk) Excuse me, Mrs. Murphy. You wouldn’t really say I set off the alarms, would you?

SPUD MURPHY: Oh, wouldn’t I? (She opens her desk and speaks sweetly) (Pg 84) Stand in front of my desk. I have something for you. (Chapter 3)

WILL: (Pg 85) Oh no! The gas-powered spud gun!

SPUD MURPHY: You’re going to get what you deserve. Go on, in front of my desk. (Chapter 3) I have a collection of stamps here. One came in last week you might like. It’s in the shape of a pirate flag. A lot of the boys like me to stamp it onto their forearms, like a temporary tattoo. . . But maybe you’re too young.

MARTY: No, I’d love that (already rolling up his sleeve) Wait until the guys at the swimming pool see this!

SPUD MURPHY: Are you sure, Martin? (Spud inks the stamp) This won’t wash off for a couple of weeks.

MARTY: I’m sure. Stamp away.

SPUD MURPHY: (smiling widely) Okay then. Keep still. (she rolls the stamp on Marty forearm)

MARTY: (leaning over to read it, he wails) I LOVE BARBIE!

SPUD MURPHY: Oops. Wrong stamp. Sorry about that. (a glare) One more thing. Any more of your little games and I get nasty. There are worse things in this desk than rubber stamps. (she brings out her potato shooter and cocks it with a hiss) Enjoy swimming (she laughs as the boys run for the door)
```

---

## IC-2449: Life is So Good

- Title: Life is So Good
- Author (byline): George Dawson and Richard Glaubman
- Work: Not specified
- Publisher: Penguin USA
- Publication date as stated: June 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2116
- Already set (do not supply): none

### Source block (context only)

```text
Author: George Dawson and Richard Glaubman
ISBN: 978-0141001685
Publisher: Penguin USA
Date (Month/Year): June 2001
```

### Introduction (context only: never use it for content warnings)

```text
People spend most of their lives in the quest of happiness and can’t find it. See, the problem is they look to the world to provide them with reasons to be happy. But according to Ralph Marston, “Happiness is a choice, not a result. Nothing will make you happy until you choose to be happy.”

In this selection, George Dawson, a 101-year-old black man who didn’t learn to read until he was 98, recalls a childhood event that set his course through life – the death of Pete, an older boy who was George’s hero.

George’s father helped his son deal with Pete’s death and also taught him a lesson that stuck with George for over a hundred years: Despite all the negative forces at work in our society . . .

Life is So Good by George Dawson and Richard Glaubman.
```

### Performance text (classify this)

```text
Pg 3-13

Wanting to enjoy every moment, I stared at the hard candies in the different wooden barrels. The man behind the counter was white. I could tell he didn't like me, so I let him see the penny in my hand.

“Take your time, son. You did a man's work this year. Putting his hand on my shoulder, he said to the store clerk, ”He’s all of ten years, but the boy crushed as much cane as I did.”

Since the age of four, I had always been working to help the family. I don't know if it was pride from Father's words or the pleasure from a piece of hard candy that beckoned, but I felt so good I thought I would burst. I had been thinking of those hard candies since my father woke me before daybreak and said, “Hitch the wagon. We gonna take some ribbon syrup into town and you comin’.“

I wanted to tell him that I was glad he was taking me and it was going to be just him and me together all day. He took care of us. We had potatoes and carrots buried in the straw and salt pork hangin' from the rafters. We was free of worries. Papa was a good provider. Someday I would be just like him.

“With this ribbon syrup, we be out of debt and have some left for trading. We gonna have seeds for cotton, some new banty chicks, and the fruit trees that are gonna bear fruit next year. No one has the fever and we all be healthy. Life is good.” And with a grin, he added, “ I do believe it's getting better.” I liked it when Papa talked to me as a man.

It was 1908, and I hadn't yet seen a car. I had heard of them, but nobody I knew owned one. The cafe and the barbershop was whites only, but I knew a boy that worked in the cafe. And I knew some folks that shined shoes at the barbershop.

I remember everything. I saw the white man frowning, my father grinning at me, and those barrels of candy to choose from. I also remember everything my ears told me that day. As I picked up a piece of peppermint, I heard a commotion from the street. My father's gaze followed mine. There were people running, harsh words, and a lot of shouting. Papa run to the door. I followed with the counterman behind me. I heard Pete's voice before I saw him. “It wasn't me. I didn't touch her,” Pete screamed. “Lord, let me go.

First time in my life I saw the white folks and the colored folks together in a crowd. It scared me. There was no more frown on the face of the white counterman that was beside of me. His lips were set in a smile. Hate was in his eyes. Across the street, in front of the barbershop, I saw three colored men frozen in place. The white folks surrounding them had red, twisted faces. They were screaming. I had done nothing, but I felt them screaming at me.

“Kill the nigger boy, kill the nigger. They can't be messing with our white women.”

Six men had Pete by the arms. The toes of his boots dragged in the dust. His face looked up to the sky as he screamed, “I didn't touch her.”

I knew Pete and knew that was so. I shouted, "Pete, I'll tell-" My father's hand clamped over my mouth. His other arm crushed the air right out of my chest. I read his eyes and then he slowly let me go without saying a word. I knew it wasn't so, though. The Rileys' cook had heard the whole thing; she just kept on working in the kitchen and watched Betty Jo and her father. Betty Jo had gotten herself in trouble. When her daddy found out she was with a child, she had a whipping coming sure enough. Her daddy was steaming mad and of short temper anyhow.

“Who's the boy that done this to you?” her daddy shouted. Betty Jo looked at the belt in his hand. She was crying but wouldn't say nothing. She was scared, and afraid to tell the boy's name, because she figured that her daddy just might go off and kill him. “Well, if you did this 'cause you wanted to, a good beating will teach you right. You got it coming unless maybe this happened against your will. Is that what happened?” he said slowly.

Scared as she was, Betty Jo could tell that the safe answer was yes. Not wanting to tell a whole lie, she just nodded her head.

“Damn. Was it that Jackson boy from across the ridge?”

Betty Jo, she loved him, or at least thought she did, shook her head no. Her daddy looked at her hard. His face turned angry and he said, “Was it our hired boy, Pete? That worthless, lazy nigger! Did he rape you? Did he do this?” To each question, she just nodded in the smallest way. The tears still flowed, but he threw the belt down and stormed out the door.

Pete was seventeen and the hired boy around their farm-picking cotton, cutting cane, chores like that. He was a good worker. But he was smart and he knew enough not to even look at a white woman. I knew Pete since we were little. Pete, he would do anything for anybody. As I was growing up, I didn't have any toys, but I did still own a baseball that Pete had given me a year earlier. Pete played shortstop. He was good too. If you wanted fast, you should have seen Pete run the bases. Pete was my hero. The colored couldn't play in the big leagues, but if they could I know Pete would of made it.

Yeah, someone had committed a sin and Pete was gonna pay for it. I looked down the boardwalk. They was dragging Pete in the direc-tion of the post office. Sheriff Tate stepped off the boardwalk up ahead from where the mob was. I let out a big breath of air. The sheriff was a big man. I knew he could stop this. People was spilling off the boardwalk and cursing Pete something terrible.

“We gonna keep our women safe.”

“Make that boy pay and show all the niggers that they can't get away with this.”

Pete was kicking and thrashing, but the mob was still hauling him farther down the street. Taking a few steps along the edge of the road, the sheriff stopped. A big pistol hung off his belt. He pulled the pistol out and crossed his arms so that the pistol set against his chest. He turned and looked back toward the boardwalk. The sheriff was in front of a group of colored that was pressed into the crowd. He scowled and sent them a message that gave me a chill on a hot day. I had heard tell that the sheriff ran with the Klan at night when they would come through the colored section or out to the colored farms. They would leave a burning cross or shoot some windows out. That's what people said about him and now I knew it was true.

Behind us, a man was pushing his way out of the store. The sheriff walked toward us and waved his pistol. We opened up some space and let the man through. I saw the big coil of rope slung over his shoulder. I wanted to cry, but I held it back. He ran along the edge of the street and a couple other men stepped down to join him. Some of them were farmers I recognized from when we delivered our cotton. They looked like ordinary farmers with overalls and farm work boots. But that day, their hateful faces made them different. As they caught up alongside Pete, the mob seemed to get inspired. Pete had been twisting and screaming all get-out, but those men seemed to double their strength when they seen the lynching rope coming.

Someone pulled a wagon into the shade under the rope. Pete was closer now, could see the rope and the wagon. His shouts and protests had changed to cries for mercy. “I swear to God it wasn't me. Have mercy, you've got the wrong man. I didn't touch her.”

Pete's eyes had a wild look as more men began milling around him. He was up on his feet now, but it was more that they was holding him up. Pete was swaying, as if he was about to faint. His face was all bloodied, but his eyes could see clear what was going to happen. His arms were pinned behind him and someone had bound him around the wrists. One of the men in the buckboard said, "Get that boy up here." Now it was Pete that stood steady and still.

Some men were still holding Pete tight from behind so that he couldn't even budge. But if Pete knew he was gonna die, the fear had left his face.

[Then] Pete's legs buckled. He moaned as those men dragged him the remaining few feet around to the back of the buckboard.

“I didn't do nothing,” Pete cried in a voice that rang without hope. I buried my head against my father's chest.

When I heard the whip snap and the buckboard lurch forward, I looked back. Pete's neck broke instantly; his head rested at an awk-ward angle. His eyes were open and he looked out at everyone. As he swayed from the tree, the crowd hushed and tried to look away from his accusing eyes. Not till Pete's body stopped swinging did anyone move. The crowd broke up in silence and went their separate ways.

I didn't want to, but as we left Marshall I turned 'round in my seat and looked. Pete was still looking at me and I knew that he always would be. Pete would stay till morning. When they did a lynching, they made us leave the body hanging, to put a terror in the colored folk.

His face looked different than I had ever seen it, but Papa still hadn't said a word.

“I will never work for or talk to a white person again.” I said with anger.

My father, who had seemed lost in his own thoughts, jerked his head and looked at me. “That was wrong what they did. Those white folks are mean and nasty people." Papa swallowed hard and pulled up on the reins so that the wagon stopped. He turned toward me. “No. You will work for white folks. You will talk to them.“

“But, Papa, what about Pete? He didn't do

“Yeah, I know they had no cause for that, but- his suffering is over, son. It's all over for Pete. You don't need to worry for him.”

“Some of those white folks was mean and nasty. Some were just scared. It doesn't matter. You have no right to judge another human being. Don't you ever forget.”

My father had spoken. There was nothing to say. I didn't know it then, but his words set the direction my life would take even till this day. I cried and my daddy wrapped his arms around me and held me to his chest. Then something broke loose deep inside. I didn't know a body could have so many tears. I cried for me. I cried for Pete. I cried for the little ones and for Mama and Papa. I cried for all the pain that there was in this world. Papa had his own tears and he just held me. When the tears slowed, Papa told me. “This morning, I said that you did a man's work. But you was still a boy. Now you are learning to be a man.”

About six months after the lynching, Betty Jo had her baby. It was a boy, a little white boy. No one said nothing. I guess by then most folks, white folks anyway, had all forgotten. I didn't forget.

I'm one hundred and one years old now. But I still remember. Though that was over ninety years ago, I see it in my mind like I was there today. I can't let loose of my memories, even if I wanted to. Yeah, I've seen it all in these hundred years, the good and the bad.

(PG 260) Things will be alright. Most folks just don't understand. Life is so good and it gets better every day.
```

---

## IC-2450: The Littlest Hitler

- Title: The Littlest Hitler
- Author (byline): Ryan Boudinot
- Work: The Best American Non-Required Reading 2003
- Publisher: Houghton Mifflin, Co.
- Publication date as stated: Oct 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2234
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ryan Boudinot
Book: The Best American Non-Required Reading 2003
ISBN: 978-0618246960
Publisher: Houghton Mifflin, Co.
Date (Month/Year): Oct 2003
```

### Introduction (context only: never use it for content warnings)

```text
A child’s understanding and comprehension of the atrocity known as The Holocaust is understandably limited. It is only with maturity, that the social concepts surrounding this time in history become clear. When one is 8 or 9, intellectual capacity often falls into the categories of good versus bad, black versus white, right versus wrong. In The Littlest Hitler by Ryan Boudinot we find a young boy just coming to terms with a concept which was at first beyond his grasp . . . . Hitler (scary Halloween costume or something more?)
```

### Performance text (classify this)

```text
[I remember] the time I went as Hitler for Halloween. I had gotten the idea after watching World War II week on PBS. My dad helped me make the costume. I wore tan polyester pants and one of his khaki shirts, with sleeves so long they dragged on the floor unless I rolled them up. With some paints left over from when we made the pinewood derby car for YMCA Indian Guides, the painted a black swastika in a white circle on a red bandanna and tied it around my left arm. Using the Dippity-Do he put in his hair every morning, he gave my own hair that plastered, parted style that had made Hitler look as if he was always sweating. We clipped the sides off a fifty-cent mustache and adhered it to my upper lip with liquid latex. I tucked my pants into the black rubber boots I had to wear whenever I played outside and stood in front of the mirror. My dad laughed and said, “I guarantee it, Davy. You’re going to be the scariest kid in the fourth grade.”

My school had discouraged trick-or-treating since the razor blade and thumbtack incidents of 1982. Instead, they held the Harvest Carnival, not officially called “Halloween” so as not to upset the churchy types. Everyone at school knew the carnival was for wimps. All week before Halloween the kids had been separating themselves into two camps, those who got to go trick-or-treating and those who didn’t. My dad was going to take me to the carnival, since I, like everybody else, secretly wanted to go. Then we’d go trick-or-treating afterward.

There were problems with my costume as soon as I got on the bus that morning. “Heil Hitlah!” the big kids in the back chanted until Mrs. Reese pulled over to reprimand them. We knew it was serious when she pulled over. The last pulling-over incident occurred when Carl Worthington cut off one of Ginger Lopez’s pigtails with a pair of scissors stolen from the library.

“That isn’t polite language appropriate for riding the bus!” Mrs. Reese said. “Do you talk like that around the dinner table? I want you both in the front seats, and as soon as we get to school I’m marching you to Mr. Warneke’s office.”

“But I didn’t do anything!”

I felt guilty for causing the ruckus. Everybody was looking at me with these grim expressions. It’s important, I suppose, to note that there wasn’t a single Jewish person on the bus. Or in our school, for that matter. In fact, there was only one Jewish family in our town, the Friedlanders, and their kids didn’t go to West Century Elementary because they were home-schooled freaks.

When I got to school Mrs. Thompson considered me for a moment in the doorway and seemed torn, both amused and disturbed at the implications of a fourth-grade Hitler. When she called roll I stood up sharply from my desk, did the salute I’d been practicing in front of the TV, and shouted, “Here!” Some people laughed.

After roll was taken we took out our spelling books, but Mrs. Thompson had other ideas. “Some of you might have noticed we have a historical figure in our class today. While the rest of you dressed up as goblins and fairies and witches, it looks like Davy is the only one who chose to come as a real-life person.”

“I’m a real-life person, too, Mr. Thompson.”

“And who would you be, Lisette?”

“I’m Anne Frank.”

Mrs. Thompson put a hand to her lips. Clearly she didn’t know how to handle this. I’d never paid much attention to Lisette before. She’d always been one of the smart, pretty girls everyone likes. When I saw her rise from her desk with a lopsided Star of David made of yellow construction paper pinned to her Austrian-looking frock or whatever you call it, I felt the heat of her nine-year-old loathing pounding me in the face.

“This is quite interesting,” Mrs. Thompson said. “You both came as figures from World War II. Maybe you can educate us about what you did. Davy, if you could tell us what you know about Hitler.”

I cleared my throat. “He was a really, really mean guy.”

“What made him so mean?”

“Well, he made a war and killed a bunch of people and made everybody think like him. He only ate vegetables, and his wife was his niece. He kept his blood in jars. Somebody tried to kill him with a suitcase, and then he took some poison and died.”

“What people did he kill?”

“Everybody. He didn’t like Jesse Owens because he as Afro-American.”

“Yes, but mostly what kind of people did he have problems with?”

“He killed all the Jews.”

“Not all Jews, fortunately, but millions of them. Including Anne Frank.”

The classroom was riveted. I didn’t know whether I was in trouble or what. Lisette smirked at me when Mrs. Thompson said her character’s name, then walked to the front of the class to tell us about her.

“Anne Frank lived in Holland during World War II. And when the Nazis invaded she lived in someone’s attic with her family and some other people. She wrote in her diary every day and liked movie stars. She wanted to grow up to write stories for a newspaper, but the Nazis got her and her family and made them go to a concentration camp and killed them. A concentration camp is a place where they burn people in ovens. Then somebody found her diary and everybody liked it.”

When Lisette was done everybody clapped. George Ford, who sat in front of me and was dressed as Mr. T. turned around, lowered his eyes, and shook his fist at me. “I pity the foo’ who kills all the Jews.”

Recess was a nightmare.

I was followed around the playground by Lisette’s friends, who were playing horse with a jump rope, berating me for Anne Frank’s death.

“How would you like it if you had to live in an attic and pee in a bucket and couldn’t walk around or talk all day and didn’t have much food to eat?”

It didn’t take long for them to make me cry. The rule about recess was you couldn’t go back into the building until the bell, so I had to wait before I could get out of my costume. I got knots in my stomach thinking about the parade at the end of the day. Everybody else seemed so happy in their costumes. And then Lisette started passing around a piece of notebook paper that said “We’re on Anne Fran’s Side,” and all these people signed it. When my friend Charlie got the paper he tore it up and said to the girls, “Leave Davy alone! He just wanted to be a scary bad guy for Halloween and he didn’t really kill anybody!”

“I should just go as someone else,” I said, sitting beneath the slide while some kids pelted it with pea gravel. This was Charlie’s and my fort for when we played GI Joe.

“They can kiss my grits,” Charlie said. He was dressed as a deadly galactic robot with silver spray-painted cardboard tubes for arms and a pair of New Wave sunglasses. “This is a free country, ain’t it? Hey! Stop throwing those son-of-a-bitching rocks!”

“Charlie!”

“Oops. Playground monitor. Time for warp speed.” Charlie pulled on his thumb, made a clicking sound, and disappeared under the tire tunnel.

Despite Charlie’s moral support, I peeled my mustache off and untied my armband as soon as I made it to the boys’ room. There were three fifth-graders crammed into a stall, going, “Oh, man! There’s corn in it!” None of them seemed to notice me whimpering by the sink.

Mrs. Thompson gave me her gray-haired wig to wear for the parade.

“Here, Davy. You can be an old ma. An old man who likes to wear khaki.”

I knew Mrs. Thompson was trying to humor me and I resented her for it. Lisette, for whatever, reason, maybe because her popularity in our classroom bordered on celebrity worship, got to lead the parade. I was stuck between Beck Lewis and her pathetic cat outfit and Doug Becker, dressed as a garden. His mom and dad were artists. Each carrot, radish, and potato had been crafted in meticulous papier-mache, painted, lacquered, and halfway embedded in a wooden platform he wore around his waist. The platform represented a cross section, with brown corduroys painted with rocks and earthworms symbolizing dirt, and his fake-leaf-covered shirt playing the part of a trellis. For the third year in a row Doug ended up winning the costume contest.

By the time our parade made it to the middle school I was thoroughly demoralized. I had grown so weary of being asked, “What are you?” that I had taken to wearing the wig over my face and angrily answering, “I’m link! I’m lint!”

My dad made wood stoves for a living. When my mom left he converted our living room into a shop, which was embarrassing when my friends came over, because the inside of our house was always at least ninety degrees. My dad was genuinely disappointed when he learned of my classmates’ reactions.

“But everyone knows you’re not prejudiced. It’s Halloween, for crying out loud.” He folded the bandanna, looking sad and guilty. “I’m sorry, Davy. We didn’t mean for it to turn out like this, did we? Tell you what. Let’s go to Sprouse-Reitz and buy you the best goddamn costume they got.”

We drove into town in the blue pickup we called Fleetwood Mack. Smooth like a Cadillac, built like a Mack truck. The Halloween aisle at 6:30 P.M. on October 31 is pretty slim pickings. There was a little girl with her mom fussing over a ballerina outfit – last-minute shoppers like us. I basically had a choice between a pig mask, some cruddy do-it-yourself face paint deals, and a discounted Frankenstein mask with a torn jaw.

“Hey! Lookit! Frankenstein!” my dad said, trying to invest some enthusiasm in the ordeal. “Don’t worry about the jaw, we’ll just duct tape it from the inside. Nobody’ll even notice.”

“I want a mask with real hair. Not fake plastic lumpy hair,” I said.

“You don’t really have a choice here, Davy. Unless you want the pig mask.”

“Fine. I’ll go as stupid Frankenstein.”

My dad grabbed me by the elbow and spun me around. “Do you want a Halloween this year or not? You can’t go trick-or-treating without a costume, and this is about your only option. Otherwise it’s just you and me sitting on our [butts] in front of the television tonight.”

In Fleetwood Mack we sang along to the Steve Miller Greatest Hits tape and picked the richest-looking neighborhoods to trick-or-treat on. With a greasy Burger King bag salvaged from the floor of the truck, we went door-to-door, my dad hanging out behind me, waving politely. Somebody even tossed him a can of beer.

I didn’t know we were at the Friedlanders’ house until Mrs. Friedlander opened the door. Word had it they were among the parents who didn’t let their kids go trick-or-treating since the razor blade and thumbtack scare of 1982. Hannah Friedlander sat on the steps up to the second story of their split-level house, leaning over in her sorceress costume to see who it was. Mike, her brother, came up the stairs from the rec room and joined her, breathing dramatically in his Darth Vader mask. I wanted to do something nice for them, wanted to just hand them my whole bag, but I couldn’t bring myself to do it. I’d be too embarrassed, I’d make my father angry, I’d call too much attention to the fact that they couldn’t go trick-or-treating. SO I chose to do nothing but accept Mrs. Friedlander’s individually wrapped Swiss chocolate balls and thanked her, then walked back to Fleetwood Mack with my dad and went home, looking at all the Halloween displays through the nostrils of Frankenstein’s nose.

“So, did you have an okay Halloween after all?” my dad said, carrying me upstairs to my bedroom. I nodded and got into my PJs. He pulled the covers over my face and bit my nose through the blanket as he did every night. Later, when I could hear him snoring through the wall, I took the bag of candy from my dresser and tiptoed downstairs to what used to be our living room. There was a stove hooked up to each of our three chimneys, one which was cold, one with some embers inside, the third filled with flames. I opened the door to the flaming stove and thought about throwing my whole bag in there, but then remembered the rule: wood and paper only. Besides, I had an entire Snickers bar in there; I wasn’t insane. I sat for a long time eating chocolates, one by one, in front of the fire. Then I reached into the stove to see how far I could go before it really started to hurt.
```

---

## IC-2451: A Long Way Gone: Memoirs of a Boy Soldier

- Title: A Long Way Gone: Memoirs of a Boy Soldier
- Author (byline): Ishmael Beah
- Work: Not specified
- Publisher: Sarah Crichton Books
- Publication date as stated: Feb 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: FRIEND, ISHMAEL, ALHAJI, KANEI, GASEMU, REBEL 1, REBEL 2, SOLDIER
- Teaser before the introduction: Yes
- Spoken words (computed): 1675
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ishmael Beah
ISBN: 978-0374105235
Publisher: Sarah Crichton Books
Date (Month/Year): Feb 2007
```

### Introduction (context only: never use it for content warnings)

```text
It is, perhaps, one of the most important war stories of our time. In over twenty countries around the world, children as young as 7 years old are serving as child soldiers. And not just a few of them either – more than 300,000 boys are fighting in current armed conflicts. They wield AK-47s and M-16s, serve as human mine detectors, and participate in suicide missions. Many of these children are abducted or recruited by force. Others join out of desperation, believing it is their best chance for survival.

In this true story, author Ishmael Beah tells how he became one of them. He was only 12 when rebel forces attacked his Sierra Leone village in 1998. Separated from his family, Ishmael spent months searching for them. In this scene, he and his fellow child soldiers approach a village where their families are said to be in hiding.

A Long Way Gone: Memoirs of a Boy Soldier by Ishmael Beah
```

### Performance text (classify this)

```text
My high school friends have begun to suspect I haven’t told them the full story of my life.

FRIEND: Why did you leave Sierra Leone?

ISHMAEL: Because there was a war.

FRIEND: You saw people running around with guns and shooting each other?

ISHMAEL: Yes, all the time.

FRIEND: Cool.

ALHAJI: I look forward to getting to this village. Ah, I will give my mother a very tight hug. (smiles) She always complains, though, when I give her a tight hug: ‘If you love me, stop squeezing my old bones so I can be alive longer.’ She is funny.

KANEI: I have a feeling that we will find our families, or at least news of them.

Finally, we were approaching the village where seeing our families was actually a possibility. I couldn’t stop smiling. We came across a man cutting down ripe bananas. The sight of his face awakened my memory. He was much skinnier than when I had last seen him. His name was Gasemu – Ngor Gasemu. (Ngor is a title like “Mr.”)

GASEMU: (Peeps at them from behind a banana leaf. Wipes the sweat off his forehead and walks toward them. Smiles.)

You boys want to help me carry some bananas to the village?

(asks in the manner that adults usually ask young people when they won’t take no for an answer.) Come on. (Motions for them to follow him into the banana farm. Continues waving his hand.) (speaks to Ishmael)

Are you still a troublesome boy?

ISHMAEL: There is no time to be troublesome these days.

GASEMU: Your parents and brothers will be happy to see you. They have been talking about you every day and praying for your safety. Your mother cries every day. Your older brother left to look for you, but he returned about a week ago. His face was sad when he returned. I think he blames himself for losing you.

I wanted to drop the bananas and run as fast as I could to the village. I felt as if my heart would explode if I waited any longer.

GASEMU: The village is just over the hill.

I heard gunshots. And dogs barking. And people screaming and crying. We dropped the bananas and began running. A thick smoke started rising from the village. Nails were popping off tin roofs, and they flew landing on nearby thatched roofs, increasing the wrath of the fire. We heard screams and loud banging a few houses away. There were people locked in it. We banged the door open, but it was too late. Only two people came out, a woman and a young child. They were on fire, and ran up and down the village, slamming themselves against everything in their way. The woman fell and stopped moving. The child gave a loud screech and sat next to a tree. He stopped moving. It all happened so fast that we just stood there, rooted to the ground. The child’s yelp was still echoing in my head, as if it had taken on a life of its own inside me.

On other paths of the village were the half-burnt remains of those who had fought fiercely to free themselves, only to die outside. I hesitantly tried to make out the faces of burnt bodies, but it was impossible to tell who they had been. Besides, there were too many of them.

GASEMU: Your family stayed in that house. (Pointing toward one of the charred houses.) The fire had consumed all the door and window frames. (His entire body goes into shock. Only his eyes move, slowly opening and closing. He falls to the ground, holding his face. He gets up and runs toward the house. Without any fear, he goes inside and looks around the smoke-filled rooms. He screams at the top of his lungs and begins to cry as loudly as he can, punching and kicking with all his might into the weak walls that continue to burn.)

My hands and feet punched and kicked the burning walls, but I couldn’t feel a thing. Gasemu and the rest of the other boys began pulling me away from the house.

Soon we heard loud voices of people approaching the village. We ran into the nearby coffee farm and lay in the dirt watching. A group of more than ten rebels were laughing and giving each other high fives. Two looked slightly older than me – maybe 13 or 14. They had blood on their clothes, and one of them carried the head of a man, which he held by the hair. Blood dripped from where the neck had once been. The other rebel carried a gallon of gasoline and a big box of matches.

REBEL 1: We burned three villages today. (laughing)

REBEL 2: Yes, three is impressive, in just a few hours in the afternoon. (pauses) I especially enjoyed burning this village. We caught everyone here. No one escaped. That is how good it was. Commander will be pleased when he gets here. (nods)

REBEL 1: Some people escaped in the other two villages. (pauses, rubs his forehead as if pondering why that had happened.) They probably saw the smoke from this village and knew something was happening. We should change our strategy. Next time we must attack all the villages at the same time.

I had heard from adults that this was a revolutionary war, a liberation of the people from corrupt government. But what kind of liberation movement shoots (and burns) innocent civilians, children? We escaped the village and ran to the forest. We must have been walking for days, I do not really remember, when suddenly two men put us at gunpoint and motioned, with their guns, for us to come closer. They were the soldiers – not the rebels. There were four men lying on the ground, their uniforms soaked with blood. I turned away, and my eyes caught the smashed head of another man. I felt nauseated. Everything began to spin around me. One of the soldiers was looking at me (smiling). He took a drink from his water bottle and threw the remaining water at my face.

SOLDIER: You will get used to it; everybody does eventually.

The soldier led us to Yele, a village that was occupied by the military. In the beginning, it seemed we had finally found safety there. The village was full of lively chattering and laughter. All that darkened the mood of the village was the sight of orphaned children. There were over thirty boys between the ages of seven and sixteen. I was one of them. One morning the atmosphere in the village suddenly became tense. It wasn’t clear what had caused the change, but something was about to happen. I was awake when the soldiers left in the middle of the night. The following morning, wounded soldiers were brought back only to die by lamplit surgery. Prisoners were lined up and shot in the head. These things went on for many days, and each time the soldiers went to the front lines, few returned. The lieutenant asked his men to gather everyone at the square.

(in the voice of the Lieutenant): In the forest there are men waiting to destroy all of our lives. We have fought them as best as we can, but there are too many of them. They are all around the village. (Makes a circle in the air with his hands.) They won’t give up until they capture this village. They want our food and ammunition.

(Pauses, and slowly continues.) Some of you are here because they have killed your parents or families; others because this is a safe place to be. Well, it is not that safe anymore. That is why we need strong men and boys to help us fight. If you do not want to fight or help, that is fine. But you will not have rations and will not stay in this village. This is your time to revenge the deaths of your families and to make sure more children do not lose theirs.

We had no choice. Leaving the village was as good as being dead. The women and older people in the village stood on their verandahs and watched as we were led away by the adult soldiers into the clearing toward the forest. A baby cried uncontrollably in his mother’s arms, as if he knew what lay ahead of us. I have never been so afraid to go anywhere in my life as I was that day. Tears had begun to form in my eyes, but I struggled to hide them and gripped my gun for comfort. The lieutenant had passed the word down through a whisper: “Fire on my command.” As we watched, a group of men dressed in civilian clothes emerged. Some were boys, as young as we were. The lieutenant gave the order to fire. I lay there unable to shoot. The forest had begun to spin. (clutches the base of a tree with one hand.) I couldn’t think, but I could hear the sounds of the guns far away in the distance and the cries of people dying in pain. A splash of blood hit my face. (spits it out, wipes his face) I saw the soldier it had come from. Blood poured out of the bullet holes in him like water rushing through newly opened tributaries. He cried for his mother in the most painfully piercing voice I had ever heard. My face, my hands, my shirt and gun were covered with blood. I raised my gun and pulled the trigger, and I killed a man. Suddenly, as if someone was shooting them inside my brain, all the massacres I had seen since the day I was touched by war began flashing in my head. I angrily pointed my gun into the swamp and killed more people. I shot everything that moved. We went out two more times that week, and I had no problem shooting my gun. The idea of death didn’t cross my mind at all, and killing had become as easy as drinking water. My mind had not only snapped during the first killing, it had also stopped making remorseful records. We practiced killing prisoners. We were supposed to slice their throats on the corporal’s command. The person whose prisoner died quickest would win the contest. I didn’t feel a thing for my prisoner, didn’t think that much about what I was doing. I just waited for the corporal’s order. The prisoner was simply another rebel who was responsible for the death of my family, as I had come to truly believe. The corporal gave the signal with a pistol shot and I grabbed the man’s head and slit his throat in one fluid motion. I was the winner. CLOSING At age 16, Ishmael Beah was removed from the fighting by UNICEF. He was brought to New York City, where he graduated from high school and earned a college degree. Today, he serves as a member of various human rights groups, having spoken before the United Nations, the Council on Foreign Relations, and the Center for Emerging Threats and Opportunities. Through the help of a rehabilitation center, Ishmael has learned how to forgive himself, to regain his humanity, and, finally, to heal.
```

---

## IC-2452: Looking a Lot Like Christmas

- Title: Looking a Lot Like Christmas
- Author (byline): Jason Sheets
- Work: Turning Points
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 989
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jason Sheets
Book: Turning Points
Publisher: Tichenor Publishing
ISBN: 978-0742117013
Date: 2001
```

### Introduction (context only: never use it for content warnings)

```text
Pantomime: Put a record on the record player . . .listen for a moment then begin singing as you decorate the Christmas tree.

Have yourself a Merry little Christmas Let your hearts be light From now on, our troubles will be out of sight

Have yourself a merry little Christmas Make the Yuletide gay From now on, our troubles will be miles away

Welcome to my holiday ritual. It begins with the early Christmas specials and ends with Dick Clark's Rockin' Eve. I watch by myself. Alone with a glass of egg nog. . . . Looking a Lot Like Christmas by Jason Sheets
```

### Performance text (classify this)

```text
Ever notice how the characters on Christmas specials have no family? I mean Rudolph: a loner. Charlie Brown has a whole party without his parents. Those elves may have a social network going, but rarely do you see them with their family. I'm sure they all have fami-lies. It's implied. I guess that's why I watch them each Christmas. People assume I have a family. It's implied. So how'd I end up this way? One word: homosexuality. Or, as my sister put it, three words: "that queer thing". For 20 years, I was the straightest man in Wichita.

Sure, there were hints. When my friends had sleepover parties and we'd sneak a look at Playboy, everyone else was mesmerized. They'd say "Whoa!", so I'd say "Whoa!" But I never really understood what all the" whoaing" was about. When Die Hard was big, all the other guys liked it when Bruce Willis kicked some ass. I liked it when the ass-kicking required ripping off his shirt. So, the thoughts were there, but that's all they were. Thoughts.

In college I hid it. I was too busy. It was always something else. A paper. A party. An intramural basketball game. Anything but the topic of romance. Anything but a blind date. Anything but addressing my weird fascination to my fraternity brother. Anything but that.

But then I met someone. Not just anyone. The someone that you always dream about. In my first year in the office, Tom asked me out for drinks. I didn't think it was a date. Maybe it wasn't at first. But as the seasons changed from autumn to winter to spring, I knew. And when Tom said he loved me, I had no problem loving back. OK, some problem - I was new at this. Still, I was whisked into a fantasy world. A place I could call my own.

One problem: family. Actually two sub-sets of the same problem:

1.) I always wanted a family. OK - call me short-sighted, but just as I knew I was gay, I also pictured myself with the standard wife, kids, dog, picket fence - you know the routine. Tom and I weren't exactly family Channel material.

2.) My family would be stunned. They would call a therapist, a priest, and my old high school prom date simultaneously and plot a conversion. It would be hell.

So, when I got up the strength to tell my family, 28 months later, I decided to do it with style. Pizzazz.

Christmas dinner. Extended family and all. I was really wasn't going for the shock factor - I just would be damned if I'd have to give the spiel twice. It opened as planned: Mom fixes ham and potatoes, dad says grace, sisters complain of the fat content, grandpa states that it's good to have the family together on the holidays, and off we go on another Christmas at the Engelhans. I was ready.

"OK everyone. I wanted to tell you something. I know you all have said I should date more. I just wanted to tell you that I've met someone. Actually we've been dating for almost 3 years. I've never felt so right, so alive. His name is Tom -"

Stop. Freeze frame. You know how you learn in science class that at zero degrees Kelvin, all motion ceases? Zero degrees Kelvin - right there at the dinner table. Dad gives me a look like he should have played more football with me when I was a kid. Mom stares into space. My sisters look like I just stole their boyfriend. Then things happen in slow motion. My aunt drops her fork into her soup. Dad says, "This is no time for sick jokes." Mom says, "Yes, it's Christmas." Grandma says, "Is Tom short for Thomasina?" Grandpa says, "I'm not listening to this" and leaves.

Dinner continues. Silent. Voiceless. And yet speaking volumes.

That night I meet up with dad in the living room. He's always been the spokesperson for the family. He certainly will be for this, too.

"Do you love him?"

"Yes."

"Does he love you?"

"Yes."

"Do you see a future with him?"

"I certainly hope so."

"Son, you've pulled the rug out from under me. What do you want me to say? I'm happy? I'm not. You've chosen a difficult lifestyle."

"It's not-"

"I know. I know. It's not a choice. Maybe it's not. Who's to say? But now you've forced a choice on me. My Bible says it's wrong. I can choose to accept you and reject my Bible, or I can accept the Bible and reject you. Do you understand what decision you're forcing on this family?"

I knew this was going to be difficult. I knew that. But I never dreamed of the horror of that night. Growing up, my father taught me one thing above all others: never turn your back to the Lord. And that was what he chose to do that night. Not turning his back on the Lord meant the family turning its back on me. I never went back to that house. I drove past, but never went back.

There was only one person who hadn't turned his back on me, but he did so three weeks later. He said he didn't envision a future for us. He said so in a note. My life reduced to a post-it. And then there was none.

And that's how I'm here. Uniquely myself; uniquely alone. Sure, we've got support meetings. Meetings to make us feel like we're not alone. But we are alone, often reduced to two emotions: numbness and rage.

Numbness, rage, Christmas specials, and egg nog.

The life of a gay man in America. No family to marry into; no way to re-create the old one. I have made the right decision. To be true to myself But still - it's Christmas. I light a Christmas candle. It represents hope.
```

---

## IC-2453: Love is a Fallacy

- Title: Love is a Fallacy
- Author (byline): Max Shulman
- Work: Current Issues and Enduring Questions
- Publisher: St. Martin's Press
- Publication date as stated: Feb 1987
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1766
- Already set (do not supply): none

### Source block (context only)

```text
Author: Max Shulman
Book: Current Issues and Enduring Questions
ISBN: 978-0312179243
Publisher: St. Martin's Press
Date (Month/Year): Feb 1987
```

### Introduction (context only: never use it for content warnings)

```text
Love is a Fallacy by Max Shulman
```

### Performance text (classify this)

```text
Cool was I and logical. Keen, calculating, perspicacious, acute and astute—I was all of these. My brain was as powerful as a dynamo, precise as a chemist’s scales, as penetrating as a scalpel. And—think of it!—I only eighteen.

It is not often that one so young has such a giant intellect. Take, for example, Petey Bellows, my roommate at the university. Same age, same background, but dumb as an ox.

One afternoon I found Petey lying on his bed with an expression of such distress on his face that I immediately diagnosed appendicitis. “Raccoon,” he mumbled thickly.

“Raccoon?”.

“I want a raccoon coat,” he wailed. . I stroked my chin thoughtfully. It so happened that I knew where to get my hands on a raccoon coat. My father had had one in his undergraduate days; it lay now in a trunk in the attic back home. It also happened that Petey had something I wanted -- his girlfriend, Polly Espy.

I had long coveted Polly Espy. Beautiful she was. Gracious she was. Intelligent she was not. In fact, she veered in the opposite direction. But I believed that under my guidance she would smarten up. At any rate, it was worth a try. It is, after all, easier to make a beautiful dumb girl smart than to make an ugly smart girl beautiful.

“Look,” I said to Petey when I got back Monday morning. I threw open the suitcase and revealed the huge, hairy, gamy object that my father had worn in 1925.

“Holy Toledo!” said Petey.

“Would you like it?” I asked.

“Oh yes!” he cried. “What do you want for it?”

“Your girl.” I said, mincing no words.

“Polly?” he said in a horrified whisper. “You want Polly?”

I sat down in a chair and pretended to read a book, but out of the corner of my eye I kept watching Petey. He was a torn man. First he looked at the coat with the expression of a waif at a bakery window. Then he turned away and set his jaw resolutely. Then he looked back at the coat, with even more longing in his face.

“It isn’t as though I was in love with Polly,” he said thickly. “Or going steady or anything like that.”

I rose from my chair. “Is it a deal?” I asked, extending my hand.

He swallowed. “It’s a deal,” he said and shook my hand.

I had my first date with Polly the following evening. I wanted to find out just how much work I had to do to get her mind up to the standard I required. I took her first to dinner. “Gee, that was a delish dinner,” she said as we left the restaurant. Then I took her to a movie. “Gee, that was a marvy movie,” she said as we left the theatre. And then I took her home. “Gee, I had a sensaysh time,” she said as she bade me good night.

I went about it, as in all things, systematically. I gave her a course in logic. As a law student, I was taking a course in logic myself, so I had all the facts at my fingertips. “Poll’,” I said to her when I picked her up on our next date, ‘Logic’ is the science of thinking. Before we can think correctly, we must first learn to recognize the common fallacies of logic. These we will take up tonight.”

“Wow-dow!” she cried, clapping her hands delightedly.

I winced, but went bravely on. “First let us examine the fallacy called Dicto Simpliciter.”

“By all means,” she urged, batting her lashes eagerly.

“Dicto Simpliciter means an argument based on an unqualified generalization. For example: Exercise is good. Therefore everybody should exercise.”

“I agree,” said Polly earnestly. “I mean exercise is wonderful. I mean it builds the body and everything.”

“Polly,” I said gently, “the argument is a fallacy. Exercise is good is an unqualified generalization. For instance, if you have heart disease, exercise is bad, not good. Many people are ordered by their doctors not to exercise. You must qualify the generalization. You must say exercise is usually good, or exercise is good for most people. Otherwise you have committed a Dicto Simpliciter. Do you see?”

“No,” she confessed. “But this is marvy. Do more! Do more!”

“Next we take up a fallacy called Hasty Generalization. Listen carefully: You can’t speak French. Petey Bellows can’t speak French. I must therefore conclude that nobody at the University of Minnesota can speak French.”

“Really?” said Polly, amazed. “Nobody?”

I fought off a wave of despair. I was getting nowhere with this girl, absolutely nowhere. Still, I am nothing if not persistent. I continued. “Next comes Post Hoc. Listen to this: Let’s not take Bill on our picnic. Every time we take him out with us, it rains.”

“I know somebody just like that,” she exclaimed. “A girl back home—Eula Becker, her name is. It never fails. Every single time we take her on a picnic—”

“Polly,” I said sharply, “it’s a fallacy. Eula Becker doesn’t cause the rain. She has no connection with the rain. You are guilty of Post Hoc if you blame Eula Becker.”

I frowned, but plunged ahead. “Here’s an example of Contradictory Premises: If God can do anything, can He make a stone so heavy that He won’t be able to lift it?”

“Of course,” she replied promptly.

“But if He can do anything, He can lift the stone,” I pointed out.

“Yeah,” she said thoughtfully. “Well, then I guess He can’t make the stone.”

“But He can do anything,” I reminded her.

She scratched her pretty, empty head. “I’m all confused,” she admitted.

“Of course you are. Because when the premises of an argument contradict each other, there can be no argument. If there is an irresistible force, there can be no immovable object. If there is an immovable object, there can be no irresistible force. Get it?”

I decided to give it one more try.

“Listen closely,” I said. “A man applies for a job. When the boss asks him what his qualifications are, he replies that he has a wife and six children at home, the wife is a helpless cripple, the children have nothing to eat, no clothes to wear, no shoes on their feet, there are no beds in the house, no coal in the cellar, and winter is coming.”

A tear rolled down each of Polly’s pink cheeks. “Oh, this is awful, awful,” she sobbed.

“Yes, it’s awful,” I agreed, “but it’s no argument. The man never answered the boss’s question about his qualifications. Instead he appealed to the boss’s sympathy. He committed the fallacy of Ad Misericordiam. Do you understand?”

One more chance, I decided. But just one more. There is a limit to what flesh and blood can bear. “The next fallacy is called “Poisoning the Well.”

“How cute!” she gurgled.

“Two men are having a debate. The first one gets up and says, ‘My opponent is a notorious liar. You can’t believe a word that he is going to say.’ ... Now, Polly, think. Think hard. What’s wrong?”

I watched her closely as she knit her creamy brow in concentration. Suddenly a glimmer of intelligence—the first I had seen—came into her eyes. “It’s not fair,” she said with indignation. “It’s not a bit fair. What chance has the second man got if the first man calls him a liar before he even begins talking?”

“Right!” I cried exultantly. “One hundred per cent right. It’s not fair. The first man has poisoned the well before anybody could drink from it... Polly, I’m proud of you.”

Five grueling nights with this took, but it was worth it. I had taught Polly to think. My job was done. She was worthy of me, at last. She was a fit wife for me, a proper hostess for my many mansions, a suitable mother for my well-heeled children.

I decided to acquaint her with my feelings at our very next meeting. The time had come to change our relationship from academic to romantic.

“My dear,” I said, favoring her with a smile, “we have now spent five evenings together. We have gotten along splendidly. It is clear that we are well matched.”

“Hasty Generalization,” said Polly brightly. “How can you say that we are well matched on the basis of only five dates?”

I chuckled with amusement. She had learned her lessons well. “My dear,” I said, patting her hand in a tolerant manner, “five dates is plenty. After all, you don’t have to eat a whole cake to know that it’s good.”

“False Analogy,” said Polly promptly. “I’m not a cake. I’m a girl.”

I chuckled with somewhat less amusement. She had learned her lessons perhaps too well. I decided to change tactics. Obviously the best approach was a simple, strong, direct declaration of love. I paused for a moment while my massive brain chose the proper words. Then I began:

“Polly, I love you. You are the whole world to me, the moon and the stars and the constellations of outer space. Please, my darling, say that you will go steady with me, for if you will not, life will be meaningless. I will languish. I will refuse my meals. I will wander the face of the earth, a shambling, hollow-eyed hulk.”

There, I thought, folding my arms, that ought to do it.

“Ad Misericordiam,” said Polly.

I dashed perspiration from my brow. “Polly,” I croaked, “you mustn’t take all these things so literally. I mean this is just classroom stuff. You know that the things you learn in school don’t have anything to do with life.”

“Dicto Simpliciter,” she said, wagging her finger at me playfully.

That did it. I leaped to my feet, bellowing like a bull. “Will you or will you not go steady with me?”

“I will not,” she replied.

“Why not?” I demanded.

“Because this afternoon I promised Petey Bellows that I would go steady with him.”

With an immense effort of will, I modulated my voice. “All right, Let’s look at this thing logically,” I said. “How could you choose Petey Bellows over me? Look at me—a brilliant student, a tremendous intellectual, a man with an assured future. Look at Petey—a knothead, a jitterbug, a guy who’ll never know where his next meal is coming from. Can you give me one logical reason why you should go steady with Petey Bellows?”

“I certainly can,” declared Polly. “He’s got a raccoon coat.”
```

---

## IC-2454: Lucky Man

- Title: Lucky Man
- Author (byline): Michael J. Fox
- Work: Not specified
- Publisher: Hyperion Press
- Publication date as stated: April 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1388
- Already set (do not supply): none

### Source block (context only)

```text
Author: Michael J. Fox
ISBN: 978-0786888740
Publisher: Hyperion Press
Date (Month/Year): April 2002
```

### Introduction (context only: never use it for content warnings)

```text
When the symptoms of his Parkinson's disease are at their worst, Michael J. Fox can't write. Or speak. Or stay still. With medication, these effects can be masked for short periods. It's during these times that he wrote Lucky Man: A Memoir,
```

### Performance text (classify this)

```text
Gainsville, Florida - November 1990

I woke up to find the message in my left hand. It had me trembling. It wasn't a fax, telegram, memo, or the usual sort of missive bringing disturbing news. In fact, my hand held nothing at all. The trembling was the message.

I was feeling a little disoriented. I’d only been shooting the movie in Florida for a week or so, and the bed in the hotel suite still came as a bit of a shock each morning.

That’s when I noticed my pinkie. It was twitching, trembling, auto-animated. How long this had been going on I wasn’t exactly sure, but I was surprised to discover that I couldn’t stop it. Weird-maybe I slept on it funny.

The trembling had been going on for a few minutes with no sign of quitting and what had begun as curiosity was now blossoming into a full-fledged worry.

I found myself wandering the halls of New York City’s Mount Sinai Hospital. White jacketed nursed and doctors scurried back and forth through the corridor. Any one of them would have recognized the name of the physician I was looking for, but that was the problem: they were also just as likely to recognize me. I didn’t want any gossip about why Michael J. Fox was seeing one of the preeminent neurologists in North America.

The nurse at the front desk showed me into the examining room, and as I was shedding my coat and baseball cap, she noticed the shaking in my left hand.

“It’s ok,” she said. “You don’t have to be nervous.”

Confused for a second, I suddenly realized she was talking about the tremor.

“Oh,” I responded. “That’s…that’s why I’m here. In a neurologist’s office, I mean.”

After a second of mutual embarrassment, she left, closing the door behind her. Minutes later, it opened again, and walked in the legendary neurologist himself.

“Essential tremor, maybe,” he said. “Possibly something else, but you’re here, so let’s have a look.”

“Finally,” I thought. “We’re going to get to the bottom of this. This guy knows what he’s talking about.”

The most paranoid fantasy I could think of would not have prepared me for the two words the neurologist bludgeoned me with that day: Parkinson’s disease.

Recollecting my exact response to this is difficult. My symptoms showed up in my late twenties! How could I possibly have this old person’s disease?

The air sucked from my lungs, my left arm was shaking clear up to my shoulder. Why was he doing this to me? What was I going to tell Tracy? I looked up at the doctor and stared; he was so composed. Tough for him, I bet, dropping this on a guy my age. He was really very good…I hated his guts!

As I stepped out of the door of his office building and onto the rain-soaked streets of mid town Manhattan, it was as if I were entering a whole new world, but the only profound change was not around me, but within me. I had to get home though. Hailing a cab and the ride itself would be slow going. That was ok-I needed every second to sort out what just happened and how I was going to explain this to Tracy, my mother, family, and the rest of my friends. It wouldn’t be enough time.

I let myself into the apartment. I could smell dinner cooking in the kitchen and hear my son Sam giggling. I couldn’t go in there and face him at the moment. Tracy entered from the kitchen and I met her in the foyer and silently motioned her to the bedroom. As she followed me, I could feel her curiosity escalating toward panic.

In the bedroom is where I told Tracy. Tracy, stunned and frightened, cried. At the same time she was so present, so loving…In sickness and in health I remember her whispering, her arms around me. Typically my first instinct to Tracy: It’ll be ok; to myself: what will be ok?! I have Parkinson’s disease!

As it was, each week’s show presented a brand new set of creative and physical challenges. Could I count on my body to respond in performance the same way it had in rehearsal? By now I could see that the strain I put myself through by trying to be funny was exhausting. Whatever I appeared to be doing onstage, I was, in fact, doing something else: hiding symptoms with a repertoire of little tricks and distracting maneuvers. Many days I had to concentrate more on my physical relationship to the scene unfolding around me than to emotional, comedic, or dramatic content. All the while I was doing the math-how long since the last pill? How long until it wears off? And at what point in the show will I have to take another one? “Please…let it be during a scene I’m not in.”

If the warning came when I was in the middle of a four-to-five minute scene, there wasn’t a thing I could do to stave off the return of my symptoms. If a studio audience were to detect a tremoring of my arm, a slowing of my speech, or a rigidity of my movements, it would undoubtedly betray the fact that something was wrong and that something would be decidedly unfunny. This became one of my greatest fears; just making an audience laugh remained one of my greatest pleasures.

So I did everything I could to make sure the audience didn’t know I was sick. I have always thrived on my relationship to the audience, and feared taking any risk that would distract or detract from it. Timing a joke depends on the audience being with me, and if their attention is lost even for a second while they are watching my arm or a hitch in my gait, then I’ve lost them. If an audience didn’t know what I was dealing with, they wouldn’t know what to look for, so I still had a shot at making them laugh. But if they already knew that I was battling an incurable disease, would they still go along for the ride, or would they be watching for symptoms and feeling sorry? Can sick people be funny?

I was beginning to realize that this was what was keeping me from telling people that I had Parkinson’s disease. Over the past seven years I had experienced so many highs and lows, and had finally set about facing my fears. The distance my disease had put between me and the people I care about had been narrowed, but what about the audience? Until I felt ready to tell them my story, my life would never be fully integrated and as happy.

I can vividly remember all those nights when the studio audience had to wait for my symptoms to subside. I’d be back stage, lying on the dressing room rug, twisting and rolling around. When that approach failed, I’d spruce up the walls with fist sized holes, the graffiti of my frustration! How much longer could this go on?

I entered into Joyce’s office on Friday morning. I had a show a show to do that night.

“I’ve had this feeling lately,” I began. “One I haven’t had in years. That old feeling like I’m waiting for the other shoe to drop.”

Joyce was quiet. “Michael, you have Parkinson’s disease-the other shoe dropped a long time ago.”

Almost as if I had walked into a hug, I immediately felt enveloped in a wave of emotion, not of sadness, but of relief and pride. Joyce was right. The other shoe had already dropped, and I survived. There was nothing left to fear. It was time, I was ready.

*************

Coping with the relentless assault and the accumulating damage is not easy. Nobody would ever choose to have this visited upon them. Still, this unexpected crisis forced a fundamental life decision: adopt a siege mentality -- or embark upon a journey. Whatever it was - courage? acceptance? wisdom? -- that finally allowed me to go down the second road (after spending a few disastrous years on the first) was unquestionably a gift - and absent this neurophysiological catastrophe, I would never have opened it, or been so profoundly enriched. That's why I consider myself a lucky man.
```

---

## IC-2455: The Lunatic’s Tale

- Title: The Lunatic’s Tale
- Author (byline): Woody Allen
- Work: Side Effects
- Publisher: Ballantine Books
- Publication date as stated: Sept 1986
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1832
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: Side Effects
ISBN: 978-0345343352
Publisher: Ballantine Books
Date (Month/Year): Sept 1986
```

### Introduction (context only: never use it for content warnings)

```text
Everyone knows why men cheat. Well, everyone thinks they know. The theory runs like this: Men — not all of them, but quite a few — are pigs. They identify themselves as hunters, as opposed to gatherers or certified public accountants or weenies, and thus deem themselves biologically incapable of remaining monogamous. Some might even come clean and admit that they have met somebody younger. Or better-looking. Or richer. Or younger, better-looking and richer. With whom the sex is awesome. Some may even go as far as to claim insanity. Thank you. Dr. Farkis! Which brings us back to the original point, that a lot of men are pigs. Woody Allen in The Lunatic’s Tale attempts to explain infidelity from a man’s point of view – Funny? Maybe . . . A cutting insight into what’s wrong with our society today . . . . More likely. The Lunatic’s Tale by Woody Allen.
```

### Performance text (classify this)

```text
Madness is a relative state. Who can say which of us is truly insane? And while I roam through Central Park wearing moth-eaten clothes and a surgical mask, screaming revolutionary slogans and laughing hysterically, I wonder even now if what I did was really so irrational. For, I was not always what is popularly referred to as "a New York street crazy," pausing at trash cans to fill my shopping bags with bits of string and bottle caps. No, I was once a highly successful doctor living on the upper East Side, gadding about town in a brown Mercedes, and bedecked dashingly in a varied array of Ralph Lauren tweeds. Hard to believe that I, Dr. Ossip Farkis, am now sometimes seen roller skating unshaven down Broadway wearing a knapsack and a pinwheel hat.

The dilemma that precipitated this catastrophic fall from grace was simply this. I was living with a woman, Olive Chomsky, whom I cared for very deeply and who had a winning and delightful personality and mind. But (and I curse Fate for this) she did not turn me on . . . sexually. Concurrently, I was sneaking crosstown nightly to rendezvous with a photographer's model called Tiffany Schmeederer. Undoubtedly, you have heard the expression, "a body that wouldn't quit," Well Tiffany's body would not only not quit, it wouldn't take five minutes off for a coffee break. Skin like satin, a leonine mane of chestnut hair, long willowy legs and a shape so curvaceous that to run one's hands over any portion of it was like a ride on the Cyclone. This not to say Olive was a slouch - Not at all. In fact she was a handsome woman - a charming and witty culture vulture and, crudely put, a mechanic in the sack. Perhaps it was the fact that when the light hit Olive at a certain angle she inexplicably resembled my Aunt Rifka. Not that Olive actually looked like my mother's sister. (Rifka had the appearance of a character in Yiddish folklore called the Golem) It was just that some vague similarity existed around the eyes, and then only if the shadows fell properly. Perhaps it was just that a face and body like Tiffany Schmeederer's comes along every few million years and usually heralds an ice age or the destruction of the world by fire. The point is, my needs required the best of two women.

It was Olive I met first. And this after an endless string of relationships wherein my partner invariably left something to be desired. My first wife was brilliant, but had no sense of humor. My second wife was beautiful, but lacked real passion. Sharon Pflug, whom I lived with for three months, was too hostile. Whitney Weisglass was too accommodating. Pippa Mondale, a cheerful divorcee, made the fatal mistake of defending candles shaped like Laurel and Hardy.

Well-meaning friends fixed me up with a relentless spate of blind dates, all unerringly from the pages of H.P. Lovecraft. Ads, answered out of desperation, in the New York Review of Books, proved equally futile as the "thirtyish poetess" was sixtyish, the "coed who enjoys Bach and Beowulf" looked like Grendel, and the "Bay Area bisexual" told me I didn't quite coincide with either of her desires. This is not to imply that now and again an apparent plum would not somehow emerge: a beautiful woman, sensual and wise with impressive credentials and winning ways. But, obeying some age old law, perhaps from the Old Testament or Egyptian Book of the Dead, she would reject me. And so it was that I was the most miserable of men. On the surface, apparently blessed with all the necessities for the good life. Underneath, desperately in search of a fulfilling love.

Nights of loneliness led me to ponder the esthetics of perfection. Is anything in nature actually "perfect"? Who am I to demand perfection? I, with my myriad faults, I made a list of my faults, but could not get past: 1) Sometimes forgets his hat.

Did anyone I know have a "meaningful relationship"? My parents stayed together 40 years, but that was out of spite. Greenglass, another doctor at the hospital, married a woman who looked like a Feta cheese "because she's kind." Iris Merman cheated with any man who was registered to vote in the tri-state area. Nobody's relationship could actually be called happy. Soon I began to have nightmares.

I dreamed I visited a singles bar where I was attacked by a gang of roving secretaries. My analyst counseled compromise. My rabbi said, "Settle, settle. What about a woman like Mrs. Blitzstein? She may not be a great beauty, but nobody is better at smuggling food and light firearms in and out of a ghetto." An actress I met, who assured me her real ambition was to be a waitress at a coffee house, seemed promising, but during one brief dinner her single response to everything I said was, "Oh, wow," Then one evening, in an effort to unwind after a particularly trying day at the hospital, I attended a Stravinsky concert alone. During intermission I met Olive Chomsky and my life changed.

Olive Chomsky, literate and wry, who quoted Eliot and played tennis and who never said, "Oh, wow," or wore anything marked Pucci or Gucci or listened to country and western music or dialogue radio. And incidentally, who was always willing at the drop of a hat to do the unspeakable and even initiate it. What joyful months spent with her till my sex drive (listed, I believe, in the Guinness Book of World Records) waned. Concerts, movies, dinners, weekends, endless wonderful discussions of everything from Pogo to Rig-Vheda. And never a gaffe from her lips. Insights only. Wit too! And of course the appropriate hostility toward all deserving targets: politicians, television, facelifts, the architecture of housing projects, men in leisure suits, film courses, and people who begin sentences with "basically." Oh, curse the day that a wanton ray of light coaxed forth those ineffable facial lines bringing to mind Aunt Rifka's stolid visage. And curse the day also that at a loft party in Soho, an erotic archetype with the unlikely name of Tiffany Schmeederer adjusted the top of her plaid wool kneesock and said to me with a voice resembling that of a mouse in the animated cartoons, "What sign are you?" I felt compelled to oblige her with a brief discussion of astrology, a subject rivaling my intellectual interest with such heavy issues as ESP, alpha waves, and the ability of leprechauns to locate gold.

And so it began.

Alibis to Olive. Furtive meetings with Tiffany. Excuses for the woman I loved while my lust was spent elsewhere. Spent, in fact, on an empty little yo-yo whose touch and wiggle caused the top of my head to dislodge like a frisbee and hover in space like a flying saucer. I was forsaking my responsibility to the woman of my dreams for a physical obsession not unlike the one Emil Jannings experienced in The Blue Angel.

Once I feigned illness, asking Olive to attend a Brahms Symphony with her mother so that I could satisfy the moronic whims of my sensual goddess who insisted I drop over to watch "This Is Your Life" on television, "because they're doing Johnny Cash!"

Another time I casually told Olive I was going out to buy the paper. Then I raced seven blocks to Tiffany's, took the elevator up to her floor, but, as luck would have it, the infernal lift stuck. I paced like a caged cougar between floors, unable to satisfy my flaming desires and also unable to return home by a credible time. Released at last by some firemen, I hysterically concocted a tale for Olive featuring myself, two muggers and the Loch Ness monster.

Fortunately, luck was on my side and she was sleeping when I returned home. Olive's own innate decency made it unthinkable to her that I would deceive her with another woman, and while the frequency of our physical relations had fallen off, I husbanded my stamina in such a manner as to at least partially satisfy her. Constantly ridden with guilt, I offered flimsy alibis about fatigue from overwork, which she bought with the guilessness of an angel. In truth, the whole ordeal was taking its toll on me as the months went by. I grew to look more and more like the figure in Edward Munch's "The Scream."

Pity my dilemma! This maddening predicament that afflicts perhaps a good many of my contemporaries. Never to find all the requirements one needs in a single member of the opposite sex. On one hand, the yawning abyss of compromise. On the other, the enervating and reprehensible existence of the amorous cheat. Were the French right? Was the trick to have a wife and also a mistress, thereby delegating responsibility for varied needs between two parties? I knew that if I proposed this arrangement openly to Olive, understanding as she was, the chances were very good I would wind up impaled on her British umbrella. I grew weary and depressed and contemplated suicide. I held a pistol to my head, but at the last moment lost my nerve and fired in the air.

Then one night it all cleared up. Suddenly, and with a clarity one usually associates with LSD, my course of action became apparent. I had taken Olive to see a revival of a Bela Lugosi film at the Elgin. In the crucial scene, Lugosi, a mad scientist, switches the brain of some unlucky victim with that of a gorilla, both being strapped to operating tables during an electrical storm. If such a thing could be devised by a screenwriter in the world of fiction, surely a surgeon of my ability could, in real life, accomplish the same thing.

Well, I won't bore you with the details. Suffice it to say that one dark and stormy night a shadowy figure might have been observed smuggling two drugged women (one with a shape that caused men to drive their cars up on the sidewalk) into an unused operating room at Flower Fifth Avenue. There, as bolts of lightning crackled jaggedly through the sky, he performed an operation done before only in the world of celluloid fantasy.

The result? Tiffany Schmeederer, her mind now existing in the less spectacular body of Olive Chomsky, found herself delightfully free from the curse of being a sex object. As Darwin taught us, she soon developed a keen intelligence, and it did permit her to recognize the follies of astrology and marry happily. Olive Chomsky, suddenly the possessor of a cosmic topography to go with her other superb gifts, became my wife as I became the envy of all around me.

The only hitch was that after several months of bliss with Olive, I inexplicably grew dissatisfied with this dream woman and developed instead a crush on Billie Jean Zapruder, an airline stewardess whose boyish, flat figure and Alabama twang caused my heart to do flipflops. It was at this point that I resigned my position at the hospital, donned my pin wheel hat and knapsack and began skating down Broadway.
```

---

## IC-2456: A Man Named Dave

- Title: A Man Named Dave
- Author (byline): Dave Pelzer
- Work: Not specified
- Publisher: Plume
- Publication date as stated: Sept 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2425
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Pelzer
ISBN: 978-0452281905
Publisher: Plume
Date (Month/Year): Sept 2000
```

### Introduction (context only: never use it for content warnings)

```text
Dave Pelzer was the victim of unbelievable child abuse. His mother denied him food and clothing, locked him in the basement, and told her son she could kill him any time she wanted to – and nearly did. And Dave’s father? He never intervened. By the time Dave was 12, the state had removed him from his home and placed him in foster care. But even years after he was rescued, his life remained a continual struggle. In this scene, Dave tries to reconnect with his dying father. A Man Named Dave by Dave Pelzer
```

### Performance text (classify this)

```text
Nothing could have prepared me for seeing my father. "My father, Stephen Pelzer, he's here? I mean, he's okay and he's in this hospital on this floor. Right?" I blurted out.

Steve, *the nurse*, began to reply but raised a hand to his mouth as if to first collect his thoughts. "Man, we've been waiting on you. Yeah, kid, your father's here, and . . . yeah, he's on this floor. But chill for a sec. There's a few things you need to know."

I rolled my eyes as if to say, Yeah, yeah, come on, out with it. "So . . . I nagged, "What's the deal? What happened? He fell down, broke an arm? What is it? When does he check out?"

My ears picked up the faint sound of a hacking cough. Without thinking, I spun to the right and marched into the room next to the nurses' station. Before me, shaking like a leaf in a flimsy hospital gown, was the skeleton-like figure of my father. He seemed to be using whatever strength he could muster to make it to the bathroom. By the vacant look in his eyes I could tell he had no idea of who I was, or even that someone else was in the room with him. Coming around behind him, I slung his arm around my shoulder and helped him into the bathroom. "Are you all right? Are you okay? Dad," I gently whispered, "it's David. Dad," I said in a firmer tone, "can you hear me?" Father's only response was a raspy exhale. "Dad? Hey, Dad! Can you . . . do you hear me? It's me, David. Say something, anything. Dad?"

"We need to talk," *Steve* said without the slightest trace of embarrassment.

When we were both outside of the room, Steve carefully closed the heavy oak door. "What's wrong with him?" I demanded. "What type of medication do you have him on? How come he doesn't recognize me? Is it the drugs? How long will it be until he gets better and gains some weight? When do you expect him to be released?"

"Hey, man," Steve said, raisng his hand, "give it a rest. “Didn't your mother tell you . . . ? You don't know, do you?"

"Know what? If I knew, I wouldn't be bugging you!" I sarcastically shot back. "Just tell me, what in the heck is going on? Please!" I now begged.

Leading me down the corridor, Steve searched for a more private setting. At the end of the hallway, he stopped to offer me a chair. I refused, feeling the need to stand. "It was about four months ago when your father was admitted - Your father ... he wanted to keep things discreet. Anyway, it was only after we ran all the tests that our diagnosis was confirmed. David, your father has cancer. I'm afraid it's terminal. He's in the advanced stages. I'm sorry." Steve reached out for my hands. "There is nothing we can do. David," Steve said in a deliberate, slow voice, gripping me by the shoulders, "your father ... he's not going to make it. "

"You mean ... you're saying he's going to die? My dad is going to die? No way!" I shook my head in complete denial. "Can't you give him a shot of something ... or I thought there's some kind of chemo treatment. If it's money you need . . . just don't let him die. Not now. Please!" I begged, as if he alone decided the fate of my father.

"David, listen, chill for a sec. I don't know, no one knows exactly how long your father has, but," he emphasized in a strong tone, "the thing I do know for certain is this: your father is not going to make it. And there is nothing, nothing, that you, I, or anyone else can do about it. I am sorry. I truly am."

I simply stood in front of Steve like a zombie. I wanted to release everything and cry. A heartbeat later, I suppressed the urge. "Four months?" I asked incoherently. "You're telling me my dad's been here that long? How long has he been ... like he is now? Why can't he talk? Is he doped up? I mean, he acts like he doesn't even recognize me .... I don't, I just don't understand," I stammered.

"Well," Steve began, sliding a chair for me next to his, "your father checked in a few months ago. Since then his condition has rapidly deteriorated. The growth was primarily centered on the side of his neck, but has since spread to his throat. He is on medication. That is the reason he lacks discernment. If we take him off the 'meds,' his understanding might improve, but the pain would be unbearable."

"So . . . he'll never be able to say anything again? Ever ... ?" I asked as my voice trailed off.

"That is correct. Not any longer," Steve replied, nodding his head.

I still refused to admit I could be losing Father. "SO ... what can I do?" I asked. Why doesn't he look at me? Does he know, I mean, is he capable of knowing I'm even here?"

Steve sighed as if growing tired of my endless stream of questions. "For the most part, it's fifty-fifty at best. He seems more coherent in the morning but, for the most part, no more than a few minutes at a time. He's at the stage when he drifts off quite a bit . . . I know it's a lot to deal with," he stated, shaking his head, "but first things first. Spend time with your father . . . That's priority one. I can walk you through the paperwork and all the other things you need to do when the time comes. For now, just spend time with your dad."

"But ... I, ah, I don't know what to say," I replied. "I mean, he doesn't even know that I'm with him."

“Your father doesn't show it, but he's scared. He knows he's not going to make it. Anything you can do would mean the world to him. He's all alone in there." Steve gently scolded, "You have to do this! Just . . . just reminisce about all those good times you spent together. Keep him 'up.' He'll know."

Yeah, all those good times, I said mockingly to myself. Not knowing what to say or do, I felt paralyzed. For the first time in nearly two years, I finally had the chance to be with my father. As I stared at him, I suddenly realized I knew nothing about him. As long as I could remember, my visits with Father had probably amounted to less than ten, maybe twenty hours together. Without warning tears began to swell in my eyes. "I, ah ... I tried to write. I mean, I wrote ... but I wasn't sure of your address. I'm sorry. I truly am. I didn't know. I would have come sooner. I just didn't know."

I turned away to compose myself. The last thing I wanted was to lose it in front of my father. Out of nowhere, a memory of Father and me, when I was a preschooler, sprang from my mind. I sat on Father's bed while tucking the sheet under his frail back. "You may not remember," I began, "but when I was four, maybe five, all of us went to the Russian River .... Early one evening, after dinner, you stepped out for a walk, and I tagged along behind you. . . . I snuck out and walked behind you, tracing your steps. I had those little Forest Ranger boots, and I tried to keep up while being as quiet as I could. I think I made it five, maybe ten feet away from the cabin, when you heard me. You spun around so fast I thought you were going to bite my head off, but you - You simply extended your giant hand and scooped my fingers into yours .... Then, without a word, you let me walk with you.

"I have to say, as a kid that was pretty cool. At the time, between Ron, Stan, and me, to be able to hog a few minutes alone with you, well, back then that was all I talked about after our walk. It was that summer when I knew that's where I wanted to live. The trees, the river, the smell, those precious moments with you, that's when I knew. Back then, with you, I was safe. Back then you were my superhero; you were my Superman. I know it sounds kinda dumb," I scoffed, "but that was the only time you held my hand. When you wanted to be with me."

"When I was at The House, I remember all those times you'd come home from the fire station for just a few minutes to check in on me. Mother didn't know it, but I made sure I timed your arrival when I was washing the dishes so I could actually see you. Sometimes I got too far behind with my chores and ... well, you know Mother ... I paid the price when you were gone. I knew she'd never allow you to go down to the basement, so I'd wash the dishes over and over until I heard you open the front door." I paused to stare directly into Father's eyes. "You saved me. Even though it was only for a few seconds alone in the kitchen, it made all the difference. Sometimes if you brushed against me, I'd breathe in your Old Spice cologne. You were my invisible force field. I'm just sorry you, the boys-everyone-had to deal with so much crap. I somehow thought I'd be able to make it up to you-to everyone.

"You see, Dad, I knew. I always knew you came back to the house for me. And now, no matter what happens, I'm here for you. No matter what anybody says, I'll protect your honor."

"As a kid, I was always proud of you being a fireman. You looked so cool in your dark blue uniform, it was then that I knew I wanted to be a fireman. Dad, I asked, "Dad, do you ... do ... do you still have your badge? Your fireman's badge?" (to audience) “It’s the only thing he has that showed what he did. After everything, it’s all he has.”

His head continued to twitch, but now more to the right, while his eyes strained as if telling me to look into ... "The closet!" I exclaimed. "You want me to look in the closet?" I jumped from the bed and flung open the door. I gave Father a slight nod before my hands patted down his coat. I felt a small bulge. Without looking I yanked out a small, black-leather casing. Searching his eyes, I understood. I whispered into his ear, praying he could hear me, "As God is my witness, I will protect and keep your badge. I will carry it as a sign of honor."

As Father's grip eased, I could tell he had fallen asleep. Before his fingers could slip away, I kissed his hand. Turning toward the door, I saw Steve.

"He'll be able to rest now. You've made him very happy. He told me months ago, when he checked in, that he wanted you to have it. Today was a good day for your father. A very good day."

TRANSITION: - These words are not in the text of the book: I spent a few days at the hospital, talking to my dad and listening to him too. On the fourth day, when I arrived at the hospital, I met Steve at the entrance to Father’s room.

I knew by Steve's forced smile all I needed to know. "David, you need to understand ... sometimes they can't ... they won't go until they know the ones they love will be fine. He's in pain. You have to tell him you'll be fine. You have to let him go. He won't pass until you do this. Ease his suffering. It's the right thing for him. It's the proper thing to do. He won't pass until ..."

I fled to the far end of the hall, where I found a wooden bench. Clasping my hands together, I prayed. "I've never really asked you for much. And you know what I've been through. I guess I thought I could save him .... So, if you could grant me this ... if there's no way that he can get better ... then take him. Ease his pain and take my dad. Amen." Not knowing what to do next, I wiped away my tears, cleared my mind, and made my way to Father's room.

Standing by his bed, I took Father's trembling hand. From behind my eyes I could feel the pressure build, and fought to bury the pain.

"I, ah, got ... some great news," I lied. "The doctor says everything's gonna be fine ... and that ... they can have you up and outta here real soon." Peering into Father's face, I stated with confidence, "I didn't tell you this before, but I got a home on the Russian River. It's got knotty pine walls and ceilings. A stone fireplace, your own room. It's always warm and sunny. It's on the river, and when the sun goes down, the water's as smooth as glass. At night you can smell the redwood trees ... it's a piece of heaven, Dad. Heaven. And in the summer ... we can go to San Fran and catch a game at Candlestick-just like you always said we'd do. We can be like a real father and son. Just the two of us. Everything's gonna be fine. We can be together ... and live at peace. We got a home, a real home. No more fighting, no more troubles. You just relax and ... I'll take care of you . . . I'll take care of everything."

I broke off when I felt Father's trembling fingers clutch my hand. Never before in my entire life had both of us looked deep into each other. His dark eyes were perfectly clear as they bore into mine. I could somehow feel the immense shame, loneliness, sorrow, and pain in Father's gaze. "I've always been proud of you. You've always been my hero. And as your son, I swear to God, one day I will, I will make you proud. I always have and always will love you, Father. Now you relax ... and I'll meet you at the river."

Then, like so many years ago, as he had that summer when we strolled together at the Russian River, my father winked at me before he slipped away.
```

---

## IC-2457: The Man Who Forgot Ray Bradbury

- Title: The Man Who Forgot Ray Bradbury
- Author (byline): Neil Gaiman
- Work: Shadow Show: All-New Stories in Celebration of Ray Bradbury
- Publisher: William Morrow Paperbacks
- Publication date as stated: July 2012
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2097
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil Gaiman
Book: Shadow Show: All-New Stories in Celebration of
Ray Bradbury
ISBN: 978-0062122681
Publisher: William Morrow Paperbacks
Date (Month/Year): July 2012
```

### Introduction (context only: never use it for content warnings)

```text
Hi! I’m ________________(insert name). I gave you my, umm, you, know, that sheet of paper where you are supposed to write down comments for me and rate and rank my performance today . . . . dang, what’s it called . . . . umm . . . oh, yeah my BALLOT!

Don’t you hate it when you forget the words for simple things? Or you forget people’s names, but can remember absolutely everything else about them. That’s what this selection is about, actually . . .

The Man Who Forgot Ray Bradbury by Neil Gaiman
```

### Performance text (classify this)

```text
I am forgetting things, which scares me.

I am losing words, although I am not losing concepts. I hope that I am not losing concepts. If I am losing concepts, I am not aware of it. If I am losing concepts, how would I know?

Which is funny, because my memory was always so good. Everything was in there. Sometimes my memory was so good that I even thought I could remember things I didn't know yet. Remembering forward . . . I don't think there's a word for that, is there? Remembering things that haven't happened yet. I don't have that feeling I get when I go looking in my head for a word that isn't there, as if someone must have come and taken it in the night.

When I was a young man I lived in a big, shared house. I was a student then. We had our own shelves in the kitchen, neatly marked with our names, and our own shelves in the fridge, upon which we kept our own eggs, cheese, yoghurt, milk. I was always punctilious about using only my own provisions. Others were not so . . . there. I lost a word. One that would mean "careful to obey the rules." The other people in the house were... not so. I would go to the fridge, but my eggs would have vanished.

I am thinking of a sky filled with spaceships, so many of them that they seem like a plague of locusts, silver against the luminous mauve of the night.

Things would go missing from my room back then as well. Boots. I remember my boots going. Or "being gone," I should say, as I did not ever actually catch them in the act of leaving. Boots do not just "go." Somebody "went" them. Just like my big dictionary. Same house, same time period. I went to the small bookshelf beside my face (everything was by my bed — it was my room, but it was not much larger than a cupboard with a bed in it). I went to the shelf and the dictionary was gone, just a dictionary-sized hole in my shelf to show where my dictionary wasn't.

All the words and the book they came in were gone. Over the next month they also took my radio, a can of shaving foam, a pad of notepaper, and a box of pencils. And my yoghurt. And, I discovered during a power cut, my candles.

Now I am thinking of a boy with new tennis shoes, who believes he can run forever. No, that is not giving it to me. A dry town in which it rained forever. A road through the desert, on which good people see a mirage. A dinosaur that is a movie producer. The mirage was the pleasure dome of Kublai Khan.

No . . .

Sometimes when the words go away I can find them by creeping up on them from another direction. Say I go and look for a word — I am discussing the inhabitants of the planet Mars, say, and I realise that the word for them has gone. I might also realise that the missing word occurs in a sentence or a title. The________ Chronicles. My Favourite _________.If that does not give it to me, I circle the idea. Little green men, I think, or tall, dark-skinned, gentle: Dark they were and Golden-eyed . . . and suddenly the word Martians is waiting for me, like a friend or a lover at the end of a long day. I left that house when my radio went. It was too wearing, the slow disappearance of the things I had thought so safely mine, item by item, thing by thing, object by object, word by word.

When I was twelve I was told a story by an old man that I have never forgotten. A poor man found himself in a forest as night fell, and he had no prayer book to say his evening prayers. So he said, "God who knows all things, I have no prayer book and I do not know any prayers by heart. But you know all the prayers. You are God. So this is what I am going to do. I am going to say the alphabet, and I will let you put the words together."

There are things missing from my mind, and it scares me. Icarus! It's not as if I have forgotten all names. I remember Icarus. He flew too close to the sun. In the stories, though, it's worth it. Always worth it to have tried, even if you fail, even if you fall like a meteor forever. Better to have flamed in the darkness, to have inspired others, to have lived, than to have sat in the darkness, cursing the people who borrowed, but did not return, your candle.

I have lost people, though. It's strange when it happens. I don't actually lose them. Not in the way one loses one's parents, either as a small child, when you think you are holding your mother's hand in a crowd and then you look up, and it's not your mother . . . or later. When you have to find the words to describe them at a funeral service or a memorial, or when you are scattering ashes on a garden of flowers or into the sea.

I sometimes imagine I would like my ashes to be scattered in a library. But then the librarians would just have to come in early the next morning to sweep them up again, before the people got there. I would like my ashes scattered in a library or, possibly, a funfair. A 1930s funfair, where you ride the black . . . the black . . . the . . .

I have lost the word. Carousel? Roller coaster? The thing you ride, and you become young again. The Ferris wheel. Yes. There is another carnival that comes to town as well, bringing evil. "By the pricking of my thumbs . . ."

Shakespeare.

I remember Shakespeare, and I remember his name, and who he was and what he wrote. He's safe for now. Perhaps there are people who forget Shakespeare. They would have to talk about "the man who wrote 'to be or not to be'" — not the film, starring Jack Benny, whose real name was Benjamin Kubelsky, who was raised in Waukegan, Illinois, an hour or so outside Chicago. Waukegan, Illinois, was later immortalised as Green Town, Illinois, in a series of stories and books by an American author who left Waukegan and went to live in Los Angeles. I mean of course, the man I am thinking of. I can see him in my head when I close my eyes. I used to look at his photographs on the back of his books. He looked mild and he looked wise, and he looked kind.

He wrote a story about Poe, to stop Poe being forgotten, about a future where they burn books and they forget them, and in the story we are on Mars although we might as well be in Waukegan or Los Angeles, as critics, as those who would repress or forget books, as those who would take the words, all the words, dictionaries and radios full of words, as those people are walked through a house and murdered, one by one: by orang-utan; by pit and pendulum; for the love of God, Montressor . . .

Poe. I know Poe. And Montressor. And Benjamin Kubelsky and his wife, Sadie Marks, who was no relation to the Marx Brothers and who performed as Mary Livingston. All these names in my head. I was twelve.

I had read the books, I had seen the film, and the burning point of paper was the moment where I knew that I would have to remember this. Because people would have to remember books, if other people burn them or forget them. We will commit them to memory. We will become them. We become authors. We become their books.

I am sorry. I lost something there. Like a path I was walking that dead-ended, and now I am alone and lost in the forest, and I am here and I do not know where here is anymore.

You must learn a Shakespeare play; I will think of you as Titus Andronicus. Or you, my friend, you could learn an Agatha Christie novel; you will be Murder on the Orient Express. Someone else can learn the poems of John Wilmot, Earl of Rochester, and you, whoever you are, reading this, you can learn a Dickens book, and when I want to know what happened to Barnaby Rudge, I will come to you. You can tell me.

And the people who would burn the words, the people who would take the books from the shelves, the firemen and the ignorant, the ones afraid of tales and words and dreams and Hallowe'en and people who have tattooed themselves with stories and Boys! You Can Grow Mushrooms in Your Cellar! and as long as your words which are people which are days which are my life, as long as your words survive, then you lived and you mattered and you changed the world and I cannot remember your name.

I learned your books. Burned them into my mind. In case the firemen come to town.

But who you are is gone. I wait for it to return to me. Just as I waited for my dictionary or for my radio, or for my boots, and with as meagre a result.

All I have left is the space in my mind where you used to be.

And I am not so certain about even that.

I was talking to a friend. And I said, "Are these stories familiar to you?" I told him all the words I knew, the ones about the monsters coming home to the house with the human child in it, the ones about the lightning salesman and the wicked carnival that followed him, and the Martians and their fallen glass cities and their perfect canals. I told him all the words, and he said he hadn't heard of them. That they didn't exist.

And I worry.

I worry I was keeping them alive. Like the people in the snow at the end of the story, walking backwards and forwards, remembering, repeating the words of the stories, making them real.

I think it's God's fault.

I mean, he can't be expected to remember everything, God can't. Busy chap. So perhaps he delegates things, sometimes, just goes, "You! I want you to remember the dates of the Hundred Years' War. And you, you remember okapi. You, remember Jack Benny who was Benjamin Kubelsky from Waukegan, Illinois." And then, when you forget the things that God has charged you with remembering, bam. No more okapi. Just an okapi-shaped hole in the world, which is halfway between an antelope and a giraffe. No more Jack Benny. No more Waukegan. Just a hole in your mind where a person or a concept used to be.

I don't know.

I don't know where to look. Have I lost an author, just as once I lost a dictionary? Or worse: Did God give me this one small task, and now I have failed him, and because I have forgotten him he has gone from the shelves, gone from the reference works, and now he only exists in our dreams . . .

My dreams. I do not know your dreams. Perhaps you do not dream of a veldt that is only wallpaper but that eats two children. Perhaps you do not know that Mars Is Heaven, where our beloved dead go to wait for us, then consume us in the night. You do not dream of a man arrested for the crime of being a pedestrian.

I dream these things.

If he existed, then I have lost him. Lost his name. Lost his book titles, one by one by one. Lost the stories.

And I fear that I am going mad, for I cannot just be growing old.

If I have failed in this one task, oh God, then only let me do this thing, that you may give the stories back to the world.

Because, perhaps, if this works, they will remember him. All of them will remember him. His name will once more become synonymous with small American towns at Hallowe'en, when the leaves skitter across the sidewalk like frightened birds, or with Mars, or with love. And my name will be forgotten.

I am willing to pay that price, if the empty space in the bookshelf of my mind can be filled again, before I go.

Dear God, hear my prayer.

A . . . B . . . C . . . D . . . E . . . F . . . G . . .
```

---

## IC-2458: Mario

- Title: Mario
- Author (byline): Simon Rich
- Work: Glory Days, Pgs 15-32
- Publisher: Little, Brown and Company
- Publication date as stated: July 2024
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MARIO, PRINCESS PEACH, KWAME, LUIGI, DR. MARIO
- Teaser before the introduction: Yes
- Spoken words (computed): 1704
- Already set (do not supply): none

### Source block (context only)

```text
Author: Simon Rich
Book: Glory Days, Pgs 15-32
ISBN: 978-0316569002
Publisher: Little, Brown and Company
Date (Month/Year): July 2024
```

### Introduction (context only: never use it for content warnings)

```text
VOICE OVER: 40 years ago, the Mushroom Kingdom was invaded by the Koopa, a tribe of turtles famous for their black magic. The peace-loving Mushroom People were turned into stones and bricks, and the Kingdom fell into ruin. The only one who could undo the magic spell was Princess Peach, daughter of the Mushroom King. Unfortunately, she was in the hands of Bowser, King of the Koopa! It was up to Mario to free Princess Peach.

(chants Free Princess Peach, Free Princes Peach)

Wait . . . You don’t know who Mario is??? 2025 marks the 40th anniversary of the original Super Mario Brothers video game, but Mario isn’t just a video game character — he’s a global icon! He is so famous that even the Prime Minister of Japan dressed up as Mario for the closing ceremony of the 2016 Summer Olympics!

But I’ll give you the inside scoop. Mario’s exciting, "super-fun" life is hitting a very quiet, middle-age crisis. . . Decades of running, jumping, and smashing bricks with his head have taken a toll.

Mario by Simon Rich
```

### Performance text (classify this)

```text
MARIO: It’s-a me, Mario! I was-a working as a plumber in New York when I fell-a down a pipe and landed in the Mushroom Kingdom. Pretty soon, I was-a having all kinds of super-fun adventures, crushing Koopas, dodging hammers, and jumping through castle after castle. It’s-a like my whole life was a game. I’d-a wake up each morning shouting, “Wahoo! Yiiiiippeee! Here we go!”*

MARIO: (Pg 15-32) I’m-a 40 years old. I wasn’t-a really thinking about it much. Just another birthday, right? Then it’s-a like the reality of the thing just hit me. “Mamma mia, I’m-a going to be middle-aged.”

Turning 40 forces you to take-a stock of how you’re doing. And to be honest, I’m-a not doing so great. I guess the best way to explain it is-a to start from the beginning of last week. Basically, I wake up, and it’s-a, like, I can’t-a move my back. Like, at all. So I go to Dr. Mario (no relation) and I’m-a in this tiny room for hours, doing all kinds of tests that I’ve-a never done before, and finally Dr. Mario comes back holding some X-rays, and he says that between the jumping and the running and the smashing the bricks with my head, I’ve-a basically given myself arthritis. And he says, “We need-a to schedule the surgery, Mario.

The one we’ve been-a talking about. To fuse-a your spine. Recovery’s-a going to be brutal, but the alternative is you could-a end up in a wheelchair. You could lose-a your ability to walk.”

And he gives me his card and writes his cell phone number on it, and I’m-a thinking, “Mamma mia, it must be serious if he’s-a giving me his private line.” And I walk out of his office. I check-a my phone and there’s-a, like, 20 missed calls from the Princess. (heavy sigh) I call her back and she starts-a going off on me for being out of touch all day, and I’m about to hang up when she tells me she’s-a been kidnapped by a Koopa. (rolls his eyes)

Lately I’ve started to think she’s been getting kidnapped by Koopas on purpose. The first few times it happened, I was-a, like, “Okay, that’s a weird coincidence.” But then it happened, like, literally thousands more times. (to Princess Peach) “If you know that the Koopas are after the Princess, why do you walk around wearing a crown?”

PRINCESS PEACH: Oh, so you’re saying I was asking for it? Because of the way that I was dressed?

MARIO: You know what? If you want to get-a me canceled, go ahead! (to audience) Honestly, sometimes I fantasize about that since it would give me an excuse to stop. I wouldn’t even do an apology, I’d-a just go off the grid, because at this point I’m-a so tired, I’d just be, like, “Great, I’m out! Wahoo! Yiiiiippeee!” You know?

So anyway, she texts-a me the address of this castle she’s trapped in, and it’s-a, like, seven worlds away. And my back -- I have, at most, like, two days of mobility left before I’m-a going to be paralyzed. (to Princess Peach) I’m-a sorry, but I can’t save you this time.

PRINCESS PEACH: (shocked, then calculating) Guess I’ll call Devon.

MARIO: (to audience) Devon -- he’s-a this DJ who’s, like, 22 at most, super tall and thin, with all the piercings and the neck tattoo. It’s-a like she has this power over me. Still, after all these years. (to Princess Peach) Hey, baby. Relax. It’s-a me, Mario.(to audience) And her voice gets soft, and she asks if I’m-a coming to save her or not. (to Princess Peach) Of course. Just wait on your floating block over the fire. I’ll-a think of something.

So I’m-a frantically searching message boards about back pain, and there’s this miracle device from Europe -- an electronic belt that takes-a all the pressure off your spine. But it’s-a going to cost $10,000. And I’ve-a got, like, 5 coins in my checking account.

I know what you’re-a thinking: “How does Super Mario go broke? You collected entire rooms of coins! What happened?” And the answer is-a simple: I trusted a close personal friend (stage whispers “Yoshi”) to manage-a my money. And I know I deserve-a some of the blame for not catching on, because by the end he had his own island, and safari, and even Yoshi’s World. I mean, this guy got so rich he had his own private world named after him.

There’s-a only one move I can make. I’ve-a got no choice but go see my brother. So, look, here’s-a the deal with Luigi. I’m-a glad he got sober, but now he and his husband, Kwame, does 4 hours of yoga every day. (without excitement) Wahoo. Yippee.

So, I walk up to their fancy gate and ring the stupid intercom: “It’s-a me, Mario.” And Kwame’s, like, “Mario, what a pleasant surprise!” I guess that he’s-a loaded, because Luigi is a professional sunbather now, and their driveway, it’s-a, like, Tesla, Tesla, Tesla. So I tell-a them how the Princess is-a trapped, and I need to buy this spine belt, but I’ve-a got no money—But instead of writing me a check, Kwame says there’s-a “no shame” in aging out of professional rescuing, and it’s-a not too late for me to transition into something less physically demanding. And he hands-a me this book called What Color Is Your Parachute? And Luigi gives me a big thumbs-up, like I’ve-a just won an extra life.

KWAME: What would you say is your most marketable skill?

MARIO: I don’t know, fighting Koopas?

KWAME: We could focus on your combat skills. But I think it might widen the net if we highlight your experience with plumbing. And he writes up this cover letter that’s-a designed to turn “the negative into a positive”:

MARIO: (reading aloud) Dear prospective employer, I am writing to apply for the position of plumber at your company. Plumbing is a lifelong passion of mine. After beginning my career in New York City, I took a multi-year hiatus to the Mushroom Kingdom in order to improve my knowledge of pipes. Now I am ready to jump back in the game. Sincerely, Mario All my adventures, the entirety of my adult life, boils down to a “hiatus”? (to Luigi) Listen, I really appreciate all this great advice, but today the main thing is, I need-a to borrow some money, so I can buy this spine belt and save the Princess from the Koopa.

LUIGI: (long silence, then removes his hat and launches into a rehearsed speech) Mario, we want to help you, but we don’t-a think we’ve-a been helping you in the right way. And that’s-a why, for your sake and ours, we have-a decided to put up some financial boundaries.

MARIO: And as I’m-a hobbling out of their dumb gate, I start to think about my relationship with the Princess. Did I really want to be with her? Or was her love just a [way] to prove-a to myself that I had worth -- That, despite my immigrant background, I was-a still deserving of love? I’d-a been with the Princess for decades, but it’s not like we’d-a ever actually connected. I barely even saw her, except for a few seconds after each rescue, and even then, it’s-a not like we had deep conversations—we just stood next to each other, staring straight ahead, while some text scrolled anticlimactically over our heads, followed by Japanese names.

I pull out Dr. Mario’s card, and call-a his personal number. (on phone) “It’s-a me, Mario. I need help.” (to audience) And within thirty minutes I’m-a in his office signing consent forms for “anterior lumbar interbody fusion.”

DR. MARIO: You’re going to need someone to wash your body and help-a you use-a the bathroom. For the first 12 weeks of recovery you’re-a going to have zero mobility. Do you-a have a partner who can help you?

MARIO: And by now the Princess has straight-up blocked my number. I guess she did end up calling Devon, because she’s-a posting all these pictures on social media, tagged, like, #realhero and #waybetterthanmario. And Dr. Mario, he’s-a walking me through the different options when Luigi jumps through the window. It turns out someone from Dr. Mario’s office called them, because they were-a listed as my emergency contacts.

LUIGI: We knew how much physical pain you were-a in, but we had no idea you were suffering so much emotionally. We love you, and we’re-a with you for the long haul, no matter what it takes.

MARIO: And I’m-a looking up at these guys, because I’ve-a been playing the game for 40 years, but this is the first time that it’s-a me who’s being rescued.

(wipes a tear, beat)

Now it’s-a the night before the surgery, and it’s-a gonna be a long time before I can jump or even walk. And the truth is, I’m-a never going to be “Super Mario” again. I’m-a going to just be plain regular Mario, a middle-aged guy with a slight limp.

But maybe getting older’s not all bad. My whole life I’ve-a struggled with body stuff, like my weight and how I look-a naked. It’s-a why I wear the overalls even when it makes no sense for what I’m doing. Like, why can’t a short fat guy be sexy? (does some sexy moves) I feel-a sexy, and I’m not afraid to say I feel-a sexy. Deal-a with it. (becomes self-conscious and returns to his narrative)

I’m-a ready for the challenge. Like, I really want to do a podcast. We even came up with a name for it (The Next Level with Mario). And Luigi’s going to read-a the commercials, and Kwame’s-a going to be my first guest. (long beat as he reflects) These past 40 years, I’ve-a had all kinds of ups and downs. I’ve-a won and lost, flown and fallen, jumped and been jumped on. I’m-a covered in scars and soon I’ll have some more. But I’m-a not scared. I’m-a ready. Someday, I’ll-a run out of continues, but in the meantime I’ve got plenty of lives left.

Here we go . . .
```

---

## IC-2459: The Martyrdom of Andy

- Title: The Martyrdom of Andy
- Author (byline): Ben Burton
- Work: A 2nd Helping of Chicken Soup for the Soul
- Publisher: HCI
- Publication date as stated: Jan 1995
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1329
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ben Burton
Book: A 2nd Helping of Chicken Soup for the Soul
ISBN: 978-1558743311
Publisher: HCI
Date (Month/Year): Jan 1995
```

### Introduction (context only: never use it for content warnings)

```text
In recent years, bullying and harassment have been grabbing headlines, creating greater awareness. But there’s a dehumanizing experience that is just as common, perhaps even more damaging, and far less well-understood – Ostracism.

It’s a form of social rejection that goes by many names and comes in many flavors. Some call it the “social death penalty.” Whatever you call it, ostracism is a ghastly form of hurt.

You might think bullying is worse than ostracism, but recent research suggests that being frozen out is actually more painful. It is deeply connected to our most fundamental human need to be recognized and accepted. Ostracism can reshape the human brain.

Ben Burton in his confession entitled “The Martyrdom of Andy” recalls his involvement in the exclusion of classmate named Andy and his understanding and remorse as an adult of how he once behaved.
```

### Performance text (classify this)

```text
Andy was a sweet, amusing little guy whom everyone liked yet harassed just because that was the way one treated Andy Drake. He took the kidding well. Andy always smiled back with those great big eyes that seemed to say, “Thank you, thank you, thank you,” with each sweeping blink.

For us fifth graders, Andy was our outlet; he was our whipping boy. He even seemed grateful to pay this special price for membership in our group.

“Andy Drake don’t eat no cake,

And his sister don’t eat no pie.

If it wasn’t for the welfare dole,

All the Drakes would die.”

Andy even appeared to appreciate this sing-song parody of Jack Spratt. The rest of us really enjoyed it, gad grammar and all. I do not know why Andy had to endure this special treatment to deserve our friendship and membership in the group. It just evolved naturally – no plan or discussion.

I don’t recall anyone ever mentioning in this connection that Andy’s father was in prison; or that his mother took in washing and men,; or that Andy’s ankles, elbows and fingernails were always dirty and his old coat was way to big. We soon wore all the fun out of those. Andy never fought back.

Snobbery blossoms in the very young, I guess. It is plain now that the group attitude was that it was our right to belong, but that Andy was a member of our sufferance. Despite all that, we all liked Andy until that day – until that very moment.

“He’s different! We don’t want him, do we?”

Which one of us said it? I have wanted to blame Randolph all these years. But, I cannot honestly say who spoke those trigger words that brought out the savagery lying dormant but so near the surface in all of us. It doesn’t matter who, for the fervor with which we took up the cause revealed us all.

“But I didn’t want to do what we did.” For years I tried to console myself with that. Then one day I stumbled on the unwelcome but irrefutable words that convicted me forever: “The hottest corners of hell are reserved for those who, during a moment of crisis, maintain their neutrality.”

The weekend was to be like others the group had enjoyed together. After school on a Friday we would meet at the home of one of the members – mine this time – for a campout in the nearby woods. Our respective mothers, who did most of the preparation for these safaris, fixed an extra pack for Andy who was to join us after chores.

We quickly made camp, mothers’ apron strings forgotten. With individual courage amplified by the group, we were now “men against the jungle.” The others decided that since it was my party, I should be the one to give Andy the news.

I? I, who had long believed that Andy secretly thought a little more of me than he did the others because of the puppy-like way he looked at me? I who often felt Andy revealing his love and appreciation with those huge, wide-open eyes? I can still plainly see Andy as he came toward me down the long, dark tunnel of trees that leaked only enough of the late afternoon light to kaleidoscope changing patterns on his soiled old sweatshirt.

Andy was on his rusty, one-of-a-kind bike – a girl’s model with sections of garden hose wired to the rims for tires. He appeared excited and happier than I had ever seen him, this frail little guy who had been an adult all his life. I knew he was savoring the acceptance by the In-group; this first chance to belong, to have boy fun, to do boy things.

Andy waved to me as I stood in the camp clearing awaiting him. I ignored his happy greeting. He vaulted off the funny old bike and trotted over toward me, full of joy and conversation. The others, concealed in the tent, were silent but I felt their support.

Why won’t he get serious? Can’t he see that I am not returning his cheer? Can’t he see by now that his euphoria is not reaching me? Then, suddenly, he did see. His innocent countenance opened even more, leaving him entirely vulnerable. His whole demeanor said, “It is going to be very bad, isn’t it, Ben? Let’s have it.”

Well-practiced in facing disappointment, he didn’t even brace for the blow. Andy never fought back.

Incredulously, I heard myself say, “Andy, we don’t want you.”

Hauntingly vivid still is the stunning quickness with which two huge tears sprang into Andy’s eyes and just stayed there; vivid because of a million maddening reruns of that scene in my mind. The way Andy looked at me – frozen for an eternal moment. What was it? It wasn’t hate. Was it shock? Was it disbelief, Or, was it pitty -- for me?

Or forgiveness?

Finally a fleet little tremor broke across Andy’s lips and he turned without appeal, or even a question, to make the long, lonely trip back home in the dark. As I turned and entered the tent, someone—the last one of us to feel the full weight of the moment – started the old doggerel:

“Andy Drake don’t eat no cake,

And his sister . . . . . ”

Then is was unanimous. No vote taken, no word spoken, but we all knew we had done something horribly, cruelly wrong. We were swept over by the delayed impact of dozens of lessons and sermons. Each of us heard perhaps for the first time, “Inasmuch as ye do it unto the least of these . . . . “

In that long, hushed heavy moment we gained an understanding new to us then but indelibly fixed in our minds. We had destroyed an individual made in the image of God with the only weapon for which he had no defense, and we had no excuse, rejection.

Andy’s poor attendance in school made it difficult to tell when he actually withdrew, but one day it dawned on me that he was gone forever. I had spent too many days struggling within myself to find and to polish a proper way of telling Andy how witheringly ashamed and sorry I was, and am. I now know that to have hugged Andy and to have cried with him and even to have joined with him in a long silence would have been enough. It may have healed us both.

I never saw Andy Drake again. I have no idea where he went or where he is, if he is. But to say I haven’t seen Andy is not entirely accurate. In the decades since that autumn day in the Arkansas woods – I have encountered thousands of Andy Drakes. My conscience places Andy’s mask over the face of every disadvantaged person with whom I come in contact. Each stares back at me with the same haunting and expectant look, which became fixed in my mind that day long ago.

Dear Andy Drake,

The chance you will ever see these words is quite remote, but I must try. It is much too late for this confession to purge my conscience of guilt. I neither expect nor want it to. What I do pray for, my little friend of long ago, is that you might somehow learn of, and be lifted by knowing of, the continuing force of your sacrifice. What you suffered at my hands that dreadful day, and the grace you showed in response, has been twisted, turned and molded by God into a blessing. I hope this knowledge might ease the memory of that terrible day for you.

I have been no saint, Andy, nor have I done all the things I could and should have done with my life. But what I yearn for you to know is that I have never again knowingly betrayed an Andy Drake. Nor, I pray, shall I ever.

Love,

Ben
```

---

## IC-2460: Meanwhile, Back at the B Western

- Title: Meanwhile, Back at the B Western
- Author (byline): Patrick F. McManus
- Work: They Shoot Canoes, Don't They?
- Publisher: Owl Books
- Publication date as stated: Sept 1982
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1881
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick F. McManus
Book: They Shoot Canoes, Don't They?
ISBN: 978-0805000306
Publisher: Owl Books
Date (Month/Year): Sept 1982
```

### Introduction (context only: never use it for content warnings)

```text
Sing: Happy Trails to you . . .Until we meet again . . . . Happy Trails to you . . .

In the late ’40s and early ’50s, the Western was escapist entertainment, all half-hour black-and-white adventures about good guys and bad guys. Everything was filmed within 50 miles of Hollywood. The white hat would triumph over the black hat and then sing a song. He had a comic sidekick and his horse had a name: Thunder, Trigger, Hi Ho, Silver! He was always in danger but never really. He was bowling with bumpers. Let’s just face it . . . The West in those days was easier. So saddle up your ponies and ride with me into the past. Meanwhile, Back at the B Western by Patrick F. McManus.
```

### Performance text (classify this)

```text
Few people appreciate the great contribution the handgun has made to television and motion pictures. What would police shows, for example, be without .38 Specials and .357 Magnums? Imagine police detectives standing around the squad room in shirt-sleeves, rifles dangling from under their armpits. Ridiculous!

The shows that would really suffer from an absence of handguns, though, would be the westerns. Without the pistol, there would e no fast draw, and without the fast draw, westerns would be a whole lot different. Consider, if you will, and if you have the stomach for it, a quick-draw scene with rifles. Matt Dillon clumps out into the street from the Long Branch Saloon to issue a warning to one of the quaintly named villains so characteristic of “Gunsmoke.”

“Chester and I caught you red-handed stealing’ buffalo humps up on the flat, Ick Crud,” he says. “You be outta town by sundown if you know what’s good fer ya. Folks her ‘bouts don’t take kindly to buffalo-humpers.”

Ick Crud sneers. “Reach fer yer iron, Marshal!”

The camera zooms in for a close-up of Matt’s low-slung Winchester, the tie-downs knotted around his ankle. Quicker than Dean Martin can sing “Old Man River,” Matt draws . . . and draws . . . and draws. Ick Crud uses a frantic hand-over-hand draw on his Sharps- Borchardt. During the draw, Chester, Doc, and Miss Kitty go back into the Long Branch for a drink to steady their nerves.

“Three whiskeys and be quick about it,” Miss Kitty snaps to the bartender. “Matt’s drawin’ out there in the street, and we ain’t got much time before the shootin’ starts.”

“I don’t know why Matt don’t git outta the marshaling business,” Doc grumbles. “I keep tellin’ him, ‘Matt, sooner or later a gun fighter’s gonna shade your draw by just a minute or two, and that’ll be it fer ya.’”

“We better git back out there,” Chester whines. “They should be just about finished drawin’, and I don’t want to miss the shootin’.”

No doubt about it, the handgun and the fast draw are essential to the true western, and any movie fan worth his hot-buttered popcorn not only expects them to be in the western but knows the ritual by heart. The ritual usually begins with the “call out.” The villain stands in the street and calls out the hero – “C’mon out, Ringo, you yellow-bellied, chicken-livered, varicose-veined, spastic-coloned wimp!”

Upon hearing himself being called out, the hero immediately begins his preparations. He tosses down his shot of whisky and grinds out his cigar on the greasy nose of the belligerent bartender. He slips his pistol out of its holster and checks the cylinder to make sure he reloaded after his last shoot-out. (There is nothing more disappointing than to beat the other fellow to the draw and then discover that you forgot to reload.) He then reholsters his gun and slips it out and in a few times to make sure it isn’t sticking. (A stuck gun is just about as bad as an unloaded one.) Next he unstraps his spurs, his motive here apparently being that, should he change his mind about the fight, it is a lot easier to run when you’re not wearing spurs. He pulls his hat low over his eyes, limbers up the fingers of his gun hand, and trucks his jacket back behind the butt of his revolver. One purpose of all this preparation may be the hope that the villain will get tired of waiting and go home. The villain never does, of course, although sometimes he gets a cramp in his lip from holding a sneer so long.

Back in the olden days when I was a kid, we had what were called the B westerns. The B stood for “best.” These were movies starring Roy Rogers, Gene Autry, and Hopalong Cassidy. They weren’t anything like the westerns nowadays starring Clint Eastwood, the ones where you have to buy a program to tell the good guys from the bad guys. In the B westerns, you always knew the good guys. They were neatly dressed, clean-shaven, and didn’t cuss, smoke, drink, kiss, or do anything else that was bad for health or morals. Even the bad guys didn’t do most of these things, but you could tell them anyway. For one thing, they all used the interrupted curse:

“What the . . . !”

“Well, Ill be . . . !”

“Why you . . . !”

They had real action in the B’s too, not like the “modern” western where you spend half the movie watching Eastwood squint his eyes and ripple his jaw muscles. Clint holsters his gun like he was setting a carton of milk back in a refrigerator. Why, Roy, Gene, and Hoppy wouldn’t even think of putting their guns back into their holsters without giving them a twirl or two first.

I don’t recall seeing Roy, Gene, or Hoppy ever shoot anybody, but they probably did. Usually, they just shot the gun out of the villain’s hand and let it go at that. Sometimes they would rope the bad guys, often getting a single loop of their lasso around the whole gang. Heroes knew their business in the B westerns.

One nice bit of business Roy, Gene, and Hoppy perfected was to leapfrog over the rumps of their horses and land smack in the saddle. They never landed on the saddle horn either, although once I think I heard the Lone Ranger cry out in a shrill voice, “Hii owwwww Silver away!”

My cousin Buck, who was several years older than I and knew everything, told me he was an expert at getting on horses like that and that there really wasn’t anything to it. I said I couldn’t believe that. He said if I had a horse handy he would show me. I said I didn’t have a horse but I had a cow. Would a cow work? He said sure. We went out to the pasture and found a cow engaged in licking a salt block. Buck said that one would do just fine. I suggested that we warn the cow of what to expect, but Buck said that wouldn’t be necessary. As it turned out, Buck was wrong about that and the rest as well. I still think the cow probably would have cooperated and even entered into the spirit of the thing had we just let her know what to expect. As it was, Buck got back twenty yards or so and made a dash for her. At the exact instant he got his hands on the cow’s rump and his legs had crossed over his arms in mid-vault, the cow let out a frightened bellow and bolted forward. As the cow disappeared over a nearby hill, Buck was still perched on her tail bones in a strange variation of the lotus position and screaming, “Whoa, you stupid cow, whoa!”

“Well, I’ll be . . . !” I said.

The B western heroes were big on tricks. Say the villain got the drop on Roy in a little cabin out in the middle of the desert. Just as the baddy was about to plug him, Roy would shout “Watch out!” and point over the other man’s shoulder. The villain would spin around, and Roy would jump him and thump his head to a fare-thee-well. These villains were dumb! Otherwise, why would they expect the guy they were about to gun down to warn them of a surprise attack? They were slow to learn. Roy, Gene and Hoppy would catch them with this little trick movie after movie. Maybe the reason why were so dumb was from getting their heads thumped so often.

Eventually, however, they did start catching on to the trick. “You ain’t foolin’ me with that old trick, Rogers,” the bad guy would say, as if he had seen some of these movies before himself. But this time Gabby Hayes would actually be sneaking up behind him and would thump his head a good one. Again, one might wonder why Roy thought it necessary to warn the villain when his comical sidekick was in fact sneaking up behind the man. The reason, of course, was to complicate matters for the villain when this particular situation arose in future movies. Roy, Gene, and Hoppy all worked half a dozen different ploys of this same routine, always with success. After a while the villain could scarcely get the drop on one of them without instantly becoming a nervous wreck from wondering whether or not he was about to be jumped.

The B western villain was a sucker for pebbles, too. Anytime the hero wanted to draw the baddy’s attention away from himself, he would toss a pebble. The villain would whirl around and empty his six-gun into the pebble. Then he would see that it was only a pebble and would get this worried, expectant look in his eyes, which said, “Head, get ready for a thumping!”

Counting shots was a favorite tactic of B western heroes. They would wave a hat around on a stick or perform some other trick to draw fire, all the time counting shots. Then, suddenly, they would walk right out in the open and announce, “Six! That was your last bullet, Slade!” Villains liked to try this trick too, but having the IQ’s of celery, they could never get it straight. There was scarcely a villain in B westerns who could count to six without making a mistake. “Six,” the bad guy would say, walking out from behind his rock. “That was your last bullet, Autry!”

BANG!

If the movie patron wondered what it was the villain was muttering as he lay sprawled in the dust, it was probably, “Let’s see now, two shots ricocheted off the rock, two went through my hat on the stick, that makes five. . . “

Even among the B Western audiences there were those who counted shots. They counted the number of shots the hero fired without reloading. I hated these wise guys. Right in the tense part of the movie, they would guffaw: “That’s nine shots without reloading! Roy must be using a nine-shooter!”

“Why you . . . !” I would say under my breath. IF there was anyone who couldn’t appreciate a B western, it was a nitpicker.

The last B western I ever saw in a theater was in a small college town in Idaho. It starred Randolph Scott, and in the big scene the baddies had ganged up on Randolph in the saloon. When they started blazing away at him, Randolph jumped behind a cast-iron stove and, if I recall correctly, used the stove lid as a sort of shield while he returned their fire. The theater was filled with college kids and, and as it the nature of college kids, they began whopping and jeering and laughing at Randolph’s plight. Seated just behind me were an old farmer and his wife who had paid their hard-earned $1.50 for an evening of serious entertainment. As the slugs were spanging off the stove like lead hail and the college kids were whooping it up, I heard the old woman whisper nervously to her husband. The farmer, in a gruff but gentle voice, reassured her. “Don’t worry, Mother,” he said, “Ol’ Randolph, he’ll figure a way to get hisself out of this mess.”

You bet! The farmer and his wife were my kind of people.
```

---

## IC-2461: Memoirs of an Imaginary Friend

- Title: Memoirs of an Imaginary Friend
- Author (byline): Matthew Dicks
- Work: Not specified
- Publisher: St. Martin’s Press
- Publication date as stated: August 2012
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: DAD, BUDO, MOM, MAX, TEACHER, TOMMY
- Teaser before the introduction: Yes
- Spoken words (computed): 1707
- Already set (do not supply): none

### Source block (context only)

```text
Author: Matthew Dicks
ISBN: 978-1250006219
Publisher: St. Martin’s Press
Date (Month/Year): August 2012
```

### Introduction (context only: never use it for content warnings)

```text
When I was little, I had a very good friend named ______. He was fearless when I was scared, rebellious when I was obedient and athletic when I was clumsy. He was also entirely imaginary. I can’t remember how I met _______ and I don’t remember the last time I saw him. But I do remember that he inspired me to go on adventures I would not have had the confidence to undertake without him. know.

In 2019, a study by The Telegraph* indicated that children today are too busy with electronic devices to have imaginary friends. And while the loss for the children is clear, consider this same loss from the perspective of imaginary friends who will never be “poofed” into existence.

For ‘Tis better to have loved and lost than never to have loved at all. --Tennyson

Memoirs of an Imaginary Friend by Matthew Dicks
```

### Performance text (classify this)

```text
DAD: (Pg 15-16) (argument takes place in hushed tones so Max doesn’t overhear) I don’t care what the damn therapist thinks. He’s a normal kid . . . he’s just a late bloomer.

BUDO: (Pg 17) (to the audience at normal volume) I think Max’s dad is wrong about Max being a late bloomer. I spend most of the day with Max and I see how he is different from other kids. Max lives on the inside and the other kids live on the outside. Max doesn’t have an outside. Max is all inside.

MOM: (Pg 16) He is not a late bloomer and I wish you’d stop saying that. I know it kills you to admit it, John, but he needs help.

DAD: I just don’t get it. He plays with toys. He plays sports. He has friends.

BUDO: (to the audience) Max’s Dad is not correct. Max doesn’t have any friends. The kids at school either like Max, hate Max or ignore Max, but none of them are his friend. Max is happiest when left alone.

DAD: Why are we trying to fix the poor kid when there’s nothing wrong with him?

MOM: (Pg 17) John, he doesn’t like to hug us. He can’t make eye contact. He talks to himself constantly. He flips out if I switch brands of toothpaste. These are not normal kid behaviors.

BUDO: (Pg 1) (to the audience) My name is Budo. Max’s parents call me an imaginary friend. I am NOT imaginary. (Pg 5) As long as Max believes in me, I exist.

MAX: (Pg 19) They fight because of me. (playing with Legos) (Pg 15) Hand me that blue two-pronger.

BUDO: (to audience) A two-pronger is a kind of LEGO. Max has names for all the LEGO pieces. (to Max) I can’t.

MAX: Oh, yeah. I forgot.

BUDO: (Pg 19-20) [They fight] only because they don’t know what’s best for you. They’re trying to figure out what is right.

MAX: (pause, he looks angry, then sad) When other people try to make me feel better by twisting words, it only makes me feel worse. When you do it, it makes me feel the worst.

BUDO: I’m sorry. I’m sorry that your parents argue about you, even if it’s only because they love you.

MAX: Oh. (a slow, small smile, head tilted to the right) Thanks.

BUDO: (changing the subject) (Pg 15) [So . . . . ] If I’m real, then why are you the only one who can see me?

MAX: (irritated) I don’t know. I think you’re real. Why do you keep asking me?

BUDO: (to audience) Mrs. Hume told Max’s mom that it’s (mimicking Mrs. Hume’s voice) “not uncommon for kids like Max to have imaginary friends, and they tend to persist longer than most imaginary friends.” Persist. I like that word. I persist. (Pg 5) Max imagined me when he was four years old. (proudly) Five years is a very long time for someone like me to be alive. (admires himself in the bedroom mirror) (Pg 3) I’m lucky. Imaginary friends get their appearance from their human friend’s imagination. Max is very creative, so I have two arms, two legs and a face. I’m not missing a single body part. Too much imagination can be bad, though. I once met an imaginary friend named Pterodactyl whose eyes were stuck on the ends of these two gangly, green antennas. *****Scene Change***** Bell Rings

BUDO: (Pg 83) It’s Monday and we are at school) (Pg 139) A school is full of kids. Most of them leave their imaginary friends home. Unless it’s someone like Max, it is hard to talk or play with an imaginary friend when teachers and other kids are around. School is the time when most imaginary friends stop existing. Kindergarten kills them. (Pg 32) I once saw an imaginary friend pop up in Max’s kindergarten classroom for fifteen minutes and then just disappear. It was like someone inflated her in the middle of the room. She got bigger and bigger and bigger like one of those people-shaped balloons they sell at parades. A big, pink girl with pigtails and yellow flowers for feet. But when the story was done, it was like someone popped her with a pin. Fifteen minutes is nothing. [Now Max is in the 3rd grade] (Pg 21) and Max is in the bathroom. He is making a poop. He almost never makes a poop in a public restroom. But it’s 1:15 and there are still two hours of school left and he couldn’t hold it anymore. [My job?] Stand outside the door and warn him if someone is coming. Max hates surprises. He’ll lift his feet off the floor so no one can see him and wait until the bathroom is empty again before he finishes. (Pg 23-24) He never knows what to say when someone knocks on the door when he’s in there. He used to say . .

MAX: Max is pooping!

BUDO: But then he got in trouble when a kid told the teacher what he said. The teacher told Max that it’s not appropriate to say that you’re pooping.

TEACHER: Just say ‘I’m in here’ the next time someone knocks.

MAX: But that sounds silly. The person won’t know who I am. I can’t just say ‘I’m in here.’

TEACHER: (frustrated) Fine, tell them who you are then.

BUDO: So now when someone knocks on the bathroom door, Max says . . .

MAX: Occupied by Max Delaney!

BUDO: (Pg 22) (standing guard outside the bathroom) That’s when I see trouble come walking down the hallway. Tommy Swinden – fifth grade! (passes through the bathroom door to warn Max) (Pg 23) Max! Tommy Swinden is coming! (Max groans) (to audience) His sneakers disappear from the crack between the stall and the floor. Tommy (an obvious bully) enters the bathroom, takes a quick peek under the stalls and sees no feet. Thinks he is alone. Reaches back and pulls his underwear from the crack of his butt.

BUDO: (to audience) I see people do this all the time, because I spend a lot of time with people who think they are alone. It’s called a wedgie and it can’t be too comfortable.

(Pg 24) Tommy stands at the sink, reaches for the faucet and is just about to turn the knob when he hears . . . PLOP! From the stall where Max is hiding. He whirls around, stomps to the 1st stall door and peeks through the crack. He bangs on the stall door hard.

TOMMY: I know you’re in there! I can see you through the crack!

BUDO: (calls out to Max) Don’t say anything, Max! He can’t get in there. He’ll have to leave eventually! (Max squeaks) (to audience) But I’m wrong. Tommy gets down on his hands and knees and peeks his head under the door.

TOMMY: Max the Moron. It’s my lucky day. What’s the matter? Couldn’t hold the last one in?

MAX: (panicked shout) It was already halfway out!

BUDO: Everything about this situation is bad. (Pg 25) Max is trapped in a public bathroom, a place that already frightens him. His pants are wrapped around his ankles and he probably hasn’t finished (whispers) pooping.

But it’s the way Max answered Tommy that scares me the most. There was more than panic in his voice. There was fear. Like when people in the movies see the monster for the first time. He might already be close to getting stuck. (Pg 64) When Max gets stuck, there’s nothing anyone can do for him. He sits with his knees pulled really tight into his chest and rocks back and forth and makes a whining sound. His eyes are open, but they can’t see anything. There’s nothing anyone can do for him.

MAX: (Pg 25) (screeching like a little girl) Occupied by Max Delaney! Occupied by Max Delaney!

BUDO: (Pg 64) (breathes a heavy sigh of relief) There’s no screaming when he is stuck! (Pg 25-26) But I don’t know what to do now. Tommy Swinden is about to crawl under the door and enter the tiny bathroom stall where Max is trapped. If he’s not crying yet, he soon will be. Things stay with Max forever. He never forgets. And even the tiniest things can permanently change him.

TOMMY: Last chance, moron. Open up or I’m coming in!

BUDO: Fight, Max! Fight! Don’t let him in there! (to audience) It’s not a great idea. It’s not smart or even original. It’s just the only thing left to do. I am as stuck as Max has ever been. (anticipatory pause then Tommy screams in disgust)(Budo is in disbelief) The door flies open and Max is standing there, pants nearly pulled up but not buttoned or zipped, his legs straddling Tommy’s head. (to Max) Run! (they both run, Max buttoning and zipping his pants without stopping. Finally, they find a hiding place near the nurse’s office)(out of breath)(Pg 27) What happened to Tommy? What did you do?

MAX: I pooped on his head.

BUDO: (impressed) You pooped with someone else in the bathroom? (to audience) The fact that he pooped on Tommy Swinden’s head is unbelievable, but the fact that he managed to poop in the presence of another human person is even more amazing.

MAX: (matter of factly) Just a little one. I was almost finished when he came in. I pooped this morning, so it was a bonus poop. *****Scene Change*****

BUDO: (Pg 303-304) [So that brings us to today] Max has stopped talking to me. It’s not that he is angry with me. He just doesn’t know that I am around anymore. And when I’m gone, I’ll just be a story that his mom tells him some day. How he once had an imaginary friend named Budo. (Pg 253) The thing I like best about Max is that he is brave. It’s not one thing -- (Pg 305) [Not] bonus poops and Tommy Swinden. (Pg 253) It’s everything. Max is not like any other person in the whole world. Kids make fun of him because he is different. His mom tries to change him, and his dad tries to treat him like he is someone else. Even his teacher, Mrs. Gosk, treats him differently. No one treats him like a regular boy, but everyone wants him to be regular instead of himself. With all that, Max still gets out of bed every morning and goes to school and the park and the bus stop and even the kitchen table. You have to be the bravest person in the world to go out every day, being yourself when no one likes who you are. (Pg 308-309) When I am gone, Mrs. Gosk will have to protect Max. She will have to help him with the bonus poops and Tomy Swinden and all the other little things that Max cannot do because he lives to much of his life on the inside. That big, beautiful inside that one imagined me. . . And she will. I want to be angry at Max for forgetting about me, but I am not. (pause) (Pg 140) It’s strange to be an imaginary friend. You can’t suffocate and you can’t get sick, and you can’t fall and break your head, and you can’t catch pneumonia. The only thing that can kill you is a person not believing in you. That happens more than all the suffocating and bumps and pneumonia combined. (pause) (Pg 309) Death is not scary for me anymore. It is just sad. I just want to watch the little boy who I love so much grow up. I want to know the rest of Max’s story. I hold the image of Max’s face in my mind for as long as I can. (whispers) I love you, Max.
```

---

## IC-2462: Miracle Boy

- Title: Miracle Boy
- Author (byline): Pinckney Benedict
- Work: Prize Stories 1999
- Publisher: Anchor Books
- Publication date as stated: Sept 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2244
- Already set (do not supply): none

### Source block (context only)

```text
Author: Pinckney Benedict
Book: Prize Stories 1999
ISBN: 978-0385493581
Publisher: Anchor Books
Date (Month/Year): Sept 1999
```

### Introduction (context only: never use it for content warnings)

```text
Miracle Boy by Pinckney Benedict
```

### Performance text (classify this)

```text
MIRACLE BOY'S FEET REATTACHED IN EIGHT-HOUR SURGERY. Everybody in school knew, everybody in town. Theirs was not a big town. It had happened a number of years before, but an accident of that sort has a long memory.

Lizard and Geronimo and Eskimo Pie wanted to see the scars. Show us the scars, Miracle Boy, they said. Show us the scars. Lizard and Geronimo and Eskimo Pie knew all about the accident and Miracle Boy's reattached feet. The newspaper headline had named him

Miracle Boy didn't want to show them. He shook his head when they said to him, Show us the scars. He was a portly boy, soft and jiggly at his hips and belly from not being able to run around and play sports like other boys, He was pigeon-toed and wearing heavy dark brogans that looked like they might have some therapeutic value. His black corduroy pants were too long for him and pooled around his ankles. He carried his locust walking stick in one hand.

Miracle Boy's old man was the one who cut Miracle Boy's feet off. He was chopping corn into silage. One of the front wheels of the [tractor] that he was driving broke through the crust of the cornfield into a snake's nest. Copperheads boiled up out of the ground. The tractor nose-dived, heeled hard over to one side, and Miracle Boy slid off the fender where he'd been riding.

Miracle Boy's old man couldn't believe what he had done. He shut off the tractor's power-takeoff and scrambled down from the high seat. He was sobbing. He pulled his boy out of the jaws of the silage chopper and saw that the chopper had taken his feet.

Thinking fast, he put his boy down, gently put his maimed boy down on the ground. He had to sweep panicked copperheads out of the way to do it. He made a tourniquet for one leg with his belt, made another with his blue bandanna that he kept in his back pocket. Then he went up the side of the silage wagon like a monkey. He began digging in the silage. He

Lizard and Geronimo and Eskimo Pie asked him one last time--they were being patient with him because he was a cripple--and then they knocked him down. Eskimo Pie sat on his head while the other two took off his pants and shoes and socks. They tied the laces of the heavy brogans together and pitched them high in the air, so that they caught and dangled from the electric line overhead.

They pinned Miracle Boy to the ground and examined his knotted ankles, the smooth lines of the scars, their pearly whiteness, the pink and red and purple of the swollen, painful-looking skin around them.

Don't look like any miracle to me, said Eskimo Pie. Miracle Boy wasn't fighting them. He was just lying there, looking in the other direction.

It's miracles around us every day, said Miracle Boy. Jesus, he made the lame man to walk, Miracle Boy said. And Jesus, he made me to walk, too.

But you wasn't lame before, Geronimo said. Did Jesus take your feet off just so he could put them back on you?

Miracle Boy didn't say anything more. Lizard and Geronimo and Eskimo Pie noticed then that he was crying. His face was wet, shining with tears and mucus. They saw him bawling, without his shoes and socks and trousers, sprawled in his underpants on the ground,. They were tempted to leave him, but instead they helped him up and retrieved his socks and unknotted his pants and assisted him into them. He was still crying as they did it. They debated briefly whether to go after his shoes, dangling from the power line overhead. In the end, though, they decided that, having set him on his feet again, they had done enough.

Miracle Boy's old man called Lizard's mother on the telephone. He told Lizard's mother what Lizard and Geronimo and Eskimo Pie had done to Miracle Boy. The next day, Miracle Boy's old man came to Lizard's house. He brought Miracle Boy with him. Lizard thought that probably Miracle Boy's old man was going to whip the tar out of him for his part in what had been done to Miracle Boy. He figured Miracle Boy was there to watch the beating.. Instead, Lizard's mother made them sit in the front room together, Lizard and Miracle Boy. She brought them cold Coca-Colas and grilled cheese sandwiches. She let them watch TV.

Geronimo and Eskimo Pie got a hiding from their old man. He used his two-inch-wide black bull-hide belt in his good hand, and he made them take their pants down for the beating, and he made them thank him for every stroke. They couldn't believe it when Lizard told him what his punishment had been. That, Geronimo told Lizard, is the difference between a house with a woman in charge and one with a man.

Lizard saw Miracle Boy's shoes every day, hanging on the electric wire over by McClung's property line, slung by their laces. He kept hoping the laces would weather and rot and break and the shoes would come down by themselves, and that never did. When he was outside the school, his eyes were drawn to them. He figured that everybody in the school saw those shoes. Everybody knew whose shoes they were. Lizard figured that Miracle Boy must see them every day on his way home.

I'm going to go get the shoes, Lizard announced one day to Geronimo and Eskimo Pie.

Miracle Boy's shoes,

You don't want to fool with those, Eskimo Pie said.

Lectrocute yourself, Geronimo said.

Or fall to your doom, Eskimo Pie said.

Lizard didn't say anything more to them. He kept his eyes on the shoes as they moved through their slow oscillation, and he watched the small figure of Miracle Boy, dressed in black like a preacher, bent like a question mark as he moved beneath the shoes, as he bobbed over the fence stile and hobbled across the brittle dead grass of the field beyond.

Lizard made a study of the subject of the shoes. They were hung up maybe a yard out from one of the utility poles, so clearly the pole was the way to go. He had seen linemen scramble up the poles with ease, using their broad climbing slings and their spiked boots, but he had no idea where he could come by such gear.

In the end, he put on the tool belt that his old man had left behind, cinched it tight, holstered his old man's Tiplady hammer, and filled the pouch of the belt with sixtypenny nails. He left the house in the middle of the night, slipping out the window of his bedroom and clambering down the twisted silver maple that grew there. He walked and trotted the four miles down the state highway to the junior high school. His plan was this: to drive one of the sixtypenny nails into the utility pole about three feet off the ground. Then to stand one-footed on that nail and drive in another some distance above it. Then he would stand on the second nail and drive a third, and so on, ascending nail by nail until he reached the humming transformer at the top of the pole. Then, clinging to the transformer, he imagined, he would lean out from the pole and, one-handed, pluck the shoes from the wire, just like taking fruit off a tree.

The first nail went in well and held solid under his weight, and he hugged the pole tight. He fished in the pouch of nails, selected one, and drove it in as well. He climbed onto it. His hands were beginning to tremble as he set and drove the third nail. The next several nails were not hard to sink, and he soon found himself a dozen feet up, clinging to the pole. He straightened his back and fought off a yawn. He was getting tired and wished he could quit the job he had started. And another, and another.

The nail on which Lizard was standing began to give dangerously beneath his weight, and he hurried to make his next foothold. He gripped the utility pole between his knees, clinging hard, trying to take the burden off the surrendering nail as it worked its way free of the wood. A rough splinter stung his thigh. He whacked at the wobbling nail that he held and caught the back of his hand instead, peeling skin from his knuckles. He sucked briefly at the bleeding scrapes and then went back to work, striking the nail with the side of the hammer's head. The heavy nail bent under the force of his blows, and he whimpered at the thought of falling. He struck it again, and the nail bit deep into the pine. Again, and it tested firm when he tugged on it.

He pulled himself up. Resting on the bent nail, he found himself at eye level with the transformer at the pole's top. Miracle Boy's shoes dangled a yard behind him. Lizard felt winded, and he took hold of the transformer. The cold metal cut into the flesh of his fingers. There was deadly current within the transformer, he knew, but still it felt like safety to him. He held fast, shifted his weight to his arms.

He craned his neck farther and found the shoes. Still there. The shoes were badly weathered. To Lizard, they looked a million years old, like something that ought to be on display in a museum somewhere, with a little white card identifying them. SHOES OF THE MIRACLE BOY. The uppers were cracked and swollen, pulling loose from the lowers, and the tongues protruded obscenely.

Lizard put a tentative hand out toward them. Close, but no cigar.

He loosened his grip, leaned away from the pole. The arm with which he clung to the transformer trembled with the effort. He jerked, and the shoes held fast. Jerked again and felt the raveling laces begin to give. A third time, a pull nearly strong enough to dislodge him from his perch, and the laces parted. One shoe other fell to the ground below with a dry thump. He wondered if the sound the shoe made when it hit was similar to the sound he might make.

He tucked Miracle Boy's left shoe beneath his arm and began his descent. [Mustering his courage, he raced to Miracle Boy’s house with the shoes.] Miracle Boy's old man stood behind the closed screen door of his house, his arms crossed over his chest, a cigarette mugged in the corner of his mouth. The hall way behind him was dark. You think my boy wants anything to do with you little bastards?

I don't necessarily want anything to do with him, Lizard said. I just brought him his shoes.

He held out the shoes, but Miracle Boy's old man didn't even look at them.

Your mommy may not know what you are, Miracle Boy's old man said, and his voice was tired and calm. But I do.

Lizard offered the shoes again.

You think he wants those things back? Miracle Boy's old man asked. He's got new shoes now. Different shoes.

Lizard said nothing. He stayed where he was.

Put them down there, Miracle Boy's old man said, nodding at a corner of the porch.

I'm sorry, Lizard said. He held on to the shoes. He felt like he was choking.

It's not me you need to be sorry to.

Miracle Boy appeared at the end of the dark hallway. Lizard could see him past the bulk of his old man's body. He was wearing canary-yellow pajamas. Lizard had never before seen him wear any color other than black.

Daddy? he said. The sleeves of the pi's were too long for his arms, they swallowed his hands, and the pajama legs lapped over his feet. He began to scuff his way down the hall toward the screen door. He moved deliberately. He did not have his walking stick with him, and he pressed one hand against the wall.

His old man kept his eyes fixed on Lizard. Go back to bed, junior, he said in the same tired tone that he had used with Lizard before.

Daddy?

Miracle Boy brushed past his old man, who took a deferential step back. He came to the door and pressed his pudgy hands against the screen. He looked at Lizard with wide curious eyes. He was a bright yellow figure behind the mesh. He was like a bird or a butterfly. Lizard was surprised to see how small he was.

Miracle Boy pressed hard against the door. If it had not been latched, it would have opened and spilled him out onto the porch. He nodded eagerly at Lizard, shyly ducking his head. Lizard could not believe that Miracle Boy was happy to see him. Miracle Boy beckoned, crooking a finger at Lizard, and he was smiling, a strange small inward smile. Lizard did not move. Miracle Boy beckoned again, and this time Lizard took a single stumbling step forward. He held Miracle Boy's ruined shoes in front of him. He held them out before him like a gift.
```

---

## IC-2463: Mr. Big

- Title: Mr. Big
- Author (byline): Woody Allen
- Work: Getting Even
- Publisher: Vintage
- Publication date as stated: Aug 1978
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: KAISER, HEATHER/CLAIRE/ELLEN, WISEMAN, CHICAGO PHIL, SERGEANT REED, THE POPE
- Teaser before the introduction: Yes
- Spoken words (computed): 2189
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: Getting Even
ISBN: 978-0394726403
Publisher: Vintage
Date (Month/Year): Aug 1978
```

### Introduction (context only: never use it for content warnings)

```text
Mr. Big by Woody Allen
```

### Performance text (classify this)

```text
KAISER: I was sitting in my office, cleaning the debris out of my .38 and wondering where my next case was coming from. I like being a private eye, and even though once in a while I've had my gums massaged with an automobile jack, the sweet smell of greenbacks makes it all worth it. Not to mention the dames, which are a minor preoccupation of mine that I rank just ahead of breathing. That's why, when the door to my office swung open and a long-haired blonde named Heather Butkiss came striding in and told me she needed my help, my salivary glands shifted into third.

KAISER: "What can I do for you, sugar?"

HEATHER/CLAIRE/ELLEN: "I want you to find someone for me, Mr. Lupowitz."

KAISER: "Call me Kaiser, sugar. All right, so what's the scam?"

HEATHER/CLAIRE/ELLEN: "God. The Creator, the Underlying Principle, the First Cause of Things, the All Encompassing. I want you to find Him for me."

KAISER: "Why?"

HEATHER/CLAIRE/ELLEN: "That's my business, Kaiser. You just find Him."

KAISER: "I'm sorry, sugar. You got the wrong boy."

HEATHER/CLAIRE/ELLEN: "But why?"

KAISER: "Unless I know all the facts," I said, rising.

HEATHER/CLAIRE/ELLEN: "O.K., O.K.," she said, biting her lower lip.

KAISER: She straightened the seam of her stocking, which was strictly for my benefit, but I wasn't buying any at the moment. "Let's have it on the line, sugar."

HEATHER/CLAIRE/ELLEN: My name is not Heather Butkiss, either. It's Claire Rosensweig and I'm a student at Vassar. Philosophy major. History of Western Thought and all that. I have a paper due January. On Western religion. All the other kids in the course will hand in speculative papers. But I want to know. Professor Grebanier said if anyone finds out for sure, they're a cinch to pass the course. And my dad's promised me a Mercedes if! get straight Xs."

KAISER: I opened a deck of Luckies and a pack of gum and had one of each. Her story was beginning to interest me. Spoiled coed. High IQ and a body I wanted to know better. "What does God look like?"

HEATHER/CLAIRE/ELLEN: "I've never seen Him."

KAISER: "Well, how do you know He exists?"

HEATHER/CLAIRE/ELLEN: "That's for you to find out."

KAISER: "Oh, great. Then you don't know what He looks like? Or where to begin looking?"

HEATHER/CLAIRE/ELLEN: "No. Not really. Although I suspect He's everywhere. In the air, in every flower, in you and I-and in this chair." "Vh-huh."

KAISER: So she was a pantheist. I made a mental note of it and said I'd give her case a try-for a hundred bucks a day, expenses, and a dinner date. She smiled and O.K.'d the deal. We rode down in the elevator together. Outside it was getting dark. Maybe God did exist and maybe He didn't, but somewhere in that city there were sure a lot of guys who were going to try and keep me from finding out. My first lead was Rabbi Itzhak Wiseman, a local cleric who owed me a favor for finding out who was rubbing pork on his hat. I knew something was wrong when I spoke to him because he was scared. Real scared.

WISEMAN: "Of course there's a you-know-what, but I'm not even allowed to say His name or He'll strike me dead, which I could never understand why someone is so touchy aboUt having his name said."

KAISER: "You ever see Him?"

WISEMAN: "Me? Are you kidding? I'm lucky I get to see my grandchildren."

KAISER: "Then how do you know He exists?"

WISEMAN: "How do I know? What kind of question is that? Could I get a suit like this for fourteen dollars if there was no one up there? Here, feel a gabardine-how can you doubt?"

KAISER: "You got nothing more to go on?"

WISEMAN: "Hey-what's the Old Testament? Chopped liver? How do you think Moses got the Israelites out of Egypt? With a smile and a tap dance? Believe me, you don't part the Red Sea with some gismo from Korvette's. It takes power."

KAISER: "So He's tough, eh?"

WISEMAN: "Yes. Very tough. You'd think with all that success He'd be a lot sweeter."

KAISER: "How come you know so much?"

WISEMAN: "Because we're the chosen people. He takes best care of us of all His children, which I'd also like to someday discuss with Him."

KAISER: "What do you pay Him for being chosen?"

WISEMAN: "Don't ask."

KAISER: So that's how it was. The Jews were into God for a lot. It was the old protection racket. Take care of them in return for a price. And from the way Rabbi Wiseman was talking, He soaked them plenty. I got into a cab and made it over to Danny's Billiards on Tenth Avenue. The manager was a slimy little guy I didn't like. Chicago Phil. Forger, bank robber, strong-arm man, and avowed atheist.

CHICAGO PHIL: "The guy never existed, Kaiser. This is the straight dope. It's a big hype. There's no Mr. Big. It's a syndicate. Mostly Sicilian. It's international. But there is no actual head. Except maybe the Pope."

KAISER: "I want to meet the Pope."

CHICAGO PHIL: "It can be arranged," he said, winking.

KAISER: "Does the name Claire Rosensweig mean anything to you?"

CHICAGO PHIL: "No."

KAISER: "Heather Butkiss?"

CHICAGO PHIL: "Oh, wait a minute. Sure. She's that peroxide job with the bazooms from Radcliffe."

KAISER: "Radcliffe? She told me Vassar."

CHICAGO PHIL: "Well, she's lying. She's a teacher at Radcliffe. She was mixed up with a philosopher for a while."

KAISER: "Pantheist?"

CHICAGO PHIL: "No. Empiricist, as I remember. Bad guy. Completely rejected Hegel or any dialectical methodology."

KAISER: "One of those."

CHICAGO PHIL: "Yeah. He used to be a drummer with a jazz trio. Then he got hooked on logical positivism. When that didn't work, he tried pragmatism. Last I heard he stole a lot of money to take a course in Schopenhauer at Columbia. The mob would like to find him-or get their hands on his textbooks so they can resell them."

KAISER: "Thanks, Phil."

CHICAGO PHIL: "Take it from me, Kaiser. There's no one out there. It's a void. I couldn't pass all those bad checks or screw society the way I do if for one second I was able to recognize any authentic sense of Being. The universe is strictly phenomenological. Nothing's eternal. It's all meaningless."

KAISER: I had a beer at O'Rourke's and tried to add it all up, but it made no sense at all. Socrates was a suicide-or so they said. Christ was murdered. Nietzsche went nuts. If there was someone out there, He sure as hell didn't want anybody to know it. And why was Claire Rosensweig lying about Vassar? Could Descartes have been right? Was the universe dualistic? Or did Kant hit it on the head when he postulated the existence of God on moral grounds? Then the phone rang. The voice on the other end was Sergeant Reed of Homi-cide.

SERGEANT REED: "You still looking for God?"

KAISER: "Yeah."

SERGEANT REED: ''An all-powerful Being? Great Oneness, Creator of the Universe? First Cause of All Things?"

KAISER: "That's right."

SERGEANT REED: "Somebody with that description just showed up at the morgue. You better get down here right away."

KAISER: It was Him all right, and from the looks of Him it was a professional job.

SERGEANT REED: "He was dead when they brought Him in."

KAISER: "Where'd you find Him?"

SERGEANT REED: ''A warehouse on Delancey Street."

KAISER: ''Any dues?"

SERGEANT REED: "It's the work of an existentialist. We're sure of that."

KAISER: "How can you te11?"

SERGEANT REED: "Haphazard way how it was done. Doesn't seem to be any system followed. Impulse."

KAISER: ''A crime of passion?"

SERGEANT REED: "You got it. Which means you're a suspect, Kaiser."

KAISER: "Why me?"

SERGEANT REED: "Everybody down at headquarters knows how you feel about Jaspers."

KAISER: "That doesn't make me a killer."

SERGEANT REED: "Not yet, but you're a suspect."

KAISER: Outside on the street I sucked air into my lungs and tried to dear my head. I took a cab over to Newark and got out and walked a block to Giordino's Italian Restaurant. There, at a back table, was His Holiness. It was the Pope, all right. Sitting with tWo guys I had seen in half a dozen police lineups. : "Sit down," he said, looking up from his fettuccine. He held out a ring. I gave him my toothiest smile but didn't kiss it. It bothered him and I was glad. Point for me.

THE POPE: "Would you like some fettuccine?"

KAISER: "No thanks, Holiness. But you go ahead."

THE POPE: "Nothing? Not even a salad?"

KAISER: "I just ate."

THE POPE: "Suit yourself, but they make a great Roquefort dressing here. Not like at the Vatican, where you can't get a decent meal."

KAISER: "I'll come right to the point, Pontiff. I'm looking for God."

THE POPE: "You came to the right person."

KAISER: "Then He does exist?" They all found this very amusing and laughed. The hood next to me said, "Oh, that's funny. Bright boy wants to know if He exists." I shifted my chair to get comfortable and brought the leg down on his little toe. "Sorry." But he was steaming.

THE POPE: "Sure He exists, Lupowitz, but I'm the only one that communicates with Him. He speaks only through me."

KAISER: "Why you, pal?"

THE POPE: "Because I got the red suit."

KAISER: "This get-up?"

THE POPE: "Don't knock it. Every morning I rise, put on this red suit, and suddenly I'm a big cheese. It's all in the suit. I mean, face it, if I went around in slacks and a sports jacket, I couldn't get arrested religion-wise."

KAISER: "Then it's a hype. There's no God."

THE POPE: "I don't know. But what's the difference? The money's good."

KAISER: "You ever worry the laundry won't get your red suit back on time and you'll be like the rest of us?"

THE POPE: "I use the special one-day service. I figure it's worth the extra few cents to be safe."

KAISER: "Name Claire Rosensweig mean anything to you?"

THE POPE: "Sure. She's in the science department at Bryn Mawr."

KAISER: "Science, you say? Thanks."

THE POPE: "For what?"

KAISER: "The answer, Pontiff" I grabbed a cab and shot over the George Washington Bridge. On the way I stopped at my office and did some fast checking. Driving to Claire's apartment, I put the pieces together, and for the first time they fit. When I got there something seemed to be troubling her.

HEATHER/CLAIRE/ELLEN: "God is dead. The police were here. They're looking for you. They think an existentialist did it."

KAISER: "No, sugar. It was you."

HEATHER/CLAIRE/ELLEN: "What? Don't make jokes, Kaiser."

KAISER: "It was you that did it."

HEATHER/CLAIRE/ELLEN: "What are you saying?"

KAISER: "You, baby. Not Heather Butkiss or Claire Rosensweig, but Dr. Ellen Shepherd."

HEATHER/CLAIRE/ELLEN: "How did you know my name?"

KAISER: "Professor of physics at Bryn Mawr. The youngest one ever to head a department there. At the midwinter Hop you get stuck on a jazz musician who's heavily into philosophy. He's married, but that doesn't stop you. A couple of nights and it feels like love. But it doesn't work out because something comes between you. God. Y'see, sugar, he believed, or wanted to, but you, with your pretty little scientific mind, had to have absolute certainty."

HEATHER/CLAIRE/ELLEN: "No, Kaiser, I swear."

KAISER: "So you pretend to study philosophy because that gives you a chance to eliminate certain obstacles. You get rid of Socrates easy enough, but Descartes takes over, so you use Spinoza to get rid of Descartes, but when Kant doesn't come through you have to get rid of him too."

HEATHER/CLAIRE/ELLEN: "You don't know what you're saying."

KAISER: "You made mincemeat out of Leibniz, but that wasn't good enough for you because you knew if anybody believed Pascal you were dead, so he had to be gotten rid of too, but that's where you made your mistake because you trusted Martin Buber. Except, sugar, he was soft. He believed in God, so you had to get rid of God yourself."

HEATHER/CLAIRE/ELLEN: "Kaiser, you're mad!"

KAISER: "No, baby. You posed as a pantheist and that gave you access to Him-if He existed, which he did. He went with you to Shelby's party and when Jason wasn't looking, you killed Him."

HEATHER/CLAIRE/ELLEN: "Who the hell are Shelby and Jason?"

KAISER: "What's the difference? Life's absurd now anyway."

HEATHER/CLAIRE/ELLEN: "Kaiser," she said, suddenly trembling. "You wouldn't turn me in?"

KAISER: "Oh yes, baby. When the Supreme Being gets knocked off, somebody's got to take the rap."

HEATHER/CLAIRE/ELLEN: "Oh, Kaiser, we could go away together. Just the two of us. We could forget about philosophy. Settle down and maybe get into semantics."

KAISER: "Sorry, sugar. It's no dice." She was all tears now. A Venus whose right hand tousled my hair while her left hand had picked up a .45 and was holding it behind my back. I let go with a slug from my .38 before she could pull the trigger, and she dropped her gun and dou-bled over in disbelief.

HEATHER/CLAIRE/ELLEN: "How could you, Kaiser?"

KAISER: She was fading fast, but I managed to get it in, in time. "The manifestation of the universe as a complex idea unto itself as opposed to being in or outside the true Being of itself is inherently a conceptual nothingness or Nothingness in relation to any abstract form of existing or to exist or having existed in perpetuity and not subject to laws of physicality or motion or ideas relating to non-matter or the lack of objective Being or subjective otherness." It was a subtle concept but I think she understood before she died.
```

---

## IC-2464: Mud

- Title: Mud
- Author (byline): Geoffrey Forsyth
- Work: New Sudden Fiction
- Publisher: WW Norton & Company
- Publication date as stated: Jan 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1365
- Already set (do not supply): none

### Source block (context only)

```text
Author: Geoffrey Forsyth
Book: New Sudden Fiction
ISBN: 978-0393328011
Publisher: WW Norton & Company
Date (Month/Year): Jan 2007
```

### Introduction (context only: never use it for content warnings)

```text
The death of anyone especially close to us creates an interruption to the flow of our everyday lives. It takes time to recapture our sense of equilibrium, and our awareness of everyday tasks and responsibilities. How much time a person needs to regain stability is as unique to an individual as their fingerprint. Take, David for instance. He has finally achieved stability after the death of his grandmother, father and wife; only to find that stability threatened in a most unusual way. It’s and average workday. David wakes up to his alarm, showers, brushes his teeth, dresses for work and stops off in the kitchen for a quick cup of coffee . . . . it’s then that everything begins to go very, very wrong. Mud by Geoffrey Forsyth.
```

### Performance text (classify this)

```text
This morning I found my grandmother sitting at the kitchen table. She had been dead almost five years, but here she was now, sitting in my wife’s old seat, covered in mud. I almost didn’t recognize her because the mud had flattened her hair and darkened her normally pale skin. She said it wasn’t easy digging her way out of the grave and that it took most of the night, and wasn’t I going to at least offer her a glass of tomato juice?

“I don’t get it,” I said. “You’re here?”

She said, “Am I going to have to ask twice for that juice?”

While alive, my grandmother’s biggest pet peeve was having to ask twice for something she wanted. I poured her some juice.

“Grandma,” I said. “I hate to say this, but today is not a good day. I have to be at the office early for a meeting, eight sharp. People are counting on me.”

She stared at me, as if the tie I had on was all wrong.

“I have responsibilities and commitments that I can’t get out of. It’s a big day. They need me there today.”

It was then that I heard the television in the living room.

“Who’s watching the television?” I asked.

“Your father,” she said.

“He’s here, too?” I walked into the living room and found him sitting on the couch, mud all over his face and his arms and his hair.

“Dad?” I said. “What are you doing here?”

“Is that any way to greet your father?” he said. Turning to my grandmother, he said: “In seven years he hasn’t seen me, and this is how he greets me?”

“You’re getting mud on his remote, dear,” said my grandmother.

He glared at his mother and rolled his eyes.

“Excuse me, Dad,” I said, “but you’re supposed to be dead.”

He handed me my remote, mud all over the buttons. I held it away from my suit so I wouldn’t get dirty.

“There’s nothing on,” he said.

When my father was alive, he loved watching television. He watched two hours of it before he went to his job at the phone company, then five more hours when he came home. His favorite show was All In The Family. He loved that show. Seeing him there in front of the television, hunched over with his hands resting flat on his stomach, injured me in the best possible way.

“I want to hug you,” I said to my father. “But I have a meeting to get to. I can’t afford to be late.”

“You look sharp, kiddo,” he said. The way he called me kiddo made me forget about work for a second. I had forgotten about kiddo. “Really, kiddo,” he said. “You look like a million bucks.”

“You think so?” I said.

Both of them nodded.

“I’d hug you guys, but I don’t want to ruin my suit, you know?”

“Don’t worry about it,” said Grandma.

“I am worried about it,” I said. “I never got to hug you goodbye, Grams.”

“I was in Cleveland,” she said.

“Still, I wish that I could’ve given you a proper goodbye.”

“It’s O.K.”

“No it isn’t,” I said.

I spread my arms and walked towards her, but she backed away.

“Better not, kiddo,” said my father. “You’ll get dirty.”

“I don’t care,” I said.

I turned to him and tried to throw my arms around his muddy neck, but he backed away from me as well.

“You’ve got a big day ahead of you,” he said. “A really big day.”

The phone rang. It was my boss, reminding me not to forget the reports. He sounded nervous. I asked him if I should bring anything besides the reports. He told me to bring my good sense and my sound judgment and the right frame of mind. Then he hung up.

While I was on the phone, my father and grandmother moved to the couch, tracking mud all over the carpet and the furniture. It tired me to look at it, gathering at their feet.

“I can’t do this,” I said. “Not now.” I didn’t know what exactly I couldn’t do.

“Yes, you can,” said my father. “You can do this.”

He raised his arm, as if he meant to give me a high five, but then he remembered the mud, and folded his arms at his waist.

I gathered all the reports that were stacked on the dining room table and placed them neatly in my briefcase, then buckled it shut.

“I’m so sorry,” I called to them. “I have to leave. I wish that I didn’t, but I have to go now.”

“We understand,” said Grandma. “Don’t you worry, darling.”

“I can’t help it,” I said. “I’m always worry. Always. Always.”

“Take a deep breath,” came a new voice from the study.

It was my wife. Two years ago she died of cancer, but now I heard her voice from the study. I froze. Then I held my briefcase to my chest, wrapped my arms around it, and squeezed.

“Honey,” I said. “Is that you?”

“You bet,” she called back.

“I don’t know how to tell you this,” I said. “But I have to leave.”

“I know,” she said. “You’ve got a big day.”

The next moment held a thoughtful silence.

“I’m not coming in there,” I said finally.

“I know,” she said.

My chest tightened. I wanted to run into the study and throw my arms around her and kiss her mouth and tell her how much I couldn’t stand not having her around, but I knew if I went in there, she’d be covered in mud, too, and I had my life to think about, the life that was, any minute, going to start without me.

I went back into the living room and stood in front of my dead father and grandmother, briefcase still pressed to my chest. My briefcase had become like one of those square cushions that can also be used as a flotation device. Though I stood still, I felt like my legs were kicking.

“Show me the way out of here,” I said.

My father got up and came within a few inches of me, making sure none of his mud touched the sleeves of my blazer. He leaned in, breath smelling like damp earth, and said: “I’m sorry we brought her here. She wasn’t supposed to say anything. That was the deal. She was supposed to listen and not say a thing.”

“It’s O.K.,” I said. “I’m glad she came. I just hate running out like this.”

He nodded, then said, “Follow me.”

I followed him to the front door, bow-legged over the wake of mud, so I wouldn’t get dirty. Last night, after finishing my final report, I had used a half a tin of black Kiwi on my shoes. Buffed them until I thought I could see myself in the leather. I don’t know why, but now the whole idea of rubbing black junk on my shoes to make them look better confounded me. It made me think: does anything really get clean?

My father opened the door. There must have been mica in the mud because his legs sparkled when sunlight entered the room. I thought for a moment that standing there, framed by the doorway, he meant to use his body to wall me in and keep me from going outside, where now I heard birds and passing cars and, every few seconds, the sound of a hammer, rapping in the hollow belly of someone’s garage. But then he moved to the side, and I looked back towards the study, wondering if I should go in there, if it would be wise to go in there on the biggest day of my life. I listened for her, but all I heard was her silence. Her silence gave me a mother of a headache, like someone pounding a nail in the back of my head. If she’d spoken again, I’d have gone to her, but, lucky for me, I think, she didn’t, and what I heard instead was my neighbor’s hammer, calling me out.
```

---

## IC-2465: My Apology

- Title: My Apology
- Author (byline): Woody Allen
- Work: Side Effects
- Publisher: Ballantine Books
- Publication date as stated: Sept 1986
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: AGATHON, ALLEN, SIMMIAS, EXECUTIONER, MESSENGER
- Teaser before the introduction: Yes
- Spoken words (computed): 1196
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: Side Effects
ISBN: 978-0345343352
Publisher: Ballantine Books
Date (Month/Year): Sept 1986
```

### Introduction (context only: never use it for content warnings)

```text
My Apology by Woody Allen
```

### Performance text (classify this)

```text
Of all the famous men who ever lived, the one I would most like to have been is Socrates. Not just because he was a great thinker, because I have been known to have some reasonably profound insights myself, although mine invariably revolve around a Swedish airline stewardesses. No, the great appeal for me of this wisest of all Greeks was his courage in the face of death. His decision was not to abandon his principles, but rather to give his life to prove a point. I personally am not quite as fearless about dying and will, after any untoward noise such as a car backfiring, I leap directly into the arms of the person I am conversing with. In the end, Socrates' brave death gave his life authentic meaning, something my existence lacks totally, although it does possess a minimal relevance to the Internal Revenue Department. I must confess I have tried putting myself in this great philosopher's sandals many times and no matter how often I do, I immediately wind up dozing off and having the following dream. (The scene is my prison cell I am usually sitting alone, working out some deep problem of rational thought like: Can an object be called a work of art if it can also be used to clean the stove? Presently I am visited by Agathon and Simmias.)

AGATHON: Ah, my good friend and wise old sage. How go your days of confinement?

ALLEN: What can one say of confinement, Agathon? Only the body may be circumscribed. My mind roams freely, unfettered by the four walls, and therefore in truth I ask, does confinement exist?

AGATHON: Well, what if you want to take a walk?

ALLEN: Good question. I can't.

(The three of us sit in classical poses, not unlike a frieze. Finally Agathon speaks.)

AGATHON: I'm afraid the word is bad. You have been condemned to death.

ALLEN: Ah, it saddens me that I should cause debate in the senate.

AGATHON: No debate. Unanimous.

ALLEN: Really?

AGATHON: First ballot.

ALLEN: Hmmm. I had counted on a little more support.

SIMMIAS: The senate is furious over your ideas for a Utopian state.

ALLEN: I guess I should never have suggested having a philosopher-king.

SIMMIAS: Especially when you kept pointing to yourself and clearing your throat.

ALLEN: And yet I do not regard my executioners as evil.

AGATHON: Nor do I.

ALLEN: Er, yeah, well ... for what is evil but merely good in excess?

AGATHON: How so?

ALLEN: Look at it this way. If a man sings a lovely song it is beautiful. If he keeps singing, one begins to get a headache.

AGATHON: True.

ALLEN: And if he definitely won't stop singing, eventually you want to stuff socks down his throat.

AGATHON: Yes. Very true.

ALLEN: When is the sentence to be carried out?

AGATHON: What time is it now?

ALLEN: Today?!

AGATHON: They need the jail cell.

ALLEN: Then let it be! Let them take my life. Let it be recorded that I died rather than abandon the principles of truth and free inquiry. Weep not, Agathon.

AGATHON: I'm not weeping. This is an allergy.

ALLEN: For to the man of the mind, death is not an end but a beginning.

SIMMIAS: How so?

ALLEN: Well, now give me a minute.

SIMMIAS: Take your time.

ALLEN: It is true, Simmias, that man does not exist before he is born, is it not?

SIMMIAS: Very true.

ALLEN: Nor does he exist after his death.

SIMMIAS: Yes. I agree.

ALLEN: Hmmm.

SIMMIAS: So?

ALLEN: Now, wait a minute. I'm a little confused. You know they only feed me lamb and it's never well-cooked.

SIMMIAS: Most men regard death as the final end. Consequently they fear it.

ALLEN: Death is a state of non-being. That which is not, does not exist. Therefore death does not exist. Only truth exists. Truth and beauty. Each is interchangeable, but are aspects of themselves. Er, what specifically did they say they had in mind for me?

AGATHON: Hemlock.

ALLEN: (Puzzled) Hemlock?

AGATHON: You remember that black liquid that ate through your marble table?

ALLEN: Really?

AGATHON: Just one cupful. Though they do have a backup chalice should you spill anything.

ALLEN: I wonder if it's painful?

AGATHON: They asked if you would try not to make a scene. It disturbs the other prisoners.

ALLEN: Hmmm ...

AGATHON: I told everyone you would die bravely rather than renounce your principles.

ALLEN: Right, right ... er, did the concept of "exile" ever come up?

AGATHON: They stopped exiling last year. Too much red tape.

ALLEN: Right ... yeah ... (Troubled and distracted but trying to remain self-possessed) I er ... so er ... so-what else is new?

AGATHON: Oh, I ran into Isosceles. He has a great idea for a new triangle.

ALLEN: Right ... right ... (Suddenly dropping all pretense of courage) Look, I'm going to level with you-I don't want to go! I'm too young!

AGATHON: But this is your chance to die for truth!

ALLEN: Don't misunderstand me. I'm all for truth. On the other hand I have a lunch date in Sparta next week and I'd hate to miss it. It's my turn to buy. You know those Spartans, they fight so easily.

SIMMIAS: Is our wisest philosopher a coward?

ALLEN: I'm not a coward, and I'm not a hero. I'm somewhere in the middle.

SIMMIAS: A cringing vermin.

ALLEN: That's approximately the spot.

AGATHON: But it was you who proved that death doesn't exist.

ALLEN: Hey, listen-I've proved a lot of things. That's how I pay my rent. Theories and little observations. A puckish remark now and then. Occasional maxims. It beats picking olives, but let's not get carried away.

AGATHON: But you have proved many times that the soul is immortal.

ALLEN: And it is! On paper. See, that's the thing about philosophy-it's not all that functional once you get out of class.

SIMMIAS: And the eternal "forms"? You said each thing always did exist and always will exist.

ALLEN: I was talking mostly about heavy objects. A statue or something. With people it's a lot different.

AGATHON: But all that talk about death being the same as sleep.

ALLEN: Yes, but the difference is that when you're dead and somebody yells, "Everybody up, it's morning," it's very hard to find your slippers.

(The executioner arrives with a cup of hemlock. He bears a close facial resemblance to the Irish comedian Spike Milligan.)

EXECUTIONER: Ah-here we are. Who gets the poison?

AGATHON: (Pointing to me) He does.

ALLEN: Gee, it's a big cup. Should it be smoking like that? EXECUTIONER: Yes. And drink it all because a lot of times the poison's at the bottom.

ALLEN: (Usually here my behavior is totally different from Socrates' and I am told I scream in my sleep.) No-I won't! I don't want to die! Help! No! Please!

(He hands me the bubbling brew amidst my disgusting pleading and all seems lost. Then because of my innate survival instinct the dream always takes an upturn and a messenger arrives.)

MESSENGER: Hold everything! The senate has re-votedl The charges are dropped. Your value has been reassessed and it is decided you should be honored instead.

ALLEN: At last! At last! They came to their senses! I'm a free man! Free! And to be honored yet! Quick, Agathon and Simmias, get my bags. I must be going. Praxiteles will want to get an early start on my bust. But before I leave, I give a little parable.

SIMMIAS: Gee, that really was a sharp reversal. I wonder if they know what they're doing?

ALLEN: A group of men live in a dark cave. They are unaware that outside the sun shines. The only light they know is the flickering flame of a few small candles which they use to move around.

AGATHON: Where'd they get the candles?

ALLEN: Well, let's just say they have them.

AGATHON: They live in a cave and have candles? It doesn't ring true.

ALLEN: Can't you just buy it for now?

AGATHON: O.K., O.K., but get to the point.

ALLEN: And then one day, one of the cave dwellers wanders out of the cave and sees the outside world.

SIMMIAS: In all its clarity.

ALLEN: Precisely. In all its clarity.

AGATHON: When he tries to tell the others they don't believe him.

ALLEN: Well, no. He doesn't tell the others.

AGATHON: He doesn't?

ALLEN: No, he opens a meat market, he marries a dancer, and dies of a cerebral hemorrhage at forty-two.

(They grab me and force the hemlock down. Here I usually wake up in a sweat and only some eggs and smoked salmon calm me down.)
```

---

## IC-2466: My Brother’s Keeper

- Title: My Brother’s Keeper
- Author (byline): Mike Resnick and Jack Nimershein
- Work: Urban Nightmares (eds: Josepha Sherman and Keith DeCandido)
- Publisher: Baen
- Publication date as stated: Nov 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1454
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mike Resnick and Jack Nimershein
Book: Urban Nightmares (eds: Josepha Sherman and
Keith DeCandido)
ISBN: 978-0671878511
Publisher: Baen
Date (Month/Year): Nov 1997
```

### Introduction (context only: never use it for content warnings)

```text
The phrasing may differ, but the requests are always the same. And it is I who must respond to each summons, answer every request. Such is my duty; such is my curse.Damn! There's another one. Oh, well. No rest for the wicked—yet another idiom steeped in irony. My Brother’s Keeper by Mike Resnick and Jack Nimershein
```

### Performance text (classify this)

```text
Kyle Patton felt extremely satisfied with himself as he swaggered down the sidewalk of West Holland Boulevard. The sun warmed his smiling face. A gentle breeze cooled the sweat from his tan, muscular body. He'd had a good day: a towering three-run homer in the bottom of the sixth inning that turned an anticipated defeat for his high-school baseball team into a surprise victory; the congratulations of his teammates; the gratitude of his coach; the cheers from a hometown crowd; Jenny Firth's promise to reward his heroics later that night with a special “surprise,” provided he could borrow his father's Grand Cherokee and then find a nice, quiet, secluded spot out by Tucker's Pond.

Ripping off that dweeb's Starter jacket behind the bleachers after the game was mere icing on the cake of Kyle's insatiable ego. Of course, it would never fit him. Too small. Every fancy jacket he'd ever peeled off the quivering frame of a skinny underclassman was too small for him to wear. But then, wasn't that the point of the exercise? Who'd be so stupid as to pick on someone his own size? Or bigger? Certainly not Kyle, that was for damned sure.

Kyle was still swaggering, still smiling, when a large hand wrapped itself around his mouth and pulled him, none too gently, into the alleyway that separated Karen's Boutique from The Daily Grind Croissant and Expresso Shoppe. My hand.

“That's a nice jacket you're carrying, kid,” I said. Kyle didn't know me from Adam—excuse me, make that from Cain—but he didn't have any trouble recognizing my threatening tone. (Why should he have? He'd spent endless hours perfecting a similar inflection in his own speech patterns.) “Looks a little small for you, though,” I continued. “I wonder why that is?”

I released Kyle's mouth, grabbed his left shoulder, and spun him around.

“What do you want?” Kyle managed to stammer, stumbling even farther back into the shadows of the cramped alleyway. I'd heard that question so many hundreds, thousands, even millions of times.

“What I want is peace. And He'd grant it to me, if it weren't for punks like you. As long as you and your kind—my kind—exist, I remain here, an eternal balance to the scales. Since I can't have the peace I crave,” I continued, my voice almost a whisper, “I must content myself with the retribution that He insists is my responsibility.” I stepped toward Kyle, feeling the usual combination of rage and resignation welling up within me. “So get ready to cough up the jacket, kid, along with some blood and a couple of teeth from that perfect smile.” * * * *

A coat! Amazing, that the children of today visit harm upon one another over something as inconsequential as a coat. Other trivial objects trigger violence, as well. Last week—or maybe it was last month; Time has very little meaning at this late date—the call came from a playground. I materialized just as one child toppled another from the upper rungs of a ladder attached to a tall metal slide. I heard the smaller child's femur snap as he feel heavily to the asphalt. I saw the satisfaction in the larger child's eyes as he stared down at his victim, a cruel sneer playing across his young face. Those youthful features bore no sign of the innocence normally associated with adolescence, nor the slightest sign of regret for the pain he'd caused. Of course there wasn't. Otherwise, I would not have been summoned—although, now that I reflect upon it, “summoned” is probably not the right word. No disembodied voice issues forth from the heavens, demanding my presence. Rather, I'm drawn to youthful conflict, like a moth to the proverbial flame.

My involvement is implied, not imposed. “Am I my brother's keeper?” Those are the very words I once used; the Bible got that right, anyway.

Give the Old Man credit. He possesses a marvelous sense of irony. Because now that is precisely what I am, what He made me. On my eternal shoulders rests the responsibility for defending those children who are too small, or too weak, or too frightened, or too meek, or too gentle, or too genteel, to defend themselves. A fearful child calls, and I respond. Whenever the big abuse the small, the strong mistreat the weak, I appear—always bigger, always stronger ("More ablebodied,” He once proclaimed, again demonstrating the ironic wit few realize He possesses) to balance the scales.

The specifics of my appearance and abilities change continually, calculated each time to counterbalance the current circumstances, whatever they might be. The pattern of my intervention, however, remains constant. It is always the same. At least it was, until that day at the park.

There were two big kids, almost men, in leather jackets, beating the hell out of a younger boy. I walked over, unseen. “That's enough,” I said.

The larger of the boys turned and landed a roundhouse on my jaw. I didn't flinch. “Don't you know that hurts?” I said, landing the same blow on his chin. He spun like a top, then collapsed. I grabbed the second boy by the throat and held him a few inches above the ground as he gasped for air, and then, for the first time, my eyes fell on the face of his victim.

I set the boy on his feet. “Go!” I said firmly.

“Thank you,” said their victim.

I turned to him, and saw the face I had been sure I would never see again: the clear blue eyes, the perfect nose, the light blond hair.

"You!" I hissed. “That face has haunted me for millennia!” I said. “Every time I struck another child, it was you I was hitting. Every time I sent them running off into the dark, it was you! Why have you come to torment me? Why, after a thousand thousand generations? Why now?”

“I am not here to torment you,” he said in the voice that still haunts my every moment. “You have paid your penalty. It is time to make your peace with God, and to rest.”

“God has sent you?”

“How else could I be having this conversation with you, my brother?”

“And what does He want of me?” I asked.

“Only that you beg Him for His divine forgiveness.”

“I begged Him for that ten million full moons ago,” I said. “When I wandered cold and alone in the land of Nod, I confessed my guilt and asked for His mercy.” I paused. “You see what it got me.”

“Ask Him again,” said my brother. “This time He will listen.”

“Has He no memory of what I said?” I demanded. “Can God not recall my confession and my plea?”

“He is God,” said my brother, as if that answered everything.

“Then go to him and tell Him that He must ask for my forgiveness, for the punishment He gave me is totally out of proportion to the crime I committed.”

“You took my life.”

“Have you any idea how many men have taken the lives of other men? Do they all wander the Earth, meting out punishment to those who perform acts of force? I don't think so, or the world would not be overrun by violence.”

“No,” admitted my brother. “You are the only one. The others have other punishments.”

“So I am the only one condemned to right wrongs and defend the defenseless?”

“It is not a condemnation, my brother. It may have felt like a punishment, but it is a high calling that has cleansed your soul. Otherwise I would not be here to present God's offer.”

I considered his words for a long moment.

“Nonsense,” I said. “We are what we are. You were made a victim, and I was made a killer. If I were not avenging acts of violence, I would be perpetrating them.”

“But this need not be!” protested Abel. “God loves you!”

“If God loves me, I shudder to think what He does to those He merely likes!”

“I shall curse your name as long as I live, Cain!”

“That won't be as long as you think, my brother,” I said, approaching him with a grim smile on my lips.

It was over in a matter of seconds. The police will round up the usual suspects, and they may even convict one of them of my crime, but since I have no true existence, no fingerprints, no thick file in their headquarters, they will never know what truly happened.

Just before I vanished, I felt His voice inside my head: Thou hast broken thy covenant with me, Child of Perdition! From this day forth, until Judgment Day, thou shalt be an outcast to My kingdom, and thy only existence shall be as the Children's Avenger!

Blessing or curse, it all depends on your point of view.
```

---

## IC-2467: My First and Bestest Girlfriend

- Title: My First and Bestest Girlfriend
- Author (byline): Paul Feig
- Work: Kick Me: Adventures in Adolescence, Pgs 54-65
- Publisher: Three Rivers Press
- Publication date as stated: Sept 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1832
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Feig
Book: Kick Me: Adventures in Adolescence, Pgs 54-65
ISBN: 978-0609809433
Publisher: Three Rivers Press
Date (Month/Year): Sept 2002
```

### Introduction (context only: never use it for content warnings)

```text
I want to be perfectly clear up front . . . I have extensively researched this issue and nothing my mother told me is actually true!!

1. It does NOT stunt your growth

2. It does NOT cause blindness.

3. It does NOT cause you to grow hair on your palms.

4. It will NOT drive a person crazy. . . and most

importantly . . .

5. You CANNOT die from it. In fact, all the books say that it is perfectly healthy as long as it does not interfere with relationships with friends and family, or with doing other activities.

But at the time, at age 7, I didn’t know anything!

My First and Bestest Girlfriend by Paul Feig.
```

### Performance text (classify this)

```text
(Pgs 54-65) I met my first real and true girlfriend when I was in the second grade. It turned out to be the beginning of a very long and faithful relationship.

We met in gym class. It was about a month into the new school year when our teacher, Mrs. Handler, informed us that we were going to learn how to climb ropes. Beneath the rope was an extra-thick mat, signaling to us all that severe injury was possible. Mrs. Handler, making it sound simple, informed us that we were to grab the rope and use our hands to propel ourselves upward. She said that as we climbed we should use our thighs to pinch the cord and hold ourselves in place. I watched as each of my friends, both boys and girls, scurried up the rope as if it were the easiest thing in the world. Maybe this wouldn't be so bad, I thought. However, nobody else in the class cried when they got a mosquito bite, either.

When my turn arrived, I approached the rope and awkwardly took it in my hands. The minute I touched that rope, I knew my success was going to depend strictly on how much strength I did or didn't have in my arms and legs. I've never had much upper-body strength, and at age seven I couldn't defeat a newborn baby in an arm-wrestling tournament.

"Just pull yourself up," Mrs. Handler said in an encouraging tone.

I looked up the rope and decided that if I could jump up and grab it, at least I'd be off the mat. I sprang up a few feet and gripped the rope. I immediately wrapped my legs around it and hung on. It felt like I had gotten myself pretty high up, but when I looked down, I saw that I was about one foot off the mat. I readjusted myself so that the rope was firmly pinched between my thighs and started to pull my body up. And to my amazement, I was actually getting up the rope.

And then something happened.

All of a sudden, I felt this strange wave coming over me, a powerful sensation that seemed to be building inside my body but I didn't know from where. It almost seemed to start in my chest and expand outward. I felt it in my butt, in my legs, in my arms . . . but especially in my pants. And the weird thing about it was that it felt good. Better than anything I'd ever felt in my life. The next thing I knew, the entire sensation rushed into my groin area and specifically into my-as the girls who lived next door to me used to call it- "thing." Boom boom boom. Was I having a heart attack? Was this what a stroke was?

"Paul? What are you doing up there? Are you stuck?" Mrs. Handler called up.

" . . . no . . . " was all I could muster.

"Well, either keep going or come back down. People are waiting."

"Uh, okay." The feeling was starting to subside and so I cautiously began to let myself down. As I slid slowly down the rope, it happened again. This time it hit harder and actually made me gasp. I froze again. Another wave of euphoric muscle contractions swept through my midsection. Boom boom boom.

"Paul, I don't know what you're doing but please hurry up."

I got to the bottom of the rope and put my feet on the mat. As I tried to walk away, I almost fell onto the gym floor. My legs felt like Jell-o.

A few hours later at recess, I decided to find out if I was the only one who'd experienced "the rope feeling." I asked my friend Brian if he'd felt anything during his climb.

"My hands really hurt after it" was all he offered up.

"Didn't you feel anything else? Anything that was really good?" I didn't want to get more detailed than that for fear that I would be informed of some life-ending disease that had as its main symptom "an intense, pleasurable sensation when climbing ropes in gym class."

Brian just shrugged at my question. "I didn't feel anything. What did it feel like?"

"I don't know," I said, trying to figure out how to verbalize it. "It was like I was floating or something. It felt really good."

"Huh. I don't know. Maybe you have cancer."

That night, I was watching TV in my usual position, lying on my stomach with my chin on my hands and my legs bent at the knees behind me, my calves and feet slowly moving back and forth. Then something strange happened. The rope feeling started to come back again. I was very surprised and stunned. My brain was now beginning to overload with the joy I was experiencing at the return of my new best friend, "the rope feeling." As the sensation built, my father walked in the room.

"What are you watching?" he asked.

At that moment, I had no idea what I was watching. I was numb with intense feeling as the pounding returned. Boom boom boom.

" ... nothing ... " was all I could get out.

"Well, you shouldn't lie so close to the TV. You're gonna hurt your eyes. Move back."

It was as if the world were conspiring against me. I started to think that maybe what I was feeling was somehow forbidden and so God had sent my father in to put an end to it. But once again, I couldn't move.

"Okay, I'll move in a minute."

"Move now," my dad said impatiently.

I slid myself back and the feeling immediately peaked. I gave a little gasp.

"What's the matter? Did you get a carpet burn?"

I couldn't summon the breath to speak and so just shook my head no.

Whereas bath time used to be an opportunity to make my G.I. Joe perform all sorts of underwater adventures in his Army Jack scuba gear, my time in the tub was now transformed into a quest for knowledge. Re-creation of "the rope feeling" apparently had something to do with pressure or contact between my private area and another surface and movement or friction between them. The bathtub became a virtual testing ground --Shampoo bottles, sponges, washcloths, soap bars, the side of the tub-yes, I'm afraid even GI. Joe was called into duty-but nothing seemed to work. However, as with all great inventors, a breakthrough occurs when one least expects it.

Somehow, through a coincidental sequence of washing with soap and scrubbing certain areas harder than normal, I stumbled across what appeared to be a winning combination. I had cracked the code and found that my discovery worked every single time I performed the same sequence of events. And trust me, I had just test-driven it. Many, many times.

I was now a seven-year-old Clark Kent, possessing an awe-inspiring secret that I would have to hide from the world. Superman never used his powers to rob banks and so I vowed that I would somehow find the strength to keep my new ability in check. But I knew it wouldn't be easy.

Wednesday arrived and I was reunited with my girlfriend, the rope. I was practically trembling with excitement and anticipation as I waited my turn to once again become one with my twenty-five-foot friend.

"Think you can make it all the way this time?" chuckled Mrs. Handler.

I nodded and headed up the rope. At first, nothing was happening. Then, at the ten-foot mark, I once again felt the stirrings that I had spent so much of the past week attempting to re-create. Another few pulls and the religious feeling returned. Boom boom boom.

I froze. Keep moving, I told myself. *But I can't, came another voice.* If I move, it'll stop. *It'll get better, I swear.* It's already about as good as I can handle. *That's what you think.*

Okay, okay, I thought. I'll do it. Muscles locked and tight, head spinning, throat clamped shut, I moved my hands up to pull. Unfortunately, my arms were Jell-o. My stomach suddenly seized into a cramp and my head and shoulders pitched backward. My legs flinched and contracted and the next thing I knew, I was plummeting downward. I heard a girl scream and Mrs. Handler yell "Stand back!" as I thudded heavily onto the mat.

"Maybe climbing the rope isn't your cup of tea, Paul," Mrs. Handler said sympathetically.

That afternoon on the playground, my friend Brian came over to me with urgent news. "Paul, I felt it! On the ropes today!"

"You did?" I wasn't sure if I was pleased or not. I had been leading myself to believe that I was the Chosen, that "the rope feeling" was mine and mine alone, something that Mother Nature had given me to make up for the fact that I was so goofy and girls didn't seem to really like me.

"Yeah. It was weird. It felt really good."

I stared at him for a second, thinking. Should I let him in on the fruits of my bathtub research? I leaned in close to him. "I figured out how to get that feeling without a rope," I said in the same way a guy in prison might tell a fellow inmate about a tunnel he'd been digging for years with a teaspoon. "You can do it in the bathtub."

Brian's eyes went wide and he immediately wanted to know everything. And so I filled him in. He sat, rapt, taking in every detail. I mentioned that shampoo bottles provided an interesting feeling because of the smoothness of their sides when used in conjunction with the soapy bathwater. By the time I finished, I could tell that he might feel that force of nature that makes you run, not walk, home from school and head straight for the bathtub.

The next day, I noticed Brian giving me dirty looks as we passed in the halls before school started. "Thanks a lot,” he said angrily.

"Why? What happened?"

"I got my thing stuck in the shampoo bottle. My mom had to come in and take it off. She's really mad at me now."

"Why did you stick your thing in the bottle?"

"You told me to!"

"No, I didn't. I said to rub it on the side."

"Well, now my mom's making me read the Bible. She says she's even going to make me go to church camp." Brian looked at the ground and shook his head.

Oh, well. At least he didn't tell his mom that I was the one who'd told him how to do it. Brian stood up and started to walk away. . . . "And my mom said I'm not allowed to hang out with you anymore. And she says she wants your phone number so she can call your parents."

Hello, church camp.
```

---

## IC-2468: My First Deer, and Welcome to It

- Title: My First Deer, and Welcome to It
- Author (byline): Patrick F. McManus
- Work: They Shoot Canoes, Don’t They
- Publisher: Macmillan
- Publication date as stated: 1982
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1867
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick F. McManus
Book: They Shoot Canoes, Don’t They
ISBN: 978-0805000306
Publisher: Macmillan
Date (Month/Year): 1982
```

### Introduction (context only: never use it for content warnings)

```text
The picture of a fisherman, his arms spread wide, extolling the size of the "one that got away", has become an over-worked cliché. But for the avid hunter . . it’s deer, not fish that leads the pack in the “way I remember it”good-old boy pastime of one-ups-man-ship. My First Deer, and Welcome to It by Patrick F. McManus will leave you with visual images that will not soon be forgotten!
```

### Performance text (classify this)

```text
For a first deer, there is no habitat so lush and fine as a hunter’s memory. I’m convinced that a first deer not only lives on in the memory of a hunter but thrives there, increasing in points and pounds with each passing year until at last it reaches full maturity, which is to say, big enough to shade a team of Belgian draft horses in its shadow at high noon. It is a remarkable phenomenon and worthy of study.

Not long ago, I was chatting with some of the boys down at Kelly’s Bar & Grill and the talk turned to first deer. It was disgusting. I can stand maudlin sentimentality as well as the next fellow, but I have my limits. Some of those first deer had a mastery of escape routines that would have put Houdini to shame. Most of them were so smart there was some question in my mind as to whether the hunter had bagged a deer or a Rhodes Scholar. And Big! There wasn’t a deer there who couldn’t have cradled a baby grand piano in its rack. All first deer are like that.

Except mine.

I banged the table for attention. “Now,” I said, “I’m going to tell you about a real first deer, not a figment of my senility, not some fossilized hope of my gangling adolescence, but a real first deer.”

Now I could tell from looking at their stunned faces that the boys were upset. There is nothing that angers the participants of a bull session more than someone who refuses to engage in the mutual exchange of illusions, someone who tells the simple truth, unstretched, unvarnished, unembellished, and whole.

“Even though it violates the code of the true sports-person,” I began, “I must confess that I still harbor unkind thoughts for my first deer. True to his form and unlike almost all other first deer, he has steadfastly refused to grow in either my memory or imagination; he simply stands there in original size, peering over the lip of my consciousness, an insolent smirk decorating his pointy face. “

The boys at Kelly’s shrank back in horror at this heresy. “No, don’t tell us!” they said. “Don’t destroy the myth of the first deer!” Unrelenting and with only an occasional pause for a bitter, sardonic cackle to escape my lips, I plunged on with the tale, stripping away layer after layer of myth until at last the truth about one man’s first deer had been disrobed an lay before them in all its grim and naked majesty, shivering and covered with goose bumps.

I began by pointing out what I considered to be one of the great bureaucratic absurdities of all time: that a boy at age fourteen was allowed to purchase his first hunting license and deer tag but was prevented from obtaining a driver’s license until he was sixteen. This was like telling a kid he could go swimming but to stay away from the water. Did the bureaucrats think that trophy mule deer came down from the hills in the evening to drink out of your garden hose? This meant that in order to get up to the top of the mountain where the trophy mule deer hung out, I had to start out at four in the morning if I wanted to be there by noon. I remember one time when I was steering around some big boulders in the road and a Jeep with two hunters in it came plowing up behind me. I pulled over so they could pass. The hunters grinned at me as they went by. You’d think they’d never before seen anyone pedaling a bike twenty miles up the side of a mountain to go deer hunting.

I had rigged up my bike especially for deer hunting. There were straps to hold my rifle snugly across the handlebars, and saddlebags draped over the back fender to carry my gear. The back fender had been reinforced to support a sturdy platform, my reason for this being that I didn’t believe the original fender was stout enough to support a buck when I got one. Deer hunting on a bike was no picnic.

A mile farther on and a couple of hours later I came to where the fellows in the Jeep were busy setting up camp with some other hunters. Apparently, someone told a fantastic joke just as I went pumping by because they all collapsed in a fit of laughter and were doubled over and rolling on the ground and pounding trees with their fists. They seemed like a bunch of lunatics to me, and I hoped they didn’t plan on hunting in the same area I was headed for. I couldn’t wait to see their faces when I came coasting easily back down the mountain with a trophy buck draped over the back of my bike.

As luck would have it, just as I was unstrapping my rifle from the handlebars, a buck mule deer came dancing out of the brush not twenty yards away from me. Now right then I should have known he was up to no good. He had doubtless been lying on a ledge and watching me for hours as I pumped my way up the mountain. He had probably even snickered to himself as he plotted ways to embarrass me.

All the time I was easing the rifle loose from the handlebars, digging a shell out of my pocket, and thumbing it into the rifle, the deer danced and clowned and cut up all around me, smirking the whole while. The instant I jacked the shell into the chamber, however, he stepped behind a tree. I darted to one side, rifle at the ready. He moved to the other side of the tree and struck his head out just enough so I could see him feigning a yawn. As I moved up close to the tree, he did a rapid tiptoe to another tree. I heard him snort with laughter. For a whole hour he toyed with me in this manner, enjoying himself immensely. Then I fooled him, or at least so I thought at the time. I turned and started walking in a dejected manner back toward my bike, still watching his hiding place out of the corner of my eye. He stuck his head out to see what I was up to. I stepped behind a small bush and knelt as if to tie my shoe. Then, swiftly I turned, drew a bead on his head, and fired. Down he went.

I was still congratulating myself on a fine shot when I rushed up to his crumpled form. Strangely, I could not detect a bullet hole in his head, but one of his antlers was chipped and I figured the slug had struck there with sufficient force to do him in. I pictured in my mind the joyous welcome I would receive when I came home hauling in a hundred or so pounds of venison. Then I discovered my knife had fallen out of its sheath during my frantic pursuit of the dear. Instant anguish! The question that nagged my waking moments for years afterwards was: Did the deer know that I had dropped my knife? Had I only interpreted it correctly, the answer to that question was written all over the buck’s face – he was still wearing that stupid smirk.

“Well,” I told myself, “what I’ll do is just load him on my bike, haul him down to the lunatic hunters’ camp, and borrow a knife from them to dress him out with.” I thought this plan particularly good in that it would offer me the opportunity to give those smart alecks a few tips on deer hunting.

Loading the buck on the bike was much more of a problem than I had expected. When I draped him crosswise over the platform on the rear fender, his head and front quarters dragged on one side and his rear quarters on the other. Several times as I lifted and pulled and hauled, I thought I heard a giggle, but when I looked around nobody was there. It was during one of these pauses that a brilliant idea occurred to me. With herculean effort, I managed to arrange the deer so that he was sitting astraddle of the platform, his four legs splayed out forward and his head drooping down. I lashed his front feet to the handlebars, one on each side. Then I slid up onto the seat ahead of him, draped his head over my right shoulder, and pushed off.

I must admit that riding a bike with a deer on behind was a good deal more difficult than I had anticipated. Even though I pressed down on the brake for all I was worth, or wobbling descent was much faster than I would have like. The road was narrow, twisting, and filled with ruts and large rocks, with breathtaking drop-offs on the outer edge. When we came hurtling around a sharp, high bend above the hunters’ camp, I glanced down. Even from that distance I could see their eyes pop and their jaws sag as they caught sight of us.

What worried me most was the hill that led down to the camp. As we arrived at the crest of it, my heart, liver, and kidneys all jumped in unison. The hill was much steeper than I had remembered. It was at that point that the buck gave a loud, startled snort.

My first deer had either just regained consciousness or been shocked out of his pretense of death at the sight of the plummeting grade before us. We both tried to leap free of the bike, but he was tied on and I was locked in the embrace of his front legs.

When we shot past the hunters’ camp, I was too occupied at the moment to get a good look at their faces. I probably would have been able o get the bike stopped sooner and with fewer injuries to myself if I had had enough sense to tie down the deer’s hind legs. As it was, he started flailing wildly about with them and somehow managed to het his hooves on the pedals. By the time we reached the bottom of the mountain he not only had the hang of pedaling but was showing considerable talent for it. He also seemed to be enjoying himself immensely. We zoomed up and down over the rolling foothills with the deer pedaling wildly and me shouting and cursing and trying to wrest control of the bike from him. At last he piled us up in the middle of a farmer’s pumpkin patch. He tore himself loose from the bike and bounded into the woods, all the while making obscene gestures at me with his tail. I threw the rifle to my shoulder and got off one quick shot. It might have hit him too, if the bike hadn’t been still strapped to the rifle.

“Now that, is how to tell about a first deer – a straightforward factual report unadorned by a lot of lies and sentimentality.”
```

---

## IC-2469: My Flamboyant Grandson

- Title: My Flamboyant Grandson
- Author (byline): George Saunders
- Work: In Persuasion Nation
- Publisher: Riverhead Books
- Publication date as stated: April 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1645
- Already set (do not supply): none

### Source block (context only)

```text
Author: George Saunders
Book: In Persuasion Nation
ISBN: 978-1594489228
Publisher: Riverhead Books
Date (Month/Year): April 2006
```

### Introduction (context only: never use it for content warnings)

```text
My Flamboyant Grandson by George Saunders
```

### Performance text (classify this)

```text
I had brought my grandson to New York to see a show. Because what is he always doing, up here in Oneonta? Singing and dancing, sometimes to my old show-tune records, but more often than not to his favorite CD, "Babar Sings," sometimes even making up his own steps, which I do not mind, or rather I try not to mind it. Although I admit that once, coming into his room and finding him wearing a pink boa while singing, in the voice of the Old Lady, "I Have Never Met a Man Like That Elephant," I had to walk out and give it some deep thought and prayer.

What I prayed was: Dear Lord, he is what he is, let me love him no matter what. If he is a gay child, God bless him; if he is a non-gay child who simply very much enjoys wearing his grandmother's wig while singing "Edelweiss" to the dog, so be it, and in either case let me communicate my love and acceptance in everything I do.

Where is a child to go for unconditional love, if not to his grandfather? He has had it tough, in my view, with his mother in Nevada and a father unknown, raised by his grandmother and me in an otherwise childless neighborhood, playing alone in a tiny yard that ends in a graveyard wall. The boys in his school are hard on him, as are the girls, as are the teachers.

Then one day I had a revelation. If the lad likes to sing and dance, I thought, why not expose him to the finest singing and dancing there is? So I called 1-800- CULTURE, got our Promissory Voucher in the mail, and on Teddy's birthday we took the train down to New York.

As we entered the magnificent lobby of the Eisner Theatre, I was in good spirits, when suddenly we were stopped by a stern young fellow who said, We are sorry, sir, but you cannot be admitted on merely a Promissory Voucher, are you kidding us, you must take your Voucher and your Proof of Purchases from at least six of our Major Artistic Sponsors, such as AOL, such as Coke, and go at once to the Redemption Center, on Forty-fourth and Broadway, to get your real actual tickets, and please do not be late, as latecomers cannot be admitted,

Well, this was news to me, but I was not about to disappoint the boy.

We left the Eisner and started up Broadway, the Everly Readers in the sidewalk reading the Everly Strips in our shoes, the building-mounted mini-screens at eye level showing images reflective of the Personal Preferences we'd stated on our monthly Everly Preference Worksheets, the numerous Cybec Sudden Emergent Screens outthrusting or down-thrusting inches from our faces, and in addition I could very clearly hear the sound-only messages being beamed to me and me alone via various Kakio Aural Focussers, such as one that shouted out to me between Forty-second and Forty-third, "Mr. Petrillo, you chose Burger King eight times last fiscal year but only two times thus far this fiscal year, please do not forsake us now, there is a store one block north

So that was fun, that was very New York, but what was not so fun was, by the time we got through the line at the Redemption Center, it was ten minutes until showtime, and my feet had swollen up the way they do shortly before they begin spontaneously bleeding, which they have done ever since a winter spent in the freezing muck of Cho-Bai, Korea. It is something I have learned to live with. If I can sit, that is helpful. If I can lean against something, also good. Best of all, if I can take my shoes off. Which I did, leaning against a wall.

And standing beside me was our little Teddy, tiny and sad, whose grandfather could not even manage to get him into one crummy show.

So I said to myself, Get off the wall, old man, blood or no blood, just keep the legs moving and soon enough you'll be there. And off we went, me hobbling, Teddy holding my arm, making decent time, and I think we would have made the curtain. Except suddenly there appeared a Citizen Helper, who asked were we from out of town, and was that why, via removing my shoes, I had caused my Everly Strips to be rendered Inoperative?

I have no problem with the concept of the Everly Strip. That is not why I had my shoes off. I am as patriotic as the next guy. Rather it was due to my bleeding feet.

I told all this to the Citizen Helper, who asked if I was aware that, by rendering my Strips Inoperative, I was sacrificing a terrific opportunity to Celebrate My Preferences?

And I said yes, yes, I regretted this very much.

He said he was sorry about my feet, he himself having a trick elbow, and that he would be happy to forget this unfortunate incident if I would only put my shoes back on and complete the rest of my walk extremely slowly, looking energetically to both left and right, so that the higher density of Messages thus received would compensate for those I had missed.

And I admit, I was a little short with that Helper, and said, Young man, these dark patches here on my socks are blood, do you or do you not see them?

Which was when his face changed and he said, Please do not snap at me, sir, I hope you are aware of the fact that I can write you up?

And then I made a mistake. I brought out a twenty and, leaning over, said, Look, please, the kid just really wants to see this show.

Which is when he pulled out his pad and began to write!

Now, even being from Oneonta, I knew that being written up does not take one or two minutes, we would be standing there at least half an hour, after which we would have to go to an Active Complaints Center, where they would check our Strips for Operability and make us watch that corrective video called "Robust Economy, Super Moral Climate!," which I had already been made to watch three times last winter, when I was out of work and we could not afford cable. And we would totally miss "Babar Sings"!

Well, there I was, in my socks, there was Teddy, with a scared look in his eyes I hadn't seen since his toddler days. So I made a quick decision, and seized that Citizen Helper's ticket pad and flung it into the street, shouting at Teddy, Run! Run!

And run he did. And run I did, and soon I was handing our tickets to the same stern theatre fellow, who was now less stern, and in we went, and took our seats, as the stars appeared overhead and the Eisner was transformed into a nighttime jungle.

And let me tell you, from that moment everything changed for Teddy. I am happy to report he has joined the play at school. He wears a scarf everywhere he goes, throwing it over his shoulder with what can only be described as bravado, and says, whenever asked, that he has decided to become an actor. This from a boy too timid to trick-or-treat! This from the boy we once found walking home from school in tears, padlocked to his own bike! There are no more late-night crying episodes, he no longer writes on his arms with permanent marker, he leaps out of bed in the morning, anxious to get to school, and dons his scarf, and is already sitting at the table eating breakfast when we come down.

When an Everly Reader is reading, then suddenly stops, it is not hard to trace, and within a week I received a certified letter setting my fine at one thousand dollars, and stating that, in lieu of the fine, I could elect to return to the originating location of my infraction (they included a map) and, under the supervision of that Citizen Helper, retrace my steps, shoes on, thus reclaiming a significant opportunity to Celebrate My Preferences.

This, to me, is not America.

What America is, to me, is a guy doesn't want to buy, you let him not buy, you respect his not buying. A guy has a crazy notion different from your crazy notion, you pat him on the back and say hey, pal, nice crazy notion, let's go have a drink.

But do the math: a day's pay, plus train ticket, plus meals, plus taxis to avoid the bleeding feet, still that is less than one thousand.

So down I went.

That Citizen Helper said he was glad about my change of heart. Every time a voice shot into my ear, telling me things about myself I already knew, every time a celebrity hologram walked up like an old friend, Rob checked a box on my Infraction Correction Form and said, Isn't that amazing, Mr. Petrillo, that we can do that, that we can know you so well, that we can help you identify the things you want and need? And I would say, Yes that is amazing.,

As for Teddy, as I write this it is nearly midnight and he is tapping in the room above. He watches the same musical fifteen times in a row. He looks like no one else, acts like no one else, his clothes are increasingly like plumage, late at night he choreographs using plastic Army men, he fits no mold and has no friends, but I believe in my heart that someday something beautiful may come from him.
```

---

## IC-2470: My Speech to the Graduates

- Title: My Speech to the Graduates
- Author (byline): Woody Allen
- Work: The Insanity Defense
- Publisher: Random House Trade Paperbacks
- Publication date as stated: 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1241
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: The Insanity Defense
ISBN: 978-0812978117
Publisher: Random House Trade Paperbacks
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
Nobody listening to President Obama--or, say, Lady Gaga-- give a commencement address is likely to be bored, but, let’s face it: While graduation is exciting, most graduation speeches can put a crowd to sleep. How many people actually remember who gave the address at their own graduation ceremonies, much less anything specific that was said, beyond the generic “this is the first moment of the rest of your life” message? But there are some classes who get lucky, and are graced with a speaker who says something remarkably memorable, either because it is profound rather than sappy, or because it is really funny, or, because it is profound and funny at the same time. In "Side Effects", Woody Allen wrote a short funny piece called, "My Speech to the Graduates." Not a speech he ever actually delivered but quite entertaining and completely memorable!
```

### Performance text (classify this)

```text
More than any other time in history, mankind faces a crossroads. One path leads to despair and utter hopelessness. The other, to total extinction. Let us pray we have the wisdom to choose correctly. I speak, by the way, not with any sense of futility, but with a panicky conviction of the absolute mean-inglessness of existence which could easily be misinterpreted as pessimism. It is not. It is merely a healthy concern for the predicament of modern man. (Modern man is here defined as any person born after Nietzsche's edict that "God is dead," but before the hit recording "I Wanna Hold Your Hand. ") This "predicament" can be stated one of two ways, though certain linguistic philosophers prefer to reduce it to a mathematical equation where it can be easily solved and even carried around in the wallet.

Put in its simplest form, the problem is: How is it possible to find meaning in a finite world given my waist and shirt size? This is a very difficult question when we realize that science has failed us. True, it has conquered many diseases, broken the genetic code, and even placed human beings on the moon, and yet when a man of eighty is left in a room with two eighteen-year-old cocktail waitresses nothing happens. Because the real problems never change. After all, can the human soul be glimpsed through a microscope? Maybe-but you'd definitely need one of those very good ones with two eyepieces. We know that the most advanced computer in the world does not have a brain as sophisticated as that of an ant. True, we could say that of many of our relatives but we only have to put up with them at weddings or special occasions. Science is something we depend on all the time. If I develop a pain in the chest I must take an X-ray. But what if the radiation from the X-ray causes me deeper problems? Before I know it, I'm going in for surgery. Naturally, while they're giving me oxygen an intern decides to light up a cigarette. The next thing you know I'm rocketing over [New York City (suggested replacement for The World Trade Center] in bed clothes. Is this science? True, science has taught us how to pasteurize cheese. And true, this can be fun in mixed company-but what of the H-bomb? Have you ever seen what happens when one of those things falls off a desk accidentally? And where is science when one ponders the eternal riddles? How did the cosmos originate? How long has it been around? Did matter begin with an explosion or by the word of God? And if by the latter, could He not have begun it just two weeks earlier to take advantage of some of the warmer weather? Exactly what do we mean when we say, man is mortal? Obviously it's not a compliment.

Religion too has unfortunately let us down. Miguel de Unamuno writes blithely of the "eternal persistence of consciousness," but this is no easy feat. Particularly when reading Thackeray. I often think how comforting life must have been for early man because he believed in a powerful, benevolent Creator who looked after all things. Imagine his disappointment when he saw his wife putting on weight. Contemporary man, of course, has no such peace of mind. He finds himself in the midst of a crisis of faith. He is what we fashionably call "alienated." He has seen the ravages of war, he has known natural catastrophes, he has been to singles bars. My good friend Jacques Monod spoke often of the randomness of the cosmos. He believed everything in existence occurred by pure chance with the possible exception of his breakfast, which he felt certain was made by his housekeeper. Naturally belief in a divine intelligence inspires tranquility. But this does not free us from our human responsibilities. Am I my brother's keeper? Yes. Interestingly, in my case I share that honor with the Prospect Park Zoo. Feeling godless then, what we have done is made technology God. And yet can technology really be the answer when a brand new Buick, driven by my close associate, Nat Zipsky, winds up in the window of Chicken Delight causing hundreds of customers to scatter? My toaster has never once worked properly in four years. I follow the instructions and push two slices of bread down in the slots and seconds later they rifle upward. Once they broke the nose of a woman I loved very dearly. Are we counting on nuts and bolts and electricity to solve our problems? Yes, the telephone is a good thing-and the refrigerator-and the air conditioner. But not every air conditioner. Not my sister Henny's, for instance. Hers makes a loud noise and still doesn't cool. When the man comes over to fix it, it gets worse. Either that or he tells her she needs a new one. When she complains, he says not to bother him. This man is truly alienated. Not only is he alienated but he can't stop smiling.

The trouble is, our leaders have not adequately prepared us for a mechanized society.

Unfortunately our politicians are either incompetent or corrupt. Sometimes both on the same day. The Government is unresponsive to the needs of the little man. Under five-seven, it is impossible to get your Congressman on the phone. I am not denying that democracy is still the finest form of government. In a democracy at least, civil liberties are upheld. No citizen can be wantonly tortured, imprisoned, or made to sit through certain Broadway shows. And yet this is a far cry from what goes on in the Soviet Union. Under their form of totalitarianism, a person merely caught whistling is sentenced to thirty years in a labor camp. If, after fifteen years, he still will not stop whistling, they shoot him. Along with this brutal Fascism we find its handmaiden, terrorism. At no other time in history has man been so afraid to cut into his veal chop for fear that it will explode. Violence breeds more violence and it is predicted that by [1990 *change this date] kidnapping will be the dominant mode of social interaction. Overpopulation will exacerbate problems to the breaking point. Figures tell us there are already more people on earth than we need to move even the heaviest piano. If we do not call a halt to breeding, by the year [2000 *change this date] there will be no room to serve dinner unless one is willing to set the table on the heads of strangers. Then they must not move for an hour while we eat. Of course energy will be in short supply and each car owner will be allowed only enough gasoline to back up a few inches.

Instead of facing these challenges we turn instead to distractions like drugs and sex. We live in far too permissive a society. Never before has pornography been this rampant. And those films are lit so badly! We are a people who lack defined goals. We have never learned to love. We lack leaders and coherent programs. We have no spiritual center. We are adrift alone in the cosmos wreaking monstrous violence on one another out of frustration and pain. Fortunately, we have not lost our sense of proportion. Summing up, it is clear the future holds great opportunities. It also holds pit-falls. The trick will be to avoid the pitfalls, seize the opportunities, and get back home by six o'clock.
```

---

## IC-2471: Naked Mole Rat Gets Dressed

- Title: Naked Mole Rat Gets Dressed
- Author (byline): Mo Willems
- Work: Not specified
- Publisher: Hyperion Books for Children
- Publication date as stated: Jan 2009
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, MOLE RAT 1, MOLE RAT 2, MOLE RAT 3, WILBUR, MOLE RAT 4, GRAND-PAH
- Teaser before the introduction: Yes
- Spoken words (computed): 470
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mo Willems
ISBN: 978-1423114376
Publisher: Hyperion Books for Children
Date (Month/Year): Jan 2009
```

### Introduction (context only: never use it for content warnings)

```text
I believe that we are not all meant to be the same; look the same, think the same. There is no one right way to show up in the world. Our individual, unique, varied expressions of life are beautiful.

George Bernard Shaw once said: “There are those that look at things the way they are, and ask why? I dream of things that never were, and ask why not?

Why not? Why not, indeed? Do clothes hurt anyone? In the infamous words of RuPaul: “We’re all born naked and the rest is . . . ”

Naked Mole Rate Gets Dressed by Mo Willems
```

### Performance text (classify this)

```text
NARRATOR: There is so much to learn about the fascinating little creatures known as naked mole rats. But for this story you only need to know three things: 1) They are a little bit rat. 2) They are a little bit mole. 3) They are ALL naked. Well, they were, with one exception . . .

NARRATOR: Wilbur the naked mole rat who liked to get dressed. (Wilbur inspects his attire in a large floor length mirror and adjusts his tie) When the other naked mole rats saw him, they said:

MOLE RAT 1: Eeeeeeewwww!

MOLE RAT 2: Yuck!

MOLE RAT 3: What are you doing?

WILBUR: I like clothes. When I get dressed, I can be . . . fancy, or funny, or cool, or I can just be an astronaut.

(Wilbur assumes the demeanor of each description)

NARRATOR: When the others heard that, they said:

MOLE RAT 1: Eeeeeewwww!

MOLE RAT 2: Yuck!

MOLE RAT 3: If you like clothes so much, then why don’t you open a store or something?!

NARRATOR: Naked mole rats can be very sarcastic . . . But Wilbur thought that was a great idea. (Wilbur pantomimes opening a glorious clothing store and showing off his wares to all the mole rats) The other naked mole rats did not. (Grumbling, they haul Wilbur away from the store) They brought Wilbur to a giant portrait of Grand-pah, the oldest, greatest and most naked naked mole rate ever. (assume a stately pose that would be hilarious if naked)

MOLE RAT 1: Look at that picture!

MOLE RAT 2: Look at his heroic face!

MOLE RAT 3: Look at his regal bearing!

MOLE RAT 4: Look at his total lack of clothing!

WILBUR: (to audience) Grand-pah did look heroic. Grand-pah did look regal. (to the other mole rats) But he would also look heroic and regal in a casual shirt and some summer slacks.

MOLE RAT 1: Ugh! Don’t you get it?

MOLE RAT 2: NAKED MOLE RATS DON’T WEAR CLOTHES!

WILBUR: Why not?

NARRATOR: Something had to be done. The naked mole rats marched right over to Grand-pah and told him all about Wilbur.

MOLE RAT 3: And then he asked “Why not?!”

NARRATOR: Grand-pah was very wise. (Grand-pah thinks and thinks) He thought seriously about everything he had heard. (Grand-pah hmmms and hahhhhss) Then he thought some more.

GRAND-PAH: (in a heroic, regal voice) Gather the colony! I shall make a proclamation!

MOLE RAT 1: (excited) A proclamation!

MOLE RAT 2: (racing to tell everyone) A proclamation!

MOLE RAT 3: (in utter awe) A proclamation!

NARRATOR: When Wilbur heard about Grand-pah’s proclamation, he knew it was serious. But he had no idea what to wear. (Wilbur begins trying on different outfits, hats, ties, jackets. shoes) In the end, Wilbur decided to play it safe. (Wilbur takes off all his clothes except for his socks)

(The mole rats are fixated on Wilbur’s socks, whispering and pointing – they are not happy) The others were so busy looking at Wilbur’s socks that no one noticed Grand-pah enter, until he cleared his throat and proclaimed . . .

GRAND-PAH: (clearing his throat, adjusting his jacket, hat and tie) Fellow naked mole rats! I had never worn clothes until I heard Wilbur’s simple question: Why not? Why not, indeed? Do clothes hurt anyone? No. Are they fun? Well, they may not be for everyone, but this old naked mole rate wishes he had tried getting dressed earlier!

NARRATOR: Then Grand-pah complimented Wilbur on his socks. As fast as his legs could take him, Wilbur rushed home, put on his favorite outfit and dashed back! (actor pantomimes as narrator speaks) When he returned, Wilbur discovered he was not alone.

MOLE RAT 1: (curtsy’s in a party dress)

MOLE RAT 2: (puts on some sunglasses and begins to moonwalk)

MOLE RAT 3: (crosses arms and refuses to join in the with the “dressed”)

MOLE RAT 4: (pops an eye patch into place and draws a sword) [ARGH!]

NARRATOR: Much has been said about that day, but for this story, you only need to know three things: 1) Some of the mole rats were naked. 2) Some of the mole rats were clothed. 3) All of the mole rats had a great time. No exceptions!

WILBUR: Why not?
```

---

## IC-2472: Never Been Dissed – Until Now

- Title: Never Been Dissed – Until Now
- Author (byline): Shad Powers
- Work: Chicken Soup for the Teenage Soul III
- Publisher: HCI Teens
- Publication date as stated: April 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1418
- Already set (do not supply): none

### Source block (context only)

```text
Author: Shad Powers
Book: Chicken Soup for the Teenage Soul III
ISBN: 978-0439237314
Publisher: HCI Teens
Date (Month/Year): April 2000
```

### Introduction (context only: never use it for content warnings)

```text
Growing up is not about when you get a driver's license or when you can legally drink or even when you get married or have your first child. Growing up happens every single time you think for yourself make choices and take ownership of the outcomes of those choices. It’s a balancing act between the “what IS” and “what OUGHT to be.” Some people never seem to quite make it, others of us are force to grow up way too fast. Never Been Dissed – Until Now takes a quick snap-shot of a growing up experience in the life of one teen-age boy.
```

### Performance text (classify this)

```text
What can I say? Sometimes I’m a little dumb. I consider Cheetoes a major food group. I play air guitar. I think burping is funny. And worst of all, I screwed up my chance with Darcy by listening to a bunch of other jerks who were just as clueless as me.

Darcy was kinda like the Jewel CD I loved. I played that thing over and over on the way to school, but the second I pulled into the parking lot, it got stuffed under my seat for, uh, safekeeping and replaced with the Beastie Boys.

Imagine me confessing to my friends that I, captain of the basketball team, was dating Darcy, captain of the debate team. Believe me, I didn’t plan on falling for the school brain. But I was blown away by the first words she ever spoke to me.

“Uh, are you lost? This is the li-brar-y. The gym is on the other side of the school, remember?” she said, enunciating the words like she was talking to a toddler. Ouch.

Even though we went to the same school, Darcy and I lived in completely different worlds. She spent her time with the Net nerds, and I roamed the halls like Moses parting the Red Sea of fans who worshipped the guys on my team. I was totally knocked for a loop when she broke the silence.

“Books. I need a book,” I stammered, suddenly unable to remember my assignment. She pointed to a row of books on Thomas Edison – just the man I was looking for – and before I could turn to thank her, she was gone.

When I did catch up with her again, she was on her tippy toes reaching for an encyclopedia in the next aisle. “Need a ladder? Or how ‘bout some platforms?” I asked, giving her a taste of her own sarcasm.

“How about giving me a hand?” she replied. “Oh, that’s right. Books are square, not round like a basketball. Think you can hold one?” Cha-ching! This girl has guts, I thought. When I started laughing, Darcy totally cracked up and started snort-laughing. The number-two pencils holding up her hair were shaking.

“I can’t believe I said that to you. I can’t believe you’re laughing. This is so surreal,” she laughed. “Oh, sorry, that’s a big word. Do you need a dictionary?” More laughing, more snorting. We went on like that for a while, ripping on each other until I thought my sides would split.

For the rest of the day – okay, the rest of the week – every time I thought about her, I felt the same gut-socking, dizzy feeling I get before a big game. Then I found myself taking different routes to get to class just to see if I’d bump into her, and when I did . . . doh! We didn’t say a word to each other, but the joke was still going. I’d innocently make gorilla noises, and she’d die laughing. Or she’d take off her glasses and bump into walls, sending her books, pen and protractor flying everywhere. She taped Brain Gum to my locker. I glued a pair of sweaty gym socks to hers. Two weeks into our secret game, Darcy asked me out. Correction: she blackmailed me into a date. I found a ransom note in my locker saying that if I ever wanted to see my lucky jockstrap again, I’d better meet her at a nearby coffee shop. What guy wouldn’t love a girl with that sense of humor?

After that first date, we spent nearly every day together talking about everything – cheesy Kung Fu movies (our shared obsession), how I hated being judged as a jock despite my 3.5 GPA, why I hadn’t lost my virginity – all of the things I could never talk about with the guys or would even thing about mentioning to any of the other girls I had dated. Then again, Darcy wasn’t like anyone I had ever been with before. She was a lot of firsts for me. She was the first girl who had the guts to ask me out. She was the first girl I didn’t judge by her bra size or reputation. She was the first person who made me feel I had more to offer the world than a killer turnaround jumper. She was the first girl I dated who didn’t obsess about her hair, her weight or what she was wearing. And she was the first girl I didn’t blab about in the locker room when the guys started bragging about their weekend conquests.

It didn’t take long for everyone to start wondering why I was flaking on basketball practice or missing the weekly Duke Nukem marathons at Kyle’s. I had been making up the lamest excuses to cover for hanging out with Darcy and was feeling pretty skanky about it when the guys confronted me about it. So I told them about her.

“Who?” Steve aske.

“Not the girl in overalls and hightops?” Eric asked.

“Why are you wasting time on that?” Kyle asked.

I sat there as they teased me about slumming with a “geeky chick,” assuming that once they exhausted all of their lame jokes about Darcy, they’d move onto their next target. Wrong. After that day, whenever I told them I was doing stuff with Darcy, they unloaded on her again. At first, I didn’t let it bother me. Then one morning, Dave asked, “Have you figured out how to get her to wear a bag over her head to the prom yet?” That really pissed me off and eventually the little things turned into big things, like “accidentally” forgetting to tell me about practice or suddenly not having enough room at the lunch table for me.

After a few weeks of getting the cold shoulder from my friends, I started to doubt my own judgment. Darcy wasn’t one of the prettiest girls in school. Was I actually planning to take her to my senior prom? She’d probably wear number-two pencils in her hair and those hideous hightops. Once I finished picking her apart, I was convinced she was totally wrong for me. Darcy didn’t like basketball or my friends. She refused to go to any of the team parties. I’d been blowing off practices to be with her, and my game was totally suffering. In my mind, the relationship was doomed.

I tried to be subtle at first by taking different routes to my classes to avoid her. I’d promise to call her but never did. She finally cornered me in the hall one day and demanded an explanation, so I swore I’d meet her after school. Then I blew her off. I was hoping she’d get the hint and go away if I flaked, but she didn’t let me off that easily. The next day, in front of the entire school, Darcy let me have it. She yelled at me, called me a coward, a jerk and an idiot, and, worst of all, tossed my friends a box of notes I’d written to her. I stood there speechless as they read each on aloud and laughed like hyenas. The funny thing was that for the first time (another first with Darcy) I didn’t really care what the guys were saying or who saw me standing there like an idiot, because I knew she was right. When I looked at my friends howling and high-fiving each other, I finally realized that I was going to be the first guy in our pathetic circle to grow up.

I wish I could say there was a happy ending to the story, that I begged Darcy to take me back and she did, but it didn’t happen. Well, at least not the part about her taking me back. I begged. I pleaded. I stuffed notes in her locker. I followed her around school. I was practically stalking her by the time I realized it was too late. She had already gotten over slumming with a dummy.

Last I heard, Darcy graduated early and got accepted to an out-of-state college. I still feel a little sad when I think about her and what could have been, but I’m also grateful that I learned what I did, when I did. I know a little bit more about who I am – the whole me, not just the big man on campus part – and who I can be, regardless of what my friends think or say. So, Darcy . . . . Thanks.
```

---

## IC-2473: Nigger: An Autobiography

- Title: Nigger: An Autobiography
- Author (byline): Dick Gregory
- Work: Not specified
- Publisher: Simon and Schuster Adult Publishing
- Publication date as stated: May 1976
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1821
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dick Gregory
ISBN: 978-0671735609
Publisher: Simon and Schuster Adult Publishing
Date (Month/Year): May 1976
```

### Introduction (context only: never use it for content warnings)

```text
Richard Claxton Gregory was born on Columbus Day, 1932. A welfare case. You’ve seen him on every street corner in America. You knew he had rhythm by the way he snapped his cloth while he shined your shoes. Happy little black boy, the way he grinned and picked your quarter out of the air. Then he ran off and bought himself a Twinkie Cupcake, a bottle of Pepsi-Cola, and a pocketful of caramels. You didn’t know that was his dinner. And you never followed him home. . . .

Nigger: An Autobiography by Dick Gregory
```

### Performance text (classify this)

```text
Page 209

This is a revolution. It started long before I came into it, and I may die before it’s over, but we’ll bust this thing and cut out this cancer. America will be as strong and beautiful as it should be, for black folks and white folks. We’ll all be free then, free from a system that makes a man less than a man, that teaches hate and fear and ignorance.

You didn’t die a slave for nothing, Momma. You brought us up. You and all those Negro mothers who gave their kids the strength to go on, to take that thimble to the well while the whites were taking buckets. Those of us who weren’t destroyed got stronger, got calluses on our souls. And now we’re ready to change a system, a system where a white man can destroy a black man with a single word. Nigger.

When we’re through, Momma, there won’t be any niggers any more.

Page 25 - 32

Like a lot of Negro kids, we never would have made it without our Momma. When there was no socks to go with the shoes, no hope to go with tomorrow, she’d smile and say: “We ain’t poor, we’re just broke.” Poor is a state of mind you never grow out of, but being broke is just a temporary condition. She always had a big smile, even when her legs and feet swelled from high blood pressure and she collapsed across the table with sugar diabetes. You have to smile twenty-four hours a day, Momma would say. If you walk through life showing the aggravation you’ve gone through, people will feel sorry for you, and they’ll never respect you. She taught us that man has two ways out in life – laughing or crying. There’s more hope in laughing. So you laugh, so you smile.

(PG 28) I wonder how she kept from teaching us hate when the social worker came around. [She] would poke around the house, wrinkling her nose at the coal dust on the chilly linoleum floor, shaking her head at the bugs crawling over the dirty dishes in the sink. [Mama] would follow that nasty *woman* around those drafty three rooms, keeping her fingers crossed that the telephone hidden in the closet wouldn’t ring. Welfare cases weren’t supposed to have telephones. (Page 23) When you have a good mother and no father . . . God kind of sits in.

(PG 29) I never learned hate at home, or shame. I had to go to school for that. I was about seven years old when I got my first big lesson. I was in love with a little girl named Helene Tucker, a light-complexioned little girl with pigtails and nice manners. She was always clean and she was smart in school. I think I went to school then mostly to look at her. I brushed my hair and even got me a little old handkerchief. It was a lady’s handkerchief, but I didn’t want Helene to see me wipe my nose on my hand. The pipes were frozen again, there was no water in the house, but I washed my socks and shirt every night. I’d get a pot, and go over to Mister Ben’s grocery store, and stick my pot down into his soda machine. Scoop out some chopped ice. By evening, the ice melted to water for washing. I got sick a lot that winter because the fire would go out at night before the clothes were dry. In the morning I’d put them on, wet or dry, because they were the only clothes I had.

Everybody’s got a Helene Tucker, a symbol of everything you want. I loved her for her goodness, her cleanness, her popularity. She’d walk down my street and my brothers and sisters would yell, “Here comes Helene,” and I’d rub my tennis sneakers on the back of my pants and wish my hair wasn’t so nappy and the white folks’ shirt fit me better. I’d run out on the street. If I knew my place and didn’t come too close she’d wink at me and say hello. That was a good feeling. Sometimes I’d follow her all the way home, and shovel the snow off her walk and try to make friends with her Momma and her aunts. I’d drop money on her stoop late at night on my way back from shining shoes in the taverns. And she had a Daddy, and he had a good job. He was a paperhanger.

I guess I would have gotten over Helene by summertime, but something happened in that classroom that made her face hang in front of me for the next twenty-two years. When I played the drums in high school it was for Helene, and when I broke track records in college it was for Helene and when I started standing behind microphones and hear applause I wished Helene could hear it, too. It wasn’t until I was twenty-nine years old and married and making money that I finally got her out of my system. Helene was sitting in that classroom when I learned to be ashamed of myself.

It was on a Thursday. I was sitting in the back of the room, in a seat with a chalk circle drawn around it. The idiot’s seat, the troublemaker’s seat.

The teacher thought I was stupid. Couldn’t spell, couldn’t read, couldn’t do arithmetic. Just stupid. Teachers were never interested in finding out that you couldn’t concentrate because you were so hungry, because you hadn’t had any breakfast. All you could think about was noontime, would it ever come? Maybe you could sneak into the cloakroom and steal a bite of some kid’s lunch out of a coat pocket. A bite of something. Paste. You can’t really make a meal of paste, or put it on bread for a sandwich, but sometimes I’d scoop a few spoonfuls out of the paste jar in the back of the room. Pregnant people get strange tastes. I was pregnant with poverty. Pregnant with dirt and pregnant with smells that made people turn away, pregnant with cold and pregnant with shoes that were never bought for me, pregnant with five other people in my bed and no Daddy in the next room, and pregnant with hunger. Paste doesn’t taste too bad when you’re hungry.

The teacher thought I was a troublemaker. All she saw from the front of the room was a little black boy who squirmed in his idiot’s seat and made noises and poked the kids around him. I guess she couldn’t see a kid who made noises because he wanted someone to know he was there.

It was on a Thursday, the day before the Nero payday. The eagle always flew on Friday. The teacher was asking each student how much his father would give to the Community Chest. On Friday night, each kid would get the money from his father, and on Monday he would bring it to the school. I decided I was going to buy me a Daddy right then. I had money in my pocket from shining shoes and selling papers, and whatever Helene Tucker pledged for her Daddy, I was going to top it. And I’d hand the money right int. I wasn’t going to wait until Monday to buy me a Daddy.

I was shaking, scared to death. The teacher opened her book and started calling out names alphabetically.

“Helene Tucker?”

“My Daddy said he’d give two dollars and fifty cents.”

“That’s very nice, Helene. Very, very nice indeed.”

That made me feel pretty good. It wouldn’t take much to top that. I had almost three dollars in dimes and quarters in my pocket. I stuck my hand in my pocket and held onto the money, waiting for her to call my name. But the teacher closed her book after she called everybody else in the class.

I stood up and raised my hand.

“What is it now?”

“You forgot me.”

She turned toward the blackboard. “I don’t have time to be playing with you, Richard.”

“My Daddy said he’d . . .”

“Sit down, Richard, you’re disturbing the class.”

“My Daddy said he’d give . . . fifteen dollars.”

She turned around and looked mad. “We are collecting this money for you and your kind, Richard Gregory. If your Daddy can give fifteen dollars you have no business being on relief.”

“I got it right now. I got it right now, my Daddy gave it to me to turn in today, my Daddy said. . .”

“And furthermore,” she said, looking right at me, her nostrils getting big and her lips getting thin and her eyes opening wide, “we know you don’t have a Daddy.”

Helene Tucker turned around, her eyes full of tears. She felt sorry for me. Then I couldn’t see her too well because I was crying, too.

“Sit down, Richard.”

And I always thought the teacher kind of liked me. She always picked me to wash the blackboard on Friday, after school. That was a big thrill; it made me feel important. If I didn’t wash it, come Monday the school might not function right.

“Where are you going, Richard?”

I walked out of school that day, and for a long time I didn’t go back very often. There was shame there.

Now there was shame everywhere. It seemed like the whole world had been inside that classroom, everyone had heard what the teacher had said, everyone had turned around and felt sorry for me. There was shame in going to the Worthy Boys Annual Christmas Dinner for you and your kind, because everybody knew what a worthy boy was. Why couldn’t they just call it the Boys Annual Dinner, why’d they have to give it a name? There was shame in wearing the brown and orange and white plaid mackinaw the welfare gave to three thousand boys. Why’d it have to be the same for everybody so when you walked down the street the people could see you were on relief? It was a nice warm mackinaw and it had a hood, and my Momma beat me and called me a little rat when she found out I stuffed it in the bottom of a pail full of garbage way over on Cottage Street. There was shame in running over to Mister Ben’s at the end of the day and asking for his rotten peaches, there was shame in asking Mrs. Simmons for a spoonful of sugar, there was shame in running out to meet the relief truck. I hated that truck, full of food for you and your kind. I ran into the house and hid when it came. And then I started to sneak through alleys, to take the long way home so the people going into White’s Eat Shop wouldn’t see me. Yeah, the whole world heard the teacher that day . . . . we all know you don’t have a Daddy.
```

---

## IC-2474: Nocturne

- Title: Nocturne
- Author (byline): Adam Rapp
- Work: Not specified
- Publisher: Faber and Faber, Inc.
- Publication date as stated: Dec 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MOM, SON, DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 2067
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adam Rapp
ISBN: 978-0571211326
Publisher: Faber and Faber, Inc.
Date (Month/Year): Dec 2001
```

### Introduction (context only: never use it for content warnings)

```text
Nocturne by Adam Rapp
```

### Performance text (classify this)

```text
Fifteen years ago I killed my sister. There. I said it. . . I can change the order of the words. My sister I killed fifteen years ago. I, fifteen years ago, killed my sister. Sister my killed I years ago fifteen. I can cite various definitions. To deprive of life: the farmer killed the rabid dog. To put an end to: the umpire killed the tennis match. To mark for omission: he killed the paragraph. To destroy the vital essential quality of: the dentist killed the nerve with Novocain. To cause to stop: the bus driver killed the engine. To cause extreme pain to: his monologue killed the audience. To slay. To murder. To assassinate. To dispatch. To execute. You can play with tenses. Will kill. Did kill. Have killed. Will have killed. Would like to have killed. You can turn it into a gerund. Killing. There's a kind of progress with a gerund. If you conjugate in the past tense it's all the same. I killed. You killed. He, she, it killed. They killed. You all killed. We killed. There's no way around it. Fifteen years ago I killed my sister. I was seventeen, she was nine. A fact.

The accident happens like this: Joliet, Illinois. I'm coming home from Sub-Diggity, my summer sandwich-making job. My clothes smell like roast beef and mayonnaise. My fingers are stained with mustard. Steely Dan's Hey Nineteen is playing on the AM.

(Singing – see end of selection for a link to the lyrics and music of this song) Way back when In Sixty-seven / I was the dandy Of Gamma Chi It's the second week in July. I'm traveling west on Black Road. It's roughly ninety-five degrees. Mosquitoes are plotting their mid-summer feast. There's an endless feeling of Little League being played. Slurpies and caramel corn. Blue snow cones staining the chins of toddlers. Hot-dogs that are so good they can feed entire families. An ocean of Little League diamonds. I tum south onto Gael Drive. (Singing) Sweet things from Boston So young and willing / Moved down to Scarsdale I'm going forty-five in a thirty. At least that's where the speedometer freezes after the collision. So, it's seven-thirty and the sun is a flaming orb on the horizon. There are colors in the sky. Reds. Pinks. Burnt oranges. Clouds like frayed gauze. Their underbellies golden somehow. Steely Dan is well into its chorus. (Singing) The Cuervo gold The fine Colombian / Make tonight a wonderful thing Say it again . . I turn north onto Gael Drive and I decide to not go home. There's a place where I'll sometimes go and think. It's an enormous platoon of power lines. The radio trees. I want to take my shoes off and feel the buzz in my feet. I accelerate. Something small runs out in the road. I brake. Nothing happens. It's a dog. A garbage can. A plastic bag that's stolen a bit of breeze. I pump the brake pedal. I swerve. There's a thud. A hollow, almost wooden thud. Small as an egg. I continue pumping the brakes. Nothing happens. Steely Dan turns into the Alan Parsons Project. (see end of selection for a link to the lyrics and music of this song) I am the eye in the sky. I pump the brakes and the Electra just keeps going as though by its own volition. I swerve. I counterswerve. I crash into a large oak tree at the end of the street. The front end of the Electra accordions to the windshield. Birds are everywhere. A schizophrenic cloud of crows. I crack three ribs and break my nose. I can taste the metal in my blood. Like warm pewter. The speedometer sticks at forty-five miles per hour.

In that strange, post-crash ethereal silence, I get out of the car and walk the hundred yards or so back to where I heard the thud. The crows have formed a kind of wavering anvil and are flying south toward the sound of the highway. It feels as if the steering wheel has been inserted into my ribcage. My sister's body lies in the street. It looks like a doll's body. Legs. Feet. Yellow socks perfectly folded. Bits of lace turned down-my mother's touch. Shoes so small it's as if they were born out of a children's fable. Hands. Arms. Neck. A small white dress with blue flowers. Anemones. Buttercups. Her head is across the street. It has rolled into the Petersens' driveway. I walk over and pick it up. Simply. Perfunctorily. Only a feeling of great clarity and absence. Like a sudden gust of lake wind. As if it's a ball or some kind of fugitive picnic toy. Its weight seems tremendous. I will reattach it to the neck and she will rise off the pavement and go back into the house and wash up for supper. As I'm reattaching my mother can be seen framed in the living room window, her hand pressed against the glass, her head slightly tilted as though she is peering out over a strange body of water; as though she is watching something hellish emerging from the fog. The sound of sirens. Shrieking sirens from all directions. The shrieking turns into a kind of weeping. Sirens weeping in an octave only known to whales and dolphins. *********** I can't remember my sister's face. Other parts of her are as definite as forks and knives. Legs so slender you wonder how they could support the weight of even the smallest torso. Her wrists as thin as Popsicle sticks. Her boyish arms. Mosquito-bitten. Stained with iodine and calamine lotion. Her tiny hands. Her fingers as light and delicate as bird bones. I try and reconstruct the images. • Frame one: a dog; King-the Petersens' German Shepherd.

• Frame two: a bird; a spooked swallow swooping down from some unknown eaves; nose-diving into the grille at the threat of rain. • Frame three: a small garbage can; green somehow; for recycling; and plastic because there's no music in the thud. • Frame four; a mis-kicked football hurtling end-over-end from the Doughertys' back yard. • And then frame five: My sister in her dress; her hand rising up theatrically. Stop. Please stop. Not now. Not like this. I'm too small for this to happen. She swam. She rode her bike. She liked boys' clothes. She'd steal my boxer shorts and wear them to swimming practice. Once at dinner she ambitiously announced her plan of owning a tuxedo. My mother, of course, made her wear dresses and pierced her ears. She proposed marriage to me at least once a week. She'd go to a knee and say, Marry me you big juicy hunk of yummy boy steak. I'm not kidding. She'd actually say that. And then she'd laugh and I'd laugh and the chorus of our laughter was like a jet flying through our silent house. . . She called me Dorkus. So the memories are there. As clear as if they happened yesterday. I just can't see her face. I wonder if she wanted to be hit. She wasn't chasing a ball or a kite. There weren't any kids calling to her from the other side of Gael Drive. She wasn't pushed from behind. From our driveway approaching cars can be seen at least fifty yards away. No, she wasn't abused. She wasn't ridiculed. She was rarely, if ever, sent to her room. She was loved. And fed. She was well clothed. She was the first girl on her swim team to do the butterfly. In jacks she was good to sixes. A faceless child walks in front of a speeding car. I could buy that. A man with three children and a beautiful wife leaps from the thirtieth floor of his Wall Street building. A pregnant woman walks off the Verrazano Bridge and everyone says she was so happy. But you never hear about it with children. It's always an accident [But] perhaps there is a kind of deathwish in some children: I don't want to be an adult. I don't want to do that. I don't want to hide behind the drapes and darn my husband's socks. I don't want my belly to distend with multiple pregnancies or the disease of tumors. I want to swim and run and spin. I want to get away with things. I want to eat snow cones for the rest of my life. So I'll end it while the going's still good. And I'll make it quick. I'll walk in front of a speeding car. The evening of my sister's death it was discovered that the brake line on the Electra had snapped. I'm in the hospital when my mother walks-or rather glides-into my room. Her face hardened with grief. She sits in a chair beside me for a long time before she speaks. I look down and see that her hands are clenched into fists.

MOM: It was the brake line . . . They're going to let you off with involuntary manslaughter. The only thing you are guilty of is failure to stop to avoid an accident.

She almost sounds disappointed.

MOM: A fifty-dollar fine. Your father paid it for you. . . He's taking it very hard.

SON: (to Mom) How are you, Mother? (to audience) She doesn't respond. Her eyes are screaming to blink. (to Mom) I'm sorry, Mother.

MOM: It wasn't your fault . . . Your father is taking it pretty hard, but we'll get through this. . . Rest well

And then she gets up and walks out. That would be the last thing my mother would say to me: Rest well. A month after the accident, she would move out of our little house on Gael Drive and into an apartment with her sister. She would live with my aunt for three years and then, one day, I would receive a letter from her sister saying that my mother had been moved to a private boarding residence for the clinically depressed. I would later learn of the daily diet of a hundred milligrams of Haldol and the bench where she spends most of her afternoons incessantly singing Old MacDonald's Farm and that her favorite pastime is the making of potholders. My father takes the death of my sister pretty hard. We haven't spoken since I've been home. I hover at the door to his study, leaning against the jamb. He can't look at me.

DAD: Come in, Son.

I've lost my name. I enter his study. I sit across from him at his hulking oak banker's desk. His hands are flat on the blotter. His head tilted down, almost shamefully. There is a small snub-nosed revolver set between the axis of his thumbs. I have never seen this gun before. I had no idea that there's a small black gun living in our house. (to Dad) Dad, is that a gun? Dad . . .

(to audience) The gun is clutched between his hands now and its nose pointed at my throat. In a slow deliberate lean the gun gets closer and closer. I am thinking, "No, Dad. Please, no." But nothing comes out.

DAD: Don't move.

The gun is in my mouth now. The cylinder forcing my lips apart. Like kissing the engine of a toy train. Its smell of axle grease. Its weight incredible on my teeth. My father seethes. His breath is hot and his skin is a flat dull pink and I don't recognize myself in him. I see nothing of his only son in this strange violent intimacy. . . . I hear my mother's voice.

MOM: (gently with fatigue) Earl. Put the gun down, Earl. . . Not this way, Honey.

It's as if she is coaxing a child out of a tree. Not this way, Honey. What does that mean? He would remove the gun from my mouth and my mother would take it and drop it in the trash, somehow rendering the thing powerless.

The taste of it still haunts me. Sickens me. I would eventually lift off the chair and walk out of our little house on Gael Drive. I would lurch/slouch/spiral to a bus stop. The bus would take me to the train station. I would arrive in New York City the following morning in a kind of severe, tightly coiled body clench. Grand Central Station. A cathedral with noise. Anonymity. Here is where I would begin my fifteen-year disappearance from the town with the little house on Gael Drive. I would step out onto Forty-second Street with twelve dollars and forty-two cents in my pocket. . . [because] Fifteen years ago I killed my sister. I was seventeen, she was nine.
```

---

## IC-2475: Not a Genuine Black Man

- Title: Not a Genuine Black Man
- Author (byline): Brian Copeland
- Work: Not specified
- Publisher: Hyperion
- Publication date as stated: July 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: BRIAN, SYLVESTER, MOM, POLICE
- Teaser before the introduction: Yes
- Spoken words (computed): 1302
- Already set (do not supply): none

### Source block (context only)

```text
Author: Brian Copeland
ISBN: 978-1401302337
Publisher: Hyperion
Date (Month/Year): July 2006
```

### Introduction (context only: never use it for content warnings)

```text
It has often been said that comedians deal with pain through humor. They laugh so they don’t have to cry. This was especially true for comedian Brian Copeland. When he was eight, his mother moved his family from Oakland to San Leandro, hoping to escape her abusive husband. Now, keep in mind, that in the early 1970s, San Leandro was 99.99% white and considered one of the most racist enclaves in the nation. The result. He was labeled his whole life - an outsider in his own community based on the color of his skin and an outsider within his race for not being black enough.

Brian spent his adult years trying to leave behind his painful childhood. But an anonymous letter ultimately forces him question his own identity.

Not a Genuine Black Man by Brian Copeland
```

### Performance text (classify this)

```text
BRIAN: (xi-xii) Although I’m a stand-up comic by trade, I also do a radio show for a talk station in San Francisco.

(begins to settle back into his office) I’d been out on the road for a couple of weeks, and when I got back into the station, I had all this mail piled up. In talk radio, mail generally comes to you from two sources: old ladies and kooks. That’s it. Nobody else writes you. The upside is that it makes the mail easy to sort. (going through his mail)

So I’m going through the pile. Old lady. Old lady. Death threat. Old lady. Ooh, here’s a good one. Death threat from an old lady.

Then I come across one that’s typed . . . I mean typed on an actual typewriter. No return address. Local postmark. Addressed to me. I open it, taking out an unsigned sheet that reads: “As an African American, I am disgusted every time I hear your voice because . . .” (trails off as he finishes the sentence silently; tries again aloud.) “As an African American, I am disgusted every time I hear your voice because YOU are not a genuine black man.”

BRIAN: (xii-xiv) (picks up reading again) “... not a genuine black man.” Why do people say that to me? Actually, people have said that to me throughout my life. I don’t even know what that means. Is it how I dress? Is it how I talk? Is it how my machine is set to TiVo (could replace with Stream) Frasier?

If you’re talking about pigment, you can tell by looking at me that I am clearly black. But if you’re talking about some cultural delineation, I don’t know. I can’t swim. That’s black.

(Thinks for a moment) I’m a Democrat. That’s black. I never understood black Republicans. To me, a black joining the Republican Party is like a deer joining the National Rifle Association.

(xvii) Whatever the answer is, any confusion I have about race, any misunderstanding I have about ethnicity, any confusion I have about blackness . . . is my mother’s fault. [When I was 8-years-old she moved my family to San Leandro, CA]

(Pg 12) San Leandro borders Oakland, to the south. Oakland was nearly half black. San Leandro (on the other hand) was 99.99 percent white. Ninety-nine point ninety-nine percent! Ivory Soap looked at that number and went, “WOW!” (Pg 15) To this day, I don’t know how much my mother knew about San Leandro and its reputation when she moved us there. [The only reason we moved was to get away from Sylvester, my father.]

(Pg 8) He was crazy. I never knew what he was going to say or do. He used to mess with my head.

SYLVESTER: Hey Brian, come here . . . . Knock, knock.

BRIAN: Who’s there?

SYLVESTER: (slapping Brian on the head violently) What did I tell you about answering the door when you don’t know who’s on the other side of it?

BRIAN: Once when I was five, I sniffed in a way that Sylvester thoughts was directed at him. He grabbed my nose and pinched it so hard that it was bruised for a month. (Pg 7) He was always doing things like that. [Anyway] (Pg 19) my mother moved us.

(Pg 95) My mother worked very hard at learning “the white man’s culture,” from her conversion to Catholicism (crosses himself) to her switch to the Republican party. She tried to assimilate in any and every way possible. Her philosophy was that while we may not look like them, we could act like them if that’s what it took to be accepted; if that was what we had to do to succeed.

(Pg 131) My childhood was a confusing barrage of mixed messages. On the one hand, Mom would say, “Be proud that you’re black, because black is beautiful. Then, when we acted up, she would say, “Act your age, not your color,” as if immaturity, rambunctiousness and negative behavior were “black” things. (beat as memories pour back in) (Pg 19) My mother moved us.

MOM: (Pg 20) It’ll be okay, honey. Remember you’re the man of the house now.

BRIAN: Maybe it would be okay. Sylvester wasn’t there . . . How bad could it be? [until he found us]

MOM: (Pg 171) Your father . . . He’s coming home.

BRIAN: (Pg 195-196) [I remember] (Voice shifts to that of a young boy as Brian re-lives the event in actions and words) I came home from school and the apartment appeared to be empty. Mom and Grandma must still be at work. That left the question, where was Sylvester? Actually, that was always the question. At that moment, a craving took over my body. (opening the cabinet and getting a huge bowl and box of cereal) I wanted a great big salad bowl filled to the brim with Cap’n Crunch. Isn’t that the best after school snack in the world? It’s sweet and crunchy . . . What more can a kid ask for? (BUMP, BUMP) (Brian looks around perplexed) There it was again. (BUMP, BUMP) It was coming from my mother’s room. I took the stairs two at a time. (BUMP) I got to the doorway of my mother’s room and there I saw him.

(Actor assumes the role of Sylvester who is repeatedly slamming mother’s head against the wall) (BUMP, BUMP, BUMP) (Brian reacts)

It was Sylvester, my mother’s head gripped firmly in his hands, banging her skull against the wall. (BUMP, BUMP) I ran back downstairs into the kitchen. What to do? What to do? Then I saw it, there in the sink. The shiny blade of Grandma’s butcher knife. It was the sharpest knife in the house. I grabbed it and took it upstairs. The bumping had stopped. I stood in the doorway. (knife pointed at Sylvester) LET HER GO! Let her go or I swear to God I will stick this knife in your heart!

SYLVESTER: (Turns and smiles in amusement) What? You a man now? Do you know I will kill you? (Pg 9) N****, quit sticking you lip out at me!

BRIAN: (Pg 197) Yes, I’m the man of the house and I want you to get out! (shaking with tears running down his face) Let her go! (to audience) He reached for me with both hands. I was watching him every second but I never saw him coming. (rises on tiptoe, as if Sylvester has him be the throat; he struggles to loosen Sylvester’s grip) Before I knew it, he had his hands around my throat. (Pg 9) My father strangling me (Pg 199) My mother screamed. [But] her screech was broken by . . .

POLICE: Police!

BRIAN: With that, Sylvester took his hands from around my neck. I gasped for air. He shook his head in disgust. He was disgusted! He pushed past me and walked out the door into the hallway. I could hear him talking to the police as I closed the bedroom door. [And just like that he was gone]

(Pg 167-169) If you go to the street corners of East Oakland or Detroit or Compton, or just about any other urban area with a large black population, you’ll find all these guys selling crack, and all of these guys with five babies by five different women, none of whom they’re supporting. Yet never once has anybody ever accused them of not being a “genuine black man.”

(Crosses to pick up the letter that started all this) Is that what the black person who sent me [this] letter expects me to be? They want me to be Sylvester? I have to be the worst possible stereotype or I’m not “keeping it real?” No.

(Emotional level starts quiet but builds to one of extremely strong emotion) I have this fantasy. I’d track down the writer’s address and go to his house and get in his face and say: I owe you an apology. I’m sorry. I’m sorry that I don’t deal drugs. I’m sorry for wanting more and not less. I’m sorry that all of my children were born into wedlock and that I support them. I’m sorry that I help them with their homework and that I don’t tell them that getting good grades is “acting white”. I’m sorry for wanting to live in a neighborhood where I’m not kept awake at night by gunshots, sirens and screams. I’m sorry that I look so shitty in an orange jumpsuit that I’m not going to prison for anybody. I’m sorry, I’m sorry, I’m sorry, (Rips ups the letter and he is overcome with emotion) I’M SORRY!

(Pg 231) (softly) Wow. (Pg 169) I’m sorry. (Pg 231) I’m a firm believer that most things in this world happen for a reason. (Pg 243-244) When all is said and done, I AM a Genuine Black Man – because I am resilient. I’m still here. I [survived] harassment, schoolyard bullies and Sylvester and bouts of crippling depression. I am still here. (tears) That’s what being black in America is truly about: resilience.

(Pg 245) People sometimes ask me if my mother made the right choice moving us to San Leandro. All I can say in response is, “It’s my hometown.” I am proud and I am at peace. Genuinely.
```

---

## IC-2476: Not Your Typical Dragon

- Title: Not Your Typical Dragon
- Author (byline): Dan Bar-el
- Work: Not specified
- Publisher: Viking Books for Young Readers
- Publication date as stated: Feb 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, FATHER, MOTHER, CRISPIN, DOCTOR, NURSE, FIRST DRAGON, SECOND DRAGON, COACH, SIR GEORGE, SIR GEORGE’S FATHER, CRISPIN’S FATHER, CRISPIN’S MOTHER, EVERYONE, OLD UNCLE
- Teaser before the introduction: Yes
- Spoken words (computed): 882
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dan Bar-el
ISBN: 978-0670014026
Publisher: Viking Books for Young Readers
Date (Month/Year): Feb 2013
```

### Introduction (context only: never use it for content warnings)

```text
When I was little, I was a “free spirit.” I had this glorious silk scarf that I tied around my neck-- it billowed when I ran; red cowboy boots and swim goggles. I wore them constantly. With them, I was invincible and protected my family and my neighborhood from all forms of imaginary bad guys. Then one day my mother uttered those words . . . “What will the neighbors think.” And she took my scarf, my boots and my goggles. My uniqueness was traded in for a conformity that would not draw undue attention.

I remember watching Rudolph putting mud on his nose so it wouldn’t glow, and Hermy the Elf, who really wanted to be a Dentist, toil away making toys instead. They tried to fit in too. I thought, is fitting in really so important?

Maya Angelou once said, “If you are always trying to be normal, you will never know how amazing you can be.” And Crispin finds that out in Not Your Typical Dragon by Dan Bar-el
```

### Performance text (classify this)

```text
NARRATOR: Crispin Blaze was born into a proud family of fire-breathing dragons.

FATHER: (boasting) Every Blaze breathes fire. I breathe fire. Your mother breathes fire. Tomorrow, when you turn seven, you’ll breathe fire, too.

NARRATOR: The little dragon imagined all the forests he would burn down. He dreamed of all the castles he would destroy. He also considered boiling water to make tea, but he didn’t tell his father that. The next day, Crispin sat among family and friends as a big cake was brought to the table.

MOTHER: Who will light the birthday candles?

CRISPIN: I will!

NARRATOR: He could feel a tingling inside his tummy. (Crispin takes a big breath) But when he opened his mouth, fire did not come out. (Crispin starts to blow)

CRISPIN: (Blows with gusto and lots of mushy sound; he is shocked and embarrassed)

NARRATOR: Whipped cream came out.

FATHER: (shouting) Crispin! Dragons breathe fire!

MOTHER: (worried) What will the neighbors think?

ASHLEY (C’s Little Sister): I love whipped cream!

NARRATOR: The little dragon was whisked off to the doctor the very next day.

FATHER: (demanding) Please fix my son!

DOCTOR: What seems to be the problem? (He turns to Chrispin . . . Crispin opens his mouth and breathes)

NARRATOR: But fire did not come out. Band-Aids came out.

DOCTOR: (he reacts, then speaks gravely) I see.

FATHER: Dragons should breathe fire.

NURSE: We were low on Band-Aids.

NARRATOR: The doctor sent Crispin home with medicine. He swallowed two teaspoons before going to school.

FATHER: (pouring out the last dose and giving it to Crispin) It will help you become a real dragon. (he winks)

CRISPIN: (swallows and makes a horrible face)

NARRATOR: After school, Crispin joined his first fire breathing practice. One by one, little dragons aimed their fiery breath at stacks of logs until they burst into flames.

FIRST DRAGON: (breathes fire -- Cheers)

SECOND DRAGON: (breathes fire -- Cheers)

CRISPIN: (steps up confidently)

NARRATOR: He could feel the medicine bubbling in his belly. (Crispin rubs his stomach) But when he opened his mouth, fire did not come out. (Crispin opens his mouth wide and reacts in shock and embarrassment) Marshmallows came out. (laughter)

COACH: (yelling) Dragons breathe fire! Isn’t that right, class?

NARRATOR: The other dragons didn’t answer. They were too busy looking for pointy sticks for marshmallow roasting. (dragon eagerly putting a marshmallow on a stick)

CRISPIN: (turning away dejectedly) I guess I’m not a real dragon.

NARRATOR: He worried that his family would be disappointed. So, he ran away from home. (Crispin sighs) The world can be a scary place for a little dragon who can’t breathe fire. Crispin found a dark cave.

CRISPIN: I’ll be a fireless dragon all by myself. I won’t bother anyone, and no one will bother me.

NARRATOR: [But] An hour later, he had a visitor.

SIR GEORGE: (squeaky, scared voice from outside the cave) I am Sir George. Sh-sh-show yourself, dragon! (Crispin shuffles outside) (Sir George holds up a tiny sword) D-d-do your worst, dragon!

NARRATOR: (Crispin opens his mouth) But fire did not come out. (Crispin hiccups repeatedly) Soap bubbles came out. (Crispin sighs)

SIR GEORGE: (popping the bubbles with the tip of his sword) Don’t you breathe fire, dragon?

CRISPIN: (shaking his head) I can’t.

SIR GEORGE: (moans) But my father insists that I fight a fire-breathing dragon. (sets down his sword and takes a book from his satchel) It even says here in my book that your typical dragon breathes fire.

CRISPIN: I’m not your typical dragon.

SIR GEORGE: (sighs) I can’t go home.

CRISPIN: Me neither. (then he has an idea) Maybe your book could tell us what to do.

SIR GEORGE: Of course! (leafing through the pages) It says it’s probably just your diet.

NARRATOR: Sir George fed Crispin spicy curry, scorching chili, and blistering salsa. (Crispin eats and sweats, eats and sweats, then opens his mouth) But fire did not come out. Red party streamers came out. (Crispin shrugs)

SIR GEORGE: At least they’re the right color. (he searches through the book again) Aha! It says it’s probably your attitude.

NARRATOR: Sir George showed Crispin how to look mean and angry enough to breathe fire. (Sir George makes a face, Crispin tries (x2))

NARRATOR: Crispin opened his mouth. (Crispin opens his mouth) But fire did not come out. Soft, cuddly teddy bears came out.

SIR GEORGE: Hmmmm, we may have taken a step backward.

CRISPIN: (sighs) It’s no use. I’m just not your typical dragon.

NARRATOR: But Sir George was not ready to give up.

SIR GEORGE: (looking at the book) Aha! The book says you’re too stressed.

NARRATOR: Sir George made Crispin close his eyes while he described a quiet, relaxing day at the ocean.

SIR GEORGE: (softly) Do you feel calm? (with urgency) Now imagine a hundred shiny knights attacking you!

NARRATOR: Crispin opened his mouth. (Crispin opens his mouth) But fire did not come out. Beach balls came out.

SIR GEORGE: Well, that’s just plain weird. (Crispin shrugs)

NARRATOR: Secretly, Sir George was glad that Crispin couldn’t breathe fire. He liked the little dragon and didn’t want to fight him. Crispin liked the shiny knight, too, but he missed his parents.

CRISPIN: (sadly) Sir George, it’s getting dark. I want to go home.

SIR GEORGE: (patting him on the back) Don’t worry, little dragon. I will take you.

NARRATOR: Crispin’s parents were relieved when he arrived home safely. Sir George was about to say good-bye when . . .

SIR GEORGE’S FATHER: There you are, boy! Why on earth are you playing with a fire-breathing dragon?

SIR GEORGE: (intimidated, he speaks softly) He’s my friend, Father, and besides, he doesn’t breathe fire.

SIR GEORGE’S FATHER: (laughing) A dragon that doesn’t breathe fire? That’s the silliest thing I’ve ever heard!

CRISPIN’S FATHER: (storming outside) My son is not silly! He may not breathe fire, but I certainly do! (Lets out a powerful spray of flames)

SIR GEORGE’S FATHER: Do your worst, dragon!

NARRATOR: But then the flames scorched the lawn.

CRISPIN’S MOTHER: That’s enough, honey.

NARRATOR: The flames singed the fence.

CRISPIN’S MOTHER: (scolding) You’ve made your point, dear, no stop showing off.

NARRATOR: The flames ignited the roof.

CRISPIN’S FATHER: (Still spewing flames) I can’t stop breathing fire!

CRISPIN’S MOTHER: (Panicked) You’ll burn our house down! You’ll burn down the whole neighborhood!

NARRATOR: Dragons came running from all directions. They knew how to start fires, but no one knew how to stop them. Crispin suddenly felt a tingling in his tummy. (Crispin rubs his stomach) He felt a bubbling in his belly. (Crispin opens his mouth) But fire did not come out. A gush of water shot out! (Crispin puts out the flames) Crispin aimed the water at his father’s flames. He saved his home, and he even saved the shiny man, who wasn’t looking so shiny anymore.

EVERYONE: Hurray for Crispin!

NARRATOR: On Crispin’s next birthday, there was a big party. Family and friends came from all over the land.

Sir George and his family came, too. Lots of dragons were dancing. Crispin stood with his mouth open wide. Fire still did not come out. Music came out instead.

(Crispin dances and hums a favorite dance tune)

OLD UNCLE: Your son, he’s not your typical dragon, is he?

FATHER: (proudly) No, my son is something special!
```

---

## IC-2477: A November Farewell

- Title: A November Farewell
- Author (byline): Mike Royko
- Work: One More Time: The Best of Mike Royko
- Publisher: University of Chicago Press
- Publication date as stated: May 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1148
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mike Royko
Book: One More Time: The Best of Mike Royko
ISBN: 978-0226730721
Publisher: University of Chicago Press
Date (Month/Year): May 2000
```

### Introduction (context only: never use it for content warnings)

```text
Most people think of Mike Royko as a hard-edged, hard-hitting, no-nonsense columnist for the Daily News, Sun- Times and Tribune, and that he was. Fifteen years after he died, he remains a Chicago icon for exposing hypocrisy, corruption, and the high and mighty who perpetrated it.

Most people don't think of him as sentimental, but he could be. When his wife, Carol, died suddenly at the age of 44 of a brain hemorrhage — on his 47th birthday — Royko was devastated. For the first time in his career, his column went on hiatus. He was back on Nov. 22, only two months after she had died,with a column titled, "A November Farewell," about a man closing up a summer home for the last time on a lake in Wisconsin. He wrote the column, as was typical, the day before it ran, November 21, 1979. What few people realized, was that November 21st, 1979 would have been Carol’s 45th birthday. A November Farewell by Mike Royko . . . for Carol.
```

### Performance text (classify this)

```text
Do me a favor. If there's someone you love but haven't said so in a while, say it now. Always, always say it now. – Mike Royko The two of them first started spending weekends at the small, quiet Wisconsin lake almost 25 years ago. Some of her relatives let them use a tiny cottage in a wooded hollow a mile or so from the water.

He worked odd hours, so sometimes they wouldn't get there until after midnight on a Friday. But if the mosquitoes weren't out, they'd go to the empty public beach for a moonlight swim, then sit with their backs against a tree and drink wine and talk about their future.

They were young and had little money, and they came from working class families. So to them the cottage was a luxury, although it wasn't any bigger than the boat garages on Lake Geneva, where the rich people played.

The cottage had a screened porch where they sat at night, him playing a guitar and her singing folk songs in a sweet, clear voice. An old man who lived alone in a cottage beyond the next clump of woods would applaud and call out requests.

One summer the young man bought an old motorboat for a couple of hundred dollars. The motor didn't start easily. Some weekends it didn't start at all, and she'd sit and laugh and row while he pulled the rope and swore.

But sometimes it started, and they'd ride slowly along the shoreline, looking at the houses and wondering what it would be like to have a place that was actually on the water. He'd just shake his head because even on a lake without social status, houses on the water cost a lot more than he'd ever be able to afford.

The years passed, they had kids, and after a while they didn't go to the little cottage in the hollow as often. Something was always coming up. He worked on weekends, or they had someplace else to go. Finally the relatives sold the cottage.

Then he got lucky in his work. He made more money than he ever dreamed they'd have. They remembered how good those weekends had been and they went looking at lakes in Wisconsin to see if they could afford something on the water.

They looked at one lake, then another. Then another. Cottages they could afford, they didn't like. Those they liked were overpriced. Or the lake had too many taverns and not enough solitude.

So they went back to the little lake. They hadn't been there for years. They were surprised to find it was still quiet. That it still had no taverns and one grocery store.

And they saw a For Sale sign in front of a cedar house on the water. They parked and walked around. It was surrounded by big old trees. The land sloped gently down to the shore. On the other side of the road was nothing but woods. Beyond the woods were farms.

On the lake side, the house was all glass sliding doors. It had a large balcony. From the outside it was perfect.

A real estate salesman let them in. The interior was stunning - like something out of a homes magazine.

They knew it had to be out of their reach. But when the salesman told them the price, it was close enough to what they could afford that they had the checkbook out before they saw the second fireplace upstairs.

They hadn't known summers could be that good. In the mornings, he'd go fishing before it was light. She'd sleep until the birds woke her. The he'd make breakfast and they'd eat omelets on the wooden deck in the shade of the trees.

They got to know the chipmunks, the squirrels, and a woodpecker who took over their biggest tree. They got to know the grocer, the old German butcher who smoked his own bacon, the little farmer who sold them vine-ripened tomatoes and sweet corn.

They were a little selfish about it. They seldom invited friends for the weekends. But they didn't feel guilty. It was their own, quiet place.

The best part of their day was dusk. They had a west view and she loved sunsets. Whatever they were doing, they'd always stop to sit on the pier or deck and silently watch the sun go down, changing the color of the lake from blue to purple to silver and black. One evening he made up a small poem:

The sun rolls down
like a golden tear
Another day.
Another day
gone.

She told him it was sad, but that she liked it.

What she didn't like was October, even with the beautiful colors and the evenings in front of the fireplace. She was a summer person. The cold wind wasn't her friend.

And she saw November as her enemy. Sometime in November would be the day they would take up the pier, store the boat, bring in the deck chairs, take down the hammock, pour antifreeze in the plumbing, turn down the heat, lock everything tight and drive back to the city.

She'd always sigh as they pulled onto the road. He'd try to cheer her up by stopping at a German restaurant that had good food and a corny band, and he'd tell her how quickly the winter would pass, and how soon they'd be there again.

And the snow finally would melt. Spring would come, and one day, when they knew the ice on the lake was gone, they would be back. She'd throw open all the doors and windows and let the fresh air in. Then she'd go out and greet the chipmunks and woodpeckers. And she'd plant more flowers. Every summer, there were more and more flowers. And every summer seemed better than the last. The sunsets seemed to become more spectacular. And more precious.

This past weekend, he closed the place down for the winter. He went alone.

He worked quickly, trying not to let himself think that this particular chair had been her favorite chair, that the hammock had been her Christmas gift to him, that the lovely house on the lake had been his gift to her.

He didn't work quickly enough. He was still there at sunset. It was a great burst of orange, the kind of sunset she loved best.

He tried, but he couldn't watch it alone. Not through tears. So he turned his back on it, went inside, drew the draperies, locked the door and drove away without looking back.

It was the last time he would ever see that lovely place. Next spring there will be a For Sale sign in front and an impersonal real estate man will show people through.

Maybe a couple who love to quietly watch sunsets together will like it. He hopes so.
```

---

## IC-2478: Only Superman Onstage

- Title: Only Superman Onstage
- Author (byline): Daniel Tosh
- Work: I Killed: True Stories from the Road from America’s Top Comics
- Publisher: Crown Publishing
- Publication date as stated: Oct 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 844
- Already set (do not supply): none

### Source block (context only)

```text
Author: Daniel Tosh
Book: I Killed: True Stories from the Road from
America’s Top Comics
ISBN: 978-0307341990
Publisher: Crown Publishing
Date (Month/Year): Oct 2006
```

### Introduction (context only: never use it for content warnings)

```text
No moment in popular culture is more charged and anxious than when a stand-up comic battles with a heckler. It usually ends with a knockout insult and a huge laugh. But when things turn ugly, it can expose the gap between comedians and patrons who see this clash very differently. In Only Superman Onstage, Daniel Tosh shares a true story from his life on the road as a stand-up comic and one heckler who took things from the venue to the road. Only Superman Onstage by Daniel Tosh
```

### Performance text (classify this)

```text
In 2002, I emceed a Battle of the Bands at a college in Lakeview, Florida. I thought it would be fun, kind of like American Idol, and I could make fun of each band a little bit after it had performed.

What I didn’t realize was that the only people who showed up at these things were friends of the people performing. They don’t want to hear some stranger belittle their friends right after they’ve performed.

The show was going on and we were having a good time. Then some guy really just went into me, heckling and screaming at me. So I went right back into him. He wouldn’t quit, so I had them turn the houselights up and offered him a microphone if he wanted to continue. It wasn’t a fun exchange, like in a comedy club. This was pretty angry and violent.

He said, “Who do you think you are?” I was just like, “I’m the guy who they’re paying a lot of money to make fun of your friend’s band.”

Onstage, a comedian can be fearless. You get all that laughter from so many people and start to feel superhuman, invincible. So I didn’t hesitate before I said something like, “I’ll kill you and all your friends.” I was so drunk with thoughts of immortality that it never occurred to me somebody out there might be saying, “Okay. We’re gonna wait outside for this guy afterwards.”

Sure enough, the show ended and I was walking outside to the care with my little college-girl student sponsor, who noticed very quickly that, “Hey, there’s that guy.” And there was the heckler with a crew of guys. He was probably about fifty yards away from me, screaming, “Com one, let’s fight!” I yelled back, “Oh, no. I’m busy,” and told the student “Okay, let’s go to the car. Now. Qu8ickly.” The entire group started running toward us. And that’s when I transformed from the powerful comic to the scared little *guy* who had needed to become a comic in the first place.

Seconds after we took off, they were on our bumper, and I realized that the student was driving me to my hotel and got a big dose of pure fear. “Hey, you do know these guys are really trying to kill me, right?” She kept right on driving the speed limit, straight to my hotel. Suddenly this carload of guys pulled into the lane next to us, screaming for us to pull over. She began to realize that maybe something unusual was happening. “What are we going to do?”

“Well, for starters, we’re not going to pull over.”

Then the guy who wanted to kill me waved a gun out of his window, and she still stopped at the next red light.

By now I’d stopped trying to look cool and was just yelling at her, “Run the light! They’re pointing a gun at us!” and she said, “No. I could get a ticket.” I was trying to enlighten her: “Yes. Yes. We want police now.”

Finally she got it, ran the light, and started speeding and ducking into backroads trying to lose them. After watching this fresh-faced college girl turn from law-abiding citizen to demonic driver, I’m convinced everyone has the ability to lead a high-speed chase, given the proper motivation.

I guess the heckler and his posse were pretty motivated, because they stayed right with us. Suddenly my driver screeched to a halt in front of my hotel and smiled at me like, “We made it.” Meanwhile, they were pulling up right behind us, and I started yelling, “Go! Go!” Finally I called 911 from my cell. Conscious of the fact that they play those recordings back, I was trying not to act too scared. “Oh, yes. Hi. Well, you see, we seem to have some crazies driving next to us with a gun. We really could use your help. We’re going to stay in the car just driving around until a cop intercepts us.” And that’s what happened – a patrol car showed up, my pursuers took off, and another cop went and followed them. I said, “That’s it. I’m not staying at that hotel.” The 911 operator said, “Yeah, the cop just found them circling your hotel.”

When I got into the police car, the college girl reacted just as if we’d driven back to the hotel from having a tuna melt, instead of being chased there by gun-toting lunatics. She just smiled at me and said, “Okay, it was nice meeting you. Hopefully you can come back next year.”

So I had a police escort take me to the hotel and go up to my room with me and pack all my stuff. I even got a police escort back to the freeway, where I drove to my brother’s house in Orlando. And I curled up in bed with him and cried. For the next six months, all hecklers got from me was a smile, “God bless you,” and the next joke.
```

---

## IC-2479: The Other Woman

- Title: The Other Woman
- Author (byline): Sherwood Anderson
- Work: The Best American Short Stories of the Century
- Publisher: Houghton Mifflin
- Publication date as stated: April 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2146
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sherwood Anderson
Book: The Best American Short Stories of the Century
ISBN: 978-0395843673
Publisher: Houghton Mifflin
Date (Month/Year): April 2000
```

### Introduction (context only: never use it for content warnings)

```text
"I am in love with my wife," he said--a superfluous remark, as I had not questioned his attachment to the woman he had married. We walked for ten minutes and then he said it again. I turned to look at him. He began to talk and told me the tale I am now about to set down. The tale of The Other Woman by Sherwood Anderson
```

### Performance text (classify this)

```text
The thing he had on his mind happened during what must have been the most eventful week of his life. He was to be married on Friday afternoon. On Friday of the week before he got a telegram announcing his appointment to a government position. Something else happened that made him very proud and glad. In secret he was in the habit of writing verses and during the year before several of them had been printed in poetry magazines. One of the societies that give prizes for what they think the best poems published during the year put his name at the head of its list. The story of his triumph was printed in the newspapers of his home city and one of them also printed his picture.

As might have been expected he was excited and in a rather highly strung nervous state all during that week. Almost every evening he went to call on his fiancée, the daughter of a judge. When he got there the house was filled with people and many letters, telegrams and packages were being received. He stood a little to one side and men and women kept coming up to speak to him. They congratulated him upon his success in getting the government position and on his achievement as a poet.

As he explained when he told me of his experience, it was for him an altogether abnormal time. He felt like one floating in air. When he got into bed after seeing so many people and hearing so many words of praise his head whirled round and round. When he closed his eyes a crowd of people invaded his room. It seemed as though the minds of all the people of his city were centered on himself. The most absurd fancies took possession of him. He imagined himself riding in a carriage through the streets of a city. Windows were thrown open and people ran out at the doors of houses. "There he is. That's him," they shouted, and at the words a glad cry arose.

My friend could not explain whether the excitement of the people was due to the fact that he had written a new poem or whether, in his new government position, he had performed some notable act. The apartment where he lived at that time was on a street perched along the top of a cliff far out at the edge of his city, and from his bedroom window he could look down over trees and factory roofs to a river.

As would be natural under such circumstances, he tried to control his thoughts, but when he sat by the window and was wide awake a most unexpected and humiliating thing happened.

At a corner of the street where he lived there was a small cigar store and newspaper stand run by a fat man of forty and his wife, a small active woman with bright grey eyes. In the morning he stopped there to buy a paper before going down to the city. Sometimes he saw only the fat man, but often the man had disappeared and the woman waited on him. She was, as he assured me at least twenty times in telling me his tale, a very ordinary person with nothing special or notable about her, but for some reason he could not explain, being in her presence stirred him profoundly. During that week in the midst of his distraction she was the only person he knew who stood out clear and distinct in his mind. When he wanted so much to think noble thoughts he could think only of her. Before he knew what was happening his imagination had taken hold of the notion of having a love affair with the woman.

"I could not understand myself," he declared, in telling me the story. " I thought about her all the time. After two or three days of that sort of thing the consciousness of her got into my daytime thoughts. I was terribly muddled. When I went to see the woman who is now my wife I found that my love for her was in no way affected by my vagrant thoughts. There was but one woman in the world I wanted to live with and to be my comrade in undertaking to improve my own character and my position in the world, but for the moment, you see, I wanted this other woman to be in my arms. To satisfy the annoying impulse in myself I went and stood on the sidewalk before the tobacco shop. It was a two story building, and I knew the woman lived upstairs with her husband. For a long time I stood in the darkness with my body pressed against the wall of the building, and then I thought of the two of them up there and no doubt in bed together. That made me furious.

"Then I grew more furious with myself. I went home and got into bed, shaken with anger. It was a miserable experience.

"On Thursday morning I went into the store. There stood the woman alone. I think she knew how I felt. Perhaps she had been thinking of me as I had been thinking of her. A doubtful hesitating smile played about the corners of her mouth. She had on a dress made of cheap cloth and there was a tear on the shoulder. She must have been ten years older than myself. When I tried to put my pennies on the glass counter, behind which she stood, my hand trembled so that the pennies made a sharp rattling noise. When I spoke the voice that came out of my throat did not sound like anything that had ever belonged to me. It barely arose above a thick whisper. 'I want you,' I said. 'I want you very much. Can't you run away from your husband? Come to me at my apartment at seven tonight.'

"The woman did come to my apartment at seven. That morning she didn't say anything at all. For a minute perhaps we stood looking at each other. I had forgotten everything in the world but just her. Then she nodded her head and I went away.

"It was on that morning, just the day before my marriage, that I got a long and very beautiful letter from my fiancée. In it she,poured out her heart. She told me how afraid she was and how glad too. Like most young women she had heard things whispered. In the letter she was very sweet and fine. 'For a long time, after we are married, we will forget we are a man and woman,' she wrote. 'We will be human beings. You must remember that I am ignorant and often I will be very stupid. You must love me and be very patient and kind.

When I know more, when after a long time you have taught me the way of life, I will try to repay you. I will love you tenderly and passionately. I am afraid but I am also happy. O, I am so glad our marriage time is near at hand!'

"Now you see clearly enough what a mess I was in. In my office, after I had read my fiancée’s letter, I became at once very resolute and strong. I remember that I got out of my chair and walked about, proud of the fact that I was to be the husband of so noble a woman. 'I'm all right now,' I said to myself. 'The beauty of her character has saved me from myself. I will go home now and send the other woman away.'

"Then a thought came to me. “I cannot be rude to the other woman. I will have to make some kind of an explanation,' I said to myself.

"The woman came at seven o'clock, and, as you may have guessed, I let her in and forgot the resolution I had made. It is likely I never had any intention of doing anything else. There was a bell on my door, but she did not ring, but knocked very softly. It seems to me that everything she did that evening was soft and quiet, but very determined and quick. Do I make myself clear? When she came I was standing just within the door where I had been standing and waiting for a half hour. My hands were trembling as they had trembled in the morning when her eyes looked at me and when I tried to put the pennies on the counter in the store. When I opened the door she stepped quickly in and I took her into my arms. We stood together in the darkness. My hands no longer trembled. I felt very happy and strong.

"Although I have tried to make everything clear I have not told you what the woman I married is like. I have emphasized, you see, the other woman. It is inevitable that I give you the impression that I am in love with the tobacconist's wife. That's not true. To be sure I was very conscious of her all during the week before my marriage, but after she had come to me at my apartment she went entirely out of my mind.

"As a matter of fact I went to see my beloved on that evening filled with a new faith in the outcome of our life together. When I got to my fiancée’s house there was a crowd of people standing about. Some were relatives from distant places I had not seen before. She looked up quickly when I came into the room. My face must have been radiant. I never saw her so moved. She thought her letter had affected me deeply, and of course it had. Up she jumped and ran to meet me. She was like a glad child. Right before the people who turned and looked inquiringly at us, she said the thing that was in her mind. 'O, I am so happy,' she cried. 'You have understood. We will be two human beings. We will not have to be husband and wife.'

"As you may suppose everyone laughed, but I did not laugh. The tears came into my eyes. I was so happy I wanted to shout. Perhaps you understand what I mean. In the office that day when I read the letter my fiancée had written I had said to myself, 'I will take care of the dear little woman.' There was something smug, you see, about that. To tell you the truth I had come down off my perch. The spirit of the other woman did that to me. Before all the people gathered about I held my fiancée close and we kissed. They thought it very sweet of us to be so affected at the sight of each other. What they would have thought had they known the truth about me God only knows!

"I have said that after that evening I never thought of the other woman at all. That is partially true but, sometimes the feeling of her comes sharply into my body and mind. After that one meeting I never saw her again. On the next day I was married and I have never gone back into her street.

"And now you see I am married and everything is all right. My marriage is to me a very beautiful fact. If you were to say that my marriage is not a happy one I could call you a liar and be speaking the absolute truth. I have tried to tell you about this other woman. There is a kind of relief in speaking of her. I have never done it before. To-night I shall think of the other woman. That sometimes occurs My thoughts will not take the form they did during the week before I was married. I will wonder what has become of the woman. For a moment I will again feel myself holding her close. I will think that for an hour I was closer to her than I have ever been to anyone else. Then I will think of the time when I will be as close as that to my wife. She is still, you see, an awakening woman. For a moment I will close my eyes and the quick, shrewd, determined eyes of that other woman will look into mine. My head will swim and then I will quickly open my eyes and see again the dear woman with whom I have undertaken to live out my life. Then I will sleep and when I awake in the morning it will be as it was that evening when I walked out of my dark apartment after having had the most notable experience of my life.
```

---

## IC-2480: The Paper Menagerie

- Title: The Paper Menagerie
- Author (byline): Ken Liu
- Work: The Paper Menagerie and Other Stories
- Publisher: S&S/Saga Press
- Publication date as stated: Oct 2016
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JACK, MOM, MARK, DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 1470
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ken Liu
Book: The Paper Menagerie and Other Stories
ISBN: 978-1481424363
Publisher: S&S/Saga Press
Date (Month/Year): Oct 2016
```

### Introduction (context only: never use it for content warnings)

```text
*According to a 2023 Pew Research Study, 1 in 5 Asian American adults say they have hidden a part of their heritage – cultural customs, food, clothing or religious practices from non-Asians at some point in their lives. Why? Fear of ridicule and a desire to fit in are the most common reasons. Being from a mixed culture sounds glamorous; but for many it is a challenge.

In this selection, Jack grows up with one heart and two cultural identities. From a young age, he struggles to find common ground with his mother, a mail-order bride from Hong Kong who speaks little English and the American values which he obviously prefers. Can he find it in his heart to love his mother despite their differences?

The Paper Menagerie by Ken Liu
```

### Performance text (classify this)

```text
JACK: (Pg 178-192) One of my earliest memories starts with me sobbing. I refused to be soothed no matter what Mom and Dad tried. Dad gave up, but Mom took me into the kitchen and sat me down at the breakfast table.

“Kan, kan," she said, as she pulled a sheet of wrapping paper from on top of the fridge. She set the paper down and began to fold it. I stopped crying and watched her, curious. She turned the paper over and folded it again. She pleated, packed, tucked, rolled, and twisted until the paper disappeared between her cupped hands. She lifted the folded paper to her mouth and blew into it, like a balloon, then put her hands down on the table and let go.

MOM: Kan . . .Laohu

JACK: A little paper tiger stood on the table. Its tail twitched -- "Rawrr-sa." I laughed and stroked its back with an index finger. "Zhe jiao zhezhi," Mom said. This is called origami. At my request, Mom also made a goat, a deer and a water buffalo out of wrapping paper. – A paper menagerie. . . I didn't know this at the time, but Mom’s kind was special. She breathed into them so that they moved with her life. This was her magic.

JACK: [When I was ten], one of the neighborhood boys, came over with his Star Wars action figures. Obi-Wan Kenobi's lightsaber lit up; he could swing his arms and say, "Use the Force!" (to Mark) Can he do anything else? (to audience) Mark was annoyed by my question.

MARK: Show me your toys!

JACK: I didn't have any toys except my paper menagerie. I brought Laohu out from my bedroom and sat him down on the coffee table.

MARK: (examining the tiger, scoffing) Doesn't look like a tiger at all. Your Mom makes toys for you from trash?

JACK: I had never thought of Laohu as trash. But looking at him now, he was really just a piece of paper. Mark pushed Obi-Wan' s head again. The lightsaber flashed; he moved his arms up and down. "Use the Force!" Laohu turned and pounced, knocking Obi-Wan off the table. "Rawwww!" [But when] it hit the floor and broke, Mark punched me, hard. Gabbed Laohu, crumpled him in his hand, tore him in half and threw them at me.

MARK: (throwing with anger) Here's your stupid cheap Chinese garbage.

JACK: After Mark left, I spent a long time trying to tape together the pieces, smooth out the paper, and follow the creases to refold Laohu. (beat) At dinner I asked Dad, "Do I have a chink face?"

MOM: (looking confused)"Sha jiao chink?"

JACK: (to himself) I look nothing like her, nothing! (to Mom) English! Speak English!

MOM: (trying) What happen?

JACK: (ignoring her) I pushed the chopsticks and the bowl before me away. "We should eat American food."

DAD: A lot of families cook Chinese sometimes.

JACK: We are not other families. (to himself) Other families don't have Moms who don't belong.

MOM: Bu haochi?

JACK: (raising his voice) English . . . Speak English! (to audience) Mom reached out to touch my forehead, feeling for my temperature.

MOM: Fashao la?

JACK: (brushing her hand away) I'm fine. Speak English! (to audience) She tried to speak, stopped; tried and stopped again.

MOM: "If I say 'love,' I feel here." (points to her lips) "If I say 'ai,' I feel here." (puts her hand over her heart)

JACK: (shaking his head) You are in America . . . And I want some real toys! (to audience) Dad bought me a full set of Star Wars action figures, [and] I packed the paper menagerie in a shoebox and shoved it into the corner of the attic.

"You shouldn't treat your mother that way," Dad said. But he couldn't look me in the eyes as he said it. Deep in his heart, he must have realized that it was a mistake to have tried to take a Chinese peasant girl and expect her to fit in the suburbs of Connecticut.

If Mom spoke to me in Chinese, I refused to answer her. After a while, she tried to use more English. But her accent and broken sentences embarrassed me. Eventually, she stopped speaking altogether if I was around. Every once in a while, I would see her at the kitchen table studying a sheet of wrapping paper. Later a new paper animal would appear on my nightstand. I squeezed them until the air went out and stuffed them away in the box in the attic.

Mom finally stopped making the animals when I was in high school. By then her English was much better, but I was already at that age . . . I wasn't interested in what she had to say whatever language she used. It was hard for me to believe that she gave birth to me. We had nothing in common.

[And we still didn’t six years later when] Dad and I stood, one on each side of Mom, lying on the hospital bed. She was not yet forty, but she looked much older. For years she had refused to go to the doctor. By the time an ambulance finally carried her in, the cancer had spread far beyond the limits of surgery.

My mind was not in the room. It was the middle of campus recruiting season, and I was focused on resumes, transcripts, and interviews. I understood that it was terrible to think about this while your mother lay dying, but that didn't change how I felt. I reached out to touch her hand because that was what I was supposed to do.

MOM: Jack, if I . . . don't make it, don't be sad. Focus on your life. Just keep that box you have in the attic with you, and once in a while take it out and think about me. I'll be with you always.

JACK: (puzzled at first, then remembers; to himself) The paper menagerie hidden in the darkness of the attic for so long . . . (to Mom) Just rest, Mom.

MOM: Just open it once in a while. Just open –

(coughing spell) Haizi, mama ai ni

JACK: An image from years ago flashed into my memory: Mom saying ai and then putting her hand over her heart. (to Mom) It's okay, Mom.

(stroking her arm awkwardly) Stop talking. (to audience) Dad came back, and I said that I needed to get to the airport early because I didn't want to miss my flight. (long beat) She died when my plane was somewhere over Nevada.

After [that], the paper animals did not move. Perhaps I had only imagined that [they] were once alive. The memory of children could not be trusted. (beat)

It was two years after Mom's death. I was home, flipping through the TV channels, [when I heard] a rustle. I looked up and saw a ball of wrapping paper and torn tape on the floor. I walked over to pick it up. The ball of paper shifted, unfurled itself, and I saw that it was Laohu, who I hadn't thought about in a very long time. "Raw-sa." Mom must have put him back together after I had given up. I reached out a finger. Laohu's tail twitched, and he pounced playfully. I laughed, stroking his back. "How've you been, old buddy?" Laohu stopped playing and proceeded to unfold himself. [There] in my [hand] was a square of creased wrapping paper, the plain side up. It was filled with dense Chinese characters in Mom's handwriting. The language that I had tried to forget for years came back, and I felt the words sinking through my skin until they squeezed tight around my heart.

MOM’S VOICE (as JACK reads silently): Son, We haven't talked in a long time. You are so angry when I try to touch you that I'm afraid. And I think maybe this pain I feel all the time now is something serious.

But if I write to you with all my heart, I'll leave a little of myself behind on this paper, in these words. Then the creatures I made for you will again leap and run and pounce, and maybe you'll get to see these words.

[When] you were born! I was so happy. When you said your first words to me, in Chinese I cried for hours. When I made the first zhezhi animals for you, and you laughed, I felt there were no worries in the world.

Son, I know that you do not like your Chinese eyes, which are my eyes. I know that you do not like your Chinese hair, which is my hair. But can you understand how much joy your very existence brought to me? Can you understand how it felt when you stopped talking to me and wouldn’t let me talk to you in Chinese? I felt I was losing everything all over again. You know what the Chinese think is the saddest feeling in the world? For a child to finally grow the desire to take care of his parents, only to realize that they [are] gone.

Why won't you talk to me, son?

JACK: (beat) [Her] pain makes it hard to bear. (beat) Following the creases, I refolded the paper back into Laohu. I cradled him in the crook of my arm, and as he purred, I traced out the character for ai on the paper, intertwining my pen strokes with her words.
```
