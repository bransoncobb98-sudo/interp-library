# Classification request: batch 56 of 63 (40 records, IC-2201 to IC-2240)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-056-reply.json`.

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

## IC-2201: But Also Bring Cheese

- Title: But Also Bring Cheese
- Author (byline): Kate Tellers
- Work: The Moth Presents All These Wonders; Pgs 237-243
- Publisher: Crown/Archetype
- Publication date as stated: March 2017
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: KATE
- Teaser before the introduction: Yes
- Spoken words (computed): 1400
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kate Tellers
Book: The Moth Presents All These Wonders; Pgs 237-243
ISBN: 978-1101904404
Publisher: Crown/Archetype
Date (Month/Year): March 2017
```

### Introduction (context only: never use it for content warnings)

```text
Memories are precious. When you lose someone, the last thing you want is to lose memories of them too. See, we spend so much time talking about things that don't matter and so little time talking about things that really do. Death is inevitable and touches each of us but talking about it is complete taboo. This has to stop. Keep your loved ones alive in your conversations, your memories. Grief may numb your body and break your heart, but grief is also just another form of love. We grieve because we love . . . and that’s okay.

But Also Bring Cheese by Kate Tellers
```

### Performance text (classify this)

```text
KATE: (Pg 237-243) In our little house [in] Pittsburgh, we had one television. We kept it behind the couch, and I was never allowed to watch it. Most nights it was my mother, my father, me . . . maybe some wooden blocks. It was very Little House on the Prairie, but in the 1980s.

One day, though, I snuck across the street to my neighbor's house, and she let me watch The Love Boat. It blew my mind. I can just picture Gavin MacLeod dressed in a captain's uniform, making out with all of these beautiful women with perfect perms. I loved it.

When I came home, I asked my mother why they kissed in that crazy way. She was like, "Well, um, when people love each other, like, a whole lot, that is the way that they kiss."

So when she came in that night to put me to bed, I grabbed her head and I smashed it up against mine, and I moved my head back, and I said, 'I’m giving you Love Boat kisses." I was obsessed with my parents.

KATE: When our friends were getting pets, they would get a guinea pig and name it Punky Brewster. I got two goldfish, and I named them Paul and Lisa, after my parents, because they were my rock stars.

The rest of the world existed outside of our family, so much so that when my parents divorced, I didn't get angry. I was like, Oh, this is the next thing we're doing together. I wrote my college essay on how my parents' divorce made them my two best friends and took us on to our next adventure together. (I did get into college, though, despite that.)

The day before I was leaving for college, my mother and I were having lunch. She confessed to me that she had seen a doctor, and she was sick. And it wasn't a big deal, she was just going to have some chemo, and she would be fine.

And I really did, honestly, believe her. But I couldn't unhear that. And I felt like I suddenly had to start considering a world with this big hole where my mom should be.

We'd be spending time together, and it's like my brain would split. And part of me would be completely present, and the other half of me would be taking all of these notes, so I could sear all of these specifics about her into my brain in case I ever needed them when she wasn't there.

After college I moved to New York. Sometimes on Friday afternoons, I would drive to Pittsburgh and I'd get in really late. [My mom would] open the door, and she'd say, "Would you like a glass of wine?" I would say, "Yes." And we both knew that it wasn't [just] a glass of wine, because it never was. She laid out all these mismatched blue-and-white plates, with white cheeses.

One night we're sitting and we're talking, and she confessed to me that the hardest thing she ever had to do as a mother was to give me ipecac to induce vomiting, because when I was little, I accidentally ate a bunch of her asthma medicine. They were these little, red-coated pills, and she could see the red in my mouth.

And I confessed to her that actually I'd eaten Red Hots. It was the only candy in our house, ever. But I knew her reaction to me eating her asthma medicine would be better than her reaction to me eating refined sugar, so I let her just go with it.

So she's laughing about this, and she throws her head back. And my brain splits. And I start to take notes. I note the way that she laughs so big that I can see the fillings in the back of her mouth. And that her head is so small that she shops in the children's section at LensCrafters. I can tell because the candlelight catches the arm of her glasses, and they say "Harry Potter." This is my mom. She is the most elegant and gracious woman in the world. I pick up my glass, and I toast my mother, and I look -- and she's glowing. I take her in. And I think, This is good.

Four Januaries later I'm back in Pittsburgh. The doctors have told us that it's time to come home. I'm in my mother's bathroom. She's leaning on the sink. I see her look up and look at herself in the mirror. I see a change come over her face, and I can tell that she's made up her mind. She tells me to call a nurse.

I know that this is the day that I have been afraid of for ten years. And now we're calling everyone, and we're telling them, "Come over now, for what will probably be one of the worst nights of your life."

But because I'm my mother's daughter, I'm doing this as I'm pulling her plates off of the shelf and saying, "But also bring cheese."

And they do. I've put food out, and I'm filling people's glasses of wine. People start to go in to visit my mother. I hear her saying to them, as she's laid out in her bed, "Can I get you anything? Can I get you a cup of tea?" And I'm like, "You're dying. I am going to do this right now." So I start handing people saucers and empty cups. I'm like, "Just carry this in so she knows that we're okay out here."

When the hospice first came to visit us, they gave me this pamphlet, a little blue booklet called Gone From My Sight. There's a line drawing of a ship on it. And it explains in somewhat poetic but also somewhat technical terms what happens to a body when a human being is starting to die. And I remember when they gave it to me, I was sort of furious. I thought, “There's no line drawing that can describe this very personal and very massive event in my life. This is my mom.” But on this night, it's the only guide that we have. We've never done this before.

I go in to check on her, and she's standing at her closet, and she says, "I have to pack." And I don't know what to say to that. So finally, I say, "Mommy, where you're going, you don't need a suitcase."

And she lays back into her bed, and she goes silent. People continue to go in, and they start to say their good-byes. Finally, it's my turn. I go into her room, and I sit down on her bed.

I know that I should say I love her, and that I'll miss her. And that in twenty-eight years I can throw her the best eighty fifth-birthday party. Then, after that, maybe sometime we'll explode in one big fireball, so that neither of us would ever have to experience what it'd be like for one of us to have to live without the other . . . But she knows all of that. So I just tell her that the following November I'm going to be a bridesmaid in my friend Jess's wedding . . . so that she knows that I have plans.

And then that's it. My mother is gone.

We all gather in the living room, and we drink all of the wine, and we eat all of the cheese. Everyone leaves, and I go to bed.

The next morning I wake up. And it's the day that I've been afraid of. I go into the kitchen, and I open up the front of the coffee machine, and I realize that I still know how to make a pot of coffee. I go into the living room, and I sit in her big blue leather chair. I open my computer, and I check my e-mail. There's an e-mail from my friend Nick and he's asking me how I am.

I hit reply, and I type, "Nick, my mom died." And it's real. I wait for that big gut punch to hit me, for that big hole to open up. That emptiness. But instead, I feel the strangest thing, the purest thing I've ever felt. I just feel sad . . .

And it feels white. And it feels hot. And it envelops me. And I feel full.
```

---

## IC-2202: But the One on the Right

- Title: But the One on the Right
- Author (byline): Dorothy Parker
- Work: Complete Stories
- Publisher: Penguin
- Publication date as stated: 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1883
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dorothy Parker
Book: Complete Stories
ISBN: 978-0142437216
Publisher: Penguin
Date (Month/Year): 2003
```

### Introduction (context only: never use it for content warnings)

```text
As the social season descends upon us, tables the world over are being set to host that high-point of human interaction: the dinner party. Yes, it's time again to enjoy drinks, food and conversation with friends, family, colleagues and strangers - a seemingly harmless endeavor on the surface, but one that is capable of striking fear into the heart of hosts and guests alike.

Small talk usually takes place at a dinner party with a stranger you have just met. Small talk allows you to remain vague, if you so desire, and exchange simple questions and answers. Of course, it can lead to a more serious conversation, but small talk generally deals with innocuous subjects such as the weather, family, or the food being served. In other words, it is a wonderful way to acquaint yourself with someone else and allows you to decide whether you want to pursue the conversation with the stranger next to you or move on to someone or something else. But the One on the Right by Dorothy Parker
```

### Performance text (classify this)

```text
I knew it. I knew if I came to this dinner, I’d draw something like this baby on my left. They’ve been saving him up for me for weeks. Now, we’ve simply got to have him – his sister was so sweet to us in London; we can stick him next to Mrs. Parker – she talks enough for two. Oh, I should never have come, never. I’m here against my better judgment. Friday, at eight-thirty, Mrs. Parker vs. her better judgment, to a decision. That would be a good thing for them to cut on my tombstone: Wherever she went, including here, it was against her better judgment. This is a fine time of the evening to be thinking about tombstones. That’s the effect he’s had on me, already, and the soup hardly cold yet. I should have stayed at home for dinner. I could have had something on a tray. The head of John the Baptist, or something. Oh, I should not have come.

Well, the soup’s over, anyway. I’m that much nearer to my Eternal Home. Now the soup belongs to the ages, and I have said precisely four words to the gentleman on my left. I said, “Isn’t this soup delicious?”; that’s four words. And he said, “Yes, isn’t it?”; that’s three. He’s one up on me.

At any rate, we’re in perfect accord. We agree like lambs. We’ve been all through the soup together, and never a cross word between us. It seems rather a pity to let the subject drop, now we’ve found something on which we harmonize so admirably. I believe I’ll bring it up again; I’ll ask him if that wasn’t delicious soup. He says, “Yes, wasn’t it?” Look at that, will you; perfect command of his tenses.

Here comes the fish. Goody, goody, goody, we got fish. I wonder if he likes fish. Yes, he does; he says he likes fish. Ah, that’s nice. I love that in a man. Look, he’s talking! He’s chattering away like a veritable magpie! He’s asking me if I like fish. Now does he really want to know, or is it only a line? I’d better play it cagey. I’ll tell him, “Oh, pretty well.” Oh, I like fish pretty well; there’s a fascinating bit of autobiography for him to study over. Maybe he would rather wrestle with it alone. I’d better steal softly away, and leave him to his thoughts.

I might try my luck with what’s on my right. No, not a chance there. The woman on his other side has him cold. All I can see is his shoulder. It’s a nice shoulder, too; oh, it’s a nice, nice shoulder. All my life, I’ve been a fool for a nice shoulder. Very well, lady; you saw him first. Keep your Greek god, and I’ll go back to my Trojan horse.

Let’s see, where were we? Oh, we’d got to where he had confessed his likeing for fish. I wonder what else he likes. Does he like cucumbers? Yes, he does; he likes cucumbers. And potatoes? Yes, he likes potatoes, too. Why, he’s a regular old Nature-lover, that’s what he is. I would have to come out to dinner, and sit next to the Boy Thoreau. Wait, he’s saying something! Words are simply pouring out of him. He’s asking me if I’m fond of potatoes. No, I don’t like potatoes. There, I’ve done it! I’ve differed from him. It’s our first quarrel. He’s fallen into a moody silence. Silly boy, have I pricked your bubble? Do you think I am nothing but a painted doll with sawdust for a heart? Ah, don’t take it like that. Look, I have something to tell you that will bring back your faith. I do like cucumbers. Why, he’s better already. He speaks again. He says, yes, he likes them, too. Now we’ve got that all straightened out, thank heaven. We both like cucumbers. Only he likes them twice.

I’d better let him alone now, so he can get some food. He ought to try to get his strength back. He’s talked himself groggy.

I wish I had something to do. I hate to be a mere drone. People ought to let you know when they’re going to sit you next to a thing like this, so you could bring along some means of occupation. Dear Mrs. Parker, do come to us for dinner on Friday next, and don’t forget your drawn-work. I could have brought my top bureau drawer and tidied it up, here on my lap. I could have made great strides towards getting those photographs of the groups on the beach pasted up in the album. I wonder if my hostess would think it strange if I asked for a pack of cards. I wonder if there are any old copies of St. Nicholas lying about. I wonder if they wouldn’t like a little help out in the kitchen. I wonder if anybody would want me to run up to the corner and get a late paper.

I could do a little drinking, of course, all by myself. There’s always that. Oh, dear, oh, dear, oh, dear, there’s always that. But I don’t want to drink. I’ll get vin triste. I’m melancholy before I even start. I wonder what this stiff on my left would say, if I told him I was in a fair way to get vin triste. Oh, look at him, hoeing into his fish! What does he care whether I get vin triste or not? His soul can’t rise above food. Purely physical, that’s all he is. Digging his grave with his teeth, that’s what he’s doing. Yah, yah, ya-ah! Digging your grave with your teeth! Making a god of your stommick! Yah, yah, ya-ah!

He doesn’t care if I get vin triste. Nobody cares. Nobody gives a damn. And me so nice. All right, you baskets, I’ll drink myself to death, right in front of your eyes, and see how you’ll feel. Here I go . . . . Oh, my God, it’s Chablis. And of a year when the grapes failed, and they used Summer squash, instead. Fifteen dollars for all you can carry home on your shoulder. Oh, now, listen, where I come from, we feed this to the pigs. I think I’ll ask old Chatterbox on my left if this isn’t rotten wine.

That ought to open up a new school of dialectics for us. Oh, he says he really wouldn’t know – he never touches wine. Well, that fairly well ends that. I wonder how he’d like to step to hell, anyway. Yah, yah, ya-ah! Never touches wi-yine! Don’t know what you’re miss-sing! Yah, yah, ya-ah!

I’m not going to talk to him any more. I’m not going to spend the best years of my life thinking up pearls to scatter before him. I’m going to stick to my Chablis, rotten though it be. From now on, he can go his way, and I’ll go mine. I’m better than anybody at this table. Ah, but am I really? Have I, after all, half of what they have? Here I am lonely, unwanted, silent, and me with all my new clothes on. Oh, what would Louiseboulanger say if she saw her gold lame going unnoticed like this? It’s life, I suppose. Poor little things, we dress, and we plan, and we hope – and for what? What is life, anyway? A death sentence. The longest distance between two points. The bunch of hay that’s tied to the nose of the tired mule. The –

Well, well, well, here we are at the entrecote. Button up your entrecote, when the wind is free – no, I guess not. Now I’ll be damned if I ask old Loquacity if he likes meat. In the first place, his likes and dislikes are nothing to me, and in the second – well, look at him go after it! He must have been playing hard all afternoon; he’s Mother’s Hungry Boy, tonight. All right, let him worry it all he wants. As for me, I’m on a higher plane. I do not stoop to him. He’s less than the dust beneath my chariot wheel. Yah, yah, ya-ah! Less than the du-ust! Befor I’d be that way. Yah, yah, ya-ah!

I’m glad there’s red wine now. Even if it isn’t good, I’m glad. Red wine gives me courage. The Red Badge of Courage. I need courage. I’m in a thin way, here. Nobody knows what a filthy time I’m having. My precious evening, that can never come again, ruined, ruined, ruined, and all because of this Somewhat Different Monologist on my left. But he can’t lick me. The night is not yet dead, no, nor dying. You know, this really isn’t bad wine.

Now what do you suppose is going on with the Greek God on my right? Ah, no use. There’s still only the shoulder – the nice, nice shoulder. I wonder what the woman’s like, that’s got him. I can’t see her at all. I wonder if she’s beautiful. I wonder if she’s Greek, too. When Greek meets immovable body – you might be able to do something with that, if you only had the time. I’m not going to be spineless any longer. Don’t think for a minute, lady, that I’ve given up. He’s still using his knife and fork. While there’s hands above the table, there’s hope.

Really, I suppose out of obligation to my hostess, I ought to do something about saying a few words to his macaw on my left. What shall I try? Have you been reading anything good lately, do you go much to the play, have you ever been to the Riviera? I wonder if he would like to hear about my Summer on the Riviera; hell, no, that’s no good without lantern slides. I bet, though, if I started telling him about That One Night, he’d listen. I won’t tell him – it’s too good for him. Anybody that never touches wine can’t hear that. But the one on the right – he’d like that. He touches wine. Touches it, indeed! He just threw it for a formidable loss.

Oh, look, old Silver Tongue is off again! Why, he’s mad with his own perfume! He’s rattling away like lightning. He’s asking me if I salad. Yes, I do; what does he want to make of that? He’s telling me about salad through the ages. He says it’s so good for people. So help me God, if he gives me a talk on roughage, I’ll slap his face. Isn’t that my life, to sit here, all dressed up in my best, and listen to this thing talk about romaine? And all the time, right on my right - - - -

Well, I thought you were never going to turn around . . . You haven’t? . . . . You have? Oh, Lord, I’ve been having an awful time, too. . . Was she? . . . Well, you should have seen what I drew . . . Oh, I don’t see how we could . . . Yes, I know it’s terrible, but how can we get out of it? . . . Well . . . Well, yes, that’s true . . . Look, right after dinner, I’ll say I have this horrible headache, and you say you’re going to take me home in your car, and - - - -
```

---

## IC-2203: Carl and I

- Title: Carl and I
- Author (byline): Robert Olen Butler
- Work: Had a Good Time
- Publisher: Atlantic Monthly Press
- Publication date as stated: July 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1993
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Olen Butler
Book: Had a Good Time
ISBN: 978-0802117779
Publisher: Atlantic Monthly Press
Date (Month/Year): July 2004
```

### Introduction (context only: never use it for content warnings)

```text
Tuberculosis was one of the leading causes of death in the United States in the early twentieth century. There was no treatment . . . instead, those infected were isolated from society and placed in sanatoriums known as "waiting rooms for death."

What would you do if your spouse contracted the disease, was isolated from you for the rest of time and you were alone to await his unquestionable death? Would you make the same decision as our speaker?

Carl and I by Robert Olen Butler.
```

### Performance text (classify this)

```text
Dearest Sweetheart A line or two hoping they will find you all in good health . . . as for me I am getting worse. I don't think I will live long enough to see your dear face again.

Three nights after I married Carl Peterson, we watched Sarah Bernhardt die of consumption on a bed strewn with camellias. She was very beautiful, her face a sad white mask, her eyes enormous and dark, her voice rising from the stage and filling the Lyric Theatre. I grasped my Carl's arm on the seat next to me as she died, for he was the one man I had ever loved and now we were married, on the previous Saturday, December 16, 1905, and the church was filled with red camellias.

The newspapers said that Sarah Bernhardt slept in her own coffin, transporting it with her wherever she went, and she had died nearly twenty thousand times in her life, just as she was dying before us, and she took a cloth from her bosom as she lay on her deathbed, and she coughed terribly into it.

Now Carl has written to me from Attleboro that he is dying. He left for the sanitarium barely a month ago and he has lost hope. So quickly. The death is coming upon him very quickly.

He put the postcard in an envelope so the postal carrier would not share his words. Dearest Sweetheart, he said to me. I grew weak at this. And he tried hard to put his bravery down on the card, going quite formal for a moment. A line or two hoping they will find you all in good health, he said. All in good health. Completely in good health. As I seem, in fact, to be, which gives me no comfort. As for me, he said, I am getting worse. I don't think I will live long enough to see your dear face again.

He turned his face to me when we tucked the quilts around him in the backseat of the automobile that came to take him. He was as white as Sarah Bernhardt dying in the Lyric Theatre.

not. I have kept all the postcards Carl has sent to me. They are in a teakwood box. He wooed me with postcards. And he continued to write them even after we were married. He would be at work and I would come home from the library before him, and waiting in the mailbox would be a card from him. Oh, you sweetheart, he wrote. This was not so very long ago. His face was white and his eyes were terrible dark when he left for Attleboro.

I must write him now in return. He will not let me come to visit. He says I've been exposed long enough to the contagion, he could not bear for me to get sick. And he doesn't say it, but he's ashamed of how he's grown weak, how he's lost so much weight. He has always been a man to take off his coat and roll up his sleeves and have at some physical thing. My only recourse is a penny postcard that lies before me now in the center of the little flattop desk in our bedroom. I've chosen a card of a woman sitting with her hands clasped around a knee and her eyes are cast down and beneath her is the printed word heartbroken. I am, in fact, heartbroken. Carl will understand.

I look out the open window and across the yard to the sugar maple and to the laundry I'd hung this afternoon, the sheets and my nightgowns and underskirts and two of his dress shirts and I cannot look at his shirts. I'm finding more things I cannot look at in this house. The overstuffed armchair in our front room where he would read his newspaper of the evening. The porch swing. The cotton handkerchief near my feet. I wish I'd found it before I'd done the laundry. It was caught in the narrow dark space between the wall and his bed, near the headboard. It is folded tightly over the things he brought up from his lungs in his last days in our home. I can see the stains, the color of dried camellias. I found it an hour ago and dropped it at once and I washed my hands, as Carl would wish me to do.

I have filled my fountain pen. I turn the card over.

I look at it for a long time, its blank, divided back.

My mind is seizing idly on this and that. The ticking of the clock from the front room. The stirring of the maple tree. We first kissed under a vast maple tree, Carl and I. Decoration Day, 1904. We'd met in a late March snow that year. I came out of the general store and I had my shopping bag clutched to my chest. The air was unexpectedly full of snow and I was dazzled by this. I lifted my face as I stepped out and turned and I even closed my eyes to let the flakes fall on my eyelids and I ran into Carl Peterson, a great tall oak of a man whose arms went around me even before I had looked into his face. As soon as I was steady on my feet he withdrew and we looked into each other's face and he did not seem particularly handsome to me in those first moments. I am an overly critical sort, I think. It is my nature. His eyes were rather too close together and his face too round and too ruddy and though he was clearly a young man, he had deep-shadowed furrows across his brow above his nose and defining his cheeks from nose to lips. I would come to love these places on his face. Even when I had long prayed for that ruddiness to return, and when his face had begun to go gaunt, I would lie beside him and run my fingertip in these places and he would close his eyes and perhaps dream of how we met.

He suddenly bent forward and I took a step back, startled.

Then he rose up with the tinned milk that had fallen from my bag. "I make these," he said. "Well, so to speak," he said, lifting the can and considering it, his lower lip pushing up thoughtfully.

"I'd say cows made those."

"Well now, miss, do you think the cows run all the kettles and vacuum pans and heating chambers and cooling tanks to make this stuff pure and safe?"

"So the cows work for you?"

"And then there's the canning." He lifted the tinned milk high. "No cow can do a double seam on a tin can."

"All right, I'm prepared to give you credit. . . . You own the company, do you?"

He drew up to full height and he laid the can in the center of his chest. "Please," he said. "I'm a proud member of the working class, which does the real work. Neither cow nor tycoon can usurp our importance." He paused to let that sink in for a moment and I duly stood there looking up at him, agape. Then he winked at me and said, "I am a foreman, however."

And that was how we met, Carl Peterson and I. And we kissed under a maple tree up along a creek where we lingered, sitting on a log, and we talked, and there were daisies all around . . . and this was Decoration Day, 1904.

I slept in the yard last night in a reclining chair, my body swaddled like Carl's. I want to share this sanitarium life of his. Yesterday I ate raw eggs and milk and did exercises, moderately, morning and evening, and I lay in that chair under the sky all day long, trying to think of nothing, resting my body and mind, resting completely and activating my body's own defenses out in the fresh pure air.

On the day we found out for sure that our worst fears about his persistent cough, his afternoon flush, his weakness were true-this was still before the blood-on that day, Dr. Gilbert, sat behind his massive desk and his glasses hung round his neck on a cord and he told us straight out. "Mr. Peterson, you have tuberculosis of the lungs."

I was calm, at this. And, of course, Carl was calm. We had known for a while, though the words had never been spoken between us. Carl and I held hands before Dr. Gilbert, who was going on in a voice tainted with sarcasm, "These bacilli, though they may well exist, must necessarily fall on favorable soil, fertile soil, to grow and live. So we must build up the soil."

He had used the same metaphor-apparently the only one he knew-when he'd told me the year before that my ovaries were not properly formed and my womb was tilted. So I cannot have children? I said, not really a question. You have no fertile soil, he said. I imagine him bending over a man suffering a heart attack to say, Your heart lacks fertile soil for beating. He is a fool with his words.

I held Carl the night we discovered my barrenness and for several nights thereafter. I held him till morning, my arms around him as if to cradle him. We both shed tears, though with no sounds, no words about this turn of events. There would be no children for us.

Though so many die young, anyway. When yellow fever and cholera and smallpox aren't going around, there's always influenza and pneumonia and typhus and scarlet fever and measles and whooping cough and diphtheria, to name a few, and there is always a bit of poisoned meat or milk or something else that a child can eat and die from, and, of course, there is tuberculosis. Let us die then, Carl and I, but not a child. It's better for us not to have a child than to bear a child that will die young, is it not?

It is not. But I have no other consolation.

I rise up from my desk. The postcard is still blank, except for my husband's name and his final address in this world, the Attleboro Sanitarium. I cross the room and stand in the doorway from the bedroom to the living room. I wait for another thought. I wait for words to say to my husband.

We were so careful. He was always a careful consumptive, even at home, and I let him. I regret that. Standing now looking at our bed I understand that I should have kissed him more. I should have turned his face to me when he was coughing so terribly in the night and I should have taken his face in my hands and kissed him in that moment when he needed something no one could give. I should have kissed him on the lips.

I move to the desk now. I sit. I pick up my pen. I think to call him sweetheart. I think to say, My darling I love you and always will. I kiss your dear face, your darling lips. But I write none of this. These are foolish words. They have nothing to do with the life Carl and I now share.

And then I know what to say: We'll meet in death.

And I know what to do. I put the pen down and I push my chair back and I bend to the handkerchief on the floor. I hold it with my two hands, Carl's handkerchief, and I unfold it. I expose the remnants of his tortured breath and I lift it to my face. And I breathe in, deeply. I breathe into myself my husband's life, and I pray that I am fertile soil.
```

---

## IC-2204: Cat Got Your Tongue?

- Title: Cat Got Your Tongue?
- Author (byline): Sonya Sones
- Work: Sixteen: Stories About That Sweet and Bitter Birthday (Pg 120-168)
- Publisher: Broadway Books
- Publication date as stated: May 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2707
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sonya Sones
Book: Sixteen: Stories About That Sweet and Bitter
Birthday (Pg 120-168)
ISBN: 978-1400052707
Publisher: Broadway Books
Date (Month/Year): May 2004
* Cutting Compliments of Tracey Repa, Greater Chicago
Area, IL
```

### Introduction (context only: never use it for content warnings)

```text
The day we turn 16 is a magical day, full of good wishes and birthday cake. For Bria this is also the day for newfound love and a cat that might steal her heart before she has the chance to give it away.

Cat Got Your Tongue by Sonya Sones
```

### Performance text (classify this)

```text
*NOTE: written in poetry form but included in a prose anthology. Check the regulations for your tournament for the appropriate category in which to enter this selection.

It Feels Just Like I Dreamed It Would (Pg 120-168)

My skin misting all over, my T-shirt clinging to me, my breath coming in short, soft gasps,

my heart hip-hopping in my chest, my hands trembling and reaching out,

my fingertips buzzing as I take hold of it,
gripping it for the very first time,
slipping around it as if it were a trophy—
my very own driver’s license!

Everybody Sing!

Happy Birthday to me, Happy Birthday to me, Happy Birthday, dear Bria,

Happy Birthday
to deliriously happy, totally independent,
sixteen-year-old, licensed-driver
me!

Actually, My Real Name Isn’t Bria

It’s Umbria.
And just in case you’re wondering why
I have such a bizarre yet fabulously exotic name
it’s because my parents named me
after a region in Italy.

Which, supposedly,
is the very region in which I was conceived.
So, as you might well imagine,
every day I thank my lucky stars
that I wasn’t conceived
in Oxnard.

My Parents Told Me That It Happened in a Car

Not that I had even the eensy beensiest desire to know that.

Mom says maybe that’s why learning how to drive came so easily to me.

So That Means

That even if my big brother, Paris (can you guess where he was conceived?), wasn’t twenty-one years old,

it’d still be okay for me to be the one driving us up to Aunt Ginger’s place for my birthday luau

(her idea, not mine),

Levitating to My Luau in Paris’s Mustang

Shooting through the night
like an arrow on the wind,
we’re zooming past the orchards
with the top down.

Breezing down the road,
listening to rap,
my fingers have to tap,
have to dance to the music of the ride.

The car and I are one,

I could drive like this for hours,
I could drive us anywhere,
drive us right up past the moon
to the stars.

Both of Us See It

This bullet of fur,

this tiger-striped shadow, this smudge, this blur

that darts from the dark

We see it streak out. But it’s just

too sudden, too fast,

too—!

I Slam on the Brakes

Slam them so hard that wheels scream, rubber burns.

“Oh, no!” I gasp. “Did I hit it? I didn’t hit it. Did I?”

Paris doesn’t answer. He doesn’t need to.

I already know.

I know. But I don’t want to know.

And I sure don’t want to turn around and see it lying in the middle of the road. But I swivel in my seat and there it is—

a mangled mound of tiger-striped fur, one delicate paw extended out of the heap, as though caught in mid-swipe,

a small white moth fluttering above it in the blood red glow of the tail lights

as if trying to coax the little cat to life, trying to lure it back to the chase—

I rest my forehead n the steering wheel and cry.

I Guess Paris Must Feel Pretty Sorry for Me

Because he doesn’t even call me Dumbria.
He just reaches over and switches off the ignition,
silencing the CD and filling the night
with the sudden echoing choir of crickets.

He lets me cry it out for a few minutes. Then he hands me a Kleenex, tousles my hair, and says, “Geez, Bria.

I know you aren’t particularly fond of kitties, but don’t you think you’ve gone just a tad too far this time?”

Now I’m laughing instead of crying. And thinking to myself how much I love my brother.

But then that gets me thinking about the people who probably loved that cat.

And I break down all over again.

Paris Sighs

Then he puts his arm around me and says, That there wasn’t anything I could do.

“Believe me,” he says, totally deadpan. “Even if a good driver had been driving the car, the same thing would have happened.”

It takes me a second to realize that I’ve just been insulted. Then I start laughing again.

He says, “Well, we better get going or we’ll be late to your birthday luau.”

So I blow my nose one last time, switch on the ignition, shift into drive,

And flee from the scene of the crime.

Two Minutes Later

We pull up in front of Aunt Ginger’s house.
Paris commends me on my courage,
my fortitude,
and my parallel parking.

We head toward the front door,
but before we can even knock,
it sweeps open and Aunt Ginger yanks us inside,
hurling herself into our arms.

It’s like being hugged by an unusually friendly octopus who just happens to be wearing a hula skirt and one of those bras made out of coconuts. (Ouch! Ouch!)

“Aloha, my darlings!” she cries,
flinging a lei over each of our heads.
“I want you to meet Leon,
my fifth and final husband.”

Leon stops strumming his ukulele
and steps forward to pump both our hands.
He’s a Buddha-esque little man dressed only in a pareo,
with a belly as round as his gleaming bald head.

“Which one is the birthday girl?” he says with a grin.
This is apparently Leon’s subtle way
of letting us know that he’s noticed
the length of my brother’s hair.

“I am,” Paris says,
with a seductive bat of his eyelashes.
This totally cracks Leon up.
“You’re going to get along great with my son!” he says.
His son? No one said anything about a son.

Flynn Walks Through the Door

Suddenly I’m staring deep into a pair of swimming-pool-blue eyes,

these huge, dreamy, heavy-lidded miracles fringed with a forest of feathery black lashes.

I’m just
standing here
dumbstruck,
and my heart starts dancing the hula.

I’ve Read About This Sort of Thing Happening
This hokey love-at-first-sight thing,
this sparks-flying-fireworks-exploding-
ohmigod-I-think-I’m-about-to-melt-into-a-puddle-
right-here-and-now-
all-over-the-floor thing.

But I never thought it would ever happen to me.

Or That When It Did

It would be with a boy named Flynn.

I Let My Eyes Drift Down to Flynn’s Lips

“Hau’oli la hanau momona ‘umi kumaono,” he says. “Huh?” I say. “It’s Hawaiian for ‘Happy Birthday, sweet sixteen.’ I’ve been practicing.”

“Wow . . .” I say, temporarily stunned into monosyllables by the husky sound of his sexy voice. But a second later I manage to pull myself together and purr, “I love it when you talk Hawaiian to me.”

Then Paris says, “Hey, Flynn.
Can you teach me the Hawaiian words for
‘How about them Lakers?’”
And Flynn cracks up, as Leon herds us into the kitchen.

Aunt Ginger Tells Us She’s Been Secretly Yearning

To throw me a luau for my sixteenth birthday,

Then she slips on an apron and asks my brother to help her chop the onions and tomatoes for the lomi lomi salmon.

Leon opens the oven to check on the kalua pig. He asks Flynn to peel the sweet potatoes. I offer to set the table, and head out onto the patio.

Alone at last, under a full moon, with my fantasies of Flynn . . .

I’ll be setting out the plates when he’ll come up behind me and whisper in my ear, so near that I’ll feel the tingle of his breath on my skin.

“Do you need any help, Bria?” But I won’t answer. I’ll just lean back, pressing my body tightly to his.

He’ll wrap his arms around me, holding me so close that I’ll feel his heartbeat’s wild drumming.

Then he’ll start kissing my neck,
my shoulders,
my—
“Do you need any help, Bria?”
I whirl around—
Ohmigod!

It’s Flynn.

I Can Feel My Cheeks Flushing Hibiscus Pink

“Sure,” I say,

“How about if you put out the napkins,” I say,
trying my best to sound nonchalant,
“and I put out the plates?”
“Okay,” he says.

I begin circling the table, placing a dish in front of each chair.

Wherever I go,
Flynn goes, too,
gliding along next to me
as though we’re doing the tango.

He begins passing me
the little paper umbrellas for the glasses.
That’s when it happens—
his fingertips brush my wrist!

Suddenly, this quivery sort of shiver
flutters all through me
and Flynn takes a step closer,
his fingers finding mine, lacing us together.

“Hey, kids,” Paris calls.
He’s standing in the kitchen doorway smirking,
with his arms crossed over his chest,
one eyebrow raised.

“Can you give us a hand grating these coconuts?”

I Muddle Through the Next Half Hour

Avoiding eye contact, avoiding any contact with Flynn the Magnificent.

Because it’s entirely too weird to be falling for him While his father is watching, not to mention my aunt and my nosy big brother,

who for some strange reason has decided that his baby sister is off-limits to every boy on the entire planet.

When We Finally Head Out onto the Patio to Eat

Flynn practically breaks into a trot to grab the seat next to mine. This totally goose-bumps me.

We Share a Secret Smile That Lasts a Nanosecond

Then, Flynn slithers his hand into mine under the table, and a dizzying current of energy surges between us.

“So, Flynn,” Paris asks,
“were you in Maui with your father when he met Ginger?”
But Flynn doesn’t answer.
He doesn’t even appear to have heard the question.

That son of yours,” Aunt Ginger says fondly,
resting her head on Leon’s shoulder,
and smiling across the table at Flynn.
“He’s such a daydreamer.”

“What’s the matter, boy?” Leon asks gently.
“Cat got your tongue?”
“Hey, speaking of cats,” Aunt Ginger says,
“has anyone seen Bitsy?”

Did she just say “speaking of cats”?!
“Who . . .” I ask warily, “. . . is Bitsy?”
Aunt Ginger heaves a dreamy sigh and says,
“Only the most wonderful kitty on the face of this earth.”

“She really is terrific,” Leon says.
“I wonder where that little rapscallion could be.
It’s not like her to be late for supper.
She’s always home by eight . . .”

I check my watch— It’s 8:25!

My Heart Freezes in Mid-beat
Under the table, Paris grabs my other hand.
We sneak a quick peek at each other.
He’s obviously thinking what I’m thinking.
I squeeze his hand in panic.
Paris knocks back the rest of his Mai Tai in a single gulp.

“I hope that dear little cat hasn’t gotten herself
into any trouble . . .” Aunt Ginger says.
And a line creases her forehead.
“Don’t you worry, doll,” Leon says.
“I’m sure our Bitsy’s just fine.”

“She better be,” Flynn says,
finally emerging from his love trance.
“I’ve gotten way attached to the Bitster.
I can’t wait for her to get home
so you can see her, Bria.”

“Me neither,” I barely manage to croak.
As Aunt Ginger’s eyes start misting over.
“You know,” she says, “if it weren’t for Bitsy,
I never would have even met Leon.”

Then she tells us this long story about how she was taking a walk on Hamoa Beach in Maui, and she was feeling so sorry for herself,

because there she was, all alone in this tropical paradise, letting this fabulously deserted beach go to waste,

when she heard this tiny mew coming from behind her.

So she turned around and there was this scruffy kitten, following right along after her.

“She could easily fit into a single one of my footprints,” Aunt Ginger says. “She was such an itsy-bitsy little thing.”

“Hence . . . the name?” Paris asks, with a visible lurch of his Adam’s apple. “Exactly,” Aunt Ginger says,

not seeming to notice his oddly strangled tone of voice.

There’s a Question Burning in My Throat

A question that has to do
with whether or not
a certain little wonder cat is tiger-striped.
But I’m way too scared to ask it.

“I figured she was lost,” Aunt Ginger continues.
“So I picked her up and started knocking
on all the doors of the houses nearby
to try and find her owner.”

“When Flynn and I answered our door,” Leon says,
“there was this absolutely gorgeous woman
standing there,
holding this scrawny little feline in her arms.”

Well, apparently,
one thing led to another,
and the three of them spent the rest of the day together,
searching to no avail for the kitten’s owner.

But before the moon rose that night,
Leon was in love with Aunt Ginger.
And they all were in love
with Bitsy.

“Which Was Totally Strange for Dad and Me,” Flynn Says

“Because both of us had always been allergic to cats.
“But Dad and I decided that we’d rather spend
the rest of our lives on antihistamines
than have to give up the Bitsinator.”

And Flynn
squeezes my left hand,
while Paris
squeezes my right one.

My Stomach’s Doing the Jitterbug

then, Paris (says) “What does the Bitserino look like, anyway?”

“Yeah,” I say hopefully. “What color is she? Gray? Calico?”

“Nope,” Flynn says, pulling out his wallet, like a proud father, to show me her picture.

She’s a cute little tiger-striped thing.”

No!

Suddenly I’m choking on my lau lau. Or is that my heart that’s stuck in my throat? Paris and Flynn start slapping me on my back.

“Dang hairballs,” Paris says. And everyone laughs. Even Paris and me.

But anyone who took a close look at either one of us would be able to see the ohmigod!!! in our eyes.

Flynn Reaches for My Hand Again

Let’s take a walk to see if we can find Bitsy, okay?”

Find Bitsy?! Oh, man . . .

“Sure,” I gulp, as Flynn takes my hand and yanks me out the front door,

before Paris even sees where we went.

I Try

To steer Flynn in the opposite direction from the scene of the crime.

But he says that Bitsy sometimes visits
the cat that lives at the apple farm
a few blocks down the road,
so we ought to check there first.

Now it’s just the full moon dappling the lawns, the echoing of the cricket choir, and Flynn’s long, warm fingers entwined with mine, as we stroll together through the summer night lit with stars and fireflies and possibilities . . .

The only problem is that every step we’re taking is leading us closer and closer still

to a certain heap of roadkill.

“Here, Bitsy, Bitsy, Bitsy . . .”

Flynn’s calling softly to her, in that husky voice of his—

that voice that practically makes me swoon.

One block . . . Two blocks . . .

Now Flynn’s telling me stories about his life. Funny ones.

Stories that make me like him even more than I already did.

The sound of his laugh, the feel of his hand, those lips, those lashes . . .

“Here, Bitsy . . . Here, Bitster, Bitster, Bitster . . .”

Three blocks . . . Four blocks . . .

But I Can See It in the Distance Now

I can just make it out at the far end of the block— the lump that’s lying in the middle of the road! The poor little kitty that I snuffed out . . .

Then, without warning, Flynn slows to a stop and pulls me around to face him.

But I keep my eyes trained on the ground. Because if I look up into his, I know what will happen.

And I can’t let that happen. Can I? Can I?

He Takes a Step Closer to Me

And brushes his lips against my forehead. “Flynn,” I whisper. “Yeah?” he whispers back.

“There’s something I have to tell you.”

“What is it, Bria?” he asks. “Is there someone else?” “No,” I say, closing my eyes tight.

“It’s nothing like that . . . It’s . . . it’s about your . . . your . . .”

Suddenly, something brushes against my ankle. I leap back and then I see it—

it’s something furry, something soft, something tiger-striped!

“Bitsy!”

Flynn cries, “Where have you been?” scooping her up and burying his face in her fur. “We’ve been looking all over for you.”

“Bitsy . . . ?!” I gasp.

“But . . . but I thought . . . Ohmigod! Bitsy! It’s you!”

“Mew,” Bitsy says matter-of-factly, gazing at me with her big yellow eyes.

I lean in to rub my cheek against the softest fur in the universe and then I find Flynn’s lips

and kiss him!
```

---

## IC-2205: Caught up in the Rapture

- Title: Caught up in the Rapture
- Author (byline): Sheneska Jackson
- Work: Not specified
- Publisher: Simon and Schuster
- Publication date as stated: June 1996
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 839
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sheneska Jackson
ISBN: 978-0684831534
Publisher: Simon and Schuster
Date (Month/Year): June 1996
```

### Introduction (context only: never use it for content warnings)

```text
Jazmine Deems wants to reach for the stars, gain success and have a music career that is elusive to other people who only dream. Jazmine can do more than dream, however . . . she can SING! Her father, a Baptist preacher, feels if she goes after a career in music she will end up like her mother – alcoholic, irresponsible and gone. Her father wants her to stay in college, get a “real” career, and pray for her very soul. Neither dream is unreasonable . . . but for Jazmine – the dream to sing supersedes the wishes of her father. Sometime you just have to let yourself get Caught up in the Rapture by Sheneska Jackson
```

### Performance text (classify this)

```text
I’m just about sick and tired of all this sneaking around like I’m some two-year old child. I mean, look at me. I’m twenty-six years old and still breaking out in a cold sweat because I’m afraid Daddy won’t let me go out tonight. He’ll probably break out into tone of his holy chants. “Oh, Lord, save this child. Make her see the error of her evil ways!” By the time he’s finished, I’ll feel so guilty that’ I’ll get dressed in one of my little white dresses and follow right behind him to the Holy Sight Baptist Church. Or at least that’s what usually happens, but not tonight. Tonight I’ve got big plans and nothing, not the good Reverend Deems, not even the Almighty Himself is going to stop me. Today Dakota called me up at work and said she had two tickets to Black Tie Records’ annual executive party. If I could just get my tape into the hands of somebody, anybody, at that company, I’d be set.

Okay now, let’s see. I’ve got my hot curlers, my makeup kit, and my good panties: “demon material.” My best friend Dakota says I’m weak when it comes to daddy, but she just doesn’t understand. I envy Dakota, I really do. Dakota’s parents were musicians. They treated the two of us to a concert. I told Daddy we were going to see a young gospel group. He was glad that I was “becoming closer to the Lord.” I got to my seat, the house lights went off, and the crowd could barely contain themselves. I lady behind me began shouting, “Go on girl, sang that song.” Then the man next to her stood up and started hollering too, “Sang it, baby, sang it!” And the it happened. Anita Baker walked into the spotlight, standing less than five foot free, but seeming larger than life. I was in awe. At that moment, I knew what I wanted to do. I wanted to sing. I wanted to get onstage in front of thousands of people and touch them deep down in their souls the way Anita touched me. I wanted to make people yearn, make their hearts bleed, move them, make them feel. That was eight year ago. (to God) I’m still waiting for my dreams to come true, just in case you were wondering! But get this, I got a phone call the day after the executive party.

“I’m Bobby strong of Black Tie Records, and I’d like to meet with you this afternoon to discuss your future here at Black Tie. I have an opening in my schedule at four o’ clock, and by the way, your friend Colorado was right, your voice is impeccable! Don’t thank me. Thank your friend Colorado.”

I wanted to tell him her name was Dakota, but HELL, he could call her Alaska if he wanted to! I quickly got dressed, but before I got out the door, Daddy stood in the doorway glaring at me.

“I just got back from church and Miss Ola told me her son Oliver saw you at a party last night. Girl, you ought to be shamed.”

“Just stop it, Daddy. All I did was go out to a little party. What is it? Do you think I’m going to go out one night and never come back? Do you think I’m momma? I’m not momma!”

“Jazmine, who do you think you’re talking to? Jazmine, don’t you dare walk out that door, girl!”

I kept right on walking. At that moment I felt like the force of God was within me, but that couldn’t be possible, because the way I had just spoken to Daddy, I knew God wouldn’t want to be with me right now. I got to Black Tie Records, and Bobby said, “Now Jazmine, I just want to hear your voice. Give us a little somethin’, somethin’.”

Okay Mr. Strong

Ah, ah, ah, ah, ah, ah, caught up in the rapture of love…

When I finally opened my eyes:

(bobby) “Jazmine, it’s only a matter of time before that voice lands you on the Billboards.”

I did it. I had finally made my dreams come true, and you know what? I did it all by myself. That night, by the time I reached the steps, Daddy had opened the door and looked out.

“Come fix you a plate.”

I fixed myself a place and sat at the table.

(father) “You any good?”

“Yeah.”

“Better than your momma?”

“Yeah.” I knew we weren’t talking about voice quality or music arrangement. We were comparing lifestyles. I’m smart enough to know that drugs can’t make me any more artistic than I already am. I’m smarter than Billie Holiday, smarter than Janice Joplin, and yeas, smarter than Momma. Daddy lifted my hands to his face and kissed my palms. I felt close to him that I ever had before. You see, at that moment, my father wasn’t the Great Reverend Deems, healer of lost souls; he was finally just my Daddy.
```

---

## IC-2206: Center Stage

- Title: Center Stage
- Author (byline): Jane Denitz Smith
- Work: Chicken Soup for the Teenage Soul III, Pgs 305-310
- Publisher: Health Communications Inc
- Publication date as stated: April 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: JANE, SARA, JOE
- Teaser before the introduction: Yes
- Spoken words (computed): 1231
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Denitz Smith
Book: Chicken Soup for the Teenage Soul III,
Pgs 305-310
ISBN: 978-1558747616
Publisher: Health Communications Inc
Date (Month/Year): April 2000
```

### Introduction (context only: never use it for content warnings)

```text
From the quiet doctor whose advice we rely on to the charisma of an inspiring speaker, self-confident people have qualities everyone admires. Self-confidence is important in almost every aspect of our lives, yet many people struggle to find it -- spiraling into a vicious cycle that keeps them from becoming successful.

In this selection, a high school student finds that the encouragement and support of a peer helps introduce her to an inner self she didn’t know existed.

Center Stage by Jane Denitz Smith
```

### Performance text (classify this)

```text
JANE: (Pg 305-310) Once upon a time, my life was as orderly as the inside of my locker. I took detailed notes, never talked out of turn, helped put away library books during my free periods, and went to track practice after school. But all that changed the day Mr. Soames made Sara McGee my partner in biology.

SARA: (whispering) If he thinks I’m touching this, he’s dreaming!

JANE: [that’s what Sara said] after Mr. Soames told us to make the first incision into the earthworms we were dissecting. She pushed her bangs – they were orange today as opposed to last week’s green – out of her face and frowned. I took the knife from her hand and split the earthworm neatly down its center.

SARA: Thanks. (rolling up her sleeves) I know I’m a baby, but cutting open animals makes me sick.

JANE: I finished dissecting the worm, and when the period was over, Sara slipped her backpack over her shoulder and asked me to eat lunch with her. (to Sara, surprised) Okay. (to audience) I followed her to her locker, where she opened a tube of tomato-red lipstick and thickly applied it.

SARA: (applying lipstick) Want some? Just a tiny bit?

JANE: And before I could stop her, she dabbed it on. Then she removed the tortoise-shell barrette I always wore and lifted my hair into a high ponytail, pulling two tendrils down on either side of my ears.

SARA: Stunning!

JANE: [she was] standing behind me so that I could see both of us in the little mirror that hung from a hook. Stunning? I wasn’t so sure.

Soon, whenever Sara chewed Juicy Fruit gum in class, I did, too, even though I was careful not to get caught. I wore long skirts like Sara’s, and dangle earrings. She hid in the stacks during study hall and read old magazines and, consequently, so did I. She took me to Papa Jimmy’s and introduced me to double caffe lattes and biscotti dipped in chocolate. She like to start arguments in world history class about personal freedom and even though I never could do that, I did find myself, miraculously, volunteering to read out loud in Mr. Bernard’s English class.

It was Mr. Bernard, in fact, who pulled me aside and told me I had a flair for drama (we were reading Romeo and Juliet). He also said I should try out for the part of Laura in the junior class production of The Glass Menagerie.

I told Sara as soon as we left the room. (to Sara) No way. I could never do that! (to audience) Secretly, though, I was pleased he had asked.

SARA: Of course you can! You’ll be great! You have to try out!

JANE: She bugged me until I finally agreed. At the audition, I read a scene with Joe Greenlaw, who I’d never said a word to before. I doubt he knew who I was, but I could recite his activities as if they were listed in alphabetical order under his picture in the yearbook: junior class vice-president; photo editor for the Park Ridge Banner; captain, debate team; soccer goalie.

After we finished, Mrs. Layton, the director, just smiled and said, “Thank you very much,” and the next day the casting list was posted on the bulletin board and there was my name, second from the top, with Joe Greenlaw’s just above it.

I had play rehearsal almost every night, and so I had to use all my free time to catch up on my schoolwork and hardly ever had time to go to Papa Jimmy’s with Sara. Slowly, though, a strange thing began to happen. Homework and chores, babysitting, and even Sara started to fade in importance, but the time I spent at rehearsals was as vivid as the glow-in-the-dark stars on my bedroom ceiling.

Joe talked to me, calling me “Laura” from way down the hall. This made me so happy that I didn’t even mind when I saw Rachel Thompson, who had waist-long hair that was shiny as glass, put her arm across his shoulder. One night, during dress rehearsal week, we were standing together on the fire escape outside the auditorium watching the snowflakes gather on the iron railing. Joe told me that deep down inside he was really shy and that he was glad he could be himself with me.

JOE: Maybe we should do things together. Go running, go to a dance, I don’t know.

JANE: And then we heard Mrs. Layton calling for us, so we ran back inside. The next day, Sara stood by my locker just before homeroom.

SARA: Hi. (tugging on her earring) I never see you anymore. Except in classes, and that doesn’t count.”

JANE: I know, it’s the play. I’m really busy. It’ll be over soon. (to audience) I looked closely at Sara, past her makeup, and her jewelry, and the long black cape that covered her shirt and her thick, black hiking boots. She always seemed so bold, the way she stated her opinions as if they were facts, and looked anybody in the eye. But now she was quiet, more like the old me than Sara. I gave her a hug.

SARA: Let’s do something . . .

JANE: She looked at the poster on the bulletin board just behind us. It was a drawing of a flapper girl twirling a strand of pearls.

SARA: Let’s get a bunch of people together and crash the Winter Carnival dance. We’ll go to the thrift shop and get some beaded dresses!

JANE: A dance. I thought of Joe and of our conversation the night before. And even though I knew, deep down, that it would be a white lie to say he’d invited me to that particular dance, I told her I was busy. (to Sara) I can’t . . . Joe Greenlaw asked me.

SARA: Yeah, right.

JANE: I’m sorry. He did. (to audience) Sara picked up her backpack from between her feet and started to walk away. I called after her. . . Sara!

SARA: (bitterly) Let me know when you can fit me into your busy schedule. (long beat)

JANE: This is the part of my story that is really embarrassing – the part that I wish I could tell in third person, as if it really belonged to somebody else.(pause) A week after the play was over Joe found me during sixth-period study hall.

JOE: I’m sorry.

JANE: I looked at him, not understanding

JOE: Sara McGee asked me if it was true we were going to the dance together. (pause) I’m sorry. I’m going with Rachel.

JANE: I looked down at my feet. The new me was going away, like a picture on a computer screen that fades out. I was sure my ears were bright red.

JOE: I’m sorry. It’s nothing personal . . .

JANE: He turned and looked like he was leaving, but then he came back. He put his hand on my arm.

JOE: Don’t be embarrassed. You know, I should have asked you. I wish I had.

JANE: And then he left. (long beat) Now Sara passes me in the hall without speaking. I spend most of my free time studying or practicing my sprints. I went back to wearing my plain, comfortable clothes and threw away my makeup. And I only talked when teachers called on me.

As if nothing had changed.

But that wouldn’t be true. To Sara, I might have looked the same. Still, deep inside, where she couldn’t see, there was another me. I was brave, I was fun. I got a standing ovation in the middle of a stage, and a boy regretted not asking me to a dance. And it was Sara I had to thank for introducing that girl to me.
```

---

## IC-2207: A Child’s Book of Sickness and Death

- Title: A Child’s Book of Sickness and Death
- Author (byline): Chris Adrian
- Work: A Better Angel: Stories
- Publisher: Farrar, Straus and Giroux
- Publication date as stated: Aug 2008
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: CINDY
- Teaser before the introduction: Yes
- Spoken words (computed): 1202
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chris Adrian
Book: A Better Angel: Stories
ISBN: 978-0374289904
Publisher: Farrar, Straus and Giroux
Date (Month/Year): Aug 2008
```

### Introduction (context only: never use it for content warnings)

```text
According to the University of Michigan, a chronic illness is “a long-lasting condition that can be controlled but not cured. Examples in children include diabetes, cancer, organ failure, and for the two children in this story, short-gut syndrome. For these children, hospitals become a second home and the doctors and nurses who care for them, a second family.

Cindy faces sickness and death on a regular basis; but she’s developed a way of coping. She’s become an author of her own book . . .

A Child’s Book of Sickness and Death by Chris Adrian
```

### Performance text (classify this)

```text
CINDY: (Pg 177) Ella Thims sits in her little red wagon by the clerk’s desk. Ella had some trouble finishing up her nether parts, and was born without a colon, or most of her small intestine, and her kidneys are shaped like spirals. She’s only two. I’ve known her all her life. (Beat) (Pg 196) Ella Thims died in the PICU, killed, it was discovered, by too much potassium in her sauce. A newly graduated nurse meticulously verified the poisonous contents of the solution and delivered them without comment. It put her heart in that bad rhythm they couldn’t get her out of, though they worked over her till dawn. She’d been at it for a while before she was discovered, so it was already too late when they put her on the bypass machine. It made her dead alive - her blood was moving in her, but by midmorning of the next day she was rotting inside.

CINDY: (Pg 172) My room, 616, is always waiting for me when I get back, unless it is the dead of winter, rotavirus season, when the floor is crowded with gray-faced toddlers rocketing down the halls. They are only transiently ill, and not distinguished. You earn something in a lifetime of hospitalizations that the rotavirus babies, the RSV wheezers, the accidental ingestions, the rare tonsillectomy, that these sub-sub-sickees could never touch. The least of it is the sign that the nurses have hung above my door, silver glitter on red poster board: Chez Cindy.

(Pg 174) [You see] I am a former twenty-six week miracle preemie. When I was born you were pretty much dead if you emerged at twenty-six weeks. I did well except for a belly infection that took about a foot of my gut -- nothing a big person would miss but it was a lot to me. So I’ve got difficult bowels. I don’t absorb well, and get this horrible pain, and barf like mad, and need tube feeds, and beyond that I sometimes have to go on the sauce, [that’s] TPN - total parenteral nutrition - where they skip my wimpy little gut and feed me through my veins. (Pg 196) (softly) Ella Thims died by too much potassium in her sauce.

(Pg 174) I am waiting for my PICC- you must have central access to go back on the sauce- when a Child Life person comes rapping at my door. You can always tell when it’s them because they knock so politely, and because they call out so politely: “May I come in? (Pg 175) We are collaborating with the children. A collaboration of poetry and prose!”

I want to say, people like you wear me out, honey. If you don’t go away soon I know my heart will stop beating from weariness, but I let her go on. When she asks if I will make a submission to their hospital literary magazine I say, “Sure!” I won’t, though. I am working on my own project, a child’s book of sickness and death, and cannot spare thoughts or words for [Margaret]. (as if she’s been asked a question) (Pg 178) My book? The cat and the bunny and the peacock and the pony, each delightful creature afflicted with a uniquely horrible disease. (as if the audience has responded negatively) There’s a book -- Everybody Poops. Why not one that’s just about sickness and death? Everybody poops. Everybody suffers. Everybody dies.

(Pg 173-174) (She reads from her manuscript) See the cat? The cat has feline leukemic indecisiveness. He is losing his fur, and his cheeks are hurting him terribly, and he bleeds from out of his nose and his ears. His eyes are bad. He can hardly see you. Suffer, cat, suffer!

(Pg 172) (to the audience) If you are the sort of child who only comes into the hospital once every ten years, then the whole world comes to visit, and your room is filled with flowers and chocolates and aluminum balloons.

(Pg 177) See the pony? She has dreadful hoof dismay. She gets a terrible pain every time she tries to walk, and yet she is very restless, and can hardly stand to sit still. Late at night her hooves whisper at her as cruelly as anyone who ever hated her. She hardly knows how she feels about them anymore, her hooves, because they hurt her so much, yet they are still so very pretty - her best feature, everyone say s- and biting them very hard is the only thing that makes her feel any better at all. Suffer, pony, suffer!

(Pg 172) (a soft echo of thought as she turns the page) After the tenth or fifteenth admission, the people and the flowers stop coming.

(Pg 182) See the zebra? She has atrocious pancreas, oh! Her belly hurts her terribly - sometimes it’s like frogs are crawling in her belly, and sometimes it’s like snakes are biting her inside just below her belly button, and sometimes it’s a pain she can’t even describe. Suffer, zebra, suffer!

(Pg 172) (a soft echo of thought as she turns the page) My room, 616, is always waiting for me when I get back.

(Pg 186-187) See the peacock? He has crispy lung surprise. He has got an aching in his chest, and every time he tries to say something nice to someone, he only coughs. His breath stinks so much it makes everyone run away, and he tries to run away from it himself, but of course no matter where he goes, he can still smell it. Sometimes he holds his breath, just to escape it, until he passes out, but he always wakes up, even when he would rather not. He only feels ashamed now when he spreads out his feathers. Suffer, peacock, suffer!

(Pg 172) (a soft echo of thought as she turns the page) Gray-faced toddlers rocketing down the halls

(Pg 192-193) See the bunny? She has high colonic ruin, a very fancy disease. Only bunnies from the very best families get it, but when she cries bloody tears and the terrible spiders come crawling out of her bottom, she would rather be poo., When her pillow feeds her dreams of happy bunnies playing in the snow, she only feels jealous and sad, and she bites her tongue while she sleeps, and bleeds all night. In the morning a servant drives her to the Potty Club, where she sits with other wealthy bunny girls on a row of crystal toilets. They are supposed to be her friends, but she doesn’t like them at all. Suffer, bunny, suffer!

(Pg 196) (a soft echo of thought as she turns the page) Ella Thims died in the PICU

See the cat? He has died. Feline leukemic indecisiveness is always terminal. Now he just lies there. You can pick him up. Go ahead. He will be smellier in the morning, but no more alive. Maybe he is in a better place, maybe his illness could not follow him where he went, or maybe everything is the same, the same pain in a different place. Maybe there is nothing at all, where he is. Goodbye, cat, goodbye!

(Pg 198) All the sadness of the past twenty-four hours ought to count for something, ought to change something, inside of me, or outside in the world. But I expect that nothing will change - children have died here before, and hapless idiots have come and gone, and always the next day the sick still come to languish and be poked, and they will lie in bed hoping, not for healing, but for something to make them feel better, just for a little while. I think of my animals and hear them all, not just the cat but the whole bloated menagerie, crying and crying, make it stop.
```

---

## IC-2208: Choosing Hope

- Title: Choosing Hope
- Author (byline): Kaitlin Roig-Debellis and Robin Fisher
- Work: Not specified
- Publisher: GP Putnam's Sons
- Publication date as stated: Oct 2015
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: KAITLIN, CHILDREN, LITTLE GIRL, CHILD 1, CHILD 2, CHILD 4, CHILD 5, CHILD 6, CHILD 7, CHILD 8, VOICE 1, CHILD 9, VOICE 2
- Teaser before the introduction: Yes
- Spoken words (computed): 2189
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kaitlin Roig-DeBellis
ISBN: 978-0399174452
Publisher: GP Putnam's Sons
Date (Month/Year): Oct 2015
```

### Introduction (context only: never use it for content warnings)

```text
Kaitlin Roig-Debellis wanted to be a teacher from a young age, and relished working with children ever since she was allowed to babysit. After seven years as a first-grade teacher, her life changed dramatically. Choosing Hope is her story . . . assisted by Robin Gaby Fisher.
```

### Performance text (classify this)

```text
KAITLIN: (Pg 81) The morning sun rising over Long Island Sound on December 14 was even more breathtaking than usual. My step had a skip as I pushed out the door and walked to my car to head to school. Could life get any better? I was twenty-nine years old, engaged to the man of my dreams, and working in a job I would have done for free, I loved it so much. (Pg 1-3) I live every day wishing I could go back to December 13, 2012. Back to who I was, who my kids were, back to our school and the life I would never in a million years have changed. The Sandy Hook Elementary School massacre was the worst mass murder of schoolchildren in the United States since the Bath School bombing in 1927. Six of my colleagues and twenty first-graders -- six and seven-year-olds who were still learning to tell time, and count to 120, and spell 100 words – were murdered that morning.

KAITLIN: (Pg 82-94) It was 7:45. I parked my car in the teachers' lot, reached for my pile of books and papers, and proceeded to the school's main entrance, through the double doors, past the main office, and across the hall to my classroom. Dropping my books on my desk, I went right to work. Our reading specialist was coming to observe my class and I wanted to make sure everything was ready for her visit. I was so busy that I hadn't even taken the time to greet a group of my coworkers as they walked back and forth between the main office and a nearby conference room where a meeting was being held. By the time the buses arrived and my students filed into our classroom, a few minutes before nine, I felt ready for the day. (to students) Good morning, Fantastic Friends!

CHILDREN: Good morning, Miss Roig!

KAITLIN: After attendance, my students settled in to do their morning work until I played the song to signal morning meeting. (sing) “Oh, what a beautiful morning! Oh, what a beautiful day. (return to narration) They gathered around my chair, excited to get started. I picked up a pile of cards, each one with a different greeting written on it, and fanned them out the way a magician does a deck of playing cards before a magic trick. The cards said things like jHola! and Bonjour and High Five! One student picked a card from the deck, and whatever was written on it was the day's greeting. That morning, the card chosen was Ball Roll, a special card and one of the kids' favorites, which meant they got to roll a ball to one another as they said their good mornings. The student seated next to me was always excited about being able to greet the teacher. That morning, it was the little girl with cascades of brown curly hair who always wore pink.

LITTLE GIRL: Good morning, Miss Roig.

KAITLIN: I loved that moment. You can't help but be happy after looking into the eager eyes of a sweet, smiling first-grader. After that, we moved on to sharing time. Because the Christmas season and Hanukkah were upon us, the theme that day was "Our Holiday Traditions." One of my students, a rambunctious boy with chestnut-- colored eyes and foot-long lashes, smart as a whip, had been chattering about Christmas since September, and now it was just eleven days away. He was wild with anticipation. He told the story of his cousins coming to spend the holidays, squealing as he spoke. The others talked about making cookies, and visiting Santa, and listening for reindeer, and lighting the menorah, and visits with family members and friends. (to students) Let's get excited about today! You're going to shine! (to audience) It was 9:30, fifteen minutes before the "big test" . . . but we never got that far.

First comes the initial blast of gunfire, then the sound of shattering glass. The hair on my arms stands up. I know right away what I am hearing. Columbine is happening in the place we called Pleasantville. How can it be? Someone with a weapon is shooting their way into our perfect school. My classroom is the first one in the building. We are in grave danger -- sitting targets. I jump up, run to the door, pull it closed, and switch off the lights. I can't lock the door. My keys are clear across the room, on top of my desk and a locked door is no match for a magazine of bullets. If we're going to live, we have to find a hiding place. Fast. I look around the classroom. The windows don't open wide enough for a first-grader to climb through, and who knows what or who is waiting outside? Evil is coming for us and there's nowhere to go.

Where can we hide? Where can we hide? There's only one place. The bathroom-a tiny, tiny first grade-sized lavatory with only a toilet and a toilet-paper dispenser inside. Its dimensions are about the size of two first-grade desks pushed together. Maybe three feet by four feet. There is so little space that the sink is on the outside, in the classroom. I have never even been inside the bathroom before. An adult wouldn't fit comfortably. How in God's name will I get sixteen of us in there? It is our only chance. The impossible will have to become possible. (to students) Into the bathroom! Now!

CHILD 1: In there? How?

CHILD 2: Why?

KAITLIN: (to students) Bathroom! Now! (to audience) They understand that the teacher means business. I rush them toward the back of the classroom. Shots are being fired outside our classroom door. There's no time. "Hurry!" I say, pushing them into the tiny space. ."Hurry!" But I know that no matter how quickly my students respond, it will still take two or three minutes to get everyone inside, minutes I feel sure we don't have.

We all push into the bathroom, and when there isn't a millimeter of space left, I begin lifting my students and piling them inside. I place one student, then two, then three on top of the toilet and hoist up my littlest girl and sit her on the toilet-paper dispenser. We are all crushed together with not even enough room left to take a deep breath. I reach out to pull the door closed. My heart pounds against my chest, but I cannot afford to lose my composure, not if we are to have any chance of getting out of this alive. First-graders model their teacher's be-havior. If I panic, they'll all panic, and we'll be dead. (to students) Now, we have to be absolutely quiet. We can't say a word.

Someone shouts, "Shooter! Stay put!" Then, ear-splitting, rapid-fire shots, like a machine gun -- di-di-di-di-di-di-di-di-di-di-di-di -- over and over and over. My students stay perfectly quiet. They understand that someone very bad is searching for us. In our silence, we hear voices -- muffled voices. People are pleading for their lives. "No! Please, no! Please! No!" With the inescapable sounds of carnage happening all around us, my little ones are feeling desperate.

CHILD 4: (whispering) What is happening?"

KAITLIN: My fashionista begins to cry. I cup her face in my hands and look into her teary eyes. (to student) We're going to be okay. (to audience) The boy who straddles the top of the toilet is shaking so hard that he accidently flushes. Once, then again. We all hold our breath. Shhhhhhhhhh!!!!! Did the shooter hear? I look at the boy and his face says it all. I'm scared and I'm sorry and I don't know what to do.

CHILD 5: (whispering) Miss Roig, I don't want to die today.

CHILD 6: (fighting tears) I just want my mom.

CHILD 7: (whispering) I don't want to die before Christmas.

CHILD 8: (whispering) I'll lead the way! I know karate.

KAITLIN: (to audience) Hadn't it been only moments ago that he told us the story of finding a dollar under his pillow for his two front teeth? (to students, gently) No. There are bad guys out there and we need to wait for the good guys to come. It's going to be okay. We're going to be okay . . . I need you to know that I love you all very much. (to audience) In comforting them, I also brought comfort to myself. (to students) Anyone who believes in the power of prayer needs to pray right now.

(close eyes and pray) Suggested “prayer” – Not in the original text. You may insert your own prayer here if desired or simply pray in silence for a few beats. Check the rules governing your tournament regarding addition of “transition/additional” words.

KAITLIN: [(softly) God, we are scared. But You are there. Even when we don’t know what to say, we can just pray, “Help me, God, I’m so scared.” Thank You for this day, even though it’s not been the best day. Help us. Help us to see and remember all of the good things You have blessed our lives with. In Jesus’ Name, Amen.]

It’s been quiet for a while now. Eerily quiet. I wonder if the gunman is lurking outside our door, waiting for us to feel safe enough to come out of the bathroom and fall into his trap. If the good guys were coming, they would have been here by now, wouldn't they? Why is it so deathly quiet? I think about my students' parents and the unimaginable grief they will suffer because I was powerless to save their children. My worst fear is that I will see my class murdered before I die and I won't be able to stop it. All we can do now is wait. . . An eternity passes. Some of my kids are becoming impatient.

Several say they need to go to the bathroom. For the most part, though, they are quite content to be quiet if it means the bad guy can't find us. I wonder what is happening outside. Then, from the other side of the wall, come the voices of people who are barking orders. I hear them clearly.

VOICE 1: Don't look up. Don’t open your eyes. Walk Quickly.

KAITLIN: Oh, God. Is there more than one shooter? Are they kidnapping people? What is going to happen to us? My heart races in my chest. My kids look up at me. (to students) Shhhhhhhh. (to audience) We have been in the bathroom for a very long time. At least forty-five minutes.

A knock comes at the door and we all stiffen with fear.

(put index finger to lips as a signal to the children) I fear that if we make any noise, the shooter will realize that the teacher has hidden her whole class in here. (to student in a whisper) Ask who's there. (to audience) I don't want the shooter to know that there are sixteen terrified people huddled together behind the bathroom door.

CHILD 9: (voice quivering) Who is it?"

VOICE 2: (a kind voice) Hey, little fella. We're here to help you. Unlock the door.

KAITLIN: No way! Why in the world would I trust the words of a faceless stranger? No way am I going to risk opening the door for a killer. (to the person outside the door) If you really are the police, I need your badge. (to audience) Seconds pass. A badge is slipped under the door. I pick it up and examine it. I desperately want for it to be real, but I'm not convinced. (to person outside the door) This doesn't look real. I don't believe you. (to audience) I look around at my kids and I know they are thinking what· I am. Please let this be the good guys. One little girl is choking back tears. I take her face in my hands and smile. If she starts to cry, the others will cry. I can't let that happen, not until I find out who is on the other side of the door. (to person outside the door) If you are the police and you're here to help us, then you should have the key to this door. Or you should be able to get it. (to audience) A few more minutes pass before I hear the rattle of keys. I hear the scraping sound of a key going into the lock. It doesn't work. Another key, another failed attempt. Five. . . six . . . seven tries. My stomach churns with each twist of the lock. My students' eyes are wide.

The tenth key works. The knob turns and the door pushes in. I see an army of uniforms-people dressed in black and wearing helmets and carrying big guns, peering in at us. A SWAT team is in our classroom. The good guys are here. They pull us out of the bathroom, at first, one by one, until there is enough room for us to move on our own. Our heroes lead us out of the classroom and guide us in the op-posite direction of the bodies in the hallway and the blood-stained floor. I grab the hands of the two students closest to me and follow the instructions to "Go. Fast." We rush the students down the hall and out of the building. "Where is the bad guy?" I ask as we make our way to the firehouse. Is he still lurking here, somewhere, ready to hurt us? They assure me that we are safe. I say "Thank you" over and over . . . Thank you for finding us in that tiny bathroom . . . Thank you for being the good guys . . . Thank you for saving our lives.
```

---

## IC-2209: Coat of Many Colors

- Title: Coat of Many Colors
- Author (byline): Dolly Parton
- Work: A 6th Bowl of Chicken Soup for the Soul, Pgs 318-321
- Publisher: Health Communications, Inc.
- Publication date as stated: Jan 1999
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1065
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dolly Parton
Book: A 6th Bowl of Chicken Soup for the Soul,
Pgs 318-321
ISBN: 978-1558746626
Publisher: Health Communications, Inc.
Date (Month/Year): Jan 1999
```

### Introduction (context only: never use it for content warnings)

```text
Dolly Parton is truly a legend -- one of the most prestigious entertainers in the world; but her childhood was far from the bright lights of Nashville. Her father was a struggling tobacco farmer who never learned to read or write; and her mother, a preacher’s daughter from South Carolina, poured her heart and soul into raising the family’s 12 children. Imagine raising a family in a one-room cabin with no electricity or indoor plumbing.

She jokes that her family was so poor “the ants used to bring back food they’d taken from us because they felt sorry for us.”

Dolly’s mother didn’t know it, but the day she took a box of rags and sewed them into a patchwork coat for her daughter was a moment in time that became one of Dolly’s treasured memories and the inspiration behind one of her most beloved songs.

Coat of Many Colors by Dolly Parton
```

### Performance text (classify this)

```text
(Pg 318-321) Mama began to make me a coat. A lot of times when she made something out of patchwork, she would try to find scraps that matched as close as possible so that it wouldn’t be so obvious. But she knew me and my personality, so she decided to make my coat out of the brightest, most different colors she could find. This was going to be a colorful coat with no apologies.

It’s a lot of work to tailor a coat for a child and line it all by hand, even if you cut it all out of one piece of cloth. You can imagine how much work it took to make one out of little pieces. I knew she was making it for me, so I watched her almost the entire time. She told me the story from the Bible about Joseph and the coat of many colors. Joseph’s coat was given to him as a sign that he was loved and special and I felt the same way about mine. I watched how she folded every edge of every little piece under and sewed it with close stitches so that there wouldn’t be any ragged seams. When there are so many kids in a family, you can imagine how a mother’s time has to be divided up among them. So to see my mother spending this much time to do something just for me was special indeed.

As soon as it started to look anything like a coat, I would beg her to let me put it on, and I would strut in front of the fire in it like some kind of patchwork peacock. I could tell the other kids were getting jealous, probably not so much of the coat as of the attention I was getting from Mama. I started to understand how Joseph’s brothers got so jealous of him that they put him down a well and sold him into slavery. Aside from [my brother] Denver, I don’t know if any of the other kids would have actually sold me into slavery; but I could easily be in for a few spiteful pinches or hair pullings. I didn’t care. After all, it was me they were being jealous of – me and my beautiful coat. And it was beautiful.

I remember the night Mama finished it. I wore it around the house until she made me take it off and everybody got sick of telling me (with my none-too-subtle prodding) how beautiful it was. That night, I almost never got to sleep. It was worse than Christmas Eve. I couldn’t wait to wear my coat to school the next day. It wasn’t really cold enough for a coat yet, but Mama let me wear it anyway. She could see it was no use trying to dissuade me, so off I went down the path, lickety-split. It’s the only time in my life I have ever been anxious to get to school.

I burst through the school doors like a multi-colored whirlwind, wondering just how many people I could find to admire my coat. I was so proud of it. I wanted to be seen in it. I wanted to be noticed. ‘See my new coat?’ I said to one boy. ‘New,’ he sneered, ‘it looks like a bunch of rags.’ My heart sank a little, but he was just one boy. Surely the others would see how wonderful and special my coat was. My heart sank further as other children poked fun at me and my coat. Soon it turned into a whole room full of mocking faces; laughing, pointing, jeering at me . . . me and my coat. I wanted to tell them the story Mama had told about Joseph and make them understand how special, how singular, how beautiful . . . but they would not hear it.

My heart was broken. I couldn’t understand the cruelty, the ignorance that made them laugh at me that way. The teacher came in and noticed I was being picked on, so she tried to help. ‘Don’t you want to put your coat in the cloakroom?’ she suggested, but I would not. They would not shake my pride in my coat, my love for my mother, my faith in myself. I would not have it. I would sit there and be hot and wait them out. I would wait until school was over and walk proudly from the building wearing my coat like a banner of pride. I would walk with my head high into the autumn afternoon and show my coat to God. He would know how special it was, how special I was. He did. He liked the way it complemented his evergreens and the rich brown earth of the path. He watched carefully to catch glimpses of it from his side of the clouds as I marched proudly home. He loved the way it looked on his Dolly Parton.

As painful as it was, that experience at school that day was a great blessing to me. It was what inspired me years later to write the song that has become my signature piece. ‘Coat of Many Colors’ is still my favorite song that I ever wrote or sang. It was also a big hit, and that did a lot to help me forget that early pain. [It goes like this. . .]

(May be spoken or sung)

Back through the years
I go wonderin' once again
Back to the seasons of my youth
I recall a box of rags that someone gave us
And how my momma put the rags to use
There were rags of many colors
Every piece was small
And I didn't have a coat
And it was way down in the fall
Momma sewed the rags together
Sewin' every piece with love
She made my coat of many colors
That I was so proud of

As she sewed, she told a story From the bible, she had read About a coat of many colors Joseph wore and then she said Perhaps this coat will bring you Good luck and happiness And I just couldn't wait to wear it And momma blessed it with a kiss

My coat of many colors
That my momma made for me
Made only from rags
But I wore it so proudly
Although we had no money
I was rich as I could be
In my coat of many colors
My momma made for me
```

---

## IC-2210: The Color of Scars

- Title: The Color of Scars
- Author (byline): Florri McMillan
- Work: American Fiction: The Best Unpublished Short Stories by Emerging Writers
- Publisher: Carol Publishing Corporation
- Publication date as stated: July 1990
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: DOCTOR, CONNIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1812
- Already set (do not supply): none

### Source block (context only)

```text
Author: Florri McMillan
Book: American Fiction: The Best Unpublished Short
Stories by Emerging Writers
ISBN: 978-1559720298
Publisher: Carol Publishing Corporation
Date (Month/Year): July 1990
```

### Introduction (context only: never use it for content warnings)

```text
A stroke can happen to anyone at any time. Blood flow to an area of the brain is cut off; brain cells are deprived of oxygen and begin to die. Each year nearly 800,000 people experience a stroke of some type. In this selection, Connie is one of those people. At the age of 34, she has experienced a stroke strong enough to damage the part of her brain that controls language. This condition is called aphasia – Connie is trapped within her own mind, with the ability to form coherent thoughts, but with no means to express them to those around her. This is The Color of Scars by Florrie McMillan.
```

### Performance text (classify this)

```text
NOTE: Connie’s narration to the audience is clear and precise. Her interactions with other characters should demonstrate the aphasia she is experiencing.

DOCTOR: Close your eyes, Constance, and keep them closed I obey, but my ears cling to the tiny nylon crackles of her uniform. White blots explode-angry spurting flashes against a humming in my brain. Flakes of snow dance flat on a black square; a television set is broken or left on all night, abandoned by the sleeper.

DOCTOR: Open your eyes, Constance, and keep them open. (Into a tape recorder) This is a thirty-four year old white female ... (To Connie) How many fingers?

CONNIE: (unintelligible response)

DOCTOR: Do you know what day this is?

CONNIE: (unintelligible response) He purses his fat lips into a pink "0", as if he has expected this disappointment.

DOCTOR: What color is this? (holding out the tape recorder) But I do not know what color is. Dr. Francesca non-chalantly squeezes my hand. He studies my face and his eyes are turning black. From their cold depths he searches, listening and probing, for a chink in death, one thin shaft of light. A colorless heat has risen in my brain, spraying little electric bursts that burn out as quickly as they come. (loud cries and unintelligible animal sounds) Charred fumes trickle from my lips; sounds I have never heard. I can smell the residue of rage. All the people in the room are backing away from my bed with horrified eyes, seeking protection in the soft vanilla walls.

DOCTOR: She can't help the shouting. She hardly knows she does it. All short circuits up here, you see (pointing to her temple) She is afraid too, maybe. ***** Mother is allowed to see me for five minutes of each hour. One morning I try to find out what happened. She flutters around the end of the bed, telling me there was a seizure – [a fit, she says]. "What's the matter?" I ask (unintelligible sounds), and she keeps right on talking about how I cannot talk quite, can't understand always, and the artery is broken, yes, deep in there. "Why aren't I dead," I say. (unintelligible sounds) She explains there is a blob of blood, like jello, around the break, covering it over a little. She doesn't know what will happen if the jello melts; yes she supposes it will melt, but not before the operation, she hopes. Her voice is sparrow cheerful, but she picks at the corners of my tucked in blanket, her fingers darting like delicate claws over the wool. *********************** [After weeks of tests and assessments] they push machines around and arrange my limbs with straps. They [are] going to shoot dye into my brain and take an X-ray. Then we'd know. "Know what?" I asked him.

(unintelligible sounds)

DOCTOR: Don't be afraid. But he [is] afraid. Everyone in this room is afraid. Dr. Francesca stands close to my head, looking at me. Deliberately I meet his eyes.

DOCTOR: (encouringly as he injects the dye) You can stand anything for four seconds. (In words and pantomime) I slam rigid into the pain, shooting upward so hard my teeth fuse into my skull; and it crumples, a steel hull destroyed entirely. Its fragments float by, washed away in turquoise. The color is everywhere, so intense that it obliterates me: the I, the eyes, all things, nothing, nothing exists except the color turquoise . . . [and then] I am lying calm in light. There is no weight or color to the air. Water has no ripples. My brain holds no pattern . . . [Dr. Francesca] breaks through the swinging door.. He holds the wet, black square of the X-ray high, in triumph.

DOCTOR: Now I know where it is. Put your index finger on your nose and put the other finger in your ear. Extend the lines until they meet. That's where it is. . . It's a bad place. I know it is in a bad place.. The neurologists have explained that I say "Thursday Thursday Thursday Thursday Thursday Thursday Thursday," instead of the days of the week. At ten in the morning I can talk to Mother. By dark I can only make the hard sounds. "Kick," I can say. Kick, like bones cracking. Most other words are gone, not there anymore. Color is gone. Where are the words? What color is Thursday?

DOCTOR: We'll go in here (indicating a spot on Connie’s temple) And clip here and then ...

here (indicating two additional locations on Connie’s head) and hope we can get the thing out without removing too much of the brain. His eyes are sad when he begins, touching the points where the burl of the electric drill will enter, but by the time he has completed the pattern, they glitter with the hard reflection of challenge.

DOCTOR: I'm confident about this. I'm confident. He is watching me closely. My head aches with the effort to find a word. I know that I can say kick, kick. "Talk." I say it twice, and Francesca understands. He looks at me without moving for a long time. I wait for an answer.

DOCTOR: You want to go with this operation?

CONNIE: Talk?

DOCTOR: Alive is everything.

CONNIE: (Struggling with the word) Go

DOCTOR: This Thursday, then. *********** In the dark I hide from Death. I lie very quietly, as wild birds and beggars do, to avoid detection, to be not sufficiently interesting to her. My eyes are always open, spreading wide to find light. It is always black, empty. I am always alone. I stare for days until white begins to flow into my eye sockets, stuffing the holes until it chokes me. I open my mouth to push it back and . . . (scream, again and again in abject fear) Someone is shouting. The rough edges of the voice rip small holes in the black around me. The barked commands tear the darkness into lacy, floating shreds. Beyond them is the Devil's face, surrounded by a ring of light. Dark eyes are glittering. Lips stretch wide against white, flashing teeth. I hear Him laughing, piercing the black with rising, unearthly sound, and then I recognize Dr. Francesca, who has cut his deal-alive is everything

DOCTOR: (shouting) Squeeze my fingers! Squeeze my fingers! (in words and pantomime) And I reach up to them and grab his hand. (laughter at the accomplishment) Alive is everything.

************ The color of pain is the winter sky, no end and no beginning. The muscles deep in the pit of my stomach are clenched all the time, so tight I cannot make any sound. If I move, the pain will never end. (In obvious pain and in words and pantomime) I lift the top of the tray that swings across my bed. There is a steel mirror underneath. I have not looked at myself since the operation. I expect to see the marks of prolonged pain: ravaged eyes and deep lines around the mouth. I can't take my eyes off my head. There is a wide flat shelf on the right side. And a hole. There is a deep hole the size of a Kennedy half dollar in my head. A thin layer of shiny skin is sucked down into it.. I close my eyes, but I do not cry. *************** When it is clear to everyone that I am not going to die, they hire Sheila, an R.N. who works at the Rehabilitation Institute across the street. Sheila has special training in physical medicine – [she] nurses people who are too sick for therapy, sort of warming them up for rehabilitation. She won't give me coffee until I walk over to the chair. She asks me questions as long as I can talk. Then, when I am tired, she reads the newspaper out loud. Sheila usually asks me who the people are in the newspaper pictures, but I never recognize any of them. This used to irritate me, but now, sometimes, it makes me feel like weeping. Sheila says I am getting much better, that almost everything I say before lunch makes sense. We name things together. [Bed, newspaper, mirror, light] She is very pleased. She calls the tiny marks on the newspaper "letters." I don't understand letters. Can I make some? she asks, giving me a paper and a pen. Suddenly my fingers are frozen. I can't move them.

When Sheila picks up her pad of paper and the pen it is close to the end of her shift. One afternoon I understand something. "You're writing," I say, and she looks very pleased. It is suddenly clear that the newspaper is "reading." I look at my fingers and say, "I can't write." And I can't read-names or newspapers. I don't know pictures or faces. I won't be able to learn to write, read, which is which. (quietly) "I can't talk." *** [The next day Dr. Francesca confronts me] ****

DOCTOR: (angrily) Sheila says you won't talk. His eyes, deep in the sockets, are ignited like live, black coals.

DOCTOR: You can talk. I stare back, helpless.

CONNIE: (to the Doctor) Cat

DOCTOR: Yes you can.

CONNIE: (shaking her head) Cat.

DOCTOR: Try harder.

CONNIE: (shouting and crying) Cat! CAT CAT CAT It is so hard to say it. I am panting.

DOCTOR: Can't.

CONNIE: (softly, exhausted) Can't. The water is tickling my cheeks. It is covering softly, not quite warm, washing the dirt from my eye sockets. I can see the blackness receding, flaking away and dripping with the water, out of sight. It rises in my head and then empties itself, until the darkness is washed away.

DOCTOR: Why are you crying?

CONNIE: (speaking haltingly, but clearly for the first time as she wraps her hands around her head) I'm afraid . . . I am afraid. I can't read or write. I can't talk.

DOCTOR: (Peeling her fingers away from her scalp and looking directly into her eyes – moving his fingers over the indentions in her head) You're a living miracle.

CONNIE: (looking up) You did that before. With a red pencil, your finger.

DOCTOR: You remember that? (He fits the ball of his thumb into the hole and presses against the skin.) It doesn't matter what you lost. It's healed now. [And] I can feel it, feel the edges of my skull soften. ************ Fourteen is not the same as the other floors.

Everyone has the same horseshoe-shaped wound on one side of the head, a tribal scar which can never be rubbed out. When I move carefully along the corridor I can see, in 1487, a tiny, shriveled woman with fingers curved into bird claws, so old that her flesh, veined like onion skin, clings tight to the outlines of her skull. A thin ribbon is tied around her scar and a few white tufts on the unshaven side of her head.

Next door there is a handsome boy about eighteen with a stubble growth of beard beginning. The white of his scar glows through his dark brown crew cut. Sheila told me he had a football injury. My eyes met his, but there is no flicker of response. Sheila says he is fine except that he can't walk.

The retarded boy in 1462, next to me, cries all the time. Sometimes his noises are like moaning, other times he sounds like angry, jabbering crows outside a window. Often, in the night, he heaves dry sobs, without tears, until he falls asleep. He has had an operation to relieve his pain. Today he is calling out to someone unnamed in a language no one understands.

(In words and pantomime) I stop in sunlight to examine my fingers. I riffle them like a child playing a hand game, and it seems to me wonderful that I can do this. I lift them slowly, one at a time in sequence and I see the old lady raising her white, fluttering fingers over a piano keyboard; the retarded boy behind a podium, speaking clearly and forcefully; the quarterback cutting down the sideline, dancing out his dream. Moving the fingers of my good working hand, I weep.
```

---

## IC-2211: Crying in H Mart

- Title: Crying in H Mart
- Author (byline): Michelle Zauner
- Work: Not specified
- Publisher: Knopf
- Publication date as stated: April 2021
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MICHELLE
- Teaser before the introduction: Yes
- Spoken words (computed): 1674
- Already set (do not supply): none

### Source block (context only)

```text
Author: Michelle Zauner
ISBN: 978-0525657743
Publisher: Knopf
Date (Month/Year): April 2021
```

### Introduction (context only: never use it for content warnings)

```text
Crying in H Mart by Michelle Zauner
```

### Performance text (classify this)

```text
MICHELLE: (Pg 8-14) Ever since my mom died, I cry in H Mart.

H Mart is a supermarket chain that specializes in Asian food. The H stands for han ah reum, a Korean phrase that roughly translates to "one arm full of groceries." H Mart is where parachute kids flock to find the brand of instant noodles that reminds them of home. It's where Korean families buy rice cakes to make tteokguk, the beef and rice cake soup that brings in the New Year. It's the only place where you can find a giant vat of peeled garlic, because it's the only place that truly understands how much garlic you'll need for the kind of food your people eat.

H Mart is freedom from the single-aisle "ethnic" section in regular grocery stores. They don't prop Goya beans next to bottles of sriracha here. Instead, you'll likely find me crying by the banchan refrigerators, remembering the taste of my mom's soy-sauce eggs and cold radish soup.

Or in the freezer section, holding a stack of dumpling skins, thinking of all the hours that Mom and I spent at the kitchen table folding minced pork and chives into the thin dough. Sobbing near the dry goods, asking myself, “Am I even Korean anymore if there's no one left to call and ask which brand of seaweed we used to buy?”

MICHELLE: Growing up in America with a Caucasian father and a Korean mother, I relied on my mom for access to our Korean heritage. While she never actually taught me how to cook (Korean people tend to disavow measurements and supply only cryptic instructions along the lines of "add sesame oil until it tastes like Mom's"), she did raise me with a distinctly Korean appetite.

Food was how my mother expressed her love. No matter how critical or cruel she could seem --constantly pushing me to meet her intractable expectations -- I could always feel her affection radiating from the lunches she packed and the meals she prepared for me just the way I liked them. I can hardly speak Korean, but in H Mart it feels like I'm fluent. I fondle the produce and say the words aloud - - chamoe melon, danmu ji. I fill my shopping cart with every snack that has glossy packaging decorated with a familiar cartoon. I think about the time Mom showed me how to fold the little plastic card that came inside bags of Jolly Pong, how to use it as a spoon to shovel caramel puffed rice into my mouth, and how it inevitably fell down my shirt and spread all over the car. I remember the snacks Mom told me she ate when she was a kid and how I tried to imagine her at my age. I wanted to like all the things she did, to embody her completely.

My grief comes in waves and is usually triggered by something arbitrary.

I can tell you with a straight face what it was like watching my mom's hair fall out in the bathtub, or about the five weeks I spent sleeping in hospitals, but catch me at H Mart when some kid runs up double-fisting plastic sleeves of ppeongtwigi and I'll just lose it. Those little rice-cake Frisbees were my childhood, a happier time when Mom was there and we'd crunch away on the Styrofoam-like disks after school, splitting them like packing peanuts that dissolved like sugar on our tongues.

I'll cry when I see a Korean grandmother eating seafood noodles in the food court, discarding shrimp heads and mussel shells onto the lid of her daughter's tin rice bowl. Her gray hair frizzy, cheekbones protruding like the tops of two peaches, tattooed eyebrows rusting as the ink fades out. I'll wonder what my mom would have looked like in her seventies, if she'd have wound up with the same perm that every Korean grandma gets, as though it were a part of our race's evolution. She'd pluck the lint off my coat and pick on me -- how my shoulders slumped, how I needed new shoes, how I should really start using that argan-oil treatment she bought me -- but we'd be together.

If I'm being honest, there's a lot of anger. I'm angry at this old Korean woman I don't know, that she gets to live and my mother does not. Why is she here slurping up spicy jjamppong noodles and my mom isn't? Other people must feel this way. Life is unfair, and sometimes it helps to irrationally blame someone for it.

Sometimes my grief feels as though I've been left alone in a room with no doors. Every time I remember that my mother is dead, it feels like I'm colliding with a wall that won't give. There's no escape, just a hard surface that I keep ramming into over and over, a reminder of the reality that I will never see her again.

H Marts are usually situated on the outskirts of the city and serve as a secondary center for strip malls of Asian storefronts and restaurants that are always better than the ones found closer to town. You'll know that you're headed the right way because there will be signs to mark your path. The lettering on the awnings slowly begins to turn into symbols that you may or may not be able to read. Suddenly, it's another country. Everyone is Asian, a swarm of different dialects crisscross like invisible telephone wires, [and] the only English words are HOT POT and LIQUORS.

Inside an H Mart complex, there will be some kind of food court, an appliance shop, and a pharmacy. My local H Mart is in Elkins Park, a town northeast of Philadelphia. [It] has two stories; the grocery is on the first floor and the food court is above it -- an array of stalls serving different kinds of food. One is dedicated to sushi, one is strictly Chinese. There's a stall for Korean street food [and] there's my personal favorite: Korean-Chinese fusion, which serves tangsuyuk -- a glossy, sweet-and-sour orange pork-seafood noodle soup, fried rice, and black bean noodles.

The food court is the perfect place to people-watch. I think about my family who lived in Korea, before most of them died, and how Korean-Chinese was always the first thing we'd eat when my mom and I arrived in Seoul after a fourteen-hour flight from America. Twenty minutes after my aunt would phone in our order, the apartment ringer would buzz, and up would come a helmeted man, fresh off his motorcycle, with a giant steel box. He'd slide open the metal door and deliver heaping bowls of noodles and deep-fried battered pork with its rich sauce on the side. We'd dribble black, chunky goodness all over the noodles and pour the shiny, sticky, translucent orange sauce over the pork. We'd sit cross-legged on the cool marble floor, slurping and reaching over one another. My aunts and mom and grandmother would jabber on in Korean, and I would eat and listen, unable to comprehend, bothering my mom every so often, asking her to translate.

I wonder how many people at H Mart miss their families. How many are thinking of them as they bring their trays back from the different stalls. If they're eating to feel connected, to celebrate these people through food. Which ones weren't able to fly back home this year, or for the past ten years? Which ones are like me, missing the people who are gone from their lives forever?

It's a beautiful, holy place. A cafeteria full of people from all over the world who have been displaced in a foreign country, each with a different history. But I know we are all here for the same reason. We're all searching for a piece of home, or a piece of ourselves. We look for a taste of it in the food we order and the ingredients we buy. H Mart is where your people gather under one odorous roof, full of faith that they'll find something they can't find anywhere else. In the H Mart food court, I find myself again, searching for the story I want to tell about my mother.

I am sitting next to a Korean mother and her son. The kid dutifully gets their silverware from the counter and places it on paper napkins for both of them. He's eating fried rice and his mom has seolleongtang, ox-bone soup. He must be in his early twenties, but his mother is still instructing him on how to eat, just like my mom used to. "Dip the onion in the paste." "Don't add too much gochujang or it'll be too salty." Some days, the constant nagging would annoy me. Woman, let me eat in peace! But, most days, I knew it was the ultimate display of a Korean woman's tenderness, and I cherished that love. A love I'd do anything to have back.

The boy's mom places pieces of beef from her spoon onto his. He is quiet and looks tired and doesn't talk to her much. I want to tell him how he should be kind to his mom, remember that life is fragile and she could be gone at any moment. Tell her to go to the doctor and make sure there isn't a small tumor growing inside her too.

Within five years, I lost both my aunt and my mother to cancer. So, when I go to H Mart, I'm not just on the hunt for cuttlefish; I'm searching for memories. I'm collecting the evidence that the Korean half of my identity didn't die when they did. H Mart is the bridge that guides me away from the memories that haunt me, of chemo and skeletal bodies and hydrocodone. It reminds me of who they were before, beautiful and full of life, wiggling Chang Gu honey-cracker rings on all ten of their fingers, showing me how to suck a Korean grape from its skin and spit out the seeds.

[You see, that’s why] . . . Ever since my mom died, I cry in H Mart.
```

---

## IC-2212: The Day I Ate Whatever I Wanted

- Title: The Day I Ate Whatever I Wanted
- Author (byline): Elizabeth Berg
- Work: Not specified
- Publisher: Ballantine Books
- Publication date as stated: May 2011
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SOURCE OF THIS QUOTE
- Teaser before the introduction: Yes
- Spoken words (computed): 1873
- Already set (do not supply): none

### Source block (context only)

```text
Author: Elizabeth Berg
ISBN: 978-0345487537
Publisher: Ballantine Books
Date (Month/Year): May 2011
```

### Introduction (context only: never use it for content warnings)

```text
The Day I Ate Whatever I Wanted by Elizabeth Berg
```

### Performance text (classify this)

```text
Jonetta Reed, a 27-year-old graduate student at Cleveland State University explains . . . "If I could sum it up in one sentence: There's more to me than meets the eye. And I think that goes for pretty much everyone, including every person who's overweight. It's not this whole thing where you just eat too much and you have no self-control and you don't exercise. I do exercise. I do try to control my portions. We're not like Homer Simpson, just eating a thousand hamburgers. It's not like that. We're really great people to be friends with and go out with and have relationships with, so don't just count us out because we're fat."

SOURCE OF THIS QUOTE: http://www.cleveland.com/fighting-fat/index.ssf/2010/04/the_heavy_burden_of_being_heavy_as_told _by_5_who_have_struggled.html

I began at Dunkin’ Donuts. I hadn’t gone there since I started Weight Watchers a year ago because I had to lose weight; my doctor made me go.

Weight Watchers is a good organization, I mean it does actually work if you do the program and they try really hard to make you like you, which as you may know is a problem a lot of fat people have, they have low self-esteem. Skinny people look at fat people with disgust and have visions of them stretched out on fuchsia-colored silk sofas snarfing down Cool Ranch Doritoes and Ben and Jerry’s Chunky Monkey, but it isn’t like that. What it is, is eating and eating with your shoulders hunched and your head down to scratch that itch that won’t get scratched, and you have so much shame when you gobble things down you hardly even taste them. You start with I want and you end with I want, only now you have even more weight added to what is already too much and don’t think we don’t know it all, all, all the time.

But anyway, I went to my Weight Watchers meeting one day, and in addition to the usual annoying emaciated people who have no business there, there were two new members who absolutely blew my mind. Both of them on the same day. One was an old woman on oxygen with a walker taking about a thousand hours to get to the scales, and she was not to my eye fat at all. The other was a blind woman. Here is my question: When that blind woman looks into her mirror, what does she see? And anyway, she, too, had no visible blubber. I mean, I just walked out. I said to myself, No. Today, on account of those two women, on behalf of those two women, I am going to eat anything I want from now until midnight. And I drove right over to Dunkin’ Donuts [and] got coffee, heavy cream. “Anything else?” the counter person asked. She was about thirty years old, beautiful long black hair tied back in a ponytail under her Dunkin’ Donuts hat and a really big caboose. What can you do? You’d have to be a weird person not to gain a lot of weight if you worked at D.D. But anyway, [her] fat looked good, truly, every now and then you see a person who wears fat well, it is that tight fat and just really looks kind of delicious and also their attitude is just great, like in your face: I’m fat . . . so what . . . get over your sanctimonious self. Anyway, after [she] said, “Anything else?” I said, “Oh yes, I want some donuts.” I cannot tell you how swell that felt.

“How many donuts?” And I said, “Just get a big box, please, but maybe we won’t quite fill it.” So she got out a big Dunkin’ Donuts box and I just started salivating, like that experiment dog. “Okay. A bow tie, a chocolate-frosted cake, a Key lime, a powdered cake, a Boston Kreme, a lemon bark, a maple-frosted, a coffee roll, a maple-frosted coffee roll, a cranberry muffin, a bagel and cream cheese and butter, too, on the bagel, and a plain Dunkin donut.” And then before she tallied it up I handed her a fifty and said just keep the change and walked out. My back was feeling kind of hypervisible, like I was walking away really cool from a crime scene where I’d been the criminal. My heart was racing and my mood level had shot way, way up.

I got in my car and then I looked around and there was no one so I ran my tongue along every single surface of every single donut. Then I sucked the filling out of the Boston Kreme. I dipped the powdered cake in the coffee and had one bit; ditto the chocolate-frosted. I went on in this manner until I would say about a third of the donuts were gone. And then I am sorry to say I threw the rest away.

I was pretty full, so I went for a walk in a park to make room for lunch. It was a nice day and there were joggers and lots of dogs. Once was a bulldog puppy, which, please, has cornered the market on cuteness. The owner was this very thin woman who looked sort of bitchy, which, think about it, most very thing women do – even when they smile, it’s like grimacing. Fat people are often miserable, too, but at least they look jolly even though it’s really mostly them apologizing, like “Sorry, sorry, sorry I’m taking up so much room,” “Sorry I’m offending your idea of bodily aesthetics,” “Sorry I’m clogging my arteries and giving the thumbs-up to diabetes.” And spilling over airline seats, which, come on, even for skinny people those seats are ridiculous.

Metal girdles!

I decided I’d go for lunch to this café I know where the butter is real and the syrup is real and the waitresses do not in any way judge what you order. I ordered a bacon cheeseburger, fries, and a chocolate malted, and I loaded up the fries with salt and made a neat pile of catsup. When the waitress asked, “Will there be anything else?” I almost ordered two over easy with hash browns because I just wanted one bit of the potatoes mixed with yolk, but no, that would be been too much wastefulness in one day.

But. Because this was a day purposefully given over to gluttony and greed, I walked over to a bookstore, where I looked at cookbooks. You may think, Right, she looked at dessert books, but that’s where you would be wrong. Because guess what? Vegetarian. And some Mediterranean and Indian. And okay, then I found this one? The cake doctor? Which so made me in the mood for a piece of cake. So I went and got that at another café, but I could only fit in half.

By now I was feeling the shame but also defiance.

Like here, I’m carrying the banner for all of you who cut off a little piece wanting a big one, who spend a good third of your waking hours feeling bad about your desires, who infect those with whom you work and live with your judgments and pronouncements, you on the program who tally points all day long, every day, let’s see, 7 for breakfast, I’m going to need only 3 or 4 for lunch, what can I have for so little? Oh, I know. Broth and a salad with very little dressing. And broth is good! Yea! So chicken! That’s what we tell ourselves, we who cannot eat air without gaining, we who eat the asparagus longing for the potatoes au gratin, for the fettuccine Alfredo, for the pecan pit. And if you’re one of those who doesn’t stop right there. You are not invited to the rest of this story. . . . [I thought so].

Okay. Dinner. I was going to have steak and mushrooms and a loaded backed potato and Caesar salad . . . and apple crisp and crumb-topped cherry pie. And a baguette with European butter. You can imagine it, can’t you? The mushrooms sautéed in butter lying seductively over the steak. The potato, buried under butter, bacon, green onion, and sour cream. The two desserts sitting side by side, can you see them? I knew after the day was over I’d have to go back to the plan, go back and confess at my meeting. Which is okay, it’s fine, you can say anything at a meeting. Once someone said she had cheesecake left in her refrigerator from a family dinner and everyone was saying, “Oh, my God, get rid of it, give it away.” Someone else said, “just throw it away.” And this other woman said, “Well, I’m sort of embarrassed to admit this but I have actually taken food out of my garbage and now I’ve learned that I have to pour water on it before I throw it away.”

I myself put coffee grounds over food I throw away, that’ll do it. . . . I ate the dinner, the whole thing, just like I said. And then I took a wooden mallet and I bet my scale. I wanted springs to pop out like they might in a cartoon, but all that happened was it didn’t work anymore and it had a few dents. Still.

The next day I went to a Weight Watchers meeting. . . . I never confessed. I got weighed and I was four pounds up and they were just like, “Well, that happens,” and I bought another scale and that night I had turkey burgers for dinner. 7 points and actually very good and I had spinach and a two-point ice cream thing. And I drank lots of water.

I have to tell you this funny story about water and Weight Watchers that our leader told us. She said she was telling a new member the rules and she guessed she talked too fast. She told the woman to be sure to drink six to eight glasses of water a day. And the woman came back the next week saying, “I did everything you said, but I just can’t drink sixty-eight classes of water a day.” Imagine her at the sink, upending yet another glass of water, wide-eyed and discouraged: This program is hard!

I would like to end this by saying that it felt really good to cheat all day, to eat whatever I wanted. But it didn’t. All that happened was that I felt hollow-eyed. I felt like one time when I was a little girl and I sat on the porch steps one summer evening with my dad. I was already really chubby and he was a very fat man with pretty blue eyes. A couple of times I was with him when people made jokes about how fat he was. He would laugh like he thought it was funny and his belly would shake, it went up and down when it shook, but their remarks hurt him, I could see it – he registered pain in those instances by one quick jerk of his right eyelid. But that night he took my hand and I moved closer to him. I wished someone could [really] see.
```

---

## IC-2213: The Days of Cardboard Boxes

- Title: The Days of Cardboard Boxes
- Author (byline): Eva Burke
- Work: Chicken Soup for the Teenage Soul
- Publisher: Health Communications, Inc.
- Publication date as stated: May 1997
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1409
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eva Burke
Book: Chicken Soup for the Teenage Soul
ISBN: 978-1558744639
Publisher: Health Communications, Inc.
Date (Month/Year): May 1997
```

### Introduction (context only: never use it for content warnings)

```text
Walt Disney once said: “Every child is born blessed with a vivid imagination. But just as a muscle grows flabby with disuse, so the bright imagination of a child pales in later years if he ceases to exercise it.” Travel back with me to your own memories of childhood and the imagination that made everyday and everything an adventure in The Days of Cardboard Boxes by Eva Burke
```

### Performance text (classify this)

```text
Cardboard boxes played a significant role in my childhood days. Don’t get me wrong; toys were wonderful, too, but nothing could out-do a cardboard box and a few kids to go along with it – especially my two best neighborhood friends, Chris and Nick, brothers who lived three blocks away.

Sumer was always the perfect time to have a cardboard box. The long, lazy days offered sufficient time to experience the true essence of a box and to truly bond with it. However, in order to bond with a box, we first had to find one. The three of us would pile into the back of my parents’ truck, briefly jockeying for the coveted wheel seat, then sing the “Na Na Na” song (any song we only knew some of the words to but sang anyway) while we waited for my mom to find her keys. None of us dared to suggest that we ride in the front of the truck; that was for sissies.

Finally, after an infinite number of “Na Na Na” songs, Mom drove us to a box place, and there it was! The most beautiful box we had ever seen. It was a refrigerator box, most definitely the best kind to have. Refrigerator boxes could journey to far better places than any other box, and their ability to anything was simply phenomenal. The furniture warehouse/showroom had thrown this glorious bounty out the back door like it was useless. We had arrived in time to rescue it from the nefarious jaws of a trash truck.

We watched with anticipation as Mom slid the box to the back of the truck. We crawled into the box for the ride home, sheltered from the wind and the bugs that seemed to aim right for the tonsils during mid – “Na.”

Arriving back in the neighborhood was an experience that made our heads swell. Everyone who was outdoors could see us, and word would soon spread that Nick, Chris and Eva possessed a refrigerator box. You see, anyone who owned a refrigerator box held an esteemed position. We would be legends. We would take our box where no kids had ever gone before.

We unloaded our treasure and carried it with great care into the back yard. Chris said we should spend a few minutes of quiet time to gather our thoughts, and then we could discuss our ideas for this magnificent being. We did so for about five seconds. Then suddenly, as if an unknown force opened our voice boxes, we broke into song:

Na Na Na Na

Our box is groovy

Na Na Na

And so are we!

Okay, it was a short song. But it was beautiful.

And I’m sure it would have touched the hearts of those fortunate enough to hear it.

It was time to make our decision. “Let’s go to Zo in our box, “ I said

“Who?” Nick and Chris gave me one of their looks.

“Where to go or where not to go, that is the question,” I retorted.

Nick told me I didn’t make any sense, and I explained that it was all very simple, that he and Chris just needed to learn how to think backwards. Chris decided Nick was right – I didn’t make any sense.

“Zo is Oz backwards, you ignorant little twerps! We wanna go to Zo and do everything Dorothy does in Oz, but backwards.” I was hollering at them because I knew they had better sense than they were using.

Chris looked first at me and then at the box as he contemplated my bright idea. I wondered if Chris and Nick were seriously ill because they should have known by then, from all our past experiences, that boxes (especially this one) could take us anywhere. We could be or do anything we wanted because of the power of the almighty refrigerator box. And we could be backwards about it too.

“You know, Eva is right,” Chris said. “We have never done anything backwards before, so let’s make this the first time. But we can go anywhere backwards, not just Zo.”

At that moment in our young lives we understood clearly that we were going to go down in history. People all over the world would be talking about “The Three Backwards Box Kids.” Other children would attempt to go where we had gone, but none of them could ever be like us because their imaginations were inferior to ours.

We made a solemn declaration that our box would be a time machine. We swore on chocolate peanut butter cups that his backward idea was here to story (at least until the next box). And anyone who broke a promise made over chocolate peanut butter cups was basically considered immoral.

After we had traveled several years back in time, we were faces with a dilemma. We were visiting with a singer named Elvis who inquired about how we got to Graceland. We told him about our time machine, the backwards idea, the chocolate-peanut-butter-cup promise, and how we were going to go down in history. Elvis was all shook up about us, and he said that we were pretty neat kids . . . but . . . .

“But what?” we pressed.

He wanted to know how we were eventually going to get home again if we could only go backwards.

In all our days, we had never been faced with a predicament such as this. We had also never broken a chocolate-peanut-butter-cup promise. We were, you know, up a creek. We could not capitulate. Life always had its ups and downs – this was just one of the very big downs that would take a long night of pondering. Luckily, our parents would not let us stay out all night to play our make believe games.

Soon my mom called out the back door, breaking us out of our imaginary world and landing us abruptly in the backyard again. It was time for Nick and Chris to go home. The three of us quickly made plans to meet at eight o’clock the next morning to discuss solutions to get us out of the disaster we were in. As I ran the few feet to my back door, Nick and Chris took off running the three blocks toward their home. Time could not be squandered. We only had until morning before we would be back in the reality of our imaginary world again.

At 7:33 the next morning, the phone broke the silence, and I stumbled out of bed with a handover from thinking. When I answered the phone, Nick demanded to know if I had covered the box with plastic the night before like we were supposed to do, in case of rain. I looked out the window to see that it had rained, a very hard and drenching rain. With deep regret in my heart, I told Nick I hadn’t, but the responsibility belonged to all of us, so it wasn’t completely my fault.

Nick and Chris came over, and silence replaced our usual banter. Our box had only been with us for one day. Now we were stuck in the real world because our box was dead.

The soggy cardboard couldn’t just be left out in the yard to rot away. It had been a good box while it lasted, and it deserved proper respect. So we dragged it to the side of the street where the garbage was picked up. The day before we had saved it from a trash truck that would have taken its life too early; now it was time for our box to go. Although it was a natural death, it could have been prevented. This reality would be a weight we would carry for all our childhood days.

The three of us sat next to our dead box so we could be there when the trash truck came. We even made up a “Na Na Na” requiem, and we sang with all our might as the truck hauled our box away. No one could have put more sincerity or emotion into a song than we did that day. Although we were mourning our box, we knew we must go on. We must find another box, and we must build another imaginary world with it.

I miss the cardboard-box days. However, just as we had to go on after the demise of our box, I had to go on and grow up. But my childhood imagination will always be a part of me. I will always believe in cardboard boxes.
```

---

## IC-2214: Dear Husband

- Title: Dear Husband
- Author (byline): Joyce Carol Oates
- Work: Not specified
- Publisher: Ecco Press
- Publication date as stated: April 2010
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: LAURI LYNN
- Teaser before the introduction: Yes
- Spoken words (computed): 1717
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joyce Carol Oates
ISBN: 978-0061704321
Publisher: Ecco Press
Date (Month/Year): April 2010
```

### Introduction (context only: never use it for content warnings)

```text
On the morning of June 20, 2001, Andrea Yates drowned her five children in the family’s bathtub. Then she called 911 and waited for the police to arrive. Born Andrea Pia Kennedy on July 2, 1964, in Houston, Texas, Andrea thrived at Milby High School. She was valedictorian, a member of the National Honor Society, and the swim team captain. However, she also had an eating disorder and considered suicide. As an adult, she would be diagnosed with depression, delusional thinking, and schizophrenia. Still, she lived a relatively stable, simple, and devoutly religious life with her husband, Russell, and their family. But by 2001, Andrea Yates was convinced that she and her children were destined for hell. She came to believe the only way to save her children and prevent Satan from returning to Earth was by killing them — and being executed for the crime.

Joyce Carol Oates boldly reimagines the mental state of Andrea Yates in her fictionalized short story, Dear Husband.
```

### Performance text (classify this)

```text
LAURI LYNN: (Pg 316+) Dear Husband, You alone will know the truth of what has happened in this house, in the early hours 6:10 a.m. to 6:50 a.m. You alone have the right to condemn me. It was my failure as a wife and the mother of your children that is my true crime. I am confessing this crime only to you, dear husband, for it is you I have wronged.

LAURI LYNN: Loell, Jr. was a very happy baby. [He] had such a sparkle in his eyes though he came late to speech and could not seem to hear words spoken to him unless loudly, and you were facing him. It was God’ wish to cause our first born to be as he was. And then God sent us twin daughters: Rosalyn and Rosanna. Bright lively girls with white-blond hair. The twins were closest to Mommy’s heart. And little Paul, with his Daddy’s sharp eyes and wavy hair, and Dolly-Ann, our “sudden gift” from God, born within a year of your second son. All of my life has been our family, dear husband.

You are praised as a draftsman and you work with blueprints out of a computer I can’t comprehend. It is like a foreign language to me. Though in high school I took algebra, geometry, trigonometry. Each semester my name was on the honor roll. [I was] a guard on the girls’ basketball team and at the Christian Youth Conference in Atlanta, I was a delegate in my senior year. You would not remember for you were three years older than “Lauri Lynn Mueller” and popular on the football team. It was unbelievable to me that Loell McKeon would wish to date me, still less to marry me!

Dear husband, this letter will be on the kitchen table. I will dial 911 when it is time. On the counter, there are three knives. Who has placed them there so shiny-sharp, I am not certain. I have swallowed five OxyContin tablets saved out of my prescription, and there are twelve more I am to swallow when God so instructs me. Upstairs, the children are peaceful at last. They have been placed on our bed in the exact order of their age for it is this order in which God sent them to us. Those children are so peaceful!

Dear husband, when the “bad feelings” first began, I would have a dream while awake and my eyes staring open driving out on the highway and my hands would turn the wheel of the car to the right—quick as a lightning-flash!— before any of the children could perceive it, we would crash into the concrete wall at the overpass and all would be over in an explosion of flame. This was long ago it seems when Rosalyn and Rosanna were still in car seats in the back. Later, when Paulie was in back with the twins, it was the station wagon I was driving, and the children were fretting as usual, for a kind of devil would come into them when Mommy was behind the wheel and anxious in traffic. Little Paulie would shriek to torment me, his cries were sharp like an ice pick in my brain!

Your mother said, “Can’t you control these children, Lauri Lynn? It should not be that hard, you are their mother.” In her face there is disappointment like a creased glove someone has crushed in his hand.

At Thanksgiving, I was very anxious. You said, “Why on earth are you hiding away in the kitchen washing dishes before the meal is concluded, why do you behave so rudely, what is wrong with you?” Little Dolly-Ann had diarrhea and the twins could not be seated together for their giggling and squabbling and Loell, Jr. ate so fast, with his head lowered, and was so messy, and Paulie sulked wanting to play his videos and shoved at me saying, “Go away Mommy, I don’t love you Mommy.”

Mother McKeon crinkled her nose saying, “You’d think these children are starving, and nobody taught them table manners, look at the messes they make.”

Dear husband, I have tried to keep them bathed. It is hard to fight them sometimes, for they kick and splash in the bath knowing how fearful I am that the floor will get wet, and the tile will warp, and water will drip down through the dining room ceiling. I have tried to keep this house clean. You would laugh at me, your angry laugh like silk tearing -- but I have tried.

When the police come into this house this morning, I am ashamed of what [they] will discover. The bathrooms are not clean. The toilets cannot be kept clean. The boys’ rooms are not clean -- bedclothes stained. There is a harsh smell of the baby’s diapers and of bleach. The twins’ hair cannot be kept free of snarls. They push at my hands, they whimper and kick, when I try to comb their hair. And so many dirtied clothes, socks and sneakers, and towels. I am so ashamed of what will be revealed to you, after I am gone.

It was my fault. I know that such terrible words would never erupt from your mouth, dear husband, except for me. You said, “Lauri Lynn what the hell do you do all day? Look at this house. You have nothing to do but take care of the children and this house and look at this house, Lauri Lynn. You are a failure as a mother as you are a failure as a wife, Lauri Lynn. Tricked me into marrying you, pretending to be someone you are not.”

And never would you strike a woman. My jaw still hurts, but it is a good hurt. A waking-up hurt. I am so ashamed, yet there is a fascination in it, what I have become. I am not now Lauri Lynn, a plain girl known for her smiles. Where that girl has gone, I do not know. Lauri Lynn is not here, the children scarcely knew her. I am a bad mother, and now all the world will know. My children are flawed and broken like the dolls and toys they break, the stuffed animals they have torn. It is for this reason, I think, that this morning at last I acted, as God has instructed. For now what is done, is done. For now it cannot be undone.

It was very hard to force them, dear husband. I began with Loell, Jr. for he was the oldest, and the biggest. He fought me, I was surprised. When I chased him in the upstairs hallway he ran screaming—he fought me, and bit my fingers, but I was too strong for him, and carried him back to the bathroom and to the tub where the water was just warm the way the children like it, and now there is so much water on the floor, it is leaking through the floor and through the dining room ceiling, you will be so disgusted.

Some parts of what happened, I don’t remember. I remember laying Loell, Jr. on our bed, his pajamas so wet. Jesus said to me, “It is true that you are a bad mother but there is a way: ‘If thine eye offend thee, pluck it out.’” And God instructed me, “Lauri Lynn! You must act now.” The little ones believed it was their bath time. And the promise of bath time in the morning is breakfast. If they do not misbehave, they can have their favorite cereal. It was so very early—not yet dawn!

I will not break down and cry. I will not be ridiculed or pitied. I will not be laughed at. I have done a good job, I think. But I am so tired . . .

One by one I drowned them in the tub, it was not so very different from bathing them, for always they kicked, and splashed, and whimpered, and whined, and made such ugly faces. Some parts of what God instructed me, I can recall, but others are faded already now, like a dream that is so powerful when you are asleep, you would wish to keep it, but when your eyes open, already it begins to fade.

“Mommy!” Rosanna cried but I did not heed her, for the strength of God flowed through my limbs. It was a hard task but needed to be accomplished for the children had not turned out right, that is the simple fact. At birth, some babies are not right, malformed, or their hearts are too small, or their brains, or the baby itself is too small, and God does not mean for such babies to survive. These children did not show their deformities to the eye. God has instructed me, and Jesus Christ has guided my hand. I am a bad mother; I will be punished by the laws of man, but I will not be punished by God for God has forgiven me.

The baby did not suffer, I promise. Like the others Dolly- Ann thrashed and kicked with surprising strength for a five-month infant but could not fight her mother as the others tried to do, and beneath the water little Dolly-Ann could not scream. How many times you have pressed your hands over your ears, dear husband: “Why does that baby scream so? Why is it our baby that screams?”

Dear husband, in Heaven, the children will be at peace. They will no longer be dirty, and squabbling; they will be perfect as they were meant to be. From this day forward, your beloved children are with God.

The twins, I have wrapped in their new plaid coats, to lay on the bed. I brushed out their snarled hair like halos around their heads. The others are in their wet pajamas, and I have hidden their faces with a sheet. In the place where I am going, I will not have children.

I am very tired, it is all that I can do to swallow these pills, and take up the carving knife. You will find another woman to honor and to cherish and to bear your children and they will be perfect.

Your loving wife, Lauri Lynn
```

---

## IC-2215: The Death of Innocence

- Title: The Death of Innocence
- Author (byline): Nikki Giovanni
- Work: Acolytes: Poems, Pgs 13-16
- Publisher: William Morrow
- Publication date as stated: Jan 2007
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MAMIE TILL-MOBLEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1757
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nikki Giovanni
Book: Acolytes: Poems, Pgs 13-16
ISBN: 978-0061231315
Publisher: William Morrow
Date (Month/Year): Jan 2007
```

### Introduction (context only: never use it for content warnings)

```text
In 1955, when 14-year-old Emmett Till traveled from his home in Chicago to stay with a great-uncle in Tallahatchie County, Mississippi., his mother was nervous. Though the
```

### Performance text (classify this)

```text
This selection is listed as a Prose Poem and contained in Giovanni’s book of poetry. Check with your tournament for official ruling regarding which category to enter this selection: PROSE or POETRY MAMIE TILL-MOBLEY: (Pg 16) I wanted the world to see what they did to my boy. I wanted Emmett's death to be the last death. I wanted Emmett's death to kill American innocence. I wanted Emmett's death to be not only the death of my boy but the death of innocence. I wanted Mississippi, I wanted America, to give us justice. And I prayed that I would live long enough to see it.

world was changing — the Brown v. Board of Education decision had come the year before — the Deep South was still a dangerous place to be black. The murder of Emmett Till was evidence of the decades-old codes of violence exacted upon Black men and women for breaking the rules of white supremacy. But rather than bending to the intimidation and psychic horror caused by the savage murder, Till’s family, along with national newspapers and civil rights organizations – including the NAACP used his death to strike a blow against racial injustice and terrorism.

Death of Innocence by Nikki Giovanni

MAMIE TILL-MOBLEY: (Pg 13-16) It must have been the waiting. The waiting had to be the worst of it. The only possible, the only possible, the very only possible thing worse than the waiting might be couldn't be would be the waiting being over. The knowing. The knowing they had killed your boy. Not killed. Killed could be an automobile accident. He could be walking down the road with that sort of doo-wop walk he developed as a result of being a breech birth with a knee caught against his chest almost choking him to death before he had a chance to live or that limp could be a result of polio. You had to be grateful that the only scar left was that limp and, of course, that stutter. That stutter that was so frustrating to him because he didn't want to stutter, the other kids would tease him; he wanted to talk strong and manly like he imagined his Daddy did. He wanted to be strong and take care of his mother.

And be wonderful and great and show the world how wonderful he was. Yes. Maybe he was walking down the road on the way back to Uncle Mose's house. Dreaming as he was prone to do. Not just daydreaming like some children sitting in a window on a rainy day wanting to go out but dreamy like he had plans like he was talking to someone from somewhere else. Just not paying attention. How many times had you tried to teach him: Pay attention, Bo. And he smiled that baby-ish smile, that sweet smile, that I'm a good boy Mama smile and said "okay" and went right on not paying attention. Not killed. This was, after all, Mississippi. Killed could be, most likely was, probably was two or three or four mean white boys riding around in a pickup truck. Emmett was on the road alone maybe going to Bryant's to get some bubble gum or some nickel candy maybe some of those windmill cookies 2 for 5 cents and those poor Mississippi crackers were jealous of his shoes and his pants and his white shirt that he wore like he saw a picture of his Daddy wearing a white shirt with the sleeves rolled up. He had the ring on LT May 25, 1943. His Daddy's ring. He was almost big enough to wear it on his ring finger. It was just a little too big so he had wrapped it. Those jealous Mississippi crackers, four or five, maybe six boys riding around in a pickup truck looking for something to do to any girl they could find alone or somebody Black too small to defend himself. Maybe those jealous crazy Mississippi boys grabbed him and wrestled him down. Maybe they hit him and kicked him and threw him in the river. They didn't know they didn't care that he couldn't swim and maybe they watched him flailing and they laughed and drove off and my baby tried and tried but the water pulled him down and he had to give up his spirit. Maybe that's what they mean when they say killed. Emmett was missing. That's what the phone call in the middle of the night said. That he was missing. Mose put his wife on the Chicago train then went calling on everyone who might could help. They didn't want to call me or Mama too early maybe it could get solved without having to make that call. But they had to call. Emmett is missing. Mr. Bryant and Mr. Milam came to get him in the middle of the night. It was 2:00 A.M. and that's not an hour people come to get you when they only intend to teach you a lesson; that's the hour they come when they intend to murder you. There was someone else in the truck. A woman. There was a Black man in the truck bed. "It's Mr. Bryant, Uncle Mose. Open the door." No shame. No sense that there was anything to hide. "I want the boy from Chicago. The one who did all that talking." They offered to pay. They offered to whip him good. They said he was simpleminded and didn't know what he was saying. They said please. But they took my boy. "You don't need no socks, boy. Get on out here." "I never put on shoes without socks," he said. Never understanding the danger. Just a fourteen-year-old boy trying to impress his Mississippi cousins. They would laugh at his stutter; they would ape his doo-wop walk. He wanted to show them he wasn't afraid. Talk to that woman in the store, if you're so tough. She's a white woman. If you so tough in Chicago. talk to that woman. They knew. They knew the danger. They knew he would probably take a good whipping from somebody: Mr. Bryant, Uncle Mose. Somebody would show him that just because he was from Chicago his Mama was from Webb and they were from Money and this is Mississippi and the cousins knew how this system worked not the cripple stuttering boy from Chicago. With his ring and his pants and his soft shoes and his white shirt. And that hat on the side of his head. They would show him. Never thinking three days later there would be a knock at the door. At first nobody knew. Whatever was said was said. The Black community held its breath but Bryant was away taking fish or crabs or something with his half brother J. W. Milam. Milam was a mean cracker. Bragged he knew how to take care of niggers. Didn't hesitate to show anyone. Three days passed and nothing was said. But Bryant came home. Tired. Unhappy. With not much more money than he left with. Working too hard for a good-looking white man and not making much money. Some little Black Judas whispered: What you going to do about that boy from Chicago who did all that talking to your wife? Carolyn Bryant hadn't said a word about it. She knew what would happen. She didn't have to be a nice person, a concerned person, a person with a conscience. She just knew what would happen and she didn't want it on her plate. Milam's wife who stayed with Carolyn while the men were away trying to make a little extra money knew what would happen. She knew what her husband would do. She knew what he did to her; she knew what he did to the children. She didn't want it on her plate. But some little Black Judas without even the thirty pieces without even a piece of candy or a cookie. Some little jealous Black Judas whispered to Bryant: What you going to do? Did he think there would be a show? That Bryant would take Emmett to the front of the store. strip his shirt off and give him five or ten lashes? Did he think it would be fun to see my boy, a fourteen-year-old. a barely fourteen-vear-old cry for mercy? Did he think that would make his life in Mississippi any better? What could he have been thinking? But whatever he was thinking it couldn't have been that Bryant and Milam would take Emmett out at 2:00 A.M. throw him in the back of the pickup and take him to Milam's barn. No one would think they would strip his clothes off of him to make fun of his penis. No one would think they would handle him like they did. That they would beat him and beat him and then the cutting started. Then they beat him and Emmett's eye popped out. There was blood, Emmett's blood all over that barn. The Black man beat him, too. Just so the white men could think he would not testify against them. Finally, mercifully, they put a bullet in his head. But I know my baby was gone way before that. I know Jesus reached into that barn and took Emmett away. I know they sat on a cloud and watched the horror but Emmett was not in that barn when they started putting things in every orifice that they could. Emmett was not in that barn when they started the cutting. No. Emmett was not in that barn. They wrapped the barbed wire around what was left of his neck and told that Negro to attach it to the cotton-gin fan. They hauled his body to the Tallahatchie River. Even they must have known what a horrible thing they had done. Even they must have been ashamed. But, no, killed did not describe what they did to my boy. Three days later when his body was found they wanted to bury him in Mississippi. I wanted him home in Chicago. I wanted the world to see what they did to my boy. I wanted Emmett's death to be the last death. I wanted Emmett's death to kill American innocence. I wanted Emmett's death to be not only the death of my boy but the death of innocence. I wanted Mississippi, I wanted America, to give us justice. And I prayed that I would live long enough to see it.
```

---

## IC-2216: Deja Vu (Again)

- Title: Deja Vu (Again)
- Author (byline): Cole Kazdin
- Work: The Moth Presents All These Wonders, Pgs 112-118
- Publisher: Crown/Archetype
- Publication date as stated: March 2017
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: COLE
- Teaser before the introduction: Yes
- Spoken words (computed): 1651
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cole Kazdin
Book: The Moth Presents All These Wonders,
Pgs 112-118
ISBN: 978-1101904404
Publisher: Crown/Archetype
Date (Month/Year): March 2017
```

### Introduction (context only: never use it for content warnings)

```text
50 First Dates, a comedy starring Drew Barrymore and Adam Sandler made us all chuckle. Every morning, Drew’s character, Lucy, woke up with no memory of what had occurred before she slept. She remembered people, she remembered how to drive, but painted the same mural day after day after day; her family whitewashing her work each night as she slept. It was cute, it was funny . . . it was devastating.

Cole Kazdin gives us insight into life with amnesia in Déjà vu (Again)
```

### Performance text (classify this)

```text
COLE: (Pg 112-118) I wanted a fresh start. I was living in New York. My boyfriend, Adam, had just broken up with me and moved across the country to Los Angeles. Neither of us had done anything horrible, like have an affair. We just weren't a good fit.

But Adam and I were both just passive enough to keep it going. If things got bad, and one of us might begin to muster the courage to pull the plug, then it would be one of our birthdays. Or we’d get really great concert tickets. And that would keep the relationship going for a few more months. And months turned into years.

In three years, Adam never told me he loved me. I think I loved him, but I wasn't going to say it first. (Because I'm so mature.) Then one night Adam took me out to this beautiful dinner. He told me he cared about me very deeply . . . And that he never wanted to marry me. It was essentially a reverse proposal.

COLE: And that was it. He broke up with me, he moved to Los Angeles, it was over. And it was so painful for me.

I remember just wanting to forget him -- forget the past three years and just wake up one morning and start fresh. I got my wish.

I woke up in an ambulance, wearing a cheerleading outfit (which, if you're over thirty and it's not Halloween, raises questions, you know?). There were EMTs all around me, and then I was being placed into a CT scanner, and then I was in this hospital room with all these concerned strangers gathered around me.

But they weren't strangers. I just couldn't identify them.

What I didn't know was that earlier that day there’d been an accident. I’d been filming this television pilot. It was a movie spoof show. The pilot was a parody of Bring It On, the cheerleading movie. We were asked to do a stunt that we never rehearsed.

The stunt was I was to be thrown high up in the air and caught. . . I was thrown high up in the air . . . but I landed on my back and my head. I suffered a massive concussion and a slipped disk in my back. I could barely walk, and I had no idea who I was.

Diagnosis: amnesia.

So I also didn't know that my boyfriend had dumped me a few weeks before and moved to Los Angeles. I didn't know anything.

In the hospital someone put a phone up to my ear and told me it was my mother. I heard this frantic female voice on the other end of the line, and it meant nothing. A friend knew where I lived, took me home, dug the keys out of my purse, got me into my apartment, and put me into bed.

I wanted to call my dad. I remember having that thought. My friend said, "Why don't you rest? We can call him later."

But I wanted to call my dad, and I needed help, because I didn't know the number. Again my friend kind of put me off. "Why don't you rest? We'll call later. Sleep a couple of hours." I started getting frustrated. "Why aren't you helping me? I want to call my dad!" My friend was looking at me like I was out of my mind. Finally he said, "Don't you remember? You just called your dad. You've talked to him three times. We've done this three times. So you can call him, but it'll be the fourth time. And I'm just worried we're starting to freak him out."

I had both short- and long-term amnesia. So I knew some things: I knew how to speak, and I knew how to read. But I didn't know the big stuff, like who I was. I also couldn't retain anything. So if someone left the room and came back ten minutes later, we had to start over. I was living quite literally moment to moment.

Everyone that came and went, they were just strangers to me from a past I didn't even know existed. They tried to help. I remember my best friend, Amy, stormed into the bedroom, screaming, "She's a vegetarian! Don't let her eat any meat!!" That sounded familiar, but it didn't mean anything. I mean, I could have been gnawing on a veal shank. But it sounded important, and I didn't want to forget it, so I wrote it down. There was a pad of Post-it notes on a table next to my bed. I wrote, "You are a vegetarian."

Someone had called Adam, and he flew in from L.A. right away and was at my bedside with tears in his eyes. In fact, the first night he slept in my bed with me, which I remember was kind of weird and, I thought, presumptuous because, like, Who is this guy in my bed? He said he was my boyfriend, but he could have been the mailman. I don't know - I've got amnesia.

The next day Adam showed me pictures of us together, to see if maybe that would jog my memory (and maybe even to make a case for the fact that we were a couple). Pictures of a recent trip I had taken to L.A.: Adam and Cole at the beach, Adam and Cole in front of Mann's Chinese Theatre, Adam and Cole in the Ferris wheel on the Santa Monica Pier. I was in the pictures, but I remembered none of it.

I wrote down everything. I was terrified of forgetting. Every piece of information was precious. Anytime someone told me something, or on the rare occasions when something might come back on its own, I wrote it down.

"You are a vegetarian." "We are at war with Iraq." "Kristen is your friend."

One afternoon I was in a cab, coming home from physical therapy, going over the Queensboro Bridge. I noticed the hole in the skyline where the Twin Towers used to be. My accident happened in November of 2001, and this was a month or so after that.

I thought, That's funny . . . I wrote it down on a Post-it: "Twin Towers gone."

Adam was the Wonderful Boyfriend. This accident was the best thing that could ever have happened to our relationship. He moved into my apartment. He took me to my weekly neurologist appointments and almost-daily physical therapy. He doled out my medications at night and then held me when I woke screaming in the middle of the night from the nightmares that those medications gave me. Or from the sheer disorientation of not knowing who or where I was.

A girl from yoga visited. I do yoga? What else do I do? I was on this detective mission to find out who I was.

I found journals written in my handwriting, in another language. Adam told me it was Portuguese from when I lived in Brazil. I lived in Brazil? Cool. What else? Do I paint? Can I cook?

I overheard doctors saying things like, "We don't know how long she's going to be like this" and "We're not sure if she'll ever fully recover." And they're talking about me. I mean, I'm sitting right there in the room.

The only thing I could be sure of was this growing pile of Post-it notes on my bedside table. I thought the bigger that pile got, the more of a person I became. But it still wasn't me. It was just information, filling an empty space.

Then one afternoon I was in a cab coming home from physical therapy, going over the Queensboro Bridge again. I started to cry. I had no idea why. But I couldn't stop. And it was right as we passed the hole in the skyline where the Twin Towers used to be. When it first happened, there was that really chilling empty space, like ghosts of buildings.

I felt flooded. I mean, I wailed. And I couldn't figure it out. And then it came to me: I was remembering. But it wasn't a fact or a thing - it was a feeling. It was the first time since the accident that I felt real.

That night Adam was tucking me into bed. He had just given me my medications, and he was writing it down on a Post-it note, for when in five minutes I asked if it was time for my medications, as I did every night.

I watched this man taking such wonderful care of me, and I was overcome with emotion.

I said, "I love you." And he said nothing. So I said it again (because I had amnesia and I could get away with that).

"I love you." Again nothing. I didn't understand . . . And then I remembered. The breakup and all the pain that went with it. His move to L.A. Then a post - 9/11 reconciliation. September 11 happened, and we were going to give it one more try.

I went out to L.A. to visit him. We went to the beach, and we went to Mann's Chinese Theatre, and we rode the Ferris wheel at the Santa Monica Pier. I thought of everything he was doing for me. If this wasn't love, what was? Why was he even here? And I think the answer is, he's a good, good man, and he cared for me very deeply.

It took about six months for me to recover. My memory just came back slowly over time. And then I must have been fully healed, because a few months after that, Adam and I broke up again. Only this time I knew it was coming because we'd done it before.

I wanted this fresh start. And I got it. I lost myself completely, and then got myself back, almost as if following a script, replaying my entire history with Adam. Nothing had changed.

But this time, that was comforting. Because if nothing changed, it meant I knew who I was. That I was a real person. And that even without my memory, I was still me.
```

---

## IC-2217: Dielarity

- Title: Dielarity
- Author (byline): Lizz Winstead
- Work: Lizz Free or Die, Pgs 281-296
- Publisher: Riverhead Books
- Publication date as stated: May 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: LIZZY, DAD, LINDA, ANNE, GENE, ANN, MOM
- Teaser before the introduction: Yes
- Spoken words (computed): 1793
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lizz Winstead
Book: Lizz Free or Die, Pgs 281-296
ISBN: 978-1594631429
Publisher: Riverhead Books
Date (Month/Year): May 2013
```

### Introduction (context only: never use it for content warnings)

```text
Have you ever laughed so hard, you cried? Or been in such a sorrowful situation that a burst of laughter escaped? Humor, especially during extremely stressful moments, has the benefit of acting like a “release valve,” relieving tension — if even for a moment — so everyone can re-set and re-evaluate. It is often the glue that holds human connections together. Humor as a way of facing and coping with death: Hospice caregivers call it therapeutic humor in this selection it’s called . . .

Dielarity by Lizz Winstead
```

### Performance text (classify this)

```text
LIZZY: (Pgs 281-296) When they took Dad to the hospital for the last time, it was my birthday; and I was celebrating in Coney Island with my sister Ann and her family. He called me from his room.

DAD: Lizzy, the paramedics asked me if I was on any medications. I told them everything but Viagra. Then they put the oxygen mask on me.

LIZZY: (to audience) Those were the last actual words I heard him say. It was typical of Dad: dark, inappropriate, and funny. (to family, brightly) We'll call him later. Let's go see the sword swallower. (to audience) [But] my sister Linda called back the following morning.

LINDA: (softly, with fear in her voice) You need to come home. Dad is dying.

LIZZY: Dad had tried to prepare me for this day. A few months before his death, he had sent me a card and had asked me not to open it "till after I'm gone." Of course I opened it immediately. The front was a photo of the Manhattan skyline. When I opened it, it simply said, I love you. You are my favorite. Please don't tell the others. The sentiment evoked a range of emotions in me at the time. It made me feel elated that I did something right. Then it made me feel bad for my brother and sisters. Finally, I felt horribly guilty for opening it.

LIZZY: Ann and I flew to Minneapolis and went straight to the hospital from the airport. As we walked toward Dad's room, the sound of laughter got louder. Dad's big double room had become a de facto hospice/party space. There was Dad, lying on his back in a heavy morphine paradise, the bedside table littered with a pizza box and pop cans. Mom was sitting in the chair next to him, holding a piece of pizza in one hand and Dad's hand in the other. My brother, two sisters, and sister-in-law were sitting in a row on the extra bed, tears were streaming down their faces as they laughed. They looked like little kids who were still too small to have their feet touch the floor. Dad couldn’t speak, but he could hear everything. His stomach was bouncing up and down, as he was laughing, too.

ANNE: What did we miss? I hate when I miss any laughing.

GENE: (gasping) The meat! The gas station meat!

LIZZY: . . . my brother said, choking through what I like to think of as dielarity. (pauses as if the audience has asked “what is dielarity?”) dielarity: The dark humor created in the environment of or at the expense of someone dying.

[And] the gas station meat was the crown jewel in the pantheon of Dad's many "deals." Dad loved getting a bargain. He mostly liked gag gifts, like the footstool with humanlike legs wearing tube socks and sneakers. Or the sixty-five-pound brass elephant phones we each got for Christmas one year.

Throughout his years of cruising for "deals." Dad had created a whole world for himself. There was a Vietnamese restaurant he liked with a sign: I DIDN'T COME 9,000 MILES TO COOK YOU ORDINARY FOOD. And a place he called "the Institute." -- a barber school that trained guys just out of prison to cut hair. He could get a shave and a cut for eight bucks.

DAD: I could get the basic shave for six, but I get the works for eight. When you're doing something that involves a razor and a guy just out of jail, you don't want to do it on the cheap.

LIZZY: His criteria for what to do "on the cheap" were wildly inconsistent. Which brings us back to the gas station meat. (to family) We were in Beanie's backyard, eating these beautiful rib eyes Dad had just grilled. (to audience) Dad’s stomach was in full bounce.

(to family) I will never forget being halfway through my steak when you got to the part . . . (mimicking Dad’s voice) "I was filling up the tank and notice this fella's got a station wagon there with the tailgate open. And the guy says, "You want to check out my meat?" And at first, I thought, Who is this weirdo who wants to show me his meat?" (to audience, laughing) Dad was so proud of that dumb joke. Then the story reached its climax with each of us interrupting all over the place.

ANN: (laughing) That guy had half a cow in an old cardboard box in the back of that station wagon.

GENE: (laughing) That came from God knows where! Or when!

LINDA: (laughing) And Dad bought all of it! For forty bucks!

LIZZY: (laughing) We were eating black market roadkill.

MOM: (laughing) The ribs were really very good.

LIZZY: We swapped stories for a few more hours until the dielarity exhausted us all. Dielarious laughter is different from regular laughter, as it drains you of every emotion inside you. It is an exhausting release of all the pain, fear, love, and loss that you have been holding in until your body can no longer physically take it. I freely let it happen, because if I didn't, if I had left even an ounce of energy in me, I would have spent it reminding myself that my life was about to change forever. I looked at Mom gently rubbing his hand. She was eighty- four and had survived three heart attacks, but somehow she never seemed stronger.

MOM: I need to go home. . . I think tomorrow will be a long day. (kissing dad on the forehead) Night, Wilb, see ya tomorrow.

LIZZY: Her tenderness inspired a comforting confidence that we would have Dad tomorrow. [The next day] we didn't know what to do. A hospice worker suggested we each take some time alone with Dad to share our private thoughts.

And so that process began. Mom suggested we say our good- byes in birth order, which meant that I would go last. At first, I felt a bit afraid of being alone with him. His breathing pattern started sounding finite. Each inhale was a jarring gasp that seemed to come in ten-minute increments. When he exhaled, it sounded like a January wind whistling through a small crack in a window. I learned later that is what is referred to in hospice circles as a death rattle.

I climbed into bed with him and grabbed his hand. I put my lips right up to his ear and spoke in my normal voice. "Dad, squeeze my hand so I know you can hear me." (to audience) He squeezed back. I didn't know where to start, so I started with . . . "Dad, I opened your card. I couldn't wait. I hope you are not mad. It made me feel so special." (to audience) He didn't squeeze my hand, but his belly started to bounce. Right then, that felt better than a squeeze.

"Dad, I am who I am because of you, and that includes the bad parts, mister! You couldn't have done a better job of being a dad. I hope you are proud of me. I love you." Squeeze.

I kissed him on the forehead again and went to open the door. His breathing became so shallow, so slow, that as a family we all tried to breathe for him. As a group we inhaled with him and painfully watched as he choked out an exhale, like he had breathed in a box of tacks. It was the worst thirty minutes of our lives. Each of us wanted his pain to end, and we took turns assuring him that he could go, that we would all be okay.

Finally, he took his last breath. We all exhaled with him. His jaw slacked and my brother gently took his two fingers, closed Dad's eyes, and removed the oxygen tubes from his nose. We hadn't seen him without those tubes in years. My father used to say,

DAD: (smiling through tears) Next to your mother, this oxygen tank is the longest relationship I've ever had.

LIZZY: He looked rested. Yellow, but rested. I always wondered what this would feel like, but it all seemed natural. Before I could even form my first thoughts, I looked over at Mom. She was still holding his hand.

MOM: He loved you kids so much; you were his world. He always hoped he told you enough. It's why he sent you kids the cards to open after he died, so you would always have a reminder.

LIZZY: I keep mine open in my jewelry case. (to audience) Then I thought, They all got cards? I had heard that people prepared for their own deaths by reaching out to their loved ones and getting their emotional house in order. I loved that Dad helped prepare all of us in his own way with a special thought for each of us.

MOM: Oh, you opened it? . . . And did the rest of you open your cards, too?

LIZZY: Suddenly I felt horribly guilty. Oh, please tell me I was not the only [one] who went against his wishes and opened the card. Everyone smiled and nodded. They were all clearly shamed, but you could read in each person's face how much Dad's special words gave them peace. No one would be judging anyone today. He had given everyone something lovely to think about.

MOM: Dad wanted you to open those cards after he died, and since you all went against his wishes and already have, I would love to hear what he wrote to each of you. Lizz, you start.

LIZZY: (to herself) Oh, no, Mom, Not now. This is so not the time. This cannot be happening. My father has been dead for five minutes, and I am about to make people feel worse than they already do? (to audience) Do I lie? Yes, I would just lie. I would say the card said, You will always be my baby and I love you. Wait, I can't lie. The first thing I do after Dad is dead is to lie? I don't think so. I haven't even had a decent cry yet.

LINDA: Mom, maybe now is not the time.

ANN: Let's just focus on Dad and you.

LIZZY: Crisis averted. No one wanted to read their cards! I felt relieved, and now I am not the bad guy who denied Mom.

MOM: (determined) Lizz, you start.

LIZZY: (finally crying) The card said, 'I love you. You were my favorite. Please don't . . ." (to audience) . . . and before I finished, everyone said in various tones of unison, "tell the others." Mom had a smile on her face that put the Cheshire Cat to shame. The room erupted with convulsions of dielarity.

Dad had pulled off the greatest gotcha moment of his life. And at his death, no less. He knew we all would open that card the second we got it. And he knew we would all find some smug superiority in what he wrote. But more than anything else, he knew how hard we would laugh when we found out -- laugh at our own ridiculousness and remember that he made us laugh, even after his death. He knew that this moment would be more precious than ever feeling like the favorite.

Bravo, Dad. Bravo.
```

---

## IC-2218: A Difficult Lesson

- Title: A Difficult Lesson
- Author (byline): Tierra French
- Work: Proverbs for the People (Pg 162)
- Publisher: Kensington
- Publication date as stated: 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1329
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tierra French
Book: Proverbs for the People (Pg 162)
ISBN: 978-0758202871
Publisher: Kensington
Date (Month/Year): 2004
```

### Introduction (context only: never use it for content warnings)

```text
Dealing with discrimination, financial strain and the challenges of parenting their children alone, single black mothers often have difficulty finding support programs to help their families. Why? Very few exist. So moms are left to struggle alone, telling themselves that everything is fine, when they know that their kids are spirally out of control.

As we work toward becoming a more inclusive society, we should consider how we address the special challenges single black mothers face. Support systems must be created to provide a safety net. No mother should have to learn such . . .

“A Difficult Lesson” by Tierra French
```

### Performance text (classify this)

```text
I should’ve seen it coming, but I didn’t. I should’ve stopped it before things got this bad, but I couldn’t. Now my baby girl is dead, and there’s nothing I can do to change it. I guess I should take this story back about a year, but first, let me explain a few things.

My name is Rosa Lee Sherman. Me and my family have lived in Hopkinsville, Kentucky, since our ancestors planted roots here in the nineteenth century. I have a son, Joseph Lee Sherman, and, well, a daughter, Tonya Lee Sherman. Things seemed to be going pretty smoothly for my family – that is, until about a year ago.

Joseph Lee was a model student. He made good grades in school, was the captain of the junior debate team, and all in all, a fine son. Joseph even won a trophy for his many debates on the horror women experienced as a result of rape and sexual assault. But Joseph was what most teenagers would call an outsider. He didn’t have many friends, and the ones he did have were closer to associates than real pals. He never went out to parties or spent the night over at a friend’s house. He never talked on the phone or went to school functions, except for those debates he loved so much.

And then we had my daughter, Tonya Lee. Tonya and Joseph were like oil and vinegar. They hardly ever spoke to each other except to say, “Move,” or “get out of my way.” Tonya loved to party; child, that girl could really party! There were school nights when she kept me waiting up until four in the morning for her to come home. But through it all, she was my baby, and I loved her.

At this point Joseph was a junior in high school, and he was six feet-six inches at sixteen years old. Child, I tell you that boy was big, and I never thought nothing of it. I guess we had grown used to his size. At the beginning of the first semester, the basketball coach asked him to join the school team. I’ll never forget that day Joseph came home grinning from ear to ear. It was the first time I’d seen him that happy in a long while. He said, “Mama, I’m finally gonna be accepted. Finally, I’m gonna be accepted!”

The next day, Joseph went to try out for the team, and child, I tell you, he had a ball. The kids was right nice to him. Joseph told me the coach just loved him and guaranteed him a starting spot on the team! So, needless to say, Joseph began playing basketball for the school. It was like he was coming out of his shell. The boys on the team really liked him, or acted like they did, and Joseph began to hang around them more and more.

I noticed that Tonya was still rowdy and unpredictable as usual, but she was learning to like her brother a lot more, and the same with him. I even caught them one night in her room at one in the morning, talking and laughing with each other. That made me so happy, I just went into my room and cried tears of joy. Then Joseph started to hang out with the boys on the basketball team. They just went out for pizza occasionally, or to a movie, but gradually they became really close friends and Joseph started partying and hanging out almost more than Tonya Lee.

What I didn’t know at the time was the kind of things this new group of “friends” were encouraging my son to do. Child, I swear to God if I had known I would have beaten every last one of them, then sent them running home to they mamas.

One afternoon, Joseph didn’t come home from school, and I knew he was out there hanging out with his “friends.” They were roaming the streets all night.

From what the police told me, they busted the windows out of someone’s care, and they hid in some bushes and got caught.

Now I tell y’all, if I’da been in my right mind that boy would’ve gotten the whipping of his life and I would’ve made him spend the night in jail, but I picked him up and gave him a screaming about making me come out the house so late at night.

Well, I guess I thought that brush with jail would’ve been enough to make him not want to get in trouble with the law anymore, but that definitely did not work. It looked like every week the police were either knocking on my door or calling on my phone. Lord, I wish I could’ve stopped this before it got so big.

About a week before the prom, Joseph turned seventeen. To celebrate, he and his friends decided that they would throw a party, but they didn’t have any money. I don’t know whose bright idea it was, but they decided to rob a 7-Eleven. And they did it. No one was caught, but like my mama always told me, “what you do in the dark will eventually come to the light.”

I remember Joseph’s prom night like it was yesterday. Tonya Lee had been invited by some friends, and she looked so pretty. Joseph even rented a tux even though he hadn’t asked any girl to the prom. I took pictures of them and walked them out to the limousine, never imagining that my baby girl would not be coming back home that night.

Tonya and Joseph rode to the prom together, but they split up when they go there. Afterwards, Joseph met up with his friends from the basketball team. They dover up to a teen hangout called The Lot, which was really just an old parking lot where kids got drunk.

All night Joseph and his friends had been trying to get girls to sleep with them, but none would. Finally, they did something I thought my son would never do. One of the other boys grabbed a girl who was so far out of it, she was laying across the hood of a car. They put her in the backseat and placed a paper bag over her head so they wouldn’t have to look at her. Each one took their turn with her. After Joseph’s turn, one of his friends went back, and while he was having his way with her, she woke up and started fighting. They boy tried to hold her down, but the paper bag fell off and she saw his face. He shot her in the head. Joseph heard the gunshot and ran to the car. The boy was already gone, but he found his sister . . . dead. My baby girl was dead in the car.

A week later my baby was buried, and all I could think about was how my son became the exact same thing that he so forcefully debated against: a rapist. The police had taken him and the other boys to jail, where they were being held until their court date.

At the funeral I cried, begging them not to take my baby away, but she was already gone. No matter how much I cried, it didn’t change a thing. My baby girl was gone. Gone.

After Tony Lee died, I tried to pick my life up, what little I had left. Joseph and the other boys were charged with aggravated rape and were each sentenced to three years in prison.

Like this famous black guy used to say in the sixties, “If you don’t stand for something, you will fall for anything.” My Joseph just lost sight of everything he stood for. So he fell. But even at my age you still can learn how to stand on your principles, and for us, this has truly been a difficult lesson. Good-bye, Tonya Lee.
```

---

## IC-2219: Disneyland

- Title: Disneyland
- Author (byline): Laurie Notaro
- Work: I Love Everybody (and Other Atrocious Lies) Pg 133-150
- Publisher: Villard Books
- Publication date as stated: June 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: LAURIE, ANGELINA-CHARLIZE, NICOLAS, OTHER CHILD, MAD HATTER, MAD HATTAR, CONDUCTOR, NICHOLAS
- Teaser before the introduction: No
- Spoken words (computed): 2152
- Already set (do not supply): none

### Source block (context only)

```text
Author: Laurie Notaro
Book: I Love Everybody (and Other
Atrocious Lies) Pg 133-150
ISBN: 978-0812969009
Publisher: Villard Books
Date (Month/Year): June 2004
```

### Introduction (context only: never use it for content warnings)

```text
According to literally everybody on planet Earth, it’s impossible for a person to make it to 30+ years of age without ever having been to the most magical place on Earth.

In fact, whenever you tell a person you’ve never been to Disneyland, they go through at least seven different stages of stunning disbelief before telling you that you have to — no, listen: YOU. HAVE. TO. — get in a car and drive to Disneyland immediately.

Hours later, you find yourself in a car bound for the magical land of Disney, and there’s no going back. You’re going to Disneyland for the first time, as a grown adult, and there’s nothing you can do about it.

Disneyland by Laurie Notaro
```

### Performance text (classify this)

```text
LAURIE: (Pg 133-151) Everywhere we went in Disneyland at least two out of five kids were sobbing, screaming, or hyperventilating, having either been recently smacked, recently yelled at, or recently threatened with being "sent back to the room."

I, however, was having a grand time. Somehow, either I had arrived on the perfect day or I had traveled through some sort of self-esteem time warp, but I was one of the prettiest people at Disneyland. Now, honestly, that's not saying much about me, but I will admit that every time I saw two honey-baked hams swinging out the armholes of a tank top, my self-esteem skyrocketed. A size sixteen anywhere else in the free world translated to a size four here, and I never felt so liberated.

I loved Disneyland. I LOVED IT. I had no idea I was going to have such a good time when my sister had asked me to accompany her and my nephew Nicholas to celebrate his fourth birthday. I mean, it's Disneyland, and it has very little appeal for a childless woman in her thirties, unless her intelligence level is significantly below average. I agreed to go on this trip for two reasons:

1. I try really hard to be the cool aunt . . . going on this trip would give me the opportunity to have fun with my nephew, bond even closer with him, and build his trust in me so that I might wield him like a puppet and mold him into the child I absolutely knew we both wanted him to be.

2. I was also at Disneyland paying penance for "embarrassing and traumatizing him in front of twenty of his little friends," as a helper in Nicholas's preschool classroom for the Harvest Festival or, what they used to call in less stringently politically correct days of yore, Halloween.

Now, I will admit that perhaps I had some responsibility in the matter, but what unfolded that afternoon was in no way entirely my fault . . .

After the teacher introduced me as Nicholas's Aunt Laurie, she assigned me to the spider web table, where I was supposed to help little kids make a spider web on a piece of paper with glue and string. And that was all go-ing fine until the first little girl I was supposed to help, Angelina-Charlize, didn't want to make a spider web, she just wanted to write her name. I was cool with that. That was fine. No skin off my nose. Go ahead and write your name, you know? So Angelina-Charlize wrote her name, complete with a backward r. ln an attempt at helping, I told her that we should try turning the r around a bit, and that's when she openly mocked me.

ANGELINA-CHARLIZE: (chanting) Aunt Gloria doesn't know how to make an “r” . . . That's so sad for a grown-up.

LAURIE: No, really, the r needs to face the other way -- Would you like me to show you?

ANGELINA-CHARLIZE: There's an r in my name, so I should know. Aunt Gloria can't make an r, Aunt Gloria can't make an r!

LAURIE: Actually, it's Aunt Laurie, and I've been writing for a long time, so maybe I should know.

ANGELINA-CHARLIZE: If you know, then why can't you make one? Because you can't! You can't you can't you caaaan't!"

LAURIE: "You know," I wanted so desperately to tell them, "you girls keep writing in your little chimpy hieroglyphics that only a mirror can read and I'll be more than happy to write you a recommendation to Klown Kollege when the time comes, because you will indeed need it."

Instead, I just smiled and said: March to your own dyslexic drum, Angelina Calista Jennifer Aniston Lopez Drew Barrymore. I just really hope you like the circus.

That was pretty much the moment that Nicholas's teacher came over, leaned into my ear and whispered, "Maybe we should try the play area, where it's not so structured."

I had been fired from the spider web table. I had just totally gotten fired from the spider web table, and unjustly so!

Whatever, I said to myself, I'll show them what I can do in the play area, I'll show them. Much to my relief, I saw my nephew in the play area, running what appeared to be an invisible grocery store, using his creative imagination, just like his Aunt Laurie had taught him.

NICOLAS: And there you go. [Nicholas said to another little boy as he handed him a big fistful of air.]

LAURIE: Hello, sir. I would like an apple. Do you sell apples, Nicholas?"

NICOLAS: Yes, I do," [handing me absolutely nothing] And my name is Mr. Booley when I'm at my store . . . It's forty dollars, please.

LAURIE: Well, that's a little steep, don't you think? Safeway has apples for ninety-nine cents a pound, and I can actually see those!"

NICOLAS: Well, then, maybe you should go to Safeway.

LAURIE: Okay, okay, I get it [putting out my hand with nothing in it.] Here's your forty dollars.

NICOLAS: [Scoffing] My store only takes credit cards.

LAURIE: Did he give you a credit card? [pointing to the customer before me]

NICOLAS: He's a little boy, Aunt Gloria. He doesn't have credit cards. Are any of your credit cards still good?"

LAURIE: I think maybe you've been talking to Grandma about my credit status, but let me assure you that it is almost cleared up now. Maybe I will go to Safeway! And you know my name is Aunt Laurie!"

NICOLAS: [yelling and pointing] Aunt Gloria shoplifted! She shoplifted my apple!

LAURIE: I did not! And his prices are highway robbery! Would you pay forty bucks for an apple? Plus twenty-one percent interest? . . . Wait . . .There is no apple! [showing everyone empty, appleless hands] You can't steal something that doesn't exist! There is no apple!"

OTHER CHILD: I saw her take a banana, too!

LAURIE: So that was why I was at Disneyland. I thought it would make up for the alleged, imaginary fruit thievery incident.

Now, I was at the "Character Breakfast" in Goofy's Kitchen ($35 to have the Mad Hatter hop around your table like a flea as you're trying to eat your Mickey Mouse waffles).

MAD HATTER: Hey, how are those waffles? They should make Mad Hatter waffles! Mad Hatter waffles! Waffles with a big hat! Those are the kind of waffles I'd eat!"

LAURIE: You know, we could have grabbed a bagel outside for two bucks, but then the delight of having a neurotic midget dressed as Oscar Wilde buzz around us like a palmetto roach would have been lost forever.

NICOLAS: [squealing] Goofy! Goofy!! Over here, Goofy, over here! It's my birthday!

LAURIE: I turned around, and there he was; that giant dog thing or walrus or whatever he is suddenly appeared, pulling the little children toward him like safety pins to a magnet.

MAD HATTER: It's my un-birthday! Come to my tea party!"

NICOLAS: "I love Goofy!" [hugging Goofy]

MAD HATTAR: Goofy thinks he's all that, but he's not. You'll hug Goofy but you won't hug me. But let me tell you something, Goofy is not as hot as he thinks he is. Are you, Goofy? Are you?"

LAURIE: And then, as I turned to look at Goofy and Nicholas, Goofy's middle finger-and I mean there was no mistaking it, since he only has three of them-was vividly scratching his nose. Goofy flipping off the Mad Hatter? That is the coolest thing I've ever seen. I'd totally give them both fifty bucks to fight. *******

NICOLAS: I love Gadget's Go Coaster! You'll ride, too, won't you, Aunt Laurie?

LAURIE: Of course. It's your birthday, how could I not? (to audience) The whole ride, which was a basic, no-frills kiddie roller coaster sporting props of oversize combs, and a couple rather large stationary frogs, lasted no more than a minute, so when the train pulled to the boarding platform at the end, Nicholas said he wanted to go again.

Before I could even say anything, the train took off and I was trying to concentrate on his fun when we turned a bend in the ride, and then suddenly out of nowhere, something hard and fast struck me in the side of the head. I grabbed my skull, which was now wet with a liquid I was really hoping was not a body fluid, like blood, and that's when I saw it -- a seemingly placid, peaceful, unaggressive frog statue until it decided to spit at you with a fire hose of water that was conveniently hidden from view. I was still trying to wipe the water from my face when we pulled into the boarding station next to an empty platform.

CONDUCTOR: Wanna go again?

LAURIE: And the conductor took off for our next round without even stopping. (to conductor) Hey! I'm done with this ride! Aunt Laurie is done!

PPPLLLLTTT!! went the frog as I passed him again, hard and fast like the first time and just as wet. And there I was, there I was, a wet, childless woman in her thirties, trying to wipe water out of her eyes, one side of her head dripping with frog spit, as she went around and around and around the Go Coaster. Finally, THANK GOD, someone was on the platform when we came around the last time.

[to Nicholas] The frog on your ride hocked on me, you know, and wrecked my pretty supermodel hair. And I think it also left a hematoma where the spray hit me in the head. It's all soft and squishy in that spot now."

NICOLAS: Gadget's Go Coaster made me ready for Splash Mountain! Can we go?

LAURIE: Oh, come on, dude! [stomping my foot] I already look like a sponge! Splash Mountain? Let's go back to the hotel and eat room service stuff, okay? Eighteen-dollar grilled cheese sandwiches!

NICOLAS: [shaking his head] Splash Mountain!

LAURIE: Okay, fine. I am here to pay for my sins. Before I knew it, I was hustled into a log, sitting in the second seat behind one of the almost teenage sons of the guy ahead of us in line. He looked at the wet side of my head and gave me a pained smile.

(to pre-teen) I know you were hoping to be straddled by a skinny blonde cheerleader with perfect skin and a Crest Nighttime Whitening Strips smile. But an hour ago, I was the hottest chick in this park.

He grimaced visibly and moved forward on the log before we lurched and then took off. I heard my nephew squeal with anticipation directly behind me. We reached the top, paused for a moment, and then dropped furiously downward, and that's when I gasped.

Because that's when it hit me: When you're about to dive into a pool of water from four stories up going roughly 30 to 40 miles per hour and you're wearing a white T-shirt with a white nylon bra underneath it, there's a very good reason to try to get the hell out of that car. A very good reason.

NICOLAS: Why are your arms crossed? Are you mad?

LAURIE: I'm not sure if 'mad' is the word, Nicholas. I'm just trying to keep our little trip here at a G rating. If I uncross my arms, either I'd get taken away by or I'd pop up in the latest version of Totally Ugly Girls Gone Wild. I started out so great this morning, and now I look like a used Bounty paper towel.

NICHOLAS: Let's go to Tom Sawyer Island!"

LAURIE: Fine with Aunt Laurie. She needs to find some sun before she gets nominated for adult entertainer of the year.

Over on the island, I tried my best to keep up, but I lost [him] in the labyrinth of Injun Joe's Cave, being that I couldn't move very freely without exposing myself to a random child. In favor of keeping my balance and remaining upright, I decided to try and backtrack my way out and then find a nice sunny spot where I could dry out and enjoy the benefits of opaque clothing again. Finally, I saw the opening of the cave and headed toward it, and as I entered daylight, I suddenly saw the tumble of sky, the sun, glimpses of blurry faces, and finally, a big patch of brown all tossed in front of me like a salad.

When I looked up, I heard a chorus of tiny giggles and saw a bunch of rotten kids above me on the mountain, peering over and cackling like Children of the Corn. I had totally eaten it on Tom Sawyer Island, which wasn't surprising since my arms were entirely useless. As I got up from my full-body dirt sprawl, grasping at the base of the mountain, I tried to act cool, like it was no big deal, while the kids still chortled.

I looked down at myself, and I saw three mud circles, one formed perfectly over each already wet boob, then a particularly large one that covered the spot where my big, fat belly is.

Well, I thought, at least I'm not naked anymore. I am emotionally destroyed and physically devastated, but I am no longer flashing.

I HATE DISNEYLAND.
```

---

## IC-2220: A Door Near Here

- Title: A Door Near Here
- Author (byline): Heather Quarles
- Work: Not specified
- Publisher: Laurel Leaf
- Publication date as stated: January 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: DOUGLAS, KATHERINE, TRACEY, ALISA
- Teaser before the introduction: Yes
- Spoken words (computed): 1587
- Already set (do not supply): none

### Source block (context only)

```text
Author: Heather Quarles
ISBN: 978-0440227618
Publisher: Laurel Leaf
Date (Month/Year): January 2000
```

### Introduction (context only: never use it for content warnings)

```text
Everyone dreams of having the “perfect family” -- with siblings (brothers and sisters) you can count on, lovable grandparents, and understanding parents. Even though some families are filled with weird and wacky relatives, you grow up loving them anyway.

Of course, there are the “broken families.” In this selection, the mother of four children grows to become an alcoholic after she gets divorced and loses her job. It is up to Katherine, the eldest, to keep her family alive in A Door Near Here by Heather Quarles.
```

### Performance text (classify this)

```text
(pg 9-12) Careful not to step on any of the empty bottles near my feet, I reached out to push her shoulder again, but she slapped my hand away with a force that encouraged me. I wondered if maybe she was starting to get better. A little bit of her hair was sticking out from the top of the quilt - blond and wavy like Tracy’s - and if I only looked at that part of the picture, I could almost pretend she was fine. Just taking a nap or something. “Mom, do you know where the main water valve is? Douglas is trying to fix the sink.” “Go away, I’m sick.” I couldn’t stand to look at her swollen eyes, so I concentrated only on her hair, which was golden. Perfectly golden, like it always had been… for years and years, before her face had changed. “The main valve, Mom. The main water valve? Where is it - in the basement?”

“In the base… ment? What are you talking about? Ask your father where it is - he’s the one who wanted the stupid… house.” She lifted the bottle of sherry and emptied the contents into the glass, sending it spinning in crazy circles on its base. She watched until it stopped teetering, then she gave a strange giggle and let the bottle fall to the carpet. “Mom, Dad lives in Michigan. He left 10 years ago.” “Well, tell me something I don’t already know. You little brat.” Right then Douglas stuck his head in the door. “Katherine (whispering), we found it. It’s fixed. It’s off.” I backed toward the door, keeping my eyes on my mother. “Ok. Sorry, we found it, Mom, you can go back to sleep.” “You kids get out of my bed, my . . . room. My God, can’t you even let me rest in peace? Just go away!”

(Pg 19-20) See, this wasn’t the first time my mom had gone on a drinking-sleeping binge for a bunch of days in a row. It was just the longest - because before, she’d always had a job to worry about. And even when Mom was up and sober, she was practically never around. Even though she earned money, Mom herself was always saying that if it wasn’t for Dad’s child-support checks we’d all go down the tubes. That fact really pissed her off, which is why she worked so many hours to try to get promoted, and why it especially sucked when she got fired by her boss “for having one lousy beer on the job.” That was all she talked about for the rest of the summer, which was extremely annoying. She bought a ton of new clothes, went around job hunting, got all these rejection letters. Then, finally one day in September, she just climbed into bed with her sherry and told us she wouldn’t take any phone calls. My mom is an alcoholic, in case you haven’t figured that out by now. She has all the signs. I’ve read a million magazine articles on the subject, so when she started drinking so much and missing work, I knew what was going on and I explained the whole thing to Douglas and Tracey. It didn’t take a rocket scientist to figure it out. But Alisa didn’t know - she just thought our mom was sick. (Pg 24-25) I was five years old the day my dad left my mother and took off to live with Ophelia in Michigan. I only knew who Ophelia was because she used to sit at the front desk of my dad’s dental practice, and she gave me purple toothbrushes when I went in for check-ups. My dad took Douglas, Tracey, and I all out to dinner and when we finished eating, he told us he was moving far away with Ophelia - not because he didn’t love us, but because he loved her so much more than Mommy. Then he drove us back to the house, dropped us off on the front steps, and we didn’t hear from him again for three years - when he mailed us an invitation to his and Ophelia’s wedding. My mom yelled and swore and drank for three weeks straight after that. I still remember it. It was the first time I ever saw her drunk. Even though I didn’t know what drunk was at the time, I knew something was different. She started serving popcorn for dinner every night, for one thing. While we ate our popcorn, she’d tell us what a dirt-eating worm our father was, and drink sherry and cry. I kept thinking I would cry too, but instead I just kept getting that headache behind my eyes. And ever since then, for almost ten years, I have never cried again for any reason. I’m not sure whether that should worry me or not. (Pg 16) Two years after my parents got divorced, Alisa was born. I have no idea who Alisa’s biological father is – I don’t think my mother even knows. (Pg 41)

My mom had a million boyfriends. Strictly speaking, I guess Alisa was only our half sister. But she’d always seemed more related, not less. We all remembered the day she’d come home from the hospital, looking like a shriveled-up raisin in a yellow blanket. We’d been in love with her from that day on. (Pg 1) Alisa [is] in third grade and (Pg 17) is crazy about C.S. Lewis – [you know] The Lion, the Witch and the Wardrobe. (Pg 1) [She] handed me the letter: (Pg 18) Dear CS, I like your books about Narnia. I can tell you did not make them up because no one could make up espeshially about Aslan, so I know they are true. I was wondering if you could tell me where a secret door is from here to Narnia. I need to go to Narnia very bad, I think someone there can help my mom, she is sick. Love, Alisa Donavan (Pg 21) I decided Tracey, Douglas and I should have a meeting. We needed a more organized way to deal with Alisa and Mom – and life in general. (Pg 34) After school, we had our first official “family meeting in the treehouse.

(Pg 37) KATHERINE: “I think we should really talk about how we’re running things. The situation with the house and food and Alisa – especially money and food. Well?”

DOUGLAS: “Well, what?”

KATHERINE: “What do you think?”

DOUGLAS: “What do we think of what?”

TRACEY: “She means about Mom, Douglas. What are we going to do about Mom?” (pg 39) KATHERINE: “We need a plan for what to do about us - and Alisa – Especially Alisa. She’s getting totally neglected. We need to figure out a way to keep things normal while Mom’s in bed. We should eat together and have clean laundry, you know? (Pg 37) What I’m talking about are goals. Establishing the means and ends to a plan of survival.” (Pg 38) TRACEY: “We’re running out of food. The house is a sty. You’re the only one who works, Douglas, and you don’t make that much from a paper route once a week. Mommy’s probably not going to ever get up, she’s probably going to die up there, and what Katherine means is what the hell are we going to do?” (Pg 39) KATHERINE: “I made a list of ideas --”

DOUGLAS: “You’re not going to try to get the sherry away from her again, are you?

KATHERINE: Calm down, Douglas. I don’t think we can do anything about Mom. As long as she keeps eating, at least a little bit, she’s not going to die. People don’t die from being alcoholic, except after a long time like twenty years. (Pg 40) DOUGLAS: Maybe we should just call Dad.”

TRACEY: “We can’t.”

DOUGLAS: “Why not? Just because you guys hate him.”

TRACEY: “If Dad found out Mom’s been drunk for this long, he’d make us go stay with him and Ophelia in Michigan -- and then what would happen to Alisa?” (Pg 42) DOUGLAS: “Ok, you’re right. We can’t tell Dad.”

TRACEY: “We can’t tell any teachers either. They’ll report Mom to Social Services and we’ll get stuck in foster homes.

(pg 43) KATHERINE: “It probably won’t come to that. If we’re smart about how we act right now, it won’t come to that.” (pg 45) In the end I wrote down conclusions in my notebook: 1. Tree house meetings will now be daily. 2. Current assets: $33.25. 3. Don’t tell ANYONE about Mom. And 4. Don’t act suspicious. (Pg 44) I believed we could handle anything. Even if Mom never got back up. I thought we could keep everybody safe. Which just goes to show how stupid you can be when you’re fifteen. Even if you’re smart. (Pg 230) My mother didn’t stop drinking until they actually took her to the hospital. Ms. Haley [Alisa’s teacher] took her, and the only reason Mom agreed to go was because she was still drunk and she wanted Ms. Haley to leave her alone. As far as I know, she hasn’t gotten any less depressed and it’s been eight months. (Pg 223) We live in Grand Rapids now, with my father and Ophelia. All of us, including Alisa.

(Pg 230-231) [The other day], Alisa sat down under the tree house where there was a patch of shade. I sat down beside Alisa and we looked back at the house.

ALISA: “Katherine, you still don’t believe in Narnia, do you?”

KATHERINE: “No.”

ALISA: “Do you believe in God?” I looked up through the tree branches to the sky. “I don’t know.”

ALISA: “I do. I believe in God.”

KATHERINE: “Well, you believe in everything.” Right at that moment, looking at Alisa’s suntanned face, I felt practically joyful. I’m not sure why, even, but I was happier than I had been in a long time.
```

---

## IC-2221: Dorrie and the Pin Witch

- Title: Dorrie and the Pin Witch
- Author (byline): Patricia Combs
- Work: Not specified
- Publisher: Lothrop Lee & Shepard
- Publication date as stated: March 1989
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1514
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patricia Combs
ISBN: 978-0688080556
Publisher: Lothrop Lee & Shepard
Date (Month/Year): March 1989
```

### Introduction (context only: never use it for content warnings)

```text
The bad reputation witches have acquired is mainly due to the way they were presented in the fairy tales collected by the Brothers Grimm in the beginning of the 19th century. There is the vicious cannibalistic witch in Hans and Gretel, and the horrible woman who locks Rapunzel into the tower. Poor Snow White has a witch for a stepmother, and Sleeping Beauty was sent dreaming by another evil representative of the trade. But not all witches deserve the bad rap. My favorite witch of all time is Dorrie . . .
```

### Performance text (classify this)

```text
Dorrie is a witch. A little witch. Her hat is always on crooked and her socks never match. She lives with her mother, the Big Witch, and Cook and her black cat, Gink. Dorrie and the Pin Witch by Patricia Combs.

All of Witchville was noisy and busy. Tonight was the Witches Ball.

Cook had made cakes. The Big Witch was wrapping them while Dorrie packed them into baskets. Suddenly there was a pounding on the back door.

The door flew open. Witch Burdock and her sister Henna stood there, shrieking, “The cakes! The cakes! Hurry!”

Cook handed them the baskets. Witch Burdock looked inside. “You made them orange, not yellow!”

“Henna told me orange,” said Cook.

“I never! Liar!” screeched Henna.

“Goodbye,” snapped Cook, pushing them out the door.

“I wish there weren’t going to be a ball,” said Dorrie. “It’s been one crabby person after another all week long.”

“That’s just party nerves,” said the Big Witch. “I’m off to get my new cape from the Pin Witch before I do the rest of my errands.”

“Don’t forget me,” said Dorrie. “I’m helping with the balloons.”

“Hurry! Jump on and hold tight,” said the Big Witch. “The traffic is terrible.”

Witches and wizards swarmed in the air. They zigged, they zagged, they bumpted and tumbled and yelled. A wizard just missed them. “Out of my way, fools!”

“That was Wizard Knott,” said Dorrie. “He never gets cross. He didn’t even yell when Miss Malady’s goat ate his marigolds. Something strange is going on.”

“It isn’t strange at all! Don’t be a pest,” said the Big Witch as they landed near the Tower. “I’ll be back for you later.”

The doors were open. Witches and wizards rushed to and fro with shouts and cries. Squig and Mr. Obs were mending a torn banner. They grinned and waved at Dorrie and Gink. Dorrie waved back.

“At least those two aren’t crabby today, Gink,” said Dorrie as they made their way over to the balloon table.

Well! It’s about time,” snapped Miss Glitch “Start with the blue ones.”

“No!” yelled Plomm. “Red! Like this!” He blew and the balloon burst. Gink shot under the table.

“Nincompoop!” sneered Miss Glitch, aiming a kick at Plomm. A box of balloons spilled on the floor.

“Clumsy numskull!” yelled Plomm. He stamped his foot, just missing Gink’s tail.

Dorrie picked Gink up in her arms. “Com on, we’ll meet Mother at the Pin Witch’s shop,” she said, making her way out of the Tower. “Wer’re staying away from here. This kind of crabby is catching.

The sign in front of the shop read: GRAND OPENING! THIS WEEK ONLY! FREE CAPES AND SHAWLS AND HATS!

Inside, the shop was dark. A curtain was swept back, and the Pin Witch came out. “Who is in my shop?”

Dorrie jumped, “It’s me. I’m waiting for my mother.”

“Ohhh, what a dear little thing!” crooned the Pin Witch. Her cold fingers reached out and touched Dorrie’s face. Gink hissed and backed away.

“Ahh, a kitty, too! But we don’t want his nasty fur all over our pretty clothes, do we? You can both wait outside.” The Pin Witch disappeared behind the curtain.

Dorrie looked around for Gink. He was in the back of the shop. On a table nearby was a small cauldron with green stuff in the bottom, and a dish of pins, each with a spot of green on the tip. A few pins had fallen on the floor. As Dorrie picked one up, the Pin Witch called out, “Are you still in here, dearie?”

Dorrie dropped the pin in her pocket and picked up Gink. Quickly she slipped out of the shop.

Soon the Big Witch came out. “Can’t you stay out of trouble for two minutes, Dorrie? She yelled. “I told you to wait for me at the Tower!”

“But Mother, the . . . “

“Excuses, excuses! Get on this broomstick!”

The Big Witch flew home. She dumped Dorrie and Gink with a thump in the back yard, then flew off.

Dorrie opened the back door. “Are you still okay, Cook?”

“As far as I know,” said Cook. “Why?”

“Mother isn’t. She was, and then she wasn’t. Something strange is going on.” Dorrie told Cook about the quarrels at the Tower, and about the Pin Witch’s shop.

Cook shrugged. “well, there’s nothing we can do about it.”

Dorrie took the pin out of her pocket and looked at it. She got Cook’s old sweater and put it on. “Let’s see what happens when I put this pin in the sleeve,” she said.

Cook laughed. “What a zany idea!”

“Zany?” snapped Dorrie. “Don’t you call my ideas zany, you great overstuffed lobster!”

Cook tried to grab the sweater. “Don’t touch me, you muffin-headed monster!” shouted Dorrie, running into the hall. Around and around the house they went. Lamps and books and rugs tumbled, rumpled, and slid.

Cook stopped to catch her breath. Dorrie pulled off the sweater and threw it at her. “Take your old sweater. It’s too hot. It smells.”

Dorrie stood still. Her scowl melted away. Cook looked at her, panting. “That’s the answer,” said Dorrie.

“Cook, I have to figure out how to get all those magic pins out of the new clothes,” said Dorrie as they put everything back. “If people get any madder, they’ll start throwing spells at each other. We can’t let that happen. Will you fly me to the Ball, please?”

“Well, all right,” said Cook. “But you be careful.”

Through the night sky they flew. Ahead, the Town tower glowed with light.

Inside, no one was dancing. Everyone was quarreling. One wizard stopped fighting to mop his brow, then threw his cape aside. As Dorrie watched, his scowl turned to a smile. “Gink, that’s it!” she whispered. “if they get too warm, they’ll get rid of the clothes!”

Staying close to the walls, they went over to the musicians. Dorrie told Mr. Obs what she needed.

Soon Mr. Obs, Squig, Viola, and the Malady sisters began to play polkas fast and loud. The witches and wizards began to dance, but then they bumped, they pushed, they kicked and shoved.

“Oh, no!” Dorrie cried. “They’re too cross to dance. We have to do something else to heat them up . . . Heat! The furnace! Willi must be in the cellar. We’ll go find him.”

Dorrie and Gink hurried through the doorway that led to the cloakroom and the cellar. There in the dim light a witch was dancing by herself and cackling as she sang:

“Needles and pins! Needles and pins!

Crabby and cross, angry and mad –

These are the sounds that make me glad!

I who am my own invention

Thrive on uproar, strife, contention!

Needles and pins! Needles and pins!

This is how the Pin Witch wins!”

Dorrie and Gink sneaked past the Pin Witch and rand down the steps. Willi was asleep in his chair near the furnace.

“Willi, wake up,” said Dorrie. “it’s much too cold upstairs. Will you please turn the furnace up, way up?”

Willi yawned and nodded and turned the dial to eighty-five.

When they got back upstairs, the Pin Witch was nowhere in sight. Dorrie and Gink watched the crowd. As the room got hotter and hotter, off came the capes, the hats, the shawls. More witches and wizards stopped arguing and started dancing.

“Whew! It’s working, Gink,” said Dorrie.

The Big Witch had tossed her new cape over a chair. She saw Dorrie. “What are you doing here?” she said. “Why, how strange! I’m not cross! What . . . “

“The Pin Witch, Mother. She stuck magic pins in the clothes. Look! There she goes!”

The Pin Witch was dancing toward the door, singing:

“Away, away to another town,

Offering hat and cape and gown.

Whenever friends are being kind,

My magic pins will change their minds!”

The Big Witch turned to the crowd. “Now, the Witchville ‘Unity in Our Community’ song, please!”

They all sang. The Pin Witch threw up her hands. A shriek, a shower of pins, and she was gone.

Then everyone began to have a good time. Dorrie danced two polkas and a fandango with Mr. Obs. She was sure it was the bets ball Witchville had ever had.

Dorrie and Gink flew home holding tight to the Big Witch. Cook met them at the door.

“Everything is okay again,” said Dorrie. “Thank you for helping, Cook.”

“Tell me all about it while I make tea,” said Cook.

She took her sweater from the chair and put it on. All at once she banged the teakettle on the stove and yelled. “What do you mean, waking me up at this hour? What a nerve!”

“Mother, quick, the sweater!” shouted Dorrie.

Around and around the house they ran, up the stairs and down again. At last they cornered her in the hall. The Big Witch made a flying tackle and held Cook down while Dorrie pulled off the sweater.

They began to laugh. They laughed so hard their stomachs hurt. Still giggling, they went off to bed.
```

---

## IC-2222: Dreamland

- Title: Dreamland
- Author (byline): Sarah Dessen
- Work: Not specified
- Publisher: Speak
- Publication date as stated: May 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: CAITLIN, CASSANDRA, MOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1393
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sarah Dessen
ISBN: 978-0142401750
Publisher: Speak
Date (Month/Year): May 2004
```

### Introduction (context only: never use it for content warnings)

```text
As humans, we may want to focus on reality but sometimes catch ourselves. . . daydreaming. Daydreaming has the power to take us away from pushy parents, a difficult class at school, or work. But what if this semi-conscious dreamland is suddenly turned into a living nightmare?

In this selection, a nightmare slowly overtakes Caitlin who seeks out Rogerson as an escape from her reality: A missing sister, a withdrawn mother and an overall lackluster life. But she soon comes to realize that semi-conscious dreamlands aren’t always an escape.

Dreamland by Sarah Dessen
```

### Performance text (classify this)

```text
CAITLIN: My sister, Cassandra, had been the best at everything, even when it came to boys. She’d spend hours on the phone at night telling her latest boyfriend goodbye, this involving about twenty-I love you’s and pet names like “my little pumpkin“. Little did we know she was planning on leaving to be with her latest in California.

CASSANDRA: Oh, Caitlin, someday this will happen to you! You won’t feel like you’re missing out!

CAITLIN: God, I hope not. If I act like that, be sure to put me out of my misery.

But that was before I met Rogerson Biscoe. He was standing next to this black BMW; brown mass of curls; so mysterious and very different. I had never seen any other guy like him and at that moment, I could see myself setting across uncharted territory, places I’d never been or seen or even heard of. My world was suddenly wide and limitless, and I was ready.

CAITLIN: I was hooked on him. With Rogerson I was someone else. There were so many things I already loved about him. The smell of his skin, the way he pressed his hand in to the small of my back, whenever I walked into any place with him. And he was so attentive, always keeping one eye on me regardless of what else he was doing.

Since Cassandra was gone, my parents thought it would be good for me to join something. My making cheerleader changed my mother’s life. But the truth was, I hated cheerleading. Whatever pep the other girls had was missing in me, like a genetic or chemical malfunction.

I felt like an imposter, and it showed. And after Rogerson and I started going together, cheerleading meant nothing to me.

Rogerson was always there. He drove me home everyday. And we never really went on dates. With Rogerson, it was all about being in motion. Going from party to party, place to place. And, of course, there were the drugs. Rogerson operated a brisk business selling pot and other various illegals to the kids around town. The more I was around Rogerson, the less I became involved with my friend Rina and cheerleading.

Sometimes, however, Rogerson wouldn’t talk and he just wanted to be near me. It was never clear. But I did know this: he was quiet and never spoke without thinking. That he drove like a maniac. That the only time I saw the small simmering of temper behind his cool demeanor was when someone was late or not where they said they’d be. He was punctual to the second.

And I guess that’s what made my perfect relationship slide on through. Everything was perfect... before I missed his ride to the Winter Athletic Ceremony at school. Before he hit me. It was like a crack, like a gunshot. And it wasn’t like in the movies, where the person just stands there and takes it. I reeled back hitting my head against the seat of his car. He acted like what he had done was my fault. And after that, he drove me home, like nothing had happened, nothing at all.

It was during this time that I took up photography. Despite the fact that cheerleading was going from bad to worse, taking pictures was the first thing I had done in a long time that I was truly proud of. Until Rogerson saw me talking to my photography class instructor. He punched me in the jaw as soon as I got in his car. I convinced my mother when I got home that I had “slipped on the ice” by the mailbox.

MOTHER: It’s just so red. You must have hit so hard.

CAITLIN: I felt as if I couldn’t tell anyone about Rogerson-as long as I didn’t say it out loud, it wasn’t real.

As if by silent agreement since that night, Rogerson had taken only to hitting me where I could cover it. I wore only long-sleeved shirts, big sweaters, and turtlenecks, but at least now my face was off-limits.

On Christmas Eve, he gave me this beautiful silver necklace and that night, I slept with him for the first time. It was then that I gave him all of me, believing that I could trust him.

There was no pattern, no way of knowing when to expect it. Whenever he did hit me, I could count on a 24-hour safe period, which I had come to rely on, like home base. Those were the good days. But no matter what we were doing, the fact that he hit me was always on my mind.

One day, he was working on his car and I glanced at my reflection in the chrome of the bumper in front of me: skinny, long baggy shirt hiding the bruises across my skin and bones like a road map of all that had happened, every mile of the journey. And it was getting harder to hide.

See, my family always has this April Fool’s Party in the backyard, a small neighborhood get-together and my mom was just so determined to get me to wear this short white swooshy-skirted dress. It was beautiful, the kind of dress you wore with bare legs, uncovered arms, and white strappy sandals.

MOTHER: I’m concerned, Caitlin. All you ever wear now is black. An occasional red or white, but that’s it. You know how nice you always looked in blue.

CAITLIN: And I kept thinking, ‘I still do, look here, on the back of my wrist, those two spots the size of fingertips. Or here at the base of my back; that’s blue, too.’ I looked up into her face, but she didn’t seem to see me, even as I pleaded that she would.

My parents had no idea until the night of that party. Rogerson and I were supposed to hang out that day, but Rina had kidnapped me, taking me to the lake. I tried calling him, many times, but he just wouldn’t pick up.

I arrived home late, and his car was already parked in front. It didn’t take him long to start grabbing at me, pushing me around. His fist came and hit me right over my left eye and that’s when I slid down onto the grass and stayed there. I tried rolling away from him, but everything hurt all at once; my face, my fingers, the back of my head, the skin itself. Each place he’d ever struck me, like old war wounds on rainy days.

He was still pleading with me to get up when my mother came running outside. She wrapped her arms around me, trying to find a spot that wasn’t hurt. And even after my father called the police and they led Rogerson away, I still pulled out of the hands of all my family and friends, sobbing, screaming, everything hurting, to try and make him stay.

After that night, when my dreams of Rogerson were finally shattered, I was admitted into the Evergreen Care Center. The irony in this is just a few years back my sister and I had made fun of their slogan, “We can’t heal you at Evergreen, but we can help you heal yourself.“ I’d cried for Rogerson and for myself. How had I let it get so far? It was easier to take the days in tiny swallows, rather than biting everything off at once, and I was learning how to heal myself day by day with the help of my many visitors who cared so much about me.

A month went by and they finally decided I was well enough to go home. Before stepping outside my room, I looked up at my mirror. I looked so different from the day I’d arrived. I’d gained weight, my hair was longer, my skin clearer. I lowered my camera to my waist, tilting it upward. Then I put my finger on the shutter and smiled at the girl in the mirror. She smiled back, and I knew she understood it all, what I had gone through to make it this far. This is who I wanted to be. This was the person who I needed to become. So I kept my eyes on hers, steady, and pressed down on the button of the camera to catch this final face.

Click.
```

---

## IC-2223: The End of Aaron

- Title: The End of Aaron
- Author (byline): David James Poissant
- Work: The Heaven of Animals, Pgs 63-77
- Publisher: Simon and Schuster
- Publication date as stated: Mar 2014
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: GRACE, AARON, MANDY
- Teaser before the introduction: Yes
- Spoken words (computed): 1985
- Already set (do not supply): none

### Source block (context only)

```text
Author: David James Poissant
Book: The Heaven of Animals, Pgs 63-77
ISBN: 978-1476729961
Publisher: Simon and Schuster
Date (Month/Year): Mar 2014
```

### Introduction (context only: never use it for content warnings)

```text
Aaron has suffered from paranoid disorders since childhood. Choosing again to stop taking his medication, he is in the middle of another mental health crisis and has locked himself in the basement of his home to escape the apocalypse he believes is imminent. Can his girlfriend Grace convince save him from himself or will this be . . .

The End of Aaron by David James Poissant
```

### Performance text (classify this)

```text
GRACE: (Pg 63-77) Aaron calls to say we’re running out of time,

AARON: Grace, get ten—twenty—gallons of water, eight rolls of duct tape, five pounds of jerky, and a pear. I like pears.

GRACE: And I know we’re going to have to do it all over again -- the collecting, the hiding, the waiting to come out. For Aaron, the world is always ending. It’s the third time this year, and it’s only July. Probably he’s off his meds. (beat) Used to be, he’d warn me.

AARON: I’m just going to try. Just for a week or two.

GRACE: When I stopped supporting these experiments, he stopped telling me. Now, I have to guess, which isn’t hard given the things that come out of his mouth. The trick is figuring out how long he’s been off.

GRACE: First, he’ll feel nothing. Then, week two will hit, and like clockwork, Aaron will start in on that year’s fear. It wasn’t always the end of the world. For a while, Aaron was afraid to leave the house. Then there was the year of the bees. When he was a child, a bee sting put him in the hospital for two days. Now, everywhere he goes, there’s an EpiPen in his pocket. Aaron gets stung, he has less than a minute to plunge the needle into his leg before his throat swells shut. He’s only been stung the one time, but twice he’s put himself back in the hospital.

I blame his parents. Not for the depression—I mean, maybe that’s their fault. Maybe there’s something messed up with their genes. I don’t know. I only know that his folks bought into the whole Y2K thing, and Aaron’s never been the same since.

Imagine it: You’re eight years old, it’s New Year’s Eve and, instead of watching the ball drop with your parents, you’re huddled in the basement, stocked with two years’ worth of water, batteries, and green beans, watching your mom cry. Upstairs, Dick Clark counts down. Downstairs, you shut your eyes and wait for the end of the world. Aaron’s been waiting ever since.

I’ve known Aaron most of his life. Truth is, we’re twenty and we live with our parents, but that’s okay because we have each other, and I’ve come to believe that each other is enough.

I get everything on Aaron’s list. His therapist calls this enabling. I call it love. Home, I pop the trunk. It’s got a dozen gallons in it, and I grab the first two. I start up the front steps and almost kick over the jar -- a mason jar fat with amber, lid collared by a yellow bow—a thank-you for ignoring the bees. A while back, the woman next door set up a hive. Aaron’s mom petitioned the homeowners association, but the HOA let the lady keep her bees, provided no one got stung, and, in two years, no one has. And now we get honey.

I find Aaron in the basement where he lives. The clothes he has on are the clothes he wore yesterday, and I wonder how long it’s been since he slept.

AARON: Come on, come on!

GRACE: He pulls the jar from my hand, and I run back to the car and unload the gallons. I make half a dozen trips up and down the stairs, carrying water, the rolls of tape, the jerky in its five-pound bag. And Aaron stocks his pantry. When I come down the stairs with the last gallon of water Aaron is crying.

AARON: (screaming and sobbing) There’s no room. There’s no more room!

GRACE: I touch his shoulder and he turns, wild-eyed. I hold up the last gallon. (to Aaron) We can slide it under the bed.

(to audience) How, you’re wondering. How could she love a man who yells, who cries, who makes her carry jugs of water up and down the stairs? But you’re only seeing Aaron unwell. Aaron at his best is better than anyone I’ve ever known. He’s gentle. He’s kind. But those are just words. Here’s a story: I’m twelve, and, one day, this girl, Mandy Templeton, empties her carton of milk onto my tray and floods my lunch.

MANDY: What’re you gonna do, cry about it?

GRACE: We’re at that age where, at lunch, boys sit with boys and girls sit with girls, but Aaron hears this; walks over. He taps Mandy Templeton on the shoulder, and, when she turns, he punches her, hard as he can, right in the mouth. Mandy’s teeth never looked right afterward, and no one ever messed with Aaron again.

Aaron’s always worked that way. And if the trade-off is that, a few weeks a year, he goes cuckoo, then that’s a trade-off I’m willing to take. And so I buy the water. I tape the windows. I hunker down with Aaron, and, when I can, I get him to take his medication, knowing that, in a few days, it will kick back in and the man I love will come bubbling up from the ocean floor. He’ll break the surface.

Aaron uncaps the honey jar and sticks a finger in. He doesn’t offer me any, and I don’t ask. (to Aaron) So . . . How do you know? (to audience) I may as well be asking a toddler how the spaghetti sauce got all over the walls.

AARON: I can feel it.

GRACE: (to Aaron) How does it happen? (to audience) Aaron turns the TV on. According to the news, there’s been a strike in Pakistan. Something to do with American missiles. and the threat of nuclear armament. It’s all the evidence Aaron needs.

AARON: If there’s a detonation, even a hundred miles away, the fallout alone will keep us underground for ten years.

GRACE: I don’t know where Aaron gets his information. Maybe he makes stuff up. Maybe he’s trying to scare me, or maybe he believes what he says. Aaron changes the channel. More Middle East, more death. The pill bottle is on the dresser. I reach it and uncap it. The next part, I have to be careful.

(to Aaron) How about some medicine, sweetie. (to audience) And Aaron knocks the bottle from my hand. The first pill’s the hardest, but it’s only the beginning.

They’re antipsychotics, not miracle drugs, and sometimes it’s a week before they kick in. Even if I can get this one into him, I have a long road ahead of me. I stand, hands on my hips. Aaron pops the pill.

I brush my teeth over the kitchen sink and when I move back to the bed, Aaron’s already asleep. It’s almost midnight when he wakes. I tell him to take another pill, and I hear him move to the pantry, hear the honey jar lid come unscrewed followed by a quiet, occasional slurping. (to Aaron) Wake me up for the end of the world.

AARON: Don’t worry, I will

GRACE: -- no trace of irony, sarcasm, any of it. Maybe it’s going to be an easy one. In March, Aaron and I spent an afternoon under the bed. In May, he stayed in the basement, lights off, for a week. But I know that, one of these times, it’s not going to be easy. One of these days, no matter what I do, I won’t be able to get Aaron back on his meds. (beat) The end of the world? It could happen. No one’s denying that. But it’s the end of Aaron that scares me.

I wake. I turn to put my arm around Aaron, but all I get is pillow. The TV’s off. It’s still dark outside. I check under the bed. I check the cabinet below the kitchen sink. Aaron doesn’t leave the basement, not when he’s like this. This is new, and new is scary. There’s a sock on his dresser, weirdly out of place. Beneath the sock, I find the pills, chalky, deformed, and I wonder how long each stayed tucked under his tongue before I looked away. This worries me, but not as much as the honey jar -- empty, licked clean.

I tell myself no way could he be where I think he is, but, nights like this, I know better than to underestimate Aaron. I’m up the stairs in seconds, out the door and running through the yard. The garage door is up. Gardening tools scatter the driveway like a tornado came. I run faster, into the neighbor’s yard. The perimeter is a fence of wood planks too high to climb, but an open gate tells me which way Aaron went. A floodlight flicks on. And there is Aaron. And there is the hive -- a white, wooden box half a coffin in length.

I don’t see any bees. No, what I see is Aaron with a rake in his hands in what I can only guess is an attempt to pry open the lid. The rake quivers in his hands. He’s got an EpiPen in each leg. I don’t know what a jarful of honey and two shots of adrenaline do to a man, but Aaron doesn’t look good. He shakes, almost convulsing.

I could call 911. I could run back to the house and pick up the phone, but by then it would be too late. “Aaron,” I say, and he jumps. I take a step closer. I don’t want to scare him. I don’t want him making any sudden moves. From somewhere, a bee rises and swims, lazy, in the air around us.

AARON: I wanted to surprise you.

GRACE: His arms tremble and the rake scrapes the box. (to Aaron) Aaron, I want you to put the rake down. Now. (to audience) Perhaps, at night, the bees go to bed and don’t fly and don’t sting. God, I want to believe it. I take another step forward.

AARON: (shrieking) Stop!

GRACE: I hold up my hands like a bank teller on the wrong end of a gun.

AARON: (crying) I ate all the honey, it’s not fair. You didn’t get any.

GRACE: I take another step. (to Aaron) I’m fine. I don’t even like honey all that much. (to audience) The rake slaps the hive and rattles the lid. A bee lands on the rake, then lifts back into the sky. Another circles Aaron’s head. I’m close. If I lunged, I could grab the rake. I think I could take him down, but what will it mean if I’m wrong.

A hum has started in the box, and that can’t be good. (to Aaron) Aaron, I want you to put the rake down and come inside. (to audience) He’s looking right at me, but it’s like he can’t hear me, can’t hear past the grim determination to do the thing he set out to do. (beat) It’s my fault. I shouldn’t have slept.

AARON: (voice garbled and far-away) Once the bombs fall, there won’t be any honey. It’s for you . . . All of the honey . . . for you.

GRACE: There are bees in his hair, bees covering the lid of the box. Their wings shine like diamonds in the security lights, and I give up the hope that Aaron hasn’t been stung. I leap. I knock Aaron to the ground and pry the rake from his hands. I fling it like a javelin across the yard, far from the hive, and I sit on Aaron’s chest, hands pinning his wrists to the lawn.

They say that, with enough adrenaline, you can do anything. You hear stories of mothers lifting cars off their kids. I’m on top of Aaron, but I see too late that the weight of my body is nothing compared to what courses through his veins.

And then I’m in the air. I’m falling and I hit something, hard. The hive comes apart, the buzz turns to roar, and the moon, like magic, goes out of the sky. I hear grunting and turn to see Aaron dragging himself toward me on his elbows, like a soldier passing beneath barbed wire.

I feel a sting, then another. My legs are lightning, and, soon, I can’t even look at Aaron, who’s no longer crawling, but rolling, a man on fire. I look up and the swarm descends, looking like the end of the world.
```

---

## IC-2224: Endangered Species: Case 47401

- Title: Endangered Species: Case 47401
- Author (byline): Crystal Wilkinson
- Work: The Best Short Stories 2021
- Publisher: Anchor
- Publication date as stated: Sept 2021
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: SPEAKER, WHITE WOMAN, OFFICER
- Teaser before the introduction: Yes
- Spoken words (computed): 1598
- Already set (do not supply): none

### Source block (context only)

```text
Author: Crystal Wilkinson
Book: The Best Short Stories 2021
ISBN: 978-0593311257
Publisher: Anchor
Date (Month/Year): Sept 2021
```

### Introduction (context only: never use it for content warnings)

```text
Living at the intersection of racism and sexism is far from easy. We are discriminated against for being Black and for being women, existing in both identities at all times. The story of Black women at work and in life is one of resilience. Despite the challenges and barriers in our way, we have accomplished so much and continue to make amazing strides. But it’s time to acknowledge it is (insert year) and systemic racism is not a thing of the past. It is up close and

personal in the present.

Endangered Species: Case 47401 by Crystal Wilkinson
```

### Performance text (classify this)

```text
SPEAKER: All black women got this thrumming inside us, but don’t nobody notice. That thrum just sits in our bellies and then one day it comes on so strong that we can’t stop it even if we want to. And that’s when your abusive husband might get shot. That’s when she might quit that stupid job with the manager who says she can’t wear dreadlocks. That’s when she be in the corner curled up crying her eyes out over somebody black she don’t even know that got killed somewhere (beat) again. You might see her on the front lines of a protest—loud and regal and effective. What you don’t realize is that this thrum been with us always.

SPEAKER: I was cooking breakfast that morning in my new kitchen. Out the window was six stray cats preening and stretching in the back yard. A gray one was perched on the patio chair, fat and round, looking proud of itself. The cats came to the backyard nearly every day to make themselves known. They’d been there since we moved in two months [ago]. Later that morning, Little V played on the carpet in the living room while I slung cardboard boxes into a corner of the garage and scattered my prized possessions around me in a circle on the kitchen floor. I was just standing there looking at all my heirlooms when I saw a white woman traipsing up our sidewalk, looking like an after school special with that blonde hair curled around her chin. Green sweater with bright red apples, plaid culottes and white stockings. The doorbell rang just as I was wondering if she had the right address. (Speaker opens the door slightly, cautiously)

WHITE WOMAN: Are you the lady of the house?

SPEAKER: I am. (holding the door open just a little)

WHITE WOMAN: Can we count on you? (shoving a clipboard through the crack in the door)

SPEAKER: A man across the street was sweeping his sidewalk. A woman was ushering a girl into a waiting car. An old woman was sitting on a porch in a rocking chair holding a dog. They were all watching. They were all white people. I didn’t say nothing, but the thrum was shifting. I took the petition, thanked the woman and shut my door. (reading the petition)

(picks up Little V and speaks to him) What kind of people write a petition to kill cats? Little V looked up at me just like he knew what I was talking about. My sweet, sweet boy. If them cats had been house cats they would have been something else. Magnificent. The black one lounging on the arms of a couch, a man rubbing on its head, or a girl cradling the yellow one, like a doll while she watched some cartoons. But they were feral, at least that’s what that white woman had called them, but I didn’t see too much wild about them.

After that, I went out into the garage for more boxes. That’s when I saw a mouse. A different kind of woman would have screamed bloody murder, but I didn’t. I knew if I could have gotten close, I could have crushed him with one stomp from my shoe. But that mouse, just like them cats, just like me, wasn’t bothering nobody so I left him alone. It wasn’t but a few seconds later, that the doorbell rang again. Here come this white woman with her cat killing petition at my door a second time. Sometimes I just sit back and try to imagine a whole room of white people sitting around in a meeting talking about killing cats. Is that what y’all doing when so many black people are on cooling boards all over this country?

WHITE WOMAN: (opening the door and letting herself in) Lady of the house?

SPEAKER: (low and slow) How you just come up in somebody’s house, lady? (to audience) I knew this wasn’t going to turn out right. I knew it from that moment.

WHITE WOMAN: We need 50 more signatures. Have you had time to consider our materials?

SPEAKER: (obviously perturbed) I don’t have time. (to audience) And as I was trying to close my door she stuck her foot right in my front door. Yes. Can you believe it?

WHITE WOMAN: How long have you lived here?

SPEAKER: And had the nerve to raise her pen up above her clipboard like this, like she was about to write down whatever I said. “What?” That’s what I said. “What?!” Just like that.

WHITE WOMAN: Do you have a copy of a mortgage or lease that I could see?

SPEAKER: I leaned my face toward hers and I’m not lying when I tell you that I wanted the tip of my nose to touch the tip of hers to make sure I heard her right. “What did you say? Do I have what?” (to audience) She repeated herself then got a little scared look on her face, before she stepped back and removed her foot. I slammed the door closed, but before I could lock it the woman grabbed the door knob and turned it. With Little V in my arms I was losing this game of tug of war. And let me be clear -- my thrumming was there constantly. She yanked the door open wider and stepped one foot back in. Then come this wooshing feeling just beneath my heart. Woosh, woosh. Now I’m telling you, it was never my intention to lay hands on that funny looking white woman but when she wouldn’t remove her foot from my door, I pushed her out as hard as I could. Yes, I did that. I sure did. I pushed her out of my door. She tumbled to the sidewalk. Her pen went one way and her clipboard went another. but she wasn’t dead. And you and I know she ain’t dead now. I ain’t killed nobody. Right? I closed my door and locked it. Ain’t that what people do all over the world? Close their door, lock it, and think they’re safe?

WHITE WOMAN: (banging on the door and yelling) We’ll see about this!

SPEAKER: And then suddenly it was quiet again. (beat) Little V played peek-a-boo with me, while I worked in the kitchen, his curly head bobbing back and forth from view. A little while after that is when the police showed up. (she turns and opens the door)

OFFICER: Ma’am, we’ve had a report of a situation here.

SPEAKER: The officer was standing at my front door with his hand on his gun. Can you imagine somebody at your front door with a gun when you ain’t been in no situation with no police your whole damn life?

OFFICER: May I ask what you are doing in this house, ma’am? We are going to need you to step out here to the sidewalk.

SPEAKER: (shocked and stammer for words) What? . . . I don’t understand . . . I – I - live here.

OFFICER: Well, some of the folks around here said that they don’t think you live here. Do you have any proof? And they saw you assault a woman here, not too long ago. We are looking for the victim. (more forcefully) Step out of the house, please.

SPEAKER: The victim?! I live here! (to audience) If there had been room for laughter, I sure would have laughed but I stayed quiet. I bounced Little V on my hip and moved him to the other side and my brain was fogged up. But mostly it was my legs that wouldn’t act right or move fast enough.

OFFICER: Was there a woman here. A white woman?

SPEAKER: (dazed) Yes. Blonde. Talking about killing cats.

OFFICER: Tell us what happened.

SPEAKER: I started at the beginning, but by then my thrum was threatening to leave my body -- growing and pulsing. I talked about history, my mama. I told them about the birth of my children. I told them about that boy in the park who had been shot because he was holding a toy gun up in Cleveland. I told them about that famous singer who had raped all them young black girls and nobody had done nothing in Chicago. I told them about the woman who had died in the jail in Texas. “You know good and well that woman didn’t kill herself,” I said. I told them about the three-year-old Minnesota girl who watched her mother’s boyfriend get shot to death by police. “This is why black people don’t trust white people or the police,” I said. When I got to the part of about the humming thing that lived inside the wombs of black women, the officers looked at each other. One looked surprised. The other one had a smirk on his face like that white boy from Covington had when he was talking to that Native American elder.

“Covington, Kentucky,” I said. I talked about Covington. I talked about Kentucky. I’m from Kentucky, too. Did you know that? I talked and talked but when I stopped to catch my breath the officer said

OFFICER: Ma’am, we’re going to have to ask you to put the baby down.

SPEAKER: He talked to me like I was a dog and not a woman. (beat) I know you think I’m crazy but I’m not. I didn’t say nothing else, but I wasn’t about to put Little V down. I’d hold him till his daddy and his sister came home if I had to. I’d hold him until the next time I saw my mama. I’d hold him until black people stopped dying in the streets. And that’s when I heard the thrum louder than I’d ever heard it before. I could feel it spreading through my entire body and then it left my body and floated like a summer storm above our heads, above the neighborhood, above the entire country. And one cop had his hand on his gun and the other one kept saying, “Ma’am I’m going to need you to put that boy down right now.” But I didn’t. I wasn’t going to ever let go of my baby. Not until all my people were free.
```

---

## IC-2225: Everyday Use

- Title: Everyday Use
- Author (byline): Alice Walker
- Work: Not specified
- Publisher: Rutgers University Press
- Publication date as stated: May 1994
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2310
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alice Walker
ISBN: 978-0813520766
Publisher: Rutgers University Press
Date (Month/Year): May 1994
```

### Introduction (context only: never use it for content warnings)

```text
Quite often, growing up also means growing away. As the apron strings are unknotted, children must learn to depend less and less on their parents who must, in turn, allow their children to lead their own lives. As the child becomes her own person she can take the lessons learned from childhood and put them into “Everyday Use” by Alice Walker.
```

### Performance text (classify this)

```text
You've no doubt seen those TV shows where the child who has "made it" is confronted, as a surprise, by her own mother and father, tottering in weakly from backstage. (A pleasant surprise, of course: What would they do if parent and child came on the show only to curse out and insult each other?) On TV mother and child embrace and smile into each other's faces. Sometimes the mother and father weep, the child wraps them in her arms and leans across the table to tell how she would not have made it without their help. I have seen these programs.

Sometimes I dream a dream in which Dee and I are suddenly brought together on a TV program of this sort. I am ushered into a bright room filled with many people. There I meet a smiling, gray, sporty man like Johnny Carson who shakes my hand and tells me what a fine girl I have. Then we are on the stage and Dee is embracing me with tears in her eyes.

In real life I am a large, big-boned woman with rough, man-working hands. My fat keeps me hot in zero weather. I can work outside all day, breaking ice to get water for washing But of course all this does not show on television. I am the way my daughter would want me to be: a hundred pounds lighter. My hair glistens in the hot bright lights. Johnny Carson has much to do to keep up with my quick and witty tongue.

But that is a mistake. I know even before I wake up. Who ever knew a Johnson with a quick tongue? Who can even imagine me looking a strange white man in the eye? Dee, though. She would always look anyone in the eye. Hesitation was no part of her nature.

"How do I look, Mama?" Maggie says, showing just enough of her thin body for me to know she's there,

"Come out into the yard," I say.

Have you ever seen a lame animal, perhaps a dog run over by some careless person rich enough to own a car, sidle up to someone who is ignorant enough to be kind to him? That is the way my Maggie walks. She has been like this, chin on chest, eyes on ground, feet in shuffle, ever since the fire that burned the other house to the ground.

Dee is lighter than Maggie, with nicer hair and a fuller figure. She's a woman now, though sometimes I forget. How long ago was it that the other house burned? Ten, twelve years? Sometimes I can still hear the flames I can see Dee standing back; a look of concentration on her face as she watched the last dingy gray board of the house fall in toward the red-hot brick chimney. She had hated the house that much. Dee wanted nice things. A yellow organdy dress to wear to her graduation from high school; black pumps to match a green suit she'd made from an old suit somebody gave me. At sixteen she had a style of her own: and knew what style was.

I never had an education myself. After second grade the school was closed down. Don't ask me why: in 1927 colored asked fewer questions than they do now.. I was always better at a man's job anyway.

I have deliberately turned my back on the house. It is three rooms, just like the one that burned, except the roof is tin; they don't make shingle roofs any more. This house is in a pasture, too, like the other one. No doubt when Dee sees it she will want to tear it down. She wrote me once that no matter where we "choose" to live, she will manage to come see us. But she will never bring her friends. When she comes I will meet—but there they are!

It is hard to see them clearly through the strong sun. From one side of the car comes a short, stocky man. Hair is all over his head a foot long and hanging from his chin like a kinky mule tail. I hear Maggie suck in her breath. "Uhnnnh, " is what it sounds like. Like when you see the wriggling end of a snake just in front of your foot on the road. "Uhnnnh."

Dee next. A dress down to the ground, in this hot weather. A dress so loud it hurts my eyes. There are yellows and oranges enough to throw back the light of the sun. I feel my whole face warming from the heat waves it throws out.. The dress is loose and flows, and as she walks closer, I like it. I hear Maggie go "Uhnnnh" again.

"Wasuzo-Teano!" she says, coming on in that gliding way the dress makes her move. The short stocky fellow with the hair to his navel is all grinning and he follows up with "Asalamalakim, my mother and sister!" He moves to hug Maggie but she falls back, right up against the back of my chair. I feel her trembling there and when I look up I see the perspiration falling off her chin.

"Don't get up," says Dee. Since I am stout it takes something of a push. You can see me trying to move a second or two before I make it. She turns, showing white heels through her sandals, and goes back to the car. Out she peeks next with a Polaroid. She stoops down quickly and lines up picture after picture of me sitting there in front of the house with Maggie cowering behind me. She never takes a shot without making sure the house is included. Then she puts the Polaroid in the back seat of the car, and comes up and kisses me on the forehead.

"Well," I say. "Dee."

"No, Mama," she says. "Not 'Dee,' Wangero Leewanika Kemanjo!"

"What happened to 'Dee'?" I wanted to know.

"She's dead," Wangero said. "I couldn't bear it any longer, being named after the people who oppress me."

"You know as well as me you was named after your aunt Dicie," I said.

"But who was she named after?" asked Wangero.

"I guess after Grandma Dee," I said.

"And who was she named after?" asked Wangero.

"Her mother," I said, and saw Wangero was getting tired. "That's about as far back as I can trace it," I said. Though, in fact, I probably could have carried it back beyond the Civil War through the branches.

"Well," said Asalamalakim, "there you are."

"Uhnnnh," I heard Maggie say.

"There I was not," I said, "before 'Dicie' cropped up in our family, so why should I try to trace it that far back?"

He just stood there grinning, Every once in a while he and Wangero sent eye signals over my head. "How do you pronounce this name?" I asked. "You don't have to call me by it if you don't want to," said Wangero.

"Why shouldn't 1?" I asked. "If that's what you want us to call you, we'll call you."

"I know it might sound awkward at first," said Wangero.

"I'll get used to it," I said. "Ream it out again."

Well, soon we got the name out of the way. Asalamalakim had a name twice as long and three times as hard. After I tripped over it two or three times he told me to just call him Hakim-a-barber. I wanted to ask him was he a barber, but I didn't really think he was, so I didn't ask.

"You must belong to those beef-cattle peoples down the road," I said. They said "Asalamalakim" when they met you, too, but they didn't shake hands. Always too busy: feeding the cattle, fixing the fences, putting up salt-lick shelters, throwing down hay. Hakim-a-barber said, "I accept some of their doctrines, but farming and raising cattle is not my style." (They didn't tell me, and I didn't ask, whether Wangero (Dee) had really gone and married him.)

We sat down to eat and Wangero, went through the chitlins and com bread, the greens and everything else. She talked a blue streak over the sweet potatoes. Everything delighted her. Even the fact that we still used the benches her daddy made for the table when we couldn't afford to buy chairs.

"Oh, Mama!" she cried. "I never knew how lovely these benches are. You can feel the rump prints," she said, running her hands underneath her and along the bench. Then she gave a sigh and her hand closed over Grandma Dee's butter dish. "That's it!" she said. "I knew there was something I wanted to ask you if I could have." She jumped up from the table and went over in the corner where the churn stood, the milk in it crabber by now. She looked at the churn and looked at it.

"This churn top is what I need," she said. "Didn't Uncle Buddy whittle it out of a tree you all used to have?"

"Yes," I said.

"Un huh," she said happily. "And I want the dasher, too."

"Uncle Buddy whittle that, too?" asked the barber.

"Aunt Dee's first husband whittled the dash," said Maggie so low you almost couldn't hear her. "His name was Henry, but they called him Stash."

"Maggie's brain is like an elephant's," Wangero said, laughing. "I can use the chute top as a centerpiece for the alcove table," she said, "and I'll think of something artistic to do with the dasher."

When she finished wrapping the dasher the handle stuck out. I took it for a moment in my hands. You didn't even have to look close to see where hands pushing the dasher up and down to make butter had left a kind of sink in the wood. It was beautiful light yellow wood, from a tree that grew in the yard where Big Dee and Stash had lived.

After dinner Dee (Wangero) went to the trunk at the foot of my bed and started rifling through it. Maggie hung back in the kitchen over the dishpan. Out came Wangero with two quilts. They had been pieced by Grandma Dee and then Big Dee and me had hung them on the quilt frames on the front porch and quilted them. In both of them were scraps of dresses Grandma Dee had worn fifty and more years ago. Bits and pieces of Grandpa Jattell's Paisley shirts. And one teeny faded blue piece, about the size of a penny matchbox, that was from Great Grandpa Ezra's uniform that he wore in the Civil War.

"Mama," Wanegro said sweet as a bird. "Can I have these old quilts?"

I heard something fall in the kitchen, and a minute later the kitchen door slammed.

"Why don't you take one or two of the others?" I asked. "These old things was just done by me and Big Dee from some tops your grandma pieced before she died."

"No," said Wangero. "I don't want those. They are stitched around the borders by machine."

"That'll make them last better," I said.

"That's not the point," said Wangero. "These are all pieces of dresses Grandma used to wear. She did all this stitching by hand. Imag' ine!" She held the quilts securely in her arms, stroking them.

"The truth is," I said, "I promised to give them quilts to Maggie, for when she marries John Thomas." She gasped like a bee had stung her. "Maggie can't appreciate these quilts!" she said. "She'd probably be backward enough to put them to everyday use."

"I reckon she would," I said. "God knows I been saving 'em for long enough with nobody using 'em. I hope she will!"

"But they're priceless!" she was saying now, furiously; for she has a temper. "Maggie would put them on the bed and in five years they'd be in rags!”

"She can always make some more," I said. "Maggie knows how to quilt."

Dee (Wangero) looked at me with hatred. "You just will not understand. The point is these quilts, these quilts!"

"Well," I said, stumped. "What would you do with them?"

"Hang them," she said. As if that was the only thing you could do with quilts.

Maggie by now was standing in the door.

"She can have them, Mama," she said, like somebody used to never winning anything, or having anything reserved for her. "I can 'member Grandma Dee without the quilts."

I looked at her hard. It was Grandma Dee who taught her how to quilt herself. She looked at her sister with something like fear but she wasn't mad at her. This was Maggie's portion. This was the way she knew God to work.

When I looked at her like that something hit me in the top of my head and ran down to the soles of my feet. Just like when I'm in church and the spirit of God touches me and I get happy and shout. I did something I never done before: hugged Maggie to me, then dragged her on into the room, snatched the quilts out of Miss Wangero's hands and dumped them into Maggie's lap.

"Take one or two of the others," I said to Dee. But she turned without a word and went out to Hakim-a-barber.

"You just don't understand," she said, as Maggie and I came out to the car.

"What don't I understand?" I wanted to know.

"Your heritage," she said, and then she turned to Maggie and said, "You ought to try to make something of yourself, too, Maggie. It's really a new day for us. But from the way you and Mama still live you'd never know it." She kissed Maggie and left with the barber. Maggie smiled; a real smile, not scared. And then the two of us sat there just enjoying, until it was time to go in the house and go to bed.
```

---

## IC-2226: Expecting Adam

- Title: Expecting Adam
- Author (byline): Martha Beck
- Work: Not specified
- Publisher: Berkley Publishing Group
- Publication date as stated: Aug 2000
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: MARTHA, MRS. ROSS, MARTH
- Teaser before the introduction: Yes
- Spoken words (computed): 1589
- Already set (do not supply): none

### Source block (context only)

```text
Author: Martha Beck
ISBN: 978-0425174487
Publisher: Berkley Publishing Group
Date (Month/Year): Aug 2000
```

### Introduction (context only: never use it for content warnings)

```text
This is the story of two driven Harvard academics who found out in mid-pregnancy that their unborn son would be born with Downs Syndrome. To their own surprise and the horrified dismay of the university community, the couple ignored the abundant means, motive, and opportunity to obtain a therapeutic abortion. They decided to allow their baby to be born. What they did not realize is that they themselves were the ones who would be `born,' infants in a new world where magic is commonplace, Harvard professors are the slow learners, and babies with disabilities are the master teachers.

Expecting Adam by Martha Beck
```

### Performance text (classify this)

```text
MARTHA: (Pg 6-7) I wonder a lot of things, since Adam came along. I wonder about all the strange and beautiful and terrible things that accompanied him into my life.

MARTHA: (Pg 3-8) This happened when Adam was about three years old . . . I was sitting in a small apartment with a woman I had barely met, talking to her about her life. I'll call her Mrs. Ross. I had been doing similar interviews for months, collecting data for my Ph.D. dissertation. Mrs. Ross was a scrawny forty-five-year-old with a master's degree in art history and a job as an elementary school janitor. I was taking notes, considering what this woman's experience had to teach about the real-world value of the more refined academic fields, when she suddenly stopped talking. There was a moment of silence, and then I looked up and said, "Yes?" in a helpful voice, which was normally enough to keep an interview rolling. But Mrs. Ross wasn't acting normal. She had been sitting on a straight-backed wooden chair, both feet set firmly on the floor and her hands resting primly on her knees. Now she was curled into an almost fetal position, forearms crushed between the tops of her thighs and her chest, her eyes tightly closed. I became alarmed. (to Mrs. Ross) Are you all right?

MRS. ROSS: (waving her hand) I can't ... quite ... make it out. (gasping, her eyes closed) Usually I can tell which side of the veil it's coming from ... that's usually the first thing I can tell ... but this time I ... can't.

MARTHA: Uh-huh I said cautiously, glancing toward the door, wondering if I could get to it before Mrs. Ross leapt upon me like a mad dog.

MRS. ROSS: It's like ... he's not really on one side of the veil or the other ... maybe he's on both. (shakes her head) At least I know it's a he. (her eyes fly open) You know who it is! You know who it is, but you're blocking!

MARTHA: I know who?

MRS. ROSS: That's right! You see, I have this ... well, it's a gift. I get messages for people. (sighs) There was a point in my life when I stopped talking about it, you know, because it's very embarrassing. And then, you know, I began to lose it. It was getting fainter, and sometimes the spirits would be angry at me, because I wouldn't help them get through to people.

MARTH: (to audience) At this moment, I swear to God, a large green parrot walked out of Mrs. Ross's small kitchen and into the living room. It paced slowly across the carpet, peered at me suspiciously with one flinty eye, then proceeded on foot up the leg of Mrs. Ross's chair and onto her shoulder. She's a witch, I thought. I'm sitting here talking to a genuine witch. The parrot was obviously a familiar. I would have been willing to bet it was her husband.

MRS. ROSS: (stroking the bird absentmindedly) So I promised God that I would always deliver the messages as soon as I got them. No matter what.

MARTHA: (to audience) Four years earlier I would have dismissed Mrs. Ross and her "gift" immediately. Back then I had known exactly how the world worked. Back then I had been sure of my own intellect, sure of the primacy of Reason, sure that, given enough time and training, I could control my destiny. That was before Adam. But now it was four years later, and Adam was at home with the baby-sitter, and I had learned a lot about how much I had to learn. So I sat still and waited for Mrs. Ross to go on.

MRS. ROSS: The messages are usually from the other side of the veil—I mean, from the spirit world. Sometimes they're from living people who are far away and need to get a message through immediately. But that's always the first thing I can tell—which side of the veil the message is coming from. (frowning) And this time, I can't tell.

MARTHA: By now, I admit it, I was hooked. I wanted my message. (to Mrs. Ross helpfully) Just relax.

MRS. ROSS: (whispering) We should pray.

MARTHA: (to audience) So Mrs. Ross and I bowed our heads, and I drew a deep breath and relaxed for just a second, and then her head snapped up like a Pez dispenser

MRS. ROSS: All right, you stopped blocking. It's your son.

MARTHA: My son? (to audience) Even after everything that had already happened, this surprised me. I had been hoping the message would be from my guardian angel, or perhaps a stray ancestor with an interest in my career.

MRS. ROSS: You have a son who's halfway between worlds.

MARTHA: (to audience) I felt the hair go up on my arms. You see, no matter how much evidence you have, over time you tend to block out the experiences that aren't "normal." Who wants to turn into a Mrs. Ross, blurting out gibberish about spirits and veils? How much of that sort of conversation are you allowed before people stop inviting you to parties, and you end up pushing a mop in an elementary school? (to Mrs. Ross) Well, maybe I do have a son ... uh ... like that.

MRS. ROSS: (a withering look) You do. And he wants me to give you a message.

MARTHA: (to audience) By now my whole body was bristling with a strange electricity. The sensation had become familiar to me over the past few years, yet it was always a surprise. At least I kept my mouth shut.

MRS. ROSS: (closing her eyes) He says that he's been watching you very closely from both sides of the veil. He says that you shouldn't be so worried. He says you'll never be hurt as much by being open as you have been hurt by remaining closed.

MARTHA: That's it? (Mrs. Ross nods and smiles) What the heck is that supposed to mean?

MRS. ROSS: (shrugging) Beats me.

MARTHA: Oh, come on. There's got to be more. Ask him.

MRS. ROSS: I don't ask questions. I just deliver messages. Like Western Union. What the messages mean is none of my business.

MARTHA: (to audience) And that was all she had to say. After a pathetic attempt to pretend I was still conducting an interview, I raced home to confront Adam. He was in his crib, asleep. He was about half the size of a normal three-year-old, had barely learned to walk, and had never spoken an intelligible word. I reached down and poked him in the tummy, and he woke up with his usual jolly grin on his face. I looked into his small, slanted eyes. (to Adam) Adam, you've got to tell me. Are you sending me messages through Mrs. Ross? (to audience) His smile broadened. That was all. And he hasn't said a thing about it since. So here I am, still wondering what the hell happened that day, wondering whether Mrs. Ross was really channeling my three-year-old, wondering what he meant. I wonder a lot of things, since Adam came along. I wonder about all the strange and beautiful and terrible things that accompanied him into my life. My husband, John, knows about my wondering—shares it, in fact, since his life, too, was changed when we were expecting Adam. But when I wasn't talking to John, I learned to keep it all to myself. I learned to ignore the miraculous in my life, to pretend it didn't exist, to tell lies in order to be believed. In short, I kept myself closed.

This has not been easy. It is difficult not to tell people when one of your interview subjects turns out to be Parrot Woman. The strangeness, the curiosity, the wonder keeps pushing outward, begging to be communicated, needing air and company. On many occasions, I have tried to talk about Adam without letting on that I actually believed in everything that happened to me. I have written this book twice already, both times as a novel. You see, by calling it a novel, I could tell the story without putting myself in danger from skeptics, scientists, and intellectuals. "Fiction!" I would assure them. "Made it all up! Not a word of truth in it!" Then they would all go away and leave me alone, and perhaps a few sturdy souls would be willing to believe me, and I could open up in safety to them. It hasn't worked out that way. The editors and agents and writers I respect most have always come back, after reading my "novel," with the same question: "Excuse me, but how much of this is fiction?" And I would hem and haw a bit before admitting that aside from making John and myself sound much better-looking than we are, I didn't fictionalize anything. It's all true, I would say. Then I would sink into my chair five or six inches and wait for them to call security.

So far, that hasn't happened. It has been five years since Mrs. Ross delivered Adam's message, and in all that time my favorite people have continually repeated his advice. Open up, they say. It will feel better than remaining closed. I am none too sure about this. I am very much afraid of being caught in the firestorms of controversy over abortion, genetic engineering, medical ethics. It worries me to think that I will be lumped together with the right-to-lifers, not to mention every New Age crystal kisser who ever claimed to see an angel in the clouds over Sedona. I am reluctant to wave good-bye to my rationalist credibility. Nevertheless, the story will not stop unfolding, and it will not stop asking me to tell it. I have resisted it for what feels like a very long time, hoping it would back off and disappear. But it hasn't. So, Mrs. Ross, wherever you are, thank you for delivering my son's message. After all these years, I've finally decided to listen.
```

---

## IC-2227: Explaining Death to the Dog

- Title: Explaining Death to the Dog
- Author (byline): Susan Perabo
- Work: Who Was I Supposed to Be, Pgs 77-84
- Publisher: Simon & Schuster
- Publication date as stated: June 27, 2006
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: NARRATOR, TODD
- Teaser before the introduction: Yes
- Spoken words (computed): 2266
- Already set (do not supply): none

### Source block (context only)

```text
Author: Susan Perabo
Book: Who Was I Supposed to Be, Pgs 77-84
ISBN: 978-0743290371
Publisher: Simon & Schuster
Date (Month/Year): June 27, 2006
```

### Introduction (context only: never use it for content warnings)

```text
Explaining Death to the Dog by Susan Perabo
```

### Performance text (classify this)

```text
NARRATOR: (Pgs 77-84) After the baby died, I found it imperative that my German shepherd Stu understand and accept the concept of death. The first week wasn't so bad, what with all our friends and relatives around, smothering Stu with affection. And Todd was home from work that week, dumping well-meaning casseroles accidentally-on-purpose onto the kitchen floor for Stu to indulge in. So Stu didn't notice the absence so much, didn't seem to. He trotted around the house happily, oblivious to the fact that the baby, who he had had a big hand in raising, was missing.

Then the party ended. Guests cried the last of their tears at my front door, said "What a waste" for the thousandth and final time, and made their separate ways back to their separate lives, lives that sailed along quite smoothly despite the absence of the infant whom they had been mourning for a good seven or eight days.

Todd went back to work; packed up his briefcase and kissed me good-bye. He nearly tripped over Stu in his rush to get out of the house. He wanted away, wanted to get busy again. Stu and I stood at the window and watched him drive away. Stu looked up at me and then back at the empty driveway. He lay down on the floor in front of the window. I sat next to him and rubbed his stomach. He sighed.

NARRATOR: What to do with the baby dead? No diapers, no screaming, no feeding. What had I done before the baby? I had been pregnant. Pregnant for longer than she had been alive. And what had I done before I got pregnant? I tried to remember. I supposed I had cleaned the house. Cooked. Taken Stu to the park. It didn't seem like it could have been nearly enough to take up a whole day. In the afternoon I made myself a sandwich from one of the two whole hams that were still in the refrigerator and sat in front of the television. I waited for Stu, waited for him to emerge from wherever he was sleeping, jingling and jangling his way to a possible meal. The house was quiet. Still, very still. The morning the baby died Todd shook me awake to the stillness and said, "Listen, she's sleeping ... "

I set my sandwich on the coffee table and got up to look for Stu. I called him a few times. Nothing. I walked through the house, from room to room. I found him upstairs, in the baby's room. The room was empty, except for one chair. Todd and the relatives had cleaned it out the day of the funeral because they said it was just too sad to look at. They stashed the crib in the back of a stranger's car and carted it away, hid the dolls and mo-biles with the cobwebs in the basement. Then Todd's mother said the room looked so bare, so she had taken a chair from our bedroom and set it by the window. It looked unnatural by itself in the baby's room. Worse than bare. Just awkward.

Stu was lying in the middle of the empty room. His ears were back and his eyes open. He didn't raise his head when I came in. He just followed me with his eyes. (to the dog) Stu. Stu, what the hell are you doing? (to the audience) He looked like he had eaten too much casserole, was what it was, looked like he might toss his canine cookies at any moment. He stood up lazily. He walked in circles around the room. You could tell he was looking for the baby.

(to the dog) No. (patting his head) No more baby. Baby's gone. No baby. (to the audience) He looked at me with the universal blank dog look. He had no idea what I was talking about. It was then that I realized the impossibility of the situation. It wasn't even like trying to explain death to a child. The dog simply couldn't understand the language. He had a brain the size of a walnut and all he knew was that the baby wasn't where she was supposed to be. I imagined it must be even worse than knowing the baby was dead. At least Todd had been able to logically spell it out for me that morning to get me to stop shaking her and trying to wake her up, hold the little girl up in my face, point to the chest. NO BREATHING.

It was then I decided that I needed to teach Stu about death, whatever the cost. I figured he had a right to know, being a member of the family.

(to the dog) Come on, boy. (to the audience) On the coffee table we had a book. A big Life magazine book. Best of Life, something like that. I gave Stu part of my ham sandwich to lure him up on the couch with me. I opened the book out on the coffee table, paged through it, looking for the sixties, the best lesson of death on film. I turned the dog's head toward the contorted face of Lee Harvey Oswald, and the man behind him, a man whose name they never mentioned, looking like he might jump right out of his skin from the shock of it. Oswald was holding his stomach, hadn't even hit the floor.

(to the dog) Dead. Stu, it's dead. (to the audience) Stu didn't seem to see the picture. He looked at the book, sure, but there was nothing in his eyes that said that he saw the proverbial farm being bought. The way he looked at it, it could have been a picture of a rolling wheat field. I turned the page, looking for something bigger, and found a two-page spread from Memphis, 1968, the man dead on the balcony, people pointing out into the sky. It was big; you couldn't miss it.

(to the dog) Death. No more. (to the audience) Again Stu glanced at the picture, then back at my ham sandwich. I jabbed my finger on Martin Luther King, Jr., held the pic-ture up in Stu's face, and still his eyes didn't focus on it. What was I expecting? I don't know. If Todd had been there he would have clapped the book shut and told me the dog didn't know what the hell was going on and he'd be over it in a day and a half anyway. But Todd was gone. Strange things happen when you're alone in the house with pets all day . . .

In the middle of the night I woke up and heard the baby crying. I sat up and reached for my glasses before I remembered. It was not a staggering thing. It washed over me slowly, the way you remember what day it is when you wake up in the morning. I looked at Todd lying on his stomach next to me, the side of his face pressed to the pillow, his mouth open. The first week it was him who couldn't sleep. I'd open my eyes and he'd be sitting up in bed, his back against the wall, staring into space. The minister had come by and Todd told him about not being able to sleep. The minister said it was probably guilt, thinking that if he'd been awake when the baby started dying he could have done something about it. After that I guess Todd became comfortable with the guilt, because he didn't sit up nights anymore.

Todd? . . . Todd? (to the audience) I didn't have the courage to touch him, to wake him up and force him to share the grief, to try to explain to me why I might have heard the baby crying when the baby had been dead for over a week. I lay back down next to him and started thinking about the simplicity of a dog's mind. I tried to think of a way to explain to Stu just exactly what was going on.

The morning was cool and dark. It was May and the natural order of things said it should have been warm and bright. But the natural order of things was wrong, so it was ugly out. Todd sat at breakfast and looked at the newspaper in much the same way Stu had looked at the coffee table book. His spoon went from the cereal bowl to his mouth without being led by anything but habit. I stared at him and he didn't even notice.

NARRATOR: (to Todd) I think Stu misses the baby.

TODD: (looking up from the paper, his mouth open and his eyes empty. What?

NARRATOR: Yesterday he was lying in her room.

TODD: Close the door.

NARRATOR: I was thinking. I was trying to figure out how to get it across to him that she's not coming back.

TODD: Why would you think something like that?

NARRATOR: I just thought it was interesting. I wondered how dogs understand those kinds of things.

TODD: What are you doing today? Why don't you call somebody for lunch?

NARRATOR: No one wants to have lunch with me.

TODD: (sighing) We'll go out tonight, then.

NARRATOR: (to the audience) But he wasn't even looking at me. He was looking over my shoulder out the back door, out into the grayness that was passing itself off as morning.

I decided I would go ahead and take Stu to the park, force him down the slide for a good laugh, spin us both around on the merry-go-round just for a change of pace. There would be no baby carriage to drag through the sand, no need to worry about it slipping from my grip and ca-reening down a hill into the creek. The park was different with no baby. It seemed much safer.

Then we found the squirrel. Stu walked right past it, didn't even notice, but I saw it. It was lying on its side in the grass. Its mouth was open, its eyes empty holes. Other than that it was fine. Perfectly whole, not the work of a cat or a child with a BB gun.

(to the dog) Stu. Stu, come here baby. (to the audience) He stopped, turned back, then trotted to where I was kneeling on the ground. He saw the squirrel and stopped for a second. He looked at me. I reached out to touch the squirrel and Stu took a step back. Its fur was damp and brittle. Stu walked up to the squirrel, then turned his head away and looked at me like I had gotten him into something he wasn't near ready for. A fly landed on the squirrel's head and crawled into the empty eye socket.

(to the dog) Stu. This is important. (takes his head and turns it toward the rodent, pushing his nose closer to the body) The squirrel's dead. You understand? (to the audience) Squirrels, I could hear Stu thinking. I chase these things. This squirrel is not running. Stu backed away from the animal. I tried to hold on to him but he pulled me backward and I fell from my knees onto the wet grass. Stu ran in circles around me, afraid he was in trouble . . . So we were going to go out for dinner. Todd came home and sat on the couch in a heap. His tie was askew and his hair mussed. I asked him if he had a bad day and he said he was just a little tired. (to Todd) Does that mean we're not going to dinner?

TODD: (wearily) I didn't say that. I didn't say we weren't going out. (pause) Where do you want to go?

NARRATOR: We could go someplace fancy. We haven't been someplace fancy in a long time.

TODD: (noticing the dog) What's up with him?

NARRATOR: I told you. He's confused.

TODD: He's confused. The dog is confused. (shakes his head sadly)

NARRATOR: (to the audience) I was trying to think of a way to make a case for how confused Stu really was, but Todd didn't seem receptive to the idea.

TODD: (loosening his tie) Let me change. We'll go out. I just have to get out of these clothes.

NARRATOR: (to the audience) I sat on the couch with Stu and waited. Stu put his head on my thigh and looked up at me. I wanted to do something for him, take him out to dinner with us to get his mind off the mystery of the missing baby. We sat there for a few minutes. I couldn't hear any noises coming from the bedroom, so I got up and went down the hallway. I looked in the door and saw Todd sitting on the edge of the bed. He was banging the side of his head, crying while he was doing it. Actually he wasn't really crying. He was more making little howling noises with his throat. And he just kept whacking himself on the head.

I went back into the living room. I had a desire to get Stu off the couch and give him a push toward the bedroom, so he could stumble upon Todd and see what the death thing was all about, but I didn't have the heart . . .

I woke again in the middle of the night, but I didn't hear any crying. I got out of bed anyway and went into the baby's room. Stu hopped up and followed me, hopefully, but the room was still empty except for the chair by the window. Still, the dog wandered around, sniffing out the emptiness, the way he had the day before, and the day before that, and the way I realized he probably would for quite a while. I sat down in the chair by the window.

Everything was quiet, and I thought of saying to Stu that that was it, that was death, the quiet. But Stu was still sniffing around the room, trying to pick up the scent of the baby, and I realized he would never understand death. All he would come to understand was that the baby was not coming back.
```

---

## IC-2228: Extenuating Circumstances

- Title: Extenuating Circumstances
- Author (byline): Joyce Carol Oates
- Work: Haunted: Tales of the Grotesque
- Publisher: Dutton Books
- Publication date as stated: 1994
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1688
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joyce Carol Oates
Book: Haunted: Tales of the Grotesque
ISBN: 978-0525936558
Publisher: Dutton Books
Date (Month/Year): 1994
```

### Introduction (context only: never use it for content warnings)

```text
I offer you . . . . A mother's tale about murdering her two-year-old child and her reasons for doing so. Every sentence begins with "Because" and ends with a twisted explanation. For every action there is always a plethora of Extenuating Circumstances by Joyce Carol Oates.
```

### Performance text (classify this)

```text
• Because. it was a mercy.

• Because God even in His cruelty will sometimes grant mercy.

• Because Venus was in the sign of Sagittarius.

• Because you laughed at me, my faith in the stars. My hope.

• Because he cried, you do not know how he cried.

• Because at such times his little face was so twisted and hot, his nose running with mucus, his eyes so hurt.

• Because in such he was his mother, and not you.

• Because I wanted to spare him such shame.

• Because he remembered you, he knew the word Daddy.

• Because watching TV he would point to a man and say, Daddy-?

• Because this summer has gone on so long, and no rain. The heat lightning flashing at night, without thunder.

• Because in the silence, at night, the summer insects scream.

• Because by day there are earthmoving machines and grinders operating hour upon hour razing the woods next to the playground.

• Because the red dust got into our eyes, our mouths.

• Because he would whimper Mommy?-in that way that tore my heart.

• Because last Monday the washing machine broke down, I heard a loud thumping that scared me, The dirty soapy water would not drain out.

• Because in the light of the bulb overhead he saw me holding the wet sheets in my hand crying What can I do? what can I do?

• Because the sleeping pills they give me now are made of flour and chalk, I am certain.

• Because I loved you more than you loved me even from the first when your eyes moved on me like candleflame.

• Because I did not know this yet; yes I knew it but cast it from my mind.

• Because there was shame in it. Loving you knowing you would not love me enough.

• Because my job applications are laughed at for misspellings and torn to pieces as soon as I leave.

• Because they will not believe me when listing my skills. Because since he was born my body is misshapen, the pain is always there.

• Because I see that it was not his fault and even in that I could not spare him.

• Because even at the time when he was conceived (in those early days we were so happy! so happy I am certain! lying together on top of the bed the corduroy bedspread in that narrow jiggly bed hearing the rain on the roof that slanted down so you had to stoop being so tall and from outside on the street the roof with its dark shingles looking always wet was like a lowered brow over the win-dows on the third floor and the windows like squinty eyes and we would come home together from the University meeting at the Hardee's corner you from the geology lab or the library and me from Accounting where my eyes ached because of the lights with their dim flicker no one else could see and I was so happy your arm around my waist and mine around yours like any couple, like any college girl with her boy friend, and walking home, yes it was home, I thought always it was home, we would look up at the windows of the apartment laughing saying who do you think lives there? what are their names? who are they? that cozy secret-looking room under the eaves where the roof came down, came down dripping black runny water I hear now drumming on this roof but only if I fall asleep during the day with my clothes on so tired so exhausted and when I wake up there is no rain, only the earthmoving machines and grinders in the woods so I must acknowledge It is another time, it is time) yes I knew.

• Because you did not want him to be born.

• Because he cried so I could hear him through the shut door, through all the doors.

• Because I did not want him to be Mommy, I wanted him to be Daddy in his strength.

• Because this washcloth in my hand was in my hand when I saw how it must be.

• Because the checks come to me from the lawyer's office not from you.

• Because in tearing open the envelopes my fingers shaking and my eyes showing such hope I revealed myself naked to myself so many times.

• Because to this shame he was a witness, he saw.

• Because he was too young at two years to know. Because even so he knew.

• Because his birthday was a sign, falling in the midst of Pisces. Because in certain things he was his father, that knowledge in eyes that went beyond me in mockery of me.

• Because one day he would laugh, too, as you have done.

• Because there is no listing for your telephone and the operators will not tell me.

• Because in any of the places I know to find you, you cannot be found.

• Because your sister has lied to my face, to mislead me.

• Because she who was once my friend, I believed, was never my friend.

• Because I feared loving him too much, and in that weakness failing to protect him from hurt.

• Because his crying tore my heart but angered me too, so I feared laying hands upon him wild and unplanned.

• Because he flinched seeing me. That nerve jumping in his eye.

• Because he was always hurting himself, he was so clumsy falling off the swing hitting his head against the metal post so one of the other mothers saw and cried out Oh.' oh look your son is bleeding! and that time in the kitchen whining and pulling at me in a bad temper reaching up to grab the pot handle and almost overturning the boiling water in his face so I lost control slapping him shaking him by the arm Bad! bad! bad! bad! my voice rising in fury not caring who heard.

• Because that day in the courtroom you refused to look at me your face shut like a fist against me and your lawyer too, like I was dirt beneath your shoes. Like maybe he was not even your son but you would sign the papers as if he was, you are so superior.

• Because the courtroom was not like any courtroom I had a right to expect, not a big dignified courtroom like on TV just a room with a judge's desk and three rows of six seats each and not a single window and even here that flickering light that yellowish-sickish fluorescent tubing making my eyes ache so I wore my dark glasses giving the judge a false impression of me, and I was sniffing, wiping my nose, every question they asked me I'd hear myself giggle so nervous and ashamed even stammering over my age and my name so you looked with scorn at me, all of you.

• Because they were on your side, I could not prevent it. Because in granting me child support payments, you had a right to move away.

• Because I could not follow.

• Because he wet his pants, where he should not have, for his age.

• Because it would be blamed on me. It was blamed on me.

• Because my own mother screamed at me over the phone. She could not help me with my life she said, no one can help you with your life, we were screaming such things to each other as left us breathless and crying and I slammed down the receiver knowing that I had no mother and after the first grief I knew It is better, so.

• Because he would learn that someday, and the knowledge of it would hurt him.

• Because he had my hair coloring, and my eyes. That left eye, the weakness in it.

• Because that time it almost happened, the boiling water overturned onto him, I saw how easy it would be. How, if he could be prevented from screaming, the neighbors would not know.

• Because yes they would know, but only when I wanted them to know.

• Because you would know then. Only when I wanted you to know.

• Because then I could speak to you in this way, maybe in a letter which your lawyer would forward to you, or your sister, maybe over the telephone or even face to face.

• Because then you could not escape.

• Because though you did not love him you could not escape him.

• Because I have begun to bleed for six days quite heavily, and will then Spot for another three or four. Because soaking the blood in wads of toilet paper sitting on the toilet my hands shaking I think of you who never bleed.

• Because I am a proud woman, I scorn your charity.

• Because I am not a worthy mother.

• Because I am so tired.

• Because the machines digging in the earth and grinding trees are a torment by day, and the screaming insects by night.

• Because there is no sleep.

• Because he would only sleep, these past few months, if he could be with me in my bed.

• Because he whimpered, Mommy!-Mommy don't!

• Because he flinched from me when there was no cause.

• Because the pharmacist took the prescription and was gone such a long time, I knew he was telephoning someone.

• Because at the drugstore where I have shopped for a year and a half they pretended not to know my name.

• Because in the grocery store the cashiers stared smiling at me and at him pulling at my arm spilling tears down his face.

• Because they whispered and laughed behind me, I have too much pride to respond.

• Because he was with me at such times, he was a witness to such.

• Because he had no one but his Mommy and his Mommy had no one but him. Which is so lonely.

• Because I had gained seven pounds from last Sunday to this, the waist of my slacks is so tight.

• Because I hate the fat of my body.

• Because looking at me naked now you would show disgust.

• Because I was beautiful for you, why wasn't that enough?
```

---

## IC-2229: Fairness

- Title: Fairness
- Author (byline): Chinelo Okparanta
- Work: Happiness, Like Water; Pgs 32-40
- Publisher: Mariner Books
- Publication date as stated: Aug 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: CHINELO, BARNA, ENO, EKAITE, MAMA, PAPA
- Teaser before the introduction: No
- Spoken words (computed): 1588
- Already set (do not supply): none

### Source block (context only)

```text
Author: Chinelo Okparanta
Book: Happiness, Like Water; Pgs 32-40
ISBN: 978-0544003453
Publisher: Mariner Books
Date (Month/Year): Aug 2013
* Intro Source and additional information about skin
bleaching in African Nations.
https://files.aho.afro.who.int/afahobckpcontainer/production
/files/Skin_Bleaching_in_Africa_regional_fact_sheet_Nov23
.pdf
```

### Introduction (context only: never use it for content warnings)

```text
Whether we like to admit it or not, our global society is segregated -- divided by tribe, religion, even skin color. Colorism, much like racism, is a form of discrimination that regards darker skin as inferior, ugly and unacceptable and lighter or “fair” skin as superior. All over the world, people with darker skin tones attempt to gain social acceptance by bleaching their skin. It is not uncommon to see videos of people peeling off layers of their skin to reveal a lighter hue. In fact, according to a 2023 World Health Organization report*, 77% of Nigerian women use skin bleaching products.

In this selection, Nigerian author Chinelo Okparanta shares a tale from her youth even though it’s ugly – inferior -- unacceptable. Her actions were all in the quest for. . . Fairness by Chinelo Okparanta
```

### Performance text (classify this)

```text
CHINELO: (Pgs 32-40) We gather outside the classroom in the break between morning and afternoon lectures. We stand on the concrete steps, chewing groundnuts and meat pies, all of us with the same dark skin, matching, like the uniforms we wear. All of us, excepting Onyechi of course, because her skin has now turned color, and we are eager to know how. She no longer belongs. She is now one of the others, one of the girls with fair skin.

BARNA: (chuckling in disbelief; she claps her hands, eyes wide) 'Chi mo! My God! How fast the miracle!

CHINELO: Onyechi shakes her head, tells us that it was no miracle at all. She tells us of the bleach. I listen and nod, trying to catch every bit of the formula. Our skin is the colour not of ripe pawpaw peels, but of its seeds. We are thirsty for fairness. I think of returning home and telling Eno.

Hours later, I sit on a stool outside. Ekaite is at the far end of the backyard where the clotheslines hang. She collects Papa's shirts from the line, which wave in the breeze like misshapen flags. Even in the near darkness, I can see the yellowness of Ekaite's skin. A natural yellow, not like Onyechi's or some of the other girls'. Not like Mama's.

Eno sits with me. It is late evening, and the sky is grey. Mosquitoes swirl around. (swats at biting mosquitoes) At the clothesline, Ekaite is slapping even more than Eno and I. Her skirt only comes down to her knees. (to Eno) They bite us all the same.

ENO: (with angry dejection) No, they bite Ekaite more. Even the mosquitoes prefer fair skin.

CHINELO: The scent of chlorine billows in the air, and I think of Onyechi. I toss it about in my mind, like a pebble in the air, to get a feel for its texture, its potential, its capacity for success. And then I tell Eno.

When the sky grows black, we go into the house. We cut through the kitchen, pass the dining room, and enter together into the bathroom. Papa and Mama do not catch us. In the bathroom, we pour bleach into the bucket, only a quarter of the way full. Then we watch water bubble out of the faucet. We inhale and exhale deeply, and the sound of our breathing is weirdly louder than the sound of the running water. We turn the faucet off and gaze into the bucket.

EKAITE: Eno . . . Eno!

CHINELO: (both girls jump) Eno runs off to answer, more quickly than usual because she knows she should not be in the bathroom with me. She must use the house girls' bathroom, outside in the far corner of the backyard. But mostly, Eno runs off, because dinner will be served in an hour, and Eno will have to help in its preparation.

At the dining table, Papa sits at the head, Mama by his side. The scent of egusi soup enters through the kitchen. Mama picks up her spoon, looks into it, unscrews the tiny canister, still with the spoon in her hand. The lipstick is a rich colour, red like the hibiscus flower; and it rises from the container slowly, steadily, like a lizard cautiously peeking out of a hole. Overhead the ceiling fan rattles and buzzes. The air conditioner hums, like soft snoring. In the kitchen we hear the clangclanging of food preparation: of the pestle hitting the mortar, yam being pounded for the soup. And then I hear the shutting of the fridge, that shiny, stainless-steel door all the way from America. And I wonder if Ekaite ever takes the time to look at her reflection in the door. And if she does, does she see herself in that superior way in which I imagine all fair people see themselves?

A bowl of velvet tamarinds sits at the centre of the table. Mama bought the bowl on one of her business trips overseas. She returned from that trip with other things too -- silk blouses from Macy's, Chanel, Nike apparel. The evening she returned, she held up the overseas items for me to see. One blouse she held to my chest. It was the yellow of a ripe pineapple.

MAMA: Will lighten you up. . .

CHINELO: The first magazine arrived two weeks later, Cosmopolitan, pale faces and pink lips decorating the cover, women with hair the colour of fresh corn. Next was Glamour, then Elle.

I remember the bucket in the bathroom, and I feel hope billowing in me. Eno serves our food -- dishes of pounded yam and soup. Mama waves Eno away. I watch her hand waving, the gold rings on her fingers, the bracelet that dangles from her wrist.

MAMA: U zoamaka. You are looking very tattered today. It's no way to present yourself at the dinner table.

CHINELO: The words tumble out of her mouth that American way, one tumbling into the next with no space between. Papa looks at me for a moment, as if for the first time in a long time.

PAPA: How was school today?

MAMA: (to Papa) A good week. A good month even.

Imagine, an entire month and no strike! Surprising, with the way those lecturers are always on strike. Not to worry. (pause) Arrangements are already being made. (to Chinelo) You need a good education. That is what America will give you. A solid education. And no strikes. (smiling widely) With a degree from America, you can land a job with a big company here, or maybe even remain in America. Land of opportunities. (pause) In the meantime, you can't walk around looking tattered, shirt untucked, hair unbrushed. As for your face, dab some powder on. It will help brighten you up. (clears her throat) Even Ekaite presents herself better than you do. Very well mannered, that one. Takes care of herself. Beautiful all around.

CHINELO: (rolling her eyes) Eno is pretty too.

MAMA: (mocking in a sing-song) Eno is pretty too. Eno is no comparison. No comparison at all.

CHINELO: It's only bias, the way Mama feels about Ekaite. Ekaite's face reminds her of the faces she sees on her magazines. Because, of course, Ekaite's complexion is light and her nose is not as wide and her lips not as thick as mine or Eno's.

I remember the first time [Mama] came back with boxes of those creams. Esoterica, Movate, Skin Success, Ambi. It was around the time television commercials started advertising them -- the fade creams. We'd go to the Everyday Emporium, and there'd be stacks of them at the entrance. It was around this time too that the first set of girls in school started to grow lighter. Mama's friends started to grow lighter, too. Mama did not at first grow light with them. She was cautious. She'd only grow light if she had the best-quality creams, the kinds she knew America would have, not just the brands they sold at the Everyday Emporium.

In just a few weeks, her skin had turned that shade of yellow. She insisted I use the cream too. With Movate, dark and light patches formed all over my skin, like shadows on a wall. She insisted I stop. People would know, she said. Those dark knuckles and kneecaps and eyelids. People would surely know. We tried Esoterica next. No progress at all. Same with Skin Success and Ambi.

I tell Mama that I'm not feeling well and excuse myself from the table before she has a chance to respond. I carry my dishes into the kitchen, where Eno is waiting for me. Inside the bathroom, the air is humid and smells clean, purified, a chemical kind of fresh. Eno holds the towel and stands back, but I call her to me, because I am again finding myself skeptical of the water and bleach. Fear catches me, and I think perhaps we should just pour everything out. But then I hear Mama's voice, saying, ' Eno is no comparison. No comparison at all.' (taking the towel from Eno) You should go first. You're not supposed to be here. That way you'll be done by the time anyone comes to chase you out.

(to audience) She gets on her knees so that her face is just above the bucket. (to Eno) We'll do only the face today. Only get up when you feel you feel something like a tingle. (Eno takes a deep breath and dips her face into the water; long pause) Do you feel it yet? (Eno shakes her head face still in the water, long pause) Not yet? -- Okay. Come up. (Eno lifts her face from the water and takes a shuddering breath)

(to audience) The colour of her skin seems softer, a little lighter than before (to Eno, smiling) It's working! But we need to go full force. (to audience) The bath bowl is sitting in the sink. I pick it up, pour the bleach straight into it. I call Eno to my side, tell her to place her face into the bowl. (Eno takes a deep breath and dips her face into the bleach)

ENO: (screams and screams)

CHINELO: Her scream fills the bathroom. There is the thud of the door slamming into the wall. Ekaite rushes towards us. She holds Eno's face in her palms.

ENO: (twisting her face away, screaming)

CHINELO: I feel the pain in my own face. Papa looms in the doorway

PAPA: (fiercely) What did you do to her? What did you do?

CHINELO: In the doorway, I see Mama just watching. I turn to him, wanting desperately to make my case, but I don't find the words. My legs feel weak. I think of Mama and her creams. (to Eno) Don't worry. We'll find something that works. . .

Days later, when the scabs start to form, I imagine peeling them off. Eno's flesh underneath the scabs is reddish-yellow, not quite the yellow of a ripe pawpaw peel. And even if I know that this scabby fairness of hers is borne of injury -- a temporary fairness of skinless flesh, patchy and ugly -- I think how close she has come to having skin like Onyechi's, and I feel something like envy in me, because what she has wound up with is fairness after all. Fairness, if only for a while.
```

---

## IC-2230: Fangs of Endearment

- Title: Fangs of Endearment
- Author (byline): Dave Barry
- Work: I’ll Mature When I’m Dead
- Publisher: Berkley Trade
- Publication date as stated: April 2011
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1998
- Already set (do not supply): none

### Source block (context only)

```text
Author: Dave Barry
Book: I’ll Mature When I’m Dead
ISBN: 978-0425238981
Publisher: Berkley Trade
Date (Month/Year): April 2011
```

### Introduction (context only: never use it for content warnings)

```text
Twilight . . . Who doesn’t love a good vampire vs werewolf saga, right? As proof, Stephenie Meyer’s Twilight series has sold over 100 million copies. But the question is . . . why? I apologize in advance to Team Edward and Team Jacob, but let’s face it . . . the writing is . . . bad, laughably bad.

Have you ever heard of “purple prose” – It consists of words and phrases that sound stilted, overly descriptive or cliché. No? Let me show you what I mean. This is Dave Barry’s Fangs of Endearment - a humorous tribute to the writing style of Stephenie Meyer. . adjectives and adverbs and similes, Oh, my!
```

### Performance text (classify this)

```text
With a feeling of ominous foreboding, I turned my battered old pickup truck into the last remaining parking spot outside Creepstone High School. I glanced in the rearview mirror and scrunched my forehead in dismay as I realized for the millionth time that I do not consider myself at all attractive, although roughly 85 percent of the male characters I encounter either fall in love with me or want to kill me, or both, and in the movie version I am portrayed by a total babe.

Chapter 1: Warning

Heaving a sigh of exasperation, I creaked open the truck door, and with my trademark charming clumsiness, fell out face-first. But before I hit the asphalt, Phil [aka Team Edward] was there to catch me, having covered the 75 yards from his luxury car to my truck in 2/10ths of a second. Fortunately nobody noticed this because Phil is brilliantly clever, and the other students at Creepstone High have the observational skills of boiled ham.

Phil swooped me into his arms using the super vampire strength that he has in addition to his super vampire speed and his ability to read minds, perform complex mathematical calculations in his head, assemble a working nuclear submarine entirely from clock p arts, and recite all the lyrics to Guys and Dolls . . . backward.

Phil, a gorgeous brilliant wealthy sophisticated centuries-old vampire posing as a high-school student for reasons that are never totally clear, gently set me down on the parking lot and took my hand in his strong and perfect hand. As we entered the school I felt Phil’s grip tighten. Possibly fracturing my ring and index fingers. Looking up I saw the reason: Stewart [aka Team Jacob] was striding toward us in an ominous way. Stewart is a member of an indigenous tribe of Native Americans who become werewolves at puberty, in addition to developing acne. They do not get along with the vampires. One time in Boys’ phys. Ed. The two sides played each other in volleyball, and before it was over seven civilian students had been disemboweled. This could have created a real stink had not the Creepstone High authorities, who are even less observant than the student body, concluded that the cause was an unusually fast-acting stomach flu.

“Hello, Stewart” He looked at Phil with a look of pure lanky indigenous hatred before turning to me and replying, with a voice drenched in the aching and smoldering longingness of a powerful emotion that I knew he could never express in words. “What is it?”

He looked at me with his dark lanky eyes. Suddenly his expression changed to one of dark foreboding. “If you go out in the woods today,” he whispered hoarsely, “you better not go alone.”

“What . . .” I protested elliptically. But Stewart was already striding lankily away. Finally finding my voice, I inquired, “What did he mean by that?”

Phil turned his perfect gaze upon me, causing me to be struck by how unbelievably handsome he is, with his perfect face and chiseled cheekbones, and his gorgeous eyes that change color depending on how recently he has sucked all the blood out of a live bear, and his perfectly teased hair tousling down over his broad gorgeous forehead. “I’m sure it’s nothing. I’m especially sure it’s not Denise the vengeful psychopathic female vampire from the previous book who has vowed to hunt you down and torture you to death and who has been sighted recently in the woods around Creepstone. There is definitely no need to worry about that.”

Despite Phil’s reassurance, there was something in his tone that troubled me. But what was it? What had Stewart been trying to tell me? Was something bad about to happen? Would I soon find myself in yet another dramatic plot situation filled with peril? And why did everybody find me so attractive?

Chapter 2 – Decision

“How was school today?” inquired my father, Pete [aka Charlie]. Pete is chief of police of Creepstone, but he is not exactly Sherlock Holmes, if you catch my drift. He has so far failed to pick up on the fat that my boyfriend is a vampire who spends every night in my room, and that y other boyfriend is a werewolf, and that Creepstone, not to mention the entire state of Washington, is teeming with violent homicidal supernatural creatures, about 60 percent of whom are trying to kill me personally.

“Fine.” Satisfied, Pete grunted and returned to his paper. Then remembering something in his mind, he looked up again. “By the way,” he intoned, “I want you to stay out of the woods.”

I gasped. “Why?” I inquired forebodingly.

“In the past two days, 158 hikers have been killed in the woods around Creepstone.”

“Killed?” I queried. I felt a cold feeling shoot through my veins like an intravenous Slushie. “How?” I elaborated.

“It’s the darnedest thing,” marveled Pete. “All of them were violently dismembered, apparently by someone or something with incredibly savage strength. Some of the victim’s limbs were found as far as two football fields away from their bodies.

I stared at him with a facial expression of shock. “But how . . .” I began, searching for the words to complete the question that was even then forming in my brain. “How did two football fields get into the woods?

Pete shook his head and shrugged, raising and lowering his shoulders to indicate he didn’t know the answer. “That’s got us stumped so far. Right now we’re working on the theory that it could be a bobcat, or a pack of unusually aggressive squirrels. But until we get this thing figured out, I don’t want you going out in the woods, OK?

My forehead puckered into a frown as I remembered that Phil has mentioned that Denise the psychopathic vampire had been sighted recently in the woods. Could she have something to do with the 158 slain hikers? Should I mention any of this to Pete?

Nah. The more I thought about it, the more I knew what I had to do: I had to go out into the woods alone. That’s what I always do with my trademark stubbornness: I place myself in grave plot peril when there is no coherent reason to do so. . Some people may call this ridiculous, but I am guessing that “some people” have not sold [100] million books to date.

I prepared to go out into the woods with nothing to protect me except my various attractive supernatural boyfriends. I did not know what peril I was about to face. All I knew was one thing, the most important thing of all: Whatever happened, it would involve me.

Chapter 3: Peril

I stumbled through the woods, tripping with clumsy endearingness over the logs that lay everywhere, like the corpses of dead trees knocked down by gravity. It was getting dark, and I knew that Phil would be out looking for me with his tawny eyes nestled in the perfection of his face. Stewart would also be looking for me in his lanky way with his bulging, rippling muscles or giant snout, depending on what form he was in.

I came to a clearing completely surrounded on all sides by the dark forbidding words. I walked into the clearing as the cold wind blew my hair around into a big trademark mess, although fortunately I don’t care about hair or makeup because the last thing I need to do is make myself even more irresistible. With a feeling of even greater foreboding than usual, I kept walking forward, putting one leg in front of the other in an alternating sequence.

Suddenly, I saw movement at the far edge of the clearing. I stopped and stared. A chill slithered up my spine like an ascending iguana wearing tiny booties made from pieces of Fudgsicle as I saw the terrifying shadowy figure step menacingly into the clearing. With a shock of recognition I recognized who it was: Denise.

She bared her teeth, revealing her needle-like fangs, which glinted brightly in the moonlight like some kind of sharp highly reflective things used in a simile. I squinched my eyes shut, preparing myself to be killed in a horrible manner. The dramatic tension mounted to a fever pitch as I waited to feel Denise’s teeth plunge vengefully into my neck and suck my blood out like a giant supernatural mosquito. I wondered how much it would hurt, and how long it would last before I was dead, and who, if anybody, would take over as narrator.

And just then it happened, a dramatic turn of events so unexpected and shocking that nobody could have predicted it in a million years without having read the previous books. I heard a snarling sound and opened my eyes to see that Denise, instead of attacking me, was fighting for her life. And the person she was fighting against – the person who, against all odds, had appeared at the last possible instant to rescue me, was:

[Donald Trump] *the text says “Barbara Walters”, but Donald Trump may be more fun and more relevant*

No, I am leavening the narrative with humor. It was really Phil. His eyes flashed me an alarmed look of tawny ominousness. “Run away; they’re coming!” he commanded. He pointed toward the edge of the clearing. I looked in that direction, and my mouth gaped open as I saw them emerging from the woods: [Phil’s] vampire family: Grover, Buck, Scooter, Eldrigede, DeeDee, Trixie and Skeeter. Grover nodded to Phil with a special code vampire nod, indicating something ominous was about to transpire.

“Stay here,” asserted Phil. “Stay perfectly still. Whatever you do, don’t do anything to draw attention to yourself. “

An incredible battle had erupted between the werewolves and the various attractive sets of vampires. There were snarls and roars and hideous supernatural screams. It was incredibly exciting and terrifying, although because of my trademark inability to describe action in anything except very general terms you are just going to have to take my word for this.

As the battle raged on, an alarming thought crept into my mind: I was not playing a central role. I realized that I needed to do something. But what could I, a mere human, although a highly endearing one, do? Then it struck me: I could draw attention to myself.

Frantically I looked around, searching for a sharp object. Suddenly I saw it, lying on the ground, clearly visible in the bright moonlight: A sharp object. I picked it up and stabbed at myself. Blood streamed redly down my leg. Suddenly there was a vampire stampede coming my way at the speed of vampire, with the werewolves right behind.

They were almost on me, dozens of blood-crazed vampires and enraged werewolves. I knew there was no way I could be saved. And then, at the absolute climactic height of the action sequence, everything went dark.

Chapter 4: Resolution

“She’s coming around,” I heard Phil’s voice intone.

“What happened?” I queried weakly.

Phil shook his head lovingly. “You almost got yourself and all of us killed because of your unbelievably irresponsible, deranged, and self-centered behavior,” he remarked, adding, “but that just makes me desire you more, you crazy, quirky, irresistible woman, you.”

“But how did you win the climactic fight?” I pressed.

“Through a lot of action,” Phil explained.

“Wow,” I stated. That must have been incredibly exciting.” I sighed in rueful resignation. “Well, at least our other troubles are over.” Phil looked at me with an expression of not totally agreeing with my assertion. “What is it?” I interrogated, adding, “Is something wrong?”

“It turns out that all those recent hiker deaths were not caused by Denise, but by a long-dormant supernatural race of giant homicidal pine cones who have been awakened by global warming and now prowl the woods around Creepstone each night, savagely attacking every living thing in their path!”

Until the next book . . . .
```

---

## IC-2231: The Fart that (Almost) Altered My Destiny . . .

- Title: The Fart that (Almost) Altered My Destiny . . .
- Author (byline): Anna Lind Thomas
- Work: Not specified
- Publisher: Anna Lind Thomas
- Publication date as stated: 2018
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1870
- Already set (do not supply): none

### Source block (context only)

```text
Author: Anna Lind Thomas
ISBN: N/A
Publisher: Anna Lind Thomas
Date (Month/Year): 2018
```

### Introduction (context only: never use it for content warnings)

```text
The Fart that (Almost Altered My Destiny by Anna Lind Thomas
```

### Performance text (classify this)

```text
[NOTE: Selection available in e-book format directly from the author. Check for publication requirements in your state before performing.]

(Pg 5–9) Like everything in life, farts have a time and place. However, I never realized that in the wrong time and place, flatulence had enough power to alter my course in history. Well, it can if it’s the third date with the man of your dreams. And, if it makes his eyes burn. If God destined us to be together, I was one SBD away from foiling His plans (that’s “Silent But Deadly” for *the uninformed*).

It was about five years ago. I was trying to lose a few pounds so I was staying away from carbs. That’s when I met my husband, Rob. On our first date, he booked the next two. He liked me. I liked him. Things were looking real good.

He picked me up in a Cobra Mustang and his pathetic attempt to win me over with a car totally worked. I’m not shallow, but since I spent most of my twenties picking men up because I didn’t want my hair to frizz in their non-air conditioned jalopies on 3 wheels and a 15 year old spare, I welcomed his fancy sports car with open arms.

We arrived at the restaurant and Rob was ordering food I hadn’t allowed myself to eat in years. I didn’t want to be “that girl” so I ate, drank, and oh, was I merry. Later we shopped a bit. Rob surprised me by buying an expensive pair of shoes that he caught me eyeing. Was this love?

That’s when it happened. Gas strikes in two different ways - uncontrollable toots or sharp, shooting pains that feel a lot like dying. I thought I was dying.

Not to make a scene, I told Rob I suddenly wasn’t feeling well and probably needed to head home. On the way home in his Cobra, he tried to hold my hand and ask me lots of questions, but I wasn’t having any of it. The pain was so bad it felt like I was being stabbed with a bunch of tiny forks. Then I realized …

My God, help me. I have a horrendous fart on deck. I’m in trouble. Big trouble. The more I held it in, the more pain would shoot through my stomach and down my legs. I was even having to raise myself off the seat, gripping on to my door and the dashboard.

“Seriously, you need to hurry - I’m in a lot of pain.” I managed to say through gritted teeth.

“Wow, it’s that bad? What’s wrong? Do I need to take you to a hospital?” How do you tell a man you just started dating that the reason you’re writhing in pain is because you have to fart?

Well, you can either tell him, or like me, let the fart speak for itself.

People, hear me. There was nothing I could do. As impressive as I am with sphincter control, this was out of my hands. Slowly, it eeked out. The more I tried to stop it, the more it forced its way through the door. However, to my pleasant surprise, there was no sound. I sat silently, sweat accumulating above my upper lip. Ok, maybe I got away with it. Maybe I’m home free. Then it hit me. Not an idea, a cloud. A horrific, fart cloud. Not in a, “Am I smelling something?” sort of way. More like a “Is someone dead and rotting in your trunk and am I in hell?” sort of way. Suddenly, I panicked. “Roll down the windows!” I screamed (yes, I literally screamed it like I was in a horror movie).

“What? Why?” Rob asked, starting to freak out because I was freaking out. “I can’t roll down the windows, unlock it! UNLOCK IT!”

“What’s going on?” Rob yells back to me, “Why are you ...” then it hit him. I could see it in his eyes. Was it surprise? Horror? Water started to accumulate at the base of his eyelids, “Oh my God, I CAN TASTE IT!” he screamed.

“Roll down the windows!” As I screamed, the toots started to flood out uncontrollably. I scratched and clawed at the window like I was being kidnapped. Rob, unable to see either by fart cloud or panic, kept turning on the windshield wipers instead of unlocking the window.

It was chaos. We were acting like we were under siege by gun fire. We were under siege alright, just not by gun fire.

Finally he was able to hit the right control and he rolled down our windows. We both gulped in fresh air. I was horrified, yet happy to be alive, then remembered I just farted on the man of my dreams, then sorta wished I was dead.

We sat silently for the rest of the way home. Although the shooting pains had subsided, I now desperately needed to use the bathroom, in an urgent, explosive kind of way.

He pulled up to my apartment and before he could come to a stop I had already jumped out, “Ok, thanks for dinner, sorry about the fart, love the shoes!” and ran in to my apartment like I was running from the cops.

I burst through my door and ran straight for the bathroom, where I was finally able to unleash and make noises that no one should ever, EVER, hear coming from another person.

Then I heard it. Rob’s voice. Right. Outside. My. Bathroom. Door.

“Anna? You left your shoes in my car and your front door was open. Where do you want me to put them?”

“Get away from the door!” I screamed like Reagan from The Exorcist.

“Ok, I’m sorry. Are you okay?”

*toot* *toot* *splatter* *ungodly noise*

“I’m fine, Rob - just leave the shoes there. I’ll call you later okay?”

“Okay, are you sure you’re …”

“I’m fine! Get away from the door!”

This man! I mean, I love him, but take a freakin’ hint!

Finally, I heard the front door shut, and the Cobra engine zoom away. I thought that was the last I’d hear from him. I didn’t think it was possible to ever see a man again after he screams he can taste your fart after only knowing you for 48 hours.

But, to my surprise, I did. A couple days later, actually. Now we’re married and he’s lying on the couch while I type this ... “It was your rack that saved you,” he just lovingly reminded me.

Well, thank you boobs. You saved us. You saved our destiny.

TRANSITION The human body is amazing, somewhat embarrassing, but amazing, nevertheless. You know what else it is? Hairy. Completely normal. That’s why razors were invented, right? But sometimes unexpected hairs crop up in unanticipated places. According to CNN, an estimated 20 million American women remove hair from their chins per week. This is An Open Letter to the Black hair Under My Chin . . .

(Pg 25–27) Dear Freak Black Hair,

I remember the first time we met. It was a few years ago. I was casually resting my chin on my hand. Probably amid a deep thought, like trying to process Rachael Ray’s boob situation, or determining which Property Brother was more attractive. Then I felt you. I was confused at first. I had never felt that sensation on my chin before. I’d be lying if I said I wasn’t afraid. I’m sorry if that hurts you, but you have to understand – I’m not used to this.

I rushed to the bathroom and there you were. One inch of thick, black, man hair, so long you even started to curl, making yourself right at home under my chin. I’ll admit it. I was horrified. So many questions flooded my brain. What were you, some kind of silent ninja? How did you set up camp on my face for that long without me ever noticing? Why were you there? Who sent you? And again, how did you grow that long without me ever noticing?!

I didn’t even want to get to know you. I grabbed my tweezers and plucked you out of my life and let you fall to the sink along with my husband’s whiskers. My husband’s whiskers, by the way, that I continually ask him to wash out of the sink, but for some reason it’s just way too much to ask, so apparently it’s my job to clean up after his damn facial hair and I’m just like, how can I trust him with the big things if I can’t even trust him with the little things?

Pardon me, I’ve strayed off topic.

Where was I? Oh yes. After washing you down the sink I thought it was the last I’d ever see of you. I admit, I judged you immediately and didn’t even give you a chance. You threatened me. The only people I knew who had man hair on their face were men, witches and Sicilian grandmas – and only the Sicilian grandmas that stir a huge pot of spaghetti sauce all day.

Yes, it’s true. I am Sicilian, I suppose I should have seen this coming, but why had you come for me so early? I was afraid.

The next day I awoke, entered my bathroom to brush my teeth and screamed in terror. There you were again. But how could this be? I just plucked you at the root, now you’re straight chillin’ on my face again like it never happened?

What is this, voodoo? Some kind of dark magic?

I plucked you again. You seemed thicker this time, about the circumference of a tree trunk, but I suppose I can’t be entirely sure as I didn’t have a measuring tape on hand. With my heart racing, hand shaking, I ripped you out of my life once again and ran from the bathroom.

I bumped into my husband. He could tell something was wrong. I was wild eyed like I just saw a ghost. No, it was worse, I told him. I was attacked by a thick man hair growing on my face that was regenerating itself at a freak pace that can’t be explained by science.

Day after day, you came back. Day after day, I plucked.

God forbid I forgot about you for a couple days. Left to your own devices, you would get so long I could string beads on you. I know, because I tried it once. I suppose by now, you’ve become a friend. Not a good friend, one of those friends who you can't stand the sight of their stupid face. A stupid, familiar face that I can always count on to arrive right on time. I know that if I’m at an important event, or out of town and forgot my tweezers, you’ll pop right out and shout “Hello world!”

I hate you. But you’re a part of me now, so I need to be honest with you.

I don’t know where you’ve come from, how you grow so fast or how you’re totally invisible until you reach three inches long, but you can’t live on my face. It’s weird, distracting, and people don’t look me in the eyes when you’re around. So, with these tweezers, I say goodbye to you forever. And by forever, I mean, I'll see you tomorrow.
```

---

## IC-2232: Fat Girls and Lawn Chairs: Queen of the Gym

- Title: Fat Girls and Lawn Chairs: Queen of the Gym
- Author (byline): Cheryl Peck
- Work: Fat Girls and Lawn Chairs
- Publisher: Grand Central Publishing
- Publication date as stated: Jan 2004
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1643
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cheryl Peck
Book: Fat Girls and Lawn Chairs
ISBN: 978-0446692298
Publisher: Grand Central Publishing
Date (Month/Year): Jan 2004
```

### Introduction (context only: never use it for content warnings)

```text
We’ve all been exposed to them: those girls/women who go to the gym in full blown make-up with matching accessories to go with their new workout outfits? Have you ever seen one of those ladies completely decked out with lipstick and all? At 7:00 am?? Do these women even sweat? What is the point? And then to top if off....they're on their phone during the entire workout on the treadmill?? Again, at 7:00 am??? Crazy huh? Well, Cheryl Peck is definitely NOT one of THOSE women, but at 300 pounds, she has become an Inspirational Goddess at her local gym. This is her story: Fat Girls and Lawn Chairs: Queen of the Gym by Cheryl Peck
```

### Performance text (classify this)

```text
It happened again this morning. I was sitting there half-naked on a bench when a fellow exerciser leaned over and said, "I just wanted to tell you-I admire you for coming here every day. You give me inspiration to keep coming myself."

"Here" is the gym. I have become an inspirational goddess. In a gym.

I grinned at the very image of it, myself: here is this woman who probably imagines herself to be overweight-or perhaps she is overweight, she is just not in my weight division-sitting on the edge of her bed in the morning, thinking to herself, "There is that woman at the gym who is twenty years older than I am and has three extra people tucked under her skin, and she manages to drag herself to the gym every day. . ."

It is not my goal here to be unkind to myself or to others. Perhaps I am an inspiration to her because I am easily three times her size and I take my clothes off in front of other women. Being fat and naked in front of other women is an act of courage. Perhaps my admirer did not realize that it was exactly when she spoke to me that I was artfully arranging my hairbrush and underwear and bodily potions to cut the buck-naked, ass-exposing mini-towel-hugging moments of my gym experience to the absolute minimum. She wears a pretty little lace-edged towel-thing to the shower and back. I don't, but I understand the desire.

It was not that long ago that she bent over to pick up something as Miss Tri Athlete walked into the locker room and whistled, "Boy did I get a moon!" Junior high gym, revisited: I can't swear that particular exchange was the reason, but I did not see my admirer again for the next month. To Miss Tri Athlete she answered, "Just when I had forgotten for half a second that I was totally naked. . ." I doubt that she forgets that often. Almost none of us do.

Nor do I: which is why, the first time someone in the locker room said to me, "I have to give you credit just for coming here," I smiled politely and thought ugly thoughts for some time afterwards.

Up yours thrummed through my mind. Nobody asked you for credit zinged along on its tail, followed closely by Who died and left you queen of the gym?"

Like it takes any more for me to go the gym than it does any other woman there," I seethed to my Beloved.

"Well it does," my Beloved returned sedately, "and you know it. How many other women our size have you seen at our gym?"

The answer is-none.

There are women of all shapes and sizes-up to a point- from Miss Tri Athlete, who runs in the 20-25- year-old pack, wears Victoria's Secret underthings and is self-effacing about her own physical prowess to women who are probably in their sixties, perhaps even seventies. There are chubby women and post-partum moms and stocky women and lumpy women. . . but there are very few truly fat women.

Exercise, you might advise me solemnly, is hard for fat women. Exercise is hard for everyone. Exercise is as hard as you make it.

Miss Tri Athlete shared a conversation with me the other morning. She said, "It feels really good to get this out of the way first thing in the morning, doesn't it? I think when you plan to exercise in the evening it just hangs over you like a bad cloud all day."

She can't be more than twenty-five, she can't be carrying more than six ounces of unnecessary body fat and I've never seen her move like anything hurts. Her joints don't creak. Her back doesn't ache. She sweats and turns pink just like everybody else. She trains like an iron woman, but she's relieved when it's over.

I don't believe it's exercise that keeps fat women out of the gym. I think it's the distance from the bench in front of the locker to the shower and back. I think it's years and years of standing in grocery lines and idly staring at the anorexic women on the cover of Cosmo, I think it's four-year-olds in restaurants who stage-whisper, "Mommy-look at that FAT lady," I think it's years of watching American films where famous actresses never have pimples on their butts or stretch marks where they had kids.

It's Baywatch. Barbie. It's never really understanding, in our gut, that if we could ask her even Barbie could tell us exactly what is wrong with her body. And we all know, intellectually, of course, that Barbie's legs are too long, her waist is too short, her boobs are too big and her feet are ridiculous, but she's a doll. What we do not know, as women, is that my sports physiologist, who is in her late twenties and runs marathons, also has tendonitis in her shoulder, a bad back, and passes out if she trains too hard. My former coach for the Nautilus machines had MS. None of us have perfect bodies. If we did have perfect bodies, we would still believe we are too short or too fat or too skinny or not tan enough.

None of us have ever been taught to admire the bodies we have.

And nothing reminds us of our personal imperfections like taking off our clothes. Imagining that-for whatever reason- other people are looking at us.My sports physiologist is more afraid of wounding me than I am of being wounded. The program she has set up for me to regain my youthful vim and vigor is appropriately hard. Not too hard, not too easy. It's just exercise. The most difficult part of my routine, designed by my physiologist, is walking through the heavy-duty weight room to get the equipment I need for my sit-ups.

The weight room is full mostly of men. Lifting weights. Not one of them has ever been rude to me, not one of them has even given me an unkind glance: still, the irony that I make the greatest emotional sacrifice to do the exercise I like the least is born again each time I walk into the room.

Someone might laugh at me. Someone might say, "What are you doing here?" I have a perfectly acceptable answer.

I joined the gym because my girlfriend said, "I want to walk the Appalachian Trail." I have no desire to backpack across the wilderness: but I could barely keep up with her when she made this pronouncement, and I could see myself falling farther and farther behind if I stayed home while she trained. I joined the gym because I used to work out and I used to feel better. Moved better. Could tie my shoes. I joined the gym because I dropped a piece of paper on the floor of my friend's car and I could not reach down and pick it up. I joined the gym because I have a sedentary job and a number of aches and pains and chronic miseries that are the result of being over fifty and having a sedentary job. I joined the gym because my sister, who is younger than I am and more fit, seriously hurt her back picking up a case of pop. It could have been me. It probably should have been me.

I keep going back to the gym because I love endorphins. I love feeling stronger. More agile. I can tie my shoes without holding my breath. I can pick papers up off the car floor without having to wait until I get out of the car. I don't breathe quite as loudly. I have lost that doddering, uncertain old lady's walk that made strange teenaged boys try to hold doors or carry things for me.I keep going back because I hate feeling helpless. Years ago, a friend of mine convinced me to join Vic Tanney, a chain of gyms popular at the time. There was a brand-new gym just around the corner from where we lived-just a matter of a few blocks. She had belonged to Vic Tanney before, so she guided me through the guided tour, offering me bits of advice and expertise along the way. . . I plopped down money, she plopped down money, and a few days later it was time for us to go to the gym.

She couldn't go.

She was fat.

Losing weight had been her expressed goal when she joined: now she couldn't go until she was "thinner."

Everyone else at the gym, she said, was buff and golden. "I'll be there," I pointed out (for I have never been a small woman).

She couldn't go. She was too fat. She was a size twelve.

I have determined that I don't particularly mind being the queen of my gym. There may indeed be women who wake up in the morning and sit on the edges of their beds and think to themselves, "There is that fat woman at my gym who goes almost every day, and if she can do it. . ." I am proud to be an inspirational goddess. It has taken me most of my life to understand that what we see, when we look at another person, may reflect absolutely nothing about how they see themselves.

Always having been a woman of size, I have always believed that it must be just a wonderful experience to be thin. What I am learning is that the reverse of the old truism is equally true: inside every thin woman there is a fat woman just waiting to jump out.

We give that woman entirely too much power over our lives. We all do.
```

---

## IC-2233: A Few Words About Breasts

- Title: A Few Words About Breasts
- Author (byline): Nora Ephron
- Work: Best of Modern Humor
- Publisher: Alfred A. Knopf, Inc
- Publication date as stated: Oct 1983
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1314
- Already set (do not supply): none

### Source block (context only)

```text
Author: Nora Ephron
Book: Best of Modern Humor
ISBN: 978-0394515311
Publisher: Alfred A. Knopf, Inc
Date (Month/Year): Oct 1983
```

### Introduction (context only: never use it for content warnings)

```text
IN AN EDUCATIONAL FILM VOICE: PUBERTY: OK, so it's a funny word - but what is puberty, anyway? Puberty (say: pyoo-ber-tee) is the name for the time when your body begins to develop and change as you become an adult. We're talking about stuff like girls developing breasts and boys starting to look more like men. During puberty, your body will grow faster than at any other time in your life, except for when you were a baby.

It helps to know about the changes that puberty causes before they happen. That way, you know what to expect. It's also important to remember that everybody goes through these changes. No matter where you live, whether you're a boy or a girl, whether you like vanilla or double-fudge-chunk ice cream, you will experience them. No two people are exactly alike, but one thing everyone has in common is that we all go through puberty.

And now . . . . A Few Words About Breasts by Nora Ephron
```

### Performance text (classify this)

```text
I have to begin with a few words about androgyny. In grammar school, in the fifth and sixth grades, we were all tyrannized by a rigid set of rules that supposedly determined whether we were boys or girls. The episode in Huckleberry Finn where Huck is disguised as a girl and gives himself away by the way he threads a needle and catches a ball-that kind of thing. We learned that the way you sat, crossed your legs, held a cigarette, and looked at your nails-the way you did these things instinctively was absolute proof of your sex. Now obviously most children did not take this literally, but I did. I thought that just one slip, just one incorrect cross of my legs or flick of an imaginary cigarette ash would turn me from whatever I was into the other thing; that would be all it took, really. Even though I was outwardly a girl and had many of the trappings generally associated with girldom-a girl's name, for example, and dresses, my own telephone, an autograph book-I spent the early years of my adolescence absolutely certain that I might at any point gum it up. I did not feel at all like a girl. I was boyish. I was athletic, ambitious, outspoken, competitive, noisy, rambunctious. I had scabs on my knees and my socks slid into my loafers and I could throw a football. I wanted desperately not to be that way, not to be a mixture of both things, but instead just one, a girl, a definite indisputable girl. As soft and as pink as a nursery. And nothing would do that for me, I felt, but breasts.

I was about six months younger than everyone else in my class, and so for about six months after it began, for six months after my friends had begun to develop (that was the word we used, develop), I was not particularly worried. I would sit in the bathtub and look down at my breasts and know that any day now, any second now, they would start growing like everyone else's. They didn't. "I want to buy a bra," I said to my mother one night. "What for?" she said. My mother was really hateful about bras, and by the time my third sister had gotten to the point where she was ready to want one, my mother had worked the whole business into a comedy routine. "Why not use a Band-Aid instead?" she would say. It was a source of great pride to my mother that she had never even had to wear a brassiere until she had her fourth child, and then only because her gynecologist made her. It was incomprehensible to me that anyone could ever be proud of something like that. It was the 1950s, for God's sake. Jane Russell. Cashmere sweaters. Couldn't my mother see that? "I am too old to wear an undershirt." Screaming. Weeping. Shouting. "Then don't wear an undershirt," said my mother. "But I want to buy a bra." "What for?"

I suppose that for most girls, breasts, brassieres, that entire thing, has more trauma, more to do with the coming of adolescence, with becoming a woman, than anything else. Certainly more than getting your period, although that, too, was traumatic, symbolic. But you could see breasts; they were there; they were visible. Whereas a girl could claim to have her period for months before she actually got it and nobody would ever know the difference. Which is exactly what I did. All you had to do was make a great fuss over having enough nickels for the Kotex machine and walk around clutching your stomach and moaning for three to five days a month about The Curse and you could convince anybody. There is a school of thought somewhere in the women's lib/women's mag/gynecology establishment that claims that menstrual cramps are purely psychological, and I lean toward it. Not that I didn't have them finally. Agonizing cramps, heating-pad cramps, go-down-to-the-school-nurse-and-lie-on-the cot cramps.

But, unlike any pain I had ever suffered, I adored the pain of cramps, welcomed it, wallowed in it, bragged about it. "I can't go. I have cramps." "I can't do that. I have cramps." And most of all, gigglingly, blushingly: "I can't swim. I have cramps." Nobody ever used the hard-core word. Menstruation. God, what an awful word. Never that. "I have cramps."

The morning I first got my period, I went into my mother's bedroom to tell her. And my mother, my utterly-hateful-about-bras mother, burst into tears. It was really a lovely moment, and I remember it so clearly not just because it was one of the two times I ever saw my mother cry on my account (the other was when I was caught being a six-year-old kleptomaniac), but also because the incident did not mean to me what it meant to her. Her little girl, her firstborn, had finally become a woman. That was what she was crying about. My reaction to the event, however, was that I might well be a woman in some scientific, textbook sense (and could at least stop faking every month and stop wasting all those nickels). But in another sense in a visible sense I was as androgynous and as liable to tip over into boyhood as ever

I started with a 28 AA bra. I don't think they made them any smaller S in those days, although I gather that now you can buy bras for five-year-olds that don't have any cups whatsoever in them; trainer bras they are called. My first brassiere came from Robinson's Department Store in Beverly Hills. I went there alone, shaking, positive they would look me over and smile and tell me to come back next year. An actual fitter took me into the dressing room and stood over me while I took off my blouse and tried the first one on. The little puffs stood out on my chest. "Lean over," said the fitter. (To this day, I am not sure what fitters in bra departments do except to tell you to lean over.) I leaned over, with the fleeting hope that my breasts would miraculously fall out of my body and into the puffs. Nothing. And I knew that no one would ever want to marry me. I had no breasts. I would never have breasts.

Here are some things I did to help: Bought a Mark Eden Bust Developer. Slept on my back for four years.

Splashed cold water on them every night because some French actress said in Life magazine that that was what she did for her perfect bustline.

Ultimately, I resigned myself to a bad toss and began to wear padded bras. I think about them now, think about all those years in high school that I went around in them, my three padded bras, every single one of them with different-sized breasts. Each time I changed bras I changed sizes: one week nice perky but not too obtrusive breasts, the next medium-sized slightly pointy ones, the next week knockers, true knockers; all the time, whatever size I was, carrying around this rubberized appendage on my chest that occasionally crashed into a wall and was poked inward and had to be poked outward-I think about all that and wonder how anyone kept a straight face through it. My parents, who normally had no restraints about needling me-why did they say nothing as they watched my chest go up and down? My friends, who would periodically inspect my breasts for signs of growth and reassure me - why didn't they at least counsel consistency?

You probably think I am crazy to go on like this: Here I have set out to [give] a confession that is meant to hit you with the shock of recognition, and instead you are sitting there thinking I am thoroughly warped. Well, what can I tell you? If I had had them, I would have been a completely different person. I honestly believe that.
```

---

## IC-2234: Finding Alice

- Title: Finding Alice
- Author (byline): Melody Carlson
- Work: Not specified
- Publisher: WaterBrook
- Publication date as stated: Sept 2003
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: ALICE, MOTHER, DR. THORNTON, VOICE 1, VOICE 2, TWEEDLE VOICE, FAYE
- Teaser before the introduction: Yes
- Spoken words (computed): 1666
- Already set (do not supply): none

### Source block (context only)

```text
Author: Finding Alice
ISBN: 978-1578567737
Publisher: WaterBrook
Date (Month/Year): Sept 2003
```

### Introduction (context only: never use it for content warnings)

```text
Robert Louis Stevenson once said, “You cannot run away from weakness; you must sometimes fight it out or perish; and if that be so, why not now, and where you stand?” In this selection, Alice struggles with paranoid schizophrenia during her senior year of college. Feeling shut off from everyone and alone, her mind takes her on a parallel trip into Wonderland with her namesake -- a curious adventure where she realizes that sometimes it’s better to find strength in your weakness.

Finding Alice by Melody Carlson
```

### Performance text (classify this)

```text
ALICE: (Pg 1) I’m not sure how it all started or even why. I was simply walking through my life, minding my own business, when someone pulled the earth out from under me. It felt like a curious adventure. I still remember that rainy day back in fifth grade when my mother caught me reading Alice’s Adventures in Wonderland.

MOTHER: (Pg 2-3) What are you doing, Alice?

ALICE: Reading.

MOTHER: Oh, dear, you’re not reading that, are you? They say the author was on drugs when he wrote it.

ALICE: Well, I like it. How do you know he was on drugs?

MOTHER: Everyone knows that.

ALICE: (to audience) Then she held out her hand for the book. [Reading about Alice made me feel special. See . . .] (Pg 15) I always wanted to be special. I used to fantasize about it, imagining myself as someone famous or smart or beautiful. I wanted to be noticed, to be somebody that mattered. (beat) (Pg 47) At some point, I imagined God with a pair of golden scissors, neatly snipping my life into two separate sections. One life I call “before crazy”; the other one is simply “now.” But it’s not until I hear Dr. Thornton at Forest Hills say that hideous word – schizophrenia -- that I begin to differentiate between the two separate lifetimes.

DR. THORNTON: (Pg 47-48) (in a grade-school teacher voice) Do you know what schizophrenia is? (beat) It’s an illness of the brain. An impairment or chemical imbalance. The brain experiences hallucinations. Unable to differentiate between what is real and what is not.

ALICE: (knowingly) (Pg 228) Everything is just an elaborate scheme to set me up. (Pg 71) Although I suspect there are many players in this game. [Dr. Thornton. The Mad Hatter. The Red Queen.] (Pg 73) They say this is a hospital, but I can tell it’s a prison – (Pg 71) the Queen’s Prison. (Pg 73) The woman in the room next to mine screams almost constantly. I call her the Duchess since she’s always in a royally foul mood. And the scrawny blond “orderly” with the thin pale mustache is definitely a spy. (Pg 4) A variety of people sitting around on sagging sofas or in wheelchairs, many of them with their heads hanging limply, discarded marionettes with their strings cut.

(Pg 55) It seems there is a tiny door that I must walk through. It is called “normal.” But I am not. As a result, I cannot fit through this door. And yet they keep telling me I must go through it. They being my mom, the doctor, and the medical profession in general. (Pg 56) As I recall, the only way the other Alice could fit through her tiny door was to take the pills that made her get very, very small. I guess that is what Dr. Thornton’s pills are supposed to do for me. Make me very, very small. Or, in a word, normal. (beat)

(Pg 53) Mostly I remember Grandma. . . how she sat in a chair with a blank stare and didn’t even recognize her own daughter. Do I want to end up like her? Locked up and doped up and totally useless? I don’t think so. No, I’m certain there must be another way out of this mess.

(Pg 85) That’s when I notice it. The door to the waiting area is propped open. Without thinking, I pass through the open door. This time I don’t even have to take a pill to make myself fit. I simply walk across the vacant waiting room and past the main entrance. Suddenly I am outside.

(Pg 130) For a few days it doesn’t seem too terribly awful. (Pg 140-141) [But] all the voices are yelling at me now. They are calling me names . . .

VOICE 1: STUPID!

VOICE 2: WORTHLESS!

ALICE: And it’s not that I disagree; I just want them to go away.

I sit in the middle of the city, removed from everyone and everything, separated, quarantined perhaps. I see people passing by, a blur of winter coats and blank faces, [but] I am not part of them. I am encased in Plexiglas, a specimen to be gawked at.

(Pg 130) I am anxious and nervous. My mind races in all directions and my ability to function is as thin as a butterfly wing. Every nighttime noise makes my heart leap out of my chest. And lately I am covered with bugs. I awake in the night trying to swat and push them away from me, but they are crawling under my skin. (Pg 146-147) Sometimes my head is a really screwed-up radio station. Voices, voices, voices – all jabbering at the same time.

My life is completely impossible. I just don’t know how much longer I can take all this. Although some of the voices tell me they have the solution. Destruction. [And one of the voices tells me . . .]

VOICE 1: (Pg 112-113) You might as well call it quits, Alice. Look over there. There’s your ticket out of this mess. There’s something over the side. The end of your troubles.

ALICE: I don’t know the name of the bridge, but I think I’ve heard of people who have jumped to their deaths below. I wonder how long it would take me to climb over the railing and then simply jump off. What would it feel like to fall? Would it be like going down the rabbit hole? Down, down, down? And then what? I ask myself, which is worse? To live like this or to die?

(Pg 150) [Suddenly] I feel something warm rubbing against my leg, a small cat. I reach down and stroke its back. I feel all the bones in its spine. He looks cold, like me. (Pg 151-153) I believe that God has sent him to me to save me from the bridge. I call him Cheshire Cat, Cheshire for short. But he looks half-dead. Tweedle Dweeb says. . .

TWEEDLE VOICE: You should take him to the Cat Lady. This lady takes in stray cats and knows how to make them well. Haven’t you ever heard of her?

ALICE: We walk for miles and miles, or so it seems.

TWEEDLE VOICE: This is it. Go on . . . Knock on the door. Go on, Alice!”

ALICE: (knocks on the door – to woman) I, uh, I have a cat. He’s very sick. (to audience) I glance over my shoulder. The Tweedles have vanished. Were they even here at all? The woman reaches over and removes my lifeless cat.

FAYE: (Pg 159) My name is Faye, but lots of people call me the Cat Lady. (laughs) There are worse things to be called, you know.

ALICE: Yes, I know. There are things like “crazy girl” or “nut case” or “loony” or “weirdo.”

FAYE: (Pg 162) You and Cheshire can sleep in the spare bedroom.”

ALICE: Really? . . . .

FAYE: Really.

ALICE: (Pg 164) And it feels as though I am at home. Not home like where my mother lives, but home where I belong, like somebody really wants me. I hope it’s not just my mind playing tricks on me.

(Pg 175-177) [One] afternoon I sit in Faye’s living room and I notice how the glass in her big front window is becoming reflective like a mirror. I can see everything in the room behind me as if it’s really in front of me, as though I’m watching something in another world. It all seems so very far away, removed from me, like something I can never really belong to.

I wonder if this is how Alice felt in Through the Looking Glass. Perhaps, like me, she just didn’t fit in. I turn around to see that the exact same world is right behind me, only clearer and brighter and probably warmer than the one I’ve been looking at. For a moment I wonder which side is real.

FAYE: Are you all right, Alice? (Pg 181-182) It’s just me, Faye.

ALICE: (whispering) I am . . . well, I should leave. Your neighbors think I’m crazy. I am just a great big problem. (referring to the voices in her head that have been silent for a while) I’m worried that they’re going to find me. Or that they’ll tell you lies about me or that I’m not good enough.

(to audience) (Pg 187) I rack my brain trying to figure out what I must’ve done to deserve this kind of life.

FAYE: [Oh, honey.] God doesn’t punish us for our sins. He forgives us for sinning. (Pg 181) I think we’re all a little crazy. It’s not necessarily a bad thing. And when we don’t get along all right, we work together to resolve our little differences. TRANSITION It was hard for Alice not to trust Faye. And over time, she agrees to consider a unique treatment center for the psychologically challenged. A treatment center called Golden Home.

FAYE: (Pg 298) I can only tell you that I think it would be the best thing for you. But you’re the one who must make the final decision. No one is going to force you into this. And if Dr. Golden isn’t convinced you’re there of your own free will, he won’t even let you in.

ALICE: My own free will. (Pg 316) I am finally willing to admit I need help. (Pg 322) I really do want to get well. (beat) (Pg 338-339) I become anxious again, then remember the CD [that Dr. Golden gave me] on the practice of controlled breathing – an exercise that’s supposed to reduce anxiety. (inhale slowly, then slowly exhale x 2) And it’s not long before a strange sensation begins to wash over me. Peace. I am experiencing peace. And I believe it’s coming from God. It’s a beginning, a door.

When Alice stepped through the looking glass into a different world, it turned out to be a twisted and crazy world, not unlike the place I have wandered these last few months. Through this entrance, I [c]ould find myself in a better place where life makes sense. For the first time I sense a wave of real hope. And I want to hold on to it, savor it. (Inhale and exhale slowly) A small sense of control returns to me. And it feels good.

(Pg 350) [I realize that] I don’t need to have all the answers. It’s enough that I simply keep moving forward, one step at a time. So that’s what I’m doing. Sometimes I imagine myself as a little kid who’s learning to walk again. And if it’s rocky or rough, I envision God walking alongside me and holding my hand.

(Pg 371) I welcome each new day with the hopeful expectancy that I will rise above the ordinary. For I am not content to live a merely “normal” life or settle for an average existence. No, I am destined for more – much, much more.
```

---

## IC-2235: Fine Times: An Oral Memoir

- Title: Fine Times: An Oral Memoir
- Author (byline): Woody Allen
- Work: The Complete Prose of Woody Allen
- Publisher: Crown Publications
- Publication date as stated: Nov 1991
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1646
- Already set (do not supply): none

### Source block (context only)

```text
Author: Woody Allen
Book: The Complete Prose of Woody Allen
ISBN: 978-0517072295
Publisher: Crown Publications
Date (Month/Year): Nov 1991
```

### Introduction (context only: never use it for content warnings)

```text
Fine Times: An Oral Memoir by Woody Allen
```

### Performance text (classify this)

```text
The following are excerpts from the soon-to-be published memoirs of Flo Guinness. Certainly the most colorful of all speakeasy owners during Prohibition, Big Flo, as her friends called her (many enemies called her that, too, mostly for convenience), emerges in these taped interviews as a woman with a lusty appetite for living, as well as a disappointed artist who had to give up her lifetime ambition to become a classical violinist, when she realized it would mean studying the violin. Here, for the first time, Big Flo speaks for herself.

Originally I danced at the Jewel Club in Chicago, for Ned Small. Ned was a shrewd businessman who made all his money by what we would now call "stealing." Of course, in those days it was quite different. Yes, sir, Ned had great charm-the kind you don't see today. He was famous for breaking both your legs if you disagreed with him. And he could do it, too, boys. He broke more legs! I'd say fifteen or sixteen a week was his average.

But Ned was sweet on me, maybe 'cause I always told him straight to his face what I thought of him. "Ned," I told him over dinner once, "you're a mealymouth grifter with the morals of an alley cat." He laughed, but later that night I saw him looking up "mealymouth" in a dictionary.

Anyhow, like I said, I danced at Ned Small's Jewel Club. I was his best dancer, boys-a dancer-actress. The other girls just hoofed, but I danced a little story. Like Venus emerging from her bath, only on Broadway and Forty-second Street, and she goes night-clubbing and dances till dawn and then has a massive coronary and loses control of the facial muscles on her left side. Sad stuff, boys. That's why I got respect. One day, Ned Small calls me into his office and says, "Flo." (He always called me Flo, except when he got real mad at me. Then he'd call me Albert Schneiderman-I never knew why. Let's say the heart has strange ways.)

So Ned says, "Flo, I want you to marry me." Well, you could've knocked me over with a feather. I started crying like a baby. "I mean it, Flo," he said. "I love you very deeply. It's not easy for me to say these things, but I want you to be the mother of my children. And if you don't I'll break both your legs." Two days later, to the minute, Ned Small and I tied the knot. Three days later, Ned was machine-gunned to death by the mob for spilling raisins on Al Capone's hat.

After that, of course, I was rich. First thing I did was buy my mother and father that farm they'd always talked about. They claimed they had never talked about a farm and actually wanted a car and some furs, but they gave it a try. Liked the rural life, too, although Dad got struck by lightning in the north forty and for six years afterward when asked his name could only say the word "Kleenex." As for me, three months later I was broke. Bad investments. I backed a whaling expedition in Cincinnati, on the advice of friends.

******

I danced for Big Ed Wheeler, who made bootleg hooch that was so strong it could only be sipped through a gas mask. Ed paid me three hundred dollars a week to do ten shows, which in those days was big money. Hell, with tips I made more than President Hoover. And he had to do twelve shows. I went on at nine and eleven, and Hoover went on at ten and two. Hoover was a good President, but he was always sitting in his dressing room humming. It drove me crazy. Then one day the owner of the Apex Club saw my act and offered me five hundred dollars a week to dance there.

I put it squarely to Big Ed: "Ed, I got an offer of five hundred bucks from Bill Hallorhan's Apex Club."

"Flo," he said, "if you can get five hundred a week, I won't stand in your way." We shook hands and I went to tell Bill Hallorhan the good news, but several of Big Ed's friends had gotten there first and when I saw Bill Hallorhan his physical condition had undergone a change and he was now only a high-pitched voice that came from inside a cigar box. He said he had decided to get out of show business, leave Chicago, and settle down somewhere closer to the equator. I went on dancing for Big Ed Wheeler till the Capone mob bought him out. I say, "bought him out," boys, but the truth of it was Scarface Al offered him a tidy sum but Wheeler said no.

Later that day, he was having lunch at the Rib and Chop House when his head burst into flames. No one knew why.

I bought the Three Deuces with money I'd saved, and in no time it was the hot spot in town. They all came- Babe Ruth, Jack Dempsey, Jolson, Man o' War. Man o' War was there every night. My God, how that horse could drink! I remember once Babe Ruth had this crush on a showgirl named Kelly Swain. He was so crazy about her he couldn't keep his mind on baseball and twice greased his body, thinking he was a famous channel swimmer.

"Flo," he said to me, "I'm nuts about this redhead, Kelly Swain. But she hates sports. I lied and told her I give a course on Wittgenstein, but I think she suspects something."

"Can you live without her, Babe," I asked him.

"No, Flo. And it's affecting my concentration. Yesterday, I got four hits and stole two bases, but this is January and there are no games scheduled. I did it in my hotel room. Can you help me?"

I promised him I'd speak to Kelly, and the next day I stopped by the Golden Abattoir, where she was dancing. I said, "Kelly, the Bambino is nuts about you. He knows you like culture and he says if you date him he'll give up baseball and join the Martha Graham troupe."

Kelly looked me squarely in the eye and said, "Tell that palooka I didn't come all the way from Chippewa Falls to wind up with some overstuffed right fielder. I got big plans." Two years later, she married Lord Osgood Wellington Tuttle and became Lady Tuttle. Her husband gave up an ambassadorship to play shortstop for the Tigers.

Jumpin' Joe Tuttle. He holds the record for most times beaned in the first inning.

Gambling? Boys, I was present when Nick the Greek got his name. There was a small-time gambler named Jake the Greek, and Nick called me and said, "Flo, I'd like to be The Greek."

And I said, "I'm sorry, Nick, you're not Greek. And under New York State gambling laws it's forbidden."

And he said, "I know, Flo, but my parents always wanted me to be called The Greek. You think you could arrange a lunch meeting with Jake?"

I said, "Sure, but if he knows what it's for he won't show."

And Nick said, "Try, Flo. It would mean a lot to me."

So the two met at the Grill Room of Monty's Steak House, which did not allow women but I could go there because Monty was a great friend of mine and didn't regard me as either male or female but, in his own words, "undefined protoplasm." We ordered the specialty of the house, ribs, which Monty had a way of preparing so they tasted like human fingers. Finally, Nick said, "Jake, I'd like to be called The Greek."

And Jake turned pale and said, "Look, Nick, if that's what you got me here for-" Well, boys, it got ugly. The two squared off. Then Nick said, "I'll tell you what I'll do. I'll cut you. High card gets to be called The Greek."

"But what if I win?" Jake said. "I'm already called The Greek."

"If you win, Jake, you can go through the phone book and pick any name you like. My compliments."

"No kidding?"

"Flo's the witness."

Well, you could feel the tension in that room. A deck of cards was brought out and they cut. Nick cut a queen, and Jake's hand was shaking. Then Jake cut an ace! Everybody let out a cheer, and Jake went through the phone book and selected the name Grover Lembeck. Everybody was happy, and from that day on women were allowed into Monty's, provided they could read hieroglyphics. I remember once there was a big musical review at the Winter Garden, Star-Spangled Vermin. Jolson was the lead, but he quit because they wanted him to sing a song called "Kasha for Two," and he hated it. It had the line in it "Love is all, like a horse in a stall." Anyway, eventually it was sung by a young unknown named Felix Brompton, who was later arrested in a hotel room with a one-inch cardboard cutout of Helen Morgan. It was in all the papers.

Well, Jolson come into the Three Deuces one night with Eddie Cantor, and he says to me, "Flo, I hear George Raft did his tap dance here last week."

And I said, "George has never been here."

And he said, "If you let him do his tap dance, I'd like to sing."

And I said, "Al, he was never here."

And Al said, "Did he have any accompaniment on piano?"

And I said, "Al, if you sing one note I'll personally throw you out." And with that Jolie got down on one knee and started on "Toot-Toot Tootsie." While he was singing, I sold the place, and by the time he was finished it was the Wing Ho Hand Laundry. Jolson never got over that or forgave me for it. On the way out, he tripped over a pile of shirts.
```

---

## IC-2236: Fireworks from Above

- Title: Fireworks from Above
- Author (byline): Faye Lane
- Work: The Moth: 50 True Stories; Pgs 385-391
- Publisher: Hachette Books
- Publication date as stated: Sept 2013
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: FAYE, CEO, WOMAN, MAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1790
- Already set (do not supply): none

### Source block (context only)

```text
Author: Faye Lane
Book: The Moth: 50 True Stories; Pgs 385-391
ISBN: 978-1401311117
Publisher: Hachette Books
Date (Month/Year): Sept 2013
```

### Introduction (context only: never use it for content warnings)

```text
Are you a people person? Let’s check. Take a moment to think about people and things that irritate you – that make you angry . . . (pause) Okay, okay . . . that’s plenty. If you are like me there’s a whole list of things that cause frustration for you every single day. But you know what?

Every day, we have a choice regarding how we view the world. We cannot change our past. We cannot change the way others choose to act. We cannot change the inevitable. The only thing we can do is play the one card we have – our attitude. I am convinced that life is 10% what happens to us and 90% how we react to it.

Let me give you another example: Fireworks from Above by Faye Lane
```

### Performance text (classify this)

```text
FAYE: (Pg 385-391) What I always wanted as a little girl was to tell stories on the stage, because I wanted to be connected to something bigger than myself, and I wanted to be connected to other people. And I believe that a really good performer takes a group of individuals and, through a shared emotional experience, turns it into a collective. For as long as I can remember, I’ve wanted to do this. I’ve wanted to be a performer. . . slash STEWARDESS!

FAYE: I grew up in my mama’s beauty shop in Texas. It was this old A-frame house with big mirrors and swivel chairs in the front room and shampoo bowls in what had been the back bedroom. My mama had this long line of hood dryers on one wall, and I would wait until all the ladies were held captive under the dryers and give mandatory concerts. That was my very first stage.

When I wasn’t telling stories and doing show for the ladies, I would play stewardess, and I would push this little manicure cart around the beauty shop. (with thick Southern drawl as she enacts this memory) "Miss Helen, Miss Melba, would y'all like a magazine? Would y'all like a cocktail?"

And the ladies would say, "Baby, you just give great cus-tomer service." I was all about customer service.

And sometimes I'd sit on the porch playing with my Barbie's Friendship airplane, and I would wear this long, silk scarf tied on the side (and it's hot in Texas in the summer). But I loved playing stewardess.

Well, about 10 years ago, I was living in New York City, working as a performer, telling stories and singing songs on the stage. Bad pay, no job security, no benefits. I really needed a job. And I very randomly met this lovely girl with a long, silk scarf tied on the side, who said nine words that changed my life forever: "Have you ever thought about being a flight attendant?"

I had!

Three weeks later, I was in Miami training. Training was so exciting. It was a brand-new airline. They had seven airplanes, a handful of destinations, and a lot of great buzz. They had buzz around the fact that there was live TV at every seat. And they had blue potato chips and designer uniforms. But most of the buzz was around the fact that they had amazing customer service. Perfect! I was all about customer service back at the beauty shop.

And when the founder and CEO of the airline came into our training class and gave this amazing, uplifting speech, I knew I was in the right place.

CEO: Every one of you is here for a reason, and that reason is your ability to smile and be kind. We can teach you how to evacuate an airplane. We can teach you how to handle a medical emergency. We can teach you how to serve. But we cannot teach you to smile and be kind. Your mother did that. Please thank her for me.

FAYE: So beautiful. He said he saw this not as an airline, not as a corporation, but as a humanitarian experiment. He said his goal was to bring humanity back to air travel. I was right on board with this vision. I was so caught up in it. And when I graduated, they made me president of my class, and they even gave me this special certificate called the Spirit Award.

I couldn't wait to get out there on the line -- to surprise people with kindness and, in the process of moving people from Point A to Point B, really, actually move people. And then I graduated and started the job. Maybe you see where this is going. I had this epiphany almost right away: This job is hard, and people are horrible! Really horrible.

First of all, the job was physically exhausting. In the beginning I was on reserve, which meant I was on call and had to be within 2 hours of Kennedy Airport at all times.

So I was either running to get to the airport or waiting for the phone call to run to get to the airport, constantly on edge.

And then the actual commute to the airport was extremely hard. I had to take the subway to the bus to the shuttle to the terminal. Even before I got on the plane, I was exhausted. And then when I did get on the plane, there was a whole world of hurt.

My feet hurt. There's this thing that happens where you get bruises on the bottom of your feet from turbulence, and it was horrible. And new flight attendants are sick a lot, because it's kind of like being a kindergarten teacher - - you're exposed to a lot of germs. At one point I had pinkeye in both eyes, a sinus infection, a double ear infection, and strep throat all at the same time. I couldn't see, I couldn't hear, I couldn't talk. And it was mainly because I was taking garbage from everyone all day. And saying "thank you" for it!

"Thank you. Thank you for your garbage. Thank you." They actually made us stop calling it trash. We had to call it "service items," because some of the really bitter girls would say, "Sir . . . you('re) trash," "Ma'am . . . your whole family's trash."

But I understand why they were jaded, because I was kind of getting jaded too. I just couldn't believe how horrible people could be. It's really hard to be mean when someone is smiling at you and handing you a cup of coffee and a cookie, but people are. Because a lot of times they don't see you -- they just see a uniform.

And traveling is hard. It's stressful, and people get ugly. I tried really hard to keep that vision and to smile and be kind, even in the face of meanness. But I hit bottom one day when I had a passenger who had a heart attack on my flight. He was lying in the aisle, and we had opened his shirt and had the pads of the defibrillator on him. I was holding an oxygen bottle. And this woman in the row sitting next to me kept tugging on my blouse:

WOMAN: Excuse me. Excuse me!

FAYE: (to woman) Just a minute, please. We're trying to save this guy's life. (to audience) She kept tugging and tugging . . . (to woman) Just a minute! JUST A MINUTE!

(to audience) And then I thought: Wait a minute. Maybe she has an emergency, or maybe she knows something. (to woman) What is it? (to audience) And she held up her coffee cup

WOMAN: This coffee is cold.

FAYE: And I learned that people can be cold. There's something that happens to your psychology because you see the world from above when you fly a lot. And I saw a lot of really horrible things from the air, like devastating California forest fires, New Orleans under water, and most upsetting for me, lower Manhattan smoldering for weeks and weeks.

In late September of 2001, I was working a flight, and a passenger came on with a garbage bag, which is kind of a flight attendant pet peeve, because, "Really, sir, a garbage bag? 14th Street, $9.99. Get a roll-aboard." You know? But you see that. Sometimes people just throw things in a garbage bag and bring it on.

So he goes to row two, which is where he was seated, and he opened the overhead bin and put the garbage bag in. And my next thought was: What's in that garbage bag? Because in late September of '01, we were all still a little edgy and paranoid, so I was kind of keeping my eye on him and the bag. And he put it in the overhead bin and closed the bin and stood there with his hand on it, guarding it.

Which is another flight attendant pet peeve. The overhead bins are shared space, okay? And if you hog up all the space, somebody's bag is gonna get checked. And by the way, if you're in row 12, please don't leave your bag in row 1. It's not nice. You're taking somebody's space.

So my instinct was to go up to this man and say, "Sir, please sit down." But I thought: Just let it go. Just smile and be kind, and if we need the space, I'll deal with it later. [Then] he got up while the seat belt sign was on and stood, waiting for the bathroom. If the seat belt sign is on, it's because the captain knows something we don't know, okay? (to man) Sir, the seat belt sign is on.

MAN: I know, I know, but I really need to go.

FAYE: (to audience) And I thought: Let it go. Just let it go. I was sitting on the jump seat, and it was kinda awkward because he was just standing there, and I felt like I should say something. (to man) Are you traveling for business or pleasure?

MAN: Neither. I live in California, but I came to New York because my son was a first responder at Ground Zero, and he died there. I came to pick up his uniform, which is all I have of him.It's in a bag in the overhead bin.

FAYE: And I remembered why I was there and why I wanted that job. I remembered that everybody has a story, and I don't know what that story is. People fly for a reason. Maybe they're going to a funeral or to see someone who's sick, or maybe it's something joyful, like a wedding. I don't know what their story is, but for that little piece of time, I'm a part of it, and I have an impact on their experience.

What I love about performing is taking a group of indi-viduals and, through a shared emotional experience, turning it into a collective. But my job as a flight attendant is to take a collective and to turn it back into a group of individuals.

Flight attendants talk about "crowds" sometimes, like, "Avoid the Fort Lauderdale crowd. They're horrible," or "Avoid the Long Beach crowd." But every crowd is a group of individuals, and every individual has a story. And yeah, I’ve seen a lot of horrible things from the air. But I've also seen a lot of amazing, beautiful things, like the Grand Canyon, the Northern Lights, fireworks from above.

And now when I go through the cabin with my garbage bag, saying "thank you" and smiling, I mean it, because I'm making a gratitude list in my head. And every time I say, "thank you," I think of something I'm grateful for: "Thank you" (for my job). "Thank you" (for these comfy shoes). "Thank you" (for my life). Because my job enables me to be part of something bigger than me, and to be connected to other people, like this. So thank you.
```

---

## IC-2237: Forgiveness

- Title: Forgiveness
- Author (byline): Rebecca Brown
- Work: Terrible Girls
- Publisher: City Lights Publishers
- Publication date as stated: Jan 2001
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1870
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rebecca Brown
Book: Terrible Girls
ISBN: 978-0872862661
Publisher: City Lights Publishers
Date (Month/Year): Jan 2001
```

### Introduction (context only: never use it for content warnings)

```text
Relationships are complex. How far would you go to prove your love? And if you do sacrifice for someone else, give everything you have for that special someone; how do you deal with it if that same devotion and love is not returned? Do you forgive and forget?

To forgive the perpetrator is to blame the victim. To forgive the perpetrator is to set up a system in which people who are not sorry are given a free pass to continue their behavior. The only people we need to forgive is ourselves. Let go of your anger at yourself for having trusted untrustworthy people. Let go of your anger at yourself for being naive. Forgive yourself for making bad choices.

Forgiveness by Rebecca Brown personifies the sacrifices made in the name of love by one woman and her path to forgiveness – forgiveness not for her partner, but for herself.
```

### Performance text (classify this)

```text
When I said I’d give my right arm for you, I didn’t think you’d ask me for it, but you did.

You said, Give it to me.

And I said OK.

There were lots of reasons I gave it to you. First of all, I didn’t want to be made a liar of, (I had never lied to you.) So when you reminded me that I’d said it and asked me if I really meant it, I didn’t want to seem like I was copping out by saying that I’d only spoken figuratively. (It is an old saying, after all.) Also, I had the feeling you didn’t think I would really do it, that you were testing me to see if I would, and I wanted you to know I would.

Also, I believed you wouldn’t have asked me for it unless you really wanted it, and needed it.

But then, when you got it, you bronzed it and put it on the mantel over the fireplace in the den.

The night you took it, I dreamt of arms. I slept on the couch in the den ‘cause I was still bleeding, even through the bandages, and I knew I’d stir during the night and need to put on more bandages and we didn’t want me to wake you up. So I stayed on the couch and when I slept, I dreamt of arms.

We kept my arm in the bathtub, bleeding like a fish. When I went to bed, the water was the color of rose water, with thick red lines like strings. And when I woke up the first time to change my bandages, it was colored like salmon. Then it was carnation red, and then maroon, then burgundy, then purple, thick, and almost black by morning.

In the morning, you took it out. I watched you pat it dry with my favorite big fat terry cloth towel and wrap it in saran wrap and take it out to get it bronzed.

I learned to do things differently. To button my shirts, to screw and unscrew the toothpaste cap, to tie my shoes. We didn’t think of this.

Together, we were valiant, brave and stoic. Though I couldn’t quite keep up with you at tennis anymore.

In a way, it was fun. Things I once took for granted became significant. Cutting a steak with a knife and fork, or buttoning my fly, untying a knot around a bag, adding milk while stirring.

After a while, I developed a scab and you let me come back to bed. But sometimes in the night, I’d shift or have a nightmare, jolt, and suddenly, I’d open up again, and bleed all over uncontrollably. The first time this happened neither of us could go back to sleep. But after a while, you got used to it and you’d be back asleep in a minute. It didn’t seem to bother you at all.

But I guess after a while it started bothering you, because one day when I was washing out the sheets I’d bloodied the night before, you said: You sleep too restless. I don’t like it when your bleeding wakes me up. I think you’re sick. I think it’s sick to cut off your own arm.

I looked at you, your brown eyes, innocent as a puppy. But you cut it off I said. You did it. You didn’t blink. You asked me for it, so I said OK.

Don’t try to make me feel guilty, you said. It was your arm. You didn’t blink. I closed my eyes.

That night I bled again. I woke up and the bed was red, all full of blood and wet. I reached over to touch you and to wake you up and tell you I was sorry but you were not there.

I learned more. To cook and clean, to eat a quarter pounder with one fist, to balance my groceries on my knee while my hand fumbled with the front door key.

My arm got strong, My left sleeve on my shirts got tight and pinched. My right shirt sleeve was lithe and open, carefree.

But then the novelty wore off. I had to convince myself. I read about those valiant cases, one-legged heroes who run across the continent to raise money for causes, and paraplegic mothers of four, one-eyed pool sharks. I wanted these stories to inspire me, but they didn’t. I didn’t want to be like those people. I didn’t want to be cheery and valiant. I didn’t want to have to rise above my situation. What I wanted was my arm. Because I missed it. I missed everything about it. I missed the long solid weight of it in my sleeve. I missed clapping and waving and putting my hand in my pocket. I missed waking up at night with it twisted behind my head, asleep and heavy and tingling.

And then I realized that I had missed these things all along, the whole time my arm had been over the mantel, but that l’d never said anything or even let myself feel anything bad because I didn’t want to dwell on those feelings because I didn’t want to make you feel bad and I didn’t want you to think I wanted you to feel bad.

I decided to look for it. Maybe you’d sold it. You were always good with things like that.

I hit the pawnshops. I walked into them and they’d ask me could they help me and I’d say, I’m looking for an arm. And they’d stare at me, my empty sleeve pinned to my shirt, or flapping in the air. I never have liked acting like things aren’t the way they are.

When I searched all the local pawnshops, I started going to ones further away. I saw a lot of the country. It was nice. And I got good at it. The more I did, the more I learned to do. The braver ones would look at me directly in the eye. They’d give me the names and addresses of outlets selling artificial limbs, or reconstructive surgeons. But I didn’t want another one, I wanted mine. And then, the more I looked for it, the more I wondered if I wasn’t looking more for something else besides my severed arm. I wondered was I really searching for you?

It all came clear to me. Like something hacked away from me; you’d done this to me as a test. To show me things. To show me what things meant to me, how much my arm was part of me, but how I could learn to live without it. How, if I was forced to, I could learn to get by with only part of me, with next to nothing. You’d done this to me to teach me something.

And then I thought how, if you were testing me, you must be watching me, to see if I was passing. So I started acting out my life for you. And then I felt you watching all my actions. I whistled with bravado, jaunted, rather than walked. I had a confident swagger. I slapped friendly pawnshop keepers on their shoulders and told them jokes. I was fun, an inspiration they’d remember after I’d passed through.

I acted like I couldn’t care less about my old arm. Like I liked the breezes in my sleeve.

I began to think in perfect sentences, as if you were listening to me. I thought clear sentences inside myself. I said, I get along just fine without my arm. I think that I convinced myself, in trying to convince you, that I had never had an arm I’d lost.

Soon I didn’t think the word inside me anymore. I didn’t think about the right hand gloves buried in my bottom drawer.

I made myself not miss it. I tested myself. I sat in the den and stared at the empty space above the mantel. I spent the night on the couch. I went into the bathroom and looked in the tub. I felt nothing. I went to bed.

I thought my trips to pawnshops, my wanderlust, were only things I did to pass the time. I thought of nothing almost happily.

I looked at my shoulder. The tissue was smooth. I ran my fingers over it. Round and slightly puffed, pink and shiny and slick. As soft as pimento, as cool as a spoon, the tenderest flesh of my body.

My beautiful empty sleeve and I were friends, like intimates.

So everything was fine.

For a while.

Then you came back.

Then everything did.

But I was careful. It had been a long time. I had learned how to live. Why, hadn’t I just forgotten what used to fill my empty sleeve entirely? I was very careful. I acted like nothing had ever been different, that you had never ripped it out of me, then bronzed it, put it on the mantel, left with it. I wanted things to stay forgot.

So we were sitting in the den. You looked at me with your big brown eyes and you said. “Oh, I’m so sorry. Can you ever forgive me?” You started crying, your lips quivering.

Why did you do it? I whispered.

You looked at me, your eyes all moist and sweet like you could melt anything in the world. You didn’t answer.

What did you do with it?

You shrugged your shoulders, shook your head and smiled at me.

Say something. Say something, goddammit.

[But instead of answering], you chatted to me about your adventures. You told me you’d worked hard in the time you’d been away. You told me you had grown. You told me how much you had learned about the world, about yourself, about honor, faith and trust . . . You looked deep into my eyes and said, I’ve changed. You said how good and strong and true and truly different you were. How you had learned that it is not our acts, but our intents, that make us who we are.

I watched your perfect teeth. I felt your hands run over the empty sleeve that rumpled on the exposed side of me. I closed my eyes and couldn’t open them. My mouth was closed. I couldn’t tell you anything.

I couldn’t tell you that you can’t re-do a thing that’s been undone. I couldn’t tell you anything that you would understand. I couldn’t tell you that it wasn’t just the fact that you ripped it out of me and taken it and mounted it, then left with it, then lost it. How it wasn’t only that, but it was more. How it was that when you asked me, I believed you and I told you yes. How, though I had tried a long time to replace what you had hacked away from me, I never could undo the action of your doing so. How I believed with all my heart, that given time, you’d do something else again . . . again. And then I thought that I would never believe you again, never forget what I know of you, never forget what you’ve done to me, what you will do. I’ll never believe the myth of forgiveness between us.
```

---

## IC-2238: Freak the Geek

- Title: Freak the Geek
- Author (byline): John Green
- Work: Geektastic: Stories from the Nerd Herd
- Publisher: Little, Brown Books for Young Readers
- Publication date as stated: Aug 2009
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1723
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Green
Book: Geektastic: Stories from the Nerd Herd
ISBN: 978-0316008099
Publisher: Little, Brown Books for Young Readers
Date (Month/Year): Aug 2009
```

### Introduction (context only: never use it for content warnings)

```text
First off, let me start out by saying being a geek is cool. It's awesome, even. The geeks are the better species. I, for one, take pride in the fact that I am a geek. But unfortunately, almost every geeky kid gets socially ostracized. Almost all get mocked. In fact, almost all face some physical abuse. In fact, at the Hoover Preparatory School for Girls . . . . it’s tradition. Freak the Geek by John Green.
```

### Performance text (classify this)

```text
Right after our last class, Kayley and I are walking past the only bit of stone wall that survived the epic 1922 fire that nearly destroyed Hoover Preparatory School for Girls. The only redeemable facet of Hoover is Kayley herself, who is about the best baof one could ask for. (Baof meaning, of course, best and only friend; it is the final frontier in friendship, the heady waters out past the Sea of Bff.)

Hoover Preparatory School for Girls has a number of profoundly stupid traditions--such as the singing-the-alma-mater-song-every-Thursday-at-lunch tradition, and the stand-when-your-teachers-enter-the-classroom tradition, and the everyone-has-to-wear-the-exact-same-uniform-so-that-no-one-will-beable-to-tell-who-the-geeks-are-except-of-course-everyone-can-tell-who-the-geeks-are-because-geek-isn't-something-you-wear-it-is-something-you-are tradition.

As it happens, I think doing things solely because they were done in the past is absolutely idiotic. I suppose it shows respect to our teachers when we stand every time they come into the room, but you know what would show more respect? If the insolent students who have colonized this awful place paid attention in class. Or took notes.

Witness, for instance, seventh period: AP Physics. In the row before me, Amber and Nataley quietly discuss whose basically identical calf-length white socks are cuter. ("No, yours are," Amber whispers, when Dr. Halfrecht turns around to draw a diagram of how one can measure the speed of light. "No,"

Nataley mouths silently in response. "Yours are adorable.")

The weirdest things get cool sometimes. This is why I have never taken a lot of stock in 'being' cool (as if popularity is something that inhabits you, permanently, a virus that overwhelms your immune system so completely that you cease to 'be' you; instead you have become cool).

Hoover is all right. But the incessant fetishizing of traditions? Unbearable. And so when, someone runs past Kayley and me and whispers "Freak the Geek," I am doubly pissed. First, I am pissed because Freak the Geek is a tradition. And second, I'm pissed because you only hear those words whispered to you when you are one of the geeks who are about to get freaked. I'm not ashamed that I love Dr. Who, or that I've read ten thousand pages of HP fanfiction online. I'm not even ashamed about my Pokemon addiction. (Okay, a little.) I like being a geek. But no one--not even the hard-core geeks who have g-e-e-k tattooed on their knuckles-- wants to be one of THE geeks.

Kayley and I wheel around simultaneously, trying to identify the whisperer. But she's already several paces away, just a narrow-hipped body with a blond ponytail bobbing around. She could be any of us, really. And that's the idea, I guess: Freak the Geek is the one day each year when everybody at Hoover gets to be One of Us--except, I suppose, for Kayley and me. I feel weirdly embarrassed, like I've disappointed the universe by failing to claw far enough out of the social-caste basement to escape whatever humiliation awaits.

We know the drill, because we've seen geeks Freaked our freshman and sophomore years. The entire class gets together and on a chosen day in the second semester of junior year, they pick two geeks to Freak. Freaking takes various forms, of course: They might drag you by the ankles to the pond and throw you in, or they might egg your car with three hundred eggs.

Kayley and I don't say anything; we just take off sprinting toward my car. I figure it's our best chance. But when we get within view of the parking lot, I see fifty girls standing in concentric rings around my SUV. Each of them appears to be holding a gun.

"Jesus, Lauren," she mumbles under her breath to me, "have they renamed it Kill the Geek?" One of them-raises her weapon toward us. It's a strange-looking gun, with a pink handle and an exceptionally long barrel. I'm pretty sure it doesn't shoot bullets, but even so I dive for the ground and cover my head. Kayley just stands there, and when I look up at her, she's shaking her head. "Paintballs?!" she shouts.

"Paintballs?! The whole world of mischief and malfeasance is available to you and you pick PAINTBALLS?! You disappoint me, ladies." The sound is a loud puff of air.: Kayley doesn't even flinch when a splatter of scarlet red paint bursts a foot away from her head against one of our campus's famed live oaks.

We take off running together, away from the parking lot toward the lacrosse practice field. I don't hear any more paintball firings as I race across Hoover Green. I want to run back toward the classrooms, because surely someone will help. I mean, the administration has no official policy on Freak the Geek because they love traditions too much to denounce any of them, but they wouldn't let this happen to us. But Kayley grabs me, steering me toward the woods. "We just need a teacher," I say. I can hear them behind me, some girl shouting, "Switch to automatic mode, Scarlet Ballers!" Kayley swivels around and starts running backward long enough to shout, "You call yourselves the Scarlet Ballers and we're the geeks?"

Kayley shouts, "Lauren, come on. Fast." We're almost across the lacrosse field now, a thick stand of trees before us, and the Freakers must have terrible aim or else paintball guns are hard to shoot, because the trees are soon riddled with abstract paintings in red, but nothing's hit me yet and then finally we're in among the trees.

And here is our advantage: The Freakers might be in better physical shape than us, but no one knows these woods like Kayley and me. We've been walking around the hundreds of acres of forest on Hoover's campus for three years' worth of lunch periods. Both the food and the atmosphere at the cafeteria are unbearable, and anyway, we've never really gotten along terribly well with the girls who eat there--which is to say all of them.

"I never really thought about it before," I tell Kayley as we simultaneously duck under a low-hanging oak branch, "but just the phrase 'Freak the Geek' is just hugely lame."

By the time we crest the hill, I can't even hear the Freakers anymore. , I feel good. I wish they hadn't picked us. There are plenty of unpopular people to go around--the drama kids who do the tech work, the girl who single-handedly runs the student newspaper, the girls who Kayley and I play Pokemon with in the student lounge during free periods--but if they had to pick us, at least they've picked BOTH of us.

We descend the other side of the hill, headed toward the cemetery where the school founder and her family are buried. I know we're near the bottom when I hear Hoover Creek.

"The bridge," I say.

"Kayley and I had spent many lunches under the bridge--the cement outcropping lets us sit with our legs dangling over the water, which ran loud enough to muffle our voices to anyone walking or driving above, but quiet enough that we could always hear each other. I reach the bridge a couple minutes later and sit down next to Kayley, who is staring into the water.

She doesn't say anything to me, so after a while, I tell her, "I feel kinda like an ork, hiding out under a bridge."

"A troll," she says, and then sighs. "You feel kinda like a troll."

"No, trolls are people. I don't feel like a person. I feel like an ork," I insist.

She sighs again, this time clearly annoyed. "Lauren," she says. "You're so stupid sometimes. Trolls are not people. Orks are not people. Only humans are people. Orks are from Tyrol folklore, and they live on mountains. Trolls live under bridges. And they have really long hair and big noses, and that's clearly what you mean when you say ork."

I reach over and put my hand on her shoulder and say, "Okay. Sorry. I meant trolls. Jeez, are you okay?"

"Yeah, Lauren, I'm splendid. Everyone in my entire class is trying to attack me with paintball guns, and I've officially been declared one of the two least liked people in my peer group, and my best friend doesn't know crap about folklore, and I'm dirty and sweaty and gross and just splendid."

"Well, you don't have to be bitchy," I say. "It's not my fault."

She says nothing.

"It's not my fault," I repeat, and she says nothing, and then smaller, I say, "You think..."

She takes that as a start. "I think that sometimes you can be a little...I don't know. Meek. And they prey on that. So they prey on us."

I just stand up and climb out from under the bridge. Maybe what bothers me so much is the thought that Kayley might be right, but mostly I'm just furious with her for even thinking that, let alone saying it out loud.

"Where are you going?" she asks.

"To the car," I say as I walk away. I'm talking so softly she probably can't even hear me. "All things being equal, I would rather be paintballed."

I'm walking for about thirty seconds when I hear Kayley's footfalls behind me. "I'm sorry," she says.

I wheel around. "You know, you're a total know-it-all. And it's incredibly rude sometimes; I mean, you're not perfect either, and you act like it's my fault but it's not my fault for being quiet or your fault for being a know-it-all. It's not your problem or my problem; it's their problem. They're the demented ones, not us, so don't take it out on me, because the only thing that holds anything together for me is having someone else on the Not Demented Team."

Kayley just nods, and then we stand there for a second, and then she hugs me. She says, "I'm sorry," and I can hear her crying in her voice a little.,. “For now, let us return to your car."

By the time we make it to the car, in the gray twilight, I've forgotten our fight entirely in a way that the Freakers never forget their fights, because their fights are all they have. The Freakers have gone home, their cars all disappeared from the parking lot.

There's a single lipstick-red splotch of paintball goo on the front grill of my car. It doesn't wash off for months, but I don't mind. It is not my scarlet letter. It's theirs.
```

---

## IC-2239: From Far Around They Saw Us Burn

- Title: From Far Around They Saw Us Burn
- Author (byline): Alice Jolly
- Work: The Best Short Stories 2021
- Publisher: Anchor
- Publication date as stated: Sept 2021
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1237
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alice Jolly
Book: The Best Short Stories 2021
ISBN: 978-0593311257
Publisher: Anchor
Date (Month/Year): Sept 2021
This story is based on documents and personal testimony
relating to the fire at St. Josephs orphanage in Cavan on the
night of February 23,1943.
```

### Introduction (context only: never use it for content warnings)

```text
St. Joseph's Orphanage and Industrial School, the institution once run by the Poor Clare Sisters in Cavan town, has largely been forgotten; but it outraged the whole of Ireland over 70 years ago after a terrible fire broke out in the basement laundry in the early hours of a February morning in 1943.

Incredibly, when alerted to the gathering smoke by an orphan girl, a senior nun made the decision not to evacuate the children, instead she directed them to the top floor dormitory and closed the doors. Thirty-five children burned to death. The nuns survived.

From Far Around They Saw Us Burn by Alice Jolly
```

### Performance text (classify this)

```text
We are the children of Cavan. Do you know of that place? It is a border town, betwixt and between, a place of crossroads--and yet strangely few pass by there. Walking the main street, you pass the Central Hotel and Sullivans the General Store. And then, of course, the Convent buildings and the orphanage.

Those buildings are there and yet they are not. For that place is never opened up, the nuns being a closed order, so though many windows face onto the street, the glass obscured by bars. We orphanage girls are never seen. And should you ever have cause to knock, the nun who unlocks the door will keep to the side so that you may not see her, for that is the way of our world.

It was the Sullivan family who knew of it first -- smoke, smoke, pumping out of a vent in the orphanage wall. We orphanage girls felt it first as a settling of boards, the scraping of a hinge, a sound like a yawn, a taste of ash. But we were feared to get up. We lay rigid in our beds. Ten to two.

Suddenly, the lights came on and we all stood blinking in our white night dresses, standing between the six rows of iron beds.

Later, it was recorded that it was Cissie Reilly started banging. For how else could they wake the sleeping nuns and alert them to the danger? Then John McNally was kicking with stout boots.

Get the children out. Do you not see? The fire is spreading. But a nun said No, no. It is the fire in the laundry which must be put out. So a group of them ran to the laundry door but it was locked. The nuns said, You must wait for the key. But the men knew better and kicked it in.

We girls were waiting in the dormitory, our hands knotted together, the little ones silent and hollow-eyed. When Miss O'Reilly came in, she was not at all fussed. She said, Get down on your knees and pray. Say an Act of Contrition.

Some of us then crowded to the window. From there we saw a group of had gone into the infirmary and were carrying out the babies. Then the door burst open, and girls started pouring out, their white night dresses swelling as they ran. A girl burst out, and the soles of her feet were burning. She ran screaming across the courtyard, her arms waving, her eyes rolling. Screaming and screaming, her feet blazing fire.

My sister, my sister. I must get her down. That shout came from Kathleen, looking for Bernadette. Other voices came up from down the wooden stairs. Then banging and coughing, a sound of choking. But no one came up the stairs, only a wall of smoke.

We said to each other We must pray. But we could think of no prayers. We need to have air. We need to have air.

Then suddenly all was dark -- We heard a door breaking somewhere close and a rush of air, which pushed the smoke further upon us. We were blown back into the room by the force of it. All below was alight. Blessed Mary have mercy on us.

[It was] forty feet up to our dormitory. We knew we were trapped. Ladders were the only hope. We opened the windows and bashed on the sections which did not give. Sparks, fire balls, and pieces of slate were raining down.

Then a girl jumped, rising up first, so it seemed, like some great white bird, then dipping down, falling faster and faster through the air. Even the blankets spread out below could not break her fall.

Some of us sat on the beds and gathered the smaller children around us. Hail Mary, full of Grace, the Lord is with thee. Pray for us sinners now and at the hour of our death. Dear Lord, we were trying. But the little children were all screaming.

We heard a rush and crash as the wooden stairs below us collapsed. The window was burning hot. The glass cracking, blowing out, melting down. The floor started to go. Wardrobes and beds disappeared into the furnace. One girl was lying unconscious on her bed, the clothes on her back on fire. Then she disappeared. Only those of us on the windowsill now were left. The men were calling up: Come on, girl. Come on. Jump. Jump. It was too far down.

Praise God a man came with a ladder. He put out his hands and pulled some of us off, placing us on the ladder so that we might get down. But when it came to the turn of Bernadette, who was but seven years old, she tried to go back into the room, such was her terror. Theresa went after her and got hold of her by the hair, dragged her toward the man on the ladder so that he got her down. Though by then Bernadette’s back and hair were flaming. As he came down, flames smashed out through the window above. A roar, a heaving, a smash of timbers. The time was 2.40 a.m.

The next day, the orphanage was nothing but a burnt-out frame -- damp wisps of smoke curling out through the debris. Only the many iron beds could you see still standing, stuck up in curved shapes, like the rib cages of so many skeleton beasts. All the businesses in the town were closed and a sickening smell spread all about.

It was not until darkness was falling that all the bodies were brought out. The men shouldered the coffins and took them to the Convent chapel, laid them down near the altar. Thirty-five girls but only eight coffins.

*****

Later, we were asked--those of us who still had tongues to speak--about what happened. We were asked again and again: You knew the instructions in case of a fire, so why did you not follow those procedures? Yet that question was never asked of the nuns.

It was said, many of those orphan girls are simple. But we were not simple, we were frightened. Mother Carmel would strip your clothes from your body, beat you skinless.

Questions were asked about the fire escape. It was but seven foot away from the dormitory, so why were the children not able to get out? And the lights in the building, why were they switched off? Miss O'Reilly was questioned at some length. Was there not a full fifteen minutes during which those children could have been brought down? In the town it was whispered, It was because those girls must not be seen in their nightdresses by the men of the town. All of the nuns safe enough, so God be praised.

Many years have passed now. It was long ago. But we are still waiting. We are the children of Cavan. Have you heard speak of us? From all around they saw us burn but none could help. It was discipline and fear which killed us [they said], not the wire in the laundry clothes dryer.

We are still waiting at the window. Please, will you bring the ladder up to us? Or must we run to heaven with our feet on fire?

We are the children of Cavan. From all around they saw us burn . . .
```

---

## IC-2240: From Mother . . . With Love

- Title: From Mother . . . With Love
- Author (byline): Ellen Gilchrist
- Work: Early September
- Publisher: Nelson Canada
- Publication date as stated: 1980
- Event as filed: Prose
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2154
- Already set (do not supply): none

### Source block (context only)

```text
Author: Zoa Sherburne
Book: Early September
ISBN: 978-0176014278
Publisher: Nelson Canada
Date (Month/Year): 1980
```

### Introduction (context only: never use it for content warnings)

```text
Letting go of a child is hard for every mother to deal with. Yet perhaps, it is even harder for a child to let go of her mother. Minta Hawley grapples with her mother’s eminent death in “From Mother…With Love” bu Zoa Sherburne.
```

### Performance text (classify this)

```text
The day that Minta Hawley grew up was a crisp golden day in early September.

It began like any other Saturday, with Minta lying in bed an extra hour. Breakfast was always lazy and unhurried on Saturday mornings. The three of them in the breakfast room. Mom, Dad and Minta.They talked, the casual happy talk of people who love each other and don't have to make conversation. About neighborhood doings . . . about items in the paper . . . about the clothes Minta would need when she went away to school in a couple of weeks.

It was after the dishes were finished that Minta's father asked her if she would like to go down to the beach for a little while. "Low tide," he said. "Might get a few clams."

He was silent as they drove toward the beach, but it wasn't the companionable silence that Minta had come to expect from him. There was something grim about it. "He's going to talk to me about school," Minta told herself. "He's going to try to talk me out of it again."

Last year was different. With mother just recovering from that operation it was natural that he should expect Minta to stay home; she had even wanted to stay. But now going to MaryHill was something special. She would live in a dormitory and be part of all the campus fun. It wasn't as if MaryHill were clear across the country, either, she'd probably be getting home every month or so . . . and there were the Christmas holidays . . . and then spring vacation.

Minta's chin was lifted in a stubborn line as her father parked the car and went around to get the shovels and pail form the trunk. It wasn't like him to be so stubborn; usually he was jolly and easy going and inclined to leave such matters entirely up to Minta's mother.

She followed him down to the beach, her boots squishing in the wet sand. The tide was far out and farther up the beach she could see bent figures busily digging along the water's edge. A scattered beach fire smoldered near the bank and Minta poked it into place and revived it with splinters of driftwood until she had coaxed back a steady warning blaze. When she sat back on her heels to smile up at her father she felt her throat constrict with a smothering fear. His eyes looked the way they had when. . .When?

Suddenly she remembered. He was looking at her and trying to smile, just the way he had looked at her the time her appendix burst and they were taking her to the hospital. She could almost hear the wail of the ambulance siren and feel the way he had held her hands tightly, trying to make it easier. His eyes had told her then, as they told her now, that he would a thousand times rather bear the pain than watch her suffer.

He took her hand and pulled her to her feet and they started walking up the beach slowly, not toward the group of people digging clams, but in the other direction, toward the jagged pile of rocks that jutted out into the bay.

"I went to see Dr. Morton last week, Minta. I've been seeing him pretty regularly these last few months."

She flashed a quick frightened look up at him. "You aren't ill?"

"No." He sighed and it was a heartbreaking sound. "No. It isn't me. It's your mother. That's why I don't want you to go to MaryHill this year."

"But . . . but she's feeling so much better, Dad. even taking on a little weight–" She broke off and stopped walking and her hand was steady on his arm. "Tell me," she said quietly.

Her mother was going to die To die. Her mother. To die, the doctor said. Three months, perhaps less. . . . Her mother who was gay and scatterbrained and more fun than anyone else in the world. Her mother who could be counted on to announce in the spring that she was going to do her Christmas shopping early this year, and then left everything until the week before Christmas. No one was worse about forgetting anniversaries and birthdays and things like that; but the easy-to-remember dates, like Valentine's Day and St. Patrick's Day and Halloween were always gala affairs complete with table favors and three-decker cakes.

Minta's mother wore the highest heels of any mother on the block. She was so pretty. And she always had time for things like listening to new records and helping paste pictures in Minta's scrapbook. She wasn't ever sick—

"I shouldn't have told you." Her father was speaking in a voice that Minta had never heard from him before. A voice that held loneliness and fear and a sort of angry pain. "I was afraid I couldn't make you understand, why you had to stay home . . . why you'd have to forget about MaryHill for this year." His eyes begged her to forgive him and for some reason she wanted to put her arms around him, as if she were much older and stronger.

"Of course you had to tell me," she said steadily. "Of course I had to know." And then—"Three months but Dad, that's Christmas."

He talked quietly, explaining, telling her everything the doctor had said, and Minta listened without tears, without tears, without comment. She watched his face as though it were the face of a stranger. She thought about a thousand unrelated things.

It was like coming back from a long journey when her father stopped talking and they turned back toward the car. "So that's why I can't let you go away, Midge." Her father's voice was very low and he didn't seem to realize that he had called her by the babyish name she had discarded when she started to first grade. "It isn't just your mother I'm thinking about . . . it's me. I need you."

She looked at him quickly and her heart twisted with pity. He did need her. He would need her more than ever.

"We can't tell her, Minta. The doctor left it up to me and I said not to tell her. We have to let her have this last time . . . this last little time . . . without that hanging over her. We have to go on as if everything were exactly the same."

She nodded to show that she understood. After a moment she spoke past the ache in her throat. "About school. I'll . . . I'll tell her that I decided to wait until next year. Or that I'm afraid I'd be lonesome without the gang. I've been sort of . . . sort of seesawing back and forth, anyway."

It seemed impossible that life could go on exactly as before. The small private world peopled by the three of them was as snug and warm and happy as though no shadow had touched them.

They watched television and argued good-naturedly about the programs. Minta's friends came and went and there was the usual round of parties and dances and games. Her father continued to bowl two evenings a week and her mother became involved in various preholiday pursuits.

"I really must get at my Christmas shopping," she mentioned the day she was wrapping trick-or-treat candy for Halloween. Minta shook her head and sighed gustily.

It was amazing that Minta could laugh and say, "Oh, you . . ." the way she did year after year.

It was a knife turning in her heart when her mother straightened up from the gay cellophane-wrapped candies and brushed a stray wisp of taffy-colored hair back from one flushed cheek.

"Don't laugh," she said, pretending to be stern. "You know you're just exactly like me."

She wanted to put her arm around her mother and hug her, hard. She wanted to say, "I hope I am like you. I want to be." But instead she got up and stretched and wrinkled her nose. "Perish forbid," she said, "that I should be such a scatterbrain." She was rewarded by the flash of a dimple in her mother's cheek.

It seemed to Minta, as week followed week, that the day at the beach had been something out of a nightmare: Something that she could push away from her and forget about. Sometimes she looked at her father, laughing, teasing them, or howling about the month-end bills and she thought, "It didn't happen . . . it isn't true."

And in the dark hours of the night Minta had known it wasn't a nightmare. It was true. It was true.

One windy November day she hurried home from school and found her mother in the yard raking leaves. Minta stopped and leaned on the gate. She saw with a new awareness that there were dark circles under her mother's eyes and that the flags of color in her cheeks were too bright. But she managed a chuckle.

"I wish you could see yourself, Mom. I'll get my camera and take a picture of you." She ran into the house and got her camera and they took a whole roll of pictures.

"Good," her mother said complacently. "Now we can show them to your father the next time he accuses me of being a Sally-Sit-by-the-Fire." Her mother was tired that night. She lay on the davenport and made out her Christmas card list while Minta and her father watched the wrestling matches. It was like a thousand other such evenings but in some unaccountable way it was different.

"Because it's the last time," Minta told herself. "The last time we'll ever rake the leaves and make a bonfire in the alley. The last time I'll snap a picture of her with her arms around the Kelly kids. The last time . . . the last time. . . . "

That night she wakened in the chilly darkness of her room and began to cry, softly, her head buried in the curve of her arm. At first it helped, loosening the tight bands about her heart, washing away the fear and the loneliness, but when she tried to stop she found that she couldn't. Great wracking sobs shook her until she could no longer smother them against her pillow. And then the light was on and her mother was there bending over her, her face concerned, her voice soothing.

"Darling, what is it? Wake up, baby, you're having a bad dream."

"No . . . no, it isn't a dream," Minta choked. "It's true . . . it's true."

The thin hand kept smoothing back her tumbled hair and her mother went on talking in the tone she had always used to comfort a much smaller Minta. "Want me to leave the light on in case your spook comes back?"

Minta shook her head, blinking against the tears that crowded against her eyelids, even managing a wobbly smile. She never cried again.

Not even when the ambulance came a week later to take her mother to the hospital. Not even when she was standing beside her mother's high white hospital bed, holding her hand tightly, Not even at the funeral. . . .

One night he came to the door of her room where she was studying. "I wonder if you'd like to go through those clothes before your Aunt Grace takes them to the church bazaar," he began haltingly.

And then when she looked up at him, not understanding, he went on gently, "Your mother's clothes. We thought someone might as well get some good out of them."

She stood up and closed the book and went past him without another word, but she closed the door behind her when she went into her mother's room. Her hands felt slightly unsteady as she pulled open the closet door. A faint perfume clung to most of her garments. Minta started folding the things with haste, stuffing them into boxes, cramming the lids on and then starting on another box.

At the very back of the closet were the two pieces of matched luggage that had been her mother's last birthday gift from her father. They were heavy when she tried to move them—too heavy.

She brought them out into the room and put them side by side on her mother's bed. Her breath caught in her throat when she opened them.

Dozens and dozens of boxes, all tied with bright red ribbon, the gift tags written out in her mother's careful script. Gaily colored Christmas stickers, sprigs of holly. To Minta from Mother and Dad . . . to Grace from Mary . . . to John from Mary . . . to the Kelly Gremlins from Aunt Mary . . . to Uncle Art from the Hawley family. . . .

"So you knew," Minta whispered the words. "You knew all the time."

She looked down in surprise as a hot tear dropped on her hand and she dashed it away almost impatiently. She picked up another package and read the tag. To Minta from Mother . . . with love.
```
