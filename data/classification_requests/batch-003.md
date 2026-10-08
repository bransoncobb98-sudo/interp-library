# Classification request: batch 3 of 63 (40 records, IC-0081 to IC-0120)

You are an experienced high school speech and debate coach classifying interpretation cuttings
for a searchable library used by students and coaches.

## Reply format

Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to
`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.
Save the reply as `batch-003-reply.json`.

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

## IC-0081: Angels in America: Millennium Approaches

- Title: Angels in America: Millennium Approaches
- Author (byline): Tony Kushner
- Work: Not specified
- Publisher: Theatre Communications Group
- Publication date as stated: April 1993
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: HARPER, JOE
- Teaser before the introduction: Yes
- Spoken words (computed): 1525
- Already set (do not supply): none

### Source block (context only)

```text
Author: Tony Kushner
ISBN: 978-1559360616
Publisher: Theatre Communications Group
Date (Month/Year): April 1993
```

### Introduction (context only: never use it for content warnings)

```text
Harper is a mess. A quirky, loveable mess, but a mess all the same. Agoraphobic (afraid of public places) and hooked on valium, Harper spends most of her time hallucinating in her Brooklyn apartment while her husband, Joe, is away from home. Joe is a straight-laced Mormon from Salt Lake City adrift in big city of New York. Raised to think that homosexuality is a sin, he takes a giant step away from the morality he grew up with.

A society that encourages the repression of homosexuality isn't just harmful to gay people themselves. If Joe had felt comfortable with his sexuality, he never would have married Harper, and she wouldn't have suffered years of torture. Maybe they would have just been good friends – who knows? Instead, societal pressure forced them into a life of denial. In this scene the walls of denial finally crumble. Angels in America: Millennium Approaches by Tony Kushner.
```

### Performance text (classify this)

```text
HARPER: People who are lonely, people left alone, sit talking nonsense to the air, imagining . . . beautiful systems dying, old fixed orders spiraling apart . . .

When you look at the ozone layer, from outside, from a spaceship it looks like a pale blue halo, a gentle, shimmering aureole encircling the atmosphere encircling the earth. Thirty miles above our heads, a thin layer of three-atom oxygen molecules, product of photosynthesis, which explains the fussy vegetable preference for visible light, its rejection of darker rays and emanations. Danger from without.

It’s a kind of gift, from God, the crowning touch to the creation of the world: guardian angels, hands linked, make a spherical net, a blue-green nesting orb, a shell of safety for life itself. But everywhere, thing are collapsing, lies surfacing, systems of defense giving way . . . This is why, Joe, this is why I shouldn’t be left alone. (Little pause)

I’d like to go travelling . . . Leave you behind to worry. I’ll send postcards with strange stamps and tantalizing messages on the back. ‘Later maybe.’ ‘Nevermore . . .’

HARPER: Where were you?

JOE: Out.

HARPER: Where?

JOE: Just out. Thinking.

HARPER: It’s late.

JOE: I had a lot to think about.

HARPER: I burned dinner.

JOE: Sorry.

HARPER: Not my dinner. My dinner was fine. Your dinner. I put it back in the oven and turned everything up as high as it could go and I watched till it burned black. It’s still hot. Very hot. Want it?

JOE: You didn’t have to do that.

HARPER: I know. It just seemed like the kind of thing a mentally deranged sex-starved pill-popping housewife would do.

JOE: Uh huh

HARPER: So I did it. Who know anymore what I have to do?

JOE: How many pills?

HARPER: A bunch. Don’t change the subject.

JOE: I won’t talk to you when you . . .

HARPER: No. No. Don’t do that! I’m . . . I’m fine pills are not the problem, not our problem. I WANT TO KNOW WHERE YOU’VE BEEN! I WANT TO KNOW WHAT’S GOING ON!

JOE: Going on with what? The job?

HARPER: Not the job.

JOE: I said I need more time.

HARPER: Not the job!

JOE: Mr. Cohn, I talked to him on the phone, he said I had to hurry . . .

HARPER: Not the . . .

JOE: But I can’t get you to talk sensibly about anything so

HARPER: SHUT UP!

JOE: Then what?

HARPER: Stick to the subject.

JOE: I don’t know what that is. You have something you want to ask me? Ask me. Go

HARPER: I . . . . can’t. I’m scared of you.

JOE: I’m tired. I’m going to bed.

HARPER: Tell me without making me ask. Please.

JOE: This is crazy, I’m not . . .

HARPER: When you come through the door at night your face is never exactly the way I remembered it. I get surprised by something . . . mean and hard about the way you look. Even the weight of you in the bed at night, the way you breathe in your sleep seems unfamiliar. (Beat) You terrify me.

JOE: I know who you are.

HARPER: Yes. I’m the enemy. That’s easy. That doesn’t change. You think you’re the only one who hates sex; I do; I hate it with you; I do. I dream that you batter away at me till all my joints come apart, like wax, and I fall into pieces. It’s like a punishment. It was wrong of me to marry you. I knew you . . . (She stops herself) It’s a sin, and it’s killing us both.

JOE: I can always tell when you’ve taken pills because it makes you red-faced and sweaty and frankly that’s very often why I don’t want to . . .

HARPER: Because . . .

JOE: Well, you aren’t pretty. Not like this.

HARPER: I have something to ask you.

JOE: Then ASK! AKS! What in the hell are you . . .

HARPER: Are you a homo? (Beat) Are you? IF you try to walk out right now I’ll put your dinner back in the oven and turn it up so high the whole building will fill with smoke and everyone will asphyxiate. SO help me God I will. Now answer the question.

JOE: What if I . . . (Beat)

HARPER: Then tell me, please. And we’ll see.

JOE: No. I’m not. I don’t see what difference it makes. (Beat) I think we ought to pray. Ask God for help. Ask him together . . .

HARPER: God won’t talk to me. I have to make up people to talk to me.

JOE: You have to keep asking.

HARPER: I forgot the question. Oh year. God, is my husband a . . .

JOE: Stop it. Stop it. I’m warning you. Does that make any difference? That I might be one thing deep within, no matter how wrong or ugly that thing is, so long as I have fought, with everything I have, to kill it. What do you want from me? What do you want from me, Harper? More than that? For God’s sake, there’s nothing left, I’m a shell. There’s nothing left to kill. (Beat) As long as my behavior is what I know it has to be. Decent. Correct. That alone in the eyes of God.

HARPER: No, no not that, that’s Utah talk, Mormon talk. I hate it, Joe, tell me, say it . . .

JOE: All I will say is that I am a very good man who has worked very hard to become good and you want to destroy that. You want to destroy me, but I am not going to let you do that. (Beat).

HARPER: I’m going to have a baby.

JOE: Liar.

HARPER: You liar. A baby born addicted to pills. A baby who does not dream but who hallucinates, who stares up as us with big mirror eyes and who does not know who we are. (Beat)

JOE: Are you really . . ..

HARPER: No. Yes. No. Yes. Get away from me. Now we both have a secret. (Beat) When you pray, what do you pray for?

JOE: I pray for God to crush me, break me up into little pieces and start all over again.

HARPER: Oh. Please. Don’t pray for that.

JOE: I had a book of Bible stories when I was a kid. There was a picture I’d look at twenty times every day: Jacob wrestles with the angel. I don’t really remember the story, or why the wrestling – just the picture. Jacob is young and very strong. The angel is . . . a beautiful man, with golden hair and wings, of course. I still dram about it. Many night. I’m . . . It’s me. In that struggle. Fierce, and unfair. The angel is not human, and it holds nothing back, so how could anyone human win, what kind of a fight is that? It’s no just. Losing means your soul torn down in the dust, your heart torn out from God’s. But you can’t not lose.

HARPER: In the whole entire world, you are the only person, the only person I love or have ever loved. And I love you terribly. Terribly. That’s what’s so awfully, irreducibly real. I can make up anything but I can’t dream that way.

JOE: Are you . . . are you really going to have a baby?

HARPER: It’s my time, and there’s no blood. I don’t really know. I suppose it wouldn’t be a great thing. Maybe I’m just not bleeding because I take too many pills. Maybe I’ll give birth to a pill. That would give a new meaning to pill popping, huh? I think you should go to Washington. Alone.

JOE: I’m not going to leave you, Harper.

HARPER: Well maybe not, But I’m going to leave you.

JOE: Harper. Please listen. I still love you very much. You’re still my best buddy; I’m not going to leave you. Please listen. Stay. This is really hard. We have to talk.

HARPER: We are talking. Aren’t we. Now please shut up. OK?

JOE: Just listen. You want the truth. This is the truth. I knew this when I married you. I’ve know this I guess for as long as I’ve known anything, but . . . I don’t know, I thought maybe that with enough effort and will I could change myself . . . but I can’t . . . I’m losing ground here, I go walking, you want to know where I walk, I . . . go to the park or up and down 53rd Street, or places where . . . And I keep swearing I won’t go walking again, but I just can’t. (Beat) I try to tighten my heart into a knot, a snarl, I try to learn to live dead, just numb, but then I see someone I want, and it’s like a nail, like a hot spike right through my chest, and I know I’m losing. My whole life has conspired to bring me to this place, and I can’t despise my whole life. I think I believed when I met you I could save you, you at least if not myself, but . . . I don’t have any sexual feeling for you, Harper. And I don’t think I ever did. (Little pause)

HARPER: I think you should go.

JOE: Where?

HARPER: Washington. Doesn’t matter.

JOE: What are you talking about?

HARPER: Without me. Without me, Joe. Isn’t that what you want to hear? (little pause)

JOE: Yes.

HARPER: You were going to save me, but the whole time you were spinning a lie. I just don’t understand that. . . This is so scary, I want this to stop, to go back . . .

JOE: Harper . . . As long as I’ve known you Harper you’ve been afraid of . . . of men hiding under the bed, men hiding under the sofa, men with knives. Who are these men? I never understood it. Now I know.

HARPER: What?

JOE: It’s me. . . . I’m the man with the knives.
```

---

## IC-0082: Animal Dreams

- Title: Animal Dreams
- Author (byline): Jennifer Maisel
- Work: Even More Monologues for Women by Women
- Publisher: Heinemann
- Publication date as stated: March 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NATALIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1440
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jennifer Maisel
Book: Even More Monologues for Women by Women
ISBN: 0325002479
Publisher: Heinemann
Date(Month/Year): March 2001
```

### Introduction (context only: never use it for content warnings)

```text
Animal Dreams by Jennifer Maisel
```

### Performance text (classify this)

```text
(Begin in a fetal position on the floor)

NATALIE: I wonder when they’ll tell me about the cancer - is this the wrong thing to be happening to my body? Maybe it’s the right thing, maybe it’s the only reaction to the world my body can have, maybe it’s the only way it can express itself, make itself heard, going out of control, multiplying chaos, anarchy. We try to contain the revolution of cells with knives and poisons and affirmations. What if those cells are my battle against the world? - a way of growing stronger to combat the daily and the lifelong, to make more of just me against the world.

(Natalie is dressed in a hospital gown. Behind her, a hospital bed holds an image of her body in fetal position. Natalie looks down at her body. There is the sound of whirring machinery.)

NATALIE: (Natalie has now “left” her body and is free to move about the stage) I don't recognize that body at all. I mean even if you were to take me into a lineup of bodies and force me choose . . . It's so . . . slack, soft tired skin. Look at that razor stubble-I mean the legs. I used to let the legs go an extra day or two but I always shaved under the arms. I didn't like the way it looked when I didn't shave under the arms. I smelled a little rancid too when I didn't. That is one sorry-looking case. (Looks around her to call) Could someone around here just take a minute and, y'know, shave her under the arms please? It would only take a minute. Look, you get so convinced she can hear you, that she could respond if only given the right stimulus, give her a little dignity, why don't you? Oh, to hell with it.

All the positions you put your body in over a lifetime and when push comes to shove this is the one it chooses to remember. It's a good cliche, but not all that comfortable without the waves in the amniotic fluid keeping you afloat. (To the body on the bed) Why don't you revert back to one of the good posi-tions, huh? Don't you remember any of the good ones? Try this one. (She perches on the stool, legs up and splayed apart, head back.) Oh c'mon, this one always worked. What about-(Gets off the stool and bends over it, looking back coyly over her shoulder. Tries a look of passion.} You are no fun at all. You've gotta remember. It hasn't been that long, has it? The body's supposed to remember these things. Like a bicycle, right?

They're not sure whose hand they hold. They're not sure whether it can hear them. They're not sure if they're doing any good at all. They're not sure if they know who she is anymore. They can label her-parts of what she was- Mom. Lover. Wife. Sixth-Grade Teacher. Friend. . . Patient. . . Statistic. They're not sure if she is anymore.

(A school bell rings. As a teacher.) According to the medical profession a coma is the state from which a person cannot be aroused. According to the medical profession there are fifteen stages of coma-stage 1 showing no response to the outside world and stage 15 the most. . . social. According to the medical profession, Glascow's fifteen-point coma scale is also a crock. It just depends on who you talk to.

Maybe we're just too tired to wake up. Maybe it's just not worth the effort. Maybe there's a comfort in the deep irreverence of ignoring the commotion and the congestion of the everyday. Maybe it's just too painful to be awake right now. Maybe it's time to heal. Maybe I just need a rest! I need a rest!

(Composes herself) In the deep stages I've been able to escape the body and watch the remnants of it metastasizing into one connected mass of small cancerous lumps. I keep my eyes focused inward and note the proliferation of cells like a dandelion patch gone wild and I blow one small tumor into pieces that take root where they fall. I make a wish. And I walk through the inside of my body noting the holocaust of my being, the radiation having killed the healthy and not the sick, the florid growth, the blood full of lumpy cells. And I notice, my wish hasn't come true. This is still the body they say belongs to me.

Celia, my daughter, sits by me and tells me it's OK to let go. To let go. It's OK to let go. How do you know. Trying to get rid of me? . . . How do you know it's OK? What if I let go and there's nothing? What if I let go to nothing? Hold tight! (Extends hands in front of her. Four irregular breaths. Four more regular breaths.)

Your hand is warm. I can feel that tic of blood at the bottom of your thumb. I'd put my lips there when you were a baby. You wonder if I like it here. You wonder if I know you. You wonder if I know where I am. Don't let go! Don't bring me out of it. It will hurt. God! If you bring me out of it, it will hurt. I'm not coming out of it again. Do you hear me? I am not coming out of it again.

Don't let go of my hands now. You brought me back in here. Don't let go of them. . . .

You know as much as they tell you about the inevitability of fate-you are very concerned because you don't want to end up like me. You tell people you take care of yourself You say it's not heredity but environment. You say . . .Don't let go of my hands. Do not let go of my hands, young lady. Where do you think you're going? Come back here. Come back here.

Things I can tell you that you just might not know: There are times when I am trapped in my body in a heavy stupor. One of those stupors like after a really bad drunk. One of those times you struggle to get to the surface only to find-out it's not the place that you want to be.

There are times when I'm not in my life as it is anymore but as it was. I am teaching. I am falling in love again. I'm watching Mom die. My body lets me go. I am in the room, I am on the street, I am flying over the world seeing places I never made it to. I am visiting the people I love and they feel me there but they can't quite put a name to it. My body lets me go. I want to kick it. I want to punch it. I want to scratch great holes in the skin and watch the blood well up. I want to pinch it black and blue and scream, "You miserable thing, what good have you been for me? What have you been doing to me? How dare you betray me like this? How dare you?"

But I can't bite and I can't tear or scratch. My body lets me go and the freedom becomes unbearable and I want to be back inside the confines of my body, if only to know my limitations.

I guess you just have to be there. (To her husband) Oh . . . What are you doing here? You hate hospitals. You hate antiseptic smell not really masking, cotton swabs, TVs positioned high above the bed. You hate me. You live that moment when your hand grasped the. . . breast. . . over and over. It was sex, it was skin, it was touching, absorbing, culminating. . . like so many times before, so many times before, we don't have to speak. . . we've never had to speak. Then you say. . . "What's that? Feel that. What's that? Feel that." Ruined the mood, I can say that much. This is how you'll remember me now.

(School bells rings. As teacher speaking in a student's voice.) I was going to bring something very special to show and tell today, teacher, but I must have lost them on the way. No I did, really, look. (She bares her chest, showing two big scars winding where her breasts used to be.) l'll look for them and bring them tomorrow, I promise. They must be around here somewhere. l'll look real hard. I swear. (School bell rings again.)

I wonder. I wonder when they tell me about the cancer is this the wrong thing to be happening to my body? Maybe it's the right thing, maybe it's the only reaction to the world my body can have, maybe it's the only way it can express itself, make itself heard, going out of control, multiplying chaos, anarchy. We try to contain the revolution of cells with knives and poisons and affirmations. What if those cells are my battle against the world? A way of growing stronger to combat the daily and the lifelong, to make more of just me against the world. What if I somehow agreed to let the doctor cut out my strength?

(The machine whirring grows louder.) They say go into the light. They say come back to us. I can't. I can't. If I just stay here. If I just stay here. If I could just stay here. (The sounds of the machinery. . . the heart monitor, the dripping, take over as the world around Natalie becomes dark. . . . )
```

---

## IC-0083: Anne of a Thousand Days

- Title: Anne of a Thousand Days
- Author (byline): Maxwell Anderson
- Work: Not specified
- Publisher: Dramatists Play Service, Inc
- Publication date as stated: Dec 1950
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 770
- Already set (do not supply): none

### Source block (context only)

```text
Author: Maxwell Anderson
ISBN: 082220049X
Publisher: Dramatists Play Service, Inc
Date (Month/Year): Dec 1950
AWARD RECORD
2001 National Qualifier – DI - Female
```

### Introduction (context only: never use it for content warnings)

```text
Anne Bolin has been arrested for a crime she did not commit and has been imprisoned. Her love has also been betrayed. Her crime is adultery and high treason. Her betrayer is her husband, her love, and her king. She was the queen. They called her “Anne of a Thousand Days” by Maxwell Anderson.
```

### Performance text (classify this)

```text
If I die now, I go out into night, and Elizabeth, my firstling, all I have, must face the new world in the morning. To those who die, we seem to go forward into darkness. To those who are newborn, we seem to go forward into dawn. And as I bore Elizabeth, midnight will bear morning.

If I were to die now, but I must not die yet, not yet. It’s been too brief. A few weeks . . . and days. How many days, I wonder, since the first time I gave myself to that last day, when he left me at the lists and I saw him no more? Well I can reckon it. I have time enough. Those who sit in the tower do not lack for time.

He could never cipher. He was shrewd and heavy, and cunning with his tongue, and wary in intrigue. But when it came to adding up an account, he filled it with errors and bit his tongue and swore, till I slapped his hand like a child and took the pen and made it straight. “A king,” I said, “a king and cannot reckon.”

I was his clever girl then, his Nan. He’d kiss me then, and maul me, and take me down. On the rushes, anywhere. Why do I think of it now? Would he kill me? Kill me? Henry? That fool? That great fool kill me?

Could I kill him, I wonder? I feel it in my hands perhaps I could. So perhaps he could kill me. Perhaps he could kill me. He knew I’d love him when once he’d made me his. And so it was. After that night I loved him more and more, and hated him less and less. And I was lost.

From the first day he made me his, to the last day I made him mine, yes, let me set it down in numbers. I who can count and reckon. Of all the days I was his and did not love him, of all the days I was his and he had ceased to love me? In days…. It comes to a thousand days, out of the years. Strangely, just a thousand. And of that thousand, one… only one when we were both in love, one when our loves met, and overlapped, and were both mine and his. When I no longer hated him, he began to hate me. Except for that one day. One day out of the years.

If his majesty were here….

There are fools and fools, King Henry. You have locked me up here to be tried for adultery and treason towards you. You have done this because you love elsewhere, and I know it. And now you come here, to make sure if there were truly adultery, because that would touch your manhood, or your pride.

And you wait, and listen, a cat in a corner, watching the pet mouse before it dies. And then you come out, to make sure. And oh, fool of fools, even so my heart and my eyes are glad of you. Fool of all women that I am, I am glad of you here.

I never thought what it was like to die. To become meat that rots, and food for shrubs… someone told me the story of the homely daughter of Sir Thomas Moore, climbing at night up the trestles of the London Bridge, where they had stuck her father’s head on a spike. And hunting among the stinking and bloody heads, of criminals, still she found her father’s head, his beard matted and hard with blood. And climbing down with it and taking it home, to bury in the garden, perhaps.

Would they stick my head up on London Bridge? No even Henry would object to that. I’ve been his queen! He’s kissed my lips. He wouldn’t want it. I’ll lie in lead, or brass, as meat. Dead meat. But, if my head were on the bridge, he wouldn’t climb to take it down. Nobody’d climb for me. I’d stay and face up the river, my long hair blowing out and tangling ‘round the spikes. Till the seabirds took me, and there was nothing left but a wisp of hair and a cup of bone.

I must think of something to say, when the time comes. If I could say it, with the ax edge toward me, could I do it? Could I lay my head down, and smile, and speak, till the blow comes? They say it’s subtle. It doesn’t hurt. There’s no time. No time. That’s the end of time.
```

---

## IC-0084: Antigone

- Title: Antigone
- Author (byline): Sophocles (Translated by R.C. Jebb)
- Work: Sophocles :Plays: Antigone
- Publisher: Intl Pub Marketing
- Publication date as stated: Aug 2004
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 1629
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sophocles (translated by R.C. Jebb)
Book: Sophocles :Plays: Antigone
ISBN: 1853996475
Publisher: Intl Pub Marketing
Date (Month/Year): Aug 2004
```

### Introduction (context only: never use it for content warnings)

```text
A great battle has ended over dominion of the ancient city of Thebes. Massive causalities are incurred by both the insurgents and those soldiers defending their King. Two brothers die; one given a hero’s burial; the other, by royal edict, will receive no burial . . . but will instead be left as he fell . . . food for carrion. The law of man has spoken . . . but one young girl refuses to governed by the blasphemous laws of man: Antigone by Sophocles.
```

### Performance text (classify this)

```text
ANTIGONE Ismene, sister, mine own dear sister, knowest thou what ill there is, of all bequeathed by Oedipus, that Zeus fulfils not for us twain while we live? Nothing painful is there, nothing fraught with ruin, no shame, no dishonour, that I have not seen in thy woes and mine.

And now what new edict is this of which they tell, that our Captain hath just published to all Thebes? Knowest thou aught? Hast thou heard? Or is it hidden from thee that our friends are threatened with the doom of our foes?

ISMENE No word of friends, Antigone, gladsome or painful, hath come to me, since we two sisters were bereft of brothers twain, killed in one day by twofold blow; and since in this last night the Argive host hath fled, know no more, whether my fortune be brighter, or more grievous.

ANTIGONE I knew it well, and therefore sought to bring thee beyond the gates of the court, that thou mightest hear alone.

ISMENE What is it? 'Tis plain that thou art brooding on some dark tidings.

ANTIGONE What, hath not Creon destined our brothers, the one to honoured burial, the other to unburied shame? Eteocles, they say, with due observance of right and custom, he hath laid in the earth, for his honour among the dead below. But the hapless corpse of Polyneices-as rumour saith, it hath been published to the town that none shall entomb him or mourn, but leave unwept, a welcome store for the birds, as they espy him, to feast on at will.

ISMENE Poor sister,-and if things stand thus, what could I help to do or undo?

ANTIGONE Consider if thou wilt share the toil and the deed. Wilt thou aid this hand to lift the dead?

ISMENE Thou wouldst bury him,-when 'tis forbidden to Thebes? Ah, over-bold! when Creon hath forbidden?

ANTIGONE Nay, he hath no right to keep me from mine own.

ISMENE Ah me! think, sister, how our father perished, amid hate and scorn, when sins bared by his own search had moved him to strike both eyes with self-blinding hand; then the mother wife, two names in one, with twisted noose did despite unto her life; and last, our two brothers in one day,-each shedding, hapless one, a kinsman's blood,-wrought out with mutual hands their common doom. And now we in turn-we two left all alone think how we shall perish, more miserably than all the rest, if, in defiance of the law, we brave a king's decree or his powers. Nay, we must remember, first, that we were born women, as who should not strive with men; next, that we are ruled of the stronger, so that we must obey in these things.

ANTIGONE Nay, be what thou wilt; but I will bury him: well for me to die in doing that. I owe a longer allegiance to the dead than to the living: in that world I shall abide for ever. But if thou wilt, be guilty of dishonouring laws which the gods have stablished in honour.

ISMENE I do them no dishonour; but to defy the State,-I have no strength for that. A hopeless quest should not be made at all.

ANTIGONE If thus thou speakest, thou wilt have hatred from me, and will justly be subject to the lasting hatred of the dead. Leave me, and the folly that is mine alone, to suffer this dread thing; for I shall not suffer aught so dreadful as an ignoble death.

TRANSITION

And so Antigone. . . alone. . . bears the honor and the burden of burying her beloved brother, Polyneices. For her disobedience she will face the wrath of King Creon. . . again . . . alone. Silence descends as Antigone is brought before the King, the dirt from her brother’s grave still fresh upon her hands.

CREON Thou-thou whose face is bent to earth-dost thou avow, or disavow, this deed?

ANTIGONE I avow it; I make no denial.

CREON Now, tell me thou-not in many words, but briefly-knewest thou that an edict had forbidden this?

ANTIGONE I knew it: could I help it? It was public.

CREON And thou didst indeed dare to transgress that law?

ANTIGONE Yes; for it was not Zeus that had published me that edict; not such are the laws set among men by the justice who dwells with the gods below; nor deemed I that thy decrees were of such force, that a mortal could override the unwritten and unfailing statutes of heaven. For their life is not of to-day or yesterday, but from all time, and no man knows when they were first put forth.

Not through dread of any human pride could I answer to the gods for breaking these. Die I must,-I knew that well (how should I not?)-even without thy edicts. But if I am to die before my time, I count that a gain: for when any one lives, as I do, compassed about with evils, can such an one find aught but gain in death?

So for me to meet this doom is trifling grief; but if I had suffered my mother's son to lie in death an unburied corpse, that would have grieved me; for this, I am not grieved. And if my present deeds are foolish in thy sight, it may be that a foolish judge arraigns my folly.

CREON Yet I would have thee know that o'er-stubborn spirits are most often humbled; 'tis the stiffest iron, baked to hardness in the fire, that thou shalt oftenest see snapped and shivered; and I have known horses that show temper brought to order by a little curb; there is no room for pride when thou art thy neighbour's slave. So oft, before the deed, the mind stands self-convicted in its treason, when folks are plotting mischief in the dark. But verily this, too, is hateful,-when one who hath been caught in wickedness then seeks to make the crime a glory.

ANTIGONE Wouldst thou do more than take and slay me?

CREON No more, indeed; having that, I have all.

ANTIGONE Why then dost thou delay? In thy discourse there is nought that pleases me,-never may there be!-and so my words must needs be unpleasing to thee. And yet, for glory-whence could I have won a nobler, than by giving burial to mine own brother? All here would own that they thought it well, were not their lips sealed by fear. But royalty, blest in so much besides, hath the power to do and say what it will.

CREON Was it not a brother, too, that died in the opposite cause?

ANTIGONE Brother by the same mother and the same sire.

CREON And yet thou makest him but equal in honour with the wicked.

ANTIGONE It was his brother, not his slave, that perished.

CREON But the good desires not a like portion with the evil.

ANTIGONE Tis not my nature to join in hating, but in loving.

CREON to Antigone Pass, then, to the world of the dead, and, it thou must needs love, love them. While I live, no woman shall rule me . . .

CREON thinks I will take her where the path is loneliest, and hide her, living, in rocky vault, with so much food set forth as piety prescribes, that the city may avoid a public stain. And there, praying to Hades, the only god whom she worships, perchance she will obtain release from death; or else will learn, at last, though late, that it is lost labour to revere the dead.

CREON to Antigone Know ye not that songs and wailings before death would never cease, if it profited to utter them? Away with her-away! And when ye have enclosed her, according to my word, in her vaulted grave, leave her alone, forlorn-whether she wishes to die, or to live a buried life in such a home. Our hands are clean as touching this maiden. But this is certain-she shall be deprived of her sojourn in the light.

ANTIGONE Tomb, bridal-chamber, eternal prison in the caverned rock, whither go to find mine own, those many who have perished, and whom Persephone hath received among the dead! Last of all shall I pass thither, and far most miserably of all, before the term of my life is spent. But I cherish good hope that my coming will be welcome to my father, and pleasant to thee, my mother, and welcome, brother, to thee; for, when ye died, with mine own hands I washed and dressed you, and poured drink-offerings at your graves; and now, Polyneices, 'tis for tending thy corpse that I win such recompense as this.

And yet I honoured thee, as the wise will deem, rightly. Such was the law whereby I held thee first in honour; but Creon deemed me guilty of error therein, and of outrage, ah brother mine! And now he leads me thus, a captive in his hands; no bridal bed, no bridal song hath been mine, no joy of marriage, no portion in the nurture of children; but thus, forlorn of friends, unhappy one, I go living to the vaults of death.

And what law of heaven have I transgressed? Why, hapless one, should I look to the gods any more,-what ally should I invoke,-when by piety I have earned the name of impious? Nay, then, if these things are pleasing to the gods, when I have suffered my doom, I shall come to know my sin; but if the sin is with my judges, I could wish them no fuller measure of evil than they, on their part, mete wrongfully to me.
```

---

## IC-0085: The Bad Seed

- Title: The Bad Seed
- Author (byline): Maxwell Anderson
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: 1956
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: No
- Spoken words (computed): 2495
- Already set (do not supply): none

### Source block (context only)

```text
Author: Maxwell Anderson
ISBN: 978-0822200888
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): 1956
AWARD
2002 National Qualifier – DI - Female
```

### Introduction (context only: never use it for content warnings)

```text
Radio: “I interrupt this broadcast to- I have been asked to announce that one of the children on the annual outgoing of the Fern Grammar School was accidentally drowned in the bay this afternoon. The name of the victim is being withheld until the parents are first notified. More news of the tragic affair is expected momentarily.” “He appears to have fallen into the water from an abandoned wharf on the Fern property. How the little boy got on the wharf, for all the children had been forbidden to play near or on it, but his body was found off the end of the landing, wedged among the pilings. The guards who brought up the body applied artificial respiration without result. There were bruises on the forehead and hands, but it is assumed these were caused by the body washing against the pilings. And now back to the national news.”

The Bad Seed by Maxwell Anderson
```

### Performance text (classify this)

```text
Rhoda: Mother, you know we didn’t really have our lunch because Claude Daigle was drowned.

Christine: I know. It was on the radio.

Rhoda: He was drowned, so then they were all rushing and calling and hurrying to see if they could make him alive again, but they couldn’t, so then they said the picnic was over and we had to go home.

Christine: I’m glad you’re home!

Rhoda: So could I have a peanut-butter sandwich and milk?

Christine: Did you see him dear?

Rhoda: Yes, of course. Then they put a blanket over him.

Christine: Did you see him taken from the water?

Rhoda: Yes, they laid him out on the lawn and worked and worked. But it didn’t help.

Christine: I want you to get those pictures right out of your mind. I don’t want you to be frightened or bothered at all. These things happen sometimes and when they do we simply accept them.

Rhoda: I thought it was exciting. Could I have my peanut-butter sandwich?

Christine: Darling, you’re controlling yourself very well, but just the same it was an unfortunate thing to see and remember. I understand how you feel, my darling.

Rhoda: I don’t know what you’re talking about. I don’t feel anyway at all. [Rhoda, seeing she has displeased her mother, rises and throws her arms around her waist, then takes her mother’s hand and kisses it.]

Christine: Have you been naughty?

Rhoda: Why, no mother. What will you give me if I give you a basket of kisses?

Christine: I’ll give you a basket of hugs.

Rhoda: I want to go out and skate on the asphalt.

Christine: Then you should go dear.

Rhoda exits through the kitchen, just as Miss Fern, an administrator from Rhoda’s school rings the bell

Miss Fern: May I come in, Mrs. Penmark?

Christine: Yes, of course, Miss Fern. I meant to come and see you.

Miss Fern: We’re in such distress, all of us at school, and we’ve suffered such a blow, losing one of the children that way, I’m sure you’ll excuse us for going over and over things!

Christine: I think everybody has been puzzled and worried and saddened.

Miss Fern: I don’t think I’ve ever known any happening to puzzle so many people in so many ways. And I can help so few of them. I’ve just come from seeing Mrs. Daigle. Of course, our first thought was of her. The rest of us are toughed only lightly by this tragedy. She will have to live with it the rest of her days.

Christine: I know.

Miss Fern: I have seen her several times, and each time she has asked me to find out from you if you had any possible clue to where the penmanship medal might be.

Christine: Was it lost?

Miss Fern: Yes, it wasn’t found with the body and has completely disappeared.

Christine: I didn’t know of this.

Rhoda: Good morning, Miss Fern.

Miss Fern: Good morning, Rhoda.

Rhoda: Mother, could I sit under the arbor for a whole and read my book?

Christine: Of course, Rhoda.

Rhoda: It’s shady there, and I can see your window, and you can watch me from the window, and I like to be where you can see me. Good Bye Miss Fern.

Miss Fern: It did occur to me that- that Rhoda might have told you a detail or two which she hadn’t remembered when she talked with me. You see, she was the last to see the little Daigle boy alive-

Christine: Are you sure of that? I hadn’t realized—

Miss Fern: About an hour after we arrived at the estate one of our older pupils came on Rhoda and Claude at the far end of the grounds. The boy was upset and crying, and Rhoda was standing in from of him, blocking his path. The older girl was among the trees, and neither child saw her. She was just about to intervene when Rhoda shoved the boy and snatched at his medal, but he broke away and ran down the beach in the direction of the wharf where he was later found. Rhoda followed him, not running, just walking along, taking her time, the older girl said.

Christine: Has it occurred to you that the older girl might not have been telling the truth?

Miss Fern: That isn’t at all likely. She was on of the monitors we appointed to keep an eye on the younger children. She’s fifteen and has been with us since kindergarten days. No, Mrs. Penmark, she was telling precisely what she saw. We know her well.

Christine: And this was the last time Claude was seen?

Miss Fern: Yes. A little later—it might have been about noon—one of the guards saw Rhoda coming off the wharf. He shouted a warning, but by then she was on the beach again and he decided to forget the matter. The guard didn’t identify the girl by name, but she was wearing a red dress, he said, and Rhoda was the only girl who wore a dress that day. At one o’clock the lunch bell rang and Claude was missing when the roll was called. You know the rest, I think.

Christine: Yes. But this is very serious—if Rhoda was on the wharf----

Miss Fern: Not serious, really, when you’ve seen as much of how children behave as I have. Children conceal things from adults. Suppose Rhoda did follow the Daigle child onto the wharf-so many things could have happened quite innocently. He may have concealed himself in the old boathouse and then, when discovered, may have backed away from Rhoda and fallen in the water.

Christine: Yes, that could have happened.

Miss Fern: Now, Claude, although he looked frail, was an excellent swimmer—and, of course Rhoda knew that. Once he was in the water she would have expected him to swim ashore. How could she know that the treacherous pilings were at the exact spot where he fell?

Christine: No, she couldn’t possibly…

Miss Fern: Perhaps the thought in Rhoda’s mind when he fell in the water was that he’s ruin his new suit and she’d get scolding for causing it. When he didn’t swim ashore at once she may have thought, with the logic of childhood, that he’d hidden under the wharf to frighten her—or to escape her. Later on, when it was too late to do anything, she was afraid to admit what had happened.

Christine: Them you think Rhoda knows something she isn’t admitting?

Miss Fern: Yes. I think that, like many a frightened soldier, she deserted under fire. This is not a serious charge. Few of us are courageous when tested.

Christine: She has lied, though.

Miss Fern: Is there any adult who hasn’t lied? Smooth the lines from your brow, my dear. You’re so much prettier when smiling.

Christine: I shall question Rhoda.

Miss Fern: I wish you would, though I doubt that you’ll learn more than you know.

Christine: Miss Fern, there’s something I want to ask you. There was a floral tribute at Claude’s funeral sent by the children of the Fern School. I suppose the children shared in the expense—but I haven’t been asked to pay any part of it.

Miss Fern: No, my dear. We thought perhaps you’d want to send flowers individually.

Christine: But why should we have sent flowers individually? Rhoda wasn’t friendly with the boy, and my husband and I had never met the Daigles.

Miss Fern: I don’t know, my dear, I really---there are three of us, you know, and in the hurry of making decisions

Christine: You make excuses for Rhoda—and then you admit that you didn’t ask me to help pay for the flowers—and the reasons you give for not asking are obviously suspicious. Does this mean that in your mind, and the minds of your sisters, there is some connection between Claude’s death and Rhoda’s presents on the wharf?

Miss Fern: I refuse to believe there is any connection.

Christine: And yet you have acted as if there were.

Miss Fern: Perhaps we have.

Christine: This is a terrible tragedy for Mrs. Daigle, as you say. She has lost her only child. But if there were any shadow over Rhoda—from what has happened—I shall have to live under it—and my husband too. As for Rhoda—she would not be happy in your school next year—and you have already decided not to invite her back.

Miss Fern: We have made that decision.

Christine: But you can’t tell me why?

Miss Fern: I think her behavior in the matter of the medal would be sufficient explanation. She has no sense of fair play. She’s a poor loser. She doesn’t play the game.

Christine: I’ll talk to Rhoda. I know there isn’t anything that will help. But I’ll do what I can.

[Miss Fern leaves and Christine opens Rhoda’s table drawer and finds the locket in the chocolate box. Lifts the edge of the drawer’s felt lining and sees the Penmanship Medal]

Rhoda: Did you want me to come in, Mother?

Christine: So you had the medal, after all. Claude Daigle’s medal.

Rhoda: Where did you find it?

Christine: How did the penmanship medal happen to be hidden under the lining of the drawer of your table, Rhoda? Now I want you to tell me the truth. [Rhoda takes off one of her shoes and examines it. Then smiles a little in a fashion she had always found charming]

Rhoda: When we move into our new house can we have an arbor, Mother? Can we, Mother? It’s so shady, and pretty, and I love sitting in it!

Christine: Answer my question. And remember I’m not as innocent about what went on at the picnic as you think. Miss Fern has told me a great deal. So please don’t bother to make up any story for my benefit. How did Claude Daigle’s medal get in your drawer? It certainly didn’t get there by itself. I’m waiting for your answer.

Rhoda: I don’t know how the medal got there, Mother. How could I?

Christine: You know. You know very well how it got there. Did you go on the wharf at any time during the picnic? At any time?

Rhoda: Yes Mother. I went there once.

Christine: Was it before or after you were bothering Claude?

Rhoda: I wasn’t bothering Claude, Mother. What makes you think that?

Christine: Why did you go on the wharf?

Rhoda: It was real early. When we first go there.

Christine: Why did you go on the wharf? You knew it was forbidden.

Rhoda: One of the big boys said there were little oysters that grew on the pilings. I wanted to see if they did.

Christine: One of the guards said he saw you coming off the wharf. And he says it was just a little before lunch time.

Rhoda: I don’t know why he says that. He’s wrong, and I told Miss Fern he was wrong. He hollered at me to come off the wharf and I did. Went back to the lawn and that’s where I saw Claude. But I wasn’t bothering him.

Christine: What did you say to Claude?

Rhoda: I said—if I didn’t win the medal, I was glad he did.

Christine: Please, please, Rhoda. I know you’re an adroit liar. But I must have the truth.

Rhoda: But it’s all true, Mother. Every word.

Christine: One of the monitors saw you try to snatch the medal off Claude’s shirt. Is that all true? Every word?

Rhoda: Oh, that big girl was Mary Beth Musgrove. She told everybody she saw me. You see, Claude and I wee just playing a game we made up. He said if I could catch him in ten minutes and touch the medal with my hand—it was like prisoners base—he’d let me wear the medal for an hour. How can Mary Beth say I took the medal? I didn’t.

Christine: She didn’t say you took the medal she said you grabbed at it. And that Claude ran away down the beach. Did you have the medal even then?

Rhoda: No mommy. Not then.

Christine: Rhoda, how did you get the medal.

Rhoda: Oh, I got it later on.

Christine: How?

Rhoda: Claude went back on his promise and I followed him up the beach. Then he stopped and said I could wear the medal all day if I gave him fifty cents.

Christine: Rhoda, stop that! Is that the truth?

Rhoda: Yes, Mother. I gave him fifty cents and he let me wear the medal.

Christine: Then why didn’t you tell this to Miss Fern when she questioned you?

Rhoda: Oh, Mommy, Mommy! Miss Fern doesn’t like me at all! I was afraid she’d think bad things about me if I told her I had the medal!

Christine: Rhoda, you knew how much Claude’s mother wanted the medal didn’t you?

Rhoda: Yes, mother, I guess I did.

Christine: Then why didn’t you give it to her? She is heart-broken over Claude’s death. It’s destroyed her. I don’t think she’ll ever recover from it. Do you know what I mean? No. You don’t know what I mean.

Rhoda: But it was silly to want to bury the medal pinned on Claude’s coat Claude was dead. He wouldn’t know whether he had the medal pinned on him or not. I’ve got the sweetest mother. I tell everybody I’ve got the sweetest mothering the world!—If she wants a little boy that bad, why doesn’t she take one out of the Orphans’ Home.

Christine: Rhoda! Get away from me! Don’t talk to me. We have nothing to say to each other. When we lived in Baltimore, there was an old lady upstairs, Mrs. Clara Post, who liked you very much. You used to go up to see her every afternoon. She was very old, and liked to show you all her treasures. The one you admired most was a crystal ball, in which opals floated. The old lady promised this treasure to you when she died. One afternoon when the daughter was out shopping at the super-market, and you were alone with the old lady, she somehow managed to fall down the spiral backstairs and break her neck. You said she heard a kitten mewing outside and went to see about it and somehow missed her footing and fell five flights to the courtyard below.

Rhoda: Yes, it’s true.

Christine: Then you asked the daughter for the crystal ball. She gave it to you, and it’s still hanging at the head of your bed. Rhoda, did you have anything to do, anything at all, no matter how little it was, with Claude getting drowned. Look me in the eyes and tell me. I must know.

Rhoda: No, Mother. I didn’t.
```

---

## IC-0086: Bald in the Land of Big Hair

- Title: Bald in the Land of Big Hair
- Author (byline): Joni Rogers
- Work: Not specified
- Publisher: HarperCollins Publishers, Inc
- Publication date as stated: Feb 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: JONI, DR. RO, MALACHI
- Teaser before the introduction: Yes
- Spoken words (computed): 1480
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joni Rogers
ISBN: 978-0060955267
Publisher: HarperCollins Publishers, Inc
Date (Month/Year): Feb 2002
```

### Introduction (context only: never use it for content warnings)

```text
Being a parent while living with cancer is physically and emotionally exhausting. You do everything you can to protect your child from the pretend monsters under the bed and the real monsters lurking in the world. Yet, here at your doorstep is the most real and feared monster of them all, Cancer, and you have no choice but to let it in.

Bald in the Land of Big Hair by Joni Rodgers
```

### Performance text (classify this)

```text
JONI: (Pg 1) When tomorrow was still a given and ignorance was still bliss, I was floating along like a paper sailboat on a lazy river, too caught up in my life to know that I was dying. But the day you're diagnosed with cancer, you stop dying and start surviving. You stop living and start staying alive.

JONI: (Pg 42-47) Dr. Ro made a concise explanation of the diagnosis: diffuse large-cell lymphoma, a high-grade, swiftly spreading cancer. (To Dr. Ro) So what does this mean? Does this mean . . . am I dying? (to audience) But Dr. Ro was reluctant to place a statistical probability on my survival, dodging the question with cautionary statements like . . .

DR. RO: This is a very serious situation. It is important that we move ahead quickly.

JONI: (to audience) Chemotherapy, she said, had proved successful in such cases, and she was ordering six to eight cycles, for starters. (To Dr. Ro) No, I don't want chemotherapy. I want to investigate my alternatives.

DR. RO: (bluntly) Your alternatives are chemotherapy or death. You have very good chance of getting remission with chemotherapy.

JONI: But I read in this book-it said chemotherapy is like removing a wart with a blowtorch.

DR. RO: That's not an appropriate comparison. A wart doesn't kill you.

JONI: (to audience) Her eyes never wavered from mine, and they held not a trace of apology, sympathy, or doubt. She laid out the gruesome possibilities in clinical nomenclature, couching blunt realities like "barfing" and "agony" in palatable terms like "nausea" and "discomfort." This was the first time I heard the word alopecia.

DR. RO: The loss of one's hair.

JONI: (to audience) The word that starts with B and rhymes with "appalled." (To Dr. Ro) It doesn't matter. That's the least of my worries. ******

JONI: (Pg 109) When I was diagnosed with cancer, Malachi [my son] was a savvy second grader. He was old enough to know facts, but young enough to struggle with implications and smart enough that there was no keeping the truth from him. He accepted with a silent nod each time we explained a new side effect or defined a new clinical term, and I would hear him at night, whispering in the dark.

MALACHI: Are you going to die, Mom?

JONI: (to Malachi) I’m trying not to. I promise I’ll do everything possible to stay here with you as long as I can. (to audience) Later, when I wasn’t too sure, I started adding something about how he was a part of me and I was part of him because he grew right out of my own body, so no matter what, I would always be with him.

(Pg 112-113) A child's life is made up of fragile combinations. The irresistible upward motion of precariously stacked building blocks. The intricate logic of a Tinker Toy Ferris wheel. The smooth symbiosis of peanut butter and jelly.

MALACHI: Mom . . .

JONI: I awoke to the feeling of a small hand patting on my cheek, but it took me a moment to open my eyes. (to Malachi) Sweetie, please. Mommy doesn't feel good. Just turn to the Disney channel, okay?

MALACHI: But I'm hungry.

JONI: Can you make yourself a PB and J?

MALACHI: No, you have to make it.

JONI: Sweetie, could you just give it a try? C'mon. Be my big boy.

MALACHI: Why can't you get up and make it? It'll just take a minute. Then you can lay down again.

JONI: All right. (to audience) I sat up on the couch and dragged my feet to the floor. A wave of nausea and dizziness engulfed me, and I rested my head forward in my hands. (to Malachi) Malachi, I can't. I'm sorry, sweetie, you're going to have to do it yourself.

MALACHI: (whining) Nooooo (pause, thinking) I don't feel good. I'm sick. You have to, Mom! You have to do it.

JONI: You're not too sick, Malachi, you're just too lazy. Now would you please . . . oh . . . Lord . . . (to audience) I struggled up from the couch and lurched toward the bathroom.

MALACHI: (groaning) Are you going to throw up again?

JONI: I closed the door behind me. In a little while, I heard the sound of the refrigerator door. Then the silverware drawer. Then a chair scraping across the kitchen floor. ******

JONI: (Pg 119-123) When I woke up the next day, Malachi wouldn't speak to me. I tried to jolly him through the first half of the morning, then let him avoid me until lunchtime. (to Malachi) Hey, Ike. Can I make you a PB and J?

MALACHI: I'm not hungry.

JONI: Oh, c'mon. I'll put more peanut butter on it. Way more. It'll be nice and messy.

MALACHI: Why don't you go lay down if you're so sick.

JONI: Well, thanks for your concern, Dr. Snidely, but I'm feeling better today. (to audience) Cringing at the cranky sound of that, I deliberately softened my tone and laid my hand on his head. (to Malachi) That was kind of rough yesterday, I know. But Dr. Ro said it's normal to be kind of rough the first few days after chemo, and then it gets better. (Kneeling to be on eye level) It gets better, right?

MALACHI: (Softly then gaining strength as he is overcome with anger and sadness) You're not sick! You're just lazy! You don't play -- you don't read books -- you just lay around on the couch all day! You don't want to go to the park or do art projects or science experiments like we always-"

JONI: Malachi, I still want to do those things, but some days it's too hard for me. (Pause) Ike, life is full of stuff we have a tough time understanding . . .

MALACHI: (Mimicking in a jeering falsetto) Life is full of stuff we have a tough time understand-ing.

JONI: Hey! (Grabbing his arm and jerking him close – she speaks harshly right in his face) I'm sorry this is hard for you, and someday you can tell your analyst how horrible it was having me for a mother, but in the meantime, I will not allow you to speak to me this way, do you understand?

MALACHI: (Pulling away) I think you like having cancer! I wish I had cancer!

JONI: (She slaps him hard, across the face) Don't you ever, ever say that again! (immediately appalled, she covers her face with her hands and cries)

MALACHI: (racing away to his room) I wish you would just die! (slamming the door to his room) I hate you!

JONI: But I hated myself more. After five minutes, a glass of water, and a few deep breaths

(take calming breaths), I followed him down the hall. (knocking gently on the door) Ike? Hey, can I come in? (no answer, after a moment she opens the door and steps inside) All right. First, I'm sorry I hit you. That was wrong, wrong, wrong, and I'm sorry. (silence) Malachi, I know you don't wish you had cancer. And I know you don't hate me. And I know that you know none of those other things you said are true. You're just mad because I'm sick, and that's -- it's just . . .

MALACHI: (eyes filled with tears and voice quivering) Mom, I don't want you to -- I don't wish -

JONI: I know. But I wouldn't blame you if you did. Because a few times lately . . . I've wished it myself. I've wished I would just die, Ike. There are times it seems like that would be easier. (to audience) He closed his eyes and shook his head, fighting not to cry. He tried to turn his face toward his pillow, but I pulled him onto my lap. (to Malachi) Malachi, I don't blame you for being mad at me. Everything's out of whack right now, and it seems like it's all my fault. But I really think I'm going to start getting better soon. And if I do die, it won't be because you wished it. Just the opposite. Every day I go on like this -- well, it's hard, Ike. And I don't know if I would have had the courage to do it if it wasn't for you. You make me want to stay alive. You're so full of surprises. I just have to stay around and see how you turn out. ******

JONI: (Pg 127) Trying to be an effective parent when physical and emotional reserves are depleted. The uncertainty and the painful truths that must be told. A child's grief and anger and fear. Though I couldn't see it at the time, Malachi's experience mirrored mine, emotion for emotion, challenge for challenge. He climbed his private mountain and came down changed, just as I did. Both of us discovered reservoirs of unexpected strength, but each of us left a little of our innocence behind.

(Pg 250-251) Someone sent me a little wooden plaque that said, "Adversity is a blessing." But I disagree. The overcoming of adversity is a blessing. Adversity is not a blessing. Adversity just sucks.

"Cancer is the definition of who I am now," said one survivor in a magazine article I read a while back. But if cancer is what we are, and all our efforts are bent toward killing cancer, then what's to become of us?

Cancer is not what I am. It's not a gift or a curse. It's not a blessing in disguise (unless that is one dang good disguise!). It's not the scourge of God, not the Red Badge of Courage, nor is it a purely clinical phenomenon. Personally, I like Malachi's definition: "Cancer is what happens when your cells decide to go funky." We are who we are, regardless of a few funky cells, and surviving cancer is the same as emerging from any of life's refining fires.

I'm still wondering if and when I'll ever "get over it." After all this time, cancer can still reach out and grab me with insidious tentacles of survivor's guilt, fears of reoccur-rence, and self-pitying fantasies of what might have been had the beast passed me by.
```

---

## IC-0087: The Beauty Inside

- Title: The Beauty Inside
- Author (byline): Catherine Filloux
- Work: The Best American Short Plays 2002-2003
- Publisher: Applause Books
- Publication date as stated: Nov 2007
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LATIFE, YALOVA, PERI
- Teaser before the introduction: Yes
- Spoken words (computed): 1674
- Already set (do not supply): none

### Source block (context only)

```text
Author: Catherine Filloux
Book: The Best American Short Plays 2002-2003
ISBN: 978-1557837202
Publisher: Applause Books
Date (Month/Year): Nov 2007
```

### Introduction (context only: never use it for content warnings)

```text
Hundreds, if not thousands, of women are murdered by their families each year in the name of family "honor." It's difficult to get precise numbers on the phenomenon of honor killing; the murders frequently go unreported, the perpetrators unpunished, and the concept of family honor justifies the act in the eyes of some societies. Complicity by other women in the family and the community strengthens the concept of women as property and the perception that violence against family members is a family and not a judicial issue. Females in the family—mothers, mothers-in-law, sisters, and cousins—frequently support the attacks. In The Beauty Inside by Catherine Filloux, a 14-year-old girl in southeastern Turkey is raped by a neighbor and becomes the victim of a botched “honor killing” at the hands of her family. In a terrifying clash of value systems, the girl's traditionalist mother and her Westernized female lawyer struggle with one another to seal her fate. The Beauty Inside by Catherine Filloux.
```

### Performance text (classify this)

```text
Cast of Characters (3 women)

YALOVA:, 14-year-old daughter of PERI:

PERI:, YALOVA:'s mother, clever

LATIFE: (pronounced La-tee-fay), lawyer

Place: Hospital, southeastern Turkey

Time: Present

[In shadow two figures drag a 14-year-old girl [YALOVA:] harshly by her hands and feet. These figures are played by PERI: and LATIFE:, but should be only dark shadows.]

YALOVA: He came at night! In the thick dark black, I always saw him eyeing me. "When I went to get the water. Bashed me down. Mud in my mouth. But something worse. So much worse! [The figures hurl Yalova who is now in rushing water.] Down there! Tumbling. Her inside me. Myself inside. That's all I can imagine. Too small. For this. Still playing games. With sticks. In the dark night. "When he comes. Still playing games at night. Till my mother calls me, "Yalova, to bed! My little [Screaming.] Yalovaaaa!" [Lights up on a hospital room. Yalova’s mother, Peri wearing a head scarf, is trying to drag Yalova out of the room.]

PERI: Yalovaaaa! My little one. Hurry! [Yalova is bandaged, severely hurt.]

YALOVA: Mama, they heard me crying. Down the river. The villagers came on their own. I did not call to them!

PERI: I myself will take you to the police.

YALOVA: I didn't tell the doctor, not yet, I promise ...

PERI: Quiet, you will tell them your brothers had nothing to do with it!

YALOVA: But rocks ... I bumped into rocks ... Did it hurt her?

PERI: That's enough! What good are you to us now? [Latife, a Westernized woman, rushes into the room.]

LATIFE: What are you doing to her? Get her back into that bed! Are you crazy?

PERI: This is not for you. There are certain things between a mother and daughter that are private.

LATIFE: Put her back in bed or I will get the police. Your sons left her for dead in that canal, Mrs. Bey.

PERI: She dishonored our family. [Latife struggles with Peri to get the girl, Yalova back into bed. Latife speaks to Yalova.]

LATIFE: Your two brothers are in jail. And your father, for ordering your killing.

YALOVA: Jail? No. Mama! I'm so sorry! [Peri changes tactics, helping Yalova into the bed.]

PERI: Now, now, hush, let me touch you. Does it hurt?

YALOVA: [Softly.] ... Does it hurt her, Mama?

PERI: Shh-shh, lie still, little one. [To Latife.] We must pray now. Would you please leave us alone to pray?

LATIFE: I will be just outside the door.

PERI: May I ask you for a small favor? She needs cold water. Would you bring us some? She is ill and my own throat is parched, I have walked so far in the hot sun, my village is very far away ...

LATIFE: I will need to speak to her. Do you understand?

PERI: The water. Please. You are very gracious, we are both unwell, please ...

LATIFE: I'll get water. [Latife exits. Peri whispers to Yalova so Latife won't hear.]

PERI: What have you done? Are you mad? [Shaking her.] Stupid foolish child!

YALOVA: They are not really in jail, Mama?

PERI: You went to the police. To shame us! You must go back now and say it was a story you invented. It is you who jumped into the canal to save yourself.

YALOVA: ... But he came, the neighbor. In the night. I was playing alone ... Mama ...

PERI: And what is inside you now? Bad, bad girl! [Peri starts to hit her]

YALOVA: Stop, Mama. I keep thinking why didn't you call me to bed a little earlier that night ... [Calling like her mother.] "Yalovaa ... " [Peri yanks Yalova back out of the bed.]

PERI: On the road we will ask for help ...

YALOVA: My head, it is turning ...

PERI: I, who fed you, sang to you when you cried ...

YALOVA: ... turning ...

PERI: What are you worth to us now?

YALOVA: The walls slipping ...

PERI: We can get no money for you!

YALOVA: What will you do to me? [Yalova slips to the floor.] Don't kick me, Mama. [Shielding her stomach.] Be careful ...

PERI: I will kill you right here! Then you will see what a curse you have brought on this family. I, all alone, without our men. I SAY GET UP AND WALK.

YALOVA: STOP IT, PLEASE! [Latife reenters with a pitcher and glass of water.]

LATIFE: [Furious.] Get away from her. Move away from her.

PERI: Let go of me. [Peri starts to hit Latife]

LATIFE: Move away from her, stop it!

PERI: I am her mother.

LATIFE: Mother? Kicking her like that.

PERI: What would you know of it?

LATIFE: Move away. [Throwing water at Peri] Now sit in that chair and stay until I am finished.

PERI: I will stand.

LATIFE: Stand at a distance.

PERI: Give me some water. [Latife fills the glass and hands it to her.] Give her some water. [Latife kneels next to Yalova]

LATIFE: Can you hear me? [Peri starts to approach Yalova again.] Don't you come closer, go back to the chair.

PERI: She needs a doctor. [Latife whispers to Yalova]

LATIFE: You did well to survive-thrown into an irrigation ditch. You floated at least a mile down the canal. [Yalova whimpers.] [Comfortingly.] Shh-shh. The villagers that rescued you said your cries were so loud, like an animal's. Like an animal they could not recognize. It was not your fault, you did well to tell the police. Right after they threw you in your brothers shot your neighbor ... the man who raped you. Your brothers hoped to kill you too ... No mind can wrap itself around such a thought.

PERI: She is with child. [Motioning to Yalova’ s stomach.] That is what happened. [Latife looks at Peri, then at Yalova]

LATIFE: [To Yalova] Really? [Yalova nods.]

PERI: Stupid girl.

LATIFE: Come, let me help you back into the bed, we need to call the doctor. [Yalova hallucinates.]

YALOVA: In the rain time there was silver on the canal.

LATIFE: Stand up, now, that's good.

YALOVA: Like a million fish.

LATIFE: One foot in front of the other.

YALOVA: Sun so bright on the silver, like blinding lights ...

LATIFE: Almost there, you'll rest ...

YALOVA: Don't go in the water, it's dirty, Mama told us ... How could something so beautiful be so dirty, just put a foot in, a toe ...

LATIFE: Let me put the blanket around you. You're not the only one, by far, but when the girl dies the crime disappears. Not with you,

YALOVA: How could something so beautiful be so dirty? [Peri gets up from the chair.]

PERI: My water is finished. [Obsequious.] I must approach, lady. If it is not asking too much. [To Yalova] You will go to the police and tell them your brothers and father are not to blame. To restore their honor.

LATIFE: And hers?

PERI: It is not for her to have.

LATIFE: Sometimes I ask myself, did I really come from this country?

PERI: [Disgusted.] You left.

LATIFE: No, I live here, in Istanbul. I've been here all my life.

PERI: Istanbul! [Latife faces Peri]

LATIFE: I will protect her now.

PERI: And our family? Will you protect us? Without a husband and sons I will become so poor I will survive on handfuls of dirt. All my village: "There goes the dishonored one." [She spits on Yalova] Rotten girl.

YALOVA: [Fainting] Mama ...

PERI: Don't call to me now.

YALOVA: If only you'd called ...

PERI: Too late, you should have come with me before when I told you to.

YALOVA: If only you'd called me a little earlier to bed that night. [Imitating her mother, calling.] "Yalovaaaa!"

PERI: Nonsense! You know what you must do to save us. [Peri puts her scarf over her head and exits, head bowed against the hot sun ahead. Latife stands a moment, then approaches the hospital bed.]

LATIFE: My name's Latife Inan. [She stands looking at Yalova who curls into herself] There are other girls. Perhaps in your village you heard rumors ... A girl who died because she brought dishonor on her husband, not getting permission to go to the movies. Another's throat cut because a love song was dedicated to her on the radio. I will return to the city to prepare your case. We'll place you under security protection. We'll send you somewhere where you'll be safe. When you're better you must agree to testify. Let me get the doctor ... [Latife starts to go. Yalova whimpers. Latife sees a little girl, in pain, with a baby inside her.] When I was a little girl my own mother died. She died in a car crash-if you ever go to Istanbul, you'll see that traffic lights are only there for decoration. They say my mother was the type to stop at them. So ... I was raised by men. My father, two brothers taught me how to excel, study hard, debate at the dinner table, defend my honor. I went to the best university, was lauded by my teachers, lauded especially by my father and my brothers, who always seemed giddy that I, a woman, their creation, succeeded so well, worked out so right. [Latife speaks with self-deprecation.] Now I am a senior lawyer, but there is no place to debate at the dinner table about people like you. Your fate is unthinkable to those who raised me. These men would never understand how in your belly will be your life, yourself; how that woman who walked out the door is still your heroine; how the canal you traveled down is both your road to freedom and the rope to hang you. That silvery mirage you speak of, just out of reach ... I will fight with what I have been given by those men who honor me so highly. For them it's all for common markets, but that's not what it is for me. I will have to fight this their way, the way my own father taught me, for you, Yalova.

Now let me go get the doctor. [Back to the rushing canal.]

YALOVA: And I was in it. Swirling. Diving. Gasping. I was in the canal. More than my toe. But my whole body. I screamed not for me. Because I would rather have drowned than dishonor my mother, My father, my brothers. Whom I loved so much. But I screamed. For her ... [She is holding a baby in her arms. It is in the future.] The girl I chose to call Latife. Born into a world of men.
```

---

## IC-0088: Beauty: When the Other Dancer is the Self

- Title: Beauty: When the Other Dancer is the Self
- Author (byline): Alice Walker
- Work: 75 Thematic Readings
- Publisher: McGraw-Hill
- Publication date as stated: Sept 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ALICE, BROTHER, DOCTOR, JIMMY
- Teaser before the introduction: Yes
- Spoken words (computed): 1411
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alice Walker
Book: 75 Thematic Readings
ISBN: 978-0072469318
Publisher: McGraw-Hill
Date (Month/Year): Sept 2002
```

### Introduction (context only: never use it for content warnings)

```text
The Prettiest . . . What does that mean? Physical features? Big eyes, glossy hair, high cheek bones? Rarely do you hear someone defining beauty as generosity, courage, kindness, and sense of humor.” At the age of two, Alice Walker, knew that physical beauty was definitely a selling-point. And she reveled in the role of being the “prettiest.” But how do you cope when a sudden accident renders you disfigured and you aren’t pretty anymore? Can you find the beauty within? Beauty: When the Other Dancer is the Self by Alice Walker.
```

### Performance text (classify this)

```text
NOTE: Speaker is an African-American woman

ALICE: It is a bright summer day in 1947. My father, a fat, funny man with beautiful eyes, is trying to decide which of his eight children he will take with him to the county fair. I am two-and-a-half years old. I want to go everywhere my daddy goes. I am excited at the prospect of riding in a car. Someone has told me fairs are fun. That there is room in the car for only three of us doesn't faze me at all. Whirling happily, showing off my biscuit-polished patent-leather shoes and lavender socks, tossing my head in a way that makes my ribbons bounce, I stand, hands on hips, before my father. (With assurance to her father) Take me, Daddy. I'm the prettiest!

.

ALICE: Later, it does not surprise me to find myself sharing the back seat with the other lucky ones. At home that night I tell the unlucky ones all I can remember about the merry-go-round, the man who eats live chickens, and the teddy bears, until they say: that's enough, baby Alice. Shut up now, and go to sleep.

It is Easter Sunday, 1950. I am six years old and have learned one of the longest Easter speeches to be heard that day. When I rise to give my speech I do so on a great wave of love and pride and expectation. People in the church stop rustling.

They seem to hold their breath. I can tell they admire my dress, but it is my spirit, bordering on sassiness, they secretly applaud. "That girl's a little mess," they whisper to each other, pleased. Naturally I say my speech without stammer or pause, unlike those who stutter, stammer, or, worst of all, forget. This is before the word "beautiful" exists in people's vocabulary, but "Oh, isn't she the cutest thing!" frequently floats my way.

It was great fun being cute. But then, one day, it ended.

I am eight years old and a tomboy. I have a cowboy hat, cowboy hoots, checkered shirt and pants, all red. My playmates are my brothers, two and four years older than I. We chase each other for hours rustling cattle, being outlaws, delivering damsels from distress. Then my parents decide to buy my brothers guns. These are not "real" guns. They shoot BBs. Because I am a girl, I do not get a gun. Instantly I am relegated to the position of Indian.

One day while I am standing on top of our makeshift "garage" --pieces of tin nailed across some poles--holding my bow and arrow and looking out toward the fields, I feel an incredible blow in my right eye. I look down just in time to see my brother lower his gun.

BROTHER: If you tell, we will get a whipping. You don't want that to happen, do you? Here is a piece of wire, say you stepped on one end of it and the other flew up and hit you.

ALICE: Confronted by our parents we stick to the lie agreed upon. First there is intense fever, Then there are chills: A week after the "accident" they take me to see a doctor.

DOCTOR: (Looking into the damaged eye and shaking his head) Why did you wait so long to come? Eyes are sympathetic. If one is blind, the other will likely become blind too.

ALICE: This comment of the doctor's terrifies me. But it is really how I look that bothers me most. Where the BB pellet struck there is a glob of whitish scar tissue, a hideous cataract, on my eye. Now when I stare at people--a favorite pastime, up to now--they will stare back. Not at the "cute" little girl, but at her scar. For six years I do not stare at anyone, because I do not raise my head.

I am eight, and, for the first time, doing poorly in school, where I have been something of a whiz since I was four.

I am twelve. I abuse my eye. I rant and rave at it, in front of the mirror. I plead with it to clear up before morning. I tell it I hate and despise it. I do not pray for sight. I pray for beauty.

I am fourteen and baby-sitting for my brother Bill, who lives in Boston. He is my favorite. Understanding my feelings of shame and ugliness he and his wife take me to a local hospital, where the "glob" is removed. There is still a small bluish crater where the scar tissue was, but the ugly white stuff is gone. Almost immediately I become a different person from the girl who does not raise her head. Or so I think.

Now that I've raised my head I win the boyfriend of my dreams. Now that I've raised my head I have plenty of friends. Now that I've raised my head classwork comes from my lips as faultlessly as Easter speeches did, and I leave high school as valedictorian, most popular student, and queen, hardly believing my luck.

Ironically, the girl who was voted most beautiful in our class (and was) was later shot twice through the chest by a male companion, using a "real" gun, while she was pregnant. But that's another story in itself. Or is it?

It is now thirty years since the "accident." [And] I remember:

I am talking to my brother Jimmy, asking if he remembers anything unusual about the day I was shot. He does not know I consider that day the last time my father, with his sweet home remedy of cool lily leaves, chose me, and that I suffered and raged inside because of this.

JIMMY: Well, all I remember is standing by the side of the highway with Daddy, trying to flag down a car. A white man stopped, but when Daddy said he needed somebody to take his little girl to the doctor, he drove off.

ALICE: I remember:

[Being] in the desert for the first time. I am so overwhelmed by its beauty, I confront for the first time, consciously, the meaning of the doctor's words years ago: "Eyes are sympathetic. If one is blind, the other will likely become blind too." I realize I have dashed about the world madly, looking at this, looking at that, storing up images against the fading of the light. But I might have missed seeing the desert! The shock of that possibility--and gratitude for over twenty-five years of sight--sends me literally to my knees.

But mostly, I remember this:

I am twenty-seven, and my baby daughter is almost three. Since the birth I have worried about her discovery that her mother's eyes are different from other people's. Will she be embarrassed? I think. What will she say? Every day she watches a television program called Big Blue Marble. It begins with a picture of the earth as it appears from the moon. It is bluish, a little battered-looking, but full of light, with whitish clouds swirling around it. One day when I am putting Rebecca down for her nap, she suddenly focuses on my eye. Something inside me cringes, gets ready to try to protect myself. All children are cruel about physical differences, I know from experience. I assume Rebecca will be the same.

But no-o-o-o. She studies my face. She even holds my face maternally between her dimpled little hands. Then, looking every bit as serious and lawyerlike as her father, she says gently, but with great interest: "Mommy, where did you get that world in your eye?"

For the most part, the pain left then. Crying and laughing I ran to the bathroom, while Rebecca mumbled and sang herself to sleep. Yes indeed, I realized, looking into the mirror. There was a world in my eye. And I saw that it was possible to love it: that in fact, for all it had taught me of shame and anger and inner vision, I did love it. Even to see it drifting out of orbit in boredom, or rolling up out of fatigue, not to mention floating back at attention in excitement, deeply suitable to my personality, and even characteristic of me.

That night I dream I am dancing. As I dance, whirling and joyous, happier than I've ever been in my life, another bright-faced dancer joins me. The other dancer has obviously come through all right, as I have done. She is beautiful, whole, and free . . . And she is also me.
```

---

## IC-0089: Because I am Furniture

- Title: Because I am Furniture
- Author (byline): Thalia Chaltas
- Work: Not specified
- Publisher: Viking Juvenile
- Publication date as stated: Apr 2009
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 2110
- Already set (do not supply): none

### Source block (context only)

```text
Author: Thalia Chaltas
ISBN: 978-0670062980
Publisher: Viking Juvenile
Date (Month/Year): Apr 2009
AWSARD HISTORY
2019 National Qualifier
CO State Qualifier
KS State Qualifier
```

### Introduction (context only: never use it for content warnings)

```text
We often hear stories from the perspective of those who are abused, but what does it feel like to be the one child in the family who is ignored, forgotten, and left feeling powerless to help the ones you love? What is it like to have no voice? Anke is the youngest of three siblings. Welcome to her life of silence . . . and bear witness . . . Because I am Furniture by Thalia Chaltas
```

### Performance text (classify this)

```text
I am always there. But they don't care if I am because I am furniture.

I don't get hit
I don't get fondled I
don't get love
because I am furniture.

Suits me fine. (pg 3)

Quiet and earnest, he is squatting in front of me. I hunch on the couch.

"I know you think you want to play volleyball.

--- aren't I already? Competition creates a false sense of empowerment,

an I’m better than you euphoria

believe me. I know.
I wouldn't want you to get caught up in that,
the hunger for control over others.
When I was young blah blah blah blah

My eyes watch his thin lips moving against

each other in silence,
and I know
that Darren and Yaicha were right
when they once used our father to teach me the

meaning of the word hypocrite. (Page 51-52)

Dinner.

He knocked Darren onto the linoleum.

I don't remember his arm swing, just Darren and his chair -- eight tangled limbs on the floor.

No reason that I could see.

But my father picked up his reasons and his

plate and went to eat in the living room.

Darren picked up his chair and himself and we are now eating in customary ice-age silence. (pg 5)

His Anger stands alone
stands erect
in the
middle of the room.

We step gently around it, a terrifying totem pole bristling beaks, pinions, talons.

I can't remember when it started when firm hand

became

fisted liege

became

feral

tyrannical

rage

more important than

the rest of us,

but
it didn't used to be this way
and that
keeps us tied to him,
guessing,
teetering,
waiting,
while stepping around
his Anger
in the
middle of the room. (125-126)

He's losing it bad tonight,
the second time this week,
chasing Yaicha out of the kitchen
holding his chair over her head-

she cowers on the living room rug.

I am close behind mom, but it's not like I can ever do anything.

No one sees me.

Mom gets him to stop,

with taut and twisted face, open hands, before the chair comes down.

Yaicha runs.

He sits down, tired, and says to mom, "I'm sorry you had to see that."

Inevitable that he does it.

But he doesn't really want a witness. (page 19-20)

My Father,
Who Art Not in Heaven,
and never will be,
sometimes
doesn't come home
from work
until two a.m.

and for his own reasons goes to my sister's room

before he goes to his own bed.

I don't want to
hear
know
live here.

I am scared for her but I am so glad he doesn't

come to my room. (Page 39-40)

Little packet by Yaicha's bed

I've seen them before--

Marci takes the pill before school

laughing in the girls' room,

proof of her

extracurricular

activities

But I overheard Yaicha tell her friend she's a virgin, never even had a boyfriend,

so I don't get it.

And she storms in snatches the packet raging about privacy.

Bubbling panic I go on the offensive –

"Why should you take the pill?"

My insides shred as she glares a full minute

and I stand my ground
wanting her to tell me
tell me
anything,

but when I see pain forming on her retinas

I decide I don't want to know. I run. (109-110)

I mean, WHY can't she just tell on him? It's just words.

Just open her mouth and out come those words.

And then he'd be stopped.

Right? (pg 163)

Darren came into the kitchen
this morning,
black circles
around wavering eyes,
and he wouldn't look at any of us.

Mom said he was sick

but he's not sick. I've seen this a few times before

always after he and my father fight

and then

my father "talks" to him in private

in his room for hours

but most of the time I don't hear their voices (page 146-147)

Why am I not good enough?

At least he loves Darren and Yaicha in some way

even if it's horrible, he shows them attention

and I am furniture
I get nothing
nothing
nothing
no
thing

or
at times I get
a knife-edge glimpse of
something scary.

I think that it is supposed to be good, that I get less from him

but I feel . . . worth less. (105-106)

. . . and i'm jealous!
with a sick
acidic
burbling
bile
i want what they have

as horrible
curdling
vile
as it is
darren and yaicha get more
than
me. (pg 235)

Yanking jeans over sweaty skin,
I come out of my room,
Darren comes up the stairs,
and our father comes from the bathroom,

a damp bath towel dangling

from forefinger and thumb.

"Whose." he intones at me in the hallway,

"is this?"

Darren holds out his hand. "Mine," he whispers.

Our father looks surprised. Did he think it was mine?

He breathes in, launches the offensive at Darren. "HOW MANY TIMES HAVE I TOLD YOU TO

HANG THIS ... "
louder and louder
words crushing together
in a piling roar
"YOU THINK YOU CAN JUST DO WHAT YOU

WANT ... " "I AM THE ONE WHO KNOWS WHAT'S GOOD

FOR YOU ... "

I want to make him turn to me yell at me

I want to yell at him

I am here

right here

I am not furniture --

But when his hand smothers Darren's face with the wet towel, shoving him hard into the wall,

I am backing away. (177-179)

Yaicha is crying gently in the bathroom. (pg 231)

It just occurred to me.

It's her choice.
Yaicha chooses not to tell anyone
and Darren does too
and Mom.

Am I the only one bothered by this? I mean bothered enough to think about it?

So all the pressure is on me,
the Youngest and Most Bothered.
Or maybe I am just
outside enough,
being the footstool observing from the corner,
that I have a view of reality.

And I can't stand it anymore.

Why me? I don't need this crap

Then

why don't I tell on him?

If they don't, why don't I? Because.

Because I am safe this way, silent unnoticed.

Because my family would crack snap shatter

like pine boughs in an ice storm jagged pieces scattered, irreparable,

and there would be no family and I don't want that on my head.

What we have is better than that.

Right? (239-240)

TRANSITION

Confusion, feelings of worthlessness, fear . . . such strong feelings can only be locked inside for so long. A catalyst is all that is needed to force these emotions to the surface – It is then that the “furniture” finds a voice - - A branch can bend only so far before it breaks . . . And once Anke develops a friendship outside her family, Angeline becomes that catalyst and Anke finds her voice.

"Your father must have
info like that."
Angeline is at me
again.

Mom is making me work with her on topics for government

"He must have
books and books,"
Angie is pleading.
"He's a professor."

I'm not asking him for anything.

I want to say,

Get over your goddamn crush,

Angie,

you have no idea

who he is. But my jaws clamp.

" I'll call him." she offers.

Well why not? She's already more a part of my family than I am. (266-267)

I am annoyed
when Angeline comes,
clutching her pale pink sweater,
breathlessly spilling
that we could pick up government law info
at my father's office.

"He said 'Sure’” she squeals.
He’ll leave a folder on his desk because,
sigh,
"he might have a meeting."
She is is briefly bereft.

I say I’ll meet her in the lobby

"Oh, I told him I'd go, I don't mind."

Grrrr.
He is my father.
"No, I'll meet you," I throw at her retreating back
but she's gone.

"Why don't you just frickin' move in with us,"

I say out loud.

I'll be glad when this government thing is over,
this annoying extracurricular supposed honor
that forces me to spend
even more time
with Angeline. (300 - 301)

I'm a little late getting to my father's building.

I scan for Angeline in the lobby then sprint up the three flights. Coming to the DR. LARUS FELD etched on his

frosted door,
Tapping lightly,
turning the knob,
the door swings in silence, fangs of light

glinting in the glass.

Then I hear -- I hear something soft crying somewhere.

Angeline?

Sneakers on carpet,

carpet,

carpet,

lean around the bookcase. –

My
father with a small smile
leaning toward the armchair,
zipper on its way clown,
Angeline, her skirt tweaked,
swelling closing one eye,
pleading softly, no, no.

"NO!"
Dr. Feld is shock still.
I take another lungful,
"NO!"

Angie slides to standing,

gathering her book bag,

running for the exit. Raising brows, he mocks me, but, dammit, he will hear me,

"NO!"

Slamming by the bookcase
tearing through the doorway
pounding down the stairwell,
no-no-no-no,
NO--NO--NO. (302-304)

By the brook
with a crunch of fine ice,
I double over,
dry heaves
on my knees.

What did I see? What did I see in his office?

How could he, to poor Angeline?

I sink onto a rock near the water,
taking a blood-red
maple leaf
and dunking it under,
holding it beneath the frigid liquid.

Poor Angie.

She was supposed to be outside our

house of horrors
and I let her in.
I should have kept her away from him.
He went outside.

And the tears burst through
heavy as mercury,
heated by guilt,
and I take the leaf out of the water,
sobbing.

Angeline, Angie, I'm sorry (306-307)

Pushing open the bathroom door I take two steps toward Yaicha who is wrestling with her hair.

"I saw him hurt Angeline."

The brush stops moving.

"At his office today." Small sounds

like a dying cricket come from Yaicha's lips. “I’m sure you were mistaken." she says

to her brush.
"MISTAKEN?
I know who Angie is, Yaicha.
I know who our father is, Yaicha.
He hurts people, he hurts you,

you never do anything!" My claws scrape the wall paint.

She turns with soft rabbit eyes. "He'll kill me."

"He's already doing that!"
I am growling, grabbing her sleeve,
"Every day,
every day he rips you open,
chips off pieces week by week,
till a few years from now you are not even a

mouthful of sawdust.
A drawn-out killing.
Well, I'm tired of all of us doing nothing.
He has to be stopped."

Yaicha's eyes have flinched a few times but soften again. "Nobody can stop him."

"Nobody can stop him?
Good.
To him I have always been
Nobody." (311 - 313)

They all swivel to me -- Mom, Darren, and Yaicha --

Footfall,
Darren frozen, eyes on the baseboard,
Yaicha melted against the stereo cabinet,
as he steps lightly up the stairs.

"Sorry I couldn't give you
a ride home,"
he says to me,
sliding into the living room
with his briefcase,

"I had a meeting.”

His eyes dare me. Dare me. (319-320)

Slow motion twitching

twitching

hissing burning

blood pushing

itching skin

pushing out

something scary

pushing out something stronger. (321)

I stand behind his chair. "Liar,"

under my breath.

His eyebrows rise,

pupils sharpen.

"You weren't at a meeting,"

take a breath, gain speed, bursting,
"You were with Angie in the office.
I saw you. I saw you.
You clamp us down,
you think no one knows.
You hurt my brother! My sister!
You hurt my friend! Small trusting prey, huh?
You could have chosen to hurt me!

But I'm not worth enough I never am

and you picked poor Angie,

you were going to RAPE her,

I SAW YOU TRY TO RAPE ANGIE,

you f***ing MONSTER!"

I shove his chair forward

with the force of my words,

the wooden leg touches

his foot.

Stillness. Shaking.

White-faced, cold,

slowly

he picks it up by the seat.

Suddenly spinning the chair in air

he smashes it on me hard –

with a great crack
I go down,
splinters of wood
splinters of bone
my leg showing bone,

and finally I roar. (322-323)

Where is the safe, cuddling daddy who sang “I’m Being Swallowed by a Boa

Constrictor" to me

when I had a fever?

Was that man molted off
like scales that no longer
lie smoothly
around the shape of what he has become?

I want my daddy back.

Too bad for me. (316)

He's been arrested.

In jail.

Such an odd disconnect

to feel so relieved and so guilty,

yet so cold about the whole thing, like concrete, like a nuclear reactor decommissioned

and left by itself to withstand the

winter.

I wonder if he has to wear one of those

bar-striped suits. (329)

I did it.
I filed
a restraining order
against
my own father.

He's out on bail and needs more than restraining.

But it's
a damn good
start,
and
I did it. (331-332)
```

---

## IC-0090: Bed Among the Lentils

- Title: Bed Among the Lentils
- Author (byline): Alan Bennett
- Work: Not specified
- Publisher: Samuel French, Inc.
- Publication date as stated: Feb 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: GREGORY, SUSAN, RAMESH
- Teaser before the introduction: Yes
- Spoken words (computed): 1654
- Already set (do not supply): none

### Source block (context only)

```text
Author: Alan Bennett
ISBN: 978-0573132247
Publisher: Samuel French, Inc.
Date (Month/Year): Feb 1998
```

### Introduction (context only: never use it for content warnings)

```text
Life for Susan, wife of Geoffrey the vicar, is complicated. She is always expected to be on parade. Why? Actor’s wives don’t come to every performance; a barrister’s wife isn’t always in court – why should she be expected to be present at every service? It’s very stressful, especially if you are hopeless with the church flowers, can’t run a tight rummage sale, and you’re an awful cook! She has to find ways of dealing with the stress. Bed Among the Lentils by Alan Bennett
```

### Performance text (classify this)

```text
Recommend British accent . . .

I stand up and say, 'My name is Susan. I am a vicar's wife and I am an alcoholic'. Then I tell my story. Or some of it anyway. 'Don't pull any punches', says Clem, my counselor. 'Nobody's going to be shocked, believe me, love, we've all been there.' But I don't tell them about Mr. Ramesh because they've not been there. 'Listen, people. I was so drunk I used to go and sleep with an Asian grocer. Yes, and you won't believe this. I loved it. Loved every minute'. Dear oh dear. This was a real drunken lady.

Geoffrey's bad enough but I'm glad I wasn't married to Jesus. The lesson this morning was the business in the Garden of Gethsemane when Jesus prays and the disciples keeps falling asleep. He wakes them up and say, "Could you not watch with me one hour?" It's my mother.

The sermon was about sex. I didn't actually nod off, though I have heard it before. Marriage gives the OK to sex is the gist of it, but while it is far from being the be all and end all sex is nevertheless the supreme joy of the married state and a symbol of the relationship between us and God. SO, Geoffrey concludes, when we put our money in the plate it is a symbol of everything in our lives we are offering to God and that includes our sex. I could only find 10 pence.

Amazing scenes at the church door. Geoffrey stands there the wind billowing out his surplice and ruffling his hair, what "Who's Who in the Diocese of Ripon' calls 'his schoolboy good looks'. I helped put away the books while he did his 'underneath this cassock I am but a man like everybody else' act. Mrs. Shrubsole burble, 'We must cherish him'.

We came back and I cherished him with some chicken wings in a tuna fish sauce.

GREGORY: 'That went down well'.

SUSAN: 'The chicken wings?'

GREGORY: 'My sermon. I felt it hit the nail on the head'. He put his hand over mine, hoping, I suppose, that having hit one nail he might hit another, but I said I had to go round with the parish magazine. Geoffrey was off to Evensong, was I going to come?

One of the unsolved mysteries of life, or the unsolved mysteries of my life, is why the vicar's wife is expected to go to church at all. A barrister's wife doesn't have to go to court, an actor's wife isn't at every performance so why have I always got to be on parade? Not to mention the larger question of whether one believes in God. To look at me, the hair, the flat chest, the wan smile, you'd think I was just cut out for God. And maybe I am. I'd just like to be asked that's all. It could be that Geoffrey doesn't believe in God either. I've always longed to ask him only God never seems to crop up. 'Geoffrey do you really believe in God? I mean, God's just a job like any other. You've got to bring home the bacon somehow'. But no. Not a word. The subject's never discussed.

After he'd gone, I discovered we were out of sherry so I drive into Leeds. There's a little Indian shop behind the Infirmary I've found--it sells drinks and anything really, the way they do. Open last thing at night, Sundays included, my ideal. Ramesh he's called, Mr. Ramesh, whose first name turns out also to be Ramesh. Ramesh Ramesh. --Though Ramesh may be his Christian name. Only not Christian of course. I've been twice now, only this time he sits me in the back place on a sack of something and talks. He's married apparently, but his wife's only fourteen so they won't let her in. Little statuette of God on the wall. A god, not The God. One of several thousand apparently. "Safety in numbers', I said but he didn't understand. He calls me Mrs. Vicar. He has lovely teeth.

Once upon a time I had my life planned out…I was all set out to turn into a wonderful woman… equipped with the skills necessary: how to produce jam, how to whip Victoria sponge, how to plan and carry a successful garden fete. But I can do none of these things. I'm even a fool at the flower arrangement.

On this particular morning, I'm paired with Mrs. Shrubsole to do the altar and the lectern. My honest opinion, never voiced needless to say, is that if they were really sincere about religion they'd forget flower arrangement altogether and put the money towards the current most popular famine. However, I wander over with a few dog-eared chrysanthemums. They look as if they could do with an immediate drink so I call in at the vestry and root out a vase or two from the cupboard where Geoffrey keeps the communion wine. I assume I am doing the alter and Mrs. Shrubsole the lectern, but when I wonder out of the vestry Mrs. S is at the altar well embarked on her arrangement. She smiled sweetly, 'Do you have a preference'? The only preference I have is to shove my chrysanthemums up her nose but instead I practice a bit of Christian forbearance and retire to the vestry for a bit to calm my shattered nerves, and when I come out, Mrs.

Shrubsole has apparently finished. So I wander up and take a look, 'Mrs. Shrubsole. This is not a floral arrangement. This is a booby trap! Permit me to demonstrate'. And I begin getting down on my knees, only I must have slipped because next thing I know I'm rolling down the altar steps and end up banging my head on the communion rail.

When I woke up I got the car out and drove to Leeds. I sat in the shop a bit, not saying much. Then I felt a bit wanny and Mr. Ramesh let me go into the back place to lie down. I must have dozed off because when I woke up Mr. Ramesh has come in and started taking off his clothes.

SUSAN: 'What are you doing?'

RAMESH: 'I have closed the shop.'

SUSAN: 'It's only nine. You don't close till eleven'.

RAMESH: 'I do tonight--a chance in a million, a turn up for the books. Will you take your clothes off please?' And I did.

We made love there among the lentils on the second Sunday after Trinity.

'So how did you come to AA'? they ask. 'My husband', I say. 'The vicar. He persuaded me'. But I lie. It was not my husband, it was Mr. Ramesh, the Mr. Ramesh who one Sunday night turned his troubled face towards me with its struggling moustache and asked if he might take the bull by the horns and inquire if intoxication was a prerequisite for sexual intercourse, or whether it was only when I was going to bed with him, the beautiful Mr. Ramesh, twenty six, with wonderful legs, whether it was only with him I had to be inebriated. And was it, asked his slim, flawless and troubled creature, was it perhaps his color? Because if not he would like to float the suggestion that sober is even nicer. So the credit for the road to Damascus goes to Mr. Ramesh.

So now everything has changed. For the moment I am a new woman and Geoffrey is a new man. And he brings it up on the slightest pretext. 'My wife's and alcoholic, you know. Yes. It's a great challenge to me and to the parish as extended family'. From being a fly in the ointment I find myself transformed into a feather in his cap. Included it in his sermon on Prayers Answered when he reveals that he and the fan club have been having these jolly get togethers in which they'd all prayed over what he calls 'my problem'. We were at some doleful diocesan jamboree last week and I'm stuck there clutching my grapefruit juice as Geoffrey's telling the tale to some bearded cleric. Suddenly he seizes my hand. 'We met it with love', he cries, as if love were some all-purpose antibiotic, which to Geoffrey it probably is.

I've caught the other young, upwardly mobile parsons sneaking looks at me now and again and you see them thinking why weren't they smart enough to marry an alcoholic, problem wives whom they could do a nice redemption job on, right there on their own doorstep. Because there's no stopping Geoffrey now. He grips my hand in public, nay brandishes it. 'We're a team', he cries. Looks certain to be rural dean and that's only the beginning. As the bishop says, 'Just the kind of man we're looking for on the bench… someone with a seasoned compassion, someone who's looked life in the face. Someone who's been there'.

Mr. Ramesh sold his shop. He's gone back to India to fetch his wife. She's old enough now apparently. I went down there on Sunday. There was a boy writing Under New Management on the window. Spelled wrong. And something underneath in Hindi, spelled right probably. He said he thought Mr. Ramesh would be getting another shop, only in Preston. They do that of course, Asians, build something up, get it going nicely, then take the profit and move on. It's a good thing. We ought to be more like that, more enterprising.

My group meets twice a week and I go. Religiously. And that's what it is, of course. I never liked going to one church so I end up going to two. Geoffrey would call that the wonderful mystery of God. I call it bad taste. And I wouldn't do it to a dog. But that's the thing nobody ever says about God… he has no taste at all.
```

---

## IC-0091: Before Fergus

- Title: Before Fergus
- Author (byline): Lynn Ferguson
- Work: The Moth Presents Occasional Magic, Pg 36-45
- Publisher: Crown/Archetype
- Publication date as stated: Mar 2019
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LYNN
- Teaser before the introduction: Yes
- Spoken words (computed): 1560
- Already set (do not supply): none

### Source block (context only)

```text
Author: Lynn Ferguson
Book: The Moth Presents Occasional Magic, Pg 36-45
ISBN: 978-1101904428
Publisher: Crown/Archetype
Date (Month/Year): Mar 2019
```

### Introduction (context only: never use it for content warnings)

```text
Congratulations! You are expecting a baby! The time has come for the 20-week scan -- when names have been chosen, tummies are swelling and babies are kicking. The 20-week scan -- the opportunity to find out, will our child be a boy or a girl? But the 20-week scan is also called the “anomaly scan.” Its intention is to determine if the baby is developing properly. You see, especially for women who conceive later in life, the risks of chromosomal birth defects exponentially increase.

In this selection, Lynn Ferguson is given a number of choices. Choices that will determine the fate of her family and her unborn child. Choices that, with the overturning of Roe v Wade, are no longer options for women in America. Lynn shares her personal stance on the issue of terminating a pregnancy: “I think it's a matter of choice . . . and I am completely and utterly pro-choice.”

Before Fergus by Lynn Ferguson
```

### Performance text (classify this)

```text
LYNN: I’m Scottish. A friend of mine is Bosnian, and he married a Serbian, and together they had a child. They had to flee their country, because their child -- being of mixed race -- was in danger by just being. They called their son Trim, which means "courage."

My friend said he called his son "Courage" because he felt that as soon as the child was born, he' cl lost all of his own courage, and that anything that he' cl fought for in his previous life had gone, and now he’d fight for nothing but the life of that child.

You know, I've thought about that a lot since I've had my son.

LYNN: I was thirty-seven when I first fell pregnant. Well, I didn't fall pregnant. There wasn't some incident with a sidewalk and a flip-flop. I did stuff. I got pregnant. I was thirty-seven. The discovery wasn't the kind of romantic one you get in black-and-white movies. I had been touring France on the back of a motorcycle with my husband when I started to feel a bit unwell.

Now, a word of advice: if you're feeling sick, don't do it at eighty miles an hour, leather pants on one end, crash helmet on the other, in a country where they eat snails because they can.

I've heard it said that you feel most like a woman when you're pregnant. It's complete rubbish. It's not so. I felt most like a beached whale. It's a completely bizarre thing, because you suddenly find yourself entirely responsible for this other person. And this other person has only got you, and so even though the two of you are together twenty-four hours a day, it's not like you can have a discussion about it.

Before I got pregnant, my greatest fear about getting run down by a car was that I wouldn't be wearing matching underwear. After I got pregnant, the whole idea of getting run over by a car took on a whole different meaning. Never mind the eating for two, it's the thinking for two that wears you out, you know?

There was a lot of difficulty around my pregnancy, because thirty-seven is considered quite an old age to be having your first child. So almost as soon as everybody agreed that I was in the family way, they decided that I should have an amniocentesis. An amniocentesis is an invasive test where they put a needle through the mother's belly and into the amniotic fluid, and it can tell you whether the baby has Down syndrome or not. But there's also a 1-percent risk that it will cause damage to the fetus or the fetus will miscarry.

Now, I'm totally not against risk; I think it's a matter of choice, and I like risk, and I am completely and utterly pro-choice. But there was no way they were going to do it. It wasn't the baby's fault I was thirty-seven. That was entirely on me. So, I was like, No. But every appointment it would come up, and initially I would deal with it that way you do when you don't want to have coffee with someone.

"Oh, the amniocentesis -- we will, we'll do it. I can't do it this week, though. Maybe next week? Oh, no, my mother's coming. No, I can't do that." But as they became more insistent about it, I kind of felt like I had to, too.

So, I was like, "You know, can this test tell me whether this child will be a jerk? Can your test tell me whether this kid is going to be one of those really screamy ones that annoys everybody on airplanes? Because I'm worried about Down syndrome, hands up, but I'm pregnant, and I'm worried about a lot of things. So, thanks very much and everything, but no."

Then came the twenty-week scan. We were told we were having a boy. Woo-hoo! Then the lady scanning the baby said that my son had statistically a very large head. I looked across at my husband for the first time, I swear, noticing his statistically large head. I silently cursed love for being blind.

She told me I was thirty-seven. I knew that.

Then, scanning the baby's head, she said there were choroid plexus cysts all down one side of the baby's brain. Okay. That wasn't something I was expecting. We were told that everything was going to be "fine," in that way where you just know it's not, and we had to wait for a specialist.

The specialist we went to see told us we were having a boy. We knew that. She told me I was thirty-seven. I know. She said the baby had a statistically large head. Then she said that the choroid plexus cysts were a problem. We'd kind of guessed that. And then, scanning the baby again, she said that there was a vessel missing on the umbilical cord.

She said we needed to do the test. But because I had waited so long, they didn't want to do an amnio, they wanted to do something called a cordio, which is pretty much the same as an amnio. They insert a big needle into the womb, and they take a little bit of the umbilical cord, and that can tell them what's going on with the baby. Now, this is an umbilical cord that they have just told me isn't fully functioning.

We didn't even need a discussion for the decision. I was like, "Okay, the Down syndrome thing, it's not exactly what we'd planned, and I know it's going to be difficult, probably -- for us and for him and in ways that I don't even know yet. But actually, personally, I think there are worse things than having Down syndrome, you know? "I mean, having Down syndrome doesn't mean you're a bad person, does it?" So I said no.

But that's when they told me that Down syndrome was off the table and what we were talking about now was Edwards, a syndrome that means the baby will likely die, either in the womb or within the first year of life.

We'd had so many scans, and I'd seen my son. I'd seen his heart, seen the inside of his eyes. I'd seen his hands and his feet, and in fact, during one of the scans, he'd held his hand out to the front of my body as if to say, Will you go away? I'm busy. Do not disturb.

I'd felt my son move inside my body. What did it matter whether he had a disorder or not? And if he was going to die, well, we're all going to die, right? So, we should meet first. He was my son, and he needed me. He was depending on me to make the right decision. So, I said no.

We had no choice but to change hospitals after they offered me a termination at twenty-five weeks. It became really clear that they wanted to win a battle, and I just wanted to see my boy.

At precisely thirty-five weeks and five days, my son decided it was time to be born. My husband drove us to the hospital in our car, neither of us talking about what lay ahead.

The conversation was made up of the same four phrases: "Are you okay?" "Yeah." "You do know I love you?" "Yeah."

The birth process was the true definition of laborious. My husband gave me water and held my hand, and the midwives were brilliant. They were patient and reassuring. It would be okay, they said, everything was really early, but it would be okay.

I have no idea how long labor lasted, but eventually, my son appeared -- shot out, in fact, doing a kind of hand-brake turn on the table as he did so. He was purple in color, and my husband cut the cord. But whereas before there had been noise and bustle and shouting, suddenly there was silence. It was like the whole world had gone underwater.

The door burst open, and people in white coats came in. They bundled my son over onto a metal table, where they hurriedly tried to resuscitate him.

I had failed my son. He was depending on me, and I had failed him, and the whole world was underwater.

Then suddenly he choked, gagged, coughed up something, and started to breathe. The people in the white coats wandered off, and with my husband standing next to me, they handed me my son.

He. Was. Perfect.

"Fine," they said. "He's absolutely fine."

My son looked up at me. He was curious. He was amazing. He looked up at me as if to say, Ooh, that was all a bit of a trial.

"I am so glad you're here," I said.

My son is ten years old now, and he's still perfect (some of the time). And, like his father, he still has a statistically large head.

I haven't seen my Bosnian friend for such a long time, but I often wonder how he's getting on in his self-imposed exile. I called my son Fergus. In Irish it means "the right choice," but it has a different meaning in Scottish. It means "courage,” too.
```

---

## IC-0092: Before Women had Wings

- Title: Before Women had Wings
- Author (byline): Connie May Fowler
- Work: Not specified
- Publisher: Ballantine Books
- Publication date as stated: April 1997
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BIRD, BILLIE, GLORY, PHOEBE
- Teaser before the introduction: Yes
- Spoken words (computed): 1187
- Already set (do not supply): none

### Source block (context only)

```text
Author: Connie May Fowler
ISBN: 978-0449911440
Publisher: Ballantine Books
Date (Month/Year): April 1997
```

### Introduction (context only: never use it for content warnings)

```text
(Sing)
```

### Performance text (classify this)

```text
BIRD: (Pg 1-3) Back in 1965, on a day so hot that God Almighty should have been writhing with sick-to-the-stomach guilt over driving His children out of the cool green of Eden, my daddy walked into our general store, held a revolver to his head, told my mama, Glory, that he couldn’t take any more and that because of her harsh ways and his many sins he was going to blow his brains out.

*Some bright morning when this life is over
I’ll fly away
To that home on God’s celestial shore
I’ll fly away

I’ll fly away oh glory
I’ll fly away
When I die hallelujah by and by
I’ll fly away
Before Women had Wings by Connie May Fowler

BIRD: I was six years old, and I prayed that my guardian angel, who so far in my life had proven to be an elusive helper, would materialize. Prayerful words welled up inside me, whirled through my head: Please angel, whisk me away. Take me to your house in the clouds, just for a little while, just for today.

BILLIE: (Crying, voice loud and trembly) Glory, I mean it. I’m sick and tired of trying to make it in this godforsaken world. You and the girls will be happier with me gone.

BIRD: Daddy’s voice was loud, trembly. He was crying. I shut my eyes, and on the backs of my eyelids I saw Mama get up from behind the desk and put her arms around Daddy and coo, “Everything is going to be fine. Yes, baby, I love you. Your daughters love you.” If I’d been her, I would have done that.

But my daydream did not come true. When I looked again, Mama was still sitting. When she spoke, her words pounded into me: “Jesus, Billy, you’re behaving like a fool.” Daddy raised the revolver to his temple, and for a split second the gun seemed alive, a blackbird flapping.

BILLIE: I swear to sweet Jesus, you’re gonna be sorry, Glory.

BIRD: Then he slipped the weapon into the waistband of his pants and stormed out the front screen door.

GLORY: (Pg 5) Quit that foolish crying, Bird.

BIRD: I cried because my mama had told me not to. I cried because I didn’t know what else to do. (Pg 12) My true name is Avocet. Avocet Abigail Jackson. But because Mama couldn’t find anyone who thought Avocet was a fine name for a child, she called me Bird. Which is okay by me. She named both her children after birds, her logic being that if were named for something with wings, then maybe then maybe we’d be able to fly above the shit in our lives. (Pg 23) And so it went. And every night my parents fought:

BILLIE: (Pg 22) Listen here, I’m doing the best I can, woman. You know that. But I’m sick and tired of trying to please you. Nothing I do is good enough for you – Nothing!

GLORY: Trying like hell! You son-of-a-bitch, when was the last time you tried anything that turned out right! You’re no good, Billy Jackson, you’re no damn good! (Pg 54) When was the last time you acted like a father to your girls instead of like a useless drunk?

BIRD: (Pg 26) Some nights I would put my pillow over my head, trying to block out the sound of their arguing. And I would pray to Jesus. I would say, “Dear sweet Jesus, give me angel wings so I can fly away from here.” (Pg 50) Then I’d wonder if guardian angels really existed. (Pg 54) Daddy inhaled, swung his arm as if it were a bat. Then his breath crashed across his lips as he backhanded Mama smack in the mouth. A thread of bright red blood trickled down her chin. (Pg 67) [Again and again] I saw everything so clearly and wished I hadn’t. Her face was pummeled into ground beef. Her nose was no longer in the middle of her face. Her black-and-blue eyes were swollen shut. Mama might be dead. Summer crashed to pieces all around my feet.

PHOEBE: (whispering) She’ll be okay.”

BIRD: (Pg 50) [Now] Phoebe, [my sister], and I suffered beatings as frequently as some children were showered with hugs.

GLORY: We’re trying to make decent humans out of you.

BIRD: Mama would explain. And I’d wonder if there were children in the world who, at that very moment, were being doted on by fat grandmamas. Or little girls whose hair was being brushed out of their eyes as their mamas whispered, “You’re such a good child.” My mama, she wasn’t capable of whispering such sweet words. (Pg 72-73) I dug my nails into my wrists, and as the sting pushed back my tears, an awful notion struck me: My family, we needed to get the hell out of this roach-infested shack. If we didn’t we’d continue to be dumb-assed crackers who drink till dawn in a sorry attempt to forget about all the things they will never have, never become. But there’s no forgetting when you’re white trash. (Pg 74-75) Come morning, I slowly floated up through layers of dream-time, feeling a rush of wings against my skin. Mama sat at the kitchen table, her eyes wild and red-rimmed from tears.

GLORY: Come here, Bird, I need to talk to you. . . I don’t know how to say this easy, so I’ll just say it hard. Your daddy was found this morning by the police. And, well, he had such a tough time with life, he couldn’t handle it no more, honey. Bird, your daddy, he’s gone to heaven.

BIRD: (Pg 76) There wasn’t a funeral. We didn’t have any money, and the priest wouldn’t agree to a service because Daddy wasn’t a Catholic and he’d killed himself, so they said, and that was a sin in their church. (Pg 73) Smirks, stares, stolen glances remind you at every turn that you’re not worth squat. So the men, raging drunk, bullshit each other into believing that bruised fists and broken noses will act as charms, paving their way to heaven. And we females – girls and women alike – can’t find enough strength in our battered souls to escape. We cast daddies, husbands into near-respectable village idiots in the stories we spin over clotheslines draped with bleach-scented, bloodstained damp sheets. And after all that, we still aren’t decent. We’re still trapped. (Pg 233-234) My daddy . . . In my mind, I saw his suicide face, him gazing upon the black waters and finding no peace. Tears welled – I squatted and covered my eyes. Goddamn it! A voice filled my head: “Don’t you wish you were dead!” No! No! No! I cried. (Pg 242) I screamed. Screamed so loud I must have woke the dead. But nobody came. What do you do when you beg loud and long for help but there ain’t nobody listening? (Pg 234) I didn’t want to be like my daddy. (Pg 238) Night birds appeared suddenly, flashing past like ghosts. (Pg 243-244) A small flock of birds with long, upturned bills, stilt necks, white feathers edged in black. My, oh my, I knew what they were! How odd, I thought, this night I would find my avocets. Creatures with wings could end up most anywhere. (Pg 26) And I pray[ed] to Jesus. “Dear sweet Jesus, give me wings so I can fly away from here.”
```

---

## IC-0093: The Bell Jar

- Title: The Bell Jar
- Author (byline): Sylvia Plath
- Work: Not specified
- Publisher: Perennial
- Publication date as stated: Dec 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ESTHER, JOAN
- Teaser before the introduction: No
- Spoken words (computed): 1359
- Already set (do not supply): none

### Source block (context only)

```text
Author: Sylvia Plath
ISBN: 978-0060930189
Publisher: Perennial
Date (Month/Year): Dec 1999
```

### Introduction (context only: never use it for content warnings)

```text
The Bell Jar by Sylvia Plath tells the story of a gifted young woman's mental breakdown beginning during a summer internship as a junior editor at a magazine in New York City in the early 1950s. The real Plath committed suicide in 1963 and left behind this scathingly sad, honest and perfectly-written book, which remains one of the best-told tales of a woman's descent into insanity. In this selection, Esther is engaged in a conversation with Joan, another mentally disturbed young woman who seems to idolize Esther for her suicide attempt.

The Bell Jar by Sylvia Plath
```

### Performance text (classify this)

```text
ESTHER: (to audience) Joan's room, with its closet and bureau and table and chair and white blanket with the big blue C on it, was a mirror image of my own. It occurred to me that Joan, hearing where I was, had engaged a room at the asylum on pretense, simply as a joke. That would explain why she had told the nurse I was her friend. I had never known Joan, except at a cool distance. (To Joan) How did you get here?

JOAN: I read about you.

ESTHER: What?

JOAN: I read about you, and I ran away.

ESTHER: (evenly) How do you mean?

JOAN: Well, I had a summer job working for the chapter head of some fraternity, like the Masons, you know, but not the Masons, and I felt terrible. I had these bunions, I could hardly walk -- in the last days I had to wear rubber boots to work, instead of shoes, and you can imagine what that did to my morale . . .

ESTHER: (to audience) I thought either Joan must be crazy-wearing rubber boots to work-or she must be trying to see how crazy I was, believing all that. Besides, only old people ever got bunions. I decided to pretend I thought she was crazy, and that I was only humoring her along . . . (to Joan) I always feel lousy without shoes. (smiling) Did your feet hurt much?

JOAN: Terribly. And my boss-he'd just separated from his wife, he couldn't come right out and get a divorce, because that wouldn't go with this fraternal order - my boss kept buzzing me in every other minute, and each time I moved my feet hurt like the devil, but the second I'd sit down at my desk again, buzz went the buzzer, and he'd have something else he wanted to get off his chest. . . .

ESTHER: Why didn't you quit?

JOAN: Oh, I did quit, more or less. I stayed off work on sick leave. I didn't go out. I didn't see anyone. I stowed the telephone in a drawer and never answered it . . . Then my doctor sent me to a psychiatrist at this big hospital. I had an appointment for twelve o'clock, and I was in an awful state. Finally, at half past twelve, the receptionist came out and told me the doctor had gone to lunch. She asked me if I wanted to wait, and I said yes.

ESTHER: Did he come back? (to audience) The story sounded rather involved for Joan to have made it up out of whole cloth, but I led her on, to see what would come of it.

JOAN: Oh yes. I was going to kill myself, mind you. I said, 'If this doctor doesn't do the trick, that's the end.' Well, the receptionist led me down a long hall, and just as we got to the door, she turned to me and said, 'You don't mind if there are a few students with the doctor, do you?' What could I say? 'Oh no,' I said. I walked in and found nine pairs of eyes fixed on me. Nine! Eighteen separate eyes. Now, if that receptionist had told me there were going to be nine people in that room, I'd have walked out on the spot. But there I was, and it was too late to do a thing about it. Well, on this particular day I happened to be wearing a fur coat . . .

ESTHER: In August?

JOAN: Oh, it was one of those cold, wet days, and I thought, my first psychiatrist you know. Anyway, this psychiatrist kept eyeing that fur coat the whole time I talked to him; and I could just see what he thought of my asking to pay the students' cut rate instead of the full fee. I could see the dollar signs in his eyes. Well, I told him I don't know whatall -- about the bunions and the telephone in the drawer and how I wanted to kill myself-and then he asked me to wait outside while he discussed my case with the others, and when he called me back in, you know what he said? . . . He folded his hands together and looked at me and said, 'Miss Gilling, we have decided that you would benefit by group therapy.

ESTHER: Group therapy?

JOAN: That's what he said. Can you imagine me wanting to kill myself, and coming round to chat about it with a whole pack of strangers, and most of them no better than myself . . .

ESTHER: That's crazy! That's not even human.

JOAN: That's just what I said. I went straight home and wrote that doctor a letter. I wrote him one beautiful letter about how a man like that had no business setting himself up to help sick people . . .

ESTHER: Did you get any answer?

JOAN: I don't know. That was the day I read about you.

ESTHER: How do you mean?

JOAN: Oh, about how the police thought you were dead and all. I've got a pile of clippings somewhere.

ESTHER: (To audience) She heaved herself up, and I had a strong horsey whiff that made my nostrils prickle. Joan had been a champion horse-jumper at the annual college gymkhana, and I wondered if she had been sleeping in a stable. Joan rummaged in her open suitcase and came up with a fistful of clippings

JOAN: Here, have a look.

ESTHER: The first clipping showed a big, blown-up picture of a girl with blackshadowed eyes and black lips spread in a grin. I couldn't imagine where such a tarty picture had been taken until I noticed the Bloomingdale earrings and the Bloomingdale necklace glinting out of it with bright, white highlights, like imitation stars. SCHOLARSHIP GIRL MISSING. MOTHER WORRIED. The article under the picture told how this girl had disappeared from her home on August 17th, wearing a green skirt and a white blouse, and had left a note saying she was taking a long walk. When Miss Greenwood had not returned by midnight, it said, her mother called the town police.

The next clipping showed a picture of my mother and brother and me grouped together in our backyard and smiling. I couldn't think who had taken that picture either, until I saw I was wearing dungarees and white sneakers and remembered that was what I wore in my spinach-picking summer, and how Dodo Conway had dropped by and taken some family snaps of the three of us one hot afternoon. Mrs. Greenwood asked that this picture be printed in hopes that it will encourage her daughter to return home. SLEEPING PILLS FEARED MISSING WITH GIRL A dark, midnight picture of about a dozen moon-faced people in a wood. I thought the people at the end of the row looked queer and unusually short until I realized they were not people, but dogs. Bloodhounds used in search for missing girl. Police Sgt. Bill Hindly says: It doesn't look good. GIRL FOUND ALIVE! The last picture showed policemen lifting a long, limp blanket roll with a featureless cabbage head into the back of an ambulance. Then it told how my mother had been down in the cellar, doing the week's laundry, when she heard faint groans coming from a disused hole . . . I laid the clippings on the white spread of the bed.

JOAN: You keep them. You ought to stick them in a scrapbook. (Esther folds the clippings and slips them in her pocket) I read about you. Not how they found you, but every thing up to that, and I put all my money together and took the first plane to New York.

ESTHER: Why New York?

JOAN: Oh, I thought it would be easier to kill myself in New York.

ESTHER: What did you do? (Joan grins sheepishly and stretches out her hands, palm up) (To audience) Like a miniature mountain range, large, reddish weals upheaved across the white flesh of her wrists. (To Joan) How did you do that? (To audience) For the first time it occurred to me Joan and I might have something in common.

JOAN: I shoved my fists through my roommate's window . . . My old college roommate. She was working in New York, and I couldn't think of any place else to stay, and besides, I'd hardly any money left, so I went to stay with her. My parents found me there-she'd written them I was acting funny-and my father flew straight down and brought me back.

ESTHER: But you're all right now.

JOAN: (thoughtfully) I guess so. Aren't you?
```

---

## IC-0094: Bellyfruit

- Title: Bellyfruit
- Author (byline): Maria Bernhard, Susannah Blinkoff, Janet Borrus
- Work: The Best American Short Plays 1997-1998
- Publisher: Applause Books
- Publication date as stated: 2000
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHRISTINA, ARLENE
- Teaser before the introduction: Yes
- Spoken words (computed): 1702
- Already set (do not supply): none

### Source block (context only)

```text
Author: Maria Bernhard, Susannah Blinkoff, Janet Borrus
Book: The Best American Short Plays 1997-1998
ISBN: 1557833664
Publisher: Applause Books
Date(Month/Year): 2000
```

### Introduction (context only: never use it for content warnings)

```text
According to Victor Strausburg of the New Mexico School of Medicine, one million teens in the USA will become pregnant over the next twelve months. Ninety-five percent of those pregnancies will be unintended. About one third will end in abortion; one third will end in spontaneous miscarriage; and one third will continue their pregnancy to term and keep their baby. More than half of these teen mothers will be 17 years old or younger. Why? Some say it’s because we don't educate about birth control in sex education classes, we don't discuss it at home, and we don't give teens good access to it. Some say it’s because abstinence is not a value passed on to our kids at home or in school. Regardless of the reasons, the facts remain the same . . . Children are having children. Bellyfruit by Maria Bernhard, Susannah Blinkoff, Janet Borrus puts a face and a name with this crisis. You’ve already met Christina. This is her story.
```

### Performance text (classify this)

```text
CHRISTINA, female, age 16, Caucasian ARLENE, female, mid-30's, Christina's mother

CHRISTINA: You know how you can only get pregnant like two days out of the month? That's when I took the pill! Before I had my baby, I did some modeling at the mall, but they don't call me no more. I wasn't thinking about having a baby when I was having sex. I was thinking about having sex when I was having sex... like most people, right?

CHRISTINA: I had sex with seven guys last Saturday. Not many girls can say that. See, I decided not to feel bad about who I am and just accept that I'm a slut. It's what I am. You don't always get to choose what you are. I tried to change. It doesn't work. Last weekend I went to a party with my best friend. I was gonna be this whole new person, right? I wasn't gonna just get wasted and go off with some guy. But as soon as her boyfriend showed up she ditched me. Then practically everybody started pairing up, and I just kind of stood there feeling...stupid. Then I saw this whole other group of guys sitting on the wall. And they were all looking at me. They started calling me "sexy girl" and "beautiful." It made me feel good. I took off this sweater I had on over this kind of crop top thing. I downed one of their beers and started making out with one of them. Then, somehow, I was sitting on one of the other guy's laps and... then everything got really wild. The guys took me to a park. I tried to run but I was in the middle of this mass of men. At first, I was scared but then there was nothing I could do. They were all undressing me and undressing themselves, grabbing at me and...I don't really re-member. Anyway, that's it. I did them all. Not many girls can say they did what I did. [SCENE BREAK ]

CHRISTINA: I slept in the bathtub last night. I watched this really scary movie about two sisters and one is really evil and the other one is in a wheelchair. It freaked me out so bad, I had to sleep in the bathroom 'cause it's the only door in the house that has a lock. My mom's been gone four days this time... 'sposed to be just the weekend. She usually calls, unless she's really drunk. I hope she's OK. She's fine. Guess she got lucky. Whatever. I don't care, I just wish she'd left me some money. They turned the gas off on Friday so I'm, like, wearing six sweaters. But it's not a tragedy or anything. We have a microwave. She finally returns to find me in the bathroom . . .

[To CHRISTINA and her mother ARLENE in the bathroom of their apartment.]

ARLENE: Why'd you have to lock the bathroom door? I thought you overdosed or slit your wrists or something.

CHRISTINA: Not yet.

ARLENE: Don't start. God, I need coffee.

CHRISTINA: Good luck. The gas got turned off.

ARLENE: They said I had 'til the end of the month! Shit, I was gonna pay it, I just needed cash this weekend. [Sighs.] I'm a lousy mother, right?

CHRISTINA: [Reciting her usual response.] No, you're not.

ARLENE: C'mon, I'll take us out to breakfast.

CHRISTINA: I have school, Mom.

ARLENE: I haven't seen you all weekend, I want to tell you about Frank. I need advice.

CHRISTINA: Frank? What happened to Gary?

ARLENE: Gary is an [jerk]. Frank's the one.

CHRISTINA: Did you tell him about me?

ARLENE: Frank needs more time to fall in love with me but soon I'll tell him all about you. Then you'll have a father.

CHRISTINA: I don't want a father.

ARLENE: You want the bills paid?

CHRISTINA: I want someone to love me. . . I want a family, not a father.

[Lights crossfade to CHRISTINA in her bathroom.]

CHRISTINA: It's been three months now and I know. I haven't been to the doctor yet, but I don't have to have a doctor tell me what I can feel. My butt's getting bigger and my boobs - Like, storing up fat for some future time, like I'm some kind of Eskimo or something. And I haven't told anyone yet. Sometimes I want to tell like a total stranger on the bus. Or sometimes I just wanna pull up my sweatshirt in front of my mom and her new boyfriend and yell: "Surprise!" No one has any idea. I still go to parties and stuff but I wear really baggy clothes so nobody notices. I don't know which guy it was. But it doesn't really matter. It's not like any of these guys are gonna help me out at all. But, you know, a lot of women are alone when they're having a baby, so I'll be just like them. I don't think I'd want any of those guys around anyway. I mean, they're not fathers, they're just guys. They were just having sex. Like I was. [SCENE BREAK ]

CHRISTINA: At the hospital, everyone kept asking me about the father. They gave me all these forms to fill out and all the real fathers it could be just blurred in my head: the guys on the field, that boy from Spanish class, my friend's brother, the guy at the 7-11...and I just started crying. This nurse came up to me and asked me what was wrong and I told her I didn't know and she said: What? What don't you know? And I said, "I don't know who the father is!" I felt so stupid. Like, yeah, I'm really popular now, right? So she says: You can get the different men to come in for a test ...and I'm, like, picturing the guys at my school. No way am I gonna go up to, like, thirty different guys and say, "Hi! I don't know if this is your kid, but if you could just come down to the hospital for a test..." And then I realized I don't even like any of them and that was too depressing. So I told the nurse that the father moved out of state and I don't know where he is. And she said: Oh, I see, and wrote "Unknown" in about a million places on the page. Sometimes I feel like I made a really big mistake... [SCENE BREAK ]

CHRISTINA: I have a huge scar. It's really gross. They had to cut me open 'cause the baby came five weeks too early. I felt like I was in a magic trick, you know, like I was the girl inside the box with everybody watching while the guy saws me in half. They cut my stomach open! Like I will ever wear a crop top again, right? But then the nurse.. .she puts this little wet person on my chest and I could see these little fingernails and toes, her little ear was right over my heart and then she opened up these blue amazing eyes and looked right at me. She's the most incredible and perfect thing I've ever seen! And she came out of me...which proves I'm not as [messeed] up as I thought, you know?

[Lights up on ARLENE in apartment. CHRISTINA enters, slightly drunk.]

ARLENE: You're forty minutes late, Christina! We agreed that you'd be home by . . .

CHRISTINA: Hi, baby! Hi, sweetie, did you miss me?

ARLENE: Shhh! She finally just fell asleep. [ARLENE gives the baby to CHRISTINA.] What, you can't tell time?

CHRISTINA: The party rocked and no one wanted to leave! I couldn't get a ride

ARLENE: She cried and screamed all night. She drove me crazy.

CHRISTINA: She cried for me? Ohhh, you missed me, little sweetie, didn't you. Well, mommy won't leave you ever again, I promise.

ARLENE: Right. Not 'til there's another rockin' party.

CHRISTINA: I'm just trying to meet someone, okay? Sound familiar?

ARLENE: It's not that easy, trust me. I gave up everything when I had you! Everything!

CHRISTINA: SO I was forty minutes late, so what, mom! Don't shit lightning bolts.

ARLENE: You don't get it, do you? I am not your babysitter! I already DID this, I raised you all by myself for sixteen years!

CHRISTINA: Mom

ARLENE: No, Christina! You got pregnant, not me! This is your mess, not mine! [SCENE BREAK ]

CHRISTINA: I miss school. I never thought I would, but I do. I can't believe my mom let me do whatever I wanted. I'm gonna be strict with my kid. All I do with my baby is watch T.V: We never go out or nothin'. No guys go out with you if you have a kid. I go for every job I hear about, but they all say the same thing. "What if your kid gets sick? We can't depend on you." When she's 16 I'll be 30. That's not too old to go to college. Is it? [SCENE BREAK ]

[Lights up on CHRISTINA with her baby, knocking on an apartment door.]

CHRISTINA: Hi, um, I'm Christina and this is my daughter and, uh.. .we're kind a stuck. John lets us stay here sometimes. I can't stay with my mom 'cause her new boyfriend can't deal with the baby crying, he gets migraines and he's pissed off 'cause I borrowed some money without asking. I was gonna tell him. Anyway, I went to this shelter place in Hollywood but I could only stay two weeks. And then I slept in this van with a guy and his girlfriend and their baby but it was really crowded and then they got lice and...I mean, I'm not, like, homeless. I'm not gonna end up to be one of those people who gets their baby taken away by the county. I'm a normal person! I was popular, okay? But now it's like...we don't even have a place to sleep. Aren't people supposed to like babies? [SCENE BREAK ]

CHRISTINA: I look into my baby's eyes and I see how innocent she is. She doesn't expect the worst from everybody...and I'm gonna keep it that way. I used to think, like, everything is temporary, you know, don't nothin' last... but now that I have my kid it's just like my mama said: People come and go, but children are forever.
```

---

## IC-0095: Between Shades of Gray

- Title: Between Shades of Gray
- Author (byline): Ruta Sepetys
- Work: Not specified
- Publisher: Speak
- Publication date as stated: April 2012
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LINA, JONAS, MAMA, OFFICER, ONA, DOCTOR, GUARD
- Teaser before the introduction: Yes
- Spoken words (computed): 1239
- Already set (do not supply): none

### Source block (context only)

```text
Author: Ruta Sepetys
ISBN: 978-0142420591
Publisher: Speak
Date (Month/Year): April 2012
* NKVD - the Soviet Secret Police
```

### Introduction (context only: never use it for content warnings)

```text
The year was 1941. While Adolf Hitler orchestrated his “Final Solution” against the Jewish population, Joseph Stalin took the opportunity to target “anti-Soviet” elements in the Baltic States where anyone with a prestigious job, regardless of religion, was viewed as a potential threat to Stalin’s power.

Overshadowed by the atrocities of Hitler’s extermination camps, history is eerily quiet regarding Stalin’s Great Purge. More than a million people from Estonia, Latvia and Lithuania were loaded onto cattle cars. The destination: forced labor camps in Siberia.

This is the story of Lina Vilkas, only 15 when Stalin’s Great Purge begins. Can Lina keep her humanity as she navigates . . .

Between Shades of Gray by Ruta Sepetys
```

### Performance text (classify this)

```text
LINA: (Pg 26-27) They were taking Jonas. My beautiful, sweet brother who shooed bugs out of the house instead of stepping on them.

JONAS: Mama! Lina! (he hangs his head and cries)

LINA: Mother grabbed the officer and began speaking in Russian – pure, fluent Russian. The officer jerked Jonas toward him. His body began to vibrate as sobs wracked his shoulders. Mother pulled a bundle of rubles from her pocket. Her hand flew up and ripped the amber pendant from her neck and pressed it into the officer’s hand. He didn’t seem satisfied. Mother pulled a pocket watch from her coat. I knew that watch. It was her fathers’ and had his name engraved on the back. The officer snatched the watch and let go of Jonas. Have you ever wondered what a human life is worth? That morning, my brother’s was worth a pocket watch.

MAMA: (Pg 7) (frantically) Shoes, Jonas, extra socks, a coat! Lina . . . Hurry!

LINA: (Pg 11) The door burst open and three officers entered our house carrying rifles with bayonets. Mother looked in the foyer mirror to put on her hat. The officer slammed her in the shoulder with the butt of his rifle, throwing her face-first into the mirror.

OFFICER: Bourgeois pigs, always wasting time. You won’t need that hat.

MAMA: (flatly without making eye contact) Pardon me.

LINA: Pardon me? These men burst into our home, slam her into the mirror and she asks them to pardon her? Then she reached for it, the long gray coat, and suddenly I understood. She was playing the Soviet officers like a careful hand of cards, not quite sure what might be dealt next. I saw her in my mind, sewing jewelry, papers, silver and other valuables into the coat’s lining.

OFFICER: (Pg 13) Davai! (Hurry!)

LINA: We marched into the intersection of the street toward a truck surrounded by more NKVD* (Pg 14) We were all on the list. I didn’t know what the list was only that we were on it. Apparently so were the other fifteen people sitting inside on their luggage. (Pg 15) I squeezed my eyes shut. The truck stopped in front of the hospital. Waiting. A woman who was also on the list was giving birth to a baby. As soon as the umbilical cord was cut, they would both be thrown into the truck.

ONA: (Pg 20) (Screaming) My baby! Please don’t hurt my baby!

DOCTOR: Please, you cannot take the newborn. It won’t survive! Sir, I beg you. Please!

LINA: The officer turned to the doctor and kicked the heel of his boot into the doctor’s kneecap. They lifted the woman into the truck. The baby was handed up. I held the bundle and instantly felt the warmth of its little body penetrating through my coat. The child let out a soft cry and its tiny fists pummeled the air. Its fight for life had begun. (Pg 21) The child had been alive only minutes but was already considered a criminal by the Soviets. (Pg 23) We arrived at a small train depot in the countryside. A deserted area, surrounded by dark woods. Soviet trucks filled the rail yard, packed with people just like ours. I pictured a rug being lifted and a huge Soviet broom sweeping us under it.

(Pg 29) Wooden train cars lined the platform, stretching as far as the eye could see. They were crudely built and dirty, the kind that would haul livestock. Masses of Lithuanians thronged toward them. White knuckles clutching suitcases. People on their knees yrying bags with twine while officers stepped on the contents. (Pg 35) I counted the people – 46 packed in a cage on wheels. Faces spoke to their future. Courage, anger, fear and confusion. Others had already given up. Which was I? (Pg 41) The back of our train car had Russian writing on it. Thieves and prostitutes. Mothers were in that car. Along with a teacher, a librarian, elderly people, and a newborn baby – thieves and prostitutes. (Pg 49) Two Soviets pulled a priest down the platform. His hands were bound and his cassock was dirty. Why a priest? But then . . . why any of us?

MAMA: (Pg 51) Stalin has a plan. The Kremlin will do anything to see it through. He wants Lithuania for the Soviet Union. I imagine he’s doing the same to Latvia, Estonia and Finland.

LINA: (Pg 55) I hated them, the NKVD and the Soviets. I planted a seed of hatred in my heart. It would grow to be a massive tree whose roots would strangle them all. I looked around the train car. No one spoke. How could we stand up for ourselves if everyone cowered in fear and refused to speak? (Pg 62-63) While I devised a plan, the women in the car showed constant concern for the baby, who could not seem to nurse. We rolled for days, stopping in the middle of nowhere. (Pg 50) A guard approached and handed up a bucket of water and a buckry of slop.

GUARD: (Pg 64) One person! Two buckets! Any dead bodies in there?

LINA: Ona was quiet. Her baby was dead.

MAMA: (Pg 71) Ona, dear. Give me the baby.

ONA: (begging) Don’t give her to them. Please!

MAMA: We will not give her to the guards. I promise. We’ll wrap her in something beautiful.

LINA: (Pg 75-76) We tried for three days to sneak Ona’s baby out. The smell of rotting flesh had become unbearable in the hot car. Ona finally agreed to drop the baby down the bathroom hole.

ONA: (whimpering) She’ll be crushed on the tracks. . .

LINA: Mother moved toward Ona. Before she reached her, Miss Grybas snapped the bundle from Ona and threw it down the hole. (gasp) (Pg 82) Ona was only a few years older than me. (Pg 78) Weeks . . . I lost track of how long we had been traveling. I stopped watching for bodies to be hurled from the cars. Every time the train pulled away, we left a litter of corpses in our wake. Would someone bury them, or would they believe they were really thieves and prostitutes? (Pg 80-81) After six weeks and the third day without food, the train stopped. We heard clanking. The guards opened the door and said we would be getting out. Finally. My entire body trembled at the shock of daylight. The NKVD had bayoneted rifles at the ready.

ONA: (Pg 94) (crying and rocking back and forth unconsolably she chants) No, no, no, no!

LINA: (Pg 101) She could not be calmed. The commander saw Ona standing up, sitting down, and pulling her hair. He stepped up and pulled her from the truck.

ONA: (Pg 94) No, no, no, no! (Screaming and clawing at him as if being drug by her hair)

LINA: (Pg 101) She was no match for his height or strength. He threw her to the ground. His eyes narrowed. His jaw tightened . . . (in horror) He pulled out a pistol and shot Ona in the head. (long beat, then with little emotion -- dazed) (Pg 102) Blood, the color of thick red wine. Leg splayed out in an unnatural angle. One of her feet was missing a shoe. Ona’s body got smaller and smaller as we drove away. She lay dead in the dirt, murdered by the NKVD. Somewhere hundreds of miles away, her daughter decomposed in the grass. (long beat, reflective) (Pg 163-164) My art teacher said if you breathed deeply and imagined something, you could be there. I learned to do that. I clung to my rusted dreams during times of silence. At gun point, I fell into every hope and allowed myself to wish from the deepest part of my heart. (Pg 112) What had happened to Ona? Was she in heaven with her daughter? Or was she floating amongst the trains and masses of Lithuanians, searching for her husband? ****** (Pg 3) They took me in my nightgown. Thinking back, the signs were there – family photos burned in the fireplace. Mother sewing her best silver and jewelry into the lining of her coat. Only later did I realize that Mother and Father intended we escape. We did not escape. We were taken . . . June 14, 1941.
```

---

## IC-0096: Big Butt Girls, Hard-Headed Women

- Title: Big Butt Girls, Hard-Headed Women
- Author (byline): Rhodessa Jones
- Work: Colored Contradictions: An Anthology of Contemporary African American Plays, Pgs 364-376
- Publisher: Plume Drama
- Publication date as stated: Nov 1996
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: GIRL, ARTIST, REGINA BROWN, MAMA PEARL, DORIS
- Teaser before the introduction: Yes
- Spoken words (computed): 1642
- Already set (do not supply): none

### Source block (context only)

```text
Author: Rhodessa Jones
Book: Colored Contradictions: An Anthology of Contemporary African American Plays,
Pgs 364-376
ISBN: 978-0452274976
Publisher: Plume Drama
Date (Month/Year): Nov 1996
```

### Introduction (context only: never use it for content warnings)

```text
At a time when poor black women were represented in the media and in American politics as parasitic “welfare queens,” “crack whores” and prostitutes incapable and undesiring of anything other than a life of crime, Rhodessa Jones was working with incarcerated women at the San Francisco County jail. She learned much about how Regina, Mama Pearl and Doris came to be there and how they did their time. The portraits she creates of these real women demonstrate that there is more to being a criminal than simply being black, and more to humanity than what power and authority allow.

Big Butt Girls, Hard-Headed Women by Rhodessa Jones
```

### Performance text (classify this)

```text
GIRL: (Pg 364-365) (In the voice of the girlchild, reminiscent of a “jump rope rhyme”) Milkshake, milkshake, cream of tartar Tell me the name of her sweethearter

(A la Aretha Franklin’s Respect*)
What you want
Somebody got
What you need
You know I got it

(She dances suggestively-hands on hips) I got it. I got it. I got it. Git it, Girl! Gon girl!

(She freezes into a position of fatherly authority and speaks) Git in the house! Git yo' big butt in the house!!! (The girl-child whines) But I wasn't doin' nothin' . . . nothin', nothin'. I ain't nothin'.

GIRL: (Pg 365-366) (Assuming the attitude and posture of an adolescent girl, trying to be a grown woman) Hey, Tony! Hey, Jerry! (Over her shoulder, conspiratorially) Girl, that looks like Tony and Jerry. Let's go to the sto'. (She circles downstage, ending with her back to the audience. She mimes necking, heavy breathing, childish groping) I love you. Nobody does it like you do. Just kiss me. (In a masculine voice) Is it good? Tell me that it's good.

(Scenario evolves from passion to labor to childbirth ending with the girl-child facing the audience holding a baby. She freezes into a position of motherly authority) Git in the house. Git yo' big butt in the house. Don't be so hard-headed. Haven't you done enough?! (She whines) But I wasn't doin' nothin' . . . nothin', nothin'. I ain't nothin'.

(She moves into a frenzied dance of self defense . . . Warding off blows while holding the baby) You better stop, Jerry. I'ma tell my daddy. Stop!

(She mimes being punched in the stomach, knocked to the ground and sexually assaulted. She
rolls to her side and assumes the voice of authority)
Git in the house. Git yo' big butt in the house. A hard head makes a soft a**
(Rising from the floor. It is painful) But I wasn't doin' nothin' . . .

(Sound of a car horn. She beckons in a pleading voice) Hey, you! You wanna kiss me? Yeah, kiss me, kiss me.

(Sirens and suddenly she's handcuffed and struggling, caught) Take yo' hands off me. I wasn't doin' nothin'. Regina, call my mother. Tell her they takin' me to jail, girl. Take yo' hands offa me! Doris, tell my grandmama they takin' me to jail, girl, and I wasn't doin' nothin'. ******Scene Change******

ARTIST: (Pg 366-367) (Prison) Good morning. I am Rhodessa Jones from the California Arts Council. I will be teaching aerobics here every Wednesday morning. My pass is newly issued. You got to run a check? Look, Sergeant, why would I want to break into jail? Whoa -- It's not that I'm trying to be a wiseass. I just have no great need to sneak into jail first thing on a Wednesday morning! Oh, this? This is my beat box. These are my tapes. Here. I'd love to discuss it with you, but I've got a class to teach. I beg your pardon? Read my lips: I have far better thangs to do with my time than sneaking into jail first thing in the morning. Could I have my pass please?! (Scene change. She is on the aerobics platform, overly enthusiastic)

Good morning, Ladies. We're going to begin with some windmills. Now everybody smile, and one. . . two. . . C'mon Latoya, you too. All right good. . . And now for all you big butt girls, that's right, we gon' do some booty building this morning! What's the use of having a big ol' butt that you can't use. You know, to express yo' self. You know, a butt that com-mands attention. . . One that stands alone. Let's begin by tightening up with some lunges, and press one. . . two. . . (She freezes. Scene change. She steps foward addressing the audience)

In jail. A black, woman artist, working in jail. I look out at all those faces. There's my mother's face, my sister's face and my daughter's face. And I'm wondering how in the hell did they get here in the first place. And I realize that it is but for a flip of fate that it could be me in here and she out there.

(Scene change - she moves as though she's catching bodies falling from the air. It is sporadic.
She calls out simultaneously)
Vanessa! Jeanita! Paula! Beverly! (stops and spouts statistics)
85% of all women incarcerated in U.S. penal institutions are women of color.
Donna! Naomi! Paulette! Jessica!

50% are African American women. It is a revolving door. And how can I, as one woman artist, make a difference, provide a supportive environment in the face of women who know that it's so goddamn hard to live anyway. Women with no jobs, who've lost their chil-dren. How do we counter life-threatening situations such as alcoholism, drug addictions, sexual abuse? How do we discuss and explore the reality of AIDS, coming to grips with the fact that screams: "Women die far faster from it"?

(Scene change. She returns to the aerobics platform) Today we're going to work with the mask -- in theatre your face is the mask. Let's begin by stretching the face. Big face. Little face. C'mon -- it is an anti-aging device. Now, use the tongue. Stretch to the side. . . To the top. . .To the other side. . . All you working girls, pay attention.

(softly to audience) So many faces. . . So many masks. . . So many stories. . . ******Scene Change******

REGINA BROWN: (Pg 368) (an African-American woman of about thirty. Strong and aggressive)

I learned early, a man or a woman ain't nothin' but a plaything. I tell them all, "It's like the lotto, Baby. You got to be in it to win it." Later for all that "Ooh, Baby" this and "Ooh, Baby" that. I believe in action, so you best get on with the A team. Like Tyrone, he's in love with me, always has been, and I can understand that. But I told him, "I was born a full-grown woman, and it ain't about 'my woman this' and 'my woman that.' I'm my own woman." But, like a lot of men, he don't want to listen. Wanted to control me . . . thought he was my daddy. My daddy is dead, Baby. And my mama raised me to be strong and on my own. He got all mad, 'cause he wasn't ready for the real deal. Brought some other girl home! And now who's crying? Tyrone. Because I'm carrying another man's baby. And that man ain't even important. The reality check has to do with me and, my baby. I am a prostitute, straight up. I decided a long time ago, wasn't no man gonna tell me what to do. I'm a full-grown woman, straight up and down. Or my name ain't Regina Brown. WORD! ******Scene Change******

MAMA PEARL: (Pg 369-370) (an African American woman about seventy. She speaks with a velvet voice) My hand to God, some of them so young . . . I've been in and out of the joint since 1965 and I ain't never seen it as bad as it is now. The young women coming and going in this day and time don't have no sense of theyself. I got three daughters. My older daughter was born deaf and dumb. She's the reason I went to jail in the first place. (She pauses and looks around before continuing in a more secretive tone) You see, I embezzled some money from the company that I was working at so my daughter could get special training so that she could take care of herself, despite her handicap.

These girls need somebody to help them understand that you ain't got to be in and out of jail to feel important. They got to find a reason to let go of that crack and cut loose these men that pimp them for drugs, money, cars, even a leather coat. Look at them. Most of them not even 25 yet and have the nerve to be pregnant up in here. Treat these babies the way they do. How? They will sell them, lease them to the dope man for some rock. They're flesh and blood, honey. Then the dope man, he gon get busted and then the baby is lost to child protective services. And these b****es want to cry about they babies. I got three daughters. You know what I tell 'em? "Take that whining and complaining someplace else.” ******Scene Change******

DORIS: (Pg 372-373) (an African American woman about 19. The classic girlchild with a child of her own. She sucks her thumb as she speaks) Hey, Brittany. It’s Mommy. Stay with Grandma and be a good girl. (beat) Mama, what did Mr. Sullivan say about when I can get out of here? I wasn’t doin’ nothin’. Resisting arrest?! I wasn’t! I was with Big Willie when the police stopped us, ran a check on him, came back to the car and asked for some ID. I asked why. They waid I was in the company of a known felon. I said, felon or not, this is my baby’s daddy. Then the white police say, “Then your baby must be a felon, too.” I say, “Your mama is a felon.” Then he try and snatch me out of the car. Big Willie was all over him. So the next thing we know, we down here in jail. I’m gonna lose my job and I wasn’t doin’ nothing.’ Mama, call Mrs. Ryan and tell her I got to reschedule my GED. Remind Aunt Ossie to call Social Services. Tell them that she will keep the kids while you in the hospital, ‘cause these people ain’t seen no criminal activity until some of them try to take my babies and put them in a home. Give little Willie a kiss for Mommy. I love you. Bye, Mama. Bye.

ARTIST: (Pg 374-375) (to audience) Who are these women? And what are they to you? (points to the audience) They wear my mother's face, my sister, my daughter. And now, if I'm to believe statistics, my granddaughter? You know, working in the jails, I don't delude myself and pretend that the time I spend with these people is gonna make a whole lot of difference. Their problems are too great, too immense. Benign neglect. Alienation. Isolation. Blind rage. Living in some township just outside of Amerika.

(with hands joined as in prayer) But I was raised in a family by a mother and a father who taught me that when you're called to something too great, too immense, you can always take it to God. Now the African in my American teaches me to take it to the Ancestors. (The Artist begins incantation) Build spirit catchers. This is a spirit catcher for one Regina Brown, age 27. Regina Brown, murdered in the winter of 1989, after her third release from jail. Regina Brown, mother of two children, a boy and a girl, left to make it in this hard-luck place called the world. (beat)

******Scene Change******

GIRL: (Pg 364-365) (In the voice of the girlchild, reminiscent of a “jump rope rhyme”) Milkshake, milkshake, cream of tartar Tell me the name of her sweethearter

(A la Aretha Franklin’s Respect*)
What you want
Somebody got
What you need
You know I got it

(She freezes into a position of fatherly authority and speaks) Git in the house! Git yo' big butt in the house!!! (The girl-child whines) But I wasn't doin' nothin' . . . nothin', nothin'. I ain't nothin'.

ARTIST: (Pg 376) (to audience) How many people have ever been mugged? Apartment broken into? Had your credit cards misused and abused? Been raped? Know somebody, who knows somebody, who knows somebody . . . My point is, we're all involved here. This ain't no time to be locking doors 'cause you see "them" comin'. "They" could be "us" and you may wake up and find that you've locked yourself in and they're sitting at your breakfast table . . . the struggle continues for all of us.

GIRL: (Pg 365) (She freezes into a position of fatherly authority and speaks) Git in the house! Git yo' big butt in the house!!!
```

---

## IC-0097: Bitch Boxer

- Title: Bitch Boxer
- Author (byline): Charlotte Josephine
- Work: Not specified
- Publisher: Oberon Books
- Publication date as stated: August 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHLOE
- Teaser before the introduction: Yes
- Spoken words (computed): 1370
- Already set (do not supply): none

### Source block (context only)

```text
Author: Charlotte Josephine
ISBN: 978-1849434775
Publisher: Oberon Books
Date (Month/Year): August 2013
```

### Introduction (context only: never use it for content warnings)

```text
Professor Neal Roese of Northwestern University found that in his 2012 study, this biggest regret of all, the regret that derives from the loss of loved one, is the most crippling. However, if we accept the lessons from our regrets, we become motivated to improve ourselves to ultimately meet our goals. Because in the end, we decide whether our regret debilitates us, or propels us.

Bitch Boxer by Charlotte Josephine
```

### Performance text (classify this)

```text
(Chloe walks on stage carrying a jump rope. She has one hour until her fight; the qualifier for the Olympics 2012. She stands center stage and is still for a moment taking in her audience.

She begins skipping and the sounds slowly fade until she is alone. She is professional and focused, skipping center stage facing the audience. The skipping builds in speed and intensity becoming very fast and furious until it suddenly stops and she drops the rope to the floor. She stands still, breathing hard until she has caught her breath and can speak. If her hood to her hoodie hasn’t already fallen down she pulls it back off her face.)

CHLOE: I’d woken up well late. Knew it was late before I looked at my phone. Ten, twenty-seven. Blind panic as I jump outta bed and run round the house trying to tidy up/make breakfast and get dressed at the same time. Multi-tasking to the max. I jump out the front door to stick the rubbish in the bins. I actually thought to myself wouldn’t it be funny if, when I heard the door shut. Click.

CHLOE: Ah, no way. You gotta be joking. But no. I’m officially locked out. And it’s half ten in the morning/ I’ve got to be at the gym in an hour and my dad will kill me if I’m late.

I quickly hatch a plan. I reckon I can climb onto the outhouse thing we got at the back of our house ‘n’ try my bedroom window which is always open. But I gotta ask next door if I can hop their fence. I knock next door, but there ain’t no answer. By now I’m panicking. Three doors down and some woman opens the door. She finds it funny, leads me across her garden and gives [me] a leg up. “Good Luck!” “Cheers love.” Fence number one done.

The next one is high, it makes the most sense to balance on a little boy’s bike and climb up the fence onto the shed next door. This I do, no problem, my upper-body strength is in top condition. Dropping down off the shed roof I land on the concrete when I hear that very/ distinct/ pad/ of feet. I turn slowly. It’s a pit-bull. It rubs it’s hairy head on my bare leg. Somehow I don’t get bit. I back away. Never taking my eyes of the dog.

(Breath out and launch into next section.) Up and over the fence, this one is rotten, a real stunner, the green mossy wood snaps under me cutting my stomach and scratching my legs. But I’m here.

(Smile.) I made it. I shimmy up the drainpipe. Surprising myself with a new-found-talent. I scramble up the roof, and I make it to the window. I see my keys on my bedroom floor next to my handbag. Next to me on the roof is a whole load of metal poles/ from when Dad was decorating. I have a moment of genius. Involving some keys, a metal pole, and a handbag. Results! Keys in my mouth/ I wiggle down the drainpipe. I am very proud of myself. I feel liberated/ like a super hero. I get in and check the time, I did all that in a half an hour! Ladies and Gentleman, Gold medal Olympian Chloe Jackson! Oh yes, I am the best/ I am the champion of cat burglars! The phone rings, “Yes mate! You will never guess what has just happened to me/ seriously/ I just. What?” And then he tells me. Dad’s dead. Just like that. Two words. (Pause)

I hate funerals. Nah really/ I don’t get it. All that money spent on flowers. My dad never bought no one flowers, so why now all of a sudden was he getting hundreds of ‘em? Everyone turned up, all the kids from the gym, their parents, their parent’s parents. If you wanna spend your money spend it down the gym/ that’s what he’d ave wanted. Not on flowers! And everyone kept hugging me all the time, crying on me, telling me what a terrible waste it was. Yeah you’re right/ I wanted to say, waste of money on all [these flowers]. And I could tell they were watchin’ me, all sly like, out of the corner of their eyes. Waiting for me to crumble.

(Pause) When you’ve been a fighter all your life it’s hard…When Dad died I just had to get on with things/ No amount of crying is gonna bring him back so I didn’t let ‘em fall.

Ma left us when I was eleven. Buggered off with some bloke she’d met in Tesco. My dad was gutted. Like, she taken his heart [and] stamped on it.

(Beat) Came home from school and my dad was sat on the sofa/ crying. (beat) He stayed like that for two weeks/ that’s how much he loved her. [Me?] I smashed the house up. (Beat)

[But] dad knew what to do. Took us down the gym. Stopped me smashing things up round the house and started me training. Taught me to control my anger. Focus it in to Power, strength and speed. Just me and my dad fighting the world together/and I loved it. And low and behold, natural talent.

I’d slip my hand in Dad’s whilst we walk and he’d look down at me and smile. I grew up a bit/ I still held his hand. Liked the feel of it. Got to that age where I didn’t want to hold Dad’s hand anymore, wasn’t cool. I could tell that he was hurt by it, but he never said nuffink. (Beat.)

I was ‘bout eighteen year old. Sweating away working the bags, He approaches, “Come on then kid, show me what you got.” Two blocks/ two straights/ two body shots. “Good.” He says. “You’re in Clo, women are gonna fight in the Olympics 2012.” And whooping with delight we ran round the gym laughing/ And without saying a word, it was all agreed. I’m gonna fight at the Olympics. We made battle plans like it was Waterloo. Stuck charts up on the wall, every competition one step closer to my new dream. A chance to prove to the whole world I’m worth sumionk, to prove ‘em all wrong. Women can’t box? You watch. (Beat.)

Months of training, and this is it. The two of us the same. Both bringing our A- Game to this one shot we both got at the title. I’m quickly learning her habits. The tiny pop-up she does with her shoulder before she throws a right, the shift in weight to duck and dive that leaves her open. I widen my eyes and blink hard, sweat is stinging but I keep them on her.

We wait for the bell [and break].

She’s in her corner listening to her coach. Her face, eager for some words of wisdom. He demonstrates what he wants her to do. She smiles and nods, he pats the side of her face and smiles back, placing his forehead onto hers for a moment. It’s suddenly clear, that he’s her dad. (Break, big push)

I wish I’d never been embarrassed. I wish I’d been proud of holding Dad’s hand ‘cause yeah I miss it now. And I regret it now. I wish I’d just held my dad’s hand forever.

(Chloe caught in the ropes)
What do I do? Dad!
(Chloe still caught on the ropes) “Keep your head down Chloe and look for an
opening.”

(Chloe finds a way out; one series of hard jabs that seems to take all of her energy.)

And I suddenly realize I - could – win - this. (She knocks her opponent out. She celebrates, her hand in the air. As the noise of the crowd dies down her smile fades slightly. She is alone and winning is suddenly bittersweet.)

Apparently he did watch. Snuck in the back. Wouldn’t have missed it for the world. (Beat) . . . Funny thing. You get a knock in life, and it winds you for a moment/ you can’t breathe, but you pick yourself back up and you get your game face on. (Beat.)

When people ask me what my dad was like I don’t really know what to say, do you know what I mean? I mean what was your dad like? Oh yeah? Good for you. My dad was just my dad you know, nothing special. I mean yeah, he was special to me/ but then I’m bound to say that, ain’t I? (Beat)

[My dad always said]: Chloe: It ain’t gonna be easy. “You’ve got to fight for the things you love.”
```

---

## IC-0098: The Block Party

- Title: The Block Party
- Author (byline): Joseph Lizardi
- Work: Voices of Color: Scenes and Monologues from the Black American Theatre, pg 114)
- Publisher: Hal Leonard Corporation
- Publication date as stated: 1994
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: LENA
- Teaser before the introduction: Yes
- Spoken words (computed): 691
- Already set (do not supply): none

### Source block (context only)

```text
Author: Joseph Lizardi
Book: Voices of Color: Scenes and Monologues from the Black American Theatre, pg 114)
ISBN: 978-1557831743
Publisher: Hal Leonard Corporation
Date (Month/Year): 1994
```

### Introduction (context only: never use it for content warnings)

```text
Prostitution is the oldest profession in the world. According to US Health Department (March 2016), the average female prostitute enters the profession when she is only 14 years of age. And although it is extremely clear that these young women want out -- 92 percent of them say they can’t escape due to a lack of money or food. In this selection, Lena discovers that leaving the profession is not as easy as she had hoped. The Block Party by John Lizardi
```

### Performance text (classify this)

```text
Lena, known as a pretty neighborhood prostitute, has just returned from a job interview, angry and frustrated.

LENA: Been a long day. Long, hard day. Went for a job, you know. A decent job. Secretary. Well, a receptionist. Saw it advertised in El Diario. Didn’t get it. He said I ain’t got the right kind of voice. Whatever that means. Really wanted that job, you know. I practiced every day. “Good morning, Damon Enterprises, Incorporated.” That was the name of the company. “Good morning, Damon Enterprises, Incorporated.” Everybody ‘round here said I sounded great. Perfect, you know. A whole week practicing. But at the interview, he said I looked good but sounded terrible. Wanted to spit on his face. But you know what I did? Begged him to try me somewhere else. So he asked if I could type, so I lied. So he put me in front of this typewriter – and I tried to type. Everybody laughed at me. I was a big joke.

LENA: I know everybody ‘round here laugh when I say I wanna get out of all this, but I do. I really do. I don’t enjoy what it do. Never did. I hate it. Nothing to be proud, you know. So degrading, you know. I really hate those creep(s) when they come here looking for me. A few bucks gives ’em the right to own every inch of you. So you just lay there. Let ‘em work you over. Anything they want. Always kept saying “Next creep’s gonna be my last one.” ‘Cause, you know, always had this feeling I could go out there anytime, get a decent job. So today I tried and what happened? [They] tell me I ain’t got the right kind of voice.

Wanna know something? I won a beauty contest in high school. I was the prettiest girl in the whole school. For real. And you know what else? I was in love once. Really in love. When I was sixteen. Even made plans to get married. A young boy. My age. Handsome as anything. Real sensitive. Used to play the piano real nice. And he used to write me poems. Many nights, we used to go to his house, and he’d play the piano and recite the poems. Just for me. We loved each other a lot.

But then they killed him. The big, bad macho freaks in the town. They hated him ‘cause I loved him and not ‘em. They used to pick on him, torture him. One night they made him so ashamed – he didn’t know how to swim – but he jumped in this lake, let the filthy waters take the life outta him. They killed him ‘cause I loved him.

One night I was praying by his grave, and they came. They hurt me bad. After that, they followed me everywhere I went. Making demands. And I always had to give in to ‘em, keep ‘em from hurting me. You can’t run away. They’re everywhere, you know. Waiting to hurt you. But they can never take care of Lena! Oh, I know they think they can. I love when they come here looking for Lena. I love showing ‘em they ain’t [nothin’]. They try. They pay big bucks to try. They wanna see pleasure on my face, but all they get’s one big laugh. That kills ‘em. They hate that, you know. When you make fun of all that macho they come wrapped in. They come in to hurt Lena, but they can’t They just make me laugh.

That’s why I wanted to get that job. To come back here and yell out for all of ‘em to hear. LENA AIN’T FOR SALE NO MORE! LENA’S FREE AGAIN! AND SHE’S GONNA STAY FREE THE REST OF HER LIFE! LISTEN TO ME, YOU CREEPS! LENA’S FREE AGAIN.

Wanted, you know, hear a new beat, a different parade. Nobody’s cheap toy no more. Wanted to tell ‘em all, hands off no matter how much. But, they won again - (yelling into the night) Yeah! Bring the studs in! Let ‘em parade for Lena! Come on! Lena’s waiting! Bring on the parade so Lena can die laughing!

(She laughs hysterically, then collapses on the stoop, shaking and crying)
```

---

## IC-0099: Blue

- Title: Blue
- Author (byline): Michel Magee
- Work: Monologues for Women by Women, Pgs 68-71
- Publisher: Heinemann Drama
- Publication date as stated: June 1994
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BECKY
- Teaser before the introduction: Yes
- Spoken words (computed): 991
- Already set (do not supply): none

### Source block (context only)

```text
Author: Michel Magee
Book: Monologues for Women by Women, Pgs 68-71
ISBN: 978-0435086305
Publisher: Heinemann Drama
Date (Month/Year): June 1994
```

### Introduction (context only: never use it for content warnings)

```text
Most new mothers anticipate the birth of their child will be one of the best days of their lives. Unfortunately, this isn’t always the case. We live in a 1st world country where nearly *1 in 10 babies still takes their first breath too soon. And behind every tiny incubator lies a world of hope, fear, and quiet resilience -- a mother’s whispered prayers competing with the steady hum of hospital machines. (sing 1st line(s) from **You are My Sunshine)

This selection gives voice to the journey of these women: the sleepless nights, the fragile beginnings, and the unshakable love that binds a mother to her child even when that tiny being doesn’t survive.

Blue by Michel Magee
```

### Performance text (classify this)

```text
(Becky is tidying the child’s toys. She hums “You Are my Sunshine” while she works. She picks up a blue ball and hugs it to herself. She closes her eyes for a moment and smiles)

BECKY: (Pg 68-71) (in a straightforward manner)Right off I named her Blue seein’ as she was born on the first night of the Blue Moon ‘n all and bein’ so little – shy a’ three pounds, downright puny – cause a’ comin’ almost three months early ‘n I didn’t want her to go off havin’ no name when they come for her by ambulance for the ride up to the hospital in Jeff City, right after Mama Linny and me baptized her and held hands and recited the Lord’s Prayer with Nurse Carter aleadin’, who is, I’ll have you know, a direct descendant of Mother Maybelle herself. Doc Rhoads joined in for the “Amen!” (pause) Then . . . Blue was gone.

(walks over to the porch steps, settles herself, and begins to snap string beans) When I recollect that night, I can still hear the siren wailin’ down the highway with my baby, long past the distance an ear can take in sound for sure. Mama Linny, who is, for your information, my aunt what raised me up when my own good mama died birthin’ me, says that kind of distance ain’t measured in miles ‘cause the heart don’t know nothin’ ‘bout miles.

(pauses, snapping the string beans, as though considering her next comment, perhaps for the first time) Hearts don’t know nothin’ ‘bout speed either, if y’all’s to ask me. It all a’ got to goin’ so fast. But when I play it over in my heart, that night moves like one a’ them slowed down commercials for face soap or ice tea. (pause) However, the truth be known here, Blue started a makin’ her UN-hesitatin’ way into this world less’n two hours after I had ice cream with her daddy at the Tastee Top, just off the four-lane over by Bender’s Dry Goods, where, by the way, I’d already started puttin’ her layette away on lay away, in yella ‘n white mostely, seein’ as I didn’t know if she was gonna turn out a boy or a girl. (pause) Ray – that’s Blue’s daddy – dropped me off to home early. We was in the very middle of another set-to over getting’ married, but the ice cream – or maybe it was the marshmalla butter-nutter toppin’ – had me feelin’ outta favor with my innards, so I let go a’ my haranguin’ and then sure ‘nough, I started in with cramps ‘ n all and Mama Linny said she didn’t feel it was a plain ol’ bellyache from too much indulgence and we’d est call Doc Rhoads. And the rest y’all know.

(resumes snapping beans, shifting her position occasionally) Naturally right off, I called the hospital long distance up in Jeff City to inquire how Blue was getting’ on. The nurse said fine, and I said, well, if she’s fine, then why’s she there? (Forcefully, in an I’m nobody’s fool manner) I didn’t much care for the sassy answer she give back, so I packed my bag and never mind that I was practically bleedin’ to death. I called Ray right now and told him he was a daddy – ready or not – and that he’d better do right by me and Blue and drive me up to where they was keepin’ her and I wasn’t takin’ no for no answer, ‘n that was that.

(snapping the bean she is holding with ferocity) Well! Let me tell y’all . . . it’s a good thing that child had her mama at hand, ‘cause y’all never seen nothin’ like it. When I got there they had tubes stickin’ outta her pitiful little body and an IV needle in her head! (without a hint of condescension) IV is for intravenous, I’ll have you know. (tenderly) Poor sweet Blue. Her little red baby arms weren’t no bigger ‘n my thumb. Veins too small. Thin as a hayer a nurse explained to me, so that’s why they done it to her head where the veins is bigger.

(turns to bring the laundry basket closer. Facing the audience, she drifts forward, absently touching the clothes still hanging on the line as she moves) ‘Bout mid-point in our ordeal, I also had me a serious talk with Blue. Not the out loud kind . . . the kind you have in your head ‘n the folks you’re close with pick up on. Now y’all take for instance my ol’ Uncle Sonny. He’s got Alzheimer’s ‘n things mixed up but good. (pause) He’ll say: “The WALLS is on fire! . . . and who’r you?” (with patience and sincerity) And I’ll say the walls ain’t on fire, ol’ honey . . . ‘n I’m Becky, same as you been seein’ ever’ day a’ my life. (pause) Holdin’ a conversation with Uncle Sonny can wear a body thin. (pause) But the point I was makin’ was there’s time we’ll be a’settin’ quiet like . . . and I’ll be spinnin’ in my own mind ‘bout tryin’ one a’ them new hybrid okras and Uncle Sonny’ll come back from his private wild blue younder and say, “Yessum, okra’d be right fine” . . . Like he was plugged into my head.

I plugged into Blue’s head that very same way . . . and I got a sad, floatin’ feelin’ like Blue didn’t know where she was s’posed to be. Had things gone accordin’ to plan, she’d a’ been safe and sound right inside me. But things didn’t go accordin’ to plan – and here was my child, little as she was, weighin’ this mighty decision ‘tween choosin’ Earth or what surely would be Heaven. So I said . . .

(The break with the present occurs here, as she drifts center stage. The lighting dims until Becky is spotlit on a darkened stage. Her hands are held to indicate they are resting on either side of an incubator. She begins this passage as though speaking through her heart to Blue – slowly, and with great tenderness)

BECKY: Listen here, Little Lady . . . this here is your Mama a’talkin’ . . . You got to get better . . . and bigger. There’s a fine land outside these walls, Blue . . . and a lake so wide you’ll think it’ll never end . . . And at night . . . there’s stars . . . ‘bout a forever’s worth . . . One of ‘em shinin’ just for you. It’s home . . . (pause) I know your early comin’ was a surprise to you ‘n me both, but there’s such a thing as nice surprises. Just wait ‘til you see all them pretty things I got put on layaway for you . . . (long pause) Blue, honey . . . I need to hold you . . . and I can’t if you gonna stay hangin’ out on that ventilator, hole-up in your little Plexiglas box. Holdin’s real good, Blue. ‘Member that time . . . couple days back . . . I got to hold you seven . . . whole . . . minutes. (smiling, with tears about to spill) They was the best seven minutes a’ my life, Blue.

(in pantomime, Becky opens an imaginary incubator and lifts out her baby. She cradles Blue in her arms. Her voice is barely above a whisper as she begins to croon) You are my sunshine . . . my only sunshine . . . you make me happy . . . when skies are gray . . . You’ll never know dear . . . How much I love you . . . (her voice breaks. Her expression is one of anguish as she looks up as though both pleading and praying) Please . . . oh, please, don’t take my sunshine away. . .
```

---

## IC-0100: The Blue Dress

- Title: The Blue Dress
- Author (byline): Reginald Gibbons
- Work: Slow Trains Overhead: Chicago Poems and Stories, Pg 78-86
- Publisher: University of Chicago Press
- Publication date as stated: May 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ESTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1795
- Already set (do not supply): none

### Source block (context only)

```text
Author: Reginald Gibbons
Book: Slow Trains Overhead: Chicago Poems and
Stories, Pg 78-86
ISBN: 978-0226290584
Publisher: University of Chicago Press
Date (Month/Year): May 2010
```

### Introduction (context only: never use it for content warnings)

```text
According to the National Coalition Against Domestic Violence, an estimated 1.3 million American women are victims of physical assault by a husband or boyfriend each year. The majority of these women continue a relationship with their abuser. But why? Why do battered women stay? The answer given in the 1920s was that battered women were of low intelligence or mentally retarded. In the '40s it was determined that women did not leave because they were masochistic. By the '70s the experts claimed that a woman stayed in an abusive situation because she was isolated from friends and neighbors, had few economic resources, and was terrorized into a state of "learned helplessness" by repeated abuse.

But you see, the answer is not the problem . . . the problem is the question itself. "Why doesn't she just leave?" When we ask that question first, we lose sight of the criminal and the crime and begin to place blame on the victim.

The Blue Dress by Reginald Gibbons.
```

### Performance text (classify this)

```text
ESTHER: [I remember the night] . . . and locked me in there, shouted (Pg 84- 85) you tore my new blue dress through the door if I ever that you couldn't tell from silk tried to leave you, you would right off my back, left me cut me so bad, no one naked in a corner with my hands would want me, while I cried up and you yelling at me into a torn rag of my dress, I spent too much of your money, all ruined and lost and wasted. said I wouldn't

That was for you, that dress, leave you alone,

to make you happy, make made me get in the closet

you want to be with me.

ESTHER: (Pg 78 – 86) You tore it off my back.

But I'm not good
at telling a story -- you'd shut
me up by saying that --
so I guess I can't tell this one,
that had to do with the way
I once used to feel
when someone like you
who had done a rough kind
of work -- work that can kill you
if you're not careful -- talked
to me like my listening
was important to him.

And listened
to me, too, made me feel
I could be the gentleness
he needed after bad
times -- someone who'd grown
up hard and alone, like you,
or gotten through the war
alive. . . But I don't feel
the same about you any-
more, or nearly anyone,
any man, I've known.
I thought when I met you
and it was exciting to me

to be with you, it was

more life I was getting --

and it was less.

But you said I was special,

I was the best of all

the girls -- the women -- you'd had,

the sexiest, I turned you on

the most. That's what I'd

remember when I'd want

to leave you,

when you'd been

after me again, like always

drunk, hunting me or saying

you'd kill me. I'd try remembering

that nobody else ever told me

I was special or beautiful,

and I thought it was loving

me that made you say it --

I know I'm not pretty

the way some women are,

the way some were that you

would look at twice and make

me forget what you'd done

and want you for myself again.

But it was just being

scared that kept me from leaving,

you saw to that many times.

And I did used to love you,
I did love your kisses,
love that touch you had for me,
holding my face in your hands,
squeezing my shoulders for me,
the way you'd rub my tired legs
and how you'd put your hands
on *me*, that was so careful,
I thought, not to hurt.
And my gripping you as hard
to me as I could,
and you'd say I was the best of all
of them, the best and the best
till the waves of it hit --
I'd float for a long
second or two and then it
slams through, so sweet.

But you'd hit me. Just sitting
together in the apartment and you'd
jump up and hit me yelling
"Don't do that!" and I don't
even know what it is.
You used your belt on me,
you threw me down the stairs
more than once and locked
me out alone for hours
and I never knew anyone

in the building who I could

go to, I'd just stay down

near the front door inside,

people would come in and go out

and hold the door for me

but I'd say no, I was

waiting

for someone. . .

Till you came down to look.

When you made up to me

I was so happy to have

you back -- back to yourself --

and we'd go out dancing,

you'd know everybody there

and those friends of yours would always

pretend that nothing's wrong.

I felt grateful to them

for treating me so friendly,

so polite, so respectful. Nice.

And they could laugh with me,

in a way you couldn't, or wouldn't.

The preacher says to talk.

So I do and he listens

and doesn't say very much.

He still thinks that all

the bad came from you, that
everything bad that was done,
you did -- which I'm not going
to tell him any different.
All he knows about that
night is you chased me
downstairs and into the street
at 3 a.m. with me
in my nightgown in the cold and no shoes
and you with the sharp kitchen
knife in your hand, yelling
you were going to cut me.

You never even knew how
afraid I was to go
to sleep and afraid to wait up
for you, too, but what would
you have cared, in those moods –
I went crazy wondering
what you'd do when you came in,
turning like a mean dog
and trying to get me when you
could barely stand up and had
to hold onto the furniture
to walk across the room.

I don't know how you were able all of a sudden to move so fast that night,

the state you were in, and the knife

in your hand. Then when you stopped

in the middle of the dead

street and said it was over

and turned around and started

back, I don't know why

I followed you home, either.

I watched you real carefully

when you got into bed

with your clothes on and you put

the knife under your pillow

and said to me that if I

wanted to kill you while you

were sleeping, there it was.

I waited one more hour

watching the clock go slow,

afraid you'd wake up

sick out of your alcohol sleep

and with one of your nightmares.

Then I had to reach under

your pillow to find the knife

and I cut my finger on it --

I almost cried out

but I realized that what I was

was so mad at you that

all of a sudden I wanted

to beat you hard as I could
with my fists and scream
and it still makes me crazy and I
wish I had done it --
instead. But I didn't
make a sound, just held
my cut finger that I couldn't
look at and looked at you
for a long time, trying
to guess where in you was your heart.

I had a thought and I
went back to the kitchen to put
a bandage on my cut and hold
it till it stopped bleeding
and only throbbed and I called
the police. Come over here
right now, I told them, I'm
going to kill him, and I gave
the address, the apartment,
the floor, the bedroom. . . I wanted
a bunch of them in case
they had to save me from
what you might do while you
were dying.

Or maybe what I wanted was what they did.

I took the knife and went first to unlock the door

for when they'd come, wondering

how long it would be. I stood

in the doorway to our room

counting to two hundred

in my mind and then counted

again, and heard them stamping

and running up the stairs

so loud I thought they'd wake you

and I ran to stab your

chest holding the knife in both hands.

It slipped sideways and tore

your shirt down your ribs

and only cut you some.

You jumped and opened your eyes

but it didn't seem like you

could see me and I stabbed you

again and it slipped again,

I couldn't make it go

into you, but too late to stop.

When the cops pulled you off

of me -- I don't know where

the knife went -- know what?

I had to run onto the back

landing outside and pull

the door shut, that always

locks, lock myself out

because you were yelling
Help me, Esther, help me
please God Esther, help,
they're killing me, Esther!
I would have rushed back
and killed those cops to get
them off of you.

Then the noise was gone away.
I was trying to figure out
how to get back in, freezing
and crying in my nightgown,
they must have taken you away
and what would happen to you
and how could I get you out
somehow when I heard two shots
from the street around front.
I don't know what they've said
you did -- when they came up
calling for me and let me
into our place and told me
what had happened to you
I couldn't seem to hear them.

What I thought of while they
were talking and talking and waiting
for me to say something
that I wasn't going to say
was how I'd last seen one

of them at your back holding

you by the collar the way

you grabbed mine the night

you tore my new blue dress

that you couldn't tell from silk

right off my back, left me

naked in a corner with my hands

up and you yelling at me

I spent too much of your money,

said I wouldn't leave you alone,

made me get in the closet

and locked me in there, shouted

through the door if I ever

tried to leave you, you would

cut me so bad, no one

would want me, while I cried

into a torn rag of my dress,

all ruined and lost and wasted.

That was for you, that dress,

to make you happy, make

you want to be with me.

All I had was a physical

need in my body, for you,

and wanting you to say

you loved me and be nice

the way you used to be.

I kept thinking that if
I was nicer to you
you'd get better, you'd be
all right again, and I'd
be special to you, like before.
Now nothing can change ever
between us, we'll always
be stuck where we were that night.
Only I'm the only one
to feel it, you can't.

The preacher will tell me I
should forgive you now,
should let it go, should come
to church once in a while,
I look at him and see
another man looking at me.
You used to tell all your
stories to your friends, the hard
knocks you'd had -- you said
harder than mine. Is this

story good enough, you think,

for me to tell it? But you

aren't listening, you can't

answer me, you never did,

you're not here but you won't

go away, and you can't

give me back what you took

if you're dead. If you could

give me back that one dress

then you could give me everything,

even the way one time you put

your hand in my hair after

you had hit me and said

Please don't cry, sugar, don't,

honey, stop crying, please,

I promise to you that

I'll never do it ever again.
```

---

## IC-0101: Bonsey

- Title: Bonsey
- Author (byline): Charlayne Woodard
- Work: Pretty Fire
- Publisher: Plume Drama
- Publication date as stated: Feb 1995
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CHARLAYNE, CAROLYN, ROBERT, MOTHER
- Teaser before the introduction: Yes
- Spoken words (computed): 1504
- Already set (do not supply): none

### Source block (context only)

```text
Author: Charlayne Woodward
Book: Pretty Fire
ISBN: 978-0452273856
Publisher: Plume Drama
Date (Month/Year): Feb 1995
```

### Introduction (context only: never use it for content warnings)

```text
There are safe secrets: A surprise birthday party, Christmas gifts, and what boy your best friend has a crush on. And there are unsafe secrets. The kind Charlayne Woodward keeps is an unsafe secret: as secret of assault, harassment and abuse. Bonsey by Charlayne Woodard.
```

### Performance text (classify this)

```text
CHARLAYNE: When I was ten years old, I loved . . . a secret. I'd give my eyetooth for anyone to share a secret with me. And kids did! Oh yes. They'd tell me their secrets, and I wouldn't tell a soul. To this day, I have those secrets locked up in my heart. But I had secrets I never told. Secrets I never shared with . . . (she finds an audience member) anyone.

(Pause.)

CHARLAYNE: Let's share some secrets this evening . . . I'll go first. When I was ten years old, my aunt Carolyn moved up from Savannah to live with us, while she went to nursing school. Every day when Allie and I came home from our schools, my aunt Carolyn would call us into her room.

CAROLYN: (Primping in the mirror;) "Charlayne, Allie! (As she waits for her nieces, she sings to "Shotgun" by junior Walker and the All Stars and does the Soulfinger. The girls interrupt her.) Do me a favor and run up to Bernie's corner store. Get me a block of Philadelphia cream cheese and a bag of onion and garlic potato chips. Here, honey. (She takes a dollar from her bosom.) Hurry back before your momma and your daddy get home."

CHARLAYNE: Now, in order to get to Bernie's corner store, Allie and I had to walk up Second Street, past School 6, past some neat little houses that looked a lot like ours. . . . It was a nice walk . . . until we reached that last house just before the corner. This house was right out of a horror movie. If it wasn't condemned, it should've been. This is where Robert Blair lived . . . . Robert Blair. And his seven, rude, lowlife, snot-dribbling-out-of-their-noses, bound-for-the-detention-center brothers. If they had parents, nobody knew. We never saw them. Just those Blair boys, out on their stoop, all hours of the day and night, shooting spitballs, cursing, smoking cigarettes . . . . Allie and I would start up Second Street . . . holding hands. (She walks across the stage.) We had our heads bowed to the ground. We were trying to be invisible. "Ssssh! Stop breathing, Allie. They might hear us!" (Looking up;) Too late. Robert Blair spotted us before we even got near his house. He'd come slithering across his old front yard (becoming Robert Blair, walking with an obvious "pimp, " smoking), had a cigarette dangling out the side of his mouth, lean up against his old, raggedy fence.

ROBERT: (Menacing.) "Bonesy! Hey, Bonesy! When you and your liver-lipped sister gonna give me some?"

CHARLAYNE: And as if that wasn't bad enough, he'd sic his dog, Sooner, on us.

ROBERT: "Sick 'em, Sooner! Sic 'em!"

CHARLAYNE: Now, Sooner was the dog from hell. He had one white, blind eye, with a whole lot of white stuff dribbling out of that. Then he had one black eye, that just came at you, like daggers. Old Sooner'd come tearing down that front stoop. I'd grab Allie's hand and we'd jump up on the nearest parked car. (She runs and jumps.) "No, Sooner! No, boy! Please, Sooner! Down! Down, boy! Down! No!

Stay, Sooner! Stay. Good boy . . . . " (climbs down from car and back pedals while watching the dog until they get to the Bernie’s – enters the door still back-pedaling, then heaves a sign of relief and turns) Hi, Bernie. A block of Philadelphia cream cheese and a bag of onion and garlic potato chips, please." Bernie would pass us the food over the counter, in a brown paper bag, and hand us our change. Now we had to get home . . . . Allie and I would look each other dead in the eye . . . "Get on your mark, get set, go!" And we'd tear out of Bernie's, running down Second Street, as fast as we could, but as soon as we passed Robert Blair's house, he'd sic that dog on us (running in a large circle), and old Sooner would be right on our heels, right on our heels . . . And not until we got past School 6 did Robert Blair call his mangy dog back home. (She stops running.) Every single school day, we risked our lives for a block of Philadelphia cream cheese and a bag of onion and garlic potato chips. Oh, but then came Saturday. We loved Saturday, because Saturday meant no going to school, no going to Sunday school, even. And no going to Bernie's! Because my aunt didn't dare send us on errands when my parents were at home. On Saturday, when we woke up, my mother would be preparing the "breakfast of life." You know what that is: grits, with butter; scrambled eggs with onions; fresh-baked biscuits with her own homemade preserves spread all over those; fresh-squeezed orange juice. . . . Ooooh! The "breakfast of life"! Mommy came into the living room and said,

MOTHER: "Charlayne, we've run out of grits. Run up to Bernie's corner store and get me a box."

CHARLAYNE: (Pause.) I looked around and Allie had totally disappeared. Then my mother said,

MOTHER: "Charlayne, it's raining out. You can wear your new rain slicker."

CHARLAYNE: My new yellow rain slicker! I got dressed in a flash, and Mommy took that rain slicker out of the closet. I put it on. You could still smell the rubber! It had this really keen hood that would just grip your face. (She demonstrates with her hands.) You couldn't see from side to side. And then it had this really keen beak that came down like this, so when the rain hit, the water would just slide off your head! Whoosh! There were these really great puddles left over from last night's downpour. (She jumps from puddle to puddle.) Made it to Bernie's. "Good morning, Bernie. Look at me! Can I have a box of grits, please? (Listens to Bernie.) A licorice?! Sure. Thanks, Bernie . . . Oh, Bernie, can I have one for Allie, please . . . ? Thank you, Bernie." Bernie passed me the grits in a brown paper bag, and he gave me my change. When I looked outside, it was pouring rain. I couldn't wait to get out in it. (Singing and dancing a la Gene Kelly.) (She freezes.) Robert Blair. I couldn't see him. But I could feel him right in back of me. So I started walking really fast. He came right up beside me. He was so close he was touching my arm. I couldn't see him, though, because of my keen hood.

ROBERT: "Hey, Bonesy . . . when you gonna give me some?"

CHARLAYNE: (Puzzled;) And I'm thinking . . . "Gimme some what?" Then I just took off, running . . . But Robert Blair was one of those big boys. And he was doing what big boys do. He ran in front of me, backpedaling, blocking me. . . . I couldn't get around him. When I tried . . . he grabbed me, he pushed me up, up, up onto School 6's steps, up against the iron gates that locked the school. He snatched my hood down off my head. He wrapped his arm around that iron bar in back of my head and grabbed my hair. He took his other hand and he held me at my throat. No one was out in that rain that day. No one in the whole world, but me . . . and Robert Blair. He was pressing up against me. He was breathing on me. "Let me go, Robert Blair. Please?" He knocked the grits out of my arm, onto the stone steps. ' And still pressing up against me, he took his hand and put it . . . up under my rain slicker, and he placed it . . . in between my legs. (Pause.) "Please let me go, Robert Blair."

ROBERT: "What do you call this . . . Bonesy?"

CHARLAYNE: "I don't know what you call it. I don't call it anything. Honest." And then he squeezed me down there, really hard.

ROBERT: "You got to call it something, Bonesy! I said what do you call it?"

CHARLAYNE: (In pain, frightened.) "I don't know what you call it, Robert Blair. Honest to God. I don't call it anything."

ROBERT: (Banging her head into the iron bars for emphasis as he speaks.) "What . . . do . . . you . . . call . . . this, Bonesy?"

CHARLAYNE: (Searching desperately for an answer.) "Okay . . . okay . . . okay . . . my mother's a nurse . . . she calls it something. (He squeezes her down there.)

My mother calls it . . . it's . . . Okay . . . ! Okay . . . ! It's . . . . a ragina?"

ROBERT: "A what?"

CHARLAYNE: (Yelling desperately.) "It's a ragina!"

ROBERT: "What the hell is a 'ragina,' Bonesy? Don't give me any of your big words! (He squeezes her.) I said (banging her head again), what do you call this?!"

CHARLAYNE: "Okay . . . okay . . . wait . . . wait . . . (Still searching desperately.) It's a . . . it's . . . it's . . . (humiliated) a pee-pee hole?" Well, the light came to Robert Blair's face. I watched him throw back his head, and fall back into that rain. Just like some horrible bird, Robert Blair flew all the way up Second Street. Laughing at me! (She notices what's left of the grits on the stone steps. Defeated, she kneels and attempts to gather as much as she can, and puts it back into the soaked box. Painfully, she stands and walks to her house. She's about to knock on the door, when she stops and decides to wipe away her tears. She pulls her "keen" hood back on her head, then . . . she knocks on the door.) "I'm sorry, Mommy. I dropped the grits."

MOTHER: "Would you look at you. You certainly did get caught in that downpour. Oh, it's okay, Charlayne. It's just a box of grits. Give me this mess."

(Mother takes the wet, tattered box and throws it out.)

CHARLAYNE: Then Mommy went into her bedroom and she came back with a dollar and an umbrella.

MOTHER: "Here. Run back to Bernie's and get me another box. Hurry now. Breakfast is waiting."

CHARLAYNE: And I just lost my legs and fell to the rug. I couldn't stand anymore.

MOTHER: "Charlayne, hey, come on. It's okay. (She kisses her.) It's okay. You don't have to go back. . . . No . . . Come on, let's get you out of these wet clothes. (Mommy helps her out of her rain slicker, shakes the water off, and hangs it up on a hook.) Take off those shoes and socks. I know your feet are soaked."

CHARLAYNE: Then my mother put on her own raincoat. She took back the dollar and the umbrella. And she left. I could hear Daddy puttering around in the basement, but I couldn't find Allie anywhere. And then I did. She was in her new hiding place, up under the dining room table, stretched out on the seats of the chairs. She was peeking out at me from underneath the lace tablecloth. And I could tell by the look in my sister's eyes . . . . that Allie already knew all too well . . . . what had happened to me.
```

---

## IC-0102: Breath, Boom

- Title: Breath, Boom
- Author (byline): Kia Corthron
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 2002
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CAT, PRIX
- Teaser before the introduction: Yes
- Spoken words (computed): 1228
- Already set (do not supply): none

### Source block (context only)

```text
Author: Kia Corthron
ISBN: 978-0822218494
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 2002
```

### Introduction (context only: never use it for content warnings)

```text
It's a fundamental desire to want to fit in, to feel accepted -- to feel loved. But what happens when our peers cast us off? For Cat, being an outcast has been a way of life. Though she is desperate to fit in -- even in juvenile detention -- there is no group she can fit into because deep down she believes "the big lie" that she is not worthy to be a part of any group. BREATH, BOOM by Kia Corthron.
```

### Performance text (classify this)

```text
Cutting focuses on Cat who is in juvenile detention for running away from her foster home and possibly prostitution at age 15 – In this cutting she speaks to Prix, her cell mate. (Jail cell – bunk cots)

CAT: (To Prix) My name is Cat. I’m coming to your group tomorrow. I told Miss Collins I didn’t feel comfortable in my group, she said Give it a try, you only been here a month, I said Some of them bitches threatenin’ me, say they gonna take my teeth out. Randy, Scooter. She said I’ll talk to ‘em. I said I wish you wouldn’t That really make life hell, I wish you just change my group please. The lie is, Randy and Scooter never said nothin’ ‘bout my teeth, I just hate their ugly faces wanted get away from ‘em. The truth is, Miss Collins tell ’em what I said I would be in life-threatenin’ trouble for lyin’ ‘bout ‘em the first place. Luckily Miss Collins buy it I’m your group tomorrow. (Beat) Lap a luxury. Three meals. Street clothes.

PRIX: You the only one around here ready to print up the welcome travelers’ brochure for jail.

CAT: I hear ‘em! Cryin’ on the phone, “My honey, my honey,” Most of ‘em honeys was kickin’ the shit out of ‘em daily and their friends? Their best girlfriend’s on the outside and so’s their honey guess what one plus one is equalin’? (Beat.) Could be worse. See them ugly green one-piece things they make the women wear? Least adolescents, we wear our own shit. (Beat.) Easy time. Eleven <months> left for me, shit. Scotfree and I’m fifteen, three more years a minor, I get caught, easy time. Eleven months. I know my roof? Know my mealtimes? shit. Damn sure beats the fosters.

PRIX: Usually all I hear’s you whinin’ ‘bout the clothes situation.

CAT: Lacka choices! I love my clothes, but wearin’ the same five outfits gets limitin’ after awhile. Ain’t my first time in. Fourth!

PRIX: Runaway.

CAT: Three more years I’m a criminal for it! Can’t wait ‘til eighteen! Runnin’ away (Beat) Dontcha never believe that crap about best to tell the counselor tell the teacher it’ll make things better. Cuz ya will get sent back home and just when ya thought things could get no worse, they do.

CAT: (to her cellmate, Prix) What’s the big one? Single most thing earned you all the gracious undivided esteem? I heard this: shot a enemy girl in the face. Then went to her funeral cuz yaw was best friends second grade, put the whole goddamn family on edge and every one of ‘em knew and not one of them said a word about it to you. (Beat.) And one time jumpin a girl in, and she not too conscious, but you jump your whole weight on her face ten times maybe? Twelve? ‘Fore a sister pull you off. And one time on a revenge spree, dress up like a man so no one identify you later, stick your hair under a cap and shoot dead some boy teen years old. And . . .

PRIX: Fifteen (pause: Cat is confused) I don’t kill no kids. Fifteen.

CAT: O.G.! you gonna earn it. Original Gangsta, people respect you long after you retire. Take me in! (no answer) You get it. The high, right? The kickin’ and smashin’ and breakin’ bones snap! Somebody lyin’ still in a flood a their own blood. You made it happen! Them dead, you done it! You ever get that high?

(Thinking silently about wanting to be in a gang.) Take me in! I tried once, Small little club I was interested in. Wore the right colors, I talked the shit. They wouldn’t even jump me in, I said “I’ll do it! Either way, all yaw stand in a line and rough me through it OR I’ll take the toughest one on, two minutes!” They just laugh. (Beat.)

PRIX: Wannabe

CAT: They think I ain't tough I got it! I can fight! I was four, these two boys was six, tried to steal my bike I flattened ‘em! And when my foster sisters steak-knife stabbed me and drowned me in the tub, somebody called an ambulance, he mouth-to-mouthed me back alive, said if I wasn’t strong I’da stayed dead. (Chuckles.) She’s dead! Jessie, she the one screamin’ “Hold her down! No air bubbles hold the bitch ‘til she dead dead dead!” Look who’s talkin’, she with her homegirls and boys thinkin’ she a member in good standin’, got drunk one night and said somethin’ smart to a homey, he blew her head off. (Laughs.)

PRIX: You ever wish you done it? You ever . . . You ever regret wasn’t you pulled that trigger?

CAT: (Confused) She’s dead.

PRIX: Yeah, but like . . . that thought. It ever get stuck your mind? Wishin’ the last thing she seen was you robbin’ her last breath?

CAT: (Beat – changes subject as she refocuses on her clothes) The clothes make me mad. How come only five outfits? (Beat)

PRIX: What makes me mad is music. John Philip Souza, trombone pansy crap. <But> fireworks got their own music: reports and hummers, whistles. Magic, each one born with that little sound. A gulp. A breath. And we holdin’ our breaths, waitin’ three . . . four . . . five . . . .BOOM! Then nothin’ left but pastel smoke, pink, blue floatin’ calm. Calm.

CAT: (Admiration) You the coldest fish I know! Ruthless! (Beat) You met Ms. Bramer? She’s the new Current Events -- she’s nice I hope she stick around awhile. She say the six ‘ o'clock news always hypin:’ “Tough on teens! Youth violence outa hand, try ‘em like adults!” But she say news never say three times as many murders committed by late-forties as by age under-eighteens. Ms. Bramer say if we violent where we learn it? Sow what you reap.

PRIX: Reap what you sow. (Long pause as CAT thinks)

CAT: (Suddenly sobbing): They took ‘em away! They took em’ away! . . . . . Little boy! Had a baby! Little boy, they make me, they made me adopt him away! They said Do it! They said Do it! (long pause while Cat composes herself) [It was] before I was charged! I oughtn’t be here no way, awaitin’ trail, innocent ‘til proven guilty, how come I gotta sit here for lacka five hundred? They ain’t proved nothin’ yet. (As Cat speaks she will pull the sheet off the upper bunk, then sit tying it.) You ever plan your funeral?

PRIX: Fireworks.

CAT: Knew it! Nothin’ somber for me neither, I got the tunes all picked out, went through my CD collection, I know who my special guest stars be, I figure they come, like this poor unfortunate fifteen-year-old girl died, aint the city violent and sad? <The celebrities> feel so depressed [they] come give a free funeral concert. (Beat) My coffin’s gonna be open. I’m gonna look good (Drift into daydreaming) I got the dress picked, and I want people to see it. You ever plan your suicide?

PRIX: Fifth grade

CAT: Pills? Gun stuck up your mouth?

PRIX: Off the Brooklyn Bridge. (puzzled) Would that kill ya?

CAT: <Know where I was yesterday?> Infirmary, doctor checkin’ me out after this girl come up to me pow! She say, “What your name?” I’m tryin’ to answer, “My name’s Cat” but before I get the first word out pow! She punch me in my face I’m all knocked out! Supper tonight, I seen her people, them girls follows her around, she weren’t there guess they threw her in the bean. I come to her girls, say, “Your friend ask me what my name is. My name’s Cat.” But soon as I say “Your friend ask me what my name is” they start laughin’ so hard I think they don’t hear the second part, so I keep sayin’ it louder but the louder I say it the louder they laugh. “My name is Cat!” (Beat, stands on the upper bunk.) “MY NAME IS CAT!” (Cat has swung the sheet --- tied into a rope—around an overhead horizontal pope and secured it. It is suddenly clear that she has formed a noose. Standing on the edge of the bunk, she has stuck her head through it. If she jumps off, she’ll hang. Her eyes are closed, her breathing harsh and uneven. The most delicate push would be enough to knock her over.)

PRIX: Jump!
```

---

## IC-0103: The Bridge

- Title: The Bridge
- Author (byline): Paula Cizmar
- Work: Seven
- Publisher: Dramatists Play Service
- Publication date as stated: Oct 2009
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MARINA, WOMAN, SVETLANA, MAN
- Teaser before the introduction: Yes
- Spoken words (computed): 1415
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paula Cizmar
Book: Seven
ISBN: 978-0822223511
Publisher: Dramatists Play Service
Date (Month/Year): Oct 2009
```

### Introduction (context only: never use it for content warnings)

```text
1993 Russia. Domestic violence is not classified as a crime. Victims are invisible. Their cries unheard. Until one woman, takes it upon herself to, at last, provide these victims with a voice and end the silence, beginning with a single hotline.

The Bridge. A documentary play by Paula Cizmar
```

### Performance text (classify this)

```text
Moscow. Marina, walks across a long stone bridge. She looks toward the end of the bridge and suddenly slows down. (Perhaps to feed a bird or two? For blocking purposes this was used to define the area where she is by the bridge . . . the office set up is straightforward enough with setting pieces.)

MARINA: I like this bridge. It goes over the Moscow River.
It ends up at St. Basils.
My office is near.
This is my favorite part,
In the wintertime, the pond is frozen, people are skating.
In spring, the leaves are just coming out --- It’s like a green smoke, around
the trees. The leaves are not out yet, but you feel as if they are coming.
My favorite time is when it is snowing.
Snow makes it beautiful.
This is the time for me to put myself together.
To come to some harmony with myself.
Because if you are not in harmony with yourself, this is a very difficult job to
do.

MARINA: I’m thinking about my work.
I’m thinking about what I have to do.
Thinking about --- (A telephone rings, sounding muffled, distant. Marina watches
the river, trying to steady herself, trying to shake off a memory. Finally:)

She never told me her name. --- Crisis center for women. How may I help you? Then she says,

WOMAN: --- I heard you on the radio --- My husband---my husband is beating me---

MARINA: --- Tell me what is happening ---

WOMAN: --- He has beaten me for twenty-six years.

MARINA: --- Tell me your address.

WOMAN: --- my husband is very powerful.

MARINA: --- I will come and bring the police.

WOMAN: --- You don’t understand. If you call someone, he will find out ---

MARINA: --- Tell me ---

WOMAN: --- Before you can get to me, I will be dead.

MARINA: She is one of the ones I could not save. (Marina watches the river a moment, breathes in the cold air.) Walking over this bridge. The time for me to evaluate In 1995, statistics were published that said that Fourteen thousand women a year had been killed by their husbands in Russia. Every hour in Russia, a woman dies due to domestic violence. What am I going to do? The Beginning --- No One Talks It was post-Soviet times. So much was new to us. I am assigned to the Institute for Socioeconomic Studies for the Population, and we put together a survey about women’s issues. We get two letters from women --- letters we don’t know how to classify --- talking about things their husbands are doing to them. My administrator at the Institute says: --- You have just come across a case of domestic violence. I have never heard of this. At my son’s school --- Peter was seven years old --- One morning I am talking to two other women --- I am doing this survey about domestic violence … Both of them just freeze. Then they say, --- What do you mean, domestic violence? (To the audience.) When I was growing up in the Soviet Union, “domestic violence”---nobody talked of such things. We did not even have words for it. So I explain that it is . . . when husbands are controlling, jealous, when they put you down, isolating you. The psychological slowly comes to physical abuse. --- both of them say they are abused. One for six years. One for ten. I feel something sinking inside me. The director of the Institute. She gives me an office and a phone. And I start the domestic violence hotline --- actually I don’t call it a hotline, I call it a trust line. Because all the women who call can do is trust. It is six months into my work; I get a call from a woman. Svetlana. (Telephone rings.) --- Crisis center for Women. How may I help you?

SVETLANA: --- I think my husband is going to kill me. It started when I told him I was pregnant. I saw his eyes.

It was like someone flipped a switch.

MARINA: Something about this call. I am scared for her.

SVETLANA: --- When the baby was nine months old,
I was holding the baby.
He came to me, and I didn’t know what he was going to do.
He grabbed me by the hair and started beating my head against the wall.
I got to the bedroom and covered the baby with my body.
In the morning. He said he was drunk. He asked me to forgive him.
But this time, I said No.
No. I want a divorce.
He looked at me and said: I’ll kill you.
--- I really believe him.

MARINA: So I call the police. I speak to the officer. He says, I will see what I can do. Next thing he does, he calls the husband.

(Marina back at the bridge.) <In Russia> He beats you, therefore he loves you. It’s a saying that comes from the sixteenth century. It was called “domostroi.” Domostroi were basically household rules. These rules described how a man should punish his wife to make her more obedient. Don’t beat her on her face, because you won’t be able to show her in public. It’s better to use the whip rather than a stick because it will be more painful so she will learn her lesson better. He beats you, therefore he loves you. Since the sixteenth century it has been an excuse. I didn’t have much. My salary is not enough, and I don’t know how I am going to feed my son. One friend, she brings me a set of wonderful dishes. Very nice colors and cheerful. And I did need dishes. It was very thoughtful. But I look at her and say, I cannot accept this. And she says, --- You know what, you have to learn to accept, not just give. And this teaches me. I start to realize I am supported by so many other people. That keeps me going. It’s a community. When you grow up with love around you, that gives you internal freedom to share this love with others. It gives you an internal responsibility to share this love, and it gives you the ability to share it. For the first few months, it was hard. At one point my son came to me and said from now on, he’s going to be taking care of me --- and I suddenly realize, I have to give him his childhood. I need to be strong for him. So I say, No. You are still a boy. Someday, when you grow up, I will need your help. You will take care of me. But now, I will take care of us. After work, I would get out of the subway and stop on the way and get something nice --- cookies or fruit, something to cheer us up, and then come home. (A telephone rings. Distant.) But then, this guy starts calling me at home. He is watching me. And the thing is, he---See, threat calls on the hotline are very common. But this guy knows who I am and knows my home number. So he calls and he says,

MAN: Marina? Aren’t you afraid to do what you are doing?

MARINA: I say, Excuse me, who are you?

MAN: I’m someone who was affected by your work. I know everything about you…

MARINA: ---Who are you?

MAN: --- Aren’t you afraid that your son is alone in the street?

MARINA: That is the worst thing. I feel that somebody has stuck a knife in my heart. He knows about my son. I don’t allow Peter to pick up the phone at home; I have my parents pick him up from school every day, he is never, never alone. I am scared. He calls,

MAN: --- I know where you live. --- Aren’t you afraid for your son?

MARINA: Don’t you dare touch my son, ever. Don’t even think about it.
I know what he is doing. Control me. I try to use all my knowledge and skills
not to play into this game.
I buy a phone with caller ID.
And when he calls, I say to him,
--- I’ve got your number. If you are not going to stop, I am going to the police.
Don’t think things go unnoticed, unpunished. Don’t.
And he hangs up.
And he never calls again.
My phone didn’t identify his number totally.
I was bluffing.
But it was a great bluff. (Marina huddles into herself, walking into the wind. She
stops. Watches the river.)
Last year a woman was killed and they were showing the story on TV. Her
husband was beating her every night.
She died from the beating.

Everybody knew this was going on for three years.
Why? Why did no one do anything?
Honestly, every time I hear about another case, I feel like I am back in 1993!
Violence is still going on!
What am I going to do? (Marina watches the river flow by.)
This bridge is called Bolshoi Moskvoretskiy ----
You have to be careful on this path. There is so much responsibility; there are
so many people that matter.
Our work is not done yet. (Marina -- into her office. A telephone rings.)
--- Crisis Center for Women.
---What can I do for you?
---Can you tell me what happened?
---Tell me, please so that I can help. (Another telephone rings.)
```

---

## IC-0104: Bright. Apple. Crush.

- Title: Bright. Apple. Crush.
- Author (byline): Steve Yockey
- Work: Off Off Broadway Festival Plays, 32nd Series; Pgs 33-41
- Publisher: Samuel French
- Publication date as stated: Oct 2010
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NANCY
- Teaser before the introduction: Yes
- Spoken words (computed): 826
- Already set (do not supply): none

### Source block (context only)

```text
Author: Steve Yockey
Book: Off Off Broadway Festival Plays, 32nd Series; Pgs 33-41
ISBN: 978-0573660238
Publisher: Samuel French
Date (Month/Year): Oct 2010
```

### Introduction (context only: never use it for content warnings)

```text
Short workdays, smaller class sizes, long breaks – including the entire summer off. “Our schools are excellent places to work,” insists our society. So why, amid reports of depression, breakdowns and suicide, is teaching now rated one of the most stressful occupations in the country?

According to Stan Gilmore of the Institute of Counseling, “Most teachers, if they are honest, will testify that at some point in their teaching career they have encountered difficulties in coping with the relentless pressure to maintain order, which has led a "mental breakdown".

And while the majority of teachers simply leave the profession in 5 years or less . . . teacher Nancy Miller stays, and her atypical breakdown becomes an extreme example of how things can go horribly wrong.

Bright. Apple. Crush by Steven Yockey
```

### Performance text (classify this)

```text
NANCY: (Pgs 33-41) Teaching is not for everyone. I’m Nancy, Nancy Miller. You might have read about me. Those kids were horrible. I can’t say a single nice thing and their parents were just . . . Some people shouldn’t be allowed to have children.

There was one little boy who would kick me as hard as he could. Every chance he got. I couldn’t believe it. Ridiculously painful. Every day, every time, kicking me. And he was one of the better kids. If that gives you an idea of how bad they really were.

NANCY: It’s hard when you decide you’re really going to try and help people. Become a teacher; take a job where you can make a difference. Where you think you can make a difference. It’s hard when that turns out to be impossible. That’s frustrating. Especially when you can help a kid and they don’t want it. Like they know anything. When you’re trying to help a kid and they act like they’re smarter than you. A bunch of ****** ten-year-olds. Like they know anything . . . Except how to be mean. No one warns you about that, in college, in your classes. Even when you’re assistant teaching. No one tells you. Kids can be terrible.

I remember so vividly the moment when I just snapped. I was at my desk. I was trying to explain photosynthesis. Well, the way you explain photosynthesis to a bunch of ten-year-olds.

(In her condescending teacher’s voice) “The plants have their leaves and the sunlight shines down, bright light . . . . “

And as I’m trying to each these kids something, I’m writing on the board, with my back to them like this (she turns and speaks over her shoulder). And I get hit with something, hit hard on the shoulder and then again in the leg. And again, in the hip. It took me a moment to even realize what was happening. They were throwing rocks at me. These kids in my class, these young kids, were actually throwing rocks at me and laughing. I couldn’t even speak. They were hitting me.

I took the rest of the day off. I went home. (She pulls an apple from behind her back where she has been hiding it in one hand or the other . . . ) While I was at home, I had some time to think. To really thing about what happened, about everything that had happened in my three months at that school. I made some decisions. About those ***** ten-year-olds. If you can’t teach them to even be human, then what good are they?

(she tosses and catches the apple) The healthiest snack in the world. I passed them out and said: (a return to the teacher’s voice) “All right, it’s important that you all stay healthy. But I know that not everyone loves to eat apples. So here’s a little deal for you guys: Whoever finishes their apple first will get an extra twenty minutes at recess.”

It all happened so quickly. They just started tearing into the apples. And I’ll confess that it was exciting. I didn’t expect them all to react with such enthusiasm for just twenty extra minutes at recess. I thought it would somehow be harder.

I might have used too much poison. If I had known they’d be so voracious, I probably would have eased off a bit. I like to think I would have been more restrained. But that might be too generous, really.

It took about ten minutes before the first one started convulsing. But it happened quickly after that. I wouldn’t let any of them go to the bathroom, I wouldn’t let any of them leave. I told them to stay in their seats, and for the first time, and I don’t know if they were afraid or disoriented or just stunned, but they did as they were told. I sat behind my desk and watched these horrible children drop to the floor or collapse onto their desks one by one in pools of spit and some crimson streaks. And they were crying and asking for help and confused. Clearly confused. It’s hard for me to say this, but honestly it was a real delight to see these worthless children suffer the way that I suffered when all I wanted to do was help them become better people.

There were only one or two left mildly conscious when I even began to realize that this might cause a problem. I knew they wouldn’t understand. No one. So the general reaction didn’t surprise me. Maybe some of the other teachers . . . but no, no one did. But I think the other teachers were secretly proud of me.

I don’t even read the papers or watch television anymore, because of the ridiculous things people are saying about me. Saying I hate children. It’s amazing what people will believe. I took that job because I love kids. Those weren’t kids though, you see? They were . . . . . something else.

I’ve been told as part of the whole court thing, that I’ll be going to a hospital. Where someone will take care of me for a change. That will be nice. Healthy. Or, I don’t know . . . . It doesn’t matter anyway. No harm done. (she holds out the apple . . . . ) Apple?
```

---

## IC-0105: Broken Child

- Title: Broken Child
- Author (byline): Marcia Cameron
- Work: Not specified
- Publisher: Kensington Publishers
- Publication date as stated: Jan 1996
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DOCTOR, MARCIA, MOTHER, EMILY
- Teaser before the introduction: Yes
- Spoken words (computed): 1381
- Already set (do not supply): none

### Source block (context only)

```text
Author: Marcia Cameron
ISBN: 978-1575660004
Publisher: Kensington Publishers
Date (Month/Year): Jan 1996
```

### Introduction (context only: never use it for content warnings)

```text
The autobiographical narrative, Broken Child by Marcia Cameron takes us on a harrowing, unforgettable journey into the nightmare of parental abuse and the darkness of mental illness. As a way of coping with daily abuse at the hands of her mother, Marcia Cameron’s created Emily, an alternate personality who from the age of three became her constant companion. Broken Child by Marcia Cameron.
```

### Performance text (classify this)

```text
(NOTE: Paragraphs are Marcia’s narration as an adult looking back on her childhood – Her flashbacks are noted as character’s speaking (ex MARCIA:))

I couldn’t make the blood stop. It was everywhere. I got in my car to escape. As I drove I kept taking my hands off the steering wheel to wipe the blood from my eyes. I made an instantaneous decision. Enough. I could do no more, stand no more, be hurt no more. I unbuckled my seatbelt, closed my eyes, and pressed the gas pedal to the floor. “Let me die. Just let me die!”

Lying in a hospital bed in walked a tall man

DOCTOR: “My name is Dr. Williams . . . smashed femur . . . fractured lumbar . . . . “ Struggling through pain and drugs I spoke the only thread of thought in my mind “Please let me die. I beg you.” Dr. Williams held my hand.

DOCTOR: “Marcia, how did you get all those fractures I saw on the X-rays? You have many . . . “

MARCIA: “I don’t know.” Nothing made sense. The year was 1982, I was forty-one, and my mind was in chaos. All my adult life I have lived what I felt was a charade. I was a great actress playing a role covering up for the missing on the clock, living with unexplainable fears and panics, fighting suicidal impulses, and battling depression. I had a childhood I kept trying not to remember . . . My first memory of abuse was the closet. I spilled milk all over the table and in a rage my mother dragged me to the closet under the front stairs. My mother struggled with my flailing arms and legs as I screamed “NO, Mommy, no! I’ll be good! I’m sorry I spilled my milk! She shoved me into the blackness of the closet. I screamed and screamed, throwing my whole body against the door. The blackness was encompassing. I felt I couldn’t breathe. I have no way of knowing if I was there for minutes or hours. At three and a half it seemed forever. My mother opened the door. I looked at her in defiance

MARCIA: “Just wait until Daddy gets home and I tell him what you did to me!” My mother grabbed my arm and dragged me up the stairs to my bedroom, she threw me on the bed, she tied my arms and legs to the posts of the bed. Her wild eyes were looking at me but not seeing me . . .

MOTHER: “You are a wicked little girl. If you ever tell anyone about what I do to you I will give you away to the gypsies. The gypsy men will tie you to their wagons and they will hurt you. And you will never see daddy again. You must never tell anyone I hurt you.” I writhed against the kerchiefs binding me and screamed and screamed and screamed.

MOTHER: “You must not tell” . . . When daddy came home I did not say a word. Abuse breeds more abuse. The closet became a more regular occurrence. In the long hours of silence and imagination Emily, my imaginary escapist friend, became more real to me. She could fly, breathe under water, she could even dare to be angry. One time I was put in the closet for what seemed an eternity. I worried that I had been forgotten. I wet my pants. My stomach cramped and I doubled over in pain . . . I used to corner to defecate . . . I sat in the stinking black closet and waited and waited.

EMILY: “I’m here! We can’t stay here. It stinks.”

MARCIA: “We can’t go, we have to stay here”

EMILY: “She’s mean to leave us in here. There is nothing to do. It isn’t fair. I’m getting really mad. You know what? Let’s go play with the ca-ca in the corner. Let’s put it on the walls and let mommy know how mad we are.”

MARCIA: “NO! We can’t do that. She’ll hurt us.”

EMILY: “I don’t care” Emily went up to the pile of feces in the blackness I watched in fascination as she smeared and painted all over the walls getting it in our fingers and hair. Letting it cover us in angry satisfaction. When the closet door opened, mom let out an angry yell

MOTHER: “What a truly evil child you are!”

MARCIA: “Emmy did it, mommy. I’m sorry. She did it.”

MOTHER: “Now you’re even a liar!” She shoved me back into the closet.

MARCIA: “See, Emily, being angry just makes it worse”

EMILY: “It was worth it” And that began our lifetime of differences. Emily couldn’t help me in moments of intense physical pain. No fantasy could take away the pain. There was the old enema bag I hated. My Mother would strip off my clothes and put me in the empty tub. Then she would run hot water into my while I sobbed.

MARCIA: “I’m sorry I’m evil, mommy. I don’t mean to be bad. Stop! Please stop! It hurts! I’ll be good I promise to be good!” The pain got so intense . . . I learned to focus on the gold drain, hunched in agony, pretending I was going down, down the drain into blue water where I was free. There were many nightmares; nights I didn’t sleep, nights when physical pain kept me awake. One day while trying to help set the table I dropped the cream pitcher and it exploded in a spray of glass. Mom dragged me up the stairs and tied me to the bedposts again. She left the room for what seems a hundred years. My mother came back with straight pins. As I lay immobilized in my tied up position, she took pins and stuck then through my labia as though I were a thanksgiving turkey. She untied me and left the room. The pins still sticking through my parts and the ends of the pins stabbing into my left thigh. I couldn’t see the pins to take them out. Getting stabbed harder with each move, I waddled to the bathroom mirror. I saw the drops of blood spread on the white hexagonal tiles. I was crying in great hiccupping sighs, as I pulled out the pins one at a time. My body healed faster than my mind. The terrorizing continued. I lived in constant pain. It was part of my life. I still tried not to provoke violence. No one in the world tries harder than an abused child . . .

MARCIA: “I must not talk loudly. I mustn’t laugh. I mustn’t run in the house. I mustn’t spill things. I must never be angry.” Some things I accepted. Because I was evil, I must be burned, cut, hit, and locked up. My sense of abandonment was the most intense I had ever experienced. I was alone-terrifyingly frighteningly alone. I couldn’t even escape in fantasy. I was deeply depressed. I walked onto the balcony overlooking the cement driveway. The only thought was a compelling need to escape . . .

EMILY: “Let’s leave”

MARCIA: “I wish I could fly like you. I would fly away. No one loves me,”

EMILY: “It's easy just flap your arms real hard and you’ll go up, up into the sky. You’re right. No one loves you.”

MARCIA: “Will you help me fly?”

EMILY: “Sure! I’ll go with you. We’ll never come back.” I climbed onto the railing of the balcony, looking up at the sky. I do not remember consciously choosing to die . . . merely to leave what I could not tolerate anymore. I stood on the rail flapping my arms, determined I would fly away. I took a giant leap off the rail and plunged head first from the second story balcony. I felt no fear as I fell, merely a fascination that flying didn’t work. I never told anyone I jumped off the balcony on purpose. My story is one of child abuse in the extreme, and the multiple personalities I created to deal with the pain. The cost of child abuse is a story that needs repeating until every baby born is cherished and safe. Writing this story will be worth the effort if even one abusive parent reads this and seeks help. It will be enough if one more hurt human being feels there are answers to the inner pain. Maybe like all authors I am inspired to write so like footprints in the snow, someone will know I lived. . . Not well, but I’m here.
```

---

## IC-0106: Bums (Evelyn, aka Mary)

- Title: Bums (Evelyn, aka Mary)
- Author (byline): Robert Shaffron
- Work: Off-Off Broadway Festival Plays, 14th Series; Pgs 101-121
- Publisher: Samuel French, Inc.
- Publication date as stated: Jan 1989
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: MARY
- Teaser before the introduction: Yes
- Spoken words (computed): 1359
- Already set (do not supply): none

### Source block (context only)

```text
Author: Robert Shaffron
Book: Off-Off Broadway Festival Plays, 14th Series; Pgs 101-121
ISBN: 978-0573623639
Publisher: Samuel French, Inc.
Date (Month/Year): Jan 1989
```

### Introduction (context only: never use it for content warnings)

```text
This is Evelyn Kantmeier’s story. Evelyn Kantmeier, also known as Mary.

But before Mary shatters the silence with fragmented faith and fury, it’s important to ground her story in the stark reality faced by many in the United States today. * On a single night in 2024, over 770,000 people were experiencing homelessness, the highest count on record, with roughly 36% of them living unsheltered on the streets, in cars, or in encampments rather than in shelters. ** Within this population, mental illness looms large: about 22–26% of homeless adults are living with a serious mental illness. And broader research estimates that up to two-thirds of unhoused individuals have a current mental health disorder when substance use and mood disorders are included.

These numbers remind us that Evelyn’s unraveling isn’t just personal tragedy. It reflects a broader crisis of displacement, invisibility, and unmet care that haunts communities across the nation.

Bums by Robert Shaffron

MARY is on the stage writing furiously in the margins of a discarded newspaper. She is overweight, slovenly, looks to be in her 50s but may be younger. Next to her is a fold-away shopping cart with a variety of objects: bags, clothing, a thermos, newspapers, etc. She suddenly stops writing, and looks up at the audience, suspicious.
```

### Performance text (classify this)

```text
(cutting revised and expanded, 2026)

Lights up on Evelyn (aka Mary). She is absolutely still and looks out directly into the audience.

She speaks as Evelyn, the woman Mary was before going mad. Rational, a little shy.

MARY: (Pg 112) I don’t know when I stopped living my life and my life started living me. (beat) My mother was a Christian. A Bible slamming, fire and brimstone, hallelujah Christian. I remember the day — the night — of her conversion. I was sleeping. She tore into the apartment — I slept on the couch — and she was out of breath, and her hair was, well, some of it had slipped out from under the elastic band she always had it pulled back in. And she ran around the room turning on all the lamps, and she turned on the light in the little half-kitchen, and she turned on the lights in her bedroom and left the door open so the light came into the living room where I was sleeping. I sat up, I was scratching and trying to straighten the crumpled sheets under me with my eyes closed the lights were so bright and I asked her, "Ma why are you turning all the lights on like that it hurts my eyes." And she rushed over to me and she pulled me off the couch onto the floor and said, "Evelyn, we’re gonna get down on our knees and pray. In the light. And we’re gonna pray to the Lord that we may always live in the light. The clean, pure holy light that falls down on us from the good Lord in heaven." We’d never prayed in our lives. I didn’t even know what praying was, really. I knew people prayed in church. I’d seen pictures of churches, and they always looked beautiful and scary with the colored lights all coming through the stained glass windows and shiny wood benches and gigantic stone arches, and I wondered how in hell we were gonna pray in our little apartment with the greasy walls and the chipped tile floors and bare lightbulbs — scary but not beautiful like the churches. (beat) All Mother wanted was a man who wouldn’t leave her so she brought God home. And he stayed. Mother went crazy with religion. And as soon as I was old enough, I did the only thing I could think to do. I got pregnant and left home. Amen

MARY: (Pg 103-104) Whattaya lookin’ at? Whattaya lookin’ at?? Bastids always lookin’, lookin’ — wanna see what I’m writin’ here. Always lookin’ at me outa the sides o’ their eyes so they think I don’t know they’re lookin’. Know what I’m writin’ here? I’m writin’ the Bible. That’s right. Ya read the Bible, ain’t ya? Well, I wrote it. Only it ain’t finished. I gotta finish it. Sometimes I ain’t got enough paper and I gotta write it on the New York Newsday. Only first I gotta cross out all the words that’s already printed there so nobody gets the Bible mixed up with the New York Newsday.

(an outburst) HEY YOU TRYIN’ TO LOOK UP MY DRESS?! I KNOW WHAT YOU WAS LOOKIN’ AT! YOU JUST GET YOUR EYES OUTTA THERE AIN’T NOTHIN’ UP THERE YOU GOT NO BUSINESS GOOGLIN’ AT! I KNOW WHAT YOU WAS TRYIN’ TO LOOK AT SNEAKIN’ PEEKS UP MY DRESS WHILE I’M WRITIN’ THE HOLY WORD!!

(a beat, then back to normal tone.) You know why I’m writin’ the Bible? You know why? God tol’ me to. God the little infant Jesus tol’ me to. You know why he picked me? He knows the evil I seen. That’s right. I seen the worst evil in the world and the Holy Lord our savior Jesus Christ tells me the word and he writes the Holy Epistle through me. I’m a vessel. I’m a vessel of the Lord. You wanna know my name? I’ll tell ya. It’s Mary. That’s all. Nothin’ else. Just Mary. Used to be Evelyn Kantmeier. Now it’s Mary.

(Pg 106-108) (rummaging through one of her bags) Whattaya lookin’ at?? Wanna see what’s in my bag, doncha? Everybody does. Everybody wants to see. Wanna know? Wanna see what’s in here? You’ll rot in hell first. Nobody gets in my bag. It’s my bag. It’s fulla my treasures. Man touched my bag once. He’s sorry. I was sittin’ in Grand Central Station I like it there you can feel the Lord’s presence in the echoes. I’m sittin’ there writin’ the Bible with my special bag down between my feet I keep the handle wrapped around my leg so no stinkin’ bastid can steal it ‘cause everybody wants it. Wants to possess it it’s precious. I’m sittin’ right on that bench writin’ and keepin’ an eye out for evil — I’m the Holy Lord’s guardian of evil. I keep an eye out when God is watchin’ over things over in Italy or somethin’ — bastid comes up tries to touch my bag. Musta been crazy is the only thing I can figure. But I got him. Fixed the crazy son of a b**** good. Put a curse on him. Ordained his hands to fall off. He’ll never touch another bag again. Eye for an eye. I wrote that.

(beat) Don’t touch my bag. You don’t ever touch my bag. Thou shalt not lay a rotten finger on my bag and that’s a commandment. (beat) You wanna know what’s in my bag? Sacraments. Holy sacraments and treasures and some sacred relics. And some cigarettes. (beat) Alright. I’ll show ya. But only if you swear on the holy mother’s eyes not to covet nothin’ in here. But you will. You’ll covet it all. It’s holy. (pulls out an old cardigan sweater with pearls or sequins on it. It’s wrinkled and dirty) Here. This here’s sacred vestments. Jesus wore this at the Last Supper. Then he gave it to me. Isn’t it beautiful? (shakes it so the sequins catch the ligh.) It glows. That’s holy light. You wanna touch it? It heals. (holds it out, then snatches it back) Don’t even try.

(rummages in the bag and finds a keychain with keys on it; shakes it) This here’s Jesus’ lucky keychain. He blessed this. Sometimes it spouts wine. (goes back into the bag, pulls out a crumpled box of Count Chocula cereal) This is the holy communion. This box got the wafers that’s the flesh of Christ. (opens the box, places a single piece of cereal on her tongue) Ain’t supposed to chew it. Gotta let it lie on your tongue and count your sins while it melts. (takes a handful of cereal and eats it.) Only I ain’t got no sins. I been purified. ‘Sgot marshmallows in it. (rummages in the bag again, pulling out a succession of objects, until she comes up with a tattered baby doll) This is Him. This is the Holy Infant Jesus himself. Not Him. His image. The Baby Jesus. My beautiful, blessed Baby Jesus. This here’s loaded with holy magic spiritual power. No one, no one can ever hold this Infant Jesus. ‘Cept me. One little touch and he’ll resurrect and smite you but good.

(Pg 116-118) (suddenly angry) Whattaya think I’m a goddamn freak show??! Don’t look at me. I was in the convent for a long time. But I escaped. The religious persecution of Sister Mary (hysterical laugh, then stops abruptly) They refused to call me by my chosen holy name. Called me Evelyn. (mimicking) Evelyn, DEAR, don’t you want to sit in the music area with the other ladies? Evelyn, DEAR, wouldn’t you like something to eat? (back to her own voice) Food there was rotten. Lousy convent. (beat) I took the holy communion every day. Twice a day. They brought it to me in my cell. Barged right in with their communion trolley. Kept the wafers in little white paper cups to keep the holiness from leaking out.

I was in the convent ‘cause of the evil I seen. I seen a woman. A terrible, cruel woman. With a child. A little boy. They was in the playground in the park. Swing mommy swing, said the little boy. The woman picked him up and held him under his tiny thin arms, and put him on the swing, all dressed in the blue romper she sewed for him herself. (gets the doll out of her bag and mimes the story with the doll)

It was a beautiful day that day. The sun was so bright and loud, louder than all the evil in the world. So loud it shut out all the evil. Swing mommy swing. So gently she pushed him in the swing. Higher mommy higher. The sun was so bright, the light was so beautiful. She pushed harder. A little harder. He swung farther away. Higher mommy higher. He laughed. She loved the sound of his laugh. It was magic how she pushed him and he flew away and back, away and back. Laughing, screaming with joy as he flew up into the light.

(by now she is on her knees, clutching the doll to her breast and rocking with it) MY BABY! JESUS MY JESUS GOD MY BABY WHERE IS MY BABY!!!!!
```

---

## IC-0107: Burned Alive

- Title: Burned Alive
- Author (byline): Souad
- Work: Not specified
- Publisher: Bantam Books
- Publication date as stated: Aug 2005
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SOUAD
- Teaser before the introduction: Yes
- Spoken words (computed): 2694
- Already set (do not supply): none

### Source block (context only)

```text
Author: Souad
ISBN: 978-0553816303
Publisher: Bantam Books
Date (Month/Year): Aug 2005
```

### Introduction (context only: never use it for content warnings)

```text
Honor killings. Almost always, the victim is a woman; the killer a male family member. The woman’s offense is invariably refusing to bend to the will of her family. She is a sister who falls in love with a man not of her family’s choosing, She is a daughter who refuses to agree to an arranged marriage, sometimes to a man old enough to be her father. She is a wife who can no longer stay in an abusive marriage and divorces her husband.

According to the Washington Post, it remains a common practice in Pakistan today, with an estimated 1,000 Pakistani women murdered every year. There are few survivors; Souad was one of the “lucky” ones. This is her story. Burned Alive by Souad.
```

### Performance text (classify this)

```text
SOUAD: (Pg 1) I am a girl. A girl must walk fast, head down, as if counting the number of steps she’s taking. She may never stray from her path or look up, for if a man were to catch her eye, the whole village would label her a charmuta. A girl must be married before she can raise her eyes and look straight ahead, or go into a shop, or pluck her eyebrows and wear jewelry. My mother was married at fourteen. If a girl is still unmarried by that age, the village begins to make fun of her.

SOUAD: (Pg 2-3) It is a curse in my village to be born a girl. I have no memory of having played games or having fun as a child. The only freedom a girl can dream about is marriage, leaving your father’s house for your husband’s and not coming back. I dream about it. Ever since I heard that a man spoke to my father about me, I have been consumed by impatience and curiosity. I know [Faiez] lives three or four steps from us. He must have a good job in the city because he never dresses like a laborer. He always wears a suit, carries a briefcase, and has a car. I imagine I am married to him and he’ll come back from work at sunset and I will remove his shoes, and on my knees I will wash his feet as my mother does for my father. I will be a woman who has a husband!

(Pg 5) As I have mentioned, where I come from, being born a girl was a curse. (Pg 20) In my village, if the men had to choose between a girl and a cow, they would choose the cow. My father repeated endlessly how we girls were not good for anything. A cow gives milk and produces calves. What do you do with milk and calves? You sell them and bring the money homme, which means a cow does something for the family. But a girl? What does the family get from her? Nothing.

(Pg 52) Rights do not exist [for women] There are customs. This is the way it is and that is all. If your father points to a corner of the room and tells you to stay in that corner the rest of your life, you won’t move from there until you die. If your father places an olive in a plate and tells you that today that’s all you’ll have to eat, you eat only that olive.

(Pg 34-35) Once, by mistake, I picked a green tomato. It was half yellow and half red and was beginning to ripen. I knew that I shouldn’t have picked it but I was working too fast with both hands. My father shouted: You fool! You see what you’ve done?” He struck me and then he crushed the tomato over my head. “Now you’re going to eat it!” He crammed it into my mouth and he rubbed my face with the rest of the tomato. It was acid, very bitter, and smelled bad. I was forced to swallow it. I couldn’t eat anything after that because my stomach was upset. But he pushed my head into my plate and made me eat my meal, almost like a dog. He had me by the hair. I felt sick but I couldn’t move. The more I said my head hurt the more he persisted din crushing my face into the semolina. Then he wiped his hands on a napkin, threw it at my head, and went and calmly settled himself in the shade on the veranda. I had food all over my face, my hair, and in my eyes. I never forgot this green tomato, and the humiliation of being treated as less than a dog. He was the symbol of an enslavement that was taken for granted, that I accepted, bending my back and lowering my head under the blows, like my sisters and my mother. This was everyday life.

(Pg 48-49) Being married was the most I could hope for in terms of freedom. But even married, a woman risked her life at the least lapse in her conduct. I remember a woman who had four children. One day I heard my mother say that the village was telling stories about her. People thought she was involved with the owner of the store because she went there frequently to buy bread, vegetables and fruit. One day my mother said that her brothers had gone into her house and cut off her head. They left the body on the ground and walked around the village with her head. She also said that when her husband returned from his job he was happy to learn that his wife was dead since she’d been suspected of something with the store owner. This woman had been punished for her violation of the rules, this was normal. I didn’t realize that simple gossip based on the neighbors’ assumptions, or lies even, could turn any woman into a charmuta and lead to her death, for the sake of the honor of the others. IT is what is called a crime of honor, Jamirat el Sharaf, and for the men of my region it is not considered a crime.

(Pg 72-74) Faiez lives in the house opposite ours, on the other side of the road. [He] works in the city [and] is all elegance. The first time I saw him I was lucky. He came out in a suit, with beautiful black-and-tan laced shoes, carrying a briefcase, very black hair, very tanned complexion, a proud bearing. My heart beat loudly in my chest and my legs trembled. And I said to myself: I want this man for my husband. I love him. I want him, I want him . . .

But what to do? How could I plead with him to go and beg my father to conclude the marriage? How could I even speak to him first? A girl does not speak first to a man. She is not even supposed to look directly at him. He is inaccessible. Even if this man wants to marry me, it’s not for him to decide it. It’s my father, always him, and he would kill me if he knew I lingered for a second on the road to draw Faiez’s attention. I decided to do everything I could to meet him in secret and speak to him, at the risk of being beaten or stoned to death. I didn’t want to lose all hope of going away with a man, of getting free of my father’s brutality.

(Pg 76-77) The next morning, I pretend to be chasing a goat in order to pass in front of [Faiez’] house. He smiles at me – I know he’s watching me go off toward the fields with the animals. I can’t go any farther in taking the initiative. Now it’s for him to decide how he will arrange to speak to me in secret. He knows where I go and when . . . the next day Faiez appears in front of me. He has followed me discreetly and says hello to me. I am ashamed and I look down at my feet, I twist the fabric of my dress and pull on the buttons of my jacket. I don’t know what to say. He says: “Would you like us to get married together? . . . You’re afraid?”

“Yes, I’m afraid. My father is mean. It’s dangerous for you, too. My father could beat both of us.”

(Pg 78-83) I have never been so happy. To be with him, so close, even for a few minutes. For the first time in my life I am someone because I myself decided to do what I want. I am alive. I’m not obeying my father or anyone else. On the contrary, I’m disobeying. My first real meeting with Faiez, in the field of green wheat, give me an idea of who I am. A woman who is determined to become his wife at any price.

“Do you want me to speak to your father about the marriage?” Faiez comes closer to me, very close. I close my eyes, I’m a little afraid. I feel his hand behind my neck and he kissed me on the mouth. “See you tomorrow. Wait for me, but not on the road, it’s too dangerous. Hide here, in the ditch. I’ll meet you after work.”

And the next day, as I watch him approach my hiding place, my heart is trembling. No one in the house suspects my secret meeting. [But] I’m afraid Faiez wants more than a kiss, and at the same time I want it without really knowing what is waiting for me. I’m afraid that if he goes too far and I push him away, he’ll get angry. I also have confidence in him because he knows very well I can’ let myself be touched before marriage. He knows that I’m not a charmuta. And he has promised me marriage. But I’m afraid all the same, all alone in this field. Hidden in the tall grass.

We sit on the ground. He tries to place his hand on my thigh. I don’t let him do it. He gets annoyed. His expression is mean as he looks at me. “Why don’t you want to? Come on!” I’m so afraid he’ll go away, that he’ll look for somebody else. He is my only hope. So I let him do what he wants. He pushes me into the grass. He knows very well what he’s doing. He says nothing, either before or after. He doesn’t ask me why I’m crying, and I don’t even know why I have so many tears. I didn’t want to. I know nothing about love between a man and a woman, no one has taught me anything about it. I don’t dare look at him, I’m ashamed. I didn’t want to make love with him hidden in a ditch, I wanted what all the girls of my village want. To be married, to have a beautiful dress and go to be in his house. He took advantage of my fear, he knew I would give in to keep him. I begged him not to drop me, to arrange the marriage quickly. A girl who is no longer a virgin, this is too serious, it’s all over for her.

He says: “Now go back, change your clothes, and act like nothing happened.

Especially don’t cry in the house.”

(Pg 85-87) One morning in the stable I suddenly feel very strange. The odor of the manure makes me dizzy. And later as I prepare the meal, the mutton makes me feel ill. I’m nervous, I want to go to sleep or cry for no reason. Every time Faiez comes out of his house he looks somewhere else, makes no sign to me. It’s been a long time, too long, and I don’t know when I last had my period, or when it should arrive. If I’m pregnant my father is going to smother me in the sheepskin blanket. So I hide, I pretend to be fine, but it becomes more and more difficult. Summer begins. This lie can’t go on for long. I am pregnant and it’s been a month since the last time I saw Faiez. (Pg 88-89) I believed him, I wanted so much to believe him. [But] I was so afraid that I picked up a big stone and struck my stomach with it hoping to make myself bleed and put things right. (Pg 93) I have lost hope. It’s over. He’s dropped me. He took advantage of me, it was a fine time for him. Not for me. I’ll never see him again. [and] I can’t ask anyone for help.

(Pg 100-102) The weeks pass. No one questions me, no one wants to know who did this to me, how and why. Even if I accuse Faiez, my father won’t go looking for him to make him marry me. It’s my fault, not his. A man who has taken a girl’s virginity is not guilt, she was willing. And even worse she’s the one who asked for it, who provoked the man because she is a whore without honor. I have no defense. My naivete, my love for him, his promise of marriage, nothing of all that counts for anything. In our culture, a man who has self-respect doesn’t marry the girl he has deflowered. Did he love Me? No. And if I committed a fault, it was believing that I would hold on to him by doing what he wanted.

One evening - a family meeting. I listen behind the wall, terrified. My mother speaks to Hussein, my older sister’s husband: “We can’t ask our son, he won’t be able to do it, he’s too young.”

“I can take care of her. Don’t worry about it. I’ll find a way. You’ll go out. Leave the house, you can’t be there. When you come back, it will be done.”

I hear my sister crying, saying she doesn’t want to hear this and that she wants to go home. I had heard my death sentence with my own ears. Are they really going to do it? Is it just to frighten me? And if they do it, when will it be? How? By cutting off my head? Maybe they’re going to let me have this child and then kill me after. Will they keep the child if it’s a boy?

The next day, I act as though I’ve heard nothing. My mother says to me: “It’s time for you to do the washing, your father and I are going to the city.” I know what is going to happen. They are leaving the house just as they’d told Hussein.

I first go for water from the well at the back of the garden. I arrange the wood for the fire and sit down on a stone while I wait for the water to heat. (PG 105 – 107) Suddenly I hear the door clang. He’s there, my brother-in-law Hussein. He says: “Hi! How goes it? I’m going to take care of you.” That smile – I wasn’t expecting that. “You’ve got a big belly, huh? “ He didn’t say anything more. I kept my head down in shame, a little relieved that he didn’t ask me other questions.

I suddenly felt a cold liquid running over my head and instantly I was on fire. I start to run in the garden, barefoot. I slap my hair, I scream. I feel my dress billow out behind me. . Was my dress on fire too? I know I’m running and I’m on fire and I’m screaming. I must have climbed onto the garden wall to end up in the street. There were women, it seems to me two of them, and they beat on me, I suppose with their scarves. They dragged me to the village fountain and the water hit me suddenly and I screamed in fear. I hear the voices of women wailing over me “The poor thing . . . the poor thing . . “ I’m going to die. That’s good. Maybe I’m already dead. It’s over, finally.

TRANSITION But Souad didn’t die . . . with 3rd degree burns destroying her face and covering most of her body, she survived. And with the help of SURGIR, a Swiss foundation dedicated to working with women who are subjected to criminal traditions, she escaped with her unborn child to tell her story. 30 years after her attempted murder, she explains . . .

SOUAD: (Pg 197) I have met girls who have come from afar, as I did years ago. They are in hiding. A young girl who has no legs: She was attacked by two neighbor men who tied her up and put her in the path of a train. Another whose father and brother tried to murder by stabbing her and throwing her into a garbage bin. Still another whose mother and two brothers threw her out a window. She is paralyzed . . . [But] I have never met any burned women like myself; they haven’t survived. And still I hide, I cannot say my real name, show my face. I can only speak out, it is the only weapon I have.
```

---

## IC-0108: But Also Bring Cheese

- Title: But Also Bring Cheese
- Author (byline): Kate Tellers
- Work: The Moth Presents All These Wonders; Pgs 237-243
- Publisher: Crown/Archetype
- Publication date as stated: March 2017
- Event as filed: Dramatic Interpretation
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

## IC-0109: Cats in the Courtyard - Coral’s Story

- Title: Cats in the Courtyard - Coral’s Story
- Author (byline): Patti Feuereisen (ed)
- Work: Invisible Girls: The Truth About Sexual Abuse, Pg 74+
- Publisher: Seal Press
- Publication date as stated: March 2005
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CORAL
- Teaser before the introduction: Yes
- Spoken words (computed): 2060
- Already set (do not supply): none

### Source block (context only)

```text
Author: Patti Feuereisen (ed)
Book: Invisible Girls: The Truth About Sexual Abuse, Pg 74+
ISBN: 978-1580051354
Publisher: Seal Press
Date (Month/Year): March 2005
```

### Introduction (context only: never use it for content warnings)

```text
Child sexual abuse has only recently been surfacing in Greece as an issue of concern among professionals, researchers and the public, following a long period of denial that continues to exist in many settings. However, it is important to realize that this type of abuse does occur world-wide and is not merely a US aberration. Regardless of the county, the long-term psychological impact on the young women who experience abuse, especially by their fathers, is undeniable.

Cats in the Courtyard - Coral’s Story as edited by Patti Feuereisen
```

### Performance text (classify this)

```text
CORAL: (Pg 74+) My father took away my adolescence. It started in Greece, when I was ten, but the first time he raped me was after we moved to Holland, when I was twelve. From the ages of eleven to eighteen, I was abused by my father sexually on a regular basis . . . whenever he demanded it.

CORAL: My father is a professor. He is egocentric and has a major persecution complex, but he has cultivated a public image of being very intelligent and wise and calm. There was this aura around him, like he was a Zen monk or something.

At home he could not keep up the persona. At home he felt entitled to be moody, controlling, and belligerent. He ruled our house. His thoughts were the right thoughts, and my mother and I had to attend to his every mood and desire. What he said ruled.

My mother was a seamstress. She catered to his every whim. She took care of the house, cooked our meals, woke me up in the morning, and put me to bed. I remember getting a lot of love from her. Unlike my father, she was never smothering, telling me what I could and could not do, and she played with me a lot.

I have a lot of blank spots in my memories of my childhood. From what I have pieced together with the help of therapy, I know that when I was a child I was on my own a lot. I can remember one summer when I was six years old, my parents tied the house key to a string and put it around my neck. I was to entertain myself during the day and return home by evening.

It has taken me years of therapy to realize that my mother was very afraid of life. She thought she’d found in my father a support system; with him she did not have to think on her own. My father mattered more to my mother than I did. She would rush around to get dinner on the table for him every night. She knew that if dinner was not on the table when he expected it, he would go on and on about how hungry he was and how he was a better cook anyway. I learned early on that what he said was not always what he meant. He may have said we did not have to do certain things, but there was never really any choice.

The rule of our house was not to upset Daddy. He had an explosive temper, and at times he would throw fits, screaming and breaking things. My father was a master at manipulating reality. As long as we did what he wanted us to do, the household would run smoothly.

When I was very young, my father would leave for months at a time to attend university lectures in other countries, and my mother and I would bond. I would sleep in the big bed with her, which was a huge treat. When I climbed into her bed I felt very safe and cozy. We would play and eat when we wanted to, travel where and when we wanted to, and just relax.

When I was ten years old, my father started holding me just a little too long when he would hug me. I don’t have any clear memory of being sexualized at ten, but things definitely got uncomfortable. He used to have me sit on his lap a lot. The first time he abused me sexually I was eleven. At least that’s the first time I remember clearly. We were still living in Greece. I remember staring out the window at the garden downstairs when he came up behind me and touched my breasts under my shirt. I was wearing white summer pants and a little red top that I really loved. It had little bows on the side. I was wearing little white shoes with black dots. I even remember the underwear I was wearing.

I loved all animals, and I loved watching the cats in the courtyard as they played. As I stared at the cats, my father French-kissed me. My legs started shaking. I was supposed to go to a piano lesson, but he took me to his bed. I remember shaking all over and just focusing on the thought, “Soon I will be at my piano lesson.” I don’t remember exactly what he said to me, but I know he was telling me what he was doing would feel really good.

I was shaking the whole way to the piano lesson, and when I got there I couldn’t play the music, I was shaking so much.

He raped me for the first time when I was twelve. We were living in Holland by then. My memories of it are like a sped-up film. He started to kiss me and I fought with him. I told him I did not like this; that I was a virgin and wanted to remain one. But he kept insisting that this was what I needed to do. He got angry. He screamed, “Enough of this!” and then stood up and pushed me and said, “Get naked and get in bed, now.” I went into the bathroom and stayed there, then I got into my pajamas and got into my bed. He came and got me and put me in his bed, then climbed in, too. I was wearing my underwear and socks and three T-shirts under my pajamas; he was naked. I kept turning away from him and rolling onto my side.

I don’t remember how one thing led to another, but at some point he took off my clothes, put a condom on, and began raping me. I was screaming and he covered my mouth. At that point I was present (I hadn’t taught myself to leave my body yet), and I was in excruciating pain. Afterward he teased me and laughed at me and asked me why I was making such a fuss.

We hadn’t been in Holland long, and I was having a hard enough time as it was. I did not speak English or Dutch. I had no family, no friends; my mother was traveling a lot; I had no protection or resources. My father could be so persuasive. He said that having sex with me was the natural way of things, and he cited all these examples of animals who are initiated into sex by their fathers. He babbled on about rituals and coming of age. He said that in the Jewish religion there is a ceremony call a bat mitzvah to celebrate the transition from child to woman and that he wanted to initiate me into womanhood.

Thus began my father’s invasion of my body and my soul. Any chance he got, he had intercourse with me. Because my life at home was a living hell, I built an fantasy world, and I had easy access to it. This world had elaborate characters with complicated story lines, in most I was a heroine saving abused orphans. In this other world, I was always strong and invincible. It seems I was always in that world when I was at home.

When I asked him why he was doing this to me, he said, “That’s like putting a plate of spaghetti in front of a hungry man and asking him why he wants to eat it.” It took me a long time to realize how much that line affected me. It must have been my fault; after all, I was the spaghetti. It must have been my fault I started to develop and was getting more attention from males.

He also said one thing that really got to me. He said that mothers know; they just do not discuss it with their daughters. He convinced me that my mother knew and was fine with it. When my mother would leave for her trips and say, “Take care of Daddy,” I began to assume that this was some kind of secret code and she really did know what was happening. Everything felt really crazy and unsafe.

The one time I refused to comply, my mother was away on a five-day trip. I think I was fourteen at the time. I screamed, “No! I will not! Keep away from me!” and ran to my room and locked the door. There was a way to lock my door with a key from the outside, and my father actually locked me in my room and told me I had to stay in there without food or water until I came to my senses. I stayed in my room for at least a day and a half, until I felt faint and had to eat or drink something. Then I gave in and asked him to let me out.

Before I could even eat or shower, he raped me. After that experience, I figured it would be easier just to let it happen. I learned to leave my body and go somewhere else during the rapes. I’d go numb. I was always numb.

I used to think that my mother was not to blame. After all, I never told her about the abuse. But a memory that came back to me during therapy changed my view of her.

When I was about fourteen, my father needed a photo of himself for a magazine cover and decided to have me stand naked in front of him. He would be dressed all in black, his eyes closed. He had my mother take the picture. You could not make out my face, but my body was clearly visible. The idea was that an artist can resist the temptation of the naked woman. Through my therapy I realized that my mother was really a co-conspirator.

My therapy has helped me to realize that I had no options during my childhood and adolescence and that the incest was not my fault. I now understand that my mother was weak and would not protect me. Also, there was no modesty allowed in my home. My parents walked around naked and expected me to do so as well. I was ridiculed by both of them if I expressed a desire to behave modestly. There was not even a door on the bathroom. When I was twelve years old and wanted a bathing suit top, my mother teased me and said that I was to continue to go topless at the beaches.

Even though I’ve been free of my parents for several years now, I still hear my father’s voice inside my head controlling me at times. As the years move on, his voice is quieter and quieter. My therapist assures me that someday it will be so faint I will barely hear it.

Getting some perspective has helped me to begin to forgive myself. I still feel depressed at times. During my adolescence I developed severe headaches and frequent nausea, which I continue to suffer from. Some days I feel worthless. But I realize now that as a child and adolescent I did my best to keep myself alive. My mother was passive and frightened of the world. My father defined her every move. He molded her and tried to mold me, too. But with me he did not succeed.

At the time I was being molested, I thought I was the only one. If I could have read something at the time about sex abuse, if people had talked openly about it, I could have been saved so many years of guilt and shame and secrecy. Each time I talk about my incest, I get rid of some of that shame and guilt. Each person I share with, no matter what their response, takes another piece of the pain away.

It’s taken a while, but I have begun to see things through my own eyes. I have started to hear my own voice. Three years ago, I changed my name so I would no longer have to share a name with my father. I will never go back to Holland, and I will never go back to what my life was. I have choices and freedoms and I accept my incest as something that has happened to me. But it no longer defines who I am.
```

---

## IC-0110: Caught up in the Rapture

- Title: Caught up in the Rapture
- Author (byline): Sheneska Jackson
- Work: Not specified
- Publisher: Simon and Schuster
- Publication date as stated: June 1996
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DAD, BOBBY, JAZMINE
- Teaser before the introduction: Yes
- Spoken words (computed): 837
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
I’m just about sick and tired of all this sneaking around like I’m some two-year old child. I mean, look at me. I’m twenty-six years old and still breaking out in a cold sweat because I’m afraid Daddy won’t let me go out tonight. He’ll probably break out into tone of his holy chants.

DAD: “Oh, Lord, save this child. Make her see the error of her evil ways!” By the time he’s finished, I’ll feel so guilty that I’ll get dressed in one of my little white dresses and follow right behind him to the Holy Sight Baptist Church. Or at least that’s what usually happens, but not tonight. Tonight I’ve got big plans and nothing, not the good Reverend Deems, not even the Almighty Himself is going to stop me. Today Dakota called me up at work and said she had two tickets to Black Tie Records’ annual executive party. If I could just get my tape into the hands of somebody, anybody, at that company, I’d be set.

Okay now, let’s see. I’ve got my hot curlers, my makeup kit, and my good panties: “demon material.” My best friend Dakota says I’m weak when it comes to daddy, but she just doesn’t understand. I envy Dakota, I really do. Dakota’s parents were musicians. They treated the two of us to a concert. I told Daddy we were going to see a young gospel group. He was glad that I was “becoming closer to the Lord.” I got to my seat, the house lights went off, and the crowd could barely contain themselves. A lady behind me began shouting, “Go on girl, sang that song.” Then the man next to her stood up and started hollering too, “Sang it, baby, sang it!” And then it happened. Anita Baker walked into the spotlight, standing less than five foot three, but seeming larger than life. I was in awe. At that moment, I knew what I wanted to do. I wanted to sing. I wanted to get onstage in front of thousands of people and touch them deep down in their souls the way Anita touched me. I wanted to make people yearn, make their hearts bleed, move them, make them feel. That was eight years ago. (to God) I’m still waiting for my dreams to come true, just in case you were wondering! But get this, I got a phone call the day after the executive party.

BOBBY: “I’m Bobby Strong of Black Tie Records, and I’d like to meet with you this afternoon to discuss your future here at Black Tie. I have an opening in my schedule at four o’ clock, and by the way, your friend Colorado was right, your voice is impeccable! Don’t thank me. Thank your friend Colorado.” I wanted to tell him her name was Dakota, but HELL, he could call her Alaska if he wanted to! I quickly got dressed, but before I got out the door, Daddy stood in the doorway glaring at me.

DAD: “I just got back from church and Miss Ola told me her son Oliver saw you at a party last night. Girl, you ought to be shamed.”

JAZMINE: “Just stop it, Daddy. All I did was go out to a little party. What is it? Do you think I’m going to go out one night and never come back? Do you think I’m momma? I’m not momma!”

DAD: “Jazmine, who do you think you’re talking to? Jazmine, don’t you dare walk out that door, girl!”

I kept right on walking. At that moment I felt like the force of God was within me, but that couldn’t be possible, because of the way I had just spoken to Daddy, I knew God wouldn’t want to be with me right now. I got to Black Tie Records . . .

BOBBY: “Now Jazmine, I just want to hear your voice. Give us a little somethin’, somethin’.”

JAZMINE: Okay Mr. Strong (Sings) Ah, ah, ah, ah, ah, ah, caught up in the rapture of love. . .

(Sing for ~20 seconds Check out http://www.youtube.com/watch?v=IUb3HjFEq6Y for the melody)

When I finally opened my eyes:

BOBBY: “Jazmine, it’s only a matter of time before that voice lands you on the Billboards.” I did it. I had finally made my dreams come true, and you know what? I did it all by myself. That night, by the time I reached the steps, Daddy had opened the door and looked out.

DAD: “Come fix you a plate.” I fixed myself a place and sat at the table.

DAD: “You any good?”

JAZMINE: “Yeah.”

DAD: “Better than your momma?”

JAZMINE: “Yeah.” I knew we weren’t talking about voice quality or music arrangement. We were comparing lifestyles. I’m smart enough to know that drugs can’t make me any more artistic than I already am. I’m smarter than Billie Holiday, smarter than Janice Joplin, and yeas, smarter than Momma. Daddy lifted my hands to his face and kissed my palms. I felt closer to him that I ever had before. You see, at that moment, my father wasn’t the Great Reverend Deems, healer of lost souls; he was finally just my Daddy.
```

---

## IC-0111: Chain

- Title: Chain
- Author (byline): Pearl Cleage
- Work: The Best American Short Plays 1999-2000, Pgs 28-52
- Publisher: Applause Theatre & Cinema Book Publishers
- Publication date as stated: Nov 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: ROSA
- Teaser before the introduction: Yes
- Spoken words (computed): 2659
- Already set (do not supply): none

### Source block (context only)

```text
Author: Pearl Cleage
Book: The Best American Short Plays 1999-2000, Pgs 28-52
ISBN: 978-1557834522
Publisher: Applause Theatre & Cinema Book Publishers
Date (Month/Year): Nov 2001
```

### Introduction (context only: never use it for content warnings)

```text
Meet Rosa Jackson a sixteen-year-old crack addict whose parents have decided to take matters into their own hands. Their solution: keep their daughter chained inside their home for seven days. Will this desperate attempt to keep Rosa away from drugs and the violence of their Harlem neighborhood work? How far would you be willing to go to protect your child?

Chain by Pearl Cleage
```

### Performance text (classify this)

```text
(Pgs 28-52) A loud scream. Sounds of scuffling, struggling, trying to escape and being caught. Only one voice is heard, ROSA JENKINS, a 16-year-old crack addict. DAY ONE

ROSA: [Screaming, crying, pleading] What are you doing? No! Stop It!! Don't, Daddy!! Please don't!! Stop it!! Wait, Daddy!! Wait! Don't do it! Please, don't do it! Daddy, Please! Please! Da-a-a-a-a-deeeeee!! [sounds of struggle suddenly stop. A door slams and a deadbolt lock clicks loudly into place. Silence. ROSA is crumpled in the middle of the floor sobbing loudly]

ROSA: Mama? [She listens intently and then speaks tentatively.] Mama? Is that you? [Listens again and then speaks angrily] I hear you out there listening. What kind of mother are you? How can you let him do this to me? You don't love me! You never loved me!! You hate me! You all hate me!! [Crumples again, sobbing. Stops suddenly and sits up. This time her look is more crafty. She is still listening.] Mama? Mama are you still there? I didn't mean it, Mama. You know I didn't mean it. I know. you love me. I love you, Mama. [Listens.] Mama? Talk to me, Mama. Say something. Say anything!! [Listens again.] Well, don't then! I don't care what you do! You can't keep me in here if I don't want to stay! I'll get away just like I always do. You know I can do it, Mama!! And you know I will! How do you like that? [Listens again. Suddenly frightened.] Mama? Please let me out! I'm scared to be in here like this! Please let me out, Mama! I won't tell Daddy, I promise. He'll never know the difference. I won't go nowhere, I swear. I was just kiddin'. You can trust me, Mama. Honest! [No sound at all from outside. She is suddenly enraged.] Open this door and look at me! You scared to see me like this? [Laughs crazily.] Well, that's just too damn bad because you gotta deal with it. Look at me! [ROSA lunges for the door and we see she is chained to the radiator with a long, thick chain -- shackled by her left foot. As she lunges, the chain jerks her back. She yelps in pain and falls down. She grabs the chain and tries to pull it off her leg, but she can't. She goes to the radiator and tries to pull the chain off the radiator, but she can't. She is like a caged animal and growls in a way that expresses wordless rage and frustration. She stands breathlessly looking around.] DAY TWO

ROSA: Damn! [frustrated and angry. She faces the audience and seems to see them for the first time. She is startled, but immediately takes on a craftiness.] Got a match? [holds up a cigarette.] Hey! I'm talking to you! Y'all got a match? [Disgusted at the lack of response.] It ain't no reefer, okay? It's a Winston. Y'all probably don't smoke no way. Right? Lookin’ out for your health. You probably wouldn't give me a damn match if you had it. [A beat] My dad told you not to talk to me, right? Not to listen to anything I said cuz I'm a dope fiend and I might trick you into doing something bad. [Tosses cigarette aside. She moves restlessly around, touching the chain a lot. She is already feeling the effects of being deprived of the drug.]

Think they can keep me chained up in here like some kind of freak. But that's where they wrong. I ain't no dumb dog! I can figure this out. Be back on the street before they get home from work tonight.

I wasted a lot of time yesterday. I mean, when I got home, they was actin’ so glad to see me and now this?!I slept all day Saturday. Next morning ... before they went to work, I came out to tell' em good-by and they sittin at the table talkin real quiet and they stop real fast when I come in. Then they look at each other and my dad pulls out a chair for me. They was lookin so serious, I thought they was gettin' ready to send me back to rehab and then my dad goes to the closet and pulls out this big bag and comes over and sits down beside me and hugs me and starts talking about how happy they were when I was first born and how I'll always be their daughter and they love me so much. Then I looked at Mama and she's cryin'. Mama ain't cried when I went to rehab since I was thirteen, so I know this is serious. I know this sounds crazy, but I thought they was gonna kill me. I could tell it was something heavy in the bag and I thought maybe Daddy had, like a sledgehammer, or something and they was gonna beat me to death and then put me in a bag and drop me in the river. [Laughs.] Crazy, right? Then Daddy takes out this big chain and I freaked.

Help! [She waits. Listens. Then louder.] Help!! [Listening.] Help, they're killin me! [Listens -- Thinks for a minute.] Fire! [Listens. Still nothing.] I could burn up and nobody would even know. I ought to have them arrested for doing this to me. [A beat.]

The first day we moved on this block, I was sittin on the stoop out front while Daddy moved our stuff inside and I was looking at this guy staggerin down the street, bumpin into people. I had never seen anybody that drunk before, so I was starin’ at him. He hollered right in my face. I like died! New York is so different from Alabama it might as well be on another planet. When we got here, I was freaked out. My parents moved to New York so I could go to good schools and have better opportunities. Yeah, right. Opportunities to do what? I ain't complainin’ though. It was exciting. I had never seen kids my age do what these New York *kids* were doing. They did everything. I mean eleven, twelve year old kids drinkin and smokin like they was grown already. It was like nobody had control of them or somethin. I didn't do none of that s*** for a long time. I was real goody goody. It was kind of a drag at first, but then I met Jesus (pronounced Hey-sus) and he hipped me to a lot about living in New York. Stuff I really needed to know, right? And plus, he was real fine and real cool and a Puerto Rican. Wadn't one Puerto Rican in Tuskegee, Alabama. Period. He thought I was Puerto Rican before he met me because my name was Rosa and someone told him I had a accent. He thought they meant a Spanish accent, but they was talkin about a Alabama accent. He thought that was real funny, too. I been knowin’ Jesus since I was eleven years old.

Jesus mama had a boyfriend, right? And he was a crackhead and she hid his *stash* from him. Call herself tryin to help him get off it. Well, she wouldn't tell him where it was, so he shot her right there in their apartment, went through all her *stuff* until he found it, and was sittin there smokin it when Jesus came home. Jesus mama layin right on the floor in the next room, dead. Jesus say he didn't even tell him she was dead. He just looked up when he walked in and said, "Your mama in the kitchen." When Jesus came back out, he was gone. [A beat.]

So after they buried her, Jesus said he started thinkin about that crackhead just sittin there smokin while his mama layin in the next room dead and he said he just thought, If it’s that good, let me have it. I told him he was just thinkin that way cause he felt bad about his mom but he said he wadn't askin’ me if he should do it. He was just tellin’ me. He didn't act like no addict either. He don't act like one now, unless he can't get it, then he start actin weird. Talkin crazy When Jesus need to get high, he talk about killin people a lot. He ain't never killed nobody, but he talk about it a lot when he can't get high. I know it's because of his mama, so I try to change the subject so he won't go off on it.

My Dad wanted to kill Jesus when he found out I was smokin crack, but I won't tell him where Jesus live. He act like it's Jesus' fault I'm smokin it. [Laughs.] I told you my dad be trippin! He never did like me to be around Jesus after what happen to Jesus mom.

DAY THREE

ROSA: [A beat.] Last night when they got home, my Mom was still cryin. They had both worked double shift, so it was late and they was worried about how I was gonna be when they got here. I started to layout like I was dead so when they opened the door they'd see me layin there with my eyes open..But I was just sittin here when they busted in all hyper. My Mom started huggin me and my Dad was lookin real relieved, right? They were scared I had figured a way to get out and wouldn't be here. They did unchain me while they were here, but then they followed me around. My mom even went in the bathroom with me, which was embarrassing. Then when we all got ready to go to bed, Daddy got this really sad look on his face, and put this chain right back on me like "this is hurting me more than it's hurting you." I hate when people say that to their kids. [Laughs.] I used to try to scream real loud when he would beat me so he'd feel bad and quit. I didn't even get my first whippin til I was thirteen. I kept runnin away from rehab and he didn't know what else to do. Me neither, so we lookin at each other like, well? And I'm thinkin, do somethin if you gonna do somethin or leave me alone so I can get high! So he took off his belt and hit me a couple of times, but it wadn't bad or nothin. My dad don't have the heart for that. DAY FOUR

ROSA: My mom keeps tellin me to just take it one day at a time like they tell you in rehab. This is like a minute by minute trip, right? I want to get high so bad ... damn! My fingernails wanna get high. "One day at a time." [In frustration, she begins to pull and tug at the chain in a rage.] I'm not gonna make it. I'm gonna die all by myself. They're killin me. They're killin me. [A beat, then trying to calm herself] But it's gonna be okay. I just gotta hang in there til I'm eighteen, then they got no power over me no more. Jesus say when I get eighteen; I should move in wit him since he got plenty of room. I'm down wit it. I know Jesus dig me and he always got enough rock for us to get high. [A beat, then ROSA yells several times in loud succession in complete frustration.] I just wanna get high, you understand? I just need to get high. I need to get high! DAY FIVE

ROSA: You know what’s funny, I was almost glad to see my daddy when he came to get me. They told him if he didn't pay the hundred dollars owed them they'd blow my brains out right in front of him. My daddy just stood there for a minute lookin at that *guy* holdin his 9 millimeter against my head and I'm thinking, my daddy ain't got that kinda money! I'm dead! And then he reached in his pocket and took out a roll a money and handed it to the guy. He counted it right in front of my daddy and it was a hundred dollars exactly. Then he told my daddy to get his little crack addict outta his place and pushed me so hard I fell against his chest. My daddy didn't even look at me. He took off his jacket and put it around my shoulders and we walked the three blocks home with him holdin my arm like you do a little kid when they been bad. When we got home, my moms was there and she started cryin and holdin my face up so she could look at me. So I'm standin there and I catch a eye-ful of my pops sittin at the table and tears just runnin down his face. He ain't cryin or hollerin or nothin. He just sittin there lookin at me. That hurt me worse than anything. I never seen my daddy cry in my life. Never, I seen him mad plenty of times, but he never cried. He didn't cry when his momma died. Took the phone call, drove down south and buried her, came back and never broke. So I felt real bad when I saw him cryin over me. I love my daddy ... So I went over and stood in front of him and I said, don't worry about me, daddy. I'm okay. And he just looked at me and tears runnin all down his chin and started sayin my name over and over and over like he wasn't sure it was even me: Rosa, Rosa, Rosa! DAY SIX

ROSA: [She paces, but slowly -- thinking.] My daddy say I been doin so good, he ask me was I worried about the street takin me back if he take the chain offa me. He sound so serious when he say that, but to me, he just be trippin. Like the street some kind of weird, scary thing waitin for you. So I told him no. I wasn't worried about the street takin me back. And he hug me and tell me there is nothin out there for me. I say, I know that's right. My pops told me I should pray instead of gettin high. No, He really did tell me that. I wish I believe in God, but I don't. It take time, my dad tell me. You have to get to know him just like any good friend. That's what he said. [A beat.] My daddy told me only God stronger than crack. I tell him this chain been doin a pretty good job. I was just kiddin, but I think it made him feel bad cause his face got all sad. [A beat.] He told me he knew I was a good girl and he trusted me. I wanted to say, hey, man! This is Harlem! Trust ain't in it! [A beat.] I don't trust nobody. [She looks around.] At least in here, ain't nobody *messin’* with me. I got food. I got a bathroom, so how bad can it be? DAY SEVEN [ROSA is rubbing her ankle distractedly and thinking. The chain is no longer on but she is still limping slightly. She speaks slowly and fiercely to herself]

ROSA: Okay, look. This is a prayer, okay? [A beat.] I can't do that s***. [She is paces. She goes to the closet, slowly reaches in and gets the bag her dad had the chain in. She takes it out, handling it gingerly. There is both resignation and comfort in the chain. She places the shackle around her wrist like a bracelet. She takes it off but not away. She realizes what she is considering and the thought horrifies her. She looks at the chain for a beat and then reaches toward it again.]
```

---

## IC-0112: Children of a Lesser God

- Title: Children of a Lesser God
- Author (byline): Mark Medoff
- Work: Not specified
- Publisher: Dramatists Play Service, Inc.
- Publication date as stated: Jan 1998
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: NOTE 2, SARAH
- Teaser before the introduction: Yes
- Spoken words (computed): 1209
- Already set (do not supply): none

### Source block (context only)

```text
Author: Mark Medoff
ISBN: 978-0822202035
Publisher: Dramatists Play Service, Inc.
Date (Month/Year): Jan 1998
```

### Introduction (context only: never use it for content warnings)

```text
"The Sounds of Silence." By Simon and Garfunkel relates the beauty of silence. But have we ever really taken it seriously - the sounds of silence? (mouth the following line with no sound)
```

### Performance text (classify this)

```text
NOTE: This selection should be both signed using ASL and spoken. For an example of the spoken word of the deaf, check out the video at this link: http://www.youtube.com/watch?v=uKKpjvPd6Xo The following ALS speech, translated into standard English would have SARAH speaking . . . “I have nothing; no hearing, no speech, no intelligence, no language. I have only you. I don’t need you. I have me alone. I don’t want anything. I don’t need what you want to give me. My language is just as good as yours”

NOTE 2: The remainder of the selection is written in standard English, but would need to be translated into ASL for the performance enhancement.

SARAH: (Signing) Me have nothing. Me defy. Speech inept. Intelligence – tiny blockhead. English – blow away. Left one you (point to audience) Depend – no. Think myself enough. What do I want? Nothing. I don’t need what you want to give me. I have a language that’s just as good as yours!

Can you even imagine what it is like to live in a world of total silence? Did you get that? I just said: Can you even imagine what it is like to live in a world of total silence. You may have thought I had forgotten my lines, or maybe you were trying to read my lips. Welcome to the world of Sarah Norman, now in her mid-twenties who has been deaf from birth. Sarah's mother -- ashamed of her deafness -- pushed her aside and ignored her. Until she was 12, doctors and her own parents believed Sarah to be mentally handicapped. At a loss for how to cope with their broken child, her father left the family and Sarah’s mother placed Sarah in a state-run institution for the deaf. But Sarah is far from mentally handicapped – she is brilliant and if you will come with me into Sarah’s silent world, she will tell you . . . no . . . show you how it feels. Children of a Lesser God by Mark Medoff,

SARAH: I have more than enough communication skills. You don't. They never did. They? Who's they? - Hearing boys. They could never be bothered learning my language. No - that was too difficult. I was always expected to learn to speak. The boys who did try to communicate with me got about as far as: How are you, I am fine. (Pause) At first I let them have me because they would. Sex was something I could do as well as hearing girls. Better! It got to be that when I went home, the boys would be lined up on a waiting list my sister kept for me. Most of them didn't even take me for a Coke first. No introductions. No conversations. We just went straight to a dark place. But I liked that communication. I loved it. It made me feel a lot better than this kind of talk you make. (Pause) I never hurt from other people. What if [I] admitted that I do hurt? I would shrivel up and blow away.

[You see] I live in a place you can't enter. It's out of your reach. Deafness isn't the opposite of hearing, as you think. It's a silence full of sound. The sound of spring breaking up through the death of winter. My secret. No hearing person has ever gotten in here to find out . . . No person, period.

[You know what I want?] I want to teach in a deaf school . . . . a house . . . a car. Plant a garden and . . . So much! A microwave oven! And children! Deaf children. My father left us because I'm deaf. [I want to go] on with my schooling and [get] a teaching certificate. (with emphasis) I know it's possible. [But] I feel split down the middle, caught between two worlds - deaf world here, (motion to yourself), hearing world there (motion to the audience). I hope I'm strong enough to juggle both. I'm too old to learn to speak and lip read well.

(“hears” music and responds by swaying her body, snapping her fingers) Listen to your music. I can enjoy your music. Really! The vibrations don't have a sound but they do have a feel. Fast. Slow. Very intense. Not so intense. And when I see people dancing, I feel still more. I can feel it . . . . Don't be sorry. I could never know what music sounds like. But I can understand what it means to you. And that makes me very happy. Ssshh. (responds negatively as the “music” shifts to organ music) I don't like this kind of music . . . organ music (makes a face). [You want to know why?]

When we were kids in school here, on Sunday they made us go to church. They played an organ fiercely. [My friend] cried because he could hear just enough for it to hurt his ears. The kids with hearing aids were forbidden to turn them off. We were told it was the voice of God and should hurt. They said we should love God for being so fierce and demanding. When [my friend] was nine and I was eleven, we started hiding in the trees behind the duck pond on Sunday. We pretended we were soldiers and threw dirt clods at the church and made sounds like hand grenades. (Laugh and pretend to make grenade explosions with your hands in the air).

(Long pause) I haven't left the deaf world. I haven't done anything yet. I don't know which role I’m supposed to play. [Some people] treat me like an idiot. Let me be a person! (emphatic, yet pleading). You want me to be a deaf person so you can change me into a hearing person. [Or you] want me to hate being deaf so all the hearing people will feel sorry for me. And I just want to be me! Don't pity me!

For all my life I have been the creation of other people. The first thing I was ever able to understand was that everyone was supposed to hear but I couldn't and that was bad. Then they told me everyone was supposed to be smart but I was dumb. Then they said, oh no, I wasn't permanently dumb, only temporarily, but to be smart I had to become an imitation of the people who had from birth everything a person has to have to be good: ears that hear, mouth that speaks, eyes that read, brain that understands. Well, my brain understands a lot, and my eyes are my ears; and my hands are my voice; and my language, my speech, my ability to communicate is as great as yours. Greater, maybe, because I can communicate to you in one image an idea more complex than you can speak to each other in fifty words. For example, the sign "to connect," is a simple sign-- but it means so much more when it is moved between us like this. Now it means to be joined in a shared relationship, to be individual yet as one. A whole concept just like that. Well, I want to be joined to other people, but for all my life people have spoken for me. She says; she means; she wants. As if there were no I. As if there were no one in here (motion to chest or head) who could understand. Until you let me be an individual, an I, just as you are, you will never truly be able to come inside my silence and know me. And until you can do that, I will never let myself know you. Until that time, we cannot be joined. We cannot share a relationship. (Long pause).

Me have nothing. Me deafy. Speech inept. Intelligence --tiny blockhead. English -- blow away. Left one you. Depend -- no. Think myself enough. Join. Unjoined.

You didn’t hear a word I said. (at first sadly, then with anger) You want me to be like you. How do you like my voice? Am I beautiful? Am I what you want me to be? What about me? What I want? What I want? (painfully and heartfelt). To say I hurt and know I won’t shrivel up and blow away . . . . to meet in another place; not in silence or in sound, but somewhere else.
```

---

## IC-0113: A Child’s Book of Sickness and Death

- Title: A Child’s Book of Sickness and Death
- Author (byline): Chris Adrian
- Work: A Better Angel: Stories
- Publisher: Farrar, Straus and Giroux
- Publication date as stated: Aug 2008
- Event as filed: Dramatic Interpretation
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

(Pg 174) I am waiting for my PICC- you must have central access to go back on the sauce-when a Child Life person comes rapping at my door. You can always tell when it’s them because they knock so politely, and because they call out so politely: “May I come in? (Pg 175) We are collaborating with the children. A collaboration of poetry and prose!”

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

## IC-0114: Choosing Hope

- Title: Choosing Hope
- Author (byline): Kaitlin Roig-Debellis and Robin Fisher
- Work: Not specified
- Publisher: GP Putnam's Sons
- Publication date as stated: Oct 2015
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: KAITLIN, CHILDREN, LITTLE GIRL, CHILD 1, CHILD 2, CHILD 3, CHILD 4, CHILD 5, CHILD 6, CHILD 7, CHILD 8, CHILD 9, VOICE 1, CHILD 10, VOICE 2
- Teaser before the introduction: Yes
- Spoken words (computed): 2329
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

First comes the initial blast of gunfire, then the sound of shattering glass. The hair on my arms stands up. I know right away what I am hearing. Columbine is happening in the place we called Pleasantville. How can it be? Someone with a weapon is shooting their way into our perfect school. My classroom is the first one in the building. We are in grave danger -- sitting targets. I jump up, run to the door, pull it closed, and switch off the lights. I can't lock the door. My keys are clear across the room, on top of my desk and a locked door is no match for a magazine of bullets. If we're going to live, we have to find a hiding place. Fast. I look around the classroom. My students don't seem to understand what is happening. One, the little girl I call our fashionista, because she wears things like leopard prints and leggings, stands there smiling. I can't tell if she is somehow oblivious to the sounds or scared frozen. The windows don't open wide enough for a first-grader to climb through, and who knows what or who is waiting outside? Evil is coming for us and there's nowhere to go.

Where can we hide? Where can we hide? There's only one place. The bathroom-a tiny, tiny first grade-sized lavatory with only a toilet and a toilet-paper dispenser inside. Its dimensions are about the size of two first-grade desks pushed together. Maybe three feet by four feet. There is so little space that the sink is on the outside, in the classroom. I have never even been inside the bathroom before. An adult wouldn't fit comfortably. How in God's name will I get sixteen of us in there? It is our only chance. The impossible will have to become possible. (to students) Into the bathroom! Now!

CHILD 1: In there? How?

CHILD 2: Why?

CHILD 3: What do you mean, Miss Roig?"

KAITLIN: (to students) Bathroom! Now! (to audience) They understand that the teacher means business. I rush them toward the back of the classroom. Shots are being fired outside our classroom door. There's no time. "Hurry!" I say, pushing them into the tiny space. ."Hurry!" But I know that no matter how quickly my students respond, it will still take two or three minutes to get everyone inside, minutes I feel sure we don't have.

We all push into the bathroom, and when there isn't a millimeter of space left, I begin lifting my students and piling them inside. I place one student, then two, then three on top of the toilet and hoist up my littlest girl and sit her on the toilet-paper dispenser. We are all crushed together with not even enough room left to take a deep breath. I reach out to pull the door closed, but just before I do, I reach outside for a large storage cabinet on wheels that is nearby and pull it as close as I can to the front of the bathroom door, hoping that maybe it will conceal it.

My heart pounds against my chest, but I cannot afford to lose my composure, not if we are to have any chance of getting out of this alive. First-graders model their teacher's behavior. If I panic, they'll all panic, and we'll be dead. (to students) Now, we have to be absolutely quiet. We can't say a word.

Someone shouts, "Shooter! Stay put!" Is that our principal? The school nurse? Another teacher? The sounds are too muffled to tell. Then, ear-splitting, rapid-fire shots, like a machine gun -- di-di-di-di-di-di-di-di-di-di-di-di -- over and over and over. My students stay perfectly quiet. They understand that someone very bad is searching for us and in order for us not to be discovered they stay perfectly quiet. In our silence, we hear voices -- muffled voices. People are pleading for their lives. "No! Please, no! Please! No!" With the inescapable sounds of carnage happening all around us, my little ones are feeling desperate.

CHILD 4: (whispering) What is happening?"

KAITLIN: My fashionista begins to cry. I cup her face in my hands and look into her teary eyes. (to student) We're going to be okay. (to audience) The boy who straddles the top of the toilet is shaking so hard that he accidently flushes. Once, then again. We all hold our breath. Shhhhhhhhhh!!!!! Did the shooter hear? I look at the boy and his face says it all. I'm scared and I'm sorry and I don't know what to do.

CHILD 5: (whispering) Miss Roig, I don't want to die today.

CHILD 6: (fighting tears) I just want my mom.

CHILD 7: (whispering) I don't want to die before Christmas.

CHILD 8: (whispering) I'll lead the way! I know karate.

KAITLIN: (to audience) Hadn't it been only moments ago that he told us the story of finding a dollar under his pillow for his two front teeth? (to students, gently) No. There are bad guys out there and we need to wait for the good guys to come. It's going to be okay. We're going to be okay . . . I need you to know that I love you all very much. (to audience) In comforting them, I also brought comfort to myself. (to students) Anyone who believes in the power of prayer needs to pray right now.

(close eyes and pray) Suggested “prayer” – Not in the original text. You may insert your own prayer here if desired or simply pray in silence for a few beats. Check the rules governing your tournament regarding addition of “transition/additional” words. [(softly) God, we are scared. But You are there. Even when we don’t know what to say, we can just pray, “Help me, God, I’m so scared.” Thank You for this day, even though it’s not been the best day. Help us. Help us to see and remember all of the good things You have blessed our lives with. In Jesus’ Name, Amen.]

It’s been quiet for a while now. Eerily quiet. I wonder if the gunman is lurking outside our door, waiting for us to feel safe enough to come out of the bathroom and fall into his trap. If the good guys were coming, they would have been here by now, wouldn't they? Why is it so deathly quiet? I think about my students' parents and the unimaginable grief they will suffer because I was powerless to save their children. My worst fear is that I will see my class murdered before I die and I won't be able to stop it. All we can do now is wait. . . An eternity passes. Some of my kids are becoming impatient.

CHILD 9: I'm hot, Miss Roig. Can we please get out?"

KAITLIN: Several say they need to go to the bathroom. For the most part, though, they are quite content to be quiet if it means the bad guy can't find us. I wonder what is happening outside. Then, from the other side of the wall, come the voices of people who are barking orders. I hear them clearly.

VOICE 1: Don't look up. Don’t open your eyes. Walk Quickly.

KAITLIN: Oh, God. Is there more than one shooter? Are they kidnapping people? What is going to happen to us? My heart races in my chest. My kids look up at me. (to students) Shhhhhhhh. (to audience) We have been in the bathroom for a very long time. At least forty-five minutes.

A knock comes at the door and we all stiffen with fear. (put index finger to lips as a signal to the children) I fear that if we make any noise, the shooter will realize that the teacher has hidden her whole class in here. (to student in a whisper) Ask who's there. (to audience) I don't want the shooter to know that there are sixteen terrified people huddled together behind the bathroom door.

CHILD 10: (voice quivering) Who is it?"

VOICE 2: (a kind voice) Hey, little fella. We're here to help you. Unlock the door.

KAITLIN: No way! Why in the world would I trust the words of a faceless stranger? No way am I going to risk opening the door for a killer. (to the person outside the door) If you really are the police, I need your badge. (to audience) Seconds pass. A badge is slipped under the door. I pick it up and examine it. It looks fake, like a play badge that one of my students might wear. I desperately want for it to be real, but I'm not convinced. (to person outside the door) This doesn't look real. I don't believe you. (to audience) I look around at my kids and I know they are thinking what· I am. Please let this be the good guys. One little girl is choking back tears. I take her face in my hands and smile. If she starts to cry, the others will cry. I can't let that happen, not until I find out who is on the other side of the door. (to person outside the door) If you are the police and you're here to help us, then you should have the key to this door. Or you should be able to get it. (to audience) A few more minutes pass before I hear the rattle of keys. I hear the scraping sound of a key going into the lock. It doesn't work. An-other key, another failed attempt. Five. . . six . . . seven tries. My stomach churns with each twist of the lock. My students' eyes are wide.

The tenth key works. The knob turns and the door pushes in. I see an army of uniforms-people dressed in black and wearing helmets and carrying big guns, peering in at us. A SWAT team is in our classroom. The good guys are here. They pull us out of the bathroom, at first, one by one, until there is enough room for us to move on our own. Our heroes lead us out of the classroom and guide us in the opposite direction of the bodies in the hallway and the blood-stained floor. I grab the hands of the two students closest to me and follow the instructions to "Go. Fast." We rush the students down the hall and out of the building. "Where is the bad guy?" I ask as we make our way to the firehouse. Is he still lurking here, somewhere, ready to hurt us? They assure me that we are safe. I say "Thank you" over and over . . .

Thank you for finding us in that tiny bathroom . . . Thank you for being the good guys . . . Thank you for saving our lives.
```

---

## IC-0115: Claire

- Title: Claire
- Author (byline): John Kuntz
- Work: Boston Theater Marathon of Ten-Minute Plays, Volume 2, pg 113
- Publisher: Baker's Plays
- Publication date as stated: Jan 2001
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: CLAIRE
- Teaser before the introduction: Yes
- Spoken words (computed): 1759
- Already set (do not supply): none

### Source block (context only)

```text
Author: John Kuntz
Book: Boston Theater Marathon of Ten-Minute Plays, Volume 2, pg 113
ISBN: 978-0874401547
Publisher: Baker's Plays
Date (Month/Year): Jan 2001
```

### Introduction (context only: never use it for content warnings)

```text
Claire Wilson had reached the pinnacle of success: a lead role in a Broadway production. The roar of the crowd, the applause, the standing ovations. But there’s a darker side to the profession. Acting, while it may be your passion, is an intense career path, with rejections, unpredictable work schedules, strained relationships, and a constant fear that your time in the spotlight is over. How do you cope with the loss of the very profession that has defined your life?

Claire by John Kuntz
```

### Performance text (classify this)

```text
Lights up on Claire, an attractive, rather regal actress. Her age is impossible to determine, but she’s been around for a while. Music is blaring and Claire appears to be humming loudly and conducting the music, sans baton. She begins to talk to someone who has just entered the room but does not stop her “conducting” (Song is Bizet - L'Arlesienne Suite No. 2: Farandole*)

CLAIRE: (Pg 113+) Please don’t turn the music off, it’s almost done. No, I’m afraid I can’t stop now. I can’t stop once it’s started, I have to wait until it’s finished. Just a few more seconds. I’m almost done. (She continues. The music ends. Clair takes a moment to catch her breath. She seems almost transported and needs to remember where she is. She addresses the audience) Well. Quite a show, huh? No applause? (pause) No, I don’t want you to applaud. It was a joke (pause) You’re the first person ever to see me do that. And it was absolutely free. Most theatre tickets cost at least 60 dollars these days. But this is actually costing me money, isn’t it? So, what’s your name? Marcia? Well, that’s a nice, sensible name. Marcia (She tries saying it in different moods and tones) Marcia . . . Marcia . . . Marcia . . . Marcia . . . Sorry, just trying it on for size. So, Marcia, nice to meet you. I’m Claire.

CLAIRE: Theatre is a dying art form, did you know that? At least that’s what my agent says. (pause) My first therapist actually said that I was pursuing a career in theatre for all the wrong reasons. He said I wanted to be on stage because I didn’t receive enough attention as a child and this was how I was trying to fulfill this emotional need in my adult life. He said I was completely out of touch with some of the more important emotions like anger and fear and that I was using the characters I play on stage to feel them for me. Because it was safer that way. But I ignored him and kept going and now here I am. A retreat. That’s what my agent likes to call it. A “retreat.” (AS HER AGENT) Oh, Claire is resting. It was a grueling run in New York and she’s having a nice little vacation. (to audience) Marty has always been marvelous at putting a fresh, positive spin on things. (pause)

You know what I love about this place? I love that you actually have a theater here. Right on the grounds of the hospital. Psychodrama. Theatre as therapy. All the kooks putting on a play so they can act out what’s wrong with their lives and reach some kind of understanding about themselves. I find it extremely ironic, don’t you? I mean acting is what got me into this snake pit in the first place and now it’s supposed to get me out? I find that hilarious (pause) I could be acting right now for all you know. I mean, who’s to say that I haven’t planned out everything and make it seem like it’s all just floating to the top of my head? Pause. Pause. Pause. Was that spontaneous? OR was it rehearsed? Studied and blocked. Act 5 Scene 2. (pause) You get to a point, I mean I do, I get to a point where . . . you don’t know what’s real anymore. What’s honest. You start to become obsessed with it. (She turns on the music again and begins to wave her arms in the air, as if conducting the music)

Do you know why I do this? I was auditioning for a very important role. It was the role that would bring me to the next level of my career. I was 23. A leading role -- I wanted that part so badly. And when they called me to say that it was mine, that they wanted me . . . I heard this song playing. I think I’ll remember that moment, that feeling of triumph and satisfaction for the rest of my life. This is my lucky song . . . I would play it every time I had an important audition. Right before I left the house. To inspire me . . . And when I came back from the audition, I played it again. For good luck. It was kind of a ritual. That was how it started . . . (She abruptly shuts off the music) You have to understand that I’m working in a profession where luck plays a major part, Marcia. And finding some way to control your fortune is a very, very seductive idea. You’re going to need luck to get the audition, and the callback, and then the part. And once you have that part, you’re going to need luck to keep it. You need to pray every night that you’ll remember your lines, remember your blocking, that the lead won’t upstage you, that your understudy won’t plot your violent murder, that the audience won’t laugh during your death scene, or worse walk out, that the reviews are kind, that your voice won’t give out, that the play won’t close after two weeks, and when it does, you’re going to need luck to start the whole thing all over again. (pause)

You know, I don’t really belong here. I’m fine. In fact, I can’t really stay . . . I need to be back in town soon. I’m playing Truly Scrumptious in “Chitty Chitty Bang Bang.” It’s the stage version of the movie. I know it sounds hideous and it is, but Marty says it’s a sure-fire hit, and I’m going to need a hit after all this. Do you know that when I tell some people that I’m an actress they immediately ask what movies I’ve done. And when I tell them I’m a stage actress they sort of smile, as if to say: “Oh, what a quaint hobby.” I would like to make one thing very clear: great acting takes place in the theatre and only the theatre. Because it’s alive. It’s living. It’s happening right in front of you. If something happens or goes wrong during the show then it becomes a part of the show, no two of which are ever the same. You can’t stop and start over again. That moment is gone. BANG! Here comes another one! It’s happening right in front of you! BANG! And other one! BANG! And another! BANG! BANG! BANG! That is theatre! It’s living! It’s breathing! It’s the Super bowl! It’s the Sermon on the Mount! It’s Jazz! It’s bongo beats and café au lait in a smoky room filled with shadowy smiling strangers! It’s the birth of your child! It’s yin! It’s yang! It’s playing poker with God! (pause) And so much more. I don’t want to insult the experience by trying to describe it but there you go. It’s an addicting thing. You can’t get enough of it. (pause)

So, listen, I suppose you want to hear the whole sordid tale of why I’m here so I might as well tell you so I can get the hell out. The whole thing was an accident. I didn’t have a nervous breakdown, I’m fine. The show I had just worked on for God knows how long . . . It was bad luck from the beginning: the wrong director, the wrong theatre, the wrong cast . . . The closer we got to opening night the more I played my lucky song. In the morning before I went to rehearsal . . . at night when I got back, over and over. And soon that wasn’t enough. I started to play it in my dressing room during breaks, softly so no one would hear, the door closed. On opening night, half the audience left before Act II and I suddenly realized that just playing the song wasn’t enough. I needed to do something to the music. Control it. (She begins to wave her arms in the air) I started to conduct, waving my hands, easing the music out. Everything would fall into place if I just did it right.

The reviews came out, the worst I’ve ever seen for any play in my career . . . “Claire Wilson is a vapid marionette on stage” – New York Times . . . “Claire Wilson is in the twilight of her career . . . not one honest moment . . . – The Village Voice . . . “Claire Wilson is the worst dressed actress on Broadway” – People Magazine . . . “Clair Wilson has a big butt” – The National Inquirer . . .

The male lead was fired after 5 performances . . . The stage manager quit . . . During the curtain call of a matinee performance the audience actually booed. I’ve never been booed at in my life . . . I started listening to [my song] in the wings right before I went on stage, waving my arms and whirling about, the rest of the cast thought I was crazy, I thought I was crazy and I took small comfort in the notion that I couldn’t be crazy if I knew what I was doing was crazy because a crazy person wouldn’t know that.

And then Marty called me one afternoon. The show was closing. Last nights’ performance for 20 people would be the last. I hung up the phone and just laid there on my bed. I couldn’t move. I must have fallen asleep because when I opened my eyes everything was dark. I turned on a light and went over to the mirror. I know how this sounds but I just wanted to look to make sure it was still there . . . The mirror in my bedroom was this large oval full-length one on a stand. The mirror was on hinges to you could spin it around. And I started to spin the mirror like a wheel, faster and faster, until it didn’t look like a mirror anymore, just this round motion and flashes of light, and I could see my reflection in between the flashes, and then, and I don’t know why I did this but. . . I walked into it. As if it were a door, or space . . . I walked into it . . . and the mirror came crashing down and hit me and shattered. (pause)

I saw, felt, fragments of the mirror flying around me . . . and each chard held a reflection of me . . . but it wasn’t me . . . it was every character I had ever lived, every person I had ever turned myself into in the last 20 years . . . They flew all around me and then disappeared . . . (pause) I don’t remember anything else . . . I woke up in the hospital, and Marty said I had tried to kill myself which is ridiculous. I’ve never had a suicidal thought in my life . . . It was an accident . . . (She looks at her wrists)

So that’s it. Are we done? Well, when is our next session? Tomorrow at 3. Well, I’ll be here. I’m not going anywhere, evidently. (Marcia leaves; Clair puts a new cassette in the stereo and speaks to herself) Marty sent me all the music for Chitty Chitty Bang Bang so I can work on my songs while I’m here. I don’t normally do musicals but.

(“Doll on a Music Box” from Chitty Chitty Bang Bang plays. Claire sings sadly and
begins to conduct . . .)
What do you see
You people gazing at me
You see a doll on a music box
That's wound by a key
You cannot see
How much I long to be free
Turning around on this music box
That's wound by a key
```

---

## IC-0116: Class Act

- Title: Class Act
- Author (byline): Michael Elkin
- Work: Voices from Ariel
- Publisher: Dramatic Publishing
- Publication date as stated: 1999
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SARA
- Teaser before the introduction: Yes
- Spoken words (computed): 1760
- Already set (do not supply): none

### Source block (context only)

```text
Author: Michael Elkin
Book: Voices from Ariel
ISBN: 0871298953
Publisher: Dramatic Publishing
Date(Month/Year): 1999
```

### Introduction (context only: never use it for content warnings)

```text
Widowhood has become a new stage of an older woman's life. Almost half of women over age 65 are widows, according to the U.S. Census Bureau. In fact, it is widows who have set the example for how to remain active and stay involved–despite the crushing losses that come with old age. When you no longer can live as a wife, then you have to figure out who you are as a woman.

When your spouse dies, your world changes. You are in mourning—feeling grief and sorrow at the loss. You may feel numb, shocked, and fearful.. At some point, you may even feel angry at your spouse for leaving you. All these feelings are normal. There are no rules about how you should feel. There is no right or wrong way to mourn.

Class Act by Michael El kin
```

### Performance text (classify this)

```text
Setting: A school registration booth in a big city.

SARA is examining an unseen schedule posted on a wall, squinting and trying to make sense of it.

SARA: Does that say two o’clock . . . excuse me, miss, does that say, Tuesday, two o’clock? (Ponders the response) You only have volleyball Tuesday at two? (Grimaces) No, it’s not a problem It’s just I get my nails done at one. You couldn’t move the class to three? (Under her breath.) I don’t know how you expect me to play volleyball with wet nails. (Turns head.) Badminton? Please, don’t insult me. Badminton is not “in” this year. It’s like playing mahjongg with old tiles You just don’t do it. (Annoyed.) Audit? You want me to audit volleyball? I should sit and watch from the corner? Please, at my age I do enough sitting and watching. I don’t have to go to school to be a bump on a log. I can do that on my own.

(Checks schedule) Wait . . . wait. What’s this . . . (Points at schedule.) TM?

Vus a dus? TM? (She struggles with pronunciation) Transcendental meditation . . A course in relaxation. (Laughs) I can teach that. How to fall asleep in your chair when the news comes on. You call it TM? I call it Tom Brokaw . . . No . . . wait . . . I’ll take it. (Looks at paper in her hand) It fills a hole for me. What hole? Wednesday. Good. Now I only have six more holes to fill. (Smiles.) You’re laughing. See? That’s because I’m funny, right? I wasn’t always funny, you know. It’s because I took a comedy course last year. You know what was a blast? Mr. Goldenberg, who sat next to me. He had gas problems that kept the whole class awake, you should pardon the expression. A real walking billboard for Gelusil. Oh, we had a special name for him too. Let’s just say it began with “Old” and leave it at that. (Stares at wall).

I see the Yiddish class is filled up. (Laughs) Me? I know Yiddish like the back of my hand. (Looks at hand absentmindedly) Another liver spot. Overnight, they come out. You turn your back on them and they sneak up on you and say, “Peek-a-boo! You’re old!” Just like that (Suddenly tired.) Oy! I’ve got to sit down. (Approaches stool) They don’t make these for a 75-year-old tuchas. Thirty years ago, I could have done this.

Of course, thirty years ago I didn’t wear orthopedic shoes, so I was closer to the ground. I’ve always said the day a woman starts wearing orthopedic shoes, she may as well announce to the world that it’s all over. It’s like getting up on a chair and yelling, “Hey I can’t keep up anymore!” (Lifts up shoes to look at them) Did you ever see anything so mishuga? (Grimaces, then rubs her legs)

Old age? (Defiantly) No. That’s not the problem today. It was the aerobics. I overdid it again. Me and Richard Simmons, we’re an item. He kvetches, I shvitz. (Leans over, conspiratorially) Ever hear him on Howard Stern? (Surprised) You don’t know who Howard Stern is? It’s the most disgusting show. I can’t listen to it for more than an hour at a time. But at least I’m not afraid to listen, like some women I know. I’m hip. That’s what my grandson tells me anyway. See this? (Points to her Grateful Dead T-Shirt).

He bought this for me, my grandson. He calls me Bobby. His father – my son, the attorney – said to him, “Stuart, how do you like your bubbie?” From then on, he calls me Bobby. (Shrugs shoulders) That was eight years ago. I told them to check his hearing, but my daughter-in-law – may she rest in peace – says no, that it’s not my concern. So, what do I care? It’s not my business. I wash my hands of it. I don’t bring it up again with my son’s wife – may she rest in peace . . . Hummm? No, she’s still living, why do you ask? (Pause)

Anyway, my grandson, says to me, “Bobby, you’re one happening mama. Real regular.” Regular. (Pause. Holds up hand) Let’s not even talk about that . . . But, you know, at least I’ve got a life. Not like those other yentas. That’s what Jackie Mason would call them . . . yentas. Sure, I saw his show. Three times. With three different ORT groups. Yeah. And I belong to two Hadassah chapters. Why? For the trips. (Looks up).

Wait, I’ll take that one. What’s is called? “Jews You Didn’t Think Were Jewish.” Maybe they’ll tell me something I don’t know. Like? After all these years – I just learned Jerry Lewis was Jewish. Imagine, Jerry Lewis a Jew. (Frowns) Now exactly what I would call a victory for our side . . .

You know, I could teach a class myself, I’ve taken so many of them . . . What could I teach? I could teach life. A class on how to mother – or how to smother – as my son used to say. He said I knew it better than anyone. Now, I can also teach how to play the bubba. Not that I get such a chance these days. Complaining? No, not me. My kids call like clockwork – if you got a clock that only works twice a year. No, it’s fine. I have my life. Why do I need to mess up theirs?

(Straightens out hem of her shorts) I wouldn’t have time for the kids even if they asked me . . . Besides, with all my courses, you think I could fit them in? I’ve taken crocheting, knitting, sewing . . . anything that ends in an “i-n-g” I take. My son says the only course left is kvetching and I already mastered that.

(Grimace) He’s so funny. If they gave a degree just for me, he says it would be a masters of aggravation. An M.A. because it spells “Ma.” He gets his sense of humor from me.

(Seriously) I’m funny when I have to be. Don’t kid yourself, I know how to laught. But, somehow, it sounds different bounding off the walls in an efficiency apartment when the only noise you hear is yourself sneezing. Wait, I don’t want you to think I don’t have friends. Them I have plenty of. Mrs. Garfinkel, Mrs. Simon, Mrs. Robinson . . . No. Wait. (Pause) She’s dead. Mrs. Robinson’s dead. (Shakes head)

Such a lovely funeral. Everyone turned out. All of her friends from the club. Her husband? He passed on years ago. That’s why she joined the club. Some of these women will do anything to forget, to have company. You make friends.

Friends who last your whole life – whatever’s left of it. Like Mrs. Robinson and me. We were like this. (Entwines her fingers gingerly) Her first name? (Pause) I . . . never asked.

(Changing the subject). Say, is that mime you’re offering again Friday afternoon? I took mime two years ago. Maybe three. Terrible. Terrible. They wouldn’t let me talk. And what’s a class without a little gossip? (Laughs) If I wanted someone who didn’t talk, I’d dig up my dead husband. Fine conversations we used to have. Nu, Saul? How was work? “Nich te fellich,” he’d say. Nu, Saul, what do you think of President Roosevelt’s New Deal? “If it’s good for the Jews, it’s OK by me.” Nu, Saul, what’s the weather like tonight? “Dark.” A scholar he wasn’t

(Softens) No, no. But . . . But, he had his moments. Nu, Saul, what do you think of my new blue dress? (Stops, her eyes moist with memory) “It’s beautiful, Sara. Just like you.” (Grows somewhat softer, smiling a bit) He had a way, my Saul. . . So maybe he wasn’t an Einstein. I never wanted a man with such messy hair anyway. Saul, let’s go to the movies, I’d say. “OK, Sara, if that will make you happy.” He did. He made me happy. He used to listen to me play the piano for hours and then he’d say, “Sara, please don’t stop. I could listen to you forever.” He would always tell me that I was the one in the family with the smarts, with the talent . . .He was the one with the heart . . . Did I tell you about our forth-fifth anniversary?

(Smiles; she seems to be growing younger) You know what he did? He took me dancing. Dancing. For the first time in our lives. Oh, he would step on my feet occasionally – oy, do you know what it’s like to have someone give a shtup to a hammer toe? I said, Saul, Saul, you’re no Fred Astaire. And do you know what he said to me. He said, “Sara, that’s OK, that’s OK, because he only had Ginger Rogers and I have you. For that I’m luckier that Fred Astaire.”

(Smiles). He said that. My Saulie. I guess that’s why I loved him. He swept me off my feet. (listens intently) A prince? He was a king. But . . . (Whisking away imaginary lint from her shorts) . . . even kings don’t live up to their word. And I never forgave him for that. (Listens. ) Hmmm? No, I’d rather not get into it. (Taken aback) Cheat? Did Saul cheat? No. Of course not. He was a Jewish husband. No, my Saulie was a good man . . . How did he lie? (Long pause) What does it matter now?

(Long pause) He always told me that no matter what, “No matter what, Sara,” he said, “I will always be there for you.” My protector, that’s what he called himself. My other lady friends, whose husbands fell asleep on the sofa watching reruns of Love Connection, they’d scream in their ears, trying to wake them up, “Be like Saul! Be like Saul!”

(Softly) Be like Saul.

(Pause) Our children, they grew up, they moved out. I never had time to be lonely because Saul was there for me. Always. “And I always will be,” he told me. And then, just like that, he. . . wasn’t. It wasn’t the way we planned it. Death never is . . It . . . wasn’t the way we planned it at all.

(Directly) Do you know what loneliness is? (Doubtful) Do you? (Shakes head) I’ll tell you what it is. It’s an old lady buying soup for one and freezing half of it. It’s making new lady friends so you have someplace to go on a Saturday. The couples you used to go out with Saturday night you don’t see anymore. The ones who still have husbands don’t want to be reminded what’s in store for them. And those that don’t . . . well . . they just stop calling. You stop calling. Everyone . . . stops. And suddenly, there’s . . . nothing.

(Smiles) No, Saulie, as much as he loved me, he went back on his word. He left me. Alone And I’ll never forgive him for that.

(Sarcastically) So, tell, me, on that big schedule of yours, with all these fancy courses, do you have anyone here who can teach me to deal with that? (Shakes her head, closing her eyes. Long pause. Slowly, sadly, she breaks away from her memories. Back to registrar, brushing back tears.)

So what’s that, Thursday at three? Bungee jumping? (Pause) You jump from a WHAT? (Sighs) All right. Sign me up. Maybe I’ll start out easy . . like getting up from a chair. Look, it couldn’t be worse than physical therapy. I could use a good scream. What have I got to lose? (Looks at her own schedule.) Say, what do you have Monday at one? I’ve got some time to kill. Anything at two? No, how about three? (Nods head as she listens to registrar. Fade to black).
```

---

## IC-0117: Clear Glass Marbles

- Title: Clear Glass Marbles
- Author (byline): Jane Martin
- Work: Talking With
- Publisher: Chilton Books
- Publication date as stated: 1991
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: none
- Teaser before the introduction: Yes
- Spoken words (computed): 1024
- Already set (do not supply): none

### Source block (context only)

```text
Author: Jane Martin
Book: Talking With
ISBN: 1880399202
Publisher: Chilton Books
Date (Month/Year): 1991
FORENSICS AWARDS
2002 National Qualifier – DI – Female
Utah State Finalist
```

### Introduction (context only: never use it for content warnings)

```text
But that’s just what I intend to do today regarding the author of “Clear Glass Marbles” and the question is . . . . Who is Jane Martin? It is a mystery that has confounded the theatre community for over two decades. She has produced over ten full length plays, six one-acts, and numerous shorts. She has been nominated for the Pulitzer prize, and won the American Theatre Critics Association New Play Award twice. Yet, she has not made one public appearance. There are no interviews. No pictures. No sightings. Nothing. She has been called "America's best known unknown playwright." In her absence, retired Actors Theatre of Louisville artistic director Jon Jory has accepted her awards and served as her spokesman. Countless theatrical sleuths have tried to connect the dots, and they all seem to lead to Jory himself.

A clue to at least the “gender” of this elusive author may be found as you contemplate these “Clear Glass Marbles” by Jane Martin (aka Jon Jory?)
```

### Performance text (classify this)

```text
The day my mother found out she was dying she asked me to go out and buy her these clear glass marbles. Dad and I hadn’t even known she was ill. Which was nothing new. Whenever you asked my mother if she was ill she would throw things at you, sesame buns, the editorial page, a handful of hair ribbons. ‘Do not,’ she would say, ‘suggest things to suggestible people.’

I brought her the marbles and she counted out ninety of them and put them in this old cut-glass bowl which had been the sum total of great Aunt Helena’s estate. The doctor had given her three months and she set great store by doctors. She said she always believed them because they were the nearest thing to the Old Testament we had. ‘I wouldn’t give you two bits for these young smiley guys,’ she’d say, ‘I go for a good, stern-furrowed physician.’ She wouldn’t even have her teeth cleaned by a dentist under fifty. So she counted out ninety clear glass marbles and set them in the bowl on her bedside table. Then she went out and spent twelve hundred dollars on nightgowns. She said, ‘In my family you are only dying when you take to your bed, and that, my darlings, is where I am going.’ And she did. Dad said she couldn’t possibly be dying but the doctors convinced him. I told her it seemed a little medieval to just lie up there but she said she didn’t want to be distracted from what she loved. Us.

And she said there was nothing outside except drugstores and supermarkets and drycleaners and that given her situation they were beneath her dignity. I asked her what she intended to do up there and she said study French, visit with us, and maybe call a few pals. Study French. She said she had made a pledge to herself years ago that she would die bilingual.

Dad and I cried a lot, but she didn’t. From then on the doctors had to come see her because, as she put it, she came in with a house call and she was going out with a house call. And all day, every day, she would hold one of these marbles in her hand. Why? She said it made the day longer. Mother had her own bedroom. That was the way it always was, for as long as I can remember. She called my father ‘The Thrasher.’ Dad could really get into a nightmare. Apparently early on in the marriage he had flipped over and broken her nose and that was it. Separate beds. Her room was very spare really. Wooden floors, and old steel-and-brass bed, oak dresser, bedside table, and a hat rack. No pictures on the walls. She never understood how people could look at the same darn thing day after day. She said it was bound to ‘deflate the imagination.’ We’d sit with her after dinner and talk about ‘issues.’ She told us she was too far gone for gossip or what we ate for lunch. Then we’d all go to bed and in a little while, just before I’d drift off I’d hear this…*(drops a marble) Happened every night. After the third of fourth day I saw one on the floor and started to pick it up but she said ‘leave it.’ She said it very sharply. I asked, ‘How come?’ She said she was ‘learning to let go of them.’ * (drops marble)

She made out a list of children’s books from her own childhood and we got as many of them as we could find from the library. She said they were still the only good books she’d ever read. *(drops marble)

She wrote notes to, I don’t know, maybe sixty or seventy people, and they told us later on that they were sort of little formal goodbyes, each of them recalling some incident or shared something, not very significant, but the odd thing was that in each one she included a recipe. A recipe in every one of them.

We got out the big cookie tin full of snapshots that somehow never became a scrapbook. She liked that. She showed my father how to do the medical insurance and how she handled the accounts. We even went through her jewelry. *(drops marble) She wrote down the names of the roofers and plumbers and air-conditioning people. She called it ‘wrapping it up.’ ‘Well, this is good,’ she’d say, ‘I’m wrapping it up.’ * (drops marble)

She had the television moved up in her room and she called aside to say that it was entirely possible that she might reach a stage where she really wouldn’t know what she was watching but that I must promise her her that I’d keep it on P.B.S.

Later on, when it started getting hard, *(drops marble) she told Dad and me that she would like to spend more time alone. ‘I’m afraid,’ she said, ‘that I’m going to have to do this more or less myself.’ She said that she was glad, and she hoped we would be, that this was arranged so that you got less attached to the people you loved at the end. The next period isn’t worth going into, it was just…hard. (pick up bowl of marbles) Do you know that from the very beginning down to the very last she never admitted to any pain. Never. She called it ‘the chills.’ The last thing she asked for was a picture we had in the front entrance hall of a Labrador retriever she and Dad had owned when they were first married. He was, she said, a perfectly dreadful dog. ‘When you are young,’ she said, ‘you believe in the perfection of dogs.’

I was in bed two weeks ago Wednesday toward dawn, then this…(drop all marbles out of bowl, talk when they are done rolling) Dad and I ran in there. The bedside table was turned over and she was gone. Dead. When the emergency medical people got there the found this… (She opens her hand to disclose one more marble) The rest spilled when the table fell, but this one was still in her hand.

I keep it.

I keep it in my hand all day.

It makes the day longer.
```

---

## IC-0118: The Color of Scars

- Title: The Color of Scars
- Author (byline): Florri McMillan
- Work: American Fiction: The Best Unpublished Short Stories by Emerging Writers
- Publisher: Carol Publishing Corporation
- Publication date as stated: July 1990
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: DOCTOR, CONNIE
- Teaser before the introduction: Yes
- Spoken words (computed): 1812
- Already set (do not supply): none

### Source block (context only)

```text
Author: Florri McMillan
Book: American Fiction: The Best Unpublished Short Stories by Emerging Writers
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

DOCTOR: Close your eyes, Constance, and keep them closed

CONNIE: I obey, but my ears cling to the tiny nylon crackles of her uniform. White blots explode-angry spurting flashes against a humming in my brain. Flakes of snow dance flat on a black square; a television set is broken or left on all night, aban-doned by the sleeper.

DOCTOR: Open your eyes, Constance, and keep them open. (Into a tape recorder) This is a thirty-four year old white female ... (To Connie) How many fingers?

CONNIE: (unintelligible response)

DOCTOR: Do you know what day this is?

CONNIE: (unintelligible response) He purses his fat lips into a pink "0", as if he has expected this disappointment.

DOCTOR: What color is this? (holding out the tape recorder)

CONNIE: (to audience) But I do not know what color is. Dr. Francesca nonchalantly squeezes my hand. He studies my face and his eyes are turning black. From their cold depths he searches, listening and probing, for a chink in death, one thin shaft of light. A colorless heat has risen in my brain, spraying little electric bursts that burn out as quickly as they come. (loud cries and unintelligible animal sounds) Charred fumes trickle from my lips; sounds I have never heard. I can smell the residue of rage. All the people in the room are backing away from my bed with horrified eyes, seeking protection in the soft vanilla walls.

DOCTOR: She can't help the shouting. She hardly knows she does it. All short circuits up here, you see (pointing to her temple) She is afraid too, maybe. *****

CONNIE: Mother is allowed to see me for five minutes of each hour. One morning I try to find out what happened. She flutters around the end of the bed, telling me there was a seizure – [a fit, she says]. "What's the matter?" I ask (unintelligible sounds), and she keeps right on talking about how I cannot talk quite, can't understand always, and the artery is broken, yes, deep in there. "Why aren't I dead," I say. (unintelligible sounds) She explains there is a blob of blood, like jello, around the break, covering it over a little. She doesn't know what will happen if the jello melts; yes she supposes it will melt, but not before the operation, she hopes. Her voice is sparrow cheerful, but she picks at the corners of my tucked in blanket, her fingers darting like delicate claws over the wool. ***********************

CONNIE: [After weeks of tests and assessments] they push machines around and arrange my limbs with straps. They [are] going to shoot dye into my brain and take an X-ray. Then we'd know. "Know what?" I asked him.

(unintelligible sounds)

DOCTOR: Don't be afraid.

CONNIE: But he [is] afraid. Everyone in this room is afraid. Dr. Francesca stands close to my head, looking at me. Deliberately I meet his eyes.

DOCTOR: (encouringly as he injects the dye) You can stand anything for four seconds.

CONNIE: (In words and pantomime) I slam rigid into the pain, shooting upward so hard my teeth fuse into my skull; and it crumples, a steel hull destroyed entirely. Its fragments float by, washed away in turquoise. The color is everywhere, so intense that it obliterates me: the I, the eyes, all things, nothing, nothing exists except the color turquoise . . . [and then] I am lying calm in light. There is no weight or color to the air. Water has no ripples. My brain holds no pattern . . . [Dr. Francesca] breaks through the swinging door.. He holds the wet, black square of the X-ray high, in triumph.

DOCTOR: Now I know where it is. Put your index finger on your nose and put the other finger in your ear. Extend the lines until they meet. That's where it is. . . It's a bad place.

CONNIE: (to audience) I know it is in a bad place.. The neurologists have explained that I say "Thursday Thursday Thursday Thursday Thursday Thursday Thursday," instead of the days of the week. At ten in the morning I can talk to Mother. By dark I can only make the hard sounds. "Kick," I can say. Kick, like bones cracking. Most other words are gone, not there anymore. Color is gone. Where are the words? What color is Thursday?

DOCTOR: We'll go in here (indicating a spot on Connie’s temple) And clip here and then ... here (indicating two additional locations on Connie’s head) and hope we can get the thing out without removing too much of the brain.

CONNIE: His eyes are sad when he begins, touching the points where the burl of the electric drill will enter, but by the time he has completed the pattern, they glitter with the hard reflection of challenge.

DOCTOR: I'm confident about this. I'm confident.

CONNIE: He is watching me closely. My head aches with the effort to find a word. I know that I can say kick, kick. "Talk." I say it twice, and Francesca understands. He looks at me without moving for a long time. I wait for an answer.

DOCTOR: You want to go with this operation?

CONNIE: Talk?

DOCTOR: Alive is everything.

CONNIE: (Struggling with the word) Go

DOCTOR: This Thursday, then. ***********

CONNIE: In the dark I hide from Death. I lie very quietly, as wild birds and beggars do, to avoid detection, to be not sufficiently interesting to her. My eyes are always open, spreading wide to find light. It is always black, empty. I am always alone. I stare for days until white begins to flow into my eye sockets, stuffing the holes until it chokes me. I open my mouth to push it back and . . . (scream, again and again in abject fear) Someone is shouting. The rough edges of the voice rip small holes in the black around me. The barked commands tear the darkness into lacy, floating shreds. Beyond them is the Devil's face, surrounded by a ring of light. Dark eyes are glittering. Lips stretch wide against white, flashing teeth. I hear Him laughing, piercing the black with rising, unearthly sound, and then I recognize Dr. Francesca, who has cut his deal-alive is everything

DOCTOR: (shouting) Squeeze my fingers! Squeeze my fingers!

CONNIE: (in words and pantomime) And I reach up to them and grab his hand. (laughter at the accomplishment) Alive is everything. ************

CONNIE: The color of pain is the winter sky, no end and no beginning. The muscles deep in the pit of my stomach are clenched all the time, so tight I cannot make any sound. If I move, the pain will never end. (In obvious pain and in words and pantomime) I lift the top of the tray that swings across my bed. There is a steel mirror underneath. I have not looked at myself since the operation. I expect to see the marks of prolonged pain: ravaged eyes and deep lines around the mouth. I can't take my eyes off my head. There is a wide flat shelf on the right side. And a hole. There is a deep hole the size of a Kennedy half dollar in my head. A thin layer of shiny skin is sucked down into it.. I close my eyes, but I do not cry. ***************

CONNIE: When it is clear to everyone that I am not going to die, they hire Sheila, an R.N. who works at the Rehabilitation Institute across the street. Sheila has special training in physical medicine – [she] nurses people who are too sick for therapy, sort of warming them up for rehabilitation. She won't give me coffee until I walk over to the chair. She asks me questions as long as I can talk. Then, when I am tired, she reads the newspaper out loud. Sheila usually asks me who the people are in the newspaper pictures, but I never recognize any of them. This used to irritate me, but now, sometimes, it makes me feel like weeping. Sheila says I am getting much better, that almost everything I say before lunch makes sense. We name things together. [Bed, newspaper, mirror, light] She is very pleased. She calls the tiny marks on the newspaper "letters." I don't understand letters. Can I make some? she asks, giving me a paper and a pen. Suddenly my fingers are frozen. I can't move them.

When Sheila picks up her pad of paper and the pen it is close to the end of her shift. One afternoon I understand something. "You're writing," I say, and she looks very pleased. It is suddenly clear that the newspaper is "reading." I look at my fingers and say, "I can't write." And I can't read-names or newspapers. I don't know pictures or faces. I won't be able to learn to write, read, which is which. (quietly) "I can't talk." ********* [The next day Dr. Francesca confronts me] *********

DOCTOR: (angrily) Sheila says you won't talk.

CONNIE: His eyes, deep in the sockets, are ignited like live, black coals.

DOCTOR: You can talk.

CONNIE: I stare back, helpless. (to the Doctor) Cat

DOCTOR: Yes you can.

CONNIE: (shaking her head) Cat.

DOCTOR: Try harder.

CONNIE: (shouting and crying) Cat! CAT CAT CAT (to audience) It is so hard to say it. I am panting.

DOCTOR: Can't.

CONNIE: (softly, exhausted) Can't. The water is tickling my cheeks. It is covering softly, not quite warm, washing the dirt from my eye sockets. I can see the blackness receding, flaking away and dripping with the water, out of sight. It rises in my head and then empties itself, until the darkness is washed away.

DOCTOR: Why are you crying?

CONNIE: (speaking haltingly, but clearly for the first time as she wraps her hands around her head) I'm afraid . . . I am afraid. I can't read or write. I can't talk.

DOCTOR: (Peeling her fingers away from her scalp and looking directly into her eyes – moving his fingers over the indentions in her head) You're a living miracle.

CONNIE: (looking up) You did that before. With a red pencil, your finger.

DOCTOR: You remember that? (He fits the ball of his thumb into the hole and presses against the skin.) It doesn't matter what you lost. It's healed now.

CONNIE: [And] I can feel it, feel the edges of my skull soften. ************

CONNIE: Fourteen is not the same as the other floors. Everyone has the same horseshoe-shaped wound on one side of the head, a tribal scar which can never be rubbed out. When I move carefully along the corridor I can see, in 1487, a tiny, shriveled woman with fingers curved into bird claws, so old that her flesh, veined like onion skin, clings tight to the outlines of her skull. A thin ribbon is tied around her scar and a few white tufts on the unshaven side of her head.

Next door there is a handsome boy about eighteen with a stubble growth of beard beginning. The white of his scar glows through his dark brown crew cut. Sheila told me he had a football injury. My eyes met his, but there is no flicker of response. Sheila says he is fine except that he can't walk.

The retarded boy in 1462, next to me, cries all the time. Sometimes his noises are like moaning, other times he sounds like angry, jabbering crows outside a window. Often, in the night, he heaves dry sobs, without tears, until he falls asleep. He has had an operation to relieve his pain. Today he is calling out to someone unnamed in a language no one understands.

(In words and pantomime) I stop in sunlight to examine my fingers. I riffle them like a child playing a hand game, and it seems to me wonderful that I can do this. I lift them slowly, one at a time in sequence and I see the old lady raising her white, fluttering fingers over a piano keyboard; the retarded boy behind a podium, speaking clearly and forcefully; the quarterback cutting down the sideline, dancing out his dream. Moving the fingers of my good working hand, I weep.
```

---

## IC-0119: Cowboys

- Title: Cowboys
- Author (byline): Susan Steinberg
- Work: Spectacle
- Publisher: Graywolf Press
- Publication date as stated: Jan 2013
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: SPEAKER
- Teaser before the introduction: Yes
- Spoken words (computed): 1788
- Already set (do not supply): none

### Source block (context only)

```text
Author: Susan Steinberg
Book: Spectacle
ISBN: 978-1555976316
Publisher: Graywolf Press
Date (Month/Year): Jan 2013
```

### Introduction (context only: never use it for content warnings)

```text
The grief that comes with losing a parent, spouse or sibling after a long illness can be devastating. But there is an additional burden for family members involved in making end-of-life care decisions on behalf of their loved ones. Surrogate decision-makers can be haunted by lingering doubts about whether they made the right choices for family members or may feel guilty about those decisions. They often feel anxious and depressed, and are at significant risk for posttraumatic stress disorder. And the distress is slow to fade. Cowboys by Susan Steinberg
```

### Performance text (classify this)

```text
SPEAKER: There are some who say I did not kill my father. Not technically they mean.

SPEAKER: When the doctor called at four a.m., waked me from a dream I can almost remember, something about chasing dogs in a field, something about a fence, he introduced himself as the doctor. He said, I am doctor such-and-such, in this uptight voice, this deadpan voice. And I laughed and said, You're who. I said, Who is this.

My brother was also on the line. My brother was in Boston. The doctor was in Baltimore. And I was in a place called Warrensburg, Missouri. I was in Warrensburg, Missouri, for a job I was trying to quit. When I mention Warrensburg, Missouri, people say, Where is that. I tell them there are cowboys there. I tell them there are tornadoes that can blow your house across the state. There are brown recluse spiders, I tell them, in every corner of every room. And there I was, trying my best to sleep right through it, a doctor telling me, at four a.m., please, to please be serious.

I was not always serious, and somehow the doctor already knew this, knew perhaps because I laughed when he said he was the doctor. Or perhaps he knew because my brother told him I would not be serious. Or perhaps he knew because when he told me to kill my father, I laughed again. He did not, of course, use the word kill. He had another word, a series of words, a more technical way of wording. The doctor sounded exhausted . . . [He] had been up all night. Trying to save your father, he said. To no avail, he said, and I wondered at the word avail, wondered if the doctor got to be a doctor because of whatever it was he had that made him use that word.

The doctor said my father had flatlined several times. I knew the word flatlined from my ex, who had flatlined three times when we were together. He had flatlined, my ex, because he was an addict, and being an addict, as it turns out, will make you flatline. After the first time, my mother, a nurse, said, He'll never be the same. But he was the same, as it turned out, because he flatlined again. After the third time, we broke up. I'd like to say we broke up because I'd had enough, but really he broke up with me for another woman, a thinner woman, a paler woman, the veins too vivid through her face, and she eventually flatlined too, and she eventually died from this, but he did not. He became a firefighter. I moved to Warrensburg, Missouri. The whole world just went on.

The doctor said my father would be a vegetable, and upon hearing this word, I imagined a plate. I imagined vegetables on this plate. One does not want to imagine this. One wants to imagine one's father running through a field, arms spread, something dynamic like that. Something totally made up like that.

The doctor said my name. He said, Please. My brother said my name. I had a decision to make. I had a serious decision to make, because I was the older kid. Though, as stated, I was not the more serious of the two. And my serious brother, was waiting for me to do the right thing.

This was years ago, and I'm telling you this because the story came to me today for no real reason, just because I happened to see a guy digging through the trash, and I was like, You again. I was like, Get out of there. And I'm telling you this, because some have been wondering why I am the way I am. Which is to say a mess. Which is to say a lot of things.

I could not at first kill my father. I at first said no. I said, Not as long as he's still breathing. But he isn't breathing, said the doctor. Not technically, he said. The doctor sounded fed up. But not fed up with the limitations of science. And not with the limitations of the human body.

The doctor said, A machine is making him breathe. He did not use the word machine. I said I would have to call my mother to get her advice, and my brother said, Don't be a dumbass, and the doctor sighed in that way that the *guys* I have dated since this night sigh when they don't get what they want. Like the restaurant is out of chicken wings. Like the beer is flat. Like I'm trying to convince them I'm a terrible person. The sigh applies pressure to the woman. Then the woman is supposed to give them what they want. Which is to say the woman is then supposed to perform.

Which is to say the woman is then supposed to know the subtle difference between being a woman and performing one.

I said, I'm calling our mother. My mother was in Miami. I disconnected, pressed some buttons, and there was my mother. Then I reconnected, and there we all were. I said, They want me to kill Dad.

My mother had left my father thirty years before. There is no reason to go into the details. I was not calling my mother because she loved my father. I was not even calling her because she was my mother. I was call-ing her because she was a nurse. I hoped that because she was a nurse she would tell me the right thing to do. I'm not talking morally. I'm talking medically. She knew about this.

My mother said, What. My brother said, Tell her. The doctor said, He flatlined. My mother said, You have to kill him. She did not, of course, use these words. I don't know why I'm being so melodramatic. She used technical terms. She said, Take him off the respirator. She said, It's the right thing to do. She said, Trust me. She said, I need to go, though. She said, I need to get to work. She said, I'm sorry. And because I more often than not do the wrong thing, I said fine.

A few days later, because I was older, because the decision was mine, I would donate my father's body to science. I would do this over the phone, and the conversation would be recorded. A woman would ask me questions I had not before this heard. Do you wish to donate the lungs. Do you wish to donate the heart. There were other organs one doesn't think of. There were other things besides organs. The tissue was to go to the tissue bank. The eyes were to go to the eye bank. There were other things I can't remember.

But it was the thought of the eyes removed from the head, the thought of the eyes going their own way, that made me cry. I don't know why this was. I was not suddenly a believer of the soul. I was not suddenly a believer of anything. It was just thinking about it.

And as I cried, the woman said, It's okay, said, Let it out, and I stopped crying and sat there, silent, and the recording went on, just recorded my breathing, the woman's breathing, the sound of static in the phone, and minutes passed. And I thought for some reason of a night years before, me, my father, and my brother in some fast-food place.

My brother was visiting home from college, and he was sticking his French fries into his milk shake, and I said, Sick, and he said, Try it, and I stuck a French fry into the milk shake, and it was amazing. My father was poor then, always poorer the next day, living in some hole, like a hostel, like a hospital, like a halfway house, and my brother said he would take him to dinner. Anywhere you want, he said. My father wanted to go to the fast-food place. He met us there. He was filthy. His shirt was missing buttons. He ordered two cheeseburgers. He ordered onion rings. He ordered an orange soda. He ate too fast. And, watching us stick French fries into the milk shake, he said, You're both sick. But then he tried it too, and then he laughed, and then we ordered more French fries and another milk shake, and what I'm trying to say is, you should try it.

What I'm trying to say is. What I'm trying to say is. . . .

I did not donate the eyes to the eye bank. At some point I said, I can't. The parts that didn't go to science were burned. And, no, I did not want the ashes. I told the woman to send the ashes to my brother. Because my brother was a better person than I was.

There are no more details to tell. There is no reason to go into the why of my father. Or the why of madness, which I cannot answer. Or the why of addiction, which I also cannot answer. Or the why of poor, which I also cannot answer. Suffice it to say it's always about a loss of something. Then a loss of some things. Then a loss of all things. Then he was already dead, some might say. What do you mean, I might say back. If he had already lost everything, some might say, then he was already dead. Yes, I might say. Then you didn't kill him, some might say as they move toward me. That's not the point . . . Then what is . . .

There were late nights he would call from a pay phone, a friend's house, a hospital, and because it was late, and because I was not poor, and because I was not ferociously mad, but, rather, mad mad, a machine answered my phone and lied that I wasn't there eating in bed, watching TV, lied that I would return the call. The machine would then say, Hello, stranger. The machine would then say, It's your father, stranger. There were voices in the background. There was traffic in the background. I'm okay, stranger, the machine would then say. There was screaming in the background. There was me in my bedroom. Pick up the phone, the machine would say loudly. I know you're there, the machine would say louder.

There was me turning the TV all the way up. There was every poor soul looking downward. There was me not believing in the soul. Call it what you will, but there I was, just some poor soul. Same as you.
```

---

## IC-0120: Crafty

- Title: Crafty
- Author (byline): Paul Rudnick
- Work: The New Century (Collection)
- Publisher: Dramatists Play Service
- Publication date as stated: Feb 2009
- Event as filed: Dramatic Interpretation
- Record type: Cutting
- Speaker labels in the text: BARBARA
- Teaser before the introduction: Yes
- Spoken words (computed): 2102
- Already set (do not supply): none

### Source block (context only)

```text
Author: Paul Rudnick
Book: The New Century (Collection)
ISBN: 978-0822223153
Publisher: Dramatists Play Service
Date (Month/Year): Feb 2009
```

### Introduction (context only: never use it for content warnings)

```text
This selection is all about your relationship with your mother, so take a moment to picture her in your mind. What are her hobbies, dreams, feelings? Do you even know? I admit - I’m guilty – Before I worked on this selection, I knew none of these things about my mom. So often we take our mothers for granted. We don’t see them as “real” people – we just see the tiny portion that fits into our lives – Breakfast, dinner, money, someone to listen to what’s going on in OUR lives. We are embarrassed by them, we downplay their importance and we question their intelligence.

But in Crafty by Paul Rudnick . . . we are introduced to Barbara Ellen Diggs, mother to Hank . . . and we find out that she is real – funny and embarrassing sometimes – but so real. Listen carefully to her and then go home and listen to your mom. But more importantly . . . hear her!
```

### Performance text (classify this)

```text
Barbara Ellen Diggs stands in a conference room of a municipal building in Decatur, Illinois.

Barbara Ellen is a sweet-faced, extremely good-natured, outgoing woman, wearing a sweatshirt with a floral applique or a hand knit sweater. She is surrounded by tables holding many homemade craft items.

BARBARA: Hi. I'm Barbara Ellen Diggs, and I'm a craftsperson here in Decatur. And this morning I would like to speak to you on the critical importance of crafts in our culture. Before I discovered crafts, I suffered from clinical depression and had no self-esteem; but today I exhibit my work statewide and I teach workshops at our local women's prison, where a lady who slaughtered her entire family now makes notecards personalized with sequins and dried corn. I have invented over five hundred and twelve different saleables for Christmas bazaars, including doorknob covers, (She holds up a board holding three doorknobs with crocheted holiday covers.) microwave bonnets (She holds up a large quilted microwave bonnet) and toilet paper caddies (She holds up a crocheted cover for a roll of toilet paper.) And I have recently hand-crocheted a tuxedo for my toaster. (She holds up a toaster dressed in a hand crocheted black and white cover with a bowtie.) For wardrobe items I practice applique, which is the art of heat-bonding a felt Santa or a three-dimensional chenille snowman onto a garment. (She holds up a sweatshirt appliqued with a snowman and a Santa.) Last Christmas, across a particularly memorable sweatshirt, I created an entire colonial village, including an ice-skating pond, a blacksmith's shop, and a mischievous Jewish peddler. I also deeply enjoy scrap booking. (She picks up a scrapbook and opens it to a page, showing it to the audience as she points to various features.) For example, on this page, I color-xeroxed a simple Polaroid of my Aunt Polly, and I placed the image at the center of a piece of oaktag. Then I surrounded the picture with heart-shaped lace doilies, crepe-paper rosettes, and silk ribbon worked to spell out "Aunt Polly." I've also included some ticket stubs from a movie we saw together, That Darn Cat, the invitation to her wedding to Uncle Walt, and a tiny burlap bag containing one of her kidney stones. The page now weighs over fifteen pounds, and it can tell you Aunt Polly's entire life story . . . . and I don't even like her.

Some sophisticated people say that crafts aren't art, but by the same token, some people say that New Yorkers aren't people. Crafts allow me to express myself, to create something worth dusting. When I pick up a crochet hook or a staple gun I'm tingling. I'm transported. This one time I started rubber cementing sea shells onto a keepsake box as a baby gift, and by the time I looked up, that child was in college.

My family has always been very supportive of my hobbies, well, except for my son, whom I loved dearly. Hank was always - very special. He always used to scold me for using words like that, what did he call them - euphemisms. He said, Mom, I'm gay. And I said, no you're not, you're special. And he said no, that makes me sound like I'm retarded. And I would say, I wish. And we would laugh. It never really bothered me, even though he did move away and started working for a fancy Broadway costume designer in New York and he didn't come back home all that often. But we would write back and forth, and he would send me trims and braid, all these beautiful expensive things from the costumes and I wouldn't know what to do with them. But to thank him I would send him Hummel figurines, you know, those cute little ceramic children, holding umbrellas or petting kittens, or sitting on a swing. And he'd get so angry on the phone, he'd say Mom, don't send me anything you can order from TV . . . which upset me, so to express that, I sent him the Hummel sad little clown. And he said that Hummels were originally made by Nazis, and I said they were not, they were made by German nuns who didn't read the newspaper. I just liked the picture of all those Hummels, all lined up in his New York studio apartment, to remind him of where he came from. I'd say Hank, maybe you're still wearing white T-shirts and Levi's, but I remember when you didn't shrink them. I told him, if homosexuality is genetic, then maybe so is home shopping.

And then, well, he got sick. With that terrible disease. And I flew to New York to see him in the hospital, and do you know what I brought? Nothing. I didn't want to embarrass him, in front of his friends. Who were all so sweet, I mean, they all sort of sounded alike and they all kept kissing and hugging me and saying, Henry, we love your Mom, she's a hoot. A hoot. That means I wear polyester without irony. But they were all really very nice, and so good to Hank, and when we were finally alone he looked up at me and said, so what did you bring me? A potholder, a picture frame dec-orated with twine and plastic daisies, two little bunnies on a sled? And I said no, I know all of that just upsets you, makes you feel like a hick. And he leaned back onto the pillow and he said, oh. It's okay. I just wanted to see you.

And I stayed there until, well, let's use one of those euphemisms, until he passed on. Maybe that's why euphemisms get invented, not because people are ashamed, but because - they hate the real word too much. And I hated that word, and I hated that disease, and for the longest time I just went to work and came home and I didn't touch a thing. Not a needle, not a bobbin, not a hole punch or a pair of pinking shears. I would not bring color or beauty or rickrack into this world. I was just too sad.

And then one day I saw on the television, that quilt. All spread out in Washington, right on the ground in front of the Capitol. Over seventy-two thousand squares, each for a different man, woman, or child. And I looked at it and I thought, my Lord, it's like a cemetery created by the Ladies Home Journal. And I took all the fancy trims and laces and bugle beads that Hank had sent me, and I went over to Newberry's and I got a rectangle of hot pink felt. And I made his name in embroidered script, and I stitched on one of his report cards and his mittens and one of his T-shirts which said, "No One Knows I'm Gay." Only I changed it so it said, "No One Knows I'm From Decatur." And in the corner I attached one of those labels I always use, that says, "Especially Handmade Just For You By Barbara Ellen Diggs." And I folded up the whole thing and sent it away, so Lord knows where it is now.

But that was ages ago, and now they have all that new medicine, so people, well, at least some people, can keep going. And we've got whole new ways to hurt people, like that 9/11. And I have to tell you something, and you're going to think I'm awful, but when I first heard about it, on TV, and they said Muslim terrorists had attacked those buildings? I swear to God, I thought they said muslin. Muslin terrorists. And I didn't understand and I thought, they're just using cheap cotton? But of course then I found out what it really was, and I saw that all of those people had died and I wondered, will there be a quilt? And I thought, well, probably not in New York, where everyone is so fancy, I thought, maybe they'll make a duvet. I'm sorry.

And about a year or so later, I went back to New York, because I was a finalist in a cake-decorating competition. It was cutthroat. The woman next to me, from Ohio, she was so sure that she was going to win, because she'd baked a five-layer devil's food supreme, frosted with the entire Battle of Gettysburg. She'd used mocha pudding and shredded coconut for the battlefield, and the Union forces were Necco wafers, and the Confederates were all Gummi Bears. But the judges said it was contrived. No comment.

And I thought that maybe I had a shot, for my special Easter Sunday extravaganza. I had frosted a lemon meringue sheet cake with an exact replica of Leonardo DaVinci's "The Last Supper," only instead of the apostles everyone at the table was either a chocolate bunny or a marshmallow peep. But then that Gettysburg woman made a stink, and said that my work was sacrilegious, because I'd included Mary Magdalene, but I said, I know that it's controversial, but she's a peanut M&M!

So I lost, and the city reminded me of Hank, and people said that you could sometimes still smell the, what was it, the jet fuel from that day. And I just couldn't go downtown because it was so terrible, and because that's where Hank lived and so I walked over, from the Marriot, to Central Park. And they were having this, I didn't really know what to call it, but people said it was an installation. By this French artist named Christo. And it seems that this Christo person goes all around the world, and he wraps up landmarks in fabric. I'm not kidding. That's what he does, he pays for it and he gets all of these helpers and all of these sewing machines and they wrap up buildings and islands and bridges. I'm not kidding! And I wondered if maybe, when he was younger, for Christmas, if Christo once gave someone a particularly bulky item, like a bicycle or an outdoor barbeque, and he had to wrap it. Eureka! And in the park, he'd put up hundreds of these sort of archways, these aluminum gates, and from each one, from the top, there was a bright orange curtain. And I thought, well, now I know what an installation is - it's just a giant French crafts project.

And I stood there and the sun came out and the breeze was blowing all of those orange curtains and it didn't make any sense, but it was very pretty. And then I saw this car, this limousine, driving slowly through the park, and this woman next to me, she said that the man in the car was Christo, with his wife, Jean-Claude. And that they drove through all the time, to watch people's reactions. And as the car got closer the window rolled down and inside I could see this little man, Christo, and I waved. And he waved back, and I didn't know what to say, so I just pointed to all of the gates and I said, "Wow! Yardage!" And the car drove past and I asked the woman, I said, does this installation, and all of this orange fabric, does it make people feel better? And I could tell that she was a New Yorker because she said, (She uses a tougher New York voice.) "Yes, it does. Because it's free and they're gonna take it down." And I hadn't really talked about him in so long, especially not to a stranger, but I stood under one of those gates and I told her about Hank. And I asked her if she was there, if she was in the city on 9/11. And she said yes. And I asked, did you lose anyone, and she said yes. That her brother was a firefighter.

And it's strange, but when I got back to Decatur, I started to feel a little cheerier, for the first time in years. My friend Susan Deckerman says that maybe I found closure, and I said, Susan, Oprah is just a person. But I've started to make these sock monkeys (She picks up a pair of sock monkeys from the table.) and I take them to our local hospital and I hang them on the patient's IV stands. Because maybe when a sick person sees a sock monkey, they'll smile.

And that woman I met in New York, in the park, her name is Eileen and we've kept in touch. And after they took those gates down, Eileen got some of the fabric and sent it to me. And so I made this ... (She holds up a bright orange, quilted oven mitt.) It's a quilted oven mitt. And I'm gonna send it to Eileen, with a note that says, "You see? That Christo can make something useful." I don't know if I believe in God anymore. But I do believe in cute. I believe in glue. I believe in hot pink felt. And maybe if I was a New Yorker, I would believe in orange shower curtains hanging in Central Park. Amen.
```
