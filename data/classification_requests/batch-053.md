# Classification request: batch 53 of 53 (39 records, IC-2481 to IC-2519)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-053-reply.json`.

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

## IC-2481: Past Wasn’t Done with Me

- Title: Past Wasn’t Done with Me
- Author (byline): Kemp Powers
- Work: The Moth: 50 True Stories, Pgs 335-342
- Publisher: Hachette Books
- Publication date as stated: Sept 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1666
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kemp Powers
Book: The Moth: 50 True Stories, Pgs 335-342
ISBN: 978-1401311117
Publisher: Hachette Books
Date (Month/Year): Sept 2013
```

### Introduction (context only: never use it for content warnings)

```text
Past trauma has a way of refusing to stay buried -- resurfacing when life cracks open just enough. And the truth is: surviving something doesn’t mean you’ve escaped it; in fact, healing often begins only when we stop running from what haunts us.

The Past Wasn’t Done with Me by Kemp Powers
```

### Performance text (classify this)

```text
(Pgs 335-342) The first time that I passed out on the Chicago train, I knew I was dying from mad cow disease. At least that's what I told my doctor, and he was pretty impressed by the depths of my neurosis. But he assured me that I wasn't. I had anxiety. And he asked me if there was anything that had happened recently causing stress, and I had to think about the question.

I said, "My father's dying of cancer -- My daughter almost died last year from febrile seizures, and I'm pretty much terrified to be left alone with her." Now, this raised his eyebrows. He wrote me a prescription for Xanax and gave me the name of a therapist.

Now, I don't know what prompted me to say what I said next, but as he handed me the prescription, I blurted out: "There's one more thing: When I was 14 years old, I shot my best friend in the face accidentally, and I watched him die."

Henry was one of seven people to die that day in New York City, 1988. He wasn't even the youngest kid from Queens that had that dubious distinction. But his was the death that I saw with my own eyes. The one that I was responsible for with my own hands, and the one I'm going to carry with me for the rest of my life.

Home back then was a 2-bedroom in Brooklyn. It was a big source of pride for my mom, who had raised my three older sisters and me since splitting from my dad when I was 4 years old. New York was really violent and dangerous back then. 2000-murders-a-year violent. But I never let the violence in the world impact me.

I was actually an honor roll student. And when Henry and I met in the 7th grade, we got along immediately. The physical contrast couldn't have been more extreme. He was unusually muscular and well-built for a 12-year-old, and I was just as oddly tall and lanky for a kid the same age. But that's where our differences ended. We were into all the same things. We shared all the same fears. We walked together every day after school to the Carroll Street subway station in South Brooklyn. And we both hated the older boys from John Jay High School nearby, who'd show up every Halloween and rain rotten eggs and water balloons filled with Nair on our heads, which gave you a nice surprise when you got home and tried to clean up. He was my first and best friend.

On the afternoon of April 14, 1988, Henry and Chris, another friend of mine, came by my apartment. They dropped their book bags and plopped down on my bed. My mother was a captain in the Army Reserves at this time; we had three guns in the house. The .38-caliber revolver was my favorite, not just because it was the one kept loaded. It looked like a gun from the movies, and it was the one I always showed to my friends, even though my mom never knew about it. And this day was no different.

I started off by emptying the gun, made sure all the bullets were out. Then I demonstrated my index finger spin-the cowboy move that I'd been working on. Then I took a single bullet, pretended to insert it into the cylinder, and pointed the gun at my friends. I can actually remember smiling as I pulled the trigger, ready to shout, "Gotcha!" when I made them jump.

But instead of the dull click of a hammer followed by laughter, there was a muzzle flash, an explosion, and shock. How did the bullet get into the chamber?

Chris looked at me, and my heart started racing, and we both looked over at Henry. I guess we were waiting for him to turn around and tell me how much trouble I was gonna get into when my mother got home.

Now, whenever we're faced with something horrific, I think it's human instinct to want to run, and mentally that's what I did. Then the next thing you know the hallway was full of people.

My mom was there, sobbing. The paramedics were there. Of course, the cops were there. When one of the paramedics came out of the apartment, I remember begging him, "Please tell me he's okay, please tell me he's okay," and even though I knew what he was gonna say, I wasn't prepared for the words: "He's gone."

That night in the police station I had to recount in detail everything that happened. I didn't want to. I wanted to crawl under that table and hide. But I did, slowly, methodically, choking back tears when I looked down and realized my sweatshirt was covered in blood.

The wake came a week later, and I didn't think Henry's family would have any interest in me attending, but my mom insisted we go. There was a huge crowd gathered around the coffin, and I made my way over to Henry. They had him in a really nice blue suit. But I remember the coffin making him look so small. And I just stood there and stared at him. That's when I heard this woman's voice. She said, "I JUST WANT TO SEE HIM!" I didn't know whether she was talking about Henry lying there in a coffin, or me, his killer, standing over him, crying onto his jacket. Every eye in the funeral home was on me, and all I could do was close my eyes and wish that I was someplace else.

Miraculously, Henry's family did not want to press charges. They embraced me and offered their forgiveness, and when the Brooklyn DA hit me with a list of charges, ranging from manslaughter to assault with a deadly weapon, they were the ones who stood up and said they didn't want to destroy two young lives instead of one.

They're the reason that, instead of going to jail, I got one year of counseling. That was my sentence. I remember thanking them that day for giving me a second chance when I didn't think I deserved one.

In the years that followed, I thought it was odd that no one -- none of my friends, none of my family -- ever said a single word about Henry. Everyone went about their lives as though he had never existed. [And] the entire incident was wiped from my record when I was sixteen.

But I thought about the shooting and Henry almost every day. And oddly enough, it's what drove me for a number of years. I wouldn't touch alcohol. I wouldn't smoke a cigarette. I just felt like I had to do him proud. I had to be perfect. And for a long period of time, I thought I was doing it. Successful career. Faithful husband. Doting father to my daughter.

When my daughter got sick at eighteen months, it pretty much derailed all of it. We rushed her to the hospital, her body was convulsing, and all of a sudden emotions and feelings I hadn't felt since I was 14 came rushing back. The feeling of panic. . . helplessness. And that's when it dawned on me, Maybe this is gonna be my sentence, that l'm gonna have to see what it's like to lose a child. Miraculously, she did survive, but the damage was done, and when we got back home, everything was completely different. I was terrified to be left alone with her. I felt like the second it was just me and her, something was gonna go wrong.

After she got sick, a recurring dream I was having about Henry began to repeat itself with disturbing frequency. Always the same dream: I'd be asleep, I'd wake up, and he'd be sitting on the edge of my bed, staring at me, with the bullet hole still in his chin.

I'd start talking to him. I'd say, "Hey, how are you doing?" and his blank face would show no expression. After a while, I'd start pleading with him, asking him if he knew how sorry I was -- if he knew it was an accident. I'd ask him if he knew how much I missed him. Finally he would open his mouth and try to respond, but just like on that day, the bullet stopped him from speaking, and he gasped for air. I'd wake up crying in bed.

This dream repeated itself for years. Fourteen, eighteen, twenty-one, twenty-five, thirty. It took me passing out on the train that day to realize I needed help.

Henry is dead, and I killed him. I honestly don't believe there's any amount of good I can do in my life that'll absolve me of his death. But my trying to live a life for two people, one of whom I can never bring back, was a recipe for disaster that was gonna doom me and everyone who cared about me.

My marriage died, but I lived on. My daughter's 13 years old now and healthy. I have an 8-year-old son. I hope both grow up to be wonderful people -- the type who bring so much joy to everyone around them that their absence would be a tragedy, because that's the type of person that Henry was.

He died 24 years ago, and it's still fresh. But I'm no longer miserable. In fact, I am well on my way to becoming one of the happiest people I know, and I think that fact would've made him happy. He also doesn't visit me in my dreams anymore, and I can finally admit that I'm comfortable with never seeing his face ever again, in my dreams or otherwise. Because at the end of the day, what would a man like me have to say to his 14-year-old friend that hasn't been said already?
```

---

## IC-2482: Perfect Moments

- Title: Perfect Moments
- Author (byline): Brian Finkelstein
- Work: The Moth, Pg 373-384
- Publisher: Hachette Books
- Publication date as stated: Sept 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: BRIAN, AMY
- Teaser before the introduction: Yes
- Spoken words (computed): 1225
- Already set (do not supply): none

### Source block (context only)

```text
Author: Brian Finkelstein
Book: The Moth, Pg 373-384
ISBN: 978-1401311117
Publisher: Hachette Books
Date (Month/Year): Sept 2013
```

### Introduction (context only: never use it for content warnings)

```text
Perfect Moments by Brian Finkelstein
```

### Performance text (classify this)

```text
BRIAN: (Pg 373-384) So the standard commitment to work at the Humanitarian Suicide Hotline is six months. Most people work six months, and then leave, quickly. A few make it a year. I was a volunteer there for four years. It started when I was twenty-two years old, and I believed in things. I thought I could help the world.

BRIAN: So one Saturday morning, I walk into this church, and there’s a bunch of people milling about, but I see this guy that’s clearly in charge. He tells us his name is Glen. And he's got a little bit of a Louis Gossett, Jr., drill sergeant thing going on, because as soon as he starts the training class, he's starting to weed people out.

One of the most important things Glen weeded out was people who were either suicide survivors, meaning they'd lost somebody because of suicide, or because they themselves, had contemplated suicide.

At the end of two weeks of training, out of fifty-eight people who came to volunteer, there were only four of us left, because Glen was really good . . . But I was better. Because what Glen didn't know about me was that about four years before this, I was dating this girl Tracy. Tracy slept with my best friend. And Glen didn't know that my father's a retired cop. I took his .38 and I drove to Torrey Pines Beach. Glen has no idea how good it feels to stick a loaded gun in your mouth . . to have control.

And I sat there, trying to contemplate doing it, and then . . . I threw up all over the gun. There's nothing snaps you out of a suicide impulse more than throwing up on a gun. And I thought to myself, Well, at least I know I'm not the type of person that's gonna pull the trigger. And I felt this moment of clarity. It was late at night. Beautiful full moon. I sat there and I realized that's what life is. There are these moments of beauty, like moons and oceans, and then there are moments of horror. And then it's good again. And for me that was enough. But Glen didn't know any of that because I never told him.

So, at the end of two weeks of training class we [are ready for] the hotline room. There's a sign that hangs on the wall that says the motto of the hotline, which is SHUT UP AND LISTEN. It's how you prevent suicides . . . by listening to people.

A lot of people think about suicide, but most people don't really go the next step. The closest thing to a warning sign for suicide is if somebody says something like "I don't want to die. I just want the pain to stop." And if you hear somebody say that -- that they want the pain to stop -- a bell should go off. That's a person who's on the edge. [I’ll never forget my last night at the hotline] . . .

BRIAN: Hello, Humanitarians, can I help you?

AMY: (scared) Hi. My name is Amy. I'd like to talk.

BRIAN: What's up, Amy? What's going on?

AMY: I was just calling because I was feeling a little sad.

BRIAN: Oh, what are you sad about?

AMY: Ah, I don't know, things are pretty good. I have good grades at school, and my parents don't get it, but they love me.

BRIAN: Well, that sounds good. But you said you were sad. What do you think about when that happens?

AMY: I don't know. I can't control it. Sometimes when I have a great day, I try to duplicate it. I wake up at the same time, I eat the same food, try to have the same pattern, so that I don't feel bad.

BRIAN: (to audience) But then, out of nowhere, she said, she felt a hand coming from behind her and pushing her down. (to Amy) Okay, what's going on when that happens? What are you thinking about?

AMY: Everything, nothing . . . I just feel so stupid.

BRIAN: (to audience) So we were [just] talking like that. And I noticed that it was about time to wrap it up, but Amy started telling me this story about going to some place with her family one day, and their father bought ice cream, and it was a great day. But then [she] started to slur her speech a little bit.

BRIAN: Amy, what's going on? Are you okay?

AMY: (slurred speech) Yeah. Look, I know it's selfish, but I can't do it anymore. I just want it to stop.

BRIAN: What do you mean? What do you mean by 'it'?

AMY: Look, I don't want to die. I just want the pain to stop.

BRIAN: (to audience) And I woke up. Amy, do you feel so bad that you think about suicide?

AMY: Yes.

BRIAN: Do you have a plan for how you would do it?

AMY: Yes.

BRIAN: Have you set a time for when you're gonna do it?

AMY: Uh-huh.

BRIAN: Amy, have you taken any steps today to kill yourself?

AMY: Yes.

BRIAN: Amy, what have you done? (to audience) And she told me she took twenty painkillers. And she started to cry. (to Amy) Amy, do you want help? Do you want me to do something? I can do something, but I can only help you if you ask. (to audience) Our policy was not to intervene unless people asked us to.

AMY: I do. I don't want to do this.

BRIAN: Great, what's your address? (to audience) She gave me her address and [as I alerted 911] I kept Amy talking. (to Amy) Uh, Amy, what kind of ice cream was it that your father bought you? You mentioned that your father bought you ice cream. What kind of ice cream was it? (to audience) But it was silent. And it was silent for two minutes. And it was silent for five minutes. And I'm supposed to hang up the phone, but who the hell could hang up the phone? So I didn't. And then around thirteen, fourteen minutes, I heard noises, people knocking, and then I heard the door crash open. And then I heard the phone being picked up, and a voice said, "It's okay. We've got her." Click.

I went home. I was supposed to go to class that day at Queens College. But I never went back. I never graduated. I was supposed to go back to the hotline for a debriefing based on that phone call. But I called Glen and told him I quit, that I wasn't coming back. And then I did all the things you're not supposed to do. I looked through the papers and listened to the radio, and finally, after three days, I found it. In the Daily News, page 23, a small paragraph that said they had found the body of a nineteen-year-old NYU student named Amy Walters who had died of an overdose.

I didn't know until that moment that she was dead, and I was the last person to talk to her. Not her mom, or her best friend, or some boy at NYU that probably had a crush on her but never talked to her. . . Me.

I spoke to her for less than an hour *many* years ago. But I think about it every day . . . She's me, in that car. If I had pulled the trigger, that would be me. And she never got to find out what I got to find out, which is it's terrible sometimes . . . but there are these perfect life moments . . . And that's enough.
```

---

## IC-2483: Pin

- Title: Pin
- Author (byline): Robert McCammon
- Work: Blue World (Pg 93-99)
- Publisher: Pocket
- Publication date as stated: April 1990
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JOEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1616
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert McCammon
Book: Blue World (Pg 93-99)
ISBN: 978-0671695187
Publisher: Pocket
Date (Month/Year): April 1990
```

### Introduction (context only: never use it for content warnings)

```text
According to the National Institutes of Health, not only can childhood trauma cause people to re-live the past over and over, a condition commonly known as PTSD; childhood trauma significantly increases the risk of developing some form of mental illness later in life. The American Academy of Pediatrics goes one step further and calls adverse childhood experiences “the single greatest unaddressed public health threat facing our nation today.”

Our young people are at risk. The result? Suicide and homicide are at the highest rates in decades (CDC, June
```

### Performance text (classify this)

```text
JOEY: (Pg 93-99) I’m going to do it. Yes. I am. I hold the pin in my hand, and tonight I’m going to peer into the inner sun. Then, when I’m filled up with all that glare and heat and my brain is on fire like a four-alarm blaze, I’m going to take my Winchester rifle down to the McDonald’s on the corner and we’ll see who says what to who when.

15, 2023) https://www.cnn.com/2023/06/15/health/youth-suicide-homicide/index.html And mass shootings? Most of the deadliest in the U.S. since 2018 were committed by those 21 or younger.

(https://www.axios.com/2022/06/02/mass-shooting-killers-young-teens) But statistics are easy to brush aside. Let me bring the issue of childhood trauma and its aftermath to you in a more compelling way. . . Meet Joey Shatterly a mentally ill young man who struggles with the compelling urge to inflict harm on others or himself.

Pin by Robert McCammon

JOEY: There you go, talking to yourself. Well, there’s nobody else around, is there, so who am I supposed to talk to? No, no; my friend’s here. Right here, in my hand. Pin. Oh, look at that little point gleam. It hypnotizes you, Pin does. It says look at me look long and hard and in me you will see your future. It is a very sharp future, and there is pain in it. Pin is better than God, because I can hold Pin. God frets and moans in silence, somewhere . . . up there.

Now, Johnny’s an okay guy. I mean, I wouldn’t shoot him. He’s okay. The others -- I don’t like the way they clam up when I walk past, like they’ve got secrets I’m not supposed to know anything about. Like you have secrets when you work on cars all day and fix tires and brake shoes and get that gunk under your fingernails that won’t ever wash out? Some secrets. Now, Pin . . . Pin does have secrets. Tonight, I’m going to learn them, and I’m going to share my knowledge with those people down on the corner eating their hamburgers in the safe, safe world.

The trick, I think, is not to blink. I’ve heard about people who did this before. They saw the inner sun, and they went out radiant. It’s always dark in this town. I think they need a little sunlight, don’t you?

Who’re you talking to, anyway? Me myself and I. Pin makes four. What else did you have to do in that place anyway? Oh, those white white walls. I saw that Baptist preacher on TV. He said come down the aisle come on while you can and I’ll show you the door to heaven. It’s a big white door, he said. And he smiled when he said it, and the way he smiled, he was really saying, Joey you know all about big white doors, don’t you, and how when they swing shut you hear the latch fall and the key rattle and that big white door won’t open again until somebody comes and opens it. There was always a long time between the closing and the opening.

I’ve always wanted to be a star. Like on TV or movies, somebody important. People like that always look like they know where they’re going and they’re always in a hurry to get there. Well, I know where I’m going now. Right down to the corner, where the golden arches are. Look out my window, I can see it. There goes a car turning in. Going to be full up on a Saturday night. My Winchester has a seven-shot magazine. I have more bullets, too. Saturday night. Date night. I hope she’s there. That girl. You know the one. She drives a blue Camaro and she has long blond hair and eyes like diamonds. Diamonds are hard, but you hit one with a bullet and it’s not so hard anymore. Pin, we won’t think about her, will we? Nope! If she’s there it’s fate. Maybe I won’t shoot her, and she’ll see I’m a nice guy.

Hold Pin close. Closer. Closer still. Up against the right eye. I’ve thought a long time about this. It was a tough decision. Left or right? I’m right-handed, so it makes sense to use my right eye. I can already see the sun sparkle on the end of Pin, like a promise.

Oh, what I could do with a machine gun. Eliot Ness, Untouchables, tommy-gun-type thing. I sure could send a lot of people behind that big white door, couldn’t I? See, the funny thing is that everybody wants to go to heaven but everybody’s scared to die. That’s what I’m going to say when the light comes on and that news guy sticks a microphone in my face. I need to shave first. I need to wear a tie. No, they won’t know me with a tie on. I need to wear my gray uniform – gray, now there’s a man’s color. Pick you up good on TV in gray.

Speak to me, Pin. Say it won’t hurt. It has to be in the center. In that black part. It has to go in deep. Real deep, and you have to keep pushing it in until you see the inner sun. You know, I’ll bet that part’s dead anyway. I’ll bet you can’t even feel any pain in the black part. Just push it in and keep pushing, and you’ll see that sunburst and then you can go down and have a hamburger when it’s all said and done.

Closer. Almost touching. Don’t blink! Cowards blink, nobody can ever say Joey Shatterly’s a coward no sir! Wait. Wait. I think I need a mirror for this.

(Sniffs under his arms) Ban roll-on. You don’t want to smell when they turn the lights on you. Oh hell, I’m out of Ban. Old Spice that’ll do. My dad used to use Old Spice. Now, that was a good day, when we saw the Reds play the Pirates and he bought me a bag of peanuts and said he was proud of me. That was a good day.

He was a Marine. I remember that Iwo Jima crap when he got crazy and drank all the time -- Iwo Jima Iwo Jima -- he lived it in his mind a million times. You got sick of hearing who all died at Iwo Jima and how come you ought to be proud to be an American and how things weren’t how they used to be. Nothing is, is it? Except Old Spice. Iwo Jima Iwo Jima. And then he went and did it, put the rope up in the garage and stepped off the ladder and me coming in to get my bike and that grin on his face that said Iwo Jima.

Oh, Ma, I didn’t mean to find him. Why didn’t you go in there so you could hate yourself?

Now, that was a good day, when we saw the Reds play the Pirates and he bought me a bag of peanuts and said he was proud of me. He was a real Marine.

The black part looks small in the mirror, small as a dot. But Pin’s smaller. Sharp as truth. My Winchester holds seven bullets. Pin, you’re so beautiful. I want to learn things. I want to know secrets. In the glare of the inner sun I will walk tall and proud like a Marine on the hot sands of Iwo Jima. Closer, Pin. Closer still. Almost there. Close against the black part, the unblinking black. Look in the mirror, don’t look at Pin. Don’t blink! Closer. Steady, steady. Don’t . . . Dropped. Don’t go down the sink! Get Pin, get it! Don’t let it go . . .

Who blew that horn? Camaro, wasn’t it? Blond girl at the wheel? Seven bullets. I’ll make a lot of horns blow.

Nothing’s how it used to be. The whole world is turning faster and faster and sometimes I hold on to my bed because I’m scared the world is going to throw me off. So, I hang on and my knuckles get white and pretty soon I can stand up and walk again. Baby steps.

How straight and strong Pin is, like a little silver arrow. My friend, my key to light and truth. You shine and wink, and you say take your Winchester to the golden arches where Marines fear to tread.

I’m going to do it. Yes. I am. Closer. Closer. You will not blink. No. You will not. Pin will take care of you. Pin will lead you. Think about something else. Think about . . . Iwo Jima.

One jab. Quick. OW! Hurts. Hurts like truth. Yes it does. Another jab. Quick. Oh, Jesus. Deeper. Little bit deeper. I was wrong the black part isn’t dead. Deeper. Got to see the inner sun. Joey Shatterly’s no coward no sir no sir. Deeper. Streak of light that time. Blue light. Oh, it hurts. Oh oh . . . Dad where’s my bike?

Pin, sliding in. Slow. Cold steel. I love you, Dad. Pin, show me the truth show me show me show . . . Deeper. Though the pulse. White’s turned red. Seven bullets, seven names. Deeper, to the center of the inner sun. Oh! There! I saw it! Right there! I saw a flash of it push it deeper into the brain where the inner sun is! A flash of light! Please. Almost there.

White light. Flashbulb. Hi, Ma! Oh . . . there . . . right there . . . I love you, Dad . . . Ma, I’m so sorry I had to find him I didn’t mean to I didn’t . . . One more push. A little one. Pin is almost gone. My eye is heavy, freighted with sight . . .

Pin, sing to me.
```

---

## IC-2484: A Plague of Tics

- Title: A Plague of Tics
- Author (byline): David Sedaris
- Work: Naked
- Publisher: Back Bay Books
- Publication date as stated: June 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2545
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
Obsessive-compulsive disorder (OCD) is an illness that causes people to have unwanted thoughts (obsessions) and to repeat certain behaviors (compulsions) over and over again. We all have habits and routines in our daily lives, such as brushing our teeth before bed. However, for people with OCD, patterns of behavior get in the way of their daily lives. Most people with OCD know that their obsessions and compulsions make no sense, but they can't ignore or stop what quickly becomes . . . A Plague of Tics by David Sedaris
```

### Performance text (classify this)

```text
When the teacher asked if she might visit with my mother, I touched my nose eight times to the surface of my desk.

"May I take that as a 'yes'?" she asked.

According to her calculations, I had left my chair twenty-eight times that day. "You're up and down like a flea. I turn my back for two minutes and there you are with your tongue pressed against that light switch. Maybe they do that where you come from, but here in my classroom we don't leave our seats and lick things whenever we please. That is Miss Chestnut's light switch, and she likes to keep it dry. Would you like me to come over to your house and put my tongue on your light switches? Well, would you?"

I tried to picture her in action, but my shoe was calling. Take me off, it whispered. Tap my heel against your forehead three times. Do it now, quick, no one will notice.

"Well?" Miss Chestnut raised her faint, penciled eyebrows. "I'm asking you a question. Would you or would you not want me licking the light switches in your house?" I slipped off my shoe, pretending to examine the imprint on the heel. "You're going to hit yourself over the head with that shoe, aren't you?" It wasn't "hitting," it was tapping; but still, how had she known what I was about to do? "Heel marks all over your forehead," she said, answering my silent question. "You should take a look in the mirror sometime. Shoes are dirty things. We wear them on our feet to protect ourselves against the soil. It's not healthy to hit ourselves over the head with shoes, is it?" I guessed that it was not. "Guess? This is not a game to be guessed at. I don't 'guess' that it's dangerous to run into traffic with a paper sack over my head. There's no guesswork involved. These things are facts, not riddles." She sat at her desk, continuing her lecture as she penned a brief letter. "I'd like to have a word with your mother. You do have one, don't you? I'm assuming you weren't raised by animals. Is she blind, your mother? Can she see the way you behave, or do you reserve your antics exclusively for Miss Chestnut?" She handed me the folded slip of paper. "You may go now, and on your way out the door I'm asking you please not to bathe my light switch with your germ-ridden tongue. It's had a long day; we both have."

It was a short distance from the school to our rented house, no more than six hundred and thirty-seven steps, and on a good day I could make the trip in an hour, pausing every few feet to tongue a mailbox or touch whichever single leaf or blade of grass demanded my attention. If I were to lose count of my steps, I'd have to return to the school and begin again. "Back so soon?" the janitor would ask. "You just can't get enough of this place, can you?" Depressing as it was, arriving at the front stoop of the house meant that I had completed the first leg of that bitter-tasting journey to my bedroom. Once home I would touch the front door seven times with each elbow, a task made more difficult if there was someone else around. "Why don't you try the knob," my sister Lisa would say. "That's what the rest of us do, and it seems to work for us." Inside the house there were switches and doorstops to be acknowledged. My bedroom was right there off the hallway, but first I had business to tend to. After kissing the fourth, eighth, and twelfth carpeted stair, I wiped the cat hair off my lips and proceeded to the kitchen, where I was commanded to stroke the burners of the stove, press my nose against the refrigerator door, and arrange the percolator, toaster, and blender into a straight row. After making my rounds of the living room, it was time to kneel beside the banister and blindly jab a butter knife in the direction of my favorite electrical socket. There were bulbs to lick and bathroom faucets to test before finally I was free to enter my bedroom, where I would carefully align the objects on my dresser, lick the corners of my metal desk, and lie upon my bed, rocking back and forth and thinking of what an odd woman she was, my third-grade teacher, Miss Chestnut. Why come here and lick my switches when she never used the one she had? Maybe she was drunk. Her note had asked if she might visit our home in order to discuss what she referred to as my "special problems." "Have you been leaving your seat to lick the light switch?" my mother asked. She placed the letter upon the table and lit a cigarette.

"Once or twice," I said. "Once or twice what? Every half hour? Every ten minutes?" "I don't know," I lied. "Who's counting?" "Well, your math teacher, for one. That's her job, to count. What, do you think she's not going to notice?" "Notice what?" It never failed to amaze me that people might notice these things. Because my actions were so intensely private, I had always assumed they were somehow invisible. "And I suppose this Miss…" My mother unfolded the letter and studied the signature. "This Miss Chestnut is mistaken? Is that what you're trying to tell me? Maybe she has you confused with the other boy who leaves his seat to lick the pencil sharpener or touch the flag or whatever the hell it is you do the moment her back is turned?" "That's very likely," I said. "She's old. On the afternoon that Miss Chestnut arrived for her visit, I was in my bedroom, rocking. Unlike the obsessive counting and touching, rocking was not a mandatory duty but a voluntary and highly pleasurable exercise. It was my hobby, and there was nothing else I would rather do. The point was not to rock oneself to sleep: This was not a step toward some greater goal. It was the goal itself. The perpetual movement freed my mind, allowing me to mull things over and construct elaborately detailed fantasies. Toss in a radio, and I was content to rock until three or four o'clock in the morning, listening to the hit parade and discovering that each and every song was about me. I might have to listen two or three hundred times to the same song, but sooner or later its private message would reveal itself. Because it was pleasant and relaxing, my rocking was bound to be tripped up, most often by my brain, which refused to allow me more than ten consecutive minutes of happiness. At the opening chords of my current favorite song, a voice would whisper, Shouldn't you be upstairs making sure there are really one hundred and fourteen peppercorns left in that small ceramic jar? And, hey, while you're up there, you might want to check the iron and make sure it's not setting fire to the baby's bedroom. The list of demands would grow by the moment. What about that television antenna? Is it still set into that perfect V, or has one of your sisters destroyed its integrity. You know, I was just wondering how tightly the lid is screwed onto that mayonnaise jar. Let's have a look, shall we? I was coming to terms with "The Shadow of Your Smile" when Miss Chestnut arrived. She rang the bell, and I cracked open my bedroom door, watching as my mother invited her in. I tried rocking in bed, but the sound of laughter drew me to the top of the landing, where from my vantage point behind an oversized wardrobe box, I watched the two women discuss my behavior. "Oh, you mean the touching," my mother said. She studied the ashtray that sat before her on the table, narrowing her eyes much like a cat catching sight of a squirrel. Her look of fixed concentration suggested that nothing else mattered. Time had stopped, and she was deaf to the sounds of the rattling fan and my sisters' squabbling out in the driveway. She opened her mouth just slightly, running her tongue over her upper lip, and then she inched forward, her index finger prodding the ashtray as though it were a sleeping thing she was trying to wake. I had never seen myself in action, but a sharp, stinging sense of recognition told me that my mother's impersonation had been accurate. "Priceless!" Miss Chestnut laughed, clasping her hands in delight. "Oh, that's very good, you've captured him perfectly. Bravo, I give you an A-plus." "God only knows where he gets it from," my mother said. "He's probably down in his room right this minute, counting his eyelashes or gnawing at the pulls on his dresser. One, two o'clock in the morning and he'll still be at it, rattling around the house to poke the laundry hamper or press his face against the refrigerator door. The kid's wound too tight, but he'll come out of it. Following Miss Chestnut's visit, my father attempted to cure me with a series of threats. "You touch your nose to that windshield one more time and I'll guarantee you'll wish you hadn't," he said driving home from the grocery store with a lapful of rejected, out-of-state coupons. It was virtually impossible for me to ride in the passenger seat of a car and not press my nose against the windshield, and now that the activity had been forbidden, I wanted it more than anything. I tried closing my eyes, hoping that might eliminate my desire, but found myself thinking that perhaps he was the one who should close his eyes. So what if I wanted to touch my nose to the windshield? Who was it hurting? Why was it that he could repeatedly worry his change and bite his lower lip without the threat of punishment? My mother smoked and Miss Chestnut massaged her waist twenty, thirty times a day — and here I couldn't press my nose against the windshield of a car? I opened my eyes, defiant, but when he caught me moving toward my target, my father slammed on the brakes. "You like that, did you?" He handed me a golf towel to wipe the blood from my nose. "Did you like the feel of that?" Like was too feeble for what I felt. I loved it. If mashed with the right amount of force, a blow to the nose can be positively narcotic. Touching objects satisfied a mental itch, but the task involved a great deal of movement: run upstairs, cross the room, remove a shoe. I soon found those same urges could be fulfilled within the confines of my own body. Punching myself in the nose was a good place to start, but the practice was dropped when I began rolling my eyes deep in their sockets, an exercise that produced quick jolts of dull, intoxicating pain. "I know exactly what you're talking about," my mother said to Mrs. Shatz, my visiting fourth-grade teacher. "The eyes rolling every which way, it's like talking to a slot machine. Hopefully, one day he'll pay off, but until then, what do you say we have ourselves another glass of wine?" "Hey, sport," my father said, "if you're trying to get a good look at the contents of your skull, I can tell you right now that you're wasting your time. There's nothing there to look at, and these report cards prove it." I took to violently shaking my head, startled by the feel of my brain slamming against the confines of my skull. It felt so good and took so little time; just a few quick jerks and I was satisfied for up to forty-five seconds at a time. "Have a seat and let me get you something cool to drink." My mother would leave my fifth- and then my sixth-grade teachers standing in the breakfast nook while she stepped into the kitchen to crack open a tray of ice. "I'm guessing you're here about the head-shaking, am I right?" she'd shout. "That's my boy, all right, no flies on him." She suggested my teachers interpret my jerking head as a nod of agreement. "That's what I do, and now I've got him washing the dishes for the next five years. I ask, he yanks his head, and it's settled. This was part of my mother's act. She played the ringleader, blowing the whistle and charming the crowd with her jokes and exaggerated stories. She noticed my tics and habits but was never shamed or seriously bothered by any of them. Her observations would be collected and delivered as part of a routine that bore little resemblance to our lives. I'd like to think that some of my nervous habits faded during high school, but my class pictures tell a different story. "Draw in the missing eyeballs and this one might not be so bad," my mother would say. In group shots I was easily identified as the blur in the back row. For a time I thought that if I accompanied my habits with an outlandish wardrobe, I might be viewed as eccentric rather than just plain retarded. I was wrong. Only a confirmed idiot would wander the halls of my high school dressed in a floor-length caftan; as for the countless medallions that hung from around my neck, I might as well have worn a cowbell. They clanged and jangled with every jerk of my head, calling attention when without them I might have passed unnoticed. My oversized glasses did nothing but provide a clearer view of my rolling, twitching eyes, and the clunky platform shoes left lumps when used to discreetly tap my forehead. I was a mess. "College is the best thing that can ever happen to you," my father used to say, and he was right, for it was there that I discovered drugs, drinking, and smoking. I'm unsure of the scientific aspects, but for some reason, my nervous habits faded about the same time I took up with cigarettes. Maybe it was coincidental or perhaps the tics retreated in the face of an adversary that, despite its health risks, is much more socially acceptable than crying out in tiny voices. Were I not smoking, I'd probably be on some sort of medication that would cost the same amount of money but deny me the accoutrements: the lighters I can thoughtlessly open and close, the ashtrays that provide me with a legitimate reason to leave my chair, and the cigarettes that calm me down while giving me something to do with my hands and mouth. It's as if I had been born to smoke, and until I realized it, my limbs were left to search for some alternative. Everything's fine as long as I know there's a cigarette in my immediate future. The people who ask me not to smoke in their cars have no idea what they're in for.
```

---

## IC-2485: Prayer for What

- Title: Prayer for What
- Author (byline): Robert C. Reinhart
- Work: Telling Moments
- Publisher: Applause Theatre Books
- Publication date as stated: 1994
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1326
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert C. Reinhart
Book: Telling Moments
ISBN: 978-1557831637
Publisher: Applause Theatre Books
Date (Month/Year): 1994
```

### Introduction (context only: never use it for content warnings)

```text
There are a high number of homosexual priests and seminarians in the United States. How high is difficult to say. (Estimates range from 23 percent to 58 percent, with even higher percentages for younger priests.) That a high number of priests share a similar characteristic means that the church needs to consider both the challenges and the gifts offered by this group-- men who seek to serve God and the church with their whole selves. Prayer for What by Robert C. Reinhart
```

### Performance text (classify this)

```text
There she is again. Always that same awful black dress. I never see her at Mass or taking communion. Why does she come here? Lapsed Catholic? Too cold out? Crazy? It feels colder in here. I should go speak to her. No. If I leave her alone, she'll leave me alone.

She's lighting another candle. That's the third candle she's lit and I still haven't heard any money go into the box. Oh, God, she's turning around. Don't see me. You've lit your candle, lady, why don't you go home and give me a few minutes alone? I just want some peace and I can't even find it in my own church. Light another free candle. Be my guest.

Are you here because you've sinned, lady? Big sins? Little sins? Venial? Mortal? I'm tired of confessing. God, give me some new sins. Give poor Father Gilberti a break. I confess the same things every week, and he gives me the same advice and the same penance. "Bless me, father, for I am about to bore you to death. I have had frequent impure thoughts, had...accidents." What else can I call them?

What must Mrs. Cleary think? We playa game: It didn't happen and she doesn't know and I don't wash my sheets under cover of darkness. I'm the Phantom Laundryman, down in the laundry room at three in the morning, wondering if Father Gilberti can hear that damned old washing machine screaming away. I turn my Walkman up and pretend that old machine won't wake the dead. And I plug in that old iron and pray it won't blow the fuses again or electrocute me.

And how would that saintly old man take hearing that I take the cross off my wall because I can't keep my eyes off it? Who sculpted that incredibly beautiful body?

You lied, Father Flynn. In the seminary you said this passed. "Once you're working eighteen hours a day in some parish, me boy, you'll go to bed too tired to even think of it," says he. "You'll see, me boy, there is no room for impure thoughts in exhausted minds." Wrong, Father Flynn, there's room for an army of them in there.

And when I told him I had "tendencies." "Tendencies?" says he. "Well-er, ah, em-tendencies, you say? Ah, those tendencies. Well, terrible as they are in the eyes of Christ, those...tendencies...won't keep you from serving your savior if you don't act on them. Shower alone, me boy. Shower alone." The road to salvation is flooded with cold water.

And the old fraud must have told George the same thing. "Shower, George, shower." No wonder they said George was crazy. Water on the brain. But he didn't look crazy when I found him. He looked exhausted. No, he looked as if he was pleading with me, as if he wanted me to help him. How could he do that to himself and then just sit there waiting to bleed to death?

I couldn't understand what I was seeing, and now I can't stop seeing it...over and over. How did he do that much damage with that dull knife? And that filthy blue rag in his mouth. Couldn't understand that for days. Of course he bit it to keep from screaming. Just sitting there on the stones in his blood and not saying a word, just trying to beat me off, just trying to get me to leave him the hell alone. Father Shay said it was God's will that I found him and I should thank God. I don't. I just don't want George to hate me for stopping him. What did they do with him? Doesn't matter. Now he's no good to God or man.

She's lighting another candle and I still didn't hear any money go in the box. I really should speak to her. Oh, to hell with it. Go ahead, light them all, lady.

What keeps me here? God help me, I don't give a damn about people. I only half listen to them. I tell them things I only half believe, but they look at me and they hope I do, because if I don't believe, what's left? Oh, yes, my child, there's hope in hopeless situations. There, there. It's God's will. Throw them a little something to keep terrible things from scaring them to death, to keep them from wanting to kill me for being a fraud. Can't be the cause of murderous thoughts in their hearts. That would be leading them into sin.

Confessions are the worst. How do I hear another confession from some poor man who's had sex with another man? "Your immortal soul is in grave danger. Say thirty 'Hail. Marys.'" No, say twenty-nine...we're having a special. How do I tell that man who lives with his lover that he must not touch his Edmund or sleep with him? Every week I tear another piece off him. He asks me why God sent him Edmund to love if it's a mortal sin? It is God's way of testing you and you must cease sinning. I want to tell him to stop coming to me before Edmund gets fed up and leaves him. And wouldn't that be a sin

But I want to tell all the men to run, even that wretched man who tells me he lusts after little boys. I tell him to honor his marriage. I give him endless rosaries to say, just to keep him busy. Not busy enough. I tell all the married men to avoid the occasions of sin with other men and while I listen I want to know more, to have them whisper every detail through the grill.

And damn that man with the sexy voice. He does tell me everything. He talks so softly that I have to put my ear right against the grill and then I can feel his breath on my ear. He tells me he doesn't want to lose his soul, but he can't give up life, be celibate like me. I tell him to pray, to want a family, to want a woman. I dread his confessions because I want to know what he looks like. Sometimes I'm sure he's not a penitent, but some man who knows all about me and tells me these awful things because he knows. And when I'm alone, I imagine he confesses to me, because he wants me.

Someday one of them will say, "You don't believe any of this, why should 17"

God! I come here to be alone to think, but I can't stand what I think.

I must stop this. Keep your eye on that woman. Think about what brings her here, keeps her lighting all those candles? They aren't free, lady. But maybe her soul is seeping out of her or she comes here to hide, so IT-that big IT won't get her. God help me, lady, I should care about you, but I don't.

Well, I can't stay here forever. I'm stiff and it's damned cold in here. Get moving, Francis. Mrs. Cleary will give you hell if you're late for dinner again. And that man's coming for instruction. We both know he's converting to please his fiancée, but I can't just tell him he's a liar, that he doesn't want faith. Oh, and there's that damned ladies' sodality meeting tonight.

I must tell Mrs. Cleary to put more bleach in the wash. The altar cloths look dingy. How long has it been since the brass has been polished or the marble shined? I can even see the dust on the grillwork over the stained glass from here. My God, what kind of world do we live in that forces us to put stained glass in cages? Dear God, where is people's respect for churches? Why in the world should churches have to protect themselves from people?
```

---

## IC-2486: Proud to be a Blerd

- Title: Proud to be a Blerd
- Author (byline): Omar Holman and Daniel Beaty
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Prose
- Record type: Program
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1384
- Already set (do not supply): none

### Source block (context only)

```text
Author: Omar Holman
Book: We Were All Someone Else Yesterday, Pgs 93-96
ISBN: 978-1943735686
Publisher: Button Poetry
Date (Month/Year): May 2020
Author: Omar Holman
On-line Transcript:
https://destinyspoetrymovements.weebly.com/slam.html
Date (Month/Year): Performance at NYC-Urbana 2010
Finals at the Bowery Poetry Club, May 2010
Access video at:
https://www.youtube.com/watch?v=FP2gDoZPeOI&t=1s
Author: Daniel Beaty
Book: Transforming Pain to Power: Unlock Your
Unlimited Potential
ISBN: 978-0425267486
Publisher: Berkley
Date (Month/Year): March 2014
Found on-line at https://www.answers.com/music-and-
radio/What_are_the_lyrics_to_Duality_Duel_by_Daniel_
Beaty
```

### Introduction (context only: never use it for content warnings)

```text
The word “blerd” was coined in the late 1990s; meaning the experience of growing up as a Black person who has nerdy interests. The first signs of popularity began with Steve Urkel, an obnoxious and nerdy character on the show “Family Matters.” With every . . . “Did I do that?” Urkel made his way into the hearts of viewers; and more importantly, he validated the feelings of Black nerds just like him.

Today, with various online communities and groups, the ‘nerd’ segment of the Black population can easily find kindred spirits while staying true to their identity. We are more than just “athletic.” We are not all “thugs,” gang members or criminals. We are unique and today Black creativity is celebrated and embraced.

Proud to be a Blerd with poems by Omar Holman and Daniel Beaty
```

### Performance text (classify this)

```text
Trigger Warning: Contains the “N” word referring to Black men

10 Things I Want to Say to a Black Nerd by Omar Holman (Pg 93-96)

After Jenifer Falu’s “10 Things I want to say to a Black Man”

1 - It’s so hard being a Black nerd
2 - The books you love
don’t have many heroes or villains that look like you
It’s not the color but the content of
the characters that keep you reading

3 - You thank God for Donald Glover
and his songs as Childish Gambino
Listening to him is the like having Nikola Tesla sitting
shotgun in The Delorean
while doing Pi …sorry, “donuts” in a Game Stop
parking lot, top down as Tesla says,
“Is that the new Afrofuturism mixtape?
Homie, TURN. THAT. SHIT. UP!”

4 - Batman’s superpower
is generational wealth and stock options.
That has nothing to do with the rest of the poem,
I just felt it really needed to be said

5 - There is nothing more beautiful than a Black nerd girl
Any time you hear ’em rep their fandoms,
you Dance Dance Revolutions round your heart
If she has natural hair
and wants to converse about Converse?
+10 damage points
Talks trash whenever she beats you in Mario Kart?
+25 skill points
If she watches Craig of Creek
and writes her own fan fiction,
there’s, no calculation for how sexy that is

6 - When you get the girl,
you’ll remember every detail,
like how the paint on her nails
chips into isolated islands
When you get the boy, you’ll reminisce
on how he made oblivious look like the new abstinence
When you have each other,
you’ll recall the memory as an 8-bit adventure;
call it old-school, call it classic,
whatever symbolizes
that the moment was an arcade high score
you both achieved together

7 - Your most hood moment on Game of Thrones
when they killed Ned Stark
Even as I mention it now,
inside you’re saying to yourself,
“They killed my n****a Ned Man”
They killed my ni***a Ned!”
For nerds, Ned Stark’s death is equivalent to
when Hip-Hop heads lost Biggie Smalls
or when Friends went off the air for white people

8 - Your black friends say
hand over your black card
because you never watched “The Wire”
Your white friends think,
having watched “The Wire,”
it’s okay for them to say
they’re “blacker” than you are
since nerd is the new Black,
so, “Everybody wanna be a nerd
but don’t nobody wanna be a nerd”

9 - A nerd-off is the closest you will ever come
to battle rap
It occurs whenever someone
corrects you on a topic obnoxiously
If you engage in this Battle Royale of facts,
your retort should always sound something like this:
“Actually, Blade is the movie that kick-started all these
other superhero movies …”
and once you see that look of
“Oh they ‘bout murder me” on their face,
you Highlander them with a stare that says,
“You goin’ get this work,
cause I’m a Grayskull graduate
with a Masters in the Universe
and you ain’t ‘bout this life, B”

10 - It is so hard being a Black nerd,
slinging six-sided-dice on the block,
keeping it retro
when you pop out the Nintendo 64
like it’s an Impala,
all Black everything
because that’s what you’ve always been …

everything.
From
Chuck Taylors to lightsabers
From
“Press Start” to “Game Over”

I am Nerd by Omar Holman

I heard they want to abolish the “n” word
but I am the “n” word,
the "n" word is me,
I am that nerd.
I am that nerd that “cool” passed up in high school.
Left standing against the walls at school dances,
snapping my fingers to the music,
asking ladies "Dance?
No, okay that's cool. Dance?

Hell no, okay that's cool. I'm still good."

I am that nerd,
that never scored the winning touchdown for the team
but was an English class MVP.
Report cards looking like Duracell batteries, triple A's.
Standing on top of my desk,
with a one hundred percent on my test,
yelling out "Who want it with me?"
I'm Oscar Wildin' Out, Rob. You can't defrost me.
I'm stone cold Jane Austin out this b****.

I am that nerd,
it was I who was online 25 days, 4 hours, and 5 minutes.
Yes, it was I who stood in line waiting 18 hours for Halo 3.
If Carrie Underwood were dating me,
there would be no car for her to key.
She'd have to sing while scratching my Xbox 360,
taking a Louisville slugger to both controllers,
while singing . . .
"Next time, he'll maybe think twice before he uses a cheat

code on me."

Yes, that nerd is me. Therefore, I'm entitled to be that geek with the vast

knowledge of
Mangas, Animes, and comic books;
since these are the foundations of our culture.
Thus in the name of Harry Potter, Goku, Optimus Prime,

He Man, Sailor Moon . . . (chanting/singing) *Thunder, Thunder, Thunder, Thunder Cats -- Hoooo!

But once 12 o'clock came, it was all over when you heard

Soul Train.
You remember me from 2nd period chemistry.
I'm that geek with no need for using a third eye;
I'm equipped with four eyes.
The pocket protector stays strapped, what you need?
Ruler, pen, calculator, I got that.

So, know that it is me who rocks different super hero shirts for everyday of the week. Yes, it is I who’s obsessed with Green Lantern and The

Space Police.

We harass Jedis, while pulling over Autobots and

Decepticons Because this is training day in outer space and Voltron ain't got sh** on me.

Duality Duel by Daniel Beaty
There's a battle going on inside of me
Between my well-crafted external persona
and an internal force trying to break free.
It's a battle you see, between the nerd,
and the n****r in me.
Can the nerd and the n*** a coexist?
They 'gon have to nerd
But Ni***!-
It doesn't make sense.
I didn't spend four years in the Ivy League,
learning how to think, talk, and feel,
in order to jump into a rage every time they try and kill

me. But the truth is Nerd, I've always been around: When that

Poison Ivy bullsh*t was beating you down, these

strong arms, they held you: told you not to feel it. Gave you time enough to heal it and become a Nerd

again.

But N***a! All you seem to feel is rage and that will keep me out of

their circles and off the front page of the New York

Times and the Daily News. Not if you shoot a *man.* And that's my point. You are more than that cold stony

glare, those weighty Timberlands and that nappy hair. Aw hold up now! No N***a! That rage is like a cage that keeps love out and

you in jail.

Aww shut up Nerd! You ain't heard a word I said. I gotta

smack you upside yo well-brushed head? Without me

there is no you.

No wait a minute N***a, let's talk this through. Naw Nerd! Journey to the n***a in you. I've been inside

long enough, I got ya through school, gave you time

enough to learn their rules. Now the time has come to

pay your dues. Cuz these little n****s in the street, they need you. But they think they can't relate cuz you act all removed. When the truth is Nerd; what they are is you. Cuz no matter how hard you try to deny the way you

think, talk, and feel, ghetto nightmares still haunt your

dreams, and your Mamma is still black. I ain't saying you gotta become me, but this one thing is

true; inside you is a harda** n***a, you gotta let him come

through. Cuz this assimilating bullsh*t will surely beat you down. You choke me long enough, I will not stick around. Put the strut back in your walk. Say what you really feel. Be all of you, so all of us can heal. The time for lying and denying is through. It's time Nerd, journey to the N***a in you.

*Theme from ThunderCats can be found here: https://www.youtube.com/watch?v=Na8ThDftsKk&t=1s
```

---

## IC-2487: The Rake: A few Scenes from my Childhood

- Title: The Rake: A few Scenes from my Childhood
- Author (byline): David Mamet
- Work: The Cabin: Reminiscence and Diversions
- Publisher: Vintage
- Publication date as stated: November 1993
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2525
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Mamet
Book: The Cabin: Reminiscence and Diversions
ISBN: 978-0679747208
Publisher: Vintage
Date (Month/Year): November 1993
```

### Introduction (context only: never use it for content warnings)

```text
For some things in life, you don’t get a choice -- like your family. No matter what happens – good or bad – family is the one institutional relationship that stands the test of time. However, quite often the bad memories also stand the test of time. Sometimes childhood nostalgia can be brought on by a simple household item, such as, “The Rake: A few Scenes from my Childhood” by David Mamet
```

### Performance text (classify this)

```text
There was the incident of the rake and there was the incident of the school play, and it seems to me that they both took place at the round kitchen table.

The table was not in the kitchen proper but in an area called the nook, which held its claim to that small measure of charm by dint of a waist-high wall separating it from an adjacent area known as the living room.

All family meals were eaten in the nook. There was a dining room to the right, but, as in most rooms of that name at the time and in those surroundings, it was never used.

The round table was of wrought iron and topped with glass; it was noteworthy for that glass, for it was more than once and rather more than several times, I am inclined to think, that my stepfather would grow so angry as to bring some object down on the glass top, shattering it, thus giving us to know how we had forced him out of control.

And it seems that most times when he would shatter the table, as often as that might have been, he would cut some portion of himself on the glass, or that he or his wife, our mother, would cut their hands on picking up the glass afterward, and that we children were to understand, and did understand, that these wounds were our fault.

So the table was associated in our minds with the notion of blood. The house was in a brand-new housing development in the southern suburbs. The new community was built upon, and now bordered, the remains of what had once been a cornfield. When our new family moved in, there were but a few homes in the development completed, and a few more under construction. Most streets were mud, and boasted a house here or there, and many empty lots marked out by white stakes.

The house we lived in was the development's Model Home. The first time we had seen it, it had signs plastered on the front and throughout the interior telling of the various conveniences it contained. And it had a lawn, and was one of the only homes in the new community that did.

My stepfather was fond of the lawn, and he detailed me and my sister to care for it, and one fall afternoon we found ourselves assigned to rake the leaves.

Why this chore should have been so hated I cannot say, except that we children, and I especially, felt ourselves less than full members of this new, cobbled-together family, and disliked being assigned to the beautification of a home that we found unbeautiful in all respects, and for which we had neither natural affection nor a sense of proprietary interest.

We went to the new high school. We walked the mile down the open two-lane road on one side of which was the just-begun suburban community and on the other side of which was the cornfield.

The school was as new as the community, and still under construction for the first three years of its occupancy. One of its innovations was the notion that honesty would be engendered by the absence of security, and so the lockers were designed and built both without locks and with-out the possibility of attaching locks. And there was the corresponding rash of thievery and many lectures about the same from the school ad-ministration, but it was difficult to point with pride to any scholastic or community tradition supporting the suggestion that we, the students, pull together in this new, utopian way. We were, in school, in an uncompleted building in the midst of a mud field in the midst of a corn-field. Our various sports teams were called The Spartans; and I played on those teams, which were of a wretchedness consistent with their novelty.

Meanwhile my sister interested herself in the drama society. The year after I had left the school she obtained the lead in the school play. It called for acting and singing, both of which she had talent for, and it looked to be a signal triumph for her in her otherwise unremarkable and unenjoyed school career.

On the night of the play's opening, she sat down to dinner with our mother and our stepfather. It may be that they ate a trifle early to allow her to get to the school to enjoy the excitement of opening night. But however it was, my sister had no appetite, and she nibbled a bit at her food, and then she got up from the table to carry her plate back to scrape it in the sink, when my mother suggested that she sit down, as she had not finished her food. My sister said she really had no appetite, but my mother insisted that, as the meal had been prepared, it would be good form to sit and eat it.

My sister sat down with the plate and pecked at her food and she tried to eat a bit, and told my mother that, no, really, she possessed no appetite whatever, and that was due, no doubt, not to the food, but to her nervousness and excitement at the prospect of opening night.

My mother, again, said that, as the food had been cooked, it had to be eaten, and my sister tried and said that she could not; at which my mother nodded. She then got up from the table and went to the telephone and looked the number up and called the school and got the drama teacher and identified herself and told him that her daughter wouldn't be coming to school that night, that, no, she was not ill, but that she would not be coming in. Yes, yes, she said, she knew her daughter had the lead in the play, and, yes, she was aware that many children and teachers had worked hard for it, et cetera, and so my sister did not play the lead in her school play. But I was long gone, out of the house by that time, and well out of it. I heard that story, and others like, at the distance of twenty-five years.

In the model house our rooms were separated from their room, the master bedroom, by a bathroom and a study. On some weekends I would go alone to visit my father in the city and my sister would stay and some-times grow frightened or lonely in her part of the house. And once, in the period when my grandfather, then in his sixties, was living with us, she became alarmed at a noise she had heard in the night; or perhaps she just became lonely, and she went out of her room and down the hall, calling for my mother, or my stepfather, or my grandfather, but the house was dark, and no one answered.

And, as she went farther down the hall, toward the living room, she heard voices, and she turned the corner, and saw a light coming from under the closed door in the master bedroom, and heard my stepfather crying, and the sound of my mother weeping. So my sister went up to the door, and she heard my stepfather talking to my grandfather and saying, "Jack. Say the words. just say the words . . " And my grandfather in his Eastern European accent, saying with obvious pain and difficulty, "No. No. I can't. Why are you making me do this? Why?" And the sound of my mother crying convulsively.

My sister opened the door, and she saw my grandfather sitting on the bed, and my stepfather standing by the closet and gesturing. On the floor of the closet she saw my mother, curled in a fetal position, moaning and crying and hugging herself. My stepfather was saying, "Say the words. Just say the words." And my grandfather was breathing fast and repeating, "I can't. She knows how I feel about her. I can't." And my stepfather said, "Say the words, Jack. Please. Just say you love her." At which my mother would moan louder. And my grandfather said, "I can't."

My sister pushed the door open farther and said - I don't know what she said, but she asked, I'm sure, for some reassurance, or some explanation, and my stepfather turned around and saw her and picked up a hairbrush from a dresser that he passed as he walked toward her, and he hit her in the face and slammed the door on her. And she continued to hear "Jack, say the words."

She told me that on weekends when I was gone my stepfather ended every Sunday evening by hitting or beating her for some reason or other. He would come home from depositing his own kids back at their mother's house after their weekend visitation, and would settle down tired and angry, and, as a regular matter on those evenings, would find out some intolerable behavior on my sister's part and slap or hit or beat her.

Years later, at my mother's funeral, my sister spoke to our aunt, my mother's sister, who gave a footnote to this behavior. She said when they were young, my mother and my aunt, they and their parents lived in a small flat on the West Side. My grandfather was a salesman on the road from dawn on Monday until Friday night. Their family had a fiction, and that fiction, that article of faith, was that my mother was a naughty child. And each Friday, when he came home, his first question as he climbed the stairs was, "What has she done this week . . . ?" At which my grand-mother would tell him the terrible things that my mother had done, after which she, my mother, was beaten.

This was general knowledge in my family. The footnote concerned my grandfather's behavior later in the night. My aunt had a room of her own, and it adjoined her parents' room. And she related that each Friday, when the house had gone to bed, she, through the thin wall, heard my grandfather pleading for sex. "Cookie, please." And my grandmother responding, "No, Jack." "Cookie, please." "No, Jack." "Cookie, please."

And once, my grandfather came home and asked, "What has she done this week?" and I do not know, but I imagine that the response was not completed, and perhaps hardly begun; in any case, he reached and grabbed my mother by the back of the neck and hurled her down the stairs.

And once, in our house in the suburbs there had been an outburst by my stepfather directed at my sister. And she had, somehow, prevailed. It was, I think, that he had the facts of the case wrong, and had accused her of the commission of something for which she had demonstrably had no opportunity, and she pointed this out to him with what I can imagine, given the circumstances, was an understandable, and, given my prejudice, a commendable degree of freedom. Thinking the incident closed she went back to her room to study, and, a few moments later, saw him throw open her door, bat the book out of her hands, and pick her up and throw her against the far wall, where she struck the back of her neck on the shelf.

She was told, the next morning, that her pain, real or pretended, held no weight, and that she would have to go to school. She protested that she could not walk, or, if at all, only with the greatest of difficulty and in great pain; but she was dressed and did walk to school, where she fainted, and was brought home. For years she suffered various headaches; an X ray taken twenty years later for an unrelated problem revealed that when he threw her against the shelf he had cracked her vertebrae.

When we left the house we left in good spirits. When we went out to dinner, it was an adventure, which was strange to me, looking back, because many of these dinners ended with my sister or myself being banished, sullen or in tears, from the restaurant, and told to wait in the car, as we were in disgrace.

These were the excursions that had ended, due to her or my intolerable arrogance, as it was explained to us.

The happy trips were celebrated and capped with a joke. Here is the joke: My stepfather, my mother, my sister, and I would exit the restaurant, my stepfather and mother would walk to the car, telling us that they would pick us up. We children would stand by the restaurant entrance. They would drive up in the car, open the passenger door, and wait until my sister and I had started to get in. They would then drive away.

They would drive ten or fifteen feet, and open the door again, and we would walk up again, and they would drive away again. They sometimes would drive around the block. But they would always come back, and by that time the four of us would be laughing in camaraderie and appreciation of what, I believe, was our only family joke.

We were raking the lawn, my sister and I. I was raking, and she was stuffing the leaves into a bag. I loathed the job, and my muscles and my mind rebelled, and I was viciously angry, and my sister said something, and I turned and threw the rake at her and hit her in the face.

The rake was split bamboo and metal, and a piece of metal caught her lip and cut her badly.

We were both terrified, and I was sick with guilt, and we ran into the house, my sister holding her hand to her mouth, and her mouth and her hand and the front of her dress covered in blood.

We ran into the kitchen where my mother was cooking dinner, and my mother asked what happened.

Neither of us, myself out of guilt, of course, and my sister out of a desire to avert the terrible punishment she knew I would receive, neither of us would say what occurred.

My mother pressed us, and neither of us would answer. She said that until one or the other answered, we would not go to the hospital; and so the family sat down to dinner where my sister clutched a napkin to her face and the blood soaked the napkin and ran down onto her food, which she had to eat; and I also ate my food and we cleared the table and went to the hospital.

I remember the walks home from school in the frigid winter, along the cornfield that was, for all its proximity to the city, part of the prairie. The winters were viciously cold. From the remove of years, I can see how the area might and may have been beautiful. One could have walked in the stubble of the cornfields, or hunted birds, or enjoyed any of a number of pleasures naturally occurring.
```

---

## IC-2488: Red Diaper Baby

- Title: Red Diaper Baby
- Author (byline): Josh Kornbluth
- Work: Not specified
- Publisher: Mercury House Publishing
- Publication date as stated: Oct 1996
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: FATHER, JOSH, MOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1842
- Already set (do not supply): none

### Source block (context only)

```text
Author: Josh Kornbluth
ISBN: 978-1562790875
Publisher: Mercury House Publishing
Date (Month/Year): Oct 1996
```

### Introduction (context only: never use it for content warnings)

```text
It's a morning in the mid-1960s, and 6-year-old Josh Kornbluth is woken by his father, Paul, in the usual manner -- with Paul bursting naked into Josh's room and singing "The Internationale." So begins this raucous tale of a young American communist's coming-of-age The true story of a boy whose dream is to lead a revolution. Quite a challenge, especially for such a shy, chubby kid.

Red Diaper Baby by Josh Kornbluth
```

### Performance text (classify this)

```text
FATHER: (Singing)* Arise, you prisoners of starvation! / Arise, you wretched of the earth! For justice thunders condemnation. / A better world's in birth.

JOSH: My father, Paul Kornbluth, was a Communist. He believed there was going to be a violent Communist revolution in this country -- and that I was going to lead it. Just so you can get a sense of the pressure.

JOSH: Anything my father told me I'd believe, because my father was such a physically magnificent man: he was big, and he had this great big potbelly -- not a wiggly-jiggly, Social Democratic potbelly; a firm, Communist potbelly. You bopped it, it would bop you back. It was strong.

I would have loved to have slept in late on the weekends, but I couldn't because my father wouldn't let me. He'd come bursting into my room and running up to my bed, looming over me he'd sing: Arise, ye prisoner of starvation! Arise, ye wretched of the earth! I didn't know that was the international Communist anthem. I thought it was my own personal wake-up song. I knew from an early age that one day I must grow up and lead the Revolution!

My father had his own language -- not only his own English, but his own Yiddish. I used to think it was real Yiddish, but my mom would say

MOTHER: What your father speaks is not Yiddish. I went to Yiddish school and what your father speaks is not Yiddish.

JOSH: In my father's Yiddish, there was a term ouska -- a prefix, meaning "a lot of," "very"

FATHER: I am ouska-cold, my son!"

JOSH: (to father) Of course you're ouska-cold, Dad; the window is ouska-open."

Dad and I would sit around the kitchen table having hard-boiled eggs (my father, not a soft-boiled kind of guy). And Dad would regale me with his stories of organizing with the Henry Wallace campaign. (That's **Henry Wallace. Henry. Okay?) And he'd drill me in the catechisms of our faith of Communism. Like how society has been driven from one stage to the next, driven inexorably by the forces of dialectical materialism, until ...

According to Marx and Engels -- and my dad -- the first human society was Primitive Communalism: everyone's just kind of dancing around, like at a Grateful Dead concert.

The next stage after Primitive Communalism was Slavery -- which must have been a bummer of a transition.

Then from Slavery to Feudalism, and from
Feudalism ... Well, we've learned from history that
it's very important after Feudalism to stop in
Capitalism before moving on to Socialism. Very
important to stop in Capitalism. Because that's
where you get your appliances.

So you stop in Capitalism, you get your stuff, and then you move on to Socialism, and finally to Communism -- and you're back at the concert.

All along the walls of our kitchen, bathroom, living-room and dining-room area were posters of our heroes, our gods: W. E. B. Du Bois, Malcolm X, Dr. King, Ho Chi Minh, Bertolt Brecht, Emma Goldman . . . And at the end of all these posters: my height chart.

And we'd go outside for our walks. When we went
outside, my father -- in his one true concession to
society -- would put on clothing. This was back in '65,
when I was about six years old; and being
Communists, we had songs associated with every
activity. Me and Dad didn't just have generic walking
songs; we had specific going-up-the-hill songs,
specific going-down-the-hill songs.

We learned our biggest going-up-the-hill song off an album by Paul Robeson, a great Jewish folksinger. It was a record my dad had borrowed from the public library, and then -- as a revolutionary act refused to return. (And my mom was a librarian!)

Going downhill, [we] would sing: ***As I go down in the valley [to the river] to pray / Studying about that good old way / And who shall wear the robe and crown / Good Lord, show me the way!

My father couldn't hear me. He didn't connect it with the fact that he was singing so ouska-loud he was drowning me out. So periodically he'd turn to me on the sidewalk and go

FATHER: Sing louder, my son-I can't hear you! (singing loudly) Come on, fathers, let's go down! / Down in the valley to pra-a-a-ay ... to pray-yee! (declaring emphatically) And a child shall lead them!

JOSH: A nice, cheerful walking song-though confusing lyrically, to an urban child. (beat) We had to live ouska-cheaply. Because my father . . . Well, he was a schoolteacher -- a very good schoolteacher with great passion, but at the same time he would be developing this anger towards his bosses: the principal, the assistant principals, the school board. And this anger at his bosses would build and build, until finally Dad couldn't take it anymore. This would take about two weeks. And at the end of those two weeks, Dad would go storming into the principal's office and yell

FATHER: F*** you!

JOSH: Often the guy would never have seen my dad before. And he'd say, "You're fired! ... If you work for me, you're fired!" And then Dad would get another job, and he'd be teaching his new students with great passion but developing this anger towards his new bosses. And at the end of two weeks he would storm into his new principal's office and go

FATHER: F*** you!

JOSH: And the new principal would go; "You're fired!" This went on for years and years; my father never saw the pattern. He never saw the cause-and-effect between "F*** you!" and "You're fired!" So we had to live ouska-cheaply. Which was fine with me: I loved ouska-cheap adventures, like the Museum of Natural History -- where at the time the admission was whatever you would care to donate. They've since changed that policy; I think because of my dad.

FATHER: Pay them a penny and not a penny more!

JOSH: We'd go running to the dinosaur exhibit, where Dad would give me a tour. I don't think he was an expert in the field, but . . .

FATHER: The Tyrannosaurus rex, my son-one of the largest . . . reptilian(s) ever to walk the earth!

JOSH: And other little kids would break away from their field trips and join us. [It] was a lot more interesting the way my dad described it. (beat) And then, after a weekend of this kind of ouska-fun, my dad -- as the courts had mandated -- had to return me to . . . my mom -- Bernice "Bunny" Selden: also Jewish, also a New Yorker, also a vollege grad, also a Communist -- but so different from my father in temperament. If my father was an out-there, ouska-Communist, my mom was ... inska.

And she had her own inska-wake-up song for me, too. And like I thought Dad had written the "Internationale" for me, I thought my mom had written her wake-up song for me; I only found out years later that Irving Berlin wrote it.

She'd go into the bathroom in her nightgown and come back out with her hair in a bun. And she'd stand in my open doorway -- which was easy for her to do, because for some reason she would not let me have a door. She'd tiptoe to my bed and lean down and sing:

MOTHER: (singing) ****Oh, how I hate to get up in the morning / Oh, how I'd love to stay in bed For the hardest blow of all / Is to hear that bugler

call: "You gotta get up, you gotta get up; You gotta get up in the morning. You gotta get up, you gotta get up, You gotta get up in the morning."

JOSH: A pretty nice wake-up song. Unless you know the second verse, which gets to a surreal level of violence . . .

MOTHER: (singing) Someday I'm gonna murder the bugler / Someday you're gonna find him dead / I'll amputate his reveille / And stamp upon it heavily/ And spend the rest of my life in bed!

JOSH: I thought she could snap at any moment. So I'd get out of bed; I didn't want my reveille amputated! (beat) But I still didn't have that get-up-and-go that the "Internationale" gives a kid. She'd guid lead me into the living room and sit me down on the couch. She had this little motherly trick she'd play to get me going in the morning: she'd serve me a tall cup of double-espresso with whipped cream and a maraschino cherry on top.

And I'd sit there sipping my double-espresso on the couch, beneath the half-dozen ceramic disks that she bought in Mexico, where she went to divorce my dad -- which, by the way, was when I was six months old.

They were married for nine years, then I was born. Then, when I was six months old, they divorced. From time to time I'd wonder why. (beat) A few months ago, I was reading this article about a guy named Saul Newton, a crazed psychoanalyst who ran this cult called the Sullivanians. They had a co-op on the Upper West Side. (thoughtfully) Saul Newton . . . Saul Newton -- and suddenly it hit me: Wait a second! My dad's therapist was named Saul! So I called up my mom and said, "Mom, I'm reading about this Saul Newton guy," and she said, "Yeah, that was your father's therapist." Evidently Dad was an early patient of Saul's -- sort of a test case.

After I was born, Saul convinced my dad that now that he had a family, and families were evil, his family must be broken up. So, Dad left me and my mom and got an apartment on the Lower East Side. According to my mom, after a couple of weeks Dad started to miss us. He came running to try to reconcile with us. But Mom escaped with me down to Mexico, where she got the divorce, bought big, floppy hats, danced around with strangers, and got the half-dozen or so ceramic disks -- each one depicts a woman escaping from slavery.

So I'd sit there under the disks on the couch, sipping my double espresso, as my mom turned on the old radio. The morning disc jockey was Julius Lester -- he of the ouska-deep voice. Supposedly, Julius's program was a classical music show. But Julius would play about five minutes of an oboe concerto, and then speak for hours about his various ex-wives and their peccadilloes.

I'd listen to Julius and sip my double-espresso and then go running off to school-jazzed!

I was so excited my first day of kindergarten. After spending the first five years of my life exclusively in the company of my parents and their friends; for the first time, I was going to get to mingle with the masses. Boy, was I disappointed! That first day, I walked into my kindergarten classroom and saw all these little kids running around screaming, pulling hair, bopping each other, crying. I thought, How will I ever organize these people? (then he gets an idea) Remember . . . my father was a Communist. He believed I was going to lead a violent Communist revolution – so . . . (singing as a 5-year-old) * Arise, you prisoners of starvation! / Arise, you wretched of the earth! / For justice thunders condemnation. / A better world's in birth.
```

---

## IC-2489: Redeployment

- Title: Redeployment
- Author (byline): Phil Klay
- Work: Redeployment, Pgs 1-16
- Publisher: Penguin Books
- Publication date as stated: Feb 2015 (Reprint)
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SGT PRICE
- Teaser before the introduction: Yes
- Spoken words (computed): 1874
- Already set (do not supply): none

### Source block (context only)

```text
Author: Phil Klay
Book: Redeployment, Pgs 1-16
ISBN: 978-0143126829
Publisher: Penguin Books
Date (Month/Year): Feb 2015 (Reprint)
```

### Introduction (context only: never use it for content warnings)

```text
Military service is difficult, demanding, and dangerous. But leaving the military is one of the most challenging life changes anyone can experience. According to the journal Psychiatry Research, veterans within their first year of transitioning into civilian life have a suicide rate more than double that of active service members. Why is the transition so difficult?

Let’s begin with military training. Physical, mental and moral toughness are prerequisites. In basic training young people are transformed from aimless individuals into soldiers. Soldiers whose primary mission has always been to kill and destroy the enemy. They are sent to parts of the globe most people will never see, required to kill or be killed, immersed in cultures with far different values and desensitized to violence.

We cannot begin to comprehend living every day on a threat level scale.

Redeployment by Phil Klay
```

### Performance text (classify this)

```text
SGT PRICE: (Pg 1-16) We shot dogs. Not by accident. We did it on purpose and we called it 'Operation Scooby'. I'm a dog person, so I thought about that a lot. First time was instinct. There's a skinny brown dog lapping up blood the same way he'd lap up water from a bowl. It wasn't American blood, but still. And that's the last straw, I guess, and then it's open season on dogs.

At the time you don't think about it. You're thinking about who's in that house, what's he armed with, how's he gonna kill you. The thinking comes later when they give you the time. See, it's not a straight shot back, from war to the Jacksonville mall. They took us to Kuwait and put us on a commercial airliner to go home.

So, there you are. You've been in a war zone and then you're sitting in a plush chair looking up at a little nozzle shooting air conditioning. You've got a rifle between your knees, but they take away your bayonets because you aren't allowed to have knives on an airplane. Even though you've showered, you all look grimy and lean. Everybody's hollow-eyed. And you sit there, and close your eyes, and think.

SGT PRICE: The problem is your thoughts don't come out in any kind of straight order. You don't think, oh, I did A, then B, then C, then D. You try to think about home, then you're in the torture house. You see the body parts in the locker and the guy in the cage. He squawked like a chicken. His head was shrunk down to a coconut. It takes you a while to remember Doc saying they'd shot mercury into his skull, and then it still doesn't make any sense.

You see the little girl, the photographs Curtis found in a desk. First had a beautiful Iraqi kid, maybe seven or eight years old, in bare feet and a pretty white dress like it's First Communion. Next, she's in a red dress, high heels, heavy make-up. Next photo, same dress but her face is smudged and she's holding a gun to her head.

I tried to think of other things, like my wife Cheryl. But here's the thing. I'm thinking a lot, and I mean, a lot, about those dogs. And I'm thinking about my dog. Vicar. About the shelter we'd got him from; Cheryl said we had to get an older dog because nobody takes older dogs. So, there it was. Vicar and Operation Scooby, all the way home. Maybe, I don't know, you're prepared to kill people. You practice on man-shaped targets so you're ready. And it's not easy to kill people, either. On the flight, I thought about that too.

When we touched down in Cherry Point, we all got in line. I got to the window and handed in my rifle; it brought me up short. That was the first time I'd been separated from it in months. I didn't know where to rest my hands. First, I put them in my pockets, then I took them out and crossed my arms, and then I just let them hang, useless, at my sides.

After all the rifles were turned in, we marched down A Street. When we got to the edge of the first barracks, people started cheering. Off to the side there were picnic tables and a Marine grilling hot dogs. And there was a bouncy castle. A bouncy castle! I saw some TV cameras. There were a lot of US flags. Up front, right in the middle, a banner that read: WELCOME BACK HEROES OF BRAVO COMPANY. All around us were families and big smiles and worn-out Marines.

And there was Cheryl. I walked up to her and kissed her. I figured that was what I was supposed to do. But it'd been too long, and we were both too nervous and it felt like just lip on lip pushed together, I don't know.

Cheryl said, 'How are you?' which meant: How was it?

Are you crazy now?

I said, 'Good. I'm fine.' And then it was quiet again. One step at a time. You can get through anything, one step at a time.

When we got home, she opened the door for me. Vicar wasn't at the door to greet me. I stepped in and scanned around and there he was on the couch. When he saw me, he got up slow. His fur was greyer than before, and there were weird clumps on his legs, little tumors that Labs get. He stepped down off the couch real careful, like he was hurting.

And that was my homecoming. It was fine, I guess. Getting back feels like your first breath after nearly drowning. Even if it hurts, it's good.

I can't complain. Cheryl handled it well. I saw Lance Corporal Curtis's wife back in Jacksonville. She spent all his combat pay before he got back, and she was five months pregnant, which, for a Marine coming back from a seven-month deployment, is not pregnant enough.

Corporal Weissert's wife wasn't there at all when we got back. He laughed, said she probably got the time wrong, and O'Leary gave him a ride to his house. They get there and it's empty. Not just of people, of everything: furniture, wall hangings, everything.

So, I sat on the couch with Vicar, watching the baseball games Cheryl'd taped for me. Sometimes Cheryl and I talked about her seven months, about the wives left behind, about her family, her job, her boss. Sometimes she'd ask little questions. Sometimes I'd answer. Vicar'd sleep with his head in my lap. It looked like it hurt him to do everything, wag his tail, eat his chow. Walk. Sit. I wanted Vicar around, but I couldn't bear to look at him. And glad as I was to be in the States, and even though I hated the past seven months and the only thing that kept me going was the Marines I served with and the thought of coming home, I started feeling like I wanted to go back. Because f*** this.

So, here's an experience. Your wife takes you shopping. Last time you walked down a city street, your Marine on point went down the side of the road, checking ahead and scanning the roofs. The Marine behind him checks the windows on the top levels of the buildings, the Marine behind him gets the windows a little lower, and so on until your guys have the street level covered. In a city there's a million places they can kill you.

[Here], you don't have a squad, you don't have a battle buddy, you don't even have a weapon. You're safe, so your alertness should be at white, but it's not. Instead, your wife gives you some clothes to try on and you walk into the tiny dressing room. You close the door, and you don't want to open it again.

Outside, there're people walking around by the windows like it's no big deal. People who have no idea where Fallujah is, where three members of your platoon died. People who've spent their whole lives at white. They'll never get even close to orange. You can't, until the first time you're in a firefight, or the first time an IED goes off that you missed, and you realize that everybody's life, everybody's life, depends on you not *messing* up. You depend on them.

Some guys go straight to red. They stay like that for a while and then they crash, go down past white, down to whatever is lower than 'I don't care if I die'. Most everybody else stays orange, all the time.

Here's what orange is. You don't see or hear like you used to. Your brain chemistry changes. You take in every piece of the environment, everything. I could spot a dime in the street twenty yards away. It's hard to even remember exactly what that felt like. I think you take in too much information to store so you just forget, free up brain space to take in everything about the next moment that might keep you alive. And then you forget that moment too and focus on the next. And the next. And the next. For seven months.

And then you go shopping in Wilmington, unarmed, and you think you can get back down to white? It'll be a long time before you get down to white.

And when we got back, we saw Vicar there on the couch, trying to stand on shaky legs. And I said, 'Damn it, Cheryl. It's time.'

I sat down on the couch and scratched Vicar behind the ears and I came up with a plan. Not a good plan, but a plan. Sometimes that's enough. There's a dirt road near where I live and a stream off the road where the light filters in around sunset. It's pretty. I used to go running there sometimes. I figured it'd be a good spot for it. We got there right at sunset. I parked just off the road, got out, pulled my rifle out of the trunk, slung it over my shoulders, and moved to the passenger side. I opened the door and lifted Vicar up in my arms and carried him down to the stream. He was heavy and warm, and he licked my face as I carried him, slow lazy licks from a dog that's been happy all his life. When I put him down and stepped back, he looked up at me. He wagged his tail. And I froze. This feeling, like, something in me is going to break if I do this. And I thought, I have to do this. I didn't have a shotgun, I had an AR-15. And I'd been trained to do it right.

There had to be three shots. It's not just pull the trigger and you're done. Hammer pair to the body. A final well-aimed shot to the head. The first two have to be fired quick, that's important.

If I were to shoot you on either side of your heart, one shot. . . and then another, you'd have two punctured lungs, two sucking chest wounds. But you'll still be alive long enough to feel your lungs fill up with blood.

If I shoot you there with the shots coming fast, it's no problem. The ripples tear up your heart and lungs and you don't do the death rattle, you just die. There's shock, but no pain.

I pulled the trigger, felt the recoil, and focused on the sights, not on Vicar, three times. Two bullets tore through his chest, one through his skull, and the bullets came fast, too fast to feel. That's how it should be done, each shot coming quick after the last so you can't even try to recover, which is when it hurts. I stayed there staring at the sights for a while. Vicar a blur of grey and black . . . [and] down past white, down to whatever is lower than 'I don't care if I die'.

The light was dimming. I couldn't remember what I was going to do with the body.
```

---

## IC-2490: Rest Area

- Title: Rest Area
- Author (byline): Clay McLeod Chapman
- Work: Rest Area: Stories, Pgs 1-8
- Publisher: Hyperion
- Publication date as stated: Feb 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: GRACE’S DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 2051
- Already set (do not supply): none

### Source block (context only)

```text
Author: Clay McLeod Chapman
Book: Rest Area: Stories, Pgs 1-8
ISBN: 978-0786867370
Publisher: Hyperion
Date (Month/Year): Feb 2002
```

### Introduction (context only: never use it for content warnings)

```text
When you’re traveling on a long road trip, a rest stop can provide a much-needed break and an opportunity to
```

### Performance text (classify this)

```text
GRACE’S DAD: (talking to a family through the window of a car) (Pg 1-8) Carolina plates. You guys have come far. Where you heading? Out Midwest? Lord, that’s a long haul. And with the whole family, boy. Who’s the little tinker in the backseat? Hi there. She doesn’t mind being buckled up all day? Good for her. My daughter and I did our own bit of venturing cross-country this summer, just the two of us. We ambled along the back roads for weeks.

Could you tell me if you’ve seen her? Here. (holds out a flyer) Here’s a photograph of her. Well, a photocopy. You can’t make out her features very well. But if you look here, right above the smudge, you can still spot her smile. That’s Grace’s smile.

I’m pasting them up all along here. On the soda machines. There’s a whole stack with the tourist pamphlets. Just in case someone’s seen her. Can’t be too sure, now.

You didn’t, did you? Did you see a girl on the road? Red hair, Cream shorts. No sign of her?

recharge your batteries; especially if you are traveling alone with children. Unfortunately, because they are often in isolated locations where help is many miles away, rest areas are not always safe.

The last thing anyone wants to think about is a child being abducted, but it’s a harsh reality. *According to the Child Crime Prevention and Safety Center, “each day 33 children are abducted by someone who is not a family member.”

What should you do if your child is missing? Immediately call local law enforcement. But that’s not what happens in Rest Area by Clay McLeod Chapman and we begin to wonder why.

GRACE’S DAD: (directly to audience members as if they are travelers) We drove through here a few months ago, about halfway into our trip. The A/C was on its own time, leaving us with the windows down for most of the ride. The heat wasn’t the problem, really. I could’ve dealt with that. It’s the puddle of sweat forming at the stem of your neck that drowns your temper. The wet itch you get all along your scalp. Let your nerves juggle that, while your girl is in the seat next to you. Trust me, it doesn’t make for a calm, cool ride. Grace had found a couple candy bars in the glove compartment, which had been sitting in there for God knows how long. At ninety what-not degrees, they melted into this ropy tar she didn’t mind lapping off the wrapper. It found its way onto every part of her face except her mouth. Her hands left chocolate on the windows. She got caramel on the seat belt that still hasn’t come out.

The rest stop was five miles away. We pulled into the third slot, down at the far end there. It was mid-afternoon, so this place was full of enough people to not see any particular person. I don’t think I made eye contact with one single person.

My shorts had crawled up my waist, so the upholstery was clinging to my thighs. Grace is giggling at my hairy legs – these chunks of half-melted chocolate dangling from her teeth. She didn’t understand what all the hours in the car had done to my patience, mistaking my irritation for some game. I wasn’t talking, so she flipped on the radio, turning the volume up to some harsh static – only to smear chocolate on the dial.

That was it. My boiling point had hit. I told Grace to get out of the car. Slamming doors, deep sighs – the entire routine. Pointing to the curb, I told her to wait while I ran to the men’s room.

I come back with a whole roll of toilet paper, finding Grace on the curb, crying. She’s doing a better job at washing off her cheeks than I could’ve, the tears tasing more sweet than salty. We must have moped around for a few minutes, until she slaps a thick hand print of candy right across my cheek. I reach my tongue around to taste it, licking the bottom side of her palm clear off. I keep going back for more of her until there’s none left. She’s giggling again, so I start swiping the chocolate off her cheeks, too – until she’s tickled back into having a fun time.

Good, I think.

A few sniffles later and she asked to wash up in the ladies’ room.

She took the keys with her. Fetched them right out of my hand. They didn’t fit in hers, poking out between her knuckles. It was as if her fingers had multiplied all of a sudden. I remember Grace walking down the sidewalk here – this stop-and-run between all the other families. She’d gallop along until someone walked in front of her, whinnying in place while they passed by, and then pick up her stride again once the path was clear. The farther she went, the more those keys sounded like spurs pushing her along. I watched her slip off into the crowd, and I remember wanting to keep looking at her. I’d stash the memory of this place I the trunk, with all our luggage. She would come back to me, and we would take that highway. Take it to wherever it led us.

I found more handprints wrapped around the seat. There were chocolate fingers pointing in all directions, navigating the toilet paper into deep crevices. Wherever I’d bury it, my hand would come up gooey, gummy. The candy wouldn’t let go of the car, stretching out in long strands of caramel – only to lash back onto the upholstery. Even the sweets didn’t want to let her go.

Five minutes passed and I fumbled for my watch. There was no sign of her. No smell of her. No taste anymore.

Women kept walking in and out from the bathroom, while I waited outside the door. That picture nailed to the front, that symbol or whatever you’d call it. She’s a taunter, that’s for sure. A stick figure in a skirt marking the ladies’ room. She could have been a man wearing a dress for all I knew. But I’m watching her slip away and slide right back at me while all these women kept coming in or coming out. But none of them were her. I asked some lady if she’d see if Grace was still in there, but she came out shaking her head. There were dirty looks from everyone inside, but I had to walk in. I called out Grace’s name at every stall. I kneeled down in hopes of finding her legs hanging in front of me. I just wanted to see familiar feet. Cream short down at her ankles. That’s all.

No one had seen her at the vending machines. All the picnic tables had other families sitting at them. I’d spot a girl on her own and I’d think it was Grace. I’d run to her. The closer I got, the more the shorts wouldn’t match, or her hair would turn a color off right in front of me. She wasn’t waiting at the car. The phone booths were full of teenagers necking with each other. The walls had everyone else’s name scrawled over them, but not Grace’s. The parked cars kept switching with fresh ones. But I wouldn’t let anyone drive off until I looked through their windows. Until I knew that she wasn’t inside. I kept searching. Kept asking. Kept calling out, “Grace! Daddy wants to leave now!”

But that was months ago. Now I can’t remember which finger of mine touched her last. What part of me she kissed before running off. All I see now are people on their way somewhere else, tangling up into each other long enough to relive themselves. And then they leave. While I’m still here. You’d think people could remember seeing a face like hers. A head of hair as red as that, she could light her way through a crowd.

That’s her, that’s what she looks like. Sprinkle her with some freckles and she’s good enough to eat. They’re covering her cheeks, leaving her looking like a chocolate chip cookie. See that? She’s smiling at the idea. This is the best photocopy of her, I think. All of these smudges could be sweet, if I rubbed them right. Because I’m sure she’s still got a bit of candy on her face, somewhere. Think of the black parts of the picture as chocolate. And then you’ve got my girl.

You’re coming through here at a pretty good time, now. This place emptied out about an hour or so ago. The weekend traffic thinned itself down to the serious drivers, like yourself. IF you want soda, the vending machines are that way. I think I finished off most of the snacks yesterday, so I don’t know how good your selection will be. The man who refills them doesn’t com back until Thursday, so . . . sorry. My meals don’t stray too far from potato chips and pop, but I’m not complaining. With the few handprints of Grace’s still stuck on the car, you’d think I could scrape off a meal for myself. But I’d just end up smudging what’s left of her over the upholstery. I want to keep her there for as long as I can. Let her fingers point me in the right direction.

I’m sure she thinks this is all some sort of game. That’s what I get for starting our vacation off by feasting on the states. You can’t help but choke once you forget to chew. And now I’ve got a bone in my throat that won’t slip up the highway or down it.

I know she’s still here. Caught right above the Adam’s apple, you could say. I’ve become so used to this place, even the people are looking alike now. I’m sure the same cars have driven through here two times over, at least. And I can’t even find my keys. I’ve spent days looking for them, peering up underneath the stalls when no one’s around. Getting real familiar with the plumbing. I feel like I have more in common with the drainage here than anything else. Their pipes are probably as clogged as mine are. Eating from these vending machines has left my insides feeling stiff. The fifty-cent foods here have become the staple in my diet, while the toilet feeds off of whatever I drop for it.

So there are a hundred and one different places she could be. Who’s to say I’ve looked through them all? You have the woods, the toilets, the tourist info. All these cars.

Our car. It’s been sitting there in the same parking spot for so long now, she has to know where it is. I’ve left a trail of candy wrappers for Grace, just in case. She couldn’t miss it if she closed her eyes. It’s been there for so long, it’s staring to smell. I didn’t think cars could rot, but ours is somehow. I haven’t been able to get into the trunk, where all of our luggage is, so I’m thinking she might’ve brought along some pet and just not have told me.

It's these games. I can’t keep up with them. I feel like I’m in the middle of one now, but I’ll be damned if I’m not the last to know.

We’re playing out a fairy tale here. I can’t get to my shaving kit, so I’ve become some rest-area troll for her to hide from. I catch a glance of myself in the bathroom, or find my reflection in the rearview mirror. It’s hard now to recognize what’s staring back. It’s hairy all over and just as scared as I am. It has an ordor that follows me around, strongest in the places that I want to sleep. It’s taken over the car with such a stink – letting me know that it’s been there and will stay there for as long as it’s parked in this place. And this is the part I have to play, while Grace is the princess running away, hiding from me. She has the keys, so she makes the rules. I can’t leave until I find her. And I know she’s close. God, sometimes I can almost smell her underneath all of this, she feels so close.
```

---

## IC-2491: Rescui-Annie

- Title: Rescui-Annie
- Author (byline): Paul Feig
- Work: Kick Me: Adventures in Adolescence
- Publisher: Three Rivers Press
- Publication date as stated: Sept 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2022
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Feig
Book: Kick Me: Adventures in Adolescence
ISBN: 978-0609809433
Publisher: Three Rivers Press
Date (Month/Year): Sept 2002
```

### Introduction (context only: never use it for content warnings)

```text
Whether the latest Ebola or Zika virus news has triggered your inner germaphobe, or you’re just a year-round clean freak like me, you’ll be able to identify with this childhood memory of Paul Feig. Middle school . . . . those in between years are rough, but if you are a germaphobe, then it’s even worse, especially if gym class includes CPR training with Sergeant Korn, Coach Wendell and . . . Rescui-Annie by Paul Feig
```

### Performance text (classify this)

```text
When I was a kid, I was germ conscious. Really germ conscious. You see, much of childhood is set up as one big germ- and spit-spreading activity. And it seemed as if all of my grade-school peers were more than willing to put their mouths on whatever it was that I or anyone else happened to be consuming at any given moment during the day. Whenever I had a bottle of pop, at any point from age four to fourteen, it was guaranteed that within seconds of opening it, some kid I knew would appear behind me and utter these dreaded words: "Hey, can I have a drink?" Every time. And then I was stuck. Because if I dared to say no, it was sure to provoke a thoughtful and understanding response of "C'mon, ya baby. I'm not gonna drink it all."

"Yeah, but you're gonna get your mouth all over it." Or at least, that's what I wanted to say. But instead, in my true non-confrontational fashion, I'd always relent: "Uh ... okay. Here." I mean, what other option did I have? The circumstances were always the same. It would be a warm afternoon. I'd be walking home from grade school, tired and worn out from a full day of crushes and failures and overreactions. As I walked, I'd twist off the top. The bottle would give me a friendly hiss that seemed to say, "Oh, friend, are you going to enjoy me." I'd take a deep breath, releasing all the tensions of the day, raise the bottle to my lips, tilt my head back and take a drink, enjoying life to its fullest. The world seemed to melt away. And life for that one moment was good. That is, until the dream would be shattered when Norman would suddenly walk out of the bushes and want to backwash into my bottle.

So, I'd reluctantly give him my Squirt and he'd put his mouth on it and take a sloppy swig and I'd feel defiled as I'd watch him gulp down my once pleasure-producing soft drink. My thoughts would be torn between hoping he choked on the pop and figur-ing out how I could possibly salvage what was left in the bottle. Maybe I could pour out the top inch of spit-contaminated liquid, then thoroughly wipe down the mouth of the bottle with my shirttail to remove the memory of his mouth. . . . when suddenly the nightmare would worsen. Another kid would invariably walk up. "Hey, Norman, can I have a drink?"

"It's okay with me, but it's Paul's pop. Ask him."

What was I gonna say? "No, I don't mind Norman's saliva but yours is a no-go." Why did all these kids have to drink out of the same bottle anyway? So Norman's friend would grab the bottle and take a drink and get his stupid mouth all over it and then a gang of Cub Scouts who were friends of the kid currently drinking would show up and take their turns and after an eternity I'd get the bottle back. The top would be coated with everything our grade school served for lunch that day and the few inches of liquid left at the bottom of the bottle would have about the same viscosity as old motor oil. I'd look at it and feel queasy and feel like crying but instead would try to sound casual and say, "You guys can have the rest. I'm not thirsty anymore."

"No way. I'm not drinking that. It's all backwash." Yeah, YOURS!

Well, it was a couple of years later, when I was in junior high school, that something happened during gym class that was to prove one of the most trauma-tic events of the spit-and-germ-avoiding segment of my childhood. Simply put, I met a girl. And that girl's name was . . . Resusci-Annie.

"Annie," as I've affectionately come to know her, wasn't a girl in the standard person-who's-actually-alive sense. No, Annie was a mannequin, a life-size doll with a rubber head, a mouth, a working windpipe, a set of lungs, and a body that was in possession of neither arms nor legs. Resusci-Annie, Queen of the Latex Torso Women, was something invented by paramedics and CPR instructors to be used for the teaching of the uninitiated in the fine art of mouth-to-mouth resuscitation. Annie also had one other thing going for her . . . She was terrifying.

The first traumatic thing about Annie was that she looked like a dead person. Her face was white and rubbery, her eyes were closed, her mouth was loosely open, exposing a disturbing set of rubber teeth, and she had a full mane of greasy, matted hair on top of her head. She hardly looked like someone anybody had a chance of saving. I'd throw a blanket over her face and start contacting next of kin if I saw her lying in the street. But as far as the emergency health care community was concerned, Annie had one purpose in this world and that was to be revived over and over again by anyone and everyone trying to master the very practical skills of lifesaving.

Mr. Wendell told us to gather in the center of the gym as we came out of the locker room. As we walked over, we saw ResusciAnnie lying on the floor. Just then, a very large policeman with a big red drinker's face and a handlebar mustache entered the gym and walked up to us.

"Hello, gentlemen. My name is Sergeant Korn. As part of an organized effort to teach people in our community about emergency medical procedures, I'm here today to demonstrate to you the proper way to administer the life-saving technique of mouth-to-mouth resuscitation."

If learning mouth-to-mouth meant it would keep us from having to play flag football or floor hockey or having to embark on yet another pointless attempt to do enough sit-ups to try to qualify for the much-unwanted President's Physical Fitness Award, then I was all for it.

"And now, with the help of my good friend Resusci-Annie here," Sergeant Korn said, gesturing grandly and then chuckling at his allegedly cute comment, "I'm going to show you the correct way to administer the 'Kiss of Life.'” And then, accompanied by an aria of grunts and groans, he awkwardly got down on his knees next to Annie. He stuck his fingers into her mouth, telling us that before we did anything, we were supposed to make sure that there were no "objects" blocking the victim's throat. Sergeant Korn pinched Annie's deathly white nose, put his hand under her neck to "open the throat," took a deep breath, put his mouth on top of Annie's, and blew. I immediately started to feel a bit nauseous. Maybe it was the image of an overweight cop on his hands and knees blowing into the mouth of an oversize doll and making his already uncomfortably red face even redder that made it feel more like I was watching a very low-quality porn film than a lifesaving demonstration.

Unsettling images of Sergeant Korn's private life with Mrs. Korn started to flood into my head. Fortunately, before I was able to ruminate on these mental pictures for too long, Sergeant Korn looked up and breathlessly said, "Resusci-Annie ... now has enough air ... to start breathing on her own again." And then he struggled to stand up again. Hearing him pant and try to catch his breath, I had a momentary flash that Sergeant Korn might keel over and that one of us would then be expected to put our newfound Kiss of Life knowledge to the test. Well, I knew one thing for sure: that "one of us" wouldn't be me.

Mr. Wendell stepped forward. "All right, you guys. Line up. You're all gonna take a turn."

Huh? Excuse me? I'm sorry, I must not have heard you correctly. It sounded like you said that we were all going to take a turn giving mouth-to-mouth resuscitation to that doll that Sergeant Korn had just had his grown man's mouth all over. That couldn't be right. I looked over at Mr. Wendell and saw him produce a bottle of rubbing alcohol and a rag. He dumped some alcohol onto the rag and wiped Sergeant Korn's spit off of Annie's mouth. My stom-ach dropped into my Keds. A wave of panic overtook me. My eyes zoomed in on Annie's mouth. White and cold and open and now dripping with an indeterminate mixture of Sergeant Korn's spit and alcohol. My head started to spin.

My mind raced. This couldn't be happening. But it was. My fellow classmates were starting to line up in front of Annie. There had to be some way out of this. It just wasn't possible that I was going to have to put my mouth on that thing. Especially after other guys in my class were about to do it, too. Something had to be done.

"Mr. Wendell, I think it's against my religion to do stuff like this."

"Feig, I don't care if you're the pope. You're doing this, so get in line."

There was no way around it. I was eventually going to have to give Annie the Kiss of Life. I was really starting to feel sick. And this was before I realized that with all the air going in and out of Annie's chest, there was a whole reservoir of lung germs inside my future Resusci-girlfriend just waiting to infect my body. I was stuck, doomed, and now the last in line. More and more spit was being deposited on Annie by the second. And now I noticed that the kid directly in front of me was Doug Blaychek. He was a nice enough guy if you met him in the hallway, but he had extremely large and droopy lips that constantly seemed to be soaked with saliva. Doug turned and gave me a big, wet smile. My life started to flash in front of my eyes.

It was Doug's turn. He kneeled down and bent over Annie. He took a loud, deep breath. I saw his back rise and fall several times as he tried to revive the lifeless rubber doll on the floor. As he moved away, I looked down. There she was. Annie. Her face was soaked. I didn't know what part of that "soaked" was spit and what part was alcohol, and I didn't care. Annie's face must now be a festering cesspool of disease and death.

"All right, Feig. You're up." . . . Maybe if I throw up all over it, I won't have to do it, I thought. . . . "C'mon, Feig. What is it with you? Get moving!" barked Mr. Wendell. My mind reeled. I had to do something and I had to do it immediately. But what? Think fast, I told myself. Then it hit me. Faint.

I coughed violently and fell over. There was immediate commotion. I hadn't been sure if they would buy my sudden and convenient fainting spell or not, but I guess that the perception of me as someone who was prissy enough to faint at the thought of giving mouth-to-mouth resuscitation was enough to convince them.

"I'LL SAVE HIM!"

It was Doug! New panic set in as I heard him stomp toward me to deliver his newly learned Kiss of Life. I was nanoseconds away from blowing my cover by screaming and running away when Mr. Wendell saved me by quickly grabbing Doug by the arm. "No, Blaychek," said Mr. Wendell, "we don't know if he needs mouth-to-mouth."

"He coughed really loud before he fell down," said Norman.

Sergeant Korn stepped forward and looked me over. "You said he coughed?" he asked, sounding tense and official. "Then he must have choked. Everybody step back." And with that, Sergeant Korn stuck his fingers in my mouth, pinched my nose, and kissed me.

I was home sick for three days.
```

---

## IC-2492: The Rifle

- Title: The Rifle
- Author (byline): Patrick F. McManus
- Work: They Shoot Canoes, Don’t They
- Publisher: Holt Paperbacks
- Publication date as stated: Sept 1982
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1673
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patrick F. McManus
Book: They Shoot Canoes, Don’t They
ISBN: 978-0805000306
Publisher: Holt Paperbacks
Date (Month/Year): Sept 1982
```

### Introduction (context only: never use it for content warnings)

```text
There are some lucky people out there who have better jobs or who work at jobs where they do something they like. If you are one of these people, you have to ask yourself; Do you really like your job, or do you just hate your job less than most people? If you had a choice, would you choose to work at your job for 40 hours a week? Let’s face it even “you know what” would get boring after going at it 40 hours a week, 50 weeks a year. Work can spoil anything. Many people love gardening, but farm-work is hot and back-breaking. Cooking can be fun, but working as a cook in a busy restaurant is not. If you like your job now, trust me . . . . you will like your job even more if you work less. In The Rifle, Patrick finds out that working . . . . even if it is to earn money to buy something you REALLY want . . . . is not all it’s cracked up to be. The Rifle by Patrick F. McManus.
```

### Performance text (classify this)

```text
At least once a week from the fifth grade on, I made it a practice to stop by Clyde Fitch’s Sport Shop after school. Clyde was always glad to see me, and we would josh each other.

“Hi, Clyde,” I’d say as I came through the door.

“Don’t handle the guns,” Clyde would say. “You got peanut butter on one of the twelve-gauges last time. I wish you’d find someplace else to eat your after-school snack.”

Before I knew what was happening, a .30-06 would have leaped into my hands and I would be checking its action.

“DON’T TOUCH THE GUNS!” Clyde Fitch would yell, doing a fair impression of an enraged businessman.

“Good, Clyde, good,” I would say as I set the rifle back in the rack and peered down at a sleek, inviting .300. Apparently displeased by my lack of enthusiasm for his performance, Clyde would rush over, grab me by the back of my coat collar and belt, and rush me out the door of his establishment.

Just a few days short of eternity, my fourteenth birthday finally arrived. I had expected it to come bearing as a gift one .30-30 rifle, about which I had dropped approximately 30,000 hints to my family. No rifle! I could tell from the shapes of the packages. They were all shaped like school clothes. “Something seems to be missing here,” I said, nervously ripping open a package of Jockey shorts. “You sure you didn’t forget and leave one of my presents in the closet? I was, uh, sort of expecting a, uh, thirty-thirty rifle.”

“Oh,” Mom said. “Well, if you want a rifle, you’ll just have to get yourself a job and earn enough money to buy one.”

It was not unusual in those days for parents to say brutal things like that to their children. There were no laws back then to prevent parents from saying no and, worse yet, meaning no. Life was hard for a kid. Still, I couldn’t believe that my mother was actually suggesting that her only son go out and find a job.

Naturally, I had heard about work. My family was always talking about it within range of my hearing, and as far as I could tell, seemed generally to be in favor of it. I didn’t know why. Nothing I ever heard about work made it seem very appealing.

Still, if I wanted to hunt deer that coming fall, I would need a rifle. On the other hand, if I got a job, that would ruin my summer and leave me only mornings and evenings and weekends to fish. At best, I might be able to get in some more fishing on days I was too sick to work. I weighed my need for the rifle against a ruined summer and, after much long and painful thought, arrived at a distasteful decision: I would have to borrow a rifle.

Then, as now, people did not stand in line to loan out their rifles to beginning hunters, or to anyone else for that matter. My old friend Rancid Crabtree seemed to me to be the best prospect for the loan of a rifle.

“By the way, Rancid,” I said to him casually one day, “how about loaning me your thirty-thirty for deer season this year.”

Rancid’s face erupted into that beautiful snaggle-toothed grin of his. “Thet’s a good-un,” he said. “Make it up yersef or somebody tell it to you?”

“It’s no joke,” I said. “I need a deer rifle, and I don’t see why you can’t loan me your thirty-thirty.”

“Wall, Ah would loan it to you except fer one thang,” Rancid said. “An’ thet is, Ah don’t want to.”

I shook my head in despair. “You’re the only person I can think of, Rancid, who might loan me a rifle. I guess the only thing left for me to do is to get a job and earn some money.”

“Now don’t go talkin’ like thet,” Rancid said, as soon as he had recovered from the shock. “A young fella like you, got everthang to live fer, talkin’ about getting’ a j-j-jo – throwin’ away his life. No sar, Ah won’t stand fer it! Now, hyar’s what you do. You go as the Inyun if you kin borry one of his rifles.”

“Pinto Jack?”

“Why shore, ol’ Pinto’d give you the hid offen his scrawny carcass iffin it had a zipper on it.”

I found Pinto Jack puffing a pipe on the front porch of his cabin, and put my request straight to him.

Pinto Jack smiled only on rare occasions, and this was not one of them. “You want to borrow my rifle?” he said, studying me thoughtfully through a cloud of pipe smoke. “If I loaned you my rifle, what would I use when I raided the ranchers and burned their buildings and drove off their livestock, and like that?”

“Couldn’t you use a bow and arrow for a few raids?” I said.

“You tell me, how am I going to drive my old truck and shoot a bow and arrow at the same time? No, I got to have my rifle for raiding the ranchers.”

I looked crestfallen, having many years before learned that this was one of the best looks to use on Pinto Jack.

“Tell you what,” he said after a moment. “I could maybe let you use the old rifle my father brought back from the Great War. It’s a single-shot and kicks a bit, but you’re welcome to it.”

I rushed home lugging the monstrous firearm, pinned a target to a fence post backed by a sandbank, paced off a hundred years, drew a bead on the target, and gently squeezed the trigger. Later I heard that all the livestock within a mile radius sprang two feet into the air and went darting about in all directions at that altitude. Apples rained down out of the trees in the orchards. Three lumberjacks swore off drink, and two atheists were converted to religion. My own interpretation of the event was that I had just been struck by lightning, a meteorite, or a bomb. When my vision cleared, I knew I was in trouble. Nevertheless, I decided to try one more shot, this one left-handed. The second shot went off a little better, since by now I knew what to expect. It was easier for me to keep my nose out of the way, too, because the first hot had moved it up into the vacant area above my right eyebrow where it would be safe. By the time I had finished sighting in the rifle, I figured I’d be the only kid in the school talent show who could applaud behind his back with his shoulder blades.

By the time the next summer rolled around, it had become apparent to me that the only way I was ever going to get a deer rifle was to earn the money for it. There was a dairy farmer by the name of Brown who lived nearby and whose reputation in the community was that of a kindly, if somewhat frugal, gentleman. Out of desperation for a deer rifle, I broke down and indentured myself to him at the rate of fifty cents an hour manufacturing postholes. Mr. Brown gave me the job after asking if I thought I could do a man’s work. My ingenious reply was: “it depends on the man.” The farmer said later that he supposed the particular man I had been referring to was an Egyptian mummy. For all his other drawbacks, Mr. Brown did not lack a sense of humor.

About his other drawbacks. It was only after going to work for him that I discovered that he wasn’t a kindly gentleman at all but the former commandant of a slave-labor camp. Our mutual misfortune was that he had somehow missed the last boat to Brazil and had been forced to escape to Idaho, where he took up dairy farming as a cover.

“Vork, vork!” he would scream at me, slapping the leg of his bib overalls with a swagger stick. “Make die postholes, make die postholes, fahster, fahster!”

And I would streak about the landscape, trailing fresh-dug postholes. Sometimes, after glancing nervously around, I would step behind a tree to catch my breath. The farmer would drop out of the branches and screech at me: “Vot you do-ink? I not pay-ink you fifty zents an hour to breathe! Vork! Vork!.”

At the end of the very hour in which I earned the last fifty cents I need to buy the rifle, I resigned my position. When I told the farmer I was quitting, he tried to conceal his disappointment by leaping in the air and clicking his heels. There are few things, by the way, more disgusting than a dairy farmer clicking his heels in the air.

“I’ll say this for you,” he told me. “You have dug what I regard to be the most expensive postholes in the whole history of agriculture. If it was possible, I would gather them all up and put them in a bank vault rather than leave them scattered randomly about my property. Nevertheless, lad, should you ever find yourself in need of a job to buy yourself, say, a shotgun, why you just come to me. I’ll be happy to recommend you as a worker.”

Naturally, I was flattered by this little farewell speech. I even changed my mind about his being a former commandant of a slave-labor camp. “Thanks,” I told him, “but now that I’ve tried work and found it to be about what I expected, I think I’ll avoid it in the future.”

Mr. Brown said he thought that would be a good idea and that, as far as he had observed, I had considerable talent for that line of endeavor and was practically assured of success.
```

---

## IC-2493: The Robin

- Title: The Robin
- Author (byline): Gore Vidal
- Work: A Thirsty Evil
- Publisher: Gay Sunshine Press
- Publication date as stated: Oct 1981
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1708
- Already set (do not supply): none

### Source block (context only)

```text
Author: Gore Vidal
Book: A Thirsty Evil
ISBN: 978-0917342844
Publisher: Gay Sunshine Press
Date (Month/Year): Oct 1981
```

### Introduction (context only: never use it for content warnings)

```text
The power over life and death, the ability to hold the future of another creature in the palm of your hand and decide whether it is worthy of life or should be put to death. In America, some juries are given this dominion over criminals convicted of heinous crimes. Or consider the concept of euthanasia, the practice of killing in a painless or minimally painful way for merciful reasons, usually to end suffering. There are opponents and advocates of both practices and the ethical debate of each situation will rage on for years to come. In The Robin by Gore Vidal, we take a more personal look at this life and death decision.
```

### Performance text (classify this)

```text
I have forgotten whose idea it was first. I hope it was Oliver's. We decided he must be put out of his misery; he must be killed. The decision was made easily enough but when it came to the actual execution we were not only uninventive but frightened.

At nine I was very much tougher than I am now. I enjoyed all sorts of unpleasant things: other people's fights (I was early an audience), automobile accidents, stories of suicides and one particular peepshow at an amusement park near Washington where, through holes in a tall imitation stockade, one could observe an immense plaster elephant goring a plaster Hindu. But best of all I liked the magazines sold in drugstores, magazines with pictures of young women entangled in giant spider webs on their covers and, inside, pictures of the most exciting scenes of torture. I used to sit for hours on the tile floor of a certain drugstore and carefully examine the magazines. Sometimes I even read the stories. I liked very much the directness, the naturalness of the style. I had long since become bored with the colorless fourth-grade reader and I hadn’t yet discovered the Oz books which, at ten, helped bring to an end my tough period.

In the fourth grade I had one close friend: thin pale-haired, pale-eyed, pale-skinned boy whose name was Oliver. I suppose he has since grown up to become a lawyer or a realtor. Most boys from our group in Washington became either one or the other. To my knowledge no one has become anything interesting like a movie star or an artist though a number have been divorced once or twice and several show signs of alcoholism.

Oliver loved violence and torture as much as I did and he was almost as tough as I was, and that was very tough indeed. Our conversation was a mixture of gangster and nursery talk. We organized secret societies, encouraged gang warfare at school, and sometimes we even went to grocery stores and stole.

All of us had elaborate dream worlds. I can guess now what Oliver's was probably like; as for my own, I can remember it vividly: the climate, the scenery and even various plots of my imaginary life when I was nine and depraved. I know I that I had great physical strength and lived in a castle, wore a cloak and very often a crown. I was not only stronger than the other nine-year-olds, I was stronger than grown men too: that deep-voiced, rough-faced alien race. And in my world I invented all sorts of tortures for my enemies. The most constant and satisfactory victim was the fourth-grade teacher, a shapeless woman with bobbed hair, gray and untidy, and a dreadful nose that was thin with a pink, translucent membrane. She almost always had a cold and a fever blister on her upper lip. She was stern, malicious and, in moments of anger, an arm-twister. She received her reward in my world.

About the middle of October, shortly after my ninth birthday, on a clear bright afternoon, Oliver and I saw the robin.

First, let me say that our school was what they call a country day school, several miles from the city. The school had broad, well-kept lawns where less imaginative boys resolved their violence in football and fighting. Oliver and I seldom joined them; we were contemptuous of such simplicity. Sometimes of course we were forced to play and when that happened I'd pick a part of the field where nothing much was going to disturb me and here I would stand and daydream. In these dreams I was the actor, never the audience.

The school occupied a large country home in Virginia some ten minutes by bus from Washington. The house was what we, in that part of the South, call Georgian though actually it was a gracious late 19th century muddle of styles: red brick, with tall windows on the ground floor and inside, a curving staircase. There were high ceilings, cracks in the walls and everywhere the sense of many generations of Southern feudal life. . . actually, the house was the relic of a rich Northerner who, having come South with a Republican administration, built this house, fancied himself a squire, willed it to his children, died and they, true heirs, promptly sold it.

But to us, to the sixty pupils, the grounds were far more interesting than the house: smooth lawn curved from the house to the line of woods where between thin dark trees bright in autumn with the colors of the fool, one could just make out the brown slow Potomac River which roared continuously, sea-like and far away, a sad lonely sound.

The day of the robin was like any other day of autumn. I caught the school bus in front of my house and talked to Oliver as we drove to school. I haven't the faintest idea what our conversations were like when we were nine.

I suppose that Oliver and I discussed our teachers, the other boys and the peculiarities of our parents. I do remember once turning to him and saying solemnly (this was a year later, after my mother's divorce): "We've gone through hell and high water together, my mother and I." By the time I was ten I do recall that I talked almost entirely in sonorous clichés - and I had begun to demonstrate an alarming talent for moral poetry. But at nine, on this sharp October day, I was more colorful, more desperate and certainly more original than I've ever been since.

We arrived at the school, entered the classroom and here recollection ceases. I suppose something must have happened in those classes but I cannot remember what. During the twelve years I spent in schools, I remember almost nothing that happened in the classrooms. I have only one clear memory of my first six years in school. For some reason we built a model of the Appian Way on a card table. And since, among my numerous talents, I had a gift for modeling, I was invited to make the human figures for the Appian Way. They were beautiful, splendid Romans, happily proportioned, clothed in togas of the whitest tissue paper. Everyone was impressed. But unfortunately they would not stand up and the teacher, that thin-lipped terrible woman, squashed all the legs down to fat columns, completely ruining their classic symmetry. When I discovered this, I gave such a demonstration of outraged sensibility that she was forced to call in the principal who tried to soothe me by suggesting that with long togas no one would notice the legs and, besides I should remember I had been commissioned to do figures (very admirable they were, too) which could stand up in chariots.

Aside from this one episode I remember nothing of those six years in the classroom but I do remember the afternoons out of doors, especially this particular afternoon in October. The sky was pale and the clouds were heavy and white and they moved so slowly, changed shape so slowly that one was quite hypnotized watching the castles become elephants, and the elephants swans and the swans teachers. On this day Oliver and I unobtrusively slipped away from our game-playing classmates.

We walked quickly to the edge of the lawn where a wooded cliff dropped nearly vertical to the river below. Here, hidden from the others by a row of evergreens, the river beneath us, we sat comfortably on the ground and I began to make up a story while Oliver listened eagerly, flatteringly.

It was he who noticed the robin first. "Look he said, interrupting me, pointing at something in the grass. I looked and saw the bird. One of its wings had been broken and it fluttered feebly, still trying to fly. We went over and examined carefully. Both wary of touching it for fear of an unexpected sting or bite or sinister germs.

"What'll we do?" I asked. One always had to do something about everything that came one's way.

Oliver shook his head; he was no use. "It’s hurt bad." We watched the robin as it fluttered in a small circle on the ground. It made a small piping sound.

"Maybe we ought to take it home." But Oliver shook his head: "It's hurt too bad. It's not going to live long and anyway we wouldn't know what to do."

"Maybe we should get some witch hazel or something," I suggested; but since this meant approaching the authorities of the school, we decided against doctoring.

I have forgotten whose idea it was first. I hope it was Oliver's. We decided the robin must be put out of its misery; it must be killed. The decision was made easily enough but when it came to the actual execution we were not only uninventive but frightened.

Thinking of a picture I had seen of Saint Stephen, I suggested the robin be killed with stone. Oliver took the first stone (I'm almost certain it was Oliver) and dropped it directly on top of the creature, but the stone fell to one side and the bird, still alive, fluttered its wings and gasped. Then I took a stone and dropped it and now, horribly, there was blood on the wings that fluttered in the bright air, that fanned the dead leaves on the ground.

Then we grew frightened and angry and we took more stones and threw them as hard as we could at the robin, anything to stop the motion of those wings and the sound of pain. The stones fell one upon another until the bird was covered except for its head . . . and still it was not dead: it would not die. Oliver (I am sure now it was Oliver) finally took a very large stone and smashed it as hard as he could on top of the pyramid, finishing the tomb. Then we listened carefully: there were no more sounds from within.

We stood for a long time, not looking at one another, the pile of stones between us. No sound but the distant shouts of our classmates playing on the lawn. The sun shone brilliantly; nothing had changed in the world but suddenly, without a word and at the same moment, we both began to cry.
```

---

## IC-2494: SantaLand Diaries

- Title: SantaLand Diaries
- Author (byline): David Sedaris
- Work: Holidays on Ice, Pgs 1-44
- Publisher: Back Bay Books
- Publication date as stated: Nov 1998
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: DAVID, OFFICIAL VOICE, MAN, SANTA SANTA, RILEY, WOMAN, MAN 1, WOMAN 1
- Teaser before the introduction: Yes
- Spoken words (computed): 1396
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Sedaris
Book: Holidays on Ice, Pgs 1-44
ISBN: 978-0316779234
Publisher: Back Bay Books
Date (Month/Year): Nov 1998
```

### Introduction (context only: never use it for content warnings)

```text
PERKS TO BEING AN ELF: You can walk home with all the leftover toys come December 25th . . . a never-ending supply of cookies, milk, hot chocolate and other tasty holiday treats. THE DOWN SIDE: Elves are required to wait on Santa and Mrs. Claus hand and foot . . . Mall Duty: they receive the brunt of screaming kids, stray kicks to the shins and sticky candy cane hands in their hair. So even though Will Ferrell made being an ELF seem like the next best thing to Christmas . . . the reality of being a mall elf is, well . . . my therapist suggested that I should keep

SantaLand Diaries by David Sedaris
```

### Performance text (classify this)

```text
DAVID: (Pgs 1-44) I was in a coffee shop looking through the want ads when I read:

OFFICIAL VOICE: Macy's Herald Square, the largest store in the world, has big opportunities for outgoing, fun-loving people of all shapes and sizes who want more than just a holiday job! Working as an elf in Macy's SantaLand means being at the center of the excitement!

DAVID: This morning we were lectured by the Santa-Land managers and presented with a Xeroxed booklet of regulations titled "The Elfin Guide." In the afternoon we were given a tour of SantaLand, which really is something. It's beautiful, a real wonderland, with ten thousand sparkling lights, false snow, train sets, bridges, decorated trees, mechanical penguins and bears, and really tall candy canes.

We traveled the path a second time and were given the code names for various posts, such as "The Vomit Corner," a mirrored wall near the Magic Tree, where nauseous children tend to surrender the contents of their stomachs. When someone vomits, the nearest elf is supposed to yell "VAMOOSE," which is the name of the janitorial product used by the store. We were taken to the "Oh, My God, Corner," a position near the escalator. People arriving see the long line and say "Oh, my God!" and it is an elf's job to calm them down and explain that it will take no longer than an hour to see Santa.

We were given a demonstration of the various positions in action, performed by returning elves who were so animated and relentlessly cheerful that it embarrassed me to walk past them. I don't know that I could look someone in the eye and exclaim, "Oh, my goodness, I think I see Santa!" or "Can you close your eyes and make a very special Christmas wish!" Everything these elves said had an exclamation point at the end of it!!! I am afraid I won't be able to provide the grinding enthusiasm Santa is asking for. I'll be a low-key sort of an elf.

My costume is green. I wear green velvet knickers, a yellow turtleneck, a forest-green velvet smock, and a perky stocking cap decorated with spangles. My elf name is Crumpet. We were allowed to choose our own names and given permission to change them according to our outlook on the snowy world.

Today was the official opening day of SantaLand and I worked as a Magic Window Elf. The Magic Window is located in the adult "Quick Peep" line. My job was to say, "Step on the Magic Star and look through the window, and you can see Santa!" I was at the Magic Window for 15 minutes before a man approached me

MAN: You look so stupid.

DAVID: He had a point. But, at least I get paid to look stupid; he gives it away for free. But I can't say things like that because I'm supposed to be merry. So instead I said, "Thank you!" as if I had misunderstood and thought he said, "You look terrific." (to man) Thank you!

[One day] I was stuck being Photo Elf with Santa Santa. I don't know his real name; no one does. During most days, there is a slow period when you sit around the house and talk to your Santa. Most of them are nice guys and we sit around and laugh, but Santa Santa takes himself a bit too seriously. I asked him where he lives, Brooklyn or Manhattan.

SANTA SANTA: Why, I live at the North Pole with Mrs. Claus! (Santa laugh)

DAVID: I asked what he does the rest of the year . . .

SANTA SANTA: (Santa laugh) I make toys for all of the children.

DAVID: (to Santa) Yes, but what do you do for money?

SANTA SANTA: Santa doesn't need money. (Santa laugh)

DAVID: Santa Santa sits and waves and jingles his bell sash when no one is there. He actually recited "The Night Before Christmas," and it was just the two of us in the house, no children. Just us. What do you do with a nut like that?

SANTA SANTA: Oh, Little Elf, Little Elf, straighten up those mantel toys for Santa.

DAVID: I reminded him that I have a name, Crumpet, and then I straightened up the stuffed animals. (beat) Santa Santa has an elaborate little act for the children. He'll talk to them and give a hearty chuckle and ring his bells and then he asks them to name their favorite Christmas carol. Most of them say "Rudolph, the Red- Nosed Reindeer." Santa Santa then asks if they will sing it for him. The children are shy and don't want to sing out loud, so Santa Santa says

SANTA SANTA: Oh, Little Elf, Little Elf! Help young Brenda to sing that favorite carol of hers.

DAVID: Then I have to stand there and (sings enthusiastically) Rudolph, the Red-Nosed Reindeer. . (drops elf façade) which I hate. Half the time young Brenda's parents are my age and that certainly doesn't help!

[Another day] I worked as an Exit Elf, telling people (in a loud voice) THIS WAY OUT OF SANTALAND. A woman was standing at one of the cash registers paying for her idea of a picture, while her son lay beneath her having a tantrum.

RILEY: (pitches a tremendous fit)

WOMAN: Riley, if you don't start behaving yourself, Santa's not going to bring you any of those toys you asked for.

RILEY: He is too going to bring me toys, liar, he already told me!

WOMAN: (grabbing David’s arm) You there, Elf, tell Riley here that if he doesn't start behaving immediately, then Santa's going to change his mind and bring him coal for Christmas.

DAVID: (to audience) I told her Santa no longer traffics in coal. Instead, if you're bad he comes to your house and steals things If he didn't behave himself, Santa was going to take away his TV and all his electrical appliances and leave him in the dark. (to Riley) All your appliances, including the refrigerator!

RILEY: (pitches a tremendous fit)

DAVID: Your food is going to spoil and smell bad!

RILEY: (continues his fit)

DAVID: It's going to be so cold and dark where you are. Man, Riley, are you ever going to suffer! You're going to wish you never heard the name Santa!

RILEY: (gasps for air, processes the new information and abruptly stops his fit)

DAVID: Lately I am feeling trollish and have changed my elf name from Crumpet to Blisters. Blisters — I think it's cute.

I was the Pointer Elf this afternoon, one of my favorite jobs. The Pointer stands inside the Magic Tree and appoints available Santa Elves to lead parties of visitors to the houses. First-time visitors are enthusiastic, eager that they are moments away from Santa. Some of the others, having been here before, have decided to leave nothing to chance.

Out of all the Santas, two are black and both are so light-skinned that, with the beard and makeup, you would be hard-pressed to determine their race. Last week, a Black woman became upset when, having requested a "Santa of Color," she was sent to Jerome. I've had requests from both sides -- White Santa, Black Santa. A Pointer Elf is instructed to . . . (shrugs shoulders, feigning ignorance) There's only one Santa.

After she was led to the house, the woman demanded to speak with a manager.

WOMAN: (complaining) He's not black!

DAVID: Bridget assured this woman that Jerome was indeed black.

WOMAN: Well, he isn't black enough!

DAVID: We were packed today, absolutely packed, and everyone was cranky. Once the line gets long, we break it up into four different lines because anyone in their right mind would leave if they knew it would take over 2 hours to see Santa. 2 hours — you could see a movie in 2 hours. Standing in a 2-hour line makes people worry that they're not living in a democratic nation. People stand in line for 2 hours and they go over the edge. I was sent into the hallway to direct the second phase of the line. The hallway was packed with people, and all of them seemed to stop me with a question.

MAN 1: Which way to the down escalator,

WOMAN 1: Which way to the elevator (rapidly changing voices and personas) the Patio Restaurant, gift wrap, the women's rest room, Trim-A-Tree.

DAVID: There was a line for Santa and a line for the women's bathroom, and one woman, after asking me a dozen questions already, asked

WOMAN: Which is the line for the women's bathroom?

DAVID: (shouting) The line with all the women in it!

WOMAN: I'm going to have you fired!

DAVID: I had two people say that to me today

MAN: I'm going to have you fired!

DAVID: Go ahead, be my guest. I'm wearing a green velvet costume; it doesn't get any worse than this. Who do these people think they are? (sings the first verse) You’d better watch out . . .
```

---

## IC-2495: Saying No to Nick

- Title: Saying No to Nick
- Author (byline): Bruce Coville
- Work: Twice Told: Original Stories Inspired by Original Artwork, Pgs 45-58
- Publisher: Dutton Juvenile
- Publication date as stated: April 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JEREMY, NICK
- Teaser before the introduction: Yes
- Spoken words (computed): 2108
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bruce Coville
Book: Twice Told: Original Stories Inspired by Original
Artwork, Pgs 45-58
ISBN: 978-0525468189
Publisher: Dutton Juvenile
Date (Month/Year): April 2006
```

### Introduction (context only: never use it for content warnings)

```text
Saying No to Nick by Bruce Coville
```

### Performance text (classify this)

```text
JEREMY: (Pg 45-58) Nick Foster used to be my best friend, and boy, let me tell you, I miss him. It’s not like we had a fight or anything. It’s just that I died. Well, I didn’t just die. The process was pretty painful and horrible – horrible for me but even worse, I think, for Nick. After all, the two of us had been best friends since kindergarten.

JEREMY: It seems so weird not to be able to talk to him now. I miss him every day. Of course, the fact that What Do I miss? Is one of the games we play most often here in The Waiting Room doesn’t help any.

I don’t suppose “The Waiting Room” is the real name for where I am. But it’s what most of us call it, since it’s been made clear to us that this is just a temporary stop.

Okay, What do I Miss? Peanut butter. Sumer vacation. Comic books. Eighth grade, believe it or not. My parents. My dog. Nick.

We were in seventh grade when Nick got really interested in religion. Actually, what he got interested in first was Stacy Prendergast and her shining red hair. Since Stacy was all wrapped up in her church’s youth group, Nick decided to join it so he could be near her. This meant that I joined too.

The youth group was all right. We did do a lot of praying, which kind of annoyed me at the time. But who knows – it might be one reason I’m here in The Waiting Room and not someplace a lot worse! I was just as happy when Nick decided he wasn’t in love with Stacy anymore, and we could drop out. But as it turned out, even though Nick was no longer in love with Stacy, he had fallen in love with God. Which was how we ended up doing the baptism.

Nick had always liked ceremonies – we had buried more animals in his backyard than I could count. Nick always said a few words over the grave. I think that was his favorite part.

He was good with words – it was one of the things that made it so hard for me to say no when he got an idea. We were lying in my backyard one night last July, looking at the stars when Nick said . . .

NICK: I think we should do a baptism ceremony, Jeremy. It’s a way of cleansing ourselves. Starting over.

JEREMY: What do we need a cleansing for?

NICK: (laughing) Are you telling me you’ve led a life without sin?

JEREMY: Don’t we need a priest for something like that?

NICK: Nah. Priests just get in the way. They put a layer between you and God.

JEREMY: (to audience) I didn’t want to admit to Nick that if there really was a God, having a layer between me and him, her, or it didn’t seem like such a bad idea.

NICK: We’ll do it at my house. We can use the swimming pool. If we’re gonna do this, we’re gonna do it mountaintop.

JEREMY: (to audience) Mountaintop was a Nickism. It meant doing something all out, all the way.

NICK: Total immersion is what it’s called. Come over after your folks have left for work tomorrow. We’ll have the house to ourselves.

JEREMY: (to audience) I still wasn’t taking this baptism thing all that seriously. But as Nick kept talking, I realized he was dead serious.

NICK: This is going to help us get pure again. It will take us back to our state of original grace.

JEREMY: What are you talking about?

NICK: It’s going to wash away our transgressions. And don’t tell me you don’t have any, Jeremy. I saw you looking at Mary Sue Betts at the mall yesterday. Lust in your heart is a sin in itself. And we never told Mrs. Parker about that window we broke. Come on, Jeremy. This is important.

JEREMY: (to audience) So the next day I showed up at Nick’s house, ready for the baptism. He had written out the whole ceremony, and I have to admit it was pretty good. He had tucked the script inside a plastic binder sheet, so we could take it into the water with us. (to Nick) Are you sure it’s not sacrilegious for us to do this? I mean, it’s not like we’re priests or ministers or anything.

NICK: I don’t think God cars about that. Come on, let’s get out of our clothes.

JEREMY: What?

NICK: We’ve got to be naked to do this. It’s like being born. And you don’t get born with clothes on. Mountaintop, Jeremy, just like I said. Look, I’ve got sheets we can wrap around us when we go outside. But once we go into the pool, it’s birthday suit city.

JEREMY: (to audience) We got undressed and wrapped the sheets around us, then went out to the pool. (to Nick) Who goes first?

NICK: Me, because it was my idea. What we do is, I lie back in the water – you’ll have to support me with one arm – and you follow the scripts. It will tell you when to lower me into the water.

JEREMY: I held out my right arm, and cradled Nick’s head. Then I read aloud what was in the script. When I got to the part that said “It is time for you to be washed free of your sins,” I lowered my arm to let his head into the water. He was kind of floating, so I had to push him down to get him completely under. I wasn’t sure how long I was supposed to keep him that way, so I held my breath myself, and when it started to get a little uncomfortable, I let him back up.

NICK: (gasping for breath, shaking water from his head) That was great! Okay, now it’s your turn.

JEREMY: We switched places. Nick began to speak, though I think he was reciting from memory rather than reading from the script.

NICK: (formally) We come to the water to be washed free of our sins, so that we may become as little children again, pure in the eyes of God, closer to the heart of the universe. Do you, Jeremy, come to this of your own free will.

JEREMY: Yes. (to audience) I don’t think that was a lie, really. I think I could have backed out, even then. But I had never said no to Nick before, and this didn’t seem like the time to start.

NICK: Then it is time for you to be washed free of your sins

(pushing Jeremy under)

JEREMY: (to audience; speaking calmly in memory) It wasn’t Nick’s fault that I panicked. Maybe I was just spooked by all that God stuff. Whatever the reason, I began to thrash and fight to get up. Did Nick try to hold me down? I honestly can’t remember. What I do remember is that somehow I got a big mouthful of water and began gasping for breath. I was terrified. I felt as if my heart was trying to beat its way out of my chest.

It wasn’t Nick’s fault. It surely wasn’t his fault that I had a weakness in my heart that no one – not me, not my parents, not my doctor – even knew was there. Not his fault that my heart blew a valve. Not his fault that I went limp and died there in the pool, in his arms. Not his fault at all.

Somewhere far behind me I could hear Nick . . .

NICK: (sobbing) No! No! Jeremy! Come back! Jeremy!

JEREMY: (to audience) But it was too late for that. For once I couldn’t do what Nick said. (beat) It took me a while to get used to The Waiting Room and then I figured out how to ‘Drop In’ -- when you go back to the physical world to check on things. A lot of people advised not to do it. They think Dropping In somehow makes it hard to ‘Move On’. I was in no hurry to ‘Move On’.

I went to see Nick. Only he didn’t look like Nick. I could tell he was being turned inside out by guilt. It was sad. The whole reason he had come up with the baptism was to get rid of guilt, and now he had more of it than ever. But after a while I figured out that it wasn’t only guilt that was eating at him. It was shame.

The whispering was what tipped me off: kids whispering when Nick walked by. Nick had killed me, they were saying – killed me because we were boyfriends. I was so furious and baffled when I heard them that it took me a while to figure out the obvious: Nick had called 911, of course, and when the rescue squad got to his place, they found my naked body. Nick was probably still naked too. The baptism script might have been enough to convince the police of what had really happened, but it had no power against the mighty tongue of Rumor.

It made me sick. Not out of shame – you start to let go of that here in The Waiting Room – but because I could tell it was making Nick sick too. Even so, I didn’t realize he was in danger until the afternoon I ‘Dropped In’ to check on him and found him standing at the edge of the pool, staring into the blue ripples.

As I watched, he knelt and dipped his hand into the water.

Then he gripped the edge of the pool and lowered his head. His shoulders began to shake. He stayed that way for a long time. I wanted to talk to him but didn’t know how. I had no voice, no body, no way to say, “It’s not your fault, Nick. I’m not angry. I forgive you.”

I checked on him every day after that, and every day would find him standing at the edge of the pool, staring into the water as if he could still see me there, as if by looking hard enough he could bring me back, make it all go away. I knew it was getting worse. (watching, sadly, then. . .)

Nick goes into the house. I follow. He goes to the garage and takes some rope from his father’s workbench. Then he picks up a concrete block. I feel sick. I can’t watch this. I have to. I follow him back to the pool’s edge.

NICK: (crying) I’m sorry, Jeremy . . . I’m so sorry.

JEREMY: Slowly, carefully, he ties the rope around his waist. (shouts) Nick, don’t! No sound, even though I’m shouting it with every fiber of my being. He stands the concrete block on end, loops the rope through it, ties another knot. Ties it close, ties it tight. He stands, picks up the block, holds it over the water. I fling myself at him, crying, “No, no, no!” And then I’m inside him.

NICK: Jeremy?

JEREMY: I feel the question, feel his shock, feel his fear and astonishment and hope. And I feel one more thing. Nick did love me, and not just as a friend. He loved me and never dared say it, and I died in his arms with him feeling it, and all the rumors that had no truth in reality had a slicing truth in his own heart.

NICK: (crying) I’m so sorry. But I’m going to make up for it. I’m going to make up for what I did. (holds block over the water)

JEREMY: No, no, no, no no! (to audience) It’s like a wrestling match for a while, Nick willing his arms to drop the block into the pool, me fighting him, trying to control his body and all the while thinking, It’s all right, Nick. It’s all right.

NICK: (tormented) It’s not!

JEREMY: (to Nick) You were my hero. Heroes don’t quit.

NICK: I’m so tired, Jeremy. And I hurt so much. And I’m so ashamed. I hate myself.

JEREMY: I don’t hate you. (to audience) And then I realize it’s not enough, so I give him the harder words, the words I could never have spoken, or even thought, before I died, words it’s hard to repeat even now, even though they’re true. (to Nick) I love you, Nick.

And that stops him. He puts the block down, then collapses next to it, clutching it as if for some comfort, as if he needs something, anything to hold on to. He begins to sob. He’s still sobbing when his parents come home. Which is when I leave.

So now I know. You can’t fix someone else’s broken heart. And you can’t take on someone else’s guilt. All you can do is love them. (beat) I’m going now. Someone – I don’t know who -- has called me. My stay in The Waiting Room is over. I suppose I’ll never see Nick again. But I’m glad I could be there for him that one last time. Glad I could tell him I loved him, even if it wasn’t the way he wanted. Glad I could finally tell him no.

Good-bye, Nick. I love you.
```

---

## IC-2496: Secret

- Title: Secret
- Author (byline): Jared Carter
- Work: Peoples Culture, a new series #24-25 (1994-1995): 2-3 a literary magazine published in Kansas City, KS by Fred Whitehead
- Publisher: Fred Whitehead
- Publication date as stated: 1994
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1647
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jared Carter
Alternate Title: Disclosure
Book: Peoples Culture, a new series #24-25 (1994-1995):
2-3 a literary magazine published in Kansas City,
KS by Fred Whitehead
ISBN: N/A
Publisher: Fred Whitehead
Date (Month/Year): 1994
Peoples Culture, PO Box 5224, Kansas City, KS 66119.
Edited by Fred Whitehead. Single issue $2.50;
Subscription (6 issues) $15.
```

### Introduction (context only: never use it for content warnings)

```text
Every place like every person has its secrets, holes and entryways into the earth, its shafts abandoned and still burning underground. Today, you will discover Jared Carter’s family Secret.
```

### Performance text (classify this)

```text
Over there, in the corner. Shine your light
that way. Through that door. Watch your step.
Lumps of leftover coal. Years ago the furnace
was converted to gas. No one comes here now.
Careful. Look out for the cobwebs overhead.
This place is filled with them, up at the top,
one side to the other. Sometimes I think
if you poked a stick in here, it would be taken
from your hand, and disappear. But imagine—
when they were first built, they were clear.
A new web shows nothing. By definition
it’s transparent. With time, with dust and grit
sifting down through the joists and floorboards,
it begins to change. To emerge, even in the dark,
as something substantial. Made tangible now.
What’s left is fragile. But balanced. Layer
upon layer, one whorl leading back into another,
nothing to disturb the whole. Nothing to come near,
for months, years. All this patience, this industry
underground. These paths curving back to zero.

Coal Cellar ( Poetry, Midwest Winter 2005, Number 12 (Volume 4, Number 3) ISSN 1536-870X Copyright ©1995–2005, Poetry Midwest. All rights reserved. Poetry Midwest is published electronically three times a year (Spring/Summer, Fall, Winter) by Poetry Midwest. Office at Poetry Midwest, 4909 West 69th Street, Prairie Village, KS 66208, USA.

When my father reached the mandatory retirement age, I applied for permission to visit him for an evening. I wanted to encourage him as he made the transition from a lifetime of hard work to one of leisure and rest. My walk took me through the oldest part of the city, down cobbled streets and along brick sidewalks half-obscured by patches of crabgrass and occasional clumps of dandelion.

He had placed a candle in the window of his small frame house—the very house in which I was born, and had spent my childhood. Other houses along the street were boarded up. People had been moving out; many of the houses stood dark and empty. There was a burnt smell in the air, like fresh tar.

I passed beneath an enormous elevated highway. From factories half a mile away, behind chain-link fences, tall chimneys gave off showers of sparks and plumes of smoke. Through banks of overhead windows came an odd, flickering light cast by the ceaseless cutting and welding of metal sheets and iron girders.

My father greeted me at the door. He looked tired and worn, though I pretended not to notice. He took the candle from the window and led me to the kitchen. We sat down at the same wooden table I remembered from my youth. From a half-filled bottle of red wine he poured out two small glasses. With the candle between us, we talked about his retirement, and how the house was holding up. Eventually he asked about my wife and children.

I steered the conversation to the subject of his health. What was he going to do with his remaining years? I had a suggestion. As a young man he had been good with his hands, and had hoped to become an artisan—a carpenter, perhaps, or a cabinet-maker. Circumstances had prevented this, however. During his final term at school his abilities had been reassessed, and he had been given a more technical assignment.

Nonetheless, I said, I distinctly remembered that when I was a boy, he had fashioned a series of remarkably lifelike dolls, and had given them to my sisters to play with. These beautiful objects were made of wax and linen, and wood from an apple tree that had stood in our yard. He had carved the heads and hands from a fallen branch of that forgotten tree. My two sisters played with these dolls every day until they fell to pieces. I mentioned this now, in the hope that his former pastime might again become a source of satisfaction during his declining years.

He thanked me, and explained that it was time I learned something he had never told to anyone else. Not even my mother had known of it during her lifetime. He took down a coal-oil lantern—the kind used in the early days of railroading—and lit it with the candle. He beckoned, and I followed him through the door to the cellar and down the stairs. We passed through whitewashed rooms where strands of cobweb brushed against our faces. He paused before a low wooden doorframe set in the earth—a feature I had never noticed before. He opened the door.

We entered a downward-sloping tunnel and descended for several minutes, reaching out to touch and feel our way along the damp, rough walls. Eventually I could no longer hear the humming nor feel the vibrations of the factories and mills in the industrial sector above us. We came out at last into a measureless, dark, cool space somewhere beneath the city. I expressed surprise, for I knew there were no caves in this region.

He agreed, explaining, as he took down and lit a second lantern and handed it to me, that he had hollowed out the space by himself during a period of many years—had brought up the earth in small quantities, and scattered it in abandoned lots and waste places, in such a way that the authorities had never noticed.

The sound of his voice was swallowed up in the darkness that surrounded us. I held up the second lantern. Its light failed to show the limits of the excavation, and I had no way of judging its true dimensions. Crude timbers shored up the edges, but the earthen vault itself, looming in the darkness over our heads, appeared to be of cathedral proportions.

In that same instant I saw the reason for our descent: immediately before us, on a platform of planks, lay supine a colossal male figure, fifty feet or more in length. It was nude, muscular and lean, and extremely vivid in every detail. Its size and the dimness of the light prevented me from seeing it entirely, but at my father's bidding I approached and began to examine it more closely.

An upturned hand lay alongside the huge torso. The deep creases of the palm, the whorls of the fingertips, the thick nails—all this was truly remarkable. While studying these details, I had the momentary impression—no doubt a trick of the shadows—that a slight tremor had moved across the figure's chest.

I moved in that direction and held up the lantern but could detect no further motion. Everything was still.

Some elusive presence, momentarily drawn close, seemed to wait suspended now, as though about to flow again. I stood beside a massive forearm over which great veins coiled and intertwined like the exposed roots of trees. I turned to my father. "Is it finished?" I asked.

"No, not yet."

"You're still working on it? And this is why you always seemed so tired?"

"Only a little more," he said. "When it is done, it will have taken my entire life."

"But how?" I asked. "And why?"

"I cannot remember," he said. "I began it such a very long time ago, before you were born. I brought the necessary materials home each night from the factory, in small quantities, hiding them in my lunch bucket. And the tools, too, though there were not many I could take without arousing suspicion. But the skills I developed were more important than the equipment.

"I learned many things as I worked here by myself. Now, as you can see, I am nearly exhausted. My brain is weary, my body worn—from years of daytime labor, from long nights spent down here in the weak light and the dampness of the earth. It has taken me so long I have forgotten the secrets of the craft I once taught myself. My mind has begun to fail. I could not tell you how I managed to build it, nor even why I began. All I know is that it is here."

"Yes," I said, gaining the courage to reach out and touch one of the enormous fingers, and finding the skin to be as warm and supple as my own.

"Originally I may have conceived of it as a commemorative vessel or tomb," he said. "I seem to recall that at one time its chest contained a cavity, behind a set of sliding panels—a space into which a human being could have climbed. It might have been a bridge or pilot-house from which the figure was to be steered, after being equipped for movement. But it could just as easily have been a temporary stage of construction, one that was eliminated as the improvements continued.

"Whatever the intention," he said, raising his lantern above the colossal chest—whereupon I blinked several times before reassuring myself that it was not actually breathing—"there is, as you can see, no trace of any door or opening."

He indicated that we should be returning soon. "But what will happen now?" I asked. "What will become of it?"

"It will remain here, of course," he replied. "It would be impossible to lift it to the surface, unless the factories and warehouses directly above it were first removed. We are too far down, and it is much too large. My last act, before my death, will be to seal off the single narrow passageway that led us here, so that no one will ever find it."

"And it will lie here—forever?"

"I do not know," he said, taking the lantern I held and putting out its flame, and hanging it on a nearby post. He held up the remaining lantern so that its pale light fell across his enormous, shadowy creation.

"That is not for me to know," he said, pointing ahead now and beginning to guide me back toward the entrance to the tunnel, "nor for you."
```

---

## IC-2497: The Secret Life of Walter Mitty

- Title: The Secret Life of Walter Mitty
- Author (byline): James Thurber
- Work: Not specified
- Publisher: Creative Education
- Publication date as stated: Nov 1983
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: COMMANDER, NARRATOR, LTN BERG, MRS. MITTY, WALTER, NURSE, DR. RENSHAW, DR. P-M, INTERN, WALKER, PARKING LOT ATTENDANT, DISTRICT ATTORNEY, MITTY’S ATTORNEY, PASSING WOMAN, CLERK, SERGEANT, CAPTAIN MITTY
- Teaser before the introduction: Yes
- Spoken words (computed): 1364
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Thurber
ISBN: 978-0871919618
Publisher: Creative Education
Date (Month/Year): Nov 1983
```

### Introduction (context only: never use it for content warnings)

```text
Ever wish you could escape the crushing responsibility of remembering grocery lists, making small talk, or figuring out why you walked into a room… and instead enter a world where you are always the main character?

A world where every decision is bold, every line is dramatic, and no one ever asks, “Did you remember the puppy biscuits?” (harumph) Obviously, you’re too busy saving lives, winning battles, and looking incredibly cool while doing it.

For octogenarian Walter Mitty reality is optional, heroism is guaranteed, and the only real danger is getting snapped back to the boring real world at the worst possible moments.

The Secret Life of Walter Mitty by James Thurber
```

### Performance text (classify this)

```text
DAYDREAM #1

(Somewhere in a Navy hydroplane in a winter storm)

COMMANDER: We're going through!

NARRATOR: The Commander's voice was like thin ice breaking. He wore his full-dress uniform, with the heavily braided white cap pulled down rakishly over one cold gray eye.

LTN BERG: We can't make it, sir. It's spoiling for a hurricane, if you ask me.

COMMANDER: I'm not asking you, Lieutenant Berg. Throw on the power lights! Rev her up to 8500! We're going through!

NARRATOR: The pounding of the cylinders increased (ta-pocketa-pocketa-pocketa-pocketa-pocketa)

COMMANDER: (twisting a row of dials, shouting) Switch on No. 8 auxiliary! Full strength in No. 3 turret!

LTN BERG: No. 8 auxiliary! Full strength in No. 3 turret! The Old Man'll get us through. The Old Man ain't afraid of hell!

NARRATOR: The pounding of the cylinders increased (ta-pocketa-pocketa-pocketa-pocketa-pocketa. Walter is immersed in his daydream) REALITY

MRS. MITTY: Not so fast! You're driving too fast! What are you driving so fast for?

WALTER: Hmm?

NARRATOR: He looked at his wife, in the seat beside him, with shocked astonishment. She seemed grossly unfamiliar, like a strange woman who had yelled at him in a crowd. MRS. MITTY: You were up to 55. You know I don't like to go more than 40. You were up to 55.

NARRATOR: Walter Mitty drove on in silence, the roaring of the SN202 through the worst storm in 20 years of Navy flying fading in the airways of his mind.

MRS. MITTY: You're tensed up again. It's one of your days. I wish you'd let Dr. Renshaw look you over.

NARRATOR: Walter Mitty stopped the car in front of the building where his wife went to have her hair done.

MRS. MITTY: Remember to get those overshoes while I'm having my hair done.

WALTER: I don't need overshoes.

MRS. MITTY: (arranging things in her handbag) We've been all through that. (getting out of the car) You're not a young man any longer.

WALTER: (races the engine a little - ta-pocketa-pocketa-pocketa-pocketa-pocketa)

MRS. MITTY: Why don't you wear your gloves? Have you lost your gloves? (Walter reaches in a pocket; brings out the gloves and puts them on)

NARRATOR: But after she had turned and gone into the building and he had driven on to a red light, he took them off again. He drove around the streets aimlessly for a time, and then he drove past the hospital. DAYDREAM #2

NURSE: It's the millionaire banker, Wellington McMillan.

WALTER: (removing his gloves slowly) Yes? Who has the case?

NURSE: Dr. Renshaw and Dr. Benbow, but there are two specialists here, Dr. Remington from New York and Dr. Pritchard-Mitford from London. He flew over.

DR. RENSHAW: (entering, looking distraught and haggard) Hello, Mitty. We're having the devil's own time with McMillan, the millionaire banker and close personal friend of Roosevelt. Obstreosis of the ductal tract. Wish you'd take a look at him.

NARRATOR: In the operating room there were whispered introductions.

DR. RENSHAW: Dr. Remington, Dr. Mitty. Dr. Pritchard- Mitford, Dr. Mitty.

DR. P-M: (shaking Walter’s hand) I've read your book on streptothricosis. A brilliant performance, sir.

NARRATOR: A huge, complicated machine, connected to the operating table began at this moment to go (pocketa-pocketa-queep-pocketa-queep)

INTERN: The new anesthetizer is giving away! There is no one in the East who knows how to fix it!

WALKER: (in a low cool voice) Quiet, man! (moving dials on the machine) Give me a fountain pen! (he pulls a faulty piston from the machine and inserts the pen) That will hold for 10 minutes. Get on with the operation.

NARRATOR: A nurse hurried over and whispered to Renshaw, and Mitty saw the man turn pale.

DR. RENSHAW: (nervously) Coreopsis has set in. If you would take over, Mitty?

NARRATOR: Mitty looked at him and at the uncertain faces of the two great specialists.

WALTER: If you wish. (he dons a surgical gown, adjust a mask and pulls on thin latex gloves) REALITY

PARKING LOT ATTENDANT: Back it up, Mac!! Look out for that Buick! (Walter jams on the breaks in a panic) Wrong lane, Mac.

WALTER: Gee. Yeh.

NARRATOR: He began cautiously to back out of the lane marked "Exit Only."

PARKING LOT ATTENDANT: Leave her sit there. I'll put her away. (Walter gets out of the car) Hey, better leave the key.

WALTER: Oh . . . (handing the man the ignition key)

NARRATOR: The attendant vaulted into the car, backed it up with insolent skill, and put it where it belonged.

WALTER: (he walks away muttering) They're so damn cocky, They think they know everything.

NARRATOR: Once he had tried to take his chains off, outside New Milford, and he had got them wound around the axles. A man had had to come out in a wrecking car and unwind them, a young, grinning garage man. Since then Mrs. Mitty always made him drive to a garage to have the chains taken off.

WALTER: The next time, I'll wear my right arm in a sling; they won't grin at me then. I'll have my right arm in a sling and they'll see I couldn't possibly take the chains off myself. (kicks at something on the sidewalk as he remembers his task) Overshoes.

NARRATOR: When he came out into the street again, with the overshoes in a box under his arm, Walter Mitty began to wonder what the other thing was his wife had told him to get. She had told him twice before they set out from their house. In a way he hated these weekly trips to town- -he was always getting something wrong.

WALTER: Kleenex? No. Razor blades? No. Tooth paste?

NARRATOR: He gave it up. But she would remember it.

WALTER: (mimicking Mrs. Mitty) Where's the what's-its-name.

NARRATOR: A newsboy went by shouting something about the Waterbury trial. DAYDREAM #3

DISTRICT ATTORNEY: (holding out an automatic gun to the person on the witness stand) Perhaps this will refresh your memory. Have you ever seen this before?

WALTER: (takes the gun and examines it expertly, then calmly) This is my Webley-Vickers 50.80.

NARRATOR: An excited buzz ran around the courtroom. The Judge rapped for order.

DISTRICT ATTORNEY: You are a crack shot with any sort of firearms, I believe?

MITTY’S ATTORNEY: Objection! We have shown that the defendant could not have fired the shot. We have shown that he wore his right arm in a sling on the night of the 14th of July.

WALTER: (raises his hand and the bickering attorneys are stilled) With any known make of gun, I could have killed Gregory Fitzhurst at three hundred feet with my left hand.

NARRATOR: Pandemonium broke loose in the courtroom. A woman's scream rose above the bedlam and suddenly a lovely, dark-haired girl was in Walter Mitty's arms. The District Attorney struck at her savagely.

WALTER: (lets the DA have it on the point of his chin) You miserable cur! (the word “cur” brings him back to reality) REALITY

WALTER: Puppy biscuit. . .

PASSING WOMAN: (laughs) He said “Puppy biscuit.” That man said “Puppy biscuit” to himself.

NARRATOR: Walter Mitty hurried on. He went into an A&P.

WALTER: I want some biscuit for small, young dogs.

CLERK: Any special brand, sir?

NARRATOR: The greatest pistol shot in the world thought a moment . . .

WALTER: It says 'Puppies Bark for It' on the box. (looks at his watch)

NARRATOR: His wife would be through at the hairdresser's in fifteen minutes. She didn't like to get to the hotel first, she would want him to be there waiting for her as usual. He found a big leather chair in the lobby, facing a window, and he put the overshoes and the puppy biscuit on the floor beside it. He picked up an old copy of Liberty and sank down into the chair.

WALTER: (reading a headline) Can Germany Conquer the World Through the Air? DAYDREAM #4

SERGEANT: The cannonading has got the wind up in young Raleigh, sir.

CAPTAIN MITTY: (wearily) Get him to bed with the others. I'll fly alone.

SERGEANT: (anxiously) But you can't, sir. It takes two men to handle that bomber and the Archies are pounding the hell out of the air. Von Richtman's circus is between here and Saulier.

WALTER: Somebody's got to get that ammunition dump. I'm going over. (pours a drink) Spot of brandy?

NARRATOR: War thundered and whined around the dugout and battered at the door. There was a rending of wood and splinters flew through the room.

WALTER: (barely flinching) A bit of a near thing.

SERGEANT: The box barrage is closing in!

WALTER: (with a faint fleeting smile) We only live once, Sergeant . . . Or do we? (pours another shot and throws it back)

SERGEANT: I’ve never seen a man could hold his brandy like you, sir. (Mitty straps on his huge Webley-Vickers automatic) Begging your pardon, sir. It's 40 kilometers through hell, sir.

WALTER: (finishes one last brandy, speak softly) After all, what isn't?

NARRATOR: The pounding of the cannon increased; there was the rat-tat-tatting of machine guns, and from somewhere came the menacing (ta-pocketa-pocketa-pocketa-pocketa-pocketa) of the new flame-throwers. REALITY

MRS. MITTY: (striking Walter on the shoulder) I've been looking all over this hotel for you. Why do you have to hide in this old chair? How did you expect me to find you?

WALTER: (vaguely) Things close in . . .

MRS. MITTY: What? Did you get the what's-its-name? The puppy biscuit? What's in that box?

WALTER: Overshoes.

MRS. MITTY: Couldn't you have put them on in the store?

WALTER: (protesting weakly) I was thinking. Does it ever occur to you that I am sometimes thinking?

MRS. MITTY: I'm going to take your temperature when I get you home.

NARRATOR: They went out through the revolving doors that made a faintly derisive whistling sound when you pushed them. It was two blocks to the parking lot. At the drugstore on the corner . . .

MRS. MITTY: Wait here for me. I forgot something. I won't be a minute.

NARRATOR: She was more than a minute.

WALTER: (lighting a cigarette, he leans against the wall of the drugstore, smoking)

DAYDREAM #5

WALTER: (putting his shoulders back and his heels together, he says scornfully) To hell with the handkerchief! (takes one last drag on the cigarette and snaps it away)

NARRATOR: Then, with that faint, fleeting smile playing about his lips, he faced the firing squad; erect and motionless, proud and disdainful, Walter Mitty the Undefeated, inscrutable to the last.
```

---

## IC-2498: A Soldier’s Thoughts

- Title: A Soldier’s Thoughts
- Author (byline): Zachary Scott-Singley
- Work: Not specified
- Publisher: Mariner Books
- Publication date as stated: Oct 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2012
- Already set (do not supply): none

### Source block (context only)

```text
Author: Zachary Scott-Singley
BOOK: The Best American Nonrequired Reading 2006
ISBN: 978-0618570515
Publisher: Mariner Books
Date (Month/Year): Oct 2006
```

### Introduction (context only: never use it for content warnings)

```text
Zachary Scott-Singley was a sergeant in the 3rd Infantry Division, stationed in Tikrit, Iraq. In this selection, Zachary shares his thoughts and feelings, helping us to better understand our soldiers upon their return to civilian life.

“A Soldier’s Thoughts” from the The Best American Nonrequired Reading of 2006 by Zachary Scott-Singley.
```

### Performance text (classify this)

```text
April 29, 2005

I have a confession to make. My platoon and I have had over 192 confirmed kills during our first deployment here to Baghdad. We targeted people and then they just disappeared. Why? They were going to kill me. I had my orders and they had theirs. We were mortal enemies because we were told that we were. There are some who would tell me to not think about what I had to do, or it will drive you insane.

But I can’t help but think about it.

The enemy was men like me. Some of them were even conscripted into military service. What made them fight? Were they more scared of their leader than of us? What has become of their families? How could I forget or not think about all that I have done? Should I wash my hands of it all like Pontius Pilate? I think not.

My choices have been made, my actions irreversible. So live I will, for we were the victors, right? The ones who survived. It is our victory, and our burden to carry, and I bear it with pride and with the greatest of remorse. Do you think that there is a special place in hell for people like me? Or will God judge me to have been a man of honor and duty?

When they told us how many we had killed my first thought was pride. Pride for such a high number. How does one feel pride for killing? Two years later and my thoughts are changed, transformed if you will. Those were just numbers so long ago when I first heard them. Now, however, I know that they were men with families like mine. It is crazy that we humans can be so destructive. There are people out there lining up to become martyrs, to kill themselves in order to kill others, and yet you still have people who fight tooth and nail to live for just one more minute longer. We are an oxymoron, humanity that is. What makes someone look down the sights of a rifle to take aim on a fellow human being? What does it take to pull the trigger? I have done those things. I have done them and would do it again if it meant returning to my wife and children again. Some of you may think that I am a beast and you are probably right. I am. I will kill, I will take aim and fire, I will call fire upon you from afar with rockets and bombs or anything I can get my hands on if it means that I will see my family one more time.

But I will also choose to dwell on and live with my choices. I chose to enlist as a soldier. My time has been served and now it is becoming overtime, but I won’t just run away. As much as I would love to just be done (and rightly so now that I have been involuntarily extended). One thing is all I ask of you. I ask that you not judge me. Let me be my own judge, for my judgment is harsher than any you could give me anyway. For I will always have those memories to remind me of what I have done and what I am. Please know that I pray for peace every day, that and to see my family again.

May 4, 2005

It was still dark. I got dressed in that darkness and got in the truck. I was going to go line the truck up in preparation for the raid we were about to go on. The targets were three houses where RPG attacks had come from a few days prior. Sitting there in that darkness listening to the briefing on how we were to execute the mission, I let my mind wander and said a prayer. “Just one more day, God, let me live one more day.” It was the same prayer I said every day because every day I did the same thing. I left the base. With a small team I would go out each day on different missions. I was their translator.

There were different people to meet each day. There were some who would kill you if they could. They would look at you and you could see the hate in their eyes. I also met with people who would have given me everything they owned. People that were so thankful to us because we had rid them of Saddam.

The raid began without a hitch. I was talking to an Iraqi woman, checking to see if her story correlated with what the detained men had said. I heard gunfire. It was automatic gunfire. I saw a soldier amongst the others who was still aiming his M249 at a black truck off in the distance. His was the weapon I had heard.

I ran up near his position and overheard the captain asking why this soldier had opened fire. The soldier said he was sure he had seen a man holding an AK-47 in the back of the black truck.

I was among the four selected to go and see what was up with that truck.

We were out of breath when we got there. There was a group of four Iraqis walking toward us from the truck. They were carrying a body. When I saw this I ran forward and began to speak in Arabic to the man holding the body, but I couldn’t say a word.

There in the arms of one of the men I saw a small boy (no more than three years old). His head was cocked back at the wrong angle and there was blood. So much blood. How could all that blood be from that small boy? I heard crying too. All of the Iraqi men standing there were crying and sobbing and asking me WHY? Someone behind me started screaming for a medic. It was the young soldier who had fired his weapon. He screamed and screamed for a medic until his voice was hoarse and a medic came to tell us what I already knew. The boy was dead. I was so numb.

I stood there looking at that little child, someone’s child (just like mine), and seeing how red the clean white shirt of the man holding the boy was turning. It was then that I realized that I had been speaking to them, speaking in a voice that sounded so very far away. I heard my voice telling them (in Arabic) how sorry we were. My mouth was saying this but all my mind could focus on was the hole in the child’s head. The white shirt covered in bright red blood. Every color was so bright.

I can still see it all to this very day. The raid was over, there were no weapons to be found, and we had accomplished nothing except killing a child of some unknowing mother. Not wanting to leave yet, I stayed as long as I could, talking to the man holding the child. I couldn’t leave because I needed to know who they were. I wanted to remember. The man was the brother of the child’s father. He was the boy’s uncle, and he was watching him for his father who had gone to the market. They were carpenters and the soldier who had fired upon the truck had seen someone holding a piece of wood and standing in the truck bed.

Before I left to go back to our base I saw the young soldier who had killed the boy. His eyes were unfocused and he was just standing there, staring off into the distance. My hand went to my canteen and I took a drink of water. That soldier looked so lost, so I offered him a drink from my canteen. In a hoarse voice he quietly thanked me and then gave me such a thankful look, like I had given him gold.

Later that day those of us who had been selected to go inspect the black truck were filling reports out about what we had witnessed for the investigation. The captain who had led the raid entered the room we were in and you could see that he was angry. He said, “Well this is just great! Now we have to go and give that family bags of money to shut them up.” I wanted to kill him. I sat there trembling with my rage. Some family had just lost their beautiful baby boy and this man, this COMMISSIONED OFFICER in the United States Army is worried about trying to pay off the family’s grief and sorrow. He must not have been a father, otherwise he would know that money doesn’t even come close. . . .I wanted to use my bare hands to kill him, but instead I just sat there and waited until the investigating officer called me into his office.

To this day I still think about that raid, that family, that boy. I wonder if they are making attacks on us now. I would be. If someone took the life of my son or my daughter nothing other than my own death would stop me from killing that person. I still cry too. I cry when the memory hits me. I cry when I think of how very far away I am from my family who needs me. I am not there just like the boy’s father wasn’t there. I pray every day for my family’s safety and just that I was with them. I have served my time, I have my nightmares, I have enough blood on my hands.

June 17, 2005

I can’t stop thinking about what a major said to me the other day: “The whole country of Iraq, every man, woman, and child . . . Kill every one of them and it still won’t be worth one American’s life.”

So often I hear, “I’m gonna go shoot me some Hajji.” The soldiers who say these things speak as if the Iraqi people were some kind of animal to be hunted, but if you look at the statistics most of those killed are civilians not foreign fighters.

There are things like the value of a human life or the value of an entire nation that has been kicked so many times by tyrants that it may look downtrodden and useless but under it all there is the beauty of LIFE.

October 27, 2005

What is the human condition? Here in Iraq we fight terrorists and insurgents. We give them names (hajji, towelhead, raghead) to peel away their humanity. We focus only on the horrible things that have happened so that we can bring ourselves to kill, but in doing so we too become changed. No longer do we fit in when we get home. We become outsiders and misfits amongst our own families and distance ourselves as others too distance themselves from us.

You can’t let others know the things you have done because they would never understand and it would only serve to make us even more alone.

We must build as well. Walls are our specialty, so we build them thick and high around ourselves. These walls shut out all the pain and hurt we feel when others can’t seem to understand why we are the way we are, or when they judge and condemn us as if they were God himself. These walls don’t just keep those things out, but they serve to keep so much in as well. All of it, the guilt, the pain, and the fears we have can be kept deep inside where nobody will have to see them except ourselves.

That is OK though, because from there we can learn one last and important skill, that of the beast tamer. We learn tricks to keep the beast inside so that nobody will ever have to see how much of a monster we have become. In doing so we can continue our walk through life. That is the soldier’s cost of war, and it is ours to bear alone until the end.
```

---

## IC-2499: Spilt Milk

- Title: Spilt Milk
- Author (byline): Tim Miller
- Work: Extreme Exposure
- Publisher: Theatre Communications Group
- Publication date as stated: March 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1989
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tim Miller
Book: Extreme Exposure
ISBN: 978-1559361552
Publisher: Theatre Communications Group
Date (Month/Year): March 2000
```

### Introduction (context only: never use it for content warnings)

```text
Harvey Bernard Milk was the first openly gay man to be elected to public office in the United States (and only the second open homosexual, after Massachusetts State Assembly member Elaine Noble). Milk's tenure in office was tragically short-lived. On November 27, 1978, after serving on the San Francisco Board of Supervisors for only 11 months, Milk and San Francisco Mayor George Moscone were assassinated by Dan White, a disgruntled former Supervisor who had resigned in opposition to the recent passage of Milk's only significant piece of legislation, a landmark gay rights ordinance.

White crawled in through a basement window at City Hall to avoid the metal detectors; he walked into the Mayor's office and shot Moscone at point-blank range; then he reloaded his gun and walked down the corridor to kill Milk.

For young gay men, San Francisco in the 1970’s represented a hope of a new freedom, due in large part to the political contribution of Harvey Milk. This autobiographical excerpt from Tim Miller’s Spilt Milk paints a picture of the time that was the 70’s in San Francisco.
```

### Performance text (classify this)

```text
I was hitchhiking to San Francisco. I had started out from Bakersfield first thing in the California, springtime morning, hitch-hopping with several short rides up Highway 99. My thumb had been out on the on-ramps of San Fernando, on the on-ramps of Delano, on the on-ramps of Fresno and a long wait on the on-ramps of dreary Merced, too.

And now my thumb was out on a postnuclear-looking stretch of Modesto. I walked backward along the freeway on-ramp, smiling in my best "I'm-not-a-serial-killer-and-I-hope-neither-are-you" manner. My thumb was out. My body was young. My heart was pure. I was emotionally completely tucked-up, and I needed a ride pronto.

I was going to San Francisco for a few days. I was nineteen. As late seventies, Southern California, punk-rock kid, I had missed out on the hippie/antiwar/cultural revolution by about ten years, but I felt the weight of the previous generation's nostalgia as heavy as a truckload of Woodstock albums on my skinny chest.

But important things seemed to be happening up in San Francisco. There was this new mayor named Moscone, a good guy. Also, this fellow named Harvey Milk had gotten elected a few months before to citywide office. He was gay like me. It was a revolution, a better world trying to be born. El Dorado. The Grail. The perfectible social order. So, I was on my way to check it out and offer my assistance. I had an address of a friend of a friend of a friend-and twelve dollars in my pocket. I was not nearly as smart as I thought I was, but at least I was starting to realize that.

My thumb was out. Three cars whooshed past without slowing down, not even bothering to glance in their rearview mirror.

Maybe this '74 Vega will stop? Whoosh. Nope! Perhaps this '72 Ford Capri? Whoosh. Nope again!

Finally, I heard the crackle of rubber on gravel as a canary yellow Pinto eased its way onto the shoulder. Two hours later I found myself in San Francisco at Powell and Market streets, a comer which reminded me of so many cheap family vacations to the Bay Area.

I am not that kid with my family anymore. I repeated to myself this mantra as I hoisted my backpack to my shoulders. I am a self-motivated, young gay man who has escaped from his family. I am on a hero's journey to find immediately a cute boy or the ideal political system. I am a self-motivated, young gay man. . .

"Hello," the girl said. "We're from the Creative Community Project, a progressive forward-looking communal organization working toward a new world order. Please join us for a delicious free meal on our bus as we travel to our utopian farm. My name is Jennie. What's yours?"

Her offer did sound pretty good to me. I had been hitchhiking for sixteen hours and had only twelve dollars in my pocket. The offer from these seemingly friendly folk of a ride on a bus with free food was pretty tempting. Also, wasn't this the kind of thing that's supposed to happen your first ten minutes in San Francisco?

I made a decision. "Sure. I'll come with you." I got on the bus with this group of odd, smiling people.

"All aboard for utopia!" the bus driver cackled, pounding the clutch as he forced the beat-up gears to mesh. The doors hissed closed as we drove down Market Street.

On the bus, there was a buffet spread out at the back with some very strange food. The dishes all seemed to be made with broccoli as the main ingredient. In fact, everything was made with wilted broccoli, the kind that you might find tossed in a Dumpster at the back of a supermarket. The million little nubs on the broccoli were all droopy and yellow. There were wilted broccoli muffins. Wilted broccoli sandwiches. Wilted broccoli casserole. Wilted broccoli danish! What did all this wilted broccoli mean?

As the lights of San Francisco faded behind us, I grew skeptical. I found anew mantra: This is a progressive forward-looking communal organization working toward a new world order! This is a progressive forward. . .

Three hours later the bus creaked and grinded over a dirt road a hundred and fifty miles north of San Francisco to what my hosts referred to as their "utopian farm." Rubbing a bad dream from my eyes, I staggered off the bus and found myself in a new nightmare. I had a flash for a panicked moment of barking dogs and German accents in the floodlight-illuminated parking area. Emergency mantra: This is not Dachau. This is not Dachau. This is not. . .

Immediately after breakfast the next morning the elders in charge gathered us in a circle in a meadow. I was then tortured with several hours of indoctrination, calisthenics and camp songs. During one lecture there was this heavyset guy at a blackboard drawing incomprehensible diagrams as he tried to explain to us everything we needed to know: the function of good and bad in the universe. The ultimate evil of Communism. How man and woman could be happy and complete only through the union of heterosexual marriage.

I finally lost it during one of our many exercise breaks. We were coerced out onto the playing field for a set of volleyball. I had definitely had enough. I broke away from the game and approached the smiling scorekeeper. "Look, time out," I sputtered out my words. "I don't think I'm cut out to be a member of a cult. I have an appointment with someone in the Haight in just two hours, so could you please get me my backpack and sleeping bag and then drive me back to San Francisco?"

There was complete silence on the volleyball court. A skinny member of the staff ran off toward the main building. A siren began to wail in the distance. The dogs were let loose. I pulled away as the Boonville camp staff surrounded me, backing me against a California oak. I imagined they all were hiding something behind their backs. As my breath raced, I saw that the staffers all carried. . . heads of broccoli. I was locked in a battle with the attack of the Broccoli Brain Suckers!

"Back!" I shouted, "I am the Antichrist. I am a Communist. I am GAY!" (What else can I say to scare them away?) "Get me my backpack and sleeping bag now, or I'll call the police!"

Well, that did the trick. About one second later the camp bouncers dumped me and my backpack out on the dirt road. I was breathing fast. I looked around. The world was still there. I had managed to escape from the bizarre clutches of the broccoli brain snatchers.

Scared, shaking but breathing, I braced myself for my second day in San Francisco.

I wandered around North Beach, the direct-from-central-casting fog wisping around my ankles. I felt depressed. Disillusioned. What had I expected? What did I want?

I thought going to the beach might restore me. I got on a bus and I went out to Land's End. It was unbearably beautiful there. Climbing over one razor-sharp rock, I suddenly saw a vision: a sinewy, young man with curly, long, brown hair was dipping his foot in the ice-cube-cold sea. He looked directly at me and smiled. I almost fainted. I jumped in the water and strode toward this man through the icy surf.

"Hey! Isn't the water cold?" he shouted to me.

"I . . . urn . . . oh!" I sounded like an idiot. I looked at this guy through my dangling water-soaked curls. He was so confident, so sure of himself. How did he get like that?

He pulled me out of the surf. "I'm Michael."

"I'm-m-m-m-m Tim."

"Would you like to come to my house tonight?" Michael asked. "I live in a small, socialist gay men's commune in the Mission. We compost and everything. Well, we're having a meal tonight. A few of us are thinking about going to Cuba as part of the Venceremos Brigade to help bring in the sugarcane harvest and defeat the imperialist U.S. embargo. Would you like to join us?"

"I'd love to."

Since we didn't have any paper, Michael neatly printed his phone number on the inside of my arm with the same fluorescent green highlighter. "There," he said as he capped the pen. "Now you won't lose me."

Weaving my future with Michael, I drifted into a sun-baked sleep. I imagined our dinner that night. There will be a brood of dynamic, leftist gay men in attendance. We will eat a delicious ovo-vegetarian meal that Michael and I will prepare. I'll commit to going to Cuba with them. "Venceremos! We shall be victorious!" we will all shout. At the right moment Michael will invite me into his bedroom to listen to his album of whale songs. The tide came in and woke me up.

Two hours later I was walking in downtown San Francisco killing time before my date. Carefully checking the bright green numbers marked on my arm, I called Michael to get directions to his house in the Mission District.

"Hi, Michael. It's me, Tim, the guy you met at Land's End."

"What shall I make for us to eat?" Michael asked. "Do you like broccoli?"

"Sure," I said with a gulp. "I love broccoli."

I hung up resigned to yet another dinner of broccoli. I made a detour on Fulton Street so I could see City Hall before I went to Michael's flat. I wanted to check out the building where Harvey Milk was chang-ing the world. Well, at least my world. Finally, I arrived at City Hall and I looked at the vaulted dome high above me. I thought to myself, Why is this building so huge? Is it because there is a big idea inside? It looks like it could be the Capitol of an empire or something, not just a City Hall.

I looked at the huge building and I felt a huge joy. There I was, a foolish, young man. I felt the wheels of the state apparatus, for once, grinding begrudgingly in concert with me. There was a guy named Harvey Milk, gay like me, inside City Hall tickling the power that be! I felt so strong. I felt for once that the world was not an enemy, that society was perfectible.

My body was in front of City Hall. I could feel my skin, my feelings, my hopes for the future as tangible as the sidewalk under my feet. For once the law and the government would not pull the rug out from under me. I had all these powerful feelings and a date for dinner with Michael, too.

As I walked away from City Hall, I thought to myself, Well, I guess I'll have to go back to Whittier pretty soon. I only have three dollars left. Maybe I won't go to New York. I want to come back to San Francisco and make a life in this city someday. But, for now, I went off to my broccoli.

A few months later, I was working another soul-killing job at a gas station, trying to make ends meet. As I pumped gas into an old man's Buick, I overheard two other people in a pickup truck having this conversation.

"Hey, d'ya hear the news?" this obvious jerk in the truck slurred through his open door. "They got those two guys up in Frisco. Yeah, some ex-cop killed that queer Milk and that mayor of theirs, whashizname, Macaroni?"

I dropped the gas nozzle to my side. I knew it was time to leave California. I was covered in gasoline.
```

---

## IC-2500: Strong Arms

- Title: Strong Arms
- Author (byline): Albert Lujan
- Work: Virgins, Guerrillas & Locas
- Publisher: Cleis Press
- Publication date as stated: Oct 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1524
- Already set (do not supply): none

### Source block (context only)

```text
Author: Albert Lujan
Book: Virgins, Guerrillas & Locas
ISBN: 978-1573440875
Publisher: Cleis Press
Date(Month/Year): Oct 1999
```

### Introduction (context only: never use it for content warnings)

```text
Toys have always played an important role in enriching children's lives. They often reflect the culture of the times and are an indicator of historical changes and trends in society. Although today's toys may seem very different from those of years past, the purpose of toys has always been the same: to bring laughter and joy, and to create opportunities for learning and developmental growth. Maybe you can remember the power of the first toy you fell in love with. . . Strong Arms by Albert Lujan.
```

### Performance text (classify this)

```text
At the age of six I declared my love, my desire, my utter need out loud, to the image on the smooth convex surface of my family’s Zenith color television console. From my seat on the tangled shag of the living room I was levitated forward by a force so magnetic that it pulled my tongue from my mouth and my eyes from their sockets, to vibrate only inches from the screen. It pulled the words from my mouth. “I want you.”

I vowed to sit there, in front of the television, until I saw again the commercial that so transfixed me; a vow that only lasted till 8:30, my bedtime. I swore I would resume my vigil at dawn. I would see it again. See him again. There, I said it. Not out loud, of course, but secretly, with conviction and desire.

Who was he? Why hadn’t I heard mention of him in the schoolyard or park? All night I thrashed these questions around, between dreaming and waking. He was on my mind when I woke up. It seemed I’d imagined him, but my dreams were so detailed that I knew, deep down, he was real.

That next morning, before school and between bites of Alpha-Bits cereal, he appeared to me again, on Channel 2.

“Mom, hurry mira lookit, hurry mira lookit! The one I told you about. Hur-ryyy!” I sprayed milk and bits through my nose across the table as I bolted for the TV. Clearly she didn’t sense the urgency in my screams. By the time she reached the living room, from the kitchen, where she wrapped a beans-and-rice burrito for my lunch, he was gone.

It was too late to pretend that I felt sick in order to spend the day in front of the TV. A successful sick act had to begin the night before or the minute she woke me up. Plan B had me rummaging through the medicine chest before breakfast for something that would have the school nurse calling home to let my mother know she was sending me home for the day. I examined the various pills of ever color and shape. I resisted eating the Hershey-imitation Ex-Lax. I tried that the day Luke and Laura were scheduled to be married on General Hospital. It worked, only I spent the whole day on the toilet and missed it all. I pushed the children’s multi vitamins off to the side and selected the bottle with the baby-blue colored pills in it. The label read “Midol.” I popped the top and poured three into my pocket. After all, I wasn’t suicidal, I was in love.

On the walk to school I ate the pills from my pocket. I tasted the chalky bitterness and gagged. I silently beckoned to Him. I mouth His name. Called it out. Even chanted it. Armstrong. Mr. Stretch Armstrong from Hasbro. Hasbro – where was that magical country? I wondered. Strong arms. Yes, clearly he was very strong. Buff like the Tasmanian Devil but in complete control. Stronger than any Tonka truck I’d ever owned and destroyed. He had powerful arms with shoulders out to there and legs so muscular it was clear he would never be able to cross them like a girl, even if he wanted to. He had a Bob’s Big Boy soft-serve chocolate ice cream flip going on. Sexy, of course, but in a manly way. Painfully blue eyes. He held a sensual half-grin/half-snarl that said, “I’ll be your special friend, but don’t [mess] with me ‘cuz I could still kill you with my hands if I have to.”

Stretch was quite confident too. Proud of his hard-earned physique. All he ever ran around in was a pair of Speedos. Red. They looked like they were painted on. He was the color of Band-Aids. G.I. Joe and that old sissy, Ken, were obviously ashamed of their scrawny bodies. I was quite disappointed in them, considering how hard it was to get their clothes off.

At school I couldn’t concentrate. I felt kind of lightheaded and kept needing to pee. At my desk I misspelled his name over and over again on my H.R. Puffinstuff notebook. If I got him for Christmas I would never mistreat him. If I got him for my birthday I would cuddle him. Rest him on my chest like some mini-manchild. Feed him mini-muscle bars so that he could have the strength to put Ken in a headlock.

At lunchtime, after I threw away my burrito, I stood in line in the cafeteria holding my bile-yellow fiberglass tray loaded with bile-yellow food. The guy in front of me, this gangly third grader, kept reaching around, checking the contents of his book bag with one hand and trying to balance the tray with the other. It was as if he were afraid some bully was gonna steal his math book or something. Or someone. I saw it. From the edge of the book bag flap I saw it protruding like some obscene, pink udder. Like and arm. A strong arm.

Oh my God. Only one day after the commercial aired for the first time. How hard did he have to whine to get him so soon? And he had the nerve to bring Stretch to school with him. Nine months ‘til Christmas, ten ‘til my birthday. It just wasn’t fair.

By the time we reached the milk I was hyperventilating. I was so enraged and jealous that I started gagging. Everyone around me was going “eeiiuu” and moving away. I instantly reacted. I jerked forward, snatched Stretch from the backpack, dropped him onto my tray, pulled my tray to my chest, and spilled creamed-corn and fruit cocktail on myself. Still I held him tight next to my thumping heart and obscured him. I was delirious and a little nauseous. The little punk out a scream.

The Lord works in a mysterious ways, ‘cuz all of a sudden projectile vomit sprayed from my smiling face. I was wild. Kids ran in all direction. Like a far-reaching sprinkler, I caught most of them on their pants legs. Everyone screamed. It was pandemonium. They cleared out a wide-open get-away path and I took it, laughing, gurgling, almost drowning in my barf, clutching the tray to my chest. I was halfway out the cafeteria before I heard the third grader scream, “Hey, puke-boy’s got my doll!”

Doll? Is that all he thought Stretch was? Some toy to stuff into a chest like some old deflated Hoppity-Hop? I thought not. He really didn’t deserve him. I ducked in the teachers’ restroom. The ladies’. Jumped into a stall. “Oh, Stretch,” I murmured. “But they’re coming for us. They’ll want to take you from me.” There was nowhere to hide him. He didn’t fit in my pockets. I tried to stuff him into my pants and that was kinda nice but really obvious. I could hear them outside. They had followed the trail of puke and food. “You’re mine, Stretch, forever. No matter what,” I vowed.

I pulled the packet that contained the napkin, straw, and ‘spork’ that had stuck to my shirt. “Before they take you from me, my love, we must take the blood oath.” Yes, I was a bit melodramatic for six years old. I slashed the back of my hand with the spork, but getting through Stretch’s skin was a little harder. It took a couple of hard jabs with my pencil to finally puncture the tough hide on his arm.

I put my bleeding hand to his face. I held him over my face and squeezed out his pink, gummy insides, which dangled sensuously and thick like melted mozzarella. I put my mouth over his whole arm and sucked it. Like it was my thumb. I sucked his insides into me. It tasted like Ponds cold cream and paste. Tears ran down my face. I sucked until I passed out.

I woke up in the hospital. His nontoxic goop lined my insides and blocked my air passage. A 125-year-old nurse told me that I had turned blue, “…just like a Smurf.” I had to have my stomach pumped.

At the hospital my parents, and some relatives whom I only saw on Easter and Christmas, watched me nervously, praying the rosary over me and pulling my arm with the I.V. in it to make the sign of the cross. They lavished on me welcomed kisses, Spanish comic books I couldn’t figure out, and a Lite-Brite set with a note taped to the top of it that read, “Do not swallow the pegs! They are not JUJU-BEES!” I had a strange feeling that from then on everybody would be watching what I ate very closely.

That night I fell asleep with the soft, colorfully glowing Lite-Brite set clutched to my chest. On it was the first message I wrote. My first love letter: “I ‘heart’ S.A. 4- ever.”
```

---

## IC-2501: Stuck in Neutral

- Title: Stuck in Neutral
- Author (byline): Terry Trueman
- Work: Not specified
- Publisher: Harper Tempest
- Publication date as stated: Oct 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SHAWN’S INNER VOICE, SHAWN’S VOICE IMPACTED BY CP, ALLY, MOM, DAD, GUY
- Teaser before the introduction: Yes
- Spoken words (computed): 1004
- Already set (do not supply): none

### Source block (context only)

```text
Author: Terry Trueman
ISBN: 978-0060285197
Publisher: Harper Tempest
Date (Month/Year): Oct 2001
```

### Introduction (context only: never use it for content warnings)

```text
Shawn McDaniel is an enigma and a miracle--except no one knows it, least of all his father. His life is not what it may seem to anyone looking at him. Not even those who love him best have any idea what he is truly like. Today, I personally challenge you to look beyond the obvious and truly see a person whose spirit is rich beyond imagining and whose story is unforgettable.

Stuck in Neutral by Terry Trueman
```

### Performance text (classify this)

```text
SHAWN’S INNER VOICE: My name is Shawn McDaniel. My life is like one of those "good news—bad news" jokes. Like, "I’ve got some good news and some bad news– which do you wanna hear first?" In the jokes, it’s always the good news first, so here goes: my mom and dad love me!

I could go on about my good news for hours, but you probably want to hear the punch line, my bad news, right? This bad news is complicated, difficult to explain. In a nutshell, it's that I am pretty sure that my dad is planning to kill me. The good news is that he'd be doing this out of his love for me. The bad news is that whatever the wonderfulness of his motives, I'll be dead.

SHAWN’S INNER VOICE: Every year the school district sends out a school psychologist (scientist) to test me -- mainly intelligence tests filled with questions like "Who was George Washington?" and "What’s two plus one?" And every year I sit there and miss every question. Then the shrink goes in and gives my mom a number: I.Q. = 1.2, or mental age 3 to 4 (that’s months, not years).

(Transition into the vocal qualities and mannerisms of someone with CP)

SHAWN’S VOICE IMPACTED BY CP: The deal is, I have cerebral palsy. I can't control any of my muscles: not my fingers, my eyes, [my voice] . . . none of them. Not a one. So when the psychologist says, "Who was George Washington?" I can't tell him what I know. All I can do is sit there and drool if my drool function is running, or go, "ahhhhhh!"

(Transition back to regular mannerisms and speech)

SHAWN’S INNER VOICE: When people first meet me, they usually speak real slowly and real loudly:

ALLY: Hi Shawn, nice to meet you! My name is Ally Williamson! How are you!

(Transition into the vocal qualities and mannerisms of someone with CP)

SHAWN’S VOICE IMPACTED BY CP: Well, I’m not deaf! (Beat) Oh, but it gets worse. You should see my mom!

MOM: Goo-goo-baby boy-go . . . you a big baby boy . . . boogie woogie googie snoogie.

SHAWN’S VOICE IMPACTED BY CP: It’s OK, you can laugh. I do! You know, people mean well. They just don’t always know how to show it. Like my dad.

(Transition back to regular mannerisms and speech)

SHAWN’S INNER VOICE: I guess I should explain about my father, about why I think he's planning to kill me. It's not as though he's stated it directly. It's more an intuition -- intuition and a thing that happened last week when my dad stopped by the house.

DAD: How're you doing, big boy? Everything going okay for you? Any hot news for me? (Laughs)

SHAWN’S INNER VOICE: He laughed at his joke, not a big or happy or mean laugh, but a quiet, sad one. Then he leaned over in front of me and brought his face down close to mine. With his brown eyes only inches away from my eyes, it felt as though he were trying to stare through me, straight through my eyes and into my brain.

DAD: (softly) You're not getting any of this, are you, Shawn?

(Transition into the vocal qualities and mannerisms of someone with CP)

SHAWN’S VOICE IMPACTED BY CP: In fourteen years I've heard him say my name aloud in my presence a total of sixteen times.

DAD: God . . . look what he did to you! You can’t even protect yourself, Shawn. I can’t protect you, or your mom or anyone else. You know I love you, right? When I think about you, Shawn, my heart breaks. When I think about you hurting, I can barely even breathe, my chest aches so badly. I want to help you, Shawn, I do.

But I just don’t know how. Am I supposed to let all your pain and your seizures continue, or should I just end it. Is that what you want, Shawn – you want me to end your pain?

SHAWN’S INNER VOICE: No, I don’t want that! End my pain? It made me mad. What right does he have to decide what's best for me? What right does he have to think about ending my pain? . . . You see, I know he loves me, but when he looks at me all he sees . . .

(Transition into the vocal qualities and mannerisms of someone with CP)

SHAWN’S VOICE IMPACTED BY CP: . . . is this twisted, drooling pile of flesh. (Beat) What do you see? You know, it’s just a shock to me. There’s an actual person inside here who wants to be seen and loved, but of course, I can’t tell him. He can’t hear me. You see, he can only remember what happened.

(Transition back to regular mannerisms and speech)

SHAWN’S INNER VOICE: One day I was out on our front porch sitting in my wheelchair, when this guy showed up . . .

GUY: Hey! You know if the bus has come by or not? Hey!

You there, Roller Derby, has the bus come by or not?

(Transition into the vocal qualities and mannerisms of someone with CP)

SHAWN’S VOICE IMPACTED BY CP: Ahhhhhh!

GUY: Are you laughing at me, huh? Did I say something funny. Look at me when I’m talking to you. Did I say something funny? Maybe I should teach you some respect, huh?

SHAWN’S VOICE IMPACTED BY CP: Then he held a lighter under my chin.

GUY: Not’s so funny now, huh?

SHAWN’S VOICE IMPACTED BY CP: Ahhhhhh!

(Transition back to regular mannerisms and speech)

SHAWN’S INNER VOICE: Do you know what it’s like to smell your own flesh burning and not be able to do anything about it? He burned a hole under my chin and I couldn’t even stop him. When my dad came out, he freaked. Without a word the stranger scurried out our open gate. In ten seconds he was gone. We never saw him again.

(Transition into the vocal qualities and mannerisms of someone with CP)

SHAWN’S VOICE IMPACTED BY CP: So now I have to worry about what my dad is going to do to me. Is my father going to kill me? When? How? What's going to happen?

DAD: When you were born, and we were told that you'd have these kinds of problems, I got down on my knees and prayed harder than I'd ever prayed, begging God or Satan, or anybody in between, to let me trade places with you. I prayed, night after night, that I could be the one trapped inside your body and that you could take my place. I don't know what to do, son. Shawn . . . I love you.

(Transition back to regular mannerisms and speech)

SHAWN’S INNER VOICE: You know, I just wish for one moment that I could have complete control over my body. Just for 2 minutes. So I could tell my dad that I love him and I could cuddle with my mom. So I could tell her that I love her and tell my dad that I AM happy and that his unconditional love . . .

(Transition into the vocal qualities and mannerisms of someone with CP)

SHAWN’S VOICE IMPACTED BY CP: . . . is everything I need. And that I’m just sorta stuck in neutral.
```

---

## IC-2502: Subliminal Messages

- Title: Subliminal Messages
- Author (byline): Jason Sheets
- Work: Turning Points
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1141
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
Sooner or later it happens to us all. The love of our life decides it's just not going to work out and takes off, leaving us feeling shattered, unlovable, abandoned, and very much alone. When it happens to you, you may believe your life can never again be the same. The pain is excruciating as are the memories. Subliminal Message by Jason Sheets
```

### Performance text (classify this)

```text
I keep trying to rationalize all that has happened, yet in the end all I can surmise is that it is over. Summer leaves, autumn falls, and winter is nature's way of saying “screw you,” whisking everything away and making it appear as if nothing ever happened. I'm still not sure what did happen. I will remember the Rachel I fell in love with. I will remember our relationship in the way I had always hoped it would be. I will believe that she remembers as well. I reached out for happiness in the only way I knew how and it was within my grasp. I think. I choose to believe that.

For as long as I can remember, I have not been a memorable person. I don't think people disliked me; I just don't think they noticed me. That is until I met Rachel. When we were fourteen, our science teachers made us lab partners and somehow, maybe because she needed help in science, she noticed me. We started talking after class and meeting after school and soon enough we were friends. Now, for a fourteen year old boy, having a girl for a best friend can be a traumatic experience. Trust me. I know. It wasn't like we sat around playing dolls or anything. This was a mature relationship. We just talked-hung out, you know. We listened to each other.

After we graduated, Rachel and I still wrote. Not a lot. OK - I wrote more, but she wrote back. I want to believe she really thought about me when she wrote, the way I always thought about her when I wrote to her. I want to think she got married because she had to, she got pregnant; her father arranged it, something. I need to believe that she still remembered what we meant to each other.

I had always wanted more than friendship from Rachel, but I never planned on telling her. That is until Rob decided to stick his big nose in the middle of it. I am sure everyone has a friend like Rob: the one person who manages to squash your dreams while he is stepping into your life to "help out." Rob was the one who finally told Rachel the whole story. I don't know why she reacted the way she did. I expected her to laugh, to tell her husband, maybe look up my picture in the yearbook, but never, never did I expect her to call. I never expected her to ask me out.

The first date was magic. As strange as it seemed at the time, she never brought up Rob, never brought up her husband, and never stopped smiling. We talked. We danced. We reminisced. We listened to each other wonder about where our lives were headed. And then she kissed me. Fifteen years, I had been in love with the same woman, she had gotten married, I'd gotten lost, and for the first time since eighth grade science, we kissed. Holding her hand, her fingers hidden in my palm, I thought to myself that only a deeply crazy person would get involved with a married woman.

Oh, I was crazy. We began to meet two or three times a week. We never talked about it. We really didn't talk much. It was as if we had to spend each minute we had grasping for what we'd missed before: the years. Mostly, we never said a word. I'd pick her up at her office. We'd go back to my place. We'd make dinner. Make love. Make coffee. Sometimes she'd cry. Quietly. Then she'd ask me to take her home. I would drop her off at the corner of the block she lives on and watch her walk back home to her husband.

In the supermarket, about a month after we started the affair, I ran into Rachel- shopping with her husband. I'd never met him before, but there he was. At first, I thought I could duck into the canned goods aisle. Hide behind a Coca Cola display. But her husband caught me staring at Rachel. I smiled, looked at Rachel like I hadn't seen her since high school, and I introduced myself to her husband. And I realized, partially, as Rachel stared intensely at the spaghetti sauce, that she had never mentioned me before. She'd never told her husband about us growing up together. About dissecting frogs in eighth grade. About cheating in Junior French. About prom. About the letters we had written. I mean, this man had no clue who I was. And I was having an affair with his wife. Three times a week and twice on Saturday. Yet, Rachel had not even mentioned my name in passing.

The next day my crisis began. It came in the form of a note that was slipped under the door like a piece of junk mail. I recognized Rachel's handwriting immediately. The note answered questions that I had always wondered about but never really wanted answered. She told me that she was leaving her husband. She was accepting a job in Tennessee and she did not want to see me anymore. She did not tell me where she was going or how to find her.

I dropped the note and I called her office, but they just told me she had quit. My palms were starting to get wet. I tried to punch in the numbers of her home phone, but my finger...my finger kept slipping...slipping on the number three. Her number has three three's in a row and I couldn't get my fingers to press the numbers correctly. So I kept trying, and trying, and trying, and finally I just dropped the phone and I lost it. I don't know. The phone witch kept rambling on about hanging up and dialing again. Hang up. Dial again.

Sort of struck me as funny. Like I didn't even have an effect on anyone. The recording didn't care if l was there or not. She would keep rambling on in her smoothly corrosive voice. And I wondered if Rachel had told her husband about me before she left. I wondered what she was thinking as she studied the spaghetti jars while I introduced myself.

Now, I spend a great deal of my time writing. I write like this. I write poems. I write letters. Mostly, I write letters to Rachel. I never send them because I wouldn't know where to send them to, but I ask her a lot of questions. I have not asked her if she loved me. I haven't asked her to remember me. These two things I will wait on. I will wait until she writes me. Until then, I am going to assume that she did. I am going to assume that she will.
```

---

## IC-2503: Suzanne’s Diary for Nicholas

- Title: Suzanne’s Diary for Nicholas
- Author (byline): James Patterson
- Work: Not specified
- Publisher: Warner Books, Inc
- Publication date as stated: (Month/Year): July 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1219
- Already set (do not supply): none

### Source block (context only)

```text
Author: James Patterson
ISBN: 978-0446611084
Publisher: Warner Books, Inc
Date: (Month/Year): July 2003
```

### Introduction (context only: never use it for content warnings)

```text
Many families keep a journal of special events that occur in the lives of their child: A special book of memories . . . a tradition. In this selection we find Nicholas’ father, Matthew logging his own personal entries in Suzanne’s Diary to Nicholas by James Patterson
```

### Performance text (classify this)

```text
Hello, my sweet Nicholas, it’s Dada.

Have I told you how much I love you? Have I told you how precious you are to me? There---now I have. You are the best little boy, the best anyone could ever hope for. I love you so much.

Yesterday morning something happened. And that’s why I’m writing to you today instead of Mommy.

Fathers and sons need to talk more than they do. A lot of us are so afraid to show our emotions, but I never want us to be like that.

This is so hard, Nicky. It’s the hardest thing I have ever had to say to anybody.

Mommy was going to the store to the store to pick up your birthday present, your beautiful framed pictures. She was incredibly happy. She looked so pretty, deeply tanned and toned from all her walks on the beach. I remember seeing her leave, and I can’t get that image out of my mind.

Suzanne had such a beautiful smile on her face. She was dressed in a yellow jumper and gauzy white blouse. Her blond hair was full of curls and swung with her body as she walked. She was humming your song, “Whistle a Happy Tune.”

I should have gone to her, should have kissed Suzanne good-bye, should have hugged her in my arms. But I just called, “Love you,” and since her hands were full, she blew me a kiss. Oh, Nicky, Nicky, Nicky. How can I say this? How can I write these words?

Mommy had a heart attack on the way into town, sweet baby. Her heart, which was so big, so special in so many ways, could no longer hold out.

I was told that Suzanne was unconscious before she crashed into the guardrail on Old Pond Bridge Road.

Her Jeep dropped into the water, landing on its side. I haven’t gone to look at the actual scene of the accident. That is an image I don’t need inside my head. What I can see is already is too much.

Dr. Cotter says that Suzanne died instantly after the massive coronary, But who really knows about those final seconds? I hope she didn’t feel any pain. I hate to think that she did. It would be too cruel.

She was unimaginably happy the last time I saw her. She looked so pretty, Nick. Oh God, I just want to see Suzanne one more time. Is that too much to ask? Is it unreasonable? It doesn’t seem so to me.

It’s important to me that you know it wasn’t Mommy’s fault. She was such a safe driver; she would never have taken any chances. I always teased her about her driving.

She was the most generous-hearted person I have ever known, the most caring and compassionate. Maybe what I loved best about her was that she was a great, great listener. And she was funny. She would make a joke, right now. In know she would. And maybe she is. Are you smiling now, Suzanne? I’d like to think that you are I believe you must be.

I went today to the cemetery on Abel’s Hill, to choose Mommy’s special place. She was just thirty-seven when she died. How sad, how completely unthinkable to me, and to everyone else who knew her. What a shame; what a waste. Sometimes it makes me so angry.

Tonight I sit in your nursery and watch your clown lamp throw happy shadows against the walls in the half-light. The oak rocking horse I made for you reminds me of the Flying Horses Carousel. Remember when we all went there on our vacation and rode the colorful horses? Nicholas, Suzanne, and Matt.

I held you in front of me, and you loved to stroke the real horsehair mane. I can see Mommy riding ahead of us on National Velvet. She turns and there’s that famous wink of hers.

Dear, sweet Nick,

I was startled out of my thoughts and reveries this afternoon by an unexpected phone call. It was for Mommy.

Obviously someone had no idea what had happened, and for the first time, those strange and awful words passed through my lips like heavy weights: “Suzanne has passed away.”

There was a long silence on the other end, followed by quiet apologies, and then nervous condolences. I was the man from the frame shop on the other side of the island, in Chilmark Center. Mommy had never made it there, and the pictures she had framed for you were still at the store. I told the shop owner that I would come around for the photos. Somehow, I would manage to do it.

I walk aimlessly from room to room, trying desperately to find a place where I can feel at peace with myself. Somehow, I always end up back in your room, sitting in the same rocker Mommy so often did when she talked to you and read to you and recited her goofy rhymes.

And so I sit here now, looking at the pictures of us I finally picked up this afternoon. We are all sitting in front of the Flying Horses Carousel on a perfect, blue-skied afternoon.

You are wedged between us, Nick. Mommy has her arm around you and her legs crossed on mine. You’re kissing Mommy, and I’m tickling you, and everyone is laughing, and it’s just so beautiful.

Nicholas, Suzanne, and Matt----Forever One.

I pull the cord on your music box in your crib, and it begins to play “Whistle a Happy Tune.” I love this song, Nicky. I reach into the crib and I touch your sweet cheek. I tousle your golden blond hair, always so soft and fragrant. I wish I had listened to Mommy and never cut it.

I place an index finger in each of your small hands and let you squeeze. You’re so strong buddy. I listen to your beautiful laugh, and it almost makes me laugh. “Whistle a Happy Tune” continues to play.

Oh my dear, darling little boy. I remember Mommy leaving on her errand that morning. I called out “I love you,” and she blew me a kiss. Then she crinkled up her nose the way she does. You know what I mean. You know that look of hers. Then she gave me her “famous wink.”

Her arms were full, because she was carrying you, sweet baby. She wanted you to be the first to see the beautiful framed photographs. That’s why she took you with her to town on your birthday morning.

Suzanne carried you outside and carefully strapped you in your car seat. You were in the Jeep with Mommy when she crashed on the Old Pond Bridge Road. The two of you were together. I still can’t bear to think about it.

I should’ve been there, Nicholas. I should’ve been there with you and Mommy! Maybe I could have helped: maybe I could have saved you somehow. At least I could have tried, and that would have meant everything to me.

But isn’t it lucky that I knew you, held you and loved you, for the twelve months before God took you away? Isn’t it lucky that I got to know you, sweet little boy, my son?
```

---

## IC-2504: Telephone Man

- Title: Telephone Man
- Author (byline): Chris Crutcher
- Work: Athletic Shorts: Six Short Stories
- Publisher: Harper Tempest
- Publication date as stated: Nov 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2116
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
Telephone Man by Chris Crutcher
```

### Performance text (classify this)

```text
"Eccentric" is what the teachers at Oakland High School call kids they think are crazy. They use words like that so people like me won't know what they're really saying. Around this school they call me Telephone Man, which is one of the few things I like, even though I know they think I'm a dork for wearing telephone equipment strapped to my hip. But without it, I feel like how the Duke must feel when they make him check his six-shooter at the saloon door. I feel bare naked.

I can fix any telephone that a regular telephone man can fix. I can fix it if the people on the other end can't hear you or if you can't hear them. And if you have more than one phone in your place, I can set them up like walkie-talkies, if they have the right stuff in 'em. That's what I can do.

Sometimes I wish Hawk wouldn't of saved me from the China kids because it confuses me, and I hate that most of all. When a nigger goes saving you from Chinamen, it throws you off because everyone knows niggers are the worst. It all happened on one of those days when I just don't think. That's what my mom and dad both say: "Jack, most of the time you get into trouble because you just don't think." I got up late that day, and it looked like I would have to go to school without breakfast again. Well, Mom was still in bed and the bus was coming in about four minutes and I looked through the cupboards and I couldn't find anything except there was the Bisquick. Well, I knew that's what Mom made biscuits out of, and I figured, hey, even if they don't taste as good not cooked, they have to be just as good for you, right? I mean, your stomach doesn't know if they're cooked. Everything turns about the same temperature pretty quick down there anyway.

There wasn't any strawberry jam in the fridge, so I just ate the Bisquick right out of the box, which it was pretty dry. But then, when I was in the bathroom trying to blast off a pimple from my nose that looked about like a spaceship or something, I saw this strawberry stuff sitting on the bathtub, and I didn't know why it was there; but I did figure it was no big deal if I ate it after the biscuits because like I said before, it all ends up in the same place anyway and your stomach would never know which order you ate it in. Right?

I think it should be against the law to make soap or shampoo that smells like jam and has pictures of strawberries on the front. I mean, it was red and it was thick, and even though it didn't have clumps of strawberries in it and it tasted funny, it looked like syrup, which is close enough to jam to drink when you're in a hurry and just want to get something close to your regular breakfast in you.

Well, what went on inside me probably would of made a good science lesson, I bet. I didn't know how many biscuits you can make out of one box of Bisquick, but I found out later it's a lot. And I also didn't know what happens when you get soap inside you.

I was in history when it hit. There was this sort of rumbling inside me, and all of a sudden I knew I had to get to the bathroom really quick, so I just ran for it. I was lucky enough to get my telephone stuff off and up high out of the way, but right after I did that, I started feeling like a balloon that you just let go of the end. I wanted to save my clothes, and I got my shirt off, but my pants got stuck down around my knees right when my butt just turned into a cannon and I was shooting biscuit stuff all over the whole room.

So everything would of been okay except on my way to the bus I ran into the China kids. The China kids hang out at the top of the stairs, and if they're going to get you, that's where they do it. I saw them there, and right away I was going to go back; but our school bell rings outside and inside, and I heard it and I knew the kids would be changing classes and some of them would come outside and see me if I tried to go back the other way-and I thought they'd know what I did in the bathroom. I think people just know if you mess up sometimes, even if no one tells them. So anyway, I decided to just go ahead and pretend I didn't see the China kids and maybe they'd just let me go to the bus so I could go change my clothes.

But they didn't. The leader, he's a guy named Kam, was practicing that karate stuff, and the rest of his gang was clapping their hands and saying "way to go." They call theirselves the Jo-Boys. That's a really dumb name, and I don't get it; but I wasn't going to say anything. I just put my head down and walked around the corner to the steps, trying to make it like no one could see me. I can do that sometimes, but not this time. Somebody said, "Hey, kid!” but I just put my head down and kept walking. I tried to do it like when you're trying to get past a mean dog. My dad told me not to walk any faster or anything, just to act like I'm not there. But this kid wasn't a dog, and he said, "Hey, kid:' ~. I tried to walk faster; but somebody grabbed my shoulder, and I turned around toward him and said, "You better leave me alone," but I kept my head down.

But he said, "Well, yeah, but they are our stairs, and we have to charge you to go down 'em," and I said I don't have any money, which was a little bit of a lie because I had enough for lunch, but my dad told me to always say I don't have any.

Then the kid who talked to me first says, "What's that you got around your waist?" and I tell him it's my telephone stuff. He wants to know what it's worth, and I tell him it's not for sale; but he just laughs, and Kam tells me to take it off.

Now, I'm scared a lot of the time, and most of the time I'm afraid to talk because people just make fun of me because I have this really deep voice and these stupid zits on my nose plus it's hard to get the words in my head out so they sound right. But they want my telephone stuff, and they're just not going to get it. They're just not. I'm almost nobody anyway, but if I don't have my telephone stuff, I'm really nobody. Absolutely, completely, and all the way nobody. So I scream, "Leave me alone!" and they start laughing and kind of pushing me between each other. I grab the buckle to my telephone belt and hold on to it tight, and they push me harder, and they start sort of singing, "Leave me alone, leave me alone, leave me alone," so I scream it at them again, only louder this time, and I keep my eyes closed really tight and hold on to my belt buckle with all my might. Sometimes if I scream and scream and keep my eyes closed tight, things just get over.

Then all of a sudden everything stops, and I think maybe it worked, but I keep my eyes closed a little bit longer because sometimes that makes sure everyone goes away. Then I open them just a little and take a peek to see if it's time to get up and run yet.

But what I see is Hawk, and I know I'm done for. See, Hawk is this big nigger that goes to OMLC, and everybody knows if he's after you, you might as well buy a plot in a cemetery somewhere because he might just be the toughest guy in the world. He's never teased me before. Usually Hawk just walks up to me and says some-thing like "Telephone Man, you a kick," and he smiles and shakes his head and walks away.

But now I get it. He gets the China kids to beat me up a little, and then he comes along to finish me off. I think, so that's his nigger trick, and I roll up into a ball because now I know it won't be very long until it's all over.

But then I hear him say, "What you Jo-Boys think you doin' here?" and there's no answer. Then Hawk says, "This here’s Telephone Man. Friend of mine," and still there's no answer. "How many time I gotta tell you China boys don' go be messin' with my friends?"

Kam starts breathing big and kind of crouching like an animal; but right before you know it, Hawk's got him down on the ground, and he doesn't get to use any of his karate stuff because Hawk's choking him right to death. The China kid's eyes are so big they're about ready to explode, and Hawk's only using one hand, 'cause he's looking at all these other China guys, who must be thinking they should jump on his back and help out their friend. But nobody does it; they just stand there and Hawk says, "Come on. I be closin' off you number one Jo-Boy air-hole for him; then I take anybody else want some," and still nobody moves. Then Hawk turns back to Kam and says, "Gonna let you up, China boy. Nice an' slow. You try any you Bruce Lee stuff, gonna embarrass you, front you friends," and he lets a little bit loose.

Kam gets up kind of slow, and when he's about halfway, Hawk grabs him by his cheeks between his fingers and makes him look at me. "You see that boy?" he says. "Got all kinda telephone stuff on him?" Kam doesn't say anything, so Hawk moves his head up and down for him, like he's saying yes, and then Hawk says, "You touch him, you touchin' me. Unnerstan'?" Kam doesn't say anything again, so Hawk moves his head up and down again. "Now you Jo-Boys, get on. This over here be my school, an' you got no binnis here."

Hawk walks me down the stairs to the bus stop then starts walking back up the stairs. When he gets about halfway back up, he turns and says, "Hey, Telephone Man," and I look up there and he gets a big grin and says, "You a kick. An' you right. Don' be lettin' nobody get that telephone stuff off you. That's you one big thing."

So then I'm on the bus and no niggers beat me up like they were supposed to. In fact, they helped me, and so now what was I supposed to do? I quit worrying about it for a while, though, because there was this awful smell, like somebody hung a bunch of strawberries down in the sewer, and I figured out I wasn't all done in that rest room and probably getting beat up made me quit paying attention and I had gone and messed up the the sweats Willie Weaver got for me out of the Lost and Found. I’m pretty sure the people around me noticed it because of the way they looked at me and then how the ones with perfectly good seats got up to stand near the back of the bus. So I got out at the next stop and walked on home. While I walked, I got to think a little bit, which is something I don’t usually like to do because it makes me feel nervous, and I wondered if my dad would mind if I stopped hating niggers for a while. I really love my dad and I wouldn’t stop if he said not to, and I wasn’t going to ask him right out because I didn’t want to disappoint him – but if my dad made a mistake about them, I wonder if he could of made a mistake about the other colors, too.
```

---

## IC-2505: The Thing about Turbulence

- Title: The Thing about Turbulence
- Author (byline): Elliott Hester
- Work: Plane Insanity
- Publisher: St. Martin's Griffin
- Publication date as stated: Feb 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1467
- Already set (do not supply): none

### Source block (context only)

```text
Author: Elliott Hester
Book: Plane Insanity
ISBN: 978-0312310066
Publisher: St. Martin's Griffin
Date (Month/Year): Feb 2003
```

### Introduction (context only: never use it for content warnings)

```text
Many people fear flying. After all, once you get on an airplane, you are committed to it for the duration of your journey; there’s no pulling over and stopping if you get uncomfortable. And while airplane crashes are much less common than car accidents, the media attention they receive makes them seem like a real threat. It’s little wonder, then, that airplane turbulence makes many travelers uneasy. It can happen without warning, causing a plane to shudder and dip erratically. Fear is a natural reaction – unless you are a flight attendant. Then it’s just a minor inconvenience . . . right? Well, here’s “The Thing About Turbulence” by Elliott Hester
```

### Performance text (classify this)

```text
Imagine you are floating

Released from the grip of gravity, you soar through recirculated airplane cabin air, high above those who were wise enough to heed the captain’s P.A. announcement. You are still clutching a plastic cup in one hand, but the beverage is now dripping from your seatmate’s face. The other hand has released the periodical you’d been reading, bringing a whole new meaning to the term “in-flight” magazine. You see these images, and more, in the slow-motion, frame-by-frame vision of one who has been forcibly ejected from his seat.

From this new and unusual vantage point, you look around and catch glimpses of insanity: a walking cane, minus its owner, hurtling through the cabin: a laptop crashing against a bulkhead: an explosion of peanuts; a sea of twisting heads; overhead bins opening like a chorus line of jaws – ejecting hats, coats and a whole slew of carry-on bags. No longer do you have to imagine how it would feel to fly. You are flying. You are a virtual Peter Pan – an airborne tourist, caught in the seismic upheaval of midair turbulence

This is what can happen when you fail to buckle your seat belt.

And don’t forget that the seat belt sign blinked on several minutes earlier. The flight attendants had roamed down the aisle, reminding everyone to buckle up, and the captain had warned of bumpy skies ahead. He told you to stay in your seat, to strap in tight, to be ready for a good jolt or two. However, as with most airplane announcements (except for those warning about delays or flight diversions), you regarded the captain’s remarks as gibberish. Besides, you don’t like wearing your seat belt. It’s too restrictive. You were annoyed when a flight attendant interrupted your conversation to tell you to buckle up. In fact, you rolled your eyes and frowned at her.

So, just to piss her off, you think about getting up to go to the bathroom – even though the plane is trembling as if hit by an earthquake. You’ll just walk right on over to the lavatory, stumbling if you have to, ignoring the attendant who will probably be strapped in her jump seat, pleading for you to sit down. You decide to do this, but you never get the chance. While you’re still in your seat – with your unfastened seat belt dangling from the cushion – the airplane suddenly drops a couple hundred feet.

Now look at you. Folded like a pretzel between rows 27 and 28, five rows from where you once sat.

In-flight turbulence is nothing to kid about. Our Emergency Procedures and Training report claims that each year, an average of fifty-eight passengers are injured in the U.S. while not wearing their seat belts during turbulence This is the leading cause of injury to passengers and crew in nonfatal accidents.

In the ten-month period between October 1999 and August 2000, some seventy-two passengers were injured in four separate incidents involving Chinese, Japanese, U.S. and British airlines. Perhaps the most serious incident occurred when a China Southern Airlines flight – en route from Kunming in southwestern Ching to Hong Kong – plunged two thousand feet, injuring forty-five passengers in the process. Though several of the injured were treated at a hospital and discharged, twenty-one had longer hospital stays. Seven remained in serious condition.

Chances are, none of the injured was wearing a seat belt.

This brings to mind a video that is part of the New York Department of Motor Vehicle license application process. After finishing the driver’s test, applicants are required to attend a few hours of class, which includes a video showing in glaring detail a series of gruesome accident scenes. A state trooper then appears on-screen to address the group. When the other driver wanna-bes and I watched the video, we began to have second thoughts about driving the streets of New York. In a strong, authoritative, “I’ve seen it all so you better listen” voice, Trooper Johnson left us with one parting thought about driver safety. “In all my years on the force,” he said. “I’ve never had to pull a dead person from behind a buckled seat belt.”

Trooper Johnson had a good point.

Since that day, I have never failed to wear a seat belt while riding in a car. And because the trooper’s advice can be easily applied to airplane passengers faced with in-flight turbulence, I always wear my seat belt when traveling as a passenger. While on duty, however, I’m forced to throw caution to the wind. The nature of the job demands that flight attendants check for compliance when the seat belt sign winks on during turbulence. It’s no surprise, then, that we’re usually the first to get injured.

During one particular flight to the Caribbean, I stood before the toilet in an airplane lavatory, eyes closed, pants gathered around my ankles answering the primal call of nature. When you stop and think about it, relieving oneself is one of life’s most tranquil experiences: a moment of reflection, an escape from the rigors of the work day, a blessed accomplishment that ends with a sigh of relief. But before my bladder could be purged, I found myself mashed against the ceiling with my feet dangling precariously above the toilet.

Over the years, colleagues have told me they’ve been slammed against the cabin ceiling or thrown into the laps of startled passengers. I’ve heard about the busted backs, fractured limbs and bloodied faces that resulted when passengers didn’t buckle up, even after the seat belt sign flashed on, even after the crew had completed a mandatory safety check and P.A. announcements warned of dangerous bumps ahead.

One fellow flight attendant was slammed against the ceiling so violently that his uniform shirt ended up covered with blood. Luckily, he sustained no permanent injuries. But when the plane landed, and the more severely injured passengers were removed, an airline supervisor walked up and asked him to change his shirt.

Can’t have bloodied flight attendants limping through the airport terminal, now can we?

Like most flight attendants, I’ve been forced to scramble to my jump seat during moments of rough turbulence. When chaos strikes, and the plane starts bucking like a mechanical bull gone berserk, we slam and lock galley doors, strap into our jump seats, then look at each other with disbelieving eyes. If ever I was to be launched toward the ceiling, I always imagined it would happen out in the aisle or in the galley, surrounded by shrieking humanity. I never thought that turbulence would strike when I was alone, in the lavatory, with my underwear at half mast.

Without warning, I seemed to float toward the ceiling. I was an astronaut in the middle of a weightlessness experiment. A mortal sent airborne against his will. In a split second I had gone from the sublime to the ridiculous. With my back pressed high against the lavatory wall, neck bent against the ceiling at an angle that only a contortionist could appreciate, I was at the mercy of God and aircraft dynamics.

That’s when I peed all over the toilet and the walls. I even let loose on my own shoes. This embarrassing act was not the result of fear. There wasn’t enough time to be scared. It happened because turbulence hit before I could finish my business.

The experience brought back childhood memories of an amusement park ride. Twenty or thirty people entered a large round room devoid of straps or any safety apparatus. The door shut behind us. A disembodied voice then instructed us to lean back against the wall. The room spun slowly at first, then picked up speed, with the centrifugal force pinning us against the spinning wall. Then the floor dropped, and we spun around and around, stuck to the wall like wet clothes in the final wash cycle.

Everybody loved it. I did too.

But I did not love my experience in the airplane lavatory.

In the next split second, I watched in horror as a couple of gallons of d-germ cam splashing up and out of the toilet. (D-germ is the pungent blue chemical that swishes around the toilet bowl after every flush. It’s designed to break down wasted and mask unpleasant odors by creating an unpleasant odor of its own.) It was a true comic moment. A Monty Python sketch come to life. My trousers became soaked with d-germ. My only consolation was that there were no chunks.

The airplane suddenly regained its composure. Gravity reestablished its grip. Wobbly as an Olympic gymnast who’d been drinking martinis the night before a crucial vault, my feet hit the floor and I came sprawling through the open lavatory door.

Nobody on the plan was hurt. Everyone, including my fellow crew members, had been wearing seat belts. Startled and only slightly bruised, I strapped myself into the jump seat, smelling of urine and d-germ.
```

---

## IC-2506: Tips for Women

- Title: Tips for Women
- Author (byline): Dave Barry
- Work: Dave Barry's Complete Guide to Guys
- Publisher: Ballantine Publishing
- Publication date as stated: April 1996
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 874
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Barry
Book: Dave Barry's Complete Guide to Guys
ISBN: 978-0449910269
Publisher: Ballantine Publishing
Date(Month/Year): April 1996
```

### Introduction (context only: never use it for content warnings)

```text
Humor is a tool that can improve relationships. Laughter has a way of establishing closeness and creating intimacy between couples. In relationships, it provides a way for people to bond on an emotional level. According to neuroscientist Dr. Robert Provine, who studies laughter, “Laughter establishes – or restores – a positive emotional climate and a sense of connection between two people, who literally take pleasure in the company of each other. Of course levity can defuse anger and anxiety, and in so doing it can pave the path to intimacy. Laughter is not primarily about humor, but about social relationships." Today I’d like to form a social relationship with you by presenting Tips for Women by Dave Barry.
```

### Performance text (classify this)

```text
CONTRARY to what many women believe, it's fairly easy to develop a long-term, stable, intimate, and mutually fulfilling relationship with a guy. Of course this guy has to be a Labrador retriever. With human guys, it's extremely difficult. This is because guys don't really grasp what women mean by the term relationship.

Let's say a guy named Roger is attracted to a woman named Elaine. He asks her out to a movie; she accepts; they have a pretty good time. A few nights later he asks her out to dinner, and again they enjoy themselves. They continue to see each other regularly, and after a while neither one of them is seeing anybody else.

And then, one evening when they're driving home, a thought occurs to Elaine, and, without really thinking, she says it aloud: ''Do you realize that, as of tonight, we've been seeing each other for exactly six months?''

And then there is silence in the car. To Elaine, it seems like a very loud silence. She thinks to herself: Geez, I wonder if it bothers him that I said that. Maybe he's been feeling confined by our relationship; maybe he thinks I'm trying to push him into some kind of obligation that he doesn't want, or isn't sure of.

And Roger is thinking: Gosh. Six months.

And Elaine is thinking: But, hey, I'm not so sure I want this kind of relationship, either. Sometimes I wish I had a little more space, so I'd have time to think about whether I really want us to keep going the way we are, moving steadily toward . . . I mean, where are we going? Are we just going to keep seeing each other at this level of intimacy? Are we heading toward marriage? Toward children? Toward a lifetime together? Am I ready for that level of commitment? Do I really even know this person?

And Roger is thinking: . . . so that means it was . . . let's see . . . February when we started going out, which was right after I had the car at the dealer's, which means . . . lemme check the odometer . . . Whoa! I am way overdue for an oil change here.

And Elaine is thinking: He's upset. I can see it on his face. Maybe I'm reading this completely wrong. Maybe he wants more from our relationship, more intimacy, more commitment; maybe he has sensed -- even before I sensed it -- that I was feeling some reservations. Yes, I bet that's it. That's why he's so reluctant to say anything about his own feelings. He's afraid of being rejected.

And Roger is thinking: And I'm gonna have them look at the transmission again. I don't care what those morons say, it's still not shifting right. And they better not try to blame it on the cold weather this time. What cold weather? It's 87 degrees out, and this thing is shifting like a garbage truck, and I paid those incompetent thieves $600.

And Elaine is thinking: He's angry. And I don't blame him. I'd be angry, too. I feel so guilty, putting him through this, but I can't help the way I feel. I'm just not sure.

And Roger is thinking: They'll probably say it's only a 90-day warranty. That's exactly what they're gonna say, the scumballs.

And Elaine is thinking: Maybe I'm just too idealistic, waiting for a knight to come riding up on his white horse, when I'm sitting right next to a perfectly good person, a person I enjoy being with, a person I truly do care about, a person who seems to truly care about me. A person who is in pain because of my self-centered, schoolgirl romantic fantasy.

And Roger is thinking: Warranty? They want a warranty? I'll give them a warranty. I'll take their warranty and stick it right up their . . .

''Roger,'' Elaine says aloud.

''What?'' says Roger, startled.

''Please don't torture yourself like this,'' she says, her eyes beginning to brim with tears. ''Maybe I should never have . . . Oh, I feel so . . . '' (She breaks down, sobbing.)

''What?'' says Roger.

''I'm such a fool,'' Elaine sobs. ''I mean, I know there's no knight. I really know that. It's silly. There's no knight, and there's no horse.''

''There's no horse?'' says Roger.

''You think I'm a fool, don't you?'' Elaine says.

''No!'' says Roger, glad to finally know the correct answer.

''It's just that . . . It's that I . . . I need some time,'' Elaine says.

(There is a 15-second pause while Roger, thinking as fast as he can, tries to come up with a safe response. Finally he comes up with one that he thinks might work.)

''Yes,'' he says.

(Elaine, deeply moved, touches his hand.)

''Oh, Roger, do you really feel that way?'' she says.

''What way?'' says Roger.

''That way about time,'' says Elaine.

''Oh,'' says Roger. ''Yes.''

(Elaine turns to face him and gazes deeply into his eyes, causing him to become very nervous about what she might say next, especially if it involves a horse. At last she speaks.)

The next day Elaine will call her closest friend, or perhaps two of them, and they will talk about this situation for six straight hours. In painstaking detail, they will analyze everything she said and everything he said, going over it time and time again, exploring every word, expression, and gesture for nuances of meaning, considering every possible ramification. They will continue to discuss this subject, off and on, for weeks, maybe months, never reaching any definite conclusions, but never getting bored with it, either.

Meanwhile, Roger, while playing racquetball one day with a mutual friend of his and Elaine's, will pause just before serving, frown, and say:

''Norm, did Elaine ever own a horse?''
```

---

## IC-2507: True Detective

- Title: True Detective
- Author (byline): David Sedaris
- Work: Naked
- Publisher: Little, Brown & Company
- Publication date as stated: March 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1981
- Already set (do not supply): none

### Source block (context only)

```text
Author: David Sedaris
Book: Naked
ISBN: 978-0316779494
Publisher: Little, Brown & Company
Date (Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
True Detective by David Sedaris
```

### Performance text (classify this)

```text
My mother had a thing for detectives, be they old, blind, or paralyzed from the waist down - she just couldn't get enough. My older sister shared her interest. Detective worship became something they practiced together, swapping plotlines the way other mothers and daughters exchanged recipes or grooming tips.

"How's your case coming?" my mother would shout from the kitchen during commercial breaks. Cupping her hands to the sides of her mouth, Lisa would yell, from the living room, "Tubby's still tracking down leads, but I'm betting it's the Chinesey guy with the eye patch and the ponytail." Theirs was a world of obvious suspects. Looking for the axe murderer? Try the emotionally disturbed lumberjack loitering near the tool shed behind the victim's house. Who kidnapped the guidance counselor? Perhaps it's the thirty-year-old tenth-grader with the gym bag full of bloody rope.

"You want to know who set fire to the retirement home? All right, it was ME, you satisfied now? That's right, ME. I did it. ME."

It's easy to solve a case when none of the suspects are capable of telling a decent lie. Television took the bite out of crime, leaving the detective as nothing more than a lifestyle. It seemed that anyone could solve a murder as long as he had a telephone, a few hours of spare time, and a wet bar. My mother had all three ingredients in spades. The more suspects she identified over the course of a season, the more con-fident she became. Together, she and my sister would comb the local newspaper, speculating on each reported crime.

"We know that the girl was held at knifepoint on the second floor of her house," Lisa said, tapping a pencil against her forehead. "So probably the person who robbed her was. . . not in a . . . wheelchair."

"I'd say that's a pretty safe assumption," my mother answered. "While you're at it, I think we might as well eliminate anyone confined to an iron lung. The important thing is that he used a knife. All right now, what kind of person uses a knife?"

Lisa guessed that it might have been a chef. "Maybe she was at a restaurant and the cook noticed she had a lot of money in her pocketbook."

"Right," my mother said, "because that's what cooks do, isn't it. They crawl around the dining-room floor looking through purses while the food sits in the kitchen cooking itself.

"I call the TV," my mother and sister would say. It didn't matter what you were watching, when they laid claim to one of the televisions, you surrendered it the same way cars gave up the road at the sight of an advancing ambulance. I couldn't bear the detective shows but made it a point to regularly check in with The Fugitive. This was the story of Dr. Richard Kimble, a man on the run, falsely accused of a crime he did not commit. We are told in the opening credits that "he changed his name. . . and his identity. The notion of identity was illustrated by a can of shoe polish sitting on what appeared to be the scuffed surface of a motel dresser. This had me stumped for months. "What," I asked, "would nobody recognize him with freshly shined shoes? Did he use it to blacken his face? I don't get it."

"His hair, stupid," Lisa said. "He used it to dye his hair."

It was one thing to sit in front of the television second-guessing a third-rate detective program, but quite another to solve a real case. We were well into the summer reruns when our household was shaken by a series of very real crimes no TV detective could ever hope to crack. Someone in our family had taken to wiping his or her butt on the bath towels. What made this exceptionally disturbing was that all our towels were fudge-colored. You'd be drying your hair when, too late, you noticed an unmistakable odor on your hands, head, and face.

This sudden turn of events tested our resolve to the core, leaving us to wonder who we were and where we, as a people, had gone wrong. Soul-searching aside, it also called for plenty of hot water, gallons of shampoo, steel wool, industrial scrub brushes, and blocks of harsh deodorizing soap. The criminal hit all three bathrooms, pausing just long enough to convince the rest of us that it was finally safe to let down our guard. I might spend twenty minutes carefully sniffing the towel only to discover that this time the idiot had used the washcloth.

Everybody had their theories but nobody had any hard evidence. My mother and sister had always thought themselves so wily and smart, but when pressed for a suspect, they said only that this case was beneath them. If someone were to be murdered or kidnapped, they'd rise to the occasion and finger the guilty party within an hour. This particular case fell under the category of "aggravated mischief" and was therefore unworthy of their professional attention.

Whoever it was would listen to their conscience and confess sooner or later. In the meantime, my mother would stock the linen closet with white towels. Case closed.

Later that month someone went through my father's top drawer, stealing a knee sock packed with one hundred and twelve Liberty silver dollars. I had seen and counted these coins many times. We all had, but who would go so far as to steal them?

My father gathered us all in the dining room and listened as we each took turns denying any involvement. "Dollars come in silver? I never knew that. Does the government issue them in a knee sock or was that your idea?"

Okay," my father said. "All right, I understand now. Nobody took my coins. I guess they just got tired of living cooped up in that dresser and decided to roll out the door and spend themselves on candy and magazines. That's what happened, isn't it! Oh, they're probably out there as we speak, having themselves a grand old time, aren't they?"

My mind was snagged on the thought of those jubilant silver dollars, raucous and dizzy with their first feelings of independence. I pictured their splitting into groups and traveling by night to avoid any excess attention. The thought of it made me laugh and when I did, my father said, "You think this is funny? You getting a chuckle out of this, are you? I'm glad you find it so amusing. Let's see how funny it is when I search your room, funny guy."

On television a search warrant guaranteed that your home would be trashed, and this was no different. Mine was the only clean room in the entire house. This was my shrine, my temple, and I watched in horror as my drawers were emptied and my closets brutally divorced of order. became the prime suspect, tried and convicted on circumstantial evidence. There was nothing I could say to change his mind.

Falsely convicted of a crime I didn't commit, there was only one thing I could do. The shoe polish was kept in the linen closet. I chose black, massaging it into my scalp in an attempt to change my identity.

The Fugitive's hair always looked perfectly natural. It blew in the breeze created by oncoming trucks as he stood beside the lonesome road, bidding farewell to a town unable to appreciate his unique gifts. My natural hair looked pretty much the same way, but once the polish dried, my hair hardened into a stiff, unified mass that covered my head like a helmet. I went to bed and awoke to find my sheets and pillows smudged and ruined. My face and arms were bruised looking, and everything stank with the rigid, military odor of a buffing rag. It was no wonder the Fugitive was a loner. I liked the sheen and color of my hair but found I needed to slick it back to maintain a clean forehead. This hair of mine was bulletproof. You could have pounded my head with a golf club and I wouldn't have felt a thing. I carried my soiled sheets into the woods, knowing that from here on out, things were going to be different. I had crossed over the edge, and there was no turning back.

After I changed my identity, my next step was to find the real thief and clear my name. My mother and sister were fond of saying, "The criminal always returns to the scene of the crime." This was a bit of dime-store wisdom picked up from one of their television programs, but I thought it might be worth a try. Aside from the silver dollars, my father's drawers were home to several pocket watches, a pair of cuff links shaped like dice, tie clips, and fine cigarette lighters.

Figuring the thief had good reason to return for more, I undertook a stakeout. My father's closet had shuttered, louvered doors that afforded a view of the entire room. I took my place, waiting a full hour before my mother entered the room. I watched as she rummaged through her closet, returning with a tall plastic box secured with the sort of latches you might find on a suitcase.

She carried the box to her dresser and unfastened the latches, lifting the lid to reveal a pale Styrofoam head supporting a sandy blond wig, the hair sculpted into a series of cresting waves. This was a magnificent crown of hair, so perfect that it might have been styled by God himself on one of those off days he was feeling creative rather than vengeful. After carefully removing the pins, my mother placed the wig upon her head and studied herself in the mirror. She nodded her head this way and that, but the curls, defying all laws of physics, held their position. Fumes from the shoe polish were making me nauseous, and I had begun to perspire, the inky sweat running down my forehead and staining my shirt.

"What do you say to that, missy?" my mother asked herself. She applied a coat of lipstick and brought her face close to the mirror, cocking her head and arching her eyebrows in a series of expressions that conveyed everything from heartfelt concern to full-throttle rage. Then she stepped away from the mirror, reintroducing herself slowly, as if her reflection were a guest she was meeting for the first time

Television stakeouts tend to reduce the hours of monotonous waiting into a single moment of truth. The detective arrives just in time to overhear the ransom instructions or catch the jewel thieves studying the blueprints to the museum. I stood for an hour with a head full of shoe polish, a fugitive, watching my mother in disguise and waiting for something to reveal itself.

Finally, my mother returned her wig to its hiding place and left the room. I waited for a few minutes and then crept downstairs, where I washed my hair three times, taking care to rinse the tub with Comet and destroy my soiled shirt. At the sound of my father's footsteps coming through the front door, I darted into my bedroom, slapping my face and examining my reflection in the darkened window. I wanted to be apple-cheeked, looking fresh and innocent when he rounded up the usual suspects, herding us into the dining room in an attempt to solve the greatest mystery of all: who had smeared his shirts and jackets with shoe polish?

When the time came, I'd take a seat beside the same crooks who had stolen the coins and wiped themselves on the towels and say, "Did you say shoe polish? On your suits? Today? No, sorry, I wouldn't know anything about that." .
```

---

## IC-2508: Truth in Dreams

- Title: Truth in Dreams
- Author (byline): Joshua Sands
- Work: Turning Points
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1019
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joshua Sands
Book: Turning Points
Publisher: Tichenor Publishing
ISBN: 978-0742117013
Date: 2001
```

### Introduction (context only: never use it for content warnings)

```text
I look in the mirror and say to myself:

"I look like me but I don't feel like me. Everything in my life seems to be changing. I'm not reacting the way I usually do. What's happening? Am I going crazy?"

No, I’m not. I’m going through one of the most intense, frightening and difficult emotional experiences of life and sometimes I believe that I’ve only just begun to find the Truth in Dreams by Joshua Sands.
```

### Performance text (classify this)

```text
The dream always begins the same way. Darkness becomes light and I'm marching to the cadence of a drum commander: Left, left, left, right, left. Only I can never stay in step, always skipping a beat to get back with the cadence. The cadence gets faster. And faster. And faster. Suddenly, I'm out of control. I'm marching straight into a tree, only the tree doesn't stop me. It shatters like glass and I continue on. Light becomes darkness. The cadence slowly fades away: Left, left, left, right, left.

My wife, Karen, and I are deeply in love. We only fight approximately three times per year. Sort of a tri-annual ritual, you might say. These fights usually involve money, taxes, or in-laws. Of course the third tight of this year falls into the" miscel-laneous" category: we're fighting over my potency. See, we want to have a child but can't seem to make it happen. She says I'm not potent enough; I say let's try harder. She may be right, but I can't admit that. I mean, you're told that one of the rea-sons you enter this world is to reproduce. Pass something on. Leave it behind. Can't imagine not being able to do that. So we fight; I defend myself out of sheer masculinity. And we try again. You can have anything if you try hard enough, my dad always said.

Our lives have begun to resemble a First Response commercial. It's as if our life evolves around the stick. The plus or minus that determines our future. A plus represents the future. A family. A minus means something is subtracted. With each minus, we lose something: control, hope, dreams.

The dream begins to come into focus. Left, right, left. I'm no longer marching but the cadence is clear. I'm riding a bus. Karen is next to me. She wants to get off the bus but I won't let her so I hold her in her seat. The bus accelerates with the beat. Left, right, left. It hits the tree and the wood shatters like glass. Light becomes darkness.

When she exits the bathroom: Honey, you won't believe this but... What - we got a double minus this time? No honey, we've done it.' See for yourself! My life has evolved around the stick and the stick reads: plus. Positive. As if God were reaching down and saying, "OK, you can start your life now." Positive. Addition. A new addition. What are we gonna do first?

First, the mall. Second, Toys R' Us. They've got some really fine products! Nothing is too much for my kid. I got him a plastic ball and bat. What if it's a girl? Then we'll play softball! You know the baby won't be born ready to throw a curveball. I know. I buy everything I can think of. Things for the future. Additions. I always envisioned buying this deluxe swing set so we got one! Four swings, three slides - a teeter-totter. You know, we're only having one child! Yeah, but we're making this one count! Think we have an overzealous father on our hands! Well, maybe.

It was if time stood still and flew by simultaneously. Karen and I were planners -like we were coordinating a big convention when tons of people would soon arrive. There was only one arrival on the way, but we were planning for more. We were moving from couple to family. Philosophers argue that if you can find just a few days of absolute happiness, then you're fortunate. Karen and I found months of absolute happiness. In the midst of going to work, paying bills, and all the other mundane tasks, we had found joy. And the true joy was still on the way...

Then one October night, Karen's putting away the dinner dishes when she says: Honey, Oh my God! He's coming! Oh my God, he's coming! OK, I've prepared for this for months. I can do this. One: Get her bag with her things. Got it. Two: Call the hospital. Check. Three: Help Karen to the car. Check. The contractions are getting closer. It's almost time! I have to get her there! The way I normally would go to the hospital has a train blocking the road. U-turn. Oh my God! My water broke! Are things supposed to happen that quickly? Don't worry, dear, I'll get you there! I'm taking side roads - swerving back and forth passing the other cars quickly and accurately. Wait - shortcut! I turn left, and I see a car coming straight at me. I turn back. A car is bearing down from the other side. Left. No wait, right. No - left. Suddenly, I'm spinning around. Spinning. Spinning. Karen!

Karen? Karen? I'm not actually speaking, but screaming in my head. My brother is there.

Where am I?

Ryan, you're in the hospital. Save your breath.

The hospital? Did I get Karen here on time? Why don't I remember?

Ryan, you were in an accident. Ryan, it was bad. I don't know how to say this. Ryan, Karen did-n't make it. I'm sorry Ryan.

What? My God - what have I done? I bring myself to say “Baby?”

Ryan, I'm really sorry. There was nothing anyone could do,

Nothing? You mean it's over? Over? Don't tell me that. Don't tell me they're gone. I thought, you know, maybe I'm hallucinating. Maybe I'm in a coma. Maybe. Bur I knew. I was in the hospital, the sole survivor of a bad accident. The result of a wrong turn - made by me: an overzealous father.

The dream crystallizes. The bus is a car. I'm driving the car. I swerve left. Then right. Then left again. No matter which way I turn, I am swerving the wrong way. Off beat. The tree has become a telephone pole. I reach over to hold Karen, trying to brace her from the crash. Light turns to darkness as the rescue unit breaks the car windows to save us. They say, “We can still save him but she's already gone.” Gone. Addition becomes subtraction. Dream becomes nightmare.
```

---

## IC-2509: Tuesdays with Morrie

- Title: Tuesdays with Morrie
- Author (byline): Mitch Albom
- Work: Not specified
- Publisher: Broadway Books
- Publication date as stated: Oct 1992
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2271
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mitch Albom
ISBN: 978-0767905923
Publisher: Broadway Books
Date (Month/Year): Oct 1992
```

### Introduction (context only: never use it for content warnings)

```text
Tuesdays with Morrie by Mitch Albom
```

### Performance text (classify this)

```text
The last class of my old professor’s life took place once a week in his house, by a window in the study where he could watch a small hibiscus plant shed its pink leaves.

The class met on Tuesdays. The subject was The Meaning of Life. No books were required, yet many topics were covered, including love, work, community, family, aging, forgiveness, and, finally, death. It was taught from experience.

The last class of my old professor’s life had only one student. I was the student.

His death sentence came in the summer of 1994. Morrie had amyotrophic lateral sclerosis (ALS), Lou Gehrig’s disease - There was no known cure.

“How did I get it?” Morrie asked. Nobody knew.
“Is it terminal?”
Yes.
“So I’m going to die?”
Yes, you are, the doctor said. I’m very sorry.

ALS is like a lit candle: it melts your nerves and leaves your body a pile of wax. Often, it begins with the legs and works its way up. You lose control of your thigh muscles, so that you cannot support yourself standing. You lose control of your trunk muscles, so that you cannot sit up straight. By the end, you are breathing through a tube in a hole in your throat, while your soul, perfectly awake, is imprisoned inside a limp husk, perhaps able to blink, or cluck a tongue, a man frozen inside his own flesh. This takes no more than five years from the day you contract the disease. Morrie’s doctors guessed he had two years left. Morrie knew it was less.

But my old professor had made a profound decision: He would not wither. He would not be ashamed of dying. Instead, he would make death his final project, the center point of his days. Since everyone was going to die, he could be of great value, right? He could be research. A human textbook.

“Study me in my slow and patient demise. Watch what happens to me. Learn with me.” Morrie would walk that final bridge between life and death, and narrate the trip.

We Talk about Death

“Mitch,” he said softly, “you know that I’m dying.” I knew. “All right, then.” Morrie swallowed the pills, put down the paper cup, inhaled deeply, then let it out. “Shall I tell you what it’s like?”

What it’s like? To die?

“Yes,” he said. Although I was unaware of it, our last class had just begun.

“Dying,” Morrie suddenly said, “is only one thing to be sad over, Mitch. Living unhappily is something else. So many of the people who come to visit me are unhappy.”

Why?

“Well, for one thing, the culture we have does not make people feel good about themselves. We’re teaching the wrong things. And you have to be strong enough to say if the culture doesn’t work, don’t buy it. Create your own. Most people can’t do it. They’re more unhappy than me—even in my current condition. “I may be dying, but I am surrounded by loving, caring souls. How many people can say that?”

I was astonished by his complete lack of self-pity. Morrie, who could no longer dance, swim, bathe, or walk; Morrie, who could no longer answer his own door, dry himself after a shower, or even roll over in bed. How could he be so accepting?

We Talk About the World

“It’s hard to explain, Mitch. Now that I’m suffering, I feel closer to people who suffer than I ever did before. The other night, on TV, I saw people in Bosnia running across the street, getting fired upon, killed, innocent victims . . . and I just started to cry. I feel their anguish as if it were my own. I don’t know any of these people. But—how can I put this?—I’m almost . . . drawn to them.” His eyes got moist, and I tried to change the subject, but he dabbed his face and waved me off.

Amazing , I thought. I worked in the news business. I covered stories where people died. I interviewed grieving family members. I even attended the funerals. I never cried. Morrie, for the suffering of people half a world away, was weeping. Is this what comes at the end, I wondered? Maybe death is the great equalizer, the one big thing that can finally make strangers shed a tear for one another.

I leaned over to give him a hug. And then, although it is not really like me, I kissed him on the cheek. I felt his weakened hands on my arms, the thin stubble of his whiskers brushing my face.

“So you’ll come back next Tuesday?” he whispered.

We Talk About Feeling Sorry for Yourself

I asked Morrie if he felt sorry for himself.

“Sometimes, in the mornings,” he said. “That’s when I mourn. I feel around my body, I move my fingers and my hands—whatever I can still move—and I mourn what I’ve lost. I mourn the slow, insidious way in which I’m dying. But then I stop mourning. I concentrate on all the good things still in my life. On the people who are coming to see me. On the stories I’m going to hear. On you—if it’s Tuesday. Because we’re Tuesday people.”

I grinned. Tuesday people. I thought about all the people I knew who spent many of their waking hours feeling sorry for themselves. How useful it would be to put a daily limit on self-pity. Just a few tearful minutes, then on with the day. And if Morrie could do it, with such a horrible disease . . .

“It’s only horrible if you see it that way,” Morrie said. “It’s horrible to watch my body slowly wilt away to nothing. But it’s also wonderful because of all the time I get to say good-bye.” He smiled. “Not everyone is so lucky.”

I studied him in his chair, unable to stand, to wash, to pull on his pants. Lucky? Did he really say lucky?

We Talk About Regrets

I wondered what regrets he had once he knew his death was imminent. Would he have done much differently? Selfishly, I wondered if I were in his shoes, would I be consumed with sad thoughts of all that I had missed? Would I regret the secrets I had kept hidden?

“Mitch,” he said, “the culture doesn’t encourage you to think about such things until you’re about to die. We’re so wrapped up with egotistical things, career, family, having enough money, meeting the mortgage, getting a new car, fixing the radiator when it breaks— we’re involved in trillions of little acts just to keep going. So we don’t get into the habit of standing back and looking at our lives and saying, Is this all? Is this all I want? Is something missing?” He paused.

“You need someone to probe you in that direction. It won’t just happen automatically.”

I knew what he was saying. We all need teachers in our lives. And mine was sitting in front of me. And I figured if I was to be the student, then I would be as good a student as I could be.

That day, I made a small list on a yellow legal pad,
issues and questions that we all grapple with:
Death
Fear
Aging
Greed
Marriage
Family
Society
Forgiveness
A meaningful life

We Talk About Fear

The small horrors of [Morrie’s] illness were growing, and when I finally sat down [again] with him, he was coughing more than usual, a dry, dusty cough that shook his chest and made his head jerk forward. After one violent surge, he stopped, closed his eyes, and took a breath.

“What I’m doing now,” he continued, his eyes still closed, “is detaching myself from the experience. And this is important—not just for someone like me, who is dying, but for someone like you, who is perfectly healthy. Learn to detach. Detachment doesn’t mean you don’t let the experience penetrate you. On the contrary, you let it penetrate you fully. That’s how you are able to leave it.”

I’m lost.

“Take any emotion—love for a woman, or grief for a loved one, or what I’m going through, fear and pain from a deadly illness. If you hold back on the emotions— if you don’t allow yourself to go all the way through them—you can never get to being detached, you’re too busy being afraid. You’re afraid of the pain, you’re afraid of the grief. You’re afraid of the vulnerability that loving entails. But by throwing yourself into these emotions, by allowing yourself to dive in, all the way, over your head even, you experience them fully and completely. You know what pain is. You know what love is. You know what grief is. And only then can you say, ‘All right. I have experienced that emotion. I recognize that emotion. Now I need to detach from that emotion for a moment.’”

Morrie stopped and looked me over; perhaps to make sure I was getting this right. “I know you think this is just about dying,” he said, “but when you learn how to die, you learn how to live.”

I thought about how often this was needed in everyday life. How we feel lonely, sometimes to the point of tears, but we don’t let those tears come because we are not supposed to cry. Or how we feel a surge of love for a partner but we don’t say anything because we’re frozen with the fear of what those words might do to the relationship.

Morrie’s approach was exactly the opposite. Turn on the faucet. Wash yourself with the emotion. It won’t hurt you. It will only help. If you let the fear inside, if you pull it on like a familiar shirt, then you can say to yourself, “All right, it’s just fear, I don’t have to let it control me. I see it for what it is. I know that there are other emotions in the world, and I’m going to experience them as well.”

“Detach,” Morrie said again.

We Talk about Society

Morrie believed in the inherent good of people. But he also saw what they could become. “People are only mean when they’re threatened,” he said later that day, “and that’s what our culture does. That’s what our economy does. Even people who have jobs in our economy are threatened, because they worry about losing them. And when you get threatened, you start looking out only for yourself. You start making money a god. It is all part of this culture.” He exhaled. “Which is why I don’t buy into it.”

“You must build your own subculture. Here’s what I mean,” Morrie said. “I don’t mean you disregard every rule of your community. I don’t go around naked, for example. I don’t run through red lights. The little things, I can obey. But the big things—how we think, what we value—those you must choose yourself. You can’t let anyone—or any society determine those for you.

“Take my condition. The things I am supposed to be embarrassed about now—not being able to walk, not being able to wipe [myself], waking up some mornings wanting to cry—there is nothing innately embarrassing or shaming about them. It’s the same for women not being thin enough, or men not being rich enough. It’s just what our culture would have you believe. Don’t believe it.”

He continued. “The problem, Mitch, is that we don’t believe we are as much alike as we are. Whites and blacks, Catholics and Protestants, men and women. If we saw each other as more alike, we might be very eager to join in one big human family in this world, and to care about that family the way we care about our own. “But believe me, when you are dying, you see it is true. We all have the same beginning—birth—and we all have the same end—death. So how different can we be?”

“Invest in the human family. Invest in people. Build a little community of those you love and who love you.”

He squeezed my hand gently. He smiled. “In the beginning of life, when we are infants, we need others to survive, right? And at the end of life, when you get like me, you need others to survive, right?” His voice dropped to a whisper. “But here’s the secret: in between, we need others as well.”

Graduation

Morrie died on a Saturday morning. He had fallen into a coma two days after our final visit, and the doctor said he could go at any moment. Instead, he hung on, through a tough afternoon, through a dark night. Finally, on the fourth of November, when those he loved had left the room just for a moment—to grab coffee in the kitchen, the first time none of them were with him since the coma began—Morrie stopped breathing. And he was gone.

Have you ever really had a teacher? One who saw you as a raw but precious thing, a jewel that, with wisdom, could be polished to a proud shine? If you are lucky enough to find your way to such teachers, you will always find your way back.

The last class of my old professor’s life took place once a week, in his home, by a window in his study where he could watch a small hibiscus plant shed its pink flowers. The class met on Tuesdays. No books were required. The subject was the meaning of life. It was taught from experience . . . The teaching goes on.
```

---

## IC-2510: Under the Wolf, Under the Dog

- Title: Under the Wolf, Under the Dog
- Author (byline): Adam Rapp
- Work: Not specified
- Publisher: Candlewick Press
- Publication date as stated: Sept 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MOM, DAD, NURSE
- Teaser before the introduction: Yes
- Spoken words (computed): 2182
- Already set (do not supply): none

### Source block (context only)

```text
Author: Adam Rapp
ISBN: 978-0763618186
Publisher: Candlewick Press
Date (Month/Year): Sept 2004
```

### Introduction (context only: never use it for content warnings)

```text
Steven Nugent was a gifted student, in the honor program at school, taking accelerated classes and he appeared to have the world by the tail . . . that is until his world and his family began to fall apart. This is his story . . . . Under the Wolf, Under the Dog by Adam Rapp
```

### Performance text (classify this)

```text
(Page 1-3) How to start. Okay. Here it goes. Mrs. Leene said I should begin by describing myself. So, my name is Steve Nugent. I'm just seventeen. It was my birthday last month, in November. Now it's the middle of December, and the trees around here arc caked in ice and sort of silvery in that creepy, wintry way, so right now seventeen seems like a hundred years off. In terms of size, I'm six foot three and about 145 pounds, which is way too skinny, I know. I can't help that right now. The doctors say I'll fill out in a few years. At this point I would describe myself as being a pretty high-percentage dodge-ball target. I’m also blind in my right eye, which I will tell you more about later. So I'm currently in residence at this place in the middle of Michigan called Burnstone Grove. There are about thirty-five kids here. About half of us are drug addicts, and the other half have tried to check out of this world in one way or another. Probably a third of us have dabbled in both pursuits. I don't entirely fit into either category, so I'm what they call a Gray Grouper. The Red Groupers are the junkies, and the Blue Groupers are the suicide kids. There are only seven Gray Groupers, and we're generally kept here for a month or two before we're either shipped back home or sent to another, more affordable, facility. The truth is that I could easily be a Red or Blue Grouper. I’ve done some drugs, and I have to admit that I’ve through about the other scenario more than once. All of that will come later, though. I don’t want to tell you everything just yet.

(Page 6) So . . . a couple of months ago, my brother, Welton, hanged himself with a necktie. I think that’s a good place to begin. My Mom died just a few weeks before that . . . (Page 9) My mom my mom my mom my mom my mom. . . (page 10-14) Maybe Welton killed himself because he lived in the basement. Who knows what all that damp air and cement will do to a person. Maybe he killed himself because for the last year of his life all he did was smoke weed and play Vice City on his Play Station II. And then again, maybe it was some weird noise in my brother’s head, some little digital murmur he never told anyone about. I’ve heard about that – how you wake up one day and there’s like this permanent dial tone droning somewhere in your head, a little Dustbuster trapped where the brain saves you from going crazy. After a while you wind up ending it all just to make things quiet again. I found Welton in his room in the basement. He'd knotted the necktie around a hook at the top of his door. The hook had broken, but that didn't stop the asphyxiation. What's weird is that he was kneeling. It looked like he was praying or pulling up weeds in a garden. For some reason half his face was blue. Right now when I close my eyes and try and see the parts of his body, I keep missing stuff, like his arms and his shoulders. I can see his face as clear as day and I could even go into detail about his Adam's apple or this little blue vein under his right eye or the weird paste that was coming out of his left nostril, but other more obvious things like limbs are lost to me. Limbs and eye color. I can't place that either. It was like someone had stolen that stuff. The EMT guys were as quiet as aliens, and when they pushed the gurney through the living room, I finally reached over and closed Welton’s mouth. "Bye," I said to him as they wheeled him away. Just for a second I had the feeling that he might say something back, but he didn’t. He just looked sort of waxy and stunned. I know my mom would have been making coffee for everyone and trying not to cry – she was strong like that – but she was already dead. [I remember her last few weeks] . . . I was about to get ready for bed [one night] when I heard my mom call for me. Whenever she would call out my name like that – especially during her last few weeks – it was like getting thumped between the shoulder blades with a hammer. (Page 47-50) In the hospice room, my mom was trying to reach the straw from her water cup. She was totally bald at this point, and the whites of her eves had dulled to this weird brownish gray. She only weighted eighty-something pounds and her lips had sort of disappeared. My mouth hurts just imagining her.

MOM: Steven, help me drink, honey. I took a step toward her and l could see a new growth pressing through her forehead. There were things emerging all over her lately. At first they were calling it breast cancer, but now it was everywhere. A few weeks before, the oncologist had discovered a tumor in her abdomen that was the size of a baseball. She took my hand and asked me to do an Our Father with her. I knelt down at the side of her bed and bowed my head. She took my hands with one of hers, and we began. [Our father who art in heaven, hallowed be thy name] Her fingers were bloated and soft. While we prayed, I sort of went blank. I kept waiting for something to stir inside – like a holy fluttering or whatever – but it never came. When we were through praying, my mom fell asleep. Even though her mouth was all dried and shriveled, she was sort of smiling. The morphine always made her happy. I must confess here that there was a time or two when I was tempted to slip the needle into my own vein just to see what it was like, but that would have been heinous. I slid my hands out from under hers and quietly left her room. (Page 52) All of a sudden, for some reason, my [house] felt like it was shrinking, like the walls were totally losing in on me. So that’s when I left. The keys to the Fairmont were on the kitchen table. I grabbed them – no one else would be using them anytime soon. (Page 55-57) l got bored with the radio after about fifteen minutes and turned it off. The last think I needed was more insanity in my life. Suddenly the steering wheel was vibrating. I looked at my hands and they were trembling so bad I thought the veins in my wrists would burst. I pulled over to a Shell station. I was sort of hyperventilating, so I had to take a moment to catch my breath. That’s when I started doing the Our Father again. [Our father who art in heaven, hallowed be thy name] I sat there for a moment and thought about my mom. It was her groans of pain that would get me the most. Sometimes they didn’t even sound human. (Page 77-79) When I turned onto our block, I switched the lights off and stopped the engine. Then I shifted to neutral and coasted into the driveway. I left the car keys on the kitchen table and limped straight to my mom’s room. She was sleeping really still and her room smelled even worse than ever, I just stood there and watched her curtains blowing for a moment. I remember how blue they were. I think it was the first time I had ever noticed them. A moment later I heard the door creak behind me. I turned around and my dad was standing in the entrance. He was wearing a three-piece suit. It was gray and it looked too small, like he'd stolen it. He made a swallowing sound and adjusted the knot in his tie.. .

DAD: She's dead. He just stood there staring at my mom, but I wouldn't look at her. You couldn't have paid me a million dollars. I was afraid of what I might see, that some other crazy tumor was popping out of her mouth or something. Then he said it again. “Dead.” One word. All by itself. (Page 90-91) My mom my mom my mom my mom my mom ... The day after she died, they cremated mv mom and stuffed her ashes into a pine box and put an eight-by-ten photo next to it. When the priest announced that there would be a moment of silence for those of us, who were too shy to share a special memory or speak on [her] behalf, Welton started singing "The Star Spangled Banner." (Page 94) Mrs. Leene says that everyone grieves differently, that sorrow and anger manifest themselves in strange ways because of how our minds are actually designed to protect us from those feelings. I will say this: I wish I could have cried then. I think if I could have had a good cry, things might have gotten better somehow. (Page 239-241) [That night, I found that my mom had left Weldon and me a letter]. . . (Steven reads) “Remember me, please. An ordinary woman with a good heart. A woman who loved her children and took great pride in them. Remember that I was a great nurse who treated everyone with the same compassion. Remember that I wanted our family to be close, but I died without that happening and I felt sad about it. Remember that I loved you both with my whole heart and though I was far from a perfect mom, I did the best I knew how. Welton, have faith that your back will heal and that you will one day again play basketball. [aside: (Page 10) As a junior, Welton was the starting forward on the basketball team, but he had to quit three-quarters of the way through the season because of a herniated disk. My brother never quite made it back onto the basketball court]

Steven Jacob, remember that I loved you – and would have done anything to stay with you. I think you are the smartest person I know, my sweet boy. The Moon will rise, The Sun will set, Please do not forget . . . . Mary Lee Nugent.” (Steven puts his hand to his face and pushes hard against his eyes with his thumbs, struggling to control his emotions) (Page 244-250) I woke to a nurse feeding a tube into my right arm. The IV needle was cold, and I couldn’t see out of my right eye. Everything on the right side of my body sort of throbbed, and I was afraid to move. “Where am I?”

NURSE: You’re in the intensive care unit of the ophthalmology ward at Medical Associates. “What happened?” My voice sounded like it hasd been taken out and put back in.

NURSE: Well, from what I hear, you put ywn thumb through your right eve. You have a shield over it. It was a various serious puncture, Steven. There’s a strong chance that you’ve lost vision in your right eye.

(Page 272-273) . . . “My mom died,” I said. I had no idea that was going to come out of my mouth, but it did. “She had breast cancer . . . And she died.” I could feel this totally thick sort of anguish feeling taking over my body that has never quite left. (Long silence) (Page 6) And then . . . a couple of months ago, my brother, Welton, hanged himself with a necktie. [I found him . . . ] (Page 286-288) Down in the basement, Welton’s door was three-quarters open. The Price Is Right was on full volume. My brother’s room was a cyclone of laundry, CD boxes and warped and ketchup-stained paper plates. His stereo had been turned down, but a CD was spinning quietly. It was that Bottomside song “Forty Holes and Forty Goals.” I turned the TV off and the music played. [Sing a couple of lines of the song here – link to a video of the song is provided at the end of this selection]: “There’s a hole in my head, I’m gonna find it; I’m gonna fill it . . . . There’s a hole.” I pressed stop and turned the stereo off. I turned around and there he was.

He’d hanged himself from a coat hook at the top of the door. He’d used one of my dad’s old Marine Corps ties. I just stared at him for a moment. “Hey . . . Everything’s gonna be okay, okay?” Then I closed his door, which was actually really heavy, and headed back upstairs. (Long silence) (Page 2) So [now] I'm currently in residence at this place in the middle of Michigan called Burnstone Grove. (Page 310) [Before you go] I just have to say a few more things. I’ve been thinking about them a lot the past few days. It’s sort of this list I’m starting . . .

1. People are born and people die.
2. Parents get cancer and their ashes get stuffed
into earns.
3. The urns get buried in holes
4. Brothers break your heard.
5. You have to deal with stuff on your own and
that’s all there is to it.

Song “Forty Holes and Forty Goals” by Bottomside : https://www.youtube.com/watch?v=p-8yV4JRehA
```

---

## IC-2511: Viva Vargas!

- Title: Viva Vargas!
- Author (byline): Woody Allen
- Work: Complete Prose of Woody Allen
- Publisher: Random House
- Publication date as stated: March 1992
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ANNOUNCER
- Teaser before the introduction: Yes
- Spoken words (computed): 1859
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: Complete Prose of Woody Allen
ISBN: 978-0517072295
Publisher: Random House
Date (Month/Year): March 1992
```

### Introduction (context only: never use it for content warnings)

```text
Before the Assassination of the President of San Marcos, rebel forces led by Emilio Molina Vargas struggled as all rebel forces must. The life of a revolutionary is seldom as glamorous as it may seem. We flash back now to the early days of the rebellion as shown though the eyes of a common man . . . . a cook . . . . a revolutionary! Viva Vargas! Excerpts from the diary of a Revolutionary by Woody Allen.
```

### Performance text (classify this)

```text
ANNOUNCER: Good afternoon. Wide World of Sports is in the Republic of San Marcos where we're going to bring you a live, on-the-spot assassination. They’re going to kill the president of this lovely country and replace him with a military dictatorship. The weather this afternoon is perfect and, if you've just joined us, we've seen a series of colourful riots that started with the bombing of the American Embassy, a ritual as old as the city itself. It was one of the most exciting spectacles I've ever seen. Now the moment we've been waiting for is here. Everyone is getting quiet.

June 3: Viva Vargas! Today we took to the hills. Outraged and disgusted at the exploitation of our little country by the corrupt Arroyo regime, we sent Julio to the place with a list of our grievances and demands, none hastily arrived at nor, in my opinion, excessive. As it turned out, Arroyo's busy schedule did not include taking time away from being fanned to meet with our beloved rebel emissary, and instead he referred the entire matter to his minister, who said he would give our petitions his full consideration, but first he just wanted to see how long Julio could smile with his head under molten lava. Because of many indignations such as this one, we have at last, behind the inspired leadership of Emilio Molina Vargas, decided to take matters into our own hands. If this be treason, we yelled on street corners, let us make the most of it.

I was, unfortunately, lolling in a hot tub when word ar-rived that the police would be by shortly to hang me. Bounding from my bath with understandable alacrity, I stepped on a wet bar of soap and cascaded off the front patio, luckily breaking the fall with my teeth, which skidded around the ground like loose Chiclets. Though naked and bruised, survival dictated I act quickly, and mounting El Diablo, my stallion, I gave the rebel yell! The horse reared and I slid down his back to the ground, fracturing certain small bones. Were all this not devastating enough, I scarcely got twenty feet by foot when I remembered my printing press, and not wanting to leave behind such a potent political weapon or piece of evidence, I doubled back to retrieve it. As luck would have it, the thing weighed more than it looked, and lifting it was a job more suited to a derrick than a hundred-and-ten-pound college student. When the police arrived, my hand was caught in the machinery as it roared uncontrollably, reprinting large passages of Marx down my bare back. Don't ask me how I managed to tear loose and vault out a back window.

Luckily I eluded the police and made my way to safety in Vargas's camp.

June 4: How peaceful it is here in the hills. Living out under the stars. A group of dedicated men all working toward a common goal. Although I had anticipated a say in the actual planning of the campaigns, Vargas felt my services might better be employed as company cook. This is not an easy job with foodstuffs scarce, but somebody has to do it and, all things considered, my first meal was a big hit. True, not all the men are terribly partial to Gila monster but we can't be choosy, and apart from some picayune eaters who are prejudiced against any reptile, dinner came off without incident.

July 10: Today was generally a good day, despite the fact that we were ambushed by Arroyo's men and badly decimated. This was partially my fault as I gave away our position by inadvertently shrieking the names of the Christian triumvirate when a tarantula crawled over my leg. For several moments I could not dislodge the tenacious little spider as it made its way into the inner recesses of my garments, causing me to gyrate spastically toward the stream and thrash about in it for what seemed like forty-five minutes. Shortly after, Ar-royo's soldiers opened fire on us. We fought gamely, although the shock of being surprised created a mild disorganization, and for the first ten minutes our men were shooting at each other. Vargas narrowly escaped catastrophe as a live hand grenade landed at his feet. He commanded me to fall on it, aware that he alone is indispensable to our cause, and I did so. As Providence would have it, the grenade did not explode and I walked away unharmed except for a slight twitch and the inability to fall asleep unless someone holds my hand.

July 15: The morale of the men seems to be holding up, despite certain minor setbacks. First, Miguel stole some ground-to-ground missiles but mistook them for ground-to-air missiles and, attempting to down several of Arroyo's planes, blew all our trucks up. When he tried to laugh it off, Jose became furious and they fought. Later, they patched things up and deserted. Desertion, incidentally, could become a major problem, although at this moment optimism and team spirit have held it down to three out of every four men. I, of course, remain loyal and do the cooking, but the men still do not seem to appreciate the difficulty of that as-signment. The fact is, my life has been threatened if I don't come up with an alternative to Gila monster. Sometimes soldiers can be so unreasonable. Still, perhaps one of these days I will surprise them with something new. Meanwhile we sit around the camp and wait.

August 1: Despite all we have to be thankful for, there is no doubt that a certain tension has set in here at rebel headquarters. Little things, apparent only to the observant eye, indicate an undercurrent of uneasiness. For one thing, there are quite a few stabbings among the men, as quarrels become more frequent. Also an attempt to raid an ammunitions depot and rearm ourselves ended in a rout when Jorge's signal flare went off prematurely in his pocket. All the men were chased except for Jorge, who was captured after banging off two dozen buildings like a pinball. Back at camp in the evening, when I brought out the Gila monster the men rioted. Several of them held me down while Ramon struck me with my ladle. I was mercifully saved by an electrical storm that claimed three lives. Finally, with frustrations at a peak, Arturo struck up "Cielito Lindo" and some of the less musically inclined ones in the group took him behind a rock and force-fed him his guitar. Vargas now feels that perhaps he was premature in predicting a December success and indicates that total victory might require additional time. Strangely enough, he has turned from his field maps and charts and relies more heavily now on astrological readings and the entrails of birds.

August 12: The situation has taken a turn for the worse. As luck would have it, the mushrooms I so carefully picked to vary the menu with turned out to be poisonous, and while the only really disconcerting side effect was some minor convulsions most of the men suffered, they seemed unduly embittered. On top of that, the CIA has reconsidered our chances of bringing off the revolution and as a result threw Arroyo and his cabinet a conciliatory brunch at Wolfie's in Miami Beach. This, coupled with a gift of twenty-four jet bombers, Vargas interprets as a subtle shift in their sympathies. Morale still seems reasonably high and, while the desertion rate has risen, it is still limited to those who can walk. Vargas himself appears to be a bit morose and has taken to saving string. It is now his feeling that life under the Arroyo regime might not be all that uncomfortable, and he wonders if we should not reorient the men that are left, abandon the ideals of the revolution, and form a rumba band. Meanwhile the heavy rains have caused the mountain to landslide, and the Juarez brothers were carried off into the gorge as they slept. We have dispatched an emissary to Arroyo, with a modified list of Our demands, taking care to strike out the portions concerning his unconditional surrender and substituting in its place an award-winning recipe for guacamole. I wonder how it will all turn out.

August 15: We have taken the capital! The incredible details follow: After much deliberation, the men took a vote and de-cided to pin our last hopes on a suicide mission, guessing that the element of surprise might be just the thing to offset Arroyo's superior forces. As we marched through the jungle, toward the palace, hunger and fatigue slowly sapped a portion of our resolve and, approaching our destination, we decided to switch tactics and see if groveling would work. We turned ourselves over to the palace guards, who brought us at gunpoint before Arroyo. The dictator took into consideration the mitigating fact that we had given up voluntarily, and while he still planned to disembowel Vargas, the rest of us were going to get off with being skinned alive. Reevaluating our situation in light of this fresh concept, we succumbed to panic and bolted in all directions while the guards opened fire. Vargas and I raced upstairs and, seeking a place to hide, burst into Madame Arroyo's boudoir, surprising her in a moment of illicit passion with Arroyo's brother. Both became flustered. Arroyo's brother then drew his revolver and let fly a shot. Unbeknownst to him, this acted as a signal to a group of mercenaries who had been hired by the CIA to help clean us out of the hills in return for Arroyo's granting the United States rights to open Orange Julius stands here. The mercenaries, who were themselves confused regarding their loyalties due to weeks of American foreign policy equivocating, attacked the palace by mistake. Arroyo and his staff suddenly suspected a CIA double cross and turned their guns on the invaders. Concurrently a long-smoldering plot to assassinate Arroyo by several Maoists misfired when a bomb they planted in a taco went off prematurely, exorcising the left wing of the palace and projecting Arroyo's wife and brother through some wood beams.

Throughout this, Vargas, our beloved leader, brilliantly adopted a policy of watchful waiting, which he executed by crouching motionless at the fireplace and assuming the disguise of a decorative blackamoor. As the coast became clear he advanced on tiptoe to the central office and assumed power, pausing only to open the royal refrigerator and slap together a deviled-ham sandwich. I spoke with Vargas afterward about the serious business of running a country. While he believes free elections are essential to any democracy, he prefers to wait until the people become a bit more educated before there is any voting. Until then, he has improvised a workable system of government based on divine monarchy and has rewarded my loyalty by allowing me to sit by his right hand at mealtime. Plus I also am responsible for seeing that the latrine is spotless.
```

---

## IC-2512: Waffle

- Title: Waffle
- Author (byline): Owen Egerton
- Work: How Best to Avoid Dying
- Publisher: Dalton Publishing
- Publication date as stated: 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1759
- Already set (do not supply): none

### Source block (context only)

```text
Author: Owen Egerton
Book: How Best to Avoid Dying
ISBN: 978-0974070377
Publisher: Dalton Publishing
Date (Month/Year): 2007
```

### Introduction (context only: never use it for content warnings)

```text
• NOTE: GREETING COULD USE MORE VERVE. FLOOR AT ENTRANCE STICKY. • NOTE: BLINDS NEED DUSTING. CASA DE WAFFLE HOT SAUCE ECLIPSED BY A.1. SAUCE. SYRUP CONTAINTER NEEDS TOPPING OFF. • NOTE: WAITRESS ‘HILLARY.’ SHIRT STAINED AND UNTUCKED. PANTS RUMPLED.

Waffle by Owne Egerton
```

### Performance text (classify this)

```text
For thirty-four years I was a Waffle House secret inspector. In fact, I was the top secret inspector. I traveled to every Waffle House in the nation and trained hundreds of others. My unofficial title was Uber-Inspector. That was six months ago, but my eyes still catch it all. The batter crust on the menu, the cracked tile three from the register, the radio playing instead of the juke box. Minor infractions. Incidentals. Nothing I’d report to the main office. Just notes for the manager in my report. I would never meet him. He can never know my face. Secrecy is key. I used to take notes with a pen the size of a toothpick on a notepad the size of a credit card. But I’ve turned in my tiny pen and pad. Still, I can’t help but think what I would have written.

Hillary is obese. Very obese. The front roll of her belly rests on my table. Her hair is an unnatural red. Heated coil red. It sticks out from her scalp like wires. She is wearing make-up, but she is not wearing it well. It looks as if it has been applied in the dark by a drunk child.

I don’t judge people based on physical beauty. But Hillary is unclean and that’s a bad trait for a food server. She also has a problem with mucus. She places a glass of water down and drags her flabby, wet nostrils along her uniform’s sleeve. I’m disgusted, but my face reveals nothing. I am a spy.

“Anything to drink?” she asks. Her voice is pleasant enough. Softer than I’d expected.

“I’ll have a decaf coffee, please.” Under the table I press start on my stopwatch. The beverage should reach the customer within a minute and a half. Add an extra fifteen seconds if the order is hot cocoa.

As in every Waffle House, there are two distinct coffee pots. Black handle for regular. Orange handle for decaffeinated. Hillary grabs the black handle, pours a cup and returns to my table.

“Is that decaf?” I ask

She nods.

“Because I’m allergic to caffeine and if it’s not decaf my heart will explode and I will die.”

“I’m allergic to walnuts.”

My hands twitch.

“Anything to eat?” she asks. I order the All Star Special.

“Stumpy,” she yells. “We need an A-S-S.”

Stumpy, a short black cook hovering over the grill, raises his hand, which isn’t there. In place of the hand is a spatula duct-taped to the stump. I watch him. He’s fast. He’s good. I relax and sip my coffee. I’m not really allergic to caffeine.

Waffle House are magic. Eclectic gatherings. It’s a quarter till four and look at these wanderers who have found each other. The drunk stewing at the counter, the Hispanic couple cooing in booth three, the teenagers daring each other to French kiss spoonfuls of ketchup. This is life. This is America.

The All Star Special includes two eggs, one waffle, four strips of bacon, grits, and toast. It should arrive at the table in six to nine minutes. Stumpy prepares a plate in seven minutes and thirty-four seconds. Well done, Stumpy. Hillary brings it to the table – not careless, but clumsy. As she walks the eggs slide into the grits, but she’s trying and she’s smiling. I’ll give her that, she smiles.

Runny eggs, soft waffle, shiny bacon. I’m happy. I like Waffle Houses to work. I like to write STELLAR at the top of my report. I like the basics to be covered so a store can go deeper. Moving beyond “Was the water glass refilled?” to “What was the true motivation of the waiter pouring the water?”

I enjoy every bit, saving the waffle for last. I’m ready to add the perfect amount of Whipped Spread and syrup and gobble it up while it’s still hot, but when I open up my tub of Whipped Spread I find an unpleasant surprise.

NOTE: MELTED SPREAD

It’s a tub of yellow liquid, little white globs floating like scum in an overused hotel hot tub. I motion for Hillary, who is staring at the air. She sees me and waddles over.

“More coffee?” she asks.

“Can I have another tub of butter? This one is melted.” Notice I call it butter. All part of the disguise. Anyone who knows Waffle House knows the Whipped Spread is about as close to butter as Alabama is to Asia. Personally, I prefer the spread. Perfect for waffles.

Hillary is on her way back to my table with a fresh tub when the phone rings. She squeals and hops to the phone. It’s the fastest I’ve seen her move since I arrived.

“Hello, Waffle House,” she says. She nods, then covers the mouth-piece. “Stumpy, it’s the radio people again.”

“Oh, my,” says Stumpy, turning from his half-grilled hash browns. The drunk gives a loud whoop.

“Radio people?” I ask.

“They’ve been calling us for the past hour. It’s their morning show.”

“It’s four a.m.”

“They start real early.”

“Is it the station we’re listening to?”

“Yep, yep, yep.”

“Why didn’t we hear you?”

She looks at me with what I can only presume is some kind of pity. “They pre-record it.” she says.

I nod and return to my waffle. I open my new spread and find it, too, is liquid.

“Excuse me.” I grab Hillary by the sleeve. “This is all melted, too.”

“Yeah,” she frowns. “We keep them by the grill. Anything else?” Hillary is waiting, doodling on her pad. I take a deep breath. “Yes, please,” I say. “A hot slice of apple pie and a cold scoop of vanilla ice cream.”

“No apple pie,” she says without looking from her doodles. “I think we’re out.”

“Can you check?”

“I did a minute ago,” she says. “We’re out.”

“Then why did you say you think?”

She looks up from her pad. “It’s a figure of speech. Like a metaphor.”

“Like a metaphor?”

“Would you like pecan?”

“I want apple.”

“No apple. Just pecan.”

I order pecan. She brings it, smiling again, but I no longer find it pleasant. The pecan pie tastes like sticky chalk. Hard to swallow. I chew slowly. I try to calm myself. My doctor says no losing my temper. I’m too old to afford anger.

“More coffee?” she asks. I could kill her. “Or another slice of pie?” I could pour syrup down her throat until she drowns.

The phone rings and Hillary squeals, drops my check and scampers off.

I try another bite. Paper and sugar.

“They say I should stand on a table,” Hillary says to Stumpy, the phone again pressed to her ear. “They say they’re watching somewhere outside. They want me to life my shirt, Stumpy.”

“You can’t see *that* on the radio.”

“Stumpy, it’s five thousand dollars.”

“I don’t know. You could lose – “

But it’s too late. Hillary climbs up on the table of the booth next to mine, unbuttons her shirts and out flop her breasts. Dear God. Pink, strained flesh popping from the sides of tan mesh bra. It’s as if two shaved possums are hammocked and hibernating on her chest. The teenagers gasp, the drunk claps, Stumpy hides his eyes with his one good hand.

Hillary giggles, rebuttons her shirt, and bounces back to the phone.

“What are they saying?” Stumpy asks.

“I don’t know. They’re laughing,” Hillary says. “They hung up. I don’t understand.” She puts down the phone. “I think they said something mean.” Her face is a flustered red. “I wonder how I get my money?”

My anger is gone. It’s just too sad. I abandon my pecan pie, walk up to the register, and hand Hillary a twenty dollar bill and my check. I avoid looking at her. I avoid thinking about her. I just want to be outside, driving away.

“Here’s your change,” she says, no embarrassment, no shame in her tone. It makes everything worse. I’m looking up to tell her to keep the change when I notice, right next to the register, on a plate, under a glass lid – an untouched, genuine, Waffle House apple pie. And there’s Hillary’s chubby fist handing me crumpled bills.

“I take it back,” I say. “I do not like the Waffle House.” My voice is loud. The couple looks up. “I do not enjoy your smells, your grimy menus. I despise your unclean lavatories, your timorous steaks, your powdered hot cocoa.” The drunk is leaning away. Stumpy is forgetting to flip an egg. “And you,” I yell, pointing a shaking finger at Hillary, “you are not going to win any money, you stupid thing. Thing! So mop the entrance floor, turn down the music and keep the damned spred in the fridge.”

The door dings open.

“Good morning,” Stumpy says weakly, keeping his eyes on me. I turn to the door. Two men walk in carrying a life-sized pink cow with the words “KLOL Cash Cow” painted on the side.

“We’re here to give away some mooooooney!” shouts one of the men into a wireless microphone.

“Oh my God! Oh my God! Oh my God!” Hillary leaps up and down, her body jiggling in waves. The other man runs through the store high-fiving the customers and staff, stopping just short of Stumpy. It takes both men to hoist Hillary up on the back of the Cash Cow. They hand her a wad of cash and snap some photos.

Stumpy turns up the radio and pumps his arms in the air.

“The Waffle House is a rockin’,” yells one DJ into his microphone.

Hillary is happy. A goofy, doughy ball of joy. Why can’t I feel happy for her? Why do I find myself wishing the plastic cow would collapse under her weight or that the DJs would snap the money back and laugh at her naivete?

Stumpy is weeping behind the counter. People are cheering and laughing and toasting Hillary with coffee cups and juice glasses. Hillary is chanting, “Thank you, radio people! Thank you, radio people!”

I squeeze past the Cash Cow and leave.

It is still more night than morning. But the sky is growing paler. I notice the Waffle House sign is glowing above me.

NOTE: ‘A’ AND SECOND ‘F’ NEED NEW BULBS.

I climb into my car and start the engine. Glancing in my rearview mirror, I can’t see the Cash Cow. It’s below the window, but I see Hillary. She’s galloping, waving an arm above her head like a rodeo star.
```

---

## IC-2513: A Walk to Remember

- Title: A Walk to Remember
- Author (byline): Nicholas Sparks
- Work: Not specified
- Publisher: Grand Central Publishing
- Publication date as stated: Sept 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JAMIE, LANDON
- Teaser before the introduction: Yes
- Spoken words (computed): 2218
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nicholas Sparks
ISBN: 978-0446693806
Publisher: Grand Central Publishing
Date (Month/Year): Sept 2004
```

### Introduction (context only: never use it for content warnings)

```text
In this heart-wrenching story, Landon Carter is shown the depths of the human heart and the joy and pain of living from a most unexpected person . . . Jamie Sullivan.

A Walk to Remember by Nicholas Sparks
```

### Performance text (classify this)

```text
Now, Jamie was a nice girl. She really was, [but she] wasn’t exactly what I considered attractive. Despite the fact that she was thin, with honey blond hair and soft blue eyes, most of the time she looked sort of . . . . plain. [And] Jamie carried her Bible wherever she went. She would [even] read the Bible during lunch break at school. Despite these strikes, though, the one thing that really drove me crazy about her was the fact that she was always so [dang] cheerful.

The homecoming dance was coming up, and I still didn’t have a date. So there I was, flipping through the pages in the [yearbook] when I saw Jamie Sullivan’s picture. I closed the yearbook. Jamie Sullivan? [The reverend's] daughter? Absolutely not. I spent the rest of the evening debating the pros and cons, but in the end the choice was obvious. I had to ask Jamie to the dance. I made my way down the streets of Beaufort, reached her front door, took a second to catch my breath, and finally knocked.

JAMIE: Landon, this is a surprise! Well, I’d invite you in, but my father isn’t home, and he doesn’t allow boys in the house while he’s not around.

LANDON: Oh, that’s okay. We can talk out here, I guess.

JAMIE: So, what did you want to talk to me about?

LANDON: Sure is a beautiful day. Why I’ll bet there’s not a single cloud in the whole sky.

JAMIE: Landon, you didn’t come here to talk about the weather, did you?

LANDON: Not really.

JAMIE: Then why are you here?

LANDON: Well . . . . I wanted to know if you would like to go to the homecoming dance with me.

JAMIE: I’d love to . . . on one condition. You have to promise that you won’t fall in love with me.

I knew she was kidding by the way she laughed, [so] I smiled and gave her my word. In the two weeks following the homecoming dance, my life pretty much returned to normal. Sunday I was in my room, working on my application to UNC. I was writing one of my essays when the phone rang.

JAMIE: Landon?

LANDON: Oh, hey. What’s going on? Why are you calling me?

JAMIE: I wanted to ask you a favor. I’d like to ask you if you wouldn’t mind playing Tom Thornton in the school play.

LANDON: Can’t someone else do it instead? Being seen with her once was bad enough . . . but being seen with her every day? What would my friends say? But I could tell this was really important to her.

JAMIE: I’ve been praying about it, Landon. I’d really like this play to be special this year, not for me, but because of my father. I know how much it will mean to him to see me be the angel, because this play reminds him of my mother . . . Will you think about it? The next day I talked to Miss Garber, went through the audition and got the part. Rehearsals started the next week. I began to stumble through my lines for the next few days, not really even attempting to learn them. I’d crack a joke or two, which everyone laughed at, except for Jamie and Miss Garber. [But] Jamie wasn’t going to let me off that easy.

JAMIE: Do you ever think about the future, Landon? What you want to do with your life?

LANDON: I don’t know yet. I haven’t figured that part out. I’m going to UNC next fall, at least I hope so. I have to get accepted first. How about you? What do you want to do in the future?

JAMIE: I want to get married. And when I do, I want my father to walk me down the aisle and I want everyone I know to be there. I want the church bursting with people. . . . Yes. That’s all I want.

LANDON: Well, you’ll get married someday. You’ll meet some guy and the two of you will hit it off, and he’ll ask you to marry him. And I’m sure that your father will be happy to walk you down the aisle.

JAMIE: (wistfully) I hope so. The next night, as I was walking her home we talked about her Bible.

LANDON: Why do you always carry it with you?

JAMIE: It was my mother’s.

LANDON: Oh . . . . I’m sorry I asked.

JAMIE: It’s okay, Landon. How could you have known. My mother and father were given this Bible for their wedding, but my mom was the one who claimed it first. She read it all the time, especially whenever she was going through a hard time in her life. She had it with her in the hospital when I was born. When my father found out that she had died, he carried the Bible and me out of the hospital at the same time.

LANDON: I’m sorry.

JAMIE: It just gives me a way to . . . to be a part of her. Can you understand that? The night of the play was cool and crisp. [My character] Tom Thornton is [is supposed to be] amazed when he first sees the angel [Jamie], which is why he goes around helping her as she shares Christmas with those less fortunate. The first words out of Tom’s mouth are, “You’re beautiful,” and I was supposed to say them as if I meant them from the bottom of my heart. The problem, however, was that I still hadn’t nailed this lie yet. Sure, I said the words, but they didn’t come off to convincingly. I kept trying to imagine someone else as the angel so that I could get it just right. The next thing I knew, the curtain was opening and I was walking past storefronts and looking in windows for the music box my daughter wants for Christmas. My back was turned from where Jamie entered, but I heard the crowd collectively draw a breath as soon as she appeared on stage. I readied myself to turn around, and when I did, I finally saw what it was all about. Her honey-colored hair was handing loosely, with a trace of glitter in [it], sparkling like a crystal halo. It was absolutely amazing to behold. She was smiling slightly, as if she were holding a secret close to her heart. She looked exactly like an angel.

LANDON: You’re . . . . You’re beautiful And I think that everyone in the whole auditorium knew that I actually meant it. To say that the play was a smashing success was to put it mildly. But because of Jamie’s presence, it really became something special . . . . [After the play] Jamie insisted that I go with her to the orphanage on Christmas Eve.

JAMIE: I’m so glad you could come.

LANDON: So am I . . . . I bought you something . . . . A gift, I mean.

JAMIE: You didn’t have to do that.

LANDON: I know, but I wanted to.

JAMIE: I brought you something, too. Please, open it. I want you to have it. I already knew what was inside, and I couldn’t believe what she had done. My hands began to tremble. When it was finally free of the paper, I slowly ran my hand over the top of the well-worn leather as tears filled my eyes. Jamie had given me her Bible.

JAMIE: Thank you for doing what you did. It was the best Christmas I’ve ever had. She smiled at me and I smiled at her and all I could do was wonder how I’d ever fallen in love with a girl like Jamie Sullivan. I drove Jamie home from the orphanage later that night.

JAMIE: Landon, do you ever think about God? Do you ever wonder why things have to turn out the way they do? I’ve been thinking about it a lot lately. I know the Lord has a plan for us all, but sometimes, I just don’t understand what the message can be. Does that ever happen to you?

LANDON: Well, I don’t think that we’re meant to understand it all the time. I think that sometimes we just have to have faith.

JAMIE: (thoughtfully) Yes, you’re right. I realized that Jamie had been misunderstood her entire life, not only by me, but by everyone. Jamie wasn’t simply the minister’s daughter, someone who read the Bible and did her best to help others. Jamie was also a 17-year-old girl with the same hopes and doubts that I had. At least that’s what I assumed, until she finally told me.

JAMIE: People think I’m strange, don’t they? Do you think I’m strange, too?

LANDON: You’re a wonderful person, Jamie. You’re beautiful, you’re kind, you’re gentle . . . you’re everything that I’d like to be. I love you, Jamie. You’re the best thing that ever happened to me.

JAMIE: (beginning to cry) Please don’t say that. . . Please . . . . I’m sorry. I’m so, so sorry . . . You can’t be in love with me, Landon We can be friends, we can see each other . . . but you can’t love me.

LANDON: Why not?

JAMIE: Because, I’m very sick, Landon. I’m dying. She had leukemia; she’d known it since last summer. Time had suddenly stopped and I understood everything. I understood why she’d wanted me to do the play; why she wanted Christmas to be so special. Why she’d given me her Bible.

LANDON: No, no, there has to be some mistake. Why didn’t you tell me?

JAMIE: I’d made a decision that it would be better if I told no one, and I asked my father to do the same. No one would look me in the eye. If you had only a few months left to live, is that what you would want? I was for the first time in my life, completely and utterly at a loss. I’d been in love with her for only 18 days. Those 18 days seemed like my entire life, but now, when I looked at her, all I could do was wonder how many more days there would be. On Monday she didn’t show up for school, and I somehow knew that she’d never walk the hallways again. She was finished with school forever; she would never receive her diploma. I left school early and went to Jamie’s

JAMIE: Hello, Landon, this is a surprise. My father isn’t home right now, but if you’d like to sit on the porch, we can.

LANDON: How can you do this? How can you pretend that nothing is wrong? Aren’t you frightened?

JAMIE: Yes, I’m frightened all the time. [But] when the doctors first told us, they said that I should try to lead as normal a life as possible for as long as I could.

LANDON: There’s nothing normal about this.

JAMIE: I know. . . I know you’re frightened too. I began to pray for a miracle. We started reading the Bible together. On February 14, Valentines Day, Jamie picked out a passage that meant a lot to her. She told me that if she’d ever had the chance, it was the passage she’d wanted read at her wedding.

JAMIE: Love is always patient and kind. It is never jealous. Love is never boastful or conceited. It is never rude or selfish. It does not take offense and is not resentful. Love takes no pleasure in other people’s sins, buts delights in the truth. It is always ready to excuse, to trust, to hope and to endure whatever comes. Jamie was the truest essence of that very description. A week later Jamie’s trips to the hospital became more regular, although she insisted that she didn’t want to stay there overnight.

JAMIE: I want to die at home. Since the doctors couldn’t do anything for her, they had no choice but to accept her wishes

LANDON: I’ve been thinking about the past few months. Do you have any regrets?

JAMIE: We all have regrets, Landon. But I’ve led a wonderful life.

LANDON: How can you say that? With all that’s happening to you.

JAMIE: I’ve been happy, Landon. I really have. I’ve had a special father who taught me about God. I can look back and know that I couldn’t have tried to help other people any more than I did. I’ve even fallen in love and had someone love me back.

LANDON: Will you do something for me?

JAMIE: I don’t know if I can anymore.

LANDON: Will you marry me? Just as she’d wanted, the church was bursting with people as we were married on March 12, 1959. Although Jamie was weak and hadn’t moved from her bed in two weeks, she insisted on walking down the aisle so that her father could give her away.

JAMIE: It’s very important to me, Landon. It’s part of my dream, remember? Then Jamie and [her dad] slowly made their way down the aisle, while everyone in the church sat silently in wonder. Halfway down the aisle, Jamie suddenly seemed to tire, and they stopped while she caught her breath. Her eyes closed, and I remember thinking it was the most difficult walk anyone ever had to make. In every way, a walk to remember. It was, I remember, the most wonderful moment of my life. In front of God and everyone else, I’d promised my love and devotion, in sickness and in health, and I’d never felt so good about anything. It is now forty years later, and I can still remember everything from that day. I still love her, you see, and I’ve never removed my ring. I smile slightly, looking toward the sky, knowing there’s one thing I still haven’t told you: I now believe that miracles can happen.
```

---

## IC-2514: Wanda Hickey’s Night of Golden Memories

- Title: Wanda Hickey’s Night of Golden Memories
- Author (byline): Jean Shepherd
- Work: Not specified
- Publisher: Broadway Books
- Publication date as stated: Jan 1976
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: REPORTER, SCHWARTZ, ME, AL, MORTY, MOM, WANDA, WAITER
- Teaser before the introduction: Yes
- Spoken words (computed): 1236
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jean Shepherd
ISBN: 978-0385116329
Publisher: Broadway Books
Date (Month/Year): Jan 1976
```

### Introduction (context only: never use it for content warnings)

```text
Or do they? Wanda Hickey’s Night of Golden Memories by Jean Shepherd
```

### Performance text (classify this)

```text
REPORTER: (Pg 299 – 300) Puberty rites in the more primitive tribal societies are almost invariably painful and traumatic experiences . . . A classic example is the Ugga Buggah tribe of lower Micronesia. When an Ugga Buggah reaches puberty, the rites are rigorous for both sexes. Difficult dances are performed and the candidate for adulthood must eat a sickening ritual meal during the postdance banquet. You will also notice that his costume is as uncomfortable as it is decorative . . . Here we see the ritual dance in progress. (An obviously uncomfortably dressed young man dances a crazy ritual dance to heavy drum beats) Of course, we in more sophisticated societies no longer observe these rites . . .

SCHWARTZ: (Pg 301-302) You going to the prom? I read on the bulletin board where it said you wear a summer formal to the prom.

ME: That’s where you wear one of those white coats. Ya gotta rent ‘em. (Pg 305-312) The next day, after school, I went downtown to Al’s Swank Formalwear. I could feel excitement rising deep inside me.

AL: OK, boys. Ya wanna make it big at the prom, am I right? Ya come to the right place. (Yelling to the back room) HEY, MORTY! HERE’S [ONE] MORE FOR THAT BASH AT CHERRYWOOD. I’D SAY ONE FAWTY REGULAH.”

MORTY: THE FAWTY AIN’T BEEN CLEANED YET!

AL: BRING IT OUT, AWREADY! This suit just come in from anotha job. Don’t worry about how it looks. We’ll clean it up an’ take it in so’s it’ll fit good.

ME: Al held up the suit invitingly. (slips his arms into the jacket)

AL: Perfect. Couldn’t be bettuh. Take it in a little here. . . An’ doan worry ‘bout the stain; we’ll get it out. Here, try on these pants. (Putting on the pants) They were rumpled and smelled strongly of some spilled beverage, but they were truly magnificent. The waist came to just a shade below my armpits. (sashaying around)

AL: Perfect. Just right. Put a little tuck in the waist, so. (Grabbing several yards of the seat) And a little in here. You’re [a] high-class customer. Now, I suppose ya wanna go first class right? . . . . Right? With an air of mystery, he bent over, slid open a drawer and placed atop the counter an object that unfocused my eyes with its sheer brilliance.

AL: A genuwine Hollywood paisley cummabund. It’s only a buck extra . . . [And] how do you expect to trip the light fantastic without a pair of black patent-leatha dancin’ pumps?

ME: Dancin’ what?

AL: (Irritably) Shoes, shoes. And we throw in the socks for nuttin’. How ‘bout it?

Step by step, in the ancient tradition, the tribal ritual was being acted out. The prom was now two weeks off . . . (Pg 315) Everything was set to go, except for one thing – no girl.

SCHWARTZ: How ya doin’ with Daphne Bigelow?

ME: Oh, that. I haven’t had time to ask her. (pg 312) [She] drifted by on gossamer wings, her brilliant smile lighting up the corners of homeroom. (Pg 314) [Then there was only] one week to go. I knew I could never ask Daphne Bigelow to be my date . . .

MOM: (Pg 303) Why not take that nice Wanda Hickey?

ME: Ah, come on, Ma. This is the prom. This is important. You don’t take Wanda Hickey to the prom. Wanda Hickey was the only girl who I knew for an absolute fact liked me. She laughed at my jokes and once when we were 12, actually sent me a valentine. (pg 315-319) A feeling of helpless rage settled over me as I [went to water] the lawn.

WANDA: What are you doing?

ME: (Somewhat exasperated) Oh, hi, Wanda. I’m sprinkling the lawn.

WANDA: I’m sure glad school’s almost over. I never thought I’d be a senior.

ME: Yeah. Then it happened. I realized there was no sense fighting it. Some guys are born to dance forever with the Daphne Bigelows. Others – well, they do the best they can.

ME: (To Wanda) Wanda? Would you . . . well . . . I mean uh . . . how about . . . going to the prom with me? The die was cast. There was no turning back. . . (Pg 326) [Prom] day dawned bright and sunny, as perfect as a day can be. (Pg 328-333) I took two showers. I knew what happened to people who didn’t – disastrous B.O. It would not happen to me. (sniffs armpits) Tonight I would be a truly magnificent specimen of lusty manhood. Laid out on my bed was my beautiful summer formal. (In words and pantomime) Carefully, I undid the pins that festooned my pleated Monte Carlo shirt. I struggled to get [the studs] in place between the concrete slits. It was impossible! Never in my life had I experienced a collar remotely like the one that now clamped its iron grasp around my windpipe. It dug mercilessly into my throat – a mere sample of what was to come. Tie, shoes, cummerbund and snowy coat. And there I stood – Adonis! (Admiring himself in the mirror) (Pg 334-335) When I pulled up before Wanda’s house, she was out on the porch. With stately tread, I moved up the walk; my pants were so tight that if I’d taken one false step, God knows what would have happened. (Sees Wanda and his mouth drops open) This was NOT the old Wanda. For one thing, she didn’t have her glasses on, and her eyes were unnaturally large and liquid. Milky skin and golden hair radiating in the glow of the porch light. In accordance with the tribal custom, we drove off through the soft night. [And] from all over town, other cars, polished and waxed, carried the rest of the junior class to their great trial by fire.

REPORTER: (pg 300) Here we see the ritual dance in progress. (An obviously uncomfortably dressed young man dances a crazy ritual dance which shifts to the standard box step as the Ugga Buggah tribesman morphs into our narrator) (Pg 336-341) 1-2-3 Pause . . . Back and forth, up and down. 1-2-3 Pause . . . By now my dashing concrete collar had removed a wide strip of skin encircling my neck. Wanda was exhaling directly into my face with a heady essence of cough drops and sauerkraut. [She] started to sweat through her taffeta. I felt it running down her back. My own back was already wet and the sweat, which had now saturated my jockey shorts was pouring down my legs. I pulled [her] closer and we swung back into action. .1-2-3 Pause . . . . [Then] all of a sudden, it was over. The band played Good Night, Sweetheart and we were out . . . . SEE YOU AT THE ROOSTER! – The savage tribal rite was nearing its final and most vicious phase.

REPORTER: (Pg 300) The candidate for adulthood must eat a sickening ritual meal during the postdance banquet. (pg 342-347) A beady-eyed waiter, hair glistening with Vaseline Hair Oil, sidled over and hovered like a vulture. Quickly distributing the famous Red Rooster Deluxe Menu, he smirked and waited for us to impress our dates.

WAITER: Can I bring you anything to drink? My first impulse was to order my favorite drink, a bottled chocolate concoction called Kayo, the Wonder Drink; but remembering that better things were expected of me on prom night, I said, in my deepest voice

ME: Uh . . . make mine . . . burbon.

WAITER: How will you have it, sir?

ME: Well, in a glass, I guess. And make it a triple. (To audience) I had some vague idea that this was a brand or something. I also ordered – for reasons that even today I am unable to explain – lamb chops, yellow turnips, mashed potatoes and gravy and a side dish of Italian Cole slaw. (Acknowledges the waiter returning with the drink) Swiftly, I brought the bourbon to my lips, intending to down it in a single devil-may-care [shot]. Down it went – a screaming 90-proof rocket searing savagely down my gullet. (Eyes watering, unable to gasp for breath, but trying desperately to appear manly)

WANDA: Isn’t this romantic? Isn’t this the most wonderful night in all our lives?

ME: Urk . . . Urk . . . yeah! In all the excitement of preparation for the prom, I realized that I hadn’t eaten a single thing all day. Maybe [food] would help! (Lowers head and shovels food in quickly) I tried the potatoes and gravy. I wolfed down the Cole slaw. My stomach . . . .

(He’s obviously going to get sick, he gags and throws up violently beside his chair– after he recovers, he wipes his mouth sheepishly with the back of his hand)

(Pg 348-349) It was the absolute high point of the junior prom.
```

---

## IC-2515: What’s the Worst That Could Happen?

- Title: What’s the Worst That Could Happen?
- Author (byline): Bruce Coville
- Work: Oddest of All
- Publisher: Harcourt Children's Books
- Publication date as stated: Sept 2008
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MIKEY, MURPHY, TIFFANY, MRS. WHITCOMB, VOICE
- Teaser before the introduction: Yes
- Spoken words (computed): 1718
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bruce Coville
Book: Oddest of All
ISBN: 978-0152058081
Publisher: Harcourt Children's Books
Date (Month/Year): Sept 2008
```

### Introduction (context only: never use it for content warnings)

```text
What’s the Worst That Could Happen? by Bruce Coville
```

### Performance text (classify this)

```text
Good luck and I have rarely shared the same park bench. Sometimes I think Murphy’s law – “If something can go wrong, it will” – was invented just for me. I suppose the fact that my name is Murphy Murphy might have something to do with that feeling. Yeah: Murphy Murphy. It’s like a family curse. (Beat) The last name I got from my father, of course. The first name came down from my mother’s side, where it is a tradition for the firstborn son. You would think my mother might have considered that before she married Dad, but love makes fools of us all. I guess. (Beat) Anyway, you can see that right from the beginning of my life, if something could go wrong, it did. Okay, I suppose it could have been worse. I could have been born with two heads or something. On the other hand, as I lie here in my hospital bed trying to work out exactly how I got here, there are times when I wonder if being born with two heads might not have been the best thing. (Beat) To begin with, I want to say here and now that Mikey Farnsworth should take at least part of the blame for this situation. The one I am not going to blame is Tiffany Grimsley, though if I hadn’t had this stupid crush on her, it never would have happened.

MIKEY: Man, you’ve got it bad for Tiffany!

MURPHY: (Blushing and embarrassed) What are you talking about?

MIKEY: (laughing) Look at you blush, Murphy! There’s no point in trying to hide it. I watched you drooling over her in social studies class today. And you’ve only mentioned her, like, sixteen times since we got home this afternoon. I do not think I have actually drooled over Tiffany during social studies class. But it is hard not to think about her then, because she sits right in front of me. It’s the last class of the day, and the October sunlight comes in and catches in her golden hair in a way that makes it hard to breathe. (To Mikey, groaning) What am I going to do?

MIKEY: (shrugs) Either you suffer in silence, or you tell her you like her. Is he nuts? If you tell a girl you like her, it puts you totally out in the open. I mean, you’ve got no place to hide. And there are really only two possible responses you’re going to get from her: (a) She likes you, too (expression of pure terror) or (b) anything else, which is, like, totally, utterly humiliating. Then, on Wednesday, it’s as if the gods are smiling on me, which not something I am used to. Tiffany grabs my arm on the way out of social studies and says

TIFFANY: Can I talk to you for a second, Murphy?

MURPHY: Sure. Not very eloquent, but it is better than the first thought that crossed my mind, which is, “Anytime, anywhere, any moment of the day.” It is also better than, “Your words would be like nectar flowering into the hungry mouths of my ears,” which was a line I had come up with for a poem I was writing about her. She hands me a folded-over set of papers, and my heart skips a beat. Can this be a love letter?

TIFFANY: I wrote this skit for drama club, and I thought maybe you would do it with me next Friday. I think you’d be just right for the part.

MURPHY: Yes! She gives me one of those sunrise smiles of hers, grabs my arm and gives it a squeeze, and says,

TIFFANY: Thanks. This is going to be fun. Then she’s gone, leaving me with a memory of her fingers on my arm and a wish that I had started pumping iron when I was in first grade, so my biceps would have been ready for this moment.

MIKEY: Murphy, you can’t go onstage with her. You can’t even move when you get onstage. Don’t you remember what happened in fifth grade?

As if I could forget . . . . (Flashback) Mrs. Carmichael had cast me as George Washington in our class play, and I was, I want to tell you, pretty good during rehearsals. But when they opened the curtain and I saw the audience…well, let’s just say that when my mother saw the look on my face, she actually let out a scream. She told me later she thought I was having a heart attack. As for me, my mouth went drier than day-old toast, and the only reason I didn’t bolt from the stage was that I couldn’t move my arms or legs. Heck, I couldn’t even move my fingers. I couldn’t even squeak! They had to cancel the performance. Even after the curtains were closed, it took two teachers and a janitor to carry me back to the classroom. (To Mikey) Oh, man, what am I gonna do? I wail.

MIKEY: Come on, let’s look at the script. Maybe all you have to do is sit there and she’ll do all the acting. (the boys leaf through the script) No such luck. The script, which is called “Debbie and the Doofus,” is very funny. It also calls for me to say a lot of lines. It also calls for me to act like a complete dork. Immediately, I begin to wonder why Tiffany thinks I would be just right for this role. After two days I know not only my lines, but all of Tiffany’s lines, too, as well as the lines for Laurel Gibbon, who is going to be playing the waitress at the little restaurant where we go for our date. My theory is that I will enjoy rehearsals and the excuse they give me to be with Tiffany, and then pray for a meteor to strike me before the day of the performance.

MIKEY: (Scanning the skies) No meteor yet! Maybe you could be sick that day.

MURPHY: (Shaking his head) If I let her down, I will hate myself forever.

MIKEY: (Rolling his eyes) Maybe you should run away from home. Despite my prayers, Friday arrives. I don’t suppose I really expected God to cancel it, though I would have been deeply appreciative if he had. I go through the day in a state of cold terror. At 2:45 Mrs. Whitcomb, the drama club coach, comes back to wish us luck.

MRS. WHITCOMB: Okay, kids – break a leg! This is how people wish each other luck in theater?!

TIFFANY: Are you excited?

MURPHY: You have no idea. Inside me, a small voice is screaming,

VOICE: What were you thinking of you moron? You are going to humiliate yourself in front of all these people, including the girl you would cut out your heart for, who will be even more humiliated than you are because it’s her skit that you are messing up! Run away! Run away! My stomach clenches. Cold sweat starts out on my brow.

TIFFANY: Murphy! Your shoelace! (glancing down) I have forgotten to untie it, which is the key to one of my first funny bits. I lift my foot to take care of the lace. At that instant the curtain opens, which startles me so much that I lose my balance and fall over, landing onstage in full view of the audience. There they are. The enemy. The people who are going to stare at me, judge me, whisper about me tomorrow. I am so frozen with terror I cannot move.

This is it, I will never be able to face another living human being.

TIFFANY: (whispering) Murphy, are you all right?

(is startled out of his frozen terror and speaks to the audience) For the sound of that voice, I would do anything! (He turns to the invisible door of the script and fake knocks) Knock-knock. Knockity-knock-knock. To my surprise, the audience finds this funny. Tiffany comes to the door, and we go through our opening business. But something is happening. I’m not making up lines, but I am making bigger gestures, (gestures broadly) broader moves, weirder voices than I did in rehearsal. People are howling. I am a genius! Who is this funny person, making everyone laugh? (with a flourish he shakes out the cloth napkin . . . and blows his nose in it – He inspects the results and is fascinated by the imaginary boogers) The audience is just about screaming. This kind of laughter is even better than the sound of Tiffany’s voice. Laurel comes back with our “order” which, because this is a skit and we are on a low budget, is a plate of Hostess cupcakes. Chocolate. I am supposed to eat in a disgusting way.

(picks up a cupcake and stuffs it whole into his mouth.) I deliver my next line – which is about how beautiful she is – with bits of chocolate spewing out. It’s disgusting but hilarious. Desperate to keep the riff going, I cram another entire cupcake in my mouth. This is when disaster strikes. Suddenly, I discover that I can’t breathe because there is a chocolate logjam in my throat. I try to give my next line, but nothing comes out. Which is when Mikey comes barreling on stage from behind me, screaming, “He’s choking! He’s choking!” Then he grabs me around the waist and jabs his fists into my belly. I’ve been Heimliched! Those of you who know about the Heimlich maneuver will remember that basically it forces the air out of your lungs, blowing whatever is blocking your breathing out of your mouth. Those of you who have been staging this in your mind as you read will remember who is directly across from me. Those of you with even minimal powers of prediction will know what happens next. An unholy mix of partially chewed Hostess chocolate cupcakes spews out my mouth and spatters all over Tiffany. I am filled with deeper horror than any I have ever known. Wrenching my way out of Mikey’s grasp, I bolt around the table to clean her off. Unfortunately, the table is close to the edge of the stage. Too close. Tripping over my untied shoelace, I hurtle headfirst into the darkness. (Beat) Okay, I probably could have accepted the broken leg. I might even have been able to live with the memory of the look on Tiffany’s face. But when Mikey told me that my fly had been open during the entire fiasco, that was too much! Anyway, that’s how I ended up in this hospital bed, staring at my right leg, which is up in traction.

MIKEY: Tough luck, Murphy. I try to remember that he is my friend and really thought he was saving my life when he Heimliched me. It is not easy.

MIKEY: Cheer up. It couldn’t get worse than this. (Makes a disgusted face) Right . . . . After all, my name is still Murphy Murphy. And I am thirteen years old. I don’t even want to think about what might happen next week.
```

---

## IC-2516: Where You Can Stick the Sticker Price

- Title: Where You Can Stick the Sticker Price
- Author (byline): Dave Barry
- Work: Dave Barry Talks Back
- Publisher: Three Rivers Press
- Publication date as stated: May 1992
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SALESPERSON, MANAGER
- Teaser before the introduction: Yes
- Spoken words (computed): 1089
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Barry
Book: Dave Barry Talks Back
ISBN: 978-0517588680
Publisher: Three Rivers Press
Date (Month/Year): May 1992
```

### Introduction (context only: never use it for content warnings)

```text
Where You can Stick the Sticker Price by Dave Barry
```

### Performance text (classify this)

```text
To a car salesman, selling cars is a game of strategy. And as in any strategic game, the more you know about your opponent, the better. When you are at a dealership, the car salesman will ask you lots of questions in order to learn as much about you as he can. So to even the score, here are four important facts that you should know about him: 1. He needs you more than you need him. The car salesman is under a lot of stress. Since he works on commission, he doesn't eat or pay his rent if he doesn't sell a car. That's a lot to live with. In addition, his Sales Manager is constantly pressuring him to sell, sell, sell. 2. He is not really in control. The car salesman operates under the illusion that he is in control of the car-buying situation, that he's running the show. He's confident and smooth. Yet in actuality, you have the final say. He knows that, at any point, you can simply say "no" and just walk away. 3. No matter what he says or does, it's probably all an act. The car-buying situation is very theatrical. The car salesman is very much an actor. And it's safe to assume that much of his salesmanship and his lines and even his "sincerity" are, often, simply part of his performance. So do yourself a favor - don't fall for any of it. 4. He can't be fully trusted. When you ask the car salesman a question, he may give you an honest answer. Or he may lie. Or he may say he doesn't know the answer because he really doesn't know. Or he may say he doesn't know because he wants you to think that he's not as smart as he really is. So to protect yourself, it pays to never fully trust any car salesman no matter how friendly you may get with him and no matter how much you like him.

.

We are attempting to purchase a new car, and I have just one teensy little question: WHY WON”T THEY TELL YOU HOW MUCH IT COSTS? I mean, let’s say you’re in the market for a rutabaga. You go to the supermarket and there, plain as day, is a sign stating the price of the rutabaga, allowing you to decide instantly whether it is in your price range. If it is, you simply pay the amount and take your rutabaga home, and you hurl it into your garbage disposal. At least that’s what I would do, because I hate rutabagas. But when you walk into a car dealership, you are entering Consumer Hell. There is no easy way to find out what the actual true price of any given car is. Oh, sure, there is a “sticker price,” but only a very naïve fungal creature just arrived from a distant galaxy would dream of paying this. In fact, federal law now requires that the following statement appear directly under the sticker price: WARNING TO STUPID PEOPLE: DO NOT PAY THIS AMOUNT. The only way to find out the real price is to undergo a fraternity-style initiation. First you squint at the sticker, which lists the car’s 163 special features, none of which you could ever locate on the actual car because they all sound like rocket parts, as in “transverse-mounted induced-torque modality propounders.” Then a salesperson comes sidling toward you in an extremely casual fashion (do not attempt to escape, however; an experienced car salesperson can sidle great distances at upwards of 45 miles per hour) and chatters on a length about the many extreme advantages of whatever car you are looking at (“It has your obverse-shafted genuine calfskin bivalve exuders”). But if you ask him the true price, he will make some vague, Confucius-type statement like: “Dave, we are definitely willing to go the extra mile to put a smile on your face.” “But how much does it cost?” you say. “Dave,” he says, lowering his voice to indicate that you and he have become close personal friends. “Frankly, Dave, (name of whatever month it is) has been a slow month, and I think, Dave, that if we sit down and cut bait, we can come up with a number that we can play ball with.” “WHAT number?” you say. “TELL ME THE NUMBER.” “Dave,” he says, “I think if we both pull on our oars here, we can put the icing on the cake while the iron is still hot.” The easiest solution, of course, is to simply pull out a loaded revolver and say, “Tell me how much this car costs or I will kill you,” but unfortunately it is still a misdemeanor in some states to shoot a car salesperson. So eventually you have to start guessing at the price (“Is it more than $9,500?”). It is very similar to the childhood game Twenty Questions, only it takes much longer, because instead of saying “yes” or “no,” the salesperson always answers: “Let me talk to my manager.” The manager is comparable to the Wizard of Oz, and omnipotent being who stays behind the curtain and pulls the levers and decides whether or not the Cowardly Lion will get a free sunroof. I have never heard a conversation between a manager and a salesperson, but I assume it goes like this:

SALESPERSON: He wants to know if it’s more than $9,500. Can I tell him?

MANAGER: How many times have you called him “Dave”?

SALESPERSON: 1,672 times

MANAGER: Not yet. So it can take hours to determine the true price, and this is just for one car. If you want to find out the price of another brand of car, you have to go through the entire fraternity initiation all over again. And there are hundreds of brands of cars out there. Thousands of them. Back when I was a child and Abraham Lincoln was the president, there were only about four kinds of cars, all of them manufactured by General Motors, but how you see new dealerships springing up on a daily basis, selling cars you never heard of, cars whose names sound like the noise that karate experts make just before they break slabs of concrete with their foreheads (“Hyundai!!”). So far, the cars we have looked at include, the Mimosa Uhuru 2000-LXJ. The Mikado Sabrina Mark XVIXMLCM, the Ford Peligroso, which is actually the same as the Chevrolet Sombrero, the Jeep Violent Savage, and the Chrysler Towne Centre Coupe de Grace, which is manufactured partly in Asia (engine, transmission, body) and partly in the United States (ashtray). They are all fine cars, but at the present time, based on our discussions with the various salespersons, we find ourselves leaning toward the rutabaga.
```

---

## IC-2517: Winning and Losing

- Title: Winning and Losing
- Author (byline): Donald Davis
- Work: Ride the Butterflies, Pg 23-38
- Publisher: August House
- Publication date as stated: Dec 2005
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: DONALD, MOTHER, MR. UNDERHILL, CARRIE BOYD, DADDY, MR. BOYD
- Teaser before the introduction: Yes
- Spoken words (computed): 1412
- Already set (do not supply): none

### Source block (context only)

```text
Author: Donald Davis
Book: Ride the Butterflies, Pg 23-38
ISBN: 978-0874836066
Publisher: August House
Date (Month/Year): Dec 2005
```

### Introduction (context only: never use it for content warnings)

```text
Donald Davis was born in 1944 in a Southern Appalachian mountain world rich in stories. His career as a storyteller has carried him all over the nation and the world. But his stories never stray far from his family who have occupied the same land in Haywood County, NC for over two centuries. In this selection Mr. Davis takes us back to a simpler time – 1950 . . . when a six-year-old learns his first lesson about

Winning and Losing by Donald Davis
```

### Performance text (classify this)

```text
DONALD: (Pg 23-24) For six years I had waited for this day to arrive. I was going to school! It was Tuesday, the day after Labor Day. Mother got me up with orders to take a bath.

MOTHER: You’ve got to at least start out clean. We don’t want any of the teachers to get you mixed up with those nasty short-necked Rabbit Creek boys.

DONALD: So I was scrubbed, then dressed in a brand-new pair of blue jeans so stiff I could barely move my knees. (demonstrate) Every time I tried to sit down, they tried to stand me up again! The outfit was topped off by a new shirt with a collar that felt like the edge of a tin can.

(move neck uncomfortably)

Daddy drove Mother and me to Sulpher Springs School on his way to work – a school that looked like a school in a story book. All red brick with three sets of tall, white columns. Mother and I went into the auditorium for the assembling of new first graders. I had never seen such a big room. (look around in awe) It was bigger than the inside of our church!

DONALD: (Pg 24-25) There were rows and rows and rows of wooden seats with curved backs and seat bottoms which folded up and down making a loud “clunk” each time you dared move them. Mother and I were almost exactly in the center of our row. We were not alone. On this day there were more than a hundred new first graders, more than a hundred mamas and, I think, three daddies. Our row was packed.

Finally the stage curtain began to open. There, standing center stage was Mr. Lonnie Underhill. [He] began to welcome us to the first grade and tell us all the things we needed to know for success at Sulpher Springs School: School spirit, behavior rules, school buses, how to pay for lunch, rules about vaccinations and absences. Mr. Underhill’s speech went on and on and on.

At last, he began to introduce the first-grade teachers. First was Miss Caldwell. It was the first of four good, long, substantial introductions we were to hear that day.

MR. UNDERHILL: . . . Miss Caldwell was just born with teaching right in her blood.

DONALD: (Begin to wiggle, cross legs) About this time, I began to realize I did not know where the bathroom was. Even if I had known . . . trapped in the very center of row G, there was no way out! Mr. Underhill finished his last introduction. Maybe we’ll get to go now.

MR. UNDERHILL: (Pg 26-27) Now, children. We still have a lot of housekeeping to take care of. We have to call the roll.

DONALD: With every name he called, the bathroom crisis got worse. (uncomfortableness increases)

MR. UNDERHILL: Setzer . . . Smith . . . Summey . . .

DONALD: I could not possibly be dry by the time we got out of this place! I began to try every trick I could think of to relieve the pain in my bladder. (tighten hand into fist, grit teeth, hold breath) In desperation I tried to think of something good about all this. Suddenly I got it! I am wearing brand-new, dark blue, unfaded blue jeans. I won’t look nearly as wet in these as I would in old, faded jeans!

Mr. Underhill and the teachers had finished calling the roll and determined that all students from Patricia Abernethy to Thoms Greene will be in Miss Caldwell’s room. That’s me! If we go now, I can make it! But it was not to be. It was time for Mr. Underhill’s first-day-of-school principal speech.

MR. UNDERHILL: Life, boys and girls, is made up of two things: WINNING and LOSING.

DONALD: He was right, and I was about to lose . . .

MR. UNDERHILL: The most important thing is that you do a lot more losing than winning. But, once in a while you do get to win. And when that time finally comes, it is so good that you forget all about the losing you did to get there.

DONALD: I began my own version of losing --first a drop, then a trickle, then a little squirt. Then I thought, If you’re going to wet your pants, go ahead and do it right! So I did! (wets pants with a sigh of pure relief; looks down) The new blue jeans had worked! I looked completely dry. If I could slip out of here sideways, with my back to the wall, no one would ever know. [Except. . ]

The floor of the auditorium sloped from the back toward the front. I could see kids in front of me punch one another as they looked down and pointed at the mysterious stream of water making its way down the sloping floor toward the growing puddle that was building into a lake in front of the stage.

Just when I was sure Mr. Underhill would demand to know who that came from, he suddenly dismissed us to our rooms. (wipes brown in relief) (Pg 28) I walked sideways with my back to the wall, certain I was going to make it there and get seated before anyone discovered I was wet. [But] it was necessary to turn momentarily to go into Miss Caldwell’s door. And in that brief unguarded moment . . .

CARRIE BOYD: Look! That little boy wet his pants!

DONALD: I thought I was going to die. She knows!

MR. UNDERHILL: (echoing) Life is made up of winning and losing . . . and there’s a lot more losing than winning.

CARRIE BOYD: (Pg 35) There’s water dripping out of your britches leg! HA, HA, HA!

DONALD: No conscious thought went into what happened next. The reaction her words inspired was much too fast for thought to have been involved. My right hand clenched itself tightly into a hard little fist and shot out – smack! – striking Carrie Boyd full force in the mouth.

The entire room was silent. In the moment before her scream, we heard a little “plunk,” as one of her big front teeth fell out of her ugly mouth.

(Pg 36) I never knew what happened next as Miss Caldwell glided with me all the way to Mr. Underhill’s office. After a short speech, I was deposited in a chair until the bell finally rang and we all went home. Mother knew. I could tell the moment I saw her. I saved myself some time by going to the maple tree in the back yard and breaking off a switch before I even went into the house. Without saying a word, she gave me a pretty good switching right through those wet britches.

MOTHER: You ought to be ashamed of yourself. Now change your clothes and wait for your Daddy to get home.

DONALD: Finally I heard the Dodge come in the driveway. Daddy was home. (heavy sigh – to Dad) Go ahead and whip me and get it over with.

DADDY: I’m not going to whip you. You’ve had enough of that. But you’re going to have to walk up to Carrie Boyd’s house and apologize to her parents for knocking her tooth out.

DONALD: (to Dad almost crying, frantic) No! Please just whip me and get it over with. Whip me every day for a week. Just don’t make me go up there.

DADDY: (points in the direction of the Boyd’s)

DONALD: (Pg 37-38) The Boyds’ house was less than a half-mile from ours but it took me two hours to walk up there. I would take a few steps, then stop to think about it for a while. At last I got to the Boyds’ Mr. Boyd had a yellow Piper Cub airplane which he kept in the hay barn. I knew he would be there working on the airplane. Both Mr. and Mrs Boyd looked at me as I walked slowly into their presence.

My knees would hardly hold, my chin quivered, my eyes filled with tears . . . I stood before them for a long uncomfortable minute while they looked down at me and didn’t say a word. I had never talked to either of them before in my entire life.

(To the Boyds’ -- whimpering) I’m sorry . . . I’m sorry that I knocked Carrie’s tooth out. (crying hard)

The Boyds didn’t say a word. They just looked at one another, at me, at one another again. Then, as if in slow motion, Mr. Boyd reached into his hip pocket and pulled out his wallet. He took out one of the first real five dollar bills I have ever seen close-up.

MR. BOYD: That tooth? That tooth was a baby tooth. It’s been hanging there by a thread for two months. Carrie wouldn’t let either one of touch it. (laughing) Thank you for finally getting that thing out!

DONALD: He handed me the five-dollar bill. Suddenly I remembered Mr. Underhill’s speech, and I knew that he was right. Life is made up of winning and losing, and like he said, “When you finally get to win, it’s so good, you forget all the losing you’ve done to get there!
```

---

## IC-2518: The World and Mr. Chicken

- Title: The World and Mr. Chicken
- Author (byline): Paul Feig
- Work: Kick Me: Adventures in Adolescence
- Publisher: Three Rivers Press
- Publication date as stated: Sept 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1833
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Feig
Book: Kick Me: Adventures in Adolescence
ISBN: 978-0609809433
Publisher: Three Rivers Press
Date (Month/Year): Sept 2002
```

### Introduction (context only: never use it for content warnings)

```text
When I was five, my older brother convinced me that a monster lived under my bed. It didn't matter that I had examined the space between my mattress and floor a dozen times. It didn't matter that there was not a shred of evidence to support his existence. As soon as the lights were turned off, the possibility that a monster could be lurking under my bed transformed into a real and frightening fact. (whispering) – Sometimes I still check . . . just to be sure.

Let’s face it we all have some irrational fear . . . even as adults. But in The World and Mr. Chicken, Paul Feig claims the title as the MOST paranoid and MOST gullible! The World and Mr. Chicken by Paul Feig
```

### Performance text (classify this)

```text
I was a huge chicken when I was a kid.

It's hard to say why, exactly. I mean, most kids are scared of one thing or another, but I just seemed to be afraid of absolutely everything.

Loud noises always scared me. Up until about the age of six, I always reacted to a thunderstorm in the same way: I'd clamp my hands over my ears and refuse to take them off until the thunder stopped, the storm clouds cleared, and the sun came back out. The loud rumbles and claps of thunder sounded to me as if the earth were exploding and about to fall apart, and I guess I figured that if I could keep the sound out of my head, I could somehow make myself exempt from the world's destruction. If it was thundering during a meal and my parents wanted me to eat, one of them would have to feed me by hand because my palms would not leave my ears even if I was on the verge of starvation. I'd put my arms up and elbows out to the sides and clamp my hands so solidly onto the sides of my skull that the Jaws of Life couldn't pry them off. I looked like a human loving cup, the living booby prize for my poor parents, who were quickly discovering that their only child was a neurotic mess.

My first experience in a movie theater went from fun to frightening when my mother took me to a double feature that saw a Winnie the Pooh cartoon inexplicably programmed on the same bill with the Rat Pack's Roaring Twenties bootlegger musical Robin and the 7 Hoods. Sammy Davis Jr. sang, jumped up on a bar, danced a few steps, then pulled out a tommy gun and started firing wildly. As a trucker might say, I was "off like the bride's panties" and cowering in the lobby before Sammy finished his first verse.

Circuses scared the hell out of me, both because performers always seemed to be shooting off giant cannons all the time and because the disturbing, antics of the creepy clowns usually involved blowing something up or hitting each other with exploding sticks that would crack loudly like gunshots. As the kids around me were cheering and laughing at these allegedly comedic exploits, I would fleeing for the parking lot like an extra in a Godzilla movie.

Those clowns also played into another of my major fears: I was afraid of anyone in a costume. A trip to see Santa might as well have been a trip to sit on Hitler's lap for all the trauma it would cause me. Once, when I was four, my mother and I were in a Sears and someone wearing an enormous Easter Bunny costume headed my way to present me with a chocolate Easter egg. I was petrified by this nightmarish six-foot-tall bipedal pink fake-fur monster with human-sized arms and legs and a soulless, impassive face heading toward me. It waved halfheartedly as it held a piece of candy out in an evil attempt to lure me into its clutches. Fearing for my life, I pulled open the bottom drawer of a display case and stuck my head inside, the same way an ostrich buries its head in the sand. Over the next several years, I would run away in terror from a guy in a gorilla suit whose job it was to wave customers into a car wash, a giant Uncle Sam on stilts, a midget dressed like a leprechaun, Ronald McDonald, Big Bird, and Bozo the Clown. Add to this an irrational fear of small dogs that saw me on more than one occasion fleeing in terror from our neighbor's four-inch-high miniature dachshund as if I were being chased by the Hound of the Baskervilles and a chronic case of germ phobia, and it's pretty apparent that I was what some of the less politically correct among us might call-a first-class *wussy*.

Even though I tried to conquer my fears as I went through grade school and junior high, convincing myself that loud noises could be cool when they came in the form of firecrackers blowing up model cars and Led Zeppelin albums turned up full blast, and teaching myself that people in costumes are usually only present when an event is supposed to be "fun," I would still succumb to a fear of anything unknown. Especially if the unknown meant I was potentially going to get my ass kicked. One of the biggest unknowns I feared was high school.

A lot of my more irrational fears as a kid came from the fact that my next-door neighbor Mary and her older sisters used to love to scare the crap out of me. They'd always tell me horror stories about things that would happen if I did something or other. They're the ones who, when we were all at the beach, put the fear of God in me that I might spontaneously combust because "it happened to this kid over on Moravian Drive after he stayed out in the sun too long." They made me paranoid for years about a mythical "sewing bee" that reportedly flew into kids' bedrooms and sewed their mouths and nostrils shut in the middle of the night so that they'd smother to death. And to this day, I'm still afraid to put my cold hands in hot water because they told me if I did, my fingers would fall off. Looking back, I know that they were merely having fun with my perpetual fears and my chronic gullibility. And in the weeks before I was to enter high school, their minds reeled at the opportunity to ruin something I was actually starting to look forward to.

One summer evening, I was sitting with them in the ditch in their front yard listening to seventeen-year-old Becky, the eldest girl in their family, explain to us what hermaphrodites were, she suddenly looked at me and said . . . .(in Becky’s voice) "So, Fig Newton, you're starting high school next month, huh? You better be careful. They don't like freshmen very much." A hot flush immediately went up the back of my neck.

"They don't?" (trying not to sound worried)

"Nope, you should see what they do to freshmen. Sometimes, if you're walking down the hall, a bunch of seniors will grab you, drag you into the bathroom, and give you a swirly.

I looked at Sharon and Mary, who were listening to Becky, wide-eyed. "What's a swirly?"

“It's when they stick your head in the toilet and flush it. Last year, some kid drowned. The year before, another kid got sucked down. They found him in the sewer. Long and skinny and dead."

(feeling faint) "Really?"

"Yeah. But that's nothing," (leaning forward and whispering). "A lot of times, what they'll do is grab a freshman, drag him into the bathroom, and make him eat drugs."

I was now officially in a panic. My dad had just the other night given me the world's most sobering talk about drugs after he and I came across a picture of a hippie shooting up heroin in an antidrug ad in National Geographic.

(in Dad’s Voice) (sighing, pointing at the picture and very adamant) "You see that kid? That kid is the stupidest kid you'll ever see. And you know why he's so stupid? Because what you see him doing, right there, is throwing his life away. Right down the toilet." My father then launched into a one-hour lecture, telling me that if I took drugs, any drugs - if I decided it'd be fun to "get all doped up" - I'd turn into a vegetable. Immediately. And all of a sudden, there I was in the ditch hearing that a group of crazed seniors were going to put me in a coma the minute I entered the school on my first day. I came home very upset.

"Mom! I'm not going to high school. No way!"

"Of course you are. What are you talking about?"

"I'm just not going. Forget it!"

"Why not?"

"Because they're gonna make me eat drugs."

Who is?"

"Seniors. They hate freshmen. This kid was walking down the hall last year and a bunch of seniors jumped him and stuck his head in the toilet and made him eat drugs!"

"Oh, my goodness," my mother said, extremely concerned. "I'll call the school tomorrow."

The next day, my mom told me that she had talked to Mr. Walker, the principal of the high school. Apparently, she tracked down the poor guy's home phone number and bothered him during his summer vacation because of my paranoia.

"I spoke to the principal today,"

(embarrassed)

(as Paul to audience) Clearly he had convinced her that her son was crazy.

"He said he wasn't aware that any of this toilet and drug business was going on but that he'd look into it. He told me to tell you not to worry, though. He said it was probably just a story."

Between my mother's face and my reading between the lines of what the principal said, I immediately felt like the dumbest kid in the world. I started imagining the conversation that must have taken place between my mother and the principal.

"Mr. Walker, my son says that the older boys in your school force the younger ones to eat drugs."

"Um . . . who is your son?"

"Paul Feig."

"Feig? I don't seem to recall the name."

"Well, he's not in high school yet. He starts next month."

"Oh, well . . . I think he's just been told some wild stories by some students having a little fun with him."

"So, you don't think it actually happens?"

"I sincerely doubt it, Mrs. Feig. If the kids have any drugs, I really doubt they're going to waste them on your son."

And then he probably hung up and mentally filed the name "Paul Feig" in the Whining Little Idiots folder.

That night, we had a very loud thunderstorm, and as I lay in bed and listened to the thunder claps rattle my bedroom window I started to hate myself for having spent my life up to that point being such a wuss.

When I got to high school the next month, still nervous and on guard, just in case Becky was right and I was going to be jumped, dunked, and turned into an addict, I found that high school wasn't the jungle I was imagining it would be. After a few days of being looked through like the Invisible Man by sophomores, juniors, and seniors, all of whom were having more fun than I was, I found myself with a new and actually legitimate fear - the fear of being completely ignored. I suddenly wished that even one of the older kids in my school would find me noticeable enough to merit a swirly or a forced meal of their stash.

Because, after all, if people are sticking your head in a toilet or shoving drugs down your throat, at least they're paying attention to you.
```

---

## IC-2519: YMA Dream

- Title: YMA Dream
- Author (byline): Thomas Meehan
- Work: Fierce Pajamas: An Anthology of Humor Writing from The New Yorker
- Publisher: English
- Publication date as stated: October 2002
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1430
- Already set (do not supply): none

### Source block (context only)

```text
Author: Thomas Meehan
Book: Fierce Pajamas: An Anthology of Humor Writing
from The New Yorker
ISBN: 978-0375761270
Publisher: English
Date (Month/Year): October 2002
```

### Introduction (context only: never use it for content warnings)

```text
Dreams are known to reveal the secret desires of the dreamer. Many prophecies have been made through dreams. Dreams made Martin Luther King Jr. famous. Jesus was a dream interpreter. Therapists wouldn’t have bread on the table if not for bizarre and questionable dreams. However, if Tom is expecting his dream to hold relevance in reality, he will find himself increasingly tongue tied. “YMA Dream” by Thomas Meehan
```

### Performance text (classify this)

```text
In this dream, which I have had on the night of the full moon for the past three months, I am giving a cocktail party in honor of Yma Sumac, the Peruvian singer. This is strange at once, for while I have unbounded admiration for four-octave voices, I have never met Miss Sumac, and, even in a dream, it seems unlikely that I should be giving her a party. No matter. She and I are in the small living room of my apartment, on Charles Street, in Greenwich Village, and we are getting along famously. I have told her several of my Swedish-dialect stories, and she has reciprocated by singing for me, in Qyechua, a medley of Andean folk songs. Other guests are expected momentarily. I have no idea, however, who any of them will be. Miss Sumac is wearing a blue ball gown and I am in white tie and tails. Obviously, despite the somewhat unfashionable neighborhood and the cramped quarters of my apartment, it is to be a pretty swell affair. In any case, I have spread several dishes of Fritos about the room, and on what is normally my typing table there is a bowl of hot glugg.

The doorbell rings. A guest! I go to the door, and there, to my astonished delight, is Ava Gardner. This is going to be a bit of a night, I think.

"Tom, darling!" she says, embracing me warmly. "How wonderful of you to have asked me." In my waking hours, unfortunately, I have never met Miss Gardner. In my dream, though, my guests seem to know me rather intimately, while, oddly, none of them seem to know each other. Apparently it is their strong common affection for me that has brought them to Charles Street. For my part, although I immediately recognize each guest as he or she arrives, I have no memory of having ever met any of them, or, for that matter, of having invited them to a party in my apart-ment. On with the dream, however. "Miss Ava Gardner," I say, "I'd like you to meet Miss Yma Sumac." "Charmed," says Miss Sumac.

"Delighted," counters Miss Gardner.

“Ah, but Tom," says Miss Sumac, with an enchanting laugh (which runs up the scale from E above middle C to C above high C), "let us not, on this of all occasions, be formal. Por favor, introduce each guest only by the first name, so that we may all quickly become-how shall I say?-amigos. "

Typical Peruvian friendliness, I think, and reintroduce the two. "Ava, Yma," I say.

We sit around for some time, sipping glugg and munching Fritos. Things seem to be going well. The doorbell rings again. The second guest is a man-Abba Eban, the former Israeli Ambassador to the United Nations. Again I make the introductions, and, bowing to the wishes of the guest of honor, keep things on a first-name basis. ''Abba, Yma; Abba, Ava," I say.

I stifle a grin, but neither Miss Sumac nor my two other guests see anything amusing in the exchange. We chat. The bell rings again, and I am pleased to find Oona O'Neill, Charlie Chaplin's wife, at the door. She is alone. I bring her into the room. "Oona, Yma; Oona, Ava; Oona, Abba," I say.

We are standing in a circle now, smiling brightly but not talking much. I sense a slight strain, but the party is young and may yet come to life. The bell again. It is another man- Ugo Betti, the Italian playwright. A bit hurriedly, I introduce him to the circle. "Ugo, Yma; Ugo, Ava; Ugo, Oona; Ugo, Abba," I say.

Miss Sumac gives me an enigmatic glance that I try to interpret. Boredom? Thirst? No, she looks almost irritated. Hastily, I replenish everyone's glass. For some reason, I begin to hope that no other guests have been invited. The doorbell rings once again, however, and I open the door on two lovely actresses, Ona Munson and Ida Lupino. This gives me a happy inspiration for my introductions. "Ona and Ida," I say, "surely you know Yma and Ava? Ida, Ona-Oona, Abba." Damn! It doesn't come out even. "Ida, Ona-Ugo," I finish lamely.

I have scarcely given Miss Munson and Miss Lupino their first drinks when I am again summoned to the door. My guests stand stonyfaced as I usher in the new arrival, the young Aga Khan. He is looking exceptionally well turned out in a dinner jacket with a plaid cummerbund. Smiling too cheerfully, I introduce him to the waiting group. "Folks," ,I say, using a word I have always detested, "here's the Aga Khan! You know." But there is silence, so I must continue. ''Aga- Yma, Ava, Oona, Ona 'n' Ida, Abba 'n' Ugo."

The Aga Khan and Mr. Eban, I notice, take an immediate dislike to each other, and I begin to feel an unmistakable pall descending over my party. I suggest a game of charades. This is met with glacial looks from everyone, including Miss Gardner, whose earlier affection for me has now totally vanished. When the doorbell rings this time, everybody turns and glares at the door. I open it and discover another pair- Ira Wolfert, the novelist, and Ilya Ehrenburg, the Russian novelist. The latter, I know, is quite a man-of-the-world, so I try a new approach. "Ilya," I say, "why don't you just introduce yourself and Ira? You know all these lovely people, don't you?"

"Nyet," says Mr. Ehrenburg. "Can't say that I do."

"Oh, all right," I say. "Ilya, Ira, here's Yma, Ava, Oona. Ilya, Ira, Ona, Ida, Abba, Ugo, Aga."

I ask Miss Sumac to sing for us. She refuses. We continue with the glugg and some hopelessly inane small talk. Mr. Eban and the Aga Khan stand at opposite sides of the room, eying each other. I begin to wish I'd never given the goddam party. Ona Munson jostles Ugo Betti's elbow by accident, spilling his drink. I spring forward to put them at their ease, whipping a handkerchief from my pocket. "Never mind!" I cry. "No damage done! Ugo, you go get yourself another drink. I'll just wipe this glugg off the, uh, rug."The guests fix me with narrowed eyes. At this moment, Eva Gabor, the Hungarian actress, sweeps through the door, which I have cleverly left open. Unaware of the way things are going, she embraces me and turns, beaming, to meet the others. Inevitably, I must make the introductions. I start rapidly. "Eva, meet Yma and Ava and Oona-" But then I find that Miss Gabor is pausing to hug each guest in turn, so I am forced to make the remaining introductions separately. "Eva, Ona; Eva, Ida; Eva, Ugo; Eva, Abba; Eva, I1ya; Eva, Ira; Eva, Aga."

This is a terrible party. All the men have bunched up. We stand in a circle, glowering at one another. I can think of nothing to say. I feel oddly hemmed in, like a man who is about to be stoned to death.

"Am I late?" asks the actress Uta Hagen gaily as she comes tripping into the room.

"No, no!" I say, gallantly taking her arm and steering her at once toward the punch bowl and away from the others.

"Please have the common decency to introduce your guests to one another," says Miss Sumac, in a cold monotone. "And in the proper manner.”

In the dream, Yma Sumac seems to have some kind of hold over me, and I must do as she wishes. "O.K., O.K.," I snap crossly. "Uta, Yma; Uta, Ava; Uta, Oona; Uta, Ona; Uta, Ida; Uta, Ugo; Uta, Abba; Uta, Ilya; Uta, Ira; Uta, Aga; Uta, Eva." I turn to see if this has placated Miss Sumac. But she coldly ignores me. I have begun to hate her. Then I discover that the glugg has run out, and I am forced to offer my guests rye and-7- Up. In the hope that no further company will arrive, I silently close the door. The bell rings instantly, however, and I feel a chill run down my spine. I pretend not to hear it.

“Answer the door," Miss Sumac says peremptorily. My circle of guests moves menacingly toward me. With a plummeting heart, I open the door. Standing before me, in immaculate evening dress, is a sturdy, distinguished-looking man. He is the Polish concert pianist Mieczyslaw Horszowski.

"Come in, Mieczyslaw!" I cry, with tears in my eyes. "I've never been so glad to see anyone in my whole life!"

And here always, my dream ends.
```
