# Classification request: batch 9 of 63 (40 records, IC-0321 to IC-0360)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-009-reply.json`.

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

## IC-0321: The Boogeyman

- Title: The Boogeyman
- Author (byline): Stephen King
- Work: Night Shift
- Publisher: Signet Books
- Publication date as stated: Dec 1994
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LESTER
- Teaser before the introduction: Yes
- Spoken words (computed): 1766
- Already set (do not supply): none

### Source block (context only)

```text
Author: Stephen King
Book: Night Shift
ISBN: 978-0451170118
Publisher: Signet Books
Date (Month/Year): Dec 1994
```

### Introduction (context only: never use it for content warnings)

```text
Meet Lester Billings of Waterbury, Connecticut. According to his history taken by Nurse Vickers, he is twenty-eight, employed by an industrial firm in New York, divorced, and the father of three children. All deceased.

This is Lester’s story – also known as The Boogeyman by Stephen King.
```

### Performance text (classify this)

```text
LESTER: (Pg 100-114) I came to you because I want to tell my story, I can't go to a priest because I’m not Catholic. I can't go to a lawyer because I haven't done anything to consult a lawyer about. All I did was kill my kids. One at a time. Killed them all. Denny in 1967. Shirl in 1971. And Andy this year. I want to tell you about it.

LESTER: I married Rita in 1965-I was twenty-one and she was eighteen. She was pregnant. That was Denny. I had to leave college and get a job, but I didn't mind. I loved both of them. We were very happy.

Rita got pregnant just a little while after Denny was born, and Shirl came along in December of 1966. Andy came in the summer of 1969. Denny was already dead by then. Andy was an accident. That's what Rita said. She said sometimes that birth-control stuff doesn't work. I think that it was more than an accident. Children tie a man down, you know. Women like that, especially when the man is brighter than they. It doesn't matter, though. I loved him anyway.

The boogeyman killed them all. Just came out of the closet and killed them. You think I’m crazy. It's written all over you. But I don't care. All I want to do is tell you and then get lost.

It started when Denny was almost two and Shirl was just an infant. He started crying when Rita put him to bed. We had a two-bedroom place, see. Shirl slept in a crib in our room. At first, I thought he was crying because he didn't have a bottle to take to bed anymore. Rita said don't make an issue of it, let it go, let him have it and he'll drop it on his own. But that's the way kids start off bad. You get permissive with them, spoil them. Then they break your heart. Get some girl knocked up, you know, or start shooting dope. Or they get to be sissies. Can you imagine waking up some morning and finding your kid-your son-is a sissy?

After a while, though, when he didn't stop, I started putting him to bed myself. And if he didn't stop crying I’d give him a whack. Then Rita said he was saying 'light' over and over again. Well I don't know. Kids that little, how can you tell what they’re saying. Only a mother can tell.

Rita wanted to put in a nightlight. One of those wall-plug things with Mickey Mouse or Huckleberry Hound or something on it. I wouldn't let her. If a kid doesn't get over being afraid of the dark when he's little, he never gets over it.

Anyway, he died the summer after Shirl was born. I put him to bed that night and he started to cry right off. I heard what he said that time. He pointed right at the closet when he said it. 'Boogeyman," the kid says. 'Boogeyman, Daddy.'

I turned off the light and went into our room and asked Rita why she wanted to teach the kid a word like that. I was tempted to slap her around a little, but I didn't. She said she never taught him to say that.

That was a bad summer for me, see. The only job I could get was loading Pepsi-Cola trucks in a warehouse, and I was tired all the time. Shirl would wake up and cry every night and Rita would pick her up and sniffle. I tell you, sometimes I felt like throwing them both out a window. Christ, kids drive you crazy sometimes. You could kill them.

Well, the kid woke me at three in the morning, right on schedule. I went to the bathroom, only a quarter awake, you know, and Rita asked me if I’d check on Denny. I told her to do it herself and went back to bed. I was almost asleep when she started to scream.

I got up and went in. The kid was dead on his back. Just as white as flour except for where the blood had . . . had sunk. Back of the legs, the head. His eyes were open. That was the worst, you know. Wide open and glassy, like the eyes you see on a moosehead some guy put over his mantel. Like pictures you see of those gook kids over in Nam. But an American kid shouldn't look like that. Dead on his back. Wearing diapers and rubber pants because he'd been wetting himself again the last couple of weeks. Awful, I loved that kid.

Rita was screaming her head off. She tried to pick Denny up and rock him, but I wouldn't let her. The cops don't like you to touch any of the evidence. I know that-

The closet door was open. Not much. Just a crack. But I knew I left it shut, see.

We moved Shirl into Denny's old room a month after the funeral. Rita fought it tooth and nail, but I had the last word.

It hurt me, of course it did. Jesus, I loved having the kid in with us. But you can't get overprotective. You make a kid a cripple that way. Life goes on. Shirl went right into Denny's crib. We sent the old mattress to the dump, though. I didn't want my girl to get any germs.

So, a year goes by. And one night when I'm putting Shirl into her crib she starts to yowl and scream and cry. 'Boogeyman, Daddy, boogeyman, boogeyman!” That threw a jump into me. It was just like Denny. And I started to remember about that closet door, open just a crack when we found him.

The boogeyman got her, too. A month later. But something happened before that. I heard a noise in there one night. And then she screamed. I opened the door real quick-the hall light was on-and . . . she was sitting up in the crib crying and . . . something moved. Back in the shadows, by the closet.

When she died I found her, see. And she was black. All black. She swallowed her own tongue, and she was staring at me. Her eyes, they looked like those eyes you see on stuffed animals, all shiny and awful, like five marbles, and they were saying it got me, Daddy, you let it get me, you killed me, you helped it kill me . . .

Rita still loved me. Oh, she was sort of colorless the first four or five months after - dragged around the house, didn't sing, didn't watch the TV, didn't laugh. I knew she'd get over it. When they're that little, you don't get so attached to them. After a while you have to go to the bureau drawer and loot at a picture to even remember exactly what they looked like.

So, what's next? She's knitting little things, singing in the shower, and eating pickles like crazy. Sitting on my lap and saying things about how it must have been God's will. The baby came at the end of the year after Shirl's death. That's right. A boy. She named it Andrew Lester Billings. I didn't want anything to do with it, at least at first. My motto was she screwed up, so let her take care of it. I know how that sounds but you have to remember that I'd been through a lot.

But I warmed up to him, you know it? He was the only one of the litter that looked like me, for one thing. Denny looked like his mother, and Shirl didn't look like anybody. But Andy was the spitting image of me.

That next year was the best one for us. I’d give every finger on my right hand to have it back again. But this last year wasn't so good. Something about the house changed. I started keeping my boots in the hall because I didn't like to open the closet door anymore. I kept thinking: Well, what if it's in there? All crouched down and ready to spring the second I open the door?

Andy died in February. Rita wasn't there. She got a call from her father. Her mother had been in a car crash the day after New Year's and wasn't expected to live. She took a bus back that night. It was all right when Rita was there, but when she was gone, it started to get bolder.

You'd wake up at three in the morning and look into the dark and at first you'd say, 'It's only the clock.' But underneath it you could hear something moving in a stealthy way. But not too stealthy, because it wanted you to hear it. And you'd close your eyes, knowing that hearing it was bad, but if you saw it.

And always you'd be afraid that the noises might stop for a little while and then there would be a laugh right over your face and a breath of air like stale cabbage on your face and then hands on your throat.

The kid was sleeping in the room with me. I didn't want to move him. I was afraid to, after Denny and Shirl. But with Rita gone, I moved him. I knew it would go for him, see. Because he was weaker. And it did. That very first night he screamed in the middle of the night and finally, when I got up the courage to go in, he was standing up in bed and screaming. 'The boogeyman, Daddy. . . boogeyman . . . wanna go wif Daddy, go wif Daddy.”

But I couldn't. I couldn't! And an hour later there was a scream. An awful, gurgling scream. And I knew how much I loved him because I ran in, I didn't even turn on the light, I ran, ran, ran, oh, Jesus God Mary, it had him; it was shaking him, and I heard . . . I heard it when Andy's neck broke.

When it was over, I called the police. He was lying on the floor and staring at me. Accusing me. A tiny bit of blood had run out of one ear. Only a drop, really. And the closet door was open-but just a crack.

I lied to the police, see? Told them the kid must have tried to get out of his crib in the night and . . . they swallowed it. Course they did. That's just what it looked like. Accidental. like the others. But Rita knew. Rita . . . finally . . . knew. . .
```

---

## IC-0322: Born Guilty

- Title: Born Guilty
- Author (byline): Ari Roth
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Jan 1994
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: RUDOLF
- Teaser before the introduction: Yes
- Spoken words (computed): 1077
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ari Roth
ISBN: 978-0573694882
Publisher: Samuel French, Inc.
Date (Month/Year): Jan 1994
```

### Introduction (context only: never use it for content warnings)

```text
“Born Guilty” is a play based on a 1988 oral history by Peter Sichrovsky, a Jewish journalist and a child of Holocaust survivors who, after growing up and playing with children of former Nazis, decided to start asking them what their daddies had done during the war and simply tape-record their answers. "Born Guilty" was published to international acclaim for its insightful portraits of deeply complex and conflicted people, whose damaged psychology, previously ignored, was both frightening and telling. What do the children of murderers look like? They look like us. We are all . . .

Born Guilty by Ari Roth
```

### Performance text (classify this)

```text
RUDOLF: Come, Peter. Enough questions. I want to ask one of you now. Do you ever get nightmares? You know the ones. Big? Black? Lacerating? What do you do with them? I’ve been to doctors, therapists, specialists: “Come to terms,” they say. Yes, but whose? No terms exist, wouldn’t you agree?

RUDOLF: Always at night, they come, tear me out of bed, push me into a car, men in uniforms. We stop at a house. I’m shoved down stairs into a room. A white room. I’m handed a towel and cake of soap. They rip off my pajamas. Doors lock. I look up, I see them: Shower heads. And through the holes, a hisssssssss. Fall to the floor. Soap cake turning to Zyklon. Trouble breathing. Beginning to choke. Rush for the door, try to open it, bang on it, silent scream, eyes are burning. Fingernails. Excrement. Tractor ploughs. My parents eating cheesecake. I wake up. As soon as I close my eyes it starts again – shower heads, fingernails, cheesecake.

Well? What am I? Hero? Villain? Victim? Murdered? I think I ‘m a murderer, and do I get any congratulations for it, hmmmm? What about you? You think I’m a fraud, don’t you? Tell me, Peter. Does the name “Project Reinhard” ring a bell? . . . I thought it might. Can you imagine, growing up in South America surrounded by Einzadst Reinhard!? German schools, German book store, German tavern, German butcher, all in the middle of a jungle!

All the money came from “Reinhard.” Fake names. Fake passports. By the time I was ten, it has moved us four times. Then one day, they stopped looking for us, we were no longer dangerous. We were allowed to settle into a nice little villa, surrounded by nice little slaves – I can’t tell you where exactly, it’s too horrible, how we ruined them; Oh, those poor little brown people. Overnight, we had become victors. Eternal spring, fertile soil. Is this more what you’d like to hear?

A paradise, that’s what it was. But I was fat. A real officer’s kid. “Why was I born?” Hmmmm? Have you ever asked yourself? Where did our parents get the insane notion to make a child? This was the question asked by Jodl after he was sentenced to death at Nuremberg. Quite a question.

I have read everything from that trial, eight thousand pages. Of all the defendants, Hans Frank I believe is the only one to have voiced any regret. I often try to imagine what father would have said, “What’s all the excitement about?” He didn’t do anything. “Driving into a village? Rounding up some Poles? Walk to a clearing, men here, women there. Men dig a trench and the women pile their clothes?” Once, one single time, my father was drunk enough to talk about it, how terrible it had been, that time they had to shoot the children one by one with a hand-gun because those idiotic soldiers had aimed their rifles too high. “Oh my God!” he sobbed “What bad times those were!” How he loved to whine . . In his will he requested to be buried in Germany, but I prevented it. No more orders. He used to whip me repeatedly for even the slightest provocation. I remember once, he discovered some money missing. Not much. He used to throw change in a bowl for tips and now it was gone. Well, he decided he was going to show us who was Boss! So one night he called in The Slaves. One by one, he told them they had “one hour to report the culprit or they’d all be fired!” I was twelve at the time. Slowly, I raised my hand. I suggested that maybe dear papa might be mistaken: Perhaps it was I who had taken the money . . . ! Father turned birght red. He sent them out, all the while cursing them. “HOW DARE YOU? HOW DARE YOU?” And you know why he was so upset? Because I’d said it in SPANISH. “Dejelos solos; Yo lo hice; Y fui el que tome eldinero!” I’d humiliated him in front of The Help! My first puny triumph.

By the time I was fifteen, I had gotten quite good at it. I’d lost twenty pounds. Suddenly I had a lot of friends. I would hitch-hike into town. I could have anyone I wanted. Back then, of course. You know what mother said? “Twenty years ago they would have pinned a pink triangle on you!” My father, he just wanted to kill me, or maybe himself first, then me. It was all over for German honor, that’s for sure. No more beer in the taverns. No more chairman of the annual carnival committee. They crawled into their shells. Once I realized, I became completely uninhibited. I brought friends over, left magazines under the bed so they could find them. I dressed like a fag, talked like a fag, “especially if a visitor ever came to the door!” I really let ‘em have it. You should have seen. I was kicked out of school for sexual molestation, it was beautiful! My father was called to the principal’s office. I think it was the second worst day of his life! I am convinced that anything, even being charged with Crimes Against Humanity, would have been preferable. But his son A FAGGOT!?

You see, here’s my theory: I think he drove into that tree on purpose. “Burned beyond recognition” That’s what was written on the report. And it was gorgeous. Absolutely gorgeous. A fireball. An atomic blast. Unfortunately, I didn’t see it. But I was there. The night after the funeral I went back to the cemetery and pissed on his grave, trampled on it, cried, went crazy. I was my own personal farewell. The next day, I waited for friends to call. Nothing. No cake, No congratulations. Did even on of those creeps tell me how much they admired me?

So I sold everything and came to Berlin. After all, I still had my German passport, and all the money I needed. I still don’t have to work, and I don’t. I don’t work. I haven’t done a thing in fifteen years except read about the Third Reich, and what’s wrong with that, hmmmm? Who reads anymore? Just us. Over and over I come across my father’s name, his old one. I don’t think I can mention it here. It stays with me – a deeply buried secret.
```

---

## IC-0323: Bottleman

- Title: Bottleman
- Author (byline): Eric Bogosian
- Work: Sex, Drugs, Rock & Roll, Pgs 45-50
- Publisher: Theatre Communications Group
- Publication date as stated: Sept 2008
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BOTTLEMAN
- Teaser before the introduction: No
- Spoken words (computed): 1044
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Bogosian
Book: Sex, Drugs, Rock & Roll, Pgs 45-50
ISBN: 978-1559361248
Publisher: Theatre Communications Group
Date (Month/Year): Sept 2008
```

### Introduction (context only: never use it for content warnings)

```text
This past Monday, 36,782 homeless people spent the night in a New York City shelter; the number who slept on the street is impossible to ascertain. Homeless men and women are part of an expanding, often faceless community. When we come in contact with a homeless person, we may feel repulsed, annoyed, even angered as we avert our eyes and think, "Why don't they do something to help themselves?" or "If I look them in the eye, that'll just encourage them to ask me for money" or "They choose to be homeless." Frequently, it is our lack of understanding about the complexities of homelessness that fuels our prejudices and fears about homeless people. Somehow, that gives us "permission" to act less compassionately towards a homeless person — who is, after all, a human being just like us.

I’d like to introduce you to Bottleman by Eric Bogosian
```

### Performance text (classify this)

```text
(A man talks quickly, nervously, rarely looking at the audience. He constantly hitches his pants and pats his hair. His over cheerful manner covers his fear. He’s making conversation with an imaginary listener. He begins by talking to the wall.)

BOTTLEMAN: (PG 45-50) I don’t like to complain. I’m not a complaining kind of guy, I’m a happy kind of guy – runs in my family, happiness. Never been sick in my life. Not one day. Unless you count broken bones, which I don’t. But I like to stay positive. Stay on the sunny side of the street. You give me a pack of cigarettes, egg salad sandwich, cup of coffee, a newspaper, someplace to sit down, and I’m happy – I’m happy.

I don’t even need the cigarettes, I should quit anyway. It’s a dirty habit. Unhealthy. Expensive. Of course you can always find cigarettes. People always have cigarettes – they’ll give ‘em to you. Food’s another subject altogether. People aren’t exactly walking around with an egg salad sandwich in their pocket – unless they’re crazy! And you figure, egg salad sandwich’s gonna run you maybe seventy-eighty bottles. I’m findin’ maybe fifty bottles a day – you’re talking a short-fall of about twenty bottles. . . or cans . . . bottles or cans, it doesn’t make much difference.

Back in the old days, I used to weigh a lot more than I do now. Used to be on a diet all the time. Always trying to lose weight. I don’t have that problem anymore. I’m on the egg salad sandwich diet now. One egg salad sandwich every two days . . . you lose weight like crazy. The fat just flies off . . . and it stays off. I’m gonna patent it. Get a copyright and put an ad in the newspaper. Make a little money.

See, newspapers – newspapers, you can get. You can always find a newspaper, people just leave ‘em around. And I read ‘em. I wanna know about the world.

It’s important to stay informed. I read about a train in Japan goes three hundred miles an hour, gets you there in no time. They got hotels for cockroaches now, hotels for mice. I stay away from hotels. Too much money – who’s got that kinda money? Then bucks a night, forget it. You figure that’s two hundred bottles – bottles or cans – and that’s not in my budget.

But it’s not a problem. You can always find someplace – there’s always someplace to stay. You wedge yourself in someplace. The real problem is the concrete. The stone. They make everything out of rocks and cement! Too hard. Whatever happened to wood? Used to be all the buildings were made out of wood. Used to make benches outa wood. But no more. Because they make wood outa trees, and trees, they don’t got them no more.

I saw this tree . . . there was this tree, beautiful tree . . . they dug a hole and put it in the sidewalk. Every day I come to say hello. And this guy was backing up his truck. The truck was making that beep sound – beep-beep-beep-beep—right over the tree, That was it for the tree. That was it. What are you gonna do? It’s just in the nature of a tree that if you run ‘em over they die. They’re not like people – they can’t take the abuse.

Take a tree, replace it was a metal pole, then there’s no problem. Truck hits the pole, that’s it, But you lose the leaves. You lose the leaves and the twigs. You lose the wood. Wood is good.

Dogs like wood. I know – I used to have a dog. Walked him every day. I used to say (miming walking the dog) “Come on! Come on! . . . Who takes care of you? Who takes care of you? I take care of you. Who’s gonna take care of me in my old age? Who’s gonna take care of me?” That’s what I used to ask him . . .

He ran away. But that’s okay – they gotta eat too, the little ones. Everybody’s gotta eat, sooner or later. It’s human nature. It’s human nature. I like to eat. I like to eat. Kind of a habit of mine, food.

(he holds an imaginary sandwich before his face) Nice egg salad sandwich. Cup a coffee . . . Cream. Sugar.

I’m cutting down on the coffee. I don’t drink much coffee these days. Sixty cents a cup. Where did they come up with that figure, that’s the question I want to ask. Should be ten cents! But they got ya, see, they got ya. ‘Cause they got the beans. They got the beans. You got no choice. They got a cartel. This OPEC.

But I don’t need coffee. I don’t need the coffee. People drink coffee to stay awake – I don’t need to stay awake. I’m awake, I’m awake. When I’m asleep I’m awake. You gotta keep your eyes open when you’re sleeping, ‘cause you find a place to lie down and you don’t keep your eyes open and a guy comes back with a baseball bat and that’s it – bang, bang, you’re dead!

No more coffee, no more cigarettes – that’s it!

See, these guys on the street, they like to fight. I don’t got that luxury. I’m on my second set of teeth, I’m missing a kneecap, I can’t hear in one ear. I’m like the bionic man without the hardware. I’m no Cassius Clay. I’m no Cassius Clay. (pause) But I stay on the sunny side of the street. I stay on the sunny side of the street. A guy once told me, “Life is like a half a glass of water . . . half a glass of water . . . “ (loses his train of thought; his hand is shaking, holding the imaginary glass)

You got a half a glass a water . . . “And . . . uh . . . you should drink the water,” that’s what he said. . . (sheepish – he didn’t get the saying right – he turns away, then laughs at himself)

No, that isn’t what he said . . . He said . . . he said . . . “Half a glass of water is better than no water at all!” That’s it. “Half a glass of water is better than no water . . . “ (full of energy again)

I look at it this way – I could be living in Ethiopia. Those poor people got it terrible. They got nothing to eat. Starving all the time. They just sit in the sand all day long . . . It’s too sunny, too many flies . . . it’s not for me. It’s not my bag. I prefer it here . . . it’s better here.

(lost in thought, convincing himself)

It’s good here, it’s good. It’s good. Thank God! (pause. He’s just standing, staring at the ground. He snaps out of it – sunny, cheerful again, he addresses the audience.)

Well, I gotta get going, got to get to work. You know what they say: “The early bird catches the can!”

Or bottles . . . bottles or cans, it don’t make no difference . . . It don’t make no difference at all . . .
```

---

## IC-0324: Boy in Hoodie

- Title: Boy in Hoodie
- Author (byline): Daniel MacIvor
- Work: I, Animal, Pgs 25-40
- Publisher: Playwrights Canada Press
- Publication date as stated: Dec 2015
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BOY
- Teaser before the introduction: No
- Spoken words (computed): 1580
- Already set (do not supply): none

### Source block (context only)

```text
Author: Daniel MacIvor
Book: I, Animal, Pgs 25-40
ISBN: 978-1770913424
Publisher: Playwrights Canada Press
Date (Month/Year): Dec 2015
```

### Introduction (context only: never use it for content warnings)

```text
This is the story of the “Dead Cat Kid,” as he’s known by his classmates. He’s fascinated by death — curious about it in a philosophical sense — but he’s not morbid, and he DID NOT kill a cat.

But which is more important, the truth or perception? Boy in Hoodie by Daniel MacIvor
```

### Performance text (classify this)

```text
Outside. Night. A neighborhood. A teenaged boy in a hoodie holds a flashlight to his face.

BOY: (Pg 25-40) Death. Death. Death. Death. Comes. Not. Death comes not because death is already here. Death lives. Life is Death. (He drops the flashlight to his side) “Life Is Death”. As a band. Excellent band name.

I’m standing in Beverly Fitzgerald’s driveway. It’s Saturday night and I’m standing in Beverly Fitzgerald’s driveway looking at the moon. (He looks up)

I’m supposed to be good at math because I got a telescope for my birthday. Because that’s what I asked for. It’s a good one. I could have got a laptop. But I asked for a telescope instead. And now everyone thinks I’m good at math. And because now people who are bad at math are really supposed to be good at math, but just getting taught math wrong, I have to go to a special class. Maybe I’m bad at math because I don’t like math. Maybe I just wanted a telescope and it has nothing to do with math.. Just because a person asks for a telescope doesn’t mean they’re good at math, maybe they’re just depressed. (He looks up)

I remember when my father died. (He looks to us) “I have some bad news.” My mother said that. “I have some bad news.” That’s the first time anybody ever said that to me. . . . Ed has a rainbow on a t-shirt. A rainbow in his brain. You know, dream catchers and pot and a ponytail, a rainbow in his brain. My Mom’s been trying to get him to cut his ponytail for years. It’s not even a ponytail now. It’s more like a skinny grey tail now. It’s okay to me but kind of depressing. Getting old. Shrinking. Turning to dust. He never asked me to call him Dad. I appreciated that. My mom was always “you can call him Dad if you want to.” And this is way after the best-before date for that conversation. Ed doesn’t care. We don’t need to have that conversation. Ed and me have lots of conversations. Conversation. That’s what we call it. Ed says “Perhaps we need to have a Conversation”. Ed’s hilarious. (laughs -- He looks up)

And I’m standing in Beverly Fitzgerald’s driveway and I’m laughing because I’m thinking about something Ed said while we were having a Conversation and I hear: “What’s so funny?” And that’s one of those really hard questions to answer. Like “what are you thinking”. Actually it’s even harder to answer than “what are you thinking” because whatever you’re thinking had better be funny or you’ll look like a knob. And it’s especially hard because you didn’t know anyone could hear you, and that is more especially hard because as soon as you realize someone could hear you, you immediately forget what you laughed at, and most especially it’s a hard question because Beverly Fitzgerald is asking it. And this is when I realize that Beverly Fitzgerald is sitting in the dark on her front step. How long has she been there?

And I say: Oh hey. And she says again: What’s so funny? And I say: Just life, you know, the joke of life you know. We are puppets, we are sheep, as The Down say. And she says: I love The Down.

Beverly Fitzgerald loves The Down? Beverly Fitzgerald is a cheerleader. Beverly Fitzgerald is a cheerleader who goes to church. The Down is the music you put on when you want your used-to-be best friend from grade seven who is now really boring to go home. The Down is the only music my Mom yells “turn that down” at. Even Ed. At first he was all “whatever” but one time he came into my room and he says “How can that music be in any way helpful?” Helpful? I’m not looking for help. If I was looking for help I’d call the Youth Distress Line. I’m not looking for help -- I’m looking for confirmation.

Beverly Fitzgerald loves The Down. Beverly Fitzgerald goes out with college guys. Beverly Fitzgerald is popular. Nobody popular likes The Down. (a moment)

When I was popular I didn’t know what popular was . . . I had a website. It was pictures of cats. Not cute cats or stupid dressed up cats or anything. One time there was this site of cats with stuff on them? Just random stuff. It was hilarious. So I started taking pictures of my cat with like a book on him or a slipper or a mug. The mug was hilarious. They’re pretty good. And one time a picture of a dead cat.

It was just some random dead cat. He was hit by a car. It was just a picture. It was a huge deal. It was on the news. I had to change schools. Why is that better? At least at my old school people knew me. First day at the new school I’m the Dead Cat Kid that nobody knows. Good luck with that. I was cut off. Cut off. That was cold. (He looks up for a moment)

So, I go to this new school. At first it’s like I’m wearing a stay-back-500-feet shirt. At first people are just scared. Then people get curious. The really creepy people start coming around. But they have true-creepiness radar and they can tell when somebody is a cat killer or somebody just took a picture of an already dead cat. So, they just crawl back under the bleachers. Then the more-normal people. They can be good at it. They start out with talking about music or having a laugh. But they really just want answers to questions. To report back to the group. They want the story. The Story of the Dead Cat Kid. (laughs) That’s the album. Drops this Christmas. Walmarts worldwide. (laughs) And I’m the Dead Cat Kid and I don’t know anyone and I’m standing in Beverly Fitzgerald’s driveway and I just found out she loves The Down and her parents are away. She invites me inside. (He looks up for a moment) And I didn’t say “yes” or anything. I just went in. Beverly Fitzgerald gets me a beer from her fridge. I just put it on the counter because I don’t drink. Beverly Fitzgerald’s drinking vodka. And I ask her if she wants to have a conversation and she doesn’t know what that means. So, I explain it to her and she really gets excited. So, we have a conversation but I can tell why she doesn’t call it having a conversation because it makes her get really, really quiet. First she mostly just looked at her hands and then stared at me. Finally she started talking but it wasn’t a conversation it was just her telling a long story about some party she didn’t go to tonight and then she got quiet again.. And I’m in Beverly Fitzgerald’s [house] and her parents are away and she’s maybe more than a little bit drunk and we just had a conversation. And I feel like this: Phew. Phew. That’s the perfect word for the sound because the sound is the word and the feeling all together: Phew. Everything’s going to be okay. Things are going to get normal finally. Things are going to get better than normal. (He holds the flashlight to his face. A moment)

Beverly Fitzgerald threw up. She stayed in the bathroom for a long time. When she came out she had another vodka. She talked about the party again and answered the phone a bunch of times. It seemed like time to leave a couple of times so I got up to go and she walked me to the door. And we were at the door and I turned to her cause I’m not sure to kiss her or hug her to shake hands and she says “Did you kill the cat?” (He turns on the flashlight)

I was just coming round the corner. And I had the flashlight on. On my feet on the sidewalk. Sometimes taking pictures of my feet on the sidewalk. And I stop and I see this thing on the road. And it’s a cat and it’s dead. It must have been hit by a car but there’s no blood and nothing flattened. It’s just like a normal looking cat lying down on the road, but he’s dead. And you can tell he’s dead. And the only way to tell that he’s dead is not by something that’s there–guts or crushed bones–but by what’s not there. Do cats think?

I moved him to the sidewalk after. That’s when I touched him. That’s all. I didn’t kill him. It was just a picture. (He turns off the flashlight)

And Beverly Fitzgerald says “Did you kill the cat?” And I say yes. (He looks up)

Ed says “People see what they see -- you can only be responsible for what you do.” But I say, you can be responsible for what they see. It’ll probably be easier in the end. (He looks at us)

Ed liked the picture. Not like he liked it but he got it. Yeah yeah, get me the Youth Distress Line please it’s an emergency. It’s all good. I can talk to Ed. We’ll have a Conversation about it. My Mom would freak. She hated that picture. She hated it more than anybody. It’s just a picture. Pixilations of pixilations. There’s nothing there. (He looks at us)

And right now Beverly Fitzgerald is on the phone or at a party and she’s telling everyone she talks to and everyone who wants to talk to her what the Dead Cat Kid said.

Monday will be interesting. Could work. For a band. (He holds the flashlight in his face and speaks in a scary voice) Ladies and Gentlemen, put your hands together for “Monday Will Be Interesting”!
```

---

## IC-0325: The Boy in the Striped Pajamas

- Title: The Boy in the Striped Pajamas
- Author (byline): John Boyne
- Work: Not specified
- Publisher: David Fickling Books
- Publication date as stated: Oct 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SHMUEL, BRUNO, SCHMUEL, BURNO, BRUO
- Teaser before the introduction: Yes
- Spoken words (computed): 1731
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Boyne
ISBN: 978-0385751537
Publisher: David Fickling Books
Date (Month/Year): Oct 2007
```

### Introduction (context only: never use it for content warnings)

```text
ATC his is the story of an event seared into the fabric of history. It is a fable told through the voice of a child . . . but it is not for children. The year is 1943. Bruno is 9-years-old and is quite unaware of a place called Auschwitz and the fate of the Jews where were sent there. All he knows is that his father is a soldier. Shmeul is also 9, but lives on the other side of the fence. They form a friendship that crosses dangerous boundaries and can only end in tragedy. And somehow, events are all the more tragic when narrated by those who do not understand. The Boy in the Striped Pajamas by John Boyne
```

### Performance text (classify this)

```text
SHMUEL: (Pg 126) All I know is this. Before we came here I lived with my mother and father and my brother Josef in a small flat above the store where Papa makes his watches. Every morning while we went to school, Papa mended the watches that people brought to him and made new ones too.

SHMUEL: (Pg 126-128) And then one day things started to change. I came home from school and my mother was making armbands for us and drawing a star on each one. Like this (Draws a Star of David in the air). And every time we left the house, she told us we had to wear one of these armbands.

BRUNO: My father wears one too . . . on his uniform. It’s very nice. It’s bright red with a black-and-white design on it. (Draws a swastika in the air)

SCHMUEL: Yes, but they’re different, aren’t they?

BRUNO: No one’s ever given me an armband.

SHMUEL: But I never asked to wear one.

BRUNO: All the same, I think I’d quite like one. I don’t know which one I’d prefer though, your one or Father’s.

SCHMUEL: We wore the armbands for a few months, and then things changed again. I came home one day and Mama said we couldn’t live in our house anymore.

BRUNO: That happened to me too! The Fury came for dinner, you see, and the next thing I knew we moved here. And I hate it here. Did he come to your house and do the same thing?

SCHMUEL: No, but when we were told we couldn’t live in our house, we had to move to a different part of Cracow, where the soldiers built a big wall and my mother and father and my brother and I all had to live in one room.

BRUNO: All of you? In one room?

SCHMUEL: And not just us. There was another family there and the mother and father were always fighting with each other and one of the sons was bigger than me and he hit me even when I did nothing wrong.

BRUNO: You can’t have all lived in the one room. That doesn’t make any sense.

SCHMUEL: All of us. Eleven in total. (Pg 129-132) Then one day the soldiers all came with huge trucks and everyone was told to leave the houses. Lots of people didn’t want to and they hid, but in the end I think they caught everyone. And the trucks took us to a train and a train . . . . and the train was horrible. There were too many of us in the carriages for one thing. And there was no air to breathe. And it smelled awful.

BRUNO: That’s because you all crowded onto one train. When we came here, there was another one on the side of the platform but no one seemed to see it. That was the one we got. You should have got on it too.

SCHMUEL: I don’t think we would have been allowed. We weren’t able to get out of our carriage.

BRUNO: The doors are at the end.

SCHMUEL: There weren’t any doors.

BRUNO: Of course there were door. They’re at the end. Just past the buffet section.

SCHMUEL: There weren’t any doors. If there had been, we would all have got off. When the train finally stopped, we were in a very cold place and we all had to walk here.

BRUNO: We had a car

SCHMUEL: And Mama was taken away from us, and Papa and Josef and I were put into the huts over there and that’s where we’ve been ever since.

BRUNO: Are there many other boys over there?

SCHMUEL: Hundreds.

BRUNO: Hundreds? That’s not fair at all. There’s no one to play with on this side of the fence. Not a single person.

SCHMUEL: We don’t play. . . . . You don’t have any food on you, do you?

BRUNO: Afraid not . . . perhaps you can come to dinner with us one evening.

SCHMUEL: Perhaps

BRUNO: Or I could come to you. Perhaps I could come and meet your friends.

SCHMUEL: You’re on the wrong side of the fence though.

BRUNO: I could crawl under. (Reaches down and lifts the wire fence off the ground)

SCHMUEL: I have to go back.

BRUNO: Some other afternoon then.

SCHMUEL: I’m not supposed to be here. If they catch me, I’ll be in trouble.

BRUNO: (Pg 133) I’ll come back tomorrow. NARRATOR (Actor playing Schmuel): (Pg 161) For several weeks the rain was on and off and on and off and Bruno and Schmuel did not see as much of each other as they would have liked.

BRUNO: (Pg 194-196) I thought you weren’t coming any more. I came yesterday and the day before and you weren’t here.

SCHMUEL: I’m sorry. Something happened. . . . Papa. We can’t find him.

BRUNO: Can’t find him? That’s very odd. You mean he’s lost?

SCHMUEL: I suppose so. He was here on Monday and then he went on work duty with some other men and none of them have come back.

BRUNO: And hasn’t he written you a letter? Or left a note to say when he’ll be coming back?

SCHMUEL: No.

BRUNO: How odd. Have you looked for him?

SCHMUEL: Of course I have.

BRUNO: And there was no sign?

SCHMUEL: None.

BRUNO: Well, that’s very strange. But I think there must be a simple explanation. I could ask Father if you wanted.

SCHMUEL: I don’t think that would be a good idea.

BRUNO: Why not? Father is very knowledgeable about life on that side of the fence.

SCHMUEL: I don’t think the soldiers like us. Well, I know they don’t like us. They hate us.

BRUNO: I’m sure they don’t hate you.

SCHMUEL: They do, but that’s all right because I hate them too. I hate them!

BRUNO: You don’t hate Father, do you? (Long pause) Anyway, I have something to tell you too. I’m going back to Berlin. We’re leaving on Saturday.

SCHMUEL: But for how long?

BRUNO: I think it’s forever. Mother doesn’t like it at Out-With (Bruno’s pronunciation of Auschwitz) – she says it’s no place to bring up children – so Father is staying here to work because the Fury has big things in mind for him, but the rest of us are going home.

SCHMUEL: So I won’t see you again?

BURNO: Well, someday, yes. You could come on a holiday to Berlin. You can’t stay here forever after all. Can you?

SCHMUEL: I suppose not. I won’t have anyone to talk to anymore when you’re gone.

BRUNO: (Pg 197-199) I wish we’d got to play together. Just once. Just to remember. We’ve been talking to each other for more than a year and we never got to play once. All this time I’ve been watching where you live from my bedroom window and I’ve never even seen for myself what it’s like

SCHMUEL: You wouldn’t like it. Yours is much nicer.

BRUNO: I’d still like to have seen it.

SCHMUEL: (putting his hand under the fence and lifting a little) Well? Why don’t you then?

BRUNO: But if I was caught I’d be in trouble.

SCHMUEL: That’s true. I suppose I’ll see you tomorrow to say goodbye then.

BRUNO: Unless . . . . Don’t you remember that you said I looked like you? Since I had my head shaved? Well, if that’s the case and if I had a pair of striped pyjamas too, then I could come over on a visit and no one would be any the wiser.

SCHMUEL: Would you do it? You could help me look for Papa.

BRUNO: Why not. The only problem is getting a spare pair of striped pyjamas.

SCHMUEL: That’s all right. There’s a hut where they keep them. I can get some in my size and bring them with me. Then you can change and we can look for Papa.

BRUNO: Wonderful. Then it’s a plan!

NARRATOR (actor playing Schmuel): [The next day, the two boys meet for the last time.] (Pg 202-203) Schmuel lifted the bottom of the fence off the ground and handed a pair of striped pyjama bottoms, a striped pyjama top and a striped cloth cap exactly like the one he was wearing, underneath to Bruno.

BRUNO: Well, turn round. I don’t want you watching me. (Schmuel turns and Bruno changes clothes) When was this last washed?

SCHMUEL: I don’t know if it’s ever been washed. (Bruno finishes changing)

BRUNO: (Pg 204) There, you can turn back now. (They wander into the camp)

NARRATOR (actor playing Schmuel): If it wasn’t for the fact that Bruno was nowhere near as skinny as the boys on [this] side of the fence, and not quite so pale either, it would have been difficult to tell them apart. It was almost as if they were all exactly the same really.

BRUNO: (Pg 205) I’m pretending to be a person from the other side of the fence.

SCHMUEL: A Jew, you mean.

BRUNO: Yes, that’s right. NARRATOR (actor playing Schmuel): (Pg 208) Everywhere [Bruno] looked, all he could see was two different types of people: either happy, laughing, shouting soldiers in their uniforms or unhappy, crying people in their striped pajamas, most of whom seemed to be staring into space as if they were actually asleep.

BRUNO: I don’t think I like it here.

SCHMUEL: Neither do I. NARRATOR (actor playing Schmuel): (Pg 209-210) The two boys spent an hour and a half searching the camp. They weren’t sure exactly what they were looking for, but they didn’t find anything at all that might give them a clue to Shmuel’s papa’s disappearance, and it started to get darker.

BRUNO: I’m sorry, Shmuel. I’m sorry we didn’t find [anything]. I think I ought to go home now. Will you walk back to the fence with me? (Actor playing Schmuel steps behind Bruno and whistles loudly – the whistle is the sound of the solders getting ready to order people on a march). What’s happening? What’s going on?

SCHMUEL: It happens sometimes. They make people go on marches.

BRUNO: Marches! I can’t go on a march. I have to be home in time for dinner. It’s roast beef tonight.

SCHMUEL: Sshhh! Don’t say anything or they get angry.

BRUNO: (Pg 211-213) Does the marching go on for long?

SCHMUEL: I don’t think so. I never see the people after they’ve gone on a march. But I wouldn’t imagine it does.

BRUNO: That’s it. I’m going to catch a cold out here. I have to go home.

NARRATOR (actor playing Schmuel): But as he said this, his feet brought him up a set of steps and into a long room that was surprisingly warm and must have been very securely built because no rain was getting in anywhere. In fact it felt completely airtight.

BRUO: Well, that’s something. I expect we’ll have to wait here till [the rain] eases off and then I’ll get to go home. I’m sorry we didn’t find your Papa. [And] I’m sorry we didn’t really get to play, but when you come to Berlin, that’s what we’ll do. You’re my best friend, Schmuel. My best friend for life!

NARRATOR (actor playing Schmuel): At that moment there was a loud gasp from all the marchers who had filled the room. The door at the front was suddenly closed and a loud metallic sound rang through from the outside.

NARRATOR (actor playing Bruno): And then the room went very dark and somehow despite the chaos that followed, Bruno found that he was holding Schmuel’s hand in his own and nothing in the world would have persuaded him to let it go.
```

---

## IC-0326: The Boys Next Door

- Title: The Boys Next Door
- Author (byline): Tom Griffin
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: June 1995
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BARRY, MR. HEDGES, MR. KLEMPER
- Teaser before the introduction: Yes
- Spoken words (computed): 1404
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tom Griffin
ISBN: 978-0822201434
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): June 1995
```

### Introduction (context only: never use it for content warnings)

```text
Barry Klemper . . . self-proclaimed golf-pro, but don’t get too invested in that description. Barry suffers from schizophrenia and has lived most of his life in an institution. Now at age 28, he has moved into a supervised group home with other handicapped and mentally ill young men. He spends his days recruiting golf-students who are excited about his extremely low rates at first . . . but then, like Mr. Hedges, they discover the reason why. In this selection, you’ll learn there is much more to Barry than meets the eye – You’ll discover his past, his family and possibly begin to understand why Barry struggles to relate to a father whom he wants to idolize, but simply cannot. The Boys Next Door by Tom Griffin
```

### Performance text (classify this)

```text
(Barry and Mr. Hedges on the grounds of the apartment complex. A bench. Bright sun. Barry is twenty-eight. He is full of positive conviction.)

BARRY: I’ll tell you one of the basic problems of gold. Maybe the basic problem of golf. Gold is a game. It’s just a game, Mr. Hodges, just a game.

MR. HEDGES: Hedges.

BARRY: It’s too early to worry about that. Besides, I don’t know of more than two or three courses with a serious hedge hazard. Sure, traps. Sure, thick rough. Sure. But hedges. That’s rare.

MR. HEDGES: My name is Hedges. My Name is John Hedges.

BARRY: I have no reason to doubt that. But you’re paying good money for this lesson, and we can’t spend all the time worrying about the occasional hedge. It just doesn’t make senses.

MR. HEDGES: Are you joking?

BARRY: I don’t joke, John. (Pause). Today, our first lesson we’re not even going to touch a club. Today’s lesson, I call, “How to Handle a Heckler in the Gallery.”

MR. HEDGES: Gallery? What gallery? I play on a nine hole public course. I just want a few basic tips. Maybe we should just forget this whole thing. It doesn’t seem to be working out.

BARRY: Don’t quit now, John. Hang in there. I know that the first lesson is difficult, but it’ll get easier. I promise you. There’ll be a lot less to memorize as we go along.

MR. HEDGES: (Coldly) What’s the tip?

BARRY: Okay. Let me think. There are so many. Ah, here’s one that I think can be quite useful. At the top of your backswing, come to a complete stop, the club parallel to the ground, and take a moment to reflect on how fortunate we are to live in a time when golf is in full flower. Then hit that little round sucker as viciously as you can!

(SCENE)

BARRY: (to audience) I couldn’t begin to figure it. He just quit. Hodges quit. He was obsessed with Hedges. He walked away screaming at me, “Hedges! Hedges! Hedges!” Now I’m down to two students. At one dollar and thirteen cents per student, each student would have to take forty hours of instruction each week just for me to get ninety dollars and forty cents. I computed it. That’s before expenses (Dawns on him) I still have to buy clubs yet.

BARRY: A letter? (After a pause, affected) It’s from my Dad. He’s coming to visit me. He’s going to be in Boston for a day and he’s coming down to visit me. (Barry is shaken by the letter – Trancelike) It’s from Dad . . . My Dad. . . Dad is coming to visit me . . . Do you know what Dad does? He coaches third base for the New York Yankees. Kipper Klemper is what they call him. [He] used to be a backfield coach with the San Francisco Forty-niners. He know all the guys. All the guys knew him. . . . I haven’t seen him in nine years. . . . You know, he’s been busy. You know, on the road. But every Christmas, no matter what, he sends me a box of chocolates. Whether he’s busy of not. Every Christmas. Oh, a couple of times, you know, the box arrived late, but he never forgets. Not my Dad! . . . Did you know that my Dad once played one on one with Bob Cousy and ate him up. Just ate Cousey right up. (On the edge) A hook shot here, a driving layup there. Defense! Defense! Defense! . . . Can I tell you something personal? I mean, just between you and me? A secret? . . . My Dad scares me. He scares me something terrible. Something terrible. . . If I had lots of money, I’d got to Florida now Really. I’d go down there, play a few rounds every day, ie on the beach and listen to the radio, maybe even bring a thermos full of highballs. Maybe even take my dad. Yeah, I’d take Dad. (Pause) In just two days, he’ll be here. Of course, he’ll probably look older. People look older. That’s just the aging process. (Starkly) My dad, you know, when Mom died, he was pretty busy with his career. So when he brought me out to the Institutions, he couldn’t stay around too long. He kind of waves. (Barry cannot continue. He is very disturbed. Pause). Every Christmas, no matter what, those chocolates came. But, and I guess Dad just forgot this, but I never really like chocolate very much. I’d get stomachaches from it, you know. (Barry breaks down and sobs) TRANSITION And soon the day arrives . . . Barry’s father arrives at the group home for the first visit with his son in over 9 years – Is Barry’s hero-worship of his father justified, or simply a product of his schizophrenic illness? I’ll let you decide . . . .

MR. KLEMPER: These goddam apartment zoos are all like a maze. Built for goddamn rats. Wouldn’t live in one of these sties for all the tea in goddam China. (Seeing Barry, stopped cold) So this is my little Barry. Grown up real good. Real good. A . . . real man. Real good (Pause) (Tossing a bag in Barry’s lap)

Got you this. It’s just a little something. (Sees the sign) You do this, Barry? It’s real nice. “Welcome, Home, Dad!” Real thoughtful. So, why don’t you open it up? (No response)

BARRY: Hello. My name is Barry Klemper. Welcome to my home. Won’t you take a seat?

MR. KLEMPER: I think I’ll stand. Those buses put the seats so close together it’s a goddamn wonder I don’t have a hernia. But thanks for the offer.

(gesturing to the bag as Barry begins to open it) It’s nothing. Just a little something. Nothing. (Barry reaches in the bag and pulls out a cheap boxed heart. The heart is visible through cellophane. It is broken)

BARRY: (By rote) Thank you very much. I appreciate it. Thank you.

MR. KLEMPER: Like I said, it’s just a thought. You can take that cellophane off if you want to. They just put it on to keep it fresh.

BARRY: Thank you very much. I appreciate it. Thank you.

MR. KLEMPER: (Nervous loud stream of consciousness.) My scheme was to get you a bos, you know, like always. A nice box of Fanny Farmer, something like that. One of those boxes where inside they got a cherry wrapped up fancy in tinfoil. But I was kind of in a rush, so I had to pick it up at the bus station. They got a gift shop at the bus station. Gifts, cigarettes, gum. Anyway, they didn’t have any chocolates. I asked. But then the lady said they had this. This chocolate heart. Well, right way I could see that the goddamn thing was all broken into pieces. “It’s damaged,” I told the lady. “It’s been here since Valentine’s Day,” she said. “The goddamn thing is damaged,” I told her. They get sassy with me, I get sassy right back. They think, a one-armed man, he won’t be sassy. Well, bullshit to that. So I said to her, “I’ll give you half price.” And get this? The old sow said yes. (Silence. Barry is still. Mr. Klemper paces uncomfortably). . . . Yeah, it’s real nice here, Barry. A nice setup. I heard your roommate was a darkie (Pause) So what have you been doing with yourself?

BARRY: Won’t you take a seat?

MR. KLEMPER: I’ll stand (Long pause) So what have you got to say for yourself, boy?

(Silence. Mr. Klemper is getting progressively more frustrated) Your mother, God rest her pathetic soul, used to worry that you’d never talk. It wasn’t until you were about three that you said your first word. You know what that word was? “Bitch.” Your mother and me, we thought that was about the funniest thing we ever heard. We took you right over to Auntie Mae’s house so she could hear it. And you said it again, “Bitch.” Clear as a bell. We were real proud of you, boy. Real Proud. “Bitch.” I’ll never forget it. (Stops) Are you going to talk, boy, or are you going to keep it up with this silent crap? (No response). I’m talking to you, you little sonovabitch! I’m your goddamn father. When your goddamn father talks, you better goddamn listen. (Nothing). You hear me boy? This is your father, not some goddamn darkie roommate. This is your father! You hear me boy? You goddamn nut!! (Mr. Klemper, impulsively, violently, slaps Barry across the side of the head. Barry recoils, then instinctively draws into a fetal position on the couch. Mr. Kelmper backs off, shocked by his own violence. Barry protects himself and moans)

BARRY: No, Dad! No more, Dad. Please, Dad. No more . . . . Don’t hit me anymore! Please, Dad . . .

MR. KLEMPER: No, no I’m sorry. I . . . lost control. Jesus, Barry, I didn’t mean to . . . I’m sorry, I . . .

BARRY: (Whimpering) No, Dad. Please, Dad. Don’t hit me . . . Please. . .

MR. KLEMPER: (Paralyzed) It was . . . .It was an accident, Barry. I didn’t mean to. I just . . . you know . . . lost control. I’m sorry. Jesus . . . . (Barry stops whimpering. Warily, he rights himself. There is nothing or either of them to say. Mr. Klemper starts for the door). Well, I . . . guess I’d better go. Those buses, they run right on time. Buses don’t wait for a one-armed man. That’s one thing I’ve learned in life, Barry. Buses don’t wait for a one-armed man. (Pause) And don’t you worry, boy. Christmas comes around, those chocolates will be in the mail. Count on it. (Pause) It ain’t my way, Barry, but your mother, God rest her pathetic soul, would want you to know that when you were just a little baby who couldn’t talk or nothing, she loved you more than life itself. More than goddamned life itself. (Mr. Kemper exits. Barry calls weakly to the closed door)

BARRY: Dad. Dad, I’m a golf pro now, Dad.
```

---

## IC-0327: A Brief Moment in the Life of Angus Bethune

- Title: A Brief Moment in the Life of Angus Bethune
- Author (byline): Chris Crutcher
- Work: Prejudice: Stories about Hate, Ignorance . . .
- Publisher: Hyperion Press
- Publication date as stated: Sept 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ANGUS, MOM, GRANDDAD, MELISSA, RICK
- Teaser before the introduction: Yes
- Spoken words (computed): 2410
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Crutcher
Book: Prejudice: Stories about Hate, Ignorance . . .
ISBN: 978-0786813100
Publisher: Hyperion Press
Date (Month/Year): Sept 1998
2015 National Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
According to the U.S. Department of Education, approximately 160,000 students a day stay home from school because they are afraid of being bullied. That's over 3 million a month. And the highest percentage of bullying is directed toward overweight students. Options: avoid the situation, or learn to take daily verbal and sometimes physical abuse. But if your name is Angus and you have two sets of gay parents . . . that’s only the beginning. A Brief Moment in the Life of Angus Bethune by Chris Crutcher
```

### Performance text (classify this)

```text
ANGUS: While farsighted parents of other infants my age were pre-enrolling their kids four years ahead into elite preschools, my dad was hounding the World Wrestling Federation to hold a spot for me sometime in the early 1990s. I mean, my mom had to go to the husky section of Safeway to buy me Pampers. I’m a big kid. And they named me Angus. God!

ANGUS: Sometimes, when I stand back and take a good look, I think my parents are ambassadors from hell. Two of them, at least, the biological ones, the big ones. Four parents are what I have altogether, not unlike a whole lot of other kids. But quite unlike a whole lot of other kids, there ain’t a hetero among ‘em. My dad’s divorced and remarried, and my mom’s divorced and remarried, so my mathematical account of my family suggests simply another confused teenager from a broken home. But my dads aren’t married to my moms. They’re married to each other. Same with my moms.

That frightening little off-season trade took place prior to – though not much prior to – my birth, so until I began collecting expert feedback from friends at school, somewhere along about fourth grade, I perceived my situation as relatively normal.

No, what really hacks me off is that when people the size of my parents decide to reproduce, they usually dig a pit and crawl down in there together for several days. Really, I’m surprised someone in this family doesn’t have a trunk. Or a blowhole. I swear my gestation period was three years and seven months.

“Angus is a cow,” I said to my mother when she got home from her job at Westhead Trucking firm. “You guys named me after a cow.”

MOM: Your father’s uncle was named Angus.

ANGUS: So my father’s uncle was named after a cow, too. What did he think of that?

MOM: Actually, I think he was kind of proud. Angus was quite a farmer, you know.

ANGUS: Jesus help me. As Angus, the fat kid with perverted parents, I’ve had my share of adjustment problems, though it isn’t as bad as it sounds. I am incredibly quick for a fat kid, and I have world-class reflexes. Plus you don’t have to dig too deep in our ancestral remains to find an IQ safely into three digits, so grades come pretty easy to me. But I’d sure be willing to go into the winter trade meetings and swap reflexes, biceps, and brain cells, lock, stock, and barrel, for a little physical beauty.

Which brings me to tonight. Tonight is a big night, and I don’t want the blubbery bogeyman or the phantoms of sexual perversity, who usually pop up to point me out for public mockery, mucking it up for me. I want normal. I want socially acceptable. See, I was elected Senior Winter Ball King, which means for about one minute I’ll be featured gliding across the floor beneath the crimson and gold crepe paper streamers at lake Michigan High School with Melissa Lefevre, the girl of my dreams – and only my dreams – who was elected Senior Winter Ball Queen. For that minute we’ll be out there alone. Alone with Melissa Lefevre.

I mean, it’s a joke, I know that. I just don’t know whose. It’s a hell of a good one, though, because someone had to coax a plurality of more than five hundred seniors to forgo casting their ballots for any of a number of bona fide Adonises to write in the name of a cow. At first I tried to turn it down, but Granddad let me know right quick I’d draw a lot more attention if I made a fuss than if I acted as if I were the logical choice – indeed, the only choice – and went right along. Granddad is the man who taught me to be a dignified fat kid.

GRANDDAD: Always remember these words, and live by ‘em, Screw ‘em. Anybody doesn’t like the way you look, screw ‘em.”

ANGUS: And that’s just what I’ve done. Sometimes I’ve screwed ‘em by punching them in the nose, and sometimes by walking away. And sometimes by joining them – you know, laughing at myself. That’s the one that works best. So you see, slowly but surely I’m getting all this under control. I don’t mind that my detractors will wonder aloud tonight whether it is Melissa or I who is the Winter Ball Queen, a playful reference to my folks’ quirky preferences, and I don’t mind that I’ll likely hear, “Why do they just swim up on the beach like that?” at least three times. What I mind is that during those few seconds when Melissa and I have the floor to ourselves, all those kids, will be watching me dance. Now, I’ve chronicled the majority of my maladies here, but none remotely approaches my altogether bankrupt sense of rhythm. When it comes to clapping his hands or stomping his feet to the beat, Angus Bethune is completely, absolutely, and, most of all, irreversibly brain dead.

I’ve known about the dance for three weeks now. I even know the name of the song, though I don’t recognize it, and I went out and spent hard-earned money on dance lessons, [But] I’ve been planning for Melissa Lefevre for a long time. I fell in love with her in kindergarten, when she dared a kid named Alex Immergluck to stick his tongue on a car bumper in minus-thirty-five-degree weather for calling her a “big, fat, snot-nosed deadbeat.” Being a fat kid, I was interested in all the creative retaliatory methods I could get to store in the old computer for later use, and when I saw the patch of Alex’s tongue stuck tight to the bumper as he screamed down the street, holding his bleeding mouth, I knew I was in the company of genius.

The bottom line, though, [is] I would never have the opportunity for any conversation with Melissa other than one in my head. Until tonight. Tonight I’ll have to talk to her. If I don’t, she’ll have only my dancing by which to remember me, which is like Mrs. Fudd remembering Elmer for his hair. It’d be a damn shame. All I really want is my moment with her. All I want is my moment.

So now I stand at the door to the gym. Heads turn as I move through the door. I see Melissa on the dance floor with her boyfriend – a real jerk in my book, Rick Sanford – and my heart bursts against the walls of my chest, like in Alien. I order it back. A sophomore server leaves a glass of punch on the table, and I sip it slowly through the next song, after which the lead singer announces that the “royal couple” and their court are due behind the stage curtain in five minutes.

Tibutaries of perspiration join at my rib cage to form a raging torrent of sweat rushing toward my shoes as I silently hyperventilate, listening for my grandfather’s voice, telling me to screw ‘em, telling me once again I can do anything I want. I want my moment. . . . I want to run. What am I doing here? What was I thinking of? Suddenly I’d give up my moment in a heartbeat for the right to disappear. What a fool, even to think . . .

They stand before me. [Rick and Melissa] Melissa smiles.

MELISSA: Hi.

ANGUS: I smile and nod, any words far, far from my throat.

MELISSA: Why don’t we go on up?”

ANGUS: And she takes my arm, leaving Rick’s hanging limply at his side.

RICK: Yeah, why don’t you go on up? You right on up behind that curtain with my girl, snowball king.

ANGUS: Melissa drops my arm and grips his elbow.

MELISSA: Shut up. (whispering between her clenched teeth) I’m warning you, Rick. Shut up.

ANGUS: Rick tears his arm away. “Enjoy yourself,” he says to me, ignoring her.

RICK: Your campaign cost me a lot of money, probably close to two bucks a pound.

ANGUS: He looks me up and down as couples at the nearest tables turn to stare. The heat of humiliation floods up through my collar, and I fear the worst will follow. I fear I’ll cry. Melissa takes my arm again and says, “Let’s go.” We move two steps toward the stage, and Rick says loud,

RICK: Got your rubber gloves, honey?

ANGUS: What do you mean by that? (quietly, knowing full well what he means by that)

RICK: I wasn’t talking to you, bigfoot. (looking at Melissa) I’m asking if my sweetie’s got her rubber gloves.

MELISSA: I hate you, Rick. I really do.

RICK: (ignoring her) Bigfoot comes from a high-risk home. Best wear your rubber gloves, honey, in case he has a cut.

ANGUS: In that instant I sweep his feet with mine, and he lands hard on the floor. He moves to get up, but I’m over him, crowding. When he tries to push himself up, I kick his hands out, following his next movements like a cow dog, mirroring him perfectly, trapping him there on the floor. No chaperone is in view, so it isn’t totally out of hand yet. When he sees he can’t rise, I kneel, sweat pouring off my forehead like rain. Softly, very softly, I say, “You may not like how my parents live. But they’ve been together since 1971 – monogamous as the day is long. That’s a low-risk group, Rick. The only person at high risk right now is you.”

He looks into my eyes, and he knows I mean it, knows I’m past caring about my embarrassment.

RICK: Okay, man. (raising his hands in surrender) Just having a little fun.

ANGUS: I’m apologizing to Melissa all the way up the backstage stairs, but she’s not having any.

MELISSA: You should have stomped on his throat. If you ever get another chance, I’ll pay you money.

ANGUS: At the side door to the stage I say, “Speaking of embarrassment, there’s something you need to know.” She waits. “I can’t dance.”

MELISSA: (smiling) We’ll survive.

ANGUS: Yeah, well, I didn’t say I can’t dance well. I said I can’t dance. Good people have been badly hurt trying to dance with me. (to audience) We take our places. The darkness of the stage and the silence are excruciating. The curtains part as the trumpets blare. I gaze out into the spotlights, smiling like a giant. The introduction of last year’s king and queen begins, and they move toward us from stage left and right to relinquish their crowns to us. It all would be unbelievably ridiculous even if they weren’t crowning King Angus the Fat. Without moving her lips, Melissa says,

MELISSA: I picked a slow song. We don’t have to move much. Dance close to me. When you feel me lean, you lean. Whatever you do, don’t listen to the music. It’ll just mess you up. Trust me. My brother’s like you. Just follow.

ANGUS: A part of me stays to concentrate, but another part goes to heaven. In my wildest dreams I could never have imagined Melissa Lefevre being nice to me in my moment, would never have dared imagine holding her tight without feeling pushy and ugly and way out of line. Feeling greedy now, I want my moment to last.

MELISSA: Angus? Do you ever get tired of who you are?

ANGUS: I pull back a second, but it’s like Lois Lane releasing Superman’s hand twenty thousand feet in the air. She falls. I pull close again. “Do you know who you’re talking to?”

MELISSA: (smiling) Yeah, I thought so. I know it’s not the same, but it’s not always so great looking the way I do, either. I pay, too.

ANGUS: (to audience) She’s right. I think it’s not the same.

MELISSA: Want to know something about me? I’m bulimic. Do you know what that is?

ANGUS: (smiling) I’m a fat kid with faggot parents who’s been in therapy on and off for eighteen years. Yes, I know what that is. It means when you eat too much, you chuck it up so you don’t turn out to look like me.

MELISSA: Close enough for discussion purposes. Don’t worry, I’m in therapy for it. A lot of pretty girls are.”

ANGUS: Actually, I even tried it once, but when I stuck my finger down my throat, I was still hungry and I almost ate my arm. (to audience) Melissa laughs and holds me tighter.

MELISSA: You’re the only person I’ve ever told except for the people in my therapy group; I just wanted you to know things aren’t always as they appear. Would you do me a favor?

ANGUS: If it doesn’t involve more than giving up my life,

MELISSA: Would you leave with me? I like how you stood up for your family. It must be hard. Defending them all the time, I mean.

ANGUS: Compared to me, a boy named Sue had it made. (to audience) The music ends; all dancers stop and clap politely.

MELISSA: I want to dance one more. A fast one.

ANGUS: I’ll wait over by the table.

MELISSA: No. I want to dance it with you.

ANGUS: You don’t understand. When I dance to the beat of rock and roll, decent folks across this great land quake in their boots.

MELISSA: Listen. Do what you did when you wouldn’t let Rick up. Don’t listen to the music; just follow me the way you followed him.

ANGUS: I try to protest; but the band breaks into “Bad Moon Rising,” and the dance floor erupts. I back away as she comes at me, mirroring her every move, top to bottom. A crowd gathers and I’m trapped inside a cheering circle, actually performing the unheard of: I’m Angus Bethune, Fat Man Extraordinaire, dancing in the limelight with Melissa Lefevre, stepping outside the oppressive prison of my body to fly to the beat of Credence Clearwater Revival.

When the drummer bangs the last beat, the circle erupts in celebration, and I take a long, low bow. Melissa is clapping wildly. Rick yells at the door as I help Melissa into her coat.

RICK: (to Melissa) You practiced with this tub of lard! You guys were getting together dancing. You set me up. (turning to Angus) I ought to take you out, fat boy.

ANGUS: (to audience) But his unimaginative description can’t touch my glory. I put up a finger and wag it side to side in front of his nose. (to Rick) “You know the difference between you and me, Sanford?”

RICK: There are a lot of differences between us, lardo. You couldn’t count the differences between us.

ANGUS: That’s probably true, (closing my fist under his nose) But the one that matters right now is that I can make you ugly. (to audience) He stares silently at my fist. (to Rick) Don’t even think it. Next to dancing, that’s my strong suit.
```

---

## IC-0328: Brutal Imagination

- Title: Brutal Imagination
- Author (byline): Cornelius Eady
- Work: Not specified
- Publisher: G.P. Putnam's Sons
- Publication date as stated: Feb 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: IMAGINED BLACK MAN, SUSAN SMITH, LITTLE BOY
- Teaser before the introduction: Yes
- Spoken words (computed): 1560
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cornelius Eady
ISBN: 978-0399147203
Publisher: G.P. Putnam's Sons
Date (Month/Year): Feb 2001
```

### Introduction (context only: never use it for content warnings)

```text
On October 25, 1994, 23-year-old Susan Smith, accused a man of kidnapping her two small boys. She said that a black gunman had jumped into her Mazda while she waited at a stoplight, forced her out of the car and drove away with her sons. Nine days later, she shocked the entire nation by confessing that she herself had driven her car, with the two children strapped in the back seat, into a lake.

Over a quarter of a century later, the investigation that took place and the headlines Susan’s lies created, have faded. But not for everyone . . . This selection poses the question: what if, at least during the nine days between the boys' disappearance and Ms. Smith's confession, the black man in her imagination actually existed? What would he have to say?

Brutal Imagination by Cornelius Eady.
```

### Performance text (classify this)

```text
IMAGINED BLACK MAN: (Pg 5) Though it's common belief
That Susan Smith willed me alive
At the moment
Her babies sank into the lake

When called, I come.
A mother needs me clothed
In hand-me-downs
And a knit cap ???? Whatever.

SUSAN SMITH: (Pg 53-57) --When I left my home on Tuesday, October 25, I was very emotionally distraught

IMAGINED BLACK MAN: I have yet
To breathe.
I am in the back of her mind,
Not even a notion.
A scrap of cloth, the way
A man lopes down a street.

Later, a black woman will say:
"We knew exactly who she was describing."
At this point, I have no language,
No tongue, no mouth.
I am not me, yet.
I am just an understanding.

SUSAN SMITH: --I felt I couldn't be a good mom anymore, but I didn't want my children to grow up without a mom.

IMAGINED BLACK MAN: I am not me, yet.
At the bridge,
One of Susan's kids cries,
So she drives to the lake,
To the boat dock. . .
I am not yet opportunity.

SUSAN SMITH: --I wanted to end my life so bad
And was in my car ready to
Go down that ramp into
The water

IMAGINED BLACK MAN: My hand isn't her hand Panicked on the Emergency brake.

SUSAN SMITH: --And I did go part way, But I stopped. I then got out of the car.

IMAGINED BLACK MAN: Susan stares at the sinking.
My muscles aren't her muscles,
Burned from pushing.
The lake has no appetite,
But it takes the car slowly,
Swallow by swallow, like a snake.

Susan stares at the taillights As they slide from here To hidden.

******

IMAGINED BLACK MAN: (Pg 6) Susan Smith has invented me because
Nobody else in town will do what
She needs me to do.
I mean: jump in an idling car
And drive off with two sad and
Frightened kids in the back.
She has given me a poisoned heart.
It pounds both our ribs, black, angry, nothing but business.
Since her fear is my blood
And her need part mythical,
Everything she says about me is true.
******
(Pg 36-37) Susan fills our hands with plain objects,
Key, door handle, steering wheel,
But my hands are nothing:
A song you can't remember
The words to,
The button that pops
Off a vest, a comb that
Falls out of a pocket
Or purse.
Susan fills my lungs with air,
But what do I breathe out?
Parchment, ink, low growls, the
Blank gap between words.
Nothing fits upon my back,
Nothing actually catches my eye,
I am hidden and found,
I am North, South, East, West,
My dark skin porous, in-between.

Susan claims my name is muscle,
Bone, calls me tissue
And sinew, fills in my blank
With the absence of her boys,
But I am water, pebble,
Silt and gravity,
Evidence under her nail.
*******

LITTLE BOY: (Pg 7) --Who are you, mister?

IMAGINED BLACK MAN: One of the boys asks
From the eternal backseat
And here is the one good thing:
If I am alive then so, briefly, are they.
Two boys returned, three and one,
Quiet and scared, bunched together
Breathing like small beasts.
They can't place me, yet there's
Something familiar.
Though my skin and sex are different, maybe
It's the way I drive
Or occasionally glance back
With concern,
Maybe it's the mixed blessing
Someone, perhaps circumstance,
Has given us,
The secret thrill of hiding,
Childish, in plain sight,
Seen, but not seen,
As if suddenly given the power
To move through walls,
To know every secret without permission.

We roll sleepless through the dark streets, but inside
The cab is lit with brutal imagination.
******
(Pg 8-9) A few nights ago
A man swears he saw me pump gas
With the children
At a convenience store
Like a punchline you get the next day,
Or a kiss in a dream that returns while
You're in the middle of doing
Something else.
I left money in his hand.
Mr. who lives in ___
South Carolina,
Of average height
And a certain weight
Who may or may not
Believe in any of the
Basic recognized religions,
Saw me move like an angel
In my dusky skin
And knit hat.
Perhaps I looked him in the eye.

Ms. __ saw a glint of us
On which highway?
On the street that's close
To what landmark?
She now recalls
The two children in the back
Appeared to be behaving.
Mr. __ now knows he heard
The tires of the car
Everyone is looking for
Crunch the gravel
As I pulled up,
In the wee, wee hours
At the motel where
He works the night desk.
I signed or didn't sign the register.
I took or didn't take the key from his hand.
He looked or forgot to look
As I pulled off to park in front
Of one of the rooms at the back.
Did I say I was traveling with kids?
Who slept that night
In the untouched beds?
********
(Pg 18-19) How far do you think we'd have gotten
If I'd jumped in her car, a car I wanted
For who knows what,
A woman,
And not noticed the paraphernalia?
The rattles, the child's seat?
Had smelled the spills, the dried pee,
The cloudy musk of old formula?
Even if I had pushed her out, head wild
With all I guessed I'd taken,
How many minutes,
After my foot brushed a ball,
After my eyes cooled down and focused on
The rubble of play,
How many lights do you think I'd run
Before all the stuff they'd dropped
Over the years
Into the small cracks; the straws, the cold
Fries, the pacifier,
How long do you think the cops would listen
Had Susan not sworn
I was black, I was a bad dream,
The children didn't mean a thing
To that woman.
*******
(Pg 21) I am not the hero of this piece.
I am only a stray thought, a solution.
But now my face is stuck to lampposts, glued
To plate glass, my forehead gets stapled
To my hat.
I am here, and here I am not.
I am a door that opens, and out walks
No-one-can-help-you.
Now I gaze, straight into your eye,
From bulletin boards, tree trunks.
I am papered everywhere,
A blizzard called
You see what happens?

I turn up when least expected.
If you decide to buy some milk,
If you decide to wash your car,
If you decide to mail a letter,
I might tumbleweed onto a pant leg.
You can stare, and stare, but I can't be found.
Susan has loosed me on the neighbors,
A cold representative,
The scariest face you could think of.
*******
(Pg 39-40) The black man in town
They thought looked like me,
Without the dreamed-up cap
And wardrobe,
The police have him now.
He sits in a small room.
They turn him this way
And that.
He'll cool there for hours.
How do you think he feels?
I whisper we're innocent
Into his ears.

He looks so much like me,
We could be brothers.
Already, folks
May have their doubts:
He's poor enough.
Where has he been?
He has his needs.
What do they know?
Susan has lent me
His cheekbones,
His gait.
For a while,
He is as close as
They'll ever get.
********
(Pg 41) The sheriff reads off a list of things I have not done:
I have not called on the phone. I did not discard the
Childrens' clothing they found by the highway,
I wasn't the man who robbed a convenience store
In a car the same color as Susan's. I didn't drop
Off the child they found, in Seattle, in a child's
Seat like hers; the baby someone thought they
Heard crying in the woods; not there, none of
My doing.

Bloodhounds cannot catch a whiff of me. Divers
Rake the bottom of John D. Long Lake. I give
Them a snootful of silt. Who am I? Nothing
Says the sheriff, can be ruled out. A teenaged girl
Sees a man, covered in mud, walk out of the woods.
The heat sensors of the helicopter they send fail
To light my soggy footprints. Nothing can be
Dismissed. A psychic tumbles through a dream.
He nods as the children point everywhere but
In my direction. I am zip, my
Face and reasons an educated guess.
*********
(Pg 38) WHAT THE SHERIFF SUSPECTS . . .
Each time the town tells the sheriff
To look harder, my nose straightens and
My hair uncurls. I rustle like wind upon
The surface of a lake. I wink just
Below Susan's cheeks.
The sheriff has shuffled my deck all week.
So many miles, so many deeds.
I do not tire. I can't stop driving. I can
Wrangle kids in broad daylight and never
Be seen or heard. I'm not doing this for ransom.
When I'm about, things simply don't add up,
A short distance becomes too large, clocks run amok,
Stop signs change into traffic lights. Now he wonders
Why he's never noticed the way Susan's body can't sit still,
My accent rising from her alibi.

CONCLUSION Unfounded criminal accusations across racial lines have a long history in the United States. The overwhelming majority of these cases have involved white accusers implicating black people, and the consequences have often been grievous. These hoaxes have one thing in common: The accusers are counting on stereotypes to distract the police and the public from what actually took place. In the end, these hoaxes are a clarion call, reminding us of the work we as a society still have to do to achieve racial justice.
```

---

## IC-0329: The Burn Journals

- Title: The Burn Journals
- Author (byline): Brent Runyon
- Work: Not specified
- Publisher: Vintage
- Publication date as stated: Oct 2005
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BRENT, LAURA, CRAIG, MOM
- Teaser before the introduction: Yes
- Spoken words (computed): 2340
- Already set (do not supply): none

### Source block (context only)

```text
Author: Brent Runyon
ISBN: 978-1400096428
Publisher: Vintage
Date (Month/Year): Oct 2005
```

### Introduction (context only: never use it for content warnings)

```text
One February day in 1991, Runyon came home from eighth grade, had a snack, soaked his full-length bathrobe in gasoline, and set himself on fire. He intended to kill himself. But Brent was not successful . . . instead he survived to suffer the pain of burns to 85 percent of his body. What made a smart, popular, funny, loving boy try to take his own life? Depression, a chemical imbalance? I don’t have the answers and neither does Brent Runyon, but the following excerpts from The Burn Journals tries to explain what happened before, during and after the horrendous “accident.”
```

### Performance text (classify this)

```text
BRENT: When we moved here, the first thing they did was start testing me to see how smart I was. I didn’t even have time to make any friends before they put me in this program for smart kids called GT, which stands for Gifted and Talented. I started calling it Goobers and Twerps because all of the kids that were in it were real dorks. None of the cool kids were in it. None. Well, one, if you count me. I started begging my parents to let me out of the program because it was so stupid. I kept begging and begging, and then, finally, this year, they let me out of GT, and for some reason I started doing really badly. Now I’m getting F’s in a couple of classes.

BRENT: I’m awake, listening to the radio, and Mom is yelling at me to get out of bed. I don’t want to get out of bed. I don’t want to go to school. Maybe I should play sick, but I’ve done that too many times this year already.

I run the whole thing back in my head. I did so many things wrong, I can’t even believe it. I shouldn’t have taken the matches from Adam. I shouldn’t have set the whole pack on fire. I shouldn’t have thrown them into that locker. And I really shouldn’t have put that lock on the locker. When I walk into gym, Mr. Huff is standing in the back of the locker room, right next to the locker that was on fire. He says, “Okay, boys, settle down. Some arsonist among you purposefully set a shirt on fire. Boys, whoever did this is in an enormous amount of trouble. Charges will be pressed. He’ll be expelled. So whoever did it, or if you know who did it, come see me in my office before the end of the period.” His eyes lock with mine on the last word and I feel a cold sickness all over my body, but somehow I manage to keep my eyes from showing that I know he knows it’s me. What am I going to do? What am I going to do? . . . I’m going to kill myself. I think about that movie we saw in English class, about the guy who’s standing on the bridge waiting to get hung. As soon as the rope snaps his head back, he’s dead. I wonder why all the ways I’ve tried to kill myself haven’t worked. I mean, I’ve tried hanging. I used to have a noose tied to my closet pole. I’d go in there and slip the thing over my head and let my weight go. But every time I started to lose consciousness, I’d just stand up. I tried to take pills. One afternoon, I took twenty Advil, but that just made me sleepy. And all the times I tried to cut my wrists, I could never cut deep enough. I took my knife from its hiding place between the mattress and the box spring and held it against my wrist. I sliced as fast as I could and bit my lip from the pain. I hung my arm between the two twin beds pushed together from when my brother used to share the room with me and let it bleed. I was surprised when I work up in the morning. I had to find a Band-Aid big enough to cover the wound and told my parents I’d scratched my wrist on a locker. That’s the thing – your body tries to keep you alive no matter what you do. I’ve got to think of a way to kill myself that I can’t turn back from. When seventh period is finally over, I run to my locker and put all my books inside. I won’t need them anymore. Laura walks with me down D hall.

LAURA: Hey, I heard you set that fire in gym class.

BRENT: Yeah.

LAURA: What are you going to do?

BRENT: I’m going to set myself on fire.

BRENT: She stops at her locker and I keep walking. On the bus ride home, I sit by myself. I lean my head against the cold glass window and try not to think about all the stupid things I’ve done, all the bad things I’ve done, and all the pain I’ve caused everyone. My brother is playing basketball outside the house when I get home. I rebound the ball for him and throw it back. I tell him the whole story, about what I did and what they’re going to do to me. I don’t tell him what I’m going to do to myself.

CRAIG: That sucks.

BRENT: And I go inside the house. I don’t have to write a note anymore. Craig knows everything. I walk out to the shed to get the gas can. I bring it inside to the bathroom at the top of the stairs because that’s the room with the most locks. I go back downstairs and get the matches from the kitchen. I take off all my clothes and put on the pair of red boxers that my mom bought for me at the mall last weekend. I bring my bathrobe into the shower and I pour the gasoline all over it. The gas can is only about a quarter full, but it seems like enough. I step into the bathtub and I put the bathrobe over my shoulders. It’s wet and heavy, but there’s something kind of comforting about the smell, like going on a long car trip. I hold the box of matches out in front of me in my left hand. I take out a strike-anywhere match and hold it against the box. Should I do it? . . . Yes. Do it. I strike the match, but it doesn’t light. Try again. I light the match. Nothing happens. I bring it closer to my wrist and then it goes up, all over me, eating through me everywhere. I can’t breathe. I’m screaming, “Craig! Craig!” I fall down. I’m going to die. I’m going to find out what death is like. I’m going to know. But nothing’s happening. This hurts too much. I need to stop it. I need to get up. I stand. I don’t know how I stand, but I do, and I turn on the shower. I’m breathing water and smoke. I unlock the door and open it. My hand is all black. I walk out. There’s Craig with Rusty, or dog, next to him. They have the same expression on their faces. Craig yells something and runs downstairs. I think he’s calling 911. I’m following him. He hands me the phone and runs off. There’s a woman on the phone asking me questions. I try to tell her what’s happened, but my voice sounds choked and brittle. There’s something wrong with my voice. The woman on the phone says the fire trucks and ambulances are on their way. Somehow she knows my address. Craig is gone now, gone to get Mom, and Rusty is hiding somewhere. Smoke is coming from the bathroom upstairs and I can see that the whole room has turned black. I look down and see my flesh is charred and flaking and the boxer shorts are burnt into my skin The woman on the phone says everything is going to be all right, and I believe her. She keeps asking me if I’m still on fire and I say, “I don’t think so.” I’m walking around the kitchen, waiting for the ambulance to come. I can see my reflection in the microwave. Where’s my hair? Where did my hair go? Is that my face? We used to put marshmallows in the microwave. We used to watch them get bigger and bigger and then shrink down . “Oh god, just tell them to get here, just tell them to get here, okay? I’m so sorry. I’m so sorry.” I can hear the sirens in the distance now . . . Then the firemen are here. They’re putting me on a plastic sheet. They say I’m going to be okay. One of them puts something over my face. That feels good. That feels so good. The cold air feels so good going into my lungs What are they talking about? What are they saying? They’re giving me a shot. They say it’s going to make the pain go away. Make the pain go away. I’m looking at the faces of all the men who are gathered around me. Their eyes are so blue and so clear. I turn my head and see Craig in the front hall. He’s yelling and punching the walls. He’s angry And my mom is here, and she’s smiling and saying she loves me, and her eyes, which are green like my eyes, are the most beautiful things I’ve ever seen. I don’t want to die anymore. I hope Craig can love me again. **************

BRENT: I’ve been [at the burn center] for exactly one month. Mom sits by my bedside and I can tell that she wants to talk about the fire and everything about it. So I start by trying to say why I was so sad, and how I thought that the principal was going to expel me and how I didn’t want them to be mad at me because they both wanted me to be so smart and I’m sorry I couldn’t be what you wanted.

MOM: You are everything we wanted.

BRENT: And we both cry together. “Mom, no one’s ever going to love me, are they?” But mom puts her hand on my fingertips and whispers,

MOM: Brent, listen to me, honey, you are so smart and so kind. You will fall in love, and someone will fall in love with you. I promise.”

BRENT: It makes me feel better to hear her say that, but I can tell that she’s not really sure. It’ll be okay, I tell myself, I can live in the basement when I get older so people don’t have to look at me. I’m crying and crying. I want her to go away and leave me alone.

**************

BRENT: People here like to talk to me about Pain Management. They ask me to rate my pain on a scale of one to ten. One being the least painful and ten being the most. I don’t think they have a number for some of the pain I’m going through. I don’t think they even have a number. I keep thinking about it. I was in the bathroom and I had the gas can and the matches and I sat on the toilet. That’s when I should’ve realized how stupid I was being. That’s when I should’ve stopped it. But I stood in the bathroom and put the bathrobe on, and it was wet and heavy, and I could have taken it off and gone back outside to play basketball with Carig and said, You won’t believe what I almost did. And he would’ve known what to do. He would’ve gotten me help and made that Mom and Dad weren’t made at me. I should’ve done that. I wish, I wish, I wish, I wish, I wish I’d stopped. But I didn’t.

********************

BRENT: Mom is here and she looks like she’s ready to talk. If I just say it, then maybe I’ll be able to stop feeling so bad inside. I’ll say, Hey Mom, guess who tried to kill themselves a bunch of other times besides the one you know about? That’s right, me. Hey, Mom, remember the Band-Aids on my wrist? Well, I didn’t really scrape it on my locker. I cut it with a knife that I kept under my bed. . . . And you know the furnace in the basement, I thought about pouring gasoline in there and blowing up the whole house . . . And you know how I got the book on how to make knots? It was so I could tie a noose and hang myself from the closet pole. I can’t say any of this. So I say, “Mom . . . when I . . . . when I tried . . . to hurt myself before . . . that wasn’t the first time that I tried to do something like that.” She doesn’t look surprised, but she’s starting to cry. She puts her hand on top of mine.

MOM: I know, honey. I figured it wasn’t the first time. I’m sorry I didn’t know you were so sad.

BRENT: She’s crying hard now, and I’m crying too. “I know. I’m sorry, Mom.”

MOM: Brenny? . . . About a week before your accident . . . .

BRENT: An accidental house fire. Right. Okay. Okay. We can say that. We don’t have to tell anyone what really happened. An accidental house fire.

MOM: . . . . we got into a fright at the dinner table and you stormed up to your room, and I remember, I said, “Where are you going?” and you said, I think I heard you say, “I’m going to set myself on fire.”

BRENT: I think about it. “I don’t think I said that. I mean, I might have, but I didn’t mean it.” She can hardly get the words out, she’s crying so hard.

MOM: But if you ever get that sad again, you have to promise to tell someone so they can help you . . . And know that we love you so much and we don’t ever want to lose you.” ********************

BRENT: It’s been nine months and I still don’t know why I did it. I was so sad. I wanted to be funny and cool and I wanted everyone to love me, but I still don’t know why I did it. [Once I was home] we never mentioned my suicide attempt or my time in the hospital – my parents still call it an accident. To them, the entire thing was a mystery they’d given up on solving. But as I talked to more people, I realized that the only thing unique about my story is the rather unfortunate and dramatic way in which I tried to kill myself. Other than that, I’m just another guy with a history of depression, which is somehow very comforting to me . . .
```

---

## IC-0330: The Button

- Title: The Button
- Author (byline): Robert Newman
- Work: Not specified
- Publisher: Originally Published by Wetmore Declamation Bureau (no longer in business)
- Publication date as stated: 1949
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JOE, DR. TREVOR
- Teaser before the introduction: Yes
- Spoken words (computed): 1146
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Newman
ISBN: 978-1600451157
Publisher: Originally Published by Wetmore Declamation Bureau (no longer in business)
Date (Month/Year): 1949
```

### Introduction (context only: never use it for content warnings)

```text
In the choking blackness of solitary confinement, Joe Ransom teeters on the brink of madness. A single match, a drifting spider, a worthless white button become his last defenses against the terror. He devises a simple game to protect his sanity. Will the game work or will the button prove to be his downfall?

The Button by Robert Newman
```

### Performance text (classify this)

```text
The scene is a solitary confinement cell in a large American prison. It is a stone-walled room about six feet square and in it, a hard cot, no other object of any kind. The room is in absolute darkness. On the cot sits a prisoner, Joe Ransom, about forty years of age. He is in solitary after a prison riot in which another convict has been murdered. His head in his hands, he sits and rocks from side to side on the cot; the springs creak with every move. Suddenly he stops swaying, lifts his head and listens. Far away an iron door opens.

JOE: Warden! Warden! I knew you’d come. Warden, listen -- listen to me. Listen, Warden, you gotta take me out of here. You gotta, see? I’m goin’ nuts. I can’t stand it, Warden, I’m goin’ nuts!

Look, look, Warden, I’ll tell you what I’ll do, see. I’ll confess. Get me a pencil and paper and for a little light and I’ll write out a confession. Then you can take me out and hang me. I’ll confess see –Warden! (shouts) Warden, are you listenin’? I tell you I killed him. I killed him. I KILLED HIM!

JOE: All right. All right. I’ll be calm, see -- Calm an’ quite, so’s you’ll know I mean what I’m sayin’. Listen: I, Joe Ransom killed my cellmate, Mike Malari. I did it. An’ I’ll tell you why, Warden. It was his eyes. He used to sit there starin’ at me. The guards wouldn’t put me in another cell. They just laughed, Warden. Thought it was funny, they did, him starin’ at me like that. Five years, Warden, five years I stood it. Five years I stood those eyes. Then I killed him. That night when hell broke loose in the block an’ everybody was fightin’ back and forth in the corridor, I killed him. It was him or me, Warden, him or me -- So I squeezed his throat, ‘till I knew he wouldn’t stare at me no more. There, Warden, I confessed. Now hang me -- do anything to me -- only take me out of this hole. I’m afraid, Warden, I’m afraid of bein’ alone in this dark -- I start seein’ things -- I start seein’ Mike’s eyes again!

(shouts)

Warden! Take me out! Open this door! Take me out! Take me out! Take me out! (pause, silence, then almost timidly) Warden!

Gone! He’s gone! He’s gone and left me here! In the dark. Pitch dark. Ssssh! What’s that! Something movin’! Up there. Up there in the corner. Mike! No, no, it can’t be Mike, or you could see his eyes. Take it easy now. The match. . . the one match you saved. Don’t tremble! So, light it! (strikes the match and then reacts) A spider! It’s a spider! He’s weaving a web. He’s weaving a web to catch flies! You fool, spider, you fool! There’s no flies here. There’s nothin’ here except me. Me! Why don’t you catch me in your web, spider? Why don’t you catch me? I’ll sit down and watch you. You’re weaving, spider, back and forth, back and forth, back and forth. (mesmerized) Look, I can do that too. Back and forth, back and forth, back and forth, back and forth, back and forth, back and forth, the spider and I, back forth . . .

Stop it! Stop it, you hear Joe Ransom. You’ll go nuts that way! Nuts, crazy, mad! Stop it!

What are you going to do? What are you going to do?

What was that? I heard something. I heard something drop. What was it? A button! A button came off my jacket. Here it is. Little button. White button. What do I want it for? What good can it do me? I’ll throw it away. (tosses the button) Throw it away like I threw my life away.

Now it’s gone. Gone like my life. Like everything. (beat) No, its not gone. It’s still here. Here in this cell some place. I heard it. I heard it. I heard it drop. I threw it away like my life, like everything, but it’s still here, here in the cell!

(determined) I’ve got to find it. I’ve got to find it, you hear? It means something! Now where is it? Where? I heard it hit the wall and then the floor. Is it under . . . (looks under the cot) Here it is! Here it is, the little button. I found it. It means something. I know. It’s a game! I play the game and it keeps me from thinkin’. It makes me tired and then I can sleep. Sleep! And not see Mike’s eyes. This is it! I’m saved! Saved! Play it again. Close your eyes.

Now throw! This side. It went over there. No! Further to the left. There it is. This is it! This’ll save me! I was a sucker to shoot off my mouth to the Warden like that. Well, it wasn’t in writing, that was one good thing! I’ll have to get hold of a mouthpiece right away, there must be something . . . (long beat) Insanity! That’s it. Pull the nut act! Boy, oh boy, oh boy, I’m saved!

The button! The button, you fool! Throw the button. Play that game! Throw! Over here. No. over further. That was near the other side. Near the door. No. Here? No. Where? Where? Oh, here it is! What would happen if I couldn’t find it? What would happen in a little stone cell? Where could it get lost? Play! Throw the button!

That was near the bed. No nearer the middle – there! But if it did get lost? Stop it! It can’t get lost! Play the game. Play and forget! Shut your eyes. Put your arm back and throw!

(he slowly descends into madness) Throw? I threw. I threw the button. I threw the button, but I didn’t hear it hit. I threw and it didn’t hit. I didn’t hear it hit anything. All I can hear is my heart beating, beating, beating. Pounding -- pounding in my ears.

I threw the button and now it’s gone. It didn’t hit the walls, the floor, anything. I threw and it disappeared. It’s gone! Gone! Where is it? What happened? I threw and it’s, its gone! Something grabbed it! Something . . .

(terrified) Mike! Mike! Stop staring! Stop staring at me! Mike! Don’t! Don’t, Mike! Don’t touch me, Mike!

******

DR. TREVOR: (on the phone) Hello, hello. Yes, operator, get me the Warden’s office. Hello, Warden? This is Dr.Trevor. (beat) Yes, I’m down in the solitary confinement wing. (beat) Yes. Yes, I examined him. (beat) No. I had him sent away. (beat) Yes. Completely, hopelessly mad. (beat) No, not a chance. His mind’s gone. (beat) What caused it? Hard to say, sudden terrific shock or an emotional blow. Solitary confinement is a strain on the best of them. (beat) No, that’s all. Oh, yes, one thing, very curious. I looked around the cell after he was taken away, there was a spider web in one corner. (beat) Yes, I said spider’s web. And in the spider’s web was a button - a little white button. Odd, isn’t it.
```

---

## IC-0331: A Child Called It

- Title: A Child Called It
- Author (byline): Dave Pelzer
- Work: Not specified
- Publisher: Health Communications, Inc.
- Publication date as stated: Oct 1995
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DAVID, MOTHER, FATHER, MOTEHR
- Teaser before the introduction: Yes
- Spoken words (computed): 1451
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Pelzer
ISBN: 978-1558743663
Publisher: Health Communications, Inc.
Date (Month/Year): Oct 1995
```

### Introduction (context only: never use it for content warnings)

```text
From the outside looking in, you might’ve believed the Dave Pelzer had the perfect life – but four teachers who happened to be paying attention in the 1970s realized that was not the case at all. On paper, the Pelzer home seemed picture-perfect. But there were secrets at home. You see, when Dave’s mother drank, she morphed into something quite horrific. And unfortunately for Dave, he became her primary target. But in the 1970s, Child Protective Services did not exist, and our society didn’t want to know that there were parents out there actually hurting their children.

A Child Called It by Dave Pelzer
```

### Performance text (classify this)

```text
DAVID: (Pg 15) [Once upon a time] My family was the Brady Bunch of the 1960’s. My two brothers and I were blessed with the perfect parents. Our every whim was fulfilled with love and care.

My mother, Catherine, was a woman who glowed with love for her children. (Pg 16) One day, she took us to Chinatown in San Francisco. As we drove around the area, Mom told us about the culture and history of the Chinese people. When we returned, she decorated the dining room with Chinese lanterns, she dressed in a kimono and served what seemed to us as a very exotic meal. At the end of dinner Mom gave us fortune cookies and read the captions for us. I felt that the cookie’s message would lead me to my destiny -- “Love and honor thy mother, for she is the fruit that gives thou life.”

(Pg 18) [And Christmas!] Before dawn, Mom would creep into our room and wake us, whispering, “Santa came!”

DAVID: (Pg 21-22) [As I got older] My relationship with Mom drastically changed. As a small child, I probably had a voice that carried farther than others. I also had the unfortunate luck of getting caught at mischief, even though my brothers and I were often committing the same “crime.” In the beginning, I was put in a corner of our bedroom. When she yelled at us, her voice changed from nurturing mother to the wicked witch. Soon, the sound of Mother’s voice began to send tremors down my spine.

When Mother decided that the “corner treatment” was no longer effective, I graduated to the “mirror treatment.” Mother would grab me and smash my head against the mirror, smearing my tear-streaked face on the slick, reflective glass. Then she would order me to say over and over again, “I’m a bad boy! I’m a bad boy! I’m a bad boy!”

(Pg 27-28) When I came home from school one day Mother told me that she had often driven to school to watch my brothers and me play during our lunch period recess. Mother claimed that she had seen me that very day playing on the grass, which was absolutely forbidden by her rules. I quickly answered that I never played on the grass. I knew Mother had somehow made a mistake. My reward for observing Mother’s rules and telling the truth was a hard punch in the face. Mother then reached over and turned on the gas burners to the kitchen stove. She sneered at me,

MOTHER: You’ve made my life a living hell! Now it’s time I showed you what hell is like.

DAVID: Gripping my arm, Mother held it in the orange-blue flame. As hard as I fought, I could not force Mother to let go of my arm. Finally, I fell to the floor, on my hands and knees, and tried to blow cool air on my arm. Mother ordered me to climb up onto the stove and lie on the flames so she could watch me burn. I refused, crying and pleading. I had to buy time.

(Pg 29) Finally, I heard the front door fly open. It was my brother Ron. My heart surged with relief. For a moment in time, Mother froze. I seized that instant to race to the garage. I had beaten her. That day I vowed to myself that I would never again give [her] the satisfaction of hearing me beg her to stop.

(Pg 30-31) The summer after the burn incident, school became my only hope of escape. By then, Mother would “forget” to feed me. On a good day, I was allowed leftover cereal portions from my brothers, but only if I performed chores before going to school. I started stealing food at school. (Pg 39-40) My idea was to rip off frozen lunches from the school cafeteria. Alone in the restroom, I swallowed frozen hot dogs and tater tots so fast I almost choked myself in the process. I returned to the classroom, feeling proud I had fed myself. I had fed myself!

That afternoon, Mother changed my mind. She dragged me into the bathroom and slugged me in the stomach so hard that I bent over. She rammed her finger into my mouth as if she wanted to pull my stomach up through my throat. I knew what was going to happen next. I closed my eyes as chunks of red meat spilled into the toilet. “I thought so. Your father’s going to hear about this!” Mother ordered me to scoop the partially digested food out of the toilet and put it in a bowl. Mother was gathering evidence. (Pg 41) That evening Mother and Father stormed into the kitchen.

MOTHER: So, you think the boy is through stealing food, do you?

DAVID: I could tell he was getting more and more tired of the constant “What the boy had done now” routine. Staring at me, Father shook his head in disapproval and stammered,

FATHER: Well, if you would just let The Boy have something to eat.

MOTEHR: EAT? You want the boy to eat? Well, the boy is going to EAT! He can eat this!

DAVID: I sat on a chair and picked the clumps of hot dogs out of the bowl with my hand. Globs of thick saliva slipped through my fingers, as I dropped it in my mouth. As I tried to swallow, I began to whimper. I turned to Father. He nodded for me to continue. I felt a hand clamp on the back of my neck.

MOTHER: Chew it! Eat it all!

DAVID: (Pg 42) Father turned away to avoid my pain. And at that moment, I hated Mother to no end, but I hated Father even more. He stood like a statue while his son ate something even a dog wouldn’t touch.

(Pg 50-54) The summer of 1971 – my morale dwindled. Food was little more than a fantasy. I rarely received breakfast and never lunch. As for dinner, I averaged about one every three days. During dinner, I sat at the bottom of the stairs listening to the sounds of “the family” eating. Suddenly [I heard] Mother’s snarling voice.

MOTHER: Get up here!

DAVID: I had begun clearing the dishes from the dining room table, praying that tonight I would get something, anything, to soothe my hunger.

MOTHER: You have 20 minutes! One minute, one second more, and you go hungry again! Is that understood?” Look at me when I’m talking to you!

DAVID: As I looked at her, Mother snatched a carving knife from the countertop and . . .

MOTHER: If you don’t finish on time, I’m going to kill you!

DAVID: Her words had no effect on me. She had said the same thing over and over again for almost a week now. But something looked wrong. Very wrong! I strained my eyes to focus on Mother. Her whole body began to weave back and forth. I thought she was going to fall. I imagined that the old drunk was going to fall flat on her face. Out of the corner of my eye I saw a blurred object fly from her hand. A sharp pain erupted from just above my stomach. I tried to remain standing, but my legs gave out, and my world turned black.

It took my Mother nearly half an hour to dress my wound. There was no remorse in her eyes. I thought that, at the very least, she would try to comfort me. Looking at me with no emotion, Mother stood up, washed her hands and told me I now had 30 minutes to finish the dishes.

From the kitchen I could hear Father flipping through his newspaper. I made my way into the living room. Sitting on the far end of the couch was my hero. I knew he would take care of Mother and drive me to the hospital. “Mo . . . Mo . . . Mother stabbed me. She told me if I didn’t do the dishes on time . . she’d kill me.”

FATHER: (Long pause - coldly) Well . . . you better go back in there and do the dishes. Damn it boy, we don’t need to do anything that might make her more upset! I don’t need that tonight . . . Go!

DAVID: I stood before Father in total shock. He didn’t even look at me.

(Pg 95-97) (As an adult) As a child living in a dark world, I feared for my life and thought I was alone. As an adult, I know now that I was not alone. There were thousands of other abused children. Some victims stay quietly locked in their shells. They look the other way, believing that by not acknowledging their past it will go away. This is my story. And I believe if society is to come to grips with the problem of child abuse, it must be exposed. Childhood should be carefree, playing in the sun; not living a nightmare in the darkness of the soul.
```

---

## IC-0332: Children of Cambodia's Killing Fields

- Title: Children of Cambodia's Killing Fields
- Author (byline): Dith Pran and Kim DePaul (eds)
- Work: Not specified
- Publisher: Yale University Press
- Publication date as stated: April 1997
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2724
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dith Pran and Kim DePaul (eds)
ISBN: 978-0300068399
Publisher: Yale University Press
Date (Month/Year): April 1997
```

### Introduction (context only: never use it for content warnings)

```text
Youkimny Chan's story is one of millions. Every day, somewhere in the world, someone is struggling to survive genocide, oppression and hopelessness. Children watch their families die around them on a daily basis. They are left with a lifetime of pain, suffering and healing.

Youkimny Chan was sponsored in 1980 by Catholic Social Services in Minnesota. He received an education in the states following the Khmer Rouge and is now a social worker in Long Beach, California.

It's time for us to wake up. It's time to start really seeing what is going on in the world – outside our circle of complacent comfort. It's time to fight for those unable to fight for themselves.. It's time for peace to be restored. Bring truth. Bring life. Give hope. Show grace. Heal the world.

What follows is an excerpt from Children of Cambodia's Killing Fields, edited by Dith Pran and Kim DePaul – it is a collection of memoirs by child survivors. This is Youkimny Chan’s story.
```

### Performance text (classify this)

```text
When I was just a little boy I would sit with my sister Sinuoen in our swing under a coconut tree. She would read stories to me about amazing places. We would talk and sing songs together and sometimes listen to soap operas on the radio. I loved my sister and I loved those happy times we spent together. In the evenings we would sit under the full moon and listen to the crickets and the coconut tree leaves rustling in the breeze. We would talk about what we wanted to do when we grew up. It was good growing up in Cambodia.

In the afternoon, while the adults napped, the children would go down to the river to swim. The beaches of the Mekong River were wide and sandy, and the river was blue and sparkling. My friends and I would splash and yell and then run onto the beach and start a game of soccer or hopscotch or volleyball. If we got hungry, there were always fruit trees nearby, heavy with mangos, coconuts, and bananas. The Cambodia I knew as a child was a beautiful place. Things grew quickly there. Hibiscus and roses of all colors filled the air with fragrance. My grandmother would bring armfuls of flowers into our house every day.

We lived in a garden. When I close my eyes I can still see the blue skies and the tropical flowers. I can still see the laughing faces of my friends and family.

My family was very close. My father, who was a captain, in the Cambodian army, had died of malaria when I was three years old, but my grandparents took me, my mother, and my brothers and sisters to live with them. They became my second parents. I always thought of my grandfather as my real father. Although he was gone often, when he was at home he made time for his grandchildren. I respected him and loved him deeply. My mother was a professional nurse and was very respected by people who knew her.

My oldest sister, Sinoy, was already married and had three children. My brother, Kimhour, who was seven years older than I, was a student at the University of Cambodia and a well-known soccer player. My favorite sibling was Sinuoen, who was five years older than I. She was always patient with me. The youngest in my family was my little brother, Sombo. With my grandparents, we lived in a very large house that had been in the family for generations. It was a beautiful house and it had wonderful black hardwood floors. My grandmother was so proud of those shiny floors. She waxed them every day with coconut skins, kerosene and candle wax to make them glow.

In 1974, the Khmer Rouge took over all the small villages surrounding Phnom Penh, as my grandfather predicted. Soon after that, the bombing of our city began. When the shelling of Phnom Penh started, we were frightened, but we were also a little relieved. We knew that the war would soon be over. Many people from the small towns around us had fled to Phnom Penh as their villages were attacked and destroyed. Many of them had nowhere to live, and so they slept in the streets.

On April 17, 1975, when I was fourteen years old, the Khmer Rouge army came into Phnom Penh with tanks. A man in a slow-moving car shouting into a loudspeaker ordered all the police and military leaders to put down their guns and surrender. He told all the people to leave their houses. My grandfather didn't want the Khmer Rouge to know he was a military officer for their enemy, so he hid his uniform and weapons. We wouldn't leave the house. It was our home, and we were free people. We were not about to let anyone tell us to leave.

Then soldiers came to our house with their guns and ordered us to leave. They said we would be gone for only three days, and during that time the Khmer Rouge would clean up the city so that it would be safe for us to return. But the soldiers came again and said that the American B-52 bombers were going to attack the city and that we would have to leave in a hurry or be killed by their bombs. The soldiers assured us that they would defeat the Americans and that then we could return to our homes.

These soldiers were our countrymen. We had no reason not to believe them. They weren't going to let us get hurt. So we packed our car with clothes, some gold and jewelry, and some food. Everyone in my family left together. Some crowded into the car and the rest of us walked. Leaving Phnom Penh was an adventure. Thousands of people were leaving at the same time. The streets and sidewalks were covered with people carrying bags, and cars crept along slowly in the congestion. There was so much noise.

The next day, soldiers came and searched us. They took our jewelry, our car, and most of our clothes. Now everyone in our family had to walk, and we had to divide the remaining food among us to carry it on our backs. It was the dry season and it was very hot. There was no water. People began to get heatstroke and fall down on the road. The soldiers wouldn't let us stop to help those who were sick. I couldn't believe what was happening. We walked for days, then weeks. Pregnant women gave birth under trees by the road. Old people died from exhaustion and lack of water. Everywhere was the sound of babies screaming and people crying for loved ones who had died and had to be left on the road.

There was no time for funerals. Soldiers threw the bodies into empty ponds and kept everyone moving. Guns were pointed at us, and tanks forced us to keep moving. I saw two men with their hands tied behind their backs. Soldiers were questioning them on the side of the road. The soldiers cut off the men's heads, which fell to the ground as their bodies slumped. There was nothing I could do. People were being murdered before my eyes. These were my friends, my neighbors. The rest of us kept walking.

Finally, after almost two and a half months of walking and stopping, walking and stopping, we arrive outside the province of Battambang, where most of the small villages in the jungle had been burned to ashes during the fighting. We were told that we must live in those burned-out villages. We were civilized people. We had never lived in the jungle without houses and electricity and running water. We still believed that we would be allowed to return home. My grandfather asked the soldiers when we would leave and was told, "In a few days." After many days, I saw him beginning to lose faith.

Our family had to survive even though we had almost nothing. My grandfather, older brother, and brother-in-law built a small hut out of bamboo they cut down. It had a bamboo floor to protect us from snakes and palm leaves for the roof. Thirteen of us lived together in the hut.

All of us started to get sick from malnutrition. Many were getting malaria. There was no medicine and no doctors. Finally we began to eat banana and papaya trees - not the fruit of the trees. We would peel off some layers of the bark, then cut off pieces of the tree and boil them with salt. It gave us something to eat, but it also made some of my family very sick. My sister's ten-year-old son got diarrhea and died after three days of suffering. Then her seven-year-old daughter died. My sister went crazy with grief. She would not move from the spot where we buried them. She never recovered.

After we had been in our hut for about a year, the soldiers came to take my grandfather. They grabbed him and tied his hands behind his back. "We know you were in the military," they said to him. Grandfather did not struggle. But as he left, he turned to my grandmother and said, "Would you take care of my family?" The soldiers slapped him in the face and marched him out. Many minutes went by. We heard a shot deep in the jungle. We knew Grandfather was dead.

The Khmer Rouge continued their killing. If someone was suspected of having an education or of being an intellectual, the soldiers would pull him out of his hut at night and shoot him or cut his throat. None of us could ask questions or cry out. We were weak and sick. We had no weapons. And if we made the soldiers angry, they would kill us.

Three months after my grandfather was murdered, the soldiers took my brother and brother-in-law. They were tied up and taken two or three miles into the jungle. This time I followed, sneaking through the undergrowth so that no one would see me. I watched as my brothers were forced to dig a large hole while the soldiers held guns to their heads. I remember one soldier saying to the other, "We will save our bullets." Then they took big bamboo shoots and beat my brothers again and again until they were dead. Their bodies were kicked into the hole. Their grave was not far from where my grandfather was killed.

Those who were not murdered by the soldiers were dying a slow death. We traded what little we had been able to hide for food from a government family. An ounce of gold would get us a cup of rice. Soon we had nothing left to trade. We were always hungry. We were always sick. My oldest sister, Sinoy, could no longer talk or move. After about a year of living in the jungle, one of my mother's sisters, who had been living with us, died early in the morning. Sooner after, my other aunt died. We found her body already stiff when we woke one morning. The neighbors helped us bury them but we had no grave makers. So many had been buried around the village that it was impossible to keep track of the burial places. By the next day, we couldn't tell where their graves were.

Within about three months after the deaths of my aunts, my grandmother died, and then my older sister. She had already buried her husband and children, and she had nothing to live for. The rest of us continued to struggle to survive. Whenever we got some food, we would divide it. My mother would always give me part of hers. I was her favorite child, and she wanted me to live. But now my mother was very sick. I was afraid she was dying.

She spoke to me quietly. "Son, if you ever get away from the Communists, go to school. They can take away your possessions, but they can't take your education. They can't take what you know." Soon after that, my mother died. I wanted to die, too. She had always taken care of me and I had depended on her. Now there was no one to take care of me. Soon my little brother died. The neighbors helped me bury him. Now only my sister and I remained.

My favorite sister, Sinuoen, continued to get weaker and weaker. Her skin was sticking to her bones, and she had lost her long black hair. I think this was the hardest time of all for me. It was my responsibility as the oldest male to protect my sister. My mother would be counting on me. But there was nothing I could do. And one day, as we sat together in the hut, Sinuoen put her head on my lap and said, "Kimny, I don't know if I can live any longer. Can I have a spoon of rice?"

My heart was breaking. It was such a little thing she asked. But we had no rice. I got up and brought her our last cup of water. "Sister," I said, "I have no rice to give you. Drink this water." She looked into my face for a moment, and then she sipped the water. She put her head down on my lap. And then she died.

I don't know why I didn't die, too. I didn't want to live any more. I was so tired and so hungry. I wandered around for months after that begging for a bit of rice from anyone who had some. I never went back to our hut. Sometimes I slept outside. Sometimes I crawled into the hut of another family. But most families had suffered like mine. No one had enough food. No one had hope.

Then the Khmer Rouge decided they needed more young people from the villages to work for them. They took all the teenagers from our jungle village to a concentration camp in the jungle about thirty miles from where my new hut was. I wasn't afraid to go. My family was all gone. I thought, "If I walk and drop dead, I'll drop dead. It's not so bad."

The concentration camp was just a clearing in the jungle. The other young prisoners and I built a makeshift hut with the bamboo we found. We worked from sunrise to sunset, fourteen or fifteen hours a day, in the rice paddies. It was the rainy season, and the work was hard. After a whole day's work we would be fed a few bites of dry fish and a little rice. Then, before we could sleep, the Khmer Rouge would lecture us about how to be good Communists. They said that Pol Pot was our Angka. Pol Pot was our new family. If any of us found that our parents were not obeying the Communists, we should turn them in.

We could not escape. The camp was encircled by barbed wire, and the thousand or so of us were all afraid for our lives. Sometimes they would pull a boy out of his hut at night and we wouldn't see him again. Sometimes they would take a boy into the jungle and we would hear him scream. Sometimes they would throw the body parts of a boy they had cut apart into the rice paddies as we worked. "Fertilizer," they would say.

When I was about seventeen years old, I remember trying to sleep at night but the sound of bombing in the distance kept me awake. Each night the bombing got closer and closer. We found out later that the Vietnamese were pushing the Khmer Rouge out of our area and up against the Thai border. The Khmer Rouge guards never said anything about the fighting.

Then one day the Vietnamese soldiers entered our camp. At first, we didn't know who they were. But when they began speaking to us, some of the boys recognized their language. We discovered that the Cambodian soldiers had all deserted the camp. The Vietnamese were kind to us but they told us to leave. We had hoped and prayed to leave for years, and now that we had the chance, we realized that we had nowhere to go. I left the camp with Savath, my new friend. We headed toward Battambang and luckily my friend met up with his family. Houses did not have electricity or running water. The hospitals, schools, and markers were closed. Food was still scarce.

When I was eighteen, I felt I had to return to Phnom Penh to see if any of my cousins or friends had survived Pol Pot. My house was more than one hundred twenty kilometers from Battambang, and I didn't know the way. I started walking in that general direction. I got on an old train, got rides on wagons, and walked some more. Eventually I arrived in Phnom Penh. As I entered my old neighborhood, my spirit crumbled. My house was burned and my friends' houses were burned. Everything that had once been so familiar was gone. I knew that my life was changed forever.
```

---

## IC-0333: Coax

- Title: Coax
- Author (byline): Neil LaBute
- Work: Wrecks and Other Plays, Pgs 101-114
- Publisher: Faber and Faber
- Publication date as stated: July 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: YOUNG MAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1732
- Already set (do not supply): none

### Source block (context only)

```text
Author: Neil LaBute
Book: Wrecks and Other Plays,
Pgs 101-114
ISBN: 978-0865479708
Publisher: Faber and Faber
Date (Month/Year): July 2007
```

### Introduction (context only: never use it for content warnings)

```text
Coax by Neil LaBute
```

### Performance text (classify this)

```text
Silence. Darkness. YOUNG MAN standing at a sandwich bar, pacing a bit near a round standing table. Bottle of spring water in one hand. He notices us. He carries a manuscript. There should be a distinct difference in the YOUNG MAN’s character when speaking to the audience verses when speaking to the YOUNG WOMAN. His demeanor when speaking to the audience should gradually evolve into something quite sinister.

YOUNG MAN: (directly to judge or female in the audience) Hey! Hello there, how's it going . . . are you . . . ? . . . no. Sorry. I didn't, I'm looking for . . . doesn't matter. Thanks anyway . . . He takes a gulp from the bottle; Looks back at audience, smiles. I don't know why I even said that, "are you . . . ?" because, I mean, look, you're obviously not the person I'm waiting for. (Points to script.) Says so right here. I realize that, I must've . . . you know, it's just that whole weird "theater" thing, right? I mean, you can see me, I know you're there, but hey, let's just pretend it's "real," let's all sit here and act like I'm this college guy who's hanging out in some local spot, waiting to meet up with someone . . . but none of it's really happening, is it? I mean, that's what we're taught to believe, anyway. That's the idea. I could never get my head around that stuff, I mean, that kinda concept. The "fourth wall" thing. It's just so . . . odd.

See, I took some theater in college, I mean "drama," that's what they liked to call it where I went to school, "draaa-ma." Big deal, right? Same difference. Anyhow, I took an intro course once, and this sort of little acting thing, improv or whatever, and I was okay, not like some Charlie Chaplin or anything but kinda good. I had no problem getting up in front of people, or pretending to be somebody else.

I mean, think about it, though, the whole thing's confusing. I'm here, I am, I'm right up here, standing in front of you. That's really happening, isn't it? It's true. So does that make me an actor, or just some guy who's waiting to see somebody, this girl that I met? I dunno, you decide. I mean, You don't know me, I could be anybody. I'm just some dude waiting to see this girl that I hooked up with. But you . . . you are sitting there, thinking, I’m an actor, doing my stuff, and this is all made up and part of the thing. Wow . . .

YOUNG MAN: (Pg 101-114) He checks his watch. She's late . . . or is it just not her cue yet? (Smiles.) So what's the truth? Actor, some guy? Hey, whatever. You figure it out . . . He glances off, spots someone. I think this might be her . . . hold on. (He gestures offstage.) Hey! Hello . . . how's it going? (back to audience) Really cute. See, we met online, not like in a chat room or anything, I don't really get into all that, sitting and talking about music or whatever, but I'll hang around just outside one, you know, like where you can read the names of who's in there, and then I'll just randomly e-mail 'em or strike up one of those instant message things and that'll usually do it . . . (Actor shifts focus on-stage and responds as if a YOUNG WOMAN has entered and put her hand out to the YOUNG MAN, who warmly takes it in his.)

Hi it's great to meet you. Finally . . . (waits for her response) After, like, four months! Didn't think it'd happen . . .

(back to audience) Seems nice . . . She's cute, huh? Yeah. Really cute, And they’re not all that way, believe me. People are usually sorta misleading when you talk to 'em on your laptop. Smarter. Better looking. Or richer. You can easily be whatever you wanna be when you're floating around out there in cyberspace.

She thinks I'm a senior at Milton, studying economics, into John Grisham, hockey, and camping. Which is fine. Let her think that. I do like some of those things, so what's it matter, right? And you, you're still pretty positive I'm an actor, anyway, and this is all some little show that she and I have been rehearsing and stuff . . . but you can't be sure, can you? I mean, not completely. When we walk out of here, a few minutes from now, when I say, "Hey, you wanna go see the sunset? It's beautiful out by the lake 'cause you got a clear shot looking at it back over the mountains there . . ." you'll just think it's a line, right? But is it a line that I read in my script, been practicing, or is it the same thing I say to all the women I meet?

(Beat. Actor shifts focus on-stage to the YOUNG WOMAN) And you're even cuter than you said. Seriously. (waits for her response) So . . . do you get on there much, I mean, online? Talking to people and whatever. (waits for her response) Nah, me either. In fact, I just got my computer, I mean, hooked up to the Internet, like, six months ago, and I just happened to be on that night . . . (waits for her response) It's true . . . sometimes I'll get on there, to talk about music . . . and then . . . we just sorta found each other. Setting up times to meet, typing away to each other, wondering . . . this is better. (Beat.) So, did you tell your boyfriend or not? (waits for her response-which is obviously a “No”) Hey, we're just talking, right? It's only coffee. (Beat) But I gotta tell you, I was jealous, I was, when I heard you were seeing someone. I thought we clicked, really early I felt that, and then when I heard about . . . Jacob . . . well, I just was like, "Damn, this guy's got it going on, this Jacob dude, because this girl is something else. She's special . . . " (Beat.) Anyhow, I'll put the violin away now! Sorry, God, listen to me, I'm just really happy you decided to meet up . . . that's all.

The YOUNG MAN starts offstage but stops, looking at the audience. That was nice, huh? I think it went very well . . . and now we're gonna take off. I'm gonna do the line about the sunset and then we're gonna take her car and drive up the road to this place I know. And that'll be that. Basically. I mean, ol' Jacob might put up a few "missing person" posters downtown or whatever-might even find that he's a suspect there for a while! (Laughs.)

But that's pretty much the whole deal. Or . . . she and I are gonna go backstage, maybe grab a drink and hope the reviews are good . . . You think what you want. Whatever gets you to sleep at night. (Looks back at the YOUNG WOMAN.) I'll give her a chance. I will.

In that class I took, the one I mentioned-the drama one-the teacher told us about what the theater used to be like, not just in places like Paris or wherever, but even here in the States . . . I mean, people used to fight over plays, like, go out in the street and riot and burn places down, start hitting each other right in the aisles because they believed in this movement or Romanticism or whatnot. Can you believe that?

I thought that was kinda neat, that it used to mean that much to 'em . . . Nothing means shit these days. So I'm gonna give you a chance. All your lives you've been told to shut up and watch, just sit there, don't say anything; if you hate it, grab your coat and leave . . . but don't ever say what you feel. Don't make a scene. Well, that's fine, but it's not exactly very passionate, either.

So here's the deal . . . I'm gonna go back over there, ask her up to the lake, and she's gonna go with me. I promise you; she is. Whether it's in this script here, or I'm just such a charmer, you'll have to work that out, but I'm telling you, it's gonna happen. However . . . if you call out and let her know what's going on, what I'm about to do to her, then maybe I'll let her go. Maybe.

I know it sounds a bit goofy, like Peter Pan or some children's show, but if you care about her enough, if you can just, just suspend whatever the hell it is you're supposed to suspend for a couple seconds and think about her, ask yourselves is it worth it to look a little foolish but maybe save that girl, then you say something. Just say it. Out loud right now and maybe she'll hear you. What can it hurt, right? Otherwise, you're always gonna wonder ... (Beat.) Now, maybe you'll see one of us on the subway, or at a restaurant or something and then it'll be okay, all some great big lark . . . but if you don't, I bet it's gonna eat at you a bit. Just a little bit.

This is it, your last chance . . . we're not gonna come out for a curtain call, or be outside in the lobby later. This, right now, is it. So do whatever . . . (When the audience doesn't react-the YOUNG MAN should smile and shake his head, heading back toward the YOUNG WOMAN.) Ha! You’ re worse than I am! Cold, man ...

(Beat. Actor shifts focus on-stage to the YOUNG WOMAN) Hey, you wanna go see the sunset? It's beautiful out by the lake 'cause you got a clear shot looking at it back over the mountains there . . . (waits for her response, which is obviously hesitant) I mean, only if you want to. It's just ... lovely, that's all. (waits for her response, innocently) All right, good . . .

can we take your car?

(To audience.) Well, you had your chance . . . anyway, it's gonna be a really nice evening. I can tell. I know you're heading out after this, but maybe you'll think about it later, tomorrow even, and wonder if I was sh**ing you or not . . . who knows? I love that, though, that uncertainty that you've got now, even if it's only a little. Yeah, I completely get into that!

It's like what I saw in her eyes, just then, that moment when I asked about the lake and she's studying me, noticing the J. Crew and the good haircut and feeling okay that I'm not some Ted Bundy or someone like that and then just jumping off the deep end with a "Sure, why not?" To me, that, right there, is perfect, untroubled happiness. When they look at you, these girls, and they suddenly trust you. Or you, in your little seat there, doing nothing to help her because this isn't "real" but you want to because she's cute and sweet and, you know, what if . . . ?

At that moment when people're just on the edge, right on the very, very edge of it, that place between reality and illusion, and you coax them, that's all, just coax 'em a touch, and they cross over. And then it's too late. (Beat) I love that. Yeah. Love it. I do. (Smiles.) See you around. He starts off, offers his arm to the willing YOUNG WOMAN and exits. Lights slowly fade out behind him. Silence. Darkness.
```

---

## IC-0334: Cobb

- Title: Cobb
- Author (byline): Lee Blessing
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: PEACH, TY, MR. COBB, MR, MR.COBB
- Teaser before the introduction: Yes
- Spoken words (computed): 1611
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lee Blessing
ISBN: 978-0822202240
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
Ty Cob once said, “Baseball was one-hundred percent of my life. It is a game haunted by the spirits of its rich history. Shoeless Jo Jackson, Hank Aaron, Babe Ruth . . . In this selection, Ty Cobb, one of the game’s most enigmatic players, comes back from the grave to sharpen his spikes once more . . . To play to one final crowd. Cobb by Lee Blessing
```

### Performance text (classify this)

```text
Portrays Ty Cobb at 3 different stages of his life

PEACH: Intense, athletic, quick to anger – about 20

TY: Self-Important, quick to anger – about 40

MR. COBB: Bitter, quick to anger – over 70.

MR. COBB: (Pg 7) You think you invented me, but I invented you. You think this life you live is somehow your creation. It isn’t. Everything about you started with men like me. The way you think, the world you live in – all of it shaped by men like me. At the turn of the century I took a rustic, folk-art form called baseball and applied the science of warfare to it. Fit like a damn glove. That's what you owe me. (He suddenly stares out with surprise, and cocks his head as though listening. With a growing tone of accusation). You're trying to forget me. Aren't you? You're trying to forget me. You’re trying to forget.

PEACH: (Pg 8) (With a noticeable Southern drawl- he picks up a bat, holds it out, testing its weight) Look at that. Baseball bat’s a serious item. Now and again I think about how many times one of theses been used to kill somebody. It's a club... is what it is. People use it that way. In homes all over the nation. They club each other to death with the first thing that comes to hand. (He suddenly slams the bat hard against the bench, speaks quietly) I’m the greatest player that ever lived. Ty Cobb (Pg 15)... the Georgia Peach.

MR. COBB: It meant perfection. I became perfection.

PEACH: (Pg 8) My name's been on a lot of bats. So it's been covered in blood, I suppose - - its share of the time. (He makes to slam the bat against the bench again, but suddenly stops, relaxes) It’s no toy. And it’s no game, neither. When I was 18, my mother killed my father.

TY: Babe Ruth was an orphan, and American adopted him. My mother killed my father, and no one wants to know me. (Pg 9) My mother took a lover. That’s what some people said. Personally I think it’s a goddamn vicious lie, but they said it. My father was W.H. Cobb. People called him Professor. School commissioner, newspaper editor, state senator. When he was 21 he married my mother.

PEACH: She was 12.

TY: I was playing with Augusta Tourists in the Sally League. It was 1905. One night, down in Royston, my father said that he was going out to the farm for a couple days. He took the buggy and left my mother alone in the house. She was afraid of being alone. She went to bed. Little after midnight [she] heard a noise outside her window, out on the porch roof. Someone was trying to open the window. She was all alone in the house

PEACH: There was a gun in the room. Papa kept it there, for times of danger. (Pg 10) She just fired. She didn’t look. It could’ve been anybody. Outside that window, on the porch roof -- with all that broken glass --that's where my father died.

TY: He was shot in the stomach -- and in the head. My mother was arrested. Accused of voluntary manslaughter.

MR. COBB: (Pg 11) The son of homicide. See, a myth’s got to have the right kind of start. Look at Babe Ruth. He had a beautiful myth: In a home for wayward boys from the age of seven. His folks couldn’t handle him. A priest became his second father. Boy hero rises from nothing. What did I have? A [damn] Greek tragedy. Where the hell was my second father?

TY: (Pg 23) Put yourself in my place. For seven years you’re the finest player in baseball. Better hitter, better runner, better fielder, better thinker than any man who’s played the game. If an outfielder was slow throwing the ball in, I took an extra base. If someone got in my way, I knocked ‘em down. If they blocked a base, I spiked ‘em. If they wanted to fight over it, I fought ‘em ... anyone. That was the bargain I made with baseball. If I was destined to play a child's game all my life, at least I was going to play it like an adult. (Pg 16-17) They made me feel like an animal. Hell, I learned what “team” meant – it meant them against me.

MR. COBB: It was the way then. You’re there to replace one of ‘em – they don’t take kindly to it.

TY: I was humiliated every day by players not fit to stand on the same field with me. I fought people. Blood, bruises, broken bones – people laid up for days. Careers ended. I had fights. (Pg 19) I fought. That’s who I was. (Pg 21) I was someone! . . . (Pg 23) There’s no damn dignity in the game! None! 5,000 strangers right behind you – like little kinds – Them sitting, you standing up all day. They should vileness. I can think of no other art form in which ignoramuses are expected to scream insults in your face on a daily basis.

MR. COBB: (Subdued) What are they thinking when they shout those things?

PEACH: (Pg 24) (shouting like a fan) Hey, Cobb! Your mother can run better ‘n you!

MR: COBB: Your mother can do everything better ‘n you!

TY: Your mother . . . Your mother!! YOUR MOTHER!

MR. COBB: (Pg 23) What’s in their hearts that makes them need to pull a man down?

TY: (Pg 24) You bear it. As much as possible, anyway. They pick you out. They choose you alone. That more than anything is why you hate them Claude Lueker.

Many times I ignored him. Whole games. Whole series. I shouted back, but I never crossed that railing. I held myself back.

PEACH: But then he figured out something new to say.

TY: (Almost unable to say it) He called me a . . . a “half-nigger.”

PEACH: And up I went – over that railing1 I WENT LIKE A SHOT! His throat was big and white as the moon. I kicked him hard. Nobody could p ull me off him! And I never paused. I just kept kicking. Why? ‘Cause it made me feel so right? (to audience) You think I was right, don’t you?

TY: (Pg 26) Every congressman from Georgia wired me congratulations. The mayor and police chief of Atlanta both supported me. The police chief said if I hadn’t done what I’d done, I’d’ve “lost the respect of every decent man in the country.”

MR.COBB: I did not just fight people . . . I . . . loved.

PEACH: (Pg 43) Whenever I walked into a ballpark, it was like fallin’ in love for the first time – again and again.

MR. COBB: (Pg 26) Who’s going to remember me if they think I was a monster? They’ll toss me away. They'll keep Ruth... him they'll remember for centuries. Me (Trails off, quieter) He’s the one. He’s the damn mountain.

TY: It's not easy to be dethroned. I'd already won eight straight batting titles before Ruth [even] showed up. I even led the league in homers once. Then in 1920, Ruth hit 54. (We hear the crack of a bat, a crowd roars) 54 home runs. No one had ever come near that. Overnight, people went crazy for home runs. They went crazy for him, too. Didn't matter that I could do everything in the game. As far as the fans were concerned, he only had to do one thing.

MR. COBB: (Pg 27) What exactly did Babe Ruth offer? Look at a typical trip to the plate for him. What happens? He takes a cut, hits a home run, trots his way around the base path like a big cow without a thought in his head. That's no trip around the bases.

PEACH: I'll show you a trip around the bases. Cobb style. It starts with a few carefully-chosen words to the pitcher. Thigs like, “Hey, Rag-arm! That can’t be your fastball. (picks up a bat, demonstrating)

MR. COBB: You hit a liner -- not some soft, lazy fly ball that flops into the stands someplace. No. You hit a bullet. You sizzle it past the pitcher's ear. Make him glad just to be alive.

TY: Then you run to first like (Pg 28) you're legging out a triple.

PEACH: Just the sight of speed can demoralize the other team.

TY: Once you’re on first, you start to systematically destroy the pitcher's mind. It's not hard...

PEACH: And when he makes that little unconscious gesture that means he's going home and not to first

MR. COBB: You take off!

PEACH: And that catcher sees you go, and his heart turns to cinder ‘cause he knows you already got the base stole..

TY: But he know he’s got to throw it anyway, so’s not to look like a coward.

MR. COBB: No mercy for cowards!

PEACH: (Pg 29) The throw’s low! Safe at third. On a single. But not home yet!

MR. COBB: On the very next pitch, I take a long, walking lead off third. When the pitcher goes home so do I.

PEACH: There’s no pleasure on earth like stealin’ home. You've got to force your way in.

TY: If he drops the ball you're safe. You got to do anything. You got to hit him... bruise him.... break his arm, his leg, and his ribs. You got to smell his blood. You got to put your spikes in his chest! You got to score!

PEACH: (Pg 30) You can bet Babe Ruth never took that trip. Or ever could. I could hit home runs. But he could never move around the bases like me. (Pg 37) Most hits, most runs scored, most stolen bases , most singles, most triples. Most records.

TY: (Pg 48) When they opened the Hall of Fame in 1939, the first thing they put in it was a pair of shoes. My shoes. My spikes. The first symbol of baseball to enter that building. They didn't have to choose ‘em. Babe Ruth had plenty of stuff lying around. But they chose my spikes because they truly knew the game.

MR. COBB: (Pg 49) What’s it matter? Ruth was the game. You should’ve seen people when Babe Ruth died. Sure he died young, but still.

PEACH: The whole city of New York wept. Whole nation.

MR. COBB: When I went, I just . . . went. Good myth should go out with more than that.

PEACH: Ty Cobb died of cancer in a hospital when he was old and unconscious.

TY: The most hated man in baseball.

PEACH: My father died better than me.

TY: I was too real for myths. You couldn’t sell what I was.

MR. COBB: (Pg 50) No man wants to be forgotten. Every man wants someone to remember. I was the quickest, meanest, smartest, fiercest . . . best . . . man to ever play the game... just remember.
```

---

## IC-0335: Cold Storage

- Title: Cold Storage
- Author (byline): Ronald Ribman
- Work: Not specified
- Publisher: Avon Books
- Publication date as stated: Sept 1983
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: PARMIGIAN, LANDAU
- Teaser before the introduction: Yes
- Spoken words (computed): 1738
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ronald Ribman
ISBN: 978-0380400065
Publisher: Avon Books
Date (Month/Year): Sept 1983
```

### Introduction (context only: never use it for content warnings)

```text
“You have cancer.” The tragically-common, often literal death sentence no one wants to hear. What do you do? How do you respond to those life-threatening words? Chemotherapy, radiation? Humor or depression . . . denial? In Cold Storage by Ronald Ribman, we meet to men with very different responses to the diagnosis of cancer. Some see a hopeless end, while others see an endless hope.
```

### Performance text (classify this)

```text
(LANDAU takes a bite of a candy bar which is stale and tastes bad, he tries to re-wrap it and looks for a place to throw it away)

PARMIGIAN: You're squashing it. You’re squashing it!

LANDAU: What?

PARMIGIAN: If ya don't want it give it to me! (pause) There's no point in squashing something just because you don't want it! What are you saving it for Halloween?

LANDAU: I’ll throw (the candy) it away later there’s no garbage out here.

PARMIGIAN: Don’t throw it away later. Throw it away now. What are you in for anyway?

LANDAU: Exploratory surgery.

PARMIGIAN: Oh yeah? What are they exploring for? Cancer? (laugh)

LANDAU: It was just a shadow on an x-ray of my stomach, a few cells they weren’t quite sure about.

PARMIGIAN: Sure

LANDAU: Really just a small twinge. I don’t even feel it anymore.

PARMIGIAN: Whatta ya working on, Landau?

LANDAU: I don’t understand

PARMIGIAN: Sure you understand. What are you working on? An ulcer? Is that what you’re working on for yourself? I told them I had a tickle in the throat. Honest to God, that’s what I thought I had. I came through the door and told them I had a tickle in my throat!

(laughter stops) Take my word for it. On this floor, it’s never a twinge in the stomach or tickle in the throat. You got what I got.

LANDAU: What’s that?

PARMIGIAN: The big C.

PARMIGIAN: Yep, you’re going down for the count, same as me.

LANDAU: On the contrary, Mr. Parmigian, I’m just here for exploratory surgery.

PARMIGIAN: Sure, and you’re all dressed up in your Bloomingdales pajamas. You look…. Spiffy

LANDAU: Thank you.

PARMIGIAN: You know what I weighed six months ago? 252 pounds. I looked spiffy too. I was the King Kong of the fruit and vegetable business. I had a fist like two hammocks. Now I can’t even find them anymore. I tell ‘em my clothing don’t fit me anymore, they tell me the hospital laundry must be stretching them out. Can you believe such a pack of crap? You have to be a moron to believe something like that. What did you used to do for a living?

LANDAU: I didn’t used to do anything Mr. Parmigian, I’m still doing it. I’m an investment advisor in fine art.

PARMIGIAN: Oh yeah? What the hell’s an investment advisor in fine art?

LANDAU: I recommend investment purchases in fine art to investors interested in capital appreciation. I generally handle accounts in European glass and Chinese ceramics.

PARMIGIAN: Hey that’s terrific, that’s really terrific…. Listen, Do you have any recommendations for long term growth? (he laughs – starts to cough bad).

LANDAU: Are you all right, Mr. Parmigian? Mr. Parmigian. (When he doesn’t answer him, Landau starts to get nervous) I’ll get a nurse. I’ll be right back.

PARMIGIAN: (grabbing his arm) Don’t bother. (tries to gets breath back)

LANDAU: Are you sure?

PARMIGIAN: Yes, I’m sure! I’m sure! It only hurts when I try and stay alive. When I make jokes and try to stay alive. Listen, you want to do me a favor?

LANDAU: If I can yes.

PARMIGIAN: Don’t worry, it’s just a little favor. Get behind me and push me off the roof.

LANDAU: What?

PARMIGIAN: I’d do it myself but I don’t have the guts.

LANDAU: I really don’t think you ought to joke about that.

PARMIGIAN: You think it’s a joke? Come on be a sport, do it now and you’ll be just in time for the six o’clock news. “Incredible man splatters to death on pavement in front of Hope Memorial Hospital.” You’ll be famous for five or six minutes.

LANDAU: I have no desire to be famous at the cost of somebody else’s life.

PARMIGIAN: I’ll make it interesting for you. As soon as you push me off the roof I’ll go into a triple summersault fold up like a jack knife and do a swan dive through the entrance awning. You live another six months you won’t see that again.

LANDAU: I’m not going to listen to this. I don’t know whether you’re joking or not but I’m not going to listen to this.

PARMIGIAN: Alright I’ll do it myself.

LANDAU: No!

PARMIGIAN: Take your hand off me or I’ll bite it off!

LANDAU: You’re not going to bite anything off.

PARMIGIAN: I’m warning you. Aright, you win. I don’t have the energy to fight with anybody. I want a Doctor Pepper. Go inside and get me a Doctor Pepper I’m thirsty.

LANDAU: Not now.

PARMIGIAN: What’s the matter? It disturbs you?

LANDAU: Seeing somebody try to take their own life? Yes, it disturbs me. Nobody has the right to do something like that.

PARMIGIAN: Why not? Whose life is it?

LANDAU: That’s not the point. The point is… Look they’re coming up with something.

PARMIGIAN: They’re coming up with nothing.

LANDAU: Don’t say that. They’re making fantastic progress all the time. Just last Sunday I read and article in The Times about how cockroaches can’t get cancer.

PARMIGIAN: That’s wonderful news if you’re a cockroach.

LANDAU: That’s not the point. If they can’t give cockroaches cancer, maybe they can find out what it is that prevents cancer.

PARMIGIAN: You want to know what prevents cancer? Death! Death prevents cancer.

LANDAU: Well, with that attitude you might as well just give up.

PARMIGIAN: I have. Push me off the roof.

LANDAU: Look, I can’t handle this kind of thing right now! I just (catching himself then offering up hope of ending the conversation.) You’re just depressed. Tomorrow you’ll be glad you’re still alive.

PARMIGIAN: No I won’t.

LANDAU: Yes, you will, believe me.

PARMIGIAN: No, I won’t, and why should I believe you?

LANDAU: Because people SURVIVE! They go on! They live. Nobody tries to commit suicide unless they’re depressed.

PARMIGIAN: I happen to be in a very good mood Mr. Landau or hadn’t you noticed? The sun is shining; the dogs are peeing all over the side walk. The best time to commit suicide is when you’re in a good mood. I tried to commit suicide three times this month, and never once was I in a bad mood.

LANDAU: Why do you insist on involving me with this?

PARMIGIAN: To tell you the truth, the reason I asked you is that I don’t have the courage myself. What I said about not having any guts is true, literally. They took out my bladder, shaved off my prostate, and tied my bowels to my hip bone. See… Now my urine flows with my blood, and when I shake my leg, my liver drips prostatic fluid on my shoes. And that’s the good news. Want to hear some bad news? Last week I ran outta Blue Cross.

LANDAU: Oh, I’m sorry. It must be terrible watching your estate being destroyed by an illness.

PARMIGIAN: It’s not an estate; it’s a fruit and vegetable business. It’s always been my dream. I’ll tell you what, Landau. You tell me your filthy dreams and I’ll tell you mine.

LANDAU: I have no dreams that would interest anybody.

PARMIGIAN: You would be surprised at what interests me. The closer I get to death, the more everything interests me. Dreams other people throw out with the garbage I can spend a whole day living on.

LANDAU: I have no dreams of interest to anybody.

PARMIGIAN: What an absolutely marvelous quality of surface veneer you have, Mr. Landau.

LANDAU: If you’re interested in surface veneer, perhaps I might show you something in a 19th century Chinese lacquer box. You might find it interesting to see how coat upon coat of lacquer can be laid down until the box itself may be removed leaving nothing behind but the form and the lacquer – the black, brilliant, slightly poisonous lacquer. (pause) I’m sorry to disappoint you, Mr. Parmigian, but there’s nothing in me you’re going to be able to live on. I’ve got nothing to give you.

PARMIGIAN: Nothing?

LANDAU: Nothing.

PARMIGIAN: All right, I’ll accept that lie. There’s no point in being too pushy the first ten minutes you meet somebody. First you should break the ice, so I’ll give a riddle. What’s shaped like a big green football with four legs and a tail?

LANDAU: How outrageous you are.

PARMIGIAN: Not the answer.

LANDAU: I don’t know the answer.

PARMIGIAN: A watermelon.

LANDAU: A watermelon doesn’t have four legs and a tale!

PARMIGIAN: I lied. Where are you going?

LANDAU: I have an appointment down in the x-ray room this afternoon. I have to swallow something and they’re going to x-ray it.

PARMIGIAN: That’s a terrific test. You’ll like it.

LANDAU: You had that test?

PARMIGIAN: Oh sure. That’s one of the best procedures in the hospital.

LANDAU: I’ll be home in a few days. Time enough to have a few friends over for dinner.

PARMIGIAN: Oh yea, that’s right. You’re just in for an exploratory. I forgot. Tell me something, Landau. You seem to be in pretty good physical shape. You do something?

LANDAU: I play squash a couple of afternoons a week, and on the weekends some tennis if I can get away.

PARMIGIAN: Listen, your cardiovascular system stays in good shape there’s no reason why you couldn’t go on living until this time next year.

LANDAU: I wish you’d stop doing that.

PARMIGIAN: Doing what?

LANDAU: Implying that there is something wrong with me.

PARMIGIAN: Was that what I was doing?

LANDAU: YES! THAT’S ENOUGH!

PARMIGIAN: If you don’t like what I’m saying push me off the roof! You’re a pretty violent man, Mr. Landau.

LANDAU: I’m not violent. You just irritated me, that’s all. I hate violence.

PARMIGIAN: It doesn’t pay to get irritated. You’ll probably be out in two or three weeks.

LANDAU: You think so?

PARMIGIAN: No.

LANDAU: What’s the matter with you?

PARMIGIAN: That’s pretty obvious isn’t it?

LANDAU: I’m not talking about that. You don’t seem to give an ounce of thought to what you’re saying! You don’t know anything about me!

PARMIGIAN: That’s right.

LANDAU: You bet that’s right so knock it off!

PARMIGIAN: I apologize.

LANDAU: All right let’s just forget it.

PARMIGIAN: Oh, what a great liar you are.

LANDAU: What lie?

PARMIGIAN: Death is knocking on your door and still you persist in lying to yourself.

LANDAU: That’s garbage! Absolute garbage!

PARMIGIAN: You deny it?

LANDAU: Yes of course I deny it!

PARMIGIAN: Naturally, of course.

LANDAU: What the hell is that supposed to mean!

PARMIGIAN: What’s the matter I touched a nerve?

LANDAU: Forget it I don’t have time for this.

PARMIGIAN: You got at least six months.

LANDAU: STOP IT! Talking to you! Trying to talk to you… it’s… it’s

PARMIGIAN: Absurd?

LANDAU: It’s humiliating!

PARMIGIAN: Of course it’s humiliating. You know why? Because the mind’s a piece of garbage. It’s never happy with what you do for it. I once took my mind down to Barbados for two weeks and you know what it said to me? “You should have taken us to Jamaica.” The real reason Adam and Eve got thrown out of the Garden had nothing to do with fruit. Because there’s nothing wrong with a piece of fruit. It’s a good laxative. God finally got tired of waiting around for thanks from the human brain.

LANDAU: Oh god . . . I’m going inside now Mr. Parmigian. I have to go to x-ray.

PARMIGIAN: Landau?

LANDAU: Yes?

PARMIGIAN: I’ll meet you out here tomorrow?

LANDAU: Okay.

PARMIGIAN: I promise you a very interesting day.
```

---

## IC-0336: The Color of Water

- Title: The Color of Water
- Author (byline): James McBride
- Work: Not specified
- Publisher: Riverhead Books
- Publication date as stated: Feb 2006
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JAMES, RICHIE, MOMMY, DAUGHTER
- Teaser before the introduction: Yes
- Spoken words (computed): 2039
- Already set (do not supply): none

### Source block (context only)

```text
Author: James McBride
ISBN: 978-1594481925 (10th Anniversary Edition)
Publisher: Riverhead Books
Date (Month/Year): Feb 2006
```

### Introduction (context only: never use it for content warnings)

```text
It took James McBride 14 years to unearth his mother’s remarkable story – the daughter of an Orthodox Jewish rabbi who married a black man in 1942. In this excerpt, James examines her life, his own childhood in Brooklyn’s housing projects, and the force of his mother’s love. The Color of Water: A Black Man’s Tribute to His White Mother by James McBride
```

### Performance text (classify this)

```text
JAMES: (Pg xvii) As a boy, I never knew where my mother was from – where she was born, who her parents were. When I asked she’d say, “God made me.” When I asked if she was white, she’d say, “I’m light-skinned,” and change the subject. She raised 12 black children and sent us all to college and in most cases graduate school. Her children became doctors, professors, chemists, teachers - yet none of us even knew her maiden name until we were grown.

JAMES: (Pg 21-25) Answering questions about her personal history did not jibe with Mommy’s view of parenting twelve curious, wild, brown-skinned children. She issued orders and her rule was law. Since she refused to divulge details about herself or her past, and because my stepfather was largely unavailable to deal with questions about himself or Ma, what I learned of Mommy’s past I learned from my siblings. We traded information on Mommy the way people trade baseball cards, offering bits and pieces fraught with gossip, nonsense, wisdom, and sometimes just plain foolishness.

RICHIE: What does it matter to you? You’re adopted anyway.

JAMES: You’re lying.

RICHIE: You’ll see when Mommy takes you back to your real mother next week. Why do you think she’s been so nice to you all week?

JAMES: Suddenly, it occurred to me that Mommy had been nice to me all week. But wasn’t she nice to me all the time? I couldn’t remember, partly because within my confused 8-year-old reasoning was a growing fear that maybe Richie was right. Mommy, after all, did not really look like me. In fact, she didn’t look like Richie, or David – or any of her children for that matter. We were all clearly black, of various shades of brown, some light brown, some medium brown, some very light-skinned. And all of us had curly hair. Mommy was, by her own definition, “light-skinned,” a statement which I had initially accepted as fact but at some point later decided was not true. There was something inside me that told me. It was in my blood, you might say. Yet Mommy refused to acknowledge her whiteness. Why she did so was not clear, but even my teachers seemed to know she was white and I wasn’t. On open school nights, the question most often asked by my schoolteachers was, “Is James adopted?” which always prompted an outraged response from Mommy.

JAMES: If I’m adopted, you’re adopted too.

RICHIE: Nope. Just you, and you’re going back to your real mother in jail.

JAMES: I’ll run away first.

RICHIE: You can’t do that. Mommy will get in trouble if you do that. You don’t want to see Ma get in trouble, do you?

JAMES: (Panic setting in) But I don’t want to go to my real mother. I want to stay here with Ma. . .

RICHIE: You gotta go. I’m sorry, man.

JAMES: This went on until I was in tears. I remember pacing about nervously all day while Richie, knowing he had ruined my life, cackled himself to sleep. That night I law wide awake in bed waiting for Mommy to get home from work at 2 a.m.

MOMMY: (laughing) You’re not adopted.

JAMES: So you’re my real mother?

MOMMY: Of course I am. (big kiss) You want some coffee cake?

JAMES: Enough said . . . In 1966, when I was 9, black power had permeated every element of my neighborhood in St. Albans, Queens. Malcolm X had been killed the year before and had grown larger in death than in life. Afros were in style. The Black Panthers were a force. Congas played at night on the streets. (Pg 26-30) But there was a part of me that feared black power very deeply for the obvious reason. I thought black power would be the end of my mother. I had swallowed the white man’s fear of the Negro, as we were called back then, whole. It began with a sober white newsman on our black-and-white television set introducing a news clip showing a Black Panther rally led by one of those black militant leaders, screaming to hundreds and hundreds of angry African-American students, “Black power! Black power! Black power!” while the crowd roared. I thought to myself, these people will kill Mommy. Mommy, on the other hand, seemed unconcerned. Her motto was,

MOMMY: If it doesn’t involve your going to school or church, I could care less about it and my answer is no whatever it is.

JAMES: She insisted on absolute privacy, excellent school grades, and trusted no outsiders of either race. But even if she had any interest in black power, she had no time to talk about it. She worked the swing shift at Chase Manhattan Bank as a typist, leaving home at 3 p.m. and returning around 2 a.m., so she had little time for games. On his end, my father, Andrew McBride, a Baptist minister, had his doubts about the world accepting his mixed family. He always made sure his kids never got into trouble, was concerned about money, and trusted the providence of the Holy Father to do the rest. After he died and Mommy remarried; my stepfather, Hunter Jordan, seemed to pick up where my father left off, insistent on education and church.

On her end, Mommy had no model for raising us other than the experience of her own Orthodox Jewish family which represented the best and worst of the immigrant mentality: hard work, no nonsense, quest for excellence, and a deep belief in God and education. They believed that money without knowledge was worthless, that education tempered with religion was the way to climb out of poverty in America, and over the years they were proved right. Yet conflict was a part of our lives. Mommy’s contradictions crashed and slammed against one another like bumper cars at Coney Island. White folks, she felt, were implicitly evil toward blacks, yet she forced us to go to white schools to get the best education. Blacks could be trusted more, but anything involving blacks was probably slightly substandard. She couldn’t stand racists of either color and had great distaste for bourgeois blacks who sought to emulate rich whites by putting on airs and

MOMMY: . . . doing silly things like covering their couches with plastic and holding teacups with their pinkies out. (hissing) What fools!

JAMES: (Pg 32-33) When Malcolm X talked about “the white devil” Mommy simply felt those references didn’t apply to her. She viewed the civil rights achievements of black Americans with pride, as if they were her own. And she herself occasionally talked about “the white man” in the third person, as if she had nothing to do with him, and in fact she didn’t, since most of her friends and social circle were black women from church.

MOMMY: What’s the matter with these white folks?” (reading the newspaper) They’re fighting over this man’s money now that he’s dead. None of them wanted him when he was alive, and now look at them. Forget it, honey. (she’s talking to the newspaper) Your husband’s dead, okay? He’s dead – poop! You had your chance. Is money gonna bring him back? No!

JAMES: Then she’d turn to us and deliver the invariable lecture:

MOMMY: You don’t need money. What’s money if your mind is empty! Educate your mind! Is this world crazy or am I the crazy one? It’s probably me.

JAMES: Indeed it probably was – at least, I thought so. I knew of no other white woman who would board the subway in Manhattan at one o’clock every morning and fall asleep till she got to her stop in Queens 45 minutes later. Her lack of fear for her safety – particularly among blacks, where she often stuck out like a sore thumb and seemed an easy target for muggers – had me stumped. As a grown man, I understand now, understand how her Christian principles and trust in God kept her going through all her life’s battles, but as a boy, my faith was not that strong. Mommy once took me to Harlem. When we got off the bus, two black men came up behind us and one of them grabbed Mommy’s purse. (Pg 35) It seemed that the only white person for miles was my own mother. (Pg 34) The incident confirmed my fears that Mommy was always in danger. (Pg 45) Mommy loved God. She went to church each and every Sunday, the only white person in sight, butchering the lovely hymns with a singing voice that sounded like a cross between a cold engine trying to crank on an October morning and a whining Maytag washer. My siblings and I would muffle our laughter as Mommy dug into hymns with verve and gusto:

MOMMY: Leaning. . . .oh, leannnning . . . safe and secure on the --- *

JAMES: Up, up, and away she went, her shrill voice climbing higher and higher. (Pg 50-51) Even as a boy I knew God was all-powerful because of Mommy’s utter deference to Him, and also because she would occasionally do something in church that I never saw her do at home or anywhere else: at some point in the service, usually when the congregation was singing one of her favorite songs, like “What a Friend We Have in Jesus,” she would bow down her head and weep. It was the only time I ever saw her cry. I asked her one afternoon after service . . .

JAMES: Why do you cry in church?

MOMMY: Because God makes me happy.

JAMES: Then why cry?

MOMMY: I’m crying ‘cause I’m happy. Anything wrong with that?

JAMES: But there was [something wrong], because happy people did not seem to cry like she did. Mommy’s tears seemed to come from somewhere else, a place far away, a place inside her that she never let any of us children visit, and even as a boy I felt there was pain behind them. I thought it was because she wanted to be black like everyone else in church, because maybe God liked black people better, and one afternoon on the way home from church I asked her whether God was black or white.

MOMMY: (a deep sigh) Oh boy. . . God’s not black. He’s not white. He’s a spirit.

JAMES: Does he like black or white people better?

MOMMY: He loves all people. He’s a spirit.

JAMES: What color is God’s spirit?

MOMMY: It doesn’t have a color. God is the color of water. Water doesn’t have a color.

JAMES: (Pg 274) There are probably a hundred reasons why [Mommy] should have stayed on the Jewish side, instead of taking New Jersey Transit and the F train to go to a Christian church in Brooklyn, but I'm glad she came over to the African- American side. She married two extraordinary men and raised twelve very creative and talented children [who became doctors, professors, chemists, and teachers]. (Pg 277) Like any family we have problems, but we have always been close. Through marriage and adoptions, the original dozen has expanded into dozens and dozens more -- wives, husbands, children, grandchildren, cousins, nieces, nephews -- ranging from dark-skinned to light-skinned; from black kinky hair to blond hair and blue eyes. In running from her past, Mommy has created her own nation. (Afterword to the 10th Anniversary Edition) I have met hundreds of mothers – African American, Jewish, European, Arab, Latino, African, Muslim, Christian, Hindu, Buddhist – and all of them understand that family love, a mother’s love gives us grace, courage, and power beyond measure. One afternoon, a few years ago, my African American daughter, who was about eight years old asked me:

DAUGHTER: “Daddy, if Grandma is your mother, how come she doesn’t look like me or you?”

JAMES: I gave her the only answer I could: I don’t know. But she loves us, and that’s the most important thing. In all the important ways, my family’s story is not unique. It plays out across the world, on every continent, in every nation, city, town and village every day. Family love: It is firm footing, something to cling to in a frightened world that seems to spin out of control with war, turmoil, terrorism and uncertainty. It is our highest calling and our greatest nobility. So if you see a woman driving in Trenton with her blinkers on, look out. Back off. Give her some space. She could go left, she could go right. She could go up into Heaven clear out of sight! But no matter which way she goes, she’s not likely going your way. And if she is, don’t bother her with any questions about it, or you’ll get an earful of God.
```

---

## IC-0337: The Congo: A Study of the Negro Race

- Title: The Congo: A Study of the Negro Race
- Author (byline): Vachel Lindsay
- Work: Not specified
- Publisher: Dover Publications
- Publication date as stated: Sept 1992
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1319
- Already set (do not supply): none

### Source block (context only)

```text
Author: Vachel Lindsay
ISBN: 0486272729
Publisher: Dover Publications
Date (Month/Year): Sept 1992
FORENSICS AWARDS
2010 National Qualifier-DI
```

### Introduction (context only: never use it for content warnings)

```text
Vachel Lindsay is often ignored in analogies of twentieth-century poetry because he is judged to be exceptionally reactionary in his racism. However, when Lindsay justified his pacifism during World War I, he said he would rather have died "of his own will mounting a blazing pyre . . . by the side or in place of some black who had not trial by jury" than in the trenches.” He held a conviction that "the only way to end lynching would be to thrust
```

### Performance text (classify this)

```text
yourself into the thick of such a mob and make the men slay you instead of the Negro. Was Lindsay too controversial for America nearly 100 years ago? Is he too controversial for America today . . . or does he perhaps provide and insight into the cultural history of African Americans which is too seldom recognized? The Congo by Vachel Lindsay. I. Their Basic Savagery Fat black bucks in a wine-barrel room, Barrel-house kings, with feet unstable,

# A deep rolling bass. #
Sagged and reeled and pounded on the table,
Pounded on the table,
Beat an empty barrel with the handle of a broom,
Hard as they were able,
Boom, boom, BOOM,
With a silk umbrella and the handle of a broom,
Boomlay, boomlay, boomlay, BOOM.
THEN I had religion, THEN I had a vision.
I could not turn from their revel in derision.

# More deliberate. Solemnly chanted. # THEN I SAW THE CONGO, CREEPING THROUGH THE BLACK, CUTTING THROUGH THE FOREST WITH A GOLDEN TRACK.

Then along that riverbank
A thousand miles
Tattooed cannibals danced in files;
Then I heard the boom of the blood-lust song

# A rapidly piling climax of speed and racket. #
And a thigh-bone beating on a tin-pan gong.
And "BLOOD" screamed the whistles and the fifes of the warriors,
"BLOOD" screamed the skull-faced, lean witch-doctors,
"Whirl ye the deadly voo-doo rattle,
Harry the uplands,
Steal all the cattle,
Rattle-rattle, rattle-rattle,
Bing.
Boomlay, boomlay, boomlay, BOOM,"

# With a philosophic pause. #
A roaring, epic, rag-time tune
From the mouth of the Congo
To the Mountains of the Moon.
Death is an Elephant,

# Shrilly and with a heavily accented metre. #
Torch-eyed and horrible,
Foam-flanked and terrible.
BOOM, steal the pygmies,
BOOM, kill the Arabs,
BOOM, kill the white men,
HOO, HOO, HOO.

# Like the wind in the chimney. #
Listen to the yell of Leopold's ghost
Burning in Hell for his hand-maimed host.
Hear how the demons chuckle and yell
Cutting his hands off, down in Hell.
Listen to the creepy proclamation,
Blown through the lairs of the forest-nation,
Blown past the white-ants' hill of clay,
Blown past the marsh where the butterflies play: --
"Be careful what you do,
# All the”o” sounds very golden. Heavy accents very heavy. Light accents very light.
Last line whispered. #
Or Mumbo-Jumbo, God of the Congo,
And all of the other
Gods of the Congo,
Mumbo-Jumbo will hoo-doo you,
Mumbo-Jumbo will hoo-doo you,
Mumbo-Jumbo will hoo-doo you."

II. Their Irrepressible High Spirits

# Rather shrill and high. #
Wild crap-shooters with a whoop and a call
Danced the juba in their gambling-hall
And laughed fit to kill, and shook the town,
And guyed the policemen and laughed them down
With a boomlay, boomlay, boomlay, BOOM.

# Read exactly as in first section. # THEN I SAW THE CONGO, CREEPING THROUGH THE BLACK, CUTTING THROUGH THE FOREST WITH A GOLDEN TRACK.

# Lay emphasis on the delicate ideas. Keep as light-footed as possible. #
A negro fairyland swung into view,
A minstrel river
Where dreams come true.
The ebony palace soared on high
Through the blossoming trees to the evening sky.
The inlaid porches and casements shone
With gold and ivory and elephant-bone.
And the black crowd laughed till their sides were sore
At the baboon butler in the agate door,
And the well-known tunes of the parrot band
That trilled on the bushes of that magic land.

# With pomposity. #
A troupe of skull-faced witch-men came
Through the agate doorway in suits of flame,
Yea, long-tailed coats with a gold-leaf crust
And hats that were covered with diamond-dust.
And the crowd in the court gave a whoop and a call
And danced the juba from wall to wall.

# With a great deliberation and ghostliness. #
But the witch-men suddenly stilled the throng
With a stern cold glare, and a stern old song: --
"Mumbo-Jumbo will hoo-doo you." . . .

# With overwhelming assurance, good cheer, and pomp. #
Just then from the doorway, as fat as shotes,
Came the cake-walk princes in their long red coats,
Canes with a brilliant lacquer shine,
And tall silk hats that were red as wine.

# With growing speed and sharply marked dance-rhythm. #
And they pranced with their butterfly partners there,
Coal-black maidens with pearls in their hair,
Knee-skirts trimmed with the jassamine sweet,
And bells on their ankles and little black feet.
And the couples railed at the chant and the frown
Of the witch-men lean, and laughed them down.
(O rare was the revel, and well worth while
That made those glowering witch-men smile.)
The cake-walk royalty then began
To walk for a cake that was tall as a man
To the tune of "Boomlay, boomlay, BOOM,"

# With a touch of negro dialect, and as rapidly as possible toward the end. #
While the witch-men laughed, with a sinister air,
And sang with the scalawags prancing there: --
"Walk with care, walk with care,
Or Mumbo-Jumbo, God of the Congo,
And all of the other
Gods of the Congo,
Mumbo-Jumbo will hoo-doo you.
Beware, beware, walk with care,
Boomlay, boomlay, boomlay, boom.
Boomlay, boomlay, boomlay, boom,
Boomlay, boomlay, boomlay, boom,
Boomlay, boomlay, boomlay,
BOOM."

# Slow philosophic calm. # Oh rare was the revel, and well worth while That made those glowering witch-men smile.

III. The Hope of their Religion

# Heavy bass. With a literal imitation of camp-meeting racket, and trance. #
A good old negro in the slums of the town
Preached at a sister for her velvet gown.
Howled at a brother for his low-down ways,
His prowling, guzzling, sneak-thief days.
Beat on the Bible till he wore it out
Starting the jubilee revival shout.
And some had visions, as they stood on chairs,
And sang of Jacob, and the golden stairs,
And they all repented, a thousand strong
From their stupor and savagery and sin and wrong
And slammed with their hymn books till they shook the room
With "glory, glory, glory,"
And "Boom, boom, BOOM."

# Exactly as in the first section. Begin with terror and power, end with joy. #
THEN I SAW THE CONGO, CREEPING THROUGH THE BLACK
CUTTING THROUGH THE JUNGLE WITH A GOLDEN TRACK.
And the gray sky opened like a new-rent veil
And showed the apostles with their coats of mail.

In bright white steele they were seated round
And their fire-eyes watched where the Congo wound.
And the twelve Apostles, from their thrones on high
Thrilled all the forest with their heavenly cry: --

# Sung to the tune of "Hark, ten thousand harps and voices". #
"Mumbo-Jumbo will die in the jungle;
Never again will he hoo-doo you,
Never again will he hoo-doo you."

# With growing deliberation and joy. #
Then along that river, a thousand miles
The vine-snared trees fell down in files.
Pioneer angels cleared the way
For a Congo paradise, for babes at play,
For sacred capitals, for temples clean.
Gone were the skull-faced witch-men lean.

# In a rather high key -- as delicately as possible. #
There, where the wild ghost-gods had wailed
A million boats of the angels sailed
With oars of silver, and prows of blue
And silken pennants that the sun shone through.
'Twas a land transfigured, 'twas a new creation.
Oh, a singing wind swept the negro nation
And on through the backwoods clearing flew: --

# To the tune of "Hark, ten thousand harps and voices". #
"Mumbo-Jumbo is dead in the jungle.
Never again will he hoo-doo you.
Never again will he hoo-doo you."

Redeemed were the forests, the beasts and the men,
And only the vulture dared again
By the far, lone mountains of the moon
To cry, in the silence, the Congo tune: --

# Dying down into a penetrating, terrified whisper. #
"Mumbo-Jumbo will hoo-doo you,
Mumbo-Jumbo will hoo-doo you.
Mumbo . . . Jumbo . . . will . . . hoo-doo . . . you."
```

---

## IC-0338: Continuing Education

- Title: Continuing Education
- Author (byline): Jordan Douglas
- Work: Speak Out (James Doyle ed)
- Publisher: Lulu.com
- Publication date as stated: March 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ROBERT, EVIE, PRINCIPAL
- Teaser before the introduction: Yes
- Spoken words (computed): 2059
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jordan Douglas
Book: Speak Out (James Doyle ed)
ISBN: 978-1300800798
Publisher: Lulu.com
Date (Month/Year): March 2013
```

### Introduction (context only: never use it for content warnings)

```text
Continuing Education by Jordan Douglas
```

### Performance text (classify this)

```text
ROBERT: (Pg 34-38) You’ll have to forgive me. I’m not very good with words. I’m a numbers guy. But I never could get my thoughts in order. I think that’s why when I meet people who used to know me in high school and I tell them I became a teacher, they give me one of these looks like . . . (does the look) . . . But, hey, I don’t blame them . . . I was never the brightest kid in my class . . . I wasn’t a dunce either, but I don’t think anybody was expecting much of me. So when they move back home to start a family of their own and find out that I’m the one who’s going to be teaching their kids . . . well, let’s just say they have their reservations. But, hey . . . It’s 7th grade algebra. It doesn’t take a genius. Truth is, I never expected to become a teacher myself. But when I met Evangeline . . . I changed my mind. Hell, when I met Evangeline . . . everything changed.

ROBERT: Evangeline and I met in college. First day. Now I had barely gotten accepted and my parents were thrilled because I was the first one in my family. So, I’m sitting there in my freshman composition class ready to work my tail off and do my family proud when all of a sudden . . . BAM! In walks Evangeline . . . She looks around for a seat and I don’t think she noticed me . . . ok, she didn’t notice me . . . at all . . . but I noticed her. Her long, brown hair and her eyes . . . she had these green eyes that just . . . they were magic. Like little crystal balls or something . . . . I was hypnotized . . . they made my heart stop. Everything stopped. I don’t think I even started to breathe again until class was over and she walked out of the room. Needless to say that’s all I remember from my freshman comp class.

I started to wait outside class until she went in just so I could get a seat next to her. Of course, Evie was no dunce. Not at all. She was as sharp as a tack. So . . . she noticed my childish attempts at flirting . . . Our first conversation went something like this: Hi. . . hi, there . . . it’s Evangeline? Right? I mean, of course it’s Evangeline. I mean, I hear the teacher call your name in class and I see you walking around campus all the time. I mean, not like I’m stalking you or anything, ‘cause that would be creepy (uncomfortable laugh) I mean . . . I . . . I like your . . . I mean, you have a nice . . . uh . . . book. Nice book.

EVIE: Uh . . . thank you . . . ? I see you have one too . . . The book . . .

ROBERT: Right! Right! Because we’re in the same class! (uncomfortable laugh) Oh, God, this is going to badly . . . .

EVIE: No! No . . . you’re doing great.

ROBERT: Really? You think so?

EVIE: Sure! Just go ahead and ask me to go to lunch with you after class. Go on. Give it a try.

ROBERT: Oh. Oh! Ok . . . Evangeline . . . would you go with me to lunch after class?

EVIE: Yes. I would.

ROBERT: You would? I mean you would! Great! Great! I mean . . . great! Ok. Well, I’ll see you then! (fades to present) And that tragic conversation was actually the first thing Evie taught me . . . how to talk to girls. From that moment on she taught me everything I needed to know. I don’t think I would have graduated without her help. She taught me how to study . . . how to dress like a gentleman . . . how to love. And there was nobody and nothing I loved like Evangeline . . . And even though I never felt like I deserved it, Evangeline loved me too. Almost as much as she loved kids.

Evie’s dream was to be a teacher and after all she taught me, becoming a teacher just seemed like . . . like the right thing to do. I mean if I could make a difference for just one kid like Evie made a difference for me . . . then what else would I want to do with my life? I mean isn’t that what it’s all about? Making a difference? Ok, so I sound a little sappy, but I care, you know? I love what I do. I do. I love these kids like they were my own.

See, Evie and I never had our own kids . . . Evie had . . . Evie had ovarian cancer. Even when we got married it was already growing inside of her. Eating away at her. We had just started our life together. And here we were about to be pulled apart. But like I said, Evie was sharp as a tack and tough as nails. She fought like a champion and I was in her corner every second. I prayed all day every day. Please God. Please don’t take my Evie away from me. When she started chemo, I held her hand as hair fell out. When she had her oophorectomy . . . when they removed her ovaries . . . I held her head as she cried. Cried and Cried. Cried for week. Even years later, sometimes I would find her crying. I didn’t even need to ask. I knew why. Evie had always wanted children of her own . . . and to lose that change . . . to lose the opportunity to carry life inside of her . . . it nearly broke her to pieces. And if I had lost her to that . . . like that . . . it would have broken me beyond repair.

But with all her tacks and nails she pieced our life back together and beat it.

I thank God every day for giving me the chance to be with her. For blessing me with that time. For the next six years I didn’t waste a single second. I wanted to be with her at all times. That’s why we moved back to my home town and started teaching at the same school. We just couldn’t be apart. Any chance I got I would run around the corner and down the hall and peak in through her classroom window. Just to see her. After years of marriage I was still a schoolboy with a crush. There are no words for it. Just . . . I love you . . . That’s the only thing that comes close.

Like I said, I’m a numbers man. One number I can never forget. 4/24/1998. April 4th, 1998. I can’t ever forget that day. It was just like any other day . . . I woke up in the morning . . . Evie made breakfast while I packed our lunches, and we danced in the kitchen to the Bee Gees. Then I drove Evie and I to work. Her classroom was right by the door, so I snuck into her room and gave her a kiss before the kids started to pour in. I said, “I love you.” She looked up at me with those magic green eyes and said, “I love you too.” There were no other words. Just I love you. And I walked down the hall and around the corner to my classroom.

Three hours later the fire alarm goes off. Now this isn’t a drill. They tell us if there’s going to be a drill. Now I’m thinking it’s probably just some kid avoiding their history exam, so I’m not making too much of it except to follow protocol and get the kids outside as quickly and safely as possible. . So we pour out into the hall and around the corner and start making our way to the exit. All of a sudden I hear a sound like an explosion, it cracks the air and scares the hell out of the kids. And they all start to scream and run because now they know this isn’t a drill. Something real is happening. But bang, bang, bang . . . the sound keeps coming and I know that’s not an explosion. All of a sudden the doors up ahead are slammed shut and the Principal comes running back through the crowd screaming . . .

PRINCIPAL: Get back! Get back! Everyone into your classrooms NOW! There’s someone outside with a gun!

ROBERT: I don’t think. Instincts kick in and I know I have to protect my kids. “Alright, everyone get into the room. Go, go, go! Everyone! Come on!” And I get all of my kids into the nearest classroom, counting heads as they enter. When all the kids are out of the hallway, I lock the door and get everyone into the safest corner away from the windows and doors. We all get down on the ground. And I pray. I pray that this will go away. That this is just a nightmare and that I’m going to wake up any second and everything will be ok. Please God. Please take this away. Take this away. You took Evie’s cancer, God, now please take this too . . .

No . . . no . . . Evie . . . her classroom was right by the door. And I look at the other teachers huddles with their students and I say, “Watch my kids.” And I can hear them scream after me as I run out the door and down the hall into Evie’s classroom. But there’s nobody there. Evie?! Evie?! Where are you? Evie?! I don’t even stop to think about the gunman waiting outside. I bolt through the doors. Evie?! But there’s no gunman. The police have arrived. There’s panic everywhere. People are screaming everywhere and . . . (looks down) Evie?! (goes to her) Evie? No . . . no . . . no No NO! Please, no, God, no . . . Evie. Wake up. Please. Please. Please. Don’t take her now, God. Please give us just a little more time. Please don’t take my Evie . . .

Next thing I remember I’m in the hospital. They tell me I blacked out. I ask the nurse, “Where’s Evie? Where’s my wife?” She doesn’t answer. But she doesn’t need to. I already know she’s gone.

Slowly the details filter in. There were two gunmen. . . No, two boys. Two boys with guns. Just twelve and fourteen years old. I knew these boys. I taught these boys. They sat in my classroom. And I never . . . I mean, how could I know . . . I never would have dreamed that they were capable of something like this . . . but it was all planned out. Cold, calculated, mass murder. They pulled the fire alarm to lure everyone out of the school and then opened fire. Ten injured. Five dead. Four students . . . and one teacher. Mrs. Evangeline Foster stepped in the line of fire to save one of her students . . . Thirteen-year-old Angela Brooks.

I taught Angela too. She is the nicest, sweetest girl you’ll ever meet. Has long brown hair, and bright green eyes. Just like Evie. But you don’t hear about that on the news. You only hear about the misguided young boys, filled with hatred, who got their hands on a gun. Hearing their names . . . seeing their faces . . . day after day on every T.V. . . You start to hate those boys. But whenever my blood starts to boil, I just think of Evie. I think of how she loved every child for who they were. And I know that if she were in my shoes, she would find a way to forgive . . . Believe me, I try. I try to imagine how much they must have been hurting inside. But no matter how hard I try to understand . . . there are days when I wish those boys were dead and gone. It’s those days that Evie is teaching me still . . . teaching me to forgive . . . to love . . . and to live. That is my continuing education . . .

It was on one of those days that I got a letter from Angela Brooks . . . If you don’t mind, I’d like to read it for you . . . . “Dear Mr. Foster, I am so sorry that Mrs. Foster is gone. She was my favorite teacher. She saved my life and I would like to thank her, but I don’t know how. So I would like to thank you. I know I was not a good student in algebra class, but I promise I am going to do my best from now on. I want to be a teacher someday, just like her. I think maybe that is how I will thank her. Thank you for being a good husband to Mrs. Foster. She talked about you in class all the time. So if you are sad, just remember that she loved you very much. I know you and Mrs. Foster are not my family, but I want to say that . . . I love you too.”

See Evie? You made a difference . . . I miss you Evie. I love you. There are no other words.
```

---

## IC-0339: Cornrockets

- Title: Cornrockets
- Author (byline): Todd Hearon
- Work: The Kenyon Review
- Publisher: Kenyon College
- Publication date as stated: Summer 2004, Vol. XXVI (26), No. 3
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHRISTOPHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1569
- Already set (do not supply): none

### Source block (context only)

```text
Author: Todd Hearon
Book: The Kenyon Review
ISSN: 0163-075X
Publisher: Kenyon College
Date (Month/Year): Summer 2004, Vol. XXVI (26), No. 3
NOTE: Also Published in Boston Theater Marathon 4 available from Concord Theatricals
```

### Introduction (context only: never use it for content warnings)

```text
IN THE PERSONA OF A HOSPITAL ORDERLY: Christopher was a bright child. Everyone said so. But the death of his father profoundly changed his world. I’m so glad you could come today. Christopher doesn’t get many visitors; just the school tutor and his therapist. I know he’ll enjoy having a new person to talk to.

Cornrockets by Todd Hearon
```

### Performance text (classify this)

```text
The scene opens with CHRISTOPHER, a boy of 11, drawing with crayons. He keeps stopping to listen to something only he can hear off stage. Finally, he addresses the audience.

CHRISTOPHER: Hear that? (gesturing toward noises) That’s me they’re making. At it, Harold and Mom. Hopped up, like a couple of rabbits. (beat) Like on that battery commercial? The one that never stops? (proudly shows the picture he’s drawing) That’s them. That’s these two. They got hopped up a lot.

They don’t know, of course, it’s me that’s coming. Nobody knows, not yet. Least of all ha-ha old Shadowface, working graveyard shift at the prison. Shadowface, he’s my—(beat) He’s “the man Mom’s married to.” Right now. (gesturing toward noises) Get it? While the bunny show is going on. (sighs) Ah well. It’s as good a way as any to begin.

Anyways, it doesn’t matter. Shadowface fades fast. Gets stabbed in the back one night on cell patrol. Next Sunday, Harold shows up at the door. Mom calls me down and says, “Christopher, I’d like for you to meet your father.” (beat) I say, “But my dad’s dead.” She smiles, “Well, honey, that’s true, too, but this is Harold. Your other dad. Biological. . .” (beat) Biological was a big word for Mom. It meant real. They taught us that in school. As in your “biological father.”

“Go on, say hi, polite,” Mom says. “Hey,” I say. “Hey,” says Harold. (beat) It was . . . strange.

CHRISTOPHER: Miss Wong, the guidance counselor at school? — all the kids call her Miss Wrong — she says I have a prodigious memory. I had to look it up. Prodigious: “enormous or extraordinary in size.” She’s right, Miss Wong. I remember everything. (beat) That’s what’s wrong. I can’t forget.

• I remember the way the sunlight looked on a penny in a puddle one day when I was five. • Five times seven divided by three is eleven-point-six-repeating. • I remember the shapes in clouds. The colors. All of them. • I remember everything I’ve read. (quickly) “The Canyon de Chelly in Arizona is a breathless secret valley which has been inhabited by one Indian tribe after another almost without a break for two thousand years.” • I remember the morning I was born. The next word down from prodigious in the dictionary is Prodigy: “Noun. A person or thing of remarkable qualities or powers.” As in “child prodigy.” It also can mean monstrous. Most people don’t know that. “Something outside of the normal course of nature.” (beat)

Anyways. Miss Wong says my prodigious memory will come in handy one day, like when I’m an astronaut. That’s what I told her I was maybe going to be. An astronaut or a geologist. Her face got bright. “Ah geowogist! Just fink of all dose wocks!” Minerals, actually. (beat) Petrologists do rocks. That’s when I told her my dream of going to the Grand Canyon — (he glances offstage as if the sounds are getting louder, then turns back to audience)

You just have to ignore them. Eventually they go away. It’s worse at night. That’s not “normal.” That’s not within “the normal course of nature.” (Silence. He continues to draw) Us, we never went on family vacation. We went, like everybody else, like to the mall, like Sundays to Lake Michigan, but never technically “on vacation.” That’s why it was so ultimate the summer I turned ten and Mom said what would I think about a trip—a big trip, the three of us, to—ready? THE GRAND CANYON!

Oh. (beat) It was long. Real long and really hot. Middle of July. I rode in the back-back of the station wagon with my stuff. Read a lot. Drew a lot. Stuck to the seat a lot. Watched the wires on the side of the highway dip and rise, dip and rise. It was pretty monotonous. ‘Cause Harold drove three days and nights, nonstop. I think he must have been hopped up. I asked why we couldn’t stop and spend the night at a campground, like real vacation families. Harold said this was like being at a campground, just on wheels. (beat) It was strange. You wake up moving. (beat) I watched our shadow for a long time that first night, in the moonlight, on the side of the road. The three of us, out there, traveling so fast . . . I wondered what we must look like to it, to our shadow. ‘Cause it was just what we were, only not. Our opposite—looking back at us, up from its black, empty world, like us only . . . not . . .

We stopped in the morning for a pee break in this place called Jupiter, Nebraska. I was going to get a postcard for my class — “GREETINGS EARTHLINGS FROM JUPITER NEBRASKA! CORN CAPITAL OF THE UNIVERSE!” Get it? (beat) Anyways. That’s when I saw the CornRockets. (beat) CornRockets. They’re like — rockets (beat) shaped like corn. They’re cool. You take the plug out of the bottom and fill it up with water — that’s the fuel. Then you stick the pump in (he demonstrates with an imaginary rocket), it’s kinda hard, you’ve gotta create a seal. Then you pump it up and pull the latch and — whoosh! Liftoff in a spray of water just like smoke! But the coolest thing is when it hits its apogee — that’s the word for the highest point — an astronaut CornRocketMan pops out and floats off on a parachute. That’s the most righteous thing. Floating off like that. Lost. (beat) Harold got pretty pissed about the CornRocketMan getting lost every time we stopped. I said technically he wasn’t “lost” because we always finally found him. “Exactly,” Harold said and took the Man away and put him up on the floorboard, down with all the maps. (beat) That was in Colorado, in a place called Glory Falls. (beat) I don’t remember seeing any falls.

When we got to the Grand Canyon, it was early Sunday morning. I remember the sun was coming up. The parking lot was empty. Mom looked across at Harold as the car came to a stop and said, “Perfect.” That was my thought, too. Perfect.

My stomach was full of butterflies as we walked down the hill, towards it. We came to the rail and stepped up, looking out across. I was standing in between them. I could feel their skin. Our arms were touching. (he steps forward)

It was every color you remember from the crayon box. Burnt sienna, raw sienna, sepia, raw umber. Far down, a thread of thistle, turquoise blue. Comflower freckles, periwinkle patches on the walls, all Indian red—the whole gone goldenrod in rising sun. Maize. Amazing. Earth. But not Earth. The opposite of Earth, Earth’s . . . shadow? Space where Earth had been, before a giant’s hand scooped it out. Now, bright big bowl of morning air. And the colors—all down the walls, I named them but I couldn’t see how deep. I leaned across the rail and balanced on my buckle and, swear, for a second I was flying. Out and out—not a bird, not a plane, but (beat) SuperCornRocketChristopher! AstroGeologistMan! And down, down, down, parachuting through, I memorized the colors on the walls. Every patch, each stranded tuft of tree. Birds, this big — I was looking at the backs of flying birds! I turned to Mom and Harold — “Look! it’s—” (pause) Gone.

I got down off the rail and walked back up the hill. I was coming to the car when I heard it. That sound. They were at it, somewhere. The information booth? The bathrooms? The cactus patch? Wherever. (sighs) I walked up to the car to wait. That’s when I saw the windows were rolled down. There they were, in the back-back. Hopped up, going at it, all over my stuff. They didn’t see me; I saw them. (beat) It wasn’t normal.

I walked around to the driver’s side. I looked up at the sun. It had come a long way, from the opposite side of the world. China . . . I thought of Miss Wong. I thought of all the other kids in my class. I watched them for a while.

My ComRocketMan was down where Harold kept him, on the floorboard, down with all the maps. I reached in through the window. It was louder inside. (his movements are hurried, frenetic) I see him, down there. Past the brake. The handle says “EMERGENCY.” I’m trying to be quick, but the Man, the Man, he catches on the handle as I pull. (beat) It pops. The wagon starts to roll. (he crouches and begins to mime the action of priming a CornRocket. He is speaking quickly, forcefully, as if to block out the sounds]

Pull plug, fill rocket hull with fuel, replace plug, five times seven divided by three, take pump, in Arizona is a breathless, insert pump, a secret canyon, screw, inhabited, create a seal, almost without a break for, pump, two thousand years, eleven, pump, point six repeating, five, pump four, repeating, pump, for three, two, one, pull!—

(CHRISTOPHER looks up. No SOUND)

I was flying. This was our vacation. The three of us, a family, standing at the rail. One morning, for a morning, it was real. For just one second it was biological. We could have been a postcard. I could have stuck a stamp on us and sent us back to school: “GREETINGS EARTHLINGS FROM CHRIS T. ON VACATION! This is my family. Look at us and weep.” That’s the memory I wanted—the one, us three, that Sunday morning speechless at the rail. Perfect, like she said. Above the empty Earth. The opposite of shadow. Real. (he looks down in his empty hands. Silence)

I fired the CornRocket after them over the edge. And as it hit its apogee, I saw the astronaut eject and disappear. Parachuting down that maze of morning light. Lost.

(Silence)

I wish I’d never been.
```

---

## IC-0340: Courier

- Title: Courier
- Author (byline): Carol Mack
- Work: The Best American Short Plays 2005-2006
- Publisher: Applause Books
- Publication date as stated: Dec 2008
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: INTERROGATOR, PROFESSOR, YOUNG MAN, RECRUITER, DOCTOR, POLICEMAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1970
- Already set (do not supply): none

### Source block (context only)

```text
Author: Carol Mack
Book: The Best American Short Plays 2005-2006
ISBN: 978-1557837141
Publisher: Applause Books
Date (Month/Year): Dec 2008
```

### Introduction (context only: never use it for content warnings)

```text
Since 2001, as part of its War on Terror, the United States' Central Intelligence Agency has operated a network of off-shore detention facilities, commonly known as black sites, which are used as part of the system of extraordinary rendition used to hold and interrogate "high-value" foreign combatants captured during the US's wars in Iraq and Afghanistan. The ACLU has stated they consider extraordinary rendition to be an illegal form of forced disappearance and called for the detainees to receive trials and the camps to be closed; the US government argues that since the combatants are captured while participating in active military conflict against the United States and officially designated as "Illegal Combatants" under the Geneva Convention, the detentions are legal under international law. Courier by Carol Mack explores the concept of extraordinary rendition from a different angle. If our government can detain “foreign” combatants; what is to stop them from detaining U.S. citizens in the name of “National Security.” How far is too far in the quest to ensure the “safety” of our Government? Courier by Carol Mack
```

### Performance text (classify this)

```text
Set: The play takes place in an unidentified location where the PROFESSOR is being held and in the remembered moments in the PROFESSOR's consciousness. [Lights up. A man sits on a chair. An INTERROGATOR stands upstage of him.]

INTERROGATOR: . . . Go on.

PROFESSOR: So. I'm walking along through the park, my hands clasped behind my back. So ... I'm walking along when it begins to rain ... just then I see a man lying on a bench. I stop to see if he is all right, just sleeping it off, or . . .

INTERROGATOR: And then?

PROFESSOR: . . . then he opens his eyes. Wide. Looks terrified. . . And he grabs my arm. He says, PLEASE. That's all. Please. Stops me cold, that desperate sound in his voice. . . he pulls himself up on my arm. He feels so light. Weighs no more than a ghost. His face is unshaven. He sits and looks right through me. There's nobody anywhere. Empty paths, vacant benches . . . and I hear him say, "Let me tell you." Then he stops dead as if he hasn't talked to anyone in a long time and his own voice shocks him. I say, like you would to a child, 'It's O.K., what is it? What's wrong?' He says, "Let me tell you how I got here." Then he tells me the story I've already told you.

INTERROGATOR: You were supposed to meet him there. You arranged it? Think!

PROFESSOR: I never saw him before! How many times must I -

INTERROGATOR: You're the only people in the whole park, huh?

PROFESSOR: That's right. Fate. Call it what you will. Why am I here? . . . [As INTERROGATOR turns away.] What is this place?! [As INTERROGATOR exits.) Where is "here"?! [Angrily to offstage.] You'll have to let me out soon! They're looking for me! [To himself, bitterly, fighting to remain himself] I will not forget the story! I will make notes every day. I won't forget. I'll write it all down bit by bit and when they let me out I'll give them to my wife. Oh, Rachel! . . . [Very upset.] You'll send them to the newspapers. In case I . . . am silenced, in case I come home unable to speak or . . . You'll find them. You'll know what to do. He told me he was "chosen." Chosen! I looked at him like he was crazy. [Tbe PROFESSOR reappears as the RECRUITER in the remembered scene.]

YOUNG MAN: [Linking to remembered moment, on bench as lights shift, Urgently.] But it's true! Honest. That's how it started. I was chosen, see? out of hundreds of candidates. I was secretly tested. Before the interview. They never said where or how. I mean, all they said was: "You've been selected for the job." RECRUITER Now, son, we have conducted a thorough search and you have been chosen out of hundreds of potential candidates as most trustworthy. Most reliable. Now, son, this is one of the most important secret government jobs you could ever hope to do. This is about total trust in your country, O.K.? This takes a pledge that is way beyond allegiance. This is about faith. That's what we're dealing with here. See that package, son? That package and every package must be delivered under any circumstances. You never ever ask questions. And, son, if necessary you give your life for your country. And you walk ALONE. Outside this room? Anybody asks what you do for a living, you say you're a part-time whatever but you do NOT say "courier." It could get you killed, son. Got it? [At nod, he pushes a note across desk.] These are your instructions. When. Where. How. Memorize it .... Good. There's your first mission. Good luck.

YOUNG MAN: Thank you, sir.

RECRUITER: For what?

YOUNG MAN: Choosing me.

RECRUITER: For what?

YOUNG MAN: The job?

RECRUITER: What job?

YOUNG MAN: . . . I ... can't say.

RECRUITER: Why not?

YOUNG MAN: 'Cause I don't know?

RECRUITER: Don't know what?

YOUNG MAN: . . . Don't know anything, sir.

RECRUITER: About what? Anything about what?!

YOUNG MAN: Nothing.

RECRUITER: [As he exits.] Good!

YOUNG MAN: The packages. They were all sealed. And every day there was a new one. I was taking them to a lab. All these boxes, sealed red boxes. Shiny. Nothing could leak out but ... all going from Central to this lab, see? After a coupla months I wonder who's it going to? And what's in the boxes? All I did was take off the label. Just the label. No name. Some kind of bar code label. I just start to take it off with my penknife- [Very odd mechanical noise. YOUNG MAN startled, stands.] And before I know it these guys show up, see? Then I get arrested for possession of lethal materials. They accuse me of planning a terrorist attack. They say the box contains a biological weapon. I say that's not possible. They say, "Who do you work for?" I tell them I take the package from Central to the lab. I tell them that's my job. They tell me there IS no lab. They tell me there IS no central nothing. That they don't exist and they never have. Then I figure O.K., O.K., this has gotta be some kinda test. Right? Maybe they test you every month. So then they say, "Who do you work for?" and I say, "I ... I used to work for the U.S. post office and I don't work for nobody now," and they say, "Then who told you to do it?" [Breaking down, in tears.] And I say, "Do what?" Do WHAT? For chrissakes! I trusted them. I BELIEVED in them. I was selected for this job and now they turn against me for WHAT

DOCTOR: [Appears standing with case file, listening, then assured, clinical.] I see ... Do you know where you are? ... [At the nod "no. '] . . . You're in a hospital.

YOUNG MAN: . . . Why?

DOCTOR: So you can get better.

DOCTOR: I have your file here. And your diagnoses. But we are going to cure you. You'll be all right.

YOUNG MAN: Then do I get out of here? I mean, if I get better?

DOCTOR: Yes. Of course. Absolutely.

YOUNG MAN: How'd they find me? I mean, after I ran away? Does it say in the file?

DOCTOR: Who are "they," these people who "found you"?

YOUNG MAN: I don't know, but they musta thought I was dangerous 'cause they tried to kill me. I got away and I was hiding out in this other city and they . . . I could see how they thought maybe I'd talk about the lab? Where I took the stuff? I could-

DOCTOR: Listen, try to hear me out. There is no lab. There is no what you call "Central Office." There is no "package." We know how real these things are to you but they are not real, and when you can understand this, you'll feel much better.

YOUNG MAN: I trusted them. I had faith. I trusted my life to them. Why?! [Light shift.] ******

PROFESSOR: [Alone on chair, remembering, as he was earlier, making a note.] And by the time he finishes, his face is wet with tears and rain and he starts coughing, then choking and I put my arm around him . . . He twists round and his jacket opens . . . There's a wound. Dark, blackened blood. He twists violently once more, then collapses. I take his hand, his wrist. There's no pulse . . . People must die like this every day. Alone. Shot by criminals. He seemed, so . . . innocent. I don't know what to think. His story seems incredible. A fantasy. And yet, they were his last words his last story. . . Oh my God. If I hadn't stopped. If I hadn't heard . . . [Thinking.] I didn't believe his claim that they could track him. After he escaped the hospital . . . To be that . . . able to find him in another city and then to be so near when he tells a stranger his story. Of course I don't know who "they" are . . . But suddenly there's a man in uniform ... a policeman. ****

POLICEMAN: [Enters, looking at offstage body and then back at PROFESSOR.] You found him like that?

PROFESSOR: No, I ... he just started choking, then all this blood

POLICEMAN: Hands up. Keep them up. [Frisking PROFESSOR, takes his wallet out, looks at J.D.] You were just walking by here, huh? You do it a lot? Walk in the rain?

PROFESSOR: It wasn't raining when I started out.

POLICEMAN: So you stop by here and he's lying there bleeding?

PROFESSOR: No! Yes, I mean. I, I didn't, I didn't see the wound until

POLICEMAN: And what's your name?

PROFESSOR: Dr. Ahrensky, I teach at Columbia-

POLICEMAN: Ahrensky [Inspecting wallet.] What's the origin of this name?

PROFESSOR: How far back? Russia? Aramaic? What are you?

POLICEMAN: Look, you got blood on your hands. That guy's dead. “Professor," you're gonna have to answer questions. That guy? You say you never seen him before? He talk to you? Did he approach you?

PROFESSOR: No, I . . . I walk by, see he's bleeding, I see blood, I see he's been shot.

POLICEMAN: That right? But you said, uh, "I didn't see the wound at first."

PROFESSOR: Did I? I'm . . . I'm quite upset. I need to wash my hands. All this blood. I must call my wife, I-

POLICEMAN: Look, we've got a homicide here-

PROFESSOR: Are you accusing me of something? If so, I believe you have to read me my rights.

POLICEMAN: You're wrong on that one, "professor," O.K.? Now, how about I do my job, you stick to yours. What exactly is your field, professor?

PROFESSOR: Ethics.

POLICEMAN: "Ethics." Look, I gotta know exactly what happened here. How you got involved. We got a dead body. There's blood on your hands. First you say you didn't see the wound. Then you say you did. You say you don't know this person but you're here, right? ***

PROFESSOR: [At his chair as at top of play.] I should've run then. . . But it's Central Park! On Poet's Walk. That's where I was! That's . . . I was in shock. And I assumed he was just a cop . . . I assumed the world was a different world . . . I know. I know I'm naive, but then, weren't we all? [Pause. Then passionately.] I find it impossible to believe that it has all come to this "life being nasty, brutish and short" and all people against each other like driven mad animals. [Pause.] That policeman. I thought he was "only doing his job." He believed that I could kill another human being . . . in the park. In the rain. In some world that . .

. Had I known we'd come to this. HERE?! ***

POLICEMAN: So he tells you that whole story?

PROFESSOR: Yes . . . Yes he did.

POLICEMAN: Incredible.

PROFESSOR: Yes. But, officer, somebody shot him-

POLICEMAN: Drugs. Probably drugs. Gangs. But that story . . . Sounds to me like he made up the whole nine yards.

PROFESSOR: . . . I don't know. Poor kid, he seemed so, lost, so . . . Yes, I think I do. [POLICEMAN exits.] Yes. I do .... And the world changed . . . The towers fell, and the ivory tower tumbled invisibly and in the rubble, from there to here we fell into another world where I am taken unaware. Yes, I DO! I don't know why I said it. But . . . why would anybody care even if I told the story? I am just an old professor . . . And what do I know?! That the boy worked for some , , , what? Secret government organization somewhere? Some lab, but where? I don't even know where! Is it still in operation? What does it do that's worth killing for? Worth removing anybody who knows it exists. It is impossible to believe that . . . OH God, If you make too much noise. "Yes, I do." Then they put me in a car and bring me here. Poor kid. The "courier" . . . It must be much more complicated to vanish someone with a family . . . Unless you were to take the whole family. Oh, Rachel, please don't do anything foolish! . . . I vanished . . . Where to? Why? I was not unhappy. I was not "political,". . . Please be careful. Watch what you say. The more you say, the more publicity, the less likely it is I can get out . . . from here. [Pause.] But where is here? Where are we?
```

---

## IC-0341: Coyote on a Fence

- Title: Coyote on a Fence
- Author (byline): Bruce Graham
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Aug 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BOBBY, JOHN, SAM, SHAWNA
- Teaser before the introduction: Yes
- Spoken words (computed): 1211
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bruce Graham
ISBN: 978-0822217381
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Aug 2000
```

### Introduction (context only: never use it for content warnings)

```text
Welcome to Death Row. * This year, as of November 1, 2024, 21 prisoners have been executed in 8 US states, with over 2,200 still awaiting execution. (update as needed) And while the number of death sentences per year have dropped dramatically since 1996, 27 States, the US Federal Government and the US Military still retain it as a sentencing option for heinous crimes. ** President-elect Trump, during his 2024 campaign for re-election, signaled his stance on capital punishment -- indicating he would make more people eligible including child rapists, migrants who kill US citizens and those convicted of drug and human trafficking. How do you feel? Is the death penalty warranted for these types of crimes; or are you against this form of punishment? The State vs Robert Alvin Reyburn provides the backdrop for this drama . . .

Coyote on a Fence by Bruce Graham
```

### Performance text (classify this)

```text
Bobby – White Inmate on death row; late 20s, skinny, pale, damage to one of his eyes John – White inmate on death row; mid 40s; writes obituaries for “The Death Row Advocate” Sam – Reporter from the NY Times – 30’s Shawna – Prison guard, race doesn’t matter.

BOBBY: (Pg 44) (singing as he bounces a ball, he appears almost childlike and when he doesn’t know the words he uses “da, da”) “God rest ye Merry gentlemen, let nothing you da, da. Remember Christ our savior was born on Christmas day.

JOHN: (Pg 49) In seventy-two hours they are going to kill you.

BOBBY: And I will go to a better place. (Pg 51) That’s in the Bible, John. (returns to his ball bouncing, which he enjoys very much) (Pg 46) Dashing through the snow, in a one horse open sleigh, o’r the fields we go, laughing all the way ha-ha-ha (Bobby breaks into giggles)

JOHN: (Pg 49) If I could get that on tape and show it to a jury, they’d never kill you. You’re runnin’ around like a happy puppy or something.

BOBBY: (blank look; John has lost him, but he understood the word “puppy” and he begins to imitate one, taking the ball in his mouth and making puppy noises) I’m a happy puppy!

BOBBY: (Pg 27) (to the audience) God spoke ta me a lot. . . but that mornin' . . . I'm passin’ a church - had an old pick-up Uncle Hew gimme - and I could hear 'em in there . . . singin’ . . .

Beautiful singin’.

SAM: (Pg 32) [His] mother was a transient. Did some prison time herself: prostitution, public drunkenness, assault.

BOBBY: (Pg 27) I pull over and just listen. And then God said, "Help them, Bobby. You gotta’ help those people . . . show them the way home!"

SAM: (Pg 32) Drunk all through her pregnancy. Got beat up pretty bad when she was seven months along. Between the booze and the beating, they’re pretty sure the fetus suffered a little . . . damage.

BOBBY: (Pg 28) So I went in..."Excuse me Reverend? I need to speak the word of God!"

SAM: (Pg 33) He never made it out of the seventh grade.

BOBBY: (Pg 28) Got real quiet...everybody starin’ at me. But I didn't feel no hate. (to the congregation) "God has spoken to me! He wants you all to know it is immoral for whites and n**** ta live together.”

BOBBY: (Pg 28) (shocked) They turned on me. Started clawin’ at me like animals--you believe that? I was tryin ta help them! (A deep breath).

SAM: (Pg 35) Mother had him put in the juvenile detention center for running away. He was twelve – other kids were older. Whole dorm – first night. Got a little rough, shattered his hip.

BOBBY: (Pg 28) I got in my truck, drove down the road... (Bobby laughs in God’s voice, then speaks in awe) It was God! (in God’s voice) “They mock you, Bobby, they mock me! They must be cleansed!” I turned around and headed back. They're singin’ again--real loud--so I pulled the truck right up to their door there. Parked it, got out my gas can, made a big ring. Let the circle be unbroken. (beaming) Sat under a tree and watched . . .

SAM: (Pg 33) Fire killed thirty-seven people. Fourteen of them kids. Sunday school in the basement. He didn’t just confess, he made a proclamation. Took full responsibility.

JOHN: (Pg 33-34) The trial . . . There was no medical testimony. There was no psychological testimony. He’s not competent enough to take responsibility. Bobby totally disassociates. He shouldn’t be on the row!

BOBBY: (Pg 20) Hey, I ever do my penguin for ya? Watch this (he begins to waddle around like a penguin) (Pg 23) (begins to frantically look for something – he’s suddenly in a panic) Where’s my towel? I need my towel!

JOHN: Here! Take mine if it’ll shut you up! (he shoves his towel into Bobby’s cell)

BOBBY: (Bobby grabs it desperately and holds it tightly to his chest) They done this before. They want my other eye. They got this one when I was sleepin’ but they ain’t gettin’ the other one. (whispering intently) That’s when they get ya – when you’re sleepin’. They get bleach outta’ the laundry and throw it in your face. Burns . . . Lord it burns. So I always gotta’ sleep with a towel over me.

SHAWNA: (Pg 36) They’re all bullshitters. (mocking) I’m poor, I’m black, daddy beat me, momma didn’t love me.

BOBBY: (Pg 30) Seal! (tries to balance a ball on his nose, slaps his hands and makes seal sounds)

SAM: (Pg 35) (quiet but intense) I am against the death penalty (pause) I think people like Bobby are evil. I know that’s probably . . . simplifying things a little too much. But (shrugs) I keep picturing thirty-seven people frightened out of their minds, knowing they’re going to die. Sorry – I just can’t work up a lot of sympathy over someone like him.

BOBBY: (Pg 30) Hey, I ever show ya my toad? (crouches down, makes toad sounds and mimes catching a fly, then jumps up laughing)

SHAWNA: (Pg 36) (Shakes her head) Never take responsibility. Bad family, bad neighborhood. “I’m a victim of society” I am so sick’a that. How ‘bout your victim, huh? (long pause) *****

JOHN: (Pg 10-11) Silence for a change. (deep breath, heavy sigh, beat) They murdered Willie T. last night. That’s why it was quiet. They never announce in on the row, but we all know when it happens. We know even before the crowd outside begins to cheer. And the silence rolls in, one cell at a time. (rubs his face, tired) *****

BOBBY: (Pg 52) (to audience) They have coyotes where you grew up? . . . Nasty animals. Wipe out a whole chicken house in one night. Hate coyotes more than anything. (howls like a coyotes, then is quiet for a moment, thinking back) I know, I seen it. Just got outta’ the hospital ‘cause’a my hip

SAM: (Pg 42) (to John) Now let’s talk about the obituaries. The angle of my article is that you try to . . . undemonized these men.

BOBBY: (Pg 52) So one day, my mother--I tell her I wanna go to Uncle Hew's but she--heck--she couldn't got me there if she wanted to and this man's she with, he...so I walked—(Laughs) Well, limped. Six miles outta town. man-oh-man it hurt.

JOHN: (Pg 42) Undemonize?

BOBBY: (Pg 52) Just wanted to get to my uncle's. I can see the lights and. . . man-oh-man I almost peed myself--cause there's this. . . monster!

SAM: (Pg 42-43) Find the positive . . . whatever. But Willie T. was an animal! Mutilating a twelve-year old boy is not the act of a human being.

BOBBY: (Pg 52) And it's floatin in the air, and I can see its eyes and--- I burst in on poor Hew shaki’n and cryin’ --didn't even know I was comin,’ but he hugged me and put me in the truck and drove on out there. Coyote—that’s all it was – He’d shot it and stuck it up on the barbed wire. Beat on it too, while it was wounded.

SAM: (Pg 43) Sneer all you want, John. You people frighten us. We are not the bad guys just because we want to protect ourselves.

BOBBY: (Pg 52) He told me ‘bout coyotes bein’ evil and how it’s okay ta kill ‘em. That’s why he stuck it up onna’ fence. Let the world know -- death to predators. (simply) Then he told me all about the Jews. How Hitler knew they were predators. How they was usin’ the n***** and mud people to turn us all into animals so they can enslave us. (a beat, then to John) (Pg 49) Watcha’ gonna say ‘bout me? Inna’ paper. I mean, ya are gonna’ write somethin’ ‘bout me, right. Put my name in there.

JOHN: Wish I didn’t have to – What would you like.

BOBBY: Well . . . that I was a good Aryan soldier and upheld the code. (Pg 17) (springing to attention) I am Aryan!! If I am incarcerated I will remember at all times my duty as an Aryan!

JOHN: (Pg 49) I’m not putting that crap in my paper – (Pg 19) 70% of our readership is African- American.

BOBBY: (Pg 49-50) Then don’t write nothin’ ‘bout me.

JOHN: I don’t have a choice here. (pause) Remorse, Bobby. Give me that at least, please. That’s the one thing I can always fall back on – showing some remorse. Tell me you’re sorry you killed 37 people.

BOBBY: (Pg 51) There’s nothin’ wrong with killin’ a predator. Ol’ Hew said it. Predators must be destroyed. *****

SAM: (Pg 54) The state murdered Robert Alvin Reyburn last night. He was twenty-eight years old. Bobby was accused of a heinous crime.

JOHN: [He] never denied it. In his own unique way he was an honest man.

SAM: He did animal impressions. Forgot the words to songs. (pause) St. Francis once said, "Where there is charity and wisdom . . .

JOHN: . . . there is neither fear nor ignorance." Bobby Reyburn knew no charity or wisdom in his life. (sighs sadly) And the only person who ever loved him taught him how to hate.
```

---

## IC-0342: ‘Cuz He’s Black

- Title: ‘Cuz He’s Black
- Author (byline): Javon Johnson
- Work: Viral
- Publisher: Button Poetry
- Publication date as stated: Dec 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 560
- Already set (do not supply): none

### Source block (context only)

```text
Author: Javon Johnson
Book: Viral
ISBN: 978-0989641517
Publisher: Button Poetry
Date (Month/Year): Dec 2013
```

### Introduction (context only: never use it for content warnings)

```text
Ntozake Shange once wrote that “cuz he’s black and poor he’s disappeared – the name was lost”

This is what I want to say: Dear White America: Take a deep breath. Don’t tell me about how many black friends you have. Don’t tell me that you voted for Obama. Don’t tell me that you don’t see color. Don’t tell me that I’m blaming whites for everything. To do so is to hide yet again.

You are part of a system that allows you to NOT engage in “the talk” that black people must have with their children. The “talk” about what to do when they are confronted by white police officers.” ‘Cuz He’s Black by Javon Johnson
```

### Performance text (classify this)

```text
So I'm driving down the street with
my 4-year-old nephew.
He, knocking back a juice
box, me, a Snapple, today y'all
we are doing manly shit. I love
watching the way his mind works.
He asks a million questions.
Uncle, why is the sky blue?
Uncle, how do cars go?
Uncle, why don't dogs talk?
Uncle, uncle, uncle, he asks,
uncle, uncle, uncle, he asks
uncle uncle uncle
as if his voice box is
a warped record. I try my best
to answer every question, I do.
I say it's because the way
the sun lights up the outer space.
It's because engines
make the wheels go.
It's because their minds aren't
quite like ours. I say Yes.
No. No. Yes. No. Yes. No. I don't know.
Who knows? Maybe. We laugh.
He smiles at me, looks out the window,
spots a cop car, drops his seat
and says,
"Oh man, Uncle, 5-0, we gotta hide."
I'll be honest. I'm not happy
with the way we raise our Black boys.
Don't like the fact that
he learned to hide
from the cops before
he knew how to read.
Angrier that his survival
depends more on
his ability to deal
with the "authorities"
than it does his own literacy.
"Get up," I yell at him. "In this car, in this family,
we are not afraid
of the law."
I wonder if he can hear
the uncertainty in my voice.
Is today the day he learns
that uncle is willing to lie to him,
that I am more human
than hero?
We both know the truth
is far more complex than
do not hide. We both know too many
Black boys who disappeared.
Names lost.
Know too many Trayvon Martins
Oscar Grants
and Abner Louimas, know too many
Sean Bells, and Amadou Diallos
Know too well that we are
the hard-boiled sons of Emmett Till.
Still, we both know
it's not about whether or not
the shooter is racist,
it's about how poor Black boys
are treated as problems
well before we are treated as people.
Black boys in this country
cannot afford
to play cops and robbers
if we're always considered the latter,
don't have the luxury
of playing war
when we're already in one.
Where I'm from,
seeing cop cars drive
down the street feels a lot
like low-flying planes in New York
City. Where I'm from, routine traffic
stops are more like mine
fields, any wrong move
could very well mean your life.
And how do I look my nephew in his apple face
and tell him to be strong when we both know
black boys are murdered every day, simply
for standing up for themselves? I take him
by the hand, I say
be strong. I say be smart. Be kind, and polite.
Know your laws. Be aware of
how quickly your hands move
to pocket for wallet or ID,
be more aware of how quickly
the officer's hand moves to holster, for gun.
Be Black. Be a boy and have fun,
because this world will force you to
become a man much quicker
than you need to.
"Uncle," he asks, "what happens
if the cop is really mean?"
And, it scares me to
know that he, like
so many Black boys,
is getting ready for a war
I can't prepare him for.
```

---

## IC-0343: Daddy’s Little Girl

- Title: Daddy’s Little Girl
- Author (byline): Jason Sheets
- Work: Turning Points, Pgs 153-157
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Dramatic Interpretation
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
And we did. We tried to see the blue skies every single day from that moment on.
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

DADDY: Suddenly, I see her shoes hit the first step. Slowly, step by step, she comes into focus. The dress looks great and (shocked pause) And she's not wearing her wig. Beaming like a choirgirl, my bald little girl comes down the stairs. She walks to me and says . . .

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

(sings) **You're the end of the rainbow; You're my shining star, You're sugar and spice; You're everything nice and you're Daddy's little girl.
```

---

## IC-0344: Daisy Chains

- Title: Daisy Chains
- Author (byline): Michael Dean
- Work: Daisy Chains
- Publisher: SpeechGeek
- Publication date as stated: 2018
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1352
- Already set (do not supply): none

### Source block (context only)

```text
Daisy Chains by Michael Dean
ISBN: 978-1-61387-201-7
Copyright 2018 by SpeechGeek.
Free performance of this play for high school and college level competitive forensics is
permitted. All other rights reserved.
This PDF version of this selection, e-published in 2018, is identical to the printed published
version of this same publication dated 2018. This statement along with the entire printed
PDF of this publication must be presented at any National Speech and Debate Association
District or National event for the script to comply with NSDA rules per the request of the
Executive Director.
This and other selections of quality performance literature for competitive oral
interpretation are published by SpeechGeek.
For more information and performance rights, contact SpeechGeek.
SpeechGeek
248 Arlington Park Dr.
Hot Springs, AR 71901
Phone: 1-888-742-2028
Email: thegeek@speechgeek.com
Web: www.speechgeek.com
Facebook: www.facebook.com/speechgeek
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
PAUL. Have you ever had the feeling that you’re walking forward but moving backward? Like your metaphysical self is trying really hard to escape, but your stupidity has your body moving headlong toward a disaster?

Yeah…me neither.

The sticker on the welcome table reads “Hello, my name is ______.” And I think, “Should I use an alias? If this thing goes sideways, do I need plausible deniability?” But I opt for the truth and write… Paul. There, that wasn’t so hard.

Then I look up and find what seems like something out of American Horror Story or some demented haunted house: helpless and confused men sit in rows on backless stools in a gymnasium, staring blankly at the sharp instruments of torture on the table in front of them, looking into the dead eyes of dozens of severed mannequin heads.

Once again, I think, “Nope. Nope. Nope.”

Just as my self-preservation instinct begins to suck me away toward the door, a bright and chipper voice echoes off the wood floors like basketball, “Hey, fellas. Welcome to Daddy Does Hair.”

And I know that there’s no getting out of this one.

During the 2016 Super Bowl, a commercial aired portraying NFL stars attempting, and mostly failing, to do their daughter's hair. That commercial was part of a global movement which challenged the gendered roles of fatherhood, and showed parenting as a skill that is learned. For single father, Paul, raising a daughter is all trial and error, yet his struggles remind us that the willingness to learn is at the root of all love. Daisy Chains by Michael Dean

PAUL. I find my seat between two guys who look even more uncomfortable than I do. We shake hands too hard—each asserting that we are men and that our masculinity is not threatened. It’s the same way we puffed up when our daughters were first born. Everyone knew that one look—one tiny hand wrapped around a finger—and we were meltier on the inside than a bag of M&M’s in a clothes dryer. But it doesn’t matter. You still gotta play the part, walk tall, and drop your voice. Because, for a little while anyway, I was the manliest man she knew, then her mom left. And I had to become so much more.

My mannequin…whom I have named Wanda…has red hair, like my daughter’s. It’s a deep Irish red. When she was a baby, it was like the color of a sunrise, and now it’s taking on this copper warmth like my ex-wife’s. Megan, that’s her name. My daughter, not my ex-wife.

Megan was very clear on my assignment here: I am required to learn a looped French braid—or else.

It’s for her dance recital next week. It’s a big one. She’s got a solo and everything. Shown it to me so many times, I bet I’ve even got it memorized.

So her hair has to be perfect, obviously.

The instructor starts the class by congratulating us on our bravery. She chuckles. We do not. there’s no man here because it’s chuckle time. In fact, I’d wager that if each of us hadn’t been threatened in some way, shape, or form, we’d give all these mannequin’s buzz cuts and head down to the bar to watch Monday Night Football.

Miss Chipper tells the class, “We’ll start simple,” “brush out the hair in long smooth strokes.”

Well yeah, it’s a hell of a lot easier when it’s a mannequin, not a squirming rat’s nest, squealing that it’s taking too long.

Ok, next up is the flat iron. Miss Chipper says, “do it in layers and sections.”

I look nervously at the guy next to me. He seems to know this part so I copy his moves, feeling once again entirely inadequate as the mannequin stares at me.

I clamp down on my finger and scream, “Holy hot hell! You want me to solder my kid’s hair or what?”

I asked if one of the dance moms could handle the French braid, but Megan told me that it was time for us to figure it out for ourselves, which I agreed with thinking it meant that she would YouTube something or whatever and learn for herself. Then I found this flyer taped to my steering wheel.

Ten-year-old’s are not known for their subtlety, I guess.

I like that about her. It’s the part that reminds me of me. In these last two years on our own, I’ve developed a self-preservation instinct, but before that—whoa, I wouldn’t just mess up. I made full-throated, whole-hearted, two-footed fails—usually because I tried too hard and said too much. This one time, Megan had this little second graders’ singing show thing at school and the directions that were sent home stated clearly that each child should dress as a flower for the performance.

And I thought to myself, “Well… Ok, then!”

I got tag board, wire, and elastic, and I made her this neon flower headdress. I made it big so she’d be the brightest flower in the garden. And then we got to the show… Well, I didn’t know they were having the kids stand in rows and I didn’t know she was standing in front. She eclipsed like half the class. But by god, you could’ve spotted that child from the moon!

Megan’s mom said she couldn’t believe I screwed it up. She was always saying she just “couldn’t believe me.” But somehow I knew she was talking more about believing in me. That’s the part I failed at.

Wholeheartedly.

When someone stops believing in you, you lose them. In every possible way. You lose. And no matter how hard you try to make it right, eventually you’re just punishing yourself. And I didn’t blame her for not loving me anymore. I mean, some of that has to be beyond your control. But leaving me to explain it to an eight-year-old? No one deserves a punishment like that. Just because someone stops loving you doesn’t mean you’re right there saying, “Well, great. I was wondering if one of us was ever gonna fess up to this.” Because I never would have. I never would have quit—I didn’t.

The room looks at me briefly until the teacher chuckles again and I want to throw the mannequin head at her.

This isn’t some joke.

Every day I see my daughter look more and more and more like her mother: the same hair, the same eyes, the same voice. And every day I feel us getting one step closer to that same disappointment. And the harder I try, the harder I fail. And while I used to be fine with that, there are different stakes now. And last night when she was telling me yet again about this stupid class, and I was trying to weasel out of it, she told me—yelled at me— you’d understand if you didn’t have a mom!

And just like that, it’s that same backwards feeling.

I try to be tough, but I’m not. Every day she’s becoming this person who can see the world around her and everyone in it. Sooner or later, she’ll realize what I’ve been dreading forever…

That I am probably not enough for her.

Miss Chipper stops by my workstation and sees the mess I’ve made of everything. I know she can see the tears forming in my eyes, and I just pray she doesn’t chuckle at me.

“Paul?” She asks reading my nametag. She’s asking if I’m okay. I don’t know if I am.

“Yeah,” I tell her. “I’m okay—just failing a little bit here.”

“That’s good. It means you’re trying. Now brush it out and start again,” she says.

And I think to myself, “That’s the best thing you can say to a dad like me,” because it’s not a choice or a thing you can quit; failure’s not an option. All you can do is hope you’ll get a little better each time you try.
```

---

## IC-0345: Dance, Dance, Dance (from The Absolutely True Diary of a Part-Time Indian)

- Title: Dance, Dance, Dance (from The Absolutely True Diary of a Part-Time Indian)
- Author (byline): Sherman Alexie
- Work: The Absolutely True Diary of a Part-Time Indian
- Publisher: Little, Brown and Co
- Publication date as stated: Sept 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ARNIE, PENELOPE, ROGER
- Teaser before the introduction: Yes
- Spoken words (computed): 1941
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

ARNIE: Traveling between Reardan and Wellpinit, between the little white town and the reservation, I always felt like a stranger. I was half Indian in one place and half white in the other. It was like being Indian was my job, but it was only a part-time job. And it didn't pay well at all.

The only person who made me feel great all the time was Penelope. Well, I shouldn't say that. I mean, my mother and father were working hard for me, too. They were constantly scraping together enough money to pay for gas, to get me lunch money, to buy me a new pair of jeans and a few new shirts. My parents gave me just enough money so that I could pretend to have more money than I did.

I lied about how poor I was. Everybody in Reardan assumed we Spokanes made lots of money because we had a casino. But that casino, mismanaged and too far away from major highways, was a money-losing business. In order to make money from the casino, you had to work at the casino.

And white people everywhere have always believed that the government just gives money to Indians.

And since the kids and parents at Reardan thought I had a lot of money, I did nothing to change their minds. I figured it wouldn't do me any good if they knew I was dirt poor. What would they think of me if they knew I sometimes had to hitchhike to school?

Yeah, so I pretended to have a little money. I pretended to be middle class. I pretended I belonged. Nobody knew the truth.

Of course, you can't lie forever. Lies have short shelf lives. Lies go bad. Lies rot and stink up the joint.

In December, I took Penelope to the Winter Formal. The thing is, I only had five dollars, not nearly enough to pay for anything—not for photos, not for food, not for gas, not for a hot dog and soda pop. If it had been any other dance, a regular dance, I would have stayed home with an imaginary illness. But I couldn't skip Winter Formal. And if I didn't take Penelope then she would have certainly gone with somebody else.

Because I didn't have money for gas, and because I couldn't have driven the car if I wanted to, and because I didn't want to double date, I told Penelope I'd meet her at the gym for the dance. She wasn't too happy about that.

But the worst thing is that I was worried that people would make fun of me, right? And they probably would have if Penelope hadn't immediately squealed with delight when she first saw me walk into the gym.

PENELOPE: Oh, my, God! That suit is so beautiful. It's so retroactive. It's so retroactive that it's radioactive!

ARNIE: And every dude in the joint immediately wished he'd worn his father's lame polyester suit. And I imagined that every girl was immediately breathless at the sight of my bell-bottom slacks. So, drunk with my sudden power, I pulled off some lame disco dance moves that sent the place into hysterics. Even Roger, the huge dude I'd punched in the face, was suddenly my buddy.

Penelope and I were so happy to be alive, and so happy to be alive TOGETHER, even if we were only a semi-hot item, and we danced every single dance.

Nineteen dances; nineteen songs. Twelve fast songs; seven slow ones. Eleven country hits; five rock songs; three hip-hop tunes. It was the best night of my life. Of course, I was a sweaty mess inside that hot polyester suit. But it didn't matter. Penelope thought I was beautiful and so I felt beautiful.

And then the dance was over. The lights flicked on. And Penelope suddenly realized we'd forgotten to get our picture taken by the professional dude.

PENELOPE: Oh, my God! We forgot to get our picture taken! That sucks!

ARNIE: She was sad for a moment, but then she realized that she'd had so much fun that a photograph of the evening was completely beside the point. A photograph would be just a lame souvenir.

I was completely relieved that we'd forgotten. I wouldn't have been able to pay for the photographs. I knew that. And I'd rehearsed a speech about losing my wallet. I'd made it through the evening without revealing my poverty.

I figured I'd walk Penelope out to the parking lot, where her dad was waiting in his car. I'd give her a sweet little kiss on the cheek (because her dad would have shot me if I'd given her the tongue while he watched). And then I'd wave good-bye as they drove away. And then I'd wait in the parking lot until everybody was gone. And then I'd start the walk home in the dark. It was a Saturday, so I knew some reservation family would be returning home from Spokane. And I knew they'd see me and pick me up.

That was the plan. But things changed. As things always change.

Roger and a few of the other dudes, the popular guys, decided they were going to drive into Spokane and have pancakes at some twenty-four-hour diner. It was suddenly the coolest idea in the world. It was all seniors and juniors, upperclassmen, who were going together. But Penelope was so popular, especially for a freshman, and I was popular by association, even as a freshman, too, that Roger invited us to come along.

Penelope was ecstatic about the idea. I was sick to my stomach. I had five bucks in my pocket. What could I buy with that? Maybe one plate of pancakes. Maybe. I was doomed.

ROGER: What do you say, Arnie? You want to come carbo-load with us?

PENELOPE: Oh, I want to go, I want to go. Let me go ask Daddy.

ARNIE: Oh, man, I saw my only escape. I could only hope that Earl wouldn't let her go. Only Earl could save me now. I was counting on Earl! That's how bad my life was at that particular moment! Penelope skipped over toward her father's car.

ROGER: Hey, Penultimate, I'll go with you. I'll tell Earl you guys are riding with me. And I'll drive you guys home.

ARNIE: Roger's nickname for Penelope was Penultimate. It was maybe the biggest word he knew. I hated that he had a nickname for her. And as they walked together toward Earl, I realized that Roger and Penelope looked good together. They looked natural. They looked like they should be a couple. And after they all found out I was a poor-ass Indian, I knew they would be a couple.

Come on, Earl! Come on, Earl! Break your daughter's heart! But Earl loved Roger. Every dad loved Roger. He was the best football player they'd ever seen. Of course, they loved him. It would have been un-American not to love the best football player. I was angry and jealous and absolutely terrified.

PENELOPE: I can go! I can go! (running back and hugging Arnie)

ARNIE: An hour later, about twenty of us were sitting in a Denny's in Spokane. Everybody ordered pancakes. I ordered pancakes for Penelope and me. I ordered orange juice and coffee and a side order of toast and hot chocolate and French fries, too, even though I knew I wouldn't be able to pay for any of it. I figured it was my last meal before my execution, and I was going to have a feast.

Halfway through our meal, I went to the bathroom. I thought maybe I was going to throw up, so I kneeled at the toilet. But I only retched a bit. Roger came into the bathroom and heard me.

ROGER: Hey, Arnie, are you okay?

ARNIE: Yeah, I'm just tired.

ROGER: All right, man. I'm happy you guys came tonight. You and Penultimate are a great couple, man . . . Are you going to try out for basketball?"

ARNIE: I knew that practice started in a week. I'd planned on playing. But I didn't know if the Coach liked Indians or not.

ROGER: You think you're good enough to play varsity?

ARNIE: No way, I’m junior varsity all the way.

ROGER: All right. It will be good to have you out there. We need some new blood.

ARNIE: Thanks, man. (To audience) I couldn't believe he was so nice. He was, well, he was POLITE! How many great football players are polite? And kind? And generous like that? It was amazing. (To Roger) Hey, listen. The reason I was getting sick in there is— (To audience) I thought about telling him the whole truth, but I just couldn't.

ROGER: I bet you're just sick with love.

ARNIE: No, well, yeah, maybe . . . But the thing is, my stomach is all messed up because I, er, forgot my wallet. I left my money at home, man.

ROGER: Dude! Man, don't sweat it. You should have said something earlier. I got you covered.

ARNIE: He opened his wallet and handed me forty bucks. Holy, holy. What kind of kid can just hand over forty bucks like that? (To Roger) I'll pay you back, man.

ROGER: Whenever, man, just have a good time, all right?

ARNIE: He slapped me on the back again. He was always slapping me on the back. We walked back to the table together, finished our food, and Roger drove me back to the school. I told them my dad was going to pick me up outside the gym.

ROGER: Dude, it's three in the morning.

ARNIE: It's okay. My dad works the swing shift. He's coming here straight from work.

ROGER: Are you sure? I'll bring Penultimate home safely, man.

ARNIE: So Penelope and I got out of the car so we could have a private good-bye. She had laser eyes.

PENELOPE: Roger told me he lent you some money.

ARNIE: Yeah, I forgot my wallet. (To audience) Her laser eyes grew hotter.

PENELOPE: Arnold? Can I ask you something big?

ARNIE: Yeah, I guess.

PENELOPE: Are you poor?

ARNIE: (To audience) I couldn't lie to her anymore. (To Penelope) Yes, I'm poor. (To audience) I figured she was going to march out of my life right then. But she didn't. Instead she kissed me. On the cheek. I guess poor guys don't get kissed on the lips. I was going to yell at her for being shallow. But then I realized that she was being my friend. Being a really good friend, in fact. She was concerned about me. I'd been thinking about her looks and she'd been thinking about my whole life. I was the shallow one.

PENELOPE: Roger was the one who guessed you were poor.

ARNIE: Oh, great, now he's going to tell everybody.

PENELOPE: He's not going to tell anybody. Roger likes you. He's a great guy. He's like my big brother. He can be your friend, too.

ARNIE: That sounded pretty good to me. I needed friends more than I needed my lust-filled dreams.

PENELOPE: Is your Dad really coming to pick you up?

ARNIE: Yes.

PENELOPE: Are you telling the truth?

ARNIE: No.

PENELOPE: How will you get home?

ARNIE: Most nights, I walk home. I hitchhike. Somebody usually picks me up. I've only had to walk the whole way a few times. (To audience) She started to cry. FOR ME! Who knew that tears of sympathy could be so sexy?

PENELOPE: (with tears in her voice) Oh, my God, Arnold, you can't do that. I won't let you do that. You'll freeze. Roger will drive you home. He'll he happy to drive you home.

ARNIE: I tried to stop her, but Penelope ran over to Roger's car and told him the truth. And Roger, being of kind heart and generous pocket, drove me home that night. And he drove me home plenty of other nights, too. . . . If you let people into your life a little bit, they can be pretty amazing.
```

---

## IC-0346: The Day the Voices Stopped

- Title: The Day the Voices Stopped
- Author (byline): Ken Steele
- Work: Not specified
- Publisher: Basic Books
- Publication date as stated: 978-0465082278
- Event as filed: Dramatic Interpretation
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
For thirty-two years Ken Steele lived with the devastating symptoms of schizophrenia. The voices arrived without warning on an October night in 1962 when Ken was 14 years old. Derisive voices that continually said derogatory things to and about him. For thirty-two years, destructive voices inhabited his disordered mind, teasing him, mocking him, driving him time and again to the very edge of life. . . and daring him to take the final step. They commanded he kill himself in horrific ways. This is how Ken’s story began . . .The Day the Voices Stopped by Ken Steele
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

KEN: (Pg 6-8) That evening, the voices won out. As my father quizzed me about what we had seen on TV, what I knew, what I thought, I did as the voices directed (overwhelmed, puts hands over ears and turns away) Dad became enraged. “Go to bed without dinner,” he ordered me, stalking out of the living room. It was a punishment he rarely imposed.

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

VOICE 2: (interrupting) Schizo – Schizo - Schizophrenia! (laughter)
```

---

## IC-0347: Dog Chameleon

- Title: Dog Chameleon
- Author (byline): Eric Bogosian
- Work: Sex Drugs and Rock & Roll, Pgs 81-90
- Publisher: Theatre Communications Group
- Publication date as stated: Nov 1996
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1486
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Bogosian
Book: Sex Drugs and Rock & Roll, Pgs 81-90
ISBN: 978-1559361248
Publisher: Theatre Communications Group
Date (Month/Year): Nov 1996
```

### Introduction (context only: never use it for content warnings)

```text
Dog Chameleon by Eric Bogosian
```

### Performance text (classify this)

```text
A man with suppressed anger. He tries to be pleasant.

MAN: (Pgs 81-90) Hey, I want to be normal, just like every other guy! Don't leave me out, come on! There's got to be more to life than worrying about the price of cigarettes, getting a job, what's on TV. I know-I know about normalcy. Don't tell me about normalcy!

I want to- drive a station wagon with a bunch of kids singing Christmas carols in the backseat. I want to go to the supermarket and compare prices. I want to lose weight while I sleep. I want to buy life insurance. I want to wear pajamas and a bathrobe, sneak into the kitchen in the middle of the night and steal a drumstick out of the refrigerator. Worry about my dog's nutrition. Or maybe just order something nice from the L. L. Bean catalog. . . a nice down parka maybe, a flannel shirt. . . something in corduroy!

I know all about normalcy!

I want to yell at my wife when she goes on a spending spree! I want to help my kids with their grades! I want to fertilize my lawn. I want to order my hamburger my way! I want to donate money to impoverished minorities!

But all that stuff costs money. Being normal is expensive, you know?

MAN: There was this rat scratching inside my wall the other night. After a while it sounded like it was inside my head. And I said, "Wait a minute! Wait one minute! I'm white, I'm an American! I'm a male! I should be doing better than this!

Ozzie and Harriet didn't have rats in the wall. There were no roaches in the Beaver's room! Even Mister Ed had heat! WHAT IS THIS?

This rat kept scratching and I realized something: times have changed.

It's a race to the death now. Anyone waiting around for the good life to show up is a fool! Anyone who thinks that playing fair will get you anywhere is blind!

Then I said, “Calm down, calm down, you're getting all excited about nothing. Sure you're poor, you're an artist! You have an artistic sensibility! Artists are supposed to be poor."

I want to be rich. And I want to be famous. These are normal desires, that should not be thwarted. If you thwart them, if you repress them, you get cancer.

I want fame! Look at me, man! Fame is what counts. Fame with money. Any jerk can go-to the top of some tower with a scope rifle and start shooting at people. That's not fame. I want the good kind. The kind with lots and lots of money. Any slob can win the lottery, it takes skill and brains to get the fame and the money at the same time. . . that's success, man. So everyone looks at you, wherever You go, and they say, "That guy, he did it. He got everybody to look at him, admire him and give him money, their money, at the same time!"

I heard about this guy, he made four-hundred-million dollars. Four-hundred-million dollars! I'd be happy with fifty million. Most people would still think I was a success, even if I wasn't as successful as that guy. I don't care what they think! I wouldn't even tell them how much money I have! I'd just ride around in my stretch limousine, and when I got tired of that I'd go home and I'd have this enormous mansion with fifty rooms . . . And . . . and I'd have this room with a trench around it full of pit bulls, and I'd have a chair that tilts back and a TV set with remote control and a big bowl of potato chips!

And I'd just watch TV all day and change the channels. Maybe I'd just sit in a large bathtub with lots of bubbles.

I hate people. They get in the way of a good time. Just when everything's getting good, they want something from you!

But I want you all to love me. Even though I hate all of you. Just joking. Just joking. Don’t get all excited. Nothing to get excited about. Just love me. Tell me I'm great. And pay me. And then we'll be even. For all the crap you've given me my whole life! I know, I know what you're all thinking, "What a jerk. All he does is talk about himself." Yeah? And what do you do? LISTEN!

I was wronged when I was little. I never really got what I wanted. Now it's time to even the score. Even if I tell you my plans you can't stop me. I'm gonna be so rich and powerful, no one will touch me.

And all those rich creeps who lorded over me, all those muscular jocks who kicked sand in my face, all those blondies who laughed at me when I asked them for a date, all those parsimonious, paternal, patronizing administrators at school and at the unemployment office and at the IRS and the police station. . . you'll all be sorry. You have no idea what I've got in store for you. Hah!

You know what it means to be really, really rich? You walk into a store and the jerk behind the counter smirks at you because he thinks you can't afford the most expensive watch in the case. . . You know the look they give you, they humor you, "Yes sir, may I help you?"

He doesn't want to help me, he doesn't want to help anybody. Hhe just wants to laugh at me! Won't show me the watch, won't take it out, won't even tell me the price. . .

Well, when I make it, I'm going to go back to that store and I'm not going to buy one watch, I'm not going to buy ten watches-I'm going to buy the whole store, and then I'll fire that patronizing jerk for laughing at me . . . And then, I'm going to find out where he lives and I'm going to buy his apartment building and I'm going to have him evicted. . . one more pathetic homeless person walking the streets in a state of permanent depression!

Or those big thugs that push into you when you're walking down the street and don't say they're sorry or nothing. Why? Because they think I can't fight back. They think I'm afraid of them. Well, when I make it, I'm gonna get me some bodyguards. They'll walk with me when I'm going down the street. And some idiot pushes into me and I'll just step aside and there's my. He won't know what's hit 'im. He'll just end up on the ground, looking up at me with glazed eyes, and I'll just lean over and step over 'im and say, "Excuse me. (Laughs)

You think I should be ashamed of myself? I HAVE NO GUILT! Because I am not a man. I am a dog. (barks a long howl)

You know what I find fascinating? Human nature. The nature of human beings. . . what they like, what they don't like, what turns them on, what turns them off. What incredible appetites they have. Night after night they stay glued to their TV sets watching some pinheaded newscaster going on and on about today's news. They munch on popcorn and suck up TV dinners as they absorb the minutiae pertaining to the day's massive mud slide or exploding chemical plant.

(Mimicking the newscaster) “Thousands dead and dying! Hundreds blinded!"

Munch. . . munch. . . "Carol, get some more salt while you're in the kitchen! . . . Oh wait, wait, come here, you have to see this-they're completely buried! Come on, you'll miss it, there's a commercial coming on!”

Then, these same people watch shows on educational TV about dolphins, then they cry . . . Then they stay up late to watch some old Christmas movie with Jimmy Stewart standing on a bridge on Christmas Eve; then they go berserk!

The next morning, they jump into their sporty compact cars, drink ten cups of coffee, and race each other on the highway while they sing along with some ardent rock singer screaming and yelling about emaciated, dark-skinned, hopeless people turning to dung half a world away.

So they feel so guilty they race home and write out a check for five dollars and mail it to some post-office box in New York City and then they feel so good about themselves, because they really, really care. . . (pause)

I know I'm negative. I know I'm not a nice guy. I know you all hate me. But I don't care.

Because at least I realize I'm a bad person, and for that tiny fragment of truth, I respect myself. That's why normalcy is so far out of my reach. Because you have to be blind to be normal. You have to like yourself, and the thought of that is so repellent to me that I'm ecstatic to be in the depressing place that I am!
```

---

## IC-0348: Dog Sees God

- Title: Dog Sees God
- Author (byline): Bert V. Royal
- Work: Not specified
- Publisher: Dramatists Play Service
- Publication date as stated: March 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CB, BEETHOVEN, MATT, TEACHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1704
- Already set (do not supply): none

### Source block (context only)

```text
Author: Bert V. Royal
ISBN: 978-0822221524
Publisher: Dramatists Play Service
Date (Month/Year): March 2007
```

### Introduction (context only: never use it for content warnings)

```text
Even the most devoted fans of the comic strip "Peanuts" must wish that Charlie Brown would just once change out of that yellow, jagged-striped shirt. Or shave his string of hair, kick that darn football or do something -- anything -- different. In this selection, that wish comes true for not only Charlie Brown, but for others in the original comic strip as well. They grow up and their transformation is definitely . . . different. Pigpen has grown up into a violent, homophobic jock – You’ll see him here as Matt. Charlie Brown, or CB, as he's called, becomes a popular kid with a mean streak who is still questioning his place in the world. And Beethoven (think Schroeder), the artistic pianist, has been long abused by the popular kids and his father.

Dog Sees God by Bert V. Royal
```

### Performance text (classify this)

```text
CB, a handsome, however sullen, teenager. (Voice over by Actor 2 as he “writes”)

CB: (Pg 7-8) Dear Pen Pal. I know it's been a few years since I last wrote you. I hope you're still there. I'm not sure you ever were. I never got any letters back from you when I was a kid. It was pretty frustrating when I was young, but now I'm glad that you won't respond. Just listen. That's what I want. (beat) My dog died. I don’t know if you remember, but I had a beagle. I went out to feed him and he didn't come bounding out like usual. I looked in the doghouse. There was blood everywhere. The blood belonged to a little yellow bird that had always been around. My dog and the bird used to play together. . . Anyway, the bird had been mangled. Ripped apart. By my dog. My parents called a center and they came and took him away. Later that day, they put him to sleep. When my dog died, that was when the rain cloud came back and everything went to hell . . .

CB: (Pg 20-24) (to audience) I was passing by the music room when I heard a song. The song was simple. Much more simple than what he usually played. (beat) Lights up on Beethoven playing the piano. He has a black eye. CB enters unseen by Beethoven. He stands and listens to the music, as if hypnotized by it. He begins to cry silently, but then accidentally lets out a sob. Beethoven abruptly stops, spins around and sees him. CB pulls himself together.

BEETHOVEN: You're not supposed to be in here. I have permission to practice during lunch. But nobody else.

CB: You've gotten really good. I mean, you always were, but - Who wrote that? Beethoven?

BEETHOVEN: Chopin.

CB: Do you mind if I just listen for a little while? (Beethoven resumes; CB cries) God. This is really embarrassing. (pause) My dog died. He got rabies. They, um, had to put him under. (beginning to ramble) Have you ever had someone close to you die and you can't stop thinking about what's happened to them? It's like you're stuck in this morbid place and there's so much death that you feel like your head is going to explode and it makes you think that maybe you're dead, too. (Beethoven slams his fist down on the keys) What?

BEETHOVEN: Well, it's just that you haven't spoken to me in years. Except to call me a "faggot" or to dislocate my shoulder and all of a sudden I get a stream-of-consciousness monologue about your dead dog while I'm trying to spend the only moments of my day that don't truly SUCK. Forgive my bluntness. But I *don’t care* about you or your morbid curiosities or your dead dog, so why don't you just leave?

CB: We were just messing with you.

BEETHOVEN: I haven't had lunch in the cafeteria in two and a half years for fear of going home with some part of it smeared across my shirt! I haven't been in a bathroom on campus since the time my head got slammed into the wall. I believe you were there. And what really kills me is that everybody wonders why kids bring guns to school. Maybe you're not the bully, but you stand idly by and watch. In my eyes that makes you even worse. So - Please. Just. Go.

CB: Maybe if you didn't act so – Well. Gay.

BEETHOVEN: And how does one act gay? (silence) By playing the piano? Maybe I'll stop carrying around a pink purse. What?! What is it?!

CB: You're being hostile and I'm just trying to talk to you like a civilized -

BEETHOVEN: I don't want to talk to you!!! I just want to be left alone!

CB: See, this is why you don't have any friends. Don’t be so melodramatic!

BEETHOVEN: You’re crying about a dead dog and I’M being melodramatic?! (Beethoven shoves CB. CB doesn't fight back. Beethoven hits him and CB begins to laugh) What's so funny?

CB: I'm sorry. It's just that I was scared of you for, like, a second. (Beethoven joins in the laughter)

BEETHOVEN: I'm sorry.

CB: No, it's okay. I deserved it. (beat) Promise me you won't bring a gun to school.

BEETHOVEN: I don't know where to get one. (silence) You were one of my best friends. You all were. I just don't get it.

CB: It's no consolation, but - well, can I be honest? (beat) No one knew what to say to you after your dad got arrested . . . I'm sorry we weren't there for you. (extends his hand) Truce?

BEETHOVEN: Okay. Truce. (shakes CB’s hand for longer than expected. CB pulls his away)

CB: Are you. . . ?

BEETHOVEN: I don't know. I've never had sex, so it would be hard to say at this point.

CB: But what about. . .?

BEETHOVEN: My dad? I don't think that's considered sex. (silence)

CB: Do you remember how my dog used to howl whenever you played the piano? What do you think happens to pets when they die?

BEETHOVEN: They go to heaven. . . There has to be some reward for having to live through this.

CB: (looks depressed) But my dog killed a living thing. Wouldn't God be mad?

BEETHOVEN: He was sick, CB. He couldn't help it. They say a dog sees God in his master. A cat looks in the mirror.

CB: (chuckling) I hate cats. TRANSITION

When asked to describe the melancholy of his original comic strip Peanuts, Charles Shultz said . . . it’s simple: “All the loves in the strip are unrequited; all the baseball games are lost; all the test scores are D-minuses; the Great Pumpkin never comes; and the football is always pulled away.” Life is hard in elementary school, and it doesn’t get any easier in high school. CB and Beethoven, both confused and looking for love, begin a relationship, but over the course of the next few weeks, the anxiety for Beethoven becomes more and more pronounced.

Beethoven at the piano. CB approaches with a paper sack and starts unpacking lunch on the piano.

CB: (Pg 41-43) I brought you lunch. (Beethoven stops playing and gives CB a look of despair and frustration) Hey, halfway through the day and I only got called a queer three times.

BEETHOVEN: That's because people are scared you'll beat them up.

CB: Don't worry. I've already started spreading the word that if they mess with my boyfriend, I'll be kicking some ass. (kisses the top of Beethoven's head)

BEETHOVEN: Your boyfriend? I don't want a boyfriend. . . This can't happen. CB, I really need to practice.

CB: You really need to eat.

BEETHOVEN: (losing it) CB! Just stop! Okay? This isn't what I want.

CB: What's the problem?

BEETHOVEN: THIS is the problem! I'm stressed out right now and I'm trying to calm my nerves by playing the piano . . . Look. The other night was great, but . . .You go back to being yourself. This is just too weird.

CB: (getting perturbed) Fine. I'll leave you alone. (grabs backpack and starts to exit; turns back)

BEETHOVEN: Just give me time. (CB exits) (to himself) Oh my God. (resumes playing with a smile as Matt enters)

MATT: Hey there, Liberace. (Beethoven stops playing and turns, trying to conceal his terror)

BEETHOVEN: Matt, you're not supposed to be in here.

MATT: Where's your boyfriend?

BEETHOVEN: He's not my boyfriend . . . Just leave me alone, okay? Please. I didn't do anything.

MATT: Play something. (Beethoven doesn't move. Matt bends Beethoven’s finger backwards, leading him to the keys; he begins to play) So, are you two, like, a couple now? Are you going to parade around the halls holding hands? Go to prom together? (beat) Can't you people just keep it hidden? Instead of throwing it in our faces? (Beethoven stops and looks at him; he realizes Matt's secret) CB is not like you. And if you so much as look at him again, I'll kill you. You got that, perv? (starts to exit)

BEETHOVEN: No.

MATT: What? (goes back to the piano) What did you say?

BEETHOVEN: I said no . . . Pigpen. (Matt grabs Beethoven in an act of violence; Beethoven screams) ***** SCENE *******

CB: (to audience) Frederic Chopin died of tuberculosis on October 17, 1849. He had two requests. He was terrified of being buried alive, so he asked that his heart be removed from his body. The second request was that Mozart's "Requiem" be sung at his funeral. (long beat) Beethoven didn't leave a note. So, I don't know if he had any last requests. (bell rings for class) ***** Classroom. CB does not want to be there *******

TEACHER: (Pg 44-45) (whaa – whaa question)

CB: Huh? (whaa – whaa question again) How does his death make me feel? No one even liked him. Who cares? He's dead! That's life. The world is full of people who have tough lives. But do you see them killing themselves? No. There are people out there who can't walk. Can't see. Do they give up? No. They keep going. Suicide is pathetic bullshit. It's weak. (Losing it) DID HE SAY GOODBYE TO ME?! I wish he was still here so I could twist his arm behind his back and shove his face in a toilet. (hits the wall and storms off) ***** SCENE *******

CB: (Pg 46) (writing to his pen pal – Actor 2 voices lines while Actor 1 “acts”) Sorry for unloading all of this. (Forcing a smile) I bet this is the longest letter you've ever gotten. Thanks for listening. Sincerely. No. Yours truly. No. Your pen pal. CB. TRANSITION

And weeks later, shockingly, CB’s silent pen pal replies

CB stands alone, holding the letter; just staring at it. He opens it tentatively (NOTE: In the original script, which includes many more characters . . . multiple characters not included in this cutting are assigned voice-over lines from the letter while CB silently reads it – This cutting contains all the original lines which CB can present himself)

CB: Dear CB. How unexpected to get a letter from you after all these years. I thought you had forgotten about me. It sounds like you're going through a pretty rough time and having to deal with situations that you feel like you can't handle - But if anyone is equipped to deal with these things, it's you. I promise that things get better.

I was talking to a girl the other day who told me of an incident that happened at her high school. There was a boy. Bullied. Tormented. To the point of opening fire on their cafeteria. He was quiet and awkward. No one ever spoke to him unless it was to insult him. He took the lives of many people. How differently things could have been through just one connection. No matter how great or small.

She lives where I live now. A place where there is no violence. Everyone treats others with kindness, love and respect. Can you imagine such a place? Don't concern yourself with death. Immerse yourself in life. Enjoy every moment that you're allowed. But keep asking questions, my dear friend.

A boy recently came to live down the street from me. He's had a tough life, but things are better for him now. He plays the piano like your friend. I often hear his music wafting from an open window, where a small yellow bird sits. Sometimes I cry when I hear it. But mostly I smile. He found a dog who likes to sing along. He tells me of a person he knew; Someone very special who means more than anything to him. A person that reminds me of you.

Maintain in your heart all that makes you who you are. You are a good man. (pause) Your Pen Pal. CS. (drops the letter and cries for his dog, his friend and for himself) CLOSING

C.S. -- Could this be Charles Shultz? or a symbolic message from the “Creator” or God. Pop culture hits like the Peanuts endure by being constantly recreated and experimented on by fervent fans. RIP Charles Shultz, your characters and your legacy live on.
```

---

## IC-0349: Don’t Sleep, There Are Snakes

- Title: Don’t Sleep, There Are Snakes
- Author (byline): Daniel Everett
- Work: Not specified
- Publisher: Pantheon Books
- Publication date as stated: Nov 2008
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1372
- Already set (do not supply): none

### Source block (context only)

```text
Author: Daniel Everett
ISBN: 978-0375425028
Publisher: Pantheon Books
Date (Month/Year): Nov 2008
```

### Introduction (context only: never use it for content warnings)

```text
The Pirahã (pronounced Pee-da-HAN) are a little known tribe of Amazonian Indians who live on the banks of two rivers in territory that, before Everett encountered them, had never been assigned officially to the tribe but that they defended, occasionally to the death. Largely peaceful, they have intermarried and retained a very primitive lifestyle that they consider to be in every way superior to that of outsiders, including Americans, for thousands of years.

Everett, then a Christian missionary, arrived among the Pirahã in 1977–with his wife and three young children–intending to convert them. What he found was a language that defies all existing linguistic theories and reflects a way of life that evades contemporary understanding: The Pirahã have no counting system and no fixed terms for color. They have no concept of war or of personal property. They live entirely in the present. Everett became obsessed with their language and its cultural and linguistic implications, and with the remarkable contentment with which they live–so much so that he eventually lost his faith in the God he’d hoped to introduce to them.

Don’t Sleep, There are Snakes by Daniel Everett
```

### Performance text (classify this)

```text
"Look! There he is, Xigagai, the spirit." "Yes, I can see him. He is threatening us." "Everybody, come see Xigagai. Quickly! He is on the beach!"

I roused from my deep sleep, not sure if I was dreaming or hearing this conversation. It was 6:30 on a Saturday morning in August, the dry season of 1980. The sun was shining, but not yet too hot. A breeze was blowing up from the Maici River in front of my modest hut in a clearing on the bank. I opened my eyes and saw the palm thatch above me, its original yellow graying from years of dust and soot. My dwelling was flanked by two smaller Piraha huts of similar construction, where lived Xahoabisi, Kohoibiiihiai, and their families.

Mornings among the Pirahas, so many mornings, I picked up the faint smell of smoke drifting from their cook fires, and the warmth of the Brazilian sun on my face, its rays softened by my mosquito net. Children were usually laughing, chasing one another, or noisily crying to nurse, the sounds reverberating through the village. Dogs were barking. Often when I first opened my eyes, groggily coming out of a dream, a Piraha child or sometimes even an adult would be staring at me from between the paxiuba palm slats that served as siding for my large hut. This morning was different.

I was now completely conscious, awakened by the noise and shouts of Pirahas. I sat up and looked around. A crowd was gathering about twenty feet from my bed on the high bank of the Maici, and all were energetically gesticulating and yelling. Everyone was focused on the beach just across the river from my house. I got out of bed to get a better look — and because there was no way to sleep through the noise.

I picked my gym shorts off the floor and checked to make sure that there were no tarantulas, scorpions, centipedes, or other undesirables in them. Pulling them on, I slipped into my flip-flops and headed out the door. The Pirahas were loosely bunched on the riverbank just to the right of my house. Their excitement was growing. I could see mothers running down the path, their infants trying to hold breasts in their mouths.

The women wore the same sleeveless, collarless, midlength dresses they worked and slept in, stained a dark brown from dirt and smoke. The men wore gym shorts or loincloths. None of the men were carrying their bows and arrows. That was a relief. Prepubescent children were naked, their skin leathery from exposure to the elements. The babies' bottoms were calloused from scooting across the ground, a mode of locomotion that for some reason they prefer to crawling. Everyone was streaked from ashes and dust accumulated by sleeping and sitting on the ground near the fire.

It was still around seventy-two degrees, though humid, far below the hundred-degree-plus heat of midday. I was rubbing the sleep from my eyes. I turned to Kohoi, my principal language teacher, and asked, "What's up?" He was standing to my right, his strong, brown, lean body tensed from what he was looking at.

"Don't you see him over there?" he asked impatiently. "Xigagai, one of the beings that lives above the clouds, is standing on the beach yelling at us, telling us he will kill us if we go to the jungle."

"Where?" I asked. "I don't see him."

"Right there!" Kohoi snapped, looking intently toward the middle of the apparently empty beach.

"In the jungle behind the beach?"

"No! There on the beach. Look!" he replied with exasperation.

In the jungle with the Pirahas I regularly failed to see wildlife they saw. My inexperienced eyes just weren't able to see as theirs did.

But this was different. Even I could tell that there was nothing on that white, sandy beach no more than one hundred yards away. And yet as certain as I was about this, the Pirahas were equally certain that there was something there.

Maybe there had been something there that I just missed seeing, but they insisted that what they were seeing, Xigagaí, was still there.

Everyone continued to look toward the beach. I heard Kristene, my six-year-old daughter, at my side.

"What are they looking at, Daddy?"

"I don't know. I can't see anything."

Kris stood on her toes and peered across the river. Then at me. Then at the Pirahas. She was as puzzled as I was.

Kristene and I left the Pirahas and walked back into our house. What had I just witnessed? Over the more than two decades since that summer morning, I have tried to come to grips with the significance of how two cultures, my European-based culture and the Pirahas' culture, could see reality so differently. I could never have proved to the Pirahas that the beach was empty. Nor could they have convinced me that there was anything, much less a spirit, on it.

As a scientist, objectivity is one of my most deeply held values. If we could just try harder, I once thought, surely we could each see the world as others see it and learn to respect one another's views more readily. But as I learned from the Pirahas, our expectations, our culture, and our experiences can render even perceptions of the environment nearly incommensurable cross-culturally.

The Pirahas say different things when they leave my hut at night on their way to bed. Sometimes they just say, "I'm going." But frequently they use an expression that, though surprising at first, has come to be one of my favorite ways of saying good night: "Don't sleep, there are snakes." The Pirahas say this for two reasons.

First, they believe that by sleeping less they can "harden themselves," a value they all share. Second, they know that danger is all around them in the jungle and that sleeping soundly can leave one defenseless from attack by any of the numerous predators around the village. The Pirahas laugh and talk a good part of the night. They don't sleep much at one time. Rarely have I heard the village completely quiet at night or noticed someone sleeping for several hours straight. I have learned so much from the Pirahas over the years. But this is perhaps my favorite lesson. Sure, life is hard and there is plenty of danger. And it might make us lose some sleep from time to time. But enjoy it.

Life goes on.

I went to the Pirahas when I was twenty-six years old. Now I am old enough to receive senior discounts. I gave them my youth. I have contracted malaria many times. I remember several occasions on which the Pirahas or others threatened my life. I have carried more heavy boxes, bags, and barrels on my back through the jungle than I care to remember. But my grandchildren all know the Pirahas. My children are who they are in part because of the Pirahas. And I can look at some of those old men (old like me) who once threatened to kill me and recognize some of the dearest friends I have ever had — men who would now risk their lives for me.

This book is about the lessons I have learned over three decades of studying and living with the Pirahas, a time in which I have tried my best to comprehend how they see, understand, and talk about the world and to transmit these lessons to my scientific colleagues. This journey has taken me to many places of astounding beauty and into many situations I would rather not have entered. But I am so glad that I made the journey — it has given me precious and valuable insights into the nature of life, language, and thought that could not have been learned any other way.

The Pirahas have shown me that there is dignity and deep satisfaction in facing life and death without the comfort of heaven or the fear of hell and in sailing toward the great abyss with a smile. I have learned these things from the Pirahas, and I will be grateful to them as long as I live.
```

---

## IC-0350: The Dramatic Faces of Robin Williams – A Tribute

- Title: The Dramatic Faces of Robin Williams – A Tribute
- Author (byline): Various Authors (See sources after each monologue below)
- Work: Not specified
- Publisher: Not specified
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Program
- Speaker labels in the text: PATCH, MR. KEATING, CHRIS
- Teaser before the introduction: No
- Spoken words (computed): 1223
- Already set (do not supply): none

### Source block (context only)

```text
Author: Steve Oedekerk
ISBN: N/A
Publisher: Scriptfly.com
Date (Month/Year): 1998
Author: James DeMonaco and Gary Nadeau
ISBN: N/A
Publisher: Scriptfly.com
Date (Month/Year): 1996
Author: Tom Schulman
ISBN: N/A
Publisher: Scriptfly.com
Date (Month/Year): 1989
Author: Ronald Bass
ISBN: N/A
Publisher: Scriptfly.com
Date (Month/Year): 1998
```

### Introduction (context only: never use it for content warnings)

```text
When Robin Williams died by his own hand in 2014, the world gasped for air, shocked that a man with Williams’ gifts could perform an act of such desperation. Williams could make us laugh; but just as powerfully, could sober us up in seconds with some of films’ most powerful monologues. This is a tribute to his brilliance and to the amazing legacy he left behind . . . The Dramatic Faces of Robin Williams.
```

### Performance text (classify this)

```text
PATCH: You ask me if I’ve been practicing medicine. Well if this means opening your door to those in need, those in pain, caring for them, listening to them, applying a cold cloth until a fever breaks, if this is practicing medicine, if this is treating a patient, then I am guilty as charged.

TRANSITION In 1969, a suicidal Hunter Adams voluntarily commits himself to a mental institution. Once there, he finds that helping his fellow inmates gives him a purpose in life. Inspired, he leaves the asylum and vows to become a doctor. "Patch" Adams is determined to find a way to help his patients, even if it means being expelled from medical school. This is his monologue to the review board in Patch Adams by Steve Oedekerk

PATCH: What’s wrong with death? What are we so mortally afraid of? Why can’t we treat death with a certain amount of humanity and dignity and decency and, God forbid, maybe even humor. Death is not the enemy. If we’re going to fight a disease, let’s fight one of the most terrible diseases of all, indifference. Now, I’ve sat in your schools and heard people lecture on transference and professional distance. Transference is inevitable. Every human being has an impact on another. Why don’t we want that in a patient-doctor relationship? That’s why I’ve listened to your teachings and I believe they’re wrong. A doctor’s mission should be not just to prevent death but also to improve the quality of life. That’s why, you treat a disease, you win you lose; you treat a person, I guarantee you win no matter what the outcome. Now here today, this room is full of medical students. [HE TURNS TO THE STUDENTS] Don’t let them anesthetize you. Don’t let them numb you to the miracle of life. Always live in awe of the glorious mechanism of the human body. Let that be the focus of your studies and not a quest for grades which will give you no idea of what kind of doctor you’ll become. And don’t wait until you’re on the ward to get your humanity back. Start your interviewing skills now. Start talking to strangers, talk to your friends, talk to wrong numbers, talk to everyone. [HE TURNS BACK TO THE COMMITTEE] I want to be a doctor with all my heart. I wanted to become a doctor so I could serve others. And because of that, I’ve lost everything, but I’ve also gained everything. I’ve shared the lives of patients and staff members at the hospital, I’ve laughed with them, I’ve cried with them. This is what I want to do with my life. And, as God is my witness, no matter what you decide today, I will still become the best damn doctor the world has ever seen.

TRANSITION You see, life doesn’t guarantee a happy ending, just a series of struggles and the occasional moment of grace. It is in these moments, the role and Robin Williams become one. Take, for example, the graduation speech from Jack in 1993. Because of an unusual aging disorder, Progeria, Jack finishes high school at age 18 with the body of an 80-year-old man. Jack by James DeMonaco and Gary Nadeau JACK: I don't have very much time these days so I'll make it quick. Like my life. You know, as we come to the end of this phase of our life, we find ourselves trying to remember the good times and trying to forget the bad times, and we find ourselves thinking about the future. We start to worry, thinking, "What am I gonna do? Where am I gonna be in ten years?" But I say to you, "Hey, look at me!" Please, don't worry so much. Because in the end, none of us have very long on this Earth. Life is fleeting. And if you're ever distressed, cast your eyes to the summer sky when the stars are strung across the velvety night. And when a shooting star streaks through the blackness, turning night into day... make a wish and think of me. Make your life spectacular. I know I did.

TRANSITION "But only in their dreams can men be truly free. 'Twas always thus, and always thus will be."

Remember Dead Poet’s Society? In 1989 Williams portrayed John Keating, an English teacher at a rigid prep school, who inspires a love of learning in his students. Dead Poet’s Society by Tom Schulman

MR. KEATING: “We don't read and write poetry because it's cute. We read and write poetry because we are members of the human race. And the human race is filled with passion. And medicine, law, business, engineering, these are noble pursuits and necessary to sustain life. But poetry, beauty, romance, love, these are what we stay alive for. To quote from Whitman, "O me! O life!... of the questions of these recurring; of the endless trains of the faithless... of cities filled with the foolish; what good amid these, O me, O life?" Answer. That you are here - that life exists, and identity; that the powerful play goes on and you may contribute a verse. That the powerful play goes on and you may contribute a verse. What will your verse be?”

“Boys, you must strive to find your own voice. Because the longer you wait to begin, the less likely you are to find it at all. Thoreau said, “Most men lead lives of quiet desperation.” Don’t be resigned to that. Break out!” Go on, lean in. Listen, you hear it? – – Carpe – – hear it? – – Carpe, carpe diem, seize the day boys, make your lives extraordinary.”

TRANSITION From Dead Poets to life after death. In What Dreams May Come by Ronald Bass, Williams plays Dr. Chris Nielsen. He journeys from Heaven to the depths of Hell to rescue his wife’s soul after the death of their two children. In the words of Robin Williams: “Good people end up in Hell because they can’t forgive themselves.” That’s what suicide is all about.

CHRIS: I'm sorry, babe, but there's some things I have to say. I'm sorry for all the things I'll never give you. I'll never buy you another meatball sub with extra sauce -- that was a big one! I'll never make you smile. I just wanted us to be old together, just two old farts laughin' at each other as our bodies fell apart, together at the end by that lake in your painting. That was our Heaven, see? There's lots of things to miss: books, naps, kisses, and fights! God, we had some great ones. Thank you for those. Thank you for every kindness. Thank you for our children. For the first time I saw them. Thank you for being someone I was always proud to be with. For your guts. For your sweetness. For how you always looked, for how I always wanted to touch you. You were my life. I apologize for every time I failed you. Especially this one.

CONCLUSION No matter what people tell you, words and ideas can change the world. – Robin Williams There is a profound wisdom in these monologues. Robin Williams spoke the lines from the depths of his soul; they jumped off the screen and went straight into ours. What made his performances so powerful? Maybe it’s because we knew he wasn’t acting.

NOTE: All original screenplays can be purchased from Scriptfly.com.
```

---

## IC-0351: Elephant’s Graveyard

- Title: Elephant’s Graveyard
- Author (byline): George Brant
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: April 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: HUNGRY TOWNSPERSON, ENGINEER, RINGMASTER, YOUNG TOWNSPERSON, TOWNSPEOPLE, MUDDY TOWNSPERSON, STRONGMAN, CLOWN, TRAINER, YOUNG TOUNSPERSON, TOUR MANAGER, MARSHAL, STEAM SHOVEL OPERATOR, PREACHER, MUDDY TONSPERSON
- Teaser before the introduction: Yes
- Spoken words (computed): 1627
- Already set (do not supply): none

### Source block (context only)

```text
Author: George Brant
ISBN: 978-0573698156
Publisher: Samuel French, Inc.
Date (Month/Year): April 2010
IL State Qualifier
Historical Reference material:
https://rarehistoricalphotos.com/murderous-mary-1916/
```

### Introduction (context only: never use it for content warnings)

```text
Her nickname, “Big Mary,” came well-earned. Touted as “The Largest Living Land Animal On Earth,” the five-ton elephant stood taller than the popular Barnum & Bailey’s star, Jumbo, hovering over him by a supposed three inches. Playing musical instruments, standing on her head, and even catching baseballs, this gentle giant awed crowds all over the country. Mary’s future would find an expiration date, however, when the circus made its way to Tennessee.

Based on true events . . . Elephant’s Graveyard by George Brant
```

### Performance text (classify this)

```text
HUNGRY TOWNSPERSON: (Pg 10) It was September and there was a Town . . . Erwin, Tennessee

ENGINEER: It was September and there was a Town and a Circus

RINGMASTER: Sparks World Famous Shows Proudly Presents . . .

YOUNG TOWNSPERSON: an Elephant . . . Mary . . . (Pg 15) We dreamed her before we saw her.

TOWNSPEOPLE: (Pg 16) Mary! Mary! Mary!

MUDDY TOWNSPERSON: (Pg 15) She was plastered on every telephone pole.

RINGMASTER: (Pg 16) Ladies and Gentlemen, Children of All Ages!

STRONGMAN: Proudly present a tremendous exhibition of wealth and splendor

CLOWN: All new for 1916.

TRAINER: Starring Mary: the largest living land animal on Earth.

YOUNG TOUNSPERSON: (Pg 15) The Circus was coming!

TOWNSPEOPLE: (Pg 16) Mary! Mary! Mary! (beat)

TOUR MANAGER: (Pg 10) And there was as Man with Red Hair. (A train whistle)

RINGMASTER: (Pg 17) An elephant is an investment. You’ve got the trained seals, the trapeze, the Strongman. Fine, but they aren’t the bread and butter. No rubberneck comes to a circus doesn’t have a big elephant.

TRAINER: They love a parade. All elephants do in the wild anyway. Wild elephant herd follows the leader and the leader is the biggest female. So they all march behind Mary, one behind the other. Let me tell ya, only thing better than watchin’ an elephant parade is being in the elephant parade. Sittin’ on top of the world – on top of Mary, legs wrapped around her back, head in the clouds.

TOUR MANAGER: (Pg 18) They’re not just for show. Hardest workers I got. Once that train stops in a town – they’re mine. Get ‘em to load and unload the boxcars, push up the tent poles. . . (beat) Tennessee started off with a bang. Circus can tell how it goes over by how many locals want to run away with it afterwards. Fifteen —That was a record.

CLOWN: (Pg 19) There was a Man with Red Hair

TOUR MANAGER: (Pg 20) Shocka red hair. Tells me he’s good with animals. He says, I want to work with the elephants, I have to work with the elephants.

TRAINER: (Pg 21) Lou knocks on my car, tells me I got a new roommate. Goofy-lookin’ red-haired guy. I show Red his corner. He gripes about the smell and I tell him get used to it. Townies think elephants smell bad in the ring, try sleepin’ with one in a boxcar. He shuts up when he sees Mary, looks at her like she’s the answer to his prayers.

TOUR MANAGER: We left Kingsport for Erwin. (A train whistle)

TRAINER: (Pg 24) I’d shown Red how to feed her, groom her, that’s it. That’s all he knew. One day. One day! What the hell can you learn in one day? In India, guy stays with an elephant his whole life, like a marriage. Here. . . Lou waltzed in—says . . .

TOUR MANAGER: (Pg 25) Shorty, he wants to ride Mary in the march. Back off and give the new guy a chance.

TRAINER: I shoulda said something. I shoulda told him she was mine. I didn’t. Just stepped aside. Maybe made a face. That was my big protest, a face. (beat) It’s trust. Trust you build up over years, not one day. Every peanut, every bath, every pat on the trunk. It’s love. But Red didn’t have time for any of that. (beat) TRUNKS UP! (Circus music as the parade begins)

YOUNG TOWNSPERSON: (Pg 26) That big elephant was leadin’ the whole thing. That goofy guy – red hair? He was up on her back.

TOWNSPEOPLE: Mary, Mary, Mary!

HUNGRY TOWNSPERSON: (Pg 27-28) A band was playin, people rushin’ out, circus plowin’ through the middle of town . . . Erwin Garbage Department on strike until further notice. Clean up your own junk, people of Erwin. We on strike. And thus, the Holy Grail of Garbage left in the mud: a juicy chunk of watermelon. That’s when the dominoes start to fallin’ Elephant see melon . . . walks toward [it].

Elephant rider encourages elephant to abandon melon – is most insistent. Elephant hook across [its] head. Breaks elephant hook across [its] tusk.

Elephant decides she’s had enough – picks the rider off [its] back and throws [him] into a soda pop stand.

[Just when] the rider thinks it’s over, the elephant walks over and puts [its] foot on [his] head. (scream) [And his] head explodes.

MUDDY TOWNSPERSON: (Pg 29) She stepped on his skull. Crushed it. (beat) Coulda been any of us.

MARSHAL: (Pg 30) It coulda ended there, but that wouldn’ta been right, that wouldn’ta been justice. It wasn’t walking away from this. Erwin don’t look kindly upon murderers.

TOUR MANAGER: (Pg 31) Tried to get in touch with Red’s family, friends. Didn’t have none.

TRAINER: Like he didn’t exist except for us, like he was born to do nothin’ but cause us trouble.

RINGMASTER: Still have a show to do that night. Must go on. DOORS!

TOUR MANAGER: I told Charlie, maybe we should keep Mary out, maybe the people’d forget. But he told me what I already knew:

RINGMASTER: They won’t forget. Aren’t coming to see the circus. Coming to see the killer. (Pg 32) Ladies and Gentlemen, Children of All Ages . . . Sparks World Famous Shows Proudly Presents . . .

TOUR MANAGER: Normal night we play up the danger, talk up the toothless tier. Not this time. Brought Mary out like she was the most innocent a’ God’s creatures. (Drum roll / cymbal crash. A gasp)

TOWNSPEOPLE: (Pg 33) Kill it. Kill it. Kill it!

YOUNG TOWNSPERSON: It got louder . . .

TOWNSPEOPLE: Kill it. Kill it. Kill it!

YOUNG TOWNSPERSON: The marshal and people were wavin’ guns around. Everybody shoutin’. All ‘cept the colored section.

CLOWN: No, no, no! Red was one of us. Part of the circus. He knew the risks. You townies go no claim here. Military has its own court – so does the circus.

TRAINER: She was favoring her left tusk! They have nerves in there, big ones, run down half the tooth. You all saw him hittin’ her tusk with the hook, whackin’ the spit outta it, tryin’ to get her to behave, to stay in line. What’s she s’posed to do? She stopped him. That’s all. She stopped him!

TOWNSPEOPLE: Kill it. Kill it. Kill it!

YOUNG TOWNSPERSON: (Pg 34) Fin’ly the Ringmaster raised his hand.

RINGMASTER: (Pg 35) (hand raised) Ladies and Gentlemen, Children of All Ages – the Circus Understands Your Wishes. Theis Mary Matter Will Be Settled to Your Liking Tomorrow . . . and We are Open to Suggestions.

ENGINEER: (Pg 36) They talked about electrocuting it, frying it like some of them had seen in the moving picture Thomas Edison made. But that was copycat stuff. (beat) The railyard. There’s a crane there can lift 100 tons. Now, something like that could do something special, something never been done before. Something like that could hang her. Hang her like any other murderer.

MUDDY TOWNSPERSON: Eye for an eye. Erwin’ll fin’ly be clean.

TRAINER: (Pg 37) (sadly) So now Lou and Sparks need my help. (to the men) I wasn’t good enough to handle her while she was alive, but I’m good enough to help you kill her? (beat) I will never forgive you; (to audience) [but] I stay ‘cause if I don’t, they’ll mess it up.

MUDDY TOWNSPERSON: (Pg 41-42) Mornin’ fin’ly came. Got to the railroad tracks, saw men in the only suits they owned. Women in their Sunday best, prancin’ ‘round with parasols like it was Easter. People standin’ top of boxcars, picknic baskets, punch. Laughin’, dancin’. You could feel it – we were ready.

TRAINER: TRUNKS UP! (marching drums)

STEAM SHOVEL OPERATOR: The killer was in front. Them elephants marched out holdin’ each other’s tails with their trunks – like a parade.

TRAINER: (Pg 37) Tuskers aren’t stupid, they know when somethin’s up. You have to make her think it’s a normal march. She can’t go out there alone. Mary has to lead the parade, like it’s any other parade.

STEAM SHOVEL OPERATOR: (Pg 42) They walked through the railyard up to the crane, and this guy chained the killer’s foot to a train track.

TRAINER: (calming Mary down) It’s okay, it’s okay, it’s okay. Ready? Showtime, sweetie.

STEAM SHOVEL OPERATOR: The guy hooked the chain ‘round her neck, patted her back and stood up. (applause)

YOUNG TOWNSPERSON: She looked scary.

PREACHER: (Pg 44) Helpless.

STEAM SHOVEL OPERATOR: Confused.

MUDDY TOWNSPERSON: Guilty.

MARSHAL: Like a killer.

ENGINEER: The crane groaned, gears grindin and --- (gasp)

MUDDY TONSPERSON: It rose up steady till it was standin’ on it’s hind ligs, tiptoe. Toenails scrapin’ the railroad track . . . like it was doin’ a trick.

MARSHAL: (Pg 45) But then we started wonderin’ why that thing wasn’t goin’ any higher up.

HUNGRY TOWNSPERSON: Nobody remembered to unhook her. Her foot was still chained to the track.

STEAM SHOVEL OPERATOR: They were rippin’ her in half, pullin’ her leg at this weird angle.

MUDDY TOWNSPERSON: Her leg broke – a bone ‘bout as big as my whole body – breakin’, I could feel it in my spine, my spine buckled, ached in sympathy, rang like a tuning fork.

STEAM SHOVEL OPERATOR: Shoulda left then, I s’ose. But I stayed to see ‘em unhook her foot, lift her up again –

PREACHER: (Pg 46) Think she was nearly gone, then. Or woulda been, soon. That is . . . if the chain hadn’t broke.

YOUNG TOWNSPERSON: The chain popped and she came crashin’ down onto the railroad track with this sound like an oak tree crackin’ in half. That guy who climbed her before started screamin’ like he was the one fell down. And they handed him a thicker link chain. And I couldn’t believe it, but he hooked her up again.

MARSHAL: (Pg 47) Crane lifted it off its feet again – higher . . .

YOUNG TOWNSPERSON: Higher . . She made some noises, some . . . air just kinda puffed outta her trunk and then that . . . that was it. (quiet)

MUDDY TOWNSPERSON: (with shock and sadness) I let my breath out. I breathed in, lungs searchin’ for that sanctified air. Waiting to be made clean. But the air . . . it tasted no different. It was flat and stale and rank.

MARSHAL: (Pg 48) (proudly) Look. Look at that thing swing. We hung an elephant today. An elephant. We made the impossible possible. This is America. And we can do anything we dream of. Anything at all!

HUNGRY TOWNSPERSON: (Pg 50) (disgusted) People go short mem’ries. But not me. (beat) All them colored boys led out to the yard must blur together somethin’ fierce, ‘ause nobody ever talk about how they hung colored boys in Erwin. They just talk about how they hung an elephant. Damndest thing. (train whistle)

RINGMASTER: (Pg 52) It was September and there was a Town and there was. Circus and there was a Man with Red Hair and there was an Elephant. (beat) You wait . . . After midnight, after the townsfolk have gone home and the prying eyes of Erwin are closed; sleeping with the certainty that their boogie monster is dead; You wake up the clowns and tell them to digger he up. Saw off her tusks and being them to you. You have to see what you can salvage, what you can get for the ivory. An elephant is an investment.
```

---

## IC-0352: Emergency

- Title: Emergency
- Author (byline): Daniel Beaty
- Work: Emergency and Through the Night
- Publisher: Samuel French, Inc.
- Publication date as stated: March 2011
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: REPORTER, CLARISSA, BESSIE, RONALD, BIACK FEMALE SCHOLAR, VENDOR, BLACK FEMALE SCHOLAR, SLAVE-OLOGIST, RODNEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1125
- Already set (do not supply): none

### Source block (context only)

```text
Author: Daniel Beaty
Book: Emergency and Through the Night
ISBN: 978-0573699528
Publisher: Samuel French, Inc.
Date (Month/Year): March 2011
```

### Introduction (context only: never use it for content warnings)

```text
A growing throng of African Americans flood the shores near the Statue of Liberty. Beyond rational explanation, the invisible past has materialized and it quickly become an . . . Emergency by Daniel Beaty.
```

### Performance text (classify this)

```text
REPORTER: (Pg 13) We are live at Liberty Island with this breaking news report. A slave ship has just risen out of the Hudson River in front of the Statue of Liberty. That's right, you heard me. A slave ship has just risen out of the Hudson River in front of the Statue of Liberty. Slave-ologists are busy trying to figure it out. Let's get some live on the spot feedback from the crowd gathering here at Liberty Island.

CLARISSA: (Pg 14) I mean, I ain't never really thought about slavery before this slave ship . . . They ain't teach us nothin' about it in school. Naw, they ain't teach us about Africa or nothing. Yeh, okay, they taught us about Egypt. The pyramids and stuff, right? Yeh, but nothing about Africa. (listens to a voice from the crowd) Egypt is in Africa? Them people was black?!

BESSIE: (Pg 13) (a seventy something soulful southern grandmother) When I first saw the slave ship, I was in stunned silence. Then I started to pray, "Thank you Jesus! Hallelujah! Thank you for not forgetting about your people. Thank you for this sign to help us remember who we are."

RONALD: (Pg 14) (a forty something high class colored man) It's . . . it's . . . appalling! It's a setback. There are black people succeeding in every field-tennis, golf, we even run for president. This is the last thing we need.

REPORTER: (Pg 24) Tensions are high and escalating here at Liberty Island. Hundreds of people are arriving with suitcases, old trunks, even trash bags full of clothes attempting to board the ship. Oprah is calling this slave ship a "full circle "ah ha" moment." Liberty is in a state of emergency.

RONALD: (Pg 14-15) I work in corporate America and one of my colleagues just came into my office in tears after hearing the news on the radio and she tells me she has papers that prove her great great grandparents owned slaves and she wants to apologize. And I said, "Why are you apologizing to me, Cathy? It was your great great grandparents." And she's hysterical, and so I say, "Look at me, Cathy. You've been to my home, our children play together. Cathy, I'm your boss!"

BIACK FEMALE SCHOLAR: (a fifty-something; angry sistah with an education) This slave ship is proof that slavery is not history, its reality. I write books on Post Traumatic Slave Syndrome - how slavery still impacts the minds and hearts of black people today. Look at these people's faces. This is exactly why most of us never watch those PBS specials or talk about slavery with our children. We don't know what to do with the anger.

VENDOR: (Pg 22) Yo! Check it! Slave ship buttons! Yo' ma, check it, I got yo' slave' ship buttons!

BLACK FEMALE SCHOLAR: (Pg 23) (distracted for a moment by the vendor then returning to her speech) It's not about the few us that make it; it's what slavery has done to the psyche of the masses. Why do you think there are more black people in jail and poor than any other group? Because we're inferior? No, the ghetto is a modern-day plantation.

RONALD: (Pg 39) Slavery ended two hundred years ago. We need to get over it. It's been forty years since the Civil Rights Movement. It's time to move on people. This place is out of control.

BLACK FEMALE SCHOLAR: (Pg 23) Don't get it twisted; you can have a six-figure income, a PhD, and still be a slave. But it's never too late to redeem the past, is it?

REPORTER: (Pg 26) Reporting live from Liberty Island where the crowds have gotten out of control. Some people are running around screaming, speaking in unknown tongues as if possessed and dancing what appears to be ancient African dance. (Actress does just that: screams, speaks in an unknown tongue and dances an ancient African dance)

RONALD: (Pg 39-40) (Distracted by the dancing, but then returns to his speech) Not all white Americans owned slaves. Many fought to free them. Affirmative action was reparations enough. I'm not an Uncle Tom. I'm not a sellout. I'm just tired of black people asking for a handout. I don't need to go back to Africa. I can reconnect . . . to that black man begging money for food (points to a person in the crowd). Reconnect to that black woman prostituting herself to keep a roof over her head. (points to a person in the crowd). Reconnect to those black kids in the orphanages who are like four and five-years old living with AIDS who nobody wants to adopt because they're sick. Yes, they are the product of this slave ship, but nobody's going to help us if we don't start helping ourselves! (pause) We are here now. We have arrived.

REPORTER: (Pg 26) We are speaking now with a slave-ologist. You are from Ghana, West Africa, correct?

SLAVE-OLOGIST: (forty-something West African man) Yes, I am. We have identified the slave ship as one of the many dispatched from the Cape Coast Slave Dungeons of Ghana, West Africa. We call this slave ship Remembrance. (Pg 37-38) (To the crowd gathered around) As a slave-ologist, slave dungeons are my specialty. And with this slave ship, I feel compelled to tell you what I know. I will take you on a tour as if you were standing with me in Ghana, West Africa. (Actress joins the tour and reacts silently to the Slave- Ologist) The slave dungeons you are about to see are the largest facility where the Africans were kept during the Transatlantic Slave Trade. As our tour begins, we ask that you leave your rage and pain at the entrance gate because there is enough inside. Thank you and please follow me. (As he turns upstage, his hands cross violently above his head as if chained. Enraged, he speaks the following words of resistance to an imaginary guard.) Olokikijulu amanla owetu! Olokikijulu amanla owetul (To crowd) We have now entered the Slave Dungeons where the Africans were kept. Here, they defecated on the same floor where they slept and ate. This is where the Africans were brought before they boarded slave ships like Remembrance for the passage to America . . . TRANSITION But then, just as mysteriously as The Remembrance appeared, the great slave ship sank. Leaving many to wonder if it was real, or just a figment of their collective consciousness.

REPORTER: (Pg 49-51) Remembrance has disappeared. Moments ago the slave ship Remembrance began to sink back into the Hudson River. Divers were immediately dispatched into the water and all they see is an endless stretch of skeletons, human bones, and the chains are gone. And what's even more bizarre is that while Remembrance has disappeared from the vision of most of us here at Liberty Island others are insisting that they can still see it floating right here in front of the Statue of Lib-erty. (The Reporter fades from the scene, leaving Rodney alone on stage)

RODNEY: (A performance poet) The pain I feel and the pain I see
It's a pain particular to being black in this country,
And it's a pain beyond race, class, sex, or any other label of identity-
We are all afraid, all confused, all connected ... all Free
As Free as we choose to be
I tell the story for that man begging money for food,
For that child living with AIDS,
Our bones, our bones, our bones they breathe:
In this world we may be bound but our spirits are free
And our bones, our bones, our bones they breathe:
We can overcome if we change the way we see
See ourselves, see our past, see our possibility
Our bones, our bones, our bones they breathe:
We are all family!
We must not die!
We must not sleep!
We must wake up!
Wake up and DREAM!
```

---

## IC-0353: Empanada for a Dream or Dios te va Castigar (God Will Punish You)

- Title: Empanada for a Dream or Dios te va Castigar (God Will Punish You)
- Author (byline): Juan Francisco Villa
- Work: Not specified
- Publisher: Lulu.com
- Publication date as stated: July 2012
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JUAN, MAMI, TIO ALVARO, RITCHIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1615
- Already set (do not supply): none

### Source block (context only)

```text
Author: Juan Francisco Villa
ISBN: 978-1312261921
Publisher: Lulu.com
Date (Month/Year): July 2012
```

### Introduction (context only: never use it for content warnings)

```text
When Juan Francisco Villa’s mother immigrates to NYC from Colombia at the young age of 19, she couldn’t imagine what life had in store for her. She quickly finds a community of extended family and other Colombian immigrants on the Lower East Side, but the harsh realities of living in a foreign land plunge her family into the dark underworld of cocaine trafficking.

Villa captures his own child-like wonder of the American dream and the dangerous choices some make when the dream is not so easy to achieve.

Empanada for a Dream or Dios te va castigar (God will punish you) by Juan Francisco Villa
```

### Performance text (classify this)

```text
JUAN: You have not tasted heaven until you have had one of my mom's homemade empanadas de carne molida. (ground beef empanadas) The one thing I craved every day of my life. The one thing I would trade all my Batman comic books for -- no -- my Batman and X- Men comic books for was a homemade empanada.

CRRRRRRRACK of dawn all the women are up. Mi Abuelita (grandmother) Consuelo, my mom, my Tias (aunts) Negra and Martha, my sisters Sandra and Jenine, my cousins Giselle, Sohanny, Xiomarra, and Carinoso and whoever else happened to be staying at our place would get up for the birthday/holiday ritual.

They would break off into teams. One team would get the harina (cooking flour) to mold with the water and then pancake it flat with a homemade plancha (flat iron). Another would make the homemade pique (traditional hot sauce from Puerto Rico). What my friends still talk about to this day. The immortal pique that as long as you had a metal spoon in it, would never go bad. . . according to my mom. Another team made el desayuno (breakfast) for everyone in the apartment. Scrambled eggs with tomatoes and green onions soaked in Manteca (butter). Do not call it a Denver omelette. Do not call it Huevos a la Mexican (Mexican eggs). Son huevos perico! (They are parrot eggs!) That smell would wake up all of apartment 3A.

By afternoon the empanadas were made. By evening the entire neighborhood was knocking on our door. By night the empanadas were gone. My mom's Colombian empanadas were legendary in the Caribbean dominated neighborhood. You have not tasted heaven until you have had one of my mom's homemade empanadas de carne molida.

Birthdays were fun growing up. They always are when you are a kid. Everyone pitched in to make it as fun as possible. The morning of, the victim would wake up and as they were being hugged and kissed with birthday wishes, a barrage of raw eggs were smashed on their head. It’s a Colombian tradition. For good luck. Colombia and it's traditions. (beat, then solemnly) I hated being Colombian.

JUAN: To be Colombian was to NOT be American. The last time I was in Colombia, I could see them milk their cows and it tasted nasty. It tasted like the earth. And I'm no organic foods connoisseur. I don't care about no "the closer it is to the tree the better it is for you." No, "the closer it is to a tree" the more it tasted like an immigrant.

Colombians only know how to play futbol (American soccer). They didn't have Levi jeans, and they always stared at my Spanish. My American English cartoons were all in Spanish over there. I couldn't understand anything.

The worst part was coming back home. Security would endlessly question us at the airport. We would always be detained and put in a room where they would rip apart our suitcases cuz they "had an inside tip on us." They would never find anything.

My mom at 19 was the first to immigrate here in the states. She was the pioneer of the family. She was lonely. She met my father: boisterous, charming, possessive and addicting.

It is 1981. My mom, my pops, my sis, Little Juan Francisco Villa, all of us snuggled together, sleeping together in one bed. Freezing [our] little Colombian asses off but warm with the laughter of love and opportunity of life here in the 6th floor of 169 Allen St. Such an American thing to have, apartment buildings that go past the 3rd floor. Until my mom left my pops and moved us to the 3rd Floor of 169 Allen St. the Lower East Side, New York.

My uncles were like fathers to me after my mom kicked my pops out. (beat) I have this memory. It was my birthday. I was turning 11 years old, and my uncles would want to splurge on me, but my mom was not a fan of it.

MAMI: No lo trate asi. (Don’t treat him like that) I don't want him to feel like a king. Como un (Like an) Americana thinking he doesn't have to work for anything. No! When you do not work hard. Dios te va castigar. (God will punish you.)

JUAN: Somehow pushing me to accept that I will never get what I dream of having. Hard work gets you closer but it's never enough. So my uncle, Tio Alvaro. He would be like

TIO ALVARO: Juanita! It's your birthday. Whaddaya want? I can give it to you. Toda lo que quiera. Cuando yo era pequeno no tenia nada. (Whatever you want. When I was little, I had nothing.)

JUAN: Woooooow! No one ever said that to me. No one ever asked me what I really wanted. So I said: MCDONALDS!!!!! Yeah. That's what I said. $.39 hamburgers and $.49 cheeseburgers. Now, this was back in the day when I could eat, and eat, and eat. I was a scrawny kid, but I could throw down with the best of them. My Uncle says . . .

TIO ALVARO: How many you want? Don't be ashamed. How many you want? Es tu cumpleanos (It's your birthday) . . . DREAM BIG.

JUAN: I would look at my mom. She would sigh and I would belt out 4 CHEESEBURGERS!!!! (to audience) I get them and chomp them down fast.

TIO ALVARO: Diablo Juanita. You ate them fast. Like a big strong man. You want more?

JUAN: SI! 4! 4 Mas! (to audience) So I now have had a total of 8 and I am feeling good.

TIO ALVARO: Wow, Juanita. Todavia tienes hambre? (Are you still hungry?)

MAMI: No mas. He's already eaten a lot. And he's going to get sick.

TIO ALVARO: Leave him alone. He's a little boy. Juanito, you still hungry.

JUAN: 4 mas! . . . por favor. (to audience) And there was a gasp all around us. I didn't even know people were paying attention to me.

MAMI: Be careful God is going to punish you.

JUAN: So I sat down and ate 4 more cheeseburgers bringing my total up to 12! I barely was able to get the last one in. I felt like a king. And we walked home and no one talked. I was sauntering with a smile. My uncle was bobbing with a smile and my mom was grimacing all the way home, not happy that I got what I wanted.

I get home and within 40 minutes my stomach is killing me. I feel like I am possessed by a demon. Seriously, I was doing the whole Gremlins in sunlight writhing in pain act. So I do what any 11 year old would do and . . . MAAAAAMMMMMMIIIIIII!!!! My stomach hurts!

MAMI: What did I tell you?! That you were going to get sick and God was going to punish you.

JUAN: (softly) Dios te va castigar. From that day on everything changed. And I mean for all of us. . . (beat) My uncles introduced coke to the neighborhood. Then it took a life of its own. My blood has caused so much pain and death in this neighborhood. My uncles murdered a lot of people.

RITCHIE: Your Tio Alvaro ruled this area; him and your Tio Luis. They were crazy, man. This dude was sellin some of Alvaro’s stash on the side. So, he walked behind the guy. Held his head up high and just cut this dude’s throat. I’ve never seen so much blood. Then Alvaro just walks away.

JUAN: Dios te va castigar. My Tio Chepe met a woman named Liliana from Colombia. She was the woman that everyone in my family loved. She was quiet. She didn't argue. She spoke Spanish. New Year's Eve party 1990 – that was the last time my entire family was together. My Tio Chepe came. Liliana was there, of course, but they left early -- she was feeling ill. They went back home deep in Queens. It was 3 am-she was like: "I’m hungry. I want ice cream." He goes to get ice cream. He's gone for hours. She calls the cops. They go searching for him. He's- he's- he's lying in the street. My family gets hysterical when they get the news. We get to the hospital. There's a ventilator and I don't recognize him. He is soooo swollen. so swollen. He had gotten beat with aluminum baseball bats. You ever heard an aluminum bat hit a human head? Sounds just like hitting a baseball. Kink. kink. kink.

4 days later. My family pulled the plug. He died. And months later we find out that this perfect woman. This perfect Colombian was in love with another man, another drug dealer. So they worked on a plan to have my uncle killed. Dios te va castigar.

This entire building feels like it is in a famine. It feels post-apocalyptic. This entire building has been infested with this mindset, this transition from bettering each other to bettering themselves. The American Dream.

MAMI: ERES LAZY! Yo nose porque no sirves para nada. (I don't know why you're good for nothing.) I take you to church. I've sent you to the best schools. I've bought you clothes.

JUAN: Ma! Callate! (Be quiet!) You are constantly at me! It's never enough for you. If I get an A, then it's "Why didn't you get an A+" Oh, I'm sorry, do you not understand what I am saying? You have been in this country for 20 years. Lean English! Here's a word in English: COCAINE. That's what's in my blood. Death. Why would anyone want to say they are Columbian? My grandmother, your mother, let her own kids sell that s*** on the streets and kill sooo many of our own people from our own neighborhood who trusted us! You never stopped them either. I think God did notice. He took away your brothers. Don't you see what's happening?! Dios te va castigar! (long beat, he is gasping for breath in his rage)

She reaches for me and this is where it happens. (another long beat, then softly) This is where my mom says that I hit her. I remember all of this up to this moment. I don't remember hitting her. (sadly) [But I do remember] You have not tasted heaven until you have had one of my mom's homemade empanadas . . .
```

---

## IC-0354: Equus

- Title: Equus
- Author (byline): Peter Shaffer
- Work: Not specified
- Publisher: Penguin
- Publication date as stated: Oct 1984
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DYSART, ALAN, MOTHER, FRANK, JILL
- Teaser before the introduction: No
- Spoken words (computed): 1654
- Already set (do not supply): none

### Source block (context only)

```text
Author: Peter Shaffer
ISBN: 978-0140481853
Publisher: Penguin
Date (Month/Year): Oct 1984
```

### Introduction (context only: never use it for content warnings)

```text
In this selection, a psychiatrist, Martin Dysart, investigates the savage blinding of six horses with a metal spike. The atrocity was committed by an unassuming seventeen-year-old stable boy named Alan Strang, the only son of an opinionated father and a genteel, religious mother. Alan is found guilty, but mentally disturbed, and he is sentenced to an inpatient ward at Rokesby Psychiatric Hospital. Can Dr. Dysart discover the motive behind Alan’s brutal actions; can Alan be saved from himself? Equus by Peter Shaffer.
```

### Performance text (classify this)

```text
DYSART: (Pg 21-23) Hallo. I’m pleased to meet you (he puts out his hand. Alan does not respond in any way. Dysart opens his file) Is this your full name? Alan Strang? (Silence) And you’re seventeen. Is that right? Seventeen? . . . . Well?

ALAN: (singing low) Double your pleasure, Double your fun, With Doublemint, Doublemint, Doublemint gum. (See note at the end of this selection for a link to the Doublemint jingle)

DYSART: (unperturbed) Now, let’s see. You work in an electrical shop during the week. You live with your parents.

ALAN: (approaching him, hostile but still singing) Double your pleasure, Double your fun, With Doublemint, Doublemint, Doublemint gum.

DYSART: (appreciatively) That’s a good song. Please do that one again. (Silence. The boy glares at him; Dysart speaks to audience) (Pg 26-29) It took him two more days of commercials, and then he snapped. He burts in – just like that – without knocking or anything. Fortunately I didn’t have a patient with me.

ALAN: (belligerently) [My mother] knows more than you. I bet I do too. I bet I know more history than you . . . Who was the Hammer of the Scots?

DYSART: I don’t know: who?

ALAN: King Edward the First. Who never smiled again? (with hardly a pause to allow the doctor to answer) It was Henry the First. (bragging) I know all the Kings.

DYSART: And who was your favorite?

ALAN: John . . . he put out the eyes of that smarty little – (Pause, sensing he has said something wrong) Well, he didn’t really. He was prevented, because the gaoler* was merciful! He was prevented! . . . Who said “Religion is the opium of the people?” (giggles inappropriately)

DYSART: (to audience) The odd thing was, he said it with a sort of guilty snigger. The sentence is obviously associated with some kind of tension. It’s probably his dad. He may say it to provoke his wife.

ALAN: Mind your own beeswax!

DYSART: (to audience) I want[ed] to have a look at his home, so I invited myself over. If there’s any tension over religion, it should be evident on a Sabbath evening! ***** Scene breaks to Dysart’s meeting with Alan’s parents *****

MOTHER: (pg 30) It’s all so unbelievable, Doctor . . . Alan’s always been such a gentle boy. He loves animals! Especially horses. He even has a photograph of one up in his bedroom. (Pg 45) It’s a most remarkable picture, really. You very rarely see a horse taken from that angel – absolutely head on. It comes out all eyes. (pg 30-32) And when he was seven or eight, I used to have to read him the same book over and over, all about a horse. It was called Prince, and no one could ride him. (Mother steps back in time to a scene with Alan)

ALAN: (excited, younger voice) Why not? . . . Why not? . . . Say it! In his voice. Say it! Say it! . . . . Use his voice!

MOTHER: (‘proud’ horses voice that will be used by Alan later) Because I am faithful! (Alan giggles) My name is Prince and I’m a prince among horses! Only my young Master can ride me! Anyone else – I’ll throw off! (Alan giggles louder – Mother speaks to both Alan and Dysart simultaneously) Did you know that when Christian calvary first appeared in the New World, the pagans thought horse and rider was one person?

ALAN: (amazed) One person?

MOTHER: Actually, they thought it must be a god.

ALAN: A god!

DYSART: That’s fascinating. I never heard that before . . . Can you remember anything else like that you may have told him about horses?

MOTHER: (to Dysart) They’re in the Bible, of course. ‘He saith among the trumpets, Ha ha’ (The Ha Ha should be a trumpet-like sound) The Book of Job. Such a noble passage. You know – (quoting to both Dysart and Alan) ‘Hast thou given the horse strength?’

ALAN: (responding) ‘Hast thou clothed his neck with thunder?’

MOTHER: ‘The glory of his nostrils is terrible!’

ALAN: ‘He swallows the ground with fierceness and rage!’

MOTHER: ‘He saith among the trumpets – ‘

ALAN: (trumpeting) ‘Ha! Ha!’ (and again) ‘Ha! Ha!’

MOTHER: (to Dysart) We’ve always been a horsey family. My grandfather used to ride every morning . . . indulging in equitation, he called it.

ALAN: (trying the word) Equitation

MOTHER: (to Dysart) I told him how that came from equus, the Latin word for horse. Alan was fascinated by that word.

ALAN: (savoring it) Equus!

DYSART: (turns to Frank) (Pg 33 – 35) Would you say she was closer to him than you are?

FRANK: They’ve always been thick as thieves. I can’t say I entirely approve – especially when I hear her whispering that Bible to him hour after hour, up there in his room. I’m an atheist, and I don’t mind admitting it. If you want my opinion, it’s the Bible that’s responsible for all this . . . A boy spends night after night having this stuff read into him; an innocent man tortured to death – thorns driven into his head – nails into his hands – a spear jammed through his ribs. It can mark anyone for life, that kind of thing. The boy was absolutely fascinated by all that. He was always mooning over religious pictures. I mean real kinky ones, if you receive my meaning. (Pause) Bloody religion – it’s our only real problem in this house.

ALAN: (begins to murmur) Ek! . . . Ek! . . . Ek! . . .

DYSART: Pg 46 (to audience) It was then – that moment – I felt real alarm. ***** Scene returns to a session between Dysart and Alan ******

DYSART: (Pg 37-38) [Alan], what is Ek? (no response) [O.K., then] what is your first memory of a horse? How old were you? (still no response) I thought you might like to talk about it.

ALAN: (Singing) Pg 23 Double your pleasure, Double your fun,

DYSART: Pg 37 Come on, now. You can do better than that.

ALAN: (Singing louder) Pg 23 With Doublemint, Doublemint, Doublemint gum.

DYSART: Pg 37 All right. We’re finished for today.

ALAN: That’s not fair! (Emptily clenching his hands. He turns away, pauses, then sullenly) On a beach . . . [I was] six (pg 48) (pause – He is in great emotional difficulty) The horse . . . his sides were all warm, and the smell . . . (Pause) When the horse first appeared, I looked up into his mouth. It was huge. There was this chain in it. I said ‘Does it hurt?’ and he said – the horse said – said – (He stops in anguish then continues desperately in the voice of the horse) (Pg 66-67) Yes. (as Alan) I’ll take it out for you. (as horse) It never comes out. They have me in chains.

DYSART: Like Jesus? (silence) Only his name isn’t Jesus, is it? What is it? You can tell me, Alan. Name him.

ALAN: (with great difficulty and nearly inaudibly) Equus.

DYSART: Now think of the stable. What is the stable? His Temple? His Holy of Holies?

ALAN: (quietly) Yes. (returning to the present) (Pg 48-49) It was always the same, after that. Every time I heard one clop by, I had to run and see. I couldn’t take my eyes off them. Just to watch their skins. The way their necks twist, and sweat shines in the folds . . . (Pause) I can’t remember when it started. Mum reading to me about Prince who no one could ride, except one boy. Or the white horse in Revelations. ‘His eyes were as flames of fire.’ Words like reins. Stirrup, Flanks . . . Even the words made me feel – (pause, Alan’s breathing becomes quicker, louder) The horse is the most naked thing you ever saw! No one understands! . . . except cowboys. They do. I wish I was a cowboy. They’re free. No one ever says to cowboys (mimicking his father) ‘Receive my meaning’! Or ‘God’ all the time (mimicking his mother) ‘God sees you, Alan. God’s got eyes everywhere – ‘ (he stops abruptly, filled with emotion) I’m not doing any more! . . . . I hate this!

DYSART: (Pg 106) Here . . . here . . . Sssh . . . calm now. Breathe in deep. (Alan complies and takes a couple of calming breaths) Pg 66 Good boy. Now, [imagine] you’re in your bedroom at home. You’re twelve years old. You’re looking at Equus from the foot of your bed. Now tell me. Why is Equus in chains?

ALAN: (kneeling as before a church altar; he may even cross himself in the Catholic tradition) For the sins of the world. (Alan begins praying silently, the audience can see his lips moving, but can’t understand any words)

DYSART: (Pg 53- 55) (listens for a moment then interrupts) Tell me something. Who introduced you to the stable to begin with?

ALAN: (rising reluctantly – he’d like to continue his worship) Someone I met . . . [at] Bryson’s.

DYSART: The shop where you worked? (Alan steps into a flashback scene) ***** Scene shifts to Alan’s first meeting of Jill *****

JILL: Hallo. Have you any blades for a clipping machine? – To clip horses.

ALAN: (Pause. He stares at her, open mouthed – in awe) You work at Dalton’s Stables.

JILL: (amused) You’re the boy who’s always staring into the yard around lunch-time. Are you looking for a job or something?

ALAN: (eagerly) Is there one?

JILL: We can always use extra hands. Can you ride?

ALAN: No . . . No . . . I don’t want to.

JILL: (shrugging her shoulders) It’d mainly be mucking out. . . . Come up on Saturday. I’ll introduce you to Mr. Dalton.

ALAN: (Pg 57-59) (in pantomime, scene shifts to Alan at the stable for the first time – He is lost in wonder. He starts almost involuntarily to kneel on the floor in reverence before the horse stalls, but is interrupted by the cheery voice of Jill. He straightens up guiltily)

JILL: This is Nugget. He’s my favorite. (she picks up a curry-comb and begins showing Alan how to brush the invisible body of Nugget.) Don’t be afraid to do it hard. The harder you do it, the more the horse loves it. Push it right through the coat: like this. Down towards the tail and right through the coat . . . You try. (She hands him the brush)

ALAN: (embarrassed and excited, he performs his own pantomime, copying her movements and echoing Jill’s words reverently) Nice and easy. Never rush. Down towards the tail and right through the coat.

JILL: You’ve got a feel for it. I can tell. It’s going to be nice teaching you. (Jill exits)

ALAN: (runs his hands over Nugget’s flesh. Lifts his palm to his face and smells it deeply, closing his eyes – he is lost in the sensation)

DYSART: (softly interjecting) Was that good? Touching them.

ALAN: (with a faint groan) Mmmm. (silence as Alan resumes bushing Nugget)

DYSART: How about the girl? Did you like her? (silence) Did you take her out? Come on now: tell me. Did you have a date with her? Tell me if you did.

ALAN: (Angry at being pulled out of his fantasy; Alan suddenly explodes in a rage – yelling) TELL ME! Tell me, tell me, tell me, tell me! On and on, sitting there! Just like Dad. On and on and bloody on! Tell me, tell me tell me! (Pg 73-74) (turning away from Dysart, Alan shifts into his ritual, chanting voice as a way to soothe himself) Equus – son of Fleckwus – son of Neckwus. The king rides out on Equus, mightiest of horses. (Alan pantomimes mounting Nugget) Only I can ride him. Equus, my God-slave! . . . Now the King commands you. (Alan pantomimes riding Nugget, his voice becoming louder and more forceful; and equally more disturbed) And Equus the mighty rose against All! His enemies scatter, his enemies fall! Trample them, trample them! My flanks! (rubs the outsides of his thighs) My hooves! (looks lovingly at his own hands) Equus -- Bear me away! Make us One Person! (more and more frantic in his fantasy) One Person! One Person! (He rises up on the horse’s back and calls like a trumpet) Ha-HA! . . . . Ha-HA! . . . Ha-HA! (Silence – slowly Alan dismounts, lowers his head an kneels once again in front of his God, Nugget – his breathing slows, he looks up reverently and cries) AMEN!!

DYSART: (interrupting again, softly) (pg 88-89) [Alan], you are going to tell me everything that happened with this girl.

ALAN: (Pg 98) (as if in a trance) The Stables . . .

DYSART: (Pg 100) The temple? The Holy of Holies? ***** Scene flashes back to Alan and Jill at the stable *****

JILL: (Pg 99) - (suggestively) What’s the matter? Don’t you want to?

ALAN: (aching to) Yes! (desperately fearful as he looks at the horses in their stalls) Them! . . . Them! . . . (low) Horses. (Alan starts shaking)

JILL: Look, if the sight of horses offends you, we can just shut the door. You won’t have to see them. All right?

ALAN: (pg 100-102) (to Dysart) What else can I do? . . . I can’t say! I can’t tell her . . . . (to Jill) Lock it!

JILL: It’s just an old door. What’s the matter with you? They’re in their [stalls]. They can’t get out.

ALAN: (emphatically) Lock it! (to Dysart as he describes the stable) [It’s a] large room. Straw everywhere. Some tools. . . (picks up a hoof pick) A hoof pick! (Alan mentally assesses the stable almost in a trance) At the end this big door. Behind it. . . (trembling he can’t continue)

DYSART: (Dysart helps) Horses. How many?

ALAN: Six . . . She put her mouth [on] mine. It was lovely! Oh, it was lovely! (Alan’s trembling increase and he begins cry)

DYSART: (gently) What was it? You couldn’t? Though you wanted to very much?

ALAN: I couldn’t . . . see her. Only Him. Every time I kissed her – HE was in the way . . . No! (suddenly he crouches in the corner like a beast in a cage)

JILL: (Pg 103-104) Alan. It’s all right . . . Don’t worry about it. Alan, look at me. Alan?

ALAN: Get out! . . . (he snatches up the invisible pick) GET OUT!

JILL: Alan . . . (moving away from him warily) Listen: you don’t have to do anything. Nothing at all. Why don’t we just lie here together in the straw. And talk.

ALAN: (to Dysart) He was there. Through the door. The door was shut, but he was there! . . . He’d seen everything. I could hear him. He was laughing. (Alan reverts to his memory and speaks to Equus) Friend . . . Equus the Kind . . . The Merciful! . . . Forgive me! (Silence) (Pg 105-106) I’ll never do it again. I swear . . . I swear! . . . (Silence, then in a moan) Please! (pause as Alan is overcome with fear) I see his eyes! They are rolling! (in the horse’s voice) ‘I see you. Always! Everywhere! Forever!’ (Alan’s voice in terror) Eyes! . . . Eyes like flames – coming – coming! God seest! God seest! NO! . . . . (Collecting himself, Alan moves slowly toward Nugget, the pick concealed behind his back. He strokes Nugget’s muzzle, then says gently) Equus . . . Noble Equus . . . Thou – God – Seest (long pause) NOTHING! (raising the pick, Alan violently stabs out Nugget’s eyes, then yelling in hysteria he collapses on the ground, stabbing at his own eyes with the invisible pick) Find me! . . . Find me! . . . KILL ME!
```

---

## IC-0355: Eukiah

- Title: Eukiah
- Author (byline): Lanford Wilson
- Work: 21 Short Plays
- Publisher: Smith & Kraus
- Publication date as stated: May 1993
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BUTCH, EUKIAH
- Teaser before the introduction: Yes
- Spoken words (computed): 1434
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lanford Wilson
Book: 21 Short Plays
ISBN: 1880399318
Publisher: Smith & Kraus
Date(Month/Year): May 1993
```

### Introduction (context only: never use it for content warnings)

```text
Eukiah, a young stable boy, earns his keep by caring for horses. Some people have an affinity for animals . . . After all, animals are safe. It loves you unconditionally and once you have been adopted by an animal, it would never hurt you. People, however, are much more complex. Eukiah, although viewed a backwards by most people, has learned this over time. Animals you can trust . . . but not people . . . not even family.

Eukiah by Lanford Wilson
```

### Performance text (classify this)

```text
Butch walks into the light. He is a young. powerful. charming man; everybody's best friend. He is also menacing. Nothing he says is introspective. Everything is for a purpose. During the indi-cated beats of silence he listens; for Eukiah to answer, for the sound of breathing, for the least indication of where Eukiah is. The play is a seduction. Voices have a slight echo in here.

BUTCH: Eukiah? (Beat.) Eukiah? (Beat.) Barry saw you run in here, so I know you're here. You're doin' it again, Eukiah, you're jumping to these weird conclusions you jump to just like some half-wit. You don't wanna be called a half-wit, you gotta stop actin' like a half-wit, don't ya? You're gettin' to where nobody can joke around you, ya know that? What kind of fun is a person like that to be around, huh? One you can't joke around? We talked about that before, remember?

(Beat.)

BUTCH: What are you thinkin'? You thinkin' you heard Harry say something, you thought he meant it, didn't you? What did you think you heard? Huh? What'd you thing he meant? Eukiah? (Beat.) You're gonna have to talk to me, I can't talk to myself here. (Beat.) Have you ever known me to lie to you? Eukiah? Have you ever known that? (Pause. He might walk around some.) Okay. Boy, this old hangar sure seen better days, hasn't it? Just like everything else on this place, huh? Been pretty much a losing proposition since I've known it, though. Probably you too, hasn't it? Hell, I don't think they have the wherewithall anymore, give even one of those or barns a swab a paint. You think? Might paint 'em pink, whattaya think? Or candy stripes. Red and white. Peppermint. You'd like that. (Beat.) This'll remind you of old Mac's heyday, though, won't it? Private airplane hangar. Talk about echoes, this is an echo of the past, huh? or Mac had some winners, I guess, about twenty years ago. That must have been the life, huh? Private planes, keep 'em in your private hangar. You got your luncheons with the dukes and duchesses. Winner's Circle damn near every race. If they wasn't raised by 01' Mac or their sire or dam one wasn't raised by or Mac, I don't imagine anybody'd bother to bet on em, do you? Boy that's all gone, huh? Planes and limos and all, dukes and duchesses-good lookin' horses, though. Damn shame we can't enter 'em in a beauty contest somewhere. I know, you're attached to 'em, but I'll tell you they make damn expensive pets. What was you? Out by the paddock when Barry was talkin' to me? You think you overheard something, is that it? What do you think you heard? You want to talk about it? I know you'd rather talk to me than talk to Barry, huh? Eukiah? (Pause.) Is this where you come? When you run off all temperamental and sulking? Pretty nasty old place to play in. Echoes good though. Gotta keep awful quiet if you're trying to be secret like you always do in a place like this. Why do you do that? You got any idea? I'm serious, now. Run off like that. They're waitin' supper on you, I guess you know. You know how happy they're gonna be about it, too. (Beat.) Eukiah? What was it you think you heard, honey? What? Was it about the horses? Cause I thought I told you never trust anything anybody says if it's about horses.

EUKIAH: (Still unseen.) I heard what Barry said. You said you would. too.

BUTCH: (Butch relaxes some. smiles.) Where the dickens have you got to? There's so much echo in here I can't tell where you are. You back in those oil drums? You haven't crawled up in the rafters have you? Watch yourself. We don't want you getting' hurt. I don't think those horses would eat their oats at all, anybody gave 'em to 'em 'cept you. I think they'd flat out go on strike. Don't you figure?

EUKIAH: They wouldn't drink, you couldn't get 'em to.

BUTCH: Don't I know it. Pot-A-Gold, for sure. You're the only one to get him to do anything. I think he'd just dehydrate. He'd blow away, you wasn't leadin' him. We could lead him to water but we couldn't make him to drink, isn't that right? (Beat.) What are you hiding about? Nobody's gonna hurt you. Don't I always take up for you? You get the weirdest ideas. What do you think you heard Barry say?

EUKIAH: He's gonna bum the horses.

BUTCH: What? Oh, man. You are just crazy sometimes, these things you dream up. Who is? Barry? What would he wanna do something crazy like that for?

EUKIAH: I heard you talkin.'

BUTCH: Can you answer me that? Why would he even dream of doin' something like that?

EUKIAH: For the insurance.

BUTCH: No, Eukiah. Just come on to supper, now, I got a date tonight, I can't mess around with you anymore. You really are a half-wit. I'm sorry, but if you think Barry'd do something like that, I'm sorry, that's just flat out half-witted thinkin'. It's not even funny. The way you talk, you yak all day to anybody around, no idea what you're saying half the time; anybody heard something like that there wouldn't be no work for me or you or anybody else around here, 'cause they'd just lock us all up.

EUKIAH: You said you would.

BUTCH: I would? I would what?

EUKIAH: You said it was about time somebody did somethin'.

BUTCH: Eukiah, come out here. I can see you over by that old buggy, my eyes got used to the dark. There ain't no sense in hiding anymore. (Beat.) Come on out, damn it, so we can go to supper. I'm not going to play with you anymore. Come on. Well, just answer me one thing. How's bumin' 'em up gonna be any better than splittin' a hoof or somethin' like that? Come on, crazy. The least little thing happens to make a horse not run, it's the same as if he had to be destroyed, you ought to know that.

(Eukiah is just visible now. He is maybe 16 years old. He is slow and soft; he has the mentality of an 8 year old.)

EUKIAH: Yeah, but they already took Pot-A-Gold and Flashy and that gray one, the speckled one, off. They already sold 'em.

BUTCH: Which one do you call Flashy, you mean Go Carmen? The filly? And Old Ironside? Why would they do that?

EUKIAH: Cause they're the best ones. Then they put three no good horses in their stalls, so nobody would know. And they're gonna burn 'em and nobody would know. And they're gonna burn 'em and nobody can tell they ain't the horses they're supposed to be, Butchy.

BUTCH: Nobody could run Pot-A-Gold somewhere else, Euky. You know those numbers they tattoo in his mouth? That's gonna identify him no matter where he goes, anybody'll know that's Pot-A-Gold.

EUKIAH: Some other country. They wouldn't care.

BUTCH: Anywhere on earth.

EUKIAH: They got some plan where it'll work, 'cause I heard 'em.

BUTCH: I don't know what you think you heard, but you're really acting half-witted here.

EUKIAH: Don't call me

BUTCH: Well, I'm sorry, but what would you call it? A person can't bum down a bam full of horses, Euky. What a horrible thing to think. No wonder you get scared, you scare yourself thinking things like that. Those horses are valued, hell I don't even know, millions of dollars probably. Insurance inspectors come around, they take a place apart. You tell me, how would somebody get away with a trick like that?

EUKIAH: What was you talkin' about then?

BUTCH: I don't even know. Where it was you heard what you thought you heard. You're too fast for me. You'll just have to go in to supper and ask Mac what Harry was talking about, won't you? Would that make you feel better? Instead of jumpin' to your weird conclusions. Now, can you get that out of your head? Huh? So we can go eat and I can take a bath and go on my date? Is that all right with you? Then I'll come back and tell you all about it. Got a date with Mary, you'd like to hear about that, wouldn't you? (Eukiah begins to grin.) Yes? That's okay with you, is it?,

EUKIAH: I guess. (He moves into the light, closer to Butch.)

BUTCH: You guess. You're just going to have to trust me, Eukiah, no body needs money that bad. Not even on this place. I don't even think nobody could get away tryin' to pull something like that. (He puts his arm around Eukiah's neck and they start to move off, but Butch has Eukiah in a head lock. He speaks with the strain of exertion.) Not unless there was some half-wit on the place that got his neck broke being kicked in the head and got burned up in the fire. (Eukiah goes to his knees. Butch bears down on his neck; it breaks with a dull snap. He lets Eukiah slump to the floor. Butch is breathing hard, standing over Eukiah's body.) I thought I told you. Never trust anything anybody says if it's about horses.
```

---

## IC-0356: Faith

- Title: Faith
- Author (byline): Eric Lane
- Work: Take Ten II: More Ten-Minute Plays, Pg 113
- Publisher: Vintage Books
- Publication date as stated: Nov 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MICHAEL, FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 481
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Lane
Book: Take Ten II: More Ten-Minute Plays, Pg 113
ISBN: 978-1400032174
Publisher: Vintage Books
Date (Month/Year): Nov 2003
```

### Introduction (context only: never use it for content warnings)

```text
When a priest sexually abuses a child, the effects can be devastating. The most trusted person imaginable suddenly does something that feels terribly wrong. It's a shattering experience. In this selection, Michael (now a grown man) summons the courage to confront his abuser.

This performance is dedicated to the multitude of children betrayed by "pillars of the church."

Faith by Eric Lane
```

### Performance text (classify this)

```text
(A confessional, simply represented by two chairs. FATHER, a priest in his forties to sixties, listens to MICHAEL 's confession. MICHAEL is in his twenties to thirties. Average looking.)

MICHAEL: . . . Bless me father for I have sinned.

FATHER: How long has it been since your last confession?

MICHAEL: Many years.

FATHER: Tell me your sins, my child.

MICHAEL: I have killed someone. (A pause.)

FATHER: Go on.

MICHAEL: Over and over. In my mind. Killed them for what they have done. And I'm scared.

FATHER: Scared of what?

MICHAEL: What will happen.

FATHER: What will happen?

MICHAEL: When it's no longer in my mind but me, actually not thinking but when it's time- Trying to believe, to find a reason not to-But less and less and wondering-

FATHER: Wondering what?

MICHAEL: Why?

FATHER: Wondering why what?

MICHAEL: How someone could have done this -- could have taken so much, when I trusted, believed . . . Why did I believe?

MICHAEL: I trusted, believed . . . Why did I believe?

FATHER: You were right to have faith.

MICHAEL: Not then. Not in him. He stole from me. Took things-

FATHER: Things.

MICHAEL: Not things. But important-Irreplaceable. Not things.

FATHER: Something closer to you.

MICHAEL: My youth. My joy. My innocence. He took my innocence.

FATHER: He hurt you.

MICHAEL: My soul. He took my soul.

FATHER: No one can take your soul. Only the Lord has that divine power.

MICHAEL: Took it. Pretending he knew things. Secrets. I didn't know.

FATHER: Your soul is still yours. No one can-

MICHAEL: Took it. When it wasn't his to take. To hold. Close. Me not knowing, thinking I should believe. That this is faith. That this is what God wants from me.

FATHER: You must forget.

MICHAEL: How can I forget?

FATHER: You must forgive.

MICHAEL: Forgive?

FATHER: You must.

MICHAEL: No. No forgiveness. Not for this. Not him.

FATHER: The Lord forgives our sins.

MICHAEL: I'm not the Lord.

FATHER: Washes them away.

MICHAEL: Too easy.

FATHER: Offers salvation.

MICHAEL: Only words.

FATHER: And hope.

MICHAEL: No meaning.

FATHER: To those who pray.

MICHAEL: I'm out of prayers.

FATHER: Prayers are answered.

MICHAEL: I can't.

FATHER: Redemption.

MICHAEL: No.

FATHER: Salvation.

MICHAEL: Can't.

FATHER: Hope.

MICHAEL: None.

FATHER: Faith.

MICHAEL: Gone.

FATHER: Joy.

MICHAEL: I can't.

FATHER: Love.

MICHAEL: I can't forgive you. (A beat.) I can't forgive you.

FATHER: Tell me your name.

MICHAEL: You don't get to ask. You don't get to do anything. You listen. And you pray. For what you've done to me.

FATHER: Who-

MICHAEL: Shut up. (A beat.) You don't even know who I am. Were there so many? You asshole. How many Hail Marys is it going to take to wipe away your sins? Now it's your turn. I want to hear it. Or I tell. Everyone. (Silence.) Now.

FATHER: What, my son?

MICHAEL: I am not your son. I never was your son. I want to hear your confession.

FATHER: I can't.

MICHAEL: Trust me.

FATHER: Only him.

MICHAEL: Where's your faith?

FATHER: My faith is in Jesus.

MICHAEL: Don't even try it.

FATHER: In the Lord Jesus Christ.

MICHAEL: Jesus Christ-

FATHER: In his divine mercy.

MICHAEL: Shut . . . up!

FATHER: I ask for his forgiveness.

MICHAEL: What about mine?

FATHER: Forgive me if I have sinned.

MICHAEL: "If." What kinda bullshit is that?

FATHER: If I have not seen-

MICHAEL: F*** you.

FATHER: Not followed-

MICHAEL: How could I have followed?

FATHER: For what I am about

MICHAEL: What are you about?

FATHER: To do.

MICHAEL: I was five years old. Do you remember? I was five years old.
```

---

## IC-0357: Falling Man

- Title: Falling Man
- Author (byline): Will Scheffer
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: March 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1272
- Already set (do not supply): none

### Source block (context only)

```text
Author: Will Scheffer
ISBN: 978-0822216681
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): March 1999
```

### Introduction (context only: never use it for content warnings)

```text
Nearly a quarter of a century has passed since reports of a voracious disease with an ability to destroy immune systems appeared in The New York Times. At the time, neither the disease, nor the agent that caused it, had names. Today they are known only too well: HIV causes AIDS. In the 1980s and 1990s, AIDS cut a devastating swath through the dance world, cutting short too many lives and careers. Falling Man by William Scheffer recounts one dancer’s experience as he reflects on the rise and fall of his dancing career and his life. Falling Man by William Scheffer
```

### Performance text (classify this)

```text
You get used to the sound of the wind as it rushes past your ears. And the ominous sense of velocity becomes familiar after a while. You watch as the stars whiz by you like flying candles. You listen to the planets as they sing their songs. You think to yourself, at any moment I am going to come crashing down into the Earth, but you never do. At least not yet.

You begin to wonder about gravity. You become obsessed with it. You say to yourself over and over: I'm falling I'm falling, but soon you get used to not having your feet on the ground anymore. In fact, ground itself, becomes a concept that no longer has any meaning to you.

You convince yourself that if you are talking, if someone can hear you, you must still be alive. You scream: I'm alive I'm alive, to no one in particular. You discover you don't like looking down, but prefer to look up, for obvious reasons. And then quite suddenly, for a moment, without warning: you have this unbearable urge to Cha Cha once more.

Before I started falling, I was a ballroom dancing champion, expert at ten dances. On a perfect night in 1983, at the age of 22, I became the Cha Cha champion of the world. No one much remembers that now, but it's true. Even before this however, I was famous for my Cha Cha. My dancing partner Svetlana defected from the Soviet Union in 1981, specifically to dance the Cha Cha with me. And, at that time, we were legendary. You would have loved Svetlana. She had an accent just like Norma Shearer in Idiots Delight. You know, all “vonderfuls” and “werys” . . . "I am so wery, wery crazy about you," she would often say to me. As I said before, we won the title of Cha Cha champion of the world on a perfect night in January of 1983. And we were perfect that night, as we moved across the dance floor of the Cincinnati Hilton Hotel. The floor was so highly polished that a few couples actually fell that evening. But not us. My strong arms that night; supported Svetlana in poses of inspired and delirious sexuality. Our footwork was impeccable and unrivaled. We glittered and sparkled and shined. Perhaps there could have been more of a natural passion between us, yes, but our acting was flawless and inspired. Not for a second was there a false move to our grace, to our speed and authority. And I now realize that in my life up until that moment there had never ever been even the remotest possibility of falling. It wasn't even a question. I would not have allowed it. I was not that kind of person. No.

That night we floated, we glided, we dazzled. And for a moment at the very climax of our passionate Cha Cha embrace, I was almost happy.

You must forgive me for talking so much. It's just that since I - started - falling - I don't dance anymore. I hope I’m not boring you. Really all I'd like to do is entertain you. You see, that’s what ballroom really is about, it's - entertainment and - it makes people feel good about life, about living, about being alive. Yes! That's what I'd really like to do more than anything else. "Oh I'd like to do a Cha Cha but the lesions hurt my feet!" Sorry. Bad joke. Anyway. That night, Svetlana and I celebrated in my hotel room. We drank champagne from her silver slipper, we got drunk, and I convinced her that we should make an appearance at the party in the hotel.

When we made our entrance the party was in full swing the waves seemed to part for us. Compliments flowed endlessly along with all the alcohol, but I felt uncomfortable that night with Svetlana on my arm. Sometimes it seems to me that Destiny has a way of making you ready for her arrival. Of creating the conditions necessary for her to play out her cards. Because I can't explain why I felt as I did on the night of my triumphant Cha Cha, that my young life until then had been nothing more than a championship performance a perfect ten absolutely, but just a performance none the less. And no sooner than I had this impression, I saw an enchanting stranger from across the room. He was not precisely a stranger, but I had never met him, as Pablo, a Brazilian dancer. You might find this hard to believe, but at the ripe age of 22, even in that day and time, I was still a virgin on that night in Cincinnati, in 1983. And as Pablo came closer my heart beat with a fear, but there was no turning back. Destiny had opened its arms wide to greet me and soon so had Pablo, who kissed me warmly on both cheeks with congratulations. This action on his part caused an uncontrollable "reaction" on my part so to speak.

I don't really know how to put into words what happened next. If I could I would dance it for you; I would dance that night and not trivialize it with words. Sometimes I think love is about inventing, a private language, a language that lovers makeup, that only they can speak and understand - isn't that what love is just an intoxicating language that you have forgotten and must now remember.

I wonder if you can understand what it felt like to me - please try because tonight I want us to be like lovers - but I wonder if you can, can know what it felt like for me to dance the Cha Cha with him. To dance with a man. For me, who had danced a thousand sambas, with a thousand lovely women, in a thousand sparkling rooms, for me to dance with a man for the first time in my life.

How can I explain it to you. How can I describe it as I fell. As I fell for the first time in my young life. As we fell into each other. As we danced.

You must forgive me for talking so much. I know it's silly but I am afraid that you will forget me and my Cha Cha. That you will judge me. That you will condemn me for falling that night. I want so much to entertain you, but you must understand, that night, it was as if I had to fall. As if a person like me had just been waiting to fall all his life. And it felt not so much as if I were falling, but more like I was being born, but of course you understand that don't you?

I’m afraid I’m running out of time. I'll just tell you this. Pablo died a year later. It was so fast, not long after that Svetlana took me to the clinic to get tested. And I've been falling ever since.

You know, sometimes I see the other falling people around me and I want to grab onto them as we fall. I want to dance with them up here in the sky. So everyone can look up and just see these fabulous falling people. I think that would be terrific, but it’s so hard to organize.

I have to stop talking. I do have one thing to ask you though. When I am finished remember that I used to dance the Cha Cha, that I was the Cha Cha champion of the world. And remember the sound of my voice
```

---

## IC-0358: Fences

- Title: Fences
- Author (byline): August Wilson
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Jan 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BONO, TROY, CORY, CROY
- Teaser before the introduction: Yes
- Spoken words (computed): 1948
- Already set (do not supply): none

### Source block (context only)

```text
Author: August Wilson
ISBN: 978-0573619052
Publisher: Samuel French, Inc.
Date (Month/Year): Jan 2000
```

### Introduction (context only: never use it for content warnings)

```text
According to Life Coach Elisabetta Franzoso: our ability to sustain satisfying and committed relationships, find gratification in our work, be effective parents, and our ability to speak up and assert ourselves are largely dependent on the relationship we have or had with our fathers. When that relationship is toxic, the cycle of damage is carried on from generation to generation.

In Fences by August Wilson, the sins of the father are visited upon the son. Troy Maxson’s damaging relationship with his father comes barreling down to impact the relationship Troy has with his own son.

Fences by August Wilson
```

### Performance text (classify this)

```text
BONO: (Pg 59) Some people build fences to keep people out . . . and other people build fences to keep people in . . .

TROY: (Pg 49-50) (to the audience – he has a bat in his hands and occasionally takes a swing at an imagined pitch) Sometime I wish I hadn’t known my daddy. He ain’t cared nothing about no kids. A kid to him wasn’t nothing. All he wanted was for you to learn how to walk so he could start you to working. When it come time for eating . . . he ate first. If there was anything left over, that’s what you got. Man would sit down and eat two chickens and give you the wing.

The only thing my daddy cared about was getting them bales of cotton in to Mr. Lubin. That’s the only thing that mattered to him. Sometimes I used to wonder why he was living. Wonder why the devil hadn’t come and got him. “Get them bales of cotton in to Mr. Lubin” and fine out he owe him money . . .

But I’ll say this for him . . . he felt a responsibility toward us. Maybe he ain’t treated us the way I felt he should have . . . but without that responsibility he could have walked off and left us . . . made his own way. (pause, considering) How he gonna leave with eleven kids? And where he gonna go? He aint knew how to do nothing but farm. No, he was trapped and I think he knew it. *******

TROY: (Pg 33) (calling) Cory! Get your butt out here, boy! (Cory (17) enters) You just now coming in here from leaving this morning?

CORY: Yeah, I had to go to football practice.

TROY: Yeah, what?

CROY: Yessir.

TROY: I ain’t but two seconds off you noway. The garbage sitting in there overflowing . . you ain’t done none of your chores . . . and you come in here talking about “Yeah” (pause) (Pg 37) Your mama tell me you done got recruited by a college football team? Is that right?

CORY: Yeah. Coach Zellman say the recruiter gonna be coming by to talk to you. Get you to sign the permission paper.

TROY: (Pg 36) Colored guy got to be twice as good before he get on the team. I don’t want you to get all tied up in them sports. (Pg 37) I thought you supposed to be working down there at the A&P. You suppose to keep up with your chores and hold that job down.

CORY: Mr. Stawicki say he gonna hold my job for me until after the football season. Starting next week I can work weekends.

TROY: You damn right you are! And ain’t no need for nobody coming around here to talk to me about signing nothing.

CORY: Hey, Pop . . . you can’t do that. He’s coming all the way from North Carolina.

TROY: I don’t care where he coming from. The white man ain’t gonna let you get nowhere with that football noway. You go on and work yourself up in that A&P or learn how to fix cars or build houses or something, get you a trade.

CORY: I get good grades, Pop. That’s why the recruiter wants to talk with you. You got to keep up your grades to get recruited. I’ll be going to college.

TROY: (Pg 38) You a bigger fool than I thought. Let somebody take away your job so you can play football. I’m the boss . . . you understand? (tense beat –gets in Cory’s face) I asked you . . . did you understand? (Cory is silent) You go on down there to that A& P and see if you can get your job back. You quit the football team. (turns and starts to walk away)

CORY: (pause) How come you ain’t never liked me?

TROY: Liked you? Who the hell say I got to like you? (pause) (Pg 39) You eat every day. Got a roof over your head. Got clothes on your back. Why you think that is?

CORY: Cause of you? (hesitant) Cause you like me?

TROY: Like you? You about the biggest fool I ever say. (pause) (Pg 40) Not cause I like you! Cause it’s my duty to take care of you. Let’s get this straight right here . . . I ain’t got to like you. Mr. Rand don’t give me my money come payday cause he likes me. He gives me cause he owe me. I done give you everything I had to give you. I gave you your life! And liking your ass wasn’t part of the bargain. Don’t go through life worrying about if somebody like you or not. You understand what I’m saying, boy? Get the hell out of my face, and get on down to that A&P. ******

TROY: (Pg 50-51) (to the audience – he has a bat in his hands and occasionally takes a swing at an imagined pitch) My daddy stayed right there with his family. But he was just as evil as he could be. My mama couldn’t stand him. Couldn’t stand that evilness. She run off when I was about eight. She sneaked off one night after he had gone to sleep. Told me she was coming back for me. I ain’t never seen her no more. All his women run off and left him. He wasn’t good for nobody. When my turn come to head out, I was fourteen and had us an old mule we called Greyboy. My daddy sent me out to do some plowing and I tied up Greyboy and went to fooling around with Joe Canewell’s daughter. She about thirteen and we done figured we was grown anyway . . . so we down there enjoying ourselves . . . ain’t thinking about nothing. We didn’t know Greyboy had got loose and wandered back to the house and my daddy was looking for me.

My daddy come up on us. Surprised us. He had them leather straps off the mule and commenced to whupping me like there was no tomorrow. I jumped up, mad and embarrassed. I was scared of my daddy.

******

CORY: (Pg 79) I ain’t scared of you! You don’t count around here no more.

TROY: I don’t count around here no more. All of a sudden you done got so grown that your daddy don’t count around here no more. (Pg 80) You gonna wear my pants? I done spent the last seventeen years worrying about what you got. Now it’s your turn, see? You grown. . . You a man. Now let’s see you act like one. (pushes Cory’s chest hard) Turn your behind around and walk out this yard. And when you get out there in the alley . . . you can forget about this house. See? Cause this is my house. ******

TROY: (Pg 51) (to the audience – he has a bat in his hands and occasionally takes a swing at an imagined pitch) When he commenced to whupping on me . . . I run to get out of the way (pause) I thought he was mad cause I ain’t done my work. But I see where he was chasing me off so he could have the gal for himself.

When I see what the matter of it was, I lost all fear of my daddy. Right there is where I become a man. . . at fourteen years of age. (Pause) Now it was my turn to run him off. (he beats the ground with the bat) I picked up them same reins that he had used on me and commenced to whupping on him. The gal jumped up and run off . . . and when my daddy turned to face me, I could see why the devil had never come to get him . . . cause he was the devil himself.

CORY: (Pg 38) (echoing in Troy’s mind) How come you ain’t never liked me?

TROY: (Pg 51) I don’t know what happened. When I woke up, I was laying right there by the creek. I thought I was blind. I couldn’t see nothing. Both my eyes were swollen shut. I layed there and cried. I didn’t know what I was gonna do. The only thing I knew was the time had come for me to leave my daddy’s house.

(Pg 52) I got up from the creek and walked on down to Mobile. I was through with farming. Figured I could do better in the city. So I walked the two hundred miles to Mobile. They ain’t had no cars and things like they go now. We talking about 1918.

(Pg 53) I walked on down to Mobile and hitched up with some of them fellows that was heading this way. Got up here and found out . . . not only couldn’t you get a job . . . you couldn’t find no place to live.

TROY: (Pg 37) (echoing his words to Cory) You suppose to keep up with your chores and hold that job down.

TROY: (Pg 53) I thought I was in freedom. Shhh. Colored folks living down there on the riverbanks in whatever kind of shelter they could find for themselves. Right down there under the Brady Street Bridge. Living in shacks made of sticks and tar paper. Went from bad to worse. Started stealing. First it was food. Then I figured, hell, if I steal money I can buy me some food. Buy me some shoes too! One thing led to another.

Went out one day looking for somebody to rob . . . that’s what I was, a robber. I’ll tell you the truth. I’m ashamed of it today. But it’s the truth. Went to rob this fellow . . . pulled out my knife . . . and he pulled out a gun. Shot me in the chest. It felt just like somebody had taken a hot branding iron and laid it on me. When he shot me I jumped at him with my knife. They told me I killed him and they put me in the penitentiary and locked me up for fifteen years. That’s where I learned to play baseball. (takes a swing)

(Pg 14) What [baseball] ever get me? Ain’t got a pot to piss in or a window to throw it out of. (softly) (Pg 15) If you could play ball then they ought to have let you play. Don’t care what color you were. If you could play . . . then they ought to have let you play. (echoing of words he had with Cory) (Pg 36) Colored guy got to be twice as good before he get on the team. I don’t want you to get all tied up in them sports.

*****

CORY: (Pg 55-56) (storms in, angry and confrontational) What you do that for, Pop? Went up to the school and told Coach Zellman I can’t play football no more. Told him to tell the recruiter not to come.

TROY: (threateningly) Yeah, I did it. And [you] know why I did it. (pause) Lied to me! Wanna play football . . . keep up [your] chores and hold down that job at the A& P. That was the conditions.

CORY: (Pg 80-81) You ain’t never done nothing but hold me back. Afraid I was gonna be better than you. All you ever did was try and make me scared of you. I used to tremble every time you called my name. Every time I heard your footsteps in the house. What’s Papa gonna say if I do this? . . . What’s he gonna say if I do that? What you gonna do . . . give me a whupping? You’re too old. You just an old man!

TROY: Get your ass out of my yard! (Cory grabs up Troy’s bat from where it always lays)

CORY: I ain’t going nowhere. I ain’t scared of you. (swings the bat at Troy who steps back, then advances) Come on! Come on!

TROY: (Pg 82) You wanna draw that bat back on me . . .you’re gonna have to use it (Cory swings the bat a second time and misses) You’re gonna have to kill me! (grabs the bat and the struggle. Ultimately Troy is stronger and takes the bat from Cory. Cory crouches in a protective position. Troy stands over him ready to swing. He stops himself) Go on and get away from my house. (Cory, stung by his defeat exits slowly)

(Troy walks about the yard. A quiet rage threatens to consume him. He tries desperately to calm himself. He clutches his heart, wipes sweat from his face and rubs his arm - He is clearly having a heart attack)

(Pg 72-73) All right Mr. Death. See now . . . I’m gonna take and build me a fence around this year. See? I’m gonna build me a fence around what belong to me. And then I want you to stay on the other side.

BONO: (Pg 59) Some people build fences to keep people out . . . and other people build fences to keep people in

TROY: (Pg 73) You ain’t gonna sneak up on me no more. Ain’t nobody else got nothing to do with this. This is between you and me. Man to man. You say on the other side of that fence until you ready for me. Then bring your army. Bring your sickle. When the top of your list say Troy Masxon (swings the bat feebly) Come on! Come on! I be ready for you . . . but I ain’t gonna be easy! (falls and the light and rage leave him)

CORY: (Pg 89) (rnters and finds his father dead on the ground; his bat still in his hands. He grieves silently for a moment then speaks slowly to the audience) The whole time I was growing up. . . Papa was like a shadow that followed you everywhere. It weighed on you and sunk into your flesh. It would wrap around you and lay there until you couldn’t tell which one was you anymore. Everywhere I looked, Troy Maxson was staring back at me. (reaches out to close Troy’s eyes) (Pg 90) I don’t want to be Troy Maxson . . . I want to be me.

NOTE: A video clip of a scene from this play showing 2 different characterizations for Troy Maxson (James Earl Jones vs Denzel Washington) can be found here: https://www.youtube.com/watch?v=jE2dDmMGfa4
```

---

## IC-0359: Drums, Girls and Dangerous Pie – “Fever”

- Title: Drums, Girls and Dangerous Pie – “Fever”
- Author (byline): Jordan Sonnenblick
- Work: Not specified
- Publisher: Scholastic Press
- Publication date as stated: Oct 2004
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2992
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jordan Sonnenblick
ISBN: 097610301X
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

OK. Mom, is this serious?

I don’t know honey. I don’t know. I wish I knew.

She must have thought the situation was pretty urgent, though, because she usually won't leave the house in sweats, and I noticed she hadn't even taken the time to put shoes on Jeffrey. Also, she's the careful driver in our family on most days, but our ride to the hospital was like the Indy 500. I didn't even have time to think of how in the world I was going to explain this away to my friends on Monday -I was mostly too busy trying to keep from passing out from the incredible G-forces every time we turned a corner. Somehow, Jeffrey didn't wake up, but he was definitely groaning in his sleep. I reached over and crammed his blanket between his head and the corner of his booster seat so he wouldn't get whipped around so much; my hand brushed against his forehead, and he was definitely ragingly hot.

The ER staff didn't mess around at all when we got there. As soon as my mom said the word "leukemia," there were doctors, nurses, and technicians swarming all over. The doctor in charge was barking orders like a Marine drill sergeant.

As they started to take Jeffrey's clothes off: he woke up. I guess he wasn't surprised to find himself in a hospital - both he and my mother seemed to have become used to this bizarre world. I couldn't even understand what the doctors and nurses were saying, but they were both clued in to this secret language. He didn't say anything as they took his temperature orally, even though he used to always make a big show of choking when my parents did it at home. He responded to all of the commands that came his way - Tilt your head! Take three deep breaths! Lean forward, -with mute obedience. Until they laid him down, and went for his chest with a needle. Now, I knew that something had been done to Jeffrey's chest in Philadelphia; I had seen the two lines of stitches, and the round bulge under the skin of his ribs. But during the whole period up until that night, the medical stuff had only sunk in to a point; I only accepted what I had to accept to make sense of any given moment. So I only really knew that he was taking steroids every day, for example, when I saw him gagging down the syringes of bitter liquid in the kitchen every morning and night. And I guess now was my moment to believe in the Port-a-Cath, which was an IV tube that had been surgically implanted under the skin a couple of inches above Jeffrey's right nipple.

Jeffrey pulled away from the doctor when he saw the needle, and asked in a little pathetic voice:

Can't we do the emm-lah?

I didn't know it then, but EMLA is a cream that makes your skin numb. They had been using EMLA so Jeffrey wouldn't feel the hurt of the needle as it stabbed through his skin to get at the catheter in his chest.

The doctor's voice softened then, and he almost whispered to Jeffrey:

I'm sorry, Buddy. The EMLA takes an hour to work, and we can't wait. Then the doctor half-turned to me, and asked Jeffrey: Would it help if your brother held your band?

Jeffrey didn't respond at all, but he looked at me, and his eyes were brimming. I am pretty squeamish about shots and blood and stuff, but what was I going to do? I grabbed his hand, and let him sort of lean his head on my shoulder without sitting up from his pillow. I started the "You're OK, Jeffy" chant, and a nurse scrubbed the circle of skin over the port with yellowish-orange stuff. Then she broke open one of those sterile packets that needles come in, and took out a truly large one, which was bent in the middle at a ninety-degree angle. Jeffrey started to whimper, and the tears began to soak the shoulder of my shirt, but he didn't even flinch as the huge needle jabbed straight into his chest. The nurse taped the needle in place, and I closed my eyes. I heard someone say, "Flushing the port," and then I got a little woozy. Jeffrey kept squeezing my hand really hard for a few minutes, until the blood specimens had all been taken and an IV line was hooked up to his port. I think we both fell asleep for a little while then. When I opened my eyes, the doctor was talking with my mom; neither of them noticed I was awake, so I just lay there and listened. Evidently, Jeffrey had what should have been a simple ear infection, but his white blood cell counts were low because of the chemotherapy drugs he was on, so his body couldn't fight off germs very well. The doctor was saying that Jeffrey would need to spend a few days in the hospital get-ting antibiotics through his IV line in addition to his regular chemo medicines. My mom didn't look pleased. Can we do it here, or does he -- He’ll be here until morning. We’ll put him on a pediatric floor for now, but we're going to have to transport him to a Children’s Hospital in Philadelphia and soon to get his fever down.

Transport him?

Yes, we can send him in an ambulance so we don’t have to stop the IV, or we can cap the line and have you drive him. I’ll consult with the specialist in the morning and see what he thinks is best. Oh, God. How costly is an ambulance? I don't know, but we have to do whatever’s best for your son medically right now.

I understand. It’s just, we’re in some financial trouble with all of this…

My mom started crying then.

I'm sorry Doctor, it’s just all this, all of a sudden, you know? We have very good insurance, but things add up. My husband isn’t…taking it well…

I hear you, Ma 'am. He sort of patted my mom on the shoulder at this point. I'll be back around in a few hours –we’ll move you all up to a private room any minute now, and then maybe you can try and get some rest.

Yeah, sure. My mom looked tired enough to sleep for a week, but I knew she wasn't going to get any rest.

I got out of Jeffrey's bed for the big move upstairs, and fell back asleep in a chair by the window of the new room. My mom spent a few hours lying on a cot they had brought in, but I really don't think you could say she slept. Every hour or so some medical person or another came in to take Jeffrey's temperature, or attach a new bag to his IV, or do something that would ruin our rest.

At 2 a.m., my mom walked out of the room. I wanted to know what was going on, so after a couple of minutes, I followed her. I found her sitting in the hallway, leaning back on the wall with her knees to her chest, holding a cup of coffee that must have come from the little coin-operated machine that was out there. 1 plopped down next to her.

Hey, Mom. How are ya?

I'm fine, Steven. I was really worried about your brother last night. But it looks like this is just what it’s going to be like…for a while.

Mom, how long is this going to last?

They're going to run some nests next week. If he’s cancer-free by then, he’ll still be in treatment for a few years. Then, who knows?

After five years without any, he should be totally normal.

Mom, what if he’s not cancer-free next week?

I don't know Steven. I just don’t know. By the way, I’m sorry that we ruined your night.

Mom, forget it. It was fine.

Oh, really? Fine, was it? Should I storm into your graduation wearing sweats too?

Yeah, that would be pretty cool. Maybe you could have your hair up in curlers for extra style points?

I might be able to do that Steven. How about some flip-flops on my feet?

Excellent, Mom. That would be excellent.

Right there in the hallway, I put my head in her lap. She stroked my hair for a while, and then she sent me back into the room:

Get some sleep, pal.

At about five in the morning, my dad came into the room and shook me awake (I guess my mom had gotten through to him by phone at some point). He put a finger over his lips so I wouldn't make noise and wake Jeffrey, but of course, right when I was about to tiptoe out of the room, a lady came crashing in with the giant breakfast cart. So we had this odd little family conference while Jeffrey attempted to choke down some food. My parents spent a few minutes looking at Jeffrey's hospital chart, worked out the details of what needed to be done if my mom and Jeffrey were going to Philadelphia for a week, and went out into the hall to argue about something. I had a little while alone with Jeffrey. He looked really exhausted, but his fever was gone, and he was much more alert mentally than he'd been the night before. He asked me about my dance:

Did you have fun? Did you dance a lot? Did Renee Albert kiss you? Did it feel gross?

Get out of here, you little nut-ball. I'm telling you, I have zero chance of kissing Renee Albert. Zero. Zilch. Nada.

So who DID you kiss?

Nobody. I was just standing around with my friends when you came to get me.

Did I ruin your night?

Mom asked me that, too. Jeffy, you didn't ruin my night. It was ruined from the start. You had a worse night than I did, anyway.

Oh, well. At least you didn’t have to kiss anybody.

Yes, Jeffy, that’s a big comfort to me. My parents came back in, and I started to get up and leave. Jeffrey asked me for a hug, and I gave him one.

Take care Jeffy, I’ll see you soon, right? Just remember not to throw food at the nurses. I don't want to get any complaint calls, OK?

Steven, I don’t throw food at…oh, it was a joke, right?

Yup, buddy boy. It was a joke. But seriously, no kissing the nurses on their lips, either. It messes up their makeup.

Eeeeeeewwwww!

It was about 7 a.m. when my Dad and I got home. I somehow made it to my bed, and collapsed into a near coma that lasted until I got too hungry to sleep through lunchtime. It was probably noon or so when I made it to the kitchen. My dad was sitting there, looking stubbly and worn-down, eating a bagel without much of an expression on his face. He gave me a tiny nod that was almost business-like -totally neutral, like he wasn't really seeing me. I got out cereal and milk, and it was so quiet between us that I was getting grossed out by the distinct sounds of our food-chewing processes. As soon as I finished, I went downstairs to play the drums. And play the drums. And play the drums. I played through all of the basic rudiments, and then did all of my lesson pages for the week. Then I put five CDs in the changer behind my drums, put on my headphones, pressed "SHUFFLE," and played along with at least ten really loud metal songs in a row without stopping.

I looked up in the middle of a Led Zeppelin drum solo, and my dad was sitting on the beat-up old couch about eight feet in front of my bass drum. Because he startled me pretty badly, and because I figured he was probably about 43% deaf if he had been sitting there a while, I jumped up and whipped off the headphones.

Uhhh . . . hi, Dad.

I just got the call from your mother. They're taking Jeffrey to Philadelphia in about two hours. She wants us to get his stuff together for him. Do you know what toys and clothed he likes? Can you help me?

My dad looked ashamed at this, like he had asked me to steal him a bottle of Jack Daniels or something.

Sure, Dad.

Hey, you're been down here playing for a while now. Are you all right?

I couldn't believe my father was just now noticing me, and that I might be upset about my brother's situation.

I'm fine, Dad. Oh, your mother thought you seemed upset at the emergency room, and when they put the tubes in . . .

Dad, they didn’t just put tubes in. They stabbed him in the chest. They STABBED him!

I was stunned by what happened next, although I had to admit it was becoming a pretty common occurrence: I started to cry. And once I started, I couldn't stop. My dad wasn't necessarily going to win the Teddy Bear Society's Father of the Year Award, but for the first time in weeks, he reacted. He put his arm around my shoulders, and sort of squeezed me in. We must have stayed like that for a good twenty minutes, until I couldn't postpone blowing my nose anymore. I picked my head up off of my dad, walked over to the other end of the sofa, got a tissue, and blew my nose. Then I sat right back down by him. We stared at each other without having any concept of what to do or say next. My dad finally broke the silence with an old family punch line: So, uhhh, how about those Knicks?

We chuckled awkwardly, but at least it was a chuckle. Then we went upstairs and packed up Jeffrey's stuff. On the drive over to the hospital, I had an odd realization: this was the first time in weeks that I had laughed with each member of my family within a 24-hour period.

At the hospital, Jeffrey was looking fairly worried. My mom was out in the hall, arguing with the doctors in Philly on her cell phone. My dad stayed to talk with her, and I went right to my brother.

Hey, Jeffy, how ya feelin?

I'm okay. We had oatmeal for breakfast but it wasn’t as good as yours. I’m scared.

What are you scared about?

Mommy said that they might have to do another bone marrow tomorrow. It was supposed to be next time, but now it’s tomorrow. The bone marrow HURTS. And I might still be very sick if they give it to me early. They said they would do it in a month, and all the bad stuff should be gone. But what if they aren't gone yet? Then they have to give me more throw-up medicine. It’s NO FAIR!

Jeffy, I'm sure the doctors know what they're doing. They wouldn't do the bone marrow this early unless they thought it would be OK.

But it might not be OK It might realty really not.

Well, buddy, you're in luck. Check out what I brought you. And with a flourish, I pulled his favorite Rescue Hero action figure out of his bag. Look! It’s Matt Medic. He’s here to protect you.

Matt Medic, I'm scared.

Don't he frightened, young man. He always loved it when I pretended to be one of his toys, and Matt Medic was perfect for the occasion. He carried a huge plastic paramedic pack and a giant gun-like thing that we always pretended was some kind of vaccine syringe.

But what if I'm still very sick?

Well, son, let’s concentrate on my Matt Medic Shot Shooter. It’s full of magic anti-hurt stuff - guaranteed to save your bone marrow. Here we go.

And I used Matt Medic to give Jeffrey a "shot."

That ought to do it. Just remember, you never have to worry when Matt Medic is on the watch. And one other thing: don't kiss the nurses. It gets them in trouble!

My parents came into the room then, and we had the whole obligatory hugs-and-farewells scene. It was fairly touching, all things considered. We said we'd be back together again soon, and that everything would be fine, and at that moment, everyone in the family was united toward the common goal of getting Jeffrey well.

The last thing I said to Jeffrey was: I'll see you in no time, pal. Just remember to listen to Matt Medic, and there will be no trouble! As things would turn out, though, there would be a lot more of both time and trouble before we were all in one room again.
```

---

## IC-0360: Fire Dance

- Title: Fire Dance
- Author (byline): Will Scheffer
- Work: Falling Man and Other Monologues
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: March 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CRYSTAL
- Teaser before the introduction: Yes
- Spoken words (computed): 1367
- Already set (do not supply): none

### Source block (context only)

```text
Author: Will Scheffer
Book: Falling Man and Other Monologues
ISBN: 978-0822216681
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): March 1999
```

### Introduction (context only: never use it for content warnings)

```text
Drag is a celebration. Drag is an attitude. Today’s drag queen is often a gay man who has embraced that part of himself that, as a child, was considered shameful and undeserving. Rather than allowing himself to be bullied, he has revealed that hidden aspect of himself, dressed her up, made her fabulous and invincible. He has found strength in her and wears her like a shield. Drag is some of the best parts of who he is, magnified and impervious. Today’s drag queen is at home in a gay bar, a pride parade or an AIDS charity event. Her audience is comprised of individuals who want to rejoice in difference, to celebrate a shared triumph over prejudice and misunderstanding, to find strength in community. So when Crystal’s mentor dies in a freak accident, she struggles to remain invincible . . . impervious. Fire Dance by Will Scheffer
```

### Performance text (classify this)

```text
An African-American man enters in a conservative business suit. He addresses the audience. He speaks very quickly. Throughout he changes from his male drag into her full and divine female drag -- makeup, pumps, wig and all. The transformation is efficient, rhythmic, and astonishing.

CRYSTAL: Before I went on Prozac . . . I used to be a very emotional person, hyper-sensitive you know, hysterical - and just forget about self-esteem. This used to make things hard for me, you know, like it would make it hard for me sometimes, to live in this world, to do the things that people need to do to - you know - live. For instance, like to go to the grocery store, or to mail a letter, you know, NORMAL things. I didn't even used to be able to go to the bank even, to stand on that line, to talk to the teller, it would get me - agitated. (He begins to remove suit.)

Now, I didn't think that this was always so bad of a thing though, at that particular time in my life - because what I was . . . was - what I was - I was a creative person, you know, a performer. Uh-huhhh! I used to do shows at The Anvil and The Mineshaft - you remember those places, yes? Perhaps then you have even heard of me - Crystal was my name, Crystal Chandaliah - (He waits for recognition.)

CRYSTAL: Yes, well - in my time, did I ever light up a stage - oh yes honey, I was electric. Fabulous. FLAMING! (Lights pop on at makeup table.)

You see, before I went on Prozac, I was the partner of The Amazing Nubia - now you MUST remember HER - She did the Fire Dance at The Anvil: the most famous act since Carmen Miranda, the Salem Witch Trials, and Cher all rolled into one.

Oh yes - Nubia taught me everything I know about show business, she was like a sister to me; and her and me, we were like the hottest sister act in town.

(Puts on his makeup robe.)

You COULD say that Nubia discovered me and you wouldn't be lying. She discovered me one night in 1975, lying on the floor of the bathroom, with my wrists slit open and my dress slashed to pieces. What a mess, darling - bleeding all over that linoleum! Now what Nubia DID - what she did was . . . this is what she did: she ripped off her gold lame sash, tied it around my arms and stopped off the bleeding! Next day I woke up in her cold-water apartment on Christopher Street, Donna Summers was singing on the radio, and Nubia fed me on rose hips tea. She called herself Miss Nurse ... and for two weeks she didn't get out of her stunning white nursing ensemble with matching white pumps. She saved my life! And she taught me how to Fire Dance. She said: "Honey, if you gotta burn - make 'em pay to see it." (Begins to put on makeup.)

Nubia was the mother of all drag queens. They don't make 'em like that anymore. She was the first queen to throw a bottle at the cops during the Stonewall Rebellion. Other queens invented the word, FIERCE, just to describe her. It has even been rumored that Nubia was the first homosexual ever to snap her fingers (She snaps.) and the phrase: "I will read your beads, Miss Mary Dugan!" has been attributed to her. (He does his eyes, rouge and cheekbones.)

Nubia taught me that to do the Fire Dance you gotta have a . . . VENEER, you know what I'm talking about? One day she says to me: "Honey - honey - you best be gettin' yourself some VENEER! else you gonna wind up on that bathroom floor again!" “VENEER?” I says to her. “VENEER,” she says, "like you know, like a . . . like a SHEEN, you see, 'cause let me tell you something, Miss Thing Girl: It ain't easy doin' the Fire Dance, bein' a drag queen, livin' the life. Uh-uh - No, darlin'." And Nubia was right. (Lipwork.)

It seems these days everybody and her mother wants to be a drag queen, how funny you know, when all I ever wanted was just to be a NORMAL person, like y'all. I mean sure it may LOOK glamorous, but it's an awful lot of work to make yourself over! I mean let all the other queens sing "I AM WHAT I AM," but drag queens we sing "I AM WHAT I AM NOT," you know what I'm sayin'?

(Powder and final touches.)

Uh-uh. Tsk tsk tsk: I even hear that Mr. Patrick Swayze is dressin' himself up for some big Hollywood type movie about drag queens - well I got some advice for you Mr. Patrick Swayze honey: You best be doin' some serious research, girlfriend! (Final lip outline - gets into stockings, breasts, dress.) Oh yes. Nubia taught me how to have a fierce veneer.

Sometimes we danced the Fire Dance five or six times a night. Twirling our fiery batons to Pearl Bailey's rendition of "Hot Voodoo," lip synching to Martha and the Vandella's cover of "Heatwave," glittering in our sequined dresses, our amazing black bodies shimmering under the virgin olive oil that we had so carefully applied before the show to protect us from the heat. But to tell you the truth, underneath my veneer - I still dreamed of a normal life - like married to some nice blonde Republican, like George Bush's nephew . . . a life in which I went to the bank without fear, in which I balanced my check-book, a life in which I cooked my man dinner and cleaned his kitchen, but Nubia said: "You're crazy girl! Don't even think such thoughts. That life ain't never gonna be for you. But you know, the real fact is, I loved Nubia. Not in a sexy way. But I really loved her. More than the guys from Greenpoint in the back seats of their white Continentals. The guys who I couldn't stop loving even though they used to beat me up after, more than them, more than myself even, I loved her.

And I loved the Fire Dance, the life of dancin' the Fire Dance with abandon, unafraid. (Lights shift.) – Sing portions of * Heatwave while performing with fire batons)

Then one night in the middle of a performance I looked on as suddenly, Nubia's amazing black body was consumed by flames. A freak accident. Her skin blazing like some highly flammable material, which no one could put out, no matter how we tried. Sometimes I see her face looking up at me, as it did at that moment, and I swear it was like she was almost smiling through the pain.

The crowd was going crazy around us, screaming and wailing, but I felt almost calm as I looked into Nubia's smiling face, as if she was saying to me what she had said a hundred thousand times to me before: "Crystal, if you do the Fire Dance, you gotta be prepared to burn." (Finishing touches on costume, boa, jewels.)

Next day I went to a Chemical Bank and I opened a checking account. I went to a Dr. Casey, a very nice man, who put me on Prozac. That was five years ago and I've never looked back. Today, I am a normal person. A happy person. I really, really am! I work as a word processor in a small law firm. I live with my boyfriend in New Jersey. He's a chemical engineer at Hoffman-La Roche Labs and he gets me my Prozac for free.

Nowadays my life is good! On Saturdays I shop at ShopRite. On Sundays I iron my shirt to get ready for work. And I balance my checkbook once a week!

(Wig, and then finished, a vision, she presents herself to the crowd.)

I don't dance the Fire Dance anymore. Sometimes when I go to the city, I'll run into one of the girls on the street, and they'll ask me if I don't miss performing. I tell then no, and it's true: I don't miss the Fire Dance. But sometimes late at night, around two in the morning, when my night shift's done and I can't sleep, I sneak into the bathroom. I close the door and I light many candles - (Lights candles, spotlight focuses on her.) - and I stare at my face in the mirror . . . And as I stare into the flames of the candles flickering around me I begin to sing, I sing in my own voice. I sing for Nubia, for all the girls, for myself I sing, this is what I tell us (Smoke blows around her as she sings a song like * Aretha Franklin's, "I Say a Little Prayer . . . " Lights fade.)
```
