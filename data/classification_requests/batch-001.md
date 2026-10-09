# Classification request: batch 1 of 53 (40 records, IC-0401 to IC-0440)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-001-reply.json`.

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

## IC-0401: Life on Death Row: A Monologue

- Title: Life on Death Row: A Monologue
- Author (byline): Walter A. Davis
- Work: Counter Punch Newsletter Eds: Alexander Cockburn and Jeffrey St. Clair
- Publisher: CounterPunch
- Publication date as stated: November 29, 2005
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2388
- Already set (do not supply): none

### Source block (context only)

```text
Author: Walter Davis
Magazine: Counter Punch Newsletter
Eds: Alexander Cockburn and Jeffrey St. Clair
ISBN: B00006KAF2
Publisher: CounterPunch
Date (Month/Year): November 29, 2005
Order Hardcopies on line at http://www.counterpunch.org/davis11292005.html
```

### Introduction (context only: never use it for content warnings)

```text
There are over 600 inmates currently on death row in San Quentin. He’s been on death row in San Quentin for the past 15 years. His appeal of the death sentence is now at the Federal level. For that reason I have been advised by attorneys not to use his name and to take other steps to disguise his identity. Within the terms of that restriction what follows is a factually complete account.. Life on Death Row by Walter A. Davis
```

### Performance text (classify this)

```text
I fell off the edge of the world. That's what it felt like, the moment the bars clanged shut. My life over. Nothing now but waiting, without hope, for something that'll come someday, it doesn't matter when, because time is nothing now but this wall in front of me. I see myself under water looking up at Mother's face all twisted, her hands like claws, forcing me down, my eyes pleading, dying- then breaking the surface gasping in a shriek toward air.

There'd be this pop, right in the pit of the stomach and I'd feel all the air go out of me. As if life is breath like Homer says, and mine had gone leaving nothing but the struggle to hide the panic building inside me Because I could see it now -- flashing in front of me-a blanket pressed down over my face, my mother's hands holding me down under the water, my eyes looking up at her, pleading, the whole thing whirling around inside me--until there was nothing but rage, blind rage, to explode out of myself-- as if bringing my fist down upon the world was the only way I could breathe.

That's what they tried to give me. A way to breathe. Mother, Father, Regina-I loved them so, the way they came forth to plead for my life at the trial. They let themselves be known-utterly. All the family secrets. Like they were offering their lives to me so that I could try to piece it all together here. Only like the way it is in a dream-a dream in which you walk through yourself becoming the thing you behold. Mother weeping all day, every day tied up down in that basement, the rats scurrying across her toes; my father waiting in that shack, trembling, the long processional of men like it was all one day, a summer afternoon, just a little boy but holding his jaw out stiff the way it always got just before he'd start hitting my mother; Regina holding her jaw the same way, refusing to cry, telling the Court what father forced her to do-- what my mother's father did to her-- what I did to that poor little girl, fucking her that way then forcing her head down into the bathtub.

I could see us now, the family, like branches of a poison tree, a tree that could only grow downward, clawing its way into the earth, latching onto whatever it could take hold of to root itself deeper, water itself with our tears, reach out and claw like Mother's fingernails, twine round itself like tendrils choking off anything that could grow upward and break free, dragging everything back down into the one knot at the center. Only now when I woke sobbing it was my mother I heard crying, not me; my father that time I heard him in the kitchen when he thought no one was home, Sis huddling in the corner of the closet when we hid from Momma, whimpering like that but saying "no, no don't you touch me" her face like granite locked in its impenetrable stare.

And I felt it all rush back on me. Everything rushes away but the rage, rage raging in me, in my fists hitting at her, my hands tightening around her throat forcing her down--, so I get to see it in her face for a change-- fear, panic, terror-- the full weight of my body over her pressing down on her wind-pipe, cursing and crying (he emits a terrifying sound) -- only it was too late: there was nothing but her eyes staring at me with that look that came into them right before the end, staring at me like that forever.

I'd put it all together, sitting alone in my cell, and what I knew drove me back out into the hall again, only not like before but now like a dead man walking, shuffling my feet along the floor, the same ten steps one way and then back, eyes fixed on the floor, the arms hanging limp, the shoulders stooped like an old man's and what must have been on my face the look of a corpse because everyone stayed clear of me. Everyone except Reverend John. He was from one of Colson's prison ministries and would walk freely among us every day, taking men aside, one by one, whispering to them, opening the book and pointing at it with his insistent finger.

And I guess he knew right away I was one of the ones who'd read the parts in red, over and over, long into the night when the only light left was from the moon, and feel the tidal pull of a compassion so inconceivable that soon I couldn't wait to tell him "yes yes I accept Jesus Christ as my Lord and Savior," weeping and saying it over and over while he held me in the thick embrace of his bear-like arms. And I tried, tried to hold onto Jesus later when I felt him slipping away, no matter how hard I tried to feel his love, tried to hold onto the Reverend too even after I saw that it was all about power for him. He wasn't interested in the questions I was asking now, only in what came later when the beckoning of his sad eyes told me it was time to confess again and sob how thankful I was to him and Jesus for forgiving me, again and again. No, goddammit! I couldn't forgive myself and didn't want to. I'd done the most terrible thing a human being can do. 'Forgive yourself," he said 'even as your heavenly Father forgives you.' Only that doesn't bring back a life. The dead are the only ones who have a right to forgive-and they can't. Their eyes say something else. That death is a horror in which there's no comfort or forgiveness. Only nothingness, pitiless and final--and as your life slips from you the last thing you see is that nothingness, triumphing over every hope and illusion. Besides, the afterlife and the great banquet of forgiveness. It undoes everything. As if all the evil and suffering we do doesn't matter finally. Life's a shell game to amuse something vindictive in us that wants to call itself God.

It got to where all I could do was lay in my cell, balled up in a fetal position, trembling and crying like a baby. So I did it-the one thing you can never do here. I dropped a kite. On myself. I'm sorry, a kite, that's what we call it when you slip a note to a guard ratting on somebody. "Save me. He's everywhere now, his dreadlocks like snakes with eyes at the end-eyes like fangs."

They took me to the white room. That's when it really got bad. When I was safe. After they strapped me down on a bed like I asked them to-and I was free, free to rave. I didn't need him anymore. It was all back inside me, but torn loose from all the ways I'd tried to contain it. I could feel it, something ravenous, scooping out chunks of my heart, devouring them: "No" I screamed when they told me they were going to medicate me. "No you can't, not without my permission. I know my rights, even here." Somehow in my raving I knew that this is what had to happen. What I had to go into wherever it took me. The only thing I had to hold onto-my madness. The only thing left that was mine. Mine--even when they put me down in the hole.

That's where it happened, what I'd always sought, deservedEverything drifted away-even the images. I was left with only the one thing. Emotion. That's what we are. All we are. Something happens and an emotion is formed. Later something triggers it and it returns-in all its fury. Then it's like what Spinoza said-an emotion can only be replaced by another emotion and the strongest always wins. Hate, fear, love, rage-each the pure product of pure and brutal experiences-warring with each other. Emotion-the thing that tears us apart. And so we try to blow it out into the world. Inflict it on someone else to get some relief. But it always returns to its source. Life nothing but the process of being blown with restless violence from one emotion to another. But always in the end rage, only rage

Let it come, I said, feeling the sweat of it pouring over me rocking myself back and forth in it making my body a cradle for it. For rage so pure it'd consume me, rage raging in me until it burst into remorse-- remorse becoming love-- a terrible love, ripping me apartThen again nothing but the panic of feeling myself-what you'd call my soul-dying within. Then reborn, reborn in rage. I felt it claw at me: not I it, I said like that play of Beckett's, only I knew it was I and I felt myself vanish into it until there was nothing but one emotion after another searing my flesh. Time went away and space. The room went away. I was utterly alone, with nothing left between me and what I was.

Most of the time it felt like I'd never come back. That rage would claim me so complete and entire that I'd run and dash my brains out against the padded wall. Or that I'd dissolve in a love that was nothing but pity, pity for a loss so deep that one morning they'd find me gone in a weeping that could never end. Or that the panic would seize me"yes that's how it'll end crying out against myself for the Meds, begging for them, pleading with them please please I'll do anything just take the pain away." Or fear, the worst fear, that I'd become my deed-but without remorse-my deed and nothing but a monster raving kill kill kill, living only for horror, wanting it, more of it, unable to get enough of it, hurt and hatred and revenge.

I felt each emotion blow down white hot all over me. Burning itself up in me. Renewing itself through me. And in the brief interim, when the whole thing would pause and turn on itself like a ferris wheel about to run backwards-Dread-- the cold sweat of dread all over me, knowing this might never end yet knowing I had to sustain it because otherwise I was truly lost. Do it to yourself, I cried. Be it, rage, hate, terror, despair. Assault yourself with yourself. Make each emotion a spike driven through the brain straight into the heart. That's the only way, I cried, and in that cry I became a young girl in Nepal sold into prostitution, raped and beaten by two men; a woman in New York bleeding to death in an alley 10 feet from home, the neighbors gawking through closed windows; then little girls, dozens of them, sexually abused children crying out of me for it to "stop." Stop!" And that's when it began, what had to happen, though I had no way to know it then, all the emotions bleeding into one another, out of their clash refining themselves into something else that I no longer felt would crush or swallow me but out of which something new might come to be.

I lay there like a corpse feeling the whole process moving across me the way a rat down here sometimes crawls across your chest in the night, slow and tentative, almost delicate, like it was your companion and didn't want to wake you. Don't move, I said. Hold yourself still in the still of this. Wait. Wait. And then I felt it, my whole life, coming back to me, all the images, every event, but like there was finally room in me for them. Like I'd created a womb in myself and something was being born there. All I'd felt, done, suffered, all the violence of my passage through life, was being transmuted into something else. Like I was giving birth to myself. Out of myself. Feeling in myself something I'd never felt before. I wept then, but in a way I never had before. There was no desperation in it. The tears were warm and slow-streaming down my cheeks-and full of what I can only call gladness. But grief too, real grief. A grief for her deeper than any I'd felt before when the panic to deny who I was got all mixed up in it. No, this was real grief. Grief for someone I never knew-someone who never had a chance like mine to know herself. For a life that never was. Unforgivable-to take that from someone. And so for the first time I could really say it to her: " I'm sorry, sorry for your lossfor taking from you the chance to discover who you were." (breaks down and weeps.)

The journey. It's all that matters and the only way to make it is to live purely with nothing between you and who you are. For some, it takes all their time here just to get started-but that's enough. A life begun. I was lucky, I always had remorse. I didn't have to waste years trying to crack the hard nut of denial.

I can't say I'm thankful for my life. That would be obscene. And yet I'm one of the fortunate men. I found a way, in this place, to do what few people can do. Rehabilitated? I don't know what that means. After a time any man in here isn't the same man he was when he got here. Because there are only two choices. To finish it -- become the thing one was trying to be on the outside. Murder. Rape. Terror. Revenge. Or to somehow find a way to live life to the full every day, knowing it isn't life, can't ever be life. Life is what I took. That's what I try to live too, knowing that every breath I draw comes after she, the woman I killed, Rosalie, Rosalie Romans, drew her last
```

---

## IC-0402: Liquid Healing

- Title: Liquid Healing
- Author (byline): Mark Donnelly
- Work: Best Men’s Stage Monologues of 1998
- Publisher: Smith and Kraus
- Publication date as stated: Sept 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: TIM
- Teaser before the introduction: No
- Spoken words (computed): 1370
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mark Donnelly
Book: Best Men’s Stage Monologues of 1998
ISBN: 978-1575251851
Publisher: Smith and Kraus
Date (Month/Year): Sept 1999
```

### Introduction (context only: never use it for content warnings)

```text
“Seeing is believing” the old song says. But what if you’re robbed of sight? Are you then robbed of belief? Belief in life, belief in people, belief in yourself. Can you struggle on? Or are you blind to more than the visual images the world has to offer? “Liquid Healing” by Mark Donnelly
```

### Performance text (classify this)

```text
(Tim McCoy, a blind man in his mid 20s, walks on stage. He turns off the light switch on the wall and the lights dim so he is somewhat in shadow. He struggles to find a chair, hits it as he walks, curses, then gropes and finds the chair arm.)

TIM: There. Now we're all in the dark. (Pause.) How'd I get like this? A fight, man. gang kids. Fourth of July . . . Bang . . . I was going to pick up Molly, then drive us out to Jones Beach to watch the fireworks with some friends. (Pause.) Fireworks, all right. I'm coming out of the liquor store and I see these punks breaking into my car. One of these creeps got a coat hanger and he's shimmying it through the window to get the door button up . . . I had an older car . . . '83 Cutlass. And this jerk's just about got it open. Like a game in a penny arcade where you use the little crane to extract the prize.

There's three of these guys, but I don't care. I snap. I drop my shopping bag I'm so pissed, and the six-pack of Michelob and the soda all smash on the ground. I go after the guy with the hanger and grab his arm. And one of his pals jumps me. Then Coat Hanger pokes me in the left eye. I'm screaming and I've got blood allover me. The punks just left me there lying on the pavement. The store owner comes out . . . Asian man. I gotta be grateful to him. He ripped his sport shirt off and rapped it around my face. Got me down to the emergency room with his son driving like a madman. (Pause.)

The doctor couldn't save my eye. And here's the kicker. I end up eventually going blind in the right eye, too, because I'm diabetic. My father died of it when I was twelve. Then the diabetes started working on me at about twenty. Six months or so after the fight, that right eye was acting up . . . my vision got cloudier and cloudier. . . I was in my third year at St. John's. (Pause.) By the end of the spring semester I could barely see the print in my textbooks. I was using a magnifying glass, then even that wasn't helping. I walked out of my Business Management final. Couldn't read the charts and graphs. (Pause.) That summer the doctor told me my diabetes made the deterioration in the other eye irreversible. I dropped out when that eye went and I was completely blind. Lights out for old Tim McCoy . . . only I'm still here walking around . . . just barely . . . Yeah, that trip to the fridge for more beers is a killer . . . (Pause.)

You know what I miss? I miss going into the kitchen in the dark late at night and letting the light from the fridge brighten up the room just a little . . .

(As if talking to the inside of the refrigerator) No more Mr. Bright Guy now, you little light. You still working? Still amazing millions of other drunks with your late night bath of artificial sunshine? (Pause. Speaks directly to audience again.) Didn't know I was so sensitive and literary did you? That's what an education can do for you. (Pause.) Oh, I tried to go back to college again to finish up. Had a counselor for the handicapped there who tried to help me with Braille. But that's tough. I think it's almost easier if you're blind as a kid. He also told me there's some kind of stuff you can do on the computer that's voice activated. Said there's all sorts of support groups for blind people . . . I know all that now. I went to one of those groups. The people even kid around, call themselves Blinks. But I'm not laughing. I felt uncomfortable around them. (Pause.)

I'm getting disability checks from the Government. Even had money to pay for readers when I was still taking courses. Molly did some of it, but she'd never take the money. So I also got other readers through her . . . Molly was an elementary education major and some of her classmates were up for that kind of work . . . They didn't know what they were in for with me though. I gave 'em hell, I just was so frustrated and pissed off. I gave up altogether and never finished my degree. (Pause.) I'm not doing much now . . . unless you call smoking and drinking doing something. (Pause.) My hobby? I watch TV . . . I mean, listen to TV . . . and get loaded. (Lights a cigarette and smokes it.)

They tell me all the smoking and drinking is bad for me. My mother is worried I'll fall asleep with a lit cigarette and burn the house down. (Pause.) I don't blame her. She works hard all day and comes home to find me in my sweats. Some days I don't even bother to take a shower. (Pause.) Where am I? Living in the house I grew up in and blind as a bat. Talk about feeling like the baby brother! (Pause.) My sister Susan . . . she's a nurse. She comes by, but she's busy with her little boy. And my brother Bobby, he brings me out to his place on Long Island some weekends. It's better in the summer because he has a small motorboat he takes out into the Sound. He likes to get out there, says it clears his head from all the crap he sees as a New York City cop. But do you know how much you miss when you're out there on the water and you're blind? Sure, I can smell the salt, and put my hand in the water, and feel the sun . . . but I can't see any of it . . . I gotta rely on my memories of all that stuff . . . and they fade, man . . . really fade. (Pause.)

Bobby's got a girlfriend named Marie. And they're gettin' married next year. Where's that put me? Mr. Third Wheel? (Pause.) Not this guy. I don't want it. (Pause.) I mentioned Molly already. I met her at St. John's before all this happened to me. Beautiful girl . . . Great girl . . . too great . . . stuck by me through all of this . . . Said it didn't matter if I was blind. Said she loved me, man and still wanted to marry me . . . we'd talked about that seriously before the accident . . . accident . . . He should have his own eyes gauged out, man. (Pause.)

Sometimes I wake up at night from dreams where I've thrown acid in his face . . . then destroyed him by ripping his arms and legs off. . . Molly said I've got so much rage that's still inside me . . . that's what all the nutso drinking's about. . . I yell and scream at everybody. . . my family, friends. . . and Molly. She tried to calm me. . . tried to get me to talk to a therapist. I went a couple of times, but it didn't change anything. Didn't reduce the rage. Why wouldn't I be in a rage! What am I gonna do, rot in this house the rest of my life? (Pause.)

I'd be at Molly's apartment and I'd be touching her, so soft and smooth . . . and she would hold me close . . . but I couldn't see her. . . I couldn't see her face anymore, and look in her eyes. (Sadder.) Never can again. (Pause.) I pushed her. . . I pushed her . . . I made things so ugly for her. . . I think it was intentional now. I couldn't bear her leaving me someday. I couldn't believe anybody could love me so much, put up with so much to stay with a blind guy. So I pushed her out the door . . . How else? What else? It's hard man. . . I love her, but I don't want to be pitied. I don't want to be a charity case for her. (Pause.)

What kind of job am I gonna get? A vocational counselor told me that with my intelligence and skills there were plenty of opportunities for me. Opportunities?! You know anybody who wants a blind office manager? Blind stock broker? And skills? What skills! (Pause.) I never did know what the hell I wanted. Used to dream of flying planes when I was a kid. My grandfather flew in World War II. But when he died, my dream sort of died, too. . . And did you ever hear of a blind pilot? (Pause.)

Molly's teaching at an elementary school out in Glen Cove. She's good with kids, she's got patience. . . I'm probably the biggest kid she had to deal with. . . drove me to campus after I got hurt. . . Didn't matter if her classes weren't lined up with mine. She worked around it. . . she went all out for me. . . wouldn't give up on me. . . but I made it too rough for her. . . And now she's gone.
```

---

## IC-0403: The Littlest Hitler

- Title: The Littlest Hitler
- Author (byline): Ryan Boudinot
- Work: The Best American Non-Required Reading 2003
- Publisher: Houghton Mifflin, Co.
- Publication date as stated: Oct 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2254
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ryan Boudinot
Book: The Best American Non-Required Reading 2003
ISBN: 0618246967
Publisher: Houghton Mifflin, Co.
Date (Month/Year): Oct 2003
```

### Introduction (context only: never use it for content warnings)

```text
A child’s understanding and comprehension of the atrocity known as The Holocaust is understandably limited. It is only with maturity, that the social concepts surrounding this time in history become clear. When one is 8 or 9, intellectual capacity often falls into the categories of good versus bad, black versus white, right versus wrong. In The Littlest Hitler by Ryan Boudinot
```

### Performance text (classify this)

```text
[I remember] the time I went as Hitler for Halloween. I had gotten the idea after watching World War II week on PBS. My dad helped me make the costume. I wore tan polyester pants and one of his khaki shirts, with sleeves so long they dragged on the floor unless I rolled them up. With some paints left over from when we made the pinewood derby car for YMCA Indian Guides, the painted a black swastika in a white circle on a red bandanna and tied it around my left arm. Using the Dippity-Do he put in his hair every morning, he gave my own hair that plastered, parted style that had made Hitler look as if he was always sweating. We clipped the sides off a fifty-cent mustache and adhered it to my upper lip with liquid latex. I tucked my pants into the black rubber boots I had to wear whenever I played outside and stood in front of the mirror. My dad laughed and said, “I guarantee it, Davy. You’re going to be the scariest kid in the fourth grade.”

we find a young boy just coming to terms with a concept which was at first beyond his grasp . . . . Hitler (scary Halloween costume or something more?)

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

## IC-0404: A Long Way Gone: Memoirs of a Boy Soldier

- Title: A Long Way Gone: Memoirs of a Boy Soldier
- Author (byline): Ishmael Beah
- Work: Not specified
- Publisher: Sarah Crichton Books
- Publication date as stated: Feb 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: FRIEND, ISHMAEL, ALHAJI, KANEI, GASEMU, REBEL 1, REBEL 2, SOLDIER, LIEUT.
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

ISHMAEL: Finally, we were approaching the village where seeing our families was actually a possibility. I couldn’t stop smiling. We came across a man cutting down ripe bananas. The sight of his face awakened my memory. He was much skinnier than when I had last seen him. His name was Gasemu – Ngor Gasemu.

(Ngor is a title like “Mr.”)

GASEMU: (Peeps at them from behind a banana leaf. Wipes the sweat off his forehead and walks toward them. Smiles.)

You boys want to help me carry some bananas to the village?

(asks in the manner that adults usually ask young people when they won’t take no for an answer.) Come on. (Motions for them to follow him into the banana farm. Continues waving his hand.) (speaks to Ishmael)

Are you still a troublesome boy?

ISHMAEL: There is no time to be troublesome these days.

GASEMU: Your parents and brothers will be happy to see you. They have been talking about you every day and praying for your safety. Your mother cries every day. Your older brother left to look for you, but he returned about a week ago. His face was sad when he returned. I think he blames himself for losing you.

ISHMAEL: I wanted to drop the bananas and run as fast as I could to the village. I felt as if my heart would explode if I waited any longer.

GASEMU: The village is just over the hill.

ISHMAEL: I heard gunshots. And dogs barking. And people screaming and crying. We dropped the bananas and began running. A thick smoke started rising from the village. Nails were popping off tin roofs, and they flew landing on nearby thatched roofs, increasing the wrath of the fire. We heard screams and loud banging a few houses away. There were people locked in it. We banged the door open, but it was too late. Only two people came out, a woman and a young child. They were on fire, and ran up and down the village, slamming themselves against everything in their way. The woman fell and stopped moving. The child gave a loud screech and sat next to a tree. He stopped moving. It all happened so fast that we just stood there, rooted to the ground. The child’s yelp was still echoing in my head, as if it had taken on a life of its own inside me.

On other paths of the village were the half-burnt remains of those who had fought fiercely to free themselves, only to die outside. I hesitantly tried to make out the faces of burnt bodies, but it was impossible to tell who they had been. Besides, there were too many of them.

GASEMU: Your family stayed in that house. (Pointing toward one of the charred houses.)

ISHMAEL: The fire had consumed all the door and window frames.

(His entire body goes into shock. Only his eyes move, slowly opening and closing. He falls to the ground, holding his face. He gets up and runs toward the house. Without any fear, he goes inside and looks around the smoke-filled rooms. He screams at the top of his lungs and begins to cry as loudly as he can, punching and kicking with all his might into the weak walls that continue to burn.)

My hands and feet punched and kicked the burning walls, but I couldn’t feel a thing. Gasemu and the rest of the other boys began pulling me away from the house.

Soon we heard loud voices of people approaching the village. We ran into the nearby coffee farm and lay in the dirt watching. A group of more than ten rebels were laughing and giving each other high fives. Two looked slightly older than me – maybe 13 or 14. They had blood on their clothes, and one of them carried the head of a man, which he held by the hair. Blood dripped from where the neck had once been. The other rebel carried a gallon of gasoline and a big box of matches.

REBEL 1: We burned three villages today. (laughing)

REBEL 2: Yes, three is impressive, in just a few hours in the afternoon. (pauses) I especially enjoyed burning this village. We caught everyone here. No one escaped. That is how good it was. Commander will be pleased when he gets here. (nods)

REBEL 1: Some people escaped in the other two villages. (pauses, rubs his forehead as if pondering why that had happened.) They probably saw the smoke from this village and knew something was happening. We should change our strategy. Next time we must attack all the villages at the same time. ******************

ISHMAEL: I had heard from adults that this was a revolutionary war, a liberation of the people from corrupt government. But what kind of liberation movement shoots (and burns) innocent civilians, children? ********************

ISHMAEL: We escaped the village and ran to the forest. We must have been walking for days, I do not really remember, when suddenly two men put us at gunpoint and motioned, with their guns, for us to come closer. They were the soldiers – not the rebels. There were four men lying on the ground, their uniforms soaked with blood. I turned away, and my eyes caught the smashed head of another man. I felt nauseated. Everything began to spin around me. One of the soldiers was looking at me (smiling). He took a drink from his water bottle and threw the remaining water at my face.

SOLDIER: You will get used to it; everybody does eventually.

ISHMAEL: The soldier led us to Yele, a village that was occupied by the military. In the beginning, it seemed we had finally found safety there. The village was full of lively chattering and laughter. All that darkened the mood of the village was the sight of orphaned children. There were over thirty boys between the ages of seven and sixteen. I was one of them.

One morning the atmosphere in the village suddenly became tense. It wasn’t clear what had caused the change, but something was about to happen. I was awake when the soldiers left in the middle of the night. The following morning, wounded soldiers were brought back only to die by lamplit surgery. Prisoners were lined up and shot in the head. These things went on for many days, and each time the soldiers went to the front lines, few returned. The lieutenant asked his men to gather everyone at the square.

LIEUT.: In the forest there are men waiting to destroy all of our lives. We have fought them as best as we can, but there are too many of them. They are all around the village. (Makes a circle in the air with his hands.) They won’t give up until they capture this village. They want our food and ammunition. (Pauses, and slowly continues.) Some of you are here because they have killed your parents or families; others because this is a safe place to be. Well, it is not that safe anymore. That is why we need strong men and boys to help us fight. If you do not want to fight or help, that is fine. But you will not have rations and will not stay in this village. This is your time to revenge the deaths of your families and to make sure more children do not lose theirs.

ISHMAEL: We had no choice. Leaving the village was as good as being dead. The women and older people in the village stood on their verandahs and watched as we were led away by the adult soldiers into the clearing toward the forest. A baby cried uncontrollably in his mother’s arms, as if he knew what lay ahead of us.

I have never been so afraid to go anywhere in my life as I was that day. Tears had begun to form in my eyes, but I struggled to hide them and gripped my gun for comfort. The lieutenant had passed the word down through a whisper: “Fire on my command.” As we watched, a group of men dressed in civilian clothes emerged. Some were boys, as young as we were. The lieutenant gave the order to fire. I lay there unable to shoot. The forest had begun to spin. (clutches the base of a tree with one hand.) I couldn’t think, but I could hear the sounds of the guns far away in the distance and the cries of people dying in pain. A splash of blood hit my face. (spits it out, wipes his face) I saw the soldier it had come from. Blood poured out of the bullet holes in him like water rushing through newly opened tributaries. He cried for his mother in the most painfully piercing voice I had ever heard.

My face, my hands, my shirt and gun were covered with blood. I raised my gun and pulled the trigger, and I killed a man. Suddenly, as if someone was shooting them inside my brain, all the massacres I had seen since the day I was touched by war began flashing in my head. I angrily pointed my gun into the swamp and killed more people. I shot everything that moved. We went out two more times that week, and I had no problem shooting my gun. The idea of death didn’t cross my mind at all, and killing had become as easy as drinking water. My mind had not only snapped during the first killing, it had also stopped making remorseful records.

We practiced killing prisoners. We were supposed to slice their throats on the corporal’s command. The person whose prisoner died quickest would win the contest. I didn’t feel a thing for my prisoner, didn’t think that much about what I was doing. I just waited for the corporal’s order. The prisoner was simply another rebel who was responsible for the death of my family, as I had come to truly believe. The corporal gave the signal with a pistol shot and I grabbed the man’s head and slit his throat in one fluid motion. I was the winner.

CLOSING At age 16, Ishmael Beah was removed from the fighting by UNICEF. He was brought to New York City, where he graduated from high school and earned a college degree. Today, he serves as a member of various human rights groups, having spoken before the United Nations, the Council on Foreign Relations, and the Center for Emerging Threats and Opportunities. Through the help of a rehabilitation center, Ishmael has learned how to forgive himself, to regain his humanity, and, finally, to heal.
```

---

## IC-0405: Looking a Lot Like Christmas

- Title: Looking a Lot Like Christmas
- Author (byline): Jason Sheets
- Work: Turning Points
- Publisher: Tichenor Publishing
- Publication date as stated: 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 988
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jason Sheets
Book: Turning Points
Publisher: Tichenor Publishing
ISBN: 978-0618640157
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
Ever notice how the characters on Christmas specials have no family? I mean Rudolph: a loner. Charlie Brown has a whole party without his parents. Those elves may have a social network going, but rarely do you see them with their family. I'm sure they all have families. It's implied. I guess that's why I watch them each Christmas. People assume I have a family. It's implied.

So how'd I end up this way? One word: homosexuality. Or, as my sister put it, three words: "that queer thing". For 20 years, I was the straightest man in Wichita. Sure, there were hints. When my friends had sleepover parties and we'd sneak a look at Playboy, everyone else was mesmerized. They'd say "Whoa!", so I'd say "Whoa!" But I never really understood what all the" whoaing" was about. When Die Hard was big, all the other guys liked it when Bruce Willis kicked some ass. I liked it when the ass-kicking required ripping off his shirt. So, the thoughts were there, but that's all they were. Thoughts.

In college I hid it. I was too busy. It was always something else. A paper. A party. An intramural basketball game. Anything but the topic of romance. Anything but a blind date. Anything but addressing my weird fascination to my fraternity brother. Anything but that.

But then I met someone. Not just anyone. The someone that you always dream about. In my first year in the office, Tom asked me out for drinks. I didn't think it was a date. Maybe it wasn't at first. But as the seasons changed from autumn to winter to spring, I knew. And when Tom said he loved me, I had no problem loving back. OK, some problem - I was new at this. Still, I was whisked into a fantasy world. A place I could call my own.

One problem: family. Actually two sub-sets of the same problem:

1.) I always wanted a family. OK - call me short-sighted, but just as I knew I

was gay, I also pictured myself with the standard wife, kids, dog, picket

fence - you know the routine. Tom and I weren't exactly family Channel

material. 2.) My family would be stunned. They would call a therapist, a priest, and my old

high school prom date simultaneously and plot a conversion. It would be hell.

So, when I got up the strength to tell my family, 28 months later, I decided to do it with style. Pizzazz. Christmas dinner. Extended family and all. I was really wasn't going for the shock factor - I just would be damned if I'd have to give the spiel twice. It opened as planned: Mom fixes ham and potatoes, dad says grace, sisters complain of the fat content, grandpa states that it's good to have the family together on the holidays, and off we go on another Christmas at the Engelhans. I was ready.

"OK everyone. I wanted to tell you something. I know you all have said I should date more. I just wanted to tell you that I've met someone. Actually we've been dating for almost 3 years. I've never felt so right, so alive. His name is Tom -"

Stop. Freeze frame. You know how you learn in science class that at zero degrees Kelvin, all motion ceases? Zero degrees Kelvin - right there at the dinner table. Dad gives me a look like he should have played more football with me when I was a kid. Mom stares into space. My sisters look like I just stole their boyfriend.

Then things happen in slow motion. My aunt drops her fork into her soup. Dad says, "This is no time for sick jokes." Mom says, "Yes, it's Christmas." Grandma says, "Is Tom short for Thomasina?" Grandpa says, "I'm not listening to this" and leaves.

Dinner continues. Silent. Voiceless. And yet speaking volumes.

That night I meet up with dad in the living room. He's always been the spokesperson for the family. He certainly will be for this, too.

"Do you love him?"

"Yes."

"Does he love you?"

"Yes."

"Do you see a future with him?"

"I certainly hope so."

"Son, you've pulled the rug out from under me. What do you want me to say?

I'm happy? I'm not. You've chosen a difficult lifestyle."

"It's not-"

"I know. I know. It's not a choice. Maybe it's not. Who's to say? But now you've forced a choice on me. My Bible says it's wrong. I can choose to accept you and reject my Bible, or I can accept the Bible and reject you. Do you understand what decision you're forcing on this family?"

I knew this was going to be difficult. I knew that. But I never dreamed of the horror of that night. Growing up, my father taught me one thing above all others: never turn your back to the Lord. And that was what he chose to do that night. Not turning his back on the Lord meant the family turning its back on me. I never went back to that house. I drove past, but never went back.

There was only one person who hadn't turned his back on me, but he did so three weeks later. He said he didn't envision a future for us. He said so in a note. My life reduced to a post-it. And then there was none.

And that's how I'm here. Uniquely myself; uniquely alone. Sure, we've got support meetings. Meetings to make us feel like we're not alone. But we are alone, often reduced to two emotions: numbness and rage.

Numbness, rage, Christmas specials, and egg nog. The life of a gay man in America. No family to marry into; no way to re-create the old one. I have made the right decision. To be true to myself But still - it's Christmas. I light a Christmas candle. It represents hope.
```

---

## IC-0406: Lucky Man

- Title: Lucky Man
- Author (byline): Michael J. Fox
- Work: Not specified
- Publisher: Hyperion Press
- Publication date as stated: April 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MICHAEL, NURSE, DR. JOYCE
- Teaser before the introduction: Yes
- Spoken words (computed): 1380
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

MICHAEL: I was feeling a little disoriented. I’d only been shooting the movie in Florida for a week or so, and the bed in the hotel suite still came as a bit of a shock each morning.

That’s when I noticed my pinkie. It was twitching, trembling, auto-animated. How long this had been going on I wasn’t exactly sure, but I was surprised to discover that I couldn’t stop it. Weird-maybe I slept on it funny.

The trembling had been going on for a few minutes with no sign of quitting and what had begun as curiosity was now blossoming into a full-fledged worry.

I found myself wandering the halls of New York City’s Mount Sinai Hospital. White jacketed nursed and doctors scurried back and forth through the corridor. Any one of them would have recognized the name of the physician I was looking for, but that was the problem: they were also just as likely to recognize me. I didn’t want any gossip about why Michael J. Fox was seeing one of the preeminent neurologists in North America.

The nurse at the front desk showed me into the examining room, and as I was shedding my coat and baseball cap, she noticed the shaking in my left hand.

NURSE: It’s ok . . . You don’t have to be nervous.

MICHAEL: Confused for a second, I suddenly realized she was talking about the tremor. (to nurse) Oh.That’s…that’s why I’m here. In a neurologist’s office, I mean. After a second of mutual embarrassment, she left, closing the door behind her. Minutes later, it opened again, and walked in the legendary neurologist himself.

DR. JOYCE: Essential tremor, maybe. Possibly something else, but you’re here, so let’s have a look.”

MICHAEL: “Finally,” I thought. “We’re going to get to the bottom of this. This guy knows what he’s talking about.”

The most paranoid fantasy I could think of would not have prepared me for the two words the neurologist bludgeoned me with that day: Parkinson’s disease.

Recollecting my exact response to this is difficult. My symptoms showed up in my late twenties! How could I possibly have this old person’s disease? The air sucked from my lungs, my left arm was shaking clear up to my shoulder. Why was he doing this to me? What was I going to tell Tracy? I looked up at the doctor and stared; he was so composed. Tough for him, I bet, dropping this on a guy my age. He was really very good…I hated his guts!

As I stepped out of the door of his office building and onto the rain-soaked streets of mid town Manhattan, it was as if I were entering a whole new world, but the only profound change was not around me, but within me. I had to get home though. Hailing a cab and the ride itself would be slow going. That was ok-I needed every second to sort out what just happened and how I was going to explain this to Tracy, my mother, family, and the rest of my friends. It wouldn’t be enough time.

I let myself into the apartment. I could smell dinner cooking in the kitchen and hear my son Sam giggling. I couldn’t go in there and face him at the moment. Tracy entered from the kitchen and I met her in the foyer and silently motioned her to the bedroom. As she followed me, I could feel her curiosity escalating toward panic.

In the bedroom is where I told Tracy. Tracy, stunned and frightened, cried. At the same time she was so present, so loving…In sickness and in health I remember her whispering, her arms around me. Typically my first instinct to Tracy: It’ll be ok; to myself: what will be ok?! I have Parkinson’s disease!

As it was, each week’s show presented a brand new set of creative and physical challenges. Could I count on my body to respond in performance the same way it had in rehearsal? By now I could see that the strain I put myself through by trying to be funny was exhausting. Whatever I appeared to be doing onstage, I was, in fact, doing something else: hiding symptoms with a repertoire of little tricks and distracting maneuvers. Many days I had to concentrate more on my physical relationship to the scene unfolding around me than to emotional, comedic, or dramatic content. All the while I was doing the math-how long since the last pill? How long until it wears off? And at what point in the show will I have to take another one? “Please…let it be during a scene I’m not in.” If the warning came when I was in the middle of a four-to-five minute scene, there wasn’t a thing I could do to stave off the return of my symptoms. If a studio audience were to detect a tremoring of my arm, a slowing of my speech, or a rigidity of my movements, it would undoubtedly betray the fact that something was wrong and that something would be decidedly unfunny.

This became one of my greatest fears; just making an audience laugh remained one of my greatest pleasures.

So I did everything I could to make sure the audience didn’t know I was sick. I have always thrived on my relationship to the audience, and feared taking any risk that would distract or detract from it. Timing a joke depends on the audience being with me, and if their attention is lost even for a second while they are watching my arm or a hitch in my gait, then I’ve lost them. If an audience didn’t know what I was dealing with, they wouldn’t know what to look for, so I still had a shot at making them laugh. But if they already knew that I was battling an incurable disease, would they still go along for the ride, or would they be watching for symptoms and feeling sorry? Can sick people be funny?

I was beginning to realize that this was what was keeping me from telling people that I had Parkinson’s disease. Over the past seven years I had experienced so many highs and lows, and had finally set about facing my fears. The distance my disease had put between me and the people I care about had been narrowed, but what about the audience? Until I felt ready to tell them my story, my life would never be fully integrated and as happy. I can vividly remember all those nights when the studio audience had to wait for my symptoms to subside. I’d be back stage, lying on the dressing room rug, twisting and rolling around. When that approach failed, I’d spruce up the walls with fist sized holes, the graffiti of my frustration! How much longer could this go on?

I entered into Joyce’s office on Friday morning. I had a show a show to do that night.

(To Doctor) I’ve had this feeling lately One I haven’t had in years. That old feeling like I’m waiting for the other shoe to drop. (to audience) Joyce was quiet

DR. JOYCE: Michael, you have Parkinson’s disease-the other shoe dropped a long time ago.

MICHAEL: Almost as if I had walked into a hug, I immediately felt enveloped in a wave of emotion, not of sadness, but of relief and pride. Joyce was right. The other shoe had already dropped, and I survived. There was nothing left to fear. It was time, I was ready.

Coping with the relentless assault and the accumulating damage is not easy. Nobody would ever choose to have this visited upon them. Still, this unexpected crisis forced a fundamental life decision: adopt a siege mentality -- or embark upon a journey. Whatever it was - courage? acceptance?

wisdom? -- that finally allowed me to go down the second road (after spending a few disastrous years on the first) was unquestionably a gift - and absent this neurophysiological catastrophe, I would never have opened it, or been so profoundly enriched. That's why I consider myself a lucky man.
```

---

## IC-0407: A Man Named Dave

- Title: A Man Named Dave
- Author (byline): Dave Pelzer
- Work: Not specified
- Publisher: Plume
- Publication date as stated: Sept 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DAVID, STEVE
- Teaser before the introduction: Yes
- Spoken words (computed): 1857
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
Dave Pelzer was the victim of unbelievable child abuse. His mother denied him food and clothing, locked him in the basement, and told her son she could kill him any time she wanted to – and nearly did. And Dave’s father? He never intervened.

By the time Dave was 12, the state had removed him from his home and placed him in foster care. But even years after he was rescued, his life remained a continual struggle. In this scene, Dave tries to reconnect with his dying father. A Man Named Dave by Dave Pelzer
```

### Performance text (classify this)

```text
DAVID: My father, Stephen Pelzer, he’s here? I mean, he’s okay and he’s in this hospital on this floor. Right? (blurting it out)

STEVE: (begins to reply, but raises a hand to his mouth as if to first collect his thoughts.) Man, we’ve been waiting on you. Yeah, kid, your father’s here, and . . . yeah, he’s on this floor. But chill for a sec. There’s a few things you need to know.

DAVID: (rolling his eyes as if to say, Yeah, yeah, come on, out with it.) So . . . (nagging) what’s the deal? What happened? He fell down, broke an arm? What is it? When does he check out? (Spins to the right, marches into the room where his father is. Takes a few seconds for his eyes to adjust. Mind is spinning. Slings his arm around his dad’s shoulder to help him walk.) Dad, are you all right? Are you okay?” (His Father’s eyes are blank. Eyes roll to whatever catches his attention for a split second before drifting off somewhere else. His body is trembling. He fights to stand up straight.) Dad (whispering gently) . . . it’s David. (no reaction) Dad (firmer tone) can you hear me? (raspy exhale from Father) Dad? Hey, Dad! Can you . . . do you hear me? It’s me, David. Say something, anything. Dad? (looking for the slightest response. Hoping he can communicate with his eyes -- No response.)

STEVE: (Firm, but gentle squeeze on David’s right shoulder). We need to talk.

DAVID: What’s wrong with him? (demanding, anxious) What type of medication do you have him on? How come he doesn’t recognize me? Is it the drugs? How long will it be until he gets better and gains some weight? When do you expect him to be released?

STEVE: Hey, man (raising his hand), give it a rest. Didn’t your mother tell you? You don’t know, do you?

DAVID: Know what? If I knew, I wouldn’t be bugging you! (Sarcastically) Just tell me, what in the heck is going on? Please! (begging) I gotta know.

STEVE: (leads him down the corridor, Steve searches for a more private setting. At the end of the hallway, he stops to offer David a chair. David refuses the chair and stands.) It was about four months ago when your father was admitted –

DAVID: Four months! (yelling) Admitted? Admitted for what? Why didn’t anybody call me? Why now?

STEVE: Please (interjecting) give me a chance. Your father. . . he wanted to keep things discreet. A lot of patients are like that. Anyway, it was only after we ran all the tests that our diagnosis was confirmed. David, your father has cancer. I’m afraid it’s terminal. He’s in the advanced stages. I’m sorry. (reaching out for David’s hands) There is nothing we can do.

DAVID: Hang on! (stepping away from his gesture) What do you mean, terminal? I don’t get it. . .

STEVE: David, (deliberate, slow voice, gripping David by the shoulders) your father . . . he’s not going to make it.

DAVID: You mean. . . you’re saying he’s going to die? My dad is going to die? No way! (shakes head in complete denial.) Can’t you give him a shot of something . . . or I thought there’s some kind of chemo treatment. If it’s money you need . . . just don’t let him die. Not now. Please! (begging, as if Steve alone decided the fate of his father)

STEVE: David, listen, chill for a sec. I don’t know, no one knows exactly how long your father has, but, (emphasizing this in a strong tone) the thing I do know for certain is this: your father is not going to make it. And there is nothing, nothing, that you, I or anyone else can do about it. (pausing) David, (taking David’s hand) I am sorry. I truly am.

DAVID: (No energy. Thoughts are disjointed. Helpless.) Four months? (Incoherently) You’re telling me my dad’s been here that long? How long has he been . . . like he is now? Why can’t he talk? Is he doped up? I mean, he acts like he doesn’t even recognize me . . . I don’t, I just don’t understand. (stammering.)

STEVE: Well (sliding a chair next to David’s) your father checked in a few months ago. Since then his condition has rapidly deteriorated. The growth was primarily centered on the side of his neck, but has since spread to his throat. He is on medication, and under the circumstances, I’m sure you can understand why. That is the reason he lacks discernment. If we take him off the ‘meds,’ his understanding might improve, but the pain would be unbearable.

DAVID: So. . . he’ll never be able to say anything again? Ever. . . ? (voice trailing off)

STEVE: That is correct. Not any longer. (nodding his head)

DAVID: So . . . what can I do? Why doesn’t he look at me? Does he know, I mean, is he capable of knowing I’m even here?

STEVE: (sighs) For the most part, it’s fifty-fifty at best. He seems more coherent in the morning but, for the most part, no more than a few minutes at a time. He’s at the stage where he drifts off quite a bit. (Beat) I know it’s a lot to deal with. (shaking his head) But first things first. Spend time with your father. That’s priority one. I can walk you through the paperwork and all the other things you need to do when the time comes. For now, just spend time with your dad.

DAVID: But . . . I, ah, I don’t know what to say. I mean, he doesn’t even know that I’m with him.

STEVE: Your father doesn’t show it, but he’s scared. He knows he’s not going to make it. Anything you can do would mean the world to him. He’s all alone in there. (gently scolding) You have to do this! Just . . . just reminisce about all those good times you spent together. Keep him ‘up.’ He’ll know.

DAVID: (cautiously walking back to his father’s room; mockingly to himself) Yeah, all those good times. All my visits with Father probably amounted to less than ten, maybe twenty hours together. (Enters room . . . Tears swell in his eyes. Speaks to Father) I, ah. . . I tried to write. I mean, I wrote. . . but I wasn’t sure of your address. (Shakes his head, stammering on) I’m sorry. I truly am. I didn’t know. I would have come sooner. I just didn’t know.

(Turns away to compose himself. Doesn’t want to lose it in front of his father. A few moments of silence, and then he remembers Steve’s advice about keeping Father uplifted. Out of nowhere, a memory of Father and David springs to his mind, from when he was a preschooler.)

You may not remember, but when I was four, maybe five, all of us went to the Russian River . . . Early one evening, after dinner, you stepped out for a walk, and I tagged along behind you . . I snuck out and walked behind you, tracing your steps. I had those little Forest Ranger boots, and I tried to keep up while being as quiet as I could. I think I made it five, maybe ten feet away from the cabin, when you heard me. You spun around so fast I thought you were going to bite my head off, but you . . . (stops for a second to smile at Father’s face) you simply extended your giant hand and scooped my fingers into yours. Then without a word, you let me walk with you.

I have to say, as a kid that was pretty cool. At the time, between Ron, Stan, and me, to be able to hog a few minutes alone with you, well, back then that was all I talked about after our walk. It was that summer when I knew that’s where I wanted to live. The trees, the river, the smell, those precious moments with you, that’s when I knew. Back then, with you, I was safe. Back then you were my superhero; you were my Superman. I know it sounds kinda dumb. (scoffing) But that was the only time you held my hand. When you wanted to be with me. (stops for a moment to close his eyes.)

When I was at the house, I remember all those times you’d come home from the fire station for just a few minutes to check in on me. Mother didn’t know it, but I made sure I timed your arrival when I was washing the dishes so I could actually see you. Sometimes I got too far behind with my chores and . . . well, you know Mother . . . I paid the price when you were gone. I knew she’d never allow you to go down to the basement, so I’d wash the dishes over and over until I heard you open the front door. (pauses to stare directly into Father’s eyes.)

You saved me. Even though it was only for a few seconds alone in the kitchen, it made all the difference. Sometimes if you brushed against me, I’d breathe in your Old Spice cologne. You were my invisible force field. I’m just sorry you, the boys – everyone – had to deal with so much stuff. I somehow thought I’d be able to make it up to you – to everyone.

You see, Dad, I knew. I always knew you came back to the house for me. And now, no matter what happens, I’m here for you. No matter what anybody says, I’ll protect your honor. (Beat) As a kid, I was always proud of you being a fireman. You looked so cool in your dark blue uniform. It was then that I knew I wanted to be a fireman. Dad, Dad, do you. . . do . . . do you still have your badge? Your fireman’s badge?

(to audience) It’s the only thing he has that showed what he did. After everything, it’s all he has. Look, his eyes! The closet? You want me to look in the closet?

(searching his father’s face for a reaction. Jumps from the bed and flings open the door. Eyes dart to the bottom of the closet. Opens the drawers. He finds nothing. Shakes his head. Picks up his father’s coat. Pats it down. Yanks out a small leather casing. (Immediately father’s breathing eases. He shuts his eyes as if in concentration. Lips quiver. Sounds trying to escape his mouth. Eyes lock onto David’s)

I don’t know! I don’t know what you’re trying to . . .(suddenly feels the slightest sensation on his right hand. Glances down and sees father’s bony fingers wrapped around his hand clutching the badge. He seals his son’s hand around the black leather case.) As God is my witness, I will protect and keep your badge. I will carry it as a sign of honor. (Father’s grip eases. He falls asleep) (David kisses his hand. Lays his hand on his chest.)

STEVE: He’ll be able to rest now. You’ve made him very happy. He told me months ago, when he checked in, that he wanted you to have it. Today was a good day for your father. A very good day.

DAVID: How do you – I mean, I don’t know if he can understand me. If he could just talk

STEVE: He is talking. And you’re learning to listen. It’s hard, but as long as he knows you’re there, beside him, that’s all that matters.

TRANSITION: - These words are not in the text of the book: I spent a few days at the hospital, talking to my dad and listening to him too. On the fourth day, when I arrived at the hospital, I met Steve at the entrance to Father’s room.

STEVE: (extending his arm to block David from entering) We need to talk. (forced smile) David, you need to understand . . . sometimes they can’t . . . they won’t go. . . until they know the ones they love will be fine. You . . . ah, get what I’m saying, David? He’s in pain. You have to tell him you’ll be fine. You have to let him go.

You understand, right, David? He won’t pass until you do this. Ease his suffering. It’s the right thing for him. It’s the proper thing to do. He won’t pass until . . .”

DAVID: (flees to the far end of the hall, where he finds a wooden bench. Clasps his hand together, he prays.) I’ve never really asked you for much. And you know what I’ve been through. So, if you could grant me this . . . if there’s no way that he can get better . . . then take him. Ease his pain and take my dad. Amen. (wipes away his tears, clears his mind, and makes his way to Father’s room.)

I, ah, got. . . .some great news. (lying) The doctor says everything’s gonna be fine. . . and that. . . they can have you up and outta here real soon. (confidently peering into his father’s face) I didn’t tell you this before, but I got a home on the Russian River. (beaming) It’s got knotty pine walls and ceilings. A stone fireplace, your own room. It’s always warm and sunny. It’s really nice. It’s got everything. It’s on the river, and when the sun goes down, the water’s as smooth as glass. At night you can smell the redwood trees . . . it’s a piece of heaven, Dad. Heaven. You and I can live there. . . and go fishing. . . sit at the beach., or do anything we want. And in the summer . . . we can go to San Fran and catch a game at Candlestick – just like you always said we’d do. We can be like a real father and son. Just the two of us.

We made it, Dad! We really made it! Everything’s gonna be fine. We can be together. . . and live at peace. We got a home, a real home. No more fighting, no more troubles, no one’s gonna kick us out. We got it made! It’s gonna be fine. You just relax and. . . I’ll take care of you. . . .I’ll take care of everything.

I’ve always been proud of you. You’ve always been my hero. And as your son, one day I will, I will make you proud. I always have and always will love you, Father.

Now you relax. . . and I’ll meet you at the river.” (Holds him behind his neck as delicately as possible. Kisses him on the forehead. Eases his head back onto the pillow.)
```

---

## IC-0408: Memoirs of an Imaginary Friend

- Title: Memoirs of an Imaginary Friend
- Author (byline): Matthew Dicks
- Work: Not specified
- Publisher: St. Martin’s Press
- Publication date as stated: August 2012
- Event as filed: Dramatic Interpretation
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
When I was little, I had a very good friend named ______. He was fearless when I was scared, rebellious when I was obedient and athletic when I was clumsy. He was also entirely imaginary. I can’t remember how I met _______ and I don’t remember the last time I saw him. But I do remember that he inspired me to go on adventures I would not have had the confidence to undertake without him.

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

BUDO: Everything about this situation is bad. (Pg 25) Max is trapped in a public bathroom, a place that already frightens him. His pants are wrapped around his ankles and he probably hasn’t finished (whispers) pooping. But it’s the way Max answered Tommy that scares me the most. There was more than panic in his voice. There was fear. Like when people in the movies see the monster for the first time. He might already be close to getting stuck. (Pg 64) When Max gets stuck, there’s nothing anyone can do for him. He sits with his knees pulled really tight into his chest and rocks back and forth and makes a whining sound. His eyes are open, but they can’t see anything. There’s nothing anyone can do for him.

MAX: (Pg 25) (screeching like a little girl) Occupied by Max Delaney! Occupied by Max Delaney!

BUDO: (Pg 64) (breathes a heavy sigh of relief) There’s no screaming when he is stuck! (Pg 25- 26) But I don’t know what to do now. Tommy Swinden is about to crawl under the door and enter the tiny bathroom stall where Max is trapped. If he’s not crying yet, he soon will be. Things stay with Max forever. He never forgets. And even the tiniest things can permanently change him.

TOMMY: Last chance, moron. Open up or I’m coming in!

BUDO: Fight, Max! Fight! Don’t let him in there! (to audience) It’s not a great idea. It’s not smart or even original. It’s just the only thing left to do. I am as stuck as Max has ever been. (anticipatory pause then Tommy screams in disgust)(Budo is in disbelief) The door flies open and Max is standing there, pants nearly pulled up but not buttoned or zipped, his legs straddling Tommy’s head. (to Max) Run! (they both run, Max buttoning and zipping his pants without stopping. Finally, they find a hiding place near the nurse’s office)(out of breath)(Pg 27) What happened to Tommy? What did you do?

MAX: I pooped on his head.

BUDO: (impressed) You pooped with someone else in the bathroom? (to audience) The fact that he pooped on Tommy Swinden’s head is unbelievable, but the fact that he managed to poop in the presence of another human person is even more amazing.

MAX: (matter of factly) Just a little one. I was almost finished when he came in. I pooped this morning, so it was a bonus poop. *****Scene Change*****

BUDO: (Pg 303-304) [So that brings us to today] Max has stopped talking to me. It’s not that he is angry with me. He just doesn’t know that I am around anymore. And when I’m gone, I’ll just be a story that his mom tells him some day. How he once had an imaginary friend named Budo. (Pg 253) The thing I like best about Max is that he is brave. It’s not one thing -- (Pg 305) [Not] bonus poops and Tommy Swinden. (Pg 253) It’s everything. Max is not like any other person in the whole world. Kids make fun of him because he is different. His mom tries to change him, and his dad tries to treat him like he is someone else. Even his teacher, Mrs. Gosk, treats him differently. No one treats him like a regular boy, but everyone wants him to be regular instead of himself. With all that, Max still gets out of bed every morning and goes to school and the park and the bus stop and even the kitchen table. You have to be the bravest person in the world to go out every day, being yourself when no one likes who you are. (Pg 308-309) When I am gone, Mrs. Gosk will have to protect Max. She will have to help him with the bonus poops and Tomy Swinden and all the other little things that Max cannot do because he lives to much of his life on the inside. That big, beautiful inside that one imagined me. . . And she will. I want to be angry at Max for forgetting about me, but I am not. (pause) (Pg 140) It’s strange to be an imaginary friend. You can’t suffocate and you can’t get sick, and you can’t fall and break your head, and you can’t catch pneumonia. The only thing that can kill you is a person not believing in you. That happens more than all the suffocating and bumps and pneumonia combined. (pause) (Pg 309) Death is not scary for me anymore. It is just sad. I just want to watch the little boy who I love so much grow up. I want to know the rest of Max’s story. I hold the image of Max’s face in my mind for as long as I can. (whispers) I love you, Max.
```

---

## IC-0409: How to Ride a Motorcycle (Badly)

- Title: How to Ride a Motorcycle (Badly)
- Author (byline): Clint Snyder
- Work: How to Ride a Motorcycle (Badly)
- Publisher: Mushroom Cloud Press
- Publication date as stated: Not specified
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1694
- Already set (do not supply): none

### Source block (context only)

```text
(none)
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
A Dramatic Interpretation (Male)

By Clint Snyder

STEVE My father’s death wasn’t spectacular. It wasn’t the type of death that you would see in a

movie, but in my head I still like to convince myself that he died in some grand Shakespearean way, like poison or a swordfight to the death. Prior to this he would recite a ten minute monologue explaining everything I've ever wanted to hear and tying up all

his loose ends. In reality, he died in a hospital bed and his last words to me were, "Change the channel backs to ESPN you pansy." Then he coughed a few times and died,

but I convinced myself for at least a few minutes that he was still alive, so I told a joke

after he died. I have the unfortunate habit of making awful jokes when I get

uncomfortable. (Pause.) "Hey two cannibals are eating a clown and one asks the other

"Does this taste funny to you?"" (Uncomfortable laugh.) I find the jokes on Popsicle sticks and I save them all in a dresser drawer. Dad called me that a few times, "Popsicle stick". I'm not completely sure what he meant. That I'm skinny, I guess. The only thing that could have possibly made the situation more awkward, and did, was finding out that

an answer to a question I never wanted answered. In case you were wondering, “Yes,

people do relieve themselves when they die, but that's my life, one awkward moment

after the next. The only time that I can remember that was even more awkward was

shortly after, on my newly purchased motorcycle, trying not to crash into every car Harlem avenue on the way to my father's funeral. (Suggested intro place/ end of teaser)

I started growing up like any other kid, playing little league for a while, karate, hockey. My dad put me in about every sport known to man. I'd be in it for a few weeks, until I had worn down each coach enough to beg my father to let me quit. "We'll find something that you're good at." He would tell me. I already had- I was clearly the best artist in my class. At six years old my macaroni portraits would make Van Gogh cry himself to sleep after realizing just how bad he was. I had given one to my dad, a T-rex biting the neck off a cheetah on the moon, quite spectacular if I say so myself. I found it in the trash the next morning. What he meant was, "We'll find something that you're good at that Chuck Norris might also be good at." Walker Texas Ranger was his favorite show. Technically, Chuck Norris is an actor, most actors did theatre, and I don't think theatre qualifies under Dad's list of "Things Men Should do", but I chose not to remind him of this fact.

By the time I got older, I think he had finally given up. I had worn him down the same way I wore down those coaches and my tight, but fashionable bell bottom jeans. He would talk a lot about his friend's sons and all the amazing things they were doing, like killing deer and buying cars. "Did you know that Doug's son got two turkeys on their last weekend trip." "No, that's… great." I lied a lot to my dad. As far as I was concerned Doug's son was a turkey. I guess he sort of "mentally adopted" them, as a way of making up for me being such a failure. I tried to revive his faith every now and then by watching a football game with him or a John Wayne movie. He saw right through me though, whenever someone made a touchdown and he would start shouting at the t.v. like he was trying to somehow channel his aggression to the players through the t.v. I would make a comment like, "Yeah, he was… fast." Then it would get uncomfortable and I would start making Popsicle jokes. "Two cookies were sitting in an oven together. One cookie says, "is it just me or is it getting warm? The other one says, "Ahhh, A talking cookie." (Laughs uncomfortably.)

A few years after I made that joke we found out he had prostate cancer. He forgot to flush one time and my mom found some blood in his pee. She wasn't really a forceful woman, but she had a quiet way of getting what she wanted and she wanted him to go to the doctor.

My dad compared women to furniture one time. I've always thought of it as just another sexist rant, but after the doctors told my dad I remember my mom's eyes were wet and tense with pain. I focused on her eyes hard to stop myself from allowing myself to feel the gravity of what was happening, that must have been what my dad had done too because his face hardly moved at all until he shouted, "Maybe you should have learned something at med school instead of wasting your parents money!" He stormed out and we followed my mother raining tears the whole way home.

He tried to convince everyone, including himself, that he was fine. To him, prostate cancer was like the ultimate insult. It emasculated him… he must have felt… like me. So he tried to pretend it didn't exist. It worked for a while, but he eventually got so weak he couldn't ignore it anymore. He got taken to the hospital. He laid in that hospital bed for two months complaining to everyone who would listen about anything he could think of. Then he died. No meaningful last words. No dignity. No manhood. No son... not the way he wanted anyway.

I went home and did the only sensible thing a man like me could do. I locked myself in the bathroom and cried. What was worse, I watched myself cry. Standing there, weak, pale, he must have looked just like me before he died. I think that was the biggest slap in the face for him. He used to say, "Always look like you're ready to fight someone, it shows confidence." I stood looking at myself in the mirror imagined my peach fuzz turning into thick black curls, my limp body becomes bulging muscles and I'm wearing the kind of hat Clint Eastwood would kill someone in. ( Stand straighter, with new strength.) Then it came to me. I'd buy a motorcycle and drive it to his funeral. It wasn't exactly a horse, but I think dad would have approved. It was the kind of testosterone packed choice that might have made him change his mind about me. The man I bought it from asked me if I had a motorcycle license. I didn't even know I needed one. "Of course I have one." That's not something the old me would have done, but I think the danger of driving without a license was just the kind of move and that was what I was going for. I drove it all the way to the funeral, if you could call it driving. I almost got into about six accidents and I’m pretty sure someone had to have reported me, but it was important. It was important to him. I cried, but I was wearing sunglasses, so no one would see, which made it more difficult to drive. Everyone stared at me when I got off the motorcycle, but probably because it took me ten minutes to park. After that everything happened so fast. The priest said a few words, mom cried a lot and everyone threw some cheap gas station flowers onto the cheap coffin while the cheap undertaker looked upset about his cheap job. They lowered him into the ground and I went home on my seven hundred pound mechanical beast that I was trying way too hard to tame. I can’t believe I had to try so hard to do something every sloppy redneck half-way across the country could do blind-folded.

Days later I still had his death fresh in my head. I couldn't get him out. I just wanted to be done. I thought it must have been because the stupid mechanical beast in the garage was there reminding me of him, so I “drove”, and I use that term loosely, to a field with nobody around in circles until the gas was all gone. I brought a small container of gas with me, but instead of pouring it in the tank I dumped it all over the bike and set it on fire. I wanted this gone, not just the bike, but that part of my life. I wanted him out of my head. It was like he was my cancer that ate its way into my system and spread throughout my body until every single choice, every move I make was dictated by him, even after he died. Why couldn't this just die with him?

I thought that would kill it. His voice ringing in my head, but it was still there and I came to a realization. It was ringing louder and louder until the flames grew higher and higher. They reached they reached what was left of the small gas container and pop. The explosion forced me backwards and flashed a short bright light and licked my face with hot flames. I lay there in the tall grass a moment completely unharmed, but changed. I came to a realization. My mind became clear as I stared at the clear sky. There was more to my dad than the disappointment. I had spent so long focusing on how I could not be what he wanted me to be. There were plenty of times where he just let that melt away and loved me for who I was. It was time for me to forgive my father and time for me to forgive myself. It took my father’s death for me to realize that he did love me, but in truth I had to learn to love myself before I could let anyone love me and that for everyone’s sake I should never try to ride a motorcycle again. (Smiles.)
```

---

## IC-0410: NO LONGER THE FIRST

- Title: NO LONGER THE FIRST
- Author (byline): Josh Danz
- Work: NO LONGER THE FIRST
- Publisher: Mushroom Cloud Press
- Publication date as stated: 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1176
- Already set (do not supply): none

### Source block (context only)

```text
(none)
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
To this day I can remember my very first girlfriend. Probably because she was the only girlfriend I’ve ever had. People have asked me how… over the course of 20 years have I only had one girlfriend? And to be honest, I don’t know. I’m shy, I guess. Talking to girls isn’t something that comes naturally to me. I either say something really stupid, or I can’t even work up enough nerve to say anything at all. And yeah, it’s embarrassing- to say that the only girlfriend I’ve ever had was back in the 7th grade.

So I’m sitting in my Anatomy for Bio Majors class, when this girl walks in. And you can tell from the moment you saw her that she was just one of those girls who you knew you couldn’t have. The girl with that perfect smile and personality. Well, after about 20 seconds of praying to God that she sat next to me, take a guess where she ended up. So here I am trying to think of something to say to her when she beats me to the punch and says “Hi I’m Alison.” So trying to play it cool, I say (Cracked voice) “Hey… Hey, I’m Ben.” And as I can feel the blood rushing out of my face she laughs… and says “Nice to meet you.”

Over the next couple of weeks, we started to get pretty friendly. She’d come to class and sit down next to me and we would talk for a while until class started. I’d generally try to say something funny, which usually came out wrong… and like always, she would just laugh. You know one day I made some sort of joke that her and I should go out and the next thing I know she’s actually giving me her number. So after practicing what I was gonna say around 65 times, I finally worked up enough nerve to ask her out. And she said yes.

The first few dates were awesome. After we went out we would go back to my apartment and talk until we fell asleep or well, usually until I fell asleep. Anyways, one night, we got back to my place after going to see some little chick flick and Alison said she wanted to thank me for putting up with her crying throughout the movie… Remember that Anatomy class? Well, let’s just say I got a head start on that homework!

It was hard to believe that three months had already passed since we started dating. It’s been a great three months, but over the past few days Alison had seemed kind of distant. As we walked to class that Monday, she stopped me. She said “Ben, I need to talk to you. (Pause) I’m pregnant Ben.”

“What? You’re telling me that after all- Well, I hope you and whoever the hell the father is are, really happy!” And she laughed and said “Me too. I’m sorry to spring this on you, but I need to know that you’re here for us Ben… if not” “No! I am. I love you Alison. And I’m gonna love that baby too.”

How is this possible? How am I supposed to take care of a baby? Shit, I’m still a baby. I used to laugh at the people who were in my situation. Used to wonder how someone could be so stupid. Well I’m not laughing anymore.

So I found out today that it’s a girl (Laugh then stop)- Kind of disappointed. Girls are great if you love little pink bows and barbies- I hate that shit. Alison’s at that point now where she is sick, like, every morning. It’s funny cuz, after she threw up the other day she asked me if I still thought she was beautiful. And I said “Yes, you are still beautiful… right in here.” (Pointing to my heart). That wasn’t the answer she wanted to hear. And then she proceeded to throw up on my feet… Again.

We went in the other day for a little check up and the doctor told us that everything is going great, but right now, Alison’s a wreck. Over the past week or so I’ve stayed up with her almost all night just playing with her hair until she fell asleep on me. Look, I know she’s pregnant and sick and everything… but it’s getting really tough for me too. It’s just getting really tough…

So, I wake up the other night only to find that my leg is covered in water breakage. So I start to freak out and hurry to clean myself off, and then we rush off to the hospital. At this point I’m starting to get really nervous… because I’m about to be a father. But at the same time I’m really excited… because I’m about to be a father. But, pretty nervous (Pee running down leg)… oh boy, yeah that’s water breakage running down my leg right now.

After what seemed like forever, Alison finally went in to labor… and for that matter, I felt like I did too. She kept yelling at me and telling me that this whole thing was my fault. She started to scream “You bastard, you bastard, you did this to me,” then the nurse epiduraled her ass!

When the doctor finally came in he started to mess around… down there and he asked me if I wanted to see what was going on. So I- “Oh my God, that is disgusting!” And then she started to scream again. So the doctor asked me to leave.

I’m having a hard time sitting still. Every few seconds I keep looking up, waiting for the good news… When the doctor finally came out, I ran up to him and say “Hey! How’s my baby? How’s my baby girl?” (Pause) He just stood there for a minute. “Ben, during the child birth, there were some complications. Things that you just can’t foresee. I’m sorry Ben. Your baby-”

Is gone! Right? Yeah look, I need to go see Alison.” “Ben, your baby is fine. But during child birth, Alison”

“No… you shut-up! Just shut up and stop lying to me. Just shut up and tell me you’re lying.” (Long pause)

It’s called Eclampsia. I don’t really know what it is… I didn’t even ask. I just know that she had it. (Sad smile) We didn’t even get the chance to talk about names. Doctors told me I get to see her tomorrow, my little girl. I’m looking forward to that.

As I walked to the nursery the next day, I thought about all the things I wanted to tell my little girl. Things I wanted to tell her about myself, and her mother. But when I saw her- (Short of breath). She’s beautiful. She’s has her mother’s eyes, and her nose and her chin. She looks just like her. She’s got my ears… which, is kind of unfortunate (slight laugh). But she’s beautiful.

(Whispering) “Hey little girl… I’m your dad. Your mom, she’s not here now, but, she loves you. And so do I. So right now, It’s just gonna be you and me now little girl.” (Pause and smile)
```

---

## IC-0411: Red God (Красный Бог)

- Title: Red God (Красный Бог)
- Author (byline): Kevin Bushek and Bronne Bruzgo
- Work: Red God (Красный Бог)
- Publisher: Mushroom Cloud Press
- Publication date as stated: 2005
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1433
- Already set (do not supply): none

### Source block (context only)

```text
(none)
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
Красный Бог

(Lights up on a single man onstage.)

CLICK! CLICK! BOOM! … That one had a ring on his finger. Oh well, one more widow in the world. … What? Is not my fault that he wandered away from his platoon… and right into my sights, but that is another matter.

You look at me as though I am mad! Don’t worry, don’t worry, rest assured. I am.

Allow me to introduce mysef, I am sniper for the Glorious Red Army, Nikolai Traschev, and I am a machine. Now, I was not always the embodiment of the reaper you see before you, when I was sent into battle with nothing but my mosin-nagant and 10 shells, I was harmless. I can still remember my first time though…

(Flashback, the environment is a snow-covered forest. Nikolai shivers as he stands, rifle aimed at a German across a deep ravine.)

I crouched in the bushes, my makeshift snow camouflage doing nothing to shield me from the Russian Winter. My sights were locked on a German manning an MG-42 across the chasm. He hadn’t seen me, but I just couldn’t do it. This was a man whose people had invaded our country, burned our cities and killed helpless people, but he was still a man, just like me. With my mind off my target for a mere moment, I happened to shift my weight and snap a branch. In an instant I knew I was about to die, for my rifle shot one bullet at a time, and the German shot 30 rounds every second. I quickly raised my scope to see him spring to life across the chasm CLICK It was him or me CLICK And it certainly wasn’t going to be me BOOM!

(Freeze position, he sounds very distressed, on the verge of panic and tears)

I had done it
I had taken life
I had played God
And it felt GREAT.

I held in my hands the power to destroy. From that second on, I never thought twice or hesitated to pull that trigger. Day after day, shot after shot, one by one the Germans fell at my hand. Slowly, the man in my crosshairs became less and less of a man, and more of a nameless target. Just as slowly, the man on this end of the scope became less of a man, and more of a monster. I became almost excited when I saw the german uniform colors walking between the trees. Soon, I couldn’t go a day WITHOUT taking life, it was a drug. The click, click, boom of the rifle could lull me to sleep, this great God of death.

My squadron and I moved like ghosts through the snow, we always joked that we were so good that we didn’t even leave footprint in the snow. We would all huddle around the fire when the night would fall and make fun of the Germans and their ridiculous-looking leader. My spotter, Innokentiy (ee-nah-KYEN-teey), and I would constantly ridicule those silly Germans by pretending to be Hitler, like this:

(Nikolai rearranges his rifle strap across his chest and strikes an overly exaggerated stiff german stance. He then brings up his pinky to his lip to imitate the famous Hitler moustache. During his entire German tirade, Nikolai attempts to remain as stiff as possible, with all movements being rigid and robotic.)

Oh, look at me, I am such a fancy German! Somebody stole my moustache and my hair is made of shiny plastic! My name is Adolf Hitler, ya?! Oooh, ya! I can stomp around in my big German boots and not move my knees at all. Deutschland, Deutschland. Allow me to try and be a swastika! Tell me, what is it doing?

(Attempt to contort into swastika using bent arms and legs.)

It is running, ya!

(Nikolai fixes his rifle strap about his shoulder and breaks away from the German impersonation)

Ah, those were great times. Stalin, now THAT is a leader, he can move his knees when he walks AND, most importantly, he’s god a full moustache. Oh yes. Fear the moustache. Regardless or facial hair, Innokentiy and I were like brothers, the ghost brothers. I would shoot, he would confirm, we were bound never to leave each other’s side, we were a team. My squad consisted of about 6 or so of these teams. One day, I wanted to move to the Eastern Pass because I thought that the Germans would foresee our sniper ambush in the gulley below, but no, those stupid Krauts would undoubtedly walk right into our sights. Days passed, and not a single German went through that valley, I found out later that those “stupid Germans” anticipated us brilliant Russians and moved through the Eastern Pass, exterminating several Russian squadrons before they were stopped?

I could have stopped them. Myself. Well, Innokentiy and I… no. Just me. I could have done it without him even. But this squadron is untrusting of me. They see my power. They’re jealous. They KNOW that I am the most skilled behind the trigger and they are trying to hold me back. They don’t want the higher command to realize that I am the only thing keeping these monstrous foreign invaders from progressing into the great motherland. If I were my own commander, I bet that I could exterminate the entire German race, a genocide. No, a Germancide at my hands. I proposed it to the squadron commander, Yuri, the next day.

Nikolai: Yuri, Nikolai Traschev, I respectfully request for Innokentiy and myself to be
released from this squadron.
Yuri: Why?
Nikolai: So that we may further pursue the German threat uninhibited by others.
Yuri: Those “others” keep you alive out there.
Nikolai: Those others keep me restrained. Chained up like a dog!
Yuri: You do not know your place, soldier!
Nikolai: With all due respect, sir, my place is out there killing Germans, NOT sitting
around here!
Yuri: Your request is denied, Nikolai, return to the squadron!

I could see that requesting was getting me nowhere, time to start demanding. No longer would I be held back.

(Nikolai brings his hand up to his neck and mimics a slitting of the throat as he says the following line.)

Night fell, and I cut myself free from my bonds. I left only Innokentiy and myself alive.

Nikolai: Innokentiy wake up! A German assassin killed our comrades! GET UP! We need to go find him! Inno: (Waking up, still groggy.) What? The comrades, where is the assassin? Nikolai: He ran when he saw me with my rifle, come on, we’ve got to collect what we can from the dead and move, there’s a killer out there. Quickly, move!

It was true, there was a killer out there, Innokentiy just didn’t know he was right in front of him. I only did what was necessary, and now we were free. We left and got far away from there, and it was like I had just killed for the first time. We were free, no orders, just lots of bullets and lots of Germans out there, just waiting to be killed.

We traversed for days, living off of rations that our comrades so readily gave up to us in death, and then… Nikolai: Look at all these footprints, there must be a whole regiment moving through here. Come, let’s hurry and we can intercept them. Inno: I don’t know Nikolai. This looks like at least 50 men went through here. Even if we did intercept them, your first shot would give our position away to 49 other Germans with automatic weapons. Nikolai: Come now, where is your spirit?

Inno: Right next to my common sense and will to survive, Nik, that is suicide. Nikolai: That’s a shame that you think that, Inno. Why do you hold me back so? CLICK Inno: I’m not holding you back at all, Nik, I am your best friend, your only friend out here. CLICK Nikolai: Friends are for peace, not war. BOOM.

What…? He held me back, and I was a ghost that needed to be absolutely free. The last shred of the shackle that bound me was now splattered all over the snow in a brilliant display of red. It was like a message written in the language of life and death, my language. The language of God.

… that’s right. God.
Blasphemy, you say? Poslisha Tai, Mudak!
You go out there and tell me that your religion will save you? NIET!
There is only ONE religion in that wasteland, MINE.
My church is the war zone, my prayers are the gunshots, so I hear people praying all day
long to God – Me. Because I tell you that THIS god is not on the battlefield
CLICK
I am God on the battlefield!
CLICK!
I choose who lives, and who dies! I see life
BOOM!
And I Take it.

But look at the great reaper of life now, useless. Berlin has been taken, the Germans are gone, and I am without a target. Peace is hell. A God of the battlefield in a world devoid of battles. I have no purpose in this land any longer, my purpose is to destroy, and I was not good at it. I was God at it.

(Nikolai takes a pistol out of the back of his belt, a German luger)

I miss the war zone church,
Click
I miss the gunshot prayers.
Click
But at least I can hear my prayer one last time.

(He holds the pistol to his chin, looks skyward, closes his eyes, and pulls the trigger.)

Boom.
```

---

## IC-0412: THE YEARBOOK

- Title: THE YEARBOOK
- Author (byline): josh danz
- Work: THE YEARBOOK
- Publisher: Mushroom Cloud Press
- Publication date as stated: 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1246
- Already set (do not supply): none

### Source block (context only)

```text
(none)
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
You know that girl from the Brady Bunch? You know the “Marsha, Marsha, Marsha” one…. Yeah that’s me. I mean, it’s not that I’m jealous of my sister… It’s just that I go out of my way to wake up early for her so I can take her to school and drop her off so she can see her friends... and me well… (Pause) OK! So I’m jealous! But it’s cool, it’s normal, it’s ok to be jealous…. Of your 13 year old sister. (Look up and close the book- embarrassed)

When it comes to my sister, I’m pretty protective of her. And with good reason. She looks older than 13… I would say 16. And… you know, at that age… the boys…. They’re horny little bastards. So, if I see some kid approach her, I do what any big brother would do…. I beat the shit out of each one of them. Black eyes, bloody nose, broken knee caps… the whole nine yards. I don’t really mind doing it. Maggie on the other hand… (Shake hand in so-so motion). She hates it… but she’s my sister, you know? So I gotta protect her.

You know, it’s funny. I remember the day she got caught skipping school. I did that once, and my ass was on lockdown for a good 3 months. And Maggie never gets in trouble. She’s always looked at as the princess and me… I’m not. Not that I’d want to be a Princess or anything. Anyway, she ended up getting off easy at school. An afternoon of detention. But the hard part was telling our parents. They would look at you and just stare. Silence. I mean, I would rather be bombarded with screaming. Do you know what the silent stare is like? (Stare at someone for a few seconds with big eyes and odd expression). It’s awkward yes? … Yeah, and Maggie didn’t want to go through that. So I get this call from Maggie on the way to basketball practice saying that she’s a whole lot of trouble and she really, really needs my help.

Maggie never needs my help, so here I am thinking ‘Oh crap…. Oh crap…. she’s in prison…… Then she tells me she got caught skipping. So I picked her up.

When I got there, she started to cry. It wasn’t often that my sister cried in front of me, because she always puts up that tough guy act, but when she did, it made me realize that she was still a little girl, you know? “Ben, I’m so sorry, I won’t do it again… Please don’t tell mom and dad. Please Ben.”

Phew…. Good thing I didn’t over react! (Embarrassed smile)

Now here it is, weeks before graduation and I’m pumped. A few weeks back we were told that there would be an assembly for all seniors. One final time to be together before we left. The assembly was at 4:00, and Maggie needed to be picked up at 4:45. Clearly that wasn’t going to happen. So on the day of the assembly, Maggie reminded me that Sarah’s mom was taking her home…. And begged me, not to check up on her. And though I didn’t like the idea, I thought, hey, what the hell?

So after the assembly I got in my car, but it seemed like out of nowhere, I started to feel sick. I figured the pain was either the tacos I ate for lunch in the cafeteria, which (Nod)… pretty likely, or nerves about graduating! I sat there a minute and just waited until the pain went away. When I left, I drove by Maggie’s school which was on the way home. When I looked over in the parking lot, I saw a couple ambulances with a crowd of people gathered around them there, and I thought “Damn, I bet they served those tacos at Maggie’s school too! (Laugh)” Let me tell you something. If there is one thing that I’m looking forward to about college, it’s not having to eat that crap they serve to you in the cafeteria. Three weeks ago, the Chess Team had an “End of the year banquet, catered by the lunch ladies.” The chess team is like the pride and joy of our school. And that’s mainly because: our football team sucks, and… well the rest of our teams are practically non-existent. But that’s beside the point. The lunch ladies managed to practically poison the entire chess team just before Nationals. The culprit… bad lettuce. Lettuce! Seriously, who gets sick from lettuce? And you know what, based on that story, I knew whatever happened over at Maggie’s school couldn’t be that bad.

When I got home I heard my parents in the kitchen. By the way things sounded, it seemed that they had gotten into yet another argument. I could hear my mother “Crelling and Sitching,” as I liked to call it. Which is umm… a combo of crying, yelling screaming and bitching... mainly bitching. Now, usually I’d leave em’ alone, but uh, well I’m nosey. When I walked in I knew something was going on, and then, I see the blood just drain out of my mother’s face. She looked at me, then looked at my father, then tears were pouring out of her eyes. (Pause) “What the hell is going on here? (Pause) What’s the Problem?” Then my father started to cry. (Long Pause)

They said my sister died about 25 minutes after the accident. Apparently the father of some girl lost control of his car and ummm… (Turn to the side). I mean, here I am joking about the cafeteria food and she can’t even breathe. (Pause) And I couldn’t do anything. (Said whispering).

I went back to school a week later. When I walked to lunch that day, a man who I thought was Maggie’s Principal came up to me. He introduced himself and told me he was sorry to hear about what happened. He said something about this Grief Group meeting for the 8th grade the next day. He told me that over the past four days, all of Maggie’s friends and teachers had signed her yearbook, and that he wanted me to read a few of the things from it. I mean do I do it, do I not do it… And then he said, “Look Ben, I know it’s short notice, but we’d really like you there.” (Pause… put book under arm… warm up hands and say “ok.”)

As I walked into the auditorium the next day, I started to reconsider reading Maggie’s yearbook, but after being introduced by Mr. McGee, I looked into the crowd of about 200 or so and thought “Here we go”. (Open book to first page) (Clear Throat)

“Mags, you are my best friend now and always. I will never forget your smile. I miss you so much and I just want to tell you that I love you. Your best friend, Sarah.”

(Chuckle) I thought back to when Maggie got stuck in a raft at this water park and even though my parents were right next to her, she called for me.

About an hour had passed and there were only a few more signings for me to read. After I finished reading the last one, I sat there for a minute and just looked out at these people. I thought about to say something, but I got choked up. When I regained my composure, I looked back up and said “Thank you all for coming here today. It means a lot to me, and I’m sure it means a lot to Maggie. Thank you for writing these amazing things in my sister’s yearbook. But most of all, thank you… Thank you, for making me feel like Maggie’s brother again (Smile).”
```

---

## IC-0413: My Son Susie

- Title: My Son Susie
- Author (byline): Cheryl Royce
- Work: Women Playwrights: Best of 1993, Pgs 178-186
- Publisher: Smith and Kraus Publishers
- Publication date as stated: June 1994
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SEYMORE, SISTER MARY, MRS. SINGH, KAY
- Teaser before the introduction: Yes
- Spoken words (computed): 1583
- Already set (do not supply): none

### Source block (context only)

```text
Author: Cheryl Royce
Book: Women Playwrights: Best of 1993, Pgs 178-186
ISBN: 978-1880399453
Publisher: Smith and Kraus Publishers
Date (Month/Year): June 1994
```

### Introduction (context only: never use it for content warnings)

```text
Both my parents loved me. I know that emphatically, down in the deepest recesses of my being. I haven’t always given them the love . . . the respect they deserve . . . see, they are retarded. That’s the word they used when I was growing up in the 1960’s. Today the better term is “intellectually challenged.”

My Son Susie by Cheryl Royce.
```

### Performance text (classify this)

```text
A man speaks from the waiting room of a hospital maternity ward and reflects on his own childhood.

SEYMORE: (Pg 178) I was born on May 19, 1962, a son, to Eleanor and Buster Santacroce of Skokie, Illinois. I was perfectly normal in every way. Delivered in the manner of Julius Caesar due to the extreme size of my head and the extreme youth of the mother. She was 15 at the time.

SEYMORE: (Pg 178-182) To say that my birth was “unplanned” is the hyperbole of understatement. Both my parents were orphans, my mother abandoned at birth in a laundry basket on the church steps. No kidding. My father was a change-of-life baby born in the 49th year of a woman already mother to eight others. She died when he was 4. Buster wended his way through the foster care system until he arrived at the same institution as my mother. It was love at first sight. Mom and Pop. Romeo and Juliet. John and Yoko. The Captain and Tenille.

Oh, did I mention that my parents are severely retarded?

Had this occurred in a secular institution, a discreet abortion would have been performed, especially in light of the fact that neither of the parents had parents and to cover the odd bureaucratic ass for its obvious lack of supervision. But it was a Catholic institution and instead, discreet nuptials were performed and the groom carried his pregnant bride over the threshold of an efficiency apartment paid for by the parish.

Buster and Eleanor were legally married in the eyes of God and therefore entitled to all conjugal embraces, which is Catholic for . . . the hokey-pokey. Since birth control is forbidden and the rhythm method beyond a pair who counts “1, 2, 9, 17, 9 . . . “; since Eleanor had at least thirty fertile years ahead of her, and Buster, was 23, letters seeking a sterilization procedure were dispatched to the Vatican . . . [but] May 19 rolled around, and the Holy Father still had not been heard from. As Buster sat in the waiting room, amusing himself with pictures of bare-breasted African women in the National Geographics, a kindly Jewish doctor knocked Eleanor out, brought her 9 pound baby boy into the world, and without fuss or fanfare, (or anyone’s permission) quietly tied her tubes. While Catholics and Jews share the same Ten Commandments, I always suspect that an Eleventh was slipped to Moses on Mt. Sinai and that is . . . Common Sense.

Eleanor came out of the ether none the worse for wear and delighted as a child to see me. Buster was overjoyed, though I suspect that some of his excitement was due to the naked ladies he had been ogling all afternoon. A few days later, the nurse enquired of my mother the name of the baby for the birth certificate. “Susie” she replied promptly and would not be dissuaded despite the calendar of saint’s names proffered. Buster was consulted, but his choice of “Boy” was hardly better and rather than have me sound like something out of a Tarzan comic book, they turned again to my mother. Besides, Buster had discovered the buttons for making the hospital bed go up and down and was having too much fun to concern himself with the problem at hand. At this point, the kindly Jewish doctor intervened once more and wrote “Seymore” in the space for given name. The name he gave me was his own.

Since the Catholics don’t have a “Saint Seymore” I was baptized “Savior” – close enough – and Santacroce which means “Holy Cross” and is the name of the parish church. SO it is Seymore Savior Santacroce who [is] before you. My mother, however, calls me “Susie” to this day.

When the proud parents returned to the apartment, they did not go alone. They were accompanied by a flotilla of nurses, public health care officials, advocacy groups for the “intellectually challenged,” journalists, nuns, neighborhood biddies, thrill seekers and a succession of social workers only marginally les strange than they.

I, like the Sleeping Beauty of the fable, was attended by a dozen fairy godmothers on any given day. I was coddled and cuddled. The “flotilla’s” main concern was that I might not be receiving enough “stimulation.” And so I was flashcarded, Montessori’ed, and Suzuki’ed within an inch of my life, any quiet time with a thumb and a blanket viewed as delinquency on the part of my nursemaids. I was like the office philodendron which everyone waters because they are afraid no one else will. It didn’t hurt me though.

I grew until at the age of 5, having an intelligence higher than that of both my parents – combined – I set off for the first day of kindergarten. What a day it was! Remember your very first day of school? The pity? The terror? Papa Bear, Mama Bear, Baby Bear and our social worker, Mrs. Singh – striking out while the porridge cooled! Mrs. Singh bundled us into her Nash Rambler and off we dashed to Holy Cross Parochial School – Sister Mary’s K-1 class! Wheee!

Sister Mary was young and freckled and sweet as pie. [She] shook hands politely with Mother and Father, introduced them to some of the other parents and graciously invited them to look around the room. Then she knelt down to me.

SISTER MARY: What’s your name?

SEYMORE: (shyly) Susie (to audience) Sister Mary had been forewarned, but not for that.

MRS. SINGH: His name is Seymore

SEYMORE: But from the end of the room came my mother’s ten decibel echolalia, “Susie, Susie, Susie, Susie, Susie, Susie, Susie!” setting everyone straight for once and all.

Then came the moment of truth: the moment when mothers and fathers and social workers tiptoe out of the room. I was a brave boy. I didn’t cry or wet my pants. Buster did both. It was less about leaving me than leaving a toy fire engine he had been riding around the room.

Mrs. Singh tried to coax him away, but he was having none of it. Great blubbering sobs shook him. Eleanor had meanwhile retreated to the farthest corner of the playhouse and had taken up her wail of “Susie, Susie, Susie.” Several children joined Buster in his blub, blub, blubbing. Eventually, they all just ran out of steam, and as kindergarten was only half-day, Mrs. Singh was able to drive us home a couple of hours later, a good time had by all. Wheeee! (long beat)

(Pg 183-186) Escape came on the “little cat feet” of a college education. The State defrayed all my tuition and expenses and threw in a stipend. I went away to school. My mother cried and so did my father. And he wet his pants again. I phoned them frequently at first, and while they both loved the telephone, our lopsided conversations grew harder and harder and Buster and Eleanor grew more and more remote. I made phone calls instead to their social worker, Mr. Gold, to reassure myself that they were OK. I was convinced they hardly knew I was gone and positive they didn’t miss me. I didn’t miss them. The sweet breezes of normalcy blew through my life for the first time.

It was spring of my freshman year. I hadn’t seen Mom and Pop since Christmas. I hadn’t pledged a frat but was considering it for the fall. Anyway, that’s where I was on a beautiful spring night – in a frat house on Greek Row, kissing the prettiest girl in the room – when I saw the hunched back of Mr. Gold enter the room.

I can’t tell you what my heart did. For close behind him were Buster and Eleanor. The room went silent. Not all at once. Voices died and conversations dropped off and someone unplugged the stereo that was blaring and the trio stopped before me. Mr. Gold explained that Eleanor had become more and more despondent when she hadn’t heard from “Susie” and that Buster had been dialing his number at all hours of the day and night, hollering that it was a “mergency!” And so, at his wits’ end, he had piled them into his car and driven them to see me. He was sorry, but what was he supposed to do?

I stood like a tree stump. I could see the two of them holding hands and grinning from ear to ear behind Mr. Gold. I think Eleanor waved a little wave. And I could see my life pass before my eyes. Not my past. My future. The girl I had been kissing, the pretty one, stepped from behind me and around Mr. Gold.

KAY: You must be Seymore’s parents. It’s nice to meet you. My name is Kay. Seymore, why don’t we take your folks outside.

SEYMORE: Which of us doesn’t think their parents are retarded? Who doesn’t live with them in an agony of love and shame? No one. (long beat)

Buster died later that year. He was 43. As you may or may not know, the retarded have a shorter life expectancy. I was home when it happened, on summer vacation. The sound that came out of Eleanor when I told her was like nothing I have heard before or since. She howled like a dog is as near as I can describe it. And she wept. Endlessly. Ceaselessly. Tirelessly. For three days. And then, I think, she forgot. (long beat)

[Kay’s] inside now, sleeping. She just gave birth to our daughter. Six pounds, eight ounces. Susan Eleanor. (picks up the baby from her crib and crosses to Eleanor, his mother, gently handing her the swaddled baby) So, Mom, what do you think of your new granddaughter . . . Susie . . . That’s right, Mom. (to audience) Perfectly normal in every way.
```

---

## IC-0414: Nigger: An Autobiography

- Title: Nigger: An Autobiography
- Author (byline): Dick Gregory
- Work: Not specified
- Publisher: Simon and Schuster Adult Publishing
- Publication date as stated: May 1976
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DICK, TEACHER, HELENE, WINO, MR. WILLIAMS
- Teaser before the introduction: Yes
- Spoken words (computed): 2283
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

DICK: This is a revolution. It started long before I came into it, and I may die before it’s over, but we’ll bust this thing and cut out this cancer. America will be as strong and beautiful as it should be, for black folks and white folks. We’ll all be free then, free from a system that makes a man less than a man, that teaches hate and fear and ignorance.

You didn’t die a slave for nothing, Momma. You brought us up. You and all those Negro mothers who gave their kids the strength to go on, to take that thimble to the well while the whites were taking buckets. Those of us who weren’t destroyed got stronger, got calluses on our souls. And now we’re ready to change a system, a system where a white man can destroy a black man with a single word. Nigger.

When we’re through, Momma, there won’t be any niggers any more.

Page 25 - 32

DICK: Like a lot of Negro kids, we never would have made it without our Momma. When there was no socks to go with the shoes, no hope to go with tomorrow, she’d smile and say: “We ain’t poor, we’re just broke.” Poor is a state of mind you never grow out of, but being broke is just a temporary condition. She always had a big smile, even when her legs and feet swelled from high blood pressure and she collapsed across the table with sugar diabetes. You have to smile twenty-four hours a day, Momma would say. If you walk through life showing the aggravation you’ve gone through, people will feel sorry for you, and they’ll never respect you. She taught us that man has two ways out in life – laughing or crying. There’s more hope in laughing. So you laugh, so you smile.

(PG 28) I wonder how she kept from teaching us hate when the social worker came around. [She] would poke around the house, wrinkling her nose at the coal dust on the chilly linoleum floor, shaking her head at the bugs crawling over the dirty dishes in the sink. [Mama] would follow that nasty *woman* around those drafty three rooms, keeping her fingers crossed that the telephone hidden in the closet wouldn’t ring. Welfare cases weren’t supposed to have telephones. (Page 23) When you have a good mother and no father . . . God kind of sits in.

(PG 29) I never learned hate at home, or shame. I had to go to school for that. I was about seven years old when I got my first big lesson. I was in love with a little girl named Helene Tucker, a light-complexioned little girl with pigtails and nice manners. She was always clean and she was smart in school. I think I went to school then mostly to look at her. I brushed my hair and even got me a little old handkerchief. It was a lady’s handkerchief, but I didn’t want Helene to see me wipe my nose on my hand. The pipes were frozen again, there was no water in the house, but I washed my socks and shirt every night. I’d get a pot, and go over to Mister Ben’s grocery store, and stick my pot down into his soda machine. Scoop out some chopped ice. By evening, the ice melted to water for washing. I got sick a lot that winter because the fire would go out at night before the clothes were dry. In the morning I’d put them on, wet or dry, because they were the only clothes I had.

Everybody’s got a Helene Tucker, a symbol of everything you want. I loved her for her goodness, her cleanness, her popularity. She’d walk down my street and my brothers and sisters would yell, “Here comes Helene,” and I’d rub my tennis sneakers on the back of my pants and wish my hair wasn’t so nappy and the white folks’ shirt fit me better. I’d run out on the street. If I knew my place and didn’t come too close she’d wink at me and say hello. That was a good feeling. Sometimes I’d follow her all the way home, and shovel the snow off her walk and try to make friends with her Momma and her aunts. I’d drop money on her stoop late at night on my way back from shining shoes in the taverns. And she had a Daddy, and he had a good job. He was a paperhanger.

I guess I would have gotten over Helene by summertime, but something happened in that classroom that made her face hang in front of me for the next twenty-two years. When I played the drums in high school it was for Helene, and when I broke track records in college it was for Helene and when I started standing behind microphones and hear applause I wished Helene could hear it, too. It wasn’t until I was twenty-nine years old and married and making money that I finally got her out of my system. Helene was sitting in that classroom when I learned to be ashamed of myself.

It was on a Thursday. I was sitting in the back of the room, in a seat with a chalk circle drawn around it. The idiot’s seat, the troublemaker’s seat.

The teacher thought I was stupid. Couldn’t spell, couldn’t read, couldn’t do arithmetic. Just stupid. Teachers were never interested in finding out that you couldn’t concentrate because you were so hungry, because you hadn’t had any breakfast. All you could think about was noontime, would it ever come? Maybe you could sneak into the cloakroom and steal a bite of some kid’s lunch out of a coat pocket. A bite of something. Paste. You can’t really make a meal of paste, or put it on bread for a sandwich, but sometimes I’d scoop a few spoonfuls out of the paste jar in the back of the room. Pregnant people get strange tastes. I was pregnant with poverty. Pregnant with dirt and pregnant with smells that made people turn away, pregnant with cold and pregnant with shoes that were never bought for me, pregnant with five other people in my bed and no Daddy in the next room, and pregnant with hunger. Paste doesn’t taste too bad when you’re hungry.

The teacher thought I was a troublemaker. All she saw from the front of the room was a little black boy who squirmed in his idiot’s seat and made noises and poked the kids around him. I guess she couldn’t see a kid you made noises because he wanted someone to know he was there.

It was on a Thursday, the day before the Nero payday. The eagle always flew on Friday. The teacher was asking each student how much his father would give to the Community Chest. On Friday night, each kid would get the money from his father, and on Monday he would bring it to the school. I decided I was going to buy me a Daddy right then. I had money in my pocket from shining shoes and selling papers, and whatever Helene Tucker pledged for her Daddy, I was going to top it. And I’d hand the money right int. I wasn’t going to wait until Monday to buy me a Daddy.

I was shaking, scared to death. The teacher opened her book and started calling out names alphabetically.

TEACHER: Helene Tucker?

HELENE: My Daddy said he’d give two dollars and fifty cents.

TEACHER: That’s very nice, Helene. Very, very nice indeed.

DICK: That made me feel pretty good. It wouldn’t take much to top that. I had almost three dollars in dimes and quarters in my pocket. I stuck my hand in my pocket and held onto the money, waiting for her to call my name. But the teacher closed her book after she called everybody else in the class. I stood up and raised my hand.

TEACHER: What is it now?

DICK: You forgot me. (to the audience) She turned toward the blackboard.

TEACHER: I don’t have time to be playing with you, Richard.

DICK: My Daddy said he’d . . .

TEACHER: “Sit down, Richard, you’re disturbing the class.

DICK: My Daddy said he’d give . . . fifteen dollars. (to audience) She turned around and looked mad.

TEACHER: We are collecting this money for you and your kind, Richard Gregory. If your Daddy can give fifteen dollars you have no business being on relief.

DICK: I got it right now. I got it right now, my Daddy gave it to me to turn in today, my Daddy said. . .

TEACHER: And furthermore,

DICK: (to audience) she said, looking right at me, her nostrils getting big and her lips getting thin and her eyes opening wide,

TEACHER: we know you don’t have a Daddy.

DICK: Helene Tucker turned around, her eyes full of tears. She felt sorry for me. Then I couldn’t see her too well because I was crying, too.

TEACHER: Sit down, Richard.

DICK: And I always thought the teacher kind of liked me. She always picked me to wash the blackboard on Friday, after school. That was a big thrill; it made me feel important. If I didn’t wash it, come Monday the school might not function right.

TEACHER: Where are you going, Richard?”

DICK: I walked out of school that day, and for a long time I didn’t go back very often. There was shame there.

Now there was shame everywhere. It seemed like the whole world had been inside that classroom, everyone had heard what the teacher had said, everyone had turned around and felt sorry for me. There was shame in going to the Worthy Boys Annual Christmas Dinner for you and your kind, because everybody knew what a worthy boy was. Why couldn’t they just call it the Boys Annual Dinner, why’d they have to give it a name? There was shame in wearing the brown and orange and white plaid mackinaw the welfare gave to three thousand boys. Why’d it have to be the same for everybody so when you walked down the street the people could see you were on relief? It was a nice warm mackinaw and it had a hood, and my Momma beat me and called me a little rat when she found out I stuffed it in the bottom of a pail full of garbage way over on Cottage Street. There was shame in running over to Mister Ben’s at the end of the day and asking for his rotten peaches, there was shame in asking Mrs. Simmons for a spoonful of sugar, there was shame in running out to meet the relief truck. I hated that truck, full of food for you and your kind. I ran into the house and hid when it came. And then I started to sneak through alleys, to take the long way home so the people going into White’s Eat Shop wouldn’t see me. Yeah, the whole world heard the teacher that day . . . . we all know you don’t have a Daddy.

It lasted for a while, this kind of numbness. I spent a lot of time feeling sorry for myself. And then one day I met this wino in a restaurant. I’d been out hustling all day, shining shoes, selling newspapers, and I had goo-gobs of money in my pocket. Bought me a bowl of chili for fifteen cents, and a cheeseburger for fifteen cents, and a Pepsi for five cents, and a piece of chocolate cake for ten cents. That was a good meal. I was eating when this old wino came in. I love winos because they never hurt anyone but themselves.

The old wino sat down at the counter and ordered twenty-six cents worth of food. He ate it like he really enjoyed it. When the owner, Mister Williams, asked him to pay the check, the old wino didn’t lie or go through his pocket like he suddenly found a hole.

WINO: Don’t have no money.

MR. WILLIAMS: Why in hell you come in here and eat my food if you don’t have no money? That food cost me money.

DICK: Mister Williams jumped over the counter and knocked the wino off his stool and beat him over the head with a pop bottle. Then he stepped back and watched the wino bleed. Then he kicked him. And he kicked him again.

I looked at the wino with blood all over his face and I went over. (to Mr. Williams) Leave him alone, Mr. Mister Williams. I’ll pay the twenty-six cents.

(to audience) The wino got up, slowly, pulling himself up to the stool, then up to the counter, holding on for a minute until his legs stopped shaking so bad. He looked at me with pure hate.

WINO: Keep your twenty-six cents. You don’t have to pay, not now. I just finished paying for it.

DICK: He started to walk out, and as he passed me, he reached down and touched my shoulder.

WINO: Thanks, sonny, but it’s too late now. Why didn’t you pay it before?

DICK: I was pretty sick about that. I waited too long to help another man. (PG 177) And it dawned on me that anytime you help a Negro in America, even the Negroes will question your intentions. I was just beginning to realize what a long hard row it would be.

(PG 209) Those of us who weren’t destroyed got stronger, got calluses on our souls. And now we’re ready to change a system. (PG 201) Every white man in America knows we are Negroes, and some of them know us by our names. So when he calls us a nigger, he’s calling us something we are not, something that exists only in his mind. So if nigger exists only in his mind, who’s the nigger? (PG 209) When we’re through, Momma, there won’t be any niggers any more.
```

---

## IC-0415: Nocturne

- Title: Nocturne
- Author (byline): Adam Rapp
- Work: Not specified
- Publisher: Faber and Faber, Inc.
- Publication date as stated: Dec 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SON, MOM, DAD
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
SON: Fifteen years ago I killed my sister. There. I said it. . . I can change the order of the words. My sister I killed fifteen years ago. I, fifteen years ago, killed my sister. Sister my killed I years ago fifteen.

I can cite various definitions. To deprive of life: the farmer killed the rabid dog. To put an end to: the umpire killed the tennis match. To mark for omission: he killed the paragraph. To destroy the vital essential quality of: the dentist killed the nerve with Novocain. To cause to stop: the bus driver killed the engine. To cause extreme pain to: his monologue killed the audience. To slay. To murder. To assassinate. To dispatch. To execute.

You can play with tenses. Will kill. Did kill. Have killed. Will have killed. Would like to have killed. You can turn it into a gerund. Killing. There's a kind of progress with a gerund. If you conjugate in the past tense it's all the same. I killed. You killed. He, she, it killed. They killed. You all killed. We killed. There's no way around it.

Fifteen years ago I killed my sister. I was seventeen, she was nine. A fact.

SON: The accident happens like this: Joliet, Illinois. I'm coming home from Sub- Diggity, my summer sandwich-making job. My clothes smell like roast beef and mayonnaise. My fingers are stained with mustard. Steely Dan's Hey Nineteen is playing on the AM. (Singing – see end of selection for a link to the lyrics and music of this song) Way back when In Sixty-seven / I was the dandy Of Gamma Chi

It's the second week in July. I'm traveling west on Black Road. It's roughly ninety-five degrees. Mosquitoes are plotting their mid-summer feast. There's an endless feeling of Little League being played. Slurpies and caramel corn. Blue snow cones staining the chins of toddlers. Hot-dogs that are so good they can feed entire families. An ocean of Little League diamonds.

I tum south onto Gael Drive. (Singing) Sweet things from Boston So young and willing / Moved down to Scarsdale

I'm going forty-five in a thirty. At least that's where the speedometer freezes after the collision.

So, it's seven-thirty and the sun is a flaming orb on the horizon. There are colors in the sky. Reds. Pinks. Burnt oranges. Clouds like frayed gauze. Their underbellies golden somehow. Steely Dan is well into its chorus. (Singing) The Cuervo gold The fine Colombian / Make tonight a wonderful thing Say it again . .

I turn north onto Gael Drive and I decide to not go home. There's a place where I'll sometimes go and think. It's an enormous platoon of power lines. The radio trees. I want to take my shoes off and feel the buzz in my feet.

I accelerate. Something small runs out in the road.

I brake. Nothing happens. It's a dog. A garbage can.

A plastic bag that's stolen a bit of breeze. I pump the brake pedal. I swerve. There's a thud. A hollow, almost wooden thud. Small as an egg. I continue pumping the brakes. Nothing happens. Steely Dan turns into the Alan Parsons Project. (see end of selection for a link to the lyrics and music of this song) I am the eye in the sky.

I pump the brakes and the Electra just keeps going as though by its own volition. I swerve. I counterswerve. I crash into a large oak tree at the end of the street. The front end of the Electra accordions to the windshield. Birds are everywhere. A schizophrenic cloud of crows.

I crack three ribs and break my nose. I can taste the metal in my blood. Like warm pewter. The speedometer sticks at forty-five miles per hour.

In that strange, post-crash ethereal silence, I get out of the car and walk the hundred yards or so back to where I heard the thud. The crows have formed a kind of wavering anvil and are flying south toward the sound of the highway. It feels as if the steering wheel has been inserted into my ribcage.

My sister's body lies in the street. It looks like a doll's body. Legs. Feet. Yellow socks perfectly folded. Bits of lace turned down-my mother's touch. Shoes so small it's as if they were born out of a children's fable. Hands. Arms. Neck. A small white dress with blue flowers. Anemones. Buttercups.

Her head is across the street. It has rolled into the Petersens' driveway. I walk over and pick it up. Simply. Perfunctorily. Only a feeling of great clarity and absence. Like a sudden gust of lake wind. As if it's a ball or some kind of fugitive picnic toy. Its weight seems tremendous. I will reattach it to the neck and she will rise off the pavement and go back into the house and wash up for supper.

As I'm reattaching my mother can be seen framed in the living room window, her hand pressed against the glass, her head slightly tilted as though she is peering out over a strange body of water; as though she is watching something hellish emerging from the fog.

The sound of sirens. Shrieking sirens from all directions. The shrieking turns into a kind of weeping. Sirens weeping in an octave only known to whales and dolphins.

***********

I can't remember my sister's face.

Other parts of her are as definite as forks and knives. Legs so slender you wonder how they could support the weight of even the smallest torso. Her wrists as thin as Popsicle sticks. Her boyish arms. Mosquito-bitten. Stained with iodine and calamine lotion. Her tiny hands. Her fingers as light and delicate as bird bones.

I try and reconstruct the images.

• Frame one: a dog; King-the Petersens' German Shepherd.

• Frame two: a bird; a spooked swallow swooping down from some unknown eaves; nose-diving into the grille at the threat of rain.

• Frame three: a small garbage can; green somehow; for recycling; and plastic because there's no music in the thud.

• Frame four; a mis-kicked football hurtling end-over-end from the Doughertys' back yard.

• And then frame five: My sister in her dress; her hand rising up theatrically.

Stop. Please stop. Not now. Not like this. I'm too small for this to happen.

She swam. She rode her bike. She liked boys' clothes. She'd steal my boxer shorts and wear them to swimming practice. Once at dinner she ambitiously announced her plan of owning a tuxedo. My mother, of course, made her wear dresses and pierced her ears.

She proposed marriage to me at least once a week. She'd go to a knee and say, Marry me you big juicy hunk of yummy boy steak. I'm not kidding. She'd actually say that. And then she'd laugh and I'd laugh and the chorus of our laughter was like a jet flying through our silent house. . . She called me Dorkus.

So the memories are there. As clear as if they happened yesterday. I just can't see her face.

I wonder if she wanted to be hit. She wasn't chasing a ball or a kite. There weren't any kids calling to her from the other side of Gael Drive. She wasn't pushed from behind. From our driveway approaching cars can be seen at least fifty yards away.

No, she wasn't abused. She wasn't ridiculed. She was rarely, if ever, sent to her room. She was loved. And fed. She was well clothed. She was the first girl on her swim team to do the butterfly. In jacks she was good to sixes.

A faceless child walks in front of a speeding car. I could buy that. A man with three children and a beautiful wife leaps from the thirtieth floor of his Wall Street building. A pregnant woman walks off the Verrazano Bridge and everyone says she was so happy. But you never hear about it with children. It's always an accident

[But] perhaps there is a kind of deathwish in some children: I don't want to be an adult. I don't want to do that. I don't want to hide behind the drapes and darn my husband's socks. I don't want my belly to distend with multiple pregnancies or the disease of tumors.

I want to swim and run and spin. I want to get away with things. I want to eat snow cones for the rest of my life. So I'll end it while the going's still good. And I'll make it quick. I'll walk in front of a speeding car.

The evening of my sister's death it was discovered that the brake line on the Electra had snapped.

I'm in the hospital when my mother walks-or rather glides-into my room. Her face hardened with grief. She sits in a chair beside me for a long time before she speaks. I look down and see that her hands are clenched into fists.

MOM: It was the brake line . . . They're going to let you off with involuntary manslaughter. The only thing you are guilty of is failure to stop to avoid an accident.

SON: She almost sounds disappointed.

MOM: A fifty-dollar fine. Your father paid it for you. . . He's taking it very hard.

SON: (to Mom) How are you, Mother? (to audience) She doesn't respond. Her eyes are screaming to blink. (to Mom) I'm sorry, Mother.

MOM: It wasn't your fault . . . Your father is taking it pretty hard, but we'll get through this. . . Rest well

SON: And then she gets up and walks out. That would be the last thing my mother would say to me: Rest well.

A month after the accident, she would move out of our little house on Gael Drive and into an apartment with her sister. She would live with my aunt for three years and then, one day, I would receive a letter from her sister saying that my mother had been moved to a private boarding residence for the clinically depressed. I would later learn of the daily diet of a hundred milligrams of Haldol and the bench where she spends most of her afternoons incessantly singing Old MacDonald's Farm and that her favorite pastime is the making of potholders.

My father takes the death of my sister pretty hard. We haven't spoken since I've been home. I hover at the door to his study, leaning against the jamb. He can't look at me.

DAD: Come in, Son.

SON: I've lost my name. I enter his study. I sit across from him at his hulking oak banker's desk. His hands are flat on the blotter. His head tilted down, almost shamefully. There is a small snub-nosed revolver set between the axis of his thumbs. I have never seen this gun before. I had no idea that there's a small black gun living in our house. (to Dad) Dad, is that a gun? Dad . . .

(to audience) The gun is clutched between his hands now and its nose pointed at my throat. In a slow deliberate lean the gun gets closer and closer. I am thinking, "No, Dad. Please, no." But nothing comes out.

DAD: Don't move.

SON: The gun is in my mouth now. The cylinder forcing my lips apart. Like kissing the engine of a toy train. Its smell of axle grease. Its weight incredible on my teeth. My father seethes. His breath is hot and his skin is a flat dull pink and I don't recognize myself in him. I see nothing of his only son in this strange violent intimacy. . . . I hear my mother's voice.

MOM: (gently with fatigue) Earl. Put the gun down, Earl. . . Not this way, Honey.

SON: It's as if she is coaxing a child out of a tree. Not this way, Honey. What does that mean?

He would remove the gun from my mouth and my mother would take it and drop it in the trash, somehow rendering the thing powerless.

The taste of it still haunts me. Sickens me.

I would eventually lift off the chair and walk out of our little house on Gael Drive. I would lurch/slouch/spiral to a bus stop. The bus would take me to the train station. I would arrive in New York City the following morning in a kind of severe, tightly coiled body clench.

Grand Central Station. A cathedral with noise. Anonymity.

Here is where I would begin my fifteen-year disappearance from the town with the little house on Gael Drive. I would step out onto Forty-second Street with twelve dollars and forty-two cents in my pocket. . . [because] Fifteen years ago I killed my sister. I was seventeen, she was nine.
```

---

## IC-0416: Not a Genuine Black Man

- Title: Not a Genuine Black Man
- Author (byline): Brian Copeland
- Work: Not specified
- Publisher: Hyperion
- Publication date as stated: July 2006
- Event as filed: Dramatic Interpretation
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
It has often been said that comedians deal with pain through humor. They laugh so they don’t have to cry. This was especially true for comedian Brian Copeland. When he was eight, his mother moved his family from Oakland to San Leandro, hoping to escape her abusive husband. Now, keep in mind, that in the early 1970s, San Leandro was 99.99% white and considered one of the most racist enclaves in the nation. The result? He was labeled his whole life - an outsider in his own community based on the color of his skin and an outsider within his race for not being black enough.

Brian spent his adult years trying to leave behind his painful childhood. But an anonymous letter ultimately forces him question his own identity.

Not a Genuine Black Man by Brian Copeland
```

### Performance text (classify this)

```text
BRIAN: (xi-xii) Although I’m a stand-up comic by trade, I also do a radio show for a talk station in San Francisco. (begins to settle back into his office) I’d been out on the road for a couple of weeks, and when I got back into the station, I had all this mail piled up. In talk radio, mail generally comes to you from two sources: old ladies and kooks. That’s it. Nobody else writes you. The upside is that it makes the mail easy to sort. (going through his mail)

So I’m going through the pile. Old lady. Old lady. Death threat. Old lady. Ooh, here’s a good one. Death threat from an old lady.

Then I come across one that’s typed . . . I mean typed on an actual typewriter. No return address. Local postmark. Addressed to me. I open it, taking out an unsigned sheet that reads: “As an African American, I am disgusted every time I hear your voice because . . .”

(trails off as he finishes the sentence silently; tries again aloud.) “As an African American, I am disgusted every time I hear your voice because YOU are not a genuine black man.”

BRIAN: (xii-xiv) (picks up reading again) “... not a genuine black man.” Why do people say that to me? Actually, people have said that to me throughout my life. I don’t even know what that means. Is it how I dress? Is it how I talk? Is it how my machine is set to TiVo (could replace with Stream) Frasier?

If you’re talking about pigment, you can tell by looking at me that I am clearly black. But if you’re talking about some cultural delineation, I don’t know. I can’t swim. That’s black.

(Thinks for a moment) I’m a Democrat. That’s black. I never understood black Republicans. To me, a black joining the Republican Party is like a deer joining the National Rifle Association.

(xvii) Whatever the answer is, any confusion I have about race, any misunderstanding I have about ethnicity, any confusion I have about blackness . . . is my mother’s fault. [When I was 8-years-old she moved my family to San Leandro, CA]

(Pg 12) San Leandro borders Oakland, to the south. Oakland was nearly half black. San Leandro (on the other hand) was 99.99 percent white. Ninety-nine point ninety-nine percent! Ivory Soap looked at that number and went, “WOW!” (Pg 15) To this day, I don’t know how much my mother knew about San Leandro and its reputation when she moved us there. [The only reason we moved was to get away from Sylvester, my father.] (Pg 8) He was crazy. I never knew what he was going to say or do. He used to mess with my head.

SYLVESTER: Hey Brian, come here . . . . Knock, knock.

BRIAN: Who’s there?

SYLVESTER: (slapping Brian on the head violently) What did I tell you about answering the door when you don’t know who’s on the other side of it?

BRIAN: Once when I was five, I sniffed in a way that Sylvester thoughts was directed at him. He grabbed my nose and pinched it so hard that it was bruised for a month. (Pg 7) He was always doing things like that. [Anyway] (Pg 19) my mother moved us.

(Pg 95) My mother worked very hard at learning “the white man’s culture,” from her conversion to Catholicism (crosses himself) to her switch to the Republican party. She tried to assimilate in any and every way possible. Her philosophy was that while we may not look like them, we could act like them if that’s what it took to be accepted; if that was what we had to do to succeed.

(Pg 131) My childhood was a confusing barrage of mixed messages. On the one hand, Mom would say, “Be proud that you’re black, because black is beautiful. Then, when we acted up, she would say, “Act your age, not your color,” as if immaturity, rambunctiousness and negative behavior were “black” things. (beat as memories pour back in) (Pg 19) My mother moved us.

MOM: (Pg 20) It’ll be okay, honey. Remember you’re the man of the house now.

BRIAN: Maybe it would be okay. Sylvester wasn’t there . . . How bad could it be? [until he found us]

MOM: (Pg 171) Your father . . . He’s coming home.

BRIAN: (Pg 195-196) [I remember] (Voice shifts to that of a young boy as Brian re-lives the event in actions and words) I came home from school and the apartment appeared to be empty. Mom and Grandma must still be at work. That left the question, where was Sylvester? Actually, that was always the question. At that moment, a craving took over my body.

(opening the cabinet and getting a huge bowl and box of cereal) I wanted a great big salad bowl filled to the brim with Cap’n Crunch. Isn’t that the best after school snack in the world? It’s sweet and crunchy . . . What more can a kid ask for? (BUMP, BUMP) (Brian looks around perplexed) There it was again. (BUMP, BUMP) It was coming from my mother’s room. I took the stairs two at a time. (BUMP) I got to the doorway of my mother’s room and there I saw him. (Actor assumes the role of Sylvester who is repeatedly slamming mother’s head against the wall) (BUMP, BUMP, BUMP) (Brian reacts)

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

## IC-0417: On My Own

- Title: On My Own
- Author (byline): Mary Krell-Oishi
- Work: Perspectives: Relevant Scenes for Teens
- Publisher: Merriwether Publishing, Ltd
- Publication date as stated: March 1997
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NATHAN
- Teaser before the introduction: Yes
- Spoken words (computed): 2373
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mary Krell-Oishi
Book: Perspectives: Relevant Scenes for Teens
ISBN: 1566080304
Publisher: Merriwether Publishing, Ltd
Date(Month/Year): March 1997
```

### Introduction (context only: never use it for content warnings)

```text
On My Own by Mary Krell-Oishi
```

### Performance text (classify this)

```text
NATHAN: Today was the one-year anniversary of my dad's funeral. I loved him and I know he loved me. But I hardly knew him. I've been pretty much on my own since I was a kid. Not that I'm that old now, but I'm sure not a kid. Dad was a lawyer. Criminal defense. He was pretty good, I guess, because people were always calling the house to get him to defend their low-life relatives from some crime they were accused of. I couldn't understand how he could do that, but he said if we are to have justice in this country, then everyone has a right to a fair trial, both the guilty and the innocent. Yeah, I guess, but how fair is it when someone who is guilty walks free? He could never explain that part of it.

NATHAN: Dad was one of a kind. Really smart, star athlete, school government, everything I want to be, but doubt I will. My mom says I'm just as good as Dad. I guess so. Everything I know about my dad I learned from my mom. Dad was never one for talking. At least not to me. Oh, I always knew he loved me, but I wasn't sure he liked me. I feel kind of strange saying that, but that's how I feel. He was always in court or a law library or meeting with a client or something. I honestly don't remember him coming to a game or a concert or anything I did at school. Mom was always telling me that he wanted to be there, but work and all...1 don't know. It always seemed to me that if he really wanted to be there, he would. Mom came. Not all the time, but most of the time. She works, too. She teaches, so she's off during summer and vacations, but she always has papers to grade and tests to prepare and all that kind of stuff. She used to get mad at Dad sometimes, though, when I had a football game or something and he couldn't be there. One time I remember them arguing about it. But you know, it was really no big deal to me. I was used to him not being there, so you know, so what, right?

There was a time when I was little that I used to get mad about looking up into the stands at, say a Little League game. He, of course, would tell me he would try to be there. Like a jerk, I'd spend the whole game watching the stands instead of the field hoping I'd see him. One time - and this is really dumb - one time I looked up and I thought I saw him. I was so excited, you know? Then it was my turn to bat and I knew I was going to hit that ball out of the park. So I lined myself up at the plate, took my practice swing, and then waited. The pitcher threw the ball. Strike one! I wasn't worried. I knew I was going to nail the ball. The pitch and strike two! OK, now I started to get worried. I looked up and saw those sunglasses he always wore, shining there. I thought I heard him call out to me. I was so happy. I had to hit the ball out of the park for him, make him proud, make him want to come to all my games. I looked at that pitcher and inside I dared him to try to strike me out. Dared him! Well, he looked me dead in the eyes, wound up, and fired a pitch so fast all it was to me was a blur. I swung hard and heard a big "crack." I'll be damned if I didn't hit the hell out of the ball. I stood there and watched it go into this beautiful high arch and fly like it had wings right out of the field. I figured the only one more surprised and happier than me at that moment would be my dad. The coach yelled at me to circle the bases, and I did. You'll never have a greater feeling than running the bases after a home run! As I rounded third to home, I looked up and waved at my dad. But he wasn't watching me. He had taken off his glasses to clean them. That's when I saw it wasn't him. The only home run I ever hit and he wasn't there. He had promised that for sure, this time, he'd be at that game. But he wasn't. No one from my family was there. When I got home, Mom told me she had a student conference, and when Dad finally got home, at about nine o'clock, he apologized and said he had to meet with a client being held for murder. So it goes, right? I didn't even tell them about the home run. I mean, what was the point? It wasn't like they had planned to not be there just to make me unhappy. They both had to be at their jobs and that was important. That was the last year I played Little League. It just didn't seem all that important, you know?

I spent a lot of time playing really cool video games when I was home alone. I wasn't allowed to go outside or have anyone in the house if my parents weren't home. That was OK...I mean I understood it because they wanted me safe. But it was kind of a drag to have to come straight home from school and stay in the house until they got home. Everyone else would hang out at school and play basketball or something, but I had to be home. After awhile, though, that got old, so I started staying at school and hanging out with my friends until right before Mom would get home. See, school was out at two forty-five for me, and three o'clock for her. But she always had to stay after and work with kids. She was the on-site math tutor, so she never really left school until about four-thirty, then it took her about half an hour to get home, so I was on my own until five o'clock. I didn't do bad things. Can't do much bad in less than two hours. One time, though, my friends and I went to the mall and got our ears pierced. Neither of my parents noticed for about two weeks. By the time they did I just told them that I had done it months earlier and all the kids did it. What was cool was my dad noticed it first about eleven o'clock at night. He said something, then my mom came in and they had a discussion about it, but it was late and they were tired, so by the time they were done talking about it, they just told me it was my ear and I could do what I thought was right. The funny thing is, though, I was kind of hoping they'd get mad and tell me to take it out. My friend Glenn got his ear pierced that same day. He got home and his parents noticed it right away. Boy, were they mad. They grounded him for a week. I gave him a hard time about it. But you know what? I was jealous. I wished my parents had paid enough attention to get mad at me about it. Hell, I wish they had just noticed that I had done it. jeez, it sounds like my parents are bad. But they're not. Or weren't. Whoa, Dad's gone. Wow. Dad has passed away. He's not with us. Dad is dead. Anyway you say it doesn't make it better. He died really dumb, too. Not even something that he'd be proud he died of, like saving someone from a burning building or pushing a child out from in front of an oncoming car. Nope, he died choking. He was running late to an appointment with one of his criminals and stopped to get some chicken at a fast-food place. He did what he always did, which was eat in the car in the parking lot. He would never eat while he drove, because he said it was unsafe and he didn't want to cause an accident. But he choked on a chicken bone. And he was alone. Alone with a bone. I can almost guarantee you that his last thought wasn't of me and my mom. His last thought had to be, "Well, this is dumb."

So, Dad's been gone a year. In some ways I miss him. I don't miss money, because he had a great insurance plan and savings and stuff, so financially we're OK. And it's not like I miss him at the dinner table, because he was never really there for dinner. In fact, I don't think I can really remember ever sitting down and having dinner at an appointed time. Glenn gets in huge trouble if he's not home by six-thirty. Dinner is on the table and everyone better be there or there is hell to pay. I eat there a lot. It's gotten to be a kind of joke with his family, because they just automatically set a place for me at dinner. No, it's weird. I don't really miss my dad, because I was used to him never being around. When he was alive I could always have the hope that he would show up for a game. I could dream that some day he would put me first over one of the criminals and actually show up for something when he said he'd show up. When Dad was alive I could hope that some day, maybe some day, we'd sit down and have that father/son stuff going on. I figured it would probably happen when I grew up. But now it won't. I'm going to grow up and Dad won't be there. You know what's really scary, though? I can't remember what he looked like. Oh, we have pictures and stuff. But I look at them and I can't remember him being there in person. I look at those pictures and see a stranger.

I tried to talk to my mom about it all. Not easy. At first she was pretty shook up. But after a few months, she settled back into her job. She's working on her Ph.D. in education because she wants to be an administrator. I guess that's good. Whatever, huh? She's dating. My mom has dates. More dates than me. What does that tell you about my social life. What kind of bothers me, though, is that she can suddenly find the time to date, because before she and Dad couldn't find the time to be together as a family. Does anyone see the irony in that besides me?

So, like I said, I'm pretty much on my own. I have a car now, and Mom has let up on the be-home-no-one-in-the house stuff, which is good, because I wasn't doing it anyway. She never knew, so so what. So, I go to school, keep my grades up, and hang out at the mall with my friends and do sports. I think I've done a helluva job raising myself. I'm a good kid. But I feel lonely sometimes. I go home to our big old house and hear my footsteps echo on the stairs. I make myself dinner and do my homework. I'd play with a dog if I had one, but Dad was allergic and Mom said dogs were dirty, so I lost out there. I go out with my friends and try to beat Mom home. She has late-night classes at the university. And don't forget her dates. Anyway, I take care of me.

lt hasn't been all that easy being on my own, especially when you look around and see friends that have parents who are there for everything. But other people have it worse than me. At least my parents stayed together and tried to make sure I had everything I needed. But it would have been nice to have them there, you know?

So, Dad's been dead a year. I don't miss him, really. He wasn't around that much to miss. And I'm not mad at him. I mean, he worked hard to be a good lawyer and he had to work hard to stay at the top. What I miss is the idea of a dad. I go to the cemetery sometimes. To be honest, I go to the cemetery more than Mom. I sit by his grave and talk to him, tell him what's going on in my life. I ask for his advice and if I'm really quiet and listen really hard, sometimes I feel he answers me. I didn't feel this close to him when he was alive. One thing I remember, though, is when I'd be asleep. I was usually in bed before he got home from work. I remember hearing him open the door and I'd open my eyes so that he'd know I was still awake. I could see the light beam through the crack of the door. Then Dad would come in and sit on the bed for a minute and pat my back and mess up my hair. He'd say, "Good night, Natty." He never called me Nathan unless he was mad; it was always Natty. Hey, that was one really good thing about him not being around when my friends were around - they couldn't hear him call me Natty. Anyway, I remember his hand on my hair, and his good night and I would pat his leg and tell him I loved him. And now, sometimes when I talk to him at the cemetery, the wind will blow, just a little bit. Just enough to mess up my hair. If I really listen, 1 can hear him say, "Good night, Natty." I put my hand on his grave and I whisper, "I love you, Dad"
```

---

## IC-0418: Harrowdown Hill from Palace of the End

- Title: Harrowdown Hill from Palace of the End
- Author (byline): Judith Thompson
- Work: The Palace of the End
- Publisher: Playwrights Canada Press
- Publication date as stated: Nov 2009
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DAVID KELLY
- Teaser before the introduction: Yes
- Spoken words (computed): 1430
- Already set (do not supply): none

### Source block (context only)

```text
Author: Judith Thompson
Book: The Palace of the End
ISBN: 978-0887548352
Publisher: Playwrights Canada Press
Date (Month/Year): Nov 2009
```

### Introduction (context only: never use it for content warnings)

```text
In 2003, an inspection team led by David Kelly, one of the world's foremost experts on nuclear, chemical and biological weapons, conducted a thorough review of the military capacity of the sovereign nation of Iraq. He advised Prime Minister Tony Blair there were NO weapons of mass destruction in Iraq.

Despite this information, British Prime Minister Tony Blair declared that Iraq was a serious threat to national security and was capable of striking with weapons of mass destruction. Dr Kelly spoke with the press “off the record” to denounce this information as false, but the invasion of Iraq continued as planned in March of 2003.

On July 18, 2003, Dr. David Kelly was found dead on Harrowdown Hill, near his home in Oxfordshire. Suicide? Murder? We may never know the truth surrounding his death or if the threat of weapons of mass destruction really did justify military action against Iraq.

The fictionalized monologue Harrowdown Hill by Judith Thompson, gives voice to what may have been going through Dr. Kelly’s mind before his untimely death. Harrowdon Hill from The Palace of the End by Judith Thompson
```

### Performance text (classify this)

```text
DAVID KELLY: I’m beginning to think that it’s the greatest sin of our time. Knowing, and pretending that we don’t know so that we won’t be inconvenienced in any way. Do you understand what I am saying? I knew. Oh, the things I knew. And I did nothing.

DAVID KELLY: Can you imagine, knowing that a man is torturing a child in your basement, and just going on with your life? Knowing it is happening right under your feet, as you wait for the kettle to boil, as you tuck your own children in bed, as you work in the garden . . . the dim light is always there, the muffled sound of her screaming. You pretend to yourself, “It’s the crows on the line,” but in your belly you know it is her agony. He is cutting off her fingers one by one, pulling out her eyes, her teeth . . . unimaginable torture. And this is something you know for certain; others my guess at it, many deny it, but you know it for certain and you don’t tell anyone because you might lose something if you do. Your carefree life, your ability to be happy, your job. Your job. And if you lose your job, you lose your pension. And you don’t want to lose your pension. They said . . . they admitted they needed to sex it up, for the people – the people of Britain were not going to send their boys to a war they didn’t believe in. They would tie them down rather than see them go. They said we had to fill the people with fear, we had to remind them of WWII, they had to understand that the threat of Saddam was like the threat of the Nazis. We all knew that this was not true. We all knew that the casus belli was a lie. What could we do? We had no power. We just shook our heads and scurried away, little mouse men. We were not to talk; we had taken a vow of secrecy. If we wanted to hold onto our jobs, we had to keep our mouths shut. So. . . . I put my head in the sand.

I told myself . . “I am for the invasion. Saddam is a monster – no doubt about that. Regime change is a must. The people will dance in the streets, if only for a day.” I told myself: “They are good men, Bush and Blair, and Berlusconi. They want good for the people. They will topple Saddam, give aid to the new government and be on their way.”

I told myself lies. Have you ever? Have you ever told an unforgivable lie to yourself? (Long beat)

A few weeks before the invasion, a friend of mine, an American ambassador to Sweden asked me what would happen to me if Iraq were invaded. And do you know what I answered? I said I would probably be found dead in the woods. They’ll make much of that, after my death. It’ll be all over the Internet. And the funny thing is, I can’t explain it. I was making a kind of morbid joke. But maybe I knew something that I didn’t know I knew, you know?

At the start of the war I would wake up at six, watch the news every morning, from my bed. Each day’s smooth account of bombings and causalities, and “collateral damage.” I watched, hoping against hope that things would . . . would get better, but it soon became very clear to me that things were far, far, far worse for the Iraqi people than even I could have imagined.

What did I do? Did I go scream in the streets? Did I write to the papers? No. I did nothing. Nothing at all.

I became . . . clumsy. Yes, that was the only giveaway. I burned myself on the stove, I cut myself chopping onions, and I fell flat on my face on the pavement. I crashed into people in hallways, sat on my glasses, dropped the phone constantly, dropped and broke plates, couldn’t eat without dribbling, staining all of my shirts with food. I was in great demand. Flying to conferences all over the world. With stained shirts and broken glasses. The truth about Weapons of Mass Destruction – that’s what everyone wanted to know. I skirted the truth, bobbed and weaved, but I loved to hear my own voice -- loved to be regarded as the expert – the world expert – on biological weapons. Nominated for a Nobel Peace prize for my work in Russia ten years before: uncovering Stalinist secrets – disarming the next Black Plague and that is how they always introduced me. I talked to the press incessantly, my words always precise, witty – always filtered, always bloody lies. Walked through a screen door in Houston Texas, and feel into a river in Bern. Bit my tongue constantly. That was maybe the worst.

And then one day, one sunny June morning I was in New York City, just leaving the UN, I received a phone call from my dear old friend Jalal. He owned a bookstore in Baghdad, called in English, the Date Palm Tree. It was my favorite bookstore in the world, and I have been to almost all of them. No, I truly have! It’s what I do in my down time, wherever I am. Well, Jalal was one of the most kind and joyful and learned men I had ever known. Oh, you would live his family – Marwa, well, Marwa, and she wouldn’t mind me saying this at all, is sort of an Arabic Lucille Ball – she would turn the act of getting ice out of the fridge into this huge comic routine, have us all on the floor shouting with laughter. And their daughter, Sahar, I think she had just turned thirteen last time I saw them. She was obsessed with Anne of Green Gables. And Tabarek – the naughtiest five-year-old boy in the Universe, had to climb everything he say – tables, fridges, walls, people. I became . . . so . . . so close to this family. I loved that family – they became, in a way, my best friends in the world.

He said they were watching her. Sahar, his 13 year old. She was a very pretty girl, like a magazine model, I suppose, tall for her age, beautiful smile, a woman’s figure but still very much a little girl – a happy child who loved her stuffed animals. And he said the American soldiers were watching her. He said they looked at her like a wolf looks at a rabbit. They were ravenous. There was evil in their eyes, he said. Blood. He said he planned to move her the next day, to take her to another town, to stay with her cousins. He wanted to know if I could speak to someone. I said I was sorry, but there really wasn’t anyone I could speak to, even if they had been British. And then I reassured him. I told him not to worry; I said they were probably bored young hicks from Alabama who couldn’t put two words together. Intimidating young girls – their only entertainment. I reassured him that they were carefully monitored by their commanding officers, and they would never dare approach her.

“If you could only see their eyes,” he said. Even when he was with her, they would look her up and down, and say what were clearly crude things and laugh. She would go home and cry in her mother’s arms. I told him again not to worry. I was sure everything would be fine. Not two days later, according to the New York Times, four American soldiers confronted Jalal and his Sahar outside his bookstore. Took them inside. Said they were looking for weapons. For insurgents. “There are only books, please take all the books you want,” said Jalal, according to a witness. Once in the store they took Sahar aside. Rounded up Marwa and Tabarek, took the three of them into the basement. And shot them. The killer climbed the stairs and said, “I’ve killed them. They’re all dead.” And then the four soldiers threw Sahar to the floor, raped the child. Put a bayonet through the child and shot her in the fact.

They then set fire to the bookstore. (He is having rouble breathing) The press initially said it was the work of insurgents. “The terrorists.” Until two soldiers from the same battalion as the killers were captured and beheaded on camera. One of the four, tortured with guilt over his comrades deaths, certain it had been revenge for the murders, confessed.

Oh, the things I knew. And I did nothing.
```

---

## IC-0419: The Paper Menagerie

- Title: The Paper Menagerie
- Author (byline): Ken Liu
- Work: The Paper Menagerie and Other Stories
- Publisher: S&S/Saga Press
- Publication date as stated: Oct 2016
- Event as filed: Dramatic Interpretation
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

MOM: Just open it once in a while. Just open – (coughing spell) Haizi, mama ai ni

JACK: An image from years ago flashed into my memory: Mom saying ai and then putting her hand over her heart. (to Mom) It's okay, Mom. (stroking her arm awkwardly) Stop talking. (to audience) Dad came back, and I said that I needed to get to the airport early because I didn't want to miss my flight. (long beat) She died when my plane was somewhere over Nevada.

After [that], the paper animals did not move. Perhaps I had only imagined that [they] were once alive. The memory of children could not be trusted. (beat)

It was two years after Mom's death. I was home, flipping through the TV channels, [when I heard] a rustle. I looked up and saw a ball of wrapping paper and torn tape on the floor. I walked over to pick it up. The ball of paper shifted, unfurled itself, and I saw that it was Laohu, who I hadn't thought about in a very long time. "Raw-sa." Mom must have put him back together after I had given up. I reached out a finger. Laohu's tail twitched, and he pounced playfully. I laughed, stroking his back. "How've you been, old buddy?" Laohu stopped playing and proceeded to unfold himself. [There] in my [hand] was a square of creased wrapping paper, the plain side up. It was filled with dense Chinese characters in Mom's handwriting. The language that I had tried to forget for years came back, and I felt the words sinking through my skin until they squeezed tight around my heart.

MOM’S VOICE (as JACK reads silently): Son, We haven't talked in a long time. You are so angry when I try to touch you that I'm afraid. And I think maybe this pain I feel all the time now is something serious.

But if I write to you with all my heart, I'll leave a little of myself behind on this paper, in these words. Then the creatures I made for you will again leap and run and pounce, and maybe you'll get to see these words.

[When] you were born! I was so happy. When you said your first words to me, in Chinese I cried for hours. When I made the first zhezhi animals for you, and you laughed, I felt there were no worries in the world.

Son, I know that you do not like your Chinese eyes, which are my eyes. I know that you do not like your Chinese hair, which is my hair. But can you understand how much joy your very existence brought to me? Can you understand how it felt when you stopped talking to me and wouldn’t let me talk to you in Chinese? I felt I was losing everything all over again. You know what the Chinese think is the saddest feeling in the world? For a child to finally grow the desire to take care of his parents, only to realize that they [are] gone.

Why won't you talk to me, son?

JACK: (beat) [Her] pain makes it hard to bear. (beat) Following the creases, I refolded the paper back into Laohu. I cradled him in the crook of my arm, and as he purred, I traced out the character for ai on the paper, intertwining my pen strokes with her words.
```

---

## IC-0420: Past Wasn’t Done with Me

- Title: Past Wasn’t Done with Me
- Author (byline): Kemp Powers
- Work: The Moth: 50 True Stories, Pgs 335-342
- Publisher: Hachette Books
- Publication date as stated: Sept 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: KEMP
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
Past trauma has a way of refusing to stay buried --resurfacing when life cracks open just enough. And the truth is: surviving something doesn’t mean you’ve escaped it; in fact, healing often begins only when we stop running from what haunts us.

The Past Wasn’t Done with Me by Kemp Powers
```

### Performance text (classify this)

```text
KEMP: (Pgs 335-342) The first time that I passed out on the Chicago train, I knew I was dying from mad cow disease. At least that's what I told my doctor, and he was pretty impressed by the depths of my neurosis. But he assured me that I wasn't. I had anxiety. And he asked me if there was anything that had happened recently causing stress, and I had to think about the question.

I said, "My father's dying of cancer -- My daughter almost died last year from febrile seizures, and I'm pretty much terrified to be left alone with her." Now, this raised his eyebrows. He wrote me a prescription for Xanax and gave me the name of a therapist.

Now, I don't know what prompted me to say what I said next, but as he handed me the prescription, I blurted out: "There's one more thing: When I was 14 years old, I shot my best friend in the face accidentally, and I watched him die."

Henry was one of seven people to die that day in New York City, 1988. He wasn't even the youngest kid from Queens that had that dubious distinction. But his was the death that I saw with my own eyes. The one that I was responsible for with my own hands, and the one I'm going to carry with me for the rest of my life.

KEMP: Home back then was a 2-bedroom in Brooklyn. It was a big source of pride for my mom, who had raised my three older sisters and me since splitting from my dad when I was 4 years old. New York was really violent and dangerous back then. 2000-murders-a-year violent. But I never let the violence in the world impact me.

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

My marriage died, but I lived on. My daughter's 13 years old now and healthy. I have an 8- year-old son. I hope both grow up to be wonderful people -- the type who bring so much joy to everyone around them that their absence would be a tragedy, because that's the type of person that Henry was.

He died 24 years ago, and it's still fresh. But I'm no longer miserable. In fact, I am well on my way to becoming one of the happiest people I know, and I think that fact would've made him happy. He also doesn't visit me in my dreams anymore, and I can finally admit that I'm comfortable with never seeing his face ever again, in my dreams or otherwise. Because at the end of the day, what would a man like me have to say to his 14-year-old friend that hasn't been said already?
```

---

## IC-0421: Perfect Moments

- Title: Perfect Moments
- Author (byline): Brian Finkelstein
- Work: The Moth, Pg 373-384
- Publisher: Hachette Books
- Publication date as stated: Sept 2013
- Event as filed: Dramatic Interpretation
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

## IC-0422: The Pillowman

- Title: The Pillowman
- Author (byline): Martin McDonagh
- Work: Not specified
- Publisher: Faber and Faber
- Publication date as stated: Sept 2004
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: TUPOLSKI, KATURIAN, MICHAL, MICHAEL
- Teaser before the introduction: Yes
- Spoken words (computed): 2669
- Already set (do not supply): none

### Source block (context only)

```text
Author: Martin McDonagh
ISBN: 978-0571220328
Publisher: Faber and Faber
Date (Month/Year): Sept 2004
```

### Introduction (context only: never use it for content warnings)

```text
In The Pillowman by Martin McDonagh, a writer is interrogated about the gruesome content of his short stories and their similarities to a number of child-murders that are happening in his town. He learns that his older brother, Michal, is also being held and questioned in another cell. Michal, who has the mind of a child. Michal, who our author, Katurian, has raised ever since the death of their parents.

The Pillowman by Martin McDonagh
```

### Performance text (classify this)

```text
PAGE 25 - 30

TUPOLSKI: What happened to the third child? Andrea Jovacovic. You know who she was?

KATURIAN: (pause) Only from the papers. She was the girl they found on the heath.

TUPOLSKI: She was the girl they found on the heath, yes. You know how she died?

KATURIAN: No. The papers didn’t say.

TUPOLSKI: You know who Aaron Goldberg was? He was the boy they found in the dump behind the Jewish quarter. You know how he died?

KATURIAN: No. The papers didn’t say.

TUPOLSKI: (mocking) No, the papers didn’t say. They papers didn’t say a lot of things. The papers didn’t say anything about the third child, a little mute girl, went missing three days ago, the same area, the same age.

KATURIAN: What did my brother say to you? Whatever he said, you made him say. He doesn’t speak to strangers. I want to see him. I’ve got a right to see my brother! (crying) I just write stories! I don’t understand a thing of what’s going on!

TUPOLSKI: No? Well, here’s where we stand. Along with the evidence we found in your house, your brother has, under duress or not, admitted enough about the killings for us to execute him before the evening’s out. But, he’s hardly the brains behind the operation, so we want you to confess too. We like executing writers. Dimwits we can execute any day. And we do. But, you execute a writer, it sends out a signal, y’know? (Pause) It sends out the signal ‘DON’T . . . GO . . AROUND . . . KILLING . . . LITTLE . . . KIDS.’ (Pause) Where’s the mute girl?

KATURIAN: (pause) I’ve listened to your bullshit for a long time now, and I want to tell you a couple of things. . . I don’t believe my brother said a word to you. I believe that you are trying to frame us for two reasons. One, because you don’t like the kind of stories I write, and two, because you don’t like retarded people cluttering up your streets.

PAGE 36 – 67 A cell. Michal is listening to the intermittent screams of his brother, Katurian, being tortured a room away. Michal mimics them till they fade way. Michal’s cell is unbolted and the bloody, breathless Katurian is thrown in. Michal looks over Katurian, who is shivering on the floor, goes to caress his head, can’t quite do it.

MICHAL: Hiya. You were making some racket. What were they doing, torturing ya?

KATURIAN: Did yours hurt? When they tortured you?

MICHAL: They didn’t torture me. (Katurian looks him over for the first time, seeing there are no cuts or bruises) Oh, no, the man said he was going to torture me, but I thought, ‘No way, boy, that’d hurt,’ so I just told him whatever he wanted to hear, and he was fine then.

KATURIAN: (pause) Swear to me on your life that you didn’t kill those three kids.

MICHAL: I swear to you on my life that I didn’t kill those three kids. (Katurian breathes a sign of relief)

KATURIAN: The only thing they’ve got against us is what you’ve said, and the stuff they said they found in the house. Oh my God. Whatever they do, Michal, no matter what, you don’t sign anything. You got it?

MICHAL: Whatever they do to me, I don’t sign anything. (Pause) Can I sign your name?

KATURIAN: Especially don’t sign my name.

MICHAL: ‘I killed a loda kids,’ signed Katurian Katurian. Hah! ‘And it was nothing to do with his brother, Michal, not even a bit,’ Hah!

KATURIAN: (Pause) We’ll be alright, Michal. We’ll be alright. We’ll get out of here. If we just stick together.

MICHAL: Tell us a story, Katurian. It’ll take my mind off . . .

KATURIAN: What story do you want?

MICHAL: Do ‘The Pillowman’.

KATURIAN: (Pause) Once upon a time . . . there was a man, who did not look like normal men. He was about nine feet tall . . . (Michal looks up, silently whistles) And he was all made up of these fluffy pink pillows: Even his head was a pillow, a big round pillow.

MICHAL: A circular pillow – I prefer ‘ a circular pillow’.

KATURIAN: His head was a circular pillow. And on his head he had two button eyes and a big smiley mouth.

MICHAL: Do your mouth smiley like the Pillowman’s mouth is. (Katurian gives a big dopey smile)

KATURIAN: Well, the Pillowman had to look like this, he had to look soft and safe, because of his job, because his job was a very sad and a very difficult one . .

MICHAL: Uh-oh, here it comes . . .

KATURIAN: Whenever a man or a lady was very very sad because they’d had a dreadful and hard life and they just wanted to take their own lives by razor, or by bullet, or by gas, or . . .

MICHAL: Or by jumping off of something big.

KATURIAN: Yes. Just as that person was about to do it, the Pillowman would go to them, and sit with them, and gently hold them, and he’d say, ‘Hold on a minute,’ and time would slow strangely. The Pillowman would go back in time to when that man or that lady was just a little boy or a little girl, to when the life of horror they were to lead hadn’t quite yet begun, and the Pillowman’s job was very very sad, because the Pillowman’s job was to get that child to kill themselves.

MICHAL: Um, could you skip on to the end, please? This bit’s a bit boring.

KATURIAN: Well, that’s a bit rude, Michal, actually. MICHAL; Oh, Sorry, Katurian. (Pause) But could you skip on to the end, please?

KATURIAN: (Pause) Well . . . the end of the Pillowman . . . See, when the Pillowman was successful in his work, a little child would die. And when the Pillowman was unsuccessful, a little child would have a horrific life, grow into an adult who’d also have a horrific life, and then die horrifically. He decided to do just one final job and that’d be it. So he went to this place beside this pretty stream that he remembered from a time before . . .

MICHAL: I like this bit . . .

KATURIAN: And he brought a little can of petrol with him, and he sat and he waited there a while. There was a little caravan nearby, and the Pillowman heard the door open and little footsteps come out. It was a little Pillowboy. And the Pillowman told him all about his sad job and the dead kids and all that type of stuff. And the little Pillowboy understood instantly, and he poured the can of petrol all over himself. And the Pillowboy struck a match, and the Pillowman sat there watching him burn. And as the Pillowman gently started to fade away, the last thing he saw was the Pillowboy’s happy smiley mouth as it slowly melted away. The last thing he heard was the screams of the hundred thousand children he’d helped to commit suicide coming back to life and going on to lead the cold, wretched lives that were destined to them because he hadn’t been around to prevent them.

MICHAL: (Pause) So the Pillowman just faded away? Ah.

KATURIAN: Into the air. Into Heaven.

MICHAL: I like the Pillomwman. He’s my favourite. (Thinking) Hmmm. I still can’t figure it out.

KATURIAN: Figure what out? Figure out ‘The Pillowman’?

MICHAL: No, I thought I’d hidden it really well.

KATURIAN: Hidden what really well?

MICHAEL: The box with the little boy’s toes in it. They must’ve used sniffer dogs or something. Because, no, way, I hid them brilliant. Christmas tree pot. You only see it once a year.

KATURIAN: You just told me you didn’t touch those kids. You just lied to me.

MICHAL: No I didn’t. I just told you the man came in and said he’d torture me unless I said I killed those kids, so I said I killed those kids. That don’t mean I didn’t kill those kids. I did kill those kids.

KATURIAN: You swore to me, on your life, that you didn’t kill those three kids.

MICHAL: Ohhh. See with that one, yeah, I was kind of playing a trick on ya. Sorry, Katurian. I know it was wrong. Really, But it was very interesting. The little boy was just like you said it’d be [in your story, The Tale of the Town on the River] I chopped his toes off and he didn’t scream at all. His name was Aaron. God, he bled a lot. You wouldn’t’ve thought there’d be that much blood in such a little boy. Then he stopped bleeding and went blue. I feel quite bad now, he seemed quite nice. But the girl was a pain in the *ass*. Kept bawling her eyes out. And she wouldn’t eat them. She wouldn’t eat the applemen, and I’d spent ages making them. It’s really hard to get the razor blades inside. You don’t say how to make them in [that] story, do ya? I checked. So, anyway, I had to force ‘em down her. It only took two. Not being mean, but at least that shut her up.

KATURIAN: (Realization has finally dawned –quietly) What did you do it for?

MICHAL: Don’t cry, Katurian. Don’t cry. You know. Because you told me to.

KATURIAN: (pause) I remember telling to your do your homework on time. I remember telling you to brush your teeth every night . . . I don’t remember telling you to take a bunch of little kids and go butcher them!

MICHAL: I didn’t butcher them. .”Butcher them’ it’d be more like . . . (Michal imitates viciously hacking at someone.) Mine was more like . . . (Michael imitates a gentle, single hack onto imaginary toes, then delicately throwing the tows away.) And . . . (Michal imitates placing two applemen inside a little mouth, then swallowing) And I wouldn’t have done anything if you hadn’t told me, so don’t you act all the innocent. Every story you tell me, something horrible happens to somebody. I was just testing out how far-fetched they were. (Pause) D’you know what? They ain’t all that far-fetched.

KATURIAN: You’re a sadistic, retarded pervert who enjoys killing little kids!

MICHAL: (Pause) I didn’t enjoy killing those kids. It was irritating. It took ages. And I didn’t set out to kill those kids. I just set out to chop the toes off one of them and to put razors down the throat of one of them.

KATURIAN: Are you telling me you don’t know that if you chop the toes off a little boy and put razors down the throat of a little girl, you don’t know that they’re gonna die?

MICHAL: Well, I know now! (Katurian puts his head in his hands, trying to think of a way out of this). Well, the torture man certainly seemed to be on my side. He seemed to agree it was all your fault. [That] all the things I did to all the kids I got from stories you wrote and read out to me.

KATURIAN: That isn’t the truth, Michal.

MICHAL: Yes it is. Did you write some stories with children getting murdered in them?

KATURIAN: Yes, but . . .

MICHAL: Well, did you read them out to me?

KATURIAN: Yes . . .

MICHAL: Well, did I go out and murder a bunch of children? (Pause) ‘Yes, I did,’ is the answer to that one. So I don’t see how the ‘That isn’t the truth’ comes into it. I mean, you’re my brother and I love you, but y’know, you’ve just [been] telling me a story about a bloke, his main thing in life’s is to get a bunch of little kids to set themselves on fire, so y’know? And he’s the hero! I’m not criticizing. He’s a very good character. He reminds me a lot of me – You know, getting little children to die. All that.

KATURIAN: The Pillowman never killed anybody, Michal. And all the children that died were going to lead horrible lives anyway.

MICHAL: You’re right, all children are going to lead horrible lives. You may as well save them the hassle.

KATURIAN: Not all children are going to lead horrible lives.

MICHAL: Erm, hmmm. Did you lead a horrible life since you was a child? Yes. Erm, did I lead a horrible life since I was a child. Yes. That’s two out of two for a start.

KATURIAN: They’re going to execute us in an hour and a half. They’re going to destroy us, they’re going to destroy my stories.

MICHAL: Well, I think it’s us we should be worrying about, Katurian, not your stories. They’re just paper.

KATURIAN: (barely containing he anger) If they came to me right now and said, “We’re going to burn two out of the three of you, you, your brother, or your stories,’ I’d have them burn you first, I’d have them burn me second, and I’d have it be the stories they saved.

MICHAL: You’re just like Mum and Dad!

KATURIAN: (Laughing) I’m just like Mum and Dad? Let me work this out . . . Mum and Dad kept their first-born son in a room where they tortured him for seven straight years, and you made a little boy bleed to death, made a little girl choke to death, and God knows what to another little girl and you’re not like Mum and Dad?

MICHAL: I’m not like them. I didn’t want to hurt anybody. I was just doing your stories.

KATURIAN: What did you do to the third girl?

MICHAL: (long pause) When I was in here listening to you screaming next door, I thought this musta been kinda like how it was for you all those years. Well, let me tell ya, it’s easier from this side.

KATURIAN: I know it is.

MICHAL: You only had it for an hour and you came in *whining* your snotty head off. Try it for a lifetime.

KATURIAN: That doesn’t excuse anything.

MICHAL: It excused the two you murdered. Why shouldn’t it excuse the two I murdered?

KATURIAN: I murdered two people who tortured a child for seven years. You murdered three children who hadn’t tortured anybody for any years. There’s a difference. . . How did you kill the third girl, Michal? I just need to know. Was she like in a story too? Which story was she like?

MICHAL: You’re gonna be mad. Like, um . . . she was like in um . . . ‘The Little Jesus’. ‘The Little Jesus’. (Katurian looks at Michael, hands to his face and, as he pictures the horrific details of the story, he slowly starts to cry.) Will they execute us together or separate? I hope it’s together. I wouldn’t wanna be on my own.

KATURIAN: I haven’t done anything!

MICHAEL: At least we’ll be together in Heaven, whatever happens. And hang out with God.

KATURIAN: Which particular Heaven is this you’re going to Michal? Child-killer Heaven? Do you want to know where you’re going when you die? You’re going to go to a little room in a little house in a little forest, and for the rest of all time you’re going to be looked after not by me, but by a person called Mum and a person called Dad, and they’re gonna look after you in the same way they always looked after you, except this time I’m not gonna be around to rescue you, ‘cos I ain’t going to the same place you’re going, ‘cos I never butchered any little kids . . .

MICHAL: That is just the most meanest thing that any person has ever said to any other person.

KATURIAN: I used to love you so much.

MICHAL: (pause) What do you mean, ‘used to’? (Long silence)

KATURIAN: Right at this moment, I don’t care if they kill me. I don’t care. But they’re not going to kill my stories. They’re all I’ve got. The three stories you chose to act out just happened to be the three most repulsive stories you could’ve chosen to act out. They weren’t the first three you happened to come across, they were the three that most suited your repulsive little mind.

MICHAL: So, what, I could’ve done ones that wouldn’t’ve been so horrible? Like what? Like ‘The Face Basement’? Slice off their face, keep it in a jar on top of a dummy, downstairs? They’re all sick. You couldn’t’ve picked one that wouldn’t’ve been just as sick.

KATURIAN: Why did it have to be ‘The Little Jesus’, though?

MICHAL: Tell me a story. Tell me the one about the little green pig.

KATURIAN: (pause) I can’t remember how it goes, ‘The Little Green Pig’ . . .

(remembering) Okay. Settle down (Michael does so with a pillow beside his head) Once upon a time, on a farm in a strange land far way. . .

MICHAL: Far away . . .

KATURIAN: There lived a little pig who was different from all the other pigs around.

MICHAL: He was green.

KATURIAN: Are you telling this story or am I? Are we interrupting or are we listening and sleeping?

MICHAL: You. Sorry. Fingers on lips. Shhh. Listening and sleeping.

KATURIAN: Good. (pantomimes telling the rest of the story as Michael falls asleep. Katurian looks at Michael and realizes he is asleep – and finishes the story in a whisper) . . . he knew that he was still, and he always would be, just a little bit peculiar . . . (Pause) You like that one, don’t you Michal? You used to like that one. No little toes in it . . . no razor blades in it. (Pause) It’s not your fault, Michal. (Crying) I’ll be coming along soon. (Katurian takes the pillow and holds it down forcefully over Michal’s face. Michal starts to jerk. After a minute Michal’s jerks lessen. He’s dead. Katurian takes the pillow off, kisses Michal, crying , he closes Michal’s eyes. He goes to the door, clangs it loudly) Detective?! (Pause) Detective?! I would like to make a confession to my part in the murders of six people. (Pause) I have one condition. (Pause) It involves my stories . . .
```

---

## IC-0423: Pin

- Title: Pin
- Author (byline): Robert McCammon
- Work: Blue World (Pg 93-99)
- Publisher: Pocket
- Publication date as stated: April 1990
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JOEY
- Teaser before the introduction: Yes
- Spoken words (computed): 1615
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

Our young people are at risk. The result? Suicide and homicide are at the highest rates in
```

### Performance text (classify this)

```text
JOEY: (Pg 93-99) I’m going to do it. Yes. I am. I hold the pin in my hand, and tonight I’m going to peer into the inner sun. Then, when I’m filled up with all that glare and heat and my brain is on fire like a four-alarm blaze, I’m going to take my Winchester rifle down to the McDonald’s on the corner and we’ll see who says what to who when.

decades (CDC, June 15, 2023) https://www.cnn.com/2023/06/15/health/youth-suicide-homicide/index.html And mass shootings? Most of the deadliest in the U.S. since 2018 were committed by those 21 or younger. (https://www.axios.com/2022/06/02/mass-shooting-killers-young-teens) But statistics are easy to brush aside. Let me bring the issue of childhood trauma and its aftermath to you in a more compelling way. . . Meet Joey Shatterly a mentally ill young man who struggles with the compelling urge to inflict harm on others or himself.

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

(Sniffs under his arms) Ban roll-on. You don’t want to smell when they turn the lights on you. Oh hell, I’m out of Ban. Old Spice that’ll do. My dad used to use Old Spice.. Now, that was a good day, when we saw the Reds play the Pirates and he bought me a bag of peanuts and said he was proud of me. That was a good day.

He was a Marine. I remember that Iwo Jima crap when he got crazy and drank all the time - - Iwo Jima Iwo Jima -- he lived it in his mind a million times. You got sick of hearing who all died at Iwo Jima and how come you ought to be proud to be an American and how things weren’t how they used to be. Nothing is, is it? Except Old Spice. Iwo Jima Iwo Jima. And then he went and did it, put the rope up in the garage and stepped off the ladder and me coming in to get my bike and that grin on his face that said Iwo Jima.

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

## IC-0424: Placebo

- Title: Placebo
- Author (byline): Andrew Vachss (pronounced like “fox”)
- Work: Plays in One Act, ed. Daniel Halpern
- Publisher: Ecco Press
- Publication date as stated: Dec 2005
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: THE REPAIRMAN
- Teaser before the introduction: No
- Spoken words (computed): 1629
- Already set (do not supply): none

### Source block (context only)

```text
Author: Andrew Vachss
Book: Plays in One Act, ed. Daniel Halpern
ISBN: 978-0880014908
Publisher: Ecco Press
Date (Month/Year): Dec 2005
```

### Introduction (context only: never use it for content warnings)

```text
A placebo is fine while you believe. But when the believing stops, you need a good friend to take up the slack. The Repairman has become a good friend to Mrs. Barnes’ 10-year old son Tommy, who goes to a special school run by Dr. English, and he makes a machine that helps overcome Tommy’s nightmares. However, there comes a day when the machine is no longer effective. The Repairman loves Tommy and determines that his problems originate at the school. This play is about his determination to solve Tommy’s problems and the solution at which he finally arrives. Placebo by Andrew Vachss
```

### Performance text (classify this)

```text
THE REPAIRMAN: I know how to fix things. I know how they work. When they don't work like they're supposed to, I know how to make them right. I don't always get it right the first time, but I keep working until I do.

I've been a lot of places. Some of them pretty bad-some of them where I didn't want to be. I did a lot of things in my life in some of those places. In the bad places, I did some bad things. I paid a lot for what I know, but I don't talk about it. Talking doesn't get things fixed.

People call me a lot of different things now. Janitor. Custodian. Repairman. Lots of names for the same thing. I live in the basement. I take care of the whole building. Something gets broke, they call me. I'm always here.

I live by myself. A dog lives with me. A big Doberman. I heard a noise behind my building one night-it sounded like a kid crying. I found the Doberman. He was a puppy then. Some freak was carving him up for the fun of it. Blood all over the place. I took care of the freak; then I brought the puppy down to my basement and fixed him up. I know all about knife wounds. The freak cut his throat pretty deep. When the stitches came out, he was okay, but he can't bark. He still works, though.

I don't mix much with the people. They pay me to fix things-I fix things. I don't try and fix things for the whole world. I don't care about the whole world. Just what's mine. I just care about doing my work.

People ask me to fix all kinds of things-not just the boiler or a stopped-up toilet. One of the gangs in the neighborhood used to hang out in front of my building, give the people a hard time, scare them, break into the mailboxes, petty stuff like that. I went upstairs and talked to the gang. I had the dog with me. The gang went away. I don't know where they went. It doesn't matter.

Mrs. Barnes lives in the building. She has a kid, Tommy. He's a sweet-natured boy, maybe ten years old. Tommy's a little slow in the head, goes to a special school and all. Other kids in the building used to bother him. I fixed that. Maybe that's why Mrs. Barnes told me about the monsters. Tommy was waking up in the night screaming. He told his mother monsters lived in the room and they came after him when he went to sleep. I told her she should talk to someone who knows how to fix what's wrong with the kid. She told me he had somebody. A therapist at his special school-an older guy. Dr. English. Mrs. Barnes couldn't say enough about this guy. He was like a father to the boy, she said. Took him places, bought him stuff. A real distinguished-looking man. She showed me a picture of him standing next to Tommy. He had his hand on the boy's shoulder.

The boy comes down to the basement himself. Mostly after school. The dog likes him. Tommy watches me do my work. Never says much, just pats the dog and hands me a tool once in a while. One day he told me about the monsters himself. Asked me to fix it. I thought about it. Finally I told him I could do it. I went up to his room. Nice big room, painted a pretty blue color. Faces out the back of the building. Lots of light comes in his window. There's a fire escape right off the window. Tommy tells me he likes to sit out there on nice days and watch the other kids play down below It's only on the second floor, so he can see them good.

I checked the room for monsters. He told me they only came at night. I told him I could fix it but it would take me a few days. The boy was real happy. You could see it. I did some reading, and I thought I had it all figured out. The monsters were in his head. I made a machine in the basement-just a metal box with a row of lights on the top and a toggle switch. I showed him how to turn it on. The lights flashed in a random sequence. The boy stared at it for a long time. I told him this was a machine for monsters. As long as the machine was turned on, monsters couldn't come in his room. I never saw a kid smile like he did. His mother tried to slip me a few bucks when I was leaving. I didn't take it. I never do. Fixing things is my job. She winked at me, said she'd tell Dr. English about my machine. Maybe he'd use it for all his kids. I told her I only fixed things in my building.

I saw the boy every day after that. He stopped being scared. His mother told me she had a talk with Dr. English. He told her the machine I made was a placebo, and Tommy would always need therapy. I go to the library a lot to learn more about how things work. I looked up "placebo" in the big dictionary they have there. It means a fake, but a fake that somebody believes in. Like giving a sugar pill to a guy in a lot of pain and telling him it's morphine. It doesn't really work by itself-it's all in your mind.

One night Tommy woke up screaming and he didn't stop. His mother rang my buzzer and I went up to the apartment. The kid was shaking all over, covered with sweat. He saw me. He said my machine didn't work anymore. He wasn't mad at me, but he said he couldn't go back to sleep. Ever. Some guys in white jackets came in an ambulance. They took the boy away. I saw him in the hospital the next clay. They gave him some-thing to sleep the night before and he looked dopey.

The day after that he said he wasn't afraid anymore. The pills worked. No monsters came in the night. But he said he could never go home. He asked if I could build him a stronger machine. I told him I'd work on it. His mother said she called Dr. English at the special school, but they said he was out for a few clays. Hurt himself on a ski trip or something. She couldn't wait to tell Dr. English about the special medicine they were giving the boy and ask if it was all right with him.

I called the school. Said I was with the State Disability Commission. The lady who answered told me Dr. English was at home, recuperating from a broken arm. I got her to tell me his full name, got her to talk. I know how things work. She told me they were lucky to have Dr. English. He used to work at some school way up north-in Toronto, Canada-but he left because he hated the cold weather. I thought about it a long time. Broken arm. Ski trip. Cold weather.

The librarian knows me. She says I'm her best customer because I never check books out. I always read them right there. I never write stuff down-I keep it in my head. I asked the librarian some questions, and she showed me how to use the newspaper index. I checked all the Toronto papers until I found it. A big scandal at a special school for slow kids. Some of the staff were indicted. Dr. English was one of the people they questioned, but he was never charged with anything. Four of the staff people went to prison. A few more were acquitted. Dr. English, he resigned.

Dr. English was listed in the phonebook. He lives in a real nice neighborhood. I waited a couple of more days, working it all out in my head. Mrs. Barnes told me Dr. English was coming back to the school next week. She was going to talk to him about Tommy, maybe get him to do some of his therapy in the hospital until the boy was ready to come home.

I told Tommy I knew how to stop the monsters for sure now. I told him I was building a new machine-I'd have it ready for him next week. I told him when he got home I wanted him to walk the dog for me. Out in the back where the other kids played. I told him I'd teach him how. Tommy really liked that. He said he'd try and come home if I was sure the new machine would work. I gave him my word.

I'm working on the new machine in my basement now. I put a hard rubber ball into a vise and clamped it tight. I drilled a tiny hole right through the center. Then I threaded it with a strand of piano wire until about six inches poked through the end. I knotted it real carefully and pulled back against the knot with all my strength. It held. I did the same thing with another ball the same way. Now I have a three-foot piece of piano wire anchored with a little rubber ball at each end. The rubber balls fit perfectly, one in each hand.

I know how to fix things. When it gets dark tonight, I'll show Dr. English a machine that works.
```

---

## IC-0425: Prayer for What

- Title: Prayer for What
- Author (byline): Robert C. Reinhart
- Work: Telling Moments
- Publisher: Applause Theatre Books
- Publication date as stated: 1994
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1326
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert C. Reinhart
Book: Telling Moments
ISBN: 1557831637
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

## IC-0426: Prodigal Son

- Title: Prodigal Son
- Author (byline): Garrison Keillor
- Work: Not specified
- Publisher: Ecco Press
- Publication date as stated: Nov 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DAD, DWIGHT, WALLY, NARRATOR, WISE, BIMBO, PUBLICAN, FARMER
- Teaser before the introduction: No
- Spoken words (computed): 1544
- Already set (do not supply): none

### Source block (context only)

```text
Author: Garrison Keillor
ISBN: 0880014903
Publisher: Ecco Press
Date(Month/Year): Nov 1999
```

### Introduction (context only: never use it for content warnings)

```text
A happy day, a sunny street, you're young and in love and life is good and you're on your way to lunch, when suddenly a cold shadow falls and (Loathsome laugh.) you feel a cold slimy hand touch your face. (Worse laugh.) And it's your own hand. (Worst laugh.) That's evil. Where does evil come from? Whose fault is it? The American Council of Remorse-a nonprofit organization working for greater contrition on the part of people who do terrible things brings you: The Prodigal Son by Garrison Keillor
```

### Performance text (classify this)

```text
DAD: I run a feed-lot operation here in Judea, fattening feeder calves for the Jerusalem market, in partnership with my two sons: my prodigal son, WALLY, and my older son, DWIGHT. One morning about two years ago, I came down to breakfast and-no WALLY. Morning, DWIGHT.

DWIGHT: (Sitting at table, reading newspaper.) Morning.

DAD: You see your brother this morning?

DWIGHT: In bed.

DAD: I promised Harry Shepherd I'd be over to his place by seven-thirty. He's got a lost sheep out on the mountain wild and steep.

DWIGHT: Says here that fatted calves are down one and three-quarter shekels on the Damascus market, DAD. Makes me wonder if maybe lean calves wouldn't have a higher profit margin, and then we could spend more time in the vineyard- DAD, are you listening to me?

DAD: I'm worried about your brother.

DWIGHT: We can't afford to stand still, DAD. Look at the Stewarts they're buying up land left and right! You've got to move ahead or you lose ground. . . .

WALLY: (Thickly.) Morning, DAD. Morning, DWIGHT. (He sits down, groans, puts his head in his hands.)

DAD: You look a little peaked, son.

WALLY: I donno-it's some kind of morning sickness, DAD. I feel real good at night and then I wake up and hurt all over.

DWIGHT: I noticed a couple empty wineskins behind the fig tree this mormng.

WALLY: I dropped them and they spilled! Honest!

DAD: Where were you taking them?

WALLY: I was putting them outside! Wine's got to breathe, you know. And so do I, DAD. I've got a real breathing problem here. I'm worried about my health, DAD. I read an article the other day in Assyrian Digest that says bad feelings may be environmental. I donno. Maybe I need to get away for a while, DAD. Get my head straight. Work out some things.

DAD: Well, if that's how you feel, I guess I . . .

WALLY: I was thinking I'd sort of take my share of the farm and head for a far country for a while until I get back on my feet, headwise, and then come back a brand-new guy.

DWIGHT: DAD, could we discuss this?

NARRATOR: And not many days after, the younger son gathered his inheritance together, and took his journey into a far country. . . .

WALLY: (Walking.)
I'm walkin' . . . to a far-out land.
I'm talkin' . . . got cash in hand.
I'm hot now. . . don't you understand.
You're lookin' at a brand-new man. (FOOLISH VIRGINS enter,
harnessed together, led by a WISE VIRGIN.)
Hey! Who's this? Hey. What's shakin', babes?

WISE: I'm taking these five foolish virgins home, mister. We were supposed to be at a wedding an hour ago, but they're low on oil. You see an oil station that way?

WALLY: Hey, they don't look foolish to me. They look like kinda fun people. Tell you what, they can come with me. I'll buy them oil. My treat.

WISE: Sorry, mister. I've got to look after these virgins myself. They take a lot of supervision. You gotta watch 'em pretty close so they don't bunch up and walk up each other's backs. (Crash.)

WALLY: Whoops-dropped your lamp, huh? Good thing it didn't have oil in it.
Well, 'bye! Don't do anything I wouldn't do.
We're movin' . . . down the ole highway.
We're improvin' . . . every day.
We're groovin' . . . and we're okay.

NARRATOR: And he took his journey into a far country, and there wasted his substance in riotous living. . . . (Enter LOOSE COMPANIONS, dancing, drinking, feasting, whooping. BIMBO on WALLY'S arm.)

WALLY: Take it off! Take it all off! Go for it! Put it on and take it off again! (To audience.) Hey, you Pharisees, loosen up

BIMBO: You're such a wonderful, vital person.

WALLY: (To "Hey Jude. ")
Hey, Judea-you're a real great place.
You're the best spot in the Bi-i-i-ible. . . .
You're right there by Canaan and Galilee,
You're family, you're tribal.
Hey, PUBLICAN! Another round of wine for my pals! Put it on my tab!
Phhhh! Blaaaaghhhhh! What is this??? Lite wine?

PUBLICAN: You don't like it?

WALLY: Give it to some virgins-and bring me your best.

PUBLICAN: I'll give you a jar to take with you-it's closing time. Time to lock up, Mr. WALLY.

WALLY: Hey! I'll pay. Let's party!

BIMBO: Oh, WALLY! You're so joyful! So many persons with a farm back ground, they don't know how to let go and have a good time.

WALLY: Not me, Wanda! Life is a feast if you know where to find it.

PUBLICAN: Here's your bill, Mr. WALLY.

BIMBO: That's so beautiful: "Life is a feast." So many people-they place such restrictions on themselves. (He reads bill, page after page, then searches his pockets and brings out a few coins.) You have a better sense of who you are. You have that rare quality of trusting yourself. Believing in festivity, not negativity. In a smile, not denial. Sure, rules are good for people who need 'em. But you prefer freedom. You have this tremendous-this great- It's not a structured thing. You know? Your energy is so focused. Like a locust.

WALLY: That's the last of my money. That's all I have left. Amazing.

PUBLICAN: You all right? You need a ride home?

WALLY: No.

BIMBO: WALLY-listen. It's been great. Three of the best weeks of my life. Bye. (The BIMBO, the PUBLICAN, and the LOOSE COMPANIONS leave, one by one.)

NARRATOR: And when he had spent all, there arose across a mighty famine in that land, and he began to be in want. And he went and lived with a FARMER who sent him into his fields to feed swine.

FARMER: You ever feed swine before?

WALLY: No, but I fed calves. You just dump the husks and swill down in front of them, right?

FARMER: Lot more to it than that. Usually we require swine feeders to have at least four years of professional experience. But tell you what-I'll put you in my internship program.

WALLY: What does it pay?

FARMER: Pay! I'm offering you a chance to learn the swine business from the mud up.

WALLY: SO, you mean I'll sleep out here and eat with the pigs?

FARMER: You want it or not?

WALLY: Fine. Just want to get it clear in my own mind, that's all. C'mon, hogs. Sooo-eyyy! C'mon. C'mon, piggy, piggy, piggy.

NARRATOR: And when he came to himself, he said:

WALLY: How many hired servants of my father's have bread enough and to spare, and I perish with hunger! I will arise and go to my father, and will say unto him: "Father, I have sinned against heaven and before thee, and am no more worthy to be called thy son: make me as one of thy hired servants." No, that doesn't sound good. I will arise and go to my father and will say unto him, "Father, it was a great learning experience, and now I'm back, looking for an entry level position- No. I will arise and go to my father and will say unto him, "Hi, DAD, how you been? Oh, I'm fine. Had a good trip. Say, you got anything to eat around here?"

NARRATOR: And he arose and came to his father. And when he was yet a great way off, his father saw him, and had compassion on him, and ran, and fell on his neck, and kissed him. . ..

DAD: WALLY! Son! Oh, WALLY! (He shouts offstage.) Bring some clothes! And a ring! And some shoes! And not those running shoes! The dress shoes! And make that two rings!

WALLY: I spent all the money, DAD.

DAD: And bring the fatted calf-let's eat and be merry! My son who was dead is alive again; he was lost and now he is found. Amazing!

WALLY: Mind if I invite some friends too? (The FOOLISH VIRGINS enter, roped together.) I met them on the road. They're okay people once you get to know them.

DAD: More rings! More shoes! Another fatted calf! You look good. You look like you've lost weight.

WALLY: I've been on a high-husk diet.

DAD: DWIGHT! Look who's here! It's WALLY!

DWIGHT: (Enters reluctantly.) Hi. Nice to see you. (His DAD turns to WALLY, and DWIGHT shakes both his fists and sticks out his tongue and makes a vulgar gesture.)

DAD: We're having veal tonight, DWIGHT! WALLY's home.

WALLY: I'm going to go get some of that calf, DAD. Be right back.

DWIGHT: DAD, I don't want this to sound negative in any way, but-how many years have I been working here?

DAD: All your life.

DWIGHT: Have I ever disobeyed you, DAD?

DAD: Never.

DWIGHT: And have you ever given me a fatted calf and thrown a big party for me and my friends?

DAD: No, but, son

DWIGHT: But the minute this bozo comes hoofing it home-this leaker

DAD: But your brother was dead and he's alive again! He was lost and now he's found!

DWIGHT: I don't think you're hearing what I'm saying, DAD. You never ran up to me and hugged me- I'd just like to point that out.

DAD: I'm not a hugger, I guess.

WALLY: (Enters, mouth full.) Have some calf, you guys. That fat won't keep, you know. Sure is good fatted calf, DAD. Sure beats husks. (Off) Care for another piece, you virgins?

DWIGHT: Ever stop to think who fatted that calf, WALLY? That was our best calf, DAD. The best one. (The others slowly leave, talking among themselves.) Try to think how I feel. I'm hoeing corn all day, come in bone-tired, there's my brother smelling of pig manure, and they got the beer on ice and my calf on the barbecue! And MY RING on his hand! My ring! You promised it to me, but oh no-can't give it to the son who's worked his tail off for thirty years, oh no, gotta give it to the weasel who comes dragging his butt in the door- Oh great. Wonderful, DAD. Terrific. Maybe I'll go sleep with the pigs, seeing as you go for that. See ya later, WALLY. Help yourself to the rest of my stuff-clothes, jewels, shekels, just take what you want. Take my room. Don't worry about me. I'll be in the pigpen. (He leaves. Offstage sounds: A stove being kicked, muttered curses, pots and pans being thrown, dishes broken.)
```

---

## IC-0427: QED

- Title: QED
- Author (byline): Peter Parnel
- Work: Not specified
- Publisher: Applause Theatre and Cinema Book Publishers
- Publication date as stated: Sept 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: RICHARD
- Teaser before the introduction: Yes
- Spoken words (computed): 1004
- Already set (do not supply): none

### Source block (context only)

```text
Author: Peter Parnell
ISBN: 978-1557835925
Publisher: Applause Theatre and Cinema Book Publishers
Date (Month/Year): Sept 2002
```

### Introduction (context only: never use it for content warnings)

```text
Richard Feynman, a physics professor at Cornell University, is a man faced with a choice. He has to decide whether or not he will undergo surgery that could extend his life or end it. He is also tormented by memories of his wife and the desire to believe in something more than science.

QED by Peter Parnel
```

### Performance text (classify this)

```text
RICHARD: The thing about solving a problem – in science or in life – is that you have to think a problem through rationally, even if you disagree with your outcome emotionally. See, if your intuition doesn’t accept what your reasoning concludes, that’s okay – you’re entitled to your feelings. But at least you’ve gotten yourself to think about it.

RICHARD: When I was a kid growing up in Far Rockaway, I loved to solve puzzles. In high school, during first period, a guy would come up to me with a puzzle in geometry. I wouldn’t stop until I figured the damn thing out. Then, during the day, other guys would come to me with the same problem, and I’d do it for them in a flash. So for one guy, it took me twenty minutes, while there were five guys who thought I was a super-genius.

So I got a fancy reputation. And it might not have been all that deserved, but what did I care?!

Then, later, at Cornell, I was still solving puzzles! Only they were bigger! I tried solving the infinities of quantum electrodynamics, QED. I’d worked on it since graduate school. But the thing is, I solved it my own way, by creating my own system! Because I didn’t trust the experts who’d solved everything before me, I resolved everything they did, as if it was the first time. “Know How To Solve Every Problem That’s Already Been Solved” – that’s one of my mottoes – because, “what I Cannot Create, I do Not Understand.”

Sometimes you get so caught up with solving a puzzle, you loose sight of the reality of the world outside the puzzle. Like with this cancer I’ve got. It’s the oddest thing – it doesn’t metastasize. It just spreads. It just grows like a giant tree.

The first cancer I got, in my abdomen, got removed about four years ago along with one of my kidneys. They thought they got it all. Then it shoed up in a crazy pattern around my intestines. Dr. Hackett told me he wanted to cut out as much of it as he possibly could. He said he wouldn’t stop until he saw the bottom of the operating table underneath.

Hackett told me he never expected me to make it through that first surgery – and I’ve had too more since!

I was just reading here . . . if I do this operation, I’ll probably lose my one good kidney and be on dialysis for the rest of my life . . . Mmmmm . . . You know, I’m wondering, what am I looking at if we don’t go in? . . . Six months? A year? What’s the risk involved while I’m on the table? . . . And what about post-operatively? What are my chances of dying or living?

What should I do? Should I do this? How can I answer such a question? “If I do this, what will happen?” See, that’s usually a scientific question: The answer is always: “Try it and see.” But with this, I only have one chance.

All of this, and they can’t even tell me how much time the operation would buy me . . . . Just for some kind of hope. Hope! What good is hope? Why should I console myself with crazy, mythical thinking?

My wife, hadn’t.

When she first go sick, we made a pact that we must speak honestly with each other and look at everything directly. Her doctors told me she had Hodgkin’s disease – I told her she had glandular fever, a much less serious disorder. I lied to her. And she believed me, for a while. When she suspected something was wrong, she asked me again. And I told her the truth.

And she thanked me for it. She was better at facing what was happening to her than I was . . . I clung to false hope. I had to! How could I not . . . ?

In the last days, at the hospital . . . Arlene was very weak. She didn’t seem to know what was happening . . . She stared straight ahead most of the time, and she was trying hard to breathe. Every once in a while her breathing would stop, and then it would go on again . . . . I felt strange, sort of calm in a way. As I watched her, I kept imagining all the things going on physiologically – the lungs not getting enough oxygen into her blood, making the brain fogged out and the hear weaker which made the breathing more difficult. I kept expecting some sort of avalanche, some dramatic collapse . . . but it didn’t appear that way at all . . . she just got foggier . . . and her breathing became more shallow . . . until there was only one very small one.

It was several months before I could react emotionally to her death. Not that I didn’t feel it deeply. But it wasn’t sinking in, until I was walking past a department store with dresses in the window, and I saw a pretty dress, and I thought, she would like that. And then it hit me.

I don’t know . . . suddenly it all came out . . . it was too much for me . . .

A couple years after she died, I wrote Arlene a letter. I haven’t looked at it for . . . I haven’t looked at it in over forty years.

“Arlene, I adore you . . . it is such a terribly long time since I last wrote
you, but I know you’ll understand, because you know how I am –
stubborn and realistic – and I thought there was no sense in writing. But
now I know, my darling wife, that it is right to do what I have delayed in
doing. I want to tell you I love you. I always will love you.

You, dead, are so much better than anyone else alive. (I love my wife. My
wife is dead)
P.S. Please excuse my not mailing this, but I don’t know your new address
I’ve been dreaming about her again lately.

I’m not going to do the operation. It’s time to simply let go. Remember what the old folktale says: “Don’t cry. Don’t be sad. All men must die, and you are not the first.”
```

---

## IC-0428: Rash

- Title: Rash
- Author (byline): Eric Bogosian
- Work: Pounding Nails into the Floor with my Forehead
- Publisher: Theatre Communications Group
- Publication date as stated: Nov 1994
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1476
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Bogosian
Book: Pounding Nails into the Floor with my Forehead
ISBN: 1559360968
Publisher: Theatre Communications Group
Date(Month/Year): Nov 1994
AWARD HISTORY of selections from this text
2003 National Qualifier - DI
2005 National Qualifier- DI
2006 National Qualifier- DI
```

### Introduction (context only: never use it for content warnings)

```text
Two types of people exist in today’s society: Type One is the put-upon, guilt- ridden, half-liberated white American middle-class individual and Type Two is everyone who preys upon Type One. In Rash from Pounding Nail into the Floor with my Forehead, Eric Bogosian plunges us into the world of the self-interested living in today’s “SUBURBIA”. . . where the affluent escape from the perils of the urban jungle. You may not like the character you meet, but you’ve certainly seen him around before and no matter how detestable, unfortunately, there is a little of us in each of them. Rash by Eric Bogosian
```

### Performance text (classify this)

```text
Man speaks directly to the audience, gesticulating with a large barbecue fork as he mimes grilling at a barbecue.

So what we did, we put a chain-link fence around the whole fifteen acres. Barbed wire on top. For security, for security. 'Cause you know, Charlie, we're here all summer, the kids are running around in the yard. I sleep better at night just knowing it's out there.

Oh, yeah, we're here all summer. I go down the city maybe two, three times a month. But you know it's hot down there and we got everything we need up here. The pool. Sonia's got her tennis court, I got my griller. I just stay here all summer and grill. I put everything on this thing: steaks, chops, chicken. Last Sunday, I did some lobsters. Came out beautiful. Once they stop moving, they're a snap to cook.

Did you look at my grill, Charlie? Look at my grill. Brand new, I just got it. It's beautiful. See, right here where the steaks are, this is the grilling part. Then over here I got two stovetops, you wanna boil some peas, carrots. Underneath, oven. You-can bake a cake, cookies, whatever you want.

Up here, microwave oven. Ice chest on the side, 'frigerator on the back. Three phone lines.

Very reasonable, around three grand. Got it from the Hammacher-Schlemmer catalog. I love it. I just stand here all summer and grill. Very relaxing, I just stay here by the pool, they swim' I grill. Makes me very mellow. Like meditating.

(Shouts WHAT?!! Nah, we don't want any . . . You want any goat cheese? Charlie doesn't want any either. I don't care what you did to it, we hate goat cheese. Listen, Honey, we're starving to death out here, send out some Doritos or something. Well, if you're too busy, Jeremy can bring 'em.

(Calling to a different part of the stage) Jeremy, Honey, go up to Mommy on the porch, get Daddy and Uncle Charlie some Doritos.

(Back to Sonia) He can do it, Sonia, just give him the Doritos. Give him the Doritos! Don't give him the goat cheese!

(To Charlie) Oh yeah, he loves it. He's in there all day. Like a fish. No. No. No. No. There's no chlorine in that pool, Charlie. They use chlorine in the cheap pools. This filter, this is the best you can get. Fourteen layers of charcoal, three layers of sand. Then there's a machine, you can't see it, under the tennis courts, boils the water into steam, sterilizes it drop by drop.

Comes back to the pool, completely pure. Completely pure. You can't get water like that in nature. 'Cause I figure we got people comin' over every weekend. Somebody's gonna come over, do a couple of laps. Guy's got herpes, next thing I know everybody in the house has herpes. What do you do with a six year old with herpes? I figure spend the money, get the filter. Why waste the aggravation?

I got a good life. I never want to leave the house. I had to go to the city last week, visit a client, it was torture. It was like going off to war.

I mean you go down there now, it's like the black hole of Calcutta. You been down there lately? It's depressing. They're lying on the streets, begging, on drugs. With the babies, now they're begging. I feel so bad for those poor people, 'cause it's not their fault.

But what can you say? Life isn't fair. It's the roll of the dice. I didn't make up the rules. I just say thank God he loves us. (Fiddles with the cooking steaks)

You like roast peppers? (Stabs downward, then holds the fork up) Look at this pepper, isn't it beautiful? Balducci's, five bucks each, the best you can get. I'll have one too.

See, I keep 'em on ice over here in the ice chest, anytime I want peppers, I . . . WHAT? YES! PUT THE CORN ON NOW. PUT THE CORN ON NOW, SONIA! THE STEAK'S GONNA BE READY IN FIVE MINUTES. YOU WANT COLD STEAK? I'M ASKING, YOU WANT COLD STEAK? THEN PUT THE CORN ON NOW!

Did I tell you about last spring when we went on vacation? No, I know you know we went on vacation, but let me tell you. . .

About three weeks before we go away, I'm working in mid-town around 48th Street. And every day, I go out to lunch, stretch my legs. And every day there's this guy in front of the building with one of those signs: WILL WORK FOR FOOD. Begging. So every day, I pass this guy, I give him a quarter, I figure, I can afford it.

The guy gets used to seeing me. Every day at lunch, sees me coming, kinda gets all perky when he sees me. Gets up on his hind legs.

So about a week before we're gonna go on vacation, I go out to lunch, I see the guy, guy sees me, I reach into my pocket, I don't have any change! He's looking at me. So I figure, what the hell, who's it gonna kill? Give the guy a buck.

I throw a buck at the guy. Turns out, it's not a buck, it's a twenty dollar bill. Don't ask me how it happened. Guy jumps up, starts shaking my hand, blessing me, telling me God loves me, Jesus loves me. Shaking my hand in the middle of the sidewalk. And I never really looked at this guy up close before. He's got all these sores all over his face, no teeth, his breath could peel paint. And I'm thinking, you know, "I gave you the money, now go back and sit down!"

Anyway, I forget about the guy; three days later, me and Sonia go down to St. Barth's. . . Very nice hotel by the beach, they give you a brochure about the food and how there's these dolphins and you lie on the beach and watch the dolphins. Seven hundred dollars a night.

We get down there, I'm a little tense, I want to relax, so we go down the beach. I'm lying there, looking for the dolphins, no dolphins. I'm getting a strain in my neck. Turns out, there's no dolphins in the Caribbean. I'm in litigation with the hotel as we speak.

Anyway, we're lying there, Sonia says, "What's that?" She's pointing to my hand. There's this rash on the back of my hand. I say, I don't know, poison ivy from the country house. Forget about it.

Charlie, by the end of the week, this rash is halfway up my arm. We come back to the city, I go straight to my doctor's.

He says, "Good thing you came to see me. If you hadn't come to see me, that would have gone right up your arm, up your neck, into your eyes. You'd be blind!" Turns out. . . RIGHT! THAT'S RIGHT! The guy. Turns out, it's some kind of disease they give each other in the men's shelter. Some kind of bum disease.

All I'm saying, Charlie, all I'm saying is: I give the guy money, he gives me a disease!

(Looks up) Jeremy, what are doing?! No, Honey, don't throw Doritos in the pool. Get away from the pool, YOU'RE GONNA CLOG UP THE FILTER, IT'S GONNA COST ME FIFTY THOUSAND DOLLARS, NOW GET AWAY FROM THE POOL. JUST GO SOMEWHERE.

(Back to Charlie) I mean, look, I'm the world's biggest liberal. But you know I'm watching that CNN, I'm watching those riots in L.A. and I'm thinking to myself, What if they start doing that around here? What if they start running around like that around here?

I mean, look at this house, Charlie. You can't see this house from the road. We're vulnerable up here. What happens, we're up here one Sunday, we're hanging out: reading the paper, eating bagels, grinding coffee beans. I pick up the phone to call my mother, "Oh, the phone is dead!"

I look up, a couple of homies are at the back door. Breaking down the back door. They don't even have to be black, they could be anybody. Then what do I do? What do I do then? "Oh, come on in, would you like a cup of coffee? Maybe you'd like to rape my wife, kill my kids, burn my house down?"

What do I do then, Charlie? What do I do then?

That's why I have the gun. (Fiddles with steak) I would, I would shoot them, for the kids I would shoot. If they were from the phone company, I would still shoot them.

Anyways, these are ready. (Calls off) Jeremy, Honey, come out of the bushes, Daddy's not angry anymore. Come on out, we'll discuss it later. We're gonna have din-din now. No, no hot dogs, we've got fifteen dollar-a-pound prime sirloin from Dean & DeLuca, now come out of the bush. COME ON! COME IN THE HOUSE!
```

---

## IC-0429: Red

- Title: Red
- Author (byline): John Logan
- Work: Not specified
- Publisher: Oberon Books
- Publication date as stated: May 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ROTHKO, KEN
- Teaser before the introduction: Yes
- Spoken words (computed): 2352
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Logan
ISBN: 978-1840029444
Publisher: Oberon Books
Date (Month/Year): May 2010
```

### Introduction (context only: never use it for content warnings)

```text
Red is the color you feel when anger strikes your bones, and shudders through your being. Red is the color of the last rays of the sun touching you and filling you with warmth. Red is fire, red is lust. Red is passion, red is trust. Red reminds us that we are all simply phoenixes destined to burn.

Red by John Logan
```

### Performance text (classify this)

```text
Rothko stands, staring forward. Ken, a man in his early twenties, enters nervously. He wears a suit and tie. This is the first time he has been in the studio. Rothko gestures for him not to speak. Then he beckons for Ken to join him. Ken goes to Rothko, stands next to him. Rothko indicates the central painting (ie the audience)

ROTHKO: What do you see? (Ken is about to respond—) Wait. Stand closer. You’ve got to get close. Let it pulsate. Let it wrap its arms around you; let it embrace you. — Meet it halfway for God’s sake! Lean forward, lean into it. Engage with it! . . . Now, what do you see? — Be exact — but sensitive. You understand? Be kind. Be a human being. These pictures deserve compassion, and they live or die in the eye of the sensitive viewer, they quicken only if the empathetic viewer will let them. That is what they deserve . . . Now . . . What do you see?

(Beat.)

KEN: Red.

ROTHKO: Hang up your jacket outside. I appreciate you put on your Sunday clothes to impress me, it’s poignant really, touches me, but it’s ridiculous. We work hard here. Go hang up your jacket outside. (Ken exits and returns without his jacket. Takes off his tie and rolls up his sleeves.) We start every morning at nine and work until five. You’ll help me stretch the canvases and mix the paints and clean the brushes and build the stretchers and move the paintings. You’ll pick up food and cigarettes and anything else I want, any whim, no matter how demanding or demeaning. If you don’t like that, leave right now. Answer me. Yes or no.

KEN: Yes.

ROTHKO: I am not your rabbi, I am not your father, I am not your shrink, I am not your friend, I am not your teacher —I am your employer. You understand?

KEN: Yes.

ROTHKO: I’m painting a series of murals now — (He gestures all around.) You’ll help me put on the undercoat and then I’ll paint them and then I’ll look at them and then paint some more.

(Rothko moves away. Beat.) How do they make you feel?

KEN: Give me a second. (Ken moves to the middle of the room and takes in all the paintings.) Disquieted.

ROTHKO: And?

KEN: Thoughtful . . . Um . . . Sad.

ROTHKO: Tragic.

KEN: Yeah.

ROTHKO: They’re for a restaurant. (Rothko smiles. He enjoys this.) So I’m minding my own business when Mister Philip Johnson calls me. He’s designing the new Seagram Building on Park Avenue. In this building there is to be a restaurant called the Four Seasons, like the Vivaldi, and on the walls of this restaurant . . . (He gestures expansively to his paintings. Beat. Proud.) Thirty-five thousand dollars they are paying me. (Ken is impressed. Thirty-five thousand dollars is a fortune.)

KEN: (Beat . . . trying to impress his new employer) I went to the Modern last night, saw the Picasso show.

ROTHKO: That man — though now a charlatan, of course, signing menus for money like Dali, when he’s not making ugly little pots, also for money — that man at his best understood the workings of time . . . Tragic, really, to grow superfluous in your own lifetime. We destroyed Cubism, de Kooning and me and Pollock and Barnett Newman and all the others. We stomped it to death.

KEN: You take pride in that. “Stomping” Cubism to death.

ROTHKO: The child must banish the father. Respect him, but kill him.

KEN: And enjoy it?

ROTHKO: Picasso I thank for teaching me that movement is everything! Movement is life. The second we’re born we squall, we writhe, we squirm; to live is to move. Without movement paintings are what?

KEN: Dead?

ROTHKO: Precisely (He gestures to his paintings.) . . . Look at the tension between the blocks of color: the dark and the light, the red and the black and the brown. The more you look at them the more they move . . . they breathe . . . They’re not dead because they’re not static.

KEN: (Excited.) They need the viewer. Representational pictures are unchanging; they don’t require the active participation of the viewer. In the Louvre in the middle of the night the “Mona Lisa” is still smiling. But do these paintings still pulse when they’re alone? (Ken is lost in thought. Rothko watches him, pleased.) That’s why you keep the lights so low. . . To help the illusion. Like a magician. Like a play. To keep it mysterious, to let the pictures pulsate. Turn on bright lights and the stage effect is ruined — (Ken goes to the light switches. He snaps on all the lights. Ugly fluorescent lights sizzle on. The room immediately loses its magic.)

ROTHKO: What do you see?

KEN: My eyes are adjusting . . . Just . . . White.

ROTHKO: What does white make you think of?

KEN: Bones, skeletons . . . Charnel house . . . Anemia . . . Cruelty. (Rothko is surprised by this response.)

ROTHKO: How does white make you feel?

KEN: Frightened? . . . It’s like the snow . . . outside the room where my parents died. It was winter. I remember the snow outside the window: white (Turns his attention to the paintings.) . . . And the pictures in this light . . . They’re flat. Vulgar . . . This light hurts them. (Rothko turns off the fluorescent lights. The normal light returns.)

ROTHKO: You see how vulnerable they are? . . . People think I’m controlling . . . It’s not controlling, it’s protecting. A picture lives by companionship. It dies by the same token. It’s a risky act to send it out into the world. (He abruptly stops to stare at his painting. He tilts his head. Like he’s listening. Bring me the second bucket. (Ken, excited, brings him a brush and a bucket of dark maroon paint. Rothko is unsure. He looks at the painting. The moment is passing. He is getting desperate. To himself, frustrated.) Come on . . . come on . . . come on . . . What does it need?

KEN: Red.

ROTHKO: I wasn’t talking to you! (Beat. Tragically, the moment has passed for Rothko. He flings the paintbrush away. It splatters. He spins on Ken.) DON’T YOU EVER DO THAT AGAIN! (He rages, stomping restlessly around the room:) By what right do you express an opinion on my work? Who are you? “RED”?! — I don’t even know what that means! You mean scarlet? You mean crimson? You mean plum-mulberry-magenta-burgundy-salmon-carmine-carnelian-coral? What is “RED”?! (Rothko stands, getting his breath, collecting himself. Beat.)

KEN: I meant sunrise. I meant the red at sunrise . . . The feeling of it. Sunrise is red and red is sunrise. (Ken begins cleaning up.) Red is heartbeat. Red is passion. Red wine. Red roses. Red lipstick.

ROTHKO: Arterial blood.

KEN: That too. (Rothko thinks about it.)

ROTHKO: Rust on the bike on the lawn.

KEN: And apples . . . And tomatoes.

ROTHKO: Lava. Lobsters. Scorpions.

KEN: Stop sign. Sports car. A blush.

ROTHKO: Slash your wrists. Blood in the sink. (Beat.) So . . . red. (Rothko gazes thoughtfully at his painting then turns away) I can’t look at it now. It’s too depressing.

KEN: How can all that red be depressing?

ROTHKO: I don’t see the red anymore . . . .

KEN: What?

ROTHKO: Black. (Beat.) There is only one thing I fear in life, my friend . . . One day the black will swallow the red. (He puts on his glasses again and stares at his painting.) (Beat) I was walking up to my house last week and this couple was passing. Lady looks in the window, says: “I wonder who owns all the Rothkos.” . . . Just like that I’m a noun. A Rothko . . . An overmantel.

KEN: A what?

ROTHKO: (as Rothko speaks, they finish priming the next canvas) The overmantels. Those paintings doomed to become decoration. You know, over the fireplace in the penthouse. They say to you, “I need something to work with the sofa, you understand. Here’s a paint chip from the Sherwin-Williams” . . . . It’s an investment . . . It goes with the lamp . . . It’s interior decoration . . . It’s anything but what it is. (Beat.) (The priming is finished on the canvas and Rothko steps back and studies it. Musing.) So . . . so . . . so . . . it’ll do . . . What do you think?

KEN: It’s a . . . a good ground, a good base layer. Nice and even. (Ken smiles, Then he stops abruptly. Surprisingly, tears come to his eyes. The emotion is unexpected.)

ROTHKO: What is it?

KEN: It’s strange . . . I’m remembering something . . . The, um, color . . . is . . . Dried blood . . . When the blood dried it got darker. On the carpet where my parents died. (Ken tries to shake off the thought. He moves away. But then he stops again. He can’t shake the emotion. The canvas draws him back.) It’s exactly the color.

ROTHKO: What happened to your parents?

KEN: They were murdered.

ROTHKO: What happened? (Ken stares forward, lost in thought. Beat.) What do you see? (Ken shakes his head. Beat.)

KEN: (Reliving it) I woke up . . . and the first thing I saw was the snow outside my window. But . . . but . . . It was really quiet. . . . And it’s cold. There’s a window open somewhere . . . Then I see my sister, just standing in the hallway, staring into my parent’s room. My sister . . . she’s standing in a puddle of pee. Her eyes . . . I go to the door and look in and see the snow first. And then the blood. The bed’s stained with it. And the wall. They’re on the bed . . . Apparently it was a knife. (Beat.) Burglars, I found out. At least two of them . . . I don’t want my sister to see anymore. My little sister [I was seven] . . . I turn around and push her out and shut the door. The door handle . . . With blood . . . Is red. (Beat.) That’s all.

ROTHKO: What happened to you two?

KEN: State took us. Foster homes. People were nice, actually. They kept us together. But they shuffled us around a lot. We were rootless… Never belonged . . . Never had a place. (Ken continues to clean up. Pause.) Can I ask you something? . . . Are you really scared of black?

ROTHKO: No, I’m really scared of the absence of light.

KEN: Like going blind?

ROTHKO: Like going dead.

KEN: And you equate the color black with death. . . Because black is the lack of red, if you will. The bright colors are your passion, your will to survive — your “life force.” But if black swallows those bright colors then you lose that excess and extravagance, and what do you have left?

ROTHKO: [T]rust me, as you get older those colors are harder to sustain. The palate fades and we race to catch it before it’s gone.

KEN: In reality we both know black’s a tool, just like ochre or magenta. It has no effect. Seeing it as malevolent weird.

ROTHKO: You think so? What about equating white with death; like snow?

KEN: That’s different. That’s just a personal reaction. I’m not building a whole artistic sensibility around it.

ROTHKO: Maybe you should.

KEN: Come on, a painter gets older and the color black starts to infuse his work, therefore, the cliché goes, he’s depressed, he’s fearing death. He’s losing touch, he’s losing relevance, he’s saying goodbye.

ROTHKO: That’s a cliché except for when it’s not.

KEN: But it’s not true. . . Look at Van Gogh; his last pictures are all color. He paints the most ecstatic yellows and blues know to man — then shoots himself . . . Or Matisse, his last works were nothing but great shocks of primary colors . . . . he was dying, he knew he was dying, but he was still Matisse. When he got too ill to hold a paintbrush he used scissors, cutting up paper and making collages. He never gave up. On his deathbed he was still organizing the color patterns on the ceiling. He had to be who he was.

ROTHKO: (Rothko looks at him.) In the National gallery in London there’s a picture by Rembrandt called Belshazzar’s Feast . . . Belshazzar, King of Babylon blasphemes, so a divine hand appears and writes some Hebrew words on the wall as a warning . . . In the painting these words pulsate from the dark canvas like something miraculous. Rembrandt’s wrote “Mene, Mene, Tekel, Upharsin.” “You have been weighed in the balance and have been found wanting.” (Beat.) That’s what black is to me . . . ****Scene***** Ken is alone, building a wooden canvas stretcher/frame. Then the sound of a slamming door from outside surprises him. Rothko rages in, flinging off his overcoat and hat.

ROTHKO: THEY’RE TRYING TO KILL ME! I swear to God they’re trying to kill me!

KEN: So . . . how did you like the exhibit? (Rothko is not amused. He lights a cigarette.)

ROTHKO: (Seriously.) These young artists are out to murder me.

KEN: Andy Warhol? (Rothko doesn’t even answer.) You sound like an old man.

ROTHKO: My point is . . . People like me . . . My contemporaries, my colleagues . . . We all had one thing in common . . . We understood the importance of seriousness. (Beat.) You know the problem with those painters? They are painting for this moment right now. And that’s all. Completely temporal, completely disposable, like Kleenex, like —

KEN: Like Campbell’s soup, like comic books —

ROTHKO: You really think Andy Warhol will be hanging in museums in a hundred years?

KEN: He’s hanging alongside Rothko now.

ROTHKO: Because those goddamn galleries will do anything for money — cater to any wicked taste. That’s business, young man, not art! (Ken approaches. Not backing down.)

KEN: You ever get tired of telling people what art is?

ROTHKO: No, not ever. Until they listen.

KEN: You’re just mad because the barbarians are at the gate. And, whattaya know, people seem to like the barbarians.

ROTHKO: Of course they like them. That’s the goddamn point! You know what people like? Happy, bright colors. they want things to be pretty. (Explodes.) “Pretty.” “Beautiful.” “Nice.” “Fine.” How are you? Fine. How was your day? Fine. How are you feeling? Fine. Well, let me tell you, everything is not fine! (He spins to his paintings.) Conflicted. Nuanced. Troubled. Diseased. Doomed. I am not fine. Look at these pictures. Look at them! You see the dark rectangle, like a doorway, , yes but it’s also a gaping mouth letting out a silent howl of something feral and foul and primal and REAL. Not nice. Not fine . . . I AM HERE TO MAKE YOU THINK! . . . I AM NOT HERE TO MAKE PRETTY PICTURES! (A long beat. Rothko roams, disturbed, trying to recover his equilibrium. Ken hasn’t moved.)

KEN: So said the Cubist, the second before you stomped him to death. (Rothko stops, looks at him.) “Tragic, really, to grow superfluous in your own lifetime” . . . Right? “The child must banish the father. Respect him, but kill him.” . . . Isn’t that what you said? . . . You guys went after Cubists and Surrealists and, boy, did you love it. And now your time has come and you don’t want to go. Well, exit stage left, Rothko. Because Pop Art has banished Abstract Expressionism . . . (Beat.) Don’t worry; you can always sign menus for money.

ROTHKO: How dare you?

KEN: (Beat.) Do you know where I live? Uptown? Downtown? Brooklyn? [Do] you know if I’m married? Dating? Queer?

ROTHKO: No. Why should I —? You’re an employee. This is about me. Everything here is about me. You don’t like that; leave . . . your neediness bores me —

KEN: (Explodes) Bores you?! Bores you?! — (Ken roams angrily.) You know, not everything has to be so goddamn IMPORTANT all the time! Not every painting has to rip your guts out and expose your soul! Not everyone wants art that actually HURTS! Sometimes you just want a still life or landscape or soup can or comic book! Nothing is ever good enough for you! Not even the people who buy your pictures! Museums are nothing about mausoleums, galleries are run by pimps and swindlers, and art collectors are nothing but shallow social-climbers. (He stops, slows, realizing.) Who’s good enough to even see your art? . . . Is it just possible no one is worthy to look at your paintings? . . . That’s it, isn’t it? . . . We have all been “weighed in the balance and have been found wanting.” (He approaches Rothko.) You say you spend your life in search of real “human beings,” people who can look at your pictures with compassion. But in your heart you no longer believe those people exist . . . So you lose faith . . . you lose hope . . . black swallows red. (Beat. Ken is standing right before Rothko.) My friend, I don’t think you’d recognize a real human being if he were standing right in front of you.

ROTHKO: (defeated) You’re fired. (Beat. Ken stares at him. He can’t believe it.) Write down your address, I’ll send you your final check.

KEN: You owe me an explanation.

ROTHKO: I don’t owe you anything — (Ken pursues. Rothko tries to avoid him. The conflict builds. Rothko spins on him, points to the outside with the realization dawning that his artistic time is past.) Because your life is out there! (Beat.) Listen, kid, you need to find your contemporaries and make your own world, your own life . . . You need to . . . make them look. (Ken is moved. Rothko continues with quiet emotion.) When I was your age, art was a lonely thing: no galleries, no collecting, no critics, no money. We didn’t have mentors. We didn’t have parents. We were alone. But it was a great time, because we had nothing to lose and a vision to gain. (Beat.) Okay? . . . Make something new. (Rothko steps away. Ken gathers his things and starts to go. He stops at the door. He turns back.) What do you see? (Ken looks at the paintings. But then he looks at Rothko. Beat.)

KEN: Red. (Beat. Ken exits. Rothko stands alone.)
```

---

## IC-0430: Redeployment

- Title: Redeployment
- Author (byline): Phil Klay
- Work: Redeployment, Pgs 1-16
- Publisher: Penguin Books
- Publication date as stated: Feb 2015 (Reprint)
- Event as filed: Dramatic Interpretation
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

Cheryl said, 'How are you?' which meant: How was it? Are you crazy now?

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

## IC-0431: Rest Area

- Title: Rest Area
- Author (byline): Clay McLeod Chapman
- Work: Rest Area: Stories, Pgs 1-8
- Publisher: Hyperion
- Publication date as stated: Feb 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: GRACE’S DAD
- Teaser before the introduction: Yes
- Spoken words (computed): 1947
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
When you’re traveling on a long road trip, a rest stop can provide a much-needed break and an opportunity to recharge your batteries; especially if you are traveling alone with children. Unfortunately, because they are often in isolated locations where help is many miles away, rest areas are not always safe.

The last thing anyone wants to think about is a child being abducted, but it’s a harsh reality. *According to the Child Crime Prevention and Safety Center, “each day 33 children are abducted by someone who is not a family member.”

What should you do if your child is missing? Immediately call local law enforcement. But that’s not what happens in Rest Area by Clay McLeod Chapman and we begin to wonder why.
```

### Performance text (classify this)

```text
GRACE’S DAD: (talking to a family through the window of a car) (Pg 1-8) Carolina plates. You guys have come far. Where you heading? Out Midwest? Lord, that’s a long haul. And with the whole family, boy. Who’s the little tinker in the backseat? Hi there. She doesn’t mind being buckled up all day? Good for her. My daughter and I did our own bit of venturing cross-country this summer, just the two of us. We ambled along the back roads for weeks.

Could you tell me if you’ve seen her? Here. (holds out a flyer) Here’s a photograph of her. Well, a photocopy. You can’t make out her features very well. But if you look here, right above the smudge, you can still spot her smile. That’s Grace’s smile.

I’m pasting them up all along here. On the soda machines. There’s a whole stack with the tourist pamphlets. Just in case someone’s seen her. Can’t be too sure, now.

You didn’t, did you? Did you see a girl on the road? Red hair, Cream shorts. No sign of her?

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

## IC-0432: The Robber

- Title: The Robber
- Author (byline): William Heuman
- Work: 12 New Testament Portraits
- Publisher: Standard Publishing
- Publication date as stated: 1966
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1613
- Already set (do not supply): none

### Source block (context only)

```text
Author: William Heuman
Book: 12 New Testament Portraits
ISBN: B0007HWB26
Publisher: Standard Publishing
Date(Month/Year): 1966
```

### Introduction (context only: never use it for content warnings)

```text
(no introduction)
```

### Performance text (classify this)

```text
"Which of the two do you want me to release to you?" asked the governor.

"Barabbas," they answered.

"What shall I do, then, with Jesus who is called Christ?" Pilate asked.

They all answered, "Crucify Him!"

"Why? What crime has He committed?" asked Pilate.

But they shouted all the louder, "Crucify Him!" Barabbas was a notorious criminal who Pilate proposed to execute instead of Jesus. This is his story . . . The Robber by William Heuman.

I have seen men crucified out in the hills. I have seen some of the hills of Galilee covered with the crosses; I have heard men cry out in agony. I have seen them die this slow and most torturous death, but I am not afraid. Never have I been afraid to die. I will spit in their faces when they nail me to the cross; I will laugh at them; I will mock them, and they will wait in vain for my cries. I am Barabbas, and in my body runs the blood of David, mighty warrior, mighty king.

Even here, though, in this hole in the ground where there is no light, where there is only dampness and cold and these dead dreams, there comes yet one small ray of hope. It has been said that the governor is to release a prisoner for the Passover feast. This gesture is to make the governor a trifle more acceptable to the people, who hate him as they hate those who sent him.

There is a prisoner to be released, and it could be me. My crime was not murder, though some say it is. We fought the Romans and we defeated them, and I am held here for sedition. I will not plead or beg for my life, but if it is given to me I shall not refuse it.

I am not old. I am a young man who has run through the hills, who has drunk from the cool mountain springs, who has eaten lamb in the wild mountains, who has loved women. It is not that I despise life; it is only that I reject cowardice. A man is a man, or he is a dead dog. Life, if miraculously returned to me, I would accept with pleasure, because great pleasures still lie ahead of me.

But I speak foolishness. In this deep hole I would have heard nothing had not the slave who was brought in here to fasten the fetters on my ankles whispered to me that there was this small hope. I would be a fool to magnify such a rumor. For all I know there are fifty prisoners in this dungeon to be released ahead of Barabbas, the robber. Still a man can hope and he can dream of the high hills, the wind once again ruffling his hair, the warm sun on the side of the mountain in the early morning, and the firelight in the evening. He can remember choice comrades at his side, brave men and true, all dead now except Barabbas who is to die tomorrow.

In the darkness now I see a glow of light, and it has been but a few hours since I ate last. They are not bringing me food. I have no friends to visit me, and no friends are permitted if there were such. The light is coming closer, and I hear the rattle of armor and the clank of sword. Now they are at my door, and I see their faces, the hard, cruel Roman faces, the gleam of torchlight on their armor. The slave is with them, grinning, his white teeth like so many ivories. It is he who informs me that I am to be released, and it is he who strikes the chains from my feet with powerful blows of his hammer, the Roman guard watching in cool arrogance.

“You are free,” the slave informs me. “The governor has released you, Barabbas, to please the people.”

“Man,” the Roman tells me scornfully, “They are to crucify another in your place. You will live until we run our swords through you at another place.”

“Who is to die for me?” I ask. “The teacher, Jesus of Nazareth,”

I have heard of him. Indeed, once I saw him in the hills of Galilee when my men came down into a village to forage. I saw him speak with the poor. I saw the crowds about him. I had heard that he was a great healer of many sicknesses, but he was not a warrior. He carried no sword with him, nor did his followers. This was a man of peace, and I did not wait to hear his words. One can talk of peace to the Romans only with the sword in one hand and a buckler in the other. This is the only peace they understand.

Yet I remember his face, a young man. His face was not like the faces of other men, and I still remember, even though it was several years ago that I saw him. His was a face full of kindness and love, and with no evil in it. This was the face of a god and not a man; not a weak face, but a face where sin could not abide. Many times I have thought of that face, and I have heard much talk of this Jesus in my wanderings and fighting in Judea, in Galilee, in Samaria. I had not known that he, like myself, was a prisoner in this evil place.

“What crime has he done?” I ask the Roman. “He a man without a sword.”

“It is not for you to ask questions,” the Roman informs me. “Go and pray to your god or we will run you through before you have passed the outer gate.”

There is a weakness in my legs as I hurry down the damp, stony corridor, passing one gate and then another until I emerge into the sunlight. I have not seen the sun in many weeks, and I am blinded by it. I want to sing and shout aloud for joy because life is good, but it is then that I remember this Jesus of Nazareth, who is to die in my place. I try to convince myself that it is my good fortune and his loss, but I cannot forget his face. What charges could they have brought against so good and just man? What evil could he have committed?

There are crowds in the street, and all seem to be hastening toward the gate of the city. There seems to be a holiday atmosphere. I touch one man’s arm and ask him, “Where is the crowd going, friend?”

With contempt he looks at my rags, my filth, my blood-caked body. “They are crucifying Jesus of Nazareth this morning,” he says, as he hurries on with the others. It is a strange fact that men of peace love the sight of blood and suffering in others.

I follow the crowd out through the gate and off on a hill nearby. The place is called Golgotha, the place of the skull. I see the vast crowd assembled with more and more people streaming out of the city, pushing to get up closer. I see two crosses on the hill, and now a third is being raised against the pale blue sky. It is already done! Barabbas is free, but the man Jesus will never walk the Galilean streets again.

I must see Him. I must see the face that has haunted me through the years. I ask another, “What is the charge against this man, Jesus?”

‘Treason against Rome,” he says, “and blasphemy against our God.” “Blasphemy!” I repeat. “He preached that he is the Son of God.”

I must see his face before the light of life is gone from it. I push on through the crowd because I am a big man and strong. Curses are hurled at me as I make my way up the hill. I see the priests in their costly robes, watching him on the middle cross. There are some women, followers of his from Galilee, and I hear one say that his mother is here also. Poor woman, to witness this terrible suffering of her son! I see the soldiers, their armor gleaming in the sunlight. Some watch the three dying men on the crosses; others play their favorite game of dice. I see the face now, and it is the same face, pale, drawn with suffering, but there is in it something that never can be erased, not by cruel nails or flagellations or scourgings. Nothing that men can do can take away the love on that face.

His eyes are closed as I come closer and closer. I hear the weeping of the women. I hear the derisive taunts and shouts of those who this day have called for his blood. I hear the ribald curses of the Romans at their game, and I hear the moans of the two thieves crucified with him, one on either side, but no sound comes from him on the middle cross.

I come closer and I stand behind the Romans who kneel at their game. I look up into his face, and he opens his eyes, and he looks down on me. He has never met me; he has never seen me, although I have seen him, but he knows me. This I can see in his eyes. There is compassion, love, the forgiveness of my crimes. He looks at me, and I sink slowly to my knees.

“My Lord,” I whisper, “and my God!”
```

---

## IC-0433: Sarah Cole: A Type of Love Story

- Title: Sarah Cole: A Type of Love Story
- Author (byline): Russell Banks
- Work: Success Stories
- Publisher: Harper and Row
- Publication date as stated: June 1986
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: RON, SARAH
- Teaser before the introduction: Yes
- Spoken words (computed): 2448
- Already set (do not supply): none

### Source block (context only)

```text
Author: Russell Banks
Book: Success Stories
ISBN: 978-0060155674
Publisher: Harper and Row
Date (Month/Year): June 1986
```

### Introduction (context only: never use it for content warnings)

```text
There are those of us who think, “Beauty is in the eye of the beholder”, or even, “it’s what’s on the inside that counts”. But to be brutally honest . . . isn’t that just what we said to our overweight, uglier friends when we were in high school? In this selection, our handsome protagonist, Ron, reflects on a period in his life when he crossed paths with and possibly fell in love with homely, Sarah Cole. Can men see past a woman’s looks? Do men ever form real relationships with unattractive women? Sometimes the truth itself is ugly.

Sarah Cole: A Type of Love Story by Russell Banks
```

### Performance text (classify this)

```text
RON: Here is a scene in which I am the man and my friend Sarah Cole is the woman. I don’t mind describing it now, because I’m a decade older and don’t look the same now as I did then, and Sarah is dead. I was extremely handsome then. And I must tell you that Sarah was very homely. In fact, she was the homeliest woman I have ever known. Personally, I mean. I’ve seen a few women who were more unattractive than Sarah, but they were clearly freaks of nature or had been badly injured or had been victimized by some grotesque, disfiguring disease. Sarah, however, was quite normal, and I knew her well.

RON: Around six o’ clock on a Wednesday evening in late May a man enters a bar. Our man, Ron, is effortlessly attractive, a genetic wonder, tall, slender, symmetrical, and clean. His flaws: a small mole on the left corner of his square but not-too-prominent chin, a slight excess of blond hair on the tops of his tanned hands, and somewhat underdeveloped buttocks, only contribute to his beauty.. And he is nice, too, the consequence, perhaps, of his seeming not to know how beautiful he is. Ron takes a seat at the bar, unfolds the evening paper in front of him, and orders a scotch and soda, with a twist.

He has got to the classified section, when the woman who will turn out to be Sarah Cole leaves a booth in the back and approaches him. She comes up from the side and sits next to him. She’s wearing heavy, tan cowboy boots and a dark brown, suede cowboy hat, lumpy jeans and a yellow tee shirt that clings to her arms, breasts, and round belly like the skin of a sausage. Though he will later learn that she is thirty-eight years old, she looks older by about ten years, which makes her look twenty years older than he actually is.

SARAH: It’s not bad here at the bar. (looking around) More light, anyhow. Whatcha readin’?

RON: Ron looks up from his paper with a slight smile on his lips, sees the face of a woman homelier than any he has ever seen or imagined before, and goes on smiling lightly. He feels himself falling into her tiny, slightly crossed, dark brown eyes, pulls himself back, and studies for a few seconds her mottled, pocked complexion, bulbous nose, loose mouth, twisted and gapped teeth, and heavy but receding chin. He casts a glance over her thatch of dun-colored hair and along her neck and throat, where acne burns against gray skin, and returns to her eyes, and again feels himself falling into her. (To Sarah) What did you say? She knocks a mentholated cigarette from her pack, and Ron swiftly lights it. Blowing smoke from her large, wing-shaped nostrils, she speaks again. Her voice is thick and nasal, a chocolate-colored voice.

SARAH: I asked you whatcha readin’, but I can see now.” (loud bark of a laugh) The paper!

RON: (laughing too) The paper! The Concord Monitor!” (to audience) He is not hallucinating, he clearly sees what is before him and admits to himself that he is speaking to the most unattractive woman he has ever seen. He begins to ask questions of her, he buys her a drink, he smiles, until soon it seems, even to him, that he is taking her and her life quite seriously. He learns her name, of course, and she volunteers the information that she spoke to him on a dare from one of the two women still sitting in the booth behind her. Sarah goes on telling him what he wants to know, about her job at the Rumford Press, about her divorced husband who was a bastard. She tells Ron about her three children. She speaks of her children with genuine tenderness and concern, and Ron is touched. (to Sarah) You’re a nice woman. (to audience) He wonders about her husband. What kind of man would fall in love with Sarah Cole? (Scene Break)

Friday, and once again Ron appeared with his evening newspaper. After a few minutes Sarah was once again at his side. She talked more easily than she had the night before, and [Ron . . . . no . . . .] (Shift to first person is intentional) I listened as eagerly and carefully as I had before. I did not know how cruel this was. When you have never done a thing before and that thing is not simply and clearly right or wrong, you frequently do not know if it is a cruel thing, you just go ahead and do it, and maybe later you’ll be able to determine whether you acted cruelly.

While we drank, Sarah told me that she hated her ex-husband because of the way he treated the children.

SARAH: He won’t even write them a letter or anything. He won’t call them on the phone, all he calls for is to bitch at me because I’m trying to get the state to take him to court so I can get some of the money he’s s’posed to be paying for child support. And he won’t even think to talk to the kids when he calls. Won’t even ask about them.

RON: He sounds like a bastard.

SARAH: He is, he is. I don’t know why I married him. Or stayed married. Fourteen years, for Christ’s sake. He put a spell over me or something, I don’t know. (wistfully) He wasn’t what you’d call good-looking.

RON: (to audience) After her second drink, she decided she had to leave. Her children were at home, I left the place and drove straight to my apartment. One night several weeks later, Ron (Shift to 3rd person is intentional) meets Sarah at Osgood’s, and after buying her three white Russians and drinking three scotches himself, he takes her back to his apartment.

I’m still the man in this story, and Sarah is still the woman, but I’m telling it this way because what I have to tell you now confuses me, embarrasses me, and makes me sad, and consequently, I’m likely to tell it falsely.

Ron unlocks the door to his apartment, walks in ahead of her, and flicks on the lamp beside the couch. (to Sarah) Come in, come in. (to audience) She steps timidly in and closes the door behind her. She removes her cowboy hat, then quickly puts it back on, crosses the living room, and plops down in a blond easy chair. (to Sarah) Would you like a drink?

SARAH: No . . . I guess not. (not looking at Ron and visibly nervous) I don’t know. I don’t know . . . I don’t know.

RON: What? Change your mind? Seriously. Want me to fix you a white Russian?

SARAH: No.

RON: (gently) Are you scared? . . . . I am.

SARAH: Well, no, I’m not scared. (silent beat) You’re scared? Of what? (still avoiding eye contact)

RON: Well . . . I don’t do this all the time, you know. Bring home a woman I . . .

SARAH: Picked up in a bar.

RON: No. I mean, I like you, Sarah, I really do. And I didn’t just pick you up in a bar, you know that. We’ve gotten to be friends, you and me.

SARAH: You want to sleep with me? (still no eye contact)

RON: Yes. Do you want to sleep with me?

SARAH: (turning away and speaking softly) Sure I do, but … it’s hard to explain. You and me . . . we’re real different . . . you’re nice, but you don’t know what I mean, and that’s one of the things that makes you so nice. But we’re different. (suddenly gathering herself and heading toward the door) Listen I gotta go. I gotta leave now. We can be friends. Okay? (Sarah leaves in a rush – Ron watches her go, then softly closes the door

RON: (to audience) But that’s not the point of my story. I’m trying to tell the story so that I can understand what happened between me and Sarah Cole that summer and early autumn ten years ago. To say we were lovers says very little about what happened; to say we were friends says even less. No, if I’m to understand the whole thing, I have to say the whole thing. What I need to know is whether what happened between me and Sarah Cole was right or wrong. But let me go on with my story.

Sarah appeared at my apartment door the following morning, a Sunday, cool and rainy. She wore a yellow rain slicker and cap and looked more like a disconsolate schoolgirl facing an angry teacher than a grown woman. I invited her inside, and she accepted my invitation. I

What else can I do? I must describe it. I remember that moment of ten years ago as if it occurred ten minutes ago, the newpapers scattered over the couch and floor, the sound of windblown rain washing the sides of the building outside, and the silence of the room, as we stood across from one another and watched, while we each simultaneously removed our own clothing, my robe, her blouse, my pajama top, her skirt, my pajama bottom . . .

We made love that morning in my bed for long hours that drifted easily into afternoon. And we talked, as people usually do when they spend half a day or half a night in bed together. I told her of my past, named and described the people I had loved and had loved me, my ex-wife in New York, my brother in the Air Force, my father and mother in their condominium in Florida, and I told her of my ambitions and dreams and even confessed some of my fears. She listened patiently and intelligently throughout and talked much less than I.

During the next few weeks we met often and always at my apartment. Then one hot night, a Saturday in August, Sarah suggested that we go out for a drink. (To Sarah) Now?”

SARAH: Sure. It’s early. What time is it?

RON: Nine-forty-nine.

SARAH: There. See? Besides, Ron, it’s Saturday night. Don’t you want to go out and dance or something? (silence for a moment) You don’t want anybody to know about us, do you? Do you? You’re ashamed of being seen with me. You’ll sleep with me, but you won’t go out in public with me.

RON: That’s not true, Sarah.

SARAH: You owe me, Ron, you owe me.

RON: I don’t know what you’re talking about, Sarah. I don’t owe you anything.

SARAH: Friendship you owe me. And respect. Friendship and respect. A person can’t do what you’ve done with me without owing them friendship and respect.

RON: Sarah, I really don’t know what you’re talking about. I am your friend, you know that. And I respect you. I really do.

SARAH: You really think so, don’t you? (silence, then a sigh and in an almost inaudible voice) Then you’ll have to go out in public with me. Maybe well even go to a couple of parties, because I get invited to parties sometimes, you know. I have friends, and I have some family, too, and you’re gonna have to meet my family. (voice gradually rising until she was almost shouting) My kids you’re gonna have to meet them. And sometimes you’re gonna come over and spend the evening at my place! You owe that to me. Or else you’re a bad man. It’s that simple.

RON: (to audience) It was. (scene change- Intentional shift to 3rd person) The handsome man is over-dressed. Everyone else is dressed appropriately - jeans and cowboy boots, tee shirts with catchy sayings printed across the front. The man doesn’t know anyone, but the woman knows most of the people there, and she gladly introduces him. The woman does most of the talking for everyone. She chats and rambles aimlessly through loud monologues, laughs uproariously at trivial jokes, and drinks too much, until soon she is drunk, thick-tongued, clumsy, and the man has to say her goodbyes and ease her out the door to his car and drive her home to her apartment.

This happens twice in one week, and then three times the next. Ron no longer calls Sarah when he gets home from work; he waits for her call, and sometimes, when he knows it’s she, he doesn’t answer the phone. Usually, he lets it ring five or six times, and then he reaches down and picks up the receiver. (to Sarah) Hello?

SARAH: (in a flat voice) We should talk.

RON: (to audience) The woman arrives at Ron’s apartment. It’s a warm evening, and she’s wearing her white bermuda shorts, a pink sleeveless sweater, and shower sandals. Ron hates those clothes. He hates the way the shorts cut into her flesh at the crotch and thigh, hates the large, dark caves below her arms that get exposed by the sweater, hates the flapping noise made by the sandals.

Shortly, there is a soft knock at his door. He opens it, turns away. He invites her to sit down. (to Sarah) Well, you wanted to talk.

SARAH: Yes. But now you’re mad at me. I can see that. I didn’t do anything, Ron. (long pause and a sign) You don’t want to see me anymore, do you?

RON: Yes. That’s right.

SARAH: (in a low voice) You’re a son of a bitch. You’re worse than my ex-husband. (smiling meanly) You think I’m just so much meat, and all you got to do is call up the butcher shop and cancel your order. Well, now you’re going to find out different. You can’t cancel your order. I’m not meat, I’m not one of your pretty little girlfriends who come running when you want them and go away when you get tired of them. I’m different. I got nothing to lose, Ron. Nothing. You’re stuck with me, Ron.

RON: (through clinched teeth) Enough is enough. I’ve given you enough. (to audience) Ron orders her to leave. She refuses. He grabs her by the arm and yanks her to her feet. He stands back and places his fists on his hips and looks at her. (to Sarah) Go on and leave, you ugly bitch. (to audience). And then she is gone, and he is alone again. Perhaps I should admit, since we are nearing the end of my story, that I don’t actually know that Sarah Cole is dead. People said Sarah moved back with her ex-husband and was living in a trailer in a park . . . .

When someone you have loved dies, you accept the fact of his or her death, but then the person goes on living in your memory. You have imaginary conversations with him or her, you see something striking and remind yourself to tell your loved one about it and then get brought up short by the knowledge of the fact of his or her death, With Sarah, none of that happened. When she was gone from my life, she was gone absolutely, as if she had never existed in the first place. It was only later, when I could think of her as dead and could come out and say it: “My friend Sarah Cole is dead” -- that I was able to tell this story, for that is when she began to enter my memories. I learned that I truly did love her, and now I have begun to grieve over her death, to wish her alive again, so that I can say to her the things I could not know or say when she was alive, when I did not know that I loved her.
```

---

## IC-0434: Satan

- Title: Satan
- Author (byline): Kahlil Gibran
- Work: Treasured Writing of Kahlil Gibran
- Publisher: Castle Books
- Publication date as stated: Oct 2009
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SATAN, FATHER SAMAAN, NARRATOR
- Teaser before the introduction: No
- Spoken words (computed): 2876
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kahlil Gibran
Book: Treasured Writing of Kahlil Gibran
ISBN: 978-0890093894
Publisher: Castle Books
Date (Month/Year): Oct 2009
```

### Introduction (context only: never use it for content warnings)

```text
Father Samaan was well known in North Lebanon and most appreciated even in the remotest villages for his untiring preaching and curing people from the spiritual disease of sin, and saving them from the horrible trap of Satan, with whom he waged constant war. Satan by Kahlil Gibran tells how Father Samaan, on his way through a lonely valley, finds a deadly wounded stranger who turns out to be none other than Satan by Kahlil Gibran.
```

### Performance text (classify this)

```text
SATAN: Save me, help me. Have mercy on me, I am dying.

FATHER SAMAAN: This man must be a thief.... He probably tried to rob the wayfarers and failed. Someone has wounded him, and I fear that should he die I may be accused of having taken his life."

SATAN: Do not leave me! I am dying!"

FATHER SAMAAN: He must surely be one of the madmen wandering in the wilderness. The sight of his wounds brings fear into my heart; what shall I do? Surely a spiritual doctor is not capable of treating flesh-wounded bodies."

SATAN: Come close to me! Come, for we have been friends a long time.... You are Father Samaan, the Good Shepherd, and I am not a thief nor a madman.... Come close, and do not let me die in this deserted place. Come, and I will tell you who I am."

FATHER SAMAAN: Who are you?

SATAN: You know my identity! You have seen me one thousand times and you speak of me each day.... I am dearer to you than your own life." I am Satan.

FATHER SAMAAN: The hands which offer a daily sacrifice to God shall not touch a body made of the secretion of Hell.... You must die accursed by the tongues of the Ages, and the lips of Humanity, for you are the enemy of Humanity, and it is your avowed purpose to destroy all virtue.

SATAN: You know not what you are saying, nor understand the crime you are committing upon yourself. Give heed, for I will relate my story. Today I walked alone in this solitary valley. When I reached this place, a group of angels descended to attack, and struck me severely; had it not been for one of them, who carried a blazing sword with two sharp edges, I would have driven them off, but I had no power against the brilliant sword, The armed angel - I believe he was Michael - was an expert gladiator. Had I not thrown myself to the friendly ground and feigned to have been slain, he would have torn me into brutal death.

FATHER SAMAAN: Blessed be Michael's name, who has saved Humanity from this vicious enemy.

SATAN: My disdain for Humanity is not greater than your hatred for yourself.... You are blessing Michael who never has come to your rescue.... You are cursing me in the hour of my defeat, even though I was, and still am, the source of your tranquility and happiness.... You deny me your blessing, and extend not your kindness, but you live and prosper in the shadow of my being.... You have adopted for my existence an excuse and weapon for your career, and you employ my name in justification for your deeds. Has not my past caused you to be in need of my present and future? Have you found it impossible to extract more gold and silver from your followers, using my kingdom as a threat? Do you not realize that you will starve to death if I were to die? What would you do tomorrow if you allowed me to die today? What vocation would you pursue if my name disappeared? For decades you have been roaming these villages and warning the people against falling into my hands. They have bought your advice with the products of their land. What would they buy from you tomorrow, if they discovered that their wicked enemy no longer existed? Your occupation would die with me, for the people would be safe from sin. As a clergyman, do you not realize that Satan's existence alone has created his enemy, the church? Father, you are proud, but ignorant. I will disclose to you the history of belief, and in it you will find the truth which joins both of our beings, and ties my existence with your very conscience. In the first hour of the beginning of time, man stood before the face of the sun and stretched forth his arms and cried for the first time, saying, 'Behind the sky there is a great and loving and benevolent God.' Then man turned his back to the great circle of light and saw his shadow upon the earth, and he hailed, 'In the depths of the earth there is a dark devil who loves wickedness.' And the man walked toward his cave, whispering to himself, 'I am between two compelling forces, one in whom I must take refuge, and the other against whom I must struggle.' And the ages marched in procession while man existed between two powers, one that he blessed because it exalted him, and one that he cursed because it frightened him. But he never perceived the meaning of a blessing or of a curse. When man saw the dawn of civilization, which is human understanding, the family as a unit came into being. Then came the tribes, whereupon labour was divided according to ability and inclination; one clan cultivated the land, another built shelters, others wove raiment or hunted food. There was a man in the first tribe called La Wiss. He was an intelligent creature, but extremely indolent and he detested work in the cultivation of land, construction of shelters, grazing of cattle or any pursuit requiring body movement or exertion. And since food, during that era, could not be obtained except by arduous toil, La Wiss slept many nights with an empty stomach. One Summer night, as the members of that clan were gathered around the hut of their Chief, talking of the outcome of their day and waiting for their slumber time, a man suddenly leaped to his feet, pointed toward the moon, and cried out, saying, 'Look at the Night God! His face is dark, and his beauty has vanished, and he has turned into a black stone hanging in the dome of the sky!' The multitude gazed at the moon, shouted in awe, and shook with fear, as if the hands of darkness had clutched their hearts, for they saw the Night God slowly turning into a dark ball which changed the bright countenance of the earth and caused the hills and valleys before their eyes to disappear behind a black veil. At that moment, La Wiss, who had seen an eclipse before, and understood its simple cause, stepped forward to make much of this opportunity. He stood in the midst of the throng, lifted his hands to the sky, and in a strong voice he addressed them, saying, 'Kneel and pray, for the Evil God of Obscurity is locked in struggle with the Illuminating Night God; if the Evil God conquers him, we will all perish, but if the Night God triumphs over him, we will remain alive....Pray now and worship.... Cover your faces with earth.... Close your eyes, and lift not your heads toward the sky, for he who witnesses the two gods wrestling will lose his sight and mind, and will remain blind and insane all his life! Bend your heads low, and with all your hearts urge the Night God against his enemy, who is our mortal enemy!' Thus did La Wiss continue talking, using many cryptic words of his own fabrication which they had never heard. After this crafty deception, as the moon returned to its previous glory, La Wiss raised his voice louder than before and said impressively, 'Rise now, and look at the Night God who has triumphed over his evil enemy. He is resuming his journey among the stars. Let it be known that through your prayers you have helped him to overcome the Devil of Darkness. He is well pleased now, and brighter than ever.' The multitude rose and gazed at the moon that was now shining in full beam. Their fear became tranquility, and their confusion was now joy. They commenced dancing and singing and striking with their thick sticks upon sheets of iron, filling the valley with their clamour and shouting. That night, the Chief of the tribe called La Wiss and spoke to him, saying, 'You have done something that no man has ever done.... You have demonstrated knowledge of a hidden secret that no other among us understands. Reflecting the will of my people, you are to be the highest ranking member, after me, in the tribe. I am the strongest man, and you are the wisest and most learned person.... You are the medium between our people and the gods, whose desires and deeds you are to interpret, and you will teach us those things necessary to gain their blessings and love.' And La Wiss slyly assured, 'Everything the Human God reveals to me in my divine dreams will be conveyed to you in awakeness, and you may be confident that I will act directly between you and him.' La Wiss rose and started to leave, but the Chief stopped him, saying, 'Who and what is the one whom you call the Human God? Who is this daring God who wrestles with the glorious Night God? We have never pondered him before.' La Wiss rubbed his forehead and answered him, saying, 'My Honourable Master, in the olden time, before the creation of man, all the Gods were living peacefully together in an upper world behind the vastness of the stars. The God of Gods was their father, and knew what they did not know, and did what they were unable to do. He kept for himself the divine secrets that existed beyond the eternal laws. During the seventh epoch of the twelfth age, the spirit of Bahtaar, who hated the great God, revolted and stood before his father, and said, "Why do you keep for yourself the power of great authority upon all creatures, hiding away from us the secrets and laws of the Universe? Are we not your children who believe in you and share with you the great understanding and the perpetual being?' The God of Gods became enraged and said, 'I shall preserve for myself the primary power and the great authority and the essential secrets, for I am the beginning and the end.' And Bahtaar answered him saying, 'Unless you share with me your might and power, I and my children and my children's children will revolt against you!' At that moment, the God of Gods stood upon his throne in the deep heavens, and drew forth a sword, and grasped the Sun as a shield; and with a voice that shook all corners of eternity he shouted out, saying, 'Descend, you evil rebel, to the dismal lower world where darkness and misery exist! There you shall remain in exile, wandering until the Sun turns to ashes and the stars into dispersed particles!' In that hour, Bahtaar descended from the upper world into the lower world, where all the evil spirits dwelt. Thereupon, he swore by the secret of Life that he would fight his father and brothers by trapping every soul who loved them.' As the Chief listened, his forehead wrinkled and his face turned pale. He ventured, 'Then the name of the Evil God is Bahtaar?' And La Wiss responded, 'His name was Bahtaar when he was in the upper world, but when he entered into the lower world, he adopted successively the names Baalzaboul, Satanail, Balial, Zamiel, Ahriman, Mara, Abdon, Devil, and finally Satan, which is the most famous.' The Chief repeated the word 'Satan' many times with a quivering voice that sounded like the rustling of the dry branches at the passing of the wind; then he said, 'Why does Satan hate man as much as he hates the gods?' And La Wiss responded quickly, 'He hates man because man is a descendant of Satan's brothers and sisters.' The Chief exclaimed, 'Then Satan is the cousin of man!' In a voice mingled with confusion and annoyance, he retorted, 'Yes, Master, but he is their great enemy who fills their days with misery and their nights with horrible dreams. He is the power who directs the tempest toward their hovels, and brings famine upon their plantation, and disease upon them and their animals. He is an evil and powerful god; he is wicked, and he rejoices when we are in sorrow, and he mourns when we are joyous. And La Wiss left the Chief of the tribe and went to his retiring place, happy over his ingenuity, and intoxicated with the wine of his pleasure and fancy. For the first time, the Chief and all of the tribe, except La Wiss, spent the night slumbering in beds surrounded by horrible ghosts, fearful specters, and disturbing dreams." Thus divination came to this earth, and thus was my existence the cause for its appearance. La Wiss was the first who adopted my cruelty as a vocation. After the death of La Wiss, this occupation circulated through his children and perspired until it became a perfect and divine profession, pursued by those whose minds are ripe with knowledge, and whose souls are noble, and whose hearts are pure, and whose fancy is vast. In every city under the sun my name was the axis of the educational circle of religion, arts, and philosophy. Had it not been for me, no temples would have been built, no towers or palaces would have been erected. I am the courage that creates resolution in man.... I am the source that provokes originality of thought.... I am the hand that moves man's hands.... I am Satan everlasting. I am Satan whom the people fight in order to keep themselves alive. If they cease struggling against me, slothfulness will deaden their minds and hearts and souls, in accordance with the weird penalties of their tremendous myth.

I am the enraged and mute tempest who agitates the minds of man and the hearts of women. And in fear of me, they will travel to places of worship to condemn me, or to places of vice to make me happy by surrendering to my will. The monk who prays in the silence of the night to keep me away from his bed is like the prostitute who invites me to her chamber. I am Satan everlasting and eternal. I am the builder of convents and monasteries upon the foundation of fear. I build wine shops and wicked houses upon the foundation of lust and self-gratification. If I cease to exist, fear and enjoyment will be abolished from the world, and through their disappearance, desires and hopes will cease to exist in the human heart. Life will become empty and cold, like a harp with broken strings. I am Satan everlasting. I am the inspiration for Falsehood, Slander, Treachery, Deceit and Mockery, and if these elements were to be removed from this world, human society would become like a deserted field in which naught would thrive but thorns of virtue. I am Satan everlasting. I am the father and mother of sin, and if sin were to vanish, the fighters of sin would vanish with it, along with their families and structures. I am the heart of all evil. Would you wish for human motion to stop through cessation of my heartbeats? Would you accept the result after destroying the cause? I am the cause! Would you allow me to die in this deserted wilderness? Do you desire to sever the bond that exists between you and me? Answer me, clergyman!" I am tired and weak. I did wrong by using my waning strength to speak on things you already knew. Now you may do as you please.... You may carry me to your home and treat my wounds, or leave me in this place to die."

FATHER SAMAAN: I know now what I had not known an hour ago. Forgive my ignorance. I know that your existence in this world creates temptation, and temptation is a measurement by which God adjudges the value of the human soul. It is a scale which Almighty God uses to weigh the spirits. I am certain that if you die, temptation will die, and with its passing, death will destroy the ideal power which elevates and alerts man. You must live, for if you die and the people know it, their fear of hell will vanish and they will cease worshipping, for naught would be sin. You must live, for in your life is the salvation of humanity from vice and sin. As to myself, I shall sacrifice my hatred for you on the altar of my love for man.

SATAN: What an intelligent person you are, Father! Now we realize our need for each other. Come close to me, my brother; darkness is submerging the plains, and half of my blood has escaped upon the sand of this valley, and naught remains of me but the remnants of a broken body which Death shall soon buy unless you render aid."

NARRATOR: Father Samaan rolled the sleeves of his robe and approached, and lifted Satan to his back and walked toward home. In the midst of those valleys, engulfed with silence and embellished with the veil of darkness, Father Samaan walked toward the village with his back bent under his heavy burden. His black raiment and long beard were spattered with blood streaming from above him, but he struggled forward, his lips moving in fervent prayer for the life of the dying Satan.
```

---

## IC-0435: Scaramouche Jones

- Title: Scaramouche Jones
- Author (byline): Justin Butcher
- Work: Not specified
- Publisher: Methuen Publishing Ltd
- Publication date as stated: Sept 2003
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SCARAMOUCHE
- Teaser before the introduction: Yes
- Spoken words (computed): 1157
- Already set (do not supply): none

### Source block (context only)

```text
Author: Justin Butcher
ISBN: 978-0413772213
Publisher: Methuen Publishing Ltd
Date (Month/Year): Sept 2003
```

### Introduction (context only: never use it for content warnings)

```text
Orphaned, exiled and sold into slavery in a single day, Scaramouche’s life was always one of discord. He was apprenticed to a Latin-speaking African snake-charmer, rescued by an Italian homosexual prince and spent time with Gypsies selling shoes in Poland. But those are each stories of their own. Today’s tale is of Croatia . . . when Scaramouche, the strangely pale-faced child of a gypsy whore first became a clown. (Insert brief mime routine here)

Scaramouche Jones by Justin Butcher
```

### Performance text (classify this)

```text
*Scaramouche – (pronounced scare – a – moosh)

Scaramouche enters – an ancient clown with white face, red nose, wig, elongated slap shoes, baggy suit, etc. Slowly, balefully, he eyes the audience.

SCARAMOUCHE: (Pg 4) Allow me to introduce myself: Scaramouche Jones, Esquire – Clown . . . Englishman – or so I have always maintained, but thereby hangs a tale. Tonight is the last night of my life. As a million clocks strike midnight, I shall lay down my long and weary life. But before I go, indulge me by your attentiveness, my friends. Keep vigil with me and be rewarded with the Tale – and the Surrendering Up - of Scaramouche Jones.

SCARAMOUCHE: (Pg 27-30) [September 1, 1939] The day that Poland fell. I escaped Krakow and the fury of the blitzkrieg by a matter of hours, fleeing southwards through Romania, disguised as a monk, with no clear intent but to depart these troubled northern realms forever. I walked, hitched, clambered on to the backs of trains and buses, speaking Latin to anyone who spoke to me and hiding my snow-white face under my cowl for fear it should excite comment. I reached the Adriatic coast finally in Croatia, where I was prevented from boarding a ship bound for Egypt by Ustashi soldiers, unmasked as some sort of impostor and slung into the back of a military station wagon – crammed with men, women and children who all bore on their garments a yellow star.

The Nazi doctors could find nothing in their books of eugenic anthropology to account for the pristine whiteness of my face, but neither were they ready to believe that I was a thorough-bred Aryan, so they kept me alive as a curiosity that would bear further looking at, and gave me a job as a gravedigger at the concentration camp at Split.

My role in the ‘Final Solution’ was to dig mass graves, even in the bitterest winter when the shovel bent in the frozen earth, and then to stand by and watch as trailer-loads of dead bodies were u-ended into them. Sometimes presumably for the sake of variation, huge droves of living victims were herded to the edges of the pits and then machine-gunned into the ground.

However, the corpses arrived, whether by gas, bullet or malnutrition, my task was then to shovel white lime all over their contorted limbs and twisted faces – like the painting of so many clowns. So many clowns, millions of clowns – Jewish clowns, gypsy clowns, homosexual clowns, children clowns – all with white lime to cover their faces. It used to sting and burn horribly if you got it on your hands while you were shoveling it out of the sacks. [This] white mask (gestures to his face) was composed entirely of lime, the pain of which has never left me.

An extraordinary thing happened: I discovered a certain facility for making children laugh . . . yes . . . when those ranks upon ranks of frightened, worn-down people were lined up for the machine-gun squads, naked and shorn, one by one the children began to catch sight of me with my funny white face, leaning on my shovel, waiting to resume my work . . . and I would (in words and in pantomime) wink at them, pull faces, laugh hugely without a sound, cavorting and making fun of the guards behind their backs, acting out a silent pantomime of the execution that was about to take place, pretending to be a victim gunned down, falling down into the pit and having my face painted white, then rising, fluttering on angel’s wings, up into heaven.

I got caught fooling around in this way plenty of times and my punishments were far from pleasant, but it seemed to me a price worth paying, to see those haunted little faces fixed on mine as they waited for the end . . . and sometimes, just sometimes, one of them would almost break into a smile before the bullets ripped into them from behind and they toppled down, down, down and beyond the reach of pain or fear for evermore. And so the common euphemism for extermination in our camp became not going to the showers, or going for a haircut, but ‘going to see the clown’.

This . . . honing of my training lasted until the Allied invasion of Italy, when the Germans fled, leaving me the sole proprietor in our particular establishment, leaning on my shovel at the edge of the last empty pit. I had dug it the day before for the last batch of surviving prisoners who were, as it turned out, saved by the bell. I was locked up, not surprisingly, for complicity in war crimes and there, in Spandau Prison, I mouldered, enduring the worst torments of boredom imaginable – having to listen to the interminable self-justifying raving and poisonous rhetoric of my fellow prisoners.

They talk about the death penalty these days; I’ve got a much better idea – take your condemned man and stick him in a cell with an old Nazi for seventeen hours a day and he’ll wish he bloody well had been hanged.

My reprieve came in 1951, when my case, among others, was re-examined in the light of some of the stories the survivors of the camps were beginning to tell for the first time. The Hon. Justice Percy Rawlins, informed me that he had become intrigued by a particular clutch of testimonies regarding the ‘white-faced gravedigger of the camp at Split.’ Was I really the concentration camp clown whose antics had kept fear at bay for so many holocaust victims?

I muttered that yes, I had tried to make the little ones laugh before they . . . He was flabbergasted and asked me how, how had I done it? And so, standing in the dock at Nuremberg, I performed for him the Mime of the Comic Execution. (performs the mime he used for the children)

He remained silent for some time. ‘It would sem that, in your own way, you have been of some service to humanity. You have been wrongfully imprisoned and shall receive your liberty forthwith. You are free to go.’ (Pg 33-34) I purchased a pot of Leichner face paint and daubed on my final white mask – a magical poultice, a soothing salve to be applied and re applied like a dressing, night after night, year after year, in the dressing room of a clown. And I painted my smile indelibly into the white-scarred tissues of my face, like a wound. All that remained was to stitch the aperture with sutures strong enough to withstand the rigors of another fifty years of . . . . buffoonery. The threat of my life proved admirably handy and, in a matter of moment, my lips – along with my face – were sealed. And from that day forth and for the next fifty years, I never opened my mouth again.

So now you know . . . fifty years to make the clown, fifty years to play the clown. And now, I feel unmasked at last . . . I might dare say . . . almost free. (Pg 26) “Though your sins be as scarlet, yet shall they be as white as snow.” [Isiah 1:18]

(Performs one final “good-bye” mime)
```

---

## IC-0436: Scooter Thomas makes it to the Top of the World

- Title: Scooter Thomas makes it to the Top of the World
- Author (byline): Peter Parnell
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DENNIS, DAD, SCOOTER, WALLY, EDDIE, MR. GREENBAUM, SCOOTER’S FATHER
- Teaser before the introduction: Yes
- Spoken words (computed): 2016
- Already set (do not supply): none

### Source block (context only)

```text
Author: Peter Parnell
ISBN: 978-0822210009
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
We all knew somebody like Scooter Thomas: the kid who was always getting called to the principal’s office, who sassed the PE coach in junior high, the rebel, the outsider. The risk-taker who we all secretly wanted to be a little more like.

But teen-age rebels can have trouble adapting to the realities of adulthood. You see, our childhood is something we carry with us for the rest of our lives – the lessons learned, the relationships built or discarded. Its these experiences that shape us into the adults we become.

Scooter Thomas Makes it to the Top of the World by Peter Parnell
```

### Performance text (classify this)

```text
DENNIS: The call came in only a few hours ago

DAD: (Both on phone) Hello, son.

DENNIS: What’s the matter?

DAD: Don’t worry, Dennis. It’s not any of us – It’s your friend, Scooter.

DENNIS: Scooter Thomas, Scoots? But he’s in California (Pause) Oh, God, no . . . . (Put down phone) (Begins packing a suitcase – talks to audience) How many of you out there would like to receive a phone call from your dad telling you that your best friend in high school, whom you grew up with (Close suitcase) has just killed himself. And you’re expected to drive all night to be a pallbearer at a service taking place in, oh, less than twenty-four hours time? It’s funny, like – no matter how hard you try to just get on with it, other things keep coming back. It isn’t just stories, or names, or . . . or faces . . . it’s . . . it’s . . . this incredible sense of emptiness – you know? I guess it’s just knowing I’ll never see him again that’s really the most upsetting thing of it all. I guess what I’m really trying to tell you about is what happened between us – Scooter and me. That is . . . because (Start pacing to the side) well . . . it’s something that’s been on my mind since this afternoon . . . .

SCOOTER: Psst! Tell them how I made it.

DENNIS: Scoots?

SCOOTER: Tell them how I . . .

DENNIS: Scooter, for God’s sake, what are you doing here?

SCOOTER: . . . made it to the top of the world.

DENNIS: What do you mean?

SCOOTER: I made it, Dennis. Don’t you understand? When it happened. You’re not going to leave out the most important part! Wally would have been proud of me.

DENNIS: (to audience) Scooter’s older brother. Now a corporate lawyer in Washington.

WALLY: Let’s not take the children, dear. It’s not an important affair. Just my kid brother, Scooter, who never could manage to . . .

DENNIS: Look, I realize you and he were never the closest of friends, but that’s no reason at this late date for you to start in. And what kind of stupid thing was that to do anyway? Go mountain-climbing all alone and then jump.

SCOOTER: I couldn’t find anyone else to go with. (Dennis pulls something out of his pocket and hands it to Scooter). The picture I sent you from Yosemite! I forgot about that. (slowly) Cathedral Peak! Dennis, that’s the mountain I . . .

DENNIS: Yeah. That’s what I figured. You and your mountains.

SCOOTER: Hatch’s Cliff.

DENNIS: What?

(SCENE – FLASH BACK TO WHEN THEY ARE 10-YEARS-OLD)

SCOOTER: On your mark, get set . . .

DENNIS: Last one to the top is a rotten . . . (Flash to the edge of the cliff) Lookit how high we are!

SCOOTER: Wanna jump into the water?

DENNIS: We can’t, Scoots – we’re too high up. Think anybody’ll find us?

SCOOTER: Nobody even knows we’re up here. You didn’t tell anyone didja?

DENNIS: Uh-uh.

SCOOTER: Me either.

DENNIS: Look, nobody’s got know about this place, okay? It’ll be our secret hiding place, okay.

SCOOTER: Promise? (Start to shake hands) Wait! (Scooter produces a knife from his pocket and cuts his hand open, then hands the knife to Dennis).

SCOOTER: Got it?

DENNIS: What do we say?

SCOOTER: I dunno, blood brothers? (Holds out hand)

DENNIS: Blood brothers (Holds out hand)

(SCENE – FLASH TO WHEN THEY ARE 13-YEARS-OLD (at school desks))

DENNIS: (Whispers) Oh geezo, geez. What’s the capital of Peru?

SCOOTER: (Whispers) It’s Lima

DENNIS: (Whispers) When did Columbus discover America?

SCOOTER: (Whispers) 1492

DENNIS: (Pause – still whispering) How come you know all this stuff, anyway? (Scooter holds out his hand where he has written all the answers) You can’t do that, that’s cheating!

SCOOTER: Relax. I’m going to wash it off.

DENNIS: You better. If Miss Palmer ever found out . . .

SCOOTER: She won’t. (Pounds fist and grinds it in, wiping off the answers) Will she?

(SCENE – POP TO DENNIS AS EDDIE MARCUS – SCOOTER’S BROTHER’S BEST FRIEND)

EDDIE: Psst! Hey, Scooter!

SCOOTER: Eddie, whadda you doin’ here? You cutting’ class in high school? Is Wally goin’ with ya?

EDDIE: He’s waiting outside –

SCOOTER: Oh, boy. I’m coming too!

EDDIE: N-O!

SCOOTER: I’ll tell my dad that you an’ he . . .

EDDIE: (Slaps Scooter) Just shut up, ya little moron, Okay!?! Nobody’d want to go drivin’ with you! You’re just Wally’s kid brother, ya little creep!’

SCOOTER: (to audience) He really got me angry when he said that. About me being Wally’s kid brother. I mean, who did he think he was?

(SCENE – POP TO SCENE WITH MR. GREENBAUM – 8th GRADE)

MR. GREENBAUM: . . . . Well, the nurse seems to think you might have even broken one of his ribs.

SCOOTER: Sorry, Mr. Greenbaum, sir.

MR. GREENBAUM: Let me tell you something, Scooter. You are a very bright, young boy. You could go far. But when will you learn to follow instructions? Eighth grade isn’t the end of the line.

SCOOTER: I didn’t start that fight, Mr. Greenbaum.

MR. GREENBAUM: But you certainly finished it, didn’t you?

SCOOTER: I’m just my brother Wally’s kid brother.

MR. GREENBAUM: Then why don’t you start acting like him, young man? Wallace was always one of my favorite students. He’ll be a tough man to follow – even beat.

SCOOTER: Then I won’t plan on trying, sir.

MR. GREENBAUM: I bet you must think you’re pretty funny, don’t you?

SCOOTER: Not especially, sir.

MR. GREENBAUM: Oh, yes. I think you think you’re very funny. Well, let me tell you something, Scooter Thomas: You may find yourself dead before you’re thirty, with the way you’re going. And that would be just about the un-funniest thing of all.

(SCENE – POP TO BOTH BOYS ON HATCH’S CLIFF – SCOOTER is sitting down, throwing rocks over the edge)

DENNIS: Hey there! Didn’t you hear me? I kept calling and calling down there. Nobody knew where you were . . . figured I’d try Hatch’s Cliff. Why weren’t you at practice.

SCOOTER: I didn’t even know there was one.

DENNIS: Whaddya talkin’ about. I told ya yesterday.

SCOOTER: So maybe I forgot.

DENNIS: Did Razorhead send you to Brownstein again?

SCOOTER: Yeah.

DENNIS: Look, I’m sorry I didn’t raise my hand or anything when he asked who else . . . I mean, I wanted to go up to him after . . . I really did.

SCOOTER: He likes you. He wouldn’t have gotten mad.

DENNIS: No, he’d have remembered from the last time . . . when we put chalk in his erasers.

SCOOTER: Yeah, what did he say?

DENNIS: (mocking Mr. Greenbaum) I’m very disappointed in you, Dennis. Associating yourself with the likes of Scooter Thomas. I should think you’d be embarrassed . . .

(Realizes he should not have said that. Scooter stands and throws a rock hard) Yeah

(SCENE – POP TO AGE 16 – and throwing a football)

DENNIS: Margery Matthews?

SCOOTER: About a 6 (Throws ball)

DENNIS: Betsy Hamilton? (Throws ball)

SCOOTER: 4 . . . on Fridays a 5. (Throws ball)

DENNIS: Amy Lewis? (Throws ball) . . . Amy Lewis . . . . Scooter, Amy Lewis. Scooter are you in love with . . .

SCOOTER: What the hell kind of a lousy, stupid, moron thing is that to ask me, Dennis?

(Throws ball).

DENNIS: I just wanted to know, that’s all.

SCOOTER: Why? So you can go around and tell every idiot you see that it’s true? Well, you can tell all those idiots anything you like.

DENNIS: (Throws ball down) What’s that supposed to mean?

SCOOTER: It means . . . I just don’t think it’s that big a deal, that’s all.

DENNIS: I suppose you think you could go all the way the first time out or something, huh? Huh?

SCOOTER: Yeah, well. Maybe I could. (DENNIS exits – Scooter paces back and forth and talks to unseen girl off stage front) What have I gotten myself into . . . Are you still out there? I understand if you don’t want to come out. Look, I just want you to hear what I have to say. I never woulda tried to do what I did with you if it hadn’t been for a stupid, crazy, insane bet I made six weeks ago with my idiot friend Dennis Wright. Anyway, I’m sorry I tried to put my tongue down your throat. I’m even sorrier it missed and got stuck in your braces. It wasn’t too pleasant for me either. I hope we can still be friends . . . Okay?

(SCENE – POP TO AGE 17 – Scooter is in a car)

DENNIS: Scoots, where have you been?

SCOOTER: (Hands on the wheel) C’mon, Dennis, get in the car.

DENNIS: (Gets in the car and they are moving) Scoots, are you drunk again?

SCOOTER: Smashed, buddy, ol’ pal of mine.

DENNIS: The guys and I waited all night for you to show.

SCOOTER: To the stars. Tonight I have been to the . . . you can put me right up there with the Big Dipper . . .

DENNIS: Listen, maybe I better drive. Remember what your parents . . . You’ve already nearly wrecked the car once . . . (Watches stop sign go by) Scoots – you just missed that stop sign!

SCOOTER: Was I supposed to hit it?

DENNIS: No, you were supposed to stop!

SCOOTER: Wanna honk the horn?

DENNIS: Jesus Scoots, you’ll wake up the whole . . . WATCH OUT!

SCOOTER: Ooooooh, we almost went over the cliff.

(SCENE – POP TO AGE 18 – playing poker)

DENNIS: Harvard.

SCOOTER: What about Yale?

DENNIS: Too tough.

SCOOTER: Dartmouth?

DENNIS: Too cold. Nobody’s applying to . . . Listen Scoots, your Dad’ll let you drive your car again soon. And anyway, after a year at home, once you pick up your grades, you’ll be able to transfer.

SCOOTER: To where?

DENNIS: Umm . . . well . . . You can visit me on weekends.

SCOOTER: It won’t be the same.

DENNIS: It’ll be cool . . . You still seeing . . .

SCOOTER: Carol? Yeah. I go over a lot. She says “hi.”

DENNIS: Say “hi” to her back. She like you.

SCOOTER: I like her.(Scooter exits)

DENNIS: (to audience) So, I didn’t see much of him the rest of that summer. Not because . . . I don’t know, I was busy working or something. I suppose it was about a year later that Scooter dropped out of college. I never did find out. It wasn’t until I went home one vacation that I ran into him working behind the post office counter that I found out. And then . . . it was sometime the following fall . . . he wrote me about this fight he’d had with his father - see . . .

(SCENE)

SCOOTER’S FATHER: What the hell you doing sleeping all morning? Come on, get up and get out of it . . .

SCOOTER: Dad, it’s Saturday for Christ sakes.

SCOOTER’S FATHER: What’s this all about? A letter from the mental clinic of Boston Hospital. It arrived this morning. A bill for psychiatric services, it says, fifty dollars. Fifty bucks!

SCOOTER: Dad, that letter was addressed to me, you had no right . . .

SCOOTER’S FATHER: No right? A letter to my son from a looney bin and I’m not supposed to know about it? Well, I’m not gonna pay for it if you think . . .

SCOOTER: I had to go in for a check-up . . .

SCOOTER’S FATHER: What kind of a . . . . in your head?

SCOOTER: Yes!

SCOOTER’S FATHER: What was it . . . stuck up your ass?

SCOOTER: I got into a fight with somebody last month. When I went to Boston with Carol, remember? She was going out with this other buy from B.U. and . . .

SCOOTER’S FATHER: Oh, I get it. And you just tagged along. You told us you were both going to visit Dennis. But instead you followed her to Boston and . . .

SCOOTER: I couldn’t help it, Dad. Carol, she lets this guy treat her so bad . . . and I . . . I love her . . . I really do!

SCOOTER’S FATHER: Love her? You love her? You don’t know the first thing about love. Love means responsibility. It means being an adult, which you don’t know the first thing…

SCOOTER: Look . . . just leave me alone, okay!?! Just go screw yourself!

(SCENE – POP TO AGE 26)

DENNIS: Hey, it’s really nice up here, you know? I’m glad you suggested we . . . I haven’t been on top of Hatch’s Cliff since . . . Jesus, must have been over a year ago. Yeah . . . you still seeing . . .

SCOOTER: On and off, yeah.

DENNIS: What’s she been doing?

SCOOTER: Getting married.

DENNIS: Oh, really? To that . . .

SCOOTER: Yeah . . . it’s just the way it is.

DENNIS: Yeah.

SCOOTER: I’ve been thinking about going out to the west coast.

DENNIS: You mean to visit?

SCOOTER: Maybe to live. To get out there and . . . I don’t know. Start sort of a new life for myself. I know you don’t think it’s a good idea.

DENNIS: What? No. I think it’s fine. Great. But, have you thought about maybe going back to school . . .

SCOOTER: I know you think I’m being irresponsible. You think I can’t do it.

DENNIS: No . . No . . . I didn’t say . . . I just thought if maybe you went back to school . . .

(SCENE – PRESENT DAY – DENNIS IS BACK TO PACKING HIS SUITCASE)

SCOOTER: Every time you asked me a question, you didn’t have to judge me . . .

DENNIS: Scooter. . . For Christ . . . I did not . . .

SCOOTER: Face it, man, you did!

DENNIS: Look. If you want to know what really made me judge you, it was all the silly little games you were playing, okay? The whole smug routine. Never telling me at all what was really going on inside your head . . . For Christ’s sake, Scooter. I was your friend!

SCOOTER: Friend, yeah! Just like Mom and Dad and Wally and Eddie and Greenbaum and Carol and all those other . . . all the rest . . . who spent so much time telling me how to live my life they wouldn’t even let me breathe . . .

DENNIS: Look, you’re not even here – You’re dead – so just GO AWAY! I won’t be made to feel responsible! Just because you . . . Oh, God . . .

SCOOTER: (Now he gets it . . . your work here is done) I think it’s time for me to get going.

DENNIS: I’m sorry, Scooter. If I did judge you, I . . . people grow older. Change. Maybe it was meant to be . . . maybe it was my fault, I . . . I had to move on . . . Say, Scoots? Listen, I . . . I hope you found what you were looking for. Up there.

SCOOTER: Found what I . . . Oh, yeah, Dennis. I did. I mean, I made it up, didn’t I? And then, somehow it all suddenly . . . well, finally began to make sense. I got to go now.

DENNIS: I know, Scoots. I know.

SCOOTER: See ya, pardner. (Exits)

DENNIS: See ya, Scooter (Dennis returns to packing then hears Scooter’s voice echo in his memory once more)

SCOOTER at 10: Nobody even knows we’re up here. You didn’t tell anyone, didja?

DENNIS as ADULT: (Hesitates at first) Uh-uh. Look, nobody’s gotta know about this place, okay? It’ll be our secret hiding place.

SCOOTER at 10: Promise . . . Wait! (Hold up hand and traces the scar from the blood brother pact) Got it?

DENNIS: Yeah. What do we say?

SCOOTER: I dunno. Blood brothers?

DENNIS: (Slowly brings his hand up in the air) Blood brothers.
```

---

## IC-0437: She Walked Alone

- Title: She Walked Alone
- Author (byline): Daisy Bates
- Work: Long Shadow of Little Rock
- Publisher: University of Arkansas Press
- Publication date as stated: June 1987
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 972
- Already set (do not supply): none

### Source block (context only)

```text
Author: Daisy Bates
Book: Long Shadow of Little Rock
ISBN: 0938626744
Publisher: University of Arkansas Press
Date: June 1987
```

### Introduction (context only: never use it for content warnings)

```text
Dr. Benjamin Fine was then education editor of The New York Times. He had years before won for his newspaper a Pulitzer prize. He was among the first reporters on the scene to cover the Little Rock de-segregation story.

A few days after the National Guard blocked the Negro children's entrance to the school, Ben showed up at my house. He paced the floor nervously, rubbing his hands together as he talked.
```

### Performance text (classify this)

```text
"Daisy, they spat in my face. They called me a 'dirty Jew.' I've been a marked man ever since the day Elizabeth tried to enter Central. I never told you what happened that day. I tried not to think about it. Maybe I was ashamed to admit to you or to myself that white men and women could be so beastly cruel.

"I was standing in front of the school that day. Suddenly there was a shout-- `They're here! The niggers are coming!' I saw a sweet little girl who looked about fifteen, walking alone. She tried several times to pass through the guards. The last time she tried, they put their bayonets in front of her. When they did this, she became panicky. For a moment she just stood there trembling. Then she seemed to calm down and started walking toward the bus stop with the mob baying at her heels like a pack of hounds. The women were shouting, 'Get her! Lynch her!' The men were yelling, 'Go home, you bastard of a black bitch!' She finally made it to the bus stop and sat down on the bench. I sat down beside her and said, `I'm a reporter from The New York Times, may I have your name?' She just sat there, her head down. Tears were streaming down her cheeks from under her sun glasses. Daisy, I don't know what made me put my arm around her, lifting her chin, saying, `Don't let them see you cry.' Maybe she reminded me of my fifteen-year-old daughter, Jill.

"There must have been five hundred around us by this time. I vaguely remember someone hollering, `Get a rope and drag her over to this tree.' Suddenly I saw a white-haired, kind-faced woman fighting her way through the mob. She looked at Elizabeth, and then screamed at the mob, `Leave this child alone! Why are you tormenting her? Six months from now, you will hang your heads in shame.' The mob shouted, `Another nigger-lover. Get out of here!' The woman, who I found out later was Mrs. Grace Lorch, the wife of Dr. Lee Lorch, professor at Philander Smith College, turned to me and said, `We have to do something. Let's try to get a cab.'

"We took Elizabeth across the street to the drugstore. I remained on the sidewalk with Elizabeth while Mrs. Lorch tried to enter the drugstore to call a cab. But the hoodlums slammed the door in her face and wouldn't let her in. She pleaded with them to call a cab for the child. They closed in on her saying, `Get out of here, you bitch! Just then the city bus came. Mrs. Lorch and Elizabeth got on. Elizabeth must have been in a state of shock. She never uttered a word. When the bus pulled away, the mob closed in around me. `We saw you put your arm around that little bitch. Now it's your turn.' A drab, middle-aged woman said viciously, `Grab him and kick him in the balls!' A girl I had seen hustling in one of the local bars screamed, `A dirty New York Jew! Get him!' A man asked me, `Are you a Jew?' I said, `Yes.' He then said to the mob, `Let him be! We'll take care of him later.'

"The irony of it all, Daisy, is that during all this time the national guardsmen made no effort to protect Elizabeth or to help me. Instead, they threatened to have me arrested--for inciting to riot."

Elizabeth, whose dignity and control in the face of jeering mobsters had been filmed by television cameras and recorded in pictures flashed to newspapers over the world, had over-night become a national heroine. During the next few days newspaper reporters besieged her home, wanting to talk to her. The first day that her parents agreed she might come out of seclusion, she came to my house where the reporters awaited her. Elizabeth was very quiet, speaking only when spoken to. I took her to my bedroom to talk before I let the reporters see her. I asked how she felt now. Suddenly all her pent-up emotion flared.

"Why am I here?" she said, turning blazing eyes on me. "Why are you so interested in my welfare now? You didn't care enough to notify me of the change of plans--"

I walked over and reached out to her. Before she turned her back on me, I saw tears gathering in her eyes. My heart was breaking for this young girl who stood there trying to stifle her sobs. How could I explain that frantic early morning when at three o'clock my mind had gone on strike?

In the ensuing weeks Elizabeth took part in all the activities of the nine--press conferences, attendance at court, studying with professors at nearby Philander Smith College. She was present, that is, but never really a part of things. The hurt had been too deep.

On the two nights she stayed at my home I was awakened by the screams in her sleep, as she relived in her dreams the terrifying mob scenes at Central. The only times Elizabeth showed real excitement were when Thurgood Marshall met the children and explained the meaning of what had happened in court. As he talked, she would listen raptly, a faint smile on her face. It was obvious he was her hero.

Little by little Elizabeth came out of her shell. Up to now she had never talked about what happened to her at Central. Once when we were alone in the downstairs recreation room of my house, I asked her simply, "Elizabeth, do you think you can talk about it now?"

She remained quiet for a long time. Then she began to speak.
```

---

## IC-0438: Shell Game with Organs

- Title: Shell Game with Organs
- Author (byline): Jacob M. Appel
- Work: Boston Review
- Publisher: Boston Review
- Publication date as stated: Dec 98/Jan 99
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2204
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jacob M. Appel
Book: Boston Review
ISBN: 07342306
Publisher: Boston Review
Date (Month/Year): Dec 98/Jan 99
```

### Introduction (context only: never use it for content warnings)

```text
Presented in the tone of a Great Magicigan, with lots of bravado and Thanks to the wonders of modern medicine, anyone who shares a blood type can share a kidney: Body magic -- A shell game with organs. Three nights in the hospital and I'd have my girlfriend off dialysis for life. Not to mention that second kidney wasn't doing me any good where it was. So why was this magic trick so much more difficult that all the others I’d performed as the Great Santini? Shell game with Organs by Jacob M. Appel
```

### Performance text (classify this)

```text
Houdini urges me to disappear again. That's his panacea, his sovereign remedy. If he had his way, I'd vanish into thin air one night without a trace. On Lois, on mother, on him. And I suppose that would suit the old fellow just fine, too. The building crew would sniff him out eventually--find him belly-up on the carpet, caked in is own excrement, his kingdom lost for want of a saltine. Even then he'd be croaking "Disappear" through parched lips, I imagine. Houdini squeezes shut his onyx eyes, raises his wings to his cheeks. His voice is urgent. "Disappear! Disappear!"

"Shut up!"

Three hours straight I've debated alternatives, judged and unjudged myself. I don't have to visit mother. I don't have to play the shell game with organs. After tonight's show I could stow my equipment in the back of the truck and relocate to New York. Or rural Mauritania. A magician pulling off a disappearing act. Nothing could be more natural.

Already I despise myself for shouting at him and I feed him a chocolate-coated wafer. He clasps the treat in his beak, slides it down his gullet with a tilt of his head. At least I can please someone, I think. So what if the snacks cause parrot cancer.

"What do you say we ditch mother and Lois and head off to Africa--just the two of us?"

"Disappear," Houdini retorts ambiguously, "Disappear." His vocabulary--the product of a magic routine we once did together--is frozen in time like a dead language.

Lois interrupts our conversation, struts in through the open door. Her heels pummel the hardwood in the foyer. We've been dating for almost a month now--which at forty-one means we're serious, that we know each other well--and still her vigor astounds me afresh at every meeting. She's so put-together, so fast-paced. She bounces through life like a wired kangaroo. If you saw her behind the counter at the crafts shop, you'd think she had kidneys.

We don't discuss the organ shell game on the way to Mass General. It's like a marriage proposal; it demands a yes or a no.

"I wish I could borrow one," she’d said last night

"I wish you could too."

The words reached my brain seconds after they left my lips. Before I could decide whether I meant them--abstractly, of course--Lois had bombarded me with this "emotional donor" business. She revealed that, thanks to the wonders of modern medicine, anyone who shares a blood type can share a kidney: Emotion is now thicker than blood.

"Body magic," she called it. "A shell game with organs." Three nights in the hospital and I'd have her off dialysis for life. Not to mention which, she added, the second kidney wasn't doing me any good where it was.

Lois made it sound as though she'd be doing me a favor: Relieving weight from my abdomen, giving my liver room to grow. She could have been a "Let's Make a Deal" contestant selecting Kidney #2. No emotional blackmail, no hang-dog looks. And that's probably why I like her. She's the only woman I've ever met who could compare invasive surgery to a sleight-of-hand.

" Mother still wants me to kill her. . . . Did you hear me?" I ask Lois. "She keeps making that sign with her hands. Like she's trying to silence a stranger or slaughter a chicken."

"You don't know what she means by it," says Lois.

"She's my mother," I say irritably. "I can tell. How am I supposed to concentrate tonight with all this to think about--with mother slicing her throat with her finger?"

Lois doesn't add, "And with your girlfriend begging for an organ handout." Most women would do that. At least most of the women I've dated. Instead, Lois says, "That's your problem. You're the magician."

So we drive in silence, sensing that last night has changed us: She has broached the kidney question and now it hangs over our relationship like some kind of love test.

I feel the need to argue my case again: That the magician's life does not easily permit this sort of commitment. Implicit for me, if not for her, is that the kidney and commitment questions are bound together like the sleeves of a straight jacket.

"I want you to speak with Dr. Sandkirk," says Lois. We're in the pay parking garage at the hospital; each minute of protest will add to the meter.

"Dr. Sandkirk," is all I answer.

"Yes, Dr. Sandkirk. The nephrologist."

Then we part ways, the echo of Lois's steps reverberating against the concrete. Her dialysis treatments permit me four hours alone with my mother.

Mother greets me from bed with a salvo of, "Late trees under water and each one has his own." That's the retired English teacher poking through, her speech without content yet impeccably grammatical. It's hard to imagine that a month ago, before the stroke, she was organizing Grey Panthers for a library boycott.

"Hi, Mom," I say, dropping a dry kiss on her leather cheek. "Bet you didn't think I was coming. "

"Late, late trees under water and each one has his own," she retorts. Her voice is weary, reproving. Her face looks fractured down the center and glued back together like a broken vase. When she speaks, the words bend around the comer of her mouth. She frowns at me and adds, emphatically, "Or her own."

I find myself ready to shake her like an appliance on the blink. What right does she have to speak gibberish, to abandon me just when I've returned home for good? All those years on the road turning face cards into flowers, all those late night phone calls from Peoria and Yazoo City--and when I finally have a Boston gig, a sold-out debut in less than eight hours, the one person I thought I could depend on mutters, "Pills stock knowing that nurse, yes, yes," as though it were a schoolgirl's secret in need of release.

"Lois wants my kidneys," I finally say. "Well not both of them," I explain. "Only one."

In response, my mother slides her index finger across her jugular vein and closes her eyes. Her tongue falls from her mouth, her head sinks into the hospital pillows. There is no mistaking her meaning.

"I can't do that, Mother," I answer as I take her small hand in my large one. "Do you understand me? You know I can't do that. I can't. Besides, you'll be out on the picket lines in no time."

Mother opens her eyes, examines me with the wonder of a child. The doctors say the words go in with as little sense as they come out. My mother will never picket the library again, much less read a book. She is seventy-six years old. If we are lucky, chirps the underage rehabilitation therapist, she'll be able to count to ten and recite the days of the week within a year.

"Lois wants one of my kidneys," I say again. I produce a photograph from my wallet, point at Lois and then at my stomach. "Do you understand, Mother? Kid-ney. " To emphasize my claim, I draw a lima bean in the air with my finger.

My mother examines the photograph carefully and frowns in confusion. It is no use. I know the whole situation is untenable. Cruel, even. She has lost her vocabulary, her memories. And she has lived too hard, too earnestly, to squander her final years distinguishing Mondays from Wednesdays.

"I have to go now, Mom. I have a show tonight. My Boston debut. I'm going to escape from chains and a straight jacket in an underwater tank."

"Either nurse or trees," she retorts vehemently. "Neither nurse nor trees."

Somehow this means that she's angry I will not kill her. Angry she doesn't have the strength, the means, to do it herself.

My cheek is wet when I press it against hers. Then I draw back her hair, brush the purple-grey strands into place, plant my lips on her forehead.

"Hang in there," I say. "Hang in there, Mom."

My mother leans forward in her bed, reaches out toward me with ghost-walk arms. I retreat rapidly to the lobby, to the small alcove of vending machines and pay telephones.

The wall clock reminds me that I still have three hours to kill, so I collapse into a vinyl chair, my mind blank, and absorb the soothing murmur of the electronic ice maker.

"Rip Van Winkle returns," says Lois, startling me from my slumber. "Your twenty years are up, Rip. Time to find out who's dead and who's alive. Dr. Sandkirk doesn't have all day."

Sandkirk defies my expectations. He has small round eyes, matching small round glasses. His head slopes from a broad brow to a narrow, almost inverted chin. All in all, he resembles a giant radish. So this is the celebrated nephrologist! I'd anticipated a full, glowing figure in a giant kidney costume, a man not unlike the human peach in the Fruit of the Loom underwear commercials.

Sandkirk steers me to another vinyl chair. His wall biography tells me everything I need to know. He's a Princeton graduate, a champion Little League coach, a Fellow of the American College of Physicians. All of this indicates a man with connections: One whose absence would be noted if I made him disappear.

Sandkirk says, "So, you're thinking about donating a kidney."

"Thinking about it," I say. "Only thinking."

"That's good, Mr. Sternberg. I'd be the first to warn you against a hasty decision. Because there are risks, you understand.” He outlines the advantages and drawbacks of the emotional donor. Lois listens attentively, glances at me periodically through the corners of her eyes. Sandirk narrates my recovery from post-op stitching to outpatient check-ups. After fifteen minutes, he has me feeling as though the entire procedure is as easy as a card trick. Nothing more than a shell game with organs.

"Of course I'll need some blood," the nephrologist concludes. "We need to confirm blood types and check for antibodies. Lois says you're both O-positives. Now roll up your sleeve."

He's rummaging through his filing cabinet for a needle when I stand up to excuse myself "I'll think about it, Sandkirk," I offer. "But no blood. Not now. I have a show tonight."

"What was that about'?" I demand as soon as we've escaped.

"What do you mean?"

"I mean that guy's knife-happy. I'm lucky he didn't do it right there on his desk with a scissors. "

Lois laughs. A short, sharp laugh. She asks, "So is that your answer?"

"I'm thinking," I say. "Still thinking."

I'm tired of doctors, tired of hospitals. I find myself wishing that mother would die and give Lois the kidney--and then I despise myself for the thought. That's not a solution. Not a realistic solution, at least. Vanishing, on the other hand, has a lot to be said for it. Almost too much to be said for it. Who'd miss me? I don't coach little league; I didn't go to Princeton. My alma mater, the exalted Garfield School of the Arts, went bust in the early 80s. The only two people who'd notice, who'd really notice, are Lois and mother--and with mother I don't really know. So there's only Lois. Lois. And, of course, Houdini. But Houdini's actively urging me to disappear.

"Disappear!" I call into the empty apartment. I pause at the kitchen table to sort through the afternoon's mail. "Isn't that right, Houdini? Disappear!"

But it's Houdini who's taken his own advice and gone belly-up on the floor of his cage. I stare at him in disbelief, but there is no disbelieving: Circles of blood ring his onyx eyes.

I shout at him. "I warned you about those parrot treats. A thousand times I warned you. Just because you have a brain the size of a pea doesn't give you a right to have a parrot aneurysm on the night of my debut.

Twenty-five years I've had Houdini. Loved Houdini. Twenty-five years. He was my best friend, my brother.

"You stupid, stupid bird," I repeat as I cradle his lifeless body in my arms. I can still feel his warmth through the feathers. "Stupid, stupid bird."

It's two hours later when I ring the one-armed super for a cardboard box. I wrap Houdini in his aquamarine towel and plant one final kiss on his tufted head. Good bye, old fellow. Good bye, old bird.

After phoning the theater to inform them that there's been a death in the family, I carry Houdini's coffin to the car. Then I drive out to Mass General, to be with my mother. Not to kill her, but to be with her. Tomorrow, I know, I must end things with Lois. But tonight, a middle-aged escape artist on the way to bury my closest friend, I feel the need to listen to my mother's gibberish. I want to hear her count Mondays and Wednesdays in the brief interval before she's gone.
```

---

## IC-0439: Silent Nights of Firefly Light

- Title: Silent Nights of Firefly Light
- Author (byline): Eric Benson
- Work: Fat Horse Plays, Round 2; Pgs 3-8
- Publisher: Fast Horse Drama
- Publication date as stated: June 2012
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DARREN
- Teaser before the introduction: Yes
- Spoken words (computed): 1619
- Already set (do not supply): none

### Source block (context only)

```text
Author: Eric Benson
Book: Fat Horse Plays, Round 2; Pgs 3-8
ISBN: 978-0615668734
Publisher: Fast Horse Drama
Date (Month/Year): June 2012
```

### Introduction (context only: never use it for content warnings)

```text
Darren Alexander Dennon, a 15-year-old is obsessed with Christmas and singing and his little sister Holly. He is the best big brother in the whole world even though he knows Holly was born because his parents wanted a smarter child who wasn’t deaf. So, Holly became the family’s Christmas miracle. She brought so much joy. Until . . . a tragic accident forces Darren to learn what it means to lose what you love most.

Silent Nights of Firefly Light by Eric Benson
```

### Performance text (classify this)

```text
Darren, 15, is verbal and enthusiastic. He is intellectually challenged and lost his hearing at age 13. He carries a stuffed animal (Snoopy)

DARREN: (Pgs 3-8) (singing) "Have yourself a merry little Christmas, let your heart be light, from now on our troubles will be out of sight ... "

Oh. I'm sorry about my voice, sometimes, my family says I get a little carried away when I sing. I think maybe it's because I don't wanna forget the . . . tunes of my favorite songs. Sometimes I think every time I sing one it's a little worse. I don't know how much time I have, so I think I'll introduce myself now. Okay? Okay. I'm Darren Alexander Dennon. Yes, my initials spell dad. I like . . . potato salad, playing frisbee and the color orange. My mom says that when I was really little, I would come out of my bedroom in the morning wearing orange from head to toe. I guess she'd make me change most days because she said I looked like a caution sign or something. What do moms know? I don't like artichokes (because they're hard to say and eat), alligators and my kindergarten teacher. Oh. This is Snoopy. He likes strawberry cupcakes. I love Christmas and . . . my sister, Holly. I hate . . . myself.

DARREN: I haven't always been like this. My ears have gotten a lot worse, which makes a lot of stuff really, really hard. Mom and Dad took me out of school after fourth grade because my teachers thought I was "too difficult." I think maybe they just got tired of having to make sure I wasn't crying because all the other kids were mean to me. But Mom says it was for the best and now a lady who smells like Windex comes and reads to me and stuff on Tuesdays and Thursdays. I didn't mind so much, because it meant I got to spend more time with Holly. She's almost six.

When mom and dad told me they were going to have a baby, I was really mad. Snoopy remembers -- They wanted another kid who was smart and could hear. One they could talk to everybody at work or the grocery store about. But, as mom's stomach got bigger and bigger, and people started to put Christmas trees up in their living rooms, I got excited to meet my little sister. Holly was born at 1:25 in the morning on Christmas. I waited in the waiting room with Grandma and sang (singing) "Grandma got run over by a reindeer, coming home from our house Christmas eve . . . " Until she told me to be quiet because the family across from us was staring. I thought it was funny.

Holly was the tiniest person I've ever seen, and I know I sound like a total cheese ball with extra cheese, but my entire heart moved up to my throat and made hot sticky tears run down my face the first time mom let me hold her. She was so light, like a tree ornament or maybe even a snowflake. I sang to her whenever she cried. (singing) "Deck the halls with boughs of Holly, fa la la la, la la la la, tis the season to be jolly la la ... " What, Snoopy? No, I won't forget, just calm down. I'm trying to tell this, okay?

Holly's first word was "Dar Dar." Dad likes to tell people it was Da Da and blames me confusing it on "my condition," but I saw her mouth move . . . Dar Dar. When she turned two, I put her in the biggest box I could find and put her under the Christmas tree with a gigantic red bow. I made sure Snoopy sat in the box with her, so she wouldn't get lonely. I thought it was going to be the funniest, best Christmas ever, but Mom and Dad didn't. Sometimes, I think they wish I disappeared when Holly was born and I maybe I should've. That's how great she is. It's kind of like all the stuff l'm . . . rnissing, Holly has. She's the brains and ears for both of us. I think I lost all of my "comprehensive hearing" when Holly was four. It was about three weeks after the fourth of July and I was sitting outside with Holly counting the fireflies on our porch. It wasn't sudden . . . I just kinda realized I'd stopped hearing the crickets chirping, and that Holly wasn't singing that song, have you heard it? (singing) "Jeremiah was a bullfrog da na nuh . . . " but when I looked at her, her mouth was still moving, so I told her I couldn't hear her. I guess she started singing really, really loudly, her eyes so so wide, with her little hands fluttering around like the fireflies. Mom and dad came outside, probably to tell us to quiet down, but when they saw Holly's face, and me holding my hands to my head, to see if the big quiet was living in my brain, right? They started mouthing angry, scared words at me, which made Holly start crying, and the worst thing about that was that I couldn't hear. . . anything. Just. White. Firefly. Light.

A week before Holly's birthday last year we were shopping with mom at the market for groceries and wrapping paper, when I noticed that Holly's big blue eyes were staring at someone. Not in the nice staring way. I turned around from pushing the cart and saw some kids from school. I guess they were making fun of me, because one was walking funny with one hand cupped to his ear and the other hand hitting his chest. Like this. (demonstrates) I just put my head down. I didn't want to cry and have mom get upset at me, but Holly marched up to them like nothing I've ever seen and started moving her mouth really fast. The next thing I knew, mom was walking us out of the store and shaking her hand at Holly who was smiling the biggest smile I'd ever seen. She held my hand in the car all the way home.

I wanted to make Holly the best present this year. Usually, I give her two separate things. One birthday. One Christmas. But this year, my plans were so great that I knew that just one would be okay. The only thing was that I needed to make sure my parents would leave the house for just a couple hours. It took six days to convince them it would be okay. They could see some movie and pretend they liked each other and I would make sure Holly ate dinner and took a bath, and then they'd come home. No sweat, right?

The big night arrived and I had bought the blank cassette tape. Dug the dusty old tape recorder out of the basement. Sound proofed my room the best I could with my old comforter duct taped to the windows. I made Holly Spaghetti O's for dinner, well, she mostly made them and I sort of . . . watched her, we ate together and had some milk and went upstairs to start her bath. Extra Mr. Bubbles, not too hot water. I was good at this big brother thing, right? I made sure she was okay, and said I was going into my room to do something. She wrote "Ok, poop face" in the steamed up mirror.

So, I went to my room. My big surprise was to sing every single one of Holly's favorite Christmas songs and record them. They probably sounded pretty crappy because of. . . me. But I knew she would love them. I'm a good big brother. So, Jingle Bells, Rocking Around the Christmas Tree, Here Comes Santa Claus, even Do You Hear What I Hear? When I looked at the clock it was 8:45 and I had started singing at seven. I thought, Holly must be a big prune by now, the water must be freezing. So, I walked down the hallway to the bathroom doorway. But, something wasn't right.

Holly was. Holly was. She was . . . Why does she look like that? Her face was under the water and she was not moving. And the water in the bathtub was not the color it was supposed to be. It was red. It was all red. Holly had slipped and hit her little head in the bathtub. I may be slow and deaf and stupid but this was definitely not how little sisters who hold your hand and write poop face in steamed up mirrors, and make everything okay in this very, very crappy world are supposed to look when you leave them, like a good big brother, like the best big brother in the entire world to take a bubble bath.

And I did hear something then, for the first time in two years. My heart. I heard it beating in my throat. Pounding. I dialed mom's number and started screaming and screaming as loud as I could. I didn't know what else to do. Today was Holly's birthday. Merry Christmas. I am the worst big brother in the entire world. I can't change how stupid I am. And I know that.

I tried to go into Holly's room yesterday, because I just needed to be around her stuff you know? But mom or dad . . . or maybe grandma put a lock on the door. I don't really know why they did that. I tried to give my mom a hug today, just to remind her that I am here, but she just looked at me, her eyes watery and strange, like there wasn't anything behind them and walked away.

(singing) Silent night, holy night, all is calm, all is bright, round yon virgin, mother and child, holy infant so tender and mild, sleep in heavenly peace . . . "
```

---

## IC-0440: Simon the Cyrene

- Title: Simon the Cyrene
- Author (byline): Richard Exley
- Work: Witness the Passion
- Publisher: White Stone Books
- Publication date as stated: 2004
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1445
- Already set (do not supply): none

### Source block (context only)

```text
Author: Richard Exley
Book: Witness the Passion
ISBN: 159379021X
Publisher: White Stone Books
Date(Month/Year): 2004
```

### Introduction (context only: never use it for content warnings)

```text
SIMON WAS A STRANGER IN JERUSALEM, A PILGRIM who had traveled to the holy city to celebrate the Passover with his sons, Alexander and Rufus. He was most likely a devout member of the Jewish Dispersion who had settled in the Greek city of Cyrene in North Africa. Upon entering Jerusalem he was suddenly seized and compelled to carry the cross for a condemned man named Jesus. And through the merciful providence of God his conscription resulted in his conversion. Simon the Cyrene by Richard Exley
```

### Performance text (classify this)

```text
APROACHING THE CITY VIA THE SOUTH Samaria- Jerusalem road, I cannot avoid seeing the place of execution. It is situated on a bare rocky hill in a small triangle, formed where the road converges with the Joppa-Jerusalem road. From a distance it looks remarkably like a bleached skull as it rises fifteen or twenty feet above the surrounding terrain.

Today it is devoid of victims, a fact I note with no little gratitude. Nonetheless, it casts an ominous shadow across the road as I turn toward the Gennath Gate which leads into the city. My sons, Alexander and Rufus, are with me, and they stare in morbid fascination at the three cypress posts which stand like daggers stabbed in the crown of the skull. These are the uprights upon which the cross beams are attached to form the implements of execution. They are permanent, serving as a constant reminder of Roman justice, which is both swift and cruel.

Anxious as I am to put that grisly scene behind us, my progress is slowed by the throng of pilgrims who are flooding into the city for the Passover. For us Hebrews it is the holiest of all feasts, commemorating our deliverance from Egypt. Jerusalem, I observe, is alive with anticipation. There are people everywhere. The noise is constant-the cries of street vendors hawking their wares, shouted greetings between old friends, the running laughter of children, the bleating of sheep, and the cooing of doves. For me, the noise is nostalgic, resurrecting long-dead memories of a happier time.

As a boy I journeyed with my parents each year to this very city to celebrate my faith. Then, against their wishes, I married a Greek girl from Cyrene, a cultured city on the northern coast of Africa. Following the wedding, her father invited me to become part of the family's prosperous import business, and I accepted his offer.

Financially it was a good move, but it has not been without its drawbacks. For instance, my children are more Greek than Hebrew. They know almost nothing of their Jewish roots and have never celebrated Passover in the Holy City. Although their mother did not forbid it, she made her wishes clear enough.

In many ways ours is a good marriage, but on the issue of religion we have not been able to agree. She finds my Jewish faith barbaric with its blood sacrifices, not to mention sectarian. I, in turn, cannot stomach the proliferation of gods which her Greek tradition espouses. This year I have risked the peace of our house to celebrate Passover with my sons in the Holy City.

The crowds have stalled and, being a big man, I impatiently shoulder my way through, motioning for the boys to keep up. The side street upon which we are traveling twists around a corner and empties into the Via Dolorosa, where we are brought to an abrupt halt. The scene before me turns my stomach, and I frantically attempt to retrace my steps. My sons must not see this. It will spoil the whole Passover experience, taint every memory. Too late I see Rufus and Alexander push through to the front of the crowd. In an instant their ruddy faces turn chalk white. For a moment their eyes are riveted on the drama being played out in the street before them, then they look around wildly, searching the crowd for me. Before I can push through the throng to them, a heavy hand falls upon my shoulder, and I am ordered into the street.

his cannot be happening! I am a respected merchant, a well-placed man in the city of Cyrene. How dare these barbaric Romans cause me to defile myself by participating in the execution of these terrorists! But dare they do and I am powerless to refuse. At the centurion's order I grudgingly shoulder the fallen man's cross and fall in behind him. Shame burns my face and I am thankful the mother of my children is not here to endure this ignominy. Bad enough that my sons should see their father marched through the city in the company of common criminals!

As we move out, I study the men in front of me. At the head of the column is the centurion astride a gray horse. With controlled forcefulness he clears the street of the curious peasants, making way for the condemned men who follow bearing their crosses.

The man whose cross I carry brings up the rear and with each step he lags farther behind. It is not the fear of death that slows his pace, bur the weakness of his abused body. He has been scourged, what the Romans call the "halfway death." It is not supposed to be administered in addition to other punishment, but in his case it has been.

From time to time, I glance over my shoulder to make sure Rufus and Alexander are part of the crowd which follows our pathetic parade. I would like to send them away in order to spare them this scandalous trauma, but we are strangers in the city and I have no place to send them. It is better, I decide, for them to endure this gruesome experience than for us to risk becoming separated from each other.

Having settled that issue, I turn my attention to the task at hand. We are now ascending the steep hill leading to the Gennath Gate, and I am laboring beneath the weight of the cross. Though I am a large man and well muscled, it has been years since I have done physical labor, leaving me in no condition for this strenuous climb. Before we have reached the half-way point, my garments are soaked with sweat and my lungs are on fire. Ahead of me the beaten man stumbles, and I think he must surely collapse, but somehow he finds the strength to go on. His head is bowed, his breathing labored, his face a suffering mask. Behind me I hear the sound of sobbing. Not a wail but a whimper, and more sorrowful for it. It is coming from a small group of women who seem oblivious to everything except the bleeding man who staggers up the hill toward the place of his death. From the crowd I hear someone say, "It's Mary, his mother. Poor woman."

At last we reach the crown of the skull. Dropping his cross I fall to one knee, fighting to catch my breath. The sun is merciless, and I would give almost anything for a little shade and a drink of cold water. Hardly has that thought taken shape in my mind before a shadow falls across my face, shielding me from the glare. Glancing up, I find myself looking full into his face. My first impulse is to turn away in revulsion, so abused is his visage. One eye is swollen nearly shut, and beneath the bruises, his skin is pasty and white. His beard is matted with dried blood, and flecks of spittle coat his raw lips.

Around me things continue as before. The soldiers prepare for the execution. The trailing crowd forms a semicircle before the condemned men. A group of religious leaders stand apart from everyone else, waiting impatiently. The women still weep. But all of this seems to recede, leaving just the two of us alone on this barren hill. Inside my head I hear the ancient words of the prophet Isaiah: "He had no beauty or majesty to attract us to him, nothing in his appearance that we should desire him. He was despised and rejected by men, a man of sorrows, and familiar with suffering. Like one from whom men hide their faces he was despised, and we esteemed him not."2

While I am still puzzling over this passage, he puts his hand upon my shoulder. His touch is both a blessing and a benediction, causing me to tremble-not in revulsion, but in reverence. Before I can speak a soldier shoves me out of the way, while two others grab the man called Jesus and position him on the cross. An order is given, and the heavy hammer falls. It strikes the five-inch spike with a resounding clang that rolls over the crowd like a death knell.

I walk away, never looking back. I have no stomach for this sort of thing. Try as I may though, I am never able to forget this day or more especially the Jewish carpenter who placed his work-hardened hand on my shoulder just before laying it on the cross to receive that Roman nail.
```
